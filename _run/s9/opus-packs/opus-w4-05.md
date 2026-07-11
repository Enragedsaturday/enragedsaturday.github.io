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

## GROUP: _overhaul2/lake/cases/Florida v. Jardines.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. Jardines"
type: case
citation: ""
parallel_cite: "133 S. Ct. 1409; 185 L. Ed. 2d 495; 569 U.S. 1; 24 Fla. L. Weekly Fed. S 117; 81 U.S.L.W. 4209"
neutral_cite: "2013 U.S. LEXIS 2542; 2013 WL 1196577"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-03-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-03-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Jardines
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/856347/florida-v-jardines/"
  cluster_id: 856347
  opinion_id: 856347
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Key — Anchor"
  - page: "[[Trespass]]"
    role: "Key"
related: ["[[Florida v. Harris]]", "[[United States v. Jones]]", "[[California v. Ciraolo]]"]
aliases: []
tags: ["case", "fourth-amendment", "curtilage", "knock-and-talk", "dog-sniff", "trespass"]
holding: "Bringing a drug dog onto the home's curtilage (the front porch) to investigate exceeded the implied license to approach and knock — a…"
lake:
  record_id: Florida v. Jardines
  status: verified
  projected_at: 2026-07-06
---

# Florida v. Jardines

*569 U.S. 1 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Detectives received an unverified tip that Joelis Jardines was growing marijuana in his home. An officer took a drug-detection dog onto Jardines's front porch; the dog sniffed around the base of the front door and alerted to the odor of narcotics. Using that alert, the officer obtained a search warrant, and the ensuing search found marijuana plants. Jardines moved to suppress.

## Issue
Whether using a drug-detection dog on a homeowner's front porch to investigate the contents of the home is a "search" within the meaning of the Fourth Amendment.

## Rule
Yes. Bringing a drug dog onto the [[Curtilage|curtilage]] to gather evidence is a physical intrusion on a constitutionally protected area that exceeds any implied license, and so is a search. "The officers were gathering information in an area belonging to Jardines and immediately surrounding his house—in the curtilage of the house, which we have held enjoys protection as part of the home itself. And they gathered that information by physically entering and occupying the area to engage in conduct not explicitly or implicitly permitted by the homeowner." — [569 U.S. at 6](https://www.courtlistener.com/opinion/856347/florida-v-jardines/#:~:text=to%20Jardines%20and%20immediately%20surrounding%20his%20house). ^pin-6

The implied license that lets a visitor (or officer) walk up and knock does not extend to canine investigation: "But introducing a trained police dog to explore the area around the home in hopes of discovering incriminating evidence is something else. There is no customary invitation to do that." — [*Id.* at 9](https://www.courtlistener.com/opinion/856347/florida-v-jardines/#:~:text=There%20is%20no%20customary%20invitation%20to%20do%20that). ^pin-9

## Application
The officer entered the porch — part of the home's [[Curtilage|curtilage]] — and used a trained dog to detect what was inside, a purpose well outside the customary invitation extended to anyone who walks up to knock. Because the officer physically occupied protected ground to gather evidence beyond the scope of any implied license, the front-door dog sniff was a search; the warrant that followed rested on that unlawful sniff.

## Conclusion
The front-porch dog sniff was an unlicensed physical intrusion and thus a Fourth Amendment search; the Florida Supreme Court's suppression order was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Jardines* fixes the [[Curtilage|curtilage]] / implied-license boundary that governs the [[Knock and Talk|knock-and-talk]]; the separate question of a dog's reliability once it alerts is addressed in [[Florida v. Harris]].

## Appears on
- [[Knock and Talk]] — *Key — Anchor*
- [[Trespass]] — *Key*

## Sources
- *Florida v. Jardines*, 569 U.S. 1 (2013) — https://www.courtlistener.com/opinion/856347/florida-v-jardines/ — pinpoints: 6, 9.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "212349f784ec94df", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. Jardines"}, "payload": {"all": [{"cite": "133 S. Ct. 1409", "page": "1409", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "133"}, {"cite": "185 L. Ed. 2d 495", "page": "495", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "185"}, {"cite": "2013 U.S. LEXIS 2542", "page": "2542", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2013"}, {"cite": "569 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "569"}, {"cite": "24 Fla. L. Weekly Fed. S 117", "page": "117", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "24"}, {"cite": "81 U.S.L.W. 4209", "page": "4209", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "81"}, {"cite": "2013 WL 1196577", "page": "1196577", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2013"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Florida v. Jardines"}}
{"assertion_id": "861f6aaddb45f2e5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-6", "record_id": "Florida v. Jardines"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-6", "pinpoint_status": "slip-only", "quote": "within the meaning of the Fourth Amendment. ## Rule Yes. Bringing a drug dog onto the curtilage to gather evidence is a physical intrusion on a constitutionally protected area that exceeds any implied license, and so is a search.", "quote_fidelity": "mismatch", "record_id": "Florida v. Jardines", "star_marker": null}}
{"assertion_id": "a9431009fbbf3753", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-9", "record_id": "Florida v. Jardines"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-9", "pinpoint_status": "slip-only", "quote": "But introducing a trained police dog to explore the area around the home in hopes of discovering incriminating evidence is something else. There is no customary invitation to do that.", "quote_fidelity": "mismatch", "record_id": "Florida v. Jardines", "star_marker": null}}
{"assertion_id": "943d3bbacd758e93", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. Jardines"}, "payload": {"as_of_content": "2013-03-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. Jardines", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Florida v. Jardines

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Jardines",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Jardines",
    "case_name_short": "Jardines",
    "case_name_full": "FLORIDA, Petitioner v. Joelis JARDINES.",
    "input_case_name": "Florida v. Jardines",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-03-26",
    "year": 2013,
    "docket": null,
    "cluster_id": 856347,
    "lead_opinion_id": 856347,
    "sibling_ids": [
      856347
    ],
    "absolute_url": "/opinion/856347/florida-v-jardines/",
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
        "cite": "133 S. Ct. 1409",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 495",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 1",
        "volume": "569",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 117",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "117",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4209",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4209",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 2542",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "2542",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1196577",
        "volume": "2013",
        "reporter": "WL",
        "page": "1196577",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1409",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 495",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "495",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 2542",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "2542",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 1",
        "volume": "569",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 117",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "117",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4209",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4209",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1196577",
        "volume": "2013",
        "reporter": "WL",
        "page": "1196577",
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
      "id": "pin-6",
      "page": null,
      "quote": "within the meaning of the Fourth Amendment. ## Rule Yes. Bringing a drug dog onto the curtilage to gather evidence is a physical intrusion on a constitutionally protected area that exceeds any implied license, and so is a search.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-9",
      "page": null,
      "quote": "But introducing a trained police dog to explore the area around the home in hopes of discovering incriminating evidence is something else. There is no customary invitation to do that.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-03-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Jardines",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Florida v. Jardines:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Phillips",
          "cluster_id": 10125493,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Phillips",
          "cluster_id": 10055410,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane1_negative"
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
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
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
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Schenectady",
          "cluster_id": 1038554,
          "cite": [
            "728 F.3d 149",
            "2013 U.S. App. LEXIS 17943",
            "2013 WL 4528864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turrubiate v. State",
          "cluster_id": 2948365,
          "cite": [
            "399 S.W.3d 147",
            "2013 WL 1438172",
            "2013 Tex. Crim. App. LEXIS 635"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
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
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Angelo Dahlia v. Omar Rodriguez",
          "cluster_id": 1038229,
          "cite": [
            "735 F.3d 1060",
            "36 I.E.R. Cas. (BNA) 613",
            "2013 WL 4437594",
            "2013 U.S. App. LEXIS 17489",
            "97 Empl. Prac. Dec. (CCH) 44,900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caniglia v. Strom",
          "cluster_id": 4883694,
          "cite": [
            "593 U.S. 194",
            "209 L. Ed. 2d 604",
            "141 S. Ct. 1596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cregan",
          "cluster_id": 2681818,
          "cite": [
            "2014 IL 113600"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sidney Arnold v. Steven Williams",
          "cluster_id": 4799821,
          "cite": [
            "979 F.3d 262"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Talkington",
          "cluster_id": 2784485,
          "cite": [
            "301 Kan. 453",
            "345 P.3d 258",
            "2015 Kan. LEXIS 167",
            "2015 WL 968451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
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
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
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
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North American Butterfly Association v. Chad F. Wolf",
          "cluster_id": 4795622,
          "cite": [
            "977 F.3d 1244"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cuong Phu Le",
          "cluster_id": 2950561,
          "cite": [
            "463 S.W.3d 872",
            "2015 Tex. Crim. App. LEXIS 516",
            "2015 WL 1933960"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Wiedeman",
          "cluster_id": 1033708,
          "cite": [
            "286 Neb. 193",
            "835 N.W.2d 698"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Patterson",
          "cluster_id": 3196972,
          "cite": [
            "304 Kan. 272",
            "371 P.3d 893",
            "2016 WL 1612915",
            "2016 Kan. LEXIS 240"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cary King v. Louisiana Tax Commission",
          "cluster_id": 3201479,
          "cite": [
            "821 F.3d 650",
            "2016 U.S. App. LEXIS 8462",
            "2016 WL 2621454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Com. v. Prater, W.",
          "cluster_id": 10279435,
          "cite": [
            "2021 Pa. Super. 141",
            "256 A.3d 1274"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morse v. Cloutier",
          "cluster_id": 4421636,
          "cite": [
            "869 F.3d 16"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Elvan Moore v. Kevin Pederson",
          "cluster_id": 3066706,
          "cite": [
            "806 F.3d 1036",
            "2015 U.S. App. LEXIS 17894",
            "2015 WL 5973304"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baird v. State",
          "cluster_id": 2948278,
          "cite": [
            "398 S.W.3d 220",
            "2013 WL 1890722",
            "2013 Tex. Crim. App. LEXIS 736"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jardines:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(856347) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjIxMjA5NjAwMDAwJnM9NDg4MzY5NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28856347%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(856347)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01OCZzPTI3NzI3MzAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28856347%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(856347)",
        "reviewed": 143,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 143,
        "triage_read": 3,
        "triage_snippet_classified": 140
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(856347)",
    "indexed_citing_opinions": 750,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 856347,
        "count": 750,
        "count_source": "search"
      }
    ],
    "citation_count": 1623,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-jardines.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0ODc4ODYmcz0xMDY1MjM2OCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28856347%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 856347,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 100047,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 104917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 111305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 111666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 112795,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 137742,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 222692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 319379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 686744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 1443807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 1647372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 2134398,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 2459843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 856347,
        "cited_id": 2484673,
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
    "date_created": "2026-07-05T03:59:43Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:59:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:59:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:05:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:59:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Jardines

```
(Slip Opinion)              OCTOBER TERM, 2012                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                         FLORIDA v. JARDINES

        CERTIORARI TO THE SUPREME COURT OF FLORIDA

    No. 11–564.      Argued October 31, 2012—Decided March 26, 2013
Police took a drug-sniffing dog to Jardines’ front porch, where the dog
  gave a positive alert for narcotics. Based on the alert, the officers ob-
  tained a warrant for a search, which revealed marijuana plants;
  Jardines was charged with trafficking in cannabis. The Supreme
  Court of Florida approved the trial court’s decision to suppress the
  evidence, holding that the officers had engaged in a Fourth Amend-
  ment search unsupported by probable cause.
Held: The investigation of Jardines’ home was a “search” within the
 meaning of the Fourth Amendment. Pp. 3–10.
    (a) When “the Government obtains information by physically in-
 truding” on persons, houses, papers, or effects, “a ‘search’ within the
 original meaning of the Fourth Amendment” has “undoubtedly oc-
 curred.” United States v. Jones, 565 U. S. ___, ___, n. 3. Pp. 3–4.
    (b) At the Fourth Amendment’s “very core” stands “the right of a
 man to retreat into his own home and there be free from unreason-
 able governmental intrusion.” Silverman v. United States, 365 U. S.
 505, 511. The area “immediately surrounding and associated with
 the home”—the curtilage—is “part of the home itself for Fourth
 Amendment purposes.” Oliver v. United States, 466 U. S. 170, 180.
 The officers entered the curtilage here: The front porch is the classic
 exemplar of an area “to which the activity of home life extends.” Id.,
 at 182, n. 12. Pp. 4–5.
    (c) The officers’ entry was not explicitly or implicitly invited. Offi-
 cers need not “shield their eyes” when passing by a home “on public
 thoroughfares,” California v. Ciraolo, 476 U. S. 207, 213, but “no man
 can set his foot upon his neighbour’s close without his leave,” Entick
 v. Carrington, 2 Wils. K. B. 275, 291, 95 Eng. Rep. 807, 817. A police
 officer not armed with a warrant may approach a home in hopes of
 speaking to its occupants, because that is “no more than any private
2                          FLORIDA v. JARDINES

                                   Syllabus

    citizen might do.” Kentucky v. King, 563 U. S. ___, ___. But the scope
    of a license is limited not only to a particular area but also to a specif-
    ic purpose, and there is no customary invitation to enter the curtilage
    simply to conduct a search. Pp. 5–8.
       (d) It is unnecessary to decide whether the officers violated
    Jardines’ expectation of privacy under Katz v. United States, 389
    U. S. 347. Pp. 8–10.
73 So. 3d 34, affirmed.

   SCALIA, J., delivered the opinion of the Court, in which THOMAS,
GINSBURG, SOTOMAYOR, and KAGAN, JJ., joined. KAGAN, J., filed a con-
curring opinion, in which GINSBURG and SOTOMAYOR, JJ., joined. ALITO,
J., filed a dissenting opinion, in which ROBERTS, C. J., and KENNEDY
and BREYER, JJ., joined.
                       Cite as: 569 U. S. ____ (2013)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 11–564
                                  _________________


    FLORIDA, PETITIONER v. JOELIS JARDINES
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       FLORIDA

                               [March 26, 2013]


  JUSTICE SCALIA delivered the opinion of the Court.
  We consider whether using a drug-sniffing dog on a
homeowner’s porch to investigate the contents of the
home is a “search” within the meaning of the Fourth
Amendment.
                             I
  In 2006, Detective William Pedraja of the Miami-Dade
Police Department received an unverified tip that mari-
juana was being grown in the home of respondent Joelis
Jardines. One month later, the Department and the
Drug Enforcement Administration sent a joint surveillance
team to Jardines’ home. Detective Pedraja was part of
that team. He watched the home for fifteen minutes and
saw no vehicles in the driveway or activity around the
home, and could not see inside because the blinds were
drawn. Detective Pedraja then approached Jardines’
home accompanied by Detective Douglas Bartelt, a trained
canine handler who had just arrived at the scene with his
drug-sniffing dog. The dog was trained to detect the scent
of marijuana, cocaine, heroin, and several other drugs,
indicating the presence of any of these substances through
particular behavioral changes recognizable by his handler.
2                  FLORIDA v. JARDINES

                     Opinion of the Court

    Detective Bartelt had the dog on a six-foot leash, owing
in part to the dog’s “wild” nature, App. to Pet. for Cert. A–
35, and tendency to dart around erratically while search-
ing. As the dog approached Jardines’ front porch, he
apparently sensed one of the odors he had been trained to
detect, and began energetically exploring the area for the
strongest point source of that odor. As Detective Bartelt
explained, the dog “began tracking that airborne odor by
. . . tracking back and forth,” engaging in what is called
“bracketing,” “back and forth, back and forth.” Id., at A–
33 to A–34. Detective Bartelt gave the dog “the full six
feet of the leash plus whatever safe distance [he could]
give him” to do this—he testified that he needed to give
the dog “as much distance as I can.” Id., at A–35. And
Detective Pedraja stood back while this was occurring, so
that he would not “get knocked over” when the dog was
“spinning around trying to find” the source. Id., at A–38.
    After sniffing the base of the front door, the dog sat,
which is the trained behavior upon discovering the odor’s
strongest point. Detective Bartelt then pulled the dog
away from the door and returned to his vehicle. He left
the scene after informing Detective Pedraja that there had
been a positive alert for narcotics.
    On the basis of what he had learned at the home, De-
tective Pedraja applied for and received a warrant to
search the residence. When the warrant was executed later
that day, Jardines attempted to flee and was arrested; the
search revealed marijuana plants, and he was charged
with trafficking in cannabis.
    At trial, Jardines moved to suppress the marijuana
plants on the ground that the canine investigation was an
unreasonable search. The trial court granted the motion,
and the Florida Third District Court of Appeal reversed.
On a petition for discretionary review, the Florida Su-
preme Court quashed the decision of the Third District
Court of Appeal and approved the trial court’s decision to
                  Cite as: 569 U. S. ____ (2013)             3

                      Opinion of the Court

suppress, holding (as relevant here) that the use of the
trained narcotics dog to investigate Jardines’ home was
a Fourth Amendment search unsupported by probable
cause, rendering invalid the warrant based upon infor-
mation gathered in that search. 73 So. 3d 34 (2011).
  We granted certiorari, limited to the question of whether
the officers’ behavior was a search within the meaning of
the Fourth Amendment. 565 U. S. ___ (2012).
                               II
   The Fourth Amendment provides in relevant part that
the “right of the people to be secure in their persons, houses,
papers, and effects, against unreasonable searches and
seizures, shall not be violated.” The Amendment estab-
lishes a simple baseline, one that for much of our history
formed the exclusive basis for its protections: When “the
Government obtains information by physically intruding”
on persons, houses, papers, or effects, “a ‘search’ within
the original meaning of the Fourth Amendment” has “un-
doubtedly occurred.” United States v. Jones, 565 U. S.
___, ___, n. 3 (2012) (slip op., at 6, n. 3). By reason of
our decision in Katz v. United States, 389 U. S. 347
(1967), property rights “are not the sole measure of Fourth
Amendment violations,” Soldal v. Cook County, 506 U. S.
56, 64 (1992)—but though Katz may add to the baseline, it
does not subtract anything from the Amendment’s protec-
tions “when the Government does engage in [a] physi-
cal intrusion of a constitutionally protected area,” United
States v. Knotts, 460 U. S. 276, 286 (1983) (Brennan, J.,
concurring in the judgment).
   That principle renders this case a straightforward one.
The officers were gathering information in an area belong-
ing to Jardines and immediately surrounding his house—
in the curtilage of the house, which we have held enjoys
protection as part of the home itself. And they gathered
that information by physically entering and occupying the
4                  FLORIDA v. JARDINES

                     Opinion of the Court

area to engage in conduct not explicitly or implicitly per-
mitted by the homeowner.
                             A
   The Fourth Amendment “indicates with some precision
the places and things encompassed by its protections”:
persons, houses, papers, and effects. Oliver v. United
States, 466 U. S. 170, 176 (1984). The Fourth Amendment
does not, therefore, prevent all investigations conducted
on private property; for example, an officer may (subject to
Katz) gather information in what we have called “open
fields”—even if those fields are privately owned—because
such fields are not enumerated in the Amendment’s text.
Hester v. United States, 265 U. S. 57 (1924).
   But when it comes to the Fourth Amendment, the home
is first among equals. At the Amendment’s “very core”
stands “the right of a man to retreat into his own home
and there be free from unreasonable governmental in-
trusion.” Silverman v. United States, 365 U. S. 505, 511
(1961). This right would be of little practical value if the
State’s agents could stand in a home’s porch or side gar-
den and trawl for evidence with impunity; the right to
retreat would be significantly diminished if the police
could enter a man’s property to observe his repose from
just outside the front window.
   We therefore regard the area “immediately surrounding
and associated with the home”—what our cases call the
curtilage—as “part of the home itself for Fourth Amend-
ment purposes.” Oliver, supra, at 180. That principle has
ancient and durable roots. Just as the distinction between
the home and the open fields is “as old as the common
law,” Hester, supra, at 59, so too is the identity of home
and what Blackstone called the “curtilage or homestall,”
for the “house protects and privileges all its branches and
appurtenants.” 4 W. Blackstone, Commentaries on the
Laws of England 223, 225 (1769). This area around the
                    Cite as: 569 U. S. ____ (2013)                   5

                         Opinion of the Court

home is “intimately linked to the home, both physically
and psychologically,” and is where “privacy expectations
are most heightened.” California v. Ciraolo, 476 U. S. 207,
213 (1986).
   While the boundaries of the curtilage are generally
“clearly marked,” the “conception defining the curtilage” is
at any rate familiar enough that it is “easily understood
from our daily experience.” Oliver, 466 U. S., at 182, n. 12.
Here there is no doubt that the officers entered it: The
front porch is the classic exemplar of an area adjacent to
the home and “to which the activity of home life extends.”
Ibid.
                               B
   Since the officers’ investigation took place in a constitu-
tionally protected area, we turn to the question of whether
it was accomplished through an unlicensed physical in-
trusion.1 While law enforcement officers need not “shield
their eyes” when passing by the home “on public thorough-
fares,” Ciraolo, 476 U. S., at 213, an officer’s leave to
gather information is sharply circumscribed when he steps
off those thoroughfares and enters the Fourth Amend-
ment’s protected areas. In permitting, for example, visual
observation of the home from “public navigable airspace,”
we were careful to note that it was done “in a physically
nonintrusive manner.” Ibid. Entick v. Carrington, 2 Wils.
K. B. 275, 95 Eng. Rep. 807 (K. B. 1765), a case “undoubt-
edly familiar” to “every American statesman” at the time
of the Founding, Boyd v. United States, 116 U. S. 616, 626
——————
   1 At oral argument, the State and its amicus the Solicitor General

argued that Jardines conceded in the lower courts that the officers had
a right to be where they were. This misstates the record. Jardines
conceded nothing more than the unsurprising proposition that the of-
ficers could have lawfully approached his home to knock on the front
door in hopes of speaking with him. Of course, that is not what they
did.
6                       FLORIDA v. JARDINES

                           Opinion of the Court

(1886), states the general rule clearly: “[O]ur law holds the
property of every man so sacred, that no man can set his
foot upon his neighbour’s close without his leave.” 2 Wils.
K. B., at 291, 95 Eng. Rep., at 817. As it is undisputed
that the detectives had all four of their feet and all four of
their companion’s firmly planted on the constitutionally
protected extension of Jardines’ home, the only question is
whether he had given his leave (even implicitly) for them
to do so. He had not.
   “A license may be implied from the habits of the coun-
try,” notwithstanding the “strict rule of the English com-
mon law as to entry upon a close.” McKee v. Gratz, 260
U. S. 127, 136 (1922) (Holmes, J.). We have accordingly
recognized that “the knocker on the front door is treated
as an invitation or license to attempt an entry, justifying
ingress to the home by solicitors, hawkers and peddlers
of all kinds.” Breard v. Alexandria, 341 U. S. 622, 626
(1951). This implicit license typically permits the visitor
to approach the home by the front path, knock promptly,
wait briefly to be received, and then (absent invitation to
linger longer) leave. Complying with the terms of that
traditional invitation does not require fine-grained legal
knowledge; it is generally managed without incident by
the Nation’s Girl Scouts and trick-or-treaters.2 Thus, a
police officer not armed with a warrant may approach a
home and knock, precisely because that is “no more than
any private citizen might do.” Kentucky v. King, 563 U. S.
——————
    2 With this much, the dissent seems to agree—it would inquire into

“ ‘the appearance of things,’ ” post, at 5 (opinion of ALITO, J.), what is
“typica[l]” for a visitor, ibid., what might cause “alarm” to a “resident of
the premises,” ibid., what is “expected” of “ordinary visitors,” ibid., and
what would be expected from a “ ‘reasonably respectful citizen,’ ” post, at
7. These are good questions. But their answers are incompatible with
the dissent’s outcome, which is presumably why the dissent does not
even try to argue that it would be customary, usual, reasonable, re-
spectful, ordinary, typical, nonalarming, etc., for a stranger to explore
the curtilage of the home with trained drug dogs.
                     Cite as: 569 U. S. ____ (2013)                     7

                          Opinion of the Court

___, ___ (2011) (slip op., at 16).
   But introducing a trained police dog to explore the area
around the home in hopes of discovering incriminating
evidence is something else. There is no customary invita-
tion to do that. An invitation to engage in canine forensic
investigation assuredly does not inhere in the very act of
hanging a knocker.3 To find a visitor knocking on the door
is routine (even if sometimes unwelcome); to spot that
same visitor exploring the front path with a metal detec-
tor, or marching his bloodhound into the garden before
saying hello and asking permission, would inspire most
of us to—well, call the police. The scope of a license—
express or implied—is limited not only to a particular area
but also to a specific purpose. Consent at a traffic stop to
an officer’s checking out an anonymous tip that there is a
body in the trunk does not permit the officer to rummage
through the trunk for narcotics. Here, the background
social norms that invite a visitor to the front door do not
invite him there to conduct a search.4
——————
   3 The dissent insists that our argument must rest upon “the particu-

lar instrument that Detective Bartelt used to detect the odor of mari-
juana”—the dog. Post, at 8. It is not the dog that is the problem, but the
behavior that here involved use of the dog. We think a typical person
would find it “ ‘a cause for great alarm’ ” (the kind of reaction the dis-
sent quite rightly relies upon to justify its no-night-visits rule, post,
at 5) to find a stranger snooping about his front porch with or without
a dog. The dissent would let the police do whatever they want by way
of gathering evidence so long as they stay on the base-path, to use a
baseball analogy—so long as they “stick to the path that is typically
used to approach a front door, such as a paved walkway.” Ibid. From
that vantage point they can presumably peer into the house through
binoculars with impunity. That is not the law, as even the State con-
cedes. See Tr. of Oral Arg. 6.
   4 The dissent argues, citing King, that “gathering evidence—even

damning evidence—is a lawful activity that falls within the scope of the
license to approach.” Post, at 7. That is a false generalization. What
King establishes is that it is not a Fourth Amendment search to ap-
proach the home in order to speak with the occupant, because all are
8                      FLORIDA v. JARDINES

                         Opinion of the Court

  The State points to our decisions holding that the sub-
jective intent of the officer is irrelevant. See Ashcroft v.
al-Kidd, 563 U. S. ___ (2011); Whren v. United States, 517
U. S. 806 (1996). But those cases merely hold that a stop
or search that is objectively reasonable is not vitiated by
the fact that the officer’s real reason for making the stop
or search has nothing to do with the validating reason.
Thus, the defendant will not be heard to complain that
although he was speeding the officer’s real reason for the
stop was racial harassment. See id., at 810, 813. Here,
however, the question before the court is precisely whether
the officer’s conduct was an objectively reasonable search.
As we have described, that depends upon whether the
officers had an implied license to enter the porch, which in
turn depends upon the purpose for which they entered.
Here, their behavior objectively reveals a purpose to con-
duct a search, which is not what anyone would think he
had license to do.
                              III
   The State argues that investigation by a forensic narcot-
ics dog by definition cannot implicate any legitimate pri-
vacy interest. The State cites for authority our decisions
in United States v. Place, 462 U. S. 696 (1983), United
States v. Jacobsen, 466 U. S. 109 (1984), and Illinois v.
Caballes, 543 U. S. 405 (2005), which held, respectively,
that canine inspection of luggage in an airport, chemical
testing of a substance that had fallen from a parcel in
transit, and canine inspection of an automobile during a
lawful traffic stop, do not violate the “reasonable expecta-
tion of privacy” described in Katz.

—————— 

invited to do that. The mere “purpose of discovering information,” post,
at 8, in the course of engaging in that permitted conduct does not cause
it to violate the Fourth Amendment. But no one is impliedly invited to
enter the protected premises of the home in order to do nothing but
conduct a search.
                 Cite as: 569 U. S. ____ (2013)            9

                     Opinion of the Court

   Just last Term, we considered an argument much like
this. Jones held that tracking an automobile’s where-
abouts using a physically-mounted GPS receiver is a Fourth
Amendment search. The Government argued that the
Katz standard “show[ed] that no search occurred,” as the
defendant had “no ‘reasonable expectation of privacy’ ” in
his whereabouts on the public roads, Jones, 565 U. S., at
___ (slip op., at 5)—a proposition with at least as much
support in our case law as the one the State marshals
here. See, e.g., United States v. Knotts, 460 U. S. 276, 278
(1983). But because the GPS receiver had been physically
mounted on the defendant’s automobile (thus intruding on
his “effects”), we held that tracking the vehicle’s move-
ments was a search: a person’s “Fourth Amendment rights
do not rise or fall with the Katz formulation.” Jones,
supra, at ___ (slip op., at 5). The Katz reasonable-
expectations test “has been added to, not substituted
for,” the traditional property-based understanding of the
Fourth Amendment, and so is unnecessary to consider
when the government gains evidence by physically intrud-
ing on constitutionally protected areas. Jones, supra, at
___ (slip op., at 8).
   Thus, we need not decide whether the officers’ investiga-
tion of Jardines’ home violated his expectation of privacy
under Katz. One virtue of the Fourth Amendment’s
property-rights baseline is that it keeps easy cases easy.
That the officers learned what they learned only by physi-
cally intruding on Jardines’ property to gather evidence is
enough to establish that a search occurred.
   For a related reason we find irrelevant the State’s ar-
gument (echoed by the dissent) that forensic dogs have
been commonly used by police for centuries. This argu-
ment is apparently directed to our holding in Kyllo v.
United States, 533 U. S. 27 (2001), that surveillance of
the home is a search where “the Government uses a device
that is not in general public use” to “explore details of the
10                 FLORIDA v. JARDINES

                     Opinion of the Court

home that would previously have been unknowable with-
out physical intrusion.” Id., at 40 (emphasis added). But
the implication of that statement (inclusio unius est exclu-
sio alterius) is that when the government uses a physical
intrusion to explore details of the home (including its
curtilage), the antiquity of the tools that they bring along
is irrelevant.
                      *    *    *
   The government’s use of trained police dogs to inves-
tigate the home and its immediate surroundings is a
“search” within the meaning of the Fourth Amendment.
The judgment of the Supreme Court of Florida is therefore
affirmed.
                                         It is so ordered.
                 Cite as: 569 U. S. ____ (2013)           1

                     KAGAN, J., concurring

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 11–564
                         _________________


    FLORIDA, PETITIONER v. JOELIS JARDINES
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       FLORIDA

                       [March 26, 2013]


   JUSTICE KAGAN, with whom JUSTICE GINSBURG and
JUSTICE SOTOMAYOR join, concurring.
   For me, a simple analogy clinches this case—and does
so on privacy as well as property grounds. A stranger
comes to the front door of your home carrying super-high-
powered binoculars. See ante, at 7, n. 3. He doesn’t knock
or say hello. Instead, he stands on the porch and uses the
binoculars to peer through your windows, into your home’s
furthest corners. It doesn’t take long (the binoculars are
really very fine): In just a couple of minutes, his uncom-
mon behavior allows him to learn details of your life you
disclose to no one. Has your “visitor” trespassed on your
property, exceeding the license you have granted to mem-
bers of the public to, say, drop off the mail or distribute
campaign flyers? Yes, he has. And has he also invaded
your “reasonable expectation of privacy,” by nosing into
intimacies you sensibly thought protected from disclosure?
Katz v. United States, 389 U. S. 347, 360 (1967) (Harlan,
J., concurring). Yes, of course, he has done that too.
   That case is this case in every way that matters. Here,
police officers came to Joelis Jardines’ door with a super-
sensitive instrument, which they deployed to detect things
inside that they could not perceive unassisted. The equip-
ment they used was animal, not mineral. But contra the
dissent, see post, at 2 (opinion of ALITO, J.) (noting the
ubiquity of dogs in American households), that is of no
2                   FLORIDA v. JARDINES

                     KAGAN, J., concurring

significance in determining whether a search occurred.
Detective Bartelt’s dog was not your neighbor’s pet, come
to your porch on a leisurely stroll. As this Court discussed
earlier this Term, drug-detection dogs are highly trained
tools of law enforcement, geared to respond in distinctive
ways to specific scents so as to convey clear and reliable
information to their human partners. See Florida v.
Harris, 568 U. S. ___ (2013) (slip op. at 2–3, 7–8). They
are to the poodle down the street as high-powered binocu-
lars are to a piece of plain glass. Like the binoculars, a
drug-detection dog is a specialized device for discovering
objects not in plain view (or plain smell). And as in the
hypothetical above, that device was aimed here at a
home—the most private and inviolate (or so we expect) of
all the places and things the Fourth Amendment protects.
Was this activity a trespass? Yes, as the Court holds to-
day. Was it also an invasion of privacy? Yes, that as well.
   The Court today treats this case under a property ru-
bric; I write separately to note that I could just as happily
have decided it by looking to Jardines’ privacy interests. A
decision along those lines would have looked . . . well,
much like this one. It would have talked about “ ‘the right
of a man to retreat into his own home and there be free
from unreasonable governmental intrusion.’ ” Ante, at 4
(quoting Silverman v. United States, 365 U. S. 505, 511
(1961)). It would have insisted on maintaining the “prac-
tical value” of that right by preventing police officers from
standing in an adjacent space and “trawl[ing] for evidence
with impunity.” Ante, at 4. It would have explained that
“ ‘privacy expectations are most heightened’ ” in the home
and the surrounding area. Ante, at 4–5 (quoting Califor-
nia v. Ciraolo, 476 U. S. 207, 213 (1986)). And it would
have determined that police officers invade those shared
expectations when they use trained canine assistants to
reveal within the confines of a home what they could not
otherwise have found there. See ante, at 6–7, and nn. 2–3.
                      Cite as: 569 U. S. ____ (2013)                      3

                          KAGAN, J., concurring

  It is not surprising that in a case involving a search of a
home, property concepts and privacy concepts should so
align. The law of property “naturally enough influence[s]”
our “shared social expectations” of what places should be
free from governmental incursions. Georgia v. Randolph,
547 U. S. 103, 111 (2006); see Rakas v. Illinois, 439 U. S.
128, 143, n. 12 (1978). And so the sentiment “my home is
my own,” while originating in property law, now also
denotes a common understanding—extending even beyond
that law’s formal protections—about an especially private
sphere. Jardines’ home was his property; it was also his
most intimate and familiar space. The analysis proceed-
ing from each of those facts, as today’s decision reveals,
runs mostly along the same path.
  I can think of only one divergence: If we had decided
this case on privacy grounds, we would have realized that
Kyllo v. United States, 533 U. S. 27 (2001), already re-
solved it.1 The Kyllo Court held that police officers con-
ducted a search when they used a thermal-imaging device
to detect heat emanating from a private home, even
though they committed no trespass. Highlighting our
intention to draw both a “firm” and a “bright” line at “the
entrance to the house,” id., at 40, we announced the fol-
lowing rule:
     “Where, as here, the Government uses a device that is
     not in general public use, to explore details of the
     home that would previously have been unknowable
——————
   1 The dissent claims, alternatively, that Illinois v. Caballes, 543 U. S.

405, 409–410 (2005), controls this case (or nearly does). See post, at 9,
11. But Caballes concerned a drug-detection dog’s sniff of an automo-
bile during a traffic stop. See also Florida v. Harris, 568 U. S. ___
(2013). And we have held, over and over again, that people’s expecta-
tions of privacy are much lower in their cars than in their homes. See,
e.g., Arizona v. Gant, 556 U. S. 332, 345 (2009); Wyoming v. Houghton,
526 U. S. 295, 303 (1999); New York v. Class, 475 U. S. 106, 115 (1986);
Cardwell v. Lewis, 417 U. S. 583, 590–591 (1974) (plurality opinion).
4                      FLORIDA v. JARDINES

                         KAGAN, J., concurring

       without physical intrusion, the surveillance is a
       ‘search’ and is presumptively unreasonable without a
       warrant.” Ibid.
That “firm” and “bright” rule governs this case: The police
officers here conducted a search because they used a
“device . . . not in general public use” (a trained drug-
detection dog) to “explore details of the home” (the pres-
ence of certain substances) that they would not otherwise
have discovered without entering the premises.
   And again, the dissent’s argument that the device is just
a dog cannot change the equation. As Kyllo made clear,
the “sense-enhancing” tool at issue may be “crude” or
“sophisticated,” may be old or new (drug-detection dogs
actually go back not “12,000 years” or “centuries,” post, at
2, 8, 12, but only a few decades), may be either smaller or
bigger than a breadbox; still, “at least where (as here)” the
device is not “in general public use,” training it on a home
violates our “minimal expectation of privacy”—an expecta-
tion “that exists, and that is acknowledged to be reasona-
ble.” 533 U. S., at 34, 36.2 That does not mean the device
——————
    2 The
        dissent’s other principal reason for concluding that no violation
of privacy occurred in this case—that police officers themselves might
detect an aroma wafting from a house—works no better. If officers can
smell drugs coming from a house, they can use that information; a
human sniff is not a search, we can all agree. But it does not follow
that a person loses his expectation of privacy in the many scents within
his home that (his own nose capably tells him) are not usually detecti-
ble by humans standing outside. And indeed, Kyllo already decided as
much. In response to an identical argument from the dissent in that
case, see 533 U. S., at 43 (Stevens, J., dissenting) (noting that humans
can sometimes detect “heat emanating from a building”), the Kyllo
Court stated: “The dissent’s comparison of the thermal imaging to
various circumstances in which outside observers might be able to
perceive, without technology, the heat of the home . . . is quite irrele-
vant. The fact that equivalent information could sometimes be ob-
tained by other means does not make lawful the use of means that
violate the Fourth Amendment. . . . In any event, [at the time in
question,] no outside observer could have discerned the relative heat of
                     Cite as: 569 U. S. ____ (2013)          5

                         KAGAN, J., concurring

is off-limits, as the dissent implies, see post, at 11–12; it
just means police officers cannot use it to examine a home
without a warrant or exigent circumstance. See Brigham
City v. Stuart, 547 U. S. 398, 403–404 (2006) (describing
exigencies allowing the warrantless search of a home).
   With these further thoughts, suggesting that a focus on
Jardines’ privacy interests would make an “easy cas[e]
easy” twice over, ante, at 9, I join the Court’s opinion in
full.




—————— 

Kyllo’s home without thermal imaging.” Id., at 35, n. 2. 

                 Cite as: 569 U. S. ____ (2013)           1

                     ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 11–564
                         _________________


    FLORIDA, PETITIONER v. JOELIS JARDINES
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       FLORIDA

                       [March 26, 2013]


  JUSTICE ALITO, with whom THE CHIEF JUSTICE,         JUS-
TICE KENNEDY, and JUSTICE BREYER join, dissenting.
   The Court’s decision in this important Fourth Amend-
ment case is based on a putative rule of trespass law that
is nowhere to be found in the annals of Anglo-American
jurisprudence.
   The law of trespass generally gives members of the
public a license to use a walkway to approach the front
door of a house and to remain there for a brief time. This
license is not limited to persons who intend to speak to an
occupant or who actually do so. (Mail carriers and persons
delivering packages and flyers are examples of individuals
who may lawfully approach a front door without intending
to converse.) Nor is the license restricted to categories
of visitors whom an occupant of the dwelling is likely to
welcome; as the Court acknowledges, this license applies
even to “solicitors, hawkers and peddlers of all kinds.”
Ante, at 6 (internal quotation marks omitted). And the
license even extends to police officers who wish to gather
evidence against an occupant (by asking potentially in-
criminating questions).
   According to the Court, however, the police officer in
this case, Detective Bartelt, committed a trespass because
he was accompanied during his otherwise lawful visit to
the front door of respondent’s house by his dog, Franky.
Where is the authority evidencing such a rule? Dogs have
2                     FLORIDA v. JARDINES

                        ALITO, J., dissenting

been domesticated for about 12,000 years;1 they were
ubiquitous in both this country and Britain at the time of
the adoption of the Fourth Amendment;2 and their acute
sense of smell has been used in law enforcement for centu-
ries.3 Yet the Court has been unable to find a single
case—from the United States or any other common-law
nation—that supports the rule on which its decision is
based. Thus, trespass law provides no support for the
Court’s holding today.
  The Court’s decision is also inconsistent with the
reasonable-expectations-of-privacy test that the Court
adopted in Katz v. United States, 389 U. S. 347 (1967). A
reasonable person understands that odors emanating from a
house may be detected from locations that are open to the
public, and a reasonable person will not count on the
strength of those odors remaining within the range that,
while detectible by a dog, cannot be smelled by a human.
  For these reasons, I would hold that no search within
the meaning of the Fourth Amendment took place in this
case, and I would reverse the decision below.
                             I
   The opinion of the Court may leave a reader with the
mistaken impression that Detective Bartelt and Franky
remained on respondent’s property for a prolonged period
of time and conducted a far-flung exploration of the front
yard. See ante, at 4 (“trawl for evidence with impunity”),
7 (“marching his bloodhound into the garden”). But that
is not what happened.
   Detective Bartelt and Franky approached the front door
via the driveway and a paved path—the route that any
——————
  1 See, e.g., Sloane, Dogs in War, Police Work and on Patrol, 46 J.

Crim. L., C. & P. S. 385 (1955–1956) (hereinafter Sloane).
  2 M. Derr, A Dog’s History of America 68–92 (2004); K. Olsen, Daily

Life in 18th-Century England 32–33 (1999).
  3 Sloane 388–389.
                    Cite as: 569 U. S. ____ (2013)                   3

                         ALITO, J., dissenting

visitor would customarily use4—and Franky was on the
kind of leash that any dog owner might employ.5 As
Franky approached the door, he started to track an air-
borne odor. He held his head high and began “bracketing”
the area (pacing back and forth) in order to determine the
strongest source of the smell. App. 95–96. Detective
Bartelt knew “the minute [he] observed” this behavior that
Franky had detected drugs. Id., at 95. Upon locating the
odor’s strongest source, Franky sat at the base of the front
door, and at this point, Detective Bartelt and Franky im-
mediately returned to their patrol car. Id., at 98.
  A critical fact that the Court omits is that, as respond-
ent’s counsel explained at oral argument, this entire
process—walking down the driveway and front path to the
front door, waiting for Franky to find the strongest source
of the odor, and walking back to the car—took approxi-
mately a minute or two. Tr. of Oral Arg. 57–58. Thus, the
amount of time that Franky and the detective remained
at the front porch was even less. The Court also fails to
mention that, while Detective Bartelt apparently did not
personally smell the odor of marijuana coming from the
house, another officer who subsequently stood on the front
porch, Detective Pedraja, did notice that smell and was
able to identify it. App. 81.
                             II
  The Court concludes that the conduct in this case was a
search because Detective Bartelt exceeded the boundaries
of the license to approach the house that is recognized by

——————
  4 See App. 94; App. to Brief for Respondent 1A (depiction of respond-

ent’s home).
  5 The Court notes that Franky was on a 6-foot leash, but such a

leash is standard equipment for ordinary dog owners. See, e.g.,
J. Stregowski, Four Dog Leash Varieties, http://dogs.about.com/od/
toyssupplies/tp/Dog-Leashes.htm (all Internet materials as visited Mar.
21, 2013, and available in Clerk of Court’s case file).
4                  FLORIDA v. JARDINES

                     ALITO, J., dissenting

the law of trespass, but the Court’s interpretation of the
scope of that license is unfounded.
                              A
   It is said that members of the public may lawfully pro-
ceed along a walkway leading to the front door of a house
because custom grants them a license to do so. Breard v.
Alexandria, 341 U. S. 622, 626 (1951); Lakin v. Ames, 64
Mass. 198, 220 (1852); J. Bishop, Commentaries on the
Non-Contract Law §823, p. 378 (1889). This rule encom-
passes categories of visitors whom most homeowners
almost certainly wish to allow to approach their front
doors—friends, relatives, mail carriers, persons making
deliveries. But it also reaches categories of visitors who
are less universally welcome—“solicitors,” “hawkers,”
“peddlers,” and the like. The law might attempt to draw
fine lines between categories of welcome and unwelcome
visitors, distinguishing, for example, between tolerable
and intolerable door-to-door peddlers (Girl Scouts selling
cookies versus adults selling aluminum siding) or be-
tween police officers on agreeable and disagreeable mis-
sions (gathering information about a bothersome neighbor
versus asking potentially incriminating questions). But
the law of trespass has not attempted such a difficult
taxonomy. See Desnick v. American Broadcasting Cos., 44
F. 3d 1345, 1351 (CA7 1995) (“[C]onsent to an entry is
often given legal effect even though the entrant has inten-
tions that if known to the owner of the property would
cause him for perfectly understandable and generally
ethical or at least lawful reasons to revoke his consent”);
cf. Skinner v. Ogallala Public School Dist., 262 Neb. 387,
402, 631 N. W. 2d 510, 525 (2001) (“[I]n order to determine
if a business invitation is implied, the inquiry is not a
subjective assessment of why the visitor chose to visit the
premises in a particular instance”); Crown Cork & Seal
Co. v. Kane, 213 Md. 152, 159, 131 A. 2d 470, 473–474
                 Cite as: 569 U. S. ____ (2013)            5

                     ALITO, J., dissenting

(1957) (noting that “there are many cases in which an
invitation has been implied from circumstances, such as
custom,” and that this test is “objective in that it stresses
custom and the appearance of things” as opposed to “the
undisclosed intention of the visitor”).
   Of course, this license has certain spatial and temporal
limits. A visitor must stick to the path that is typically
used to approach a front door, such as a paved walkway.
A visitor cannot traipse through the garden, meander into
the backyard, or take other circuitous detours that veer
from the pathway that a visitor would customarily use.
See, e.g., Robinson v. Virginia, 47 Va. App. 533, 549–550,
625 S. E. 2d 651, 659 (2006) (en banc); United States v.
Wells, 648 F. 3d 671, 679–680 (CA8 2011) (police exceeded
scope of their implied invitation when they bypassed the
front door and proceeded directly to the back yard); State
v. Harris, 919 S. W. 2d 619, 624 (Tenn. Crim. App. 1995)
(“Any substantial and unreasonable departure from an
area where the public is impliedly invited exceeds the
scope of the implied invitation . . . ” (internal quotation
marks and brackets omitted)); 1 W. LaFave, Search and
Seizure §2.3(c), p. 578 (2004) (hereinafter LaFave); id.,
§2.3(f), at 600–603 (“[W]hen the police come on to private
property to conduct an investigation or for some other
legitimate purpose and restrict their movements to places
visitors could be expected to go (e.g., walkways, drive-
ways, porches), observations made from such vantage points
are not covered by the Fourth Amendment” (footnotes
omitted)).
   Nor, as a general matter, may a visitor come to the front
door in the middle of the night without an express invita-
tion. See State v. Cada, 129 Idaho 224, 233, 923 P. 2d 469,
478 (App. 1996) (“Furtive intrusion late at night or in the
predawn hours is not conduct that is expected from ordi-
nary visitors. Indeed, if observed by a resident of the
premises, it could be a cause for great alarm”).
6                  FLORIDA v. JARDINES

                     ALITO, J., dissenting

   Similarly, a visitor may not linger at the front door for
an extended period. See 9 So. 3d 1, 11 (Fla. App. 2008)
(case below) (Cope, J., concurring in part and dissenting in
part) (“[T]here is no such thing as squatter’s rights on a
front porch. A stranger may not plop down uninvited to
spend the afternoon in the front porch rocking chair, or
throw down a sleeping bag to spend the night, or lurk on
the front porch, looking in the windows”). The license is
limited to the amount of time it would customarily take to
approach the door, pause long enough to see if someone is
home, and (if not expressly invited to stay longer), leave.
   As I understand the law of trespass and the scope of the
implied license, a visitor who adheres to these limitations
is not necessarily required to ring the doorbell, knock on
the door, or attempt to speak with an occupant. For ex-
ample, mail carriers, persons making deliveries, and in-
dividuals distributing flyers may leave the items they
are carrying and depart without making any attempt to
converse. A pedestrian or motorist looking for a particular
address may walk up to a front door in order to check a
house number that is hard to see from the sidewalk or
road. A neighbor who knows that the residents are away
may approach the door to retrieve an accumulation of
newspapers that might signal to a potential burglar that
the house is unoccupied.
   As the majority acknowledges, this implied license to
approach the front door extends to the police. See ante, at
6. As we recognized in Kentucky v. King, 563 U. S. ___
(2011), police officers do not engage in a search when they
approach the front door of a residence and seek to engage
in what is termed a “knock and talk,” i.e., knocking on the
door and seeking to speak to an occupant for the purpose
of gathering evidence. See id., at ___ (slip op., at 16)
(“When law enforcement officers who are not armed with a
warrant knock on a door, they do no more than any pri-
vate citizen might do”). See also 1 LaFave §2.3(e), at 592
                  Cite as: 569 U. S. ____ (2013)             7

                      ALITO, J., dissenting

(“It is not objectionable for an officer to come upon that
part of the property which has been opened to public
common use” (internal quotation marks omitted)). Even
when the objective of a “knock and talk” is to obtain evi-
dence that will lead to the homeowner’s arrest and prose-
cution, the license to approach still applies. In other
words, gathering evidence—even damning evidence—is a
lawful activity that falls within the scope of the license to
approach. And when officers walk up to the front door of a
house, they are permitted to see, hear, and smell whatever
can be detected from a lawful vantage point. California v.
Ciraolo, 476 U. S. 207, 213 (1986) (“The Fourth Amend-
ment protection of the home has never been extended to
require law enforcement officers to shield their eyes when
passing by a home on public thoroughfares”); Cada, supra,
at 232, 923 P. 2d, at 477 (“[P]olice officers restricting their
activity to [areas to which the public is impliedly invited]
are permitted the same intrusion and the same level
of observation as would be expected from a reasonably
respectful citizen” (internal quotation marks omitted)); 1
LaFave §§2.2(a), 2.3(c), at 450–452, 572–577.
                             B
  Detective Bartelt did not exceed the scope of the license
to approach respondent’s front door. He adhered to the
customary path; he did not approach in the middle of the
night; and he remained at the front door for only a very
short period (less than a minute or two).
  The Court concludes that Detective Bartelt went too far
because he had the “objectiv[e] . . . purpose to conduct a
search.” Ante, at 8 (emphasis added). What this means, I
take it, is that anyone aware of what Detective Bartelt did
would infer that his subjective purpose was to gather
evidence. But if this is the Court’s point, then a standard
“knock and talk” and most other police visits would like-
wise constitute searches. With the exception of visits to
8                   FLORIDA v. JARDINES

                      ALITO, J., dissenting

serve warrants or civil process, police almost always ap-
proach homes with a purpose of discovering information.
That is certainly the objective of a “knock and talk.” The
Court offers no meaningful way of distinguishing the
“objective purpose” of a “knock and talk” from the “objec-
tive purpose” of Detective Bartelt’s conduct here.
   The Court contends that a “knock and talk” is different
because it involves talking, and “all are invited” to do that.
Ante, at 7–8, n. 4 (emphasis deleted). But a police officer
who approaches the front door of a house in accordance
with the limitations already discussed may gather evi-
dence by means other than talking. The officer may ob-
serve items in plain view and smell odors coming from the
house. Ciraolo, supra, at 213; Cada, 129 Idaho, at 232,
923 P. 2d, at 477; 1 LaFave §§2.2(a), 2.3(c), at 450–452,
572–577. So the Court’s “objective purpose” argument
cannot stand.
   What the Court must fall back on, then, is the particular
instrument that Detective Bartelt used to detect the odor
of marijuana, namely, his dog. But in the entire body of
common-law decisions, the Court has not found a single
case holding that a visitor to the front door of a home
commits a trespass if the visitor is accompanied by a dog
on a leash. On the contrary, the common law allowed even
unleashed dogs to wander on private property without
committing a trespass. G. Williams, Liability for Animals
136–146 (1939); J. Ingham, A Treatise on Property in
Animals Wild and Domestic and the Rights and Respon-
sibilities Arising Therefrom 277–278 (1900).           Cf. B.
Markesinis & S. Deakin, Tort Law 511 (4th ed. 1999).
   The Court responds that “[i]t is not the dog that is the
problem, but the behavior that here involved use of the
dog.” Ante, at 7, n. 3. But where is the support in the law
of trespass for this proposition? Dogs’ keen sense of smell
has been used in law enforcement for centuries. The
antiquity of this practice is evidenced by a Scottish law
                  Cite as: 569 U. S. ____ (2013)            9

                      ALITO, J., dissenting

from 1318 that made it a crime to “disturb a tracking dog
or the men coming with it for pursuing thieves or seizing
malefactors.” K. Brown et al., The Records of the Parlia-
ments of Scotland to 1707, (St Andrews, 2007–2013),
online at http://www.rps.ac.uk/mss/1318/9. If bringing a
tracking dog to the front door of a home constituted a
trespass, one would expect at least one case to have arisen
during the past 800 years. But the Court has found none.
  For these reasons, the real law of trespass provides no
support for the Court’s holding today. While the Court
claims that its reasoning has “ancient and durable
roots,” ante, at 4, its trespass rule is really a newly struck
counterfeit.
                              III
   The concurring opinion attempts to provide an alterna-
tive ground for today’s decision, namely, that Detective
Bartelt’s conduct violated respondent’s reasonable expec-
tations of privacy. But we have already rejected a very
similar, if not identical argument, see Illinois v. Caballes,
543 U. S. 405, 409–410 (2005), and in any event I see no
basis for concluding that the occupants of a dwelling have
a reasonable expectation of privacy in odors that emanate
from the dwelling and reach spots where members of the
public may lawfully stand.
   It is clear that the occupant of a house has no reasona-
ble expectation of privacy with respect to odors that can be
smelled by human beings who are standing in such places.
See United States v. Johns, 469 U. S. 478, 482 (1985)
(“After the officers came closer and detected the distinct
odor of marihuana, they had probable cause to believe
that the vehicles contained contraband”); United States
v. Ventresca, 380 U. S. 102, 111 (1965) (scent of ferment-
ing mash supported probable cause for warrant); United
States v. Johnston, 497 F. 2d 397, 398 (CA9 1974) (there
is no “reasonable expectation of privacy from drug agents
10                    FLORIDA v. JARDINES

                         ALITO, J., dissenting

with inquisitive nostrils”). And I would not draw a line
between odors that can be smelled by humans and those
that are detectible only by dogs.
   Consider the situation from the point of view of the
occupant of a building in which marijuana is grown or
methamphetamine is manufactured. Would such an oc-
cupant reason as follows? “I know that odors may ema-
nate from my building and that atmospheric conditions,
such as the force and direction of the wind, may affect the
strength of those odors when they reach a spot where
members of the public may lawfully stand. I also know
that some people have a much more acute sense of smell
than others,6 and I have no idea who might be standing in
one of the spots in question when the odors from my house
reach that location. In addition, I know that odors coming
from my building, when they reach these locations, may be
strong enough to be detected by a dog. But I am confident
that they will be so faint that they cannot be smelled by
any human being.” Such a finely tuned expectation would
be entirely unrealistic, and I see no evidence that society
is prepared to recognize it as reasonable.
   In an attempt to show that respondent had a reasonable
expectation of privacy in the odor of marijuana wafting
from his house, the concurrence argues that this case is
just like Kyllo v. United States, 533 U. S. 27 (2001), which
held that police officers conducted a search when they
used a thermal imaging device to detect heat emanating
from a house. Ante, at 3–4 (opinion of KAGAN, J.). This
Court, however, has already rejected the argument that
——————
  6 Some humans naturally have a much more acute sense of smell

than others, and humans can be trained to detect and distinguish odors
that could not be detected without such training. See E. Hancock, A
Primer on Smell, http://www.jhu.edu/jhumag/996web/smell.html. Some
individuals employed in the perfume and wine industries, for example,
have an amazingly acute sense of smell. Ibid.
                 Cite as: 569 U. S. ____ (2013)           11

                     ALITO, J., dissenting

the use of a drug-sniffing dog is the same as the use of a
thermal imaging device. See Caballes, 543 U. S., at 409–
410. The very argument now advanced by the concurrence
appears in Justice Souter’s Caballes dissent. See id., at
413, and n. 3. But the Court was not persuaded.
   Contrary to the interpretation propounded by the con-
currence, Kyllo is best understood as a decision about the
use of new technology. The Kyllo Court focused on the fact
that the thermal imaging device was a form of “sense-
enhancing technology” that was “not in general public
use,” and it expressed concern that citizens would be “at
the mercy of advancing technology” if its use was not
restricted. 533 U. S., at 34–35. A dog, however, is not a
new form of “technology or a “device.” And, as noted, the
use of dogs’ acute sense of smell in law enforcement dates
back many centuries.
   The concurrence suggests that a Kyllo-based decision
would be “much like” the actual decision of the Court, but
that is simply not so. The holding of the Court is based on
what the Court sees as a “ ‘physical intrusion of a constitu-
tionally protected area.’ ” Ante, at 3 (quoting United States
v. Knotts, 460 U. S. 276, 286 (1983) (Brennan, J., concur-
ring in judgment)). As a result, it does not apply when a
dog alerts while on a public sidewalk or street or in the
corridor of a building to which the dog and handler have
been lawfully admitted.
   The concurrence’s Kyllo-based approach would have a
much wider reach. When the police used the thermal
imaging device in Kyllo, they were on a public street, 533
U. S., at 29, and “committed no trespass.” Ante, at 3.
Therefore, if a dog’s nose is just like a thermal imaging
device for Fourth Amendment purposes, a search would
occur if a dog alerted while on a public sidewalk or in the
corridor of an apartment building. And the same would be
true if the dog was trained to sniff, not for marijuana, but
for more dangerous quarry, such as explosives or for a
12                 FLORIDA v. JARDINES

                    ALITO, J., dissenting

violent fugitive or kidnaped child. I see no ground for
hampering legitimate law enforcement in this way.
                            IV
  The conduct of the police officer in this case did not
constitute a trespass and did not violate respondent’s
reasonable expectations of privacy. I would hold that this
conduct was not a search, and I therefore respectfully
dissent.

```

---

## GROUP: _overhaul2/lake/cases/Florida v. Jimeno.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. Jimeno"
type: case
citation: "500 U.S. 248 (1991)"
parallel_cite: "111 S. Ct. 1801; 114 L. Ed. 2d 297"
neutral_cite: 1991 U.S. LEXIS 2910
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-05-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-05-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Jimeno
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112595/florida-v-jimeno/"
  cluster_id: 112595
  opinion_id: 9432279
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Progeny / Refinement"
related: ["[[Schneckloth v. Bustamonte]]", "[[Illinois v. Rodriguez]]", "[[United States v. Ross]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "scope-of-consent", "containers", "automobile"]
holding: "The SCOPE of a consent search is measured by OBJECTIVE REASONABLENESS — what the typical reasonable person would have understood by the…"
lake:
  record_id: Florida v. Jimeno
  status: verified
  projected_at: 2026-07-06
---

# Florida v. Jimeno

*500 U.S. 248 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Dade County officer overheard Enio Jimeno apparently arranging a drug deal on a pay phone and followed his car. After Jimeno committed a traffic violation, the officer stopped him, said he believed Jimeno was carrying narcotics, and asked to search the car; Jimeno consented. Inside, the officer opened a folded brown paper bag on the floorboard and found a kilogram of cocaine. Jimeno moved to suppress, arguing his consent to search the car did not extend to the closed bag.

## Issue
Whether a suspect's general consent to search his car for narcotics authorizes an officer to open a closed container found inside the car that might hold the drugs.

## Rule
Yes — the scope of consent is measured objectively. "The standard for measuring the scope of a suspect's consent under the Fourth Amendment is that of 'objective' reasonableness—what would the typical reasonable person have understood by the exchange between the officer and the suspect?" — 500 U.S. at 251. ^pin-251

And "[t]he scope of a search is generally defined by its expressed object." — *Id.* ^pin-251a

A general consent to search a car for drugs therefore reasonably extends to containers inside the car that could hold drugs.

## Application
Jimeno gave a general, unlimited consent to search the car after the officer told him he was looking for narcotics. A typical reasonable person would understand that authorization to include a paper bag on the floorboard where drugs might be carried — so it was objectively reasonable for the officer to open the bag, and the search did not exceed the consent given.

## Conclusion
The officer's opening of the paper bag was within the scope of Jimeno's general consent; the Florida Supreme Court's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Jimeno*'s objective-reasonableness scope standard builds on the voluntary-consent framework of [[Schneckloth v. Bustamonte]] and the expressed-object principle of [[United States v. Ross]].

## Appears on
- [[Consent Searches]] — *Key — Progeny / Refinement*

## Sources
- *Florida v. Jimeno*, 500 U.S. 248 (1991) — https://www.courtlistener.com/opinion/112595/florida-v-jimeno/ — pinpoint: 251.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d630f3e97b83df43", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. Jimeno"}, "payload": {"all": [{"cite": "500 U.S. 248", "page": "248", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "500"}, {"cite": "111 S. Ct. 1801", "page": "1801", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "111"}, {"cite": "114 L. Ed. 2d 297", "page": "297", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "114"}, {"cite": "1991 U.S. LEXIS 2910", "page": "2910", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1991"}], "display": "500 U.S. 248", "official": {"cite": "500 U.S. 248", "page": "248", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "500"}, "official_selection_present": true, "record_id": "Florida v. Jimeno"}}
{"assertion_id": "29b03309673af1b5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-251a", "record_id": "Florida v. Jimeno"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-251a", "pinpoint_status": "slip-only", "quote": "[t]he scope of a search is generally defined by its expressed object.", "quote_fidelity": "mismatch", "record_id": "Florida v. Jimeno", "star_marker": null}}
{"assertion_id": "41ecbb48b6b41c5a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-251", "record_id": "Florida v. Jimeno"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-251", "pinpoint_status": "slip-only", "quote": "--- # Florida v. Jimeno *500 U.S. 248 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Dade County officer overheard Enio Jimeno apparently arranging a drug deal on a pay phone and followed his car. After Jimeno committed a traffic violation, the officer stopped him, said he believed Jimeno was carrying narcotics, and asked to search the car; Jimeno consented. Inside, the officer opened a folded brown paper bag on the floorboard and found a kilogram of cocaine. Jimeno moved to suppress, arguing his consent to search the car did not extend to the closed bag. ## Issue Whether a suspect's general consent to search his car for narcotics authorizes an officer to open a closed container found inside the car that might hold the drugs. ## Rule Yes — the scope of consent is measured objectively.", "quote_fidelity": "mismatch", "record_id": "Florida v. Jimeno", "star_marker": null}}
{"assertion_id": "1598161dfd7c8cad", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. Jimeno"}, "payload": {"as_of_content": "1991-05-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. Jimeno", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Florida v. Jimeno

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Jimeno",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Jimeno",
    "case_name_short": "Jimeno",
    "case_name_full": "FLORIDA v. JIMENO Et Al.",
    "input_case_name": "Florida v. Jimeno",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-05-23",
    "year": 1991,
    "docket": null,
    "cluster_id": 112595,
    "lead_opinion_id": 9432279,
    "sibling_ids": [
      112595,
      9432279,
      9432280
    ],
    "absolute_url": "/opinion/112595/florida-v-jimeno/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9107096,
        "score": 20,
        "case_name": "Florida v. Jimeno"
      },
      {
        "cluster_id": 9107095,
        "score": 20,
        "case_name": "Florida v. Jimeno"
      },
      {
        "cluster_id": 9105239,
        "score": 20,
        "case_name": "Florida v. Jimeno"
      },
      {
        "cluster_id": 9105238,
        "score": 20,
        "case_name": "Florida v. Jimeno"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "500 U.S. 248",
      "volume": "500",
      "reporter": "U.S.",
      "page": "248",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 1801",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 L. Ed. 2d 297",
        "volume": "114",
        "reporter": "L. Ed. 2d",
        "page": "297",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 2910",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2910",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "500 U.S. 248",
        "volume": "500",
        "reporter": "U.S.",
        "page": "248",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 1801",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1801",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 L. Ed. 2d 297",
        "volume": "114",
        "reporter": "L. Ed. 2d",
        "page": "297",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 2910",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "2910",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "500 U.S. 248",
    "official_selection": {
      "court_class": "scotus",
      "selected": "500 U.S. 248",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-251",
      "page": null,
      "quote": "--- # Florida v. Jimeno *500 U.S. 248 (1991)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Dade County officer overheard Enio Jimeno apparently arranging a drug deal on a pay phone and followed his car. After Jimeno committed a traffic violation, the officer stopped him, said he believed Jimeno was carrying narcotics, and asked to search the car; Jimeno consented. Inside, the officer opened a folded brown paper bag on the floorboard and found a kilogram of cocaine. Jimeno moved to suppress, arguing his consent to search the car did not extend to the closed bag. ## Issue Whether a suspect's general consent to search his car for narcotics authorizes an officer to open a closed container found inside the car that might hold the drugs. ## Rule Yes \u2014 the scope of consent is measured objectively.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-251a",
      "page": null,
      "quote": "[t]he scope of a search is generally defined by its expressed object.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-05-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Jimeno",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Florida v. Jimeno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Gutierrez",
          "cluster_id": 6240355,
          "cite": [
            "245 Cal. Rptr. 3d 143",
            "33 Cal. App. Supp. 5th 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane1_negative"
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
        "journal_ref": "Florida v. Jimeno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Matter of James C. Wollrab",
          "cluster_id": 4510606,
          "cite": [
            "2018 CO 64",
            "420 P.3d 960"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brian Thurman",
          "cluster_id": 4494862,
          "cite": [
            "889 F.3d 356"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane1_negative"
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
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
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
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muscarello v. United States",
          "cluster_id": 118224,
          "cite": [
            "141 L. Ed. 2d 111",
            "118 S. Ct. 1911",
            "524 U.S. 125",
            "1998 U.S. LEXIS 3879"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Valtierra v. State",
          "cluster_id": 1370428,
          "cite": [
            "310 S.W.3d 442",
            "2010 Tex. Crim. App. LEXIS 828",
            "2010 WL 1850384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. David Lee Rusher, United States of America v. Sarah Jean Shoemaker Rusher, A/K/A Sarah Anne Rusher, United States of America v. James Joseph Flannery, A/K/A James Joseph Fleming, A/K/A Richard J. Mutschler",
          "cluster_id": 584528,
          "cite": [
            "966 F.2d 868",
            "1992 U.S. App. LEXIS 12338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Alvarez",
          "cluster_id": 1160457,
          "cite": [
            "14 Cal. 4th 155",
            "926 P.2d 365",
            "96 Cal. Daily Op. Serv. 8805",
            "58 Cal. Rptr. 2d 385",
            "96 Daily Journal DAR 14567",
            "1996 Cal. LEXIS 6514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
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
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Tully",
          "cluster_id": 844166,
          "cite": [
            "54 Cal. 4th 952",
            "282 P.3d 173",
            "145 Cal. Rptr. 3d 146",
            "2012 WL 3064338",
            "2012 Cal. LEXIS 7247"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peterson v. City of Fort Worth, Tex.",
          "cluster_id": 69197,
          "cite": [
            "588 F.3d 838",
            "2009 U.S. App. LEXIS 25183",
            "2009 WL 3818826"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dunn",
          "cluster_id": 1131042,
          "cite": [
            "850 P.2d 1201",
            "208 Utah Adv. Rep. 100",
            "1993 Utah LEXIS 54",
            "1993 WL 79651"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
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
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
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
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
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
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Jay Hill and Malcolm Scott Hill",
          "cluster_id": 766585,
          "cite": [
            "195 F.3d 258",
            "1999 U.S. App. LEXIS 24597",
            "1999 WL 781810"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reedy v. Evanson",
          "cluster_id": 152023,
          "cite": [
            "615 F.3d 197",
            "2010 U.S. App. LEXIS 15974",
            "2010 WL 2991378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jaime Soto, Also Known as Leonel Guerra",
          "cluster_id": 602824,
          "cite": [
            "988 F.2d 1548",
            "1993 U.S. App. LEXIS 5415",
            "1993 WL 77475"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Scottie Ray Hurst",
          "cluster_id": 770650,
          "cite": [
            "228 F.3d 751",
            "2000 U.S. App. LEXIS 23606",
            "2000 WL 1363206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lanning v. City of Glens Falls",
          "cluster_id": 8443755,
          "cite": [
            "908 F.3d 19"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DuBose v. State",
          "cluster_id": 2468681,
          "cite": [
            "915 S.W.2d 493",
            "1996 Tex. Crim. App. LEXIS 17",
            "1996 WL 61148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gasho v. United States",
          "cluster_id": 7030706,
          "cite": [
            "39 F.3d 1420",
            "1994 WL 595370"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brigham",
          "cluster_id": 35972,
          "cite": [
            "382 F.3d 500",
            "2004 WL 1854552"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Pack",
          "cluster_id": 150729,
          "cite": [
            "612 F.3d 341",
            "2010 U.S. App. LEXIS 14562",
            "2010 WL 2777061"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Randall Lee Pals",
          "cluster_id": 4472392,
          "cite": [
            "805 N.W.2d 767",
            "2011 Iowa Sup. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Jimeno:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112595 OR 9432279 OR 9432280) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTIyOTcyODAwMDAwJnM9NDQ4NDc5MiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112595+OR+9432279+OR+9432280%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112595 OR 9432279 OR 9432280)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODUmcz01ODI1NjQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112595+OR+9432279+OR+9432280%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112595 OR 9432279 OR 9432280)",
        "reviewed": 67,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 67,
        "triage_read": 0,
        "triage_snippet_classified": 67
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112595 OR 9432279 OR 9432280)",
    "indexed_citing_opinions": 1450,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112595,
        "count": 1271,
        "count_source": "search"
      },
      {
        "opinion_id": 9432279,
        "count": 208,
        "count_source": "search"
      },
      {
        "opinion_id": 9432280,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2280,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-jimeno.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMDgzNzQmcz0xMDM3OTU4NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112595+OR+9432279+OR+9432280%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112595,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 110119,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 112412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 1095147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112595,
        "cited_id": 1707694,
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
    "date_created": "2026-07-05T04:05:42Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:06:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:06:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:10:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:06:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Jimeno

```
<opinion type="majority">
<author id="b303-7">Chief Justice Rehnquist</author>
<p id="AGn_">delivered the opinion of the Court.</p>
<p id="b303-8">In this case we decide whether a criminal suspect’s Fourth Amendment right to be free from unreasonable searches is violated when, after he gives a police officer permission to search his automobile, the officer opens a closed container found within the car that might reasonably hold the object of the search. We find that it is not. The Fourth Amendment is satisfied when, under the circumstances, it is objectively reasonable for the officer to believe that the scope of the suspect’s consent permitted him to open a particular container within the automobile.</p>
<p id="b303-9">This case began when a Dade County police officer, Frank Trujillo, overheard respondent, Enio Jimeno, arranging what appeared to be a drug transaction over a public telephone. Believing that Jimeno might be involved in illegal drug trafficking, Officer Trujillo followed his car. The officer observed respondents make a- right turn at a red light without stopping. He then pulled Jimeno over to the side of the road in order to issue him a traffic citation. Officer Trujillo told Jimeno that he had been stopped for committing a traffic infraction. The officer went on to say that he had reason to believe that Jimeno was carrying narcotics in his car, and asked permission to search the car. He explained that Jimeno did not have to consent to a search of the car. Jimeno stated that he had nothing to hide and gave Trujillo <page-number citation-index="1" label="250">*250</page-number>permission to search the automobile. After Jimeno’s spouse, respondent Luz Jimeno, stepped out of the car, Officer Trujillo went to the passenger side, opened the door, and saw a folded, brown paper bag on the floorboard. The officer picked up the bag, opened it, and found a kilogram of cocaine inside.</p>
<p id="b304-5">The Jimenos were charged with possession with intent to distribute cocaine in violation of Florida law. Before trial, they moved to suppress the cocaine found in the bag on the ground that Jimeno’s consent to search the car did not extend to the closed paper bag inside of the car. The trial court granted the motion. It found that although Jimeno “could have assumed that the officer would have searched the bag” at the time he gave his consent, his mere consent to search the car did not carry with it specific consent to open the bag and examine its contents. No. 88-23967 (Cir. Ct. Dade Cty., Fla., Mar. 21, 1989); App. to Pet. for Cert. A-6.</p>
<p id="b304-6">The Florida District Court of Appeal affirmed the trial court’s decision to suppress the evidence of the cocaine. <span class="citation multiple-matches"><a href="/c/So.%202d/550/1176/">550 So. 2d 1176</a></span> (Fla. 3d DCA 1989). In doing so, the court established a <em>per se </em>rule that “consent to a general search for narcotics does not extend to ‘sealed containers within the general area agreed to by the defendant.’” <em>Ibid. </em>The Florida Supreme Court affirmed, relying upon its decision in <em>State </em>v. <em>Wells, </em><span class="citation" data-id="1095147"><a href="/opinion/1095147/state-v-wells/" aria-description="Citation for case: State v. Wells">539 So. 2d 464</a></span> (1989), aff’d on other grounds, <span class="citation" data-id="9431971"><a href="/opinion/112412/florida-v-wells/" aria-description="Citation for case: Florida v. Wells">495 U. S. 1</a></span> (1990). <span class="citation" data-id="1707694"><a href="/opinion/1707694/state-v-jimeno/" aria-description="Citation for case: State v. Jimeno">564 So. 2d 1083</a></span> (1990). We granted cer-tiorari to determine whether consent to search a vehicle may extend to closed containers found inside the vehicle, <span class="citation multiple-matches"><a href="/c/U.%20S./498/997/">498 U. S. 997</a></span> (1990), and we now reverse the judgment of the Supreme Court of Florida.</p>
<p id="AY7">The touchstone of the Fourth Amendment is reasonableness. <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360</a></span> (1967). The Fourth Amendment does not proscribe all state-initiated searches and seizures; it merely proscribes those which are unreasonable. <em>Illinois </em>v. <em>Rodriguez, </em><span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/" aria-description="Citation for case: Illinois v. Rodriguez">497 U. S. 177</a></span> (1990). Thus, we have long approved consensual searches because it <page-number citation-index="1" label="251">*251</page-number>is no doubt reasonable for the police to conduct a search once they have been permitted to do so. <em>Schneckloth </em>v. <em>Bustamonte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#219" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 219</a></span> (1973). The standard for measuring the scope of a suspect’s consent under the Fourth Amendment is that of “objective” reasonableness—what would the typical reasonable person have understood by the exchange between the officer and the suspect? <em>Illinois </em>v. <span class="citation" data-id="9432101"><a href="/opinion/112475/illinois-v-rodriguez/#183" aria-description="Citation for case: Illinois v. Rodriguez"><em>Rodriguez, supra, </em>at 183-189</a></span>; <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#501" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 501-502</a></span> (1983) (opinion of White, J.); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#514" aria-description="Citation for case: Florida v. Royer"><em>id., </em>at 514</a></span> (Blackmun, J., dissenting). The question before us, then, is whether it is reasonable for an officer to consider a suspect’s general consent to a search of his car to include consent to examine a paper bag lying on the floor of the car. We think that it is.</p>
<p id="b305-5">The scope of a search is generally defined by its expressed object. <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">456 U. S. 798</a></span> (1982). In this case, the terms of the search’s authorization were simple. Respondent granted Officer Trujillo permission to search his car, and did not place any explicit limitation on the scope of the search. Trujillo had informed Jimeno that he believed Jimeno was carrying narcotics, and that he would be looking for narcotics in the car. We think that it was objectively reasonable for the police to conclude that the general consent to search respondents’ car included consent to search containers within that car which might bear drugs. A reasonable person may be expected to know that narcotics are generally carried in some form of a container. “Contraband goods rarely are strewn across the trunk or floor of a car.” <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#820" aria-description="Citation for case: United States v. Ross"><em>Id., </em>at 820</a></span>. The authorization to search in this case, therefore, extended beyond the surfaces of the car’s interior to the paper bag lying on the car’s floor.</p>
<p id="b305-6">The facts of this case are therefore different from those in <em>State </em>v. <em>Wells, supra, </em>on which the Supreme Court of Florida relied in affirming the supression order in this case. There the Supreme Court of Florida held that consent to search the trunk of a car did not include authorization to pry open a locked briefcase found inside the trunk. It is very likely <page-number citation-index="1" label="252">*252</page-number>unreasonable to think that a suspect, by consenting to the search of his trunk, has agreed to the breaking open of a locked briefcase within the-trunk, but it is otherwise with respect to a closed paper bag.</p>
<p id="b306-5">Respondents argue, and the Florida trial court agreed, that if the police wish to search closed containers within a car they must separately request permission to search each container. But we see no basis for adding this sort of superstructure to the Fourth Amendment’s basic test of objective reasonableness. Cf. <em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983). A suspect may of course delimit as he chooses the scope of the search to which he consents. But if his consent would reasonably be understood to extend to a particular container, the Fourth Amendment provides no grounds for requiring a more explicit authorization. “[T]he community has a real interest in encouraging consent, for the resulting search may yield necessary evidence for the solution and prosecution of crime, evidence that may insure that a wholly innocent person is not wrongly charged with a criminal offense.” <em>Schneckloth </em>v. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#243" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>Bustamonte, supra, </em>at 243</a></span>.</p>
<p id="b306-6">The judgment of the Supreme Court of Florida is accordingly reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b306-7">
<em>It is so ordered.</em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Florida v. Meyers.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. Meyers"
type: case
citation: "466 U.S. 380 (1984)"
parallel_cite: "104 S. Ct. 1852; 80 L. Ed. 2d 381; 52 U.S.L.W. 3774"
neutral_cite: 1984 U.S. LEXIS 66
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-04-23
docket: 83-1279
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Meyers
  varies_by_point: false
  scope_note: "Per curiam. Settled application of the automobile exception; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111157/florida-v-meyers/"
  cluster_id: 111157
  opinion_id: 9429577
  identity_checked: true
homes:
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Thomas]]", "[[Chambers v. Maroney]]", "[[Maryland v. Dyson]]"]
aliases: ["Florida v. Myers"]
tags: ["case", "fourth-amendment", "automobile-exception", "impound", "second-search", "no-exigency"]
holding: "A second warrantless search of an already-impounded automobile, conducted hours after the first, is valid under the automobile exception; immobilization in police custody does not defeat the exception."
lake:
  record_id: Florida v. Meyers
  status: verified
  projected_at: 2026-07-09
---

# Florida v. Meyers

*466 U.S. 380 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

> **Caption / identity note:** the official caption (and CourtListener) spell the respondent's name **"Meyers"** ("Florida v. Meyers, aka Weyers"). The ingest-queue spelling "Florida v. Myers" is carried as an `alias` so bare `[[Florida v. Myers]]` links resolve here (L6 identity correction; SR-5/N1 caption fix).

## Background
The respondent was arrested for sexual battery. Officers searched his car at the scene and seized items, then towed the car to a wrecker yard, where it was impounded in a locked, secure area. About eight hours later an officer returned to the compound and, without a warrant, searched the car a second time, seizing additional evidence. The Florida District Court of Appeal reversed the conviction, holding that although the first search was conceded valid, the second warrantless search violated the Fourth Amendment because impoundment had removed the car's mobility.

## Issue
Whether a second warrantless search of an automobile already lawfully impounded and immobilized in a police compound is valid under the automobile exception.

## Rule
Yes. The automobile exception is not defeated by the car's prior impoundment or by an earlier search: "In *Michigan* v. *Thomas*, 458 U. S. 259 (1982), we upheld a warrantless search of an automobile even though the automobile was in police custody and even though a prior inventory search had already been made. That ruling controls the disposition of this case." — 466 U.S. at 382. ^pin-382

The Court reiterated, quoting *[[Michigan v. Thomas|Thomas]]*, that "the justification to conduct such a warrantless search does not vanish once the car has been immobilized." — [*Id.*](https://www.courtlistener.com/opinion/111157/florida-v-meyers/#:~:text=the%20justification%20to%20conduct%20such) (quoting 458 U.S. at 261). ^pin-382a

## Application
The state appellate court's ground — that impoundment removed mobility and therefore required a warrant for the second search — was "clearly inconsistent" with *[[Michigan v. Thomas]]* and *[[Chambers v. Maroney]]*. Because the justification for the warrantless search did not disappear once the car was impounded, the second search of the secured vehicle was valid.

## Conclusion
Reversed (per curiam). A second warrantless search of an already-impounded car is permissible under the automobile exception; immobilization in police custody does not require a warrant.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Meyers* applies [[Michigan v. Thomas]] and [[Chambers v. Maroney]] and sits within the line the Court later distilled in [[Maryland v. Dyson]] (auto exception has no separate [[Exigent Circumstances and Hot Pursuit|exigency]] requirement).

## Appears on
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Florida v. Meyers*, 466 U.S. 380 (1984) — https://www.courtlistener.com/opinion/111157/florida-v-meyers/ — pinpoint: 382.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "0b248313775cce1f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. Meyers"}, "payload": {"all": [{"cite": "466 U.S. 380", "page": "380", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "466"}, {"cite": "104 S. Ct. 1852", "page": "1852", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "104"}, {"cite": "80 L. Ed. 2d 381", "page": "381", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "1984 U.S. LEXIS 66", "page": "66", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}, {"cite": "52 U.S.L.W. 3774", "page": "3774", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "52"}], "display": "466 U.S. 380", "official": {"cite": "466 U.S. 380", "page": "380", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "466"}, "official_selection_present": true, "record_id": "Florida v. Meyers"}}
{"assertion_id": "c3a43122b0915745", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-382", "record_id": "Florida v. Meyers"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-382", "pinpoint_status": "slip-only", "quote": "is carried as an `alias` so bare `[[Florida v. Myers]]` links resolve here (L6 identity correction; SR-5/N1 caption fix). ## Background The respondent was arrested for sexual battery. Officers searched his car at the scene and seized items, then towed the car to a wrecker yard, where it was impounded in a locked, secure area. About eight hours later an officer returned to the compound and, without a warrant, searched the car a second time, seizing additional evidence. The Florida District Court of Appeal reversed the conviction, holding that although the first search was conceded valid, the second warrantless search violated the Fourth Amendment because impoundment had removed the car's mobility. ## Issue Whether a second warrantless search of an automobile already lawfully impounded and immobilized in a police compound is valid under the automobile exception. ## Rule Yes. The automobile exception is not defeated by the car's prior impoundment or by an earlier search:", "quote_fidelity": "mismatch", "record_id": "Florida v. Meyers", "star_marker": null}}
{"assertion_id": "d219a2ca1c10974d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-382a", "record_id": "Florida v. Meyers"}, "payload": {"fragment": "#:~:text=the%20justification%20to%20conduct%20such", "page": null, "pin_id": "pin-382a", "pinpoint_status": "star-verified", "quote": "the justification to conduct such a warrantless search does not vanish once the car has been immobilized.", "quote_fidelity": "matched", "record_id": "Florida v. Meyers", "star_marker": "382"}}
{"assertion_id": "77bcb5ade947d619", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. Meyers"}, "payload": {"as_of_content": "1984-04-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. Meyers", "scope_note": "Per curiam. Settled application of the automobile exception; no negative treatment.", "varies_by_point": false}}
```

### lake record — Florida v. Meyers

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Meyers",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Meyers",
    "case_name_short": "Meyers",
    "case_name_full": "FLORIDA v. MEYERS, AKA WEYERS",
    "input_case_name": "Florida v. Meyers",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-04-23",
    "year": 1984,
    "docket": "83-1279",
    "cluster_id": 111157,
    "lead_opinion_id": 9429577,
    "sibling_ids": [
      111157,
      9429577,
      9429578
    ],
    "absolute_url": "/opinion/111157/florida-v-meyers/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9350297,
        "score": 20,
        "case_name": "Florida v. Meyers"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "466 U.S. 380",
      "volume": "466",
      "reporter": "U.S.",
      "page": "380",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 1852",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1852",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 381",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 3774",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "3774",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 66",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "466 U.S. 380",
        "volume": "466",
        "reporter": "U.S.",
        "page": "380",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 1852",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "1852",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 381",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "381",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 66",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "66",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 3774",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "3774",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "466 U.S. 380",
    "official_selection": {
      "court_class": "scotus",
      "selected": "466 U.S. 380",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-382",
      "page": null,
      "quote": "is carried as an `alias` so bare `[[Florida v. Myers]]` links resolve here (L6 identity correction; SR-5/N1 caption fix). ## Background The respondent was arrested for sexual battery. Officers searched his car at the scene and seized items, then towed the car to a wrecker yard, where it was impounded in a locked, secure area. About eight hours later an officer returned to the compound and, without a warrant, searched the car a second time, seizing additional evidence. The Florida District Court of Appeal reversed the conviction, holding that although the first search was conceded valid, the second warrantless search violated the Fourth Amendment because impoundment had removed the car's mobility. ## Issue Whether a second warrantless search of an automobile already lawfully impounded and immobilized in a police compound is valid under the automobile exception. ## Rule Yes. The automobile exception is not defeated by the car's prior impoundment or by an earlier search:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-382a",
      "page": null,
      "quote": "the justification to conduct such a warrantless search does not vanish once the car has been immobilized.",
      "star_marker": "382",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 3324,
      "fragment": "#:~:text=the%20justification%20to%20conduct%20such",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Meyers",
    "varies_by_point": false,
    "scope_note": "Per curiam. Settled application of the automobile exception; no negative treatment.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Florida v. Meyers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Colorado v. Connelly",
          "cluster_id": 111587,
          "cite": [
            "474 U.S. 1050",
            "106 S. Ct. 785",
            "88 L. Ed. 2d 763",
            "54 U.S.L.W. 3457",
            "1986 U.S. LEXIS 2291"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Adkins v. State",
          "cluster_id": 1487299,
          "cite": [
            "675 S.W.2d 604",
            "1984 Tex. App. LEXIS 5852"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "New Jersey v. T. L. O.",
          "cluster_id": 111268,
          "cite": [
            "468 U.S. 1214",
            "104 S. Ct. 3583",
            "82 L. Ed. 2d 881",
            "52 U.S.L.W. 3935",
            "1984 U.S. LEXIS 2821"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Delaware v. Van Arsdall",
          "cluster_id": 111625,
          "cite": [
            "89 L. Ed. 2d 674",
            "106 S. Ct. 1431",
            "475 U.S. 673",
            "1986 U.S. LEXIS 94",
            "20 Fed. R. Serv. 1",
            "54 U.S.L.W. 4347"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patton v. Yount",
          "cluster_id": 111228,
          "cite": [
            "81 L. Ed. 2d 847",
            "104 S. Ct. 2885",
            "467 U.S. 1025",
            "1984 U.S. LEXIS 125",
            "52 U.S.L.W. 4896"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kansas v. Marsh",
          "cluster_id": 145632,
          "cite": [
            "165 L. Ed. 2d 429",
            "126 S. Ct. 2516",
            "548 U.S. 163",
            "2006 U.S. LEXIS 5163"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Bruder",
          "cluster_id": 112152,
          "cite": [
            "102 L. Ed. 2d 172",
            "109 S. Ct. 205",
            "488 U.S. 9",
            "1988 U.S. LEXIS 4816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kansas v. Kansas",
          "cluster_id": 3170728,
          "cite": [
            "577 U.S. 108",
            "136 S. Ct. 633",
            "193 L. Ed. 2d 535",
            "2016 U.S. LEXIS 845",
            "84 U.S.L.W. 4037",
            "25 Fla. L. Weekly Fed. S 593"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James v. Arizona",
          "cluster_id": 111324,
          "cite": [
            "469 U.S. 990",
            "105 S. Ct. 398",
            "53 U.S.L.W. 3339",
            "83 L. Ed. 2d 332",
            "1984 U.S. LEXIS 4325"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bradford",
          "cluster_id": 166424,
          "cite": [
            "423 F.3d 1149",
            "2005 U.S. App. LEXIS 19776",
            "2005 WL 2225800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Billy G. Byers",
          "cluster_id": 439952,
          "cite": [
            "740 F.2d 1104",
            "239 U.S. App. D.C. 1",
            "15 Fed. R. Serv. 1857",
            "1984 U.S. App. LEXIS 20244"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
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
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Moore",
          "cluster_id": 2627094,
          "cite": [
            "154 P.3d 1",
            "283 Kan. 344",
            "2007 Kan. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Caldwell",
          "cluster_id": 4904976,
          "cite": [
            "7 F.4th 191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Estrada",
          "cluster_id": 44577,
          "cite": [
            "459 F.3d 627",
            "2006 WL 2256493"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jimmie Calvin Caves, United States of America v. Chloe Kathleen Gorman",
          "cluster_id": 532599,
          "cite": [
            "890 F.2d 87",
            "1989 U.S. App. LEXIS 17573",
            "1989 WL 139633"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nathan v. State",
          "cluster_id": 1425474,
          "cite": [
            "805 A.2d 1086",
            "370 Md. 648",
            "2002 Md. LEXIS 564"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. James",
          "cluster_id": 6015436,
          "cite": [
            "111 A.D.2d 254",
            "489 N.Y.S.2d 527",
            "1985 N.Y. App. Div. LEXIS 51383"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vazquez",
          "cluster_id": 171754,
          "cite": [
            "555 F.3d 923",
            "2009 U.S. App. LEXIS 2473",
            "2009 WL 311268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Meyers:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111157 OR 9429577 OR 9429578) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 78,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 78,
        "triage_read": 5,
        "triage_snippet_classified": 73
      },
      "lane2_top_cited": {
        "query": "cites:(111157 OR 9429577 OR 9429578)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMCZzPTE2NTg3OTYmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111157+OR+9429577+OR+9429578%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111157 OR 9429577 OR 9429578)",
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
    "complete_query": "cites:(111157 OR 9429577 OR 9429578)",
    "indexed_citing_opinions": 101,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111157,
        "count": 96,
        "count_source": "search"
      },
      {
        "opinion_id": 9429577,
        "count": 6,
        "count_source": "search"
      },
      {
        "opinion_id": 9429578,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 166,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-meyers.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjIxMjMxODkmcz0yMzc0Mjg1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111157+OR+9429577+OR+9429578%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111157,
        "cited_id": 105766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 108889,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 109207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110574,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110590,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110807,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 110954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 111022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 111045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 111048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 111051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 1087618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 1676210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111157,
        "cited_id": 1949968,
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
    "date_created": "2026-07-05T04:10:55Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:18:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Meyers

```
<opinion type="majority">
<author id="b440-11">Per Curiam.</author>
<p id="b440-12">Respondent was charged with sexual battery. At the time of his arrest, police officers searched his automobile and seized several items. The vehicle was then towed to Sunny’s Wrecker, where it was impounded in a locked, secure area. Approximately eight hours later, a police officer went to the compound and, without obtaining a warrant, searched the car for a second time. Additional evidence was seized. At the subsequent trial, the court denied respondent’s motion to suppress the evidence seized during the second search, and respondent was convicted.</p>
<p id="b440-13">On appeal, the Florida District Court of Appeal for the Fourth District reversed the conviction, holding that even <page-number citation-index="1" label="381">*381</page-number>though respondent conceded that the initial search of the automobile was valid, the second search violated the Fourth Amendment. <span class="citation" data-id="1676210"><a href="/opinion/1676210/meyers-v-state/" aria-description="Citation for case: Meyers v. State">432 So. 2d 97</a></span> (1983). The court concluded that <em>Chambers </em>v. <em>Maroney, </em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), in which this Court held that police officers who have probable cause to believe there is contraband inside an automobile that has been stopped on the road may search it without obtaining a warrant, was distinguishable, stating that “in this case the element of mobility was removed because [respondent’s] vehicle had been impounded.” <span class="citation" data-id="1676210"><a href="/opinion/1676210/meyers-v-state/#99" aria-description="Citation for case: Meyers v. State">432 So. 2d, at 99</a></span>. The Florida Supreme Court denied the State’s petition for discretionary review, and the State filed the present petition for certiorari. We reverse.<footnotemark>*</footnotemark></p>
<p id="b442-4"><page-number citation-index="1" label="382">*382</page-number>The District Court of Appeal either misunderstood or ignored our prior rulings with respect to the constitutionality of the warrantless search of an impounded automobile. In <em>Michigan </em>v. <em>Thomas, </em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">458 U. S. 259</a></span> (1982), we upheld a war-rantless search of an automobile even though the automobile was in police custody and even though a prior inventory search had already been made. That ruling controls the disposition of this case. In <em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">Thomas</a></span>, </em>we expressly rejected the argument accepted by the District Court of Appeal in the present case, noting that the search upheld in <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span> </em>was conducted “after [the automobile was] impounded and [was] in police custody” and emphasizing that “the justification to conduct such a warrantless search does not vanish once the car has been immobilized.” <span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/#261" aria-description="Citation for case: Michigan v. Thomas">458 U. S., at 261</a></span>. The District Court of Appeal’s ruling that the subsequent search in this case was invalid because the car had been impounded is clearly inconsistent with <em><span class="citation" data-id="110776"><a href="/opinion/110776/michigan-v-thomas/" aria-description="Citation for case: Michigan v. Thomas">Thomas</a></span> </em>and <em><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Chambers</a></span>. </em>The petition for certiorari is therefore granted, the judgment of the <page-number citation-index="1" label="383">*383</page-number>District Court of Appeal is reversed, and the case is remanded to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b443-5">
<em>It is so ordered.</em>
</p>
<footnote label="*">
<p id="b441-5">Even though the District Court of Appeal remanded the case for a new trial, its decision on the federal constitutional issue is reviewable at this time because if the State prevails at the trial, the issue will be mooted; and if the State loses, governing state law, <span class="citation no-link">Fla. Stat. § 924.07</span> (1981); <em>State </em>v. <em>Brown, </em><span class="citation" data-id="1949968"><a href="/opinion/1949968/state-v-brown/#536" aria-description="Citation for case: State v. Brown">330 So. 2d 535, 536</a></span> (Fla. App. 1976), will prohibit it from presenting the federal claim for review. In such circumstances, we have consistently held that “the decision below constitute^ a final judgment under <span class="citation no-link">28 U. S. C. § 1257</span>(3).” <em>California </em>v. <em>Stewart, </em>decided with <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#497" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 497, 498, n. 71</a></span> (1966). See <em>South Dakota </em>v. <em>Neville, </em><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#558" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 558, n. 6</a></span> (1983); <em>North Dakota Pharmacy Board </em>v. <em>Snyder’s Stores, </em><span class="citation" data-id="108889"><a href="/opinion/108889/north-dakota-state-board-of-pharmacy-v-snyders-drug-stores-inc/#159" aria-description="Citation for case: North Dakota State Board of Pharmacy v. Snyder&#x27;s Drug...">414 U. S. 156, 159-164</a></span> (1973). See also <em>Cox Broadcasting Corp. </em>v. <em>Cohn, </em><span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#481" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S. 469, 481</a></span> (1975).</p>
<p id="b441-6">Respondent contends that we should not review the issue raised by petitioner because “the appellate court reversed [respondent’s] conviction on two independent grounds, one of which (restricted cross-examination) petitioner does not contest.” Brief in Opposition 2. To the extent that this is an argument that the lower court’s judgment is unreviewable because it rests on adequate and independent state grounds, we reject it. First, it is highly questionable whether the District Court of Appeal would have reversed the conviction had it not reversed the trial court’s ruling on the suppression motion. The court did state that respondent’s cross-examination of the victim had been unduly restricted by the trial court. However, the court’s short discussion of this issue was introduced by the observation that “[s]ince the case must be remanded for a new trial we briefly mention another appellate point.” <span class="citation" data-id="1676210"><a href="/opinion/1676210/meyers-v-state/#99" aria-description="Citation for case: Meyers v. State">432 So. 2d, at 99</a></span>. This is hardly a clear indication <page-number citation-index="1" label="382">*382</page-number>that the cross-examination ruling provided an independent and adequate basis for reversal of the conviction. See <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1040" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032, 1040-1041</a></span> (1983).</p>
<p id="Aeb">Moreover, even if the cross-examination ruling did provide an independent state ground for reversal, we would still be empowered to review the constitutional issue raised by petitioner. The reason we cannot review a state-court judgment resting on adequate and independent state grounds is that “[w]e are not permitted to render an advisory opinion, and if the same judgment would be rendered by the state court after we corrected its views of federal laws, our review could amount to nothing more than an advisory opinion.” <em>Herb </em>v. <em>Pitcairn, </em><span class="citation multiple-matches"><a href="/c/U.%20S./324/117/">324 U. S. 117</a></span>, 126 (1946). In the present case, there is no possibility that our opinion will be merely advisory. Even if the District Court of Appeal were to order a new trial solely on the basis of its cross-examination ruling, the admissibility of critical evidence at that trial hinges on the constitutional issue presented for review by petitioner. Thus, our resolution of that issue will affect the proceedings below regardless of how the District Court of Appeal rules on remand. In such circumstances there is no jurisdictional reason why we cannot address the issue presented to us.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Florida v. Powell.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Florida v. Powell"
type: case
citation: "559 U.S. 50 (2010)"
parallel_cite: "130 S. Ct. 1195; 175 L. Ed. 2d 1009"
neutral_cite: 2010 U.S. LEXIS 1898
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2010
date_decided: 2010-02-23
docket: 08-1175
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2010-02-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Florida v. Powell
  varies_by_point: false
  scope_note: "Good law; the four Miranda warnings are invariable in substance but need not be conveyed in any precise words — the test is whether the warnings reasonably convey the suspect's rights."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/1736/florida-v-powell/"
  cluster_id: 1736
  opinion_id: 1736
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Rhode Island v. Innis]]", "[[Dickerson v. United States]]", "[[Berghuis v. Thompkins]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "warning-adequacy", "right-to-counsel", "custodial-interrogation"]
holding: "Miranda warnings need not be given in any precise words; the four warnings are substantively invariable but the test is whether the advice, given a commonsense reading, reasonably conveys the suspect's rights — including, here, the right to have counsel present throughout interrogation."
lake:
  record_id: Florida v. Powell
  status: verified
  projected_at: 2026-07-06
---

# Florida v. Powell

*559 U.S. 50 (2010)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Kevin Dewayne Powell was arrested in Tampa and questioned about a handgun found during the arrest. Before interrogation, the officers read him a standard form advising that he had "the right to talk to a lawyer before answering any of [their] questions" and "the right to use any of [his] rights at any time [he] want[ed] during th[e] interview." He admitted owning the gun and was convicted of being a felon in possession. The Florida Supreme Court held the warnings inadequate under Miranda because they did not expressly state that he could have a lawyer present *during* questioning, and suppressed the statement.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] that advise of the right to talk to a lawyer "before answering any questions" and to use that right "at any time . . . during the interview," but do not expressly state a right to have counsel present throughout interrogation, adequately convey the right to counsel.

## Rule
Yes — warnings need not track any precise script. "The four warnings *Miranda* requires are invariable, but this Court has not dictated the words in which the essential information must be conveyed." — 559 U.S. at 60. ^pin-60

In assessing warnings, "reviewing courts are not required to examine the words employed 'as if construing a will or defining the terms of an easement. The inquiry is simply whether the warnings reasonably "conve[y] to [a suspect] his rights as required by *[[Miranda v. Arizona|Miranda]]*."'" — *Id.* (quoting *Duckworth v. Eagan*, 492 U.S. 195, 203 (1989), in turn quoting *[[California v. Prysock]]*, 453 U.S. 355, 361 (1981)).

## Application
Reading the two statements together, the warning passed the test. "The first statement communicated that Powell could consult with a lawyer before answering any particular question, and the second statement confirmed that he could exercise that right while the interrogation was underway. In combination, the two warnings reasonably conveyed Powell's right to have an attorney present, not only at the outset of interrogation, but at all times." — 559 U.S. at 62. ^pin-62

A reasonable suspect would not infer the "counterintuitive" idea that he had to leave and reenter the room to consult counsel between questions. Though "not the clearest possible formulation," the advice was "sufficiently comprehensive and comprehensible when given a commonsense reading." (Before reaching the merits the Court confirmed its jurisdiction, finding the Florida decision rested on federal law rather than an independent state ground.)

## Conclusion
The warnings reasonably conveyed Powell's right to counsel and satisfied Miranda; the judgment of the Florida Supreme Court was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Powell* applies the warning-adequacy principle of *[[California v. Prysock]]* (1981) and *[[Duckworth v. Eagan]]* (1989) to the right-to-counsel advisement, in the [[Miranda v. Arizona]] line. The Court noted that the FBI's fuller standard warnings are "exemplary" but declined to make any precise formulation mandatory. Related custody/interrogation doctrine appears in [[Rhode Island v. Innis]] and [[Berghuis v. Thompkins]]; Miranda's constitutional status was reaffirmed in [[Dickerson v. United States]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Florida v. Powell*, 559 U.S. 50 (2010) — https://www.courtlistener.com/opinion/1736/florida-v-powell/ — pinpoints: 60, 62.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "de7cd493a431f809", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Florida v. Powell"}, "payload": {"all": [{"cite": "559 U.S. 50", "page": "50", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "559"}, {"cite": "130 S. Ct. 1195", "page": "1195", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "130"}, {"cite": "175 L. Ed. 2d 1009", "page": "1009", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "175"}, {"cite": "2010 U.S. LEXIS 1898", "page": "1898", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2010"}], "display": "559 U.S. 50", "official": {"cite": "559 U.S. 50", "page": "50", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "559"}, "official_selection_present": true, "record_id": "Florida v. Powell"}}
{"assertion_id": "5fcea5c2e9bccdb9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-60", "record_id": "Florida v. Powell"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-60", "pinpoint_status": "slip-only", "quote": "but do not expressly state a right to have counsel present throughout interrogation, adequately convey the right to counsel. ## Rule Yes — warnings need not track any precise script.", "quote_fidelity": "mismatch", "record_id": "Florida v. Powell", "star_marker": null}}
{"assertion_id": "ea1cba51f1c05fd0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-62", "record_id": "Florida v. Powell"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-62", "pinpoint_status": "slip-only", "quote": "— *Id.* (quoting *Duckworth v. Eagan*, 492 U.S. 195, 203 (1989), in turn quoting *California v. Prysock*, 453 U.S. 355, 361 (1981)). ## Application Reading the two statements together, the warning passed the test.", "quote_fidelity": "mismatch", "record_id": "Florida v. Powell", "star_marker": null}}
{"assertion_id": "baacbabbab05dc8a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Florida v. Powell"}, "payload": {"as_of_content": "2010-02-23", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Florida v. Powell", "scope_note": "Good law; the four Miranda warnings are invariable in substance but need not be conveyed in any precise words — the test is whether the warnings reasonably convey the suspect's rights.", "varies_by_point": false}}
```

### lake record — Florida v. Powell

```json
{
  "schema_version": "s2.v1",
  "record_id": "Florida v. Powell",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Florida v. Powell",
    "case_name_short": "Powell",
    "case_name_full": "Florida v. Powell",
    "input_case_name": "Florida v. Powell",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2010-02-23",
    "year": 2010,
    "docket": "08-1175",
    "cluster_id": 1736,
    "lead_opinion_id": 1736,
    "sibling_ids": [
      1736,
      9413180,
      9413181
    ],
    "absolute_url": "/opinion/1736/florida-v-powell/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "559 U.S. 50",
      "volume": "559",
      "reporter": "U.S.",
      "page": "50",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "130 S. Ct. 1195",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "1195",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "175 L. Ed. 2d 1009",
        "volume": "175",
        "reporter": "L. Ed. 2d",
        "page": "1009",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. LEXIS 1898",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "1898",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "559 U.S. 50",
        "volume": "559",
        "reporter": "U.S.",
        "page": "50",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "130 S. Ct. 1195",
        "volume": "130",
        "reporter": "S. Ct.",
        "page": "1195",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "175 L. Ed. 2d 1009",
        "volume": "175",
        "reporter": "L. Ed. 2d",
        "page": "1009",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. LEXIS 1898",
        "volume": "2010",
        "reporter": "U.S. LEXIS",
        "page": "1898",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "559 U.S. 50",
    "official_selection": {
      "court_class": "scotus",
      "selected": "559 U.S. 50",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-60",
      "page": null,
      "quote": "but do not expressly state a right to have counsel present throughout interrogation, adequately convey the right to counsel. ## Rule Yes \u2014 warnings need not track any precise script.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-62",
      "page": null,
      "quote": "\u2014 *Id.* (quoting *Duckworth v. Eagan*, 492 U.S. 195, 203 (1989), in turn quoting *California v. Prysock*, 453 U.S. 355, 361 (1981)). ## Application Reading the two statements together, the warning passed the test.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2010-02-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Florida v. Powell",
    "varies_by_point": false,
    "scope_note": "Good law; the four Miranda warnings are invariable in substance but need not be conveyed in any precise words \u2014 the test is whether the warnings reasonably convey the suspect's rights.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Larry Loucious",
          "cluster_id": 4347647,
          "cite": [
            "847 F.3d 1146",
            "2017 WL 510457",
            "2017 U.S. App. LEXIS 2166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Rigterink v. State of Florida",
          "cluster_id": 3196514,
          "cite": [
            "193 So. 3d 846",
            "41 Fla. L. Weekly Supp. 177",
            "2016 WL 1592714",
            "2016 Fla. LEXIS 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colavita",
          "cluster_id": 1917344,
          "cite": [
            "993 A.2d 874",
            "606 Pa. 1",
            "2010 Pa. LEXIS 939"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 2445914,
          "cite": [
            "5 A.3d 177",
            "607 Pa. 165",
            "2010 Pa. LEXIS 2866"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kansas v. Kansas",
          "cluster_id": 3170728,
          "cite": [
            "577 U.S. 108",
            "136 S. Ct. 633",
            "193 L. Ed. 2d 535",
            "2016 U.S. LEXIS 845",
            "84 U.S.L.W. 4037",
            "25 Fla. L. Weekly Fed. S 593"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Runningeagle v. Schriro",
          "cluster_id": 804607,
          "cite": [
            "686 F.3d 758",
            "2012 WL 2913810",
            "2012 U.S. App. LEXIS 14682"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doody v. Ryan",
          "cluster_id": 216097,
          "cite": [
            "649 F.3d 986",
            "2011 U.S. App. LEXIS 9102",
            "2011 WL 1663551"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Clenney",
          "cluster_id": 184207,
          "cite": [
            "631 F.3d 658",
            "2011 U.S. App. LEXIS 2117",
            "2011 WL 322640"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Morgan Chase Woods",
          "cluster_id": 802516,
          "cite": [
            "684 F.3d 1045",
            "88 Fed. R. Serv. 970",
            "2012 WL 2196179",
            "2012 U.S. App. LEXIS 12295"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dunbar",
          "cluster_id": 5643419,
          "cite": [
            "24 N.Y.3d 304",
            "23 N.E.3d 946"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. State",
          "cluster_id": 2534150,
          "cite": [
            "42 So. 3d 204",
            "35 Fla. L. Weekly Supp. 323",
            "2010 Fla. LEXIS 854",
            "2010 WL 2195709"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson, Terence",
          "cluster_id": 3007650,
          "cite": [
            "475 S.W.3d 860",
            "2015 Tex. Crim. App. LEXIS 1057",
            "2015 WL 5853115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Murphy",
          "cluster_id": 813022,
          "cite": [
            "703 F.3d 182",
            "2012 U.S. App. LEXIS 24904",
            "2012 WL 6013773"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lee v. State",
          "cluster_id": 2553300,
          "cite": [
            "12 A.3d 1238",
            "418 Md. 136",
            "2011 Md. LEXIS 21"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Treesh v. Bagley",
          "cluster_id": 150480,
          "cite": [
            "612 F.3d 424",
            "2010 U.S. App. LEXIS 14260",
            "2010 WL 2771869"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Acosta-Col\u00f3n",
          "cluster_id": 8619484,
          "cite": [
            "741 F.3d 179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Wysinger",
          "cluster_id": 802889,
          "cite": [
            "683 F.3d 784",
            "2012 WL 2362492",
            "2012 U.S. App. LEXIS 12768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dire",
          "cluster_id": 800805,
          "cite": [
            "680 F.3d 446",
            "2012 WL 1860992"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kelvin Crumpton",
          "cluster_id": 3208822,
          "cite": [
            "824 F.3d 593",
            "2016 FED App. 0131P",
            "2016 U.S. App. LEXIS 9993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexander Balbuena v. William Sullivan",
          "cluster_id": 4775798,
          "cite": [
            "980 F.3d 619"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rigterink v. State",
          "cluster_id": 2494456,
          "cite": [
            "66 So. 3d 866",
            "36 Fla. L. Weekly Supp. 273",
            "2011 Fla. LEXIS 1343",
            "2011 WL 2374188"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Luckett",
          "cluster_id": 1917460,
          "cite": [
            "993 A.2d 25",
            "413 Md. 360",
            "2010 Md. LEXIS 140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Dunbar",
          "cluster_id": 6045181,
          "cite": [
            "104 A.D.3d 198",
            "958 N.Y.S.2d 764"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Polk",
          "cluster_id": 2481127,
          "cite": [
            "942 N.E.2d 44",
            "407 Ill. App. 3d 80",
            "347 Ill. Dec. 211",
            "2010 Ill. App. LEXIS 1421"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reuben Lujan v. Silvia Garcia",
          "cluster_id": 2620316,
          "cite": [
            "734 F.3d 917"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Clayton",
          "cluster_id": 4657797,
          "cite": [
            "937 F.3d 630"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ralios",
          "cluster_id": 901976,
          "cite": [
            "2010 SD 43",
            "783 N.W.2d 647",
            "2010 S.D. LEXIS 45",
            "2010 WL 2306679"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Florida v. Powell:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(1736 OR 9413180 OR 9413181) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 96,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 96,
        "triage_read": 4,
        "triage_snippet_classified": 92
      },
      "lane2_top_cited": {
        "query": "cites:(1736 OR 9413180 OR 9413181)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03JnM9OTM5MDM5NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%281736+OR+9413180+OR+9413181%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(1736 OR 9413180 OR 9413181)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 0,
        "triage_snippet_classified": 14
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(1736 OR 9413180 OR 9413181)",
    "indexed_citing_opinions": 119,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 1736,
        "count": 84,
        "count_source": "search"
      },
      {
        "opinion_id": 9413180,
        "count": 37,
        "count_source": "search"
      },
      {
        "opinion_id": 9413181,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 253,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/florida-v-powell.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwNjI0NTkmcz00ODQxNjc1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%281736+OR+9413180+OR+9413181%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 1736,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 103332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 110556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 111146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 111635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 112175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 112322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 112640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 117905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 118063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 130147,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 131160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 278817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 291232,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 313363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 390282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 544737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 576294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 582787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 717584,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 1087618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 1571939,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 1746854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 1765408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 1822619,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 1969831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 1736,
        "cited_id": 1984308,
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
    "date_created": "2026-07-05T04:18:38Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T04:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T04:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T04:22:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T04:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Florida v. Powell

```
(Slip Opinion)              OCTOBER TERM, 2009                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                          FLORIDA v. POWELL

        CERTIORARI TO THE SUPREME COURT OF FLORIDA

 No. 08–1175. Argued December 7, 2009—Decided February 23, 2010
In a pathmarking decision, Miranda v. Arizona, 384 U. S. 436, 471, this
  Court held that an individual must be “clearly informed,” prior to
  custodial questioning, that he has, among other rights, “the right to
  consult with a lawyer and to have the lawyer with him during inter
  rogation.”
    After arresting respondent Powell, but before questioning him,
  Tampa Police read him their standard Miranda form, stating, inter
  alia: “You have the right to talk to a lawyer before answering any of
  our questions” and “[y]ou have the right to use any of these rights at
  any time you want during this interview.” Powell then admitted he
  owned a handgun found in a police search. He was charged with pos
  session of a weapon by a convicted felon in violation of Florida law.
  The trial court denied Powell’s motion to suppress his inculpatory
  statements, which was based on the contention that the Miranda
  warnings he received did not adequately convey his right to the pres
  ence of an attorney during questioning. Powell was convicted of the
  gun-possession charge, but the intermediate appellate court held that
  the trial court should have suppressed the statements. The Florida
  Supreme Court agreed. It noted that both Miranda and the State
  Constitution require that a suspect be clearly informed of the right to
  have a lawyer present during questioning. The advice Powell re
  ceived was misleading, the court believed, because it suggested that
  he could consult with an attorney only before the police started to
  question him and did not convey his entitlement to counsel’s presence
  throughout the interrogation.
Held:
    1. This Court has jurisdiction to hear this case. Powell contends
 that jurisdiction is lacking because the Florida Supreme Court relied
 on the State’s Constitution as well as Miranda, hence the decision
2                          FLORIDA v. POWELL

                                  Syllabus

    rested on an adequate and independent state ground. See Coleman
    v. Thompson, 501 U. S. 722, 729. Under Michigan v. Long, 463 U. S.
    1032, 1040–1041, however, when a state court decision fairly appears
    to rest primarily on federal law, or to be interwoven with federal law,
    and the adequacy and independence of any possible state-law ground
    is not clear from the face of its opinion, this Court presumes that fed
    eral law controlled the state court’s decision. Although invoking Flor
    ida’s Constitution and precedent in addition to this Court’s decisions,
    the Florida court did not expressly assert that state-law sources gave
    Powell rights distinct from, or broader than, those delineated in
    Miranda. See Long, 463 U. S., at 1044. The state-court opinion con
    sistently trained on what Miranda demands, rather than on what
    Florida law independently requires. This Court therefore cannot
    identify, “from the face of the opinion,” a clear statement that the de
    cision rested on a state ground separate from Miranda. See Long,
    463 U. S., at 1041. Because the opinion does not “indicat[e] clearly
    and expressly that it is alternatively based on bona fide separate,
    adequate, and independent [state] grounds,” Long, 463 U. S., at 1041,
    this Court has jurisdiction. Pp. 4–7.
       2. Advice that a suspect has “the right to talk to a lawyer before
    answering any of [the law enforcement officers’] questions,” and that
    he can invoke this right “at any time . . . during th[e] interview,” sat
    isfies Miranda. Pp. 7–13.
          (a) Miranda requires that a suspect “be warned prior to any
    questioning . . . that he has the right to the presence of an attorney.”
    384 U. S., at 479. This Miranda warning addresses the Court’s par
    ticular concern that “[t]he circumstances surrounding in-custody in
    terrogation can operate very quickly to overbear the will of one
    merely made aware of his privilege [to remain silent] by his interro
    gators.” Id., at 469. Responsive to that concern, the Court stated, as
    “an absolute prerequisite to interrogation,” that an individual held
    for questioning “must be clearly informed that he has the right to
    consult with a lawyer and to have the lawyer with him during inter
    rogation.” Id., at 471. While the warnings prescribed by Miranda
    are invariable, this Court has not dictated the words in which the es
    sential information must be conveyed. See, e.g., California v. Pry
    sock, 453 U. S. 355, 359. In determining whether police warnings
    were satisfactory, reviewing courts are not required to “examine
    [them] as if construing a will or defining the terms of an easement.
    The inquiry is simply whether the warnings reasonably ‘conve[y] to
    [a suspect] his rights as required by Miranda.’ ” Duckworth v.
    Eagan, 492 U. S. 195, 203. Pp. 7–9.
          (b) The warnings Powell received satisfy this standard. By in
    forming Powell that he had “the right to talk to a lawyer before an
                      Cite as: 559 U. S. ____ (2010)                     3

                                 Syllabus

  swering any of [their] questions,” the Tampa officers communicated
  that he could consult with a lawyer before answering any particular
  question. And the statement that Powell had “the right to use any of
  [his] rights at any time [he] want[ed] during th[e] interview” con
  firmed that he could exercise his right to an attorney while the inter
  rogation was underway. In combination, the two warnings reasona
  bly conveyed the right to have an attorney present, not only at the
  outset of interrogation, but at all times. To reach the opposite con
  clusion, i.e., that the attorney would not be present throughout the
  interrogation, the suspect would have to imagine the counterintuitive
  and unlikely scenario that, in order to consult counsel, he would be
  obliged to exit and reenter the interrogation room between each
  query. Likewise unavailing is the Florida Supreme Court’s conclu
  sion that the warning was misleading because the temporal language
  that Powell could “talk to a lawyer before answering any of [the offi
  cers’] questions” suggested he could consult with an attorney only be
  fore the interrogation started. In context, the term “before” merely
  conveyed that Powell’s right to an attorney became effective before he
  answered any questions at all. Nothing in the words used indicated
  that counsel’s presence would be restricted after the questioning
  commenced. Powell suggests that today’s holding will tempt law en
  forcement agencies to end-run Miranda by amending their warnings
  to introduce ambiguity. But, as the Federal Government explains, it
  is in law enforcement’s own interest to state warnings with maxi
  mum clarity in order to reduce the risk that a court will later find the
  advice inadequate and therefore suppress a suspect’s statement. The
  standard warnings used by the Federal Bureau of Investigation are
  admirably informative, but the Court declines to declare their precise
  formulation necessary to meet Miranda’s requirements. Different
  words were used in the advice Powell received, but they communi
  cated the same message. Pp. 9–13.
998 So. 2d 531, reversed and remanded.

   GINSBURG, J., delivered the opinion of the Court, in which ROBERTS,
C. J., and SCALIA, KENNEDY, THOMAS, ALITO, and SOTOMAYOR, JJ.,
joined, and in which BREYER, J., joined as to Part II. STEVENS, J., filed a
dissenting opinion, in which BREYER, J., joined as to Part II.
                       Cite as: 559 U. S. ____ (2010)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 08–1175
                                  _________________


FLORIDA, PETITIONER v. KEVIN DEWAYNE POWELL
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       FLORIDA

                             [February 23, 2010] 


    JUSTICE GINSBURG delivered the opinion of the Court.
    In a pathmarking decision, Miranda v. Arizona, 384
U. S. 436, 471 (1966), the Court held that an individual
must be “clearly informed,” prior to custodial questioning,
that he has, among other rights, “the right to consult with
a lawyer and to have the lawyer with him during interro
gation.” The question presented in this case is whether
advice that a suspect has “the right to talk to a lawyer
before answering any of [the law enforcement officers’]
questions,” and that he can invoke this right “at any time
. . . during th[e] interview,” satisfies Miranda. We hold
that it does.
                            I
  On August 10, 2004, law enforcement officers in Tampa,
Florida, seeking to apprehend respondent Kevin Dewayne
Powell in connection with a robbery investigation, entered
an apartment rented by Powell’s girlfriend. 969 So. 2d
1060, 1063 (Fla. App. 2007). After spotting Powell coming
from a bedroom, the officers searched the room and dis
covered a loaded nine-millimeter handgun under the bed.
Ibid.
  The officers arrested Powell and transported him to the
2                    FLORIDA v. POWELL

                      Opinion of the Court

Tampa Police headquarters. Ibid. Once there, and before
asking Powell any questions, the officers read Powell the
standard Tampa Police Department Consent and Release
Form 310. Id., at 1063–1064. The form states:
    “You have the right to remain silent. If you give up
    the right to remain silent, anything you say can be
    used against you in court. You have the right to talk
    to a lawyer before answering any of our questions. If
    you cannot afford to hire a lawyer, one will be ap
    pointed for you without cost and before any question
    ing. You have the right to use any of these rights at
    any time you want during this interview.” App. 3.
    See also 969 So. 2d, at 1064.
   Acknowledging that he had been informed of his rights,
that he “underst[oo]d them,” and that he was “willing to
talk” to the officers, Powell signed the form. App. 3. He
then admitted that he owned the handgun found in the
apartment. Powell knew he was prohibited from possess
ing a gun because he had previously been convicted of a
felony, but said he had nevertheless purchased and car
ried the firearm for his protection. See 969 So. 2d, at
1064; App. 29.
   Powell was charged in state court with possession of a
weapon by a prohibited possessor, in violation of Fla. Stat.
Ann. §790.23(1) (West 2007).          Contending that the
Miranda warnings were deficient because they did not
adequately convey his right to the presence of an attorney
during questioning, he moved to suppress his inculpatory
statements. The trial court denied the motion, concluding
that the officers had properly notified Powell of his right to
counsel. 969 So. 2d, at 1064; App. 28. A jury convicted
Powell of the gun-possession charge. 969 So. 2d, at 1064.
   On appeal, the Florida Second District Court of Appeal
held that the trial court should have suppressed Powell’s
statements. Id., at 1067. The Miranda warnings, the
                      Cite as: 559 U. S. ____ (2010)                        3

                           Opinion of the Court

appellate court concluded, did not “adequately inform
[Powell] of his . . . right to have an attorney present
throughout [the] interrogation.” 969 So. 2d, at 1063.
Considering the issue to be “one of great public impor
tance,” the court certified the following question to the
Florida Supreme Court:
     “Does the failure to provide express advice of the right
     to the presence of counsel during questioning vitiate
     Miranda warnings which advise of both (A) the right
     to talk to a lawyer ‘before questioning’ and (B) the
     ‘right to use’ the right to consult a lawyer ‘at any time’
     during questioning?” Id., at 1067–1068 (some capi
     talization omitted).
   Surveying decisions of this Court as well as Florida
precedent, the Florida Supreme Court answered the certi
fied question in the affirmative. 998 So. 2d 531, 532
(2008). “Both Miranda and article I, section 9 of the Flor
ida Constitution,”1 the Florida High Court noted, “require
that a suspect be clearly informed of the right to have a
lawyer present during questioning.” Id., at 542. The court
found that the advice Powell received was misleading
because it suggested that Powell could “only consult with
an attorney before questioning” and did not convey Pow
ell’s entitlement to counsel’s presence throughout the
interrogation. Id., at 541. Nor, in the court’s view, did the
final catchall warning—“[y]ou have the right to use any of
these rights at any time you want during this interview”—
cure the defect the court perceived in the right-to-counsel
advice: “The catch-all phrase did not supply the missing
warning of the right to have counsel present during police
questioning,” the court stated, for “a right that has never
been expressed cannot be reiterated.” Ibid.
——————
    1 Article I, §9 of the Florida Constitution states that “[n]o person shall

. . . be compelled in any criminal matter to be a witness against one
self.”
4                    FLORIDA v. POWELL

                      Opinion of the Court

  Justice Wells dissented. He considered it “unreasonable
to conclude that the broad, unqualified language read to
Powell would lead a person of ordinary intelligence to
believe that he or she had a limited right to consult with
an attorney that could only be exercised before answering
the first question posed by law enforcement.” Id., at 544.
The final sentence of the warning, he stressed, “avoid[ed]
the implication—unreasonable as it may [have] be[en]—
that advice concerning the right of access to counsel before
questioning conveys the message that access to counsel is
foreclosed during questioning.” Ibid. (internal quotation
marks omitted).       Criticizing the majority’s “technical
adherence to language . . . that has no connection with
whether the person who confessed understood his or her
rights,” id., at 545, he concluded that “[t]he totality of the
warning reasonably conveyed to Powell his continuing
right of access to counsel,” id., at 544.
  We granted certiorari, 557 U. S. ___ (2009), and now
reverse the judgment of the Florida Supreme Court.
                             II
   We first address Powell’s contention that this Court
lacks jurisdiction to hear this case because the Florida
Supreme Court, by relying not only on Miranda but also
on the Florida Constitution, rested its decision on an
adequate and independent state ground. Brief for Peti
tioner 15–23. See Coleman v. Thompson, 501 U. S. 722,
729 (1991) (“This Court will not review a question of fed
eral law decided by a state court if the decision . . . rests
on a state law ground that is independent of the federal
question and adequate to support the judgment.”). “It is
fundamental,” we have observed, “that state courts be left
free and unfettered by us in interpreting their state con
stitutions.” Minnesota v. National Tea Co., 309 U. S. 551,
557 (1940). “But it is equally important that ambiguous or
obscure adjudications by state courts do not stand as
                     Cite as: 559 U. S. ____ (2010)                   5

                         Opinion of the Court

barriers to a determination by this Court of the validity
under the federal constitution of state action.” Ibid.
  To that end, we announced, in Michigan v. Long, 463
U. S. 1032, 1040–1041 (1983), the following presumption:
     “[W]hen . . . a state court decision fairly appears to
     rest primarily on federal law, or to be interwoven with
     the federal law, and when the adequacy and inde
     pendence of any possible state law ground is not clear
     from the face of the opinion, we will accept as the
     most reasonable explanation that the state court de
     cided the case the way it did because it believed that
     federal law required it to do so.”
At the same time, we adopted a plain-statement rule to
avoid the presumption: “If the state court decision indi
cates clearly and expressly that it is alternatively based on
bona fide separate, adequate, and independent grounds,
we, of course, will not undertake to review the decision.”
Id., at 1041.2
   Under the Long presumption, we have jurisdiction to
entertain this case. Although invoking Florida’s Constitu
tion and precedent in addition to this Court’s decisions,
the Florida Supreme Court treated state and federal law
as interchangeable and interwoven; the court at no point
——————
  2 Dissenting  in Michigan v. Long, 463 U. S. 1032 (1983), JUSTICE
STEVENS did not urge, as he now does, inspection of state-court deci
sions to count the number of citations to state and federal provisions
and opinions, or heroic efforts to fathom what the state court really
meant. See post, at 3–7 (dissenting opinion). Instead, his preferred
approach was as clear as the Court’s. In lieu of “presuming that
adequate state grounds are not independent unless it clearly appears
otherwise,” he would have “presum[ed] that adequate state grounds are
independent unless it clearly appears otherwise.” Long, 463 U. S., at
1066; see post, at 2, n. 1. Either presumption would avoid arduous
efforts to detect, case by case, whether a state ground of decision is
truly “independent of the [state court’s] understanding of federal law.”
Long, 463 U. S., at 1066. Today, however, the dissent would require
this Court to engage in just that sort of inquiry.
6                       FLORIDA v. POWELL

                          Opinion of the Court

expressly asserted that state-law sources gave Powell
rights distinct from, or broader than, those delineated in
Miranda. See Long, 463 U. S., at 1044.
   Beginning with the certified question—whether the
advice the Tampa police gave to Powell “vitiate[d]
Miranda,” 998 So. 2d, at 532 (some capitalization omit
ted)—and continuing throughout its opinion, the Florida
Supreme Court trained on what Miranda demands, rather
than on what Florida law independently requires. See,
e.g., 998 So. 2d, at 533 (“The issue before this Court is
whether the failure to provide express advice of the right
to the presence of counsel during custodial interrogation
violates the principles espoused in Miranda v. Arizona,
384 U. S. 436.”); id., at 538 (“[T]he issue of [what] Miranda
requires . . . has been addressed by several of the Florida
district courts of appeal.”); id., at 542 (Powell received a
“narrower and less functional warning than that required
by Miranda.”).3 We therefore cannot identify, “from the
face of the opinion,” a clear statement that the decision
rested on a state ground separate from Miranda. See
Long, 463 U. S., at 1041 (the state court “need only make
clear by a plain statement in its judgment or opinion that
the federal cases are being used only for the purpose of
guidance, and do not themselves compel the result that
the court has reached”).4 “To avoid misunderstanding, the
——————
   3 JUSTICE STEVENS suggests that these statements refer to Miranda

only in a “generic” sense to mean “the warnings suspects must be given
before interrogation.” Post, at 6. This explanation fails to account for
the Florida Supreme Court’s repeated citations to the opinion in
Miranda. In context, it is obvious that the court was attempting to
home in on what that opinion—which, of course, interpreted only the
Federal Constitution and not Florida law—requires. See, e.g., 998
So. 2d 531, 533, 534, 537, 538, 539, 540, 541, 542 (2008).
   4 JUSTICE STEVENS agrees that the Florida Supreme Court’s decision

is interwoven with federal law, post, at 7, and lacks the plain statement
contemplated by Long, post, at 3. Nevertheless, he finds it possible to
discern an independent state-law basis for the decision. As Long makes
                      Cite as: 559 U. S. ____ (2010)                        7

                           Opinion of the Court

[Florida] Supreme Court must itself speak with the clarity
it sought to require of its State’s police officers.” Ohio v.
Robinette, 519 U. S. 33, 45 (1996) (GINSBURG, J., concur
ring in judgment).
   Powell notes that “ ‘state courts are absolutely free to
interpret state constitutional provisions to accord greater
protection to individual rights than do similar provisions
of the United States Constitution.’ ” Brief for Respondent
19–20 (quoting Arizona v. Evans, 514 U. S. 1, 8 (1995)).
See also, e.g., Oregon v. Hass, 420 U. S. 714, 719 (1975);
Cooper v. California, 386 U. S. 58, 62 (1967). Powell is
right in this regard. Nothing in our decision today, we
emphasize, trenches on the Florida Supreme Court’s
authority to impose, based on the State’s Constitution, any
additional protections against coerced confessions it deems
appropriate. But because the Florida Supreme Court’s
decision does not “indicat[e] clearly and expressly that it is
alternatively based on bona fide separate, adequate, and
independent [state] grounds,” Long, 463 U. S., at 1041, we
have jurisdiction to decide this case.
                           III 

                            A

  To give force to the Constitution’s protection against
compelled self-incrimination, the Court established in
Miranda “certain procedural safeguards that require
——————
clear, however, “when . . . [the] state court decision fairly appears to . . .
be interwoven with . . . federal law,” the only way to avoid the jurisdic
tional presumption is to provide a plain statement expressing inde
pendent reliance on state law. 463 U. S., at 1040. It is this plain
statement that makes “the adequacy and independence of any possible
state law ground . . . clear from the face of the opinion.” Id., at 1040–
1041. See also Ohio v. Robinette, 519 U. S. 33, 44 (1996) (GINSBURG, J.,
concurring in judgment) (“Long governs even when, all things consid
ered, the more plausible reading of the state court’s decision may be
that the state court did not regard the Federal Constitution alone as a
sufficient basis for its ruling.”).
8                   FLORIDA v. POWELL

                     Opinion of the Court

police to advise criminal suspects of their rights under the
Fifth and Fourteenth Amendments before commencing
custodial interrogation.” Duckworth v. Eagan, 492 U. S.
195, 201 (1989). Intent on “giv[ing] concrete constitutional
guidelines for law enforcement agencies and courts to
follow,” 384 U. S., at 441–442, Miranda prescribed the
following four now-familiar warnings:
    “[A suspect] must be warned prior to any questioning
    [1] that he has the right to remain silent, [2] that any
    thing he says can be used against him in a court of
    law, [3] that he has the right to the presence of an at
    torney, and [4] that if he cannot afford an attorney
    one will be appointed for him prior to any questioning
    if he so desires.” Id., at 479.
   Miranda’s third warning—the only one at issue here—
addresses our particular concern that “[t]he circumstances
surrounding in-custody interrogation can operate very
quickly to overbear the will of one merely made aware of
his privilege [to remain silent] by his interrogators.” Id.,
at 469. Responsive to that concern, we stated, as “an
absolute prerequisite to interrogation,” that an individual
held for questioning “must be clearly informed that he has
the right to consult with a lawyer and to have the lawyer
with him during interrogation.” Id., at 471. The question
before us is whether the warnings Powell received satis
fied this requirement.
   The four warnings Miranda requires are invariable, but
this Court has not dictated the words in which the essen
tial information must be conveyed. See California v.
Prysock, 453 U. S. 355, 359 (1981) (per curiam) (“This
Court has never indicated that the rigidity of Miranda
extends to the precise formulation of the warnings given a
criminal defendant.” (internal quotation marks omitted));
Rhode Island v. Innis, 446 U. S. 291, 297 (1980) (safe
guards against self-incrimination include “Miranda warn
                 Cite as: 559 U. S. ____ (2010)            9

                     Opinion of the Court

ings . . . or their equivalent”). In determining whether
police officers adequately conveyed the four warnings, we
have said, reviewing courts are not required to examine
the words employed “as if construing a will or defining the
terms of an easement. The inquiry is simply whether the
warnings reasonably ‘conve[y] to [a suspect] his rights as
required by Miranda.’ ” Duckworth, 492 U. S., at 203
(quoting Prysock, 453 U. S., at 361).
                              B
    Our decisions in Prysock and Duckworth inform our
judgment here. Both concerned a suspect’s entitlement to
adequate notification of the right to appointed counsel. In
Prysock, an officer informed the suspect of, inter alia, his
right to a lawyer’s presence during questioning and his
right to counsel appointed at no cost. 453 U. S., at 356–
357. The Court of Appeals held the advice inadequate to
comply with Miranda because it lacked an express state
ment that the appointment of an attorney would occur
prior to the impending interrogation. See 453 U. S., at
358–359. We reversed. Id., at 362. “[N]othing in the
warnings,” we observed, “suggested any limitation on the
right to the presence of appointed counsel different from
the clearly conveyed rights to a lawyer in general, includ
ing the right to a lawyer before [the suspect is] questioned,
. . . while [he is] being questioned, and all during the
questioning.” Id., at 360–361 (internal quotation marks
omitted).
    Similarly, in Duckworth, we upheld advice that, in
relevant part, communicated the right to have an attorney
present during the interrogation and the right to an ap
pointed attorney, but also informed the suspect that the
lawyer would be appointed “if and when [the suspect goes]
to court.” 492 U. S., at 198 (emphasis deleted; internal
quotation marks omitted). “The Court of Appeals thought
th[e] ‘if and when you go to court’ language suggested that
10                       FLORIDA v. POWELL

                          Opinion of the Court

only those accused who can afford an attorney have the
right to have one present before answering any ques
tions. ” Id., at 203 (some internal quotation marks omit
ted). We thought otherwise. Under the relevant state
law, we noted, “counsel is appointed at [a] defendant’s
initial appearance in court.” Id., at 204. The “if and when
you go to court” advice, we said, “simply anticipate[d]” a
question the suspect might be expected to ask after receiv
ing Miranda warnings, i.e., “when [will he] obtain coun
sel.” 492 U. S., at 204. Reading the “if and when” lan
guage together with the other information conveyed, we
held that the warnings, “in their totality, satisfied
Miranda.” Id., at 205.
   We reach the same conclusion in this case. The Tampa
officers did not “entirely omi[t],” post, at 9, any informa
tion Miranda required them to impart. They informed
Powell that he had “the right to talk to a lawyer before
answering any of [their] questions” and “the right to use
any of [his] rights at any time [he] want[ed] during th[e]
interview.” App. 3. The first statement communicated
that Powell could consult with a lawyer before answering
any particular question, and the second statement con
firmed that he could exercise that right while the interro
gation was underway. In combination, the two warnings
reasonably conveyed Powell’s right to have an attorney
present, not only at the outset of interrogation, but at all
times.5
——————
   5 JUSTICE STEVENS asserts that the Court today approves, for “the

first time[,] . . . a warning which, if given its natural reading, entirely
omitted an essential element of a suspect’s rights.” Post, at 9. See also
post, at 12 (“[T]he warning entirely failed to inform [Powell] of the
separate and distinct right ‘to have counsel present during any ques
tioning.’ ”). We find the warning in this case adequate, however, only
because it communicated just what Miranda prescribed. JUSTICE
STEVENS ascribes a different meaning to the warning Powell received,
but he cannot credibly suggest that the Court regards the warning to
have omitted a vital element of Powell’s rights.
                     Cite as: 559 U. S. ____ (2010)                    11

                          Opinion of the Court

   To reach the opposite conclusion, i.e., that the attorney
would not be present throughout the interrogation, the
suspect would have to imagine an unlikely scenario: To
consult counsel, he would be obliged to exit and reenter
the interrogation room between each query. A reasonable
suspect in a custodial setting who has just been read his
rights, we believe, would not come to the counterintuitive
conclusion that he is obligated, or allowed, to hop in and
out of the holding area to seek his attorney’s advice.6
Instead, the suspect would likely assume that he must
stay put in the interrogation room and that his lawyer
would be there with him the entire time.7
   The Florida Supreme Court found the warning mislead
ing because it believed the temporal language—that Pow
ell could “talk to a lawyer before answering any of [the
officers’] questions”—suggested Powell could consult with
an attorney only before the interrogation started. 998
So. 2d, at 541. See also Brief for Respondent 28–29. In
context, however, the term “before” merely conveyed when
Powell’s right to an attorney became effective—namely,
before he answered any questions at all. Nothing in the
words used indicated that counsel’s presence would be
restricted after the questioning commenced. Instead, the
warning communicated that the right to counsel carried
forward to and through the interrogation: Powell could
seek his attorney’s advice before responding to “any of [the
officers’] questions” and “at any time . . . during th[e]
——————
  6 It is equally unlikely that the suspect would anticipate a scenario of

this order: His lawyer would be admitted into the interrogation room
each time the police ask him a question, then ushered out each time the
suspect responds.
  7 Although it does not bear on our decision, Powell seems to have

understood the warning this way. The following exchange between
Powell and his attorney occurred when Powell testified at his trial:
  “Q. You waived the right to have an attorney present during your
questioning by detectives; is that what you’re telling this jury?
  “A. Yes.” App. 80.
12                   FLORIDA v. POWELL

                      Opinion of the Court

interview.” App. 3 (emphasis added). Although the warn
ings were not the clearest possible formulation of
Miranda’s right-to-counsel advisement, they were suffi
ciently comprehensive and comprehensible when given a
commonsense reading.
   Pursuing a different line of argument, Powell points out
that most jurisdictions in Florida and across the Nation
expressly advise suspects of the right to have counsel
present both before and during interrogation. Brief for
Respondent 41–44. If we find the advice he received ade
quate, Powell suggests, law enforcement agencies, hoping
to obtain uninformed waivers, will be tempted to end-run
Miranda by amending their warnings to introduce ambi
guity. Brief for Respondent 50–53. But as the United
States explained as amicus curiae in support of the State
of Florida, “law enforcement agencies have little reason to
assume the litigation risk of experimenting with novel
Miranda formulations,” Brief for United States as Amicus
Curiae 6; instead, it is “desirable police practice” and “in
law enforcement’s own interest” to state warnings with
maximum clarity, id., at 12. See also id., at 11 (“By using
a conventional and precise formulation of the warnings,
police can significantly reduce the risk that a court will
later suppress the suspect’s statement on the ground that
the advice was inadequate.”).
   For these reasons, “all . . . federal law enforcement
agencies explicitly advise . . . suspect[s] of the full contours
of each [Miranda] right, including the right to the pres
ence of counsel during questioning.” Id., at 12. The stan
dard warnings used by the Federal Bureau of Investiga
tion are exemplary. They provide, in relevant part: “You
have the right to talk to a lawyer for advice before we ask
you any questions. You have the right to have a lawyer
with you during questioning.” Ibid., n. 3 (internal quota
tion marks omitted). This advice is admirably informa
tive, but we decline to declare its precise formulation
                 Cite as: 559 U. S. ____ (2010)                 13

                     Opinion of the Court

necessary to meet Miranda’s requirements. Different
words were used in the advice Powell received, but they
communicated the same essential message.
                        *    *    *
  For the reasons stated, the judgment of the Supreme
Court of Florida is reversed, and the case is remanded for
further proceedings not inconsistent with this opinion.

                                                  It is so ordered.
                 Cite as: 559 U. S. ____ (2010)          1

                    STEVENS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 08–1175
                         _________________


FLORIDA, PETITIONER v. KEVIN DEWAYNE POWELL
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                       FLORIDA

                     [February 23, 2010] 


  JUSTICE STEVENS, with whom JUSTICE BREYER joins as
to Part II, dissenting.
  Today, the Court decides a case in which the Florida
Supreme Court held a local police practice violated the
Florida Constitution. The Court’s power to review that
decision is doubtful at best; moreover, the Florida Su
preme Court has the better view on the merits.
                             I
  In this case, the Florida Supreme Court concluded that
“[b]oth Miranda and article I, section 9 of the Florida
Constitution require that a suspect be clearly informed of
the right to have a lawyer present during questioning,”
and that the warnings given to Powell did not satisfy
either the State or the Federal Constitution. 998 So. 2d
531, 542 (2008). In my view, the Florida Supreme Court
held on an adequate and independent state-law ground
that the warnings provided to Powell did not sufficiently
inform him of the “ ‘right to a lawyer’s help’ ” under the
Florida Constitution, id., at 535. This Court therefore
lacks jurisdiction to review the judgment below, notwith
standing the failure of that court to include some express
sentence that would satisfy this Court’s “plain-statement
rule,” ante, at 5.
  The adequate-and-independent-state-ground doctrine
rests on two “cornerstones”: “[r]espect for the independ
2                       FLORIDA v. POWELL

                        STEVENS, J., dissenting

ence of state courts” and “avoidance of rendering advisory
opinions.” Michigan v. Long, 463 U. S. 1032, 1040 (1983).
In Long, the Court adopted a novel presumption in favor
of jurisdiction when the independence of a state court’s
state-law judgment is not clear. But we only respect the
independence of state courts and avoid rendering advisory
opinions if we limit the application of that presumption to
truly ambiguous cases.1 This is not such a case.
  “[I]f the same judgment would be rendered by the state
court after we corrected its views of federal laws, our
review could amount to nothing more than an advisory
opinion.” Herb v. Pitcairn, 324 U. S. 117, 126 (1945). In
Long we advised every state court of a formula by which it
could assure us that our review would indeed amount to
nothing more than an advisory opinion. The state court
“need only make clear by a plain statement in its judg
ment or opinion that the federal cases are being used only
for the purpose of guidance, and do not themselves compel
the result that the court has reached.” 463 U. S., at 1041.
That advice has sometimes been misunderstood as a com
mand that unless such a plain statement is included in a
state-court opinion, the court’s ruling cannot have rested
on an adequate and independent state ground. But the
real question is whether “the adequacy and independence
of any possible state law ground is . . . clear from the face
——————
    1 In my view, this Court would better respect the independence of

state courts by applying the opposite presumption, as it did in the years
prior to 1983. See Long, 463 U. S., at 1066–1067 (STEVENS, J., dissent
ing). But accepting Long as the law, we can limit its negative effects—
unnecessary intrusion into the business of the state courts and unnec
essary advisory opinions—only if we limit its application to cases in
which the independence of the state-law ground is in serious doubt.
See Pennsylvania v. Labron, 518 U. S. 938, 950 (1996) (STEVENS, J.,
dissenting) (“[T]he unfortunate effects of [its] rule” are “exacerbate[d]
. . . to a nearly intolerable degree” when the Long presumption is
applied to cases in which “the state-law ground supporting th[e] judg
men[t] is so much clearer than has been true on most prior occasions”).
                      Cite as: 559 U. S. ____ (2010)                       3

                          STEVENS, J., dissenting

of the opinion.” Id., at 1040–1041. Even if a state court
opinion does not include the magic words set forth in
Long, or some similarly explicit sentence, we lack jurisdic
tion if it is nonetheless apparent that the decision is in
deed supported by an adequate and independent state
ground. Contrary to the assumption made by the Court,
we have no power to assume jurisdiction that does not
otherwise exist simply because the Florida Supreme Court
did not include in its decision some express statement that
its interpretation of state law is independent.
   In my view, we can tell from the face of the Florida
Supreme Court’s opinion that “the decision rested on a
state ground separate from Miranda,” ante, at 6. This
case is easily distinguished from Long in that regard. In
Long, although the Michigan Supreme Court had twice
cited the Michigan Constitution in its opinion, it “relied
exclusively on its understanding of Terry [v. Ohio, 392
U. S. 1 (1968),] and other federal cases. Not a single state
case was cited to support the state court’s holding that the
search of the passenger compartment was unconstitu
tional.” 463 U. S., at 1043. There was, in short, nothing
to “indicate that the decision below rested on grounds in
any way independent from the state court’s interpretation
of federal law.” Id., at 1044.
   Other cases in which we have applied the Long pre
sumption have been similarly devoid of independent state
law analysis. We typically apply the Long presumption
when the state court’s decision cited a state constitutional
provision only a few times or not at all, and rested exclu
sively upon federal cases or upon state cases that them
selves cited only federal law.2 We have also applied Long
——————
  2 See, e.g., Illinois v. Fisher, 540 U. S. 544, 547, n. (2004) (per curiam)

(describing decision below as relying upon the portion of a state prece
dent that solely discussed due process under the Federal Constitution);
Ohio v. Robinette, 519 U. S. 33, 37 (1996) (“[T]he only cases [the opin
ion] discusses or even cites are federal cases, except for one state case
4                        FLORIDA v. POWELL

                         STEVENS, J., dissenting

when the state court’s decision indicated that under state
law, the relevant state constitutional provision is consid
ered coextensive with the federal one.3 This case shares
none of those features.4
——————
which itself applies the Federal Constitution”); Illinois v. Rodriguez,
497 U. S. 177, 182 (1990) (“The opinion does not rely on (or even men
tion) any specific provision of the Illinois Constitution, nor even the
Illinois Constitution generally. Even the Illinois cases cited by the
opinion rely on no constitutional provisions other than the Fourth and
Fourteenth Amendments of the United States Constitution”); Florida v.
Riley, 488 U. S. 445, 448, n. 1 (1989) (plurality opinion) (finding Florida
Supreme Court mentioned the State Constitution three times but the
discussion “focused exclusively on federal cases dealing with the Fourth
Amendment”); Michigan v. Chesternut, 486 U. S. 567, 571, n. 3 (1988)
(describing state court as resting its holding on two state cases that
each relied upon federal law); New York v. P. J. Video, Inc., 475 U. S.
868, 872, n. 4 (1986) (“Here, the New York Court of Appeals cited the
New York Constitution only once, near the beginning of its opinion . . .
[and] repeatedly referred to the ‘First Amendment’ and ‘Fourth
Amendment’ during its discussion of the merits of the case”); Oliver v.
United States, 466 U. S. 170, 175, n. 5 (1984) (“The Maine Supreme
Judicial court referred only to the Fourth Amendment . . . [and] the
prior state cases that the court cited also construed the Federal Consti
tution”).
   3 See, e.g., Fitzgerald v. Racing Assn. of Central Iowa, 539 U. S. 103,

106 (2003) (“The Iowa Supreme Court’s opinion . . . says that ‘Iowa
courts are to “apply the same analysis in considering the state equal
protection clause as . . . in considering the federal equal protection
claim” ’ ”); Pennsylvania v. Muniz, 496 U. S. 582, 588, n. 4 (1990) (state
court explained that relevant state constitutional provision “offers a
protection against self-incrimination identical to that provided by the
Fifth Amendment” (internal quotation marks omitted)); Maryland v.
Garrison, 480 U. S. 79, 83–84 (1987) (state-court opinion relied on state
cases but indicated “that the Maryland constitutional provision is
construed in pari materia with the Fourth Amendment”).
   4 I do not mean to suggest that this Court has never reached out be

yond these bounds in order to decide a case. For example, in Labron,
518 U. S. 938, we found that a state court decision resting on the
“Commonwealth’s jurisprudence of the automobile exception,” Com
monwealth v. Labron, 543 Pa. 86, 100, 669 A. 2d 917, 924 (1995), was
not so clearly based on state law that the Long presumption did not
apply, even though only “some” of the state cases discussed in the state
                     Cite as: 559 U. S. ____ (2010)                     5

                         STEVENS, J., dissenting

   The Florida Supreme Court did not merely cite the
Florida Constitution a time or two without state-law
analysis.5 Rather, the court discussed and relied on the
separate rights provided under Art. I, §9 of the Florida
Constitution. For example, after a paragraph describing
the general scope of Miranda warnings under federal law,
the Court explained the general scope of warnings under
state law. 998 So. 2d, at 534–535 (“[T]o ensure the volun
tariness of confessions as required by article I, section 9 of
the Florida Constitution, this Court in Traylor v. State,
596 So. 2d 957 (Fla. 1992), outlined the . . . rights Florida
suspects must be told of prior to custodial interrogation,”
which includes “ ‘that they have a right to a lawyer’s
help’ ”). The court consistently referred to these state-law
rights as separate and distinct from Miranda, noting that
in its earlier cases, it had explained that “the require
ments of both the Fifth Amendment, as explained in
Miranda, and the Florida Constitution, as explained in
Traylor,” include “the requirement that a suspect be in
formed of the right to have counsel present during ques
tioning.” 998 So. 2d, at 537–538. And when applying the
law to the specific facts of this case, the Florida Supreme
Court again invoked the specific and distinct “right to a
——————
court’s opinion analyzed federal law. 518 U. S., at 939. The Court’s
analysis proved wrong; on remand, the Pennsylvania Supreme Court
reaffirmed its prior holding and “explicitly note[d] that it was, in fact,
decided upon independent grounds, i.e., Article I, Section 8 of the
Pennsylvania Constitution.” Commonwealth v. Labron, 547 Pa. 344,
345, 690 A. 2d 228 (1997). That we have overreached before is no
reason to repeat the mistake again.
   5 In examining what the state-court opinion said regarding state law,

and whether the state precedent cited in the opinion relied upon state
law, I am undertaking no effort more arduous than what the Court has
typically undertaken in order to determine whether the Long presump
tion applies: examining how frequently a state-court opinion cited state
law, whether state law is coextensive with federal law, and whether the
cited state cases relied upon federal law. See nn. 2–3, supra.
6                   FLORIDA v. POWELL

                    STEVENS, J., dissenting

lawyer’s help” under the Florida Constitution. Id., at 540.
   Moreover, the state cases relied upon by the Florida
Supreme Court did not themselves rely exclusively on
federal law. The primary case relied upon for the state
law holding, Traylor, rested exclusively upon state law.
See 596 So. 2d, at 961. In that decision, the Florida Su
preme Court embraced the principle that “[w]hen called
upon to decide matters of fundamental rights, Florida’s
state courts are bound under federalist principles to give
primacy to our state Constitution and to give independent
legal import to every phrase and clause contained
therein.” Id., at 962. Elaborating upon the meaning of
Art. I, §9 of the Florida Constitution, the Florida Supreme
Court explained the roots of Florida’s commitment to
protecting its citizens from self-incrimination. Florida has
long “required as a matter of state law that one charged
with a crime be informed of his rights prior to rendering a
confession.” Id., at 964. It has required warnings before
some interrogations since at least 1889, and has for that
long excluded confessions obtained in violation of those
rules. Ibid. In sum, this case looks quite different from
those cases in which we have applied the Long presump
tion in the past.
   The Court concludes otherwise by relying primarily
upon the formulation of the certified question and re
statements of that question within the Florida Supreme
Court’s opinion. See ante, at 6. Yet while the certified
question asks whether particular phrases “vitiate[d]
Miranda warnings,” 998 So. 2d, at 532 (capitalization and
footnote omitted), Miranda has become a generic term to
refer to the warnings suspects must be given before inter
rogation, see Merriam-Webster’s Collegiate Dictionary 792
(11th ed. 2003) (defining “Miranda” as “of, relating to, or
being the legal rights of an arrested person to have an
attorney and to remain silent so as to avoid self
incrimination”). Thus, its invocation of Miranda in the
                     Cite as: 559 U. S. ____ (2010)                     7

                         STEVENS, J., dissenting

certified question and in its statement of the issue
presented is entirely consistent with the fact that the
state-law basis for its decision is fully adequate and
independent.
   That said, I agree with the Court that the decision below
is interwoven with federal law. In reaching its state-law
holding, the Florida Supreme Court found Miranda and
our other precedents instructive.6 But that alone is insuf
ficient to assure our jurisdiction, even under Long. In my
view, the judgment—reversal of Powell’s conviction—is
supported by the Florida Supreme Court’s independent
and carefully considered holding that these warnings were
inadequate under the Florida Constitution. See 998
So. 2d, at 534–535, 537–538, 540, 542.
   The Court acknowledges that nothing in today’s decision
“trenches on the Florida Supreme Court’s authority to
impose, based on the State’s Constitution, any additional
protections against coerced confessions it deems appropri
ate.” Ante, at 7. As the Florida Supreme Court has noted
on more than one occasion, its interpretation of the Flor
ida Constitution’s privilege against self-incrimination need
not track our construction of the parallel provision in the
——————
  6 The Florida Supreme Court need not have decided that state-law

sources “gave Powell rights . . . broader than . . . those delineated in
Miranda,” ante, at 6, in order for its judgment to have rested upon an
independent state-law ground. The independence of a state-law ground
may be especially clear when a state court explicitly finds that the state
constitution is more protective of a certain right than the national
charter, but a state constitutional provision is no less independent for
providing the same protection in a given case as does the federal
provision, so long as the content of the state-law right is not compelled
by or dependent upon federal law. Unlike other provisions of Art. I of
the Florida Constitution, §9 does not contain an express proviso requir
ing that the right be construed in conformity with the analogous federal
provision. Compare Fla. Const., Art. I, §9, with Fla. Const., Art I, §12.
Furthermore, under Florida law the scope of Art. I, §9 is clearly not
dependent upon federal law. Rigterink v. State, 2 So. 3d 221, 241 (Fla.
2009); Traylor v. State, 596 So. 2d 957, 962 (Fla. 1992).
8                   FLORIDA v. POWELL

                    STEVENS, J., dissenting

Federal Constitution. See Rigterink v. State, 2 So. 3d 221,
241 (2009) (“[T]he federal Constitution sets the floor, not
the ceiling, and this Court retains the ability to interpret
the right against self-incrimination afforded by the Florida
Constitution more broadly than that afforded by its fed
eral counterpart”); Traylor, 596 So. 2d, at 961–963. In this
very case, the Florida Supreme Court may reinstate its
judgment upon remand. If the Florida Supreme Court
does so, as I expect it will, this Court’s opinion on the
merits will qualify as the sort of advisory opinion that we
should studiously seek to avoid.
                             II
  The Court’s decision on the merits is also unpersuasive.
As we recognized in Miranda, “the right to have counsel
present at [an] interrogation is indispensable to the pro
tection of the Fifth Amendment privilege.” Miranda v.
Arizona, 384 U. S. 436, 469 (1966). Furthermore, “the
need for counsel to protect the Fifth Amendment privilege
comprehends not merely a right to consult with counsel
prior to questioning, but also to have counsel present
during any questioning.” Id., at 470. Because the “ac
cused who does not know his rights and therefore does not
make a request may be the person who most needs coun
sel,” id., at 470–471, a defendant “must be clearly in
formed” regarding two aspects of his right to consult an
attorney: “the right to consult with a lawyer and to have
the lawyer with him during interrogation,” id., at 471.
  In this case, the form regularly used by the Tampa
police warned Powell that he had “the right to talk to a
lawyer before answering any of our questions.” App. 3.
This informed him only of the right to consult with a
lawyer before questioning, the very right the Miranda
Court identified as insufficient to protect the Fifth
Amendment privilege. The warning did not say anything
about the right to have counsel present during interroga
                    Cite as: 559 U. S. ____ (2010)                  9

                       STEVENS, J., dissenting

tion. Although we have never required “rigidity in the
form of the required warnings,” California v. Prysock, 453
U. S. 355, 359 (1981) (per curiam), this is, I believe, the
first time the Court has approved a warning which, if
given its natural reading, entirely omitted an essential
element of a suspect’s rights.
   Despite the failure of the warning to mention it, in the
Court’s view the warning “reasonably conveyed” to Powell
that he had the right to a lawyer’s presence during the
interrogation. Ante, at 10. The Court cobbles together
this conclusion from two elements of the warning. First,
the Court assumes the warning regarding Powell’s right
“to talk to a lawyer before answering any of [the officers’]
questions,” App. 3, conveyed that “Powell could consult
with a lawyer before answering any particular question,”
ante, at 10 (emphasis added).7 Second, in the Court’s
view, the addition of a catchall clause at the end of the
recitation of rights “confirmed” that Powell could use his
right to consult an attorney “while the interrogation was
underway.” Ibid.
   The more natural reading of the warning Powell was
given, which (1) contained a temporal limit and (2) failed
to mention his right to the presence of counsel in the
interrogation room, is that Powell only had the right to
consult with an attorney before the interrogation began,
not that he had the right to have an attorney with him
during questioning. Even those few Courts of Appeals
that have approved warnings that did not expressly men
——————
  7 Thisassumption makes it easier for the Court to conclude the warn
ing conveyed a right to have a lawyer present. If a suspect is told he
has the right to consult with an attorney before answering any particu
lar question, the Court may be correct that he would reasonably con
clude he has the right to a lawyer’s presence because otherwise he
would have to imagine he could consult his attorney in some unlikely
fashion (e.g., by leaving the interrogation room between every ques
tion).
10                       FLORIDA v. POWELL

                         STEVENS, J., dissenting

tion the right to an attorney’s presence during interroga
tion8 have found language of the sort used in Powell’s
warning to be misleading. For instance, petitioner cites
the Second Circuit’s decision in United States v. Lamia,
429 F. 2d 373 (1970), as an example of a court applying
the properly flexible approach to Miranda. But in that
case, the Second Circuit expressly distinguished a warning
that a suspect “ ‘could consult an attorney prior to any
question,’ ” which was “affirmatively misleading since it
was thought to imply that the attorney could not be pre
sent during questioning.” 429 F. 2d, at 377.9 That even
——————
  8 Several Courts of Appeals have held that warnings that did not

expressly inform a suspect of his right to have counsel present during
interrogation did not adequately inform a suspect of his Miranda
rights. See, e.g., United States v. Tillman, 963 F. 2d 137, 141 (CA6
1992); United States v. Bland, 908 F. 2d 471, 474 (CA9 1990); United
States v. Anthon, 648 F. 2d 669, 672–673 (CA10 1981); Windsor v.
United States, 389 F. 2d 530, 533 (CA5 1968). And most of the Circuits
that have not required express mention of the right to an attorney’s
presence have approved only general warnings regarding the right to
an attorney; that is, warnings which did not specifically mention the
right to counsel’s presence during interrogation but which also con
tained no limiting words that might mislead a suspect as to the broad
nature of his right to counsel. See, e.g., United States v. Frankson, 83
F. 3d 79, 82 (CA4 1996); United States v. Caldwell, 954 F. 2d 496, 502
(CA8 1992); United States v. Adams, 484 F. 2d 357, 361–362 (CA7
1973). I am doubtful that warning a suspect of his “right to counsel,”
without more, reasonably conveys a suspect’s full rights under
Miranda, but at least such a general warning does not include the same
sort of misleading temporal limitation as in Powell’s warning.
  9 Petitioner also cites Bridgers v. Dretke, 431 F. 3d 853 (CA5 2005), in

which the Fifth Circuit held the Texas Court of Criminal Appeals did
not unreasonably apply clearly established federal law in finding
adequate a warning in which a suspect was informed that “he had the
right to the presence of an attorney before any questioning commenced.”
Id., at 857 (internal quotation marks omitted). But even assuming that
warning would sufficiently apprise an individual of his right to an
attorney’s presence during interrogation, the fact that the warning
mentioned an attorney’s presence materially distinguishes it from the
warning Powell received. The Fifth Circuit quoted with approval the
                     Cite as: 559 U. S. ____ (2010)                    11

                         STEVENS, J., dissenting

the Courts of Appeals taking the most flexible approach to
Miranda have found warnings like Powell’s misleading
should caution the Court against concluding that such a
warning reasonably conveyed Powell’s right to have an
attorney with him during the interrogation.
   When the relevant clause of the warning in this case is
given its most natural reading, the catchall clause does
not meaningfully clarify Powell’s rights. It communicated
that Powell could exercise the previously listed rights at
any time. Yet the only previously listed right was the
“right to talk to a lawyer before answering any of [the
officers’] questions.” App. 3 (emphasis added). Informing
Powell that he could exercise, at any time during the
interview, the right to talk to a lawyer before answering
any questions did not reasonably convey the right to talk
to a lawyer after answering some questions, much less
implicitly inform Powell of his right to have a lawyer with
him at all times during interrogation. An intelligent
suspect could reasonably conclude that all he was provided
was a one-time right to consult with an attorney, not a
right to have an attorney present with him in the interro
gation room at all times.10
——————
state court’s assessment that warning a suspect solely that “he had the
right to consult or speak to an attorney before questioning . . . might
have created the [impermissible] impression that the attorney could not
be present during interrogation.” Ibid. (internal quotation marks
omitted).
   10 The Court supports its analysis by taking note of Powell’s testi

mony at trial, given after the trial judge had overruled his lawyer’s
objection that the warning he received was inadequate. In my view, the
testimony in context is not probative of what Powell thought the
warnings meant. It did not explore what Powell understood the warn
ings to mean, but simply established, as a prelude to Powell’s testimony
explaining his prior statement, that he had waived his rights. Regard
less, the testimony is irrelevant, as the Court acknowledges. “No
amount of circumstantial evidence that a person may have been aware
of [the right to have a lawyer with him during interrogation] will suffice
to stand” in the stead of an adequate warning. Miranda v. Arizona, 384
12                      FLORIDA v. POWELL

                        STEVENS, J., dissenting

   The Court relies on Duckworth v. Eagan, 492 U. S. 195
(1989), and Prysock, 453 U. S. 355, but in neither case did
the warning at issue completely omit one of a suspect’s
rights. In Prysock, the warning regarding the right to an
appointed attorney contained no temporal limitation, see
id., at 360–361, which clearly distinguishes that case from
Powell’s. In Duckworth, the suspect was explicitly in
formed that he had the right “to talk to a lawyer for advice
before we ask you any questions, and to have him with you
during questioning,” and that he had “this right to the
advice and presence of a lawyer even if you cannot afford
to hire one.” 492 U. S., at 198 (emphasis deleted; internal
quotation marks omitted). The warning thus conveyed in
full the right to appointed counsel before and during the
interrogation. Although the warning was arguably under
cut by the addition of a statement that an attorney would
be appointed “if and when you go to court,” the Court
found the suspect was informed of his full rights and the
warning simply added additional, truthful information
regarding when counsel would be appointed. Ibid. (em
phasis deleted; internal quotation marks omitted). Unlike
the Duckworth warning, Powell’s warning did not convey
his Miranda rights in full with the addition of some ar
guably misleading statement. Rather, the warning en
tirely failed to inform him of the separate and distinct
right “to have counsel present during any questioning.”
Miranda, 384 U. S., at 470.
   In sum, the warning at issue in this case did not rea
sonably convey to Powell his right to have a lawyer with
him during the interrogation. “The requirement of warn
ings . . . [is] fundamental with respect to the Fifth
Amendment privilege and not simply a preliminary ritual
to existing methods of interrogation.” Id., at 476. In
determining that the warning implied what it did not say,
——————
U. S. 436, 471–472 (1966).
                  Cite as: 559 U. S. ____ (2010)           13

                     STEVENS, J., dissenting

it is the Court “that is guilty of attaching greater impor
tance to the form of the Miranda ritual than to the sub
stance of the message it is intended to convey.” Prysock,
453 U. S., at 366 (STEVENS, J., dissenting).
                               III
   Whether we focus on Powell’s particular case, or the use
of the warning form as the standard used in one jurisdic
tion, it is clear that the form is imperfect. See ante, at 12.
As the majority’s decision today demonstrates, reasonable
judges may well differ over the question whether the
deficiency is serious enough to violate the Federal Consti
tution. That difference of opinion, in my judgment, falls
short of providing a justification for reviewing this case
when the judges of the highest court of the State have
decided the warning is insufficiently protective of the
rights of the State’s citizens. In my view, respect for the
independence of state courts, and their authority to set the
rules by which their citizens are protected, should result
in a dismissal of this petition.
   I respectfully dissent.

```

---
