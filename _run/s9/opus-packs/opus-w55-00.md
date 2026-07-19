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

## GROUP: content/cases/United States v. Ventresca.md  (`case`, 6 assertions)

### content_page

```
---
title: "United States v. Ventresca"
type: case
citation: "380 U.S. 102 (1965)"
parallel_cite: "85 S. Ct. 741; 13 L. Ed. 2d 684; 16 A.F.T.R.2d (RIA) 5787"
neutral_cite: 1965 U.S. LEXIS 2438
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1965
date_decided: 1965-03-01
docket: 28
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1965-03-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Ventresca
  varies_by_point: false
  scope_note: "Controlling and foundational: warrant affidavits are read in a commonsense, not hypertechnical, manner and doubtful cases are resolved in favor of the warrant — a cornerstone of the deferential review reaffirmed in Illinois v. Gates and the good-faith rule of United States v. Leon."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106990/united-states-v-ventresca/"
  cluster_id: 106990
  opinion_id: 106990
  identity_checked: true
homes:
  - page: "[[Probable Cause in the Affidavit]]"
    role: "Progeny"
  - page: "[[Probable Cause]]"
    role: "Related (cross-doctrine)"
related: ["[[Illinois v. Gates]]", "[[Aguilar v. Texas]]", "[[Brinegar v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "warrant-requirement", "affidavit", "probable-cause"]
holding: "A search-warrant affidavit must be read in a commonsense and realistic — not hypertechnical — manner, and doubtful or marginal probable-cause questions are resolved by the preference accorded to warrants; an affidavit that recites detailed underlying circumstances (even hearsay with a substantial basis) establishes probable cause."
lake:
  record_id: United States v. Ventresca
  status: verified
  projected_at: 2026-07-09
---

# United States v. Ventresca

*380 U.S. 102 (1965)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal investigators suspected Ventresca of operating an illegal still. An investigator's affidavit, drawing on his own observations and the corroborating reports of fellow investigators, detailed numerous facts — the odor of fermenting mash, deliveries of sugar and metal cans, and related activity at the premises. A United States Commissioner issued a search warrant, and the ensuing search uncovered an illegal distillery. The Court of Appeals held the affidavit insufficient because it did not clearly separate which facts were hearsay and which were within the affiant's personal knowledge.

## Issue
Did a detailed search-warrant affidavit — combining the affiant's own observations with corroborating reports of fellow officers — establish probable cause when read in a commonsense manner?

## Rule
Yes. "[A]ffidavits for search warrants . . . must be tested and interpreted by magistrates and courts in a commonsense and realistic fashion. They are normally drafted by nonlawyers in the midst and haste of a criminal investigation. Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area." — 380 U.S. at 108. ^pin-108

The limited exceptions to the warrant requirement "underscore[] the preference accorded police action taken under a warrant." — *Id.* at 106–07. ^pin-106

An affidavit may not be "purely conclusory," but "where these circumstances are detailed, where reason for crediting the source of the information is given, and when a magistrate has found probable cause, the courts should not invalidate the warrant by interpreting the affidavit in a hypertechnical, rather than a commonsense, manner." — [*Id.* at 108–09](https://www.courtlistener.com/opinion/106990/united-states-v-ventresca/#:~:text=purely%20conclusory%2C). ^pin-109a

And "the resolution of doubtful or marginal cases in this area should be largely determined by the preference to be accorded to warrants." — [*Id.* at 109](https://www.courtlistener.com/opinion/106990/united-states-v-ventresca/#:~:text=the%20resolution%20of%20doubtful%20or). ^pin-109b

## Application
The affidavit was detailed and specific, setting forth "a good many" of the underlying circumstances — the affiant's and fellow investigators' mutually corroborating observations of still activity. Read commonsensically rather than technically, it amply established probable cause. The Court of Appeals' insistence that the affidavit label each fact as hearsay or firsthand was exactly the hypertechnical reading the Fourth Amendment does not require; the corroborated observations supplied a substantial basis for the Commissioner's probable-cause finding.

## Conclusion
The affidavit established probable cause and the warrant was valid; the judgment of the Court of Appeals was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Ventresca* remains foundational: affidavits are read commonsensically and doubtful cases favor the warrant. Its deferential posture anchors the totality-of-the-circumstances review of [[Illinois v. Gates]] and the good-faith reliance rule. No negative treatment.

## Appears on
- [[Probable Cause in the Affidavit]] — *Progeny*
- [[Probable Cause]] — *Related (cross-doctrine)*

## Sources
- *United States v. Ventresca*, 380 U.S. 102 (1965) — https://www.courtlistener.com/opinion/106990/united-states-v-ventresca/ — pinpoints: 106–107, 108, 109.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fe06d10595033fb7", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "380 U.S. 102 (1965)", "court": "U.S. Supreme Court", "neutral_cite": "1965 U.S. LEXIS 2438", "official_citation_present": true, "parallel_cite": "85 S. Ct. 741; 13 L. Ed. 2d 684; 16 A.F.T.R.2d (RIA) 5787", "title": "United States v. Ventresca", "year": "1965"}}
{"assertion_id": "21d02c0b30a4f6d2", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause in the Affidavit"}, "payload": {"home": "Probable Cause in the Affidavit", "role": "Progeny", "title": "United States v. Ventresca"}}
{"assertion_id": "c6e29eaa3f2eb793", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A search-warrant affidavit must be read in a commonsense and realistic — not hypertechnical — manner, and doubtful or marginal probable-cause questions are resolved by the preference accorded to warrants; an affidavit that recites detailed underlying circumstances (even hearsay with a substantial basis) establishes probable cause.", "title": "United States v. Ventresca"}}
{"assertion_id": "e140bea4e5bf9714", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Related (cross-doctrine)", "title": "United States v. Ventresca"}}
{"assertion_id": "0f4e0dbd2c45b71d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1965-03-01", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Ventresca", "field_i_validity": "good_law", "scope_note": "Controlling and foundational: warrant affidavits are read in a commonsense, not hypertechnical, manner and doubtful cases are resolved in favor of the warrant — a cornerstone of the deferential review reaffirmed in Illinois v. Gates and the good-faith rule of United States v. Leon.", "title": "United States v. Ventresca", "varies_by_point": "false"}}
{"assertion_id": "6097d82bd03c6f46", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "United States v. Ventresca"}}
```

### lake record — United States v. Ventresca

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Ventresca",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Ventresca",
    "case_name_short": "Ventresca",
    "case_name_full": "United States v. Ventresca",
    "input_case_name": "United States v. Ventresca",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1965-03-01",
    "year": 1965,
    "docket": "28",
    "cluster_id": 106990,
    "lead_opinion_id": 106990,
    "sibling_ids": [
      106990,
      9422971,
      9422972
    ],
    "absolute_url": "/opinion/106990/united-states-v-ventresca/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "380 U.S. 102",
      "volume": "380",
      "reporter": "U.S.",
      "page": "102",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "85 S. Ct. 741",
        "volume": "85",
        "reporter": "S. Ct.",
        "page": "741",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 L. Ed. 2d 684",
        "volume": "13",
        "reporter": "L. Ed. 2d",
        "page": "684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 A.F.T.R.2d (RIA) 5787",
        "volume": "16",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "5787",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1965 U.S. LEXIS 2438",
        "volume": "1965",
        "reporter": "U.S. LEXIS",
        "page": "2438",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "380 U.S. 102",
        "volume": "380",
        "reporter": "U.S.",
        "page": "102",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 S. Ct. 741",
        "volume": "85",
        "reporter": "S. Ct.",
        "page": "741",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "13 L. Ed. 2d 684",
        "volume": "13",
        "reporter": "L. Ed. 2d",
        "page": "684",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1965 U.S. LEXIS 2438",
        "volume": "1965",
        "reporter": "U.S. LEXIS",
        "page": "2438",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "16 A.F.T.R.2d (RIA) 5787",
        "volume": "16",
        "reporter": "A.F.T.R.2d (RIA)",
        "page": "5787",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "380 U.S. 102",
    "official_selection": {
      "court_class": "scotus",
      "selected": "380 U.S. 102",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-108",
      "page": null,
      "quote": "--- # United States v. Ventresca *380 U.S. 102 (1965)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal investigators suspected Ventresca of operating an illegal still. An investigator's affidavit, drawing on his own observations and the corroborating reports of fellow investigators, detailed numerous facts \u2014 the odor of fermenting mash, deliveries of sugar and metal cans, and related activity at the premises. A United States Commissioner issued a search warrant, and the ensuing search uncovered an illegal distillery. The Court of Appeals held the affidavit insufficient because it did not clearly separate which facts were hearsay and which were within the affiant's personal knowledge. ## Issue Did a detailed search-warrant affidavit \u2014 combining the affiant's own observations with corroborating reports of fellow officers \u2014 establish probable cause when read in a commonsense manner? ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-106",
      "page": null,
      "quote": "underscore[] the preference accorded police action taken under a warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-109a",
      "page": null,
      "quote": "purely conclusory,",
      "star_marker": "108",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 12771,
      "fragment": "#:~:text=purely%20conclusory%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-109b",
      "page": null,
      "quote": "the resolution of doubtful or marginal cases in this area should be largely determined by the preference to be accorded to warrants.",
      "star_marker": "109",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13807,
      "fragment": "#:~:text=the%20resolution%20of%20doubtful%20or",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1965-03-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Ventresca",
    "varies_by_point": false,
    "scope_note": "Controlling and foundational: warrant affidavits are read in a commonsense, not hypertechnical, manner and doubtful cases are resolved in favor of the warrant \u2014 a cornerstone of the deferential review reaffirmed in Illinois v. Gates and the good-faith rule of United States v. Leon.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Iowa v. Jesse Jon Harbach",
          "cluster_id": 9493041,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
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
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. (And",
          "cluster_id": 7171453,
          "cite": [
            "94 N.E.3d 435",
            "92 Mass. App. Ct. 1107"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gigliotti",
          "cluster_id": 7316853,
          "cite": [
            "145 F. Supp. 3d 203",
            "2015 WL 6830675"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Byron Moore",
          "cluster_id": 3150840,
          "cite": [
            "805 F.3d 590",
            "2015 U.S. App. LEXIS 18858",
            "2015 WL 6742704"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. John Flanagan",
          "cluster_id": 2826359,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fontaine",
          "cluster_id": 6590019,
          "cite": [
            "84 Mass. App. Ct. 699",
            "3 N.E.3d 82",
            "2014 WL 185357",
            "2014 Mass. App. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Simmons",
          "cluster_id": 2660461,
          "cite": [
            "951 F. Supp. 2d 137",
            "2013 U.S. Dist. LEXIS 94034",
            "2013 WL 3244813"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jesus Cervantes",
          "cluster_id": 799940,
          "cite": [
            "678 F.3d 798",
            "2012 WL 1700840",
            "2012 U.S. App. LEXIS 9843"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Howard Lee Griggs",
          "cluster_id": 2991280,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maurice Jackson v. State",
          "cluster_id": 3103664,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane1_negative"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Malley v. Briggs",
          "cluster_id": 111611,
          "cite": [
            "89 L. Ed. 2d 271",
            "106 S. Ct. 1092",
            "475 U.S. 335",
            "1986 U.S. LEXIS 29",
            "54 U.S.L.W. 4243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chambers v. Maroney",
          "cluster_id": 108184,
          "cite": [
            "26 L. Ed. 2d 419",
            "90 S. Ct. 1975",
            "399 U.S. 42",
            "1970 U.S. LEXIS 19"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Matlock",
          "cluster_id": 108967,
          "cite": [
            "39 L. Ed. 2d 242",
            "94 S. Ct. 988",
            "415 U.S. 164",
            "1974 U.S. LEXIS 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Branzburg v. Hayes",
          "cluster_id": 108611,
          "cite": [
            "33 L. Ed. 2d 626",
            "92 S. Ct. 2646",
            "408 U.S. 665",
            "1972 U.S. LEXIS 132",
            "24 Rad. Reg. 2d (P & F) 2125",
            "1 Media L. Rep. (BNA) 2617"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tyler",
          "cluster_id": 109874,
          "cite": [
            "56 L. Ed. 2d 486",
            "98 S. Ct. 1942",
            "436 U.S. 499",
            "1978 U.S. LEXIS 97"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. White",
          "cluster_id": 108304,
          "cite": [
            "28 L. Ed. 2d 453",
            "91 S. Ct. 1122",
            "401 U.S. 745",
            "1971 U.S. LEXIS 132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bigelow",
          "cluster_id": 5687958,
          "cite": [
            "66 N.Y.2d 417",
            "497 N.Y.S.2d 630",
            "488 N.E.2d 451",
            "1985 N.Y. LEXIS 17919"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Massachusetts v. Upton",
          "cluster_id": 111172,
          "cite": [
            "80 L. Ed. 2d 721",
            "104 S. Ct. 2085",
            "466 U.S. 727",
            "1984 U.S. LEXIS 81",
            "52 U.S.L.W. 3822"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Class",
          "cluster_id": 111600,
          "cite": [
            "89 L. Ed. 2d 81",
            "106 S. Ct. 960",
            "475 U.S. 106",
            "1986 U.S. LEXIS 5",
            "54 U.S.L.W. 4178"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
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
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barnes v. State",
          "cluster_id": 2455822,
          "cite": [
            "876 S.W.2d 316",
            "1994 Tex. Crim. App. LEXIS 21",
            "1994 WL 36894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1718150,
          "cite": [
            "803 S.W.2d 272",
            "1990 WL 180807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Ventresca:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106990 OR 9422971 OR 9422972) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzAyNjUyODAwMDAwJnM9MjI5MTA3MSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106990+OR+9422971+OR+9422972%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(106990 OR 9422971 OR 9422972)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNTEmcz01Mzg4MTgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106990+OR+9422971+OR+9422972%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106990 OR 9422971 OR 9422972)",
        "reviewed": 31,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 31,
        "triage_read": 1,
        "triage_snippet_classified": 30
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106990 OR 9422971 OR 9422972)",
    "indexed_citing_opinions": 2890,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106990,
        "count": 2623,
        "count_source": "search"
      },
      {
        "opinion_id": 9422971,
        "count": 334,
        "count_source": "search"
      },
      {
        "opinion_id": 9422972,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4171,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-ventresca.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MDYzNDgmcz05NDM1NzY0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106990+OR+9422971+OR+9422972%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106990,
        "cited_id": 85007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106990,
        "cited_id": 106964,
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
    "date_created": "2026-07-06T03:19:52Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:20:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:20:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:22:46Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:20:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Ventresca

```
<div>
<center><b><span class="citation" data-id="9422971"><a href="/opinion/106990/united-states-v-ventresca/" aria-description="Citation for case: United States v. Ventresca">380 U.S. 102</a></span> (1965)</b></center>
<center><h1>UNITED STATES<br>
v.<br>
VENTRESCA.</h1></center>
<center>No. 28.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 18-19, 1965.</center>
<center>Decided March 1, 1965.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE FIRST CIRCUIT.
<p><span class="star-pagination">*103</span> <i>Frank I. Goodman</i> argued the cause for the United States. On the brief were <i>Solicitor General Cox, Assistant Attorney General Miller, Beatrice Rosenberg</i> and <i>Ronald L. Gainer.</i></p>
<p><i>Matthew R. McCann</i> argued the cause for respondent. With him on the brief was <i>Edward C. Maher.</i></p>
<p>MR. JUSTICE GOLDBERG delivered the opinion of the Court.</p>
<p>Respondent, Ventresca, was convicted in the United States District Court for the District of Massachusetts of possessing and operating an illegal distillery. The conviction was reversed by the Court of Appeals (one judge dissenting) on the ground that the affidavit for a search warrant pursuant to which the still was found was insufficient to establish probable cause. <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/" aria-description="Citation for case: Giacomo Ventresca v. United States">324 F. 2d 864</a></span>.</p>
<p>The affidavit upon which the warrant was issued was made and submitted to a United States Commissioner on August 31, 1961, by Walter Mazaka, an Investigator for the Alcohol and Tobacco Tax Division of the Internal Revenue Service. He stated that he had reason to believe that an illegal distillery was in operation in respondent, Ventresca's, house at 148 1/2 Coburn Avenue in Worcester, Massachusetts. The grounds for this belief were set forth in detail in the affidavit, prefaced with the following statement:</p>
<blockquote>"Based upon observations made by me, and based upon information received officially from other Investigators attached to the Alcohol and Tobacco Tax Division assigned to this investigation, and reports orally made to me describing the results of their <span class="star-pagination">*104</span> observations and investigation, this request for the issuance of a search warrant is made."</blockquote>
<p>The affidavit then described seven different occasions between July 28 and August 30, 1961, when a Pontiac car was driven into the yard to the rear of Ventresca's house. On four occasions the car carried loads of sugar in 60-pound bags; it made two trips loaded with empty tin cans; and once it was merely observed as being heavily laden. Garry, the car's owner, and Incardone, a passenger, were seen on several occasions loading the car at Ventresca's house and later unloading apparently full five-gallon cans at Garry's house late in the evening. On August 28, after a delivery of empty tin cans to Ventresca's house, Garry and Incardone were observed carrying from the house cans which appeared to be filled and placing them in the trunk of Garry's car. The affidavit went on to state that at about 4 a. m. on August 18, and at about 4 a. m. on August 30, "Investigators" smelled the odor of fermenting mash as they walked along the sidewalk in front of Ventresca's house. On August 18 they heard, "[a]t or about the same time, . . . certain metallic noises." On August 30, the day before the warrant was applied for, they heard (as they smelled the mash) "sounds similar to that of a motor or a pump coming from the direction of" Ventresca's house. The affidavit concluded: "The foregoing information is based upon personal knowledge and information which has been obtained from Investigators of the Alcohol and Tobacco Tax Division, Internal Revenue Service, who have been assigned to this investigation."</p>
<p>The District Court upheld the validity of the warrant on a motion to suppress. The divided Court of Appeals held the warrant insufficient because it read the affidavit as not specifically stating in so many words that the information it contained was based upon the personal knowledge of Mazaka or other reliable investigators. The <span class="star-pagination">*105</span> Court of Appeals reasoned that all of the information recited in the affidavit might conceivably have been obtained by investigators other than Mazaka, and it could not be certain that the information of these other investigators was not in turn based upon hearsay received from unreliable informants rather than their own personal observations. For this reason the court found that probable cause had not been established. <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/#868" aria-description="Citation for case: Giacomo Ventresca v. United States">324 F. 2d, at 868-870</a></span>. We granted certiorari to consider the standards by which a reviewing court should approach the interpretation of affidavits supporting warrants which have been duly issued by examining magistrates. <span class="citation multiple-matches"><a href="/c/U.%20S./377/989/">377 U. S. 989</a></span>. For the reasons stated below, we reverse the judgment of the Court of Appeals.</p>
<p></p>
<h2>I.</h2>
<p>The Fourth Amendment states:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause. supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."<sup>[1]</sup></blockquote>
<p>We begin our analysis of this constitutional rule mindful of the fact that in this case a search was made pursuant to a search warrant. In discussing the Fourth Amendment policy against unnecessary invasions of privacy, we stated in <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>:</p>
<blockquote>"An evaluation of the constitutionality of a search warrant should begin with the rule that `the informed and deliberate determinations of magistrates empowered to issue warrants . . . are to be preferred <span class="star-pagination">*106</span> over the hurried action of officers . . . who may happen to make arrests.' <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span>. The reasons for this rule go to the foundations of the Fourth Amendment." <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#110" aria-description="Citation for case: Aguilar v. Texas">378 U. S., at 110-111</a></span>.</blockquote>
<p>In <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270</a></span>, this Court, strongly supporting the preference to be accorded searches under a warrant, indicated that in a doubtful or marginal case a search under a warrant may be sustainable where without one it would fall. In <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, and <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>, the Court, in condemning searches by officers who invaded premises without a warrant, plainly intimated that had the proper course of obtaining a warrant from a magistrate been followed and had the magistrate on the same evidence available to the police made a finding of probable cause, the search under the warrant would have been sustained. Mr. Justice Jackson stated for the Court in <i><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span>:</i></p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers." <i>Johnson</i> v. <i>United States, supra,</i> at 13-14.</blockquote>
<p>The fact that exceptions to the requirement that searches and seizures be undertaken only after obtaining a warrant <span class="star-pagination">*107</span> are limited<sup>[2]</sup> underscores the preference accorded police action taken under a warrant as against searches and seizures without one.</p>
<p>While a warrant may issue only upon a finding of "probable cause," this Court has long held that "the term `probable cause' . . . means less than evidence which would justify condemnation," <i>Locke</i> v. <i>United States,</i> <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span>, and that a finding of "probable cause" may rest upon evidence which is not legally competent in a criminal trial. <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#311" aria-description="Citation for case: Draper v. United States">358 U. S. 307, 311</a></span>. <span class="star-pagination">*108</span> As the Court stated in <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#173" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 173</a></span>, "There is a large difference between the two things to be proved [guilt and probable cause], as well as between the tribunals which determine them, and therefore a like difference in the <i>quanta</i> and modes of proof required to establish them." Thus hearsay may be the basis for issuance of the warrant "so long as there [is] a substantial basis for crediting the hearsay." <i>Jones</i> v. <i>United States, supra,</i> at 272. And, in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span></i> we recognized that "an affidavit may be based on hearsay information and need not reflect the direct personal observations of the affiant," so long as the magistrate is "informed of some of the underlying circumstances" supporting the affiant's conclusions and his belief that any informant involved "whose identity need not be disclosed . . . was `credible' or his information `reliable.' " <i>Aguilar</i> v. <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#114" aria-description="Citation for case: Aguilar v. Texas"><i>Texas, supra,</i> at 114</a></span>.</p>
<p>These decisions reflect the recognition that the Fourth Amendment's commands, like all constitutional requirements, are practical and not abstract. If the teachings of the Court's cases are to be followed and the constitutional policy served, affidavits for search warrants, such as the one involved here, must be tested and interpreted by magistrates and courts in a commonsense and realistic fashion. They are normally drafted by nonlawyers in the midst and haste of a criminal investigation. Technical requirements of elaborate specificity once exacted under common law pleadings have no proper place in this area. A grudging or negative attitude by reviewing courts toward warrants will tend to discourage police officers from submitting their evidence to a judicial officer before acting.</p>
<p>This is not to say that probable cause can be made out by affidavits which are purely conclusory, stating only the affiant's or an informer's belief that probable cause exists without detailing any of the "underlying circumstances" <span class="star-pagination">*109</span> upon which that belief is based. See <i>Aguilar</i> v. <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra</a></span></i><i>.</i> Recital of some of the underlying circumstances in the affidavit is essential if the magistrate is to perform his detached function and not serve merely as a rubber stamp for the police. However, where these circumstances are detailed, where reason for crediting the source of the information is given, and when a magistrate has found probable cause, the courts should not invalidate the warrant by interpreting the affidavit in a hypertechnical, rather than a commonsense, manner. Although in a particular case it may not be easy to determine when an affidavit demonstrates the existence of probable cause, the resolution of doubtful or marginal cases in this area should be largely determined by the preference to be accorded to warrants. <i>Jones</i> v. <i>United States, supra,</i> at 270.</p>
<p></p>
<h2>II.</h2>
<p>The application of the principles stated above leads us to reverse the Court of Appeals. The affidavit in this case, if read in a commonsense way rather than technically, shows ample facts to establish probable cause and allow the Commissioner to issue the search warrant. The affidavit at issue here, unlike the affidavit held insufficient in <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span>,</i> is detailed and specific. It sets forth not merely "some of the underlying circumstances" supporting the officer's belief, but a good many of them. This is apparent from the summary of the affidavit already recited and from its text which is reproduced in the Appendix.</p>
<p>The Court of Appeals did not question the specificity of the affidavit. It rested its holding that the affidavit was insufficient on the ground that "[t]he affidavit failed to clearly indicate which of the facts alleged therein were hearsay or which were within the affiant's own knowledge," and therefore "[t]he Commissioner could only conclude that the entire affidavit was based on hearsay." <span class="star-pagination">*110</span> <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/#868" aria-description="Citation for case: Giacomo Ventresca v. United States">324 F. 2d, at 868</a></span>. While the Court of Appeals recognized that an affidavit based on hearsay will be sufficient, "so long as a substantial basis for crediting the hearsay is presented," <i>Jones</i> v. <i>United States, supra,</i> at 269, it felt that no such basis existed here because the hearsay consisted of reports by "Investigators," and the affidavit did not recite how the Investigators obtained their information. The Court of Appeals conceded that the affidavit stated that the Investigators themselves smelled the odor of fermenting mash, but argued that the rest of their information might itself have been based upon hearsay thus raising "the distinct possibility of hearsay-upon-hearsay." <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/#869" aria-description="Citation for case: Giacomo Ventresca v. United States">324 F. 2d, at 869</a></span>. For this reason, it held that the affidavit did not establish probable cause.</p>
<p>We disagree with the conclusion of the Court of Appeals. Its determination that the affidavit might have been based wholly upon hearsay cannot be supported in light of the fact that Mazaka, a Government Investigator, swore under oath that the relevant information was in part based "upon observations made by me" and "upon personal knowledge" as well as upon "information which has been obtained from Investigators of the Alcohol and Tobacco Tax Division, Internal Revenue Service, who have been assigned to this investigation." It also seems to us that the assumption of the Court of Appeals that all of the information in Mazaka's affidavit may in fact have come from unreliable anonymous informers, passed on to Government Investigators, who in turn related this information to Mazaka is without foundation. Mazaka swore that, insofar as the affidavit was not based upon his own observations, it was "based upon information received officially from other Investigators attached to the Alcohol and Tobacco Tax Division assigned to this investigation, and reports orally made to me describing the results of their <i>observations</i> and investigation." (Emphasis <span class="star-pagination">*111</span> added.) The Court of Appeals itself recognized that the affidavit stated that " `Investigators' [employees of the Service] smelled the odor of fermenting mash in the vicinity of the suspected dwelling." <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/#869" aria-description="Citation for case: Giacomo Ventresca v. United States">324 F. 2d, at 869</a></span>. A qualified officer's detection of the smell of mash has often been held a very strong factor in determining that probable cause exists so as to allow issuance of a warrant.<sup>[3]</sup> Moreover, upon reading the affidavit as a whole, it becomes clear that the detailed observations recounted in the affidavit cannot fairly be regarded as having been made in any significant part by persons other than full-time Investigators of the Alcohol and Tobacco Tax Division of the Internal Revenue Service. Observations of fellow officers of the Government engaged in a common investigation are plainly a reliable basis for a warrant applied for by one of their number.<sup>[4]</sup> We conclude that the affidavit showed probable cause and that the Court of Appeals misapprehended its judicial function in reviewing this affidavit by giving it an unduly technical and restrictive reading.</p>
<p>This Court is alert to invalidate unconstitutional searches and seizures whether with or without a warrant. See <i>Aguilar</i> v. <i><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Texas, supra</a></span></i><i>; </i><i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476</a></span>; <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>; <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>. By doing so, it vindicates individual liberties and strengthens the administration of justice by promoting respect for law and order. This Court is equally concerned to uphold the actions of law <span class="star-pagination">*112</span> enforcement officers consistently following the proper constitutional course. This is no less important to the administration of justice than the invalidation of convictions because of disregard of individual rights or official overreaching. In our view the officers in this case did what the Constitution requires. They obtained a warrant from a judicial officer "upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the . . . things to be seized." It is vital that having done so their actions should be sustained under a system of justice responsive both to the needs of individual liberty and to the rights of the community.</p>
<p><i>Reversed.</i></p>
<p></p>
<h2>APPENDIX TO OPINION OF THE COURT.</h2>
<p></p>
<h2>AFFIDAVIT FOR SEARCH WARRANT</h2>
<p>BEFORE W. ARTHUR GARRITY, Worcester, Massachusetts The undersigned being duly sworn deposes and says:</p>
<p>That he has reason to believe that on the premises known as a one-family light green wooden frame dwelling house located at 148 1/2 Coburn Avenue, Worcester, occupied by Giacomo Ventresca and his family, together with all approaches and appurtenances thereto, in the District of Massachusetts, there is now being concealed certain property, namely an unknown quantity of material and certain apparatus, articles and devices, including a still and distilling apparatus setup with all attachments thereto, together with an unknown quantity of mash, an unknown quantity of distilled spirits, and other material used in the manufacture of non-tax-paid liquors; which are being held and possessed, and which have been used and are intended for use, in the distillation, manufacture, possession, and distribution of non-tax-paid liquors, in violation of the provisions of 26 USC 5171 (a), 5173, 5178, 5179 (a), 5222 (a), 5602, and 5686.</p>
<p><span class="star-pagination">*113</span> And that the facts tending to establish the foregoing grounds for issuance of a Search Warrant are as follows:</p>
<p>SEE ATTACHED SHEET</p>
                  /s/ WALTER A. MAZAKA
                  <i>Investigator, Alcohol and
                      Tobacco Tax Div., Internal
                      Revenue Service</i>
<p>Sworn to before me, and subscribed in my presence, August 31st, 1961</p>
                   /s/ W. ARTHUR GARRITY
                   <i>United States Commissioner</i>
<p>Based upon observations made by me, and based upon information received officially from other Investigators attached to the Alcohol and Tobacco Tax Division assigned to this investigation, and reports orally made to me describing the results of their observations and investigation, this request for the issuance of a search warrant is made.</p>
<p>On or about July 28, 1961, about 6:45 P.M., an observation was made covering a Pontiac automobile owned by one Joseph Garry. Garry and one Joseph Incardone put thirteen bags of sugar into the car. These bags of sugar weighed sixty pounds each. Ten such bags were put into the trunk, and three were placed in the rear seat. Those in the rear seat were marked "Domino." The others appeared to have similar markings. After the sugar was loaded into the car, Garry together with Incardone drove it to the vicinity of 148 Coburn Avenue, Worcester, Massachusetts, where the car was parked. Sometime later, the car with its contents was driven into the yard to the rear of 148 and between the premises 148 and 148 1/2 Coburn Avenue. After remaining there about twentyfive minutes, the same two men drove in the direction of Boston.</p>
<p><span class="star-pagination">*114</span> On August 2, 1961 a Pontiac car owned by Garry, and driven by Garry with Incardone as a passenger, was followed from Boston to Worcester. The car appeared heavily laden. The car was again driven into the driveway at 148 and 148 1/2 Coburn Avenue to the rear of the yard and between the above-numbered houses.</p>
<p>On August 7, 1961 at least six sixty-pound bags of Domino Sugar were loaded into the Pontiac owned by Garry. The loading was done by Garry and Incardone. The car traveled from Boston to Worcester, then to Holden, and returned with its contents and entered the driveway at 148 and 148 1/2 Coburn Avenue, where the car was parked at the rear between the two houses.</p>
<p>On August 11, 1961 new empty metal or tin cans were transferred from a car owned by Incardone to the Pontiac owned by Garry on Highland Street in Hyde Park. The Pontiac was driven by Garry with Incardone as a passenger to Worcester, and into the yard at 148 and 148 1/2 Coburn Avenue to the rear and between the two numbered premises.</p>
<p>On August 16, 1961 the Pontiac was observed. In the back seat bags of sugar were observed covered with a cloth or tarpaulin. A sixty-pound bag of sugar was on the front seat. Garry was observed after loading the above-described sugar into the car placing a carton with various five-pound bags of sugar on the top of the tarpaulin. The car was then driven by Garry with Incardone as a passenger to Worcester together with its contents into the yard at 148 and 148 1/2 Coburn Avenue to the rear of and between the two houses. About Midnight on the same night, the Pontiac driven by Garry with Incardone as a passenger was seen pulling up to the premises at 59 Highland Street, Hyde Park, where Garry lives. Garry opened the trunk of his car, and removed ten five-gallon cans therefrom, and placed them on the sidewalk. He then entered the house, and opened a door on the side. <span class="star-pagination">*115</span> Incardone made five trips from the sidewalk to the side of the house carrying two five-gallon cans on each such trip. It appeared that the cans were filled. On each of these trips, Incardone passed the two cans to someone standing in the doorway. Immediately after the fifth such trip, Garry came out of the door and joined Incardone. They walked to the sidewalk, and talked for a few moments. Incardone then drove away, and Garry went into his home.</p>
<p>On August 18, 1961 Investigators smelled an odor of fermenting mash on two occasions between 4:00 A.M. and 5:00 A.M. The first such odor was detected as they walked along the sidewalk in front of 148 Coburn Avenue, and the second such odor was detected from the side of 148 Coburn Avenue. At or about the same time, the Investigators heard certain metallic noises which cannot be further identified by source or sound.</p>
<p>On August 24, 1961 the Pontiac was observed parked at a bowling alley and coffee shop off Route 9. The back of the car contained what appeared to be boxes covered by a cloth or tarpaulin, but which cannot be more specifically identified. On the front seat of the car was observed a sixty-pound bag of Revere Sugar. Garry and Incardone were observed in the restaurant or coffee shop eating. Later the car was seen driven to the rear of 148 between 148 and 148 1/2 Coburn Avenue, Worcester.</p>
<p>About Midnight the Pontiac was observed pulling up in front of Garry's house at 59 Highland Street, Hyde Park. Garry was driving, and Incardone was a passenger. They both got out of the car. Garry opened the trunk, and then entered his house. From the trunk of the car there was removed eleven five-gallon cans which appeared to be filled. Incardone made six trips to a door on the side of the house. He carried two five-gallon cans on each trip, except the sixth trip. On that trip he carried one can, having passed the others to somebody in the door-way, <span class="star-pagination">*116</span> and on the last trip he entered the house. He remained there at least forty-five minutes, and was not observed to leave.</p>
<p>On August 28, 1961 Garry drove Incardone in his car to Worcester. On Lake Ave. they met Giacomo Ventresca, who lives at 148 1/2 Coburn Avenue, Worcester. Ventresca entered the car driven by Garry. The car was then driven into the yard to the rear of 148 and between 148 and 148 1/2 Coburn Avenue. An observation was made that empty metal cans, five-gallon size, were being taken from the car owned by Garry, and brought into the premises at 148 1/2 Coburn Avenue, which was occupied by Ventresca. Later, new cans similar in size, shape and appearance were observed being placed into the trunk of Garry's car while parked at the rear of 148 and in front of 148 1/2 Coburn Avenue. The manner in which the cans were handled, and the sound[s] which were heard during the handling of these cans, were consistent with that of cans containing liquid.</p>
<p>On August 30, 1961, at about 4:00 A.M., an odor of fermenting mash was detected while Investigators were walking on the sidewalk in front of 148 Coburn Avenue. At the same time, they heard sounds similar to that of a motor or a pump coming from the direction of 148 1/2 Coburn Avenue.</p>
<p>The foregoing information is based upon personal knowledge and information which has been obtained from Investigators of the Alcohol and Tobacco Tax Division, Internal Revenue Service, who have been assigned to this investigation.</p>
                         /s/ WALTER A. MAZAKA
<p>MR. JUSTICE DOUGLAS, with whom THE CHIEF JUSTICE concurs, dissenting.</p>
<p>With all deference, the present affidavit seems hopelessly inadequate to me as a basis for a magistrate's <span class="star-pagination">*117</span> informed determination that a search warrant should issue.</p>
<p>We deal with the constitutional right of privacy that can be invaded only on a showing of "probable cause" as provided by the Fourth Amendment. That is a strict standard; what the police say does not necessarily carry the day; "probable cause" is in the keeping of the magistrate. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486-487</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>. Yet anything he says does not necessarily go either. He too is bound by the Constitution. His discretion is reviewable. <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/#111" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108, 111</a></span>. But unless the constitutional standard of "probable cause" is defined in meticulous ways, the discretion of police and of magistrates alike will become absolute. The present case, illustrates how the mere weight of lengthy and vague recitals takes the place of reasonably probative evidence of the existence of crime.</p>
<p></p>
<h2>I.</h2>
<p>Investigator Mazaka sought a warrant for the purpose of searching the premises at 148 1/2 Coburn Avenue, occupied by respondent and his family, because, he averred, he had reason to believe that there was concealed on the premises an illegal still and other material connected with the manufacture of nontax-paid liquors. The grounds for this belief were recited in 12 paragraphs on an attached sheet, as reproduced in the Appendix to the Court's opinion, <i>ante,</i> p. 112.</p>
<p>The factual recitals comprise 10 paragraphs, each paragraph setting forth the alleged events of a single day, except that August 24, 1961, is dealt with in two paragraphs. Of these factual recitals more will be said in a moment. The first and last paragraphs of the 12 describe the sources from which the affiant has gained the information set forth in the factual paragraphs. These sources are, according to the first paragraph, three in <span class="star-pagination">*118</span> number: (1) "observations made by me"; (2) "information received officially from other Investigators"; and (3) "reports orally made to me [by other investigators] describing the results of their observations and investigation." In the last paragraph the affiant describes the sources of his information slightly differently: "The foregoing information is based upon personal knowledge and information which has been obtained from Investigators . . . ."</p>
<p>Of the 10 factual paragraphs eight describe trips said to have been made to and from the vicinity of 148 1/2 Coburn Avenue by one Garry and one Incardone. On these trips, it is said, there were delivered to the vicinity of 148 1/2 Coburn Avenue large quantities of sugar (four deliveries) and empty metal cans (two deliveries, on one of which respondent himself is said to have been a passenger in the car); on one occasion it was observed only that the car was "heavily laden." It is said that on two occasions Garry and Incardone were seen taking apparently filled cans into Garry's house, 59 Highland Street, from the Pontiac; on one such occasion the Pontiac, it is said, had been at Coburn Avenue earlier in the day, apparently making a sugar delivery. And, finally, it is averred that on one occasion seemingly filled cans were loaded into the Pontiac near 148 1/2 Coburn Avenue, shortly after a delivery of empties to that address.</p>
<p>The "facts" recited in these eight paragraphs, it is said, permit the inference that a still was being operated on respondent's premises. But are these "facts" really facts? A statement of "fact" is only as credible as its source. Investigator Mazaka evidently believes these statements to be correct; but the magistrate must, of course, know something of the basis of that belief. <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span>. Is the belief of this affiant based on personal observation, or on hearsay, or on hearsay on hearsay? Nowhere in the affidavit is the source <span class="star-pagination">*119</span> of these eight paragraphs of information revealed. In each paragraph the alleged events are simply described directly, or else it is said that certain events "were observed." Scarcely a clue is given as to who the observer might have been. It might have been the affiant, though one would not expect that he would so studiously refrain from revealing that he himself witnessed these events. The observers might have been some other investigators, though the affiant does not say so; yet in the two paragraphs next to be discussed the observers are prominently identified as investigators. Perhaps the ultimate source of most of these statements was one or more private citizens, who were interviewed by investigators, whose reports on these interviews came in due course to Investigator Mazaka, who then composed the affidavit. Perhaps many of the "facts" recited in the affidavit were supplied by an unknown informant over the telephone.</p>
<p>In most instances the language of the affidavit suggests that some investigator witnessed the alleged events. For example, the second paragraph begins: "On or about July 28, 1961, about 6:45 P. M., an observation was made covering a Pontiac automobile owned by one Joseph Garry." But the presumed investigator who may have been "covering" this automobile is in no way identified. There is no way of knowing whether the report of this alleged observation was made directly to the affiant or whether it went through one or more intermediaries.</p>
<p>Turning now to the remaining two "factual" paragraphs, we find it averred that "Investigators" smelled fermenting mash and heard metallic and other noises in the vicinity of 148 1/2 Coburn Avenue. On August 18, it is said, investigators twice smelled mash between 4 and 5 a. m. as they walked on the sidewalk in front of and beside the house at 148 Coburn Avenue, which is apparently the house next to respondent's. The "Investigators" are not further identified. On August 30 at about 4 a. m., it <span class="star-pagination">*120</span> is averred, unidentified investigators detected the odor of fermenting mash while they were "walking on the sidewalk in front of 148 Coburn Avenue." The source of the odor is again not specified; but sounds heard at the same time, similar to the sounds made by "a motor or a pump," are stated to have come "from the direction of 148 1/2 Coburn Avenue."</p>
<p>Such is the substance of the affidavit. No particular item of information is identified as within the first-hand knowledge of the affiant. Certain smells and sounds are explicitly described as having been directly perceived by unnamed investigators. The sources of all the other information are left to speculation.</p>
<p>The Court's unconcern over the failure of the affidavit to identify the sources of the information recited seems based in part on the detailed, lengthy nature of the factual recitals. The Court seems to say that even if we assume that only some small part of the information is trustworthy, still enough remains to establish probable cause. But I would direct attention to the fact that only <i>one</i> of the 12 paragraphs in this affidavit definitely points the finger of suspicion at 148 1/2 Coburn Avenue: that is the paragraph describing the alleged events of August 28, 1961. In every other paragraph the recitals point no more to <i>148</i> 1/2 Coburn Avenue than they do to <i>148</i> Coburn Avenue. The August 28 paragraph is critical to the finding of the existence of probable cause for the search of 148 1/2 Coburn Avenue. Yet the source of the information contained in that paragraph is in no way identified and it is therefore impossible to determine the trust-worthiness of that crucial information.</p>
<p></p>
<h2>II.</h2>
<p>A discussion of the legal principles governing the sufficiency of this affidavit must, unhappily, begin with <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span>. There an officer <span class="star-pagination">*121</span> had been told by an informer, known to the officer to be reliable, that a man of a certain description would get off a certain train with heroin in his possession. The officer met the train, observed a man of that description getting off, and arrested him. The Court held that there was probable cause for the arrest. In <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>, the Court applied the holding in <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> to find an affidavit sufficient to establish probable cause for the issuance of a search warrant, even though the facts stated in the affidavit did not rest on the affiant's personal observations but rather on the observations of another. The Court held that an affidavit could rest on hearsay, <i>"so long as a substantial basis for crediting the hearsay is presented." Id.,</i> at 269. (Emphasis supplied.) In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> the basis for crediting the informant's hearsay was: (1) the affiant swore that the informant had previously given information to him which was correct; (2) the affiant had been given corroborating information by other informants; and (3) the affiant was independently familiar with the persons claimed by the informants to be concealing narcotics in their apartment, and he knew them to have admitted to the use of narcotics.</p>
<p>I dissented from the decisions of the Court in these two cases, for the reasons which I set forth most fully in <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper, supra,</a></span></i> at 314 <i>et seq.</i> But though I regard these decisions<sup>[*]</sup> as taking a view destructive of the guarantees of the Fourth Amendment, they are in any event clearly not dispositive of the present case. As I have already shown, the affidavit here does not set forth a single corroborating <span class="star-pagination">*122</span> fact that is sworn to be within the personal knowledge of the affiant. Moreover, there is not a single statement in the affidavit that could not well be hearsay on hearsay or some other multiple form of hearsay.</p>
<p>We are told, however, that it is at least clear that "Investigators" detected the smell of mash in the vicinity of 148 1/2 Coburn Avenue. And the Court says: "Observations of fellow officers of the Government engaged in a common investigation are plainly a reliable basis for a warrant applied for by one of their number," <i>ante,</i> p. 111. But I would make <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States">286 U. S. 1, 6</a></span>, my starting point, where the Court stated: "Prohibition officers may rely on a distinctive odor as a physical fact indicative of possible crime; but its presence alone does not strip the owner of a building of constitutional guarantees against unreasonable search." In <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13</a></span>, the Court explained what the decision in <i><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span></i> meant: "That decision held only that odors alone do not authorize a search without warrant. If the presence of odors is testified to before a magistrate <i>and he finds the affiant qualified to know the odor,</i> and it is one sufficiently distinctive to identify a forbidden substance, this Court has never held such a basis insufficient to justify issuance of a search warrant." (Emphasis supplied.) It is hardly necessary to point out that a magistrate cannot begin to assess the odor-identifying qualifications of persons whose identity is unknown to him. Nor is it necessary to belabor the point that these odors of mash are not ever stated in the affidavit to have emanated from 148 1/2 Coburn Avenue.</p>
<p></p>
<h2>III.</h2>
<p>The Court of Appeals was surely correct when it observed that "the affidavit leaves as a complete mystery the manner in which the Investigators discovered their information." <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/#869" aria-description="Citation for case: Giacomo Ventresca v. United States">324 F. 2d 864, 869</a></span>. Such being the case, <span class="star-pagination">*123</span> I see no way to avoid the conclusion of the majority below: "If hearsay evidence is to be relied upon in the preparation of an affidavit for a search warrant, the officer or attorney preparing such an affidavit should keep in mind that hearsay statements are only as credible as their source and only as strong as their corroboration. And where the source of the information is in doubt and the corroboration by the affiant is unclear, the affidavit is insufficient." <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/#869" aria-description="Citation for case: Giacomo Ventresca v. United States"><i>Id.,</i> at 869-870</a></span>. That conclusion states a relatively clear standard of probable cause and is in sharp contrast to the amorphous one upon which today's decision rests.</p>
<p>In <i>Jones</i> v. <i>United States, supra</i><i>,</i> this Court forgot, as it forgets again today, that the duty of the magistrate is not delegable to the police. <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span>. It is for the magistrate, not the police, to decide whether there is probable cause for the issuance of the warrant. That function cannot be discharged by the magistrate unless the police first discharge their own, different responsibility: "to evidence what is reliable and why, and not to introduce a hodge-podge under some general formalistic coverall." <span class="citation" data-id="9449711"><a href="/opinion/262427/giacomo-ventresca-v-united-states/#870" aria-description="Citation for case: Giacomo Ventresca v. United States">324 F. 2d, at 870</a></span>. And see <i>Masiello</i> v. <i>United States,</i> <span class="citation" data-id="9448604"><a href="/opinion/257500/franklin-r-masiello-v-united-states/#401" aria-description="Citation for case: Franklin R. Masiello v. United States">304 F. 2d 399, 401-402</a></span>. <i>That</i> is the duty of the policethe rest is not for them.</p>
<p>I would affirm the decision below.</p>
<h2>NOTES</h2>
<p>[1]  The Fourth Amendment's policy against unreasonable searches and seizures finds expression in Rule 41 of the Federal Rules of Criminal Procedure.</p>
<p>[2]  The exceptions are illustrated by cases in which "seizure is impossible except without warrant," <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156</a></span>, such as a search of a moving object where "it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought," <i>Carroll</i> v. <i>United States, supra,</i> at 153, and those in which search is incident to a lawful arrest. This latter exception is itself a limited one. We stated in <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span>:
</p>
<p>"Unquestionably, when a person is lawfully arrested, the police have the right, without a search warrant, to make a contemporaneous search of the person of the accused for weapons or for the fruits of or implements used to commit the crime. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914); <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span> (1925). This right to search and seize without a search warrant extends to things under the accused's immediate control, <i>Carroll</i> v. <i>United States, supra,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#158" aria-description="Citation for case: Carroll v. United States">267 U. S., at 158</a></span>, and, to an extent depending on the circumstances of the case, to the place where he is arrested, <i>Agnello</i> v. <i>United States, supra,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S., at 30</a></span>; <i>Marron</i> v. <i>United States,</i> <span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#199" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 199</a></span> (1927); <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#61" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 61-62</a></span> (1950). The rule allowing contemporaneous searches is justified, for example, by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crimethings which might easily happen where the weapon or evidence is on the accused's person or under his immediate control. But these justifications are absent where a search is remote in time or place from the arrest. Once an accused is under arrest and in custody, then a search made at another place, without a warrant, is simply not incident to the arrest." <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S., at 367</a></span>.</p>
<p>[3]  See, <i>e. g., </i><i>Monnette</i> v. <i>United States,</i> <span class="citation" data-id="256395"><a href="/opinion/256395/maynard-paul-monnette-and-robert-christianson-noreng-v-united-states/#850" aria-description="Citation for case: Maynard Paul Monnette and Robert Christianson Noreng v....">299 F. 2d 847, 850</a></span> (C. A. 5th Cir.). Cf. <i>Chapman</i> v. <i>United States,</i> <span class="citation" data-id="9422156"><a href="/opinion/106197/chapman-v-united-states/" aria-description="Citation for case: Chapman v. United States">365 U. S. 610</a></span>; <i>Steeber</i> v. <i>United States,</i> <span class="citation" data-id="230030"><a href="/opinion/230030/steeber-v-united-states/#616" aria-description="Citation for case: Steeber v. United States">198 F. 2d 615, 616, 618</a></span> (C. A. 10th Cir.); <i>United States</i> v. <i>Kaplan,</i> <span class="citation" data-id="1472811"><a href="/opinion/1472811/united-states-v-kaplan/" aria-description="Citation for case: United States v. Kaplan">89 F. 2d 869</a></span> (C. A. 2d Cir.).</p>
<p>[4]  See, <i>e. g., </i><i>Rugendorf</i> v. <i>United States,</i> <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span>; <i>Chin Kay</i> v. <i>United States,</i> <span class="citation" data-id="9448973"><a href="/opinion/259093/chin-kay-v-united-states/#320" aria-description="Citation for case: Chin Kay v. United States">311 F. 2d 317, 320</a></span> (C. A. 9th Cir.); <i>United States</i> v. <i>McCormick,</i> <span class="citation" data-id="258571"><a href="/opinion/258571/united-states-v-james-waldo-mccormick/#372" aria-description="Citation for case: United States v. James Waldo McCormick">309 F. 2d 367, 372</a></span> (C. A. 7th Cir.); <i>Weise</i> v. <i>United States,</i> <span class="citation" data-id="244128"><a href="/opinion/244128/moe-weise-and-james-lester-french-v-united-states/#868" aria-description="Citation for case: Moe Weise and James Lester French v. United States">251 F. 2d 867, 868</a></span> (C. A. 9th Cir.).</p>
<p>[*]  In these cases we might have drawn a clear, unmistakable line and held that hearsay evidence could not support a search warrant. But we did not so hold; instead we held that hearsay was competent for this purpose if there was "a substantial basis" for crediting it, thereby muddying the waters with considerations of corroboration and informer's reliability. Thus, by forsaking precise standards, the discretion of police and magistrates became less subject to judicial control.</p>

</div>
```

---

## GROUP: content/cases/United States v. Vinton.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Vinton"
type: case
citation: "594 F.3d 14 (2010)"
parallel_cite: 389 U.S. App. D.C. 199
neutral_cite: "2010 U.S. App. LEXIS 2450; 2010 WL 392347"
court: "U.S. Court of Appeals, District of Columbia Circuit"
court_level: coa
circuit: D.C.
year: 2010
date_decided: 2010-02-05
docket: ""
authority_weight: "Binding in-circuit — D.C. Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2010-02-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Vinton
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/187527/united-states-v-vinton/"
  cluster_id: 187527
  opinion_id: 187527
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
related: ["[[Michigan v. Long]]", "[[Arizona v. Gant]]", "[[Terry v. Ohio]]"]
aliases: ["United States v. Vinton (D.C. Cir. 2010)"]
tags: ["case", "fourth-amendment", "traffic-stop", "protective-search", "michigan-v-long", "arizona-v-gant", "dc-circuit"]
holding: "Gant's 'secured arrestee' limitation does not abate a Michigan v. Long protective (Terry) vehicle search: the protective-search…"
lake:
  record_id: United States v. Vinton
  status: verified
  projected_at: 2026-07-06
---

# United States v. Vinton

*594 F.3d 14 (D.C. Cir. 2010)* · U.S. Court of Appeals, District of Columbia Circuit · **Binding in-circuit — D.C. Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a traffic stop, Officer Aton saw a sheathed knife in plain view in Vinton's car and removed it, placing it on the roof. A locked briefcase sat on the backseat. Considering the knife, a "thin blue line" sticker that could suggest a false law-enforcement affiliation, and knowledge of a recent nearby double-stabbing, Aton conducted a protective search of the passenger compartment, then arrested and handcuffed Vinton and pried open the locked briefcase, finding contraband and a firearm. While Vinton's appeal was pending, the Supreme Court decided *[[Arizona v. Gant]]*; Vinton argued *[[Arizona v. Gant|Gant]]* required suppression.

## Issue
Whether a protective search of a vehicle's passenger compartment for weapons under *[[Michigan v. Long]]* remains valid after the suspect has been removed and handcuffed, and whether *[[Arizona v. Gant]]*'s limits on [[Search Incident to Arrest|searches incident to arrest]] displace that protective-search authority.

## Rule
A *[[Michigan v. Long]]* protective search of the passenger compartment is justified by reasonable suspicion that the driver is dangerous and could gain access to weapons, and that justification is not eliminated by securing the suspect: "This concern was not abated by ordering Vinton out of the car and handcuffing him, because had Vinton ultimately not been arrested, he would have been 'permitted to reenter his automobile, and he w[ould] then have [had] access to any weapons inside.'" — *United States v. Vinton*, 594 F.3d 14, 20 (D.C. Cir. 2010). ^pin-20

Applying that standard, the court upheld the search: "Examining the totality of the circumstances objectively, Officer Aton had a reasonable belief, based on specific and articulable facts, that Vinton was armed and dangerous. . . . Thus, he properly searched the passenger compartment of Vinton's car for additional weapons." — *Id.* at 21. ^pin-21

## Application
Vinton's visible knife, the misleading "thin blue line" sticker, and the recent nearby stabbing gave Officer Aton reasonable suspicion that Vinton was armed and dangerous. Although Vinton had been handcuffed, the protective-search rationale persisted: if released rather than arrested, Vinton could re-enter the car and reach concealed weapons — so *[[Arizona v. Gant|Gant]]*'s limits on vehicle [[Search Incident to Arrest|searches incident to arrest]] did not bar the protective search of the passenger compartment. The court separately upheld prying open the locked briefcase under *[[Arizona v. Gant|Gant]]*'s evidentiary rationale, reasoning it was reasonable to believe evidence relevant to the crime of arrest might be found inside.

## Conclusion
The protective search of the passenger compartment was valid under *[[Michigan v. Long|Long]]* despite Vinton's having been handcuffed, and opening the briefcase was valid under *[[Arizona v. Gant|Gant]]*'s evidentiary rationale; the D.C. Circuit affirmed the denial of suppression.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — D.C. Cir.**
- No negative treatment. *Vinton* confirms that [[Arizona v. Gant]]'s limits on vehicle [[Search Incident to Arrest|searches incident to arrest]] do not displace the independent protective-search authority of [[Michigan v. Long]]: an officer with reasonable suspicion that the driver is armed and dangerous may search the passenger compartment for weapons even after the driver is secured.

## Appears on
- [[Traffic Stops]] — *Key — Progeny / Refinement*

## Sources
- *United States v. Vinton*, 594 F.3d 14 (D.C. Cir. 2010) — https://www.courtlistener.com/opinion/187527/united-states-v-vinton/ — pinpoints: 20, 21 (parallel 389 U.S. App. D.C. 199).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9c5b3b46c47bd86e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "594 F.3d 14 (2010)", "court": "U.S. Court of Appeals, District of Columbia Circuit", "neutral_cite": "2010 U.S. App. LEXIS 2450; 2010 WL 392347", "official_citation_present": true, "parallel_cite": "389 U.S. App. D.C. 199", "title": "United States v. Vinton", "year": "2010"}}
{"assertion_id": "73405c832afda363", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Gant's 'secured arrestee' limitation does not abate a Michigan v. Long protective (Terry) vehicle search: the protective-search…", "title": "United States v. Vinton"}}
{"assertion_id": "90b1451000fb8e28", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Progeny / Refinement", "title": "United States v. Vinton"}}
{"assertion_id": "1e51c6bcc76f5d1a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2010-02-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Vinton", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "United States v. Vinton", "varies_by_point": "false"}}
{"assertion_id": "9bbaa0df23b022d4", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — D.C. Cir.", "title": "United States v. Vinton"}}
```

### lake record — United States v. Vinton

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Vinton",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Vinton",
    "case_name_short": "Vinton",
    "case_name_full": "UNITED STATES of America, Appellee v. Samuel H. VINTON, Jr., Appellant",
    "input_case_name": "United States v. Vinton",
    "court": "U.S. Court of Appeals, District of Columbia Circuit",
    "court_id": "cadc",
    "court_level": "coa",
    "circuit": "D.C.",
    "state": null,
    "date_decided": "2010-02-05",
    "year": 2010,
    "docket": null,
    "cluster_id": 187527,
    "lead_opinion_id": 187527,
    "sibling_ids": [
      187527
    ],
    "absolute_url": "/opinion/187527/united-states-v-vinton/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "594 F.3d 14",
      "volume": "594",
      "reporter": "F.3d",
      "page": "14",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "389 U.S. App. D.C. 199",
        "volume": "389",
        "reporter": "U.S. App. D.C.",
        "page": "199",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. App. LEXIS 2450",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "2450",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 392347",
        "volume": "2010",
        "reporter": "WL",
        "page": "392347",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "594 F.3d 14",
        "volume": "594",
        "reporter": "F.3d",
        "page": "14",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "389 U.S. App. D.C. 199",
        "volume": "389",
        "reporter": "U.S. App. D.C.",
        "page": "199",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. App. LEXIS 2450",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "2450",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 392347",
        "volume": "2010",
        "reporter": "WL",
        "page": "392347",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "594 F.3d 14",
    "official_selection": {
      "court_class": "coa",
      "selected": "594 F.3d 14",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-20",
      "page": null,
      "quote": "sticker that could suggest a false law-enforcement affiliation, and knowledge of a recent nearby double-stabbing, Aton conducted a protective search of the passenger compartment, then arrested and handcuffed Vinton and pried open the locked briefcase, finding contraband and a firearm. While Vinton's appeal was pending, the Supreme Court decided *Arizona v. Gant*; Vinton argued *Gant* required suppression. ## Issue Whether a protective search of a vehicle's passenger compartment for weapons under *Michigan v. Long* remains valid after the suspect has been removed and handcuffed, and whether *Arizona v. Gant*'s limits on searches incident to arrest displace that protective-search authority. ## Rule A *Michigan v. Long* protective search of the passenger compartment is justified by reasonable suspicion that the driver is dangerous and could gain access to weapons, and that justification is not eliminated by securing the suspect:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-21",
      "page": null,
      "quote": "Examining the totality of the circumstances objectively, Officer Aton had a reasonable belief, based on specific and articulable facts, that Vinton was armed and dangerous. . . . Thus, he properly searched the passenger compartment of Vinton's car for additional weapons.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2010-02-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Vinton",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Iowa v. Jesse Michael Gaskins",
          "cluster_id": 2812905,
          "cite": [
            "866 N.W.2d 1",
            "2015 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Evans",
          "cluster_id": 5810664,
          "cite": [
            "200 Cal. App. 4th 735",
            "133 Cal. Rptr. 3d 323",
            "2011 Cal. App. LEXIS 1382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dante Sheffield",
          "cluster_id": 4246586,
          "cite": [
            "832 F.3d 296",
            "101 Fed. R. Serv. 182",
            "2016 U.S. App. LEXIS 14826",
            "2016 WL 4254995"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rodgers",
          "cluster_id": 613267,
          "cite": [
            "656 F.3d 1023",
            "2011 U.S. App. LEXIS 18564",
            "2011 WL 3907115"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Polanco",
          "cluster_id": 204415,
          "cite": [
            "634 F.3d 39",
            "2011 U.S. App. LEXIS 2411",
            "2011 WL 420747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Donahue",
          "cluster_id": 2720208,
          "cite": [
            "764 F.3d 293",
            "2014 U.S. App. LEXIS 16221",
            "2014 WL 4115949"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gerry Burnett",
          "cluster_id": 4236825,
          "cite": [
            "424 U.S. App. D.C. 42",
            "827 F.3d 1108",
            "2016 U.S. App. LEXIS 12549"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortes v. State",
          "cluster_id": 2458832,
          "cite": [
            "260 P.3d 184",
            "127 Nev. 505",
            "127 Nev. Adv. Rep. 44",
            "2011 Nev. LEXIS 46"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Justin Edwards",
          "cluster_id": 2739791,
          "cite": [
            "769 F.3d 509",
            "2014 U.S. App. LEXIS 18985",
            "2014 WL 4977492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Davon Peyton",
          "cluster_id": 2657561,
          "cite": [
            "409 U.S. App. D.C. 26",
            "745 F.3d 546",
            "2014 WL 1099576",
            "2014 U.S. App. LEXIS 5296"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "OLANIYI v. District of Columbia",
          "cluster_id": 2472991,
          "cite": [
            "763 F. Supp. 2d 70",
            "2011 U.S. Dist. LEXIS 10953",
            "2011 WL 339215"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Williams",
          "cluster_id": 2662144,
          "cite": [
            "878 F. Supp. 2d 190",
            "2012 WL 2951386",
            "2012 U.S. Dist. LEXIS 100618"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Davis",
          "cluster_id": 4881258,
          "cite": [
            "997 F.3d 191"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sheffield",
          "cluster_id": 2114119,
          "cite": [
            "799 F. Supp. 2d 22",
            "2011 U.S. Dist. LEXIS 106177",
            "2011 WL 4363893"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Guerrero",
          "cluster_id": 5303613,
          "cite": [
            "19 F.4th 547"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. King",
          "cluster_id": 1223116,
          "cite": [
            "696 S.E.2d 913",
            "206 N.C. App. 585",
            "2010 N.C. App. LEXIS 1555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Fischer",
          "cluster_id": 3167754,
          "cite": [
            "2016 SD 1",
            "873 N.W.2d 681",
            "2016 S.D. LEXIS 3",
            "2016 WL 97324"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 4403321,
          "cite": [
            "256 F. Supp. 3d 15",
            "2017 WL 2728393",
            "2017 U.S. Dist. LEXIS 97127"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Taylor v. State",
          "cluster_id": 2831720,
          "cite": [
            "224 Md. App. 476",
            "121 A.3d 167",
            "2015 Md. App. LEXIS 124"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terrell Armstead",
          "cluster_id": 10103154,
          "cite": [
            "116 F.4th 519"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Eversole",
          "cluster_id": 4440680,
          "cite": [
            "2017 Ohio 8436"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Vinton:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(187527) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR cadc)",
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
      },
      "lane2_top_cited": {
        "query": "cites:(187527)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9Nzg1OTgyNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28187527%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 21,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(187527)",
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
    "complete_query": "cites:(187527)",
    "indexed_citing_opinions": 58,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 187527,
        "count": 58,
        "count_source": "search"
      }
    ],
    "citation_count": 121,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-vinton.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2MTgxODcmcz00NDQwNjgwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28187527%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 187527,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 111378,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 112873,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 118474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 137733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 145887,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 145912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 184963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 185969,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 186083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 186738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 186847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 187086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 187317,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 507145,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 187527,
        "cited_id": 777993,
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
    "date_created": "2026-07-06T03:22:46Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:22:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:22:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:26:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:22:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Vinton

```
 United States Court of Appeals
         FOR THE DISTRICT OF COLUMBIA CIRCUIT



Argued December 10, 2009           Decided February 5, 2010

                        No. 07-3125

                UNITED STATES OF AMERICA,
                        APPELLEE

                             v.

                  SAMUEL H. VINTON, JR.,
                      APPELLANT


        Appeal from the United States District Court
                for the District of Columbia
                     (No. 06cr00298-01)



    Beverly G. Dyer, Assistant Federal Public Defender,
argued the cause for appellant. With her on the briefs was A.
J. Kramer, Federal Public Defender. Neil H. Jaffee, Assistant
Federal Public Defender, entered an appearance.

    James M. Perez, Assistant U.S. Attorney, argued the
cause for appellee. With him on the brief were Roy W.
McLeese III and Mary B. McCord, Assistant U.S. Attorneys.

   Before: BROWN and KAVANAUGH, Circuit Judges, and
WILLIAMS, Senior Circuit Judge.
                              2


    Opinion for the court filed by Circuit Judge BROWN.

     BROWN, Circuit Judge: Samuel Vinton, convicted of
narcotics and firearm offenses after the contraband was found
in a briefcase in his car during a traffic stop, appeals the
denial of his motion to suppress. He argues the evidence was
discovered during an unconstitutional search of his vehicle
and property. In particular, he contends that Arizona v. Gant,
129 S. Ct. 1710 (2009), decided by the Supreme Court while
this appeal was pending, establishes that the search of the
briefcase cannot be upheld under the search-incident-to-arrest
exception to the warrant requirement. Because it was
“reasonable to believe” evidence relevant to Vinton’s
weapons-possession offense would be found inside the
briefcase, we affirm.

                              I

     On September 9, 2006, around 9:00 p.m., U.S. Park
Police Officer William Alton, driving a marked cruiser in
Southeast D.C., saw a green Nissan Maxima speeding, and
also observed that its windows were excessively tinted. Tr. of
Mot. Hr’g at 6, 8, 69, United States v. Vinton, No. 06-cr-298
(D.D.C. Feb. 9, 2007) (Suppression Tr.). As Alton followed
the car, he noticed “a thin blue line sticker on the back of
[the] car,” which Alton assumed referred to the driver’s
probable affiliation with law enforcement, most likely the
Metropolitan Police Department (MPD). Id. at 8, 70.

     The driver promptly obeyed Alton’s signal to pull over
and, as Alton approached the car, the driver, Vinton, lowered
all his windows. Id. at 10, 70. Alton asked if Vinton was in
law enforcement and Vinton said he worked in “personal
security.” Id. at 11, 71. Alton immediately saw a knife with
                               3

a five-and-a-half inch sheath on Vinton’s backseat, in “close
proximity” to Vinton, easily within reaching-distance. Id. at
11–12, 25, 37, 70–71. Vinton explained the knife was used
when fishing with his grandfather, but Alton saw no other
fishing equipment in the car. Id. at 12, 14, 71. He retrieved
the knife and placed it on the roof of the car, “out of arm’s
reach of the driver.” Id. at 14, 71. Alton asked if there were
“any other weapons in the vehicle,” and Vinton responded
“no, he . . . ke[pt] that part of his trade at home.” Id. at 14,
71. Alton then measured the car’s windows with a tint meter
and determined they exceeded D.C.’s seventy-percent tint
limit. Id. at 15–17, 71. He returned to his cruiser to prepare a
citation. Id. at 17, 72.

     Officer Alton was working alone and had not called for
Park Police backup. However, when an MPD officer
appeared, Alton “asked him to stop” because he had found a
large knife and desired assistance in conducting a protective
search of the car. Id. at 19–20, 72. The officer told Alton
there had been a double-stabbing homicide in the same
vicinity approximately twenty hours earlier. Id. at 20, 72.
Alton told Vinton he was going to conduct a search for
weapons and asked twice more whether there were any
weapons in the car; Vinton first responded “no” but then
responded, “not that I know of.” Id. at 22, 73. Alton
removed Vinton from the car and handcuffed him, but
informed him he was not under arrest. Id. at 22, 73. A search
of the passenger compartment of the car revealed two cans of
mace in the front armrest, a “butterfly knife” under the front
passenger-side floor mat, a bag of Styrofoam earplugs, and a
locked briefcase on the backseat. Id. at 23–24, 26, 73–74.
Vinton claimed he used the earplugs as sleeping aids and said
the briefcase did not belong to him and he was unaware of its
contents. Id. at 26, 74. Officer Alton phoned headquarters to
request guidance on how to proceed, and U.S. Park Police
                               4

Investigator Hodge arrived shortly thereafter. Id. at 25–27,
74. Alton briefed him on the stop and Hodge conferred with
a Park Police supervisor to assess whether Alton had probable
cause to make an arrest. Id. at 27. They determined that he
did. Id.

     After placing Vinton under arrest for “possession of a
prohibited weapon,” Officer Alton pried open the locked
briefcase. Id. at 27, 29, 74–75. Inside, he found three bags of
ecstasy, three pistol magazines, a “fighting knife . . . like
brass knuckles,” and a .45 caliber semiautomatic pistol,
cocked and loaded. Id. at 29, 75.

     Vinton was charged in a two-count indictment with
unlawful possession with intent to distribute ecstasy, 21
U.S.C. § 841; and using, carrying and possessing a firearm
during a drug trafficking offense, 18 U.S.C. § 924(c)(1). He
moved to suppress all of the tangible evidence recovered, and
all of his statements made, during the traffic stop. Following
a hearing, the district court denied the motion. Mem. Op.,
United States v. Vinton, No. 06-cr-298 (Feb. 12, 2007).
Vinton was convicted by a jury of both counts and was
sentenced to twenty-seven months’ imprisonment on the first
count and sixty months’ on the second count, to run
consecutively, as well as three years’ supervised release. He
brings this appeal arguing his motion to suppress was
erroneously denied.

     We review “determinations of reasonable suspicion and
probable cause . . . de novo” but “review findings of historical
fact only for clear error and . . . give due weight to inferences
drawn from those facts by” the district court. Ornelas v.
United States, 517 U.S. 690, 699 (1996).
                              5

                              II

     The Fourth Amendment guarantees “[t]he right of the
people to be secure in their persons, houses, papers, and
effects, against unreasonable searches and seizures.” U.S.
CONST. amend. IV. “Time and again, [the Supreme] Court
has observed that searches and seizures conducted outside the
judicial process, without prior approval by judge or
magistrate, are per se unreasonable under the Fourth
Amendment—subject only to a few specifically established
and well delineated exceptions.” Minnesota v. Dickerson,
508 U.S. 366, 372 (1993). The government relies on several
exceptions in urging us to uphold the denial of Vinton’s
motion to suppress. We will address each issue in sequence:
Did Officer Alton have the right to search the passenger
compartment of Vinton’s car? Following this search, was
Vinton properly arrested? Was the search of the briefcase
permissible?

                              A

     The Supreme Court has long “recognized that traffic
stops are especially fraught with danger to police officers”
and that the “risk of harm to both the police and the occupants
[of a stopped vehicle] is minimized if the officers routinely
exercise unquestioned command of the situation.” Arizona v.
Johnson, 129 S. Ct. 781, 786 (2009) (internal quotation marks
and citations omitted) (alteration in original). Thus, during a
traffic stop, in order “to allow the officer to pursue his
investigation without fear of violence,” Adams v. Williams,
407 U.S. 143, 146 (1972), the officer may order the driver out
of his car and may search the passenger compartment of the
car for weapons if the officer develops a reasonable suspicion
that the driver is “dangerous and . . . may gain immediate
control of weapons” inside the car. Michigan v. Long, 463
                               6

U.S. 1032, 1049 (1983) (citing Terry v. Ohio, 392 U.S. 1, 21
(1968)) (footnote omitted); see Pennsylvania v. Mimms, 434
U.S. 106, 111 n.6 (1977) (per curiam). Courts assess “the
totality of the circumstances . . . to see whether the detaining
officer ha[d] a particularized and objective basis” for
suspecting the driver was armed and dangerous,
acknowledging that the “likelihood of criminal activity need
not rise to the level required for probable cause, and it falls
considerably short of satisfying a preponderance of the
evidence standard.” United States v. Arvizu, 534 U.S. 266,
273–74 (2002) (internal quotation marks omitted).

    Here, the facts that accumulated within the first few
moments of the traffic stop established a particularized and
objective basis for suspecting Vinton might be armed and
dangerous. As an initial matter, Vinton does not argue that
Officer Alton had an insufficient basis for pulling him over.
Indeed, it is clear that Vinton was properly stopped because
Officer Alton’s firsthand observations gave him probable
cause to believe that Vinton had been speeding and driving
with windows tinted in excess of the legal limit. See
Suppression Tr. at 8, 69; Whren v. United States, 517 U.S.
806, 810 (1996).

     Most crucially, upon approaching Vinton’s car, Officer
Alton saw a knife with a five-and-a-half-inch sheath in plain
view on the backseat, easily within reaching-distance of
Vinton. See Suppression Tr. at 11–12, 25, 37, 70. “[T]he
presence of one weapon may justifiably arouse concern that
there may be more in the vicinity.” United States v.
Christian, 187 F.3d 663, 669 (D.C. Cir. 1999). For instance,
in Long, the Supreme Court held that after the officers
observed “a large knife in the interior of the car,” they were
justified in “conduct[ing] an area search of the passenger
compartment” of the car “to ensure that there were no other
                              7

weapons” in “those areas to which Long would generally
have immediate control.” 463 U.S. at 1050–51. Similarly, in
Christian, we held that because the officer “saw [a] dagger in
plain view” when he “arrived at Christian’s car,” he “had
sufficient indication Christian might be armed and dangerous
to justify a protective search for weapons.” 187 F.3d at 669.
Like the defendants in Long and Christian, Vinton possessed
in plain view a knife capable of being used to cause serious
bodily harm. Although Officer Alton removed this knife and
placed it out of arm’s reach on the roof of Vinton’s car, he
was justifiably concerned that additional weapons might be
hidden elsewhere in the vicinity. This concern was not abated
by ordering Vinton out of the car and handcuffing him,
because had Vinton ultimately not been arrested, he would
have been “permitted to reenter his automobile, and he
w[ould] then have [had] access to any weapons inside.”
Long, 463 U.S. at 1052.

     We reject Vinton’s argument that while a dagger may
justify a protective search for additional weapons, see
Christian, 187 F.3d at 669, a sheathed knife like Vinton’s
may not. “[A] Terry investigation . . . involves a police
investigation at close range, when the officer remains
particularly vulnerable . . . [and] must make a quick decision
as to how to protect himself and others from possible danger.”
Long, 463 U.S. at 1052 (internal quotation marks and citation
omitted). Officer Alton did not have time to perform a close
inspection of Vinton’s sheathed knife to determine precisely
how dangerous it was. Nor was Officer Alton required to
accept Vinton’s claim that he used the knife only for fishing
with his grandfather. For one, Alton observed no other
fishing equipment in the car that might have corroborated this
story. See Suppression Tr. at 14, 71. But regardless, even a
lawfully-possessed fishing knife can be used as a dangerous
weapon. See Long, 463 U.S. at 1052 n.16 (holding that
                                8

possession of lawful hunting knife contributed to reasonable
suspicion that driver was armed and dangerous). Moreover,
there was an additional reason for viewing Vinton’s
explanations with skepticism. The “thin blue line sticker” on
the back of his car, see Suppression Tr. at 8, 70—which, as
Vinton concedes, “suggested a connection with law
enforcement,” Appellant’s Br. 36—could have been viewed
as a deliberate attempt to create the false impression that
Vinton was affiliated with law enforcement. Furthermore,
while Alton’s newly-acquired knowledge of a recent double-
stabbing homicide in the same neighborhood, see Suppression
Tr. at 20, 72, was not itself sufficient to justify the protective
search, it added to the circumstances warranting Alton’s
decision to search the car to ensure his own safety.

     Finally, Vinton’s argument that Officer Alton did not
subjectively believe Vinton was dangerous may easily be
rejected.     Because “[t]he Fourth Amendment test is
objective,” an officer’s “actual subjective motives . . . are
irrelevant to the Fourth Amendment analysis of [a] traffic
stop and protective search of the car.” United States v.
Washington, 559 F.3d 573, 575 (D.C. Cir. 2009). Of course,
it was possible that Vinton used his sheathed knife only for
fishing, that he had benign reasons for having excessively
tinted windows, and that his “thin blue line” sticker was not
meant to be misleading.         But “[a] determination that
reasonable suspicion exists . . . need not rule out the
possibility of innocent conduct.” Arvizu, 534 U.S. at 277.
Examining the totality of the circumstances objectively,
Officer Alton had a reasonable belief, based on specific and
articulable facts, that Vinton was armed and dangerous. See
Long, 463 U.S. at 1049. Thus, he properly searched the
passenger compartment of Vinton’s car for additional
weapons.
                                9

                                B

     “[A] warrantless arrest by a law officer is reasonable
under the Fourth Amendment where there is probable cause
to believe that a criminal offense has been or is being
committed.” Devenpeck v. Alford, 543 U.S. 146, 152 (2004).
“There is no precise formula for the probability required for
probable cause. Somewhere between ‘less than evidence
which would justify . . . conviction’ and ‘more than bare
suspicion,’ probable cause is satisfied. . . . The precise point is
indeterminate. . . . The standard is to be met by applying a
totality-of-the-circumstances analysis.” United States v.
Riley, 351 F.3d 1265, 1267 (D.C. Cir. 2003) (internal
quotation marks omitted).

     In the course of searching Vinton’s car for weapons,
Officer Alton found, among other things, a “butterfly knife”
hidden under the passenger-side floor mat. See Suppression
Tr. at 23, 73. Vinton was eventually arrested for “possession
of a prohibited weapon” (PPW), D.C. Code § 22-4514(b).
However, because the offense of PPW requires “proof of
intent to use [the weapon] unlawfully against another,” United
States v. Broadie, 452 F.3d 875, 881 (D.C. Cir. 2006)
(emphasis added) (internal quotation marks omitted), the
government has conceded that Officer Alton lacked probable
cause to arrest for PPW. The government nonetheless argues
the arrest was valid because there was probable cause to
believe Vinton committed the offense of “carrying a
dangerous weapon” (CDW), D.C. Code § 22-4504(a), which
“does not require proof of intent to use the weapon for an
unlawful purpose,” Broadie, 452 F.3d at 881. Because the
Fourth Amendment inquiry is objective, an officer’s
“subjective reason for making the arrest need not be the
criminal offense as to which the known facts provide
probable cause.” Devenpeck, 543 U.S. at 153; see also
                                10

Broadie, 452 F.3d at 881 (holding arrest was valid because
there was probable cause of CDW, even though officer
incorrectly believed at the time that he had probable cause of
PPW).

     The CDW statute prohibits “carry[ing] within the District
of Columbia either openly or concealed on or about their
person . . . any deadly or dangerous weapon.” D.C. Code §
22-4504(a). As we have explained, under District of
Columbia case law, a “deadly or dangerous weapon” is
“anything that is ‘likely to produce death or great bodily
injury by the use made of it.’” Broadie, 452 F.3d at 881
(quoting Strong v. United States, 581 A.2d 383, 386 (D.C.
1990)). Two categories of objects are likely to produce such
harm: (1) those that are “inherently dangerous,” i.e., where
“the design of the object is such that in its ordinary use it is
likely to cause great bodily injury”; and (2) those that
ostensibly may be “used as a tool in certain trades or hobbies
or . . . may be carried for utilitarian reasons,” but where “the
surrounding circumstances indicate” that “the purpose of
carrying the object . . . is its use as a weapon.” Id. at 882
(quoting Strong, 581 A.2d at 386; Scott v. United States, 243
A.2d 54, 56 (D.C. 1968)).

     “A butterfly knife has a split metal handle which encases
a single-edged blade. The knife is opened by folding back
both halves to expose the blade.”            United States v.
Kashiwabara, 993 F.2d 885 (table), 1993 WL 148094, at *1
(9th Cir. 1993); see also Suppression Tr. at 23–24 (describing
the butterfly knife as a knife, commonly “used in martial
arts,” where the blade “folds out” from the handle).1 The

1
  The district court at one point suggested the butterfly knife had
“several different blades.” Suppression Tr. at 73. After being
corrected, the court appeared to withdraw that finding. Id. at 77–
78. Because the testimony established that the butterfly knife had
                               11

record does not establish that butterfly knives are “inherently
dangerous,” and indeed, one can imagine they might be used
for sport or entertainment. Nonetheless, the surrounding
circumstances provided Officer Alton with probable cause to
believe Vinton intended to use this knife as a dangerous
weapon. See Lewis v. United States, 767 A.2d 219, 222 (D.C.
2001) (explaining that where the knife possessed by the
defendant is not inherently dangerous, “the government must
prove beyond a reasonable doubt that . . . the purpose of
carrying the instrument was its use as a dangerous weapon”).

     The design of a butterfly knife makes it principally useful
as an easily concealable and quickly deployable weapon
capable of injuring another person in an altercation at close
range. See, e.g., Taylor v. United States, 848 F.2d 715, 716,
720 (6th Cir. 1988) (butterfly knives are “most often
associated with the martial arts and with combat . . . [and are]
potentially dangerous, lethal” weapons that “can be opened
very rapidly, perhaps in less than 5 seconds” (internal
quotation marks omitted)); United States v. Stroman, No.
Crim. 05-66-P-S, 2006 WL 83404, at *14 (D. Me. Jan. 9,
2006) (To deploy a butterfly knife, “[t]he wielder releases one
of the halves of the handle and through a combination of
gravity and centrifugal force, the latter generated by a
movement of the arm or wrist, the wielder swings that half of
the handle around until it meets the other half. These forces
also swing the blade into position.” (internal quotation marks
omitted)).     Vinton never offered Officer Alton any
explanation whatsoever for his possession of this knife, and
certainly, he never suggested he was specially trained in the
use of butterfly knives for sport or entertainment purposes.
Thus, Officer Alton was entitled to rely on his common-sense

only one blade, and because both parties agree on this point, our
analysis assumes the knife had only one blade. See id. at 23, 76–
77.
                              12

assessment that Vinton probably intended to use the knife for
its most obvious purpose, fighting. Cf. Broadie, 452 F.3d at
882–83 (explaining that although an ASP baton is not
inherently dangerous, “the normal and the only apparent use
of an ASP baton . . . is to strike another” and that “a
reasonable officer surely would believe that a civilian,
presumably without police training, would likely inflict great
bodily injury when using [one]”). If anything, Vinton’s stated
profession—personal security—along with his allusion to
possessing weapons at home increased the likelihood that he
carried the butterfly knife for use as a weapon. See
Suppression Tr. at 11, 14, 71. That he may have planned to
use the knife only in self-defense or defense of another is
irrelevant, so long as he intended to use it as a weapon. See
Broadie, 452 F.3d at 881 (“[N]either self-defense nor any
other ‘lawful purpose’ is material to the offense or sufficient
to avoid liability [for CDW].” (citing Monroe v. United
States, 598 A.2d 439, 440 (D.C. 1991))).2

     In addition, the knife was hidden under the floor mat.
See Suppression Tr. at 23, 73.               Vinton’s various
explanations—that maybe the knife fell inadvertently and
landed under the mat, or perhaps it was stashed under the mat
to prevent passersby from being enticed to break into the car
to steal it—are, of course, possible. But Officer Alton was
not unreasonable in believing that the likeliest explanation for
the knife’s concealment was that Vinton intended to use it as
a weapon and therefore wanted to hide it from police officers
and potential adversaries. Furthermore, Vinton lied about the
knife’s existence. Officer Alton asked Vinton three times
whether there were any weapons in the car other than the
sheathed knife, and each time Vinton responded in the
2
 Vinton has not argued that the CDW statute is unconstitutional.
Therefore, we have no occasion to address the issue and our
holding expresses no view on it.
                                13

negative. See id. at 14, 22, 71, 73. This lack of candor
reasonably suggested to Officer Alton that Vinton intended to
use the butterfly knife for malicious purposes. Thus, the
totality of the circumstances provided probable cause to
believe Vinton was carrying a “deadly or dangerous weapon”
in violation of D.C. Code § 22-4504(a).

    Finally, Vinton argues that any finding of probable cause
must be struck down because the facts supporting probable
cause were uncovered only after unlawfully extending the
Terry stop beyond a reasonable duration. “[A] search which
is reasonable at its inception may violate the Fourth
Amendment by virtue of its intolerable intensity and scope.”
Terry, 392 U.S. at 18. To “assess[] whether a detention is too
long in duration to be justified as an investigative stop, we . . .
examine whether the police diligently pursued a means of
investigation that was likely to confirm or dispel their
suspicions quickly.” United States v. Sharpe, 470 U.S. 675,
686 (1985). Vinton contends that “[a]fter the frisk was
complete, the officers continued to detain Vinton for
approximately 45 minutes, including 30 minutes until
Investigator Hodge arrived on the scene and an additional 15
minutes while the[y] obtained advice from supervisors . . . .”
Appellant’s Br. 38–39.         However, Vinton waived this
argument by failing to raise it before the district court. See
Fed. R. Crim. P. 12(e) (any defense or objection not raised in
a motion to suppress is waived); United States v. Redman,
331 F.3d 982, 986 (D.C. Cir. 2003) (holding appellant waived
argument by failing to assert it at suppression hearing). In
any event, within the first few minutes of the traffic stop—as
soon as he found the butterfly knife—Officer Alton had
probable cause to arrest Vinton. Thus, Alton acted promptly
and diligently to confirm his initial suspicions.             His
subsequent efforts to determine precisely how to proceed
                               14

were a conscientious vindication of Vinton’s rights, not a
violation of them.

                               C

     Until recently, it was widely understood that New York v.
Belton, 453 U.S. 454, 460 (1981), established a “bright-line
rule,” whereby “incident to arrest the police may search the
passenger compartment of an arrestee’s automobile.” United
States v. Wesley, 293 F.3d 541, 548 (D.C. Cir. 2002); see also
United States v. Mapp, 476 F.3d 1012, 1018 (D.C. Cir. 2007)
(“As long as the arrest of an occupant of a car is lawful, a
search of the passenger compartment is reasonable.”). But
while the instant appeal was pending, the Supreme Court
decided Arizona v. Gant, which reshaped the law governing
searches incident to arrest in the automobile context. 129 S.
Ct. at 1714. Noting that Chimel v. California, 395 U.S. 752,
763 (1969), had held that “a search incident to arrest may
only include the arrestee’s person and the area within his
immediate control,” the Court explained that a reading of
Belton that would always authorize a vehicle search incident
to an occupant’s arrest “would . . . untether the rule from the
justifications underlying the Chimel exception.” Id. at 1716,
1719 (internal quotation marks omitted). Thus, Gant held
police may search a vehicle incident to the arrest of an
occupant only in two circumstances: (1) “when the arrestee is
unsecured and within reaching distance of the passenger
compartment at the time of the search” (the safety rationale);
or (2) “when it is ‘reasonable to believe evidence relevant to
the crime of arrest might be found in the vehicle’” (the
evidentiary rationale). Id. at 1719 (footnote omitted) (quoting
Thornton v. United States, 541 U.S. 615, 632 (2004) (Scalia,
J., concurring in judgment)).3
3
 Vinton argues that Gant also applies to Terry searches. Thus, he
contends Officer Alton’s initial protective search of his car was
                                  15


     During the protective search of Vinton’s car, Officer
Alton found a locked briefcase on the backseat. See
Suppression Tr. at 24, 26, 74. After placing Vinton under
arrest, Alton pried it open. See id. at 29, 74–75. The
government concedes that this search incident to Vinton’s
arrest cannot be upheld under Gant’s safety rationale because
Vinton was handcuffed at the time. See Appellee’s Br. 39.
Nonetheless, the government argues the search should be
upheld under Gant’s evidentiary rationale.4

     The Supreme Court did not elaborate on the
circumstances when it will be “reasonable to believe evidence
relevant to the crime of arrest might be found in the vehicle.”
Gant, 129 S. Ct. at 1719 (internal quotation marks omitted);
see also id. (noting that this evidentiary rationale “does not
follow from Chimel” but is based on “circumstances unique
to the vehicle context”). Presumably, the “reasonable to
believe” standard requires less than probable cause, because
otherwise Gant’s evidentiary rationale would merely

unconstitutional because he was handcuffed at the time of the
search. We decline to read Gant so expansively. The Supreme
Court explicitly limited its holding to the search-incident-to-arrest
context, see Gant, 129 S. Ct. at 1723–24, and it is doubtful that the
same rule ought to apply in the Terry search context, see id. at 1724
(Scalia, J., concurring) (“It must be borne in mind that we are
speaking here only of a rule automatically permitting a search when
the driver or an occupant is arrested. . . . In the no-arrest case, the
possibility of access to weapons in the vehicle always exists, since
the driver or passenger will be allowed to return to the vehicle
when the interrogation is completed.”).
4
 The government also argues Vinton had no reasonable expectation
of privacy in the briefcase, and consequently no protected Fourth
Amendment interest in it, because he disclaimed ownership of it.
We have no need to reach this issue.
                               16

duplicate the “automobile exception,” which the Court
specifically identified as a distinct exception to the warrant
requirement. See id. at 1721 (citing United States v. Ross,
456 U.S. 798, 820–21 (1982)). Rather, the “reasonable to
believe” standard probably is akin to the “reasonable
suspicion” standard required to justify a Terry search. See,
e.g., Adams, 407 U.S. at 146 (noting that a Terry search is
permissible if the officer “has reason to believe that the
suspect is armed and dangerous” (emphasis added)).
Accordingly, the officer’s assessment of the likelihood that
there will be relevant evidence inside the car must be based
on more than “a mere hunch,” but “falls considerably short of
[needing to] satisfy[] a preponderance of the evidence
standard.” Arvizu, 534 U.S. at 274.

     The Supreme Court explained that “[i]n many cases, as
when a recent occupant is arrested for a traffic violation, there
will be no reasonable basis to believe the vehicle contains
relevant evidence. But in others, including Belton and
Thornton, the offense of arrest will supply a basis for
searching the passenger compartment of an arrestee’s vehicle
and any containers therein.” Gant, 129 S. Ct. at 1719
(citation omitted). In both Belton and Thornton, the vehicle
occupants were arrested for possession of narcotics. See
Belton, 453 U.S. at 456; Thornton, 541 U.S. at 618. Had
Vinton been arrested merely for speeding or driving with
excessively tinted windows, Gant’s evidentiary rationale
obviously would not have authorized a subsequent search
because under the circumstances it would have been very
unlikely that evidence relevant to either of those traffic
offenses would be found inside his car. See Gant, 129 S. Ct.
at 1719 (holding that “[a]n evidentiary basis for the search
was . . . lacking . . . [because] Gant was arrested for driving
with a suspended license—an offense for which police could
not expect to find evidence in the passenger compartment of
                               17

[his] car”). But instead, Vinton was arrested for the unlawful
possession of a weapon, an offense that resembles narcotics-
possession offenses far more closely than it resembles a
traffic violation. Indeed, it is difficult to imagine a principled
basis for distinguishing the possession of narcotics from the
possession of an unlawful weapon, where an arrest for the
former makes it reasonable to believe additional narcotics
remain in the car, but an arrest for the latter does not make it
reasonable to believe additional weapons are in the car. In
both cases, the defendant has been caught with a type of
contraband sufficiently small to be hidden throughout a car
and frequently possessed in multiple quantities. Indeed, this
fact was well-known to Officer Alton, who testified that
“generally if one weapon is there . . . there’s the chance that
other weapons could be there.” Suppression Tr. 14; see id. at
28.

     The facts of this case establish that Alton was reasonable
in expecting there might be additional weapons in the car,
particularly in the locked briefcase found on the backseat.
Most significantly, Officer Alton already had found two
knives, one of which was hidden. He also had found two cans
of mace and a bag of earplugs. See id. at 23, 26, 73–74. Of
course, earplugs often are used for purposes unrelated to
weapons, but, as Alton reasonably recognized, they also are
commonly used at firing ranges to muffle the noise from
guns. See id. at 26, 74. Thus, having found two objects,
mace and earplugs, that suggested at least a possible
association with weapons, along with two other objects, a
sheathed knife and a butterfly knife, that were clearly capable
of being used as weapons, Officer Alton had an objectively
reasonable basis for believing that additional weapons might
be inside the car. A material element of the CDW offense is
that the defendant intends to use the object as a dangerous
weapon. See Lewis, 767 A.2d at 222. Finding additional
                                18

weapons in Vinton’s possession would have provided strong
circumstantial evidence of this specific intent. Thus, because
it was “reasonable to believe evidence relevant to the crime of
arrest might be found in the vehicle,” Officer Alton had the
right to search the passenger compartment of Vinton’s car
“and any containers therein,” including the locked briefcase.5
Gant, 129 S. Ct. at 1719 (internal quotation marks omitted).
The district court therefore properly admitted into evidence
the ecstasy, semiautomatic pistol, pistol magazines, and
“fighting knife” discovered inside the briefcase.

                                III

     Vinton also argues his statements were admitted into
evidence in violation of his rights under Miranda v. Arizona,
384 U.S. 436 (1966). Miranda warnings are required “where
a suspect in custody is subjected to interrogation.” Rhode
Island v. Innis, 446 U.S. 291, 300 (1980). Because “ordinary
traffic stops” are “noncoercive,” “persons temporarily
detained pursuant to such stops are not ‘in custody’ for the
purposes of Miranda.” Berkemer v. McCarty, 468 U.S. 420,
440 (1984). However, “[i]f a motorist who has been detained
pursuant to a traffic stop thereafter is subjected to treatment
that renders him ‘in custody’ for practical purposes, he will be
entitled to the full panoply of protections prescribed by
Miranda.” Id.


5
  We note that Gant sometimes states that it must be reasonable to
believe there will be evidence “of” the offense of arrest inside the
car, and elsewhere speaks more broadly of evidence “relevant” to
the offense of arrest. Compare 129 S. Ct. at 1714, 1720–23, with
id. at 1719 (quoting Thornton, 541 U.S. at 632 (Scalia, J.,
concurring in judgment)). But relevant evidence is evidence of the
offense, see FED. R. EVID. 401, so the difference in phrasing is
immaterial.
                             19

     Most of the statements Vinton claims were improperly
admitted were made by him while he was sitting in his car,
before Officer Alton handcuffed him and searched his car.
This includes his statements that he worked in personal
security, used the sheathed knife only for fishing with his
grandfather, had no other weapons in the car, and “keeps that
part of his trade at home.” See Suppression Tr. at 11–12, 14,
71. At the time he made these statements, Vinton was not “in
custody” and faced an “ordinary,” “noncoercive” traffic stop.
See Berkemer, 468 U.S. at 440. Thus, he had no entitlement
to Miranda warnings.

     Vinton also challenges the admission of two statements
he made after being handcuffed for some time but before
being formally arrested: that he used the earplugs as sleeping
aids, and that he did not own the locked briefcase or know
what was inside of it. See Suppression Tr. at 26, 74. We
need not decide whether Vinton was “in custody” at the time
he made these statements, because any Miranda violation was
harmless beyond a reasonable doubt.             Both of these
statements were wholly exculpatory and could not have
“contribute[d] to the verdict obtained.” United States v.
Harris, 515 F.3d 1307, 1311 (D.C. Cir. 2008) (internal
quotation marks omitted). Thus, even assuming a Miranda
violation occurred, there is no basis for reversal.

                             IV

    For the foregoing reasons, the judgment of the district
court is

                                                    Affirmed.

```

---

## GROUP: content/cases/United States v. Walker.md  (`case`, 5 assertions)

### content_page

```
---
title: "United States v. Walker"
type: case
citation: "799 F.3d 1361 (2015)"
parallel_cite: ""
neutral_cite: 2015 WL 5157456
court: "U.S. Court of Appeals, 11th Circuit"
court_level: coa
circuit: 11th
year: 2015
date_decided: 2015-09-03
docket: ""
authority_weight: "Binding in-circuit — 11th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2015-09-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: United States v. Walker
  varies_by_point: false
  scope_note: "Good law. Per curiam; applies Florida v. Jardines and United States v. Taylor to the geographic scope of the knock-and-talk implied license."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/2844024/united-states-v-wayne-walker/"
  cluster_id: 2844024
  opinion_id: 2844024
  identity_checked: true
homes:
  - page: "[[Knock and Talk]]"
    role: "Recent development (role-based)"
related: ["[[Florida v. Jardines]]", "[[French v. Merrill]]", "[[United States v. Lundin]]", "[[United States v. Carloss]]", "[[Kentucky v. King]]"]
aliases: ["United States v. Wayne Walker", "United States v. Walker (11th Cir. 2015)"]
tags: ["case", "fourth-amendment", "knock-and-talk", "implied-license", "curtilage", "eleventh-circuit"]
holding: "A 'small departure' from the front door — here, approaching the occupant's car parked in an open-sided carport beside the house when seeking to contact him — stays within the geographic scope of the knock-and-talk implied license, and a pre-dawn (5:04 a.m.) knock and talk is not a search and needs no exigent circumstances where the surrounding circumstances make the approach reasonable."
lake:
  record_id: United States v. Walker
  status: verified
  projected_at: 2026-07-06
---

# United States v. Walker

*799 F.3d 1361 (11th Cir. 2015)* · U.S. Court of Appeals, 11th Circuit · **Binding in-circuit — 11th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers looking for Michael Upshaw — who had an outstanding warrant and was reportedly staying at Wayne Walker's house in Macon, Georgia — went to the house twice on the night of February 28, knocking at the main door and a second door each time with no answer; on the second visit they noticed a Honda Civic newly parked in Walker's open-sided carport. A little after 5:00 a.m. they drove past again, saw lights on in the house and the car's dome light on, and approached the car, where they saw a person resting his head on the steering wheel. Sergeant Douglas knocked on the car window, asked if the person was alright, and asked him to step out; it was Walker. Walker said Upshaw was not there and volunteered that the officers "were more than welcome" to come in and look; inside, an officer saw counterfeit $100 bills in plain view. Walker entered a conditional guilty plea to manufacturing counterfeit currency (18 U.S.C. § 471) and appealed the denial of his suppression motion.

## Issue
Whether officers exceeded the [[Knock and Talk|knock-and-talk]] exception when, instead of going to the front door, they approached the occupant's car parked in an open-sided carport, and whether doing so at 5:04 a.m. was unreasonable.

## Rule
The [[Knock and Talk|knock-and-talk]] exception rests on the implied license to approach and knock, and "[t]he scope of the knock and talk exception is limited in two respects. First, it ceases where an officer's behavior 'objectively reveals a purpose to conduct a search.' . . . Second, the exception is geographically limited to the front door or a 'minor departure' from it." — 799 F.3d at 1363. ^pin-1363

A small movement from the front door to reach the occupant stays within that geographic limit: "approaching Walker's vehicle parked inside of his open-sided carport, instead of going to his front door, did not exceed the geographic limit on the knock and talk exception. A 'small departure from the front door . . . when seeking to contact the occupants' is permissible." — [799 F.3d at 1364](https://www.courtlistener.com/opinion/2844024/united-states-v-wayne-walker/#:~:text=did%20not%20exceed%20the%20geographic%20limit%20on%20the%20knock%20and%20talk%20exception) (quoting *United States v. Taylor*, 458 F.3d 1201, 1205 (11th Cir. 2006)). ^pin-1364

The court also held that a pre-dawn knock and talk is reasonable on these circumstances and that an early-morning knock and talk "is not considered a search," so it requires no [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]. — *Id.* (& n.1). ^pin-1364a

## Application
On these facts the officers did not exceed the exception. Their purpose was investigatory only in the sense of finding someone to talk to about Upshaw, not to "discover[] incriminating evidence," so their conduct did not objectively reveal a search. And approaching the open-sided carport — located right next to the house, where the lit dome light gave them reason to believe the occupant was sitting in the car — was a permissible small departure from the front door, not an intrusion into a constitutionally protected enclosed space. The 5:04 a.m. timing was reasonable given the two earlier visits and the lights indicating someone was inside; because a knock and talk is not a search, no [[Exigent Circumstances and Hot Pursuit|exigency]] was required.

## Conclusion
The officers' approach fell within the [[Knock and Talk|knock-and-talk]] exception and was reasonable; the Eleventh Circuit affirmed the denial of Walker's motion to suppress the counterfeit currency.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 11th Cir.**
- *Walker* applies the implied-license framework of [[Florida v. Jardines]] (and the Eleventh Circuit's *Taylor* "minor departure" rule) to hold that a small departure from the front door to reach the occupant stays within the [[Knock and Talk|knock-and-talk]] license. Contrast the time-plus-purpose analysis in [[United States v. Lundin]] (9th Cir.), where a pre-dawn approach undertaken to arrest the occupant exceeded the implied license.

## Appears on
- [[Knock and Talk]] — *Recent development (role-based)*

## Sources
- *United States v. Walker*, 799 F.3d 1361 (11th Cir. 2015) — https://www.courtlistener.com/opinion/2844024/united-states-v-wayne-walker/ — pinpoints: 1363, 1364.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8bb474ee6664d188", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "799 F.3d 1361 (2015)", "court": "U.S. Court of Appeals, 11th Circuit", "neutral_cite": "2015 WL 5157456", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Walker", "year": "2015"}}
{"assertion_id": "3342c07806287a8b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A 'small departure' from the front door — here, approaching the occupant's car parked in an open-sided carport beside the house when seeking to contact him — stays within the geographic scope of the knock-and-talk implied license, and a pre-dawn (5:04 a.m.) knock and talk is not a search and needs no exigent circumstances where the surrounding circumstances make the approach reasonable.", "title": "United States v. Walker"}}
{"assertion_id": "a8e54933665a65d9", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Recent development (role-based)", "title": "United States v. Walker"}}
{"assertion_id": "790adf9aef8e20b2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2015-09-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "United States v. Walker", "field_i_validity": "good_law", "scope_note": "Good law. Per curiam; applies Florida v. Jardines and United States v. Taylor to the geographic scope of the knock-and-talk implied license.", "title": "United States v. Walker", "varies_by_point": "false"}}
{"assertion_id": "fd806267b716aaa0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 11th Cir.", "title": "United States v. Walker"}}
```

### lake record — United States v. Walker

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Walker",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "United States v. Wayne Walker",
    "case_name_short": "",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Wayne WALKER, Defendant-Appellant",
    "input_case_name": "United States v. Walker",
    "court": "U.S. Court of Appeals, 11th Circuit",
    "court_id": "ca11",
    "court_level": "coa",
    "circuit": "11th",
    "state": null,
    "date_decided": "2015-09-03",
    "year": 2015,
    "docket": null,
    "cluster_id": 2844024,
    "lead_opinion_id": 2844024,
    "sibling_ids": [
      2844024
    ],
    "absolute_url": "/opinion/2844024/united-states-v-wayne-walker/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "799 F.3d 1361",
      "volume": "799",
      "reporter": "F.3d",
      "page": "1361",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2015 WL 5157456",
        "volume": "2015",
        "reporter": "WL",
        "page": "5157456",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "799 F.3d 1361",
        "volume": "799",
        "reporter": "F.3d",
        "page": "1361",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 WL 5157456",
        "volume": "2015",
        "reporter": "WL",
        "page": "5157456",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "799 F.3d 1361",
    "official_selection": {
      "court_class": "coa",
      "selected": "799 F.3d 1361",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-1363",
      "page": null,
      "quote": "to come in and look; inside, an officer saw counterfeit $100 bills in plain view. Walker entered a conditional guilty plea to manufacturing counterfeit currency (18 U.S.C. \u00a7 471) and appealed the denial of his suppression motion. ## Issue Whether officers exceeded the knock-and-talk exception when, instead of going to the front door, they approached the occupant's car parked in an open-sided carport, and whether doing so at 5:04 a.m. was unreasonable. ## Rule The knock-and-talk exception rests on the implied license to approach and knock, and",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1364",
      "page": null,
      "quote": "approaching Walker's vehicle parked inside of his open-sided carport, instead of going to his front door, did not exceed the geographic limit on the knock and talk exception. A 'small departure from the front door . . . when seeking to contact the occupants' is permissible.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1364a",
      "page": null,
      "quote": "is not considered a search,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-09-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "United States v. Walker",
    "varies_by_point": false,
    "scope_note": "Good law. Per curiam; applies Florida v. Jardines and United States v. Taylor to the geographic scope of the knock-and-talk implied license.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "French v. Merrill",
          "cluster_id": 5273192,
          "cite": [
            "15 F.4th 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "KEMP v. THE STATE (Three Cases)",
          "cluster_id": 10366887,
          "cite": [
            "303 Ga. 385"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Graham",
          "cluster_id": 10286306,
          "cite": [
            "123 F.4th 1197"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Falls",
          "cluster_id": 10019104,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Doe v. Samford University",
          "cluster_id": 6454512,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "United States v. Walker:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(2844024) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca11)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      },
      "lane2_top_cited": {
        "query": "cites:(2844024)",
        "reviewed": 5,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(2844024)",
        "reviewed": 1,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 1,
        "triage_read": 0,
        "triage_snippet_classified": 1
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(2844024)",
    "indexed_citing_opinions": 5,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 2844024,
        "count": 5,
        "count_source": "search"
      }
    ],
    "citation_count": 38,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/united-states-v-walker.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 5,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 2844024,
        "cited_id": 77385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2844024,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2844024,
        "cited_id": 626016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 2844024,
        "cited_id": 856347,
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
    "date_created": "2026-07-06T03:30:51Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T03:31:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T03:31:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T03:32:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T03:31:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — United States v. Walker

```
           Case: 15-10710   Date Filed: 09/03/2015   Page: 1 of 7


                                                                    [PUBLISH]



            IN THE UNITED STATES COURT OF APPEALS

                    FOR THE ELEVENTH CIRCUIT
                      ________________________

                            No. 15-10710
                        Non-Argument Calendar
                      ________________________

              D.C. Docket No. 5:14-cr-00055-MTT-CHW-1



UNITED STATES OF AMERICA,

                                                              Plaintiff-Appellee,

                                 versus

WAYNE WALKER,

                                                         Defendant-Appellant.

                      ________________________

               Appeal from the United States District Court
                   for the Middle District of Georgia
                     ________________________

                            (September 3, 2015)

Before ED CARNES, Chief Judge, MARCUS, and WILLIAM PRYOR, Circuit
Judges.

PER CURIAM:
                Case: 15-10710    Date Filed: 09/03/2015   Page: 2 of 7


         Wayne Walker entered a conditional guilty plea to one count of

manufacturing counterfeit United States currency in violation of 18 U.S.C. § 471.

He appeals the district court’s denial of his motion to suppress. He contends that

the officers who found counterfeit bills in his home did not comply with the

“knock and talk” exception to the Fourth Amendment’s warrant requirement and

acted unreasonably by going to his house at 5:04 a.m.

                                          I.

         Officer Jason Douglas and Sergeant Travis Douglas were working the night

shift on February 28, 2014. Because Officer Douglas had received information

that Michael Upshaw, who had an outstanding warrant, could be found at Walker’s

house, the two officers visited it that night and again in the early hours of March 1.

         Walker’s house is located at the corner of Georgia Highway 49 and 111

Moore Place in Macon, Georgia. The back of the house faces Highway 49 while

the side of the house faces Moore Place (another road). The house sits about 100

feet from Moore Place. A gravel driveway runs from Moore Place and goes

directly under a metal carport that sits about 30 feet from the main door to the

house (there is also a second door to the house). The carport is entirely open on all

sides but covered by a metal roof. It is supported by five poles on each of two

sides.




                                          2
              Case: 15-10710     Date Filed: 09/03/2015    Page: 3 of 7


      The officers first went to Walker’s house at 9:00 p.m. on February 28. They

knocked at the main door and the other door but no one answered. They left and

returned at 11:00 p.m. Again they knocked and again no one answered. The

officers noticed that parked in the open-sided carport was a Honda Civic that had

not been there when they were at the house earlier.

      The officers drove past the house again a little after 5:00 a.m. the following

morning. They noticed that some house lights were on and the dome light inside

the Honda Civic was now on. As they approached the car they saw a person inside

with his head resting on the steering wheel. The officers testified that they were

trying to figure out who was in the car and whether the person was alright.

Sergeant Douglas therefore knocked on the car window, asked the person whether

he was alright, and then asked him to step out of the car. The person in the car

turned out to be Walker. The officers told Walker that they were looking for

Upshaw. Walker said that Upshaw was not at the house and, without being asked,

told the officers that they “were more than welcome” to come in and look for him.

Upon entering the house, Officer Douglas began searching for Upshaw. He saw

counterfeit $100 bills printed on white sheets of paper sitting on a shelf in plain

view. The officers did not find Upshaw, but they did decide that they had probable

cause to arrest Walker for the counterfeit currency.

                                          II.


                                           3
               Case: 15-10710     Date Filed: 09/03/2015     Page: 4 of 7


        Walker contends that the district court should have suppressed the evidence

of counterfeit money that the officers found in his home because their search was

illegal. “A motion to suppress evidence presents a mixed question of law and

fact.” United States v. Lewis, 674 F.3d 1298, 1302 (11th Cir. 2012). We review

the district court’s factfindings for clear error and its “application of the law to the

facts de novo.” Id. at 1302–03. We construe all facts in the light most favorable to

the party who prevailed in the district court and give “substantial deference to the

factfinder’s credibility determinations, both explicit and implicit.” Id. at 1303.

        The “ultimate touchstone of the Fourth Amendment is reasonableness.”

Brigham City v. Stuart, 547 U.S. 398, 403, 126 S. Ct. 1943, 1947 (2006). Because

the home and the curtilage surrounding it is a “constitutionally protected area,”

Florida v. Jardines, ___ U.S. ___, 133 S. Ct. 1409, 1415–16 (2013), it is

“presumptively unreasonable” to search a home or its curtilage without a warrant.

Under the “knock and talk” exception, however, a “police officer not armed with a

warrant may approach a home and knock, precisely because that is no more than

any private citizen may do.” Id. at 1416 (quotation marks omitted). That

exception is based on the “implicit license” that all individuals (including police

officers) have to “approach [a] home by the front path, knock promptly, wait

briefly to be received, and then (absent invitation to linger longer) leave.” Id. at

1415.


                                            4
              Case: 15-10710      Date Filed: 09/03/2015   Page: 5 of 7


      The scope of the knock and talk exception is limited in two respects. First, it

ceases where an officer’s behavior “objectively reveals a purpose to conduct a

search.” Id. at 1416–17 (holding that using a police dog to sniff for drugs on the

front porch “in hopes of discovering incriminating evidence” exceeds the scope of

the knock and talk exception). Second, the exception is geographically limited to

the front door or a “minor departure” from it. United States v. Taylor, 458 F.3d

1201, 1204–05 (11th Cir. 2006).

      Walker contends that the officers exceeded the scope of the knock and talk

exception because they conducted an investigatory search when they approached

his vehicle. They did not, for two reasons. First, the officers’ behavior did not

objectively reveal a purpose to search. As their earlier visits to the house

indicated, the officers were trying to find someone to talk to about Upshaw’s

whereabouts. The officers did not approach Walker with the purpose of

“discovering incriminating evidence” — just to speak with the homeowner, which

is conduct that falls squarely within the scope of the knock and talk exception.

Jardines, 131 S. Ct. at 1416. Walker asserts that the officers were engaged in a

search because they did not know that he was in the vehicle when they approached

it. They knew, however, that a dome light was on, which indicated that a person

might well be inside, and that fact was confirmed when they approached the car.

An officer may not know that a homeowner is inside a home when knocking on the


                                          5
              Case: 15-10710        Date Filed: 09/03/2015   Page: 6 of 7


door, but the knock and talk exception permits knocking on the door to find out.

See Jardines, 131 S. Ct. at 1415.

      Second, approaching Walker’s vehicle parked inside of his open-sided

carport, instead of going to his front door, did not exceed the geographic limit on

the knock and talk exception. A “small departure from the front door . . . when

seeking to contact the occupants” is permissible. Taylor, 458 F.3d 1205 (citation

and quotation marks omitted); cf. Coffin v. Brandau, 642 F.3d 999, 1012 (11th Cir.

2011) (contrasting a garage attached to a home and enclosed by three walls and a

door with a carport that is open and exposed to the public in deciding whether an

officer’s entry into the garage violated the Fourth Amendment). The carport was

located right next to the house and the officers entered it because they had reason

to believe the house’s occupant was sitting in the car parked inside. They did not

exceed the scope of the knock and talk exception.

      Walker also contends that going to someone’s house before sunrise to knock

on the door is unreasonable and exceeds the implied invitation that underlies the

knock and talk exception. That contention fails in light of all the circumstances

surrounding the officers’ actions. They had already visited the house twice to

speak with its owner. When they arrived the third time at 5:04 a.m. and saw a light

on inside the vehicle, it was not unreasonable to think that someone was inside it.

Although many people might normally be asleep at that early hour, the light on in


                                            6
                Case: 15-10710       Date Filed: 09/03/2015       Page: 7 of 7


the car indicated otherwise. The officers also saw lights on in the house. They did

not act unreasonably by approaching the vehicle, tapping on the window, and

asking Walker to step out. 1 Because their conduct was reasonable, the officers

complied with the Fourth Amendment. See Brigham City, 547 U.S. at 403, 406–

07, 126 S. Ct. at 1947, 1949. The district court therefore did not err in denying

Walker’s motion to suppress the evidence of counterfeit currency found in the

home.

        AFFIRMED.




        1
         Walker argues that under Brigham City v. Stuart, 547 U.S. 398, 126 S. Ct. 1943 (2006),
any warrantless entry into the home or curtilage that occurs in the wee hours of the morning must
be accompanied by exigent circumstances. That decision held that police officers’ warrantless
search of a home at 3:00 a.m. was reasonable because exigent circumstances existed. Id. at 403–
07, 126 S. Ct. at 1947–49. It did not hold, however, that exigent circumstances must exist for a
warrantless early morning knock and talk, which is not considered a search.
                                               7

```

---

## GROUP: content/cases/United States v. Warshak.md  (`case`, 5 assertions)

### content_page

```
---
title: United States v. Warshak
type: case
citation: "631 F.3d 266 (2010)"
parallel_cite: ""
neutral_cite: "2010 U.S. App. LEXIS 25415; 2010 WL 5071766"
court: "U.S. Court of Appeals, 6th Cir."
court_level: coa
circuit: ca6
year: 2010
date_decided: ""
docket: No. 08-3997
authority_weight: "Binding in-circuit — 6th Cir."
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
  opinion_url: "https://www.courtlistener.com/opinion/181032/united-states-v-warshak/"
  cluster_id: 181032
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Warshak
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Third-Party Doctrine & CSLI]]"
    role: "Lower-court development (content/metadata line)"
related:
  - "[[Third-Party Doctrine & CSLI]]"
  - "[[Katz v. United States]]"
  - "[[United States v. Jacobsen]]"
  - "[[Carpenter v. United States]]"
tags:
  - case
  - fourth-amendment
  - email
  - third-party-doctrine
  - stored-communications-act
  - digital-privacy
  - warrant-requirement
holding: "A subscriber has a reasonable expectation of privacy in the contents of emails stored with, sent, or received through a commercial ISP; the government therefore may not compel an ISP to turn over the contents of a subscriber's emails without first obtaining a warrant based on probable cause, and to the extent the Stored Communications Act permits warrantless compelled disclosure of email contents it is unconstitutional. Because the agents relied in good faith on the SCA, however, the exclusionary rule did not require suppression."
aliases:
  - United States v. Warshak
  - "United States v. Warshak (6th Cir. 2010)"
---

# United States v. Warshak

*631 F.3d 266 (6th Cir. 2010)* (No. 08-3997) · U.S. Court of Appeals for the Sixth Circuit · **Binding in-circuit — 6th Cir.** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 181032 → combined opinion 181032 (Boggs, Circuit Judge, for the court; McKeague, J., joined; Keith, J., concurred in the result; 631 F.3d 266, argued June 16, 2010, decided Dec. 14, 2010). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*288`). S9 promotes. -->

## Background
Steven Warshak ran Berkeley Premium Nutraceuticals, the company behind the "male enhancement" supplement Enzyte, and was convicted with others of a large mail-, wire-, and bank-fraud and money-laundering scheme built on deceptive billing of customers. In building its case, the government obtained roughly 27,000 of Warshak's emails from his Internet service provider, NuVox, not with a warrant but under provisions of the Stored Communications Act (SCA) allowing compelled disclosure on less than probable cause. Warshak argued on appeal that acquiring his email contents this way violated the Fourth Amendment and that the emails should have been suppressed.

## Issue
Whether a subscriber has a Fourth Amendment [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the contents of emails held by a commercial ISP, such that the government must obtain a warrant before compelling the ISP to disclose them — and, if so, whether the exclusionary rule requires suppression.

## Rule
Analogizing email to a sealed letter or a telephone call routed through an intermediary, the court held that using an ISP as a conduit does not surrender the privacy of the message's contents; the ISP is the functional equivalent of a post office or phone company. It therefore held: "The government may not compel a commercial ISP to turn over the contents of a subscriber's emails without first obtaining a warrant based on probable cause." — 631 F.3d at 288. Because the agents obtained Warshak's emails without a warrant, they violated the Fourth Amendment, and to the extent the SCA authorizes such warrantless compelled disclosure of email contents, it is unconstitutional. ^pin-288

## Application
The court distinguished the third-party-doctrine cases: unlike the bank records in *[[United States v. Miller]]*, emails are confidential communications entrusted to an ISP as a mere intermediary, not information voluntarily conveyed to the recipient for use in the ordinary course of business — so a provider's contractual ability to access emails in limited circumstances did not extinguish the subscriber's expectation of privacy. Even so, the emails were not suppressed: relying on *[[Illinois v. Krull]]*, the court held the agents had acted in objectively good-faith reliance on the SCA, whose unconstitutionality was not then apparent, so the deterrence rationale of the exclusionary rule did not warrant suppression. The convictions were affirmed on this ground.

## Conclusion
The court held the warrantless acquisition of Warshak's emails **violated the Fourth Amendment**, but declined to suppress the emails under the [[The Good-Faith Exception|good-faith exception]]; the challenged convictions were **affirmed** on the email-privacy issue. Boggs, Circuit Judge, wrote for the court (McKeague, J., joined); Keith, J., concurred in the result.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Warshak* is the anchor circuit decision extending Fourth Amendment protection to the *contents* of emails held by a third-party ISP — a landmark limiting the third-party doctrine in the digital context and a widely followed precursor to the Supreme Court's *[[Carpenter v. United States]]* (2018). Teach it in the *[[Katz v. United States|Katz]]*/*[[United States v. Jacobsen|Jacobsen]]* line as the case that treats an ISP like a post office, while noting its in-circuit (6th Cir.) authority and the good-faith limit on suppression.

## Appears on
- [[Third-Party Doctrine & CSLI]] — *Lower-court development (content/metadata line)*

## Sources
- [*United States v. Warshak*, 631 F.3d 266 (6th Cir. 2010)](https://www.courtlistener.com/opinion/181032/united-states-v-warshak/) — pinpoint: 288 (Boggs, J., for the court; the CL opinion text carries the reporter star `*288` in the *Miller* discussion immediately before the quoted holding paragraph, which sits on page 288). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e98896cfa800bcd2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "631 F.3d 266 (2010)", "court": "U.S. Court of Appeals, 6th Cir.", "neutral_cite": "2010 U.S. App. LEXIS 25415; 2010 WL 5071766", "official_citation_present": true, "parallel_cite": "", "title": "United States v. Warshak", "year": "2010"}}
{"assertion_id": "3cd691711799c76f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A subscriber has a reasonable expectation of privacy in the contents of emails stored with, sent, or received through a commercial ISP; the government therefore may not compel an ISP to turn over the contents of a subscriber's emails without first obtaining a warrant based on probable cause, and to the extent the Stored Communications Act permits warrantless compelled disclosure of email contents it is unconstitutional. Because the agents relied in good faith on the SCA, however, the exclusionary rule did not require suppression.", "title": "United States v. Warshak"}}
{"assertion_id": "93fd6d3a2096dd1c", "dimension": "support", "kind": "home_role", "locator": {"home": "Third-Party Doctrine & CSLI"}, "payload": {"home": "Third-Party Doctrine & CSLI", "role": "Lower-court development (content/metadata line)", "title": "United States v. Warshak"}}
{"assertion_id": "d987ecdf845b332e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 6th Cir.", "title": "United States v. Warshak"}}
{"assertion_id": "f7b27a15c433364b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "United States v. Warshak", "varies_by_point": "false"}}
```

### lake record — United States v. Warshak

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Warshak",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Warshak",
    "case_name_short": "Warshak",
    "case_name_full": "UNITED STATES of America, Plaintiff-Appellee, v. Steven WARSHAK (08-3997/4085; 09-3176); Harriet Warshak (08-3997/4087/4429); TCI Media, Inc. (08-3997/4212), Defendants-Appellants",
    "input_case_name": "United States v. Warshak",
    "court": "U.S. Court of Appeals, 6th Cir.",
    "court_id": null,
    "court_level": "coa",
    "circuit": "ca6",
    "state": null,
    "date_decided": null,
    "year": 2010,
    "docket": "No. 08-3997",
    "cluster_id": 181032,
    "lead_opinion_id": 9438755,
    "sibling_ids": [],
    "absolute_url": "/opinion/181032/united-states-v-warshak/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "631 F.3d 266",
      "volume": "631",
      "reporter": "F.3d",
      "page": "266",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [
      {
        "cite": "2010 U.S. App. LEXIS 25415",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "25415",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 5071766",
        "volume": "2010",
        "reporter": "WL",
        "page": "5071766",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "631 F.3d 266",
        "volume": "631",
        "reporter": "F.3d",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 U.S. App. LEXIS 25415",
        "volume": "2010",
        "reporter": "U.S. App. LEXIS",
        "page": "25415",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2010 WL 5071766",
        "volume": "2010",
        "reporter": "WL",
        "page": "5071766",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "631 F.3d 266",
    "official_selection": {
      "court_class": "coa",
      "selected": "631 F.3d 266",
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
    "date_created": "2026-07-06T13:11:36Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:11:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-warshak--181032",
      "to_record_id": "United States v. Warshak",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Warshak (truncated)

```
<opinion type="majority">
<p id="b300-5">BOGGS, J., delivered the opinion of the court, in which McKEAGUE, J., joined. KEITH, J. (pp. 333-36), delivered a separate opinion concurring in the result.</p>
<p id="b300-6">OPINION</p>
<author id="b300-7">BOGGS, Circuit Judge.</author>
<p id="b300-8">Berkeley Premium Nutraceuticals, Inc., was an incredibly profitable company that served as the distributor of Enzyte, an herbal supplement purported to enhance male sexual performance. In this appeal, defendants Steven Warshak (“Warshak”), Harriet Warshak (“Harriet”), and TCI Media, Inc. (“TCI”), challenge their convictions stemming from a massive scheme to defraud Berkeley’s customers. Warshak and Harriet also challenge their sentences, as well as two forfeiture judgments.</p>
<p id="b300-9">Given the volume and complexity of the issues presented, we provide the following summary of our holdings:</p>
<p id="b300-10">(1) Warshak enjoyed a reasonable expectation of privacy in his emails vis-a-vis NuVox, his Internet Service Provider. <em>See Katz v. United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U.S. 347</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span> (1967). Thus, government agents violated his Fourth Amendment rights by compelling NuVox to turn over the emails without first obtaining a warrant based on probable cause. However, because the agents relied in good faith on provisions of the Stored Communications Act, the exclusionary rule does not apply in this instance. <em>See Illinois v. Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U.S. 340</a></span>, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">107 S.Ct. 1160</a></span>, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">94 L.Ed.2d 364</a></span> (1987).</p>
<p id="b300-12">(2) The district court did not err in refusing to hold a full-fledged hearing under <em>Kastigar v. United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U.S. 441</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">32 L.Ed.2d 212</a></span> (1972), when determining whether government agents had improperly used privileged materials seized during a valid search of Berkeley’s headquarters. <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>does not apply with full force outside the context of compelled testimony. <em>See United States v. Squillacote, </em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">221 F.3d 542</a></span> (4th Cir.2000).</p>
<p id="b300-13">(3) The district court did not abuse its discretion by failing to order the government to provide discovery in a different format, as Federal Rule of Criminal Procedure 16 is silent on the issue of the form that discovery must take. Moreover, the government did not duck its obligations under <em>Brady v. Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L.Ed.2d 215</a></span> (1963), by providing the defendants with massive quantities of discovery. <em>See United States v. Skilling, </em><span class="citation" data-id="64496"><a href="/opinion/64496/united-states-v-skilling/" aria-description="Citation for case: United States v. Skilling">554 F.3d 529</a></span> (5th Cir.2009), <em>vacated in part on other grounds, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./130/2896/">130 S.Ct. 2896</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/177/619/">177 L.Ed.2d 619</a></span> (2010). Finally, the district court did not err in refusing to grant the defendants a continuance so that they could continue examining the discovery materials turned over by the government.</p>
<p id="b300-16">(4) The district court did not err in refusing to grant Warshak a new trial based on an alleged <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation, as the purportedly exculpatory material did not rise <page-number citation-index="1" label="275">*275</page-number>to the level of materiality. <em>See Kyles v. Whitley, </em><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U.S. 419</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">115 S.Ct. 1555</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">131 L.Ed.2d 490</a></span> (1995).</p>
<p id="b301-5">(5) The district court did not err in refusing to grant the defendants a new trial on the basis of prosecutorial misconduct. Though the prosecution did make a number of improper remarks during its rebuttal argument, the remarks were not flagrant. <em>See United States v. Carter, </em><span class="citation" data-id="771624"><a href="/opinion/771624/united-states-v-roquel-allen-carter/" aria-description="Citation for case: United States v. Roquel Allen Carter">236 F.3d 777</a></span> (6th Cir.2001).</p>
<p id="b301-6">(6) The evidence was sufficient to support Warshak’s and Harriet’s respective convictions for conspiracy to commit mail, wire, and bank fraud, in violation of <span class="citation no-link">18 U.S.C. § 1349</span>. <em>See Jackson v. Virginia, </em><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">443 U.S. 307</a></span>, <span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">99 S.Ct. 2781</a></span>, <span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">61 L.Ed.2d 560</a></span> (1979). Those convictions are therefore sustained.</p>
<p id="b301-7">(7) The evidence was sufficient to support Warshak’s convictions for mail fraud, in violation of <span class="citation no-link">18 U.S.C. § 1341</span>. Those convictions are therefore sustained.</p>
<p id="b301-8">(8) The evidence was sufficient to support Warshak’s and Harriet’s respective convictions for bank fraud, in violation of <span class="citation no-link">18 U.S.C. § 1344</span>. Furthermore, the district court did not err in instructing the jury that, under certain circumstances, the government may prove specific intent to defraud a bank by showing specific intent to defraud a third party. <em>See United States v. Reaume, </em><span class="citation" data-id="782971"><a href="/opinion/782971/united-states-v-scott-a-reaume/" aria-description="Citation for case: United States v. Scott A. Reaume">338 F.3d 577</a></span> (6th Cir.2003). Those convictions are therefore sustained.</p>
<p id="b301-9">(9) The evidence was sufficient to support Warshak’s conviction for conspiracy to commit access-device fraud, in violation of <span class="citation no-link">18 U.S.C. § 1029</span>. That conviction is sustained.</p>
<p id="b301-10">(10) The evidence was sufficient to support Warshak’s and TCI’s respective convictions for money laundering, in violation of <span class="citation no-link">18 U.S.C. §§ 1956</span>, 1957. Those convictions are affirmed. By contrast, the evidence was insufficient to support Harriet’s money-laundering convictions. Those convictions are therefore reversed.</p>
<p id="b301-12">(11) The evidence was sufficient to support Warshak’s conviction for conspiracy to obstruct an FTC proceeding, in violation of <span class="citation no-link">18 U.S.C. §§ 371</span>, 1505. As a consequence, that conviction is sustained.</p>
<p id="b301-13">(12) The district court did not err in refusing to order the government to reveal whether or not it had conducted any additional surreptitious searches of Warshak’s emails or communications. The discovery afforded by Federal Rule of Criminal Procedure 16 is limited to the evidence referred to in its express provisions, <em>United States v. Presser, </em><span class="citation" data-id="504674"><a href="/opinion/504674/united-states-v-jackie-presser-harold-friedman-and-anthony-hughes/#1285" aria-description="Citation for case: United States v. Jackie Presser Harold Friedman and...">844 F.2d 1275, 1285</a></span> (6th Cir.1988), and those provisions do not encompass the information sought by the defendants.</p>
<p id="b301-14">(13) The district court failed to provide an adequate explanation of its determination that the defendants should be held accountable for $411 million in losses. <em>See </em>Fed.R.Crim.P. 32(i)(3)(B); <em>United States v. White, </em><span class="citation" data-id="9632037"><a href="/opinion/1446782/united-states-v-white/#415" aria-description="Citation for case: United States v. White">492 F.3d 380, 415</a></span> (6th Cir.2007). We therefore vacate Warshak’s sentence and remand.</p>
<p id="b301-15">(14) The district court did not abuse its discretion in refusing to admit certain evidence during the forfeiture phase of the trial. Furthermore, the evidence was sufficient to support the proceeds-money and money-laundering forfeiture judgments against Warshak. In addition, the evidence was sufficient to support the proceeds-money forfeiture judgment against Harriet, but it was insufficient to support the money-laundering forfeiture judgment against her. Therefore, the proceeds-money forfeiture judgment is affirmed with respect to both Warshak and Harriet, and the money-laundering money judgment is affirmed with respect to Warshak, but reversed with respect to Harriet.</p>
<p id="b302-3"><page-number citation-index="1" label="276">*276</page-number>I. STATEMENT OF THE FACTS</p>
<p id="Adx">A. Factual Background</p>
<p id="b302-4">In 2001, Steven Warshak (“Warshak”) owned and operated a number of small businesses in the Cincinnati area. One of his businesses was TCI Media, Inc. (“TCI”), which sold advertisements in sporting venues. Warshak also owned a handful of companies that offered a modest line of so-called “nutraceuticals,” or herbal supplements.<footnotemark>1</footnotemark> While the companies bore different names and sold different products, they appear to have been run as a single business, and they were later aggregated to form Berkeley Premium Nutraceuticals, Inc. (“Berkeley”).<footnotemark>2</footnotemark> In Berkeley’s early days, the company’s workforce was relatively minute; the company employed approximately 12 to 15 people, nearly all of whom were Warshak’s friends and family. Among them was his mother, Harriet Warshak (“Harriet”), who processed credit-card payments.</p>
<p id="b302-5">As the company grew, Warshak brought on additional employees to facilitate expansion, but he remained extremely “hands-on” with respect to the company’s operations. In 2001, he hired James Teegarden, who eventually became Berkeley’s Chief Operating Officer. Warshak also hired Shelley Kinmon to oversee the company’s sales, later elevating her to the role of Vice-President. In 2002, Sue and Greg Cossman, Warshak’s sister and brother-in-law, joined the company. Sue worked in Customer Care, where she dealt with customer complaints. Greg came in as the President of the company and thereafter functioned in various other capacities. That year also saw the hiring of Sam Grote, who was brought on board to work in the marketing department.</p>
<p id="b302-10">To sell its products, Berkeley took orders over the phone, but it also made sales through the mail and over the Internet. Customers purchased products with their credit cards, and their credit-card numbers were entered into a database along with other information. During sales calls, representatives would read from sales scripts,<footnotemark>3</footnotemark> which listed the major points to cover during the transaction. Shelley Kinmon testified that Warshak had the final word on the content of the scripts. Often, the scripts would include a description of the desired product, as well as language intended to persuade more pliant customers to make additional purchases.</p>
<p id="b302-11">In the latter half of 2001, Berkeley launched Enzyte, its flagship product. At the time of its launch, Enzyte was purported to increase the size of a man’s erection. The product proved tremendously popular, and business rose sharply. By 2004, demand for Berkeley’s products had grown so dramatically that the company employed 1500 people, and the call center remained open throughout the night, taking orders at breakneck speed. Berkeley’s line of supplements also expanded, ballooning from approximately four products to around thirteen. By year’s end, Berkeley’s annual sales topped out at around $250 million, largely on the strength of Enzyte.</p>
<p id="b303-4"><page-number citation-index="1" label="277">*277</page-number>1. <em>Advertising</em></p>
<p id="b303-5">The popularity of Enzyte appears to have been due in large part to Berkeley’s aggressive advertising campaigns. The vast majority of the advertising — approximately 98% — was conducted through television spots. Around 2004, network television was saturated with Enzyte advertisements featuring a character called “Smilin’ Bob,” whose trademark exaggerated smile was presumably the result of Enzyte’s efficacy. The “Smilin’ Bob” commercials were rife with innuendo and implied that users of Enzyte would become the envy of the neighborhood.</p>
<p id="b303-6">In addition to the television commercials, however, there were also advertisements in other media, such as print and radio. In 2001, just after Enzyte’s premiere, advertisements appeared in a number of men’s interest magazines. At Warshak’s direction, those advertisements cited a 2001 independent customer study, which purported to show that, over a three-month period, 100 English-speaking men who took Enzyte experienced a 12 to 31% increase in the size of their penises. The 2001 study was also referenced in radio advertisements and appeared on the company’s website, as well as in brochures and sales calls. James Teegarden later testified that the survey was bogus. He stated that, prior to the appearance of the advertisements, Warshak instructed him to create a spreadsheet and to fill it with fabricated data. Teegarden testified that he plucked the numbers out of the air and generated the spreadsheet over a twenty-four hour period.</p>
<p id="b303-7">A number of advertisements also indicated that Enzyte boasted a 96% customer satisfaction rating. Teegarden testified that that statistic, too, was totally spurious. Before the claim began showing up in Berkeley’s literature, Warshak had asked him to harvest 500 names from the customer database and to “mark an ‘X’ by either satisfied or very satisfied on say 475 of those.” As for the remaining 25, Tee-garden “was to put not satisfied.” Thereafter, the customer-satisfaction statistic cropped up in Berkeley’s print advertisements and in the “sales pitches, brochures, [and on the] Internet.”</p>
<p id="b303-11">Finally, numerous print and radio advertisements boasted that Enzyte was the brainchild of reputable doctors with impressive educational pedigrees. According to the ads, “Enzyte was developed by Dr. Fredrick Thomkins, a physician with a biology degree from Stanford and Dr. Michael Moore, a leading urologist from Harvard.” The ads also stated that the doctors had collaborated for thirteen years in developing a supplement designed to “stretch and elongate.” In reality, the doctors were just as fictitious as “Smilin’ Bob.” Investigators who contacted Stanford and Harvard learned that neither man existed.</p>
<p id="b303-12">2. <em>The Auto-Ship Program</em></p>
<p id="b303-13">The “life blood” of the business was its auto-ship program, which was instituted in 2001, shortly before Enzyte hit the market.<footnotemark>4</footnotemark> The auto-ship program was a continuity or negative-option program, in which a customer would order a free trial of a product and then continue to receive additional shipments of that product until he opted out. Before each new continuity shipment arrived on the customer’s doorstep, a corresponding charge would appear on his credit-card statement. The shipments and charges would continue until the customer decided to withdraw from the <page-number citation-index="1" label="278">*278</page-number>program, which required the customer to notify the company.</p>
<p id="b304-4">In the early days of the auto-ship program, customers who ordered products over the phone were not told that they were being enrolled.<footnotemark>5</footnotemark> From August 2001 to at least the end of December 2002,<footnotemark>6</footnotemark> customers were simply added to the program at the time of the initial sale without any indication that they would be on the hook for additional charges. Apparently, products were shipped with literature explaining the program, but no authorization was sought in advance of the shipment. According to Teegarden, Warshak explained that the auto-ship program was never mentioned because “nobody would sign up.” If nobody signed up, “you couldn’t make revenue.”</p>
<p id="b304-5">This policy resulted in a substantial volume of complaints, both to Berkeley and to outside organizations. In October 2002, the Better Business Bureau (“BBB”) contacted Berkeley and indicated that more than 1,500 customers had called to voice their consternation. Because of the complaints, Berkeley’s sales scripts and website began to include some language disclosing the auto-ship program.<footnotemark>7</footnotemark> A number of internal emails indicate that sales representatives were required to read the disclosure language and faced punishment if they failed to do so. To monitor the interactions between representatives and customers, Berkeley installed a recording system for all incoming calls.</p>
<p id="b304-12">However, as a number of Berkeley insiders testified, the compulsory disclosure language was not always read, and it was designed not to work. Shelley Kinmon testified that the disclosure of the continuity shipments was only made <em>after </em>the customer had placed his order. In other words, the sales representative had already taken the customer’s credit-card information when auto-ship was mentioned. Also, the disclosures were deliberately made with haste, and they were placed after unrelated language that was intended to divert or deaden the customer’s attention. In the case of Enzyte, sales reps were instructed to lead into the disclosure language by stating that “the product is not a contraceptive nor will it prevent or treat any sexually transmitted disease.”<footnotemark>8</footnotemark> According to Teegarden, the thinking was that, “if we started off with a statement about a contraceptive, something other than what it was, that people wouldn’t really listen to what we were disclosing to them.”</p>
<p id="b305-4"><page-number citation-index="1" label="279">*279</page-number>Moreover, disclosure of the auto-ship program was sometimes irrelevant. For example, in November 2003, Berkeley hired a company called West to handle “sales calls that were from ... Avlimil or Enzyte advertisements.” During the calls, West’s representatives asked customers if they wanted to be enrolled in the auto-ship program, and over 80% of customers declined. When Warshak learned what was happening, he issued instructions to “take those customers, even if they decline[d], even if they said no to the Auto-Ship program, go ahead and put them on the Auto-Ship program.” A subsequent email between Berkeley employees indicated that “all [West] customers, whether they know it or not, are going on [auto-ship].” As a result, numerous telephone orders resulted in unauthorized continuity shipments.</p>
<p id="b305-5">However, not all of Berkeley’s auto-ship issues related to the telephone. Many Berkeley sales were the result of orders placed on the Internet, where disclosure of the auto-ship program was inconsistent. In 2001, when Berkeley was in its infancy, the company’s websites contained no indication that customers would be enrolled in the program. Thereafter, disclosures were placed on the websites, but the disclosures would “appear[ ], disappear[ ], and chang[e].” In 2003, for instance, disclosure language that had been added to Berkeley’s Avlimil website was removed because sales had been “drastically affected.” Additionally, the language that did appear was often confusing and contained non sequiturs.</p>
<p id="b305-6">By July 2004, the complaints arising from Berkeley’s auto-ship program had not slowed, so the President of the BBB reached out to Berkeley, sending a letter directly to Warshak. The purpose of the letter was to express “serious concerns about the number of complaints that [the BBB] had received.” The complaints “related to a single issue, which was the [auto-ship] program.” According to the President of the BBB, the organization “had asked on numerous occasions that [Berkeley] consider dropping [the program], and got no positive response.”</p>
<p id="b305-10">3. <em>The Merchant Banks</em></p>
<p id="b305-11">In order for Berkeley’s business to operate, it was essential that the company be able to accept credit cards as a form of payment.<footnotemark>9</footnotemark> To process credit-card transactions, Berkeley obtained lines of credit from several merchant banks. The relationships between Berkeley and the merchant banks involved intermediaries known as credit-card processors. Often, the processors had contractual agreements with the merchant banks, and the processors were the ones who set up the credit-card processing arrangements with Berkeley. Nonetheless, when Berkeley applied for a merchant account with a given processor, the applications were passed along to the banks. Furthermore, either the banks or the processors could terminate Berkeley’s merchant accounts.</p>
<p id="b305-12">In early 2002, Warshak’s merchant account at the Bank of Kentucky was terminated for excessive “chargebacks.” A chargeback occurs when a customer calls the credit card company directly and contests or disputes a charge. Merchant banks — and credit-card processors — will generally not do business with merchants that experience high volumes of charge-backs, as those merchants present a greater financial risk. In determining whether <page-number citation-index="1" label="280">*280</page-number>a merchant is experiencing excessive chargebacks, the banks refer to a figure known as the chargeback ratio, which is simply the percentage of transactions in a given 30-day period that result in a chargeback. For example, if a company conducts 100 credit-card transactions and one chargeback results, the company will have a chargeback ratio of 1%. Typically, if a merchant experiences more than one chargeback per hundred transactions, its chargeback ratio is deemed too high, resulting in fines and, eventually, termination of its accounts, either by the merchant bank or the credit-card processor.</p>
<p id="b306-4">Following the termination of the merchant account at the Bank of Kentucky, the company applied for merchant accounts with a number of other banks. In some instances, the applications, which often bore Harriet’s signature, falsely listed her as the CEO and 100% owner of the company. In other instances, Warshak would complete the applications in his own name but falsely claim that he had never had a merchant account terminated. These prevarications were included in the applications because the prior termination would likely diminish Berkeley’s chances of securing the services of other processors.</p>
<p id="b306-5">Despite its history with the Bank of Kentucky, Berkeley was able to land (or retain) merchant accounts with several processors. However, due to the auto-ship program and an extremely onerous refund policy,<footnotemark>10</footnotemark> Berkeley was repeatedly at risk of crossing the critical 1% chargeback threshold.<footnotemark>11</footnotemark> At company meetings, the chargeback ratio was a frequent topic of discussion, as was the possibility that Berkeley’s accounts would be terminated. To prevent that from happening, a number of strategies were devised to artificially inflate the number of sales transactions and thus the denominator of the charge-back ratio, reducing that crucial ratio. One strategy was called “double-dinging.” That practice involved splitting a single transaction into two, thereby driving up the number of transactions and diminishing the chargeback ratio. A double-ding might entail carving a $59.95 charge into a $54.95 charge for the product itself and a $5.00 charge for shipping. Warshak directed that virtually all sales be double-dinged, and by 2003, triple-dinging was initiated.</p>
<p id="b306-8">Another way the company depressed the chargeback ratio was to make numerous charges to Warshak’s personal credit cards. At Warshak’s behest, Berkeley employees would ring up $1.00 charges on each of his credit cards until their limits were reached. Apparently, the thinking <page-number citation-index="1" label="281">*281</page-number>was that this torrent of additional transactions would dilute the number of charge-backs and keep the ratio under 1%. The same thinking led the company to charge and then refund the credit cards of randomly selected customers. The charges were made without authorization, and if anyone complained about the odd activity on his card, he was told that it was the result of a computer glitch. Through the use of these techniques and others, the company was able to stave off termination of its merchant-bank accounts.</p>
<p id="b307-5">B. Procedural History</p>
<p id="b307-6">In September 2006, a grand jury sitting-in the Southern District of Ohio returned a 112-count indictment charging Warshak, Harriet, TCI, and several others with various crimes related to Berkeley’s business. Warshak was charged with conspiracy to commit mail, wire, and bank fraud (Count 1); mail fraud (Counts 2-13); making false statements to banks (Counts 14,16-22, 24-26, 28); bank fraud (Counts 15, 23, 27); conspiracy to commit and attempt to commit access-device fraud (Count 29); conspiracy to commit money laundering (Count 34); money laundering (Counts 32-98, 102-106, 108); conspiracy to commit misbranding (Count 109); misbranding (Count 110); and, lastly, conspiracy to obstruct a Federal Trade Commission (“FTC”) proceeding (Count 112). Harriet was charged with conspiracy to commit mail, wire, and bank fraud (Count 1); bank fraud (Count 27); making false statements to a bank (Count 28); conspiracy to commit money laundering (Counts 30-31); and money laundering (Counts 99-101, 107). TCI was charged with money laundering (Counts 57-58, 60-73, 79, 83, 91-93).</p>
<p id="b307-7">Before trial, numerous motions were filed. First, Warshak moved to exclude thousands of emails that the government obtained from his Internet Service Providers. That motion was denied. Warshak also moved to bar the government from using any evidence “derived through improper access to privileged attorney-client communications.” Appellant’s Br. at 42. Following a <em>“Kastigar-like” </em>evidentiary hearing at which governmental inspectors testified that they did not make use of any privileged materials, the district court denied the motion. In addition, the defendants requested a continuance, which was denied.</p>
<p id="b307-9">Over fifteen months later, in January 2008, the case proceeded to trial. Approximately six weeks later, the trial ended and the defendants were convicted of the majority of the charges. Warshak was acquitted of Counts 14-22, 24-26, and 28, which charged him with making false statements to banks, and he was also acquitted of Counts 109-110, which charged him with misbranding offenses. Harriet was acquitted of Count 28, which alleged that she made false statements to a bank. She was convicted on Counts 27, 30-31, 99-101, and 107.</p>
<p id="b307-10">As soon as the trial was over, a forfeiture hearing was held, during which the jury heard additional evidence. At the hearing, the defendants attempted to introduce certain evidence that many of Berkeley’s sales were legitimate, but the district court ruled that the evidence was irrelevant. When the hearing concluded, the jury found that the government had established the requisite nexus between certain assets and the crimes of both fraud and money laundering.</p>
<p id="b307-11">On August 27, 2008, the defendants were sentenced. Warshak received a sentence of 25 years of imprisonment. He was also ordered to pay a fine of $93,000 and a special assessment of $9,300. In addition, he was ordered to surrender $459,540,000 in proceeds-money-judgment forfeiture and $44,876,781.68 in money-laundering-<page-number citation-index="1" label="282">*282</page-number>judgment forfeiture. Harriet was sentenced to 24 months of imprisonment, ordered to pay a special assessment of $800, and held jointly and severally liable for the forfeiture judgments. TCI was sentenced to five years of probation and ordered to pay a fine of $160,000 and a special assessment of $6,400.</p>
<p id="b308-4">Following a series of unsuccessful post-trial motions, the defendants timely appealed.</p>
<p id="b308-5">II. ANALYSIS</p>
<p id="b308-6">A. The Search &amp; Seizure of Warshak’s Emails</p>
<p id="b308-7">Warshak argues that the government’s warrantless, <em>ex parte </em>seizure of approximately 27,000 of his private emails constituted a violation of the Fourth Amendment’s prohibition on unreasonable searches and seizures.<footnotemark>12</footnotemark> The government counters that, even if government agents violated the Fourth Amendment in obtaining the emails, they relied in good faith on the Stored Communications Act (“SCA”), <span class="citation no-link">18 U.S.C. §§ 2701</span> et seq., a statute that allows the government to obtain certain electronic communications without procuring a warrant. The government also argues that any hypothetical Fourth Amendment violation was harmless. We find that the government <em>did </em>violate Warshak’s Fourth Amendment rights by compelling his Internet Service Provider (“ISP”) to turn over the contents of his emails. However, we agree that agents relied on the SCA in good faith, and therefore hold that reversal is unwarranted.<footnotemark>13</footnotemark></p>
<p id="b308-11">1. <em>The Stored Communications Act</em></p>
<p id="b308-12">The Stored Communications Act (“SCA”), <span class="citation no-link">18 U.S.C. §§ 2701</span> et seq., “permits a ‘governmental entity’ to compel a service provider to disclose the contents of [electronic] communications in certain circumstances.” <em>Warshak II, </em>532 F.3d at 523. As this court explained in <em>Warshak II:</em></p>
<blockquote id="b308-13">Three relevant definitions bear on the meaning of the compelled-diselosure provisions of the Act. “[Electronic communication service[s]” permit “users ... to send or receive wire or electronic communications,” [18 U.S.C.] § 2510(15), a definition that covers basic e-mail services, <em>see </em>Patricia L. Bellia et ah, <em>Cyberlaw: Problems of Policy and Jurisprudence in the Information Age 584 </em>(2d ed. 2004). “[Electronic storage” is “any temporary, intermediate storage of a wire or electronic communication ... and ... any storage of such communication by an electronic communication ser<page-number citation-index="1" label="283">*283</page-number>vice for purposes of backup protection of such communication.” <span class="citation no-link">18 U.S.C. § 2510</span>(17). “[RJemote computing serviced” provide “computer storage or processing services” to customers, <em><span class="citation no-link">id.</span> </em>§ 2711(2), and are designed for longer-term storage, <em>see </em>Orín S. Kerr, <em>A User’s Guide to the Stored Communications Act, and a Legislator’s Guide to Amending It, </em>72 Geo. Wash. L.Rev. 1208, 1216 (2004).</blockquote>
<blockquote id="b309-5">The compelled-disclosure provisions give different levels of privacy protection based on whether the e-mail is held with an electronic communication service or a remote computing service and based on how long the e-mail has been in electronic storage. The government may obtain the contents of e-mails that are “in electronic storage” with an electronic communication service for 180 days or less “only pursuant to a warrant.” <span class="citation no-link">18 U.S.C. § 2703</span>(a). The government has three options for obtaining communications stored with a remote computing service and communications that have been in electronic storage with an electronic service provider for more than 180 days: (1) obtain a warrant; (2) use an administrative subpoena; or (3) obtain a court order under § 2703(d). <em>Id. </em>§ 2703(a), (b).</blockquote>
<p id="b309-6">532 F.3d at 523-24 (some alterations in original).</p>
<p id="b309-7">2. <em>Factual Background</em></p>
<p id="b309-8">Email was a critical form of communication among Berkeley personnel. As a consequence, Warshak had a number of email accounts with various ISPs, including an account with NuVox Communications. In October 2004, the government formally requested that NuVox prospectively preserve the contents of any emails to or from Warshak’s email account. The request was made pursuant to <span class="citation no-link">18 U.S.C. § 2703</span>(f) and it instructed NuVox to preserve all future messages.<footnotemark>14</footnotemark> NuVox acceded to the government’s request and began preserving copies of Warshak’s incoming and outgoing emails — copies that would not have existed absent the prospective preservation request. Per the government’s instructions, Warshak was not informed that his messages were being archived.</p>
<p id="b309-11">In January 2005, the government obtained a subpoena under § 2703(b) and compelled NuVox to turn over the emails that it had begun preserving the previous year. In May 2005, the government served NuVox with an <em>ex parte </em>court order under § 2703(d) that required NuVox to surrender any additional email messages in Warshak’s account. In all, the government compelled NuVox to reveal the contents of approximately 27,000 emails. Warshak did not receive notice of either the subpoena or the order until May 2006.</p>
<p id="b309-12">3. <em>The Fourth Amendment</em></p>
<p id="b309-13">The Fourth Amendment provides that “[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause.... ” U.S. Const, amend. IV. The fundamental purpose of the Fourth Amendment “is to safeguard the privacy and security of individuals against arbitrary invasions by government officials.” <em>Camara v. Mun. Ct., </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U.S. 523, 528</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">87 S.Ct. 1727</a></span>, <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">18 L.Ed.2d 930</a></span> (1967); <em>see Skinner v. Ry. Labor Execs.’ Ass’n, </em><span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/#613" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">489 U.S. 602, 613-14</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">109 S.Ct. 1402</a></span>, <span class="citation" data-id="9431606"><a href="/opinion/112219/skinner-v-railway-labor-executives-assn/" aria-description="Citation for case: Skinner v. Railway Labor Executives&#x27; Assn.">103 L.Ed.2d 639</a></span> (1989) (“The [Fourth] Amend<page-number citation-index="1" label="284">*284</page-number>ment guarantees the privacy, dignity, and security of persons against certain arbitrary and invasive acts by officers of the Government or those acting at their direction.”).</p>
<p id="b310-4">Not all government actions are invasive enough to implicate the Fourth Amendment. “The Fourth Amendment’s protections hinge on the occurrence of a ‘search,’ a legal term of art whose history is riddled with complexity.” <em>Widgren v. Maple Grove Twp., </em><span class="citation" data-id="792467"><a href="/opinion/792467/kenneth-d-widgren-jr-and-kenneth-d-widgren-sr-v-maple-grove-township/#578" aria-description="Citation for case: Kenneth D. Widgren, Jr. And Kenneth D. Widgren, Sr. v....">429 F.3d 575, 578</a></span> (6th Cir.2005). A “search” occurs when the government infringes upon “an expectation of privacy that society is prepared to consider reasonable.” <em>United States v. Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#113" aria-description="Citation for case: United States v. Jacobsen">466 U.S. 109, 113</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">104 S.Ct. 1652</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">80 L.Ed.2d 85</a></span> (1984). This standard breaks down into two discrete inquiries: “first, has the [target of the investigation] manifested a subjective expectation of privacy in the object of the challenged search? Second, is society willing to recognize that expectation as reasonable?” <em>California v. Ciraolo, </em><span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/#211" aria-description="Citation for case: California v. Ciraolo">476 U.S. 207, 211</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">106 S.Ct. 1809</a></span>, <span class="citation" data-id="9430502"><a href="/opinion/111666/california-v-ciraolo/" aria-description="Citation for case: California v. Ciraolo">90 L.Ed.2d 210</a></span> (1986) (citing <em>Smith v. Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U.S. 735, 740</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">61 L.Ed.2d 220</a></span> (1979)).</p>
<p id="b310-5">Turning first to the subjective component of the test, we find that Warshak plainly manifested an expectation that his emails would be shielded from outside scrutiny. As he notes in his brief, his “entire business and personal life was contained within the ... emails seized.” Appellant’s Br. at 39-40. Given the often sensitive and sometimes damning substance of his emails,<footnotemark>15</footnotemark> we think it highly unlikely that Warshak expected them to be made public, for people seldom unfurl their dirty laundry in plain view. <em>See, e.g., United States v. Maxwell, </em><span class="citation" data-id="7269941"><a href="/opinion/7351719/united-states-v-maxwell/#417" aria-description="Citation for case: United States v. Maxwell">45 M.J. 406, 417</a></span> (C.A.A.F.1996) (“[T]he tenor and content of e-mail conversations between appellant and his correspondent, ‘Launehboy,’ reveal a[n] ... expectation that the conversations were private.”). Therefore, we conclude that Warshak had a subjective expectation of privacy in the contents of his emails.</p>
<p id="b310-8">The next question is whether society is prepared to recognize that expectation as reasonable. <em>See Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#740" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 740</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span>. This question is one of grave import and enduring consequence, given the prominent role that email has assumed in modern communication. <em>Cf. Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U.S. at 352</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span> (suggesting that the Constitution must be read to account for “the vital role that the public telephone has come to play in private communication”). Since the advent of email, the telephone call and the letter have waned in importance, and an explosion of Internet-based communication has taken place. People are now able to send sensitive and intimate information, instantaneously, to friends, family, and colleagues half a world away. Lovers exchange sweet nothings, and businessmen swap ambitious plans, all with the click of a mouse button. Commerce has also taken hold in email. Online purchases are often documented in email accounts, and email is frequently used to remind patients and clients of imminent appointments. In short, “account” is an apt word for the conglomeration of stored messages that comprises an email account, as it provides an account of its owner’s life. By obtaining access to someone’s email, government agents gain the ability to peer deeply into his activities. Much hinges, therefore, on whether the government is permitted to request that a commercial ISP turn over the contents of a subscriber’s emails without triggering the machinery of the Fourth Amendment.</p>
<p id="b311-4"><page-number citation-index="1" label="285">*285</page-number>In confronting this question, we take note of two bedrock principles. First, the very fact that information is being passed through a communications network is a paramount Fourth Amendment consideration. <em>See ibid.; United States v. U.S. Dist. Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. 297, 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">32 L.Ed.2d 752</a></span> (1972) (“[T]he broad and unsuspected governmental incursions into conversational privacy which electronic surveillance entails necessitate the application of Fourth Amendment safeguards.”). Second, the Fourth Amendment must keep pace with the inexorable march of technological progress, or its guarantees will wither and perish. <em>See Kyllo v. United States, </em><span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/#34" aria-description="Citation for case: Kyllo v. United States">533 U.S. 27, 34</a></span>, <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">121 S.Ct. 2038</a></span>, <span class="citation" data-id="9434104"><a href="/opinion/118443/kyllo-v-united-states/" aria-description="Citation for case: Kyllo v. United States">150 L.Ed.2d 94</a></span> (2001) (noting that evolving technology must not be permitted to “erode the privacy guaranteed by the Fourth Amendment”); <em>see also </em>Orín S. Kerr, <em>Applying the Fourth Amendment to the Internet: A General Approach, </em>62 Stan. L.Rev. 1005, 1007 (2010) (arguing that “the differences between the facts of physical space and the facts of the Internet require courts to identify new Fourth Amendment distinctions to maintain the function of Fourth Amendment rules in an online environment”).</p>
<p id="b311-5">With those principles in mind, we begin our analysis by considering the manner in which the Fourth Amendment protects traditional forms of communication. In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Supreme Court was asked to determine how the Fourth Amendment applied in the context of the telephone. There, government agents had affixed an electronic listening device to the exterior of a public phone booth, and had used the device to intercept and record several phone conversations. <em>See </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#348" aria-description="Citation for case: Katz v. United States">389 U.S. at 348</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>. The Supreme Court held that this constituted a search under the Fourth Amendment, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States"><em>see id. </em>at 353</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>, notwithstanding the fact that the telephone company had the capacity to monitor and record the calls, <em>see Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#746" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 746-47</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span> (Stewart, J., dissenting). In the eyes of the Court, the caller was “surely entitled to assume that the words he utter[ed] into the mouthpiece w[ould] not be broadcast to the world.” <em>Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U.S. at 352</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>. The Court’s holding in <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>has since come to stand for the broad proposition that, in many contexts, the government infringes a reasonable expectation of privacy when it surreptitiously intercepts a telephone call through electronic means. <em>Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#746" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 746</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span> (Stewart, J., dissenting) (“[S]ince <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>it has been abundantly clear that telephone conversations are fully protected by the Fourth and Fourteenth Amendments.”).</p>
<p id="b311-7">Letters receive similar protection. <em>See Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#114" aria-description="Citation for case: United States v. Jacobsen">466 U.S. at 114</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">104 S.Ct. 1652</a></span> (“Letters and other sealed packages are in the general class of effects in which the public at large has a legitimate expectation of privacy[.]”); <em>Ex Parte Jackson, </em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U.S. 727, 733</a></span>, <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">24 L.Ed. 877</a></span> (1877). While a letter is in the mail, the police may not intercept it and examine its contents unless they first obtain a warrant based on probable cause. <em><span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/" aria-description="Citation for case: Ex Parte Jackson">Ibid.</a></span> </em>This is true despite the fact that sealed letters are handed over to perhaps dozens of mail carriers, any one of whom could tear open the thin paper envelopes that separate the private words from the world outside. Put another way, trusting a letter to an intermediary does not necessarily defeat a reasonable expectation that the letter will remain private. <em>See Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U.S. at 351</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span> (“[W]hat [a person] seeks to preserve as private, even in an area accessible to the public, may be constitutionally protected.”).</p>
<p id="b311-8">Given the fundamental similarities between email and traditional forms of communication, it would defy common sense <page-number citation-index="1" label="286">*286</page-number>to afford emails lesser Fourth Amendment protection. <em>See </em>Patricia L. Bellia &amp; Susan Freiwald, <em>Fourth Amendment Protection for Stored E-Mail, </em><span class="citation no-link">2008 U. Chi. Legal F. 121</span>, 135 (2008) (recognizing the need to “eliminate the strangely disparate treatment of mailed and telephonic communications on the one hand and electronic communications on the other”); <em>City of Ontario v. Quon, </em>— U.S. -, <span class="citation" data-id="6681698"><a href="/opinion/6796843/city-of-ontario-v-quon/#2631" aria-description="Citation for case: City of Ontario v. Quon">130 S.Ct. 2619, 2631</a></span>, <span class="citation" data-id="6681698"><a href="/opinion/6796843/city-of-ontario-v-quon/" aria-description="Citation for case: City of Ontario v. Quon">177 L.Ed.2d 216</a></span> (2010) (implying that “a search of [an individual’s] personal e-mail account” would be just as intrusive as “a wiretap on his home phone line”); <em>United States v. Forrester, </em><span class="citation" data-id="1445123"><a href="/opinion/1445123/united-states-v-forrester/#511" aria-description="Citation for case: United States v. Forrester">512 F.3d 500, 511</a></span> (9th Cir.2008) (holding that “[t]he privacy interests in [mail and email] are identical”). Email is the technological scion of tangible mail, and it plays an indispensable part in the Information Age. Over the last decade, email has become “so pervasive that some persons may consider [it] to be [an] essential means or necessary instrument! ] for self-expression, even self-identification.” <em>Quon, </em><span class="citation" data-id="6681698"><a href="/opinion/6796843/city-of-ontario-v-quon/#2630" aria-description="Citation for case: City of Ontario v. Quon">130 S.Ct. at 2630</a></span>. It follows that email requires strong protection under the Fourth Amendment; otherwise, the Fourth Amendment would prove an ineffective guardian of private communication, an essential purpose it has long been recognized to serve. <em>See U.S. Dist. Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U.S. at 313</a></span>, <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">92 S.Ct. 2125</a></span>; <em>United States v. Waller, </em><span class="citation" data-id="358724"><a href="/opinion/358724/united-states-v-irvin-j-waller/#587" aria-description="Citation for case: United States v. Irvin J. Waller">581 F.2d 585, 587</a></span> (6th Cir.1978) (noting the Fourth Amendment’s role in protecting “private communications”). As some forms of communication begin to diminish, the Fourth Amendment must recognize and protect nascent ones that arise. <em>See Warshak I, </em>490 F.3d at 473 (“It goes without saying that like the telephone earlier in our history, e-mail is an ever-increasing mode of private communication, and protecting shared communications through this medium is as important to Fourth Amendment principles today as protecting telephone conversations has been in the past.”).</p>
<p id="b312-7">If we accept that an email is analogous to a letter or a phone call, it is manifest that agents of the government cannot compel a commercial ISP to turn over the contents of an email without triggering the Fourth Amendment. An ISP is the intermediary that makes email communication possible. Emails must pass through an ISP’s servers to reach their intended recipient. Thus, the ISP is the functional equivalent of a post office or a telephone company. As we have discussed above, the police may not storm the post office and intercept a letter, and they are likewise forbidden from using the phone system to make a clandestine recording of a telephone call — unless they get a warrant, that is. <em>See Jacobsen, </em><span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/#114" aria-description="Citation for case: United States v. Jacobsen">466 U.S. at 114</a></span>, <span class="citation" data-id="9429558"><a href="/opinion/111143/united-states-v-jacobsen/" aria-description="Citation for case: United States v. Jacobsen">104 S.Ct. 1652</a></span>; <em>Katz, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#353" aria-description="Citation for case: Katz v. United States">389 U.S. at 353</a></span>, <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span>. It only stands to reason that, if government agents compel an ISP to surrender the contents of a subscriber’s emails, those agents have thereby conducted a Fourth Amendment search, which necessitates compliance with the warrant requirement absent some exception.</p>
<p id="b312-8">In <em>Warshak I, </em>the government argued that this conclusion was improper, pointing to the fact that NuVox contractually reserved the right to access Warshak’s emails for certain purposes. While we acknowledge that a subscriber agreement might, in some cases, be sweeping enough to defeat a reasonable expectation of privacy in the contents of an email account, <em>see Warshak I, </em>490 F.3d at 473; <em>Warshak II, </em>532 F.3d at 526-27, we doubt that will be the case in most situations, and it is certainly not the case here.</p>
<p id="b312-9">As an initial matter, it must be observed that the mere <em>ability </em>of a third-party intermediary to access the contents of a communication cannot be sufficient to extinguish a reasonable expectation of priva<page-number citation-index="1" label="287">*287</page-number>cy. In <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the Supreme Court found it reasonable to expect privacy during a telephone call despite the ability of an operator to listen in. <em>See Smith, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#746" aria-description="Citation for case: Smith v. Maryland">442 U.S. at 746-47</a></span>, <span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/" aria-description="Citation for case: Smith v. Maryland">99 S.Ct. 2577</a></span> (Stewart, J., dissenting). Similarly, the ability of a rogue mail handler to rip open a letter does not make it unreasonable to assume that sealed mail will remain private on its journey across the country. Therefore, the threat or possibility of access is not decisive when it comes to the reasonableness of an expectation of privacy.</p>
<p id="b313-5">Nor is the <em>right </em>of access. As the Electronic Frontier Foundation points out in its <em>amicus </em>brief, at the time <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>was decided, telephone companies had a right to monitor calls in certain situations. Specifically, telephone companies could listen in when reasonably necessary to “protect themselves and their properties against the improper and illegal use of their facilities.” <em>Bubis v. United States, </em><span class="citation" data-id="277548"><a href="/opinion/277548/alvin-bubis-v-united-states/#648" aria-description="Citation for case: Alvin Bubis v. United States">384 F.2d 643, 648</a></span> (9th Cir.1967). In this case, the NuVox subscriber agreement tracks that language, indicating that “NuVox <em>may </em>access and use individual Subscriber information in the operation of the Service and as necessary to protect the Service.” Acceptable Use Policy, <em>available at </em>http:// business.windstream.com/Legal/acceptable Use.htm (last visited Aug. 12, 2010). Thus, under <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>the degree of access granted to NuVox does not dimmish the reasonableness of Warshak’s trust in the privacy of his emails.<footnotemark>16</footnotemark></p>
<p id="b313-6">Our conclusion finds additional support in the application of Fourth Amendment doctrine to rented space. Hotel guests, for example, have a reasonable expectation of privacy in their rooms. <em>See United States v. Allen, </em><span class="citation" data-id="735355"><a href="/opinion/735355/united-states-v-russell-b-allen/#699" aria-description="Citation for case: United States v. Russell B. Allen">106 F.3d 695, 699</a></span> (6th Cir.1997). This is so even though maids routinely enter hotel rooms to replace the towels and tidy the furniture. Similarly, tenants have a legitimate expectation of privacy in their apartments. <em>See United States v. Washington, </em><span class="citation" data-id="1448043"><a href="/opinion/1448043/united-states-v-washington/#284" aria-description="Citation for case: United States v. Washington">573 F.3d 279, 284</a></span> (6th Cir.2009). That expectation persists, regardless of the incursions of handymen to fix leaky faucets. Consequently, we are convinced that some degree of routine access is hardly dispositive with respect to the privacy question.</p>
<p id="b313-9">Again, however, we are unwilling to hold that a subscriber agreement will <em>never </em>be broad enough to snuff out a reasonable expectation of privacy. As the panel noted in <em>Warshak I, </em>if the ISP expresses an intention to “audit, inspect, and monitor” its subscriber’s emails, that might be enough to render an expectation of privacy unreasonable. <em>See </em>490 F.3d at 472-73 (quoting <em>United States v. Simons, </em><span class="citation" data-id="767973"><a href="/opinion/767973/united-states-v-mark-l-simons/#398" aria-description="Citation for case: United States v. Mark L. Simons">206 F.3d 392, 398</a></span> (4th Cir.2000)). But where, as here, there is no such statement, the ISP’s “control over the [emails] and ability to access them under certain limited circumstances will not be enough to overcome an expectation of privacy.” <span class="citation" data-id="767973"><a href="/opinion/767973/united-states-v-mark-l-simons/#473" aria-description="Citation for case: United States v. Mark L. Simons"><em>Id. </em>at 473</a></span>.</p>
<p id="b313-10">We recognize that our conclusion may be attacked in light of the Supreme Court’s decision in <em>United States v. Miller, </em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">425 U.S. 435</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">96 S.Ct. 1619</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">48 L.Ed.2d 71</a></span> (1976). In <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span>, </em>the Supreme Court held that a bank depositor does not have a reasonable expectation of privacy in the contents of bank records, checks, and deposit slips. <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#442" aria-description="Citation for case: United States v. Miller"><em>Id. </em>at 442</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">96 S.Ct. 1619</a></span>. The Court’s holding in <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>was based on the fact that bank documents, “including financial statements and deposit slips, contain <page-number citation-index="1" label="288">*288</page-number>only information voluntarily conveyed to the banks and exposed to their employees in the ordinary course of business.” <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Ibid.</a></span> </em>The Court noted,</p>
<blockquote id="b314-4">The depositor takes the risk, in revealing his affairs to another, that the information will be conveyed by that person to the Government.... [T]he Fourth Amendment does not prohibit the obtaining of information revealed to a third party and conveyed by him to Government authorities, even if the information is revealed on the assumption that it will be used only for a limited purpose and the confidence placed in the third party will not be betrayed.</blockquote>
<p id="b314-5"><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/#443" aria-description="Citation for case: United States v. Miller"><em>Id. </em>at 443</a></span>, <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">96 S.Ct. 1619</a></span> (citations omitted).</p>
<p id="b314-6">But <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>is distinguishable. First, <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>involved simple business records, as opposed to the potentially unlimited variety of “confidential communications” at issue here. <em>See <span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">ibid.</a></span> </em>Second, the bank depositor in <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>conveyed information to the bank so that the bank could put the information to use “in the ordinary course of business.” <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Ibid.</a></span> </em>By contrast, Warshak received his emails through NuVox. NuVox was an <em>intermediary, </em>not the intended recipient of the emails. <em>See </em>Bellia &amp; Freiwald, <em>Stored E-Mail, </em>2008 U. Chi. Legal F. at 165 (“[W]e view the best analogy for this scenario as the cases in which a third party carries, transports, or stores property for another. In these cases, as in the stored e-mail case, the customer grants access to the ISP because it is essential to the customer’s interests.”). Thus, <em><span class="citation" data-id="9426375"><a href="/opinion/109433/united-states-v-miller/" aria-description="Citation for case: United States v. Miller">Miller</a></span> </em>is not controlling.</p>
<p id="b314-7">Accordingly, we hold that a subscriber enjoys a reasonable expectation of privacy in the contents of emails “that are stored with, or sent or received through, a commercial ISP.” <em>Warshak I, </em>490 F.3d at 473; <em>see Forrester, </em><span class="citation" data-id="1445123"><a href="/opinion/1445123/united-states-v-forrester/#511" aria-description="Citation for case: United States v. Forrester">512 F.3d at 511</a></span> (suggesting that “[t]he contents [of email messages] may deserve Fourth Amendment protection”). The government may not compel a commercial ISP to turn over the contents of a subscriber’s emails without first obtaining a warrant based on probable cause. Therefore, because they did not obtain a warrant, the government agents violated the Fourth Amendment when they obtained the contents of Warshak’s emails. Moreover, to the extent that the SCA purports to permit the government to obtain such emails warrantlessly, the SCA is unconstitutional.</p>
<p id="b314-9">4. <em>Good-Faith Reliance</em></p>
<p id="b314-10">Even though the government’s search of Warshak’s emails violated the Fourth Amendment, the emails are not subject to the exclusionary remedy if the officers relied in good faith on the SCA to obtain them. <em>See Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#349" aria-description="Citation for case: Illinois v. Krull">480 U.S. at 349-50</a></span>, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">107 S.Ct. 1160</a></span>. In <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span>, </em>the Supreme Court noted that the exclusionary rule’s purpose of deterring law enforcement officers from engaging in unconstitutional conduct would not be furthered by holding officers accountable for mistakes of the legislature. <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span> </em>Thus, even if a statute is later found to be unconstitutional, an officer “cannot be expected to question the judgment of the legislature.” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span> </em>However, an officer cannot “be said to have acted in good-faith reliance upon a statute if its provisions are such that a reasonable officer should have known that the statute was unconstitutional.” <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#355" aria-description="Citation for case: Illinois v. Krull"><em>Id. </em>at 355</a></span>, 107 5. Ct. 1160.</p>
<p id="b314-12">Naturally, Warshak argues that the provisions of the SCA at issue in this case were plainly unconstitutional. He argues that any reasonable law enforcement officer would have understood that a warrant based on probable cause would be required to compel the production of private emails. In making this argument, he leans heavily on <em>Warshak I, </em>which opined that the SCA permits agents to engage in searches “that <page-number citation-index="1" label="289">*289</page-number>clearly do not comport with the Fourth Amendment.” 490 F.3d at 477.</p>
<p id="b315-5">However, we disagree that the SCA is so conspicuously unconstitutional as to preclude good-faith reliance. As we noted in <em>Warshak II, </em>“[t]he Stored Communications Act has been in existence since 1986 and to our knowledge has not been the subject of any successful Fourth Amendment challenges, in any context, whether to § 2703(d) or to any other provision.” 532 F.3d at 531. Furthermore, given the complicated thicket of issues that we were required to navigate when passing on the constitutionality of the SCA, it was not plain or obvious that the SCA was unconstitutional, and it was therefore reasonable for the government to rely upon the SCA in seeking to obtain the contents of Warshak’s emails.<footnotemark>17</footnotemark></p>
<p id="b315-6">But the good-faith reliance inquiry does not end with the facial validity of the statute at issue. In <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span>, </em>the Supreme Court hinted that the good-faith exception does not apply if the government acted “outside the scope of the statute” on which it purported to rely. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U.S. at 360</a></span> n. 17, <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">107 S.Ct. 1160</a></span>. It should be noted that this portion of the <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>Court’s opinion was merely dicta, and it appears that we have yet to pass on the question. However, it seems evident that an officer’s failure to adhere to the boundaries of a given statute should preclude him from relying upon it in the face of a constitutional challenge.<footnotemark>18</footnotemark> Once the officer steps outside the scope of an unconstitutional statute, the mistake is no longer the legislature’s, but the officer’s. <em>See <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">ibid.</a></span> </em>(“In that context, the relevant actors are not legislators or magistrates, but police officers who concededly are engaged in the often competitive enterprise of ferreting out crime.” (citation and internal quotation marks omitted)). Therefore, use of the exclusionary rule is once again efficacious in deterring officers from engaging in conduct that violates the Constitution. <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span></em></p>
<p id="b315-10">Warshak argues that the government violated several provisions of the SCA and should therefore be precluded from arguing good-faith reliance. First, Warshak argues that the government violated the SCA’s notice provisions. Under § 2703(b)(1)(B), the government must provide notice to an account holder if it seeks to compel the disclosure of his emails through either a § 2703(b) subpoena or a § 2703(d) order. However, § 2705 permits the government to delay notification in certain situations. The initial period of delay is 90 days, but the government may seek to extend that period in 90-day increments. In this case, the government issued both a § 2703(b) subpoena and a § 2703(d) order to NuVox, seeking disclosure of Warshak’s emails. At the time, the government made the. requisite showing that notice should be delayed. However, the government did not seek to renew the period of delay. In all, the government failed to inform Warshak of either the subpoena or the order for over a year.</p>
<p id="b315-11">Conceding that it violated the notice provisions, the government argues that such violations are irrelevant to the issue of whether it reasonably relied on the <page-number citation-index="1" label="290">*290</page-number>SCA in <em>obtaining </em>the contents of Warshak’s emails. We agree. As the government notes, the violations occurred <em>after </em>the emails had been obtained. Thus, the mistakes at issue had no bearing on the constitutional violations. Because the exclusionary rule was designed to deter constitutional violations, we decline to invoke it in this situation.</p>
<p id="b316-4">But Warshak does not hang his hat exclusively on the government’s violations of the SCA’s notice provisions. He also argues that the government exceeded its authority under another SCA provision— § 2703(f) — by requesting NuVox to engage in <em>prospective </em>preservation of his future emails.<footnotemark>19</footnotemark> Under § 2703(f), “[a] provider of wire or electronic communication services or a remote computing service, upon the request of a governmental entity, shall take all necessary steps to <em>preserve </em>records and other evidence <em>in its possession </em>pending the issuance of a court order or other process.” <span class="citation no-link">18 U.S.C. § 2703</span>(f) (emphasis added). Warshak argues that this statute permits only <em>retrospective </em>preservation — in other words, preservation of emails already in existence. He notes that the Department of Justice (“DOJ”) generally agrees with his construction of the statute, pointing to the DOJ’s own computer-surveillance manual, which states: “[Section] 2703(f) letters should not be used prospectively to order providers to preserve records not yet created. If agents want providers to record information about future electronic communications, they should comply with the [Wiretap Act and the Pen/Trap statute].”<footnotemark>20</footnotemark></p>
<p id="b316-8">Ultimately, however, this statutory violation, whether it occurred or not,<footnotemark>21</footnotemark> is irrelevant to the issue of good-faith reliance. The question here is whether the government relied in good faith on § 2703(b) and § 2703(d) to <em>obtain </em>copies of Warshak’s emails. True, the government might not have been able to gain access to the emails without the prospective preservation request, as it was NuYox’s practice to delete all emails once they were downloaded to the account holder’s computer. Thus, in a sense, the government’s use of § 2703© was a but-for cause of the constitutional violation. But the actual violation at issue was obtaining the emails, and the government did not rely on § 2703® specifically to do that. Instead, the government relied on § 2703(b) and § 2703(d). The proper inquiry, therefore, is whether the government violated either of <em>those </em>provisions, and the preservation request is of no consequence to that inquiry.</p>
<p id="b316-9">Warshak’s next argument is that the government violated § 2703(d) by failing to provide any particularized factual basis <page-number citation-index="1" label="291">*291</page-number>when seeking an order for disclosure. Under § 2703(d), such an order “shall issue only if the governmental entity offers specific and articulable facts showing that there are reasonable grounds to believe that the contents of a wire or electronic communication ... are relevant and material to an ongoing criminal investigation.”</p>
<p id="b317-5">To the extent that he is arguing that the government’s application was insufficient, Warshak is wrong. The government’s application indicated that it was “investigating a complex, large-scale mail and wire fraud operation based in Cincinnati, Ohio.” The application also indicated that “interviews of current and former employees of the target company suggest that electronic mail is a vital communication tool that has been used to perpetuate the fraudulent conduct.” Additionally, the application observed that “various sources [have verified] that NuVox provides electronic communications services to certain individual(s) [under] investigation.” In light of these statements, it is clear that the application was, in fact, supported by specific and articulable facts, especially given the diminished standard that applies to § 2703(d) applications. <em>See United States v. Perrine, </em><span class="citation" data-id="170424"><a href="/opinion/170424/united-states-v-perrine/#1202" aria-description="Citation for case: United States v. Perrine">518 F.3d 1196, 1202</a></span> (10th Cir.2008) (noting that “the ‘specific and articulable facts’ standard derives from the Supreme Court’s decision in <em>Terry </em>”); <em>Warshak I, </em>490 F.3d at 463 (“The parties agree that the standard of proof for a court order — ‘specific and articulable facts showing that there are reasonable grounds to believe that the contents ... or records ... are relevant and material to an ongoing criminal investigation’ — falls short of probable cause.”).</p>
<p id="b317-6">Finally, Warshak argues that a finding of good-faith reliance is improper because the government presented the magistrate with an erroneous definition of the term “electronic storage.” As noted above, if an email is in electronic storage for less than 180 days, the government may not compel its disclosure without a warrant. <span class="citation no-link">18 U.S.C. § 2703</span>(a). In applying for the subpoena and the order that eventually resulted in the disclosure of Warshak’s NuVox emails, the government suggested to the magistrate that an email is not in electronic storage if it has already been “accessed, viewed, or downloaded.” Warshak argues that this definition of electronic storage does not comport with the Ninth Circuit’s decision in <em>Theofel v. Farey-Jones, </em><span class="citation" data-id="8408646"><a href="/opinion/8438109/theofel-v-farey-jones/#1071" aria-description="Citation for case: Theofel v. Farey-Jones">359 F.3d 1066, 1071</a></span> (9th Cir.2004), which held that “prior access is irrelevant to whether the [emails] at issue were in electronic storage.” Warshak further argues that, because the government failed to mention the Ninth Circuit’s definition, it “usurped the court’s function to determine whether an email ... [is] in ‘electronic storage[.]’ ” Appellant’s Br. at 38.</p>
<p id="b317-8">As an initial matter, it is manifest that the decisions of the Ninth Circuit are not binding on courts in this circuit. It therefore cannot be said that the government somehow violated § 2703 by failing to cite an out-of-circuit decision that it thought to be wrongly decided. Incidentally, the government is not alone in thinking that the Ninth Circuit’s definition of electronic storage is incorrect. One commentator has noted that <em>“Theofel </em>is quite implausible and hard to square with the statutory test.” Kerr, <em>A User’s Guide to the Stored Communications Act, </em>72 Geo. Wash. L.Rev. at 1217; <em>see also United States v. Weaver, </em><span class="citation" data-id="1758661"><a href="/opinion/1758661/united-states-v-weaver/#773" aria-description="Citation for case: United States v. Weaver">636 F.Supp.2d 769, 773</a></span> (C.D.Ill.2009) (“Previously opened emails stored by Microsoft for Hotmail users are not in electronic storage, and the Government can obtain copies of such emails using a trial subpoena.”).</p>
<p id="b317-9">Furthermore, it does a disservice to the magistrate judge to suggest that the government usurped the role of the court. <page-number citation-index="1" label="292">*292</page-number>The government’s application did include a proposed definition of the term “electronic storage.” That does not mean, however, that the magistrate judge unhesitatingly received that definition, and, as the government notes, the magistrate “presumably [had] the opportunity to consider and review relevant precedent.” Appellee’s Br. at 117.</p>
<p id="b318-4">Consequently, we find that, although the government violated the Fourth Amendment, the exclusionary rule does not apply, as the government relied in good faith on § 2703(b) and § 2703(d) to access the contents of Warshak’s emails.<footnotemark>22</footnotemark></p>
<p id="b318-5">B. The Kastigar-Like Hearing</p>
<p id="b318-6">1. <em>Background</em></p>
<p id="b318-7">During the government’s investigation of Berkeley, case agents came into possession of myriad documents that were ostensibly subject to the attorney-client privilege. Many of the documents were obtained during a March 16, 2005 search of Berkeley’s headquarters, in which agents copied the contents of over 90 computers. Other documents were procured earlier through the subpoena and court order issued to NuVox, which granted investigators access to the contents of Warshak’s email accounts. In all, case agents had access to approximately “60,000 email communications from or to attorneys representing Berkeley and Warshak, communications facially and presumptively protected by the attorney-client privilege.” Appellant’s Br. at 41.</p>
<p id="b318-9">On July 5, 2007, Warshak filed a “motion to bar the government from using the evidence obtained in violation of the defendants’ attorney-client and work product privileges and to dismiss the indictment since privileged material was used to secure it.” <em>United States v. Warshak, </em>No. 1:06-CR-00111, <span class="citation no-link">2007 WL 3306603</span>, at *1 (S.D.Ohio Nov.5, 2007). In the motion, the defendants requested that the district court hold a hearing “in the framework of <em>Kastigar v. United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">406 U.S. 441</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">32 L.Ed.2d 212</a></span> (1972), at which the government would bear the burden of establishing that its case was untainted by attorney-client and work product privileged materials.” <em>Warshak, </em><span class="citation no-link">2007 WL 3306603</span>, at *1. To an extent, the district court granted the motion, setting a <em>“Kasti</em>par-like” hearing with the “narrow purpose of eliciting the sworn testimony of government agents as to their handling of evidence.” <em><span class="citation no-link">Ibid.</span> </em>In ordering the hearing, the district court “found that [the] [defendants had raised enough of a question about the amount of time U.S. Postal Inspector Alejandro Almaguer (‘Almaguer’) possessed privileged data, as well as the government’s methodology in screening data for privileged information, to merit a response.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b318-10">The hearing was held on September 27 and 28, 2007. During the hearing, “the government proffered evidence and the testimony of Almaguer, the [defendants were afforded [an] opportunity to cross-examine Almaguer and examine other agents on direct, and the parties argued their respective positions concerning the <page-number citation-index="1" label="293">*293</page-number>propriety of the government action in this case.” <em><span class="citation no-link">Ibid.</span> </em>In addition, the defendants called Peter Horstmann, an expert witness “who used software to analyze the electronic documents the government produced to [the] [defendants.” <em><span class="citation no-link">Ibid.</span></em></p>
<p id="b319-5">After the hearing, the district court held that the government had satisfied its burden, stating as follows:</p>
<blockquote id="b319-6">The [c]ourt’s original concerns that triggered the grant of the <em>“Kastigar-kke” </em>evidentiary hearing were rooted in the amount of time that Almaguer allegedly had access to privileged materials, and in the fact the government had proffered no sworn statements backing its contention that it did not use privileged materials to obtain witness proffers. The government has completely allayed the [c]ourt’s concerns. The United States has met its burden to demonstrate its agents have acted properly and that its case is untainted by privileged information.</blockquote>
<p id="b319-7"><span class="citation no-link"><em>Id. </em>at *8</span>.</p>
<p id="b319-8">2. <em>The Adequacy of the Government’s Presentation</em></p>
<p id="b319-9">Warshak argues that the <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span></em>like hearing was inadequate. More precisely, he argues that the district court failed to “hold[] the government to the burden prescribed by <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>and subsequent cases applying it.” Appellant’s Br. at 48. He complains that the district court “simply accepted the government’s blanket denials that it used privileged materials in preparing its case against defendants, and shifted the burden to [him] to show that privileged materials contributed to the return of the indictment.” <em>Ibid, </em>(internal citations omitted). In short, he argues that the district court improperly loosened the stringent demands of <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span>.</em></p>
<p id="b319-10">In <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span>, </em>the Supreme Court held that when a witness is compelled to give incriminating testimony under a grant of statutory immunity and is thereafter prosecuted for any matter related to the compelled testimony, the government must shoulder the “heavy burden of proving that all of the evidence it proposes to use was derived from legitimate independent sources.” <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#461" aria-description="Citation for case: Kastigar v. United States">406 U.S. at 461-62</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>; <em>see also United States v. Turner, </em><span class="citation" data-id="563258"><a href="/opinion/563258/united-states-v-diane-turner-90-1546-edwin-leon-turner-90-1547/#224" aria-description="Citation for case: United States v. Diane Turner (90-1546), Edwin Leon...">936 F.2d 221, 224</a></span> (6th Cir.1991). “This burden of proof ... is not limited to a negation of taint; rather, it imposes on the prosecution the affirmative duty to prove that the evidence it proposes to use is derived from a legitimate source wholly independent of the compelled testimony.” <em>Kastigar, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#460" aria-description="Citation for case: Kastigar v. United States">406 U.S. at 460</a></span>, <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">92 S.Ct. 1653</a></span>.</p>
<p id="b319-12">While <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>is clearly concerned with the use of testimony obtained despite an assertion of the Fifth Amendment privilege against self-incrimination, this court has suggested that <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>concerns may arise in the context of other privileges, such as the privilege accorded to attorney-client communications. Specifically, this court has hinted, in dicta, that “the leaking of privileged materials to investigators would raise the spectre of Kastigar-like evidentiary hearings.” <em>In re Grand Jury Subpoenas, </em><span class="citation" data-id="794974"><a href="/opinion/794974/in-re-grand-jury-subpoenas-04-124-03-04-124-05/#517" aria-description="Citation for case: In Re Grand Jury Subpoenas 04-124-03 &amp; 04-124-05">454 F.3d 511, 517</a></span> (6th Cir.2006). However, no other appellate court appears to have joined us in suggesting that <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>is implicated whenever investigators come into possession of materials subject to the attorney-client privilege.</p>
<p id="b319-13">One circuit, the Fourth, has engaged in a fairly lengthy analysis of Kastigar’s applicability in the arena of non-constitutional privileges. In <em>United States v. Squillacote, </em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">221 F.3d 542</a></span> (4th Cir.2000), the Fourth Circuit was faced with a scenario in which government investigators had legally conducted electronic surveillance on several defendants pursuant to the Foreign <page-number citation-index="1" label="294">*294</page-number>Intelligence Surveillance Act.<footnotemark>23</footnotemark> During the surveillance, the agents heard and recorded a number of conversations between one of the defendants and her psychotherapists. Subsequently, the defendants “moved to suppress any evidence derived from the privileged communications,” arguing that “they were entitled to a hearing to vindicate the principles set forth by the Supreme Court in <em>[Kastigar </em>].” <span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/#558" aria-description="Citation for case: United States v. Squillacote"><em>Id. </em>at 558</a></span>. Ultimately, the court determined that <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>was “simply ... not applicable.” <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span></em></p>
<p id="b320-4">In so holding, the <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Squillacote</a></span> </em>court began by conceding that the conversations at issue, which the government had obtained during surveillance, were privileged. According to the court, “[t]he question, then, [was] whether the mere existence of this privileged information br[ought] to bear the full weight of <em>Kastigar.” Id. </em>at 559. The court held that it did not, finding that “a <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>analysis is not triggered by the existence of evidence protected by a privilege, but instead by the government’s <em>effort to compel </em>a witness to testify over the witness’s claim of privilege.” <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span> </em>(emphasis added). However, the court also opined “that <em>Kastigar-\Ske </em>protections may be required in cases involving testimony compelled over the assertion of a non-constitutional privilege.” <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Ibid.</a></span> </em>Nonetheless, in concluding its analysis, the court reiterated that “because the government’s right to compel testimony in the face of a claim of privilege is the issue at the heart of <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span>, </em>its protections do not apply in cases where there is privileged evidence, but no compelled testimony.” <span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#560" aria-description="Citation for case: Kastigar v. United States"><em>Id. </em>at 560</a></span>. We agree, and hold that, absent compelled testimony, the full protections of <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>are inapplicable.</p>
<p id="b320-6">As further justification for its holding in <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Squillacote</a></span>, </em>the Fourth Circuit observed that “suppression of any evidence derived from the privileged conversations would be [im]proper in this case, given that the privilege is a testimonial or evidentiary one, and not constitutionally-based.” <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Ibid.</a></span> </em>In making this assertion, the court observed that, as of the year 2000, no court had applied the fruit-of-the-poisonous-tree doctrine to derivative evidence obtained as a result of improper access to materials covered by a non-constitutional privilege. <em>Ibid, </em>(quoting <em>United States v. Marashi, </em><span class="citation" data-id="547559"><a href="/opinion/547559/united-states-v-s-mohammad-marashi/" aria-description="Citation for case: United States v. S. Mohammad Marashi">913 F.2d 724</a></span>, 731 n. 11 (9th Cir.1990)); <em>see also Nickel v. Hannigan, </em><span class="citation" data-id="727279"><a href="/opinion/727279/willie-w-nickel-v-robert-d-hannigan-warden-hutchinson-correctional/#409" aria-description="Citation for case: Willie W. Nickel v. Robert D. Hannigan, Warden,...">97 F.3d 403, 409</a></span> (10th Cir.1996) (“[W]e decline to apply the ‘fruit of the poisonous tree’ doctrine to the possible breach of attorney-client privilege in this case.”). We have found no subsequent authority indicating that such derivative evidence is subject to suppression, and we agree that it is unwise to extend the fruit-of-the-poisonous-tree doctrine beyond the context of constitutional violations. <em>See Trammel v. United States, </em><span class="citation" data-id="9427810"><a href="/opinion/110212/trammel-v-united-states/#51" aria-description="Citation for case: Trammel v. United States">445 U.S. 40, 51</a></span>, <span class="citation" data-id="9427810"><a href="/opinion/110212/trammel-v-united-states/" aria-description="Citation for case: Trammel v. United States">100 S.Ct. 906</a></span>, <span class="citation" data-id="9427810"><a href="/opinion/110212/trammel-v-united-states/" aria-description="Citation for case: Trammel v. United States">63 L.Ed.2d 186</a></span> (1980) (indicating that testimonial privileges must be balanced against “the need for probative evidence in the administration of criminal justice”).</p>
<p id="b320-7">In the present case, the privileged materials were not obtained from Warshak as a result of compelled testimony. Instead, they were garnered pursuant to a subpoena, a court order, and a search warrant, much like the psychotherapist-patient conversations at issue in <em><span class="citation" data-id="2967273"><a href="/opinion/2967273/united-states-v-squillacote/" aria-description="Citation for case: United States v. Squillacote">Squillacote</a></span>. </em>Thus, because the documents were not the product of compelled testimony, a full <em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/" aria-description="Citation for case: Kastigar v. United States">Kastigar</a></span> </em>hearing was not required. Moreover, there is no indication that the government made any direct use of the privileged com<page-number citation-index="1" label="295">*295</page-number>munications, either at trial or before the grand jury. Consequently, given the fact that evidence derived from a violation of the attorney-client privilege is not fruit of the poisonous tree, Warshak’s argument withers.</p>
<p id="b321-5">C. Volume &amp; Format of Discovery</p>
<p id="b321-6">The volume of discovery in the present case was prodigious. Indeed, the government turned over millions of pages of discovery, but that discovery appears to have come from relatively few sources. Most of the discovery came from Berkeley itself, when, in March 2005, inspectors executed a search warrant and “imaged” (i.e., copied) the electronic contents of the company’s computers and servers. After the search, the computers and servers remained on Berkeley’s premises, except for several laptops, which were taken offsite and returned two days later. All told, the electronic evidence originating at Berkeley filled three “tera-drives” and numbered 17 million pages. In addition to the electronic evidence, agents seized approximately 506,000 pages of hard-copy documents, all of which the defendants were eventually permitted to copy. On top of the evidence obtained at Berkeley, discovery included 275 discs of material gathered by the grand jury and 13 discs of potential trial exhibits compiled by the government.</p>
<p id="b321-7">The defendants make three arguments with respect to the immense volume of discovery in this case. First, they argue that the district court abused its discretion and violated their right to a fair trial by allowing the government to turn over stupendous quantities of evidence in a disorganized and unsearchable format. Next, they argue that the government was improperly permitted to “abdicate” its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligations by producing gargantuan “haystacks” of discovery that swallowed any “needles” of exculpatory information. Appellant’s Br. at 52. Finally, the defendants argue that the district court erroneously denied a 90-day continuance, which was requested to enable the defendants to continue sifting through the mountains of discovery furnished by the government. Ultimately, none of these arguments is persuasive.<footnotemark>24</footnotemark></p>
<p id="b321-10">1. <em>The Manner in Which the Government Produced Discovery</em></p>
<p id="ArIc">The defendants’ first argument is that the district court erroneously permitted the government to produce titanic amounts of electronic discovery in formats that were simultaneously disorganized and unsearchable. Specifically, the defendants assert that the electronic images of the Berkeley computers and the discs of potential trial exhibits were difficult to search. The defendants further contend that the government’s failure to supplement the discovery materials with indices was prejudicial to the preparation of an adequate defense.<footnotemark>25</footnotemark> In making this argument, the defendants lean heavily on Federal Rule of <em>Civil </em>Procedure 34(b)(2)(E)(i), which requires a party to “produce [discovery materials] as they are kept in the usual course of business or [to] organize and label them to correspond to the categories in the request.” The defendants acknowledge that there is no corresponding provision in Federal Rule of <em>Criminal </em>Proce<page-number citation-index="1" label="296">*296</page-number>dure 16, which governs criminal discovery, but they argue that due process mandates enforcement of the civil rule in the criminal context.</p>
<p id="b322-4">A district court’s decision on a discovery matter is reviewed for abuse of discretion. <em>United States v. Gray, </em><span class="citation" data-id="1302101"><a href="/opinion/1302101/united-states-v-gray/#529" aria-description="Citation for case: United States v. Gray">521 F.3d 514, 529</a></span> (6th Cir.2008) (citing <em>United States v. $174,206.00 in U.S. Currency, </em><span class="citation" data-id="780971"><a href="/opinion/780971/united-states-v-17420600-in-us-currency-thomas-richard-dacia-love/#663" aria-description="Citation for case: United States v. $174,206.00 in U.S. Currency, Thomas...">320 F.3d 658, 663</a></span> (6th Cir.2003)); <em>see United States v. Maples, </em><span class="citation" data-id="9488302"><a href="/opinion/699570/united-states-v-roger-d-maples/#246" aria-description="Citation for case: United States v. Roger D. Maples">60 F.3d 244, 246</a></span> (6th Cir.1995) (“It is well settled that a district court has considerable discretion under Rule 16....”).</p>
<p id="b322-5">As an initial matter, it must be noted that the defendants cite scant authority suggesting that a district court must order the government to produce electronic discovery in a particular fashion.<footnotemark>26</footnotemark> Furthermore, it bears noting that Federal Rule of Criminal Procedure 16, which governs discovery in criminal cases, is entirely silent on the issue of the form that discovery must take; it contains no indication that documents must be organized or indexed. Thus, if we are to find that the district court abused its discretion, we must do so despite a pronounced dearth of precedent suggesting that the district court was wrong.</p>
<p id="b322-6">There are a number of factors that counsel against such a finding. First, the overwhelming majority of the discovery at issue was taken directly from Berkeley’s computers, which means the defendants had ready access to that information. It also means that the defendants had access to the documents “as they [were] kept in the usual course of business.” Fed.R.Civ.P. 34(b)(2)(E)(i). Thus, any difficulty that the defendants had in accessing the copies is arguably immaterial.<footnotemark>27</footnotemark></p>
<p id="b322-9">Furthermore, there is reason to believe that the defendants were experiencing little difficulty in accessing the contents of the electronic discovery. Though the defendants claim that they were provided with data that had been rendered in unsearchable formats, they were citing discovery material to the district court in their motions, leading the district court to observe that the “[defendants’ motion[s] demonstrate^] [that] they [were] capably navigating discovery.” Additionally, at the Kastigar-like hearing held before the district court, an expert witness who testified for the defense indicated that, with the use of certain software, he could perform “very quick and thorough” searches of the electronic discovery. Consequently, it does not appear that the discovery materials were nearly as unsearchable as the defense purports.</p>
<p id="b322-10">Lastly, it should be observed that the government did provide the defense with something of a guide to the electronic discovery. In response to the defense’s discovery request, the government furnished the defendants with “a detailed room-by-room inventory of all items seized from the company, including a listing of the various <page-number citation-index="1" label="297">*297</page-number>computers that were imaged.” Appellee’s Br. at 127. That listing surely offered the defendants some aid in identifying and marshaling the documents relevant to the litigation. Accordingly, we decline to hold that the district court abused its discretion in failing to order the government to produce discovery in a different form.</p>
<p id="b323-5">2. <em>The Abdication of </em>Brady</p>
<p id="b323-6">The defendants next argue that the government shrugged off its obligations under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>by simply handing over millions of pages of evidence and forcing the defense to find any exculpatory information contained therein. In essence, the defendants contend that the government was obliged to sift fastidiously through the evidence— the vast majority of which came from Berkeley itself — in an attempt to locate anything favorable to the defense. This argument comes up empty.</p>
<p id="b323-7">In <em>United States v. Skilling, </em><span class="citation" data-id="64496"><a href="/opinion/64496/united-states-v-skilling/" aria-description="Citation for case: United States v. Skilling">554 F.3d 529</a></span> (5th Cir.2009), <em>vacated in part on other grounds, </em>— U.S. -, <span class="citation multiple-matches"><a href="/c/S.Ct./130/2896/">130 S.Ct. 2896</a></span>, <span class="citation multiple-matches"><a href="/c/L.Ed.2d/177/619/">177 L.Ed.2d 619</a></span> (2010), the Fifth Circuit confronted and rejected a nearly identical argument. There, disgraced Enron CEO Jeffrey K. Skilling advanced the following contentions:</p>
<blockquote id="b323-9">Skilling ... asserts that the government’s use of an open file failed to satisfy its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligation to disclose material evidence. Skilling contends that the government’s open file, which consisted of several hundred million pages of documents, “resulted in the effective concealment of a huge quantity of exculpatory evidence.” As the government never directed Skilling to a single <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>document contained in the open file, Skilling argues that the government suppressed evidence in violation of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</em></blockquote>
<p id="b323-12"><em>Id. </em>at 576.</p>
<p id="b323-13">, In dismissing Skilling’s argument, the Fifth Circuit noted that, “[a]s a general rule, the government is under no duty to direct a defendant to exculpatory evidence within a larger mass of disclosed evidence.” <em>Ibid, </em>(citing <em>United States v. Mulderig, </em><span class="citation" data-id="12936"><a href="/opinion/12936/united-states-v-mulderig/#541" aria-description="Citation for case: United States v. Mulderig">120 F.3d 534, 541</a></span> (5th Cir.1997)). However, the <em>Skilling </em>court added a caveat:</p>
<blockquote id="b323-14">We do not hold that the use of a voluminous open file can never violate <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>. </em>For instance, evidence that the government “padded” an open file with pointless or superfluous information to frustrate a defendant’s review of the file might raise serious <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>issues. Creating a voluminous file that is unduly onerous to access might raise similar concerns. And it should go without saying that the government may not hide <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material of which it is actually aware in a huge open file in the hope that the defendant will never find it. These scenarios would indicate that the government was acting in bad faith in performing its obligations under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</em></blockquote>
<p id="Acl"><em>Id. </em>at 577.</p>
<p id="b323-15">Here, the government did not engage in any conduct indicating that it performed its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>obligations in bad faith. First, there is no proof that the government larded its production with entirely irrelevant documents.<footnotemark>28</footnotemark> Furthermore, it cannot be said that the government made access to the documents <em>unduly </em>onerous. While ac<page-number citation-index="1" label="298">*298</page-number>cess to the documents may have been somewhat hampered due to the format in which they were transferred, the district court noted that the defendants’ motion practice “demonstrate[d] they [were] capably navigating the discovery, which primarily all came from [the] [defendants in the first place.”<footnotemark>29</footnotemark> Finally, there is no indication that the government deliberately concealed any exculpatory evidence in the information it turned over to the defense.<footnotemark>30</footnotemark> Consequently, the government has not “abdicated” its duties under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</em></p>
<p id="b324-4">3. <em>The Denial of a Continuance</em></p>
<p id="ACG">On December 28, 2007, the defendants requested a 90-day continuance, which would have pushed the commencement of the trial from January 8, 2008 to April 8, 2008. In making the request, the defendants contended that they had been afforded insufficient opportunity to review the evidence, stating: “[i]t is as if the government has pointed the defendants to the Earth’s oceans, saying ‘there is your discovery.’ ” The district court declined to grant the request, noting that “[c]ounsel for [the] [defendants outnumber counsel for the government, and have all been working on this case for a substantial amount of time.”<footnotemark>31</footnotemark> The defendants now argue that the district court’s denial of their request for a continuance was error.</p>
<p id="b324-7">The district court’s denial of a motion for a continuance is reviewed for abuse of discretion. <em>United States v. Crossley, </em><span class="citation" data-id="770181"><a href="/opinion/770181/united-states-v-rebecca-k-crossley-99-4076-starla-grubich/#854" aria-description="Citation for case: United States v. Rebecca K. Crossley (99-4076) Starla...">224 F.3d 847, 854</a></span> (6th Cir.2000). “Denial amounts to a constitutional violation only if there is an unreasoning and arbitrary ‘insistence upon expeditiousness in the face of a justifiable request for delay.’ To demonstrate reversible error, the defendant must show that the denial resulted in actual prejudice to his defense.” <em>United States v. Gallo, </em><span class="citation" data-id="453322"><a href="/opinion/453322/united-states-v-joseph-c-gallo-frederick-graewe-hartmut-graewe-kevin/#1523" aria-description="Citation for case: United States v. Joseph C. Gallo Frederick Graewe Hartmut...">763 F.2d 1504, 1523</a></span> (6th Cir.1985) (quoting <em>United States v. Mitchell, </em><span class="citation" data-id="442038"><a href="/opinion/442038/united-states-v-walter-l-mitchell-jr/#704" aria-description="Citation for case: United States v. Walter L. Mitchell, Jr.">744 F.2d 701, 704</a></span> (9th Cir.1984)). “The defendant demonstrates ‘actual prejudice’ by showing that a continuance would have made relevant witnesses available or added something to the defense.” <em>United States v. King, </em><span class="citation" data-id="9490697"><a href="/opinion/747179/united-states-of-america-plaintiff-appellee-v-kenneth-king-kewin-king/#487" aria-description="Citation for case: United States of America, Plaintiff-Appellee v. Kenneth...">127 F.3d 483, 487</a></span> (6th Cir.1997); <em>see also United States v. Faulkner, </em><span class="citation" data-id="337637"><a href="/opinion/337637/united-states-v-donald-d-faulkner-united-states-of-america-v-william-e/#729" aria-description="Citation for case: United States v. Donald D. Faulkner, United States of...">538 F.2d 724, 729</a></span> (6th Cir.1976) (“No absolute rule can be articulated as to the minimum amount of time required for an adequate preparation for trial of a criminal case.”).</p>
<p id="b324-8">The defendants argue that they were prejudiced in two ways. First, they argue that “their counsel could not satisfy their constitutional obligation to review all the evidence in the government’s possession, custody, or control.”<footnotemark>32</footnotemark> Appellant’s Br. at 60. In making this argument, they allege that “the entirety of the government’s <page-number citation-index="1" label="299">*299</page-number>360,000 pages of trial exhibits ... were largely disclosed on November 29, 2007, only six weeks before trial.” <em>Id. </em>at 59. Second, the defendants argue that “[t]he defense simply did not have sufficient time to locate and then utilize material and exculpatory evidence that was hidden within the millions of pages of discovery.” <em>Id. </em>at 60.</p>
<p id="b325-5">These arguments lead nowhere. With respect to the first, it must be noted that more than a year elapsed between the time the indictment was handed down and the time the trial began, affording the defendants ample opportunity to construct a defense.<footnotemark>33</footnotemark> Additionally, the discovery time line does not indicate that the defendants were shortchanged with respect to preparation time. The bulk of the documents in question were in the company’s possession as early as April 2005.<footnotemark>34</footnotemark> Furthermore, the entirety of the discovery material in the case was in the defendants’ hands by June 2007, more than six months in advance of the trial. While the government did not provide the defense with thirteen discs of potential trial exhibits until November 29, 2007 — approximately six weeks before trial was to begin — those exhibits were ostensibly culled from the discovery material that the government had already provided.<footnotemark>35</footnotemark> It is true that this case involved millions of pages of documents, but there is no dispute that the defendants were given months to comb through the bulk of them. As a result, it cannot be said that the district court’s unwillingness to postpone the trial was the product of an undue insistence on haste.</p>
<p id="b325-10">The defendants’ second argument — that they were not given enough time to mine exculpatory evidence from the mountains of discovery dumped at their feet — similarly fails. As an initial matter, it should be noted that this argument assumes that exculpatory evidence exists. In the absence of such evidence, the lack of time to look for it would be harmless. In other words, it would not be prejudicial if the defendants were denied the chance to excavate in a mine that contained no ore. On that score, the most the defendants can say is tha

[...TRUNCATED 194596 of 314596 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
