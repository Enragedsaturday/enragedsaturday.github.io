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

## GROUP: _overhaul2/lake/cases/Warden v. Hayden.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Warden v. Hayden"
type: case
citation: "387 U.S. 294 (1967)"
parallel_cite: "87 S. Ct. 1642; 18 L. Ed. 2d 782"
neutral_cite: 1967 U.S. LEXIS 2753
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-05-29
docket: 480
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-05-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Warden v. Hayden
  varies_by_point: false
  scope_note: "Foundational hot-pursuit case; also abolished the 'mere evidence' rule of Gouled v. United States. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107465/warden-maryland-penitentiary-v-hayden/"
  cluster_id: 107465
  opinion_id: 9423434
  identity_checked: true
homes:
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Key — Anchor"
related: ["[[United States v. Santana]]", "[[Kentucky v. King]]", "[[Welsh v. Wisconsin]]"]
aliases: ["Warden, Maryland Penitentiary v. Hayden", "Hayden"]
tags: ["case", "fourth-amendment", "exigent-circumstances", "hot-pursuit", "warrantless-entry"]
holding: "Hot pursuit of a fleeing armed robber into a house is a valid warrantless entry and search where \"the exigencies of the situation made…"
lake:
  record_id: Warden v. Hayden
  status: verified
  projected_at: 2026-07-06
---

# Warden v. Hayden

*387 U.S. 294 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An armed robber held up a taxi company and fled. Two cab drivers followed him and radioed his description and the address of the house he entered. Police arrived within minutes, were told an armed suspect had just gone in, and entered without a warrant. Searching the house for the robber and his weapons, they found Hayden feigning sleep in an upstairs bedroom, a shotgun and pistol in a flush tank, ammunition, and clothing matching the robber's description in a washing machine. All were used to convict him.

## Issue
Whether the warrantless entry into and search of a house, in immediate pursuit of an armed robber reported to have entered moments earlier, was reasonable under the Fourth Amendment.

## Rule
[[Exigent Circumstances and Hot Pursuit|Hot pursuit]] of a fleeing armed suspect into a dwelling is a valid warrantless entry and search where the [[Exigent Circumstances and Hot Pursuit|exigencies]] make it imperative: "neither the entry without warrant to search for the robber, nor the search for him without warrant was invalid. Under the circumstances of this case, 'the exigencies of the situation made that course imperative.'" — 387 U.S. at 298. ^pin-298

The scope follows the emergency: "The Fourth Amendment does not require police officers to delay in the course of an investigation if to do so would gravely endanger their lives or the lives of others." — *Id.* at 298–299. ^pin-299

## Application
On these facts the police acted within minutes of an armed robbery on information that the armed suspect had just entered the house. Speed was essential: only a prompt, thorough search for persons and weapons could ensure that Hayden was the only man present and that officers controlled any weapons that could be used against them or to effect an escape. The warrantless entry and the search for the robber and his weapons were therefore reasonable, and the items found in the course of that search were admissible.

## Conclusion
The warrantless entry and search in [[Exigent Circumstances and Hot Pursuit|hot pursuit]] were reasonable; the seizure of the weapons and clothing was valid. The Court also rejected the "mere evidence" limitation, holding that evidentiary items (not just contraband, fruits, or instrumentalities) may be seized.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hayden* anchors the hot-pursuit branch of the [[Exigent Circumstances and Hot Pursuit|exigency]] doctrine, applied to a suspect fleeing into her own home in [[United States v. Santana]] and framed within the [[Exigent Circumstances and Hot Pursuit|exigency]] framework reaffirmed in [[Kentucky v. King]]; the gravity-of-offense limit on home-entry [[Exigent Circumstances and Hot Pursuit|exigencies]] is drawn in [[Welsh v. Wisconsin]]. Its separate holding abolishing the "mere evidence" rule remains good law.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Anchor*

## Sources
- *Warden v. Hayden*, 387 U.S. 294 (1967) — https://www.courtlistener.com/opinion/107465/warden-maryland-penitentiary-v-hayden/ — pinpoints: 298, 298–299.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "4cf9f3b8858be3eb", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Warden v. Hayden"}, "payload": {"all": [{"cite": "387 U.S. 294", "page": "294", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "387"}, {"cite": "87 S. Ct. 1642", "page": "1642", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "18 L. Ed. 2d 782", "page": "782", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "18"}, {"cite": "1967 U.S. LEXIS 2753", "page": "2753", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "387 U.S. 294", "official": {"cite": "387 U.S. 294", "page": "294", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "387"}, "official_selection_present": true, "record_id": "Warden v. Hayden"}}
{"assertion_id": "13f1c2f9bbac8359", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-299", "record_id": "Warden v. Hayden"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-299", "pinpoint_status": "slip-only", "quote": "The Fourth Amendment does not require police officers to delay in the course of an investigation if to do so would gravely endanger their lives or the lives of others.", "quote_fidelity": "mismatch", "record_id": "Warden v. Hayden", "star_marker": null}}
{"assertion_id": "721ad54bb36f0836", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-298", "record_id": "Warden v. Hayden"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-298", "pinpoint_status": "slip-only", "quote": "--- # Warden v. Hayden *387 U.S. 294 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An armed robber held up a taxi company and fled. Two cab drivers followed him and radioed his description and the address of the house he entered. Police arrived within minutes, were told an armed suspect had just gone in, and entered without a warrant. Searching the house for the robber and his weapons, they found Hayden feigning sleep in an upstairs bedroom, a shotgun and pistol in a flush tank, ammunition, and clothing matching the robber's description in a washing machine. All were used to convict him. ## Issue Whether the warrantless entry into and search of a house, in immediate pursuit of an armed robber reported to have entered moments earlier, was reasonable under the Fourth Amendment. ## Rule Hot pursuit of a fleeing armed suspect into a dwelling is a valid warrantless entry and search where the exigencies make it imperative:", "quote_fidelity": "mismatch", "record_id": "Warden v. Hayden", "star_marker": null}}
{"assertion_id": "1970a5d348ed98f1", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Warden v. Hayden"}, "payload": {"as_of_content": "1967-05-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Warden v. Hayden", "scope_note": "Foundational hot-pursuit case; also abolished the 'mere evidence' rule of Gouled v. United States. Good law.", "varies_by_point": false}}
```

### lake record — Warden v. Hayden

```json
{
  "schema_version": "s2.v1",
  "record_id": "Warden v. Hayden",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Warden, Maryland Penitentiary v. Hayden",
    "case_name_short": "Hayden",
    "case_name_full": "Warden, Maryland Penitentiary v. Hayden",
    "input_case_name": "Warden v. Hayden",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-05-29",
    "year": 1967,
    "docket": "480",
    "cluster_id": 107465,
    "lead_opinion_id": 9423434,
    "sibling_ids": [
      107465,
      9423434,
      9423435,
      9423436
    ],
    "absolute_url": "/opinion/107465/warden-maryland-penitentiary-v-hayden/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "387 U.S. 294",
      "volume": "387",
      "reporter": "U.S.",
      "page": "294",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 1642",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 782",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2753",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2753",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "387 U.S. 294",
        "volume": "387",
        "reporter": "U.S.",
        "page": "294",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 1642",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "1642",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "18 L. Ed. 2d 782",
        "volume": "18",
        "reporter": "L. Ed. 2d",
        "page": "782",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2753",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2753",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "387 U.S. 294",
    "official_selection": {
      "court_class": "scotus",
      "selected": "387 U.S. 294",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-298",
      "page": null,
      "quote": "--- # Warden v. Hayden *387 U.S. 294 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An armed robber held up a taxi company and fled. Two cab drivers followed him and radioed his description and the address of the house he entered. Police arrived within minutes, were told an armed suspect had just gone in, and entered without a warrant. Searching the house for the robber and his weapons, they found Hayden feigning sleep in an upstairs bedroom, a shotgun and pistol in a flush tank, ammunition, and clothing matching the robber's description in a washing machine. All were used to convict him. ## Issue Whether the warrantless entry into and search of a house, in immediate pursuit of an armed robber reported to have entered moments earlier, was reasonable under the Fourth Amendment. ## Rule Hot pursuit of a fleeing armed suspect into a dwelling is a valid warrantless entry and search where the exigencies make it imperative:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-299",
      "page": null,
      "quote": "The Fourth Amendment does not require police officers to delay in the course of an investigation if to do so would gravely endanger their lives or the lives of others.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-05-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Warden v. Hayden",
    "varies_by_point": false,
    "scope_note": "Foundational hot-pursuit case; also abolished the 'mere evidence' rule of Gouled v. United States. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Andrew Lennette, Individually and on behalf of C.L., O.L. and S.L., Minor Children v. State of Iowa, Melody Siver, Amy Howell, and Valerie Lovaglia",
          "cluster_id": 6476611,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Perkins",
          "cluster_id": 4433002,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Joseph Michael Moultrie",
          "cluster_id": 4405157,
          "cite": [
            "224 So. 3d 349",
            "2017 La. LEXIS 1382",
            "2017 WL 2836066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Amended July 5, 2017 State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4471947,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Maurice D. Angel and Kemia B. McDowell",
          "cluster_id": 4384931,
          "cite": [
            "893 N.W.2d 904",
            "2017 WL 1422692",
            "2017 Iowa Sup. LEXIS 41"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ricky Johnson v. State of Indiana",
          "cluster_id": 4371565,
          "cite": [
            "70 N.E.3d 890",
            "2017 WL 765897",
            "2017 Ind. App. LEXIS 88"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Shamel L. Alexander",
          "cluster_id": 3177044,
          "cite": [
            "2016 VT 19",
            "201 Vt. 329",
            "139 A.3d 574",
            "2016 Vt. LEXIS 19",
            "2016 WL 555794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "City and County of San Francisco v. Sheehan",
          "cluster_id": 2801435,
          "cite": [
            "575 U.S. 600",
            "135 S. Ct. 1765",
            "191 L. Ed. 2d 856",
            "2015 U.S. LEXIS 3200",
            "83 U.S.L.W. 4303",
            "25 Fla. L. Weekly Fed. S 254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Leotis B. Branigh, III",
          "cluster_id": 1034108,
          "cite": [
            "155 Idaho 404",
            "313 P.3d 732",
            "2013 WL 3718751",
            "2013 Ida. App. LEXIS 63"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane1_negative"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Royer",
          "cluster_id": 110890,
          "cite": [
            "75 L. Ed. 2d 229",
            "103 S. Ct. 1319",
            "460 U.S. 491",
            "1983 U.S. LEXIS 151",
            "51 U.S.L.W. 4293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Sykes",
          "cluster_id": 109717,
          "cite": [
            "53 L. Ed. 2d 594",
            "97 S. Ct. 2497",
            "433 U.S. 72",
            "1977 U.S. LEXIS 135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mincey v. Arizona",
          "cluster_id": 109905,
          "cite": [
            "57 L. Ed. 2d 290",
            "98 S. Ct. 2408",
            "437 U.S. 385",
            "1978 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gilbert v. California",
          "cluster_id": 107487,
          "cite": [
            "18 L. Ed. 2d 1178",
            "87 S. Ct. 1951",
            "388 U.S. 263",
            "1967 U.S. LEXIS 1086"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Belton",
          "cluster_id": 110559,
          "cite": [
            "69 L. Ed. 2d 768",
            "101 S. Ct. 2860",
            "453 U.S. 454",
            "1981 U.S. LEXIS 13"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
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
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Horton v. California",
          "cluster_id": 112448,
          "cite": [
            "110 L. Ed. 2d 112",
            "110 S. Ct. 2301",
            "496 U.S. 128",
            "1990 U.S. LEXIS 2937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Rodriguez",
          "cluster_id": 112475,
          "cite": [
            "111 L. Ed. 2d 148",
            "110 S. Ct. 2793",
            "497 U.S. 177",
            "1990 U.S. LEXIS 3295",
            "58 U.S.L.W. 4892"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Warden v. Hayden:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQwMzU4NDAwMDAwJnM9Mjg4MDMwOSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107465+OR+9423434+OR+9423435+OR+9423436%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 14,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 14,
        "triage_snippet_classified": 186
      },
      "lane2_top_cited": {
        "query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzg0JnM9MTA5NTA0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107465+OR+9423434+OR+9423435+OR+9423436%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436)",
        "reviewed": 16,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 16,
        "triage_read": 0,
        "triage_snippet_classified": 16
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107465 OR 9423434 OR 9423435 OR 9423436)",
    "indexed_citing_opinions": 2140,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107465,
        "count": 1965,
        "count_source": "search"
      },
      {
        "opinion_id": 9423434,
        "count": 239,
        "count_source": "search"
      },
      {
        "opinion_id": 9423435,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423436,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3217,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/warden-v-hayden.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxNjA2NTkmcz05MzgwNzA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107465+OR+9423434+OR+9423435+OR+9423436%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107465,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 106962,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 107102,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 268073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1421285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1476321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1481331,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107465,
        "cited_id": 1990408,
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
    "date_created": "2026-07-06T04:05:02Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:05:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:05:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:08:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:05:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Warden v. Hayden

```
<opinion type="majority">
<author id="b339-13">Mr. Justice Brennan</author>
<p id="AdV">delivered the opinion of the Court.</p>
<p id="b339-14">We review in this case the validity of the proposition that there is under the Fourth Amendment a “distinction <page-number citation-index="1" label="296">*296</page-number>between merely evidentiary materials, on the one hand, which may not be seized either under the authority of a search warrant or during the course of a search incident to arrest, and on the other hand, those objects which may validly be seized including the instrumentalities and means by which a crime is committed, the fruits of crime such as stolen property, weapons by which escape of the person arrested might be effected, and property the possession of which is a crime.” <footnotemark>1</footnotemark></p>
<p id="b340-6">A Maryland court sitting without a jury convicted respondent of armed robbery. Items of his clothing, a cap, jacket,- and trousers, among other things, were seized during a search of his home, and were admitted in evidence without objection. After unsuccessful state court proceedings, he sought and was denied federal habeas corpus relief in the District Court for Maryland.<footnotemark>2</footnotemark> A divided panel of the Court of Appeals for the Fourth Circuit reversed. <span class="citation" data-id="9451981"><a href="/opinion/272530/bennie-joe-hayden-v-warden-maryland-penitentiary/" aria-description="Citation for case: Bennie Joe Hayden v. Warden, Maryland Penitentiary">363 F. 2d 647</a></span>. The Court of Appeals believed that <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 154</a></span>, sustained the validity of the search, but held that respondent was correct in his contention that the clothing seized was improperly admitted in evidence because the items had “evidential value only” and therefore were not <page-number citation-index="1" label="297">*297</page-number>lawfully subject to seizure. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./385/926/">385 U. S. 926</a></span>. We reverse.<footnotemark>3</footnotemark></p>
<p id="b341-5">I.</p>
<p id="b341-6">About 8 a. m. on March 17, 1962, an armed robber entered the business premises of the Diamond Cab Company in Baltimore, Maryland. He took some $363 and ran. Two cab drivers in the vicinity, attracted by shouts of “Holdup,” followed the man to 2111 Cocoa Lane. One driver notified the company dispatcher by radio that the man was a Negro about 5'8" tall, wearing a light cap and dark jacket, and that he had entered the house on Cocoa Lane. The dispatcher relayed the information to police who were proceeding to the scene of the robbery. Within minutes, police arrived at the house in a number of patrol cars. An officer knocked and announced their presence. Mrs. Hayden answered, and the officers told her they believed that a robber had entered the house, and asked to search the house. She offered no objection.<footnotemark>4</footnotemark></p>
<p id="b342-5"><page-number citation-index="1" label="298">*298</page-number>The officers spread out through the first and second floors and the cellar in search of the robber. Hayden was found in an upstairs bedroom feigning sleep. He was arrested when the officers on the first floor and in the cellar reported that no other man was in the house. Meanwhile an officer was attracted to an adjoining bathroom by the noise of running water, and discovered a shotgun and a pistol in a flush tank; another officer who, according to the District Court, “was searching the cellar for a man or the money” found in a washing machine a jacket and trousers of the type the fleeing man was said to have worn. A clip of ammunition for the pistol and a cap were found under the mattress of Hayden’s bed, and ammunition for the shotgun was found in a bureau drawer in Hayden’s room. All these items of evidence were introduced against respondent at his trial.</p>
<p id="b342-6">II.</p>
<p id="b342-7">We agree with the Court of Appeals that neither the entry without warrant to search for the robber, nor the search for him without warrant was invalid. Under the circumstances of this case, “the exigencies of the situation made that course imperative.” <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span>. The police were informed that an armed robbery had taken place, and that the suspect had entered 2111 Cocoa Lane less than five minutes before they reached it. They acted reasonably when they entered the house and began to search for a man of the description they had been given and for weapons which he had used in the robbery or might use against them. The Fourth Amendment does not require police officers to delay in the course of an investigation <page-number citation-index="1" label="299">*299</page-number>if to do so would gravely endanger their lives or the lives of others. Speed here was essential, and only a thorough search of the house for persons and weapons could have insured that Hayden was the only man present and that the police had control of all weapons which could be used against them or to effect an escape.</p>
<p id="b343-5">We do not rely upon <em>Harris </em>v. <em>United States, supra, </em>in sustaining the validity of the search. The principal issue in <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>was whether the search there could properly be regarded as incident to the lawful arrest, since Harris was in custody before the search was made and the evidence seized. Here, the seizures occurred prior to or immediately contemporaneous with Hayden’s arrest, as part of an effort to find a suspected felon, armed, within the house into which he had run only minutes before the police arrived. The permissible scope of search must, therefore, at the least, be as broad as may reasonably be necessary to prevent the dangers that the suspect at large in the house may resist or escape.</p>
<p id="b343-6">It is argued that, while the weapons, ammunition, and cap may have been seized in the course of a search for weapons, the officer who seized the clothing was searching neither for the suspect nor for weapons when he looked into the washing machine in which he found the clothing. But even if we assume, although we do not decide, that the exigent circumstances in this case made lawful a search without warrant only for the suspect or his weapons, it cannot be said on this record that the officer who found the clothes in the washing machine was not searching for weapons. He testified that he was searching for the man or the money, but his failure to state explicitly that he was searching for weapons, in the absence of a specific question to that effect, can hardly be accorded controlling weight. He knew that the robber was armed and he did not know that some <page-number citation-index="1" label="300">*300</page-number>weapons had been found at the time he opened the machine.<footnotemark>5</footnotemark> In these circumstances the inference that he was in fact also looking for weapons is fully justified.</p>
<p id="b344-6">III.</p>
<p id="b344-7">We come, then, to the question whether, even though the search was lawful, the Court of Appeals was correct in holding that the seizure and introduction of the items of clothing violated the Fourth Amendment because they are “mere evidence.” The distinction made by some of our cases between seizure of items of evidential value only and seizure of instrumentalities, fruits, or contraband has been criticized by courts<footnotemark>6</footnotemark> and commentators.<footnotemark>7</footnotemark> The Court of Appeals, however, felt “obligated to adhere to it.” <span class="citation" data-id="9451981"><a href="/opinion/272530/bennie-joe-hayden-v-warden-maryland-penitentiary/#655" aria-description="Citation for case: Bennie Joe Hayden v. Warden, Maryland Penitentiary">363 F. 2d, at 655</a></span>. We today reject the distinction as based on premises no longer <page-number citation-index="1" label="301">*301</page-number>accepted as rules governing the application of the Fourth Amendment.<footnotemark>8</footnotemark></p>
<p id="b345-5">We have examined on many occasions the history and purposes of the Amendment.<footnotemark>9</footnotemark> It was a reaction to the evils of the use of the general warrant in England and the writs of assistance in the Colonies, and was intended to protect against invasions of “the sanctity of a man’s home and the privacies of life,” <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span>, from searches under indiscriminate, general authority. Protection of these interests was assured by prohibiting all “unreasonable” searches and seizures, and by requiring the use of warrants, which particularly describe “the place to be searched, and the persons or things to be seized,” thereby interposing “a magistrate between the citizen and the police,” <em>McDonald </em>v. <em>United States, supra, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S., at 455</a></span>.</p>
<p id="b345-6">Nothing in the language of the Fourth Amendment supports the distinction between “mere evidence” and instrumentalities, fruits of crime, or contraband. On its face, the provision assures the “right of the people to be secure in their persons, houses, papers, and effects . . . ,” without regard to the use to which any of these things are applied. This “right of the people” is certainly unrelated to the “mere evidence” limitation. Privacy is disturbed no more by a search directed to a purely evidentiary object than it is by a search directed to an instrumen<page-number citation-index="1" label="302">*302</page-number>tality, fruit, or contraband. A magistrate can intervene in both situations, and the requirements of probable cause and specificity can be preserved intact. Moreover, nothing in the nature of property seized as evidence renders it more private than property seized, for example, as an instrumentality; quite the opposite may be true. Indeed, the distinction is wholly irrational, since, depending on the circumstances, the same “papers and effects” may be “mere evidence” in one case and “instrumentality” in another. See Comment, <span class="citation no-link">20 U. Chi. L. Rev. 319</span>, 320-322 (1953).</p>
<p id="b346-4">In <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span>, the Court said that search warrants “may not be used as a means of gaining access to a man’s house or office and papers solely for the purpose of making search to secure evidence to be used against him in a criminal or penal proceeding . . . .” The Court derived from <em>Boyd </em>v. <em>United States, supra, </em>the proposition that warrants “may be resorted to only when a primary right to such search and seizure may be found in the interest which the public or the complainant may have in the property to be seized, or in the right to the possession of it, or when a valid exercise of the police power renders possession of the property by the accused unlawful and provides that it may be taken,” <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S., at 309</a></span>; that is, when the property is an instrumentality or fruit of crime, or contraband. Since it was “impossible to say, on the record . . . that the Government had any interest” in the papers involved “other than as evidence against the accused . . . ,” “to permit them to be used in evidence would be, in effect, as ruled in the <em>Boyd Case, </em>to compel the defendant to become a witness against himself.” <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#311" aria-description="Citation for case: Gouled v. United States"><em>Id., at </em>311</a></span>.</p>
<p id="b346-5">The items of clothing involved in this case are not “testimonial” or “communicative” in nature, and their introduction therefore did not compel respondent to be<page-number citation-index="1" label="303">*303</page-number>come a witness against himself in violation of the Fifth Amendment. <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>. This case thus does not require that we consider whether there are items of evidential value whose very nature precludes them from being the object of a reasonable search and seizure.</p>
<p id="b347-5">The Fourth Amendment ruling in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>was based upon the dual, related premises that historically the right to search for and seize property depended upon the assertion by the Government of a valid claim of superior interest, and that it was not enough that the purpose of the search and seizure was to obtain evidence to use in apprehending and convicting criminals. The common law of search and seizure after <em>Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, reflected Lord Camden’s view, derived no doubt from the political thought of his time, that the “great end, for which men entered into society, was to secure their property.” <em>Id., </em>at 1066. Warrants were “allowed only where the primary right to such a search and seizure is in the interest which the public or complainant may have in the property seized.” Lasson, The History and Development of the Fourth Amendment to the United States Constitution 133-134. Thus stolen property — the fruits of crime — was always subject to seizure. And the power to search for stolen property was gradually extended to cover “any property which the private citizen was not permitted to possess,” which included instrumentalities of crime (because of the early notion that items used in crime were forfeited to the State) and contraband. Kaplan, Search and Seizure: A No-Man’s Land in the Criminal Law, <span class="citation no-link">49 Calif. L. Rev. 474</span>, 475. No separate governmental interest in seizing evidence to apprehend and convict criminals was recognized; it was required that some property interest be asserted. The remedial structure also reflected these dual premises. Trespass, replevin, and the other means of <page-number citation-index="1" label="304">*304</page-number>redress for persons aggrieved by searches and seizures, depended upon proof of a superior property interest. And since a lawful seizure presupposed a superior claim, it was inconceivable that a person could recover property lawfully seized. As Lord Camden pointed out in <em>Entick </em>v. <em>Carrington, supra, </em>at 1066, a general warrant enabled “the party’s own property [to be] seized before and without conviction, and he has no power to reclaim his goods, even after his innocence is cleared by acquittal.”</p>
<p id="b348-6">The premise that property interests control the right of the Government to search and seize has been discredited. Searches and seizures may be “unreasonable” within the Fourth Amendment even though the Government asserts a superior property interest at common law. We have recognized that the principal object of the Fourth Amendment is the protection of privacy rather than property, and have increasingly discarded fictional and procedural barriers rested on property concepts. See <em>Jones </em>v. <em>United States, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266</a></span>; <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span>. This shift in emphasis from property to privacy has come about through a subtle interplay of substantive and procedural reform. The remedial structure at the time even of <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>, was arguably explainable in property terms. The Court held in <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>that a defendant could petition <em>before </em>trial for the return of his illegally seized property, a proposition not necessarily inconsistent with <em>Adams </em>v. <em>New York, </em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>, which held in effect that the property issues involved in search and seizure are collateral to a criminal proceeding.<footnotemark>10</footnotemark> The remedial structure finally escaped the bounds of common law property limitations in <em>Silverthorne </em><page-number citation-index="1" label="305">*305</page-number><em>Lumber Co. </em>v. <em>United States, </em><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, and <em>Gouled </em>v. <em>United States, supra, </em>when it became established that suppression might be sought during a criminal trial, and under circumstances which would not sustain an action in trespass or replevin. Recognition that the role of the Fourth Amendment was to protect against invasions of privacy demanded a remedy to condemn the seizure in <em>Silverthorne, </em>although no possible common law claim existed for the return of the copies made by the Government of the papers it had seized. The remedy of suppression, necessarily involving only the limited, functional consequence of excluding the evidence from trial, satisfied that demand.</p>
<p id="b349-5">The development of search and seizure law since <em>Silver-thorne </em>and <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>is replete with examples of the transformation in substantive law brought about through the interaction of the felt need to protect privacy from unreasonable invasions and the flexibility in rulemaking made possible by the remedy of exclusion. We have held, for example, that intangible as well as tangible evidence may be suppressed, <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#485" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 485-486</a></span>, and that an actual trespass under local property law is unnecessary to support a remediable violation of the Fourth Amendment, <em>Silverman </em>v. <em>United States, supra. </em>In determining whether someone is a “person aggrieved by an unlawful search and seizure” we have refused “to import into the law . . . subtle distinctions, developed and refined by the common law in evolving the body of private property law which, more than almost any other branch of law, has been shaped by distinctions whose validity is largely historical.” <em>Jones </em>v. <em>United States, supra, </em><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S., at 266</a></span>. And with particular relevance here, we have given recognition to the interest in privacy despite the complete absence of a property claim by suppressing the very items which at <page-number citation-index="1" label="306">*306</page-number>common law could be seized with impunity: stolen goods, <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span>; instrumentalities, <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>; <em>McDonald </em>v. <em>United States, supra; </em>and contraband, <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699</a></span>; <em>Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>.</p>
<p id="b350-6">The premise in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>that government may not seize evidence simply for the purpose of proving crime has likewise been discredited. The requirement that the Government assert in addition some property interest in material it seizes has long been a fiction,<footnotemark>11</footnotemark> obscuring the reality that government has an interest in solving crime. <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>settled the proposition that it is reasonable, within the terms of the Fourth Amendment, to conduct otherwise permissible searches for the purpose of obtaining evidence which would aid in apprehending and convicting criminals. The requirements of the Fourth Amendment can secure the same protection of privacy <page-number citation-index="1" label="307">*307</page-number>whether the search is for “mere evidence” or for fruits, instrumentalities or contraband. There must, of course, be a nexus — automatically provided in the case of fruits, instrumentalities or contraband — between the item to be seized and criminal behavior. Thus in the case of “mere evidence,” probable cause must be examined in terms of cause to believe that the evidence sought will aid in a particular apprehension or conviction. In so doing, consideration of police purposes will be required. Cf. <em>Kremen </em>v. <em>United States, </em><span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span>. But no such problem is presented in this case. The clothes found in the washing machine matched the description of those worn by the robber and the police therefore could reasonably believe that the items would aid in the identification of the culprit.</p>
<p id="b351-5">The remedy of suppression, moreover, which made possible protection of privacy from unreasonable searches without regard to proof of a superior property interest, likewise provides the procedural device necessary for allowing otherwise permissible searches and seizures conducted solely to obtain evidence of crime. For just as the suppression of evidence does not entail a declaration of superior property interest in the person aggrieved, thereby enabling him to suppress evidence unlawfully seized despite his inability to demonstrate such an interest (as with fruits, instrumentalities, contraband), the refusal to suppress evidence carries no declaration of superior property interest in the State, and should thereby enable the State to introduce evidence lawfully seized despite its inability to demonstrate such an interest. And, unlike the situation at common law, the owner of property would not be rendered remediless if “mere evidence” could lawfully be seized to prove crime. For just as the suppression of evidence does not in itself necessarily entitle the aggrieved person to its return (as, for example, contraband), the introduction of “mere evidence” does not in <page-number citation-index="1" label="308">*308</page-number>itself entitle the State to its retention. Where public officials “unlawfully seize <em>or hold </em>a citizen’s realty or chattels, recoverable by appropriate action at law or in equity . . . ,” the true owner may “bring his possessory action to reclaim that which is wrongfully withheld.” <em>Land </em>v. <em>Dollar, </em><span class="citation" data-id="9419978"><a href="/opinion/104407/land-v-dollar/#738" aria-description="Citation for case: Land v. Dollar">330 U. S. 731, 738</a></span>. (Emphasis added.) See <em>Burdeau </em>v. <em>McDowell, </em><span class="citation" data-id="99820"><a href="/opinion/99820/burdeau-v-mcdowell/#474" aria-description="Citation for case: Burdeau v. McDowell">256 U. S. 465, 474</a></span>.</p>
<p id="b352-6">The survival of the <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>distinction is attributable more to chance than considered judgment. Legislation has helped perpetuate it. Thus, Congress has never authorized the issuance of search warrants for the seizure of mere evidence of crime. See <em>Davis </em>v. <em>United States, </em><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#606" aria-description="Citation for case: Davis v. United States">328 U. S. 582, 606</a></span> (dissenting opinion of Mr. Justice Frankfurter). Even in the Espionage Act of 1917, where Congress for the first time granted general authority for the issuance of search warrants, the authority was limited to fruits of crime, instrumentalities, and certain contraband. <span class="citation no-link">40 Stat. 228</span>. <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>concluded, needlessly it appears, that the Constitution virtually limited searches and seizures to these categories.<footnotemark>12</footnotemark> After <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span>, </em>pressure <page-number citation-index="1" label="309">*309</page-number>to test this conclusion was slow to mount. Rule 41 (b) of the Federal Rules of Criminal Procedure incorporated the <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>categories as limitations on federal authorities to issue warrants, and <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, only recently made the “mere evidence” rule a problem in the state courts. Pressure against the rule in the federal courts has taken the form rather of broadening the categories of evidence subject to seizure, thereby creating considerable confusion in the law. See, <em>e. g., </em>Note, 54 Geo. L. J. 593, 607-621 (1966).</p>
<p id="b353-5">The rationale most frequently suggested for the rule preventing the seizure of evidence is that “limitations upon the fruit to be gathered tend to limit the quest itself.” <em>United States </em>v. <em>Poller, </em><span class="citation" data-id="1476321"><a href="/opinion/1476321/united-states-v-poller/#914" aria-description="Citation for case: United States v. Poller">43 F. 2d 911, 914</a></span> (C. A. 2d Cir. 1930). But privacy “would be just as well served by a restriction on search to the even-numbered days of the month. . . . And it would have the extra advantage of avoiding hair-splitting questions . . . .” Kaplan, <em>op. cit. supra, </em>at 479. The “mere evidence” limitation has spawned exceptions so numerous and confusion so great, in fact, that it is questionable whether it affords meaningful protection. But if its rejection does enlarge the area of permissible searches, the intrusions are nevertheless made after fulfilling the probable cause and particularity requirements of the Fourth Amendment and after the intervention of “a neutral and detached magis<page-number citation-index="1" label="310">*310</page-number>trate . . . .” <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>. The Fourth Amendment allows intrusions upon privacy-under these circumstances, and there is no viable reason to distinguish intrusions to secure “mere evidence” from intrusions to secure fruits, instrumentalities, or contraband.</p>
<p id="b354-4">The judgment of the Court of Appeals is</p>
<p id="b354-5">
<em>Reversed.</em>
</p>
<judges id="b354-6">Mr. Justice Black concurs in the result.</judges>
<footnote label="1">
<p id="b340-7"> <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#154" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 154</a></span>; see also <em>Gouled </em>v. <em>United States, </em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465-466</a></span>; <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#64" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 64, n. 6</a></span>; <em>Abel </em>v. <em>United States, </em><span class="citation" data-id="9421949"><a href="/opinion/106021/abel-v-united-states/#234" aria-description="Citation for case: Abel v. United States">362 U. S. 217, 234-235</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b340-8"> Hayden did not appeal from his conviction. He first sought relief by an application under the Maryland Post Conviction Procedure Act which was denied without hearing. The Maryland Court of Appeals reversed and remanded for a hearing. <span class="citation" data-id="1990408"><a href="/opinion/1990408/hayden-v-warden-of-the-maryland-penitentiary/" aria-description="Citation for case: Hayden v. Warden of the Maryland Penitentiary">233 Md. 613</a></span>, <span class="citation" data-id="1990408"><a href="/opinion/1990408/hayden-v-warden-of-the-maryland-penitentiary/" aria-description="Citation for case: Hayden v. Warden of the Maryland Penitentiary">195 A. 2d 692</a></span>. The trial court denied relief after hearing, concluding “that the search of his home and the seizure of the articles in question were proper.” His application for federal habeas corpus relief resulted, after hearing in the District Court, in the same conclusion.</p>
</footnote>
<footnote label="3">
<p id="b341-7"> The State claims that, since Hayden failed to raise the search and seizure question at trial, he deliberately bypassed state remedies and should be denied an opportunity to assert his claim in federal court. See <em>Henry </em>v. Mississippi, <span class="citation" data-id="9422929"><a href="/opinion/106962/henry-v-mississippi/" aria-description="Citation for case: Henry v. Mississippi">379 U. S. 443</a></span>; <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">372 U. S. 391</a></span>. Whether or not the Maryland Court of Appeals actually intended, when it reversed the state trial court’s denial of post-conviction relief, that Hayden be afforded a hearing on the merits of his claim, it is clear that the trial court so understood the order of the Court of Appeals. A hearing was held in the state courts, and the claim denied on the merits. In this circumstance, the Fourth Circuit was correct in rejecting the State’s deliberate-bypassing claim. The deliberate-bypass rule is applicable only “to an applicant who has deliberately by-passed the orderly procedure of the state courts <em>and in so doing has forfeited his state court remedies.” Fay </em>v. <em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/" aria-description="Citation for case: Fay v. Noia">Noia, supra,</a></span> </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#438" aria-description="Citation for case: Fay v. Noia">372 U. S., at 438</a></span>. (Emphasis added.) But see <em>Nelson </em>v. <em>California, </em><span class="citation" data-id="268073"><a href="/opinion/268073/chester-nelson-v-people-of-the-state-of-california-robert-a-heinze/#82" aria-description="Citation for case: Chester Nelson v. People of the State of California,...">346 F. 2d 73, 82</a></span> (C. A. 9th Cir. 1965).</p>
</footnote>
<footnote label="4">
<p id="b341-8"> The state postconviction court found that Mrs. Hayden “gave the policeman permission to enter the home.” The federal habeas corpus court stated it “would be justified in accepting the findings <page-number citation-index="1" label="298">*298</page-number>of historical fact made by Judge Sodaro on that issue but concluded that resolution of the issue would be unnecessary, because the officers were “justified in entering and searching the house for the felon, for his weapons and for the fruits of the robbery.”</p>
</footnote>
<footnote label="5">
<p id="b344-8"> The officer was asked in the District Court whether he found the money. He answered that he did not, and stated: “By the time I had gotten down into the basement I heard someone say upstairs, 'There’s a man up here.’ ” He was asked: “What did you do then?” and answered: “By this time I had already discovered some clothing which fit the description of the clothing worn by the subject that we were looking for . . . .” It is clear from the record and from the findings that the weapons were found after or at the same time the police found Hayden.</p>
</footnote>
<footnote label="6">
<p id="b344-9"> <em>People </em>v. <em>Thayer, </em><span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">63 Cal. 2d 635</a></span>, <span class="citation" data-id="1421285"><a href="/opinion/1421285/people-v-thayer/" aria-description="Citation for case: People v. Thayer">408 P. 2d 108</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./384/908/">384 U. S. 908</a></span>; <em>State </em>v. <em>Bisaccia, </em>45 N. J. 504, <span class="citation" data-id="1923442"><a href="/opinion/1923442/state-v-bisaccia/" aria-description="Citation for case: State v. Bisaccia">213 A. 2d 185</a></span>. Compare <em>United States </em>v. <em>Poller, </em><span class="citation" data-id="1476321"><a href="/opinion/1476321/united-states-v-poller/#914" aria-description="Citation for case: United States v. Poller">43 F. 2d 911, 914</a></span> (C. A. 2d Cir. 1930).</p>
</footnote>
<footnote label="7">
<p id="b344-10"> <em>E. g., </em>Chafee, The Progress of the Law, 1919-1922, <span class="citation no-link">35 Harv. L. Rev. 673</span> (1922); Kamisar, The Wiretapping-Eavesdropping Problem: A Professor’s View, <span class="citation no-link">44 Minn. L. Rev. 891</span>, 914-918 (1960); Kaplan, Search and Seizure: A No-Man’s Land in the Criminal Law, <span class="citation no-link">49 Calif. L. Rev. 474</span>, 478 (1961); Comment, 45 N. C. L. Rev. 512 (1967); Comment, 66 Col. L. Rev. 355 (1966); Comment, <span class="citation no-link">20 U. Chi. L. Rev. 319</span> (1953); Comment, 31 Yale L. J. 518 (1922). Compare, <em>e. g., </em>Fraenkel, Concerning Searches and Seizures, <span class="citation no-link">34 Harv. L. Rev. 361</span> (1921); Note, 54 Geo. L. J. 593 (1966).</p>
</footnote>
<footnote label="8">
<p id="b345-7"> This Court has approved the seizure and introduction of items having only evidential value without, however, considering the validity of the distinction rejected today. See <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span>; <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span>.</p>
</footnote>
<footnote label="9">
<p id="b345-10"> <em>E. g., Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-485</a></span>; <em>Marcus </em>v. <em>Search Warrant, </em><span class="citation" data-id="9422285"><a href="/opinion/106287/marcus-v-search-warrant-of-property/#724" aria-description="Citation for case: Marcus v. Search Warrant of Property">367 U. S. 717, 724-729</a></span>; <em>Frank </em>v. <em>Maryland, </em><span class="citation" data-id="9421796"><a href="/opinion/105880/frank-v-maryland/#363" aria-description="Citation for case: Frank v. Maryland">359 U. S. 360, 363-365</a></span>. See generally Lasson, The History and Development of the Fourth Amendment to the United States Constitution (1937); Landynski, Search and Seizure and the Supreme Court (1966).</p>
</footnote>
<footnote label="10">
<p id="b348-7"> Both <em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">Weeks</a></span> </em>and <em><span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">Adams</a></span> </em>were written by Justice Day, and joined by several of the same Justices, including Justice Holmes.</p>
</footnote>
<footnote label="11">
<p id="b350-7"> At common law the Government did assert a superior property interest when it searched lawfully for stolen property, since the procedure then followed made it necessary that the true owner swear that his goods had been taken. But no such procedure need be followed today; the Government may demonstrate probable cause and lawfully search for stolen property even though the true owner is unknown or unavailable to request and authorize the Government to assert his interest. As to instrumentalities, the Court in <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>allowed their seizure, not because the Government had some property interest in them (under the ancient, fictitious forfeiture theory), but because they could be used to perpetrate further crime. <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S., at 309</a></span>. The same holds true, of course, for “mere evidence”; the prevention of crime is served at least as much by allowing the Government to identify and capture the criminal, as it is by allowing the seizure of his instrumentalities. Finally, contraband is indeed property in which the Government holds a superior interest, but only because the Government decides to vest such an interest in itself. And while there may be limits to what may be declared contraband, the concept is hardly more than a form through which the Government seeks to prevent and deter crime.</p>
</footnote>
<footnote label="12">
<p id="b352-7"> <em><span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">Gouled</a></span> </em>was decided on certified questions. The only question which referred to the Espionage Act of 1917 stated: “Are papers of . . . evidential value . . . , when taken under search warrants issued pursuant to Act of June 15, 1917, from the house or office of the person so suspected, — seized and taken in violation of the 4th amendment?” <em>Gouled </em>v. <em>United States, </em>No. 250, Oct. Term, 1920, Certificate, p. 4. Thus the form in which the case was certified made it difficult if not impossible “to limit the decision to the sensible proposition of statutory construction, that Congress had not as yet authorized the seizure of purely evidentiary material.” Chafee, <em>op. cit. supra, </em>at 699. The Government assumed the validity of petitioner’s argument that <em>Entick </em>v. <em>Carrington, Boyd </em>v. <em>United States, </em>and other authorities established the constitutional illegality of seizures of private papers for use as evidence. <em>Gouled </em>v. <em>United States, supra, </em>Brief for the United States, p. 50. It argued, complaining of the absence of a record, that the papers introduced in evidence were instrumentalities of crime. The Court ruled that the <page-number citation-index="1" label="309">*309</page-number>record before it revealed no government interest in the papers other than as evidence against the accused. <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#311" aria-description="Citation for case: Gouled v. United States">255 U. S., at 311</a></span>.</p>
<p id="b353-7">Significantly, <em>Entick </em>v. <em>Carrington </em>itself has not been read by the English courts as making unlawful the seizure of all papers for use as evidence. See <em>Dillon </em>v. <em>O’Brien, </em>20 L. R. Ir. 300; <em>Elias </em>v. <em>Pasmore, </em>[1934] 2 K. B. 164. Although <em>Dillon, </em>decided in 1887, involved instrumentalities, the court did not rely on this fact, but rather on “the interest which the State has in a person guilty (or reasonably believed to be guilty) of a crime being brought to justice . . . .” 20 L. R. Ir., at 317.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Wearry v. Cain.json  (`lake-record`, 6 assertions)

### content_page

```
---
title: "Wearry v. Cain"
type: case
citation: ""
parallel_cite: "577 U.S. 385; 136 S. Ct. 1002; 194 L. Ed. 2d 78; 84 U.S.L.W. 4125; 26 Fla. L. Weekly Fed. S 17"
neutral_cite: "2016 U.S. LEXIS 1654; 2016 WL 854158"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2016
date_decided: 2016-03-07
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2016-03-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wearry v. Cain
  varies_by_point: false
  scope_note: "Per curiam; reaffirms cumulative Brady materiality. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/3183098/wearry-v-cain/"
  cluster_id: 3183098
  opinion_id: 3183080
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Kyles v. Whitley]]", "[[Smith v. Cain]]", "[[Giglio v. United States]]"]
aliases: ["Wearry"]
tags: ["case", "due-process", "brady", "materiality", "impeachment", "per-curiam"]
holding: "Reaffirms cumulative *Brady* materiality: suppressed evidence assessed collectively undermined confidence in the verdict."
lake:
  record_id: Wearry v. Cain
  status: verified
  projected_at: 2026-07-09
---

# Wearry v. Cain

*577 U.S. 385 (2016)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Michael Wearry was convicted of capital murder and sentenced to death almost entirely on the testimony of two witnesses, Scott (a prison informant) and Brown. On collateral review it emerged that the State had failed to disclose evidence impeaching both: that Scott had coached another inmate to lie about the murder, that a third man (Hutchinson) may have been physically unable to perform the role Scott described, that Scott may have implicated Wearry to settle a personal score, that Brown had twice sought a deal to reduce his own sentence, and medical records casting doubt on a witness's account of Wearry's running. The state postconviction court denied relief, finding no prejudice.

## Issue
Whether the State's suppression of evidence impeaching its key witnesses was material under *[[Brady v. Maryland]]*, requiring a new trial, where the evidence must be assessed cumulatively rather than item by item.

## Rule
Suppressed favorable evidence violates due process when it is material, and materiality is measured generously: "Evidence qualifies as material when there is "'any reasonable likelihood'" it could have "'affected the judgment of the jury.'"" — 136 S. Ct. at 1006. ^pin-1006

The defendant's burden is confidence-based, not preponderance-based: "He must show only that the new evidence is sufficient to 'undermine confidence' in the verdict." — *Id.* ^pin-1006a

And materiality must be assessed collectively — the court must conduct a "cumulative evaluation" of the suppressed evidence rather than gauge each piece "in isolation." — [*Id.* at 1007](https://www.courtlistener.com/opinion/3183098/wearry-v-cain/#:~:text=cumulative%20evaluation). ^pin-1007

## Application
On these facts the prosecution's case "resemble[d] a house of cards, built on the jury crediting Scott's account rather than Wearry's alibi." — 136 S. Ct. at 1006. ^pin-1006b

The withheld evidence went directly to the credibility of the only witnesses tying Wearry to the murder: it would have shown Scott coached a false story and had a motive to lie, that the role he assigned a confederate may have been physically impossible, and that Brown was angling for a sentence reduction. The state court compounded its error by weighing each item separately. Considered cumulatively, that evidence was enough to undermine confidence in the verdict, establishing a *[[Brady v. Maryland|Brady]]* violation.

## Conclusion
The suppressed impeachment evidence was material; its cumulative weight undermined confidence in the verdict. The Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for a new trial without reaching Wearry's ineffective-assistance claim.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Wearry* applies the materiality standard of [[Brady v. Maryland]] and [[Giglio v. United States]], reaffirms the "cumulative evaluation" command of [[Kyles v. Whitley]], and tracks the confidence-in-the-verdict analysis of [[Smith v. Cain]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Wearry v. Cain*, 577 U.S. 385 (2016) — https://www.courtlistener.com/opinion/3183098/wearry-v-cain/ — pinpoints given to the parallel S. Ct. reporter (CourtListener star-paginates *Wearry* by 136 S. Ct.): 1006, 1007. Cluster 3183098 → opinion 3183080.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "86118510f68bce74", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Wearry v. Cain"}, "payload": {"all": [{"cite": "577 U.S. 385", "page": "385", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "577"}, {"cite": "136 S. Ct. 1002", "page": "1002", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "136"}, {"cite": "194 L. Ed. 2d 78", "page": "78", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "194"}, {"cite": "2016 U.S. LEXIS 1654", "page": "1654", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2016"}, {"cite": "84 U.S.L.W. 4125", "page": "4125", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "84"}, {"cite": "26 Fla. L. Weekly Fed. S 17", "page": "17", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "2016 WL 854158", "page": "854158", "reporter": "WL", "selected_official": false, "source": "cluster.citations[]", "type": 7, "volume": "2016"}], "display": null, "official": null, "official_selection_present": false, "record_id": "Wearry v. Cain"}}
{"assertion_id": "30891be4f45debde", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1007", "record_id": "Wearry v. Cain"}, "payload": {"fragment": "#:~:text=cumulative%20evaluation", "page": null, "pin_id": "pin-1007", "pinpoint_status": "slip-only", "quote": "cumulative evaluation", "quote_fidelity": "matched", "record_id": "Wearry v. Cain", "star_marker": null}}
{"assertion_id": "405421ca979bc993", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1006b", "record_id": "Wearry v. Cain"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1006b", "pinpoint_status": "slip-only", "quote": "resemble[d] a house of cards, built on the jury crediting Scott's account rather than Wearry's alibi.", "quote_fidelity": "mismatch", "record_id": "Wearry v. Cain", "star_marker": null}}
{"assertion_id": "a1b2a401763a2d3f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1006a", "record_id": "Wearry v. Cain"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1006a", "pinpoint_status": "slip-only", "quote": "He must show only that the new evidence is sufficient to 'undermine confidence' in the verdict.", "quote_fidelity": "mismatch", "record_id": "Wearry v. Cain", "star_marker": null}}
{"assertion_id": "d381ff6d9ebbfdac", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-1006", "record_id": "Wearry v. Cain"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-1006", "pinpoint_status": "slip-only", "quote": "--- # Wearry v. Cain *577 U.S. 385 (2016)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Michael Wearry was convicted of capital murder and sentenced to death almost entirely on the testimony of two witnesses, Scott (a prison informant) and Brown. On collateral review it emerged that the State had failed to disclose evidence impeaching both: that Scott had coached another inmate to lie about the murder, that a third man (Hutchinson) may have been physically unable to perform the role Scott described, that Scott may have implicated Wearry to settle a personal score, that Brown had twice sought a deal to reduce his own sentence, and medical records casting doubt on a witness's account of Wearry's running. The state postconviction court denied relief, finding no prejudice. ## Issue Whether the State's suppression of evidence impeaching its key witnesses was material under *Brady v. Maryland*, requiring a new trial, where the evidence must be assessed cumulatively rather than item by item. ## Rule Suppressed favorable evidence violates due process when it is material, and materiality is measured generously:", "quote_fidelity": "mismatch", "record_id": "Wearry v. Cain", "star_marker": null}}
{"assertion_id": "5c727fe1c6b805f9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Wearry v. Cain"}, "payload": {"as_of_content": "2016-03-07", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Wearry v. Cain", "scope_note": "Per curiam; reaffirms cumulative Brady materiality. Good law.", "varies_by_point": false}}
```

### lake record — Wearry v. Cain

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wearry v. Cain",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wearry v. Cain",
    "case_name_short": "Wearry",
    "case_name_full": "Michael WEARRY v. Burl CAIN, Warden.",
    "input_case_name": "Wearry v. Cain",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2016-03-07",
    "year": 2016,
    "docket": null,
    "cluster_id": 3183098,
    "lead_opinion_id": 3183080,
    "sibling_ids": [
      3183080
    ],
    "absolute_url": "/opinion/3183098/wearry-v-cain/",
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
        "cite": "577 U.S. 385",
        "volume": "577",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 1002",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "1002",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "194 L. Ed. 2d 78",
        "volume": "194",
        "reporter": "L. Ed. 2d",
        "page": "78",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4125",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4125",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 17",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. LEXIS 1654",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "1654",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 854158",
        "volume": "2016",
        "reporter": "WL",
        "page": "854158",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "577 U.S. 385",
        "volume": "577",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 1002",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "1002",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "194 L. Ed. 2d 78",
        "volume": "194",
        "reporter": "L. Ed. 2d",
        "page": "78",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. LEXIS 1654",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "1654",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4125",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4125",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 17",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 854158",
        "volume": "2016",
        "reporter": "WL",
        "page": "854158",
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
      "id": "pin-1006",
      "page": null,
      "quote": "--- # Wearry v. Cain *577 U.S. 385 (2016)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Michael Wearry was convicted of capital murder and sentenced to death almost entirely on the testimony of two witnesses, Scott (a prison informant) and Brown. On collateral review it emerged that the State had failed to disclose evidence impeaching both: that Scott had coached another inmate to lie about the murder, that a third man (Hutchinson) may have been physically unable to perform the role Scott described, that Scott may have implicated Wearry to settle a personal score, that Brown had twice sought a deal to reduce his own sentence, and medical records casting doubt on a witness's account of Wearry's running. The state postconviction court denied relief, finding no prejudice. ## Issue Whether the State's suppression of evidence impeaching its key witnesses was material under *Brady v. Maryland*, requiring a new trial, where the evidence must be assessed cumulatively rather than item by item. ## Rule Suppressed favorable evidence violates due process when it is material, and materiality is measured generously:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1006a",
      "page": null,
      "quote": "He must show only that the new evidence is sufficient to 'undermine confidence' in the verdict.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1007",
      "page": null,
      "quote": "cumulative evaluation",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 17776,
      "fragment": "#:~:text=cumulative%20evaluation",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1006b",
      "page": null,
      "quote": "resemble[d] a house of cards, built on the jury crediting Scott's account rather than Wearry's alibi.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-03-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wearry v. Cain",
    "varies_by_point": false,
    "scope_note": "Per curiam; reaffirms cumulative Brady materiality. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Joseph Prystash v. Lorie Davis, Director",
          "cluster_id": 4386207,
          "cite": [
            "854 F.3d 830",
            "2017 WL 1487229",
            "2017 U.S. App. LEXIS 7365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane1_negative"
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
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armstrong v. Ashley",
          "cluster_id": 9375737,
          "cite": [
            "60 F.4th 262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Refugio Ruiz-Cortez v. Glenn Lewellen",
          "cluster_id": 4643210,
          "cite": [
            "931 F.3d 592"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
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
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Natividad, R., Aplt.",
          "cluster_id": 4583669,
          "cite": [
            "200 A.3d 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
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
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
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
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Browning v. Renee Baker",
          "cluster_id": 4427560,
          "cite": [
            "875 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex parte Chaney",
          "cluster_id": 6243270,
          "cite": [
            "563 S.W.3d 239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Walter Liew",
          "cluster_id": 4389310,
          "cite": [
            "856 F.3d 585",
            "2017 WL 1753269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glossip v. Oklahoma",
          "cluster_id": 10339023,
          "cite": [
            "604 U.S. 226"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCray v. Capra",
          "cluster_id": 7857399,
          "cite": [
            "45 F.4th 634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Ausby",
          "cluster_id": 4595449,
          "cite": [
            "916 F.3d 1089"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wearry v. Foster",
          "cluster_id": 6465433,
          "cite": [
            "33 F.4th 260"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sepulveda",
          "cluster_id": 9389969,
          "cite": [
            "64 F.4th 700"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jimenez",
          "cluster_id": 4240628,
          "cite": [
            "142 A.D.3d 149",
            "37 N.Y.S.3d 225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davel Chinn v. Warden, Chillicothe Corr. Inst.",
          "cluster_id": 6251617,
          "cite": [
            "24 F.4th 1096"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania State Conference of NAACP Branches v. Northampton County Board of Elections",
          "cluster_id": 9488671,
          "cite": [
            "97 F.4th 120"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Solorio v. Muniz",
          "cluster_id": 9022945,
          "cite": [
            "896 F.3d 914"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hill",
          "cluster_id": 4587704,
          "cite": [
            "2019 Ohio 365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brumfield",
          "cluster_id": 9454987,
          "cite": [
            "89 F.4th 506"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Juniper v. Melvin Davis",
          "cluster_id": 9414861,
          "cite": [
            "74 F.4th 196"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kuantau Reeder v. Darrel Vannoy, Warden",
          "cluster_id": 4798511,
          "cite": [
            "978 F.3d 272"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Floyd v. Darrel Vannoy, Warden",
          "cluster_id": 4484952,
          "cite": [
            "887 F.3d 214"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(3183080) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 64,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 64,
        "triage_read": 1,
        "triage_snippet_classified": 63
      },
      "lane2_top_cited": {
        "query": "cites:(3183080)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTA2OTU0MjYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%283183080%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(3183080)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(3183080)",
    "indexed_citing_opinions": 78,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 3183080,
        "count": 78,
        "count_source": "search"
      }
    ],
    "citation_count": 202,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wearry-v-cain.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4ODIzMjMmcz05NDA0ODc5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%283183080%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 3183080,
        "cited_id": 1756,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 111662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 121158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 145639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 145759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 149653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 620666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 1129223,
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
    "date_created": "2026-07-06T04:08:42Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:08:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:08:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:11:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:08:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wearry v. Cain

```
                 Cite as: 577 U. S. ____ (2016)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
     MICHAEL WEARRY v. BURL CAIN, WARDEN
  ON PETITION FOR WRIT OF CERTIORARI TO THE DISTRICT
        COURT OF LOUISIANA, LIVINGSTON PARISH
             No. 14–10008.   Decided March 7, 2016

  PER CURIAM.
  Michael Wearry is on Louisiana’s death row. Urging
that the prosecution failed to disclose evidence supporting
his innocence and that his counsel provided ineffective
assistance at trial, Wearry unsuccessfully sought postcon-
viction relief in state court. Contrary to the state postcon-
viction court, we conclude that the prosecution’s failure to
disclose material evidence violated Wearry’s due process
rights. We reverse the state postconviction court’s judg-
ment on that account, and therefore do not reach Wearry’s
ineffective-assistance-of-counsel claim.
                              I
                             A
  Sometime between 8:20 and 9:30 on the evening of April
4, 1998, Eric Walber was brutally murdered. Nearly two
years after the murder, Sam Scott, at the time incarcer-
ated, contacted authorities and implicated Michael Wearry.
Scott initially reported that he had been friends with
the victim; that he was at work the night of the murder;
that the victim had come looking for him but had instead
run into Wearry and four others; and that Wearry and the
others had later confessed to shooting and driving over the
victim before leaving his body on Blahut Road. In fact, the
victim had not been shot, and his body had been found on
Crisp Road.
  Scott changed his account of the crime over the course of
four later statements, each of which differed from the
others in material ways. By the time Scott testified as the
2                     WEARRY v. CAIN

                         Per Curiam

State’s star witness at Wearry’s trial, his story bore little
resemblance to his original account. According to the
version Scott told the jury, he had been playing dice with
Wearry and others when the victim drove past. Wearry,
who had been losing, decided to rob the victim. After
Wearry and an acquaintance, Randy Hutchinson, stopped
the victim’s car, Hutchinson shoved the victim into the
cargo area. Five men, including Scott, Hutchinson, and
Wearry, proceeded to drive around, at one point encoun-
tering Eric Brown—the State’s other main witness—and
pausing intermittently to assault the victim. Finally,
Scott related, Wearry and two others killed the victim by
running him over. On cross-examination, Scott admitted
that he had changed his account several times.
   Consistent with Scott’s testimony, Brown testified that
on the night of the murder he had seen Wearry and others
with a man who looked like the victim. Incarcerated on
unrelated charges at the time of Wearry’s trial, Brown
acknowledged that he had made a prior inconsistent
statement to the police, but had recanted and agreed to
testify against Wearry, not for any prosecutorial favor, but
solely because his sister knew the victim’s sister. The
State commented during its opening argument that Brown
“is doing 15 years on a drug charge right now, [but] hasn’t
asked for a thing.” 7 Record 1723 (Tr., Mar. 2, 2002).
During closing argument, the State reiterated that Brown
“has no deal on the table” and was testifying because the
victim’s “family deserves to know.” Pet. for Cert. 19.
   Although the State presented no physical evidence at
trial, it did offer additional circumstantial evidence link-
ing Wearry to the victim. One witness testified that he
saw Wearry in the victim’s car on the night of the murder
and, later, holding the victim’s class ring. Another wit-
ness said he saw Wearry throwing away the victim’s co-
logne. In some respects, however, these witnesses contra-
dicted Scott’s account. For example, the witness who
                     Cite as: 577 U. S. ____ (2016)                    3

                              Per Curiam

reported seeing Wearry in the victim’s car did not place
Scott in the car.
   Wearry’s defense at trial rested on an alibi. He claimed
that, at the time of the murder, he had been at a wedding
reception in Baton Rouge, 40 miles away. Wearry’s girl-
friend, her sister, and her aunt corroborated Wearry’s
account. In closing argument, the State stressed that all
three witnesses had personal relationships with Wearry.
The State also presented two rebuttal witnesses: the bride
at the wedding, who reported that the reception had ended
by 8:30 or 9:00 (potentially leaving sufficient time for
Wearry to have committed the crime); and three jail em-
ployees, who testified that they had overheard Wearry say
that he was a bystander when the crime occurred.
   The jury convicted Wearry of capital murder and sen-
tenced him to death. His conviction and sentence were
affirmed on direct appeal. 1
                              B
   After Wearry’s conviction became final, it emerged that
the prosecution had withheld relevant information that
could have advanced Wearry’s plea. Wearry argued dur-
ing state postconviction proceedings that three categories
of belatedly revealed information would have undermined
the prosecution and materially aided Wearry’s defense at
trial.
   First, previously undisclosed police records showed that
two of Scott’s fellow inmates had made statements that
cast doubt on Scott’s credibility. One inmate had reported
——————
  1 Wearry argued, inter alia, that the trial court improperly denied his

for-cause challenges, and that the prosecution discriminated on the
basis of race in jury selection in violation of Batson v. Kentucky, 476
U. S. 79 (1986). Finding both jury-selection claims credible, then-
Justice Johnson dissented from the affirmance of Wearry’s conviction.
State v. Weary, 2003–3067 (La. 4/2/06), 931 So. 2d 297, 328–337.
(Wearry’s name is misspelled in the direct-appeal case caption.)
4                           WEARRY v. CAIN

                               Per Curiam

hearing Scott say that he wanted to “ ‘make sure [Wearry]
gets the needle cause he jacked over me.’ ” Id., at 22 (quot-
ing inmate affidavit). 2 The other inmate had told investi-
gators—at a meeting Scott orchestrated—that he had
witnessed the murder, but this inmate recanted the next
day. “Scott had told him what to say,” he explained, and
had suggested that lying about having witnessed the
murder “would help him get out of jail.” Pet. Exh. 13 in
No. 01–FELN–015992, pp. 104, 107. See also Pet. for
Cert. 22 (quoting police notes).
  Second, the State had failed to disclose that, contrary to
the prosecution’s assertions at trial, Brown had twice
——————
    2 Illustrative
                 of the liberties the dissent takes with the record is the
assertion that “Scott blamed [Wearry] for putting him in the position of
having to admit his own role in the events surrounding the murder.”
Post, at 2 (opinion of ALITO, J.). Introducing the inmate’s statement,
the dissent therefore suggests, might have “backfired by allowing the
prosecution to return the jury’s focus to a point the State emphasized
often during trial, namely, that Scott’s accusations were credible
precisely because Scott had no motive to tell a story that was contrary
to his own interests.” Id., at 2–3. True, according to the inmate, Scott
had complained that his identification of Wearry had resulted in a
lengthier prison term. The inmate, however, did not suggest that Scott
was angry with Wearry because he had suffered adverse consequences
as a result of Wearry’s crime. Instead, the inmate separately stated
that Scott “wouldn’t tell me who did it”—i.e., who killed Eric Walber—
“but he said I’m gonna make sure Mike gets the needle cause he jacked
over me.” Pet. Exh. 13 in No. 01–FELN–015992, p. 103. See also ibid.
(“If [Scott] would have told me who did this I would tell because I have
a heart and what they did wasn’t right”). Scott’s refusal to identify
Wearry as the culprit—while also endeavoring to “make sure Mike gets
the needle,” ibid.—suggests that Wearry did not commit the crime, but
Scott had decided to bring him down anyway. Nor, contrary to the
dissent, is there any reason to believe that Scott anticipated his partic-
ipation in this case would cost him additional years in prison. Notably,
in the first of his five accounts to police, Scott reported that he had not
been present at the time of the murder and had learned about it only
after the fact. Indeed, it is at least as plausible as the dissent’s hypoth-
esis that Scott believed implicating Wearry might win him early release
on his existing conviction.
                     Cite as: 577 U. S. ____ (2016)                    5

                              Per Curiam

sought a deal to reduce his existing sentence in exchange
for testifying against Wearry. The police had told Brown
that they would “ ‘talk to the D. A. if he told the truth.’ ”
Pet. for Cert. 19 (quoting police notes).
   Third, the prosecution had failed to turn over medical
records on Randy Hutchinson. According to Scott, on the
night of the murder, Hutchinson had run into the street to
flag down the victim, pulled the victim out of his car,
shoved him into the cargo space, and crawled into the
cargo space himself. But Hutchinson’s medical records
revealed that, nine days before the murder, Hutchinson
had undergone knee surgery to repair a ruptured patellar
tendon. Id., at 10–11, 15–16, 32. 3 An expert witness, Dr.
Paul Dworak, testified at the state collateral-review hear-
ing that Hutchinson’s surgically repaired knee could not
have withstood running, bending, or lifting substantial
weight. The State presented an expert witness who disa-
greed with Dr. Dworak’s appraisal of Hutchinson’s physi-
cal fitness.
   During state postconviction proceedings, Wearry also
maintained that his trial attorney had failed to uncover
exonerating evidence. Wearry’s trial attorney admitted at
the state collateral-review hearing that he had conducted
no independent investigation into Wearry’s innocence and
had relied solely on evidence the State and Wearry had
provided. 4 For example, despite Wearry’s alibi, his attor-
——————
  3 The  dissent emphasizes a State’s witness’ testimony that
“Hutchinson had had surgery on his knee ‘about nine days before the
homicide happened.’ ” Post, at 4 (quoting 10 Record 2261 (Tr., Mar. 5,
2002)). But from this witness’ statement, neither Wearry nor the jury
had any way of knowing what the medical records would have revealed:
Hutchinson had undergone a patellar-tendon repair rather than a
routine minor procedure.
  4 Wearry’s trial attorney did ask the public defender’s investigator to

look into the backgrounds of the State’s witnesses and to speak with
Wearry’s family members. But the attorney testified at the collateral-
review hearing that he did not know what persons the investigator
6                          WEARRY v. CAIN

                              Per Curiam

ney undertook no effort to locate independent witnesses
from among the dozens of guests who had attended the
wedding reception.
   Counsel representing Wearry on collateral review con-
ducted an independent investigation. This investigation
revealed many witnesses lacking any personal relation-
ship with Wearry who would have been willing to corrobo-
rate his alibi had they been called at trial. Collateral-
review counsel’s investigation also revealed that Scott’s
brother and sister-in-law would have been willing to tes-
tify at trial, as they did at the collateral-review hearing,
that Scott was with them, mostly at a strawberry festival,
until around 11:00 on the night of the murder.
   Based on this new evidence, Wearry alleged violations of
his due process rights under Brady v. Maryland, 373 U. S.
83 (1963), and of his Sixth Amendment right to effective
assistance of counsel. Acknowledging that the State
“probably ought to have” disclosed the withheld evidence,
App. to Pet. for Cert. B–6, and that Wearry’s counsel
provided “perhaps not the best defense that could have
been rendered,” id., at B–5, the postconviction court de-
nied relief. Even if Wearry’s constitutional rights were
violated, the court concluded, he had not shown prejudice.
Id., at B–5, B–7. In turn, the Louisiana Supreme Court
also denied relief. Id., at A–1. Chief Justice Johnson
would have granted Wearry’s petition on the ground that
he received ineffective assistance of counsel. Id., at A–2. 5

——————
contacted and, in any event, he had serious doubts about the investiga-
tor’s qualifications and competence. Moreover, there is no indication
that the investigator ever engaged in inquiries regarding Scott’s back-
ground or his whereabouts on the night of the murder.
  5 Justice Crichton would have granted Wearry’s petition and remanded

for the trial court to address his claim of intellectual disability under
Atkins v. Virginia, 536 U. S. 304 (2002). App. to Pet. for Cert. A–15.
Wearry does not raise his Atkins claim in his petition for a writ of
certiorari.
                     Cite as: 577 U. S. ____ (2016)                    7

                              Per Curiam

                              II
   Because we conclude that the Louisiana courts’ denial of
Wearry’s Brady claim runs up against settled constitu-
tional principles, and because a new trial is required as a
result, we need not and do not consider the merits of his
ineffective-assistance-of-counsel claim. “[T]he suppression
by the prosecution of evidence favorable to an accused
upon request violates due process where the evidence is
material either to guilt or to punishment, irrespective of
the good faith or bad faith of the prosecution.” Brady,
supra, at 87. See also Giglio v. United States, 405 U. S.
150, 153–154 (1972) (clarifying that the rule stated in
Brady applies to evidence undermining witness credibil-
ity). Evidence qualifies as material when there is “ ‘any
reasonable likelihood’ ” it could have “ ‘affected the judg-
ment of the jury.’ ” Giglio, supra, at 154 (quoting Napue v.
Illinois, 360 U. S. 264, 271 (1959)). To prevail on his
Brady claim, Wearry need not show that he “more likely
than not” would have been acquitted had the new evidence
been admitted. Smith v. Cain, 565 U. S. 73, ___–___
(2012) (slip op., at 2–3) (internal quotation marks and
brackets omitted). He must show only that the new evi-
dence is sufficient to “undermine confidence” in the ver-
dict. Ibid. 6
   Beyond doubt, the newly revealed evidence suffices to
undermine confidence in Wearry’s conviction. The State’s
trial evidence resembles a house of cards, built on the jury
crediting Scott’s account rather than Wearry’s alibi. See
United States v. Agurs, 427 U. S. 97, 113 (1976) (“[I]f the
verdict is already of questionable validity, additional
evidence of relatively minor importance might be suffi-
cient to create a reasonable doubt.”). The dissent asserts
——————
  6 Given this legal standard, Wearry can prevail even if, as the dissent

suggests, the undisclosed information may not have affected the jury’s
verdict.
8                          WEARRY v. CAIN

                               Per Curiam

that, apart from the testimony of Scott and Brown, there
was independent evidence pointing to Wearry as the mur-
derer. See post, at 5 (opinion of ALITO, J.). But all of the
evidence the dissent cites suggests, at most, that someone
in Wearry’s group of friends may have committed the
crime, and that Wearry may have been involved in events
related to the murder after it occurred. Perhaps, on the
basis of this evidence, Louisiana might have charged
Wearry as an accessory after the fact. La. Rev. Stat. Ann.
§14:25 (West 2007) (providing a maximum prison term of
five years for accessories after the fact). But Louisiana
instead charged Wearry with capital murder, and the only
evidence directly tying him to that crime was Scott’s dubi-
ous testimony, corroborated by the similarly suspect tes-
timony of Brown. 7
   As the dissent recognizes, “Scott did not have an exem-
plary record of veracity.” Post, at 3. Scott’s credibility,
already impugned by his many inconsistent stories, would
have been further diminished had the jury learned that
Hutchinson may have been physically incapable of per-
forming the role Scott ascribed to him, that Scott had
coached another inmate to lie about the murder and
thereby enhance his chances to get out of jail, or that Scott
may have implicated Wearry to settle a personal score. 8
——————
  7 As for the three jailers who testified to overhearing Wearry call

himself an “innocent bystander,” post, at 4, so characterizing oneself is
the opposite of an admission of guilt.
  8 Because the inmate who told police that Scott may have wanted to

settle a score did so close to the end of trial, the State argues, the
inmate’s “statement was probably . . . never seen by anyone involved
with the actual trial until . . . it was [all] over, i[f] at all.” Brief in
Opposition 18. But “Brady suppression occurs when the government
fails to turn over even evidence that is known only to police investiga-
tors and not to the prosecutor.” Youngblood v. West Virginia, 547 U. S.
867, 869–870 (2006) (per curiam) (internal quotation marks omitted).
See also Kyles v. Whitley, 514 U. S. 419, 438 (1995) (rejecting Louisi-
ana’s plea for a rule that would not hold the State responsible for
                     Cite as: 577 U. S. ____ (2016)                     9

                              Per Curiam

Moreover, any juror who found Scott more credible in light
of Brown’s testimony might have thought differently had
she learned that Brown may have been motivated to come
forward not by his sister’s relationship with the victim’s
sister—as the prosecution had insisted in its closing ar-
gument—but by the possibility of a reduced sentence on
an existing conviction. See Napue, supra, at 270 (even
though the State had made no binding promises, a wit-
ness’ attempt to obtain a deal before testifying was mate-
rial because the jury “might well have concluded that [the
witness] had fabricated testimony in order to curry the
[prosecution’s] favor”). Even if the jury—armed with all of
this new evidence—could have voted to convict Wearry, we
have “no confidence that it would have done so.” Smith,
supra, at ___ (slip op., at 3).
   Reaching the opposite conclusion, the state postconvic-
tion court improperly evaluated the materiality of each
piece of evidence in isolation rather than cumulatively, see
Kyles v. Whitley, 514 U. S. 419, 441 (1995) (requiring a
“cumulative evaluation” of the materiality of wrongfully
withheld evidence), emphasized reasons a juror might
disregard new evidence while ignoring reasons she might
not, cf. Porter v. McCollum, 558 U. S. 30, 43 (2009) (per
curiam) (“it was not reasonable to discount entirely the
effect that [a defendant’s expert’s] testimony might have
had on the jury” just because the State’s expert provided
contrary testimony), and failed even to mention the state-
ments of the two inmates impeaching Scott.
                             III
  In addition to defending the judgment of the Louisiana
courts, the dissent criticizes the Court for deciding this
“intensely factual question . . . without full briefing and
——————
failing to disclose exculpatory evidence about which prosecutors did not
learn until after trial when that evidence was in the possession of police
investigators at the time of trial).
10                     WEARRY v. CAIN

                          Per Curiam

argument.” Post, at 6. But the Court has not shied away
from summarily deciding fact-intensive cases where, as
here, lower courts have egregiously misapplied settled
law. See, e.g., Mullenix v. Luna, ante, at ___ (per
curiam); Stanton v. Sims, 571 U. S. ___ (2013) (per curiam);
Parker v. Matthews, 567 U. S. ___ (2012) (per curiam);
Coleman v. Johnson, 566 U. S. ___ (2012) (per curiam);
Wetzel v. Lambert, 565 U. S. ___ (2012) (per curiam);
Ryburn v. Huff, 565 U. S. ___ (2012) (per curiam); Sears v.
Upton, 561 U. S. 945 (2010) (per curiam); Porter v.
McCollum, supra.
   Because “[t]he petition does not . . . fall into a category
in which the Court has previously evinced an inclination
to police factbound errors,” the dissent continues, “nothing
warned the State,” when it was drafting its brief in opposi-
tion, that the Court might summarily reverse Wearry’s
conviction. Post, at 5–6. Contrary to the dissent, however,
summarily deciding a capital case, when circumstances so
warrant, is hardly unprecedented. See Sears, supra, at
951–952 (vacating a state postconviction court’s denial of
relief on a penalty-phase ineffective-assistance-of-counsel
claim); Porter, supra, at 38–40 (attorney provided ineffec-
tive assistance of counsel by conducting a constitutionally
inadequate investigation into mitigating evidence). Per-
haps anticipating the possibility of summary reversal, the
State devoted the bulk of its 30-page brief in opposition to
a point-by-point rebuttal of Wearry’s claims. Given this
brief, as well as the State’s lower court filings similarly
concentrating on evidence supporting its position, the
chances that further briefing or argument would change
the outcome are vanishingly slim.
   The dissent also inveighs against the Court’s “de-
part[ure] from our usual procedures . . . [to] decide peti-
tioner’s fact-intensive Brady claim at this stage . . . [rather
than] allow[ing] petitioner to raise that claim in a federal
habeas proceeding.” Post, at 7. This Court, of course, has
                 Cite as: 577 U. S. ____ (2016)                 11

                          Per Curiam

jurisdiction over the final judgments of state postconvic-
tion courts, see 28 U. S. C. §1257(a), and exercises that
jurisdiction in appropriate circumstances. Earlier this
Term, for instance, we heard argument in Foster v. Chat-
man, No. 14–8349, which involves the Georgia courts’
denial of postconviction relief to a capital defendant rais-
ing a claim under Batson v. Kentucky, 476 U. S. 79 (1986).
See also Smith, 565 U. S., at ___ (slip op., at 2) (reversing
a state postconviction court’s denial of relief on a Brady
claim); Sears, supra, at 946. Reviewing the Louisiana
courts’ denial of postconviction relief is thus hardly the
bold departure the dissent paints it to be. The alternative
to granting review, after all, is forcing Wearry to endure
yet more time on Louisiana’s death row in service of a
conviction that is constitutionally flawed.
                       *     *    *
  Because Wearry’s due process rights were violated, we
grant his petition for a writ of certiorari and motion for
leave to proceed in forma pauperis, reverse the judgment
of the Louisiana postconviction court, and remand for
further proceedings not inconsistent with this opinion.

                                                  It is so ordered.
                 Cite as: 577 U. S. ____ (2016)           1

                     ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
     MICHAEL WEARRY v. BURL CAIN, WARDEN
  ON PETITION FOR WRIT OF CERTIORARI TO THE DISTRICT
        COURT OF LOUISIANA, LIVINGSTON PARISH
             No. 14–10008.   Decided March 7, 2016

   JUSTICE ALITO, with whom JUSTICE THOMAS joins,
dissenting.
   Without briefing or argument, the Court reverses a 14-
year-old murder conviction on the ground that the prose-
cution violated Brady v. Maryland, 373 U. S. 83 (1963), by
failing to turn over certain information that tended to
exculpate petitioner. There is no question in my mind
that the prosecution should have disclosed this infor-
mation, but whether the information was sufficient to
warrant reversing petitioner’s conviction is another mat-
ter. The failure to turn over exculpatory information
violates due process only “ ‘if there is a reasonable proba-
bility that, had the evidence been disclosed to the defense,
the result of the proceeding would have been different.’ ”
Kyles v. Whitley, 514 U. S. 419, 433–434 (1995) (quoting
United States v. Bagley, 473 U. S. 667, 682 (1985) (opinion
of Blackmun, J.)).
   The Court argues that the information in question here
could have affected the jury’s verdict and that petitioner’s
conviction must therefore be reversed. The Court ably
makes the case for reversal, but there is a reasonable
contrary argument that petitioner’s conviction should
stand because the undisclosed information would not have
affected the jury’s verdict. I will briefly discuss the main
points made in the per curiam, not for the purpose of
showing that they are necessarily wrong, but to show that
the Brady issue is not open and shut. For good reason, we
generally do not decide cases without allowing the parties
to file briefs and present argument. Questions that seem
2                     WEARRY v. CAIN

                     ALITO, J., dissenting

quite simple at first glance sometimes look very different
after both sides are given a chance to make their case. Of
course, this process means extra work for the Court. But
it leads to better results, and it gives the losing side the
satisfaction of knowing that at least its arguments have
been fully heard. There is no justification for departing
from our usual procedures in this case.
                              I
   The first item of information discussed by the Court is a
police report that recounts statements made about Sam
Scott, a key witness for the prosecution, by a fellow in-
mate. According to this report, Scott told the inmate: “I’m
gonna make sure Mike [i.e., petitioner] gets the needle
cause he jacked over me.” Pet. Exh. 13 in No. 01–FELN–
015992, p. 103. Scott, who had been serving a sentence on
unrelated drug charges, reportedly told the inmate that he
had been expecting to be released but that he “still [had
not] gone home because of this,” i.e., petitioner’s prosecu-
tion. Id., at 102. As stated in the report, Scott said that
he was now facing the possibility of a 10-year sentence,
apparently for his admitted role in the events surrounding
the murder. The report did not provide any further expla-
nation for Scott’s alleged statement that petitioner had
“jacked [him] over.”
   The Court reads the report to suggest that Scott impli-
cated petitioner in the murder “to settle a personal score.”
Ante, at 8. But if petitioner’s counsel had actually at-
tempted to use this evidence at trial, the net effect might
well have been harmful, not helpful, to the defense. The
undisclosed police report on which the Court relies may be
read to mean that Scott blamed petitioner for putting him
in the position of having to admit his own role in the
events surrounding the murder and thereby expose him-
self to the 10-year sentence and lose an opportunity to
secure early release from prison on the drug charges. If
                    Cite as: 577 U. S. ____ (2016)                   3

                         ALITO, J., dissenting

defense counsel had attempted to impeach Scott with this
police report, the effort could have backfired by allowing
the prosecution to return the jury’s focus to a point the
State emphasized often during trial, namely, that Scott’s
accusations were credible precisely because Scott had no
motive to tell a story that was contrary to his own inter-
ests. See, e.g., 10 Record 2307 (Tr., Mar. 5, 2002) (“If
[Scott] keeps his mouth shut, he is out in less than five
more months. . . . [But] [i]nstead of getting out in 180
days, he is going to be doing more time”). 1
   The Court next turns to an allegation that Scott had
coached another prisoner to make up lies against peti-
tioner. This prisoner never testified at trial, and there is a
basis for arguing that this information would not have
made a difference to the jury, which was well aware that
Scott did not have an exemplary record of veracity. Scott
himself admitted to fabricating information that he told
the police during their investigations. In addition, a wit-
ness who did testify against petitioner at trial also ac-
cused Scott of asking him to lie, although admittedly this
witness later denied making this accusation. Given that
the jury convicted even with these quite serious strikes
against Scott’s credibility, there is reason to question
whether the jury would have seriously considered a differ-
ent verdict because of an accusation from someone who
never took the stand.
   Third, the Court observes that the prosecution failed to
turn over evidence that another witness, Eric Brown, had
——————
  1 The  majority claims that Scott’s unwillingness to tell this fellow
inmate who killed the victim somehow exculpates petitioner. See ante,
at 4, n. 2. In my view, one cannot reasonably infer from the inmate’s
statement, “[Scott] wouldn’t tell me who did it but he said I’m gonna
make sure Mike gets the needle cause he jacked over me,” that Scott
believed petitioner Michael Wearry to be innocent—especially against
the backdrop of Scott’s complaints about his increased imprisonment.
Pet. Exh. 13 in No. 01–FELN–015992, p. 103.
4                         WEARRY v. CAIN

                         ALITO, J., dissenting

asked for favorable treatment from the district attorney in
exchange for testifying against petitioner. It is true—and
troubling—that the prosecutor claimed in her opening
statement that Brown had not sought favorable treatment.
But even so, it is far from clear that disclosing the contra-
dictory information had real potential to affect the trial’s
outcome. For one thing, there is no evidence that Brown
(unlike Scott) actually received any deal, despite defense
counsel’s efforts in cross-examination to establish that
Brown’s testimony might have earned him leniency from
the State. Moreover, Brown admitted during the ex-
change that he had manipulated his initial story to the
police to avoid implicating himself in criminal activity.
We know, then, that the jury harbored no illusions about
the purity of Brown’s motives, notwithstanding the prose-
cutor’s opening misstatement.
  Finally, the Court says that the medical records of
Randy Hutchinson would have cast doubt on Scott’s trial
testimony that Hutchinson repeatedly dragged the victim
into and out of a car and bludgeoned him with a stick.
The records reveal that Hutchinson had knee surgery to
repair his patellar tendon just nine days before the mur-
der. But one of the State’s witnesses testified at trial that
he had seen records showing that Hutchinson had had
surgery on his knee “about nine days before the homicide
happened.” 10 Record 2261 (Tr., Mar. 5, 2002); see also
id., at 2263. The jury thus knew the most salient fact
revealed by these records—that Scott had attributed
significant strength and mobility to a man nine days
removed from knee surgery. 2 Given that these particular
——————
  2 The per curiam argues that the medical records might have had a

greater effect on the jury because they mentioned the particular type of
knee surgery that petitioner had undergone, and that is certainly
possible. But what is important at this stage is that the basic fact—
that petitioner had recently undergone knee surgery—was known to
the jury, and the incremental impact of the additional details supplied
                    Cite as: 577 U. S. ____ (2016)                  5

                         ALITO, J., dissenting

details about Hutchinson’s actions were a relatively minor
part of Scott’s account of the crime and the State’s case
against petitioner, the significance of the undisclosed
medical records is subject to reasonable dispute.
   While the Court highlights the exculpatory quality of
the withheld information, the Court downplays the con-
siderable evidence of petitioner’s guilt. Aside from Scott’s
and Brown’s testimony, three witnesses told the jury that
they saw petitioner and others driving around shortly
after the murder in the victim’s red car, which according
to one of these witnesses had blood on its exterior. Peti-
tioner offered to sell an Albany High School class ring to
one of these witnesses and a set of new speakers to an-
other. The third witness said he saw petitioner throw away a
bottle of Tommy Hilfiger cologne. Meanwhile, the victim’s
mother testified that her son wore an Albany High class
ring that was not recovered with his body, had received
speakers as a gift shortly before his murder, and had a
bottle of Tommy Hilfiger cologne with him on the night
when he was killed. In addition, three jailers testified
that petitioner called his father after his eventual arrest
and stated that “he didn’t know what he was doing in jail
because he didn’t do anything [and] was just an innocent
bystander.” 9 Record 2120 (Tr., Mar. 4, 2002); see also id.,
at 2124, 2126.
   In short, this is far from a case in which the withheld
information would have allowed the defense to undermine
“the only evidence linking [petitioner] to the crime.”
Smith v. Cain, 565 U. S. 73, ___ (2012) (slip op., at 3).
                            II
  Whether disclosing the information at issue realistically
——————
by the medical records is far from clear. Even at the postconviction
evidentiary hearing, the defense’s and State’s medical experts disa-
greed about whether the particular procedure at issue would have left
the then-20-year-old Hutchinson incapable of the acts Scott described.
6                     WEARRY v. CAIN

                      ALITO, J., dissenting

could have changed the trial’s outcome is indisputably an
intensely factual question. Under Brady, we must evalu-
ate the significance of the withheld information in light of
all the proof at petitioner’s trial. See Kyles, 514 U. S., at
435 (Brady is violated when the withheld “evidence could
reasonably be taken to put the whole case in such a differ-
ent light as to undermine confidence in the verdict” (em-
phasis added)); United States v. Agurs, 427 U. S. 97, 112
(1976) (Brady materiality “must be evaluated in the con-
text of the entire record” (emphasis added)). It is unusual
and, in my judgment, unreasonable for us to decide such a
question without full briefing and argument.
   At this stage, all that we have from the State is its brief
in opposition to the petition for certiorari. And the State
had ample reason to believe when it submitted that brief
that the question on the table was whether the Court
should hear the case, not whether petitioner’s conviction
should be reversed. The State undoubtedly knew that we
generally deny certiorari on factbound questions that do
not implicate any disputed legal issue. See, e.g., this
Court’s Rule 10; S. Shapiro, K. Geller, T. Bishop, E. Hart-
nett, & D. Himmelfarb, Supreme Court Practice
§5.12(c)(3), p. 352 (10th ed. 2013). Nothing warned the
State that this petition was likely to produce an exception
to that general rule. The petition does not, for instance,
fall into a category in which the Court has previously
evinced an inclination to police factbound errors. Cf. Cash
v. Maxwell, 565 U. S. ____, ____ (2012) (Scalia, J., dissent-
ing from denial of certiorari) (slip op., at 8) (listing cases
from one such category).
   To the contrary, we have previously told litigants that
petitions like the one here, challenging a state court’s
denial of postconviction relief, are particularly unlikely to
be granted: We “ ‘rarely gran[t] review at this stage’ ” of
litigation, even when a petition raises “ ‘arguably meritori-
ous federal constitutional claims,’ ” because we prefer that
                     Cite as: 577 U. S. ____ (2016)                     7

                          ALITO, J., dissenting

the claims be reviewed first by a district court and court of
appeals in a federal habeas proceeding. Lawrence v. Flor-
ida, 549 U. S. 327, 335 (2007) (quoting Kyles v. Whitley,
498 U. S. 931, 932 (1990) (Stevens, J., concurring in denial
of stay of execution)). 3
   Why, then, has the Court decided to depart from our
usual procedures and decide petitioner’s fact-intensive
Brady claim at this stage? Why not allow petitioner to
raise that claim in a federal habeas proceeding? If the
case took that course, it would not reach us until a district
court and a court of appeals had studied the record and
evaluated the likely impact of the information in question.
   One consequence of waiting until the claim was raised
in a federal habeas proceeding is that our review would
then be governed by the Antiterrorism and Effective
Death Penalty Act of 1996 (AEDPA). Under AEDPA,
relief could be granted only if it could be said that the
state court’s rejection of the claim represented an “unrea-
sonable application” of Brady. 28 U. S. C. §2254(d)(1). By
intervening now before AEDPA comes into play, the Court
avoids the application of that standard and is able to
exercise plenary review. But if the Brady claim is as open-
and-shut as the Court maintains, AEDPA would not pre-
sent an obstacle to the granting of habeas relief. On the
other hand, if reasonable jurists could disagree about the
application of Brady to the facts of this case, there is no
good reason to dispose of this case summarily. The State
——————
   3 The Court implies that meritorious claims in capital cases do consti-

tute a category of factbound errors that the Court has shown willing-
ness to correct on certiorari papers alone. Ante, at 10. In support, it
cites Sears v. Upton, 561 U. S. 945 (2010) (per curiam), and Porter v.
McCollum, 558 U. S. 30 (2009) (per curiam). Notably, Porter did not
arise directly from state postconviction proceedings, but in federal
habeas. And in neither case did the Court take the dramatic step it
takes here and summarily reverse a long-final state conviction for
capital murder; both cases addressed errors related to the defendants’
sentences.
8                    WEARRY v. CAIN

                     ALITO, J., dissenting

should be given the opportunity to make its full case.
  In my view, therefore, summary reversal is highly inap-
propriate. The Court is anxious to vacate petitioner’s
conviction before the State has the opportunity to make its
case. But if we are going to intervene at this stage, we
should grant the petition and hear the case on the merits.
There is room on our docket to give this case the careful
consideration it deserves.

```

---

## GROUP: _overhaul2/lake/cases/Weatherford v. Bursey.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Weatherford v. Bursey
type: case
citation: "429 U.S. 545 (1977)"
parallel_cite: "97 S. Ct. 837; 51 L. Ed. 2d 30"
neutral_cite: 1977 U.S. LEXIS 40
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-02-22
docket: No. 76-446
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
  opinion_url: "https://www.courtlistener.com/opinion/109590/weatherford-v-bursey/"
  cluster_id: 109590
  opinion_id: null
  identity_checked: true
lake:
  record_id: Weatherford v. Bursey
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: Anchor
related:
  - "[[Sixth Amendment Right to Counsel]]"
  - "[[Hoffa v. United States]]"
  - "[[Massiah v. United States]]"
  - "[[United States v. Henry]]"
  - "[[Kansas v. Ventris]]"
tags:
  - case
  - sixth-amendment
  - right-to-counsel
  - undercover-informant
  - attorney-client
  - section-1983
holding: "The presence of a government undercover agent at defense meetings does not per se violate the Sixth Amendment right to counsel; there is no violation absent tainted evidence, communication of defense strategy to the prosecution (creating a realistic possibility of injury to the defendant or benefit to the State), or purposeful intrusion — none of which occurred where the agent attended at the defense's own invitation, sought no information, and conveyed nothing about the defense to the prosecutors."
aliases:
  - Weatherford v. Bursey
  - "Weatherford v. Bursey (1977)"
---

# Weatherford v. Bursey

*429 U.S. 545 (1977)* (No. 75-1510) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 109590 → combined opinion 109590 (White, J.; 429 U.S. 545, argued Dec. 7, 1976, decided Feb. 22, 1977). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*558`). S9 promotes. -->

## Background
Weatherford, an undercover South Carolina agent, took part with Bursey in vandalizing a Selective Service office and was arrested alongside him to preserve his cover. At the invitation of Bursey and his lawyer, Weatherford twice attended meetings where the coming trial was discussed, but the trial court found he never sought information and never passed anything about Bursey's defense to his superiors or the prosecutor. On the day of trial Weatherford was unexpectedly called as a prosecution witness and gave damaging eyewitness testimony about the vandalism (not about the defense meetings). After his conviction, Bursey sued under 42 U.S.C. § 1983, claiming the meetings had deprived him of effective assistance of counsel. The District Court found for the agents; the Fourth Circuit reversed, adopting a [[Common Legal Terms#per-se|per se]] rule that any prosecution intrusion into the attorney-client relationship requires a new trial.

## Issue
Whether an undercover agent's attendance at meetings between a defendant and his counsel, standing alone, deprives the defendant of the effective assistance of counsel guaranteed by the Sixth and Fourteenth Amendments.

## Rule
The Court rejected the Fourth Circuit's [[Common Legal Terms#per-se|per se]] rule as sweeping too broadly, because many such encounters cause no conceivable prejudice. A Sixth Amendment violation instead depends on the presence of concrete harm, and here there was none: "There being no tainted evidence in this case, no communication of defense strategy to the prosecution, and no purposeful intrusion by Weatherford, there was no violation of the Sixth Amendment insofar as it is applicable to the States by virtue of the Fourteenth Amendment." — 429 U.S. at 558. ^pin-558

## Application
The key was that Weatherford never communicated the substance of the defense meetings to the prosecution, so his mere presence created no realistic possibility of injury to Bursey or benefit to the State — the situation the Court had left open in *[[Hoffa v. United States|Hoffa]]*. Nor did his trial testimony change the analysis: it concerned only the vandalism and drew nothing from the meetings. The Court likewise rejected a due-process theory built on *[[Brady v. Maryland|Brady]]*, holding that the prosecution had no obligation to disclose in advance that an informant would testify, since there is no general constitutional right to criminal discovery.

## Conclusion
The judgment of the Court of Appeals for the Fourth Circuit was **reversed** (reinstating the District Court's judgment for the agents). White, J., delivered the opinion of the Court. Marshall, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Brennan, J., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Weatherford* anchors the rule that government intrusion into the attorney-client relationship violates the Sixth Amendment only on a showing of prejudice — communication of defense strategy, use of tainted evidence, or purposeful intrusion — not automatically. Teach it within the deliberate-elicitation line of *[[Massiah v. United States]]*, *[[United States v. Henry]]*, and *[[Kansas v. Ventris]]* as the case that declined a [[Common Legal Terms#per-se|per se]] remedy for informant presence at defense meetings.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Anchor*

## Sources
- [*Weatherford v. Bursey*, 429 U.S. 545 (1977)](https://www.courtlistener.com/opinion/109590/weatherford-v-bursey/) — pinpoint: 558 (White, J., for the Court; the CL opinion text carries the reporter star `*558` in the paragraph preceding the quoted holding, which sits before the star `*559`, i.e., on page 558). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "317b7cb3d83d4701", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Weatherford v. Bursey"}, "payload": {"all": [{"cite": "429 U.S. 545", "page": "545", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "429"}, {"cite": "97 S. Ct. 837", "page": "837", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "51 L. Ed. 2d 30", "page": "30", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "51"}, {"cite": "1977 U.S. LEXIS 40", "page": "40", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "429 U.S. 545", "official": {"cite": "429 U.S. 545", "page": "545", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "429"}, "official_selection_present": true, "record_id": "Weatherford v. Bursey"}}
{"assertion_id": "99002887f4044ee6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Weatherford v. Bursey"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Weatherford v. Bursey", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Weatherford v. Bursey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Weatherford v. Bursey",
  "status": "under_review",
  "identity": {
    "case_name": "Weatherford v. Bursey",
    "case_name_short": "Weatherford",
    "case_name_full": "WEATHERFORD, AGENT OF THE SOUTH CAROLINA LAW ENFORCEMENT DIVISION, Et Al. v. BURSEY",
    "input_case_name": "Weatherford v. Bursey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-02-22",
    "year": 1977,
    "docket": "No. 76-446",
    "cluster_id": 109590,
    "lead_opinion_id": 9426656,
    "sibling_ids": [],
    "absolute_url": "/opinion/109590/weatherford-v-bursey/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "429 U.S. 545",
      "volume": "429",
      "reporter": "U.S.",
      "page": "545",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 837",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "837",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 L. Ed. 2d 30",
        "volume": "51",
        "reporter": "L. Ed. 2d",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 40",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "429 U.S. 545",
        "volume": "429",
        "reporter": "U.S.",
        "page": "545",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 837",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "837",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 L. Ed. 2d 30",
        "volume": "51",
        "reporter": "L. Ed. 2d",
        "page": "30",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 40",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "40",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "429 U.S. 545",
    "official_selection": {
      "court_class": "scotus",
      "selected": "429 U.S. 545",
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
    "date_created": "2026-07-06T13:45:14Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:24Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "weatherford-v-bursey--109590",
      "to_record_id": "Weatherford v. Bursey",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Weatherford v. Bursey

```
<opinion type="majority">
<author id="b697-5">Mk. Justice White</author>
<p id="AP3o">delivered the opinion of the Court.</p>
<p id="b697-6">The issue here is whether in the circumstances present in this case the conduct of an undercover agent for a state law enforcement agency deprived respondent Bursey of his right to the effective assistance of counsel guaranteed him by the Sixth and Fourteenth Amendments of the United States Constitution or deprived him of due process of law in violation of the Fourteenth Amendment.</p>
<p id="b697-7">I</p>
<p id="b697-8">This case began when respondent Bursey filed suit under <span class="citation no-link">42 U. S. C. § 1983</span> against petitioners Weatherford and Strom, respectively an undercover agent for and the head of the South Carolina State Law Enforcement Division, asserting that the defendants had deprived him of certain constitutional rights. The case was tried without a jury. The following facts are taken from the District Court’s findings, which were not disturbed by the Court of Appeals.</p>
<p id="b697-9">During the early morning hours of March 20, 1970, Bursey and Weatherford, along with two others, vandalized the offices of the Richland County Selective Service in Columbia, S. C. Police were advised of the incident by Weatherford, who, in order to maintain his undercover status and his capability of working on other current matters in that capacity, was arrested and charged along with Bursey. Weatherford was immediately released on bond and, continuing the masquerade, retained an attorney, Frank Taylor, Sr. Bursey, who was later released on bond, retained his own counsel, C. Rauch Wise.</p>
<p id="b697-10">On two occasions thereafter and prior to trial, Weather-ford met with Bursey and Wise, and the approaching trial <page-number citation-index="1" label="548">*548</page-number>was discussed. With respect to these meetings, the District Court found as follows:</p>
<blockquote id="b698-5">“On neither of these occasions did the defendant Weatherford seek information from the plaintiff or his attorney, and on neither occasion did he initiate or ask for the meeting. He was brought into the meetings by the plaintiff and plaintiff’s attorney in an effort to obtain information, ideas or suggestions as to the plaintiff’s defense. From the beginning Weatherford advised plaintiff and plaintiff’s attorney that Weatherford would obtain a severance of his case from that of the plaintiff. This severance was to be upon the ground that Weatherford might be prejudiced in going to trial with Bursey as a codefendant, because of Bursey’s reputation and participation in other activities which had been covered by the news media. On no occasion did Bursey or his attorney question the granting of a severance, nor did they seem to concern themselves with whether the prosecutor would consent to a severance, although such consent is quite unusual where codefendants are charged with the same crime and proof will be from the same witnesses based upon identical facts. At those meetings between plaintiff, plaintiff’s attorney and defendant Weatherford the plaintiff and his attorney raised the question of a possible informer being used to prove the case, but they never asked Weatherford if he were an informer and he never specifically denied being an informer, since he was never asked or accused.” App. 248-249.</blockquote>
<p id="b698-6">At no time did Weatherford discuss with or pass on to his superiors or to the prosecuting attorney or any of the attorney’s staff “any details or information regarding the plaintiff’s trial plans, strategy, or anything having to do with the criminal action pending against plaintiff.” <span class="citation no-link"><em>Id., </em>at 249</span>. Until the <page-number citation-index="1" label="549">*549</page-number>day of trial the prosecuting attorney did not plan to use Weatherford as a witness. Consequently, until then, Weatherford had not expected to be a witness and had anticipated continuing his undercover work. However, Weatherford had lost some of his effectiveness as an agent in the weeks preceding trial because he had been seen in the company of police officers, and he was called for the prosecution. He testified as to his undercover activities and gave an eyewitness account of the events of March 20, 1970. Bursey took the stand, was convicted, and then disappeared until apprehended some two years later, at which time he was incarcerated and forced to serve his 18-month sentence.</p>
<p id="b699-5">Bursey then began this § 1983 action, alleging that Weatherford had communicated to his superiors and prosecuting officials the defense strategies and plans which he had learned at his meetings with Bursey and Wise, thereby depriving Bursey of the effective assistance of counsel to which he was entitled under the Sixth and Fourteenth Amendments as well as of his right to a fair trial guaranteed him by the Due Process Clause of the Fourteenth Amendment. The District Court found for the defendants in all respects and entered judgment accordingly.</p>
<p id="b699-6">The Court of Appeals for the Fourth Circuit reversed, <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d 483</a></span> (1975), concluding that “on the facts as found by the district court Bursey’s rights to effective assistance of counsel and a fair trial were violated.” <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#486" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually..."><em>Id., </em>at 486</a></span>. The Court of Appeals held that “whenever the prosecution knowingly arranges or permits intrusion into the attorney-client relationship the right to counsel is sufficiently endangered to require reversal and a new trial.” <em><span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">Ibid.</a></span> </em>That the intrusion occurred in order to prevent revealing Weather-ford’s identity as an undercover agent was immaterial. The Court of Appeals thought that Weatherford was himself “a member of the prosecution,” <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#487" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually..."><em>id., </em>at 487</a></span>, and that therefore it was also immaterial that he had not informed other <page-number citation-index="1" label="550">*550</page-number>officials about what was said or done in the two meetings with Bursey and Wise.</p>
<p id="b700-5">In addition, the Court of Appeals concluded that Bursey had been denied due process of law under <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), by concealment of Weatherford’s identity until the day of trial and by Weatherford’s statement that he would not be a witness, all of which lulled Bursey into a false sense of security and interfered with his preparations for trial. The judgment of the District Court was reversed, but the remand for further proceedings would have allowed Weatherford and Strom to present a qualified immunity defense under <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975).</p>
<p id="b700-6">We granted the petition for certiorari filed by Weatherford and Strom, who are represented by the State Attorney General. <span class="citation" data-id="9001254"><a href="/opinion/9008466/smith-v-united-states/" aria-description="Citation for case: Smith v. United States">426 U. S. 946</a></span> (1976). We reverse.</p>
<p id="b700-7">II</p>
<p id="b700-8">The exact contours of the Court of Appeals’ <em>per se </em>right-to-counsel rule are difficult to discern; but as the Court of Appeals applied the rule in this case, it would appear that if an undercover agent meets with a criminal defendant who is awaiting trial and with hi.s attorney and if the forthcoming trial is discussed without the agent’s revealing his identity, a violation of the defendant’s constitutional rights has occurred, whatever was the purpose of the agent in attending the meeting, whether or not he reported on the meeting to his superiors, and whether or not any specific prejudice to the defendant’s preparation for or conduct of the trial is demonstrated or otherwise threatened. The Court of Appeals was of the view, <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#486" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d, at 486</a></span>, that this Court “establish [ed] such a per se rule” in <em>Black </em>v. <em>United States, </em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">385 U. S. 26</a></span> (1966), and <em>O’Brien </em>v. <em>United States, </em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">386 U. S. 345</a></span> (1967). The Court of Appeals also relied on <em>Hoffa </em>v. <em>United States, </em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293</a></span> (1966).</p>
<p id="b701-4"><page-number citation-index="1" label="551">*551</page-number>We cannot agree that these cases, individually or together, either require or suggest the rule announced by the Court of Appeals and now urged by Bursey. Both <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span> </em>and <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span> </em>involved surreptitious electronic surveillance by the Government, which was discovered after trial and conviction and which was plainly illegal under the Fourth Amendment.<footnotemark>1</footnotemark> In each case, some, but not all, of the conversations overheard were between the criminal defendant and his counsel during trial preparation. The conviction in each case was set aside and a new trial ordered. The explanatory <em>per curiam </em>in <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span>, </em>although referring to the overheard conversations with counsel, did not rule that whenever conversations with counsel are overheard the Sixth Amendment is violated and a new trial must be had. Indeed, neither the Sixth Amendment nor the right to counsel was even mentioned in the short opinion. The Solicitor General conceded that Black was entitled to a “judicial determination” of whether “the monitoring of conversations between [Black] and his attorney had [any] <em>effect </em>upon his conviction or the fairness of his trial,” although the Solicitor General contended that information derived from the overheard conversations was not used in any way by the prosecution. Memorandum for United States in <em>Black </em>v. <em>United States, </em>O. T. 1965, No. 1029, p. 4 (emphasis added). The Court focused on the particular form the “judicial determination” <page-number citation-index="1" label="552">*552</page-number>should take, concluding that on the particular facts of the case a new trial was the more appropriate means of affording Black “an opportunity to protect himself from the <em>use </em>of evidence that might be otherwise inadmissible.” 385 U. S., at 29 (emphasis added). In <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span>, </em>the Court wrote nothing further, merely citing the <em>Black per curiam. </em>Once again the Solicitor General did not oppose further judicial proceedings to determine whether any information from the surveillance had been used at trial, notwithstanding his assertion that the contents of the overheard conversations were never communicated to the prosecuting attorneys. Brief for United States in <em>O’Brien </em>v. <em>United States, </em>O. T. 1966, No. 823, pp. 10-12.</p>
<p id="b702-5">It is difficult to believe that the Court in <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span> </em>and <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span> </em>was evolving a definitive construction of the Sixth Amendment without identifying the Amendment it was interpreting, especially in view of the well-established Fourth Amendment grounds for excluding the fruits of the illegal surveillance.<footnotemark>2</footnotemark> If anything is to be inferred from these two cases with respect to the right to counsel, it is that when conversations with counsel have been overheard, the constitutionality of the conviction depends on whether the overheard conversations have produced, directly or indirectly, any of the evidence offered at trial. This is a far cry from the <em>per se </em>rule announced by the Court of Appeals below, for under that rule trial prejudice to the defendant is deemed irrelevant. Here, the courts below have already conducted the “judicial determination,” lacking in <em><span class="citation" data-id="9423273"><a href="/opinion/107287/black-v-united-states/" aria-description="Citation for case: Black v. United States">Black</a></span> </em>and <em><span class="citation" data-id="9423374"><a href="/opinion/107396/obrien-v-united-states/" aria-description="Citation for case: O&#x27;BRIEN v. United States">O’Brien</a></span>, </em>of the effect of the overheard conversations on the defendant’s conviction, and there is nothing in their findings or in the record to indicate any “use of evidence that might be otherwise inadmissible.”</p>
<p id="b702-6">Neither does the Court’s decision in <em>Hoffa </em>v. <em>United States, supra, </em>support the proposition urged by respondent. There, an informant sat in on conversations that defendant Hoffa had with his lawyers and with others during the <page-number citation-index="1" label="553">*553</page-number>course of Hoffa’s trial on a charge of violating the TaftHartley Act. The jury at that trial hung. Hoffa was then tried for tampering with that jury. The informer testified at the latter trial with respect to conversations he had overheard in Hoffa’s hotel suite during the prior trial, not including, however, the conversations Hoffa had with counsel. The Court sustained Hoffa’s jury-tampering conviction over his claim, among others, that his Sixth Amendment counsel right had been violated.</p>
<p id="b703-5">In doing so, the Court did not hold that the Sixth Amendment right to counsel subsumes a right to be free from intrusion by informers into counsel-client consultations. Nor did it purport to describe the contours of any such right. The Court merely assumed, without deciding, that two cases in the Court of Appeals for the District of Columbia Circuit dealing with the right to counsel, <em>Caldwell </em>v. <em>United States, </em>92 U. S. App. D. C. 355, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">205 F. 2d 879</a></span> (1953), and <em>Coplon </em>v. <em>United States, </em>89 U. S. App. D. C. 103, <span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">191 F. 2d 749</a></span> (1951), were correctly decided;<footnotemark>3</footnotemark> <em>assumed </em>without deciding, that had Hoffa been convicted at his first trial, the conviction would have been set aside because the informer had overheard Hoffa and his lawyers conversing and had reported to the authorities the substance of at least some of those conversations; and then held that Hoffa’s <em>assumed </em>Sixth Amendment rights had not been violated because the informer’s testimony at the jury-tampering trial did not touch upon the overheard conversations with counsel but dealt only with conversations between Hoffa and third parties when his lawyers were not <page-number citation-index="1" label="554">*554</page-number>present. 385 U. S., at 307-308. Neither <em>Black, O’Brien, Hoffa, </em>nor any other case in this Court to which we have been cited furnishes grounds for the interpretation and application of the Sixth and Fourteenth Amendments appearing in the Court of Appeals’ opinion and judgment.</p>
<p id="b704-5">At the same time, we need not agree with petitioners that whenever a defendant converses with his counsel in the presence of a third party thought to be a confederate and ally, the defendant assumes the risk and cannot complain if the third party turns out to be an informer for the government who has reported on the conversations to the prosecution and who testifies about them at the defendant’s trial. Had Weatherford testified at Bursey’s trial as to the conversation between Bursey and Wise; had any of the State’s evidence originated in these conversations; had those overheard conversations been used in any other way to the substantial detriment of Bursey; or even had the prosecution learned from Weatherford, an undercover agent, the details of the Bursey-Wise conversations about trial preparations, Bursey would have a much .stronger case.<footnotemark>4</footnotemark></p>
<p id="b705-4"><page-number citation-index="1" label="555">*555</page-number>None of these elements is present here, however. Weather-ford’s testimony for the prosecution about the events of March and April 1970 revealed nothing said or done at the meetings between Bursey and Wise that he attended.<footnotemark>5</footnotemark> None of the State’s evidence was obtained as a consequence of Weather-ford’s participation in those meetings. Nevertheless, it <page-number citation-index="1" label="556">*556</page-number>might be argued that Weatherford, a dutiful agent, surely communicated to the prosecutors Bursey’s defense plans and strategy and his attorney’s efforts to prepare for trial, all of which was inherently detrimental to Bursey, unfairly advantaged the prosecution, and threatened to subvert the adversary system of criminal justice.</p>
<p id="b706-5">The argument founders on the District Court’s express finding that Weatherford communicated nothing at all to his superiors or to the prosecution about Bursey’s trial plans or about the upcoming trial. App. 249, 252. The Court of Appeals did not disturb this finding, but sought to surmount it by declaring Weatherford himself to have been a member of the prosecuting team whose knowledge of Bursey’s trial plans was alone enough to violate Bursey’s constitutional right to counsel and to vitiate Bursey’s conviction. <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#487" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d, at 487</a></span>. Though imaginative, this reasoning is not a realistic assessment of the relationship of Weatherford to the prosecuting staff or of the potential for detriment to Bursey or benefit to the State that Weather-ford’s uncommunicated knowledge might pose. If the fact was, as found by the District Court, that Weatherford communicated nothing about the two meetings to anyone else, we are quite unconvinced that a constitutional claim under the Sixth and Fourteenth Amendments was made out.</p>
<p id="b706-6">This is consistent with the Court’s approach in the <em>Hoff a </em>case. There, the informant overheard several conversations between Hoffa and his attorneys, but the Court found it necessary to deal with the Sixth Amendment right-to-counsel claim only after noting that the informant had reported to the Government about at least some of the activities of Hoffa’s defense counsel. 385 U. S., at 305-306. As long as the information possessed by Weatherford remained uncommunicated, he posed no substantial threat to Bursey’s Sixth Amendment rights. Nor do we believe that federal or state prosecutors will be so prone to lie or the difficulties of proof <page-number citation-index="1" label="557">*557</page-number>will be so great that we must always assume not only that an informant communicates what he learns from an encounter with the defendant and his counsel but also that what he communicates has the potential for detriment to the defendant or benefit to the prosecutor’s case.</p>
<p id="b707-5">Moreover, this is not a situation where the State’s purpose was to learn what it could about the defendant’s defense plans and the informant was instructed to intrude on the lawyer-client relationship or where the informant has assumed for himself that task and acted accordingly. Weatherford, the District Court found, did not intrude at all; he was invited to the meeting, apparently not for his benefit but for the benefit of Bursey and his lawyer. App. 248. Weatherford went, not to spy, but because he was asked and because the State was interested in retaining his undercover services on other matters and it was therefore necessary to avoid raising the suspicion that he was in fact the informant whose existence Bursey and Wise already suspected.</p>
<p id="b707-6">That the <em>per se </em>rule adopted by the Court of Appeals would operate prophylactically and effectively is very likely true; but it would require the informant to refuse to participate in attorney-client meetings, even though invited, and thus for all practical purposes to unmask himself. Our cases, however, have recognized the unfortunate necessity of undercover work and the value it often is to effective law enforcement. <em>E. g., United States </em>v. <em>Russell, </em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#432" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 432</a></span> (1973); <em>Lewis </em>v. <em>United States, </em><span class="citation" data-id="9423294"><a href="/opinion/107312/lewis-v-united-states/#208" aria-description="Citation for case: Lewis v. United States">385 U. S. 206, 208-209</a></span> (1966). We have also recognized the desirability and legality of continued secrecy even after arrest. <em>Roviaro </em>v. <em>United States, </em><span class="citation" data-id="9421409"><a href="/opinion/105484/roviaro-v-united-states/#59" aria-description="Citation for case: Roviaro v. United States">353 U. S. 53, 59, 62</a></span> (1957). We have no general oversight authority with respect to state police investigations. We may disapprove an investigatory practice only if it violates the Constitution; and judged in this light, the Court of Appeals’ <em>per se </em>rule cuts much too broadly. If, for example, <page-number citation-index="1" label="558">*558</page-number>Weatherford at Bursey’s invitation had attended a meeting between Bursey and Wise but Wise had become suspicious and the conversation was confined to the weather or other harmless subjects, the Court of Appeals’ rule, literally read, would cloud Bursey’s subsequent conviction, although there would have been no constitutional violation. The same would have been true if Wise had merely asked whether Weatherford was an informant, Weatherford had denied it, and the meeting then had ended; likewise if the entire conversation had consisted of Wise’s questions and Weatherford’s answers about Weatherford’s own defense plans. Also, and more cogently for present purposes, unless Weatherford communicated the substance of the Bursey-Wise conversations and thereby created at least a realistic possibility of injury to Bursey or benefit to the State, there can be no Sixth Amendment violation. Yet Under the Court of Appeals’ rule, Bursey’s conviction would have been set aside on appeal.</p>
<p id="b708-5">There being no tainted evidence in this case, no communication of defense strategy to the prosecution, and no purposeful intrusion by Weatherford, there was no violation of the Sixth Amendment insofar as it is applicable to the States by virtue of the Fourteenth Amendment., The proof in this case thus fell short of making out a § 1983 claim, and the judgment of the District Court should have been affirmed in this respect.</p>
<p id="b708-6">It is also apparent that neither Weatherford’s trial testimony nor the fact of his testifying added anything to the Sixth Amendment claim. Weatherford’s testimony for the prosecution related only to events prior to the meetings with Wise and Bursey and referred to nothing that was said at those meetings. There is no indication that any of this testimony was prompted by or was the product of those meetings. Weatherford’s testimony was surely very damaging, but the mere fact that he had met with Bursey and his lawyer prior to trial did not violate Bursey’s right to <page-number citation-index="1" label="559">*559</page-number>counsel any more than the informant’s meetings with Hoffa and Hoffa’s lawyers rendered inadmissible the informant’s testimony having no connection with those conversations.</p>
<p id="b709-5">Ill</p>
<p id="b709-6">Because under <em>Brady </em>v. <em>Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963), the prosecution has the “duty under the due process clause to insure that ‘criminal trials are fair’ by disclosing evidence favorable to the defendant upon request,” the Court of Appeals also held that the State was constitutionally forbidden to “conceal the identity of an informant from a defendant during his trial preparation,” to permit the informant to “deny up through the day before his appearance at trial that he will testify against the defendant,” and then to have the informant “testify with devastating effect.” <span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/#487" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">528 F. 2d, at 487</a></span>. This conduct, the Court of Appeals thought, lulled the defendant into a false sense of security and denied him “the opportunity (1) to consider whether plea bargaining might be the best course, (2) to do a background check on Weatherford for purposes of cross-examination, and (3) to attempt to counter the devastating impact of eyewitness identification.” <em><span class="citation" data-id="332135"><a href="/opinion/332135/brett-allen-bursey-v-jack-m-weatherford-individually-and-in-his-official/" aria-description="Citation for case: Brett Allen Bursey v. Jack M. Weatherford, Individually...">Ibid.</a></span> </em>The Court of Appeals apparently would have arrived at this conclusion whether or not Weatherford had ever met with Wise.</p>
<p id="b709-7">Again we are in disagreement. <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>does not warrant the Court of Appeals’ holding. It does not follow from the prohibition against concealing evidence favorable to the accused that the prosecution must reveal before trial the names of all witnesses who will testify unfavorably. There is no general constitutional right to discovery in a criminal case, and <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>did not create one; as the Court wrote recently, “the Due Process Clause has little to say regarding the amount of discovery which the parties must be afforded . . . .” <em>Wardius </em>v. <em>Oregon, </em><span class="citation" data-id="9425341"><a href="/opinion/108811/wardius-v-oregon/#474" aria-description="Citation for case: Wardius v. Oregon">412 U. S. 470, 474</a></span> (1973). <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>is not implicated here where the only claim is that the State should <page-number citation-index="1" label="560">*560</page-number>have revealed that it would present the eyewitness testimony of a particular agent against the defendant at trial.</p>
<p id="b710-5">In terms of the defendant’s right to a fair trial, the situation is not changed materially by the additional element relied upon by the Court of Appeals, namely, that Weather-ford not only concealed his identity but represented he would not be a witness for the prosecution, an assertion that proved to be inaccurate. There are several answers to the contention that the claim of misrepresentation is of crucial importance. The first is that there was no deliberate misrepresentation in this regard: The trial court found that until the day of trial Weatherford did not expect to be called as a witness; until then he did not know-that he would testify. Second, as we understand the argument, it is that once the undercover agent has successfully caused an arrest, he risks causing an unfair trial if he denies his identity when accused or asked. We would" hesitate so to construe the Due Process Clause. We are not at all convinced that there is a constitutional difference between the situation where the informant is sufficiently trusted that he is never suspected and never asked about the possibility of his testifying but nevertheless surprises the defendant by giving devastating testimony, and the situation we have here, where the defendant is suspicious enough to ask and the informant denies that he will testify but nevertheless does so. Moreover, if the informant must confess his identity when confronted by an arrested defendant, in many cases the agent in order to protect himself will simply disappear pending trial, before the confrontation occurs. In the last analysis, however, the undercover agent who stays in place and continues his deception merely retains the capacity to surprise; and unless the surprise witness or unexpected evidence is, without more, a denial of constitutional rights, Bursey was not denied a fair trial.</p>
<p id="b710-6">The Court of Appeals suggested that Weatherford’s continued duplicity lost Bursey the opportunity to plea bargain. <page-number citation-index="1" label="561">*561</page-number>But there is no constitutional right to plea bargain; the prosecutor need not do so if he prefers to go to trial. It is a novel argument that constitutional rights are infringed by-trying the defendant rather than accepting his plea of guilty. Moreover, Wise could have approached the prosecutor before trial and surely was under no misapprehension about Bursey’s plight during trial. It was also suggested by the Court of Appeals that Bursey was deprived of the opportunity to investigate Weatherford in preparation for possible impeachment on cross-examination. But there was no objection at trial to Weatherford’s testimony, no request for a continuance, and even now no indication of substantial prejudice from this occurrence. As for Bursey’s claimed disability to counter Weatherford’s “devastating” testimony, the disadvantage was no more than exists in any case where the State presents very damaging evidence that was not anticipated. Wise and Bursey must have realized that in going to trial the State was confident of conviction and that if any exculpatory evidence or possible defenses existed it would be extremely wise to have them available. Prudence would have counseled at least as much.</p>
<p id="b711-5">The judgment of the Court of Appeals is</p>
<p id="b711-6">Reversed.<footnotemark>6</footnotemark>.</p>
<footnote label="1">
<p id="b701-5"> In <em>Silverman </em>v. <em>United States, </em><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U. S. 505</a></span> (1961), the Court had held that eavesdropping accomplished through use of an electronic listening device similar to the “tubular microphone” used to overhear Black’s and O’Brien’s conversations constituted an unauthorized physical penetration of the petitioners’ premises in violation of the Fourth Amendment. The Solicitor General conceded that both Black and O’Brien should have been allowed to establish that the prosecution’s case was tainted by the interception of conversations between Black and persons other than their attorneys as well as by conversations involving counsel, thus indicating his awareness of the illegality of the Government’s eavesdropping under the Fourth Amendment.</p>
</footnote>
<footnote label="2">
<p id="b702-7"> See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="3">
<p id="b703-6"> <em><span class="citation" data-id="9442990"><a href="/opinion/227881/coplon-v-united-states-two-cases/" aria-description="Citation for case: Coplon v. United States (Two Cases)">Coplon</a></span> </em>held that interceptions by Government agents of telephone messages between the defendant and her lawyer before and during trial, if proved by the defendant, deprived her of her right to counsel and entitled her to a new trial. <em><span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/" aria-description="Citation for case: Caldwell v. United States">Caldwell</a></span> </em>held that the defendant’s right to counsel was violated where a Government undercover agent went to work as an assistant for the defense and reported frequently to the prosecution on “many matters connected with the impending trial.” 92 U. S. App. D. C., at 356, <span class="citation" data-id="232188"><a href="/opinion/232188/caldwell-v-united-states/#880" aria-description="Citation for case: Caldwell v. United States">205 F. 2d, at 880</a></span> (footnote omitted).</p>
</footnote>
<footnote label="4">
<p id="b704-6"><em> In Hoffa, </em>the United States conceded, as it does here as <em>amicus curiae, </em>that the Sixth Amendment would be violated “if the government places an informant in the defense camp during a criminal trial and receives from that informant privileged information pertaining to the defense of the criminal charges . . . because the Sixth Amendment’s assistance-of-counsel guarantee can be meaningfully implemented only if a criminal defendant knows that his communications with his attorney are private and that his lawful preparations for trial are secure against intrusion by the government, his adversary in the criminal proceeding.” Brief for United States in <em>Hoffa </em>v. <em>United States, </em>O. T. 1966, No. 32, p. 71, quoted in Brief for United States as <em>Amicus Curiae </em>in the instant <em>case, </em>p. 24 n. 13.</p>
<p id="b704-7">Respondent argues that <em><span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/" aria-description="Citation for case: Hoffa v. United States">Hoffa</a></span> </em>established the same right-to-counsel standard for government interception of attorney-client communications by an undercover agent as for interception by electronic surveillance. Even apart from the fact that the Court was merely assuming the existence of a right-to-counsel violation in that case, see <em>supra, </em>at 553, we find respondent’s argument questionable. One threat to the effective assist<page-number citation-index="1" label="555">*555</page-number>anee of counsel posed by government interception of attorney-client communications lies in the inhibition of free exchanges between defendant and counsel because of the fear of being overheard. However, a fear that some third party may turn out to be a government agent will inhibit attorney-client communication to a lesser degree than the fear that the government is monitoring those communications through electronic eavesdropping, because the former intrusion may be avoided by excluding third parties from defense meetings or refraining from divulging defense strategy when third parties are present at those meetings. Of course, in some circumstances the ability to exclude third parties from defense meetings may not eliminate the chilling effect on attorney-client exchanges, but neither <em>Hoff a </em>nor any other decision of this Court supports respondent’s theory that the chill is the same whether induced by electronic surveillance or by undercover agents. Cf. <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#402" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 402-405</a></span> (1976) (attorney-client privilege protects only those disclosures which might not haye been made absent the privilege, because the purpose of the privilege is to encourage confidential disclosures by a client to an attorney); 8 J. Wigmore, Evidence § 2311, pp. 601-602 (McNaughton rev. ed. 1961) (attorney-client communications in the presence of a third party not the agent of either are generally not protected by the privilege).</p>
</footnote>
<footnote label="5">
<p id="b705-9"> See App. 225-240 (testimony of Weatherford at state trial). On cross-examination by Wise (Bursey’s lawyer), Weatherford acknowledged that at the second meeting with Bursey and Wise, Weatherford told Wise, in response to the latter’s questions, that he had not been asked to testify for the prosecution and that he did not anticipate being present at Bursey’s trial. This testimony, elicited by defense counsel apparently for the purpose of discrediting Weatherford’s testimony on direct examination, obviously does not constitute use by the prosecution of information obtained from Weatherford’s attendance at defense meetings. Whatever the limitations on testimony by informants about statements made at defense meetings attended by them, 'the Sixth Amendment does not prevent the defense from introducing such statements to undercut the effectiveness of the informant’s testimony for the prosecution.</p>
</footnote>
<footnote label="6">
<p id="b711-9"> Because we hold that Bursey’s constitutional rights were not violated by Weatherford’s actions, we reverse the holding of the Court of Appeals that Weatherford’s superior, Strom, was also liable because of his involvement in Weatherford’s undercover activities.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Weeks v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Weeks v. United States"
type: case
citation: "232 U.S. 383 (1914)"
parallel_cite: "34 S. Ct. 341; 58 L. Ed. 652"
neutral_cite: 1914 U.S. LEXIS 1368
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1914
date_decided: 1914-02-24
docket: 461
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1914-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Weeks v. United States
  varies_by_point: false
  scope_note: "Origin of the federal exclusionary rule; extended to the States by Mapp v. Ohio (1961). Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/98094/weeks-v-united-states/"
  cluster_id: 98094
  opinion_id: 98094
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Anchor"
related: ["[[Mapp v. Ohio]]", "[[Wong Sun v. United States]]", "[[United States v. Leon]]"]
aliases: ["Weeks"]
tags: ["case", "fourth-amendment", "exclusionary-rule", "warrantless-search", "origin"]
holding: "Origin of the federal exclusionary rule: evidence obtained in violation of the Fourth Amendment is inadmissible against a defendant in…"
lake:
  record_id: Weeks v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Weeks v. United States

*232 U.S. 383 (1914)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Weeks was arrested at his place of business for using the mails to transport lottery tickets. While he was in custody, police officers and a United States Marshal entered his home without a warrant — twice — and seized letters and private papers, which were turned over to the federal prosecutor. Before trial, Weeks petitioned for the return of his property; the court returned some items but kept the letters, which were admitted over his objection and used to convict him.

## Issue
Whether evidence seized by federal officers from a defendant's home without a warrant, in violation of the Fourth Amendment, may be retained and used against him at his federal criminal trial.

## Rule
Evidence obtained by federal officers in violation of the Fourth Amendment may not be used against the accused in a federal prosecution. If it could be, the Amendment would be a dead letter: "If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures, is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution." — 232 U.S. at 393. ^pin-393

A defendant who makes a timely demand for the return of unlawfully seized property is entitled to it, and admitting it is reversible error: "the court should have restored these letters to the accused. In holding them and permitting their use upon the trial, we think prejudicial error was committed." — *Id.* at 398. ^pin-398

## Application
On these facts the letters were taken from Weeks's house by a United States Marshal acting without a warrant — "under color of his office" and in direct violation of the Fourth Amendment. Weeks had made a seasonable application for their return, which the trial court denied. Because the seizure was unconstitutional and the demand timely, the court should have restored the letters; retaining and admitting them at trial was prejudicial error requiring reversal. (The Court noted that the seizure by local police, not acting under federal authority, fell outside the Amendment's reach against the Federal Government.)

## Conclusion
The warrantless federal seizure violated the Fourth Amendment; admitting the seized letters was prejudicial error. The judgment was reversed. *Weeks* established the federal exclusionary rule.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of its core holding. *Weeks* originally bound only federal officers; its exclusionary rule was **extended to the States** by [[Mapp v. Ohio]] (1961). The rule was later elaborated and qualified — derivative evidence in [[Wong Sun v. United States]] and the [[The Good-Faith Exception|good-faith exception]] in [[United States v. Leon]] — but *Weeks* remains the foundational authority.

## Appears on
- [[The Exclusionary Rule]] — *Key — Anchor*

## Sources
- *Weeks v. United States*, 232 U.S. 383 (1914) — https://www.courtlistener.com/opinion/98094/weeks-v-united-states/ — pinpoints: 393, 398.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3bdeb8b16e0dde9f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Weeks v. United States"}, "payload": {"all": [{"cite": "232 U.S. 383", "page": "383", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "232"}, {"cite": "34 S. Ct. 341", "page": "341", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "34"}, {"cite": "58 L. Ed. 652", "page": "652", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "58"}, {"cite": "1914 U.S. LEXIS 1368", "page": "1368", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1914"}], "display": "232 U.S. 383", "official": {"cite": "232 U.S. 383", "page": "383", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "232"}, "official_selection_present": true, "record_id": "Weeks v. United States"}}
{"assertion_id": "170351cf9ccb5354", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-393", "record_id": "Weeks v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-393", "pinpoint_status": "slip-only", "quote": "--- # Weeks v. United States *232 U.S. 383 (1914)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Weeks was arrested at his place of business for using the mails to transport lottery tickets. While he was in custody, police officers and a United States Marshal entered his home without a warrant — twice — and seized letters and private papers, which were turned over to the federal prosecutor. Before trial, Weeks petitioned for the return of his property; the court returned some items but kept the letters, which were admitted over his objection and used to convict him. ## Issue Whether evidence seized by federal officers from a defendant's home without a warrant, in violation of the Fourth Amendment, may be retained and used against him at his federal criminal trial. ## Rule Evidence obtained by federal officers in violation of the Fourth Amendment may not be used against the accused in a federal prosecution. If it could be, the Amendment would be a dead letter:", "quote_fidelity": "mismatch", "record_id": "Weeks v. United States", "star_marker": null}}
{"assertion_id": "7100d29d03103b4b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-398", "record_id": "Weeks v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-398", "pinpoint_status": "slip-only", "quote": "the court should have restored these letters to the accused. In holding them and permitting their use upon the trial, we think prejudicial error was committed.", "quote_fidelity": "mismatch", "record_id": "Weeks v. United States", "star_marker": null}}
{"assertion_id": "ed03bf23feea28b8", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Weeks v. United States"}, "payload": {"as_of_content": "1914-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Weeks v. United States", "scope_note": "Origin of the federal exclusionary rule; extended to the States by Mapp v. Ohio (1961). Good law.", "varies_by_point": false}}
```

### lake record — Weeks v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Weeks v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Weeks v. United States",
    "case_name_short": "Weeks",
    "case_name_full": "Weeks v. United States",
    "input_case_name": "Weeks v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1914-02-24",
    "year": 1914,
    "docket": "461",
    "cluster_id": 98094,
    "lead_opinion_id": 98094,
    "sibling_ids": [
      98094
    ],
    "absolute_url": "/opinion/98094/weeks-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "232 U.S. 383",
      "volume": "232",
      "reporter": "U.S.",
      "page": "383",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "34 S. Ct. 341",
        "volume": "34",
        "reporter": "S. Ct.",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 L. Ed. 652",
        "volume": "58",
        "reporter": "L. Ed.",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1914 U.S. LEXIS 1368",
        "volume": "1914",
        "reporter": "U.S. LEXIS",
        "page": "1368",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "232 U.S. 383",
        "volume": "232",
        "reporter": "U.S.",
        "page": "383",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "34 S. Ct. 341",
        "volume": "34",
        "reporter": "S. Ct.",
        "page": "341",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "58 L. Ed. 652",
        "volume": "58",
        "reporter": "L. Ed.",
        "page": "652",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1914 U.S. LEXIS 1368",
        "volume": "1914",
        "reporter": "U.S. LEXIS",
        "page": "1368",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "232 U.S. 383",
    "official_selection": {
      "court_class": "scotus",
      "selected": "232 U.S. 383",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-393",
      "page": null,
      "quote": "--- # Weeks v. United States *232 U.S. 383 (1914)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Weeks was arrested at his place of business for using the mails to transport lottery tickets. While he was in custody, police officers and a United States Marshal entered his home without a warrant \u2014 twice \u2014 and seized letters and private papers, which were turned over to the federal prosecutor. Before trial, Weeks petitioned for the return of his property; the court returned some items but kept the letters, which were admitted over his objection and used to convict him. ## Issue Whether evidence seized by federal officers from a defendant's home without a warrant, in violation of the Fourth Amendment, may be retained and used against him at his federal criminal trial. ## Rule Evidence obtained by federal officers in violation of the Fourth Amendment may not be used against the accused in a federal prosecution. If it could be, the Amendment would be a dead letter:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-398",
      "page": null,
      "quote": "the court should have restored these letters to the accused. In holding them and permitting their use upon the trial, we think prejudicial error was committed.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1914-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Weeks v. United States",
    "varies_by_point": false,
    "scope_note": "Origin of the federal exclusionary rule; extended to the States by Mapp v. Ohio (1961). Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Raenard Romalle Douglas",
          "cluster_id": 10129058,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jarvis v. Kansas Dept. of Revenue",
          "cluster_id": 4618635,
          "cite": [
            "442 P.3d 1054"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dave McNeil v. State",
          "cluster_id": 3094175,
          "cite": [
            "443 S.W.3d 295",
            "2014 WL 3843757",
            "2014 Tex. App. LEXIS 8519"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
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
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jermaine Lebron v. State of Florida",
          "cluster_id": 2686855,
          "cite": [
            "135 So. 3d 1040",
            "39 Fla. L. Weekly Supp. 62",
            "2014 WL 321817",
            "2014 Fla. LEXIS 376"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Isaac Andrew Baldon III",
          "cluster_id": 4472245,
          "cite": [
            "829 N.W.2d 785",
            "2013 WL 1694553",
            "2013 Iowa Sup. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane1_negative"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bivens v. Six Unknown Named Agents of Federal Bureau of Narcotics",
          "cluster_id": 108375,
          "cite": [
            "29 L. Ed. 2d 619",
            "91 S. Ct. 1999",
            "403 U.S. 388",
            "1971 U.S. LEXIS 23"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Katz v. United States",
          "cluster_id": 107564,
          "cite": [
            "19 L. Ed. 2d 576",
            "88 S. Ct. 507",
            "389 U.S. 347",
            "1967 U.S. LEXIS 2"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wong Sun v. United States",
          "cluster_id": 106515,
          "cite": [
            "9 L. Ed. 2d 441",
            "83 S. Ct. 407",
            "371 U.S. 471",
            "1963 U.S. LEXIS 2431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mapp v. Ohio",
          "cluster_id": 106285,
          "cite": [
            "6 L. Ed. 2d 1081",
            "81 S. Ct. 1684",
            "367 U.S. 643",
            "1961 U.S. LEXIS 812"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Payton v. New York",
          "cluster_id": 110235,
          "cite": [
            "63 L. Ed. 2d 639",
            "100 S. Ct. 1371",
            "445 U.S. 573",
            "1980 U.S. LEXIS 13"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Carroll v. United States",
          "cluster_id": 100567,
          "cite": [
            "267 U.S. 132",
            "45 S. Ct. 280",
            "69 L. Ed. 543",
            "1925 U.S. LEXIS 361"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. United States",
          "cluster_id": 107636,
          "cite": [
            "19 L. Ed. 2d 1247",
            "88 S. Ct. 967",
            "390 U.S. 377",
            "1968 U.S. LEXIS 2167"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 104504,
          "cite": [
            "92 L. Ed. 2d 436",
            "68 S. Ct. 367",
            "333 U.S. 10",
            "1948 U.S. LEXIS 2583",
            "92 L. Ed. 436"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. O'Brien",
          "cluster_id": 107701,
          "cite": [
            "20 L. Ed. 2d 672",
            "88 S. Ct. 1673",
            "391 U.S. 367",
            "1968 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robinson",
          "cluster_id": 108893,
          "cite": [
            "38 L. Ed. 2d 427",
            "94 S. Ct. 467",
            "414 U.S. 218",
            "1973 U.S. LEXIS 21",
            "66 Ohio Op. 2d 202"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
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
        "journal_ref": "Weeks v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(98094) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzUxNTU1MjAwMDAwJnM9MTA0NTczMSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2898094%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(98094)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDE0JnM9MTA4NzY4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%2898094%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(98094)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 2,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(98094)",
    "indexed_citing_opinions": 2132,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 98094,
        "count": 2132,
        "count_source": "search"
      }
    ],
    "citation_count": 3480,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/weeks-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2OTgxNDYmcz05NDgxNjY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%2898094%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 98094,
        "cited_id": 89759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 93951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 98094,
        "cited_id": 97412,
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
    "date_created": "2026-07-06T04:11:06Z",
    "date_modified": "2026-07-06T09:17:03Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:13:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:11:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Weeks v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b432-5">
  Mr. Justice Day
 </author>
<p id="AXQ">
  delivered the opinion of the court.
 </p>
<p id="b432-6">
  An indictment was returned against the plaintiff in error, defendant below, and herein so designated, in the District Court of the United States for the Western District of Missouri; containing nine counts. The seventh count, upon which a conviction was had, charged, the use of the mails for the purpose of transporting certain coupons or tickets representing chances -or shares in a lottery or gift enterprise, in violation of § 213 of the Criminal Code. Sentence of fine and imprisonment was imposed. This writ of error is to review that judgment.
 </p>
<p id="b432-7">
  The defendant was arrested by a police officer, so far as the record shows, without warrant, at the Union Station in Kansas City, Missouri, where he was employed by an express company. Other police officers had gone to the house of the defendant and being told by a neighbor where the key was kept, found it and entered the house. They searched the defendant’s room and took possession of various papers and articles found there, which were afterwards turned over to the United States Marshal. Later in the same day police officers returned with the Marshal, wfio thought he might find additional evidence, and, being admitted by someone in the house, probably a boarder, in response to- a rap, the Marshal searched the defendant’s room and carried away. certain letters and envelopes found in the drawer of a chiffonier. Neither the marshal nor the police officers had á search warrant.
 </p>
<p id="b433-4">
<span citation-index="1" class="star-pagination" label="387"> 
   *387
   </span>
  The defendant filed in the cause before the time for trial the following petition:
 </p>
<blockquote id="b433-5">
  “Petition to Return Private Papers, Books and Other Property. ■ _
 </blockquote>
<blockquote id="b433-6">
  “Now comes defendant and states that he is a citizen and resident of Kansas City, Missouri, and that he resides, owns and occupies a home at 1834 Penn Street in said City;
 </blockquote>
<blockquote id="b433-7">
  “That on the 21st day of December, 1911, while plaintiff was absent at his daily vocation certain officers of the government whose names are to plaintiff-unknown,' unlawfully and without warrant or authority so to do, broke open the door to plaintiff’s said home and seized all of his books, letters, money, papers, notes, evidences of indebtedness, stock, certificates, insurance policies, deeds, abstracts, and other muniments of title, bonds, candies, clothes and other property in said home, and this in violation of Sections 11 and 23 of the Constitution of Missouri' and of the 4th and 5th Amendments to the Constitution of the United States:
 </blockquote>
<blockquote id="b433-8">
  “That the District Attorney, Marshal and Clerk of the United States Court for the Western District of Missouri took the above described property so seized- into their possession and have failed and refused to return to defendant portion of same, to-wit:
 </blockquote>
<blockquote id="b433-9">
  “One (1) leather grip, value about $7.00; one (1) tin box valued at $3.00; one, (1) Pettis County, Missouri, bond, value $500.00; three (3) Mining stock certificates which defendant is unable to more particularly describe valued at $12&gt;000.00, and certain stock certificates in addition thereto issued by the San Domingo Mining Loan and Investment Company, about $75.00 in currency; one (1) newspaper published about 1790, an heirloom; and certain other property which plaintiff is now unable to describe:
 </blockquote>
<blockquote id="b433-10">
  “That said property is being unlawfully and improperly •
  <span citation-index="1" class="star-pagination" label="388"> 
   *388
   </span>
  held by said District Attorney, Marshal and Clerk in violation of defendant’s rights under the Constitution of the United States and the State of Missouri:
 </blockquote>
<blockquote id="b434-5">
  “ That said District Attorney purposes to use said books, letters, papers, certificates of stock, etc., at the trial of the above entitled cause and that by reason thereof and of the facts above set forth defendant’s rights under the amendments aforesaid to the Constitution of Missouri, and the United States have been and will be violated unless the Court order the return prayed for:
 </blockquote>
<blockquote id="b434-6">
  “Wherefore, defendant prays that said District Attorney, Marshal and Clerk be notified, and that the Court direct and order said District Attorney, Marshal and Clerk to return said property to said defendant.”
 </blockquote>
<p id="b434-7">
  Upon consideration of the petition the court entered in the cause an order directing the return of such property as was not pertinent to the charge against the defendant, but denied the petition as to pertinent matter, reserving the right to pass upon the pertinency at a later time. In obedience to the order the District Attorney returned part of the property taken and retained the remainder, concluding a list of the latter with the statement that, “all of which last above described property is to be used in evidence in the trial of the above entitled cause, and pertains to the alleged sale of lottery tickets of the company above named.”
 </p>
<p id="b434-8">
  After the jury had been sworn and before any evidence had been given, the defendant again urged his petition for the return of his property, which was denied by the court. Upon the introduction of such papers during the' trial, the defendant objected on the ground that the papers had been obtained without a search warrant and by breaking open his home, in violation of the Fourth and Fifth Amendments to the Constitution of the United States, which objection was overruled by the court. Among the papers retained and put in evidence were a number of
  <span citation-index="1" class="star-pagination" label="389"> 
   *389
   </span>
  lottery tickets and statements with reference to the lottery, taken at the first visit of the police to the defendant’s room, and a number of letters written to the defendant in respect to the lottery, taken by the Marshal upon his search of defendant’s room.
 </p>
<p id="b435-5">
  The defendant assigns error, among other things, in the court’s refusal to grant his petition for the return of his property and in permitting the papers to be used at the trial.
 </p>
<p id="b435-6">
  It is thus apparent that the question presented involves the determination of the duty of the court with reference to the motion made by the defendant for the return of certain letters, as well as other papers, taken from his room by the United States Marshal, who, without authority of process, if any such could have been legally issued, visited the room of the defendant for the declared purpose of obtaining additional testimony to support the charge against the accused, and having gained admission to the house took from the drawer of a chiffonier there found certain letters written to the defendant, tending to show his guilt. These letters were placed in the control of the District Attorney and were subsequently produced by him and offered in evidence against the accused at the trial. The defendant contends that such appropriation of his private correspondence was in violation of rights secured to him by the Fourth and Fifth Amendments to the Constitution of the United States. We shall deal with the Fourth Amendment, which provides:
 </p>
<blockquote id="b435-7">
  “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation and particularly' describing the place to be searched, and the persons or things to be seized.”
 </blockquote>
<p id="b435-8">
  The history of this Amendment is given with particularity in the opinion of Mr. Justice Bradley, speaking for
  <span citation-index="1" class="star-pagination" label="390"> 
   *390
   </span>
  the court in
  <em>
   Boyd
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>. As was there shown, it took its origin in the determination of the framers of the Amendments to the Federal Constitution to provide for that instrument a Bill of Rights, securing to the American people, among other things, those safeguards which had grown up in England to protect the people from unreasonable searches and seizures, such as were permitted under the general warrants issued under authority of the Government by which there had been invasions of the home and privacy of the citizens and the seizure of their private papers in support of charges, real or imaginary, made against them. Such practices had also received sanction under warrants and seizures under the so-called writs of assistance, issued in the American colonies. See 2 Watson on the Constitution, 1414
  <em>
   et seq.
  </em>
  Resistance to these practices had established the principle which was enacted into the fundamental law in the Fourth Amendment, that a man’s house was his castle and not to be invaded by any general authority to search and seize his goods and papers. Judge Cooley, in his Constitutional Limitations, pp. 425, 426, in treating of this feature of our Constitution, said: “The maxim that ‘every man’s house is his castle,’ is made a part of our constitutional law in the clauses prohibiting unreasonable searches and seizures, and has always been looked upon as of high value to the citizen.” “Accordingly,” says Lieber in his work on Civil Liberty and Self-Government, 62, in speaking of the English law in this respect, “no man’s house can be forcibly opened, or he or his goods be carried away after it has thus been forced, except in cases of felony, and then the sheriff must be furnished with a warrant, and take great care lest he commit a trespass. This principle is jealously insisted upon.” In
  <em>
   Ex parte Jackson,
  </em>
  <span class="citation" data-id="89759"><a href="/opinion/89759/ex-parte-jackson/#733" aria-description="Citation for case: Ex Parte Jackson">96 U. S. 727, 733</a></span>, this court recognized the principle of protection as applicable to letters and sealed packages in the mail, and held that consistently
  <span citation-index="1" class="star-pagination" label="391"> 
   *391
   </span>
  with this guaranty of the right of the people to be secure in their papers against unreasonable searches and seizures such matter could only be opened and examined upon warrants issued on oath or affirmation particularly describing the thing to be seized, “as is required when papers are subjected to search in one’s own household.”
 </p>
<p id="b437-5">
  In the
  <em>
   Boyd Case, supra,
  </em>
  after citing Lord Camden’s, judgment in
  <em>
   Entick
  </em>
  v.
  <em>
   Carrington,
  </em>
  19 Howell’s State Trials, 1029, Mr. Justice Bradley said (630):
 </p>
<blockquote id="b437-6">
  “The principles laid down in this opinion affect the very , essence of constitutional liberty and security. They reach farther than the concrete form of the case then before the court, with its adventitious.circumstances; they apply to all invasions on the part of the government and its employés of the sanctity of a man’s home and the privacies of life. It is not the breaking of h'is doors, and the' rummaging of his drawers, that constitutes the essence of the- offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property, where that right has never been forfeited by his conviction of some public offence, — it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden’s judgment.”
 </blockquote>
<p id="b437-7">
  In
  <em>
   Bram
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span>, this court in speaking by the present Chief Justice of
  <em>
   Boyd’s Case,
  </em>
  dealing with the Fourth and Fifth Amendments, said (544): ■
 </p>
<blockquote id="b437-8">
  . “It was in that casa demonstrated that both of these Amendments contemplated perpetuating, in their full efficacy, by means of a constitutional provision, principles of humanity and civil liberty, which had been secured in the mother country only after years of-struggle, so as to implant them in our institutions in-'the fullness of their integrity, free from the possibilities of future legislative change.” ■ ;
 </blockquote>
<p id="b437-9">
  The effect of the Fourth Amendment is to put the courts
  <span citation-index="1" class="star-pagination" label="392"> 
   *392
   </span>
  of the United States and Federal officials, in the exercise of their power and authority, under limitations and restraints as to the exercise of such power and authority, and to forever secure the people, their persons, houses, papers and effects against all unreasonable searches and seizures under the guise of law. This protection reaches all alike, whether accused of crime or not, and the duty of giving to it force and effect is obligatory upon all entrusted under our Federal system with the enforcement of the laws. The tendency of those who execute the criminal laws of the country to obtain conviction by means of unlawful seizures and enforced confessions, the latter often obtained after subjecting accused persons to unwarranted practices destructive of rights secured by the Federal Constitution, should find no sanction in the judgments of the courts which are charged at all times with the support of the Constitution and to which people of all conditions have a right to appeal for the maintenance of such fundamental rights.
 </p>
<p id="b438-5">
  What then is the present case? Before answering that inquiry specifically, it may be, well by a process of exclusion to state what it is not. It is not án assertion of the right on the part of the Government, always recognized under English and American law, to search the person of the accused when legally arrested to discover and seize the fruits or evidences of crime. This right has been uniformly maintained in many cases. 1 Bishop on Criminal Procedure, §211; Wharton, Crim. Plead, and Practice, 8th ed., § 60;
  <em>
   Dillon
  </em>
  v.
  <em>
   O’Brien and Davis,
  </em>
  16 Cox C. C. 245. Nor is it the case of testimony offered at a trial where the court is asked to stop and consider the illegal means by which proofs, otherwise competent, were obtained — of which we shall have occasion to treat later in this opinion. Nor is it the case of burglar’s tools or other proofs of guilt found upon his arrest within the control of the accused.
 </p>
<p id="b439-4">
<span citation-index="1" class="star-pagination" label="393"> 
   *393
   </span>
  The case in the aspect in which we are dealing with it involves the right of the court in a criminal prosecution to retain for the purposes of evidence the letters and correspondence of the accused, seized in his house in his absence and without his authority, by a United States Marshal holding no warrant for his arrest and none for the search of his premises. The accused, without awaiting his trial,, made timely application to the court for an order for the, return of these letters, as well as other property. This application was denied, the letters retained and put in evidence, after a further application at the beginning of the trial, both applications asserting the rights of the accused under the Fourth and Fifth Amendments to the Constitution. If letters and private documents can thus be seized and held and used in evidence against a citizen accused of an offense, the protection of the Fourth Amendment declaring his right to be secure against such searches and seizures, is of no value, and, so far as those thus placed are concerned, might as well be stricken from the Constitution. The efforts of the courts and their officials to bring the guilty to punishment, praiseworthy as they are, are not to be aided by the sacrifice of those great principles established by years of endeavor and suffering which have resulted in their embodiment in the fundamental law of the land. The United States Marshal could only have invaded the house of the accused when armed with a warrant issued as required' by the Constitution, upon sworn information and describing with reasonable particularity the thing for which the search was to be made. Instead, he acted without sanction of law, doubtless prompted by the desire to bring further proof to the aid of the Government, and under color of his office undertook to make a seizure of private papers in direct violation of the constitutional prohibition against such action. Under such circumstances, without sworn information and particular description, not even an order of court would
  <span citation-index="1" class="star-pagination" label="394"> 
   *394
   </span>
  have justified such procedure, much less was it within the authority of the United States Marshal to thus invade the house and privacy of the accused. In
  <em>
   Adams
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span>, this court said that the Fourth Amendment was intended to secure the citizen in person and property against unlawful invasion of the sanctity of his home by officers of the law acting under legislative or judicial sanction. This protection is equally extended to the action of the Government and officers of the law acting under it.
  <em>
   (Boyd Case, supra.)
  </em>
  To sanction such proceedings would be to affirm by judicial decision a manifest neglect if not an open defiance of the prohibitions of the Constitution,- intended for the protection of the people against such unauthorized action.
 </p>
<p id="b440-5">
  The court before which the application was made in this case recognized the illegal character of the seizure and ordered the return of property not in its judgment competent to be offered at the trial, but refused the application of the accused to turn over the letters, which were afterwards put in evidence on behalf of the Government. While there is no opinion in the case, the court in this proceeding doubtless relied upon what is now contended by the Government to be the correct rule of law under such circumstances, that the letters having come into the control of the court,' it would not inquire into the manner in which they were obtained, but if competent would keep them and permit their use in evidence. Such proposition, the Government asserts, is conclusively established by certain decisions of this court, the first' of which is
  <em>
   Adams
  </em>
  v.
  <em>
   New <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">York, supra.</a></span>
  </em>
  In that case the plaintiff in error had been convicted in the. Supreme Court of the State of New York for having in his possession certain gambling paraphernalia used in the game known as policy, in violation of the Penal Code of New York. At the trial certain papers, which had been seized by police • officers executing a search warrant for the discovery and
  <span citation-index="1" class="star-pagination" label="395"> 
   *395
   </span>
  seizure of policy slips and which had been found in addition to the policy slips, were offered in evidence over his objection. The conviction was affirmed by the Court of Appeals of New York (176 N.-Y. 351), and the case was brought here for alleged violation of the Fourth and Fifth Amendments to the Constitution of the United States. Pretermitting the question whether these amendments applied to the action of the States, this court proceeded to examine the alleged violations of the Fourth and Fifth Amendments, and put its decision upon the ground that the papers found in the execution of the search warrant, which warrant had a legal purpose in the attempt to find gambling paraphernalia, were competent evidence against the accused, and their offer in testimony did not violate his constitutional privilege against unlawful search or seizure, for it was held that such incriminatory documents thus discovered were not the subject of an unreasonable search and seizure, and in effect that the same were incidentally seized in the lawful execution of a warrant and not in the wrongful invasion of the home of the citizen and the unwarranted seizure of his papers and property. It was further held, approving in that respect the doctrine laid down in 1 Greenleaf, § 254a, that it was no valid objection to the usq of the papers that they had been thus seized, and that the courts in the course of a trial would not make an issue to determine that question, and many state cases were cited supporting that doctrine.
 </p>
<p id="b441-5">
  The same point had been ruled in
  <em>
   People
  </em>
  v.
  <em>
   Adams,
  </em>
  <span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, from‘which decision the case was brought to this court, .where it was held that if the papers seized in ■ addition to the policy slips were competent evidence in the case, as the court held they were, they were admissible in evidence at the trial, the court saying (p. 358): “The underlying principle obviously is that the court, when engaged in trying a criminal causé, will not take notice of
  <span citation-index="1" class="star-pagination" label="396"> 
   *396
   </span>
  the manner in which witnesses have possessed themselves of papers, or other articles of personal property, which are material and properly offered in evidence.” This doctrine thus laid down by the New York Court of Appeals and approved by this court, that a court will not in trying a criminal cause permit a collateral issue to be raised as to the source of competent testimony, has the sanction of so many state cases that it would be impracticable to cite or refer to them in detail. Many of them are collected in the note to
  <em>
   State
  </em>
  v.
  <em>
   Turner,
  </em>
  <span class="citation no-link">136 Am. St. Rep. 129</span>, 135
  <em>
   et seq.
  </em>
  After citing numerous cases the editor says: “The underlying principle of all these decisions obviously is, that the court, when engaged in the trial of a criminal action, will not take notice of the manner in which a witness has possessed himself of papers or other chattels, subjects of evidence, which are material and properly offered in evidence:
  <em>
   People
  </em>
  v.
  <em>
   Adams,
  </em>
  <span class="citation" data-id="5650086"><a href="/opinion/5795142/people-v-adams/" aria-description="Citation for case: People v. Adams">176 N. Y. 351</a></span>, <span class="citation no-link">98 Am. St. Rep. 675</span>, <span class="citation" data-id="3588018"><a href="/opinion/3606309/people-v-adams/" aria-description="Citation for case: People v. . Adams">68 N. E. 636</a></span>, 63 L. R. A. 406. Such an investigation is not involved necessarily in the litigation in chief, and to pursue it would be to halt in the orderly progress of a cause, and consider incidentally a question which has happened to cross the path of such litigation, and which is wholly independent thereof.”
 </p>
<p id="b442-5">
  It is therefore evident that the
  <em>
   Adams Case
  </em>
  affords no authority for the action of the court in this case, when applied, to in due season for the return of papers seized in violation of the Constitutional Amendment. The decision in that case rests upon incidental seizure made in the execution of a legal warrant and in the application of the doctrine that a collateral issue will not be raised to ascertain the source from which testimony, competent in a criminal case, comes.
 </p>
<p id="b442-6">
  The Government also relies upon
  <em>
   Hale
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span>, in which the previous cases of
  <em>
   Boyd
  </em>
  v.
  <em>
   United States, supra, Adams
  </em>
  v.
  <em>
   New. <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">York, supra,</a></span> Interstate Com
  </em>
<span citation-index="1" class="star-pagination" label="397"> 
   *397
   </span>
<em>
   merce Commission
  </em>
  v.
  <em>
   Brimson,
  </em>
  <span class="citation" data-id="93951"><a href="/opinion/93951/interstate-commerce-commission-v-brimson/" aria-description="Citation for case: Interstate Commerce Commission v. Brimson">154 U. S. 447</a></span>, and
  <em>
   Interstate Commerce Commission
  </em>
  v.
  <em>
   Baird,
  </em>
  <span class="citation" data-id="96063"><a href="/opinion/96063/interstate-commerce-commission-v-baird/" aria-description="Citation for case: Interstate Commerce Commission v. Baird">194 U. S. 25</a></span>, are reviewed, and wherein it was held that a
  <em>
   subpoena duces tecum
  </em>
  requiring a corporation to produce all its contracts and correspondence with no less than six other companies, as well as all letters received by the corporation from thirteen other companies located in different parts of the United States, was an unreasonable search and seizure within the Fourth Amendment, and it was there stated that (201 U. S. p. 76) “an order for the production of books and papers may constitute an unreasonable search and seizure within the Fourth Amendment. While a search ordinarily implies a quest by an officer of the law, and a seizure contemplates a forcible dispossession of the owner, still, as was held in the
  <em>
   Boyd Case,
  </em>
  the substance of the offense is the compulsory production of private papers, whether under a search warrant or a
  <em>
   subpoena duces tecum,
  </em>
  against which the person, be he individual or corporation, is entitled to protection.” If such a seizure under the authority of a warrant supposed to be legal, constitutes a violation of the constitutional protection,
  <em>
   a fortiori
  </em>
  does the attempt of an officer of the United States, the United States Marshal, acting under color of his office, without even the sanction of a warrant, constitute an invasion of the rights within the protection afforded by the Fourth Amendment.
 </p>
<p id="b443-5">
  Another case relied upon is
  <em>
   American Tobacco Co.
  </em>
  v.
  <em>
   Werckmeister,
  </em>
  <span class="citation" data-id="96731"><a href="/opinion/96731/american-tobacco-co-v-werckmeister/" aria-description="Citation for case: American Tobacco Co. v. Werckmeister">207 U. S. 284</a></span>, in which it was held that the seizure by the United States Marshal in a copyright case of certain pictures under a writ of replevin did not constitute an unreasonable search and seizure. The other case from this court relied upon is
  <em>
   Holt
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span>, in which it was held that testimony tending to show that a certain blouse which was in evidence as ■ incriminating him, had been put upon the prisoner and fitted him, did not violate his constitutional right. We
  <span citation-index="1" class="star-pagination" label="398"> 
   *398
   </span>
  are at a loss to see the application of these cases to the one in hand.
 </p>
<p id="b444-4">
  . The right of the court to deal with papers and documents in the possession of the District Attorney and other officers of the court and subject to its authority was recognized in
  <em>
   Wise
  </em>
  v.
  <em>
   Henkel,
  </em>
  <span class="citation" data-id="97412"><a href="/opinion/97412/wise-v-henkel/" aria-description="Citation for case: Wise v. Henkel">220 U. S. 556</a></span>. That papers wrongfully seized should be turned over to the accused has been frequently recognized in the early as well as later decisions of the courts. 1 Bishop on Criminal Procedure, § 210;
  <em>
   Rex v. Barnett,
  </em>
  3 C. &amp; P. 600;
  <em>
   Rex
  </em>
  v.
  <em>
   Kinsey,
  </em>
  7 C. &amp; P. 447;
  <em>
   United States
  </em>
  v.
  <em>
   Mills,
  </em>
  185 Fed. Rep. 318;
  <em>
   United States
  </em>
  v.
  <em>
   McHie,
  </em>
  194 Fed. Rep. 894, 898.
 </p>
<p id="b444-5">
  We therefore reach the conclusion that the letters in question were taken from the house of the accused by an official of the United States acting under color of his office in direct violation of the constitutional rights of the defendant; that having made a seasonable application for their return, which was heard and passed upon by the court, there was involved in the order refusing the application a denial of the constitutional rights of the accused, and that the court , should have restored these letters to the accused. In holding them and permitting their use upon the trial, we think prejudicial error was committed. As to the papers and property seized by the policemen, it does not appear that they acted under any claim of Federal authority such .as would make the Amendment applicable to such unauthorized seizures. The record shows that what they did by way of arrest and search and seizure was done before the finding of the indictment in the Federal court, under what supposed right or authority does not appear. What remedies the defendant may have against them we need not inquire, as the Fourth Amendment is not directed to individual misconduct of such officials. Its limitations reach the Federal Government and its agencies.
  <em>
   Boyd Case,
  </em>
  116 U. S.,
  <em>
   supra,
  </em>
  and see
  <em>
   Twining
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>.
 </p>
<p id="b445-3">
<span citation-index="1" class="star-pagination" label="399"> 
   *399
   </span>
  It results that the judgment of the court below must be reversed, and the case remanded for further proceedings in accordance with this opinion.
 </p>
<p id="b445-4">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---
