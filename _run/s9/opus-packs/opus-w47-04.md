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

## GROUP: content/cases/Mullenix v. Luna.md  (`case`, 5 assertions)

### content_page

```
---
title: "Mullenix v. Luna"
type: case
citation: ""
parallel_cite: "577 U.S. 7; 136 S. Ct. 305; 193 L. Ed. 2d 255; 84 U.S.L.W. 4003; 25 Fla. L. Weekly Fed. S 555"
neutral_cite: 2015 U.S. LEXIS 7160
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2015
date_decided: 2015-11-09
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2015-11-09
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mullenix v. Luna
  varies_by_point: false
  scope_note: "Per curiam; good law on the specificity of 'clearly established' law for qualified immunity."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/3153112/mullenix-v-luna/"
  cluster_id: 3153112
  opinion_id: 3153112
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
related: ["[[Tennessee v. Garner]]", "[[Scott v. Harris]]", "[[Kisela v. Hughes]]", "[[White v. Pauly]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "excessive-force", "clearly-established"]
holding: "'Clearly established' law must be particularized to the specific context — 'the dispositive question is whether the violative nature of particular conduct is clearly established.'"
lake:
  record_id: Mullenix v. Luna
  status: verified
  projected_at: 2026-07-06
---

# Mullenix v. Luna

*577 U.S. 7 (2015)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A fleeing, reportedly intoxicated suspect, Israel Leija, led police on a high-speed chase and twice threatened by phone to shoot officers. As other officers set up spike strips beneath an overpass, Trooper Mullenix instead fired six rifle shots at Leija's car from the overpass, killing him. Leija's estate sued Mullenix under § 1983 for excessive force.

## Issue
Whether Mullenix was entitled to [[Qualified Immunity|qualified immunity]] — that is, whether the unlawfulness of his use of deadly force was clearly established at the time he acted.

## Rule
[[Qualified Immunity|Qualified immunity]] shields an official unless his conduct violated clearly established law, and that law must be identified with specificity, not at a high level of generality. "We have repeatedly told courts . . . not to define clearly established law at a high level of generality." — 577 U.S. at 12 (quoting *al-Kidd*). ^pin-12

"The dispositive question is 'whether the violative nature of particular conduct is clearly established.'" — *Id.* The inquiry must be undertaken in light of the specific context of the case, and existing precedent must place the conclusion that the officer acted unlawfully "beyond debate." — *Id.* at 11.

## Application
The relevant question was not whether deadly force against a fleeing felon is generally permissible, but whether it was clearly established that Mullenix acted unreasonably in the specific situation he confronted — a reportedly intoxicated fugitive who had twice threatened to shoot officers and was fleeing at high speed toward an officer's position. Because existing precedent did not place the unreasonableness of his conduct "beyond debate" in that situation, Mullenix was entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
Reversed (per curiam): Mullenix was entitled to [[Qualified Immunity|qualified immunity]] because the law did not clearly establish that his conduct was unconstitutional in the situation he faced.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Mullenix* is a leading statement that "clearly established" law must be defined with [[Particularity|particularity]] to the specific factual context, a principle reaffirmed in qualified-immunity cases such as [[Kisela v. Hughes]] and [[White v. Pauly]].

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*

## Sources
- *Mullenix v. Luna*, 577 U.S. 7 (2015) (per curiam) — https://www.courtlistener.com/opinion/3153112/mullenix-v-luna/ — pinpoints: 11, 12 (CL opinion in slip-opinion format; U.S. Reports pages per official citation).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "cf7182f66822aaef", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2015 U.S. LEXIS 7160", "official_citation_present": false, "parallel_cite": "577 U.S. 7; 136 S. Ct. 305; 193 L. Ed. 2d 255; 84 U.S.L.W. 4003; 25 Fla. L. Weekly Fed. S 555", "title": "Mullenix v. Luna", "year": "2015"}}
{"assertion_id": "407e32a575c0b4d4", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Mullenix v. Luna"}}
{"assertion_id": "81276d7da94e4a21", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "'Clearly established' law must be particularized to the specific context — 'the dispositive question is whether the violative nature of particular conduct is clearly established.'", "title": "Mullenix v. Luna"}}
{"assertion_id": "04a85905d2829753", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Mullenix v. Luna"}}
{"assertion_id": "5a5b42cfff89ef93", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2015-11-09", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Mullenix v. Luna", "field_i_validity": "good_law", "scope_note": "Per curiam; good law on the specificity of 'clearly established' law for qualified immunity.", "title": "Mullenix v. Luna", "varies_by_point": "false"}}
```

### lake record — Mullenix v. Luna

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mullenix v. Luna",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mullenix v. Luna",
    "case_name_short": "Mullenix",
    "case_name_full": "Chadrin Lee MULLENIX v. Beatrice LUNA, Individually and as Representative of the Estate of Israel Leija, Jr., Et Al.",
    "input_case_name": "Mullenix v. Luna",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2015-11-09",
    "year": 2015,
    "docket": null,
    "cluster_id": 3153112,
    "lead_opinion_id": 3153112,
    "sibling_ids": [
      3153112,
      9820073,
      9820074
    ],
    "absolute_url": "/opinion/3153112/mullenix-v-luna/",
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
        "cite": "577 U.S. 7",
        "volume": "577",
        "reporter": "U.S.",
        "page": "7",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 305",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "305",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "193 L. Ed. 2d 255",
        "volume": "193",
        "reporter": "L. Ed. 2d",
        "page": "255",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4003",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4003",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 555",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "555",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2015 U.S. LEXIS 7160",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "7160",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "577 U.S. 7",
        "volume": "577",
        "reporter": "U.S.",
        "page": "7",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 305",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "305",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "193 L. Ed. 2d 255",
        "volume": "193",
        "reporter": "L. Ed. 2d",
        "page": "255",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2015 U.S. LEXIS 7160",
        "volume": "2015",
        "reporter": "U.S. LEXIS",
        "page": "7160",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4003",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4003",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "25 Fla. L. Weekly Fed. S 555",
        "volume": "25",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "555",
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
      "id": "pin-12",
      "page": null,
      "quote": "--- # Mullenix v. Luna *577 U.S. 7 (2015)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A fleeing, reportedly intoxicated suspect, Israel Leija, led police on a high-speed chase and twice threatened by phone to shoot officers. As other officers set up spike strips beneath an overpass, Trooper Mullenix instead fired six rifle shots at Leija's car from the overpass, killing him. Leija's estate sued Mullenix under \u00a7 1983 for excessive force. ## Issue Whether Mullenix was entitled to qualified immunity \u2014 that is, whether the unlawfulness of his use of deadly force was clearly established at the time he acted. ## Rule Qualified immunity shields an official unless his conduct violated clearly established law, and that law must be identified with specificity, not at a high level of generality.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2015-11-09",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mullenix v. Luna",
    "varies_by_point": false,
    "scope_note": "Per curiam; good law on the specificity of 'clearly established' law for qualified immunity.",
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
        "journal_ref": "Mullenix v. Luna:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barton Ex Rel. Estate of Barton v. Taber",
          "cluster_id": 3198370,
          "cite": [
            "820 F.3d 958",
            "2016 WL 1658098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patrick Booker v. South Carolina Department of Corrections",
          "cluster_id": 4387227,
          "cite": [
            "855 F.3d 533",
            "2017 WL 1531576",
            "2017 U.S. App. LEXIS 7563"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tapanga Hardeman v. David Wathen",
          "cluster_id": 4647629,
          "cite": [
            "933 F.3d 816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ellen Keates v. Michael Koile",
          "cluster_id": 4474827,
          "cite": [
            "883 F.3d 1228"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kwame Ajamu v. City of Cleveland",
          "cluster_id": 4621394,
          "cite": [
            "925 F.3d 793"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rivas-Villegas v. Cortesluna",
          "cluster_id": 5290447,
          "cite": [
            "595 U.S. 1",
            "142 S. Ct. 4",
            "211 L. Ed. 2d 164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Barna v. Board of School Directors of the Panther Valley School District",
          "cluster_id": 4449477,
          "cite": [
            "877 F.3d 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Mack v. Warden Loretto FCI",
          "cluster_id": 4311322,
          "cite": [
            "839 F.3d 286",
            "2016 U.S. App. LEXIS 18336",
            "2016 WL 5899173"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Figueroa v. Mazza",
          "cluster_id": 3209159,
          "cite": [
            "825 F.3d 89",
            "2016 U.S. App. LEXIS 10152",
            "2016 WL 3126772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Reese, Jr. v. County of Sacramento",
          "cluster_id": 4489118,
          "cite": [
            "888 F.3d 1030"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fleet Hamby v. Steven Hammond",
          "cluster_id": 3199645,
          "cite": [
            "821 F.3d 1085",
            "2016 U.S. App. LEXIS 7894",
            "2016 WL 1730532"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shane Horton v. City of Santa Maria",
          "cluster_id": 4586718,
          "cite": [
            "915 F.3d 592"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
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
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shari Guertin v. State of Mich.",
          "cluster_id": 4578962,
          "cite": [
            "912 F.3d 907"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "A.M. Ex Rel. F.M. v. Holmes",
          "cluster_id": 4241340,
          "cite": [
            "830 F.3d 1123"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gutierrez v. Luna County",
          "cluster_id": 4321034,
          "cite": [
            "841 F.3d 895",
            "96 Fed. R. Serv. 3d 126",
            "2016 U.S. App. LEXIS 20466",
            "2016 WL 6694533"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Susan King v. Todd Harwood",
          "cluster_id": 4378482,
          "cite": [
            "852 F.3d 568",
            "2017 FED App. 0070P",
            "2017 WL 1130881",
            "2017 U.S. App. LEXIS 5264"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "E.W. v. Rosemary Dolgos",
          "cluster_id": 4467174,
          "cite": [
            "884 F.3d 172"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paige Ray-Cluney v. Charles Palmer",
          "cluster_id": 4542007,
          "cite": [
            "906 F.3d 540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "L.R. v. Philadelphia School District",
          "cluster_id": 4254183,
          "cite": [
            "836 F.3d 235",
            "2016 U.S. App. LEXIS 16344",
            "2016 WL 4608133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joan Kedra v. Richard Schroeter",
          "cluster_id": 4446761,
          "cite": [
            "876 F.3d 424"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Austin Gates v. Hassan Khokar",
          "cluster_id": 4476683,
          "cite": [
            "884 F.3d 1290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richard Vos v. City of Newport Beach",
          "cluster_id": 4506067,
          "cite": [
            "892 F.3d 1024"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
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
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
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
        "journal_ref": "Mullenix v. Luna:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(3153112 OR 9820073 OR 9820074) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjYxMTI2NDAwMDAwJnM9Nzg1ODUxOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%283153112+OR+9820073+OR+9820074%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(3153112 OR 9820073 OR 9820074)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzMmcz00NjU0MDk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%283153112+OR+9820073+OR+9820074%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(3153112 OR 9820073 OR 9820074)",
        "reviewed": 199,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 199,
        "triage_read": 1,
        "triage_snippet_classified": 198
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(3153112 OR 9820073 OR 9820074)",
    "indexed_citing_opinions": 756,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 3153112,
        "count": 324,
        "count_source": "search"
      },
      {
        "opinion_id": 9820073,
        "count": 437,
        "count_source": "search"
      },
      {
        "opinion_id": 9820074,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3491,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mullenix-v-luna.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzNTExNjUmcz0xMDU4NDk1MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%283153112+OR+9820073+OR+9820074%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 3153112,
        "cited_id": 64737,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 65421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 76270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 77858,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 121169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 145738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 172286,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 217703,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 223678,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 783116,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 792586,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 796504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3153112,
        "cited_id": 1189741,
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
    "date_created": "2026-07-05T14:46:44Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:46:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:46:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:49:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:46:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mullenix v. Luna

```
                 Cite as: 577 U. S. ____ (2015)           1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
   CHADRIN LEE MULLENIX v. BEATRICE LUNA, 

      INDIVIDUALLY AND AS REPRESENTATIVE OF THE

         ESTATE OF ISRAEL LEIJA, JR., ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT

            No. 14–1143. Decided November 9, 2015


   PER CURIAM.
   On the night of March 23, 2010, Sergeant Randy Baker
of the Tulia, Texas Police Department followed Israel
Leija, Jr., to a drive-in restaurant, with a warrant for his
arrest. 773 F. 3d 712, 715–716 (CA5 2014). When Baker
approached Leija’s car and informed him that he was
under arrest, Leija sped off, headed for Interstate 27.
2013 WL 4017124, *1 (ND Tex., Aug. 7, 2013). Baker gave
chase and was quickly joined by Trooper Gabriel Rodri-
guez of the Texas Department of Public Safety (DPS). 773
F. 3d, at 716.
   Leija entered the interstate and led the officers on an
18-minute chase at speeds between 85 and 110 miles per
hour. Ibid. Twice during the chase, Leija called the Tulia
Police dispatcher, claiming to have a gun and threatening
to shoot at police officers if they did not abandon their
pursuit. The dispatcher relayed Leija’s threats, together
with a report that Leija might be intoxicated, to all con-
cerned officers.
   As Baker and Rodriguez maintained their pursuit, other
law enforcement officers set up tire spikes at three loca-
tions. Officer Troy Ducheneaux of the Canyon Police
Department manned the spike strip at the first location
Leija was expected to reach, beneath the overpass at
Cemetery Road. Ducheneaux and the other officers had
received training on the deployment of spike strips, includ-
ing on how to take a defensive position so as to minimize
2                       MULLENIX v. LUNA

                             Per Curiam

the risk posed by the passing driver. Ibid.
  DPS Trooper Chadrin Mullenix also responded. He
drove to the Cemetery Road overpass, initially intending
to set up a spike strip there. Upon learning of the other
spike strip positions, however, Mullenix began to consider
another tactic: shooting at Leija’s car in order to disable it.
2013 WL 4017124, *1. Mullenix had not received training
in this tactic and had not attempted it before, but he
radioed the idea to Rodriguez. Rodriguez responded “10–
4,” gave Mullenix his position, and said that Leija had
slowed to 85 miles per hour. Mullenix then asked the DPS
dispatcher to inform his supervisor, Sergeant Byrd, of his
plan and ask if Byrd thought it was “worth doing.” 773
F. 3d, at 716–717. Before receiving Byrd’s response, Mul-
lenix exited his vehicle and, armed with his service rifle,
took a shooting position on the overpass, 20 feet above I–
27. Respondents allege that from this position, Mullenix
still could hear Byrd’s response to “stand by” and “see if
the spikes work first.” Ibid.*
  As Mullenix waited for Leija to arrive, he and another
officer, Randall County Sheriff ’s Deputy Tom Shipman,
discussed whether Mullenix’s plan would work and how
and where to shoot the vehicle to best carry it out. 2013
WL 4017124, *2. Shipman also informed Mullenix that
another officer was located beneath the overpass. 773
F. 3d, at 717.
  Approximately three minutes after Mullenix took up his
shooting position, he spotted Leija’s vehicle, with Rodri-
guez in pursuit. As Leija approached the overpass, Mul-
lenix fired six shots. Leija’s car continued forward be-
neath the overpass, where it engaged the spike strip, hit

——————
  * Although Mullenix disputes hearing Byrd’s response, we view the
facts in the light most favorable to respondents, who oppose Mullenix’s
motion for summary judgment. See Tolan v. Cotton, 572 U. S. ___, ___
(2014) ( per curiam) (slip op., at 1).
                 Cite as: 577 U. S. ____ (2015)           3

                          Per Curiam

the median, and rolled two and a half times. It was later
determined that Leija had been killed by Mullenix’s shots,
four of which struck his upper body. There was no evi-
dence that any of Mullenix’s shots hit the car’s radiator,
hood, or engine block. Id., at 716–717; 2013 WL 4017124,
*2–*3.
   Respondents sued Mullenix under Rev. Stat. §1979, 42
U. S. C. §1983, alleging that he had violated the Fourth
Amendment by using excessive force against Leija. Mul-
lenix moved for summary judgment on the ground of
qualified immunity, but the District Court denied his
motion, finding that “[t]here are genuine issues of fact as
to whether Trooper Mullenix acted recklessly, or acted as
a reasonable, trained peace officer would have acted in the
same or similar circumstances.” 2013 WL 4017124, *6.
   Mullenix appealed, and the Court of Appeals for the
Fifth Circuit affirmed. 765 F. 3d 531 (2014). The court
agreed with the District Court that the “immediacy of the
risk posed by Leija is a disputed fact that a reasonable
jury could find either in the plaintiffs’ favor or in the
officer’s favor, precluding us from concluding that Mul-
lenix acted objectively reasonably as a matter of law.” Id.,
at 538.
   Judge King dissented. She described the “ ‘fact issue’
referenced by the majority” as “simply a restatement of
the objective reasonableness test that applies to Fourth
Amendment excessive force claims,” which, she noted, the
Supreme Court has held “ ‘is a pure question of law.’ ” Id.,
at 544–545 (quoting Scott v. Harris, 550 U. S. 372, 381, n.
8 (2007)). Turning to that legal question, Judge King
concluded that Mullenix’s actions were objectively reason-
able. When Mullenix fired, she emphasized, he knew not
only that Leija had threatened to shoot the officers in-
volved in his pursuit, but also that Leija was seconds away
from encountering such an officer beneath the overpass.
Judge King also dismissed the notion that Mullenix should
4                   MULLENIX v. LUNA

                         Per Curiam

have given the spike strips a chance to work. She ex-
plained that because spike strips are often ineffective, and
because officers operating them are vulnerable to gunfire
from passing cars, Mullenix reasonably feared that the
officers manning them faced a significant risk of harm.
765 F. 3d, at 548–549.
   Mullenix sought rehearing en banc before the Fifth
Circuit, but the court denied his petition. Judge Jolly
dissented, joined by six other members of the court. Judge
King, who joined Judge Jolly’s dissent, also filed a sepa-
rate dissent of her own. 777 F. 3d 221 (2014) ( per curiam).
On the same day, however, the two members forming the
original panel’s majority withdrew their previous opinion
and substituted a new one. 773 F. 3d 712. The revised
opinion recognized that objective unreasonableness is a
question of law that can be resolved on summary judg-
ment—as Judge King had explained in her dissent—but
reaffirmed the denial of qualified immunity. Id., at 715,
718. The majority concluded that Mullenix’s actions were
objectively unreasonable because several of the factors
that had justified deadly force in previous cases were
absent here: There were no innocent bystanders, Leija’s
driving was relatively controlled, Mullenix had not first
given the spike strips a chance to work, and Mullenix’s
decision was not a split-second judgment. Id., at 720–724.
The court went on to conclude that Mullenix was not
entitled to qualified immunity because “the law was clearly
established such that a reasonable officer would have
known that the use of deadly force, absent a sufficiently
substantial and immediate threat, violated the Fourth
Amendment.” Id., at 725.
   We address only the qualified immunity question, not
whether there was a Fourth Amendment violation in the
first place, and now reverse.
   The doctrine of qualified immunity shields officials from
civil liability so long as their conduct “ ‘does not violate
                  Cite as: 577 U. S. ____ (2015)             5

                           Per Curiam

clearly established statutory or constitutional rights of
which a reasonable person would have known.’ ” Pearson
v. Callahan, 555 U. S. 223, 231 (2009) (quoting Harlow v.
Fitzgerald, 457 U. S. 800, 818 (1982)). A clearly estab-
lished right is one that is “sufficiently clear that every
reasonable official would have understood that what he is
doing violates that right.” Reichle v. Howards, 566 U. S.
___, ___ (2012) (slip op., at 5) (internal quotation marks
and alteration omitted). “We do not require a case directly
on point, but existing precedent must have placed the
statutory or constitutional question beyond debate.”
Ashcroft v. al-Kidd, 563 U. S. 731, 741 (2011). Put simply,
qualified immunity protects “all but the plainly incompe-
tent or those who knowingly violate the law.” Malley v.
Briggs, 475 U. S. 335, 341 (1986).
    “We have repeatedly told courts . . . not to define clearly
established law at a high level of generality.” al-Kidd,
supra, at 742. The dispositive question is “whether the
violative nature of particular conduct is clearly estab-
lished.” Ibid. (emphasis added). This inquiry “ ‘must be
undertaken in light of the specific context of the case, not
as a broad general proposition.’ ” Brosseau v. Haugen, 543
U. S. 194, 198 (2004) (per curiam) (quoting Saucier v.
Katz, 533 U. S. 194, 201 (2001)). Such specificity is espe-
cially important in the Fourth Amendment context, where
the Court has recognized that “[i]t is sometimes difficult
for an officer to determine how the relevant legal doctrine,
here excessive force, will apply to the factual situation the
officer confronts.” 533 U. S., at 205.
   In this case, the Fifth Circuit held that Mullenix violated
the clearly established rule that a police officer may not
“ ‘use deadly force against a fleeing felon who does not pose
a sufficient threat of harm to the officer or others.’ ” 773
F. 3d, at 725. Yet this Court has previously considered—
and rejected—almost that exact formulation of the quali-
fied immunity question in the Fourth Amendment context.
6                   MULLENIX v. LUNA

                         Per Curiam

In Brosseau, which also involved the shooting of a suspect
fleeing by car, the Ninth Circuit denied qualified immu-
nity on the ground that the officer had violated the clearly
established rule, set forth in Tennessee v. Garner, 471
U. S. 1 (1985), that “deadly force is only permissible where
the officer has probable cause to believe that the suspect
poses a threat of serious physical harm, either to the
officer or to others.” Haugen v. Brosseau, 339 F. 3d 857,
873 (CA9 2003) (internal quotation marks omitted). This
Court summarily reversed, holding that use of Gar-
ner’s “general” test for excessive force was “mistaken.”
Brosseau, 543 U. S., at 199. The correct inquiry, the Court
explained, was whether it was clearly established that the
Fourth Amendment prohibited the officer’s conduct in the
“ ‘situation [she] confronted’: whether to shoot a disturbed
felon, set on avoiding capture through vehicular flight,
when persons in the immediate area are at risk from that
flight.” Id., at 199–200. The Court considered three court
of appeals cases discussed by the parties, noted that “this
area is one in which the result depends very much on the
facts of each case,” and concluded that the officer was
entitled to qualified immunity because “[n]one of [the
cases] squarely governs the case here.” Id., at 201 (em-
phasis added).
    Anderson v. Creighton, 483 U. S. 635 (1987), is also
instructive on the required degree of specificity. There,
the lower court had denied qualified immunity based on
the clearly established “right to be free from warrantless
searches of one’s home unless the searching officers have
probable cause and there are exigent circumstances.” Id.,
at 640. This Court faulted that formulation for failing to
address the actual question at issue: whether “the circum-
stances with which Anderson was confronted . . . consti-
tute[d] probable cause and exigent circumstances.” Id., at
640–641. Without answering that question, the Court
explained, the conclusion that Anderson’s search was
                 Cite as: 577 U. S. ____ (2015)           7

                          Per Curiam

objectively unreasonable did not “follow immediately”
from—and thus was not clearly established by—the prin-
ciple that warrantless searches not supported by probable
cause and exigent circumstances violate the Fourth
Amendment. Id., at 641.
   In this case, Mullenix confronted a reportedly intoxi-
cated fugitive, set on avoiding capture through high-speed
vehicular flight, who twice during his flight had threat-
ened to shoot police officers, and who was moments away
from encountering an officer at Cemetery Road. The
relevant inquiry is whether existing precedent placed the
conclusion that Mullenix acted unreasonably in these
circumstances “beyond debate.” al-Kidd, supra, at 741.
The general principle that deadly force requires a suffi-
cient threat hardly settles this matter. See Pasco v.
Knoblauch, 566 F. 3d 572, 580 (CA5 2009) (“[I]t would be
unreasonable to expect a police officer to make the numer-
ous legal conclusions necessary to apply Garner to a high-
speed car chase . . .”).
   Far from clarifying the issue, excessive force cases in-
volving car chases reveal the hazy legal backdrop against
which Mullenix acted. In Brosseau itself, the Court held
that an officer did not violate clearly established law when
she shot a fleeing suspect out of fear that he endangered
“other officers on foot who [she] believed were in the im-
mediate area,” “the occupied vehicles in [his] path,” and
“any other citizens who might be in the area.” 543 U. S.,
at 197 (first alteration in original; internal quotation
marks omitted; emphasis added). The threat Leija posed
was at least as immediate as that presented by a suspect
who had just begun to drive off and was headed only in the
general direction of officers and bystanders. Id., at 196–
197. By the time Mullenix fired, Leija had led police on a
25-mile chase at extremely high speeds, was reportedly
intoxicated, had twice threatened to shoot officers, and
was racing towards an officer’s location.
8                    MULLENIX v. LUNA

                         Per Curiam

   This Court has considered excessive force claims in
connection with high-speed chases on only two occasions
since Brosseau. In Scott v. Harris, 550 U. S. 372, the
Court held that an officer did not violate the Fourth
Amendment by ramming the car of a fugitive whose reck-
less driving “posed an actual and imminent threat to the
lives of any pedestrians who might have been present, to
other civilian motorists, and to the officers involved in the
chase.” Id., at 384. And in Plumhoff v. Rickard, 572 U. S.
___ (2014), the Court reaffirmed Scott by holding that an
officer acted reasonably when he fatally shot a fugitive
who was “intent on resuming” a chase that “pose[d] a
deadly threat for others on the road.” 572 U. S., at ___
(slip op., at 10). The Court has thus never found the use of
deadly force in connection with a dangerous car chase to
violate the Fourth Amendment, let alone to be a basis for
denying qualified immunity. Leija in his flight did not
pass as many cars as the drivers in Scott or Plumhoff;
traffic was light on I–27. At the same time, the fleeing
fugitives in Scott and Plumhoff had not verbally threat-
ened to kill any officers in their path, nor were they about
to come upon such officers. In any event, none of our
precedents “squarely governs” the facts here. Given Lei-
ja’s conduct, we cannot say that only someone “plainly
incompetent” or who “knowingly violate[s] the law” would
have perceived a sufficient threat and acted as Mullenix
did. Malley, 475 U. S., at 341.
   The dissent focuses on the availability of spike strips as
an alternative means of terminating the chase. It argues
that even if Leija posed a threat sufficient to justify deadly
force in some circumstances, Mullenix nevertheless con-
travened clearly established law because he did not wait
to see if the spike strips would work before taking action.
Spike strips, however, present dangers of their own, not
only to drivers who encounter them at speeds between 85
and 110 miles per hour, but also to officers manning them.
                 Cite as: 577 U. S. ____ (2015)            9

                          Per Curiam

See, e.g., Thompson v. Mercer, 762 F. 3d 433, 440 (CA5
2014); Brief for National Association of Police Organiza-
tions et al. as Amici Curiae 15–16. Nor are spike strips
always successful in ending the chase. See, e.g., Cordova
v. Aragon, 569 F. 3d 1183, 1186 (CA10 2009); Brief for
National Association of Police Organizations et al. as
Amici Curiae 16 (citing examples). The dissent can cite no
case from this Court denying qualified immunity because
officers entitled to terminate a high-speed chase selected
one dangerous alternative over another.
   Even so, the dissent argues, there was no governmental
interest that justified acting before Leija’s car hit the
spikes. Mullenix explained, however, that he feared Leija
might attempt to shoot at or run over the officers manning
the spike strips. Mullenix also feared that even if Leija hit
the spike strips, he might still be able to continue driving
in the direction of other officers. The dissent ignores these
interests by suggesting that there was no “possible mar-
ginal gain in shooting at the car over using the spike
strips already in place.” Post, at 4 (opinion of SOTOMAYOR,
J.). In fact, Mullenix hoped his actions would stop the car
in a manner that avoided the risks to other officers and
other drivers that relying on spike strips would entail.
The dissent disputes the merits of the options available to
Mullenix, post, at 3–4, but others with more experience
analyze the issues differently. See, e.g., Brief for National
Association of Police Organizations et al. as Amici Curiae
15–16. Ultimately, whatever can be said of the wisdom of
Mullenix’s choice, this Court’s precedents do not place the
conclusion that he acted unreasonably in these circum-
stances “beyond debate.” al-Kidd, 563 U. S., at 741.
   More fundamentally, the dissent repeats the Fifth Cir-
cuit’s error. It defines the qualified immunity inquiry at a
high level of generality—whether any governmental inter-
est justified choosing one tactic over another—and then
fails to consider that question in “the specific context of
10                  MULLENIX v. LUNA

                         Per Curiam

the case.” Brosseau v. Haugen, 543 U. S., at 198 (internal
quotation marks omitted). As in Anderson, the conclusion
that Mullenix’s reasons were insufficient to justify his
actions simply does not “follow immediately” from the
general proposition that force must be justified. 483 U. S.,
at 641.
   Cases decided by the lower courts since Brosseau like-
wise have not clearly established that deadly force is
inappropriate in response to conduct like Leija’s. The
Fifth Circuit here principally relied on its own decision in
Lytle v. Bexar County, 560 F. 3d 404 (2009), denying quali-
fied immunity to a police officer who had fired at a fleeing
car and killed one of its passengers. That holding turned
on the court’s assumption, for purposes of summary judg-
ment, that the car was moving away from the officer and
had already traveled some distance at the moment the
officer fired. See id., at 409. The court held that a rea-
sonable jury could conclude that a receding car “did not
pose a sufficient threat of harm such that the use of deadly
force was reasonable.” Id., at 416. But, crucially, the
court also recognized that if the facts were as the officer
alleged, and he fired as the car was coming towards him,
“he would likely be entitled to qualified immunity” based
on the “threat of immediate and severe physical harm.”
Id., at 412. Without implying that Lytle was either correct
or incorrect, it suffices to say that Lytle does not clearly
dictate the conclusion that Mullenix was unjustified in
perceiving grave danger and responding accordingly, given
that Leija was speeding towards a confrontation with
officers he had threatened to kill.
   Cases that the Fifth Circuit ignored also suggest that
Mullenix’s assessment of the threat Leija posed was rea-
sonable. In Long v. Slaton, 508 F. 3d 576 (2007), for ex-
ample, the Eleventh Circuit held that a sheriff ’s deputy
did not violate the Fourth Amendment by fatally shooting
a mentally unstable individual who was attempting to flee
                 Cite as: 577 U. S. ____ (2015)          11

                          Per Curiam

in the deputy’s car, even though at the time of the shoot-
ing the individual had not yet operated the cruiser dan-
gerously. The court explained that “the law does not
require officers in a tense and dangerous situation to wait
until the moment a suspect uses a deadly weapon to act to
stop the suspect” and concluded that the deputy had rea-
son to believe Long was dangerous based on his unstable
state of mind, theft of the cruiser, and failure to heed the
deputy’s warning to stop. Id., at 581–582. The court also
rejected the notion that the deputy should have first tried
less lethal methods, such as spike strips. “[C]onsidering
the unpredictability of Long’s behavior and his fleeing in a
marked police cruiser,” the court held, “we think the police
need not have taken that chance and hoped for the best.”
Id., at 583 (alteration and internal quotation marks omit-
ted). But see Smith v. Cupp, 430 F. 3d 766, 774–777 (CA6
2005) (denying qualified immunity to an officer who shot
an intoxicated suspect who had stolen the officer’s cruiser
where a reasonable jury could have concluded that the
suspect’s flight did not immediately threaten the officer or
any other bystander).
   Other cases cited by the Fifth Circuit and respondents
are simply too factually distinct to speak clearly to the
specific circumstances here. Several involve suspects who
may have done little more than flee at relatively low
speeds. See, e.g., Walker v. Davis, 649 F. 3d 502, 503 (CA6
2011); Kirby v. Duva, 530 F. 3d 475, 479–480 (CA6 2008);
Adams v. Speers, 473 F. 3d 989, 991 (CA9 2007); Vaughan
v. Cox, 343 F. 3d 1323, 1330–1331, and n. 7 (CA11 2003).
These cases shed little light on whether the far greater
danger of a speeding fugitive threatening to kill police
officers waiting in his path could warrant deadly force.
The court below noted that “no weapon was ever seen,”
773 F. 3d, at 723, but surely in these circumstances the
police were justified in taking Leija at his word when he
twice told the dispatcher he had a gun and was prepared
12                   MULLENIX v. LUNA

                          Per Curiam

to use it.
  Finally, respondents argue that the danger Leija repre-
sented was less substantial than the threats that courts
have found sufficient to justify deadly force. But the mere
fact that courts have approved deadly force in more ex-
treme circumstances says little, if anything, about whether
such force was reasonable in the circumstances here.
The fact is that when Mullenix fired, he reasonably under-
stood Leija to be a fugitive fleeing arrest, at speeds over
100 miles per hour, who was armed and possibly intoxi-
cated, who had threatened to kill any officer he saw if the
police did not abandon their pursuit, and who was racing
towards Officer Ducheneaux’s position. Even accepting
that these circumstances fall somewhere between the two
sets of cases respondents discuss, qualified immunity
protects actions in the “ ‘hazy border between excessive
and acceptable force.’ ” Brosseau, supra, at 201 (quoting
Saucier, 533 U. S., at 206; some internal quotation marks
omitted).
  Because the constitutional rule applied by the Fifth
Circuit was not “ ‘beyond debate,’ ” Stanton v. Sims, 571
U. S. ___, ___ (2013) (per curiam) (slip op., at 8), we grant
Mullenix’s petition for certiorari and reverse the Fifth
Circuit’s determination that Mullenix is not entitled to
qualified immunity.
                                              It is so ordered.
                  Cite as: 577 U. S. ____ (2015)             1

                SCALIA, J., concurring in judgment

SUPREME COURT OF THE UNITED STATES
    CHADRIN LEE MULLENIX v. BEATRICE LUNA, 

      INDIVIDUALLY AND AS REPRESENTATIVE OF THE

         ESTATE OF ISRAEL LEIJA, JR., ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT

             No. 14–1143. Decided November 9, 2015


   JUSTICE SCALIA, concurring in the judgment.
   I join the judgment of the Court, but would not describe
what occurred here as the application of deadly force in
effecting an arrest. Our prior cases have reserved that
description to the directing of force sufficient to kill at the
person of the desired arrestee. See, e.g., Plumhoff v. Rick-
ard, 572 U. S. ___ (2014); Brosseau v. Haugen, 543 U. S.
194 (2004) (per curiam); Tennessee v. Garner, 471 U. S. 1
(1985). It does not assist analysis to refer to all use of
force that happens to kill the arrestee as the application of
deadly force. The police might, for example, attempt to
stop a fleeing felon’s car by felling a large tree across the
road; if they drop the tree too late, so that it crushes the
car and its occupant, I would not call that the application
of deadly force. Though it was force sufficient to kill, it
was not applied with the object of harming the body of the
felon.
   Thus, in Scott v. Harris, 550 U. S. 372 (2007), we de-
clined to characterize officer Scott’s use of his pursuing
vehicle’s bumper to push the fleeing vehicle off the road as
the application of deadly force. Whether or not it was
that, we said, “all that matters is whether Scott’s actions
were reasonable.” Id., at 383. So also here. But it stacks
the deck against the officer, it seems to me, to describe his
action as the application of deadly force.
   It was at least arguable in Scott that pushing a speeding
vehicle off the road is targeting its occupant for injury or
2                    MULLENIX v. LUNA

               SCALIA, J., concurring in judgment

death. Here, however, it is conceded that Trooper Mul-
lenix did not shoot to wound or kill the fleeing Leija, nor
even to drive Leija’s car off the road, but only to cause the
car to stop by destroying its engine. That was a risky
enterprise, as the outcome demonstrated; but determining
whether it violated the Fourth Amendment requires us to
ask, not whether it was reasonable to kill Leija, but
whether it was reasonable to shoot at the engine in light of
the risk to Leija. It distorts that inquiry, I think, to make
the question whether it was reasonable for Mullenix to
“apply deadly force.”
                 Cite as: 577 U. S. ____ (2015)            1

                   SOTOMAYOR, J., dissenting

SUPREME COURT OF THE UNITED STATES
   CHADRIN LEE MULLENIX v. BEATRICE LUNA, 

      INDIVIDUALLY AND AS REPRESENTATIVE OF THE

         ESTATE OF ISRAEL LEIJA, JR., ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE FIFTH CIRCUIT

            No. 14–1143. Decided November 9, 2015


   JUSTICE SOTOMAYOR, dissenting.
   Chadrin Mullenix fired six rounds in the dark at a car
traveling 85 miles per hour. He did so without any train-
ing in that tactic, against the wait order of his superior
officer, and less than a second before the car hit spike
strips deployed to stop it. Mullenix’s rogue conduct killed
the driver, Israel Leija, Jr. Because it was clearly estab-
lished under the Fourth Amendment that an officer in
Mullenix’s position should not have fired the shots, I
respectfully dissent from the grant of summary reversal.
                              I
   Resolving all factual disputes in favor of plaintiffs, as
the Court must on a motion for summary judgment, Mul-
lenix knew the following facts before he shot at Leija’s
engine block: Leija had led police officers on an 18-minute
car chase, at speeds ranging from 85 to 110 miles per
hour. 773 F. 3d 712, 716 (CA5 2014). Leija had twice
called the police dispatcher threatening to shoot at officers
if they did not cease the pursuit. Ibid. Police officers were
deploying three sets of spike strips in order to stop Leija’s
flight. Ibid. The officers were trained to stop a car using
spike strips. This training included how to take a defen-
sive position to minimize the risk of danger from the tar-
get car. Ibid. Mullenix knew that spike strips were being
set up directly beneath the overpass where he was sta-
tioned. Id., at 723. There is no evidence below that any of
2                    MULLENIX v. LUNA

                   SOTOMAYOR, J., dissenting

the officers with whom Mullenix was in communication—
including Officer Troy Ducheneaux, whom Mullenix be-
lieved to be below the overpass—had expressed any con-
cern for their safety. Id., at 720.
   Mullenix had no training in shooting to disable a mov-
ing vehicle and had never seen the tactic done before. Id.,
at 716. He also lacked permission to take the shots: When
Mullenix relayed his plan to his superior officer, Robert
Byrd, Byrd responded “stand by” and “see if the spikes
work first.” Id., at 716–717. Three minutes after arriving
at the overpass, Mullenix fired six rounds at Leija’s car.
None hit the car’s engine block; at least four struck Leija
in the upper body, killing Leija. Id., at 717.
                              II
   When confronting a claim of qualified immunity, a court
asks two questions. First, the court considers whether the
officer in fact violated a constitutional right. Saucier v.
Katz, 533 U. S. 194, 201 (2001). Second, the court asks
whether the contours of the right were “sufficiently clear
that a reasonable official would [have understood] that
what he is doing violates that right.” Id., at 202 (quoting
Anderson v. Creighton, 483 U. S. 635, 640 (1987)). This
Court has rejected the idea that “an official action is pro-
tected by qualified immunity unless the very action in
question has previously been held unlawful.” Id., at 640.
Instead, the crux of the qualified immunity test is whether
officers have “fair notice” that they are acting unconstitu-
tionally. Hope v. Pelzer, 536 U. S. 730, 739 (2002).
   Respondents here allege that Mullenix violated the
Fourth Amendment’s prohibition on unreasonable seizures
by using deadly force to apprehend Leija. This Court’s
precedents clearly establish that the Fourth Amendment
is violated unless the “ ‘governmental interests’ ” in effec-
tuating a particular kind of seizure outweigh the “ ‘nature
and quality of the intrusion on the individual’s Fourth
                 Cite as: 577 U. S. ____ (2015)            3

                   SOTOMAYOR, J., dissenting

Amendment interests.’ ” Scott v. Harris, 550 U. S. 372,
383 (2007) (quoting United States v. Place, 462 U. S. 696,
703 (1983)). There must be a “governmental interes[t]”
not only in effectuating a seizure, but also in “how [the
seizure] is carried out.” Tennessee v. Garner, 471 U. S. 1, 8
(1985).
   Balancing a particular governmental interest in the use
of deadly force against the intrusion occasioned by the use
of that force is inherently a fact-specific inquiry, not sus-
ceptible to bright lines. But it is clearly established that
the government must have some interest in using deadly
force over other kinds of force.
   Here, then, the clearly established legal question—the
question a reasonable officer would have asked—is whether,
under all the circumstances as known to Mullenix, there
was a governmental interest in shooting at the car rather
than waiting for it to run over spike strips.
   The majority does not point to any such interest here. It
claims that Mullenix’s goal was not merely to stop the car,
but to stop the car “in a manner that avoided the risks” of
relying on spike strips. Ante, at 9. But there is no evi-
dence in the record that shooting at Leija’s engine block
would stop the car in such a manner.
   The majority first suggests that Mullenix did not wait
for the results of the spikes, as his superior advised, be-
cause of his concern for the officers manning the strips.
But Leija was going to come upon those officers whether or
not Mullenix’s shooting tactic was successful: Mullenix
took his shot when Leija was between 25 and 30 yards
away from the spike strip, traveling at 85 miles per hour.
Even if his shots hit Leija’s engine block, the car would not
have stopped instantly. Mullenix would have bought the
officers he was trying to protect—officers who had been
trained to take defensive positions—less than three-
quarters of a second over waiting for the spike strips. And
whatever threat Leija posed after his car was stopped
4                     MULLENIX v. LUNA

                    SOTOMAYOR, J., dissenting

existed whether the car was stopped by a shot to the en-
gine block or by the spike strips.
   Nor was there any evidence that shooting at the car was
more reliable than the spike strips. The majority notes
that spike strips are fallible. Ante, at 8–9. But Mullenix
had no information to suggest that shooting to disable a
car had a higher success rate, much less that doing so with
no training and at night was more likely to succeed.
Moreover, not only did officers have training in setting up
the spike strips, but they had also placed two backup
strips further north along the highway in case the first set
failed. A reasonable officer could not have thought that
shooting would stop the car with less danger or greater
certainty than waiting.
   The majority cites Long v. Slaton, 508 F. 3d 576 (CA11
2007), for the proposition that Mullenix need not have
“first tried less lethal methods, such as spike strips.”
Ante, at 11. But in that case, there was a clear reason to
prefer deadly force over the alternatives. In Long, an
officer fired to stop a suspect from fleeing in a stolen police
cruiser. 508 F. 3d, at 583. When the officer fired, there
were no alternative means of stopping the car in place.
The Eleventh Circuit held that the governmental interest
against waiting for a future deployment of spike strips
that may never materialize justified the use of deadly
force. Ibid.
   In this case, by contrast, neither petitioner nor the
majority can point to any possible marginal gain in shoot-
ing at the car over using the spike strips already in place.
It is clearly established that there must be some govern-
mental interest that necessitates deadly force, even if it is
not always clearly established what level of governmental
interest is sufficient.
   Under the circumstances known to him at the time,
Mullenix puts forth no plausible reason to choose shooting
at Leija’s engine block over waiting for the results of the
                     Cite as: 577 U. S. ____ (2015)                   5

                      SOTOMAYOR, J., dissenting

spike strips. I would thus hold that Mullenix violated
Leija’s clearly established right to be free of intrusion
absent some governmental interest.
                              III
   The majority largely evades this key legal question by
focusing primarily on the governmental interest in whether
the car should be stopped rather than the dispositive ques-
tion of how the car should be stopped. But even assum-
ing that Leija posed a “sufficient,” ante, at 8, or “imme-
diate,” ante, at 7, threat, Mullenix did not face a “choice
between two evils” of shooting at a suspect’s car or
letting him go. Scott, 550 U. S., at 384; see, e.g., Plumhoff
v. Rickard, 572 U. S. ___, ___ (2014) (slip op., at 3, 10);
Brosseau v. Haugen, 543 U. S. 194, 196–197 (2004). In-
stead, Mullenix chose to employ a potentially lethal tactic
(shooting at Leija’s engine block) in addition to a tactic
specifically designed to accomplish the same result (spike
strips).* By granting Mullenix qualified immunity, this
Court goes a step further than our previous cases and does
so without full briefing or argument.
   Thus framed, it is apparent that the majority’s exhorta-
tion that the right at stake not be defined at “a high level
of generality,” see ante, at 9, is a red herring. The major-
ity adduces various facts that the Fifth Circuit supposedly
ignored in its qualified immunity analysis, including that
——————
  * The majority describes the choice between spike strips and shooting
as the choice between “one dangerous alternative” and another, noting
that spike strips can pose a danger to drivers that encounter them.
Ante, at 8–9. But Mullenix could not have thought that awaiting the
spikes was anywhere near as dangerous as shooting immediately before
Leija hit the spikes. For one thing, Mullenix had no training in shoot-
ing to disable the vehicle and so no idea of the relative danger that
shooting posed to a driver. For another, Leija would be subjected to the
danger posed by the spike strips whether Mullenix shot or not. And, in
fact, that is what happened: Leija’s car hit the spike strips and then
rolled two and a half times.
6                    MULLENIX v. LUNA

                   SOTOMAYOR, J., dissenting

Leija was “a reportedly intoxicated fugitive, set on avoid-
ing capture through high-speed vehicular flight, who twice
during his flight had threatened to shoot police officers,
and who was moments away from encountering an officer
at Cemetery Road.” Ante, at 7. But not one of those facts
goes to the governmental interest in shooting over await-
ing the spike strips. The majority also claims that estab-
lished law does not make clear that “Mullenix’s reasons
were insufficient to justify” his choice of shooting over
following his superior’s orders to wait for the spikes. Ante,
at 9–10. But Mullenix seemed to have no reasons to prefer
shooting to following orders.
   Instead of dealing with the question whether Mullenix
could constitutionally fire on Leija’s car rather than wait-
ing for the spike strips, the majority dwells on the immi-
nence of the threat posed by Leija. The majority recharac-
terizes Mullenix’s decision to shoot at Leija’s engine block
as a split-second, heat-of-the-moment choice, made when
the suspect was “moments away.” Ante, at 7. Indeed,
reading the majority opinion, one would scarcely believe
that Mullenix arrived at the overpass several minutes
before he took his shot, or that the rural road where the
car chase occurred had few cars and no bystanders or
businesses. 773 F. 3d, at 717, 720. The majority also
glosses over the facts that Mullenix had time to ask Byrd
for permission to fire upon Leija and that Byrd—
Mullenix’s superior officer—told Mullenix to “stand by.”
Id., at 717. There was no reason to believe that Byrd did
not have all the same information Mullenix did, including
the knowledge that an officer was stationed beneath the
overpass. Even after receiving Byrd’s response, Mullenix
spent minutes in shooting position discussing his next step
with a fellow officer, minutes during which he received no
information that would have made his plan more suitable
or his superior’s orders less so. Ibid.
   An appropriate reading of the record on summary judg-
                  Cite as: 577 U. S. ____ (2015)             7

                    SOTOMAYOR, J., dissenting

ment would thus render Mullenix’s choice even more
unreasonable. And asking the appropriate legal question
would leave the majority with no choice but to conclude
that Mullenix ignored the longstanding and well-settled
Fourth Amendment rule that there must be a governmen-
tal interest not just in seizing a suspect, but in the level of
force used to effectuate that seizure.
                          *    *      *
  When Mullenix confronted his superior officer after the
shooting, his first words were, “How’s that for proactive?”
Ibid. (Mullenix was apparently referencing an earlier
counseling session in which Byrd suggested that he was
not enterprising enough. Ibid.) The glib comment does
not impact our legal analysis; an officer’s actual intentions
are irrelevant to the Fourth Amendment’s “objectively
reasonable” inquiry. See Graham v. Connor, 490 U. S.
386, 397 (1989). But the comment seems to me revealing
of the culture this Court’s decision supports when it calls
it reasonable—or even reasonably reasonable—to use
deadly force for no discernible gain and over a supervisor’s
express order to “stand by.” By sanctioning a “shoot first,
think later” approach to policing, the Court renders the
protections of the Fourth Amendment hollow.
  For the reasons discussed, I would deny Mullenix’s
petition for a writ of certiorari. I thus respectfully dissent.

```

---

## GROUP: content/cases/Murray v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Murray v. United States"
type: case
citation: "487 U.S. 533 (1988)"
parallel_cite: "108 S. Ct. 2529; 101 L. Ed. 2d 472; 56 U.S.L.W. 4801"
neutral_cite: 1988 U.S. LEXIS 2881
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-06-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Murray v. United States
  varies_by_point: false
  scope_note: "Extends the independent-source doctrine to re-seizure under a later warrant; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112136/murray-v-united-states/"
  cluster_id: 112136
  opinion_id: 9431434
  identity_checked: true
homes:
  - page: "[[Inevitable Discovery & Independent Source]]"
    role: "Key — Progeny / Refinement"
related: ["[[Nix v. Williams]]", "[[Silverthorne Lumber Co. v. United States]]", "[[Segura v. United States]]", "[[Wong Sun v. United States]]"]
aliases: []
tags: ["case", "exclusionary-rule", "independent-source", "fruit-of-the-poisonous-tree"]
holding: "Independent source: evidence first observed during an unlawful entry is admissible if later acquired through a genuinely independent…"
lake:
  record_id: Murray v. United States
  status: verified
  projected_at: 2026-07-06
---

# Murray v. United States

*487 U.S. 533 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Federal agents, suspecting drug trafficking, illegally entered a warehouse without a warrant and saw bales of marijuana. They left without disturbing the bales, then obtained a search warrant based on information they had known before the illegal entry — without mentioning the entry or what they had seen — and re-entered to seize the marijuana under the warrant.

## Issue
Whether the independent-source doctrine permits admission of evidence that was first observed during an unlawful entry but later seized under a warrant obtained from genuinely independent information.

## Rule
Yes — so long as the later acquisition is genuinely independent of the unlawful entry. "The ultimate question, therefore, is whether the search pursuant to warrant was in fact a genuinely independent source of the information and tangible evidence at issue here." — 487 U.S. at 542. ^pin-542

The later seizure is **not** genuinely independent if "the agents' decision to seek the warrant was prompted by what they had seen during the initial entry, . . . or if information obtained during that entry was presented to the Magistrate and affected his decision to issue the warrant." — *Id.* ^pin-542b

## Application
The marijuana would be admissible only if the agents' decision to seek the warrant had not been prompted by what they saw during the illegal entry and if no information from that entry had been presented to the magistrate. Because the lower courts had not made an explicit finding on whether the warrant application was truly independent of the illegal entry, the Court [[Reading and Citing Cases#vacated|vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for that determination.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]] for a finding on whether the warrant was a genuinely [[Inevitable Discovery and Independent Source|independent source]] of the seized evidence.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Murray* extends the independent-source doctrine (rooted in [[Silverthorne Lumber Co. v. United States]] and restated in [[Nix v. Williams]]) to evidence first seen during an illegal entry and later seized under a genuinely independent warrant.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Murray v. United States*, 487 U.S. 533 (1988) — https://www.courtlistener.com/opinion/112136/murray-v-united-states/ — pinpoint: 542.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "537dff1b577e41bb", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "487 U.S. 533 (1988)", "court": "U.S. Supreme Court", "neutral_cite": "1988 U.S. LEXIS 2881", "official_citation_present": true, "parallel_cite": "108 S. Ct. 2529; 101 L. Ed. 2d 472; 56 U.S.L.W. 4801", "title": "Murray v. United States", "year": "1988"}}
{"assertion_id": "683488d46d17a8cd", "dimension": "support", "kind": "home_role", "locator": {"home": "Inevitable Discovery & Independent Source"}, "payload": {"home": "Inevitable Discovery & Independent Source", "role": "Key — Progeny / Refinement", "title": "Murray v. United States"}}
{"assertion_id": "95099582c1f466ca", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Independent source: evidence first observed during an unlawful entry is admissible if later acquired through a genuinely independent…", "title": "Murray v. United States"}}
{"assertion_id": "48f564dd5ee0d367", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Murray v. United States"}}
{"assertion_id": "d8661dd90f7b59a1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1988-06-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Murray v. United States", "field_i_validity": "good_law", "scope_note": "Extends the independent-source doctrine to re-seizure under a later warrant; good law.", "title": "Murray v. United States", "varies_by_point": "false"}}
```

### lake record — Murray v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Murray v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Murray v. United States",
    "case_name_short": "Murray",
    "case_name_full": "Murray v. United States",
    "input_case_name": "Murray v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-27",
    "year": 1988,
    "docket": null,
    "cluster_id": 112136,
    "lead_opinion_id": 9431434,
    "sibling_ids": [
      112136,
      9431434,
      9431435,
      9431436
    ],
    "absolute_url": "/opinion/112136/murray-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9075667,
        "score": 20,
        "case_name": "Murray v. United States"
      },
      {
        "cluster_id": 9075666,
        "score": 20,
        "case_name": "Murray v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "487 U.S. 533",
      "volume": "487",
      "reporter": "U.S.",
      "page": "533",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 2529",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2529",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 L. Ed. 2d 472",
        "volume": "101",
        "reporter": "L. Ed. 2d",
        "page": "472",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4801",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4801",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2881",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2881",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "487 U.S. 533",
        "volume": "487",
        "reporter": "U.S.",
        "page": "533",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 2529",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2529",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 L. Ed. 2d 472",
        "volume": "101",
        "reporter": "L. Ed. 2d",
        "page": "472",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2881",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2881",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4801",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4801",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "487 U.S. 533",
    "official_selection": {
      "court_class": "scotus",
      "selected": "487 U.S. 533",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-542",
      "page": null,
      "quote": "--- # Murray v. United States *487 U.S. 533 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Federal agents, suspecting drug trafficking, illegally entered a warehouse without a warrant and saw bales of marijuana. They left without disturbing the bales, then obtained a search warrant based on information they had known before the illegal entry \u2014 without mentioning the entry or what they had seen \u2014 and re-entered to seize the marijuana under the warrant. ## Issue Whether the independent-source doctrine permits admission of evidence that was first observed during an unlawful entry but later seized under a warrant obtained from genuinely independent information. ## Rule Yes \u2014 so long as the later acquisition is genuinely independent of the unlawful entry.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-542b",
      "page": null,
      "quote": "the agents' decision to seek the warrant was prompted by what they had seen during the initial entry, . . . or if information obtained during that entry was presented to the Magistrate and affected his decision to issue the warrant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Murray v. United States",
    "varies_by_point": false,
    "scope_note": "Extends the independent-source doctrine to re-seizure under a later warrant; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Serrano (A173250)",
          "cluster_id": 10135658,
          "cite": [
            "324 Or. App. 453",
            "527 P.3d 54"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tardie",
          "cluster_id": 10135114,
          "cite": [
            "319 Or. App. 229",
            "509 P.3d 705"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Wilson",
          "cluster_id": 4834605,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Pearson",
          "cluster_id": 4673683,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pamela Golinveaux v. United States",
          "cluster_id": 4589293,
          "cite": [
            "915 F.3d 564"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Charles E. Blake v. State of Mississippi",
          "cluster_id": 4541114,
          "cite": [
            "256 So. 3d 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
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
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rose",
          "cluster_id": 2961060,
          "cite": [
            "802 F.3d 114",
            "2015 U.S. App. LEXIS 16658",
            "2015 WL 5474267"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4288590,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4287047,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rivas, Gerardo Tomas",
          "cluster_id": 4286131,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "STATE of Minnesota, Respondent, v. Kyle Dean McCLAIN, Appellant",
          "cluster_id": 2798238,
          "cite": [
            "862 N.W.2d 717"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Haynes",
          "cluster_id": 2795871,
          "cite": [
            "116 A.3d 640",
            "2015 Pa. Super. 94",
            "2015 Pa. Super. LEXIS 207",
            "2015 WL 1814017"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Hill",
          "cluster_id": 2769569,
          "cite": [
            "776 F.3d 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph White",
          "cluster_id": 2669804,
          "cite": [
            "748 F.3d 507",
            "2014 WL 1408748",
            "2014 U.S. App. LEXIS 6849"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heck v. Humphrey",
          "cluster_id": 117864,
          "cite": [
            "129 L. Ed. 2d 383",
            "114 S. Ct. 2364",
            "512 U.S. 477",
            "1994 U.S. LEXIS 4824"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Dominguez-Castor",
          "cluster_id": 4691722,
          "cite": [
            "2020 COA 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
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
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Harris",
          "cluster_id": 112413,
          "cite": [
            "109 L. Ed. 2d 13",
            "110 S. Ct. 1640",
            "495 U.S. 14",
            "1990 U.S. LEXIS 2037",
            "58 U.S.L.W. 4457"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
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
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ove v. Gwinn",
          "cluster_id": 7099348,
          "cite": [
            "264 F.3d 817",
            "2001 WL 1002190"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Thompson",
          "cluster_id": 4858089,
          "cite": [
            "2021 CO 15"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
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
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin Davis (03-1451) and Keith Presley (03-1621)",
          "cluster_id": 792556,
          "cite": [
            "430 F.3d 345",
            "2005 U.S. App. LEXIS 25124",
            "2005 WL 3108503"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zapata",
          "cluster_id": 195255,
          "cite": [
            "18 F.3d 971",
            "1994 WL 86216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stabile",
          "cluster_id": 183984,
          "cite": [
            "633 F.3d 219",
            "2011 U.S. App. LEXIS 1945",
            "2011 WL 294036"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daugherty",
          "cluster_id": 1777786,
          "cite": [
            "931 S.W.2d 268",
            "1996 Tex. Crim. App. LEXIS 88",
            "1996 WL 350804"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Runyan",
          "cluster_id": 27212,
          "cite": [
            "290 F.3d 223",
            "2002 U.S. App. LEXIS 7193",
            "2002 WL 629825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Zavala",
          "cluster_id": 63259,
          "cite": [
            "541 F.3d 562",
            "2008 U.S. App. LEXIS 18132",
            "2008 WL 3877232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Robles",
          "cluster_id": 5607956,
          "cite": [
            "23 Cal. 4th 789",
            "3 P.3d 311",
            "2000 Daily Journal DAR 7789",
            "97 Cal. Rptr. 2d 914",
            "2000 Cal. Daily Op. Serv. 5894",
            "2000 Cal. LEXIS 5217"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gulbrandson",
          "cluster_id": 1127545,
          "cite": [
            "906 P.2d 579",
            "184 Ariz. 46",
            "202 Ariz. Adv. Rep. 46",
            "1995 Ariz. LEXIS 105"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Fayed",
          "cluster_id": 4741522,
          "cite": [
            "9 Cal. 5th 147",
            "260 Cal. Rptr. 3d 761",
            "460 P.3d 1149"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Morehead",
          "cluster_id": 4628457,
          "cite": [
            "2019 CO 48",
            "442 P.3d 413"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lee Erwin Johnson",
          "cluster_id": 668574,
          "cite": [
            "22 F.3d 674",
            "1994 U.S. App. LEXIS 9337",
            "1994 WL 158484"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marco Burton",
          "cluster_id": 777431,
          "cite": [
            "288 F.3d 91",
            "2002 U.S. App. LEXIS 7851",
            "2002 WL 753492"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lee",
          "cluster_id": 1685650,
          "cite": [
            "976 So. 2d 109",
            "2008 WL 343031"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Timothy W. Markling",
          "cluster_id": 655530,
          "cite": [
            "7 F.3d 1309",
            "1993 U.S. App. LEXIS 27411",
            "1993 WL 421739"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Christy",
          "cluster_id": 2648104,
          "cite": [
            "739 F.3d 534",
            "2014 WL 26455",
            "2014 U.S. App. LEXIS 84"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 7898279,
          "cite": [
            "251 Conn. 285",
            "743 A.2d 1",
            "1999 Conn. LEXIS 407"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vilar",
          "cluster_id": 1039434,
          "cite": [
            "729 F.3d 62",
            "92 A.L.R. Fed. 2d 661",
            "2013 WL 4608948",
            "2013 U.S. App. LEXIS 18143"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Murray v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112136 OR 9431434 OR 9431435 OR 9431436) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzg2NzIwMDAwMDAwJnM9Mjk0NzMwMCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112136+OR+9431434+OR+9431435+OR+9431436%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 18,
        "triage_snippet_classified": 182
      },
      "lane2_top_cited": {
        "query": "cites:(112136 OR 9431434 OR 9431435 OR 9431436)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTImcz03NTc3MTMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112136+OR+9431434+OR+9431435+OR+9431436%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112136 OR 9431434 OR 9431435 OR 9431436)",
        "reviewed": 44,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 44,
        "triage_read": 0,
        "triage_snippet_classified": 44
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112136 OR 9431434 OR 9431435 OR 9431436)",
    "indexed_citing_opinions": 844,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112136,
        "count": 716,
        "count_source": "search"
      },
      {
        "opinion_id": 9431434,
        "count": 142,
        "count_source": "search"
      },
      {
        "opinion_id": 9431435,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431436,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1426,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/murray-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3NjE1ODgmcz05NDk0NjA0JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112136+OR+9431434+OR+9431435+OR+9431436%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112136,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 106172,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 111259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 111670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 457689,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 468097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112136,
        "cited_id": 477960,
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
    "date_created": "2026-07-05T14:49:53Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:54:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:50:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Murray v. United States

```
<opinion type="majority">
<author id="b587-6"><page-number citation-index="1" label="535">*535</page-number>Justice Scalia</author>
<p id="AqtH">delivered the opinion of the Court.</p>
<p id="b587-7">In <em>Segura </em>v. <em>United States, </em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U. S. 796</a></span> (1984), we held that police officers’ illegal entry upon' private’ premises did not require suppression of evidence subsequently discovered at those premises when executing a search warrant’obtained on the basis of information wholly unconnected with the initial entry. In these consolidated cases we are faced with the question whether, again assuming evidence obtained pursuant to an independently obtained search warrant, the portion of such evidence that had been observed in plain view at the time of a prior illegal entry must be suppressed.</p>
<p id="AJ8L">I</p>
<p id="b587-3">Both cases arise out of the conviction of petitioner Michael F. Murray, petitioner James D. Carter, and others for conspiracy to possess and distribute illegal drugs. Insofar as relevant for our purposes, the facts are as follows: Based on information received from informants, federal law enforcement agents had been surveilling petitioner Murray and several of his co-conspirators. At about 1:45 p.m. on April 6, 1983, they observed Murray drive a truck and Carter drive a green camper, into a warehouse in South Boston. When the petitioners drove the vehicles out about 20 minutes later, the surveilling agents saw within the warehouse two individuals and a tractor-trailer rig bearing a long, dark container. Murray and Carter later turned over the truck and camper to other drivers, who were in .turn followed and ultimately arrested, and the vehicles lawfully seized. Both vehicles were found to contain marijuana.</p>
<p id="b587-4">After receiving this information, several of the agents converged on the South Boston warehouse and forced entry. They found the warehouse unoccupied, but observed in plain view numerous burlap-wrapped bales that were later found to contain marijuana. They left without disturbing the bales, kept the warehouse under surveillance, and did not reenter it until they had a search warrant. In applying for <page-number citation-index="1" label="536">*536</page-number>the warrant, the agents did not mention the prior entry, and did not rely on any observations made during that entry. When the warrant was issued — at 10:40 p.m., approximately eight hours after the initial entry — the agents immediately reentered the warehouse and seized 270 bales of marijuana and notebooks listing customers for whom the bales were destined.</p>
<p id="b588-5">Before trial, petitioners moved to suppress the evidence found in the warehouse. The District Court denied the motion, rejecting petitioners’ arguments that the warrant was invalid because the agents did not inform the Magistrate about their prior warrantless entry, and that the warrant was tainted by that entry. <em>United States </em>v. <em>Carter, </em>No. 83-102-S (Mass., Dec. 23, 1983), App. to Pet. for Cert. 44a-45a. The First Circuit affirmed, assuming for purposes of its-decision that the first entry into the warehouse was unlawful. <em>United States </em>v. <em>Moscatiello, </em><span class="citation" data-id="8934273"><a href="/opinion/8943744/united-states-v-moscatiello/" aria-description="Citation for case: United States v. Moscatiello">771 F. 2d 589</a></span> (1985). Murray and Carter then separately filed petitions for certiorari, which we granted,<footnotemark>1</footnotemark> <span class="citation multiple-matches"><a href="/c/U.%20S./480/916/">480 U. S. 916</a></span> (1987), and have consolidated here.</p>
<p id="b588-6">II</p>
<p id="b588-7">The exclusionary rule prohibits introduction into evidence of tangible materials seized during an unlawful search, <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and of testimony concerning knowledge acquired during an unlawful search, <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961). Beyond that, the exclusionary rule also prohibits the introduction of derivative evidence, both tangible and testimonial, that is <page-number citation-index="1" label="537">*537</page-number>the product of the primary evidence, or that is otherwise acquired as an indirect result of the unlawful search, up to the point at which the connection with the unlawful search becomes “so attentuated as to dissipate the taint,” <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939). See <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 484-485</a></span> (1963).</p>
<p id="b589-5">Almost simultaneously with our development of the exclusionary rule, in the first quarter of this century, we also announced what has come to be known as the “independent source” doctrine. See <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 392</a></span> (1920). That doctrine, which has been applied to evidence acquired not only through Fourth Amendment violations but also through Fifth and Sixth Amendment violations, has recently been described as follows:</p>
<blockquote id="b589-6">“ET]he interest of society in deterring unlawful police conduct and the public interest in having juries receive all probative evidence of a crime are properly balanced by putting- the police in the same, not a <em>worse, </em>position that they would have been in if no police error or misconduct had occurred. . . . When the challenged evidence has an independent source, exclusion of such evidence would put the police in a worse position than they would have been in absent any error or violation.” <em>Nix </em>v. <em>Williams, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#443" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 443</a></span> (1984)</blockquote>
<p id="b589-7">The dispute here is over the scope of this doctrine. Petitioners contend that it applies only to evidence obtained for the first time during an independent lawful search. The Government argues that it applies also to evidence initially discovered during, or as a consequence of, an unlawful search, but later obtained independently from activities untainted by the initial illegality. We think the Government’s view has better support in both precedent and policy.</p>
<p id="b589-8">Our cases have used the concept of “independent source” in a more general and a more specific sense. The more general sense identifies <em>all </em>evidence acquired in a fashion untainted <page-number citation-index="1" label="538">*538</page-number>by the illegal evidence-gathering activity. Thus, where an unlawful entry has given investigators knowledge of facts <em>x </em>and <em>y, </em>but fact <em>z </em>has been learned by other means, fact <em>z </em>can be said to be admissible because derived from an “independent source.” This is how we used the term in <em>Segura </em>v. <em>United States, </em><span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/" aria-description="Citation for case: Segura v. United States">468 U. S. 796</a></span> (1984). In that case, agents unlawfully entered the defendant’s apartment and remained there until a search warrant was obtained. The admissibility of what they discovered while waiting in the apartment was not before us, <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#802" aria-description="Citation for case: Segura v. United States"><em>id., </em>at 802-803, n. 4</a></span>, but we held that the evidence found for the first time during the execution of the valid and untainted search warrant was admissible because it was discovered pursuant to an “independent source,” <span class="citation" data-id="9429757"><a href="/opinion/111259/segura-v-united-states/#813" aria-description="Citation for case: Segura v. United States">id., at 813-814</a></span>. See also <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#240" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 240-242</a></span> (1967); <em>Costello </em>v. <em>United States, </em><span class="citation" data-id="9422121"><a href="/opinion/106172/costello-v-united-states/#280" aria-description="Citation for case: Costello v. United States">365 U. S. 265, 280</a></span> (1961); <em>Nardone </em>v. <em>United States, supra, </em>at 341.</p>
<p id="b590-5">The original use of the term, however, and its more important use for purposes of these cases, was more specific. It was originally applied in the exclusionary rule context, by Justice Holmes, with reference to that particular category of evidence acquired by an untainted search <em>which is identical to the evidence unlawfully acquired </em>— that is, in the example just given, to knowledge of facts <em>x </em>and <em>y </em>derived from an independent source:</p>
<blockquote id="b590-6">“The essence of a provision forbidding the acquisition of evidence in a certain way is that not merely evidence so acquired shall not be used before the Court but that it shall not be used at all. Of course this does not mean that the facts thus obtained become sacred and inaccessible. If knowledge of them is gained from an independent source they may be proved like any others.” <em>Silverthorne Lumber, supra, </em>at 392.</blockquote>
<p id="b590-7">As the First Circuit has observed, “[i]n the classic independent source situation, information which is received through an illegal source is considered to be cleanly obtained when <page-number citation-index="1" label="539">*539</page-number>it arrives through an independent source.” <em>United States </em>v. <em>Silvestri, </em><span class="citation" data-id="468097"><a href="/opinion/468097/united-states-v-frederick-silvestri-elder/#739" aria-description="Citation for case: United States v. Frederick Silvestri, Elder">787 F. 2d 736, 739</a></span> (1986). We recently assumed this application of the independent source doctrine (in the Sixth Amendment context) in <em>Nix </em>v. <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Williams, supra.</a></span> </em>There incriminating statements obtained in violation of the defendant’s right to counsel had led the police to the victim’s body. The. body had not in fact been found through an independent source as well, and so the independent source doctrine was not itself applicable. We held, however, that evidence concerning the body was nonetheless admissible because a search had been under way which would have discovered the body, had it not been called off because of the discovery produced by the unlawfully obtained statements. <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#448" aria-description="Citation for case: Nix v. Williams"><em>Id., </em>at 448-460</a></span>. This “inevitable discovery” doctrine obviously assumes the validity of the independent source doctrine as applied to evidence initially acquired unlawfully. It would make no sense to admit the evidence because the independent search, had it not been aborted, would have found the body, but to exclude the evidence if the search had continued and had in fact found the. body. The inevitable discovery doctrine, with its distinct requirements, is in reality an extrapolation from the independent source doctrine: <em>Since </em>the tainted evidence would be admissible if in fact discovered through an independent source, it should be admissible if it inevitably would have been discovered.</p>
<p id="b591-5">Petitioners’ asserted policy basis for excluding evidence which is initially discovered during an illegal search, but is subsequently acquired through an independent and lawful source, is that a contrary rule will remove all deterrence to, and indeed positively encourage, unlawful police searches. As petitioners, see the incentives, law enforcement officers will routinely enter without a warrant to make sure that what they expect to be on the premises is in fact there. If it is not, they will have spared themselves the time and trouble of getting a warrant; if it is, they, can get the warrant and use the evidence despite the unlawful entry. Brief for Peti<page-number citation-index="1" label="540">*540</page-number>tioners 42. We see the incentives differently. An officer with probable cause sufficient to obtain a search warrant would be foolish to enter the premises first in an unlawful manner. By doing so, he would risk suppression of all evidence on the premises, both seen and unseen, since his action would add to the normal burden of convincing a magistrate that there is probable cause the much more onerous burden of convincing a trial court that no information gained from the illegal entry affected either the law enforcement officers’ decision to seek a warrant or the magistrate’s decision to grant it. See Part III, <em>infra. </em>Nor would the officer <em>without </em>sufficient probable cause to obtain a search warrant have any added incentive to conduct an unlawful entry, since whatever he finds cannot be used to establish probable cause before a magistrate.<footnotemark>2</footnotemark></p>
<p id="b592-5">It is possible to read petitioners’ briefs as asserting the more narrow position that the “independent source” doctrine does apply to independent acquisition of evidence previously <page-number citation-index="1" label="541">*541</page-number>derived <em>indirectly </em>from the unlawful search, but does not apply to what they call “primary evidence,” that is, evidence acquired during the course of the search itself. In addition to finding no support in our precedent, see <em>Silverthorne Lumber, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#392" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S., at 392</a></span> (referring specifically to evidence seized during an unlawful search), this strange distinction would produce results bearing no relation to the policies of the exclusionary rule. It would mean, for example, that the government’s knowledge of the existence and condition of a dead body, knowledge lawfully acquired through independent sources, would have to be excluded if government agents had previously observed the body during an unlawful search of the defendant’s apartment; but not if they had observed a notation that the body was buried in a certain location, producing consequential discovery of the corpse.</p>
<p id="A-L">III</p>
<p id="b593-3">To apply what we have said to the present cases: Knowledge that the marijuana was in the warehouse was assuredly acquired at the time of the unlawful entry. But it was also acquired at the time of entry pursuant to the warrant, and if that later acquisition was not the result of the -earlier entry there is no reason why the independent source doctrine should not apply. Invoking the exclusionary rule would put the police (and society) not in the <em>same </em>position they would have occupied if no violation occurred, but in a <em>worse </em>one. See <em>Nix </em>v. <em>Williams, </em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#443" aria-description="Citation for case: Nix v. Williams">467 U. S., at 443</a></span>.</p>
<p id="b593-4">We think this is also true with respect to the tangible evidence, the bales of marijuana. It would make no more sense to exclude that than it would to exclude tangible evidence found upon the corpse in <em><span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/" aria-description="Citation for case: Nix v. Williams">Nix</a></span>, </em>if the search in that case had not been abandoned and had in fact come upon the body. The First Circuit has discerned a difference between tangible and intangible evidence that has been tainted, in that objects “once seized cannot be cleanly reseized without returning the objects to private control.” <em>United States </em>v. <em>Silvestri, </em><span class="citation" data-id="468097"><a href="/opinion/468097/united-states-v-frederick-silvestri-elder/#739" aria-description="Citation for case: United States v. Frederick Silvestri, Elder">787 <page-number citation-index="1" label="542">*542</page-number>F. 2d, at 739</a></span>. It seems to us, however, that reseizure of tangible evidence already seized is no more impossible than rediscovery of intangible evidence already discovered. The independent source doctrine does not rest upon such metaphysical analysis, but upon the policy that, while the government should not profit from its illegal activity, neither should it be placed in a worse position than it would otherwise have occupied. So long as a later, lawful seizure is genuinely independent of an earlier, tainted one (which may well be difficult to establish where the seized goods are kept in the police’s possession) there is no reason why the independent source doctrine should not apply.</p>
<p id="b594-5">The ultimate question, therefore, is whether the search pursuant to warrant was in fact a genuinely independent source of the information and tangible evidence at issue here. This would not have been the case if the agents’ decision to seek the warrant was prompted by what they had seen during the initial entry,<footnotemark>3</footnotemark> or if information obtained during that entry was presented to the Magistrate and affected his decision to issue the warrant. On this point the Court of Appeals said the following:</p>
<blockquote id="b594-6">“[W]e can be absolutely certain that the warrantless entry in no way contributed in the slightest either to the issuance of a warrant or to the discovery of the evidence <page-number citation-index="1" label="543">*543</page-number>during the iawful search that occurred pursuant to the warrant.</blockquote>
<blockquote id="b595-5">“This is as clear a case as can be imagined where the discovery of the contraband in plain view was totally irrelevant to the later securing of a warrant and the successful search that ensued. As there was ho causal link whatever between the illegal entry and the discovery of the challenged evidence, we find no error in the court’s refusal to suppress.” <em>United States </em>v. <em>Moscatiello, </em><span class="citation" data-id="8934273"><a href="/opinion/8943744/united-states-v-moscatiello/#603" aria-description="Citation for case: United States v. Moscatiello">771 F. 2d, at 603, 604</a></span>.</blockquote>
<p id="b595-6">Although these statements Can be read to provide emphatic support for the Government’s position, it is the function of the District Court rather than the Court of Appeals to determine the facts, and we do not think the Court of Appeals’ conclusions are supported by adequate findings. The District Court found that the agents did not reveal their warrantless entry to the Magistrate, App. to Pet. for Cert. 43a, and that they did not include in their application for a warrant any recitation of their observations in the warehouse, <em><span class="citation" data-id="8934273"><a href="/opinion/8943744/united-states-v-moscatiello/" aria-description="Citation for case: United States v. Moscatiello">id.,</a></span> </em>at 44a-45a. It did not, however, explicitly find that the agents would have sought a warrant if they had not earlier entered the warehouse. The Government concedes this in its brief. Brief for United States 17, n. 5. To be sure, the District Court did determine that the purpose of the warrantless entry was in part “to guard against the destruction of possibly critical evidence,” App. to Pet. for Cert. 42a, and one could perhaps infer from this that the agents who made the entry already planned to obtain that “critical evidence” through a warrant-authorized search. That inference is not, however, clear enough to justify the conclusion that the District Court’s findings amounted to a determination of independent source.</p>
<p id="b595-7">Accordingly, we vacate the judgment and remand these cases to the Court of Appeals with instructions that it remand to the District Court for determination whether the <page-number citation-index="1" label="544">*544</page-number>warrant-authorized search of the warehouse was an independent source of the challenged evidence in the sense we have described.</p>
<p id="b596-5">
<em>It is so ordered.</em>
</p>
<judges id="b596-6">Justice Brennan and Justice Kennedy took no part in the consideration or decision of these cases.</judges>
<footnote label="1">
<p id="b588-8">The original petitions raised both the present Fourth Amendment claim and a Speedy Trial Act claim. We granted the petitions, vacated the judgment below, and remanded for reconsideration of the Speedy Trial Act issue in light of <em>Henderson </em>v. <em>United States, </em><span class="citation" data-id="9430511"><a href="/opinion/111670/henderson-v-united-states/" aria-description="Citation for case: Henderson v. United States">476 U. S. 321</a></span> (1986). <em>Carter </em>v. <em>United States </em>and <em>Murray </em>v. <em>United States, </em><span class="citation" data-id="9054182"><a href="/opinion/9060584/carter-v-united-states/" aria-description="Citation for case: Carter v. United States">476 U. S. 1138</a></span> (1986). On remand, the Court of Appeals again rejected the Speedy Trial Act claim and did not reexamine its prior ruling on the Fourth Amendment question. <span class="citation" data-id="9475455"><a href="/opinion/477960/united-states-v-james-d-carter-united-states-of-america-v-michael-f/" aria-description="Citation for case: United States v. James D. Carter, United States of...">803 F. 2d 20</a></span> (1986). Petitioners again sought writs of certiorari, which we granted limited to the Fourth Amendment question.</p>
</footnote>
<footnote label="2">
<p id="b592-6">Justice Marshall argues, in effect, that where the police cannot point to some historically verifiable fact demonstrating that the subsequent search pursuant to a warrant was wholly unaffected by the prior illegal <em>search </em>— v. <em>g., </em>that they had already sought the warrant before entering the premises —we should adopt a <em>per se </em>rule of inadmissibilty. See <em>post, </em>at 549. We do not believe that such a prophylatic exception to the independent source rule is necessary. To say that a district court must be satisfied that a warrant would have been sought without the illegal entry is not to give dispositive effect to police officers’ assurances on the point. Where the facts render those assurances implausible, the independent source doctrine will not apply.</p>
<p id="b592-7">We might note that there is no basis for pointing to the present cases as an example of a “search first, warrant later” mentality. The District Court found that the agents entered the warehouse “in an effort to apprehend any participants who might have remained inside and to guard against the destruction of possibly critical evidence.” <em>United States </em>v. <em>Carter, </em>No. 83-102-S (Mass., Dec. 23, 1983), App. to Pet. for Cert. 42a. While they may have misjudged the existence of sufficient exigent circumstances to justify the warrantless entry (the Court of Appeals did not reach that issue and neither do we), there is nothing to suggest that they went in merely to see if there was anything worth getting a warrant for.</p>
</footnote>
<footnote label="3">
<p id="b594-7">Justice Marshall argues that “the relevant question [is] whether, even if the initial entry uncovered no evidence, the officers would return immediately with a warrant to conduct a second search.” <em>Post, </em>at 548, n. 2; see <em>post, </em>at 549-550, n. 4. We do not see how this is “relevant” at all. To determine whether the warrant was independent of the illegal entry, one must ask whether it would have been sought even if what actually happened had not occurred — not whether it would have been sought if something else had happened. That is to say, what counts is whether the actual illegal search had any effect in producing the warrant, not whether some hypothetical illegal search would have aborted the warrant. Only that much is needed to assure that what comes before the court is not the product of illegality: to go further than that would be to expand our existing exclusionary rule.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/NASA v. FLRA.md  (`case`, 5 assertions)

### content_page

```
---
title: "NASA v. FLRA"
type: case
citation: "527 U.S. 229 (1999)"
parallel_cite: "119 S. Ct. 1979; 144 L. Ed. 2d 258"
neutral_cite: 1999 U.S. LEXIS 4190
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-06-17
docket: 98-369
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: NASA v. FLRA
  varies_by_point: false
  scope_note: "Good law; a statutory (FSLMRS) holding on federal-sector representation rights — distinct from the Fifth Amendment Garrity line, grouped with it for the public-employee compelled-interview context."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118306/nasa-v-flra/"
  cluster_id: 118306
  opinion_id: 118306
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Related (cross-doctrine)"
related: ["[[Garrity v. New Jersey]]", "[[Lefkowitz v. Turley]]", "[[Kalkines v. United States]]"]
aliases: ["National Aeronautics and Space Administration v. Federal Labor Relations Authority", "NASA v. Federal Labor Relations Authority"]
tags: ["case", "public-employee", "garrity", "federal-employee", "representation-rights", "fslmrs", "weingarten"]
holding: "A NASA Office of Inspector General investigator examining a NASA employee is a 'representative of the agency' under 5 U.S.C. § 7114(a)(2)(B), so the employee's statutory right to union representation at an investigatory examination that may lead to discipline applies (the federal-sector representation right)."
lake:
  record_id: NASA v. FLRA
  status: verified
  projected_at: 2026-07-09
---

# NASA v. FLRA

*527 U.S. 229 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A NASA Office of Inspector General (NASA-OIG) investigator, acting on information from the FBI, interviewed an employee of NASA's Marshall Space Flight Center about threatening activities. The employee was allowed to have his attorney and union representative present, but the investigator limited the union representative's participation. The union filed an unfair-labor-practice charge with the Federal Labor Relations Authority, alleging a violation of the employee's right to union representation under the Federal Service Labor-Management Relations Statute (FSLMRS), 5 U.S.C. § 7114(a)(2)(B). The ALJ and the Authority ruled for the union, and the Eleventh Circuit enforced the order; the Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]] to resolve a circuit split.

## Issue
Whether an investigator employed in NASA's Office of Inspector General is a "representative of the agency" within the meaning of 5 U.S.C. § 7114(a)(2)(B), so that a NASA employee's statutory right to union representation at an investigatory examination may be invoked.

## Rule
The statute grants the representation right at "any examination of an employee in the unit by a representative of the agency in connection with an investigation if — (i) the employee reasonably believes that the examination may result in disciplinary action against the employee; and (ii) the employee requests representation." — 5 U.S.C. § 7114(a)(2), quoted at 527 U.S. at 233. ^pin-233

The Court read "representative of the agency" to reach OIG investigators: "The question presented by this case is whether an investigator employed in NASA's Office of Inspector General (NASA-OIG) can be considered a 'representative' of NASA when examining a NASA employee, such that the right to union representation in the FSLMRS may be invoked. . . . [T]he plain text of the two statutes, buttressed by administrative deference and Congress' countervailing policy concerns, dictates an affirmative answer." — [527 U.S. at 231](https://www.courtlistener.com/opinion/118306/nasa-v-flra/#:~:text=by%20a-,representative%20of%20the%20agency). ^pin-231

## Application
It was undisputed that the employee reasonably believed the OIG examination could lead to discipline, that he requested union representation, and that NASA was the relevant "agency." The only contested point was whether the OIG investigator was a "representative of the agency." Because § 7114(a)(2)(B) refers simply to a representative of "the agency" (NASA) and is not confined to management's collective-bargaining representatives or to any particular internal office, the OIG investigator qualified — the risk of discipline to the employee does not depend on which component of NASA conducts the interview. The statutory representation right therefore applied, and limiting the union representative's participation violated it.

## Conclusion
A NASA-OIG investigator is a "representative of the agency" under § 7114(a)(2)(B), so the employee's statutory right to union representation applied; the Authority's order was enforced and the Eleventh Circuit affirmed. The decision secures a federal employee's representation right during investigatory examinations that may lead to discipline.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *NASA v. FLRA* is good law. It is a **statutory** (FSLMRS) representation-rights holding — the federal-sector analog of private-sector *Weingarten* rights — rather than a Fifth Amendment ruling. It is grouped with [[Garrity v. New Jersey]], [[Lefkowitz v. Turley]], and [[Kalkines v. United States]] because it governs the same setting: the public employee facing a compelled investigatory interview.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Related (cross-doctrine)*

## Sources
- *National Aeronautics & Space Administration v. Federal Labor Relations Authority*, 527 U.S. 229 (1999) — https://www.courtlistener.com/opinion/9188189/national-aeronautics-space-administration-v-federal-labor-relations-authority/ — pinpoints: 231, 233.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b65ffea164b6a846", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "527 U.S. 229 (1999)", "court": "U.S. Supreme Court", "neutral_cite": "1999 U.S. LEXIS 4190", "official_citation_present": true, "parallel_cite": "119 S. Ct. 1979; 144 L. Ed. 2d 258", "title": "NASA v. FLRA", "year": "1999"}}
{"assertion_id": "bdad2e3e3ea7b84f", "dimension": "support", "kind": "home_role", "locator": {"home": "Public-Employee Compelled Statements (Garrity)"}, "payload": {"home": "Public-Employee Compelled Statements (Garrity)", "role": "Related (cross-doctrine)", "title": "NASA v. FLRA"}}
{"assertion_id": "f63fabf59c8db88b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A NASA Office of Inspector General investigator examining a NASA employee is a 'representative of the agency' under 5 U.S.C. § 7114(a)(2)(B), so the employee's statutory right to union representation at an investigatory examination that may lead to discipline applies (the federal-sector representation right).", "title": "NASA v. FLRA"}}
{"assertion_id": "04d25edea8a989b2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1999-06-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "NASA v. FLRA", "field_i_validity": "good_law", "scope_note": "Good law; a statutory (FSLMRS) holding on federal-sector representation rights — distinct from the Fifth Amendment Garrity line, grouped with it for the public-employee compelled-interview context.", "title": "NASA v. FLRA", "varies_by_point": "false"}}
{"assertion_id": "4d4389603883cb69", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "NASA v. FLRA"}}
```

### lake record — NASA v. FLRA

```json
{
  "schema_version": "s2.v1",
  "record_id": "NASA v. FLRA",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Nasa v. Flra",
    "case_name_short": "Nasa",
    "case_name_full": "",
    "input_case_name": "NASA v. FLRA",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-06-17",
    "year": 1999,
    "docket": "98-369",
    "cluster_id": 118306,
    "lead_opinion_id": 118306,
    "sibling_ids": [
      118306
    ],
    "absolute_url": "/opinion/118306/nasa-v-flra/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "527 U.S. 229",
      "volume": "527",
      "reporter": "U.S.",
      "page": "229",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1979",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1979",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 258",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "258",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 4190",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4190",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "527 U.S. 229",
        "volume": "527",
        "reporter": "U.S.",
        "page": "229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1979",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1979",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "144 L. Ed. 2d 258",
        "volume": "144",
        "reporter": "L. Ed. 2d",
        "page": "258",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 4190",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "4190",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "527 U.S. 229",
    "official_selection": {
      "court_class": "scotus",
      "selected": "527 U.S. 229",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-233",
      "page": null,
      "quote": "within the meaning of 5 U.S.C. \u00a7 7114(a)(2)(B), so that a NASA employee's statutory right to union representation at an investigatory examination may be invoked. ## Rule The statute grants the representation right at",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-231",
      "page": null,
      "quote": "representative of the agency",
      "star_marker": "233",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6390,
      "fragment": "#:~:text=by%20a-,representative%20of%20the%20agency",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "NASA v. FLRA",
    "varies_by_point": false,
    "scope_note": "Good law; a statutory (FSLMRS) holding on federal-sector representation rights \u2014 distinct from the Fifth Amendment Garrity line, grouped with it for the public-employee compelled-interview context.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jefferson v. Harris",
          "cluster_id": 3187270,
          "cite": [
            "170 F. Supp. 3d 194",
            "2016 U.S. Dist. LEXIS 35685",
            "2016 WL 1091063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Railroad Passenger Corporation v. Fraternal Order of Police, Lodge 189",
          "cluster_id": 3151447,
          "cite": [
            "142 F. Supp. 3d 82",
            "204 L.R.R.M. (BNA) 3525",
            "2015 U.S. Dist. LEXIS 148320",
            "2015 WL 6692104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane1_negative"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Federal Labor Relations Authority",
          "cluster_id": 2657562,
          "cite": [
            "409 U.S. App. D.C. 51",
            "745 F.3d 1219",
            "2014 WL 1099618",
            "198 L.R.R.M. (BNA) 2793",
            "2014 U.S. App. LEXIS 5297"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neighborhood Assistance Corporation of America (Naca) v. U.S. Department of Housing and Urban Development",
          "cluster_id": 2660018,
          "cite": [
            "19 F. Supp. 3d 1",
            "2013 WL 5314457",
            "2013 U.S. Dist. LEXIS 136857"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Treasury Employees Union v. Federal Labor Relations Authority",
          "cluster_id": 2678671,
          "cite": [
            "410 U.S. App. D.C. 239",
            "754 F.3d 1031",
            "2014 WL 2721170",
            "199 L.R.R.M. (BNA) 3617",
            "2014 U.S. App. LEXIS 11208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Trkr United Sfty v. Mead, Kenneth M.",
          "cluster_id": 185455,
          "cite": [
            "251 F.3d 183",
            "346 U.S. App. D.C. 122",
            "2001 U.S. App. LEXIS 11680",
            "2001 WL 603688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee Valley Authority, Georgia Power Company, Intervenor v. United States Environmental Protection Agency, John H. Hankinson, Jr., Regional Administrator, Alabama Power Company, Duke Energy Corporation, Georgia Power Company, Intervenor v. United States Environmental Protection Agency, John H. Hankinson, Jr., Regional Administrator, Tennessee Valley Authority, Georgia Power Company, Intervenor v. United States Environmental Protection Agency, John H. Hankinson, Jr., Regional Administrator, Tennessee Valley Authority, Georgia Power Company, Intervenor v. United States Environmental Protection Agency, John H. Hankinson, Jr., Regional Administrator, Alabama Power Company, Duke Energy Corporation, Georgia Power Company, Intervenor v. United States Environmental Protection Agency, John H. Hankinson, Jr., Regional Administrator, Tennessee Valley Authority, Georgia Power Company, Intervenor v. United States Environmental Protection Agency, John H. Hankinson, Jr., Regional Administrator, Tennessee Valley Authority v. Christine Todd Whitman, Administrator, United States Environmental Protection Agency, United States Environmental Protection Agency, Alabama Power Company v. Christine Todd Whitman, Administrator, United States Environmental Protection Agency, United States Environmental Protection Agency, Tennessee Valley Public Power Association, Memphis Light, Gas & Water Division, Electric Power Board of Chattanooga v. Christine Todd Whitman, Administrator, United States Environmental Protection Agency, United States Environmental Protection Agency, Duke Energy Corporation v. Christine Todd Whitman, Administrator, United States Environmental Protection Agency, United States Environmental Protection Agency",
          "cluster_id": 776384,
          "cite": [
            "278 F.3d 1184"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Truckers United for Safety v. Mead",
          "cluster_id": 2399005,
          "cite": [
            "86 F. Supp. 2d 1",
            "2000 U.S. Dist. LEXIS 2576",
            "2000 WL 280030"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DOJ v. FLRA",
          "cluster_id": 185513,
          "cite": [
            "266 F.3d 1228"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Round Rock v. Rodriguez",
          "cluster_id": 2273819,
          "cite": [
            "317 S.W.3d 871",
            "189 L.R.R.M. (BNA) 2076",
            "2010 Tex. App. LEXIS 5867",
            "2010 WL 2867385"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ben Tan",
          "cluster_id": 5296734,
          "cite": [
            "16 F.4th 1346"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "American Federation of Government Employees v. Federal Labor Relations Authority",
          "cluster_id": 4254518,
          "cite": [
            "836 F.3d 1291",
            "2016 WL 4659805"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arias v. Herzon",
          "cluster_id": 10654928,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Potential Litigation Between the Department of Labor and the United States Postal Service",
          "cluster_id": 6236899,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "National Railroad Passenger Corp. v. Fraternal Order of Police, Lodge 189 Labor Committee",
          "cluster_id": 4387093,
          "cite": [
            "855 F.3d 335",
            "209 L.R.R.M. (BNA) 3007",
            "2017 U.S. App. LEXIS 7522",
            "2017 WL 1521563"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "ID/Guerra LP v. Texas Workforce Commission",
          "cluster_id": 2952040,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "the City of Round Rock, Texas, and Round Rock Fire Chief Larry Hodge v. Jaime Rodriguez and Round Rock Fire Fighters Association",
          "cluster_id": 2952033,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "US DHS Customs and Border v. FLRA",
          "cluster_id": 2676834,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "NASA v. FLRA:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118306) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 12,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 12,
        "triage_read": 2,
        "triage_snippet_classified": 10
      },
      "lane2_top_cited": {
        "query": "cites:(118306)",
        "reviewed": 18,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 18,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(118306)",
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
    "complete_query": "cites:(118306)",
    "indexed_citing_opinions": 18,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118306,
        "count": 18,
        "count_source": "search"
      }
    ],
    "citation_count": 18,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/nasa-v-flra.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 18,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118306,
        "cited_id": 109194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118306,
        "cited_id": 112214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118306,
        "cited_id": 112437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118306,
        "cited_id": 118270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118306,
        "cited_id": 510640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118306,
        "cited_id": 670704,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118306,
        "cited_id": 744588,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118306,
        "cited_id": 1637175,
        "source": "search.opinions[].cites[]"
      }
    ]
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LR",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T15:01:24Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T15:02:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T15:02:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T15:04:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T15:02:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — NASA v. FLRA

```
<div>
<center><b><span class="citation multiple-matches"><a href="/c/U.S./527/229/">527 U.S. 229</a></span> (1999)</b></center>
<center><h1>NATIONAL AERONAUTICS AND SPACE ADMINISTRATION et al.<br>
v.<br>
FEDERAL LABOR RELATIONS AUTHORITY et al.</h1></center>
<center>No. 98-369.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued March 23, 1999.</center>
<center>Decided June 17, 1999.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE ELEVENTH CIRCUIT
<p><span class="star-pagination">*230</span> Stevens, J., delivered the opinion of the Court, in which Kennedy, Souter, Ginsburg, and Breyer, JJ., joined. Thomas, J., filed a dissenting opinion, in which Rehnquist, C. J., and O'Connor and Scalia, JJ., joined, <i>post,</i> p. 246.</p>
<p><span class="star-pagination">*231</span> <i>David C. Frederick</i> argued the cause for petitioners. With him on the brief were <i>Solicitor General Waxman, Assistant Attorney General Hunger, Deputy Solicitor General Underwood, William Kanter,</i> and <i>Howard S. Scher.</i> </p>
<p><i>David M. Smith</i> argued the cause for respondent Federal Labor Relations Authority. With him on the brief was <i>Ann M. Boehm. Stuart A. Kirsch</i> argued the cause for respondent American Federation of Government Employees, AFL CIO. With him on the brief were <i>Mark D. Roth, Jonathan P. Hiatt, James B. Coppess,</i> and <i>Laurence Gold.</i><sup>[*]</sup></p>
<p>Justice Stevens, delivered the opinion of the Court.</p>
<p>On October 12, 1978, Congress enacted the Inspector General Act (IGA), 5 U. S. C. App. § 1 <i>et seq.,</i> p. 1381, which created an Office of Inspector General (OIG) in each of several federal agencies, including the National Aeronautics and Space Administration (NASA). The following day, Congress enacted the Federal Service Labor-Management Relations Statute (FSLMRS), <span class="citation no-link">5 U. S. C. § 7101</span> <i>et seq.,</i> which provides certain protections, including union representation, to a variety of federal employees. The question presented by this case is whether an investigator employed in NASA's Office of Inspector General (NASAOIG) can be considered a "representative" of NASA when examining a NASA employee, such that the right to union representation in the FSLMRS may be invoked. § 7114(a)(2)(B). Although certain arguments of policy may support a negative answer to that question, the plain text of the two statutes, buttressed by administrative deference and Congress' countervailing policy concerns, dictates an affirmative answer.</p>
<p></p>
<h2>I</h2>
<p>In January 1993, in response to information supplied by the Federal Bureau of Investigation (FBI), NASA's OIG conducted <span class="star-pagination">*232</span> an investigation of certain threatening activities of an employee of the George C. Marshall Space Flight Center in Huntsville, Alabama, which is also a component of NASA. A NASAOIG investigator contacted the employee to arrange for an interview and, in response to the employee's request, agreed that both the employee's lawyer and union representative could attend. The conduct of the interview gave rise to a complaint by the union representative that the investigator had improperly limited his participation. The union filed a charge with the Federal Labor Relations Authority (Authority) alleging that NASA and its OIG had committed an unfair labor practice. See §§ 7116(a)(1), (8).</p>
<p>The Administrative Law Judge (ALJ) ruled for the union with respect to its complaint against NASAOIG. See App. to Pet. for Cert. 71a. The ALJ concluded that the OIG investigator was a "representative" of NASA within the meaning of § 7114(a)(2)(B), and that certain aspects of the investigator's behavior had violated the right to union representation under that section. <i>Id.,</i> at 64a65a, 69a70a. On review, the Authority agreed that the NASAOIG investigator prevented the union representative from actively participating in the examination and (1) ordered both NASA and NASAOIG to cease and desist (a) requiring bargaining unit employees to participate in OIG interviews under § 7114(a)(2)(B) without allowing active participation of a union representative, and (b) likewise interfering with, coercing, or restraining employees in exercising their rights under the statute; and (2) directed NASA to (a) order NASAOIG to comply with § 7114(a)(2)(B), and (b) post appropriate notices at the Huntsville facility. <i>NASA,</i> 50 F. L. R. A. 601, 602, 609, 622-623 (1995).</p>
<p>NASA and NASAOIG petitioned for review, asking whether the NASAOIG investigator was a "representative" of NASA, and whether it was proper to grant relief against NASA as well as its OIG. The Court of Appeals upheld the Authority's rulings on both questions and granted the <span class="star-pagination">*233</span> Authority's application for enforcement of its order. <span class="citation multiple-matches"><a href="/c/F.%203d/120/1208/">120 F. 3d 1208</a></span>, 1215-1217 (CA11 1997). Because of disagreement among the Circuit Courts over the applicability of § 7114(a)(2)(B) in such circumstances, see <i>FLRA</i> v. <i>United States Dept. of Justice,</i> <span class="citation" data-id="6964220"><a href="/opinion/7060265/federal-labor-relations-authority-v-us-department-of-justice/" aria-description="Citation for case: Federal Labor Relations Authority v. U.S. Department of...">137 F. 3d 683</a></span> (CA2 1997); <i>United States Dept. of Justice</i> v. <i>FLRA,</i> <span class="citation" data-id="6932702"><a href="/opinion/7030626/united-states-department-of-justice-v-federal-labor-relations-authority/" aria-description="Citation for case: United States Department of Justice v. Federal Labor...">39 F. 3d 361</a></span> (CADC 1994); <i>Defense Criminal Investigative Serv.</i> v. <i>FLRA,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/855/93/">855 F. 2d 93</a></span> (CA3 1988), we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./525/960/">525 U. S. 960</a></span> (1998).</p>
<p></p>
<h2>II</h2>
<p>The FSLMRS provides, in relevant part,</p>
<blockquote>"(2) An exclusive representative of an appropriate unit in an agency shall be given the opportunity to be represented at. . . . .</blockquote>
<blockquote>"(B) any examination of an employee in the unit by a representative of the agency in connection with an investigation if</blockquote>
<blockquote>"(i) the employee reasonably believes that the examination may result in disciplinary action against the employee; and</blockquote>
<blockquote>"(ii) the employee requests representation." <span class="citation no-link">5 U. S. C. § 7114</span>(a).</blockquote>
<p>In this case it is undisputed that the employee reasonably believed the investigation could result in discipline against him, that he requested union representation, that NASA is the relevant "agency," and that, if the provision applies, a violation of § 7114(a)(2)(B) occurred. The contested issue is whether a NASAOIG investigator can be considered a "representative" of NASA when conducting an employee examination covered by § 7114(a)(2)(B).</p>
<p>NASA and its OIG argue that, when § 7114(a)(2)(B) is read in context and compared with the similar right to union representation protected in the private sector by the National Labor Relations Act (NLRA), the term "representative" <span class="star-pagination">*234</span> refers only to a representative of agency management "<i>i. e.,</i> the entity that has a collective bargaining relationship with the employee's union." Brief for Petitioners 13. Neither NASA nor NASAOIG has such a relationship with the employee's union at the Huntsville facility, see <span class="citation no-link">5 U. S. C. § 7112</span>(b)(7) (excluding certain agency investigators and auditors from "appropriate" bargaining units), and so the investigator in this case could not have been a "representative" of the relevant "entity."</p>
<p>By its terms, § 7114(a)(2)(B) is not limited to investigations conducted by certain "entit[ies]" within the agency in question. It simply refers to representatives of "the agency," which, all agree, means NASA. Cf. § 7114(a)(2) (referring to employees "in the unit" and an exclusive representative "of an appropriate unit in an agency"). Thus, relying on prior rulings, the Authority found no basis in the FSLMRS or its legislative history to support the limited reading advocated by NASA and its OIG. The Authority reasoned that adopting their proposal might erode the right by encouraging the use of investigative conduits outside the employee's bargaining unit, and would otherwise frustrate Congress' apparent policy of protecting certain federal employees when they are examined and justifiably fear disciplinary action. 50 F. L. R. A., at 615, and n. 12. That is, the risk to the employee is not necessarily related to which component of an agency conducts the examination. See App. to Pet. for Cert. 65a (information obtained by NASAOIG is referred to agency officials for administrative or disciplinary action).</p>
<p>In resolving this issue, the Authority was interpreting the statute Congress directed it to implement and administer. <span class="citation no-link">5 U. S. C. § 7105</span>. The Authority's conclusion is certainly consistent with the FSLMRS and, to the extent the statute and congressional intent are unclear, we may rely on the Authority's reasonable judgment. See <i>Federal Employees</i> v. <i>Department of Interior,</i> <span class="citation" data-id="9433763"><a href="/opinion/118270/national-federation-of-federal-employees-local-1309-v-department-of-the/#98" aria-description="Citation for case: National Federation of Federal Employees, Local 1309 v....">526 U. S. 86, 98-100</a></span> (1999); <i>Fort Stewart Schools</i> v. <i>FLRA,</i> <span class="citation" data-id="9432024"><a href="/opinion/112437/fort-stewart-schools-v-federal-labor-relations-authority/#644" aria-description="Citation for case: Fort Stewart Schools v. Federal Labor Relations Authority">495 U. S. 641, 644-645</a></span> (1990).</p>
<p><span class="star-pagination">*235</span> Despite the text of the statute and the Authority's views, NASA and NASAOIG advance three reasons for their narrow reading. First, the language at issue is contained in a larger section addressing rights and duties related to collective bargaining; indeed, <span class="citation no-link">5 U. S. C. § 7114</span> is entitled "Representation rights and duties." Thus, other subsections define the union's right to exclusive representation of employees in the bargaining unit, § 7114(a)(1); its right to participate in grievance proceedings, § 7114(a)(2)(A); and its right and duty to engage in good-faith collective bargaining with the agency, §§ 7114(a)(4), (b). That context helps explain why the right granted in § 7114(a)(2)(B) is limited to situations in which the employee "reasonably believes that the examination may result in disciplinary action"a condition restricting the right to union presence or participation in investigatory examinations that do not threaten the witness' employment. We find nothing in this context, however, suggesting that an examination that obviously presents the risk of employee discipline is nevertheless outside the coverage of the section because it is conducted by an investigator housed in one office of NASA rather than another. On this point, NASA's internal organization is irrelevant.</p>
<p>Second, the phrase "representative of the agency" is used in two other places in the FSLMRS where it may refer to representatives of agency management acting in their capacity as actual or prospective parties to a collectivebargaining agreement. One reference pertains to grievances, § 7114(a)(2)(A), and the other to the bargaining process itself, § 7103(a)(12) (defining "collective bargaining"). NASA and NASAOIG submit that the phrase at issue should ordinarily retain the same meaning wherever used in the same statute, and we agree. But even accepting NASA's and NASAOIG's characterization of §§ 7114(a)(2)(A) and 7103(a)(12), the fact that some "representative[s] of the agency" may perform functions relating to grievances and bargaining does not mean that other personnel who conduct <span class="star-pagination">*236</span> examinations covered by § 7114(a)(2)(B) are not also fairly characterized as agency "representative[s]." As an organization, an agency must rely on a variety of representatives to carry out its functions and, though acting in different capacities, each may be acting for, and on behalf of, the agency.</p>
<p>Third, NASA and NASAOIG assert that their narrow construction is supported by the history and purpose of § 7114(a)(2)(B). As is evident from statements by the author of the provision<sup>[1]</sup> as well as similar text in <i>NLRB</i> v. <i>J. Weingarten, Inc.,</i> <span class="citation" data-id="9426000"><a href="/opinion/109194/national-labor-relations-board-v-j-weingarten-inc/" aria-description="Citation for case: National Labor Relations Board v. J. Weingarten, Inc.">420 U. S. 251</a></span> (1975), this section of the FSLMRS was patterned after that decision. In <i>Weingarten,</i> we upheld the National Labor Relations Board's conclusion that an employer's denial of an employee's request to have a union representative present at an investigatory interview, which the employee reasonably believed might result in disciplinary action, was an unfair labor practice. <span class="citation" data-id="9426000"><a href="/opinion/109194/national-labor-relations-board-v-j-weingarten-inc/#252" aria-description="Citation for case: National Labor Relations Board v. J. Weingarten, Inc."><i>Id.,</i> at 252-253, 256</a></span>. We reasoned that the Board's position was consistent with the employee's right under § 7 of the NLRA to engage in concerted activities. <i>Id.,</i> at 260. Given that history, NASA and its OIG contend that the comparable provision in the FSLMRS should be limited to investigations by representatives of that part of agency management with responsibility for collectively bargaining with the employee's union.</p>
<p>This argument ignores the important difference between the text of the NLRA and the text of the FSLMRS. That the general protection afforded to employees by § 7 of the NLRA provided a sufficient basis for the Board's recognition of a novel right in the private sector, see <i>id.,</i> at 260-262, <span class="star-pagination">*237</span> 266-267, does not justify the conclusion that the text of the FSLMRSwhich expressly grants a comparable right to employees in the public sectorshould be narrowly construed to cover some, but not all, interviews conducted by agency representatives that have a disciplinary potential. Congress' specific endorsement of a Government employee's right to union representation by incorporating it in the text of the FSLMRS gives that right a different foundation than if it were merely the product of an agency's attempt to elaborate on a more general provision in light of broad statutory purposes.<sup>[2]</sup> The basis for the right to union representation in this context cannot compel the uncodified limitation proposed by NASA and its OIG.</p>
<p>Employing ordinary tools of statutory construction, in combination with the Authority's position on the matter, we have no difficulty concluding that § 7114(a)(2)(B) is not limited to agency investigators representing an "entity" that collectively bargains with the employee's union.</p>
<p></p>
<h2>III</h2>
<p>Much of the disagreement in this case involves the interplay between the FSLMRS and the IGA. On NASA's and NASAOIG's view, a proper understanding of the IGA precludes treating OIG personnel as "representative[s]" of the agencies they are duty-bound to audit and investigate. They add that the Authority has no congressional mandate or expertise with respect to the IGA, and thus we owe the Authority no deference on this score. It is unnecessary for us to defer, however, because a careful review of the relevant IGA provisions plainly favors the Authority's position.</p>
<p><span class="star-pagination">*238</span> Section 2 of the IGA explains the purpose of the Act and establishes "an office of Inspector General" in each of a list of identified federal agencies, thereby consolidating audit and investigation responsibilities into one agency component. It provides:</p>
<p>"In order to create independent and objective units</p>
<blockquote>"(1) to conduct and supervise audits and investigations relating to the programs and operations of the establishments listed in section 11(2);</blockquote>
<blockquote>"(2) to provide leadership and coordination and recommend policies for activities designed (A) to promote economy, efficiency, and effectiveness in the administration of, and (B) to prevent and detect fraud and abuse in, such programs and operations; and</blockquote>
<blockquote>"(3) to provide a means for keeping the head of the establishment and the Congress fully and currently informed about problems and deficiencies relating to the administration of such programs and operations and the necessity for and progress of corrective action; "there is hereby established in each of such establishments an office of Inspector General." 5 U. S. C. App. § 2, p. 1381.</blockquote>
<p>NASA is one of more than 20 "establishment[s]" now listed in § 11(2).<sup>[3]</sup></p>
<p>Section 3 of the IGA provides that each of the offices created by § 2 shall be headed by an Inspector General appointed by the President, and confirmed by the Senate, "without regard to political affiliation and solely on the basis of integrity and demonstrated ability in accounting, auditing, financial analysis, law, management analysis, public administration, <span class="star-pagination">*239</span> or investigations." § 3(a). Each of these Inspectors General "shall report to and be under the general supervision of the head of the establishment involved or, to the extent such authority is delegated, the officer next in rank below such head," but shall not be subject to supervision by any lesser officer. <i>Ibid.</i> Moreover, an Inspector General's seniors within the agency may not "prevent or prohibit" the Inspector General from initiating or conducting any audit or investigation. <i>Ibid.;</i> see also § 6(a)(2). The President retains the power to remove an Inspector General from office. § 3(b).</p>
<p>Section 4 contains a detailed description of the duties of each Inspector General with respect to the agency "within which his Office is established." § 4(a). Those duties include conducting audits and investigations, recommending new policies, reviewing legislation, and keeping the head of the agency and the Congress "fully and currently informed" through such means as detailed, semiannual reports. §§ 4(a)(1)(5). Pursuant to § 5, those reports must be furnished to the head of the agency, who, in turn, must forward them to the appropriate committee or subcommittee of Congress with such comment as the agency head deems appropriate. § 5(b)(1); see also § 5(d). Section 6 grants the Inspectors General specific authority in a variety of areas to facilitate the mission of their offices. Accordingly, Inspectors General possess discretion to conduct investigations "relating to the administration of the programs and operations of the applicable" agency, § 6(a)(2); the ability to request information and assistance from Government agencies, § 6(a)(3); access to the head of the agency, § 6(a)(6); and the power to hire employees, enter into contracts, and spend congressionally appropriated funds, §§ 6(a)(7), (9); see also § 3(d). Finally, § 9(a)(1)(P) provides for the transfer of the functions previously performed by NASA's "`Management Audit Office' and the `Office of Inspections and Security' " to NASAOIG.</p>
<p><span class="star-pagination">*240</span> The IGA created no central office or officer to supervise, direct, or coordinate the work of all OIG's and their respective staffs. Other than congressional committees (which are the recipients of the reports prepared by each Inspector General) and the President (who has the power to remove an Inspector General), each Inspector General has no supervising authorityexcept the head of the agency of which the OIG is a part. There is no "OIGOIG." Thus, for example, NASAOIG maintains an office at NASA's Huntsville facility, which reports to NASAOIG in Washington, and then to the NASA Administrator, who is the head of the agency. § 11(1); 50 F. L. R. A., at 602.<sup>[4]</sup> In conducting their work, Congress certainly intended that the various OIG's would enjoy a great deal of autonomy. But unlike the jurisdiction of many law enforcement agencies, an OIG's investigative office, as contemplated by the IGA, is performed with regard to, and on behalf of, the particular agency in which it is stationed. See 5 U. S. C. App. §§ 2, 4(a), 6(a)(2). In common parlance, the investigators employed in NASA's OIG are unquestionably "representatives" of NASA when acting within the scope of their employment.</p>
<p>Minimizing the significance of this statutory plan, NASA and NASAOIG emphasize the potentially divergent interests of the OIG's and their parent agencies. To be sure, OIG's maintain authority to initiate and conduct investigations and audits without interference from the head of the agency. § 3(a). And the ability to proceed without consent from agency higher-ups is vital to effectuating Congress' intent and maintaining an opportunity for objective inquiries into bureaucratic waste, fraud, abuse, and mismanagement.<sup>[5]</sup><span class="star-pagination">*241</span> But those characteristics do not make NASAOIG any less a representative of NASA when it investigates a NASA employee. That certain officials within an agency, based on their views of the agency's best interests or their own, might oppose an OIG investigation does not tell us whether the investigators are "representatives" of the agency during the course of their duties. As far as the IGA is concerned, NASAOIG's investigators are employed by, act on behalf of, and operate for the benefit of NASA.</p>
<p>Furthermore, NASA and NASAOIG overstate the inherent conflict between an OIG and its agency. The investigation in this case was initiated by NASA's OIG on the basis of information provided by the FBI, but nothing in the IGA indicates that, if the information had been supplied by the Administrator of NASA rather than the FBI, NASAOIG would have had any lesser obligation to pursue an investigation. See §§ 4(a)(1), (d), 7; S. Rep. No. 95-1071, p. 26 (1978). The statute does not suggest that one can determine whether the OIG personnel engaged in such an investigation are "representatives" of NASA based on the source of the information prompting an investigation. Therefore, it must be NASA's and NASAOIG's position that even when an OIG conducts an investigation in response to a specific request from the head of an agency, an employee engaged in that assignment is not a "representative" of the agency within the meaning of § 7114(a)(2)(B) of the FSLMRS. Such management-prompted investigations are not rare.<sup>[6]</sup></p>
<p><span class="star-pagination">*242</span> Thus, not all OIG examinations subject to § 7114(a)(2)(B) will implicate an actual or apparent conflict of interest with the rest of the agency; and in many cases we can expect honest cooperation between an OIG and management-level agency personnel. That conclusion becomes more obvious when the practical operation of OIG interviews and § 7114(a)(2)(B) rights are considered. The IGA grants Inspectors General the authority to subpoena documents and information, but not witnesses. 5 U. S. C. App. § 6(a)(4). Nor does the IGA allow an OIG to discipline an agency employee, as all parties to this case agree. There may be other incentives for employee cooperation with OIG investigations, but formal sanctions for refusing to submit to an OIG interview cannot be pursued by the OIG alone. Such limitations on OIG authority enhance the likelihood and importance of cooperation between the agency and its OIG. See generally §§ 6(a)(3), (b)(1)(2) (addressing an Inspector General's authority to request assistance from others in the agency, and their duty to respond); §§ 4(a)(5), (d); 50 F. L. R. A., at 616; App. to Pet. for Cert. 65a (noting information sharing between NASAOIG and other agency officials). Thus, if the NASAOIG investigator in this case told the employee that he would face dismissal if he refused to answer questions, 120 F. 3d, at 1210, n. 2, the investigator invoked NASA's authority, not his own.<sup>[7]</sup></p>
<p><span class="star-pagination">*243</span> Considering NASAOIG's statutorily defined role within the agency, we cannot conclude that the proper operation of the IGA requires nullification of § 7114(a)(2)(B) in all OIG examinations.</p>
<p></p>
<h2>IV</h2>
<p>Although NASA's and NASAOIG's narrow reading of the phrase "representative of the agency" is supported by the text of neither the FSLMRS nor the IGA, they also present broaderbut ultimately unpersuasivearguments of policy to defeat the application of § 7114(a)(2)(B) to OIG investigations.</p>
<p>First, NASA and NASAOIG contend that enforcing § 7114(a)(2)(B) in situations similar to this case would undermine NASAOIG's ability to maintain the confidentiality of investigations, particularly those investigations conducted jointly with law enforcement agencies. Cf. 5 U. S. C. App. §§ 5(e)(1)(C), (e)(2) (restricting OIG disclosure of information that is part of an ongoing criminal investigation). NASA and its OIG are no doubt correct in suggesting that the presence of a union representative at an examination will increase the likelihood that its contents will be disclosed to third parties. That possibility is, however, always present: NASA and NASAOIG identify no legal authority restricting an employee's ability to discuss the matter with others. Furthermore, an employee cannot demand the attendance of a union representative when an OIG examination does not involve reasonably apparent potential discipline for that employee. Interviewing an employee who may have information relating to agency maladministration, but who is not himself under suspicion, ordinarily will not trigger the right to union representation. Thus, a variety of OIG investigations and interviewsand many in which confidentiality concerns are heightenedwill not implicate § 7114(a)(2)(B) at all. Though legitimate, NASA's and NASAOIG's confidentiality concerns are not weighty enough to justify a <span class="star-pagination">*244</span> nontextual construction of § 7114(a)(2)(B) rejected by the Authority.</p>
<p>Second, NASA and its OIG submit that, in other instances, the Authority has construed § 7114(a)(2)(B) so broadly that it will impair NASAOIG's ability to perform its investigatory responsibilities. The Authority responds that it has been sensitive to agencies' investigative needs in other cases, and that union representation is unrelated to OIG independence from agency interference. Whatever the propriety of the Authority's rulings in other cases, NASA and NASAOIG elected not to challenge the Authority's conclusion that the NASAOIG examiner's attempt to limit union representative participation constituted an unfair labor practice. To resolve the question presented in this case, we need not agree or disagree with the Authority's various rulings regarding the scope of § 7114(a)(2)(B), nor must we consider whether the outer limits of the Authority's interpretation so obstruct the performance of an OIG's statutory responsibilities that the right must be more confined in this context.<sup>[8]</sup></p>
<p>In any event, the right Congress created in § 7114(a)(2)(B) vindicates obvious countervailing federal policies. It provides a procedural safeguard for employees who are under investigation by their agency, and the mere existence of the right can only strengthen the morale of the federal work force. The interest in fair treatment for employees under <span class="star-pagination">*245</span> investigation is equally strong whether they are being questioned by employees in NASA's OIG or by other representatives of the agency. And, as we indicated in <i>Weingarten,</i>  representation is not the equivalent of obstruction. See <span class="citation" data-id="9426000"><a href="/opinion/109194/national-labor-relations-board-v-j-weingarten-inc/#262" aria-description="Citation for case: National Labor Relations Board v. J. Weingarten, Inc.">420 U. S., at 262-264</a></span>. In many cases the participation of a union representative will facilitate the factfinding process and a fair resolution of an agency investigationor at least Congress must have thought so.</p>
<p>Whenever a procedural protection plays a meaningful role in an investigation, it may impose some burden on the investigators or agency managers in pursuing their mission. We must presume, however, that Congress took account of the policy concerns on both sides of the balance when it decided to enact the IGA and, on the heels of that statute, § 7114(a)(2)(B).<sup>[9]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*246</span> V</h2>
<p>Finally, NASA argues that it was error for the Authority to make NASA itself, as well as NASA's OIG, a party to the enforcement order because NASA has no authority over the manner in which NASAOIG conducts its investigations. However, our conclusion that the investigator in this case was acting as a "representative" of NASA for purposes of § 7114(a)(2)(B) makes it appropriate to charge NASAOIG, as well as the parent agency to which it reports and for which it acts, with responsibility for ensuring that such investigations are conducted in compliance with the FSLMRS. NASA's Administrator retains general supervisory authority over NASA's OIG, 5 U. S. C. App. § 3(a), and the remedy imposed by the Authority does not require NASA to interfere unduly with OIG prerogatives. NASA and NASAOIG offer no convincing reason to believe that the Authority's remedy is inappropriate in view of the IGA, or that it will be ineffective in protecting the limited right of union representation secured by § 7114(a)(2)(B). See generally <span class="citation no-link">5 U. S. C. §§ 706</span>, 7123(c).</p>
<p>The judgment of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>Justice Thomas, with whom The Chief Justice, Justice O'Connor, and Justice Scalia join, dissenting.</p>
<p>In light of the independence guaranteed Inspectors General by the Inspector General Act of 1978, 5 U. S. C. App. § 1 <i>et seq.,</i> p. 1381, investigators employed in the Office of Inspector General (OIG) will not represent agency management in the typical case. There is no basis for concluding, as the Federal Labor Relations Authority (Authority) <span class="star-pagination">*247</span> did, that in this case the investigator from OIG for the National Aeronautics and Space Administration <i>was</i> a "representative of the agency" within the meaning of <span class="citation no-link">5 U. S. C. § 7114</span>(a)(2)(B). I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>The National Aeronautics and Space Administration is headquartered in Washington, D. C. Among other agency subcomponents are the George C. Marshall Space Flight Center (Marshall Center), located in Huntsville, Alabama, and the Office of Inspector General, which is headquartered in Washington, D. C., but maintains offices in all of the agency's other subcomponents, including the Marshall Center. In January 1993, the Federal Bureau of Investigation received information that an employee of the Marshall Center, who is referred to in the record only as "P," was suspected of spying upon and threatening various co-workers. The FBI referred the matter directly to NASA's OIG, and an investigator for that Office who was stationed at the Marshall Center was assigned the case. He contacted P, who agreed to be interviewed so long as his attorney and a union representative were present; the investigator accepted P's conditions. App. to Pet. for Cert. 61a. At the interview, OIG's investigator read certain ground rules, which provided, <i>inter alia,</i> that the union representative was "`not to interrupt the question and answer process.' " <i><span class="citation no-link">Ibid.</span></i><sup>[1]</sup> The union filed an unfair labor practice charge, claiming that the interview was not conducted in accordance with the requirements of <span class="citation no-link">5 U. S. C. § 7114</span>(a)(2)(B), as the Authority has interpreted that provision. The Authority's General Counsel issued a complaint to that effect, and the Authority found that <span class="star-pagination">*248</span> NASA headquarters and NASA's OIG had committed unfair labor practices. On review, the Court of Appeals for the Eleventh Circuit granted the Authority's application for enforcement of its order. <span class="citation multiple-matches"><a href="/c/F.%203d/120/1208/">120 F. 3d 1208</a></span> (1997).</p>
<p>As the Court correctly recognizes, <i>ante,</i> at 233, several points are not in dispute at this stage of the litigation. The fact that P requested union representation and reasonably believed that disciplinary action might be taken against him on the basis of information developed during the examination has never been in dispute in this case. See <i>NASA,</i> 50 F. L. R. A. 601, 606, n. 4 (1995). Although petitioners contested the matter before the Authority, on review in the Eleventh Circuit, they conceded that OIG's investigator conducted the interview of P in a way that did not comport with what § 7114(a)(2)(B) requires. See 120 F. 3d, at 1211. And all parties agree that the relevant "agency" for purposes of § 7114(a)(2)(B) is NASA. One other point is not disputed the "representative" to which § 7114(a)(2)(B) refers must represent agency management, not just the agency in some general sense as the Court suggests, <i>ante,</i> at 233-234, 240. See 50 F. L. R. A., at 614 ("`[R]epresentative of the agency' under section 7114(a)(2)(B) should not be so narrowly construed as to exclude management personnel employed in other subcomponents of the agency"); <i>id.,</i> at 615 ("`We doubt that Congress intended that union representation be denied to the employee solely because the management representative is employed outside the bargaining unit' ") (quoting <i>Defense Criminal Investigative Serv.</i> v. <i>FLRA,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/855/93/">855 F. 2d 93</a></span>, 99 (CA3 1988)); Brief for Respondent FLRA 16 ("The Authority has determined that the phrase `representative of the agency' should not be so narrowly construed as to exclude management personnel, such as the OIG, who are located in other components of the agency"); <i>id.,</i> at 21; Reply Brief for Petitioners 1 ("[A] `representative of the agency' in Section 7114(a)(2)(B) must be a representative of agency <i>management</i> ").</p>
<p><span class="star-pagination">*249</span> Since an agency's stated reasons for decision are important in any case reviewing agency action, I summarize in some detail what the Authority actually said in this case. It began by stating its conclusion:</p>
<blockquote>"We reach this conclusion based upon our determination that: (1) the term `representative of the agency' under section 7114(a)(2)(B) should not be so narrowly construed as to exclude management personnel employed in other subcomponents of the agency; (2) the statutory independence of agency OIGs is not determinative of whether the investigatory interviews implicate section 7114(a)(2)(B) rights; and (3) section 7114(a)(2)(B) and the IG Act are not irreconcilable." 50 F. L. R. A., at 614.</blockquote>
<p>The Authority headed its discussion of its first determination "Section 7114(a)(2)(B) Covers the Actions of Management Personnel Employed in Other Subcomponents of the Agency." <i>Id.,</i> at 615. This statement appears to suggest OIG itself is part of agency management. But the remainder of the Authority's discussion appears to advance a different theoryone that OIG serves as agency management's <i>agent</i> because OIG inspectors ultimately report to NASA's Administrator, see <i>ibid.</i> (OIG's investigator, "although employed in a separate component from the MSFC, is an employee of and ultimately reports to the head of NASA"), and because OIG provides information to management that sometimes results in discipline to union employees, <i>ibid.</i>  ("OIG not only provides investigatory information to NASA [headquarters] but also to other NASA subcomponent offices"); see also <i>id.,</i> at 616 (Congress would regard an OIG investigator as a representative of the agency because "[t]he information obtained during the course of an OIG investigatory examination may be released to, and used by, other subcomponents of NASA to support administrative or disciplinary <span class="star-pagination">*250</span> actions taken against unit employees").<sup>[2]</sup> The Authority recognized that the Inspector General Act grants an Inspector General, or IG, "a degree of freedom and independence from the parent agency." <i>Id.,</i> at 615. It thought, however, that the Inspector General's autonomy "becomes nonexistent" when the IG's investigation concerns allegations of misconduct by agency employees in connection with their work and the information obtained during the investigation possibly would be shared with agency management. <i>Ibid.</i>  As it further explained: "[I]n some circumstances, NASA, OIG <i>performs an investigatory role</i> for NASA [headquarters] and its subcomponents, specifically [the Marshall Center]." <i>Id.,</i> at 616 (emphasis added). Moreover, the Authority reasoned, the Inspector General "plays an integral role in assisting the agency and its subcomponent offices in meeting the agency's objectives." <i>Id.,</i> at 617. In light of all this, the Authority concluded:</p>
<blockquote>"Plainly, the IG represents and safeguards the entire agency's interests when it investigates the actions of the agency's employees. Such activities support, rather than threaten, broader agency interests and make the IG a participant, with other agency components, in meeting various statutory obligations, including the agency's labor relations obligations under the Statute." <i>Ibid.</i> </blockquote>
<p></p>
<h2>
<span class="star-pagination">*251</span> II</h2>
<p>The Authority's recognition that § 7114(a)(2)(B) protections are only triggered when an investigation is conducted by, or on behalf of, agency management, is important and hardly surprising. See, <i>e. g.,</i> 50 F. L. R. A., at 614 ("section 7114(a)(2)(B) should not be so narrowly construed as to exclude <i>management personnel</i> employed in other subcomponents of the agency" (emphasis added)); Brief for Respondent FLRA 21 ("The Authority's conclusion that the word `representative,' or phrase `representative of the agency,' includes <i>management personnel</i> in other subcomponents of the `agency' is entirely consistent with the language of the [Federal Service Labor-Management Relations Statute]" (emphasis added)). It is important because the Court seems to think it enough that NASA's OIG represent NASA in some broad and general sense. But as the Authority's own opinion makes clear, that is not enoughNASA's OIG must represent NASA's management to qualify as a "representative of the agency" within the meaning of § 7114(a)(2)(B). The Authority's position is hardly surprising in that the Federal Service Labor-Management Relations Statute (FSLMRS) plainly means just that.<sup>[3]</sup> The FSLMRS governs labormanagement relations in the federal sector. Section 7114(a)(2)(B) is captioned "[r]epresentation rights and duties," and every employee right contained therein flows from the collective-bargaining relationship.<sup>[4]</sup> As petitioners note, <span class="star-pagination">*252</span> in each of the three instances where the FSLMRS refers to an agency representative, it does so in the context of the collective-bargaining relationship between management and labor. See §§ 7103(a)(12), 7114(a)(2)(A), 7114(a)(2)(B).<sup>[5]</sup></p>
<p>Investigators within NASA's OIG might be "representatives of the agency" in two ways. First, if NASA's Inspector General and NASA's OIG itself were part of agency management, I suppose that employees of the Office necessarily would be representatives of agency management. But, to the extent that the Authority meant to hold that, there is no <span class="star-pagination">*253</span> basis for its conclusion. OIG has no authority over persons employed within the agency outside of its Office and similarly has no authority to direct agency personnel outside of the Office. Inspectors General, moreover, have no authority under the Inspector General Act to punish agency employees, to take corrective action with respect to agency programs, or to implement any reforms in agency programs that they might recommend on their own. See generally <i>Inspector General Authority to Conduct Regulatory Investigations,</i> 13 Op. Off. Legal Counsel 54, 55 (1989); Congressional Research Service, Report for Congress, Statutory Offices of Inspector General: A 20th Anniversary Review 7 (Nov. 1998). The Inspector General is charged with, <i>inter alia,</i> investigating suspected waste, fraud, and abuse, see 5 U. S. C. App. §§ 2, 4, 6, and making policy recommendations (which the agency head is not obliged to accept), see §§ 4(a)(3), (4), but the Inspector General Act bars the Inspector General from participating in the performance of agency management functions, see § 9(a). Moreover, OIG is not permitted to be party to a collective-bargaining relationship. See <span class="citation no-link">5 U. S. C. § 7112</span>(b)(7) (prohibiting "any employee primarily engaged in investigation or audit functions" from participating in a bargaining unit).</p>
<p>Investigators within NASA's OIG might "represent" the agency if they acted as agency management's representativeessentially, if OIG was agency management's agent or somehow derived its authority from agency management when investigating union employees. And something akin to an agency theory appears to be the primary basis for the Authority's decision. The agency theory does have a textual basis§ 7114(a)(2)(B)'s term "representative," as is relevant in this context, can mean "standing for or in the place of another: acting for another or others: constituting the agent for another esp[ecially] through delegated authority," or "one that represents another as agent, deputy, substitute, or delegate usu[ally] being invested with the authority of the principal." <span class="star-pagination">*254</span> Webster's Third New International Dictionary 1926 1927 (1976); see also Webster's New International Dictionary 2114 (2d ed. 1957) ("[b]eing, or acting as, the agent for another, esp. through delegated authority"). The agency notion, though, is counterintuitive, given that, as the majority acknowledges, <i>ante,</i> at 238, the stated purpose of the Inspector General Act was to establish "<i>independent</i> and objective units" within agencies to conduct audits and investigations, see 5 U. S. C. App. § 2 (emphasis added).</p>
<p>To be sure, NASA's OIG is a subcomponent of NASA and the Inspector General is subject to the "general supervision," § 3(a), of NASA's Administrator (or of the "officer next in rank below" the Administrator, <i>ibid.</i> ).<sup>[6]</sup> But, as the Fourth Circuit has observed, it is hard to see how this "general supervision" amounts to much more than "nominal" supervision. See <i>NRC</i> v. <i>FLRA,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/25/229/">25 F. 3d 229</a></span>, 235 (1994). NASA's Inspector General does not depend upon the Administrator's approval to obtain or to keep her job. NASA's Inspector General must be appointed by the President and confirmed by the Senate, "without regard to political affiliation and solely on the basis of integrity and demonstrated ability in accounting, auditing, financial analysis, law, management analysis, public administration, or investigations." 5 U. S. C. App. § 3(a). Only the President, and not NASA's Administrator, may remove the Inspector General, and even then the President must provide Congress with his reasons for doing so. § 3(b).<sup>[7]</sup> In addition, the Administrator has no <span class="star-pagination">*255</span> control over who works for the Inspector General. Inspectors General have the authority to appoint an Assistant Inspector General for Auditing and another Assistant Inspector General for Investigations, §§ 3(d)(1), (2), may "select, appoint, and employ such officers and employees as may be necessary," § 6(a)(7), and also are authorized to employ experts and consultants and enter into contracts for audits, studies, and other necessary services, see §§ 6(a)(8), (9); see generally P. Light, Monitoring Government: Inspectors General and the Search for Accountability 175-185 (1993) (describing the "unprecedented freedom" that IG's have under the Inspector General Act in organizing their offices and how IG's have enhanced their independence by exercising their statutory authority in this regard to the fullest).</p>
<p>Inspectors General do not derive their authority to conduct audits and investigate agency affairs from agency management. They are authorized to do so directly under the Inspector General Act. 5 U. S. C. App. § 2(1). Neither NASA's Administrator, nor any other agency official, may "prevent or prohibit the Inspector General from initiating, carrying out, or completing any audit or investigation, or from issuing any subpoena during the course of any audit or investigation." § 3(a). The Administrator also may not direct the Inspector General to undertake a particular investigation; the Inspector General Act commits to the IG's discretion the decision whether to investigate or report upon the agency's programs and operations. § 6(a)(2). The Authority's counsel argued to the contrary, but could not provide a single example of an instance where an agency head <span class="star-pagination">*256</span> has directed an Inspector General to conduct an investigation in a particular manner. Tr. of Oral Arg. 40, see also <i>id.,</i> at 46-48 (counsel for respondent American Federation of Government Employees (AFGE) also unable to provide an example of agency head direction of OIG investigation). The Authority's counsel also could not support his assertion that agency heads have the power to direct the Inspector General to comply with laws such as the FSLMRS. <i>Id.,</i> at 41-43.</p>
<p>Inspectors General, furthermore, are provided a broad range of investigatory powers under the Act. They are given access to "all records, reports, audits, reviews, documents, papers, recommendations, or other material" of the agency. 5 U. S. C. App. § 6(a)(1). They may issue subpoenas to obtain such information if necessary, and any such subpoena is enforceable by an appropriate United States district court. § 6(a)(4).<sup>[8]</sup> The Inspector General also may "administer to or take from any person an oath, affirmation, or affidavit, whenever necessary." § 6(a)(5). Inspectors General do not have the statutory authority to compel an employee's attendance at an interview. But if an employee refuses to attend an interview voluntarily, the Inspector General may request assistance, § 6(a)(3), and the agency head "shall . . . furnish . . . information or assistance" to OIG, § 6(b)(1).</p>
<p>NASA's Inspector General does, as the Authority claimed, provide information developed in the course of her audits and investigations to the Administrator. §§ 2(3), 4(a)(5). But she has outside reporting obligations as well. Inspectors General must prepare semiannual reports to Congress "summarizing the activities of the Office." § 5. Those reports first are delivered to the agency head, § 5(b), and the Administrator may add comments to the report, § 5(b)(1), but <span class="star-pagination">*257</span> the Administrator may not prevent the report from going to Congress and may not change or order the Inspector General to change his report. Moreover, the Inspector General must notify the Attorney General directly, <i>without notice to other agency officials,</i> upon discovery of "reasonable grounds to believe there has been a violation of Federal criminal law." § 4(d).</p>
<p>As a practical matter, the Inspector General's independence from agency management is understood by Members of Congress and Executive Branch officials alike. This understanding was on display at the recent congressional hearing on the occasion of the Inspector General Act's 20th anniversary. For example, Senator Thompson, Chairman of the Senate Government Affairs Committee, stated that "[t]he overarching question we need to explore is whether the Executive Branch is providing IGs with support and attention adequate to ensure their independence and effectiveness." Hearings on "The Inspector General Act: 20 Years Later" before the Senate Committee on Governmental Affairs, 105th Cong., 2d Sess., 2 (1998). He further explained that "[t]he IGs . . . are paid to give [Congress] an independent and objective version [of] events." <i>Ibid.</i> Senator Glenn, then the ranking minority member, opined that "the IG's first responsibility continues to be program and fiscal integrity; they are not `tools' of management." <i>Id.,</i> at 7.</p>
<p>At those hearings, testimony was received from several Inspectors General. June Gibbs Brown, the Inspector General for the United States Department of Health and Human Services, praised Secretary Shalala for "never, not even once, [seeking] to encroach on [her] independence." <i>Id.,</i> at 4. In her written testimony, she offered: "A key component of OIG independence is our direct communication with the Members and staff of the Congress. Frankly, I suspect that no agency head relishes the fact that IGs have, by law, an independent relationship with oversight Committees. Information can and must go directly from the Inspectors General <span class="star-pagination">*258</span> to the Hill, without prior agency and administration clearance." <i>Id.,</i> at 45. The testimony of Susan Gaffney, the Inspector General for the United States Department of Housing and Urban Development, revealed that agency managers know all too well that the Inspector General is independent of agency management:</p>
<blockquote>"[I]t is to me somewhat jolting, maybe shocking, that the current Secretary of HUD has exhibited an extremely hostile attitude toward the independence of the HUD OIG, and, as I have detailed in my written testimony, he has, in fact, let this hostility lead to a series of attacks and dirty tricks against the HUD OIG." <i>Id.,</i> at 6.</blockquote>
<p>In her written testimony, Ms. Gaffney further explained that, while, "[i]deally, the relationship between an IG and the agency head is characterized by mutual respect, a common commitment to the agency mission, and a thorough understanding and acceptance of the vastly different roles of the IG and the agency head," the current Secretary, in her view, was "uncomfortable with the concept of an independent Inspector General who is not subject to his control and who has a dual reporting responsibility." <i>Id.,</i> at 48-49.</p>
<p>The Authority essentially provided four reasons why OIG represented agency management in this case: because OIG is a subcomponent of NASA and subject to the "general supervision" of its Administrator; because it provides information obtained during the course of its investigations to NASA headquarters and its subcomponents; because that information is sometimes used for administrative and disciplinary purposes; and because OIG's functions support broader agency objectives. In my view, the fact that OIG is housed in the agency and subject to supervision (an example of which neither the Authority nor the Court can provide) is an insufficient basis upon which to rest the conclusion that OIG's employees are "representatives" of agency management. It is hard to see how OIG serves as agency management's agent <span class="star-pagination">*259</span> or representative when the Inspector General is given the discretion to decide whether, when, and how to conduct investigations. See 5 U. S. C. App. §§ 3(a), 6(a).<sup>[9]</sup></p>
<p>The fact that information obtained in the course of OIG interviews is shared with agency management and sometimes forms the basis for employee discipline is similarly unimpressive. The Court suggests that when this happens, OIG and agency management act in "concert." <i>Ante,</i> at 242, n. 7. The truth of the matter is that upon receipt of information from OIG, agency management has the <i>discretion</i> to impose discipline but it need not do so. And OIG has no determinative role in agency management's decision. See 5 U. S. C. App. § 9(a) (Inspector General may not participate in the performance of agency management functions). Although OIG may provide information developed in the course of an investigation to agency management, so, apparently, does the FBI, the DEA, and local police departments. See, <i>e. g.,</i> <span class="citation no-link">63 Fed. Reg. 8682</span> (1998) (FBI's disclosure policy); <span class="citation no-link">62 Fed. Reg. 36572</span> (1997) (Immigration and Naturalization Service (INS) Alien File and Central Index System); <span class="citation no-link">62 Fed. Reg. 26555</span> (1997) (INS Law Enforcement Support Center <span class="star-pagination">*260</span> Database); <span class="citation no-link">61 Fed. Reg. 54219</span> (1996) (DEA); <span class="citation no-link">60 Fed. Reg. 56648</span> (1995) (Secret Service, Bureau of Alcohol, Tobacco, and Firearms, and other Treasury components); <span class="citation no-link">60 Fed. Reg. 18853</span> (1995) (United States Marshals Service (USMS)); <span class="citation no-link">54 Fed. Reg. 42060</span> (1989) (FBI, USMS, and various Department of Justice record systems); see also <span class="citation no-link">31 CFR § 1.36</span> (1998) (listing routine uses and other exemptions in disclosure of Treasury agencies' records). Surely it would not be reasonable to consider an FBI agent to be a "representative" of agency management just because information developed in the course of his investigation of a union employee may be provided to agency management. Merely providing information does not establish an agency relationship between management and the provider.</p>
<p>Similarly, the fact that OIG may promote broader agency objectives does not mean that it acts as management's agent. To be sure, as the Court points out, <i>ante,</i> at 240, OIG's mission is to conduct audits and investigations of the <i>agency's</i>  programs and operations. See 5 U. S. C. App. §§ 2, 4(a). But just because two arms of the same agency work to promote overall agency concerns does not make one the other's representative. In any event, OIG serves more than just agency concerns. It also provides the separate function of keeping Congress aware of agency developments, a function that is of substantial assistance to the congressional oversight function.</p>
<p>The Court mentions, <i>ante,</i> at 242, that the Inspector General lacks the authority to compel witnesses to appear at an interview as if that provided support for the Authority's decision. Perhaps it is of the view that because the Inspector General must rely upon the agency head to compel an employee's attendance at an interview, management's authority is somehow imputed to OIG, or OIG somehow derives its authority from the agency. This proposition seems dubious at best. The Inspector General is provided the authority to investigate under the Inspector General Act, and is <span class="star-pagination">*261</span> given power to effectuate her responsibilities through, <i>inter alia,</i> requesting assistance as may be necessary in carrying out her duties. 5 U. S. C. App. § 6(a)(3). The head of the agency must furnish information and assistance to the IG, "insofar as is practicable and not in contravention" of law. § 6(b)(1). Perhaps, then, when agency management directs an employee to appear at an OIG interview, <i>management</i>  acts as OIG's agent.</p>
<p>The proposition seems especially dubious in this case, as P <i>agreed</i> to be interviewed. The record does not reveal that NASA's management compelled him to attend the interview nor does it reveal that P was threatened with discipline if he did not attend the interview. The Eleventh Circuit, to be sure, indicated that OIG's investigator threatened P with discipline if he did not answer the questions put to him. But that threat, assuming it indeed was made, had little to do with attendance and more to do with the conduct of the interview. As the Authority has interpreted § 7114(a)(2)(B), as the Court notes, <i>ante,</i> at 242, n. 7, no unfair labor practice is committed if an employee who requests representation is given the choice of proceeding without representation and discontinuing the interview altogether. Perhaps it could be argued that by threatening P with discipline ifhe did not answer the questions put to him, rather than giving P the choice of proceeding without representation, that OIG's investigator invoked agency management's authority to compel (continued) attendance. Along those lines, respondent AFGE contends that OIG's representative must have been acting for agency management by threatening P with discipline because only NASA's Administrator and his delegates, <span class="citation no-link">5 U. S. C. § 302</span>(b)(1); <span class="citation no-link">42 U. S. C. § 2472</span>(a), have the authority to discipline agency employees. Brief for Respondent AFGE 15-16. If OIG's investigator did mention that P could face discipline, he was either simply stating a fact or clearly acting ultra vires. OIG has no authority to discipline or otherwise control agency employees. Since the mere invocation <span class="star-pagination">*262</span> of agency management's authority is not enough to vest that authority with OIG's investigator, the argument, then, must be that it was reasonable for P to believe that OIG's investigator might have the ability to exercise agency management's authority. That is a question we simply cannot answer on this record. And more important, I do not think that § 7114(a)(2)(B) can be read to have its applicability turn on an after-the-fact assessment of interviewees' subjective perceptions, or even an assessment of their reasonable beliefs.</p>
<p></p>
<h2>* * *</h2>
<p>In light of the Inspector General's independenceguaranteed by statute and commonly understood as a practical realityan investigator employed within NASA's OIG will not, in the usual course, represent NASA's management within the meaning of § 7114(a)(2)(B). Perhaps there are exceptional cases where, under some unusual combination of facts, investigators of the OIG might be said to represent agency management, as the statute requires. Cf. <i>FLRA</i> v. <i>United States Dept. of Justice,</i> <span class="citation" data-id="6964220"><a href="/opinion/7060265/federal-labor-relations-authority-v-us-department-of-justice/#690" aria-description="Citation for case: Federal Labor Relations Authority v. U.S. Department of...">137 F. 3d 683, 690-691</a></span> (CA2 1997) ("So long as the OIG agent is questioning an employee for bona fide purposes within the authority of the [Inspector General Act] and not merely accommodating the agency by conducting interrogation of the sort traditionally performed by agency supervisory staff in the course of carrying out their personnel responsibilities, the OIG agent is not a `representative' of the employee's agency for purposes of section 7114(a)(2)(B)"), cert. pending, No. 98-667. This case, however, certainly does not present such facts. For the foregoing reasons, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   <i>Gregory O'Duden</i> and <i>Barbara A. Atkin</i> filed a brief for the National Treasury Employees Union as <i>amicus curiae</i> urging affirmance.</p>
<p>[1]  Congressman Udall, whose substitute contained the section at issue, explained that the "provisions concerning investigatory interviews reflect the . . . holding in" <i>Weingarten.</i> 124 Cong. Rec. 29184 (1978); Legislative History of the Federal Service Labor-Management Relations Statute, Title VII of the Civil Service Reform Act of 1978 (Committee Print compiled for the House Subcommittee on Postal Personnel and Modernization of the Committee on Post Office and Civil Service), Ser. No. 96-7, p. 926 (1979) (hereinafter FSLMRS Leg. Hist.); see <i>NASA,</i> 50 F. L. R. A. 601, 606 (1995).</p>
<p>[2]  See <i>id.,</i> at 608, n. 5 (Congress recognized that the right to union representation might evolve differently in the federal and private sectors); H. R. Conf. Rep. No. 95-1717, p. 156 (1978), FSLMRS Leg. Hist. 824; cf. <i>Karahalios</i> v. <i>Federal Employees,</i> <span class="citation" data-id="112214"><a href="/opinion/112214/karahalios-v-national-federation-of-federal-employees-local-1263/#534" aria-description="Citation for case: Karahalios v. National Federation of Federal Employees,...">489 U. S. 527, 534</a></span> (1989) (the FSLMRS "is not a carbon copy of the NLRA").</p>
<p>[3]  Such establishments are described as "agencies" in other federal legislation, such as the FSLMRS. See <span class="citation no-link">5 U. S. C. §§ 101-105</span>, 7103(a)(3). Note also that other OIG's were created by subsequent amendments to the IGA and may be structured differently than those OIGs, such as NASA's, discussed in the text. See, <i>e. g.,</i> 5 U. S. C. App. §§ 8, 8E, 8G.</p>
<p>[4]  At oral argument, NASA and NASAOIG indicated that the Administrator's general supervision authority includes the ability to require its Inspector General to comply with, <i>inter alia,</i> equal employment opportunity regulations. Tr. of Oral Arg. 5.</p>
<p>[5]  See § 2; S. Rep. No. 95-1071, pp. 1, 5-7, 9 (1978); H. R. Rep. No. 95-584, pp. 2, 5-6 (1977).</p>
<p>[6]  See, <i>e. g., United States INS,</i> 46 F. L. R. A. 1210, 1226-1231 (1993), review den. <i>sub nom. American Federation of Govt. Employees, AFL CIO, Local 1917</i> v. <i>FLRA,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/22/1184/">22 F. 3d 1184</a></span> (CADC 1994); <i>United States Dept. of Justice, INS,</i> 46 F. L. R. A. 1526, 1549 (1993), review granted <i>sub nom. </i><i>United States Dept. of Justice</i> v. <i>FLRA,</i> <span class="citation" data-id="6932702"><a href="/opinion/7030626/united-states-department-of-justice-v-federal-labor-relations-authority/" aria-description="Citation for case: United States Department of Justice v. Federal Labor...">39 F. 3d 361</a></span> (CADC 1994); <i>Department of Defense, Defense Criminal Investigative Serv.,</i> 28 F. L. R. A. 1145, 1157-1159 (1987), enf'd <i>sub nom. </i><i>Defense Criminal Investigative Serv.</i> v. <i>FLRA,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/855/93/">855 F. 2d 93</a></span> (CA3 1988); see also <i>Martin</i> v. <i>United States,</i>  <span class="citation" data-id="6826764"><a href="/opinion/6930374/martin-v-united-states/#740" aria-description="Citation for case: Martin v. United States">20 Cl. Ct. 738, 740-741</a></span> (1990).</p>
<p>[7]  In fact, a violation of § 7114(a)(2)(B) seems less likely to occur when the agency and its OIG are not acting in concert. Under the Authority's construction of the FSLMRS, when an employee within the unit makes a valid request for union representation, an OIG investigator does <i>not</i> commit an unfair labor practice by (1) halting the examination, or (2) offering the employee a choice between proceeding without representation and discontinuing the examination altogether. <i>United States Dept. of Justice, Bureau of Prisons,</i> 27 F. L. R. A. 874, 879-880 (1987); see also <i>NLRB</i> v. <i>J. Weingarten, Inc.,</i> <span class="citation" data-id="9426000"><a href="/opinion/109194/national-labor-relations-board-v-j-weingarten-inc/#258" aria-description="Citation for case: National Labor Relations Board v. J. Weingarten, Inc.">420 U. S. 251, 258-260</a></span> (1975). Disciplining an employee for his or her choice to demand union participation or to discontinue an examination would presumably violate the statute, but such responses require more authority than Congress granted the OIG's in the IGA.</p>
<p>[8]  The same can be said of NASA's and NASAOIG's concerns that the reach of § 7114(a)(2)(B) will become the subject of collective bargaining between agencies and unions, or hinder joint or independent FBI investigations of federal employees. See <i>United States Nuclear Regulatory Comm'n</i> v. <i>FLRA,</i> <span class="citation multiple-matches"><a href="/c/F.%203d/25/229/">25 F. 3d 229</a></span> (CA4 1994) (adopting the agency's position that it could not bargain over certain procedures by which its OIG conducts investigatory interviews); 50 F. L. R. A., at 616, n. 13 (distinguishing FBI investigations). The process by which the scope of § 7114(a)(2)(B) may properly be determined, and the application of that section to law enforcement officials with a broader charge, present distinct questions not now before us.</p>
<p>[9]  The dissent does not dispute much of our analysis; it indicates that NASAOIG is an "ar[m]" of NASA "work[ing] to promote overall agency concerns." <i>Post,</i> at 260. The dissent's premise is that the Authority determined that the phrase "representative of the agency" means "representative of . . . agency [management]," and that this issue is now uncontested. See <i>post,</i> at 246-247, 248-259, 262. But see <i>post,</i> at 251, n. 3. Putting aside the fact that NASA's and NASAOIG's construction of the statutehowever one interprets their argumentis very much in dispute, see Brief for Respondent American Federation of Government Employees, AFLCIO 26-32; Brief for Respondent FLRA 23-25, 31, and the rule that litigants cannot bind us to an erroneous interpretation of federal legislation, see <i>Roberts</i> v. <i>Galen of Va., Inc.,</i> <span class="citation" data-id="1637175"><a href="/opinion/1637175/roberts-v-galen-of-virginia-inc/#253" aria-description="Citation for case: Roberts v. Galen of Virginia, Inc.">525 U. S. 249, 253</a></span> (1999), we have ignored neither the actual rationale of the Authority's decision in this case nor NASA's and NASAOIG's arguments before this Court. Focusing on its plain reasoning, we cannot fairly read the Authority's decision as turning on whether NASA "management" was involved. The Authority emphasized that FSLMRS rights do not depend on "the organizational entity within the agency to whom the person conducting the examination reports"; and in discussing NASAOIG's role within the agency, the Authority's decision repeatedly refers to NASA headquarters together with its componentsthat is, to the agency as a whole. 50 F. L. R. A., at 615-616; <i>id.,</i> at 621 (noting "the investigative role that OIG's perform for the agency" and concluding that NASAOIG "represents" not only its own interests, "but ultimately NASA [headquarters] and its subcomponent offices"). Nowhere did the Authority rely on the assertion that OIG's act as "agency management's agent," a term coined by the dissent. <i>Post,</i>  at 253.</p>
<p>[1]  It appears that OIG's inspector informed P that he would face dismissal if he did not answer the questions put to him. See <span class="citation multiple-matches"><a href="/c/F.%203d/120/1208/">120 F. 3d 1208</a></span>, 1210, n. 2 (CA11 1997).</p>
<p>[2]  The Authority also relied on a policy ground here. It asserted that there was "no basis in the Statute or itslegislative history to make the existence of [the representational rights provided by § 7114] dependent upon the organizational entity within the agency to whom the person conducting the examination reports." 50 F. L. R. A., at 615. It elaborated, in a footnote, that "[i]f such were the case, agencies could abridge bargaining unit rights and evade statutory responsibilities under section 7114(a)(2)(B), and thus thwart the intent of Congress, by utilizing personnel from other subcomponents (such as the OIG) to conduct investigative interviews of bargaining unit employees." <i>Id.,</i> at 615, n. 12.</p>
<p>[3]  Although it is significant that the Authority recognized below and recognizes here that the statutory phrase "representative of the agency" refers to a representative of agency management, I do not, as the Court asserts, <i>ante,</i> at 245-246, n. 9, rest the argument on the premise that the point is conceded. Rather, in light of the context in which the phrase appears, and in light of the very subject matter of the statute, the phrase plainly has that meaning.</p>
<p>[4]  Section 7114(a)(1) details what "[a] labor organization which has been accorded exclusive recognition" is entitled to and must do; § 7114(a)(2) indicates when an exclusive representative may be present at discussions or examinations conducted by agency management; § 7114(a)(3) requires agency management annually to inform its employees of their rights under § 7114(a)(2)(B); § 7114(a)(4) obligates management and the exclusive representative to bargain in good faith for purposes of arriving at a collectivebargaining agreement; § 7114(a)(5) provides that the rights of an exclusive representative do not limit an employee's right to seek other representation, for example, legal counsel; § 7114(b) speaks to the duty of good faith imposed on management and the exclusive representative under § 7114(a)(4); and § 7114(c) requires the head of the agency to approve all collective-bargaining agreements.</p>
<p>[5]  I disagree with the Court as to the proper reading of petitioners' argument that the phrase "representative of the agency" refers only to the entity that has a collective-bargaining relationship with a union. I do not take petitioners to mean that OIG's representative did not represent the "agency," NASA, for the simple reason that only Space Center management had a collective-bargaining relationship with P's union. If that were truly petitioners' view, its later argument that OIG cannot represent NASA because the IG is substantially independent from the agency head would not make senseit would be enough for petitioners to argue that OIG is not under the control of the Marshall Center's management. Rather, as petitioners make clear in their reply brief, they are simply arguing that "a `representative of the agency' must be a representative of agency management, as opposed to just another employee." Reply Brief for Petitioners 2, and n. 4. It appears that they would agree, in accordance with the Authority's precedent, see, <i>e. g., Air Force Logistics Command,</i> 46 F. L. R. A. 1184, 1186 (1993); <i>Department of Health and Human Services,</i> 39 F. L. R. A. 298, 311-312 (1991), that NASA headquarters also qualifies as agency management under the FSLMRS, even though it lacks a direct collective-bargaining relationship with a union, because it directs its subordinate managers who have such a collective-bargaining relationship.</p>
<p>[6]  The Act provides that the Inspector General "shall not report to, or be subject to supervision by," any other agency officer. 5 U. S. C. App. § 3(a).</p>
<p>[7]  The Court, <i>ante,</i> at 240, does not report the full story with respect to Inspector General supervision. We were told at oral argument that Executive Order 12993, 3 CFR 171 (1996), governs the procedures to be followed in those instances where the Inspector General and NASA's Administrator are in conflict. Tr. of Oral Arg. 51-52. Complaints against an Inspector General are referred to a body known as the "Integrity Committee," which is composed "of at least the following members": an official of the FBI, who serves as Chair of the Integrity Committee; the Special Counsel of the Office of Special Counsel; the Director of the Office of Government Ethics; and three or more Inspectors General, representing both the President's Council on Integrity and Efficiency and the Executive Council on Integrity and Efficiency. The Chief of the Public Integrity Section of the Criminal Division of the Department of Justice, or his designee, serves as an advisor to the Integrity Committee with respect to its responsibilities and functions under the Executive Order.</p>
<p>[8]  The Inspector General, however, does not have the authority to subpoena documents and information from other federal agencies. See 5 U. S. C. App. §§ 6(a)(4), 6(b)(1).</p>
<p>[9]  The Court posits, <i>ante,</i> at 241, that "nothing in the [Inspector General Act] indicates that, if the information had been supplied by the Administrator of NASA rather than the FBI, NASAOIG would have had any lesser obligation to pursue an investigation." It appears shocked at the proposition that petitioners might think that "even when an OIG conducts an investigation in response to a specific request from the head of an agency, an employee engaged in that assignment is not a `representative' of the agency within the meaning of [5 U. S. C.] § 7114(a)(2)(B)." <i>Ibid.</i>  The answer to the Court is quite simple. So far as the Inspector General Act reveals, OIG has no obligation to pursue any particular investigation. And presumably the Court would agree that if NASA's Administrator referred a matter to the FBI or the Drug Enforcement Administration (DEA) (who also, we are told, rely on agency management to compel an employee's appearance at an interview, Reply Brief for Petitioners 5-6), those independent agencies would not "represent" the agency. I fail to see how it is different when the investigatory unit, although independent from agency management, is housed within the agency.</p>

</div>
```

---

## GROUP: content/cases/Napue v. Illinois.md  (`case`, 5 assertions)

### content_page

```
---
title: "Napue v. Illinois"
type: case
citation: "360 U.S. 264 (1959)"
parallel_cite: "79 S. Ct. 1173; 3 L. Ed. 2d 1217"
neutral_cite: 1959 U.S. LEXIS 811
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1959-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Napue v. Illinois
  varies_by_point: false
  scope_note: "Foundational false-testimony due-process rule; carried into the Giglio line; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105912/napue-v-illinois/"
  cluster_id: 105912
  opinion_id: 105912
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Giglio v. United States]]", "[[Brady v. Maryland]]", "[[Mooney v. Holohan]]"]
aliases: []
tags: ["case", "due-process", "false-testimony", "brady-giglio", "credibility"]
holding: "The State may not knowingly use false testimony to obtain a conviction, and that duty applies even when the false testimony goes only to…"
lake:
  record_id: Napue v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Napue v. Illinois

*360 U.S. 264 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At Napue's murder trial, the State's key witness — an accomplice already convicted of the same murder — falsely testified that he had received no promise of consideration in exchange for his testimony, when in fact the prosecutor had promised to help him. The prosecutor knew the testimony was false and did nothing to correct it.

## Issue
Whether the knowing use of false testimony violates due process even when the falsehood goes only to the witness's credibility rather than directly to the defendant's guilt.

## Rule
Yes. "[I]t is established that a conviction obtained through use of false evidence, known to be such by representatives of the State, must fall under the Fourteenth Amendment." — 360 U.S. at 269. ^pin-269

That principle "does not cease to apply merely because the false testimony goes only to the credibility of the witness," because the jury's estimate of a witness's truthfulness may be determinative of guilt or innocence. — *Id.* ^pin-269b

The duty applies as well when the State, though it did not solicit the false testimony, allows it to go uncorrected when it appears.

## Application
The accomplice's false denial of any deal went only to his credibility, but because the jury's assessment of his truthfulness could be determinative and the prosecutor knowingly allowed the false testimony to stand uncorrected, the conviction could not stand on these facts. The judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]]: the prosecution's knowing use of the uncorrected false testimony violated due process.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Napue* is foundational to the prosecutorial-duty line later developed in [[Giglio v. United States]] and synthesized with [[Brady v. Maryland]]'s disclosure rule.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Napue v. Illinois*, 360 U.S. 264 (1959) — https://www.courtlistener.com/opinion/105912/napue-v-illinois/ — pinpoint: 269.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "57b402bb4d41067c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "360 U.S. 264 (1959)", "court": "U.S. Supreme Court", "neutral_cite": "1959 U.S. LEXIS 811", "official_citation_present": true, "parallel_cite": "79 S. Ct. 1173; 3 L. Ed. 2d 1217", "title": "Napue v. Illinois", "year": "1959"}}
{"assertion_id": "cfadc05fce5afcae", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Napue v. Illinois"}}
{"assertion_id": "daeac45d58cea52b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The State may not knowingly use false testimony to obtain a conviction, and that duty applies even when the false testimony goes only to…", "title": "Napue v. Illinois"}}
{"assertion_id": "b65c2e32d90742ee", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1959-06-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Napue v. Illinois", "field_i_validity": "good_law", "scope_note": "Foundational false-testimony due-process rule; carried into the Giglio line; good law.", "title": "Napue v. Illinois", "varies_by_point": "false"}}
{"assertion_id": "d4f1cf8e60530be0", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Napue v. Illinois"}}
```

### lake record — Napue v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Napue v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Napue v. Illinois",
    "case_name_short": "Napue",
    "case_name_full": "Napue v. Illinois",
    "input_case_name": "Napue v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-06-15",
    "year": 1959,
    "docket": null,
    "cluster_id": 105912,
    "lead_opinion_id": 105912,
    "sibling_ids": [
      105912
    ],
    "absolute_url": "/opinion/105912/napue-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "360 U.S. 264",
      "volume": "360",
      "reporter": "U.S.",
      "page": "264",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "79 S. Ct. 1173",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1173",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1217",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1217",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 811",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "811",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "360 U.S. 264",
        "volume": "360",
        "reporter": "U.S.",
        "page": "264",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 S. Ct. 1173",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1173",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1217",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1217",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 811",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "811",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "360 U.S. 264",
    "official_selection": {
      "court_class": "scotus",
      "selected": "360 U.S. 264",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-269",
      "page": null,
      "quote": "--- # Napue v. Illinois *360 U.S. 264 (1959)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background At Napue's murder trial, the State's key witness \u2014 an accomplice already convicted of the same murder \u2014 falsely testified that he had received no promise of consideration in exchange for his testimony, when in fact the prosecutor had promised to help him. The prosecutor knew the testimony was false and did nothing to correct it. ## Issue Whether the knowing use of false testimony violates due process even when the falsehood goes only to the witness's credibility rather than directly to the defendant's guilt. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-269b",
      "page": null,
      "quote": "does not cease to apply merely because the false testimony goes only to the credibility of the witness,",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1959-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Napue v. Illinois",
    "varies_by_point": false,
    "scope_note": "Foundational false-testimony due-process rule; carried into the Giglio line; good law.",
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
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schmitt v. State",
          "cluster_id": 10680344,
          "cite": [
            "901 S.E.2d 102",
            "318 Ga. 835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sosa",
          "cluster_id": 9447945,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In the Matter of a Grand Jury Investigation",
          "cluster_id": 4783492,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brady v. Maryland",
          "cluster_id": 106598,
          "cite": [
            "10 L. Ed. 2d 215",
            "83 S. Ct. 1194",
            "373 U.S. 83",
            "1963 U.S. LEXIS 1615"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Bagley",
          "cluster_id": 111514,
          "cite": [
            "87 L. Ed. 2d 481",
            "105 S. Ct. 3375",
            "473 U.S. 667",
            "1985 U.S. LEXIS 130",
            "53 U.S.L.W. 5084"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wade",
          "cluster_id": 107486,
          "cite": [
            "18 L. Ed. 2d 1149",
            "87 S. Ct. 1926",
            "388 U.S. 218",
            "1967 U.S. LEXIS 1085"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Imbler v. Pachtman",
          "cluster_id": 109387,
          "cite": [
            "47 L. Ed. 2d 128",
            "96 S. Ct. 984",
            "424 U.S. 409",
            "1976 U.S. LEXIS 25"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
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
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Giglio v. United States",
          "cluster_id": 108471,
          "cite": [
            "31 L. Ed. 2d 104",
            "92 S. Ct. 763",
            "405 U.S. 150",
            "1972 U.S. LEXIS 83"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Agurs",
          "cluster_id": 109506,
          "cite": [
            "49 L. Ed. 2d 342",
            "96 S. Ct. 2392",
            "427 U.S. 97",
            "1976 U.S. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Santobello v. New York",
          "cluster_id": 108416,
          "cite": [
            "30 L. Ed. 2d 427",
            "92 S. Ct. 495",
            "404 U.S. 257",
            "1971 U.S. LEXIS 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Strickler v. Greene",
          "cluster_id": 118307,
          "cite": [
            "144 L. Ed. 2d 286",
            "119 S. Ct. 1936",
            "527 U.S. 263",
            "1999 U.S. LEXIS 4191"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Donnelly v. DeChristoforo",
          "cluster_id": 109024,
          "cite": [
            "40 L. Ed. 2d 431",
            "94 S. Ct. 1868",
            "416 U.S. 637",
            "1974 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Marion",
          "cluster_id": 108420,
          "cite": [
            "30 L. Ed. 2d 468",
            "92 S. Ct. 455",
            "404 U.S. 307",
            "1971 U.S. LEXIS 4"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Phillips",
          "cluster_id": 110645,
          "cite": [
            "71 L. Ed. 2d 78",
            "102 S. Ct. 940",
            "455 U.S. 209",
            "1982 U.S. LEXIS 69"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Trombetta",
          "cluster_id": 111206,
          "cite": [
            "81 L. Ed. 2d 413",
            "104 S. Ct. 2528",
            "467 U.S. 479",
            "1984 U.S. LEXIS 103",
            "52 U.S.L.W. 4744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Youngblood",
          "cluster_id": 112156,
          "cite": [
            "102 L. Ed. 2d 281",
            "109 S. Ct. 333",
            "488 U.S. 51",
            "1988 U.S. LEXIS 5404"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Green",
          "cluster_id": 108189,
          "cite": [
            "26 L. Ed. 2d 489",
            "90 S. Ct. 1930",
            "399 U.S. 149",
            "1970 U.S. LEXIS 14"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
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
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hinkson",
          "cluster_id": 1191667,
          "cite": [
            "585 F.3d 1247",
            "2009 U.S. App. LEXIS 24358",
            "2009 WL 3645003"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffa v. United States",
          "cluster_id": 107318,
          "cite": [
            "17 L. Ed. 2d 374",
            "87 S. Ct. 408",
            "385 U.S. 293",
            "1966 U.S. LEXIS 2778"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boyde v. California",
          "cluster_id": 112386,
          "cite": [
            "108 L. Ed. 2d 316",
            "110 S. Ct. 1190",
            "494 U.S. 370",
            "1990 U.S. LEXIS 1180"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estes v. Texas",
          "cluster_id": 107083,
          "cite": [
            "14 L. Ed. 2d 543",
            "85 S. Ct. 1628",
            "381 U.S. 532",
            "1965 U.S. LEXIS 2339",
            "1 Media L. Rep. (BNA) 1187",
            "6 Rad. Reg. 2d (P & F) 2104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burgett v. Texas",
          "cluster_id": 107540,
          "cite": [
            "19 L. Ed. 2d 319",
            "88 S. Ct. 258",
            "389 U.S. 109",
            "1967 U.S. LEXIS 266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coleman",
          "cluster_id": 2115945,
          "cite": [
            "701 N.E.2d 1063",
            "183 Ill. 2d 366",
            "233 Ill. Dec. 789",
            "1998 Ill. LEXIS 938"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
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
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 108613,
          "cite": [
            "33 L. Ed. 2d 706",
            "92 S. Ct. 2562",
            "408 U.S. 786",
            "1972 U.S. LEXIS 23"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Banks v. Dretke",
          "cluster_id": 131165,
          "cite": [
            "157 L. Ed. 2d 1166",
            "124 S. Ct. 1256",
            "540 U.S. 668",
            "2004 U.S. LEXIS 1621",
            "72 U.S.L.W. 4193",
            "17 Fla. L. Weekly Fed. S 153"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Napue v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105912) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg2MjE3NjAwMDAwJnM9NDc0Mjg1MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105912%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(105912)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MjQmcz04Njc0NzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105912%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105912)",
        "reviewed": 121,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 121,
        "triage_read": 3,
        "triage_snippet_classified": 118
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(105912)",
    "indexed_citing_opinions": 2479,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105912,
        "count": 2479,
        "count_source": "search"
      }
    ],
    "citation_count": 4249,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/napue-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMzczOTkmcz0xMDU1MzA3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28105912%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105912,
        "cited_id": 85160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 97658,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 97816,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 100264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 101991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 102101,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103621,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104842,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104844,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 105766,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 229184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 236467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 238555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 246192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 1550123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 2107640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105912,
        "cited_id": 2354547,
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
    "date_created": "2026-07-05T14:54:16Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:56:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:54:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Napue v. Illinois

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b307-3">
<span citation-index="1" class="star-pagination" label="265"> 
   *265
   </span>
  Mr. Chief Justice Warren
 </author>
<p id="Ago">
  delivered the opinion of the Court.
 </p>
<p id="b307-4">
  At the murder trial- of petitioner the principal state witness, then serving a 199-year sentence for the same murder, testified in response to a question by the Assistant State’s Attorney that he had received no promise of consideration in return for his testimony. The Assistant State’s Attorney had in fact promised him consideration, but did nothing to correct the witness’ false testimony. The jury was apprised, however, that' a public defender had promised “to do what he could” for the witness. The question presented is whether on these facts the failure of the prosecutor to correct the testimony of the witness which he knew to be false denied petitioner due process of law in violation of the Fourteenth Amendment to the Constitution, of the United States.
 </p>
<p id="b307-5">
  The record in this Court contains testimony from which the following facts could have been found. The murder in question occurred early in the morning of August 21, 1938, in a Chicago, Illinois, cocktail lounge., Petitioner Henry Napue, the witness George Hamer, one Poe and one Townsend entered the dimly lighted lounge and announced their intention to rob those present. An off-duty policeman, present in the lounge, drew his service revolver and began firing at the four men. In the melee that followed Townsend was killed, the officer wás fatally wounded, and the witness Hamer was seriously wounded. Napue and Poe carried Hamer to the car where a fifth man, one Webb, was waiting. In due course Hamer was apprehended, tried for the murder of the policeman, convicted on his plea of guilty and sentenced to 199 years. Subsequently, Poe was apprehended, tried, convicted, sentenced to death and executed. Hamer was not-used as a witness.
 </p>
<p id="b307-6">
  Thereafter, petitioner Napue was apprehended. He was put ón trial with 'Hamer being the principal witness
  <span citation-index="1" class="star-pagination" label="266"> 
   *266
   </span>
  for the State. Hamer’s testimony was. extremely important because the passage of time and the dim light in the cocktail lounge made eyewitness identification very difficult and uncertain, and because some pertinent witnesses had left the state. On the basis of the evidence presented, which consisted largely of Hamer’s testimony, the jury returned a. guilty verdict and petitioner was sentenced to 199 years.
 </p>
<p id="b308-4">
  Finally, the driver of the car, Webb, was apprehended. Hamer also testified against him. He was convicted of murder and sentenced-to 199 years.
 </p>
<p id="b308-5">
  Following the conviction of Webb, the lawyer who, as former Assistant State’s_Attorney, had prosecuted the Hamer, Poe and Napue cases filed a petition in the nature of a writ of error
  <em>
   coram nobis
  </em>
  on “behalf of Hamer. In the petition he alleged that as prosecuting attorney he had promised Hamer that if he would testify against Napue, “a recommendation for a reduction of his [Hamer’s] sentence would be made and, if possible, effectuated.”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The
  <span citation-index="1" class="star-pagination" label="267"> 
   *267
   </span>
  attorney prayed that the court would effect “consummation of the compact entered into between the duly authorized representatives of the State of Illinois and George Hamer.”
 </p>
<p id="b309-4">
  This
  <em>
   coram nobis
  </em>
  proceeding came to the attention of Napue, who thereafter filed a post-conviction petition,- in which he alleged that Hamer had falsely testified that he had been promised no consideration for his testimony,
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  and that the Assistant State’s Attorney handling the case had known this to be false. A hearing was ultimately held at which the former Assistant State’s Attorney testified that he had only'promised to help Hamer if Hamer’s story “about being a reluctant participant” in the robbery was borne out, and not merely if Hamer would testify at petitioner’s trial. He testified that in his
  <em>
   coram nobis
  </em>
  petition on Hamer’s behalf he “probably .used some language that [he] should not. have used” in his “zeal to do something for Hamer” to whom he “felt a, moral obligation.” The lower court denied petitioner relief on the basis of the attorney’s testimony.
 </p>
<p id="b309-5">
  On appeal, the Illinois Supreme Court affirmed on di£-' ferent‘grounds over two dissents. <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/" aria-description="Citation for case: Napue v. THE PEOPLE">13 Ill. 2d 566</a></span>, <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/" aria-description="Citation for case: Napue v. THE PEOPLE">150 N. E. 2d 613</a></span>. It fcjiind,' contrary to the trial éourt, that the attorney had promised Hamer consideration if he would testify at petitioner’s trial, a finding which the State does not contest here. It further found that the Assistant State’s Attorney knew that Hamer had lied in denying that
  <span citation-index="1" class="star-pagination" label="268"> 
   *268
   </span>
  he had been promised consideration. It held, however, that petitioner was entitled to no relief since the jury had already been apprised that someone whom Hamer had tentatively identified as being a public defender “was going to do what he could” in aid of Hamer, and “was trying to get something did” for him.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  We granted cer
  <span citation-index="1" class="star-pagination" label="269"> 
   *269
   </span>
  tiorari to considér the question posed in the first paragraph of this opinion. <span class="citation multiple-matches"><a href="/c/U.%20S./358/919/">358 U. S. 919</a></span>.
 </p>
<p id="AEf">
<em>
   First,
  </em>
  it is established that a conviction obtained through use of false evidence, known to be such by representatives of the State, must fall under the Fourteenth Amendment,
  <em>
   Mooney
  </em>
  v.
  <em>
   Holohan,
  </em>
  <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>;
  <em>
   Pyle
  </em>
  v. Kansas, <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span>;
  <em>
   Curran
  </em>
  v.
  <em>
   Delaware,
  </em>
  <span class="citation" data-id="246192"><a href="/opinion/246192/francis-j-curran-francis-j-maguire-and-ira-f-jones-jr-v-state-of/" aria-description="Citation for case: Francis J. Curran, Francis J. Maguire and Ira F. Jones,...">259 F. 2d 707</a></span>. See
  <em>
   New York ex rel. Whitman
  </em>
  v.
  <em>
   Wilson,
  </em>
  <span class="citation" data-id="103813"><a href="/opinion/103813/new-york-ex-rel-whitman-v-wilson/" aria-description="Citation for case: New York Ex Rel. Whitman v. Wilson">318 U. S. 688</a></span>, and
  <em>
   White
  </em>
  v.
  <em>
   Ragen,
  </em>
  <span class="citation" data-id="104125"><a href="/opinion/104125/white-v-ragen/" aria-description="Citation for case: White v. Ragen">324 U. S. 760</a></span>. Compare
  <em>
   Jones
  </em>
  v.
  <em>
   Commonwealth,
  </em>
  <span class="citation" data-id="1550123"><a href="/opinion/1550123/jones-v-commonwealth-of-kentucky/#338" aria-description="Citation for case: Jones v. Commonwealth of Kentucky">97 F. 2d 335, 338</a></span>, with
  <em>
   In re Sawyer’s Petition,
  </em>
  <span class="citation" data-id="238555"><a href="/opinion/238555/petition-for-writ-of-habeas-corpus-for-walter-j-sawyer-walter-j-sawyer/#809" aria-description="Citation for case: Petition for Writ of Habeas Corpus for Walter J. Sawyer....">229 F. 2d 805, 809</a></span>. Cf.
  <em>
   Mesarosh
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9421334"><a href="/opinion/105421/mesarosh-v-united-states/" aria-description="Citation for case: Mesarosh v. United States">352 U. S. 1</a></span>. The same result obtains when the State, although not soliciting false evidence, allows it to go unconnected when it appears.
  <em>
   Alcorta
  </em>
  v.
  <em>
   Texas,
  </em>
  <span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28</a></span>;
  <em>
   United States ex rel. Thompson
  </em>
  v.
  <em>
   Dye,
  </em>
  <span class="citation" data-id="9444580"><a href="/opinion/236467/united-states-of-america-ex-rel-cleveland-thompson-v-charles-l-dye/" aria-description="Citation for case: United States of America Ex Rel. Cleveland Thompson v....">221 F. 2d 763</a></span>;
  <em>
   United States ex rel. Almeida
  </em>
  v.
  <em>
   Baldi,
  </em>
  <span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">195 F. 2d 815</a></span>;
  <em>
   United States ex rel. Montgomery
  </em>
  v.
  <em>
   Ragen,
  </em>
  <span class="citation" data-id="2354547"><a href="/opinion/2354547/united-states-ex-rel-montgomery-v-ragen/" aria-description="Citation for case: United States Ex Rel. Montgomery v. Ragen">86 F. Supp. 382</a></span>. See generally annotation, <span class="citation no-link">2 L. Ed. 2d 1575</span>.
 </p>
<p id="b311-5">
  The principle that a State may not knowingly úse false evidence, including false testimony, to obtain a tainted conviction, implicit in any concept of ordered liberty, does not cease to apply merely because the false testimony goes only to the credibility of the witness. The jury’s estimate of the truthfulness and reliability of a given witness may well be determinative of guilt or innocence; and it is upon such subtle factors as the possible interest of the witness' in testifying falsely that a defendant’s life or liberty may depend. As stated by the New York Court of Appeals in a case very similar to this one,
  <em>
   People
  </em>
  v.
  <em>
   Savvides,
  </em>
  1 N. Y. 2d 554, 557; <span class="citation" data-id="5515949"><a href="/opinion/5668946/people-v-savvides/#854" aria-description="Citation for case: People v. Savvides">136 N. E. 2d 853, 854-855</a></span>; 154 N. Y. S. 2d 885, 887:
 </p>
<blockquote id="b311-6">
  “It is of no consequence that the falsehood bore upon the witness’ credibility rather than directly upon defendant’s guilt. A lie is a lie, no matter
  <span citation-index="1" class="star-pagination" label="270"> 
   *270
   </span>
  what its subject, and, if it is in any way relevant to the case, the district, attorney has the responsibility and duty to correct what he knows to be false and elicit the truth. . . . That the district attorney’s silence was not the result of guile or a desire to prejudice matters little, for its impact was the same, preventing, as it did, a trial that could in any real sense be termed fair.”
 </blockquote>
<p id="b312-4">
<em>
   Second,
  </em>
  we do not believe that the fact that the jury was apprised of other grounds for believing that the witness Hamer may have had an interest in testifying against petitioner turned what was otherwise a tainted trial into a fair one. &gt; As Mr. Justice Schaefer, joined by Chief Justice Davis, rightly put it in his dissenting opinion below, <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/#571" aria-description="Citation for case: Napue v. THE PEOPLE">13 Ill. 2d 566, 571</a></span>, <span class="citation" data-id="9718750"><a href="/opinion/2107640/napue-v-the-people/" aria-description="Citation for case: Napue v. THE PEOPLE">150 N. E. 2d 613</a></span>, 616:
 </p>
<blockquote id="b312-5">
  “What is overlooked here is that Hamer clearly testified that no one had offered to help him except an unidentified lawyer from the public defender’s office.”
 </blockquote>
<p id="b312-6">
  Had the jury been apprised, of the true facts, however, it might well have concluded that Hamer had fabricated testimony in order to curry the favor of the very representative of the State who was prosecuting the case in which Hamer was testifying, for Hamer might-have believed that such a representative was in a position to. implement (as he ultimately attempted to do) any promise of consideration. That the Assistant State’s Attorney himself thought it important to establish before the jury that no official source had promised Hamer consideration is made clear by his redirect examination, which was the last testimony of Hamer’s heard by the jury:
 </p>
<blockquote id="b312-7">
  “Q. Mr. Hamer, has Judge Prystalski [the trial judge] promised you any reduction of sentence?
 </blockquote>
<blockquote id="b313-5">
<span citation-index="1" class="star-pagination" label="271"> 
   *271
   </span>
  “A. No,, sir.
 </blockquote>
<blockquote id="b313-6">
  “Q. Have I promised you that I would recommend any reduction of sentence^to anybody?
 </blockquote>
<blockquote id="b313-7">
  “A. You did hot. [That answer was false and known to be so by the prosecutor.]
 </blockquote>
<blockquote id="b313-8">
  . “Q. Has any Judge of the criminal court promised that they [sic] would reduce your sentence?
 </blockquote>
<blockquote id="b313-9">
  “A. No, sir.
 </blockquote>
<blockquote id="b313-10">
  “Q. Has any representative of the Parole Board been to see you and promised you a reduction of sentence?
 </blockquote>
<blockquote id="b313-11">
  ' “A. No, sir.-
 </blockquote>
<blockquote id="b313-12">
  “Q. Has any representative of the Governor of the State of Illinois promised you a reduction of sentence?
 </blockquote>
<blockquote id="b313-13">
  “A. No, sir.”
 </blockquote>
<p id="b313-14">
  We are therefore unable to agree with the Illinois Supreme Court that “there was no constitutional infirmity by virtue of the false statement.”
 </p>
<p id="b313-15">
<em>
   Third,
  </em>
  the State argues that we are not free to reach a factual conclusion different from that reached by the Illinois Supreme Court, and that we are bound by its determination that the false testimony could not in any reasonable likelihood have affected the judgment of the jury. The State relies on
  <em>
   Hysler
  </em>
  v.
  <em>
   Florida,
  </em>
  <span class="citation" data-id="9419213"><a href="/opinion/103621/hysler-v-florida/" aria-description="Citation for case: Hysler v. Florida">315 U. S. 411</a></span>. But in that case the Court held only that a state standard of specificity and substantiality in making allegations of federal constitutional deprivations .would be respected, and this Court made its own “independent examination” of the allegations there, to determine if they had in fact met the Florida standard. The duty of this Court to make its own independent examination of the record when federal constitutional deprivations are alleged is clear, resting, as it does, on our solemn responsibility for main-' taining the Constitution inviolate.
  <em>
   Martin
  </em>
  v.
  <em>
   Hunter’s Lessee,
  </em>
  <span class="citation" data-id="85160"><a href="/opinion/85160/martin-v-hunters-lessee/" aria-description="Citation for case: Martin v. Hunter&#x27;s Lessee">1 Wheat. 304</a></span>;
  <em>
   Cooper
  </em>
  v.
  <em>
   Aaron,
  </em>
  <span class="citation" data-id="9421708"><a href="/opinion/105766/cooper-v-aaron/" aria-description="Citation for case: Cooper v. Aaron">358 U. S. 1</a></span>.
  <span citation-index="1" class="star-pagination" label="272"> 
   *272
   </span>
  This principle was well stated in
  <em>
   Niemotko
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9420519"><a href="/opinion/104842/niemotko-v-maryland/" aria-description="Citation for case: Niemotko v. Maryland">340 U. S. 268</a></span>, 271:
 </p>
<blockquote id="b314-4">
  “In cases in which there is a claim of denial of rights under the Federal Constitution, this Court is not bound by the conclusions of lower courts, but will reexamine the evidentiary basis on which those conclusions are founded.”
 </blockquote>
<p id="b314-5">
  It is now so well settled that the Court was able to speak in
  <em>
   Kern-Limerick, Inc.,
  </em>
  v.
  <em>
   Scurlock,
  </em>
  <span class="citation" data-id="9421036"><a href="/opinion/105193/kern-limerick-inc-v-scurlock/#121" aria-description="Citation for case: Kern-Limerick, Inc. v. Scurlock">347 U. S. 110, 121</a></span>, of the “long course of judicial construction which establishes as a principle that the duty rests on this Court to decide for itself facts or constructions upon which federal constitutional issues rest.”
  <a class="footnote" href="#fn4" id="fn4_ref">
<em>
    4
   </em>
</a>
<em>
</em>
  As previously indicated, our own evaluation of the record here compels us to hold that the false testimony used by the State in securing the conviction of petitioner may have had an effect on the outcome of the trial. Accordingly, the judgment below must be
 </p>
<p id="b314-6">
<em>
   Reversed.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b308-6">
   In relevant part, his petition read as follows:
  </p>
<blockquote id="b308-7">
   “After Hamer was sentenced your petitioner [the Assistant State’s Attorney] well knowing that identification of Poe, Napue and Webb if and when apprehended would be of an unsatisfactory character and not the kind of evidence upon which a jury could be asked to inflict a proper, severe penalty, and being unable to determine in advance whether Poe, Napue and Webb would make confessions of their participation in the' crime, represented to Hamer that if he would be willing to cooperate with law enforcing officials upon the trial of [sic] trials of Poe, Napue and Webb when they were apprehended, that a recommendation for a reduction of his sentence would be made-and, if possible, effectuated.
  </blockquote>
<blockquote id="b308-8">
   “Before testifying oh behalf of the State and against Napue, Hamer expressed to your petitioner a reluctance to cooperate any further Unless he were given definite assurance that a recommendation for reduction of his sentence would be made. Your petitioner, feeling that the interests of justice required Hamer’s testimony, again assured Hamer that every possible effort would be made to conform to the promise previously made to him.”
  </blockquote>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b309-6">
   The alleged false testimony of Hamer first occurred on his cross-examination :
  </p>
<blockquote id="b309-7">
   “Q. Did anybody give you a reward or promise you a reward for testifying?
  </blockquote>
<blockquote id="b309-8">
   ‘.‘A. There ain’t nobody promised me anything.”
  </blockquote>
<blockquote id="b309-9">
   On redirect examination the Assistant State’s Attorney again elicited' the same false answer.
  </blockquote>
<blockquote id="b309-10">
   “Q. [by the-Assistant State's Attorney] Have I promised you that I would recommend any reduction of sentence to anybody?
  </blockquote>
<blockquote id="b309-11">
   “A. You did not.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b310-5">
   The following is Hamer’s testimony on one subject:
  </p>
<blockquote id="b310-6">
   “Q. [on cross-examination] And didn’t you tell him [one of Napue’s •attorneys] that you wouldn’t testify in this ease unless you got some consideration for it ?
  </blockquote>
<blockquote id="b310-7">
   “A. ... Yes, I did; I told him that.
  </blockquote>
<blockquote id="b310-8">
   “Q. What are you sentenced for?
  </blockquote>
<blockquote id="b310-9">
   “A. One Hundred and Ninety-Nine Years. ‘
  </blockquote>
<blockquote id="b310-10">
   “Q. You hope to have that reduced, don’t you?
  </blockquote>
<blockquote id="b310-11">
   “A. Well, if anybody would help me or do anything for me, why certainly I would.
  </blockquote>
<blockquote id="b310-12">
   “Q. Weren’t you expecting that when you came here today?
  </blockquote>
<blockquote id="b310-13">
   “A. There haven’t no one told pie anything, no more than the lawyer. The lawyer come in and talked to me a while ago and said he was going to do what he could.
   <em>
    f &gt;
   </em>
</blockquote>
<blockquote id="b310-14">
   “Q. Which lawyer was that?
  </blockquote>
<blockquote id="b310-15">
<em>
    “A.
   </em>
   I don’t know; it was a Public Defender.' I don’t see him in here.
   <em>
    ¡,
   </em>
</blockquote>
<blockquote id="b310-16">
   “Q. You mean he was from the Public Defender s office?
  </blockquote>
<blockquote id="b310-17">
   “A. I imagine that is where he was from, I don’t know.-
  </blockquote>
<blockquote id="b310-18">
   “Q. And he was the one who told you that?
  </blockquote>
<blockquote id="b310-19">
   “A. Yes, he told me he was trying to get something did for me.
  </blockquote>
<blockquote id="b310-20">
   “Q. . . . And he told you he was going to do something for you ?
  </blockquote>
<blockquote id="b310-21">
   “A. He said he was going to try to.
  </blockquote>
<blockquote id="b310-22">
   “Q.'And you told them [police officers] you would [testify at the trial of Napue] but you expected some consideration for it?
  </blockquote>
<blockquote id="b310-23">
   “A. I asked them was there any chance of me getting any. The man told me he didn’t know, that he couldn’t promise me anything.
  </blockquote>
<blockquote id="b310-24">
   “Q. Then you spoke to a lawyer today who said he would try to get yoúr time cut?
  </blockquote>
<blockquote id="b310-25">
<em>
    “A.
   </em>
   That was this Public Defender. I don’t even know his name. . . .”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b314-7">
   See,
   <em>
    e. g., Payne
   </em>
   v.
   <em>
    Arkansas,
   </em>
   <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#562" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 562</a></span>;
   <em>
    Leyra
   </em>
   v.
   <em>
    Denno,
   </em>
   <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/#558" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556, 558</a></span>;
   <em>
    Avery
   </em>
   v.
   <em>
    Georgia,
   </em>
   <span class="citation" data-id="9420951"><a href="/opinion/105128/avery-v-georgia/#561" aria-description="Citation for case: Avery v. Georgia">345 U. S. 559, 561</a></span>;
   <em>
    Feiner
   </em>
   v.
   <em>
    New York,
   </em>
   <span class="citation" data-id="9420523"><a href="/opinion/104844/feiner-v-new-york/#322" aria-description="Citation for case: Feiner v. New York">340 U. S. 315, 322, 323, note 4</a></span> (dissenting opinion);
   <em>
    Cassell
   </em>
   v.
   <em>
    Texas,
   </em>
   <span class="citation" data-id="9420469"><a href="/opinion/104785/cassell-v-texas/#283" aria-description="Citation for case: Cassell v. Texas">339 U. S. 282, 283</a></span>;
   <em>
    Holey
   </em>
   v.
   <em>
    Ohio,
   </em>
   <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 599</a></span>;
   <em>
    Malinski
   </em>
   v.
   <em>
    New York,
   </em>
   <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#404" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 404</a></span>;
   <em>
    Ashcraft
   </em>
   v.
   <em>
    Tennessee,
   </em>
   <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#149" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143, 149</a></span>;
   <em>
    Ward
   </em>
   v.
   <em>
    Texas,
   </em>
   <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/#550" aria-description="Citation for case: Ward v. Texas">316 U. S. 547, 550</a></span>;
   <em>
    Smith
   </em>
   v.
   <em>
    Texas,
   </em>
   <span class="citation" data-id="103391"><a href="/opinion/103391/smith-v-texas/#130" aria-description="Citation for case: Smith v. Texas">311 U. S. 128, 130</a></span>;
   <em>
    South Carolina
   </em>
   v.
   <em>
    Bailey,
   </em>
   <span class="citation" data-id="102101"><a href="/opinion/102101/south-carolina-v-bailey/#420" aria-description="Citation for case: South Carolina v. Bailey">289 U. S. 412, 420</a></span>. See also,
   <em>
    e. g., Roth
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9421496"><a href="/opinion/105547/roth-v-united-states/#497" aria-description="Citation for case: Roth v. United States">354 U. S. 476, 497</a></span> (dissenting opinion);
   <em>
    Stroble
   </em>
   v.
   <em>
    California,
   </em>
   <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/#190" aria-description="Citation for case: Stroble v. California">343 U. S. 181, 190</a></span>;
   <em>
    Sterling
   </em>
   v.
   <em>
    Constantin,
   </em>
   <span class="citation" data-id="101991"><a href="/opinion/101991/sterling-v-constantin/#398" aria-description="Citation for case: Sterling v. Constantin">287 U. S. 378, 398</a></span>;
   <em>
    Southern Pacific Co.
   </em>
   v.
   <em>
    Schuyler,
   </em>
   <span class="citation" data-id="97816"><a href="/opinion/97816/southern-pacific-co-v-schuyler/#611" aria-description="Citation for case: Southern Pacific Co. v. Schuyler">227 U. S. 601, 611</a></span>;
   <em>
    Creswill
   </em>
   v.
   <em>
    Grand Lodge Knights of Pythias,
   </em>
   <span class="citation" data-id="9418222"><a href="/opinion/97658/creswill-v-grand-lodge-knights-of-pythias-of-georgia/#261" aria-description="Citation for case: Creswill v. Grand Lodge Knights of Pythias of Georgia">225 U. S. 246, 261</a></span>.
  </p>
<p id="b314-8">
   Mr. Justice Holmes, writing for the Court, recognized the principle over 35 years ago in
   <em>
    Davis
   </em>
   v.
   <em>
    Wechsler,
   </em>
   <span class="citation" data-id="100264"><a href="/opinion/100264/davis-v-wechsler/" aria-description="Citation for case: Davis v. Wechsler">263 U. S. 22</a></span>, 24:
  </p>
<blockquote id="b314-9">
   “If the Constitution and laws of the United States are to be enforced, this Court cannot accept as final the decision of a state -tribunal as (to what are the facts alleged to give rise to the right or to bar the assertion of it even upon local grounds.”
  </blockquote>
</div></div></opinion>
```

---
