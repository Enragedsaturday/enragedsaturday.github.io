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

## GROUP: _overhaul2/lake/cases/Orozco v. Texas.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Orozco v. Texas"
type: case
citation: "394 U.S. 324 (1969)"
parallel_cite: "89 S. Ct. 1095; 22 L. Ed. 2d 311"
neutral_cite: 1969 U.S. LEXIS 2154
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-03-25
docket: 641
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-03-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Orozco v. Texas
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107883/orozco-v-texas/"
  cluster_id: 107883
  opinion_id: 107883
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Berkemer v. McCarty]]", "[[Howes v. Fields]]", "[[Rhode Island v. Innis]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "custodial-interrogation"]
holding: "Miranda warnings were required where four officers questioned a suspect under arrest in his own bedroom in the early morning; custody…"
lake:
  record_id: Orozco v. Texas
  status: verified
  projected_at: 2026-07-06
---

# Orozco v. Texas

*394 U.S. 324 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
At about 4 a.m., four police officers entered Orozco's boardinghouse bedroom while he slept and questioned him about a fatal shooting. From the moment he gave his name, an officer testified, Orozco "was not free to go where he pleased but was 'under arrest.'" Without any [[Miranda and Custodial Interrogation|Miranda warnings]], the officers questioned him; he admitted owning a pistol and said it was in a washing machine, where it was found and matched by ballistics to the fatal shot.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] were required before custodial questioning that occurred in the suspect's own bedroom rather than at a police station.

## Rule
Yes. "We disagree and hold that the use of these admissions obtained in the absence of the required warnings was a flat violation of the Self-Incrimination Clause of the Fifth Amendment as construed in *Miranda*." — 394 U.S. at 326. ^pin-326

Miranda's warnings are required wherever a person is interrogated while "in custody at the station *or otherwise deprived of his freedom of action in any significant way*." — 394 U.S. at 327 (quoting *Miranda v. Arizona*, 384 U.S. at 477). ^pin-327

## Application
According to the officers' own testimony, Orozco "was under arrest and not free to leave when he was questioned in his bedroom in the early hours of the morning." Because he was therefore in custody, the warnings were required despite the familiar surroundings of his own home; their omission made the use of his statements about the pistol a violation of the Fifth Amendment.

## Conclusion
The unwarned, in-custody bedroom questioning violated the Self-Incrimination Clause; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Orozco* remains a leading illustration that Miranda custody is not confined to the station house.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Orozco v. Texas*, 394 U.S. 324 (1969) — https://www.courtlistener.com/opinion/107883/orozco-v-texas/ — pinpoints: 326, 327.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6c2338afd83e4725", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Orozco v. Texas"}, "payload": {"all": [{"cite": "394 U.S. 324", "page": "324", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "394"}, {"cite": "89 S. Ct. 1095", "page": "1095", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "89"}, {"cite": "22 L. Ed. 2d 311", "page": "311", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "22"}, {"cite": "1969 U.S. LEXIS 2154", "page": "2154", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1969"}], "display": "394 U.S. 324", "official": {"cite": "394 U.S. 324", "page": "324", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "394"}, "official_selection_present": true, "record_id": "Orozco v. Texas"}}
{"assertion_id": "4f01999e7ad9a7e5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-326", "record_id": "Orozco v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-326", "pinpoint_status": "slip-only", "quote": "Without any Miranda warnings, the officers questioned him; he admitted owning a pistol and said it was in a washing machine, where it was found and matched by ballistics to the fatal shot. ## Issue Whether Miranda warnings were required before custodial questioning that occurred in the suspect's own bedroom rather than at a police station. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Orozco v. Texas", "star_marker": null}}
{"assertion_id": "b8b660f14541a35a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-327", "record_id": "Orozco v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-327", "pinpoint_status": "slip-only", "quote": "in custody at the station *or otherwise deprived of his freedom of action in any significant way*.", "quote_fidelity": "mismatch", "record_id": "Orozco v. Texas", "star_marker": null}}
{"assertion_id": "90c3a110aa7890ed", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Orozco v. Texas"}, "payload": {"as_of_content": "1969-03-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Orozco v. Texas", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Orozco v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Orozco v. Texas",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Orozco v. Texas",
    "case_name_short": "Orozco",
    "case_name_full": "Orozco v. Texas",
    "input_case_name": "Orozco v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-03-25",
    "year": 1969,
    "docket": "641",
    "cluster_id": 107883,
    "lead_opinion_id": 107883,
    "sibling_ids": [
      107883,
      9423964,
      9423965,
      9423966
    ],
    "absolute_url": "/opinion/107883/orozco-v-texas/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 324",
      "volume": "394",
      "reporter": "U.S.",
      "page": "324",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1095",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 311",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 2154",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 324",
        "volume": "394",
        "reporter": "U.S.",
        "page": "324",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1095",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1095",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 311",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "311",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 2154",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "2154",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 324",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 324",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "Without any Miranda warnings, the officers questioned him; he admitted owning a pistol and said it was in a washing machine, where it was found and matched by ballistics to the fatal shot. ## Issue Whether Miranda warnings were required before custodial questioning that occurred in the suspect's own bedroom rather than at a police station. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-327",
      "page": null,
      "quote": "in custody at the station *or otherwise deprived of his freedom of action in any significant way*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-03-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Orozco v. Texas",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Faux",
          "cluster_id": 7312636,
          "cite": [
            "94 F. Supp. 3d 258",
            "2015 U.S. Dist. LEXIS 37051",
            "2015 WL 1347041"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hughes",
          "cluster_id": 214334,
          "cite": [
            "640 F.3d 428",
            "2011 U.S. App. LEXIS 7338",
            "2011 WL 1332061"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Fiedler v. State",
          "cluster_id": 1533838,
          "cite": [
            "991 S.W.2d 70",
            "1998 WL 1058889"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Wayne Davis",
          "cluster_id": 471603,
          "cite": [
            "792 F.2d 1299",
            "20 Fed. R. Serv. 762",
            "1986 U.S. App. LEXIS 24794"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jerry Rorex",
          "cluster_id": 437540,
          "cite": [
            "737 F.2d 753",
            "1984 U.S. App. LEXIS 21056"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Larson",
          "cluster_id": 2080732,
          "cite": [
            "346 N.W.2d 199",
            "1984 Minn. App. LEXIS 3051"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Greathouse",
          "cluster_id": 1669864,
          "cite": [
            "627 S.W.2d 592"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wilder v. State",
          "cluster_id": 2463525,
          "cite": [
            "583 S.W.2d 349",
            "1979 Tex. Crim. App. LEXIS 1817"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane1_negative"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Mathiason",
          "cluster_id": 109587,
          "cite": [
            "50 L. Ed. 2d 714",
            "97 S. Ct. 711",
            "429 U.S. 492",
            "1977 U.S. LEXIS 38"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Alabama",
          "cluster_id": 108182,
          "cite": [
            "26 L. Ed. 2d 387",
            "90 S. Ct. 1999",
            "399 U.S. 1",
            "1970 U.S. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Quarles",
          "cluster_id": 111214,
          "cite": [
            "81 L. Ed. 2d 550",
            "104 S. Ct. 2626",
            "467 U.S. 649",
            "1984 U.S. LEXIS 111",
            "52 U.S.L.W. 4790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Tucker",
          "cluster_id": 109063,
          "cite": [
            "41 L. Ed. 2d 182",
            "94 S. Ct. 2357",
            "417 U.S. 433",
            "1974 U.S. LEXIS 71"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boys Markets, Inc. v. Retail Clerks Union, Local 770",
          "cluster_id": 108154,
          "cite": [
            "26 L. Ed. 2d 199",
            "90 S. Ct. 1583",
            "398 U.S. 235",
            "1970 U.S. LEXIS 79",
            "74 L.R.R.M. (BNA) 2257"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beckwith v. United States",
          "cluster_id": 109430,
          "cite": [
            "48 L. Ed. 2d 1",
            "96 S. Ct. 1612",
            "425 U.S. 341",
            "1976 U.S. LEXIS 147",
            "37 A.F.T.R.2d (RIA) 1232"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duckworth v. Eagan",
          "cluster_id": 112322,
          "cite": [
            "106 L. Ed. 2d 166",
            "109 S. Ct. 2875",
            "492 U.S. 195",
            "1989 U.S. LEXIS 3196",
            "57 U.S.L.W. 4942"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
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
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "J. D. B. v. North Carolina",
          "cluster_id": 218925,
          "cite": [
            "180 L. Ed. 2d 310",
            "131 S. Ct. 2394",
            "564 U.S. 261",
            "2011 U.S. LEXIS 4557",
            "22 Fla. L. Weekly Fed. S 1135",
            "79 U.S.L.W. 4504"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hopfer",
          "cluster_id": 3941316,
          "cite": [
            "679 N.E.2d 321",
            "112 Ohio App. 3d 521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Linton",
          "cluster_id": 944931,
          "cite": [
            "56 Cal. 4th 1146",
            "302 P.3d 927",
            "158 Cal. Rptr. 3d 521",
            "2013 WL 3214690",
            "2013 Cal. LEXIS 5338"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Coleman v. Commonwealth",
          "cluster_id": 1227505,
          "cite": [
            "307 S.E.2d 864",
            "226 Va. 31",
            "1983 Va. LEXIS 266"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sewn Newton",
          "cluster_id": 786350,
          "cite": [
            "369 F.3d 659",
            "2004 U.S. App. LEXIS 10343",
            "2004 WL 1161747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adams v. Illinois",
          "cluster_id": 108480,
          "cite": [
            "31 L. Ed. 2d 202",
            "92 S. Ct. 916",
            "405 U.S. 278",
            "1972 U.S. LEXIS 81"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Leonard David Griffin",
          "cluster_id": 553880,
          "cite": [
            "922 F.2d 1343",
            "1990 U.S. App. LEXIS 22396",
            "1990 WL 212298"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Fioravanti, Nicholas Panaccione, and Angelo Pepe, Nicholas Panaccione",
          "cluster_id": 285356,
          "cite": [
            "412 F.2d 407"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wicker v. State",
          "cluster_id": 1655134,
          "cite": [
            "740 S.W.2d 779",
            "1987 Tex. Crim. App. LEXIS 671",
            "1987 WL 1000"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Davis",
          "cluster_id": 4667521,
          "cite": [
            "2019 CO 84"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cannon v. State",
          "cluster_id": 1564923,
          "cite": [
            "691 S.W.2d 664",
            "1985 Tex. Crim. App. LEXIS 1371"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Orozco v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjY0NTc2MDAwMDAmcz0xNDEyNzQ3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107883+OR+9423964+OR+9423965+OR+9423966%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzUmcz0xNDUzMjk4JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107883+OR+9423964+OR+9423965+OR+9423966%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966)",
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
    "complete_query": "cites:(107883 OR 9423964 OR 9423965 OR 9423966)",
    "indexed_citing_opinions": 447,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107883,
        "count": 424,
        "count_source": "search"
      },
      {
        "opinion_id": 9423964,
        "count": 34,
        "count_source": "search"
      },
      {
        "opinion_id": 9423965,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423966,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 661,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/orozco-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQ4OTQ3MTYmcz03MzE4NjgxJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107883+OR+9423964+OR+9423965+OR+9423966%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107883,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107883,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107883,
        "cited_id": 107676,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107883,
        "cited_id": 1527140,
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
    "date_created": "2026-07-05T16:28:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:28:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:28:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:31:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:28:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Orozco v. Texas

```
<div>
<center><b><span class="citation" data-id="9423964"><a href="/opinion/107883/orozco-v-texas/" aria-description="Citation for case: Orozco v. Texas">394 U.S. 324</a></span> (1969)</b></center>
<center><h1>OROZCO<br>
v.<br>
TEXAS.</h1></center>
<center>No. 641.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 26, 1969.</center>
<center>Decided March 25, 1969.</center>
CERTIORARI TO THE COURT OF CRIMINAL APPEALS OF TEXAS.
<p><i>Charles W. Tessmer</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Lonny F. Zwiener,</i> Assistant Attorney General of Texas, argued the cause for respondent. With him on the brief were <i>Crawford C. Martin,</i> Attorney General, <i>Nola White,</i> First Assistant Attorney General, <i>Hawthorne Phillips,</i> Executive Assistant Attorney General, <i>Robert C. Flowers,</i> Assistant Attorney General, and <i>W. V. Geppert.</i></p>
<p>MR. JUSTICE BLACK delivered the opinion of the Court.</p>
<p>The petitioner, Reyes Arias Orozco, was convicted in the Criminal District Court of Dallas County, Texas, of murder without malice and was sentenced to serve in the state prison not less than two nor more than 10 years. The Court of Criminal Appeals of Texas affirmed the conviction, rejecting petitioner's contention that a material part of the evidence against him was obtained in violation of the provision of the Fifth Amendment to the United States Constitution, made applicable to the States by the Fourteenth Amendment, that: "No person <span class="star-pagination">*325</span>. . . shall be compelled in any criminal case to be a witness against himself."<sup>[1]</sup></p>
<p>The evidence introduced at trial showed that petitioner and the deceased had quarreled outside the El Farleto Cafe in Dallas shortly before midnight on the date of the shooting. The deceased had apparently spoken to petitioner's female companion inside the restaurant. In the heat of the quarrel outside, the deceased is said to have beaten petitioner about the face and called him "Mexican Grease." A shot was fired killing the deceased. Petitioner left the scene and returned to his boardinghouse to sleep. At about 4 a. m. four police officers arrived at petitioner's boardinghouse, were admitted by an unidentified woman, and were told that petitioner was asleep in the bedroom. All four officers entered the bedroom and began to question petitioner. From the moment he gave his name, according to the testimony of one of the officers, petitioner was not free to go where he pleased but was "under arrest." The officers asked him if he had been to the El Farleto restaurant that night and when he answered "yes" he was asked if he owned a pistol. Petitioner admitted owning one. After being asked a second time where the pistol was located, he admitted that it was in the washing machine in a backroom of the boardinghouse. Ballistics tests indicated that the gun found in the washing machine was the gun that fired the fatal shot. At petitioner's trial, held after the effective date<sup>[2]</sup> of this Court's decision in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the trial court allowed one of the officers, <span class="star-pagination">*326</span> over the objection of petitioner's lawyer,<sup>[3]</sup> to relate the statements made by petitioner concerning the gun and petitioner's presence at the scene of the shooting. The trial testimony clearly shows that the officers questioned petitioner about incriminating facts without first informing him of his right to remain silent, his right to have the advice of a lawyer before making any statement, and his right to have a lawyer appointed to assist him if he could not afford to hire one. The Texas Court of Criminal Appeals held, with one judge dissenting, that the admission of testimony concerning the statements petitioner had made without the above warnings was not precluded by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> We disagree and hold that the use of these admissions obtained in the absence of the required warnings was a flat violation of the Self-Incrimination Clause of the Fifth Amendment as construed in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>The State has argued here that since petitioner was interrogated on his own bed, in familiar surroundings, our <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> holding should not apply. It is true that the Court did say in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that "compulsion to speak in the isolated setting of the police station may well be greater than in courts or other official investigations, where there are often impartial observers to guard against intimidation or trickery." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 461</a></span>. But the opinion iterated and reiterated the absolute necessity for officers interrogating people "in custody" to give the described warnings. See <i>Mathis</i> v. <i>United States,</i> 391 U. S. 1 <span class="star-pagination">*327</span> (1968). According to the officer's testimony, petitioner was under arrest and not free to leave when he was questioned in his bedroom in the early hours of the morning. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> opinion declared that the warnings were required when the person being interrogated was "in custody at the station <i>or otherwise deprived of his freedom of action in any significant way.</i>" <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 477</a></span>. (Emphasis supplied.) The decision of this Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was reached after careful consideration and lengthy opinions were announced by both the majority and dissenting Justices. There is no need to canvass those arguments again. We do not, as the dissent implies, expand or extend to the slightest extent our <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> decision. We do adhere to our well-considered holding in that case and therefore reverse<sup>[4]</sup> the conviction below.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE FORTAS took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>The passage of time has not made the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> case any more palatable to me than it was when the case was decided. See my dissenting opinion, and that of MR. JUSTICE WHITE, in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#504" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 504, 526</a></span> (1966).</p>
<p>Yet, despite my strong inclination to join in the dissent of my Brother WHITE, I can find no acceptable avenue of escape from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in judging this case, especially in light of <i>Mathis</i> v. <i>United States,</i> <span class="citation" data-id="9423682"><a href="/opinion/107676/mathis-v-united-states/" aria-description="Citation for case: Mathis v. United States">391 U. S. 1</a></span> (1968), which has already extended the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rules beyond the <span class="star-pagination">*328</span> police station, over the protest of JUSTICE STEWART, WHITE, and myself, <i>id.,</i> at 5-8. Therefore, and purely out of respect for <i>stare decisis,</i> I reluctantly feel compelled to acquiesce in today's decision of the Court, at the same time observing that the constitutional condemnation of this perfectly understandable, sensible, proper, and indeed commendable piece of police work highlights the unsoundness of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE STEWART joins, dissenting.</p>
<p>This decision carries the rule of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), to a new and unwarranted extreme. I continue to believe that the original rule amounted to a "constitutional straitjacket" on law enforcement which was justified neither by the words or history of the Constitution, nor by any reasonable view of the likely benefits of the rule as against its disadvantages. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#526" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 526</a></span>. Even accepting <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court extends the rule here and draws the straitjacket even tighter.</p>
<p>The opinion of the Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was devoted in large part to an elaborate discussion of the subtle forms of psychological pressure which could be brought to bear when an accused person is interrogated at length in unfamiliar surroundings. The "salient features" of the cases decided in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> were "incommunicado interrogation of individuals in a police-dominated atmosphere." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#445" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 445</a></span>. The danger was that in such circumstances the confidence of the prisoner could be eroded by techniques such as successive interrogations by police acting out friendly or unfriendly roles. These techniques are best developed in "isolation and unfamiliar surroundings," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#450" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 450</a></span>. And they take time: "the major qualities an interrogator should possess are patience and perseverance." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> The techniques <span class="star-pagination">*329</span> of an extended period of isolation, repeated interrogation, cajolery, and trickery often enough produced admissions which were actually coerced in the traditional sense so that new safeguards were deemed essential.</p>
<p>It is difficult to believe that the requirements there laid down were essential to prevent compulsion in every conceivable case of station house interrogation. Where the defendant himself as a lawyer, policeman, professional criminal, or otherwise has become aware of what his right to silence is, it is sheer fancy to assert that his answer to every question asked him is compelled unless he is advised of those rights with which he is already intimately familiar. If there is any warrant to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> at all, it rests on the likelihood that in a sufficient number of cases exposure to station house practices will result in compelled confessions and that additional safeguards should be imposed in all cases to prevent possible erosion of Fifth Amendment values. Hence, the detailed ritual which <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> fashioned.</p>
<p>The Court now extends the same rules to all instances of in-custody questioning outside the station house. Once arrest occurs, the application of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is automatic. The rule is simple but it ignores the purpose of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to guard against what was thought to be the corrosive influence of practices which station house interrogation makes feasible. The Court wholly ignores the question whether similar hazards exist or even are possible when police arrest and interrogate on the spot, whether it be on the street corner or in the home, as in this case. No predicate is laid for believing that practices outside the station house are normally prolonged, carried out in isolation, or often productive of the physical or psychological coercion made so much of in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> It is difficult to imagine the police duplicating in a person's home or on the street those conditions and practices <span class="star-pagination">*330</span> which the Court found prevalent in the station house and which were thought so threatening to the right to silence. Without such a demonstration, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> hardly reaches this case or any cases similar to it.</p>
<p>Here, there was no prolonged interrogation, no unfamiliar surroundings, no opportunity for the police to invoke those procedures which moved the majority in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> In fact, the conversation was by all accounts a very brief one. According to uncontradicted testimony, petitioner was awake when the officers entered his room, and they asked him four questions: his name, whether he had been at the El Farleto, whether he owned a pistol, and where it was. He gave his name, said he had been at the El Farleto, and admitted he owned a pistol without hesitation. He was slow in telling where the pistol was, and the question was repeated. He then took the police to the nearby washing machine where the gun was hidden.</p>
<p>It is unquestioned that this sequence of events in their totality would not constitute coercion in the traditional sense or lead any court to view the admissions as involuntary within the meaning of the rules by which we even now adjudicate claims of coercion relating to pre-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> trials. And, realistically, had Orozco refused to answer the questions asked of him, it seems most unlikely that prolonged interrogation would have followed in petitioner's own quarters; nothing similar to the station house model invoked by the court would have occurred here. The police had petitioner's name and description, had ample evidence that he had been at the night club and suspected that he had a gun. Surely had he refused to give his name or answer any other questions, they would have arrested him anyway, searched the house and found the gun, which would have been clearly admissible under all relevant authorities. But the Court insists that this case be reversed for failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.</p>
<p>I cannot accept the dilution of the custody requirements of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to this level, where the hazards to the <span class="star-pagination">*331</span> right to silence are so equivocal and unsupported by experience in a recurring number of cases. Orozco was apprehended in the most familiar quarters, the questioning was brief, and no admissions were made which were not backed up by other evidence. This case does not involve the confession of an innocent man, or even of a guilty man from whom a confession has been wrung by physical abuse or the modern psychological methods discussed in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> These are simply the terse remarks of a man who has been caught, almost in the act. Even if there were reason to encourage suspects to consult lawyers to tell them to be silent before quizzing at the station house, there is no reason why police in the field should have to preface every casual question of a suspect with the full panoply of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. The same danger of coercion is simply not present in such circumstances, and the answers to the questions may as often clear a suspect as help convict him. If the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings have their intended effect, and the police are able to get no answers from suspects, innocent or guilty, without arresting them, then a great many more innocent men will be making unnecessary trips to the station house. Ultimately it may be necessary to arrest a man, bring him to the police station, and provide a lawyer, just to discover his name. Even if the man is innocent the process will be an unpleasant one.</p>
<p>Since the Court's extension of <i>Miranda's</i> rule takes it into territory where even what rationale there originally was disappears, I dissent.</p>
<p>Memorandum of MR. JUSTICE STEWART.</p>
<p>Although there is much to be said for MR. JUSTICE HARLAN'S position, I join my Brother WHITE in dissent. It seems to me that those of us who dissented in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>, remain free not only to express our continuing disagreement with that decision, but also to oppose any broadening of its impact.</p>
<h2>NOTES</h2>
<p>[1]  The state court also rejected a contention that use of the evidence also violated the Fourth Amendment's provision against unreasonable searches and seizures. Our holding makes it unnecessary for us to consider that contention.</p>
<p>[2]  See <i>Johnson</i> v. <i>New Jersey,</i> <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719</a></span> (1966).</p>
<p>[3]  The State appears to urge that petitioner's <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> claim is unreviewable in this Court because the objection made by trial counsel to the officer's testimony was not sufficiently "specific." We fail to perceive how this could be an adequate state ground in view of the fact that the Texas Court of Criminal Appeals specifically decided that the introduction of petitioner's statement made to the officers "was not precluded under Miranda v. State of Arizona," <span class="citation" data-id="9647819"><a href="/opinion/1527140/orozco-v-state/#672" aria-description="Citation for case: Orozco v. State">428 S. W. 2d 666, 672</a></span>, while the dissenting judge thought that it was.</p>
<p>[4]  In light of some apparent misunderstanding on this point, it is perhaps appropriate to point out once again that a reversal by this Court of a conviction based in part on unconstitutional evidence leaves the State free to retry the defendant without the tainted evidence.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Owen v. City of Independence.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Owen v. City of Independence
type: case
citation: "445 U.S. 622 (1980)"
parallel_cite: "100 S. Ct. 1398; 63 L. Ed. 2d 673"
neutral_cite: 1980 U.S. LEXIS 14
court: U.S.
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-04-16
docket: 78-1779
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
  opinion_url: "https://www.courtlistener.com/opinion/110236/owen-v-city-of-independence/"
  cluster_id: 110236
  opinion_id: null
  identity_checked: true
lake:
  record_id: Owen v. City of Independence
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Anchor
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
  - "[[Monell v. Department of Social Services]]"
tags:
  - case
  - section-1983
  - municipal-liability
  - qualified-immunity
  - good-faith
  - monell
holding: "A municipality has no qualified immunity from § 1983 liability based on the good faith of its officers; it may not assert that its officials acted in good faith as a defense to liability for a constitutional deprivation."
aliases:
  - Owen v. City of Independence
  - "Owen v. City of Independence (1980)"
---

# Owen v. City of Independence

*445 U.S. 622 (1980)* (No. 78-1779) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110236 → combined opinion 110236 (Brennan, J.; 445 U.S. 622, decided Apr. 16, 1980). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*639` follows the quoted sentence, placing it at 638). S9 promotes. -->

## Background
George Owen, the police chief of Independence, Missouri, was discharged without a hearing following a City Council investigation, amid public statements impugning his conduct. He sued the City under 42 U.S.C. § 1983, alleging that the manner of his dismissal deprived him of a liberty interest — a chance to clear his name — without due process. [[Reading and Citing Cases#on-remand|On remand]] after *[[Monell v. Department of Social Services|Monell]]*, the Court of Appeals held the City could invoke a [[Qualified Immunity|qualified immunity]] resting on the good faith of its officials. The Supreme Court granted [[Reading and Citing Cases#certiorari-cert|certiorari]].

## Issue
Whether a municipality sued under § 1983 may assert a [[Qualified Immunity|qualified immunity]], based on the good faith of its officers, as a defense to liability.

## Rule
Finding no common-law tradition of immunity for municipal corporations and no policy in § 1983 to support one, the Court held: "We hold, therefore, that the municipality may not assert the good faith of its officers or agents as a defense to liability under § 1983." — 445 U.S. at 638. ^pin-638

## Application
The individual immunities the Court has recognized under § 1983 were well established at common law when the statute was enacted; municipal immunity was not. And § 1983's purposes — compensating those whose constitutional rights are violated and spreading the loss across the community that benefits from government — are best served by holding the municipality answerable regardless of its officials' subjective good faith. A city therefore cannot escape § 1983 damages by showing that its agents acted in the honest belief that their conduct was lawful.

## Conclusion
The judgment was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. Brennan, J., delivered the opinion of the Court (5–4); Powell, J. (joined by Burger, C.J., and Stewart and Rehnquist, JJ.), dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Owen* establishes the sharp asymmetry in § 1983 immunity law: **individual** officers enjoy [[Qualified Immunity|qualified immunity]], but a **municipality does not** — good faith is no defense for the city. Teach it with *[[Monell v. Department of Social Services|Monell]]*: municipal liability requires a "policy or custom," but where that predicate is met, the city cannot fall back on the good faith of its officers.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Anchor*

## Sources
- [*Owen v. City of Independence*, 445 U.S. 622 (1980)](https://www.courtlistener.com/opinion/110236/owen-v-city-of-independence/) — pinpoint: 638 (Brennan, J., for the Court; the CL opinion text places the reporter star `*639` immediately after the quoted holding, fixing it on 638). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd933871e42ab91a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Owen v. City of Independence"}, "payload": {"all": [{"cite": "445 U.S. 622", "page": "622", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "445"}, {"cite": "100 S. Ct. 1398", "page": "1398", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "63 L. Ed. 2d 673", "page": "673", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "63"}, {"cite": "1980 U.S. LEXIS 14", "page": "14", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "445 U.S. 622", "official": {"cite": "445 U.S. 622", "page": "622", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "445"}, "official_selection_present": true, "record_id": "Owen v. City of Independence"}}
{"assertion_id": "3b98577b75c74eb2", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Owen v. City of Independence"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Owen v. City of Independence", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Owen v. City of Independence

```json
{
  "schema_version": "s2.v1",
  "record_id": "Owen v. City of Independence",
  "status": "under_review",
  "identity": {
    "case_name": "Owen v. City of Independence",
    "case_name_short": "Owen",
    "case_name_full": "OWEN v. CITY OF INDEPENDENCE, MISSOURI, Et Al.",
    "input_case_name": "Owen v. City of Independence",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-04-16",
    "year": 1980,
    "docket": "78-1779",
    "cluster_id": 110236,
    "lead_opinion_id": 9427858,
    "sibling_ids": [],
    "absolute_url": "/opinion/110236/owen-v-city-of-independence/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "445 U.S. 622",
      "volume": "445",
      "reporter": "U.S.",
      "page": "622",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1398",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1398",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 673",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 14",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "445 U.S. 622",
        "volume": "445",
        "reporter": "U.S.",
        "page": "622",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1398",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1398",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 673",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "673",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 14",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "445 U.S. 622",
    "official_selection": {
      "court_class": "scotus",
      "selected": "445 U.S. 622",
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
    "date_created": "2026-07-07T13:27:14Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:27:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "owen-v-city-of-independence--110236",
      "to_record_id": "Owen v. City of Independence",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Owen v. City of Independence

```
<opinion type="majority">
<author id="b684-6">Mr. Justice Brennan</author>
<p id="Anq">delivered the opinion of the Court.</p>
<p id="b684-7"><em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978), overruled <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), insofar as <em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">Monroe</a></span> </em>held that local governments were not among the “persons” to whom 42 U. S. C. 11983 applies and were therefore wholly immune from suit under the statute.<footnotemark>1</footnotemark> <em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">Monell</a></span> </em>reserved decision, however, on the question whether local governments, although not entitled to an absolute immunity, should be afforded some form of official immunity in 1 1983 suits. <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#701" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 701</a></span>. In this action brought by petitioner in the District Court for the Western District of Missouri, the Court of Appeals for the Eighth Circuit held that respondent city of Independence, Mo., “is entitled to qualified immunity from liability” based on the good faith <page-number citation-index="1" label="625">*625</page-number>of its officials: “We extend the limited immunity the district court applied to the individual defendants to cover the City as well, because its officials acted in good faith and without malice.” <span class="citation" data-id="8908383"><a href="/opinion/8919777/owen-v-city-of-independence-missouri/#337" aria-description="Citation for case: Owen v. City of Independence, Missouri">589 F. 2d 335, 337-338</a></span> (1978). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./444/822/">444 U. S. 822</a></span> (1979). We reverse.</p>
<p id="b685-5">I</p>
<p id="b685-6">The events giving rise to this suit are detailed in the District Court’s findings of fact, <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp. 1110</a></span> (1976). On February 20, 1967, Robert L. Broucek, then City Manager of respondent city of Independence, Mo,, appointed petitioner George D. Owen to an indefinite term as Chief of Police.<footnotemark>2</footnotemark> In 1972, Owen and a new City Manager, Lyle W. Alberg, engaged in a dispute over petitioner’s administration of the Police Department’s property room. In March of that year, a handgun, which the records of the Department’s property room stated had been destroyed, turned up in Kansas City in the possession of a felon. This discovery prompted Al-berg to initiate an investigation of the management of the property room. Although the probe was initially directed by petitioner, Alberg soon transferred responsibility for the investigation to the city’s Department of Law, instructing the City Counselor to supervise its conduct and to inform him directly of its findings.</p>
<p id="b685-7">Sometime in early April 1972, Alberg received a written report on the investigation’s progress, along with copies of confidential witness statements. Although the City Auditor found that the Police Department’s records were insufficient to permit an adequate accounting of the goods contained in the property room, the City Counselor concluded that there was no evidence of any criminal acts or of any violation of <page-number citation-index="1" label="626">*626</page-number>state or municipal law in the administration of the property-room. Alberg discussed the results of the investigation at an informal meeting with several City Council members and advised them that he would take action at an appropriate time to correct any problems in the administration of the Police Department.</p>
<p id="b686-5">On April 10, Alberg asked petitioner to resign as Chief of Police and to accept another position within the Department, citing dissatisfaction with the manner in which petitioner had managed the Department, particularly his inadequate supervision of the property room. Alberg warned that if petitioner refused to take another position in the Department his employment would be terminated, to which petitioner responded that he did not intend to resign.</p>
<p id="b686-6">On April 13, Alberg issued a public statement addressed to the Mayor and the City Council concerning the results of the investigation. After referring to “discrepancies” found in the administration, handling, and security of public property, the release concluded that “[t]here appears to be no evidence to substantiate any allegations of a criminal nature” and offered assurances that “[sjteps have been initiated on an administrative level to correct these discrepancies.” <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/#1115" aria-description="Citation for case: Owen v. City of Independence, Mo."><em>Id., </em>at 1115</a></span>. Although Alberg apparently had decided by this time to replace petitioner as Police Chief, he took no formal action to that end and left for a brief vacation without informing the City Council of his decision.<footnotemark>3</footnotemark></p>
<p id="b686-7">While Alberg was away on the weekend of April 15 and 16, two developments occurred. Petitioner, having consulted with counsel, sent Alberg a letter demanding written notice of the charges against him and a public hearing with a reason<page-number citation-index="1" label="627">*627</page-number>able opportunity to respond to those charges.<footnotemark>4</footnotemark> At approximately the same time, City Councilman Paul L. Roberts asked for a copy of the investigative report on the Police Department property room. Although petitioner’s appeal received no immediate response, the Acting City Manager complied with Roberts’ request and supplied him with the audit report and witness statements.</p>
<p id="b687-5">On the evening of April 17, 1972, the City Council held its regularly scheduled meeting. After completion of the planned agenda, Councilman Roberts read a statement he had prepared on the investigation.<footnotemark>5</footnotemark> Among other allegations, <page-number citation-index="1" label="628">*628</page-number>Roberts charged that petitioner had misappropriated Police Department property for his own use, that narcotics and money had “mysteriously disappeared” from his office, that traffic tickets had been manipulated, that high ranking police officials had made “inappropriate” requests affecting the police court, and that “things have occurred causing the unusual release of felons.” At the close of his statement, Roberts moved that the investigative reports be released to the news media and turned over to the prosecutor for presentation to the grand jury, and that the City Manager “take all direct <page-number citation-index="1" label="629">*629</page-number>and appropriate action” against those persons “involved in illegal, wrongful, or gross inefficient activities brought out in the investigative reports.” After some discussion, the City Council passed Roberts’ motion with no dissents and one abstention.<footnotemark>6</footnotemark></p>
<p id="b689-5">City Manager Alberg discharged petitioner the very next day. Petitioner was not given any reason for his dismissal; he received only a written notice stating that his employment as Chief of Police was “[t]erminated under the provisions of Section 3.3(1) of the City Charter.”<footnotemark>7</footnotemark> Petitioner’s earlier demand for a specification of charges and a public hearing was ignored, and a subsequent request by his attorney for an appeal of the discharge decision was denied by the city on the grounds that “there is no appellate procedure or forum provided by the Charter or ordinances of the City of Independence, Missouri, relating to the dismissal of Mr. Owen.” App. 26-27.</p>
<p id="b689-6">The local press gave prominent coverage both to the City Council’s action and petitioner’s dismissal, linking the discharge to the investigation.<footnotemark>8</footnotemark> As instructed by the City Council, Alberg referred the investigative reports and witness statements to the Prosecuting Attorney of Jackson County, Mo., <page-number citation-index="1" label="630">*630</page-number>for consideration by a grand jury. The results of the audit and investigation were never released to the public, however. The grand jury subsequently returned a “no true bill,” and no further action was taken by either the City Council or City Manager Alberg.</p>
<p id="b690-5">II</p>
<p id="b690-6">Petitioner named the city of Independence, City Manager Alberg, and the present members of the City Council in their official capacities as defendants in this suit.<footnotemark>9</footnotemark> Alleging that he was discharged without notice of reasons and without a hearing in violation of his constitutional rights to procedural and substantive due process, petitioner sought declaratory and injunctive relief, including a hearing on his discharge, back-pay from the date of discharge, and attorney’s fees. The District Court, after a bench trial, entered judgment for respondents. <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp. 1110</a></span> (1976).<footnotemark>10</footnotemark></p>
<p id="b691-4"><page-number citation-index="1" label="631">*631</page-number>The Court of Appeals initially reversed the District Court. <span class="citation multiple-matches"><a href="/c/F.%202d/560/925/">560 F. 2d 925</a></span> (1977).<footnotemark>11</footnotemark> Although it agreed with the District Court that under Missouri law petitioner possessed no property interest in continued employment as Police Chief, the Court of Appeals concluded that the city’s allegedly false public accusations had blackened petitioner’s name and reputation, thus depriving him of liberty without due process of law. That the stigmatizing charges did not come from the City Manager and were not included in the official discharge notice was, in the court’s view, immaterial. What was un-<page-number citation-index="1" label="632">*632</page-number>portant, the court explained, was that "the official actions of the city council released charges against [petitioner] contemporaneous and, in the eyes of the public, connected with that discharge.” <em>Id., </em>at 937.<footnotemark>12</footnotemark></p>
<p id="b692-5">Respondents petitioned for review of the Court of Appeals’ decision. Certiorari was granted, and the case was remanded for further consideration in light of our supervening decision in <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span> (1978). <span class="citation" data-id="9011579"><a href="/opinion/9018430/city-of-independence-v-owen/" aria-description="Citation for case: City of Independence v. Owen">438 U. S. 902</a></span> (1978). The Court of Ap<page-number citation-index="1" label="633">*633</page-number>peals on the remand reaffirmed its original determination that the city had violated petitioner’s rights under the Fourteenth Amendment, but held that all respondents, including the city, were entitled to qualified immunity from liability. <span class="citation" data-id="8908383"><a href="/opinion/8919777/owen-v-city-of-independence-missouri/" aria-description="Citation for case: Owen v. City of Independence, Missouri">589 F. 2d 335</a></span> (1978).</p>
<p id="b693-5"><em>Monell </em>held that <em>“a </em>local government may not be sued under § 1983 for an injury inflicted solely by its employees or agents. Instead, it is when execution of a government’s policy or custom, whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy, inflicts the injury that the government as an entity is responsible under § 1983.” <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#694" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 694</a></span>. The Court of Appeals held in the instant ease that the municipality’s official policy was responsible for the deprivation of petitioner’s constitutional rights: “[T]he stigma attached to [petitioner] in connection with his discharge was caused by the official conduct of the City’s lawmakers, or by those whose acts may fairly be said to represent official policy. Such conduct amounted to official policy causing the infringement of [petitioner’s] constitutional rights, in violation of section 1983.” <span class="citation" data-id="8908383"><a href="/opinion/8919777/owen-v-city-of-independence-missouri/#337" aria-description="Citation for case: Owen v. City of Independence, Missouri">589 F. 2d, at 337</a></span>.<footnotemark>13</footnotemark></p>
<p id="b694-4"><page-number citation-index="1" label="634">*634</page-number>Nevertheless, the Court of Appeals affirmed the judgment of the District Court denying petitioner any relief against the respondent city, stating:</p>
<blockquote id="b694-5">“The Supreme Court’s decisions in <em>Board of Regents </em>v. <em>Roth, </em><span class="citation" data-id="9425009"><a href="/opinion/108608/board-of-regents-of-state-colleges-v-roth/" aria-description="Citation for case: Board of Regents of State Colleges v. Roth">408 U. S. 564</a></span> . . . (1972), and <em>Perry </em>v. <em>Sindermann, </em><span class="citation" data-id="9425012"><a href="/opinion/108609/perry-v-sindermann/" aria-description="Citation for case: Perry v. Sindermann">408 U. S. 593</a></span> . . . (1972), crystallized the rule establishing the right to a name-clearing hearing for a government employee allegedly stigmatized in the course of his discharge. The Court decided those two cases two months after the discharge in the instant case. Thus, officials of the City of Independence could not have been aware of [petitioner’s] right to a name-clearing , hearing in connection with the discharge. The City of Independence should not be charged with predicting the future course of constitutional law. We extend the limited immunity the district court applied to the individual defendants to cover the City as well, because its officials acted in good faith and without malice. We hold the City not liable for actions it could not reasonably have known violated [petitioner’s] constitutional rights.” <em>Id., </em>at 338 (footnote and citations omitted).<footnotemark>14</footnotemark></blockquote>
<p id="b695-4"><page-number citation-index="1" label="635">*635</page-number>We turn now to the reasons for our disagreement with this holding.<footnotemark>15</footnotemark></p>
<p id="b695-5">Ill</p>
<p id="b695-6">Because the question of the scope of a municipality’s immunity from liability under § 1983 is essentially one of statutory construction, see <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#314" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 314, 316</a></span> (1975); <em>Tenney </em>v. <em>Brandhove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367, 376</a></span> (1951), the starting point in our analysis must be the language of the statute itself. <em>Andrus </em>v. <em>Allard, </em><span class="citation" data-id="110156"><a href="/opinion/110156/andrus-v-allard/#56" aria-description="Citation for case: Andrus v. Allard">444 U. S. 51, 56</a></span> (1979); <em>Blue Chip Stamps </em>v. <em>Manor Drug Stores, </em><span class="citation" data-id="9426100"><a href="/opinion/109267/blue-chip-stamps-v-manor-drug-stores/#756" aria-description="Citation for case: Blue Chip Stamps v. Manor Drug Stores">421 U. S. 723, 756</a></span> (1975) (Powell, J., concurring). By its terms, § 1983 “creates a species of tort liability that on its face admits of no immunities.” <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#417" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 417</a></span> (1976). Its language is absolute and unqualified; no mention is made of any privileges, immunities, or defenses that may be asserted. Bather, the Act imposes liability upon <em>“every person” </em>who, under color of state law or custom, “subjects, or causes to be subjected, any citizen of the United States ... to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws.”<footnotemark>16</footnotemark> And <em>Monell </em>held that these words were intended to encompass municipal corporations as well as natural “persons.”</p>
<p id="b695-7">Moreover, the congressional debates surrounding the passage of § 1 of the Civil Rights Act of 1871, <span class="citation no-link">17 Stat. 13</span> — the forerunner of § 1983 — confirm the expansive sweep of the stat<page-number citation-index="1" label="636">*636</page-number>utory language. Representative Shellabarger, the author and manager of the bill in the House, explained in his introductory remarks the breadth of construction that the Act was to receive:</p>
<blockquote id="b696-5">“I have a single remark to make in regard to the rule of interpretation of those provisions of the Constitution under which all the sections of the bill are framed. This act is remedial, and in aid of the preservation of human liberty and human rights. All statutes and constitutional provisions authorizing such statutes are liberally and beneficently construed. It would be most strange and, in civilized law, monstrous were this not the rule of interpretation. As has been again and again decided by your own Supreme Court of the United States, and everywhere else where there is wise judicial interpretation, the largest latitude consistent with the words employed is uniformly given in construing such statutes and constitutional provisions as are meant to protect and defend and give remedies for their wrongs to all the people.” Cong. Globe, 42d Cong., 1st Sess., App. 68 (1871) (hereinafter Globe App.).</blockquote>
<p id="b696-6">Similar views of the Act’s broad remedy for violations of federally protected rights were voiced by its supporters in both Houses of Congress. See <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#683" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 683-687</a></span>.<footnotemark>17</footnotemark></p>
<p id="b697-4"><page-number citation-index="1" label="637">*637</page-number>However, notwithstanding § 1983’s expansive language and the absence of any express incorporation of common-law immunities, we have, on several occasions, found that a tradition of immunity was so firmly rooted in the common law and was supported by such strong policy reasons that “Congress would have specifically so provided had it wished to abolish the doctrine.” <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 555</a></span> (1967). Thus in <em>Tenney </em>v. <em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">Brandhove, supra,</a></span> </em>after tracing the development of an absolute legislative privilege from its source in 16th-century England to its inclusion in the Federal and State Constitutions, we concluded that Congress “would [not] impinge on a tradition so well grounded in history and reason by covert inclusion in the general language” of § 1983. <span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/#376" aria-description="Citation for case: Tenney v. Brandhove">341 U. S., at 376</a></span>.</p>
<p id="b697-5">Subsequent cases have required that we consider the personal liability of various other types of government officials. Noting that “[f]ew doctrines were more solidly established at common law than the immunity of judges from liability for damages for acts committed within their judicial jurisdiction,” <em>Pierson </em>v. <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#553" aria-description="Citation for case: Pierson v. Ray"><em>Ray, supra, </em>at 553-554</a></span>, held that the absolute immunity traditionally accorded judges was preserved under § 1983. In that same case, local police officers were held to enjoy a “good faith and probable cause” defense to § 1983 suits similar to that which existed in false arrest actions at common law. <span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#555" aria-description="Citation for case: Pierson v. Ray">386 U. S., at 555-557</a></span>. Several more recent decisions have found immunities of varying scope appropriate for different state and local officials sued under § 1983. See <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/" aria-description="Citation for case: Procunier v. Navarette">434 U. S. 555</a></span> (1978) (qualified im<page-number citation-index="1" label="638">*638</page-number>munity for prison officials and officers); <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409</a></span> (1976) (absolute immunity for prosecutors in initiating and presenting the State’s case); <em>O’Connor </em>v. <em>Donaldson, </em><span class="citation" data-id="9842006"><a href="/opinion/109303/oconnor-v-donaldson/" aria-description="Citation for case: O&#x27;Connor v. Donaldson">422 U. S. 563</a></span> (1975) (qualified immunity for superintendent of state hospital); <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975) (qualified immunity for local school board members) ; <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974) (qualified “good-faith” immunity for state Governor and other executive officers for discretionary acts performed in the course of official conduct).</p>
<p id="b698-5">In each of these cases, our finding of § 1983 immunity “was predicated upon a considered inquiry into the immunity historically accorded the relevant official at common law and the interests behind it.” <em>Imbler </em>v. <span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#421" aria-description="Citation for case: Imbler v. Pachtman"><em>Pachtman, supra, </em>at 421</a></span>. Where the immunity claimed by the defendant was well established at common law at the time § 1983 was enacted, and where its rationale was compatible with the purposes of the Civil Eights Act, we have construed the statute to incorporate that immunity. But there is no tradition of immunity for municipal corporations, and neither history nor policy supports a construction of § 1983 that would justify the qualified immunity accorded the city of Independence by the Court of Appeals. We hold, therefore, that the municipality may not assert the good faith of its officers or agents as a defense to liability under § 1983.<footnotemark>18</footnotemark></p>
<p id="b698-6">A</p>
<p id="b698-7">Since colonial times, a distinct feature of our Nation’s system of governance has been the conferral of political power upon public and municipal corporations for the management of matters of local concern. As <em>Monell </em>recounted, by 1871, <page-number citation-index="1" label="639">*639</page-number>municipalities — like private corporations — were treated as natural persons for virtually all purposes of constitutional and statutory analysis. In particular, they were routinely sued in both federal and state courts. See <span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#687" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 687-688</a></span>. Cf. <em>Cowles </em>v. <em>Mercer County, </em><span class="citation" data-id="87989"><a href="/opinion/87989/cowles-v-mercer-county/" aria-description="Citation for case: Cowles v. Mercer County">7 Wall. 118</a></span> (1869). Local governmental units were regularly held to , answer in damages for a wide range of statutory and constitutional violations, as well as for common-law actions for breach of contract.<footnotemark>19</footnotemark> And although, as we discuss below,<footnotemark>20</footnotemark> a municipal<page-number citation-index="1" label="640">*640</page-number>ity was not subject to suit for all manner of tortious conduct, it is clear that at the time § 1983 was enacted, local governmental bodies did not enjoy the sort of “good-faith” qualified immunity extended to them by the Court of Appeals.</p>
<p id="b700-5">As a general rule, it was understood that a municipality’s tort liability in damages was identical to that of private corporations and individuals:</p>
<blockquote id="b700-6">“There is nothing in the character of a municipal corporation which entitles it to an immunity from liability for such malfeasances as private corporations or individuals would be liable for in a civil action. A municipal corporation is liable to the same extent as an individual for any act done by the express authority of the corporation, or of a branch of its government, empowered to act for it upon the subject to which the particular act relates, and for any act which, after it has been done, has been lawfully ratified by the corporation.” T. Shear-man &amp; A. Redfield, A Treatise on the Law of Negligence § 120, p. 139 (1869) (hereinafter Shearman &amp; Redfield).</blockquote>
<p id="b700-7">Accord, 2 Dillon § 764, at 875 (“But as respects <em>municipal corporations proper, </em>... it is, we think, universally considered, even in the absence of statute giving the action, that they are liable for acts of <em>misfeasance </em>positively injurious to individuals, done by their authorized agents or officers, in the course of the performance of corporate powers constitutionally conferred, or in the execution of corporate duties”) (emphasis in original). See 18 E. McQuillin, Municipal Corporations § 53.02 (3d rev. ed. 1977) (hereinafter McQuillin). Under this general theory of liability, a municipality was deemed responsible for any private losses generated through a wide variety of its operations and functions, from personal injuries due to its defective sewers, thoroughfares, and public utilities, to property damage caused by its trespasses and uncompensated takings.<footnotemark>21</footnotemark></p>
<p id="b701-4"><page-number citation-index="1" label="641">*641</page-number>Yet in the hundreds of cases from that era awarding damages against municipal governments for wrongs committed by them, one searches in vain for much mention of a qualified immunity based on the good faith of municipal officers. Indeed, where the issue was discussed at all, the courts had rejected the proposition that a municipality should be privileged where it reasonably believed its actions to be lawful. In the leading case of <em>Thayer </em>v. <em>Boston, </em><span class="citation" data-id="6407157"><a href="/opinion/6533444/thayer-v-city-of-boston/#515" aria-description="Citation for case: Thayer v. City of Boston">36 Mass. 511, 515-516</a></span> (1837), for example, Chief Justice Shaw explained:</p>
<blockquote id="b701-5">“There is a large class of cases, in which the rights of both the public and of individuals may be deeply involved, in which it cannot be known at the time the act is done, whether it is lawful or not. The event of a legal inquiry, in a court of justice, may show that it was unlawful. Still, if it was not known and understood to be! unlawful at the time, if it was an act done by the officers! having competent authority, either by express vote of \ the city government, or by the nature of the duties and ! functions with which they are charged, by their offices, to act upon the general subject matter, and especially if the j act was done with an honest view to obtain for the public j some lawful benefit or advantage, reason and justice ob- ¡ viously require that the city, in its corporate capacity, should be liable to make good the damage sustained by an individual, in consequence of the acts thus done.” ]</blockquote>
<p id="b701-6">The <em><span class="citation" data-id="6407157"><a href="/opinion/6533444/thayer-v-city-of-boston/" aria-description="Citation for case: Thayer v. City of Boston">Thayer</a></span> </em>principle was later reiterated by courts in several jurisdictions, and numerous decisions awarded damages against municipalities for violations expressly found to have been committed in good faith. See, <em>e. g., Town Council of Akron </em>v. <em>McComb, </em><span class="citation no-link">18 Ohio 229</span>, 230-231 (1849); <em>Horton </em>v. <em>Inhabitants of Ipswich, </em><span class="citation" data-id="6410190"><a href="/opinion/6536470/horton-v-inhabitants-of-ipswich/#489" aria-description="Citation for case: Horton v. Inhabitants of Ipswich">66 Mass. 488, 489, 492</a></span> (1853); <em>Elliot </em>v. <em>Concord, </em>27 N. H. 204 (1853); <em>Hurley </em>v. <em>Town of Texas, </em><span class="citation" data-id="6599597"><a href="/opinion/6718747/hurley-v-town-of-texas/#637" aria-description="Citation for case: Hurley v. Town of Texas">20 Wis. 634, 637-638</a></span> (1866); <em>Lee </em>v. <em>Village of Sandy Hill, </em><span class="citation" data-id="3597827"><a href="/opinion/3615537/lee-v-the-village-of-sandy-hill/#448" aria-description="Citation for case: Lee v. . the Village of Sandy Hill">40 N. Y. <page-number citation-index="1" label="642">*642</page-number>442, 448-451</a></span> (1869); <em>Billings </em>v. <em>Worcester, </em><span class="citation" data-id="6415781"><a href="/opinion/6542057/billings-v-city-of-worcester/#332" aria-description="Citation for case: Billings v. City of Worcester">102 Mass. 329, 332-333</a></span> (1869); <em>Squiers </em>v. <em>Village of Neenah, </em><span class="citation" data-id="6600295"><a href="/opinion/6719394/squiers-v-village-of-neenah/#593" aria-description="Citation for case: Squiers v. Village of Neenah">24 Wis. 588, 593</a></span> (1869); <em>Hawks </em>v. <em>Charlemont, </em><span class="citation" data-id="6416517"><a href="/opinion/6542791/hawks-v-inhabitants-of-charlemont/#417" aria-description="Citation for case: Hawks v. Inhabitants of Charlemont">107 Mass. 414, 417-418</a></span> (1871).<footnotemark>22</footnotemark></p>
<p id="b702-4">That municipal corporations were commonly held liable for damages in tort was also recognized by the 42d Congress. See <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#688" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 688</a></span>. For example, Senator Stevenson, in opposing the Sherman amendment’s creation of a municipal liability for the riotous acts of its inhabitants, stated the prevailing law: "Numberless cases are to be found where a statutory liability has been created against municipal corporations for injuries resulting from a neglect of corporate duty.” Cong. <page-number citation-index="1" label="643">*643</page-number>Globe, 42d Cong., 1st Sess., 762 (hereinafter Globe).<footnotemark>23</footnotemark> Nowhere in the debates, however, is there a suggestion that the common law excused a city from liability on account of the good faith of its authorized agents, much less an indication of a congressional intent to incorporate such an immunity into the Civil Rights Act.<footnotemark>24</footnotemark> The absence of any allusion to a municipal immunity assumes added significance in light of the objections raised by the opponents of § 1 of the Act that its unqualified language could be interpreted to abolish the traditional good-faith immunities enjoyed by legislators, judges, governors, sheriffs, and other public officers.<footnotemark>25</footnotemark> Had <page-number citation-index="1" label="644">*644</page-number>there been a similar common-law immunity for municipalities, the bill’s opponents doubtless would have raised the specter of its destruction, as well.</p>
<p id="b704-5">To be sure, there were two doctrines that afforded municipal corporations some measure of protection from tort liability. The first sought to distinguish betweeá a municipality’s “governmental” and “proprietary” functions; as to the former, the city was held immune, whereas in its exercise of the latter, the city was held to the same standards of liability as any private corporation. The second doctrine immunized a municipality for its “discretionary” or “legislative” activities, but not for those which were “ministerial” in nature. A brief examination of the application and the rationale underlying each of these doctrines demonstrates that Congress could not have intended them to limit a municipality’s liability under § 1983.</p>
<p id="b704-6">The governmental-proprietary distinction <footnotemark>26</footnotemark> owed its existence to the dual nature of the municipal corporation. On <page-number citation-index="1" label="645">*645</page-number>the one hand, the municipality was a corporate body, capable of performing the same “proprietary” functions as any private corporation, and liable for its torts in the same manner and to the same extent, as well. On the other hand, the municipality was an arm of the State, and when acting in that “governmental” or “public” capacity, it shared the immunity traditionally accorded the sovereign.<footnotemark>27</footnotemark> But the principle of sovereign immunity — itself a somewhat arid fountainhead for municipal immunity<footnotemark>28</footnotemark> — is necessarily nullified when the <page-number citation-index="1" label="646">*646</page-number>State expressly or impliedly allows itself, or its creation, to be sued. Municipalities were therefore liable not only for their “proprietary” acts, but also for those “governmental” functions as to which the State had withdrawn their immunity. And, by the end of the 19th century, courts regularly held that in imposing a specific duty on the municipality either in its charter or by statute, the State had impliedly withdrawn the city’s immunity from liability for the nonperformance or misperformance of its obligation. See, <em>e. g., Weightman </em>v. <em>The Corporation of Washington, </em><span class="citation" data-id="87436"><a href="/opinion/87436/weightman-v-corporation-of-washington/#50" aria-description="Citation for case: Weightman v. Corporation of Washington">1 Black 39, 50-52</a></span> (1862); <em>Providence </em>v. <em>Clapp, </em><span class="citation" data-id="86918"><a href="/opinion/86918/city-of-providence-v-clapp/#167" aria-description="Citation for case: City of Providence v. Clapp">17 How. 161, 167-169</a></span> (1855). See generally Shearman &amp; Redfield §§ 122-126; Note, Liability of Cities for the Negligence and Other Misconduct of their Officers and Agents, <span class="citation no-link">30 Am. St. Rep. 376</span>, 385 (1893). Thus, despite the nominal existence of an immunity for “governmental” functions, municipalities were found <page-number citation-index="1" label="647">*647</page-number>liable in damages in a multitude of cases involving such activities.</p>
<p id="b707-5">That the municipality’s common-law immunity for “governmental” functions derives from the principle of sovereign immunity also explains why that doctrine could not have served as the basis for the qualified privilege respondent city claims under § 1983. First, because, sovereign immunity insulates the municipality from unconsented suits altogether, the pres-enee or absence of good faith is simply irrelevant. The critical issue is whether injury occurred while the city was exercising- governmental, as opposed to pioprietary, powers or obligations — not whether its agents reasonably believed they were acting lawfully in so conducting themselves.<footnotemark>29</footnotemark> Morfundamentally, however, the municipality’s “governmental” immunity is obviously abrogated by the sovereign’s enacment of a statute making it amenable to suit. Section 1983 was just such a statute. By including municipalities within the class of “persons” subject to liability for violations of the Federal Constitution and laws, Congress — the supreme sovereign on matters of federal law<footnotemark>30</footnotemark> — abolished whatever ves<page-number citation-index="1" label="648">*648</page-number>tige of the State’s sovereign immunity the municipality possessed.</p>
<p id="b708-5">The second common-law distinction between municipal functions — that protecting the city from suits challenging “discretionary” decisions — was grounded not on the principle of sovereign immunity, but on a concern for separation of powers. A large part of the municipality’s responsibilities involved broad discretionary decisions on issues of public policy — decisions that affected large numbers of persons and called for a delicate balancing of competing considerations. For a court or jury, in the guise of a tort suit, to review the reasonableness of the city’s judgment on these matters would be an infringement upon the powers properly vested in a coordinate and coequal branch of government. See <em>Johnson </em>v. <em>State, </em><span class="citation multiple-matches"><a href="/c/Cal.%202d/69/782/">69 Cal. 2d 782</a></span>, 794, n. 8, <span class="citation" data-id="9574558"><a href="/opinion/1312748/johnson-v-state-of-california/#361" aria-description="Citation for case: Johnson v. State of California">447 P. 2d 352, 361, n. 8</a></span> (1968) (en banc) (“Immunity for ‘discretionary’ activities serves no purpose except to assure that courts refuse to pass judgment on policy decisions in the province of coordinate branches of government”). In order to ensure against any invasion into the legitimate sphere of the municipality’s policymaking processes, courts therefore refused to entertain suits against the city “either for the non-exercise of, or for the manner in which in good faith it exercises, <em>discretionary powers </em>of a public or legislative character.” 2 Dillon § 753, at 862.<footnotemark>31</footnotemark></p>
<p id="b708-6">Although many, if not all, of a municipality’s activities would seem to involve at least some measure of discretion, the influence of this doctrine on the city’s liability was not as significant as might be expected. For just as the courts <page-number citation-index="1" label="649">*649</page-number>implied an exception to the municipality’s immunity for its “governmental” functions, here, too, a distinction was made that had the effect of subjecting the city to liability for much of its tortious conduct. While the city retained its immunity for decisions as to whether the public interest required acting in one manner or another, once any particular decision was made, the city was fully liable for any injuries incurred in the execution of its judgment. See, <em>e. g., Hill </em>v. <em>Boston, </em><span class="citation" data-id="6418891"><a href="/opinion/6545160/hill-v-city-of-boston/#358" aria-description="Citation for case: Hill v. City of Boston">122 Mass. 344, 358-359</a></span> (1877) (dicta) (municipality would be immune from liability for damages resulting from its decision where to construct sewers, since that involved a discretionary judgment as to the general public interest; but city would be liable for neglect in the construction or repair of any particular sewer, as such activity is ministerial in nature). See generally C. Rhyne, Municipal Law § 30.4, pp. 736-737 (1957); Williams § 7. Thus municipalities remained liable in damages for a broad range of conduct implementing their disere-/ tionary decisions.</p>
<p id="b709-5">Once again, an understanding of the rationale underlying the common-law immunity for “discretionary” functions explains why that doctrine cannot serve as the foundation for a good-faith immunity under § 1983. That common-law doctrine merely prevented courts from substituting their own judgment on matters within the lawful discretion of the municipality. But a municipality has no “discretion” to violate the Federal Constitution; its dictates are absolute and imperative. And when a court passes judgment on the municipality’s conduct in a § 1983 action, it does not seek to second-guess the “reasonableness” of the city’s decision nor to interfere with the local government’s resolution of competing policy considerations. Rather, it looks only to whether the municipality has conformed to the requirements of the Federal Constitution and statutes. As was stated in <em>Sterling </em>v. <em>Constantin, </em><span class="citation" data-id="101991"><a href="/opinion/101991/sterling-v-constantin/#398" aria-description="Citation for case: Sterling v. Constantin">287 U. S. 378, 398</a></span> (1932): “When there is a substantial showing that the exertion of state power has <page-number citation-index="1" label="650">*650</page-number>overridden private rights secured by that Constitution, the subject is necessarily one for judicial inquiry in an appropriate proceeding directed against the individuals charged with the transgression.”</p>
<p id="b710-5">In sum, we can discern no “tradition so well grounded in history and-reason” that would warrant the conclusion that in enacting § 1 of the Civil Rights Act, the 42d Congress <em>sub silentio </em>extended to municipalities a qualified immunity based on the good faith of their officers. Absent any clearer indication that Congress intended so to limit the reach of a statute expressly designed to provide a “broad remedy for violations of federally protected civil rights,” <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#685" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S., at 685</a></span>, we are unwilling to suppose that injuries occasioned by a municipality’s unconstitutional conduct were not also meant to be fully redressable through its sweep.<footnotemark>32</footnotemark></p>
<p id="b710-6">B</p>
<p id="b710-7">Our rejection of a construction of § 1983 that would accord municipalities a qualified immunity for their good-faith constitutional violations is compelled both by the legislative purpose in enacting the statute and by considerations of public policy. The central aim of the Civil Rights Act was to provide protection to those persons wronged by the “ ‘[mjisuse of power, possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law.’ ” <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 184</a></span> (quoting <em>United States </em>v. <em>Classic, </em><span class="citation" data-id="9419158"><a href="/opinion/103531/united-states-v-classic/#326" aria-description="Citation for case: United States v. Classic">313 U. S. 299, 326</a></span> (1941)). By creating an express federal remedy, Congress sought to “enforce provisions of the Fourteenth Amendment against those <page-number citation-index="1" label="651">*651</page-number>who carry a badge of authority of a State and represent it in some capacity, whether they act in accordance with their authority or misuse it.” <em>Monroe </em>v. <span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#172" aria-description="Citation for case: Monroe v. Pape"><em>Pape, supra, </em>at 172</a></span>.</p>
<p id="b711-5">How “uniquely amiss” it would be, therefore, if the government itself — “the social organ to which all in our society look for the promotion of liberty, justice, fair and equal treatment, and the setting of worthy norms and goals for social conduct” — were permitted to disavow liability for the injury it has begotten. See <em>Adickes </em>v. <em>Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#190" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 190</a></span> (1970) (opinion of Brennan, J.). A damages remedy against the offending' party is a vital component of any scheme for vindicating cherished constitutional guarantees, and the importance of assuring its efficacy is only accentuated when the wrongdoer is the institution that has been established to protect the very rights it has transgressed: Yet owing to the qualified immunity enjoyed by most government officials, see <em>Scheuer </em>v. <em>Rhodes, </em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232</a></span> (1974), many victims of municipal malfeasance would be left remediless if the city were also allowed to assert a good-faith defense. Unless countervailing considerations counsel otherwise, the injustice of such a result should not be tolerated.<footnotemark>33</footnotemark></p>
<p id="b711-6">Moreover, § 1983 was intended not only to provide compensation to the victims of past abuses, but to serve as a deterrent against future constitutional deprivations, as well. See <em>Robertson </em>v. <em>Wegmann, </em><span class="citation" data-id="9427228"><a href="/opinion/109877/robertson-v-wegmann/#590" aria-description="Citation for case: Robertson v. Wegmann">436 U. S. 584, 590-591</a></span> (1978); <em>Carey </em>v. <em>Piphus, </em><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/#256" aria-description="Citation for case: Carey v. Piphus">435 U. S. 247, 256-257</a></span> (1978). The knowledge that a municipality will be liable for all of its injurious conduct, whether committed in good faith or not, should create <page-number citation-index="1" label="652">*652</page-number>an incentive for officials who may harbor doubts about the lawfulness of their intended actions to err on the side of protecting citizens’ constitutional rights.<footnotemark>34</footnotemark> Furthermore, the threat that damages might be levied against the city may encourage those in a policymaking position to institute internal rules and programs designed to minimize the likelihood of unintentional infringements on constitutional rights.<footnotemark>35</footnotemark> Such procedures are particularly beneficial in preventing those “systemic” injuries that result not so much from the conduct of any single individual, but from the interactive behavior of several government officials, each of whom may be acting in good faith. Cf. Note, Developments in the Law: Section 1983 and Federalism, <span class="citation no-link">90 Harv. L. Rev. 1133</span>, 1218-1219 (1977).<footnotemark>36</footnotemark></p>
<p id="b712-5">Our previous decisions conferring qualified immunities on various government officials, see <em>supra, </em>at 637-638, are not to <page-number citation-index="1" label="653">*653</page-number>be read as derogating the significance of the societal interest in compensating the innocent victims of governmental misconduct. Rather, in each case we concluded that overriding considerations of public policy nonetheless demanded that the official be given a measure of protection from personal liability. The concerns that justified those decisions, however, are less compelling, if not wholly inapplicable, when the liability of the municipal entity is at issue.<footnotemark>37</footnotemark></p>
<p id="b714-4"><page-number citation-index="1" label="654">*654</page-number>In <em>Scheuer </em>v. <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#240" aria-description="Citation for case: Scheuer v. Rhodes"><em>Rhodes, supra, </em>at 240</a></span>, The Chief Justice identified the two “mutually dependent rationales” on which the doctrine of official immunity rested:</p>
<blockquote id="b714-5">“(1) the injustice, particularly in the absence of bad faith, of subjecting to liability an officer who is required, by the legal obligations of his position, to exercise discretion; (2) the danger that the threat of such liability would deter his willingness to execute his office with the decisiveness and the judgment required by the public good.”<footnotemark>38</footnotemark></blockquote>
<p id="b714-6">The first consideration is simply not implicated when the damages award comes not from the official’s pocket, but from the public treasury. It hardly seems unjust to require a municipal defendant which has violated a citizen’s constitutional rights to compensate him for the injury suffered thereby. Indeed, Congress enacted § 1983 precisely to provide a remedy for such abuses of official power. See <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/#171" aria-description="Citation for case: Monroe v. Pape">365 U. S., at 171-172</a></span>. Elemental notions of fairness dictate that one who causes a loss should bear the loss.</p>
<p id="b714-7">It has been argued, however, that revenue raised by taxation for public use should not be diverted to the benefit of a single or discrete group of taxpayers, particularly where the municipality has at all times acted in good faith. On the contrary, the accepted view is that stated in <em>Thayer </em>v. <em>Boston </em>— " that the city, in its corporate capacity, should be liable to make good the damage sustained by an [unlucky] indi<page-number citation-index="1" label="655">*655</page-number>vidual, in consequence of the acts thus done.” <span class="citation" data-id="6407157"><a href="/opinion/6533444/thayer-v-city-of-boston/#515" aria-description="Citation for case: Thayer v. City of Boston">36 Mass., at 515</a></span>. After all, it is the public at large which enjoys the benefits of the government’s activities, and it is the public at large which is ultimately responsible for its administration. Thus, even where some constitutional development could not have been foreseen by municipal officials, it is fairer to allocate any resulting financial loss to the inevitable costs of government borne by all the taxpayers, than to allow its impact to be felt solely by those whose rights, albeit newly recognized, have been violated. See generally 3 K. Davis, Administrative Law Treatise §25.17 (1958 and Supp. 1970); Prosser § 131, at 978; Michelman, Property, Utility, and Fairness: Some Thoughts on the Ethical Foundations of “Just Compensation” Law, <span class="citation no-link">80 Harv. L. Rev. 1165</span> (1967).<footnotemark>39</footnotemark></p>
<p id="b715-5">The second rationale mentioned in <em><span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/" aria-description="Citation for case: Scheuer v. Rhodes">Scheuer</a></span> </em>also loses its force when it is the municipality, in contrast to the official, whose liability is at issue. At the heart of this justification for a qualified immunity for the individual official is the concern that the threat of <em>personal </em>monetary liability will introduce an unwarranted and unconscionable consideration into the decisionmaking process, thus paralyzing the governing official’s decisiveness and distorting his judgment on matters <page-number citation-index="1" label="656">*656</page-number>of public policy.<footnotemark>40</footnotemark> The inhibiting effect is significantly reduced, if not eliminated, however, when the threat of personal liability is removed. First, as an empirical matter, it is questionable whether the hazard of municipal loss will deter a public officer from the conscientious exercise of his duties; city officials routinely make decisions that either require a large expenditure of municipal funds or involve a substantial risk of depleting the public fisc. See <em>Kostka </em>v. <em>Hogg, </em><span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#41" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d 37, 41</a></span> (CA1 1977). More important, though, is the realization that consideration of the <em>municipality’s </em>liability for constitutional violations is quite properly the concern of its elected or appointed officials. Indeed, a decisionmaker would be derelict in his duties if, at some point, he did not consider whether his decision comports with constitutional mandates and did not weigh the risk that a violation might result in an award of damages from the public treasury. As one commentator aptly put it: “Whatever other concerns should shape a particular official's actions, certainly one of them should be the constitutional rights of individuals who will be affected by his actions. To criticize section 1983 liability because it leads decisionmakers to avoid the infringement of constitutional rights is to criticize one of the statute’s <em>raisons </em>d’etre.”<footnotemark>41</footnotemark></p>
<p id="b717-4"><page-number citation-index="1" label="657">*657</page-number>IV</p>
<p id="b717-5">In sum, our decision holding that municipalities have no immunity from damages liability flowing from their constitutional violations harmonizes well with developments in the common law and our own pronouncements on official immunities under § 1983. Doctrines of tort law have changed significantly over the past century, and our notions of governmental responsibility should properly reflect that evolution. No longer is individual “blameworthiness” the acid test of liability; the principle of equitable loss-spreading has.joined fault as a factor in distributing the costs of official misconduct.</p>
<p id="b717-6">We believe that today’s decision, together with prior precedents in this area, properly allocates these costs among the three principals in the scenario of the § 1983 cause of action: the victim of the constitutional deprivation; the officer whose conduct caused the injury; and the public, as represented by the municipal entity. The innocent individual who is harmed by an abuse of governmental authority is assured that he will be compensated for his injury. The offending official, so long as he conducts himself in good faith, may go about his business secure in the knowledge that a qualified immunity will protect him from personal liability for damages that are more appropriately chargeable to the populace as a whole. And the public will be forced to bear only the costs of injury inflicted by the “execution of a government’s policy or custom, whether made by its lawmakers or by those whose edicts or acts may fairly be said to represent official policy.” <page-number citation-index="1" label="658">*658</page-number><em>Monell </em>v. <em>New York City Dept. of Social Services, </em>436 U. S., at 694.</p>
<p id="b718-4">
<em>Reversed.</em>
</p>
<footnote label="1">
<p id="b684-9"> Title <span class="citation no-link">42 U. S. C. § 1983</span> provides:</p>
<blockquote id="b684-10">“Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.”</blockquote>
</footnote>
<footnote label="2">
<p id="b685-8"> Under § 3.3 (1) of the city’s charter, the City Manager has sole authority to “[a]ppoint, and when deemed necessary for the good of the service, lay off, suspend, demote, or remove all directors, or heads, of administrative departments and all other administrative officers and employees of the city. . . .”</p>
</footnote>
<footnote label="3">
<p id="b686-8"> Alberg returned from his vacation on the morning of April 17, and immediately met informally with four members of the City Council. Although the investigation of the Police Department was discussed, and although Alberg testified that he had found a replacement for petitioner by that time, he did not inform the Council members of his intention to discharge petitioner.</p>
</footnote>
<footnote label="4">
<p id="b687-6"> The letter, dated April 15,1972, stated in part:</p>
<blockquote id="b687-7">“My counsel . . . have advised me that even though the City Charter may give you authority to relieve me, they also say you cannot do so without granting me my constitutional rights of due process; which includes a written charge and specifications, together with a right to a public hearing and to be represented by counsel and to cross-examine those who may. appear against me.</blockquote>
<blockquote id="b687-8">"In spite of your recent investigation and your public statement given to the public press, your relief and discharge of me without a full public hearing upon written charges will leave in the minds of the public and those who might desire to have my services, a stigma of personal wrongdoing on my part.</blockquote>
<blockquote id="b687-9">“Such action by you would be in violation of my civil rights as granted by the Constitution and Congress of the United States and you would be liable in damages to me. Further it would be in violation of the Missouri Administrative Procedure Act.</blockquote>
<blockquote id="b687-10">“May I have an expression from you that you do not intend to relieve me or in the alternative give me a written charge and specifications of your basis for your grounds of intention to relieve me and to grant me a public hearing with a reasonable opportunity to respond to the charge and a right to be represented by counsel.”</blockquote>
<p id="b687-11">City Manager Alberg stated that he did not receive the letter until after petitioner's discharge.</p>
</footnote>
<footnote label="5">
<p id="b687-12"> Roberts’ statement, which is reproduced in full in <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/#1116" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp. 1110, 1116, n. 2</a></span> (1976), in part recited:</p>
<blockquote id="b687-13">“On April 2, 1972, the City Council was notified of the existence of an investigative report concerning the activities of the Chief of Police of the <page-number citation-index="1" label="628">*628</page-number>City of Independence, certain police officers and activities of one or more other City officials. On Saturday, April 15th for the first time I was able to see these 27 voluminous reports. The contents of these reports are astoundingly shocking and virtually unbelievable. They deal with the disappearance of 2 or more television sets from the police department and signed statement that they were taken by the Chief of Police for his own personal use.</blockquote>
<blockquote id="b688-6">“The reports show that numerous firearms properly in the police department custody found their way into the hands of others including undesirables and were later found by other law enforcement agencies.</blockquote>
<blockquote id="b688-7">“Reports whow [sic] that narcotics held by the Independence Missouri Chief of Police have mysteriously disappeared. Reports also indicate money has mysteriously disappeared. Reports show that traffic tickets have been manipulated. The reports show inappropriate requests affecting the police court have come from high ranking police officials. Reports indicate that things have occurred causing the unusual release of felons. The reports show gross inefficiencies on the part of a few of the high ranking officers of the police department.</blockquote>
<blockquote id="b688-8">“In view of the contents of these reports, I feel that the information in the reports backed up by signed statements taken by investigators is so bad that the council should immediately make available to the news media access to copies of all of these 27 voluminous investigative reports so the public can be told what has been going on in Independence. I further believe that copies of these reports should be turned over and referred to the prosecuting attorney of Jackson County, Missouri for consideration and presentation to the next Grand Jury. I further insist that the City Manager immediately take direct and appropriate action, permitted under the Charter, against such persons as are shown by the investigation to have been involved.”</blockquote>
</footnote>
<footnote label="6">
<p id="b689-7"> Ironically, the official minutes of the City Council meeting indicate that concern was expressed by some members about possible adverse legal consequences that could flow from their release of the reports to the media. The City Counselor assured the Council that although an action might be maintained against any witnesses who made unfounded accusations, “the City does have governmental immunity in this area . . . and neither the Council nor the City as a municipal corporation can be held liable for libelous slander.” App. 20-23.</p>
</footnote>
<footnote label="7">
<p id="b689-8"> See n. 2, <em>supra.</em></p>
</footnote>
<footnote label="8">
<p id="b689-9"> The investigation and its culmination in petitioner’s firing received front-page attention in the local press. See, e. <em>g., </em>“Lid Off Probe, Council Seeks Action,” Independence Examiner, Apr. 18, 1972, Tr. 24-25; “Independence Accusation. Police Probe Demanded,” Kansas City Times, Apr. 18, 1972, Tr. 25; “Probe Culminates in Chief’s Dismissal,” Independence Examiner, Apr. 19, 1972, Tr. 26; “Police Probe Continues; Chief Ousted,” Community Observer, Apr. 20, 1972, Tr. 26.</p>
</footnote>
<footnote label="9">
<p id="b690-7"> Petitioner did not join former Councilman Roberts in the instant litigation. A separate action seeking defamation damages was brought in state court against Roberts and Alberg in their individual capacities. Petitioner dismissed the state suit against Alberg and reached a financial settlement with Roberts. See <span class="citation multiple-matches"><a href="/c/F.%202d/560/925/">560 F. 2d 925</a></span>, 930 (CA8 1977).</p>
</footnote>
<footnote label="10">
<p id="b690-8"> The District Court, relying on <em>Monroe </em>v. <em>Pape, </em><span class="citation" data-id="9422118"><a href="/opinion/106170/monroe-v-pape/" aria-description="Citation for case: Monroe v. Pape">365 U. S. 167</a></span> (1961), and <em>City of Kenosha </em>v. <em>Bruno, </em><span class="citation" data-id="9425343"><a href="/opinion/108813/city-of-kenosha-v-bruno/" aria-description="Citation for case: City of Kenosha v. Bruno">412 U. S. 507</a></span> (1973), held that § 1983 did not create a cause of action against the city, but that petitioner could base his claim for relief directly on the Fourteenth Amendment. On the merits, however, the court determined that petitioner’s discharge did not deprive him of any constitutionally protected property interest because, as an untenured employee, he possessed neither a contractual nor a <em>de facto </em>right to continued employment as Chief of Police. Similarly, the court found that the circumstances of petitioner’s dismissal did not impose a stigma of illegal or immoral conduct on his professional reputation, and hence did not deprive him of any liberty interest.</p>
<p id="b690-9">The District Court offered three reasons to support its conclusion: First, because the actual discharge notice stated only that petitioner was “[t]er-minated under the provisions of Section 3.3 (1) of the City Charter,” nothing in his official record imputed any stigmatizing conduct to him. .Second, the court found that the City Council’s actions had no causal connection to petitioner’s discharge, for City Manager Alberg had apparently <page-number citation-index="1" label="631">*631</page-number>made his decision to hire a new Police Chief before the-Council’s April 17th meeting. Lastly, the District Court determined that petitioner was “completely exonerated” from any charges of illegal or immoral conduct by the City Counselor’s investigative report, Alberg’s public statements, and the grand jury’s return of a “no true bill.” <span class="citation" data-id="1770095"><a href="/opinion/1770095/owen-v-city-of-independence-mo/#1121" aria-description="Citation for case: Owen v. City of Independence, Mo.">421 F. Supp., at 1121-1122</a></span>.</p>
<p id="b691-6">As an alternative ground for denying relief, the District Court ruled that the city was entitled to assert, and had in fact established, a qualified immunity against liability based on the good faith of the individual defendants who acted as its agents: “[Defendants have clearly shown by a preponderance of the evidence that neither they, nor their predecessors, were aware, in April 1972, that, under the circumstances, the Fourteenth Amendment accorded plaintiff the procedural rights of notice and a hearing at the time of his discharge. Defendants have further proven that they cannot reasonably be charged with constructive notice of such rights since plaintiff was discharged prior to the publication of the Supreme Court decisions in <em>Roth </em>v. <em>Board of Regents, </em>[<span class="citation" data-id="9425009"><a href="/opinion/108608/board-of-regents-of-state-colleges-v-roth/" aria-description="Citation for case: Board of Regents of State Colleges v. Roth">408 U. S. 564</a></span> (1972)], and <em>Perry </em>v. <em>Sindermann, </em>[<span class="citation" data-id="9425012"><a href="/opinion/108609/perry-v-sindermann/" aria-description="Citation for case: Perry v. Sindermann">408 U. S. 593</a></span> (1972)].” <em>Id., </em>at 1123.</p>
</footnote>
<footnote label="11">
<p id="b691-7"> Both parties had appealed from, the District Court’s decision. On respondents’ challenge to the court’s assumption of subject-matter jurisdiction under <span class="citation no-link">28 U. S. C. § 1331</span>, the Court of Appeals held that the city was subject to suit for reinstatement and backpay under an implied right of action arising directly from the Fourteenth Amendment. <span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#932" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d, at 932-934</a></span>. See <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971). Because the Court of Appeals concluded that petitioner’s claim could rest directly on the Fourteenth Amendment, it saw no need to decide whether he could recover backpay under § 1983 from the individual defendants in their official capacities as part of general equitable relief, even though the award would be paid by the city. <span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#932" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d, at 932</a></span>.</p>
</footnote>
<footnote label="12">
<p id="b692-6"> As compensation for the denial of his constitutional rights, the Court of Appeals awarded petitioner damages in lieu of backpay. The court explained that petitioner’s termination without a hearing must be considered a nullity, and that ordinarily he ought to remain on the payroll and receive wages until a hearing is held and a proper determination on his retention is made. But because petitioner had reached the mandatory retirement age during the course of the litigation, he could not be reinstated to his former position. Thus the compensatory award was to be measured by the amount of money petitioner would likely have earned to retirement had he not been deprived of his good name by the city’s actions, subject to mitigation by the amounts actually earned, as well as by the recovery from Councilman Roberts in the state defamation suit.</p>
<p id="b692-7">The Court of Appeals rejected the municipality’s assertion of a good-faith defense, relying upon a footnote in <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#314" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 314-315, n. 6</a></span> (1975) (“immunity from damages does not ordinarily bar equitable relief as well”), and two of its own precedents awarding back-pay in § 1983 actions against school boards. See <em>Wellner </em>v. <em>Minnesota State Jr. College Bd., </em><span class="citation" data-id="9460015"><a href="/opinion/314754/gary-a-wellner-v-minnesota-state-junior-college-board/" aria-description="Citation for case: Gary A. Wellner v. Minnesota State Junior College Board">487 F. 2d 153</a></span> (CA8 1973); <em>Cooley </em>v. <em>Board of Educ. of Forrest City School Dist., </em><span class="citation" data-id="300696"><a href="/opinion/300696/j-f-cooley-appellant-v-the-board-of-education-of-the-forrest-city/" aria-description="Citation for case: J. F. COOLEY, Appellant, v. the BOARD OF EDUCATION OF the...">453 F. 2d 282</a></span> (CA8 1972). The court concluded that the primary justification for a qualified immunity — the fear that public officials might hesitate to discharge their duties if faced with the prospect of personal monetary liability — simply did not exist where the relief would be borne by a governmental unit rather than the individual officeholder. In addition, the Court of Appeals seemed to take issue with the District Court’s finding of good faith on the part of the City Council: “The city officials may have acted in good faith in refusing the hearing, but lack of good faith is evidenced by the nature of the unfair attack made upon the appellant by Roberts in the official conduct of the City’s business. The District Court did not address the good faith defense in light of Roberts’ defamatory remarks.” <span class="citation" data-id="348313"><a href="/opinion/348313/alan-s-kostka-v-david-w-hogg/#941" aria-description="Citation for case: Alan S. Kostka v. David W. Hogg">560 F. 2d, at 941</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b693-6"> Although respondents did not cross petition on this issue, they have raised a belated challenge to the Court of Appeals’ ruling that petitioner was deprived of a protected “liberty” interest. See Brief for Respondents 45-46. We find no merit in their contention, however, and decline to disturb the determination of the court below.</p>
<p id="b693-7"><em>Wisconsin </em>v. <em>Constantineau, </em><span class="citation" data-id="9424387"><a href="/opinion/108230/wisconsin-v-constantineau/#437" aria-description="Citation for case: Wisconsin v. Constantineau">400 U. S. 433, 437</a></span> (1971), held that “[w]here a person’s good name, reputation, honor, or integrity is at stake because of what the government is doing to him, notice and an opportunity to be heard are essential.” In <em>Board of Regents </em>v. <em>Roth, </em><span class="citation" data-id="9425009"><a href="/opinion/108608/board-of-regents-of-state-colleges-v-roth/#573" aria-description="Citation for case: Board of Regents of State Colleges v. Roth">408 U. S. 564, 573</a></span> (1972), we explained that the dismissal of a government employee accompanied by a “charge against him that might seriously damage his standing and associations in his community” would qualify as something “the government is doing to him,” so as to trigger the due process right to a hearing at which the employee could refute the charges and publicly clear his name. In the present case, the city — through the unanimous resolution of the City Council — released to the public an allegedly false statement impugning petitioner’s honesty and integrity. Petitioner was discharged <page-number citation-index="1" label="634">*634</page-number>the next day. The Council’s accusations received extensive coverage in the press, and even if they did not in point of fact “cause” petitioner’s discharge, the defamatory and stigmatizing charges certainly “occur[red] in the course of the termination of employment.” Cf. <em>Paid </em>v. <em>Davis, </em><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/#710" aria-description="Citation for case: Paul v. Davis">424 U. S. 693, 710</a></span> (1976). Yet the city twice refused petitioner’s request that he be given written specification of the charges against him and an opportunity to clear his name. Under the circumstances, we have no doubt that the Court of Appeals correctly concluded that the city’s actions deprived petitioner of liberty without due process of law.</p>
</footnote>
<footnote label="14">
<p id="b694-7"> Cf. <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 322</a></span> (1975) (“Therefore, in the specific context of school discipline, we hold that a school board member is not immune from liability for damages under § 1983 if he knew or reasonably should have known that the action he took within his sphere of official responsibility would violate the constitutional rights of the student affected, or if he took the action with the malicious intention to cause a deprivation of constitutional rights or other injury to the student”).</p>
</footnote>
<footnote label="15">
<p id="b695-8"> The Courts of Appeals are divided on the question whether local governmental units are entitled to a qualified immunity based on the good faith of their officials. Compare <em>Bertot </em>v. <em>School Dist. No. 1, </em><span class="citation" data-id="9466405"><a href="/opinion/373716/donna-bertot-v-school-district-no-1-albany-county-wyoming/" aria-description="Citation for case: Donna Bertot v. School District No. 1, Albany County,...">613 F. 2d 245</a></span> (CA10 1979) (en banc), <em>Hostrop </em>v. <em>Board of Junior College Dist. No. 615, </em><span class="citation" data-id="330296"><a href="/opinion/330296/richard-w-hostrop-v-board-of-junior-college-district-no-515-counties-of/" aria-description="Citation for case: Richard W. Hostrop v. Board of Junior College District...">523 F. 2d 569</a></span> (CA7 1975), and <em>Hander </em>v. <em>San Jacinto Jr. College, </em><span class="citation" data-id="9461921"><a href="/opinion/328776/lecil-hander-v-san-jacinto-junior-college-etc/" aria-description="Citation for case: Lecil Hander v. San Jacinto Junior College, Etc.">519 F. 2d 273</a></span> (CA5), rehearing denied, <span class="citation" data-id="329966"><a href="/opinion/329966/lecil-hander-v-san-jacinto-junior-college-etc/" aria-description="Citation for case: Lecil Hander v. San Jacinto Junior College, Etc.">522 F. 2d 204</a></span> (1975), all refusing to extend a qualified immunity to the governmental entity, with <em>Paxman </em>v. <em>Campbell, </em><span class="citation" data-id="8910764"><a href="/opinion/8921863/paxman-v-campbell/" aria-description="Citation for case: Paxman v. Campbell">612 F. 2d 848</a></span> (CA4 1980) (en banc), and <em>Seda </em>v. <em>County of Suffolk, </em><span class="citation" data-id="369082"><a href="/opinion/369082/diane-sala-v-county-of-suffolk-philip-f-corso-sheriff-of-the-county-of/" aria-description="Citation for case: Diane Sala v. County of Suffolk, Philip F. Corso, Sheriff...">604 F. 2d 207</a></span> (CA2 1979), granting defendants a “good-faith” immunity.</p>
</footnote>
<footnote label="16">
<p id="b695-9"> See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="17">
<p id="b696-7"> As we noted in <em>Monell </em>v. <em>New York City Dept. of Social Services, </em>see 436 U. S., at 685-686, n. 45, even the opponents of § 1 acknowledged that its language conferred upon the federal courts the entire power that Congress possessed to remedy constitutional violations. The remarks of Senator Thurman are illustrative:</p>
<blockquote id="b696-8">“[This section’s] whole effect is to give to the Federal Judiciary that which now does not belong to it — a jurisdiction that may be constitutionally conferred upon it, I grant, but that has never yet been conferred upon it. It authorizes any person who is deprived of any right, privilege, or immunity secured to him by the Constitution of the United States, to bring an action <page-number citation-index="1" label="637">*637</page-number>against the wrong-doer in the Federal courts, and that without any limit whatsoever as to the amount in controversy. . . .</blockquote>
<blockquote id="b697-7"><em>. . </em>That is the language of this bill. Whether it is the intent or not I know not, but it is the language of the bill; for there is no limitation whatsoever upon the terms that are employed, and they are as comprehensive as can be used.” Globe App. 216-217.</blockquote>
</footnote>
<footnote label="18">
<p id="b698-8"> The governmental immunity at issue in the present case differs significantly from the official immunities involved in our previous decisions. In those cases, various government officers had been sued in their individual capacities, and the immunity served to insulate them from personal liability for damages. Here, in contrast, only the liability of the municipality itself is at issue, not that of its officers, and in the absence of an immunity, any recovery would come from public funds.</p>
</footnote>
<footnote label="19">
<p id="b699-5"> Primary among the constitutional suits heard in federal court were those based on a municipality’s violation of the Contract Clause, and the courts’ enforcement efforts often included “various forms of ‘positive’ relief, such as ordering that taxes be levied and collected to discharge federal-court judgments, once a constitutional infraction was found.” <em>Monell </em>v. <em>New York City Dept. of Social </em>Services, 436 U. S., at 681. Damages actions against municipalities for federal statutory violations were also entertained.. See, <em>e. g., Levy Court </em>v. <em>Coroner, </em><span class="citation" data-id="87666"><a href="/opinion/87666/levy-court-v-coroner/" aria-description="Citation for case: Levy Court v. Coroner">2 Wall. 501</a></span> (1865); <em>Corporation of New York </em>v. <em>Ransom, </em><span class="citation" data-id="87361"><a href="/opinion/87361/mayor-aldermen-and-commonalty-of-city-of-new-york-v-ransom/" aria-description="Citation for case: Mayor, Aldermen, and Commonalty, of City of New York v....">23 How. 487</a></span> (1860); <em>Bliss </em>v. <em>Brooklyn, </em><span class="citation" data-id="8628671"><a href="/opinion/8648861/bliss-v-brooklyn/" aria-description="Citation for case: Bliss v. Brooklyn">3 F. Cas. 706</a></span> (No. 1,544) (CC EDNY 1871). In addition, state constitutions and statutes, as well as municipal charters, imposed many obligations upon the local governments, the violation of which typically gave rise to damages actions against the city. See generally Note, Streets, Change of Grade, Liability of Cities for, <span class="citation no-link">30 Am. St. Rep. 835</span> (1893), and cases cited therein. With respect to authorized contracts — and even unauthorized contracts that are later ratified by the corporation — municipalities were liable in the same manner as individuals for their breaches. See generally 1 J. Dillon, Law of Municipal Corporations §§385, 394 (2d ed. 1873) (hereinafter Dillon). Of particular relevance to the instant case, included within the class of contract actions brought against a city were those for the wrongful discharge of a municipal employee, and where the claim was adjudged meritorious, damages in the nature of backpay were regularly awarded. See, <em>e. g., Richardson </em>v. <em>School Dist. No. 10, </em><span class="citation" data-id="6578118"><a href="/opinion/6698118/richardson-v-school-district-no-10/" aria-description="Citation for case: Richardson v. School District No. 10">38 Vt. 602</a></span> (1866); <em>Paul </em>v. <em>School Dist. No. 2, </em><span class="citation" data-id="6575930"><a href="/opinion/6695961/paul-v-school-district-no-2/" aria-description="Citation for case: Paul v. School District No. 2">28 Vt. 575</a></span> (1856); <em>Inhabitants of Searsmont </em>v. <em>Farwell, </em>3 Me. *450 (1825); see generally F. Burke, A Treatise on the Law of Public Schools 81-85 (1880). The most frequently litigated “breach of contract” suits, however, at least in federal court, were those for failure to pay interest on municipal bonds. See, <em>e. g., The Supervisors </em>v. <em>Durant, </em><span class="citation" data-id="88174"><a href="/opinion/88174/supervisors-v-durant/" aria-description="Citation for case: Supervisors v. Durant">9 Wall. 415</a></span> (1870); <em>Commissioners of Knox County </em>v. <em>Aspinwall, </em><span class="citation" data-id="9416661"><a href="/opinion/87248/board-of-commrs-of-knox-cty-v-aspinwall/" aria-description="Citation for case: Board of Comm&#x27;rs of Knox Cty. v. Aspinwall">21 How. 539</a></span> (1859).</p>
</footnote>
<footnote label="20">
<p id="b699-6"> See <em>infra, </em>at 644-650.</p>
</footnote>
<footnote label="21">
<p id="b700-8"> See generally C. Rhyne, Municipal Law 729-789 (1957); Shearman <em>&amp; </em><page-number citation-index="1" label="641">*641</page-number>Redfield §§ 143-152; W. Williams, Liability of Municipal Corporations for Tort (1901) (hereinafter Williams).</p>
</footnote>
<footnote label="22">
<p id="b702-5"> Accord, <em>Bunker </em>v. <em>City of Hudson, </em><span class="citation" data-id="8187937"><a href="/opinion/8224334/bunker-v-city-of-hudson/#54" aria-description="Citation for case: Bunker v. City of Hudson">122 Wis. 43, 54</a></span>, <span class="citation" data-id="8187937"><a href="/opinion/8224334/bunker-v-city-of-hudson/#452" aria-description="Citation for case: Bunker v. City of Hudson">99 N. W. 448, 452</a></span> (1904); <em>Oklahoma City </em>v. <em>Hill Bros., </em><span class="citation" data-id="3829428"><a href="/opinion/4071499/city-of-oklahoma-city-v-hill-bros/#137" aria-description="Citation for case: City of Oklahoma City v. Hill Bros.">6 Okla. 114, 137-139</a></span>, <span class="citation" data-id="3829428"><a href="/opinion/4071499/city-of-oklahoma-city-v-hill-bros/#249" aria-description="Citation for case: City of Oklahoma City v. Hill Bros.">50 P. 242, 249-250</a></span> (1897); <em>Schussler </em>v. <em>Board of Comm’rs of Hennepin County, </em><span class="citation" data-id="7969795"><a href="/opinion/8014737/schussler-v-board-of-commissioners/#417" aria-description="Citation for case: Schussler v. Board of Commissioners">67 Minn. 412, 417</a></span>, <span class="citation" data-id="7969795"><a href="/opinion/8014737/schussler-v-board-of-commissioners/#7" aria-description="Citation for case: Schussler v. Board of Commissioners">70 N. W. 6, 7</a></span> (1897); <em>McGraw </em>v. <em>Town of Marion, </em><span class="citation" data-id="7133323"><a href="/opinion/7221215/mcgraw-v-town-of-marion/#680" aria-description="Citation for case: McGraw v. Town of Marion">98 Ky. 673, 680-683</a></span>, <span class="citation" data-id="7133323"><a href="/opinion/7221215/mcgraw-v-town-of-marion/#20" aria-description="Citation for case: McGraw v. Town of Marion">34 S. W. 18, 20-21</a></span> (1896). See generally Note, Liability of Cities for the Negligence and Other Misconduct of their Officers and Agents, <span class="citation no-link">30 Am. St. Rep. 376</span>, 405-411 (1893).</p>
<p id="b702-6">Even in England, where the doctrine of official immunity followed by the American courts was first established, no immunity was granted where the damages award was to come from the public treasury. As Baron Bramwell stated in <em>Buck </em>v. <em>Williams, </em>3 H. &amp; N. 308, 320, 157 Eng. Rep. 488, 493 (Exch. 1858):</p>
<blockquote id="b702-7">“I can well understand if a person undertakes the office or duty of a Commissioner, and there are no means of indemnifying him against the consequences of a slip, it is reasonable to hold that he should not be responsible for it. I can also understand that, if one of several Commissioners does something not within the scope of his authority, the Commissioners as a body are not liable. But where Commissioners, who are a quasi corporate body, are not affected <em>[i. e., </em>personally] by the result of an action, inasmuch as they are authorized by act of parliament to raise a fund for payment of the damages, on what principle is it that, if an individual member of the public suffers from an act bona fide but erroneously done, he is not to be compensated? It seems to me inconsistent with actual justice, and not warranted by any principle of law.”</blockquote>
<p id="b702-8">See generally Shearman &amp; Redfield §§ 133, 178.</p>
</footnote>
<footnote label="23">
<p id="b703-5"> Senator Stevenson proceeded to read from the decision in <em>Prather </em>v. <em>Lexington, </em><span class="citation" data-id="7129316"><a href="/opinion/7217313/prather-v-city-of-lexington/#560" aria-description="Citation for case: Prather v. City of Lexington">52 Ky. 559, 560-562</a></span> (1852):</p>
<blockquote id="b703-6">“Where a particular act, operating injuriously to an individual, is authorized by a municipal corporation, by a delegation of power either general or special, it will be liable for the injury in its corporate capacity, where the acts done would warrant a like action against an individual. But as a general rule a corporation is not responsible for the unauthorized and unlawful acts of its officers, although done under the color of their office; to render it liable it must appear that it expressly authorized the acts to be done by them, or that they were done in pursuance of a general authority to act for the corporation, on the subject to which they relate. <em>(Thayer </em>v. <em>Boston, </em><span class="citation no-link">19 Pick., 511</span>.) It has also been held that cities are responsible to the same extent, and in the same manner, as natural persons for injuries occasioned by the negligence or unskillfulness of their agents jn the constmction .of works for their benefit.” Globe 762.</blockquote>
</footnote>
<footnote label="24">
<p id="b703-7"> At one point in the'debafesPSenator Stevenson did protest that the Sherman amendment would, for the first time, “create a corporate liability for personal injury which no prudence or foresight could have prevented.” <em><span class="citation no-link">Ibid.</span> As </em>his later remarks made clear, however, Stevenson’s objection went only to the novelty of the amendment’s creation of vicarious municipal liability for the unlawful acts of private individuals, “even if a municipality did not know of an impending or ensuing riot or did not have the wherewithal to do anything about it.” <em>Monell </em>v. <em>New York City Dept. of Social Services, </em>436 U. S., at 692-693, n. 57.</p>
</footnote>
<footnote label="25">
<p id="b703-8"> See, <em>e. g., </em>Globe 365 (remarks of Rep. Arthur) (“But if the Legislature enacts a law, if the Governor enforces it, if the judge upon the bench renders a judgment, if the sheriff levy an execution, execute a writ, serve a summons, or make an arrest, all acting under a solemn, official oath, <page-number citation-index="1" label="644">*644</page-number>though as pure in duty as a saint and as immaculate as a seraph, for a mere error in judgment, they are liable. . .”); <em>id., </em>at 385 (remarks of Rep. Lewis); Globe App. 217 (remarks of Sen. Thurman).</p>
</footnote>
<footnote label="26">
<p id="b704-8"> In actuality, the distinction between a municipality’s governmental and proprietary functions is better characterized not as a line, but as a succession of points. In efforts to avoid the often-harsh results occasioned by a literal application of the test, courts frequently created highly artificial and elusive distinctions of their own. The result was that the very same activity might be considered “governmental” in one jurisdiction, and “proprietary” in another. See 18 McQuillin § 53.02, at 105. See also W. Prosser, Law of Torts § 131, p. 979 (4th ed. 1971) (hereinafter Pros-ser) . As this Court stated, in reference to the “ ‘nongovernmental’-‘governmental’ quagmire that has long plagued the law of municipal corporations”: “A comparative study of the cases in the forty-eight States will disclose an irreconcilable conflict. More than that, the decisions in each of the States are disharmonious and disclose the inevitable chaos when courts try to apply a rule of law that is inherently unsound.” <em>Indian Towing Co. </em>v. <em>United States, </em><span class="citation" data-id="9421210"><a href="/opinion/105329/indian-towing-co-v-united-states/#65" aria-description="Citation for case: Indian Towing Co. v. United States">350 U. S. 61, 65</a></span> (1955) (on rehearing).</p>
</footnote>
<footnote label="27">
<p id="b705-5"> “While acting in their governmental capacity, municipal corporations proper are given the benefit of that same rule which is applied to the sovereign power itself, and are afforded complete immunity from civil responsibility for acts done or omitted, unless such responsibility is expressly created by statute. When, however, they are not acting in the exercise of their purely governmental functions, but are performing duties that pertain to the exercise of those private franchises, powers, and privileges which belong to them for theirown. corporate benefit, or are dealing with property held by them for their own corporate gain or emolument, then a different rule of liability is applied and they are generally held responsible for injuries arising from their negligent acts or their omissions to the same extent as a private corporation under like circumstances.” Williams §4, at 9. See generally 18 McQuillin §§53.02, 53.04, 53.24; Prosser § 131, at 977-983; James, Tort Liability of Governmental Units and Their Officers, <span class="citation no-link">22 U. Chi. L. Rev. 610</span>, 611-612, 622-629 (1955).</p>
</footnote>
<footnote label="28">
<p id="b705-6"> Although it has never been understood how the doctrine of sovereign immunity came to be adopted in the American democracy, it apparently stems from the personal immunity of the English Monarch as expressed in the maxim, “The King can do no wrong.” It has been suggested, however, that the meaning traditionally ascribed to this phrase is an ironic perversion of its original intent: “The maxim merely meant that the King was not privileged to do wrong. If his acts were against the law, they were <em>injuriae </em>(wrongs). Bracton, while ambiguous in his several statements as to the relation between the King and the law, did not intend .to convey the idea that he was incapable of committing a legal wrong.” Borchard, Government Liability in Tort, 34 Yale L. J. 1, 2, n. 2 (1924). See also Kates &amp; Kouba, Liability of Public Entities Under Section 1983 of the Civil Rights Act, <span class="citation no-link">45 S. Cal. L. Rev. 131</span>, 142 (1972).</p>
<p id="b705-7">In this country, “[t]he sovereign or governmental immunity doctrine, holding that the state, its subdivisions and municipal entities, may not be <page-number citation-index="1" label="646">*646</page-number>held liable for tortious acts, was never completely accepted by the courts, its underlying principle being deemed contrary to the basic concept of the law of torts that liability follows negligence, as well as foreign to the spirit of the constitutional guarantee that every person is entitled to a legal remedy for injuries he may receive in his person or property. As a result, the trend of judicial decisions was always to restrict, rather than to expand, the doctrine of municipal immunity.” 18 McQuillin § 53.02, at 104 (footnotes omitted). See also Prosser § 131, at 984 (“For well over a century the immunity of both the state and the local governments for their torts has been subjected to vigorous criticism, which at length has begun to have its effect”). The seminal opinion of the Florida Supreme Court in <em>Hargrove </em>v. <em>Town of Cocoa Beach, </em><span class="citation" data-id="1696303"><a href="/opinion/1696303/hargrove-v-town-of-cocoa-beach/" aria-description="Citation for case: Hargrove v. Town of Cocoa Beach">96 So. 2d 130</a></span> (1957), has spawned “a minor avalanche of decisions repudiating municipal immunity,” Prosser § 131, at 985, which, in conjunction with legislative abrogation of sovereign immunity, has resulted in the consequence that only a handful of States still cling to the old common-law rule of immunity for governmental functions. See K. Davis, Administrative Law of the Seventies §25.00 (1976 and Supp. 1977) (only two States adhere to the traditional common-law immunity from torts in the exercise of governmental functions); Harley &amp; Wasinger, Government Immunity: Despotic Mantle or Creature of Necessity, 16 Washburn L. J. 12, 34-53 (1976).</p>
</footnote>
<footnote label="29">
<p id="b707-6"> The common-law immunity for governmental functions is thus more comparable to an absolute immunity from liability for conduct of a certain character, which defeats a suit at the outset, than to a qualified immunity, which “depends upon the circumstances and motivations of [the official’s] actions, as established by the evidence at trial.” <em>Imbler </em>v. <em>Pachtman, </em><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/#419" aria-description="Citation for case: Imbler v. Pachtman">424 U. S. 409, 419, n. 13</a></span> (1976).</p>
</footnote>
<footnote label="30">
<p id="b707-7"> Municipal defenses — including an assertion of sovereign immunity— to a federal right of action are, of course, controlled by federal law. See <em>Fitzpatrick </em>v. <em>Bitzer, </em><span class="citation" data-id="9426527"><a href="/opinion/109520/fitzpatrick-v-bitzer/#455" aria-description="Citation for case: Fitzpatrick v. Bitzer">427 U. S. 445, 455-456</a></span> (1976); <em>Hampton </em>v. <em>Chicago, </em><span class="citation multiple-matches"><a href="/c/F.%202d/484/602/">484 F. 2d 602</a></span>, 607 (CA7 1973) (Stevens, J.) (“Conduct by persons acting under color of state law which is wrongful under <span class="citation no-link">42 U. S. C. § 1983</span> or § 1985 (3) cannot be immunized by state law. A construction of the federal statute which permitted a state immunity defense to have controlling effect would transmute a basic guarantee into an illusory promise; and the supremacy clause of the Constitution insures that the proper construction may be enforced”).</p>
</footnote>
<footnote label="31">
<p id="b708-7"> See generally 18 McQuillin § 53.04a; Shearman &amp; Redfield §§ 127-130; Williams § 6, at 15-16. Like the govemmental/proprietary distinction, a clear line between the municipality’s “discretionary” and “ministerial” functions was often hard to discern, a difficulty which has been mirrored in the federal courts’ attempts to draw a similar distinction under the Federal Tort Claims Act, <span class="citation no-link">28 U. S. C. §2680</span> (a). See generally 3 K. Davis, Administrative Law Treatise §25.08 (1958 and Supp. 1970).</p>
</footnote>
<footnote label="32">
<p id="b710-8"> Cf. P. Bator, P. Mishkin, D. Shapiro, <em>&amp; </em>H. Wechsler, Hart and Wechsler’s The Federal Courts and the Federal System 336 (2d ed. 1973) (“[W]here constitutional rights are at stake the courts are properly astute, in construing statutes, to avoid the conclusion that Congress intended to use the privilege of immunity ... in order to defeat them”).</p>
</footnote>
<footnote label="33">
<p id="b711-7"> The absence of any damages remedy for violations of all but the most “clearly established” constitutional rights, see <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#322" aria-description="Citation for case: Wood v. Strickland">420 U. S., at 322</a></span>, could also have the deleterious effect of freezing constitutional law in its current state of development, for without a meaningful remedy aggrieved individuals will have little incentive to seek vindication of those constitutional deprivations that have not previously been clearly defined.</p>
</footnote>
<footnote label="34">
<p id="b712-6"> For example, given the discussion that preceded the Independence City Council’s adoption of the allegedly slanderous resolution impugning petitioner’s integrity, see n. 6, <em>supra, </em>one must wonder whether this entire litigation would have been necessary had the Council members thought that the city might be liable for their misconduct.</p>
</footnote>
<footnote label="35">
<p id="b712-7"> Cf. <em>Albemarle Paper Co. </em>v. <em>Moody, </em><span class="citation" data-id="9426162"><a href="/opinion/109299/albemarle-paper-co-v-moody/#417" aria-description="Citation for case: Albemarle Paper Co. v. Moody">422 U. S. 405, 417-418</a></span> (1975): “If employers faced only the prospect of an injunctive order, they would have little incentive to shun practices of dubious legality. It is the reasonably certain prospect of a backpay award that ‘provide[s] the spur or catalyst which causes employers and unions to self-examine and to self-evaluate their employment practices and. to endeavor to eliminate, so far as possible, the last vestiges of an unfortunate and ignominious page in this country’s history.’ <em>United States </em>v. <em>N. L. Industries, Inc., </em><span class="citation" data-id="8890222"><a href="/opinion/8903207/united-states-v-n-l-industries-inc/#379" aria-description="Citation for case: United States v. N. L. Industries, Inc.">479 F. 2d 354, 379</a></span> (CA8 1973).”</p>
</footnote>
<footnote label="36">
<p id="b712-8"> In addition, the threat of liability against the city ought to increase the attentiveness with which officials at the higher levels of government supervise the conduct of their subordinates. The need to institute system-wide measures in order to increase the vigilance with which otherwise indifferent municipal officials protect citizens’ constitutional rights Js, of course, particularly acute where the frontline officers are judgment-proof in their individual capacities.</p>
</footnote>
<footnote label="37">
<p id="b713-5"> On at least two previous occasions, this Court has expressly recognized that different considerations come into play when governmental rather than personal liability is threatened. <em>Hutto </em>v. <em>Finney, </em><span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678</a></span> (1978), affirmed an award of attorney’s fees out of state funds for a deprivation of constitutional rights, holding that such an assessment would not contravene the Eleventh Amendment. In response to the suggestion, adopted by the dissent, that any award should be borne by the government officials personally, the Court noted that such an allocation would not only be “manifestly unfair,” but would,“def[y] this Court’s insistence in a related context that imposing personal liability in the absence of bad faith may cause state officers to ‘exercise their discretion with undue timidity.’ <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#321" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 321</a></span>.” <em>Id., </em>at 699, n. 32. The Court thus acknowledged that imposing personal liability on public officials could have an undue chilling effect on the exercise of their decision-making responsibilities, but that no such pernicious consequences were likely to flow from the possibility of a recovery from public funds.</p>
<p id="b713-6">Our decision in <em>Lake Country Estates, Inc. </em>v. <em>Tahoe Regional Planning Agency, </em><span class="citation" data-id="9427483"><a href="/opinion/110033/lake-country-estates-inc-v-tahoe-regional-planning-agency/" aria-description="Citation for case: Lake Country Estates, Inc. v. Tahoe Regional Planning Agency">440 U. S. 391</a></span> (1979), also recognized that the justifications for immunizing officials from personal liability have little force when suit is brought against the governmental entity itself. Petitioners in that case had sought damages under § 1983 from a regional planning agency and the individual members of its governing agency. Relying on <em>Tenney </em>v. <em>Brand-hove, </em><span class="citation" data-id="9420593"><a href="/opinion/104906/tenney-v-brandhove/" aria-description="Citation for case: Tenney v. Brandhove">341 U. S. 367</a></span> (1951), the Court concluded that “to the extent the evidence discloses that these individuals were acting in a capacity comparable to that of members- of a state legislature, they are entitled to absolute immunity from federal damages liability.” <span class="citation" data-id="9427483"><a href="/opinion/110033/lake-country-estates-inc-v-tahoe-regional-planning-agency/#406" aria-description="Citation for case: Lake Country Estates, Inc. v. Tahoe Regional Planning Agency">440 U. S., at 406</a></span>. At the same time, however, we cautioned: “If the respondents have enacted unconstitutional legislation, there is no reason why relief against TRPA itself should not adequately vindicate petitioners’ interests. See <em>Monell </em>v. <em>New York City Dept. of Social Services, </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658</a></span>.” <em>Id., </em>at 405, n. 29.</p>
</footnote>
<footnote label="38">
<p id="b714-8"> <em>Wood </em>v. <em>Strickland, </em><span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308</a></span> (1975), mentioned a third justification for extending a qualified immunity to public officials: the fear that the threat of personal liability might deter citizens from holding public office. See <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#320" aria-description="Citation for case: Wood v. Strickland"><em>id., </em>at 320</a></span> (“The most capable candidates for school board positions might be deterred from seeking office if heavy burdens upon their private resources from monetary liability were a likely prospect during their tenure”). Such fears are totally unwarranted, of course, once the threat of personal liability is eliminated.</p>
</footnote>
<footnote label="39">
<p id="b715-6"> <em>Monell </em>v. <em>New York City Dept. of Social Services </em>indicated that the principle of loss-spreading was an insufficient justification for holding the municipality liable under § 1983 on a <em>respondeat superior </em>theory. 436 U. S., at 693-694. Here, of course, quite a different situation is presented. Petitioner does not seek to hold the city responsible for the unconstitutional actions of an individual official <em>“solely </em>because it employs a tortfeasor.” <em>Id., </em>at 691. Rather, liability is predicated on a determination that “the action that is alleged to be unconstitutional implements or executes a policy statement, ordinance, regulation, or decision officially adopted and promulgated by that body’s officers.” <em>Id., </em>at 690. In this circumstance — when it is the local government itself that is responsible for the constitutional deprivation — it is perfectly reasonable to distribute the loss to the public as a cost of the administration of government, rather than to let the entire burden fall on the injured individual.</p>
</footnote>
<footnote label="40">
<p id="b716-5"> “The imposition of monetary costs for mistakes which were not unreasonable in the light of all the circumstances would undoubtedly deter even the most conscientious school decisionmaker from exercising his judgment independently, forcefully, and in a manner best serving the long-term interest of the school and the students.” <em>Wood </em>v. <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#319" aria-description="Citation for case: Wood v. Strickland"><em>Strickland, supra, </em>at 319-320</a></span>.</p>
</footnote>
<footnote label="41">
<p id="b716-6"> Note, Developments in the Law: Section 1983 and Federalism, <span class="citation no-link">90 Harv. L. Rev. 1133</span>, 1224 (1977). See also <em>Johnson </em>v. <em>State, </em><span class="citation multiple-matches"><a href="/c/Cal.%202d/69/782/">69 Cal. 2d 782</a></span>, 792-793, <span class="citation" data-id="9574558"><a href="/opinion/1312748/johnson-v-state-of-california/#359" aria-description="Citation for case: Johnson v. State of California">447 P. 2d 352, 359-360</a></span> (1968):</p>
<blockquote id="b716-7">“Nor do we deem an employee’s concern over the potential liability of his employer, the governmental unit, a justification for an expansive definition of 'discretionary/ and hence immune, acts. As a threshold matter, we consider it unlikely that the possibility of government liability will be <page-number citation-index="1" label="657">*657</page-number>a serious deterrent to the fearless exercise of judgment by the employee. In any event, however, to the extent that such a deterrent effect takes hold, it may be wholesome. An employee in a private enterprise naturally gives some consideration to the potential liability of his employer, and this attention unquestionably promotes careful work; the potential liability of a governmental entity, to the extent that it affects primary conduct at all, will similarly influence public employees.” (Citation and footnote omitted.)</blockquote>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Patterson v. Illinois.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Patterson v. Illinois"
type: case
citation: "487 U.S. 285 (1988)"
parallel_cite: "108 S. Ct. 2389; 101 L. Ed. 2d 261; 56 U.S.L.W. 4733"
neutral_cite: 1988 U.S. LEXIS 2876
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Patterson v. Illinois
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112127/patterson-v-illinois/"
  cluster_id: 112127
  opinion_id: 9431404
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brewer v. Williams]]", "[[Rothgery v. Gillespie County]]", "[[Michigan v. Jackson]]", "[[Edwards v. Arizona]]", "[[Montejo v. Louisiana]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "waiver", "post-indictment", "miranda"]
holding: "An accused may knowingly and intelligently waive the Sixth Amendment right to counsel for post-indictment questioning through the…"
lake:
  record_id: Patterson v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Patterson v. Illinois

*487 U.S. 285 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Patterson was indicted for a gang-related murder, and before he had retained or requested counsel, an officer informed him he had been formally charged, administered the *[[Miranda v. Arizona|Miranda]]* warnings, and questioned him. Patterson waived his rights and made incriminating statements, which were used at his trial.

## Issue
Whether an accused may waive his Sixth Amendment right to counsel for post-indictment questioning on the strength of the *[[Miranda v. Arizona|Miranda]]* warnings, where he has not retained or requested counsel.

## Rule
Yes. "As a general matter, then, an accused who is admonished with the warnings prescribed by this Court in *Miranda* . . . has been sufficiently apprised of the nature of his Sixth Amendment rights, and of the consequences of abandoning those rights, so that his waiver on this basis will be considered a knowing and intelligent one." — 487 U.S. at 296. ^pin-296

## Application
Patterson was given the *[[Miranda v. Arizona|Miranda]]* warnings, which informed him of his right to have counsel present during questioning and of the consequences of proceeding without one; under close questioning he could identify no additional information he should have received before deciding to waive. Because he had not retained or requested a lawyer, the warnings sufficiently apprised him of his Sixth Amendment rights, and his post-indictment waiver was knowing and intelligent. His statements were admissible.

## Conclusion
A *[[Miranda v. Arizona|Miranda]]*-warned waiver was a valid waiver of the Sixth Amendment right to counsel for post-indictment questioning on these facts; the conviction was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Patterson* remains good law; [[Montejo v. Louisiana]] later relied on it in overruling [[Michigan v. Jackson]], leaving *Patterson*'s waiver rule intact.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Patterson v. Illinois*, 487 U.S. 285 (1988) — https://www.courtlistener.com/opinion/112127/patterson-v-illinois/ — pinpoint: 296.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2a9bb046a129f73f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Patterson v. Illinois"}, "payload": {"all": [{"cite": "487 U.S. 285", "page": "285", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "487"}, {"cite": "108 S. Ct. 2389", "page": "2389", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "108"}, {"cite": "101 L. Ed. 2d 261", "page": "261", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "101"}, {"cite": "1988 U.S. LEXIS 2876", "page": "2876", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1988"}, {"cite": "56 U.S.L.W. 4733", "page": "4733", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "56"}], "display": "487 U.S. 285", "official": {"cite": "487 U.S. 285", "page": "285", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "487"}, "official_selection_present": true, "record_id": "Patterson v. Illinois"}}
{"assertion_id": "380c532adfa5596d", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-296", "record_id": "Patterson v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-296", "pinpoint_status": "slip-only", "quote": "--- # Patterson v. Illinois *487 U.S. 285 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Patterson was indicted for a gang-related murder, and before he had retained or requested counsel, an officer informed him he had been formally charged, administered the *Miranda* warnings, and questioned him. Patterson waived his rights and made incriminating statements, which were used at his trial. ## Issue Whether an accused may waive his Sixth Amendment right to counsel for post-indictment questioning on the strength of the *Miranda* warnings, where he has not retained or requested counsel. ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Patterson v. Illinois", "star_marker": null}}
{"assertion_id": "e6dcf9084a24973f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Patterson v. Illinois"}, "payload": {"as_of_content": "1988-06-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Patterson v. Illinois", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Patterson v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Patterson v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Patterson v. Illinois",
    "case_name_short": "Patterson",
    "case_name_full": "Patterson v. Illinois",
    "input_case_name": "Patterson v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-24",
    "year": 1988,
    "docket": null,
    "cluster_id": 112127,
    "lead_opinion_id": 9431404,
    "sibling_ids": [
      112127,
      9431404,
      9431405,
      9431406
    ],
    "absolute_url": "/opinion/112127/patterson-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9074851,
        "score": 20,
        "case_name": "Patterson v. Illinois"
      },
      {
        "cluster_id": 9074850,
        "score": 20,
        "case_name": "Patterson v. Illinois"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "487 U.S. 285",
      "volume": "487",
      "reporter": "U.S.",
      "page": "285",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 2389",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 L. Ed. 2d 261",
        "volume": "101",
        "reporter": "L. Ed. 2d",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4733",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4733",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2876",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2876",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "487 U.S. 285",
        "volume": "487",
        "reporter": "U.S.",
        "page": "285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 2389",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "2389",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 L. Ed. 2d 261",
        "volume": "101",
        "reporter": "L. Ed. 2d",
        "page": "261",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2876",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2876",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4733",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4733",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "487 U.S. 285",
    "official_selection": {
      "court_class": "scotus",
      "selected": "487 U.S. 285",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-296",
      "page": null,
      "quote": "--- # Patterson v. Illinois *487 U.S. 285 (1988)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After Patterson was indicted for a gang-related murder, and before he had retained or requested counsel, an officer informed him he had been formally charged, administered the *Miranda* warnings, and questioned him. Patterson waived his rights and made incriminating statements, which were used at his trial. ## Issue Whether an accused may waive his Sixth Amendment right to counsel for post-indictment questioning on the strength of the *Miranda* warnings, where he has not retained or requested counsel. ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Patterson v. Illinois",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jones v. Stephens",
          "cluster_id": 7317930,
          "cite": [
            "157 F. Supp. 3d 623",
            "2016 U.S. Dist. LEXIS 3888",
            "2016 WL 147919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Savino Braxton",
          "cluster_id": 2797003,
          "cite": [
            "784 F.3d 240",
            "2015 U.S. App. LEXIS 6990",
            "2015 WL 1905882"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt v. Hill, E.",
          "cluster_id": 2754405,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leonard Kidd v. Michael Lemke",
          "cluster_id": 2709205,
          "cite": [
            "734 F.3d 696",
            "2013 WL 5855718",
            "2013 U.S. App. LEXIS 22303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hodson v. State",
          "cluster_id": 2542781,
          "cite": [
            "350 S.W.3d 169",
            "2011 WL 1796088"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Crampe",
          "cluster_id": 5641118,
          "cite": [
            "17 N.Y.3d 469",
            "957 N.E.2d 255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
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
        "journal_ref": "Patterson v. Illinois:lane1_negative"
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
        "journal_ref": "Patterson v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kansas v. Ventris",
          "cluster_id": 145880,
          "cite": [
            "173 L. Ed. 2d 801",
            "129 S. Ct. 1841",
            "556 U.S. 586",
            "2009 U.S. LEXIS 3299"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane1_negative"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. Court of Appeal of California, Fourth Appellate District",
          "cluster_id": 118328,
          "cite": [
            "145 L. Ed. 2d 597",
            "120 S. Ct. 684",
            "528 U.S. 152",
            "2000 U.S. LEXIS 502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Iowa v. Tovar",
          "cluster_id": 134725,
          "cite": [
            "158 L. Ed. 2d 209",
            "124 S. Ct. 1379",
            "541 U.S. 77",
            "2004 U.S. LEXIS 1837"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Harvey",
          "cluster_id": 112385,
          "cite": [
            "108 L. Ed. 2d 293",
            "110 S. Ct. 1176",
            "494 U.S. 344",
            "1990 U.S. LEXIS 1229"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuller v. State",
          "cluster_id": 1575568,
          "cite": [
            "829 S.W.2d 191",
            "1992 Tex. Crim. App. LEXIS 62",
            "1992 WL 55274"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1407706,
          "cite": [
            "14 Cal. 4th 1005",
            "929 P.2d 544",
            "97 Daily Journal DAR 899",
            "97 Cal. Daily Op. Serv. 520",
            "60 Cal. Rptr. 2d 225",
            "1997 Cal. LEXIS 9"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Carter",
          "cluster_id": 2639408,
          "cite": [
            "70 P.3d 981",
            "135 Cal. Rptr. 2d 553",
            "30 Cal. 4th 1166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Traylor v. State",
          "cluster_id": 1765408,
          "cite": [
            "596 So. 2d 957",
            "1992 WL 4873"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rigoberto Moya-Gomez Celestino Orlando Estevez Amado Raphael Leon Adalberto Herrera and Menelao Orlando Estevez",
          "cluster_id": 513458,
          "cite": [
            "860 F.2d 706"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
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
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Collins",
          "cluster_id": 2518032,
          "cite": [
            "232 P.3d 32",
            "49 Cal. 4th 175",
            "110 Cal. Rptr. 3d 384",
            "2010 Cal. LEXIS 5032"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Sully",
          "cluster_id": 1386747,
          "cite": [
            "812 P.2d 163",
            "53 Cal. 3d 1195",
            "283 Cal. Rptr. 144",
            "91 Cal. Daily Op. Serv. 5489",
            "1991 Cal. LEXIS 2977"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Posada-Rios",
          "cluster_id": 16117,
          "cite": [
            "158 F.3d 832",
            "1998 WL 736317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Guerrero, Ex Parte Marcelino",
          "cluster_id": 2948089,
          "cite": [
            "400 S.W.3d 576",
            "2013 WL 2419595",
            "2013 Tex. Crim. App. LEXIS 820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Posada-Rios",
          "cluster_id": 758679,
          "cite": [
            "158 F.3d 832",
            "1998 WL 736317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 8437415,
          "cite": [
            "327 F.3d 56"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Patterson v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjEzNTc0NDAwMDAwJnM9MzE0Njk5NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112127+OR+9431404+OR+9431405+OR+9431406%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzkmcz0xNDU4ODAmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112127+OR+9431404+OR+9431405+OR+9431406%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406)",
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
    "complete_query": "cites:(112127 OR 9431404 OR 9431405 OR 9431406)",
    "indexed_citing_opinions": 643,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112127,
        "count": 574,
        "count_source": "search"
      },
      {
        "opinion_id": 9431404,
        "count": 86,
        "count_source": "search"
      },
      {
        "opinion_id": 9431405,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431406,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1013,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/patterson-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMjIwNTgmcz05MzkxNTQwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112127+OR+9431404+OR+9431405+OR+9431406%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112127,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 104496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 110809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 112074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 374894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 379999,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 418052,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 437719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 454503,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 1653387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 1875896,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 2037100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 2043878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112127,
        "cited_id": 2140351,
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
    "date_created": "2026-07-05T16:31:32Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:32:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:32:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:36:39Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:32:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Patterson v. Illinois

```
<opinion type="majority">
<author id="b339-8">Justice White</author>
<p id="Anm">delivered the opinion of the Court.</p>
<p id="b339-9">In this case, we are called on to determine whether the interrogation of petitioner after his indictment violated his Sixth Amendment right to counsel.</p>
<p id="AGdq">I</p>
<p id="b339-3">Before dawn on August 21, 1983, petitioner and other members of the “Vice Lords” street gang became involved in a fight with members of a rival gang, the “Black Mobsters.” Some time after the. fight, a former member of the Black Mobsters, James Jackson, went to the home where the Vice Lords had fled. A second fight broke out there, with petitioner and three other Vice Lords beating Jackson severely. The Vice Lords then put Jackson into a car, drove to the end of a nearby street, and left him face down in a puddle of water. Later that morning, police discovered Jackson, dead, where he had been left.</p>
<p id="b339-4">That afternoon, local police officers obtained warrants for the arrest of the Vice Lords, on charges of battery and mob action, in connection with the first fight. One of the gang members who was arrested gave the police a statement concerning the first fight; the statement also implicated several of the Vice Lords (including petitioner) in Jackson’s murder. A few hours later, petitioner was apprehended. Petitioner was informed of his rights under <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and volunteered to answer questions put to him by the police. Petitioner gave a statement concerning the initial fight between the rival gangs, but denied knowing anything <page-number citation-index="1" label="288">*288</page-number>about Jackson’s death. Petitioner was held in custody the following day, August 22, as law enforcement authorities completed their investigation of the Jackson murder.</p>
<p id="b340-5">On August 23, a Cook County grand jury indicted petitioner and two other gang members for the murder of James Jackson. Police Officer Michael Gresham, who had questioned petitioner earlier, removed him from the lockup where he was being held, and told petitioner that because he had been indicted he was being transferred to the Cook County jail. Petitioner asked Gresham which of the gang members had been charged with Jackson’s murder, and upon learning that one particular Vice Lord had been omitted from the indictments, asked: “[W]hy wasn’t he indicted, he did everything.” App. 7. Petitioner also began to explain that there was a witness who would support his account of the crime.</p>
<p id="b340-6">At this point, Gresham interrupted petitioner, and handed him a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver form. The form contained five specific warnings, as suggested by this Court’s <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision, to make petitioner aware of his right to counsel and of the consequences of any statement he might make to police.<footnotemark>1</footnotemark> Gresham read the warnings aloud, as petitioner read along with him. Petitioner initialed each of the five warnings, and signed the waiver form. Petitioner then gave a lengthy statement to police officers concerning the Jackson murder; petitioner’s statement described in detail the role of each of the Vice Lords — including himself — in the murder of James Jackson.</p>
<p id="b340-7">Later that day, petitioner confessed involvement in the murder for a second time. This confession came in an inter<page-number citation-index="1" label="289">*289</page-number>view with Assistant State’s Attorney (ASA) George Smith. At the outset of the interview, Smith reviewed with petitioner the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver he had previously signed, and petitioner confirmed that he had signed the waiver and understood his rights. Smith went through the waiver procedure once again: reading petitioner his rights, having petitioner initial each one, and sign a waiver form. In addition, Smith informed petitioner that he was a lawyer working with the police investigating the Jackson case. Petitioner then gave another inculpatory statement concerning the crime.</p>
<p id="b341-5">Before trial, petitioner moved to suppress his statements, arguing that they were obtained in a manner at odds with various constitutional guarantees. The trial court denied these motions, and the statements were used against petitioner at his trial. The jury found petitioner guilty of murder, and petitioner was sentenced to a 24-year prison term.</p>
<p id="b341-6">On appeal, petitioner argued that he had not “knowingly and intelligently” waived his Sixth Amendment right to counsel before he gave his uncounseled postindictment confessions. Petitioner contended that the warnings he received, while adequate for the purposes of protecting his <em>Fifth </em>Amendment rights as guaranteed by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>did not adequately inform him of his <em>Sixth </em>Amendment right to counsel. The Illinois Supreme Court, however, rejected this theory, applying its previous decision in <em>People </em>v. <em>Owens, </em><span class="citation" data-id="9724847"><a href="/opinion/2140351/people-v-owens/" aria-description="Citation for case: People v. Owens">102 Ill. 2d 88</a></span>, <span class="citation" data-id="9724847"><a href="/opinion/2140351/people-v-owens/" aria-description="Citation for case: People v. Owens">464 N. E. 2d 261</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./469/963/">469 U. S. 963</a></span> (1984), which had held that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were sufficient to make a defendant aware of his Sixth Amendment right to counsel during postindictment questioning. <em>People </em>v. <em>Thomas, </em><span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#298" aria-description="Citation for case: People v. Thomas">116 Ill. 2d 290, 298-300</a></span>, <span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#846" aria-description="Citation for case: People v. Thomas">507 N. E. 2d 843, 846-847</a></span> (1987).</p>
<p id="b341-7">In reaching this conclusion, the Illinois Supreme Court noted that this Court had reserved decision on this question on several previous occasions<footnotemark>2</footnotemark> and that the lower courts are <page-number citation-index="1" label="290">*290</page-number>divided on the issue. <span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#299" aria-description="Citation for case: People v. Thomas"><em>Id., </em>at 299</a></span>, <span class="citation" data-id="2043878"><a href="/opinion/2043878/people-v-thomas/#846" aria-description="Citation for case: People v. Thomas">507 N. E. 2d, at 846</a></span>. We granted this petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./484/895/">484 U. S. 895</a></span> (1987), to resolve this split of authority and to address the issues we had previously left open.</p>
<p id="b342-5">II</p>
<p id="b342-6">There can be no doubt that petitioner had the right to have the assistance of counsel at his postindictment interviews with law enforcement authorities. Our cases make it plain that the Sixth Amendment guarantees this right to criminal defendants. <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#629" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 629-630</a></span> (1986); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#398" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 398-401</a></span> (1977); <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#205" aria-description="Citation for case: Massiah v. United States">377 U. S. 201, 205-207</a></span> (1964).<footnotemark>3</footnotemark> Petitioner asserts that the questioning that produced his incriminating statements violated his Sixth Amendment right to counsel in two ways.</p>
<p id="b342-7">A</p>
<p id="b342-8">Petitioner’s first claim is that because his Sixth Amendment right to counsel arose with his indictment, the police were thereafter barred from initiating a meeting with him. See Brief for Petitioner 30-31; Tr. of Oral Arg. 2, 9, 11, 17. He equates himself with a preindictment suspect who, while being interrogated, asserts his Fifth Amendment right to counsel; under <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), such a suspect may not be questioned again unless he initiates the meeting.</p>
<p id="b342-9">Petitioner, however, at no time sought to exercise his right to have counsel present. The fact that petitioner’s Sixth <page-number citation-index="1" label="291">*291</page-number>Amendment right came into existence with his indictment, <em>i. e., </em>that he had such a right at the time of his questioning, does not distinguish him from the preindictment interrogatee whose right to counsel is in existence and available for his exercise while he is questioned. Had petitioner indicated he wanted the assistance of counsel, the authorities’ interview with him would have stopped, and further questioning would have been forbidden (unless petitioner called for such a meeting). This was our holding in <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson, supra,</a></span> </em>which applied <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>to the Sixth Amendment context. We observe that the analysis in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>is rendered wholly unnecessary if petitioner’s position is correct: under petitioner’s theory, the officers in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>would have been completely barred from approaching the accused in that case unless he called for them. Our decision in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span>, </em>however, turned on the fact that the accused “ha[d] asked for the help of a lawyer” in dealing with the police. <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#631" aria-description="Citation for case: Michigan v. Jackson"><em>Jackson, supra, </em>at 631, 633-635</a></span>.</p>
<p id="b343-5">At bottom, petitioner’s theory cannot be squared with our rationale in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>, </em>the case he relies on for support. <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rested on the view that once “an accused . . . ha[s] expressed his desire to deal with the police only through counsel” he should “not [be] subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication.” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Edwards, supra, </em>at 484-485</a></span>; cf. also <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#104" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 104, n. 10</a></span> (1975). Preserving the integrity of an accused’s choice to communicate with police only through counsel is the essence of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and its progeny— not barring an accused from making an <em>initial </em>election as to whether he will face the State’s officers during questioning with the aid of counsel, or go it alone. If an accused “knowingly and intelligently” pursues the latter course, we see no reason why the uncounseled statements he then makes must be excluded at his trial.</p>
<p id="b344-4"><page-number citation-index="1" label="292">*292</page-number>B</p>
<p id="b344-5">Petitioner’s principal and more substantial claim is that questioning him without counsel present violated the Sixth Amendment because he did not validly waive his right to have counsel present during the interviews. Since it is clear that after the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings were given to petitioner, he not only voluntarily answered questions without claiming his right to silence or his right to have a lawyer present to advise him but also executed a written waiver of his right to counsel during questioning, the specific issue posed here is whether this waiver was a “knowing and intelligent” waiver of his Sixth Amendment right.<footnotemark>4</footnotemark> See <em>Brewer </em>v. <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#401" aria-description="Citation for case: Brewer v. Williams"><em>Williams, supra, </em>at 401, 404</a></span>; <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464-465</a></span> (1938).</p>
<p id="b344-6">In the past, this Court has held that a waiver of the Sixth Amendment right to. counsel is valid only when it reflects “an intentional relinquishment or abandonment of a known right or privilege.” <em>Johnson </em>v. <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><em>Zerbst, supra, </em>at 464</a></span>. In other words, the accused must “kno[w] what he is doing” so that “his choice is made with eyes open.” <em>Adams </em>v. <em>United States ex rel. McCann, </em><span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#279" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 279</a></span> (1942). In a case arising under the Fifth Amendment, we described this requirement as “a full awareness of both the nature of the right being abandoned and the consequences of the decision to abandon it.” <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 421</a></span> (1986). Whichever of these formulations is used, the key inquiry in a case such as this one must be: Was the accused, who waived his Sixth Amendment rights during postindictment questioning, made sufficiently aware of his right to have counsel present during the questioning, and of the possible conse<page-number citation-index="1" label="293">*293</page-number>quences of a decision to forgo the aid of counsel? In this case, we are convinced that by admonishing petitioner with the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, respondent has met this burden and that petitioner’s waiver of his right to counsel at the questioning was valid.<footnotemark>5</footnotemark></p>
<p id="b345-5">First, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings given petitioner made him aware of his right to have counsel present during the questioning. By telling petitioner that he had a right to consult with an attorney, to have a lawyer present while he was questioned, and even to have a lawyer appointed for him if he could not afford to retain one on his own, Officer Gresham and ASA Smith conveyed to petitioner the sum and substance of the rights that the Sixth Amendment provided him. “Indeed, it seems self-evident that one who is told he” has such rights to counsel “is in a curious posture to later complain” that his waiver of these rights was unknowing. Cf. <em>United States </em>v. <em>Washington, </em><span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#188" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 188</a></span> (1977). There is little more petitioner could have possibly been told in an effort to satisfy this portion of the waiver inquiry.</p>
<p id="b345-6">Second, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings also served to make petitioner aware of the consequences of a decision by him to waive his Sixth Amendment rights during postindictment questioning. Petitioner knew that any statement that he made could be used against him in subsequent criminal proceedings. This is the ultimate adverse consequence petitioner could have suffered by virtue of his choice to make <page-number citation-index="1" label="294">*294</page-number>uncounseled admissions to the authorities. This warning also sufficed — contrary to petitioner’s claim here, see Tr. of Oral Arg. 7-8 — to let petitioner know what a lawyer could “do for him” during the postindictment questioning: namely, advise petitioner to refrain from making any such statements.<footnotemark>6</footnotemark> By knowing what could be done with any statements he might make, and therefore, what benefit could be obtained by having the aid of counsel while making such statements, petitioner was essentially informed of the possible consequences of going without counsel during questioning. If petitioner nonetheless lacked “a full and complete appreciation of all of the consequences flowing” from his waiver, it does not defeat the State’s showing that the information it provided to him satisfied the constitutional minimum. Cf. <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#316" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 316-317</a></span> (1985).</p>
<p id="b346-5">Our conclusion is supported by petitioner’s inability, in the proceedings before this Court, to articulate with precision what additional information should have been provided to him before he would have been competent to waive his right to counsel. All that petitioner’s brief and reply brief suggest is petitioner-should have been made aware of his “right under the Sixth Amendment to the broad protection of counsel” — a rather nebulous suggestion — and the “gravity of [his] situation.” Reply Brief for Petitioner 13; see Brief for Petitioner 30-31. But surely this latter “requirement” (if it is one) was met when Officer Gresham informed petitioner that he had been formally charged with the murder of James Jackson. <page-number citation-index="1" label="295">*295</page-number>See n. 8, <em>infra. </em>Under close questioning on this same point at argument, petitioner likewise failed to suggest any meaningful additional information that he should have been, but was not, provided in advance of his decision to waive his right to counsel.<footnotemark>7</footnotemark> The discussions found in favorable court decisions, on which petitioner relies, are similarly lacking.<footnotemark>8</footnotemark></p>
<p id="b348-4"><page-number citation-index="1" label="296">*296</page-number>As a general matter, then, an accused who is admonished with the warnings prescribed by this Court in <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>, has been sufficiently apprised of the nature of his Sixth Amendment rights, and of the consequences of abandoning those rights, so that his waiver on this basis will be considered a knowing and intelligent one.<footnotemark>9</footnotemark> We feel that <page-number citation-index="1" label="297">*297</page-number>our conclusion in a recent Fifth Amendment case is equally apposite here: “Once it is determined that a suspect's decision not to rely on his rights was uncoerced, that he at all times knew he could stand mute and request a lawyer, and that he was aware of the State’s intention to use his statements to secure a conviction, the analysis is complete and the waiver is valid as a matter of law.” See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 422-423</a></span>.</p>
<p id="b349-5">C</p>
<p id="b349-6">We consequently reject petitioner’s argument, which has some acceptance from courts and commentators,<footnotemark>10</footnotemark> that since “the sixth amendment right [to counsel] is far superior to that of the fifth amendment right” and since “[t]he greater the right the greater the loss from a waiver of that right,” waiver of an accused’s Sixth Amendment right to counsel should be “more difficult” to effectuate than waiver of a suspect’s Fifth Amendment rights. Brief for Petitioner 23. While our cases have recognized a “difference” between the Fifth Amendment and Sixth Amendment rights to counsel, and the “policies” behind these constitutional guarantees,<footnotemark>11</footnotemark> we have never suggested that one right is “superior” or “greater” than the other, nor is there any support in our cases for the notion that be<page-number citation-index="1" label="298">*298</page-number>cause a Sixth Amendment right may be involved, it is more difficult to waive than the Fifth Amendment counterpart.</p>
<p id="b350-5">Instead, we have taken a more pragmatic approach to the waiver question — asking what purposes a lawyer can serve at the particular stage of the proceedings in question, and what assistance he could provide to an accused at that stage — to determine the scope of the Sixth Amendment right to counsel, and the type of warnings and procedures that should be required before a waiver of that right will be recognized.</p>
<p id="b350-6">At one end of the spectrum, we have concluded there is no Sixth Amendment right to counsel whatsoever at a postin-dictment photographic display identification, because this procedure is not one at which the accused “require[s] aid in coping with legal problems or assistance in meeting his adversary.” See <em>United States </em>v. <em>Ash, </em><span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#313" aria-description="Citation for case: United States v. Ash">413 U. S. 300, 313-320</a></span> (1973). At the other extreme, recognizing the enormous importance and role that an attorney plays at a criminal trial, we have imposed the most rigorous restrictions on the information that must be conveyed to a defendant, and the procedures that must be observed, before permitting him to waive his right to counsel at trial. See <em>Faretta </em>v. <em>California, </em><span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#835" aria-description="Citation for case: Faretta v. California">422 U. S. 806, 835-836</a></span> (1975); cf. <em>Von Moltke </em>v. <em>Gillies, </em><span class="citation" data-id="9420085"><a href="/opinion/104496/von-moltke-v-gillies/#723" aria-description="Citation for case: Von Moltke v. Gillies">332 U. S. 708, 723-724</a></span> (1948). In these extreme cases, and in others that fall between these two poles, we have defined the scope of the right to counsel by a pragmatic assessment of the usefulness of counsel to the accused at the particular proceeding, and the dangers to the accused of proceeding without counsel. An accused’s waiver of his right to counsel is “knowing” when he is made aware of these basic facts.</p>
<p id="b350-7">Applying this approach, it is our view that whatever warnings suffice for <em>Miranda’s </em>purposes will also be sufficient in the context of postindictment questioning. The State’s decision to take an additional step and commence formal adversarial proceedings against the accused does not substantially increase the value of counsel to the accused at questioning, or expand the limited purpose that an attorney serves when the <page-number citation-index="1" label="299">*299</page-number>accused is questioned by authorities. With respect to this inquiry, we do not discern a substantial difference between the usefulness of a lawyer to a suspect during custodial interrogation, and his value to an accused at postindictment questioning.<footnotemark>12</footnotemark></p>
<p id="b351-5">Thus, we require a more searching or formal inquiry before permitting an accused to waive his right to counsel at trial than we require for a Sixth Amendment waiver during post-indictment <em>questioning </em>— not because postindictment questioning is “less important” than a trial (the analysis that petitioner’s “hierarchical” approach would suggest) — but because the full “dangers and disadvantages of self-representation,” <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#835" aria-description="Citation for case: Faretta v. California"><em>Faretta, supra, </em>at 835</a></span>, during questioning are less substantial and more obvious to an accused than they are at trial.<footnotemark>13</footnotemark> Because the role of counsel at questioning is relatively simple and limited, we see no problem in having a waiver procedure at that stage which is likewise simple and limited. So long as the accused is made aware of the “dangers and disadvantages <page-number citation-index="1" label="300">*300</page-number>of self-representation” during postindictment questioning, by use of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, his waiver of his Sixth Amendment right to counsel at such questioning is “knowing and intelligent.”</p>
<p id="b352-5">Ill</p>
<p id="b352-6">Before confessing to the murder of James Jackson, petitioner was meticulously informed by authorities of his right to counsel, and of the consequences of any choice not to exercise that right. On two separate occasions, petitioner elected to forgo the assistance of counsel, and speak directly to officials concerning his role in the murder. Because we believe that petitioner’s waiver of his Sixth Amendment rights was “knowing and intelligent,” we find no error in the decision of the trial court to permit petitioner’s confessions to be used against him. Consequently, the judgment of the Illinois Supreme Court is</p>
<p id="b352-7">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b340-8"> Although the signed waiver form does not appear in the record or the appendix, petitioner concedes that he was informed of his right to counsel to the extent required by our decision in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Brief for Petitioner 3; Tr. of Oral Arg. 6-8.</p>
<p id="b340-9">This apparently included informing petitioner that he had a right to remain silent; that anything he might say could be used against him; that he had a right to consult with an attorney; that he had a right to have an attorney present during interrogation; and that, as an indigent, the State would provide him with a lawyer if he so desired.</p>
</footnote>
<footnote label="2">
<p id="b341-8">See, <em>e. g., Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#635" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625, 635-636, n. 10</a></span> (1986); <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#428" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 428, n. 2</a></span> (1986); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#405" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 405-406</a></span> (1977).</p>
</footnote>
<footnote label="3">
<p id="b342-10"> We note as a matter of some significance that petitioner had not retained, or accepted by appointment, a lawyer to represent him at the time he was questioned by authorities. Once an accused has a lawyer, a distinct set of constitutional safeguards aimed at preserving the sanctity of the attorney-client relationship takes effect. See <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 176</a></span> (1985). The State conceded as much at argument. See Tr. of Oral Arg. 28.</p>
<p id="b342-11">Indeed, the analysis changes markedly once an accused even <em>requests </em>the assistance of counsel. See <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson, supra;</a></span> </em>Part II-A, <em>infra.</em></p>
</footnote>
<footnote label="4">
<p id="b344-7"> Of course, we also require that any such waiver must be voluntary. Petitioner contested, the voluntariness of his confession in the trial court and in the intermediate appellate courts, which rejected petitioner’s claim that his confessions were coerced. See <span class="citation" data-id="2037100"><a href="/opinion/2037100/people-v-patterson/#425" aria-description="Citation for case: People v. Patterson">140 Ill. App. 3d 421, 425-426</a></span>, <span class="citation" data-id="2037100"><a href="/opinion/2037100/people-v-patterson/#1287" aria-description="Citation for case: People v. Patterson">488 N. E. 2d 1283, 1287</a></span> (1986).</p>
<p id="b344-8">Petitioner does not appear to have maintained this contention before the Illinois Supreme Court, and in any event, he does not press this argument here. Thus, the “yoluntariness” of petitioner’s confessions is not before us.</p>
</footnote>
<footnote label="5">
<p id="b345-7"> We emphasize the significance of the fact that petitioner’s waiver of counsel was only for this limited aspect of the criminal proceedings against him — only for postindictment questioning. Our decision on the validity of petitioner’s waiver extends only so far.</p>
<p id="b345-8">Moreover, even within this limited context, we note that petitioner’s waiver was binding on him <em>only </em>so long as he wished it to be. Under this Court’s precedents, at any time during the questioning petitioner could have changed his mind, elected to have the assistance of counsel, and immediately dissolve the effectiveness of his waiver with respect to any subsequent statements. See, <em>e. g., Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#631" aria-description="Citation for case: Michigan v. Jackson">475 U. S., at 631-635</a></span>; Part II-A, <em>supra. </em>Our decision today does nothing to change this rule.</p>
</footnote>
<footnote label="6">
<p id="b346-6"> An important basis for our analysis is our understanding that an attorney’s role at postindictment questioning is rather limited, and substantially different from the attorney’s role in later phases of criminal proceedings. At trial, an accused needs an attorney to perform several varied functions —some of which are entirely beyond even the most intelligent layman. Yet during postindictment questioning, a lawyer’s role is rather unidimen-sional: largely limited to advising his client as to what questions to answer and which ones to decline to answer.</p>
<p id="b346-7">We discuss this point in greater detail below. See Part II-C, <em>infra.</em></p>
</footnote>
<footnote label="7">
<p id="b347-5"> Representative excerpts from the relevant portions of argument include the following:</p>
<p id="b347-6">“QUESTION: [Petitioner] . . . was told that he had a right to counsel.</p>
<p id="b347-7">“MR. HONCHELL [petitioner’s counsel]: He was told — the word ‘counsel’ was used. He was told he had a right to counsel. But not through information by which it would become meaningful to him, because the method that was used was not designed to alert the accused to the Sixth Amendment rights to counsel. . . .</p>
<p id="b347-8">“QUESTION: . . . You mean they should have said you have a Sixth Amendment right to counsel instead of just, you have a right to counsel?</p>
<p id="b347-9">“He knew he had a right to have counsel present before [he] made the confession. Now, what in addition did he have to know to make the waiver an intelligent one?</p>
<p id="b347-10">“MR. HONCHELL: He had to meaningfully know he had a Sixth Amendment right to counsel present because—</p>
<p id="b347-11">“QUESTION: What is the difference between meaningfully knowing and knowing?</p>
<p id="b347-12">“MR. HONCHELL: Because the warning here used did not convey or express what counsel was intended to do for him after indictment.</p>
<p id="b347-13">“QUESTION: So then you say . . . [that] he would have had to be told more about what counsel would do for him after indictment before he could intelligently waive?</p>
<p id="b347-14">“MR. HONCHELL: That there is a right to counsel who would act on his behalf and represent him. '</p>
<p id="b347-15">“QUESTION: Well, okay. So it should have said, in addition to saying counsel, counsel who would act on your behalf and represent you? That would have been the magic solution?</p>
<p id="b347-16">“MR. HONCHELL: That is a possible method, yes.” Tr. of Oral Arg. 7-8.</p>
<p id="b347-17">We do not believe that adding the words “who would act on your behalf and represent you” in Sixth Amendment cases would provide any meaningful improvement in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. Cf. <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#435" aria-description="Citation for case: Brewer v. Williams">430 U. S., at 435-436, n. 5</a></span> (White, J., dissenting).</p>
</footnote>
<footnote label="8">
<p id="b347-18"> Even those lower court cases which have suggested that something beyond <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings is —or may be — required before a Sixth Amend<page-number citation-index="1" label="296">*296</page-number>ment waiver can be considered “knowing and intelligent” have failed to suggest just what this “something more” should be. See, e. <em>g., Felder </em>v. <em>McCotter, </em><span class="citation" data-id="454503"><a href="/opinion/454503/sammie-felder-jr-v-ol-mccotter-director-texas-department-of/#1250" aria-description="Citation for case: Sammie Felder, Jr. v. O.L. McCotter Director, Texas...">765 F. 2d 1245, 1250</a></span> (CA5 1985); <em>Robinson </em>v. <em>Percy, </em><span class="citation" data-id="437719"><a href="/opinion/437719/eric-robinson-v-donald-e-percy-secretary-department-of-health-and/#222" aria-description="Citation for case: Eric Robinson v. Donald E. Percy, Secretary, Department...">738 F. 2d 214, 222</a></span> (CA7 1984); <em>Fields </em>v. <em>Wyrick, </em><span class="citation" data-id="418052"><a href="/opinion/418052/edward-fields-v-donald-wyrick/#880" aria-description="Citation for case: Edward Fields v. Donald Wyrick">706 F. 2d 879, 880-881</a></span> (CA8 1983).</p>
<p id="b348-9">An exception to this is the occasional suggestion that, in addition to the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, an accused should be informed that he has been indicted before a postindictment waiver is sought. See, <em>e. g., United States </em>v. <em>Mohabir, </em><span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/#1150" aria-description="Citation for case: United States v. Lionel Mohabir">624 F. 2d 1140, 1150</a></span> (CA2 1980); <em>United States </em>v. <em>Payton, </em><span class="citation" data-id="374894"><a href="/opinion/374894/united-states-v-william-charles-payton/#924" aria-description="Citation for case: United States v. William Charles Payton">615 F. 2d 922, 924-925</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./446/969/">446 U. S. 969</a></span> (1980). Because, in this case, petitioner concedes that he was so informed, see Brief for Petitioner 3, we do not address the question whether or not an accused must be told that he has been indicted before a postindictment Sixth Amendment waiver will be valid. Nor do we even pass on the desirability of so informing the accused — a matter that can be reasonably debated. See, <em>e. g., </em>Tr. of Oral Arg. 24.</p>
<p id="b348-12">Beyond this, only one Court of Appeals —the Second Circuit —has adopted substantive or procedural requirements (in addition to <em>Miranda) </em>that must be completed before a Sixth Amendment waiver can be effectuated for postindictment questioning. See <em>United States </em>v. <em>Mohabir, </em><span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/#1150" aria-description="Citation for case: United States v. Lionel Mohabir">624 F. 2d, at 1150-1153</a></span>. As have a majority of the Courts of Appeals, we reject <em>Moha-</em>bifs holding that some “additional” warnings or discussions with an accused are required in this situation, or that any waiver in this context can only properly be made before a “neutral . . . judicial officer.” <em><span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/" aria-description="Citation for case: United States v. Lionel Mohabir">Ibid.</a></span></em></p>
</footnote>
<footnote label="9">
<p id="b348-13"> This does not mean, of course, that all Sixth Amendment challenges to the conduct of postindictment questioning will fail whenever the challenged practice would pass constitutional muster under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>For example, we have permitted a <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waiver to stand where a suspect was not told that his lawyer was trying to reach him during questioning; in the Sixth Amendment context, this waiver would not be valid. See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#424" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 424, 428</a></span>. Likewise a surreptitious conversation between an undercover police officer and an unindieted suspect would not give rise to any <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>violation as long as the “interrogation” was not in a custodial setting, see <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>; however, once the <page-number citation-index="1" label="297">*297</page-number>accused is indicted, such questioning would be prohibited. See <em>United States </em>v. <em>Henry, </em><span class="citation" data-id="9427972"><a href="/opinion/110300/united-states-v-henry/#273" aria-description="Citation for case: United States v. Henry">447 U. S. 264, 273, 274-275</a></span> (1980).</p>
<p id="b349-8">Thus, because the Sixth Amendment’s protection of the attorney-client relationship — “the right to rely on counsel as a ‘medium’ between [the accused] and the State” — extends beyond <em>Miranda's </em>protection of the Fifth Amendment right to counsel, see <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#176" aria-description="Citation for case: Maine v. Moulton">474 U. S., at 176</a></span>, there will be cases where a waiver which would be valid under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>will not suffice for-Sixth Amendment purposes. See also <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#632" aria-description="Citation for case: Michigan v. Jackson">475 U. S., at 632</a></span>.</p>
</footnote>
<footnote label="10">
<p id="b349-9">See, <em>e. g., United States </em>v. <span class="citation" data-id="379999"><a href="/opinion/379999/united-states-v-lionel-mohabir/#1149" aria-description="Citation for case: United States v. Lionel Mohabir"><em>Mohabir, supra, </em>at 1149-1152</a></span>; Note, Proposed Requirements for Waiver of the Sixth Amendment Right to Counsel, 82 Colum. L.- Rev. 363, 372 (1982).</p>
</footnote>
<footnote label="11">
<p id="b349-10">See, e. <em>g., Michigan </em>v. <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson"><em>Jackson, supra, </em>at 633, n. 7</a></span>; <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300, n. 4</a></span> (1980).</p>
</footnote>
<footnote label="12">
<p id="b351-6"> We note, incidentally, that in the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>decision itself, the analysis and disposition of the waiver question relied on this Court's decision in <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938) — a <em>Sixth </em>Amendment waiver case. See <em>Miranda, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 475</a></span>.</p>
<p id="b351-7">From the outset, then, this Court has recognized that the waiver inquiry focuses more on the lawyer’s role during such questioning, rather than the particular constitutional guarantee that gives rise to the right to counsel at that proceeding. See <em>ibid.; </em>see also <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#421" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 421</a></span>. Thus, it should be no surprise that we now find a strong similarity between the level of knowledge a defendant must have to waive his Fifth Amendment right to counsel, and the protection accorded to Sixth Amendment rights. See Comment, Constitutional Law — Right to Counsel, <span class="citation no-link">49 Geo. Wash. L. Rev. 399</span>, 409 (1981).</p>
</footnote>
<footnote label="13">
<p id="b351-8"> As discussed above, see n. 6, <em>supra, </em>an attorney’s role at questioning is relatively limited. But at trial, counsel is required to help even the most gifted layman adhere to the rules of procedure and evidence, comprehend the subtleties of <em>voir dire, </em>examine and cross-examine witnesses effectively (including the accused), object to improper prosecution questions, and much more. Cf., <em>e. g., </em>1 Bench Book for United States District Court Judges 1.02-2 — 1.02-5 (3d ed. 1986); <em>McDowell </em>v. <em>United States, </em><span class="citation" data-id="9431199"><a href="/opinion/112002/mcdowell-v-united-states/" aria-description="Citation for case: McDowell v. United States">484 U. S. 980</a></span> (1987) (White, J., dissenting from denial of certiorari).</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Payton v. New York.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Payton v. New York"
type: case
citation: "445 U.S. 573 (1980)"
parallel_cite: "100 S. Ct. 1371; 63 L. Ed. 2d 639"
neutral_cite: 1980 U.S. LEXIS 13
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1980
date_decided: 1980-04-15
docket: 78-5420
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1980-04-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Payton v. New York
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110235/payton-v-new-york/"
  cluster_id: 110235
  opinion_id: 110235
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Key — Anchor"
  - page: "[[Entry to Arrest]]"
    role: "Key — Anchor"
  - page: "[[Securing the Scene]]"
    role: "Related (cross-doctrine)"
related: ["[[United States v. Watson]]", "[[Steagald v. United States]]", "[[Maryland v. Buie]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest-in-the-home", "arrest-warrant", "warrant-requirement", "threshold"]
holding: "Warrantless, nonconsensual entry into a SUSPECT'S OWN home to make a routine felony arrest is presumptively unreasonable; an arrest…"
lake:
  record_id: Payton v. New York
  status: verified
  projected_at: 2026-07-09
---

# Payton v. New York

*445 U.S. 573 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New York statutes authorized police to enter a private residence without a warrant, by force if necessary, to make a routine felony arrest. In Payton's case, detectives had probable cause that Theodore Payton murdered a gas-station manager; at 7:30 a.m. six officers went to his Bronx apartment without a warrant, got no answer, broke open the door, and seized a shell casing in plain view. (The consolidated *Riddick* case involved a similar warrantless home arrest.)

## Issue
Whether the Fourth Amendment permits police to make a warrantless and nonconsensual entry into a suspect's own home in order to make a routine felony arrest.

## Rule
No. The Fourth Amendment "prohibits the police from making a warrantless and nonconsensual entry into a suspect's home in order to make a routine felony arrest." — 445 U.S. at 576. ^pin-576

"In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant." — [445 U.S. at 590](https://www.courtlistener.com/opinion/110235/payton-v-new-york/#:~:text=In%20terms%20that%20apply%20equally). ^pin-590

## Application
The detectives had probable cause to arrest Payton but no warrant and no [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] when they forced entry into his apartment; the same was true of the warrantless entry to arrest Riddick in his home. Because the Fourth Amendment draws a firm line at the entrance to the house, those warrantless, nonconsensual entries to make routine felony arrests were unconstitutional, and the evidence obtained (including the shell casing seized in Payton's apartment) could not stand on that basis.

## Conclusion
Warrantless, nonconsensual home entry to make a routine felony arrest is presumptively unreasonable absent [[Exigent Circumstances and Hot Pursuit|exigent circumstances]]; the New York statutes were unconstitutional and the judgments were reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. An arrest warrant founded on probable cause implicitly carries the limited authority to enter a suspect's *own* dwelling to arrest when there is reason to believe he is within; entry to arrest in a *third party's* home additionally requires a search warrant ([[Steagald v. United States]]).

## Appears on
- [[Arrest in the Home]] — *Key — Anchor*
- [[Entry to Arrest]] — *Key — Anchor*
- [[Securing the Scene]] — *Related (cross-doctrine)*

## Sources
- *Payton v. New York*, 445 U.S. 573 (1980) — https://www.courtlistener.com/opinion/110235/payton-v-new-york/ — pinpoints: 576, 590.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6f84668d8234047c", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Payton v. New York"}, "payload": {"all": [{"cite": "445 U.S. 573", "page": "573", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "445"}, {"cite": "100 S. Ct. 1371", "page": "1371", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "100"}, {"cite": "63 L. Ed. 2d 639", "page": "639", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "63"}, {"cite": "1980 U.S. LEXIS 13", "page": "13", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1980"}], "display": "445 U.S. 573", "official": {"cite": "445 U.S. 573", "page": "573", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "445"}, "official_selection_present": true, "record_id": "Payton v. New York"}}
{"assertion_id": "3fc6f1a4c9d2c7e0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-590", "record_id": "Payton v. New York"}, "payload": {"fragment": "#:~:text=In%20terms%20that%20apply%20equally", "page": null, "pin_id": "pin-590", "pinpoint_status": "star-verified", "quote": "In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.", "quote_fidelity": "matched", "record_id": "Payton v. New York", "star_marker": "590"}}
{"assertion_id": "48284b734569de8e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-576", "record_id": "Payton v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-576", "pinpoint_status": "slip-only", "quote": "--- # Payton v. New York *445 U.S. 573 (1980)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New York statutes authorized police to enter a private residence without a warrant, by force if necessary, to make a routine felony arrest. In Payton's case, detectives had probable cause that Theodore Payton murdered a gas-station manager; at 7:30 a.m. six officers went to his Bronx apartment without a warrant, got no answer, broke open the door, and seized a shell casing in plain view. (The consolidated *Riddick* case involved a similar warrantless home arrest.) ## Issue Whether the Fourth Amendment permits police to make a warrantless and nonconsensual entry into a suspect's own home in order to make a routine felony arrest. ## Rule No. The Fourth Amendment", "quote_fidelity": "mismatch", "record_id": "Payton v. New York", "star_marker": null}}
{"assertion_id": "70d0910963298015", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Payton v. New York"}, "payload": {"as_of_content": "1980-04-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Payton v. New York", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Payton v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Payton v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Payton v. New York",
    "case_name_short": "Payton",
    "case_name_full": "Payton v. New York",
    "input_case_name": "Payton v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1980-04-15",
    "year": 1980,
    "docket": "78-5420",
    "cluster_id": 110235,
    "lead_opinion_id": 110235,
    "sibling_ids": [
      110235,
      9427853,
      9427854,
      9427855,
      9427856,
      9427857
    ],
    "absolute_url": "/opinion/110235/payton-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "445 U.S. 573",
      "volume": "445",
      "reporter": "U.S.",
      "page": "573",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "100 S. Ct. 1371",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1371",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 639",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1980 U.S. LEXIS 13",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "445 U.S. 573",
        "volume": "445",
        "reporter": "U.S.",
        "page": "573",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 S. Ct. 1371",
        "volume": "100",
        "reporter": "S. Ct.",
        "page": "1371",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "63 L. Ed. 2d 639",
        "volume": "63",
        "reporter": "L. Ed. 2d",
        "page": "639",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1980 U.S. LEXIS 13",
        "volume": "1980",
        "reporter": "U.S. LEXIS",
        "page": "13",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "445 U.S. 573",
    "official_selection": {
      "court_class": "scotus",
      "selected": "445 U.S. 573",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-576",
      "page": null,
      "quote": "--- # Payton v. New York *445 U.S. 573 (1980)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New York statutes authorized police to enter a private residence without a warrant, by force if necessary, to make a routine felony arrest. In Payton's case, detectives had probable cause that Theodore Payton murdered a gas-station manager; at 7:30 a.m. six officers went to his Bronx apartment without a warrant, got no answer, broke open the door, and seized a shell casing in plain view. (The consolidated *Riddick* case involved a similar warrantless home arrest.) ## Issue Whether the Fourth Amendment permits police to make a warrantless and nonconsensual entry into a suspect's own home in order to make a routine felony arrest. ## Rule No. The Fourth Amendment",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-590",
      "page": null,
      "quote": "In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.",
      "star_marker": "590",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 22362,
      "fragment": "#:~:text=In%20terms%20that%20apply%20equally",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1980-04-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Payton v. New York",
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
        "journal_ref": "Payton v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jamin Kidron Stocker v. the State of Texas",
          "cluster_id": 9329108,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane1_negative"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pembaur v. City of Cincinnati",
          "cluster_id": 111615,
          "cite": [
            "89 L. Ed. 2d 452",
            "106 S. Ct. 1292",
            "475 U.S. 469",
            "1986 U.S. LEXIS 33",
            "54 U.S.L.W. 4289"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffith v. Kentucky",
          "cluster_id": 111785,
          "cite": [
            "93 L. Ed. 2d 649",
            "107 S. Ct. 708",
            "479 U.S. 314",
            "1987 U.S. LEXIS 283",
            "55 U.S.L.W. 4089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilson v. Layne",
          "cluster_id": 118289,
          "cite": [
            "143 L. Ed. 2d 818",
            "119 S. Ct. 1692",
            "526 U.S. 603",
            "1999 U.S. LEXIS 3633"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. Buie",
          "cluster_id": 112384,
          "cite": [
            "108 L. Ed. 2d 276",
            "110 S. Ct. 1093",
            "494 U.S. 325",
            "1990 U.S. LEXIS 1176"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
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
        "journal_ref": "Payton v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk5Njk2MDAwMDAwJnM9NDc4NDA1OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110235+OR+9427853+OR+9427854+OR+9427855+OR+9427856+OR+9427857%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 2,
        "triage_snippet_classified": 198
      },
      "lane2_top_cited": {
        "query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTU4JnM9MTEyNzk1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110235+OR+9427853+OR+9427854+OR+9427855+OR+9427856+OR+9427857%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857)",
        "reviewed": 117,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 117,
        "triage_read": 1,
        "triage_snippet_classified": 116
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110235 OR 9427853 OR 9427854 OR 9427855 OR 9427856 OR 9427857)",
    "indexed_citing_opinions": 4710,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110235,
        "count": 4214,
        "count_source": "search"
      },
      {
        "opinion_id": 9427853,
        "count": 568,
        "count_source": "search"
      },
      {
        "opinion_id": 9427854,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427855,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427856,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427857,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 7628,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/payton-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1NDM0OTUmcz0xMDY3MzE4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110235+OR+9427853+OR+9427854+OR+9427855+OR+9427856+OR+9427857%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110235,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 93880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 95265,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 101905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 105925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106187,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107718,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109352,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 224194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 292572,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 292629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 301708,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 303979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 317251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 348416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 354014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 354259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 358848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 369038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1185860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1218237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1369726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1396585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1435637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1442643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1527202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1723936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1775149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1806892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1836490,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1860990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1927633,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 1948493,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2017555,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2064787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2106646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2226234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2233048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2295125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2583592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 2616403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110235,
        "cited_id": 3953469,
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
    "date_created": "2026-07-05T16:36:39Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T16:36:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T16:36:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T16:40:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T16:36:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Payton v. New York (truncated)

```
<div>
<center><b><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U.S. 573</a></span> (1980)</b></center>
<center><h1>PAYTON<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 78-5420.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 26, 1979.</center>
<center>Reargued October 9, 1979.</center>
<center>Decided April 15, 1980.<sup>[*]</sup></center>
APPEAL FROM THE COURT OF APPEALS OF NEW YORK.
<p><span class="star-pagination">*574</span> <i>William E. Hellerstein</i> reargued the cause for appellants in both cases. With him on the briefs was <i>David A. Lewis.</i></p>
<p><i>Peter L. Zimroth</i> reargued the cause for appellee in both cases. With him on the briefs were <i>John J. Santucci, Henry J. Steinglass, Brian Rosner,</i> and <i>Vivian Berger.</i></p>
<p>MR. JUSTICE STEVENS delivered the opinion of the Court.</p>
<p>These appeals challenge the constitutionality of New York statutes that authorize police officers to enter a private residence without a warrant and with force, if necessary, to make a routine felony arrest.</p>
<p>The important constitutional question presented by this challenge has been expressly left open in a number of our prior opinions. In <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span>, we upheld a warrantless "midday public arrest," expressly noting that the case did not pose "the still unsettled question <span class="star-pagination">*575</span>. . . `whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest.'" <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 418, n. 6</a></span>.<sup>[1]</sup> The question has been answered in different ways by other appellate courts. The Supreme Court of Florida rejected the constitutional attack,<sup>[2]</sup> as did the New York Court of Appeals in this case. The courts of last resort in 10 other States, however, have held that unless special circumstances are present, warrantless arrests in the home are unconstitutional.<sup>[3]</sup> Of the seven United States Courts of Appeals that have considered the question, five have expressed the opinion that such arrests are unconstitutional.<sup>[4]</sup></p>
<p><span class="star-pagination">*576</span> Last Term we noted probable jurisdiction of these appeals in order to address that question. <span class="citation multiple-matches"><a href="/c/U.%20S./439/1044/">439 U. S. 1044</a></span>. After hearing oral argument, we set the case for reargument this Term. <span class="citation multiple-matches"><a href="/c/U.%20S./441/930/">441 U. S. 930</a></span>. We now reverse the New York Court of Appeals and hold that the Fourth Amendment to the United States Constitution, made applicable to the States by the Fourteenth Amendment, <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>; <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, prohibits the police from making a warrantless and nonconsensual entry into a suspect's home in order to make a routine felony arrest.</p>
<p>We first state the facts of both cases in some detail and put to one side certain related questions that are not presented by these records. We then explain why the New York statutes are not consistent with the Fourth Amendment and why the reasons for upholding warrantless arrests in a public place do not apply to warrantless invasions of the privacy of the home.</p>
<p></p>
<h2>I</h2>
<p>On January 14, 1970, after two days of intensive investigation, New York detectives had assembled evidence sufficient to establish probable cause to believe that Theodore Payton had murdered the manager of a gas station two days earlier. At about 7:30 a. m. on January 15, six officers went to Payton's apartment in the Bronx, intending to arrest him. They had not obtained a warrant. Although light and music emanated from the apartment, there was no response to their knock on the metal door. They summoned emergency assistance and, about 30 minutes later, used crowbars to break open the door and enter the apartment. No one was there. In plain view, however, was a .30-caliber shell casing that was <span class="star-pagination">*577</span> seized and later admitted into evidence at Payton's murder trial.<sup>[5]</sup></p>
<p>In due course Payton surrendered to the police, was indicted for murder, and moved to suppress the evidence taken from his apartment. The trial judge held that the warrantless and forcible entry was authorized by the New York Code of Criminal Procedure,<sup>[6]</sup> and that the evidence in plain view was properly seized. He found that exigent circumstances justified the officers' failure to announce their purpose before entering the apartment as required by the statute.<sup>[7]</sup> He had no <span class="star-pagination">*578</span> occasion, however, to decide whether those circumstances also would have justified the failure to obtain a warrant, because he concluded that the warrantless entry was adequately supported by the statute without regard to the circumstances. The Appellate Division, First Department, summarily affirmed.<sup>[8]</sup></p>
<p>On March 14, 1974, Obie Riddick was arrested for the commission of two armed robberies that had occurred in 1971. He had been identified by the victims in June 1973, and in January 1974 the police had learned his address. They did not obtain a warrant for his arrest. At about noon on March 14, a detective, accompanied by three other officers, knocked on the door of the Queens house where Riddick was living. When his young son opened the door, they could see Riddick sitting in bed covered by a sheet. They entered the house and placed him under arrest. Before permitting him to dress, they opened a chest of drawers two feet from the bed in search of weapons and found narcotics and related paraphernalia. Riddick was subsequently indicted on narcotics charges. At a suppression hearing, the trial judge held that the warrantless entry into his home was authorized by the revised New York statute,<sup>[9]</sup> and that the search of the immediate <span class="star-pagination">*579</span> area was reasonable under <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>.<sup>[10]</sup> The Appellate Division, Second Department, affirmed the denial of the suppression motion.<sup>[11]</sup></p>
<p>The New York Court of Appeals, in a single opinion, affirmed the convictions of both Payton and Riddick. 45 N. Y. 2d 300, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/" aria-description="Citation for case: People v. Payton">380 N. E. 2d 224</a></span> (1978). The court recognized that the question whether and under what circumstances an officer may enter a suspect's home to make a warrantless arrest had not been settled either by that court or by this Court.<sup>[12]</sup> In answering that question, the majority of four judges relied primarily on its perception that there is a</p>
<blockquote>". . . substantial difference between the intrusion which attends an entry for the purpose of searching the premises and that which results from an entry for the purpose of <span class="star-pagination">*580</span> making an arrest, and [a] significant difference in the governmental interest in achieving the objective of the intrusion in the two instances." <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#310" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 310</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#228" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 228-229</a></span>.<sup>[13]</sup></blockquote>
<p><span class="star-pagination">*581</span> The majority supported its holding by noting the "apparent historical acceptance" of warrantless entries to make felony arrests, both in the English common law and in the practice of many American States.<sup>[14]</sup></p>
<p>Three members of the New York Court of Appeals dissented on this issue because they believed that the Constitution requires the police to obtain a "warrant to enter a home in order to arrest or seize a person, unless there are exigent circumstances."<sup>[15]</sup> Starting from the premise that, except in carefully circumscribed instances, "the Fourth Amendment forbids police entry into a private home to search for and seize an object without a warrant,"<sup>[16]</sup> the dissenters reasoned that an arrest of the person involves an even greater invasion of privacy and should therefore be attended with at least as <span class="star-pagination">*582</span> great a measure of constitutional protection.<sup>[17]</sup> The dissenters noted "the existence of statutes and the American Law Institute imprimatur codifying the common-law rule authorizing warrantless arrests in private homes" and acknowledged that "the statutory authority of a police officer to make a warrantless arrest in this State has been in effect for almost 100 years," but concluded that "neither antiquity nor legislative unanimity can be determinative of the grave constitutional question presented" and "can never be a substitute for reasoned analysis."<sup>[18]</sup></p>
<p>Before addressing the narrow question presented by these appeals,<sup>[19]</sup> we put to one side other related problems that are <span class="star-pagination">*583</span> <i>not</i> presented today. Although it is arguable that the warrantless entry to effect Payton's arrest might have been justified by exigent circumstances, none of the New York courts relied on any such justification. The Court of Appeals majority treated both Payton's and Riddick's cases as involving routine arrests in which there was ample time to obtain a warrant,<sup>[20]</sup> and we will do the same. Accordingly, we have no occasion to consider the sort of emergency or dangerous situation, described in our cases as "exigent circumstances," that would justify a warrantless entry into a home for the purpose of either arrest or search.</p>
<p>Nor do these cases raise any question concerning the authority of the police, without either a search or arrest warrant, to enter a third party's home to arrest a suspect. The police broke into Payton's apartment intending to arrest Payton, and they arrested Riddick in his own dwelling. We also note that in neither case is it argued that the police lacked probable cause to believe that the suspect was at home when they entered. Finally, in both cases we are dealing with entries into homes made without the consent of any occupant. In <i>Payton,</i> the police used crowbars to break down the door and in <i>Riddick,</i> although his 3-year-old son answered the door; the police entered before Riddick had an opportunity either to object or to consent.</p>
<p></p>
<h2>II</h2>
<p>It is familiar history that indiscriminate searches and seizures conducted under the authority of "general warrants" were the immediate evils that motivated the framing and adoption of the Fourth Amendment.<sup>[21]</sup> Indeed, as originally <span class="star-pagination">*584</span> proposed in the House of Representatives, the draft contained only one clause, which directly imposed limitations on the issuance of warrants, but imposed no express restrictions on warrantless searches or seizures.<sup>[22]</sup> As it was ultimately adopted, however, the Amendment contained two separate clauses, the first protecting the basic right to be free from unreasonable searches and seizures and the second requiring that warrants be particular and supported by probable cause.<sup>[23]</sup> The Amendment provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches <span class="star-pagination">*585</span> and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</blockquote>
<p>It is thus perfectly clear that the evil the Amendment was designed to prevent was broader than the abuse of a general warrant. Unreasonable searches or seizures conducted without any warrant at all are condemned by the plain language of the first clause of the Amendment. Almost a century ago the Court stated in resounding terms that the principles reflected in the Amendment "reached farther than the concrete form" of the specific cases that gave it birth, and "apply to all invasions on the part of the government and its employees of the sanctity of a man's home and the privacies of life." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span>. Without pausing to consider whether that broad language may require some qualification, it is sufficient to note that the warrantless arrest of a person is a species of seizure required by the Amendment to be reasonable. <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>. Cf. <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span>. Indeed, as MR. JUSTICE POWELL noted in his concurrence in <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i><i>,</i> the arrest of a person is "quintessentially a seizure." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#428" aria-description="Citation for case: United States v. Watson">423 U. S., at 428</a></span>.</p>
<p>The simple language of the Amendment applies equally to seizures of persons and to seizures of property. Our analysis in this case may therefore properly commence with rules that have been well established in Fourth Amendment litigation involving tangible items. As the Court reiterated just a few years ago, the "physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed." <i>United States</i> v. <i>United States District Court,</i> <span class="star-pagination">*586</span> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span>. And we have long adhered to the view that the warrant procedure minimizes the danger of needless intrusions of that sort.<sup>[24]</sup></p>
<p>It is a "basic principle of Fourth Amendment law" that searches and seizures inside a home without a warrant are presumptively unreasonable.<sup>[25]</sup> Yet it is also well settled that <span class="star-pagination">*587</span> objects such as weapons or contraband found in a public place may be seized by the police without a warrant. The seizure of property in plain view involves no invasion of privacy and is presumptively reasonable, assuming that there is probable cause to associate the property with criminal activity. The distinction between a warrantless seizure in an open area and such a seizure on private premises was plainly stated in <i>G. M. Leasing Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9426638"><a href="/opinion/109579/g-m-leasing-corp-v-united-states/" aria-description="Citation for case: G. M. Leasing Corp. v. United States">429 U. S. 338</a></span>, 354:</p>
<blockquote>"It is one thing to seize without a warrant property resting in an open area or seizable by levy without an intrusion into privacy, and it is quite another thing to effect a warrantless seizure of property, even that owned by a corporation, situated on private premises to which access is not otherwise available for the seizing officer."</blockquote>
<p>As the late Judge Leventhal recognized, this distinction has equal force when the seizure of a person is involved. Writing on the constitutional issue now before us for the United States Court of Appeals for the District of Columbia Circuit sitting en banc, <i>Dorman</i> v. <i>United States,</i> 140 U. S. App. D. C. 313, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385</a></span> (1970), Judge Leventhal first noted the settled rule that warrantless arrests in public places are valid. He immediately recognized, however, that</p>
<blockquote>"[a] greater burden is placed . . . on officials who enter a home or dwelling without consent. Freedom from intrusion into the home or dwelling is the archetype of the privacy protection secured by the Fourth Amendment." <i>Id.,</i> at 317, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/#389" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d, at 389</a></span>. (Footnote omitted.)</blockquote>
<p>His analysis of this question then focused on the long-settled premise that, absent exigent circumstances, a warrantless <span class="star-pagination">*588</span> entry to search for weapons or contraband is unconstitutional even when a felony has been committed and there is probable cause to believe that incriminating evidence will be found within.<sup>[26]</sup> He reasoned that the constitutional protection afforded to the individual's interest in the privacy of his own home is equally applicable to a warrantless entry for the purpose of arresting a resident of the house; for it is inherent in such an entry that a search for the suspect may be required before he can be apprehended.<sup>[27]</sup> Judge Leventhal concluded that an entry to arrest and an entry to search for and to seize property implicate the same interest in preserving the privacy and the sanctity of the home, and justify the same level of constitutional protection.</p>
<p>This reasoning has been followed in other Circuits.<sup>[28]</sup> Thus, the Second Circuit recently summarized its position:</p>
<blockquote>"To be arrested in the home involves not only the invasion <span class="star-pagination">*589</span> attendant to all arrests but also an invasion of the sanctity of the home. This is simply too substantial an invasion to allow without a warrant, at least in the absence of exigent circumstances, even when it is accomplished under statutory authority and when probable cause is clearly present." <i>United States</i> v. <i>Reed,</i> <span class="citation" data-id="354014"><a href="/opinion/354014/united-states-v-nancy-reed-and-morris-goldsmith-aka-marlowe/#423" aria-description="Citation for case: United States v. Nancy Reed and Morris Goldsmith, A/K/A...">572 F. 2d 412, 423</a></span> (1978), cert. denied <i>sub nom. </i><i>Goldsmith</i> v. <i>United States,</i> <span class="citation" data-id="9013020"><a href="/opinion/9019821/goldsmith-v-united-states/" aria-description="Citation for case: Goldsmith v. United States">439 U. S. 913</a></span>.</blockquote>
<p>We find this reasoning to be persuasive and in accord with this Court's Fourth Amendment decisions.</p>
<p>The majority of the New York Court of Appeals, however, suggested that there is a substantial difference in the relative intrusiveness of an entry to search for property and an entry to search for a person. See n. 13, <i>supra.</i> It is true that the area that may legally be searched is broader when executing a search warrant than when executing an arrest warrant in the home. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span>. This difference may be more theoretical than real, however, because the police may need to check the entire premises for safety reasons, and sometimes they ignore the restrictions on searches incident to arrest.<sup>[29]</sup></p>
<p>But the critical point is that any differences in the intrusiveness of entries to search and entries to arrest are merely ones of degree rather than kind. The two intrusions share this fundamental characteristic: the breach of the entrance to an individual's home. The Fourth Amendment protects the individual's privacy in a variety of settings. In none is the zone of privacy more clearly defined than when bounded by the unambiguous physical dimensions of an individual's homeâ  a zone that finds its roots in clear and specific constitutional terms: "The right of the people to be secure in their . . . houses . . . shall not be violated." That language unequivocally establishes the proposition that "[a]t the very <span class="star-pagination">*590</span> core [of the Fourth Amendment] stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion." <i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 U. S. 505, 511</a></span>. In terms that apply equally to seizures of property and to seizures of persons, the Fourth Amendment has drawn a firm line at the entrance to the house. Absent exigent circumstances, that threshold may not reasonably be crossed without a warrant.</p>
<p></p>
<h2>III</h2>
<p>Without contending that <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span>, decided the question presented by these appeals, New York argues that the reasons that support the <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> holding require a similar result here. In <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> the Court relied on (a) the well-settled common-law rule that a warrantless arrest in a public place is valid if the arresting officer had probable cause to believe the suspect is a felon;<sup>[30]</sup> (b) the clear consensus among the States adhering to that well-settled common-law rule;<sup>[31]</sup> and (c) the expression of the judgment of Congress that such an arrest is "reasonable."<sup>[32]</sup> We consider <span class="star-pagination">*591</span> each of these reasons as it applies to a warrantless entry into a home for the purpose of making a routine felony arrest.</p>
<p></p>
<h2>A</h2>
<p>An examination of the common-law understanding of an officer's authority to arrest sheds light on the obviously relevant, if not entirely dispositive,<sup>[33]</sup> consideration of what the Framers of the Amendment might have thought to be reasonable. Initially, it should be noted that the common-law rules of arrest developed in legal contexts that substantially differ from the cases now before us. In these cases, which involve application of the exclusionary rule, the issue is whether certain <span class="star-pagination">*592</span> evidence is admissible at trial.<sup>[34]</sup> See <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>. At common law, the question whether an arrest was authorized typically arose in civil damages actions for trespass or false arrest, in which a constable's authority to make the arrest was a defense. See, <i>e. g., </i><i>Leach</i> v. <i>Money,</i> 19 How. St. Tr. 1001, 97 Eng. Rep. 1075 (K. B. 1765). Additionally, if an officer was killed while attempting to effect an arrest, the question whether the person resisting the arrest was guilty of murder or manslaughter turned on whether the officer was acting within the bounds of his authority. See M. Foster, Crown Law 308, 312 (1762). See also <i>West</i> v. <i>Cabell,</i> <span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/#85" aria-description="Citation for case: West v. Cabell">153 U. S. 78, 85</a></span>.</p>
<p>A study of the common law on the question whether a constable had the authority to make warrantless arrests in the home on mere suspicion of a felonyâ  as distinguished from an officer's right to arrest for a crime committed in his presenceâ   reveals a surprising lack of judicial decisions and a deep divergence among scholars.</p>
<p>The most cited evidence of the common-law rule consists of an equivocal dictum in a case actually involving the sheriff's authority to enter a home to effect service of civil process. In <i>Semayne's Case,</i> 5 Co. Rep. 91a, 91b, 77 Eng. Rep. 194, 195-196 (K. B. 1603), the Court stated:</p>
<blockquote>"In all cases when the King is party, the Sheriff (if the doors be not open) may break the party's house, either to arrest him, or to do other execution of the K.'s process, if otherwise he cannot enter. But before he breaks it, he ought to signify the cause of his coming, and to make request to open doors; and that appears well by the stat. of Westm. 1. c. 17. (which is but an affirmance of the common law) as hereafter appears, for the law without a default in the owner abhors the destruction <span class="star-pagination">*593</span> or breaking of any house (which is for the habitation and safety of man) by which great damage and inconvenience might ensue to the party, when no default is in him; for perhaps he did not know of the process, of which, if he had notice, it is to be presumed that he would obey it, and that appears by the book in 18 E. 2. Execut. 252. where it is said, that the K's officer who comes to do execution, &amp;c. may open the doors which are shut, and break them, if he cannot have the keys; which proves, that he ought first to demand them, 7 E. 3. 16." (Footnotes omitted.)</blockquote>
<p>This passage has been read by some as describing an entry without a warrant. The context strongly implies, however, that the court was describing the extent of authority in executing the King's writ. This reading is confirmed by the phrase "either to arrest him, or to do <i>other</i> execution of the K.'s process" and by the further point that notice was necessary because the owner may "not know of the <i>process."</i> In any event, the passage surely cannot be said unambiguously to endorse warrantless entries.</p>
<p>The common-law commentators disagreed sharply on the subject.<sup>[35]</sup> Three distinct views were expressed. Lord Coke, <span class="star-pagination">*594</span> widely recognized by the American colonists "as the greatest authority of his time on the laws of England,"<sup>[36]</sup> clearly viewed a warrantless entry for the purpose of arrest to be illegal.<sup>[37]</sup><span class="star-pagination">*595</span> Burn, Foster, and Hawkins agreed,<sup>[38]</sup> as did East and Russell, though the latter two qualified their opinions by stating that if an entry to arrest was made without a warrant, the officer was perhaps immune from liability for the trespass if the suspect was actually guilty.<sup>[39]</sup> Blackstone, Chitty, and Stephen took the opposite view, that entry to arrest without a warrant was legal,<sup>[40]</sup> though Stephen relied on Blackstone who, along with Chitty, in turn relied exclusively on Hale. But Hale's view was not quite so unequivocally expressed.<sup>[41]</sup><span class="star-pagination">*596</span> Further, Hale appears to rely solely on a statement in an early Yearbook, quoted in <i>Burdett</i> v. <i>Abbot,</i> 14 East 1, 155, 104 Eng. Rep. 501, 560 (K. B. 1811):<sup>[42]</sup></p>
<blockquote>"`that for felony, or suspicion of felony, a man may break open the house to take the felon; for it is for the commonweal to take them.'"</blockquote>
<p>Considering the diversity of views just described, however, it is clear that the statement was never deemed authoritative. Indeed, in <i>Burdett,</i> the statement was described as an "extra-judicial opinion." <i><span class="citation" data-id="93880"><a href="/opinion/93880/west-v-cabell/" aria-description="Citation for case: West v. Cabell">Ibid.</a></span></i><sup>[43]</sup></p>
<p>It is obvious that the common-law rule on warrantless home arrests was not as clear as the rule on arrests in public places. Indeed, particularly considering the prominence of Lord Coke, the weight of authority as it appeared to the Framers was to the effect that a warrant was required, or at the minimum that there were substantial risks in proceeding without one. The common-law sources display a sensitivity to privacy interests that could not have been lost on the Framers. The zealous and frequent repetition of the adage that a "man's house is his castle," made it abundantly clear that both in England<sup>[44]</sup><span class="star-pagination">*597</span> and in the Colonies "the freedom of one's house" was one of the most vital elements of English liberty.<sup>[45]</sup></p>
<p>Thus, our study of the relevant common law does not provide the same guidance that was present in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i> Whereas <span class="star-pagination">*598</span> the rule concerning the validity of an arrest in a public place was supported by cases directly in point and by the unanimous views of the commentators, we have found no direct authority supporting forcible entries into a home to make a routine arrest and the weight of the scholarly opinion is somewhat to the contrary. Indeed, the absence of any 17th- or 18th-century English cases directly in point, together with the unequivocal endorsement of the tenet that "a man's house is his castle," strongly suggests that the prevailing practice was not to make such arrests except in hot pursuit or when authorized by a warrant. Cf. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>. In all events, the issue is not one that can be said to have been definitively settled by the common law at the time the Fourth Amendment was adopted.</p>
<p></p>
<h2>B</h2>
<p>A majority of the States that have taken a position on the question permit warrantless entry into the home to arrest even in the absence of exigent circumstances. At this time, 24 States permit such warrantless entries;<sup>[46]</sup> 15 States clearly <span class="star-pagination">*599</span> prohibit them, though 3 States do so on federal constitutional grounds alone;<sup>[47]</sup> and 11 States have apparently taken no position on the question.<sup>[48]</sup></p>
<p>But these current figures reflect a significant decline during the last decade in the number of States permitting warrantless entries for arrest. Recent dicta in this Court raising questions about the practice, see n. 1, <i>supra,</i> and Federal Courts of Appeals' decisions on point, see n. 4, <i>supra,</i> have led state courts to focus on the issue. Virtually all of the state courts that have had to confront the constitutional issue directly have held warrantless entries into the home to arrest to be invalid in the absence of exigent circumstances. See nn. 2, 3, <i>supra.</i> Three state courts have relied on Fourth Amendment <span class="star-pagination">*600</span> grounds alone, while seven have squarely placed their decisions on both federal and state constitutional grounds.<sup>[49]</sup> A number of other state courts, though not having had to confront the issue directly, have recognized the serious nature of the constitutional question.<sup>[50]</sup> Apparently, only the Supreme Court of Florida and the New York Court of Appeals in this case have expressly upheld warrantless entries to arrest in the face of a constitutional challenge.<sup>[51]</sup></p>
<p>A longstanding, widespread practice is not immune from constitutional scrutiny. But neither is it to be lightly brushed aside. This is particularly so when the constitutional standard is as amorphous as the word "reasonable," and when custom and contemporary norms necessarily play such a large role in the constitutional analysis. In this case, although the weight of state-law authority is clear, there is by no means the kind of virtual unanimity on this question that was present in <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i><i>,</i> with regard to warrantless arrests in public places. See <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#422" aria-description="Citation for case: United States v. Watson">423 U. S., at 422-423</a></span>. Only 24 of the 50 States currently sanction warrantless entries into the home to arrest, see nn. 46-48, <i>supra,</i> and there is an obvious declining trend. Further, the strength of the trend is greater than the numbers alone indicate. Seven state courts have recently held that warrantless home arrests violate their respective <i>State</i> Constitutions. See n. 3, <i>supra.</i> That is significant because by invoking a state constitutional provision, a state court immunizes its decision from review by this Court.<sup>[52]</sup> This heightened degree of immutability underscores the depth of the principle underlying the result.</p>
<p></p>
<h2>
<span class="star-pagination">*601</span> C</h2>
<p>No congressional determination that warrantless entries into the home are "reasonable" has been called to our attention. None of the federal statutes cited in the <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> opinion reflects any such legislative judgment.<sup>[53]</sup> Thus, that support for the <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> holding finds no counterpart in this case.</p>
<p>MR. JUSTICE POWELL, concurring in <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#429" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 429</a></span>, stated:</p>
<blockquote>"But logic sometimes must defer to history and experience. The Court's opinion emphasizes the historical sanction accorded warrantless felony arrests [in public places]."</blockquote>
<p>In this case, however, neither history nor this Nation's experience requires us to disregard the overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic.<sup>[54]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*602</span> IV</h2>
<p>The parties have argued at some length about the practical consequences of a warrant requirement as a precondition to a felony arrest in the home.<sup>[55]</sup> In the absence of any evidence that effective law enforcement has suffered in those States that already have such a requirement, see nn. 3, 47, <i>supra,</i> we are inclined to view such arguments with skepticism. More fundamentally, however, such arguments of policy must give way to a constitutional command that we consider to be unequivocal.</p>
<p>Finally, we note the State's suggestion that only a search warrant based on probable cause to believe the suspect is at home at a given time can adequately protect the privacy interests at stake, and since such a warrant requirement is manifestly impractical, there need be no warrant of any kind. We find this ingenious argument unpersuasive. It is true that an arrest warrant requirement may afford less protection than a search warrant requirement, but it will suffice to interpose the magistrate's determination of probable cause between the zealous officer and the citizen. If there is sufficient evidence of a citizen's participation in a felony to persuade a judicial officer that his arrest is justified, it is constitutionally reasonable <span class="star-pagination">*603</span> to require him to open his doors to the officers of the law. Thus, for Fourth Amendment purposes, an arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within.</p>
<p>Because no arrest warrant was obtained in either of these cases, the judgments must be reversed and the cases remanded to the New York Court of Appeals for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACKMUN, concurring.</p>
<p>I joined the Court's opinion in <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976), upholding, on probable cause, the warrantless arrest in a public place. I, of course, am still of the view that the decision in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> is correct. The Court's balancing of the competing governmental and individual interests properly occasioned that result. Where, however, the warrantless arrest is in the suspect's home, that same balancing requires that, absent exigent circumstances, the result be the other way. The suspect's interest in the sanctity of his home then outweighs the governmental interests.</p>
<p>I therefore join the Court's opinion, firm in the conviction that the result in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> and the result here, although opposite, are fully justified by history and by the Fourth Amendment.</p>
<p>MR. JUSTICE WHITE, with whom THE CHIEF JUSTICE and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>The Court today holds that absent exigent circumstances officers may never enter a home during the daytime to arrest for a dangerous felony unless they have first obtained a warrant. This hard-and-fast rule, founded on erroneous assumptions concerning the intrusiveness of home arrest entries, <span class="star-pagination">*604</span> finds little or no support in the common law or in the text and history of the Fourth Amendment. I respectfully dissent.</p>
<p></p>
<h2>I</h2>
<p>As the Court notes, <i>ante,</i> at 591, the common law of searches and seizures, as evolved in England, as transported to the Colonies, and as developed among the States, is highly relevant to the present scope of the Fourth Amendment. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S. 411, 418-422</a></span> (1976); <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#425" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 425, 429</a></span> (POWELL, J., concurring); <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 111, 114</a></span> (1975); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149-153</a></span> (1925); <i>Bad Elk</i> v. <i>United States,</i> <span class="citation" data-id="95265"><a href="/opinion/95265/bad-elk-v-united-states/#534" aria-description="Citation for case: Bad Elk v. United States">177 U. S. 529, 534-535</a></span> (1900); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#622" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 622-630</a></span> (1886); <i>Kurtz</i> v. <i>Moffitt,</i> <span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498-499</a></span> (1885). Today's decision virtually ignores these centuries of common-law development, and distorts the historical meaning of the Fourth Amendment, by proclaiming for the first time a rigid warrant requirement for all nonexigent home arrest entries.</p>
<p></p>
<h2>A</h2>
<p>As early as the 15th century the common law had limited the Crown's power to invade a private dwelling in order to arrest. A Year Book case of 1455 held that in civil cases the sheriff could not break doors to arrest for debt or trespass, for the arrest was then only in the private interests of a party. Y. B. 13 Edw. IV, 9a. To the same effect is <i>Semayne's Case,</i> 5 Co. Rep. 91a, 77 Eng. Rep. 194 (K. B. 1603). The holdings of these cases were condensed in the maxim that "every man's house is his castle." H. Broom, Legal Maxims *321-*329.</p>
<p>However, this limitation on the Crown's power applied only to private civil actions. In cases directly involving the Crown, the rule was that "[t]he king's keys unlock all doors." Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 798</span>, 800 (1924). The Year Book case cited above stated a different rule for criminal cases: for a felony, or suspicion of felony, one may break into the dwelling house to take the felon, for <span class="star-pagination">*605</span> it is for the common weal and to the interest of the King to take him. Likewise, <i>Semayne's Case</i> stated in dictum:</p>
<blockquote>"In all cases when the King is party, the Sheriff (if the doors be not open) may break the party's house, either to arrest him, or to do other execution of the K[ing]'s process, if otherwise he cannot enter." 5 Co. Rep., at 91b, 77 Eng. Rep., at 195.</blockquote>
<p>Although these cases established the Crown's power to enter a dwelling in criminal cases, they did not directly address the question of whether a constable could break doors to arrest without authorization by a warrant. At common law, the constable's office was twofold. As conservator of the peace, he possessed, <i>virtute officii,</i> a "great original and inherent authority with regard to arrests," 4 W. Blackstone, Commentaries *292 (hereinafter Blackstone), and could "without any other warrant but from [himself] arrest felons, and those that [were] probably suspected of felonies," 2 M. Hale, Pleas of the Crown 85 (1736) (hereinafter Hale); see <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 418-419</a></span>. Second, as a subordinate public official, the constable performed ministerial tasks under the authorization and direction of superior officers. See 1 R. Burn, The Justice of the Peace and Parish Officer 295 (6th ed. 1758) (hereinafter Burn); 2 W. Hawkins, Pleas of the Crown 130-132 (6th ed. 1787) (hereinafter Hawkins). It was in this capacity that the constable executed warrants issued by justices of the peace. The warrant authorized the constable to take action beyond his inherent powers.<sup>[1]</sup> It also ensured that he actually carried out his instructions, by giving him clear notice of his duty, for the breach of which he could be punished, 4 Blackstone *291; 1 Burn 295; 2 Hale 88, and by relieving him from civil liability even if probable cause to <span class="star-pagination">*606</span> arrest were lacking, 4 Blackstone *291; 1 Burn 295-296; M. Dalton, The Country Justice 579 (1727 ed.) (hereinafter Dalton); 2 Hawkins 132-133. For this reason, warrants were sometimes issued even when the act commanded was within the constable's inherent authority. Dalton 576.</p>
<p>As the Court notes, commentators have differed as to the scope of the constable's inherent authority, when not acting under a warrant, to break doors in order to arrest. Probably the majority of commentators would permit arrest entries on probable suspicion even if the person arrested were not in fact guilty. 4 Blackstone *292; 1 Burn 87-88;<sup>[2]</sup> 1 J. Chitty, Criminal Law 23 (1816) (hereinafter Chitty); Dalton 426; 1 Hale 583; 2 <i>id.,</i> at 90-94. These authors, in short, would have permitted the type of home arrest entries that occurred in the present cases. The inclusion of Blackstone in this list is particularly significant in light of his profound impact on the minds of the colonists at the time of the framing of the Constitution and the ratification of the Bill of Rights.</p>
<p>A second school of thought, on which the Court relies, held that the constable could not break doors on mere "bare suspicion." M. Foster, Crown Law 321 (1762); 2 Hawkins 139; 1 E. East, Pleas of the Crown 321-322 (1806); 1 W. Russell, Treatise on Crimes and Misdemeanors 745 (1819) (hereinafter Russell). Cf. 4 E. Coke, Institutes *177. Although this doctrine <span class="star-pagination">*607</span> imposed somewhat greater limitations on the constable's inherent power, it does not support the Court's hard-and-fast rule against warrantless nonexigent home entries upon probable cause. East and Russell state explicitly what Foster and Hawkins imply: although mere "bare suspicion" will not justify breaking doors, the constable's action would be justifiable if the person arrested were <i>in fact</i> guilty of a felony. These authorities can be read as imposing a somewhat more stringent requirement of probable cause for arrests in the home than for arrests elsewhere. But they would not bar nonexigent, warrantless home arrests in all circumstances, as the Court does today. And Coke is flatly contrary to the Court's rule requiring a warrant, since he believed that even a warrant would not justify an arrest entry until the suspect had been indicted.</p>
<p>Finally, it bears nothing that the doctrine against home entries on bare suspicion developed in a period in which the validity of <i>any</i> arrest on bare suspicionâ  even one occurring outside the homeâ  was open to question. Not until Lord Mansfield's decision in <i>Samuel</i> v. <i>Payne,</i> <span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">1 Doug. 359</a></span>, 99 Eng. Rep. 230 (K. B. 1780), was it definitively established that the constable could arrest on suspicion even if it turned out that no felony had been committed. To the extent that the commentators relied on by the Court reasoned from any general rule against warrantless arrests based on bare suspicion, the rationale for their position did not survive <i>Samuel</i> v. <i><span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">Payne</a></span></i><i>.</i></p>
<p></p>
<h2>B</h2>
<p>The history of the Fourth Amendment does not support the rule announced today. At the time that Amendment was adopted the constable possessed broad inherent powers to arrest. The limitations on those powers derived, not from a warrant "requirement," but from the generally ministerial nature of the constable's office at common law. Far from restricting the constable's arrest power, the institution of the <span class="star-pagination">*608</span> warrant was used to expand that authority by giving the constable delegated powers of a superior officer such as a justice of the peace. Hence at the time of the Bill of Rights, the warrant functioned as a powerful tool of law enforcement rather than as a protection for the rights of criminal suspects.</p>
<p>In fact, it was the abusive use of the warrant power, rather than any excessive zeal in the discharge of peace officers' inherent authority, that precipitated the Fourth Amendment. That Amendment grew out of colonial opposition to the infamous general warrants known as writs of assistance, which empowered customs officers to search at will, and to break open receptacles or packages, wherever they suspected uncustomed goods to be. <i>United States</i> v. <i>Chadwick,</i> <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#7" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 7-8</a></span> (1977); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 51-78 (1937) (hereinafter Lasson). The writs did not specify where searches could occur and they remained effective throughout the sovereign's lifetime. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#54" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 54</a></span>. In effect, the writs placed complete discretion in the hands of executing officials. Customs searches of this type were beyond the inherent power of common-law officials and were the subject of court suits when performed by colonial customs agents not acting pursuant to a writ. <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#55" aria-description="Citation for case: United States v. Chadwick"><i>Id.,</i> at 55</a></span>.</p>
<p>The common law was the colonists' ally in their struggle against writs of assistance. Hale and Blackstone had condemned general warrants, 1 Hale 580; 4 Blackstone *291, and fresh in the colonists' minds were decisions granting recovery to parties arrested or searched under general warrants on suspicion of seditious libel. <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (K. B. 1765); <i>Huckle</i> v. <i>Money,</i> 2 Wils. 205, 95 Eng. Rep. 768 (K. B. 1763); <i>Wilkes</i> v. <i>Wood,</i> 19 How. St. Tr. 1153, 98 Eng. Rep. 489 (K. B. 1763). When James Otis, Jr., delivered his courtroom oration against writs of assistance in 1761, he looked to the common law in asserting that the writs, if not construed specially, were void as a <span class="star-pagination">*609</span> form of general warrant. 2 Legal Papers of John Adams 139-144 (L. Wroth &amp; H. Zobel eds. 1965).<sup>[3]</sup></p>
<p>Given the colonists' high regard for the common law, it is indeed unlikely that the Framers of the Fourth Amendment intended to derogate from the constable's inherent commonlaw authority. Such an argument was rejected in the important early case of <i>Rohan</i> v. <i>Sawin,</i> <span class="citation no-link">59 Mass. 281</span>, 284-285 (1851):</p>
<blockquote>"It has been sometimes contended, that an arrest of this character, without a warrant, was a violation of the great fundamental principles of our national and state constitutions, forbidding unreasonable searches and arrests, except by warrant founded upon a complaint made under oath. Those provisions doubtless had another and different purpose, being in restraint of general warrants to make searches, and requiring warrants to issue only upon a complaint made under oath. They do not conflict with the authority of constables or other peace-officers. . . to arrest without warrant those who have committed felonies. The public safety, and the due apprehension of criminals, charged with heinous offences, imperiously require that such arrests should be made without warrant by officers of the law."<sup>[4]</sup></blockquote>
<p><span class="star-pagination">*610</span> That the Framers were concerned about warrants, and not about the constable's inherent power to arrest, is also evident from the text and legislative history of the Fourth Amendment. That provision first reaffirms the basic principle of common law, that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated. . . ." The Amendment does not here purport to limit or restrict the peace officer's inherent power to arrest or search, but rather assumes an existing right against actions in excess of that inherent power and ensures that it remain inviolable. As I have noted, it was not generally considered "unreasonable" at common law for officers to break doors in making warrantless felony arrests. The Amendment's second clause is directed at the actions of officers taken in their ministerial capacity pursuant to writs of assistance and other warrants. In contrast to the first Clause, the second Clause does purport to alter colonial practice: "and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>That the Fourth Amendment was directed towards safeguarding the rights at common law, and restricting the warrant practice which gave officers vast new powers beyond their inherent authority, is evident from the legislative history of that provision. As originally drafted by James Madison, it was directed <i>only</i> at warrants; so deeply ingrained was the basic common-law premise that it was not even expressed:</p>
<blockquote>"The rights of the people to be secured in their persons[,] their houses, their papers, and their other property, from all unreasonable searches and seizures, shall not be violated by warrants issued without probable cause, supported by oath or affirmation, or not particularly describing the places to be searched, or the persons or things to be seized." 1 Annals of Cong. 452 (1789).</blockquote>
<p><span class="star-pagination">*611</span> The Committee of Eleven reported the provision as follows:</p>
<blockquote>"The right of the people to be secured in their persons, houses, papers, and effects, shall not be violated by warrants issuing without probable cause, supported by oath or affirmation, and not particularly describing the place to be searched, and the persons or things to be seized." <i>Id.,</i> at 783.</blockquote>
<p>The present language was adopted virtually at the last moment by the Committee of Three, which had been appointed only to arrange the Amendments rather than to make substantive changes in them. Lasson 101. The Amendment passed the House; but "the House seems never to have consciously agreed to the Amendment in its present form." <i>Ibid.</i> In any event, because the sanctity of the common-law protections was assumed from the start, it is evident that the change made by the Committee of Three was a cautionary measure without substantive content.</p>
<p>In sum, the background, text, and legislative history of the Fourth Amendment demonstrate that the purpose was to restrict the abuses that had developed with respect to warrants; the Amendment preserved common-law rules of arrest. Because it was not considered generally unreasonable at common law for officers to break doors to effect a warrantless felony arrest, I do not believe that the Fourth Amendment was intended to outlaw the types of police conduct at issue in the present cases.</p>
<p></p>
<h2>C</h2>
<p>Probably because warrantless arrest entries were so firmly accepted at common law, there is apparently no recorded constitutional challenge to such entries in the 19th-century cases. Common-law authorities on both sides of the Atlantic, however, continued to endorse the validity of such arrests. <i>E. g.,</i> 1 J. Bishop, Commentaries on the Law of Criminal Procedure §§ 195-199 (2d ed. 1872); 1 Chitty 23; 1 J. Colby, A Practical Treatise upon the Criminal Law and Practice of the State <span class="star-pagination">*612</span> of New York 73-74 (1868); F. Heard, A Practical Treatise on the Authority and Duties of Trial Justices, District, Police, and Municipal Courts, in Criminal Cases 135, 148 (1879); 1 Russell 745. Like their predecessors, these authorities conflicted as to whether the officer would be liable in damages if it were shown that the person arrested was not guilty of a felony. But all agreed that warrantless home entries would be permissible in at least some circumstances. None endorsed the rule of today's decision that a warrant is always required, absent exigent circumstances, to effect a home arrest.</p>
<p>Apparently the first official pronouncement on the validity of warrantless home arrests came with the adoption of state codes of criminal procedure in the latter 19th and early 20th centuries. The great majority of these codes accepted and endorsed the inherent authority of peace officers to enter dwellings in order to arrest felons. By 1931, 24 of 29 state codes authorized such warrantless arrest entries.<sup>[5]</sup> By 1975, 31 of 37 state codes authorized warrantless home felony arrests.<sup>[6]</sup> The American Law Institute included such authority in its model legislation in 1931 and again in 1975.<sup>[7]</sup></p>
<p>The first direct judicial holding on the subject of warrantless home arrests seems to have been <i>Commonwealth</i> v. <i>Phelps,</i> <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">209 Mass. 396</a></span>, <span class="citation" data-id="6431509"><a href="/opinion/6557761/commonwealth-v-phelps/" aria-description="Citation for case: Commonwealth v. Phelps">95 N. E. 868</a></span> (1911). The holding in this case that such entries were constitutional became the settled rule in the States for much of the rest of the century. See Wilgus, Arrest Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 798</span>, 803 (1924). Opinions of this Court also assumed that such arrests were constitutional.<sup>[8]</sup></p>
<p><span class="star-pagination">*613</span> This Court apparently first questioned the reasonableness of warrantless nonexigent entries to arrest in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958), noting in dictum that such entries would pose a "grave constitutional question" if carried out at night.<sup>[9]</sup> In <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#480" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 480</a></span> (1971), the Court stated, again in dictum:</p>
<blockquote>"[I]f [it] is correct that it has generally been assumed that the Fourth Amendment is not violated by the warrantless entry of a man's house for purposes of arrest, it might be wise to re-examine the assumption. Such a re-examination `would confront us with a grave constitutional question, namely, whether the forcible nighttime entry into a dwelling to arrest a person reasonably believed within, upon probable cause that he had committed a felony, under circumstances where no reason appears why an arrest warrant could not have been sought, is consistent with the Fourth Amendment.' <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S., at 499-500</a></span>."</blockquote>
<p>Although <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> and <i><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> both referred to the special problem of warrantless entries during the nighttime,<sup>[10]</sup> it is not surprising that state and federal courts have tended to read those dicta as suggesting a broader infirmity applying to daytime entries also, and that the majority of recent decisions have been against the constitutionality of all types of warrantless, nonexigent home arrest entries. As the Court concedes, <span class="star-pagination">*614</span> however, even despite <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span></i> and <i><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> it remains the case that</p>
<blockquote>"[a] majority of the States that have taken a position on the question permit warrantless entry into the home to arrest even in the absence of exigent circumstances. At this time, 24 States permit such warrantless entries; 15 States clearly prohibit them, though 3 States do so on federal constitutional grounds alone; and 11 States have apparently taken no position on the question." <i>Ante,</i> at 598-599 (footnotes omitted).</blockquote>
<p>This consensus, in the face of seemingly contrary dicta from this Court, is entitled to more deference than the Court today provides. Cf. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976).</p>
<p></p>
<h2>D</h2>
<p>In the present cases, as in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>,</i> the applicable federal statutes are relevant to the reasonableness of the type of arrest in question. Under <span class="citation no-link">18 U. S. C. § 3052</span>, specified federal agents may "make arrests without warrants for any offense against the United States committed in their presence, or for any felony cognizable under the laws of the United States, if they have reasonable grounds to believe that the person to be arrested has committed or is committing such felony." On its face this provision authorizes federal agents to make warrantless arrests anywhere, including the home. Particularly in light of the accepted rule at common law and among the States permitting warrantless home arrests, the absence of any explicit exception for the home from § 3052 is persuasive evidence that Congress intended to authorize warrantless arrests there a well as elsewhere.</p>
<p>Further, Congress has not been unaware of the special problems involved in police entries into the home. In <span class="citation no-link">18 U. S. C. § 3109</span>, it provided that</p>
<blockquote>"[t]he officer may break open any outer or inner door or window of a house, or any part of a house, or anything <span class="star-pagination">*615</span> therein, to execute a search warrant, if, after notice of his authority and purpose, he is refused admittance. . . ."</blockquote>
<p>See <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/" aria-description="Citation for case: Miller v. United States">357 U. S. 301</a></span> (1958). In explicitly providing authority to enter when executing a search warrant, Congress surely did not intend to derogate from the officers' power to effect an arrest entry either with or without a warrant. Rather, Congress apparently assumed that this power was so firmly established either at common law or by statute that no explicit grant of arrest authority was required in § 3109. In short, although the Court purports to find no guidance in the relevant federal statutes, I believe that fairly read they authorize the type of police conduct at issue in these cases.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>Today's decision rests, in large measure, on the premise that warrantless arrest entries constitute a particularly severe invasion of personal privacy. I do not dispute that the home is generally a very private area or that the common law displayed a special "reverence . . . for the individual's right of privacy in his house." <i>Miller</i> v. <i>United States, supra,</i> at 313. However, the Fourth Amendment is concerned with protecting people, not places, and no talismanic significance is given to the fact that an arrest occurs in the home rather than elsewhere. Cf. <i>Ybarra</i> v. <i>Illinois,</i> <span class="citation" data-id="9427721"><a href="/opinion/110158/ybarra-v-illinois/" aria-description="Citation for case: Ybarra v. Illinois">444 U. S. 85</a></span> (1979); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#351" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 351</a></span> (1967); <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S., at 630</a></span>. It is necessary in each case to assess realistically the actual extent of invasion of constitutionally protected privacy. Further, as MR. JUSTICE POWELL observed in <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#428" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 428</a></span> (concurring opinion), all arrests involve serious intrusions into an individual's privacy and dignity. Yet we settled in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i> that the intrusiveness of a public arrest is not enough to mandate the obtaining of a warrant. The inquiry in the present case, therefore, is whether the incremental <span class="star-pagination">*616</span> intrusiveness that results from an arrest's being made <i>in the dwelling</i> is enough to support an inflexible constitutional rule requiring warrants for such arrests whenever exigent circumstances are not present.</p>
<p>Today's decision ignores the carefully crafted restrictions on the common-law power of arrest entry and thereby overestimates the dangers inherent in that practice. At common law, absent exigent circumstances, entries to arrest could be made only for felony. Even in cases of felony, the officers were required to announce their presence, demand admission, and be refused entry before they were entitled to break doors.<sup>[11]</sup> Further, it seems generally accepted that entries could be made only during daylight hours.<sup>[12]</sup> And, in my view, the officer entering to arrest must have reasonable grounds to believe, not only that the arrestee has committed a crime, but also that the person suspected is present in the house at the time of the entry.<sup>[13]</sup></p>
<p>These four restrictions on home arrestsâ  felony, knock and announce, daytime, and stringent probable causeâ  constitute powerful and complementary protections for the privacy interests associated with the home. The felony requirement guards against abusive or arbitrary enforcement and ensures that invasions of the home occur only in case of the most <span class="star-pagination">*617</span> serious crimes. The knock-and-announce and daytime requirements protect individuals against the fear, humiliation, and embarrassment of being roused from their beds in states of partial or complete undress. And these requirements allow the arrestee to surrender at his front door, thereby maintaining his dignity and preventing the officers from entering other rooms of the dwelling. The stringent probable-cause requirement would help ensure against the possibility that the police would enter when the suspect was not home, and, in searching for him, frighten members of the family or ransack parts of the house, seizing items in plain view. In short, these requirements, taken together, permit an individual suspected of a serious crime to surrender at the front door of his dwelling and thereby avoid most of the humiliation and indignity that the Court seems to believe necessarily accompany a house arrest entry. Such a front-door arrest, in my view, is no more intrusive on personal privacy than the public warrantless arrests which we found to pass constitutional muster in <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span>.</i><sup>[14]</sup></p>
<p>All of these limitations on warrantless arrest entries are satisfied on the facts of the present cases. The arrests here were for serious feloniesâ  murder and armed robberyâ  and both occurred during daylight hours. The authorizing statutes required that the police announce their business and demand entry; neither Payton nor Riddick makes any contention that these statutory requirements were not fulfilled. And it is not argued that the police had no probable cause to believe that both Payton and Riddick were in their dwellings at the time of the entries. Today's decision, therefore, sweeps away any possibility that warrantless home entries might be permitted in some limited situations other than those in which <span class="star-pagination">*618</span> exigent circumstances are present. The Court substitutes, in one sweeping decision, a rigid constitutional rule in place of the common-law approach, evolved over hundreds of years, which achieved a flexible accommodation between the demands of personal privacy and the legitimate needs of law enforcement.</p>
<p>A rule permitting warrantless arrest entries would not pose a danger that officers would use their entry power as a pretext to justify an otherwise invalid warrantless search. A search pursuant to a warrantless arrest entry will rarely, if ever, be as complete as one under authority of a search warrant. If the suspect surrenders at the door, the officers may not enter other rooms. Of course, the suspect may flee or hide, or may not be at home, but the officers cannot anticipate the first two of these possibilities and the last is unlikely given the requirement of probable cause to believe that the suspect is at home. Even when officers are justified in searching other rooms, they may seize only items within the arrestee's possession or immediate control or items in plain view discovered during the course of a search reasonably directed at discovering a hiding suspect. Hence a warrantless home entry is likely to uncover far less evidence than a search conducted under authority of a search warrant. Furthermore, an arrest entry will inevitably tip off the suspects and likely result in destruction or removal of evidence not uncovered during the arrest. I therefore cannot believe that the police would take the risk of losing valuable evidence through a pretextual arrest entry rather than applying to a magistrate for a search warrant.</p>
<p></p>
<h2>B</h2>
<p>While exaggerating the invasion of personal privacy involved in home arrests, the Court fails to account for the danger that its rule will "severely hamper effective law enforcement," <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#431" aria-description="Citation for case: United States v. Watson">423 U. S., at 431</a></span> (POWELL, J., concurring); <i>Gerstein</i> v. <i>Pugh</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 113</a></span>. The policeman <span class="star-pagination">*619</span> on his beat must now make subtle discriminations that perplex even judges in their chambers. As MR. JUSTICE POWELL noted, concurring in <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson, supra</a></span></i><i>,</i> police will sometimes delay making an arrest, even after probable cause is established, in order to be sure that they have enough evidence to convict. Then, if they suddenly have to arrest, they run the risk that the subsequent exigency will not excuse their prior failure to obtain a warrant. This problem cannot effectively be cured by obtaining a warrant as soon as probable cause is established because of the chance that the warrant will go state before the arrest is made.</p>
<p>Further, police officers will often face the difficult task of deciding whether the circumstances are sufficiently exigent to justify their entry to arrest without a warrant. This is a decision that must be made quickly in the most trying of circumstances. If the officers mistakenly decide that the circumstances are exigent, the arrest will be invalid and any evidence seized incident to the arrest or in plain view will be excluded at trial. On the other hand, if the officers mistakenly determine that exigent circumstances are lacking, they may refrain from making the arrest, thus creating the possibility that a dangerous criminal will escape into the community. The police could reduce the likelihood of escape by staking out all possible exits until the circumstances become clearly exigent or a warrant is obtained. But the costs of such a stakeout seem excessive in an era of rising crime and scarce police resources.</p>
<p>The uncertainty inherent in the exigent-circumstances determination burdens the judicial system as well. In the case of searches, exigent circumstances are sufficiently unusual that this Court has determined that the benefits of a warrant outweigh the burdens imposed, including the burdens on the judicial system. In contrast, arrests recurringly involve exigent circumstances, and this Court has heretofore held that a warrant can be dispensed with without undue sacrifice in Fourth Amendment values. The situation should be no different <span class="star-pagination">*620</span> with respect to arrests in the home. Under today's decision, whenever the police have made a warrantless home arrest there will be the possibility of "endless litigation with respect to the existence of exigent circumstances, whether it was practicable to get a warrant, whether the suspect was about to flee, and the like," <i>United States</i> v. <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#423" aria-description="Citation for case: United States v. Watson"><i>Watson, supra,</i> at 423-424</a></span>.</p>
<p>Our cases establish that the ultimate test under the Fourth Amendment is one of "reasonableness." <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#315" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 315-316</a></span> (1978); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 539</a></span> (1967). I cannot join the Court in declaring unreasonable a practice which has been thought entirely reasonable by so many for so long. It would be far preferable to adopt a clear and simple rule: after knocking and announcing their presence, police may enter the home to make a daytime arrest without a warrant when there is probable cause to believe that the person to be arrested committed a felony and is present in the house. This rule would best comport with the common-law background, with the traditional practice in the States, and with the history and policies of the Fourth Amendment. Accordingly, I respectfully dissent.</p>
<p>MR. JUSTICE REHNQUIST, dissenting.</p>
<p>The Court today refers to both <i>Payton</i> and <i>Riddick</i> as involving "routine felony arrests." I have no reason to dispute the Court's characterization of these arrests, but cannot refrain from commenting on the social implications of the result reached by the Court. Payton was arrested for the murder of the manager of a gas station; Riddick was arrested for two armed robberies. If these are indeed "routine felony arrests," which culminated in convictions after trial upheld by the state courts on appeal, surely something is amiss in the process of the administration of criminal justice whereby these convictions are now set aside by this Court under the exclusionary rule which we have imposed upon the States under <span class="star-pagination">*621</span> the Fourth and Fourteenth Amendments to the United States Constitution.</p>
<p>I fully concur in and join the dissenting opinion of MR. JUSTICE WHITE. There is significant historical evidence that we have over the years misread the history of the Fourth Amendment in connection with searches, elevating the warrant requirement over the necessity for probable cause in a way which the Framers of that Amendment did not intend. See T. Taylor, Two Studies in Constitutional Interpretation 38-50 (1969). But one may accept all of that as <i>stare decisis,</i> and still feel deeply troubled by the transposition of these same errors into the area of actual arrests of felons within their houses with respect to whom there is probable cause to suspect guilt of the offense in question.</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 78-5421, <i>Riddick</i> v. <i>New York,</i> also on appeal from the same court.</p>
<p>[1]  See also <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#433" aria-description="Citation for case: United States v. Watson">423 U. S., at 433</a></span> (STEWART, J., concurring); <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#432" aria-description="Citation for case: United States v. Watson"><i>id.,</i> at 432-433</a></span> (POWELL, J., concurring); <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113, n. 13</a></span>; <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-481</a></span>; <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span>. Cf. <i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span>.</p>
<p>[2]  See <i>State</i> v. <i>Perez,</i> <span class="citation" data-id="1836490"><a href="/opinion/1836490/state-v-perez/" aria-description="Citation for case: State v. Perez">277 So. 2d 778</a></span> (1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1064/">414 U. S. 1064</a></span>.</p>
<p>[3]  See <i>State</i> v. <i>Cook,</i> <span class="citation" data-id="9793807"><a href="/opinion/2616403/state-v-cook/" aria-description="Citation for case: State v. Cook">115 Ariz. 188</a></span>, <span class="citation" data-id="9793807"><a href="/opinion/2616403/state-v-cook/" aria-description="Citation for case: State v. Cook">564 P. 2d 877</a></span> (1977) (resting on both state and federal constitutional provisions); <i>People</i> v. <i>Ramey,</i> <span class="citation" data-id="9551973"><a href="/opinion/1185860/people-v-ramey/" aria-description="Citation for case: People v. Ramey">16 Cal. 3d 263</a></span>, <span class="citation" data-id="9551973"><a href="/opinion/1185860/people-v-ramey/" aria-description="Citation for case: People v. Ramey">545 P. 2d 1333</a></span> (1976), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./429/929/">429 U. S. 929</a></span> (state and federal); <i>People</i> v. <i>Moreno,</i> <span class="citation" data-id="9619146"><a href="/opinion/1396585/people-v-moreno/" aria-description="Citation for case: People v. Moreno">176 Colo. 488</a></span>, <span class="citation" data-id="9619146"><a href="/opinion/1396585/people-v-moreno/" aria-description="Citation for case: People v. Moreno">491 P. 2d 575</a></span> (1971) (federal only); <i>State</i> v. <i>Jones,</i> <span class="citation" data-id="1860990"><a href="/opinion/1860990/state-v-jones/" aria-description="Citation for case: State v. Jones">274 N. W. 2d 273</a></span> (Iowa 1979) (state and federal); <i>State</i> v. <i>Platten,</i> <span class="citation" data-id="1435637"><a href="/opinion/1435637/state-v-platten/" aria-description="Citation for case: State v. Platten">225 Kan. 764</a></span>, <span class="citation" data-id="1435637"><a href="/opinion/1435637/state-v-platten/" aria-description="Citation for case: State v. Platten">594 P. 2d 201</a></span> (1979) (state and federal); <i>Commonwealth</i> v. <i>Forde,</i> <span class="citation" data-id="9519710"><a href="/opinion/2017555/commonwealth-v-forde/" aria-description="Citation for case: Commonwealth v. Forde">367 Mass. 798</a></span>, <span class="citation" data-id="9519710"><a href="/opinion/2017555/commonwealth-v-forde/" aria-description="Citation for case: Commonwealth v. Forde">329 N. E. 2d 717</a></span> (1975) (federal only); <i>State</i> v. <i>Olson,</i> <span class="citation" data-id="1218237"><a href="/opinion/1218237/state-v-olson/" aria-description="Citation for case: State v. Olson">287 Ore. 157</a></span>, <span class="citation" data-id="1218237"><a href="/opinion/1218237/state-v-olson/" aria-description="Citation for case: State v. Olson">598 P. 2d 670</a></span> (1979) (state and federal); <i>Commonwealth</i> v. <i>Williams,</i> <span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">483 Pa. 293</a></span>, <span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">396 A. 2d 1177</a></span> (1978) (federal only); <i>State</i> v. <i>McNeal,</i> <span class="citation" data-id="9605191"><a href="/opinion/1369726/state-v-mcneal/" aria-description="Citation for case: State v. McNeal">251 S. E. 2d 484</a></span> (W. Va. 1978) (state and federal); <i>Laasch</i> v. <i>State,</i> <span class="citation" data-id="9718617"><a href="/opinion/2106646/laasch-v-state/" aria-description="Citation for case: Laasch v. State">84 Wis. 2d 587</a></span>, <span class="citation" data-id="9718617"><a href="/opinion/2106646/laasch-v-state/" aria-description="Citation for case: Laasch v. State">267 N. W. 2d 278</a></span> (1978) (state and federal).</p>
<p>[4]  Compare <i>United States</i> v. <i>Reed,</i> <span class="citation" data-id="354014"><a href="/opinion/354014/united-states-v-nancy-reed-and-morris-goldsmith-aka-marlowe/" aria-description="Citation for case: United States v. Nancy Reed and Morris Goldsmith, A/K/A...">572 F. 2d 412</a></span> (CA2 1978), cert. denied <i>sub nom. </i><i>Goldsmith</i> v. <i>United States,</i> <span class="citation" data-id="9013020"><a href="/opinion/9019821/goldsmith-v-united-states/" aria-description="Citation for case: Goldsmith v. United States">439 U. S. 913</a></span>; <i>United States</i> v. <i>Killebrew,</i> <span class="citation" data-id="348416"><a href="/opinion/348416/united-states-v-gerald-killebrew/" aria-description="Citation for case: United States v. Gerald Killebrew">560 F. 2d 729</a></span> (CA6 1977); <i>United States</i> v. <i>Shye,</i> <span class="citation" data-id="317251"><a href="/opinion/317251/united-states-v-reginald-jerome-shye/" aria-description="Citation for case: United States v. Reginald Jerome Shye">492 F. 2d 886</a></span> (CA6 1974); <i>United States</i> v. <i>Houte,</i> <span class="citation" data-id="369038"><a href="/opinion/369038/united-states-v-edward-corbit-houle/" aria-description="Citation for case: United States v. Edward Corbit Houle">603 F. 2d 1297</a></span> (CA8 1979); <i>United States</i> v. <i>Prescott,</i> <span class="citation" data-id="9465056"><a href="/opinion/358848/united-states-v-saundra-prescott/" aria-description="Citation for case: United States v. Saundra Prescott">581 F. 2d 1343</a></span> (CA9 1978); <i>Dorman</i> v. <i>United States,</i> 140 U. S. App. D. C. 313, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385</a></span> (1970), with <i>United States</i> v. <i>Williams,</i> <span class="citation" data-id="354259"><a href="/opinion/354259/united-states-v-william-august-halm-williams/" aria-description="Citation for case: United States v. William August Halm Williams">573 F. 2d 348</a></span> (CA5 1978); <i>United States ex rel. Wright</i> v. <i>Woods,</i> <span class="citation" data-id="292629"><a href="/opinion/292629/united-states-of-america-ex-rel-charles-a-wright-v-joseph-woods/" aria-description="Citation for case: United States of America Ex Rel. Charles A. Wright v....">432 F. 2d 1143</a></span> (CA7 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/966/">401 U. S. 966</a></span>. Three other Circuits have assumed without deciding that warrantless home arrests are unconstitutional. <i>United States</i> v. <i>Bradley,</i> <span class="citation" data-id="301708"><a href="/opinion/301708/united-states-v-charles-b-bradley-jr/" aria-description="Citation for case: United States v. Charles B. Bradley, Jr.">455 F. 2d 1181</a></span> (CA1 1972); <i>United States</i> v. <i>Davis,</i> <span class="citation" data-id="303979"><a href="/opinion/303979/united-states-v-kelley-davis-aka-tee-in-no-71-1778-and-inez-davis/" aria-description="Citation for case: United States v. Kelley Davis A/K/A Tee, in No. 71-1778,...">461 F. 2d 1026</a></span> (CA3 1972); <i>Vance</i> v. <i>North Carolina,</i> <span class="citation" data-id="292572"><a href="/opinion/292572/jacob-vance-jr-v-state-of-north-carolina/" aria-description="Citation for case: Jacob Vance, Jr. v. State of North Carolina">432 F. 2d 984</a></span> (CA4 1970). And one Circuit has upheld such an arrest without discussing the constitutional issue. <i>Michael</i> v. <i>United States,</i> <span class="citation" data-id="279701"><a href="/opinion/279701/joyce-marie-michael-v-united-states/" aria-description="Citation for case: Joyce Marie Michael v. United States">393 F. 2d 22</a></span> (CA10 1968).</p>
<p>[5]  A thorough search of the apartment resulted in the seizure of additional evidence tending to prove Payton's guilt, but the prosecutor stipulated that the officers' warrantless search of the apartment was illegal and that all the seized evidence except the shell casing should be suppressed.
</p>
<p>"MR. JACOBS: There's no question that the evidence that was found in bureau drawers and in the closet was illegally obtained. I'm perfectly willing to concede that, and I do so in my memorandum of law. There's no question about that." App. 4.</p>
<p>[6]  "At the time in question, January 15, 1970, the law applicable to the police conduct related above was governed by the Code of Criminal Procedure. Section 177 of the Code of Criminal Procedure as applicable to this case recited: `A peace officer may, without a warrant, arrest a person. . . 3. When a felony has in fact been committed, and he has reasonable cause for believing the person to be arrested to have committed it.' Section 178 of the Code of Criminal Procedure provided: `To make an arrest, as provided in the last section [177], the officer may break open an outer or inner door or window of a building, if, after notice of his office and purpose, he be refused admittance.'" <span class="citation" data-id="6197069"><a href="/opinion/6328523/people-v-payton/#974" aria-description="Citation for case: People v. Payton">84 Misc. 2d 973, 974-975</a></span>, 376 N. Y. S. 2d 779, 780 (Sup. Ct., Trial Term, N. Y. County, 1974).</p>
<p>[7]  "Although Detective Malfer knocked on the defendant's door, it is not established that at this time he announced that his purpose was to arrest the defendant. Such a declaration of purpose is unnecessary when exigent circumstances are present (<i>People</i> v. <i>Wojciechowski,</i> <span class="citation" data-id="5768902"><a href="/opinion/5911360/people-v-wojciechowski/" aria-description="Citation for case: People v. Wojciechowski">31 AD 2d 658</a></span>; <i>People</i> v. <i>McIlwain,</i> <span class="citation" data-id="5763049"><a href="/opinion/5905685/people-v-mcilwain/" aria-description="Citation for case: People v. McIlwain">28 AD 2d 711</a></span>).
</p>
<p>"`Case law has made exceptions from the statute or common-law rules for exigent circumstances which may allow dispensation with the notice . . . It has also been held or suggested that notice is not required if there is reason to believe that it will allow an escape or increase unreasonably the physical risk to the police or to innocent persons.' (<i>People</i> v. <i>Floyd,</i> <span class="citation" data-id="5525551"><a href="/opinion/5677661/people-v-floyd/#562" aria-description="Citation for case: People v. Floyd">26 NY 2d 558, 562</a></span>.)</p>
<p>"The facts of this matter indicate that a grave offense had been committed; that the suspect was reasonably believed to be armed and could be a danger to the community; that a clear showing of probable cause existed and that there was strong reason to believe that the suspect was in the premises being entered and that he would escape if not swiftly apprehended. From this fact the court finds that exigent circumstances existed to justify noncompliance with section 178. The court holds, therefore, that the entry into defendant's apartment was valid." <i>Id,</i> at 975, 376 N. Y. S. 2d, at 780-781.</p>
<p>[8]  55 App. Div. 2d 859 (1976).</p>
<p>[9]  New York Crim. Proc. Law § 140.15 (4) (McKinney 1971) provides, with respect to arrest without a warrant:
</p>
<p>"In order to effect such an arrest, a police officer may enter premises in which he reasonably believes such person to be present, under the same circumstances and in the same manner as would be authorized, by the provisions of subdivisions four and five of section 120.80, if he were attempting to make such arrest pursuant to a warrant of arrest."</p>
<p>Section 120.80, governing execution of arrest warrants, provides in relevant part:</p>
<p>"4. In order to effect the arrest, the police officer may, under circumstances and in a manner prescribed in this subdivision, enter any premises in which he reasonably believes the defendant to be present. Before such entry, he must give, or make reasonable effort to give, notice of his authority and purpose to an occupant thereof, unless there is reasonable cause to believe that the giving of such notice will:</p>
<p>"(a) Result in the defendant escaping or attempting to escape; or</p>
<p>"(b) Endanger the life or safety of the officer or another person; or</p>
<p>"(c) Result in the destruction, damaging or secretion of material evidence.</p>
<p>"5. If the officer is authorized to enter premises without giving notice of his authority and purpose, or if after giving such notice he is not admitted, he may enter such premises, and by a breaking if necessary."</p>
<p>[10]  App. 63-66.</p>
<p>[11]  56 App. Div. 2d 937, 392 N. Y. S. 2d 848 (1977). One justice dissented on the ground that the officers' failure to announce their authority and purpose before entering the house made the arrest illegal as a matter of state law.</p>
<p>[12]  45 N. Y. 2d, at 309-310, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#228" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 228</a></span>.</p>
<p>[13]  The majority continued:
</p>
<p>"In the case of the search, unless appropriately limited by the terms of a warrant, the incursion on the householder's domain normally will be both more extensive and more intensive and the resulting invasion of his privacy of greater magnitude than what might be expected to occur on an entry made for the purpose of effecting his arrest. A search by its nature contemplates a possibly thorough rummaging through possessions, with concurrent upheaval of the owner's chosen or random placement of goods and articles and disclosure to the searchers of a myriad of personal items and details which he would expect to be free from scrutiny by uninvited eyes. The householder by the entry and search of his residence is stripped bare, in greater or lesser degree, of the privacy which normally surrounds him in his daily living, and, if he should be absent, to an extent of which he will be unaware.</p>
<p>"Entry for the purpose of arrest may be expected to be quite different. While the taking into custody of the person of the householder is unquestionably of grave import, there is no accompanying prying into the area of expected privacy attending his possessions and affairs. That personal seizure alone does not require a warrant was established by <i>United States</i> v. <i>Watson</i> (<span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 US 411</a></span>, <i>supra),</i> which upheld a warrantless arrest made in a public place. In view of the minimal intrusion on the elements of privacy of the home which results from entry on the premises for making an arrest (as compared with the gross intrusion which attends the arrest itself), we perceive no sufficient reason for distinguishing between an arrest in a public place and an arrest in a residence. To the extent that an arrest will always be distasteful or offensive, there is little reason to assume that arrest within the home is any more so than arrest in a public place; on the contrary, it may well be that because of the added exposure the latter may be more objectionable.</p>
<p>"At least as important, and perhaps even more so, in concluding that entries to make arrests are not `unreasonable'â  the substantive test under the constitutional proscriptionsâ  is the objective for which they are made, viz., the arrest of one reasonably believed to have committed a felony, with resultant protection to the community. The `reasonableness' of any governmental intrusion is to be judged from two perspectivesâ  that of the defendant, considering the degree and scope of the invasion of his person or property; that of the People, weighing the objective and imperative of governmental action. The community's interest in the apprehension of criminal suspects is of a higher order than is its concern for the recovery of contraband or evidence; normally the hazards created by the failure to apprehend far exceed the risks which may follow nonrecovery." <i>Id.,</i> at 310-311, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#229" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 229</a></span>.</p>
<p>[14]  "The apparent historical acceptance in the English common law of warrantless entries to make felony arrests (2 Hale, Historia Placitorum Coronae, History of Pleas of Crown [1st Amer ed, 1847], p. 92; Chitty, Criminal Law [3d Amer, from 2d London, ed, 1836] 22-23), and the existence of statutory authority for such entries in this State since the enactment of the Code of Criminal Procedure in 1881 argue against a holding of unconstitutionality and substantiate the reasonableness of such procedure. . . .
</p>
<p>"Nor do we ignore the fact that a number of jurisdictions other than our own have also enacted statutes authorizing warrantless entries of buildings (without exception for homes) for purposes of arrest. The American Law Institute's Model Code of Pre-Arraignment Procedure makes similar provision in section 120.6, with suggested special restrictions only as to nighttime entries." <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#311" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 311-312</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#229" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 229-230</a></span> (footnote omitted).</p>
<p>[15]  <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#315" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 315</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#232" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 232</a></span> (Wachtler, J., dissenting).</p>
<p>[16]  <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#319" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 319-320</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#235" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 235</a></span> (Cooke, J., dissenting).</p>
<p>[17]  "Although the point has not been squarely adjudicated since <i>Coolidge</i> [v. <i>New Hampshire</i><i>,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span>,] (see <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 US 411, 418, n. 6</a></span>), its proper resolution, it is submitted, is manifest. At the core of the Fourth Amendment, whether in the context of a search or an arrest, is the fundamental concept that any governmental intrusion into an individual's home or expectation of privacy must be strictly circumscribed (see, <i>e. g., </i><i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 US 616, 630</a></span>; <i>Camara</i> v. <i>Municipal Ct.,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 US 523, 528</a></span>). To achieve that end, the framers of the amendment interposed the warrant requirement between the public and the police, reflecting their conviction that the decision to enter a dwelling should not rest with the officer in the field, but rather with a detached and disinterested Magistrate (<i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 US 451, 455-456</a></span>; <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 US 10, 13-14</a></span>). Inasmuch as the purpose of the Fourth Amendment is to guard against arbitrary governmental invasions of the home, the necessity of prior judicial approval should control any contemplated entry, regardless of the purpose for which that entry is sought. By definition, arrest entries must be included within the scope of the amendment, for while such entries are for persons, not things, they are nonetheless, violations of privacy, the chief evil that the Fourth Amendment was designed to deter (<i>Silverman</i> v. <i>United States,</i> <span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/#511" aria-description="Citation for case: Silverman v. United States">365 US 505, 511</a></span>)." <i>Id.,</i> at 320-321, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#235" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 235-236</a></span> (Cooke, J., dissenting).</p>
<p>[18]  <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#324" aria-description="Citation for case: People v. Payton"><i>Id.,</i> at 324</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#238" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 238</a></span> (Cooke, J., dissenting).</p>
<p>[19]  Although it is not clear from the record that appellants raised this constitutional issue in the trial courts, since the highest court of the State passed on it, there is no doubt that it is properly presented for review by this Court. See <i>Raley</i> v. <i>Ohio,</i> <span class="citation" data-id="105925"><a href="/opinion/105925/raley-v-ohio/#436" aria-description="Citation for case: Raley v. Ohio">360 U. S. 423, 436</a></span>.</p>
<p>[20]  45 N. Y. 2d, at 308, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#228" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 228</a></span>. Judge Wachtler in dissent, however, would have upheld the warrantless entry in Payton's case on exigency grounds, and therefore agreed with the majority's refusal to suppress the shell casing. See <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#315" aria-description="Citation for case: People v. Payton"><i>id.,</i> at 315</a></span>, <span class="citation" data-id="5531666"><a href="/opinion/5683033/people-v-payton/#232" aria-description="Citation for case: People v. Payton">380 N. E. 2d, at 232</a></span>.</p>
<p>[21]  "Vivid in the memory of the newly independent Americans were those general warrants known as writs of assistance under which officers of the Crown had so bedeviled the colonists. The hated writs of assistance had given customs officials blanket authority to search where they pleased for goods imported in violation of British tax laws. They were denounced by James Otis as `the worst instrument of arbitrary power, the most destructive of English liberty, and the fundamental principles of law, that ever was found in an English law book,' because they placed `the liberty of every man in the hands of every petty officer.' The historic occasion of that denunciation, in 1761 at Boston, has been characterized as `perhaps the most prominent event which inaugurated the resistance of the colonies to the oppressions of the mother country. "Then and there," said John Adams, "then and there was the first scene of the first act of opposition to the arbitrary claims of Great Britain. Then and there the child Independence was born."' <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#625" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 625</a></span>." <i>Stanford</i> v. <i>Texas,</i> <span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#481" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 481-482</a></span>.
</p>
<p>See also J. Landynski, Search and Seizure and the Supreme Court 19-48 (1966); N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 13-78 (1937); T. Taylor, Two Studies in Constitutional Interpretation 19-44 (1969).</p>
<p>[22]  "`The rights of the people to be secured in their persons, their houses, their papers, and their other property, from all unreasonable searches and seizures, shall not be violated by warrants issued without probable cause, supported by oath or affirmation, or not particularly describing the places to be searched, or the persons or things to be seized.' Annals of Cong., 1st Cong., 1st sess., p. 452." Lasson, <i>supra,</i> at 100, n. 77.</p>
<p>[23]  "The general right of security from unreasonable search and seizure was given a sanction of its own and the amendment thus intentionally given a broader scope. That the prohibition against `unreasonable searches' was intended, accordingly, to cover something other than the form of the warrant is a question no longer left to implication to be derived from the phraseology of the Amendment." Lasson, <i>supra,</i> at 103. (Footnote omitted.)</p>
<p>[24]  As Mr. Justice Jackson so cogently observed in <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">333 U. S. 10</a></span>, 13-14:
</p>
<p>"The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. Any assumption that evidence sufficient to support a magistrate's disinterested determination to issue a search warrant will justify the officers in making a search without a warrant would reduce the Amendment to a nullity and leave the people's homes secure only in the discretion of police officers. Crime, even in the privacy of one's own quarters, is, of course, of grave concern to society, and the law allows such crime to be reached on proper showing. The right of officers to thrust themselves into a home is also a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent." (Footnotes omitted.)</p>
<p>[25]  As the Court stated in <i>Coolidge</i> v. <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">New Hampshire</a></span></i><i>:</i>
</p>
<p>"Both sides to the controversy appear to recognize a distinction between searches and seizures that take place on a man's propertyâ  his home or officeâ  and those carried out elsewhere. It is accepted, at least as a matter of principle, that a search or seizure carried out on a suspect's premises without a warrant is <i>per se</i> unreasonable, unless the police can show that it falls within one of a carefully defined set of exceptions based on the presence of `exigent circumstances.'</p>
<p>.....</p>
<p>"It is clear, then, that the notion that the warrantless entry of a man's house in order to arrest him on probable cause is <i>per se</i> legitimate is in fundamental conflict with the basic principle of Fourth Amendment law that searches and seizures inside a man's house without warrant are <i>per se</i> unreasonable in the absence of some one of a number of well defined `exigent circumstances.'" <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 474-475, 477-478</a></span>.</p>
<p>Although Mr. Justice Harlan joined this portion of the Court's opinion, he expressly disclaimed any position on the issue now before us. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#492" aria-description="Citation for case: Coolidge v. New Hampshire"><i>Id.,</i> at 492</a></span> (concurring opinion).</p>
<p>[26]  As Mr. Justice Harlan wrote for the Court:
</p>
<p>"It is settled doctrine that probable cause for belief that certain articles subject to seizure are in a dwelling cannot of itself justify a search without a warrant. <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>; <i>Taylor</i> v. <i>United States,</i> <span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States">286 U. S. 1, 6</a></span>. The decisions of this Court have time and again underscored the essential purpose of the Fourth Amendment to shield the citizen from unwarranted intrusions into his privacy. See, <i>e. g., </i><i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455</a></span>; cf. <i>Giordenello</i> v. <i>United States,</i> [<span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span>]. This purpose is realized by Rule 41 of the Federal Rules of Criminal Procedure, which implements the Fourth Amendment by requiring that an impartial magistrate determine from an affidavit showing probable cause whether information possessed by law-enforcement officers justifies the issuance of a search warrant. Were federal officers free to search without a warrant merely upon probable cause to believe that certain articles were within a home, the provisions of the Fourth Amendment would become empty phrases, and the protection it affords largely nullified." <i>Jones</i> v. <i>United States,</i> 357 U. S., at 497-498 (footnote omitted).</p>
<p>[27]  See generally Rotenberg &amp; Tanzer, Searching for the Person to be Seized, 35 Ohio St. L. J. 56 (1974).</p>
<p>[28]  See n. 4, <i>supra.</i></p>
<p>[29]  See, <i>e. g.,</i> the facts in Payton's case, n. 5; <i>supra.</i></p>
<p>[30]  "The cases construing the Fourth Amendment thus reflect the ancient common-law rule that a peace officer was permitted to arrest without a warrant for a misdemeanor or felony committed in his presence as well as for a felony not committed in his presence if there was reasonable ground for making the arrest. 10 Halsbury's Laws of England 344-345 (3d ed. 1955); 4 W. Blackstone, Commentaries *292; 1 J. Stephen, A History of the Criminal Law of England 193 (1883); 2 M. Hale, Pleas of the Crown *72-74; Wilgus, Arrests Without a Warrant, <span class="citation no-link">22 Mich. L. Rev. 541</span>, 547-550, 686-688 (1924); <i>Samuel</i> v. <i>Payne,</i> <span class="citation" data-id="6629715"><a href="/opinion/6747612/green-v-graves/" aria-description="Citation for case: Green v. Graves">1 Doug. 359</a></span>, 99 Eng. Rep. 230 (K. B. 1780); <i>Beckwith</i> v. <i>Philby,</i> 6 Barn. &amp; Cress. 635, 108 Eng. Rep. 585 (K. B. 1827)." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#418" aria-description="Citation for case: United States v. Watson">423 U. S., at 418-419</a></span>.</p>
<p>[31]  "The balance struck by the common law in generally authorizing felony arrests on probable cause, but without a warrant, has survived substantially intact. It appears in almost all of the States in the form of express statutory authorization." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#421" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 421-422</a></span>.</p>
<p>[32]  "This is the rule Congress has long directed its principal law enforcement officers to follow. Congress has plainly decided against conditioning warrantless arrest power on proof of exigent circumstances." <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/#423" aria-description="Citation for case: United States v. Watson"><i>Id.,</i> at 423</a></span>.
</p>
<p>The Court added in a footnote:</p>
<p>"Until 1951, <span class="citation no-link">18 U. S. C. § 3052</span> conditioned the warrantless arrest powers of the agents of the Federal Bureau of Investigation on there being reasonable grounds to believe that the person would escape before a warrant could be obtained. The Act of Jan. 10, 1951, c. 1221, § 1, <span class="citation no-link">64 Stat. 1239</span>, eliminated this condition." <i>Id.,</i> at 423, n. 13.</p>
<p>[33]  There are important differences between the common-law rules relating to searches and seizures and those that have evolved through the process of interpreting the Fourth Amendment in light of contemporary norms and conditions. For example, whereas the kinds of property subject to seizure under warrants had been limited to contraband and the fruits or instrumentalities of crime, see <i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/#309" aria-description="Citation for case: Gouled v. United States">255 U. S. 298, 309</a></span>, the category of property that may be seized, consistent with the Fourth Amendment, has been expanded to include mere evidence. <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span>. Also, the prohibitions of the Amendment have been extended to protect against invasion by electronic eavesdropping of an individual's privacy in a phone booth not owned by him, <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, even though the earlier law had focused on the physical invasion of the individual's person or property interests in the course of a seizure of tangible objects. See <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#466" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 466</a></span>. Thus, this Court has not simply frozen into constitutional law those law enforcement practices that existed at the time of the Fourth Amendment's passage.</p>
<p>[34]  The issue is not whether a defendant must stand trial, because he must do so even if the arrest is illegal. See <i>United States</i> v. <i>Crews, ante,</i> at 474.</p>
<p>[35]  Those modern commentators who have carefully studied the early works agree with that assessment. See ALI, A Model Code of Pre-Arraignment Procedure 308 (Prop. Off. Draft 1975) (hereinafter ALI Code); Blakey, The Rule of Announcement and Unlawful Entry: <i>Miller</i> v. <i>United States</i> and <i>Ker</i> v. <i><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">California</a></span></i><i>,</i> <span class="citation no-link">112 U. Pa. L. Rev. 499</span>, 502 (1964); Comment, Forcible Entry to Effect a Warrantless Arrestâ  The Eroding Protection of the Castle, <span class="citation no-link">82 Dick. L. Rev. 167</span>, 168, n. 5 (1977); Note, The Constitutionality of Warrantless Home Arrests, <span class="citation no-link">78 Colum. L. Rev. 1550</span>, 1553 (1978) ("the major common-law commentators appear to be equally divided on the requirement of a warrant for a home arrest") (hereinafter Columbia Note); Recent Development, Warrantless Arrests by Police Survive a Constitutional Challengeâ  <i>United States</i> v. <i><span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">Watson</a></span></i><i>,</i> <span class="citation no-link">14 Am. Crim. L. Rev. 193</span>, 210-211 (1976). Accord, <i>Miller</i> v. <i>United States,</i> <span class="citation" data-id="9421667"><a href="/opinion/105731/miller-v-united-states/#307" aria-description="Citation for case: Miller v. United States">357 U. S. 301, 307-308</a></span>; <i>Accarino</i> v. <i>United States,</i> 85 U. S. App. D. C. 394, 402, <span class="citation" data-id="224194"><a href="/opinion/224194/accarino-v-united-states/#464" aria-description="Citation for case: Accarino v. United States">179 F. 2d 456, 464</a></span> (1949).</p>
<p>[36]  "Foremost among the titles to be found in private libraries of the time were the works of Coke, the great expounder of Magna Carta, and similar books on English liberties. The inventory of the library of Arthur Spicer, who died in Richmond County, Virginia, in 1699, included Coke's <i>Institutes,</i> another work on Magna Carta, and a "Table to Cooks Reports.' The library of Colonel Daniel McCarty, a wealthy planter and member of the Virginia House of Burgesses who died in Westmoreland County in 1724, included Coke's <i>Reports,</i> an abridgment of Coke's <i>Reports, Coke on Littleton,</i> and `Rights of the Comons of England.' Captain Charles Colston, who died in Richmond County, Vi

[...TRUNCATED 24323 of 144323 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
