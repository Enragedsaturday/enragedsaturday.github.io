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

## GROUP: _overhaul2/lake/cases/Smith v. Cain.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Smith v. Cain"
type: case
citation: "565 U.S. 73 (2012)"
parallel_cite: "132 S. Ct. 627; 181 L. Ed. 2d 571"
neutral_cite: 2012 U.S. LEXIS 576
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-01-10
docket: 10-8145
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-01-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Smith v. Cain
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/620666/smith-v-cain/"
  cluster_id: 620666
  opinion_id: 620666
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[Strickler v. Greene]]", "[[Kyles v. Whitley]]", "[[United States v. Bagley]]"]
aliases: []
tags: ["case", "brady", "impeachment", "materiality", "due-process"]
holding: "Modern *Brady* reversal: undisclosed impeachment of the sole eyewitness is material — conviction reversed."
lake:
  record_id: Smith v. Cain
  status: verified
  projected_at: 2026-07-06
---

# Smith v. Cain

*565 U.S. 73 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Juan Smith was convicted of five murders based solely on the testimony of a single eyewitness, Larry Boatner, who told the jury he had "[n]o doubt" Smith was the gunman. The prosecution had not disclosed police notes recording that, on the night of the crime and days later, Boatner said he could not identify anyone. Smith sought relief under *[[Brady v. Maryland|Brady]]*.

## Issue
Whether the State's failure to disclose the eyewitness's contradictory statements was a material *[[Brady v. Maryland|Brady]]* violation.

## Rule
Suppressed impeachment evidence is material when it could reasonably undermine confidence in the verdict. "[E]vidence impeaching an eyewitness may not be material if the State's other evidence is strong enough to sustain confidence in the verdict." — 565 U.S. 73 (2012) (slip op., at 2). ^pin-2

But here "Boatner's undisclosed statements were plainly material." — *Id.* (slip op., at 3). ^pin-3

## Application
Boatner's testimony was the only evidence linking Smith to the crime, and his undisclosed statements—that he "could not ID anyone because [he] couldn't see faces"—directly contradicted his confident trial identification. Because that impeachment was material and the State failed to disclose it, the nondisclosure violated *[[Brady v. Maryland|Brady]]*, and the conviction was reversed.

## Conclusion
The undisclosed impeachment of the sole eyewitness was material; the conviction was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- A modern application of the materiality standard of [[Brady v. Maryland]] and [[Strickler v. Greene]] to impeachment evidence ([[Giglio v. United States]]); see the cumulative-materiality analysis of [[Kyles v. Whitley]] and [[United States v. Bagley]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Smith v. Cain*, 565 U.S. 73 (2012) — https://www.courtlistener.com/opinion/620666/smith-v-cain/ — pinpoints: slip op. 2, 3.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "679cc0e644127402", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Smith v. Cain"}, "payload": {"all": [{"cite": "132 S. Ct. 627", "page": "627", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "132"}, {"cite": "181 L. Ed. 2d 571", "page": "571", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "181"}, {"cite": "565 U.S. 73", "page": "73", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "565"}, {"cite": "2012 U.S. LEXIS 576", "page": "576", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2012"}], "display": "565 U.S. 73", "official": {"cite": "565 U.S. 73", "page": "73", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "565"}, "official_selection_present": true, "record_id": "Smith v. Cain"}}
{"assertion_id": "8388aa7999bded64", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-3", "record_id": "Smith v. Cain"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-3", "pinpoint_status": "slip-only", "quote": "Boatner's undisclosed statements were plainly material.", "quote_fidelity": "mismatch", "record_id": "Smith v. Cain", "star_marker": null}}
{"assertion_id": "99e2e7be55a96859", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-2", "record_id": "Smith v. Cain"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-2", "pinpoint_status": "slip-only", "quote": "Smith was the gunman. The prosecution had not disclosed police notes recording that, on the night of the crime and days later, Boatner said he could not identify anyone. Smith sought relief under *Brady*. ## Issue Whether the State's failure to disclose the eyewitness's contradictory statements was a material *Brady* violation. ## Rule Suppressed impeachment evidence is material when it could reasonably undermine confidence in the verdict.", "quote_fidelity": "mismatch", "record_id": "Smith v. Cain", "star_marker": null}}
{"assertion_id": "0fc3b3114e37f241", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Smith v. Cain"}, "payload": {"as_of_content": "2012-01-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Smith v. Cain", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Smith v. Cain

```json
{
  "schema_version": "s2.v1",
  "record_id": "Smith v. Cain",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Smith v. Cain",
    "case_name_short": "Cain",
    "case_name_full": "Smith v. Cain, Warden",
    "input_case_name": "Smith v. Cain",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-01-10",
    "year": 2012,
    "docket": "10-8145",
    "cluster_id": 620666,
    "lead_opinion_id": 620666,
    "sibling_ids": [
      620666,
      9485187,
      9485188
    ],
    "absolute_url": "/opinion/620666/smith-v-cain/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 73",
      "volume": "565",
      "reporter": "U.S.",
      "page": "73",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 627",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 571",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "571",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 576",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 627",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "627",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "181 L. Ed. 2d 571",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "571",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 73",
        "volume": "565",
        "reporter": "U.S.",
        "page": "73",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 576",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "576",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 73",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 73",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-2",
      "page": null,
      "quote": "Smith was the gunman. The prosecution had not disclosed police notes recording that, on the night of the crime and days later, Boatner said he could not identify anyone. Smith sought relief under *Brady*. ## Issue Whether the State's failure to disclose the eyewitness's contradictory statements was a material *Brady* violation. ## Rule Suppressed impeachment evidence is material when it could reasonably undermine confidence in the verdict.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-3",
      "page": null,
      "quote": "Boatner's undisclosed statements were plainly material.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-01-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Smith v. Cain",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State Ex Rel. Darrell J. Robinson v. Darrel Vannoy, Warden, Louisiana State Penitentiary, Angola, Louisiana",
          "cluster_id": 10292764,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lesley Esther Diamond v. State",
          "cluster_id": 4546474,
          "cite": [
            "561 S.W.3d 288"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lesley Esther Diamond v. State",
          "cluster_id": 4534153,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Santos",
          "cluster_id": 4450366,
          "cite": [
            "176 A.3d 877"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Bartko",
          "cluster_id": 1038291,
          "cite": [
            "728 F.3d 327",
            "2013 WL 4560333",
            "2013 U.S. App. LEXIS 17914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Candelario-Del-Moral v. UBS Financial Services Incorpo",
          "cluster_id": 811754,
          "cite": [
            "699 F.3d 93",
            "2012 WL 5458435",
            "2012 U.S. App. LEXIS 23188"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dennis v. Secretary, Pennsylvania Department of Corrections",
          "cluster_id": 4250271,
          "cite": [
            "834 F.3d 263",
            "2016 U.S. App. LEXIS 15434",
            "2016 WL 4440925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fontenot v. Crow",
          "cluster_id": 4899382,
          "cite": [
            "4 F.4th 982"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wearry v. Cain",
          "cluster_id": 3183098,
          "cite": [
            "577 U.S. 385",
            "136 S. Ct. 1002",
            "194 L. Ed. 2d 78",
            "2016 U.S. LEXIS 1654",
            "84 U.S.L.W. 4125",
            "26 Fla. L. Weekly Fed. S 17",
            "2016 WL 854158"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turner v. United States",
          "cluster_id": 4403802,
          "cite": [
            "582 U.S. 313",
            "2017 U.S. LEXIS 4041",
            "137 S. Ct. 1885",
            "198 L. Ed. 2d 443",
            "26 Fla. L. Weekly Fed. S 700",
            "85 U.S.L.W. 4488",
            "2017 WL 2674152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Barton v. Warden, Southern Ohio Correctional Facility",
          "cluster_id": 2801073,
          "cite": [
            "786 F.3d 450",
            "2015 U.S. App. LEXIS 8020",
            "2015 WL 2262762"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bethel (Slip Opinion)",
          "cluster_id": 6453344,
          "cite": [
            "192 N.E.3d 470",
            "167 Ohio St. 3d 362",
            "2022 Ohio 783"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Harris v. Sheryl Thompson",
          "cluster_id": 810477,
          "cite": [
            "698 F.3d 609",
            "2012 WL 4944325",
            "2012 U.S. App. LEXIS 21727"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Grissom",
          "cluster_id": 824278,
          "cite": [
            "492 Mich. 296",
            "821 N.W.2d 50",
            "2012 Mich. LEXIS 1231"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dolloff",
          "cluster_id": 5146055,
          "cite": [
            "58 A.3d 1032",
            "2012 ME 130",
            "2012 WL 5928662",
            "2012 Me. LEXIS 130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas Lennear v. Eric Wilson",
          "cluster_id": 4655566,
          "cite": [
            "937 F.3d 257"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt v. Pelzer, K.",
          "cluster_id": 2747170,
          "cite": [
            "104 A.3d 267",
            "628 Pa. 193"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miles, Ex Parte Richard Ray Jr.",
          "cluster_id": 2947078,
          "cite": [
            "359 S.W.3d 647",
            "2012 WL 468520",
            "2012 Tex. Crim. App. LEXIS 355"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stellato",
          "cluster_id": 2828959,
          "cite": [
            "74 M.J. 473",
            "2015 CAAF LEXIS 725",
            "2015 WL 4991663"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Bies v. Ed Sheldon",
          "cluster_id": 2763624,
          "cite": [
            "775 F.3d 386",
            "2014 FED App. 0302P",
            "2014 WL 7247396",
            "2014 U.S. App. LEXIS 24242"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Genesis Hill v. Betty Mitchell",
          "cluster_id": 4326477,
          "cite": [
            "842 F.3d 910",
            "2016 FED App. 0281P",
            "96 Fed. R. Serv. 3d 131",
            "2016 U.S. App. LEXIS 21458"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tyjuan Anderson v. City of Rockford, Illinois",
          "cluster_id": 4642953,
          "cite": [
            "932 F.3d 494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Angelo McMullan v. Raymond Booker",
          "cluster_id": 2708508,
          "cite": [
            "761 F.3d 662",
            "2014 WL 3823980",
            "2014 U.S. App. LEXIS 14999"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Behenna",
          "cluster_id": 803734,
          "cite": [
            "71 M.J. 228",
            "2012 CAAF LEXIS 736",
            "2012 WL 2684980"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Floyd v. Darrel Vannoy, Warden",
          "cluster_id": 4510860,
          "cite": [
            "894 F.3d 143"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Coleman",
          "cluster_id": 867087,
          "cite": [
            "72 M.J. 184",
            "2013 WL 1920736",
            "2013 CAAF LEXIS 500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Diaz",
          "cluster_id": 799463,
          "cite": [
            "679 F.3d 1183",
            "2012 WL 1592967",
            "2012 U.S. App. LEXIS 9337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freddie McNeill, Jr. v. Margaret Bagley",
          "cluster_id": 4987267,
          "cite": [
            "10 F.4th 588"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darryl Gumm v. Betty Mitchell",
          "cluster_id": 2763627,
          "cite": [
            "775 F.3d 345",
            "2014 FED App. 0301P",
            "2014 WL 7247393",
            "2014 U.S. App. LEXIS 24245"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Cain:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(620666 OR 9485187 OR 9485188) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 130,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 6,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 130,
        "triage_read": 6,
        "triage_snippet_classified": 124
      },
      "lane2_top_cited": {
        "query": "cites:(620666 OR 9485187 OR 9485188)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yOCZzPTk0MTQ0NzAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28620666+OR+9485187+OR+9485188%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(620666 OR 9485187 OR 9485188)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 1,
        "triage_snippet_classified": 25
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(620666 OR 9485187 OR 9485188)",
    "indexed_citing_opinions": 156,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 620666,
        "count": 105,
        "count_source": "search"
      },
      {
        "opinion_id": 9485187,
        "count": 54,
        "count_source": "search"
      },
      {
        "opinion_id": 9485188,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 418,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/smith-v-cain.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1ODgwNjcmcz05NDU0OTg3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28620666+OR+9485187+OR+9485188%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 620666,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 118307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 620666,
        "cited_id": 145883,
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
    "date_created": "2026-07-05T19:52:04Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:52:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:52:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:56:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:52:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Smith v. Cain

```
(Slip Opinion)              OCTOBER TERM, 2011                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                       SMITH v. CAIN, WARDEN

        CERTIORARI TO THE CRIMINAL DISTRICT COURT OF 

                LOUISIANA, ORLEANS PARISH


 No. 10–8145. Argued November 8, 2011—Decided January 10, 2012
Petitioner Juan Smith was convicted of first-degree murder based on
  the testimony of a single eyewitness. During state postconviction re-
  lief proceedings, Smith obtained police files containing statements by
  the eyewitness contradicting his testimony. Smith argued that the
  prosecution’s failure to disclose those statements violated Brady v.
  Maryland, 373 U. S. 83. Brady held that due process bars a State
  from withholding evidence that is favorable to the defense and mate-
  rial to the defendant’s guilt or punishment. See id., at 87. The state
  trial court rejected Smith’s Brady claim, and the Louisiana Court of
  Appeal and Louisiana Supreme Court denied review.
Held: Brady requires that Smith’s conviction be reversed. The State
 does not dispute that the eyewitness’s statements were favorable to
 Smith and that those statements were not disclosed to Smith. Under
 Brady, evidence is material if there is a “reasonable probability that,
 had the evidence been disclosed, the result of the proceeding would
 have been different.” Cone v. Bell, 556 U. S. 449, 469–470. A “rea-
 sonable probability” means that the likelihood of a different result is
 great enough to “undermine[ ] confidence in the outcome of the trial.”
 Kyles v. Whitley, 514 U. S. 419, 434. Evidence impeaching an eye-
 witness’s testimony may not be material if the State’s other evidence
 is strong enough to sustain confidence in the verdict. United States v.
 Agurs, 427 U. S. 97, 112–113, and n. 21. Here, however, the eyewit-
 ness’s testimony was the only evidence linking Smith to the crime,
 and the eyewitness’s undisclosed statements contradicted his testi-
 mony. The eyewitness’s statements were plainly material, and the
 State’s failure to disclose those statements to the defense thus violat-
 ed Brady. Pp. 2–4.
2                          SMITH v. CAIN

                               Syllabus

Reversed and remanded.

   ROBERTS, C. J., delivered the opinion of the Court, in which SCALIA,
KENNEDY, GINSBURG, BREYER, ALITO, SOTOMAYOR, and KAGAN, JJ.,
joined. THOMAS, J., filed a dissenting opinion.
                        Cite as: 565 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–8145
                                   _________________


JUAN SMITH, PETITIONER v. BURL CAIN, WARDEN
ON WRIT OF CERTIORARI TO THE ORLEANS PARISH CRIMINAL
             DISTRICT COURT OF LOUISIANA
                               [January 10, 2012]

   CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
   The State of Louisiana charged petitioner Juan Smith
with killing five people during an armed robbery. At
Smith’s trial a single witness, Larry Boatner, linked Smith
to the crime. Boatner testified that he was socializing at a
friend’s house when Smith and two other gunmen entered
the home, demanded money and drugs, and shortly there-
after began shooting, resulting in the death of five of
Boatner’s friends. In court Boatner identified Smith as
the first gunman to come through the door. He claimed
that he had been face to face with Smith during the initial
moments of the robbery. No other witnesses and no physi-
cal evidence implicated Smith in the crime.
   The jury convicted Smith of five counts of first-degree
murder. The Louisiana Court of Appeal affirmed Smith’s
conviction. State v. Smith, 797 So. 2d 193 (2001). The
Louisiana Supreme Court denied review, as did this
Court. 2001–2416 (La. 9/13/02), 824 So. 2d 1189; 537 U. S.
1201 (2003).
   Smith then sought postconviction relief in the state
courts. As part of his effort, Smith obtained files from the
2                      SMITH v. CAIN

                     Opinion of the Court

police investigation of his case, including those of the lead
investigator, Detective John Ronquillo. Ronquillo’s notes
contain statements by Boatner that conflict with his tes-
timony identifying Smith as a perpetrator. The notes from
the night of the murder state that Boatner “could not . . .
supply a description of the perpetrators other then [sic]
they were black males.” App. 252–253. Ronquillo also
made a handwritten account of a conversation he had with
Boatner five days after the crime, in which Boatner said
he “could not ID anyone because [he] couldn’t see faces”
and “would not know them if [he] saw them.” Id., at 308.
And Ronquillo’s typewritten report of that conversation
states that Boatner told Ronquillo he “could not identify
any of the perpetrators of the murder.” Id., at 259–260.
  Smith requested that his conviction be vacated, arguing,
inter alia, that the prosecution’s failure to disclose Ron-
quillo’s notes violated this Court’s decision in Brady v.
Maryland, 373 U. S. 83 (1963). The state trial court re-
jected Smith’s Brady claim, and the Louisiana Court of
Appeal and Louisiana Supreme Court denied review. We
granted certiorari, 564 U. S. ___ (2011), and now reverse.
  Under Brady, the State violates a defendant’s right to
due process if it withholds evidence that is favorable to the
defense and material to the defendant’s guilt or punish-
ment. See 373 U. S., at 87. The State does not dispute
that Boatner’s statements in Ronquillo’s notes were fa-
vorable to Smith and that those statements were not dis-
closed to him. The sole question before us is thus whether
Boatner’s statements were material to the determination
of Smith’s guilt. We have explained that “evidence is
‘material’ within the meaning of Brady when there is a
reasonable probability that, had the evidence been dis-
closed, the result of the proceeding would have been dif-
ferent.” Cone v. Bell, 556 U. S. 449, 469–470 (2009). A
reasonable probability does not mean that the defendant
“would more likely than not have received a different
                 Cite as: 565 U. S. ____ (2012)            3

                     Opinion of the Court

verdict with the evidence,” only that the likelihood of a
different result is great enough to “undermine[] confidence
in the outcome of the trial.” Kyles v. Whitley, 514 U. S.
419, 434 (1995) (internal quotation marks omitted).
   We have observed that evidence impeaching an eyewit-
ness may not be material if the State’s other evidence is
strong enough to sustain confidence in the verdict. See
United States v. Agurs, 427 U. S. 97, 112–113, and n. 21
(1976). That is not the case here. Boatner’s testimony
was the only evidence linking Smith to the crime. And
Boatner’s undisclosed statements directly contradict his
testimony: Boatner told the jury that he had “[n]o doubt”
that Smith was the gunman he stood “face to face” with on
the night of the crime, but Ronquillo’s notes show Boatner
saying that he “could not ID anyone because [he] couldn’t
see faces” and “would not know them if [he] saw them.”
App. 196, 200, 308. Boatner’s undisclosed statements
were plainly material.
   The State and the dissent advance various reasons why
the jury might have discounted Boatner’s undisclosed
statements. They stress, for example, that Boatner made
other remarks on the night of the murder indicating that
he could identify the first gunman to enter the house, but
not the others. That merely leaves us to speculate about
which of Boatner’s contradictory declarations the jury
would have believed. The State also contends that Boat-
ner’s statements made five days after the crime can be
explained by fear of retaliation. Smith responds that the
record contains no evidence of any such fear. Again, the
State’s argument offers a reason that the jury could have
disbelieved Boatner’s undisclosed statements, but gives us
no confidence that it would have done so.
   The police files that Smith obtained in state postconvic-
tion proceedings contain other evidence that Smith con-
tends is both favorable to him and material to the verdict.
Because we hold that Boatner’s undisclosed statements
4                      SMITH v. CAIN

                     Opinion of the Court

alone suffice to undermine confidence in Smith’s convic-
tion, we have no need to consider his arguments that the
other undisclosed evidence also requires reversal under
Brady.
   The judgment of the Orleans Parish Criminal District
Court of Louisiana is reversed, and the case is remanded
for further proceedings not inconsistent with this opinion.

                                            It is so ordered.
                 Cite as: 565 U. S. ____ (2012)           1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 10–8145
                         _________________


JUAN SMITH, PETITIONER v. BURL CAIN, WARDEN
ON WRIT OF CERTIORARI TO THE ORLEANS PARISH CRIMINAL
             DISTRICT COURT OF LOUISIANA
                      [January 10, 2012]

   JUSTICE THOMAS, dissenting.
   The Court holds that Juan Smith is entitled to a new
murder trial because the State, in violation of Brady v.
Maryland, 373 U. S. 83 (1963), did not disclose that the
eyewitness who identified Smith at trial stated shortly
after the murders that he could not identify any of the
perpetrators. I respectfully dissent. In my view, Smith
has not shown a “reasonable probability” that the jury
would have been persuaded by the undisclosed evidence.
United States v. Bagley, 473 U. S. 667, 682 (1985) (opinion
of Blackmun, J.). That materiality determination must be
made “in the context of the entire record,” United States v.
Agurs, 427 U. S. 97, 112 (1976), and “turns on the cumu-
lative effect of all such evidence suppressed by the gov-
ernment,” Kyles v. Whitley, 514 U. S. 419, 421 (1995).
Applying these principles, I would affirm the judgment
of the Louisiana trial court.
                             I
   The evidence presented at trial showed the following
facts. On March 1, 1995, Larry Boatner and several
friends gathered at Rebe Espadron’s home in New Or-
leans. Boatner and others were drinking and talking in
the kitchen when Boatner heard the loud sound of a car
without a muffler outside. As Boatner opened the kitchen’s
outside door to investigate the noise, armed men pushed
2                         SMITH v. CAIN

                       THOMAS, J., dissenting

their way through the door, demanding drugs and money.
Tr. 153–154 (Dec. 5, 1995). The first man though the door
put a gun in Boatner’s face and pushed him backwards.
Id., at 154–155. The men initially ordered Boatner and
his friends to the floor, but then ordered Boatner to stand
up. At that time, the man who had been the first one
through the door placed his gun under Boatner’s chin. Id.,
at 156–157. When Boatner asked what the men wanted
him to do, the first man struck Boatner on the back of the
head with his gun, knocking Boatner back to the ground.
Id., at 157–158.
   After hearing the commotion, Espadron emerged from a
back bedroom, where she had been when the men entered
the house. As Espadron opened an inside door leading to
the kitchen, a man with a “covering” over his mouth point-
ed his gun at her face and ordered her to the floor. Id., at
70–71. Disregarding his command, Espadron ran back
toward the bedroom, at which point the intruders opened
fire. Id., at 71–72, 159.
   When the shooting was over, four people lay dead. A
fifth person, 17-year-old Shelita Russell, was mortally
wounded and died later at the hospital. Of those original-
ly gathered in the house, the only survivors were Boatner,
who suffered a severe laceration to his head from the first
man’s blow but was otherwise uninjured; Espadron, who
escaped unharmed; and Reginald Harbor, who had re-
mained in a back bedroom during the shooting. The police
also found a man named Phillip Young at the scene.
Young was alive but had suffered a gunshot wound to the
head. Because Boatner, Espadron, and Harbor had never
seen Young before, the police surmised that Young had
been one of the perpetrators.1
——————
  1 Young was indicted along with Smith for the murders, but he was

deemed incompetent to stand trial due to the brain damage he suffered
                    Cite as: 565 U. S. ____ (2012)                  3

                        THOMAS, J., dissenting

   New Orleans police officer Joseph Narcisse was a first
responder to the scene of the shooting. He testified at trial
that he encountered Boatner in the bathroom of Espa-
dron’s home, where Boatner was attempting to care for the
laceration to his head. According to Narcisse, “Mr. Boat-
ner . . . had let inside the perpetrators and did see them.”
Id., at 21 (Dec. 4, 1995). Narcisse further explained that
Boatner “had a description” of the person that he saw, the
details of which Narcisse could not recall. Id., at 32.
   Detective John Ronquillo, the lead investigator of the
shootings, testified that Boatner had described the first
man through the kitchen door as having a “short-type
haircut,” “a lot of golds in his teeth,” and “brown-ski[n].”2
Id., at 115 (Dec. 5, 1995). Ronquillo further testified that
Boatner could describe no other perpetrator, but that
Boatner had viewed the first man twice: once when the
man initially came through the door and again when
Boatner was ordered to stand up and the man held a gun
to his chin. Id., at 117–118.
   Ronquillo also testified that, during the four months
following the shootings, Boatner viewed 14 six-person
photograph arrays of potential suspects—only one of
which contained a picture of Smith. Id., at 89–100. Three
weeks after the crime, Ronquillo presented Boatner with
one of the arrays that did not include a picture of Smith.
Ronquillo recalled that Boatner noted that one man in the
array had a “similar haircut” and “a similar expression on
his face” as the “gentleman that came into the house
initially with the gun that [Boatner] confronted,” but that

——————
as a result of being shot. 1 Record 49.
  2 “Golds” are permanent or removable mouth jewelry, also referred to

as “grills.” See Mouth Jewelry Wearers Love Gleam of the Grill, South
Florida Sun-Sentinel, Feb. 4, 2007, p. 5, 2007 WLNR 2187080. See also
A. Westbrook, Hip Hoptionary 59 (2002) (defining a “grill” as a “teeth
cover, usually made of gold and diamonds”).
4                       SMITH v. CAIN

                     THOMAS, J., dissenting

Boatner “was positive this wasn’t the individual.” Id., at
97; see also 5 Record 828. A few months later, Ronquillo
presented Boatner with the array that included a photo-
graph of Smith. Tr. 99–101 (Dec. 5, 1995). Ronquillo
testified that Boatner identified Smith “immediately,”
stating, “ ‘This is it. I’ll never forget that face.’ ” Id., at
100. Of the 84 photographs that Boatner viewed, Smith’s
photograph was the only one that Boatner identified.
   Boatner identified Smith again when he was called to
the stand during Smith’s trial. Boatner testified that
Smith’s face was the “[s]ame face,” id., at 174, and that
Smith’s mouth was the “[s]ame mouth” “full of gold,” ibid.,
as that of the first man who came through the kitchen
door on the night of the attack. Boatner also testified that
Smith’s hair at trial was “shaved on the sides” as it was
during the crime, but that “the top was a little bit lower”
at the time of the murders. Id., at 165. Boatner explain-
ed that, during the attack, he had focused on the first
man through the door—who was unmasked—but that he
“didn’t notice” the faces of any of the other assailants or
whether they were masked. Id., at 154. On cross-
examination, Boatner testified that he had described the
first man’s build, haircut, and gold teeth jewelry to the
police. Id., at 178.
   Based on this evidence, the jury convicted Smith of first-
degree murder. Following the conclusion of direct review,
Smith petitioned the trial court for postconviction relief.
Smith argued that the State had failed to disclose various
police notes revealing favorable evidence material to
Smith’s guilt. As relevant here, those items include pre-
trial statements by Boatner; statements by victim Shelita
Russell and Espadron’s neighbor, Dale Mims; a pretrial
statement by firearms examiner Kenneth Leary; state-
ments by cosuspect Robert Trackling and Trackling’s
fellow inmate, Eric Rogers; and a statement by cosuspect
Phillip Young. After holding a 4-day evidentiary hearing,
                 Cite as: 565 U. S. ____ (2012)           5

                    THOMAS, J., dissenting

the postconviction judge—who had also presided over
Smith’s 2-day trial—denied Smith’s Brady claims.
  Like the postconviction court below, I conclude that
Smith is not entitled to a new trial under Brady. In my
view, Smith has not established a reasonable probability
that the cumulative effect of this evidence would have
caused the jury to change its verdict.
                             II

                             A

  Smith first identifies two undisclosed statements by
Boatner, which the Court concludes are “plainly material.”
Ante, at 3. First, a note by Ronquillo, documenting a
conversation he had with Boatner at the scene, states that
Boatner “could not . . . supply a description of the perpe-
trators other th[a]n they were black males.” 5 Record 809.
Second, a handwritten note by Ronquillo, documenting a
phone conversation he had with Boatner on March 6, five
days after the murders, states that “Boatner . . . could not
ID anyone because couldn’t see faces . . . glanced at 1st
one—saw man—through door—can’t tell if had—faces
covered didn’t see anyone . . . Could not ID—would not
know them if—I saw them.” 13 id., at 2515. Ronquillo’s
typed summary of this note states that Boatner advised
him that he “could not identify any perpetrators of the
murder.” 5 id., at 817.
  Smith is correct that these undisclosed statements could
have been used to impeach Boatner and Ronquillo during
cross-examination. But the statements are not material
for purposes of Brady because they cannot “reasonably be
taken to put the whole case in such a different light as to
undermine confidence in the verdict.” Kyles, 514 U. S., at
435. When weighed against the substantial evidence that
Boatner had opportunities to view the first perpetrator,
offered consistent descriptions of him on multiple occa-
sions, and even identified him as Smith, the undisclosed
6                            SMITH v. CAIN

                         THOMAS, J., dissenting

statements do not warrant a new trial.
  The evidence showed that, notwithstanding Ronquillo’s
on-scene note, Boatner offered a description of the perpe-
trator at the scene. Officer Narcisse testified that Boatner
provided him with a description of the perpetrator that
Boatner saw. Narcisse’s testimony thus corroborated
Boatner’s trial testimony that he saw the first man and
described him to police.3 Narcisse’s testimony also miti-
gated the impeachment value of Ronquillo’s on-scene note
by indicating that, although Boatner may have provided
no detailed description to Ronquillo at the scene, Boatner
had described the first man to another officer.4
  In any event, Ronquillo’s notes reflect that Boatner
provided a description of the first perpetrator at the police
station only a few hours after the shootings occurred. Tr.
403 (Jan. 22, 2009). Boatner was asked if he could “de-
scribe the subjects wh[o] shot the people in the house.” 5
Record 866. He responded: “I can tell you about one, the
one who put the pistol in my face, he was a black male
with a low cut, gold[s] in his mouth . . . about my complex-
ion, brown skinned.” Ibid. When asked, “[Y]ou say you


——————
    3 Ina pretrial hearing, Boatner testified that he “gave a description
to the officer that came to the scene.” Tr. 24 (Oct. 27, 1995). Boatner
responded negatively when asked whether this officer was Detective
Ronquillo. Ibid. Boatner further testified that he told the officer that
the first man through the door was “heavy built with his hair with a
fade, with a little small top with a lot of gold teeth in his mouth.” Ibid.
That testimony was consistent with the testimony that Boatner and
Officer Narcisse gave at trial.
  4 Moreover, Boatner’s reticence toward Ronquillo at the scene of the

crime was entirely understandable. As Ronquillo noted at the postcon-
viction hearing, “there were dead bodies everywhere,” and Boatner was
“a little shook up.” Id., at 402–403 (Jan. 22, 2009). Similarly, Narcisse
testified at trial that Boatner, while “not as frantic” as Espadron, was a
“bit emotional” when Narcisse encountered him at the scene. Id., at 34
(Dec. 4, 1995).
                 Cite as: 565 U. S. ____ (2012)            7

                    THOMAS, J., dissenting

can’t describe any of the other shooters besides the one
who put the gun in your face after you opened the door,”
Boatner replied, “No, I can’t.” Ibid. In his brief, Smith
cites this station house statement as an example of favor-
able, undisclosed evidence. But this statement actually
corroborates Boatner’s trial testimony that he saw and
described the first perpetrator to police and that he did not
get a good look at the other assailants. Moreover, the
description Boatner provided was consistent with Smith’s
appearance. The Court completely ignores Boatner’s
station house statement, but our cases instruct us to
evaluate “the net effect of the evidence withheld by the
State” in assessing materiality. See Kyles, supra, at 421–
422.
   The evidence not only shows that Boatner described the
first perpetrator twice in the immediate aftermath of the
crime, but also that Boatner described him again three
weeks later when he viewed a photograph array and elim-
inated a similar-looking individual. The evidence before
the jury further indicated that, several months after the
crime, Boatner confidently identified Smith in an array,
after evincing a discriminating, careful eye over a 4-month
investigative period. What is more, the reliability of
Boatner’s out-of-court identification was extensively tested
during cross-examination at Smith’s trial. In particular,
Boatner was asked whether the fact that he saw Smith’s
picture in a newspaper article naming Smith as a suspect
had tainted his identification. Boatner did not waiver,
responding, “I picked out the person I seen come in that
house that held a gun to my head and under my chin and
the person that was there when all my friends died.” Tr.
190 (Dec. 5, 1995). That Boatner credibly rejected defense
counsel’s “suggestion” theory is supported by the fact that
Boatner did not identify cosuspect Robert Trackling—
whose photograph was included in a separate array shown
to Boatner on the same day that Boatner identified
8                      SMITH v. CAIN

                    THOMAS, J., dissenting

Smith—even though Trackling’s picture was next to
Smith’s in the same newspaper article. 5 Record 833, 835.
   When weighed against Boatner’s repeated and con-
sistent descriptions and confident out-of-court and in-court
identifications, Boatner’s March 6 statement is also imma-
terial. As an initial matter, Ronquillo’s note of his March
6 conversation with Boatner contains an internal contra-
diction that undercuts its impeachment value. Although
the note states that Boatner “didn’t see anyone,” it also
states that Boatner “glanced at 1st one—saw man—
through door.” 13 id., at 2515. The latter part is con-
sistent with Boatner’s repeated statements that he only
saw the first man through the door. Moreover, the jury
would have evaluated any equivocation in Boatner’s
statement in light of the fact that he made it a mere five
days after a traumatic shooting, when the perpetrators
were still at large. The jury would have considered Boat-
ner’s trial testimony that, following the murders of his
friends, he began having nightmares, had difficulty sleep-
ing, quit his job, and began drinking heavily—so much so
that he checked into a hospital for substance abuse treat-
ment and grief counseling. Tr. 162–163, 170–171, 182
(Dec. 5, 1995). Any impeachment value in the March 6
note would have been further mitigated by the fact that,
as Ronquillo explained, “on the night of the incident
[Boatner] said that he could [identify someone] and he
gave a description that was very close to Mr. Smith’s
description.” Id., at 401 (Jan. 22, 2009). And, following
his March 6 conversation with Ronquillo, Boatner viewed
numerous photograph arrays, described the first perpetra-
tor, and ultimately identified him as Smith.
   Of course, had the jury been presented with Ronquillo’s
notes of Boatner’s on-scene and March 6 statements, it
might have believed that Boatner could not identify any of
the perpetrators, but a possibility of a different verdict is
insufficient to establish a Brady violation. See Strickler v.
                  Cite as: 565 U. S. ____ (2012)            9

                     THOMAS, J., dissenting

Greene, 527 U. S. 263, 291 (1999); see also Agurs, 427
U. S., at 109–110 (“The mere possibility that an item of
undisclosed information might have helped the defense, or
might have affected the outcome of the trial, does not es-
tablish ‘materiality’ in the constitutional sense.” Rather,
a “petitioner’s burden is to establish a reasonable prob-
ability of a different result.” Strickler, supra, at 291.
  Instead of requiring Smith to show a reasonable proba-
bility that Boatner’s undisclosed statements would have
caused the jury to acquit, the Court improperly requires
the State to show that the jury would have given Boatner’s
undisclosed statements no weight. See ante, at 3 (“[T]he
State’s argument offers a reason that the jury could have
disbelieved Boatner’s undisclosed statements, but gives us
no confidence that it would have done so”). But Smith
is not entitled to a new trial simply because the jury
could have accorded some weight to Boatner’s undisclosed
statements. Smith’s burden is to show a reasonable prob-
ability that the jury would have accorded those statements
sufficient weight to alter its verdict. In light of the record
as a whole—which the Court declines to consider—Smith
has not carried that burden.
                             B
   Smith also argues that statements by Shelita Russell
and Dale Mims documented in Ronquillo’s handwritten
notes could have been used to impeach Boatner’s identifi-
cation of Smith because the statements indicate that
the perpetrators were masked. One undated note, which
contains several entries about various aspects of the inves-
tigation, states, “female—face down against cabinets—
conscious.” On the next line, the note continues, “said—in
kitchen saw people barge in—one—black cloth across
face—first one through door—[no further statement].” 13
Record 2556. When cross-examined during the postconvic-
tion hearing about whether this note documented the
10                          SMITH v. CAIN

                         THOMAS, J., dissenting

statement of Russell, Ronquillo confirmed that the note
was in his handwriting, but he testified that he never
talked to Russell, that he did not know when the note was
made, and that someone else could have relayed the in-
formation to him. Tr. 415–418 (Jan. 22, 2009).5 I will
assume arguendo that, had this note been disclosed, it
would have been admissible at Smith’s trial as a dying
declaration of Russell.6 But the note would have had
minimal impeachment value because, contrary to Smith’s
assertions, it is ambiguous in light of the context in which
the statement was made. Officer Narcisse testified that
Russell was conscious and able to talk, but that she was in
“bad condition.” Id., at 20 (Dec. 4, 1995). Similarly, Reg-
inald Harbor testified that, as Russell lay wounded, she
was “whining” and he “didn’t catch nothing [t]hat she
said.” Id., at 205 (Dec. 5, 1995). And, although Smith
contends that the note says “exactly” that the “first person
through the door had a black cloth across his face,” that
is not how the note reads. Reply Brief for Petitioner 11
(emphasis deleted; internal quotation marks omitted)
(hereinafter Reply Brief). The note first states that the
declarant “saw people barge in,” then states “one—black


——————
   5 Russell did not make this statement to Officer Narcisse. He testi-

fied that Russell “was not able to give us any information or any details
of what had happened.” Id., at 20.
   6 Louisiana law provides that “[a] statement made by a declarant

while believing that his death was imminent, concerning the cause or
circumstances of what he believed to be his impending death[,]” is “not
excluded by the hearsay rule if the declarant is unavailable as a wit-
ness.” La. Code Evid. Ann., Art. 804(B)(2) (West Supp. 2012). Assum-
ing this statement was actually Russell’s, it likely qualifies as a dying
declaration. At trial, Boatner testified that, in the aftermath of the
shooting, Russell told him, “Feel like I’m about to die.” Tr. 161 (Dec. 5,
1995) (internal quotation marks omitted). Espadron also testified that
Russell told her, “I’m gonna die,” and, “Don’t let me die.” Id., at 73–74
(internal quotation marks omitted).
                     Cite as: 565 U. S. ____ (2012)                  11

                        THOMAS, J., dissenting

cloth across face—first one through door—[no further
statement].” 13 Record 2556 (emphasis added). It is at
least as logical to read this statement as indicating only
that “one” of the “people” had a “black cloth across [his]
face.” Russell, suffering from fatal wounds, said nothing
further after “first one through door,” and it is impossible
to know whether the “first one” was also the “one” with a
“black cloth across [his] face.”
  The second statement Smith identifies is that of Dale
Mims, who lived down the street from Espadron’s home
and who heard the shooting. A note by Ronquillo states
that Mims saw four males fleeing Espadron’s home, “all
wearing mask[s].” Id., at 2518. Like Russell’s purported
statement, this statement has minimal impeachment
value in light of the record. Mims’ undisclosed statement
does not address whether some or all of the perpetrators
were masked inside Espadron’s home.7 Moreover, had
Mims been called as a witness at trial, he presumably
would have testified, as he did at the postconviction hear-
ing, that he was “positive” that he only saw three perpe-
trators fleeing, and that, of those three, only two were
masked. Tr. 269, 271–273, 275 (Jan. 13, 2009).
  Both Russell’s purported statement and Mims’ testimo-
ny are consistent with Boatner’s testimony that he did not
know whether any of the other perpetrators were masked,
id., at 154 (Dec. 5, 1995), and with Officer Narcisse’s and
Espadron’s testimony that the single perpetrator whom
Espadron observed was wearing some sort of face cover-

——————
  7 Smith ridicules the “exceedingly peculiar” notion that the perpetra-

tors would have remained unmasked inside Espadron’s home, only to
mask themselves before leaving the scene. Reply Brief 12–13. But that
notion is eminently reasonable if the perpetrators intended to massacre
the witnesses who were inside the home—as they did—and were
concerned only with disguising themselves from neighbors outside who
might see or hear the burglary.
12                     SMITH v. CAIN

                    THOMAS, J., dissenting

ing, id., at 30–31 (Dec. 4, 1995); id., at 71 (Dec. 5, 1995).
Thus, the totality of the evidence indicates that some, but
not all, of the perpetrators were masked, a conclusion that
in no way undermines Boatner’s consistent assertions that
the only perpetrator he saw was unmasked.
                             C
   Smith also contends that Ronquillo’s undisclosed note
documenting a pretrial statement by firearms examiner
Kenneth Leary is material for purposes of Brady. The
note states that “Leary advised Ronquillo that the 9MM
ammunition confiscated from [the scene of the murders]
was typed to have been fired from a[n] [Intratec], ‘Mac[-]
11’ model type, semi automatic weapon.” 5 Record 831.
According to Smith, this statement conflicts with Leary’s
trial testimony that the 9-millimeter ammunition found
at the scene “was fired by one particular weapon, one 9-
millimeter handgun,” Tr. 132 (Dec. 5, 1995), because an
Intratec or Mac-11 pistol is not a “handgun.” Smith fur-
ther argues that Leary’s pretrial statement could have
been used to exculpate Smith, whose guilt the prosecution
attempted to show by calling a pathologist to testify that
Shelita Russell’s wounds could have been inflicted by a
9-millimeter “handgun,” id., at 39 (Dec. 4, 1995), and by
calling Boatner to testify that the gun Smith held under
his chin was a 9-millimeter silver “hand gun,” id., at 157
(Dec. 5, 1995).
   Contrary to Smith’s contentions, Leary’s pretrial state-
ment does not undermine the evidence presented at trial.
Leary’s pretrial statement is consistent with his and
Boatner’s trial testimony because an Intratec or Mac-11
pistol is a 9-millimeter handgun. Smith concedes that
such a weapon uses 9-millimeter cartridges. Brief for
Petitioner 48. Moreover, a “handgun” is simply “[a] fire-
arm that can be used with one hand,” American Heritage
Dictionary 819 (3d ed. 1992), and no one disputes that an
                     Cite as: 565 U. S. ____ (2012)                   13

                         THOMAS, J., dissenting

Intratec or Mac-11 pistol can be used with one hand.
Smith nonetheless insists that, “as a colloquial matter,
machine pistols of the Intratec or MAC-11 type would be
considered automatic or semiautomatic weapons, rather
than handguns.” Reply Brief 18. But even assuming that
Smith is correct, he fails to explain why Leary, a firearms
expert, would have been expected to use colloquial rather
than technical terminology.8
  The record also makes clear that, when Boatner used
the term “handgun,” he did not understand it to exclude
automatic or semiautomatic machine pistols. In the im-
mediate aftermath of the murders, as well as at trial,
Boatner stated that a second perpetrator carried a “Ma[c]
10” or “Tech Nine” “Uzi” type weapon, Tr. 159, 179 (Dec. 5,
1995); 5 Record 809, 813, 866, and Boatner described that
weapon as a “handgun,” id., at 809. Moreover, Boatner’s
pretrial description of the silver or chrome “handgun” that
the first man held was consistent with Leary’s undisclosed
statement that the gun that fired the 9-millimeter ammu-
nition found at the scene was a semiautomatic weapon. In
his station house statement, Boatner described the first
man’s weapon as a “big,” “automatic pistol.” Id., at 813,
866. Because Leary’s pretrial statement is neither im-
peaching nor exculpatory, Leary’s undisclosed statement
cannot form the basis of a Brady violation. See Strickler,

——————
  8 Smith argues that Leary himself considered an “[Intratec] or ‘Mac[-]
11’ ” model type to be different from a 9-millimeter handgun. Smith
relies on the fact that Leary’s pretrial statement indicated that the
ammunition recovered from the scene did not come from the handgun
recovered from Donielle Bannister, another suspect in the murders.
Id., at 18. Leary’s pretrial statement did not describe the handgun
recovered from Bannister as a 9-millimeter, contrary to Smith’s repre-
sentation. More importantly, Leary’s statement suggests only that
Bannister’s handgun did not fire the 9-millimeter ammunition found at
the scene, not that Leary did not consider an “[Intratec] or ‘Mac[-]11’ ”
model type to be a handgun.
14                     SMITH v. CAIN

                    THOMAS, J., dissenting

527 U. S., at 281–282 (To make out a Brady viola-
tion, “[t]he evidence at issue must be favorable to the
accused, either because it is exculpatory, or because it is
impeaching”).
                              D
   Smith next points to purportedly exculpatory and ma-
terial undisclosed pretrial statements made by Robert
Trackling, a member of the “Cut Throat Posse” street gang
with which Smith was allegedly associated, and by Eric
Rogers, an inmate who was incarcerated with Trackling.
5 Record 845. Police notes reflect that Eric Rogers gave an
interview to investigators on May 19, 1995, during which
he described a conversation that he had with Trackling
while in prison. During that conversation, Trackling
described the murders at Espadron’s home and stated that
he had committed the crime along with “Fat, Buckle, and
a guy they call uh, Short Dog.” Id., at 841. According to
Rogers, Fat’s real name was “Darnell [Donielle] Banister,”
Buckle’s real name was “Contez [Kintad] Phillips,” and
Short Dog’s real name was “Juan.” Id., at 843–844.
   Smith contends that Rogers’ interview was exculpatory
in two respects. First, he points to the following comment
by Rogers later during the interview: “They call Contez
Philip Buckle, they call Darnell Banister Fat, Short Dog
that’s what they call him, they call Robert Home.” Id., at
845. Smith suggests that Rogers’ prior identification of
“Short Dog” as “Juan [Smith]” was equivocal in light of his
later statement that “Short Dog” was a man named “Rob-
ert Home.” Reply Brief 21. Second, Smith asserts that
disclosure of Rogers’ interview would have led the defense
and the jury to learn of Rogers’ allegation—made for the
first time 10 years after Smith’s trial—that the police had
asked him to implicate Juan Smith as “Short Dog,” Tr.
284–285 (Jan. 13, 2009).
   Neither argument is persuasive. If the jury had learned
                    Cite as: 565 U. S. ____ (2012)                  15

                        THOMAS, J., dissenting

of Rogers’ statement, it would have heard information
directly inculpating Smith as “Short Dog,” a perpetrator of
the shootings. Rogers’ physical description of “Short
Dog”—“he[’s] short[,] he[’s] got golds going across his
mouth[,] and . . . he’s like built,” 5 Record 844–also corrob-
orated Boatner’s description of the first man through the
door as having a “mouth full of gold” and a “heavy” build.
Furthermore, Smith ignores other inculpatory information
documented in Ronquillo’s notes of Rogers’ statement.
Those notes reflect Trackling’s own interview with police
on June 1, 1995, in which Trackling identified Phillips,
Bannister, and “Juan Smith” as the perpetrators of the
murders at Espadron’s home. Id., at 832; see also id., at
854–855. Trackling’s statement only strengthens the
inculpatory nature of Rogers’ interview.
  Further, the jury assuredly would not have believed
Smith’s suggestion that Rogers identified “Short Dog” as a
man named “Robert Home.” When this statement is taken
in context, it appears that Rogers was describing the
nickname—“Home”9—of Robert Trackling, the “Robert”
whom Rogers had repeatedly referenced throughout his
interview. See id., at 839–850. Indeed, Rogers’ phrase-
ology, “they call Robert Home,” was consistent with his pre-
vious comments that “[t]hey call Contez Philip Buckle,”
and “they call Darnell Banister Fat.” Id., at 845 (emphasis
added). Unsurprisingly, in the thousands of pages of


——————
   9 See 2 Dictionary of American Regional English 1064–1065, 1069 (F.

Cassidy & J. Hall eds. 1991) (defining “Home” as “a term of address
used by two black people either from the same Southern state or simply
from the South,” similar to “homey” or “home boy”); 2 Green’s Diction-
ary of Slang 828 (2010) (defining “home,” an abbreviation of homeboy,
as “a friend, often used in direct address”); Concise New Partridge
Dictionary of Slang and Unconventional English (T. Dalzell & T. Victor
eds. 2008) (defining “home” as “a very close male friend,” an abbrevia-
tion of “Homeboy”).
16                          SMITH v. CAIN

                         THOMAS, J., dissenting

record material, I have not found, nor have the parties
cited, a single reference to anyone named “Robert Home.”
   If the jury had heard Rogers’ postconviction testimony
that police asked him to implicate Smith and that Track-
ling’s description of the murders did not include Smith, Tr.
284–285 (Jan. 13, 2009), it would have weighed Rogers’
allegation against Trackling’s own statement to the police
that Smith had participated in the murders at Espadron’s
home, 5 Record 832. The prosecution also would have
called Smith’s sister, Trinieze Smith, to testify that she
believed her brother was known as “Short Dog,” as she did
at the postconviction hearing. Tr. 371 (Jan. 14, 2009). On
this record, the undisclosed statements by Rogers and
Trackling actually strengthen rather than weaken confi-
dence in the jury’s guilty verdict.10
                            E
  Finally, Smith argues that an undisclosed handwritten
note by Ronquillo documenting a statement by Phillip
Young—the man found injured at the scene and suspected
of having participated in the crime—is also material evi-
dence warranting a new trial. At trial, Ronquillo testified
that he met with Young while Young was hospitalized as a
result of permanent brain damage suffered in the shoot-


——————
  10 Detective Byron Adams, who took Rogers’ statement, did not testify

at the postconviction hearing because he had died in the meantime. He
thus had no opportunity to address Rogers’ recantation or his newly
minted allegation that Detective Adams asked Rogers to implicate
Smith. Smith argues that “there is no reason to believe that . . . Adams
would have contradicted Rogers—much less that the jury would have
believed [him] if [he] did.” Reply Brief 21. But Smith offers no support
for his dubious assertion that Detective Adams would have admitted to
framing Smith, or that, had the detective denied the allegation, the jury
would have believed Rogers—a convicted murderer who never ex-
plained any motive Adams would have had to frame Smith—over the
detective.
                 Cite as: 565 U. S. ____ (2012)          17

                    THOMAS, J., dissenting

ings. Id., at 102 (Dec. 5, 1995). According to Ronquillo,
Young “was strapped to a chair. He really couldn’t talk,
[h]e mumbled. He could use his left hand, that was all.
He couldn’t walk or anything. He was fed through a tube
by the people there. He was in really bad shape.” Id., at
102–103. When asked whether Young was able to com-
municate with him “at all,” Ronquillo responded, “No. I
couldn’t understand anything that he was saying.” Id., at
103.
  The undisclosed note from Ronquillo’s meeting with
Young reads as follows: “Short Dog/Bucko/Fats—No—
Didn’t shoot me—No—Not with me when went to house—
Yes—one of people in house shot me—No—Not responsi-
ble—‘Posse’—Didn’t drive to house—‘Posse’—Yes—Knows
names of perps—Yes—Drove in car—Yes—girlfriend’s
car.” 13 Record 2568. Smith contends that this note is
exculpatory in that it suggests that he was “not involved”
in the shootings. Brief for Petitioner 43.
  Young’s statement is only exculpatory if Smith concedes
(as the statement asserts) that he is, in fact, “Short Dog”
and a member of the “Cut Throat Posse.” Such a conces-
sion would only have strengthened the inculpatory value
of the statements by Rogers and Trackling indicating that
Smith was the “Short Dog” who committed the murders at
Espadron’s home. In any event, the exculpatory value of
the note is minimal for several other reasons. First, it is
unclear whether Ronquillo’s note reflects a statement by
Young that the “Posse” was not responsible for shooting
the victims or a statement that the “Posse” was not re-
sponsible for shooting Young. Further, the statement that
“Short Dog” and others were not with Young when he went
to the house is certainly not a clear statement that “Short
Dog” did not commit the murders, especially in light of
evidence in the record that the assailants used two cars on
18                         SMITH v. CAIN

                        THOMAS, J., dissenting

the night of the murders.11 Second, had the jury learned
of Ronquillo’s note, it would have presumably heard Ron-
quillo testify, as he did at the postconviction hearing, that
he was not even sure whether his note actually reflected
statements by Young, given that Young “couldn’t talk,”
was “jumbled,” could only “kind of move his head,” and
sometimes would just sit and stare when Ronquillo asked
a question.12 Tr. 423–424 (Jan. 22, 2009). Accordingly,
Ronquillo explained, “I never had hide nor hair actually of
what [Young] said.” Id., at 423.
   The jury thus would have evaluated Ronquillo’s note, of
unclear exculpatory value on its face, against a backdrop
of doubt as to what, if anything, Young actually communi-
cated. The jury also would have weighed this evidence
against the strongly inculpatory nature of Boatner’s de-
scriptions and identifications and Rogers’ and Trackling’s
statements, which corroborated Boatner’s identification.
When all of the evidence is considered cumulatively, as it
must be, Smith has not shown a reasonable probability
that the jury would have reached a different verdict.



——————
  11 In his station house statement, Boatner explained that the loud car
that arrived at Espadron’s home was white. 5 Record 866. In Rogers’
interview with the police, Rogers said that Trackling escaped from
Espadron’s home in a burgundy car. Id., at 842.
   12 Smith also contends that the defense could have used the undis-

closed note to impeach Ronquillo’s trial testimony that Young was not
able to communicate with him “at all.” That argument lacks merit.
Ronquillo’s trial testimony, when read in context, does not suggest that
no communication occurred. Rather, Ronquillo made clear that he
simply “couldn’t understand anything that [Young] was saying.” See Tr.
103 (Dec. 5, 1995) (emphasis added). That testimony is consistent with
the garbled nature of the note, and the note thus would have had little,
if any, impeachment value.
                 Cite as: 565 U. S. ____ (2012)          19

                    THOMAS, J., dissenting

                        *      *    *
   The question presented here is not whether a prudent
prosecutor should have disclosed the information that
Smith identifies. Rather, the question is whether the cu-
mulative effect of the disclosed and undisclosed evidence
in Smith’s case “put[s] the whole case in such a different
light as to undermine confidence in the verdict.” Kyles,
514 U. S., at 435. When, as in this case, the Court departs
from its usual practice of declining to review alleged mis-
applications of settled law to particular facts, id., at 456
(SCALIA, J., joined by Rehnquist, C. J., and KENNEDY and
THOMAS, JJ., dissenting), the Court should at least consid-
er all of the facts. And, the Court certainly should not
decline to review all of the facts on the assumption that
the remainder of the record would only further support
Smith’s claims, as the Court appears to have done here.
Ante, at 3–4.
   Such an assumption is incorrect. Here, much of the
record evidence confirms that, from the night of the mur-
ders through trial, Boatner consistently described—with
one understandable exception—the first perpetrator
through the door, that Boatner’s description matched
Smith, and that Boatner made strong out-of-court and in-
court identifications implicating Smith. Some of the un-
disclosed evidence cited by Smith is not favorable to him
at all, either because it is of no impeachment or exculpa-
tory value or because it actually inculpates him. Because
what remains is evidence of such minimal impeachment
and exculpatory value as to be immaterial in light of the
whole record, I must dissent from the Court’s holding that
the State violated Brady.

```

---

## GROUP: _overhaul2/lake/cases/Smith v. Illinois.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Smith v. Illinois"
type: case
citation: "469 U.S. 91 (1984)"
parallel_cite: "105 S. Ct. 490; 83 L. Ed. 2d 488; 53 U.S.L.W. 3430"
neutral_cite: 1984 U.S. LEXIS 167
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-12-10
docket: 84-5332
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-12-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Smith v. Illinois
  varies_by_point: false
  scope_note: "Good law on its narrow holding; the threshold question whether the initial request was unambiguous is governed by Davis v. United States (1994)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111288/smith-v-illinois/"
  cluster_id: 111288
  opinion_id: 9429796
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny"
related: ["[[Edwards v. Arizona]]", "[[Davis v. United States]]", "[[Miranda v. Arizona]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "invocation", "right-to-counsel"]
holding: "Once an accused unambiguously requests counsel, his postrequest responses to continued interrogation may not be used to cast retrospective doubt on the clarity of that invocation; such later statements bear only on the distinct question of waiver."
lake:
  record_id: Smith v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Smith v. Illinois

*469 U.S. 91 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During custodial interrogation Smith was advised of his [[Miranda and Custodial Interrogation|Miranda rights]]. When told he had the right to a lawyer, Smith responded, "Uh, yeah. I'd like to do that." Rather than stopping, the officers finished the warnings and continued questioning; Smith then made some equivocal remarks and ultimately confessed. The Illinois courts used Smith's later equivocal statements to conclude that his initial request for counsel had not been a clear invocation.

## Issue
Whether an accused's responses to *continued* interrogation, given after he has requested counsel, may be used to determine that the initial request for counsel was ambiguous.

## Rule
No. Under *[[Edwards v. Arizona]]*, once an accused invokes the right to counsel all interrogation must cease until counsel is provided or the accused himself reinitiates and validly waives. The clarity of an invocation is judged on the request and the circumstances leading up to it — not on what the suspect says afterward in response to officers who improperly kept questioning.

"We hold only that, under the clear logical force of settled precedent, an accused's *postrequest* responses to further interrogation may not be used to cast retrospective doubt on the clarity of the initial request itself. Such subsequent statements are relevant only to the distinct question of waiver." — 469 U.S. at 100. ^pin-100

## Application
Smith's statement — "Uh, yeah. I'd like to do that" — was, in context, a request for counsel, and questioning should have stopped. The state courts erred by mining his *later* equivocal answers (made only because interrogation wrongly continued) to recharacterize the initial request as ambiguous. Those later answers could bear only on whether Smith waived a right he had already invoked, not on whether he invoked it.

## Conclusion
Postrequest responses cannot be used to make an otherwise clear invocation ambiguous. The judgment of the Illinois Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. (The Court expressly left open how to treat a request that is ambiguous from the outset — later answered in *Davis v. United States*.)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Smith*'s narrow holding stands. The threshold question it reserved — what counts as an unambiguous invocation, and whether officers must clarify an ambiguous one — was decided by [[Davis v. United States]] (no duty to clarify; the request must itself be unambiguous).

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny*

## Sources
- *Smith v. Illinois*, 469 U.S. 91 (1984) (per curiam) — https://www.courtlistener.com/opinion/111288/smith-v-illinois/ — pinpoint: 100.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b043c6230e8f6e2c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Smith v. Illinois"}, "payload": {"all": [{"cite": "469 U.S. 91", "page": "91", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "469"}, {"cite": "105 S. Ct. 490", "page": "490", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "83 L. Ed. 2d 488", "page": "488", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "1984 U.S. LEXIS 167", "page": "167", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "53 U.S.L.W. 3430", "page": "3430", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "53"}], "display": "469 U.S. 91", "official": {"cite": "469 U.S. 91", "page": "91", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "469"}, "official_selection_present": true, "record_id": "Smith v. Illinois"}}
{"assertion_id": "42c1c1cce0dffae0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-100", "record_id": "Smith v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-100", "pinpoint_status": "slip-only", "quote": "Rather than stopping, the officers finished the warnings and continued questioning; Smith then made some equivocal remarks and ultimately confessed. The Illinois courts used Smith's later equivocal statements to conclude that his initial request for counsel had not been a clear invocation. ## Issue Whether an accused's responses to *continued* interrogation, given after he has requested counsel, may be used to determine that the initial request for counsel was ambiguous. ## Rule No. Under *Edwards v. Arizona*, once an accused invokes the right to counsel all interrogation must cease until counsel is provided or the accused himself reinitiates and validly waives. The clarity of an invocation is judged on the request and the circumstances leading up to it — not on what the suspect says afterward in response to officers who improperly kept questioning.", "quote_fidelity": "mismatch", "record_id": "Smith v. Illinois", "star_marker": null}}
{"assertion_id": "abf76da250c77df5", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Smith v. Illinois"}, "payload": {"as_of_content": "1984-12-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Smith v. Illinois", "scope_note": "Good law on its narrow holding; the threshold question whether the initial request was unambiguous is governed by Davis v. United States (1994).", "varies_by_point": false}}
```

### lake record — Smith v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Smith v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Smith v. Illinois",
    "case_name_short": "",
    "case_name_full": "Smith v. Illinois",
    "input_case_name": "Smith v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-12-10",
    "year": 1984,
    "docket": "84-5332",
    "cluster_id": 111288,
    "lead_opinion_id": 9429796,
    "sibling_ids": [
      111288,
      9429796,
      9429797
    ],
    "absolute_url": "/opinion/111288/smith-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 91",
      "volume": "469",
      "reporter": "U.S.",
      "page": "91",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 490",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 488",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 3430",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "3430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 167",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 91",
        "volume": "469",
        "reporter": "U.S.",
        "page": "91",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 490",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "490",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 488",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "488",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 167",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "167",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 U.S.L.W. 3430",
        "volume": "53",
        "reporter": "U.S.L.W.",
        "page": "3430",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 91",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 91",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-100",
      "page": null,
      "quote": "Rather than stopping, the officers finished the warnings and continued questioning; Smith then made some equivocal remarks and ultimately confessed. The Illinois courts used Smith's later equivocal statements to conclude that his initial request for counsel had not been a clear invocation. ## Issue Whether an accused's responses to *continued* interrogation, given after he has requested counsel, may be used to determine that the initial request for counsel was ambiguous. ## Rule No. Under *Edwards v. Arizona*, once an accused invokes the right to counsel all interrogation must cease until counsel is provided or the accused himself reinitiates and validly waives. The clarity of an invocation is judged on the request and the circumstances leading up to it \u2014 not on what the suspect says afterward in response to officers who improperly kept questioning.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-12-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Smith v. Illinois",
    "varies_by_point": false,
    "scope_note": "Good law on its narrow holding; the threshold question whether the initial request was unambiguous is governed by Davis v. United States (1994).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Tellez-Suarez",
          "cluster_id": 10134379,
          "cite": [
            "312 Or. App. 531",
            "493 P.3d 28"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nader Abdallah",
          "cluster_id": 4574399,
          "cite": [
            "911 F.3d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kevin Jones, Jr. v. K. Harrington",
          "cluster_id": 4240929,
          "cite": [
            "829 F.3d 1128",
            "2015 U.S. App. LEXIS 23120",
            "2016 WL 3947820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Francisco Garcia v. David Long",
          "cluster_id": 3164323,
          "cite": [
            "808 F.3d 771",
            "2015 U.S. App. LEXIS 22205",
            "2015 WL 9267557"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2830722,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 2828358,
          "cite": [
            "413 S.C. 458",
            "776 S.E.2d 367",
            "2015 S.C. LEXIS 302"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ryan E. Bean v. State of Indiana",
          "cluster_id": 2729695,
          "cite": [
            "973 N.E.2d 35",
            "2012 WL 3598405",
            "2012 Ind. App. LEXIS 403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
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
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pecina v. State",
          "cluster_id": 2292956,
          "cite": [
            "326 S.W.3d 249",
            "2010 Tex. App. LEXIS 5631",
            "2010 WL 2825663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Ramirez",
          "cluster_id": 3145133,
          "cite": [
            "402 Ill. App. 3d 638",
            "343 Ill. Dec. 405",
            "934 N.E.2d 1008",
            "2010 Ill. App. LEXIS 587"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane1_negative"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muniz v. State",
          "cluster_id": 1471480,
          "cite": [
            "851 S.W.2d 238",
            "1993 Tex. Crim. App. LEXIS 5",
            "1993 WL 871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 1890892,
          "cite": [
            "313 S.W.3d 317",
            "2010 Tex. Crim. App. LEXIS 723",
            "2010 WL 2382567"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. State",
          "cluster_id": 2382336,
          "cite": [
            "504 A.2d 1096",
            "1986 Del. LEXIS 1040"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
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
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. State",
          "cluster_id": 2459967,
          "cite": [
            "919 S.W.2d 370",
            "1996 Tex. Crim. App. LEXIS 35",
            "1994 WL 706957"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Duff",
          "cluster_id": 2651723,
          "cite": [
            "58 Cal. 4th 527",
            "317 P.3d 1148",
            "167 Cal. Rptr. 3d 615",
            "2014 WL 321872",
            "2014 Cal. LEXIS 637"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1784340,
          "cite": [
            "587 So. 2d 848",
            "1991 WL 178413"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Billy Russell Clark v. Tim Murphy",
          "cluster_id": 782256,
          "cite": [
            "331 F.3d 1062",
            "2003 Cal. Daily Op. Serv. 4923",
            "2003 Daily Journal DAR 6263",
            "2003 U.S. App. LEXIS 11496",
            "2003 WL 21338911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Martinez",
          "cluster_id": 2637824,
          "cite": [
            "47 Cal. 4th 911",
            "10 Cal. Daily Op. Serv. 583",
            "224 P.3d 877",
            "105 Cal. Rptr. 3d 131",
            "2010 Cal. LEXIS 111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balfour v. State",
          "cluster_id": 1858937,
          "cite": [
            "598 So. 2d 731",
            "1992 WL 64497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montoya v. State",
          "cluster_id": 1529929,
          "cite": [
            "744 S.W.2d 15",
            "1987 Tex. Crim. App. LEXIS 681",
            "1987 WL 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Etheridge v. State",
          "cluster_id": 2372478,
          "cite": [
            "903 S.W.2d 1",
            "1994 Tex. Crim. App. LEXIS 83",
            "1994 WL 273325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. San Nicolas",
          "cluster_id": 2507905,
          "cite": [
            "101 P.3d 509",
            "21 Cal. Rptr. 3d 612",
            "34 Cal. 4th 614",
            "2004 Daily Journal DAR 14410",
            "2004 Cal. Daily Op. Serv. 10643",
            "2004 Cal. LEXIS 11655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duplantis v. State",
          "cluster_id": 1659824,
          "cite": [
            "644 So. 2d 1235",
            "1994 WL 590825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111288 OR 9429796 OR 9429797) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjc1MzUwNDAwMDAwJnM9MTQ3NTI5JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111288+OR+9429796+OR+9429797%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111288 OR 9429796 OR 9429797)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODAmcz0xMjAyNTMzJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111288+OR+9429796+OR+9429797%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111288 OR 9429796 OR 9429797)",
        "reviewed": 34,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 34,
        "triage_read": 0,
        "triage_snippet_classified": 34
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111288 OR 9429796 OR 9429797)",
    "indexed_citing_opinions": 751,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111288,
        "count": 658,
        "count_source": "search"
      },
      {
        "opinion_id": 9429796,
        "count": 112,
        "count_source": "search"
      },
      {
        "opinion_id": 9429797,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1228,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/smith-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NDIzODMmcz05NDkxMzY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111288+OR+9429796+OR+9429797%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111288,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 368063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 1161267,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 1259486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 1773695,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 2087192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 2090485,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111288,
        "cited_id": 2190311,
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
    "date_created": "2026-07-05T19:56:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:56:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:56:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:59:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:56:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Smith v. Illinois

```
<opinion type="majority">
<author id="b233-10">Per Curiam.</author>
<p id="b233-11">The petitioner Steven Smith was convicted of armed robbery and sentenced to a 9-year prison term. He contends that the police improperly elicited a confession from him after he clearly had requested the assistance of counsel, and that <page-number citation-index="1" label="92">*92</page-number>the trial court’s refusal to suppress the confession therefore violated <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981). The Illinois Supreme Court held that Smith’s responses to continued police questioning rendered his initial request for counsel “ambiguous,” and that the officers therefore were not required to terminate their questioning. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith">102 Ill. 2d 365, 373-374</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d 236, 240</a></span> (1984). Under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>however, an accused’s postrequest responses to further interrogation may not be used to cast doubt on the clarity of his initial request for counsel. Finding no ambiguity in Smith’s initial request, we accordingly grant the petition and reverse.</p>
<p id="b234-5">I</p>
<p id="b234-6">Shortly after his arrest, 18-year-old Steven Smith was taken to an interrogation room at the Logan County Safety Complex for questioning by two police detectives. The session began as follows:</p>
<blockquote id="b234-7">“Q. Steve, I want to talk with you in reference to the armed robbery that took place at McDonald’s restaurant on the morning of the 19th. Are you familiar with this?</blockquote>
<blockquote id="A6q">“A. Yeah. My cousin Greg was.</blockquote>
<blockquote id="b234-8">“Q. Okay. But before I do that I must advise you of your rights. Okay? You have a right to remain silent. You do not have to talk to me unless you want to do so. Do you understand that?</blockquote>
<blockquote id="b234-9">“A. Uh. She told me to get my lawyer. She said you guys would railroad me.[<footnotemark>1</footnotemark>]</blockquote>
<blockquote id="b234-10">“Q. Do you understand that as I gave it to you, Steve?</blockquote>
<blockquote id="Ayg">“A. Yeah.</blockquote>
<blockquote id="b235-4"><page-number citation-index="1" label="93">*93</page-number>“Q. If you do want to talk to me I must advise you that whatever you say can and will be used against you in court. Do you understand that?</blockquote>
<blockquote id="b235-5">“A. Yeah.</blockquote>
<blockquote id="b235-6">“Q. You have a right to consult with a lawyer and to have a lawyer present with you when you’re being questioned. Do you understand that?</blockquote>
<blockquote id="b235-7">“A. <em>Uh, yeah. I’d like to do that.</em></blockquote>
<blockquote id="b235-8">“Q. Okay.” 102 111. 2d, at 368-369, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span> (emphasis in opinion).</blockquote>
<p id="b235-9">Instead of terminating the questioning at this point, the interrogating officers proceeded to finish reading Smith his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and then pressed him again to answer their questions:</p>
<blockquote id="b235-10">“Q. ... If you want a lawyer and you’re unable to pay for one a lawyer will be appointed to represent you free of cost, do you understand that?</blockquote>
<blockquote id="b235-11">“A. Okay.</blockquote>
<blockquote id="b235-12">“Q. Do you wish to talk to me at this time without a lawyer being present?</blockquote>
<blockquote id="b235-13">“A. <em>Yeah and no, uh, I don’t know what’s what, really.</em></blockquote>
<blockquote id="Af">“Q. <em>Well. You either have [to agree] to talk to me this time without a lawyer being present </em>and if you do agree to talk with me without a lawyer being present you can stop at any time you want to.</blockquote>
<blockquote id="b235-14">“Q. All right. I’ll talk to you then.” <em>Id., </em>at 369, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span> (emphasis in opinion) (bracketed words appear in Tr. 230).</blockquote>
<p id="b235-15">Smith then told the detectives that he knewin advance about the planned robbery, but contended that he had not been a participant. After considerable probing by the detectives, Smith confessed that “I committed it,” but he then returned to his earlier story that he had only known about the planned crime. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#369" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 369-370</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span>. Upon further <page-number citation-index="1" label="94">*94</page-number>questioning, Smith again insisted that “I wanta get a lawyer.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#370" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 370</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#238" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 238</a></span>. This time the detectives honored the request and terminated the interrogation.</p>
<p id="b236-5">Smith moved at trial to suppress his incriminating statements, 1 Record 45, but the trial judge denied the motion, 4 Record 231. A transcript of the interrogation was introduced as part of the State’s case in chief, and Smith was convicted.</p>
<p id="b236-6">In affirming Smith’s conviction, the Appellate Court of Illinois for the Fourth District acknowledged that Smith’s first request for counsel “appears clear and unequivocal.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d 305, 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d 556, 559</a></span> (1983). The court concluded, however, that “when [the request] is considered with other statements — as it should be — it is clear that Smith was undecided about exercising his right to counsel” and “never made an effective request for counsel.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#309" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 309-310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#558" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 558-559</a></span>. Rather, Smith had made “merely an indecisive inquiry into the right to counsel.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 559</a></span>.</p>
<p id="b236-7">The Illinois Supreme Court affirmed in a 4-3 vote. The majority agreed with the lower court that “Smith’s statements, considered in total, were ambiguous, and did not effectively invoke his right to counsel.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span>. Specifically, the majority noted that although Smith stated “I’d like to do that” upon learning he had a right to his counsel’s presence at the interrogation, Smith <em>subsequently </em>replied “Yeah and no, uh, I don’t know what’s what really,” and “All right. I’ll talk to you then.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#372" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 372</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span>. In light of these subsequent remarks, the majority reasoned, “Steven Smith did not <em>dearly assert </em>his right to counsel.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span> (emphasis in original).</p>
<p id="b236-8">II</p>
<p id="b236-9">An accused in custody, “having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made <page-number citation-index="1" label="95">*95</page-number>available to him,” unless he validly waives his earlier request for the assistance of counsel. <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>.<footnotemark>2</footnotemark> This “rigid” prophylactic rule, <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 719</a></span> (1979), embodies two distinct inquiries. First, courts must determine whether the accused actually invoked his right to counsel. See, <em>e. g., Edwards </em>v. <em>Arizona, supra, </em>at 484-485 (whether accused “expressed his desire” for, or “clearly asserted” his right to, the assistance of counsel); <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444-445</a></span> (whether accused “indicate[d] in any manner and at any stage of the process that he wish[ed] to consult with an attorney before speaking”). Second, if the accused invoked his right to counsel, courts may admit his responses to further questioning only on finding that he (a) initiated further discussions with the police, and (b) knowingly and intelligently waived the right he had invoked. <em>Edwards </em>v. <em>Arizona, supra, </em>at 485, 486, n. 9.</p>
<p id="b237-5">This case concerns the threshold inquiry: whether Smith invoked his right to counsel in the first instance. On occasion, an accused’s asserted request for counsel may be ambiguous or equivocal. As the majority and dissenting opinions below noted, courts have developed conflicting standards for determining the consequences of such ambiguities. See <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#372" aria-description="Citation for case: People v. Smith">102 <page-number citation-index="1" label="96">*96</page-number>Ill. 2d, at 372-373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span>; <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#375" aria-description="Citation for case: People v. Smith"><em>id., </em>at 375-377</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#241" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 241-242</a></span> (Simon, J., dissenting).<footnotemark>3</footnotemark> We need not resolve this conflict in the instant case, however, because the judgment of the Illinois Supreme Court must be reversed irrespective of which standard is applied.</p>
<p id="b238-5">The conflict among courts is addressed to the relevance of alleged ambiguities or equivocations that either (1) <em>precede </em>an accused’s purported request for counsel, or (2) are part of the request <em>itself. </em>Neither circumstance pertains here, however. Neither the State nor the courts below, for example, have pointed to anything Smith previously had said that might have cast doubt on the meaning of his statement “I’d like to do that” upon learning that he had the right to his counsel’s presence.<footnotemark>4</footnotemark> Nor have they pointed to anything <page-number citation-index="1" label="97">*97</page-number>inherent in the nature of Smith’s actual request for counsel that reasonably would have suggested equivocation. As Justice Simon noted in his dissent below, “with the possible exception of the word ‘uh’ the defendant’s statement in this case was neither indecisive nor ambiguous: ‘Uh, yeah, I’d like to do that.’” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#377" aria-description="Citation for case: People v. Smith"><em>Id., </em>at 377</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#242" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 242</a></span>. And the Illinois Appellate Court for the Fourth District itself acknowledged that the statement “appears clear and unequivocal.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d, at 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 559</a></span>.<footnotemark>5</footnotemark></p>
<p id="b239-5">The courts below were able to construe Smith’s request for counsel as “ambiguous” <em>only </em>by looking to Smith’s <em>subsequent </em>responses to continued police questioning and by concluding that, “considered in total,” Smith’s <em>“statements” </em>were equivocal. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#373" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 373</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#240" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 240</a></span> (emphasis added); see also <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#310" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d, at 310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#559" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 559</a></span>.<footnotemark>6</footnotemark> This line of analysis is unprecedented and untenable. As Justice Simon emphasized below, “[a] statement either is <page-number citation-index="1" label="98">*98</page-number>such an assertion [of the right to counsel] or it is not.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#375" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 375</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#241" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 241</a></span>. Where nothing about the request for counsel or the circumstances leading up to the request would render it ambiguous, all questioning must cease. In these circumstances, an accused’s subsequent statements are relevant only to the question whether the accused waived the right he had invoked. Invocation and waiver are entirely distinct inquiries, and the two must not be blurred by merging them together.<footnotemark>7</footnotemark></p>
<p id="b240-5">The importance of keeping the two inquiries distinct is manifest. <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>set forth a “bright-line rule” that <em>all </em>questioning must cease after an accused requests counsel. <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#646" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 646</a></span> (1984). In the absence of such a bright-line prohibition, the authorities through “badger[ing]” or “overreaching” — explicit or subtle, deliberate or unintentional — might otherwise wear down the accused and persuade him to incriminate himself notwithstanding his earlier request for counsel’s assistance. <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S., at 719</a></span>. With respect to the waiver inquiry, we accordingly have emphasized that a valid waiver “cannot be established by showing only that [the accused] responded to further police-initiated custodial interrogation.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>. Using an accused’s subse<page-number citation-index="1" label="99">*99</page-number>quent responses to cast doubt on the adequacy of the initial request <em>itself </em>is even more intolerable. “No authority, and no logic, permits the interrogator to proceed ... on his own terms and as if the defendant had requested nothing, in the hope that the defendant might be induced to say something casting retrospective doubt on his initial statement that he wished to speak through an attorney or not at all.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#376" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 376</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#241" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 241</a></span> (Simon, J., dissenting).<footnotemark>8</footnotemark></p>
<p id="b241-5">Ill</p>
<p id="b241-6">Our decision is a narrow one. We do not decide the circumstances in which an accused’s request for counsel may be <page-number citation-index="1" label="100">*100</page-number>characterized as ambiguous or equivocal as a result of events preceding the request or of nuances inherent in the request itself, nor do we decide the consequences of such ambiguity or equivocation. We hold only that, under the clear logical force of settled precedent, an accused’s <em>postrequest </em>responses to further interrogation may not be used to cast retrospective doubt on the clarity of the initial request itself. Such subsequent statements are relevant only to the distinct question of waiver.</p>
<p id="b242-5">Accordingly, Smith’s motion for leave to proceed <em>informa pauperis </em>is granted, the petition for a writ of certiorari is granted, the judgment of the Illinois Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b242-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b234-11"> According to the Illinois Supreme Court, the “she” that Smith referred to was an unidentified woman named Chico. <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#368" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 368-369</a></span>, 466 N. E. 2d. at 238.</p>
</footnote>
<footnote label="2">
<p id="b237-6"> We have repeatedly emphasized this restraint on police interrogation. In addition to <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>see also <em>Solem </em>v. <em>Stumes, </em><span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#646" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 646-647</a></span> (1984); <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1044</a></span> (1983) <em>(Edwards </em>set forth a “prophylactic rule, designed to protect an accused in police custody from being badgered by police officers . . .”); <em>Wyrick </em>v. <em>Fields, </em><span class="citation" data-id="9428961"><a href="/opinion/110809/wyrick-v-fields/#45" aria-description="Citation for case: Wyrick v. Fields">459 U. S. 42, 45-46</a></span> (1982) <em>(per curiam); Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#298" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 298</a></span> (1980); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 719</a></span> (1979) (discussing the “rigid rule” that “an accused’s request for an attorney is <em>per se </em>an invocation of his Fifth Amendment rights, requiring that all interrogation cease”); <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 474</a></span> (1966) (“If the individual states that he wants an attorney, the interrogation must cease until-an attorney is present”). Cf. <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#105" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 105-106</a></span> (1975) (rule requiring termination of questioning upon accused’s invocation of his right to silence prevents police from “persisting in repeated efforts to wear down [the accused’s] resistance and make him change his mind”).</p>
</footnote>
<footnote label="3">
<p id="b238-6"> Some courts have held that all questioning must cease upon any request for or reference to counsel, however equivocal or ambiguous. See, <em>e. g., People </em>v. <em>Superior Court, </em><span class="citation" data-id="1161267"><a href="/opinion/1161267/people-v-superior-court-zolnay/#735" aria-description="Citation for case: People v. Superior Court (Zolnay)">15 Cal. 3d 729, 735-736</a></span>, <span class="citation" data-id="1161267"><a href="/opinion/1161267/people-v-superior-court-zolnay/#1394" aria-description="Citation for case: People v. Superior Court (Zolnay)">542 P. 2d 1390, 1394-1395</a></span> (1975), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/816/">429 U. S. 816</a></span> (1976); <em>Ochoa </em>v. <em>State, </em><span class="citation" data-id="9680788"><a href="/opinion/1773695/ochoa-v-state/#800" aria-description="Citation for case: Ochoa v. State">573 S. W. 2d 796, 800-801</a></span> (Tex. Crim. App. 1978). Others have attempted to define a threshold standard of clarity for such requests, and have held that requests falling below this threshold do not trigger the right to counsel. See, <em>e. g., People </em>v. <em>Krueger, </em><span class="citation" data-id="2090485"><a href="/opinion/2090485/people-v-krueger/#311" aria-description="Citation for case: People v. Krueger">82 Ill. 2d 305, 311</a></span>, <span class="citation" data-id="2090485"><a href="/opinion/2090485/people-v-krueger/#540" aria-description="Citation for case: People v. Krueger">412 N. E. 2d 537, 540</a></span> (1980) (“[A]n assertion of the right to counsel need not be explicit, unequivocal, or made with unmistakable clarity,” but not “every reference to an attorney, no matter how vague, indecisive or ambiguous, should constitute an invocation of the right to counsel”), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./451/1019/">451 U. S. 1019</a></span> (1981). Still others have adopted a third approach, holding that when an accused makes an equivocal statement that “arguably” can be construed as a request for counsel, all interrogation must immediately cease except for narrow questions designed to “clarify” the earlier statement and the accused’s desires respecting counsel. See, <em>e. g., Thompson </em>v. <em>Wainwright, </em><span class="citation" data-id="9465905"><a href="/opinion/368063/larry-thompson-v-louie-l-wainwright-secretary-department-of-offender/#771" aria-description="Citation for case: Larry Thompson v. Louie L. Wainwright, Secretary,...">601 F. 2d 768, 771-772</a></span> (CA5 1979); <em>State </em>v. <em>Moulds, </em><span class="citation" data-id="1259486"><a href="/opinion/1259486/state-v-moulds/#888" aria-description="Citation for case: State v. Moulds">105 Idaho 880, 888</a></span>, <span class="citation" data-id="1259486"><a href="/opinion/1259486/state-v-moulds/#1082" aria-description="Citation for case: State v. Moulds">673 P. 2d 1074, 1082</a></span> (App. 1983).</p>
</footnote>
<footnote label="4">
<p id="b238-7"> Indeed, as Justice Simon noted in his dissent below, Smith’s “only previous statement to the officer which is of any significance in this regard is an assertion that ‘she’ warned him that the police would ‘railroad’ him and advised him to get a lawyer before submitting to interrogation.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#377" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 377</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#242" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 242</a></span>; see <em>supra, </em>at 92. Far from creating “ambiguity” concerning Smith’s subsequent request, this statement could only have reinforced the clarity of Smith’s invocation of his right to counsel.</p>
</footnote>
<footnote label="5">
<p id="b239-6"> Justice Rehnquist in his dissent asserts that the trial judge “implicitly concluded that petitioner’s initial statement was not a clear request,” post, at 101, and criticizes the Court for “relitigat[ingj” this “essentially factual inquiry,” <em>post, </em>at 100. As this argument suggests, the trial judge did not discuss the clarity of Smith’s request, but instead simply denied without comment Smith’s motion to suppress. 4 Record 231. In fact, the only “finding” made by the state courts with respect to Smith’s initial request was that it did indeed appear to be “clear and unequivocal.” See <em>supra </em>this pagé.</p>
</footnote>
<footnote label="6">
<p id="b239-11"> The Illinois Appellate Court for the Fourth District also suggested that it was significant that Smith’s request came <em>during </em>the administration of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings: “[H]e merely expressed an <em>interest </em>in obtaining counsel during the administration of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and prior to the beginning of any interrogation. . . . Smith’s statements were not a request for counsel during interrogation. Indeed, interrogation had not begun.” <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#309" aria-description="Citation for case: People v. Smith">113 Ill. App. 3d, at 309-310</a></span>, <span class="citation" data-id="9734006"><a href="/opinion/2190311/people-v-smith/#558" aria-description="Citation for case: People v. Smith">447 N. E. 2d, at 558-559</a></span> (emphasis in original). Justice Rehnquist in his dissent similarly contends that the authorities need not stop their questioning if an accused requests counsel prior to or during the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. See <em>post, </em>at 100-101, 104. Such reasoning is plainly wrong. A request for counsel coming “at <em>any </em>stage of the process” requires that questioning cease until counsel has been provided. <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 444-445</a></span> (emphasis added).</p>
</footnote>
<footnote label="7">
<p id="b240-6"> The dissent contends that the questioning here was “entirely consistent” with the proscriptions of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039</a></span> (1983). <em>Post, </em>at 102. In those cases, the dissent argues, the authorities immediately terminated their questioning once the suspects had invoked their right to counsel, but then sought “to resume interrogation at a later time.” <em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/" aria-description="Citation for case: Oregon v. Bradshaw">Ibid.</a></span> </em>In this case, on the other hand, the detectives did not even <em>initially </em>terminate their questioning. In such circumstances, the dissent proclaims, it is proper to consider “the entire flavor of the colloquy.” <em>Post, </em>at 101. To the extent the dissent suggests that an accused’s Fifth Amendment right <em>to </em>counsel should turn on whether the authorities initially honor his request, we reject this approach as palpably untenable under <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>. </em>Whether in the same interrogating session or in subsequent sessions, the so-called “flavor” of an accused’s request for counsel cannot be dissipated by continued police questioning.</p>
</footnote>
<footnote label="8">
<p id="b241-7"> Most of the dissent is devoted to an effort at demonstrating that the detectives did not <em>actually </em>extract Smith’s confession through trickery or coercion. See <em>post, </em>at 103. This effort is of course beside the point, because the rule we announced in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and which we follow today is a prophylactic safeguard whose application does not turn on whether coercion in fact was employed. Nevertheless, the actual course of the subsequent interrogation in this case reinforces our concern that, absent a bright-line rule requiring an immediate cessation of questioning, an accused may be “badgered” to speak as a result of police “overreaching.” See <em>supra, </em>at 98. As Justice Simon noted in his dissent below:</p>
<blockquote id="b241-8">“I fail to understand how the officer could have mistaken the defendant’s meaning, and no justification is given or is apparent for his proceeding through to the end of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings and in the course of doing so misrepresenting to Smith the meaning of those warnings by the following admonition: ‘You either have to talk to me this time without a lawyer being present and if you do agree to talk with me without a lawyer being present you can stop at any time you want to.’ This communication, even if inadvertent, clearly imparted to the defendant the warning that he had to talk to the interrogator and was seriously misleading.</blockquote>
<blockquote id="b241-9">“. . . In this regard, I find it particularly significant that Smith, who was apparently in police custody for the first time in his life and admitted that he did not ‘know what’s what,’ agreed to talk to the police only after he was told, ostensibly by way of explaining the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, that he had no other choice.” <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#377" aria-description="Citation for case: People v. Smith">102 Ill. 2d, at 377-378</a></span>, <span class="citation" data-id="9714428"><a href="/opinion/2087192/people-v-smith/#242" aria-description="Citation for case: People v. Smith">466 N. E. 2d, at 242</a></span>.</blockquote>
<p id="b241-10">The interrogation here bore a substantial similarity to the one condemned in <em>Edwards </em>v. <em>Arizona, </em>where the accused after requesting counsel was told that “he had” to talk to his interrogators. <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#479" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 479</a></span>. It was precisely such “badger[ing]” that the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>safeguard was designed to prevent. See <em>Oregon </em>v. <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1044" aria-description="Citation for case: Oregon v. Bradshaw"><em>Bradshaw, supra, </em>at 1044</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Smith v. Maryland.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Smith v. Maryland"
type: case
citation: "442 U.S. 735 (1979)"
parallel_cite: "99 S. Ct. 2577; 61 L. Ed. 2d 220"
neutral_cite: 1979 U.S. LEXIS 134
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-20
docket: 78-5374
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Smith v. Maryland
  varies_by_point: false
  scope_note: "Foundational third-party-doctrine case; remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Smith."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110118/smith-v-maryland/"
  cluster_id: 110118
  opinion_id: 110118
  identity_checked: true
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Key — Anchor"
related: ["[[United States v. Miller]]", "[[Carpenter v. United States]]", "[[Katz v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "third-party-doctrine", "pen-register", "surveillance"]
holding: "No reasonable expectation of privacy in phone numbers voluntarily conveyed to the phone company; installing and using a pen register is not a Fourth Amendment search (third-party doctrine)."
lake:
  record_id: Smith v. Maryland
  status: verified
  projected_at: 2026-07-06
---

# Smith v. Maryland

*442 U.S. 735 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a robbery victim received threatening and obscene phone calls, police identified Smith as a suspect and, without a warrant, asked the telephone company to install a pen register at its central office to record the numbers dialed from Smith's home phone. The register showed a call placed to the victim. That information helped secure a search warrant for Smith's home, and he moved to suppress the fruits, arguing the pen register was an unconstitutional warrantless search.

## Issue
Whether the installation and use of a pen register — a device that records the telephone numbers dialed from a particular line — constitutes a "search" within the meaning of the Fourth Amendment.

## Rule
No. A caller has no legitimate expectation of privacy in the numbers he dials, because he voluntarily conveys them to the phone company. "This Court consistently has held that a person has no legitimate expectation of privacy in information he voluntarily turns over to third parties." — 442 U.S. at 743–744. ^pin-743

Applied to dialed numbers: "When he used his phone, petitioner voluntarily conveyed numerical information to the telephone company and 'exposed' that information to its equipment in the ordinary course of business. In so doing, petitioner assumed the risk that the company would reveal to police the numbers he dialed." — *Id.* at 744. ^pin-744

## Application
Smith voluntarily conveyed the numbers he dialed to the telephone company, whose switching equipment routed his calls and routinely recorded such numbers for billing and other legitimate business purposes. Having exposed that information to a third party, he assumed the risk it would be turned over to the government, so he had no legitimate expectation of privacy in it. The pen register therefore worked no Fourth Amendment search, and no warrant was required to install or use it.

## Conclusion
Installation and use of the pen register was not a search; the Fourth Amendment imposed no warrant requirement. With [[United States v. Miller]] (bank records), *Smith* is a foundation of the third-party doctrine the Court later confronted for digital cell-site data in [[Carpenter v. United States]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Smith* remains good law. [[Carpenter v. United States]] (2018) held the third-party doctrine does **not** extend to historical cell-site location information given its uniquely revealing, comprehensive nature, but **expressly declined to overrule** *Smith* or [[United States v. Miller]]; the pen-register/short-term-conveyance holding stands.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Key — Anchor*

## Sources
- *Smith v. Maryland*, 442 U.S. 735 (1979) — https://www.courtlistener.com/opinion/110118/smith-v-maryland/ — pinpoints: 743–744.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "52587985ce86f6cf", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Smith v. Maryland"}, "payload": {"all": [{"cite": "442 U.S. 735", "page": "735", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "442"}, {"cite": "99 S. Ct. 2577", "page": "2577", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "61 L. Ed. 2d 220", "page": "220", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "61"}, {"cite": "1979 U.S. LEXIS 134", "page": "134", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "442 U.S. 735", "official": {"cite": "442 U.S. 735", "page": "735", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "442"}, "official_selection_present": true, "record_id": "Smith v. Maryland"}}
{"assertion_id": "aeafac42fd206803", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-744", "record_id": "Smith v. Maryland"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-744", "pinpoint_status": "slip-only", "quote": "When he used his phone, petitioner voluntarily conveyed numerical information to the telephone company and 'exposed' that information to its equipment in the ordinary course of business. In so doing, petitioner assumed the risk that the company would reveal to police the numbers he dialed.", "quote_fidelity": "mismatch", "record_id": "Smith v. Maryland", "star_marker": null}}
{"assertion_id": "e4b534deb249fbcb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-743", "record_id": "Smith v. Maryland"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-743", "pinpoint_status": "slip-only", "quote": "within the meaning of the Fourth Amendment. ## Rule No. A caller has no legitimate expectation of privacy in the numbers he dials, because he voluntarily conveys them to the phone company.", "quote_fidelity": "mismatch", "record_id": "Smith v. Maryland", "star_marker": null}}
{"assertion_id": "f35c04ab66db271d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Smith v. Maryland"}, "payload": {"as_of_content": "1979-06-20", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Smith v. Maryland", "scope_note": "Foundational third-party-doctrine case; remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Smith.", "varies_by_point": false}}
```

### lake record — Smith v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Smith v. Maryland",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Smith v. Maryland",
    "case_name_short": "",
    "case_name_full": "Smith v. Maryland",
    "input_case_name": "Smith v. Maryland",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-20",
    "year": 1979,
    "docket": "78-5374",
    "cluster_id": 110118,
    "lead_opinion_id": 110118,
    "sibling_ids": [
      110118,
      9427638,
      9427639,
      9427640
    ],
    "absolute_url": "/opinion/110118/smith-v-maryland/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "442 U.S. 735",
      "volume": "442",
      "reporter": "U.S.",
      "page": "735",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2577",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2577",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 220",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "220",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 134",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "442 U.S. 735",
        "volume": "442",
        "reporter": "U.S.",
        "page": "735",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2577",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2577",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 220",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "220",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 134",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "134",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "442 U.S. 735",
    "official_selection": {
      "court_class": "scotus",
      "selected": "442 U.S. 735",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-743",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule No. A caller has no legitimate expectation of privacy in the numbers he dials, because he voluntarily conveys them to the phone company.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-744",
      "page": null,
      "quote": "When he used his phone, petitioner voluntarily conveyed numerical information to the telephone company and 'exposed' that information to its equipment in the ordinary course of business. In so doing, petitioner assumed the risk that the company would reveal to police the numbers he dialed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Smith v. Maryland",
    "varies_by_point": false,
    "scope_note": "Foundational third-party-doctrine case; remains good law. Carpenter v. United States (2018) declined to extend the third-party doctrine to cell-site location information but expressly did not overrule Smith.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Von Harris",
          "cluster_id": 10324088,
          "cite": [
            "2025 Ohio 279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Lepage",
          "cluster_id": 9503197,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman",
          "cluster_id": 10135310,
          "cite": [
            "321 Or. App. 330",
            "515 P.3d 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ajemian v. Yahoo!, Inc.",
          "cluster_id": 4434746,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane1_negative"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Brown",
          "cluster_id": 110901,
          "cite": [
            "75 L. Ed. 2d 502",
            "103 S. Ct. 1535",
            "460 U.S. 730",
            "1983 U.S. LEXIS 143",
            "51 U.S.L.W. 4361"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adrian King, Jr. v. Jim Rubenstein",
          "cluster_id": 3210222,
          "cite": [
            "825 F.3d 206",
            "2016 U.S. App. LEXIS 10276",
            "2016 WL 3165598"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Chadha",
          "cluster_id": 110985,
          "cite": [
            "77 L. Ed. 2d 317",
            "103 S. Ct. 2764",
            "462 U.S. 919",
            "1983 U.S. LEXIS 80",
            "51 U.S.L.W. 4907",
            "13 Envtl. L. Rep. (Envtl. Law Inst.) 20663"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Carter",
          "cluster_id": 118249,
          "cite": [
            "142 L. Ed. 2d 373",
            "119 S. Ct. 469",
            "525 U.S. 83",
            "1998 U.S. LEXIS 7844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Edmunds",
          "cluster_id": 2316698,
          "cite": [
            "586 A.2d 887",
            "526 Pa. 374",
            "1991 Pa. LEXIS 28"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Knotts",
          "cluster_id": 110882,
          "cite": [
            "75 L. Ed. 2d 55",
            "103 S. Ct. 1081",
            "460 U.S. 276",
            "1983 U.S. LEXIS 135",
            "51 U.S.L.W. 4232"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
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
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Campbell",
          "cluster_id": 4463634,
          "cite": [
            "2018 COA 5",
            "425 P.3d 1163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hill v. National Collegiate Athletic Assn.",
          "cluster_id": 1235436,
          "cite": [
            "865 P.2d 633",
            "7 Cal. 4th 1",
            "26 Cal. Rptr. 2d 834",
            "94 Cal. Daily Op. Serv. 681",
            "94 Daily Journal DAR 1141",
            "9 I.E.R. Cas. (BNA) 716",
            "1994 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ross",
          "cluster_id": 1060457,
          "cite": [
            "49 S.W.3d 833",
            "2001 Tenn. LEXIS 563",
            "2001 WL 760100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Smith v. Maryland:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTA1ODY1NjAwMDAwJnM9NDQyNzcyNSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110118+OR+9427638+OR+9427639+OR+9427640%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMTAmcz0xNjI1MDY5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110118+OR+9427638+OR+9427639+OR+9427640%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 2,
        "triage_snippet_classified": 67
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110118 OR 9427638 OR 9427639 OR 9427640)",
    "indexed_citing_opinions": 1450,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110118,
        "count": 1224,
        "count_source": "search"
      },
      {
        "opinion_id": 9427638,
        "count": 267,
        "count_source": "search"
      },
      {
        "opinion_id": 9427639,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427640,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2307,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/smith-v-maryland.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyODU0OTMmcz0xMDM3MzQ1NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110118+OR+9427638+OR+9427639+OR+9427640%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110118,
        "cited_id": 105746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 109953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 324659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 337714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 345476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 1416762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 2073770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110118,
        "cited_id": 2140967,
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
    "date_created": "2026-07-05T19:59:02Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:59:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:59:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:02:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:59:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Smith v. Maryland

```
<div>
<center><b><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">442 U.S. 735</a></span> (1979)</b></center>
<center><h1>SMITH<br>
v.<br>
MARYLAND.</h1></center>
<center>No. 78-5374.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 28, 1979.</center>
<center>Decided June 20, 1979.</center>
CERTIORARI TO THE COURT OF APPEALS OF MARYLAND.
<p><span class="star-pagination">*736</span> <i>Howard L. Cardin</i> argued the cause for petitioner. With him on the brief was <i>James J. Gitomer.</i></p>
<p><i>Stephen H. Sachs,</i> Attorney General of Maryland, argued the cause for respondent. With him on the brief were <i>George A. Nilson,</i> Deputy Attorney General, and <i>Deborah K. Handel</i> and <i>Stephen B. Caplis,</i> Assistant Attorneys General.</p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents the question whether the installation and use of a pen register<sup>[1]</sup> constitutes a "search" within the meaning of the Fourth Amendment,<sup>[2]</sup> made applicable to the States through the Fourteenth Amendment. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p></p>
<h2>
<span class="star-pagination">*737</span> I</h2>
<p>On March 5, 1976, in Baltimore, Md., Patricia McDonough was robbed. She gave the police a description of the robber and of a 1975 Monte Carlo automobile she had observed near the scene of the crime. Tr. 66-68. After the robbery, McDonough began receiving threatening and obscene phone calls from a man identifying himself as the robber. On one occasion, the caller asked that she step out on her front porch; she did so, and saw the 1975 Monte Carlo she had earlier described to police moving slowly past her home. <i>Id.,</i> at 70. On March 16, police spotted a man who met McDonough's description driving a 1975 Monte Carlo in her neighborhood. <i>Id.,</i> at 71-72. By tracing the license plate number, police learned that the car was registered in the name of petitioner, Michael Lee Smith. <i>Id.,</i> at 72.</p>
<p>The next day, the telephone company, at police request, installed a pen register at its central offices to record the numbers dialed from the telephone at petitioner's home. <i>Id.,</i> at 73, 75. The police did not get a warrant or court order before having the pen register installed. The register revealed that on March 17 a call was placed from petitioner's home to McDonough's phone. <i>Id.,</i> at 74. On the basis of this and other evidence, the police obtained a warrant to search petitioner's residence. <i>Id.,</i> at 75. The search revealed that a page in petitioner's phone book was turned down to the name and number of Patricia McDonough; the phone book was seized. <i>Ibid.</i> Petitioner was arrested, and a six-man lineup was held on March 19. McDonough identified petitioner as the man who had robbed her. <i>Id.,</i> at 70-71.</p>
<p>Petitioner was indicted in the Criminal Court of Baltimore for robbery. By pretrial motion, he sought to suppress "all fruits derived from the pen register" on the ground that the police had failed to secure a warrant prior to its installation. Record 14; Tr. 54-56. The trial court denied the suppression motion, holding that the warrantless installation of the pen <span class="star-pagination">*738</span> register did not violate the Fourth Amendment. <i>Id.,</i> at 63. Petitioner then waived a jury, and the case was submitted to the court on an agreed statement of facts. <i>Id.,</i> at 65-66. The pen register tape (evidencing the fact that a phone call had been made from petitioner's phone to McDonough's phone) and the phone book seized in the search of petitioner's residence were admitted into evidence against him. <i>Id.,</i> at 74-76. Petitioner was convicted, <i>id.,</i> at 78, and was sentenced to six years. He appealed to the Maryland Court of Special Appeals, but the Court of Appeals of Maryland issued a writ of certiorari to the intermediate court in advance of its decision in order to consider whether the pen register evidence had been properly admitted at petitioner's trial. <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#160" aria-description="Citation for case: Smith v. State">283 Md. 156, 160</a></span>, <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#860" aria-description="Citation for case: Smith v. State">389 A. 2d 858, 860</a></span> (1978).</p>
<p>The Court of Appeals affirmed the judgment of conviction, holding that "there is no constitutionally protected reasonable expectation of privacy in the numbers dialed into a telephone system and hence no search within the fourth amendment is implicated by the use of a pen register installed at the central offices of the telephone company." <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#173" aria-description="Citation for case: Smith v. State"><i>Id.,</i> at 173</a></span>, <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#867" aria-description="Citation for case: Smith v. State">389 A. 2d, at 867</a></span>. Because there was no "search," the court concluded, no warrant was needed. Three judges dissented, expressing the view that individuals do have a legitimate expectation of privacy regarding the phone numbers they dial from their homes; that the installation of a pen register thus constitutes a "search"; and that, in the absence of exigent circumstances, the failure of police to secure a warrant mandated that the pen register evidence here be excluded. <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#174" aria-description="Citation for case: Smith v. State"><i>Id.,</i> at 174, 178</a></span>, <span class="citation" data-id="9711193"><a href="/opinion/2073770/smith-v-state/#868" aria-description="Citation for case: Smith v. State">389 A. 2d, at 868, 870</a></span>. Certiorari was granted in order to resolve indications of conflict in the decided cases as to the restrictions imposed by the Fourth Amendment on the use of pen registers.<sup>[3]</sup> <span class="citation multiple-matches"><a href="/c/U.%20S./439/1001/">439 U. S. 1001</a></span> (1978).</p>
<p></p>
<h2>
<span class="star-pagination">*739</span> II</h2>
<p></p>
<h2>A</h2>
<p>The Fourth Amendment guarantees "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." In determining whether a particular form of government-initiated electronic surveillance is a "search" within the meaning of the Fourth Amendment,<sup>[4]</sup> our lodestar is <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967). In <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> Government agents had intercepted the contents of a telephone conversation by attaching an electronic listening device to the outside of a public phone booth. The Court rejected the argument that a "search" can occur only when there has been a "physical intrusion" into a "constitutionally protected area," noting that the Fourth Amendment "protects people, not places." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 351-353</a></span>. Because the Government's monitoring of Katz' conversation "violated the privacy upon which he justifiably relied while using the telephone booth," the Court held that <span class="star-pagination">*740</span> it "constituted a `search and seizure' within the meaning of the Fourth Amendment." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353</a></span>.</p>
<p>Consistently with <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> this Court uniformly has held that the application of the Fourth Amendment depends on whether the person invoking its protection can claim a "justifiable," a "reasonable," or a "legitimate expectation of privacy" that has been invaded by government action. <i>E. g., </i><i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 143</a></span>, and n. 12 (1978); <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#150" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 150, 151</a></span> (concurring opinion); <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#164" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 164</a></span> (dissenting opinion); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7</a></span> (1977); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 442</a></span> (1976); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#14" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 14</a></span> (1973); <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#335" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 335-336</a></span> (1973); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S. 745, 752</a></span> (1971) (plurality opinion); <i>Mancusi</i> v. <i>DeForte,</i> <span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#368" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 368</a></span> (1968); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 9</a></span> (1968). This inquiry, as Mr. Justice Harlan aptly noted in his <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> concurrence, normally embraces two discrete questions. The first is whether the individual, by his conduct, has "exhibited an actual (subjective) expectation of privacy," 389 U. S., at 361whether, in the words of the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> majority, the individual has shown that "he seeks to preserve [something] as private." <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 351</a></span>. The second question is whether the individual's subjective expectation of privacy is "one that society is prepared to recognize as 'reasonable,'" <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">id.,</a></span></i> at 361 whether, in the words of the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> majority, the individual's expectation, viewed objectively, is "justifiable" under the circumstances. <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><i>Id.,</i> at 353</a></span>.<sup>[5]</sup> See <i>Rakas</i> v. <i><span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">Illinois</a></span>,</i> 439 U. S., <span class="star-pagination">*741</span> at 143-144, n. 12; <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#151" aria-description="Citation for case: Rakas v. Illinois"><i>id.,</i> at 151</a></span> (concurring opinion); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S., at 752</a></span> (plurality opinion).</p>
<p></p>
<h2>B</h2>
<p>In applying the <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> analysis to this case, it is important to begin by specifying precisely the nature of the state activity that is challenged. The activity here took the form of installing and using a pen register. Since the pen register was installed on telephone company property at the telephone company's central offices, petitioner obviously cannot claim that his "property"' was invaded or that police intruded into a "constitutionally protected area." Petitioner's claim, rather, is that, notwithstanding the absence of a trespass, the State, as did the Government in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> infringed a "legitimate expectation of privacy" that petitioner held. Yet a pen register differs significantly from the listening device employed in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> for pen registers do not acquire the <i>contents</i> of communications. This Court recently noted:</p>
<blockquote>"Indeed, a law enforcement official could not even determine from the use of a pen register whether a communication existed. These devices do not hear sound. They disclose only the telephone numbers that have been dialeda means of establishing communication. Neither the purport of any communication between the caller and the recipient of the call, their identities, nor whether the call was even completed is disclosed by pen registers." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#167" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159, 167</a></span> (1977).</blockquote>
<p><span class="star-pagination">*742</span> Given a pen register's limited capabilities, therefore, petitioner's argument that its installation and use constituted a "search" necessarily rests upon a claim that he had a "legitimate expectation of privacy" regarding the numbers he dialed on his phone.</p>
<p>This claim must be rejected. First, we doubt that people in general entertain any actual expectation of privacy in the numbers they dial. All telephone users realize that they must "convey" phone numbers to the telephone company, since it is through telephone company switching equipment that their calls are completed. All subscribers realize, moreover, that the phone company has facilities for making permanent records of the numbers they dial, for they see a list of their long-distance (toll) calls on their monthly bills. In fact, pen registers and similar devices are routinely used by telephone companies "for the purposes of checking billing operations, detecting fraud, and preventing violations of law." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#174" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 174-175</a></span>. Electronic equipment is used not only to keep billing records of toll calls, but also "to keep a record of all calls dialed from a telephone which is subject to a special rate structure." <i>Hodge</i> v. <i>Mountain States Tel. &amp; Tel. Co.,</i> <span class="citation" data-id="9463842"><a href="/opinion/345476/james-l-hodge-v-the-mountain-states-telephone-and-telegraph-company-a/#266" aria-description="Citation for case: James L. Hodge v. The Mountain States Telephone and...">555 F. 2d 254, 266</a></span> (CA9 1977) (concurring opinion). Pen registers are regularly employed "to determine whether a home phone is being used to conduct a business, to check for a defective dial, or to check for overbilling." Note, The Legal Constraints upon the Use of the Pen Register as a Law Enforcement Tool, <span class="citation no-link">60 Cornell L. Rev. 1028</span>, 1029 (1975) (footnotes omitted). Although most people may be oblivious to a pen register's esoteric functions, they presumably have some awareness of one common use: to aid in the identification of persons making annoying or obscene calls. See, <i>e. g., </i><i>Von Lusch</i> v. <i>C &amp; P Telephone Co.,</i> <span class="citation" data-id="2347338"><a href="/opinion/2347338/von-lusch-v-c-p-telephone-co/#816" aria-description="Citation for case: Von Lusch v. C &amp; P Telephone Co.">457 F. Supp. 814, 816</a></span> (Md. 1978); Note, 60 Cornell L. Rev., at 1029-1030, n. 11; Claerhout, The Pen Register, <span class="citation no-link">20 Drake L. Rev. 108</span>, 110-111 (1970). Most phone books tell <span class="star-pagination">*743</span> subscribers, on a page entitled "Consumer Information," that the company "can frequently help in identifying to the authorities the origin of unwelcome and troublesome calls." <i>E. g.,</i> Baltimore Telephone Directory 21 (1978); District of Columbia Telephone Directory 13 (1978). Telephone users, in sum, typically know that they must convey numerical information to the phone company; that the phone company has facilities for recording this information; and that the phone company does in fact record this information for a variety of legitimate business purposes. Although subjective expectations cannot be scientifically gauged, it is too much to believe that telephone subscribers, under these circumstances, harbor any general expectation that the numbers they dial will remain secret.</p>
<p>Petitioner argues, however, that, whatever the expectations of telephone users in general, he demonstrated an expectation of privacy by his own conduct here, since he "us[ed] the telephone <i>in his house</i> to the exclusion of all others." Brief for Petitioner 6 (emphasis added). But the site of the call is immaterial for purposes of analysis in this case. Although petitioner's conduct may have been calculated to keep the <i>contents</i> of his conversation private, his conduct was not and could not have been calculated to preserve the privacy of the number he dialed. Regardless of his location, petitioner had to convey that number to the telephone company in precisely the same way if he wished to complete his call. The fact that he dialed the number on his home phone rather than on some other phone could make no conceivable difference, nor could any subscriber rationally think that it would.</p>
<p>Second, even if petitioner did harbor some subjective expectation that the phone numbers he dialed would remain private, this expectation is not "one that society is prepared to recognize as 'reasonable.'" <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S., at 361</a></span>. This Court consistently has held that a person has no legitimate expectation of privacy in information he <span class="star-pagination">*744</span> voluntarily turns over to third parties. <i>E. g., </i><i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller">425 U. S., at 442-444</a></span>; <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#335" aria-description="Citation for case: Couch v. United States">409 U. S., at 335-336</a></span>; <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#752" aria-description="Citation for case: United States v. White">401 U. S., at 752</a></span> (plurality opinion); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 302</a></span> (1966); <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span> (1963). In <i><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span>,</i> for example, the Court held that a bank depositor has no "legitimate `expectation of privacy'" in financial information "voluntarily conveyed to . . . banks and exposed to their employees in the ordinary course of business." <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller">425 U. S., at 442</a></span>. The Court explained:</p>
<blockquote>"The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government. . . . This Court has held repeatedly that the Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed." <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller"><i>Id.,</i> at 443</a></span>.</blockquote>
<p>Because the depositor "assumed the risk" of disclosure, the Court held that it would be unreasonable for him to expect his financial records to remain private.</p>
<p>This analysis dictates that petitioner can claim no legitimate expectation of privacy here. When he used his phone, petitioner voluntarily conveyed numerical information to the telephone company and "exposed" that information to its equipment in the ordinary course of business. In so doing, petitioner assumed the risk that the company would reveal to police the numbers he dialed. The switching equipment that processed those numbers is merely the modern counterpart of the operator who, in an earlier day, personally completed calls for the subscriber. Petitioner concedes that if he had placed his calls through an operator, he could claim no legitimate expectation of privacy. Tr. of Oral Arg. 3-5, 11-12, 32. We <span class="star-pagination">*745</span> are not inclined to hold that a different constitutional result is required because the telephone company has decided to automate.</p>
<p>Petitioner argues, however, that automatic switching equipment differs from a live operator in one pertinent respect. An operator, in theory at least, is capable of remembering every number that is conveyed to him by callers. Electronic equipment, by contrast, can "remember" only those numbers it is programmed to record, and telephone companies, in view of their present billing practices, usually do not record local calls. Since petitioner, in calling McDonough, was making a local call, his expectation of privacy as to her number, on this theory, would be "legitimate."</p>
<p>This argument does not withstand scrutiny. The fortuity of whether or not the phone company in fact elects to make a quasi-permanent record of a particular number dialed does not, in our view, make any constitutional difference. Regardless of the phone company's election, petitioner voluntarily conveyed to it information that it had facilities for recording and that it was free to record. In these circumstances, petitioner assumed the risk that the information would be divulged to police. Under petitioner's theory, Fourth Amendment protection would exist, or not, depending on how the telephone company chose to define local-dialing zones, and depending on how it chose to bill its customers for local calls. Calls placed across town, or dialed directly, would be protected; calls placed across the river, or dialed with operator assistance, might not be. We are not inclined to make a crazy quilt of the Fourth Amendment, especially in circumstances where (as here) the pattern of protection would be dictated by billing practices of a private corporation.</p>
<p>We therefore conclude that petitioner in all probability entertained no actual expectation of privacy in the phone numbers he dialed, and that, even if he did, his expectation was not "legitimate." The installation and use of a pen register, <span class="star-pagination">*746</span> consequently, was not a "search," and no warrant was required. The judgment of the Maryland Court of Appeals is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>Mr. JUSTICE POWELL took no part in the consideration or decision of this case.</p>
<p>Mr. JUSTICE STEWART, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>I am not persuaded that the numbers dialed from a private telephone fall outside the constitutional protection of the Fourth and Fourteenth Amendments.</p>
<p>In <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352</a></span>, the Court acknowledged the "vital role that the public telephone has come to play in private communication[s]." The role played by a private telephone is even more vital, and since <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> it has been abundantly clear that telephone conversations carried on by people in their homes or offices are fully protected by the Fourth and Fourteenth Amendments. As the Court said in <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span>, "the broad and unsuspected governmental incursions into conversational privacy which electronic surveillance entails necessitate the application of Fourth Amendment safeguards." (Footnote omitted.)</p>
<p>Nevertheless, the Court today says that those safeguards do not extend to the numbers dialed from a private telephone, apparently because when a caller dials a number the digits may be recorded by the telephone company for billing purposes. But that observation no more than describes the basic nature of telephone calls. A telephone call simply cannot be made without the use of telephone company property and without payment to the company for the service. The telephone conversation itself must be electronically transmitted by telephone company equipment, and may be recorded or overheard by the use of other company equipment. Yet we <span class="star-pagination">*747</span> have squarely held that the user of even a public telephone is entitled "to assume that the words he utters into the mouthpiece will not be broadcast to the world." <i>Katz</i> v. <i>United States, supra,</i> at 352.</p>
<p>The central question in this case is whether a person who makes telephone calls from his home is entitled to make a similar assumption about the numbers he dials. What the telephone company does or might do with those numbers is no more relevant to this inquiry than it would be in a case involving the conversation itself. It is simply not enough to say, after <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,</i> that there is no legitimate expectation of privacy in the numbers dialed because the caller assumes the risk that the telephone company will disclose them to the police.</p>
<p>I think that the numbers dialed from a private telephone like the conversations that occur during a callare within the constitutional protection recognized in <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>.</i><sup>[1]</sup> It seems clear to me that information obtained by pen register surveillance of a private telephone is information in which the telephone subscriber has a legitimate expectation of privacy.<sup>[2]</sup> The information captured by such surveillance emanates from private conduct within a person's home or officelocations that without question are entitled to Fourth and Fourteenth Amendment protection. Further, that information is an integral part of the telephonic communication that under <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> <span class="star-pagination">*748</span> is entitled to constitutional protection, whether or not it is captured by a trespass into such an area.</p>
<p>The numbers dialed from a private telephonealthough certainly more prosaic than the conversation itselfare not without "content." Most private telephone subscribers may have their own numbers listed in a publicly distributed directory, but I doubt there are any who would be happy to have broadcast to the world a list of the local or long distance numbers they have called. This is not because such a list might in some sense be incriminating, but because it easily could reveal the identities of the persons and the places called, and thus reveal the most intimate details of a person's life.</p>
<p>I respectfully dissent.</p>
<p>Mr. JUSTICE MARSHALL, with whom Mr. JUSTICE BRENNAN joins, dissenting.</p>
<p>The Court concludes that because individuals have no actual or legitimate expectation of privacy in information they voluntarily relinquish to telephone companies, the use of pen registers by government agents is immune from Fourth Amendment scrutiny. Since I remain convinced that constitutional protections are not abrogated whenever a person apprises another of facts valuable in criminal investigations, see, <i>e. g., </i><i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White">401 U. S. 745, 786-790</a></span> (1971) (Harlan, J., dissenting); <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#795" aria-description="Citation for case: United States v. White"><i>id.,</i> at 795-796</a></span> (MARSHALL, J., dissenting); <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#95" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 95-96</a></span> (1974) (MARSHALL, J., dissenting); <i>United States</i> v. <i>Miller,</i> <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#455" aria-description="Citation for case: United States v. Miller">425 U. S. 435, 455-456</a></span> (1976) (MARSHALL, J., dissenting), I respectfully dissent.</p>
<p>Applying the standards set forth in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring), the Court first determines that telephone subscribers have no subjective expectations of privacy concerning the numbers they dial. To reach this conclusion, the Court posits that individuals somehow infer from the long-distance listings on their phone bills, and from the cryptic assurances of "help" in tracing obscene <span class="star-pagination">*749</span> calls included in "most" phone books, that pen registers are regularly used for recording local calls. See <i>ante,</i> at 742-743. But even assuming, as I do not, that individuals "typically know" that a phone company monitors calls for internal reasons, <i>ante,</i> at 743,<sup>[1]</sup> it does not follow that they expect this information to be made available to the public in general or the government in particular. Privacy is not a discrete commodity, possessed absolutely or not at all. Those who disclose certain facts to a bank or phone company for a limited business purpose need not assume that this information will be released to other persons for other purposes. See <i>California Bankers Assn.</i> v. <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#95" aria-description="Citation for case: California Bankers Assn. v. Shultz"><i>Shultz, supra,</i> at 95-96</a></span> (MARSHALL, J., dissenting).</p>
<p>The crux of the Court's holding, however, is that whatever expectation of privacy petitioner may in fact have entertained regarding his calls, it is not one "society is prepared to recognize as `reasonable.'" <i>Ante,</i> at 743. In so ruling, the Court determines that individuals who convey information to third parties have "assumed the risk" of disclosure to the government. <i>Ante,</i> at 744, 745. This analysis is misconceived in two critical respects.</p>
<p>Implicit in the concept of assumption of risk is some notion of choice. At least in the third-party consensual surveillance cases, which first incorporated risk analysis into Fourth Amendment doctrine, the defendant presumably had exercised some discretion in deciding who should enjoy his confidential communications. See, <i>e. g., </i><i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/#439" aria-description="Citation for case: Lopez v. United States">373 U. S. 427, 439</a></span> (1963); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#302" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 302-303</a></span> (1966); <i>United States</i> v. <i><span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">White, supra,</a></span></i> at 751-752 <span class="star-pagination">*750</span> (plurality opinion). By contrast here, unless a person is prepared to forgo use of what for many has become a personal or professional necessity, he cannot help but accept the risk of surveillance. Cf. <i>Lopez</i> v. <i>United States, supra,</i> at 465-466 (BRENNAN, J., dissenting). It is idle to speak of "assuming" risks in contexts where, as a practical mater, individuals have no realistic alternative.</p>
<p>More fundamentally, to make risk analysis dispositive in assessing the reasonableness of privacy expectations would allow the government to define the scope of Fourth Amendment protections. For example, law enforcement officials, simply by announcing their intent to monitor the content of random samples of first-class mail or private phone conversations, could put the public on notice of the risks they would thereafter assume in such communications. See Amsterdam, Perspectives on the Fourth Amendment, <span class="citation no-link">58 Minn. L. Rev. 349</span>, 384, 407 (1974). Yet, although acknowledging this implication of its analysis, the Court is willing to concede only that, in some circumstances, a further "normative inquiry would be proper." <i>Ante,</i> at 740-741, n. 5. No meaningful effort is made to explain what those circumstances might be, or why this case is not among them.</p>
<p>In my view, whether privacy expectations are legitimate within the meaning of <i><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span></i> depends not on the risks an individual can be presumed to accept when imparting information to third parties, but on the risks he should be forced to assume in a free and open society. By its terms, the constitutional prohibition of unreasonable searches and seizures assigns to the judiciary some prescriptive responsibility. As Mr. Justice Harlan, who formulated the standard the Court applies today, himself recognized: "[s]ince it is the task of the law to form and project, as well as mirror and reflect, we should not . . . merely recite . . . risks without examining the desirability of saddling them upon society." <i>United States</i> v. <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White"><i>White, supra,</i> at 786</a></span> (dissenting opinion). In making this <span class="star-pagination">*751</span> assessment, courts must evaluate the "intrinsic character" of investigative practices with reference to the basic values underlying the Fourth Amendment. <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#95" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S., at 95</a></span> (MARSHALL, J., dissenting). And for those "extensive intrusions that significantly jeopardize [individuals'] sense of security . . . , more than self-restraint by law enforcement officials is required." <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/#786" aria-description="Citation for case: United States v. White">401 U. S., at 786</a></span> (Harlan, J., dissenting).</p>
<p>The use of pen registers, I believe, constitutes such an extensive intrusion. To hold otherwise ignores the vital role telephonic communication plays in our personal and professional relationships, see <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S., at 352</a></span>, as well as the First and Fourth Amendment interests implicated by unfettered official surveillance. Privacy in placing calls is of value not only to those engaged in criminal activity. The prospect of unregulated governmental monitoring will undoubtedly prove disturbing even to those with nothing illicit to hide. Many individuals, including members of unpopular political organizations or journalists with confidential sources, may legitimately wish to avoid disclosure of their personal contacts. See <i>NAACP</i> v. <i>Alabama,</i> <span class="citation" data-id="105746"><a href="/opinion/105746/national-assn-for-the-advancement-of-colored-people-v-alabama-ex-rel/#463" aria-description="Citation for case: National Ass&#x27;n for the Advancement of Colored People v....">357 U. S. 449, 463</a></span> (1958); <i>Branzburg</i> v. <i>Hayes,</i> <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#695" aria-description="Citation for case: Branzburg v. Hayes">408 U. S. 665, 695</a></span> (1972); <span class="citation" data-id="9425020"><a href="/opinion/108611/branzburg-v-hayes/#728" aria-description="Citation for case: Branzburg v. Hayes"><i>id.,</i> at 728-734</a></span> (STEWART, J., dissenting). Permitting governmental access to telephone records on less than probable cause may thus impede certain forms of political affiliation and journalistic endeavor that are the hallmark of a truly free society. Particularly given the Government's previous reliance on warrantless telephonic surveillance to trace reporters' sources and monitor protected political activity,<sup>[2]</sup> I am unwilling to insulate use of pen registers from independent judicial review.</p>
<p><span class="star-pagination">*752</span> Just as one who enters a public telephone booth is "entitled to assume that the words he utters into the mouthpiece will not be broadcast to the world," <i>Katz</i> v. <i>United States, supra,</i> at 352, so too, he should be entitled to assume that the numbers he dials in the privacy of his home will be recorded, if at all, solely for the phone company's business purposes. Accordingly, I would require law enforcement officials to obtain a warrant before they enlist telephone companies to secure information otherwise beyond the government's reach.</p>
<h2>NOTES</h2>
<p>[1]  "A pen register is a mechanical device that records the numbers dialed on a telephone by monitoring the electrical impulses caused when the dial on the telephone is released. It does not overhear oral communications and does not indicate whether calls are actually completed." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159</a></span>, 161 n. 1 (1977). A pen register is "usually installed at a central telephone facility [and] records on a paper tape all numbers dialed from [the] line" to which it is attached. <i>United States</i> v. <i>Giordano,</i> <span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S. 505</a></span>, 549 n. 1 (1974) (opinion concurring in part and dissenting in part). See also <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#162" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 162</a></span>.</p>
<p>[2]  "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." U. S. Const., Amdt. 4.</p>
<p>[3]  See <i>Application of United States for Order,</i> <span class="citation" data-id="8900411"><a href="/opinion/8912555/united-states-v-southwestern-bell-telephone-co/#245" aria-description="Citation for case: United States v. Southwestern Bell Telephone Co.">546 F. 2d 243, 245</a></span> (CA8 1976), cert. denied <i>sub nom. </i><i>Southwestern Bell Tel. Co.</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./434/1008/">434 U. S. 1008</a></span> (1978); <i>Application of United States in Matter of Order,</i> <span class="citation" data-id="9462905"><a href="/opinion/337714/application-of-the-united-states-of-america-in-the-matter-of-an-order/#959" aria-description="Citation for case: Application of the United States of America in the Matter...">538 F. 2d 956, 959-960</a></span> (CA2 1976), rev'd on other grounds <i>sub nom. </i><i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159</a></span> (1977); <i>United States</i> v. <i>Falcone,</i> <span class="citation" data-id="9461166"><a href="/opinion/322631/united-states-v-pasquale-falcone-appeal-of-pasquale-falconio-in-no/#482" aria-description="Citation for case: United States v. Pasquale Falcone Appeal of Pasquale...">505 F. 2d 478, 482</a></span>, and n. 21 (CA3 1974), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./420/955/">420 U. S. 955</a></span> (1975); <i>Hodge</i> v. <i>Mountain States Tel. &amp; Tel. Co.,</i> <span class="citation" data-id="9463842"><a href="/opinion/345476/james-l-hodge-v-the-mountain-states-telephone-and-telegraph-company-a/#256" aria-description="Citation for case: James L. Hodge v. The Mountain States Telephone and...">555 F. 2d 254, 256</a></span> (CA9 1977); <span class="citation" data-id="9463842"><a href="/opinion/345476/james-l-hodge-v-the-mountain-states-telephone-and-telegraph-company-a/#266" aria-description="Citation for case: James L. Hodge v. The Mountain States Telephone and..."><i>id.,</i> at 266</a></span> (concurring opinion); and <i>United States</i> v. <i>Clegg,</i> <span class="citation" data-id="324659"><a href="/opinion/324659/united-states-v-michael-william-clegg/#610" aria-description="Citation for case: United States v. Michael William Clegg">509 F. 2d 605, 610</a></span> (CA5 1975). In previous decisions, this Court has not found it necessary to consider whether "pen register surveillance [is] subject to the requirements of the Fourth Amendment." <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S., at 165</a></span> n. 7. See <i>United States</i> v. <i>Giordano,</i> <span class="citation" data-id="9425702"><a href="/opinion/109020/united-states-v-giordano/" aria-description="Citation for case: United States v. Giordano">416 U. S., at 554</a></span> n. 4 (opinion concurring in part and dissenting in part).</p>
<p>[4]  In this case, the pen register was installed, and the numbers dialed were recorded, by the telephone company. Tr. 73-74. The telephone company, however, acted at police request. <i>Id.,</i> at 73, 75. In view of this, respondent appears to concede that the company is to be deemed an "agent" of the police for purposes of this case, so as to render the installation and use of the pen register "state action" under the Fourth and Fourteenth Amendments. We may assume that "state action" was present here.</p>
<p>[5]  Situations can be imagined, of course, in which <i>Katz'</i> two-pronged inquiry would provide an inadequate index of Fourth Amendment protection. For example, if the Government were suddenly to announce on nationwide television that all homes henceforth would be subject to warrantless entry, individuals thereafter might not in fact entertain any actual expectation of privacy regarding their homes, papers, and effects. Similarly, if a refugee from a totalitarian country, unaware of this Nation's traditions, erroneously assumed that police were continuously monitoring his telephone conversations, a subjective expectation of privacy regarding the contents of his calls might be lacking as well. In such circumstances, where an individual's subjective expectations had been "conditioned" by influences alien to well-recognized Fourth Amendment freedoms, those subjective expectations obviously could play no meaningful role in ascertaining what the scope of Fourth Amendment protection was. In determining whether a "legitimate expectation of privacy" existed in such cases, a normative inquiry would be proper.</p>
<p>[1]  It is true, as the Court pointed out in <i>United States</i> v. <i>New York Tel. Co.,</i> <span class="citation" data-id="9427010"><a href="/opinion/109755/united-states-v-new-york-telephone-co/#166" aria-description="Citation for case: United States v. New York Telephone Co.">434 U. S. 159, 166-167</a></span>, that under Title III of the Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">18 U. S. C. §§ 2510-2520</span>, pen registers are not considered "interceptions" because "they do not acquire the `contents' of communications," as that term is defined by Congress. We are concerned in this case, however, not with the technical definitions of a statute, but with the requirements of the Constitution.</p>
<p>[2]  The question whether a defendant who is not a member of the subscriber's household has "standing" to object to pen register surveillance of a private telephone is, of course, distinct. Cf. <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128</a></span>.</p>
<p>[1]  Lacking the Court's apparently exhaustive knowledge of this Nation's telephone books and the reading habits of telephone subscribers, see <i>ante,</i> at 742-743, I decline to assume general public awareness of how obscene phone calls are traced. Nor am I persuaded that the scope of Fourth Amendment protection should turn on the concededly "esoteric functions" of pen registers in corporate billing, <i>ante,</i> at 742, functions with which subscribers are unlikely to have intimate familiarity.</p>
<p>[2]  See, <i>e. g., </i><i>Reporters Committee For Freedom of Press</i> v. <i>American Tel. &amp; Tel. Co.,</i> 192 U. S. App. D. C. 376, <span class="citation" data-id="9465568"><a href="/opinion/363949/reporters-committee-for-freedom-of-the-press-v-american-telephone/" aria-description="Citation for case: Reporters Committee for Freedom of the Press v. American...">593 F. 2d 1030</a></span> (1978), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./440/949/">440 U. S. 949</a></span> (1979); <i>Halperin</i> v. <i>Kissinger,</i> <span class="citation" data-id="1416762"><a href="/opinion/1416762/halperin-v-kissinger/" aria-description="Citation for case: Halperin v. Kissinger">434 F. Supp. 1193</a></span> (DC 1977); <i>Socialist Workers Party</i> v. <i>Attorney General,</i> <span class="citation" data-id="2140967"><a href="/opinion/2140967/socialist-workers-party-v-attorney-general-of-the-united-states/" aria-description="Citation for case: Socialist Workers Party v. Attorney General of the United...">463 F. Supp. 515</a></span> (SDNY 1978).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Soldal v. Cook County.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Soldal v. Cook County"
type: case
citation: ""
parallel_cite: "506 U.S. 56; 113 S. Ct. 538; 121 L. Ed. 2d 450; 92 Daily Journal DAR 16378; 61 U.S.L.W. 4019; 6 Fla. L. Weekly Fed. S 769"
neutral_cite: "1992 U.S. LEXIS 7835; 92 Cal. Daily Op. Serv. 9794"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1992
date_decided: 1992-12-08
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1992-12-08
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Soldal v. Cook County
  varies_by_point: false
  scope_note: "Good law; the holding that the Fourth Amendment protects possessory interests independent of privacy and liberty remains controlling."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112795/soldal-v-cook-county/"
  cluster_id: 112795
  opinion_id: 112795
  identity_checked: true
homes:
  - page: "[[Seizure of Property]]"
    role: "Key — Anchor (seizure of property)"
  - page: "[[Trespass]]"
    role: "Related (cross-doctrine)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Jacobsen]]", "[[Horton v. California]]", "[[Oliver v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "possessory-interest", "property", "section-1983"]
holding: "A 'seizure' of property occurs whenever there is meaningful interference with possessory interests; the Fourth Amendment protects property interests independent of privacy or liberty."
lake:
  record_id: Soldal v. Cook County
  status: verified
  projected_at: 2026-07-09
---

# Soldal v. Cook County

*506 U.S. 56 (1992)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A trailer-park owner, without an eviction order, forcibly towed the Soldals' mobile home off its lot two weeks before the scheduled eviction hearing. Cook County sheriff's deputies stood by to prevent Soldal from interfering and declined to take his trespass complaint, knowing the eviction was unlawful. Soldal sued under § 1983, claiming an unreasonable seizure. The Seventh Circuit held there was no Fourth Amendment "seizure" because only possessory (not privacy or liberty) interests were affected.

## Issue
Whether a meaningful interference with a person's possessory interest in property — here, the towing of a home — is a "seizure" under the Fourth Amendment even though no privacy or liberty interest was invaded.

## Rule
Yes. "A 'seizure' of property, we have explained, occurs when 'there is some meaningful interference with an individual's possessory interests in that property.'" — 506 U.S. at 61 (quoting [[United States v. Jacobsen]]). ^pin-61

The Fourth Amendment is not limited to privacy: "our cases unmistakably hold that the Amendment protects property as well as privacy." — [*Id.* at 62](https://www.courtlistener.com/opinion/112795/soldal-v-cook-county/#:~:text=our%20cases%20unmistakably%20hold%20that). ^pin-62

## Application
The deputies' participation in physically wrenching the Soldals' trailer from its moorings and towing it away was a quintessential meaningful interference with the family's possessory interest — indeed, the home "literally was carried away." That the action invaded no privacy or liberty interest did not remove it from the Fourth Amendment, because the Amendment independently protects possessory interests in "effects" and "houses." The seizure therefore had to be reasonable, a question [[Reading and Citing Cases#on-remand|remanded]] for resolution.

## Conclusion
The towing of the Soldals' home was a Fourth Amendment seizure; the Seventh Circuit's contrary holding was reversed. *Soldal* establishes that property seizures are governed by the Fourth Amendment whether or not any privacy or liberty interest is also implicated.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Applies the seizure definition of [[United States v. Jacobsen]] to possessory interests and complements the plain-view seizure analysis of [[Horton v. California]]; the Court cautioned the Amendment does not protect possessory interests in *all* property (cf. [[Oliver v. United States]], open fields).

## Appears on
- [[Trespass]] — *Key — Anchor (seizure of property)*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Soldal v. Cook County*, 506 U.S. 56 (1992) — https://www.courtlistener.com/opinion/112795/soldal-v-cook-county/ — pinpoints: 61, 62.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "406c4ca446d0bb00", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Soldal v. Cook County"}, "payload": {"all": [{"cite": "506 U.S. 56", "page": "56", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "506"}, {"cite": "113 S. Ct. 538", "page": "538", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "113"}, {"cite": "121 L. Ed. 2d 450", "page": "450", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "121"}, {"cite": "1992 U.S. LEXIS 7835", "page": "7835", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1992"}, {"cite": "92 Daily Journal DAR 16378", "page": "16378", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "92"}, {"cite": "61 U.S.L.W. 4019", "page": "4019", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "61"}, {"cite": "6 Fla. L. Weekly Fed. S 769", "page": "769", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "6"}, {"cite": "92 Cal. Daily Op. Serv. 9794", "page": "9794", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "92"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Soldal v. Cook County"}}
{"assertion_id": "1be558532729e1f3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-61", "record_id": "Soldal v. Cook County"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-61", "pinpoint_status": "slip-only", "quote": "under the Fourth Amendment even though no privacy or liberty interest was invaded. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Soldal v. Cook County", "star_marker": null}}
{"assertion_id": "b445c6f61bc01237", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-62", "record_id": "Soldal v. Cook County"}, "payload": {"fragment": "#:~:text=our%20cases%20unmistakably%20hold%20that", "page": null, "pin_id": "pin-62", "pinpoint_status": "star-verified", "quote": "our cases unmistakably hold that the Amendment protects property as well as privacy.", "quote_fidelity": "matched", "record_id": "Soldal v. Cook County", "star_marker": "62"}}
{"assertion_id": "62e762593d34c787", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Soldal v. Cook County"}, "payload": {"as_of_content": "1992-12-08", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Soldal v. Cook County", "scope_note": "Good law; the holding that the Fourth Amendment protects possessory interests independent of privacy and liberty remains controlling.", "varies_by_point": false}}
```

### lake record — Soldal v. Cook County

```json
{
  "schema_version": "s2.v1",
  "record_id": "Soldal v. Cook County",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Soldal v. Cook County",
    "case_name_short": "Soldal",
    "case_name_full": "SOLDAL Et Ux. v. COOK COUNTY, ILLINOIS, Et Al.",
    "input_case_name": "Soldal v. Cook County",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1992-12-08",
    "year": 1992,
    "docket": null,
    "cluster_id": 112795,
    "lead_opinion_id": 112795,
    "sibling_ids": [
      112795
    ],
    "absolute_url": "/opinion/112795/soldal-v-cook-county/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "506 U.S. 56",
        "volume": "506",
        "reporter": "U.S.",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 538",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 L. Ed. 2d 450",
        "volume": "121",
        "reporter": "L. Ed. 2d",
        "page": "450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Daily Journal DAR 16378",
        "volume": "92",
        "reporter": "Daily Journal DAR",
        "page": "16378",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 U.S.L.W. 4019",
        "volume": "61",
        "reporter": "U.S.L.W.",
        "page": "4019",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 Fla. L. Weekly Fed. S 769",
        "volume": "6",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1992 U.S. LEXIS 7835",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "7835",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Cal. Daily Op. Serv. 9794",
        "volume": "92",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9794",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "506 U.S. 56",
        "volume": "506",
        "reporter": "U.S.",
        "page": "56",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 S. Ct. 538",
        "volume": "113",
        "reporter": "S. Ct.",
        "page": "538",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 L. Ed. 2d 450",
        "volume": "121",
        "reporter": "L. Ed. 2d",
        "page": "450",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1992 U.S. LEXIS 7835",
        "volume": "1992",
        "reporter": "U.S. LEXIS",
        "page": "7835",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Daily Journal DAR 16378",
        "volume": "92",
        "reporter": "Daily Journal DAR",
        "page": "16378",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 U.S.L.W. 4019",
        "volume": "61",
        "reporter": "U.S.L.W.",
        "page": "4019",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 Fla. L. Weekly Fed. S 769",
        "volume": "6",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 Cal. Daily Op. Serv. 9794",
        "volume": "92",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "9794",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": null,
    "official_selection": {
      "court_class": "scotus",
      "selected": null,
      "reason": "unlisted_reporter:Fla. L. Weekly Fed. S"
    }
  },
  "pinpoints": [
    {
      "id": "pin-61",
      "page": null,
      "quote": "under the Fourth Amendment even though no privacy or liberty interest was invaded. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-62",
      "page": null,
      "quote": "our cases unmistakably hold that the Amendment protects property as well as privacy.",
      "star_marker": "62",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10477,
      "fragment": "#:~:text=our%20cases%20unmistakably%20hold%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1992-12-08",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Soldal v. Cook County",
    "varies_by_point": false,
    "scope_note": "Good law; the holding that the Fourth Amendment protects possessory interests independent of privacy and liberty remains controlling.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Sullivan",
          "cluster_id": 2821420,
          "cite": [
            "797 F.3d 623",
            "2015 U.S. App. LEXIS 13702",
            "2015 WL 4547498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tony Lavan v. City of Los Angeles",
          "cluster_id": 807915,
          "cite": [
            "693 F.3d 1022",
            "2012 WL 3834659",
            "2012 U.S. App. LEXIS 18639"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Poteet v. Sullivan",
          "cluster_id": 2332316,
          "cite": [
            "218 S.W.3d 780",
            "2007 WL 289871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane1_negative"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Daniel Good Real Property",
          "cluster_id": 112914,
          "cite": [
            "126 L. Ed. 2d 490",
            "114 S. Ct. 492",
            "510 U.S. 43",
            "1993 U.S. LEXIS 7941",
            "7 Fla. L. Weekly Fed. S 665",
            "93 Daily Journal DAR 15706",
            "93 Cal. Daily Op. Serv. 9143",
            "62 U.S.L.W. 4013",
            "1993 WL 505539"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Edward Hoefling, Jr. v. City of Miami",
          "cluster_id": 3171918,
          "cite": [
            "811 F.3d 1271",
            "93 Fed. R. Serv. 3d 1022",
            "2016 U.S. App. LEXIS 1177",
            "2016 WL 285358"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. Outboard Marine Corp.",
          "cluster_id": 762789,
          "cite": [
            "172 F.3d 531",
            "1999 U.S. App. LEXIS 5444",
            "1999 WL 164061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byron Halsey v. Frank Pfeiffer",
          "cluster_id": 2671183,
          "cite": [
            "750 F.3d 273",
            "2014 WL 1622769",
            "2014 U.S. App. LEXIS 7696"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Geoffrey M. Radvansky v. City of Olmsted Falls",
          "cluster_id": 788941,
          "cite": [
            "395 F.3d 291",
            "2005 U.S. App. LEXIS 739",
            "2005 WL 77154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Kimball",
          "cluster_id": 1906975,
          "cite": [
            "724 A.2d 326",
            "555 Pa. 299",
            "1999 Pa. LEXIS 134"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brian Sheppard v. Leon Beerman, as an Individual and in His Official Capacity as Justice of the Supreme Court of the State of New York",
          "cluster_id": 664638,
          "cite": [
            "18 F.3d 147",
            "1994 U.S. App. LEXIS 3985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark A. Lee v. City of Chicago",
          "cluster_id": 782110,
          "cite": [
            "330 F.3d 456",
            "2003 U.S. App. LEXIS 10254",
            "2003 WL 21196550"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muriel D. Black v. Michael P. Lane, Michael Neal, P.A. Severs, Captain",
          "cluster_id": 669084,
          "cite": [
            "22 F.3d 1395"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Young",
          "cluster_id": 1196592,
          "cite": [
            "867 P.2d 593",
            "123 Wash. 2d 173",
            "1994 Wash. LEXIS 122"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jordan v. Gardner",
          "cluster_id": 601474,
          "cite": [
            "986 F.2d 1521",
            "93 Cal. Daily Op. Serv. 1354",
            "1993 U.S. App. LEXIS 3065",
            "1993 WL 46630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freeman v. City of Santa Ana",
          "cluster_id": 7034204,
          "cite": [
            "68 F.3d 1180",
            "96 Cal. Daily Op. Serv. 25",
            "96 Daily Journal DAR 29",
            "1995 U.S. App. LEXIS 37134",
            "1995 WL 611554"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peggy Poe v. John Leonard, Defendant-Third Party-Plaintiff-Appellant, Douglas Pearl, State of Connecticut, Third-Party-Defendant",
          "cluster_id": 776746,
          "cite": [
            "282 F.3d 123",
            "2002 WL 237411"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armendariz v. Penman",
          "cluster_id": 7035099,
          "cite": [
            "75 F.3d 1311",
            "96 Cal. Daily Op. Serv. 839",
            "1996 U.S. App. LEXIS 1613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delores Henry v. Melody Hulett",
          "cluster_id": 4774392,
          "cite": [
            "969 F.3d 769"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
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
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheila Hensley v. Ronald Gassman",
          "cluster_id": 808240,
          "cite": [
            "693 F.3d 681",
            "2012 WL 3932043",
            "2012 U.S. App. LEXIS 19025"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Soldal v. Cook County:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112795) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQ5NTUyMDAwMDAwJnM9MjQyODA5MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112795%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(112795)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkmcz04MTk4NjEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112795%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112795)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 1,
        "triage_snippet_classified": 39
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112795)",
    "indexed_citing_opinions": 560,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112795,
        "count": 560,
        "count_source": "search"
      }
    ],
    "citation_count": 1158,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/soldal-v-cook-county.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2Njg3MjEmcz05NDc1MjIwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112795%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112795,
        "cited_id": 87010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 108568,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110325,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 111851,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 509655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 567219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112795,
        "cited_id": 2159763,
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
    "date_created": "2026-07-05T20:02:17Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:02:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:02:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:05:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:02:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Soldal v. Cook County

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b195-13">
  Justice White
 </author>
<p id="AA-">
  delivered the opinion of the Court.
 </p>
<p id="b195-14">
  HH
 </p>
<p id="b195-3">
  Edward Soldal and his family resided in their trailer home, which was located on a rented lot in the Willoway Terrace
  <span citation-index="1" class="star-pagination" label="58"> 
   *58
   </span>
  mobile home park in Elk Grove, Illinois. In May 1987, Terrace Properties, the owner of the park, and Margaret Hale, its manager, filed an eviction proceeding against the Soldáis in an Illinois state court. Under the Illinois Forcible Entry and Detainer Act, Ill. Rev. Stat., ch.. 110, ¶ 9-101
  <em>
   et seq.
  </em>
  (1991), a tenant cannot be dispossessed absent a judgment of eviction. The suit was dismissed on June 2, 1987. A few months later, in August 1987, the owner brought a second proceeding of eviction, claiming nonpayment of rent. The case was set for trial on September 22, 1987.
 </p>
<p id="b196-5">
  Rather than await judgment in their favor, Terrace Properties and Hale, contrary to Illinois law, chose to evict the Soldáis forcibly two weeks prior to the scheduled hearing. On September 4, Hale notified the Cook County’s Sheriff’s Department that she was going to remove the trailer home from the park, and requested the presence of sheriff deputies to forestall any possible resistance. Later that day, two Terrace Properties employees arrived at the Soldáis’ home accompanied by Cook County Deputy Sheriff O’Neil. The employees proceeded to wrench the sewer and water connections off the side of the trailer home, disconnect the phone, tear off the trailer’s canopy and skirting, and hook the home to a tractor. Meanwhile, O’Neil explained to Edward Soldal that “ ‘he was there to see that [Soldal] didn’t interfere with [Willoway’s] work.’” Brief for Petitioner 6.
 </p>
<p id="b196-6">
  By this time, two more deputy sheriffs had arrived at the scene and Soldal told them that he wished to file a complaint for criminal trespass. They referred him to Deputy Lieutenant Jones, who was in Hale’s office. Jones asked Soldal to wait outside while he remained closeted with Hale and other Terrace Properties employees for over 20 minutes. After talking to a district attorney and making Soldal wait another half hour, Jones told Soldal that he would not accept a complaint because “ ‘it was between the landlord and the tenant . . . [and] they were going to go ahead and continue to move
  <span citation-index="1" class="star-pagination" label="59"> 
   *59
   </span>
  out the trailer.’”
  <em>
   Id.,
  </em>
  at 8.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Throughout this period, the deputy sheriffs knew that Terrace Properties did not have an eviction order and that its actions were unlawful. Eventually, and in the presence of an additional two deputy sheriffs, the Willoway workers pulled the trailer free of its moorings and towed it onto the street. Later, it was hauled to a neighboring property.
 </p>
<p id="b197-5">
  On September 9, the state judge assigned to the pending eviction proceedings ruled that the eviction had been unauthorized and ordered Terrace Properties to return the Sol-dais’ home to the lot. The home, however, was badly damaged.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  The Soldáis brought this action under <span class="citation no-link">42 U. S. C. § 1983</span>, alleging a violation of their rights under the Fourth and Fourteenth Amendments. They claimed that Terrace Properties and Hale had conspired with Cook County deputy sheriffs to unreasonably seize and remove the Soldáis’ trailer home. The District Judge granted defendants’ motion for summary judgment on the grounds that the Soldáis had failed to adduce any evidence to support their conspiracy theory and, therefore, the existence of state action necessary under § 1983.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b197-6">
  The Court of Appeals for the Seventh Circuit, construing the facts in petitioners’ favor, accepted their contention that there was state action. However, it went on to hold that
  <span citation-index="1" class="star-pagination" label="60"> 
   *60
   </span>
  the removal of the Soldáis’ trailer did not constitute a seizure for purposes of the Fourth Amendment or a deprivation of due process for purposes of the Fourteenth.
 </p>
<p id="b198-5">
  On rehearing, a majority of the Seventh Circuit, sitting en banc, reaffirmed the panel decision.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  Acknowledging that what had occurred was a “seizure” in the literal sense of the word, the court reasoned that, because it was not made in the course of public law enforcement and because it did not invade the Soldáis’ privacy, it was not a seizure as contemplated by the Fourth Amendment. <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1076" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d 1073, 1076</a></span> (1991). Interpreting prior cases of this Court, the Seventh Circuit concluded that, absent interference with privacy or liberty, a “pure deprivation of property” is not cognizable under the Fourth Amendment.
  <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1078" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
   Id.,
  </em>
  at 1078-1079</a></span>. Rather, petitioners’ property interests were protected only by the Due Process Clauses of the Fifth and Fourteenth Amendments.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
</p>
<p id="b198-6">
  We granted certiorari to consider whether the seizure and removal of the Soldáis’ trailer home implicated their Fourth Amendment rights, <span class="citation no-link">603 U. S. 918</span> (1992), and now reverse.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
</p>
<p id="b199-4">
<span citation-index="1" class="star-pagination" label="61"> 
   *61
   </span>
  II
 </p>
<p id="b199-5">
  The Fourth Amendment, made applicable to the States by the Fourteenth,
  <em>
   Ker
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#30" aria-description="Citation for case: Ker v. California">374 U. S. 23, 30</a></span> (1963), provides in pertinent part that the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated . . .
 </p>
<p id="b199-6">
  A “seizure” of property, we have explained, occurs when “there is some meaningful interference with an individual’s possessory interests in that property.”
  <em>
   United States
  </em>
  v.
  <em>
   Jacobsen,
  </em>
  <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U. S. 109, 113</a></span> (1984). In addition, we have emphasized that “at the very core” of the Fourth Amendment “stands the right of a man to retreat into his own home.”
  <em>
   Silverman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.%20S./366/605/">366 U. S. 605</a></span>, 611 (1961). See also. Oliver v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#178" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 178-179</a></span> (1984);
  <em>
   Wyman
  </em>
  v.
  <em>
   James,
  </em>
  <span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/#316" aria-description="Citation for case: Wyman v. James">400 U. S. 309, 316</a></span> (1971);
  <em>
   Payton
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation multiple-matches"><a href="/c/U.%20S./446/573/">446 U. S. 573</a></span>, 601 (1980).
 </p>
<p id="b199-7">
  As a result of the state action in this case, the Soldáis’ domicile was not only seized, it literally was carried away, giving new meaning to the term “mobile home.” We fail to see how being unceremoniously dispossessed of one’s home in the manner alleged to have occurred here can be viewed as anything but a seizure invoking the protection of the Fourth Amendment. Whether the Amendment was in fact
  <span citation-index="1" class="star-pagination" label="62"> 
   *62
   </span>
  violated is, of course, a different question that requires determining if the seizure was reasonable. That inquiry entails the weighing of various factors and is not before us. •
 </p>
<p id="b200-5">
  The Court of Appeals recognized that there had been a seizure, but concluded that it was a seizure only in a “technical” sense, not within the meaning of the Fourth Amendment. This conclusion followed from a narrow reading of the Amendment, which the court construed to safeguard only privacy and liberty interests while leaving unprotected possessory interests where neither privacy nor liberty was at stake. Otherwise, the court said,
 </p>
<blockquote id="b200-6">
  “a constitutional provision enacted two centuries ago [would] make every repossession and eviction with police assistance actionable under — of all things — the Fourth Amendments which] would both trivialize the amendment and gratuitously shift a large body of routine commercial litigation from the state courts to the federal courts. That trivializing, this shift, can be prevented by recognizing the difference between posses-sory and privacy interests.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1077" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1077</a></span>.
 </blockquote>
<p id="b200-7">
  Because the officers had not entered Soldal’s house, rummaged through his possessions, or, in the Court of Appeals’ view, interfered with his liberty in the course of the eviction, the Fourth Amendment offered no protection against the “grave deprivation” of property that had occurred.
  <em>
   <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/" aria-description="Citation for case: Edward Soldal v. County of Cook">Ibid.</a></span>
  </em>
</p>
<p id="b200-8">
  We do not agree with this interpretation of the Fourth Amendment. The Amendment protects the people from unreasonable searches and seizures of “their persons, houses, papers, and effects.” This language surely cuts.against the novel holding below, and our cases unmistakably hold that the Amendment protects property as well as privacy.
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  This
  <span citation-index="1" class="star-pagination" label="63"> 
   *63
   </span>
  much was made clear in
  <em>
   <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen, supra,</a></span>
  </em>
  where we explained that the first Clause of the Fourth Amendment
 </p>
<blockquote id="b201-5">
  “protects two types of expectations, one involving ‘searches,’ the other ‘seizures.’ A ‘search’ occurs when an expectation of privacy that society is prepared to consider reasonable is infringed. A ‘seizure’ of property occurs where there is some meaningful interference with an individual’s possessory interests in that property.” 466 U. S., at 113 (footnote omitted).
 </blockquote>
<p id="b201-6">
  See also
  <em>
   id.,
  </em>
  at 120;
  <em>
   Horton
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#183" aria-description="Citation for case: Horton v. California">496 U. S. 128, 183</a></span> (1990);
  <em>
   Arizona
  </em>
  v.
  <em>
   Hicks,
  </em>
  <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#328" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 328</a></span> (1987);
  <em>
   Maryland
  </em>
  v.
  <em>
   Macon,
  </em>
  <span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#469" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463, 469</a></span> (1985);
  <em>
   Texas
  </em>
  v.
  <em>
   Brown,
  </em>
  <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown">460 U. S. 730, 747-748</a></span> (1983) (Stevens, J., concurring in judgment);
  <em>
   United States
  </em>
  v.
  <em>
   Salvucci,
  </em>
  <span class="citation" data-id="9428036"><a href="/opinion/110325/united-states-v-salvucci/#91" aria-description="Citation for case: United States v. Salvucci">448 U. S. 83, 91, n. 6</a></span> (1980). Thus, having concluded that chemical testing of powder found in a package did not compromise its owner’s privacy, the Court in
  <em>
   <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">Jacobsen</a></span>
  </em>
  did not put an end to its inquiry, as would be required under the view adopted by the Court of Appeals and advocated by respondents. Instead, adhering to the teachings of
  <em>
   United States
  </em>
  v.
  <em>
   Place,
  </em>
  <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">462 U. S. 696</a></span> (1983), it went on to determine whether the invasion of the owners’ “possessory interests” occasioned by the destruction of the powder was reasonable under the Fourth Amendment.
  <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#124" aria-description="Citation for case: United States v. Jacobsen"><em>
   Jacobsen, supra,
  </em>
  at 124-125</a></span>. In
  <em>
   <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>,
  </em>
  although we found that subjecting luggage to a “dog sniff” did not constitute a search for Fourth Amendment purposes because it did not compromise any privacy interest, taking custody of Place’s suitcase was deemed an unlawful seizure for it unreasonably infringed “the suspect’s possessory interest in his luggage.” <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#708" aria-description="Citation for case: United States v. Place">462 U. S., at 708</a></span>.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  Although lacking a privacy component, the property rights in both instances nonetheless were not
  <span citation-index="1" class="star-pagination" label="64"> 
   *64
   </span>
  disregarded, but rather were afforded Fourth Amendment protection.
 </p>
<p id="b202-5">
  Respondents rely principally on precedents such as
  <em>
   Katz
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967),
  <em>
   Warden, Maryland Penitentiary
  </em>
  v.
  <em>
   Hayden,
  </em>
  <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967), and
  <em>
   Cardwell
  </em>
  v.
  <em>
   Lewis,
  </em>
  <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583</a></span> (1974), to demonstrate that the Fourth Amendment is only marginally concerned with property rights. But the message of those cases is that property rights are not the sole measure of Fourth Amendment violations. The
  <em>
   Warden
  </em>
  opinion thus observed, citing
  <em>
   Jones
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), and
  <em>
   Silverman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), that the “principal” object of the Amendment is the protection of privacy rather than property and that “this shift in emphasis from property to privacy has come about through a subtle interplay of substantive and procedural reform.” <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#304" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S., at 304</a></span>. There was no suggestion that this shift in emphasis had snuffed out the previously recognized protection for property under the Fourth Amendment.
  <em>
   <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,
  </em>
  in declaring violative of the Fourth Amendment the unwarranted overhearing of a telephone booth conversation, effectively ended any lingering notions that the protection of privacy depended on trespass into a protected area. In the course of its decision, the
  <em>
   <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>
  </em>
  Court stated that the Fourth Amendment can neither be translated into a provision dealing with constitutionally protected areas nor. into a general constitutional right to privacy. The Amendment, the Court said, protects individual privacy against certain kinds of governmental intrusion, “but its protections go further, and often have nothing to do with privacy at all.” <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#350" aria-description="Citation for case: Katz v. United States">389 U. S., at 350</a></span>.
 </p>
<p id="b202-6">
  As for
  <em>
   <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/" aria-description="Citation for case: Cardwell v. Lewis">Cardwell</a></span>,
  </em>
  a plurality of this Court held in that case that the Fourth Amendment did not bar the use in evidence of paint scrapings taken from and tire treads observed on the defendant’s automobile, which had been seized in a parking lot and towed to a police lockup. Gathering this evidence was not deemed to be a search, for nothing from the
  <span citation-index="1" class="star-pagination" label="65"> 
   *65
   </span>
  interior of the car and “no personal effects, which the Fourth Amendment traditionally has been deemed to protect” were searched or seized. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 591</a></span> (opinion of Blackmun, J.). No meaningful privacy rights were invaded. But this left the argument, pressed by the dissent, that the evidence gathered was the product of a warrantless and hence illegal seizure of the car from the parking lot where the defendant had left it. However, the plurality was of the view that, because under the circumstances of the case there was probable cause to seize the car as an instrumentality of the crime, Fourth Amendment precedent permitted the seizure without a warrant.
  <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#593" aria-description="Citation for case: Cardwell v. Lewis"><em>
   Id.,
  </em>
  at 593</a></span>. Thus, both the plurality and dissenting Justices considered the defendant’s auto deserving of Fourth Amendment protection even though privacy interests were not at stake. They differed only in the degree of protection that the Amendment demanded.
 </p>
<p id="b203-5">
  The Court of Appeals appeared to find more specific support for confining the protection of the Fourth Amendment to privacy interests in our decision in
  <em>
   Hudson
  </em>
  v.
  <em>
   Palmer,
  </em>
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">468 U. S. 517</a></span> (1984). There, a state prison inmate sued, claiming that prison guards had entered his cell without consent and had seized and destroyed some of his personal effects. We ruled that an inmate, because of his status, enjoyed neither a right to privacy in his cell nor protection against unreasonable seizures of his personal effects.
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#526" aria-description="Citation for case: Hudson v. Palmer"><em>
   Id.,
  </em>
  at 526-528</a></span>, and n. 8;
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/#538" aria-description="Citation for case: Hudson v. Palmer"><em>
   id.,
  </em>
  at 538</a></span> (O’Connor, J., concurring). Whatever else the case held, it is of limited usefulness outside the prison context with respect to the coverage of the Fourth Amendment.
 </p>
<p id="b203-6">
  We thus are unconvinced that any of the Court’s prior cases supports the view that the Fourth Amendment protects against unreasonable seizures of property only where privacy or liberty is also implicated. What is more, our “plain view” decisions make untenable such a construction of the Amendment. Suppose, for example, that police officers lawfully enter a house, by either complying with the warrant requirement or satisfying one of its recognized exceptions—
  <span citation-index="1" class="star-pagination" label="66"> 
   *66
   </span>
<em>
   e. g.,
  </em>
  through a valid consent or a showing of exigent circumstances. If they come across some item in plain view and seize it, no invasion of personal privacy has occurred.
  <em>
   Horton,
  </em>
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#133" aria-description="Citation for case: Horton v. California">496 U. S., at 133-134</a></span>;
  <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown"><em>
   Brown, supra,
  </em>
  at 739</a></span> (opinion of Rehnquist, J.). If the boundaries of the Fourth Amendment were defined exclusively by rights of privacy, “plain view” seizures would not implicate that constitutional provision at all. Yet, far from being automatically upheld, “plain view” seizures have been scrupulously subjected to Fourth Amendment inquiry. Thus, in the absence of consent or a warrant permitting the seizure of the items in question, such seizures can be justified only if they meet the probable-cause standard,
  <em>
   Arizona
  </em>
  v.
  <em>
   Hicks,
  </em>
  <span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#326" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 326-327</a></span> (1987),
  <a class="footnote" href="#fn9" id="fn9_ref">
   9
  </a>
  and if they are unaccompanied by unlawful trespass,
  <em>
   Horton,
  </em>
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California">496 U. S., at 136-137</a></span>.
  <a class="footnote" href="#fn10" id="fn10_ref">
   10
  </a>
  That is because, the absence of a privacy interest notwithstanding, “[a] seizure of the article ... would obviously invade the owner’s possessory interest.”
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#134" aria-description="Citation for case: Horton v. California"><em>
   Id.,
  </em>
  at 134</a></span>; see also
  <em>
   Brown,
  </em>
  <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#739" aria-description="Citation for case: Texas v. Brown">460 U. S., at 739</a></span> (opinion of Rehnquist, J.). The plain-view doctrine “merely reflects an application of the Fourth Amendment’s central requirement of reasonableness to the law governing seizures of property.”
  <em>
   Ibid.; Coolidge
  </em>
  v.
  <em>
   New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 468</a></span> (1971);
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#516" aria-description="Citation for case: Coolidge v. New Hampshire"><em>
   id.,
  </em>
  at 516</a></span> (White, J., concurring and dissenting).
 </p>
<p id="b204-5">
  The Court of Appeals understandably found it necessary to reconcile its holding with our recognition in the plain-view cases that the Fourth Amendment protects property as such. In so doing, the court did not distinguish this case on the ground that the seizure of the Soldáis’ home took place in a
  <span citation-index="1" class="star-pagination" label="67"> 
   *67
   </span>
  noncriminal context. Indeed, it acknowledged what is evident from our precedents — that the Amendment’s protection applies in the civil context as well. See
  <em>
   O’Connor
  </em>
  v.
  <em>
   Ortega,
  </em>
  <span class="citation" data-id="9430897"><a href="/opinion/111851/oconnor-v-ortega/" aria-description="Citation for case: O&#x27;CONNOR v. Ortega">480 U. S. 709</a></span> (1987);
  <em>
   New Jersey
  </em>
  v.
  <em>
   T. L. O.,
  </em>
  <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#334" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S. 325, 334-335</a></span> (1985);
  <em>
   Michigan
  </em>
  v.
  <em>
   Tyler,
  </em>
  <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#504" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 504-506</a></span> (1978);
  <em>
   Marshall
  </em>
  v.
  <em>
   Barlow’s, Inc.,
  </em>
  <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312-313</a></span> (1978);
  <em>
   Camara
  </em>
  v.
  <em>
   Municipal Court of San Francisco,
  </em>
  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967).
  <a class="footnote" href="#fn11" id="fn11_ref">
   11
  </a>
</p>
<p id="b205-5">
  Nor did the Court of Appeals suggest that the Fourth Amendment applied exclusively to law enforcement activities. It observed, for example, that the Amendment’s protection would be triggered “by a search or other entry into the home incident to an eviction or repossession,” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1077" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1077</a></span>.
  <a class="footnote" href="#fn12" id="fn12_ref">
   12
  </a>
  Instead, the court sought to explain why the Fourth Amendment protects against seizures of property in the plain-view context, but not in this case, as follows:
 </p>
<blockquote id="b205-6">
  “[S]eizures made in the course of investigations by police or other law enforcement officers are almost always, as' in the plain view cases, the culmination of searches. The police search in order to seize, and it is the search
  <span citation-index="1" class="star-pagination" label="68"> 
   *68
   </span>
<em>
   and ensuing seizure
  </em>
  that the Fourth Amendment by its reference to ‘searches and seizures’ seeks to regulate. Seizure means one thing when it is the outcome of a search; it may mean something else when it stands apart from a search or any other investigative activity. The Fourth Amendment may still nominally apply, but, precisely because there is no invasion of privacy, the usual rules do not apply.”
  <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1079" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
   Id.,
  </em>
  at 1079</a></span> (emphasis in original).
 </blockquote>
<p id="b206-5">
  We have difficulty with this passage. The court seemingly construes the Amendment to protect only against seizures that are the outcome of a search. But our cases are to the contrary and hold that seizures of property are subject to Fourth Amendment scrutiny even though no search within the meaning of the Amendment has taken place. See,
  <em>
   e. g., Jacobsen,
  </em>
  466 U. S., at 120-125; Place, <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#706" aria-description="Citation for case: United States v. Place">462 U. S., at 706-707</a></span>;
  <em>
   Cardwell,
  </em>
  <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#588" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 588-589</a></span>.
  <a class="footnote" href="#fn13" id="fn13_ref">
   13
  </a>
  More generally, an officer who happens to come across an individual’s property in a public area could seize it only if Fourth Amendment standards are satisfied — for example, if the items are evidence of a crime or contraband. Cf.
  <em>
   Payton
  </em>
  v.
  <em>
   New York,
  </em>
<span citation-index="1" class="star-pagination" label="69"> 
   *69
   </span>
  445 U. S., at 587. We are also puzzled by the last sentence of the excerpt, where the court announces that the “usual rules” of the Fourth Amendment are inapplicable if the seizure is not the result of a search or any other investigative activity “precisely because there is no invasion of privacy.” For the plain-view cases clearly state that, notwithstanding the absence of any interference with privacy, seizures of effects that are not authorized by a warrant are reasonable only because there is probable cause to associate the property with criminal activity. The seizure of the weapons in
  <em>
   <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/" aria-description="Citation for case: Horton v. California">Horton</a></span>,
  </em>
  for example, occurred in the midst of a search, yet we emphasized that it did not “involve any invasion of privacy.” <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#133" aria-description="Citation for case: Horton v. California">496 U. S., at 133</a></span>. In short, our statement that such seizures must satisfy the Fourth Amendment and will be deemed reasonable only if the item’s incriminating character is “immediately apparent,”
  <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California"><em>
   id.,
  </em>
  at 136-137</a></span>, is at odds with the Court of Appeals’ approach.
 </p>
<p id="b207-5">
  The Court of Appeals’ effort is both interesting and creative, but at bottom it simply reasserts the earlier thesis that the Fourth Amendment protects privacy but not property. We remain unconvinced and see no justification for departing from our prior cases. In our view, the reason why an officer might enter a house or effectuate a seizure is wholly irrelevant to the threshold question whether the Amendment applies. What matters is the intrusion on the people’s security from governmental interference. Therefore, the right against unreasonable seizures would be no less transgressed if the seizure of the house was undertaken to collect evidence, verify compliance with a housing regulation, effect an eviction by the police, or on a whim, for no reason at all. As we have observed on more than one occasion, it would be “anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior.”
  <em>
   Camara,
  </em>
  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 530</a></span>; see also
  <em>
   O’Connor,
  </em>
  480 U. S., at 715;
  <em>
   T. L. O.,
  </em>
  <span class="citation" data-id="9429812"><a href="/opinion/111301/new-jersey-v-t-l-o/#335" aria-description="Citation for case: New Jersey v. T. L. O.">469 U. S., at 335</a></span>.
 </p>
<p id="b208-4">
<span citation-index="1" class="star-pagination" label="70"> 
   *70
   </span>
  The Court of Appeals also stated that even if, contrary to its previous rulings, “there is some element or tincture of a Fourth Amendment seizure, it cannot carry the day for the Soldáis.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1080" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1080</a></span>. Relying on our decision in
  <em>
   Graham
  </em>
  v.
  <em>
   Connor,
  </em>
  <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">490 U. S. 386</a></span> (1989), the court reasoned that it should look at the “dominant character of the conduct challenged in a section 1983 case [to] determine the constitutional standard under which it is evaluated.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1080" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1080</a></span>. Believing that the Soldáis' claim was more akin to a challenge against the deprivation of property without due process of law than against an unreasonable seizure, the court concluded that they should not be allowed to bring their suit under the guise of the Fourth Amendment.
 </p>
<p id="b208-5">
  But we see no basis for doling out constitutional protections in such fashion. Certain wrongs affect more than a single right and, accordingly, can implicate more than one of the Constitution’s commands. Where such multiple violations are alleged, we are not in the habit of identifying as a preliminary matter the claim’s “dominant” character. Rather, we examine each constitutional provision in turn. See,
  <em>
   e. g., Hudson
  </em>
  v.
  <em>
   Palmer,
  </em>
  <span class="citation" data-id="9429735"><a href="/opinion/111252/hudson-v-palmer/" aria-description="Citation for case: Hudson v. Palmer">468 U. S. 517</a></span> (1984) (Fourth Amendment and Fourteenth Amendment Due Process Clause);
  <em>
   Ingraham
  </em>
  v.
  <em>
   Wright,
  </em>
  <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span> (1977) (Eighth Amendment and Fourteenth Amendment Due Process Clause).
  <em>
   <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>
  </em>
  is not to the contrary. Its holding was that claims of excessive use of force should be analyzed under the Fourth Amendment’s reasonableness standard, rather than the Fourteenth Amendment’s substantive due process test. We were guided by the fact that, in that case, both provisions targeted the same sort of governmental conduct and, as a result, we chose the more “explicit textual source of constitutional protection” over the “more generalized notion of ‘substantive due process.’” <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S., at 394-395</a></span>. Surely,
  <em>
   <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/" aria-description="Citation for case: Graham v. Connor">Graham</a></span>
  </em>
  does not bar resort in this case to the Fourth Amendment’s specific protection for “houses, papers,
  <span citation-index="1" class="star-pagination" label="71"> 
   *71
   </span>
  and effects” rather than the general protection of property in the Due Process Clause.
 </p>
<p id="pAC6">
  III
 </p>
<p id="b209-3">
  Respondents are fearful, as was the Court of Appeals, that applying the Fourth Amendment in this context inevitably will carry it into territory unknown and unforeseen: routine repossessions, negligent actions of public employees that interfere with individuals’ right to enjoy their homes, and the like, thereby federalizing areas of law traditionally the concern of the States. For several reasons, we think the risk is exaggerated. To begin, our decision will have no impact on activities such as repossessions or attachments if they involve entry into the home, intrusion on individuals’ privacy, or interference with their liberty, because they would implicate the Fourth Amendment even on the Court of Appeals’ own terms. This was true of the Tenth Circuit’s decision in
  <em>
   Specht
  </em>
  with which, as we previously noted, the Court of Appeals expressed agreement.
 </p>
<p id="b209-4">
  More significantly, “reasonableness is still the ultimate standard” under the Fourth Amendment,
  <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><em>
   Camara, supra,
  </em>
  at 539</a></span>, which means that numerous seizures of this type will survive constitutional scrutiny. As is true in other circumstances, the reasonableness determination will reflect a “careful balancing of governmental and private interests.”
  <em>
   T. L. O., supra,
  </em>
  at 341. Assuming, for example, that the officers were acting pursuant to a court order, as in
  <em>
   Specht
  </em>
  v.
  <em>
   Jensen,
  </em>
  <span class="citation" data-id="8955392"><a href="/opinion/8964119/specht-v-jensen/" aria-description="Citation for case: Specht v. Jensen">832 F. 2d 1516</a></span> (CA10 1987), or
  <em>
   Fuentes
  </em>
  v.
  <em>
   Shevin,
  </em>
  <span class="citation" data-id="9424930"><a href="/opinion/108568/fuentes-v-shevin/" aria-description="Citation for case: Fuentes v. Shevin">407 U. S. 67</a></span> (1972), and as often would be the case, a showing of unreasonableness on these facts would be a laborious task indeed. Cf.
  <em>
   Simms
  </em>
  v.
  <em>
   Slacum,
  </em>
  <span class="citation" data-id="9416257"><a href="/opinion/84818/simms-v-slacum/#301" aria-description="Citation for case: Simms v. Slacum">3 Cranch 300, 301</a></span> (1806). Hence, while there is no guarantee against the filing of frivolous suits, had the ejection in this case properly awaited the state court’s judgment it is quite unlikely that the federal court would have been bothered with a § 1983 action alleging a Fourth Amendment violation.
 </p>
<p id="b210-5">
<span citation-index="1" class="star-pagination" label="72"> 
   *72
   </span>
  Moreover, we doubt that the police will often choose to further an enterprise knowing that it is contrary to the law, or proceed to seize property in the absence of objectively reasonable grounds for doing so. In short, our reaffirmance of Fourth Amendment principles today should not foment a wave of new litigation in the federal courts.
 </p>
<p id="b210-6">
<em>
   &gt;
  </em>
</p>
<p id="b210-3">
  The complaint here alleges that respondents, acting under color of state law, dispossessed the Soldáis of their trailer home by physically tearing it from its foundation and towing it to another lot. Taking these allegations as true, this was no “garden-variety” landlord-tenant or commercial dispute. The facts alleged suffice to constitute a “seizure” within the meaning of the . Fourth Amendment, for they plainly implicate the interests protected by that provision. The judgment of the Court of Appeals is, accordingly, reversed, and the case is remanded for further proceedings consistent with this opinion.
 </p>
<p id="b210-8">
<em>
   So ordered.
  </em>
</p>













<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b197-7">
   Jones’ statement was prompted by a district attorney’s advice that no criminal charges could be brought because, under Illinois law, a criminal action cannot be used to determine the right of possession. See Ill. Rev. Stat., ch. 110, ¶ 9-101
   <em>
    et seq.
   </em>
   (1991);
   <em>
    People
   </em>
   v.
   <em>
    Evans,
   </em>
   <span class="citation" data-id="2159763"><a href="/opinion/2159763/people-v-evans/" aria-description="Citation for case: People v. Evans">163 Ill. App. 3d 561</a></span>, <span class="citation" data-id="2159763"><a href="/opinion/2159763/people-v-evans/" aria-description="Citation for case: People v. Evans">516 N. E. 2d 817</a></span> (1st Dist. 1987).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b197-8">
   The Soldáis ultimately were evicted per court order in December 1987.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b197-9">
   Title <span class="citation no-link">42 U. S. C. § 1983</span> provides that:
  </p>
<blockquote id="b197-10">
   “Every person who, under color of any statute, ordinance, regulation, custom or usage, of any State . . . subjects, or causes to be subjected, any citizen of the United States ... to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b198-7">
   The court reiterated the panel’s conclusion that a conspiracy must be assumed on the state of the record and, therefore, that the case must be treated in its current posture “as if the deputy sheriffs themselves seized the trailer, disconnected it from the utilities, and towed it away.” <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1076" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d 1073, 1076</a></span> (1991).
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b198-8">
   The court noted that, in light of the existence of adequate judicial remedies under state law, a claim for deprivation of property without due process of law was unlikely to succeed.
   <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1075" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
    Id.,
   </em>
   at 1075-1076</a></span>. See
   <em>
    Parratt
   </em>
   v.
   <em>
    Taylor,
   </em>
   <span class="citation" data-id="9428330"><a href="/opinion/110478/parratt-v-taylor/" aria-description="Citation for case: Parratt v. Taylor">451 U. S. 527</a></span> (1981). In any event, the Soldáis did not claim a violation of their procedural rights. As noted, the Seventh Circuit also held that respondents had not violated the Soldáis’ substantive due process rights under the Fourteenth Amendment. Petitioners assert that this was error, but in view of our disposition of the case we need not address the question at this time.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b198-9">
   Under <span class="citation no-link">42 U. S. C. § 1983</span>, the Soldáis were required to establish that the respondents, acting under color of state law, deprived them of a constitutional right, in this instance, their Fourth and Fourteenth Amendment freedom from unreasonable seizures by the State. See
   <em>
    Monroe
   </em>
   v.
   <em>
    Pape,
   </em>
<span citation-index="1" class="star-pagination" label="61"> 
    *61
    </span>
   <span class="citation" data-id="106225"><a href="/opinion/106225/lush-v-commissioner-of-education-of-new-york/#184" aria-description="Citation for case: Lush v. Commissioner of Education of New York">366 U. S. 167, 184</a></span> (1961). Respondents request that we affirm on the ground that the Court of Appeals erred in holding that there was sufficient state action to support a § 1983 action. The alleged injury to the Soldáis, it is urged, was inflicted by private parties for whom the county is not responsible. Although respondents did not cross-petition, they are entitled to ask us to affirm on that ground if such action would not enlarge the judgment of the Court of Appeals in their favor. The Court of Appeals found that because the police prevented Soldal from using reasonable force to protect his home from private action that the officers knew was illegal, there was sufficient evidence of conspiracy between the private parties and the officers to foreclose summary judgment for respondents. We are not inclined to review that holding. See
   <em>
    Adickes
   </em>
   v.
   <em>
    S. H. Kress &amp; Co.,
   </em>
   <span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#152" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 152-161</a></span> (1970).
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b200-9">
   In holding that the Fourth Amendment’s reach extends to property as such, we are mindful that the Amendment does not protect possessory interests in all kinds of property. See,
   <em>
    e. g., Oliver
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9429563"><a href="/opinion/111146/oliver-v-united-states/#176" aria-description="Citation for case: Oliver v. United States">466 U. S. 170, 176-177</a></span> (1984). This case, however, concerns a house, which the Amendment’s language explicitly includes, as it does a person’s effects.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b201-7">
<em>
    <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/" aria-description="Citation for case: United States v. Place">Place</a></span>
   </em>
   also found that to detain luggage for 90 minutes was an unreasonable deprivation of the individual’s “liberty interest in proceeding with his itinerary,” which also is protected by the Fourth Amendment. <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#708" aria-description="Citation for case: United States v. Place">462 U. S., at 708-710</a></span>.
  </p>
</div><div class="footnote" id="fn9" label="9">
<a class="footnote" href="#fn9_ref">
   9
  </a>
<p id="b204-6">
   When “operational necessities” exist, seizures can be justified on less than probable cause. 480 U. S., at 327. That in no way affects our analysis, for even then it is clear that the Fourth Amendment applies.
   <em>
    Ibid.;
   </em>
   see also
   <em>
    United States
   </em>
   v.
   <em>
    Place,
   </em>
   <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#703" aria-description="Citation for case: United States v. Place">462 U. S. 696, 703</a></span> (1983).
  </p>
</div><div class="footnote" id="fn10" label="10">
<a class="footnote" href="#fn10_ref">
   10
  </a>
<p id="b204-7">
   Of course, if the police officers’ presence in the home itself entailed a violation of the Fourth Amendment, no amount of probable cause to believe that an item in plain view constitutes incriminating evidence will justify its seizure.
   <em>
    Horton,
   </em>
   <span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#136" aria-description="Citation for case: Horton v. California">496 U. S., at 136-137</a></span>.
  </p>
</div><div class="footnote" id="fn11" label="11">
<a class="footnote" href="#fn11_ref">
   11
  </a>
<p id="b205-7">
   It is true that
   <em>
    Murray’s Lessee
   </em>
   v.
   <em>
    Hoboken Land &amp; Improvement Co.,
   </em>
   <span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co.">18 How. 272</a></span> (1856), cast some doubt on the applicability of the Amendment to noncriminal encounters such as this.
   <span class="citation" data-id="87010"><a href="/opinion/87010/den-ex-dem-murray-v-hoboken-land-improvement-co/#285" aria-description="Citation for case: Den Ex Dem. Murray v. Hoboken Land &amp; Improvement Co."><em>
    Id.,
   </em>
   at 285</a></span>. But cases since that time have shed a different light, making clear that Fourth Amendment guarantees are triggered by governmental searches and seizures “without regard to the use to which [houses, papers, and effects] are applied.”
   <em>
    Warden, Maryland Penitentiary
   </em>
   v.
   <em>
    Hayden,
   </em>
   <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#301" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 301</a></span> (1967).
   <em>
    Murray’s Lessee’s
   </em>
   broad statement that the Fourth Amendment “has no reference to civil proceedings for the recovery of debt” arguably only meant that the warrant requirement did not apply, as was suggested in
   <em>
    G. M. Leasing Corp.
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/#352" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338, 352</a></span> (1977). Whatever its proper reading, we reaffirm today our basic understanding that the protection against unreasonable searches and seizures fully applies in the civil context.
  </p>
</div><div class="footnote" id="fn12" label="12">
<a class="footnote" href="#fn12_ref">
   12
  </a>
<p id="b205-8">
   This was the view expressed by the Court of Appeals for the Tenth Circuit in
   <em>
    Specht
   </em>
   v.
   <em>
    Jensen,
   </em>
   <span class="citation" data-id="8955392"><a href="/opinion/8964119/specht-v-jensen/" aria-description="Citation for case: Specht v. Jensen">832 F. 2d 1516</a></span> (1987), remanded on unrelated grounds, <span class="citation multiple-matches"><a href="/c/F.%202d/853/805/">853 F. 2d 805</a></span> (1988) (en banc), with which the Seventh Circuit expressly agreed. <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1076" aria-description="Citation for case: Edward Soldal v. County of Cook">942 F. 2d, at 1076</a></span>.
  </p>
</div><div class="footnote" id="fn13" label="13">
<a class="footnote" href="#fn13_ref">
   13
  </a>
<p id="b206-6">
   The officers in these cases were engaged in law enforcement and were ■looking for something that was found and seized. In this broad sense the seizures were the result of “searches,” but not in the Fourth Amendment sense. That the Court of Appeals might have been suggesting that the plain-view cases are explainable because they almost always occur in the course of law enforcement activities receives some support from the penultimate sentence of the quoted passage, where the court states that the word “seizure” might lose its usual meaning “when it stands apart from a search or
   <em>
    any other investigative activity.” Id.,
   </em>
   at 1079 (emphasis added). And, in the following paragraph, it observes that “[ojutside of the law enforcement area the Fourth Amendment retains its force as a protection against searches, because they invade privacy. That is why we decline to confine the amendment to the law enforcement setting.”
   <span class="citation" data-id="9482005"><a href="/opinion/567219/edward-soldal-v-county-of-cook/#1079" aria-description="Citation for case: Edward Soldal v. County of Cook"><em>
    Id.,
   </em>
   at 1079-1080</a></span>. Even if the court meant that seizures of property in the course of law enforcement activities, whether civil or criminal, implicate interests safeguarded by the Fourth Amendment, but that pure property interests are unprotected in the non-law-enforcement setting, we are not in accord, as indicated in the body of this opinion.
  </p>
</div></div></opinion>
```

---
