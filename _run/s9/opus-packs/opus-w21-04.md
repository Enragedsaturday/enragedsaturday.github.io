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

## GROUP: _overhaul2/lake/cases/Welsh v. Wisconsin.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Welsh v. Wisconsin"
type: case
citation: "466 U.S. 740 (1984)"
parallel_cite: "104 S. Ct. 2091; 80 L. Ed. 2d 732; 52 U.S.L.W. 4581"
neutral_cite: 1984 U.S. LEXIS 82
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-05-15
docket: 82-5466
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-05-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Welsh v. Wisconsin
  varies_by_point: false
  scope_note: "Gravity-of-offense factor reaffirmed; good law (cf. Lange v. California (2021), misdemeanor hot pursuit is not categorical)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111173/welsh-v-wisconsin/"
  cluster_id: 111173
  opinion_id: 9429597
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Related (cross-doctrine)"
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Key — Progeny / Refinement"
related: ["[[Payton v. New York]]", "[[Lange v. California]]", "[[Kentucky v. King]]"]
aliases: ["Welsh"]
tags: ["case", "fourth-amendment", "exigent-circumstances", "arrest-in-the-home", "minor-offense", "dui"]
holding: "The gravity of the underlying offense is a key factor in the exigency analysis; warrantless home entry for a MINOR offense should rarely…"
lake:
  record_id: Welsh v. Wisconsin
  status: verified
  projected_at: 2026-07-09
---

# Welsh v. Wisconsin

*466 U.S. 740 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A witness saw Welsh drive erratically, swerve off the road, and stop in a field; Welsh then abandoned his car and walked home. Acting on the report, police checked the car's registration, went to Welsh's house without a warrant, entered, found him in his upstairs bedroom, and arrested him for driving while intoxicated. Under Wisconsin law, a first DWI offense was a noncriminal civil forfeiture punishable only by a fine, with no possible imprisonment.

## Issue
Whether police may make a warrantless, nighttime entry into a suspect's home to arrest him for a minor, noncriminal traffic offense, on the theory that [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] (preserving blood-alcohol evidence) justified the entry.

## Rule
The seriousness of the crime bears directly on whether an [[Exigent Circumstances and Hot Pursuit|exigency]] justifies a warrantless home entry: the Court "hold[s] that an important factor to be considered when determining whether any exigency exists is the gravity of the underlying offense for which the arrest is being made." — 466 U.S. at 753. ^pin-753

For minor offenses, [[Exigent Circumstances and Hot Pursuit|exigency]] will seldom suffice: "application of the exigent-circumstances exception in the context of a home entry should rarely be sanctioned when there is probable cause to believe that only a minor offense, such as the kind at issue in this case, has been committed." — *Id.* And a warrantless home arrest for such an offense is "clearly prohibited by the special protection afforded the individual in his home by the Fourth Amendment." — [*Id.* at 755](https://www.courtlistener.com/opinion/111173/welsh-v-wisconsin/#:~:text=application%20of%20the%20exigent%2Dcircumstances%20exception%20in). ^pin-755

## Application
On these facts no [[Exigent Circumstances and Hot Pursuit|exigency]] justified the entry. [[Exigent Circumstances and Hot Pursuit|Hot pursuit]] did not apply because there was no immediate or continuous pursuit from the scene. With Welsh already home and his car abandoned at the scene, there was little remaining threat to public safety. The only claimed emergency was the dissipation of his blood-alcohol level — but because Wisconsin had classified a first DWI offense as a noncriminal civil forfeiture with no jail, the State's minimal interest could not justify a warrantless entry into the home. The arrest was therefore unreasonable.

## Conclusion
The warrantless, nighttime home entry to arrest Welsh for a civil traffic offense was invalid; the judgment of the Wisconsin Supreme Court was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Welsh* applies the home-entry protection of [[Payton v. New York]] and supplies the gravity-of-offense factor for the [[Exigent Circumstances and Hot Pursuit|exigency]] analysis later framed in [[Kentucky v. King]]. [[Lange v. California]] (2021) reinforces *Welsh*'s caution, holding that pursuit of a fleeing misdemeanant does not categorically justify a warrantless home entry — the [[Exigent Circumstances and Hot Pursuit|exigency]] must be assessed case by case.

## Appears on
- [[Arrest in the Home]] — *Related (cross-doctrine)*
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Progeny / Refinement*

## Sources
- *Welsh v. Wisconsin*, 466 U.S. 740 (1984) — https://www.courtlistener.com/opinion/111173/welsh-v-wisconsin/ — pinpoints: 753, 755.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a75c517c53063308", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Welsh v. Wisconsin"}, "payload": {"all": [{"cite": "466 U.S. 740", "page": "740", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "466"}, {"cite": "104 S. Ct. 2091", "page": "2091", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "80 L. Ed. 2d 732", "page": "732", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "1984 U.S. LEXIS 82", "page": "82", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4581", "page": "4581", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "466 U.S. 740", "official": {"cite": "466 U.S. 740", "page": "740", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "466"}, "official_selection_present": true, "record_id": "Welsh v. Wisconsin"}}
{"assertion_id": "67d79e7cd7d1c051", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-755", "record_id": "Welsh v. Wisconsin"}, "payload": {"fragment": "#:~:text=application%20of%20the%20exigent%2Dcircumstances%20exception%20in", "page": null, "pin_id": "pin-755", "pinpoint_status": "star-verified", "quote": "application of the exigent-circumstances exception in the context of a home entry should rarely be sanctioned when there is probable cause to believe that only a minor offense, such as the kind at issue in this case, has been committed.", "quote_fidelity": "matched", "record_id": "Welsh v. Wisconsin", "star_marker": "753"}}
{"assertion_id": "fc5682fece552e3c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-753", "record_id": "Welsh v. Wisconsin"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-753", "pinpoint_status": "slip-only", "quote": "--- # Welsh v. Wisconsin *466 U.S. 740 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A witness saw Welsh drive erratically, swerve off the road, and stop in a field; Welsh then abandoned his car and walked home. Acting on the report, police checked the car's registration, went to Welsh's house without a warrant, entered, found him in his upstairs bedroom, and arrested him for driving while intoxicated. Under Wisconsin law, a first DWI offense was a noncriminal civil forfeiture punishable only by a fine, with no possible imprisonment. ## Issue Whether police may make a warrantless, nighttime entry into a suspect's home to arrest him for a minor, noncriminal traffic offense, on the theory that exigent circumstances (preserving blood-alcohol evidence) justified the entry. ## Rule The seriousness of the crime bears directly on whether an exigency justifies a warrantless home entry: the Court", "quote_fidelity": "mismatch", "record_id": "Welsh v. Wisconsin", "star_marker": null}}
{"assertion_id": "ccc6d8f7081f56a9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Welsh v. Wisconsin"}, "payload": {"as_of_content": "1984-05-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Welsh v. Wisconsin", "scope_note": "Gravity-of-offense factor reaffirmed; good law (cf. Lange v. California (2021), misdemeanor hot pursuit is not categorical).", "varies_by_point": false}}
```

### lake record — Welsh v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "Welsh v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Welsh v. Wisconsin",
    "case_name_short": "Welsh",
    "case_name_full": "Welsh v. Wisconsin",
    "input_case_name": "Welsh v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-05-15",
    "year": 1984,
    "docket": "82-5466",
    "cluster_id": 111173,
    "lead_opinion_id": 9429597,
    "sibling_ids": [
      111173,
      9429597,
      9429598,
      9429599
    ],
    "absolute_url": "/opinion/111173/welsh-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "466 U.S. 740",
      "volume": "466",
      "reporter": "U.S.",
      "page": "740",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2091",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2091",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 732",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "732",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4581",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4581",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 82",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "466 U.S. 740",
        "volume": "466",
        "reporter": "U.S.",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2091",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2091",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 732",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "732",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 82",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4581",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4581",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "466 U.S. 740",
    "official_selection": {
      "court_class": "scotus",
      "selected": "466 U.S. 740",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-753",
      "page": null,
      "quote": "--- # Welsh v. Wisconsin *466 U.S. 740 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A witness saw Welsh drive erratically, swerve off the road, and stop in a field; Welsh then abandoned his car and walked home. Acting on the report, police checked the car's registration, went to Welsh's house without a warrant, entered, found him in his upstairs bedroom, and arrested him for driving while intoxicated. Under Wisconsin law, a first DWI offense was a noncriminal civil forfeiture punishable only by a fine, with no possible imprisonment. ## Issue Whether police may make a warrantless, nighttime entry into a suspect's home to arrest him for a minor, noncriminal traffic offense, on the theory that exigent circumstances (preserving blood-alcohol evidence) justified the entry. ## Rule The seriousness of the crime bears directly on whether an exigency justifies a warrantless home entry: the Court",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-755",
      "page": null,
      "quote": "application of the exigent-circumstances exception in the context of a home entry should rarely be sanctioned when there is probable cause to believe that only a minor offense, such as the kind at issue in this case, has been committed.",
      "star_marker": "753",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26435,
      "fragment": "#:~:text=application%20of%20the%20exigent%2Dcircumstances%20exception%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-05-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Welsh v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Gravity-of-offense factor reaffirmed; good law (cf. Lange v. California (2021), misdemeanor hot pursuit is not categorical).",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Shawn J. Sivertson",
          "cluster_id": 4396228,
          "cite": [
            "29 N.Y.3d 1006",
            "77 N.E.3d 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barry Trynell Davis, Jr. v. State of Florida",
          "cluster_id": 4390534,
          "cite": [
            "217 So. 3d 1006",
            "42 Fla. L. Weekly Supp. 558",
            "2017 WL 1954979",
            "2017 Fla. LEXIS 1055"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Todd Eugene Trahan",
          "cluster_id": 4311782,
          "cite": [
            "886 N.W.2d 216",
            "2016 Minn. LEXIS 660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christopher McCoy v. United States",
          "cluster_id": 3182195,
          "cite": [
            "815 F.3d 292",
            "2016 U.S. App. LEXIS 3947",
            "2016 WL 814644"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
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
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lucas v. South Carolina Coastal Council",
          "cluster_id": 112787,
          "cite": [
            "120 L. Ed. 2d 798",
            "112 S. Ct. 2886",
            "505 U.S. 1003",
            "1992 U.S. LEXIS 4537"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Olson",
          "cluster_id": 112416,
          "cite": [
            "109 L. Ed. 2d 85",
            "110 S. Ct. 1684",
            "495 U.S. 91",
            "1990 U.S. LEXIS 2038",
            "58 U.S.L.W. 4464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 1228080,
          "cite": [
            "729 P.2d 839",
            "43 Cal. 3d 171",
            "233 Cal. Rptr. 404",
            "1987 Cal. LEXIS 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marvin Berkowitz",
          "cluster_id": 557342,
          "cite": [
            "927 F.2d 1376",
            "1991 U.S. App. LEXIS 4135",
            "1991 WL 33079"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanton v. Sims",
          "cluster_id": 2641101,
          "cite": [
            "187 L. Ed. 2d 341",
            "134 S. Ct. 3",
            "2013 U.S. LEXIS 7773",
            "82 U.S.L.W. 4003",
            "571 U.S. 3",
            "24 Fla. L. Weekly Fed. S 473",
            "2013 WL 5878007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxine Veatch v. Bartels Lutheran Home",
          "cluster_id": 181829,
          "cite": [
            "627 F.3d 1254",
            "2010 U.S. App. LEXIS 26270",
            "2010 WL 5293814"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Johnson",
          "cluster_id": 773999,
          "cite": [
            "256 F.3d 895",
            "2001 Daily Journal DAR 7479",
            "2001 Cal. Daily Op. Serv. 6099",
            "2001 U.S. App. LEXIS 16092",
            "2001 WL 817633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emil Ewolski v. City of Brunswick",
          "cluster_id": 777338,
          "cite": [
            "287 F.3d 492",
            "2002 U.S. App. LEXIS 7129",
            "2002 WL 571329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDE0MDIyNDAwMDAwJnM9Mjc0NTA2NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111173+OR+9429597+OR+9429598+OR+9429599%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjAmcz00MzIxMDM0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111173+OR+9429597+OR+9429598+OR+9429599%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599)",
    "indexed_citing_opinions": 1133,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111173,
        "count": 1004,
        "count_source": "search"
      },
      {
        "opinion_id": 9429597,
        "count": 141,
        "count_source": "search"
      },
      {
        "opinion_id": 9429598,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429599,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1875,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/welsh-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2MTI5NTUmcz05NDU4MDQwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111173+OR+9429597+OR+9429598+OR+9429599%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111173,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 101618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 102196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 105404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 317151,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 358582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 391450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1149829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1223369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1383130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1482307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1585837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1612671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1696609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1927305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2064400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2081551,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2108751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2178478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2196053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2222516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2295125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2404257,
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
    "date_created": "2026-07-06T04:13:32Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:13:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:13:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:16:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:13:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Welsh v. Wisconsin

```
<opinion type="majority">
<author id="b801-10">Justice Brennan</author>
<p id="Ago">delivered the opinion of the Court.</p>
<p id="AKL"><em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), held that, absent probable cause and exigent circumstances, warrantless arrests in the home are prohibited by the Fourth Amend<page-number citation-index="1" label="742">*742</page-number>ment. But the Court in that case explicitly refused “to consider the sort of emergency or dangerous situation, described in our cases as ‘exigent circumstances,’ that would justify a warrantless entry into a home for the purpose of either arrest or search.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 583</a></span>. Certiorari was granted in this case to decide at least one aspect of the unresolved question: whether, and if so under what circumstances, the Fourth Amendment prohibits the police from making a warrantless night entry of a person’s home in order to arrest him for a nonjailable traffic offense.</p>
<p id="b802-8">h — &lt;</p>
<p id="b802-3">A</p>
<p id="b802-4">Shortly before 9 o’clock on the rainy night of April 24,1978, a lone witness, Randy Jablonic, observed a car being driven erratically. After changing speeds and veering from side to side, the car eventually swerved off the road and came to a stop in an open field. No damage to any person or property occurred. Concerned about the driver and fearing that the car would get back on the highway, Jablonic drove his truck up behind the car so as to block it from returning to the road. Another passerby also stopped at the scene, and Jablonic asked her to call the police. Before the police arrived, however, the driver of the car emerged from his vehicle, approached Jablonic’s truck, and asked Jablonic for a ride home. Jablonic instead suggested that they wait for assistance in removing or repairing the car. Ignoring Jablonic’s suggestion, the driver walked away from the scene.</p>
<p id="b802-5">A few minutes later, the police arrived and questioned Jablonic. He told one officer what he had seen, specifically noting that the driver was either very inebriated or very sick. The officer checked the motor vehicle registration of the abandoned car and learned that it was registered to the petitioner, Edward G. Welsh. In addition, the officer noted that the petitioner’s residence was a short distance from the scene, and therefore easily within walking distance.</p>
<p id="b803-4"><page-number citation-index="1" label="743">*743</page-number>Without securing any type of warrant, the police proceeded to the petitioner’s home, arriving about 9 p. m. When the petitioner’s stepdaughter answered the door, the police gained entry into the house.<footnotemark>1</footnotemark> Proceeding upstairs to the petitioner’s bedroom, they found him lying naked in bed. At this point, the petitioner was placed under arrest for driving or operating a motor vehicle while under the influence of an intoxicant, in violation of <span class="citation no-link">Wis. Stat. §346.63</span>(1) (1977).<footnotemark>2</footnotemark> The petitioner was taken to the police station, where he refused to submit to a breath-analysis test.</p>
<p id="b803-5">B</p>
<p id="b803-6">As a result of these events, the petitioner was subjected to two separate but related proceedings: one concerning his refusal to submit to a breath test and the other involving the alleged code violation for driving while intoxicated. Under the Wisconsin Vehicle Code in effect in April 1978, one arrested for driving while intoxicated under §346.63(1) could be requested by a law enforcement officer to provide breath, blood, or urine samples for the purpose of determining the presence or quantity of alcohol. <span class="citation no-link">Wis. Stat. §343.305</span>(1) (1975). If such a request was made, the arrestee was re<page-number citation-index="1" label="744">*744</page-number>quired to submit to the appropriate testing or risk a revocation of operating privileges. Cf. <em>South Dakota </em>v. <em>Neville, </em><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553</a></span> (1983) (admission into evidence of a defendant’s refusal to submit to a blood-alcohol test does not offend constitutional right against self-incrimination). The arrestee could challenge the officer’s request, however, by refusing to undergo testing and then asking for a hearing to determine whether the refusal was justified. If, after the hearing, it was determined that the refusal was not justified, the arrest-ee’s operating privileges would be revoked for 60 days.<footnotemark>3</footnotemark></p>
<p id="b804-5">The statute also set forth specific criteria to be applied by a court when determining whether an arrestee’s refusal to take a breath test was justified. Included among these criteria was a requirement that, before revoking the arrestee’s operating privileges, the court determine that “the refusal. . . to submit to a test was unreasonable.” § 343.305(2)(b)(5) (1975). It is not disputed by the parties that an arrestee’s refusal to take a breath test would be reasonable, and therefore operating privileges could not be revoked, if the underlying arrest was not lawful. Indeed, state law has consistently provided that a valid arrest is a necessary prerequisite to the imposition of a breath test. See <em>Scales </em>v. <em>State, </em><span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#494" aria-description="Citation for case: Scales v. State">64 Wis. 2d 485, 494</a></span>, <span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#292" aria-description="Citation for case: Scales v. State">219 N. W. 2d 286, 292</a></span> (1974).<footnotemark>4</footnotemark> Although the stat<page-number citation-index="1" label="745">*745</page-number>ute in effect in April 1978 referred to reasonableness, the current version of §343.305 explicitly recognizes that one of the issues that an arrestee may raise at a refusal hearing is “whether [he] was lawfully placed under arrest for violation of s.346.63(l).» §§343.306(3)(b)(5)(a), (8)(b) (1981-1982). See also 67 Op. Wis. Atty. Gen. No. 93-78 (1978) (“statutory <page-number citation-index="1" label="746">*746</page-number>scheme . . . contemplates that a lawful arrest be made prior to a request for submission to a test”).<footnotemark>5</footnotemark></p>
<p id="b806-5">Separate statutory provisions control the penalty that might be imposed for the substantive offense of driving while intoxicated. At the time in question, the Vehicle Code provided that a first offense for driving while intoxicated was a noncriminal violation subject to a civil forfeiture proceeding for a maximum fine of $200; a second or subsequent offense in the previous five years was a potential misdemeanor that could be punished by imprisonment for up to one year and a maximum fine of $500. <span class="citation no-link">Wis. Stat. §346.65</span>(2) (1975). Since that time, the State has made only minor amendments to these penalty provisions. Indeed, the statute continues to categorize a first offense as a civil violation that allows for only a monetary forfeiture of no more than $300. §346.65(2)(a) (Supp. 1983-1984). See <em>State </em>v. <em>Albright, </em><span class="citation" data-id="2064400"><a href="/opinion/2064400/state-v-albright/#672" aria-description="Citation for case: State v. Albright">98 Wis. 2d 663, 672-673</a></span>, <span class="citation" data-id="2064400"><a href="/opinion/2064400/state-v-albright/#202" aria-description="Citation for case: State v. Albright">298 N. W. 2d 196, 202</a></span> (App. 1980).</p>
<p id="b806-7">C</p>
<p id="b806-8">As noted, in this case the petitioner refused to submit to a breath test; he subsequently filed a timely request for a refusal hearing. Before that hearing was held, however, the State filed a criminal complaint against the petitioner for driving while intoxicated.<footnotemark>6</footnotemark> The petitioner responded by <page-number citation-index="1" label="747">*747</page-number>filing a motion to dismiss the complaint, relying on his contention that the underlying arrest was invalid. After receiving evidence at a hearing on this motion in July 1980, the trial court concluded that the criminal complaint would not be dismissed because the existence of both probable cause and exigent circumstances justified the warrantless arrest. The decision at the refusal hearing, which was not held until September 1980, was therefore preordained. In fact, the primary issue at the refusal hearing — whether the petitioner acted reasonably in refusing to submit to a breath test because he was unlawfully placed under arrest, see <em>supra, </em>at 744-746 — had already been determined two months earlier by the same trial court.</p>
<p id="b807-5">As expected, after the refusal hearing, the trial court concluded that the arrest of the petitioner was lawful and that the petitioner’s refusal to take the breath test was therefore unreasonable.<footnotemark>7</footnotemark> Accordingly, the court issued an order suspending the petitioner’s operating license for 60 days. On appeal, the suspension order was vacated by the Wisconsin Court of Appeals. See <em>State </em>v. <em>Welsh, </em>No. 80-1686 (May 26, 1981), App. 114-125. Contrary to the trial court, the appellate court concluded that the warrantless arrest of the petitioner in his home violated the Fourth Amendment because the State, although demonstrating probable cause to arrest, had not established the existence of exigent circumstances. The petitioner’s refusal to submit to a breath test was therefore reasonable.<footnotemark>8</footnotemark> The Supreme Court of Wisconsin in turn reversed the Court of Appeals, relying on the existence of <page-number citation-index="1" label="748">*748</page-number>three factors that it believed constituted exigent circumstances: the need for “hot pursuit” of a suspect, the need to prevent physical harm to the offender and the public, and the need to prevent destruction of evidence. See <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#336" aria-description="Citation for case: State v. Welsh">108 Wis. 2d 319, 336-338</a></span>, <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#254" aria-description="Citation for case: State v. Welsh">321 N. W. 2d 245, 254-255</a></span> (1982). Because of the important Fourth Amendment implications of the decision below, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./459/1200/">459 U. S. 1200</a></span> (1983).<footnotemark>9</footnotemark></p>
<p id="pAEJ">II</p>
<p id="b808-3">It is axiomatic that the “physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed.” <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972). And a principal protection against unnecessary intrusions into private dwellings is the warrant requirement imposed by the Fourth Amendment on agents of the government who seek to enter the home for purposes of search or arrest. See <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948).<footnotemark>10</footnotemark> It is not surprising, therefore, <page-number citation-index="1" label="749">*749</page-number>that the Court has recognized, as “a ‘basic principle of Fourth Amendment law[,]’ that searches and seizures inside a home without a warrant are presumptively unreasonable. ” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S., at 586</a></span>. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-475</a></span> (1971) (“a search or seizure carried out on a suspect’s premises without a warrant is <em>per se </em>unreasonable, unless the police can show. . . the presence of ‘exigent circumstances’ ”). See also <em>Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#296" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287, 296-297</a></span> (1984) (plurality opinion); <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U. S. 204, 211-212</a></span> (1981); <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span> (1948); <em>Johnson </em>v. <em>United States, supra, </em>at 13-15; <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886).</p>
<p id="b809-5">Consistently with these long-recognized principles, the Court decided in <em>Payton </em>v. <em>New <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">York, supra,</a></span> </em>that warrant-less felony arrests in the home are prohibited by the Fourth Amendment, absent probable cause and exigent circumstances. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 583-590</a></span>. At the same time, the Court declined to consider the scope of any exception for exigent circumstances that might justify warrantless home arrests, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York"><em>id., </em>at 583</a></span>, thereby leaving to the lower courts the initial application of the exigent-circumstances exception.<footnotemark>11</footnotemark> Prior decisions of this Court, however, have emphasized that exceptions to the warrant requirement are “few in number and carefully delineated,” <em>United States </em>v. <em>United States District Court, supra, </em>at 318, and that the police bear a heavy burden <page-number citation-index="1" label="750">*750</page-number>when attempting to demonstrate an urgent need that might justify warrantless searches or arrests. Indeed, the Court has recognized only a few such emergency conditions, see, <em>e. g., United States </em>v. <em>Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42-43</a></span> (1976) (hot pursuit of a fleeing felon); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span> (1967) (same); <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (1966) (destruction of evidence); <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 509</a></span> (1978) (ongoing fire), and has actually applied only the “hot pursuit” doctrine to arrests in the home, see <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana, supra.</a></span></em></p>
<p id="b810-5">Our hesitation in finding exigent circumstances, especially when warrantless arrests in the home are at issue, is particularly appropriate when the underlying offense for which there is probable cause to arrest is relatively minor. Before agents of the government may invade the sanctity of the home, the burden is on the government to demonstrate exigent circumstances that overcome the presumption of unreasonableness that attaches to all warrantless home entries. See <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 586</a></span>. When the government’s interest is only to arrest for a minor offense,<footnotemark>12</footnotemark> that presumption of unreasonableness is difficult to rebut, and the government usually should be allowed to make such arrests only with a warrant issued upon probable cause by a neutral and detached magistrate.</p>
<p id="b810-6">This is not a novel idea. Writing in concurrence in <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948), Justice Jackson explained why a finding of exigent circumstances to justify a warrantless home entry should be severely restricted when only a minor offense has been committed:</p>
<blockquote id="b811-4"><page-number citation-index="1" label="751">*751</page-number>“Even if one were to conclude that urgent circumstances might justify a forced entry without a warrant, no such emergency was present in this case. This method of law enforcement displays a shocking lack of all sense of proportion. Whether there is reasonable necessity for a search without waiting to obtain a warrant certainly depends somewhat upon the gravity of the offense thought to be in progress as well as the hazards of the method of attempting to reach it.. . . It is to me a shocking proposition that private homes, even quarters in a tenement, may be indiscriminately invaded at the discretion of any suspicious police officer engaged in following up offenses that involve no violence or threats of it. While I should be human enough to apply the letter of the law with some indulgence to officers acting to deal with threats or crimes of violence which endanger life or security, it is notable that few of the searches found by this Court to be unlawful dealt with that category of crime. . . . While the enterprise of parting fools from their money by the ‘numbers’ lottery is one that ought to be suppressed, I do not think its suppression is more important to society than the security of the people against unreasonable searches and seizures. When an officer undertakes to act as his own magistrate, he ought to be in a position to justify it by pointing to some real immediate and serious consequences if he postponed action to get a warrant.” <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#459" aria-description="Citation for case: McDonald v. United States"><em>Id., </em>at 459-460</a></span> (footnote omitted).</blockquote>
<p id="b811-5">Consistently with this approach, the lower courts have looked to the nature of the underlying offense as an important factor to be considered in the exigent-circumstances calculus. In a leading federal case defining exigent circumstances, for example, the en banc United States Court of Appeals for the District of Columbia Circuit recognized that the gravity of the underlying offense was a principal factor <page-number citation-index="1" label="752">*752</page-number>to be weighed. <em>Dorman </em>v. <em>United States, </em>140 U. S. App. D. C. 313, 320, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/#392" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385, 392</a></span> (1970).<footnotemark>13</footnotemark> Without approving all of the factors included in the standard adopted by that court, it is sufficient to note that many other lower courts have also considered the gravity of the offense an important part of their constitutional analysis.</p>
<p id="b812-5">For example, courts have permitted warrantless home arrests for major felonies if identifiable exigencies, independent of the gravity of the offense, existed at the time of the arrest. Compare <em>United States </em>v. <em>Campbell, </em><span class="citation" data-id="358582"><a href="/opinion/358582/united-states-v-david-campbell-and-michael-tartt/" aria-description="Citation for case: United States v. David Campbell and Michael Tartt">581 F. 2d 22</a></span> (CA2 1978) (allowing warrantless home arrest for armed robbery when exigent circumstances existed), with <em>Commonwealth </em>v. <em>Williams, </em><span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">483 Pa. 293</a></span>, <span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">396 A. 2d 1177</a></span> (1978) (disallowing war-rantless home arrest for murder due to absence of exigent circumstances). But of those courts addressing the issue, most have refused to permit warrantless home arrests for nonfelonious crimes. See, <em>e. g., State </em>v. <em>Guertin, </em><span class="citation" data-id="2404257"><a href="/opinion/2404257/state-v-guertin/#453" aria-description="Citation for case: State v. Guertin">190 Conn. 440, 453</a></span>, <span class="citation" data-id="2404257"><a href="/opinion/2404257/state-v-guertin/#970" aria-description="Citation for case: State v. Guertin">461 A. 2d 963, 970</a></span> (1983) (“The [exigent-circumstances] exception is narrowly drawn to cover cases of real and not contrived emergencies. The exception is limited to the investigation of serious crimes; misdemeanors are excluded”); <em>People </em>v. <em>Strelow, </em><span class="citation" data-id="2222516"><a href="/opinion/2222516/people-v-strelow/#190" aria-description="Citation for case: People v. Strelow">96 Mich. App. 182, 190-193</a></span>, <span class="citation" data-id="2222516"><a href="/opinion/2222516/people-v-strelow/#521" aria-description="Citation for case: People v. Strelow">292 N. W. 2d 517, 521-522</a></span> (1980). See also <em>People </em>v. <em>Sanders, </em><span class="citation" data-id="2081551"><a href="/opinion/2081551/people-v-sanders/" aria-description="Citation for case: People v. Sanders">59 Ill. App. 3d 6</a></span>, <span class="citation" data-id="2081551"><a href="/opinion/2081551/people-v-sanders/" aria-description="Citation for case: People v. Sanders">374 N. E. 2d 1315</a></span> (1978) (burglary without weapons not grave offense of violence for this purpose); <em>State </em>v. <em>Bennett, </em><span class="citation" data-id="2178478"><a href="/opinion/2178478/state-v-bennett/" aria-description="Citation for case: State v. Bennett">295 N. W. 2d 5</a></span> (S. D. 1980) (distribution of controlled substances not a grave offense for these purposes). But cf. <em>State </em>v. <em>Penas, </em><span class="citation" data-id="9697068"><a href="/opinion/1927305/state-v-penas/" aria-description="Citation for case: State v. Penas">200 Neb. 387</a></span>, <span class="citation" data-id="9697068"><a href="/opinion/1927305/state-v-penas/" aria-description="Citation for case: State v. Penas">263 N. W. 2d 835</a></span> (1978) (allowing warrantless home arrest upon hot pursuit from commission of misdemeanor in the officer’s presence; decided before Payton); <em>State </em>v. <em>Niedermeyer, </em><span class="citation" data-id="1149829"><a href="/opinion/1149829/state-v-niedermeyer/" aria-description="Citation for case: State v. Niedermeyer">48 Ore. App. 665</a></span>, <span class="citation" data-id="1149829"><a href="/opinion/1149829/state-v-niedermeyer/" aria-description="Citation for case: State v. Niedermeyer">617 <page-number citation-index="1" label="753">*753</page-number>P. 2d 911</a></span> (1980) (allowing warrantless home arrest upon hot pursuit from commission of misdemeanor in the officer’s presence). The approach taken in these cases should not be surprising. Indeed, without necessarily approving any of these particular holdings or considering every possible factual situation, we note that it is difficult to conceive of a warrantless home arrest that would not be unreasonable under the Fourth Amendment when the underlying offense is extremely minor.</p>
<p id="b813-5">We therefore conclude that the common-sense approach utilized by most lower courts is required by the Fourth Amendment prohibition on “unreasonable searches and seizures,” and hold that an important factor to be considered when determining whether any exigency exists is the gravity of the underlying offense for which the arrest is being made. Moreover, although no exigency is created simply because there is probable cause to believe that a serious crime has been committed, see <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>application of the exigent-circumstances exception in the context of a home entry should rarely be sanctioned when there is probable cause to believe that only a minor offense, such as the kind at issue in this case, has been committed.</p>
<p id="b813-6">Application of this principle to the facts of the present case is relatively straightforward. The petitioner was arrested in the privacy of his own bedroom for a noncriminal, traffic offense. The State attempts to justify the arrest by relying on the hot-pursuit doctrine, on the threat to public safety, and on the need to preserve evidence of the petitioner’s blood-alcohol level. On the facts of this case, however, the claim of hot pursuit is unconvincing because there was no immediate or continuous pursuit of the petitioner from the scene of a crime. Moreover, because the petitioner had already arrived home, and had abandoned his car at the scene of the accident, there was little remaining threat to the public safety. Hence, the only potential emergency claimed by the State was the need to ascertain the petitioner’s blood-alcohol level.</p>
<p id="b814-6"><page-number citation-index="1" label="754">*754</page-number>Even assuming, however, that the underlying facts would support a finding of this exigent circumstance, mere similarity to other cases involving the imminent destruction of evidence is not sufficient. The State of Wisconsin has chosen to classify the first offense for driving while intoxicated as a noncriminal, civil forfeiture offense for which no imprisonment is possible. See <span class="citation no-link">Wis. Stat. §346.65</span>(2) (1975); §346.65(2)(a) (Supp. 1983-1984); <em>supra, </em>at 746. This is the best indication of the State’s interest in precipitating an arrest, and is one that can be easily identified both by the courts and by officers faced with a decision to arrest. See n. 6, <em>supra. </em>Given this expression of the State’s interest, a warrantless home arrest cannot be upheld simply because evidence of the petitioner’s blood-alcohol level might have dissipated while the police obtained a warrant.<footnotemark>14</footnotemark> To allow a warrantless home entry on these facts would be to approve unreasonable police behavior that the principles of the Fourth Amendment will not sanction.</p>
<p id="pAQW">hH I — I 1 — I</p>
<p id="b814-3">The Supreme Court of Wisconsin let stand a warrant-less, nighttime entry into the petitioner’s home to arrest him for a civil traffic offense. Such an arrest, however, is clearly prohibited by the special protection afforded the individual in his home by the Fourth Amendment. The petitioner’s arrest was therefore invalid, the judgment of the Supreme Court of Wisconsin is vacated, and the case is <page-number citation-index="1" label="755">*755</page-number>remanded for further proceedings not inconsistent with this opinion.<footnotemark>15</footnotemark></p>
<p id="b815-5">
<em>It is so ordered.</em>
</p>
<p id="b815-6">The Chief Justice would dismiss the writ as having been improvidently granted and defer resolution of the question presented to a more appropriate case.</p>
<footnote label="1">
<p id="b803-7"> The state trial court never decided whether there was consent to the entry because it deemed decision of that issue unnecessary in light of its finding that exigent circumstances justified the warrantless arrest. After reversing the lower court’s finding of exigent circumstances, the Wisconsin Court of Appeals remanded for full consideration of the consent issue. See <em>State </em>v. <em>Welsh, </em>No. 80-1686 (May 26, 1981), App. 114-126. That remand never occurred, however, because the Supreme Court of Wisconsin reversed the Court of Appeals and reinstated the trial court’s judgment. See <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/" aria-description="Citation for case: State v. Welsh">108 Wis. 2d 319</a></span>, <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/" aria-description="Citation for case: State v. Welsh">321 N. W. 2d 245</a></span> (1982). For purposes of this decision, therefore, we assume that there was no valid consent to enter the petitioner’s home.</p>
</footnote>
<footnote label="2">
<p id="b803-8"> Since the petitioner’s arrest, §346.63 has been amended to provide that it is a code violation to drive or operate a motor vehicle while under the influence of an intoxicant <em>or </em>while evidencing certain blood- or breath-alcohol levels. See <span class="citation no-link">Wis. Stat. §§346.63</span>(1)(a), (b) (1981-1982). Thisamendment, however, has no bearing on the issues raised by the present case.</p>
</footnote>
<footnote label="3">
<p id="b804-6"> Since the petitioner’s arrest, this statute also has been amended, with the current version found at <span class="citation no-link">Wis. Stat. § 343.305</span> (1981-1982). Although the procedures to be followed by the law enforcement officer and the ar-restee have remained essentially unchanged, §§ 343.305(3), (8), the potential length of any revocation of operating privileges has been increased, depending on the arrestee’s prior driving record, §§ 343.305(9)(a), (b). An arrestee who improperly refuses to submit to a required test may also be required to comply with an assessment order and a driver safety plan, §§343.305(9)(c)-(e). These amendments, however, also have no direct bearing on the issues raised by the present case.</p>
</footnote>
<footnote label="4">
<p id="b804-7"> “The implied consent law does not limit the right to take a blood sample as an incident to a <em>lawful </em>arrest. <em>It should be emphasized, however, that the arrest, and therefore probable cause for making it, must precede the taking of the blood sample. </em>We conclude that the sample was constitu<page-number citation-index="1" label="745">*745</page-number>tionally taken incident to the <em>lawful </em>arrest.” <span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#494" aria-description="Citation for case: Scales v. State">64 Wis. 2d, at 494</a></span>, <span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#292" aria-description="Citation for case: Scales v. State">219 N. W. 2d, at 292</a></span> (emphasis added).</p>
<p id="AYY">Nor is there any doubt that the Supreme Court of Wisconsin applies federal constitutional standards when determining whether an arrest, even for a nonjailable traffic offense, is lawful. The court, for example, explained the basis for its holding in this case as follows:</p>
<blockquote id="At7y">“The trial court revoked the defendant’s motor vehicle operator’s license for sixty days pursuant to his unreasonable refusal to submit to a breathalyzer test, as required by [state statute].</blockquote>
<blockquote id="AbD">“The defendant challenges the officer’s warrantless arrest in his residence as violating the Fourth Amendment of the United States Constitution and Article I, section 11 of the Wisconsin Constitution. The [trial court] upheld this warrantless arrest concluding that probable cause to believe that the defendant had been operating a motor vehicle while under the influence of an intoxicant, coupled with the existence of exigent circumstances, justified the officers’ entry into the defendant’s residence. . . . [T]he court of appeals reversed the trial court, holding that, although the officers’ warrantless arrest was unreasonable, thereby violating the Fourth and Fourteenth Amendments, the absence of a finding regarding the consensual entry necessitated remanding the case on that issue. We affirm the findings of the [trial court], holding that the co-existence of probable cause and exigent circumstances in this case justifies the warrantless arrest....</blockquote>
<blockquote id="AyC"><em>“To prevail in this </em>case, <em>the state must prove the co-existence of probable cause and exigent circumstances, justifying the officer’s conduct at the defendant’s residence. We hold that there was ample evidence supporting the trial court’s ruling that the officer’s entry was justified on the basis of both probable cause and exigent circumstances. Entry to effect a war-rantless arrest in a residence is subject to the limitations imposed by both the United States and the Wisconsin Constitutions. U. S. Const. amend. IV; Wis. Const. art. I, sec. 11.” </em><span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#320" aria-description="Citation for case: State v. Welsh">108 Wis. 2d, at 320-321, 326-327</a></span>, <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#246" aria-description="Citation for case: State v. Welsh">321 N. W. 2d, at 246-247, 249-250</a></span> (emphasis added) (citations and footnotes omitted).</blockquote>
</footnote>
<footnote label="5">
<p id="b806-9"> Because state law provides that evidence of the petitioner’s refusal to submit to a breath test is inadmissible if the underlying arrest was unlawful, this case does not implicate the exclusionary rule under the Federal Constitution.</p>
</footnote>
<footnote label="6">
<p id="b806-13"> The petitioner was charged with a criminal misdemeanor because this was his second such citation in the previous five years. See § 346.65(2) (1975). Although the petitioner was subject to a criminal charge, the police conducting the warrantless entry of his home did not know that the petitioner had ever been charged with, or much less convicted of, a prior violation for driving while intoxicated. It must be assumed, therefore, that at the time of the arrest the police were acting as if they were investigating and eventually arresting for a nonjailable traffic offense that constituted only a civil violation under the applicable state law. See <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91, 96</a></span> (1964).</p>
</footnote>
<footnote label="7">
<p id="b807-6"> When ruling from the bench after the refusal hearing, the trial judge specifically indicated:</p>
<blockquote id="b807-7">“[T]he Court is bound by its earlier ruling that that was a valid arrest. And, I think [counsel for the petitioner] certainly will have the right to challenge that on appeal if he appeals this matter, as well as the previous ruling should there be a conviction on the underlying charge.” App. 111. See also <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#112" aria-description="Citation for case: Beck v. Ohio"><em>id., </em>at 112-113</a></span>.</blockquote>
</footnote>
<footnote label="8">
<p id="b807-8"> The court remanded the case for further findings as to whether the police had entered the petitioner’s home with consent. See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="9">
<p id="b808-4"> Although the state courts differed in their respective conclusions concerning exigent circumstances, they each found that the facts known to the police at the time of the warrantless home entry were sufficient to establish probable cause to arrest. The petitioner has not challenged that finding before this Court.</p>
<p id="b808-5">The parallel criminal proceedings against the petitioner, see <em>supra, </em>at 746-747, and n. 6, resulted in a misdemeanor conviction for driving while intoxicated. During the jury trial, held in early 1982, the State introduced evidence of the petitioner's refusal to submit to a breath test. His appeal from that conviction, now before the Wisconsin Court of Appeals, has been stayed pending our decision in this case. See Brief for Petitioner 17, n. 5.</p>
</footnote>
<footnote label="10">
<p id="b808-6"> In <em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span>, </em>Justice Jackson eloquently explained the warrant requirement in the context of a home search:</p>
<blockquote id="b808-7">“The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. . . . The right of officers to thrust themselves into a home is ... a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security <page-number citation-index="1" label="749">*749</page-number>and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.” <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S., at 13-14</a></span> (footnote omitted).</blockquote>
</footnote>
<footnote label="11">
<p id="b809-7"> Our decision in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>allowing warrantless home arrests upon a showing of probable cause and exigent circumstances, was also expressly limited to felony arrests. See, e. <em>g., </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#574" aria-description="Citation for case: Payton v. New York">445 U. S., at 574, 602</a></span>. Because we conclude that, in the circumstances presented by this case, there were no exigent circumstances sufficient to justify a warrantless home entry, we have no occasion to consider whether the Fourth Amendment may impose an absolute ban on warrantless home arrests for certain minor offenses.</p>
</footnote>
<footnote label="12">
<p id="b810-7"> Even the dissenters in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>although believing that warrantless home arrests are not prohibited by the Fourth Amendment, recognized the importance of the felony limitation on such arrests. See <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#616" aria-description="Citation for case: Payton v. New York">id., at 616-617</a></span> (White, J., joined by Burgee, C. J., and Rehnquist, J., dissenting) (“The felony requirement guards against abusive or arbitrary enforcement and ensures that invasions of the home occur only in case of the most serious crimes”).</p>
</footnote>
<footnote label="13">
<p id="b812-6"> See generally Donnino &amp; Girese, Exigent Circumstances for a Warrantless Home Arrest, 45 Albany L. Rev. 90 (1980); Harbaugh &amp; Faust, “Knock on Any Door” — Home Arrests After <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span>, </em><span class="citation no-link">86 Dick. L. Rev. 191</span>, 220-233 (1982); Note, Exigent Circumstances for Warrantless Home Arrests, <span class="citation no-link">23 Ariz. L. Rev. 1171</span> (1981).</p>
</footnote>
<footnote label="14">
<p id="b814-4"> Nor do we mean to suggest that the prevention of drunken driving is not properly of maj or concern to the States. The State of Wisconsin, however, along with several other States, see, <em>e. g., </em><span class="citation no-link">Minn. Stat. §169.121</span> subd. 4 (1982); <span class="citation no-link">Neb. Rev. Stat. §39-669.07</span>(1) (Supp. 1983); S. D. Codified Laws § 32-23-2 (Supp. 1983), has chosen to limit severely the penalties that may be imposed after a first conviction for driving while intoxicated. Given that the classification of state crimes differs widely among the States, the penalty that may attach to any particular offense seems to provide the clearest and most consistent indication of the State’s interest in arresting individuals suspected of committing that offense.</p>
</footnote>
<footnote label="15">
<p id="b815-11"> On remand, the state courts may consider whether the petitioner’s arrest was justified because the police had validly obtained consent to enter his home. See n. 1, <em>supra.</em></p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/White v. Pauly.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "White v. Pauly"
type: case
citation: ""
parallel_cite: "580 U.S. 73; 196 L. Ed. 2d 463; 137 S. Ct. 548; 26 Fla. L. Weekly Fed. S 409; 85 U.S.L.W. 4027"
neutral_cite: "2017 U.S. LEXIS 5; 2017 WL 69170"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-01-09
docket: 16-67
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2017-01-09
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: White v. Pauly
  varies_by_point: false
  scope_note: "Per curiam; good law on the specificity ('particularized') requirement for clearly established law in excessive-force cases."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4374579/white-v-pauly/"
  cluster_id: 4374579
  opinion_id: 4151832
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Use of Force]]"
    role: "Related (cross-doctrine)"
related: ["[[Mullenix v. Luna]]", "[[Ashcroft v. al-Kidd]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "excessive-force", "clearly-established", "per-curiam"]
holding: "Garner and Graham do not by themselves create clearly established law outside an obvious case; an officer who arrives late to an ongoing scene did not violate clearly established law by using deadly force without first shouting a warning."
lake:
  record_id: White v. Pauly
  status: verified
  projected_at: 2026-07-06
---

# White v. Pauly

*580 U.S. 73 (2017)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Responding to a reckless-driving report, New Mexico State Police officers Truesdale and Mariscal approached the Pauly brothers' rural home and (the brothers say without adequately identifying themselves) shouted "Come out or we're coming in." Believing intruders had arrived, the Paulys armed themselves and yelled "We have guns." Officer White arrived late, took cover behind a stone wall, and — without first shouting a warning — shot and killed Samuel Pauly when Samuel pointed a handgun out a window. Samuel's estate sued under § 1983 for excessive force; the district court and a divided Tenth Circuit denied White [[Qualified Immunity|qualified immunity]].

## Issue
Whether Officer White, who arrived late to an ongoing armed confrontation, violated clearly established law by using deadly force without first giving a warning.

## Rule
"Clearly established law" must be specific to the situation, not abstract. "it is again necessary to reiterate the longstanding principle that 'clearly established law' should not be defined 'at a high level of generality' . . . the clearly established law must be 'particularized' to the facts of the case." — 580 U.S. 73 (slip op., at 6) (quoting [[Ashcroft v. al-Kidd]] and *Anderson v. Creighton*). ^pin-73

The panel's reliance on *[[Tennessee v. Garner|Garner]]* and *[[Graham v. Connor|Graham]]* alone could not supply clearly established law: "we have held that *Garner* and *Graham* do not by themselves create clearly established law outside 'an obvious case.'" — *Id.* (slip op., at 7). ^pin-73b

## Application
The Tenth Circuit "failed to identify a case where an officer acting under similar circumstances as Officer White was held to have violated the Fourth Amendment," relying instead on the general principles of *[[Graham v. Connor|Graham]]* and *[[Tennessee v. Garner|Garner]]*. The panel itself called the facts "a unique set of facts and circumstances" given White's late arrival — which alone should have signaled that any violation was not "clearly established." Clearly established law does not prohibit a reasonable officer who arrives late to an ongoing police action from assuming that proper procedures, such as officer identification, were already followed.

## Conclusion
[[Reading and Citing Cases#certiorari-cert|Certiorari]] granted, judgment [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). On the record described by the court of appeals, Officer White did not violate clearly established law and was entitled to [[Qualified Immunity|qualified immunity]]; the Court left open a potential alternative ground concerning what White witnessed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *White* is part of the run of [[Common Legal Terms#per-curiam|per curiam]] qualified-immunity summary reversals applying the high-specificity requirement of [[Ashcroft v. al-Kidd]] and [[Mullenix v. Luna]] to excessive-force claims, holding that [[Graham v. Connor]] and [[Tennessee v. Garner]] supply only general principles. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Use of Force]] — *Related (cross-doctrine)*

## Sources
- *White v. Pauly*, 580 U.S. 73 (2017) (per curiam) — https://www.courtlistener.com/opinion/4374579/white-v-pauly/ — pinpoints: slip op., at 6–7 (CL stores the slip opinion "580 U. S. ____ (2017)"; pins keyed to the official case-start page 73).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a0a132b87585716b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "White v. Pauly"}, "payload": {"all": [{"cite": "580 U.S. 73", "page": "73", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "580"}, {"cite": "196 L. Ed. 2d 463", "page": "463", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "196"}, {"cite": "2017 U.S. LEXIS 5", "page": "5", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2017"}, {"cite": "137 S. Ct. 548", "page": "548", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "26 Fla. L. Weekly Fed. S 409", "page": "409", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "85 U.S.L.W. 4027", "page": "4027", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "85"}, {"cite": "2017 WL 69170", "page": "69170", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2017"}], "display": null, "official": null, "official_selection_present": false, "record_id": "White v. Pauly"}}
{"assertion_id": "0fad058abfc36792", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-73", "record_id": "White v. Pauly"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-73", "pinpoint_status": "slip-only", "quote": "Officer White arrived late, took cover behind a stone wall, and — without first shouting a warning — shot and killed Samuel Pauly when Samuel pointed a handgun out a window. Samuel's estate sued under § 1983 for excessive force; the district court and a divided Tenth Circuit denied White qualified immunity. ## Issue Whether Officer White, who arrived late to an ongoing armed confrontation, violated clearly established law by using deadly force without first giving a warning. ## Rule", "quote_fidelity": "mismatch", "record_id": "White v. Pauly", "star_marker": null}}
{"assertion_id": "8215929e130c8368", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-73b", "record_id": "White v. Pauly"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-73b", "pinpoint_status": "slip-only", "quote": "we have held that *Garner* and *Graham* do not by themselves create clearly established law outside 'an obvious case.'", "quote_fidelity": "mismatch", "record_id": "White v. Pauly", "star_marker": null}}
{"assertion_id": "73270c3e88593c7e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "White v. Pauly"}, "payload": {"as_of_content": "2017-01-09", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "White v. Pauly", "scope_note": "Per curiam; good law on the specificity ('particularized') requirement for clearly established law in excessive-force cases.", "varies_by_point": false}}
```

### lake record — White v. Pauly

```json
{
  "schema_version": "s2.v1",
  "record_id": "White v. Pauly",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "White v. Pauly",
    "case_name_short": "White",
    "case_name_full": "Ray WHITE, Et Al. v. Daniel T. PAULY, as Personal Representative of the Estate of Samuel Pauly, Deceased Et Al.",
    "input_case_name": "White v. Pauly",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-01-09",
    "year": 2017,
    "docket": "16-67",
    "cluster_id": 4374579,
    "lead_opinion_id": 4151832,
    "sibling_ids": [
      4151832,
      9873109,
      9873111
    ],
    "absolute_url": "/opinion/4374579/white-v-pauly/",
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
        "cite": "580 U.S. 73",
        "volume": "580",
        "reporter": "U.S.",
        "page": "73",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "196 L. Ed. 2d 463",
        "volume": "196",
        "reporter": "L. Ed. 2d",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 548",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "548",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 409",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4027",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4027",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 5",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 69170",
        "volume": "2017",
        "reporter": "WL",
        "page": "69170",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "580 U.S. 73",
        "volume": "580",
        "reporter": "U.S.",
        "page": "73",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "196 L. Ed. 2d 463",
        "volume": "196",
        "reporter": "L. Ed. 2d",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 5",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 548",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "548",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 409",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4027",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4027",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 69170",
        "volume": "2017",
        "reporter": "WL",
        "page": "69170",
        "type": 7,
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
      "id": "pin-73",
      "page": null,
      "quote": "Officer White arrived late, took cover behind a stone wall, and \u2014 without first shouting a warning \u2014 shot and killed Samuel Pauly when Samuel pointed a handgun out a window. Samuel's estate sued under \u00a7 1983 for excessive force; the district court and a divided Tenth Circuit denied White qualified immunity. ## Issue Whether Officer White, who arrived late to an ongoing armed confrontation, violated clearly established law by using deadly force without first giving a warning. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-73b",
      "page": null,
      "quote": "we have held that *Garner* and *Graham* do not by themselves create clearly established law outside 'an obvious case.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2017-01-09",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "White v. Pauly",
    "varies_by_point": false,
    "scope_note": "Per curiam; good law on the specificity ('particularized') requirement for clearly established law in excessive-force cases.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Nat'l Rifle Ass'n of Am. v. Vullo",
          "cluster_id": 10635063,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Katie Joseph v. John Doe",
          "cluster_id": 4821017,
          "cite": [
            "981 F.3d 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dawn Crawford v. John Tilley",
          "cluster_id": 5288690,
          "cite": [
            "15 F.4th 752"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morrow v. Meachum",
          "cluster_id": 8443910,
          "cite": [
            "917 F.3d 870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Turner v. Driver",
          "cluster_id": 4349754,
          "cite": [
            "848 F.3d 678",
            "2017 WL 650186",
            "2017 U.S. App. LEXIS 2769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Merritt Sharp, III v. County of Orange",
          "cluster_id": 4427211,
          "cite": [
            "871 F.3d 901",
            "2017 WL 4126947",
            "2017 U.S. App. LEXIS 18148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Naumovski v. Norris",
          "cluster_id": 4647449,
          "cite": [
            "934 F.3d 200"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmon v. City of Arlington",
          "cluster_id": 5292775,
          "cite": [
            "16 F.4th 1159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maria Morales v. Sonya Fry",
          "cluster_id": 4434701,
          "cite": [
            "873 F.3d 817"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gene Bell, Jr. v. City of Southfield, Mich.",
          "cluster_id": 6477591,
          "cite": [
            "37 F.4th 362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Percy Taylor v. Joseph Ways",
          "cluster_id": 4888555,
          "cite": [
            "999 F.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKinney v. City of Middletown",
          "cluster_id": 8243805,
          "cite": [
            "49 F.4th 730"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Will El v. City of Pittsburgh",
          "cluster_id": 4785653,
          "cite": [
            "975 F.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Lopez Ex Rel. Lopez v. Gelhaus",
          "cluster_id": 4428262,
          "cite": [
            "871 F.3d 998",
            "2017 U.S. App. LEXIS 18439"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bledsoe v. Board Cty Comm. Jefferson KS",
          "cluster_id": 8511576,
          "cite": [
            "53 F.4th 589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Natia Sampson v. County of Los Angeles",
          "cluster_id": 4783620,
          "cite": [
            "974 F.3d 1012"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Melton v. Hunt County",
          "cluster_id": 4442642,
          "cite": [
            "875 F.3d 256"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melissa Knibbs v. Anthony Momphard, Jr.",
          "cluster_id": 6456228,
          "cite": [
            "30 F.4th 200"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sloley v. VanBramer",
          "cluster_id": 4686314,
          "cite": [
            "945 F.3d 30"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Lawler v. Hardeman Cnty., Tenn.",
          "cluster_id": 9476181,
          "cite": [
            "93 F.4th 919"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ullery v. Bradley",
          "cluster_id": 4725783,
          "cite": [
            "949 F.3d 1282"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguirre v. City of San Antonio",
          "cluster_id": 4876506,
          "cite": [
            "995 F.3d 395"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cope v. Cogdill",
          "cluster_id": 4897232,
          "cite": [
            "3 F.4th 198"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Radwan v. Manuel",
          "cluster_id": 9302274,
          "cite": [
            "55 F.4th 101"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKenney v. Mangino",
          "cluster_id": 4432664,
          "cite": [
            "873 F.3d 75",
            "2017 WL 4450989",
            "2017 U.S. App. LEXIS 19548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4151832 OR 9873109 OR 9873111) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk1OTgwODAwMDAwJnM9NDc3MTM1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%284151832+OR+9873109+OR+9873111%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(4151832 OR 9873109 OR 9873111)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NyZzPTQ3NDA0MzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284151832+OR+9873109+OR+9873111%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4151832 OR 9873109 OR 9873111)",
        "reviewed": 129,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 129,
        "triage_read": 1,
        "triage_snippet_classified": 128
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4151832 OR 9873109 OR 9873111)",
    "indexed_citing_opinions": 330,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4151832,
        "count": 32,
        "count_source": "search"
      },
      {
        "opinion_id": 9873109,
        "count": 299,
        "count_source": "search"
      },
      {
        "opinion_id": 9873111,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2532,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/white-v-pauly.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNTA0Njcmcz0xMDM1MzA2MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284151832+OR+9873109+OR+9873111%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4151832,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 217703,
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
    "date_created": "2026-07-06T04:16:35Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:19:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — White v. Pauly

```
                 Cite as: 580 U. S. ____ (2017)           1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
RAY WHITE, ET AL. v. DANIEL T. PAULY, AS PERSONAL 

   REPRESENTATIVE OF THE ESTATE OF SAMUEL 

           PAULY, DECEASED ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE TENTH CIRCUIT

              No. 16–67. Decided January 9, 2017


   PER CURIAM.
   This case addresses the situation of an officer who—
having arrived late at an ongoing police action and having
witnessed shots being fired by one of several individuals
in a house surrounded by other officers—shoots and kills
an armed occupant of the house without first giving a
warning.
   According to the District Court and the Court of Ap-
peals, the record, when viewed in the light most favorable
to respondents, shows the following. Respondent Daniel
Pauly was involved in a road-rage incident on a highway
near Santa Fe, New Mexico. 814 F. 3d 1060, 1064–1065
(CA10 2016). It was in the evening, and it was raining.
The two women involved called 911 to report Daniel as a
“ ‘drunk driver’ ” who was “ ‘swerving all crazy.’ ” Id., at
1065. The women then followed Daniel down the high-
way, close behind him and with their bright lights on.
Daniel, feeling threatened, pulled his truck over at an off-
ramp to confront them. After a brief, nonviolent encoun-
ter, Daniel drove a short distance to a secluded house
where he lived with his brother, Samuel Pauly.
   Sometime between 9 p.m. and 10 p.m., Officer Kevin
Truesdale was dispatched to respond to the women’s 911
call. Truesdale, arriving after Daniel had already left the
scene, interviewed the two women at the off-ramp. The
women told Truesdale that Daniel had been driving reck-
lessly and gave his license plate number to Truesdale.
2                     WHITE v. PAULY

                         Per Curiam

The state police dispatcher identified the plate as being
registered to the Pauly brothers’ address.
   After the women left, Officer Truesdale was joined at
the off-ramp by Officers Ray White and Michael Mariscal.
The three agreed there was insufficient probable cause to
arrest Daniel. Still, the officers decided to speak with
Daniel to (1) get his side of the story, (2) “ ‘make sure
nothing else happened,’ ” and (3) find out if he was intoxi-
cated. Id., at 1065. The officers split up. White stayed at
the off-ramp in case Daniel returned. Truesdale and
Mariscal drove in separate patrol cars to the Pauly broth-
ers’ address, less than a half mile away. Record 215.
Neither officer turned on his flashing lights.
   When Officers Mariscal and Truesdale arrived at the
address they had received from the dispatcher, they found
two different houses, the first with no lights on inside and
a second one behind it on a hill. Id., at 217, 246. Lights
were on in the second one. The officers parked their cars
near the first house. They examined a vehicle parked near
that house but did not find Daniel’s truck. Id., at 310.
   Officers Mariscal and Truesdale noticed the lights on in
the second house and approached it in a covert manner to
maintain officer safety. Both used their flashlights in an
intermittent manner. Truesdale alone turned on his
flashlight once they got close to the house’s front door.
Upon reaching the house, the officers found Daniel’s
pickup truck and spotted two men moving around inside
the residence. Truesdale and Mariscal radioed White, who
left the off-ramp to join them.
   At approximately 11 p.m., the Pauly brothers became
aware of the officers’ presence and yelled out “ ‘Who are
you?’ ” and “ ‘What do you want?’ ” 814 F. 3d, at 1066. In
response, Officers Mariscal and Truesdale laughed and
responded: “ ‘Hey, (expletive), we got you surrounded.
Come out or we’re coming in.’ ” Ibid. Truesdale shouted
once: “ ‘Open the door, State Police, open the door.’ ” Ibid.
                  Cite as: 580 U. S. ____ (2017)            3

                           Per Curiam

Mariscal also yelled: “ ‘Open the door, open the door.’ ”
Ibid.
   The Pauly brothers heard someone yelling, “ ‘We’re
coming in. We’re coming in.’ ” Ibid. Neither Samuel nor
Daniel heard the officers identify themselves as state
police. Record 81–82. The brothers armed themselves,
Samuel with a handgun and Daniel with a shotgun. One
of the brothers yelled at the police officers that “ ‘We have
guns.’ ” 814 F. 3d, at 1066. The officers saw someone run
to the back of the house, so Officer Truesdale positioned
himself behind the house and shouted “ ‘Open the door,
come outside.’ ” Ibid.
   Officer White had parked at the first house and was
walking up to its front door when he heard shouting from
the second house. He half-jogged, half-walked to the
Paulys’ house, arriving “just as one of the brothers said:
‘We have guns.’ ” Ibid.; see also Civ. No. 12–1311 (D NM,
Feb. 5, 2014), App. to Pet. for Cert. 75–78. When White
heard that statement, he drew his gun and took cover
behind a stone wall 50 feet from the front of the house.
Officer Mariscal took cover behind a pickup truck.
   Just “a few seconds” after the “We have guns” state-
ment, Daniel stepped part way out of the back door and
fired two shotgun blasts while screaming loudly. 814
F. 3d, at 1066–1067. A few seconds after those shots,
Samuel opened the front window and pointed a handgun
in Officer White’s direction. Officer Mariscal fired imme-
diately at Samuel but missed. “ ‘Four to five seconds’ ”
later, White shot and killed Samuel. Id., at 1067.
   The District Court denied the officers’ motions for sum-
mary judgment, and the facts are viewed in the light most
favorable to the Paulys. Mullenix v. Luna, 577 U. S. ___,
___, n. (2015) (per curiam) (slip op., at 2, n.). Because this
case concerns the defense of qualified immunity, however,
the Court considers only the facts that were knowable to
the defendant officers. Kingsley v. Hendrickson, 576 U. S.
4                     WHITE v. PAULY

                         Per Curiam

___, ___ (2015) (slip op., at 9).
   Samuel’s estate and Daniel filed suit against, inter alia,
Officers Mariscal, Truesdale, and White. One of the
claims was that the officers were liable under Rev. Stat.
§1979, 42 U. S. C. §1983, for violating Samuel’s Fourth
Amendment right to be free from excessive force. All three
officers moved for summary judgment on qualified immun-
ity grounds. White in particular argued that the Pauly
brothers could not show that White’s use of force vio-
lated the Fourth Amendment and, regardless, that Sam-
uel’s Fourth Amendment right to be free from deadly
force under the circumstances of this case was not clearly
established.
   The District Court denied qualified immunity. A di-
vided panel of the Court of Appeals for the Tenth Circuit
affirmed. As to Officers Mariscal and Truesdale, the court
held that “[a]ccepting as true plaintiffs’ version of the
facts, a reasonable person in the officers’ position should
have understood their conduct would cause Samuel and
Daniel Pauly to defend their home and could result in the
commission of deadly force against Samuel Pauly by Of-
ficer White.” 814 F. 3d, at 1076. The panel majority
analyzed Officer White’s claim separately from the other
officers because “Officer White did not participate in the
events leading up to the armed confrontation, nor was he
there to hear the other officers ordering the brothers to
‘Come out or we’re coming in.’ ” Ibid. Despite the fact that
“Officer White . . . arrived late on the scene and heard only
‘We have guns’ . . . before taking cover behind a stone
wall,” the majority held that a jury could have concluded
that White’s use of deadly force was not reasonable. Id.,
at 1077, 1082. The majority also decided that this rule—
that a reasonable officer in White’s position would believe
that a warning was required despite the threat of serious
harm—was clearly established at the time of Samuel’s
death. The Court of Appeals’ ruling relied on general
                  Cite as: 580 U. S. ____ (2017)              5

                           Per Curiam

statements from this Court’s case law that (1) “the reason-
ableness of an officer’s use of force depends, in part, on
whether the officer was in danger at the precise moment
that he used force” and (2) “if the suspect threatens the
officer with a weapon[,] deadly force may be used if neces-
sary to prevent escape, and if[,] where feasible, some
warning has been given.” Id., at 1083 (citing, inter alia,
Tennessee v. Garner, 471 U. S. 1 (1985), and Graham v.
Connor, 490 U. S. 386 (1989); emphasis deleted; internal
quotation marks and alterations omitted). The court
concluded that a reasonable officer in White’s position
would have known that, since the Paulys could not have
shot him unless he moved from his position behind a stone
wall, he could not have used deadly force without first
warning Samuel Pauly to drop his weapon.
  Judge Moritz dissented, contending that the “majority
impermissibly second-guesses” Officer White’s quick
choice to use deadly force. 814 F. 3d, at 1084. Judge
Moritz explained that the majority also erred by defining
the clearly established law at too high a level of generality,
in contravention of this Court’s precedent.
   The officers petitioned for rehearing en banc, which 6 of
the 12 judges on the Court of Appeals voted to grant. In a
dissent from denial of rehearing, Judge Hartz noted that
he was “unaware of any clearly established law that sug-
gests . . . that an officer . . . who faces an occupant pointing
a firearm in his direction must refrain from firing his
weapon but, rather, must identify himself and shout a
warning while pinned down, kneeling behind a rock wall.”
817 F. 3d 715, 718 (CA10 2016). Judge Hartz expressed
his hope that “the Supreme Court can clarify the govern-
ing law.” Id., at 719.
  The officers petitioned for certiorari. The petition is now
granted, and the judgment is vacated: Officer White did
not violate clearly established law on the record described
by the Court of Appeals panel.
6                      WHITE v. PAULY

                          Per Curiam

    Qualified immunity attaches when an official’s conduct
“ ‘does not violate clearly established statutory or constitu-
tional rights of which a reasonable person would have
known.’ ” Mullenix v. Luna, 577 U. S., at ___–___ (slip op.,
at 4–5). While this Court’s case law “ ‘do[es] not require a
case directly on point’ ” for a right to be clearly established,
“ ‘existing precedent must have placed the statutory or
constitutional question beyond debate.’ ” Id., at ___ (slip
op., at 5). In other words, immunity protects “ ‘all but the
plainly incompetent or those who knowingly violate the
law.’ ” Ibid.
    In the last five years, this Court has issued a number of
opinions reversing federal courts in qualified immunity
cases. See, e.g., City and County of San Francisco v.
Sheehan, 575 U. S. ___, ___, n. 3 (2015) (slip op., at 10, n.3)
(collecting cases). The Court has found this necessary
both because qualified immunity is important to “ ‘society
as a whole,’ ” ibid., and because as “ ‘an immunity from
suit,’ ” qualified immunity “ ‘is effectively lost if a case is
erroneously permitted to go to trial,’ ” Pearson v. Callahan,
555 U. S. 223, 231 (2009).
    Today, it is again necessary to reiterate the longstand-
ing principle that “clearly established law” should not be
defined “at a high level of generality.” Ashcroft v. al-Kidd,
563 U. S. 731, 742 (2011). As this Court explained dec-
ades ago, the clearly established law must be “particular-
ized” to the facts of the case. Anderson v. Creighton, 483
U. S. 635, 640 (1987). Otherwise, “[p]laintiffs would be
able to convert the rule of qualified immunity . . . into a
rule of virtually unqualified liability simply by alleging
violation of extremely abstract rights.” Id., at 639.
    The panel majority misunderstood the “clearly estab-
lished” analysis: It failed to identify a case where an of-
ficer acting under similar circumstances as Officer White
was held to have violated the Fourth Amendment. In-
stead, the majority relied on Graham, Garner, and their
                 Cite as: 580 U. S. ____ (2017)           7

                          Per Curiam

Court of Appeals progeny, which—as noted above—lay out
excessive-force principles at only a general level. Of
course, “general statements of the law are not inherently
incapable of giving fair and clear warning” to officers,
United States v. Lanier, 520 U. S. 259, 271 (1997), but “in
the light of pre-existing law the unlawfulness must be
apparent,” Anderson v. Creighton, supra, at 640. For that
reason, we have held that Garner and Graham do not
by themselves create clearly established law outside
“an obvious case.” Brosseau v. Haugen, 543 U. S. 194,
199 (2004) (per curiam); see also Plumhoff v. Rickard,
572 U. S. ___, ___ (2014) (slip op., at 13) (emphasiz-
ing that Garner and Graham “are ‘cast at a high level of
generality’ ”).
   This is not a case where it is obvious that there was a
violation of clearly established law under Garner and
Graham. Of note, the majority did not conclude that
White’s conduct—such as his failure to shout a warning—
constituted a run-of-the-mill Fourth Amendment violation.
Indeed, it recognized that “this case presents a unique set
of facts and circumstances” in light of White’s late arrival
on the scene. 814 F. 3d, at 1077. This alone should have
been an important indication to the majority that White’s
conduct did not violate a “clearly established” right.
Clearly established federal law does not prohibit a reason-
able officer who arrives late to an ongoing police action in
circumstances like this from assuming that proper proce-
dures, such as officer identification, have already been
followed. No settled Fourth Amendment principle re-
quires that officer to second-guess the earlier steps al-
ready taken by his or her fellow officers in instances like
the one White confronted here.
   On the record described by the Court of Appeals, Officer
White did not violate clearly established law. The Court
notes, however, that respondents contend Officer White
arrived on the scene only two minutes after Officers
8                     WHITE v. PAULY

                         Per Curiam

Truesdale and Mariscal and more than three minutes
before Daniel’s shots were fired. On the assumption that
the conduct of Officers Truesdale and Mariscal did not
adequately alert the Paulys that they were police officers,
respondents suggest that a reasonable jury could infer
that White witnessed the other officers’ deficient perfor-
mance and should have realized that corrective action was
necessary before using deadly force. Brief in Opposition
11, 22, n. 5. This Court expresses no position on this
potential alternative ground for affirmance, as it appears
that neither the District Court nor the Court of Appeals
panel addressed it. The Court also expresses no opinion
on the question whether this ground was properly pre-
served or whether—in light of this Court’s holding today—
Officers Truesdale and Mariscal are entitled to qualified
immunity.
  For the foregoing reasons, the petition for certiorari is
granted; the judgment of the Court of Appeals is vacated;
and the case is remanded for further proceedings con-
sistent with this opinion.
                                           It is so ordered.
                 Cite as: 580 U. S. ____ (2017)            1

                    GINSBURG, J., concurring

SUPREME COURT OF THE UNITED STATES
RAY WHITE, ET AL. v. DANIEL T. PAULY, AS PERSONAL 

   REPRESENTATIVE OF THE ESTATE OF SAMUEL 

           PAULY, DECEASED ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE TENTH CIRCUIT

              No. 16–67. Decided January 9, 2017


   JUSTICE GINSBURG, concurring.
   I join the Court’s opinion on the understanding that it
does not foreclose the denial of summary judgment to
Officers Truesdale and Mariscal. See 814 F. 3d 1060,
1068, 1073, 1074 (CA10 2016) (Court of Appeals empha-
sized, repeatedly, that fact disputes exist on question
whether Truesdale and Mariscal “adequately identified
themselves” as police officers before shouting “Come out or
we’re coming in” (internal quotation marks omitted)).
Further, as to Officer White, the Court, as I comprehend
its opinion, leaves open the propriety of denying summary
judgment based on fact disputes over when Officer White
arrived at the scene, what he may have witnessed, and
whether he had adequate time to identify himself and
order Samuel Pauly to drop his weapon before Officer
White shot Pauly. Compare id., at 1080, with ante, at 8.
See also Civ. No. 12–1311 (D NM, Feb. 5, 2014), pp. 7, and
n. 5, 9, App. to Pet. for Cert. 75–76, and n. 5, 77 (suggest-
ing that Officer White may have been on the scene when
Officers Truesdale and Mariscal threatened to invade the
Pauly home).

```

---

## GROUP: _overhaul2/lake/cases/Whiteley v. Warden.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Whiteley v. Warden"
type: case
citation: "401 U.S. 560 (1971)"
parallel_cite: "91 S. Ct. 1031; 28 L. Ed. 2d 306; 58 Ohio Op. 2d 434"
neutral_cite: 1971 U.S. LEXIS 65
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1971
date_decided: 1971-03-29
docket: 351
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1971-03-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Whiteley v. Warden
  varies_by_point: false
  scope_note: "Collective-knowledge rule reaffirmed in United States v. Hensley (1985); good law. Cf. Herring v. United States (2009) on good-faith reliance on another agency's records."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/"
  cluster_id: 108297
  opinion_id: 9424493
  identity_checked: true
homes:
  - page: "[[Collective Knowledge and the Fellow-Officer Rule]]"
    role: "Key — Anchor"
related: ["[[United States v. Hensley]]", "[[Herring v. United States]]", "[[Mapp v. Ohio]]"]
aliases: ["Whiteley v. Warden, Wyoming State Penitentiary", "Whiteley"]
tags: ["case", "fourth-amendment", "collective-knowledge", "fellow-officer-rule", "probable-cause", "radio-bulletin"]
holding: "An officer may act on the strength of a police radio bulletin and assume the issuing officer had probable cause. But where the issuing…"
lake:
  record_id: Whiteley v. Warden
  status: verified
  projected_at: 2026-07-06
---

# Whiteley v. Warden

*401 U.S. 560 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After a county-building break-in in Wyoming, a county sheriff acting on an informer's tip filed a bare, conclusory complaint and obtained an arrest warrant for Whiteley and Daley, then issued a statewide police radio bulletin describing the men and their car. Laramie police, relying on the bulletin, stopped the car, arrested the two men, and searched the vehicle, recovering tools and other evidence of the burglary. Whiteley sought [[Common Legal Terms#habeas-corpus|habeas]] relief, arguing the arrest lacked probable cause.

## Issue
Whether an arrest made by officers relying on a police bulletin is lawful when the officer who issued the bulletin (and obtained the underlying warrant) did not himself have probable cause.

## Rule
An officer may act on a fellow officer's bulletin or request, but the validity of the arrest still depends on probable cause existing somewhere in the originating chain: "police officers called upon to aid other officers in executing arrest warrants are entitled to assume that the officers requesting aid offered the magistrate the information requisite to support an independent judicial assessment of probable cause. Where, however, the contrary turns out to be true, an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest." — 401 U.S. at 568. ^pin-568

When the originating officer lacked probable cause, the arrest is unlawful and its fruits must be suppressed: "petitioner's arrest violated his constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial." — *Id.* at 568–569. ^pin-569

## Application
On these facts the arresting officers were entitled to rely on the bulletin, but the chain failed at its source. The complaint underlying the warrant stated only the complainant's conclusion and omitted the informer's tip and every operative fact, so it could not support a magistrate's probable-cause finding. The arresting officers, in turn, knew only what the bulletin told them plus the matching car and description — nothing corroborating the tip that these men committed the burglary. Because no one in the chain actually possessed probable cause, the arrest violated the Fourth Amendment, and the evidence seized incident to it should have been excluded.

## Conclusion
The arrest was unconstitutional and the evidence inadmissible; the writ of [[Common Legal Terms#habeas-corpus|habeas corpus]] should issue. Good-faith reliance on a fellow officer's bulletin cannot supply probable cause the originating officer never had.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of the collective-knowledge principle, which was applied to investigative stops in [[United States v. Hensley]] (1985). [[Herring v. United States]] (2009) later addressed the separate question of suppression when officers reasonably rely on another agency's erroneous records, declining to suppress where the error was isolated negligence — a good-faith refinement of the *Whiteley/Mapp* exclusionary remedy rather than a change to the probable-cause rule.

## Appears on
- [[Collective Knowledge and the Fellow-Officer Rule]] — *Key — Anchor*

## Sources
- *Whiteley v. Warden*, 401 U.S. 560 (1971) — https://www.courtlistener.com/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/ — pinpoints: 568, 568–569.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e1c832caf8a4a8b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Whiteley v. Warden"}, "payload": {"all": [{"cite": "401 U.S. 560", "page": "560", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "401"}, {"cite": "91 S. Ct. 1031", "page": "1031", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "91"}, {"cite": "28 L. Ed. 2d 306", "page": "306", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "28"}, {"cite": "1971 U.S. LEXIS 65", "page": "65", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1971"}, {"cite": "58 Ohio Op. 2d 434", "page": "434", "reporter": "Ohio Op. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "58"}], "display": "401 U.S. 560", "official": {"cite": "401 U.S. 560", "page": "560", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "401"}, "official_selection_present": true, "record_id": "Whiteley v. Warden"}}
{"assertion_id": "3809eb2ac921e3c3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-568", "record_id": "Whiteley v. Warden"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-568", "pinpoint_status": "slip-only", "quote": "--- # Whiteley v. Warden *401 U.S. 560 (1971)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After a county-building break-in in Wyoming, a county sheriff acting on an informer's tip filed a bare, conclusory complaint and obtained an arrest warrant for Whiteley and Daley, then issued a statewide police radio bulletin describing the men and their car. Laramie police, relying on the bulletin, stopped the car, arrested the two men, and searched the vehicle, recovering tools and other evidence of the burglary. Whiteley sought habeas relief, arguing the arrest lacked probable cause. ## Issue Whether an arrest made by officers relying on a police bulletin is lawful when the officer who issued the bulletin (and obtained the underlying warrant) did not himself have probable cause. ## Rule An officer may act on a fellow officer's bulletin or request, but the validity of the arrest still depends on probable cause existing somewhere in the originating chain:", "quote_fidelity": "mismatch", "record_id": "Whiteley v. Warden", "star_marker": null}}
{"assertion_id": "88428e34457f510a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-569", "record_id": "Whiteley v. Warden"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-569", "pinpoint_status": "slip-only", "quote": "petitioner's arrest violated his constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial.", "quote_fidelity": "mismatch", "record_id": "Whiteley v. Warden", "star_marker": null}}
{"assertion_id": "8ab34922f7ae09f7", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Whiteley v. Warden"}, "payload": {"as_of_content": "1971-03-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Whiteley v. Warden", "scope_note": "Collective-knowledge rule reaffirmed in United States v. Hensley (1985); good law. Cf. Herring v. United States (2009) on good-faith reliance on another agency's records.", "varies_by_point": false}}
```

### lake record — Whiteley v. Warden

```json
{
  "schema_version": "s2.v1",
  "record_id": "Whiteley v. Warden",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Whiteley v. Warden, Wyoming State Penitentiary",
    "case_name_short": "Whiteley",
    "case_name_full": "Whiteley v. Warden, Wyoming State Penitentiary",
    "input_case_name": "Whiteley v. Warden",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1971-03-29",
    "year": 1971,
    "docket": "351",
    "cluster_id": 108297,
    "lead_opinion_id": 9424493,
    "sibling_ids": [
      108297,
      9424493,
      9424494
    ],
    "absolute_url": "/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "401 U.S. 560",
      "volume": "401",
      "reporter": "U.S.",
      "page": "560",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "91 S. Ct. 1031",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 306",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "306",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 Ohio Op. 2d 434",
        "volume": "58",
        "reporter": "Ohio Op. 2d",
        "page": "434",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1971 U.S. LEXIS 65",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "65",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "401 U.S. 560",
        "volume": "401",
        "reporter": "U.S.",
        "page": "560",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "91 S. Ct. 1031",
        "volume": "91",
        "reporter": "S. Ct.",
        "page": "1031",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "28 L. Ed. 2d 306",
        "volume": "28",
        "reporter": "L. Ed. 2d",
        "page": "306",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1971 U.S. LEXIS 65",
        "volume": "1971",
        "reporter": "U.S. LEXIS",
        "page": "65",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 Ohio Op. 2d 434",
        "volume": "58",
        "reporter": "Ohio Op. 2d",
        "page": "434",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "401 U.S. 560",
    "official_selection": {
      "court_class": "scotus",
      "selected": "401 U.S. 560",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-568",
      "page": null,
      "quote": "--- # Whiteley v. Warden *401 U.S. 560 (1971)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After a county-building break-in in Wyoming, a county sheriff acting on an informer's tip filed a bare, conclusory complaint and obtained an arrest warrant for Whiteley and Daley, then issued a statewide police radio bulletin describing the men and their car. Laramie police, relying on the bulletin, stopped the car, arrested the two men, and searched the vehicle, recovering tools and other evidence of the burglary. Whiteley sought habeas relief, arguing the arrest lacked probable cause. ## Issue Whether an arrest made by officers relying on a police bulletin is lawful when the officer who issued the bulletin (and obtained the underlying warrant) did not himself have probable cause. ## Rule An officer may act on a fellow officer's bulletin or request, but the validity of the arrest still depends on probable cause existing somewhere in the originating chain:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-569",
      "page": null,
      "quote": "petitioner's arrest violated his constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1971-03-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Whiteley v. Warden",
    "varies_by_point": false,
    "scope_note": "Collective-knowledge rule reaffirmed in United States v. Hensley (1985); good law. Cf. Herring v. United States (2009) on good-faith reliance on another agency's records.",
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
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
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
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Charlotte Lynn Frazier And Andrea Parks",
          "cluster_id": 4538535,
          "cite": [
            "558 S.W.3d 145"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry Smith v. The State of Wyoming",
          "cluster_id": 1043203,
          "cite": [
            "2013 WY 122",
            "311 P.3d 132",
            "2013 WL 5507295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Haslam, 08-Mo-4 (2-10-2009)",
          "cluster_id": 3937404,
          "cite": [
            "2009 Ohio 696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane1_negative"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schneckloth v. Bustamonte",
          "cluster_id": 108800,
          "cite": [
            "36 L. Ed. 2d 854",
            "93 S. Ct. 2041",
            "412 U.S. 218",
            "1973 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stone v. Powell",
          "cluster_id": 109540,
          "cite": [
            "49 L. Ed. 2d 1067",
            "96 S. Ct. 3037",
            "428 U.S. 465",
            "1976 U.S. LEXIS 86"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Papachristou v. City of Jacksonville",
          "cluster_id": 108472,
          "cite": [
            "31 L. Ed. 2d 110",
            "92 S. Ct. 839",
            "405 U.S. 156",
            "1972 U.S. LEXIS 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Crews",
          "cluster_id": 110230,
          "cite": [
            "63 L. Ed. 2d 537",
            "100 S. Ct. 1244",
            "445 U.S. 463",
            "1980 U.S. LEXIS 1293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zurcher v. Stanford Daily",
          "cluster_id": 109876,
          "cite": [
            "56 L. Ed. 2d 525",
            "98 S. Ct. 1970",
            "436 U.S. 547",
            "1978 U.S. LEXIS 98"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Evans",
          "cluster_id": 117905,
          "cite": [
            "131 L. Ed. 2d 34",
            "115 S. Ct. 1185",
            "514 U.S. 1",
            "1995 U.S. LEXIS 1806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Deville v. Marcantel",
          "cluster_id": 65780,
          "cite": [
            "567 F.3d 156",
            "2009 U.S. App. LEXIS 9403",
            "2009 WL 1162586"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Maumee v. Weisner",
          "cluster_id": 2689810,
          "cite": [
            "1999 Ohio 68",
            "87 Ohio St. 3d 295"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tisler",
          "cluster_id": 2162728,
          "cite": [
            "469 N.E.2d 147",
            "103 Ill. 2d 226",
            "82 Ill. Dec. 613",
            "1984 Ill. LEXIS 331"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Novembrino",
          "cluster_id": 1516571,
          "cite": [
            "519 A.2d 820",
            "105 N.J. 95",
            "1987 N.J. LEXIS 265"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shadwick v. City of Tampa",
          "cluster_id": 108582,
          "cite": [
            "32 L. Ed. 2d 783",
            "92 S. Ct. 2119",
            "407 U.S. 345",
            "1972 U.S. LEXIS 39"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
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
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harvey",
          "cluster_id": 1343416,
          "cite": [
            "187 S.E.2d 706",
            "281 N.C. 1",
            "1972 N.C. LEXIS 1321"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whiteley v. Warden:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108297 OR 9424493 OR 9424494) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDYxMjUxMjAwMDAwJnM9MTM3NjIyNCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108297+OR+9424493+OR+9424494%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108297 OR 9424493 OR 9424494)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDgmcz00NjYxNDM2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108297+OR+9424493+OR+9424494%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108297 OR 9424493 OR 9424494)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 1,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108297 OR 9424493 OR 9424494)",
    "indexed_citing_opinions": 1201,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108297,
        "count": 1100,
        "count_source": "search"
      },
      {
        "opinion_id": 9424493,
        "count": 147,
        "count_source": "search"
      },
      {
        "opinion_id": 9424494,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1845,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/whiteley-v-warden.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0NDE3NDYmcz01MjYyODE3JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108297+OR+9424493+OR+9424494%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108297,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107875,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 286552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108297,
        "cited_id": 1296591,
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
    "date_created": "2026-07-06T04:19:47Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:20:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:20:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:22:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:20:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Whiteley v. Warden

```
<opinion type="majority">
<author id="b645-11">Mr. Justice Harlan</author>
<p id="AOZt">delivered the opinion of the Court.</p>
<p id="b645-12">Petitioner Whiteley, in 1965, was convicted in the District Court for the Second Judicial District of the State of Wyoming on charges of breaking and entering and being an habitual criminal.<footnotemark>1</footnotemark> Both at his arraignment and at trial Whiteley challenged the constitutionality of the use of evidence seized during a search incident to an arrest which he claimed was illegal. The trial court overruled petitioner’s motion to suppress, and on appeal the Supreme Court of Wyoming affirmed. <em>Whiteley </em>v. <em>State, </em><span class="citation" data-id="1296591"><a href="/opinion/1296591/whiteley-v-state/" aria-description="Citation for case: Whiteley v. State">418 P. 2d 164</a></span> (1966). This proceeding commenced with a petition for habeas corpus in the United States District Court for the District of Wyoming, which was denied on November 25, 1968.<footnotemark>2</footnotemark> <em>Whiteley </em>v. <em>Wyoming, </em><span class="citation" data-id="8768821"><a href="/opinion/8784984/whiteley-v-wyoming/" aria-description="Citation for case: Whiteley v. Wyoming">293 F. Supp. 381</a></span>. On appeal, the United States Court of Appeals for <page-number citation-index="1" label="562">*562</page-number>the Tenth Circuit affirmed. <em>Whiteley </em>v. <em>Meacham, </em><span class="citation" data-id="286552"><a href="/opinion/286552/harold-whiteley-v-leonard-meacham-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Harold Whiteley v. Leonard Meacham, Warden, Wyoming State...">416 F. 2d 36</a></span> (1969). We granted certiorari, limiting the writ to the issue of the constitutionality of the arrest and ensuing search and seizure. <span class="citation multiple-matches"><a href="/c/U.%20S./397/1062/">397 U. S. 1062</a></span> (1970).<footnotemark>3</footnotemark> We reverse the judgment of the Tenth Circuit for the reasons stated herein.</p>
<p id="b646-5">I</p>
<p id="b646-6">The circumstances surrounding petitioner’s arrest and the incidental search and seizure, as stated by the Wyoming Supreme Court, <span class="citation" data-id="1296591"><a href="/opinion/1296591/whiteley-v-state/#165" aria-description="Citation for case: Whiteley v. State">418 P. 2d 164, 165-166</a></span>, are as follows:<footnotemark>4</footnotemark></p>
<blockquote id="b646-7">“On November 23, 1964, certain business establishments in Saratoga were broken into, including the Rustic Bar and Shively’s Hardware, the offenses being investigated by the Carbon County Sheriff [Sheriff Ogburn] who, acting on a tip, the next day signed a complaint charging defendant and another with breaking and entering the building identified <page-number citation-index="1" label="563">*563</page-number>as the Rustic Bar. This complaint was made before a justice of the peace at approximately 11:30 a. m. on the 24th, and a warrant issued. After the investigation, the sheriff put out a state item on the radio to pick up two suspects of the breaking and entering, defendant and another. The message went to the network at Casper and was transmitted over the State, received by the Albany County Sheriff’s Office and communicated to the Laramie Police Department, the message giving names and descriptions of the two persons and advising the type of car probably being driven and the amount of money taken, including certain old coins with the dates. Late at night on November 24, a Laramie patrolman, in reliance on the information in the radio item, arrested the defendant and his companion. At the time, the patrolman had no warrant for defendant’s arrest nor search warrant. The officer together with a deputy sheriff, who had come up in the meantime, searched the car and removed a number of items introduced in evidence, including tools and old coins, identified at the trial as taken from Shively’s Hardware. . . .”</blockquote>
<p id="b647-5">Sheriff Ogburn’s complaint, which provided the basis for the arrest warrant issued by the justice of the peace, is as follows:</p>
<blockquote id="b647-6">“I, C. W. Ogburn, do solemnly swear that on or about the 23 day of November, A. D. 1964, in the County of Carbon and State of Wyoming, the said Harold Whiteley and Jack Daley, defendants did then and there unlawfully break and enter a locked and sealed building [describing the location and ownership of the building].” App. 28.</blockquote>
<p id="b647-7">A state item 881, the bulletin which Sheriff Ogburn <page-number citation-index="1" label="564">*564</page-number>put out on the radio and which led to petitioner’s arrest and search by the Laramie patrolman, is as follows:</p>
<blockquote id="b648-5">“P &amp; H for B &amp; E Saratoga, early A. M. 11-24-64. Subj. #1. Jack Daley, WMA, 38, D. O. B. 2-29-[26], 5'10", 175, med. build, med. comp., blonde and blue. Tat. left shoulder: 'Love Me or Leave Me.’ #2. Harold Whitley, WMA, 43, D. O. B. 6-22-21, 5' 11", 180, med. build, fair comp, brown eyes. Tat. on right arm 'Bird.’ Poss. driving 1953 or 1954 Buick, light green bottom, dark top. Wyo. lie. 2-bal. unknown. Taken: $281.71 in small change, numerous old coins ranging from <em>,5‡ </em>pieces to silver dollars, dated from 1853 to 1908. Warrant issues, will extradite. Special attention Denver. . . .” App. 31.<footnotemark>5</footnotemark></blockquote>
<p id="b648-6">II</p>
<p id="b648-7">The decisions of this Court concerning Fourth Amendment probable-cause requirements before a warrant for either arrest or search can issue require that the judicial officer issuing such a warrant be supplied with sufficient information to support an independent judgment that probable cause exists for the warrant.<footnotemark>6</footnotemark> <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969); <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U. S. 102</a></span> <em>(1965); Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <em>Rugendorf </em>v. <em>United States, </em><span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span> (1964); <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960); <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). In the instant case — so far as the record stipulated to by the parties <page-number citation-index="1" label="565">*565</page-number>reveals<footnotemark>7</footnotemark> — the sole support for the arrest warrant issued at Sheriff Ogburn’s request was the complaint reproduced above.<footnotemark>8</footnotemark> That complaint consists of nothing more than the complainant’s conclusion that- the individuals named therein perpetrated the offense described in the complaint. The actual basis for Sheriff Ogburn’s conclusion was an informer’s tip, but that fact, as well as every other operative fact, is omitted from the complaint. Under the cases just cited, that document alone could not support the independent judgment of a disinterested magistrate.</p>
<p id="b649-5">The State,<footnotemark>9</footnotemark> however, contends that regardless of the sufficiency of the complaint to support the arrest warrant, the Laramie police officer who actually made the <page-number citation-index="1" label="566">*566</page-number>arrest possessed sufficient factual information to support a finding of probable cause for arrest without a warrant. In support of this proposition, the State argues that a reviewing court should employ less stringent standards for reviewing a police officer’s assessment of probable cause as a prelude to a warrantless arrest than the court would employ in reviewing a magistrate’s assessment as a prelude to issuing an arrest or search warrant.<footnotemark>10</footnotemark> That proposition has been consistently rejected by this Court. <em>United States </em>v. <em>Ventresca, </em><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/#105" aria-description="Citation for case: United States v. Ventresca">380 U. S., at 105-109</a></span>; <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#110" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 110-111</a></span>; <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S., at 270-271</a></span>. And the reason for its rejection is both fundamental and obvious: less stringent standards for reviewing the officer’s discretion in effecting a warrantless arrest and search would discourage resort to the procedures for obtaining a warrant. Thus the standards applicable to the factual basis supporting the officer’s probable-cause assessment at the time of the challenged arrest and search are at least as stringent as the standards applied with respect to the magistrate’s assessment. See <em>McCray </em>v. <em>Illinois, </em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/#304" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300, 304-305</a></span> (1967).</p>
<p id="b650-5">Applying those standards to the instant case, the information possessed by the Laramie police officer at the time of arrest and search consisted of: (1) the data contained in state bulletin 881, reproduced <em>supra; </em>(2) the knowledge, obtained by personal observation, that two men were driving a car matching the car described in the radio bulletin; (3) the knowledge, possessed by one of the arresting officers, that one of the people in the car was Jack Daley, App. 71; (4) the knowledge, acquired <page-number citation-index="1" label="567">*567</page-number>by personal observation, that the other individual in the car fitted the description of Whiteley contained in state bulletin 881; and (5) the knowledge, acquired by the officer after stopping Whiteley, that he had given a false name.<footnotemark>11</footnotemark></p>
<p id="b651-5">This Court has held that where the initial impetus for an arrest is an informer’s tip, information gathered by the arresting officers can be used to sustain a finding of probable cause for an arrest that could not adequately be supported by the tip alone. <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959). See <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969). But the additional information acquired by the arresting officers must in some sense be corroborative of the informer’s tip that the arrestees committed the felony or, as in <em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span> </em>itself, were in the process of committing the felony. See the opinions of the Court and that of Me. Justice White concurring in <em>Spinelli </em>v. <em>United States, supra, </em>and p. 423. In the present case, the very most the additional information tended to establish is that either Sheriff Ogburn, or his informant, or both of them, knew Daley and Whiteley and the kind of car they drove; the record is devoid of any information at any stage of the proceeding from the time of the burglary to the event of the arrest and search that would support either the reliability of the informant or the informant’s conclusion that these men were connected with the crime. <em>Spinelli </em>v. <em>United States, supra; McCray </em>v. <em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">Illinois, supra;</a></span> Aguilar </em>v. <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra.</a></span></em></p>
<p id="b652-4"><page-number citation-index="1" label="568">*568</page-number>The State, however, offers one further argument in support of the legality of the arrest and search: the Laramie police relied on the radio bulletin in making the arrest, and not on Sheriff Ogburn’s unnamed informant. Clearly, it is said, they had probable cause for believing that the passengers in the car were the men described in the bulletin, and, in acting on the bulletin, they reasonably assumed that whoever authorized the bulletin had probable cause to direct Whiteley’s and Daley’s arrest. To prevent arresting officers from acting on the assumption that fellow officers who call upon them to make an arrest have probable cause for believing the arrestees are perpetrators of a crime would, it is argued, unduly hamper law enforcement.</p>
<p id="b652-5">We do not, of course, question that the Laramie police were entitled to act on the strength of the radio bulletin. Certainly police officers called upon to aid other officers in executing arrest warrants are entitled to assume that the officers requesting aid offered the magistrate the information requisite to support an independent judicial assessment of probable cause. Where, however, the contrary turns out to be true, an otherwise illegal arrest cannot be insulated from challenge by the decision of the instigating officer to rely on fellow officers to make the arrest.</p>
<p id="b652-6">In sum, the complaint on which the warrant issued here clearly could not support a finding of probable cause by the issuing magistrate. The arresting officer was not himself possessed of any factual data tending to corroborate the informer’s tip that Daley and Whiteley committed the crime.<footnotemark>12</footnotemark> Therefore, petitioner’s arrest vio<page-number citation-index="1" label="569">*569</page-number>lated his constitutional rights under the Fourth and Fourteenth Amendments; the evidence secured as an incident thereto should have been excluded from his trial. <em>Mapp </em>v. Ohio, <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p id="b653-5">Ill</p>
<p id="b653-6">There remains the question as to the proper disposition of this case. The State urges us to remand so that it will have an opportunity to develop a record which might show that the issuing magistrate had factual information additional to that presented in Sheriff Ogburn’s complaint. Brief for Respondent 8-9. Yet the State concedes, as on the record it must, that at every stage in the proceedings below petitioner argued the insufficiency of the warrant as well as the lack of probable cause at the time of the arrest. Brief for Respondent 4. Knowing the basis for petitioner’s constitutional claim, the State chose to try those proceedings on the record it had developed in the state courts. See n. 4, <em>supra. </em>Its sole explanation for this state of affairs is that “the state has felt, based on precedent and logic, that no court would accept the legal reasoning of petitioner.” Brief for Respondent 9. In the circumstances of this case, that justification, as we have shown, is untenable.</p>
<p id="b653-7">Pursuant to our authority under <span class="citation no-link">28 U. S. C. § 2106</span> to make such disposition of the case “as may be just under the circumstances,” we reverse the judgment of the Tenth Circuit and remand with directions that the writ is to issue unless the State makes appropriate arrangements to retry petitioner.<footnotemark>13</footnotemark> Cf. <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#487" aria-description="Citation for case: Giordenello v. United States">357 U. S., at 487-488</a></span>.</p>
<p id="b653-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b645-13"> He was given concurrent sentences on the breaking and entering charges of one to 10 years and, in consequence of the recidivist charge, imprisonment for life.</p>
</footnote>
<footnote label="2">
<p id="b645-14"> Prior to commencing federal habeas corpus proceedings, Whiteley had filed a petition for post-conviction relief pursuant to the Wyoming statutes. No appeal was taken from the denial of that petition.</p>
</footnote>
<footnote label="3">
<p id="b646-8"> In his petition for habeas corpus, Whiteley raised several other issues which had previously been advanced in his state petition for post-conviction relief, but not in his direct appeal to the Supreme Court of Wyoming. On these other issues, both lower federal courts held that failure to appeal the denial of his state post-conviction petition constituted nonexhaustion of state remedies. Petitioner sought to raise the exhaustion issue in his present petition for certiorari, but, as noted in text, we granted the writ limited to the search and seizure issue decided by the lower federal courts.</p>
</footnote>
<footnote label="4">
<p id="b646-9"> At the outset of the federal habeas corpus proceeding now before us, both parties entered into the following stipulation, App. 10:</p>
<blockquote id="b646-10">“IT IS HEREBY STIPULATED by and between the parties through their respective counsel that, pursuant to the agreement of the parties in open court on February 16, 1968, both sides will rely exclusively on the record before the trial court in the original case of the State of Wyoming v. Harold Whiteley . . . and any and all parts of the record on appeal to the State of Wyoming ... in the hearing on the merits of this case before the [U. S. District Court].”</blockquote>
</footnote>
<footnote label="5">
<p id="b648-8"> A second version of state item 881 is identical in all relevant respects except that it omits reference to the arrest warrant. See App. 37.</p>
</footnote>
<footnote label="6">
<p id="b648-9"> In <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963), the Court held that the same probable-cause standards were applicable to federal and state warrants under the Fourth and Fourteenth Amendments. In <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), the Court held the exclusionary rule was applicable to state prosecutions.</p>
</footnote>
<footnote label="7">
<p id="b649-6"> See n. 4, <em>supra.</em></p>
</footnote>
<footnote label="8">
<p id="b649-7"> The dissent seems to imply that “this record shows” that Sheriff Ogburn received the description of the car contained in the radio bulletin from someone who also informed him that he also saw the car at the scene of the crime. <em>Post, </em>at 570. The record wholly fails to support any such implication. Sheriff Ogburn, who testified on four separate occasions at the trial, see R. 105-112, 187-191, 310-314, 335-337, said nothing of the sort. Only one other witness, Leonard Russell Marion, testified to having given Ogburn any information about the car prior to Whiteley’s arrest; Marion never testified to seeing the car near the scene of the crime. R. 317-322, 329-330. Indeed, it is quite apparent from reading Marion’s testimony that his observations of Whiteley on the day of the robbery took place at his own house. R. 320-321.</p>
<p id="b649-8">More importantly, even the dissent apparently concedes that as far as the record in this case reveals, the only information Sheriff Ogburn communicated to the magistrate issuing the warrant was contained in his written complaint reproduced above. Under the cases of this Court, an otherwise insufficient affidavit cannot be rehabilitated by testimony concerning information possessed by the affiant when he sought the warrant but not disclosed to the issuing magistrate. See <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>, 109 n. 1. A contrary rule would, of course, render the warrant requirements of the Fourth Amendment meaningless.</p>
</footnote>
<footnote label="9">
<p id="b649-9"> Since this is a federal habeas corpus proceeding, the State is technically not a party.</p>
</footnote>
<footnote label="10">
<p id="b650-6"> “The legal principles relied upon by the state throughout this entire litigated process have been based on the premise that a law enforcement officer may make a warrantless arrest if he has requisite probable cause, which can be something less than the requisite probable cause that must be presented to a judicial officer prior to the issuance of an arrest or search warrant.” Brief for Respondent 6.</p>
</footnote>
<footnote label="11">
<p id="b651-6"> After arresting Whiteley and Daley, the officers searched the car and discovered in the car’s interior the old coins taken in one of the burglaries and described in the radio bulletin. In addition, they found burglar’s tools in the trunk of the car. Of course, the discoveries of an illegal search cannot be used to validate the probable-cause judgment upon which the legality of the search depends.</p>
</footnote>
<footnote label="12">
<p id="b652-7"> The arrest warrant issued at about noon on November 24, 1964. See App. 53. State bulletin 881 was broadcast at 3:03 p. m. that same day. App. 31. It is apparent that Sheriff Ogbum did not himself acquire additional corroborative data possibly supporting a probable-cause arrest after securing the warrant.</p>
</footnote>
<footnote label="13">
<p id="b653-9"> The State makes a halfhearted attempt to argue that the introduction of the illegally seized evidence was harmless error. The <page-number citation-index="1" label="570">*570</page-number>evidence, of course, was damning, to say the least. See n. 10, <em>supra. </em>The only other evidence implicating Whiteley was his accomplice’s testimony. It is clear that the error cannot be said to be harmless under applicable standards. <em>Chapman </em>v. <em>California, </em><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967); <em>Harrington </em>v. <em>California, </em><span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969).</p>
<p id="b654-8">Contrary to the implications in the dissenting opinion, see <em>post, </em>at 571, no witness at trial other than the accomplice placed Whiteley “near the scene of the crime” on the night of the robbery.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Whren v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Whren v. United States"
type: case
citation: "517 U.S. 806 (1996)"
parallel_cite: "116 S. Ct. 1769; 135 L. Ed. 2d 89"
neutral_cite: 1996 U.S. LEXIS 3720
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-05-15
docket: 95-5841
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1996-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Whren v. United States
  varies_by_point: false
  scope_note: "Pretext-irrelevance rule reaffirmed throughout; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118036/whren-v-united-states/"
  cluster_id: 118036
  opinion_id: 118036
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Anchor"
related: ["[[Delaware v. Prouse]]", "[[Pennsylvania v. Mimms]]", "[[Heien v. North Carolina]]"]
aliases: ["Whren"]
tags: ["case", "fourth-amendment", "traffic-stops", "pretext", "probable-cause", "subjective-intent"]
holding: "An officer's subjective motive is irrelevant to the Fourth Amendment validity of a traffic stop; a stop supported by an objective,…"
lake:
  record_id: Whren v. United States
  status: verified
  projected_at: 2026-07-09
---

# Whren v. United States

*517 U.S. 806 (1996)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Plainclothes vice officers patrolling a "high drug area" of Washington, D.C. in an unmarked car grew suspicious of a Pathfinder with youthful occupants stopped unusually long at a stop sign, the driver looking into the passenger's lap. When the police made a U-turn, the truck turned right without signaling and sped off at an unreasonable speed. The officers stopped it; approaching the window, Officer Soto saw bags of crack cocaine in Whren's hands. The occupants, charged with drug offenses, argued the traffic stop was a pretext to investigate a drug hunch for which the officers lacked probable cause.

## Issue
Whether a traffic stop supported by probable cause of a traffic violation violates the Fourth Amendment when the officer's actual motivation was to investigate other suspected crime, or whether the test should be whether a reasonable officer would have made the stop for the stated traffic reason.

## Rule
A stop is reasonable when there is probable cause of a traffic violation: "As a general matter, the decision to stop an automobile is reasonable where the police have probable cause to believe that a traffic violation has occurred." — 517 U.S. at 810. ^pin-810

The officer's real motive does not matter: "Subjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis." — [*Id.* at 813](https://www.courtlistener.com/opinion/118036/whren-v-united-states/#:~:text=Subjective%20intentions%20play%20no%20role). ^pin-813

Claims of racially selective enforcement are governed by the Equal Protection Clause, not the Fourth Amendment.

## Application
On these facts the petitioners conceded that Officer Soto had probable cause to believe several D.C. traffic provisions had been violated — driving without full attention, turning without signaling, and traveling at an unreasonable speed. Because that probable cause existed, the stop was reasonable, and it made no difference that the officers' true interest was possible drug activity or that a reasonable officer arguably would not have made the stop for the traffic violations alone. The crack cocaine the officer then saw in plain view was lawfully observed.

## Conclusion
The traffic stop was constitutional because it was supported by probable cause of a traffic violation; the officers' subjective intent was irrelevant. The convictions were affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Whren* anchors the rule that traffic stops are judged objectively, building on [[Delaware v. Prouse]] and [[Pennsylvania v. Mimms]]; the objective-reasonableness approach extends to an officer's reasonable mistake of law in [[Heien v. North Carolina]].

## Appears on
- [[Traffic Stops]] — *Key — Anchor*

## Sources
- *Whren v. United States*, 517 U.S. 806 (1996) — https://www.courtlistener.com/opinion/118036/whren-v-united-states/ — pinpoints: 810, 813.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d9ef9cec234786f8", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Whren v. United States"}, "payload": {"all": [{"cite": "517 U.S. 806", "page": "806", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "517"}, {"cite": "116 S. Ct. 1769", "page": "1769", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "116"}, {"cite": "135 L. Ed. 2d 89", "page": "89", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "135"}, {"cite": "1996 U.S. LEXIS 3720", "page": "3720", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1996"}], "display": "517 U.S. 806", "official": {"cite": "517 U.S. 806", "page": "806", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "517"}, "official_selection_present": true, "record_id": "Whren v. United States"}}
{"assertion_id": "089f64a6eab10a9a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-810", "record_id": "Whren v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-810", "pinpoint_status": "slip-only", "quote": "of Washington, D.C. in an unmarked car grew suspicious of a Pathfinder with youthful occupants stopped unusually long at a stop sign, the driver looking into the passenger's lap. When the police made a U-turn, the truck turned right without signaling and sped off at an unreasonable speed. The officers stopped it; approaching the window, Officer Soto saw bags of crack cocaine in Whren's hands. The occupants, charged with drug offenses, argued the traffic stop was a pretext to investigate a drug hunch for which the officers lacked probable cause. ## Issue Whether a traffic stop supported by probable cause of a traffic violation violates the Fourth Amendment when the officer's actual motivation was to investigate other suspected crime, or whether the test should be whether a reasonable officer would have made the stop for the stated traffic reason. ## Rule A stop is reasonable when there is probable cause of a traffic violation:", "quote_fidelity": "mismatch", "record_id": "Whren v. United States", "star_marker": null}}
{"assertion_id": "a1bdf1bcc4432ef6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-813", "record_id": "Whren v. United States"}, "payload": {"fragment": "#:~:text=Subjective%20intentions%20play%20no%20role", "page": null, "pin_id": "pin-813", "pinpoint_status": "star-verified", "quote": "Subjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.", "quote_fidelity": "matched", "record_id": "Whren v. United States", "star_marker": "813"}}
{"assertion_id": "7746a0608d1428ca", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Whren v. United States"}, "payload": {"as_of_content": "1996-06-10", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Whren v. United States", "scope_note": "Pretext-irrelevance rule reaffirmed throughout; good law.", "varies_by_point": false}}
```

### lake record — Whren v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Whren v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Whren v. United States",
    "case_name_short": "Whren",
    "case_name_full": "WHREN Et Al. v. UNITED STATES",
    "input_case_name": "Whren v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-05-15",
    "year": 1996,
    "docket": "95-5841",
    "cluster_id": 118036,
    "lead_opinion_id": 118036,
    "sibling_ids": [
      118036
    ],
    "absolute_url": "/opinion/118036/whren-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "517 U.S. 806",
      "volume": "517",
      "reporter": "U.S.",
      "page": "806",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 1769",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 89",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "89",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 3720",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3720",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "517 U.S. 806",
        "volume": "517",
        "reporter": "U.S.",
        "page": "806",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 1769",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "1769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "135 L. Ed. 2d 89",
        "volume": "135",
        "reporter": "L. Ed. 2d",
        "page": "89",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 3720",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "3720",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "517 U.S. 806",
    "official_selection": {
      "court_class": "scotus",
      "selected": "517 U.S. 806",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-810",
      "page": null,
      "quote": "of Washington, D.C. in an unmarked car grew suspicious of a Pathfinder with youthful occupants stopped unusually long at a stop sign, the driver looking into the passenger's lap. When the police made a U-turn, the truck turned right without signaling and sped off at an unreasonable speed. The officers stopped it; approaching the window, Officer Soto saw bags of crack cocaine in Whren's hands. The occupants, charged with drug offenses, argued the traffic stop was a pretext to investigate a drug hunch for which the officers lacked probable cause. ## Issue Whether a traffic stop supported by probable cause of a traffic violation violates the Fourth Amendment when the officer's actual motivation was to investigate other suspected crime, or whether the test should be whether a reasonable officer would have made the stop for the stated traffic reason. ## Rule A stop is reasonable when there is probable cause of a traffic violation:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-813",
      "page": null,
      "quote": "Subjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.",
      "star_marker": "813",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15842,
      "fragment": "#:~:text=Subjective%20intentions%20play%20no%20role",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1996-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Whren v. United States",
    "varies_by_point": false,
    "scope_note": "Pretext-irrelevance rule reaffirmed throughout; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Robinson-Van Rader",
          "cluster_id": 9398953,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane1_negative"
      },
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
        "journal_ref": "Whren v. United States:lane1_negative"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carmouche v. State",
          "cluster_id": 1463452,
          "cite": [
            "10 S.W.3d 323",
            "2000 Tex. Crim. App. LEXIS 8",
            "2000 WL 60020"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reichle v. Howards",
          "cluster_id": 801500,
          "cite": [
            "182 L. Ed. 2d 985",
            "132 S. Ct. 2088",
            "566 U.S. 658",
            "2012 U.S. LEXIS 4132"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. al-Kidd",
          "cluster_id": 217703,
          "cite": [
            "179 L. Ed. 2d 1149",
            "131 S. Ct. 2074",
            "563 U.S. 731",
            "2011 U.S. LEXIS 4021"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460854,
          "cite": [
            "583 U.S. 48",
            "138 S. Ct. 577",
            "199 L. Ed. 2d 453",
            "2018 U.S. LEXIS 760"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
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
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Prado Navarette v. California",
          "cluster_id": 2670795,
          "cite": [
            "188 L. Ed. 2d 680",
            "134 S. Ct. 1683",
            "2014 U.S. LEXIS 2930",
            "82 U.S.L.W. 4282",
            "572 U.S. 393",
            "24 Fla. L. Weekly Fed. S 690",
            "2014 WL 1577513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peso Chavez and Gregory Lee, Individually and on Behalf of All Persons Similarly Situated v. The Illinois State Police, Terrance W. Gainer, Individually and in His Official Capacity as Director of the Illinois State Police, Michael Snyders, Individually and in His Official Capacity as Illinois State Police Operation Valkyrie Coordinator, Edward Kresl, Individually and in His Official Capacity as District Commander of the Illinois State Police, and Larry Thomas, Daniel Gillette, Craig Graham, Robert P. Cessna, Robert Lauterbach, and Dale Fraher, Officers of the Illinois State Police, in Their Individual Capacities",
          "cluster_id": 773427,
          "cite": [
            "251 F.3d 612",
            "49 Fed. R. Serv. 3d 1127",
            "2001 U.S. App. LEXIS 10560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Clark",
          "cluster_id": 6457347,
          "cite": [
            "596 U.S. 36",
            "142 S. Ct. 1332"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Whren v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118036) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjY0ODQxNjAwMDAwJnM9ODI0NjUzMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118036%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(118036)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NzEmcz00NTAyMzA2JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118036%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118036)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjkyNzQ4ODAwMDAwJnM9OTQyMjc4MyZ0PW8mZD0yMDI2LTA3LTA2JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118036%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118036)",
    "indexed_citing_opinions": 3965,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118036,
        "count": 3965,
        "count_source": "search"
      }
    ],
    "citation_count": 7126,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/whren-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MjQ3Njkmcz0xMDYyMTk5NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118036%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118036,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 110973,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 111927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118036,
        "cited_id": 695142,
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
    "date_created": "2026-07-06T04:22:20Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:22:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:22:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:24:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:22:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Whren v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b906-4">
<span citation-index="1" class="star-pagination" label="808"> 
   *808
   </span>
  Justice Scalia
 </author>
<p id="A6N">
  delivered the opinion of the Court.
 </p>
<p id="b906-5">
  In this case we decide whether the temporary detention of a motorist who the police have probable cause to believe has committed a civil traffic violation is inconsistent with the Fourth Amendment’s prohibition against unreasonable seizures unless a reasonable officer would have been motivated to stop the car by a desire to enforce the traffic laws.
 </p>
<p id="b906-6">
  I
 </p>
<p id="b906-7">
  On the evening of June 10, 1993, plainclothes vice-squad officers of the District of Columbia Metropolitan Police Department were patrolling a “high drug area” of the city in an unmarked car. Their suspicions were aroused when they passed a dark Pathfinder truck with temporary license plates and youthful occupants waiting at a stop sign, the driver looking down into the lap of the passenger at his right. The truck remained stopped at the intersection for what seemed an unusually long time — more than 20 seconds. When the police car executed a U-turn in order to head back toward the truck, the Pathfinder turned suddenly to its right, without signaling, and sped off at an “unreasonable” speed. The policemen followed, and in a short while overtook the Pathfinder when it stopped behind other traffic at a red light. They pulled up alongside, and Officer Ephraim Soto stepped out and approached the driver’s door, identifying himself as a police officer and directing the driver, petitioner Brown, to put the vehicle in park. When Soto drew up to the driver’s
  <span citation-index="1" class="star-pagination" label="809"> 
   *809
   </span>
  window, he immediately observed two large plastic bags of what appeared to be crack cocaine in petitioner Whren’s hands. Petitioners were arrested, and quantities of several types of illegal drugs were retrieved from the vehicle.
 </p>
<p id="b907-4">
  Petitioners were charged in a four-count indictment with violating various federal drug laws, including <span class="citation no-link">21 U. S. C. §§ 844</span>(a) and 860(a). At a pretrial suppression hearing, they challenged the legality of the stop and the resulting seizure of the drugs. They argued that the stop had not been justified by probable cause to believe, or even reasonable suspicion, that petitioners were engaged in illegal drug-dealing activity; and that Officer Soto’s asserted ground for approaching the vehicle—to give the driver a warning concerning traffic violations—was pretextual. The District Court denied the suppression motion, concluding that “the facts of the stop were not controverted,” and “[t]here was nothing to really demonstrate that the actions of the officers were contrary to a normal traffic stop.” App. 5.
 </p>
<p id="b907-5">
  Petitioners were convicted of the counts at issue here. The Court of Appeals affirmed the convictions, holding with respect to the suppression issue that, “regardless of whether a police officer subjectively believes that the occupants of an automobile may be engaging in some other illegal behavior, a traffic stop is permissible as long as a reasonable officer in the same circumstances
  <em>
   could have
  </em>
  stopped the car for the suspected traffic violation.” <span class="citation" data-id="695142"><a href="/opinion/695142/united-states-v-michael-a-whren/#374" aria-description="Citation for case: United States v. Michael A. Whren">53 F. 3d 371, 374-375</a></span> (CADC 1995). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./516/1036/">516 U. S. 1036</a></span> (1996).
 </p>
<p id="b907-6">
  II
 </p>
<p id="b907-7">
  The Fourth Amendment guarantees “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” Temporary detention of individuals during the stop of an automobile by the police, even if only for a brief period and for a limited purpose, constitutes a “seizure” of “persons” within the
  <span citation-index="1" class="star-pagination" label="810"> 
   *810
   </span>
  meaning of this provision. See
  <em>
   Delaware
  </em>
  v.
  <em>
   Prouse,
  </em>
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653</a></span> (1979);
  <em>
   United States
  </em>
  v.
  <em>
   Martinez-Fuerte,
  </em>
  <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556</a></span> (1976);
  <em>
   United States
  </em>
  v.
  <em>
   Brignoni-Ponce,
  </em>
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975). An automobile stop is thus subject to the constitutional imperative that it not be “unreasonable” under the circumstances. As a general matter, the decision to stop an automobile is reasonable where the police have probable cause to believe that a traffic violation has occurred. See
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 659</a></span>;
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109</a></span> (1977)
  <em>
   (per curiam).
  </em>
</p>
<p id="b908-5">
  Petitioners accept that Officer Soto had probable cause to believe that various provisions of the District of Columbia traffic code had been violated. See 18 D. C. Mun. Regs. §§2213.4 (1995) (“An operator shall . . . give full time and attention to the operation of the vehicle”); 2204.3 (“No person shall turn any vehicle ... without giving an appropriate signal”); 2200.3 (“No person shall drive a vehicle ... at a speed greater than is reasonable and prudent under the conditions”). They argue, however, that “in the unique context of civil traffic regulations” probable cause is not enough. Since, they contend, the use of automobiles is so heavily and minutely regulated that total compliance with traffic and safety rules is nearly impossible, a police officer will almost invariably be able to catch any given motorist in a technical violation. This creates the temptation to use traffic stops as a means of investigating other law violations, as to which no probable cause or even articulable suspicion exists. Petitioners, who are both black, further contend that police officers might decide which motorists to stop based on decidedly impermissible factors, such as the race of the car’s occupants. To avoid this danger, they say, the Fourth Amendment test for traffic stops should be, not the normal one (applied by the Court of Appeals) of whether probable cause existed to justify the stop; but rather, whether a police officer, acting reasonably, would have made the stop for the reason given.
 </p>
<p id="b909-4">
<span citation-index="1" class="star-pagination" label="811"> 
   *811
   </span>
  A
 </p>
<p id="b909-5">
  Petitioners contend that the standard they propose is consistent with our past cases’ disapproval of police attempts to use valid bases of action against citizens as pretexts for pursuing other investigatory agendas. We are reminded that in
  <em>
   Florida
  </em>
  v.
  <em>
   Wells,
  </em>
  <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#4" aria-description="Citation for case: Florida v. Wells">495 U. S. 1, 4</a></span> (1990), we stated that “an inventory search
  <a class="footnote" href="#fn[1]" id="fn[1]_ref">
   [1]
  </a>
  must not be a ruse for a general rummaging in order to discover incriminating evidence”; that in
  <em>
   Colorado
  </em>
  v.
  <em>
   Bertine,
  </em>
  <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#372" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 372</a></span> (1987), in approving an inventory search, we apparently thought it significant that there had been “no showing that the police, who were following standardized procedures, acted in bad faith or for the sole purpose of investigation”; and that in
  <em>
   New York
  </em>
  v.
  <em>
   Burger,
  </em>
  <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#716" aria-description="Citation for case: New York v. Burger">482 U. S. 691, 716-717, n. 27</a></span> (1987), we observed, in upholding the constitutionality of a warrantless administrative inspection,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  that the search did not appear to be “a 'pretext’ for obtaining evidence of . . . violation of . . . penal laws.” But only an undiscerning reader would regard these cases as endorsing the principle that ulterior motives can invalidate police conduct that is justifiable on the basis of probable cause to believe that a violation of law has occurred. In each case we were addressing the validity of a search conducted in the
  <em>
   absence
  </em>
  of probable cause. Our quoted statements simply explain that the exemption from the need for probable cause (and warrant), which is accorded to searches made for the purpose of inventory or administrative
  <span citation-index="1" class="star-pagination" label="812"> 
   *812
   </span>
  regulation, is not accorded to searches that are
  <em>
   not
  </em>
  made for those purposes. See
  <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#371" aria-description="Citation for case: Colorado v. Bertine"><em>
   Bertine, supra,
  </em>
  at 371-372</a></span>;
  <span class="citation" data-id="9431050"><a href="/opinion/111927/new-york-v-burger/#702" aria-description="Citation for case: New York v. Burger"><em>
   Burger, supra,
  </em>
  at 702-703</a></span>.
 </p>
<p id="b910-5">
  Petitioners also rely upon
  <em>
   Colorado
  </em>
  v.
  <em>
   Bannister,
  </em>
  <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">449 U. S. 1</a></span> (1980)
  <em>
   (per curiam),
  </em>
  a case which, like this one, involved a traffic stop as the prelude to a plain-view sighting and arrest on charges wholly unrelated to the basis for the stop. Petitioners point to our statement that “[tjhere was no evidence whatsoever that the officer’s presence to issue a traffic citation was a pretext to confirm any other previous suspicion about the occupants” of the car.
  <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/#4" aria-description="Citation for case: Colorado v. Bannister"><em>
   Id.,
  </em>
  at 4, n. 4</a></span>. That dictum
  <em>
   at most
  </em>
  demonstrates that the Court in
  <em>
   <span class="citation" data-id="110351"><a href="/opinion/110351/colorado-v-bannister/" aria-description="Citation for case: Colorado v. Bannister">Bannister</a></span>
  </em>
  found no need to inquire into the question now under discussion; not that it was certain of the answer. And it may demonstrate even less than that: If by “pretext” the Court meant that the officer really had not seen the car speeding, the statement would mean only that there was no reason to doubt probable cause for the traffic stop.
 </p>
<p id="b910-6">
  It would, moreover, be anomalous, to say the least, to treat a statement in a footnote in the
  <em>
   per curiam Bannister
  </em>
  opinion as indicating a reversal of our prior law. Petitioners’ difficulty is not simply a lack of affirmative support for their position. Not only have we never held, outside the context of inventory search or administrative inspection (discussed above), that an officer’s motive invalidates objectively justifiable behavior under the Fourth Amendment; but we have repeatedly held and asserted the contrary. In
  <em>
   United States
  </em>
  v.
  <em>
   Villamonte-Marquez,
  </em>
  <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/#584" aria-description="Citation for case: United States v. Villamonte-Marquez">462 U. S. 579, 584, n. 3</a></span> (1983), we held that an otherwise valid warrantless boarding of a vessel by customs officials was not rendered invalid “because the customs officers were accompanied by a Louisiana state policeman, and were following an informant’s tip that a vessel in the ship channel was thought to be carrying marihuana.” We flatly dismissed the idea that an ulterior motive might serve to strip the agents of their legal justification. In
  <em>
   United States
  </em>
  v.
  <em>
   Robinson,
  </em>
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), we held that
  <span citation-index="1" class="star-pagination" label="813"> 
   *813
   </span>
  a traffic-violation arrest (of the sort here) would not be rendered invalid by the fact that it was “a mere pretext for a narcotics search,”
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#221" aria-description="Citation for case: United States v. Robinson"><em>
   id.,
  </em>
  at 221, n. 1</a></span>; and that a lawful post-arrest search of the person would not be rendered invalid by the fact that it was not motivated by the officer-safety concern that justifies such searches, see
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#236" aria-description="Citation for case: United States v. Robinson"><em>
   id.,
  </em>
  at 236</a></span>. See also
  <em>
   Gustafson
  </em>
  v.
  <em>
   Florida,
  </em>
  <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260, 266</a></span> (1973). And in
  <em>
   Scott
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 138</a></span> (1978), in rejecting the contention that wiretap evidence was subject to exclusion because the agents conducting the tap had failed to make any effort to comply with the statutory requirement that unauthorized acquisitions be minimized, we said that “[sjubjective intent alone ... does not make otherwise lawful conduct illegal or unconstitutional.” We described
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson</a></span>
  </em>
  as having established that “the fact that the officer does not have the state of mind which is hypothecated by the reasons which provide the legal justification for the officer’s action does not invalidate the action taken as long as the circumstances, viewed objectively, justify that action.” <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#136" aria-description="Citation for case: Scott v. United States">436 U. S., at 136, 138</a></span>.
 </p>
<p id="b911-5">
  We think these cases foreclose any argument that the constitutional reasonableness of traffic stops depends on the actual motivations of the individual officers involved. We of course agree with petitioners that the Constitution prohibits selective enforcement of the law based on considerations such as race. But the constitutional basis for objecting to intentionally discriminatory application of laws is the Equal Protection Clause, not the Fourth Amendment. Subjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.
 </p>
<p id="b911-6">
  B
 </p>
<p id="b911-7">
  Recognizing that we have been unwilling to entertain Fourth Amendment challenges based on the actual motivations of individual officers, petitioners disavow any intention to make the individual officer’s subjective good faith the touchstone of “reasonableness.” They insist that the stand
  <span citation-index="1" class="star-pagination" label="814"> 
   *814
   </span>
  ard they have put forward — whether the officer’s conduct deviated materially from usual police practices, so that a reasonable officer in the same circumstances would not have made the stop for the reasons given — is an “objective” one.
 </p>
<p id="b912-4">
  But although framed in empirical terms, this approach is plainly and indisputably driven by subjective considerations. Its whole purpose is to prevent the police from doing under the guise of enforcing the traffic code what they would like to do for different reasons. Petitioners’ proposed standard may not use the word-“pretext,” but it is designed to combat nothing other than the perceived “danger” of the pretextual stop, albeit only indirectly and over the run of cases. Instead of asking whether the individual officer had the proper state of mind, the petitioners would have us ask, in effect, whether (based on general police practices) it is plausible to believe that the officer had the proper state of mind.
 </p>
<p id="b912-5">
  Why one would frame a test designed to combat pretext in such fashion that the court cannot take into account
  <em>
   actual and admitted pretext
  </em>
  is a curiosity that can only be explained by the fact that our cases have foreclosed the more sensible option. If those cases were based only upon the evidentiary difficulty of establishing subjective intent, petitioners’ attempt to root out subjective vices through objective means might make sense. But they were not based only upon that, or indeed even principally upon that. Their principal basis — which applies equally to attempts to reach subjective intent through ostensibly objective means — is simply that the Fourth Amendment’s concern with “reasonableness” allows certain actions to be taken in certain circumstances,
  <em>
   whatever
  </em>
  the subjective intent. See,
  <em>
   e. g., Robinson, supra,
  </em>
  at 236 (“Since it is the fact of custodial arrest which gives rise to the authority to search, it is of no moment that [the officer] did not indicate any subjective fear of the [arrestee] or that he did not himself suspect that [the arrestee] was armed”) (footnotes omitted);
  <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida"><em>
   Gustafson, supra,
  </em>
  at 266</a></span> (same). But even if our concern had been only an evidentiary one,
  <span citation-index="1" class="star-pagination" label="815"> 
   *815
   </span>
  petitioners’ proposal would by no means assuage it. Indeed, it seems to us somewhat easier to figure out the intent of an individual officer than to plumb the collective consciousness of law enforcement in order to determine whether a “reasonable officer” would have been moved to act upon the traffic violation. While police manuals and standard procedures may sometimes provide objective assistance, ordinarily one would be reduced to speculating about the hypothetical reaction of a hypothetical constable — an exercise that might be called virtual subjectivity.
 </p>
<p id="b913-5">
  Moreover, police enforcement practices, even if they could be practicably assessed by a judge, vary from place to place and from time to time. We cannot accept that the search and seizure protections of the Fourth Amendment are so variable, cf.
  <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#265" aria-description="Citation for case: Gustafson v. Florida"><em>
   Gustafson, supra,
  </em>
  at 265</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Caceres,
  </em>
  <span class="citation" data-id="9427514"><a href="/opinion/110049/united-states-v-caceres/#755" aria-description="Citation for case: United States v. Caceres">440 U. S. 741, 755-756</a></span> (1979), and can be made to turn upon such trivialities. The difficulty is illustrated by petitioners’ arguments in this case. Their claim that a reasonable officer would not have made this stop is based largely on District of Columbia police regulations which permit plainclothes officers in unmarked vehicles to enforce traffic laws “only in the case of a violation that is so grave as to pose an
  <em>
   immediate threat
  </em>
  to the safety of others.” Metropolitan Police Department, Washington, D. C., General Order 303.1, pt. 1, Objectives and Policies (A)(2)(4) (Apr. 30, 1992), reprinted as Addendum to Brief for Petitioners. This basis of invalidation would not apply in jurisdictions that had a different practice. And it would not have applied even in the District of Columbia, if Officer Soto had been wearing a uniform or patrolling in a marked police cruiser.
 </p>
<p id="b913-6">
  Petitioners argue that our cases support insistence upon police adherence to standard practices as an objective means of rooting out pretext. They cite no holding to that effect, and dicta in only two cases. In
  <em>
   Abel
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">362 U. S. 217</a></span> (1960), the petitioner had been arrested by the Immigration and Naturalization Service (INS), on the basis of
  <span citation-index="1" class="star-pagination" label="816"> 
   *816
   </span>
  an administrative warrant that, he claimed, had been issued on pretextual grounds in order to enable the Federal Bureau of Investigation (FBI) to search his room after his arrest. We regarded this as an allegation of “serious misconduct,” but rejected Abel’s claims on the ground that “[a] finding of bad faith is ... not open to us on th[e] record” in light of the findings below, including the finding that “ ‘the proceedings taken by the [INS] differed in no respect from what would have been done in the case of an individual concerning whom [there was no pending FBI investigation],’”
  <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#226" aria-description="Citation for case: Abel v. United States"><em>
   id.,
  </em>
  at 226-227</a></span>. But it is a long leap from the proposition that following regular procedures is some evidence of lack of pretext to the proposition that failure to follow regular procedures
  <em>
   proves
  </em>
  (or is an operational substitute for) pretext.
  <em>
   <span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/" aria-description="Citation for case: Abel v. United States">Abel</a></span>,
  </em>
  moreover, did not involve the assertion that pretext could invalidate a search or seizure for which there was probable cause — and even what it said about pretext in other contexts is plainly inconsistent with the views we later stated in
  <em>
   Robinson, Gustafson, Scott,
  </em>
  and
  <em>
   <span class="citation" data-id="9429252"><a href="/opinion/110973/united-states-v-villamonte-marquez/" aria-description="Citation for case: United States v. Villamonte-Marquez">Villamonte-Marquez</a></span>.
  </em>
  In the other case claimed to contain supportive dicta,
  <em>
   United States
  </em>
  v.
  <em>
   Robinson,
  </em>
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), in approving a search incident to an arrest for driving without a license, we noted that the arrest was “not a departure from established police department practice.”
  <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#221" aria-description="Citation for case: United States v. Robinson"><em>
   Id.,
  </em>
  at 221, n. 1</a></span>. That was followed, however, by the statement that “[w]e leave for another day questions which would arise on facts different from these.”
  <em>
   <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Ibid.</a></span>
  </em>
  This is not even a dictum that purports to provide an answer, but merely one that leaves the question open.
 </p>
<p id="AdW">
<em>
   f
  </em>
  — i hH t — 4
 </p>
<p id="AE3">
  In what would appear to be an elaboration on the "reasonable officer” test, petitioners argue that the balancing inherent in any Fourth Amendment inquiry requires us to weigh the governmental and individual interests implicated in a traffic stop such as we have here. That balancing, petitioners claim, does not support investigation of minor traffic in
  <span citation-index="1" class="star-pagination" label="817"> 
   *817
   </span>
  fractions by plainclothes police in unmarked vehicles; such investigation only minimally advances the government’s interest in traffic safety, and may indeed retard it by producing motorist confusion and alarm — a view said to be supported by the Metropolitan Police Department’s own regulations generally prohibiting this practice. And as for the Fourth Amendment interests of the individuals concerned, petitioners point out that our cases acknowledge that even ordinary traffic stops entail “a possibly unsettling show of authority”; that they at best "interfere with freedom of movement, are inconvenient, and consume time” and at worst “may create substantial anxiety,”
  <em>
   Prouse,
  </em>
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#657" aria-description="Citation for case: Delaware v. Prouse">440 U. S., at 657</a></span>. That anxiety is likely to be even more pronounced when the stop is conducted by plainclothes officers in unmarked cars.
 </p>
<p id="b915-5">
  It is of course true that in principle every Fourth Amendment case, since it turns upon a “reasonableness” determination, involves a balancing of all relevant factors. With rare exceptions not applicable here, however, the result of that balancing is not in doubt where the search or seizure is based upon probable cause. That is why petitioners must rely upon cases like
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>
  </em>
  to provide examples of actual “balancing” analysis. There, the police action in question was a random traffic stop for the purpose of checking a motorist’s license and vehicle registration, a practice that — like the practices at issue in the inventory search and administrative inspection cases upon which petitioners rely in making their “pretext” claim — involves police intrusion
  <em>
   without the probable cause that is its traditional justification.
  </em>
  Our opinion in
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>
  </em>
  expressly distinguished the case from a stop based on precisely what is at issue here: “probable cause to believe that a driver is violating any one of the multitude of applicable traffic and equipment regulations.”
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse"><em>
   Id.,
  </em>
  at 661</a></span>. It noted approvingly that “[t]he foremost method of enforcing traffic and vehicle safety regulations ... is acting upon observed violations,”
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#659" aria-description="Citation for case: Delaware v. Prouse"><em>
   id.,
  </em>
  at 659</a></span>, which afford the “‘quantum of individualized suspicion’ ” necessary to ensure that police
  <span citation-index="1" class="star-pagination" label="818"> 
   *818
   </span>
  discretion is sufficiently constrained,
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">id.,</a></span>
  </em>
  at 654-655 (quoting
  <em>
   United States
  </em>
  v.
  <em>
   Martinez-Fuerte,
  </em>
  <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span>). What is true of
  <em>
   <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>
  </em>
  is also true of other cases that engaged in detailed “balancing” to decide the constitutionality of automobile stops, such as
  <em>
   <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte</a></span>,
  </em>
  which upheld checkpoint stops, see <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 556-562</a></span>, and
  <em>
   <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,
  </em>
  which disallowed so-called “roving patrol” stops, see <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 882</a></span>-884: The detailed “balancing” analysis was necessary because they involved seizures without probable cause.
 </p>
<p id="b916-5">
  Where probable cause has existed, the only cases in which we have found it necessary actually to perform the “balancing” analysis involved searches or seizures conducted in an extraordinary manner, unusually harmful to an individual’s privacy or even physical interests — such as, for example, seizure by means of deadly force, see
  <em>
   Tennessee
  </em>
  v.
  <em>
   Garner,
  </em>
  <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), unannounced entry into a home, see
  <em>
   Wilson
  </em>
  v.
  <em>
   Arkansas,
  </em>
  <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995), entry into a home without a warrant, see
  <em>
   Welsh
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984), or physical penetration of the body, see
  <em>
   Winston
  </em>
  v.
  <em>
   Lee,
  </em>
  <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/" aria-description="Citation for case: Winston v. Lee">470 U. S. 753</a></span> (1985). The making of a traffic stop out of uniform does not remotely qualify as such an extreme practice, and so is governed by the usual rule that probable cause to believe the law has been broken “outbalances” private interest in avoiding police contact.
 </p>
<p id="b916-6">
  Petitioners urge as an extraordinary factor in this case that the “multitude of applicable traffic and equipment regulations” is so large and so difficult to obey perfectly that virtually everyone is guilty of violation, permitting the police to single out almost whomever they wish for a stop. But we are aware of no principle that would allow us to decide at what point a code of law becomes so expansive and so commonly violated that infraction itself can no longer be the ordinary measure of the lawfulness of enforcement. And even if we could identify such exorbitant codes, we do not know by what standard (or what right) we would decide, as
  <span citation-index="1" class="star-pagination" label="819"> 
   *819
   </span>
  petitioners would have us do, which particular provisions are sufficiently important to merit enforcement.
 </p>
<p id="b917-5">
  For the run-of-the-mine case, which this surely is, we think there is no realistic alternative to the traditional common-law rule that probable cause justifies a search and seizure.
 </p>
<p id="b917-6">
  * * *
 </p>
<p id="b917-7">
  Here the District Court found that the officers had probable cause to believe that petitioners had violated the traffic code. That rendered the stop reasonable under the Fourth Amendment, the evidence thereby discovered admissible, and the upholding of the convictions by the Court of Appeals for the District of Columbia Circuit correct. The judgment is
 </p>
<p id="b917-8">
<em>
   Affirmed.
  </em>
</p>


<div class="footnotes"><div class="footnote" id="fn[1]" label="[1]">
<a class="footnote" href="#fn[1]_ref">
   [1]
  </a>
<p id="b909-6">
   1 An inventory search is the search of property lawfully seized and detained, in order to ensure that it is harmless, to secure valuable items (such as might be kept in a towed car), and to protect against false claims of loss or damage. See
   <em>
    South Dakota
   </em>
   v.
   <em>
    Opperman,
   </em>
   <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#369" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364, 369</a></span> (1976).
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b909-7">
   An administrative inspection is the inspection of business premises conducted by authorities responsible for enforcing a pervasive regulatory scheme — for example, unannounced inspection of a mine for compliance with health and safety standards. See
   <em>
    Donovan
   </em>
   v.
   <em>
    Dewey,
   </em>
   <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/#599" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594, 599-605</a></span> (1981).
  </p>
</div></div></opinion>
```

---
