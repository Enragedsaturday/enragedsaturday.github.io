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

## GROUP: _overhaul2/lake/cases/United States v. Ventresca.json  (`lake-record`, 6 assertions)

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
{"assertion_id": "de4a12fd3ef06ad3", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Ventresca"}, "payload": {"all": [{"cite": "380 U.S. 102", "page": "102", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "380"}, {"cite": "85 S. Ct. 741", "page": "741", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "85"}, {"cite": "13 L. Ed. 2d 684", "page": "684", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "13"}, {"cite": "1965 U.S. LEXIS 2438", "page": "2438", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1965"}, {"cite": "16 A.F.T.R.2d (RIA) 5787", "page": "5787", "reporter": "A.F.T.R.2d (RIA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "16"}], "display": "380 U.S. 102", "official": {"cite": "380 U.S. 102", "page": "102", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "380"}, "official_selection_present": true, "record_id": "United States v. Ventresca"}}
{"assertion_id": "11fe534661b13333", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-109a", "record_id": "United States v. Ventresca"}, "payload": {"fragment": "#:~:text=purely%20conclusory%2C", "page": null, "pin_id": "pin-109a", "pinpoint_status": "star-verified", "quote": "purely conclusory,", "quote_fidelity": "matched", "record_id": "United States v. Ventresca", "star_marker": "108"}}
{"assertion_id": "479ba5f7d20e5437", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-106", "record_id": "United States v. Ventresca"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-106", "pinpoint_status": "slip-only", "quote": "underscore[] the preference accorded police action taken under a warrant.", "quote_fidelity": "mismatch", "record_id": "United States v. Ventresca", "star_marker": null}}
{"assertion_id": "c544bcdf805ed69f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-108", "record_id": "United States v. Ventresca"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-108", "pinpoint_status": "slip-only", "quote": "--- # United States v. Ventresca *380 U.S. 102 (1965)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal investigators suspected Ventresca of operating an illegal still. An investigator's affidavit, drawing on his own observations and the corroborating reports of fellow investigators, detailed numerous facts — the odor of fermenting mash, deliveries of sugar and metal cans, and related activity at the premises. A United States Commissioner issued a search warrant, and the ensuing search uncovered an illegal distillery. The Court of Appeals held the affidavit insufficient because it did not clearly separate which facts were hearsay and which were within the affiant's personal knowledge. ## Issue Did a detailed search-warrant affidavit — combining the affiant's own observations with corroborating reports of fellow officers — establish probable cause when read in a commonsense manner? ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "United States v. Ventresca", "star_marker": null}}
{"assertion_id": "cc52a61b97e75dcb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-109b", "record_id": "United States v. Ventresca"}, "payload": {"fragment": "#:~:text=the%20resolution%20of%20doubtful%20or", "page": null, "pin_id": "pin-109b", "pinpoint_status": "star-verified", "quote": "the resolution of doubtful or marginal cases in this area should be largely determined by the preference to be accorded to warrants.", "quote_fidelity": "matched", "record_id": "United States v. Ventresca", "star_marker": "109"}}
{"assertion_id": "46034e99d3fd1ea0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Ventresca"}, "payload": {"as_of_content": "1965-03-01", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Ventresca", "scope_note": "Controlling and foundational: warrant affidavits are read in a commonsense, not hypertechnical, manner and doubtful cases are resolved in favor of the warrant — a cornerstone of the deferential review reaffirmed in Illinois v. Gates and the good-faith rule of United States v. Leon.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Verdugo-Urquidez.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Verdugo-Urquidez
type: case
citation: "494 U.S. 259 (1990)"
parallel_cite: "110 S. Ct. 1056; 108 L. Ed. 2d 222"
neutral_cite: "1990 U.S. LEXIS 1175; 1990 WL 16772"
court: U.S.
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-02-28
docket: 88-1353
authority_weight: "Binding — SCOTUS"
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
  opinion_url: "https://www.courtlistener.com/opinion/112382/united-states-v-verdugo-urquidez/"
  cluster_id: 112382
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Verdugo-Urquidez
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Private and Foreign Searches]]"
    role: "Key — Anchor (foreign search)"
related:
  - "[[Fourth Amendment Framework]]"
  - "[[Fourth Amendment Recalibration]]"
tags:
  - case
  - fourth-amendment
  - the-people
  - extraterritoriality
  - nonresident-alien
holding: "The Fourth Amendment does not apply to the search and seizure by United States agents of property owned by a nonresident alien and located in a foreign country, because 'the people' the Amendment protects are those who are part of the national community or have otherwise developed a sufficient voluntary connection with the United States."
---

# United States v. Verdugo-Urquidez

*494 U.S. 259 (1990)* (No. 88-1353) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 112382 → lead opinion 112382; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
René Martín Verdugo-Urquidez, a citizen and resident of Mexico, was apprehended by Mexican authorities and transferred to United States custody on drug-trafficking charges. Working with Mexican police, DEA agents then searched his residences in Mexicali and San Felipe, Mexico, without a United States warrant, and seized documents. Verdugo-Urquidez moved to suppress the seized evidence, arguing that the warrantless searches of his Mexican property violated the Fourth Amendment.

## Issue
Whether the Fourth Amendment applies to the search and seizure by United States agents of property that is owned by a nonresident alien and located in a foreign country.

## Rule
The Court construed the Amendment's reference to "the people." It held: "'the people' protected by the Fourth Amendment, and by the First and Second Amendments, and to whom rights and powers are reserved in the Ninth and Tenth Amendments, refers to a class of persons who are part of a national community or who have otherwise developed sufficient connection with this country to be considered part of that community." — 494 U.S. at 265. ^pin-265

A nonresident alien whose property abroad is searched by U.S. agents is not among "the people," so the Fourth Amendment does not reach the search.

## Application
Verdugo-Urquidez was a citizen and resident of Mexico with no voluntary attachment to the United States, and the property searched was located in Mexico. The Court grounded its reading in the Amendment's text and history and in the impracticability of imposing its warrant and reasonableness requirements on U.S. operations abroad. His involuntary presence in the United States for prosecution did not supply the substantial connection the text requires; the Fourth Amendment therefore did not apply to the foreign searches.

## Conclusion
The judgment of the Ninth Circuit was **reversed**. Rehnquist, C.J., delivered the opinion of the Court; Kennedy, J., filed a [[Common Legal Terms#concurring-opinion|concurring opinion]]; Stevens, J., concurred in the judgment; Brennan, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Marshall, J.; Blackmun, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Verdugo-Urquidez* fixes the personal scope of the Fourth Amendment — defining who counts as "the people" — and remains the framework anchor for questions about the Amendment's reach over nonresident aliens and conduct abroad.

## Appears on
- [[Private and Foreign Searches]] — *Key — Anchor (foreign search)*

## Sources
- [*United States v. Verdugo-Urquidez*, 494 U.S. 259 (1990)](https://www.courtlistener.com/opinion/112382/united-states-v-verdugo-urquidez/) — pinpoint: 265 (Opinion of the Court, "the people" holding; Rehnquist, C.J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "78a8ca28a7087c78", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Verdugo-Urquidez"}, "payload": {"all": [{"cite": "494 U.S. 259", "page": "259", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "494"}, {"cite": "110 S. Ct. 1056", "page": "1056", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "110"}, {"cite": "108 L. Ed. 2d 222", "page": "222", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "1990 U.S. LEXIS 1175", "page": "1175", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1990"}, {"cite": "1990 WL 16772", "page": "16772", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "1990"}], "display": "494 U.S. 259", "official": {"cite": "494 U.S. 259", "page": "259", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "494"}, "official_selection_present": true, "record_id": "United States v. Verdugo-Urquidez"}}
{"assertion_id": "7eaebb8b3c3a291c", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Verdugo-Urquidez"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Verdugo-Urquidez", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Verdugo-Urquidez

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Verdugo-Urquidez",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Verdugo-Urquidez",
    "case_name_short": "Verdugo-Urquidez",
    "case_name_full": "United States v. Verdugo-Urquidez",
    "input_case_name": "United States v. Verdugo-Urquidez",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-02-28",
    "year": 1990,
    "docket": "88-1353",
    "cluster_id": 112382,
    "lead_opinion_id": 9431925,
    "sibling_ids": [],
    "absolute_url": "/opinion/112382/united-states-v-verdugo-urquidez/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "494 U.S. 259",
      "volume": "494",
      "reporter": "U.S.",
      "page": "259",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 1056",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 222",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 1175",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1175",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 WL 16772",
        "volume": "1990",
        "reporter": "WL",
        "page": "16772",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "494 U.S. 259",
        "volume": "494",
        "reporter": "U.S.",
        "page": "259",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 1056",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "1056",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 L. Ed. 2d 222",
        "volume": "108",
        "reporter": "L. Ed. 2d",
        "page": "222",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 1175",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "1175",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 WL 16772",
        "volume": "1990",
        "reporter": "WL",
        "page": "16772",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "494 U.S. 259",
    "official_selection": {
      "court_class": "scotus",
      "selected": "494 U.S. 259",
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
    "date_created": "2026-07-07T01:40:48Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:41:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-verdugo-urquidez--112382",
      "to_record_id": "United States v. Verdugo-Urquidez",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Verdugo-Urquidez

```
<opinion type="majority">
<author id="b327-9">Chief Justice Rehnquist</author>
<p id="AQg">delivered the opinion of the Court.</p>
<p id="b327-10">The question presented by this case is whether the Fourth Amendment applies to the search and seizure by United States agents of property that is owned by a nonresident alien and located in a foreign country. We hold that it does not.</p>
<p id="b328-4"><page-number citation-index="1" label="262">*262</page-number>Respondent Rene Martin Verdugo-Urquidez is a citizen and resident of Mexico. He is believed by the United States Drug Enforcement Agency (DEA) to be one of the leaders of a large and violent organization in Mexico that smuggles narcotics into the United States. Based on a complaint charging respondent with various narcotics-related offenses, the Government obtained a warrant for his arrest on August 3, 1985. In January 1986, Mexican police officers, after discussions with United States marshals, apprehended Verdugo-Urquidez in Mexico and transported him to the United States Border Patrol station in Calexico, California. There, United States marshals arrested respondent and eventually moved him to a correctional center in San Diego, California, where he remains incarcerated pending trial.</p>
<p id="b328-5">Following respondent’s arrest, Terry Bowen, a DEA agent assigned to the Calexico DEA office, decided to arrange for searches of Verdugo-Urquidez’s Mexican residences located in Mexicali and San Felipe. Bowen believed that the searches would reveal evidence related to respondent’s alleged narcotics trafficking activities and his involvement in the kidnaping and torture-murder of DEA Special Agent Enrique Camarena Salazar (for which respondent subsequently has been convicted in a separate prosecution. See <em>United States </em>v. <em>Verdugo-Urquidez, </em>No. CR-87-422-ER (CD Cal., Nov. 22, 1988)). Bowen telephoned Walter White, the Assistant Special Agent in charge of the DEA office in Mexico City, and asked him to seek authorization for the search from the Director General of the Mexican Federal Judicial Police (MFJP). After several attempts to reach high ranking Mexican officials, White eventually contacted the Director General, who authorized the searches and promised the cooperation of Mexican authorities. Thereafter, DEA agents working in concert with officers of the MFJP searched respondent’s properties in Mexicali and San Felipe and seized certain documents. In particular, the search of the Mexicali residence uncovered a tally sheet, which the Government <page-number citation-index="1" label="263">*263</page-number>believes reflects the quantities of marijuana smuggled by Verdugo-Urquidez into the United States.</p>
<p id="b329-5">The District Court granted respondent’s motion to suppress evidence seized during the searches, concluding that the Fourth Amendment applied to the searches and that the DEA agents had failed to justify searching respondent’s premises without a warrant. A divided panel of the Court of Appeals for the Ninth Circuit affirmed. <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez">856 F. 2d 1214</a></span> (1988). It cited this Court’s decision in <em>Reid </em>v. <em>Covert, </em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">354 U. S. 1</a></span> (1957), which held that American citizens tried by United States military authorities in a foreign country were entitled to the protections of the Fifth and Sixth Amendments, and concluded that “[t]he Constitution imposes substantive constraints on the federal government, even when it operates abroad.” <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1218" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez">856 F. 2d, at 1218</a></span>. Relying on our decision in <em>INS </em>v. <em>Lopez-Mendoza, </em><span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">468 U. S. 1032</a></span> (1984), where a majority of Justices assumed that illegal aliens in the United States have Fourth Amendment rights, the Ninth Circuit majority found it “difficult to conclude that Verdugo-Urquidez lacks these same protections.” <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1223" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez">856 F. 2d, at 1223</a></span>. It also observed that persons in respondent’s position enjoy certain trial-related rights, and reasoned that “[i]t would be odd indeed to acknowledge that Verdugo-Urquidez is entitled to due process under the fifth amendment, and to a fair trial under the sixth amendment, . . . and deny him the protection from unreasonable searches and seizures afforded under the fourth amendment.” <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1224" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez"><em>Id., </em>at 1224</a></span>. Having concluded that the Fourth Amendment applied to the searches of respondent’s properties, the court went on to decide that the searches violated the Constitution because the DEA agents failed to procure a search warrant. Although recognizing that “an American search warrant would be of no legal validity in Mexico,” the majority deemed it sufficient that a warrant would have “substantial constitutional value in this country,” because it would reflect a magistrate’s determination <page-number citation-index="1" label="264">*264</page-number>that there existed probable cause to search and would define the scope of the search. <span class="citation" data-id="9478144"><a href="/opinion/511693/united-states-v-rene-martin-verdugo-urquidez/#1230" aria-description="Citation for case: United States v. Rene Martin Verdugo-Urquidez"><em>Id., </em>at 1230</a></span>.</p>
<p id="b330-5">The dissenting judge argued that this Court’s statement in <em>United States </em>v. <em>Curtiss-Wright Export Corp., </em><span class="citation" data-id="102726"><a href="/opinion/102726/united-states-v-curtiss-wright-export-corp/#318" aria-description="Citation for case: United States v. Curtiss-Wright Export Corp.">299 U. S. 304, 318</a></span> (1936), that “[n]either the Constitution nor the laws passed in pursuance of it have any force in foreign territory unless in respect of our own citizens,” foreclosed any claim by respondent to Fourth Amendment rights. More broadly, he viewed the Constitution as a “compact” among the people of the United States, and the protections of the Fourth Amendment were expressly limited to “the people.” We granted certiorari, 490 U. S; 1019 (1989).</p>
<p id="b330-6">Before analyzing the scope of the Fourth Amendment, we think it significant to note that it operates in a different manner than the Fifth Amendment, which is not at issue in this case. The privilege against self-incrimination guaranteed by the Fifth Amendment is a fundamental trial right of criminal defendants. See <em>Malloy </em>v. <em>Hogan, </em><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964). Although conduct by law enforcement officials prior to trial may ultimately impair that right, a constitutional violation occurs only at trial. <em>Kastigar </em>v. <em>United States, </em><span class="citation" data-id="9424889"><a href="/opinion/108541/kastigar-v-united-states/#453" aria-description="Citation for case: Kastigar v. United States">406 U. S. 441, 453</a></span> (1972). The Fourth Amendment functions differently. It prohibits “unreasonable searches and seizures” whether or not the evidence is sought to be used in a criminal trial, and a violation of the Amendment is “fully accomplished” at the time of an unreasonable governmental intrusion. <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 354</a></span> (1974); <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 906</a></span> (1984). For purposes of this case, therefore, if there were a constitutional violation, it occurred solely in Mexico. Whether evidence obtained from respondent’s Mexican residences should be excluded at trial in the United States is a remedial question separate from the existence <em>vel non </em>of the constitutional violation. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#354" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 354</a></span>; <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 906</a></span>.</p>
<p id="b330-7">The Fourth Amendment provides:</p>
<blockquote id="b331-4"><page-number citation-index="1" label="265">*265</page-number>“The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.”</blockquote>
<p id="b331-5">That text, by contrast with the Fifth and Sixth Amendments, extends its reach only to “the people.” Contrary to the suggestion of <em>amici curiae </em>that the Framers used this phrase “simply to avoid [an] awkward rhetorical redundancy,” Brief for American Civil Liberties Union et al. as <em>Amici Curiae </em>12, n. 4, “the people” seems to have been a term of art employed in select parts of the Constitution. The Preamble declares that the Constitution is ordained and established by “the People of the United States.” The Second Amendment protects “the right of the people to keep and bear Arms,” and the Ninth and Tenth Amendments provide that certain rights and powers are retained by and reserved to “the people.” See also U. S. Const., Arndt. 1 (“Congress shall make no law . . . abridging <em>... the right of the people </em>peaceably to assemble”) (emphasis added); Art. I, § 2, cl. 1 (“The House of Representatives shall be composed of Members chosen every second Year <em>by the People of the several States”) </em>(emphasis added). While this textual exegesis is by no means conclusive, it suggests that “the, people” protected by the Fourth Amendment, and by the First and Second Amendments, and to whom rights and powers are reserved in the Ninth and Tenth Amendments, refers to a class of persons who are part of a national community or who have otherwise developed sufficient connection with this country to be considered part of that community. See <em>United States ex rel. Turner </em>v. <em>Williams, </em><span class="citation" data-id="9417945"><a href="/opinion/96089/united-states-ex-rel-turner-v-williams/#292" aria-description="Citation for case: United States Ex Rel. Turner v. Williams">194 U. S. 279, 292</a></span> (1904) (Excludable alien is not entitled to First Amendment rights, because “[h]e does not become one of the people to whom these things are secured by our Constitution by an attempt to enter forbidden by law”). The language of these Amendments contrasts with the words <page-number citation-index="1" label="266">*266</page-number>“person” and “accused” used in the Fifth and Sixth Amendments regulating procedure in criminal cases.</p>
<p id="b332-5">What we know of the history of the drafting of the Fourth Amendment also suggests that its purpose was to restrict searches and seizures which might be conducted by the United States in domestic matters. The Framers originally decided not to include a provision like the Fourth Amendment, because they believed the National Government lacked power to conduct searches and seizures. See C. Warren, The Making of the Constitution 508-509 (1928); The Federalist No. 84, p. 513 (C. Rossiter ed. 1961) (A. Hamilton); 1 Annals of Cong. 437 (1789) (statement of J. Madison). Many disputed the original view that the Federal Government possessed only narrow delegated powers over domestic affairs, however, and ultimately felt an Amendment prohibiting unreasonable searches and seizures was necessary. Madison, for example, argued that “there is a clause granting to Congress the power to make all laws which shall be necessary and proper for carrying into execution all of the powers vested in the Government of the United States,” and that general warrants might be considered “necessary” for the purpose of collecting revenue. <em>Id., </em>at 438. The driving force behind the adoption of the Amendment, as suggested by Madison’s advocacy, was widespread hostility among the former colonists to the issuance of writs of assistance empowering revenue officers to search suspected places for smuggled goods, and general search warrants permitting the search of private houses, often to uncover papers that might be used to' convict persons of libel. See <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#625" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 625-626</a></span> (1886). The available historical data show, therefore, that the purpose of the Fourth Amendment was to protect the people of the United States against arbitrary action by their own Government; it was never suggested that the provision was intended to restrain the actions of the Federal Government against aliens outside of the United States territory.</p>
<p id="b333-4"><page-number citation-index="1" label="267">*267</page-number>There is likewise no indication that the Fourth Amendment was understood by contemporaries of the Framers to apply to activities of the United States directed against aliens in foreign territory or in international waters. Only seven years after the ratification of the Amendment, French interference with American commercial vessels engaged in neutral trade triggered what came to be known as the “undeclared war” with France. In an Act to “protect the Commerce of the United States” in 1798, Congress authorized President Adams to “instruct the commanders of the public armed vessels which are, or which shall be employed in the service of the United States, to subdue, seize and take any armed French vessel, which shall be found within the jurisdictional limits of the United States, or elsewhere, on the high seas.” § 1 of An Act Further to Protect the Commerce of the United States, ch. 68, <span class="citation no-link">1 Stat. 578</span>. This public naval force consisted of only 45 vessels, so Congress also gave the President power to grant to the owners of private armed ships and vessels of the United States “special commissions,” which would allow them “the same license and authority for the subduing, seizing and capturing any armed French vessel, and for the recapture of the vessels, goods and effects of the people of the United States, as the public armed vessels of the United States may by law have.” § 2, <span class="citation no-link">1 Stat. 579</span>; see U. S. Const., Art. I, §8, cl. 11 (Congress has power to grant letters of marque and reprisal). Under the latter provision, 365 private armed vessels were commissioned before March 1, 1799, see G. Allen, Our Naval War with France 59 (1967); together, these enactments resulted in scores of seizures of foreign vessels under congressional authority. See M. Palmer, Stoddert’s War: Naval Operations During the Quasi-War with France, 1798-1801, p. 235 (1987). See also An Act Further to Suspend the Commercial Intercourse Between the United States and France, ch. 2, <span class="citation no-link">1 Stat. 613</span>. Some commanders were held liable by this Court for unlawful seizures because their actions were beyond the scope of the congres<page-number citation-index="1" label="268">*268</page-number>sional grant of authority, see, <em>e. g., Little </em>v. <em>Barreme, </em><span class="citation" data-id="84781"><a href="/opinion/84781/little-v-barreme/#177" aria-description="Citation for case: Little v. Barreme">2 Cranch 170, 177-178</a></span> (1804); cf. <em>Talbot </em>v. <em>Seeman, </em><span class="citation" data-id="84754"><a href="/opinion/84754/talbot-v-seeman/#81" aria-description="Citation for case: Talbot v. Seeman">1 Cranch 1, 81</a></span> (1801) (seizure of neutral ship lawful where American captain had probable cause to believe vessel was French), but it was never suggested that the Fourth Amendment restrained the authority of Congress or of United States agents to conduct operations such as this.</p>
<p id="b334-5">The global view taken by the Court of Appeals of the application of the Constitution is also contrary to this Court’s decisions in the <em>Insular Cases, </em>which held that not every constitutional provision applies to governmental activity even where the United States has sovereign power. See, <em>e. g., Balzac </em>v. <em>Porto Rico, </em><span class="citation" data-id="99954"><a href="/opinion/99954/balzac-v-porto-rico/" aria-description="Citation for case: Balzac v. Porto Rico">258 U. S. 298</a></span> (1922) (Sixth Amendment right to jury trial inapplicable in Puerto Rico); <em>Ocampo </em>v. <em>United States, </em><span class="citation" data-id="98209"><a href="/opinion/98209/ocampo-v-united-states/" aria-description="Citation for case: Ocampo v. United States">234 U. S. 91</a></span> (1914) (Fifth Amendment grand jury provision inapplicable in Philippines); <em>Dorr </em>v. <em>United States, </em><span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/" aria-description="Citation for case: Dorr v. United States">195 U. S. 138</a></span> (1904) (jury trial provision inapplicable in Philippines); <em>Hawaii </em>v. <em>Mankichi, </em><span class="citation" data-id="9417915"><a href="/opinion/95894/hawaii-v-mankichi/" aria-description="Citation for case: Hawaii v. Mankichi">190 U. S. 197</a></span> (1903) (provisions on indictment by grand jury and jury trial inapplicable in Hawaii); <em>Downes </em>v. <em>Bidwell, </em><span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">182 U. S. 244</a></span> (1901) (Revenue Clauses of Constitution inapplicable to Puerto Rico). In <em><span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/" aria-description="Citation for case: Dorr v. United States">Dorr</a></span>, </em>we declared the general rule that in an unincorporated territory — one not clearly destined for statehood — Congress was not required to adopt “a system of laws which shall include the right of trial by jury, and that <em>the Constitution does not, without legislation and of its own force, carry such right to territory so situated.” </em><span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/#149" aria-description="Citation for case: Dorr v. United States">195 U. S., at 149</a></span> (emphasis added). Only “fundamental” constitutional rights are guaranteed to inhabitants of those territories. <span class="citation" data-id="9417956"><a href="/opinion/96130/dorr-v-united-states/#148" aria-description="Citation for case: Dorr v. United States"><em>Id., </em>at 148</a></span>; <span class="citation" data-id="99954"><a href="/opinion/99954/balzac-v-porto-rico/#312" aria-description="Citation for case: Balzac v. Porto Rico"><em>Balzac, supra, </em>at 312-313</a></span>; see <em>Examining Board of Engineers, Architects and Surveyors </em>v. <em>Flores de Otero, </em><span class="citation" data-id="9426457"><a href="/opinion/109490/examining-bd-of-engineers-architects-and-surveyors-v-flores-de-otero/#599" aria-description="Citation for case: Examining Bd. of Engineers, Architects and Surveyors v....">426 U. S. 572, 599, n. 30</a></span> (1976). If that is true with respect to territories ultimately governed by Congress, respondent’s claim that the protections of the Fourth Amendment extend to aliens in foreign nations is even weaker. And certainly, it is not open to us in light of the <em>Insular Cases </em>to endorse the <page-number citation-index="1" label="269">*269</page-number>view that every constitutional provision applies wherever the United States Government exercises its power.</p>
<p id="b335-5">Indeed, we have rejected the claim that aliens are entitled to Fifth Amendment rights outside the sovereign territory of the United States. In <em>Johnson </em>v. <em>Eisentrager, </em><span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/" aria-description="Citation for case: Johnson v. Eisentrager">339 U. S. 763</a></span> (1950), the Court held that enemy aliens arrested in China and imprisoned in Germany after World War II could not obtain writs of habeas corpus in our federal courts on the ground that their convictions for war crimes had violated the Fifth Amendment and other constitutional provisions. The <em><span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/" aria-description="Citation for case: Johnson v. Eisentrager">Eisentrager</a></span> </em>opinion acknowledged that in some cases constitutional provisions extend beyond the citizenry; “[t]he alien . . . has been accorded a generous and ascending scale of rights as he increases his identity with our society.” <span class="citation" data-id="104813"><a href="/opinion/104813/johnson-v-eisentrager/#770" aria-description="Citation for case: Johnson v. Eisentrager"><em>Id., </em>at 770</a></span>. But our rejection of extraterritorial application of the Fifth Amendment was emphatic:</p>
<blockquote id="b335-6">“Such extraterritorial application of organic law would have been so significant an innovation in the practice of governments that, if intended or apprehended, it could scarcely have failed to excite contemporary comment. Not one word can be cited. No decision of this Court supports such a view. <em>Cf. Downes </em>v. <em>Bidwell, </em><span class="citation" data-id="9417865"><a href="/opinion/95504/downes-v-bidwell/" aria-description="Citation for case: Downes v. Bidwell">182 U. S. 244</a></span> [(1901)]. None of the learned commentators on our Constitution has even hinted at it. The practice of every modern government is opposed to it.” <em>Id., </em>at 784.</blockquote>
<p id="b335-7">If such is true of the Fifth Amendment, which speaks in the relatively universal term of “person,” it would seem even more true with respect to the Fourth Amendment, which applies only to “the people.”</p>
<p id="b335-8">To support his all-encompassing view of the Fourth Amendment, respondent points to language from the plurality opinion in <em>Reid </em>v. <em>Covert, </em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">354 U. S. 1</a></span> (1957). <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>involved an attempt by Congress to subject the wives of American servicemen to trial by military tribunals without the protection of the Fifth and Sixth Amendments. The Court held that it was unconstitutional to apply the Uniform Code of Military <page-number citation-index="1" label="270">*270</page-number>Justice to the trials of the American women for capital crimes. Four Justices “rejected] the idea that when the United States acts <em>against citizens </em>abroad it can do so free of the Bill of Rights.” <span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/#5" aria-description="Citation for case: Reid v. Covert"><em>Id., </em>at 5</a></span> (emphasis added). The plurality went on to say:</p>
<blockquote id="b336-5">“The United States is entirely a creature of the Constitution. Its power and authority have no other source. It can only act in accordance with all the limitations imposed by the Constitution. When the Government reaches out to punish <em>a citizen </em>who is abroad, the shield which the Bill of Rights and other parts of the Constitution provide to protect his life and liberty should not be stripped away just because he happens to be in another land.” <span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/#5" aria-description="Citation for case: Reid v. Covert"><em>Id., </em>at 5-6</a></span> (emphasis added; footnote omitted).</blockquote>
<p id="b336-6">Respondent urges that we interpret this discussion to mean that federal officials are constrained by the Fourth Amendment wherever and against whomever they act. But the holding of <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>stands for no such sweeping proposition: it decided that United States citizens stationed abroad could invoke the protection of the Fifth and Sixth Amendments. The concurrences by Justices Frankfurter and Harlan in <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>resolved the case on much narrower grounds than the plurality and declined even to hold that United States citizens were entitled to the full range of constitutional protections in all overseas criminal prosecutions. See <span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/#75" aria-description="Citation for case: Reid v. Covert"><em>id., </em>at 75</a></span> (Harlan, J., concurring in result) (“I agree with my brother Frankfurter that... we have before us a question analogous, ultimately, to issues of due process; one can say, in fact, that the question of which specific safeguards of the Constitution are appropriately to be applied in a particular context overseas can be reduced to the issue of what process is ‘due’ a defendant in the particular circumstances of a particular case”). Since respondent is not a United States citizen, he can derive no comfort from the <em><span class="citation" data-id="9421456"><a href="/opinion/105525/reid-v-covert/" aria-description="Citation for case: Reid v. Covert">Reid</a></span> </em>holding.</p>
<p id="b336-7">Verdugo-Urquidez also relies on a series of cases in which we have held that aliens enjoy certain constitutional rights. <page-number citation-index="1" label="271">*271</page-number>See, <em>e. g., Plyler </em>v. <em>Doe, </em><span class="citation" data-id="9428818"><a href="/opinion/110742/plyler-v-doe/#211" aria-description="Citation for case: Plyler v. Doe">457 U. S. 202, 211-212</a></span> (1982) (illegal aliens protected by Equal Protection Clause); <em>Kwong Hai Chew </em>v. <em>Colding, </em><span class="citation" data-id="105078"><a href="/opinion/105078/kwong-hai-chew-v-colding/#596" aria-description="Citation for case: Kwong Hai Chew v. Colding">344 U. S. 590, 596</a></span> (1953) (resident alien is a “person” within the meaning of the Fifth Amendment); <em>Bridges </em>v. <em>Wixon, </em><span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/#148" aria-description="Citation for case: Bridges v. Wixon">326 U. S. 135, 148</a></span> (1945) (resident aliens have First Amendment rights); <em>Russian Volunteer Fleet </em>v. <em>United States, </em><span class="citation" data-id="101660"><a href="/opinion/101660/russian-volunteer-fleet-v-united-states/" aria-description="Citation for case: Russian Volunteer Fleet v. United States">282 U. S. 481</a></span> (1931) (Just Compensation Clause of Fifth Amendment); <em>Wong Wing </em>v. <em>United States, </em><span class="citation" data-id="9883065"><a href="/opinion/94479/wong-wing-v-united-states/#238" aria-description="Citation for case: Wong Wing v. United States">163 U. S. 228, 238</a></span> (1896) (resident aliens entitled to Fifth and Sixth Amendment rights); <em>Yick Wo </em>v. <em>Hopkins, </em><span class="citation" data-id="91704"><a href="/opinion/91704/yick-wo-v-hopkins/#369" aria-description="Citation for case: Yick Wo v. Hopkins">118 U. S. 356, 369</a></span> (1886) (Fourteenth Amendment protects resident aliens). These cases, however, establish only that aliens receive constitutional protections when they have come within the territory of the United States and developed substantial connections with this country. See, <span class="citation" data-id="9428818"><a href="/opinion/110742/plyler-v-doe/#212" aria-description="Citation for case: Plyler v. Doe"><em>e. g., Plyler, supra, </em>at 212</a></span> (The provisions of the Fourteenth Amendment “ ‘are universal in their application, <em>to all persons within the territorial jurisdiction . </em>. .’”) (quoting <em>Yick Wo, supra, </em>at 369); <span class="citation" data-id="105078"><a href="/opinion/105078/kwong-hai-chew-v-colding/#596" aria-description="Citation for case: Kwong Hai Chew v. Colding"><em>Kwong Hai Chew, supra, </em>at 596, n. 5</a></span> (“The Bill of Rights is a futile authority for the alien seeking admission for the first time to these shores. But <em>once an alien lawfully enters and resides in this country </em>he becomes invested with the rights guaranteed by the Constitution to all people within our borders”) (quoting <span class="citation" data-id="9419697"><a href="/opinion/104184/bridges-v-wixon/#161" aria-description="Citation for case: Bridges v. Wixon"><em>Bridges, supra, </em>at 161</a></span> (concurring opinion) (emphasis added)). Respondent is an alien who has had no previous significant voluntary connection with the United States, so these cases avail him not.</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/United States v. Vinton.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "274a6141e1a9a0ba", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Vinton"}, "payload": {"all": [{"cite": "594 F.3d 14", "page": "14", "reporter": "F.3d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "594"}, {"cite": "389 U.S. App. D.C. 199", "page": "199", "reporter": "U.S. App. D.C.", "selected_official": false, "source": "cluster.citations[]", "type": 2, "volume": "389"}, {"cite": "2010 U.S. App. LEXIS 2450", "page": "2450", "reporter": "U.S. App. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2010"}, {"cite": "2010 WL 392347", "page": "392347", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2010"}], "display": "594 F.3d 14", "official": {"cite": "594 F.3d 14", "page": "14", "reporter": "F.3d", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "594"}, "official_selection_present": true, "record_id": "United States v. Vinton"}}
{"assertion_id": "5b852f10961b5186", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-20", "record_id": "United States v. Vinton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-20", "pinpoint_status": "slip-only", "quote": "sticker that could suggest a false law-enforcement affiliation, and knowledge of a recent nearby double-stabbing, Aton conducted a protective search of the passenger compartment, then arrested and handcuffed Vinton and pried open the locked briefcase, finding contraband and a firearm. While Vinton's appeal was pending, the Supreme Court decided *Arizona v. Gant*; Vinton argued *Gant* required suppression. ## Issue Whether a protective search of a vehicle's passenger compartment for weapons under *Michigan v. Long* remains valid after the suspect has been removed and handcuffed, and whether *Arizona v. Gant*'s limits on searches incident to arrest displace that protective-search authority. ## Rule A *Michigan v. Long* protective search of the passenger compartment is justified by reasonable suspicion that the driver is dangerous and could gain access to weapons, and that justification is not eliminated by securing the suspect:", "quote_fidelity": "mismatch", "record_id": "United States v. Vinton", "star_marker": null}}
{"assertion_id": "fa767babc75e92fb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-21", "record_id": "United States v. Vinton"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-21", "pinpoint_status": "slip-only", "quote": "Examining the totality of the circumstances objectively, Officer Aton had a reasonable belief, based on specific and articulable facts, that Vinton was armed and dangerous. . . . Thus, he properly searched the passenger compartment of Vinton's car for additional weapons.", "quote_fidelity": "mismatch", "record_id": "United States v. Vinton", "star_marker": null}}
{"assertion_id": "1bee900080e888c3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Vinton"}, "payload": {"as_of_content": "2010-02-05", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "United States v. Vinton", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/United States v. Von Neumann.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: United States v. Von Neumann
type: case
citation: "474 U.S. 242 (1986)"
parallel_cite: "106 S. Ct. 610; 88 L. Ed. 2d 587; 54 U.S.L.W. 4065"
neutral_cite: 1986 U.S. LEXIS 39
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1986
date_decided: 1986-01-14
docket: No. 84-1144
authority_weight: "Binding — SCOTUS"
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
  opinion_url: "https://www.courtlistener.com/opinion/111551/united-states-v-von-neumann/"
  cluster_id: 111551
  opinion_id: null
  identity_checked: true
lake:
  record_id: United States v. Von Neumann
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. $8,850 in Currency]]"
tags:
  - case
  - civil-forfeiture
  - due-process
  - remission
  - customs
  - delay
holding: "A 36-day delay by the Customs Service in ruling on a petition for remission or mitigation after seizing an undeclared car did not deny the claimant due process: because the judicial forfeiture proceeding itself supplies the post-seizure hearing due process requires (its timeliness measured by the Barker v. Wingo factors), the discretionary remission procedure is not constitutionally necessary and creates no separate right to a speedy answer to a remission petition."
aliases:
  - United States v. Von Neumann
  - "United States v. Von Neumann (1986)"
---

# United States v. Von Neumann

*474 U.S. 242 (1986)* (No. 84-1144) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 111551 → combined opinion 111551 (Brennan, J.; 474 U.S. 242, argued Nov. 4, 1985, decided Jan. 14, 1986). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star: the quoted holding sits between `*250` and `*251`, i.e., on page 250). S9 promotes. -->

## Background
In January 1975, John Von Neumann drove a Jaguar Panther he had bought in Switzerland across the Canadian border into Washington State and failed to declare it to U.S. customs; a customs officer seized the car under 19 U.S.C. § 1497. The same day, Von Neumann filed a petition for remission or mitigation under 19 U.S.C. § 1618, and about two weeks later posted a $24,500 bond to get the car back. Thirty-six days after the petition was filed, the Customs Service acted on it, reducing the penalty to $3,600. After exhausting administrative review, Von Neumann sued, and the Ninth Circuit held that the 36-day delay in ruling on the remission petition denied him due process — going so far as to require Customs to act on such petitions within 24 hours.

## Issue
Whether a claimant whose property has been seized has a due process right to a speedy disposition of his § 1618 petition for remission or mitigation, such that a 36-day delay in ruling on the petition violates the Fifth Amendment.

## Rule
The Court located the claimant's constitutional protection in the forfeiture proceeding itself, not in the remission procedure. Under *[[United States v. $8,850 in Currency|$8,850]]*, the judicial forfeiture action — whose own timeliness is measured by the *Barker v. Wingo* factors — provides the post-seizure hearing due process requires. Remission is a discretionary act of grace that lets the parties resolve the matter informally, but it is not a step the Constitution mandates. The Court therefore held: "Thus there is no constitutional basis for a claim that respondent's interest in the car, or in the money put up to secure the bond, entitles him to a speedy answer to his remission petition." — 474 U.S. at 250. ^pin-250

## Application
Because remission proceedings are not necessary to a forfeiture determination, the claimant's property interest in the car and the bond money gave him no constitutional entitlement to a prompt ruling on his remission petition; his protection was the right to a timely forfeiture proceeding, which he had. The Court added that, even assuming § 1618 created some protectable interest, any timeliness requirement was amply satisfied here: the delay was brief, part of it may not even count (Von Neumann supplemented his petition and got a final decision 13 days later), and he showed no prejudice to either his forfeiture defense or his remission "case," which was complete when filed.

## Conclusion
The judgment of the Court of Appeals for the Ninth Circuit was **reversed**. Brennan, J., delivered the opinion of the Court; Stevens, J., filed an opinion concurring in the judgment.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Von Neumann* fixes the constitutional locus of forfeiture process: the due process a claimant is owed attaches to the *forfeiture proceeding* (timed under *[[United States v. $8,850 in Currency|$8,850]]*'s *Barker* factors), not to the discretionary administrative *remission* petition. Teach it with *[[United States v. $8,850 in Currency]]* (the timeliness framework it applies) as the pair that maps where — and where not — due process constrains the pace of civil forfeiture.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*United States v. Von Neumann*, 474 U.S. 242 (1986)](https://www.courtlistener.com/opinion/111551/united-states-v-von-neumann/) — pinpoint: 250 (Brennan, J., for the Court; the CL opinion text places the quoted holding between the reporter stars `*250` and `*251`, i.e., on page 250). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1deaf9a8c0c9b4ce", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "United States v. Von Neumann"}, "payload": {"all": [{"cite": "474 U.S. 242", "page": "242", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "474"}, {"cite": "106 S. Ct. 610", "page": "610", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "106"}, {"cite": "88 L. Ed. 2d 587", "page": "587", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "1986 U.S. LEXIS 39", "page": "39", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1986"}, {"cite": "54 U.S.L.W. 4065", "page": "4065", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "54"}], "display": "474 U.S. 242", "official": {"cite": "474 U.S. 242", "page": "242", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "474"}, "official_selection_present": true, "record_id": "United States v. Von Neumann"}}
{"assertion_id": "75e0eb1e1fb6251d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "United States v. Von Neumann"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "United States v. Von Neumann", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — United States v. Von Neumann

```json
{
  "schema_version": "s2.v1",
  "record_id": "United States v. Von Neumann",
  "status": "under_review",
  "identity": {
    "case_name": "United States v. Von Neumann",
    "case_name_short": "Von Neumann",
    "case_name_full": "United States v. Von Neumann",
    "input_case_name": "United States v. Von Neumann",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1986-01-14",
    "year": 1986,
    "docket": "No. 84-1144",
    "cluster_id": 111551,
    "lead_opinion_id": 9430249,
    "sibling_ids": [],
    "absolute_url": "/opinion/111551/united-states-v-von-neumann/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "474 U.S. 242",
      "volume": "474",
      "reporter": "U.S.",
      "page": "242",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "106 S. Ct. 610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 587",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4065",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1986 U.S. LEXIS 39",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "39",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "474 U.S. 242",
        "volume": "474",
        "reporter": "U.S.",
        "page": "242",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 S. Ct. 610",
        "volume": "106",
        "reporter": "S. Ct.",
        "page": "610",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 L. Ed. 2d 587",
        "volume": "88",
        "reporter": "L. Ed. 2d",
        "page": "587",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1986 U.S. LEXIS 39",
        "volume": "1986",
        "reporter": "U.S. LEXIS",
        "page": "39",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "54 U.S.L.W. 4065",
        "volume": "54",
        "reporter": "U.S.L.W.",
        "page": "4065",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "474 U.S. 242",
    "official_selection": {
      "court_class": "scotus",
      "selected": "474 U.S. 242",
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
    "date_created": "2026-07-06T13:41:55Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:56Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "united-states-v-von-neumann--111551",
      "to_record_id": "United States v. Von Neumann",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — United States v. Von Neumann

```
<opinion type="majority">
<author id="b381-10">Justice Brennan</author>
<p id="AMB">delivered the opinion of the Court.</p>
<p id="b381-11">We must decide in this case whether a 36-day delay by the United States Customs Service in responding to a remission petition filed by respondent in response to the seizure of his car by customs agents deprived respondent of property without due process of law.</p>
<p id="b381-12">I</p>
<p id="b381-13">Title <span class="citation no-link">19 U. S. C. § 1497</span><footnotemark>1</footnotemark> provides that any article not declared upon entry into the United States which by law <page-number citation-index="1" label="244">*244</page-number>must be declared is subject to forfeiture or to a penalty equaling the value of the article. After seizure of an article by the United States Customs Service, a claimant to it has essentially two options. He may pursue an administrative remedy under <span class="citation no-link">19 U. S. C. §1618</span> (1982 ed., Supp. Ill),<footnotemark>2</footnotemark> which vests in the Secretary of the Treasury the discretionary authority to mitigate or remit the penalty or forfeiture, or he may challenge the seizure in a judicial forfeiture action initiated by the Government.<footnotemark>3</footnotemark> <span class="citation no-link">19 U. S. C. §§ 1602-1604</span>.<footnotemark>4</footnotemark></p>
<p id="b383-4"><page-number citation-index="1" label="245">*245</page-number>In 1974, respondent John Von Neumann shipped to Vancouver, Canada, a 1974 Jaguar Panther automobile he purchased in Switzerland. On January 20, 1975, he and a friend picked up the car in Vancouver, obtained a release from Canadian Customs to take possession of the vehicle and also obtained a form that Von Neumann was to deliver to the Canadian Customs station at the border. Von Neumann failed to deliver the form to Canadian Customs officials. He claimed that he inadvertently drove past the Canadian Customs station because of poor visibility and inadequate directions. Instead, Von Neumann and his friend arrived at the United States border checkpoint at Blaine, Washington, where they were questioned by United States Immigration Officer Harry Perkins, a designated customs officer. Canadian Customs officials had earlier alerted United States Customs that Von Neumann’s car would be crossing the border, and Perkins specifically asked Von Neumann whether he had anything to declare. When Von Neumann failed to declare the automobile, Perkins asked him into the checkpoint station and referred the matter to Customs Inspector Donald E. Morrison. Upon being asked why he had not declared the car, Von Neumann explained that he did not think a declaration was required. Morrison then seized the car pursuant to <span class="citation no-link">19 U. S. C. § 1497</span>.</p>
<p id="b383-5">That same day, January 20, Von Neumann prepared a “Petition for Remission or Mitigation of Forfeitures and Penalties Incurred,” pursuant to <span class="citation no-link">19 U. S. C. § 1618</span>, explaining that he had not intended to violate United States Customs laws when he failed to declare the car. Two weeks later, on February 3, Von Neumann posted a bond for $24,500, the <page-number citation-index="1" label="246">*246</page-number>value of his car, and Customs released the vehicle pursuant to its authority under <span class="citation no-link">19 U. S. C. § 1614</span>. On February 12, counsel for Von Neumann filed a supplement to the original remission petition. On February 25 — 36 days after the petition was filed — the Seattle District Director of the Customs Service, pursuant to delegation of authority from the Secretary of the Treasury,<footnotemark>5</footnotemark> acted on Von Neumann’s remission petition, and informed Von Neumann that the penalty for failure to declare the car was being reduced to $3,600. On administrative review of this determination, the Regional Commissioner of Customs in San Francisco, on April 14, 1975, upheld the $3,600 penalty.</p>
<p id="b384-5">Having exhausted his administrative remedies, Von Neu-mann filed a complaint in the United States District Court for the Central District of California. He sought cancellation of the $3,600 penalty on the ground that he had not violated § 1497. He also requested an injunction prohibiting Customs from placing his name on a computer list of violators, and a declaration that this seizure and penalty were unlawful. The District Court found that Von Neumann had violated <span class="citation no-link">19 U. S. C. § 1497</span>, and that seizure of the car therefore was proper. The court also upheld the validity of the remission and mitigation procedures. Accordingly, it entered judgment for the Government.<footnotemark>6</footnotemark> Von Neumann appealed this de-<page-number citation-index="1" label="247">*247</page-number>cisión, challenging both the procedures followed by Customs in imposing the penalty and also the penalty itself.</p>
<p id="b385-5">The Court of Appeals for the Ninth. Circuit agreed with the District Court that Von Neumann had violated § 1497. <span class="citation multiple-matches"><a href="/c/F.%202d/660/1319/">660 F. 2d 1319</a></span>, 1323 (1981). The court, however, also considered and sustained Von Neumann’s claim that the 36-day delay in acting on his remission petition denied Von Neu-mann due process of law in violation of the Fifth Amendment. The court reasoned that speed in the handling of the remission petition, particularly where the seizure is of an automobile, is constitutionally required — that strict guidelines in responding to remission petitions are necessary “to ensure the due process rights of administrative claimants,” <em>id., </em>at 1326-1327, and concluded that Customs must “act on a petition for remission or mitigation within 24 hours of receipt,” <em>id., </em>at 1327. In addition, the court ruled, a claimant has a right to a personal appearance to present his or her claim. <em>Ibid.</em></p>
<p id="b385-6">The Government petitioned for certiorari. We granted the petition, vacated, and remanded for reconsideration in light of <em>United States </em>v. <em>$8,850, </em><span class="citation multiple-matches"><a href="/c/U.%20S./461/665/">461 U. S. 665</a></span> (1983). <span class="citation" data-id="9039097"><a href="/opinion/9045725/united-states-v-von-neumann/" aria-description="Citation for case: United States v. Von Neumann">462 U. S. 1101</a></span> (1983). In <em>$8,850, </em>however, the issue presented did not involve the remission procedure; rather the question was whether the Government’s 18-month delay in bringing a <em>forfeiture </em>proceeding violated the claimant’s right to due process of law. The Court held that due process requires a postseizure determination within a reasonable time of the seizure. We concluded that the four-factor balancing test of <em>Barker </em>v. <em>Wingo, </em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">407 U. S. 514</a></span> (1972), provides the relevant framework for determining whether a delay was reasonable. The <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test involves a weighing of four factors: the length of any delay, the reason for the delay, the defendant’s assertion of his right, and prejudice suffered by the defendant. Applying this test to the 18-month delay before it, the <page-number citation-index="1" label="248">*248</page-number>Court in <em>$8,850 </em>found no unreasonable delay, in part because a substantial portion of the delay in question was attributable to pending administrative and criminal proceedings.</p>
<p id="b386-5">On remand in this case, the Court of Appeals recognized that <em>$8,850 </em>“presented a somewhat different issue from that arising in the instant case,” <span class="citation multiple-matches"><a href="/c/F.%202d/729/657/">729 F. 2d 657</a></span>, 659 (1984), because <em>$8,850 </em>dealt with forfeiture rather than the remission procedure. Nevertheless, it concluded that this Court’s holding in <em>$8,850 </em>“reinforces our earlier view that due process rights attach to the processing of the petition for remission,” 729 F. 2d, at 660, and therefore reaffirmed its holding that “due process requires Customs to act promptly in ruling on petitions for remission or mitigation under <span class="citation no-link">19 U. S. C. §1618</span>.” <em><span class="citation no-link">Ibid.</span> </em>The court recognized that its earlier attempt to set specific time limits for the processing of remission petitions was “ill-advised,” <em>ibid., </em>and held instead that the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>factors should also be applied to determine whether Customs has violated due process in delaying a response to a remission petition. The court accordingly remanded the case to the District Court to consider whether the 36-day delay violated due process. In addition, however, the court made clear its view that the circumstances of this case support a finding of a due process violation. Thus, the court noted that the propriety of the length of the delay may turn on the nature of the item that has been seized, and reemphasized the point made in its earlier opinion that “special hardships [are] imposed on persons deprived of the use of their automobiles . . . .” 729 F. 2d, at 661. With respect to the reason for the delay, the Court of Appeals observed that the “record here provides no obvious reason for the Government’s one-month delay in processing von Neumann’s petition, although we note that Customs processes a great number of petitions each year.” <em>Ibid. </em>In addition, the court pointed to the filing of the remission petition itself as the necessary assertion of the right to a speedy determination under <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span>. </em>Finally, the court <page-number citation-index="1" label="249">*249</page-number>noted that prejudice could be established by the inconvenience of being without a vehicle for any length of time.</p>
<p id="b387-7">Arguing that due process considerations do not govern the Secretary’s disposition of remission petitions, the Government petitioned for certiorari. We granted the Government’s petition. <span class="citation multiple-matches"><a href="/c/U.%20S./471/1064/">471 U. S. 1064</a></span> (1984). We now reverse.</p>
<p id="b387-8">I — ! b — I</p>
<p id="b387-1">We understand respondent to argue that his property interest in his car gives him a constitutional right to a speedy disposition of his remission petition without awaiting a forfeiture proceeding. We disagree. Implicit in this Court’s discussion of timeliness in <em>$8,850 </em>was the view that the forfeiture proceeding, without more, provides the postseizure hearing required by due process to protect Von Neumann’s property interest in the car.<footnotemark>7</footnotemark> Respondent argues, however, that “[t]he petition for remission procedure is just one step in which it is determined whether that property interest will be extinguished via a judicial foreclosure proceeding.” Brief for Respondent 8-9. We think respondent misunderstands the remission procedure’s role. It is true that, as a practical matter, most forfeitures are disposed of through the administrative remission procedures,<footnotemark>8</footnotemark> but that is constitutionally <page-number citation-index="1" label="250">*250</page-number>irrelevant. We noted in <em>One Lot Emerald Cut Stones </em>v. <em>United States, </em><span class="citation" data-id="108643"><a href="/opinion/108643/one-lot-emerald-cut-stones-and-one-ring-v-united-states/#234" aria-description="Citation for case: One Lot Emerald Cut Stones and One Ring v. United States">409 U. S. 232, 234</a></span> (1972), that in the event an item is not declared at the border under § 1497 “[t]he Government need only prove that the property was brought into the United States without the required declaration; the Government bears no burden with respect to intent.” The remission statute simply grants the Secretary the discretion not to pursue a complete forfeiture despite the Government’s entitlement to one. Remission proceedings supply both the Government and the claimant a way to resolve a dispute informally rather than in judicial forfeiture proceedings. But remission proceedings are not <em>necessary </em>to a forfeiture determination, and therefore are not constitutionally required. Thus there is no constitutional basis for a claim that respondent’s interest in the car, or in the money put up to secure the bond, entitles him to a speedy answer to his remission petition.</p>
<p id="b388-5">Ill</p>
<p id="b388-6">While his interest in the car is the only basis on which respondent relies in his support of the Court of Appeals’ decision, the Government asks that the Court adjudge the case of a claimant who relies on the argument that § 1618 itself creates a property right which cannot be taken away without due process that includes a speedy answer to a remission petition. The Government argues that the statute creates no such right. We need not address the hypothetical, however. It is abundantly clear on, the record in this case that, even if respondent had such a property right, any due process requirement of timely disposition was more than adequately provided here. It is difficult, indeed impossible, to see what prejudice respondent suffered from the 36-day delay in the response. True, he was without his car for 14 days, and then, for another 22 days, without the money he <page-number citation-index="1" label="251">*251</page-number>had to put up to secure a bond, and Von Neumann urges the importance of automobiles to citizens in this society. But we have already noted that his right to a forfeiture proceeding meeting the <em><span class="citation" data-id="9424967"><a href="/opinion/108590/barker-v-wingo/" aria-description="Citation for case: Barker v. Wingo">Barker</a></span> </em>test satisfies any due process right with respect to the car and the money. In fact, it is not altogether certain that the delay dated from the filing on January 20 of the original remission petition. Respondent supplemented his remission petition and was given a final decision just 13 days later. Moreover, respondent gives no hint as to how or why even a 36-day delay in the disposition of his remission petition deprived him of the process he claims was his due in connection with that petition. He does not argue that the delay prejudiced his defense against the forfeiture, see <em>$8,850, </em>461 U. S., at 569, and with respect to preparing his “case” for remission, that case was made at the time of filing and could not have been affected by the subsequent delay. On the record before us, the 36-day delay cannot be said to deprive respondent of due process of law.</p>
<p id="b389-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b381-14"> Section 497, <span class="citation no-link">46 Stat. 728</span>, <span class="citation no-link">19 U. S. C. § 1497</span>, provides:</p>
<p id="b381-15">“Any article not included in the declaration and entry as made, and, before examination of the baggage was begun, not mentioned in writing by such person, if written declaration and entry was required, or orally if written <page-number citation-index="1" label="244">*244</page-number>declaration and entry was not required, shall be subject to forfeiture and such person shall be liable to a penalty equal to the value of such article.”</p>
</footnote>
<footnote label="2">
<p id="b382-6"> Section 618, <span class="citation no-link">46 Stat. 757</span>, as amended and set forth in <span class="citation no-link">19 U. S. C. § 1618</span> (1982 ed., Supp. Ill), provides in pertinent part:</p>
<p id="b382-7">“Whenever any person interested in any vessel, vehicle, aircraft, merchandise, or baggage seized under the provisions of this chapter, or who has incurred, or is alleged to have incurred, any fine or penalty thereunder, files with the Secretary of the Treasury if under the customs laws ... before the sale of such vessel, vehicle, aircraft, merchandise, or baggage a petition for the remission or mitigation of such fine, penalty, or forfeiture, the Secretary of the Treasury ... if he finds that such fine, penalty, or forfeiture was incurred without willful negligence or without any intention on the part of the petitioner to defraud the revenue or to violate the law, or finds the existence of such mitigating circumstances as to justify the remission or mitigation of such fine, penalty, or forfeiture, may remit or mitigate the same upon such terms and conditions as he deems reasonable and just, or order discontinuance of any prosecution relating thereto.”</p>
</footnote>
<footnote label="3">
<p id="b382-8"> The claimant may trigger the Government’s initiation of forfeiture proceedings. In <em>United States </em>v. <em>$8,850, </em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#569" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S. 555, 569</a></span> (1983), we noted:</p>
<p id="AKp"><em>“A </em>claimant is able to trigger rapid filing of a forfeiture action if he desires it. First, the claimant can file an equitable action seeking an order compelling the filing of the forfeiture action or return of the seized property. See <em>Slocum </em>v. <em>Mayberry, </em><span class="citation" data-id="85171"><a href="/opinion/85171/slocum-v-mayberry/#10" aria-description="Citation for case: Slocum v. Mayberry">2 Wheat. 1, 10</a></span> (1817) (Marshall, C. J.). Less formally, the claimant could simply request that the Customs Service refer the matter to the United States Attorney. If the claimant believes the initial seizure was improper, he could file a motion under Federal Rule of Criminal Procedure 41(e) for a return of the seized property.”</p>
</footnote>
<footnote label="4">
<p id="b382-9"> When the Jaguar was seized in this case, a customs officer could have instituted nonjudicial, summary forfeiture proceedings if the value of the car had been not more than $10,000. See <span class="citation no-link">19 U. S. C. §§ 1607-1609</span>. Congress has since raised this limit to $100,000. <span class="citation no-link">19 U. S. C. § 1607</span> (1982 ed., <page-number citation-index="1" label="245">*245</page-number>Supp. III). Even for a seizure of property appraised at less than $100,000, the claimant has a right to a judicial determination upon posting a bond to cover costs in the sum of $2,500 or 10% of the value of the claimed property, whichever is smaller, but not less than $250. <span class="citation no-link">19 U. S. C. § 1608</span> (1982 ed., Supp. III).</p>
</footnote>
<footnote label="5">
<p id="b384-6"> The Secretary of the Treasury is authorized by statute to act on petitions for remission. <span class="citation no-link">19 U. S. C. § 1618</span>. This authority has been delegated to District Directors of the Customs Service in some cases where the total value of the merchandise forfeited does not exceed $100,000, <span class="citation no-link">19 CFR § 171.21</span> (1985). At the time of this seizure, the limit was $25,000. See <span class="citation no-link">19 CFR § 171.21</span> (1974).</p>
</footnote>
<footnote label="6">
<p id="b384-7"> The Government filed a contingent counterclaim seeking recovery of the full $24,500 in accordance with <span class="citation no-link">19 U. S. C. § 1497</span>, in the event the District Court found the mitigation invalid. Because the District Court entered judgment in favor of the Government on the merits of Von Neumann’s complaint, it denied the contingent counterclaim. In its answer in the District Court the Government had also contended that the remission and mitigation sought and received by respondent was a settle<page-number citation-index="1" label="247">*247</page-number>ment, accord, and satisfaction binding on Von Neumann. The District Court did not reach this issue; nor do we.</p>
</footnote>
<footnote label="7">
<p id="b387-2"> In <em>$8,850 </em>the claimant conceded that no preseizure hearing is required when Customs makes a seizure at the border. Respondent does not dispute that here, and we doubt that he could. In <em>$8,850 </em>we noted that while the general rule is that “absent an ‘extraordinary situation’ a party cannot invoke the power of the state to seize a person’s property without a <em>prior </em>judicial determination that the seizure is justified. . . . [D]ue process does not require federal customs officials to conduct a hearing before seizing items subject to forfeiture.” <span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/#562" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">461 U. S., at 562, n. 12</a></span>. We reasoned that such a requirement would make customs processing entirely unworkable and also found that because “the seizure serves important governmental purposes[,] a preseizure notice might frustrate the statutory purpose ....” <em><span class="citation" data-id="9429199"><a href="/opinion/110936/united-states-v-eight-thousand-eight-hundred-fifty-dollars/" aria-description="Citation for case: United States v. Eight Thousand Eight Hundred &amp; Fifty...">Ibid.</a></span></em></p>
</footnote>
<footnote label="8">
<p id="b387-3"> We noted in <em>$8,850 </em>that Customs processes over 50,000 noncontraband forfeitures per year, and that in 90% of all seizures, the claimant files a petition for remission or mitigation. We further noted that the Secretary <page-number citation-index="1" label="250">*250</page-number>in turn grants at least partial relief for an estimated 75% of the petitions. Typically, this mitigation process terminates the dispute without the necessity of filing a forfeiture action.</p>
</footnote>
</opinion>
```

---
