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

## GROUP: _overhaul2/lake/cases/United States v. Gooch.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Gooch"
type: case
citation: "6 F.3d 673 (1993)"
parallel_cite: 93 Daily Journal DAR 12716
neutral_cite: "93 Cal. Daily Op. Serv. 7462; 1993 U.S. App. LEXIS 25518; 1993 WL 390206"
court: "U.S. Court of Appeals, Ninth Circuit"
court_level: coa
circuit: 9th
year: 1993
date_decided: 1993-10-06
docket: 92-30358
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 1993-09-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Gooch
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/"
  cluster_id: 654273
  opinion_id: 654273
  identity_checked: true
homes:
  - page: "[[Tents]]"
    role: "Key — Anchor"
related: ["[[Katz v. United States]]", "[[California v. Carney]]", "[[United States v. Basher]]"]
aliases: ["United States v. Gooch (9th Cir. 1993)", "United States v. Kenneth D. Gooch"]
tags: ["case", "fourth-amendment", "tent", "reasonable-expectation-of-privacy", "campground", "ninth-circuit"]
holding: "(Persuasive (outside circuit) — 9th Cir.) An occupant has a reasonable expectation of privacy in a tent in a public campground; 'a tent is more like a house than a car,' so its warrantless search violated the 4A."
lake:
  record_id: United States v. Gooch
  status: verified
  projected_at: 2026-07-09
---

# United States v. Gooch

*6 F.3d 673 (9th Cir. 1993)* · U.S. Court of Appeals, Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Responding to a 3:50 a.m. report that a man had fired a shot at a state campground, Stevens County officers located Kenneth Gooch — who had been living in a closed tent there for several days with no other residence — asleep in his tent. Without an arrest warrant, they ordered him out, arrested and handcuffed him, locked him in a patrol car 20 yards away, removed the other occupant, and then, still without a warrant, searched the tent and found a loaded handgun under his air mattress. A post-trial [[Common Legal Terms#suppression-hearing|suppression hearing]] held the firearm should have been suppressed; the government appealed.

## Issue
Whether a person has a Fourth Amendment [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a closed tent pitched on a public campground, such that a warrantless search of the tent violates the Fourth Amendment.

## Rule
Yes. A tent is treated as a dwelling for Fourth Amendment purposes, not as a vehicle. Occupancy of a tent requires "both a subjective and an objectively reasonable expectation of privacy in the tent." — 6 F.3d at 677 (citing [[Katz v. United States]]). ^pin-677

That expectation survives pitching the tent on public ground: "This reasonable expectation is not destroyed when a person's tent is pitched instead on a public campground where one is legally permitted to camp." — [*Id.*](https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/#:~:text=This%20reasonable%20expectation%20is%20not) ^pin-677a

The court rejected any vehicle analogy and held: "The district court did not err in concluding a tent is more like a house than a car. We hold that Gooch had a reasonable expectation of privacy such that the warrantless search of his tent violated the Fourth Amendment." — [*Id.*](https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/#:~:text=The%20district%20court%20did%20not%20err%20in%20concluding%20a) ^pin-677b

## Application
On these facts the warrantless tent search was unlawful. Gooch had lived in the closed tent for days with no other residence, establishing a subjective expectation of privacy that the district court's finding (not [[Common Legal Terms#clear-error|clearly erroneous]]) supported; the government's argument that a lawbreaker expecting police response can have no such expectation would, the court noted, deny privacy to anyone because "the expectation of arrest is always imminent." The expectation was also objectively reasonable: although a tent is movable, "[t]he fact that a tent may be moved, alone, is not enough to remove the Fourth Amendment protections," and a tent is more analogous to a movable closed container — or a house — than to a car to which the automobile exception of [[California v. Carney]] would apply. With Gooch secured in the patrol car and no [[Exigent Circumstances and Hot Pursuit|exigency]], the warrantless search of the tent violated the Fourth Amendment.

## Conclusion
Gooch had a Fourth Amendment [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in his tent; the warrantless search violated the Fourth Amendment, and the suppression of the firearm was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- No negative subsequent treatment identified. *Gooch* remains the Ninth Circuit's leading statement that a tent occupied as a dwelling carries a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] ("more like a house than a car"), distinguishing the vehicle rule of [[California v. Carney]].

## Appears on
- [[Tents]] — *Key — Anchor*

## Sources
- *United States v. Gooch*, 6 F.3d 673 (9th Cir. 1993) — https://www.courtlistener.com/opinion/654273/united-states-v-kenneth-d-gooch/ — pinpoint: 677. (CL's copy carries no internal star-pagination; the 677 pinpoint is the standard reporter pinpoint for the reasonable-expectation holding — quotes verbatim-verified against the opinion text.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b606ec978358d8c1", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Gooch"}, "payload": {"all": [{"cite": "6 F.3d 673", "page": "673", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "6"}, {"cite": "93 Daily Journal DAR 12716", "page": "12716", "reporter": "Daily Journal DAR", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "93"}, {"cite": "93 Cal. Daily Op. Serv. 7462", "page": "7462", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "93"}, {"cite": "1993 U.S. App. LEXIS 25518", "page": "25518", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1993"}, {"cite": "1993 WL 390206", "page": "390206", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1993"}], "display": "6 F.3d 673", "official": {"cite": "6 F.3d 673", "page": "673", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "6"}, "official_selection_present": true, "record_id": "United States v. Gooch"}}
{"assertion_id": "187af09038a3bd12", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-677a", "record_id": "United States v. Gooch"}, "payload": {"fragment": "#:~:text=This%20reasonable%20expectation%20is%20not", "page": null, "pin_id": "pin-677a", "pinpoint_status": "slip-only", "quote": "This reasonable expectation is not destroyed when a person's tent is pitched instead on a public campground where one is legally permitted to camp.", "quote_fidelity": "matched", "record_id": "United States v. Gooch", "star_marker": null}}
{"assertion_id": "85ee37aed7cd58cf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-677", "record_id": "United States v. Gooch"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-677", "pinpoint_status": "slip-only", "quote": "--- # United States v. Gooch *6 F.3d 673 (9th Cir. 1993)* · U.S. Court of Appeals, Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Responding to a 3:50 a.m. report that a man had fired a shot at a state campground, Stevens County officers located Kenneth Gooch — who had been living in a closed tent there for several days with no other residence — asleep in his tent. Without an arrest warrant, they ordered him out, arrested and handcuffed him, locked him in a patrol car 20 yards away, removed the other occupant, and then, still without a warrant, searched the tent and found a loaded handgun under his air mattress. A post-trial suppression hearing held the firearm should have been suppressed; the government appealed. ## Issue Whether a person has a Fourth Amendment reasonable expectation of privacy in a closed tent pitched on a public campground, such that a warrantless search of the tent violates the Fourth Amendment. ## Rule Yes. A tent is treated as a dwelling for Fourth Amendment purposes, not as a vehicle. Occupancy of a tent requires", "quote_fidelity": "mismatch", "record_id": "United States v. Gooch", "star_marker": null}}
{"assertion_id": "fb25c59479b594a3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-677b", "record_id": "United States v. Gooch"}, "payload": {"fragment": "#:~:text=The%20district%20court%20did%20not%20err%20in%20concluding%20a", "page": null, "pin_id": "pin-677b", "pinpoint_status": "slip-only", "quote": "The district court did not err in concluding a tent is more like a house than a car. We hold that Gooch had a reasonable expectation of privacy such that the warrantless search of his tent violated the Fourth Amendment.", "quote_fidelity": "matched", "record_id": "United States v. Gooch", "star_marker": null}}
{"assertion_id": "e91187151b560346", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Gooch"}, "payload": {"as_of_content": "1993-09-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Gooch", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Gooch

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Gooch",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Kenneth D. Gooch",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellant, v. Kenneth D. GOOCH, Defendant-Appellee",
    "input_case_name": "United States v. Gooch",
    "court": "U.S. Court of Appeals, Ninth Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "1993-10-06",
    "year": 1993,
    "docket": "92-30358",
    "cluster_id": 654273,
    "lead_opinion_id": 654273,
    "sibling_ids": [
      654273,
      9485948,
      9485949
    ],
    "absolute_url": "/opinion/654273/united-states-v-kenneth-d-gooch/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "6 F.3d 673",
      "volume": "6",
      "reporter": "F.3d",
      "page": "673",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 Daily Journal DAR 12716",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "12716",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "93 Cal. Daily Op. Serv. 7462",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "7462",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. App. LEXIS 25518",
        "volume": "1993",
        "reporter": "U.S. App. LEXIS",
        "page": "25518",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 390206",
        "volume": "1993",
        "reporter": "WL",
        "page": "390206",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "6 F.3d 673",
        "volume": "6",
        "reporter": "F.3d",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Daily Journal DAR 12716",
        "volume": "93",
        "reporter": "Daily Journal DAR",
        "page": "12716",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 Cal. Daily Op. Serv. 7462",
        "volume": "93",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "7462",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 U.S. App. LEXIS 25518",
        "volume": "1993",
        "reporter": "U.S. App. LEXIS",
        "page": "25518",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1993 WL 390206",
        "volume": "1993",
        "reporter": "WL",
        "page": "390206",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "6 F.3d 673",
    "official_selection": {
      "court_class": "coa",
      "selected": "6 F.3d 673",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-677",
      "page": null,
      "quote": "--- # United States v. Gooch *6 F.3d 673 (9th Cir. 1993)* \u00b7 U.S. Court of Appeals, Ninth Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Responding to a 3:50 a.m. report that a man had fired a shot at a state campground, Stevens County officers located Kenneth Gooch \u2014 who had been living in a closed tent there for several days with no other residence \u2014 asleep in his tent. Without an arrest warrant, they ordered him out, arrested and handcuffed him, locked him in a patrol car 20 yards away, removed the other occupant, and then, still without a warrant, searched the tent and found a loaded handgun under his air mattress. A post-trial suppression hearing held the firearm should have been suppressed; the government appealed. ## Issue Whether a person has a Fourth Amendment reasonable expectation of privacy in a closed tent pitched on a public campground, such that a warrantless search of the tent violates the Fourth Amendment. ## Rule Yes. A tent is treated as a dwelling for Fourth Amendment purposes, not as a vehicle. Occupancy of a tent requires",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-677a",
      "page": null,
      "quote": "This reasonable expectation is not destroyed when a person's tent is pitched instead on a public campground where one is legally permitted to camp.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 7730,
      "fragment": "#:~:text=This%20reasonable%20expectation%20is%20not",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-677b",
      "page": null,
      "quote": "The district court did not err in concluding a tent is more like a house than a car. We hold that Gooch had a reasonable expectation of privacy such that the warrantless search of his tent violated the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 16441,
      "fragment": "#:~:text=The%20district%20court%20did%20not%20err%20in%20concluding%20a",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1993-09-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Gooch",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "United States v. Gooch:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rodrigo Sandoval",
          "cluster_id": 767260,
          "cite": [
            "200 F.3d 659",
            "2000 Cal. Daily Op. Serv. 581",
            "2000 Daily Journal DAR 907",
            "2000 U.S. App. LEXIS 805",
            "2000 WL 48991"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Yong Hyon Kim",
          "cluster_id": 672873,
          "cite": [
            "27 F.3d 947",
            "1994 U.S. App. LEXIS 16298",
            "1994 WL 287235"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Basher",
          "cluster_id": 183144,
          "cite": [
            "629 F.3d 1161",
            "2011 U.S. App. LEXIS 1064",
            "2011 WL 167045"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tibolt",
          "cluster_id": 196502,
          "cite": [
            "72 F.3d 965",
            "1995 U.S. App. LEXIS 37154",
            "1995 WL 757848"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gardner v. Loomis Armored Inc.",
          "cluster_id": 1179712,
          "cite": [
            "913 P.2d 377"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christopher McIver United States of America v. Brian Eberle",
          "cluster_id": 765594,
          "cite": [
            "186 F.3d 1119",
            "99 Cal. Daily Op. Serv. 6304",
            "99 Daily Journal DAR 8052",
            "1999 U.S. App. LEXIS 18290",
            "1999 WL 587573"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robin Lynn Bailey v. Anthony Newland, Warden",
          "cluster_id": 774778,
          "cite": [
            "263 F.3d 1022",
            "2001 Cal. Daily Op. Serv. 7675",
            "2001 Daily Journal DAR 9513",
            "2001 U.S. App. LEXIS 19398",
            "2001 WL 994913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lawrence Ezekiel Reid, United States of America v. Wayne Blake",
          "cluster_id": 770456,
          "cite": [
            "226 F.3d 1020",
            "2000 Cal. Daily Op. Serv. 7702",
            "2000 Daily Journal DAR 10217",
            "2000 U.S. App. LEXIS 23203",
            "2000 WL 1290375"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ray Lewis Bowman, A.K.A. Charles Clark",
          "cluster_id": 769118,
          "cite": [
            "215 F.3d 951",
            "55 Fed. R. Serv. 105",
            "2000 Cal. Daily Op. Serv. 4635",
            "2000 U.S. App. LEXIS 13013",
            "2000 WL 744083"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Harold McRae",
          "cluster_id": 758065,
          "cite": [
            "156 F.3d 708",
            "1998 U.S. App. LEXIS 24526",
            "1998 WL 673216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salemme",
          "cluster_id": 2510809,
          "cite": [
            "91 F. Supp. 2d 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fisher v. City of San Jose",
          "cluster_id": 1355654,
          "cite": [
            "558 F.3d 1069",
            "2009 U.S. App. LEXIS 5567",
            "2009 WL 606132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Collazo-Aponte",
          "cluster_id": 8619338,
          "cite": [
            "216 F.3d 163",
            "54 Fed. R. Serv. 3d 1311",
            "2000 U.S. App. LEXIS 14658"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jose Ortiz-Sandoval v. Linda Clarke, Warden",
          "cluster_id": 781363,
          "cite": [
            "323 F.3d 1165",
            "2003 Cal. Daily Op. Serv. 2602",
            "2003 U.S. App. LEXIS 5697",
            "2003 WL 1480565"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brett W. Dumstrey",
          "cluster_id": 3169926,
          "cite": [
            "366 Wis. 2d 64",
            "2016 WI 3",
            "873 N.W.2d 502",
            "2016 Wisc. LEXIS 2"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Piedad Barajas-Avalos, AKA Piedad Barajas-Avaslos",
          "cluster_id": 787179,
          "cite": [
            "377 F.3d 1040",
            "2004 U.S. App. LEXIS 15362",
            "2004 WL 1656517"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whiting v. State",
          "cluster_id": 1479286,
          "cite": [
            "885 A.2d 785",
            "389 Md. 334",
            "2005 Md. LEXIS 643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Casel Nora",
          "cluster_id": 2722177,
          "cite": [
            "765 F.3d 1049",
            "2014 U.S. App. LEXIS 16677",
            "2014 WL 4235955"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hughston",
          "cluster_id": 2285590,
          "cite": [
            "168 Cal. App. 4th 1062",
            "85 Cal. Rptr. 3d 890",
            "2008 Cal. App. LEXIS 2361"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rivera-Melendez",
          "cluster_id": 198984,
          "cite": [
            "216 F.3d 163"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Nishi",
          "cluster_id": 5811207,
          "cite": [
            "207 Cal. App. 4th 954",
            "143 Cal. Rptr. 3d 882",
            "2012 WL 2870591",
            "2012 Cal. App. LEXIS 806"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wakeford",
          "cluster_id": 884811,
          "cite": [
            "1998 MT 16",
            "953 P.2d 1065",
            "287 Mont. 220",
            "55 State Rptr. 56",
            "1998 Mont. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Arellano-Ochoa, United States of America v. Jose Luis Arellano-Ochoa",
          "cluster_id": 795590,
          "cite": [
            "461 F.3d 1142",
            "2006 U.S. App. LEXIS 22466",
            "2006 WL 2506395"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alward v. State",
          "cluster_id": 1119018,
          "cite": [
            "912 P.2d 243",
            "112 Nev. 141",
            "66 A.L.R. 5th 763",
            "1996 Nev. LEXIS 24"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gooch:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(654273 OR 9485948 OR 9485949) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 2,
        "triage_snippet_classified": 11
      },
      "lane2_top_cited": {
        "query": "cites:(654273 OR 9485948 OR 9485949)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yJnM9MjQwMDYzOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28654273+OR+9485948+OR+9485949%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(654273 OR 9485948 OR 9485949)",
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
    "complete_query": "cites:(654273 OR 9485948 OR 9485949)",
    "indexed_citing_opinions": 61,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 654273,
        "count": 54,
        "count_source": "search"
      },
      {
        "opinion_id": 9485948,
        "count": 7,
        "count_source": "search"
      },
      {
        "opinion_id": 9485949,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 119,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-gooch.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjE1NzYwOTYmcz0yMzE5MzE2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28654273+OR+9485948+OR+9485949%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 654273,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 111186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 603575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 1245135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 654273,
        "cited_id": 1500109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 111186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 112136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 546167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 566881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485949,
        "cited_id": 9430502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 251769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 431931,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 441786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 452994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 460378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 465254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 475484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 480405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 506240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 522259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 566881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 567665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 603575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 1245135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 1420587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 1500109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 7841712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 8693761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 8947287,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9049052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9108589,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9426247,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9485948,
        "cited_id": 9427384,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "RU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T00:07:12Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:07:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:07:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:11:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:07:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Gooch

```
<p class="case_cite"><span class="citation" data-id="9485948"><a href="/opinion/654273/united-states-v-kenneth-d-gooch/" aria-description="Citation for case: United States v. Kenneth D. Gooch">6 F.3d 673</a></span></p>
    <p class="case_cite"><span class="citation no-link">62 USLW 2295</span></p>
    <p class="parties">UNITED STATES of America, Plaintiff-Appellant,<br>v.<br>Kenneth D. GOOCH, Defendant-Appellee.</p>
    <p class="docket">No. 92-35428.</p>
    <p class="court">United States Court of Appeals,<br>Ninth Circuit.</p>
    <p class="date">Argued and Submitted May 4, 1993.<br>Decided Oct. 6, 1993.</p>
    <div class="prelims">
      <p class="indent">Timothy J. Ohms, Asst. U.S. Atty., Spokane, WA, for plaintiff-appellant.</p>
      <p class="indent">Daniel J. Keane and Brian L. Meck, Keane &amp; Rasmussen, Spokane, WA, for defendant-appellee.</p>
      <p class="indent">Appeal from the United States District Court for the Eastern District of Washington.</p>
      <p class="indent">Before:  WRIGHT, ALARCON, and BEEZER, Circuit Judges.</p>
      <p class="indent">BEEZER, Circuit Judge:</p>
    </div>
    <div class="num" id="p1">
      <span class="num">1</span>
      <p class="indent">The United States appeals the district court's judgment of acquittal and the subsequent order of dismissal with prejudice of defendant Kenneth D. Gooch's conviction for being a felon in possession of a firearm.  The government contends that a warrantless arrest of Gooch and a warrantless search of Gooch's tent did not violate the Fourth Amendment.  We affirm.</p>
    </div>
    <div class="num" id="p2">
      <span class="num">2</span>
      <p class="indent">* At about 3:50 a.m., a woman called the Stevens County Sheriff's office on behalf of Marc Cole, who claimed a man had shot at him at the state campground.  Two officers responded.  As they neared the campsite, they observed a vehicle leaving the campsite.  The occupants told the officers that Gooch was "hurting people" at the campground and that shots had been fired.  Closer to the campground, the officers encountered Marc Cole.  Cole said Gooch had fired a shot in his direction after a fight in which Gooch tried to "stick [Cole's] head into the fire."   These incidents occurred between midnight and 2:00 a.m.</p>
    </div>
    <div class="num" id="p3">
      <span class="num">3</span>
      <p class="indent">The officers arrived at the entrance to the campground at approximately 5:00 a.m. and then waited some time for the arrival of another deputy and a reserve officer.  It was daylight by this time.  Three officers then headed down the entrance road to the campsite itself, a distance of approximately one mile.  On the way, they encountered a young man, who told them Gooch was in his tent with a woman.  The district court found that when the officers arrived at the campsite, they observed that the campsite was quiet and they determined that Gooch was asleep in his closed tent.<a class="footnote" href="#fn1" id="fn1_ref">1</a>  Gooch had been living in the tent for several days;  he had no other residence.</p>
    </div>
    <div class="num" id="p4">
      <span class="num">4</span>
      <p class="indent">The officers, without seeking an arrest warrant, ordered Gooch out of the tent, patted him down, and arrested him.  He was handcuffed and locked in the patrol car 20 yards from the tent.  The officers then ordered the other occupant of the tent, Mary Baker, out of the tent.  The district court found that the officers then talked to other campers for about 15 minutes.  The other campers were not obstructive or threatening, nor was there any indication that they had been involved in the criminal activity.</p>
    </div>
    <div class="num" id="p5">
      <span class="num">5</span>
      <p class="indent">Still lacking a warrant, the officers searched the tent for the firearm.  One of them found a loaded handgun under Gooch's air mattress in the tent.</p>
    </div>
    <div class="num" id="p6">
      <span class="num">6</span>
      <p class="indent">After dismissal of state charges, a federal indictment for being a felon in possession of a firearm was then returned.  A jury convicted Gooch of the federal charge.  Gooch timely moved for judgment of acquittal and for a new trial.  Gooch also filed a Sec. 2255 petition for habeas corpus in which he claimed ineffective assistance of counsel in that his counsel had failed to move to suppress the firearm.  The district court held a post-trial suppression hearing and determined that the firearm, along with the holster and ammunition, should have been suppressed and that the warrantless arrest was invalid.  The district court determined that Gooch had a reasonable expectation of privacy in the tent which was protected under the Fourth Amendment, that there were no "exigent circumstances," and that even if the arrest was lawful, the search was not a valid search incident to arrest.</p>
    </div>
    <p>II</p>
    <div class="num" id="p7">
      <span class="num">7</span>
      <p class="indent">The threshold issue is whether the Fourth Amendment protects a person's privacy interests in a tent located on a public campground.  The lawfulness of a search or arrest is reviewed de novo.  United States v. Tarazon, <span class="citation" data-id="9484087"><a href="/opinion/603575/united-states-v-ramon-p-tarazon/#1048" aria-description="Citation for case: United States v. Ramon P. Tarazon">989 F.2d 1045, 1048</a></span> (9th Cir.1993), cert. denied, --- U.S. ----, <span class="citation multiple-matches"><a href="/c/S.Ct./114/155/">114 S.Ct. 155</a></span>, <span class="citation no-link">126 L.Ed.2d 116</span> (1993).  The district court's factual findings are reviewed for clear error.  United States v. Echegoyen, <span class="citation" data-id="475484"><a href="/opinion/475484/united-states-v-rodolfo-echegoyen/#1277" aria-description="Citation for case: United States v. Rodolfo Echegoyen">799 F.2d 1271, 1277</a></span> (9th Cir.1986).</p>
    </div>
    <p>III</p>
    <div class="num" id="p8">
      <span class="num">8</span>
      <p class="indent">Gooch must have had both a subjective and an objectively reasonable expectation of privacy in the tent.  Katz v. United States, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U.S. 347, 361</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#516" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507, 516</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967).  The government contends that Gooch could not have had a subjective expectation of privacy in the tent since he could have expected the police to respond to the disturbance he caused and to intrude on his privacy.  According to this view, no lawbreaker would have a subjective expectation of privacy in any place because the expectation of arrest is always imminent.  The court's finding that Gooch established a subjective expectation of privacy is not clearly erroneous.</p>
    </div>
    <div class="num" id="p9">
      <span class="num">9</span>
      <p class="indent">We have already established that a person can have an objectively reasonable expectation of privacy in a tent on private property.  LaDuke v. Nelson, <span class="citation" data-id="452994"><a href="/opinion/452994/charles-laduke-v-alan-c-nelson-etc/" aria-description="Citation for case: Charles Laduke v. Alan C. Nelson, Etc.">762 F.2d 1318</a></span>, 1326 n. 11, 1332 n. 19 (9th Cir.1985).  Accord LaDuke v. Castillo, <span class="citation" data-id="1415838"><a href="/opinion/1415838/laduke-v-castillo/" aria-description="Citation for case: LaDuke v. Castillo">455 F.Supp. 209</a></span> (E.D.Wash.1978).  This reasonable expectation is not destroyed when a person's tent is pitched instead on a public campground where one is legally permitted to camp.  The Fourth Amendment "protects people, not places."  Katz, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U.S. at 351</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#511" aria-description="Citation for case: Katz v. United States">88 S.Ct. at 511</a></span>;  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">id. at 351-52</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#511" aria-description="Citation for case: Katz v. United States">88 S.Ct. at 511</a></span> (What a citizen "seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected.");  United States v. Chadwick, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U.S. 1, 7</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#2481" aria-description="Citation for case: United States v. Chadwick">97 S.Ct. 2476, 2481</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">53 L.Ed.2d 538</a></span> (1977).  In Rakas v. Illinois, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">439 U.S. 128</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. 421</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">58 L.Ed.2d 387</a></span> (1978), the Court interpreted Katz to hold that "capacity to claim the protection of the Fourth Amendment depends not upon a property right in the invaded place but upon whether the person who claims the protection of the Amendment has a legitimate expectation of privacy in the invaded place."  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#143" aria-description="Citation for case: Rakas v. Illinois">Id. at 143</a></span>, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#430" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 430</a></span>;  <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">id.</a></span> at 144 n. 12, <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/" aria-description="Citation for case: Rakas v. Illinois">99 S.Ct. at 430</a></span> n. 12.  ("Expectations of privacy protected by the Fourth Amendment ... need not be based on a common-law interest in real or personal property, or on the invasion of such an interest.").</p>
    </div>
    <div class="num" id="p10">
      <span class="num">10</span>
      <p class="indent">The government would have us compare Gooch's case to those involving mobile motor homes, in which a person has a reduced expectation of privacy.  See California v. Carney, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">471 U.S. 386</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">105 S.Ct. 2066</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/" aria-description="Citation for case: California v. Carney">85 L.Ed.2d 406</a></span> (1985) (warrantless search of mobile home in which defendant resided did not violate Fourth Amendment because automobile exception applied).  The fact that a tent may be moved, alone, is not enough to remove the Fourth Amendment protections.  As noted above, tents are protected under the Fourth Amendment like a more permanent structure.  Also, a tent is more analogous to a (large) movable container than to a vehicle;  the Fourth Amendment protects expectations of privacy in movable, closed containers.  United States v. Ross, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#811" aria-description="Citation for case: United States v. Ross">456 U.S. 798, 811</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#2165" aria-description="Citation for case: United States v. Ross">102 S.Ct. 2157, 2165</a></span>, <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">72 L.Ed.2d 572</a></span> (1982);  United States v. Chadwick, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#13" aria-description="Citation for case: United States v. Chadwick">433 U.S. 1, 13</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#2484" aria-description="Citation for case: United States v. Chadwick">97 S.Ct. 2476, 2484</a></span>, <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/" aria-description="Citation for case: United States v. Chadwick">53 L.Ed.2d 538</a></span> (1977).  See also Pottinger v. City of Miami, <span class="citation" data-id="1500109"><a href="/opinion/1500109/pottinger-v-city-of-miami/" aria-description="Citation for case: Pottinger v. City of Miami">810 F.Supp. 1551</a></span> (S.D.Fla.1992) (person has reasonable expectation of privacy in belongings and personal effects in public area);  State v. Mooney, <span class="citation" data-id="7841712"><a href="/opinion/7894385/state-v-mooney/" aria-description="Citation for case: State v. Mooney">218 Conn. 85</a></span>, <span class="citation" data-id="7841712"><a href="/opinion/7894385/state-v-mooney/" aria-description="Citation for case: State v. Mooney">588 A.2d 145</a></span> (same), cert. denied, --- U.S. ----, <span class="citation multiple-matches"><a href="/c/S.Ct./112/330/">112 S.Ct. 330</a></span>, <span class="citation" data-id="9108589"><a href="/opinion/9114090/grumman-aerospace-corp-v-united-states/" aria-description="Citation for case: Grumman Aerospace Corp. v. United States">116 L.Ed.2d 270</a></span> (1991).  Besides, the reduced expectation of privacy in a vehicle is due in large part to the fact that there is "pervasive" government regulation of vehicles.  Carney, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#392" aria-description="Citation for case: California v. Carney">471 U.S. at 392</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#2069" aria-description="Citation for case: California v. Carney">105 S.Ct. at 2069</a></span> ("These reduced expectations of privacy derive not from the fact that the area to be searched is in plain view, but from the pervasive regulation of vehicles capable of traveling on the public highways.");  South Dakota v. Opperman, <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#368" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. 364, 368</a></span>, <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/#3096" aria-description="Citation for case: South Dakota v. Opperman">96 S.Ct. 3092, 3096</a></span>, <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">49 L.Ed.2d 1000</a></span> (1976).  Finally, even the automobile exception applies only when a vehicle is on the open road or is capable of movement and is "in a place not regularly used for residential purposes--temporary or otherwise."  Carney, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#392" aria-description="Citation for case: California v. Carney">471 U.S. at 392</a></span>, <span class="citation" data-id="9430011"><a href="/opinion/111423/california-v-carney/#2070" aria-description="Citation for case: California v. Carney">105 S.Ct. at 2070</a></span>.   The district court did not err in concluding a tent is more like a house than a car.  We hold that Gooch had a reasonable expectation of privacy such that the warrantless search of his tent violated the Fourth Amendment.</p>
    </div>
    <p>IV</p>
    <div class="num" id="p11">
      <span class="num">11</span>
      <p class="indent">The district court held the police were required to obtain an arrest warrant, so the warrantless arrest was unconstitutional.  No warrant is required to arrest a suspected felon in a public place.  United States v. Watson, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U.S. 411</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">96 S.Ct. 820</a></span>, <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">46 L.Ed.2d 598</a></span> (1976).  Absent exigent circumstances, a warrantless arrest is unconstitutional in a "non-public" place, even when that place is not one's residence.<a class="footnote" href="#fn2" id="fn2_ref">2</a>  United States v. Alvarez, <span class="citation" data-id="8947287"><a href="/opinion/8956260/united-states-v-alvarez/#881" aria-description="Citation for case: United States v. Alvarez">810 F.2d 879, 881</a></span> (9th Cir.1987);  Minnesota v. Olson, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">495 U.S. 91</a></span>, 96 n. 5, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">110 S.Ct. 1684</a></span>, 1688 n. 5, <span class="citation" data-id="9431979"><a href="/opinion/112416/minnesota-v-olson/" aria-description="Citation for case: Minnesota v. Olson">109 L.Ed.2d 85</a></span> (1990).  See United States v. Ruckman, <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1475" aria-description="Citation for case: United States v. Frank William Ruckman">806 F.2d 1471, 1475-76</a></span> (10th Cir.1986) (McKay, J., dissenting) (suggesting that inhabitant of cave on public property has an objectively reasonable expectation of privacy therein even if the cave is not considered a house).</p>
    </div>
    <div class="num" id="p12">
      <span class="num">12</span>
      <p class="indent">We have not yet settled whether a tent is a "non-public" place for arrest warrant purposes.  In United States v. Rigsby, <span class="citation" data-id="567665"><a href="/opinion/567665/united-states-v-wendell-b-rigsby/" aria-description="Citation for case: United States v. Wendell B. Rigsby">943 F.2d 631</a></span> (6th Cir.1991), cert. denied, --- U.S. ----, <span class="citation multiple-matches"><a href="/c/S.Ct./112/1269/">112 S.Ct. 1269</a></span>, <span class="citation no-link">117 L.Ed.2d 496</span> (1992), the Sixth Circuit addressed whether an officer who pulled back the unzipped flap of an unoccupied tent and saw a shotgun inside was required to obtain a search warrant.  The court concluded that no search warrant was necessary.  In that case, "there was no indication that the tent was like a 'home' or even a temporary habitation."  Id. at 636.   The court explicitly reserved judgment on the defendant's privacy interest in the tent.  Id. at 636-37 ("This is not to say that defendant had no privacy interest in the tent itself, but merely that the presence of the tent, in which no one was apparently residing, did not create a privacy interest in the otherwise non-private area surrounding it.").</p>
    </div>
    <div class="num" id="p13">
      <span class="num">13</span>
      <p class="indent">The court in People v. Livermore, <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/" aria-description="Citation for case: People v. Livermore">9 Mich.App. 47</a></span>, <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/#714" aria-description="Citation for case: People v. Livermore">155 N.W.2d 711, 714</a></span> (1967), addressed whether police could enter a tent in a public campground and arrest the occupants.  The court analyzed the case as one involving a "dwelling house" but upheld the arrest because under Michigan law the officers were justified in making a warrantless arrest in a dwelling house.  The court relied on a case involving police entry into a house to support its conclusion that the police entry was justified.  <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/" aria-description="Citation for case: People v. Livermore">Id.</a></span></p>
    </div>
    <div class="num" id="p14">
      <span class="num">14</span>
      <p class="indent">The defendant in Livermore also raised the issue whether the tent was a "public" or "private" place, arguing that the information required proof that the crime occurred in a public place.  The state trial court assumed "[f]or the purposes of argument" that the tent was "the equivalent of a private residence notwithstanding its location in a public park," but, like the appellate court, decided the case on other grounds.  <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/" aria-description="Citation for case: People v. Livermore">Id.</a></span> <span class="citation" data-id="1245135"><a href="/opinion/1245135/people-v-livermore/#715" aria-description="Citation for case: People v. Livermore">155 N.W.2d at 715</a></span>.</p>
    </div>
    <div class="num" id="p15">
      <span class="num">15</span>
      <p class="indent">Though Gooch's tent was pitched on public property, we hold that the closed tent was a "non-public" place for purposes of Fourth Amendment analysis.  We have recognized that, despite the special status afforded a residence under the Fourth Amendment, "an individual's privacy interests may be implicated in a variety of other settings."  United States v. Driver, <span class="citation" data-id="460378"><a href="/opinion/460378/united-states-v-samuel-clinton-driver-and-panom-driver/#809" aria-description="Citation for case: United States v. Samuel Clinton Driver and Panom Driver">776 F.2d 807, 809</a></span> (9th Cir.1985).  By establishing a campground, the state created a situation where campers were invited to come to set up a tent.  The campers could reasonably assert a legitimate, though temporary, interest in their privacy even in this short-term "dwelling."   A guest in Yellowstone Lodge, a hotel on government park land, would have no less reasonable an expectation of privacy in his hotel room than a guest in a private hotel, and the same logic would extend to a campsite where the opportunity is extended to spend the night.  See Stoner v. California, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#490" aria-description="Citation for case: Stoner v. California">376 U.S. 483, 490</a></span>, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#893" aria-description="Citation for case: Stoner v. California">84 S.Ct. 889, 893</a></span>, <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">11 L.Ed.2d 856</a></span> (1964) (hotel guest has Fourth Amendment protections).  See also Eng Fung Jem v. United States, <span class="citation" data-id="251769"><a href="/opinion/251769/eng-fung-jem-v-united-states/#805" aria-description="Citation for case: Eng Fung Jem v. United States">281 F.2d 803, 805</a></span> (9th Cir.1960) ("The transience of appellant's stay in the [hotel] room searched by the officers does not dilute the force of constitutional protection.  The hotel room in question was appellant's dwelling.  That he lived there for but several days is of no consequence....  The right to privacy must be accorded with equal vigor both to transient hotel guests and to occupants of private, permanent dwellings.").</p>
    </div>
    <div class="num" id="p16">
      <span class="num">16</span>
      <p class="indent">For the first time on appeal, the government argues that Gooch's use of the campground was wrongful because state law prohibited using the campground primarily for residence purposes.  We do not address that argument, as "[i]ssues not presented to the trial court cannot generally be raised for the first time on appeal."  United States v. Flores-Payon, <span class="citation" data-id="566881"><a href="/opinion/566881/united-states-v-miguel-angel-flores-payon/#558" aria-description="Citation for case: United States v. Miguel Angel Flores-Payon">942 F.2d 556, 558</a></span> (9th Cir.1991).  Though we can review pure issues of law which were not raised before the district court, <span class="citation" data-id="566881"><a href="/opinion/566881/united-states-v-miguel-angel-flores-payon/" aria-description="Citation for case: United States v. Miguel Angel Flores-Payon">id.,</a></span> it is not clear from the record, as a matter of law, that Gooch was wrongfully camping at the campground despite the fact that Gooch had no other legal residence.  See Ruckman, <span class="citation" data-id="9475634"><a href="/opinion/480405/united-states-v-frank-william-ruckman/#1476" aria-description="Citation for case: United States v. Frank William Ruckman">806 F.2d at 1476</a></span> (McKay, J., dissenting).</p>
    </div>
    <div class="num" id="p17">
      <span class="num">17</span>
      <p class="indent">We hold that Gooch's warrantless arrest in his tent violated the proscription of the Fourth Amendment, absent exigent circumstances.</p>
    </div>
    <p>V</p>
    <div class="num" id="p18">
      <span class="num">18</span>
      <p class="indent">We review de novo whether exigent circumstances justify a warrantless arrest or seizure.  Echegoyen, <span class="citation" data-id="475484"><a href="/opinion/475484/united-states-v-rodolfo-echegoyen/#1277" aria-description="Citation for case: United States v. Rodolfo Echegoyen">799 F.2d at 1277-78</a></span>.   The district court's factual findings are reviewed for clear error.  <span class="citation" data-id="475484"><a href="/opinion/475484/united-states-v-rodolfo-echegoyen/#1277" aria-description="Citation for case: United States v. Rodolfo Echegoyen">Id. at 1277</a></span>.   The government has the "heavy burden," Alvarez, <span class="citation" data-id="8947287"><a href="/opinion/8956260/united-states-v-alvarez/#881" aria-description="Citation for case: United States v. Alvarez">810 F.2d at 881</a></span>, of showing that exigent circumstances "made the warrantless arrest imperative."  United States v. Al-Azzawy, <span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#894" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d 890, 894</a></span> (9th Cir.1985), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./476/1144/">476 U.S. 1144</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./106/2255/">106 S.Ct. 2255</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/90/700/">90 L.Ed.2d 700</a></span> (1986).</p>
    </div>
    <div class="num" id="p19">
      <span class="num">19</span>
      <p class="indent">Exigent circumstances are " 'those in which a substantial risk of harm to the persons involved or to the law enforcement process would arise if the police were to delay a search [or arrest] until a warrant could be obtained.' "  Id. (citation omitted) (brackets in original).  Exigent circumstances are present when "a reasonable person [would] believe that entry ... was necessary to prevent physical harm to the officers or other persons, the destruction of relevant evidence, the escape of the suspect, or some other consequence improperly frustrating legitimate law enforcement efforts."  United States v. McConney, <span class="citation" data-id="9471865"><a href="/opinion/431931/united-states-v-winston-bryant-mcconney/#1199" aria-description="Citation for case: United States v. Winston Bryant McConney">728 F.2d 1195, 1199</a></span> (9th Cir.)  (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./469/824/">469 U.S. 824</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/101/">105 S.Ct. 101</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/83/46/">83 L.Ed.2d 46</a></span> (1984).</p>
    </div>
    <div class="num" id="p20">
      <span class="num">20</span>
      <p class="indent">* The exigencies cited by the government in justifying the arrest in this case were the risk that evidence would be destroyed and the potential danger to the officers and other campers.<a class="footnote" href="#fn3" id="fn3_ref">3</a>  As the district court observed, there was "no independent indication" that the firearm would be destroyed, nor could it even be removed from the tent with the officers present.</p>
    </div>
    <div class="num" id="p21">
      <span class="num">21</span>
      <p class="indent">The district court found the risk of harm to the officers and others to present a closer issue.  The facts that Gooch was intoxicated, that a firearm had been discharged recently, and that people were leaving the campground in fear supported the officers' conclusion that there was an immediate threat to public safety.  However, there was no actual ongoing threat.  The district court found that the campground appeared quiet when the officers arrived in the daylight hours.  The alleged fight and discharge of the firearm took place several hours before the arrest.  The district court did not err in concluding that the deputies could not have reasonably believed that there was a present danger to other occupants of the tent or to other campers.  Alvarez, <span class="citation" data-id="8947287"><a href="/opinion/8956260/united-states-v-alvarez/#883" aria-description="Citation for case: United States v. Alvarez">810 F.2d at 883-84</a></span>.</p>
    </div>
    <div class="num" id="p22">
      <span class="num">22</span>
      <p class="indent">The government compares the circumstances here to those in Al-Azzawy.   In that case, we determined exigent circumstances existed on the sole basis that the police had been informed by a reliable person that the defendant possessed explosives.  Al-Azzawy, <span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#894" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 894</a></span>.   However, we expressly contrasted Al-Azzawy's circumstances with those addressed in United States v. Morgan, <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1161" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1161-1163</a></span> (6th Cir.1984), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985).  In Morgan, the court held that defendants' possession of automatic weapons did not give rise to exigent circumstances.</p>
    </div>
    <p>B</p>
    <div class="num" id="p23">
      <span class="num">23</span>
      <p class="indent">The search was also not justified by exigent circumstances, as the district court found:  "At the time of the search, the defendant was in custody, handcuffed, and locked in the back of a patrol car.  He was not a danger to anyone, and he was the only one that the deputies had any reasonable grounds to believe had violated the law, or who could possibly have been a threat to them."</p>
    </div>
    <div class="num" id="p24">
      <span class="num">24</span>
      <p class="indent">The government argues the officers needed to search the tent immediately because the firearm presented a potential danger to the children at the campsite.  The presence of a firearm alone is not an exigent circumstance.  Morgan, <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1167" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d at 1167</a></span>;  United States v. Gooch, <span class="citation" data-id="8693761"><a href="/opinion/8710575/united-states-v-gooch/#732" aria-description="Citation for case: United States v. Gooch">780 F.Supp. 725, 732</a></span> (E.D.Wash.1991).  The cases cited by the government involved circumstances where unsupervised children would be left inside the house with the weapon or explosives if the officer did not secure it.  Al-Azzawy, <span class="citation" data-id="465254"><a href="/opinion/465254/united-states-v-riad-abed-al-azzawy/#895" aria-description="Citation for case: United States v. Riad Abed Al-Azzawy">784 F.2d at 895</a></span>;  United States v. Antwine, <span class="citation" data-id="522259"><a href="/opinion/522259/united-states-v-james-edward-antwine/#1147" aria-description="Citation for case: United States v. James Edward Antwine">873 F.2d 1144, 1147</a></span> (8th Cir.1989);  United States v. Queen, <span class="citation" data-id="506240"><a href="/opinion/506240/united-states-v-ellery-queen/#353" aria-description="Citation for case: United States v. Ellery Queen">847 F.2d 346, 353</a></span> (7th Cir.1988).  In the instant case, no one remained in the tent at the time of the search.  It would not have been difficult to prevent children or anyone else from entering the tent until a warrant was obtained.  The government's argument logically would authorize any warrantless search where officers had reason to believe a firearm was involved.</p>
    </div>
    <div class="num" id="p25">
      <span class="num">25</span>
      <p class="indent">This was not a case in which one or two police officers were forced to react quickly in an inaccessible locale that could only be reached on foot for some distance.  The officers drove directly to the campground, only one mile off the main road, in two vehicles.  They parked just 20 yards from the tent.  Three officers were present to arrest Gooch, with another as backup.  There was no ongoing threat.  We hold that no exigent circumstances existed.</p>
    </div>
    <p>VI</p>
    <div class="num" id="p26">
      <span class="num">26</span>
      <p class="indent">The government finally contends the search falls into the "search incident to a lawful arrest" exception to the warrant requirement.  Chimel v. California, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U.S. 752</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">89 S.Ct. 2034</a></span>, <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">23 L.Ed.2d 685</a></span> (1969).  As the arrest was not lawful, we need not decide whether the warrantless search was a valid search incident to a lawful arrest.</p>
    </div>
    <p class="indent">The district court's judgment is</p>
    <div class="num" id="p27">
      <span class="num">27</span>
      <p class="indent">AFFIRMED.</p>
    </div>
    <p class="indent">ALARCON, Circuit Judge, dissenting:</p>
    <div class="num" id="p28">
      <span class="num">28</span>
      <p class="indent">The majority has decided that the district court did not err in concluding that the totality of the circumstances did not justify a warrantless entry and search of Gooch's tent based upon exigent circumstances requiring immediate action to protect the officers from harm.  I cannot join in their opinion because the district court erroneously found that the officers were told prior to the entry that Gooch was asleep.  The majority, while conceding that this finding was clearly erroneous, has failed to discuss the impact of this error regarding an essential fact on the district court's conclusion that there were no exigent circumstances.  Without a remand, this court cannot determine whether, when informed of its error, the district court would reverse its determination that there were no exigent circumstances, especially in light of the fact that it stated that the issue of exigent circumstances created a "difficult question" for the court.</p>
    </div>
    <p>I.</p>
    <div class="num" id="p29">
      <span class="num">29</span>
      <p class="indent">To appreciate the gravity of the district court's factual error, it is necessary to consider the totality of circumstances known to the officers.  At approximately 4:00 a.m. on July 29, 1990, Stevens County Sheriff's Deputies Ted Campbell and Ed Burns responded to a call from a man claiming to have been shot at the State of Washington Department of Natural Resources ("DNR") campground on Long Lake.  While proceeding to the campground, the deputies encountered an automobile.  The occupants of the car informed the deputies that Ken Gooch was "hurting people" at the DNR campground on Long Lake.  The occupants also indicated that shots had been fired, but did not inform the deputies that Gooch fired the shots.  While proceeding to the campground, the deputies encountered Marc Cole walking alongside the road.  Mr. Cole stated that Gooch fired shots in his direction after they engaged in a family dispute.  These events occurred between midnight and 2:00 a.m.</p>
    </div>
    <div class="num" id="p30">
      <span class="num">30</span>
      <p class="indent">Deputies Campbell and Burns arrived at the campground at around 5:00 a.m., where they were subsequently joined by Deputy Steve Bruchman and a reserve deputy.  Without a warrant, the deputies ordered Gooch from his tent.  Gooch was searched and placed under arrest.  After placing Gooch in a patrol car, the deputies ordered Mary Baker, Gooch's companion, from the tent.  Approximately fifteen minutes later, the deputies conducted a warrantless search of the tent and located a loaded handgun under a mattress.</p>
    </div>
    <p>II.</p>
    <div class="num" id="p31">
      <span class="num">31</span>
      <p class="indent">The district court found that upon arriving at the campground the deputies determined that Gooch was sleeping in his tent.  During oral argument, we requested that counsel for Gooch file a supplemental brief indicating the portion of the record that supported this finding.</p>
    </div>
    <div class="num" id="p32">
      <span class="num">32</span>
      <p class="indent">In his supplemental brief, Gooch asserts that the record shows that Sergeant Burns spoke with a pedestrian along the roadside on his way to the campground.  According to Gooch, the pedestrian informed Sergeant Burns that Gooch was sleeping in the tent he shared with his girlfriend.  Gooch acknowledges that Sergeant Burns did not testify, but explains that Deputies Campbell and Bruchman testified that Sergeant Burns had been informed that Gooch was asleep.  Counsel for Gooch has misrepresented the evidence produced in the trial court.  The record does not support the district court's finding that any of the officers were informed prior to the search that Gooch was asleep.</p>
    </div>
    <div class="num" id="p33">
      <span class="num">33</span>
      <p class="indent">I agree with the majority that the district court's finding was clearly erroneous.  After acknowledging the district court's error in footnote 1, the majority proceeds to make its own findings regarding whether exigent circumstances justified the search for the handgun without discussing whether the district court's clearly erroneous understanding of the facts caused it to grant the motion.  Therefore, I assume that the majority has made a finding that it didn't matter what the officers were told regarding whether Gooch was asleep.  This determination invades the province of the district court, which has the responsibility to determine factual matters.</p>
    </div>
    <p>III.</p>
    <div class="num" id="p34">
      <span class="num">34</span>
      <p class="indent">Rule 12(e) of the Federal Rules of Criminal Procedure, which governs motions to suppress, requires that "[w]here factual issues are involved in determining a motion, the [district] court shall state its essential findings on the record."   While Rule 12(e) does not address the precise issue presented here, i.e., what remedy is available to the Government when the district court has made a clearly erroneous finding on a material issue, clearly the drafters of Rule 12(e) assumed that the district court would make accurate factual determinations.  A contrary conclusion would impute to Congress an intent to enact an absurd rule.  We would be required to hold that Rule 12(e) is satisfied if findings are made by the trial court, regardless of the fact that there is no evidence in the record to support them.</p>
    </div>
    <div class="num" id="p35">
      <span class="num">35</span>
      <p class="indent">I would hold that if a reviewing court determines that the district court has made a clearly erroneous factual determination on a material issue, a remand is required for further factual findings that reflect on the true state of the record.  The district court must determine, in the first instance, whether the fact that the officers did not know whether Gooch was asleep before they ordered him out of the tent was a factor in persuading them that it was necessary to locate his firearm immediately to protect themselves and others at the campground from lethal force.</p>
    </div>
    <div class="num" id="p36">
      <span class="num">36</span>
      <p class="indent">My conclusion that this court cannot substitute itself for the trial court in weighing the effect of the true circumstances relied upon by the officers in believing that exigent circumstances required a warrantless search is supported by the Supreme Court's analysis in Murray v. United States, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">487 U.S. 533</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">108 S.Ct. 2529</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/" aria-description="Citation for case: Murray v. United States">101 L.Ed.2d 472</a></span> (1988).  In Murray, federal law enforcement agents conducted a warrantless entry into a Boston warehouse where they observed bales of marijuana.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#535" aria-description="Citation for case: Murray v. United States">Id. at 535</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2532" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2532</a></span>.   The agents placed the warehouse under surveillance and applied for a search warrant, without informing the magistrate of the initial entry or the marijuana they observed.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#535" aria-description="Citation for case: Murray v. United States">Id. at 535-36</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2532" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2532</a></span>.   At issue was whether the second search was truly independent from the initial warrantless search.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#542" aria-description="Citation for case: Murray v. United States">Id. at 542</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2535" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2535</a></span>.   The district court denied the motion and the appellate court affirmed, concluding that it was "absolutely certain that the warrantless entry in no way contributed in the slightest either to the issuance of a warrant or to the discovery of the evidence during the lawful search that occurred pursuant to the warrant."  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#542" aria-description="Citation for case: Murray v. United States">Id. at 542-43</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2536" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2536</a></span>.</p>
    </div>
    <div class="num" id="p37">
      <span class="num">37</span>
      <p class="indent">The Supreme Court determined that the record did not support the Court of Appeals' findings on the application of the independent source doctrine and remanded for further factual findings on the contested issue.  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#543" aria-description="Citation for case: Murray v. United States">Id. at 543-44</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2536" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2536</a></span>.   The Court concluded that "it is the function of the District Court rather than the Court of Appeals to determine the facts."  <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#543" aria-description="Citation for case: Murray v. United States">Id. at 543</a></span>, <span class="citation" data-id="9431434"><a href="/opinion/112136/murray-v-united-states/#2536" aria-description="Citation for case: Murray v. United States">108 S.Ct. at 2536</a></span>.   In a case such as this, where the district court has made erroneous factual findings, we may not substitute our judgment for that of the district court and make a factual finding that the totality of the circumstances did not establish exigent circumstances justifying the warrantless search of Gooch's tent and the seizure of his firearm.</p>
    </div>
    <div class="num" id="p38">
      <span class="num">38</span>
      <p class="indent">We have previously relied on Murray in determining that Rule 12(e) requires the district court to make essential findings of fact when ruling upon a motion to suppress.  See United States v. Prieto-Villa, <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/" aria-description="Citation for case: United States v. Pedro Prieto-Villa">910 F.2d 601</a></span> (9th Cir.1990).  In Prieto-Villa, the defendant was arrested while the police searched a co-defendant's apartment in the process of investigating a drug conspiracy.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#602" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 602</a></span>.   Prieto filed a pre-trial motion to suppress the introduction of cocaine and post-arrest statements made to the police.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#603" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 603</a></span>.   The district court denied his motion but failed to make sufficient factual findings to permit appellate review.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#605" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 605-06</a></span>.   We held that Rule 12(e) required the district court to make appropriate factual findings and remanded for the development of an adequate record.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#607" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 607</a></span>.   In determining that Rule 12(e) imposed a mandatory requirement on the district court, we cited Murray for the proposition that the district court, and not the appellate court, is responsible for making factual findings.  <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/#608" aria-description="Citation for case: United States v. Pedro Prieto-Villa">Id. at 608-610</a></span>.</p>
    </div>
    <div class="num" id="p39">
      <span class="num">39</span>
      <p class="indent">I believe it is particularly important that we remand this matter to the district court to rectify its unsupportive finding, because of the consequences of the district court's clear error.  We have previously noted that a suppression hearing is "often as important as the trial itself."  Prieto-Villa, <span class="citation" data-id="9480660"><a href="/opinion/546167/united-states-v-pedro-prieto-villa/" aria-description="Citation for case: United States v. Pedro Prieto-Villa">910 F.2d at 609</a></span> (quoting Waller v. Georgia, <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#46" aria-description="Citation for case: Waller v. Georgia">467 U.S. 39, 46</a></span>, <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#2215" aria-description="Citation for case: Waller v. Georgia">104 S.Ct. 2210, 2215</a></span>, <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/" aria-description="Citation for case: Waller v. Georgia">81 L.Ed.2d 31</a></span> (1984)).  This observation is particularly important in this case, as the Government has conceded that it would be unable to sustain its burden of proof in the absence of the physical evidence seized from Gooch's tent.  In light of the fact that the district court stated that whether the facts in this case demonstrated a "difficult question," the district court resolved that question against the Government based on an erroneous factual finding.  A remand is mandatory under the Supreme Court's decision in Murray, and the law of this circuit as explained in Prieto-Villa.</p>
    </div>
    <p>IV.</p>
    <div class="num" id="p40">
      <span class="num">40</span>
      <p class="indent">The Government has also raised serious questions concerning Gooch's alleged violations of numerous Washington state regulations prohibiting the use of campground property primarily for residential purposes.  The Government cites California v. Ciraolo, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">476 U.S. 207</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. 1809</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">90 L.Ed.2d 210</a></span> (1985) for the proposition that a person must have a legitimate expectation of privacy to invoke the protection of the Fourth Amendment.  <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">Id. at 211</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#1811" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. at 1811</a></span>.   If these regulations were indeed violated, Gooch may not be able to demonstrate that he had a legitimate expectation of privacy in his tent.  The Government, however, failed to raise this argument before the district court.  Under the law of this circuit, "[i]ssues not presented to the trial court cannot generally be raised for the first time on appeal."  United States v. Flores-Payon, <span class="citation" data-id="566881"><a href="/opinion/566881/united-states-v-miguel-angel-flores-payon/#558" aria-description="Citation for case: United States v. Miguel Angel Flores-Payon">942 F.2d 556, 558</a></span> (8th Cir.1991).  Because I believe the Supreme Court's decision in Murray requires that we remand this case to the district court, the question whether Gooch had a legitimate expectation of privacy in a tent used as a residence in violation of Washington law should be resolved in the district court.</p>
    </div>
    <div class="footnotes">
      <div class="footnote" id="fn1">
        <a class="footnote" href="#fn1_ref">1</a>
        <p> Although Gooch had either fallen asleep or passed out due to alcohol consumption, there is no evidence in the record that the officers knew that fact.  This finding of the district court is clearly erroneous</p>
      </div>
      <div class="footnote" id="fn2">
        <a class="footnote" href="#fn2_ref">2</a>
        <p> As it happens, Gooch's tent was his residence.  However, the police officers could not reasonably have been expected to realize that fact.  This opinion does not rely in any way on the fact that Gooch actually had no other residence</p>
      </div>
      <div class="footnote" id="fn3">
        <a class="footnote" href="#fn3_ref">3</a>
        <p> The government also noted that problems with radio communication in the southwest corner of the county would have made obtaining a warrant inconvenient.  "Police officers may not, in their zeal to arrest an individual, ignore the [F]ourth [A]mendment's warrant requirement merely because it is inconvenient."  United States v. Morgan, <span class="citation" data-id="9472619"><a href="/opinion/441786/united-states-v-john-henry-morgan/#1164" aria-description="Citation for case: United States v. John Henry Morgan">743 F.2d 1158, 1164</a></span> (6th Cir.1984), cert. denied, <span class="citation multiple-matches"><a href="/c/U.S./471/1061/">471 U.S. 1061</a></span>, <span class="citation multiple-matches"><a href="/c/S.Ct./105/2126/">105 S.Ct. 2126</a></span>, <span class="citation no-link">85 L.Ed.2d 490</span> (1985)</p>
      </div>
    </div>
    
```

---

## GROUP: _overhaul2/lake/cases/United States v. Gouveia.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "United States v. Gouveia"
type: case
citation: "467 U.S. 180 (1984)"
parallel_cite: "104 S. Ct. 2292; 81 L. Ed. 2d 146; 52 U.S.L.W. 4659"
neutral_cite: 1984 U.S. LEXIS 91
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-05-29
docket: 83-128
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Gouveia
  varies_by_point: false
  scope_note: "Good law; the attachment rule was reaffirmed in Rothgery v. Gillespie County (2008)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111193/united-states-v-gouveia/"
  cluster_id: 111193
  opinion_id: 9429629
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny"
related: ["[[Kirby v. Illinois]]", "[[Massiah v. United States]]", "[[Brewer v. Williams]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "attachment"]
holding: "The Sixth Amendment right to counsel attaches only at or after the initiation of adversary judicial proceedings (formal charge, preliminary hearing, indictment, information, or arraignment); inmates held in administrative segregation during a preindictment investigation have no Sixth Amendment right to counsel."
lake:
  record_id: United States v. Gouveia
  status: verified
  projected_at: 2026-07-09
---

# United States v. Gouveia

*467 U.S. 180 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gouveia and other federal prison inmates were suspected of a murder committed inside the prison and were placed in administrative detention (segregation) for months while the crime was investigated, before any indictment. They received no appointed counsel during that segregation. After indictment they were appointed counsel, tried, and convicted; the Ninth Circuit [[Reading and Citing Cases#en-banc|en banc]] held they had been entitled to counsel during the preindictment segregation.

## Issue
Whether prison inmates have a Sixth Amendment right to appointed counsel while held in administrative segregation during the investigation of a crime, before adversary judicial proceedings have begun.

## Rule
No. "[O]ur cases have long recognized that the right to counsel attaches only at or after the initiation of adversary judicial proceedings against the defendant." — 467 U.S. at 187. ^pin-187

Adopting the *[[Kirby v. Illinois|Kirby]]* formulation, the Court explained that the recognized points of attachment "have involved points of time at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment." — [467 U.S. at 188](https://www.courtlistener.com/opinion/111193/united-states-v-gouveia/#:~:text=have%20involved%20points%20of%20time) (quoting *Kirby v. Illinois*, 406 U.S. at 689). ^pin-188

The right is tied to the defendant's status as an "accused" facing the prosecutorial forces of the State, which arises only when the government has committed itself to prosecute.

## Application
During their preindictment administrative segregation the inmates were not yet "accused" within the meaning of the Sixth Amendment — no formal charge, indictment, or other adversary judicial proceeding had been initiated. The segregation served institutional security and investigative purposes, not the commencement of prosecution. They therefore had no Sixth Amendment right to counsel for that period, and the loss of any investigative advantage was not a Sixth Amendment injury.

## Conclusion
The Sixth Amendment right to counsel had not attached during preindictment segregation; the Ninth Circuit was reversed. Attachment requires the initiation of adversary judicial proceedings.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The attachment rule stated here is settled and was reaffirmed in *[[Rothgery v. Gillespie County]]* (2008). It marks the dividing line between the Fifth Amendment *[[Miranda v. Arizona|Miranda]]* world (custody) and the Sixth Amendment world (post-charge), and confines the pre-charge attachment suggested by [[Escobedo v. Illinois]].

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny*

## Sources
- *United States v. Gouveia*, 467 U.S. 180 (1984) — https://www.courtlistener.com/opinion/111193/united-states-v-gouveia/ — pinpoints: 187, 188.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9b0e9a34693a1998", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Gouveia"}, "payload": {"all": [{"cite": "467 U.S. 180", "page": "180", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "467"}, {"cite": "104 S. Ct. 2292", "page": "2292", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "81 L. Ed. 2d 146", "page": "146", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "81"}, {"cite": "1984 U.S. LEXIS 91", "page": "91", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 4659", "page": "4659", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "467 U.S. 180", "official": {"cite": "467 U.S. 180", "page": "180", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "467"}, "official_selection_present": true, "record_id": "United States v. Gouveia"}}
{"assertion_id": "09cc4aadd2097f93", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-187", "record_id": "United States v. Gouveia"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-187", "pinpoint_status": "slip-only", "quote": "--- # United States v. Gouveia *467 U.S. 180 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gouveia and other federal prison inmates were suspected of a murder committed inside the prison and were placed in administrative detention (segregation) for months while the crime was investigated, before any indictment. They received no appointed counsel during that segregation. After indictment they were appointed counsel, tried, and convicted; the Ninth Circuit en banc held they had been entitled to counsel during the preindictment segregation. ## Issue Whether prison inmates have a Sixth Amendment right to appointed counsel while held in administrative segregation during the investigation of a crime, before adversary judicial proceedings have begun. ## Rule No.", "quote_fidelity": "mismatch", "record_id": "United States v. Gouveia", "star_marker": null}}
{"assertion_id": "fd991a6a64e8f151", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-188", "record_id": "United States v. Gouveia"}, "payload": {"fragment": "#:~:text=have%20involved%20points%20of%20time", "page": null, "pin_id": "pin-188", "pinpoint_status": "star-verified", "quote": "have involved points of time at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.", "quote_fidelity": "matched", "record_id": "United States v. Gouveia", "star_marker": "188"}}
{"assertion_id": "9a7ce63a19553e43", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Gouveia"}, "payload": {"as_of_content": "1984-05-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Gouveia", "scope_note": "Good law; the attachment rule was reaffirmed in Rothgery v. Gillespie County (2008).", "varies_by_point": false}}
```

### lake record — United States v. Gouveia

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Gouveia",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Gouveia",
    "case_name_short": "Gouveia",
    "case_name_full": "UNITED STATES v. GOUVEIA Et Al.",
    "input_case_name": "United States v. Gouveia",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-05-29",
    "year": 1984,
    "docket": "83-128",
    "cluster_id": 111193,
    "lead_opinion_id": 9429629,
    "sibling_ids": [
      111193,
      9429629,
      9429630,
      9429631
    ],
    "absolute_url": "/opinion/111193/united-states-v-gouveia/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "467 U.S. 180",
      "volume": "467",
      "reporter": "U.S.",
      "page": "180",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2292",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 146",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4659",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4659",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 91",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "467 U.S. 180",
        "volume": "467",
        "reporter": "U.S.",
        "page": "180",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2292",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2292",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 L. Ed. 2d 146",
        "volume": "81",
        "reporter": "L. Ed. 2d",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 91",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "91",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4659",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4659",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "467 U.S. 180",
    "official_selection": {
      "court_class": "scotus",
      "selected": "467 U.S. 180",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-187",
      "page": null,
      "quote": "--- # United States v. Gouveia *467 U.S. 180 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gouveia and other federal prison inmates were suspected of a murder committed inside the prison and were placed in administrative detention (segregation) for months while the crime was investigated, before any indictment. They received no appointed counsel during that segregation. After indictment they were appointed counsel, tried, and convicted; the Ninth Circuit en banc held they had been entitled to counsel during the preindictment segregation. ## Issue Whether prison inmates have a Sixth Amendment right to appointed counsel while held in administrative segregation during the investigation of a crime, before adversary judicial proceedings have begun. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-188",
      "page": null,
      "quote": "have involved points of time at or after the initiation of adversary judicial criminal proceedings \u2014 whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.",
      "star_marker": "188",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15774,
      "fragment": "#:~:text=have%20involved%20points%20of%20time",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Gouveia",
    "varies_by_point": false,
    "scope_note": "Good law; the attachment rule was reaffirmed in Rothgery v. Gillespie County (2008).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Guillermo Hernandez Ruiz v. State of Iowa",
          "cluster_id": 4501180,
          "cite": [
            "912 N.W.2d 435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4348984,
          "cite": [
            "848 F.3d 767",
            "2017 FED App. 0034P",
            "2017 WL 603848",
            "2017 U.S. App. LEXIS 2629"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zackary Stewart v. Karl Wagner",
          "cluster_id": 4255669,
          "cite": [
            "836 F.3d 978",
            "2016 U.S. App. LEXIS 16642",
            "2016 WL 4728039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Neary-French",
          "cluster_id": 4247088,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Medunjanin",
          "cluster_id": 2675041,
          "cite": [
            "752 F.3d 576",
            "2014 U.S. App. LEXIS 9306",
            "2014 WL 2054016"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Patrick Henry Murphy v. State",
          "cluster_id": 3127894,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Earl Dangerfield v. State",
          "cluster_id": 3096392,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Flores v. State",
          "cluster_id": 1871985,
          "cite": [
            "299 S.W.3d 843",
            "2009 WL 3466009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burnette",
          "cluster_id": 2519721,
          "cite": [
            "535 F. Supp. 2d 772",
            "2007 WL 4911523"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Samuel Constanza Alvarado",
          "cluster_id": 793566,
          "cite": [
            "440 F.3d 191",
            "2006 U.S. App. LEXIS 6055",
            "2006 WL 598152"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane1_negative"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doggett v. United States",
          "cluster_id": 112780,
          "cite": [
            "120 L. Ed. 2d 520",
            "112 S. Ct. 2686",
            "505 U.S. 647",
            "1992 U.S. LEXIS 4362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Moulton",
          "cluster_id": 111546,
          "cite": [
            "88 L. Ed. 2d 481",
            "106 S. Ct. 477",
            "474 U.S. 159",
            "1985 U.S. LEXIS 147",
            "54 U.S.L.W. 4039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert L. Wilson v. Edward Murray, Director of the Virginia Department of Corrections",
          "cluster_id": 480360,
          "cite": [
            "806 F.2d 1232",
            "1986 U.S. App. LEXIS 34712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Loud Hawk",
          "cluster_id": 111554,
          "cite": [
            "88 L. Ed. 2d 640",
            "106 S. Ct. 648",
            "474 U.S. 302",
            "1986 U.S. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montejo v. Louisiana",
          "cluster_id": 145873,
          "cite": [
            "173 L. Ed. 2d 955",
            "129 S. Ct. 2079",
            "556 U.S. 778",
            "2009 U.S. LEXIS 3973"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guidry v. State",
          "cluster_id": 2342370,
          "cite": [
            "9 S.W.3d 133",
            "1999 Tex. Crim. App. LEXIS 145",
            "1999 WL 1144826"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ibarra v. State",
          "cluster_id": 1960811,
          "cite": [
            "11 S.W.3d 189",
            "1999 Tex. Crim. App. LEXIS 117",
            "1999 WL 956173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bomar",
          "cluster_id": 1989353,
          "cite": [
            "826 A.2d 831",
            "573 Pa. 426",
            "2003 Pa. LEXIS 920"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mickey",
          "cluster_id": 1226896,
          "cite": [
            "818 P.2d 84",
            "54 Cal. 3d 612",
            "286 Cal. Rptr. 801",
            "91 Daily Journal DAR 13544",
            "91 Cal. Daily Op. Serv. 8732",
            "1991 Cal. LEXIS 4664"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
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
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 1205096,
          "cite": [
            "842 P.2d 1",
            "3 Cal. 4th 1183",
            "14 Cal. Rptr. 2d 702",
            "92 Cal. Daily Op. Serv. 9582",
            "92 Daily Journal DAR 15971",
            "1992 Cal. LEXIS 5693"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie v. State",
          "cluster_id": 1706565,
          "cite": [
            "585 So. 2d 660",
            "1991 WL 142136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Conway",
          "cluster_id": 6894227,
          "cite": [
            "108 Ohio St. 3d 214"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Atwood",
          "cluster_id": 1182224,
          "cite": [
            "832 P.2d 593",
            "171 Ariz. 576"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Gouveia:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQxNzc2MDAwMDAwJnM9Njg5NDIyNyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111193+OR+9429629+OR+9429630+OR+9429631%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDAmcz0yMDQwMjgwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111193+OR+9429629+OR+9429630+OR+9429631%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631)",
        "reviewed": 15,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 15,
        "triage_read": 0,
        "triage_snippet_classified": 15
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111193 OR 9429629 OR 9429630 OR 9429631)",
    "indexed_citing_opinions": 721,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111193,
        "count": 650,
        "count_source": "search"
      },
      {
        "opinion_id": 9429629,
        "count": 93,
        "count_source": "search"
      },
      {
        "opinion_id": 9429630,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429631,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1099,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-gouveia.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4MTY2MyZzPTgyNDg5NzAmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28111193+OR+9429629+OR+9429630+OR+9429631%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111193,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 104637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 110829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 322550,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 338481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 363882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 387309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 413324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 416732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111193,
        "cited_id": 1236300,
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
    "date_created": "2026-07-06T00:11:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:15:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:11:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Gouveia

```
<opinion type="majority">
<author id="b240-5">Justice Rehnquist</author>
<p id="A7g">delivered the opinion of the Court.</p>
<p id="b240-6">Respondents William Gouveia, Robert Ramirez, Adolpho Reynoso, and Philip Segura were convicted of murdering a fellow inmate at a federal prison in Lompoc, Cal. Respondents Robert Mills and Richard Pierce were convicted of a later murder of another inmate at the same institution. Prison officials placed each respondent in administrative detention shortly after the murders, and they remained there for an extended period of time before they were eventually indicted on criminal charges. On appeal of respondents’ convictions, the en banc Court of Appeals for the Ninth Circuit held by divided vote that they had a Sixth Amendment right to an attorney during the period in which they were held in administrative detention before the return of indictments against them, and that because they had been denied that right, their convictions had to be overturned and their indictments dismissed. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d 1116</a></span> (1983). We granted cer-tiorari to review the Court of Appeals’ novel application of our Sixth Amendment precedents, <span class="citation multiple-matches"><a href="/c/U.%20S./464/913/">464 U. S. 913</a></span> (1983), and we now reverse.</p>
<p id="b240-7">On November 11, 1978, Thomas Trejo, an inmate at the Federal Correctional Institution in Lompoc, Cal., was found dead from 45 stab wounds in the chest. Prison officials and agents from the Federal Bureau of Investigation began inde<page-number citation-index="1" label="183">*183</page-number>pendent investigations of the murder. Prison officials immediately suspected respondents Reynoso and Gouveia and placed them in the Administrative Detention Unit (ADU) at Lompoc. They were released back into the general prison population on November 22, 1978, but after officials obtained further information about the murder, on December 4, 1978, they returned Reynoso and Gouveia to the ADU, and placed respondents Segura and Ramirez in the ADU as well. Later in December, prison officials held disciplinary hearings, determined that all four respondents had participated in the murder of inmate Trejo, and ordered their continued confinement in the ADU. While in the ADU, respondents were separated from the general prison population and confined to individual cells. Although their participation in various prison programs was curtailed, they were still allowed regular visitation rights, exercise periods, access to legal materials, and unmonitored phone calls. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1118" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1118</a></span>; see generally <span class="citation no-link">28 CFR §§541.19</span>, 541.20(d) (1983). Respondents remained in the ADU without appointed counsel for approximately 19 months. On June 17, 1980, a federal grand jury returned an indictment against respondents on charges of first-degree murder and conspiracy to commit murder in violation of <span class="citation no-link">18 U. S. C. §§1111</span> and 1117 respectively. On July 14, 1980, respondents were arraigned in federal court, at which time a Federal Magistrate appointed counsel for them.</p>
<p id="b241-5">Before trial respondents filed a motion to dismiss their indictments, arguing that the delay of approximately 19 months between the commission of the crime and the return of the indictments violated their due process rights under the Fifth Amendment or, alternatively, their Sixth Amendment right to a speedy trial, and that their confinement in the ADU without appointment of counsel during that period violated their Sixth Amendment right to counsel. The District Court for the Central District of California denied their motion, and respondents proceeded to trial. Their first trial, which lasted approximately four weeks, ended in a mistrial. On retrial, respondents were convicted on both counts and <page-number citation-index="1" label="184">*184</page-number>were sentenced to consecutive life and 99-year terms of imprisonment.</p>
<p id="b242-5">The scenario is much the same in the case of Mills and Pierce. Inmate Thomas Hall was stabbed to death at Lom-poc on August 22, 1979. Immediately afterwards Mills and Pierce were examined by a prison doctor and questioned by FBI agents regarding the murder. Prison officials suspected them of involvement in the murder and placed them in the ADU pending further investigation. On September 13, 1979, prison officials conducted a disciplinary hearing, concluded that respondents had murdered inmate Hall, and ordered their continued confinement in the ADU where they remained for the next eight months. On March 27, 1980, a federal grand jury returned an indictment against Mills and Pierce on charges of first-degree murder in violation of <span class="citation no-link">18 U. S. C. §1111</span> and of conveyance of a weapon in prison in violation of <span class="citation no-link">18 U. S. C. § 1792</span>, and against Pierce on a charge of assault in violation of <span class="citation no-link">18 U. S. C. § 113</span>(c). At the time of their arraignment on April 21, 1980, Mills and Pierce were appointed counsel and were released from the ADU.</p>
<p id="b242-6">Before trial Mills and Pierce also filed a motion to dismiss their indictments, alleging that the 8-month preindictment delay violated their Fifth Amendment due process rights and their Sixth Amendment speedy trial right, and that their confinement without counsel for that period violated their Sixth Amendment right to counsel. The District Court for the Central District of California granted the motion to dismiss. A panel of the Court of Appeals for the Ninth Circuit reversed and remanded for trial, holding that respondents’ Sixth Amendment rights were not triggered during their administrative segregation because they had not yet been arrested and accused, and that respondents had made an insufficient showing of actual prejudice from the preindictment delay so as to justify dismissal of the indictments on due process grounds. <em>United States </em>v. <em>Mills, </em><span class="citation" data-id="9467607"><a href="/opinion/387309/united-states-v-robert-eugene-mills-and-richard-raymond-pierce/" aria-description="Citation for case: United States v. Robert Eugene Mills and Richard Raymond...">641 F. 2d 785</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./454/902/">454 U. S. 902</a></span> (1981). Respondents Mills and <page-number citation-index="1" label="185">*185</page-number>Pierce were then convicted on all counts and sentenced to life imprisonment.</p>
<p id="b243-5">The Court of Appeals, proceeding en banc, consolidated the appeals of all six respondents and addressed only the issue of whether the Sixth Amendment requires the appointment of counsel before indictment for indigent inmates confined in administrative detention while being investigated for criminal activities. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1119" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1119</a></span>.<footnotemark>1</footnotemark> The Court of Appeals majority recognized that a plurality of this Court had concluded in <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span> (1972), that the Sixth Amendment right to counsel attaches only when formal judicial proceedings are initiated against an individual by way of indictment, information, arraignment, or preliminary hearing. The majority recognized that no such proceedings had been initiated against respondents during the period of time for which they asserted a right to appointed counsel in this case.</p>
<p id="b243-6">The majority went on to note, however, that <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span> </em>is not a prison case and that the point at which the Sixth Amendment right to counsel is triggered is different in the prosecution of prison crimes. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1120" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1120</a></span>. In so holding the majority analogized to Sixth Amendment speedy trial cases, where this Court has held that the Sixth Amendment speedy trial right is triggered when an individual is arrested and held to <page-number citation-index="1" label="186">*186</page-number>answer criminal charges. See <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#320" aria-description="Citation for case: United States v. Marion">404 U. S. 307, 320</a></span> (1971). The en banc majority reasoned that just as such an arrest constitutes an “accusation” for Sixth Amendment speedy trial purposes, the administrative detention of an inmate for more than 90 days because of a pending felony investigation constitutes an “accusation” for Sixth Amendment right to counsel purposes.<footnotemark>2</footnotemark> Thus, according to the Court of Appeals’ holding, an indigent inmate isolated in administrative detention while the subject of a felony investigation must be afforded counsel after 90 days, or else be released back into the prison population, in order to ensure that he or his lawyer will be able to take preindictment investigatory steps to preserve his defense at trial. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1124" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1124</a></span>.</p>
<p id="b244-5">Applying its test to the facts of this case, the Court of Appeals majority held that each respondent had been denied his Sixth Amendment right to counsel. It concluded that the record showed that each respondent had been held in administrative detention longer than 90 days, that each had been held at least in part because of a pending felony investigation,<footnotemark>3</footnotemark> and that each had requested and had been denied counsel during his confinement in the ADU. The majority went on to conclude that the appropriate remedy for redressing <page-number citation-index="1" label="187">*187</page-number>the Sixth Amendment violations in this case was reversal of respondents’ convictions and dismissal of the indictments against them.<footnotemark>4</footnotemark></p>
<p id="b245-5">Five judges dissented from the en banc majority’s Sixth Amendment holding. Relying on <em>Kirby </em>v. <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Illinois, supra,</a></span> </em>the dissent concluded that the Sixth Amendment right to counsel is triggered by the initiation of formal criminal proceedings even in the prison context, and that the majority’s conclusion to the contrary shows a misunderstanding of the purpose of the counsel guarantee. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1127" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1127-1129</a></span>. We agree with the dissenting judges’ application of our precedents to this situation, and, accordingly, we reverse the en banc majority’s holding that respondents had a Sixth Amendment right to the appointment of counsel during their preindictment segregation.</p>
<p id="b245-6">The Sixth Amendment guarantees that “[i]n all criminal prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel for his defence.” As the Court of Appeals majority noted, our cases have long recognized that the right to counsel attaches only at or after the initiation of adversary judicial proceedings against the defendant. In <em>Kirby </em>v. <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Illinois, supra,</a></span> </em>a plurality of the Court summarized our prior cases as follows:</p>
<blockquote id="b245-7">“In a line of constitutional cases in this Court stemming back to the Court’s landmark opinion in <em>Powell </em>v. <em>Alabama, </em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, it has been firmly established that a person’s Sixth and Fourteenth Amendment right to counsel attaches only at or after the time that adversary judicial proceedings have been initiated against him. See <em>Powell </em>v. <em><span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">Alabama, supra;</a></span> Johnson </em>v. <em>Zerbst, </em><page-number citation-index="1" label="188">*188</page-number><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span>; <em>Hamilton </em>v. <em>Alabama, </em><span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>; <em>White </em>v. <em>Maryland, </em><span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>; <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>; <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>; <em>Gilbert </em>v. <em>California, </em><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>; <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span>.</blockquote>
<blockquote id="ApI">. . [Wjhile members of the Court have differed as to the existence of the right to counsel in the contexts of some of the above cases, <em>all </em>of those cases have involved points of time at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.” <em>Id., </em>at 688-689 (emphasis in original).</blockquote>
<p id="b246-5">The view that the right to counsel does not attach until the initiation of adversary judicial proceedings has been confirmed by this Court in cases subsequent to <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>. </em>See <em>Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#469" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 469-470</a></span> (1981); <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#226" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220, 226-227</a></span> (1977); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#398" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 398-399</a></span> (1977); <em>United States </em>v. <em>Mandujano, </em><span class="citation" data-id="9426389"><a href="/opinion/109442/united-states-v-mandujano/#581" aria-description="Citation for case: United States v. Mandujano">425 U. S. 564, 581</a></span> (1976) (opinion of Burger, C. J.).<footnotemark>5</footnotemark></p>
<p id="b246-6">That interpretation of the Sixth Amendment right to counsel is consistent not only with the literal language of the Amendment, which requires the existence of both a “criminal prosecutio[n]” and an “accused,” but also with the purposes which we have recognized that the right to counsel serves. We have recognized that the “core purpose” of the counsel guarantee is to assure aid at trial, “when the accused [is] con<page-number citation-index="1" label="189">*189</page-number>fronted with both the intricacies of the law and the advocacy of the public prosecutor.” <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#309" aria-description="Citation for case: United States v. Ash">413 U. S. 300, 309</a></span> (1973). Indeed the right to counsel</p>
<blockquote id="b247-4">“embodies a realistic recognition of the obvious truth that the average defendant does not have the professional legal skill to protect himself when brought before a tribunal with power to take his life or liberty, wherein the prosecution is presented by experienced and learned counsel.” <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#462" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 462-463</a></span> (1938).</blockquote>
<p id="b247-5">Although we have extended an accused’s right to counsel to certain “critical” pretrial proceedings, <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), we have done so recognizing that at those proceedings, “the accused [is] confronted, just as at trial, by the procedural system, or by his expert adversary, or by both,” <em>United States </em>v. <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#310" aria-description="Citation for case: United States v. Ash"><em>Ash, supra, </em>at 310</a></span>, in a situation where the results of the confrontation “might well settle the accused’s fate and reduce the trial itself to a mere formality.” <em>United States </em>v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#224" aria-description="Citation for case: United States v. Wade"><em>Wade, supra, </em>at 224</a></span>.</p>
<p id="b247-6">Thus, given the plain language of the Amendment and its purpose of protecting the unaided layman at critical confrontations with his adversary, our conclusion that the right to counsel attaches at the initiation of adversary judicial criminal proceedings “is far from a mere formalism.” <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>. It is only at that time “that the government has committed itself to prosecute, and only then that the adverse positions of government and defendant have solidified. It is then that a defendant finds himself faced with the prosecutorial forces of organized society, and immersed in the intricacies of substantive and procedural criminal law.” <em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Ibid.</a></span></em></p>
<p id="b247-7">The Court of Appeals departed from our consistent interpretation of the Sixth Amendment in these cases, and in so doing, fundamentally misconceived the nature of the right to counsel guarantee. We agree with the dissent that the ma<page-number citation-index="1" label="190">*190</page-number>jority’s analogy to Sixth Amendment speedy trial cases is inapt. Our speedy trial cases hold that that Sixth Amendment right may attach before an indictment and as early as the time of “arrest and holding to answer a criminal charge,” <em>United States </em>v. <em>MacDonald, </em><span class="citation" data-id="9428723"><a href="/opinion/110686/united-states-v-macdonald/#6" aria-description="Citation for case: United States v. MacDonald">456 U. S. 1, 6-7</a></span> (1982); <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#788" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 788-789</a></span> (1977); <em>Dillingham </em>v. <em>United States, </em><span class="citation" data-id="109331"><a href="/opinion/109331/dillingham-v-united-states/" aria-description="Citation for case: Dillingham v. United States">423 U. S. 64</a></span> (1975) <em>(per curiam); United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#320" aria-description="Citation for case: United States v. Marion">404 U. S., at 320</a></span>, but we have never held that the right to counsel attaches at the time of arrest. This difference is readily explainable, given the fact that the speedy trial right and the right to counsel protect different interests. While the right to counsel exists to protect the accused during trial-type confrontations with the prosecutor, the speedy trial right exists primarily to protect an individual’s liberty interest, “to minimize the possibility of lengthy incarceration prior to trial, to reduce the lesser, but nevertheless substantial, impairment of liberty imposed on an accused while released on bail, and to shorten the disruption of life caused by arrest and the presence of unresolved criminal charges.” <em>United States </em>v. <span class="citation" data-id="9428723"><a href="/opinion/110686/united-states-v-macdonald/#8" aria-description="Citation for case: United States v. MacDonald"><em>MacDonald, supra, </em>at 8</a></span>. See <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/#532" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514, 532-533</a></span> (1972); <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#320" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 320</a></span>. Thus, the majority’s attempt to draw an analogy between an arrest and an inmate’s administrative detention pending investigation may have some relevance in analyzing when the speedy trial right attaches in this context, but it is not relevant to a proper determination of when the right to counsel attaches.<footnotemark>6</footnotemark></p>
<p id="b249-4"><page-number citation-index="1" label="191">*191</page-number>The Court of Appeals’ holding also confuses the purpose of the right to counsel with purposes that are served by the Fifth Amendment due process guarantee and the statutes of limitations applicable to the particular crime being investigated. The majority concludes that the extension of the right to counsel to this prison context is necessary to protect against the possibility that the Government may delay the initiation of formal charges, thus delaying the appointment of counsel, while it develops its case against the isolated and unaided inmate. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1122" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1122</a></span>. By the time the Government decides to bring charges, the majority felt, witnesses’ memories could have dimmed, alibi witnesses could have been transferred to other facilities, and physical evidence could have deteriorated. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1126" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip..."><em>Id., </em>at 1126</a></span>.</p>
<p id="b249-5">Those concerns, while certainly legitimate ones, are simply not concerns implicating the right to counsel, and we reaffirm that the mere “possibility of prejudice [to a defendant resulting from the passage of time] ... is not itself sufficient reason to wrench the Sixth Amendment from its proper context.” <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#321" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 321-322</a></span>. In holding that the appointment of counsel or the release of the inmate from segregation could remedy its concerns, the Court of Appeals must have concluded, quite illogically we believe, that the presence of the inmate in the general prison population or the appointment of a lawyer could somehow prevent the deterioration of physical evidence, or that the inmate or his counsel could begin an effective investigation of the crime within the restricted prison walls before even being able to discover the nature of the Government’s case. Of course, both inside and outside the prison, it may well be true that in some cases preindictment investigation could help a defendant prepare a better defense. But, as we have noted, our cases have never suggested that the purpose of the right to counsel is to provide a defendant with a preindictment private investigator, and we see no reason to adopt that novel interpretation of the right to counsel in this case.</p>
<p id="b250-4"><page-number citation-index="1" label="192">*192</page-number>Thus, at bottom, the majority’s concern is that because an inmáte suspected of a crime is already in prison, the prosecution may have little incentive promptly to bring formal charges against him, and that the resulting preindictment delay may be particularly prejudicial to the inmate, given the problems inherent in investigating prison crimes, such as the transient nature of the prison population and the general reluctance of inmates to cooperate. But applicable statutes of limitations protect against the prosecution’s bringing stale criminal charges against any defendant, <em>United States </em>v. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#788" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em>at 788-789</a></span>; <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#322" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 322</a></span>, and, beyond that protection, the Fifth Amendment requires the dismissal of an indictment, even if it is brought within the statute of limitations, if the defendant can prove that the Government’s delay in bringing the indictment was a deliberate device to gain an advantage over him and that it caused him actual prejudice in presenting his defense. <em>United States </em>v. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#789" aria-description="Citation for case: United States v. Lovasco"><em>Lovasco, supra, </em>at 789-790</a></span>; <em>United States </em>v. <span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#324" aria-description="Citation for case: United States v. Marion"><em>Marion, supra, </em>at 324</a></span>.<footnotemark>7</footnotemark> Those protections apply to criminal defendants within and without the prison walls, and we decline to depart from our traditional interpretation of the Sixth Amendment right to counsel in order to provide additional protections for respondents here.</p>
<p id="b250-5">We conclude that the Court of Appeals was wrong in holding that respondents were constitutionally entitled to the appointment of counsel while they were in administrative segregation and before any adversary judicial proceedings had been initiated against them. Accordingly, we reverse <page-number citation-index="1" label="193">*193</page-number>the judgment of the Court of Appeals and remand for further proceedings consistent with this opinion.</p>
<p id="b251-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b243-7"> The narrow issue before the Court of Appeals and before us today is whether the Sixth Amendment requires the appointment of counsel for indigent inmates in respondents’ situation. Respondents have not contended that they were denied the opportunity to retain their own private counsel while they were in administrative segregation. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1119" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1119</a></span>. As the Court of Appeals noted, respondents had visitation privileges and the opportunity to make unmonitored phone calls to attorneys while in the ADU. <em><span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">Ibid.</a></span> </em>See <span class="citation no-link">28 CFR §§ 541.19</span>(c)(10), 541.20(d) (1983). Respondents also have not asserted a Sixth Amendment ineffective-assistance-of-counsel claim nor have they questioned our holding in <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#570" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 570</a></span> (1974), that inmates have no right to retained or appointed counsel at prison disciplinary proceedings. See <em>Baxter </em>v. <em>Palmigiano, </em><span class="citation" data-id="9426363"><a href="/opinion/109429/baxter-v-palmigiano/#315" aria-description="Citation for case: Baxter v. Palmigiano">425 U. S. 308, 315</a></span> (1976).</p>
</footnote>
<footnote label="2">
<p id="b244-6"> The majority arrived at the 90-day figure based on its own interpretation of the current federal prison regulations as allowing detention for up to 90 days for disciplinary reasons. See <span class="citation no-link">28 CFR § 641.20</span>(c) (1983).</p>
</footnote>
<footnote label="3">
<p id="b244-7"> Relying on his interpretation of current prison regulations, the Solicitor General vehemently argues that, whatever additional reasons legitimately may have contributed to the decision to confine respondents in the ADU, the primary reason for their confinement was to ensure the security of the institution. Thus he argues that that security-related detention cannot be equated with an arrest or accusation for Sixth Amendment purposes. Brief for United States 23-27; Tr. of Oral Arg. 9-12. But our holding today makes the reason for the detention irrelevant for purposes of the only issue before us, the point at which the Sixth Amendment right to counsel is triggered. Respondents have not challenged “the legitimacy of administrative detention in general or its appropriateness” in their particular cases. <span class="citation" data-id="9470530"><a href="/opinion/416732/united-states-v-william-gouveia-robert-ramirez-philip-segura-adolpho/#1121" aria-description="Citation for case: United States v. William Gouveia, Robert Ramirez, Philip...">704 F. 2d, at 1121</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b245-8"> The Solicitor General argues here that dismissal of the indictments is an inappropriate remedy absent a showing of actual and specific prejudice to respondents and that they have not made that showing in this case. Brief for United States 44-60. Given our holding on the substantive Sixth Amendment issue, however, we have no occasion to address the remedy question.</p>
</footnote>
<footnote label="5">
<p id="b246-7"> The only arguable deviations from that consistent line of cases are <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964). Although there may be some language to the contrary in <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), we have made clear that we required counsel in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and <em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">Escobedo</a></span> </em>in order to protect the Fifth Amendment privilege against self-incrimination rather than to vindicate the Sixth Amendment right to counsel. See <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300, n. 4</a></span> (1980); <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S., at 689</a></span>; <em>Johnson </em>v. <em>New Jersey, </em><span class="citation multiple-matches"><a href="/c/U.%20S./384/719/">384 U. S. 719</a></span>, 729-730 (1966).</p>
</footnote>
<footnote label="6">
<p id="b248-5"> Of course we express no view as to when the Sixth Amendment speedy-trial right attaches in this context because that issue is not before us. The Court of Appeals for the Ninth Circuit, like several other Circuits, see, <em>e. g., United States </em>v. <em>Daniels, </em><span class="citation no-link">698 P. 2d 221</span>, 223 (CA4 1983); <em>United States </em>v. <em>Blevins, </em><span class="citation" data-id="363882"><a href="/opinion/363882/united-states-v-ralph-blevins/#647" aria-description="Citation for case: United States v. Ralph Blevins">593 F. 2d 646, 647</a></span> (CA5 1979) <em>(per curiam), </em>however, has held that the segregation of an inmate from the general population pending criminal charges does not constitute an “arrest” for purposes of the speedy trial right. <em>United States </em>v. <em>Clardy, </em><span class="citation" data-id="338481"><a href="/opinion/338481/united-states-v-harry-clardy-united-states-of-america-v-phillip-alfonso/#441" aria-description="Citation for case: United States v. Harry Clardy, United States of America...">540 F. 2d 439, 441</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/963/">429 U. S. 963</a></span> (1976). Given its own <em><span class="citation" data-id="338481"><a href="/opinion/338481/united-states-v-harry-clardy-united-states-of-america-v-phillip-alfonso/" aria-description="Citation for case: United States v. Harry Clardy, United States of America...">Clardy</a></span> </em>holding, the Court of Appeals’ analogy here seems somewhat strained.</p>
</footnote>
<footnote label="7">
<p id="b250-6"> We have of course rejected the arguments that prosecutors are constitutionally obligated to file charges against a suspect as soon as they have probable cause but before they believe that they can establish guilt beyond a reasonable doubt, <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#791" aria-description="Citation for case: United States v. Lovasco">431 U. S., at 791</a></span>, and that prosecutors must file charges as soon as they marshal enough evidence to prove guilt beyond a reasonable doubt but before their investigations are complete. <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#792" aria-description="Citation for case: United States v. Lovasco"><em>Id., </em>at 792-795</a></span>.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Grubbs.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "United States v. Grubbs"
type: case
citation: "547 U.S. 90 (2006)"
parallel_cite: "126 S. Ct. 1494; 164 L. Ed. 2d 195"
neutral_cite: 2006 U.S. LEXIS 2496
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-03-21
docket: 04-1414
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Grubbs
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/"
  cluster_id: 145670
  opinion_id: 145670
  identity_checked: true
homes:
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Gates]]", "[[Groh v. Ramirez]]", "[[Massachusetts v. Sheppard]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "anticipatory-warrant", "triggering-condition", "particularity"]
holding: "**Anticipatory warrants** — warrants that take effect only upon a future 'triggering condition' — are not categorically…"
lake:
  record_id: United States v. Grubbs
  status: verified
  projected_at: 2026-07-09
---

# United States v. Grubbs

*547 U.S. 90 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Jeffrey Grubbs bought a child-pornography videotape from a website run by an undercover postal inspector. Officers arranged a controlled delivery to his home and obtained a search warrant supported by an affidavit stating the warrant would be executed only after the package was "received by a person(s) and has been physically taken into the residence." The package was delivered, Grubbs' wife took it inside, and officers executed the warrant. The Ninth Circuit invalidated the warrant because the triggering condition appeared only in the affidavit, not on the face of the warrant.

## Issue
(1) Whether anticipatory search warrants are categorically unconstitutional under the Fourth Amendment's probable-cause requirement; and (2) whether the Fourth Amendment requires the triggering condition to be set forth in the warrant itself.

## Rule
No to both. An anticipatory warrant — one "based upon an affidavit showing probable cause that at some future time (but not presently) certain evidence of crime will be located at a specified place" — is constitutional. "Anticipatory warrants are, therefore, no different in principle from ordinary warrants. They require the magistrate to determine (1) that it is *now probable* that (2) contraband, evidence of a crime, or a fugitive *will be* on the described premises (3) when the warrant is executed." — 547 U.S. at 96. ^pin-96

For a conditioned anticipatory warrant, "two prerequisites of probability must be satisfied": it must be probable both that the triggering condition will occur and that, if it does, the object of the search will be found at the place. — [*Id.* at 96–97](https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/#:~:text=two%20prerequisites%20of%20probability%20must). ^pin-96a

The triggering condition need not appear on the warrant: "Because the Fourth Amendment does not require that the triggering condition for an anticipatory search warrant be set forth in the warrant itself, the Court of Appeals erred in invalidating the warrant at issue here." — [*Id.* at 99](https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/#:~:text=Because%20the%20Fourth%20Amendment%20does). ^pin-99

## Application
On these facts the warrant was valid. The affidavit's triggering condition — controlled delivery and movement of the package into the residence — established that it was then probable both that the delivery would occur and that, once it did, the contraband would be in the home; the supporting probable cause therefore existed when the warrant issued. The Court rejected Grubbs' [[Particularity|particularity]] argument: the Fourth Amendment's [[Particularity|particularity]] requirement reaches only the place to be searched and the persons or things to be seized, and "does not include the conditions precedent to execution of the warrant." Because probable cause itself — "the quintessential 'precondition to the valid exercise of executive power'" — need not be recited on the warrant, neither must the triggering condition. The controlled delivery satisfied the condition, and the search was lawful.

## Conclusion
Anticipatory warrants are constitutional, and the triggering condition need not be stated on the warrant's face; the Ninth Circuit's judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative subsequent treatment identified. *Grubbs* applies the totality probable-cause standard of [[Illinois v. Gates]] to anticipatory warrants and distinguishes the [[Particularity|particularity]] defect of [[Groh v. Ramirez]] (which concerned the place/things-to-be-seized [[Particularity|particularity]] that the Fourth Amendment's text *does* require).

## Appears on
- [[Probable Cause in the Affidavit]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Grubbs*, 547 U.S. 90 (2006) — https://www.courtlistener.com/opinion/145670/united-states-v-grubbs/ — pinpoints: 96, 99.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "907448942ca83e22", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Grubbs"}, "payload": {"all": [{"cite": "547 U.S. 90", "page": "90", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "547"}, {"cite": "126 S. Ct. 1494", "page": "1494", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "126"}, {"cite": "164 L. Ed. 2d 195", "page": "195", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "164"}, {"cite": "2006 U.S. LEXIS 2496", "page": "2496", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2006"}], "display": "547 U.S. 90", "official": {"cite": "547 U.S. 90", "page": "90", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "547"}, "official_selection_present": true, "record_id": "United States v. Grubbs"}}
{"assertion_id": "9932e75d5d8fb320", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-96", "record_id": "United States v. Grubbs"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-96", "pinpoint_status": "slip-only", "quote": "The package was delivered, Grubbs' wife took it inside, and officers executed the warrant. The Ninth Circuit invalidated the warrant because the triggering condition appeared only in the affidavit, not on the face of the warrant. ## Issue (1) Whether anticipatory search warrants are categorically unconstitutional under the Fourth Amendment's probable-cause requirement; and (2) whether the Fourth Amendment requires the triggering condition to be set forth in the warrant itself. ## Rule No to both. An anticipatory warrant — one", "quote_fidelity": "mismatch", "record_id": "United States v. Grubbs", "star_marker": null}}
{"assertion_id": "b996aa2cccba52f6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-96a", "record_id": "United States v. Grubbs"}, "payload": {"fragment": "#:~:text=two%20prerequisites%20of%20probability%20must", "page": null, "pin_id": "pin-96a", "pinpoint_status": "slip-only", "quote": "two prerequisites of probability must be satisfied", "quote_fidelity": "matched", "record_id": "United States v. Grubbs", "star_marker": null}}
{"assertion_id": "c001c71f4c70f375", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-99", "record_id": "United States v. Grubbs"}, "payload": {"fragment": "#:~:text=Because%20the%20Fourth%20Amendment%20does", "page": null, "pin_id": "pin-99", "pinpoint_status": "slip-only", "quote": "Because the Fourth Amendment does not require that the triggering condition for an anticipatory search warrant be set forth in the warrant itself, the Court of Appeals erred in invalidating the warrant at issue here.", "quote_fidelity": "matched", "record_id": "United States v. Grubbs", "star_marker": null}}
{"assertion_id": "65eb60efb060c8c8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Grubbs"}, "payload": {"as_of_content": "2006-03-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Grubbs", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — United States v. Grubbs

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Grubbs",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Grubbs",
    "case_name_short": "Grubbs",
    "case_name_full": "United States v. Grubbs",
    "input_case_name": "United States v. Grubbs",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-03-21",
    "year": 2006,
    "docket": "04-1414",
    "cluster_id": 145670,
    "lead_opinion_id": 145670,
    "sibling_ids": [
      145670,
      9434968,
      9434969
    ],
    "absolute_url": "/opinion/145670/united-states-v-grubbs/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 90",
      "volume": "547",
      "reporter": "U.S.",
      "page": "90",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 1494",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1494",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 195",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "195",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 2496",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2496",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 90",
        "volume": "547",
        "reporter": "U.S.",
        "page": "90",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 1494",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1494",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 195",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "195",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 2496",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2496",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 90",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 90",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-96",
      "page": null,
      "quote": "The package was delivered, Grubbs' wife took it inside, and officers executed the warrant. The Ninth Circuit invalidated the warrant because the triggering condition appeared only in the affidavit, not on the face of the warrant. ## Issue (1) Whether anticipatory search warrants are categorically unconstitutional under the Fourth Amendment's probable-cause requirement; and (2) whether the Fourth Amendment requires the triggering condition to be set forth in the warrant itself. ## Rule No to both. An anticipatory warrant \u2014 one",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-96a",
      "page": null,
      "quote": "two prerequisites of probability must be satisfied",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 15892,
      "fragment": "#:~:text=two%20prerequisites%20of%20probability%20must",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-99",
      "page": null,
      "quote": "Because the Fourth Amendment does not require that the triggering condition for an anticipatory search warrant be set forth in the warrant itself, the Court of Appeals erred in invalidating the warrant at issue here.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 21470,
      "fragment": "#:~:text=Because%20the%20Fourth%20Amendment%20does",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Grubbs",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane1_negative"
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
        "journal_ref": "United States v. Grubbs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "381 Search Warrants Directed to Facebook, Inc. v. New York County Dist. Attorney's Off.",
          "cluster_id": 2818762,
          "cite": [
            "132 A.D.3d 11",
            "14 N.Y.S.3d 23"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane1_negative"
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
        "journal_ref": "United States v. Grubbs:lane1_negative"
      },
      {
        "citing_case": {
          "name": "David Evans v. Patrick Baker",
          "cluster_id": 813710,
          "cite": [
            "703 F.3d 636"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mink v. Knox",
          "cluster_id": 158328,
          "cite": [
            "613 F.3d 995",
            "38 Media L. Rep. (BNA) 1961",
            "2010 U.S. App. LEXIS 14684",
            "2010 WL 2802729"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kasten v. Saint-Gobain Performance Plastics Corp.",
          "cluster_id": 212970,
          "cite": [
            "179 L. Ed. 2d 379",
            "131 S. Ct. 1325",
            "563 U.S. 1",
            "2011 U.S. LEXIS 2417"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wallace",
          "cluster_id": 2303175,
          "cite": [
            "42 A.3d 1040",
            "615 Pa. 395",
            "2012 WL 1434885",
            "2012 Pa. LEXIS 981"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. Com.",
          "cluster_id": 1058401,
          "cite": [
            "670 S.E.2d 727",
            "277 Va. 171",
            "2009 Va. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip C. BAY, S/K/A Philip C. Bay v. COMMONWEALTH of Virginia",
          "cluster_id": 1061627,
          "cite": [
            "60 Va. App. 520",
            "729 S.E.2d 768",
            "2012 WL 3165070",
            "2012 Va. App. LEXIS 254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin McClain George Brandt, III Jason Davis",
          "cluster_id": 793976,
          "cite": [
            "444 F.3d 556",
            "2006 U.S. App. LEXIS 32292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hurwitz",
          "cluster_id": 2968341,
          "cite": [
            "459 F.3d 463",
            "2006 WL 2414056"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Unus v. Kane",
          "cluster_id": 1028751,
          "cite": [
            "565 F.3d 103",
            "2009 U.S. App. LEXIS 9955",
            "2009 WL 1219679"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sisson v. State",
          "cluster_id": 1443990,
          "cite": [
            "903 A.2d 288",
            "2006 Del. LEXIS 326",
            "2006 WL 1699480"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tracey",
          "cluster_id": 62,
          "cite": [
            "597 F.3d 140",
            "2010 U.S. App. LEXIS 4204",
            "2010 WL 681364"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jesus Angel Ramirez",
          "cluster_id": 4394389,
          "cite": [
            "895 N.W.2d 884",
            "2017 WL 2291388",
            "2017 Iowa Sup. LEXIS 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christopher George Storm",
          "cluster_id": 4405282,
          "cite": [
            "898 N.W.2d 140",
            "2017 WL 2822483",
            "2017 Iowa Sup. LEXIS 81"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Clark",
          "cluster_id": 206195,
          "cite": [
            "638 F.3d 89",
            "2011 U.S. App. LEXIS 4506",
            "2011 WL 781597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. SDI Future Health, Inc.",
          "cluster_id": 1459636,
          "cite": [
            "568 F.3d 684",
            "103 A.F.T.R.2d (RIA) 2436",
            "2009 U.S. App. LEXIS 13003",
            "2009 WL 1508763"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hurwitz",
          "cluster_id": 795366,
          "cite": [
            "459 F.3d 463",
            "2006 U.S. App. LEXIS 21425"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Keller",
          "cluster_id": 842342,
          "cite": [
            "739 N.W.2d 505",
            "479 Mich. 467"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scott",
          "cluster_id": 150069,
          "cite": [
            "610 F.3d 1009",
            "2010 U.S. App. LEXIS 13683",
            "2010 WL 2650709"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lyman Wagers",
          "cluster_id": 794753,
          "cite": [
            "452 F.3d 534",
            "2006 U.S. App. LEXIS 16070",
            "2006 WL 1735574"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rosa",
          "cluster_id": 178085,
          "cite": [
            "626 F.3d 56",
            "2010 U.S. App. LEXIS 22099",
            "2010 WL 4227428"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bowling v. Rector",
          "cluster_id": 172792,
          "cite": [
            "584 F.3d 956",
            "2009 U.S. App. LEXIS 23542",
            "2009 WL 3416342"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Penney",
          "cluster_id": 1188924,
          "cite": [
            "576 F.3d 297",
            "80 Fed. R. Serv. 590",
            "2009 U.S. App. LEXIS 17595",
            "2009 WL 2408721"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Spencer",
          "cluster_id": 187217,
          "cite": [
            "530 F.3d 1003",
            "382 U.S. App. D.C. 90",
            "2008 U.S. App. LEXIS 14713",
            "2008 WL 2697191"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 2281341,
          "cite": [
            "338 S.W.3d 725",
            "2011 Tex. App. LEXIS 4300",
            "2011 WL 1448147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Grubbs:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145670 OR 9434968 OR 9434969) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 178,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 178,
        "triage_read": 4,
        "triage_snippet_classified": 174
      },
      "lane2_top_cited": {
        "query": "cites:(145670 OR 9434968 OR 9434969)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MCZzPTI2NjkxNTImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145670+OR+9434968+OR+9434969%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145670 OR 9434968 OR 9434969)",
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
    "complete_query": "cites:(145670 OR 9434968 OR 9434969)",
    "indexed_citing_opinions": 245,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145670,
        "count": 199,
        "count_source": "search"
      },
      {
        "opinion_id": 9434968,
        "count": 55,
        "count_source": "search"
      },
      {
        "opinion_id": 9434969,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 430,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-grubbs.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0MDkxMDYmcz05NDIxNDM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28145670+OR+9434968+OR+9434969%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145670,
        "cited_id": 101970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 110061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 355709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 527795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 539861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 602842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 610895,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 754298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 764737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 766120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 778595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 787181,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 788436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145670,
        "cited_id": 799975,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LCU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-06T00:15:29Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T00:15:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T00:15:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T00:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T00:15:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Grubbs

```
(Slip Opinion)              OCTOBER TERM, 2005                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                    UNITED STATES v. GRUBBS

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

   No. 04–1414. Argued January 18, 2006—Decided March 21, 2006
A Magistrate Judge issued an “anticipatory” search warrant for re-
  spondent Grubbs’ house based on a federal officer’s affidavit. The af-
  fidavit explained that the warrant would not be executed until a par-
  cel containing a videotape of child pornography—which Grubbs had
  ordered from an undercover postal inspector—was received at, and
  physically taken into, the residence. The affidavit also referred to
  two attachments describing the residence and the items to be seized.
  After the package was delivered and the search commenced, Grubbs
  was given a copy of the warrant, which included the attachments but
  not the supporting affidavit. When he admitted ordering the video-
  tape, he was arrested, and the videotape and other items were seized.
  Following his indictment for receiving child pornography, see 18
  U. S. C. §2252(a)(2), Grubbs moved to suppress the seized evidence,
  arguing, inter alia, that the warrant was invalid because it failed to
  list the triggering condition. The District Court denied the motion,
  and Grubbs pleaded guilty. The Ninth Circuit reversed, concluding
  that the warrant ran afoul of the Fourth Amendment’s particularity
  requirement, which, under Circuit precedent, applied to the condi-
  tions precedent to an anticipatory warrant.
Held:
    1. Anticipatory warrants are not categorically unconstitutional un-
 der the Fourth Amendment’s provision that “no Warrants shall issue,
 but upon probable cause.” Probable cause exists when “there is a fair
 probability that contraband or evidence of a crime will be found in a
 particular place.” Illinois v. Gates, 462 U. S. 213, 238. When an an-
 ticipatory warrant is issued, the fact that the contraband is not pres-
 ently at the place described is immaterial, so long as there is prob-
 able cause to believe it will be there when the warrant is executed.
2                      UNITED STATES v. GRUBBS

                                  Syllabus

    Anticipatory warrants are, therefore, no different in principle from
    ordinary warrants: They require the magistrate to determine (1) that
    it is now probable that (2) contraband, evidence of a crime, or a fugi-
    tive will be on the described premises (3) when the warrant is exe-
    cuted. Where the anticipatory warrant places a condition (other than
    the mere passage of time) upon its execution, the first of these deter-
    minations goes not merely to what will probably be found if the con-
    dition is met, but also to the likelihood that the condition will be met,
    and thus that a proper object of seizure will be on the described
    premises.      Here, the occurrence of the triggering condition—
    successful delivery of the videotape—would plainly establish probable
    cause for the search, and the affidavit established probable cause to
    believe the triggering condition would be satisfied. Pp. 3–7.
       2. The warrant at issue did not violate the Fourth Amendment’s
    particularity requirement. The Amendment specifies only two mat-
    ters that the warrant must “particularly describ[e]”: “the place to be
    searched” and “the persons or things to be seized.” That language is
    decisive here; the particularity requirement does not include the con-
    ditions precedent to execution of the warrant. Cf. Dalia v. United
    States, 441 U. S. 238, 255, 257. Respondent’s two policy rationales—
    that setting forth the triggering condition in the warrant itself is nec-
    essary (1) to delineate the limits of the executing officer’s power and
    (2) to allow the individual whose property is searched or seized to po-
    lice the officer’s conduct—find no basis in either the Fourth Amend-
    ment or Federal Rule of Criminal Procedure 41. Pp. 7–9.
377 F. 3d 1072 and 389 F. 3d 1306, reversed and remanded.

  SCALIA, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and KENNEDY, THOMAS, and BREYER, JJ., joined, and in which
STEVENS, SOUTER, and GINSBURG, J., joined as to Parts I and II.
SOUTER, J., filed an opinion concurring in part and concurring in the
judgment, in which STEVENS and GINSBURG, JJ., joined. ALITO, J., took
no part in the consideration or decision of the case.
                       Cite as: 547 U. S. ____ (2006)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of thfe United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 04–1414
                                  _________________


UNITED STATES, PETITIONER v. JEFFREY GRUBBS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                               [March 21, 2006]

  JUSTICE SCALIA delivered the opinion of the Court.
  Federal law enforcement officers obtained a search
warrant for respondent’s house on the basis of an affidavit
explaining that the warrant would be executed only after a
controlled delivery of contraband to that location. We
address two challenges to the constitutionality of this
anticipatory warrant.
                              I
  Respondent Jeffrey Grubbs purchased a videotape
containing child pornography from a Web site operated by
an undercover postal inspector. Officers from the Postal
Inspection Service arranged a controlled delivery of a
package containing the videotape to Grubbs’ residence. A
postal inspector submitted a search warrant application to
a Magistrate Judge for the Eastern District of California,
accompanied by an affidavit describing the proposed op-
eration in detail. The affidavit stated:
    “Execution of this search warrant will not occur
    unless and until the parcel has been received by a
    person(s) and has been physically taken into the resi-
    dence . . . . At that time, and not before, this search
    warrant will be executed by me and other United
2               UNITED STATES v. GRUBBS

                     Opinion of the Court

    States Postal inspectors, with appropriate assistance
    from other law enforcement officers in accordance
    with this warrant’s command.” App. to Pet. for Cert.
    72a.
In addition to describing this triggering condition, the
affidavit referred to two attachments, which described
Grubbs’ residence and the items officers would seize.
These attachments, but not the body of the affidavit, were
incorporated into the requested warrant. The affidavit
concluded:
    “Based upon the foregoing facts, I respectfully submit
    there exists probable cause to believe that the items
    set forth in Attachment B to this affidavit and the
    search warrant, will be found [at Grubbs’ residence],
    which residence is further described at Attachment
    A.” Ibid.
  The Magistrate Judge issued the warrant as requested.
Two days later, an undercover postal inspector delivered
the package. Grubbs’ wife signed for it and took the un-
opened package inside. The inspectors detained Grubbs as
he left his home a few minutes later, then entered the
house and commenced the search. Roughly 30 minutes
into the search, Grubbs was provided with a copy of the
warrant, which included both attachments but not the
supporting affidavit that explained when the warrant
would be executed. Grubbs consented to interrogation by
the postal inspectors and admitted ordering the videotape.
He was placed under arrest, and various items were
seized, including the videotape.
  A grand jury for the Eastern District of California in-
dicted Grubbs on one count of receiving a visual depiction
of a minor engaged in sexually explicit conduct. See 18
U. S. C. §2252(a)(2). He moved to suppress the evidence
seized during the search of his residence, arguing as rele-
vant here that the warrant was invalid because it failed to
                      Cite as: 547 U. S. ____ (2006)                     3

                          Opinion of the Court

list the triggering condition. After an evidentiary hearing,
the District Court denied the motion. Grubbs pleaded
guilty, but reserved his right to appeal the denial of his
motion to suppress.
   The Court of Appeals for the Ninth Circuit reversed.
377 F. 3d 1072, amended, 389 F. 3d 1306 (2004). Relying
on Circuit precedent, it held that “the particularity re-
quirement of the Fourth Amendment applies with full
force to the conditions precedent to an anticipatory search
warrant.” 377 F. 3d, at 1077–1078 (citing United States v.
Hotal, 143 F. 3d 1223, 1226 (CA9 1998)). An anticipatory
warrant defective for that reason may be “cur[ed]” if the
conditions precedent are set forth in an affidavit that is
incorporated in the warrant and “presented to the person
whose property is being searched.” 377 F. 3d, at 1079.
Because the postal inspectors “failed to present the affida-
vit—the only document in which the triggering conditions
were listed”—to Grubbs or his wife, the “warrant was . . .
inoperative, and the search was illegal.” Ibid. We granted
certiorari. 545 U. S. ___ (2005).
                            II
  Before turning to the Ninth Circuit’s conclusion that the
warrant at issue here ran afoul of the Fourth Amend-
ment’s particularity requirement, we address the antece-
dent question whether anticipatory search warrants are
categorically unconstitutional.1 An anticipatory warrant
is “a warrant based upon an affidavit showing probable
——————
   1 This issue is “predicate to an intelligent resolution of the question

presented.” Ohio v. Robinette, 519 U. S. 33, 38 (1996) (internal quotation
marks omitted). It makes little sense to address what the Fourth
Amendment requires of anticipatory search warrants if it does not
allow them at all. Cf. Wilkinson v. Austin, 545 U. S. ___, ___ (2005) (slip
op., at 9) (addressing whether inmates had a liberty interest in avoiding
assignment to a “Supermax” prison, despite the State’s concession that
they did, because “[w]e need reach the question of what process is due only
if the inmates establish a constitutionally protected liberty interest”).
4                UNITED STATES v. GRUBBS

                      Opinion of the Court

cause that at some future time (but not presently) certain
evidence of crime will be located at a specified place.” 2 W.
LaFave, Search and Seizure §3.7(c), p. 398 (4th ed. 2004).
Most anticipatory warrants subject their execution to
some condition precedent other than the mere passage of
time—a so-called “triggering condition.” The affidavit at
issue here, for instance, explained that “[e]xecution of
th[e] search warrant will not occur unless and until the
parcel [containing child pornography] has been received by
a person(s) and has been physically taken into the resi-
dence.” App. to Pet. for Cert. 72a. If the government were
to execute an anticipatory warrant before the triggering
condition occurred, there would be no reason to believe the
item described in the warrant could be found at the
searched location; by definition, the triggering condition
which establishes probable cause has not yet been satis-
fied when the warrant is issued. Grubbs argues that for
this reason anticipatory warrants contravene the Fourth
Amendment’s provision that “no Warrants shall issue, but
upon probable cause.”
   We reject this view, as has every Court of Appeals to
confront the issue, see, e.g., United States v. Loy, 191 F. 3d
360, 364 (CA3 1999) (collecting cases). Probable cause
exists when “there is a fair probability that contraband or
evidence of a crime will be found in a particular place.”
Illinois v. Gates, 462 U. S. 213, 238 (1983). Because the
probable-cause requirement looks to whether evidence will
be found when the search is conducted, all warrants are, in
a sense, “anticipatory.” In the typical case where the
police seek permission to search a house for an item they
believe is already located there, the magistrate’s determi-
nation that there is probable cause for the search amounts
to a prediction that the item will still be there when the
warrant is executed. See People v. Glen, 30 N. Y. 2d 252,
258, 282 N. E. 2d 614, 617 (1972) (“[P]resent possession is
                     Cite as: 547 U. S. ____ (2006)                     5

                          Opinion of the Court

only probative of the likelihood of future possession.”).2
The anticipatory nature of warrants is even clearer in the
context of electronic surveillance. See, e.g., Katz v. United
States, 389 U. S. 347 (1967). When police request approval
to tap a telephone line, they do so based on the probability
that, during the course of the surveillance, the subject will
use the phone to engage in crime-related conversations.
The relevant federal provision requires a judge authoriz-
ing “interception of wire, oral, or electronic communica-
tions” to determine that “there is probable cause for belief
that particular communications concerning [one of various
listed offenses] will be obtained through such intercep-
tion.” 18 U. S. C. §2518(3)(b) (emphasis added); see also
United States v. Ricciardelli, 998 F. 2d 8, 11, n. 3 (CA1
1993) (“[T]he magistrate issues the warrant on the basis of
a substantial probability that crime-related conversations
will ensue.”). Thus, when an anticipatory warrant is
issued, “the fact that the contraband is not presently
located at the place described in the warrant is immate-
rial, so long as there is probable cause to believe that it
will be there when the search warrant is executed.”
United States v. Garcia, 882 F. 2d 699, 702 (CA2 1989)
(quoting United States v. Lowe, 575 F. 2d 1193, 1194 (CA6
1978); internal quotation marks omitted).
——————
  2 For this reason, probable cause may cease to exist after a warrant is

issued. The police may learn, for instance, that contraband is no longer
located at the place to be searched. See, e.g., United States v. Bowling,
900 F. 2d 926, 932 (CA6 1990) (recognizing that a fruitless consent
search could “dissipat[e] the probable cause that justified a warrant”).
Or the probable-cause showing may have grown “stale” in view of the
time that has passed since the warrant was issued. See United States
v. Wagner, 989 F. 2d 69, 75 (CA2 1993) (“[T]he facts in an affidavit
supporting a search warrant must be sufficiently close in time to the
issuance of the warrant and the subsequent search conducted so that
probable cause can be said to exist as of the time of the search and not
simply as of some time in the past.”); see also Sgro v. United States, 287
U. S. 206, 210–211 (1932).
6                UNITED STATES v. GRUBBS

                     Opinion of the Court

   Anticipatory warrants are, therefore, no different in
principle from ordinary warrants. They require the mag-
istrate to determine (1) that it is now probable that (2)
contraband, evidence of a crime, or a fugitive will be on
the described premises (3) when the warrant is executed.
It should be noted, however, that where the anticipatory
warrant places a condition (other than the mere passage of
time) upon its execution, the first of these determinations
goes not merely to what will probably be found if the
condition is met. (If that were the extent of the probability
determination, an anticipatory warrant could be issued for
every house in the country, authorizing search and seizure
if contraband should be delivered—though for any single
location there is no likelihood that contraband will be
delivered.) Rather, the probability determination for a
conditioned anticipatory warrant looks also to the likeli-
hood that the condition will occur, and thus that a proper
object of seizure will be on the described premises. In
other words, for a conditioned anticipatory warrant to
comply with the Fourth Amendment’s requirement of
probable cause, two prerequisites of probability must be
satisfied. It must be true not only that if the triggering
condition occurs “there is a fair probability that contra-
band or evidence of a crime will be found in a particular
place,” Gates, supra, at 238, but also that there is probable
cause to believe the triggering condition will occur. The
supporting affidavit must provide the magistrate with
sufficient information to evaluate both aspects of the
probable-cause determination. See Garcia, supra, at 703.
   In this case, the occurrence of the triggering condition—
successful delivery of the videotape to Grubbs’ residence—
would plainly establish probable cause for the search. In
addition, the affidavit established probable cause to be-
lieve the triggering condition would be satisfied. Although
it is possible that Grubbs could have refused delivery of
the videotape he had ordered, that was unlikely. The
                 Cite as: 547 U. S. ____ (2006)            7

                     Opinion of the Court

Magistrate therefore “had a ‘substantial basis for . . .
conclud[ing]’ that probable cause existed.” Gates, 462
U. S., at 238–239 (quoting Jones v. United States, 362 U. S.
257, 271 (1960)).
                              III
   The Ninth Circuit invalidated the anticipatory search
warrant at issue here because the warrant failed to specify
the triggering condition. The Fourth Amendment’s par-
ticularity requirement, it held, “applies with full force to
the conditions precedent to an anticipatory search war-
rant.” 377 F. 3d, at 1077–1078.
   The Fourth Amendment, however, does not set forth
some general “particularity requirement.” It specifies only
two matters that must be “particularly describ[ed]” in the
warrant: “the place to be searched” and “the persons or
things to be seized.” We have previously rejected efforts to
expand the scope of this provision to embrace unenumer-
ated matters. In Dalia v. United States, 441 U. S. 238
(1979), we considered an order authorizing the intercep-
tion of oral communications by means of a “bug” installed
by the police in the petitioner’s office. The petitioner
argued that, if a covert entry is necessary to install such a
listening device, the authorizing order must “explicitly set
forth its approval of such entries before the fact.” Id., at
255. This argument fell before the “ ‘precise and clear’ ”
words of the Fourth Amendment: “Nothing in the lan-
guage of the Constitution or in this Court’s decisions
interpreting that language suggests that, in addition to
the [requirements set forth in the text], search warrants
also must include a specification of the precise manner in
which they are to be executed.” Id., at 255 (quoting Stan-
ford v. Texas, 379 U. S. 476, 481 (1965)), 257. The language
of the Fourth Amendment is likewise decisive here; its
particularity requirement does not include the conditions
precedent to execution of the warrant.
8                UNITED STATES v. GRUBBS

                      Opinion of the Court

   Respondent, drawing upon the Ninth Circuit’s analysis
below, relies primarily on two related policy rationales.
First, he argues, setting forth the triggering condition in
the warrant itself is necessary “to delineate the limits of
the executing officer’s power.” Brief for Respondent 20.
This is an application, respondent asserts, of the following
principle: “[I]f there is a precondition to the valid exercise
of executive power, that precondition must be particularly
identified on the face of the warrant.” Id., at 23. That
principle is not to be found in the Constitution. The
Fourth Amendment does not require that the warrant set
forth the magistrate’s basis for finding probable cause,
even though probable cause is the quintessential “precon-
dition to the valid exercise of executive power.” Much less
does it require description of a triggering condition.
   Second, respondent argues that listing the triggering
condition in the warrant is necessary to “ ‘assur[e] the
individual whose property is searched or seized of the
lawful authority of the executing officer, his need to
search, and the limits of his power to search.’ ” Id., at 19
(quoting United States v. Chadwick, 433 U. S. 1, 9 (1977)).
The Ninth Circuit went even further, asserting that if the
property owner were not informed of the triggering condi-
tion, he “would ‘stand [no] real chance of policing the
officers’ conduct.’ ” 377 F. 3d, at 1079 (quoting Ramirez v.
Butte-Silver Bow County, 298 F. 3d 1022, 1027 (CA9
2002)). This argument assumes that the executing officer
must present the property owner with a copy of the war-
rant before conducting his search. See 377 F. 3d, at 1079,
n. 9. In fact, however, neither the Fourth Amendment nor
Rule 41 of the Federal Rules of Criminal Procedure im-
poses such a requirement. See Groh v. Ramirez, 540 U. S.
551, 562, n. 5 (2004). “The absence of a constitutional
requirement that the warrant be exhibited at the outset of
the search, or indeed until the search has ended, is . . .
evidence that the requirement of particular description
                  Cite as: 547 U. S. ____ (2006)            9

                      Opinion of the Court

does not protect an interest in monitoring searches.”
United States v. Stefonek, 179 F. 3d 1030, 1034 (CA7 1999)
(citations omitted). The Constitution protects property
owners not by giving them license to engage the police in a
debate over the basis for the warrant, but by interposing,
ex ante, the “deliberate, impartial judgment of a judicial
officer . . . between the citizen and the police.” Wong Sun
v. United States, 371 U. S. 471, 481–482 (1963), and by
providing, ex post, a right to suppress evidence improperly
obtained and a cause of action for damages.
                        *     *    *
  Because the Fourth Amendment does not require that
the triggering condition for an anticipatory search warrant
be set forth in the warrant itself, the Court of Appeals
erred in invalidating the warrant at issue here. The
judgment of the Court of Appeals is reversed, and the case
is remanded for further proceedings consistent with this
opinion.
                                             It is so ordered.

  JUSTICE ALITO took no part in the consideration or
decision of this case.
                 Cite as: 547 U. S. ____ (2006)           1

                     Opinion of SOUTER, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1414
                         _________________


UNITED STATES, PETITIONER v. JEFFREY GRUBBS
 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF
            APPEALS FOR THE NINTH CIRCUIT
                       [March 21, 2006]

   JUSTICE SOUTER, with whom JUSTICE STEVENS and
JUSTICE GINSBURG join, concurring in part and concurring
in the judgment.
   I agree with the Court that anticipatory warrants are
constitutional for the reasons stated in Part II of the
Court’s opinion, and I join in the disposition of this case.
But I would qualify some points made in Part III.
   The Court notes that a warrant’s failure to specify the
place to be searched and the objects sought violates an
express textual requirement of the Fourth Amendment,
whereas the text says nothing about a condition placed by
the issuing magistrate on the authorization to search
(here, delivery of the package of contraband). That textual
difference is, however, no authority for neglecting to spec-
ify the point or contingency intended by the magistrate to
trigger authorization, and the government should beware
of banking on the terms of a warrant without such specifi-
cation. The notation of a starting date was an established
feature even of the objectionable 18th-century writs of
assistance, see, e.g., Massachusetts Writs of Assistance
Bill, 1762, reprinted in M. Smith, The Writs of Assistance
Case 567–568 (1978); Writ of Assistance (English) of
George III, 1761, reprinted in id., at 524–527. And it is
fair to say that the very word “warrant” in the Fourth
Amendment means a statement of authority that sets out
the time at which (or, in the case of anticipatory warrants,
2                   UNITED STATES v. GRUBBS

                         Opinion of SOUTER, J.

the condition on which) the authorization begins.*
   An issuing magistrate’s failure to mention that condi-
tion can lead to several untoward consequences with
constitutional significance. To begin with, a warrant that
fails to tell the truth about what a magistrate authorized
cannot inform the police officer’s responsibility to respect
the limits of authorization, see Groh v. Ramirez, 540 U. S.
551, 560–563, 561, and n. 4 (2004), a failing assuming real
significance when the warrant is not executed by the
official who applied for it and happens to know the un-
stated condition. The peril is that if an officer simply
takes such a warrant on its face and makes the ostensibly
authorized search before the unstated condition has been
met, the search will be held unreasonable. It is true that
we have declined to apply the exclusionary rule when a
police officer reasonably relies on the product of a magis-
trate’s faulty judgment or sloppy practice, see Massachu-
setts v. Sheppard, 468 U. S. 981, 987–991 (1984). But when
a government officer obtains what the magistrate says is
an anticipatory warrant, he must know or should realize
when it omits the condition on which authorization de-
pends, and it is hard to see why the government should
not be held to the condition despite the unconditional face
of the warrant. Cf. Groh v. Ramirez, supra, at 554–555,
563, and n. 6 (declaring unconstitutional a search con-
ducted pursuant to a warrant failing to specify the items
the government asked the magistrate permission to seize
in part because “officers leading a search team must ‘make
sure that they have a proper warrant that in fact author-
izes the search and seizure they are about to conduct’ ”
(brackets omitted)).
   Nor does an incomplete anticipatory warrant address an
——————
  * Federal Rule of Criminal Procedure 41(e)(2)(A) in fact requires that
an issued warrant command the executing officer to “execute the
warrant within a specified time no longer than 10 days.”
                  Cite as: 547 U. S. ____ (2006)             3

                      Opinion of SOUTER, J.

owner’s interest in an accurate statement of the govern-
ment’s authority to search property. To be sure, the ex-
tent of that interest is yet to be settled; in Groh v. Ramirez,
supra, the Court was careful to note that the right of an
owner to demand to see a copy of the warrant before mak-
ing way for the police had not been determined, id., at 562,
n. 5, and it remains undetermined today. But regardless
of any right on the owner’s part, showing an accurate
warrant reliably “assures the individual whose property is
searched or seized of the lawful authority of the executing
officer, his need to search, and the limits of his power to
search.” United States v. Chadwick, 433 U. S. 1, 9 (1977),
quoted in Groh v. Ramirez, supra, at 561. And if a later
case holds that the homeowner has a right to inspect the
warrant on request, a statement of the condition of au-
thorization would give the owner a right to correct any
misapprehension on the police’s part that the condition
had been met when in fact it had not been. If the police
were then to enter anyway without a reasonable (albeit
incorrect) justification, the search would certainly be open
to serious challenge as unreasonable within the meaning
of the Fourth Amendment.

```

---

## GROUP: _overhaul2/lake/cases/United States v. Hanapel.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Hanapel
type: case
citation: "112 F.4th 539 (2024)"
parallel_cite: ""
neutral_cite: ""
court: 8th Cir. 2024
court_level: coa
circuit: ca8
year: 2024
date_decided: 2024-08-12
docket: 23-2653
authority_weight: "Binding in-circuit — 8th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/10038262/united-states-v-james-hanapel/"
  cluster_id: 10038262
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Hanapel
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Entrapment]]"
    role: Key
related:
  - "[[Entrapment]]"
  - "[[Jacobson v. United States]]"
  - "[[Mathews v. United States]]"
  - "[[Sherman v. United States]]"
tags:
  - case
  - entrapment
  - predisposition
  - inducement
  - undercover-sting
  - eighth-circuit
holding: "The Eighth Circuit affirmed the denial of judgment of acquittal, holding that Hanapel failed to establish entrapment as a matter of law: there was no government inducement as a matter of law, and his initial hesitation on learning the decoy's age did not negate the predisposition a reasonable jury could find from his ready pursuit of the opportunity — arriving at the meeting place with condoms within hours."
---

# United States v. Hanapel

*112 F.4th 539 (8th Cir. 2024)* (No. 23-2653) · U.S. Court of Appeals for the Eighth Circuit · **Binding in-circuit — 8th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): identity cluster 10038262 → opinion 10504863 (112 F.4th 539, decided 2024-08-12); Rule quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
During the 2021 Sturgis Motorcycle Rally, a Homeland Security agent posed on the SKOUT social app as "Journey," a fictitious fourteen-year-old. James Hanapel, messaging as a twenty-one-year-old "Max Taylor," asked to "hang out." When Journey said she was fourteen, Hanapel first replied "I can't talk to you" and that they could "be friends but nothing more." After Journey said guys her age were "lame" and that she "met people" on the app "all the time," Hanapel steered the exchange to sex, proposed that they "hook up," agreed to meet at a local middle school that night, and said he would bring condoms. He was arrested at the school with a newly purchased package of condoms and admitted he had traveled to have sex with the girl. A jury convicted him of attempted enticement of a minor, 18 U.S.C. § 2422(b); the district court denied his motion for judgment of acquittal based on entrapment and imposed the 120-month statutory minimum.

## Issue
Whether Hanapel established entrapment as a matter of law — both government inducement and his own lack of predisposition — so that the district court erred in denying his motion for judgment of acquittal, or whether a reasonable jury could reject the entrapment defense.

## Rule
The [[Common Legal Terms#affirmative-defense|affirmative defense]] of entrapment has two elements — "government inducement of the crime, and a lack of predisposition on the part of the defendant to engage in the criminal conduct." The government may use "artifice, stratagem, and undercover agents" and may furnish a willing person the opportunity to offend; it may not implant criminal design in an unwilling person. To overturn a conviction as a matter of law the defendant must establish **both** inducement and non-predisposition, and a ready response to minimal inducement itself indicates predisposition. Applying that standard, the court held that a defendant's early reluctance does not, by itself, negate predisposition: "Initial hesitance to engage in criminal conduct does not establish lack of predisposition as a matter of law." — 112 F.4th 539, slip op. at 8. ^pin-op8

## Application
Neither element was established as a matter of law. On inducement, the government did not initiate contact — Hanapel proposed the meeting and was first to raise "hook[ing] up" and sex — and neither Journey's unsolicited sports-bra photo (far more revealing images have been held insufficient) nor her mildly "precocious" persona compelled a finding of inducement; the court concluded there was no inducement as a matter of law. On predisposition, Hanapel's initial "friends but nothing more" response to Journey's age did not negate predisposition: once she signaled interest, he promptly discussed sexual acts and, within four hours of learning she was a minor, arrived at the meeting place with condoms — evidence from which a reasonable jury could find him predisposed.

## Conclusion
**Affirmed.** Chief Judge Colloton wrote for the panel (Colloton, C.J.; Erickson and Kobes, JJ.).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub and renders under the ⚪ banner until S9 promotion. *Hanapel* is a clean recent application of the federal **subjective** entrapment test: the controlling fact is **predisposition**, not the fact of inducement, so a sting that merely furnishes the opportunity — and a defendant's momentary hesitation before seizing it — leaves the jury's rejection of the defense intact.

## Appears on
- [[Entrapment]] — *Key*

## Sources
- [*United States v. Hanapel*, 112 F.4th 539 (8th Cir. 2024)](https://www.courtlistener.com/opinion/10038262/united-states-v-james-hanapel/) — pinpoint: slip op. at 8 (predisposition / no-inducement-as-a-matter-of-law holding; the CL opinion text is slip-paginated, so the pin is slip-style per S2 A3). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8e1efc7096646726", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Hanapel"}, "payload": {"all": [{"cite": "112 F.4th 539", "page": "539", "reporter": "F.4th", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "112"}], "display": "112 F.4th 539", "official": {"cite": "112 F.4th 539", "page": "539", "reporter": "F.4th", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "112"}, "official_selection_present": true, "record_id": "United States v. Hanapel"}}
{"assertion_id": "cca32d8f400078ea", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Hanapel"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Hanapel", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Hanapel

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Hanapel",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. James Hanapel",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "United States v. Hanapel",
    "court": "8th Cir. 2024",
    "court_id": "ca8",
    "court_level": "coa",
    "circuit": "ca8",
    "state": null,
    "date_decided": "2024-08-12",
    "year": 2024,
    "docket": "23-2653",
    "cluster_id": 10038262,
    "lead_opinion_id": 10504863,
    "sibling_ids": [],
    "absolute_url": "/opinion/10038262/united-states-v-james-hanapel/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "112 F.4th 539",
      "volume": "112",
      "reporter": "F.4th",
      "page": "539",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "112 F.4th 539",
        "volume": "112",
        "reporter": "F.4th",
        "page": "539",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "112 F.4th 539",
    "official_selection": {
      "court_class": "state",
      "selected": "112 F.4th 539",
      "reason": "selected_rank_3"
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
    "date_created": "2026-07-06T05:53:23Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T05:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-hanapel--10038262",
      "to_record_id": "United States v. Hanapel",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Hanapel

```
                 United States Court of Appeals
                            For the Eighth Circuit
                        ___________________________

                                No. 23-2653
                        ___________________________

                             United States of America,

                        lllllllllllllllllllllPlaintiff - Appellee,

                                           v.

                               James Dean Hanapel,

                      lllllllllllllllllllllDefendant - Appellant.
                                       ____________

                    Appeal from United States District Court
                    for the District of South Dakota - Western
                                   ____________

                            Submitted: March 15, 2024
                              Filed: August 12, 2024
                                  ____________

Before COLLOTON, Chief Judge, ERICKSON and KOBES, Circuit Judges.
                            ____________

COLLOTON, Chief Judge.

      A jury found James Hanapel guilty of attempting to entice a minor to engage
in sexual activity. See 18 U.S.C. § 2422(b). The charge arose from Hanapel’s
dialogue with an undercover officer who posed as a fourteen-year-old girl. At trial,
Hanapel raised the affirmative defense of entrapment. At the close of the
government’s case, he moved for judgment of acquittal on the ground that he was
entrapped as a matter of law. The district court* denied the motion, and we affirm.

                                          I.

      In August 2021, several law enforcement agencies participated in an operation
to combat child exploitation on the internet during the Sturgis Motorcycle Rally in
South Dakota. As part of the operation, a special agent from the Department of
Homeland Security posed as “Journey,” a fictitious fourteen-year-old girl whose
parents were attending the rally.

       The agent created an account for Journey on SKOUT, an internet application
that is used for dating and social networking. On Journey’s public profile, he
represented that she was eighteen years old because SKOUT required users to be no
younger. He also included two photographs of “Journey” that were actually pictures
of an adult woman associated with law enforcement.

      On August 10, 2021, Hanapel sent a message to Journey from an account
purporting to belong to “Max Taylor.” According to the profile, Max Taylor was a
twenty-one-year-old man located in Box Elder, South Dakota. Hanapel asked
whether Journey wanted to “hang out.” The next day, Journey said “[m]aybe” and
provided a telephone number.

       On August 12, Hanapel and Journey began to communicate via text message.
Hanapel asked whether Journey “[w]ant[ed] some company.” Journey said that she
did, but she “want[ed] to tell” Hanapel that she was “not 18” and was “just here trying



      *
       The Honorable Jeffrey L. Viken, United States District Judge for the District
of South Dakota, now retired.

                                         -2-
to have fun while my parents are at the rally.” Hanapel asked, “How old are you ??”
At 3:40 p.m., Journey replied, “14 but turn 15 in a couple months.”

        Less than one minute later, Hanapel responded, “Yoo I can’t talk to you.” He
added that they could “be friends but nothing more.” Journey wrote back: “ok.
sorry. i understand. guys my age are pretty lame and you seemed pretty cool. i
didn’t mean to upset you sorry. you were just so cute.” Hanapel reassured her that
“[i]t’s okay you seem cool I just don’t want trouble if you wanna hangout and grab
ice cream or catch a movie that’s cool but I’d have to meet your parents[.] Because
if they got the wrong impression I’m going to jail.”

      Journey said that she was “not here to get anyone in trouble,” and had “met
people” on SKOUT “all the time.” Hanapel replied, “Oh okay well do you wanna go
do something.” Journey asked what he had in mind. Hanapel suggested that they
could “grab food or watch a movie,” and asked what Journey had “done with people
before.” Journey answered, “a lot....lol [laugh out loud].” Hanapel asked what she
meant, and Journey told him to “just use your imagination hehehehe.”

       Hanapel again asked if Journey “want[ed] some company.” She said that it
“depends on what you have in mind,” because “this is my last night home by myself
so i have to be careful on who i choose to hang with so i can make the most of it.”
Hanapel told her it was “really up to” her whether they met and what they would do.
Journey said she “like[s] someone who knows what they want.”

      Hanapel asked, “Honestly you tryna hook up ?” Journey replied, “up to you
maxie.” He asked why he was “making all the decisions”; Journey said that he was
“older and more experienced.” Hanapel asked for Journey’s address. She said, “what
are you thinking maxxie? look at you trying to be my pick.”




                                        -3-
       Journey then sent a photograph of herself and asked whether Hanapel liked her
outfit. In the photo, Journey appears to be holding the camera above her head. She
is looking up at the camera, and wearing a sports bra and leggings. Special Agent
Berger testified that he sent this photo because he considered it “nonsexual in nature.”
He testified that the clothing was “consistent with what the temperature was like
outside” in mid-August. Hanapel replied that the photo was “[s]exy,” and said, “I’m
thinking I come over we watch a movie make out and see what happens from there.”
Journey asked what he “had in mind” because she “may surprise” him. He suggested
they “could hook up.”

       The conversation pivoted to Journey’s experiences with other people whom she
met on SKOUT. Hanapel asked her how many people she had met, how old they
were, and what they did together. Journey answered that she met “a few” people who
were older than “Max,” and that they did “fun stuff hehehehe.” Hanapel asked
“[w]hat kind of fun stuff,” and Journey replied, “didnt i tell you to use your
imagination. im willing to try whatever. you just name it.” Hanapel suggested
“[s]ex,” and asked if she “want[ed] to fuck.” Journey asked, “do you?” Hanapel
answered, “Yes I’m down.” Journey asked whether there was anything that Hanapel
“want[ed] to try.” He said, “Yeah anal if you[’re] down.”

       The two agreed to meet at a local middle school that night. Hanapel agreed to
bring condoms. He drove to the school and was arrested at approximately 7:30 p.m.
on August 12. Police found a newly purchased package of condoms in his car. In a
post-arrest interview, Hanapel admitted that he traveled to the school to have sex with
the girl.

       A grand jury charged Hanapel with attempted enticement of a minor to engage
in unlawful sexual activity. See 18 U.S.C. § 2422(b). At trial, the district court gave
the jury the following instruction:



                                          -4-
      One of the issues in this case is whether Mr. Hanapel was entrapped.
      The government has the burden of proving beyond a reasonable doubt
      that Mr. Hanapel was not entrapped by showing either: (1) Mr. Hanapel
      was willing to solicit a minor before he was approached or contacted by
      law enforcement agents; or (2) the government, or someone acting for
      the government, did not persuade or talk Mr. Hanapel into soliciting a
      minor. In deciding whether Mr. Hanapel was willing to solicit a minor
      before he was approached or contacted by law enforcement agents, you
      may consider whether the defendant enthusiastically responded and
      promptly availed himself of his first opportunity to commit a crime
      without government prodding. If the government proves either of these
      beyond a reasonable doubt, you must reject Mr. Hanapel’s claim of
      entrapment. If the government fails to prove at least one of these
      beyond a reasonable doubt, then you must find Mr. Hanapel not guilty.

      The law allows the government to use undercover agents, deception, and
      other methods to present a person already willing to commit a crime
      with the opportunity to commit a crime, but the law does not allow the
      government to persuade an unwilling person to commit a crime. Simply
      giving someone a favorable opportunity to commit a crime is not the
      same as persuading him.

       While the jury deliberated, Hanapel moved for judgment of acquittal. He
argued that the evidence showed that he was entrapped as a matter of law. The
district court denied the motion. The jury returned a guilty verdict, and the district
court sentenced Hanapel to the statutory minimum term of 120 months’
imprisonment. Hanapel appeals and renews his contention that he was entrapped as
a matter of law. Viewing the evidence in the light most favorable to the verdict, we
consider whether any reasonable jury could have rejected the entrapment defense.
See United States v. Neri, 89 F.4th 668, 670 (8th Cir. 2023).




                                         -5-
                                         II.

      It is “well settled that the government may use artifice, stratagem, and
undercover agents in its pursuit of criminals.” United States v. Myers, 575 F.3d 801,
806 (8th Cir. 2009). The government may not “originate a criminal design, implant
in an innocent person’s mind the disposition to commit a criminal act, and then
induce commission of the crime.” Jacobson v. United States, 503 U.S. 540, 548
(1992). The affirmative defense of entrapment “guards against such overzealous
prosecutions.” United States v. Lasley, 79 F.4th 979, 983 (8th Cir. 2023).

       An entrapment defense has two elements: “government inducement of the
crime, and a lack of predisposition on the part of the defendant to engage in the
criminal conduct.” Mathews v. United States, 485 U.S. 58, 63 (1988). The
inducement and predisposition “inquiries are often closely linked, because the need
for greater inducement may suggest that the defendant was not predisposed to commit
the crime; and conversely, a ready response to minimal inducement indicates criminal
predisposition.” Myers, 575 F.3d at 805. A defendant is entitled to a jury instruction
on entrapment if prior to trial he produces sufficient evidence of inducement. United
States v. Young, 613 F.3d 735, 746 (8th Cir. 2010). If he makes a showing of
inducement, the burden at trial shifts to the government to prove predisposition
beyond a reasonable doubt. Id. at 747.

      The district court concluded that Hanapel produced sufficient evidence to
warrant a jury instruction on entrapment. But the jury found beyond a reasonable
doubt that he was not entrapped. To prevail on appeal, Hanapel must establish as a
matter of law both that he was induced and that he was not predisposed to commit the
offense. See Myers, 575 F.3d at 805-06 & n.4; United States v. Hinton, 908 F.2d 355,
357 (8th Cir. 1990).




                                         -6-
       We begin with inducement. Four factors are relevant: (1) whether the
government initiated the contact with the defendant; (2) whether the government
introduced the topics of meeting and sex; (3) the effect of the photos sent by the
government; and (4) the degree to which the government influenced the behavior of
the defendant by portraying the minor as sexually precocious. United States v. Tobar,
985 F.3d 591, 593 (8th Cir. 2021); Myers, 575 F.3d at 806.

      The government did not initiate contact with Hanapel. Hanapel first proposed
a meeting with the minor, and he was the first to mention that they could “hook up”
and engage in “[s]ex.” Hanapel argues that the government introduced the topic of
sex when Journey told Hanapel that she wanted to “make the most” of her time at
home alone. While Journey’s response may have been suggestive, she did not
pressure Hanapel to engage in sexual activity or propose sexual activity directly.
Hanapel interpreted her message to refer to sexual activity, and he then explicitly
suggested engaging in such conduct.

       Hanapel’s primary argument is that he was induced as a matter of law when
Journey sent him an unsolicited photo of herself in a sports bra. He argues that the
government sent the “suggestive” photo because he was hesitant to meet Journey. We
are not convinced that the photo establishes inducement as a matter of law. Hanapel
argues summarily that the photo “speak[s] for itself,” but it does not say much about
entrapment. Hanapel described Journey as “fully clothed” when he described the
photo to police. Far more revealing images have been held insufficient to constitute
inducement as a matter of law. See United States v. Shinn, 681 F.3d 924, 928-30 (8th
Cir. 2012); Myers, 575 F.3d at 803, 806. The evidence also does not compel a
conclusion that the government sent the photo in response to Hanapel’s reluctance.
Journey sent the photo in direct response to his message asking for her address. By
that time, Hanapel already had asked whether she was “tryna hook up.” A reasonable
jury could reject Hanapel’s contention that the government’s use of the photo
demonstrated impermissible inducement.

                                         -7-
       Nor are we convinced that adding Journey’s supposedly “precocious” conduct
to the photograph amounts to inducement as a matter of law. While Journey implied
that she previously had engaged in sexual activity, she also downplayed her sexual
history in a message to Hanapel: “trust me im not that experienced.” To the extent
that Journey’s “photos and behavior portray her as sexually precocious, it is only to
a minor degree.” Tobar, 985 F.3d at 593. There was no inducement as a matter of
law.

      As for predisposition, we conclude that the evidence was sufficient for a
reasonable jury to reject Hanapel’s defense. A defendant is predisposed if he readily
responds to a government agent’s offer of opportunity to commit a crime. Jacobson,
503 U.S. at 549-50; Myers, 575 F.3d at 807-08. Hanapel argues that he was not
predisposed because when Journey first shared her age, he told her that they could “be
friends but nothing more.”

       Initial hesitance to engage in criminal conduct does not establish lack of
predisposition as a matter of law. In United States v. Zupnik, 989 F.3d 649 (8th Cir.
2021), the defendant also balked at first and told the minor, “I am kinda waaayyy too
old for you !” Id. at 652. But when the minor said that she was “just tired of boys,”
the defendant “proceeded to exchange sexually explicit messages with her and plan
to meet her in person to engage in sexual acts.” Id. at 652, 655-56. This court
concluded that the exchange included “more than sufficient evidence” of the
defendant’s predisposition. Id. at 656.

       Other than his initial reaction to Journey’s age, Hanapel showed no hesitation
or resistance to meet and engage in sexual conduct. Once Journey told him that “guys
my age are pretty lame,” and that she “met people on” SKOUT “all the time,”
Hanapel began to discuss sexual activity. Within four hours after Journey revealed
that she was a minor, Hanapel was at their agreed-upon meeting place with newly



                                         -8-
purchased condoms. Based on this conduct, a reasonable jury could conclude that
Hanapel was predisposed to commit the offense.

      The judgment of the district court is affirmed.
                     ______________________________




                                      -9-

```

---
