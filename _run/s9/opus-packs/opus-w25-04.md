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

## GROUP: content/cases/Aguilar v. Texas.md  (`case`, 5 assertions)

### content_page

```
---
title: "Aguilar v. Texas"
type: case
citation: "378 U.S. 108 (1964)"
parallel_cite: "84 S. Ct. 1509; 12 L. Ed. 2d 723"
neutral_cite: 1964 U.S. LEXIS 994
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-06-15
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: superseded
  as_of_content: 1964-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Aguilar v. Texas
  varies_by_point: false
  scope_note: "Two-prong Aguilar-Spinelli test for informant tips abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106865/aguilar-v-texas/"
  cluster_id: 106865
  opinion_id: 106865
  identity_checked: true
homes:
  - page: "[[Probable Cause]]"
    role: "Key — Anchor"
related: ["[[Illinois v. Gates]]", "[[Spinelli v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "probable-cause", "informants", "historical"]
holding: "A magistrate may issue a warrant on an informant's hearsay only if the affidavit shows **(1) the informant's basis of knowledge** (how…"
lake:
  record_id: Aguilar v. Texas
  status: verified
  projected_at: 2026-07-09
---

# Aguilar v. Texas

*378 U.S. 108 (1964)* · U.S. Supreme Court · **Historical** · Treatment: **abrogated** *(as of 2026-06-30)* — abrogated by [[Illinois v. Gates]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Houston officers obtained a warrant to search for narcotics on an affidavit that recited only that the affiants "have received reliable information from a credible person and do believe" that narcotics were being kept at the premises. The affidavit gave no underlying facts — neither how the informant knew nor why he was believed. The warrant issued and evidence was seized and used to convict.

## Issue
Whether an affidavit resting solely on an informant's tip — stated as a conclusion, without underlying facts showing the informant's basis of knowledge or his credibility — can support a magistrate's finding of probable cause.

## Rule
No. An affidavit may rest on hearsay, but the magistrate must be given the underlying facts behind both the informant's knowledge and his reliability. The "magistrate must be informed of some of the underlying circumstances from which the informant concluded that the narcotics were where he claimed they were, and some of the underlying circumstances from which the officer concluded that the informant . . . was 'credible' or his information 'reliable.'" — 378 U.S. at 114. ^pin-114

Otherwise the probable-cause inference is drawn not "by a neutral and detached magistrate," as the Constitution requires, "but instead, by a police officer 'engaged in the often competitive enterprise of ferreting out crime.'" — [*Id.* at 115](https://www.courtlistener.com/opinion/106865/aguilar-v-texas/#:~:text=by%20a%20neutral%20and%20detached%20magistrate%2C). ^pin-115

## Application
The affidavit here was a bare conclusion: it offered the magistrate no underlying circumstances showing how the informant learned that narcotics were on the premises, and none showing why the informant was credible or his information reliable. On these facts the magistrate could only accept the informant's "suspicion," "belief," or "mere conclusion" without question, so the warrant lacked a sufficient basis and should not have issued.

## Conclusion
The search warrant was invalid for want of probable cause; the judgment resting on the seized evidence was reversed.

## Treatment & subsequent history
- **Status:** abrogated *(as of 2026-06-30)* — **Historical** (tier 6).
- The rigid two-prong "basis of knowledge" + "veracity" framework of *Aguilar* (with [[Spinelli v. United States]]) was **abandoned by [[Illinois v. Gates]]** (1983) in favor of a **totality-of-the-circumstances** test. Under *[[Illinois v. Gates|Gates]]*, the informant's basis of knowledge and veracity remain relevant considerations but are no longer independent, dispositive requirements.

## Appears on
- [[Probable Cause]] — *Key — Anchor*

## Sources
- *Aguilar v. Texas*, 378 U.S. 108 (1964) — https://www.courtlistener.com/opinion/106865/aguilar-v-texas/ — pinpoints: 114, 115.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "544b00bd683bb43d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "378 U.S. 108 (1964)", "court": "U.S. Supreme Court", "neutral_cite": "1964 U.S. LEXIS 994", "official_citation_present": true, "parallel_cite": "84 S. Ct. 1509; 12 L. Ed. 2d 723", "title": "Aguilar v. Texas", "year": "1964"}}
{"assertion_id": "d90539764553f3b8", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A magistrate may issue a warrant on an informant's hearsay only if the affidavit shows **(1) the informant's basis of knowledge** (how…", "title": "Aguilar v. Texas"}}
{"assertion_id": "f4d1404a2682a333", "dimension": "support", "kind": "home_role", "locator": {"home": "Probable Cause"}, "payload": {"home": "Probable Cause", "role": "Key — Anchor", "title": "Aguilar v. Texas"}}
{"assertion_id": "48e0e9e3ad42a704", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Aguilar v. Texas"}}
{"assertion_id": "cdcd7263938f7ae6", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1964-06-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Aguilar v. Texas", "field_i_validity": "superseded", "scope_note": "Two-prong Aguilar-Spinelli test for informant tips abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).", "title": "Aguilar v. Texas", "varies_by_point": "false"}}
```

### lake record — Aguilar v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Aguilar v. Texas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Aguilar v. Texas",
    "case_name_short": "Aguilar",
    "case_name_full": "Aguilar v. Texas",
    "input_case_name": "Aguilar v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-06-15",
    "year": 1964,
    "docket": null,
    "cluster_id": 106865,
    "lead_opinion_id": 106865,
    "sibling_ids": [
      106865,
      9422845,
      9422846,
      9422847
    ],
    "absolute_url": "/opinion/106865/aguilar-v-texas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "378 U.S. 108",
      "volume": "378",
      "reporter": "U.S.",
      "page": "108",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1509",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1509",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 723",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 994",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "994",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "378 U.S. 108",
        "volume": "378",
        "reporter": "U.S.",
        "page": "108",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1509",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1509",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 723",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "723",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 994",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "994",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "378 U.S. 108",
    "official_selection": {
      "court_class": "scotus",
      "selected": "378 U.S. 108",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-114",
      "page": null,
      "quote": "that narcotics were being kept at the premises. The affidavit gave no underlying facts \u2014 neither how the informant knew nor why he was believed. The warrant issued and evidence was seized and used to convict. ## Issue Whether an affidavit resting solely on an informant's tip \u2014 stated as a conclusion, without underlying facts showing the informant's basis of knowledge or his credibility \u2014 can support a magistrate's finding of probable cause. ## Rule No. An affidavit may rest on hearsay, but the magistrate must be given the underlying facts behind both the informant's knowledge and his reliability. The",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-115",
      "page": null,
      "quote": "by a neutral and detached magistrate,",
      "star_marker": "115",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13622,
      "fragment": "#:~:text=by%20a%20neutral%20and%20detached%20magistrate%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "superseded",
    "as_of_content": "1964-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Aguilar v. Texas",
    "varies_by_point": false,
    "scope_note": "Two-prong Aguilar-Spinelli test for informant tips abandoned for a totality-of-the-circumstances approach by Illinois v. Gates (1983).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Illinois v. Gates",
          "cluster_id": 110959,
          "cite": "462 U.S. 213",
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:abrogated"
      },
      {
        "citing_case": {
          "name": "In re Grijalva; Judith del Cuadro-Zimmerman",
          "cluster_id": 10847130,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mercer",
          "cluster_id": 10803481,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Leighton R.",
          "cluster_id": 10742062,
          "cite": [
            "2025 NY Slip Op 06534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Luis Morales",
          "cluster_id": 10734924,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "FRASER, MARIAN v. the State of Texas",
          "cluster_id": 10667479,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wilson",
          "cluster_id": 10664712,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Silva",
          "cluster_id": 10640306,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Brandon Tylor Mulac",
          "cluster_id": 10633329,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Hill",
          "cluster_id": 10582111,
          "cite": [
            "2025 NY Slip Op 25109"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ball v. New York State Dept. of Health",
          "cluster_id": 10379926,
          "cite": [
            "2025 NY Slip Op 25090"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shannon",
          "cluster_id": 10373759,
          "cite": [
            "2025 Ohio 1224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Washington, V. Tommy Darren Tyson",
          "cluster_id": 10339068,
          "cite": [
            "564 P.3d 248"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. S. CHRISTOPHER M. BOYER / COMMONWEALTH v. S. ROMUALD BERNAUD",
          "cluster_id": 10642653,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Antwone Miguel Sanders",
          "cluster_id": 9986839,
          "cite": [
            "106 F.4th 455"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Todd Michael Glover v. the State of Texas",
          "cluster_id": 9509712,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Todd Michael Glover v. the State of Texas",
          "cluster_id": 9509711,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Willie Locust",
          "cluster_id": 9455816,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 9452598,
          "cite": [
            "2023 Ohio 4565"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams",
          "cluster_id": 9448572,
          "cite": [
            "2023 Ohio 4344"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Roosevelt Randolph",
          "cluster_id": 10612306,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grace",
          "cluster_id": 9433421,
          "cite": [
            "2023 Ohio 3781"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edward Leonidas Lewis",
          "cluster_id": 9424185,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Joyette",
          "cluster_id": 9419192,
          "cite": [
            "219 A.D.3d 628",
            "194 N.Y.S.3d 287",
            "2023 NY Slip Op 04216"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Tito Rene Scott",
          "cluster_id": 9403530,
          "cite": [
            "530 P.3d 1178",
            "97 Arizona Cases Digest 31"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Donald Ehrhardt III v. State of Mississippi",
          "cluster_id": 10628852,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Michael Figueroa",
          "cluster_id": 10642568,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Guardado",
          "cluster_id": 9391153,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Collins",
          "cluster_id": 9381212,
          "cite": [
            "2023 Ohio 646"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Schubert",
          "cluster_id": 9354069,
          "cite": [
            "219 N.E.3d 916",
            "171 Ohio St. 3d 617",
            "2022 Ohio 4604"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lucas",
          "cluster_id": 9353082,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lucas",
          "cluster_id": 8509871,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lucas",
          "cluster_id": 8436709,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. PIERRE A. SERTYL.",
          "cluster_id": 10271855,
          "cite": [
            "101 Mass. App. Ct. 836"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Morton",
          "cluster_id": 7859188,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. BRITTANY WESTGATE.",
          "cluster_id": 10271879,
          "cite": [
            "101 Mass. App. Ct. 548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Baldwin, John Wesley",
          "cluster_id": 6468832,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "COMMONWEALTH v. CRISTOBAL RODRIGUEZ.",
          "cluster_id": 10271920,
          "cite": [
            "101 Mass. App. Ct. 54"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Robinson",
          "cluster_id": 6465711,
          "cite": [
            "167 N.Y.S.3d 542",
            "205 A.D.3d 737",
            "2022 NY Slip Op 03010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Patrick Bracy",
          "cluster_id": 6452507,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jumaev",
          "cluster_id": 5305647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jumaev",
          "cluster_id": 5304277,
          "cite": [
            "20 F.4th 518"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Siegel",
          "cluster_id": 5302012,
          "cite": [
            "180 N.E.3d 574",
            "2021 Ohio 4208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mortel",
          "cluster_id": 4901591,
          "cite": [
            "152 N.Y.S.3d 68",
            "197 A.D.3d 196",
            "2021 NY Slip Op 04498"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maximo Gondres-Medrano",
          "cluster_id": 4898417,
          "cite": [
            "3 F.4th 708"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Siler",
          "cluster_id": 4879520,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Siler",
          "cluster_id": 4877161,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Victoria Catherine Pagano",
          "cluster_id": 6248596,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Victoria Catherine Pagano",
          "cluster_id": 4876573,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Salvas",
          "cluster_id": 4869523,
          "cite": [
            "149 Haw. 152",
            "483 P.3d 312"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Mayhew",
          "cluster_id": 4867625,
          "cite": [
            "145 N.Y.S.3d 202",
            "192 A.D.3d 1391",
            "2021 NY Slip Op 01807"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Richard Dale Griffin v. State",
          "cluster_id": 4843483,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Samer Abdalla",
          "cluster_id": 4780505,
          "cite": [
            "972 F.3d 838"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Nettles",
          "cluster_id": 4778561,
          "cite": [
            "186 A.D.3d 861",
            "128 N.Y.S.3d 610",
            "2020 NY Slip Op 04776"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Burn v. United States",
          "cluster_id": 4776810,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Gary Campbell",
          "cluster_id": 4771571,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Ward, III",
          "cluster_id": 4771237,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Ward, III",
          "cluster_id": 4770977,
          "cite": [
            "967 F.3d 550"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Wesley Ryder",
          "cluster_id": 4764454,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. MacIas",
          "cluster_id": 4763635,
          "cite": [
            "249 Ariz. 335",
            "469 P.3d 472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stubbs",
          "cluster_id": 4763578,
          "cite": [
            "2020 Ohio 3464"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Oki",
          "cluster_id": 4759146,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Costa",
          "cluster_id": 4744366,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Marmon",
          "cluster_id": 10133414,
          "cite": [
            "303 Or. App. 469",
            "463 P.3d 555"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thompson v. State",
          "cluster_id": 10021199,
          "cite": [
            "226 A.3d 871",
            "245 Md. App. 450"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Gilbert",
          "cluster_id": 4734622,
          "cite": [
            "952 F.3d 759"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dibble (Slip Opinion)",
          "cluster_id": 4728568,
          "cite": [
            "150 N.E.3d 912",
            "159 Ohio St. 3d 322",
            "2020 Ohio 546"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barreto",
          "cluster_id": 4690114,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Dunbar",
          "cluster_id": 4688211,
          "cite": [
            "2019 NY Slip Op 9018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Charles Edward Johnson v. State",
          "cluster_id": 4666476,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Manzo",
          "cluster_id": 4658488,
          "cite": [
            "2018 IL 122761"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Robert Jason Allison",
          "cluster_id": 4657477,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andrews v. District of Columbia",
          "cluster_id": 4648603,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Christian",
          "cluster_id": 4625269,
          "cite": [
            "925 F.3d 305"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Henderson",
          "cluster_id": 4622068,
          "cite": [
            "2019 Ohio 1974"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perkins",
          "cluster_id": 4617416,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Perkins",
          "cluster_id": 4612731,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Valentine v. State",
          "cluster_id": 4601787,
          "cite": [
            "207 A.3d 566"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ferreira",
          "cluster_id": 4601010,
          "cite": [
            "119 N.E.3d 278",
            "481 Mass. 641"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 4600764,
          "cite": [
            "119 N.E.3d 257",
            "481 Mass. 604"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kent Taderro Bailey, Jr. v. State of Indiana (mem. dec.)",
          "cluster_id": 4580461,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cintron",
          "cluster_id": 7178110,
          "cite": [
            "119 N.E.3d 357",
            "94 Mass. App. Ct. 1115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barreto",
          "cluster_id": 4548401,
          "cite": [
            "113 N.E.3d 429"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silva",
          "cluster_id": 7177073,
          "cite": [
            "113 N.E.3d 400"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Manuel, C.",
          "cluster_id": 4529555,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Manuel",
          "cluster_id": 4529554,
          "cite": [
            "194 A.3d 1076"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Monteiro",
          "cluster_id": 4512544,
          "cite": [
            "103 N.E.3d 1230",
            "93 Mass. App. Ct. 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Christian",
          "cluster_id": 4511817,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tyrone Christian",
          "cluster_id": 4511298,
          "cite": [
            "893 F.3d 846"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Richard Lebron Madden, Sr.",
          "cluster_id": 4504038,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon McGrath v. State of Indiana",
          "cluster_id": 4494172,
          "cite": [
            "95 N.E.3d 522"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Decarvalho",
          "cluster_id": 7174850,
          "cite": [
            "103 N.E.3d 771",
            "93 Mass. App. Ct. 1106"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4476634,
          "cite": [
            "96 N.E.3d 719",
            "93 Mass. App. Ct. 6"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Manha",
          "cluster_id": 4473484,
          "cite": [
            "91 N.E.3d 669",
            "479 Mass. 44"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sanchez",
          "cluster_id": 4455867,
          "cite": [
            "2017 NY Slip Op 8899"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Sanchez",
          "cluster_id": 4453920,
          "cite": [
            "2017 NY Slip Op 8899"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Luna",
          "cluster_id": 4449164,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Rodney Paul Starnes, II",
          "cluster_id": 4447496,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ezra Griffith",
          "cluster_id": 4419946,
          "cite": [
            "867 F.3d 1265",
            "2017 WL 3568288",
            "2017 U.S. App. LEXIS 15636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jordan",
          "cluster_id": 4406528,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Anthony Youngs",
          "cluster_id": 4405941,
          "cite": [
            "199 Wash. App. 472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Dominique Greer",
          "cluster_id": 4392274,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Lucy Caitlin Alford and Jeremie Alford",
          "cluster_id": 4392026,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Darius Lamarr Franklin",
          "cluster_id": 4391006,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Thomas Braden",
          "cluster_id": 4387920,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joppy v. State",
          "cluster_id": 4386883,
          "cite": [
            "158 A.3d 1112",
            "232 Md. App. 510",
            "2017 WL 1508235",
            "2017 Md. App. LEXIS 420"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan P. Jackson v. United States",
          "cluster_id": 4382813,
          "cite": [
            "157 A.3d 1259",
            "2017 WL 1373326",
            "2017 D.C. App. LEXIS 81"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jerry Lewis Tuttle",
          "cluster_id": 4380976,
          "cite": [
            "515 S.W.3d 282",
            "2017 WL 1246855",
            "2017 Tenn. LEXIS 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Christopher Douglas Smith",
          "cluster_id": 4375166,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Camel",
          "cluster_id": 4369470,
          "cite": [
            "8 Cal. App. 5th 989",
            "214 Cal. Rptr. 3d 531",
            "2017 Cal. App. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "April Smith v. Jason Munday",
          "cluster_id": 4345933,
          "cite": [
            "848 F.3d 248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kono",
          "cluster_id": 4333305,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kono",
          "cluster_id": 4333306,
          "cite": [
            "152 A.3d 1",
            "324 Conn. 80",
            "2016 Conn. LEXIS 396"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Perez",
          "cluster_id": 4314370,
          "cite": [
            "90 Mass. App. Ct. 548"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Laurie Lynn Welch and Roland John Welch",
          "cluster_id": 4312164,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Delgado v. City of New York",
          "cluster_id": 4260335,
          "cite": [
            "144 A.D.3d 46",
            "38 N.Y.S.3d 129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keenan",
          "cluster_id": 4249780,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keenan",
          "cluster_id": 4249294,
          "cite": [
            "304 Kan. 986",
            "377 P.3d 439",
            "2016 Kan. LEXIS 440"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rauf v. State",
          "cluster_id": 4243712,
          "cite": [
            "145 A.3d 430",
            "2016 Del. LEXIS 419",
            "2016 WL 4224252"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Thomas Braden",
          "cluster_id": 4242137,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moore v. State",
          "cluster_id": 3207660,
          "cite": [
            "372 P.3d 922",
            "2016 Alas. App. LEXIS 101",
            "2016 WL 3033860"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. William Gary Mosley",
          "cluster_id": 3172337,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Valadez, Alvin Jr.",
          "cluster_id": 4295917,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Donna Marie Chartrand",
          "cluster_id": 3008533,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Vernon Elliott Lockhart",
          "cluster_id": 2898080,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ramos",
          "cluster_id": 2827409,
          "cite": [
            "88 Mass. App. Ct. 68"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Darryl L. Bryant",
          "cluster_id": 2818139,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Z. U. E.",
          "cluster_id": 2817762,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Veloz",
          "cluster_id": 7313876,
          "cite": [
            "109 F. Supp. 3d 305",
            "2015 WL 3540808"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Freeman",
          "cluster_id": 2805220,
          "cite": [
            "87 Mass. App. Ct. 448"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Perez",
          "cluster_id": 2793890,
          "cite": [
            "87 Mass. App. Ct. 278"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robinson, Timothy Lee",
          "cluster_id": 4265214,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gonzales, Rodolfo v. State",
          "cluster_id": 4264446,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Gregory Robinson, Sr.",
          "cluster_id": 2779601,
          "cite": [
            "454 S.W.3d 428",
            "2015 Mo. App. LEXIS 154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Long",
          "cluster_id": 2763468,
          "cite": [
            "774 F.3d 653",
            "2014 U.S. App. LEXIS 24169",
            "2014 WL 7240718"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hoffman (Slip Opinion)",
          "cluster_id": 2747812,
          "cite": [
            "2014 Ohio 4795",
            "141 Ohio St. 3d 428",
            "25 N.E.3d 993"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 2741338,
          "cite": [
            "230 Cal. App. 4th 490",
            "178 Cal. Rptr. 3d 649",
            "2014 Cal. App. LEXIS 903"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Andrew Davis Saggers",
          "cluster_id": 2717177,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cuong Phu Le",
          "cluster_id": 2984353,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Michael A. Talley",
          "cluster_id": 2651055,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Z.E.",
          "cluster_id": 2648374,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ollivier",
          "cluster_id": 2620563,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ollivier",
          "cluster_id": 2620490,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. William Lance Walker",
          "cluster_id": 1044056,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jeffrey Kristopher King and Kasey Lynn King",
          "cluster_id": 1044089,
          "cite": [
            "437 S.W.3d 856"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Washington v. Tawana Lea Davis",
          "cluster_id": 1039839,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Betts",
          "cluster_id": 1043601,
          "cite": [
            "194 Vt. 212",
            "2013 VT 53",
            "75 A.3d 629",
            "2013 WL 3957591",
            "2013 Vt. LEXIS 56"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Stephen Baker",
          "cluster_id": 1044492,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Michael T. Shelby",
          "cluster_id": 1044601,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Kenneth Hubanks",
          "cluster_id": 1044648,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Arturo Castellanos",
          "cluster_id": 873156,
          "cite": [
            "716 F.3d 828",
            "2013 WL 2321976",
            "2013 U.S. App. LEXIS 10797"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Clagon",
          "cluster_id": 6580704,
          "cite": [
            "465 Mass. 1004",
            "987 N.E.2d 554",
            "2013 WL 1878923",
            "2013 Mass. LEXIS 325"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Cayetano Ramirez",
          "cluster_id": 1044752,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bonds, Michael Ray",
          "cluster_id": 2948506,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bonds, Michael Ray",
          "cluster_id": 2948505,
          "cite": [
            "403 S.W.3d 867",
            "2013 Tex. Crim. App. LEXIS 531",
            "2013 WL 1136522"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Montoya",
          "cluster_id": 6580607,
          "cite": [
            "464 Mass. 566",
            "984 N.E.2d 793",
            "2013 WL 951128",
            "2013 Mass. LEXIS 45"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
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
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tapia",
          "cluster_id": 6580545,
          "cite": [
            "463 Mass. 721",
            "978 N.E.2d 534",
            "2012 Mass. LEXIS 1060"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Travis Kinte Echols",
          "cluster_id": 1043929,
          "cite": [
            "382 S.W.3d 266",
            "2012 Tenn. LEXIS 738"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Madrid",
          "cluster_id": 8721843,
          "cite": [
            "916 F. Supp. 2d 730",
            "2012 WL 6771011",
            "2012 U.S. Dist. LEXIS 183606"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Duarte, Gilbert",
          "cluster_id": 2946139,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Duarte, Gilbert",
          "cluster_id": 2946138,
          "cite": [
            "389 S.W.3d 349",
            "2012 WL 3965824",
            "2012 Tex. Crim. App. LEXIS 1180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Mendes",
          "cluster_id": 6580522,
          "cite": [
            "463 Mass. 353",
            "974 N.E.2d 606",
            "2012 WL 3797614",
            "2012 Mass. LEXIS 829"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Patrick Stout v. State of Tennessee",
          "cluster_id": 1046186,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Haidle",
          "cluster_id": 891753,
          "cite": [
            "2012 NMSC 33",
            "2 N.M. 491",
            "2012 NMSC 033"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Eldridge",
          "cluster_id": 2697621,
          "cite": [
            "2012 Ohio 3747"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Barbosa",
          "cluster_id": 6580509,
          "cite": [
            "463 Mass. 116",
            "972 N.E.2d 987",
            "2012 WL 3139732",
            "2012 Mass. LEXIS 689"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Armijo v. Perales",
          "cluster_id": 805666,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Jerome Sidney Barrett",
          "cluster_id": 1046423,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Voustianiouk",
          "cluster_id": 804162,
          "cite": [
            "685 F.3d 206",
            "2012 WL 2849655",
            "2012 U.S. App. LEXIS 14317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Freeman v. Kadien",
          "cluster_id": 803571,
          "cite": [
            "684 F.3d 30",
            "2012 U.S. App. LEXIS 13674",
            "2012 WL 2551092"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Guy Alvin Williamson",
          "cluster_id": 1043952,
          "cite": [
            "368 S.W.3d 468",
            "2012 WL 1950275",
            "2012 Tenn. LEXIS 380"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Santiago",
          "cluster_id": 8358036,
          "cite": [
            "30 Mass. L. Rptr. 81"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Blane v. Commonwealth",
          "cluster_id": 2547964,
          "cite": [
            "364 S.W.3d 140",
            "2012 Ky. LEXIS 54",
            "2012 WL 1450212"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lyons",
          "cluster_id": 2500041,
          "cite": [
            "275 P.3d 314",
            "174 Wash. 2d 354"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jackson",
          "cluster_id": 2504396,
          "cite": [
            "727 S.E.2d 322",
            "220 N.C. App. 1",
            "2012 WL 1293800",
            "2012 N.C. App. LEXIS 510"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Terry v. Ohio",
          "cluster_id": 107729,
          "cite": [
            "20 L. Ed. 2d 889",
            "88 S. Ct. 1868",
            "392 U.S. 1",
            "1968 U.S. LEXIS 1345",
            "44 Ohio Op. 2d 383"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Franks v. Delaware",
          "cluster_id": 109925,
          "cite": [
            "57 L. Ed. 2d 667",
            "98 S. Ct. 2674",
            "438 U.S. 154",
            "1978 U.S. LEXIS 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chimel v. California",
          "cluster_id": 107979,
          "cite": [
            "23 L. Ed. 2d 685",
            "89 S. Ct. 2034",
            "395 U.S. 752",
            "1969 U.S. LEXIS 1166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schmerber v. California",
          "cluster_id": 107262,
          "cite": [
            "16 L. Ed. 2d 908",
            "86 S. Ct. 1826",
            "384 U.S. 757",
            "1966 U.S. LEXIS 1129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beck v. Ohio",
          "cluster_id": 106936,
          "cite": [
            "13 L. Ed. 2d 142",
            "85 S. Ct. 223",
            "379 U.S. 89",
            "1964 U.S. LEXIS 151",
            "3 Ohio Misc. 71",
            "31 Ohio Op. 2d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Williams",
          "cluster_id": 108571,
          "cite": [
            "32 L. Ed. 2d 612",
            "92 S. Ct. 1921",
            "407 U.S. 143",
            "1972 U.S. LEXIS 2206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sibron v. New York",
          "cluster_id": 107730,
          "cite": [
            "20 L. Ed. 2d 917",
            "88 S. Ct. 1889",
            "392 U.S. 40",
            "1968 U.S. LEXIS 1346",
            "44 Ohio Op. 2d 402"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ventresca",
          "cluster_id": 106990,
          "cite": [
            "13 L. Ed. 2d 684",
            "85 S. Ct. 741",
            "380 U.S. 102",
            "1965 U.S. LEXIS 2438",
            "16 A.F.T.R.2d (RIA) 5787"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payne v. Tennessee",
          "cluster_id": 112643,
          "cite": [
            "115 L. Ed. 2d 720",
            "111 S. Ct. 2597",
            "501 U.S. 808",
            "1991 U.S. LEXIS 3821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alabama v. White",
          "cluster_id": 112454,
          "cite": [
            "110 L. Ed. 2d 301",
            "110 S. Ct. 2412",
            "496 U.S. 325",
            "1990 U.S. LEXIS 3053"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Warden, Maryland Penitentiary v. Hayden",
          "cluster_id": 107465,
          "cite": [
            "18 L. Ed. 2d 782",
            "87 S. Ct. 1642",
            "387 U.S. 294",
            "1967 U.S. LEXIS 2753"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
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
        "journal_ref": "Aguilar v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzM0NjIwODAwMDAwJnM9MjUwNDM5NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106865+OR+9422845+OR+9422846+OR+9422847%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 180
      },
      "lane2_top_cited": {
        "query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05NDgmcz0xMDY5NjQmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106865+OR+9422845+OR+9422846+OR+9422847%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847)",
        "reviewed": 36,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 36,
        "triage_read": 0,
        "triage_snippet_classified": 36
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106865 OR 9422845 OR 9422846 OR 9422847)",
    "indexed_citing_opinions": 5035,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106865,
        "count": 4539,
        "count_source": "search"
      },
      {
        "opinion_id": 9422845,
        "count": 629,
        "count_source": "search"
      },
      {
        "opinion_id": 9422846,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422847,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7290,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/aguilar-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NjgzNTUmcz05OTg2ODM5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106865+OR+9422845+OR+9422846+OR+9422847%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106865,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 100996,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 102129,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 105517,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 106783,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 241734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 251313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 255849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 259614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 260180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 1183044,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106865,
        "cited_id": 2417960,
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
    "date_created": "2026-07-04T16:18:55Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: abrogated -> superseded",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T16:19:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T16:19:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T16:19:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Aguilar v. Texas

```
<div>
<center><b><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U.S. 108</a></span> (1964)</b></center>
<center><h1>AGUILAR<br>
v.<br>
TEXAS.</h1></center>
<center>No. 548.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 25-26, 1964.</center>
<center>Decided June 15, 1964.</center>
CERTIORARI TO THE COURT OF CRIMINAL APPEALS OF TEXAS.
<p><i>Clyde W. Woody</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Carl E. F. Dally</i> argued the cause for respondent. With him on the brief were <i>Waggoner Carr,</i> Attorney General of Texas, and <i>Gilbert J. Pena,</i> Assistant Attorney General.</p>
<p><span class="star-pagination">*109</span> MR. JUSTICE GOLDBERG delivered the opinion of the Court.</p>
<p>This case presents questions concerning the constitutional requirements for obtaining a state search warrant.</p>
<p>Two Houston police officers applied to a local Justice of the Peace for a warrant to search for narcotics in petitioner's home. In support of their application, the officers submitted an affidavit which, in relevant part, recited that:</p>
<blockquote>"Affiants have received reliable information from a credible person and do believe that heroin, marijuana, barbiturates and other narcotics and narcotic paraphernalia are being kept at the above described premises for the purpose of sale and use contrary to the provisions of the law."<sup>[1]</sup></blockquote>
<p>The search warrant was issued.</p>
<p>In executing the warrant, the local police, along with federal officers, announced at petitioner's door that they <span class="star-pagination">*110</span> were police with a warrant. Upon hearing a commotion within the house, the officers forced their way into the house and seized petitioner in the act of attempting to dispose of a packet of narcotics.</p>
<p>At his trial in the state court, petitioner, through his attorney, objected to the introduction of evidence obtained as a result of the execution of the warrant. The objections were overruled and the evidence admitted. Petitioner was convicted of illegal possession of heroin and sentenced to serve 20 years in the state penitentiary.<sup>[2]</sup> On appeal to the Texas Court of Criminal Appeals, the conviction was affirmed, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">172 Tex. Cr. R. 629</a></span>, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">362 S. W. 2d 111</a></span>, affirmance upheld on rehearing, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">172 Tex. Cr. R. 631</a></span>, <span class="citation" data-id="9769352"><a href="/opinion/2417960/aguillar-v-state/" aria-description="Citation for case: Aguillar v. State">362 S. W. 2d 112</a></span>. We granted a writ of certiorari to consider the important constitutional questions involved. <span class="citation multiple-matches"><a href="/c/U.%20S./375/812/">375 U. S. 812</a></span>.</p>
<p>In <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, we held that the Fourth "Amendment's proscriptions are enforced against the States through the Fourteenth Amendment," and that "the standard of reasonableness is the same under the Fourth and Fourteenth Amendments." <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California"><i>Id.,</i> at 33</a></span>. Although <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span></i> involved a search without a warrant, that case must certainly be read as holding that the standard for obtaining a search warrant is likewise "the same under the Fourth and Fourteenth Amendments."</p>
<p>An evaluation of the constitutionality of a search warrant should begin with the rule that "the informed and deliberate determinations of magistrates empowered to issue warrants . . . are to be preferred over the hurried action <span class="star-pagination">*111</span> of officers . . . who may happen to make arrests." <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 464</a></span>. The reasons for this rule go to the foundations of the Fourth Amendment. A contrary rule "that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>. Under such a rule "resort to [warrants] would ultimately be discouraged." <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#270" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 270</a></span>. Thus, when a search is based upon a magistrate's, rather than a police officer's, determination of probable cause, the reviewing courts will accept evidence of a less "judicially competent or persuasive character than would have justified an officer in acting on his own without a warrant," <i>ibid.,</i> and will sustain the judicial determination so long as "there was substantial basis for [the magistrate] to conclude that narcotics were probably present . . . ." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 271</a></span>. As so well stated by Mr. Justice Jackson:</p>
<blockquote>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States, supra,</i> at 13-14.</blockquote>
<p>Although the reviewing court will pay substantial deference to judicial determinations of probable cause, the court must still insist that the magistrate perform his "neutral and detached" function and not serve merely as a rubber stamp for the police.</p>
<p><span class="star-pagination">*112</span> In <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span>, a warrant was issued upon the sworn allegation that the affiant "has cause to suspect and does believe" that certain merchandise was in a specified location. <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#44" aria-description="Citation for case: Nathanson v. United States"><i>Id.,</i> at 44</a></span>. The Court, noting that the affidavit "went upon a mere affirmation of suspicion and belief <i>without any statement of adequate supporting facts,</i>" <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#46" aria-description="Citation for case: Nathanson v. United States"><i>id.,</i> at 46</a></span> (emphasis added), announced the following rule:</p>
<blockquote>"Under the Fourth Amendment, an officer may not properly issue a warrant to search a private dwelling unless he can find probable cause therefor from <i>facts or circumstances</i> presented to him under oath or affirmation. Mere affirmance of belief or suspicion is not enough." <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/#47" aria-description="Citation for case: Nathanson v. United States"><i>Id.,</i> at 47</a></span>. (Emphasis added.)</blockquote>
<p>The Court, in <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>, applied this rule to an affidavit similar to that relied upon here.<sup>[3]</sup> Affiant in that case swore that petitioner "did receive, conceal, etc., narcotic drugs . . . with knowledge of unlawful importation . . . ." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#481" aria-description="Citation for case: Giordenello v. United States"><i>Id.,</i> at 481</a></span>. The Court announced the guiding principles to be:</p>
<blockquote>"that the inferences from the facts which lead to the complaint `[must] be drawn by a neutral and detached <span class="star-pagination">*113</span> magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.' <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>. The purpose of the complaint, then, is to enable the appropriate magistrate . . . to determine whether the `probable cause' required to support a warrant exists. The Commissioner must judge for himself the persuasiveness of the facts relied on by a complaining officer to show probable cause. He should not accept without question the complainant's mere conclusion . . . ." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S., at 486</a></span>.</blockquote>
<p>The Court, applying these principles to the complaint in that case, stated that:</p>
<blockquote>"it is clear that it does not pass muster because it does not provide any basis for the Commissioner's determination . . . that probable cause existed. The complaint contains no affirmative allegation that the affiant spoke with personal knowledge of the matters contained therein; it does not indicate any sources for the complainant's belief; and it does not set forth any other sufficient basis upon which a finding of probable cause could be made." <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Ibid.</a></span></i>
</blockquote>
<p>The vice in the present affidavit is at least as great as in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> and <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>.</i> Here the "mere conclusion" that petitioner possessed narcotics was not even that of the affiant himself; it was that of an unidentified informant. The affidavit here not only "contains no affirmative allegation that the affiant spoke with personal knowledge of the matters contained therein," it does not even contain an "affirmative allegation" that the affiant's unidentified source "spoke with personal knowledge." For all that appears, the source here merely suspected, believed or concluded that there were narcotics in petitioner's <span class="star-pagination">*114</span> possession.<sup>[4]</sup> The magistrate here certainly could not "judge for himself the persuasiveness of the facts relied on . . . to show probable cause." He necessarily accepted "without question" the informant's "suspicion," "belief" or "mere conclusion."</p>
<p>Although an affidavit may be based on hearsay information and need not reflect the direct personal observations of the affiant, <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>, the magistrate must be informed of some of the underlying circumstances from which the informant concluded that the narcotics were where he claimed they were, and some of the underlying circumstances from which the officer concluded that the informant, whose identity need not be disclosed, see <i>Rugendorf</i> v. <i>United States,</i> <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span>, was "credible" or his information "reliable."<sup>[5]</sup> Otherwise, <span class="star-pagination">*115</span> "the inferences from the facts which lead to the complaint" will be drawn not "by a neutral and detached magistrate," as the Constitution requires, but instead, by a police officer "engaged in the often competitive enterprise of ferreting out crime," <i>Giordenello</i> v. <i>United States, supra,</i> at 486; <i>Johnson</i> v. <i>United States, supra,</i> at 14, or, as in this case, by an unidentified informant.</p>
<p>We conclude, therefore, that the search warrant should not have been issued because the affidavit did not provide a sufficient basis for a finding of probable cause and that <span class="star-pagination">*116</span> the evidence obtained as a result of the search warrant was inadmissible in petitioner's trial.</p>
<p>The judgment of the Texas Court of Criminal Appeals is reversed and the case remanded for proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>But for <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, I would have voted to affirm the judgment of the Texas court. Given <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span>,</i> I cannot escape the conclusion that to do so would tend to "relax Fourth Amendment standards . . . in derogation of law enforcement standards in the <i>federal</i> system . . ." (my concurring opinion in <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#45" aria-description="Citation for case: Ker v. California"><i>Ker, supra,</i> at 45-46</a></span>, emphasis added). Contrary to what is suggested in the dissenting opinion of my Brother CLARK in the present case (<i>post,</i> p. 118, note 1), the standards laid down in <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>, did in my view reflect constitutional requirements. Being unwilling to relax those standards for federal prosecutions, I concur in the opinion of the Court.</p>
<p>MR. JUSTICE CLARK, whom MR. JUSTICE BLACK and MR. JUSTICE STEWART join, dissenting.</p>
<p>First, it is well to point out the information upon which the search warrant in question was based: About January 1, 1960, Officers Strickland and Rogers from the narcotics division of the Houston Police Department received reliable information from a credible person that petitioner Aguilar had heroin and other narcotic drugs and narcotic paraphernalia in his possession at his residence, 509 Pinckney Street, Houston, Texas; after receiving this information the officers, the record indicates, kept the premises of petitioner under surveillance for about a week.</p>
<p>On January 8, 1960, the two officers applied for a search warrant and executed an affidavit before a justice <span class="star-pagination">*117</span> of the peace in which they alleged under oath that petitioner's residence at 509 Pinckney Street "is a place where we each have reason to believe and do believe that [Aguilar] . . . has in his possession therein narcotic drugs . . . for the purpose of the unlawful sale thereof, and where such narcotic drugs are unlawfully sold." In addition and in support of their belief, the officers included in the affidavit the further allegation that they "have received reliable information from a credible person and do believe that heroin . . . and other narcotics and narcotic paraphernalia are being kept at . . . [petitioner's] premises for the purpose of sale and use contrary to the provisions of the law."</p>
<p>Upon executing the warrant issued on the strength of this affidavit, the officers knocked on the door of Aguilar's house. Someone inside asked who was there and the officers replied that they were police and that they had a search warrant. At this they heard someone "scuffle and start to run inside of the house." The officers entered and pursued the petitioner, who ran into a back bathroom. Petitioner threw a packet of heroin into the commode, but an officer retrieved the packet before it could be flushed down the drain.</p>
<p></p>
<h2>I.</h2>
<p>At trial petitioner objected to the introduction into evidence of the heroin obtained through execution of the search warrant on the ground that the affidavit was "nothing more than hearsay." The Court holds the affidavit insufficient and sets aside the conviction on the basis of two cases, neither of which is controlling.</p>
<p>First is <i>Nathanson</i> v. <i>United States,</i> <span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">290 U. S. 41</a></span> (1933). In that case the affidavit stated that the affiant had "cause to suspect and [did] believe that certain merchandise" was in the premises described. There was nothing in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span>,</i> either in the affidavit or in the other proof introduced at trial, to suggest that any facts <span class="star-pagination">*118</span> had been brought out to support a reasonable belief or even a suspicion. Accordingly, the Court held that "[m]ere affirmance of belief or suspicion is not enough." At 47. But in Fourth Amendment cases findings of reasonableness or of probable cause necessarily rest on the facts and circumstances of each particular case. In <i>Aguilar,</i> the affidavit was based not only on "affirmance of belief" but in addition upon <i>"reliable information from a credible person"</i> plus a week's surveillance by the affiants. (Emphasis supplied.) <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> is, therefore, <i>not</i> apposite.</p>
<p>The second case the Court relies on is <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). There the affidavit alleged that "Giordenello did receive, conceal, etc., narcotic drugs, to-wit: heroin hydrochloride with knowledge of unlawful importation . . . ." The opinion of the Court, by MR. JUSTICE HARLAN, after discussing Rules 3 and 4 of the Federal Rules of Criminal Procedure, held that the defect in the complaint was that it "does not provide any basis for the Commissioner's determination under Rule 4 that probable cause existed." At 486. The dissent in the case, in commenting on the Court's holding that the complaint was invalid, said: "The Court does not strike down this complaint directly on the Fourth Amendment, but merely on an extension of Rule 4." At 491. Since <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> was a federal case, decided under our supervisory powers (Rules 3 and 4 of the Federal Rules of Criminal Procedure), it does not control here.<sup>[1]</sup> As we said in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#33" aria-description="Citation for case: Ker v. California">374 U. S. 23, 33</a></span> (1963), "the demands of our federal system compel us to distinguish between evidence held inadmissible because of our supervisory powers over federal courts and <span class="star-pagination">*119</span> that held inadmissible because prohibited by the United States Constitution."</p>
<p>Even if <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> was rested on the Constitution, it would not be controlling here because of the significant differences in the facts of the two cases. In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> the Court said: "The complaint . . . does not indicate any sources for the complainant's belief; and it does not set forth any <i>other</i> sufficient basis upon which a finding of probable cause could be made." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S., at 486</a></span>. (Emphasis supplied.) Here, in Aguilar's case, the affidavit did allege a source for the complainant's belief. <i>i. e.,</i> "reliable information from a credible person . . . that heroin . . . and other narcotics . . . are being kept" in petitioner's premises "for the purpose of sale and use contrary to the provisions of the law." This takes the affidavit here entirely outside the <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> holding. In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> no source of information was stated, whereas here there was a reliable one. The affidavit thus shows "probable cause" within the meaning of the Fourth Amendment, as that Amendment was interpreted by this Court in <i>Draper</i> v. <i>United States,</i> <span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959), where it was contended that the information given by an informant to an officer was inadmissible because it was hearsay. The Court in <i><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">Draper</a></span></i> held that petitioner was "entirely in error. <i>Brinegar</i> v. <i>United States</i> . . . has settled the question the other way." At 311. In the following year this was reaffirmed in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#271" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 271</a></span> (1960): "We conclude therefore that hearsay may be the basis for a warrant."<sup>[2]</sup><span class="star-pagination">*120</span> Furthermore, in the case of <i>Rugendorf</i> v. <i>United States</i><i>,</i> decided only this Term, we held an affidavit good based on information that an informer had seen certain furs in Rugendorf's basement. <span class="citation" data-id="9422759"><a href="/opinion/106783/rugendorf-v-united-states/" aria-description="Citation for case: Rugendorf v. United States">376 U. S. 528</a></span>. In the <i>Aguilar</i> affidavit the informer told the officers that narcotics were actually "kept at the above described premises for the purpose of sale . . . ." The Court seems to hold that what the informer says is the test of his reliability. I submit that this has nothing to do with it. The officer's experience with the informer is the test and here the two officers swore that the informer was credible and the information reliable. At the hearing on the motion to supress Officer Strickland testified that he delayed getting the search warrant for a week in order to "set up surveillance on the house." The informant's statement, Officer Strickland said, was "the first information" received and was only "some of" that which supported the application for the warrant. The totality of the circumstances upon which the officer relied is certainly pertinent to the validity of the warrant. See the use of such testimony in <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States"><i>Giordenello, supra,</i> at 485, 486</a></span>. And, just as in that case, there is nothing in the record here to show what the officers verbally told the magistrate. The surveillance of Aguilar's house, which is confirmed by the State's brief, apparently gave the officers further evidence upon which they based their personal belief. Hence the affidavit here is a far cry from "suspicion" or "affirmance of belief." It was based on reliable information from a credible informant plus personal surveillance by the officers.</p>
<p>Furthermore, the Courts of Appeals have often approved affidavits similar to the one here. See, <i>e. g., </i><i>United States</i> v. <i>Eisner,</i> <span class="citation" data-id="255849"><a href="/opinion/255849/united-states-v-samson-eisner/" aria-description="Citation for case: United States v. Samson Eisner">297 F. 2d 595</a></span> (C. A. 6th Cir.); <i>Evans</i> v. <i>United States,</i> <span class="citation" data-id="241734"><a href="/opinion/241734/add-evans-v-united-states/" aria-description="Citation for case: Add Evans v. United States">242 F. 2d 534</a></span> (C. A. 6th Cir.); <i>United States</i> v. <i>Ramirez,</i> <span class="citation" data-id="251313"><a href="/opinion/251313/united-states-v-rene-ramirez/#715" aria-description="Citation for case: United States v. Rene Ramirez">279 F. 2d 712, 715</a></span> (C. A. 2d Cir.) (dictum); and <i>United States</i> v. <i>Meeks,</i> 313 F. 2d 464 <span class="star-pagination">*121</span> (C. A. 6th Cir.). We denied certiorari in <i>Eisner,</i> <span class="citation" data-id="8943324"><a href="/opinion/8952478/eisner-v-united-states/" aria-description="Citation for case: Eisner v. United States">369 U. S. 859</a></span>, although the affidavit there stated only that "[i]nformation has been obtained by S. A. Clifford Anderson . . . which he believes to be reliable . . . ," <span class="citation" data-id="255849"><a href="/opinion/255849/united-states-v-samson-eisner/#596" aria-description="Citation for case: United States v. Samson Eisner">297 F. 2d, at 596</a></span>, and in <i>Evans,</i> <span class="citation" data-id="8931711"><a href="/opinion/8941251/evans-v-united-states/" aria-description="Citation for case: Evans v. United States">353 U. S. 976</a></span>, where the affiant was a man who "came to the headquarters of the federal liquor law enforcement officers and stated that he wished to give information . . . ," <span class="citation" data-id="241734"><a href="/opinion/241734/add-evans-v-united-states/#535" aria-description="Citation for case: Add Evans v. United States">242 F. 2d, at 535</a></span>.</p>
<p>In summary, the information must be more than mere wholly unsupported suspicion but less than "would justify condemnation," as Chief Justice Marshall said in <i>Locke</i> v. <i>United States,</i> <span class="citation" data-id="85007"><a href="/opinion/85007/locke-v-united-states/#348" aria-description="Citation for case: Locke v. United States">7 Cranch 339, 348</a></span> (1813). As Chief Justice Taft said in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925): Probable cause exists where "the facts and circumstances within their [the officers'] knowledge and of which they had reasonably trustworthy information [are] . . . sufficient in themselves to warrant a man of reasonable caution in the belief that" an offense has been or is being committed. And as Mr. Justice Rutledge so well stated in <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949):</p>
<blockquote>"These long-prevailing standards seek to safeguard citizens from rash and unreasonable interferences with privacy and from unfounded charges of crime. They also seek to give fair leeway for enforcing the law in the community's protection. Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability. The rule of probable cause is a practical, nontechnical conception affording the best compromise that has been found for accommodating these often opposing interests. <span class="star-pagination">*122</span> Requiring more would unduly hamper law enforcement. To allow less would be to leave law-abiding citizens at the mercy of the officers' whim or caprice."</blockquote>
<p>Believing that the Court has substituted a rigid, academic formula for the unrigid standards of reasonableness and "probable cause" laid down by the Fourth Amendment itselfa substitution of technicality for practicality and believing that the Court's holding will tend to obstruct the administration of criminal justice throughout the country, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[1]  The record does not reveal, nor is it claimed, that any other information was brought to the attention of the Justice of the Peace. It is elementary that in passing on the validity of a warrant, the reviewing court may consider <i>only</i> information brought to the magistrate's attention. <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>; 79 C. J. S. 872 (collecting cases). In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>,</i> the Government pointed out that the officer who obtained the warrant "had kept petitioner under surveillance for about one month prior to the arrest." The Court of course ignored this evidence, since it had not been brought to the magistrate's attention. The fact that the police may have kept petitioner's house under surveillance is thus completely irrelevant in this case, for, in applying for the warrant, the police did not mention any surveillance. Moreover, there is no evidence in the record that a surveillance was actually set up on petitioner's house. Officer Strickland merely testified that "we <i>wanted to</i> set up surveillance on the house." If the fact and results of such a surveillance had been appropriately presented to the magistrate, this would, of course, present an entirely different case.</p>
<p>[2]  Petitioner was also indicted on charges of conspiring to violate the federal narcotics laws, Act of February 9, 1909, c. 100, <span class="citation no-link">35 Stat. 614</span>, § 2, as amended, <span class="citation no-link">21 U. S. C. § 174</span>; Internal Revenue Code of 1954, § 7237 (b), as amended, <span class="citation no-link">26 U. S. C. § 7237</span> (b). He was found not guilty by the jury. His codefendants were found guilty and their convictions affirmed on appeal. <i>Garcia</i> v. <i>United States,</i> <span class="citation" data-id="260180"><a href="/opinion/260180/anthony-garcia-v-united-states/" aria-description="Citation for case: Anthony Garcia v. United States">315 F. 2d 679</a></span>.</p>
<p>[3]  In <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>,</i> although this Court construed the requirement of "probable cause" contained in Rule 4 of the Federal Rules of Criminal Procedure, it did so "in light of the constitutional" requirement of probable cause which that Rule implements. <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States"><i>Id.,</i> at 485</a></span>. The case also involved an arrest warrant rather than a search warrant, but the Court said: "The language of the Fourth Amendment, that `. . . no Warrants shall issue, but upon probable cause . . .' of course applies to arrest as well as search warrants." <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#485" aria-description="Citation for case: Giordenello v. United States"><i>Id.,</i> at 485-486</a></span>. See <i>Ex parte Burford,</i> <span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span>; <i>McGrain</i> v. <i>Daugherty,</i> <span class="citation" data-id="100996"><a href="/opinion/100996/mcgrain-v-daugherty/#154" aria-description="Citation for case: McGrain v. Daugherty">273 U. S. 135, 154-157</a></span>. The principles announced in <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> derived, therefore, fore, from the Fourth Amendment, and not from our supervisory power. Compare <i>Jencks</i> v. <i>United States,</i> <span class="citation" data-id="9421453"><a href="/opinion/105517/jencks-v-united-states/" aria-description="Citation for case: Jencks v. United States">353 U. S. 657</a></span>. Accordingly, under <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, they may properly guide our determination of "probable cause" under the Fourteenth Amendment.</p>
<p>[4]  To approve this affidavit would open the door to easy circumvention of the rule announced in <i><span class="citation" data-id="102129"><a href="/opinion/102129/nathanson-v-united-states/" aria-description="Citation for case: Nathanson v. United States">Nathanson</a></span></i> and <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>.</i> A police officer who arrived at the "suspicion," "belief" or "mere conclusion" that narcotics were in someone's possession could not obtain a warrant. But he could convey this conclusion to another police officer, who could then secure the warrant by swearing that he had "received reliable information from a credible person" that the narcotics were in someone's possession.</p>
<p>[5]  Such an affidavit was sustained by this Court in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>. The affidavit in that case reads as follows:
</p>
<p>"Affidavit in Support of a U. S. Commissioners Search Warrant for Premises 1436 Meridian Place, N. W., Washington, D. C., apartment 36, including window spaces of said apartment. Occupied by Cecil Jones and Earline Richardson.</p>
<p>"In the late afternoon of Tuesday, August 20, 1957, I, Detective Thomas Didone, Jr. received information that Cecil Jones and Earline Richardson were involved in the illicit narcotic traffic and that they kept a ready supply of heroin on hand in the above mentioned apartment. The source of information also relates that the two aforementioned persons kept these same narcotics either on their person, under a pillow, on a dresser or on a window ledge in said apartment. The source of information goes on to relate that on many occasions the source of information has gone to said apartment and purchased narcotic drugs from the above mentioned persons and that the narcotics were secreated [<i>sic</i>] in the above mentioned places. The last time being August 20, 1957.</p>
<p>"Both the aforementioned persons are familiar to the undersigned and other members of the Narcotic Squad. Both have admitted to the use of narcotic drugs and display needle marks as evidence of same.</p>
<p>"This same information, regarding the illicit narcotic traffic, conducted by Cecil Jones and Earline Richardson, has been given to the undersigned and to other officers of the narcotic squad by other sources of information.</p>
<p>"Because the source of information mentioned in the opening paragraph has given information to the undersigned on previous occasion and which was correct, and because this same information is given by other sources does believe that there is now illicit narcotic drugs being secreated [<i>sic</i>] in the above apartment by Cecil Jones and Earline Richardson.</p>
<p>"Det. Thomas Didone, Jr., Narcotic Squad, MPDC.</p>
<p>"Subscribed and sworn to before me this 21 day of August, 1957.</p>
<p>"James F. Splain, U. S. Commissioner, D. C." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States"><i>Id.,</i> at 267-268, n. 2</a></span>.</p>
<p>Compare, <i>e. g., </i><i>Hernandez</i> v. <i>People,</i> ___ Colo. ___, <span class="citation" data-id="1183044"><a href="/opinion/1183044/hernandez-v-people/" aria-description="Citation for case: Hernandez v. People">385 P. 2d 996</a></span>, where the Supreme Court of Colorado, accepting a confession of error by the State Attorney General, held that a search warrant similar to the one here in issue violated the Fourth Amendment. The court said:</p>
<p>"Before the issuing magistrate can properly perform his official function he must be apprised of the underlying facts and circumstances which show that there is probable cause . . . ." <i><span class="citation" data-id="1183044"><a href="/opinion/1183044/hernandez-v-people/" aria-description="Citation for case: Hernandez v. People">Id.,</a></span></i> at ___, <span class="citation" data-id="1183044"><a href="/opinion/1183044/hernandez-v-people/#999" aria-description="Citation for case: Hernandez v. People">385 P. 2d, at 999</a></span>.</p>
<p>[1]  MR. JUSTICE BLACK, who joined the Court's opinion in <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span>,</i> joins this dissent on the basis of his belief that <i><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">Giordenello</a></span></i> was based on Rule 4 and not on the less exacting requirements of the Fourth Amendment.</p>
<p>[2]  The affidavit in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> was more detailed, including a statement of where the heroin might be found, <i>viz.,</i> "on their person, under a pillow, on a dresser or on a window ledge in said apartment." But this detail adds nothing to the reliability of the information furnished. Likewise, the allegation in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> that the informer had "on previous occasion" given information "which was correct" was contained in substance in the <i>Aguilar</i> affidavit.</p>

</div>
```

---

## GROUP: content/cases/Alabama v. White.md  (`case`, 5 assertions)

### content_page

```
---
title: "Alabama v. White"
type: case
citation: "496 U.S. 325 (1990)"
parallel_cite: "110 S. Ct. 2412; 110 L. Ed. 2d 301"
neutral_cite: 1990 U.S. LEXIS 3053
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-06-11
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-06-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Alabama v. White
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112454/alabama-v-white/"
  cluster_id: 112454
  opinion_id: 9432055
  identity_checked: true
homes:
  - page: "[[Reasonable Suspicion]]"
    role: "Key — Progeny / Refinement"
related: ["[[Illinois v. Gates]]", "[[Florida v. J.L.]]", "[[Terry v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "reasonable-suspicion", "informants", "terry-stop"]
holding: "An anonymous tip can supply reasonable suspicion when sufficiently corroborated by police observation — especially of the tipster's…"
lake:
  record_id: Alabama v. White
  status: verified
  projected_at: 2026-07-06
---

# Alabama v. White

*496 U.S. 325 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police received an anonymous telephone tip that Vanessa White would leave a particular apartment at a stated time in a described car (a brown Plymouth station wagon with a broken right taillight), drive to Dobey's Motel, and be carrying about an ounce of cocaine in a brown attaché case. Officers watched White leave the building, enter the matching car, and drive the route toward Dobey's Motel, then stopped her; a consented search of the attaché case and her purse turned up marijuana and cocaine.

## Issue
Whether an anonymous tip, corroborated by police observation of the suspect's predicted movements, can furnish the reasonable suspicion needed for an investigatory (*[[Terry v. Ohio|Terry]]*) stop.

## Rule
Yes. Reasonable suspicion is a lower standard than probable cause and may rest on less reliable information: "Reasonable suspicion is a less demanding standard than probable cause not only in the sense that reasonable suspicion can be established with information that is different in quantity or content than that required to establish probable cause, but also in the sense that reasonable suspicion can arise from information that is less reliable than that required to show probable cause." — 496 U.S. at 330. ^pin-330

A bare anonymous tip is normally insufficient, but police corroboration of the tip's *predictions* can supply the missing reliability: "What was important was the caller's ability to predict respondent's future behavior, because it demonstrated inside information — a special familiarity with respondent's affairs." — *Id.* at 332. ^pin-332

"Although it is a close case, we conclude that under the totality of the circumstances the anonymous tip, as corroborated, exhibited sufficient indicia of reliability to justify the investigatory stop of respondent's car." — *Id.* at 332. ^pin-332a

## Application
The anonymous tip here, standing alone, gave no basis to think the caller was honest or well informed. But the police corroborated significant details — most importantly the caller's accurate prediction of White's *future* conduct (the time she left, the described car, the route toward Dobey's Motel) — which showed the tipster had inside knowledge and made it reasonable to credit the tip's assertion about criminal activity. On the totality of these facts, the corroborated tip carried enough indicia of reliability to justify the stop, "[a]lthough it is a close case."

## Conclusion
The investigatory stop was supported by reasonable suspicion; the Alabama Court of Criminal Appeals' suppression judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *White* anchors the rule that police corroboration of an anonymous tip's predictive detail can supply reasonable suspicion. The line was refined by [[Florida v. J.L.]] (a bare anonymous tip of a concealed gun, lacking predictive corroboration, is **not** reasonable suspicion) and applied in [[Navarette v. California]] (a contemporaneous, reliable 911 report can supply reasonable suspicion).

## Appears on
- [[Reasonable Suspicion]] — *Key — Progeny / Refinement*

## Sources
- *Alabama v. White*, 496 U.S. 325 (1990) — https://www.courtlistener.com/opinion/112454/alabama-v-white/ — pinpoints: 330, 332.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1a1e91e96f0eb639", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "496 U.S. 325 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 3053", "official_citation_present": true, "parallel_cite": "110 S. Ct. 2412; 110 L. Ed. 2d 301", "title": "Alabama v. White", "year": "1990"}}
{"assertion_id": "32476015d6ef438e", "dimension": "support", "kind": "home_role", "locator": {"home": "Reasonable Suspicion"}, "payload": {"home": "Reasonable Suspicion", "role": "Key — Progeny / Refinement", "title": "Alabama v. White"}}
{"assertion_id": "bf6b849bae091b5f", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "An anonymous tip can supply reasonable suspicion when sufficiently corroborated by police observation — especially of the tipster's…", "title": "Alabama v. White"}}
{"assertion_id": "172ded232f662dc2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-06-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Alabama v. White", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Alabama v. White", "varies_by_point": "false"}}
{"assertion_id": "3942f49f8c64198e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Alabama v. White"}}
```

### lake record — Alabama v. White

```json
{
  "schema_version": "s2.v1",
  "record_id": "Alabama v. White",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Alabama v. White",
    "case_name_short": "White",
    "case_name_full": "Alabama v. White",
    "input_case_name": "Alabama v. White",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-06-11",
    "year": 1990,
    "docket": null,
    "cluster_id": 112454,
    "lead_opinion_id": 9432055,
    "sibling_ids": [
      112454,
      9432055,
      9432056
    ],
    "absolute_url": "/opinion/112454/alabama-v-white/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9094334,
        "score": 10,
        "case_name": "Alabama v. White"
      },
      {
        "cluster_id": 9094333,
        "score": 10,
        "case_name": "Alabama v. White"
      },
      {
        "cluster_id": 9094069,
        "score": 10,
        "case_name": "Alabama v. White"
      },
      {
        "cluster_id": 9094068,
        "score": 10,
        "case_name": "Alabama v. White"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "496 U.S. 325",
      "volume": "496",
      "reporter": "U.S.",
      "page": "325",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 2412",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 301",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "301",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 3053",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3053",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "496 U.S. 325",
        "volume": "496",
        "reporter": "U.S.",
        "page": "325",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 2412",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2412",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 301",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "301",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 3053",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3053",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "496 U.S. 325",
    "official_selection": {
      "court_class": "scotus",
      "selected": "496 U.S. 325",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-330",
      "page": null,
      "quote": "--- # Alabama v. White *496 U.S. 325 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police received an anonymous telephone tip that Vanessa White would leave a particular apartment at a stated time in a described car (a brown Plymouth station wagon with a broken right taillight), drive to Dobey's Motel, and be carrying about an ounce of cocaine in a brown attach\u00e9 case. Officers watched White leave the building, enter the matching car, and drive the route toward Dobey's Motel, then stopped her; a consented search of the attach\u00e9 case and her purse turned up marijuana and cocaine. ## Issue Whether an anonymous tip, corroborated by police observation of the suspect's predicted movements, can furnish the reasonable suspicion needed for an investigatory (*Terry*) stop. ## Rule Yes. Reasonable suspicion is a lower standard than probable cause and may rest on less reliable information:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-332",
      "page": null,
      "quote": "What was important was the caller's ability to predict respondent's future behavior, because it demonstrated inside information \u2014 a special familiarity with respondent's affairs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-332a",
      "page": null,
      "quote": "Although it is a close case, we conclude that under the totality of the circumstances the anonymous tip, as corroborated, exhibited sufficient indicia of reliability to justify the investigatory stop of respondent's car.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-06-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Alabama v. White",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "The People of the State of Colorado, In the Interest of T.J.W., Juvenile-Appellee L.C.W. and D.W. and Concerning",
          "cluster_id": 10871666,
          "cite": [
            "2026 CO 38"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kopp v. State",
          "cluster_id": 10864408,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ruhenkamp",
          "cluster_id": 10859425,
          "cite": [
            "2026 Ohio 1791"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Santiago Tulul Sac v. the State of Texas",
          "cluster_id": 10852455,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "D.D.B. v. State of Alabama",
          "cluster_id": 10825053,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hallowell",
          "cluster_id": 10815601,
          "cite": [
            "2026 Ohio 1036"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Porter",
          "cluster_id": 10810059,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Augustine Perez",
          "cluster_id": 10799852,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stone",
          "cluster_id": 10780071,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Coleman",
          "cluster_id": 10778727,
          "cite": [
            "2026 Ohio 203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "HERNANDEZ, ISRAEL GARCIA v. the State of Texas",
          "cluster_id": 10762683,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tower",
          "cluster_id": 10759279,
          "cite": [
            "2025 Ohio 5593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Swanson v. State",
          "cluster_id": 10758425,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bryant",
          "cluster_id": 10747664,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Florida v. Milton",
          "cluster_id": 10750969,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Leighton R.",
          "cluster_id": 10742062,
          "cite": [
            "2025 NY Slip Op 06534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thomas Wesley Hollingsworth v. Commonwealth of Virginia",
          "cluster_id": 10741964,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Huerta",
          "cluster_id": 10713908,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Williams v. State of Florida",
          "cluster_id": 10751673,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jenkins",
          "cluster_id": 10677845,
          "cite": [
            "2025 Ohio 4447"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Chuppa",
          "cluster_id": 10664732,
          "cite": [
            "2025 Ohio 3117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "D.W. v. United States",
          "cluster_id": 10635093,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Solon v. Moore",
          "cluster_id": 10626717,
          "cite": [
            "2025 Ohio 2446"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wolfe",
          "cluster_id": 10604482,
          "cite": [
            "2025 Ohio 2096"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Parker & Rollerson v. United States",
          "cluster_id": 10380432,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shannon",
          "cluster_id": 10373759,
          "cite": [
            "2025 Ohio 1224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Currie",
          "cluster_id": 10347567,
          "cite": [
            "2025 Ohio 670"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Duane Gary Underwood, II",
          "cluster_id": 10340565,
          "cite": [
            "129 F.4th 912"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sidor",
          "cluster_id": 10145062,
          "cite": [
            "558 P.3d 621"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Degenhardt v. Bintliff",
          "cluster_id": 10124683,
          "cite": [
            "117 F.4th 747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Parma v. Coyne",
          "cluster_id": 10097418,
          "cite": [
            "2024 Ohio 3192"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Racheal Michelle Swanger v. the State of Texas",
          "cluster_id": 10059209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The State of Texas v. Antonio Juarez",
          "cluster_id": 10052886,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Langston",
          "cluster_id": 10028974,
          "cite": [
            "110 F.4th 408"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of New Jersey v. Mary Mellody",
          "cluster_id": 9997741,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kirby",
          "cluster_id": 9988138,
          "cite": [
            "2024 Ohio 2543"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Michael Gene Wiskowski",
          "cluster_id": 9576066,
          "cite": [
            "2024 WI 23"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Michael Gene Wiskowski",
          "cluster_id": 9567763,
          "cite": [
            "2024 WI 23"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dorian Deon McMullen",
          "cluster_id": 9514037,
          "cite": [
            "103 F.4th 1225"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shaw",
          "cluster_id": 9507576,
          "cite": [
            "2024 Ohio 2022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mayo v. United States",
          "cluster_id": 9506506,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mitchell v. United States",
          "cluster_id": 9500665,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Frederick Lorenzo Brooks v. the State of Texas",
          "cluster_id": 9487280,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McDougal v. State",
          "cluster_id": 9486694,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams",
          "cluster_id": 9484217,
          "cite": [
            "237 N.E.3d 948",
            "2024 Ohio 943"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Stephenson",
          "cluster_id": 9480259,
          "cite": [
            "236 N.E.3d 342",
            "2024 Ohio 624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cleveland Hts. v. Jackson",
          "cluster_id": 9473537,
          "cite": [
            "2024 Ohio 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rowland",
          "cluster_id": 9455992,
          "cite": [
            "232 N.E.3d 970",
            "2023 Ohio 4806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arun Rashid Turay v. Commonwealth of Virginia",
          "cluster_id": 9453329,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Houle",
          "cluster_id": 9453132,
          "cite": [
            "2023 Ohio 4609"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Payne",
          "cluster_id": 9443920,
          "cite": [
            "2023 Ohio 4198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hicks",
          "cluster_id": 9441433,
          "cite": [
            "229 N.E.3d 172",
            "2023 Ohio 4126"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Houston",
          "cluster_id": 9439762,
          "cite": [
            "2023 Ohio 4101"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Partin",
          "cluster_id": 9438413,
          "cite": [
            "2023 Ohio 4056"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jackson, K., Aplt.",
          "cluster_id": 9429769,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Jackson, K., Aplt.",
          "cluster_id": 9429768,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joanna Ellen Hopkins A/K/A Jeanna Hopkins v. the State of Texas",
          "cluster_id": 9419886,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Junjie Li State v. Zhong Kuang",
          "cluster_id": 9416202,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andre Small v. the State of Texas",
          "cluster_id": 9411292,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jeremiah Ray Janes",
          "cluster_id": 9408153,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wishon",
          "cluster_id": 9405314,
          "cite": [
            "2023 Ohio 1915"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Noli",
          "cluster_id": 9399584,
          "cite": [
            "412 Mont. 170",
            "529 P.3d 813",
            "2023 MT 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hein",
          "cluster_id": 9398655,
          "cite": [
            "2023 Ohio 1592"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rusty Alton Pearce v. the State of Texas",
          "cluster_id": 9390265,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 9385722,
          "cite": [
            "2023 Ohio 844"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Justin Thabit",
          "cluster_id": 9356749,
          "cite": [
            "56 F.4th 1145"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Washington v. State",
          "cluster_id": 10048684,
          "cite": [
            "482 Md. 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Washington v. State",
          "cluster_id": 9351030,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bearer",
          "cluster_id": 9350993,
          "cite": [
            "203 N.E.3d 1207",
            "2022 Ohio 4554"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Martin",
          "cluster_id": 9287921,
          "cite": [
            "170 Ohio St. 3d 181",
            "209 N.E.3d 688",
            "2022 Ohio 4175"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Timothy Barclift",
          "cluster_id": 8244189,
          "cite": [
            "282 A.3d 607",
            "2022 ME 50"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rose",
          "cluster_id": 8240204,
          "cite": [
            "48 F.4th 297"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Huntley",
          "cluster_id": 6620233,
          "cite": [
            "513 P.3d 1141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re: D.D.",
          "cluster_id": 10048705,
          "cite": [
            "479 Md. 206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re: D.D.",
          "cluster_id": 6479680,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fenderson",
          "cluster_id": 6476863,
          "cite": [
            "2022 Ohio 1973"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. M. Zeimer",
          "cluster_id": 6471485,
          "cite": [
            "510 P.3d 100",
            "2022 MT 96"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesus Cortez Jr. v. the State of Texas",
          "cluster_id": 6468697,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Freddie Clark",
          "cluster_id": 6463652,
          "cite": [
            "32 F.4th 1080"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jordan",
          "cluster_id": 9353271,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Patrick Bracy",
          "cluster_id": 6452507,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "the State of Texas v. Justin Sirucek",
          "cluster_id": 6246684,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rasheed",
          "cluster_id": 5311228,
          "cite": [
            "2021 Ohio 4509"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 5306903,
          "cite": [
            "454 Ill. Dec. 624",
            "190 N.E.3d 224",
            "2021 IL 125954"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Taylor",
          "cluster_id": 5305434,
          "cite": [
            "2021 Ohio 4338"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin (Weslie) Vs. State",
          "cluster_id": 5302975,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Siegel",
          "cluster_id": 5302012,
          "cite": [
            "180 N.E.3d 574",
            "2021 Ohio 4208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jacobe Dante Payton v. the State of Texas",
          "cluster_id": 5287168,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wear",
          "cluster_id": 5150028,
          "cite": [
            "2021 Ohio 3384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "the State of Texas v. Georgia Donnell",
          "cluster_id": 5173560,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marcus Gardner v. the State of Texas",
          "cluster_id": 5093032,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "the State of Texas v. Brandon Nicholas Martinez",
          "cluster_id": 5090970,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. James Bernard Braddy",
          "cluster_id": 5064977,
          "cite": [
            "11 F.4th 1298"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
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
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ferrell",
          "cluster_id": 4958148,
          "cite": [
            "2021 Ohio 2826"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Weaver",
          "cluster_id": 4957807,
          "cite": [
            "9 F.4th 129"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 4985025,
          "cite": [
            "2021 Ohio 2853"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Guam v. Erty Yerten",
          "cluster_id": 5308335,
          "cite": [
            "2021 Guam 8"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maximo Gondres-Medrano",
          "cluster_id": 4898417,
          "cite": [
            "3 F.4th 708"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tidwell (Slip Opinion)",
          "cluster_id": 4894377,
          "cite": [
            "165 Ohio St. 3d 57",
            "175 N.E.3d 527",
            "2021 Ohio 2072"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Jefferson, T.",
          "cluster_id": 10279155,
          "cite": [
            "2021 Pa. Super. 116",
            "256 A.3d 1242"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Heather Jan VanBeek",
          "cluster_id": 4889174,
          "cite": [
            "960 N.W.2d 32",
            "397 Wis. 2d 311",
            "2021 WI 51"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne Sheckles",
          "cluster_id": 4879211,
          "cite": [
            "996 F.3d 330"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Lafaris Brown",
          "cluster_id": 4877575,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Victoria Catherine Pagano",
          "cluster_id": 6248596,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Birdie Jean Jackson v. State",
          "cluster_id": 4877053,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Victoria Catherine Pagano",
          "cluster_id": 4876573,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Juan Antonio Gutierrez v. State",
          "cluster_id": 4876118,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Alvaranga",
          "cluster_id": 4870748,
          "cite": [
            "2021 Ohio 1130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Reagan v. Idaho Transportation Department",
          "cluster_id": 10732814,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Norbert",
          "cluster_id": 4865031,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Norbert",
          "cluster_id": 4864552,
          "cite": [
            "990 F.3d 968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Spain",
          "cluster_id": 4863382,
          "cite": [
            "2019 IL App (1st) 163184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Maloney",
          "cluster_id": 4860984,
          "cite": [
            "990 F.3d 232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yoder",
          "cluster_id": 4858742,
          "cite": [
            "2021 Ohio 496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lamont Lendell Bagley v. Commonwealth of Virginia",
          "cluster_id": 4858369,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 4853848,
          "cite": [
            "2019 IL App (1st) 170803"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tracy Todd Adrian",
          "cluster_id": 4853916,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cherry",
          "cluster_id": 4852863,
          "cite": [
            "2020 IL App (3d) 170622"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Shaka Markel Long v. Commonwealth of Virginia",
          "cluster_id": 4850847,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Redding",
          "cluster_id": 4840616,
          "cite": [
            "2020 IL App (4th) 190252"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jones",
          "cluster_id": 4838859,
          "cite": [
            "2020 Ohio 6667"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Edgerrin J.",
          "cluster_id": 4838065,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Edgerrin J.",
          "cluster_id": 4837847,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Edgerrin J.",
          "cluster_id": 4820971,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kendrick Brinkley",
          "cluster_id": 4805913,
          "cite": [
            "980 F.3d 377"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Salvador Ortiz, Jr. v. State",
          "cluster_id": 4802321,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 4800744,
          "cite": [
            "2020 Ohio 5062"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Toddrey Willie Bruce",
          "cluster_id": 4794438,
          "cite": [
            "977 F.3d 1112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Robert Hinshaw",
          "cluster_id": 4781551,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Armando Zubiate",
          "cluster_id": 4782216,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sexton",
          "cluster_id": 4777807,
          "cite": [
            "2020 Ohio 4179"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. David Rivera",
          "cluster_id": 4768195,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bonner",
          "cluster_id": 10733093,
          "cite": [
            "167 Idaho 88",
            "467 P.3d 452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Redding",
          "cluster_id": 4832649,
          "cite": [
            "158 N.E.3d 728",
            "442 Ill. Dec. 8",
            "2020 IL App (4th) 190252"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "E.P. v. State of Indiana (mem. dec.)",
          "cluster_id": 4756186,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leatherwood",
          "cluster_id": 4755117,
          "cite": [
            "2020 Ohio 3012"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Howell",
          "cluster_id": 4751258,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Howell",
          "cluster_id": 4751225,
          "cite": [
            "958 F.3d 589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Howell",
          "cluster_id": 4751157,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Howell",
          "cluster_id": 4751054,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amanuel Gebrengus Atsemet v. State",
          "cluster_id": 4750757,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kansas v. Glover",
          "cluster_id": 4742386,
          "cite": [
            "589 U.S. 376"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rutherford",
          "cluster_id": 4742005,
          "cite": [
            "2020 Ohio 1309"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ibrahim McCants",
          "cluster_id": 4735359,
          "cite": [
            "952 F.3d 416"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Homero Avitia Retana v. State",
          "cluster_id": 4731301,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brian Keith Houston v. State",
          "cluster_id": 4725186,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tracy Ray Conn, III v. State",
          "cluster_id": 4691601,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tidwell",
          "cluster_id": 4675183,
          "cite": [
            "2019 Ohio 4493"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 4672911,
          "cite": [
            "2019 Ohio 4370"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Kevin Dupart",
          "cluster_id": 10610205,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Ryan Bradley Tostenson",
          "cluster_id": 4668094,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lee",
          "cluster_id": 4666807,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cook",
          "cluster_id": 4664974,
          "cite": [
            "2019 Ohio 3918"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kenneth Aaron Mims v. State",
          "cluster_id": 4664361,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Billy Curry, Jr.",
          "cluster_id": 4658859,
          "cite": [
            "937 F.3d 363"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mendoza",
          "cluster_id": 4655175,
          "cite": [
            "2019 Ohio 3382"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Alexander",
          "cluster_id": 4649354,
          "cite": [
            "2019 Ohio 3310"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sharpfish",
          "cluster_id": 9507818,
          "cite": [
            "2019 S.D. 49"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Collier",
          "cluster_id": 4647022,
          "cite": [
            "2019 Ohio 3197"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Goins",
          "cluster_id": 4645553,
          "cite": [
            "2019 Ohio 3135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gregory",
          "cluster_id": 4643189,
          "cite": [
            "2019 Ohio 3000"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Holmes",
          "cluster_id": 4635398,
          "cite": [
            "2019 IL App (1st) 160987"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re E.H.",
          "cluster_id": 4633647,
          "cite": [
            "2019 Ohio 2572"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Keefer",
          "cluster_id": 4630914,
          "cite": [
            "2019 Ohio 2419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerry Weakley v. State of Florida",
          "cluster_id": 4627371,
          "cite": [
            "273 So. 3d 283"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Brown",
          "cluster_id": 4626950,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Brown",
          "cluster_id": 4626337,
          "cite": [
            "925 F.3d 1150"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Phillip Orlando Naylor",
          "cluster_id": 4626259,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rubsam",
          "cluster_id": 4625545,
          "cite": [
            "2019 Ohio 2153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Haynesworth",
          "cluster_id": 4622522,
          "cite": [
            "2019 Ohio 1986"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hairston (Slip Opinion)",
          "cluster_id": 4615930,
          "cite": [
            "2019 Ohio 1622",
            "126 N.E.3d 1132",
            "156 Ohio St. 3d 363"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tre Ron Smith v. State of Indiana",
          "cluster_id": 4608429,
          "cite": [
            "121 N.E.3d 669"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre Cherry",
          "cluster_id": 4607955,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Deandre Cherry",
          "cluster_id": 4607774,
          "cite": [
            "920 F.3d 1126"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ibrahim McCants",
          "cluster_id": 4607416,
          "cite": [
            "920 F.3d 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Davis",
          "cluster_id": 4603580,
          "cite": [
            "203 A.3d 1233",
            "331 Conn. 239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Justin Andre Baker",
          "cluster_id": 4604978,
          "cite": [
            "925 N.W.2d 602"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gaines",
          "cluster_id": 4598762,
          "cite": [
            "918 F.3d 793"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MELISSA PETERSON v. STATE OF FLORIDA",
          "cluster_id": 4596997,
          "cite": [
            "264 So. 3d 1183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Beasley",
          "cluster_id": 4595118,
          "cite": [
            "2019 Ohio 719"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Megan Barrett Jefferies v. State",
          "cluster_id": 4586027,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ibrahim McCants",
          "cluster_id": 4574345,
          "cite": [
            "911 F.3d 127"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. James",
          "cluster_id": 4573941,
          "cite": [
            "2018 Ohio 5033"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ernest Foster, Sr. v. Jeremy Hellawell",
          "cluster_id": 4565912,
          "cite": [
            "908 F.3d 1204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Alexander",
          "cluster_id": 4564129,
          "cite": [
            "2018 Ohio 4581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "J.H., A CHILD v. STATE OF FLORIDA",
          "cluster_id": 4548771,
          "cite": [
            "257 So. 3d 1071"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fausto Lopez",
          "cluster_id": 4545359,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fausto Lopez",
          "cluster_id": 4545246,
          "cite": [
            "907 F.3d 472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barbeau",
          "cluster_id": 4567022,
          "cite": [
            "301 Neb. 293"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guzman v. State",
          "cluster_id": 2449770,
          "cite": [
            "955 S.W.2d 85",
            "1997 Tex. Crim. App. LEXIS 72",
            "1997 WL 587024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
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
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Idaho v. Wright",
          "cluster_id": 112488,
          "cite": [
            "111 L. Ed. 2d 638",
            "110 S. Ct. 3139",
            "497 U.S. 805",
            "1990 U.S. LEXIS 3461",
            "30 Fed. R. Serv. 24",
            "58 U.S.L.W. 5036"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. JL",
          "cluster_id": 118352,
          "cite": [
            "146 L. Ed. 2d 254",
            "120 S. Ct. 1375",
            "529 U.S. 266",
            "2000 U.S. LEXIS 2345",
            "13 Fla. L. Weekly Fed. S 216",
            "68 U.S.L.W. 4236",
            "2000 Cal. Daily Op. Serv. 2409",
            "2000 Colo. J. C.A.R. 1642",
            "2000 Daily Journal DAR 3226"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
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
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
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
        "journal_ref": "Alabama v. White:lane2_top_cited"
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
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGee v. Commonwealth",
          "cluster_id": 1067400,
          "cite": [
            "487 S.E.2d 259",
            "25 Va. App. 193",
            "1997 Va. App. LEXIS 444"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rubin Sira v. R. Morton, C. Artuz, D. Selsky, and G. Goord",
          "cluster_id": 787387,
          "cite": [
            "380 F.3d 57",
            "2004 WL 1837779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Archer v. Commonwealth",
          "cluster_id": 1067256,
          "cite": [
            "492 S.E.2d 826",
            "26 Va. App. 1",
            "1997 Va. App. LEXIS 683"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Binette",
          "cluster_id": 1060555,
          "cite": [
            "33 S.W.3d 215",
            "2000 Tenn. LEXIS 605",
            "2000 WL 1473900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mcpherson v. Kelsey",
          "cluster_id": 746760,
          "cite": [
            "125 F.3d 989",
            "1997 U.S. App. LEXIS 26946"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Keith",
          "cluster_id": 1060825,
          "cite": [
            "978 S.W.2d 861",
            "1998 Tenn. LEXIS 521",
            "1998 WL 661198"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Derichsweiler v. State",
          "cluster_id": 2539048,
          "cite": [
            "348 S.W.3d 906",
            "2011 Tex. Crim. App. LEXIS 112",
            "2011 WL 255299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
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
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Andre Cardell King, United States of America v. Chalmers Lavette Hendricks",
          "cluster_id": 744073,
          "cite": [
            "119 F.3d 290",
            "1997 U.S. App. LEXIS 18965"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Christopher Lee Davis",
          "cluster_id": 1043997,
          "cite": [
            "354 S.W.3d 718",
            "2011 Tenn. LEXIS 962"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Kevin Gamble (071234)",
          "cluster_id": 2686119,
          "cite": [
            "218 N.J. 412",
            "95 A.3d 188",
            "2014 WL 3858497",
            "2014 N.J. LEXIS 801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 2541531,
          "cite": [
            "348 S.W.3d 919",
            "2011 Tex. Crim. App. LEXIS 912",
            "2011 WL 2555712"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas L. Feathers Kathleen Feathers v. William Aey J.P. Donohue, City of Akron",
          "cluster_id": 780866,
          "cite": [
            "319 F.3d 843",
            "2003 U.S. App. LEXIS 2642",
            "2003 WL 296924"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Beal, Jr. v. James Beller",
          "cluster_id": 4348069,
          "cite": [
            "847 F.3d 897",
            "2017 WL 544599",
            "2017 U.S. App. LEXIS 2439"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alabama v. White:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112454 OR 9432055 OR 9432056) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTM5MzAyNDAwMDAwJnM9NDU2NzAyMiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112454+OR+9432055+OR+9432056%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 190
      },
      "lane2_top_cited": {
        "query": "cites:(112454 OR 9432055 OR 9432056)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMzgmcz0xMDU5MDk1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112454+OR+9432055+OR+9432056%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 24
      },
      "lane3_recency": {
        "query": "cites:(112454 OR 9432055 OR 9432056)",
        "reviewed": 70,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 70,
        "triage_read": 0,
        "triage_snippet_classified": 70
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112454 OR 9432055 OR 9432056)",
    "indexed_citing_opinions": 2054,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112454,
        "count": 1832,
        "count_source": "search"
      },
      {
        "opinion_id": 9432055,
        "count": 255,
        "count_source": "search"
      },
      {
        "opinion_id": 9432056,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3282,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/alabama-v-white.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwMDQyNzEmcz0xMDEyNjA1NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112454+OR+9432055+OR+9432056%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112454,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 112239,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 1796245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112454,
        "cited_id": 1796971,
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
    "date_created": "2026-07-04T16:43:14Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T16:43:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T16:43:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T17:01:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T16:43:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Alabama v. White

```
<opinion type="majority">
<author id="b368-9">Justice White</author>
<p id="Avl">delivered the opinion of the Court.</p>
<p id="b368-10">Based on an anonymous telephone tip, police stopped respondent’s vehicle. A consensual search of the car revealed drugs. The issue is whether the tip, as corroborated by in<page-number citation-index="1" label="327">*327</page-number>dependent police work, exhibited sufficient indicia of reliability to provide reasonable suspicion to make the investigatory stop. We hold that it did.</p>
<p id="b369-5">On April 22, 1987, at approximately 3 p.m., Corporal B. H. Davis of the Montgomery Police Department received a telephone call from an anonymous person, stating that Vanessa White would be leaving 235-C Lynwood Terrace Apartments at a particular time in a brown Plymouth station wagon with the right taillight lens broken, that she would be going to Dobey’s Motel, and that she would be in possession of about an ounce of cocaine inside a brown attaché case. Corporal Davis and his partner, Corporal P. A. Reynolds, proceeded to the Lynwood Terrace Apartments. The officers saw a brown Plymouth station wagon with a broken right taillight in the parking lot in front of the 235 building. The officers observed respondent leave the 235 building, carrying nothing in her hands, and enter the station wagon. They followed the vehicle as it drove the most direct route to Dobey’s Motel. When the vehicle reached the Mobile Highway, on which Dobey’s Motel is located, Corporal Reynolds requested a patrol unit to stop the vehicle. The vehicle was stopped at approximately 4:18 p.m., just short of Dobey’s Motel. Corporal Davis asked respondent to step to the rear of her car, where he informed her that she had been stopped because she was suspected of carrying cocaine in the vehicle. He asked if they could look for cocaine, and respondent said they could look. The officers found a locked brown attaché case in the car, and, upon request, respondent provided the combination to the lock. The officers found marijuana in the attaché case and placed respondent under arrest. During processing at the station, the officers found three milligrams of cocaine in respondent’s purse.</p>
<p id="b369-6">Respondent was charged in Montgomery County Court with possession of marijuana and possession of cocaine. The trial court denied respondent’s motion to suppress, and she pleaded guilty to the charges, reserving the right to appeal <page-number citation-index="1" label="328">*328</page-number>the denial of her suppression motion. The Court of Criminal Appeals of Alabama held that the officers did not have the reasonable suspicion necessary under <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), to justify the investigatory stop of respondent’s car, and that the marijuana and cocaine were fruits of respondent’s unconstitutional detention. The court concluded that respondent’s motion to dismiss should have been granted and reversed her conviction. <span class="citation" data-id="1796971"><a href="/opinion/1796971/white-v-state/" aria-description="Citation for case: White v. State">550 So. 2d 1074</a></span> (1989). The Supreme Court of Alabama denied the State’s petition for writ of certiorari, two justices dissenting. <span class="citation" data-id="9938491"><a href="/opinion/1796245/white-v-state/" aria-description="Citation for case: White v. State">550 So. 2d 1081</a></span> (1989). Because of differing views in the state and federal courts over whether an anonymous tip may furnish reasonable suspicion for a stop, we granted the State’s petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./493/1042/">493 U. S. 1042</a></span> (1990). We now reverse.</p>
<p id="b370-5"><em>Adams </em>v. <em>Williams, </em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972), sustained a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop and frisk undertaken on the basis of a tip given in person by a known informant who had provided information in the past. We concluded that, while the unverified tip may have been insufficient to support an arrest or search warrant, the information carried sufficient “indicia of reliability” to justify a forcible stop. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">407 U. S., at 147</a></span>. We did not address the issue of anonymous tips in <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Adams</a></span>, </em>except to say that “[t]his is a stronger case than obtains in the case of an anonymous telephone tip,” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams"><em>id., </em>at 146</a></span>.</p>
<p id="b370-6"><em>Illinois </em>v. <em>Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">462 U. S. 213</a></span> (1983), dealt with an anonymous tip in the probable-cause context. The Court there abandoned the “two-pronged test” of <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964), and <em>Spinelli </em>v. <em>United States, </em><span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969), in favor of a “totality of the circumstances” approach to determining whether an informant’s tip establishes probable cause. <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>made clear, however, that those factors that had been considered critical under <em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">Aguilar</a></span> </em>and <em>Spinelli—an </em>informant’s “veracity,” “reliability,” and “basis of knowledge”—remain “highly relevant in determining the value of his report.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#230" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 230</a></span>. These factors are also relevant in the reasonable-suspicion context, although al<page-number citation-index="1" label="329">*329</page-number>lowance must be made in applying them for the lesser showing required to meet that standard.</p>
<p id="b371-5">The opinion in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>recognized that an anonymous tip alone seldom demonstrates the informant’s basis of knowledge or veracity inasmuch as ordinary citizens generally do not provide extensive recitations of the basis of their everyday observations and given that the veracity of persons supplying anonymous tips is “by hypothesis largely unknown, and unknowable.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#237" aria-description="Citation for case: Illinois v. Gates"><em>Id., </em>at 237</a></span>. This is not to say that an anonymous caller could never provide the reasonable suspicion necessary for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop. But the tip in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>was not an exception to the general rule, and the anonymous tip in this case is like the one in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span>: </em>“[It] provides virtually nothing from which one might conclude that [the caller] is either honest or his information reliable; likewise, the [tip] gives absolutely no indication of the basis for the [caller’s] predictions regarding [Vanessa White’s] criminal activities.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#227" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 227</a></span>. By requiring “[s]omething more,” as <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>did, <em>ibid., </em>we merely apply what we said in <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Adams</a></span>: </em>“Some tips, completely lacking in indicia of reliability, would either warrant no police response or require further investigation before a forcible stop of a suspect would be authorized,” <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">407 U. S., at 147</a></span>. Simply put, a tip such as this one, standing alone, would not “‘warrant a man of reasonable caution in the belief’ that [a stop] was appropriate.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio"><em>Terry, supra, </em>at 22</a></span>, quoting <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925).</p>
<p id="b371-6">As there was in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span>, </em>however, in this case there is more than the tip itself. The tip was not as detailed, and the corroboration was not as complete, as in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span>, </em>but the required degree of suspicion was likewise not as high. We discussed the difference in the two standards last Term in <em>United States </em>v. <em>Sokolow, </em><span class="citation" data-id="9431641"><a href="/opinion/112239/united-states-v-sokolow/#7" aria-description="Citation for case: United States v. Sokolow">490 U. S. 1, 7</a></span> (1989):</p>
<blockquote id="b371-7">“The officer [making a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop]. . . must be able to articulate something more than an ‘inchoate and unparticularized suspicion or “hunch.”’ <em>[Terry, </em>392 U. S.,] at 27. The Fourth Amendment requires ‘some minimal <page-number citation-index="1" label="330">*330</page-number>level of objective justification’ for making the stop. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#217" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 217</a></span> (1984). That level of suspicion is considerably less than proof of wrongdoing by a preponderance of the evidence. We have held that probable cause means ‘a fair probability that contraband or evidence of a crime will be found,’ <em>[Gates, </em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#238" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 238</a></span>], and the level of suspicion required for a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop is obviously less demanding than for probable cause.”</blockquote>
<p id="b372-5">Reasonable suspicion is a less demanding standard than probable cause not only in the sense that reasonable suspicion can be established with information that is different in quantity or content than that required to establish probable cause, but also in the sense that reasonable suspicion can arise from information that is less reliable than that required to show probable cause. <em>Adams </em>v. <em><span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">Williams, supra,</a></span> </em>demonstrates as much. We there assumed that the unverified tip from the known informant might not have been reliable enough to establish probable cause, but nevertheless found it sufficiently reliable to justify a <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span> </em>stop. <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#147" aria-description="Citation for case: Adams v. Williams">407 U. S., at 147</a></span>. Reasonable suspicion, like probable cause, is dependent upon both the content of information possessed by police and its degree of reliability. Both factors—quantity and quality—are considered in the “totality of the circumstances—the whole picture,” <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417</a></span> (1981), that must be taken into account when evaluating whether there is reasonable suspicion. Thus, if a tip has a relatively low degree of reliability, more information will be required to establish the requisite quantum of suspicion than would be required if the tip were more reliable. The <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>Court applied its totality-of-the-circumstances approach in this manner, taking into account the facts known to the officers from personal observation, and giving the anonymous tip the weight it deserved in light of its indicia of reliability as established through independent police work. The same approach applies in the reasonable-suspicion context, the only differ<page-number citation-index="1" label="331">*331</page-number>ence being the level of suspicion that must be established. Contrary to the court below, we conclude that when the officers stopped respondent, the anonymous tip had been sufficiently corroborated to furnish reasonable suspicion that respondent was engaged in criminal activity and that the investigative stop therefore did not violate the Fourth Amendment.</p>
<p id="b373-5">It is true that not every detail mentioned by the tipster was verified, such as the name of the woman leaving the building or the precise apartment from which she left; but the officers did corroborate that a woman left the 235 building and got into the particular vehicle that was described by the caller. With respect to the time of departure predicted by the informant, Corporal Davis testified that the caller gave a particular time when the woman would be leaving, App. 5, but he did not state what that time was. He did testify that, after the call, he and his partner proceeded to the Lynwood Terrace Apartments to put the 235 building under surveillance, <em>id., </em>at 5-6. Given the fact that the officers proceeded to the indicated address immediately after the call and that respondent emerged not too long thereafter, it appears from the record before us that respondent’s departure from the building was within the timeframe predicted by the caller. As for the caller’s prediction of respondent’s destination, it is true that the officers stopped her just short of Dobey’s Motel and did not know whether she would have pulled in or continued past it. But given that the 4-mile route driven by respondent was the most direct route possible to Dobey’s Motel, 550 So. 2d, at 1075, Tr. of Oral Arg. 24, but nevertheless involved several turns, App. 7, Tr. of Oral Arg. 24, we think respondent’s destination was significantly corroborated.</p>
<p id="b373-6">The Court’s opinion in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span> </em>gave credit to the proposition that because an informant is shown to be right about some things, he is probably right about other facts that he has alleged, including the claim that the object of the tip is engaged in criminal activity. <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#244" aria-description="Citation for case: Illinois v. Gates">462 U. S., at 244</a></span>. Thus, it is not <page-number citation-index="1" label="332">*332</page-number>unreasonable to conclude in this case that the independent corroboration by the police of significant aspects of the informer's predictions imparted some degree of reliability to the other allegations made by the caller.</p>
<p id="b374-5">We think it also important that, as in <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">Gates</a></span>, </em>“the anonymous [tip] contained a range of details relating not just to easily obtained facts and conditions existing at the time of the tip, but to future actions of third parties ordinarily not easily predicted.” <span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/#245" aria-description="Citation for case: Illinois v. Gates"><em>Id., </em>at 245</a></span>. The fact that the officers found a car precisely matching the caller’s description in front of the 235 building is an example of the former. Anyone could have “predicted” that fact because it was a condition presumably existing at the time of the call. What was important was the caller’s ability to predict respondent’s <em>future behavior, </em>because it demonstrated inside information—a special familiarity with respondent’s affairs. The general public would have had no way of knowing that respondent would shortly leave the building, get in the described car, and drive the most direct route to Dobey’s Motel. Because only a small number of people are generally privy to an individual’s itinerary, it is reasonable for police to believe that a person with access to such information is likely to also have access to reliable information about that individual’s illegal activities. See <em><span class="citation" data-id="9429232"><a href="/opinion/110959/illinois-v-gates/" aria-description="Citation for case: Illinois v. Gates">ibid.</a></span> </em>When significant aspects of the caller’s predictions were verified, there was reason to believe not only that the caller was honest but also that he was well informed, at least well enough to justify the stop.</p>
<p id="b374-6">Although it is a close case, we conclude that under the totality of the circumstances the anonymous tip, as corroborated, exhibited sufficient indicia of reliability to justify the investigatory stop of respondent’s car. We therefore reverse the judgment of the Court of Criminal Appeals of Alabama and remand the case for further proceedings not inconsistent with this opinion.</p>
<p id="b374-7">
<em>So ordered.</em>
</p>
</opinion>
```

---

## GROUP: content/cases/Alderman v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Alderman v. United States"
type: case
citation: "394 U.S. 165 (1969)"
parallel_cite: "89 S. Ct. 961; 22 L. Ed. 2d 176"
neutral_cite: 1969 U.S. LEXIS 3287
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-03-24
docket: 133
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-03-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Alderman v. United States
  varies_by_point: false
  scope_note: "The personal-rights standing rule remains good law; Rakas v. Illinois (1978) recast the inquiry as a substantive Fourth Amendment merits question but reaffirmed Alderman's core principle."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107872/alderman-v-united-states/"
  cluster_id: 107872
  opinion_id: 9423945
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Anchor"
related: ["[[Rakas v. Illinois]]", "[[Jones v. United States]]", "[[Mancusi v. DeForte]]", "[[Simmons v. United States]]", "[[United States v. Payner]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "exclusionary-rule", "electronic-surveillance", "personal-rights"]
holding: "Fourth Amendment rights are personal and may not be vicariously asserted; only a defendant whose own rights were violated by the search or surveillance — not a co-defendant or co-conspirator aggrieved solely by the evidence — may move to suppress."
lake:
  record_id: Alderman v. United States
  status: verified
  projected_at: 2026-07-09
---

# Alderman v. United States

*394 U.S. 165 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After the petitioners' convictions, it was revealed that the Government had conducted electronic surveillance that might have violated Fourth Amendment rights. The petitioners argued that any evidence traceable to the unlawful surveillance required retrial — even surveillance that invaded only a co-defendant's or co-conspirator's rights — and that the Government had to disclose the surveillance records. The Court addressed both who may suppress the fruits of illegal surveillance and the disclosure procedure.

## Issue
Whether a defendant may suppress evidence obtained by electronic surveillance (or any search) that violated only a third party's Fourth Amendment rights — that is, whether co-defendants and co-conspirators have standing to assert another's Fourth Amendment rights.

## Rule
No; standing to suppress is personal. "The established principle is that suppression of the product of a Fourth Amendment violation can be successfully urged only by those whose rights were violated by the search itself, not by those who are aggrieved solely by the introduction of damaging evidence. Coconspirators and codefendants have been accorded no special standing." — 394 U.S. at 171–172. ^pin-171

"We adhere to these cases and to the general rule that Fourth Amendment rights are personal rights which, like some other constitutional rights, may not be vicariously asserted." — [*Id.* at 174](https://www.courtlistener.com/opinion/107872/alderman-v-united-states/#:~:text=We%20adhere%20to%20these%20cases). ^pin-174

Deterrence does not eliminate that predicate: "There is no necessity to exclude evidence against one defendant in order to protect the rights of another. No rights of the victim of an illegal search are at stake when the evidence is offered against some other party." — [*Id.* at 174](https://www.courtlistener.com/opinion/107872/alderman-v-united-states/#:~:text=There%20is%20no%20necessity%20to). ^pin-174b

## Application
Each petitioner could move to suppress only the fruits of surveillance that invaded his own Fourth Amendment interests — conversations to which he was a party or surveillance of premises he owned — not surveillance aimed at someone else. The Court rejected the petitioners' claim of an "independent constitutional right of their own to exclude relevant and probative evidence because it was seized from another." On the disclosure question, it ordered the Government to turn over to a defendant the surveillance records of his own conversations or those overheard on his premises, for an adversary [[Common Legal Terms#suppression-hearing|suppression hearing]].

## Conclusion
Standing to suppress is personal and may not be vicariously asserted; the cases were [[Reading and Citing Cases#on-remand|remanded]] for suppression hearings limited to each petitioner's own conversations and premises, with disclosure of the pertinent surveillance records.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of the holding. [[Rakas v. Illinois]] (1978) recast "standing" as a substantive Fourth Amendment merits inquiry (a personal, legitimate expectation of privacy) but **reaffirmed** *Alderman*'s personal-rights principle; [[United States v. Payner]] and [[United States v. Padilla]] enforce it against, respectively, the supervisory power and a coconspirator exception. The standing definition traces to [[Jones v. United States]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Anchor*

## Sources
- *Alderman v. United States*, 394 U.S. 165 (1969) — https://www.courtlistener.com/opinion/107872/alderman-v-united-states/ — pinpoints: 171–172, 174.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6eea9633da68ee51", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "394 U.S. 165 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 3287", "official_citation_present": true, "parallel_cite": "89 S. Ct. 961; 22 L. Ed. 2d 176", "title": "Alderman v. United States", "year": "1969"}}
{"assertion_id": "0c4d379fe19ea142", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Fourth Amendment rights are personal and may not be vicariously asserted; only a defendant whose own rights were violated by the search or surveillance — not a co-defendant or co-conspirator aggrieved solely by the evidence — may move to suppress.", "title": "Alderman v. United States"}}
{"assertion_id": "120cb434aa35bec8", "dimension": "support", "kind": "home_role", "locator": {"home": "Standing to Challenge a Search"}, "payload": {"home": "Standing to Challenge a Search", "role": "Key — Anchor", "title": "Alderman v. United States"}}
{"assertion_id": "2c0866a206a479d5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Alderman v. United States"}}
{"assertion_id": "ff5b64bcee2b7da8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-03-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Alderman v. United States", "field_i_validity": "good_law", "scope_note": "The personal-rights standing rule remains good law; Rakas v. Illinois (1978) recast the inquiry as a substantive Fourth Amendment merits question but reaffirmed Alderman's core principle.", "title": "Alderman v. United States", "varies_by_point": "false"}}
```

### lake record — Alderman v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Alderman v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Alderman v. United States",
    "case_name_short": "Alderman",
    "case_name_full": "ALDERMAN Et Al. v. UNITED STATES",
    "input_case_name": "Alderman v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-03-24",
    "year": 1969,
    "docket": "133",
    "cluster_id": 107872,
    "lead_opinion_id": 9423945,
    "sibling_ids": [
      107872,
      9423945,
      9423946,
      9423947
    ],
    "absolute_url": "/opinion/107872/alderman-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 165",
      "volume": "394",
      "reporter": "U.S.",
      "page": "165",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 961",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "961",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 176",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "176",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 3287",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "3287",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 165",
        "volume": "394",
        "reporter": "U.S.",
        "page": "165",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 961",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "961",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 176",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "176",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 3287",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "3287",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 165",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 165",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-171",
      "page": null,
      "quote": "--- # Alderman v. United States *394 U.S. 165 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After the petitioners' convictions, it was revealed that the Government had conducted electronic surveillance that might have violated Fourth Amendment rights. The petitioners argued that any evidence traceable to the unlawful surveillance required retrial \u2014 even surveillance that invaded only a co-defendant's or co-conspirator's rights \u2014 and that the Government had to disclose the surveillance records. The Court addressed both who may suppress the fruits of illegal surveillance and the disclosure procedure. ## Issue Whether a defendant may suppress evidence obtained by electronic surveillance (or any search) that violated only a third party's Fourth Amendment rights \u2014 that is, whether co-defendants and co-conspirators have standing to assert another's Fourth Amendment rights. ## Rule No; standing to suppress is personal.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-174",
      "page": null,
      "quote": "We adhere to these cases and to the general rule that Fourth Amendment rights are personal rights which, like some other constitutional rights, may not be vicariously asserted.",
      "star_marker": "174",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11788,
      "fragment": "#:~:text=We%20adhere%20to%20these%20cases",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-174b",
      "page": null,
      "quote": "There is no necessity to exclude evidence against one defendant in order to protect the rights of another. No rights of the victim of an illegal search are at stake when the evidence is offered against some other party.",
      "star_marker": "174",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13237,
      "fragment": "#:~:text=There%20is%20no%20necessity%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-03-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Alderman v. United States",
    "varies_by_point": false,
    "scope_note": "The personal-rights standing rule remains good law; Rakas v. Illinois (1978) recast the inquiry as a substantive Fourth Amendment merits question but reaffirmed Alderman's core principle.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Olive",
          "cluster_id": 10872112,
          "cite": [
            "2026 Ohio 2150"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Clifton Mosley",
          "cluster_id": 10799851,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leron Liggins",
          "cluster_id": 10795801,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rykena",
          "cluster_id": 10735854,
          "cite": [
            "2025 Ohio 5136"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Aguilar, S.",
          "cluster_id": 10601729,
          "cite": [
            "2025 Pa. Super. 118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "PETTIT, JUSTIN v. the State of Texas",
          "cluster_id": 10596365,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bourrage",
          "cluster_id": 10588786,
          "cite": [
            "138 F.4th 327"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Seth Albert Lookhart v. State of Alaska",
          "cluster_id": 10581677,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Hagestedt",
          "cluster_id": 10328364,
          "cite": [
            "2025 IL 130286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Richard W. Kelley",
          "cluster_id": 10340246,
          "cite": [
            "2025 ME 1"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bonner",
          "cluster_id": 10276379,
          "cite": [
            "2024 Ohio 4717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnnie Davis",
          "cluster_id": 10020876,
          "cite": [
            "109 F.4th 1320"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fortenberry",
          "cluster_id": 9972095,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Rogers",
          "cluster_id": 9492473,
          "cite": [
            "97 F.4th 1038"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Camper",
          "cluster_id": 9454678,
          "cite": [
            "232 N.E.3d 419",
            "2023 Ohio 4673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McFadden",
          "cluster_id": 9399122,
          "cite": [
            "2023 Ohio 1630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 9397460,
          "cite": [
            "2023 Ohio 1544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "David Milton Sills a/k/a David Sills v. State of Mississippi",
          "cluster_id": 10628039,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mexican Gulf v. U.S. Dept. of Comm",
          "cluster_id": 9379875,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terrance Baker",
          "cluster_id": 9371555,
          "cite": [
            "58 F.4th 1109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pilon",
          "cluster_id": 10135363,
          "cite": [
            "321 Or. App. 460",
            "516 P.3d 1181"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kory L. George",
          "cluster_id": 6466270,
          "cite": [
            "2022 VT 21"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McClendon",
          "cluster_id": 6464833,
          "cite": [
            "2022 Ohio 1441"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jordan",
          "cluster_id": 9353271,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leonorilda Ochoa v. City of Mesa",
          "cluster_id": 6445947,
          "cite": [
            "26 F.4th 1050"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Whitehead",
          "cluster_id": 6444757,
          "cite": [
            "2022 Ohio 479"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 6352763,
          "cite": [
            "2022 Ohio 371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Beltran-Leyva (Guzman Loera)",
          "cluster_id": 6245919,
          "cite": [
            "24 F.4th 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jabrell Smith",
          "cluster_id": 5307503,
          "cite": [
            "21 F.4th 122"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Muhtorov",
          "cluster_id": 5304320,
          "cite": [
            "20 F.4th 558"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Bruce Akers",
          "cluster_id": 5093384,
          "cite": [
            "259 A.3d 127",
            "2021 ME 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stevens",
          "cluster_id": 4875709,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Billy Ray Foster, Jr. v. State",
          "cluster_id": 4853501,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Basaaly Moalin",
          "cluster_id": 4781995,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nikolas S. Shannon v. State of Indiana (mem. dec.)",
          "cluster_id": 4769800,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cunningham v. Baltimore Cnty.",
          "cluster_id": 10021171,
          "cite": [
            "232 A.3d 278",
            "246 Md. App. 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "STATE OF NEW JERSEY VS. MARQUIS ARMSTRONG (15-05-0932, ESSEX COUNTY AND STATEWIDE)",
          "cluster_id": 4757867,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pedraza",
          "cluster_id": 4748683,
          "cite": [
            "2020 Ohio 2661"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesus Francisco Campos Junior v. State",
          "cluster_id": 4740881,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Ramon D. Boyd",
          "cluster_id": 4685447,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barnhart",
          "cluster_id": 4684979,
          "cite": [
            "2019 Ohio 5002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Guzman",
          "cluster_id": 4684385,
          "cite": [
            "8 Cal. 5th 673",
            "256 Cal. Rptr. 3d 112",
            "453 P.3d 1130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dylan Davis",
          "cluster_id": 4682510,
          "cite": [
            "943 F.3d 1129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Eric Beverly",
          "cluster_id": 4678644,
          "cite": [
            "943 F.3d 225"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mobley v. State",
          "cluster_id": 10366993,
          "cite": [
            "307 Ga. 59"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Geraldine Nicholson v. Miguel Gutierrez",
          "cluster_id": 4654479,
          "cite": [
            "935 F.3d 685"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Concord Management and Consulting LLC",
          "cluster_id": 4647426,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Santiago, A., Aplt.",
          "cluster_id": 4630389,
          "cite": [
            "209 A.3d 912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ian Christian Carlson v. Commonwealth of Virginia",
          "cluster_id": 4589695,
          "cite": [
            "823 S.E.2d 28",
            "69 Va. App. 749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lopez",
          "cluster_id": 4575196,
          "cite": [
            "2018 IL App (1st) 153331"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Edwin S. Short v. State of Indiana (mem. dec.)",
          "cluster_id": 4573937,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Every, Plaintiff v. Town of Littleton, New Hampshire; Andrew Dorsett, Town Manager; Milton Bratz, Selectman; Schuyler Sweet, Selectman; Edward Hennessey, Former Selectman; Paul Smith, Chief of Police; Stephen Cox, Detective Sergeant; and George McNamara, Public Works Director, Defendants",
          "cluster_id": 10693911,
          "cite": [
            "2018 DNH 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Olsen v. Hamilton",
          "cluster_id": 7331892,
          "cite": [
            "330 F. Supp. 3d 545"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dannebohm",
          "cluster_id": 4515027,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dannebohm",
          "cluster_id": 4514861,
          "cite": [
            "421 P.3d 751"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Herd v. Cnty. of San Bernardino",
          "cluster_id": 7330286,
          "cite": [
            "311 F. Supp. 3d 1157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wilson",
          "cluster_id": 4464219,
          "cite": [
            "2018 Ohio 396",
            "106 N.E.3d 806"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
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
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mock",
          "cluster_id": 4462084,
          "cite": [
            "2018 Ohio 268",
            "106 N.E.3d 154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Shakir v. Derby Police Dep't",
          "cluster_id": 7327899,
          "cite": [
            "284 F. Supp. 3d 165"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Emilio Jean",
          "cluster_id": 4456788,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard Oliver",
          "cluster_id": 4453391,
          "cite": [
            "878 F.3d 120"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hamilton",
          "cluster_id": 4433424,
          "cite": [
            "2017 Ohio 8140"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christian Longoria v. Pinal County",
          "cluster_id": 4433102,
          "cite": [
            "873 F.3d 699",
            "2017 WL 4509042",
            "2017 U.S. App. LEXIS 19794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ernest Glover",
          "cluster_id": 4433034,
          "cite": [
            "872 F.3d 625",
            "2017 WL 4507530",
            "2017 U.S. App. LEXIS 19741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of El Cenizo v. Texas",
          "cluster_id": 7326561,
          "cite": [
            "264 F. Supp. 3d 744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 4414534,
          "cite": [
            "2017 Ohio 7048"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rose Mary Knick v. Township of Scott",
          "cluster_id": 4406717,
          "cite": [
            "862 F.3d 310",
            "2017 WL 2872871",
            "2017 U.S. App. LEXIS 12052"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "IAR Systems v. Super. Ct.",
          "cluster_id": 4405640,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cardman",
          "cluster_id": 4407744,
          "cite": [
            "2017 COA 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "IAR Sys. Software, Inc. v. Superior Court of San Mateo Cnty.",
          "cluster_id": 6238831,
          "cite": [
            "218 Cal. Rptr. 3d 852",
            "12 Cal. App. 5th 503",
            "2017 WL 2417905",
            "2017 Cal. App. LEXIS 512"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "IAR Systems v. Super. Ct.",
          "cluster_id": 4397252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Michael Christopher Frederick",
          "cluster_id": 4396951,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People of Michigan v. Todd Randolph Van Doorne",
          "cluster_id": 4396950,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Bruce Wayne Sutton",
          "cluster_id": 4393282,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The Matter of 381 Search Warrants Directed to Facebook Inc. v. New York County District Attorney's Office",
          "cluster_id": 4380365,
          "cite": [
            "29 N.Y.3d 231",
            "78 N.E.3d 141"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Escamilla, Jr.",
          "cluster_id": 4379363,
          "cite": [
            "852 F.3d 474",
            "2017 WL 1191628",
            "2017 U.S. App. LEXIS 5485"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dominique Jackson",
          "cluster_id": 4370994,
          "cite": [
            "849 F.3d 540",
            "102 Fed. R. Serv. 961",
            "2017 WL 727144",
            "2017 U.S. App. LEXIS 3367"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Leona Rose deLottinville",
          "cluster_id": 4350046,
          "cite": [
            "890 N.W.2d 116",
            "2017 WL 603602",
            "2017 Minn. LEXIS 55"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Aiken",
          "cluster_id": 7323334,
          "cite": [
            "225 F. Supp. 3d 85",
            "2016 U.S. Dist. LEXIS 167204",
            "2016 WL 7048695"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Rebekah Thonginh Ross v. State",
          "cluster_id": 4327137,
          "cite": [
            "507 S.W.3d 881",
            "2016 Tex. App. LEXIS 12673",
            "2016 WL 6995031"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hayward",
          "cluster_id": 4319281,
          "cite": [
            "2016 Ohio 7671"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of West Virginia v. Ennis C. Payne II",
          "cluster_id": 4313845,
          "cite": [
            "239 W. Va. 247",
            "800 S.E.2d 833",
            "2016 W. Va. LEXIS 760"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schuchardt v. President of the United States",
          "cluster_id": 4302531,
          "cite": [
            "839 F.3d 336",
            "2016 U.S. App. LEXIS 18025",
            "2016 WL 5799656"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cardman",
          "cluster_id": 4308869,
          "cite": [
            "2016 COA 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
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
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whole Woman's Health v. Hellerstedt",
          "cluster_id": 3217529,
          "cite": [
            "579 U.S. 582",
            "2016 U.S. LEXIS 4063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whole Woman's Health v. Hellerstedt",
          "cluster_id": 3217528,
          "cite": [
            "579 U.S. 582"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Whole Woman's Health v. Hellerstedt",
          "cluster_id": 3217332,
          "cite": [
            "579 U.S. 582",
            "136 S. Ct. 2292",
            "195 L. Ed. 2d 665"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bethea",
          "cluster_id": 7320691,
          "cite": [
            "191 F. Supp. 3d 249",
            "2016 WL 3248305"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sodomsky",
          "cluster_id": 3193577,
          "cite": [
            "137 A.3d 620",
            "2016 Pa. Super. 84",
            "2016 WL 1436501",
            "2016 Pa. Super. LEXIS 223"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Glover",
          "cluster_id": 3190718,
          "cite": [
            "174 F. Supp. 3d 431",
            "2016 U.S. Dist. LEXIS 43260",
            "2016 WL 1273171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rickey Beene",
          "cluster_id": 3183556,
          "cite": [
            "818 F.3d 157",
            "2016 U.S. App. LEXIS 4331",
            "2016 WL 890127"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lowery",
          "cluster_id": 3192409,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Lowery",
          "cluster_id": 3179486,
          "cite": [
            "23 Neb. Ct. App. 621",
            "875 N.W.2d 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Alderman",
          "cluster_id": 3169883,
          "cite": [
            "2016 Ohio 130"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Elmore",
          "cluster_id": 3169882,
          "cite": [
            "2016 Ohio 129"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Lyall v. City of Los Angeles",
          "cluster_id": 3160114,
          "cite": [
            "807 F.3d 1178",
            "2015 U.S. App. LEXIS 21055",
            "2015 WL 7873413"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. William Cordova",
          "cluster_id": 3157457,
          "cite": [
            "420 U.S. App. D.C. 138",
            "806 F.3d 1085",
            "2015 U.S. App. LEXIS 20386",
            "2015 WL 7597528"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Padilla",
          "cluster_id": 3009303,
          "cite": [
            "2015 Ohio 4220"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in Re: Thomas Lytle and Ellen Lytle",
          "cluster_id": 4283462,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Azano Matsura",
          "cluster_id": 7315592,
          "cite": [
            "129 F. Supp. 3d 975",
            "2015 U.S. Dist. LEXIS 126144",
            "2015 WL 5449912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gomez, Gilberto",
          "cluster_id": 4273686,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "A-111-13 State v. Thomas Shannon(074315)",
          "cluster_id": 2828532,
          "cite": [
            "222 N.J. 576",
            "120 A.3d 924",
            "2015 N.J. LEXIS 875"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Robert McDonnell",
          "cluster_id": 2816274,
          "cite": [
            "792 F.3d 478",
            "97 Fed. R. Serv. 1438",
            "2015 U.S. App. LEXIS 11889",
            "2015 WL 4153640"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Com. v. Sodomsky, K.",
          "cluster_id": 2806011,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bradley Leroy Thompson v. State",
          "cluster_id": 4271240,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "American Civil Liberties Union v. Clapper",
          "cluster_id": 8442192,
          "cite": [
            "785 F.3d 787",
            "43 Media L. Rep. (BNA) 1649",
            "62 Communications Reg. (P&F) 945",
            "2015 U.S. App. LEXIS 7531",
            "2015 WL 2097814"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "ACLU v. Clapper",
          "cluster_id": 2799236,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Uwadiegwu v. Department of Social Services",
          "cluster_id": 7312374,
          "cite": [
            "91 F. Supp. 3d 391",
            "2015 U.S. Dist. LEXIS 31182",
            "2015 WL 1206118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Steven Maxwell",
          "cluster_id": 2780753,
          "cite": [
            "778 F.3d 719"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Perel",
          "cluster_id": 2764157,
          "cite": [
            "107 A.3d 185",
            "2014 Pa. Super. 283",
            "2014 Pa. Super. LEXIS 4572",
            "2014 WL 7331025"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Anderson",
          "cluster_id": 8442041,
          "cite": [
            "772 F.3d 969",
            "2014 U.S. App. LEXIS 22229",
            "2014 WL 6610019"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Valentino Anderson",
          "cluster_id": 2754479,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 2750422,
          "cite": [
            "410 S.C. 519",
            "765 S.E.2d 564",
            "2014 S.C. LEXIS 492"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eddie McCoy, Jr. v. State of Mississippi",
          "cluster_id": 2744237,
          "cite": [
            "160 So. 3d 705",
            "2014 Miss. App. LEXIS 594",
            "2014 WL 5333838"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Simmons",
          "cluster_id": 2736438,
          "cite": [
            "2014 Ohio 4191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Courtney Noble",
          "cluster_id": 2716405,
          "cite": [
            "762 F.3d 509",
            "2014 WL 3882493",
            "2014 U.S. App. LEXIS 15279"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 2686476,
          "cite": [
            "218 Md. App. 1",
            "96 A.3d 765",
            "2014 WL 3736532",
            "2014 Md. App. LEXIS 72"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. George Alan Kapelle",
          "cluster_id": 3149293,
          "cite": [
            "158 Idaho 121",
            "344 P.3d 901",
            "2014 WL 3632654",
            "2014 Ida. App. LEXIS 72"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of New Jersey v. Calvin Presley",
          "cluster_id": 2684193,
          "cite": [
            "436 N.J. Super. 440",
            "94 A.3d 921"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Yassine",
          "cluster_id": 8692022,
          "cite": [
            "574 F. App'x 455"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of West Virginia v. Lamar Dorsey",
          "cluster_id": 2677126,
          "cite": [
            "234 W. Va. 15",
            "762 S.E.2d 584",
            "2014 WL 2566058",
            "2014 W. Va. LEXIS 631"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. George Kapelle",
          "cluster_id": 2672873,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Granados",
          "cluster_id": 2698211,
          "cite": [
            "2014 Ohio 1758"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950016,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
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
        "journal_ref": "Alderman v. United States:lane1_negative"
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
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rodriguez-Rodriguez",
          "cluster_id": 2646574,
          "cite": [
            "741 F.3d 179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Heney",
          "cluster_id": 2713947,
          "cite": [
            "2013 SD 77",
            "839 N.W.2d 558",
            "2013 S.D. LEXIS 137",
            "2013 WL 5861271"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Booker Powell",
          "cluster_id": 1043365,
          "cite": [
            "732 F.3d 361",
            "2013 WL 5493969"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Lambert Grandberry",
          "cluster_id": 1040986,
          "cite": [
            "730 F.3d 968",
            "2013 WL 5184439",
            "2013 U.S. App. LEXIS 19180"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pinon, Araceli Sanchez",
          "cluster_id": 3099362,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnson v. Bay Area Rapid Transit District",
          "cluster_id": 1035754,
          "cite": [
            "724 F.3d 1159"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Silvas",
          "cluster_id": 2642656,
          "cite": [
            "2013 NMCA 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Silvas",
          "cluster_id": 1034403,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Arturo Castellanos",
          "cluster_id": 873156,
          "cite": [
            "716 F.3d 828",
            "2013 WL 2321976",
            "2013 U.S. App. LEXIS 10797"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Zemlyansky",
          "cluster_id": 8725326,
          "cite": [
            "945 F. Supp. 2d 438",
            "2013 WL 2151228",
            "2013 U.S. Dist. LEXIS 71818"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Crawford",
          "cluster_id": 2702660,
          "cite": [
            "2013 Ohio 1659"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Horsley",
          "cluster_id": 2697478,
          "cite": [
            "2013 Ohio 901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Schmitz",
          "cluster_id": 821521,
          "cite": [
            "55 Cal. 4th 909",
            "288 P.3d 1259",
            "149 Cal. Rptr. 3d 640",
            "2012 WL 5990981",
            "2012 Cal. LEXIS 11006"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Madrid",
          "cluster_id": 8721843,
          "cite": [
            "916 F. Supp. 2d 730",
            "2012 WL 6771011",
            "2012 U.S. Dist. LEXIS 183606"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Bohman",
          "cluster_id": 803265,
          "cite": [
            "683 F.3d 861",
            "2012 WL 2432595",
            "2012 U.S. App. LEXIS 13195"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. City of New York",
          "cluster_id": 8716313,
          "cite": [
            "869 F. Supp. 2d 337",
            "2012 U.S. Dist. LEXIS 82673",
            "2012 WL 2154257"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stepp",
          "cluster_id": 800000,
          "cite": [
            "680 F.3d 651",
            "2012 U.S. App. LEXIS 9883",
            "2012 WL 1728826"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Maldonado v. Superior Court",
          "cluster_id": 844207,
          "cite": [
            "274 P.3d 1110",
            "53 Cal. 4th 1112",
            "140 Cal. Rptr. 3d 113",
            "2012 WL 1382220",
            "2012 Cal. LEXIS 3612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Vu",
          "cluster_id": 2706155,
          "cite": [
            "2012 Ohio 746"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
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
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. White",
          "cluster_id": 2706226,
          "cite": [
            "2011 Ohio 6748"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Raul Coronado Jr. v. State",
          "cluster_id": 3099211,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Salyer",
          "cluster_id": 2175080,
          "cite": [
            "814 F. Supp. 2d 984",
            "2011 U.S. Dist. LEXIS 98420",
            "2011 WL 3875701"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gilbert",
          "cluster_id": 2463474,
          "cite": [
            "254 P.3d 1271",
            "292 Kan. 428",
            "2011 Kan. LEXIS 242"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Klein",
          "cluster_id": 2460481,
          "cite": [
            "258 P.3d 528",
            "243 Or. App. 1",
            "2011 Ore. App. LEXIS 687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Miller",
          "cluster_id": 2704671,
          "cite": [
            "2011 Ohio 2388"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Magee",
          "cluster_id": 5810161,
          "cite": [
            "194 Cal. App. 4th 178",
            "123 Cal. Rptr. 3d 689",
            "2011 Cal. App. LEXIS 425"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Allen & Coen",
          "cluster_id": 1084281,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Epps v. State",
          "cluster_id": 2444139,
          "cite": [
            "1 A.3d 488",
            "193 Md. App. 687",
            "2010 Md. App. LEXIS 90"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Struckman",
          "cluster_id": 145496,
          "cite": [
            "603 F.3d 731",
            "2010 U.S. App. LEXIS 9140",
            "2010 WL 1757874"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Riesselman",
          "cluster_id": 2540999,
          "cite": [
            "708 F. Supp. 2d 797",
            "2010 U.S. Dist. LEXIS 41480",
            "2010 WL 1718100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Clarence Graham v. State",
          "cluster_id": 2993189,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gary Webster v. State",
          "cluster_id": 3130306,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gary Webster v. State",
          "cluster_id": 3130305,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gary Webster v. State",
          "cluster_id": 3130304,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Wallen",
          "cluster_id": 2697002,
          "cite": [
            "2010 Ohio 480"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Carriles",
          "cluster_id": 2517722,
          "cite": [
            "654 F. Supp. 2d 557",
            "2009 U.S. Dist. LEXIS 75243",
            "2009 WL 2618584"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Moldowan v. City of Warren",
          "cluster_id": 1447482,
          "cite": [
            "573 F.3d 309",
            "2009 U.S. App. LEXIS 17988",
            "2009 WL 2176640"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jeffrey Moldowan v. Maureen Fournier",
          "cluster_id": 2978087,
          "cite": [
            "570 F.3d 698",
            "2009 U.S. App. LEXIS 14238",
            "2009 WL 1872284"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. SHUFFELEN",
          "cluster_id": 2536490,
          "cite": [
            "208 P.3d 1167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MACEACHERN v. City of Manhattan Beach",
          "cluster_id": 2482170,
          "cite": [
            "623 F. Supp. 2d 1092",
            "2009 U.S. Dist. LEXIS 73835",
            "2009 WL 1591586"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Club Retro LLC v. Hilton",
          "cluster_id": 66452,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Club Retro, L.L.C. v. Hilton",
          "cluster_id": 1459439,
          "cite": [
            "568 F.3d 181",
            "2009 U.S. App. LEXIS 9864",
            "2006 WL 6245546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. El Farra",
          "cluster_id": 3054405,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. $40,955.00 in United States Currency",
          "cluster_id": 1279017,
          "cite": [
            "554 F.3d 752",
            "2009 U.S. App. LEXIS 1325",
            "2009 WL 174911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re National Security Agency Telecommunications Records Litigation",
          "cluster_id": 1683389,
          "cite": [
            "595 F. Supp. 2d 1077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Western Union Financial Services, Inc.",
          "cluster_id": 2602030,
          "cite": [
            "199 P.3d 592",
            "219 Ariz. 337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Odeh",
          "cluster_id": 8440375,
          "cite": [
            "552 F.3d 157",
            "2008 U.S. App. LEXIS 24054"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re Terrorist Bombings of U.S. Embassies (Fourth Amendment Challenges)",
          "cluster_id": 2550,
          "cite": null,
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City of Marion v. Brewer, 9-08-12 (10-20-2008)",
          "cluster_id": 4012288,
          "cite": [
            "2008 Ohio 5401"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "V.S. ex rel. T.S. v. Muhammad",
          "cluster_id": 8709367,
          "cite": [
            "581 F. Supp. 2d 365",
            "2008 U.S. Dist. LEXIS 77540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vs Ex Rel. TS v. Muhammad",
          "cluster_id": 1596595,
          "cite": [
            "581 F. Supp. 2d 365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Baptiste v. State",
          "cluster_id": 1697730,
          "cite": [
            "995 So. 2d 285",
            "2008 WL 4240489"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Galan",
          "cluster_id": 3135479,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Galan",
          "cluster_id": 2231488,
          "cite": [
            "893 N.E.2d 597",
            "229 Ill. 2d 484",
            "323 Ill. Dec. 325",
            "2008 Ill. LEXIS 639"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Davis",
          "cluster_id": 2461450,
          "cite": [
            "565 F. Supp. 2d 841",
            "2008 U.S. Dist. LEXIS 47344",
            "2008 WL 2497475"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fancher",
          "cluster_id": 890649,
          "cite": [
            "186 P.3d 688",
            "145 Idaho 832",
            "2008 Ida. App. LEXIS 58"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jackson",
          "cluster_id": 2976408,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gray",
          "cluster_id": 1302101,
          "cite": [
            "521 F.3d 514",
            "2008 WL 897513"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Crisp",
          "cluster_id": 2284418,
          "cite": [
            "542 F. Supp. 2d 1267",
            "2008 U.S. Dist. LEXIS 12867",
            "2008 WL 506214"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Wallace",
          "cluster_id": 800415,
          "cite": [
            "66 M.J. 5",
            "2008 CAAF LEXIS 226",
            "2008 WL 420013"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Vilar",
          "cluster_id": 1370326,
          "cite": [
            "530 F. Supp. 2d 616",
            "2008 WL 140958"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Jordan Heath Dentler",
          "cluster_id": 4472853,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dentler",
          "cluster_id": 1992992,
          "cite": [
            "742 N.W.2d 84",
            "2007 Iowa Sup. LEXIS 141",
            "2007 WL 4276551"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Jordan",
          "cluster_id": 1995384,
          "cite": [
            "742 N.W.2d 149",
            "2007 Minn. LEXIS 752",
            "2007 WL 4259511"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane1_negative"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyles v. Whitley",
          "cluster_id": 117923,
          "cite": [
            "131 L. Ed. 2d 490",
            "115 S. Ct. 1555",
            "514 U.S. 419",
            "1995 U.S. LEXIS 2845"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doyle v. Ohio",
          "cluster_id": 109491,
          "cite": [
            "49 L. Ed. 2d 91",
            "96 S. Ct. 2240",
            "426 U.S. 610",
            "1976 U.S. LEXIS 66"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Broadrick v. Oklahoma",
          "cluster_id": 108858,
          "cite": [
            "37 L. Ed. 2d 830",
            "93 S. Ct. 2908",
            "413 U.S. 601",
            "1973 U.S. LEXIS 34"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Calandra",
          "cluster_id": 108898,
          "cite": [
            "38 L. Ed. 2d 561",
            "94 S. Ct. 613",
            "414 U.S. 338",
            "1974 U.S. LEXIS 145",
            "66 Ohio Op. 2d 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brewer v. Williams",
          "cluster_id": 109624,
          "cite": [
            "51 L. Ed. 2d 424",
            "97 S. Ct. 1232",
            "430 U.S. 387",
            "1977 U.S. LEXIS 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Ferber",
          "cluster_id": 110794,
          "cite": [
            "73 L. Ed. 2d 1113",
            "102 S. Ct. 3348",
            "458 U.S. 747",
            "1982 U.S. LEXIS 12",
            "8 Media L. Rep. (BNA) 1809",
            "50 U.S.L.W. 5077"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cady v. Dombrowski",
          "cluster_id": 108850,
          "cite": [
            "37 L. Ed. 2d 706",
            "93 S. Ct. 2523",
            "413 U.S. 433",
            "1973 U.S. LEXIS 48"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salvucci",
          "cluster_id": 110325,
          "cite": [
            "65 L. Ed. 2d 619",
            "100 S. Ct. 2547",
            "448 U.S. 83",
            "1980 U.S. LEXIS 141"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wayte v. United States",
          "cluster_id": 111375,
          "cite": [
            "84 L. Ed. 2d 547",
            "105 S. Ct. 1524",
            "470 U.S. 598",
            "1985 U.S. LEXIS 71",
            "53 U.S.L.W. 4319"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. United States District Court for the Eastern District of Michigan",
          "cluster_id": 108581,
          "cite": [
            "32 L. Ed. 2d 752",
            "92 S. Ct. 2125",
            "407 U.S. 297",
            "1972 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. United States",
          "cluster_id": 109860,
          "cite": [
            "56 L. Ed. 2d 168",
            "98 S. Ct. 1717",
            "436 U.S. 128",
            "1978 U.S. LEXIS 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Janis",
          "cluster_id": 109539,
          "cite": [
            "49 L. Ed. 2d 1046",
            "96 S. Ct. 3021",
            "428 U.S. 433",
            "1976 U.S. LEXIS 162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. United States",
          "cluster_id": 108760,
          "cite": [
            "36 L. Ed. 2d 208",
            "93 S. Ct. 1565",
            "411 U.S. 223",
            "1973 U.S. LEXIS 82"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Metromedia, Inc. v. City of San Diego",
          "cluster_id": 110561,
          "cite": [
            "69 L. Ed. 2d 800",
            "101 S. Ct. 2882",
            "453 U.S. 490",
            "1981 U.S. LEXIS 50",
            "11 Envtl. L. Rep. (Envtl. Law Inst.) 20600",
            "49 U.S.L.W. 4925",
            "16 ERC (BNA) 1057"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Miller",
          "cluster_id": 109433,
          "cite": [
            "48 L. Ed. 2d 71",
            "96 S. Ct. 1619",
            "425 U.S. 435",
            "1976 U.S. LEXIS 148",
            "37 A.F.T.R.2d (RIA) 1261"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Alderman v. United States:lane2_top_cited"
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
        "journal_ref": "Alderman v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107872 OR 9423945 OR 9423946 OR 9423947) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTk2ODk5MjAwMDAwJnM9MTk5NTM4NCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107872+OR+9423945+OR+9423946+OR+9423947%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 194
      },
      "lane2_top_cited": {
        "query": "cites:(107872 OR 9423945 OR 9423946 OR 9423947)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MDUmcz0yNDYxMjAyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107872+OR+9423945+OR+9423946+OR+9423947%29&type=o",
        "audit_needed": true,
        "audit_marker": "R15 treatment audit required",
        "proposed_negative_events": 25
      },
      "lane3_recency": {
        "query": "cites:(107872 OR 9423945 OR 9423946 OR 9423947)",
        "reviewed": 19,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 19,
        "triage_read": 0,
        "triage_snippet_classified": 19
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107872 OR 9423945 OR 9423946 OR 9423947)",
    "indexed_citing_opinions": 1673,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107872,
        "count": 1535,
        "count_source": "search"
      },
      {
        "opinion_id": 9423945,
        "count": 176,
        "count_source": "search"
      },
      {
        "opinion_id": 9423946,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423947,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2471,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/alderman-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc3NDE0ODcmcz02NDY2MjcwJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107872+OR+9423945+OR+9423946+OR+9423947%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107872,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 103663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 103765,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 105087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 105152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 105484,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 105746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 105920,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 107776,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 265063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 274556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 277533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 281359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 1139982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 1222210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 1237532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107872,
        "cited_id": 2443377,
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
    "date_created": "2026-07-04T17:01:18Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T17:01:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T17:01:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T17:23:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T17:01:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Alderman v. United States

```
<opinion data-order="14" data-type="opinion" id="x999-2" type="majority">
<author id="b241-6">Me. Justice White</author>
<p id="AC2">delivered the opinion of the Court.</p>
<p id="b241-7">After the convictions of petitioners had been affirmed, and while their cases were pending here, it was revealed that the United States had engaged in electronic surveillance which might have violated their Fourth Amendment rights and tainted their convictions. A remand to the District Court being necessary in each case for adjudication in the first instance, the questions now before us relate to the standards and procedures to be followed by the District Court in determining whether any of the Government's evidence supporting these convictions was the product of illegal surveillance to which any of the petitioners are entitled to object.</p>
<p id="b241-8">No. 133, O. T., 1967. Petitioners Alderman and Al-derisio, along with Ruby Kolod, now deceased, were convicted of conspiring to transmit murderous threats in interstate commerce, <span class="citation no-link">18 U. S. C. §§ 371</span>, 875 (c). Their convictions were affirmed on appeal, <span class="citation" data-id="274556"><a href="/opinion/274556/ruby-kolod-v-united-states-of-america-willie-israel-alderman-v-united/" aria-description="Citation for case: Ruby Kolod v. United States of America, Willie Israel...">371 F. 2d 983</a></span> (C. A. 10th Cir. 1967), and this Court denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./389/834/">389 U. S. 834</a></span> (1967). In their petition for rehearing, petitioners alleged they had recently discovered that Alderisio’s place of business in Chicago had been the subject of electronic surveillance by the Government. Reading the response of the Government to admit that Alderisio’s conversations had been overheard by unlawful <page-number citation-index="1" label="168">*168</page-number>electronic eavesdropping,<footnotemark>1</footnotemark> we granted the petition for rehearing over the objection of the United States that “no overheard conversation in which any of the petitioners participated is arguably relevant to this prosecution.” In our per <em>curiam </em>opinion, <span class="citation" data-id="107611"><a href="/opinion/107611/kolod-v-united-states/" aria-description="Citation for case: Kolod v. United States">390 U. S. 136</a></span> (1968), we refused to accept the <em>ex parte </em>determination of relevance by the Department of Justice in lieu of adversary proceedings in the District Court, vacated the judgment of the Court of Appeals, and remanded the case to the District Court for further proceedings.</p>
<p id="b242-5">The United States subsequently filed a motion to modify that order. Although accepting the Court’s order insofar as it required judicial determination of whether any of the prosecution’s evidence was the product of illegal surveillance, the United States urged that in order to protect innocent third parties participating or referred to in- irrelevant conversations overheard by the Government, surveillance records should first be subjected to <em>in camera </em>inspection by the trial judge, who would then turn over to the petitioners and their counsel only those materials arguably relevant to their prosecution. Petitioners opposed the motion, and the matter was argued before the Court last Term. We then set the case down for reargument at the opening of the current Term, <span class="citation multiple-matches"><a href="/c/U.%20S./392/919/">392 U. S. 919</a></span> (1968), the attention of the parties being directed to the disclosure issue and the question of <page-number citation-index="1" label="169">*169</page-number>standing to object to the Government’s use of the fruits of illegal surveillance.<footnotemark>2</footnotemark></p>
<p id="b243-5">Nos. 11 and 197. Both petitioners were convicted of conspiring to transmit to the Soviet Union information relating to the national defense of the United States, <span class="citation no-link">18 U. S. C. §§ 794</span> (a), (c), and of conspiring to violate <span class="citation no-link">18 U. S. C. § 951</span> by causing Butenko to act as an agent of the Soviet Union without prior notification to the Secretary of State. Butenko was also convicted of a substantive offense under <span class="citation no-link">18 U. S. C. § 951</span>. The Court of Appeals affirmed all but Ivanov’s conviction on the second conspiracy count. <span class="citation" data-id="277533"><a href="/opinion/277533/united-states-v-john-william-butenko-and-igor-a-ivanov-united-states-of/" aria-description="Citation for case: United States v. John William Butenko and Igor A. Ivanov,...">384 F. 2d 554</a></span> (C. A. 3d Cir. 1967). Petitions for certiorari were then filed in this Court, as was a subsequent motion to amend the <page-number citation-index="1" label="170">*170</page-number><em>Ivanov </em>petition to raise an issue similar to that which was presented in No. 133, O. T. 1967.<footnotemark>3</footnotemark> Following the first argument in <em>Alderman (sub nom. Kolod </em>v. <em>United States), </em>the petitions for certiorari of both Ivanov and Butenko were granted, limited to questions nearly identical to those involved in the reargument of the <em>Alderman </em>case.<footnotemark>4</footnotemark></p>
<p id="b245-4"><page-number citation-index="1" label="171">*171</page-number>I.</p>
<p id="b245-5">The exclusionary rule fashioned in <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914), and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), excludes from a criminal trial any evidence seized from the defendant in violation of his Fourth Amendment rights. Fruits of such evidence are excluded as well. <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385, 391-392</a></span> (1920). Because the Amendment now affords protection against the uninvited ear, oral statements, if illegally overheard, and their fruits are also subject to suppression. <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961); <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967).</p>
<p id="b245-6">In <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span> </em>and <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span>, </em>the defendant against whom the evidence was held to be inadmissible was the victim of the search. However, in the cases before us each petitioner demands retrial if any of the evidence used to convict him was the product of unauthorized surveillance, regardless of whose Fourth Amendment rights the surveillance violated. At the very least, it is urged that if evidence is inadmissible against one defendant or conspirator, because tainted by electronic surveillance illegal as to him, it is also inadmissible against his codefendant or coconspirator.</p>
<p id="b245-7">This expansive reading of the Fourth Amendment and of the exclusionary rule fashioned to enforce it is admittedly inconsistent with prior cases, and we reject it. The established principle is that suppression of the product of a Fourth Amendment violation can be successfully urged only by those whose rights were vio<page-number citation-index="1" label="172">*172</page-number>lated by the search itself, not by those who are aggrieved solely by the introduction of damaging evidence. Co-conspirators and codefendants have been accorded no special standing.</p>
<p id="b246-6">Thus in <em>Goldstein </em>v. <em>United States, </em><span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114</a></span> (1942), testimony induced by disclosing to witnesses their own telephonic communications intercepted by the Government contrary to <span class="citation no-link">47 U. S. C. § 605</span> was held admissible against their coconspirators. The Court equated the rule under § 605 with the exclusionary rule under the Fourth Amendment.<footnotemark>5</footnotemark> <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), came to like conclusions. There, two defendants were tried together; narcotics seized from a third party were held inadmissible against one defendant because they were the product of statements made by him at the time of his unlawful arrest. But the same narcotics were found to be admissible against the codefendant because “[t]he seizure of this <page-number citation-index="1" label="173">*173</page-number>heroin invaded no right of privacy of person or premises which would entitle [him] to object to its use at his trial. Cf. <em>Goldstein </em>v. <em>United States, </em><span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114</a></span>.” <em>Wong Sun </em>v. <em>United States, supra, </em>at 492.</p>
<p id="b247-4">The rule is stated in <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 261</a></span> (1960):</p>
<blockquote id="b247-5">“In order to qualify as a ‘person aggrieved by an unlawful search and seizure’ one must have been a victim of a search or seizure, one against whom the search was directed, as distinguished from one who claims prejudice only through the use of evidence gathered as a consequence of a search or seizure directed at someone else. . . .</blockquote>
<blockquote id="b247-6">“Ordinarily, then, it is entirely proper to require of one who seeks to challenge the legality of a search as the basis for suppressing relevant evidence that he allege, and if the allegation be disputed that he establish, that he himself was the victim of an invasion of privacy.” <footnotemark>6</footnotemark></blockquote>
<p id="b247-7">This same principle was twice acknowledged last Term. <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364</a></span> (1968); <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968).<footnotemark>7</footnotemark></p>
<p id="b248-4"><page-number citation-index="1" label="174">*174</page-number>We adhere to these cases and to the general rule that Fourth Amendment rights are personal rights which, like some other constitutional rights, may not be vicariously asserted. <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968); <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 267</a></span> (1960). Cf. <em>Tileston </em>v. <em>Ullman, </em><span class="citation" data-id="103765"><a href="/opinion/103765/tileston-v-ullman/#46" aria-description="Citation for case: Tileston v. Ullman">318 U. S. 44, 46</a></span> (1943). None of the special circumstances which prompted <em>NAACP </em>v. <em>Alabama, </em><span class="citation" data-id="105746"><a href="/opinion/105746/national-assn-for-the-advancement-of-colored-people-v-alabama-ex-rel/" aria-description="Citation for case: National Ass&#x27;n for the Advancement of Colored People v....">357 U. S. 449</a></span> (1958), and <em>Barrows </em>v. <em>Jackson, </em><span class="citation" data-id="9420983"><a href="/opinion/105152/barrows-v-jackson/" aria-description="Citation for case: Barrows v. Jackson">346 U. S. 249</a></span> (1953), are present here. There is no necessity to exclude evidence against one defendant in order to protect the rights of another. No rights of the victim of an illegal search are at stake when the evidence is offered against some other party. The victim can and very probably will object for himself when and if it becomes important for him to do so.</p>
<p id="b248-5">What petitioners appear to assert is an independent constitutional right of their own to exclude relevant and probative evidence because it was seized from another in violation of the Fourth Amendment. But we think there is a substantial difference for constitutional purposes between preventing the incrimination of a defendant through the very evidence illegally seized from him and suppressing evidence on the motion of a party who cannot claim this predicate for exclusion.</p>
<p id="b248-6">The necessity for that predicate was not eliminated by recognizing and acknowledging the deterrent aim of the rule. See <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965); <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/" aria-description="Citation for case: Elkins v. United States">364 U. S. 206</a></span> (1960). Neither those cases nor any others hold that anything which deters illegal searches is thereby commanded by the Fourth Amendment. The deterrent values of preventing the incrimination of those whose rights the police have violated have been considered sufficient to justify the suppression of probative evidence even though the case against the defendant is weakened or destroyed. We adhere to that judgment. But we are not convinced that <page-number citation-index="1" label="175">*175</page-number>the additional benefits of extending the exclusionary rule to other defendants would justify further encroachment upon the public interest in prosecuting those accused of crime and having them acquitted or convicted on the basis of all the evidence which exposes the truth.</p>
<p id="b249-4">We do not deprecate Fourth Amendment rights. The security of persons and property remain's a fundamental value which law enforcement officers must respect. Nor should those who flout the rules escape unscathed. In this respect we are mindful that there is now a comprehensive statute making unauthorized electronic surveillance a serious crime.<footnotemark>8</footnotemark> The general rule under the statute is that official eavesdropping and wiretapping are permitted only with probable cause and a warrant. Without experience showing the contrary, we should not assume that this new statute will be cavalierly disregarded or will not be enforced against transgressors.</p>
<p id="b249-5">Of course, Congress or state legislatures may extend the exclusionary rule and provide that illegally seized evidence is inadmissible against anyone for any purpose.<footnotemark>9</footnotemark> But for constitutional purposes, we are not now <page-number citation-index="1" label="176">*176</page-number>inclined to expand the existing rule that unlawful wiretapping or eavesdropping, whether deliberate or negligent, can produce nothing usable against the person aggrieved by the invasion.</p>
<p id="b250-4">II.</p>
<p id="b250-5">In these cases, therefore, any petitioner would be entitled to the suppression of government evidence originating in electronic surveillance violative of his own Fourth Amendment right to be free of unreasonable searches and seizures. Such violation would occur if the United States unlawfully overheard conversations of a petitioner himself or conversations occurring on his premises, whether or not he was present or participated in those conversations. The United States concedes this much and agrees that for purposes of a hearing to determine whether the Government’s evidence is tainted by illegal surveillance, the transcripts or recordings of the overheard conversations of any petitioner or of third persons on his premises must be duly and properly examined in the District Court.</p>
<p id="b250-6">MR. Justice Harlan and Mr. Justice Stewart, who are in partial dissent on this phase of the case, object to our protecting the homeowner against the use of third-party conversations overheard on his premises by an unauthorized surveillance. Their position is that unless the conversational privacy of the homeowner himself is invaded, there is no basis in the Fourth Amendment for excluding third-party conversations overheard on his premises. We cannot agree. If the police make an unwarranted search of a house and seize tangible property belonging to third parties — even a transcript of a third-party conversation — the homeowner may object to <page-number citation-index="1" label="177">*177</page-number>its use against him, not because he had any interest in the seized items as “effects” protected by the Fourth Amendment, but because they were the fruits of an unauthorized search of his house, which is itself expressly protected by the Fourth Amendment.<footnotemark>10</footnotemark> Nothing seen or found on the premises may legally form the basis for an arrest or search warrant or for testimony at the homeowner’s trial, since the prosecution would be using the fruits of a Fourth Amendment violation. <em>Silverthorne Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span> (1948); <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).</p>
<p id="b251-5">The Court has characteristically applied the same rule where an unauthorized electronic surveillance is carried out by physical invasion of the premises. This much the dissent frankly concedes. Like physical evidence which might be seized, overheard conversations are fruits <page-number citation-index="1" label="178">*178</page-number>of an illegal entry and are inadmissible in evidence. <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961); <em>Wong Sun </em>v. <em>United States, supra. </em>When <em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">Silverman</a></span> </em>was decided, no right of conversational privacy had been recognized as such; the right vindicated in that case was the Fourth Amendment right to be secure in one’s own home. In <em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>, </em>the words spoken by Blackie Toy when the police illegally entered his house were not usable against him because they were the fruits of a physical invasion of his premises which violated the Fourth Amendment.</p>
<p id="b252-6">Because the Court has now decided that the Fourth Amendment protects a person’s private conversations as well as his private premises, <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967), the dissent would discard the concept that private conversations overheard through an illegal entry into a private place must be excluded as the fruits of a Fourth Amendment violation. Although officers without a valid warrant may not search a house for physical evidence or incriminating information, whether the owner is present or away, the dissent would permit them to enter that house without consent and without a warrant, install a listening device, and use any overheard third-party conversations against the owner in a criminal case, in spite of the obvious violation of his Fourth Amendment right to be secure in his own dwelling. Even if the owner is present on his premises during the surveillance, he would have no complaint unless his own conversations were offered or used against him. Information from a telephone tap or from the microphone in the kitchen or in the rooms of guests or children would be freely usable as long as the homeowner’s own conversations are not monitored and used against him. Indeed, if the police, instead of installing a device, secreted themselves on the premises, they could neither testify about nor use against the owner anything they <page-number citation-index="1" label="179">*179</page-number>saw or carried away, but would be free to use against him everything they overheard except his own conversations. And should police overhear third parties describing narcotics which they have discovered in the owner’s desk drawer, the police could not then open the drawer and seize the narcotics, but they could secure a warrant on the basis of what they had heard and forthwith seize the narcotics pursuant to that warrant.<footnotemark>11</footnotemark></p>
<p id="b253-5">These views we do not accept. We adhere to the established view in this Court that the right to be secure in one’s house against unauthorized intrusion is not limited to protection against a policeman viewing or seizing tangible property — “papers” and “effects.” Otherwise, the express security for the home provided by the Fourth Amendment would approach redundancy. The rights of the owner of the premises are as clearly <page-number citation-index="1" label="180">*180</page-number>invaded when the police enter and install a listening device in his house as they are when the entry is made to undertake a warrantless search for tangible property; and the prosecution as surely employs the fruits of an illegal search of the home when it offers overheard third-party conversations as it does when it introduces tangible evidence belonging not to the homeowner, but to others. Nor do we believe that <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>, </em>by holding that the Fourth Amendment protects persons and their private conversations, was intended to withdraw any of the protection which the Amendment extends to the home or to overrule the existing doctrine, recognized at least since <em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">Silverman</a></span>, </em>that conversations as well as property are excludable from the criminal trial when they are found to be the fruits of an illegal invasion of the home. It was noted in <em>Silverman, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S., at 511-512</a></span>, that</p>
<blockquote id="b254-4">“This Court has never held that a federal officer may without warrant and without consent physically entrench into a man’s office or home, there secretly observe or listen, and relate at the man’s subsequent criminal triai what was seen or heard.”</blockquote>
<p id="b254-5">The Court proceeded to hold quite the contrary. We take the same course here.</p>
<p id="b254-6">III.</p>
<p id="b254-7">The remaining aspect of these cases relates to the procedures to be followed by the District Court in resolving the ultimate issue which will be before it — whether the evidence against any petitioner grew out of his illegally overheard conversations or conversations occurring on his premises.<footnotemark>12</footnotemark> The question as stated in <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 488</a></span> (1963), is “ ‘whether, <page-number citation-index="1" label="181">*181</page-number>granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint.’ ” See also <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939).</p>
<p id="b255-5">The Government concedes that it must disclose to petitioners any surveillance records which are relevant to the decision of this ultimate issue. And it recognizes that this disclosure must be made even though attended by potential danger to the reputation or safety of third parties or to the national security — unless the United States would prefer dismissal of the case to disclosure of the information. However, the Government contends that it need not be put to this disclose-or-dismiss option in the instant cases because none of the information obtained from its surveillance is “arguably relevant” to petitioners’ convictions, in the sense that none of the overheard conversations arguably underlay any of the evidence offered in these cases. Although not now insisting that its own evaluation of relevance should be accepted automatically and without judicial scrutiny, the United States urges that the records of the specified conversations be first submitted to the trial judge for an <em>in camera </em>examination. Any record found arguably relevant by the judge would be turned over to the petitioner whose Fourth Amendment rights have been violated, and that petitioner would then have the opportunity to use the disclosed information in his attempt to show that the Government has used tainted evidence to convict him. Material not arguably relevant would not be disclosed to any petitioner.<footnotemark>13</footnotemark></p>
<p id="b256-5"><page-number citation-index="1" label="182">*182</page-number>Although this may appear a modest proposal, especially since the standard for disclosure would be “arguable” relevance, we conclude that surveillance records as to which any petitioner has standing to object should be turned over to him without being screened <em>in camera </em>by the trial judge. Admittedly, there may be much learned from an electronic surveillance which ultimately contributes nothing to probative evidence. But winnowing this material from those items which might have made a substantial contribution to the case against a petitioner is a task which should not be entrusted wholly to the court in the first instance. It might be otherwise if the trial judge had only to place the transcript or other record of the surveillance alongside the record evidence and compare the two for textual or substantive similarities. Even that assignment would be difficult enough for the trial judge to perform unaided. But a good deal more is involved. An apparently innocent phrase, a chance remark, a reference to what appears to be a neutral person or event, the identity of a caller or the individual on the other end of a telephone, or even the manner of speaking or using words may have special significance to one who knows the more intimate facts of an accused’s life. And yet that information may be wholly colorless and devoid of meaning to one less well acquainted with all relevant circumstances. Unavoidably, this is a matter of judgment, but in our view the task is too complex, and the margin for error too great, to rely wholly on the <em>in camera </em>judgment of the trial court to identify those records which might have contributed to the Government’s case.<footnotemark>14</footnotemark></p>
<p id="b257-4"><page-number citation-index="1" label="183">*183</page-number>The United States concedes that when an illegal search has come to light, it has the ultimate burden of persuasion to show that its evidence is untainted. But at the same time petitioners acknowledge that they must go forward with specific evidence demonstrating taint. “[T]he trial judge must give opportunity, however closely confined, to the accused to prove that a substantial portion of the case against him was a fruit of the poisonous tree. This leaves ample opportunity to the Government to convince the trial court that its proof had an independent origin.” <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span> (1939). With this task ahead of them, and if the hearings are to be more than a formality and petitioners not left entirely to reliance on government testimony, there should be turned over to them the records of those overheard conversations which the Government was not entitled to use in building its case against them.</p>
<p id="b257-5">Adversary proceedings are a major aspect of our system of criminal justice. Their superiority as a means for attaining justice in a given case is nowhere more evident than in those cases, such as the ones at bar, where an issue must be decided on the basis of a large volume of <page-number citation-index="1" label="184">*184</page-number>factual materials, and after consideration of the many and subtle interrelationships which may exist among the facts reflected by these records. As the need for adversary inquiry is increased by the complexity of the issues presented for adjudication, and by the consequent inadequacy of <em>ex parte </em>procedures as a means for their accurate resolution, the displacement of well-informed advocacy necessarily becomes less justifiable.</p>
<p id="b258-6">Adversary proceedings will not magically eliminate all error, but they will substantially reduce its incidence by guarding against the possibility that the trial judge, through lack of time or unfamiliarity with the information contained in and suggested by the materials, will be unable to provide the scrutiny which the Fourth Amendment exclusionary rule demands. It may be that the prospect of disclosure will compel the Government to dismiss some prosecutions in deference to national security or third-party interests. But this is a choice the Government concededly faces with respect to material which it has obtained illegally and which it admits, or which a judge would find, is arguably relevant to the evidence offered against the defendant.<footnotemark>15</footnotemark></p>
<p id="b258-7">We think this resolution will avoid an exorbitant expenditure of judicial time and energy and will not unduly prejudice others or the public interest. It must be remembered that disclosure will be limited to the transcripts of a defendant’s own conversations and of those which took place on his premises. It can be safely <page-number citation-index="1" label="185">*185</page-number>assumed that much of this he will already know, and disclosure should therefore involve a minimum hazard to others. In addition, the trial court can and should, where appropriate, place a defendant and his counsel under enforceable orders against unwarranted disclosure of the materials which they may be entitled to inspect. See Fed. Rule Crim. Proc. 16 (e). We would not expect the district courts to permit the parties or counsel to take these orders lightly.</p>
<p id="b259-5">None of this means that any defendant will have an unlimited license to rummage in the files of the Department of Justice. Armed with the specified records of overheard conversations and with the right to cross-examine the appropriate officials in regard to the connection between those records and the case made against him, a defendant may need or be entitled to nothing else. Whether this is the case or not must be left to the informed discretion, good sense, and fairness of the trial judge. See <em>Nardone </em>v. <em>United States, </em><span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341-342</a></span> (1939).<footnotemark>16</footnotemark></p>
<p id="b259-6">IV.</p>
<p id="b259-7">Accordingly, in No. 133, O. T. 1967, the motion of the United States is denied to the extent that it requests an initial <em>in camera </em>inspection of the fruits of any unlawful <page-number citation-index="1" label="186">*186</page-number>surveillance and the withholding of those portions of the materials which the trial judge might deem irrelevant to these convictions. Primarily because of our decision with respect to standing, however, the order and judgment of January 29, 1968, are withdrawn. The order denying to petitioners a writ of certiorari is set aside. The petition for rehearing is granted, and the petition for certiorari is granted as to both Alderisio and Alderman. The judgments of the Court of Appeals for the Tenth Circuit in No. 133, O. T. 1967, and the judgments of the Court of Appeals for the Third Circuit in Nos. 11 and 197 are vacated, and each of the cases is remanded to the District Court for further proceedings consistent with this opinion, that is, for a hearing, findings, and conclusions (1) on the question of whether with respect to any petitioner there was electronic surveillance which violated his Fourth Amendment rights, and (2) if there was such surveillance with respect to any petitioner, on the nature and relevance to his conviction of any conversations which may have been overheard through that surveillance. The District Court should confine the evidence presented by both sides to that which is material to the question of the possible violation of a petitioner’s Fourth Amendment rights, to the content of conversations illegally overheard by surveillance which violated those rights and to the relevance of such conversations to the petitioner’s subsequent conviction. The District Court will make such findings of fact on those questions as may be appropriate in light of the further evidence and of the entire existing record. If the District Court decides on the basis of such findings (1) that there was electronic surveillance with respect to one or more petitioners but not any which violated the Fourth Amendment, or (2) that although there was a surveillance in violation of one or more of the petitioners’ Fourth Amendment rights, the conviction of such petitioner was not tainted <page-number citation-index="1" label="187">*187</page-number>by the use of evidence so obtained, it will enter new final judgments of conviction based on the existing record as supplemented by its further findings, thereby preserving to all affected parties the right to seek further appropriate appellate review. If, on the other hand, the District Court concludes in such further proceedings that there was a violation of any petitioner’s Fourth Amendment rights and that the conviction of the petitioner was tainted by such violation, it would then become its duty to accord such petitioner a new trial.</p>
<p id="b261-4">
<em>Vacated and remanded.</em>
</p>
<judges id="b261-5">Mr. Justice Douglas, while joining the opinion of the Court, concurs in Part II of the opinion of Mr. Justice Fortas and would hold that the protection of the Fourth Amendment includes also those against whom the investigation is directed.</judges>
<author id="b261-6">Mr. Justice Stewart.</author>
<p id="AXT">I join Mr. Justice Harlan’s separate opinion, except insofar as it would authorize <em>in camera </em>proceedings in the <em>Ivanov </em>and <em>Butenko </em>cases. I would apply the same standards to all three cases now before us, agreeing to that extent with the opinion of the Court.</p>
<judges id="b261-7">Mr. Justice Black dissents, adhering to his dissent in <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, 364 — 374 (1967).</judges>
<judges id="b261-8">Mr. Justice Marshall took no part in the consideration or decision of these cases.</judges>
<footnote label="1">
<p id="b242-6"> In its brief on reargument, the Government suggests that no electronic surveillance was conducted at places owned by Alderisio, but rather was carried out only at premises owned by his associates or by firms which employed him. The Government also contends that Alderisio himself did not have desk space at the subject premises. Finally, the Government asserts that Alderman neither participated in any conversation overheard nor had any interest in the places which were the object of the surveillance. These allegations by the Government will have to be considered by the District Court in the first instance, and we express no opinion now on their merit.</p>
</footnote>
<footnote label="2">
<p id="b243-6"> In our order of June 17,1968, restoring the Government’s motion to the calendar for reargument, <span class="citation multiple-matches"><a href="/c/U.%20S./392/919/">392 U. S. 919</a></span>-920, we requested counsel to include the following among issues to be discussed in briefs and oral argument:</p>
<p id="b243-7">“(1) Should the records of the electronic surveillance of petitioner Alderisio’s place of business be subjected to <em>in camera </em>inspection by the trial judge to determine the necessity of compelling the Government to make disclosure of such records to petitioners, and if so to what extent?</p>
<p id="b243-8">“(2) If <em>in camera </em>inspection is authorized or ordered, by what standards (for example, relevance and considerations of injury to persons or to reputations) should the trial judge determine whether the records are to be turned over to petitioners?</p>
<p id="b243-9">“(3) What standards are to be applied in determining whether each petitioner has standing to object to the use against him of the information obtained from the electronic surveillance of petitioner Alderisio’s place of business? More specifically, does petitioner Alderisio have standing to object to the use of any or all information obtained from such electronic surveillance whether or not he was present on the premises or party to a particular overheard conversation? Also, does petitioner Alderman have standing to object to the use against him of any or all information obtained from the electronic surveillance of petitioner Alderisio’s business establishment?”</p>
</footnote>
<footnote label="3">
<p id="b244-6"> The United States admits overhearing conversations of each petitioner, but where the surveillance took place and other pertinent details are unknown. In its brief the Government states:</p>
<p id="b244-7">“In some of the instances the installation had been specifically approved by the then Attorney General. In others the equipment was installed under a broader grant of authority to the F. B. I., in effect at that time, which did not require specific authorization. . . . [P] resent Department of Justice policy would call for specific authorization from the Attorney General for any use of electronic equipment in such cases.”</p>
<p id="b244-8">In all three cases, the District Court must develop the relevant facts and decide if the Government’s electronic surveillance was unlawful. Our assumption, for present purposes, is that the surveillance was illegal.</p>
</footnote>
<footnote label="4">
<p id="b244-9"> In each case the grant of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./392/923/">392 U. S. 923</a></span>, was limited to the following questions:</p>
<p id="b244-10">“On the assumption that there was electronic surveillance of petitioner or a codefendant which violated the Fourth Amendment,</p>
<p id="b244-11">“(1) Should the records of such electronic surveillance be subjected to <em>in camera </em>inspection by the trial judge to determine the necessity of compelling the Government to make disclosure of such records to petitioner, and if so to what extent?</p>
<p id="b244-12">“(2) If <em>in camera </em>inspection is to be authorized or ordered, by what standards (for example, relevance, and considerations of national security or injury to persons or reputations) should the trial judge determine whether the records are to be turned over to the defendant?</p>
<p id="b244-13">“(3) What standards are to be applied in determining whether petitioner has standing to object to the use against him of information obtained from such illegal surveillance? More specifically, if illegal surveillance took place at the premises of a particular defendant,</p>
<p id="b244-14">“(a) Does that defendant have standing to object to the use against him of any or all information obtained from the illegal sur<page-number citation-index="1" label="171">*171</page-number>veillance, whether or not he was present on the premises or party to the overheard conversation?</p>
<p id="b245-9">“(b) Does a codefendant have standing to object to the use against him of any or all information obtained from the illegal surveillance, whether or not he was present on the premises or party to the overheard conversation?”</p>
</footnote>
<footnote label="5">
<p id="b246-7"> As the issue was put and answered by the Court:</p>
<p id="b246-8">“The question now to be decided is whether we shall extend the sanction for violation of the Communications Act so as to make available to one not a party to the intercepted communication the objection that its use outside the courtroom, and prior to the trial, induced evidence which, except for that use, would be admissible.</p>
<p id="b246-9">“No court has ever gone so far in applying the implied sanction for violation of the Fourth Amendment. While this court has never been called upon to decide the point, the federal courts in numerous cases, and with unanimity, have denied standing to one not the victim of an unconstitutional search and seizure to object to the introduction in evidence of that which was seized. <em>A fortiori </em>the same rule should apply to the introduction of evidence induced by the use or disclosure thereof to a witness other than the victim of the seizure. We think no broader sanction should be imposed upon the Government in respect of violations of the Communications Act.” 316 U. S, at 121.</p>
<p id="b246-10">The Court noted that the principle had been applied “in at least fifty cases by the Circuit Courts of Appeals . . . not to mention many decisions by District Courts.” <em>Id., </em>at 121, n. 12.</p>
</footnote>
<footnote label="6">
<p id="b247-8"> The “person aggrieved” language is from Fed. Rule Crim. Proc. 41 (e). <em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span> </em>thus makes clear that Rule 41 conforms to the general standard and is no broader than the constitutional rule.</p>
</footnote>
<footnote label="7">
<p id="b247-9"> <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948), is not authority to the contrary. It is not at all clear that the <em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">McDonald</a></span> </em>opinion would automatically extend standing to a codefendant. Two of the five Justices joining the majority opinion did not read the opinion to do so and found the basis for the eodefendant’s standing to be the fact that he was a guest on the premises searched. “But even a guest may expect the shelter of the rooftree he is under against criminal intrusion.” <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#461" aria-description="Citation for case: McDonald v. United States"><em>Id., </em>at 461</a></span> (Jackson, J., concurring). Cf. <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960). Nor does <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293</a></span> (1966), lend any support to petitioners’ position, since the Court expressly put aside the issue of standing.</p>
</footnote>
<footnote label="8">
<p id="b249-6"> Title III, Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">Pub. L. 90-351, 82</span> Stat. 211. Not only does the Act impose criminal penalties upon those who violate its provisions governing eavesdropping and wiretapping, <span class="citation no-link">82 Stat. 213</span> (<span class="citation no-link">18 U. S. C. §2511</span> (1964 ed., Supp. IV)) (fine of not more than $10,000, or imprisonment for not more than five years, or both), but it also authorizes the recovery of civil damages by a person whose wire or oral communication is intercepted, disclosed, or used in violation of the Act, <span class="citation no-link">82 Stat. 223</span> (<span class="citation no-link">18 U. S. C. §2520</span> (1964 ed., Supp. IV)) (permitting recovery of actual and punitive damages, as well as a reasonable attorney’s fee and other costs of litigation reasonably incurred).</p>
</footnote>
<footnote label="9">
<p id="b249-7"> Congress has not done so. In its recent wiretapping and eavesdropping legislation, Congress has provided only that an “aggrieved person” may move to suppress the contents of a wire or oral communication intercepted in violation of the Act. Title III, Omnibus Crime Control and Safe Streets Act of 1968, <span class="citation no-link">82 Stat. 221</span> (<span class="citation no-link">18 U. S. C. § 2518</span> (10) (a) (1964 ed., Supp. IV)). The Act’s legislative history <page-number citation-index="1" label="176">*176</page-number>indicates that “aggrieved person,” the limiting phrase currently found in Fed. Rule Crim. Proc. 41 (e), should be construed in accordance with existent standing rules. See S. Rep. No. 1097, 90th Cong., 2d Sess., at 91, 106.</p>
</footnote>
<footnote label="10">
<p id="b251-6"> If the police enter a house pursuant to a valid warrant authorizing the seizure of specified gambling paraphernalia but discover illegal narcotics in the process of the search, the narcotics may be seized and introduced in evidence in the prosecution of the homeowner, whether the narcotics belong to him or to a third party. <em>E. g., Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#155" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 155</a></span> (1947). But if the officers have neither a warrant nor the consent of the householder, it is elementary Fourth Amendment law that the narcotics are suppressible on his motion. In both cases, however, the homeowner’s interest in the narcotics and his standing to object to their seizure are the same; and insofar as the Fourth Amendment’s protection of “effects” is concerned, the right of the officer to seize the contraband without a warrant and use it in evidence is identical. The reason that the narcotics may be seized and introduced in evidence in the first ease where there was a valid warrant, in spite of the householder’s interest in the narcotics and his standing to object, but not in the second case where there was no warrant is not the simple reason suggested by Mr. Justice Harlan that the householder has a property interest in the narcotics and therefore has “standing” to object. Rather, it is because in the first case there was no illegal invasion of the premises, while in the second the officer’s entry and search violated the Fourth Amendment, the narcotics being the fruit of that illegality.</p>
</footnote>
<footnote label="11">
<p id="b253-6"> Mr. Justice Harlan would also distinguish between the situation where a document belonging to a third party and containing his own words is seized from the premises of another without a warrant and the situation where the third party’s words are spoken and overheard by electronic surveillance. Under that view the words of the third party would be admissible in the latter instance but not in the former. We would exclude the evidence in both cases.</p>
<p id="b253-7">So also we do not distinguish between electronic surveillance which is carried out by means of a physical entry and surveillance which penetrates a private area without a technical trespass. This much, we think, <em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span> </em>makes quite clear. In either case, officialdom invades an area in which the homeowner has the right to expect privacy for himself, his family, and his invitees, and the right to object to the use against him of the fruits of that invasion, not because the rights of others have been violated, but because his own were. Those who converse and are overheard when the owner is not present also have a valid objection unless the owner of the premises has consented to the surveillance. Cf. <em>Mancusi </em>v. <em>DeForte, </em><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/#367" aria-description="Citation for case: Mancusi v. DeForte">392 U. S. 364, 367-370</a></span> (1968). The Fourth Amendment protects reasonable expectations of privacy and does not protect persons engaged in crime from the risk that those with whom they associate or converse will cooperate with the Government. <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#303" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 303</a></span> (1966).</p>
</footnote>
<footnote label="12">
<p id="b254-8"> It seems that in none of these cases were there introduced any recordings, transcripts, or other evidence, of the actual conversations overheard by electronic surveillance.</p>
</footnote>
<footnote label="13">
<p id="b255-6"> This would be true even, though the material on its face contained no threat of injury to the public interest or national security, apparently because, in the Government’s view, it would be very difficult to distinguish between that which threatened and that which <page-number citation-index="1" label="182">*182</page-number>did not. As explained below, we think similar difficulties inhere in distinguishing between records which are relevant to showing taint and those which are not.</p>
</footnote>
<footnote label="14">
<p id="b256-7"> In both the volume of the material to be examined and the complexity and difficulty of the judgments involved, cases involving <page-number citation-index="1" label="183">*183</page-number>electronic surveillance will probably differ markedly from those situations in the criminal law where <em>in camera </em>procedures have been found acceptable to some extent. <em>Dennis </em>v. <em>United States, </em><span class="citation" data-id="9423265"><a href="/opinion/107265/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">384 U. S. 855</a></span> (1966) (disclosure of grand jury minutes subject to <em>in camera </em>deletion of “extraneous material”); <em>Palermo </em>v. <em>United States, </em><span class="citation" data-id="9421845"><a href="/opinion/105920/palermo-v-united-states/#354" aria-description="Citation for case: Palermo v. United States">360 U. S. 343, 354</a></span> (1959) (whether the Jencks Act, <span class="citation no-link">18 U. S. C. § 3500</span>, requires disclosure of document to the defense); <em>Roviaro </em>v. <em>United States, </em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53</a></span> (1957) (disclosure of informant’s identity). In the <em><span class="citation" data-id="9423265"><a href="/opinion/107265/dennis-v-united-states/" aria-description="Citation for case: Dennis v. United States">Dennis</a></span> </em>case the Court noted that ordinarily “[t]rial judges ought not be burdened with the task or the responsibility of examining sometimes voluminous grand jury testimony,” and that it is not “realistic to assume that the trial court’s judgment as to the utility of material for impeachment or other legitimate purposes, however conscientiously made, would exhaust the possibilities.” <span class="citation" data-id="9423265"><a href="/opinion/107265/dennis-v-united-states/#874" aria-description="Citation for case: Dennis v. United States">384 U. S., at 874-875</a></span>.</p>
</footnote>
<footnote label="15">
<p id="b258-8"> The dissents, it should be noted, would require turnover of arguably relevant material, whatever its impact on national security might be. To this extent there is agreement that the defendant’s interest in excluding the fruits of illegally obtained evidence entitles him to the product of the surveillance. Given this basic proposition, the matter comes down to a judgment as to whether <em>in camera </em>inspection would characteristically be sufficiently reliable when national security interests are at stake. On this issue, the majority and the dissenters part company.</p>
</footnote>
<footnote label="16">
<p id="b259-8"> The Chief Justice, Mr. Justice Douglas, Mr. Justice Brennan, and Mr. Justice White join the entire opinion of the Court. In addition, Mr. Justice Harlan and Mr. Justice Stewart join the opinion to the extent that it denies standing to codefendants, coconspirators, and others whose Fourth Amendment rights have not been violated by the electronic surveillance involved. The four members of the Court joining the entire opinion agree with the opinion in recognizing the householder’s standing to object to evidence obtained from an unauthorized electronic surveillance of his premises even where his own conversations are not overheard; Mr. Justice Fortas concurs in the judgment to this extent. Finally, Mr. Justice Stewart, in addition to the four members of the Court joining the entire opinion, agrees with Part III of the opinion.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Almeida-Sanchez v. United States.md  (`case`, 6 assertions)

### content_page

```
---
title: "Almeida-Sanchez v. United States"
type: case
citation: "413 U.S. 266 (1973)"
parallel_cite: "93 S. Ct. 2535; 37 L. Ed. 2d 596"
neutral_cite: 1973 U.S. LEXIS 44
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1973
date_decided: 1973-06-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1973-06-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Almeida-Sanchez v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108845/almeida-sanchez-v-united-states/"
  cluster_id: 108845
  opinion_id: 108845
  identity_checked: true
homes:
  - page: "[[Border Searches]]"
    role: "Key — Anchor"
  - page: "[[The Exclusionary Rule]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Brignoni-Ponce]]", "[[United States v. Martinez-Fuerte]]", "[[Carroll v. United States]]"]
aliases: ["Almeida-Sanchez v. US"]
tags: ["case", "fourth-amendment", "border-searches", "automobile"]
holding: "A warrantless search of a vehicle by a roving Border Patrol on a California road at least 20 miles north of the Mexican border, without…"
lake:
  record_id: Almeida-Sanchez v. United States
  status: verified
  projected_at: 2026-07-06
---

# Almeida-Sanchez v. United States

*413 U.S. 266 (1973)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A roving Border Patrol stopped and searched the petitioner's car on a California highway that lay at all points at least 20 miles north of the Mexican border. There was no warrant, no probable cause, and no consent; the search was purportedly authorized by statute and regulation permitting searches within a "reasonable distance" (defined as 100 air miles) of the border. Marijuana was found and used to convict.

## Issue
Whether a warrantless, suspicionless search of a vehicle by a roving Border Patrol — conducted away from the border and without probable cause or consent — is consistent with the Fourth Amendment.

## Rule
No. A genuine border search, or a search at the border's "functional equivalent," stands on special footing: "searches of this kind may in certain circumstances take place not only at the border itself, but at its functional equivalents as well." — 413 U.S. at 272. ^pin-272

But a roving-patrol search away from the border is ordinary Fourth Amendment business and needs probable cause or consent: "But the search of the petitioner's automobile by a roving patrol, on a California road that lies at all points at least 20 miles north of the Mexican border, was of a wholly different sort. In the absence of probable cause or consent, that search violated the petitioner's Fourth Amendment right to be free of 'unreasonable searches and seizures.'" — *Id.* at 273. ^pin-273

## Application
The search here was not at the border or its functional equivalent (an established checkpoint at a confluence of border roads, or an airport receiving a nonstop foreign flight) — it was a roving-patrol search on a highway at least 20 miles inland, with no warrant, no probable cause, and no consent. On these facts the search violated the Fourth Amendment, and the statute and regulation purporting to authorize it could not override that constitutional requirement.

## Conclusion
The roving-patrol search was unconstitutional and the seized evidence should have been suppressed; the judgment of conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Almeida-Sanchez* anchors the limit on roving interior immigration searches and introduces the "functional equivalent of the border" concept. The border-search framework was developed by [[United States v. Brignoni-Ponce]] (a roving patrol may *stop* a vehicle on reasonable suspicion) and [[United States v. Martinez-Fuerte]] (permanent interior checkpoints may stop vehicles without individualized suspicion) — refinements that leave this holding intact.

## Appears on
- [[Border Searches]] — *Key — Anchor*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*

## Sources
- *Almeida-Sanchez v. United States*, 413 U.S. 266 (1973) — https://www.courtlistener.com/opinion/108845/almeida-sanchez-v-united-states/ — pinpoints: 272, 273.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2786827bf48ad6dd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "413 U.S. 266 (1973)", "court": "U.S. Supreme Court", "neutral_cite": "1973 U.S. LEXIS 44", "official_citation_present": true, "parallel_cite": "93 S. Ct. 2535; 37 L. Ed. 2d 596", "title": "Almeida-Sanchez v. United States", "year": "1973"}}
{"assertion_id": "10a6fc55212a4c65", "dimension": "support", "kind": "home_role", "locator": {"home": "Border Searches"}, "payload": {"home": "Border Searches", "role": "Key — Anchor", "title": "Almeida-Sanchez v. United States"}}
{"assertion_id": "90629218068317af", "dimension": "support", "kind": "home_role", "locator": {"home": "The Exclusionary Rule"}, "payload": {"home": "The Exclusionary Rule", "role": "Related (cross-doctrine)", "title": "Almeida-Sanchez v. United States"}}
{"assertion_id": "ce941bd3d0a73393", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A warrantless search of a vehicle by a roving Border Patrol on a California road at least 20 miles north of the Mexican border, without…", "title": "Almeida-Sanchez v. United States"}}
{"assertion_id": "4628475ee125c12a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Almeida-Sanchez v. United States"}}
{"assertion_id": "c4ec217bb749e732", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1973-06-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Almeida-Sanchez v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Almeida-Sanchez v. United States", "varies_by_point": "false"}}
```

### lake record — Almeida-Sanchez v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Almeida-Sanchez v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Almeida-Sanchez v. United States",
    "case_name_short": "Almeida-Sanchez",
    "case_name_full": "Almeida-Sanchez v. United States",
    "input_case_name": "Almeida-Sanchez v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1973-06-21",
    "year": 1973,
    "docket": null,
    "cluster_id": 108845,
    "lead_opinion_id": 108845,
    "sibling_ids": [
      108845,
      9425395,
      9425396,
      9425397
    ],
    "absolute_url": "/opinion/108845/almeida-sanchez-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8992646,
        "score": 10,
        "case_name": "Almeida-Sanchez v. United States"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "413 U.S. 266",
      "volume": "413",
      "reporter": "U.S.",
      "page": "266",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "93 S. Ct. 2535",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 596",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1973 U.S. LEXIS 44",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "44",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "413 U.S. 266",
        "volume": "413",
        "reporter": "U.S.",
        "page": "266",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "93 S. Ct. 2535",
        "volume": "93",
        "reporter": "S. Ct.",
        "page": "2535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "37 L. Ed. 2d 596",
        "volume": "37",
        "reporter": "L. Ed. 2d",
        "page": "596",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1973 U.S. LEXIS 44",
        "volume": "1973",
        "reporter": "U.S. LEXIS",
        "page": "44",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "413 U.S. 266",
    "official_selection": {
      "court_class": "scotus",
      "selected": "413 U.S. 266",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-272",
      "page": null,
      "quote": "(defined as 100 air miles) of the border. Marijuana was found and used to convict. ## Issue Whether a warrantless, suspicionless search of a vehicle by a roving Border Patrol \u2014 conducted away from the border and without probable cause or consent \u2014 is consistent with the Fourth Amendment. ## Rule No. A genuine border search, or a search at the border's",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-273",
      "page": null,
      "quote": "But the search of the petitioner's automobile by a roving patrol, on a California road that lies at all points at least 20 miles north of the Mexican border, was of a wholly different sort. In the absence of probable cause or consent, that search violated the petitioner's Fourth Amendment right to be free of 'unreasonable searches and seizures.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1973-06-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Almeida-Sanchez v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Fooks v. State",
          "cluster_id": 10600118,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Shane Timothy Bakke",
          "cluster_id": 6619858,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Phillip Walker-Brazie & Brandi-Lena Butterfield",
          "cluster_id": 5139667,
          "cite": [
            "280 A.3d 24",
            "2021 VT 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Brian De Arrie McGee",
          "cluster_id": 4883113,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Fleming",
          "cluster_id": 4832864,
          "cite": [
            "162 N.E.3d 981",
            "2020 Ohio 5352"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leaders of Beautiful Struggle v. Baltimore Police Department",
          "cluster_id": 4803842,
          "cite": [
            "979 F.3d 219"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Billy Curry, Jr.",
          "cluster_id": 4787848,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Raymond Aigbekaen",
          "cluster_id": 4680725,
          "cite": [
            "943 F.3d 713"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Logan Vanderhoef v. Maurice Dixon",
          "cluster_id": 4654472,
          "cite": [
            "938 F.3d 271"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Miguel Cano",
          "cluster_id": 4649091,
          "cite": [
            "934 F.3d 1002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Donald Wanjiku",
          "cluster_id": 4601308,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Donald Wanjiku",
          "cluster_id": 4601253,
          "cite": [
            "919 F.3d 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hamza Kolsuz",
          "cluster_id": 4499413,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hamza Kolsuz",
          "cluster_id": 4496513,
          "cite": [
            "890 F.3d 133"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marcopoulos, Andreas",
          "cluster_id": 4455001,
          "cite": [
            "538 S.W.3d 596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Luis Sanchez v. Jefferson Sessions",
          "cluster_id": 4422886,
          "cite": [
            "870 F.3d 901",
            "2017 WL 3723238",
            "2017 U.S. App. LEXIS 16625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended September 13, 2016 State of Iowa v. Mar'yo D. Lindsey Jr.",
          "cluster_id": 4472005,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Mar'yo D. Lindsey Jr.",
          "cluster_id": 3216871,
          "cite": [
            "881 N.W.2d 411",
            "2016 Iowa Sup. LEXIS 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Andreas Marcopoulos v. State",
          "cluster_id": 3194184,
          "cite": [
            "492 S.W.3d 773",
            "2016 WL 1479703",
            "2016 Tex. App. LEXIS 3911"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Yong Shik Won",
          "cluster_id": 3158283,
          "cite": [
            "137 Haw. 330",
            "372 P.3d 1065",
            "2015 Haw. LEXIS 352"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sanchez",
          "cluster_id": 2815058,
          "cite": [
            "2015 NMSC 18",
            "8 N.M. Ct. App. 27",
            "2015 NMSC 018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gutierrez",
          "cluster_id": 2804164,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jae Shik Kim",
          "cluster_id": 2799603,
          "cite": [
            "103 F. Supp. 3d 32",
            "2015 U.S. Dist. LEXIS 60306"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "STATE OF TENNESSEE v. CHARLES A. KENNEDY",
          "cluster_id": 2739756,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jesus Hernandez v. USA",
          "cluster_id": 2681508,
          "cite": [
            "757 F.3d 249",
            "2014 WL 2932598"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lee",
          "cluster_id": 2674606,
          "cite": [
            "2014 IL App (1st) 130507"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Butorac",
          "cluster_id": 2679461,
          "cite": [
            "2013 IL App (2d) 110953"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Rennis",
          "cluster_id": 8210127,
          "cite": [
            "195 Vt. 492",
            "2014 Vt. 8",
            "90 A.3d 906",
            "2014 VT 8",
            "2014 WL 185028",
            "2014 Vt. LEXIS 5"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Harry Katzin",
          "cluster_id": 1086355,
          "cite": [
            "732 F.3d 187",
            "2013 WL 5716367",
            "2013 U.S. App. LEXIS 21377"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Booker Powell",
          "cluster_id": 1043365,
          "cite": [
            "732 F.3d 361",
            "2013 WL 5493969"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christine Ann Kern",
          "cluster_id": 4472227,
          "cite": [
            "831 N.W.2d 149",
            "2013 WL 2278018",
            "2013 Iowa Sup. LEXIS 61"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Howard Cotterman",
          "cluster_id": 854692,
          "cite": [
            "709 F.3d 952",
            "2013 WL 856292",
            "2013 U.S. App. LEXIS 4731"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brown",
          "cluster_id": 2509614,
          "cite": [
            "726 S.E.2d 654",
            "315 Ga. App. 154",
            "2012 Fulton County D. Rep. 1288",
            "2012 Ga. App. LEXIS 337"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Klager",
          "cluster_id": 902104,
          "cite": [
            "2011 S.D. 12",
            "797 N.W.2d 47",
            "2011 SD 12",
            "2011 S.D. LEXIS 12",
            "2011 WL 1228292"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cotterman",
          "cluster_id": 213651,
          "cite": [
            "637 F.3d 1068",
            "2011 U.S. App. LEXIS 6483",
            "2011 WL 1137302"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Walker",
          "cluster_id": 2474386,
          "cite": [
            "771 F. Supp. 2d 803",
            "2011 U.S. Dist. LEXIS 13760",
            "2011 WL 651414"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. James Maximiliano Ochoa",
          "cluster_id": 4472474,
          "cite": [
            "792 N.W.2d 260",
            "2010 Iowa Sup. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "True v. Nebraska",
          "cluster_id": 150327,
          "cite": [
            "612 F.3d 676",
            "30 I.E.R. Cas. (BNA) 1537",
            "2010 U.S. App. LEXIS 14007",
            "93 Empl. Prac. Dec. (CCH) 43,931",
            "2010 WL 2696744"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Villasenor",
          "cluster_id": 148280,
          "cite": [
            "608 F.3d 467",
            "2010 U.S. App. LEXIS 11833",
            "2010 WL 2303334"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hilario Alfaro-Moncada",
          "cluster_id": 3049883,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alfaro-Moncada",
          "cluster_id": 147332,
          "cite": [
            "607 F.3d 720",
            "2010 A.M.C. 1680",
            "2010 U.S. App. LEXIS 10841",
            "2010 WL 2103442"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stewart",
          "cluster_id": 2538573,
          "cite": [
            "715 F. Supp. 2d 750",
            "2010 U.S. Dist. LEXIS 50876",
            "2010 WL 2089355"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carmichael v. Village of Palatine, Ill.",
          "cluster_id": 146911,
          "cite": [
            "605 F.3d 451",
            "2010 U.S. App. LEXIS 10378",
            "2010 WL 2011509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 1584196,
          "cite": [
            "24 So. 3d 671",
            "2009 Fla. App. LEXIS 19763",
            "2009 WL 4874530"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Peoples",
          "cluster_id": 1404047,
          "cite": [
            "668 F. Supp. 2d 1042",
            "2009 U.S. Dist. LEXIS 104573",
            "2009 WL 3586564"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Vasquez-Rosales",
          "cluster_id": 3064935,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Guzman-Padilla",
          "cluster_id": 1448445,
          "cite": [
            "573 F.3d 865",
            "2009 U.S. App. LEXIS 16298",
            "2009 WL 2182818"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Denson v. United States",
          "cluster_id": 78422,
          "cite": [
            "574 F.3d 1318",
            "2009 U.S. App. LEXIS 15634",
            "2009 WL 2031036"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gowadia",
          "cluster_id": 2469880,
          "cite": [
            "610 F. Supp. 2d 1234",
            "2009 U.S. Dist. LEXIS 16502",
            "2009 WL 529097"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Whitted",
          "cluster_id": 3035592,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Whitted",
          "cluster_id": 1441555,
          "cite": [
            "541 F.3d 480",
            "50 V.I. 1081",
            "43 A.L.R. 6th 771",
            "2008 U.S. App. LEXIS 18916",
            "2008 WL 4107473"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Moya-Matute",
          "cluster_id": 2472669,
          "cite": [
            "735 F. Supp. 2d 1306",
            "2008 U.S. Dist. LEXIS 119558",
            "2008 WL 8053484"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Arnold",
          "cluster_id": 1234252,
          "cite": [
            "533 F.3d 1003",
            "2008 U.S. App. LEXIS 14690",
            "45 A.L.R. Fed. 2d 715",
            "2008 WL 2675794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Arnold",
          "cluster_id": 3052269,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Askew",
          "cluster_id": 187180,
          "cite": [
            "529 F.3d 1119",
            "2008 WL 2468501"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Arnold",
          "cluster_id": 3051719,
          "cite": [
            "523 F.3d 941",
            "2008 U.S. App. LEXIS 8590",
            "2008 WL 1776525"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re United States for an Order Directing a Provider of Electronic Communication Service to Disclose Records to the Government",
          "cluster_id": 2451365,
          "cite": [
            "534 F. Supp. 2d 585",
            "2008 U.S. Dist. LEXIS 13733",
            "2008 WL 483434"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Moya-Matute",
          "cluster_id": 2580818,
          "cite": [
            "559 F. Supp. 2d 1189",
            "2008 U.S. Dist. LEXIS 42380",
            "2008 WL 2323522"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. McGinnis",
          "cluster_id": 2975657,
          "cite": [
            "247 F. App'x 589"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Abbouchi",
          "cluster_id": 1235958,
          "cite": [
            "502 F.3d 850",
            "2007 U.S. App. LEXIS 21280",
            "2007 WL 2493507"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Abbouchi",
          "cluster_id": 3050017,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Abbouchi",
          "cluster_id": 3049356,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Warshak v. United States",
          "cluster_id": 2975254,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Steven Warshak v. United States",
          "cluster_id": 798096,
          "cite": [
            "490 F.3d 455",
            "2007 U.S. App. LEXIS 14297",
            "2007 WL 1730094"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Heapy",
          "cluster_id": 2638152,
          "cite": [
            "151 P.3d 764",
            "113 Haw. 283",
            "2007 Haw. LEXIS 13"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gurr, Bernard",
          "cluster_id": 186816,
          "cite": [
            "471 F.3d 144",
            "374 U.S. App. D.C. 21",
            "2006 U.S. App. LEXIS 30104"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ellison",
          "cluster_id": 2974262,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Curtis Ellison",
          "cluster_id": 795627,
          "cite": [
            "462 F.3d 557",
            "2006 U.S. App. LEXIS 22558",
            "2006 WL 2527973"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Barnaby",
          "cluster_id": 887572,
          "cite": [
            "2006 MT 203",
            "142 P.3d 809",
            "333 Mont. 220",
            "2006 Mont. LEXIS 399"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martinez-Aguero v. Gonzalez",
          "cluster_id": 44591,
          "cite": [
            "459 F.3d 618",
            "2006 WL 2242365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Romm",
          "cluster_id": 3038099,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Stuart Romm",
          "cluster_id": 795139,
          "cite": [
            "455 F.3d 990",
            "2006 U.S. App. LEXIS 18474",
            "2006 WL 2042827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Najar",
          "cluster_id": 167674,
          "cite": [
            "451 F.3d 710",
            "2006 U.S. App. LEXIS 15171",
            "2006 WL 1689231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. McClain",
          "cluster_id": 2973671,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kevin McClain George Brandt Jason Davis",
          "cluster_id": 793975,
          "cite": [
            "444 F.3d 537",
            "2006 U.S. App. LEXIS 7895",
            "2006 WL 827811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "AA Ex Rel. BA v. ATTY. GENERAL",
          "cluster_id": 2354253,
          "cite": [
            "894 A.2d 31",
            "384 N.J. Super. 67"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Buchanan Ex Rel. Estate of Buchanan v. Maine",
          "cluster_id": 2458001,
          "cite": [
            "417 F. Supp. 2d 45",
            "2006 U.S. Dist. LEXIS 6292",
            "2006 WL 367340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jackson, Tarry",
          "cluster_id": 186498,
          "cite": [
            "415 F.3d 88",
            "367 U.S. App. D.C. 320",
            "2005 U.S. App. LEXIS 14951",
            "2005 WL 1704843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Seljan",
          "cluster_id": 2438909,
          "cite": [
            "328 F. Supp. 2d 1077",
            "2004 U.S. Dist. LEXIS 14978",
            "2004 WL 1749495"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Rogers",
          "cluster_id": 2371475,
          "cite": [
            "849 A.2d 1185",
            "578 Pa. 127",
            "2004 Pa. LEXIS 1252"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Boumelhem",
          "cluster_id": 2970815,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ali Boumelhem",
          "cluster_id": 783064,
          "cite": [
            "339 F.3d 414",
            "2003 U.S. App. LEXIS 16425",
            "2003 WL 21914106"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Augustin Romero-Bustamente",
          "cluster_id": 782919,
          "cite": [
            "337 F.3d 1104",
            "2003 Daily Journal DAR 8541",
            "2003 Cal. Daily Op. Serv. 6765",
            "2003 U.S. App. LEXIS 15249",
            "2003 WL 21757130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Tobin",
          "cluster_id": 1962653,
          "cite": [
            "828 A.2d 415",
            "2003 Pa. Commw. LEXIS 453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Derrick A. Wiley v. Department of Justice",
          "cluster_id": 781964,
          "cite": [
            "328 F.3d 1346",
            "2003 U.S. App. LEXIS 9175",
            "2003 WL 21060833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lidster",
          "cluster_id": 3134880,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Lidster",
          "cluster_id": 2070661,
          "cite": [
            "779 N.E.2d 855",
            "202 Ill. 2d 1",
            "269 Ill. Dec. 1",
            "2002 Ill. LEXIS 944"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hurn v. United States",
          "cluster_id": 2486148,
          "cite": [
            "221 F. Supp. 2d 493",
            "2002 U.S. Dist. LEXIS 18238",
            "2002 WL 31156059"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bradley v. United States",
          "cluster_id": 3012161,
          "cite": [
            "299 F.3d 197",
            "2002 U.S. App. LEXIS 14960",
            "2002 WL 1723779"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bradley v. United States",
          "cluster_id": 778647,
          "cite": [
            "299 F.3d 197"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pollard",
          "cluster_id": 2425044,
          "cite": [
            "209 F. Supp. 2d 525",
            "2002 WL 1363433",
            "2002 U.S. Dist. LEXIS 10989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Willie Lee Douglas v. State of Texas",
          "cluster_id": 2904221,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kim Ho Ma v. Ashcroft",
          "cluster_id": 7095993,
          "cite": [
            "257 F.3d 1095",
            "2001 WL 845325"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kim Ho Ma v. John D. Ashcroft",
          "cluster_id": 774115,
          "cite": [
            "257 F.3d 1095",
            "2001 Cal. Daily Op. Serv. 6360",
            "2001 Daily Journal DAR 7799",
            "2001 U.S. App. LEXIS 16866"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dixon v. State",
          "cluster_id": 2276800,
          "cite": [
            "758 A.2d 1063",
            "133 Md. App. 654",
            "2000 Md. App. LEXIS 143"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Legg",
          "cluster_id": 1341701,
          "cite": [
            "536 S.E.2d 110",
            "207 W. Va. 686",
            "2000 W. Va. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kim Ho Ma v. Reno",
          "cluster_id": 7080220,
          "cite": [
            "208 F.3d 815",
            "2000 Daily Journal DAR 3695",
            "2000 Cal. Daily Op. Serv. 2744",
            "2000 U.S. App. LEXIS 6434"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kim Ho Ma v. Janet Reno",
          "cluster_id": 768268,
          "cite": [
            "208 F.3d 815"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 1614689,
          "cite": [
            "2000 WI 3",
            "604 N.W.2d 517",
            "231 Wis. 2d 723",
            "2000 Wisc. LEXIS 3"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Beras",
          "cluster_id": 198546,
          "cite": [
            "183 F.3d 22",
            "1999 U.S. App. LEXIS 15062",
            "1999 WL 447158"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lowe v. Pogue",
          "cluster_id": 1087697,
          "cite": [
            "143 L. Ed. 2d 384",
            "119 S. Ct. 1238",
            "526 U.S. 273",
            "1999 U.S. LEXIS 2249"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Rubio-Hernandez",
          "cluster_id": 2286418,
          "cite": [
            "39 F. Supp. 2d 808",
            "1999 U.S. Dist. LEXIS 3727",
            "1999 WL 170549"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph H. Norwood, Individually and as Representative of a Class of Citizens v. W.C. Bain, Jr., Individually and in His Official Capacity as Director of Public Safety for the City of Spartanburg Police Department City of Spartanburg, Joseph H. Norwood, Individually and as Representative of a Class of Citizens v. W.C. Bain, Jr., Individually and in His Official Capacity as Director of Public Safety for the City of Spartanburg Police Department City of Spartanburg",
          "cluster_id": 760958,
          "cite": [
            "166 F.3d 243",
            "1999 U.S. App. LEXIS 244"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hulit v. State",
          "cluster_id": 2452885,
          "cite": [
            "982 S.W.2d 431",
            "1998 Tex. Crim. App. LEXIS 174",
            "1998 WL 870923"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Loesch v. State",
          "cluster_id": 2416636,
          "cite": [
            "979 S.W.2d 47",
            "1998 Tex. App. LEXIS 6295",
            "1998 WL 698540"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "DEPT. OF BUSINESS v. Calder Race Course",
          "cluster_id": 1847855,
          "cite": [
            "724 So. 2d 100",
            "1998 WL 422515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Norwood v. Bain",
          "cluster_id": 2966869,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph H. Norwood, Individually and as Representative of a Class of Citizens v. W.C. Bain, Jr., Individually and in His Official Capacity as Director of Public Safety for the City of Spartanburg Police Department City of Spartanburg, Joseph H. Norwood, Individually and as Representative of a Class of Citizens v. W.C. Bain, Jr., Individually and in His Official Capacity as Director of Public Safety for the City of Spartanburg Police Department City of Spartanburg",
          "cluster_id": 754238,
          "cite": [
            "143 F.3d 843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "AL Post 763 v. Ohio Liquor Control Comm.",
          "cluster_id": 10684485,
          "cite": [
            "1998 Ohio 367",
            "82 Ohio St. 3d 108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "UNITED STATES of America, Plaintiff-Appellee, v. Francisco Javier SANTOS-PINON, Defendant-Appellant",
          "cluster_id": 755244,
          "cite": [
            "146 F.3d 734",
            "98 Daily Journal DAR 6584",
            "98 Cal. Daily Op. Serv. 4636",
            "1998 U.S. App. LEXIS 12796",
            "1998 WL 315489"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gora v. City of Ferndale",
          "cluster_id": 1572900,
          "cite": [
            "576 N.W.2d 141",
            "456 Mich. 704"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Mendez",
          "cluster_id": 1195185,
          "cite": [
            "947 P.2d 256",
            "88 Wash. App. 785"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Taylor",
          "cluster_id": 1624122,
          "cite": [
            "564 N.W.2d 24",
            "454 Mich. 580"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Codner",
          "cluster_id": 1729200,
          "cite": [
            "696 So. 2d 806",
            "1997 WL 100951"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alvarado-Ramirez",
          "cluster_id": 8750513,
          "cite": [
            "975 F. Supp. 906",
            "1997 U.S. Dist. LEXIS 13054",
            "1997 WL 538882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ramon Navarro",
          "cluster_id": 722575,
          "cite": [
            "90 F.3d 1245",
            "1996 WL 411847"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Loesch v. State",
          "cluster_id": 1677573,
          "cite": [
            "921 S.W.2d 405",
            "1996 Tex. App. LEXIS 1349",
            "1996 WL 155214"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Richard Townes, Jr. v. Edward W. Murray, Director",
          "cluster_id": 706844,
          "cite": [
            "68 F.3d 840",
            "1995 U.S. App. LEXIS 30789",
            "1995 WL 627452"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Cass",
          "cluster_id": 2381454,
          "cite": [
            "666 A.2d 313",
            "446 Pa. Super. 66",
            "1995 Pa. Super. LEXIS 3166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Oriakhi",
          "cluster_id": 698332,
          "cite": [
            "57 F.3d 1290",
            "1995 U.S. App. LEXIS 15499",
            "1995 WL 369608"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Barona",
          "cluster_id": 7032767,
          "cite": [
            "56 F.3d 1087",
            "1995 WL 329267"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Maria Cecilia Barona, United States of America v. Janet Martinez, Aka: Luz Janet Martinez & Luz Janeth Martinez, United States of America v. Brian Bennett, United States of America v. Mario Ernesto Villabona-Alvarado, A/K/A Tico, United States of America v. Michael Dubarry McCarver A/K/A Mike Bald, United States of America v. Michael Harris, A/K/A Tall Make",
          "cluster_id": 697352,
          "cite": [
            "56 F.3d 1087",
            "95 Daily Journal DAR 7174",
            "95 Cal. Daily Op. Serv. 4161",
            "1995 U.S. App. LEXIS 13590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Brickhouse",
          "cluster_id": 2617617,
          "cite": [
            "20 Kan. App. 2d 495",
            "890 P.2d 353",
            "1995 Kan. App. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Daniel Inocencio, Evaristo Hinojosa, Sr., Daniel Alfonso Reyes",
          "cluster_id": 682752,
          "cite": [
            "40 F.3d 716"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hinojosa",
          "cluster_id": 6811,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kimbrew v. Evansville Police Department",
          "cluster_id": 1456169,
          "cite": [
            "867 F. Supp. 818",
            "1994 U.S. Dist. LEXIS 16126",
            "1994 WL 630879"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jewel Rose Hyde Patricia Yvonne Gray Karen Boothe, A/K/A Karen Boothe-Waller, A/K/A Karen Ann Marie Boothe",
          "cluster_id": 679542,
          "cite": [
            "37 F.3d 116",
            "30 V.I. 475",
            "1994 U.S. App. LEXIS 27085",
            "1994 WL 524547"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Valenzuela",
          "cluster_id": 2270705,
          "cite": [
            "28 Cal. App. 4th 817",
            "33 Cal. Rptr. 2d 802",
            "94 Cal. Daily Op. Serv. 7452",
            "94 Daily Journal DAR 13603",
            "1994 Cal. App. LEXIS 980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilkerson v. Whitley",
          "cluster_id": 7029344,
          "cite": [
            "28 F.3d 498",
            "1994 U.S. App. LEXIS 21373",
            "1994 WL 390132"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilkerson v. Whitley",
          "cluster_id": 6539,
          "cite": [
            "28 F.3d 498"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Joseph Walton, as Next Friend of Christopher Walton, a Minor v. Alma Alexander, Alma Alexander",
          "cluster_id": 667160,
          "cite": [
            "20 F.3d 1350"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Joyce",
          "cluster_id": 7906322,
          "cite": [
            "30 Conn. App. 164",
            "619 A.2d 872",
            "1993 Conn. App. LEXIS 43"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Vincent Ezeiruaku",
          "cluster_id": 563242,
          "cite": [
            "936 F.2d 136",
            "1991 WL 105684"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McKeown",
          "cluster_id": 6047279,
          "cite": [
            "146 A.D.2d 716",
            "536 N.Y.S.2d 1018",
            "1989 N.Y. App. Div. LEXIS 611"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ingersoll v. Palmer",
          "cluster_id": 2604190,
          "cite": [
            "743 P.2d 1299",
            "43 Cal. 3d 1321",
            "241 Cal. Rptr. 42",
            "1987 Cal. LEXIS 451"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Webb v. State",
          "cluster_id": 2467075,
          "cite": [
            "739 S.W.2d 802",
            "1987 Tex. Crim. App. LEXIS 740"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane1_negative"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Delaware v. Prouse",
          "cluster_id": 110045,
          "cite": [
            "59 L. Ed. 2d 660",
            "99 S. Ct. 1391",
            "440 U.S. 648",
            "1979 U.S. LEXIS 80"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ross",
          "cluster_id": 110719,
          "cite": [
            "72 L. Ed. 2d 572",
            "102 S. Ct. 2157",
            "456 U.S. 798",
            "1982 U.S. LEXIS 18",
            "50 U.S.L.W. 4580"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brignoni-Ponce",
          "cluster_id": 109311,
          "cite": [
            "45 L. Ed. 2d 607",
            "95 S. Ct. 2574",
            "422 U.S. 873",
            "1975 U.S. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Opperman",
          "cluster_id": 109537,
          "cite": [
            "49 L. Ed. 2d 1000",
            "96 S. Ct. 3092",
            "428 U.S. 364",
            "1976 U.S. LEXIS 15"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Martinez-Fuerte",
          "cluster_id": 109541,
          "cite": [
            "49 L. Ed. 2d 1116",
            "96 S. Ct. 3074",
            "428 U.S. 543",
            "1976 U.S. LEXIS 87"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ybarra v. Illinois",
          "cluster_id": 110158,
          "cite": [
            "62 L. Ed. 2d 238",
            "100 S. Ct. 338",
            "444 U.S. 85",
            "1979 U.S. LEXIS 151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
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
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Immigration & Naturalization Service v. Delgado",
          "cluster_id": 111148,
          "cite": [
            "80 L. Ed. 2d 247",
            "104 S. Ct. 1758",
            "466 U.S. 210",
            "1984 U.S. LEXIS 57",
            "52 U.S.L.W. 4436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Bertine",
          "cluster_id": 111788,
          "cite": [
            "93 L. Ed. 2d 739",
            "107 S. Ct. 738",
            "479 U.S. 367",
            "1987 U.S. LEXIS 286",
            "55 U.S.L.W. 4105"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. DeFillippo",
          "cluster_id": 110127,
          "cite": [
            "61 L. Ed. 2d 343",
            "99 S. Ct. 2627",
            "443 U.S. 31",
            "1979 U.S. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arkansas v. Sanders",
          "cluster_id": 110119,
          "cite": [
            "61 L. Ed. 2d 235",
            "99 S. Ct. 2586",
            "442 U.S. 753",
            "1979 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marshall v. Barlow's, Inc.",
          "cluster_id": 109866,
          "cite": [
            "56 L. Ed. 2d 305",
            "98 S. Ct. 1816",
            "436 U.S. 307",
            "1978 U.S. LEXIS 26",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20434",
            "6 OSHC (BNA) 1571"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Santana",
          "cluster_id": 109504,
          "cite": [
            "49 L. Ed. 2d 300",
            "96 S. Ct. 2406",
            "427 U.S. 38",
            "1976 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Almeida-Sanchez v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108845 OR 9425395 OR 9425396 OR 9425397) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NDg2NDAwMDAwMDAmcz00ODI5MDAmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108845+OR+9425395+OR+9425396+OR+9425397%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 60,
        "triage_read": 5,
        "triage_snippet_classified": 55
      },
      "lane2_top_cited": {
        "query": "cites:(108845 OR 9425395 OR 9425396 OR 9425397)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MjMmcz0xMDkwMDUmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28108845+OR+9425395+OR+9425396+OR+9425397%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108845 OR 9425395 OR 9425396 OR 9425397)",
        "reviewed": 3,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 3,
        "triage_read": 0,
        "triage_snippet_classified": 3
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108845 OR 9425395 OR 9425396 OR 9425397)",
    "indexed_citing_opinions": 860,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108845,
        "count": 783,
        "count_source": "search"
      },
      {
        "opinion_id": 9425395,
        "count": 123,
        "count_source": "search"
      },
      {
        "opinion_id": 9425396,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9425397,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1282,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/almeida-sanchez-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2NzIzMzgmcz00NDU1MDAxJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108845+OR+9425395+OR+9425396+OR+9425397%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108845,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 92500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 93665,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 94236,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 95830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 96089,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 97062,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 102102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 102605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 108612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 229610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 241230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 247198,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 261509,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 267597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 278167,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 284848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 289951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 289998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 290134,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 291074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 291417,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 291520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 293899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 296293,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 297309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 300414,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 302071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 304092,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 304419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 306033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108845,
        "cited_id": 306459,
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
    "date_created": "2026-07-04T17:23:44Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T17:24:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T17:24:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:01:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T17:24:08Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Almeida-Sanchez v. United States

```
<div>
<center><b><span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U.S. 266</a></span> (1973)</b></center>
<center><h1>ALMEIDA-SANCHEZ<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 71-6278.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued March 19 and 28, 1973.</center>
<center>Decided June 21, 1973.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*267</span> <i>James A. Chanoux,</i> and <i>John J. Cleary</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./411/903/">411 U. S. 903</a></span>, argued the cause for petitioner. <i>Mr. Chanoux</i> was on the brief.</p>
<p><i>Deputy Solicitor General Lacovara</i> argued the cause for the United States. With him on the brief were <i>Solicitor General Griswold, Assistant Attorney General Petersen, Mark L. Evans, Beatrice Rosenberg,</i> and <i>Roger A. Pauley.</i><sup>[*]</sup></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioner in this case, a Mexican citizen holding a valid United States work permit, was convicted of having knowingly received, concealed, and facilitated the transportation of a large quantity of illegally imported marihuana in violation of 21 U. S. C. § 176a (1964 ed.). His sole contention on appeal was that the search of his automobile that uncovered the marihuana was unconstitutional under the Fourth Amendment and that, under the rule of <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, the marihuana should not have been admitted as evidence against him.</p>
<p>The basic facts in the case are neither complicated nor disputed. The petitioner was stopped by the United States Border Patrol on State Highway 78 in California, and his car was thoroughly searched. The road is essentially an east-west highway that runs for part of its course through an undeveloped region. At about the point where the petitioner was stopped the road meanders north as well as eastbut nowhere does the road reach the Mexican border, and at all points it lies north of U. S. 80, a major east-west highway entirely within the <span class="star-pagination">*268</span> United States that connects the Southwest with the west coast. The petitioner was some 25 air miles north of the border when he was stopped. It is undenied that the Border Patrol had no search warrant, and that there was no probable cause of any kind for the stop or the subsequent searchnot even the "reasonable suspicion" found sufficient for a street detention and weapons search in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, and <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span>.</p>
<p>The Border Patrol conducts three types of surveillance along inland roadways, all in the asserted interest of detecting the illegal importation of aliens. Permanent checkpoints are maintained at certain nodal intersections; temporary checkpoints are established from time to time at various places; and finally, there are roving patrols such as the one that stopped and searched the petitioner's car. In all of these operations, it is argued, the agents are acting within the Constitution when they stop and search automobiles without a warrant, without probable cause to believe the cars contain aliens, and even without probable cause to believe the cars have made a border crossing. The only asserted justification for this extravagant license to search is § 287 (a) (3) of the Immigration and Nationality Act, <span class="citation no-link">66 Stat. 233</span>, <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3), which simply provides for warrantless searches of automobiles and other conveyances "within a reasonable distance from any external boundary of the United States," as authorized by regulations to be promulgated by the Attorney General. The Attorney General's regulation, <span class="citation no-link">8 CFR § 287.1</span>, defines "reasonable distance" as "within 100 air miles from any external boundary of the United States."</p>
<p>The Court of Appeals for the Ninth Circuit recognized that the search of petitioner's automobile was not a "border search," but upheld its validity on the basis of <span class="star-pagination">*269</span> the above-mentioned portion of the Immigration and Nationality Act and the accompanying regulation. <span class="citation" data-id="9457622"><a href="/opinion/300414/united-states-v-condrado-almeida-sanchez/#461" aria-description="Citation for case: United States v. Condrado Almeida-Sanchez">452 F. 2d 459, 461</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./406/944/">406 U. S. 944</a></span>, to consider the constitutionality of the search.</p>
<p></p>
<h2>I</h2>
<p>No claim is made, nor could one be, that the search of the petitioner's car was constitutional under any previous decision of this Court involving the search of an automobile. It is settled, of course, that a stop and search of a moving automobile can be made without a warrant. That narrow exception to the warrant requirement was first established in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span>. The Court in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> approved a portion of the Volstead Act providing for warrantless searches of automobiles when there was probable cause to believe they contained illegal alcoholic beverages. The Court recognized that a moving automobile on the open road presents a situation "where it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States"><i>Id.,</i> at 153</a></span>. <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> has been followed in a line of subsequent cases,<sup>[1]</sup> but the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> doctrine does not declare a field day for the police in searching automobiles. Automobile or no automobile, there must be probable cause for the search.<sup>[2]</sup> As MR. JUSTICE WHITE wrote for the Court in <i>Chambers</i> v. <i>Maroney,</i> 399 <span class="star-pagination">*270</span> U. S. 42, 51: "In enforcing the Fourth Amendment's prohibition against unreasonable searches and seizures, the Court has insisted upon probable cause as a minimum requirement for a reasonable search permitted by the Constitution."</p>
<p>In seeking a rationale for the validity of the search in this case, the Government thus understandably sidesteps the automobile search cases. Instead, the Government relies heavily on cases dealing with administrative inspections. But these cases fail to support the constitutionality of this search.</p>
<p>In <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span>, the Court held that administrative inspections to enforce community health and welfare regulations could be made on less than probable cause to believe that particular dwellings were the sites of particular violations. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 534-536, 538</a></span>. Yet the Court insisted that the inspector obtain either consent or a warrant supported by particular physical and demographic characteristics of the areas to be searched. <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Ibid.</a></span></i> See also <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span>. The search in the present case was conducted in the unfettered discretion of the members of the Border Patrol, who did not have a warrant,<sup>[3]</sup> probable cause, or consent. The search thus embodied precisely the evil the Court saw in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> when it insisted that the "discretion of the official in the field" be circumscribed by obtaining a warrant prior to the inspection. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Camara, supra,</i> at 532-533</a></span>.</p>
<p>Two other administrative inspection cases relied upon by the Government are equally inapposite. <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span>, and <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span>, both approved <span class="star-pagination">*271</span> warrantless inspections of commercial enterprises engaged in businesses closely regulated and licensed by the Government. In <i>Colonnade,</i> the Court stressed the long history of federal regulation and taxation of the manufacture and sale of liquor, <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 76-77</a></span>. In <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>,</i> the Court noted the pervasive system of regulation and reporting imposed on licensed gun dealers, <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S., at 312</a></span> n. 1, 315-316.</p>
<p>A central difference between those cases and this one is that businessmen engaged in such federally licensed and regulated enterprises accept the burdens as well as the benefits of their trade, whereas the petitioner here was not engaged in any regulated or licensed business. The businessman in a regulated industry in effect consents to the restrictions placed upon him. As the Court stated in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>:</i></p>
<blockquote>"It is also plain that inspections for compliance with the Gun Control Act pose only limited threats to the dealer's justifiable expectations of privacy. When a dealer chooses to engage in this pervasively regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection. Each licensee is annually furnished with a revised compilation of ordinances that describe his obligations and define the inspector's authority. . . . The dealer is not left to wonder about the purposes of the inspector or the limits of his task." <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell"><i>Id.,</i> at 316</a></span>.</blockquote>
<p>Moreover, in <i>Colonnade</i> and <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>,</i> the searching officers knew with certainty that the premises searched were in fact utilized for the sale of liquor or guns. In the present case, by contrast, there was no such assurance that the individual searched was within the proper scope of official scrutinythat is, there was no reason <span class="star-pagination">*272</span> whatever to believe that he or his automobile had even crossed the border, much less that he was guilty of the commission of an offense.</p>
<p></p>
<h2>II</h2>
<p>Since neither this Court's automobile search decisions nor its administrative inspection decisions provide any support for the constitutionality of the stop and search in the present case, we are left simply with the statute that purports to authorize automobiles to be stopped and searched, without a warrant and "within a reasonable distance from any external boundary of the United States." It is clear, of course, that no Act of Congress can authorize a violation of the Constitution. But under familiar principles of constitutional adjudication, our duty is to construe the statute, if possible, in a manner consistent with the Fourth Amendment. <i>Ashwander</i> v. <i>Tennessee Valley Authority,</i> <span class="citation" data-id="9418878"><a href="/opinion/102605/ashwander-v-tennessee-valley-authority/#348" aria-description="Citation for case: Ashwander v. Tennessee Valley Authority">297 U. S. 288, 348</a></span> (Brandeis, J., concurring).</p>
<p>It is undoubtedly within the power of the Federal Government to exclude aliens from the country. <i>Chae Chan Ping</i> v. <i>United States,</i> <span class="citation" data-id="8140557"><a href="/opinion/8178642/chae-chan-ping-v-united-states/#603" aria-description="Citation for case: Chae Chan Ping v. United States">130 U. S. 581, 603-604</a></span>. It is also without doubt that this power can be effectuated by routine inspections and searches of individuals or conveyances seeking to cross our borders. As the Court stated in <i>Carroll</i> v. <i>United States</i><i>:</i> "Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S., at 154</a></span>. See also <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>.</p>
<p>Whatever the permissible scope of intrusiveness of a routine border search might be, searches of this kind may in certain circumstances take place not only at the border itself, but at its functional equivalents as well. For <span class="star-pagination">*273</span> example, searches at an established station near the border, at a point marking the confluence of two or more roads that extend from the border, might be functional equivalents of border searches. For another example, a search of the passengers and cargo of an airplane arriving at a St. Louis airport after a nonstop flight from Mexico City would clearly be the functional equivalent of a border search.<sup>[4]</sup></p>
<p>But the search of the petitioner's automobile by a roving patrol, on a California road that lies at all points at least 20 miles north of the Mexican border,<sup>[5]</sup> was of a wholly different sort. In the absence of probable cause or consent, that search violated the petitioner's Fourth Amendment right to be free of "unreasonable searches and seizures."</p>
<p>It is not enough to argue, as does the Government, that the problem of deterring unlawful entry by aliens across long expanses of national boundaries is a serious one. The needs of law enforcement stand in constant tension with the Constitution's protections of the individual against certain exercises of official power. It is precisely the predictability of these pressures that counsels a resolute loyalty to constitutional safeguards. It <span class="star-pagination">*274</span> is well to recall the words of Mr. Justice Jackson, soon after his return from the Nuremberg Trials:</p>
<blockquote>"These [Fourth Amendment rights], I protest, are not mere second-class rights but belong in the catalog of indispensable freedoms. Among deprivations of rights, none is so effective in cowing a population, crushing the spirit of the individual and putting terror in every heart. Uncontrolled search and seizure is one of the first and most effective weapons in the arsenal of every arbitrary government." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#180" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 180</a></span> (Jackson, J., dissenting).</blockquote>
<p>The Court that decided <i>Carroll</i> v. <i>United States, supra</i><i>,</i> sat during a period in our history when the Nation was confronted with a law enforcement problem of no small magnitudethe enforcement of the Prohibition laws. But that Court resisted the pressure of official expedience against the guarantee of the Fourth Amendment. Mr. Chief Justice Taft's opinion for the Court distinguished between searches at the border and in the interior, and clearly controls the case at bar:</p>
<blockquote>"It would be intolerable and unreasonable if a prohibition agent were authorized to stop every automobile on the chance of finding liquor and thus subject all persons lawfully using the highways to the inconvenience and indignity of such a search. Travellers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in. But those lawfully within the country, entitled to use the public highways, have a right to free passage without interruption or search unless there is <span class="star-pagination">*275</span> known to a competent official authorized to search, probable cause for believing that their vehicles are carrying contraband or illegal merchandise." <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S., at 153-154</a></span>.</blockquote>
<p>Accordingly, the judgment of the Court of Appeals is</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>While I join the opinion of the Court, which sufficiently establishes that none of our Fourth Amendment decisions supports the search conducted in this case, I add this concurring opinion to elaborate on my views as to the meaning of the Fourth Amendment in this context. We are confronted here with the all-too-familiar necessity of reconciling a legitimate need of government with constitutionally protected rights. There can be no question as to the seriousness and legitimacy of the law enforcement problem with respect to enforcing along thousands of miles of open border valid immigration and related laws. Nor can there be any question as to the necessity, in our free society, of safeguarding persons against searches and seizures proscribed by the Fourth Amendment. I believe that a resolution of the issue raised by this case is possible with due recognition of both of these interests, and in a manner compatible with the prior decisions of this Court.<sup>[1]</sup></p>
<p></p>
<h2>I</h2>
<p>The search here involved was carried out as part of a roving search of automobiles in an area generally proximate to the Mexican border. It was not a border search, <span class="star-pagination">*276</span> nor can it fairly be said to have been a search conducted at the "functional equivalent" of the border. Nor does this case involve the constitutional propriety of searches at permanent or temporary checkpoints removed from the border or its functional equivalent. Nor, finally, was the search based on cause in the ordinary sense of specific knowledge concerning an automobile or its passengers.<sup>[2]</sup> The question posed, rather, is whether and under what circumstances the Border Patrol may lawfully conduct roving searches of automobiles in areas not far removed from the border for the purpose of apprehending aliens illegally entering or in the country.</p>
<p>The Government has made a convincing showing that large numbers of aliens cross our borders illegally at places other than established crossing points, that they are often assisted by smugglers, that even those who cross on foot are met and transported to their destinations by automobiles, and that roving checks of automobiles are the only feasible means of apprehending them. It would, of course, be wholly impracticable to maintain a constant patrol along thousands of miles of border. Moreover, because many of these aliens cross the border on foot, or at places other than established checkpoints, it is simply not possible in most cases for the Government to obtain specific knowledge that a person riding or stowed in an automobile is an alien illegally in the country. <span class="star-pagination">*277</span> Thus the magnitude of the problem is clear. An answer, reconciling the obvious needs of law enforcement with relevant constitutional rights, is far less clear.</p>
<p></p>
<h2>II</h2>
<p>The Government's argument to sustain the search here is simply that it was reasonable under the circumstances. But it is by now axiomatic that the Fourth Amendment's proscription of "unreasonable searches and seizures" is to be read in conjunction with its command that "no Warrants shall issue, but upon probable cause." Under our cases, both the concept of probable cause and the requirement of a warrant bear on the reasonableness of a search, though in certain limited circumstances neither is required.</p>
<p>Before deciding whether a warrant is required, I will first address the threshold question of whether some functional equivalent of probable cause may exist for the type of search conducted in this case. The problem of ascertaining the meaning of the probable-cause requirement in the context of roving searches of the sort conducted here is measurably assisted by the Court's opinion in <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), on which the Government relies heavily. The Court was there concerned with the nature of the probable-cause requirement in the context of searches to identify housing code violations and was persuaded that the only workable method of enforcement was periodic inspection of all structures:</p>
<blockquote>"It is here that the probable cause debate is focused, for the agency's decision to conduct an area inspection is unavoidably based on its appraisal of conditions in the area as a whole, not on its knowledge of conditions in each particular building." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 536</a></span>.</blockquote>
<p><span class="star-pagination">*278</span> In concluding that such general knowledge met the probable-cause requirement under those circumstances, the Court took note of a "long history of judicial and public acceptance," of the absence of other methods for vindicating the public interest in preventing or abating dangerous conditions, and of the limited invasion of privacy occasioned by administrative inspections which are "neither personal in nature nor aimed at the discovery of evidence of crime." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#537" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Id.,</i> at 537</a></span>.</p>
<p>Roving automobile searches in border regions for aliens, likewise, have been consistently approved by the judiciary. While the question is one of first impression in this Court, such searches uniformly have been sustained by the courts of appeals whose jurisdictions include those areas of the border between Mexico and the United States where the problem has been most severe. See, <i>e. g., </i><i>United States</i> v. <i>Miranda,</i> <span class="citation" data-id="290134"><a href="/opinion/290134/united-states-v-luciano-abreu-miranda/" aria-description="Citation for case: United States v. Luciano Abreu Miranda">426 F. 2d 283</a></span> (CA9 1970); <i>Roa-Rodriquez</i> v. <i>United States,</i> <span class="citation" data-id="284848"><a href="/opinion/284848/carlos-roa-rodriquez-v-united-states/" aria-description="Citation for case: Carlos Roa-Rodriquez v. United States">410 F. 2d 1206</a></span> (CA10 1969). Moreover, as noted above, no alternative solution is reasonably possible.</p>
<p>The Government further argues that such searches resemble those conducted in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> in that they are undertaken primarily for administrative rather than prosecutorial purposes, that their function is simply to locate those who are illegally here and to deport them. Brief for the United States 28 n. 25. This argument is supported by the assertion that only 3% of aliens apprehended in this country are prosecuted. While the low rate of prosecution offers no great solace to the innocent whose automobiles are searched or to the few who are prosecuted, it does serve to differentiate this class of searches from random area searches which are no more than "fishing expeditions" for evidence to support prosecutions. The possibility of prosecution does not distinguish such searches from those involved in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>.</i> Despite the Court's assertion in that case that the searches <span class="star-pagination">*279</span> were not "aimed at the discovery of evidence of crime," 387 U. S., at 537, violators of the housing code there were subject to criminal penalties. <i>Id.,</i> at 527 n. 2.</p>
<p>Of perhaps greater weight is the fact that these searches, according to the Government, are conducted in areas where the concentration of illegally present aliens is high, both in absolute terms and in proportion to the number of persons legally present. While these searches are not border searches in the conventional sense, they are incidental to the protection of the border and draw a large measure of justification from the Government's extraordinary responsibilities and powers with respect to the border. Finally, and significantly, these are searches of automobiles rather than searches of persons or buildings. The search of an automobile is far less intrusive on the rights protected by the Fourth Amendment than the search of one's person or of a building. This Court "has long distinguished between an automobile and a home or office." <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#48" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 48</a></span> (1970). As the Government has demonstrated, and as those in the affected areas surely know, it is the automobile which in most cases makes effective the attempts to smuggle aliens into this country.</p>
<p>The conjunction of these factorsconsistent judicial approval, absence of a reasonable alternative for the solution of a serious problem, and only a modest intrusion on those whose automobiles are searchedpersuades me that under appropriate limiting circumstances there may exist a constitutionally adequate equivalent of probable cause to conduct roving vehicular searches in border areas.</p>
<p></p>
<h2>III</h2>
<p>The conclusion that there may be probable cause to conduct roving searches does not end the inquiry, for "except in certain carefully defined classes of cases, a search of private property without proper consent is <span class="star-pagination">*280</span> `unreasonable' unless it has been authorized by a valid search warrant." <i>Camara</i> v. <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>Municipal Court, supra,</i> at 528-529</a></span>. I expressed the view last Term that the warrant clause reflects an important policy determination: "The Fourth Amendment does not contemplate the executive officers of Government as neutral and disinterested magistrates. Their duty and responsibility is to enforce the laws, to investigate, and to prosecute. . . . But those charged with this investigative and prosecutorial duty should not be the sole judges of when to utilize constitutionally sensitive means in pursuing their tasks." <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972). See also <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#481" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 481</a></span> (1971); <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 763-764</a></span> (1969).</p>
<p>To justify warrantless searches in circumstances like those presented in this case, the Government relies upon several of this Court's decisions recognizing exceptions to the warrant requirement. A brief review of the nature of each of these major exceptions illuminates the relevant considerations in the present case. In <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court held that a policeman may conduct a limited "pat down" search for weapons when he has reasonable grounds for believing that criminal conduct has taken or is taking place and that the person he searches is armed and dangerous. "The sole justification [for such a] search . . . is the protection of the police officer and others nearby . . . ." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#29" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 29</a></span>. Nothing in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> supports an exception to the warrant requirement here.</p>
<p><i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), and <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972), on which the Government also relies, both concerned the standards which govern inspections of the business premises of those with federal licenses to engage in the sale of liquor, <i>Colonnade,</i> or the sale of guns, <span class="star-pagination">*281</span> <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>.</i> In those cases, Congress was held to have power to authorize warrantless searches. As the Court stated in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>:</i></p>
<blockquote>"When a dealer chooses to engage in this pervasively regulated business and to accept a federal license, he does so with the knowledge that his business records, firearms, and ammunition will be subject to effective inspection." <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#316" aria-description="Citation for case: United States v. Biswell">406 U. S., at 316</a></span>.</blockquote>
<p><i>Colonnade</i> and <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span></i> cannot fairly be read to cover cases of the present type. One who merely travels in regions near the borders of the country can hardly be thought to have submitted to inspections in exchange for a special perquisite.</p>
<p>More closely in point on their facts are the cases involving automobile searches. <i>E. g., </i><i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925); <i>Chambers</i> v. <i><span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">Maroney, supra</a></span></i><i>; </i><i>Coolidge</i> v. <i>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra</a></span></i><i>.</i> But while those cases allow automobiles to be searched without a warrant in certain circumstances, the principal rationale for this exception to the warrant clause is that under those circumstances "it is not practicable to secure a warrant because the vehicle can be quickly moved out of the locality or jurisdiction in which the warrant must be sought." <i>Carroll</i> v. <i>United States, supra,</i> at 153. The Court today correctly points out that a warrantless search under the <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> line of cases must be supported by probable cause in the sense of specific knowledge about a particular automobile. While, as indicated above, my view is that on appropriate facts the Government can satisfy the probable cause requirement for a roving search in a border area without possessing information about particular automobiles, it does not follow that the warrant requirement is inapposite. The very fact that the Government's supporting information relates to criminal activity in certain areas rather than <span class="star-pagination">*282</span> to evidence about a particular automobile renders irrelevant the justification for warrantless searches relied upon in <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll</a></span></i> and its progeny. Quite simply, the roving searches are justified by experience with obviously nonmobile sections of a particular road or area embracing several roads.</p>
<p>None of the foregoing exceptions to the warrant requirement, then, applies to roving automobile searches in border areas. Moreover, the propriety of the warrant procedure here is affirmatively established by <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>.</i> See also <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967). For the reasons outlined above, the Court there ruled that probable cause could be shown for an area search, but nonetheless required that a warrant be obtained for unconsented searches. The Court indicated its general approach to exceptions to the warrant requirement:</p>
<blockquote>"In assessing whether the public interest demands creation of a general exception to the Fourth Amendment's warrant requirement, the question is not whether the public interest justifies the type of search in question, but whether the authority to search should be evidenced by a warrant, which in turn depends in part upon whether the burden of obtaining a warrant is likely to frustrate the governmental purpose behind the search." <i>Camara</i> v. <i>Municipal Court, supra,</i> at 533.</blockquote>
<p>See also <i>United States</i> v. <i>United States District Court, supra,</i> at 315.</p>
<p>The Government argues that <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> and <i>See</i> are distinguishable from the present case for the purposes of the warrant requirement. It is true that while a building inspector who is refused admission to a building may easily obtain a warrant to search that building, a member of the Border Patrol has no such opportunity when <span class="star-pagination">*283</span> he is refused permission to inspect an automobile. It is also true that the judicial function envisioned in <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span></i> did not extend to reconsideration of "the basic agency decision to canvass an area," <i>Camara</i> v. <i>Municipal Court, supra,</i> at 532, while the judicial function here would necessarily include passing on just such a basic decision.</p>
<p>But it does not follow from these distinctions that "no warrant system can be constructed that would be feasible and meaningful." Brief for the United States 36. Nothing in the papers before us demonstrates that it would not be feasible for the Border Patrol to obtain advance judicial approval of the decision to conduct roving searches on a particular road or roads for a reasonable period of time.<sup>[3]</sup> According to the Government, the incidence of illegal transportation of aliens on certain roads is predictable, and the roving searches are apparently planned in advance or carried out according to a predetermined schedule. The use of an area warrant procedure would surely not "frustrate the governmental purpose behind the search." <i>Camara</i> v. <i>Municipal Court, supra,</i> at 533. It would of course entail some inconvenience, but inconvenience alone has never been thought to be an adequate reason for abrogating the warrant requirement. <i>E. g., </i><i>United States</i> v. <i>United States District Court, supra,</i> at 321.</p>
<p>Although standards for probable cause in the context of this case are relatively unstructured (cf. <i>id.,</i> at 322), there are a number of relevant factors which would merit consideration: they include (i) the frequency with which aliens illegally in the country are known or reasonably believed to be transported within a particular area; <span class="star-pagination">*284</span> (ii) the proximity of the area in question to the border; (iii) the extensiveness and geographic characteristics of the area, including the roads therein and the extent of their use,<sup>[4]</sup> and (iv) the probable degree of interference with the rights of innocent persons, taking into account the scope of the proposed search, its duration, and the concentration of illegal alien traffic in relation to the general traffic of the road or area.</p>
<p>In short, the determination of whether a warrant should be issued for an area search involves a balancing of the legitimate interests of law enforcement with protected Fourth Amendment rights. This presents the type of delicate question of constitutional judgment which ought to be resolved by the Judiciary rather than the Executive. In the words of <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Camara</a></span>,</i></p>
<blockquote>"This is precisely the discretion to invade private property which we have consistently circumscribed by a requirement that a disinterested party warrant the need to search." 387 U. S., at 532-533.</blockquote>
<p>Nor does the novelty of the problem posed by roving searches in border areas undermine the importance of a prior judicial determination. When faced with a similarly unconventional problem last Term in <i>United States District Court, supra,</i> we recognized that the focus of the search there involved was "less precise than that directed against more conventional types of crime," and that "[d]ifferent standards may be compatible with the Fourth Amendment if they are reasonable both in relation <span class="star-pagination">*285</span> to the legitimate need of Government . . . and the protected rights of our citizens." 407 U. S., at 322-323. Yet we refused to abandon the Fourth Amendment commitment to the use of search warrants whenever this is feasible with due regard to the interests affected.</p>
<p>For the reasons stated above, I think a rational search warrant procedure is feasible in cases of this kind. As no warrant was obtained here, I agree that the judgment must be reversed. I express no opinion as to whether there was probable cause to issue a warrant on the facts of this particular case.</p>
<p>MR. JUSTICE WHITE, with whom THE CHIEF JUSTICE, MR. JUSTICE BLACKMUN, and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>Trial and conviction in this case were in the United States District Court for the Southern District of California under an indictment charging that petitioner, contrary to 21 U. S. C. § 176a (1964 ed.), had knowingly received, concealed, and facilitated the transportation of approximately 161 pounds of illegally imported marihuana. He was sentenced to five years' imprisonment. He appealed on the sole ground that the District Court had erroneously denied his motion to suppress marihuana allegedly seized from his automobile in violation of the Fourth Amendment.</p>
<p>The motion to suppress was heard on stipulated evidence in the District Court.<sup>[1]</sup> United States Border Patrol Officers Shaw and Carrasco stopped petitioner's car shortly after midnight as it was traveling from Calexico, on the California-Mexico border, toward Blythe, California. <span class="star-pagination">*286</span> The stop was made on Highway 78 near Glamis, California, 50 miles by road from Calexico. The highway was "about the only north-south road in California coming from the Mexican border that does not have an established checkpoint."<sup>[2]</sup> Because of that, "it is commonly used to evade check points by both marijuana and alien smugglers." On occasions "but not at all times," officers of the Border Patrol "maintain a roving check of vehicles and persons on that particular highway." Pursuant to this practice "they stopped this vehicle for the specific purpose of checking for aliens." Petitioner's identification revealed that he was a resident of Mexicali, Mexico, but that he held a work permit for the United States. Petitioner had come from Mexicali, had picked up the car in Calexico and was on his way to Blythe to deliver it. He intended to return to Mexicali by bus.<sup>[3]</sup> The officers had been advised by an official bulletin that aliens illegally entering the United States sometimes concealed themselves by sitting upright behind the back seat rest of a car, with their legs folded under the back seat from which the springs had been removed. While looking under the rear seat of petitioner's car for aliens, the officers discovered packages believed by them to contain marihuana. Petitioner was placed under arrest and advised of his rights. His car was then searched for additional marihuana, which was found in substantial amounts.</p>
<p>On this evidence, the motion to suppress was denied, <span class="star-pagination">*287</span> and petitioner was convicted. A divided Court of Appeals affirmed, <span class="citation" data-id="9457622"><a href="/opinion/300414/united-states-v-condrado-almeida-sanchez/" aria-description="Citation for case: United States v. Condrado Almeida-Sanchez">452 F. 2d 459</a></span> (CA9 1971), relying on its prior cases and on § 287 (a) (3) of the Immigration and Nationality Act, <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3), which provides that officers of the Immigration and Naturalization Service shall have the power, without warrant, to search any vehicle for aliens within a reasonable distance from any external boundary of the United States.<sup>[4]</sup> I dissent from the reversal of this judgment.</p>
<p></p>
<h2>I</h2>
<p>The Fourth Amendment protects the people "in their persons, houses, papers, and effects, against unreasonable searches and seizures" and also provides that "no Warrants shall issue, but upon probable cause . . . ." The ordinary rule is that to be reasonable under the Amendment a search must be authorized by warrant issued by a magistrate upon a showing of probable cause. The <span class="star-pagination">*288</span> Amendment's overriding prohibition is nevertheless against "unreasonable" searches and seizures; and the legality of searching, without warrant and without probable cause, individuals and conveyances seeking to enter the country has been recognized by Congress and the courts since the very beginning. <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span> (1886), said as much; and in <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#154" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 154</a></span> (1925), the Court repeated that neither warrant nor probable cause was required to authorize a stop and search at the external boundaries of the United States: "Travelers may be so stopped in crossing an international boundary because of national self protection reasonably requiring one entering the country to identify himself as entitled to come in, and his belongings as effects which may be lawfully brought in." This much is undisputed in this case. Persons and their effects may be searched at the border for dutiable articles or contraband. Conveyances may be searched for the same purposes, as well as to determine whether they carry aliens not entitled to enter the country. Neither, apparently, is it disputed that warrantless searches for aliens without probable cause may be made at fixed checkpoints away from the border.</p>
<p>The problem in this case centers on the roving patrol operating away from, but near, the border. These patrols may search for aliens without a warrant if there is probable cause to believe that the vehicle searched is carrying aliens illegally into the country. But without probable cause, the majority holds the search unreasonable, although at least one Justice, MR. JUSTICE POWELL, would uphold searches by roving patrols if authorized by an area warrant issued on less than probable cause in the traditional sense. I agree with MR. JUSTICE POWELL that such a warrant so issued would satisfy the Fourth Amendment, and I would expect that such warrants would be readily issued. But I disagree with him <span class="star-pagination">*289</span> and the majority that either a warrant or probable cause is required in the circumstances of this case. As the Court has reaffirmed today in <i>Cady</i> v. <i>Dombrowski, post,</i> p. 433, the governing standard under the Fourth Amendment is reasonableness, and in my view, that standard is sufficiently flexible to authorize the search involved in this case.</p>
<p>In <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Court proceeding under the "general proscription against unreasonable searches and seizures," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>id.,</i> at 20</a></span> (footnote omitted), weighed the governmental interest claimed to justify the official intrusion against the constitutionally protected interest of the private citizen. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 20-21</a></span>. The "`need to search'" was balanced "`against the invasion which the search . . . entails,'" quoting from <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535, 536-537</a></span> (1967). <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio"><i>Terry, supra,</i> at 21</a></span>. In any event, as put by Mr. Chief Justice Warren, the "question is whether in all the circumstances of this on-the-street encounter, his right to personal security was violated by an <i>unreasonable</i> search and seizure." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#9" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 9</a></span> (emphasis added).</p>
<p>Warrantless but probable-cause searches of the person and immediate surroundings have been deemed reasonable when incident to arrest, see <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969); and in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> the stop of a suspected individual and a pat-down for weapons without a warrant were thought reasonable on less than traditional probable cause. In <i>Camara</i> v. <i>Municipal Court, supra</i><i>,</i> an inspection of every structure in an entire area to enforce the building codes was deemed reasonable under the Fourth Amendment without probable cause, or suspicion that any particular house or structure was in violation of law, although a warrant, issuable without probable cause, or reasonable suspicion of a violation, was required with respect to nonconsenting property owners. Also, in <i>Colonnade Catering Corp.</i> v. <i>United</i> <span class="star-pagination">*290</span> <i>States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), MR. JUSTICE DOUGLAS, writing for the Court and recognizing that the Fourth Amendment bars only unreasonable searches and seizures, ruled that the historic power of the Government to control the liquor traffic authorized warrantless inspections of licensed premises without probable cause, or reasonable suspicion, not to check on liquor quality or conditions under which it was sold, but solely to enforce the collection of, the federal excise tax.<sup>[5]</sup><i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972), involved the Gun Control Act of 1968 and its authorization to federal officers to inspect firearms dealers. The public need to enforce an important regulatory program was held to justify random inspections of licensed establishments without warrant and probable cause.</p>
<p>The Court has been particularly sensitive to the Amendment's broad standard of "reasonableness" where, as in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span></i> and <i>Colonnade,</i> authorizing statutes permitted the challenged searches. We noted in <i>Colonnade</i> that "Congress has broad power to design such powers of inspection under the liquor laws as it deems necessary <span class="star-pagination">*291</span> to meet the evils at hand," <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#76" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S., at 76</a></span>; and in <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span></i> we relied heavily upon the congressional judgment that the authorized inspection procedures played an important part in the regulatory system. <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/#315" aria-description="Citation for case: United States v. Biswell">406 U. S., at 315-317</a></span>. In the case before us, <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3), authorizes Border Patrol officers, without warrant, to search any vehicle <i>for aliens</i> "within a reasonable distance from any external boundary of the United States" and within the distance of 25 miles from such external boundary to have access to private lands, but not dwellings "for the purpose of patrolling the border to prevent the illegal entry of aliens into the United States . . . ." At the very least, this statute represents the considered judgment of Congress that proper enforcement of the immigration laws requires random searches of vehicles without warrant or probable cause within a reasonable distance of the international borders of the country.</p>
<p>It is true that "[u]ntil 1875 alien migration to the United States was unrestricted." <i>Kleindienst</i> v. <i>Mandel,</i> <span class="citation" data-id="9425024"><a href="/opinion/108612/kleindienst-v-mandel/#761" aria-description="Citation for case: Kleindienst v. Mandel">408 U. S. 753, 761</a></span> (1972). But the power of the National Government to exclude aliens from the country is undoubted and sweeping. "That the government of the United States, through the action of the legislative department, can exclude aliens from its territory is a proposition which we do not think open to controversy. Jurisdiction over its own territory to that extent is an incident of every independent nation. It is a part of its independence. If it could not exclude aliens, it would be to that extent subject to the control of another power." <i>Chae Chan Ping</i> v. <i>United States,</i> <span class="citation" data-id="8140557"><a href="/opinion/8178642/chae-chan-ping-v-united-states/#603" aria-description="Citation for case: Chae Chan Ping v. United States">130 U. S. 581, 603-604</a></span> (1889). "The power of Congress to exclude aliens altogether from the United States, or to prescribe the terms and conditions upon which they may come to this country, and to have its declared policy in that regard enforced exclusively . . . is settled by our previous adjudications." <span class="star-pagination">*292</span> <i>Lem Moon Sing</i> v. <i>United States,</i> <span class="citation" data-id="94236"><a href="/opinion/94236/lem-moon-sing-v-united-states/#547" aria-description="Citation for case: Lem Moon Sing v. United States">158 U. S. 538, 547</a></span> (1895). See also <i>Fong Yue Ting</i> v. <i>United States,</i> <span class="citation" data-id="9417622"><a href="/opinion/93665/fong-yue-ting-v-united-states/#711" aria-description="Citation for case: Fong Yue Ting v. United States">149 U. S. 698, 711</a></span> (1893); <i>Yamataya</i> v. <i>Fisher,</i> <span class="citation" data-id="95830"><a href="/opinion/95830/the-japanese-immigrant-case/#97" aria-description="Citation for case: The Japanese Immigrant Case">189 U. S. 86, 97-99</a></span> (1903); <i>United States ex rel. Turner</i> v. <i>Williams,</i> <span class="citation" data-id="9417945"><a href="/opinion/96089/united-states-ex-rel-turner-v-williams/#289" aria-description="Citation for case: United States Ex Rel. Turner v. Williams">194 U. S. 279, 289-290</a></span> (1904); <i>Oceanic Steam Navigation Co.</i> v. <i>Stranahan,</i> <span class="citation" data-id="97062"><a href="/opinion/97062/oceanic-steam-navigation-co-v-stranahan/#335" aria-description="Citation for case: Oceanic Steam Navigation Co. v. Stranahan">214 U. S. 320, 335-336</a></span> (1909); <i>United States ex rel. Volpe</i> v. <i>Smith,</i> <span class="citation" data-id="102102"><a href="/opinion/102102/united-states-ex-rel-volpe-v-smith/#425" aria-description="Citation for case: United States Ex Rel. Volpe v. Smith">289 U. S. 422, 425</a></span> (1933).</p>
<p>Since 1875, Congress has given "almost continuous attention . . . to the problems of immigration and of excludability of certain defined classes of aliens. The pattern generally has been one of increasing control. . . ." <i>Kleindienst</i> v. <span class="citation" data-id="9425024"><a href="/opinion/108612/kleindienst-v-mandel/#761" aria-description="Citation for case: Kleindienst v. Mandel"><i>Mandel, supra,</i> at 761-762</a></span>. It was only as the illegal entry of aliens multiplied that Congress addressed itself to enforcement mechanisms. In 1917, immigration authorities were authorized to board and search all conveyances by which aliens were being brought into the United States. Act of Feb. 5, 1917, § 16, <span class="citation no-link">39 Stat. 886</span>. This basic authority, substantially unchanged, is incorporated in <span class="citation no-link">8 U. S. C. § 1225</span> (a).</p>
<p>In 1946, it was represented to Congress that "[i]n the enforcement of the immigration laws it is at times desirable to stop and search vehicles within a reasonable distance from the boundaries of the United States and the legal right to do so should be conferred by law." H. R. Rep. No. 186, 79th Cong., 1st Sess., 2 (1945). The House Committee on Immigration and Naturalization was "of the opinion that the legislation is highly desirable," <i>ibid.,</i> and its counterpart in the Senate, S. Rep. No. 632, 79th Cong., 1st Sess., 2 (1945), stated that "[t] here is no question but that this is a step in the right direction." The result was express statutory authority, Act of Aug. 7, 1946, <span class="citation no-link">60 Stat. 865</span>, to conduct searches of vehicles for aliens within a reasonable distance from the border without warrant or possible cause. Moreover, in the Immigration and Nationality Act of 1952, 66 Stat. <span class="star-pagination">*293</span> 163, Congress permitted the entry onto private lands, excluding dwellings, within a distance of 25 miles from any external boundaries of the country "for the purpose of patrolling the border to prevent the illegal entry of aliens into the United States . . . ." § 287 (a) (3), <span class="citation no-link">66 Stat. 233</span>.</p>
<p>The judgment of Congress obviously was that there are circumstances in which it is reasonably necessary, in the enforcement of the immigration laws, to search vehicles and other private property for aliens, without warrant or probable cause, and at locations other than at the border. To disagree with this legislative judgment is to invalidate <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3) in the face of the contrary opinion of Congress that its legislation comported with the standard of reasonableness of the Fourth Amendment. This I am quite unwilling to do.</p>
<p>The external boundaries of the United States are extensive. The Canadian border is almost 4,000 miles in length; the Mexican, almost 2,000. Surveillance is maintained over the established channels and routes of communication. But not only is inspection at regular points of entry not infallible, but it is also physically impossible to maintain continuous patrol over vast stretches of our borders. The fact is that illegal crossings at other than the legal ports of entry are numerous and recurring. If there is to be any hope of intercepting illegal entrants and of maintaining any kind of credible deterrent, it is essential that permanent or temporary checkpoints be maintained away from the borders, and roving patrols be conducted to discover and intercept illegal entrants as they filter to the established roads and highways and attempt to move away from the border area. It is for this purpose that the Border Patrol maintained the roving patrol involved in this case and conducted random, spot checks of automobiles and other vehicular traffic.</p>
<p><span class="star-pagination">*294</span> The United States in this case reports that in fiscal year 1972, Border Patrol traffic checking operations located over 39,000 deportable aliens, of whom approximately 30,000 had entered the United States by illegally crossing the border at a place other than a port of entry. This was said to represent nearly 10% of the number of such aliens located by the Border Patrol by all means throughout the United States.<sup>[6]</sup></p>
<p>Section 1357 (a) (3) authorizes only searches for aliens and only searches of conveyances and other property. No searches of the person or for contraband are authorized by the section. The authority extended by the statute is limited to that reasonably necessary for the officer to assure himself that the vehicle or other conveyance is not carrying an alien who is illegally within this country; and more extensive searches of automobiles without probable cause are not permitted by the section. <i>Roa-Rodriquez</i> v. <i>United States,</i> <span class="citation" data-id="284848"><a href="/opinion/284848/carlos-roa-rodriquez-v-united-states/" aria-description="Citation for case: Carlos Roa-Rodriquez v. United States">410 F. 2d 1206</a></span> (CA10 1969); see <i>Fumagalli</i> v. <i>United States,</i> <span class="citation" data-id="291417"><a href="/opinion/291417/frank-thomas-fumagalli-v-united-states/#1013" aria-description="Citation for case: Frank Thomas Fumagalli v. United States">429 F. 2d 1011, 1013</a></span> (CA9 1970). Guided by the principles of <i>Camara, Colonnade,</i> and <i><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">Biswell</a></span>,</i> I cannot but uphold the judgment of Congress that for purposes of enforcing the immigration laws it is reasonable to treat the exterior boundaries of the country as a zone, not a line, and that there are recurring circumstances in which the search of vehicular traffic without warrant and without probable cause may be reasonable under the Fourth Amendment although not carried out at the border itself.</p>
<p><span class="star-pagination">*295</span> This has also been the considered judgment of the three Courts of Appeals whose daily concern is the enforcement of the immigration laws along the Mexican-American border, and who, although as sensitive to constitutional commands as we are, perhaps have a better vantage point than we here on the Potomac to judge the practicalities of border-area law enforcement and the reasonableness of official searches of vehicles to enforce the immigration statutes.</p>
<p>The Court of Appeals for the Ninth Circuit, like other circuits, recognizes that at the border itself, persons may be stopped, identified, and searched without warrant or probable cause and their effects and conveyances likewise subjected to inspection. There seems to be no dissent on this proposition. Away from the border, persons and automobiles may be searched for narcotics or other contraband only on probable cause; but under § 1357 (a) (3), automobiles may be stopped without warrant or probable cause and a limited search for aliens carried out in those portions of the conveyance capable of concealing any illegal immigrant. This has been the consistent view of that court.</p>
<p>In <i>Fumagalli</i> v. <i>United States, supra</i><i>,</i> Fumagalli was stopped at a checkpoint in Imperial, California, 49 miles north of the international boundary. In the course of looking in the trunk for an illegal entrant, the odor of marihuana was detected and marihuana discovered. Fumagalli contended that the trunk of the automobile could not be examined to locate an illegal entrant absent probable cause to believe that the vehicle carried such a person. The court, composed of Judges Merrill, Hufstedler, and Byrne, rejected the position, stating that "[w]hat all of these cases make clear is that probable cause is not required for an <i>immigration</i> search within approved limits [footnote omitted] but is generally required to sustain the legality of a search for <i>contraband</i> <span class="star-pagination">*296</span> in a person's automobile conducted away from the international borders. . . . Appellant has confused the two rules in his attempt to graft the probable cause standards of the <i>narcotics</i> cases . . . onto the rules justifying immigration inspections . . . ." <span class="citation" data-id="291417"><a href="/opinion/291417/frank-thomas-fumagalli-v-united-states/#1013" aria-description="Citation for case: Frank Thomas Fumagalli v. United States">429 F. 2d, at 1013</a></span>. Among prior cases reaffirmed was <i>Fernandez</i> v. <i>United States,</i> <span class="citation" data-id="261509"><a href="/opinion/261509/lazaro-fernandez-v-united-states/" aria-description="Citation for case: Lazaro Fernandez v. United States">321 F. 2d 283</a></span> (1963), where an automobile was stopped 18 miles north of Oceanside, California, on Highway 101 at a point 60 to 70 miles north of the Mexican border. An inspection for illegally entering aliens was conducted, narcotics were discovered and seized, and the stop and seizure were sustained under the statute. The Immigration Service, it was noted, had been running traffic checks in this area for 31 years, many illegal entrants had been discovered there, and there were at least a dozen other such checkpoints operating along the border between the United States and Mexico.<sup>[7]</sup></p>
<p>The Courts of Appeal for the Fifth and Tenth Circuits share the problem of enforcing the immigration laws along the Mexican-American border. Both courts agree with the Ninth Circuit that § 1357 (a) (3) is not void and that there are recurring circumstances where, as the statute permits, a stop of an automobile without warrant or probable cause and a search of it for aliens are constitutionally permissible.</p>
<p>In <i>United States</i> v. <i>De Leon,</i> <span class="citation" data-id="304092"><a href="/opinion/304092/united-states-v-oscar-pequeno-de-leon/" aria-description="Citation for case: United States v. Oscar Pequeno De Leon">462 F. 2d 170</a></span> (CA5 1972), De Leon was stopped without warrant or probable cause, <span class="star-pagination">*297</span> while driving on the highway leading north of Laredo, Texas, approximately 10 miles from the Mexican border. The purpose of the stop was to inspect for illegally entering aliens. De Leon opened the trunk as he was requested to do. A false bottom in the trunk and what was thought to be an odor of marihuana were immediately noticed and some heroin was seized. Judge Wisdom, writing for himself and Judges Godbold and Roney, concluded that:</p>
<blockquote>"Stopping the automobile ten miles from the Mexican border to search for illegal aliens was reasonable. <i>See</i> United States v. McDaniel, [<span class="citation" data-id="9458406"><a href="/opinion/304419/united-states-v-richard-mcdaniel/" aria-description="Citation for case: United States v. Richard McDaniel">463 F. 2d 129</a></span> (CA5 1972)]; United States v. Warner, 5 Cir. 1971, <span class="citation" data-id="9456812"><a href="/opinion/296293/united-states-v-craig-warner-april-covey-samuel-l-kranzthor-fred-w/" aria-description="Citation for case: United States v. Craig Warner, April Covey, Samuel L....">441 F. 2d 821</a></span>; Marsh v. United States, 5 Cir. 1965, <span class="citation" data-id="267597"><a href="/opinion/267597/kenneth-r-marsh-and-marion-w-martinez-v-united-states/" aria-description="Citation for case: Kenneth R. Marsh and Marion W. Martinez v. United States">344 F. 2d 317</a></span>, <span class="citation no-link">8 U. S. C. §§ 1225</span>, 1357; <span class="citation no-link">19 U. S. C. §§ 482</span>, 1581, <span class="citation no-link">8 C. F. R. § 287.1</span> [1973]; <span class="citation no-link">19 C. F. R. §§ 23.1</span> (d), 23.11 [1972]. Once the vehicle was reasonably stopped pursuant to an authorized border check the agents were empowered to search the vehicle, including the trunk, for aliens." <i>Id.,</i> at 171.</blockquote>
<p>Similarly, <i>United States</i> v. <i>McDaniel,</i> <span class="citation" data-id="9458406"><a href="/opinion/304419/united-states-v-richard-mcdaniel/" aria-description="Citation for case: United States v. Richard McDaniel">463 F. 2d 129</a></span> (CA5 1972), upheld a stop and an ensuing search for aliens that uncovered another crime. Judge Goldberg, with Judges Wisdom and Clark, was careful to point out, however, that the authority granted under the statute must still be exercised in a manner consistent with the standards of reasonableness of the Fourth Amendment. "Once the national frontier has been crossed, the search in question must be reasonable upon <i>all</i> of its facts, only one of which is the proximity of the search to an international border." <span class="citation" data-id="9458406"><a href="/opinion/304419/united-states-v-richard-mcdaniel/#133" aria-description="Citation for case: United States v. Richard McDaniel"><i>Id.,</i> at 133</a></span>. This view appears to have been the law in the Fifth Circuit for many years.<sup>[8]</sup></p>
<p><span class="star-pagination">*298</span> The Court of Appeals for the Tenth Circuit has expressed similar views. In <i><span class="citation" data-id="284848"><a href="/opinion/284848/carlos-roa-rodriquez-v-united-states/" aria-description="Citation for case: Carlos Roa-Rodriquez v. United States">Roa-Rodriquez, supra,</a></span></i> the automobile was stopped in New Mexico some distance from the Mexican border, the purpose being to search for aliens. Relying on the statute, the court, speaking through Judge Breitenstein, concluded that "[i]n the circumstances the initial stop and search for aliens were proper." <span class="citation" data-id="284848"><a href="/opinion/284848/carlos-roa-rodriquez-v-united-states/#1208" aria-description="Citation for case: Carlos Roa-Rodriquez v. United States"><i>Id.,</i> at 1208</a></span>. However, when it was determined by the officers that there were no occupants of the car illegally in the country, whether in the trunk or elsewhere, the court held that the officers had no business examining the contents of a jacket found in the trunk. The evidence in this case was excluded. The clear rule of the circuit, however, is that conveyances may be stopped and examined for aliens without warrant or probable cause when in all the circumstances it is reasonable to do so.<sup>[9]</sup></p>
<p>Congress itself has authorized vehicle searches at a reasonable distance from international frontiers in order to aid in the enforcement of the immigration laws. Congress has long considered such inspections constitutionally permissible under the Fourth Amendment. So, also, those courts and judges best positioned to make intelligent and sensible assessments of the requirements of reasonableness in the context of controlling illegal entries into this country have consistently and almost without dissent come to the same conclusion that is embodied in the judgment that is reversed today.<sup>[10]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*299</span> II</h2>
<p>I also think that § 1357 (a) (3) was validly applied in this case and that the search for aliens and the discovery of marihuana were not illegal under the Fourth Amendment. It was stipulated that the highway involved here was one of the few roads in California moving away from the Mexican border that did not have an established check station and that it is commonly used by alien smugglers to evade regular checkpoints. The automobile, when stopped sometime after midnight, was 50 miles along the road from the border town of Calexico, proceeding toward Blythe, California; but as a matter of fact it appears that the point at which the car was stopped was approximately only 20 miles due north of the Mexican border. Given the large number of illegal entries across the Mexican border at other than established ports of entry, as well as the likelihood that many illegally entering aliens cross on foot and meet prearranged transportation in this country, I think that under all the circumstances the stop of petitioner's car was reasonable, as was the search for aliens under the rear seat of the car pursuant to an official bulletin suggesting search procedures based on experience. Given a valid search of the car for aliens, it is in no way contended that the discovery and seizure of the marihuana were contrary to law.<sup>[11]</sup></p>
<p>I would affirm the judgment of the Court of Appeals.</p>
<h2>NOTES</h2>
<p>[*]  <i>Luke McKissack</i> filed a brief as <i>amicus curiae</i> urging reversal. <i>Arthur Wells, Jr.,</i> filed a brief for Gilbert Foerster as <i>amicus curiae.</i></p>
<p>[1]  <i>E. g., </i><i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span>; <i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216</a></span>; <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span>; <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span>.</p>
<p>[2]  Moreover, "[n]either <i><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">Carroll, supra,</a></span></i> nor other cases in this Court require or suggest that in every conceivable circumstance the search of an auto even with probable cause may be made without the extra protection for privacy that a warrant affords." <i>Chambers</i> v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#50" aria-description="Citation for case: Chambers v. Maroney"><i>Maroney, supra,</i> at 50</a></span>. See also <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#458" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 458-464</a></span>.</p>
<p>[3]  The Justices who join this opinion are divided upon the question of the constitutionality of area search warrants such as described in MR. JUSTICE POWELL'S concurring opinion.</p>
<p>[4]  With respect to aircraft, <span class="citation no-link">8 CFR § 281.1</span> defines "reasonable distance" as "any distance fixed pursuant to paragraph (b) of this section." Paragraph (b) authorizes the Commissioner of Immigration and Naturalization to approve searches at a greater distance than 100 air miles from a border "because of unusual circumstances."</p>
<p>[5]  The Government represents that the highway on which this search occurred is a common route for illegally entered aliens to travel, and that roving patrols apprehended 195 aliens on that road in one year. But it is, of course, quite possible that every one of those aliens was apprehended as a result of a valid search made upon probable cause. On the other hand, there is no telling how many perfectly innocent drivers have been stopped on this road without any probable cause, and been subjected to a search in the trunks, under the hoods, and behind the rear seats of their automobiles.</p>
<p>[1]  I am in accord with the Court's conclusion that nothing in § 287 (a) (3) of the Immigration and Nationality Act, <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3), or in <span class="citation no-link">8 CFR § 287.1</span> serves to authorize an otherwise unconstitutional search.</p>
<p>[2]  The Solicitor General's brief in this Court states explicitly that "We . . . do not take the position that the checking operations are justified because the officers have probable cause or even `reasonable suspicion' to believe, with respect to each vehicle checked, that it contains an illegal alien. Apart from the reasonableness of establishment of the checking operation in this case, there is nothing in the record to indicate that the Border Patrol officers had any special or particular reason to stop petitioner and examine his car." Brief for the United States 9-10.</p>
<p>[3]  There is no reason why a judicial officer could not approve where appropriate a series of roving searches over the course of several days or weeks. Experience with an initial search or series of searches would be highly relevant in considering applications for renewal of a warrant.</p>
<p>[4]  Depending upon the circumstances, there may be probable cause for the search to be authorized only for a designated portion of a particular road or such cause may exist for a designated area which may contain one or more roads or tracks. Particularly along much of the Mexican border, there are vast areas of uninhabited desert and arid land which are traversed by few, if any, main roads or highways, but which nevertheless may afford opportunitiesby virtue of their isolated characterfor the smuggling of aliens.</p>
<p>[1]  The facts, except for when petitioner was stopped, are taken from the oral stipulation in open court. See App. 11-14. The time petitioner was stopped is given by the Complaint as 12:15 a. m., App. 4, while petitioner testified at trial that he was "stopped about 1:00." 3 Tr. of Rec. 62.</p>
<p>[2]  West of Glamis the prevailing direction of the highway is east-west. At the point of the stop west of Glamis, the highway is only approximately 20 miles north of the border, running parallel to it. East of Glamis, the highway proceeds sharply northeast to Blythe, a distance of over 50 miles.</p>
<p>[3]  It appears, see App. 12, 13, that the officers were informed of these facts before initiating any search for aliens, and hence before finding any contraband.</p>
<p>[4]  Title <span class="citation no-link">8 U. S. C. § 1357</span> (a) provides in pertinent part:
</p>
<p>"Any officer or employee of the [Immigration and Naturalization] Service authorized under regulations prescribed by the Attorney General shall have power without warrant</p>
<p>. . . . .</p>
<p>"(3) within a reasonable distance from any external boundary of the United States, to board and search for aliens any vessel within the territorial waters of the United States and any railway car, aircraft, conveyance, or vehicle, and within a distance of twenty-five miles from any such external boundary to have access to private lands, but not dwellings, for the purpose of patrolling the border to prevent the illegal entry of aliens into the United States . . . ."</p>
<p>The Court of Appeals also relied on <span class="citation no-link">8 CFR § 287.1</span>, which in relevant part provides:</p>
<p>"(a) (2) <i>Reasonable distance.</i> The term `reasonable distance,' as used in section 287 (a) (3) of the Act, means within 100 air miles from any external boundary of the United States or any shorter distance which may be fixed by the district director, or, so far as the power to board and search aircraft is concerned, any distance fixed pursuant to paragraph (b) of this section."</p>
<p>[5]  In <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970), the conviction was set aside because it was thought that Congress, with all the authority it had to prescribe standards of reasonableness under the Fourth Amendment, had not intended federal inspectors to use force in carrying out warrantless, nonprobable-cause inspections. In dissent, THE CHIEF JUSTICE, joined by Justices Black and STEWART, would have sustained the search, saying: "I assume we could all agree that the search in question must be held valid, and the contraband discovered subject to seizure and forfeiture, unless (a) it is `unreasonable' under the Constitution or (b) it is prohibited by a statute imposing restraints apart from those in the Constitution. The majority sees no constitutional violation; I agree." <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#78" aria-description="Citation for case: Colonnade Catering Corp. v. United States"><i>Id.,</i> at 78</a></span>.
</p>
<p>In a separate dissent Mr. Justice Black, joined by THE CHIEF JUSTICE and MR. JUSTICE STEWART, also emphasized that the ultimate test of legality under the Fourth Amendment was whether the search and seizure were reasonable. <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/#79" aria-description="Citation for case: Colonnade Catering Corp. v. United States"><i>Id.,</i> at 79-81</a></span>.</p>
<p>[6]  In fiscal year 1972, 398,000 aliens who had entered the United States without inspection were located by Immigration and Naturalization officers; and of the 39,243 deportable aliens located through traffic checking operations, about one-third, 11,586, had been assisted by smugglers. In fiscal year 1972, 2,880 such smugglers were discovered through traffic checking operations. Ninety-nine percent of all aliens illegally entering the United States by land crossed our border with Mexico.</p>
<p>[7]  In the Court of Appeals for the Ninth Circuit, <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3) has also been sustained in, <i>e. g., </i><i>Mienke</i> v. <i>United States,</i> <span class="citation" data-id="9457657"><a href="/opinion/300565/gus-f-mienke-jr-v-united-states/" aria-description="Citation for case: Gus F. Mienke, Jr. v. United States">452 F. 2d 1076</a></span> (1971); <i>United States</i> v. <i>Marin,</i> <span class="citation" data-id="297309"><a href="/opinion/297309/united-states-v-ken-robert-marin-united-states-of-america-v-manuel-eloy/" aria-description="Citation for case: United States v. Ken Robert Marin, United States of...">444 F. 2d 86</a></span> (1971); <i>Duprez</i> v. <i>United States,</i> <span class="citation" data-id="293899"><a href="/opinion/293899/gene-duprez-v-united-states/" aria-description="Citation for case: Gene Duprez v. United States">435 F. 2d 1276</a></span> (1970); <i>United States</i> v. <i>Sanchez-Mata,</i> <span class="citation" data-id="291520"><a href="/opinion/291520/united-states-v-brigido-sanchez-mata/" aria-description="Citation for case: United States v. Brigido Sanchez-Mata">429 F. 2d 1391</a></span> (1970); <i>United States</i> v. <i>Avey,</i> <span class="citation" data-id="291074"><a href="/opinion/291074/united-states-v-arthur-joseph-avey-and-larry-richard-dean/" aria-description="Citation for case: United States v. Arthur Joseph Avey, and Larry Richard Dean">428 F. 2d 1159</a></span> (1970); <i>United States</i> v. <i>Miranda,</i> <span class="citation" data-id="290134"><a href="/opinion/290134/united-states-v-luciano-abreu-miranda/" aria-description="Citation for case: United States v. Luciano Abreu Miranda">426 F. 2d 283</a></span> (1970); and <i>United States</i> v. <i>Elder,</i> <span class="citation" data-id="289951"><a href="/opinion/289951/united-states-v-ronald-lee-elder-united-states-of-america-v-ernest/" aria-description="Citation for case: United States v. Ronald Lee Elder, United States of...">425 F. 2d 1002</a></span> (1970). See also <i>Valenzuela-Garcia</i> v. <i>United States,</i> <span class="citation" data-id="289998"><a href="/opinion/289998/manuel-valenzuela-garcia-v-united-states/" aria-description="Citation for case: Manuel Valenzuela-Garcia v. United States">425 F. 2d 1170</a></span> (1970), and <i>Barba-Reyes</i> v. <i>United States,</i> <span class="citation" data-id="278167"><a href="/opinion/278167/regino-barba-reyes-v-united-states/" aria-description="Citation for case: Regino Barba-Reyes v. United States">387 F. 2d 91</a></span> (1967).</p>
<p>[8]  <i>E. g., </i><i>Kelly</i> v. <i>United States,</i> <span class="citation" data-id="229610"><a href="/opinion/229610/kelly-v-united-states/" aria-description="Citation for case: Kelly v. United States">197 F. 2d 162</a></span> (1952). See also <i>United States</i> v. <i>Bird,</i> <span class="citation" data-id="302071"><a href="/opinion/302071/united-states-v-george-curtis-bird/#1024" aria-description="Citation for case: United States v. George Curtis Bird">456 F. 2d 1023, 1024</a></span> (1972); <i>Ramirez</i> v. <i>United States,</i> <span class="citation" data-id="247198"><a href="/opinion/247198/sergio-ruvalcaba-ramirez-v-united-states/#387" aria-description="Citation for case: Sergio Ruvalcaba Ramirez v. United States">263 F. 2d 385, 387</a></span> (1959); and <i>Haerr</i> v. <i>United States,</i> <span class="citation" data-id="241230"><a href="/opinion/241230/charles-spencer-haerr-v-united-states/#535" aria-description="Citation for case: Charles Spencer Haerr v. United States">240 F. 2d 533, 535</a></span> (1957).</p>
<p>[9]  <i>E. g., </i><i>United States</i> v. <i>Anderson.</i> <span class="citation" data-id="306459"><a href="/opinion/306459/united-states-v-philip-karsten-anderson/" aria-description="Citation for case: United States v. Philip Karsten Anderson">468 F. 2d 1280</a></span> (1972); and <i>United States</i> v. <i>McCormick,</i> <span class="citation" data-id="306033"><a href="/opinion/306033/united-states-v-michael-stephen-mccormick/" aria-description="Citation for case: United States v. Michael Stephen McCormick">468 F. 2d 68</a></span> (1972).</p>
<p>[10]  Without having undertaken an exhaustive survey, in the 20 court of appeals cases I have noted, including the one before us, 35 different judges of the three Courts of Appeals found inspection of vehicles for illegal aliens without warrant or probable cause to be constitutional. Only one judge has expressed a different view.</p>
<p>[11]  The United States does not contend, see Tr. of Oral Arg. 29, and I do not suggest that any search of a vehicle for aliens within 100 miles of the border pursuant to <span class="citation no-link">8 CFR § 287.1</span> would pass constitutional muster. The possible invalidity of the regulation and of <span class="citation no-link">8 U. S. C. § 1357</span> (a) (3) in other circumstances is not at issue here.</p>

</div>
```

---
