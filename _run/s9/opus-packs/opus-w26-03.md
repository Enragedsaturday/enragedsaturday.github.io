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

## GROUP: content/cases/Arkansas v. Sullivan.md  (`case`, 5 assertions)

### content_page

```
---
title: "Arkansas v. Sullivan"
type: case
citation: "532 U.S. 769 (2001)"
parallel_cite: "121 S. Ct. 1876; 149 L. Ed. 2d 994"
neutral_cite: 2001 U.S. LEXIS 4118
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-05-29
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arkansas v. Sullivan
  varies_by_point: false
  scope_note: "Good law. Per curiam. An arrest supported by probable cause is valid under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren v. United States from traffic stops to arrests; a state may not, as a matter of federal constitutional law, provide greater protection by inquiring into subjective motive."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2620699/arkansas-v-sullivan/"
  cluster_id: 2620699
  opinion_id: 9795082
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Progeny"
related: ["[[Whren v. United States]]", "[[Atwater v. City of Lago Vista]]", "[[Devenpeck v. Alford]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "pretext", "arrest", "per-curiam"]
holding: "An arrest supported by probable cause is reasonable under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren's rule from stops to arrests."
lake:
  record_id: Arkansas v. Sullivan
  status: verified
  projected_at: 2026-07-06
---

# Arkansas v. Sullivan

*532 U.S. 769 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Taylor stopped Kenneth Sullivan for speeding and arrested him for traffic offenses, including a fine-only speeding violation. A search of the vehicle turned up drug-related evidence. Sullivan moved to suppress, arguing that his arrest was "merely a 'pretext and sham to search' him" and therefore violated the Fourth Amendment. The trial court suppressed the evidence and the Arkansas Supreme Court affirmed on rehearing, holding that an arrest — even one supported by probable cause — violates the Fourth Amendment if the officer's true motivation was to conduct a search, and that Arkansas could in any event read the Constitution to provide such protection. The State sought [[Reading and Citing Cases#certiorari-cert|certiorari]], and the Court decided the case [[Common Legal Terms#per-curiam|per curiam]].

## Issue
Whether an arrest supported by probable cause violates the Fourth Amendment because the arresting officer had a pretextual or improper subjective motivation, and whether a state may interpret the Federal Constitution to forbid such pretextual arrests.

## Rule
No to both. The officer's subjective motive is irrelevant to an objectively justified, probable-cause arrest: the Court "held unanimously that '[s]ubjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.'" — 532 U.S. at 772 (quoting *Whren v. United States*). ^pin-772

The Arkansas court's contrary view — that a probable-cause arrest can nevertheless be invalid because of improper motive — "cannot be squared with our decision in *Whren*, in which we noted our 'unwilling[ness] to entertain Fourth Amendment challenges based on the actual motivations of individual officers.'" — *Id.* ^pin-772b

A state also may not use the *federal* Constitution to impose greater restrictions than this Court requires: while a State is free "as a matter of its own law to impose greater restrictions on police activity," it "may not impose such greater restrictions as a matter of *federal constitutional law* when this Court specifically refrains from imposing them." — *Id.* at 772 (quoting *Oregon v. Hass*). ^pin-772c

## Application
The Arkansas Supreme Court never questioned Officer Taylor's authority to arrest Sullivan for a fine-only traffic violation, and the arrest was supported by probable cause. It suppressed the drug evidence solely on the theory that Taylor's real motivation was to search — exactly the subjective-motive inquiry *[[Whren v. United States|Whren]]* forecloses. Because *[[Whren v. United States|Whren]]*'s rule applies to a probable-cause arrest no less than to a stop, the pretext theory could not invalidate the arrest; and the state court's alternative basis (reading the Federal Constitution more broadly) was foreclosed by *Oregon v. Hass*.

## Conclusion
A probable-cause arrest is reasonable regardless of the officer's pretextual or subjective motive, and a state may not hold otherwise as a matter of federal constitutional law. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Sullivan* extends [[Whren v. United States]] from traffic stops to arrests and pairs with [[Atwater v. City of Lago Vista]] (decided the same day, recognizing authority to arrest for a fine-only offense). The objective-reasonableness, motive-irrelevant principle is reaffirmed in [[Devenpeck v. Alford]].

## Appears on
- [[Traffic Stops]] — *Progeny*

## Sources
- *Arkansas v. Sullivan*, 532 U.S. 769 (2001) (per curiam) — https://www.courtlistener.com/opinion/2620699/arkansas-v-sullivan/ — pinpoint: 772.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8baeb51b3e16e6a8", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "532 U.S. 769 (2001)", "court": "U.S. Supreme Court", "neutral_cite": "2001 U.S. LEXIS 4118", "official_citation_present": true, "parallel_cite": "121 S. Ct. 1876; 149 L. Ed. 2d 994", "title": "Arkansas v. Sullivan", "year": "2001"}}
{"assertion_id": "2e979bd63a8fbed0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An arrest supported by probable cause is reasonable under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren's rule from stops to arrests.", "title": "Arkansas v. Sullivan"}}
{"assertion_id": "8ebc6f96a1258bfc", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Progeny", "title": "Arkansas v. Sullivan"}}
{"assertion_id": "251c8d99d37cfbf2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2001-05-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arkansas v. Sullivan", "field_i_validity": "good_law", "scope_note": "Good law. Per curiam. An arrest supported by probable cause is valid under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren v. United States from traffic stops to arrests; a state may not, as a matter of federal constitutional law, provide greater protection by inquiring into subjective motive.", "title": "Arkansas v. Sullivan", "varies_by_point": "false"}}
{"assertion_id": "27bd7a9f317554c1", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arkansas v. Sullivan"}}
```

### lake record — Arkansas v. Sullivan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arkansas v. Sullivan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arkansas v. Sullivan",
    "case_name_short": "Sullivan",
    "case_name_full": "Arkansas v. Sullivan",
    "input_case_name": "Arkansas v. Sullivan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-05-29",
    "year": 2001,
    "docket": null,
    "cluster_id": 2620699,
    "lead_opinion_id": 9795082,
    "sibling_ids": [
      2620699,
      9795082,
      9795083
    ],
    "absolute_url": "/opinion/2620699/arkansas-v-sullivan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "532 U.S. 769",
      "volume": "532",
      "reporter": "U.S.",
      "page": "769",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "121 S. Ct. 1876",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1876",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 994",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 4118",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "532 U.S. 769",
        "volume": "532",
        "reporter": "U.S.",
        "page": "769",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1876",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1876",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 994",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 4118",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "4118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "532 U.S. 769",
    "official_selection": {
      "court_class": "scotus",
      "selected": "532 U.S. 769",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-772",
      "page": null,
      "quote": "and therefore violated the Fourth Amendment. The trial court suppressed the evidence and the Arkansas Supreme Court affirmed on rehearing, holding that an arrest \u2014 even one supported by probable cause \u2014 violates the Fourth Amendment if the officer's true motivation was to conduct a search, and that Arkansas could in any event read the Constitution to provide such protection. The State sought certiorari, and the Court decided the case per curiam. ## Issue Whether an arrest supported by probable cause violates the Fourth Amendment because the arresting officer had a pretextual or improper subjective motivation, and whether a state may interpret the Federal Constitution to forbid such pretextual arrests. ## Rule No to both. The officer's subjective motive is irrelevant to an objectively justified, probable-cause arrest: the Court",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-772b",
      "page": null,
      "quote": "cannot be squared with our decision in *Whren*, in which we noted our 'unwilling[ness] to entertain Fourth Amendment challenges based on the actual motivations of individual officers.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-772c",
      "page": null,
      "quote": "as a matter of its own law to impose greater restrictions on police activity,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arkansas v. Sullivan",
    "varies_by_point": false,
    "scope_note": "Good law. Per curiam. An arrest supported by probable cause is valid under the Fourth Amendment regardless of the officer's pretextual or subjective motivation, extending Whren v. United States from traffic stops to arrests; a state may not, as a matter of federal constitutional law, provide greater protection by inquiring into subjective motive.",
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
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vennus v. State",
          "cluster_id": 1496491,
          "cite": [
            "282 S.W.3d 70",
            "2009 Tex. Crim. App. LEXIS 977",
            "2009 WL 1066947"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mount v. State",
          "cluster_id": 1505113,
          "cite": [
            "217 S.W.3d 716",
            "2007 Tex. App. LEXIS 1135",
            "2007 WL 484784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bookhardt, Ronnie",
          "cluster_id": 185564,
          "cite": [
            "277 F.3d 558",
            "349 U.S. App. D.C. 317",
            "2002 U.S. App. LEXIS 1224",
            "2002 WL 104531"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane1_negative"
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
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 2140668,
          "cite": [
            "767 N.E.2d 638",
            "97 N.Y.2d 341",
            "741 N.Y.S.2d 147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zellner v. Summerlin",
          "cluster_id": 2707,
          "cite": [
            "494 F.3d 344",
            "2007 U.S. App. LEXIS 17272",
            "2007 WL 2067932"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert Darruthy v. City of Miami",
          "cluster_id": 76372,
          "cite": [
            "351 F.3d 1080",
            "2003 U.S. App. LEXIS 24048",
            "2003 WL 22799497"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hicks",
          "cluster_id": 1060443,
          "cite": [
            "55 S.W.3d 515",
            "2001 Tenn. LEXIS 658",
            "2001 WL 1035172"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex parte Argent",
          "cluster_id": 5284517,
          "cite": [
            "393 S.W.3d 781",
            "2013 WL 1136518",
            "2013 Tex. Crim. App. LEXIS 532"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raymond Anthony Miller v. Terry J. Harget",
          "cluster_id": 77447,
          "cite": [
            "458 F.3d 1251",
            "2006 U.S. App. LEXIS 19887",
            "2006 WL 2190555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
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
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'BOYLE v. State",
          "cluster_id": 2629952,
          "cite": [
            "2005 WY 83",
            "117 P.3d 401",
            "2005 Wyo. LEXIS 97",
            "2005 WL 1771001"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. Com.",
          "cluster_id": 1058715,
          "cite": [
            "639 S.E.2d 217",
            "273 Va. 26",
            "2007 Va. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sykes",
          "cluster_id": 1278169,
          "cite": [
            "2005 WI 48",
            "279 Wis. 2d 742",
            "695 N.W.2d 277",
            "2005 Wisc. LEXIS 155"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America v. Curtis Dennis Callarman",
          "cluster_id": 775859,
          "cite": [
            "273 F.3d 1284",
            "2001 U.S. App. LEXIS 26204",
            "2001 WL 1561112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chris Hartman v. Jeremy Thompson",
          "cluster_id": 4642062,
          "cite": [
            "931 F.3d 471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 1812472,
          "cite": [
            "2007 WI 32",
            "729 N.W.2d 182",
            "299 Wis. 2d 675",
            "2007 Wisc. LEXIS 33"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Damato v. State",
          "cluster_id": 2571711,
          "cite": [
            "2003 WY 13",
            "64 P.3d 700",
            "2003 WL 186628"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J & J Construction Co. v. Bricklayers & Allied Craftsmen, Local 1",
          "cluster_id": 848785,
          "cite": [
            "664 N.W.2d 728",
            "468 Mich. 722"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mikal Mahdi v. Bryan Stirling",
          "cluster_id": 5308013,
          "cite": [
            "20 F.4th 846"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Franklin",
          "cluster_id": 1225871,
          "cite": [
            "547 F.3d 726",
            "2008 U.S. App. LEXIS 22305",
            "2008 WL 4694937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Ex Rel. Appleby v. Recht",
          "cluster_id": 1309488,
          "cite": [
            "583 S.E.2d 800",
            "213 W. Va. 503"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. State",
          "cluster_id": 2335692,
          "cite": [
            "67 S.W.3d 582",
            "347 Ark. 788",
            "2002 Ark. LEXIS 128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arkansas v. Sullivan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2620699 OR 9795082 OR 9795083) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 119,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 119,
        "triage_read": 6,
        "triage_snippet_classified": 113
      },
      "lane2_top_cited": {
        "query": "cites:(2620699 OR 9795082 OR 9795083)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMSZzPTIyNTUzODcmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282620699+OR+9795082+OR+9795083%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2620699 OR 9795082 OR 9795083)",
        "reviewed": 7,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 7,
        "triage_read": 0,
        "triage_snippet_classified": 7
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2620699 OR 9795082 OR 9795083)",
    "indexed_citing_opinions": 156,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2620699,
        "count": 139,
        "count_source": "search"
      },
      {
        "opinion_id": 9795082,
        "count": 21,
        "count_source": "search"
      },
      {
        "opinion_id": 9795083,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 234,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arkansas-v-sullivan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2Njc4OSZzPTEwMDQ0Mjg1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%282620699+OR+9795082+OR+9795083%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2620699,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 111552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 1448404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620699,
        "cited_id": 1960847,
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
    "date_created": "2026-07-04T18:46:09Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:55:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:46:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arkansas v. Sullivan

```
<opinion type="majority">
<author id="b869-10">Per Curiam.</author>
<p id="b869-11">In November 1998, Officer Joe Taylor of the Conway, Arkansas, Police Department stopped respondent Sullivan for speeding and for having an improperly tinted windshield. Taylor approached Sullivan’s vehicle, explained the reason for the stop, and requested Sullivan’s license, regis<page-number citation-index="1" label="770">*770</page-number>tration, and insurance documentation. Upon seeing Sullivan’s license, Taylor realized that he was aware of “ ‘intelligence on [Sullivan] regarding narcotics.’ ” <span class="citation no-link">840 Ark. 318</span>-A, 318-B, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S.W. 3d 551, 552</a></span> (2000). When Sullivan opened his ear door in an (unsuccessful) attempt to locate his registration and insurance papers, Taylor noticed a rusted roofing hatchet on the ear’s floorboard. Taylor then arrested Sullivan for speeding, driving without his registration and insurance documentation, carrying a weapon (the roofing hatchet), and improper window tinting.</p>
<p id="b870-5">After another officer arrived and placed Sullivan in his squad car, Officer Taylor conducted an inventory search of Sullivan’s vehicle pursuant to the Conway Police Department’s Vehicle Inventory Policy. Under the vehicle’s armrest, Taylor discovered a bag containing a substance that appeared to him to be methamphetamine as well as numerous items of suspected drug paraphernalia. As a result of the detention and search, Sullivan was charged with various state-law drug offenses, unlawful possession of a weapon, and speeding.</p>
<p id="b870-6">Sullivan moved to suppress the evidence seized from his vehicle on the basis that his arrest was merely a “pretext and sham to search” him and, therefore, violated the Fourth and Fourteenth Amendments to the United States Constitution. Pet. for Cert. 3. The trial court granted the suppression motion and, on the State’s interlocutory appeal, the Arkansas Supreme Court affirmed. <span class="citation multiple-matches"><a href="/c/Ark./340/315/">340 Ark. 315</a></span>, <span class="citation multiple-matches"><a href="/c/S.W.%203d/11/526/">11 S.W. 3d 526</a></span> (2000). The State petitioned for rehearing, contending that the court had erred by taking into account Officer Taylor’s subjective motivation, in disregard of this Court’s opinion in <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U.S. 806</a></span> (1996). Over the dissent of three justices, the court rejected the State’s argument that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>makes “the ulterior motives of police officers . . . irrelevant so long as there is probable cause for the traffic stop” and denied the State’s rehearing petition. 340 Ark., at 318-B, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>.</p>
<p id="b871-4"><page-number citation-index="1" label="771">*771</page-number>The Arkansas Supreme Court declined to follow <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>on the ground that “much of it is <em>dicta.” </em>340 Ark., at 318-B, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>. The court reiterated the trial judge’s conclusion that “the arrest was pretextual and made for the purpose of searching Sullivan’s vehicle for evidence of a crime,” and observed that “we do not believe that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>disallows” suppression on such a basis. <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Id.,</a></span> </em>at 318-C, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>. Finally, the court asserted that, even if it were to conclude that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>precludes inquiry into an arresting officer’s subjective motivation, “there is nothing that prevents this court from interpreting the U. S. Constitution more broadly than the United States Supreme Court, which has the effect of providing more rights.” 340 Ark., at 318-C, <span class="citation" data-id="1448404"><a href="/opinion/1448404/state-v-sullivan/#552" aria-description="Citation for case: State v. Sullivan">16 S. W. 3d, at 552</a></span>.</p>
<p id="b871-5">Because the Arkansas Supreme Court’s decision on rehearing is flatly contrary to this Court’s controlling precedent, we grant the State’s petition for a writ of certiorari and reverse.<footnotemark>*</footnotemark> As an initial matter, we note that the Arkansas Supreme Court never questioned Officer Taylor’s authority to arrest Sullivan for a fine-only traffic violation (speeding), and rightly so. See <em>Atwater </em>v. <em>Lago Vista, ante, </em>p. 318. Rather, the court affirmed the trial judge’s suppression of the drug-related evidence on the theory that Officer Taylor’s arrest of Sullivan, although supported by probable cause, nonetheless violated the Fourth Amendment because Taylor had an improper subjective motivation for making the stop. The Arkansas Supreme Court’s holding to that effect cannot be squared with our decision in <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>, </em>in which we noted our “vmwilling[ness] to entertain Fourth Amendment challenges based on the actual motivations of individual officers,” <page-number citation-index="1" label="772">*772</page-number>and held unanimously that “[sjubjective intentions play no role in ordinary, probable-cause Fourth Amendment analysis.” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U.S., at 813</a></span>. That <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>involved a traffic stop, rather than a custodial arrest, is of no particular moment; indeed, <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>itself relied on <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U.S. 218</a></span> (1973), for the proposition that “a traffic-violation arrest . . . [will] not be rendered invalid by the fact that it was ‘a mere pretext for a narcotics search.’ ” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States">517 U. S., at 812-813</a></span>.</p>
<p id="b872-5">The Arkansas Supreme Court’s alternative holding, that it may interpret the United States Constitution to provide greater protection than this Court’s own federal constitutional precedents provide, is foreclosed by <em>Oregon </em>v. <em>Hass, </em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">420 U.S. 714</a></span> (1975). There, we observed that the Oregon Supreme Court’s statement that it could “‘interpret the Fourth Amendment more restrietively than interpreted by the United States Supreme Court’” was “not the law and surely must be an inadvertent error.” <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass"><em>Id., </em>at 719, n. 4</a></span>. We reiterated in <em><span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/" aria-description="Citation for case: Oregon v. Hass">Hass</a></span> </em>that while “a State is free <em>as a matter of its own law </em>to impose greater restrictions on police activity than those this Court holds to be necessary upon federal constitutional standards,” it “may not impose such greater restrictions as a matter of <em>federal constitutional law </em>when this Court specifically refrains from imposing them.” <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass"><em>Id., </em>at 719</a></span>.</p>
<p id="b872-6">The judgment of the Arkansas Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b872-7">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b871-6"> Sullivan’s motion for leave to proceed <em>informa pauperis </em>is granted. We have jurisdiction under <span class="citation no-link">28 U. S. C. § 1257</span> notwithstanding the absence of final judgment in the underlying prosecution. See <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#651" aria-description="Citation for case: New York v. Quarles">467 U.S. 649, 651, n. 1</a></span> (1984) (“[S]hould the State convict respondent at trial, its claim that certain evidence was wrongfully suppressed will be moot. Should respondent be acquitted at trial, the State will be precluded from pressing its federal claim again on appeal”).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Ashcraft v. Tennessee.md  (`case`, 5 assertions)

### content_page

```
---
title: "Ashcraft v. Tennessee"
type: case
citation: "322 U.S. 143 (1944)"
parallel_cite: "64 S. Ct. 921; 88 L. Ed. 1192"
neutral_cite: 1944 U.S. LEXIS 782
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1944
date_decided: 1944-05-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1944-05-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ashcraft v. Tennessee
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/103981/ashcraft-v-tennessee/"
  cluster_id: 103981
  opinion_id: 103981
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "due-process", "confessions", "voluntariness", "interrogation"]
holding: "Thirty-six hours of continuous, relay interrogation without sleep is \"inherently coercive,\" rendering the resulting confession…"
lake:
  record_id: Ashcraft v. Tennessee
  status: verified
  projected_at: 2026-07-09
---

# Ashcraft v. Tennessee

*322 U.S. 143 (1944)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Ashcraft was suspected of arranging his wife's murder. Police held him in custody and questioned him for thirty-six hours straight — incommunicado, without sleep or rest, by relays of experienced investigators and lawyers under electric lights. He denied involvement throughout but allegedly confessed at the end. The confession was the principal evidence at his murder trial, and he was convicted.

## Issue
Whether a confession obtained after thirty-six hours of continuous, incommunicado interrogation by relays of officers, without rest or sleep, can be deemed voluntary — or whether such interrogation is inherently coercive so that the resulting confession violates Fourteenth Amendment due process.

## Rule
Such prolonged, relentless interrogation is inherently coercive and yields an involuntary confession: "We think a situation such as that here shown by uncontradicted evidence is so inherently coercive that its very existence is irreconcilable with the possession of mental freedom by a lone suspect against whom its full coercive force is brought to bear." — 322 U.S. at 154. ^pin-154

"The Constitution of the United States stands as a bar against the conviction of any individual in an American court by means of a coerced confession." — [*Id.* at 155](https://www.courtlistener.com/opinion/103981/ashcraft-v-tennessee/#:~:text=The%20Constitution%20of%20the%20United). ^pin-155

## Application
Ashcraft was interrogated for thirty-six hours without rest or sleep, held incommunicado, by relays of officers and lawyers — a situation the Court found inherently coercive and irreconcilable with the mental freedom of a lone suspect. On these facts the resulting confession could not be treated as voluntary, and its use to convict him violated due process.

## Conclusion
The confession was the product of inherently coercive interrogation and could not support the conviction; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Ashcraft* is a foundational due-process voluntariness decision establishing that prolonged, relentless custodial interrogation can be inherently coercive. The voluntariness inquiry later settled into a totality-of-the-circumstances test that requires coercive police activity (see [[Colorado v. Connelly]]), and custodial interrogation acquired separate procedural safeguards under *[[Miranda v. Arizona|Miranda]]*.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*

## Sources
- *Ashcraft v. Tennessee*, 322 U.S. 143 (1944) — https://www.courtlistener.com/opinion/103981/ashcraft-v-tennessee/ — pinpoints: 154, 155.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "06c7a4c3da29a76c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "322 U.S. 143 (1944)", "court": "U.S. Supreme Court", "neutral_cite": "1944 U.S. LEXIS 782", "official_citation_present": true, "parallel_cite": "64 S. Ct. 921; 88 L. Ed. 1192", "title": "Ashcraft v. Tennessee", "year": "1944"}}
{"assertion_id": "e3d0c65d7aa6c68d", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Anchor", "title": "Ashcraft v. Tennessee"}}
{"assertion_id": "f9ca138a20f8bb75", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Thirty-six hours of continuous, relay interrogation without sleep is \\\"inherently coercive,\\\" rendering the resulting confession…", "title": "Ashcraft v. Tennessee"}}
{"assertion_id": "6421319d2eee8fc3", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1944-05-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Ashcraft v. Tennessee", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Ashcraft v. Tennessee", "varies_by_point": "false"}}
{"assertion_id": "f6dd6553739f12db", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Ashcraft v. Tennessee"}}
```

### lake record — Ashcraft v. Tennessee

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ashcraft v. Tennessee",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ashcraft v. Tennessee",
    "case_name_short": "Ashcraft",
    "case_name_full": "ASHCRAFT Et Al. v. TENNESSEE",
    "input_case_name": "Ashcraft v. Tennessee",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1944-05-01",
    "year": 1944,
    "docket": null,
    "cluster_id": 103981,
    "lead_opinion_id": 103981,
    "sibling_ids": [
      103981,
      9419494,
      9419495
    ],
    "absolute_url": "/opinion/103981/ashcraft-v-tennessee/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "322 U.S. 143",
      "volume": "322",
      "reporter": "U.S.",
      "page": "143",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "64 S. Ct. 921",
        "volume": "64",
        "reporter": "S. Ct.",
        "page": "921",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 1192",
        "volume": "88",
        "reporter": "L. Ed.",
        "page": "1192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1944 U.S. LEXIS 782",
        "volume": "1944",
        "reporter": "U.S. LEXIS",
        "page": "782",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "322 U.S. 143",
        "volume": "322",
        "reporter": "U.S.",
        "page": "143",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "64 S. Ct. 921",
        "volume": "64",
        "reporter": "S. Ct.",
        "page": "921",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 1192",
        "volume": "88",
        "reporter": "L. Ed.",
        "page": "1192",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1944 U.S. LEXIS 782",
        "volume": "1944",
        "reporter": "U.S. LEXIS",
        "page": "782",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "322 U.S. 143",
    "official_selection": {
      "court_class": "scotus",
      "selected": "322 U.S. 143",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-154",
      "page": null,
      "quote": "--- # Ashcraft v. Tennessee *322 U.S. 143 (1944)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Ashcraft was suspected of arranging his wife's murder. Police held him in custody and questioned him for thirty-six hours straight \u2014 incommunicado, without sleep or rest, by relays of experienced investigators and lawyers under electric lights. He denied involvement throughout but allegedly confessed at the end. The confession was the principal evidence at his murder trial, and he was convicted. ## Issue Whether a confession obtained after thirty-six hours of continuous, incommunicado interrogation by relays of officers, without rest or sleep, can be deemed voluntary \u2014 or whether such interrogation is inherently coercive so that the resulting confession violates Fourteenth Amendment due process. ## Rule Such prolonged, relentless interrogation is inherently coercive and yields an involuntary confession:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-155",
      "page": null,
      "quote": "The Constitution of the United States stands as a bar against the conviction of any individual in an American court by means of a coerced confession.",
      "star_marker": "155",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15902,
      "fragment": "#:~:text=The%20Constitution%20of%20the%20United",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1944-05-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ashcraft v. Tennessee",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Charley B. Haswood",
          "cluster_id": 784327,
          "cite": [
            "350 F.3d 1024",
            "2003 Cal. Daily Op. Serv. 10282",
            "62 Fed. R. Serv. 1478",
            "2003 U.S. App. LEXIS 24181",
            "2003 WL 22833048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarez",
          "cluster_id": 156277,
          "cite": [
            "142 F.3d 1243",
            "1998 Colo. J. C.A.R. 2038",
            "1998 U.S. App. LEXIS 8245",
            "1998 WL 207912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cahill",
          "cluster_id": 1244769,
          "cite": [
            "853 P.2d 1037",
            "5 Cal. 4th 478",
            "20 Cal. Rptr. 2d 582",
            "93 Daily Journal DAR 8304",
            "93 Cal. Daily Op. Serv. 4902",
            "1993 Cal. LEXIS 3087"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte McCary",
          "cluster_id": 1793877,
          "cite": [
            "528 So. 2d 1133",
            "1988 WL 10157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerry Lane Jurek v. W. J. Estelle, Jr., Director, Texas Department of Corrections, Respondent",
          "cluster_id": 379222,
          "cite": [
            "623 F.2d 929",
            "1980 U.S. App. LEXIS 14967"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard A. Schmidt",
          "cluster_id": 354373,
          "cite": [
            "573 F.2d 1057"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Anderson",
          "cluster_id": 5682513,
          "cite": [
            "42 N.Y.2d 35",
            "364 N.E.2d 1318",
            "396 N.Y.S.2d 625",
            "1977 N.Y. LEXIS 2096"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Lee Thomas v. State of North Carolina and Mr. Bill Mahoney, Superintendent",
          "cluster_id": 298888,
          "cite": [
            "447 F.2d 1320",
            "1971 U.S. App. LEXIS 8130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miranda v. Arizona",
          "cluster_id": 107252,
          "cite": [
            "16 L. Ed. 2d 694",
            "86 S. Ct. 1602",
            "384 U.S. 436",
            "1966 U.S. LEXIS 2817",
            "10 Ohio Misc. 9",
            "36 Ohio Op. 2d 237",
            "10 A.L.R. 3d 974"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Denno",
          "cluster_id": 106881,
          "cite": [
            "12 L. Ed. 2d 908",
            "84 S. Ct. 1774",
            "378 U.S. 368",
            "1964 U.S. LEXIS 826",
            "1 A.L.R. 3d 1205",
            "28 Ohio Op. 2d 177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Escobedo v. Illinois",
          "cluster_id": 106883,
          "cite": [
            "12 L. Ed. 2d 977",
            "84 S. Ct. 1758",
            "378 U.S. 478",
            "1964 U.S. LEXIS 827",
            "4 Ohio Misc. 197",
            "32 Ohio Op. 2d 31"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Napue v. Illinois",
          "cluster_id": 105912,
          "cite": [
            "3 L. Ed. 2d 1217",
            "79 S. Ct. 1173",
            "360 U.S. 264",
            "1959 U.S. LEXIS 811"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hernandez v. New York",
          "cluster_id": 112601,
          "cite": [
            "114 L. Ed. 2d 395",
            "111 S. Ct. 1859",
            "500 U.S. 352",
            "1991 U.S. LEXIS 2913"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111779,
          "cite": [
            "93 L. Ed. 2d 473",
            "107 S. Ct. 515",
            "479 U.S. 157",
            "1986 U.S. LEXIS 23",
            "55 U.S.L.W. 4043"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malloy v. Hogan",
          "cluster_id": 106862,
          "cite": [
            "12 L. Ed. 2d 653",
            "84 S. Ct. 1489",
            "378 U.S. 1",
            "1964 U.S. LEXIS 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michel v. Louisiana",
          "cluster_id": 105333,
          "cite": [
            "100 L. Ed. 2d 83",
            "76 S. Ct. 158",
            "350 U.S. 91",
            "1955 U.S. LEXIS 37"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Screws v. United States",
          "cluster_id": 104135,
          "cite": [
            "325 U.S. 91",
            "65 S. Ct. 1031",
            "89 L. Ed. 1495",
            "1945 U.S. LEXIS 2096",
            "162 A.L.R. 1330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
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
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shelley v. Kraemer",
          "cluster_id": 104545,
          "cite": [
            "92 L. Ed. 2d 1161",
            "68 S. Ct. 836",
            "334 U.S. 1",
            "1948 U.S. LEXIS 2764",
            "3 A.L.R. 2d 441",
            "92 L. Ed. 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Culombe v. Connecticut",
          "cluster_id": 106284,
          "cite": [
            "6 L. Ed. 2d 1037",
            "81 S. Ct. 1860",
            "367 U.S. 568",
            "1961 U.S. LEXIS 811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garrity v. New Jersey",
          "cluster_id": 107336,
          "cite": [
            "17 L. Ed. 2d 562",
            "87 S. Ct. 616",
            "385 U.S. 493",
            "1967 U.S. LEXIS 2882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haynes v. Washington",
          "cluster_id": 106625,
          "cite": [
            "10 L. Ed. 2d 513",
            "83 S. Ct. 1336",
            "373 U.S. 503",
            "1963 U.S. LEXIS 1439"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacobellis v. Ohio",
          "cluster_id": 106877,
          "cite": [
            "12 L. Ed. 2d 793",
            "84 S. Ct. 1676",
            "378 U.S. 184",
            "1964 U.S. LEXIS 822",
            "28 Ohio Op. 2d 101"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blackburn v. Alabama",
          "cluster_id": 105977,
          "cite": [
            "4 L. Ed. 2d 242",
            "80 S. Ct. 274",
            "361 U.S. 199",
            "1960 U.S. LEXIS 1766"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spano v. New York",
          "cluster_id": 105917,
          "cite": [
            "3 L. Ed. 2d 1265",
            "79 S. Ct. 1202",
            "360 U.S. 315",
            "1959 U.S. LEXIS 751"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haley v. Ohio",
          "cluster_id": 104491,
          "cite": [
            "92 L. Ed. 2d 224",
            "68 S. Ct. 302",
            "332 U.S. 596",
            "1948 U.S. LEXIS 2643"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. North Carolina",
          "cluster_id": 107261,
          "cite": [
            "16 L. Ed. 2d 895",
            "86 S. Ct. 1761",
            "384 U.S. 737",
            "1966 U.S. LEXIS 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcraft v. Tennessee:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(103981 OR 9419494 OR 9419495) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00NjkxNTIwMDAwMCZzPTIzNzQwODkmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28103981+OR+9419494+OR+9419495%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(103981 OR 9419494 OR 9419495)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NDcmcz0xMDQ0NTUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28103981+OR+9419494+OR+9419495%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(103981 OR 9419494 OR 9419495)",
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
    "complete_query": "cites:(103981 OR 9419494 OR 9419495)",
    "indexed_citing_opinions": 436,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 103981,
        "count": 407,
        "count_source": "search"
      },
      {
        "opinion_id": 9419494,
        "count": 42,
        "count_source": "search"
      },
      {
        "opinion_id": 9419495,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 693,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ashcraft-v-tennessee.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU4MTUzNTgmcz02MjQxNzczJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28103981+OR+9419494+OR+9419495%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 103981,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 101593,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 102408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 103974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 1322156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 1545293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 103981,
        "cited_id": 3891773,
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
    "date_created": "2026-07-04T18:55:02Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:55:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:55:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:06:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:55:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ashcraft v. Tennessee

```
<div>
<center><b><span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U.S. 143</a></span> (1944)</b></center>
<center><h1>ASHCRAFT ET AL.<br>
v.<br>
TENNESSEE.</h1></center>
<center>No. 391.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 28, 1944.</center>
<center>Decided May 1, 1944.</center>
CERTIORARI TO THE SUPREME COURT OF TENNESSEE.
<p><span class="star-pagination">*144</span> <i>Messrs. James F. Bickers</i> and <i>Grover N. McCormick</i> for petitioners.</p>
<p><i>Mr. Nat Tipton,</i> with whom <i>Mr. Roy H. Beeler,</i> Attorney General of Tennessee, was on the brief, for respondent.</p>
<p>MR. JUSTICE BLACK delivered the opinion of the Court.</p>
<p>About three o'clock on the morning of Thursday, June 5, 1941, Mrs. Zelma Ida Ashcraft got in her automobile at her home in Memphis, Tennessee, and set out on a trip to visit her mother's home in Kentucky. Late in the afternoon of the same day, her car was observed a few miles out of Memphis, standing on the wrong side of a road which she would likely have taken on her journey. Just off the road, in a slough, her lifeless body was found. On her head were cut places inflicted by blows sufficient to have caused her death. Petitioner Ware, age 20, a Negro, was indicted in a state court and found guilty of her murder. Petitioner Ashcraft, age 45, a white man, husband of the deceased, charged with having hired Ware to commit the murder, was tried jointly with Ware and convicted as an accessory before the fact. Both were sentenced to ninety-nine years in the state penitentiary. <span class="star-pagination">*145</span> The Supreme Court of Tennessee affirmed the convictions.</p>
<p>In applying to us for certiorari, Ware and Ashcraft urged that alleged confessions were used at their trial which had been extorted from them by state law enforcement officers in violation of the Fourteenth Amendment, and that "solely and alone" on the basis of these confessions they had been convicted. Their contentions raised a federal question which the record showed to be substantial and we brought both cases here for review. Upon oral argument before this Court Tennessee's legal representatives conceded that the convictions could not be sustained without the confessions but defended their use upon the ground that they were not compelled but were "freely and voluntarily made."</p>
<p>The record discloses that neither the trial court nor the Tennessee Supreme Court actually held as a matter of fact that petitioners' confessions were "freely and voluntarily made." The trial court heard evidence on the issue out of the jury's hearing, but did not itself determine from that evidence that the confessions were voluntary. Instead it overruled Ashcraft's objection to the use of his alleged confession with the statement that, "This Court is not able to hold, as a matter of law, that reasonable minds might not differ on the question of whether or not that alleged confession was voluntarily obtained." And it likewise overruled Ware's objection to use of his alleged confession, stating that "the reasonable minds of twelve men might . . . differ as to . . . whether Ware's confession was voluntary, and . . . therefore, that is a question of fact for the jury to pass on."<sup>[1]</sup> Nor did the <span class="star-pagination">*146</span> State Supreme Court review the evidence pertaining to the confessions and affirmatively hold them voluntary. In sustaining the petitioners' convictions, one Justice dissenting, it went no further than to point out that, "The trial judge . . . held . . . he could not say that the confessions were not voluntarily made and, therefore, permitted them to go to the jury," and to declare that it, likewise, was "unable to say that the confessions were not freely and voluntarily made."<sup>[2]</sup></p>
<p>If, therefore, the question of the voluntariness of the two confessions was actually decided at all it was by the jury. And the jury was charged generally on the subject of the two confessions as follows:</p>
<p>"I further charge you that if verbal or written statements made by the defendants freely and voluntarily and without fear of punishment or hope of reward, have been proven to you in this case, you may take them into consideration with all of the other facts and circumstances in the case. . . . In statements made at the time of the arrest, you may take into consideration the condition of the minds of the prisoners owing to their arrest and <span class="star-pagination">*147</span> whether they were influenced by motives of hope or fear, to make the statements. Such a statement is competent evidence against the defendant who makes it and is not competent evidence against the other defendant . . . You cannot consider it for any purpose against the other defendant."</p>
<p>Concerning Ashcraft's alleged confession this general charge constituted the sole instruction to the jury.<sup>[3]</sup> But with regard to Ware's alleged confession the jury further was instructed:</p>
<p>"It is his [Ware's] further theory that he was induced by the fear of violence at the hands of a mob and by fear of the officers of the law to confess his guilt of the crime charged against him, but that such confession was false and that he had nothing whatsoever to do with, and no knowledge of the alleged crime. If you believe the theory of the defendant, Ware, . . . it is your duty to acquit him."</p>
<p>Having submitted the two alleged confessions to the jury in this manner, the trial court instructed the jury that: "What the proof may show you, if anything, that the defendants have said against themselves, the law presumes to be true, but anything the defendants have said in their own behalf, you are not obliged to believe. . . ."</p>
<p>This treatment of the confessions by the two state courts, the manner of the confessions' submission to the jury, and the emphasis upon the great weight to be given confessions make all the more important the kind of "independent examination" of petitioners' claims which, in <span class="star-pagination">*148</span> any event, we are bound to make. <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#237" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 237-238</a></span>. Our duty to make that examination could not have been "foreclosed by the finding of a court, or the verdict of a jury, or both." <i><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">Id.</a></span></i> We proceed therefore to consider the evidence relating to the circumstances out of which the alleged confessions came.</p>
<p><i>First, as to Ashcraft.</i> Ashcraft was born on an Arkansas farm. At the age of eleven he left the farm and became a farm hand working for others. Years later he gravitated into construction work, finally becoming a skilled dragline and steam-shovel operator. Uncontradicted evidence in the record was that he had acquired for himself "an excellent reputation." In 1929 he married the deceased Zelma Ida Ashcraft. Childless, they accumulated, apparently through Ashcraft's earnings, a very modest amount of jointly held property including bank accounts and an equity in the home in which they lived. The Supreme Court of Tennessee found "nothing to show but what the home life of Ashcraft and the deceased was pleasant and happy." Several of Mrs. Ashcraft's friends who were guests at the Ashcraft home on the night before her tragic death testified that both husband and wife appeared to be in a happy frame of mind.</p>
<p>The officers first talked to Ashcraft about 6 P.M. on the day of his wife's murder as he was returning home from work. Informed by them of the tragedy, he was taken to an undertaking establishment to identify her body which previously had been identified only by a driver's license. From there he was taken to the county jail where he conferred with the officers until about 2 A.M. No clues of ultimate value came from this conference, though it did result in the officers' holding and interrogating the Ashcrafts' maid and several of her friends. During the following week the officers made extensive investigations in Ashcraft's neighborhood and <span class="star-pagination">*149</span> elsewhere and further conferred with Ashcraft himself on several occasions, but none of these activities produced tangible evidence pointing to the identity of the murderer.</p>
<p>Then, early in the evening of Saturday, June 14, the officers came to Ashcraft's home and "took him into custody." In the words of the Tennessee Supreme Court,</p>
<p>"They took him to an office or room on the northwest corner of the fifth floor of the Shelby County jail. This office is equipped with all sorts of crime and detective devices such as a fingerprint outfit, cameras, high-powered lights, and such other devices as might be found in a homicide investigating office. . .. It appears that the officers placed Ashcraft at a table in this room on the fifth floor of the county jail with a light over his head and began to quiz him. They questioned him in relays until the following Monday morning, June 16, 1941, around ninethirty or ten o'clock. It appears that Ashcraft from Saturday evening at seven o'clock until Monday morning at approximately nine-thirty never left this homicide room on the fifth floor."<sup>[4]</sup></p>
<p>Testimony of the officers shows that the reason they questioned Ashcraft "in relays" was that they became so tired they were compelled to rest. But from 7:00 Saturday evening until 9:30 Monday morning Ashcraft had no rest. One officer did say that he gave the suspect a single five minutes' respite, but except for this five minutes the procedure consisted of one continuous stream of questions.</p>
<p>As to what happened in the fifth-floor jail room during this thirty-six hour secret examination the testimony <span class="star-pagination">*150</span> follows the usual pattern and is in hopeless conflict.<sup>[5]</sup> Ashcraft swears that the first thing said to him when he was taken into custody was, "Why in hell did you kill your wife?"; that during the course of the examination he was threatened and abused in various ways; and that as the hours passed his eyes became blinded by a powerful electric light, his body became weary, and the strain on his nerves became unbearable.<sup>[6]</sup> The officers, on the other hand, swear that throughout the questioning they were kind and considerate. They say that they did not accuse Ashcraft of the murder until four hours after he was brought to the jail building, though they freely admit that from that time on their barrage of questions was constantly directed at him on the assumption that he was <span class="star-pagination">*151</span> the murderer. Together with other persons whom they brought in on Monday morning to witness the culmination of the thirty-six hour ordeal the officers declare that at that time Ashcraft was "cool," "calm," "collected," "normal"; that his vision was unimpaired and his eyes not bloodshot; and that he showed no outward signs of being tired or sleepy.</p>
<p>As to whether Ashcraft actually confessed, there is a similar conflict of testimony. Ashcraft maintains that although the officers incessantly attempted by various tactics of intimidation to entrap him into a confession, not once did he admit knowledge concerning or participation in the crime. And he specifically denies the officers' statements that he accused Ware of the crime, insisting that in response to their questions he merely gave them the name of Ware as one of several men who occasionally had ridden with him to work. The officers' version of what happened, however, is that about 11 P.M. on Sunday night, after twenty-eight hours' constant questioning, Ashcraft made a statement that Ware had overpowered him at his home and abducted the deceased, and was probably the killer. About midnight the officers found Ware and took him into custody, and, according to their testimony, Ware made a self-incriminating statement as of early Monday morning, and at 5:40 A.M. signed by mark a written confession in which appeared the statement that Ashcraft had hired him to commit the murder. This alleged confession of Ware was read to Ashcraft about six o'clock Monday morning, whereupon Ashcraft is said substantially to have admitted its truth in a detailed statement taken down by a reporter. About 9:30 Monday morning a transcript of Ashcraft's purported statement was read to him. The State's position is that he affirmed its truth but refused to sign the transcript, saying that he first wanted to consult his lawyer. As to <span class="star-pagination">*152</span> this latter 9:30 episode the officers' testimony is reinforced by testimony of the several persons whom they brought in to witness the end of the examination.</p>
<p>In reaching our conclusion as to the validity of Ashcraft's confession we do not resolve any of the disputed questions of fact relating to the details of what transpired within the confession chamber of the jail or whether Ashcraft actually did confess.<sup>[7]</sup> Such disputes, we may say, are an inescapable consequence of secret inquisitorial practices. And always evidence concerning the inner details of secret inquisitions<sup>[8]</sup> is weighted against an accused, <span class="star-pagination">*153</span> particularly where, as here, he is charged with a brutal crime, or where, as in many other cases, his supposed offense bears relation to an unpopular economic, political, or religious cause.</p>
<p>Our conclusion is that if Ashcraft made a confession it was not voluntary but compelled. We reach this conclusion from facts which are not in dispute at all. Ashcraft, a citizen of excellent reputation, was taken into custody by police officers. Ten days' examination of the Ashcrafts' maid, and of several others, in jail where they were held, had revealed nothing whatever against Ashcraft. Inquiries among his neighbors and business associates likewise had failed to unearth one single tangible clue pointing to his guilt. For thirty-six hours after Ashcraft's seizure during which period he was held incommunicado, without sleep or rest, relays of officers, experienced investigators, and highly trained lawyers questioned him without respite. From the beginning of the questioning at 7 o'clock on Saturday evening until 6 o'clock on Monday morning Ashcraft denied that he had anything to do with the murder of his wife. And at a hearing <span class="star-pagination">*154</span> before a magistrate about 8:30 Monday morning Ashcraft pleaded not guilty to the charge of murder which the officers had sought to make him confess during the previous thirty-six hours.</p>
<p>We think a situation such as that here shown by uncontradicted evidence is so inherently coercive that its very existence is irreconcilable with the possession of mental freedom by a lone suspect against whom its full coercive force is brought to bear.<sup>[9]</sup> It is inconceivable that any court of justice in the land, conducted as our courts are, open to the public, would permit prosecutors serving in relays to keep a defendant witness under continuous cross-examination for thirty-six hours without rest or sleep in an effort to extract a "voluntary" confession. Nor can we, consistently with Constitutional due process of law, hold voluntary a confession where prosecutors do the same thing away from the restraining influences of a public trial in an open court room.<sup>[10]</sup></p>
<p><span class="star-pagination">*155</span> The Constitution of the United States stands as a bar against the conviction of any individual in an American court by means of a coerced confession.<sup>[11]</sup> There have been, and are now, certain foreign nations with governments dedicated to an opposite policy: governments which convict individuals with testimony obtained by police organizations possessed of an unrestrained power to seize persons suspected of crimes against the state, hold them in secret custody, and wring from them confessions by physical or mental torture. So long as the Constitution remains the basic law of our Republic, America will not have that kind of government.</p>
<p><i>Second, as to Ware.</i> Ashcraft and Ware were jointly tried, and were convicted on the theory that Ashcraft hired Ware to perform the murder. Ware's conviction was sustained by the Tennessee Supreme Court on the assumption that Ashcraft's confession was properly admitted and his conviction valid. Whether it would have been sustained had the court reached the conclusion we have reached as to Ashcraft we cannot know. Doubt as to what the state court would have done under the changed <span class="star-pagination">*156</span> circumstances brought about by our reversal of its decision as to Ashcraft is emphasized by the position of the State's representatives in this Court. They have asked that if we reverse Ashcraft's conviction we also reverse Ware's.</p>
<p>In disposing of cases before us it is our responsibility to make such disposition as justice may require. "And in determining what justice does require, the Court is bound to consider any change, either in fact or in law, which has supervened since the judgment was entered." <i>Patterson</i> v. <i>Alabama,</i> <span class="citation" data-id="102408"><a href="/opinion/102408/patterson-v-alabama/#607" aria-description="Citation for case: Patterson v. Alabama">294 U.S. 600, 607</a></span>; <i>State Tax Commission</i> v. <i>Van Cott,</i> <span class="citation" data-id="103175"><a href="/opinion/103175/state-tax-commission-v-van-cott/#515" aria-description="Citation for case: State Tax Commission v. Van Cott">306 U.S. 511, 515-516</a></span>. Application of this guiding principle to the case at hand requires that we send Ware's case back to the Tennessee Supreme Court. Should that Court in passing on Ware's conviction in the light of our ruling as to Ashcraft adopt the State Attorney General's view and reverse the conviction there then would be no occasion for our passing on the federal question here raised by Ware. Under these circumstances we vacate the judgment of the Tennessee Supreme Court affirming Ware's conviction, and remand his case to that Court for further proceedings.</p>
<p>The judgment affirming Ashcraft's conviction is reversed and the cause is remanded to the Supreme Court of Tennessee for proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE JACKSON, dissenting:</p>
<p>A sovereign State is now before us, summoned on the charge that it has obtained convictions by methods so unfair that a federal court must set aside what the state courts have done. Heretofore the State has had the benefit of a presumption of regularity and legality. A confession made by one in custody heretofore has been <span class="star-pagination">*157</span> admissible in evidence unless it was proved and found that it was obtained by pressures so strong that it was <i>in fact</i> involuntarily made, that the individual will of the particular confessor had been overcome by torture, mob violence, fraud, trickery, threats, or promises. Even where there was excess and abuse of power on the part of officers, the State still was entitled to use the confession if upon examination of the whole evidence it was found to negative the view that the accused had "so lost his freedom of action that the statements made were not his but were the result of the deprivation of his free choice to admit, to deny, or to refuse to answer." <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 241</a></span>.</p>
<p>In determining these issues of fact, respect for the sovereign character of the several States always has constrained this Court to give great weight to findings of fact of state courts. While we have sometimes gone back of state court determinations to make sure whether the guaranties of the Fourteenth Amendment have or have not been violated, in close cases the decisions of state courts have often been sufficient to tip the scales in favor of affirmance. <i>Lisenba</i> v. <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#238" aria-description="Citation for case: Lisenba v. California"><i>California, supra,</i> 238, 239</a></span>; <i>Buchalter</i> v. <i>New York,</i> <span class="citation" data-id="103850"><a href="/opinion/103850/buchalter-v-new-york/#431" aria-description="Citation for case: Buchalter v. New York">319 U.S. 427, 431</a></span>; cf. <i>Milk Wagon Drivers Union</i> v. <i>Meadowmoor Dairies,</i> <span class="citation" data-id="9419143"><a href="/opinion/103459/milk-wagon-drivers-union-local-753-v-meadowmoor-dairies-inc/#294" aria-description="Citation for case: Milk Wagon Drivers Union, Local 753 v. Meadowmoor...">312 U.S. 287, 294</a></span>.</p>
<p>As we read the present decision the Court in effect declines to apply these well-established principles. Instead, it: (1) substitutes for determination on conflicting evidence the question whether this confession was actually produced by coercion, a presumption that it was, on a new doctrine that examination in custody of this duration is "inherently coercive"; (2) it makes that presumption irrebuttable  i.e., a rule of law  because, while it goes back of the state decisions to find certain facts, it refuses to resolve conflicts in evidence to determine whether other of <span class="star-pagination">*158</span> the State's proof is sufficient to overcome such presumption; and, in so doing, (3) it sets aside the findings by the courts of Tennessee that on all the facts this confession did not result from coercion, either giving those findings no weight or regarding them as immaterial.</p>
<p>We must bear in mind that this case does not come here from a lower federal court over whose conduct we may assert a general supervisory power. If it did, we should be at liberty to apply rules as to the admissibility of confessions, based on our own conception of permissible procedure, and in which we may embody restrictions even greater than those imposed upon the States by the Fourteenth Amendment. See <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U.S. 532</a></span>; <i>Wan</i> v. <i>United States,</i> <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U.S. 1</a></span>; <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#341" aria-description="Citation for case: McNabb v. United States">318 U.S. 332, 341</a></span>; <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9419486"><a href="/opinion/103974/united-states-v-mitchell/" aria-description="Citation for case: United States v. Mitchell">322 U.S. 65</a></span>. But we have no such supervisory power over state courts. We may not lay down rules of evidence for them nor revise their decisions merely because we feel more confidence in our own wisdom and rectitude. We have no power to discipline the police or law-enforcement officers of the State of Tennessee nor to reverse its convictions in retribution for conduct which we may personally disapprove.</p>
<p>The burden of protecting society from most crimes against persons and property falls upon the State. Different States have different crime problems and some freedom to vary procedures according to their own ideas. Here, a State was forced by an unwitnessed and baffling murder to vindicate its law and protect its society. To nullify its conviction in this particular case upon a consideration of all the facts would be a delicate exercise of federal judicial power. But to go beyond this, as the Court does today, and divine in the due process clause of the Fourteenth Amendment an exclusion of confessions on an irrebuttable presumption that custody and examination are "inherently coercive" if of some unspecified duration within <span class="star-pagination">*159</span> thirty-six hours, requires us to make more than a passing expression of our doubts and disagreements.</p>
<p></p>
<h2>I.</h2>
<p>The claim of a suspect to immunity from questioning creates one of the most vexing problems in criminal law  that branch of the law which does the courts and the legal profession least credit. The consequences upon society of limiting examination of persons out of court cannot fairly be appraised without recognition of the advantage criminals already enjoy in immunity from compulsory examination in court. Of this latter Mr. Justice Cardozo, for an all but unanimous Court, said: "This too might be lost, and justice still be done. Indeed, today as in the past there are students of our penal system who look upon the immunity as a mischief rather than a benefit, and who would limit its scope, or destroy it altogether. No doubt there would remain the need to give protection against torture, physical or mental." <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U.S. 319, 325-26</a></span>.</p>
<p>This Court never yet has held that the Constitution denies a State the right to use a confession just because the confessor was questioned in custody where it did not also find other circumstances that deprived him of a "free choice to admit, to deny, or to refuse to answer." <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 241</a></span>. The Constitution requires that a conviction rest on a fair trial. Forced confessions are ruled out of a fair trial. They are ruled out because they have been wrung from a prisoner by measures which are offensive to concepts of fundamental fairness. Different courts have used different terms to express the test by which to judge the inadmissibility of a confession, such as "forced," "coerced," "involuntary," "extorted," "loss of freedom of will." But always where we have professed to speak with the voice of the due process clause, the test, in whatever words stated, has been <span class="star-pagination">*160</span> applied to the particular confessor at the time of confession.</p>
<p>It is for this reason that American courts hold almost universally and very properly that a confession obtained during or shortly after the confessor has been subjected to brutality, torture, beating, starvation, or physical pain of any kind is <i>prima facie</i> "involuntary." The effect of threats alone may depend more on individual susceptibility to fear. But men are so constituted that many will risk the postponed consequences of yielding to a demand for a confession in order to be rid of present or imminent physical suffering. Actual or threatened violence have no place in eliciting truth and it is fair to assume that no officer of the law will resort to cruelty if truth is what he is seeking. We need not be too exacting about proof of the effects of such violence on the individual involved, for their effect on the human personality is invariably and seriously demoralizing.</p>
<p>When, however, we consider a confession obtained by questioning, even if persistent and prolonged, we are in a different field. Interrogation <i>per se</i> is not, while violence <i>per se</i> is, an outlaw. Questioning is an indispensable instrumentality of justice. It may be abused, of course, as cross-examination in court may be abused, but the principles by which we may adjudge when it passes constitutional limits are quite different from those that condemn police brutality, and are far more difficult to apply. And they call for a more responsible and cautious exercise of our office. For we may err on the side of hostility to violence without doing injury to legitimate prosecution of crime; we cannot read an undiscriminating hostility to mere interrogation into the Constitution without unduly fettering the States in protecting society from the criminal.</p>
<p>It probably is the normal instinct to deny and conceal any shameful or guilty act. Even a "voluntary confession" <span class="star-pagination">*161</span> is not likely to be the product of the same motives with which one may volunteer information that does not incriminate or concern him. The term "voluntary" confession does not mean voluntary in the sense of a confession to a priest merely to rid one's soul of a sense of guilt. "Voluntary confessions" in criminal law are the product of calculations of a different order, and usually proceed from a belief that further denial is useless and perhaps prejudicial. To speak of any confessions of crime made after arrest as being "voluntary" or "uncoerced" is somewhat inaccurate, although traditional.</p>
<p>A confession is wholly and incontestably voluntary only if a guilty person gives himself up to the law and becomes his own accuser. The Court bases its decision on the premise that custody and examination of a prisoner for thirty-six hours is "inherently coercive." Of course it is. And so is custody and examination for one hour. Arrest itself is inherently coercive, and so is detention. When not justified, infliction of such indignities upon the person is actionable as a tort. Of course such acts put pressure upon the prisoner to answer questions to answer them truthfully, and to confess if guilty.</p>
<p>But does the Constitution prohibit use of all confessions made after arrest because questioning, while one is deprived of freedom, is "inherently coercive"? The Court does not quite say so, but it is moving far and fast in that direction. The step it now takes is to hold this confession inadmissible because of the time taken in getting it.</p>
<p>The duration and intensity of an examination or inquisition always have been regarded as one of the relevant and important considerations in estimating its effect on the will of the individual involved. Thirty-six hours is a long stretch of questioning. That the inquiry was prolonged and persistent is a factor that in any calculation <span class="star-pagination">*162</span> of its effect on Ashcraft would count heavily against the confession. But some men would withstand for days pressures that would destroy the will of another in hours. Always heretofore the ultimate question has been whether the confessor was in possession of his own will and self-control at the time of confession. For its bearing on this question the Court always has considered the confessor's strength or weakness, whether he was educated or illiterate, intelligent or moronic, well or ill, Negro or white.</p>
<p>But the Court refuses in this case to be guided by this test. It rejects the finding of the Tennessee courts and says it must make an "independent examination" of the circumstances. Then it says that it will not "resolve any of the disputed questions of fact" relating to the circumstances of the confession. Instead of finding as a fact that Ashcraft's freedom of will was impaired, it substitutes the doctrine that the situation was "inherently coercive." It thus reaches on a <i>part</i> of the evidence in the case a conclusion which I shall demonstrate it could not properly reach on <i>all</i> the evidence. And it refuses to resolve the conflicts in the other evidence to determine whether it rebuts the presumption thus reached that the confession is a coerced one.</p>
<p>If the constitutional admissibility of a confession is no longer to be measured by the mental state of the individual confessor but by a general doctrine dependent on the clock, it should be capable of statement in definite terms. If thirty-six hours is more than is permissible, what about 24? or 12? or 6? or 1? All are "inherently coercive." Of course questions of law like this often turn on matters of degree. But are not the States entitled to know, if this Court is able to state, what the considerations are which make any particular degree decisive? How else may state courts apply our tests?</p>
<p><span class="star-pagination">*163</span> The importance of defining these new constitutional standards of admissibility of confessions is emphasized by the decision to return the companion case of Ware to the Supreme Court of Tennessee for reconsideration "in the light of our ruling as to Ashcraft." Except for Ware's own testimony, all of the evidence is that when he confronted Ashcraft in custody Ware confessed immediately, voluntarily, and almost spontaneously. But he had been arrested, taken from bed into custody, and detained and questioned. Does the doctrine of inherent coerciveness condemn the Ware confession? Should the Tennessee court decide whether Ware, obviously a much weaker character than Ashcraft, was <i>actually</i> coerced into confessing? It already has decided that question and this Court does not hold the fact determined wrongly. Ware's case is properly in this Court. Why should not this Court decide Ware's case on the merits and thus test and expound its novel ruling as applied to a different set of circumstances?</p>
<p>No one can regard the rule of exclusion dependent on the state of the individual's will as an easy one to apply. It leads to controversy, speculation, and variations in application. To eliminate these evils by eliminating all confessions made after interrogation while in custody is a drastic alternative, but it is the logical consequence of today's ruling, as its application to the facts of Ashcraft's case will show.</p>
<p></p>
<h2>II.</h2>
<p>Apart from Ashcraft's uncorroborated testimony, which the Tennessee courts refused to believe, there is much evidence in this record from persons whom they did believe and were justified in believing. This evidence shows that despite the "inherent coerciveness" of the circumstances of his examination, the confession when made was deliberate, <span class="star-pagination">*164</span> free, and voluntary in the sense in which that term is used in criminal law. This Court could not, in our opinion, hold this confession an involuntary one except by substituting its presumption in place of analysis of the evidence and refusing to weigh the evidence even in rebuttal of its presumption.</p>
<p>As in most such cases, we start with some admitted facts. In the early morning Mrs. Ashcraft left her home in an automobile to visit relatives. She was found murdered. She had not been robbed nor ravished, although an effort had been made to give the crime an appearance of robbery. The officers knew of no other motive for the killing and naturally turned to her husband for information.</p>
<p>On the afternoon of the crime, Thursday, June 5, 1941, they took Ashcraft to the morgue to identify the body, and to the county jail, where he was kept and interviewed until 2:00 a.m. He makes no complaint of his treatment at this time. In this and several later interviews he made a number of statements with reference to the condition of the car, and as to Mrs. Ashcraft's having taken a certain drug, and as to money which she was accustomed to carry on her person, which further investigation indicated to be untrue. Still Ashcraft was not arrested. He professed to be willing to assist in identifying the killer. At last, on Saturday evening, June 14, an officer brought Ashcraft to the jail for further questioning. He was taken to a room on the fifth floor and questioned intermittently by several officers over a period of about thirty-six hours.</p>
<p>There are two versions as to what happened during this period of questioning. According to the version of the officers, which was accepted by the court which saw the witnesses, what happened? On Saturday evening Ashcraft was taken to the jail, where he was questioned by Mr. Becker and Mr. Battle. Becker is in the Intelligence <span class="star-pagination">*165</span> Service of the United States Army at the present time and before that was in charge of the Homicide Bureau of the Sheriff's office of Shelby County, Tennessee. Battle has for eight years been an Assistant Attorney General of the County. They began questioning Ashcraft about 7:00 p.m. They recounted various statements of his which had proved untrue. About 11:00 o'clock Ashcraft said he realized the circumstances all pointed to him and that he could not explain the circumstances. They then accused him of the murder, but he denied it. About 3:00 a.m. Becker and Battle retired and left Ashcraft in charge of Ezzell, a special investigator connected with the Attorney General's office. He questioned Ashcraft and discussed the crime with him until about 7:00 on Sunday morning. Becker and Battle then returned and interviewed him intermittently until about noon, when Ezzell returned and remained until about 5:00. Becker then returned, and about 11:00 o'clock Sunday night Ashcraft expressed a desire to talk with Ezzell. Ezzell was sent for and Ashcraft told him he wanted to tell him the truth. He said, "Mr. Ezzell, a Negro killed my wife." Ezzell asked the Negro's name, and Ashcraft said, "Tom Ware." Up to this time Ware had not been suspected, nor had his name been mentioned. Ashcraft explained that he did not tell the officers before because "I was scared; the Negro said he would burn my house down if I told the law."</p>
<p>Thereupon Becker, Battle, Ezzell, and Mr. Jayroe, connected with the Sheriff's office, took Ashcraft in a car and found Ware. When questioned at the jail, Ware turned to Ashcraft and said in substance that he had told Ashcraft when this thing happened that he did not intend to take the entire blame. The officers thereupon turned their attention to Ware. He promptly admitted the killing and said Ashcraft hired him to do it. Waldauer, the court reporter, was called to take down this confession, and <span class="star-pagination">*166</span> completed his transcript at about 5:40 a.m. He read it to Ware and told him he did not have to sign it unless he so chose. Ware made his mark upon it and swore to it before Waldauer as a Notary Public. A copy was given to Ashcraft, and he then admitted that he had hired Ware to kill his wife. He was given breakfast and then in response to questions made a statement which was taken down by the court reporter, Waldauer. It was transcribed, but Ashcraft declined to sign it, saying that he wanted his lawyer to see it before he signed it. No effort was made to compel him to sign the confession. However, two business men of Memphis, Mr. Castle, vice president of a bank, and Mr. Pidgeon, president of the Coca-Cola Bottling Company, were called in. Both testified that Ashcraft in their presence asserted that the transcript was correct but that he declined to sign it. The officers also called Dr. McQuiston to the jail to make a physical examination of both Ashcraft and Ware. He had practiced medicine in Memphis for twenty-eight years and both Mr. and Mrs. Ashcraft had been his patients for something like five years. In the presence of this friendly doctor Ashcraft might have complained of his treatment and avowed his innocence. The doctor testified, however, that Ashcraft said he had been treated all right, that he made no complaint about his eyes, and that they were not bloodshot. The doctor made a physical examination, and says Ashcraft appeared normal. He further testified as to Ashcraft, "Well, sir, he said he had not been able to get along with his wife for some time; that her health had been bad; that he had offered her a property settlement, and that she might go her way and he his way; and he also stated that he offered this colored man, Ware, a sum of money to make away with his wife."<sup>[1]</sup> The doctor says <span class="star-pagination">*167</span> that that statement was entirely voluntary. No matter what pressure had been put on Ashcraft before, the courts below could reasonably believe that he made this statement voluntarily to a man of whom he had no fear and who knew his family relations.</p>
<p>Ashcraft's story of torture could only be accepted by disbelieving such credible and unimpeached contradiction. Ashcraft testified that he was refused food, and was not allowed to go to the lavatory, and was denied even a drink of water. Other testimony is that on Saturday night he was brought a sandwich and coffee about midnight; that he drank the coffee but refused the sandwich; that on Sunday morning he was given a breakfast and was fed again about noon a plate lunch consisting of meat and vegetables and coffee. Both Waldauer, the Reporter, and Dr. McQuiston testified that they saw breakfast served to Ashcraft the next morning before the statement taken down by Waldauer. Ashcraft claims he was threatened and that a cigarette was slapped out of his mouth. This is all denied.</p>
<p>This Court rejects the testimony of the officers and disinterested witnesses in this case that the confession was voluntary not because it lacked probative value in itself nor because the witnesses were self-contradictory or were impeached. On the contrary, it is impugned only on grounds such as that such disputes "are an inescapable consequence of secret inquisitorial practices." We infer from this that since a prisoner's unsupported word often conflicts with that of the officers, the officer's testimony for constitutional purposes is always <i>prima facie</i> false. We know that police standards often leave much to be desired, but we are not ready to believe that the democratic process <span class="star-pagination">*168</span> brings to office men generally less believable than the average of those accused of crime.</p>
<p>Reference also is made to the fact that when petitioner was questioned investigation had failed "to unearth one single tangible clue pointing to his guilt." We cannot see the relevance of such circumstances on the question of the voluntary or involuntary character of his statements to the officers. Is the suggestion that if they had probable clews to his guilt, their questioning of him would have been better justified?</p>
<p>This questioning is characterized as a "secret inquisition," invoking all of the horrendous historical associations of those words. Certainly the inquiry was participated in by a good many persons, and we do not see how it could have been much less "secret" unless the press should have been called in. Of course, any questioning may be characterized as an "inquisition," but the use of such characterizations is no substitute for the detached and judicial consideration that the court below gave to the case.</p>
<p>We conclude that even going behind the state court decisions into the facts, no independent judgment on the whole evidence that Ashcraft's confession was in fact coerced is possible. And against this background of facts the extreme character of the Court's ruling becomes apparent.</p>
<p>I am not sure whether the Court denies the State all right to arrest and question the husband of the slain woman. No investigation worthy of the name could fail to examine him. Of all persons, he was most likely to know whether she had enemies or rivals. Would not the State have a constitutional right, whether he was accused or not, to arrest and detain him as a material witness? If it has the right to detain one as a witness, presumably it has the right to examine him.</p>
<p><span class="star-pagination">*169</span> Could the State not confront Ashcraft with his false statements and ask his explanation? He did not throw himself at any time on his rights, refuse to answer, and demand counsel, even according to his own testimony. The strategy of the officers evidently was to keep him talking, to give him plenty of rope and see if he would not hang himself. He does not claim to have made objection to this. Instead he relied on his wits. The time came when it dawned on him that his own story brought him under suspicion, and that he could not meet it. Must the officers stop at this point because he was coming to appreciate the uselessness of deception?</p>
<p>Then he became desperate and accused the Negro. Certainly from this point the State was justified in holding and questioning him as a witness, for he claimed to know the killer. That accusation backfired and only turned up a witness against him. He had run out of expedients and inventions; he knew he had lost the battle of wits. After all, honesty seemed to be the best, even if the last, policy. He confessed in detail.</p>
<p>At what point in all this investigation does the Court hold that the Constitution commands these officers to send Ashcraft on his way and give up the murder as insoluble? If the State is denied the right to apply any pressure to him which is "inherently coercive" it could hardly deprive him of his freedom at all. I, too, dislike to think of any man, under the disadvantages and indignities of detention being questioned about his personal life for thirty-six hours or for one hour. In fact, there is much in our whole system of penology that seems archaic and vindictive and badly managed. Every person in the community, no matter how inconvenient or embarrassing, no matter what retaliation it exposes him to, may be called upon to take the witness stand and tell all he knows about a crime  except the person who knows most about it. <span class="star-pagination">*170</span> Efforts of prosecutors to compensate for this handicap by violent or brutal treatment or threats we condemn as passionately and sincerely as other members of the Court. But we are not ready to say that the pressure to disclose crime, involved in decent detention and lengthy examination, although we admit them to be "inherently coercive," are denied to a State by the Constitution, where they are not proved to have passed the individual's ability to resist and to admit, deny, or refuse to answer.</p>
<p></p>
<h2>III.</h2>
<p>The Court either gives no weight to the findings of the Tennessee courts or it regards their inquiry as to the effect on the individuals involved as immaterial. We think it was a material inquiry and that respect is due to their conclusion.</p>
<p>The Supreme Court of Tennessee, writing in this case, stated the law of that State by which it reviewed and affirmed the action of the trial court. It said, "When confessions are offered as evidence, their competency becomes a preliminary question to be determined by the court. This imposes upon the presiding judge the duty of deciding <i>the fact</i> whether the party making the confession was influenced by hope or fear. This rule is so well established, that if the judge allow the jury to determine the preliminary fact, it is error, for which the judgment will be reversed.</p>
<p>"In the instant case the trial judge heard the witnesses as to their confessions out of the presence of the jury, and he held that under the facts he could not say that the confessions were not voluntarily made and, therefore, permitted them to go to the jury." (Emphasis supplied.)</p>
<p>The rule of law thus laid down complied with the law as this Court had settled it at the time of trial.</p>
<p>The Tennessee Supreme Court made a painstaking examination of the evidence in the light of the claim that <span class="star-pagination">*171</span> the confessions were coerced. It concluded that it was "unable to say that the confessions were not freely and voluntarily made. Both of the plaintiffs in error have had a fair trial and we decline to disturb the conviction."</p>
<p>That court, it is clear, renders no mere lip service to the guaranties of the Constitution. In other cases it has set aside convictions because confessions used at trials were found to have been coerced.<sup>[2]</sup> There is not the least indication that the court was passionate or biased or that the result does not represent the honest judgment of a high-minded court, sensitive to these problems.</p>
<p>A trial judge out of hearing of the jury saw and heard Ashcraft and saw and heard those whom Ashcraft accused of coercing him. In determining a matter of this kind no one can deny the great advantage of a court which may see and hear a man who claims that his will succumbed and those who, it is claimed, were so overbearing. The real issue is strength of character, and a few minutes' observation of the parties in the courtroom is more informing than reams of cold record. There is not the slightest indication that the trial judge was prejudiced or indifferent to the prisoner's rights. Ashcraft's counsel moved to exclude his confession "for the reason that the statements contained therein were not freely and voluntarily made, nor were they free from duress and restraint, but were secured by compulsion. . . ." The court said, ". . . the sole proposition, as the Court sees it from this testimony, is that he was confined and questioned for a period of approximately thirty-six hours. I think counsel concedes that is practically the main ground upon which he rests his motion. There was no physical violence offered to the defendant Ashcraft, and none claimed." He overruled the motion and received the confession. This <span class="star-pagination">*172</span> Court, not one of whose members ever saw Ashcraft or any one of the State's witnesses, overturns the decision by the trial judge.</p>
<p>Moreover, a jury held Ashcraft's statements incredible. After the trial judge, out of their presence, heard the evidence and decided the confession was admissible, the jury heard the evidence to decide whether the confession should be believed. Ashcraft again testified and so did all of the witnesses for the State. Conduct of the hearing both by the judge and the prosecutors was above criticism. The Court observes: "If, therefore, the question of the voluntariness of the two confessions was actually decided at all it was by the jury." Is it suggested that a State consistently with the Constitution may not leave this question to the sole determination of a jury? I had supposed that the constitutional duty of a State when such questions of fact arise is to furnish due process of law for deciding them. Does not jury trial meet this test? Here Tennessee, and I think very commendably, provided the double safeguards of a preliminary trial by the judge and a final determination by the jury.</p>
<p>The Court's opinion makes a critical reference to the charge of the trial judge. However, diligent counsel took no exception to the part of the charge quoted, made no request for further instruction on the subject, and assigned no error to the charge. Even if we think the charge inadequate, does the inadequacy of a charge constitute want of due process? And if so, do we review questions as to the charge although counsel for the petitioner made no objection during the trial when the judge could have corrected the error, but after the trial was over assigned it as one of twelve reasons for demanding a new trial?</p>
<p>No conclusion that this confession was actually coerced can be reached on this record except by reliance upon the utterly uncorroborated statements of defendant Ashcraft. <span class="star-pagination">*173</span> His testimony does not carry even ordinary guaranties of truthfulness, and the courts and jury were not bound to accept it. Perjury is a light offense compared to murder and they may well have believed that Ashcraft was ready to resort to a lesser crime to avoid conviction of a greater one. Furthermore, the very grounds on which this Court now upsets his conviction Ashcraft repudiated at the trial. He asserts that he was abused, but he does not testify as this Court holds that it had the effect of forcing an involuntary confession from him. On the contrary, he flatly insists that it had no such effect and that he never did confess at all.</p>
<p>Against Ashcraft's word the state courts and jury accepted the testimony of several apparently disinterested witnesses of high standing in their communities, in addition to that of the accused officers. One of the witnesses to Ashcraft's admission of guilt was his own family physician, two were disinterested businessmen of substance and standing, another was an experienced court reporter who had long held this position of considerable trust. Another was a member of the bar. Certainly, the state courts were not committing an offense against the Constitution of the United States in refusing to believe that this whole group of apparently reputable citizens entered into a conspiracy to swear a murder onto an innocent man, against whom not one of them is shown to have had a grievance or a grudge.</p>
<p>This is not the case of an ignorant and unrepresented defendant who has been the victim of prejudice. Ashcraft was a white man of good reputation, good position, and substantial property. For a week after this crime was discovered he was not detained, although his stories to the officers did not hang together, but was at large, free to consult his friends and counsel. There was no indecent haste, but on the contrary evident deliberation, in suspecting <span class="star-pagination">*174</span> and accusing him. He was not sentenced to death, but for a term that probably means life. He was defended by resourceful and diligent counsel.</p>
<p>The use of the due process clause to disable the States in protection of society from crime is quite as dangerous and delicate a use of federal judicial power as to use it to disable them from social or economic experimentation. The warning words of Mr. Justice Holmes in his dissenting opinion in <i>Baldwin</i> v. <i>Missouri,</i> <span class="citation" data-id="101593"><a href="/opinion/101593/baldwin-v-missouri/#595" aria-description="Citation for case: Baldwin v. Missouri">281 U.S. 586, 595</a></span>, seem to us appropriate for rereading now.</p>
<p>MR. JUSTICE ROBERTS and MR. JUSTICE FRANKFURTER join in this opinion.</p>
<h2>NOTES</h2>
<p>[1]  The legal test applied by the trial court to determine the admissibility of the two confessions was stated thus:
</p>
<p>"The Court has come to the conclusion . . . that the law in Tennessee with reference to confession is simply this: it is largely a question of fact as to whether or not a confession is voluntary, and is made without hope of reward or fear of punishment. It only becomes a question of law for the Court to decide when, from the facts surrounding the taking of the alleged confessions or statements, the Court, as a matter of law, can hold that the State has failed to carry its burden, which it has of showing that the confessions were free and voluntary, and that reasonable minds could not differ, and could come to but one conclusion that the confessions were involuntary and forced."</p>
<p>[2]  Notwithstanding the apparent fact that neither the trial court nor the appellate court affirmatively held the confessions voluntary, the Tennessee Supreme Court, in its opinion, restated the rule it had announced in previous cases, that, "When confessions are offered as evidence, their competency becomes a preliminary question, to be determined by the court. . . . [If] the judge allow the jury to determine the preliminary fact, it is error, for which the judgment will be reversed." See <i>Self</i> v. <i>State,</i> <span class="citation" data-id="7280307"><a href="/opinion/7361546/self-v-state/#253" aria-description="Citation for case: Self v. State">65 Tenn. 244, 253</a></span>.</p>
<p>[3]  On motion for new trial, Ashcraft's counsel urged error in that, "The court . . . in delivering his charge to the jury . . . in no place or at any time . . . presented the theory of the defendant Ashcraft to the jury. He wholly and completely in his charge ignored the contention and theory of the defendant Ashcraft that the alleged confession or admissions made by him . . . were not freely and voluntarily made. . . ."</p>
<p>[4]  From the testimony it appears that Ashcraft was taken from the jail about 11 o'clock Sunday night for a period of approximately an hour to help the officers hunt the place where Ware lived. On his return Ashcraft was, for a short time, kept in a jail room different from that in which he was kept the rest of the time.</p>
<p>[5]  "As the report avers, `The third degree is a secret and illegal practice.' Hence the difficulty of discovering the facts as to the extent and manner it is practiced." IV Reports of National Committee on Law Observance and Enforcement (Wickersham Commission), U.S. Government Printing Office, 1931, Lawlessness in Law Enforcement, p. 3. Station houses and jails are most frequently employed for third degree practices, "upstairs rooms or back rooms being sometimes picked out for their greater privacy." <i><span class="citation" data-id="7280307"><a href="/opinion/7361546/self-v-state/" aria-description="Citation for case: Self v. State">Id.,</a></span></i> The Third Degree, p. 170. Cf. <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#238" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227, 238</a></span>.</p>
<p>[6]  "`Work' is the term used to signify any form of what is commonly called the third degree, and may consist in nothing more than a severe cross-examination. Perhaps in most cases it is no more than that, but the prisoner knows that he is wholly at the mercy of his inquisitor and that the severe cross-examination may at any moment shift to a severe beating. . . . Powerful lights turned full on the prisoner's face, or switched on and off have been found effective. . . . The most commonly used method is persistent questioning, continuing hour after hour, sometimes by relays of officers. It has been known since 1500 at least that deprivation of sleep is the most effective torture and certain to produce any confession desired." Report of Committee on Lawless Enforcement of Law made to the Section of Criminal Law and Criminology of the American Bar Association (1930) 1 American Journal of Police Science 575, 579-580, also quoted in IV Wickersham Report, <i>supra,</i> p. 47.</p>
<p>[7]  The use in evidence of a defendant's coerced confession cannot be justified on the ground that the defendant has denied he ever gave the confession. <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/#531" aria-description="Citation for case: White v. Texas">310 U.S. 530, 531-532</a></span>.</p>
<p>[8]  State and federal courts, textbook writers, legal commentators, and governmental commissions consistently have applied the name of "inquisition" to prolonged examination of suspects conducted as was the examination of Ashcraft. See, e.g., cases cited in IV Wickersham Report, <i>supra,</i> and also pp. 44, 47, 48, and passim; Pound (Cuthbert W.), Inquisitorial Confessions, 1 Cornell L.Q. 77; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#237" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227, 237</a></span>; <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#544" aria-description="Citation for case: Bram v. United States">168 U.S. 532, 544</a></span>; <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#596" aria-description="Citation for case: Brown v. Walker">161 U.S. 591, 596</a></span>; <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#573" aria-description="Citation for case: Counselman v. Hitchcock">142 U.S. 547, 573</a></span>; cf. <i>Cooper</i> v. <i>State,</i> <span class="citation" data-id="6513449"><a href="/opinion/6636874/cooper-v-state/#611" aria-description="Citation for case: Cooper v. State">86 Ala. 610, 611</a></span>, <span class="citation no-link">6 So. 110</span>. In a case where no physical violence was inflicted or threatened, the Supreme Court of Virginia expressly approved the statement of the trial judge that the manner and methods used in obtaining the confession read "like a chapter from the history of the inquisition of the Middle Ages." <i>Enoch</i> v. <i>Commonwealth,</i> <span class="citation" data-id="9579748"><a href="/opinion/1322156/enoch-v-commonwealth/#423" aria-description="Citation for case: Enoch v. Commonwealth">141 Va. 411, 423</a></span>, <span class="citation" data-id="9579748"><a href="/opinion/1322156/enoch-v-commonwealth/#225" aria-description="Citation for case: Enoch v. Commonwealth">126 S.E. 222, 225</a></span>; and see <i>Cross</i> v. <i>State,</i> <span class="citation" data-id="8301941"><a href="/opinion/8333908/cross-v-state/#514" aria-description="Citation for case: Cross v. State">142 Tenn. 510, 514</a></span>, <span class="citation no-link">221 S.W. 489</span>. The analogy, of course, was in the fact that old inquisition practices included questioning suspects in secret places, away from friends and counsel, with notaries waiting to take down "confessions," and with arrangements to have the suspect later affirm the truth of his confession in the presence of witnesses who took no part in the inquisition. See Encyclopedia Britannica, Fourteenth Ed., "Inquisition"; Prescott, Ferdinand and Isabella, Sixth Ed., Part First, Chap. VII, The Inquisition; VIII Wigmore on Evidence, Third Ed., p. 307. "In the more serious offenses the party suspected is arrested, he is placed on his inquisition before the chief of police, and a statement is obtained. . . . Where the office of the district attorney is in political harmony with the police system, the district attorney is generally invited to be present as an inquisitor." 2 Wharton on Criminal Evidence, Eleventh Ed., pp. 1021-1022; and see Notes 5 and 6, <i>supra.</i>
</p>
<p>An admirable summary of the generally expressed judicial attitude toward these practices is set forth in the Report of The Committee on Lawless Enforcement of Law, 1 Amer. Journ. of Police Science, <i>supra,</i> p. 587: "Holding incommunicado is objectionable because arbitrary  at the mere will and unregulated pleasure of a police officer. . . . The use of the third degree is obnoxious because it is secret; because the prisoner is wholly unrepresented; because there is present no neutral, impartial authority to determine questions between the police and the prisoner; because there is no limit to the range of the inquisition, nor to the pressure that may be put upon the prisoner."</p>
<p>[9]  <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#556" aria-description="Citation for case: Bram v. United States">168 U.S. 532, 556, 562-563</a></span>; see also <i>Wan</i> v. <i>United States,</i> <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U.S. 1, 14-15</a></span>; <i>Burdeau</i> v. <i>McDowell,</i> <span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#475" aria-description="Citation for case: Burdeau v. McDowell">256 U.S. 465, 475</a></span>; <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/#573" aria-description="Citation for case: Counselman v. Hitchcock">142 U.S. 547, 573-574</a></span>; 3 Elliot's Debates, pp. 445-449, 452; cf. <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>. The question in the <i><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span></i> case was whether Bram had been compelled or coerced by a police officer to make a self-incriminatory statement, contrary to the Fifth Amendment; and the question here is whether Ashcraft similarly was coerced to make such a statement, contrary to the Fourteenth Amendment. <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 236-238</a></span>. Taken together, the <i><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span></i> and <i><span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">Lisenba</a></span></i> cases hold that a coerced or compelled confession cannot be used to convict a defendant in any state or federal court. And the decision in the <i><span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">Bram</a></span></i> case makes it clear that the admitted circumstances under which Ashcraft is alleged to have confessed preclude a holding that he acted voluntarily.</p>
<p>[10]  Compare the following allegation contained in Ashcraft's motion for new trial, "The Sheriff's deputies . . . set themselves up as a quasi judicial tribunal and tried . . . and convicted him there and in so doing rendered a trial . . . before the trial court . .. and the jury of peers . . . a mere formality," with <i>Lisenba</i> v. <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#237" aria-description="Citation for case: Lisenba v. California"><i>California, supra,</i> p. 237</a></span>. "The requirement of a public trial is for the benefit of the accused; that the public may see he is fairly dealt with and not unjustly condemned, and that the presence of interested spectators may keep his triers keenly alive to a sense of their responsibility and to the importance of their functions . . ." Cooley's Constitutional Limitations, Sixth Ed. (1890) p. 379; see also <i>Keddington</i> v. <i>State,</i> <span class="citation" data-id="6474469"><a href="/opinion/6599127/keddington-v-state/#459" aria-description="Citation for case: Keddington v. State">19 Ariz. 457, 459</a></span>, <span class="citation" data-id="6474469"><a href="/opinion/6599127/keddington-v-state/" aria-description="Citation for case: Keddington v. State">172 P. 273</a></span>. "The aid of counsel in preparation would be farcical if the case could be foreclosed by a preliminary inquisition which would squeeze out conviction or prejudice by means unconstitutional if used at the trial." <i>Wood</i> v. <i>United States,</i> <span class="citation" data-id="1545293"><a href="/opinion/1545293/wood-v-united-states/#271" aria-description="Citation for case: Wood v. United States">128 F.2d 265, 271</a></span>. See also <i>Chambers</i> v. <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#237" aria-description="Citation for case: Chambers v. Florida"><i>Florida, supra,</i> p. 237</a></span>, Note 10.</p>
<p>[11]  <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U.S. 227</a></span>; <i>Canty</i> v. <i>Alabama,</i> <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U.S. 629</a></span>; <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U.S. 530</a></span>; <i>Lomax</i> v. <i>Texas,</i> <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">313 U.S. 544</a></span>; <i>Vernon</i> v. <i>Alabama,</i> <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U.S. 547</a></span>; <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#236" aria-description="Citation for case: Lisenba v. California">314 U.S. 219, 236-238</a></span>; <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#555" aria-description="Citation for case: Ward v. Texas">316 U.S. 547, 555</a></span>; and see <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U.S. 532</a></span>.</p>
<p>[1]  The officers had been baffled as to any motive for Ashcraft to murder his wife (who was his third, two former ones having been separated from him by divorce). He disclosed in his confession to them that her sickness had resulted in a degree of irritability which had made them incompatible and resulted in his sexual frustration.</p>
<p>[2]  <i>Deathridge</i> v. <i>State,</i> <span class="citation" data-id="7663198"><a href="/opinion/7727512/deathridge-v-state/" aria-description="Citation for case: Deathridge v. State">33 Tenn. 75</a></span>; <i>Strady</i> v. <i>State,</i> <span class="citation multiple-matches"><a href="/c/Tenn./45/300/">45 Tenn. 300</a></span>; <i>Self</i> v. <i>State,</i> <span class="citation" data-id="7280307"><a href="/opinion/7361546/self-v-state/" aria-description="Citation for case: Self v. State">65 Tenn. 244</a></span>; <i>Cross</i> v. <i>State,</i> <span class="citation" data-id="8301941"><a href="/opinion/8333908/cross-v-state/" aria-description="Citation for case: Cross v. State">142 Tenn. 510</a></span>, <span class="citation no-link">221 S.W. 489</span>; <i>Rounds</i> v. <i>State,</i> <span class="citation" data-id="3891773"><a href="/opinion/4129358/rounds-v-state/" aria-description="Citation for case: Rounds v. State">171 Tenn. 511</a></span>, <span class="citation" data-id="3891773"><a href="/opinion/4129358/rounds-v-state/" aria-description="Citation for case: Rounds v. State">106 S.W.2d 212</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Ashcroft v. al-Kidd.md  (`case`, 6 assertions)

### content_page

```
---
title: "Ashcroft v. al-Kidd"
type: case
citation: ""
parallel_cite: "179 L. Ed. 2d 1149; 131 S. Ct. 2074; 563 U.S. 731; 79 U.S.L.W. 4393; 22 Fla. L. Weekly Fed. S 1057"
neutral_cite: 2011 U.S. LEXIS 4021
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-05-31
docket: 10-98
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-05-31
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Ashcroft v. al-Kidd
  varies_by_point: false
  scope_note: "Good law: subjective intent is irrelevant to Fourth Amendment objective reasonableness; leading 'clearly established' qualified-immunity statement."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7344719/ashcroft-v-al-kidd/"
  cluster_id: 7344719
  opinion_id: 7262676
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[Whren v. United States]]", "[[Malley v. Briggs]]", "[[Harlow v. Fitzgerald]]"]
aliases: ["al-Kidd v. Ashcroft", "Ashcroft v. Al-Kidd"]
tags: ["case", "section-1983", "bivens", "qualified-immunity", "material-witness", "pretext", "objective-reasonableness"]
holding: "An objectively reasonable arrest of a material witness on a valid warrant cannot be challenged as unconstitutional on the basis of the officer's subjective motive; subjective intent is irrelevant to Fourth Amendment reasonableness, and the contrary theory was not clearly established (QI)."
lake:
  record_id: Ashcroft v. al-Kidd
  status: verified
  projected_at: 2026-07-09
---

# Ashcroft v. al-Kidd

*563 U.S. 731 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Abdullah al-Kidd, a U.S. citizen, was arrested in 2003 on a federal material-witness warrant — ostensibly to secure his testimony in a terrorism prosecution — but was never called to testify. He sued former Attorney General John Ashcroft under *[[Bivens v. Six Unknown Named Agents|Bivens]]*, alleging that Ashcroft had adopted a policy of using the material-witness statute as a **pretext** to detain terrorism suspects whom the government lacked probable cause to charge, in violation of the Fourth Amendment. Ashcroft asserted [[Qualified Immunity|qualified immunity]].

## Issue
Whether an arrest made on a valid material-witness warrant can be challenged as unconstitutional based on the officer's alleged improper subjective motive — and, if the theory is doubtful, whether Ashcroft violated clearly established law.

## Rule
Fourth Amendment reasonableness is judged objectively, so subjective motive does not invalidate an otherwise-valid arrest. "Fourth Amendment reasonableness 'is predominantly an objective inquiry.' We ask whether 'the circumstances, viewed objectively, justify [the challenged] action.' If so, that action was reasonable 'whatever the subjective intent' motivating the relevant officials." — 563 U.S. at 736. ^pin-736

"We hold that an objectively reasonable arrest and detention of a material witness pursuant to a validly obtained warrant cannot be challenged as unconstitutional on the basis of allegations that the arresting authority had an improper motive." — [*Id.* at 743](https://www.courtlistener.com/opinion/7344719/ashcroft-v-al-kidd/#:~:text=We%20hold%20that%20an%20objectively). ^pin-743

And [[Qualified Immunity|qualified immunity]] "protects 'all but the plainly incompetent or those who knowingly violate the law.'" — *Id.* (quoting [[Malley v. Briggs]], 475 U.S. at 341).

## Application
A warrant naming only al-Kidd, supported by individualized reasons to believe he was a material witness who might disappear, took the case outside the narrow special-needs/administrative-search exceptions where subjective purpose matters; the general rule that motive is irrelevant therefore governed. Even assuming the pretextual-material-witness theory could state a Fourth Amendment violation, it was not clearly established at the time — eight court-of-appeals judges had agreed with Ashcroft's position in a case of first impression — so he was entitled to [[Qualified Immunity|qualified immunity]], and the Court did not reach whether he also had absolute immunity.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]. Subjective intent does not defeat an objectively reasonable, warrant-based arrest, and Ashcroft did not violate clearly established law; he was entitled to [[Qualified Immunity|qualified immunity]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *al-Kidd* extends the objective-reasonableness / motive-irrelevance principle of [[Whren v. United States]] beyond the traffic-stop context and is a leading modern statement of the "clearly established" standard within the [[Harlow v. Fitzgerald]] / [[Malley v. Briggs]] qualified-immunity line (its "high level of generality" admonition is quoted in [[Mullenix v. Luna]] and [[Messerschmidt v. Millender]]). No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Ashcroft v. al-Kidd*, 563 U.S. 731 (2011) — https://www.courtlistener.com/opinion/217703/ashcroft-v-al-kidd/ — pinpoints: 736, 743 (CL stores the slip opinion "563 U. S. ____ (2011)"; pins keyed to the official U.S. Reports pages — objective inquiry slip op. 3–4, holding/QI slip op. 12).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2d8d3095a8d08a83", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2011 U.S. LEXIS 4021", "official_citation_present": false, "parallel_cite": "179 L. Ed. 2d 1149; 131 S. Ct. 2074; 563 U.S. 731; 79 U.S.L.W. 4393; 22 Fla. L. Weekly Fed. S 1057", "title": "Ashcroft v. al-Kidd", "year": "2011"}}
{"assertion_id": "7305bba3b092aa3f", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Ashcroft v. al-Kidd"}}
{"assertion_id": "8a6a3414d8ddb1a3", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "Ashcroft v. al-Kidd"}}
{"assertion_id": "9ba88547ab96d0bc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An objectively reasonable arrest of a material witness on a valid warrant cannot be challenged as unconstitutional on the basis of the officer's subjective motive; subjective intent is irrelevant to Fourth Amendment reasonableness, and the contrary theory was not clearly established (QI).", "title": "Ashcroft v. al-Kidd"}}
{"assertion_id": "135b85bd465e1c50", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Ashcroft v. al-Kidd"}}
{"assertion_id": "c062cd6ea0a83f4b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2011-05-31", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Ashcroft v. al-Kidd", "field_i_validity": "good_law", "scope_note": "Good law: subjective intent is irrelevant to Fourth Amendment objective reasonableness; leading 'clearly established' qualified-immunity statement.", "title": "Ashcroft v. al-Kidd", "varies_by_point": "false"}}
```

### lake record — Ashcroft v. al-Kidd

```json
{
  "schema_version": "s2.v1",
  "record_id": "Ashcroft v. al-Kidd",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Ashcroft v. al-Kidd",
    "case_name_short": "al-Kidd",
    "case_name_full": "JOHN D. ASHCROFT v. ABDULLAH al-KIDD",
    "input_case_name": "Ashcroft v. al-Kidd",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-05-31",
    "year": 2011,
    "docket": "10-98",
    "cluster_id": 7344719,
    "lead_opinion_id": 7262676,
    "sibling_ids": [
      7262676,
      7262677,
      7262678,
      7262679
    ],
    "absolute_url": "/opinion/7344719/ashcroft-v-al-kidd/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 217703,
        "score": 110,
        "case_name": "Ashcroft v. al-Kidd"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "179 L. Ed. 2d 1149",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2074",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 731",
        "volume": "563",
        "reporter": "U.S.",
        "page": "731",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4393",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4393",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 1057",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "1057",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 4021",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "179 L. Ed. 2d 1149",
        "volume": "179",
        "reporter": "L. Ed. 2d",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 4021",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "131 S. Ct. 2074",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2074",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "563 U.S. 731",
        "volume": "563",
        "reporter": "U.S.",
        "page": "731",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 U.S.L.W. 4393",
        "volume": "79",
        "reporter": "U.S.L.W.",
        "page": "4393",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 Fla. L. Weekly Fed. S 1057",
        "volume": "22",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "1057",
        "type": 1,
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
      "id": "pin-736",
      "page": null,
      "quote": "--- # Ashcroft v. al-Kidd *563 U.S. 731 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Abdullah al-Kidd, a U.S. citizen, was arrested in 2003 on a federal material-witness warrant \u2014 ostensibly to secure his testimony in a terrorism prosecution \u2014 but was never called to testify. He sued former Attorney General John Ashcroft under *Bivens*, alleging that Ashcroft had adopted a policy of using the material-witness statute as a **pretext** to detain terrorism suspects whom the government lacked probable cause to charge, in violation of the Fourth Amendment. Ashcroft asserted qualified immunity. ## Issue Whether an arrest made on a valid material-witness warrant can be challenged as unconstitutional based on the officer's alleged improper subjective motive \u2014 and, if the theory is doubtful, whether Ashcroft violated clearly established law. ## Rule Fourth Amendment reasonableness is judged objectively, so subjective motive does not invalidate an otherwise-valid arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-743",
      "page": null,
      "quote": "We hold that an objectively reasonable arrest and detention of a material witness pursuant to a validly obtained warrant cannot be challenged as unconstitutional on the basis of allegations that the arresting authority had an improper motive.",
      "star_marker": "1161",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 52473,
      "fragment": "#:~:text=We%20hold%20that%20an%20objectively",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-05-31",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Ashcroft v. al-Kidd",
    "varies_by_point": false,
    "scope_note": "Good law: subjective intent is irrelevant to Fourth Amendment objective reasonableness; leading 'clearly established' qualified-immunity statement.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "George Trammell v. Kevin Fruge",
          "cluster_id": 4419631,
          "cite": [
            "868 F.3d 332",
            "2017 WL 3528437",
            "2017 U.S. App. LEXIS 15529"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
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
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramona Hinojosa v. Brad Livingston",
          "cluster_id": 3155936,
          "cite": [
            "807 F.3d 657",
            "2015 U.S. App. LEXIS 20016",
            "2015 WL 7422990"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MacDonald v. Town of Eastham",
          "cluster_id": 2656464,
          "cite": [
            "745 F.3d 8",
            "2014 WL 944707",
            "2014 U.S. App. LEXIS 4618"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Prall v. City of Boston",
          "cluster_id": 8729956,
          "cite": [
            "985 F. Supp. 2d 115",
            "2013 WL 6076462",
            "2013 U.S. Dist. LEXIS 166128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Morgan v. Swanson",
          "cluster_id": 8441074,
          "cite": [
            "659 F.3d 359",
            "2011 U.S. App. LEXIS 19656",
            "2011 WL 4470233"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Egbert v. Boule",
          "cluster_id": 6475794,
          "cite": [
            "596 U.S. 482",
            "142 S. Ct. 1793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Natasha Whitley v. John Hanna",
          "cluster_id": 1036944,
          "cite": [
            "726 F.3d 631",
            "2013 WL 4029134",
            "2013 U.S. App. LEXIS 16485"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roger Poole v. City of Shreveport",
          "cluster_id": 806839,
          "cite": [
            "691 F.3d 624",
            "2012 WL 3517357",
            "2012 U.S. App. LEXIS 17243"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DiStiso ex rel. DiStiso v. Cook",
          "cluster_id": 807074,
          "cite": [
            "691 F.3d 226",
            "2012 WL 3570755"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derrick Newman v. James Guedry",
          "cluster_id": 3071815,
          "cite": [
            "703 F.3d 757",
            "2012 U.S. App. LEXIS 26205",
            "2012 WL 6634975"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael-Ryan Kruger v. State of Nebraska",
          "cluster_id": 3192229,
          "cite": [
            "820 F.3d 295",
            "2016 U.S. App. LEXIS 6326",
            "2016 WL 1376343"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glik v. Cunniffe",
          "cluster_id": 612667,
          "cite": [
            "655 F.3d 78",
            "84 A.L.R. 6th 647",
            "39 Media L. Rep. (BNA) 2257",
            "2011 U.S. App. LEXIS 17841",
            "2011 WL 3769092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gray v. Cummings",
          "cluster_id": 4593291,
          "cite": [
            "917 F.3d 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corey Hughes v. Michael Rodriguez",
          "cluster_id": 6461702,
          "cite": [
            "31 F.4th 1211"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pratt Ex Rel. Estate of Pratt v. Harris County",
          "cluster_id": 3200293,
          "cite": [
            "822 F.3d 174",
            "2016 U.S. App. LEXIS 8049",
            "2016 WL 2343032"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barbara Wyatt v. Rhonda Fletcher",
          "cluster_id": 873536,
          "cite": [
            "718 F.3d 496",
            "2013 WL 2371280",
            "2013 U.S. App. LEXIS 11045"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lamont Shepard v. T. Quillen",
          "cluster_id": 4315689,
          "cite": [
            "840 F.3d 686",
            "2016 U.S. App. LEXIS 19352",
            "2016 WL 6246873"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Irish v. Fowler",
          "cluster_id": 4803838,
          "cite": [
            "979 F.3d 65"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tucker v. City of Shreveport",
          "cluster_id": 4884106,
          "cite": [
            "998 F.3d 165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Susan Doxtator v. Erik O'Brien",
          "cluster_id": 6623081,
          "cite": [
            "39 F.4th 852"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stamps Ex Rel. Estate of Stamps v. Town of Framingham",
          "cluster_id": 3175226,
          "cite": [
            "813 F.3d 27",
            "2016 U.S. App. LEXIS 2026",
            "2016 WL 457153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Matalon v. Hynnes",
          "cluster_id": 3155905,
          "cite": [
            "806 F.3d 627",
            "2015 U.S. App. LEXIS 20008",
            "2015 WL 7280627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacob Pfaller v. Mark Amonette",
          "cluster_id": 9344950,
          "cite": [
            "55 F.4th 436"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Drumgold v. Callahan",
          "cluster_id": 816494,
          "cite": [
            "707 F.3d 28",
            "2013 U.S. App. LEXIS 2301",
            "2013 WL 376747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Ashcroft v. al-Kidd:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 106,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 8,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 106,
        "triage_read": 8,
        "triage_snippet_classified": 98
      },
      "lane2_top_cited": {
        "query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MiZzPTk0MjE3NjMmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287262676+OR+7262677+OR+7262678+OR+7262679%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679)",
        "reviewed": 24,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 24,
        "triage_read": 0,
        "triage_snippet_classified": 24
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(7262676 OR 7262677 OR 7262678 OR 7262679)",
    "indexed_citing_opinions": 168,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7262676,
        "count": 168,
        "count_source": "search"
      },
      {
        "opinion_id": 7262677,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7262678,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7262679,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1746,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/ashcroft-v-al-kidd.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgzNDU1NTcmcz05NDEyMTU0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%287262676+OR+7262677+OR+7262678+OR+7262679%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T19:06:31Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:06:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:06:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:10:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:06:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Ashcroft v. al-Kidd

```
<opinion type="majority">
<p id="b1252-6">OPINION OF THE COURT</p>
<p id="b1252-7">[<span class="citation no-link">563 U.S. 733</span>]</p>
<author id="b1252-8">Justice Scalia</author>
<p id="AdE0">delivered the opinion of the Court.</p>
<p id="b1252-9">We decide whether a former Attorney General enjoys immunity from suit for allegedly authorizing federal prosecutors to obtain valid material-witness warrants for detention of terrorism suspects whom they would otherwise lack probable cause to arrest.</p>
<p id="b1252-10">I</p>
<p id="b1252-11">The federal material-witness statute authorizes judges to “order the arrest of [a] person” whose testimony “is material in a criminal proceeding ... if it is shown that it may become impracticable to secure the presence of the person by subpoena.” <span class="citation no-link">18 U.S.C. § 3144</span>. Material witnesses enjoy the same constitutional right to pretrial release as other federal detainees, and federal law requires release if their testimony “can adequately be secured by deposition, and if further detention is not necessary to prevent a failure of justice.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b1252-12">[<span class="citation no-link">563 U.S. 734</span>]</p>
<p id="b1252-13">Because this case arises from a motion to dismiss, we accept as true the factual allegations in Abdullah al-Kidd’s complaint. The complaint alleges that, in the aftermath of the September 11th terrorist attacks, then-Attorney General John Ashcroft authorized federal prosecutors and law enforcement officials to use the material-witness statute to detain individuals with suspected ties to terrorist organizations. It is alleged that federal officials had no intention of calling most of these individuals as witnesses, and that they were detained, at Ashcroft’s direction, because federal officials suspected them of supporting terrorism but lacked sufficient evidence to charge them with a crime.</p>
<p id="b1252-19">It is alleged that this pretextual detention policy led to the material-witness arrest of al-Kidd, a native-born United States citizen. FBI agents apprehended him in March 2003 as he checked in for a flight to Saudi Arabia. Two days earlier, federal officials had informed a Magistrate Judge that, if al-Kidd boarded his flight, they believed information “crucial” to the prosecution of Sami Omar al-Hussayen would be lost. App. 64. Al-Kidd remained in federal custody for 16 days and on supervised release until al-Hussayen’s trial concluded 14 months later. Prosecutors never called him as a witness.</p>
<p id="b1252-20">In March 2005, al-Kidd filed this <em>Bivens </em>action, see <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U.S. 388</a></span>, <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">91 S. Ct. 1999</a></span>, <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">29 L. Ed. 2d 619</a></span> (1971), to challenge the constitutionality of Ashcroft’s alleged policy; <page-number citation-index="1" label="1155">*1155</page-number>he also asserted several other claims not relevant here against Ashcroft and others. Ashcroft filed a motion to dismiss based on absolute and qualified immunity, which the District Court denied. A divided panel of the United States Court of Appeals for the Ninth Circuit affirmed, holding that the Fourth Amendment prohibits pre-textual arrests absent probable cause of criminal wrongdoing, and that Ashcroft could not claim qualified or absolute immunity. See <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d 949</a></span> (2009).</p>
<p id="b1253-4">[<span class="citation no-link">563 U.S. 735</span>]</p>
<p id="b1253-5">Judge Bea dissented, <em>id,, </em>at 981, and eight judges dissented from the denial of rehearing en banc, see <span class="citation" data-id="8411499"><a href="/opinion/8440576/al-kidd-v-ashcroft/#1137" aria-description="Citation for case: Al-Kidd v. Ashcroft">598 F.3d 1129, 1137, 1142</a></span> (2010). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.S./562/980/">562 U.S. 980</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/415/">131 S. Ct. 415</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/178/321/">178 L. Ed. 2d 321</a></span> (2010).</p>
<p id="b1253-6">II</p>
<p id="b1253-7">Qualified immunity shields federal and state officials from money damages unless a plaintiff pleads facts showing (1) that the official violated a statutory or constitutional right, and (2) that the right was “clearly established” at the time of the challenged conduct. <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U.S. 800, 818</a></span>, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">102 S. Ct. 2727</a></span>, <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/" aria-description="Citation for case: Harlow v. Fitzgerald">73 L. Ed. 2d 396</a></span> (1982). We recently reaffirmed that lower courts have discretion to decide which of the two prongs of qualified-immunity analysis to tackle first. See <em>Pearson </em>v. <em>Callahan, </em><span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#236" aria-description="Citation for case: Pearson v. Callahan">555 U.S. 223, 236</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">129 S. Ct. 808</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">172 L. Ed. 2d 565</a></span> (2009).</p>
<p id="b1253-8">Courts should think carefully before expending “scarce judicial resources” to resolve difficult and novel questions of constitutional or statutory interpretation that will “have no effect on the outcome of the case.” <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#236" aria-description="Citation for case: Pearson v. Callahan"><em>Id., </em>at 236-237</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">129 S. Ct. 808</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">172 L. Ed. 2d 565</a></span>; see <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/#237" aria-description="Citation for case: Pearson v. Callahan"><em>id., </em>at 237-242</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">129 S. Ct. 808</a></span>, <span class="citation" data-id="145918"><a href="/opinion/145918/pearson-v-callahan/" aria-description="Citation for case: Pearson v. Callahan">172 L. Ed. 2d 565</a></span>. When, however, a court of appeals does address both prongs of qualified-immunity analysis, we have discretion to correct its errors at each step. Although not necessary to reverse an erroneous judgment, doing so ensures that courts do not insulate constitutional decisions at the frontiers of the law from our review or inadvertently undermine the values qualified immunity seeks to promote. The former occurs when the constitutional-law question is wrongly decided; the latter when what is not clearly established is held to be so. In this case, the Court of Appeals’ analysis at both steps of the qualified-immunity inquiry needs correction.</p>
<p id="b1253-10">A</p>
<p id="b1253-11">The Fourth Amendment protects “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” An arrest, of course, qualifies as a “seizure” of a “person” under this provision,</p>
<p id="b1253-12">[<span class="citation no-link">563 U.S. 736</span>]</p>
<p id="b1253-13"><em>Dunaway </em>v. <em>New York, </em><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#207" aria-description="Citation for case: Dunaway v. New York">442 U.S. 200, 207-208</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">99 S. Ct. 2248</a></span>, <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">60 L. Ed. 2d 824</a></span> (1979), and so must be reasonable under the circumstances. Al-Kidd does not assert that Government officials would have acted unreasonably if they had used a material-witness warrant to arrest him for the purpose of securing his testimony for trial. See Brief for Respondent 16-17; Tr. of Oral Arg. 20-22. He contests, however (and the Court of Appeals here rejected), the reasonableness of using the warrant to detain him as a suspected criminal.</p>
<p id="b1253-15">Fourth Amendment reasonableness “is predominantly an objective inquiry.” <em>Indianapolis </em>v. <em>Edmond, </em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S. 32, 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span> (2000). We ask whether “the circumstances, viewed objectively, justify [the challenged] ac<page-number citation-index="1" label="1156">*1156</page-number>tion.” <em>Scott </em>v. <em>United States, </em><span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#138" aria-description="Citation for case: Scott v. United States">436 U.S. 128, 138</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">98 S. Ct. 1717</a></span>, <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/" aria-description="Citation for case: Scott v. United States">56 L. Ed. 2d 168</a></span> (1978). If so, that action was reasonable <em>“whatever </em>the subjective intent” motivating the relevant officials. <em>Whren </em>v. <em>United States, </em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#814" aria-description="Citation for case: Whren v. United States">517 U.S. 806, 814</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span> (1996). This approach recognizes that the Fourth Amendment regulates conduct rather than thoughts, <em>Bond </em>v. <em>United States, </em><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#338" aria-description="Citation for case: Bond v. United States">529 U.S. 334, 338, n. 2</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">120 S. Ct. 1462</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">146 L. Ed. 2d 365</a></span> (2000); and it promotes evenhanded, uniform enforcement of the law, <em>Devenpeck </em>v. <em>Alford, </em><span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/#153" aria-description="Citation for case: Devenpeck v. Alford">543 U.S. 146, 153-154</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S. Ct. 588</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L. Ed. 2d 537</a></span> (2004).</p>
<p id="b1254-4">Two “limited exception [s]” to this rule are our special-needs and administrative-search cases, where “actual motivations” do matter. <em>United States </em>v. <em>Knights, </em><span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/#122" aria-description="Citation for case: United States v. Knights">534 U.S. 112, 122</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">122 S. Ct. 587</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">151 L. Ed. 2d 497</a></span> (2001) (internal quotation marks omitted). Ajudicial warrant and probable cause are not needed where the search or seizure is justified by “special needs, beyond the normal need for law enforcement,” such as the need to deter drug use in public schools, <em>Vernonia School Dist. 47J </em>v. <em>Acton, </em><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#653" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U.S. 646, 653</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S. Ct. 2386</a></span>, <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L. Ed. 2d 564</a></span> (1995) (internal quotation marks omitted), or the need to ensure that railroad employees engaged in train operations are not under the influence of drugs or alcohol, <em>Skinner </em>v. <em>Railway Labor Executives’ Assn., </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S. Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L. Ed. 2d 639</a></span> (1989); and where the search or seizure is in execution of an administrative warrant authorizing, for example, an inspection of fire-damaged premises to determine the cause,</p>
<p id="b1254-5">[<span class="citation no-link">563 U.S. 737</span>]</p>
<p id="b1254-6"><em>Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#294" aria-description="Citation for case: Michigan v. Clifford">464 U.S. 287, 294</a></span>, <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">104 S. Ct. 641</a></span>, <span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/" aria-description="Citation for case: Michigan v. Clifford">78 L. Ed. 2d 477</a></span> (1984) (plurality opinion), or an inspection of residential premises to ensure compliance with a housing code, <em>Camara </em>v. <em>Municipal Court of City and County of San Francisco, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#535" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 535-538</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S. Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L. Ed. 2d 930</a></span> (1967). But those exceptions do not apply where the officer’s purpose is not to attend to the special needs or to the investigation for which the administrative inspection is justified. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States"><em>Whren, supra, </em>at 811-812</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. The Government seeks to justify the present arrest on the basis of a properly issued judicial warrant—so that the special-needs and administrative-inspection cases cannot be the basis for a purpose inquiry here.</p>
<p id="b1254-9">Apart from those cases, we have almost uniformly rejected invitations to probe subjective intent. See <em>Brigham City </em>v. <em>Stuart, </em><span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/#404" aria-description="Citation for case: Brigham City v. Stuart">547 U.S. 398, 404</a></span>, <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">126 S. Ct. 1943</a></span>, <span class="citation" data-id="9434949"><a href="/opinion/145654/brigham-city-v-stuart/" aria-description="Citation for case: Brigham City v. Stuart">164 L. Ed. 2d 650</a></span> (2006). There is one category of exception, upon which the Court of Appeals principally relied. In <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond, supra,</a></span> </em>we held that the Fourth Amendment could not condone suspicionless vehicle checkpoints set up for the purpose of detecting illegal narcotics. Although we had previously approved vehicle checkpoints set up for the purpose of keeping off the road unlicensed drivers, <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648, 663</a></span>, <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">99 S. Ct. 1391</a></span>, <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">59 L. Ed. 2d 660</a></span> (1979), or alcohol-impaired drivers, <em>Michigan Dept. of State Police </em>v. <em>Sitz, </em><span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">496 U.S. 444</a></span>, <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">110 S. Ct. 2481</a></span>, <span class="citation" data-id="9432063"><a href="/opinion/112459/michigan-department-of-state-police-v-sitz/" aria-description="Citation for case: Michigan Department of State Police v. Sitz">110 L. Ed. 2d 412</a></span> (1990); and for the purpose of interdicting those who illegally cross the border, <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U.S. 543</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">96 S. Ct. 3074</a></span>, <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">49 L. Ed. 2d 1116</a></span> (1976); we found the drug-detection purpose in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>invalidating because it was “ultimately indistinguishable from the general <page-number citation-index="1" label="1157">*1157</page-number>interest in crime control,” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#44" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S., at 44</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>. In the Court of Appeals’ view, <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>established that “ ‘programmatic purpose’ is relevant to Fourth Amendment analysis of programs of seizures without probable cause.” <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#968" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 968</a></span>.</p>
<p id="b1255-4">That was mistaken. It was not the absence of probable cause that triggered the invalidating-purpose inquiry in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>. </em>To the contrary, <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>explicitly said that it would approve checkpoint stops for “general crime control</p>
<p id="b1255-5">[<span class="citation no-link">563 U.S. 738</span>]</p>
<p id="b1255-6">purposes” that were based upon merely “some quantum of individualized suspicion.” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S., at 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>. Purpose was relevant in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>because  “programmatic purposes may be relevant to the validity of Fourth Amendment intrusions undertaken <em>pursuant to a general scheme without individualized, </em>suspicion,” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#45" aria-description="Citation for case: City of Indianapolis v. Edmond"><em>id., </em>at 45-46</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span> (emphasis added).<footnotemark>1</footnotemark></p>
<p id="b1255-7">Needless to say, warrantless, “sus-picionless intrusions pursuant to a general scheme,” <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond"><em>id., </em>at 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>, are far removed from the facts of this case. A warrant issued by a neutral Magistrate Judge authorized al-Kidd’s arrest. The affidavit accompanying the warrant application (as al-Kidd concedes) gave individualized reasons to believe that he was a material witness and that he would soon disappear. The existence of a judicial warrant based on individualized suspicion takes this case outside the domain of not only our special-needs and administrative-search cases, but of <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>as well.</p>
<p id="b1255-9">A warrant based on individualized suspicion<footnotemark>2</footnotemark> in fact grants more protection against the malevolent and the incompetent than existed in most of our cases eschewing inquiries into intent. In <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States"><em>Whren, supra, </em>at 813</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>, and <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/#153" aria-description="Citation for case: Devenpeck v. Alford"><em>Devenpeck, supra, </em>at 153</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">125 S. Ct. 588</a></span>, <span class="citation" data-id="137733"><a href="/opinion/137733/devenpeck-v-alford/" aria-description="Citation for case: Devenpeck v. Alford">160 L. Ed. 2d 537</a></span>, we declined to probe the motives behind seizures supported by probable cause but lacking a warrant approved by a detached magistrate. <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U.S. 1, 21-22</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">88 S. Ct. 1868</a></span>, <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">20 L. Ed. 2d 889</a></span></p>
<p id="b1255-10">[<span class="citation no-link">563 U.S. 739</span>]</p>
<p id="b1255-11">(1968), and <em>Knights, </em><span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/#121" aria-description="Citation for case: United States v. Knights">534 U.S., at 121-122</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">122 S. Ct. 587</a></span>, <span class="citation" data-id="9434170"><a href="/opinion/118468/united-states-v-knights/" aria-description="Citation for case: United States v. Knights">151 L. Ed. 2d 497</a></span>, applied an objective standard to war-rantless searches justified by a lesser showing of reasonable suspicion. We review even some suspicionless searches for objective reasonableness. See <em>Bond, </em><span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/#335" aria-description="Citation for case: Bond v. United States">529 U.S., at 335-336, 338, n. 2</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">120 S. Ct. 1462</a></span>, <span class="citation" data-id="9433930"><a href="/opinion/118354/bond-v-united-states/" aria-description="Citation for case: Bond v. United States">146 L. Ed. 2d 365</a></span>. If concerns about improper motives and pretext do not justify subjective inquiries in those less protective contexts, we see no reason to adopt that inquiry here.</p>
<p id="b1255-12">Al-Kidd would read our cases more narrowly. He asserts that <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>es<page-number citation-index="1" label="1158">*1158</page-number>tablishes that we ignore subjective intent only when there exists “probable cause to believe that a violation of law has occurred,” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States">517 U.S., at 811</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, 135 L. Ed. 2d 89— which was not the case here. That is a distortion of <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span>. </em>Our unanimous opinion held that we would not look behind an objectively reasonable traffic stop to determine whether racial profiling or a desire to investigate other potential crimes was the real motive. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#810" aria-description="Citation for case: Whren v. United States"><em>id., </em>at 810, 813</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. In the course of our analysis, we dismissed Whren’s reliance on our inventory-search and administrative-inspection cases by explaining that those cases do not “endors[e] the principle that ulterior motives can invalidate police conduct that is justifiable on the basis of probable cause to believe that a violation of law has occurred,” <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#811" aria-description="Citation for case: Whren v. United States"><em>id., </em>at 811</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span> But to say that ulterior motives do <em>not </em>invalidate a search that is legitimate because of probable cause to believe a crime has occurred is not to say that it <em>does </em>invalidate all searches that are legitimate for other reasons.</p>
<p id="b1256-4">“[0]nly an undiscerning reader,” <em>ibid., </em>would think otherwise. We referred to probable cause to believe that a violation of law had occurred because that was the legitimating factor in the case at hand. But the analysis of our opinion swept broadly to reject inquiries into motive generally. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States"><em>id., </em>at 812-815</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. We remarked that our special-needs and administrative-inspection cases are unusual in their concern for pretext, and do nothing more than “explain that the exemption from the need for probable cause (and warrant), which is accorded to searches made for the purpose of inventory</p>
<p id="b1256-6">[<span class="citation no-link">563 U.S. 740</span>]</p>
<p id="b1256-7">or administrative regulation, is not accorded to searches that are <em>not </em>made for those purposes,” <span class="citation no-link"><em>id., </em>at 811-812</span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. And our opinion emphasized that we had at that time (prior to <em>Edmond) </em>rejected every request to examine subjective intent outside the narrow context of special needs and administrative inspections. See <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#812" aria-description="Citation for case: Whren v. United States">517 U.S., at 812</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">116 S. Ct. 1769</a></span>, <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">135 L. Ed. 2d 89</a></span>. Thus, al-Kidd’s approach adds an “only” to a sentence plucked from the <em><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span> </em>opinion, and then elevates that sentence (as so revised) over the remainder of the opinion, and over the consistent holdings of our other cases.</p>
<p id="b1256-8">Because al-Kidd concedes that individualized suspicion supported the issuance of the material-witness arrest warrant; and does not assert that his arrest would have been unconstitutional absent the alleged pretextual use of the warrant; we find no Fourth Amendment violation.<footnotemark>3</footnotemark> Efficient<footnotemark>4</footnotemark> and evenhanded application of the law de<page-number citation-index="1" label="1159">*1159</page-number>mands that we look to whether the arrest is objectively justified, rather than to the motive of the arresting officer.</p>
<p id="b1257-4">[<span class="citation no-link">563 U.S. 741</span>]</p>
<p id="b1257-5">B</p>
<p id="b1257-6">A Government official’s conduct violates clearly established law when, at the time of the challenged conduct, “[t]he contours of [a] right [are] sufficiently clear” that every “reasonable official would [have understood] that what he is doing violates that right.” <em>Anderson </em>v. Creighton, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton">483 U.S. 635, 640</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">107 S. Ct. 3034</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">97 L. Ed. 2d 523</a></span> (1987). We do not require a case directly on point, but existing precedent must have placed the statutory or constitutional question beyond debate. See <em>ibid.; Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs">475 U.S. 335, 341</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">106 S. Ct. 1092</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">89 L. Ed. 2d 271</a></span> (1986). The constitutional question in this case falls far short of that threshold.</p>
<p id="b1257-7">At the time of al-Kidd’s arrest, not a single judicial opinion had held that pretext could render an objectively reasonable arrest pursuant to a material-witness warrant unconstitutional. A district-court opinion had suggested, in a footnoted dictum devoid of supporting citation, that using such a warrant for preventive detention of suspects “is an illegitimate use of the statute”—implying (we accept for the sake of argument) that the detention would therefore be unconstitutional. Uni<em>ted States </em>v. <em>Awadallah, </em><span class="citation" data-id="2518594"><a href="/opinion/2518594/united-states-v-awadallah/#77" aria-description="Citation for case: United States v. Awadallah">202 F. Supp. 2d 55, 77, n. 28</a></span> (SDNY 2002). The Court of Appeals thought nothing could “have given John Ashcroft fair[er] warning” that his conduct violated the Fourth Amendment, because the footnoted dictum <em>“callfed] out Ashcroft by name”! </em><span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#972" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 972-973</a></span> (internal quotation marks omitted; emphasis added). We will indulge the assumption (though it does not seem to us realistic) that Justice Department lawyers bring to the Attorney General’s personal attention all district judges’ footnoted speculations that boldly “call him out by name.” On that assumption, would it prove that for him (and for him only?) it became clearly established that pretextual use of the material-witness statute rendered the arrest unconstitutional? An extraordinary proposition. Even a district judge’s <em>ipse dixit </em>of a holding is not “controlling authority” in any jurisdiction, much less in the entire United States; and his <em>ipse dixit </em>of a footnoted dictum falls far short</p>
<p id="AuOq">[<span class="citation no-link">563 U.S. 742</span>]</p>
<p id="b1257-9">of what is necessary absent controlling authority: a robust “consensus of cases of persuasive authority.” <em>Wilson </em>v. <em>Layne, </em><span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#617" aria-description="Citation for case: Wilson v. Layne">526 U.S. 603, 617</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span> (1999).</p>
<p id="b1257-11">The Court of Appeals’ other cases “clearly establishing” the constitutional violation are, of course, those we rejected as irrelevant in our discussion of whether there was any constitutional violation at all. And the Court of Appeals’ reference to those cases here makes the same error of assuming that purpose is only disregarded when there is probable cause to suspect a violation of law.</p>
<p id="b1257-12">The Court of Appeals also found clearly established law lurking in the broad “history and purposes of the Fourth Amendment.” <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#971" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 971</a></span>. We have repeatedly told courts— <page-number citation-index="1" label="1160">*1160</page-number>and the Ninth Circuit in particular, see <em>Brosseau </em>v. <em>Haugen, </em><span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/#198" aria-description="Citation for case: Brosseau v. Haugen">543 U.S. 194, 198-199</a></span>, <span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/" aria-description="Citation for case: Brosseau v. Haugen">125 S. Ct. 596</a></span>, <span class="citation" data-id="9434715"><a href="/opinion/137736/brosseau-v-haugen/" aria-description="Citation for case: Brosseau v. Haugen">160 L. Ed. 2d 583</a></span> (2004) <em>(per </em>curiam)—not to define clearly established law at a high level of generality. See also, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#615" aria-description="Citation for case: Wilson v. Layne"><em>e.g., Wilson, supra, </em>at 615</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span>; <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton"><em>Anderson, supra, </em>at 639-640</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">107 S. Ct. 3034</a></span>, <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">97 L. Ed. 2d 523</a></span>; cf. <em>Sawyer </em>v. <em>Smith, </em><span class="citation" data-id="9432105"><a href="/opinion/112477/sawyer-v-smith/#236" aria-description="Citation for case: Sawyer v. Smith">497 U.S. 227, 236</a></span>, <span class="citation" data-id="9432105"><a href="/opinion/112477/sawyer-v-smith/" aria-description="Citation for case: Sawyer v. Smith">110 S. Ct. 2822</a></span>, <span class="citation" data-id="9432105"><a href="/opinion/112477/sawyer-v-smith/" aria-description="Citation for case: Sawyer v. Smith">111 L. Ed. 2d 193</a></span> (1990). The general proposition, for example, that an unreasonable search or seizure violates the Fourth Amendment is of little help in determining whether the violative nature of particular conduct is clearly established. See <em>Saucier </em>v. <em>Katz, </em><span class="citation multiple-matches"><a href="/c/U.S./533/194/">533 U.S. 194</a></span>, 201-202, <span class="citation multiple-matches"><a href="/c/S.%20Ct./121/2151/">121 S. Ct. 2151</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/150/272/">150 L. Ed. 2d 272</a></span> (2001); <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#615" aria-description="Citation for case: Wilson v. Layne"><em>Wilson, supra, </em>at 615</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span>.</p>
<p id="b1258-4">The same is true of the Court of Appeals’ broad historical assertions. The Fourth Amendment was a response to the English Crown’s use of general warrants, which often allowed royal officials to search and seize whatever and whomever they pleased while investigating crimes or affronts to the Crown. See <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U.S. 476, 481-485</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">85 S. Ct. 506</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L. Ed. 2d 431</a></span> (1965). According to the Court of Appeals, Ashcroft should have seen that a pre-textual warrant similarly “gut[s] the substantive protections of the Fourth Amendmen[t]” and allows the State “to arrest upon the executive’s mere suspicion.” <span class="citation" data-id="9561127"><a href="/opinion/1204118/al-kidd-v-ashcroft/#972" aria-description="Citation for case: Al-Kidd v. Ashcroft">580 F.3d, at 972</a></span>.</p>
<p id="b1258-5">Ashcroft must be forgiven for missing the parallel, which escapes us as well. The principal evil of the general warrant</p>
<p id="b1258-6">[<span class="citation no-link">563 U.S. 743</span>]</p>
<p id="b1258-7">was addressed by the Fourth Amendment’s particularity requirement, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#485" aria-description="Citation for case: Stanford v. Texas"><em>Stanford, supra, </em>at 485</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">85 S. Ct. 506</a></span>, <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">13 L. Ed. 2d 431</a></span>, which Ashcroft’s alleged policy made no effort to evade. The warrant authorizing al-Kidd’s arrest named al-Kidd and only al-Kidd. It might be argued, perhaps, that when, in response to the English abuses, the Fourth Amendment said that warrants could only issue “on probable cause” it meant only probable cause to suspect a violation of law, and not probable cause to believe that the individual named in the warrant was a material witness. But that would make <em>all </em>arrests pursuant to material-witness warrants unconstitutional, whether pretextual or not—and that is not the position taken by al-Kidd in this case.</p>
<p id="b1258-9">While featuring a District Court’s footnoted dictum, the Court of Appeals made no mention of this Court’s affirmation in <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span> </em>of the “pre-dominan [t]” rule that reasonableness is an objective inquiry, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/#47" aria-description="Citation for case: City of Indianapolis v. Edmond">531 U.S., at 47</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">121 S. Ct. 447</a></span>, <span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">148 L. Ed. 2d 333</a></span>. Nor did it mention <em>Whren’s </em>and <em>Knights’ </em>statements that subjective intent mattered in a very limited subset of our Fourth Amendment cases; or <em>Terry’s </em>objective evaluation of investigatory searches premised on reasonable suspicion rather than probable cause; or <em>Bond’s </em>objective evaluation of a suspicionless investigatory search. The Court of Appeals seems to have cherry-picked the aspects of our opinions that gave colorable support to the proposition that the unconstitutionality of the action here was clearly established.</p>
<p id="b1258-10">Qualified immunity gives government officials breathing room to make reasonable but mistaken judgments about open legal questions. When properly applied, it protects “all but the plainly incompetent or those who knowingly violate the law.” <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#341" aria-description="Citation for case: Malley v. Briggs"><em>Malley, supra, </em>at 341</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">106 S. Ct. 1092</a></span>, <span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/" aria-description="Citation for case: Malley v. Briggs">89 L. Ed. 2d 271</a></span>. Ashcroft deserves neither label, not least because eight Court of Appeals judges agreed with <page-number citation-index="1" label="1161">*1161</page-number>his judgment in a case of first impression. See <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/#618" aria-description="Citation for case: Wilson v. Layne"><em>Wilson, supra, </em>at 618</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">119 S. Ct. 1692</a></span>, <span class="citation" data-id="9433801"><a href="/opinion/118289/wilson-v-layne/" aria-description="Citation for case: Wilson v. Layne">143 L. Ed. 2d 818</a></span>. He deserves qualified immunity even assuming—contrafactually—that his alleged detention policy violated the Fourth Amendment.</p>
<p id="b1259-4">[<span class="citation no-link">563 U.S. 744</span>]</p>
<p id="pArzU">
<img class="p" height="36" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ8AAAAlAQAAAAB0FFF3AAAAlElEQVR4nO3Ouw3CUAyF4T8WooWGHpiAFZiKMWAjxCx0VOkSoeBDh6/iK4WCgiLuPuv4gSTdVdQYbsBzceFTGQZ062jWIKk/rWJ1ghuwvB5isAJJupUfjuEGsC/OVyBJm3JwDDfgtdvGXIYBw7GNbgWS2u4cqxO8Efijj+UJMsCG4nyGMVlfRBpNJfSbQ3Nkjvxl5A3isMVNie1/OQAAAABJRU5ErkJggg==" width="271"/>
</p>
<p id="b1259-5">We hold that an objectively reasonable arrest and detention of a material witness pursuant to a validly obtained warrant cannot be challenged as unconstitutional on the basis of allegations that the arresting authority had an improper motive. Because Ashcroft did not violate clearly established law, we need not address the more difficult question whether he enjoys absolute immunity. The judgment of the Court of Appeals is reversed, and the case is remanded for further proceedings consistent with this opinion.</p>
<p id="b1259-7">It is so ordered.</p>
<p id="Acxs">Justice Kagan took no part in the consideration or decision of this case.</p>
<footnote label="1">
<p id="b1255-13">. The Court of Appeals also relied upon <em>Ferguson </em>v. <em>Charleston, </em><span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">532 U.S. 67</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">121 S. Ct. 1281</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">149 L. Ed. 2d 205</a></span> (2001), which held unconstitutional a program of mandatory drug testing of maternity patients. Like <em><span class="citation" data-id="9434014"><a href="/opinion/118391/city-of-indianapolis-v-edmond/" aria-description="Citation for case: City of Indianapolis v. Edmond">Edmond</a></span>, </em>that case involved a general scheme of searches without individualized suspicion. <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/#77" aria-description="Citation for case: Ferguson v. City of Charleston">532 U.S., at 77, n. 10</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">121 S. Ct. 1281</a></span>, <span class="citation" data-id="9434054"><a href="/opinion/118414/ferguson-v-city-of-charleston/" aria-description="Citation for case: Ferguson v. City of Charleston">149 L. Ed. 2d 205</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b1255-14">. Justice Ginsburg suggests that our use of the word “suspicion” is peculiar because that word “ordinarily” means “that the person suspected has engaged in wrongdoing.” <em>Post, </em>at 749, n. 3, 179 L. Ed. 2d, at 1164 (opinion concurring in judgment). We disagree. No usage of the word is more common and idiomatic than a statement such as “I have a suspicion he knows something about the crime,” or even “I have a suspicion she is throwing me a surprise birthday party.” The many cases cited by Justice Ginsburg, <em>post, </em>at 749-750, n. 3, 179 L. Ed. 2d, at 1164-1165, which use the neutral word “suspicion” <em>in connection with </em>wrongdoing, prove nothing except that searches and seizures for reasons other than suspected wrongdoing are rare.</p>
</footnote>
<footnote label="3">
<p id="b1256-9">. The concerns of Justices Ginsburg and Sotomayor about the validity of the warrant in this case are beside the point. See <em>post, </em>at 748-749, 179 L. Ed. 2d, at 1163-1164 (Ginsburg, J., concurring in judgment); <em>post, </em>at 752, 179 L. Ed. 2d, at 1166 (Sotomayor, J., concurring in judgment). The validity of the warrant is not <em>our </em>“opening assumption,’’ <em>post, </em>at 749, 179 L. Ed. 2d, at 1164 (Ginsburg, J., concurring in judgment); it is the premise of al-Kidd’s argument. Al-Kidd does not claim that Ashcroft is liable because the FBI agents failed to obtain a valid warrant. He takes the validity of the warrant as a given, and argues that his arrest nevertheless violated the Constitution because it was motivated by an illegitimate purpose. His separate Fourth Amendment and statutory claims against the FBI agents who sought the material-witness warrant, which are the focus of both concurrences, are not before us.</p>
</footnote>
<footnote label="4">
<p id="b1256-10">. We may note in passing that al-Kidd alleges that the Attorney General authorized the use of material-witness warrants for detention of suspected terrorists, but not that he forbade the use of <page-number citation-index="1" label="1159">*1159</page-number>those warrants to detain material witnesses. Which means that if al-Kidd’s inquiry into actual motive is accepted, mere determination that the Attorney General promulgated the alleged policy would not alone decide the case. Al-Kidd would also have to prove that the officials who sought his material-arrest warrant were motivated by Ashcroft’s policy, not by a desire to call al-Kidd as a witness.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Atwater v. City of Lago Vista.md  (`case`, 7 assertions)

### content_page

```
---
title: "Atwater v. City of Lago Vista"
type: case
citation: ""
parallel_cite: "532 U.S. 318; 121 S. Ct. 1536; 149 L. Ed. 2d 549; 2001 Daily Journal DAR 3953; 2001 Colo. J. C.A.R. 2069; 14 Fla. L. Weekly Fed. S 193; 69 U.S.L.W. 4262"
neutral_cite: "2001 U.S. LEXIS 3366; 2001 Cal. Daily Op. Serv. 3203"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2001
date_decided: 2001-04-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2001-04-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Atwater v. City of Lago Vista
  varies_by_point: false
  scope_note: "Good law. If an officer has probable cause to believe a person has committed even a very minor criminal offense (including a fine-only misdemeanor) in his presence, a warrantless custodial arrest does not violate the Fourth Amendment; no case-by-case balancing is required. Extended by Virginia v. Moore (2008)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2620702/atwater-v-city-of-lago-vista/"
  cluster_id: 2620702
  opinion_id: 2620702
  identity_checked: true
homes:
  - page: "[[Arrest and Arrest Warrants]]"
    role: "Key — Anchor (minor-offense custodial arrest on probable cause)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
related: ["[[Whren v. United States]]", "[[Arkansas v. Sullivan]]", "[[Devenpeck v. Alford]]", "[[Tennessee v. Garner]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "probable-cause", "misdemeanor", "seizure"]
holding: "A warrantless custodial arrest for a fine-only misdemeanor committed in the officer's presence, supported by probable cause, does not violate the Fourth Amendment; probable cause governs all arrests without individualized balancing."
lake:
  record_id: Atwater v. City of Lago Vista
  status: verified
  projected_at: 2026-07-06
---

# Atwater v. City of Lago Vista

*532 U.S. 318 (2001)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gail Atwater was driving her pickup in Lago Vista, Texas, with her two young children; none of them was wearing a seatbelt, a misdemeanor punishable under Texas law only by a fine. Officer Turek stopped her, and rather than issue a citation, he handcuffed her, placed her in his squad car, and took her to the police station, where she was booked — required to remove her shoes, jewelry, and glasses, photographed, and held in a cell for about an hour before being taken to a magistrate and released on bond. She ultimately pleaded no contest and paid a $50 fine, then sued the City, the police chief, and Officer Turek under 42 U.S.C. § 1983, contending the custodial arrest was an unreasonable seizure.

## Issue
Whether the Fourth Amendment forbids a warrantless custodial arrest, supported by probable cause, for a minor criminal offense — such as a misdemeanor seatbelt violation punishable only by a fine — committed in the officer's presence.

## Rule
No. Probable cause governs all arrests, without case-by-case balancing: the Court "confirm[ed] today what our prior cases have intimated: the standard of probable cause 'applie[s] to all arrests, without the need to "balance" the interests and circumstances involved in particular situations.' . . . If an officer has probable cause to believe that an individual has committed even a very minor criminal offense in his presence, he may, without violating the Fourth Amendment, arrest the offender." — 532 U.S. at 354. ^pin-354

That categorical rule yields to individualized review only where an arrest is "conducted in an extraordinary manner, unusually harmful to [the arrestee's] privacy or even physical interests" (quoting *Whren v. United States*).

## Application
There was no dispute that Officer Turek had probable cause: Atwater admitted that neither she nor her children were belted, a crime committed in his presence, so he was "authorized (not required, but authorized) to make a custodial arrest without balancing costs and benefits or determining whether or not Atwater's arrest was in some sense necessary." Nor was the arrest carried out in an extraordinary manner — she was handcuffed, taken to the station, booked in the ordinary way, and held about an hour before release on bond. As the Court concluded: "The arrest and booking were inconvenient and embarrassing to Atwater, but not so extraordinary as to violate the Fourth Amendment." — *Id.* at 355. ^pin-355

## Conclusion
The warrantless custodial arrest for the fine-only seatbelt offense, supported by probable cause and executed in an ordinary manner, was reasonable; the [[Reading and Citing Cases#en-banc|en banc]] Court of Appeals' judgment for the defendants was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Atwater*'s categorical rule is extended by [[Virginia v. Moore]] (an arrest on probable cause is reasonable under the Fourth Amendment even if it violates state arrest law) and is consistent with the objective, motive-irrelevant approach of [[Whren v. United States]], [[Arkansas v. Sullivan]] (its same-day companion), and [[Devenpeck v. Alford]].

## Appears on
- [[Arrest and Arrest Warrants]] — *Key — Anchor*
- [[Seizure of the Person]] — *Related (cross-doctrine)*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *Atwater v. City of Lago Vista*, 532 U.S. 318 (2001) — https://www.courtlistener.com/opinion/2620702/atwater-v-city-of-lago-vista/ — pinpoints: 354, 355.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9f9a0d6b9d41cd94", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2001 U.S. LEXIS 3366; 2001 Cal. Daily Op. Serv. 3203", "official_citation_present": false, "parallel_cite": "532 U.S. 318; 121 S. Ct. 1536; 149 L. Ed. 2d 549; 2001 Daily Journal DAR 3953; 2001 Colo. J. C.A.R. 2069; 14 Fla. L. Weekly Fed. S 193; 69 U.S.L.W. 4262", "title": "Atwater v. City of Lago Vista", "year": "2001"}}
{"assertion_id": "4021178f4cb225a8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless custodial arrest for a fine-only misdemeanor committed in the officer's presence, supported by probable cause, does not violate the Fourth Amendment; probable cause governs all arrests without individualized balancing.", "title": "Atwater v. City of Lago Vista"}}
{"assertion_id": "6750bbb31af1dfdc", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Related (cross-doctrine)", "title": "Atwater v. City of Lago Vista"}}
{"assertion_id": "8fbc17905ddb1b1a", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest and Arrest Warrants"}, "payload": {"home": "Arrest and Arrest Warrants", "role": "Key — Anchor (minor-offense custodial arrest on probable cause)", "title": "Atwater v. City of Lago Vista"}}
{"assertion_id": "e34bcb44b2751d88", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Related (cross-doctrine)", "title": "Atwater v. City of Lago Vista"}}
{"assertion_id": "96771fcfb981f7a9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2001-04-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Atwater v. City of Lago Vista", "field_i_validity": "good_law", "scope_note": "Good law. If an officer has probable cause to believe a person has committed even a very minor criminal offense (including a fine-only misdemeanor) in his presence, a warrantless custodial arrest does not violate the Fourth Amendment; no case-by-case balancing is required. Extended by Virginia v. Moore (2008).", "title": "Atwater v. City of Lago Vista", "varies_by_point": "false"}}
{"assertion_id": "cd5bbba1dc5a10c8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Atwater v. City of Lago Vista"}}
```

### lake record — Atwater v. City of Lago Vista

```json
{
  "schema_version": "s2.v1",
  "record_id": "Atwater v. City of Lago Vista",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Atwater v. City of Lago Vista",
    "case_name_short": "Atwater",
    "case_name_full": "ATWATER Et Al. v. CITY OF LAGO VISTA Et Al.",
    "input_case_name": "Atwater v. City of Lago Vista",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2001-04-24",
    "year": 2001,
    "docket": null,
    "cluster_id": 2620702,
    "lead_opinion_id": 2620702,
    "sibling_ids": [
      2620702,
      9795084,
      9795085
    ],
    "absolute_url": "/opinion/2620702/atwater-v-city-of-lago-vista/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9199445,
        "score": 10,
        "case_name": "Atwater v. City of Lago Vista"
      },
      {
        "cluster_id": 9199444,
        "score": 10,
        "case_name": "Atwater v. City of Lago Vista"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "532 U.S. 318",
        "volume": "532",
        "reporter": "U.S.",
        "page": "318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1536",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1536",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 549",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "549",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Daily Journal DAR 3953",
        "volume": "2001",
        "reporter": "Daily Journal DAR",
        "page": "3953",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Colo. J. C.A.R. 2069",
        "volume": "2001",
        "reporter": "Colo. J. C.A.R.",
        "page": "2069",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 193",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4262",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4262",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2001 U.S. LEXIS 3366",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "3366",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Cal. Daily Op. Serv. 3203",
        "volume": "2001",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3203",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "532 U.S. 318",
        "volume": "532",
        "reporter": "U.S.",
        "page": "318",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "121 S. Ct. 1536",
        "volume": "121",
        "reporter": "S. Ct.",
        "page": "1536",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "149 L. Ed. 2d 549",
        "volume": "149",
        "reporter": "L. Ed. 2d",
        "page": "549",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 U.S. LEXIS 3366",
        "volume": "2001",
        "reporter": "U.S. LEXIS",
        "page": "3366",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Daily Journal DAR 3953",
        "volume": "2001",
        "reporter": "Daily Journal DAR",
        "page": "3953",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Colo. J. C.A.R. 2069",
        "volume": "2001",
        "reporter": "Colo. J. C.A.R.",
        "page": "2069",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "14 Fla. L. Weekly Fed. S 193",
        "volume": "14",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "193",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "69 U.S.L.W. 4262",
        "volume": "69",
        "reporter": "U.S.L.W.",
        "page": "4262",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2001 Cal. Daily Op. Serv. 3203",
        "volume": "2001",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "3203",
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
      "id": "pin-354",
      "page": null,
      "quote": "--- # Atwater v. City of Lago Vista *532 U.S. 318 (2001)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gail Atwater was driving her pickup in Lago Vista, Texas, with her two young children; none of them was wearing a seatbelt, a misdemeanor punishable under Texas law only by a fine. Officer Turek stopped her, and rather than issue a citation, he handcuffed her, placed her in his squad car, and took her to the police station, where she was booked \u2014 required to remove her shoes, jewelry, and glasses, photographed, and held in a cell for about an hour before being taken to a magistrate and released on bond. She ultimately pleaded no contest and paid a $50 fine, then sued the City, the police chief, and Officer Turek under 42 U.S.C. \u00a7 1983, contending the custodial arrest was an unreasonable seizure. ## Issue Whether the Fourth Amendment forbids a warrantless custodial arrest, supported by probable cause, for a minor criminal offense \u2014 such as a misdemeanor seatbelt violation punishable only by a fine \u2014 committed in the officer's presence. ## Rule No. Probable cause governs all arrests, without case-by-case balancing: the Court",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-355",
      "page": null,
      "quote": "(quoting *Whren v. United States*). ## Application There was no dispute that Officer Turek had probable cause: Atwater admitted that neither she nor her children were belted, a crime committed in his presence, so he was",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2001-04-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Atwater v. City of Lago Vista",
    "varies_by_point": false,
    "scope_note": "Good law. If an officer has probable cause to believe a person has committed even a very minor criminal offense (including a fine-only misdemeanor) in his presence, a warrantless custodial arrest does not violate the Fourth Amendment; no case-by-case balancing is required. Extended by Virginia v. Moore (2008).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Buckley",
          "cluster_id": 4468007,
          "cite": [
            "90 N.E.3d 767",
            "478 Mass. 861"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Stephens v. Nick Degiovanni, individually",
          "cluster_id": 4379656,
          "cite": [
            "852 F.3d 1298",
            "2017 U.S. App. LEXIS 5548",
            "2017 WL 1174381"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phyllis J. May v. City of Nahunta, Georgia",
          "cluster_id": 4339893,
          "cite": [
            "846 F.3d 1320",
            "2017 WL 218838",
            "2017 U.S. App. LEXIS 985"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Pegg v. Grant Herrnberger",
          "cluster_id": 4335908,
          "cite": [
            "845 F.3d 112",
            "2017 WL 35722",
            "2017 U.S. App. LEXIS 109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ted Phillips",
          "cluster_id": 4250252,
          "cite": [
            "834 F.3d 1176",
            "2016 WL 4435613"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Campuzano",
          "cluster_id": 7428164,
          "cite": [
            "237 Cal. App. Supp. 4th 14",
            "188 Cal. Rptr. 3d 587",
            "2015 Cal. App. LEXIS 489"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane1_negative"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Pringle",
          "cluster_id": 131150,
          "cite": [
            "157 L. Ed. 2d 769",
            "124 S. Ct. 795",
            "540 U.S. 366",
            "2003 U.S. LEXIS 9198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kim D. Lee v. Luis Ferraro",
          "cluster_id": 75789,
          "cite": [
            "284 F.3d 1188",
            "2002 U.S. App. LEXIS 3438",
            "2002 WL 340670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Laurie Tsao v. Desert Palace, Inc.",
          "cluster_id": 810771,
          "cite": [
            "698 F.3d 1128",
            "2012 WL 5200336"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gary Blankenhorn v. City of Orange Andy Romero Dung Nguyen Garrett Ross Tamara South Gray, Sergeant Montano, Officer Kayano, Officer Roman, Officer",
          "cluster_id": 797658,
          "cite": [
            "485 F.3d 463",
            "2007 U.S. App. LEXIS 10856",
            "2007 D.A.R. 6484"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thornton v. United States",
          "cluster_id": 134746,
          "cite": [
            "158 L. Ed. 2d 905",
            "124 S. Ct. 2127",
            "541 U.S. 615",
            "2004 U.S. LEXIS 3681"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Koch v. City of Del City",
          "cluster_id": 616534,
          "cite": [
            "660 F.3d 1228",
            "2011 U.S. App. LEXIS 22095",
            "2011 WL 5176164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melvin Alan Wood v. Michael Kesler, individually and in his capacity as an Alabama State Trooper, Brian Jones",
          "cluster_id": 76122,
          "cite": [
            "323 F.3d 872",
            "2003 U.S. App. LEXIS 3857",
            "2003 WL 722756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
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
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Utah v. Strieff",
          "cluster_id": 3214882,
          "cite": [
            "579 U.S. 232",
            "195 L. Ed. 2d 400",
            "2016 U.S. LEXIS 3926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Woodard",
          "cluster_id": 2540788,
          "cite": [
            "341 S.W.3d 404",
            "2011 Tex. Crim. App. LEXIS 447",
            "2011 WL 1261320"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tracy Williams v. Brandon Brooks",
          "cluster_id": 3167211,
          "cite": [
            "809 F.3d 936",
            "2016 U.S. App. LEXIS 68",
            "2016 WL 51409"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Aguilar",
          "cluster_id": 2650810,
          "cite": [
            "2013 IL 112116"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Atwater v. City of Lago Vista:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2620702 OR 9795084 OR 9795085) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzU1ODc1MjAwMDAwJnM9ODcyMTU0MSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%282620702+OR+9795084+OR+9795085%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(2620702 OR 9795084 OR 9795085)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMTMmcz03OTI1MDUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%282620702+OR+9795084+OR+9795085%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(2620702 OR 9795084 OR 9795085)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 0,
        "triage_snippet_classified": 35
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2620702 OR 9795084 OR 9795085)",
    "indexed_citing_opinions": 701,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2620702,
        "count": 612,
        "count_source": "search"
      },
      {
        "opinion_id": 9795084,
        "count": 101,
        "count_source": "search"
      },
      {
        "opinion_id": 9795085,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1392,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/atwater-v-city-of-lago-vista.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NjkwNiZzPTk0NTA1NDUmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%282620702+OR+9795084+OR+9795085%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2620702,
        "cited_id": 85827,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 96744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 108894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109402,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 109932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 112595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 117936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 117964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 546349,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2620702,
        "cited_id": 3585438,
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
    "date_created": "2026-07-04T19:10:49Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:11:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:11:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:16:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:11:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Atwater v. City of Lago Vista (truncated)

```
<div>
<center><b><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U.S. 318</a></span> (2001)</b></center>
<center><h1>ATWATER et al.<br>
v.<br>
CITY OF LAGO VISTA et al.</h1></center>
<center>No. 99-1408.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued December 4, 2000.</center>
<center>Decided April 24, 2001.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT
<p><span class="star-pagination">*320</span> <span class="star-pagination">*320</span> <span class="star-pagination">*321</span> <span class="star-pagination">*322</span> Souter, J., delivered the opinion of the Court, in which Rehnquist, C. J., and Scalia, Kennedy, and Thomas, JJ., joined. O'Connor, J., filed a dissenting opinion, in which Stevens, Ginsburg, and Breyer, JJ., joined, <i>post,</i> p. 360.</p>
<p><i>Robert C. DeCarli</i> argued the cause for petitioners. With him on the briefs were <i>Debra Irwin, Pamela McGraw,</i> and <i>Michael F. Sturley.</i> </p>
<p><i>R. James George, Jr.,</i> argued the cause for respondents. With him on the brief were <i>William W. Krueger III</i> and <i>Joanna R. Lippman.</i> </p>
<p><i>Gregory S. Coleman,</i> Solicitor General of Texas, argued the cause for the State of Texas et al. as <i>amici curiae</i> urging affirmance. With him on the brief were <i>John Cornyn,</i> Attorney General, <i>Andy Taylor,</i> First Assistant Attorney General, and <i>Lisa R. Eskow,</i> Assistant Attorney General, and the Attorneys General for their respective States as follows: <i>Mark Pryor</i> of Arkansas, <i>Ken Salazar</i> of Colorado, <i>M. Jane Brady</i> of Delaware, <i>Carla J. Stovall</i> of Kansas, <i>J. Joseph Curran, Jr.,</i> of Maryland, <i>Joseph P. Mazurek</i> of Montana, <span class="star-pagination">*323</span> <i>W. A. Drew Edmondson</i> of Oklahoma, <i>Charles M. Condon</i> of South Carolina, and <i>Mark L. Earley</i> of Virginia.<sup>[*]</sup></p>
<p>Justice Souter, delivered the opinion of the Court.</p>
<p>The question is whether the Fourth Amendment forbids a warrantless arrest for a minor criminal offense, such as a misdemeanor seatbelt violation punishable only by a fine. We hold that it does not.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>In Texas, if a car is equipped with safety belts, a frontseat passenger must wear one, <span class="citation no-link">Tex. Transp. Code Ann. § 545.413</span>(a) (1999), and the driver must secure any small child riding in front, § 545.413(b). Violation of either provision is "a misdemeanor punishable by a fine not less than $25 or more than $50." § 545.413(d). Texas law expressly authorizes "[a]ny peace officer [to] arrest without warrant a person found committing a violation" of these seatbelt laws, § 543.001, although it permits police to issue citations in lieu of arrest, §§ 543.003-543.005.</p>
<p>In March 1997, petitioner Gail Atwater was driving her pickup truck in Lago Vista, Texas, with her 3-year-old son and 5-year-old daughter in the front seat. None of them was <span class="star-pagination">*324</span> wearing a seatbelt. Respondent Bart Turek, a Lago Vista police officer at the time, observed the seatbelt violations and pulled Atwater over. According to Atwater's complaint (the allegations of which we assume to be true for present purposes), Turek approached the truck and "yell[ed]" something to the effect of "[w]e've met before" and "[y]ou're going to jail." App. 20.<sup>[1]</sup> He then called for backup and asked to see Atwater's driver's license and insurance documentation, which state law required her to carry. <span class="citation no-link">Tex. Transp. Code Ann. §§ 521.025</span>, 601.053 (1999). When Atwater told Turek that she did not have the papers because her purse had been stolen the day before, Turek said that he had "heard that story two-hundred times." App. 21.</p>
<p>Atwater asked to take her "frightened, upset, and crying" children to a friend's house nearby, but Turek told her, "[y]ou're not going anywhere." <i><span class="citation no-link">Ibid.</span></i> As it turned out, Atwater's friend learned what was going on and soon arrived to take charge of the children. Turek then handcuffed Atwater, placed her in his squad car, and drove her to the local police station, where booking officers had her remove her shoes, jewelry, and eyeglasses, and empty her pockets. Officers took Atwater's "mug shot" and placed her, alone, in a jail cell for about one hour, after which she was taken before a magistrate and released on $310 bond.</p>
<p>Atwater was charged with driving without her seatbelt fastened, failing to secure her children in seatbelts, driving without a license, and failing to provide proof of insurance. She ultimately pleaded no contest to the misdemeanor seatbelt offenses and paid a $50 fine; the other charges were dismissed.</p>
<p></p>
<h2>
<span class="star-pagination">*325</span> B</h2>
<p>Atwater and her husband, petitioner Michael Haas, filed suit in a Texas state court under <span class="citation no-link">42 U. S. C. § 1983</span> against Turek and respondents City of Lago Vista and Chief of Police Frank Miller. So far as concerns us, petitioners (whom we will simply call Atwater) alleged that respondents (for simplicity, the City) had violated Atwater's Fourth Amendment "right to be free from unreasonable seizure," App. 23, and sought compensatory and punitive damages.</p>
<p>The City removed the suit to the United States District Court for the Western District of Texas. Given Atwater's admission that she had "violated the law" and the absence of any allegation "that she was harmed or detained in any way inconsistent with the law," the District Court ruled the Fourth Amendment claim "meritless" and granted the City's summary judgment motion. No. A-97 CA 679 SS (WD Tex., Feb. 13, 1999), App. to Pet. for Cert. 50a63a. A panel of the United States Court of Appeals for the Fifth Circuit reversed. <span class="citation" data-id="6980792"><a href="/opinion/7076046/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">165 F. 3d 380</a></span> (1999). It concluded that "an arrest for a first-time seat belt offense" was an unreasonable seizure within the meaning of the Fourth Amendment, <span class="citation" data-id="6980792"><a href="/opinion/7076046/atwater-v-city-of-lago-vista/#387" aria-description="Citation for case: Atwater v. City of Lago Vista"><i>id.,</i> at 387</a></span>, and held that Turek was not entitled to qualified immunity, <span class="citation" data-id="6980792"><a href="/opinion/7076046/atwater-v-city-of-lago-vista/#389" aria-description="Citation for case: Atwater v. City of Lago Vista"><i>id.,</i> at 389</a></span>.</p>
<p>Sitting en banc, the Court of Appeals vacated the panel's decision and affirmed the District Court's summary judgment for the City. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d 242</a></span> (CA5 1999). Relying on <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), the en banc court observed that, although the Fourth Amendment generally requires a balancing of individual and governmental interests, where "an arrest is based on probable cause then `with rare exceptions . . .the result of that balancing is not in doubt.' " <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d, at 244</a></span> (quoting <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#817" aria-description="Citation for case: Whren v. United States"><i>Whren, supra,</i> at 817</a></span>). Because "[n]either party dispute[d] that Officer Turek had probable cause to arrest Atwater," and because "there [was] no evidence in the record that Officer Turek conducted the arrest in an `extraordinary manner, unusually harmful' to Atwater's <span class="star-pagination">*326</span> privacy interests," the en banc court held that the arrest was not unreasonable for Fourth Amendment purposes. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d, at 245</a></span>-246 (quoting <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States"><i>Whren, supra,</i> at 818</a></span>).</p>
<p>Three judges issued dissenting opinions. On the understanding that citation is the "usual procedure" in a traffic stop situation, Judge Reynaldo Garza thought Atwater's arrest unreasonable, since there was no particular reason for taking her into custody. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/#246" aria-description="Citation for case: Atwater v. City of Lago Vista">195 F. 3d, at 246-247</a></span>. Judge Weiner likewise believed that "even with probable cause, [an] officer must have a plausible, articulable reason" for making a custodial arrest. <span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/#251" aria-description="Citation for case: Atwater v. City of Lago Vista"><i>Id.,</i> at 251</a></span>. Judge Dennis understood the Fourth Amendment to have incorporated an earlier, common-law prohibition on warrantless arrests for misdemeanors that do not amount to or involve a "breach of the peace." <i><span class="citation" data-id="6984286"><a href="/opinion/7079285/atwater-v-city-of-lago-vista/" aria-description="Citation for case: Atwater v. City of Lago Vista">Ibid.</a></span></i> </p>
<p>We granted certiorari to consider whether the Fourth Amendment, either by incorporating common-law restrictions on misdemeanor arrests or otherwise, limits police officers' authority to arrest without warrant for minor criminal offenses. <span class="citation multiple-matches"><a href="/c/U.%20S./530/1260/">530 U. S. 1260</a></span> (2000). We now affirm.</p>
<p></p>
<h2>II</h2>
<p>The Fourth Amendment safeguards "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures." In reading the Amendment, we are guided by "the traditional protections against unreasonable searches and seizures afforded by the common law at the time of the framing," <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#931" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927, 931</a></span> (1995), since "[a]n examination of the common-law understanding of an officer's authority to arrest sheds light on the obviously relevant, if not entirely dispositive, consideration of what the Framers of the Amendment might have thought to be reasonable," <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#591" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 591</a></span> (1980) (footnote omitted). Thus, the first step here is to assess Atwater's claim that peace officers' authority to make warrantless arrests for misdemeanors was <span class="star-pagination">*327</span> restricted at common law (whether "common law" is understood strictly as law judicially derived or, instead, as the whole body of law extant at the time of the framing). Atwater's specific contention is that "founding-era common-law rules" forbade peace officers to make warrantless misdemeanor arrests except in cases of "breach of the peace," a category she claims was then understood narrowly as covering only those nonfelony offenses "involving or tending toward violence." Brief for Petitioners 13. Although her historical argument is by no means insubstantial, it ultimately fails.</p>
<p></p>
<h2>A</h2>
<p>We begin with the state of pre-founding English common law and find that, even after making some allowance for variations in the common-law usage of the term "breach of the peace,"<sup>[2]</sup> the "founding-era common-law rules" were not <span class="star-pagination">*328</span> nearly as clear as Atwater claims; on the contrary, the common-law commentators (as well as the sparsely reported cases) reached divergent conclusions with respect to officers' warrantless misdemeanor arrest power. Moreover, in the years leading up to American independence, Parliament repeatedly extended express warrantless arrest authority to cover misdemeanor-level offenses not amounting to or involving any violent breach of the peace.</p>
<p></p>
<h2>1</h2>
<p>Atwater's historical argument begins with our quotation from Halsbury in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), that</p>
<blockquote>"`[i]n cases of misdemeanor, a peace officer like a private person has at common law no power of arresting without a warrant except when a breach of the peace has been committed in his presence or there is reasonable ground for supposing that a breach of peace is about to be committed or renewed in his presence.' " <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Id.,</a></span></i> at 157 (quoting 9 Halsbury, Laws of England § 612, p. 299 (1909)).</blockquote>
<p><span class="star-pagination">*329</span> But the isolated quotation tends to mislead. In <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> itself we spoke of the common-law rule as only "sometimes expressed" that way, <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#157" aria-description="Citation for case: Carroll v. United States">267 U. S., at 157</a></span>, and, indeed, in the very same paragraph, we conspicuously omitted any reference to a breach-of-the-peace limitation in stating that the "usual rule" at common law was that "a police officer [could] arrest without warrant . . . one guilty of a misdemeanor if committed in his presence." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 156-157</a></span>. Thus, what <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> illustrates, and what others have recognized, is that statements about the common law of warrantless misdemeanor arrest simply are not uniform. Rather, "[a]t common law there is a difference of opinion among the authorities as to whether this right to arrest [without a warrant] extends to all misdemeanors." American Law Institute, Code of Criminal Procedure, Commentary to § 21, p. 231 (1930).</p>
<p>On one side of the divide there are certainly eminent authorities supporting Atwater's position. In addition to Lord Halsbury, quoted in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> James Fitzjames Stephen and Glanville Williams both seemed to indicate that the common law confined warrantless misdemeanor arrests to actual breaches of the peace. See 1 J. Stephen, A History of the Criminal Law of England 193 (1883) ("The common law did not authorise the arrest of persons guilty or suspected of misdemeanours, except in cases of an actual breach of the peace either by an affray or by violence to an individual"); G. Williams, Arrest for Breach of the Peace, <span class="citation no-link">1954 Crim. L. Rev. 578</span>, 578 ("Apart from arrest for felony . . . , the only power of arrest at common law is in respect of breach of the peace"). See also <i>Queen</i> v. <i>Tooley,</i> 2 Ld. Raym. 1296, 1301, 92 Eng. Rep. 349, 352 (Q. B. 1710) ("[A] constable cannot arrest, but when he sees an actual breach of the peace; and if the affray be over, he cannot arrest").</p>
<p>Sir William Blackstone and Sir Edward East might also be counted on Atwater's side, although they spoke only to the sufficiency of breach of the peace as a condition to warrantless <span class="star-pagination">*330</span> misdemeanor arrest, not to its necessity. Blackstone recognized that at common law "[t]he constable . . . hath great original and inherent authority with regard to arrests," but with respect to nonfelony offenses said only that "[h]e may, without warrant, arrest any one for a breach of the peace, and carry him before a justice of the peace." 4 Blackstone 289. Not long after the framing of the Fourth Amendment, East characterized peace officers' common-law arrest power in much the same way: "A constable or other known conservator of the peace may lawfully interpose upon his own view to prevent a breach of the peace, or to quiet an affray . . . ." 1 E. East, Pleas of the Crown § 71, p. 303 (1803).</p>
<p>The great commentators were not unanimous, however, and there is also considerable evidence of a broader conception of common-law misdemeanor arrest authority unlimited by any breach-of-the-peace condition. Sir Matthew Hale, Chief Justice of King's Bench from 1671 to 1676,<sup>[3]</sup> wrote in his History of the Pleas of the Crown that, by his "original and inherent power," a constable could arrest without a warrant "for breach of the peace and some misdemeanors, less than felony." 2 M. Hale, Pleas of the Crown 88 (1736). Hale's view, posthumously published in 1736, reflected an understanding dating back at least 60 years before the appearance of his Pleas yet sufficiently authoritative to sustain a momentum extending well beyond the framing era in this country. See The Compleat Parish-Officer 11 (1744) ("[T]he Constable . . . may for Breach of the Peace, and some Misdemeanors less than Felony, imprison a Man"); R. Burn, The Justice of the Peace 271 (1837) ("A <i>constable</i> . . . may at common law, for treason, felony, breach of the peace, and some misdemeanors less than felony, <i>committed in his view,</i> apprehend the supposed offender without any warrant" (italics in original)); 1 J. Chitty, A Practical <span class="star-pagination">*331</span> Treatise on the Criminal Law 20 (5th ed. 1847) ("[A constable] may for treason, felony, breach of the peace, and some misdemeanors less than felony, committed in his view, apprehend the supposed offender <i>virtiute officii,</i> without any warrant"); 1 W. Russell, Crimes and Misdemeanors 725 (7th ed. 1909) (officer "may arrest any person who in his presence commits a misdemeanor or breach of the peace").<sup>[4]</sup></p>
<p>As will be seen later, the view of warrantless arrest authority as extending to at least "some misdemeanors" beyond breaches of the peace was undoubtedly informed by statutory provisions authorizing such arrests, but it reflected common law in the strict, judge-made sense as well, for such was the holding of at least one case reported before Hale had even become a judge but which, like Hale's own commentary, continued to be cited well after the ratification of the Fourth Amendment. In <i>Holyday</i> v. <i>Oxenbridge,</i> Cro. Car. 234, 79 Eng. Rep. 805 (1631), the Court of King's Bench held that even a private person (and thus <i>a fortiori</i> a peace officer<sup>[5]</sup>) needed no warrant to arrest a "common cheater" whom he discovered "cozen[ing] with false dice." The court expressly rejected the contention that warrantless arrests were improper "unless in felony," and said instead that "there was good cause [for] staying" the gambler and, more broadly, that "it is <i>pro bono publico</i> to stay such offenders." <i>Id.,</i>  at 805-806. In the edition nearest to the date of the Constitution's framing, Sergeant William Hawkins's widely read Treatise of the Pleas of the Crown generalized from <i>Holyday</i> that "from the reason of this case it seems to follow, <span class="star-pagination">*332</span> That the [warrantless] arrest of any other offenders . . . for offences in like manner scandalous and prejudicial to the public, may be justified." 2 Hawkins, ch. 12, § 20, at 122. A number of other common-law commentaries shared Hawkins's broad reading of <i>Holyday.</i> See The Law of Arrests 205 (2d ed. 1753) (In light of <i>Holyday,</i> "an Arrest of an Offender . . . for any Crime prejudicial to the Publick, seems to be justifiable"); 1 T. Cunningham, A New and Complete Law Dictionary (1771) (definition of "arrest") (same); 1 G. Jacob, The Law Dictionary 129 (1st Am. ed. 1811) (same). See generally C. Greaves, Law of Arrest Without a Warrant, in The Criminal Law Consolidation Acts, p. lxiii (1870) ("<i>[Holyday]</i> is rested upon the broad ground that `it is <i>pro bono publico</i> to stay such offenders,' which is equally applicable to every case of misdemeanor . . . ").<sup>[6]</sup></p>
<p>We thus find disagreement, not unanimity, among both the common-law jurists and the text writers who sought to pull the cases together and summarize accepted practice. Having reviewed the relevant English decisions, as well as English and colonial American legal treatises, legal dictionaries, and procedure manuals, we simply are not convinced that Atwater's is the correct, or even necessarily the better, reading of the common-law history.</p>
<p></p>
<h2>
<span class="star-pagination">*333</span> 2</h2>
<p>A second, and equally serious, problem for Atwater's historical argument is posed by the "divers Statutes," M. Dalton, Country Justice, ch. 170, § 4, p. 582 (1727), enacted by Parliament well before this Republic's founding that authorized warrantless misdemeanor arrests without reference to violence or turmoil. Quite apart from Hale and Blackstone, the legal background of any conception of reasonableness the Fourth Amendment's Framers might have entertained would have included English statutes, some centuries old, authorizing peace officers (and even private persons) to make warrantless arrests for all sorts of relatively minor offenses unaccompanied by violence. The so-called "nightwalker" statutes are perhaps the most notable examples. From the enactment of the Statute of Winchester in 1285, through its various readoptions and until its repeal in 1827,<sup>[7]</sup> night watchmen were authorized and charged "as . . . in Times past" to "watch the Town continually all Night, from the Sun-setting unto the Sun-rising" and were directed that "if any Stranger do pass by them, he shall be arrested until Morning . . . ." 13 Edw. I, ch. 4, §§ 5-6, 1 Statutes at Large 232-233; see also 5 Edw. III, ch. 14, 1 Statutes at Large 448 (1331) (confirming and extending the powers of watchmen). Hawkins emphasized that the Statute of Winchester "was made" not in derogation but rather "in affirmance of the common law," for "every private person may by the common law arrest any suspicious night-walker, and detain him till he give good account of himself . . . ." 2 Hawkins, ch. 13, § 6, at 130. And according to Blackstone, these watchmen had virtually limitless warrantless nighttime arrest power: "Watchmen, either those appointed by the statute of Winchester . . . or such as are mere assistants to the constable, may <i>virtute officii</i> arrest all offenders, and particularly nightwalkers, and commit them to custody till the morning." 4 Blackstone 289; see <span class="star-pagination">*334</span> also 2 Hale, Pleas of the Crown, at 97 (describing broad arrest powers of watchmen even over and above those conferred by the Statute of Winchester).<sup>[8]</sup> The Statute of Winchester, moreover, empowered peace officers not only to deal with nightwalkers and other nighttime "offenders," but periodically to "make Inquiry of all Persons being lodged in the Suburbs, or in foreign Places of the Towns." On that score, the Statute provided that "if they do find any that have lodged or received any Strangers or suspicious Person, against the Peace, the Bailiffs shall do Righttherein," 13 Edw. I, ch. 4, §§ 3-4, 1 Statutes at Large 232-233, which Hawkins understood "surely" to mean that officers could "lawfully arrest and detain any such stranger[s]," 2 Hawkins, ch. 13, § 12,at 134.</p>
<p>Nor were the nightwalker statutes the only legislative sources of warrantless arrest authority absent real or threatened violence, as the parties and their <i>amici</i> here seem to have assumed. On the contrary, following the Edwardian legislation and throughout the period leading up to the framing, Parliament repeatedly extended warrantless arrest power to cover misdemeanor-level offenses not involving any breach of the peace. One 16th-century statute, for instance, authorized peace officers to arrest persons playing "unlawful game[s]" like bowling, tennis, dice, and cards, and for good measure extended the authority beyond players to include persons "haunting" the "houses, places and alleys where such games shall be suspected to be holden, exercised, used <span class="star-pagination">*335</span> or occupied." 33 Hen. VIII, ch. 9, §§ 11-16, 5 Statutes at Large 84-85 (1541). A 17th-century act empowered "any person . . . whatsoever to seize and detain any . . . hawker, pedlar, petty chapman, or other trading person" found selling without a license. 8 &amp; 9 Wm. III, ch. 25, §§ 3, 8, 10 Statutes at Large 81-83 (1697). And 18th-century statutes authorized the warrantless arrest of "rogues, vagabonds, beggars, and other idle and disorderly persons" (defined broadly to include jugglers, palm readers, and unlicensed play actors), 17 Geo. II, ch. 5, §§ 1-2, 5, 18 Statutes at Large 144, 145-147 (1744); "horrid" persons who "profanely swear or curse," 19 Geo. II, ch. 21, § 3, 18 Statutes at Large 445 (1746); individuals obstructing "publick streets, lanes or open passages" with "pipes, butts, barrels, casks or other vessels" or an "empty cart, car, dray or other carriage," 30 Geo. II, ch. 22, §§ 5, 13, 22 Statutes at Large 107-108, 111 (1757); and, most significantly of all given the circumstances of the case before us, negligent carriage drivers, 27 Geo. II, ch. 16, § 7, 21 Statutes at Large 188 (1754). See generally S. Blackerby, The Justice of Peace: His Companion, or a Summary of all the Acts of Parliament (1723) (cataloguing statutes); S. Welch, An Essay on the Office of Constable 19-22 (1758) (describing same).</p>
<p>The significance of these early English statutes lies not in proving that any common-law rule barring warrantless misdemeanor arrests that might have existed would have been subject to statutory override; the sovereign Parliament could of course have wiped away any judge-made rule. The point is that the statutes riddle Atwater's supposed common-law rule with enough exceptions to unsettle any contention that the law of the mother country would have left the Fourth Amendment's Framers of a view that it would necessarily have been unreasonable to arrest without warrant for a misdemeanor unaccompanied by real or threatened violence.</p>
<p></p>
<h2>
<span class="star-pagination">*336</span> B</h2>
<p>An examination of specifically American evidence is to the same effect. Neither the history of the framing era nor subsequent legal development indicates that the Fourth Amendment was originally understood, or has traditionally been read, to embrace Atwater's position.</p>
<p></p>
<h2>1</h2>
<p>To begin with, Atwater has cited no particular evidence that those who framed and ratified the Fourth Amendment sought to limit peace officers' warrantless misdemeanor arrest authority to instances of actual breach of the peace, and our own review of the recent and respected compilations of framing-era documentary history has likewise failed to reveal any such design. See The Complete Bill of Rights 223 263 (N. Cogan ed. 1997) (collecting original sources); 5 The Founders' Constitution 219-244 (P. Kurland &amp; R. Lerner eds. 1987) (same). Nor have we found in any of the modern historical accounts of the Fourth Amendment's adoption any substantial indication that the Framers intended such a restriction. See, <i>e. g.,</i> L. Levy, Origins of the Bill of Rights 150-179 (1999); T. Taylor, Two Studies in Constitutional Interpretation 19-93 (1969); J. Landynski, Search and Seizure and the Supreme Court 19-48 (1966); N. Lasson, History and Development of the Fourth Amendment to the United States Constitution 79-105 (1937); Davies, Recovering the Original Fourth Amendment, <span class="citation no-link">98 Mich. L. Rev. 547</span> (1999); Amar, Fourth Amendment First Principles, <span class="citation no-link">107 Harv. L. Rev. 757</span> (1994); Bradley, Constitutional Theory of the Fourth Amendment, <span class="citation no-link">38 DePaul L. Rev. 817</span> (1989). Indeed, to the extent these modern histories address the issue, their conclusions are to the contrary. See Landynski, <i>supra,</i> at 45 (Fourth Amendment arrest rules are "based on common-law practice," which "dispensed with" a warrant requirement for misdemeanors "committed in the presence of the arresting officer"); Davies, <i>supra,</i> at 551 ("[T]he Framers did not address <span class="star-pagination">*337</span> warrantless intrusions at all in the Fourth Amendment or in the earlier state provisions; thus, they never anticipated that `unreasonable' might be read as a standard for warrantless intrusions").</p>
<p>The evidence of actual practice also counsels against Atwater's position. During the period leading up to and surrounding the framing of the Bill of Rights, colonial and state legislatures, like Parliament before them, <i>supra,</i> at 333-335, regularly authorized local peace officers to make warrantless misdemeanor arrests without conditioning statutory authority on breach of the peace. See, <i>e. g.,</i> First Laws of the State of Connecticut 214-215 (Cushing ed. 1982) (1784 compilation; exact date of Act unknown) (authorizing warrantless arrests of "all Persons unnecessarily travelling on the Sabbath or Lord's Day"); <i>id.,</i> at 23 ("such as are guilty of Drunkenness, profane Swearing, Sabbath-breaking, also vagrant Persons [and] unseasonable Night-walkers"); Digest of the Laws of the State of Georgia 1755-1800, p. 411 (H. Marbury &amp; W. Crawford eds. 1802) (1762 Act) (breakers of the Sabbath laws); <i>id.,</i> at 252 (1764 Act) (persons "gaming . . . in any licensed public house, or other house sellingliquors"); Colonial Laws of Massachusetts 139 (1889) (1646 Act) ("such as are overtaken with drink, swearing, Sabbath breaking, Lying, vagrant persons, [and] night-walkers"); Laws of the State of New Hampshire 549 (1800) (1799 Act) (persons "travelling unnecessarily" on Sunday); Digest of the Laws of New Jersey 1709-1838, pp. 585-586 (L. Elmer ed. 1838) (1799 Act) ("vagrants or vagabonds, common drunkards, common night-walkers, and common prostitutes," as well as fortunetellers and other practitioners of "crafty science"); Laws of the State of New York, 1777-1784, pp. 358-359 (1886) (1781 Act) ("hawker[s]" and "pedlar[s]"); Earliest Printed Laws of New York, 1665-1693, p. 133 (J. Cushing ed. 1978) (Duke of York's Laws, 1665-1675) ("such as are overtaken with Drink, Swearing, Sabbath breaking, Vagrant persons or night walkers"); 3 Laws of the Commonwealth of Pennsylvania 177-183 <span class="star-pagination">*338</span> (1810) (1794 Act) (persons "profanely curs[ing]," drinking excessively, "cock-fighting," or "play[ing] at cards, dice, billiards, bowls, shuffle-boards, or any game of hazard or address, for money").<sup>[9]</sup></p>
<p>What we have here, then, is just the opposite of what we had in <i>Wilson</i> v. <i><span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Arkansas</a></span></i><i>.</i> There, we emphasized that during the founding era a number of States had "enacted statutes specifically embracing" the common-law knock-andannounce rule, <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#933" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 933</a></span>; here, by contrast, those very same States passed laws extending warrantless arrest authority to a host of nonviolent misdemeanors, and in so doing acted very much inconsistently with Atwater's claims about the Fourth Amendment's object. Of course, the Fourth <span class="star-pagination">*339</span> Amendment did not originally apply to the States, see <i>Barron</i> v. <i>Mayor of Baltimore,</i> <span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span> (1833), but that does not make state practice irrelevant in unearthing the Amendment's original meaning. A number of state constitutional search-and-seizure provisions served as models for the Fourth Amendment, see, <i>e. g.,</i> N. H. Const. of 1784, pt. I, Art. XIX; Pa. Const. of 1776 (Declaration of Rights), Art. X, and the fact that many of the original States with such constitutional limitations continued to grant their own peace officers broad warrantless misdemeanor arrest authority undermines Atwater's contention that the founding generation meant to bar federal law enforcement officers from exercising the same authority. Given the early state practice, it is likewise troublesome for Atwater's view that just one year after the ratification of the Fourth Amendment, Congress vested federal marshals with "the same powers in executing the laws of the United States, as sheriffs and their deputies in the several states have by law, in executing the laws of their respective states." Act of May 2, 1792, ch. 28, § 9, <span class="citation no-link">1 Stat. 265</span>. Thus, as we have said before in only slightly different circumstances, the Second Congress apparently "saw no inconsistency between the Fourth Amendment and legislation giving United States marshals the same power as local peace officers" to make warrantless arrests. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#420" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 420</a></span> (1976).<sup>[10]</sup></p>
<p>The record thus supports Justice Powell's observation that "[t]here is no historical evidence that the Framers or proponents of the Fourth Amendment, outspokenly opposed to the infamous general warrants and writs of assistance, were at <span class="star-pagination">*340</span> all concerned about warrantless arrests by local constables and other peace officers." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#429" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 429</a></span> (concurring opinion). We simply cannot conclude that the Fourth Amendment, as originally understood, forbade peace officers to arrest without a warrant for misdemeanors not amounting to or involving breach of the peace.</p>
<p></p>
<h2>2</h2>
<p>Nor does Atwater's argument from tradition pick up any steam from the historical record as it has unfolded since the framing, there being no indication that her claimed rule has ever become "woven . . . into the fabric" of American law. <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#933" aria-description="Citation for case: Wilson v. Arkansas"><i>Wilson, supra,</i> at 933</a></span>; see also <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#590" aria-description="Citation for case: Payton v. New York">445 U. S., at 590</a></span> (emphasizing "the clear consensus among the States adhering to [a] well-settled common-law rule"). The story, on the contrary, is of two centuries of uninterrupted (and largely unchallenged) state and federal practice permitting warrantless arrests for misdemeanors not amounting to or involving breach of the peace.</p>
<p>First, there is no support for Atwater's position in this Court's cases (apart from the isolated sentence in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i>  already explained). Although the Court has not had much to say about warrantless misdemeanor arrest authority, what little we have said tends to cut against Atwater's argument. In discussing this authority, we have focused on the circumstance that an offense was committed in an officer's presence, to the omission of any reference to a breach-of-the-peace limitation.<sup>[11]</sup> See, <i>e. g., </i><i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 418</a></span> ("The cases construing the Fourth Amendment thus reflect the ancient common-law rule that a peace officer was permitted to arrest without a warrant for a misdemeanor or felony <span class="star-pagination">*341</span> committed in his presence . . ."); <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span>,</i> 267 U. S., at 156 157 ("The usual rule is that a police officer may arrest without warrant one . . . guilty of a misdemeanor if committed in his presence"); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534, 536, n. 1</a></span> (1900) (noting common-law pedigree of state statute permitting warrantless arrest "[f]or a public offense committed or attempted in [officer's] presence"); <i>Kurtz</i> v. <i>Moffitt,</i>  <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#499" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 499</a></span> (1885) (common-law presence requirement); cf. also <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#756" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 756</a></span> (1984) (White, J., dissenting) ("`[A]uthority to arrest without a warrant in misdemeanor cases may be enlarged by statute' ").</p>
<p>Second, and again in contrast with <i><span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>,</i> it is not the case here that "[e]arly American courts . . .embraced" an accepted common-law rule with anything approaching unanimity. <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#933" aria-description="Citation for case: Wilson v. Arkansas">514 U. S., at 933</a></span>. To be sure, Atwater has cited several 19th-century decisions that, at least at first glance, might seem to support her contention that "warrantless misdemeanor arrest was unlawful when not [for] a breach of the peace." Brief for Petitioners 17 (citing <i>Pow</i> v. <i>Beckner,</i> <span class="citation" data-id="7032183"><a href="/opinion/7124841/pow-v-beckner/#478" aria-description="Citation for case: Pow v. Beckner">3 Ind. 475, 478</a></span> (1852), <i>Commonwealth</i>  v. <i>Carey,</i> <span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/#250" aria-description="Citation for case: Commonwealth v. Carey">66 Mass. 246, 250</a></span> (1853), and <i>Robison</i> v. <i>Miner,</i>  <span class="citation" data-id="7933442"><a href="/opinion/7980722/robison-v-miner/#556" aria-description="Citation for case: Robison v. Miner">68 Mich. 549, 556-559</a></span>, <span class="citation no-link">37 N. W. 21</span>, 25 (1888)). But none is ultimately availing. <i><span class="citation" data-id="7032183"><a href="/opinion/7124841/pow-v-beckner/" aria-description="Citation for case: Pow v. Beckner">Pow</a></span></i> is fundamentally a "presence" case; it stands only for the proposition, not at issue here, see n. 11, <i>supra,</i> that a nonfelony arrest should be made while the offense is "in [the officer's] view and . . . still continuing" and not subsequently "upon vague information communicated to him." <span class="citation" data-id="7032183"><a href="/opinion/7124841/pow-v-beckner/#478" aria-description="Citation for case: Pow v. Beckner">3 Ind., at 478</a></span>. The language Atwater attributes to <i><span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/" aria-description="Citation for case: Commonwealth v. Carey">Carey</a></span></i> ("[E]ven if he were a constable, he had no power to arrest for any misdemeanor without a warrant, except to stay a breach of the peace, or to prevent the commission of such an offense") is taken from the reporter's summary of one of the party's arguments, not from the opinion of the court. While the court in <i><span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/" aria-description="Citation for case: Commonwealth v. Carey">Carey</a></span></i> (through Chief Justice Shaw) said that "the old established rule of the common law" was that "a constable or other peace officer could not <span class="star-pagination">*342</span> arrest one without a warrant . . . if such crime were not an offence amounting in law to felony," it said just as clearly that the common-law rule could be "altered by the legislature" (notwithstanding Massachusetts's own Fourth Amendment equivalent in its State Constitution). <span class="citation" data-id="6410134"><a href="/opinion/6536414/commonwealth-v-carey/#252" aria-description="Citation for case: Commonwealth v. Carey">66 Mass., at 252</a></span>. <i>Miner,</i> the third and final case upon which Atwater relies, was expressly overruled just six years after it was decided. In <i>Burroughs</i> v. <i>Eastman,</i> <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/" aria-description="Citation for case: Burroughs v. Eastman">101 Mich. 419</a></span>, <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/" aria-description="Citation for case: Burroughs v. Eastman">59 N. W. 817</a></span> (1894), the Supreme Court of Michigan held that the language from <i>Miner</i> upon which the plaintiff there (and presumably Atwater here) relied "should not be followed," and then went on to offer the following: "[T]he question has arisen in many of our sister states, and the power to authorize arrest on view for offenses not amounting to breaches of the peace has been affirmed. Our attention has been called to no case, nor have we in our research found one, in which the contrary doctrine has been asserted." <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/#425" aria-description="Citation for case: Burroughs v. Eastman">101 Mich., at 425</a></span>, <span class="citation" data-id="7937209"><a href="/opinion/7984240/burroughs-v-eastman/#819" aria-description="Citation for case: Burroughs v. Eastman">59 N. W., at 819</a></span> (collecting cases from, <i>e. g.,</i> Illinois, Indiana, Massachusetts, Minnesota, Missouri, New Hampshire, New York, Ohio, and Texas).</p>
<p>The reports may well contain early American cases more favorable to Atwater's position than the ones she has herself invoked. But more to the point, we think, are the numerous early- and mid-19th-century decisions expressly sustaining (often against constitutional challenge) state and local laws authorizing peace officers to make warrantless arrests for misdemeanors not involving any breach of the peace. See, <i>e. g., </i><i>Mayo</i> v. <i><span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">Wilson</a></span>,</i> 1 N. H. 53 (1817) (upholding statute authorizing warrantless arrests of those unnecessarily traveling on Sunday against challenge based on state due process and search-and-seizure provisions); <i>Holcomb</i> v. <i>Cornish,</i> <span class="citation" data-id="6574474"><a href="/opinion/6694531/holcomb-v-cornish/" aria-description="Citation for case: Holcomb v. Cornish">8 Conn. 375</a></span> (1831) (upholding statute permitting warrantless arrests for "drunkenness, profane swearing, cursing or sabbath-breaking" against argument that "[t]he power of a justice of the peace to arrest and detain a citizen without complaint or warrant against him, is surely not given by the <span class="star-pagination">*343</span> common law"); <i>Jones</i> v. <i>Root,</i> <span class="citation" data-id="6410982"><a href="/opinion/6537262/jones-v-root/" aria-description="Citation for case: Jones v. Root">72 Mass. 435</a></span> (1856) (rebuffing constitutional challenge to statute authorizing officers "without a warrant [to] arrest any person or persons whom they may find in the act of illegally selling, transporting, or distributing intoxicating liquors"); <i>Main</i> v. <i>McCarty,</i> <span class="citation" data-id="6948242"><a href="/opinion/7044997/main-v-mccarty/#442" aria-description="Citation for case: Main v. McCarty">15 Ill. 441, 442</a></span> (1854) (concluding that a law expressly authorizing arrests for city-ordinance violations was "not repugnant to the constitution or the general provisions of law"); <i>White</i> v. <i>Kent,</i>  <span class="citation no-link">11 Ohio St. 550</span> (1860) (upholding municipal ordinance permitting warrantless arrest of any person found violating any city ordinance or state law); <i>Davis</i> v. <i>American Soc. for Prevention of Cruelty to Animals,</i> <span class="citation" data-id="3585438"><a href="/opinion/3603859/davis-v-american-society-for-prevention-of-cruelty-to-animals/" aria-description="Citation for case: Davis v. American Society for Prevention of Cruelty to...">75 N. Y. 362</a></span> (1878) (upholding statute permitting warrantless arrest for misdemeanor violation of cruelty-to-animals prohibition). See generally Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 550, and n. 54 (1924) (collecting cases and observing that "[t]he states may, by statute, enlarge the common law right to arrest without a warrant, and have quite generally done so or authorized municipalities to do so, as for example, an officer may be authorized by statute or ordinance to arrest without a warrant for various misdemeanors and violations of ordinances, other than breaches of the peace, if committed in his presence"); <span class="citation no-link"><i>id.,</i> at 706, nn. 570, 571</span> (collecting cases); 1 J. Bishop, New Criminal Procedure §§ 181, 183, pp. 101, n. 2, 103, n. 5 (4th ed. 1895) (same); W. Clark, Handbook of Criminal Procedure § 12, p. 50, n. 8 (2d ed. 1918) (same).</p>
<p>Finally, both the legislative tradition of granting warrantless misdemeanor arrest authority and the judicial tradition of sustaining such statutes against constitutional attack are buttressed by legal commentary that, for more than a century now, has almost uniformly recognized the constitutionality of extending warrantless arrest power to misdemeanors without limitation to breaches of the peace. See, <i>e. g.,</i> E. Fisher, Laws of Arrest § 59, p. 130 (1967) ("[I]t is generally recognized today that the common law authority to arrest without a warrant in misdemeanor cases may be enlarged by <span class="star-pagination">*344</span> statute, and this has been done in many of the states"); Wilgus, <i>supra,</i> at 705-706 ("Statutes and municipal charters have quite generally authorized an officer to arrest for any misdemeanor whether a breach of the peace or not, without a warrant, if committed in the officer's presence. Such statutes are valid" (footnote omitted)); Clark, <i>supra,</i> § 12, at 50 ("In most, if not all, the states there are statutes and city ordinances, which are clearly valid, authorizing officers to arrest for certain misdemeanors without a warrant, when committed in their presence"); J. Beale, Criminal Pleading and Practice § 21, p. 20, and n. 7 (1899) ("By statute the power of peace officers to arrest without a warrant is often extended to all misdemeanors committed in their presence." "Such a statute is constitutional"); 1 Bishop, <i>supra,</i> § 183, at 103 ("[T]he power of arrest extends, possibly, to any indictable wrong in [an officer's] presence. . . . And statutes and ordinances widely permit these arrests for violations of municipal by-laws"); J. Bassett, Criminal Pleading and Practice § 89, p. 104 (2d ed. 1885) ("[A]s to the lesser misdemeanors, except breaches of the peace, the power extends only so far as some statute gives it"). But cf. H. Vorhees, Law of Arrest § 131, pp. 78-79 (1904) (acknowledging that "by authority of statute, city charter, or ordinance, [an officer] may arrest without a warrant, one who . . . commits a misdemeanor other than a breach of the peace," but suggesting that courts look with "disfavor" on such legislative enactments "as interfering with the constitutional liberties of the subject").</p>
<p>Small wonder, then, that today statutes in all 50 States and the District of Columbia permit warrantless misdemeanor arrests by at least some (if not all) peace officers without requiring any breach of the peace,<sup>[12]</sup> as do a host of congressional enactments.<sup>[13]</sup> The American Law Institute <span class="star-pagination">*345</span> has long endorsed the validity of such legislation, see American Law Institute, Code of Criminal Procedure § 21(a), p. 28 (1930); American Law Institute, Model Code of PreArraignment Procedure § 120.1(1)(c), p. 13 (1975), and the consensus, as stated in the current literature, is that statutes "remov[ing] the breach of the peace limitation and thereby permit[ting] arrest without warrant for <i>any</i> misdemeanor committed in the arresting officer's presence" have "`never been successfully challenged and stan[d] as the law of the land.' " 3 W. LaFave, Search and Seizure § 5.1(b), pp. 13-14, and n. 76 (1996) (quoting <i>Higbee</i> v. <i>San Diego,</i> <span class="citation" data-id="546349"><a href="/opinion/546349/raymond-higbee-william-crenshaw-alexander-smogyi-roger-dennehy-v-city-of/#379" aria-description="Citation for case: Raymond Higbee William Crenshaw Alexander Smogyi Roger...">911 F. 2d 377, 379</a></span> (CA9 1990)) (emphasis in original; footnote omitted). This, therefore, simply is not a case in which the claimant can point to "a clear answer [that] existed in 1791 and has been generally adhered to by the traditions of our society ever since." <i>County of Riverside</i> v. <i>McLaughlin,</i> <span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/#60" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U. S. 44, 60</a></span> (1991) (Scalia, J., dissenting).</p>
<p></p>
<h2>III</h2>
<p>While it is true here that history, if not unequivocal, has expressed a decided, majority view that the police need not obtain an arrest warrant merely because a misdemeanor stopped short of violence or a threat of it, Atwater does not wager all on history.<sup>[14]</sup> Instead, she asks us to mint a new <span class="star-pagination">*346</span> rule of constitutional law on the understanding that when historical practice fails to speak conclusively to a claim grounded on the Fourth Amendment, courts are left to strike a current balance between individual and societal interests by subjecting particular contemporary circumstances to traditional standards of reasonableness. See <i>Wyoming</i> v. <i>Houghton,</i> <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#299" aria-description="Citation for case: Wyoming v. Houghton">526 U. S. 295, 299-300</a></span> (1999); <i>Vernonia School Dist. 47J</i> v. <i>Acton,</i> <span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/#652" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U. S. 646, 652-653</a></span> (1995). Atwater accordingly argues for a modern arrest rule, one not necessarily requiring violent breach of the peace, but nonetheless forbidding custodial arrest, even upon probable cause, when conviction could not ultimately carry any jail time and when the government shows no compelling need for immediate detention.<sup>[15]</sup></p>
<p>If we were to derive a rule exclusively to address the uncontested facts of this case, Atwater might well prevail. She was a known and established resident of Lago Vista with no place to hide and no incentive to flee, and common sense says she would almost certainly have buckled up as a condition of driving off with a citation. In her case, the physical incidents of arrest were merely gratuitous humiliations imposed by a police officer who was (at best) exercising <span class="star-pagination">*347</span> extremely poor judgment. Atwater's claim to live free of pointless indignity and confinement clearly outweighs anything the City can raise against it specific to her case.</p>
<p>But we have traditionally recognized that a responsible Fourth Amendment balance is not well served by standards requiring sensitive, case-by-case determinations of government need, lest every discretionary judgment in the field be converted into an occasion for constitutional review. See, <i>e. g., </i><i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 234-235</a></span> (1973). Often enough, the Fourth Amendment has to be applied on the spur (and in the heat) of the moment, and the object in implementing its command of reasonableness is to draw standards sufficiently clear and simple to be applied with a fair prospect of surviving judicial second-guessing months and years after an arrest or search is made. Courts attempting to strike a reasonable Fourth Amendment balance thus credit the government's side with an essential interest in readily administrable rules. See <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458</a></span> (1981) (Fourth Amendment rules "`ought to be expressed in terms that are readily applicable by the police in the context of the law enforcement activities in which they are necessarily engaged' " and not "`qualified by all sorts of ifs, ands, and buts' ").<sup>[16]</sup></p>
<p>At first glance, Atwater's argument may seem to respect the values of clarity and simplicity, so far as she claims that the Fourth Amendment generally forbids warrantless arrests for minor crimes not accompanied by violence or some <span class="star-pagination">*348</span> demonstrable threat of it (whether "minor crime" be defined as a fine-only traffic offense, a fine-only offense more generally, or a misdemeanor<sup>[17]</sup>). But the claim is not ultimately so simple, nor could it be, for complications arise the moment we begin to think about the possible applications of the several criteria Atwater proposes for drawing a line between minor crimes with limited arrest authority and others not so restricted.</p>
<p>One line, she suggests, might be between "jailable" and "fine-only" offenses, between those for which conviction could result in commitment and those for which it could not. The trouble with this distinction, of course, is that an officer on the street might not be able to tell. It is not merely that we cannot expect every police officer to know the details of frequently complex penalty schemes, see <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#431" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 431, n. 13</a></span> (1984) ("[O]fficers in the field frequently `have neither the time nor the competence to determine' the severity of the offense for which they are considering arresting a person"), but that penalties for ostensibly identical conduct can vary on account of facts difficult (if not impossible) to know at the scene of an arrest. Is this the first offense or is the suspect a repeat offender?<sup>[18]</sup> Is the weight of the marijuana a gram above or a gram below <span class="star-pagination">*349</span> the fine-only line?<sup>[19]</sup> Where conduct could implicate more than one criminal prohibition, which one will the district attorney ultimately decide to charge?<sup>[20]</sup> And so on.</p>
<p>But Atwater's refinements would not end there. She represents that if the line were drawn at nonjailable traffic offenses, her proposed limitation should be qualified by a proviso authorizing warrantless arrests where "necessary for enforcement of the traffic laws or when [an] offense would otherwise continue and pose a danger to others on the road." Brief for Petitioners 46 (internal quotation marks omitted). (Were the line drawn at misdemeanors generally, a comparable qualification would presumably apply.) The proviso only compounds the difficulties. Would, for instance, either exception apply to speeding? At oral argument, Atwater's counsel said that "it would not be reasonable to arrest a driver for speeding unless the speeding rose to the level of reckless driving." Tr. of Oral Arg. 16. But is it not fair to expect that the chronic speeder will speed again despite a citation in his pocket, and should that not qualify as showing that the "offense would . . . continue" under Atwater's rule? And why, as a constitutional matter, should we assume that only reckless driving will "pose a danger to others on the road" while speeding will not?</p>
<p><span class="star-pagination">*350</span> There is no need for more examples to show that Atwater's general rule and limiting proviso promise very little in the way of administrability. It is no answer that the police routinely make judgments on grounds like risk of immediate repetition; they surely do and should. But there is a world of difference between making that judgment in choosing between the discretionary leniency of a summons in place of a clearly lawful arrest, and making the same judgment when the question is the lawfulness of the warrantless arrest itself. It is the difference between no basis for legal action challenging the discretionary judgment, on the one hand, and the prospect of evidentiary exclusion or (as here) personal § 1983 liability for the misapplication of a constitutional standard, on the other. Atwater's rule therefore would not only place police in an almost impossible spot but would guarantee increased litigation over many of the arrests that would occur.<sup>[21]</sup> For all these reasons, Atwater's various distinctions between permissible and impermissible arrests for minor crimes strike us as "very unsatisfactory line[s]" to require police officers to draw on a moment's notice. <i>Carroll</i>  v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#157" aria-description="Citation for case: Carroll v. United States">267 U. S., at 157</a></span>.</p>
<p>One may ask, of course, why these difficulties may not be answered by a simple tie breaker for the police to follow in the field: if in doubt, do not arrest. The first answer is that in practice the tie breaker would boil down to something akin to a least-restrictive-alternative limitation, which is itself one of those "ifs, ands, and buts" rules, <i>New York</i>  v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S., at 458</a></span>, generally thought inappropriate in working out Fourth Amendment protection. See, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602</a></span>, <span class="star-pagination">*351</span> 629, n. 9 (1989) (collecting cases); <i>United States</i> v. <i>MartinezFuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#557" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 557-558, n. 12</a></span> (1976) ("The logic of such elaborate less-restrictive-alternative arguments could raise insuperable barriers to the exercise of virtually all searchand-seizure powers"). Beyond that, whatever help the tie breaker might give would come at the price of a systematic disincentive to arrest in situations where even Atwater concedes that arresting would serve an important societal interest. An officer not quite sure that the drugs weighed enough to warrant jail time or not quite certain about a suspect's risk of flight would not arrest, even though it could perfectly well turn out that, in fact, the offense called for incarceration and the defendant was long gone on the day of trial. Multiplied many times over, the costs to society of such under enforcement could easily outweigh the costs to defendants of being needlessly arrested and booked, as Atwater herself acknowledges.<sup>[22]</sup></p>
<p>Just how easily the costs could outweigh the benefits may be shown by asking, as one Member of this Court did at oral argument, "how bad the problem is out there." Tr. of Oral Arg. 20. The very fact that the law has never jelled the way Atwater would have it leads one to wonder whether warrantless misdemeanor arrests need constitutional attention, <span class="star-pagination">*352</span> and there is cause to think the answer is no. So far as such arrests might be thought to pose a threat to the probable-cause requirement, anyone arrested for a crime without formal process, whether for felony or misdemeanor, is entitled to a magistrate's review of probable cause within 48 hours, <i>County of Riverside</i> v. <i>McLaughlin,</i> <span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/#55" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U. S., at 55-58</a></span>, and there is no reason to think the procedure in this case atypical in giving the suspect a prompt opportunity to request release, see <span class="citation no-link">Tex. Transp. Code Ann. § 543.002</span> (1999) (persons arrested for traffic offenses to be taken "immediately" before a magistrate). Many jurisdictions, moreover, have chosen to impose more restrictive safeguards through statutes limiting warrantless arrests for minor offenses. See, <i>e. g.,</i> <span class="citation no-link">Ala. Code § 32</span>-14 (1999); Cal. Veh. Code Ann. § 40504 (West 2000); <span class="citation no-link">Ky. Rev. Stat. Ann. §§ 431.015</span>(1), (2) (Michie 1999); La. Rev. Stat. Ann. § 32:391 (West 1989); Md. Transp. Code Ann. § 26-202(a)(2) (1999); S. D. Codified Laws § 32-33-2 (1998); <span class="citation no-link">Tenn. Code Ann. § 40</span>-7118(b)(1) (1997); <span class="citation no-link">Va. Code Ann. § 46.2-936</span> (Supp. 2000). It is of course easier to devise a minor-offense limitation by statute than to derive one through the Constitution, simply because the statute can let the arrest power turn on any sort of practical consideration without having to subsume it under a broader principle. It is, in fact, only natural that States should resort to this sort of legislative regulation, for, as Atwater's own <i>amici</i>  emphasize, it is in the interest of the police to limit pettyoffense arrests, which carry costs that are simply too great to incur without good reason. See Brief for Institute on Criminal Justice at the University of Minnesota Law School and Eleven Leading Experts on Law Enforcement and Corrections Administration and Policy as <i>Amici Curiae</i> 11 (the use of custodial arrests for minor offenses "[a]ctually [c]ontradicts [l]aw [e]nforcement [i]nterests"). Finally, and significantly, under current doctrine the preference for categorical treatment of Fourth Amendment claims gives way to individualized review when a defendant makes a colorable <span class="star-pagination">*353</span> argument that an arrest, with or without a warrant, was "conducted in an extraordinary manner, unusually harmful to [his] privacy or even physical interests." <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States">517 U. S., at 818</a></span>; see also <i>Graham</i> v. <i>Connor,</i>  <span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#395" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 395-396</a></span> (1989) (excessive force actionable under § 1983).</p>
<p>The upshot of all these influences, combined with the good sense (and, failing that, the political accountability) of most local lawmakers and law-enforcement officials, is a dearth of horribles demanding redress. Indeed, when Atwater's counsel was asked at oral argument for any indications of comparably foolish, warrantless misdemeanor arrests, he could offer only one.<sup>[23]</sup> We are sure that there are others,<sup>[24]</sup> but just as surely the country is not confronting anything like an epidemic of unnecessary minor-offense arrests.<sup>[25]</sup> That fact caps the reasons for rejecting Atwater's request <span class="star-pagination">*354</span> for the development of a new and distinct body of constitutional law.</p>
<p>Accordingly, we confirm today what our prior cases have intimated: the standard of probable cause "applie[s] to all arrests, without the need to `balance' the interests and circumstances involved in particular situations." <i>Dunaway</i> v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#208" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 208</a></span> (1979). If an officer has probable cause to believe that an individual has committed even a very minor criminal offense in his presence, he may, without violating the Fourth Amendment, arrest the offender.</p>
<p></p>
<h2>IV</h2>
<p>Atwater's arrest satisfied constitutional requirements. There is no dispute that Officer Turek had probable cause to believe that Atwater had committed a crime in his presence. She admits that neither she nor her children were wearing seatbelts, as required by <span class="citation no-link">Tex. Transp. Code Ann. § 545.413</span> (1999). Turek was accordingly authorized (not required, but authorized) to make a custodial arrest without balancing costs and benefits or determining whether or not Atwater's arrest was in some sense necessary.</p>
<p>Nor was the arrest made in an "extraordinary manner, unusually harmful to [her] privacy or . . . physical interests." <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States">517 U. S., at 818</a></span>. As our citations in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> make clear, the question whether a search or seizure is "extraordinary" turns, above all else, on the manner in which the search or seizure is executed. See <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">ibid.</a></span></i> (citing <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985) ("seizure by means of deadly force"), <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927</a></span> (1995) ("unannounced entry into a home"), <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740</a></span> (1984) ("entry into a home without a warrant"), and <i>Winston</i> v. <i>Lee,</i> <span class="citation" data-id="9429963"><a href="/opinion/111380/winston-v-lee/" aria-description="Citation for case: Winston v. Lee">470 U. S. 753</a></span> (1985) ("physical penetration of the body")). Atwater's arrest was surely "humiliating," as she says in her brief, but it was no more "harmful to . . . privacy or . . . physical interests" than the normal custodial arrest. She was handcuffed, placed in a squad car, and <span class="star-pagination">*355</span> taken to the local police station, where officers asked her to remove her shoes, jewelry, and glasses, and to empty her pockets. They then took her photograph and placed her in a cell, alone, for about an hour, after which she was taken before a magistrate, and released on $310 bond. The arrest and booking were inconvenient and embarrassing to Atwater, but not so extraordinary as to violate the Fourth Amendment.</p>
<p>The Court of Appeals's en banc judgment is affirmed.</p>
<p><i>It is so ordered.</i> </p>
<p>APPENDIX TO OPINION OF THE COURT</p>
<p>State Statutes Authorizing Warrantless Misdemeanor Arrests <span class="citation no-link">Ala. Code § 15-10-3</span>(a)(1) (Supp. 2000) (authorizing warrantless arrest for any "public offense" committed in the presence of the officer);</p>
<p><span class="citation no-link">Alaska Stat. Ann. § 12.25.030</span>(a)(1) (2000) ("for a crime committed . . . in the presence of the person making the arrest");</p>
<p><span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-3883</span>(a)(2) (Supp. 2000) (for a misdemeanor committed in the officer's presence);</p>
<p><span class="citation no-link">Ark. Code Ann. § 16-81-106</span>(b)(2)(a) (Supp. 1999) ("where a public offense is committed in [the officer's] presence");</p>
<p>Cal. Penal Code Ann. § 836(a)(1) (West Supp. 2001) (where "the person to be arrested has committed a public offense in the officer's presence");</p>
<p><span class="citation no-link">Colo. Rev. Stat. § 16</span>-3102(1)(b) (2000) (when "[a]ny crime has been or is being committed" in the officer's presence); <span class="citation no-link">Conn. Gen. Stat. § 54</span>-1f(a) (Supp. 2000) (for "any offense" when arrestee is taken in the act);</p>
<p>Del. Code Ann., Tit. 11, § 1904(a)(1) (1995) (for any misdemeanor committed in the officer's presence);</p>
<p><span class="star-pagination">*356</span> D. C. Code Ann. § 23-581(a)(1)(B) (1996) (where officer has probable cause to believe a person has committed an offense in the officer's presence);</p>
<p><span class="citation no-link">Fla. Stat. § 901.15</span>(1) (Supp. 2001) (for misdemeanor or ordinance violation committed in presence of the officer);</p>
<p><span class="citation no-link">Ga. Code Ann. § 17</span>-420(a) (Supp. 1996) ("for a crime . . . if the offense is committed in [the] officer's presence");</p>
<p><span class="citation no-link">Haw. Rev. Stat. § 803-5</span>(a) (1999) ("when the officer has probable cause to believe that [a] person has committed any offense");</p>
<p><span class="citation no-link">Idaho Code § 19-603</span>(1) (1997) ("[f]or a public offense committed or attempted in [officer's] presence");</p>
<p>Ill. Comp. Stat., ch. 725, § 5/107-2(1)(c) (1992) (when the officer "has reasonable grounds to believe that the person is committing or has committed an offense");</p>
<p><span class="citation no-link">Ind. Code § 35-33</span>-11(a)(4) (Supp. 2000) (when the officer has probable cause to believe a person "is committing or attempting to commit a misdemeanor in the officer's presence");</p>
<p><span class="citation no-link">Iowa Code § 804.7</span>(1) (1994) ("[f]or a public offense committed or attempted in the peace officer's presence");</p>
<p><span class="citation no-link">Kan. Stat. Ann. § 22-2401</span>(d) (1999 Cum. Supp.) (for "[a]ny crime, except a traffic infraction or a cigarette or tobacco infraction," committed in the officer's view);</p>
<p><span class="citation no-link">Ky. Rev. Stat. Ann. § 431.005</span>(1)(d) (Michie 1999) (for any offense punishable by confinement committed in the officer's presence); § 431.015(2) (Supp. 2000) (officer should generally issue citation rather than arrest for certain minor "violations");</p>
<p>La. Code Crim. Proc. Ann., Art. 213(3) (West 1991) (where the officer "has reasonable cause to believe that the person to be arrested has committed an offense");</p>
<p>Me. Rev. Stat. Ann., Tit. 15, § 704 (1980) ("persons found violating any law of the State or any legal ordinance or bylaw <span class="star-pagination">*357</span> of a town"); Tit. 17A, § 15(1)(B) (1983 and Supp. 2000) (for misdemeanors committed in the officer's presence);</p>
<p>Md. Ann. Code, Art. 27, § 594B(a) (1996 and 2000 Supp.) (any person who commits, or attempts to commit, "any felony or misdemeanor" in the presence of an officer);</p>
<p>Mass. Gen. Laws, ch. 276, § 28 (1997) (for designated misdemeanor offenses); ch. 272, § 60 (for littering offenses where identity of arrestee is not known to officer);</p>
<p><span class="citation no-link">Mich. Comp. Laws Ann. § 764.15</span>(1)(a) (West 2000) (for felony, misdemeanor, or ordinance violation committed in the officer's presence);</p>
<p><span class="citation no-link">Minn. Stat. § 629.34</span>(1)(c)(1) (Supp. 2001) ("when a public offense has been committed or attempted in the officer's presence");</p>
<p><span class="citation no-link">Miss. Code Ann. § 99</span>-37 (Supp. 1998) (for indictable offense committed in presence of officer); § 45-321(1)(a)(vi) (by Highway Safety Patrol Officers of "any person or persons committing or attempting to commit any misdemeanor, felony or breach of the peace within their presence or view");</p>
<p><span class="citation no-link">Mo. Rev. Stat. § 479.110</span> (2000) (of "any person who commits an offense in [the officer's] presence");</p>
<p><span class="citation no-link">Mont. Code Ann. § 46</span>-6311(1) (1997) (if "the officer has probable cause to believe that the person is committing an offense");</p>
<p><span class="citation no-link">Neb. Rev. Stat. § 29-404.02</span>(2)(d) (1995) (when the officer has probable cause to believe that the person has committed a misdemeanor in his presence);</p>
<p><span class="citation no-link">Nev. Rev. Stat. § 171.172</span> (1997) (in fresh pursuit of a person who commits "any criminal offense" in the presence of the officer);</p>
<p>N. H. Rev. Stat. Ann. § 614:7 (Supp. 2000) (in fresh pursuit of any person who has committed "any criminal offense" in the presence of the officer); § 594:10(I)(a) (upon probable <span class="star-pagination">*358</span> cause for misdemeanor or violation committed in officer's presence);</p>
<p>N. J. Stat. Ann. § 53:2-1 (West Supp. 2000) ("for violations of the law committed in [the officers'] presence");</p>
<p>N. M. Stat. Ann. § 3-13-2(A)(4)(d) (1999) ("any person in the act of violating the laws of the state or the ordinances of the municipality"); § 30-16-16(B) (1994) (for falsely obtaining services or accommodations); § 30-16-23 (of any person officer has probable cause to believe has committed the crime of shoplifting);</p>
<p>N. Y. Crim. Proc. Law §§ 140.10(1)(a) and (2) (McKinney Supp. 2001) (when officer has probable cause to believe any offense has been committed in his presence and probable cause to believe person to be arrested committed the offense);</p>
<p>N. C. Gen. Stat. § 15A-401(b) (1999) (where an officer has probable cause to believe the person has committed "a criminal offense" in the officer's presence and for misdemeanors out of the officers presence in certain circumstances);</p>
<p>N. D. Cent. Code § 29-06-15(1)(a) (Supp. 1999) ("[f]or a public offense, committed or attempted in the officer's presence");</p>
<p><span class="citation no-link">Ohio Rev. Code Ann. § 2935.03</span> (1997 and Supp. 2000) (of a person "found violating . . . a law of this state, an ordinance of a municipal corporation, or a resolution of a township");</p>
<p>but see § 2935.26 (1997) (providing that notwithstanding any other provision of the Revised Code, when a law enforcement officer is otherwise authorized to arrest a person for the commission of a minor misdemeanor, the officer shall not arrest the person, but shall issue a citation, except in specified circumstances);</p>
<p>Okla. Stat., Tit. 22, § 196(1) (Supp. 2001) ("[f]or a public offense, committed or attempted in [the officer's] presence");</p>
<p>Ore. Rev. Stat. § 133.310(1) (1997) (upon probable cause for any felony, Class A misdemeanor, or any other offense in the <span class="star-pagination">*359</span> officer's presence except "traffic infractions" and minor "violations");</p>
<p>Pa. Stat. Ann., Tit. 71, § 252(a) (Purdon 1990) ("for all violations of the law, including laws regulating the use of the highways, which they may witness");</p>
<p>R. I. Gen. Laws § 12-73 (2000) (for misdemeanors and petty misdemeanors where "[t]he officer has reasonable grounds to believe that [the] person cannot be arrested later, or [m]ay cause injury to himself or herself or others or loss or damage to property unless immediately arrested");</p>
<p>S. C. Code Ann. § 17-13-30 (1985) (of persons who, in the presence of the officer, "violate any of the criminal laws of this State if such arrest be made at the time of such violation of law or immediately thereafter");</p>
<p>S. D. Codified Laws § 23A-3-2 (1998) ("[f]or a public offense, other than a petty offense, committed or attempted in [the officer's] presence");</p>
<p><span class="citation no-link">Tenn. Code Ann. § 40</span>-7103(a)(1) (Supp. 2000) ("[f]or a public offense committed or a breach of the peace threatened in the officer's presence"); see also § 40-7118(b)(1) (1997) (officer who has arrested a person for the commission of a misdemeanor should generally issue a citation to such arrested person to appear in court in lieu of the continued custody and the taking of the arrested person before a magistrate);</p>
<p>Tex. Code Crim. Proc. Ann., Art. 14.01 (Vernon 1977) ("for any offense committed in his presence or within his view");</p>
<p><span class="citation no-link">Utah Code Ann. § 10</span>-3915 (1999) (for "any offense directly prohibited by the laws of this state or by ordinance"); § 77 7-2 (for any public offense committed in presence of officer);</p>
<p>Vt. Rule Crim. Proc. 3(a) (2000) (where officer has probable cause to believe that "a crime" is committed in his presence);</p>
<p>see also Rule 3(c) (law enforcement officer acting without warrant who is authorized to arrest a person for a misdemeanor should generally issue a citation to appear before a judicial officer in lieu of arrest);</p>
<p><span class="star-pagination">*360</span> <span class="citation no-link">Va. Code Ann. § 19.2-81</span> (2000) (of "any person who commits any crime in the presence of [an] officer");</p>
<p><span class="citation no-link">Wash. Rev. Code § 10.31.100</span> (Supp. 2001), as amended by 2000 Wash. Laws 119, § 4 (for misdemeanors committed in the presence of the officer);</p>
<p><span class="citation no-link">W. Va. Code § 62-10-9</span> (2000) ("for all violations of any of the criminal laws of the United States, or of this state, when committed in [an officer's] presence");</p>
<p><span class="citation no-link">Wis. Stat. § 968.07</span>(1)(d) (1998) (when "[t]here are reasonable grounds to believe that the person is committing or has committed a crime"); and</p>
<p><span class="citation no-link">Wyo. Stat. Ann. § 7</span>-2102(b)(i) (1999) (when "[a]ny criminal offense" is committed "in the officer's presence").</p>
<p>Justice O'Connor, with whom Justice Stevens, Justice Ginsburg, and Justice Breyer join, dissenting.</p>
<p>The Fourth Amendment guarantees the right to be free from "unreasonable searches and seizures." The Court recognizes that the arrest of Gail Atwater was a "pointless indignity" that served no discernible state interest, <i>ante,</i> at 347, and yet holds that her arrest was constitutionally permissible. Because the Court's position is inconsistent with the explicit guarantee of the Fourth Amendment, I dissent.</p>
<p></p>
<h2>I</h2>
<p>A full custodial arrest, such as the one to which Ms. Atwater was subjected, is the quintessential seizure. See <i>Payton</i> v. <i>New York,</i> <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#585" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 585</a></span> (1980). When a full custodial arrest is effected without a warrant, the plain language of the Fourth Amendment requires that the arrest be reasonable. See <i><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">ibid.</a></span></i> It is beyond cavil that "[t]he touchstone of our analysis under the Fourth Amendment is always `the reasonableness in all the circumstances of the particular governmental invasion of a citizen's personal security.' " <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#108" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 108-109</a></span> (1977) <i>(per curiam)</i> (quoting <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, 19 <span class="star-pagination">*361</span> (1968)). See also, <i>e. g., </i><i>United States</i> v. <i>Ramirez,</i> <span class="citation" data-id="118180"><a href="/opinion/118180/united-states-v-ramirez/#71" aria-description="Citation for case: United States v. Ramirez">523 U. S. 65, 71</a></span> (1998); <i>Maryland</i> v. <i>Wilson,</i> <span class="citation" data-id="9433418"><a href="/opinion/118086/maryland-v-wilson/#411" aria-description="Citation for case: Maryland v. Wilson">519 U. S. 408, 411</a></span> (1997); <i>Ohio</i> v. <i>Robinette,</i> <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#39" aria-description="Citation for case: Ohio v. Robinette">519 U. S. 33, 39</a></span> (1996); <i>Florida</i> v. <i>Jimeno,</i>  <span class="citation" data-id="9432279"><a href="/opinion/112595/florida-v-jimeno/#250" aria-description="Citation for case: Florida v. Jimeno">500 U. S. 248, 250</a></span> (1991); <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977).</p>
<p>We have "often looked to the common law in evaluating the reasonableness, for Fourth Amendment purposes, of police activity." <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#13" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1, 13</a></span> (1985). But history is just one of the tools we use in conducting the reasonableness inquiry. See <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#13" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 13-19</a></span>; see also <i>Wilson</i> v. <i>Arkansas,</i> <span class="citation" data-id="117936"><a href="/opinion/117936/wilson-v-arkansas/#929" aria-description="Citation for case: Wilson v. Arkansas">514 U. S. 927, 929</a></span> (1995); <i>Wyoming</i> v. <i>Houghton,</i>  <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#307" aria-description="Citation for case: Wyoming v. Houghton">526 U. S. 295, 307</a></span> (1999) (Breyer, J., concurring). And when history is inconclusive, as the majority amply demonstrates it is in this case, see <i>ante,</i> at 326-345, we will "evaluate the search or seizure under traditional standards of reasonableness by assessing, on the one hand, the degree to which it intrudes upon an individual's privacy and, on the other, the degree to which it is needed for the promotion of legitimate governmental interests." <i>Wyoming</i> v. <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton"><i>Houghton, supra,</i> at 300</a></span>. See also, <i>e. g., </i><i>Skinner</i> v. <i>Railway Labor Executives' Assn.,</i> <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#619" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U. S. 602, 619</a></span> (1989); <i>Tennessee</i>  v. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#8" aria-description="Citation for case: Tennessee v. Garner"><i>Garner, supra,</i> at 8</a></span>; <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654</a></span> (1979); <i>Pennsylvania</i> v. <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms"><i>Mimms, supra,</i> at 109</a></span>. In other words, in determining reasonableness, "[e]ach case is to be decided on its own facts and circumstances." <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#357" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 357</a></span> (1931).</p>
<p>The majority gives a brief nod to this bedrock principle of our Fourth Amendment jurisprudence, and even acknowledges that "Atwater's claim to live free of pointless indignity and confinement clearly outweighs anything the City can raise against it specific to her case." <i>Ante,</i> at 347. But instead of remedying this imbalance, the majority allows itself to be swayed by the worry that "every discretionary judgment in the field [will] be converted into an occasion for constitutional review." <i><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">Ibid.</a></span></i> It therefore mints a new rule that "[i]f an officer has probable cause to believe that an individual <span class="star-pagination">*362</span> has committed even a very minor criminal offense in his presence, he may, without violating the Fourth Amendment, arrest the offender." <i>Ante,</i> at 354. This rule is not only unsupported by our precedent, but runs contrary to the principles that lie at the core of the Fourth Amendment.</p>
<p>As the majority tacitly acknowledges, we have never considered the precise question presented here, namely, the constitutionality of a warrantless arrest for an offense punishable only by fine. Cf. <i><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">ibid.</a></span></i> Indeed, on the rare occasions that Members of this Court have contemplated such an arrest, they have indicated disapproval. See, <i>e. g., </i><i>Gustafson</i>  v. <i>Florida,</i> <span class="citation" data-id="9425477"><a href="/opinion/108894/gustafson-v-florida/#266" aria-description="Citation for case: Gustafson v. Florida">414 U. S. 260, 266-267</a></span> (1973) (Stewart, J., concurring) ("[A] persuasive claim might have been made . . . that the custodial arrest of the petitioner for a minor traffic offense violated his rights under the Fourth and Fourteenth Amendments. But no such claim has been made"); <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#238" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 238, n. 2</a></span> (1973) (Powell, J., concurring) (the validity of a custodial arrest for a minor traffic offense is not "self-evident").</p>
<p>To be sure, we have held that the existence of probable cause is a necessary condition for an arrest. See <i>Dunaway</i>  v. <i>New York,</i> <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#213" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 213-214</a></span> (1979). And in the case of felonies punishable by a term of imprisonment, we have held that the existence of probable cause is also a sufficient condition for an arrest. See <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#416" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 416-417</a></span> (1976). In <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>,</i> however, there was a clear and consistently applied common law rule permitting warrantless felony arrests. See <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#417" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 417-422</a></span>. Accordingly, our inquiry ended there and we had no need to assess the reasonableness of such arrests by weighing individual liberty interests against state interests. Cf. <i>Wyoming</i> v. <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#299" aria-description="Citation for case: Wyoming v. Houghton"><i>Houghton, supra,</i> at 299-300</a></span>; <i>Tennessee</i> v. <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#26" aria-description="Citation for case: Tennessee v. Garner"><i>Garner, supra,</i> at 26</a></span> (O'Connor, J., dissenting) (criticizing majority for disregarding undisputed common law rule).</p>
<p>Here, however, we have no such luxury. The Court's thorough exegesis makes it abundantly clear that warrantless <span class="star-pagination">*363</span> misdemeanor arrests were not the subject of a clear and consistently applied rule at common law. See, <i>e. g., ante,</i> at 332 (finding "disagreement, not unanimity, among both the common-law jurists and the text writers"); <i>ante,</i> at 335 (acknowledging that certain early English statutes serve only to "riddle Atwater's supposed common-law rule with enough exceptions to unsettle any contention [that there was a clear common-law rule barring warrantless arrests for misdemeanors that were not breaches of the peace]"). We therefore must engage in the balancing test required by the Fourth Amendment. See <i>Wyoming</i> v. <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#299" aria-description="Citation for case: Wyoming v. Houghton"><i>Houghton, supra,</i> at 299-300</a></span>. While probable cause is surely a necessary condition for warrantless arrests for fine-only offenses, see <i>Dunaway</i> v. <i>New York, supra,</i> at 213-214, any realistic assessment of the interests implicated by such arrests demonstrates that probable cause alone is not a sufficient condition. See <i>infra,</i>  at 364-366.</p>
<p>Our decision in <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">517 U. S. 806</a></span> (1996), is not to the contrary. The specific question presented there was whether, in evaluating the Fourth Amendment reasonableness of a traffic stop, the subjective intent of the police officer is a relevant consideration. <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#808" aria-description="Citation for case: Whren v. United States"><i>Id.,</i> at 808, 814</a></span>. We held that it is not, and stated that "[t]he making of a traffic stop . . . is governed by the usual rule that probable cause to believe the law has been broken `outbalances' private interest in avoiding police contact." <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#818" aria-description="Citation for case: Whren v. United States"><i>Id.,</i> at 818</a></span>.</p>
<p>We of course did not have occasion in <i><span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/" aria-description="Citation for case: Whren v. United States">Whren</a></span></i> to consider the constitutional preconditions for warrantless arrests for fine-only offenses. Nor should our words be taken beyond their context. There are significant qualitative differences between a traffic stop and a full custodial arrest. While both are seizures that fall within the ambit of the Fourth Amendment, the latter entails a much greater intrusion on an individual's liberty and privacy interests. As we have said, "[a] motorist's expectations, when he sees a policeman's light flashing behind him, are that he will be obliged to spend <span class="star-pagination">*364</span> a short period of time answering questions and waiting while the officer checks his license and registration, that he may be given a citation, but that in the end he most likely will be allowed to continue on his way." <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#437" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 437</a></span> (1984). Thus, when there is probable cause to believe that a person has violated a minor traffic law, there can be little question that the state interest in law enforcement will justify the relatively limited intrusion of a traffic stop. It is by no means certain, however, that where the offense is punishable only by fine, "probable cause to believe the law has been broken [will] `outbalanc[e]' private interest in avoiding" a full custodial arrest. <i>Whren</i> v. <i>United States, supra,</i> at 818. Justifying a full arrest by the same quantum of evidence that justifies a traffic stopeven though the offender cannot ultimately be imprisoned for her conductdefies any sense of proportionality and is in serious tension with the Fourth Amendment's proscription of unreasonable seizures.</p>
<p>A custodial arrest exacts an obvious toll on an individual's liberty and privacy, even when the period of custody is relatively brief. The arrestee is subject to a full search of her person and confiscation of her possessions. <i>United States</i> v. <i><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">Robinson, supra</a></span></i><i>.</i> If the arrestee is the occupant of a car, the entire passenger compartment of the car, including packages therein, is subject to search as well. See <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981). The arrestee may be detained for up to 48 hours without having a magistrate determine whether there in fact was probable cause for the arrest. See <i>County of Riverside</i> v. <i>McLaughlin,</i> <span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U. S. 44</a></span> (1991). Because people arrested for all types of violent and nonviolent offenses may be housed together awaiting such review, this detention period is potentially dangerous. Rosazza &amp; Cook, Jail Intake: Managing A Critical FunctionPart One: Resources, 13 American Jails 35 (Mar./Apr. 1999). And once the period of custody is over, the fact of the arrest is a permanent <span class="star-pagination">*365</span> part of the public record. Cf. <i>Paul</i> v. <i>Davis,</i> <span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">424 U. S. 693</a></span> (1976).</p>
<p>We have said that "the penalty that may attach to any particular offense seems to provide the clearest and most consistent indication of the State's interest in arresting individuals suspected of committing that offense." <i>Welsh</i> v. <i>Wisconsin,</i> <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#754" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 754, n. 14</a></span> (1984). If the State has decided that a fine, and not imprisonment, is the appropriate punishment for an offense, the State's interest in taking a person suspected of committing that offense into custody is surely limited, at best. This is not to say that the State will never have such an interest. A full custodial arrest may on occasion vindicate legitimate state interests, even if the crime is punishable only by fine. Arrest is the surest way to abate criminal conduct. It may also allow the police to verify the offender's identity and, if the offender poses a flight risk, to ensure her appearance at trial. But when such considerations are not present, a citation or summons may serve the State's remaining law enforcement interests every bit as effectively as an arrest. Cf. Lodging for State of Texas et al. as <i>Amici Curiae</i> (Texas Department of Public Safety, Student Handout, Traffic Law Enforcement 1 (1999)) ("Citations. . . . Definitiona means of getting violators to court without physical arrest. A citation should be used when it will serve this purpose except when by issuing a citation and releasing the violator, the safety of the public and/or the violator might be imperiled as in the case of D. W. I.").</p>
<p>Because a full custodial arrest is such a severe intrusion on an individual's liberty, its reasonableness hinges on "the degree to which it is needed for the promotion of legitimate governmental interests." <i>Wyoming</i> v. <i>Houghton,</i> <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton">526 U. S., at 300</a></span>. In light of the availability of citations to promote a State's interests when a fine-only offense has been committed, I cannot concur in a rule which deems a full custodial arrest to be reasonable in every circumstance. Giving police <span class="star-pagination">*366</span> officers constitutional carte blanche to effect an arrest whenever there is probable cause to believe a fine-only misdemeanor has been committed is irreconcilable with the Fourth Amendment's command that seizures be reasonable. Instead, I would require that when there is probable cause to believe that a fine-only offense has been committed, the police officer should issue a citation unless the officer is "able to point to specific and articulable facts which, taken together with rational inferences from those facts, reasonably warrant [the additional] intrusion" of a full custodial arrest. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span>.</p>
<p>The majority insists that a bright-line rule focused on probable cause is necessary to vindicate the State's interest in easily administrable law enforcement rules. See <i>ante,</i> at 347-351. Probable cause itself, however, is not a model of precision. "The quantum of information which constitutes probable causeevidence which would `warrant a man of reasonable caution in the belief' that a [crime] has been committedmust be measured by the facts of the particular case." <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479</a></span> (1963) (citation omitted). The rule I proposewhich merely requires a legitimate reason for the decision to escalate the seizure into a full custodial arrestthus does not undermine an otherwise "clear and simple" rule. Cf. <i>ante,</i> at 347.</p>
<p>While clarity is certainly a value worthy of consideration in our Fourth Amendment jurisprudence, it by no means trumps the values of liberty and privacy at the heart of the Amendment's protections. What the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> rule lacks in precision it makes up for in fidelity to the Fourth Amendment's command of reasonableness and sensitivity to the competing values protected by that Amendment. Over the past 30 years, it appears that the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> rule has been workable and easily applied by officers on the street.</p>
<p>At bottom, the majority offers two related reasons why a bright-line rule is necessary: the fear that officers who arrest for fine-only offenses will be subject to "personal [42 U. S. C.] <span class="star-pagination">*367</span> § 1983 liability for the misapplication of a constitutional standard," <i>ante,</i> at 350, and the resulting "systematic disincentive to arrest . . . where . . . arresting would serve an important societal interest," <i>ante,</i> at 351. These concerns are certainly valid, but they are more than adequately resolved by the doctrine of qualified immunity.</p>
<p>Qualified immunity was created to shield government officials from civil liability for the performance of discretionary functions so long as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known. See <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982). This doctrine is "the best attainable accommodation of competing values," namely, the obligation to enforce constitutional guarantees and the need to protect officials who are required to exercise their discretion. <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#814" aria-description="Citation for case: Harlow v. Fitzgerald"><i>Id.,</i> at 814</a></span>.</p>
<p>In <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635</a></span> (1987), we made clear that the standard of reasonableness for a search or seizure under the Fourth Amendment is distinct from the standard of reasonableness for qualified immunity purposes. <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton"><i>Id.,</i> at 641</a></span>. If a law enforcement officer "reasonably but mistakenly conclude[s]" that the constitutional predicate for a search or seizure is present, he "should not be held personally liable." <i><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Ibid.</a></span></i> </p>
<p>This doctrine thus allays any concerns about liability or disincentives to arrest. If, for example, an officer reasonably thinks that a suspect poses a flight risk or might be a danger to the community if released, cf. <i>ante,</i> at 351, he may arrest without fear of the legal consequences. Similarly, if an officer reasonably concludes that a suspect may possess more than four ounces of marijuana and thus might be guilty of a felony, cf. <i>ante,</i> at 348-349, and n. 19, 351, the officer will be insulated from liability for arresting the suspect even if the initial assessment turns out to be factually incorrect. As we have said, "officials will not be liable for mere mistakes in judgment." <i>Butz</i> v. <i>Economou,</i> <span class="citation" data-id="9427337"><a href="/opinion/109932/butz-v-economou/" aria-description="Citation for case: Butz v. Economou">438 U. S. 478</a></span>, 507 <span class="star-pagination">*368</span> (1978). Of course, even the specter of liability can entail substantial social costs, such as inhibiting public officials in the discharge of their duties. See, <i>e. g., </i><i>Harlow</i> v. <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#814" aria-description="Citation for case: Harlow v. Fitzgerald"><i>Fitzgerald, supra,</i> at 814</a></span>. We may not ignore the central command of the Fourth Amendment, however, to avoid these costs.</p>
<p></p>
<h2>II</h2>
<p>The record in this case makes it abundantly clear that Ms. Atwater's arrest was constitutionally unreasonable. Atwater readily admitsas she did when Officer Turek pulled her overthat she violated Texas' seatbelt law. Brief for Petitioners 2-3; Record 381, 384. While Turek was justified in stopping Atwater, see <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#819" aria-description="Citation for case: Whren v. United States">517 U. S., at 819</a></span>, neither law nor reason supports his decision to arrest her instead of simply giving her a citation. The officer's actions cannot sensibly be viewed as a permissible means of balancing Atwater's Fourth Amendment interests with the State's own legitimate interests.</p>
<p>There is no question that Officer Turek's actions severely infringed Atwater's liberty and privacy. Turek was loud and accusatory from the moment he approached Atwater's car. Atwater's young children were terrified and hysterical. Yet when Atwater asked Turek to lower his voice because he was scaring the children, he responded by jabbing his finger in Atwater's face and saying, "You're going to jail." Record 382, 384. Having made the decision to arrest, Turek did not inform Atwater of her right to remain silent. <i>Id.,</i> at 390, 704. He instead asked for her license and insurance information. <i>Id.,</i> at 382. But cf. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).</p>
<p>Atwater asked if she could at least take her children to a friend's house down the street before going to the police station. Record 384. But Turekwho had just castigated Atwater for not caring for her childrenrefused and said he would take the children into custody as well. <i>Id.,</i> at 384, 427, 704-705. Only the intervention of neighborhood <span class="star-pagination">*369</span> children who had witnessed the scene and summoned one of Atwater's friends saved the children from being hauled to jail with their mother. <i>Id.,</i> at 382, 385-386.</p>
<p>With the children gone, Officer Turek handcuffed Ms. Atwater with her hands behind her back, placed her in the police car, and drove her to the police station. <i>Id.,</i> at 386-387. Ironically, Turek did not secure Atwater in a seatbelt for the drive. <i>Id.,</i> at 386. At the station, Atwater was forced to remove her shoes, relinquish her possessions, and wait in a holding cell for about an hour. <i>Id.,</i> at 387, 706. A judge finally informed Atwater of her rights and the charges against her, and released her when she posted bond. <i>Id.,</i> at 387-388, 706. Atwater returned to the scene of the arrest, only to find that her car had been towed. <i>Id.,</i> at 389.</p>
<p>Ms. Atwater ultimately pleaded no contest to violating the seatbelt law and was fined $50. <i>Id.,</i> at 403. Even though that fine was the maximum penalty for her crime, <span class="citation no-link">Tex. Transp. Code Ann. § 545.413</span>(d) (1999), and even though Officer Turek has never articulated any justification for his actions, the city contends that arresting Atwater was constitutionally reasonable because it advanced two legitimate interests: "the enforcement of child safety laws and encouraging [Atwater] to appear for trial." Brief for Respondents 15.</p>
<p>It is difficult to see how arresting Atwater served either of these goals any more effectively than the issuance of a citation. With respect to the goal of law enforcement generally, Atwater did not pose a great danger to the community. She had been driving very slowlyapproximately 15 miles per hourin broad daylight on a residential street that had no other traffic. Record 380. Nor was she a repeat offender; until that day, she had received one traffic citation in her lifea ticket, more than 10 years earlier, for failure to signal a lane change. <span class="citation no-link"><i>Id.,</i> at 378</span>. Although Officer Turek had stopped Atwater approximately three months earlier because he thought that Atwater's son was not wearing a seatbelt, <span class="citation no-link"><i>id.,</i> at 420</span>, Turek had been mistaken, <span class="citation no-link"><i>id.,</i> at 379, 703</span>. <span class="star-pagination">*370</span> Moreover, Atwater immediately accepted responsibility and apologized for her conduct. <span class="citation no-link"><i>Id.,</i> at 381, 384, 420</span>. Thus, there was every indication that Atwater would have buckled herself and her children in had she been cited and allowed to leave.</p>
<p>With respect to the related goal of child welfare, the decision to arrest Atwater was nothing short of counterproductive. Atwater's children witnessed Officer Turek yell at their mother and threaten to take them all into custody. Ultimately, they were forced to leave her behind with Turek, knowing that she was being taken to jail. Understandably, the 3-year-old boy was "very, very, very traumatized." <span class="citation no-link"><i>Id.,</i>  at 393</span>. After the incident, he had to see a child psychologist regularly, who reported that the boy "felt very guilty that he couldn't stop this horrible thing . . . he was powerless to help his mother or sister." <span class="citation no-link"><i>Id.,</i> at 396</span>. Both of Atwater's children are now terrified at the sight of any police car. <span class="citation no-link"><i>Id.,</i>  at 393, 395</span>. According to Atwater, the arrest "just never leaves us. It's a conversation we have every other day, once a week, and it'sit raises its head constantly in our lives." <span class="citation no-link"><i>Id.,</i> at 395</span>.</p>
<p>Citing Atwater surely would have served the children's interests well. It would have taught Atwater to ensure that her children were buckled up in the future. It also would have taught the children an important lesson in accepting responsibility and obeying the law. Arresting Atwater, though, taught the children an entirely different lesson: that "the bad person could just as easily be the policeman as it could be the most horrible person they could imagine." <i><span class="citation no-link">Ibid.</span></i> </p>
<p>Respondents also contend that the arrest was necessary to ensure Atwater's appearance in court. Atwater, however, was far from a flight risk. A 16-year resident of Lago Vista, population 2,486, Atwater was not likely to abscond. See Record 376; Texas State Data Center, 1997 Total Population Estimates for Texas Places 15 (Sept. 1998). Although she <span class="star-pagination">*371</span> was unable to produce her driver's license because it had been stolen, she gave Officer Turek her license number and address. Record 386. In addition, Officer Turek knew from their previous encounter that Atwater was a local resident.</p>
<p>The city's justifications fall far short of rationalizing the extraordinary intrusion on Gail Atwater and her children. Measuring "the degree to which [Atwater's custodial arrest was] needed for the promotion of legitimate governmental interests," against "the degree to which it intrud[ed] upon [her] privacy," <i>Wyoming</i> v. <i>Houghton,</i> <span class="citation" data-id="9433782"><a href="/opinion/118277/wyoming-v-houghton/#300" aria-description="Citation for case: Wyoming v. Houghton">526 U. S., at 300</a></span>, it can hardly be doubted that Turek's actions were disproportionate to Atwater's crime. The majority's assessment that "Atwater's claim to live free of pointless indignity and confinement clearly outweighs anything the City can raise against it specific to her case," <i>ante,</i> at 347, is quite correct. In my view, the Fourth Amendment inquiry ends there.</p>
<p></p>
<h2>III</h2>
<p>The Court's error, however, does not merely affect the disposition of this case. The <i>per se</i> rule that the Court creates has potentially serious consequences for the everyday lives of Americans. A broad range of conduct falls into the category of fine-only misdemeanors. In Texas alone, for example, disobeying any sort of traffic warning sign is a misdemeanor punishable only by fine, see <span class="citation no-link">Tex. Transp. Code Ann. § 472.022</span> (1999 and Supp. 2000-2001), as is failing to pay a highway toll, see § 284.070, and driving with expired license plates, see § 502.407. Nor are fine-only crimes limited to the traffic context. In several States, for example, littering is a criminal offense punishable only by fine. See, <i>e. g.,</i> Cal. Penal Code Ann. § 374.7 (West 1999); Ga. Code Ann. § 16 7-43 (1996); <span class="citation no-link">Iowa Code §§ 321.369</span>, 805.8(2)(af) (Supp. 2001).</p>
<p>To be sure, such laws are valid and wise exercises of the States' power to protect the public health and welfare. My concern lies not with the decision to enact or enforce these <span class="star-pagination">*372</span> laws, but rather with the manner in which they may be enforced. Under today's holding, when a police officer has probable cause to believe that a fine-only misdemeanor offense has occurred, that officer may stop the suspect, issue a citation, and let the person continue on her way. Cf. <i>Whren</i>  v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#806" aria-description="Citation for case: Whren v. United States">517 U. S., at 806</a></span>. Or, if a traffic violation, the officer may stop the car, arrest the driver, see <i>ante,</i> at 354, search the driver, see <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson">414 U. S., at 235</a></span>, search the entire passenger compartment of the car including any purse or package inside, see <i>New York</i> v. <i>Belton,</i> <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>, and impound the car and inventory all of its contents, see <i>Colorado</i> v. <i>Bertine,</i> <span class="citation" data-id="9430773"><a href="/opinion/111788/colorado-v-bertine/#374" aria-description="Citation for case: Colorado v. Bertine">479 U. S. 367, 374</a></span> (1987); <i>Florida</i> v. <i>Wells,</i> <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/#4" aria-description="Citation for case: Florida v. Wells">495 U. S. 1, 4-5</a></span> (1990). Although the Fourth Amendment expressly requires that the latter course be a reasonable and proportional response to the circumstances of the offense, the majority gives officers unfettered discretion to choose that course without articulating a single reason why such action is appropriate.</p>
<p>Such unbounded discretion carries with it grave potential for abuse. The majority takes comfort in the lack of evidence of "an epidemic of unnecessary minor-offense arrests." <i>Ante,</i> at 353, and n. 25. But the relatively small number of published cases dealing with such arrests proves little and should provide little solace. Indeed, as the recent debate over racial profiling demonstrates all too clearly, a relatively minor traffic infraction may often serve as an excuse for stopping and harassing an individual. After today, the arsenal available to any officer extends to a full arrest and the searches permissible concomitant to that arrest. An officer's subjective motivations for making a traffic stop are not relevant considerations in determining the reasonableness of the stop. See <i>Whren</i> v. <i>United States, supra,</i> at 813. But it is precisely because these motivations are beyond our purview that we must vigilantly ensure that officers' poststop actionswhich are properly within our reachcomport with the Fourth Amendment's guarantee of reasonableness.</p>
<p></p>
<h2>
<span class="star-pagination">*373</span> * * *</h2>
<p>The Court neglects the Fourth Amendment's express command in the name of administrative ease. In so doing, it cloaks the pointless indignity that Gail Atwater suffered with the mantle of reasonableness. I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging reversal were filed for the American Civil Liberties Union et al. by <i>Susan N. He

[...TRUNCATED 19712 of 139712 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
