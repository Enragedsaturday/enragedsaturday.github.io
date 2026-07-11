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

## GROUP: content/cases/Davis v. Mississippi.md  (`case`, 6 assertions)

### content_page

```
---
title: "Davis v. Mississippi"
type: case
citation: "394 U.S. 721 (1969)"
parallel_cite: "89 S. Ct. 1394; 22 L. Ed. 2d 676"
neutral_cite: 1969 U.S. LEXIS 1869
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-04-23
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-04-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Davis v. Mississippi
  varies_by_point: false
  scope_note: "Good law; dragnet station-house detention for fingerprinting without probable cause or judicial authorization is unreasonable. The Court reserved whether a narrowly circumscribed fingerprinting procedure on less than probable cause might be permissible — a question revisited in Hayes v. Florida."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107912/davis-v-mississippi/"
  cluster_id: 107912
  opinion_id: 107912
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Limiting"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Hayes v. Florida]]", "[[Terry v. Ohio]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "fingerprinting", "investigative-detention", "dragnet"]
holding: "Detaining and transporting a suspect to the station for fingerprinting without probable cause or judicial authorization is an unreasonable seizure; the fingerprints are suppressible."
lake:
  record_id: Davis v. Mississippi
  status: verified
  projected_at: 2026-07-09
---

# Davis v. Mississippi

*394 U.S. 721 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a rape in which the only leads were the victim's general description and a set of fingerprints, police rounded up and questioned at least two dozen young Black men, taking many to headquarters for fingerprinting without warrants or probable cause. Davis was among those detained; his prints, taken during a station-house detention, matched those at the scene and were used to convict him. He moved to suppress the fingerprint evidence as the fruit of an unlawful detention.

## Issue
Whether fingerprints obtained during an investigative detention undertaken without probable cause or judicial authorization must be excluded as the product of an unreasonable Fourth Amendment seizure.

## Rule
Investigative seizures are subject to the Fourth Amendment regardless of the label: "Nothing is more clear than that the Fourth Amendment was meant to prevent wholesale intrusions upon the personal security of our citizenry, whether these intrusions be termed 'arrests' or 'investigatory detentions.'" — 394 U.S. at 726–727. ^pin-726

That protection reaches detentions for fingerprinting: "Detentions for the sole purpose of obtaining fingerprints are no less subject to the constraints of the Fourth Amendment." — [*Id.* at 727](https://www.courtlistener.com/opinion/107912/davis-v-mississippi/#:~:text=Detentions%20for%20the%20sole%20purpose). ^pin-727

## Application
Davis was seized in a dragnet — taken to police headquarters and fingerprinted without probable cause to arrest, without a warrant, and without any judicial authorization for the detention. Because that station-house detention was an unreasonable seizure, the fingerprints obtained during it were its fruit and had to be suppressed. The Court added a caveat: because fingerprinting is a brief, reliable, non-coercive process, a narrowly circumscribed procedure conducted under judicial authorization might in some future case satisfy the Fourth Amendment even on less than probable cause — but no such procedure was used here.

## Conclusion
The dragnet fingerprinting detention was unreasonable and the fingerprints were inadmissible; the conviction was reversed. *Davis* establishes that investigatory detentions, including for fingerprinting, are full Fourth Amendment seizures requiring justification.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Reaffirmed and extended in [[Hayes v. Florida]] (transporting a suspect to the station for fingerprinting without probable cause is an arrest), which also developed the reserved question of brief field fingerprinting on reasonable suspicion; consistent with the seizure framework of [[Terry v. Ohio]].

## Appears on
- [[Seizure of the Person]] — *Limiting*
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Davis v. Mississippi*, 394 U.S. 721 (1969) — https://www.courtlistener.com/opinion/107912/davis-v-mississippi/ — pinpoints: 726–727.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e08510608eb4ee42", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "394 U.S. 721 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 1869", "official_citation_present": true, "parallel_cite": "89 S. Ct. 1394; 22 L. Ed. 2d 676", "title": "Davis v. Mississippi", "year": "1969"}}
{"assertion_id": "174c59ecec90180a", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "Davis v. Mississippi"}}
{"assertion_id": "a6689722cb8c331a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Detaining and transporting a suspect to the station for fingerprinting without probable cause or judicial authorization is an unreasonable seizure; the fingerprints are suppressible.", "title": "Davis v. Mississippi"}}
{"assertion_id": "aeb3c2c5e0cb2b3d", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Limiting", "title": "Davis v. Mississippi"}}
{"assertion_id": "0ab74d414ce3c7f5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Davis v. Mississippi"}}
{"assertion_id": "2707db32688be755", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-04-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Davis v. Mississippi", "field_i_validity": "good_law", "scope_note": "Good law; dragnet station-house detention for fingerprinting without probable cause or judicial authorization is unreasonable. The Court reserved whether a narrowly circumscribed fingerprinting procedure on less than probable cause might be permissible — a question revisited in Hayes v. Florida.", "title": "Davis v. Mississippi", "varies_by_point": "false"}}
```

### lake record — Davis v. Mississippi

```json
{
  "schema_version": "s2.v1",
  "record_id": "Davis v. Mississippi",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Davis v. Mississippi",
    "case_name_short": "Davis",
    "case_name_full": "Davis v. Mississippi",
    "input_case_name": "Davis v. Mississippi",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-04-23",
    "year": 1969,
    "docket": null,
    "cluster_id": 107912,
    "lead_opinion_id": 107912,
    "sibling_ids": [
      107912,
      9424010,
      9424011,
      9424012,
      9424013
    ],
    "absolute_url": "/opinion/107912/davis-v-mississippi/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8975607,
        "score": 20,
        "case_name": "Davis v. Mississippi"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "394 U.S. 721",
      "volume": "394",
      "reporter": "U.S.",
      "page": "721",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 1394",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 676",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "676",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 1869",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1869",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "394 U.S. 721",
        "volume": "394",
        "reporter": "U.S.",
        "page": "721",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 1394",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "1394",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "22 L. Ed. 2d 676",
        "volume": "22",
        "reporter": "L. Ed. 2d",
        "page": "676",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 1869",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1869",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "394 U.S. 721",
    "official_selection": {
      "court_class": "scotus",
      "selected": "394 U.S. 721",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-726",
      "page": null,
      "quote": "--- # Davis v. Mississippi *394 U.S. 721 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a rape in which the only leads were the victim's general description and a set of fingerprints, police rounded up and questioned at least two dozen young Black men, taking many to headquarters for fingerprinting without warrants or probable cause. Davis was among those detained; his prints, taken during a station-house detention, matched those at the scene and were used to convict him. He moved to suppress the fingerprint evidence as the fruit of an unlawful detention. ## Issue Whether fingerprints obtained during an investigative detention undertaken without probable cause or judicial authorization must be excluded as the product of an unreasonable Fourth Amendment seizure. ## Rule Investigative seizures are subject to the Fourth Amendment regardless of the label:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-727",
      "page": null,
      "quote": "Detentions for the sole purpose of obtaining fingerprints are no less subject to the constraints of the Fourth Amendment.",
      "star_marker": "727",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10565,
      "fragment": "#:~:text=Detentions%20for%20the%20sole%20purpose",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-04-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Davis v. Mississippi",
    "varies_by_point": false,
    "scope_note": "Good law; dragnet station-house detention for fingerprinting without probable cause or judicial authorization is unreasonable. The Court reserved whether a narrowly circumscribed fingerprinting procedure on less than probable cause might be permissible \u2014 a question revisited in Hayes v. Florida.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Southerland v. City of New York",
          "cluster_id": 8441115,
          "cite": [
            "667 F.3d 87",
            "2012 WL 310836",
            "2011 U.S. App. LEXIS 26144"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opinion Number",
          "cluster_id": 3463196,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cerrone v. Brown",
          "cluster_id": 7090171,
          "cite": [
            "246 F.3d 194",
            "2001 WL 356717"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guardiola v. State",
          "cluster_id": 1383318,
          "cite": [
            "20 S.W.3d 216",
            "2000 WL 552189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Firth",
          "cluster_id": 1997671,
          "cite": [
            "708 A.2d 526",
            "1998 R.I. LEXIS 53",
            "1998 WL 97794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Donald Johnson v. Bart Ross, Superintendent, Arthur Kill Correctional Facility",
          "cluster_id": 577020,
          "cite": [
            "955 F.2d 178",
            "1992 U.S. App. LEXIS 1068"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Boyle v. State",
          "cluster_id": 1522051,
          "cite": [
            "820 S.W.2d 122",
            "1989 WL 114545"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane1_negative"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Illinois",
          "cluster_id": 109304,
          "cite": [
            "45 L. Ed. 2d 416",
            "95 S. Ct. 2254",
            "422 U.S. 590",
            "1975 U.S. LEXIS 82"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Browder v. Director, Dept. of Corrections of Ill.",
          "cluster_id": 109761,
          "cite": [
            "54 L. Ed. 2d 521",
            "98 S. Ct. 556",
            "434 U.S. 257",
            "1978 U.S. LEXIS 53"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kolender v. Lawson",
          "cluster_id": 110926,
          "cite": [
            "75 L. Ed. 2d 903",
            "103 S. Ct. 1855",
            "461 U.S. 352",
            "1983 U.S. LEXIS 159",
            "51 U.S.L.W. 4532"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dionisio",
          "cluster_id": 108709,
          "cite": [
            "35 L. Ed. 2d 67",
            "93 S. Ct. 764",
            "410 U.S. 1",
            "1973 U.S. LEXIS 110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cantor",
          "cluster_id": 5681132,
          "cite": [
            "36 N.Y.2d 106",
            "324 N.E.2d 872",
            "365 N.Y.S.2d 509",
            "1975 N.Y. LEXIS 3100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Davis v. Mississippi:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NTM4NzUyMDAwMDAmcz0xNzY3NTQ4JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107912+OR+9424010+OR+9424011+OR+9424012+OR+9424013%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 7,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNDImcz0zOTkzMDkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107912+OR+9424010+OR+9424011+OR+9424012+OR+9424013%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107912 OR 9424010 OR 9424011 OR 9424012 OR 9424013)",
    "indexed_citing_opinions": 898,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107912,
        "count": 852,
        "count_source": "search"
      },
      {
        "opinion_id": 9424010,
        "count": 69,
        "count_source": "search"
      },
      {
        "opinion_id": 9424011,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424012,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9424013,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1385,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/davis-v-mississippi.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU3OTcwOTUmcz00NDgyOTUzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107912+OR+9424010+OR+9424011+OR+9424012+OR+9424013%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107912,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 107848,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 246966,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 250068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107912,
        "cited_id": 1722004,
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
    "date_created": "2026-07-05T02:04:14Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:15:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Davis v. Mississippi

```
<div>
<center><b><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U.S. 721</a></span> (1969)</b></center>
<center><h1>DAVIS<br>
v.<br>
MISSISSIPPI.</h1></center>
<center>No. 645.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 26-27, 1969.</center>
<center>Decided April 22, 1969.</center>
CERTIORARI TO THE SUPREME COURT OF MISSISSIPPI.
<p><i>Melvyn Zarr</i> argued the cause for petitioner. With him on the brief were <i>Jack Greenberg, Michael Meltsner, Anthony G. Amsterdam,</i> and <i>Jack Young.</i></p>
<p><span class="star-pagination">*722</span> <i>G. Garland Lyell, Jr.,</i> Assistant Attorney General of Mississippi, argued the cause for respondent. With him on the brief was <i>Joe T. Patterson,</i> Attorney General.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>Petitioner was convicted of rape and sentenced to life imprisonment by a jury in the Circuit Court of Lauderdale County, Mississippi. The only issue before us is whether fingerprints obtained from petitioner should have been excluded from evidence as the product of a detention which was illegal under the Fourth and Fourteenth Amendments.</p>
<p>The rape occurred on the evening of December 2, 1965, at the victim's home in Meridian, Mississippi. The victim could give no better description of her assailant than that he was a Negro youth. Finger and palm prints found on the sill and borders of the window through which the assailant apparently entered the victim's home constituted the only other lead available at the outset of the police investigation. Beginning on December 3, and for a period of about 10 days, the Meridian police, without warrants, took at least 24 Negro youths to police headquarters where they were questioned briefly, fingerprinted, and then released without charge. The police also interrogated 40 or 50 other Negro youths either at police headquarters, at school, or on the street. Petitioner, a 14-year-old youth who had occasionally worked for the victim as a yardboy, was brought in on December 3 and released after being fingerprinted and routinely questioned. Between December 3 and December 7, he was interrogated by the police on several occasions sometimes in his home or in a car, other times at police headquarters. This questioning apparently related primarily to investigation of other potential suspects. Several times during this same period petitioner was exhibited <span class="star-pagination">*723</span> to the victim in her hospital room. A police officer testified that these confrontations were for the purpose of sharpening the victim's description of her assailant by providing "a gauge to go by on size and color." The victim did not identify petitioner as her assailant at any of these confrontations.</p>
<p>On December 12, the police drove petitioner 90 miles to the city of Jackson and confined him overnight in the Jackson jail. The State conceded on oral argument in this Court that there was neither a warrant nor probable cause for this arrest. The next day, petitioner, who had not yet been afforded counsel, took a lie detector test and signed a statement.<sup>[1]</sup> He was then returned to and confined in the Meridian jail. On December 14, while so confined, petitioner was fingerprinted a second time. That same day, these December 14 prints, together with the fingerprints of 23 other Negro youths apparently still under suspicion, were sent to the Federal Bureau of Investigation in Washington, D. C., for comparison with the latent prints taken from the window of the victim's house. The FBI reported that petitioner's prints matched those taken from the window. Petitioner was subsequently indicted and tried for the rape, and the fingerprint evidence was admitted in evidence at trial over petitioner's timely objections that the fingerprints should be excluded as the product of an unlawful detention. The Mississippi Supreme Court sustained the admission of the fingerprint evidence and affirmed the conviction. <span class="citation multiple-matches"><a href="/c/So.%202d/204/270/">204 So. 2d 270</a></span> (1967). We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./393/821/">393 U. S. 821</a></span> (1968). We reverse.</p>
<p>At the outset, we find no merit in the suggestion in the Mississippi Supreme Court's opinion that fingerprint evidence, because of its trustworthiness, is not subject to the proscriptions of the Fourth and Fourteenth <span class="star-pagination">*724</span> Amendments.<sup>[2]</sup> Our decisions recognize no exception to the rule that illegally seized evidence is inadmissible at trial, however relevant and trustworthy the seized evidence may be as an item of proof. The exclusionary rule was fashioned as a sanction to redress and deter overreaching governmental conduct prohibited by the Fourth Amendment. To make an exception for illegally seized evidence which is trustworthy would fatally undermine these purposes. Thus, in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span> (1961), we held that "<i>all</i> evidence obtained by searches and seizures in violation of the Constitution is, by that same authority, inadmissible in a state court." (Italics supplied.) Fingerprint evidence is no exception to this comprehensive rule. We agree with and adopt the conclusion of the Court of Appeals for the District of Columbia Circuit in <i>Bynum</i> v. <i>United States,</i> 104 U. S. App. D. C. 368, 370, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#467" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465, 467</a></span> (1958):</p>
<blockquote>"True, fingerprints can be distinguished from statements given during detention. They can also be distinguished from articles taken from a prisoner's possession. Both similarities and differences of each type of evidence to and from the others are apparent. But all three have the decisive common characteristic of being something of evidentiary value which the public authorities have caused an arrested person to yield to them during illegal detention. If one such product of illegal detention is proscribed, by the same token all should be proscribed."</blockquote>
<p>We turn then to the question whether the detention of petitioner during which the fingerprints used at trial were taken constituted an unreasonable seizure of his <span class="star-pagination">*725</span> person in violation of the Fourth Amendment. The opinion of the Mississippi Supreme Court proceeded on the mistaken premise that petitioner's prints introduced at trial were taken during his brief detention on December 3. In fact, as both parties before us agree, the fingerprint evidence used at trial was obtained on December 14, while petitioner was still in detention following his December 12 arrest. The legality of his arrest was not determined by the Mississippi Supreme Court. However, on oral argument here, the State conceded that the arrest on December 12 and the ensuing detention through December 14 were based on neither a warrant nor probable cause and were therefore constitutionally invalid. The State argues, nevertheless, that this invalidity should not prevent us from affirming petitioner's conviction. The December 3 prints were validly obtained, it is argued, and "it should make no difference in the practical or legal sense which [fingerprint] card was sent to the F. B. I. for comparison."<sup>[3]</sup> It may be that it does make a difference in light of the objectives of the exclusionary rule, see <i>Bynum</i> v. <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#371" aria-description="Citation for case: Clayborne Bynum v. United States"><i>United States, supra,</i> at 371-372</a></span>, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#468" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d, at 468-469</a></span>,<sup>[4]</sup> but we need not decide the question since we have concluded that the prints of December 3 were not validly obtained.</p>
<p><span class="star-pagination">*726</span> The State makes no claim that petitioner voluntarily accompanied the police officers to headquarters on December 3 and willingly submitted to fingerprinting. The State's brief also candidly admits that "[a]ll that the Meridian Police could possibly have known about petitioner at the time . . . would not amount to probable cause for his arrest . . . ."<sup>[5]</sup> The State argues, however, that the December 3 detention was of a type which does not require probable cause. Two rationales for this position are suggested. First, it is argued that the detention occurred during the investigatory rather than accusatory stage and thus was not a seizure requiring probable cause. The second and related argument is that, at the least, detention for the sole purpose of obtaining fingerprints does not require probable cause.</p>
<p>It is true that at the time of the December 3 detention the police had no intention of charging petitioner with the crime and were far from making him the primary focus of their investigation. But to argue that the Fourth Amendment does not apply to the investigatory stage is fundamentally to misconceive the purposes of the Fourth Amendment. Investigatory seizures would subject unlimited numbers of innocent persons to the harassment and ignominy incident to involuntary detention. Nothing is more clear than that the Fourth Amendment was meant to prevent wholesale intrusions upon the personal security of our citizenry, whether these intrusions <span class="star-pagination">*727</span> be termed "arrests" or "investigatory detentions."<sup>[6]</sup> We made this explicit only last Term in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 19</a></span> (1968), when we rejected "the notions that the Fourth Amendment does not come into play at all as a limitation upon police conduct if the officers stop short of something called a `technical arrest' or a `full-blown search.' "</p>
<p>Detentions for the sole purpose of obtaining fingerprints are no less subject to the constraints of the Fourth Amendment. It is arguable, however, that, because of the unique nature of the fingerprinting process, such detentions might, under narrowly defined circumstances, be found to comply with the Fourth Amendment even though there is no probable cause in the traditional sense. See <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967). Detention for fingerprinting may constitute a much less serious intrusion upon personal security than other types of police searches and detentions. Fingerprinting involves none of the probing into an individual's private life and thoughts that marks an interrogation or search. Nor can fingerprint detention be employed repeatedly to harass any individual, since the police need only one set of each person's prints. Furthermore, fingerprinting is an inherently more reliable and effective crime-solving tool than eyewitness identifications or confessions and is not subject to such abuses as the improper line-up and the "third degree." Finally, because there is no danger of destruction of fingerprints, the limited detention need not come unexpectedly or at an inconvenient time. <span class="star-pagination">*728</span> For this same reason, the general requirement that the authorization of a judicial officer be obtained in advance of detention would seem not to admit of any exception in the fingerprinting context.</p>
<p>We have no occasion in this case, however, to determine whether the requirements of the Fourth Amendment could be met by narrowly circumscribed procedures for obtaining, during the course of a criminal investigation, the fingerprints of individuals for whom there is no probable cause to arrest. For it is clear that no attempt was made here to employ procedures which might comply with the requirements of the Fourth Amendment: the detention at police headquarters of petitioner and the other young Negroes was not authorized by a judicial officer; petitioner was unnecessarily required to undergo two fingerprinting sessions; and petitioner was not merely fingerprinted during the December 3 detention but also subjected to interrogation. The judgment of the Mississippi Supreme Court is therefore</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE FORTAS took no part in the consideration or decision of this case.</p>
<p>MR. JUSTICE HARLAN, concurring.</p>
<p>I join the opinion of the Court, with one reservation. The Court states in dictum that, because fingerprinting may be scheduled for a time convenient to the citizen, "the general requirement that the authorization of a judicial officer be obtained in advance of detention would seem not to admit of any exception in the fingerprinting context." <i>Ante,</i> this page. I cannot concur in so sweeping a proposition. There may be circumstances, falling short of the "dragnet" procedures employed in this case, where compelled submission to fingerprinting would not amount to a violation of the Fourth Amendment even in the <span class="star-pagination">*729</span> absence of a warrant, and I would leave that question open.</p>
<p>MR. JUSTICE BLACK, dissenting.</p>
<p>The petitioner here was convicted of a brutal rape of a woman, committed in her own home. Fingerprints of the petitioner, left on the window sill of her home, were the clinching evidence bringing about petitioner's conviction. The Court, by once more expanding the reach of the judicially declared exclusionary rule, ostensibly resting on the Fourth Amendment, holds the fingerprint evidence constitutionally inadmissible and thereby reverses petitioner's conviction. The rape occurred on December 2, 1965, and, as was their duty, the police authorities began to make a searching investigation the morning of December 3. The raped woman was originally able to describe the rapist only as a young Negro male. With this evidence the police proceeded to interrogate a number of young Negroes on the streets, at their homes, or at the police station, and then permitted them to go on their way. The petitioner was among those so interrogated on December 3, at which time his fingerprints were made. The fingerprints were again taken on December 14. The record does not show that petitioner or any other young man who was questioned and fingerprinted ever made the slightest objection. Apparently all of them cooperated with the police in efforts to find out who had committed the rape. This case is but one more in an ever-expanding list of cases in which this Court has been so widely blowing up the Fourth Amendment's scope that its original authors would be hard put to recognize their creation.<sup>[*]</sup> For this most <span class="star-pagination">*730</span> unnecessary expansion of the Amendment, the Court is compelled to put its chief reliance on a Court of Appeals decision, <i>Bynum</i> v. <i>United States,</i> 104 U. S. App. D. C. 368, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d 465</a></span>. I think it is high time this Court, in the interest of the administration of criminal justice, made a new appraisal of the language and history of the Fourth Amendment and cut it down to its intended size. Such a judicial action would, I believe, make our cities a safer place for men, women, and children to live.</p>
<p>I dissent from this reversal.</p>
<p>MR. JUSTICE STEWART, dissenting.</p>
<p>I do not disagree with the Court's conclusion that the petitioner was arrested and detained without probable cause. But it does not follow that his fingerprints were inadmissible at the trial.</p>
<p>Fingerprints are not "evidence" in the conventional sense that weapons or stolen goods might be. Like the color of a man's eyes, his height, or his very physiognomy, the tips of his fingers are an inherent and unchanging characteristic of the man. And physical impressions of his fingertips can be exactly and endlessly reproduced.</p>
<p>We do not deal here with a confession wrongfully obtained or with property wrongfully seizedso tainted as to be forever inadmissible as evidence against a defendant. We deal, instead, with "evidence" that can be identically reproduced and lawfully used at any subsequent trial.<sup>[*]</sup></p>
<p>I cannot believe that the doctrine of <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, requires so useless a gesture as the reversal of this conviction.</p>
<h2>NOTES</h2>
<p>[1]  The statement was not introduced at the trial.</p>
<p>[2]  Fingerprint evidence would seem no more "trustworthy" than other types of evidencesuch as guns, narcotics, gambling equipment which are routinely excluded if illegally obtained.</p>
<p>[3]  Brief for Respondent 8.</p>
<p>[4]  The Government argued in <i><span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">Bynum</a></span></i> that the controversy over the introduction in evidence of a particular set of fingerprints was "much ado over very little," because another set properly taken was available and might have been used. The Court of Appeals rejected this argument: "It bears repeating that the matter of primary judicial concern in all cases of this type is the imposition of effective sanctions implementing the Fourth Amendment guarantee against illegal arrest and detention. Neither the fact that the evidence obtained through such detention is itself trustworthy or the fact that equivalent evidence can conveniently be obtained in a wholly proper way militates against this overriding consideration. It is entirely irrelevant that it may be relatively easy for the government to prove guilt without using the product of illegal detention. The important thing is that those administering the criminal law understand that they must do it that way." 104 U. S. App. D. C., at 371-372, <span class="citation" data-id="246966"><a href="/opinion/246966/clayborne-bynum-v-united-states/#468" aria-description="Citation for case: Clayborne Bynum v. United States">262 F. 2d, at 468-469</a></span>. On Bynum's retrial another set of fingerprints in no way connected with his unlawful arrest was used, and he was again convicted. The Court of Appeals affirmed this conviction. 107 U. S. App. D. C. 109, <span class="citation" data-id="250068"><a href="/opinion/250068/clayborne-bynum-v-united-states/" aria-description="Citation for case: Clayborne Bynum v. United States">274 F. 2d 767</a></span> (1960).</p>
<p>[5]  Brief for Respondent 3.</p>
<p>[6]  The State relies on various statements in our cases which approve general questioning of citizens in the course of investigating a crime. See <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#477" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 477-478</a></span> (1966); <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#635" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 635</a></span> (concurring opinion) (1961). But these statements merely reiterated the settled principle that while the police have the right to request citizens to answer voluntarily questions concerning unsolved crimes they have no right to compel them to answer.</p>
<p>[*]  See, <i>e. g., </i><i>Bumper</i> v. <i>North Carolina,</i> 391 U. S. 543another rape case; <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span>; <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span>; <i>Recznik</i> v. <i>City of Lorain,</i> <span class="citation" data-id="9423850"><a href="/opinion/107800/recznik-v-city-of-lorain/" aria-description="Citation for case: Recznik v. City of Lorain">393 U. S. 166</a></span>; and <i>Griswold</i> v. <i>Connecticut,</i> <span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span>.</p>
<p>[*]  At the original trial the victim of the rape, under oath, positively identified the petitioner as her assailant. There now exists, therefore, ample probable cause to detain him and take his fingerprints.</p>

</div>
```

---

## GROUP: content/cases/Davis v. United States (2011).md  (`case`, 5 assertions)

### content_page

```
---
title: "Davis v. United States (2011)"
type: case
citation: "564 U.S. 229 (2011)"
parallel_cite: "131 S. Ct. 2419; 180 L. Ed. 2d 285"
neutral_cite: 2011 U.S. LEXIS 4560
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2011
date_decided: 2011-06-16
docket: 09-11328
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2011-06-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: "Davis v. United States (2011)"
  varies_by_point: false
  scope_note: Extends the Leon good-faith line to objectively reasonable reliance on binding appellate precedent later overruled. Good law.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/218926/davis-v-united-states/"
  cluster_id: 218926
  opinion_id: 9441776
  identity_checked: true
homes:
  - page: "[[The Good-Faith Exception]]"
    role: "Key — Progeny (good faith)"
related: ["[[United States v. Leon]]", "[[Herring v. United States]]", "[[Illinois v. Krull]]", "[[Arizona v. Gant]]", "[[New York v. Belton]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "good-faith", "automobile", "search-incident-to-arrest"]
holding: "The exclusionary rule does not apply to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is only later overruled, because there is no culpable police misconduct to deter."
lake:
  record_id: "Davis v. United States (2011)"
  status: under_review
  projected_at: 2026-07-09
---

# Davis v. United States (2011)

*564 U.S. 229 (2011)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above; this is the 2011 good-faith case — distinct from the 1994 Miranda-invocation [[Davis v. United States]] -->

## Background
During an Alabama traffic stop, Davis, a passenger, gave a false name, was arrested for that, handcuffed, and placed in a patrol car. Officers then searched the passenger compartment incident to the arrest under then-binding Eleventh Circuit precedent (which read [[New York v. Belton]] to authorize the search) and found a revolver in his jacket. He was convicted of being a felon in possession. While his appeal was pending, [[Arizona v. Gant]] was decided, which made the search unconstitutional. The Eleventh Circuit agreed the search violated *[[Arizona v. Gant|Gant]]* but declined to suppress.

## Issue
Whether the exclusionary rule applies to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is later overruled.

## Rule
No. The exclusionary rule is a deterrent sanction, and it is unjustified where the police are not culpable. "Because suppression would do nothing to deter police misconduct in these circumstances, and because it would come at a high cost to both the truth and the public safety, we hold that searches conducted in objectively reasonable reliance on binding appellate precedent are not subject to the exclusionary rule." — 564 U.S. at 232. ^pin-232

## Application
The officers searched Davis's car in strict compliance with the Eleventh Circuit precedent that governed at the time; they "act[ed] as a reasonable officer would and should act." Their conduct was not deliberate, reckless, or grossly negligent — the culpability that alone makes exclusion worth its costs under the *[[United States v. Leon|Leon]]* / *[[Herring v. United States|Herring]]* line. Suppressing the revolver would deter no misconduct and would only penalize an officer for following the law, while exacting the high social cost of releasing a felon caught with a firearm. That *[[Arizona v. Gant|Gant]]* later changed the rule did not retroactively make the officers' reliance unreasonable.

## Conclusion
"We therefore hold that when the police conduct a search in objectively reasonable reliance on binding appellate precedent, the exclusionary rule does not apply." — *Id.* at 249–250. ^pin-249

The Eleventh Circuit's refusal to suppress was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Davis* extends the [[The Good-Faith Exception|good-faith exception]] of [[United States v. Leon]], [[Illinois v. Krull]], and [[Herring v. United States]] to reliance on binding appellate precedent, applying it to a search valid under [[New York v. Belton]] but unlawful after [[Arizona v. Gant]].
- **Disambiguation:** this is the **2011 good-faith** decision; the bare wikilink [[Davis v. United States]] resolves to the distinct **1994** Miranda ambiguous-invocation case.

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny (good faith)*

## Sources
- *Davis v. United States*, 564 U.S. 229 (2011) — https://www.courtlistener.com/opinion/218926/davis-v-united-states/ — pinpoints: 232, 249–250.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "681a244c71394b02", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "565 U.S. 1100 (2011)", "court": "U.S. Supreme Court", "neutral_cite": "2011 U.S. LEXIS 8943", "official_citation_present": true, "parallel_cite": "181 L. Ed. 2d 563; 132 S. Ct. 864; 80 U.S.L.W. 3555", "title": "Davis v. United States (2011)", "year": "2011"}}
{"assertion_id": "f36d60f8e9073511", "dimension": "support", "kind": "home_role", "locator": {"home": "The Good-Faith Exception"}, "payload": {"home": "The Good-Faith Exception", "role": "Key — Progeny (good faith)", "title": "Davis v. United States (2011)"}}
{"assertion_id": "f8b781c910b43cb9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The exclusionary rule does not apply to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is only later overruled, because there is no culpable police misconduct to deter.", "title": "Davis v. United States (2011)"}}
{"assertion_id": "1609c4df932beb61", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2011-06-16", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Davis v. United States (2011)", "field_i_validity": "good_law", "scope_note": "Extends the Leon good-faith line to objectively reasonable reliance on binding appellate precedent later overruled. Good law.", "title": "Davis v. United States (2011)", "varies_by_point": "false"}}
{"assertion_id": "fdb6c43f03cc8d76", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Davis v. United States (2011)"}}
```

### lake record — Davis v. United States (2011)

```json
{
  "schema_version": "s2.v1",
  "record_id": "Davis v. United States (2011)",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Davis v. United States",
    "case_name_short": "Davis",
    "case_name_full": "Tyrone Roswell Davis v. United States",
    "input_case_name": "Davis v. United States (2011)",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2011-06-16",
    "year": 2011,
    "docket": "09-11328",
    "cluster_id": 218926,
    "lead_opinion_id": 9441776,
    "sibling_ids": [
      218926,
      9441776,
      9441777,
      9441778
    ],
    "absolute_url": "/opinion/218926/davis-v-united-states/",
    "identity_method": "panel-cluster-rekey",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 7350071,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 7349256,
        "score": 20,
        "case_name": "Davis v. United States"
      }
    ],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "564 U.S. 229",
      "volume": "564",
      "reporter": "U.S.",
      "page": "229",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "131 S. Ct. 2419",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "180 L. Ed. 2d 285",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2011 U.S. LEXIS 4560",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4560",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "131 S. Ct. 2419",
        "volume": "131",
        "reporter": "S. Ct.",
        "page": "2419",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "180 L. Ed. 2d 285",
        "volume": "180",
        "reporter": "L. Ed. 2d",
        "page": "285",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "564 U.S. 229",
        "volume": "564",
        "reporter": "U.S.",
        "page": "229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2011 U.S. LEXIS 4560",
        "volume": "2011",
        "reporter": "U.S. LEXIS",
        "page": "4560",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "564 U.S. 229",
    "official_selection": {
      "court_class": "scotus",
      "selected": "564 U.S. 229",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-232",
      "page": null,
      "quote": "--- # Davis v. United States (2011) *564 U.S. 229 (2011)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above; this is the 2011 good-faith case \u2014 distinct from the 1994 Miranda-invocation [[Davis v. United States]] --> ## Background During an Alabama traffic stop, Davis, a passenger, gave a false name, was arrested for that, handcuffed, and placed in a patrol car. Officers then searched the passenger compartment incident to the arrest under then-binding Eleventh Circuit precedent (which read [[New York v. Belton]] to authorize the search) and found a revolver in his jacket. He was convicted of being a felon in possession. While his appeal was pending, [[Arizona v. Gant]] was decided, which made the search unconstitutional. The Eleventh Circuit agreed the search violated *Gant* but declined to suppress. ## Issue Whether the exclusionary rule applies to evidence obtained during a search conducted in objectively reasonable reliance on binding appellate precedent that is later overruled. ## Rule No. The exclusionary rule is a deterrent sanction, and it is unjustified where the police are not culpable.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-249",
      "page": null,
      "quote": "Their conduct was not deliberate, reckless, or grossly negligent \u2014 the culpability that alone makes exclusion worth its costs under the *Leon* / *Herring* line. Suppressing the revolver would deter no misconduct and would only penalize an officer for following the law, while exacting the high social cost of releasing a felon caught with a firearm. That *Gant* later changed the rule did not retroactively make the officers' reliance unreasonable. ## Conclusion",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2011-06-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Davis v. United States (2011)",
    "varies_by_point": false,
    "scope_note": "Extends the Leon good-faith line to objectively reasonable reliance on binding appellate precedent later overruled. Good law.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7268220) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
      },
      "lane2_top_cited": {
        "query": "cites:(7268220)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(7268220)",
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
    "complete_query": "cites:(7268220)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7268220,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/davis-v-united-states-2011.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T02:15:41Z",
    "date_modified": "2026-07-09T23:22:57Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law",
      "panel cluster re-key -> cluster 218926 (evidence: S9 F-S9-DN-003; _run/s9/rekey-targets.jsonl 2026-07-09; stub cluster 7350241 -> merits 218926 (Davis v. United States, 564 U.S. 229, 2011); L.Ed.2d dup 7345713 noted)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:16:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:16:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:18:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:16:23Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Davis v. United States (2011)

```
<opinion type="majority">
<author id="b275-7">Justice Alito</author>
<p id="AG6">delivered the opinion of the Court.</p>
<p id="b275-8">The Fourth Amendment protects the right, to be free from “unreasonable searches and seizures,” but it is silent about how this right is to be enforced. To supplement the bare text, this Court created the exclusionary rule, a deterrent <page-number citation-index="1" label="232">*232</page-number>sanction that bars the prosecution from introducing evidence obtained by way of a Fourth Amendment violation. The question here is whether to apply this sanction when the police conduct a search in compliance with binding precedent that is later overruled. Because suppression would do nothing to deter police misconduct in these circumstances, and because it would come at a high cost to both the truth and the public safety, we hold that searches conducted in objectively reasonable reliance on binding appellate precedent are not subject to the exclusionary rule.</p>
<p id="b276-9">&gt; — Í</p>
<p id="b276-3">The question presented arises in this case as a result of a shift in our Fourth Amendment jurisprudence on searches of automobiles incident to arrests of recent occupants.</p>
<p id="b276-4">A</p>
<p id="b276-5">Under this Court’s decision in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), a police officer who makes a lawful arrest may conduct a warrantless search of the arrestee’s person and the area “within his immediate control.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Id., </em>at 763</a></span> (internal quotation marks omitted). This rule “may be stated clearly enough,” but in the early going after <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>it proved difficult to apply, particularly in cases that involved searches “inside [of] automobile[s] after the arrestees [we]re no longer in [them].” See <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#458" aria-description="Citation for case: New York v. Belton">453 U. S. 454, 458-459</a></span> (1981). A number of courts upheld the constitutionality of vehicle searches that were “substantially contemporaneous” with occupants’ arrests.<footnotemark>1</footnotemark> Other courts disapproved of automobile searches incident to arrests, at least absent some continuing threat that the arrestee might gain access to the vehicle and “destroy evidence or grab a <page-number citation-index="1" label="233">*233</page-number>weapon.”<footnotemark>2</footnotemark> In <em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>this Court granted cer-tiorari to resolve the conflict. See <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#459" aria-description="Citation for case: New York v. Belton"><em>id., </em>at 459-460</a></span>.</p>
<p id="b277-5">In <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>a police officer conducting a traffic stop lawfully-arrested four occupants of a vehicle and ordered the arrest-ees to line up, unhandcuffed, along the side of the thruway. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#456" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 456</a></span>; see Brief for Petitioner in <em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>O. T. 1980, No. 80-328, p. 3. The officer then searched the vehicle’s passenger compartment and found cocaine inside a jacket that lay on the backseat. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#456" aria-description="Citation for case: New York v. Belton">453 U. S., at 456</a></span>. This Court upheld the search as reasonable incident to the occupants’ arrests. In an opinion that repeatedly stressed the need for a “straightforward,” “workable rule” to guide police conduct, the Court announced “that when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#459" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 459-460</a></span> (footnote omitted).</p>
<p id="b277-6">For years, <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was widely -understood to have set down a simple, bright-line rule. Numerous courts read the decision to authorize automobile searches incident to arrests of recent occupants, regardless of whether the arrestee in any particular ease was within reaching distance of the vehicle at the time of the search. See <em>Thornton </em>v. <em>United States, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#628" aria-description="Citation for case: Thornton v. United States">541 U. S. 615, 628</a></span> (2004) (Scalia, J., concurring in judgment) (collecting cases). Even after the arrestee had stepped out of the vehicle and had been subdued by police, the prevailing understanding was that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>still authorized a substantially contemporaneous search of the automobile’s passenger compartment.<footnotemark>3</footnotemark></p>
<p id="b278-4"><page-number citation-index="1" label="234">*234</page-number>Not every court, however, agreed with this reading of <em>Bel-ton. </em>In <em>State </em>v. <em>Gant, </em><span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/" aria-description="Citation for case: State v. Gant">216 Ariz. 1</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/" aria-description="Citation for case: State v. Gant">162 P. 3d 640</a></span> (2007), the Arizona Supreme Court considered an automobile search conducted after the vehicle’s occupant had been arrested, handcuffed, and locked in a patrol car. The court distinguished <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>as a case in which “four unsecured” arrestees "presented an immediate risk of loss of evidence and an obvious threat to [a] lone officer’s safety.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#643" aria-description="Citation for case: State v. Gant">162 P. 3d, at 643</a></span>. The court held that where no such “exigencies exis[t]” — where the arrestee has been subdued and the scene secured — the rule of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>does not apply. <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#643" aria-description="Citation for case: State v. Gant">162 P. 3d, at 643</a></span>.</p>
<p id="b278-5">This Court granted certiorari in <em><span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/" aria-description="Citation for case: State v. Gant">Gant</a></span>, </em>see <span class="citation no-link">552 U. S. 1230</span> (2008), and affirmed in a 5-to-4 decision. <em>Arizona </em>v. Gant, <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U. S. 332</a></span> (2009). Four of the Justices in the majority agreed with the Arizona Supreme Court that <em>Belton's </em>holding applies only where “the arrestee is unsecured and within reaching distance of the passenger compartment at the time of the search.” <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#343" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 343</a></span>. The four dissenting Justices, by contrast, understood <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to have explicitly adopted the simple, bright-line rule stated in the <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>Court’s opinion. 556 ü. S., at 357-358 (opinion of Alito, J.); see <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton"><em>Belton, supra, </em>at 460</a></span> (“[W]e hold that when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile” (footnote omitted)). To limit <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to cases involving unsecured arrestees, the dissenters thought, was to overrule the decision’s clear holding. <em>Gant, supra, </em>at 357-358. Justice Scalia, who provided the fifth vote to affirm in <em>Gant, </em>agreed with the dissenters’ understanding of <em>Belton’s </em>holding. <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#351" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 351-352</a></span> (concurring opinion). Justice Scalia favored a more explicit and complete overruling of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>but he joined what became the majority opinion to avoid “a 4-to-l-to-4” disposition. <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#354" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 354</a></span>. As a result, the Court adopted a new, two-part rule under which an auto<page-number citation-index="1" label="235">*235</page-number>mobile search incident to a recent occupant’s arrest is constitutional (1) if the arrestee is within reaching distance of the vehicle during the search, or (2) if the police have reason to believe that the vehicle contains “evidence relevant to the crime of arrest.” <em><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">Id.,</a></span> </em>at 343 (citing <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#632" aria-description="Citation for case: Thornton v. United States"><em>Thornton, supra, </em>at 632</a></span> (Scalia, J., concurring in judgment); internal quotation marks omitted).</p>
<p id="b279-5">B</p>
<p id="b279-6">The search at issue in this case took place a full two years before this Court announced its new rule in <em>Gant </em>On an April evening in 2007, police officers in Greenville, Alabama, conducted a routine traffic stop that eventually resulted in the arrests of driver Stella Owens (for driving while intoxicated) and passenger Willie Davis (for giving a false name to police). The police handcuffed both Owens and Davis, and they placed the arrestees in the back of separate patrol cars. The police then searched the passenger compartment of Owens’ vehicle and found a revolver inside Davis’ jacket pocket.</p>
<p id="b279-7">Davis was indicted in the Middle District of Alabama on one count of possession of a firearm by a convicted felon. See <span class="citation no-link">18 U. S. C. § 922</span>(g)(1). In his motion to suppress the revolver, Davis acknowledged that the officers’ search fully complied with “existing Eleventh Circuit precedent.” App. 13-15. Like most courts, the Eleventh Circuit had long read <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to establish a bright-line rule authorizing substantially contemporaneous <em>vehicle searches incident to </em>arrests of recent occupants. See <em>United States </em>v. <em>Gonzalez, </em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/#822" aria-description="Citation for case: United States v. Augustin Gonzalez">71 F. 3d 819, 822, 824-827</a></span> (CA11 1996) (upholding automobile search conducted after the defendant had been “pulled from the vehicle, handcuffed, laid on the ground, and placed under arrest”). Davis recognized that the District Court was obligated to follow this precedent, but he raised a Fourth Amendment challenge to preserve “the issue for review” on appeal. App. 15. The District Court denied the motion, and Davis was convicted on the firearms charge.</p>
<p id="b280-5"><page-number citation-index="1" label="236">*236</page-number>While Davis’ appeal was pending, this Court decided <em>Gant. </em>The Eleventh Circuit, in the opinion below, applied <em>Ganfs </em>new rule and held that the vehicle search incident to Davis’ arrest “violated [his] Fourth Amendment rights.” <span class="citation multiple-matches"><a href="/c/F.%203d/598/1259/">598 F. 3d 1259</a></span>, 1263 (CA11 2010). As for whether this constitutional violation warranted suppression, the Eleventh Circuit viewed that as a separate issue that turned on “the potential of exclusion to deter wrongful police conduct.” <em>Id., </em>at 1265 (quoting <em>Herring </em>v. <em>United States, </em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#137" aria-description="Citation for case: Herring v. United States">555 U. S. 135, 137</a></span> (2009); internal quotation marks omitted). The court concluded that “penalizing the [arresting] officer” for following binding appellate precedent would do nothing to “dete[r]. . . Fourth Amendment violations.” 598 F. 3d, at 1265-1266 (bracketing and internal quotation marks omitted). It therefore declined to apply the exclusionary rule and affirmed Davis’ conviction. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./562/1002/">562 U. S. 1002</a></span> (2010).</p>
<p id="b280-6">II</p>
<p id="b280-3">The Fourth Amendment protects the “right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures.” The Amendment says nothing about suppressing evidence obtained in violation of this command. That rule — the exclusionary rule — is a “prudential” doctrine, <em>Pennsylvania Bd. of Probation and Parole </em>v. <em>Scott, </em><span class="citation" data-id="9433685"><a href="/opinion/118235/pennsylvania-bd-of-probation-and-parole-v-scott/#363" aria-description="Citation for case: Pennsylvania Bd. of Probation and Parole v. Scott">524 U. S. 357, 363</a></span> (1998), created by this Court to “compel respect for the constitutional guaranty.” <em>Elkins </em>v. <em>United States, </em><span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960); see <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). Exclusion is “not a personal constitutional right,” nor is it designed to “redress the injury” occasioned by an unconstitutional search. <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 486</a></span> (1976); see <em>United States </em>v. <em>Janis, </em><span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 454, n. 29</a></span> (1976) (exclusionary rule “unsupportable as reparation or compensatory dispensation to the injured criminal” (internal quotation marks omitted)). The rule’s sole purpose, we have repeatedly held, is to deter future Fourth <page-number citation-index="1" label="237">*237</page-number>Amendment violations. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#141" aria-description="Citation for case: Herring v. United States"><em>E. g., Herring, supra, </em>at 141</a></span>, and n. 2; <em>United States </em>v. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#909" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 909, 921, n. 22</a></span> (1984); <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States"><em>Elkins, supra, </em>at 217</a></span> (“calculated to prevent, not to repair”). Our cases have thus limited the rule’s operation to situations in which this purpose is “thought most efficaciously served.” <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 348</a></span> (1974). Where suppression fails to yield “appreciable deterrence,” exclusion is “clearly . . . unwarranted.” <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#454" aria-description="Citation for case: United States v. Janis"><em>Janis, supra, </em>at 454</a></span>.</p>
<p id="b281-5">Real deterrent value is a “necessary condition for exclusion,” but it is not “a sufficient” one. <em>Hudson </em>v. <em>Michigan, </em><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#596" aria-description="Citation for case: Hudson v. Michigan">547 U. S. 586, 596</a></span> (2006). The analysis must also account for the “substantial social costs” generated by the rule. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#907" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 907</a></span>. Exclusion exacts a heavy toll on both the judicial system and society at large. <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell">428 U. S., at 490-491</a></span>. It almost always requires courts to ignore reliable, trustworthy evidence bearing on guilt or innocence. <em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Ibid.</a></span> </em>And its bottom-line effect, in many cases, is to suppress the truth and set the criminal loose in the community without punishment. See <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#141" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 141</a></span>. Orn-eases hold that society must swallow this bitter pill when necessary, but only as a “last resort.” <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#591" aria-description="Citation for case: Hudson v. Michigan"><em>Hudson, supra, </em>at 591</a></span>. For exclusion to be appropriate, the deterrence benefits of suppression must outweigh its heavy costs. See <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#141" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 141</a></span>; <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#910" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 910</a></span>.</p>
<p id="b281-6">Admittedly, there was a time when our exclusionary-rule cases were not nearly so discriminating in <em>their </em>approach to the doctrine. “Expansive dicta” in several decisions, see <span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#591" aria-description="Citation for case: Hudson v. Michigan"><em>Hudson, supra, </em>at 591</a></span>, suggested that the rule was a self-executing mandate implicit in the Fourth Amendment itself. See <em>Olmstead </em>v. <em>United States, </em><span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#462" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 462</a></span> (1928) (remarking <em>on </em>the “striking outcome of the <em>Weeks </em>case” that “the Fourth Amendment, although not referring to or limiting the use of evidence in courts, really forbade its introduction”); <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio"><em>Mapp, supra, </em>at 655</a></span> ("[A]ll evidence obtained by searches and seizures in violation of the Constitution is, by <page-number citation-index="1" label="238">*238</page-number>that same authority, inadmissible in a state court”). As late as our 1971 decision in <em>Whiteley </em>v. <em>Warden, Wyo. State Penitentiary, </em><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/#568" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U. S. 560, 568-569</a></span>, the Court “treated identification of a Fourth Amendment violation as synonymous with application of the exclusionary rule.” <em>Arizona </em>v. <em>Evans, </em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#13" aria-description="Citation for case: Arizona v. Evans">514 U. S. 1, 13</a></span> (1995). In time, however, we came to acknowledge the exclusionary rule for what it undoubtedly is— a “judicially created remedy” of this Court’s own making. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><em>Calandra, supra, </em>at 348</a></span>. We abandoned the old, “reflexive” application of the doctrine, and imposed a more rigorous weighing of its costs and deterrence benefits. <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#13" aria-description="Citation for case: Arizona v. Evans"><em>Evans, supra, </em>at 13</a></span>; see, <em>e. g., <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra, supra;</a></span> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">Janis, supra;</a></span> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone, supra;</a></span> INS </em>v. <em>Lopez-Mendoza, </em><span class="citation" data-id="9429772"><a href="/opinion/111265/immigration-naturalization-service-v-lopez-mendoza/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Lopez-Mendoza">468 U. S. 1032</a></span> (1984); <em>United States </em>v. <em>Havens, </em><span class="citation" data-id="9427937"><a href="/opinion/110267/united-states-v-havens/" aria-description="Citation for case: United States v. Havens">446 U. S. 620</a></span> (1980). In a line of cases beginning with <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span>, we also recalibrated our cost-benefit analysis in exclusion cases to focus the inquiry on the “flagrancy of the police misconduct” at issue. <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#909" aria-description="Citation for case: United States v. Leon"><em>Id., </em>at 909, 911</a></span>.</p>
<p id="b282-4">The basic insight of the <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>line of cases is that the deterrence benefits of exclusion “var[y] with the culpability of the law enforcement conduct” at issue. <em>Herring, </em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#143" aria-description="Citation for case: Herring v. United States">555 U. S., at 143</a></span>. When the police exhibit “deliberate,” “reckless,” or “grossly negligent” disregard for Fourth Amendment rights, the deterrent value of exclusion is strong and tends to outweigh the resulting costs. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#144" aria-description="Citation for case: Herring v. United States"><em>Id., </em>at 144</a></span>. But when the police act with an objectively “reasonable good-faith belief” that their conduct is lawful, <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#909" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 909</a></span> (internal quotation marks omitted), or when their conduct involves only simple, “isolated” negligence, <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#137" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 137</a></span>, the “'deterrence rationale loses much of its force,”’ and exclusion cannot “pay its way,” <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#919" aria-description="Citation for case: United States v. Leon"><em>Leon, supra, </em>at 919, 908</a></span>, n. 6 (quoting <em>United States </em>v. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#539" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 539</a></span> (1975)).</p>
<p id="b282-5">The Court has over time applied this “good-faith” exception across a range of cases. <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>itself, for example, held that the exclusionary rule does not apply when the police conduct a search in “objectively reasonable reliance” on a <page-number citation-index="1" label="239">*239</page-number>warrant later held invalid. 468 U. S., at 922. The error in such a case rests with the issuing magistrate, not the police officer, and “punish[ing] the errors of judges” is not the office of the exclusionary rule. <em>Id., </em>at 916; see also <em>Massachusetts </em>v. <em>Sheppard, </em><span class="citation" data-id="111263"><a href="/opinion/111263/massachusetts-v-sheppard/#990" aria-description="Citation for case: Massachusetts v. Sheppard">468 U. S. 981, 990</a></span> (1984) (companion case declining to apply exclusionary rule where warrant held invalid as a result of judge’s clerical error).</p>
<p id="b283-6">Other good-faith eases have sounded a similar theme. <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987), extended the good-faith exception to searches conducted in reasonable reliance on subsequently invalidated statutes. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#349" aria-description="Citation for case: Illinois v. Krull"><em>Id., </em>at 349-350</a></span> (“legislators, like judicial officers, are not the focus of the rule”). In <em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">Evans, supra,</a></span> </em>the Court applied the good-faith exception in a case where the police reasonably relied on erroneous information concerning an arrest warrant in a database maintained by judicial employees. <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#14" aria-description="Citation for case: Arizona v. Evans"><em>Id., </em>at 14</a></span>. Most recently, in <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">Herring, supra,</a></span> </em>we extended <em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">Evans</a></span> </em>in a case where <em>police </em>employees erred in maintaining records in a warrant database. “[IJsolated,” “nonrecurring” police negligence, we determined, lacks the culpability required to justify the harsh sanction of exclusion. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#137" aria-description="Citation for case: Herring v. United States">555 U. S., at 137, 144</a></span>.</p>
<p id="b283-7">1 — I I — i ) — I</p>
<p id="b283-3">The question in this ease is whether to apply the exclusionary rule when the police conduct a search in objectively reasonable reliance on binding judicial precedent. At the time of the search at issue here, we had not yet decided <em>Gant, </em><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U. S. 332</a></span>, and the Eleventh Circuit had interpreted our decision in <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span>, to establish a bright-line rule authorizing the search of a vehicle’s passenger compartment incident to a recent occupant’s arrest. <em>Gonzalez, </em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/#825" aria-description="Citation for case: United States v. Augustin Gonzalez">71 F. 3d, at 825</a></span>. The search incident to Davis’ arrest in this case followed the Eleventh Circuit’s <em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/" aria-description="Citation for case: United States v. Augustin Gonzalez">Gonzalez</a></span> </em>precedent to the letter. Although the search turned out to be unconstitutional under <em>Gant, </em>all agree that the officers’ conduct was in strict compliance with then-binding Circuit law and was not <page-number citation-index="1" label="240">*240</page-number>culpable in any way. See Brief for Petitioner 49 (“suppression” in this case would “impl[y] no assignment of blame”).</p>
<p id="b284-5">Under our exclusionary-rule precedents, this acknowledged absence of police culpability dooms Davis’ claim. Police practices trigger the harsh sanction of exclusion only when they are deliberate enough to yield “meaningful 1]” deterrence, and culpable enough to be “worth the price paid by the justice system.” <em>Herring, </em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#144" aria-description="Citation for case: Herring v. United States">555 U. S., at 144</a></span>. The conduct of the officers here was neither of these things. The officers who conducted the search did not violate Davis’ Fourth Amendment rights deliberately, recklessly, or with gross negligence. See <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">ibid.</a></span> </em>Nor does this case involve any “recurring or systemic negligence” on the part of law enforcement. <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">Ibid.</a></span> </em>The police acted in strict compliance with binding precedent, and their behavior was not wrongful. Unless the exclusionary rule is to become a strict-liability regime, it can have no application in this case.</p>
<p id="b284-6">Indeed, in 27 years of practice under <em>Leon’s </em>good-faith exception, we have “never applied” the exclusionary rule to suppress evidence obtained as a result of noneulpable, innocent police conduct. <span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/#144" aria-description="Citation for case: Herring v. United States"><em>Herring, supra, </em>at 144</a></span>. If the police in this case had reasonably relied on a warrant in conducting their search, see <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon, supra,</a></span> </em>or on an erroneous warrant record in a government database, <em><span class="citation" data-id="9435413"><a href="/opinion/145922/herring-v-united-states/" aria-description="Citation for case: Herring v. United States">Herring, supra,</a></span> </em>the exclusionary rule would not apply. And if Congress or the Alabama Legislature had enacted a statute codifying the precise holding of the Eleventh Circuit’s decision in <em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/" aria-description="Citation for case: United States v. Augustin Gonzalez">Gonzalez</a></span>,</em><footnotemark><em>4</em></footnotemark><em>, </em>we <page-number citation-index="1" label="241">*241</page-number>would swiftly conclude that “ ‘[penalizing the officer for the [legislature’s] error . . . cannot logically contribute to the deterrence of Fourth Amendment violations.’” <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#350" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 350</a></span>. The same should be true of Davis’ attempt here to “ ‘[p]enaliz[e] the officer for the [appellate judges’] error.’” <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Ibid.</a></span></em></p>
<p id="b285-5">About all that exclusion would deter in this case is conscientious police work. Responsible law enforcement officers will take care to learn “what is required of them” under Fourth Amendment precedent and will conform their conduct to these rules. <em>Hudson, </em><span class="citation" data-id="9434934"><a href="/opinion/145646/hudson-v-michigan/#599" aria-description="Citation for case: Hudson v. Michigan">547 U. S., at 599</a></span>. But by the same token, when binding appellate precedent specifically <em>authorizes </em>a particular police practice, well-trained officers will and should use that tool to fulfill their crime-detection and public-safety responsibilities. An officer who conducts a search in reliance on binding appellate precedent does no more than ‘“ac[t] as a reasonable officer would and should act’ ” under the circumstances. <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S., at 920</a></span> (quoting <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#539" aria-description="Citation for case: Stone v. Powell">428 U. S., at 539-540</a></span> (White, J., dissenting)). The deterrent effect of exclusion in such a case can only be to discourage the officer from ‘“do[ing] his duty.’” 468 U. S., at 920.</p>
<p id="b285-6">That is not the kind of deterrence the exclusionary rule seeks to foster. We have stated before, and we reaffirm today, that the harsh sanction of exclusion “should not be applied to deter objectively reasonable law enforcement activity.” <em>Id., </em>at 919. Evidence obtained during a search conducted in reasonable reliance on binding precedent is not subject to the exclusionary rule.</p>
<p id="b285-7">IV</p>
<p id="b285-8">Justice Breyer’s dissent and Davis argue that, although the police conduct in this case was in no way culpable, other considerations should prevent the good-faith exception from applying. We are not persuaded.</p>
<p id="b286-4"><page-number citation-index="1" label="242">*242</page-number>A</p>
<p id="b286-5">1</p>
<p id="b286-6">The principal argument of both the dissent and Davis is that the exclusionary rule’s availability to enforce new Fourth Amendment precedent is a retroactivity issue, see <em>Griffith </em>v. <em>Kentucky, </em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">479 U. S. 314</a></span> (1987), not a good-faith issue. They contend that applying the good-faith exception where police have relied on overruled precedent effectively revives the discarded retroactivity regime of <em>Linkletter </em>v. <em>Walker, </em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span> (1965). See <em>post, </em>at 254-256.</p>
<p id="b286-7">In <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span>, </em>we held that the retroactive effect of a new constitutional rule of criminal procedure should be determined on a case-by-case weighing of interests. For each new rule, <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>required courts to consider a three-faetor balancing test that looked to the “purpose” of the new rule, “reliance” on the old rule by law enforcement and others, and the effect retroactivity would have “on the administration of justice.” <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#636" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 636</a></span>. After “weighting] the merits and demerits in each case,” courts decided whether and to what extent a new rule should be given retroactive effect. <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#629" aria-description="Citation for case: Linkletter v. Walker"><em>Id., </em>at 629</a></span>. In <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>itself, the balance of interests prompted this Court to conclude that <em>Mapp </em>v. <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio</a></span>, </em>367 U. S. 643—which incorporated the exclusionary rule against the States — should not apply retroactively to cases already final on direct review. <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#639" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 639-640</a></span>. The next year, we extended <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>to retroactivity determinations in eases on direct review. See <em>Johnson </em>v. <em>New </em>Jersey, <span class="citation" data-id="107260"><a href="/opinion/107260/johnson-v-new-jersey/#733" aria-description="Citation for case: Johnson v. New Jersey">384 U. S. 719, 733</a></span> (1966) (holding that <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964), applied retroactively only to trials commenced after the decisions were released).</p>
<p id="b286-8">Over time, <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>proved difficult to apply in a consistent, coherent way. Individual applications of the standard “produced strikingly divergent results,” <em>Danforth </em>v. <em>Minnesota, </em><span class="citation" data-id="9046929"><a href="/opinion/9053440/danforth-v-minnesota/#273" aria-description="Citation for case: Danforth v. Minnesota">552 U. S. 264, 273</a></span> (2008), that many saw as “incompatible” and “inconsistent,” <em>Desist </em>v. <em>United States, </em><span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#258" aria-description="Citation for case: Desist v. United States">394 U. S. 244, 258</a></span> (1969) (Harlan, J., dissenting). Justice Harlan in particu<page-number citation-index="1" label="243">*243</page-number>lar, who had endorsed the <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>standard early on, offered a strong critique in which he argued that “basic judicial” norms required full retroactive application of new rules to all eases still subject to direct review. <span class="citation" data-id="9423951"><a href="/opinion/107875/desist-v-united-states/#258" aria-description="Citation for case: Desist v. United States">394 U. S., at 258-259</a></span>.; see also <em>Mackey </em>v. <em>United </em>States, <span class="citation" data-id="9424506"><a href="/opinion/108302/mackey-v-united-states/#675" aria-description="Citation for case: MacKey v. United States">401 U. S. 667, 675-702</a></span> (1971) (Harlan, J., concurring in part and dissenting in part). Eventually, and after more than 20 years of toil under <em>Link-</em>letter, the Court adopted Justice Harlan’s view and held that newly announced rules of constitutional criminal procedure must apply “retroactively to all cases, state or federal, pending on direct review or not yet final, with no exception.” <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/#328" aria-description="Citation for case: Griffith v. Kentucky"><em>Griffith, supra, </em>at 328</a></span>.</p>
<p id="b287-5">2</p>
<p id="b287-6">The dissent and Davis argue that applying the good-faith exception in this case is “incompatible” with our retroactivity precedent under <em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">Griffith</a></span>. </em>See <em>post, </em>at 254; Reply Brief for Petitioner 3-7. We think this argument conflates what are two distinct doctrines.</p>
<p id="b287-7">Our retroactivity jurisprudence is concerned with whether, as a categorical matter, a new rule is available on direct review as a <em>potential </em>ground for relief. Retroactive application under <em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">Griffith</a></span> </em>lifts what would otherwise be a categorical bar to obtaining redress for the government's violation of a newly announced constitutional rule. See <em>Dan-forth, supra, </em>at 271, n. 5 (noting that it may “make more sense to speak in terms of the ‘redressability’ of violations of new rules, rather than the ‘retroactivity’ of such new rules”). Retroactive application does not, however, determine what “appropriate remedy” (if any) the defendant should obtain. See <em>Powell </em>v. <em>Nevada, </em><span class="citation" data-id="9432977"><a href="/opinion/117833/powell-v-nevada/#84" aria-description="Citation for case: Powell v. Nevada">511 U. S. 79, 84</a></span> (1994) (noting that it “does not necessarily follow” from retroactive application of a new rule that the defendant will “gain . . . relief”). Remedy is a separate, analytically distinct issue. Cf. <em>American Trucking Assns., Inc. </em>v. <em>Smith, </em><span class="citation" data-id="9432043"><a href="/opinion/112450/american-trucking-assns-inc-v-smith/#189" aria-description="Citation for case: American Trucking Assns., Inc. v. Smith">496 U. S. 167, 189</a></span> (1990) (plurality opinion) (“[T]he Court has never equated its retroac-tivity principles with remedial principles”). As a result, the retroactive application of a new rule of substantive Fourth <page-number citation-index="1" label="244">*244</page-number>Amendment law <em>raises </em>the question whether a suppression remedy applies; it does not answer that question. See <em>Leon, </em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#906" aria-description="Citation for case: United States v. Leon">468 U. S., at 906</a></span> (‘Whether the exclusionary sanction is appropriately imposed in a particular case ... is ‘an issue separate from the question whether the Fourth Amendment rights of the party seeking to invoke the rule were violated by police conduct’ ”).</p>
<p id="b288-5">When this Court announced its decision in <em>Gant, </em>Davis’ conviction had not yet become final on direct review. <em>Gant </em>therefore applies retroactively to this case. Davis may invoke its newly announced rule of substantive Fourth Amendment law as a basis for seeking relief. See <span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/#326" aria-description="Citation for case: Griffith v. Kentucky"><em>Griffith, supra, </em>at 326, 328</a></span>. The question, then, becomes one of remedy, and on that issue Davis seeks application of the exclusionary rule. But exclusion of evidence does not automatically follow from the fact that a Fourth Amendment violation occurred. See <em>Evans, </em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#13" aria-description="Citation for case: Arizona v. Evans">514 U. S., at 13-14</a></span>. The remedy is subject to exceptions and applies only where its “purpose is effectively advanced.” <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#347" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 347</a></span>.</p>
<p id="b288-6">The dissent and Davis recognize that at least some of the established exceptions to the exclusionary rule limit its availability in cases involving new Fourth Amendment rules. Suppression would thus be inappropriate, the dissent and Davis acknowledge, if the inevitable-discovery exception were applicable in this case. See <em>post, </em>at 254; Reply Brief for Petitioner 22 (“Doctrines such as inevitable discovery, independent source, attenuated basis, [and] standing . . . sharply limit the impact of newly-announced rules”). The good-faith exception, however, is no less an established limit on the <em>remedy </em>of exclusion than is inevitable discovery. Its application here neither contravenes <em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">Griffith</a></span> </em>nor denies retroactive effect to <em>Gant.</em><footnotemark><em>5</em></footnotemark></p>
<p id="b289-4"><page-number citation-index="1" label="245">*245</page-number>It is true that, under the old retroactivity regime of <em>Link-letter, </em>the Court's decisions on the “retroactivity problem in the context of the exclusionary rule” did take into account whether “law enforcement officers reasonably believed in good faith” that their conduct was in compliance with governing law. <em>Peltier, </em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#535" aria-description="Citation for case: United States v. Peltier">422 U. S., at 535-537</a></span>. As a matter of retroactivity analysis, that approach is no longer applicable. See <em>Griffith, </em><span class="citation" data-id="9430765"><a href="/opinion/111785/griffith-v-kentucky/" aria-description="Citation for case: Griffith v. Kentucky">479 U. S. 314</a></span>. It does not follow, however, that reliance on binding precedent is irrelevant in applying the good-faith exception to the exclusionary rule. When this Court adopted the good-faith exception in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>the Court’s opinion explicitly relied on <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">Peltier</a></span> </em>and imported its reasoning into the good-faith inquiry. See 468 U. S., at 918-919. That reasonable reliance by police was once a factor in our retroactivity cases does not make it any less relevant under our <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span> </em>line of eases.<footnotemark>6</footnotemark></p>
<p id="b289-5">B</p>
<p id="b289-6">Davis also contends that applying the good-faith exception to searches conducted in reliance on binding precedent will stunt the development of Fourth Amendment <page-number citation-index="1" label="246">*246</page-number>law. With no possibility of suppression, criminal defendants will have no incentive, Davis maintains, to request that courts overrule precedent.<footnotemark>7</footnotemark></p>
<p id="b290-5">1</p>
<p id="b290-6">This argument is difficult to reconcile with our modern understanding of the role of the exclusionary rule. We have never held that facilitating the overruling of precedent is a relevant consideration in an exclusionary-rule case. Rather, we have said time and again that the <em>sole </em>purpose of the exclusionary rule is to deter misconduct by law enforcement. See, <em>e. g., Sheppard, </em>468 U. S., at 990 (“ 'adopted to deter unlawful searches by police’ ”); <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#14" aria-description="Citation for case: Arizona v. Evans"><em>Evans, supra, </em>at 14</a></span> (“historically designed as a means of deterring police misconduct”).</p>
<p id="b290-7">We have also repeatedly rejected efforts to expand the focus of the exclusionary rule beyond deterrence of culpable police conduct. In <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>, </em>for example, we made clear that “the exclusionary rule is designed to deter police misconduct rather than to punish the errors of judges.” 468 U. S., at 916; see <em>id., </em>at 918 (“If exclusion of evidence obtained pursuant to a subsequently invalidated warrant is to have any deterrent effect... it must alter the behavior of individual law enforcement officers or the policies of their departments”). <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>too noted that “legislators, like judicial officers, are not the focus” of the exclusionary.rule. <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#850" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 850</a></span>. And in <em><span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/" aria-description="Citation for case: Arizona v. Evans">Evans</a></span>, </em>we said that the exclusionary rule was aimed at deterring “police misconduct, not mistakes by court employees.” <span class="citation" data-id="9433091"><a href="/opinion/117905/arizona-v-evans/#14" aria-description="Citation for case: Arizona v. Evans">514 U. S., at 14</a></span>. These cases do not suggest that the exclusionary rule should be modified to serve a purpose other than deterrence of culpable law enforcement conduct.</p>
<p id="Atb"><page-number citation-index="1" label="247">*247</page-number>2</p>
<p id="b291-4">And in any event, applying the good-faith exception in this context will not prevent judicial reconsideration of prior Fourth Amendment precedents. In most instances, as in this case, the precedent sought to be challenged will be a decision of a federal court of appeals or state supreme court. But a good-faith exception for objectively reasonable reliance on binding precedent will not prevent review and correction of such decisions. This Court reviews criminal convictions from 12 Federal Courts of Appeals, 50 state courts of last resort, and the District of Columbia Court of Appeals. If one or even many of these courts uphold a particular type of search or seizure, defendants in jurisdictions in which the question remains open will still have an undiminished incentive to litigate the issue. This Court can then grant certio-rari, and the development of Fourth Amendment law will in no way be stunted.<footnotemark>8</footnotemark></p>
<p id="b291-5">Davis argues that Fourth Amendment precedents of <em>this </em>Court will be effectively insulated from challenge under a good-faith exception for reliance on appellate precedent. But this argumentas overblown. For one thing, it is important to keep in mind that this argument applies to an exceedingly small set of cases. Decisions overruling this Court's Fourth Amendment precedents are rare. Indeed, it has been more than 40 years since the Court last handed down a decision of the type to which Davis refers. <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (overruling <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950), and <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span> (1947)). And even in those cases, Davis points out that <page-number citation-index="1" label="248">*248</page-number>no fewer than eight separate doctrines may preclude a defendant who successfully challenges an existing precedent from getting any relief. Brief for Petitioner 50. Moreover, as a practical matter, defense counsel in many cases will test this Cuurt’s Fourth Amendment precedents in the same way that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was tested in <em>Gant </em>— by arguing that the precedent is distinguishable. See Brief for Respondent in <em>Arizona </em>v. <em>Gant, </em>O. T. 2008, No. 07-542, pp. 22-29.<footnotemark>9</footnotemark></p>
<p id="b292-5">At most, Davis’ argument might suggest that — to prevent Fourth Amendment law from becoming ossified — the petitioner in a case that results in the overruling of one of this Court’s Fourth Amendment precedents should be given the benefit of the victory by permitting the suppression of evidence in that one case. Such a result would undoubtedly be a windfall to this one random litigant. But the exclusionary rule is “not a personal constitutional right.” <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S., at 486</a></span>. It is a “judicially created” sanction, <em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">Calandra</a></span>, </em>414 TI. ñ., at 848, specifically designed as a “windfall” remedy to deter future Fourth Amendment violations. See <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#490" aria-description="Citation for case: Stone v. Powell"><em>Stone, supra, </em>at 490</a></span>. The good-faith exception is a judicially created exception to this judicially created rule. Therefore, in a future case, we could, if necessary, recognize a limited exception to the good-faith exception for a defendant who obtains a judgment overruling one of our Fourth Amendment precedents. Cf. Friendly, The Bill of Rights as a Code of Criminal Procedure, <span class="citation no-link">53 Cal. L. Rev. 929</span>, 952-953 (1965) (“[T]he same authority that empowered the Court to supplement the amendment by the exclusionary rule a hundred and twenty-five years after its adoption, likewise allows it to <page-number citation-index="1" label="249">*249</page-number>modify that rule as the lessons of experience may teach” (internal quotation marks and footnotes omitted)).<footnotemark>10</footnotemark></p>
<p id="b293-5">But this is not such a case. Davis did not secure a decision overturning a Supreme Court precedent; the police in his case reasonably relied on binding Circuit precedent. See <em>Gonzalez, </em><span class="citation" data-id="709244"><a href="/opinion/709244/united-states-v-augustin-gonzalez/" aria-description="Citation for case: United States v. Augustin Gonzalez">71 F. 3d 819</a></span>. That sort of blameless police conduct, we hold, comes within the good-faith exception and is not properly subject to the exclusionary rule.</p>
<p id="b293-6">* * *</p>
<p id="b293-7">It is one thing for the criminal “to go free because the constable has blundered.” <em>People </em>v. <em>Before, </em><span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#21" aria-description="Citation for case: People v. Defore">242 N. Y. 13, 21</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/#587" aria-description="Citation for case: People v. Defore">150 N. E. 585, 587</a></span> (1926) (Cardozo, J.). It is quite another to set the criminal free because the constable has scrupulously adhered to governing law. Excluding evidence in such cases deters no police misconduct and imposes substantial social costs. We therefore hold that when the police conduct a search in objectively reasonable reliance on binding appellate <page-number citation-index="1" label="250">*250</page-number>precedent, the exclusionary rule does not apply. The judgment of the Court of Appeals for the Eleventh Circuit is</p>
<p id="b294-4">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b276-6"> See, <em>e. g., United States </em>v. <em>Sanders, </em><span class="citation" data-id="9467153"><a href="/opinion/382713/united-states-v-willard-r-sanders/#1313" aria-description="Citation for case: United States v. Willard R. Sanders">631 F. 2d 1309, 1313-1314</a></span> (CA8 1980); <em>United States </em>v. <em>Dixon, </em><span class="citation" data-id="347138"><a href="/opinion/347138/united-states-v-lewis-nathaniel-dixon/#922" aria-description="Citation for case: United States v. Lewis Nathaniel Dixon">558 F. 2d 919, 922</a></span> (CA9 1977); <em>United States </em>v. <em>Frick, </em><span class="citation" data-id="9460209"><a href="/opinion/316377/united-states-v-robert-lee-frick-and-quimet-john-petersen/#668" aria-description="Citation for case: United States v. Robert Lee Frick and Quimet John Petersen">490 F. 2d 666, 668-669</a></span> (CA5 1973); <em>Hinkel </em>v. <em>Anchorage, </em><span class="citation" data-id="9617077"><a href="/opinion/1391930/hinkel-v-anchorage/#1069" aria-description="Citation for case: Hinkel v. Anchorage">618 P. 2d 1069, 1069-1071</a></span> (Alaska 1980).</p>
</footnote>
<footnote label="2">
<p id="b277-7"> See, <em>e. g., United States v. Benson, </em><span class="citation" data-id="9467155"><a href="/opinion/382715/united-states-v-jeffrey-joseph-benson/#1340" aria-description="Citation for case: United States v. Jeffrey Joseph Benson">631 F. 2d 1336, 1340</a></span> (CA8 1980); see also <em>United States </em>v. <em>Rigales, </em><span class="citation" data-id="382105"><a href="/opinion/382105/united-states-v-ernesto-g-rigales-jr/#366" aria-description="Citation for case: United States v. Ernesto G. Rigales, Jr.">630 F. 2d 364, 366-367</a></span> (CA5 1980); <em>Ulesky </em>v. <em>State, </em><span class="citation" data-id="1687668"><a href="/opinion/1687668/ulesky-v-state/#125" aria-description="Citation for case: Ulesky v. State">379 So. 2d 121, 125-126</a></span> (Fla. App. 1979).</p>
</footnote>
<footnote label="3">
<p id="b277-8"> See, <em>e. g., United States </em>v. <em>Dorsey, </em><span class="citation" data-id="9498265"><a href="/opinion/791442/united-states-v-nikos-delano-dorsey/#1041" aria-description="Citation for case: United States v. Nikos Delano Dorsey">418 F. 3d 1038, 1041, 1043-1044</a></span> (CA9 2005) (upholding automobile search conducted after the officer had “hand cuffed [tho arrcotcc] and put him in the back of [the] patrol car”); <em>United States </em>v. <em>Barnes, </em><span class="citation" data-id="9497145"><a href="/opinion/786840/united-states-v-angelo-barnes/#604" aria-description="Citation for case: United States v. Angelo Barnes">374 F. 3d 601, 604</a></span> (CA8 2004) (same).</p>
</footnote>
<footnote label="4">
<p id="b284-7"> Cf. <span class="citation no-link">Kan. Stat. Ann. § 22-2501</span>(c) (2007) (“When a lawful arrest is ef-fécted a law enforcement officer may reasonably search the person arrested and the area within such person’s immediate presence for the purpose of . . . [discovering the fruits, instrumentalities, or evidence of a crime”). The Kansas Supreme Court recently struck this provision down in light of <em>Arizona </em>v. <em>Gant, </em><span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">556 U. S. 332</a></span> (2009). <em>State </em>v. <em>Henning, </em><span class="citation" data-id="2625720"><a href="/opinion/2625720/state-v-henning/#137" aria-description="Citation for case: State v. Henning">289 Kan. 136, 137</a></span>, <span class="citation" data-id="2625720"><a href="/opinion/2625720/state-v-henning/#714" aria-description="Citation for case: State v. Henning">209 P. 3d 711, 714</a></span> (2009). But it has applied <em>Illinois </em>v. <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">480 U. S. 340</a></span> (1987), and the good-faith exception to searches conducted in reasonable reliance on the statute. See <em>State </em>v. <em>Daniel, </em><span class="citation" data-id="9761057"><a href="/opinion/2373665/state-v-daniel/#497" aria-description="Citation for case: State v. Daniel">291 Kan. 490, 497-504</a></span>, <span class="citation" data-id="9761057"><a href="/opinion/2373665/state-v-daniel/#1191" aria-description="Citation for case: State v. Daniel">242 P. 3d 1186, 1191-1195</a></span> (2010).</p>
</footnote>
<footnote label="5">
<p id="b288-7"> The dissent argues that the good-faith exception is “unlike ... inevitable discovery” because the former applies in all cases where the police reasonably rely on binding precedent, while the latter “applies only upon occasion.” <em>Post, </em>at 254. We fail to see how this distinction makes any dif-<page-number citation-index="1" label="245">*245</page-number>forcncc. Tho same could bo said indoed, tho oame <em>wao </em>oaid <em>■ of </em>searches conducted in reasonable reliance on statutes. See <em>Krull, </em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#368" aria-description="Citation for case: Illinois v. Krull">480 U. S., at 368-369</a></span> (O'Connor, <em>J., </em>dissenting) (arguing that result in <em><span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/" aria-description="Citation for case: Illinois v. Krull">Krull</a></span> </em>was inconsistent with <em>Griffith). </em>When this Court strikes down a statute on Fourth Amendment grounds, the good-faith exception may prevent the exclusion ary rulo from applying “in <em>every </em>case pending when [the statute] is over turned.” <em>Post, </em>at 254. This result does not make the Court’s newly announced rule of Fourth Amendment law any less retroactive. It simply limits the applicability of a suppression remedy. See <span class="citation" data-id="9430871"><a href="/opinion/111835/illinois-v-krull/#354" aria-description="Citation for case: Illinois v. Krull"><em>Krull, supra, </em>at 354-355, n. 11</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b289-12"> Nor does <em>United States </em>v. <em>Johnson, </em><span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/" aria-description="Citation for case: United States v. Johnson">457 U. S. 537</a></span> (1982), foreclose application of the good faith exception in eases involving changing law. <em>John son </em>distinguished <em><span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/" aria-description="Citation for case: United States v. Peltier">Peltier</a></span> </em>and held that all Fourth Amendment cases should be retroactivo on direct review so long as tho new decision is not a “clear break” from prior precedent. <span class="citation" data-id="9428844"><a href="/opinion/110754/united-states-v-johnson/#562" aria-description="Citation for case: United States v. Johnson">457 U. S., at 562</a></span>. <em>Johnson </em>had no occasion to opino on tho good faith exception to the exclusionary rule, which we adopted two years later in <em><span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">Leon</a></span>.</em></p>
</footnote>
<footnote label="7">
<p id="b290-8"> Davis also asserts that a good faith rule would permit “new Fourth Amendment dccioiono to be applied only prospoctivoly,” thus amounting to “a regime of rule-ereation by advisory opinion.” Brief for Petitioner 23, 25. For reasons discussed in connection with Davis’ argument that application of tho good faith exception hero would revive tho <em><span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">Linkletter</a></span> </em>regime, this argument eonflatoa tho quoetion of retroactivity with tho question of remedy.</p>
</footnote>
<footnote label="8">
<p id="b291-6"> Tho diooent docs not dispute this point, but it claims that the good faith exception will prevent us from “retyping] upon lower courts to work out Fourth Amendment differences among themselves.” <em>Post, </em>at 256. If that is correct, then today’c holding may well lead to <em>moro </em>oirouit oplito in Fourth Amendment eaccs and a <em>fullov </em>docket of Fourth Amendment caceo in this Court. See this Court’s Rule 10. Such a state of affairs is unlikely to result in ossification of Fourth Amendment doctrine.</p>
</footnote>
<footnote label="9">
<p id="b292-6"> Where the search at issue is conducted in accordance with a municipal “policy” or “custom,” Fourth Amendment precedents may also be challenged, without the obotaclc of the good-faith exception or qualified immunity, in civil suits against municipalities. See <span class="citation no-link">42 U. S. C. § 1988</span>; <em>Los Angeles County </em>v. <em>Humphries, </em><span class="citation" data-id="180037"><a href="/opinion/180037/los-angeles-county-v-humphries/#36" aria-description="Citation for case: Los Angeles County v. Humphries">562 U. S. 29, 36</a></span> (2010) (citing <em>Monell </em>v. <em>New York City Dept. of Social Servs., </em><span class="citation" data-id="9427232"><a href="/opinion/109881/monell-v-new-york-city-dept-of-social-servs/#690" aria-description="Citation for case: Monell v. New York City Dept. of Social Servs.">436 U. S. 658, 690-691</a></span> (1978)).</p>
</footnote>
<footnote label="10">
<p id="b293-8"> Davis contends that a criminal defendant will lack Article III standing to challenge an existing Fourth Amendment precedent if the good-faith exception to the exclusionary rule precludes the defendant from obtaining relief based on police conduct that conformed to that precedent. This argument confuses weakness on the merits with absence of Article III standing. See <em>ASARCO Inc. </em>v. <em>Radish, </em><span class="citation" data-id="9431683"><a href="/opinion/112268/asarco-inc-v-kadish/#624" aria-description="Citation for case: Asarco Inc. v. Kadish">490 U. S. 605, 624</a></span> (1989) (standing does not “ ‘depen[d] on the merits of [a claim]’ ”). And as a practical matter, the argument is also overstated. In many instances, as in <em>Gant, </em>see <span class="citation" data-id="9435359"><a href="/opinion/145887/arizona-v-gant/#841" aria-description="Citation for case: Arizona v. Gant">556 U. S., at 841</a></span>, defendants will not simply concede that the police conduct conformed to the precedent; they will argue instead that the police conduct did not fall within the scope of the precedent.</p>
<p id="b293-9">In any event, even if some criminal defendants will be unable to challenge some precedents for the reason that Davis suggests, that provides no good reason for refusing to apply the good-faith exception. As noted, the exclusionary rule is not a personal right, see <em>Stone, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#486" aria-description="Citation for case: Stone v. Powell">428 U. S., at 486, 490</a></span>, and therefore the rights of these defendants will not be impaired. And because (at least in almost all instances) the precedent can be challenged by others, Fourth Amendment ease law will not be insulated from reconsideration.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Davis v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Davis v. United States"
type: case
citation: "512 U.S. 452 (1994)"
parallel_cite: "114 S. Ct. 2350; 129 L. Ed. 2d 362"
neutral_cite: 1994 U.S. LEXIS 4827
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1994
date_decided: 1994-06-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1994-06-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Davis v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117863/davis-v-united-states/"
  cluster_id: 117863
  opinion_id: 9433017
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Berghuis v. Thompkins]]", "[[Arizona v. Roberson]]"]
aliases: ["Davis v. United States (1994)"]
tags: ["case", "fifth-amendment", "miranda", "invocation", "right-to-counsel", "ambiguous-request"]
holding: "A suspect must invoke the right to counsel UNAMBIGUOUSLY; an equivocal or ambiguous reference (\"maybe I should talk to a lawyer\") does…"
lake:
  record_id: Davis v. United States
  status: under_review
  projected_at: 2026-07-09
---

# Davis v. United States

*512 U.S. 452 (1994)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
During a Naval Investigative Service custodial interrogation about a murder, Davis waived his rights and answered questions, then said that maybe he should talk to a lawyer. The agents asked clarifying questions; Davis said he did not want a lawyer, and questioning continued, producing incriminating statements. He moved to suppress, arguing his remark invoked his right to counsel.

## Issue
Whether an ambiguous or equivocal reference to counsel during custodial interrogation requires police to stop questioning under *[[Edwards v. Arizona]]*.

## Rule
No; the invocation of counsel must be unambiguous. "[T]he suspect must unambiguously request counsel. . . . [H]e must articulate his desire to have counsel present sufficiently clearly that a reasonable police officer in the circumstances would understand the statement to be a request for an attorney. If the statement fails to meet the requisite level of clarity, *Edwards* does not require that the officers stop questioning the suspect." — 512 U.S. 452, 459. ^pin-459

A merely ambiguous reference to a lawyer — one that a reasonable officer would understand only as a possible invocation — does not trigger the *[[Edwards v. Arizona|Edwards]]* bar, and officers are not required (though it may be good practice) to ask clarifying questions.

## Application
Davis's remark that maybe he should talk to a lawyer was, on these facts, not a clear request for counsel a reasonable officer would have understood as an invocation; indeed, when the agents sought clarification, Davis disclaimed wanting a lawyer. Because his reference was ambiguous and not an unambiguous request, the agents were not required to cease questioning, and his subsequent statements were admissible.

## Conclusion
The ambiguous reference did not invoke the right to counsel; the conviction was affirmed. Invocation of *[[Edwards v. Arizona|Edwards]]* protection requires a clear, unambiguous request.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Davis* refines [[Edwards v. Arizona]] by setting the clarity threshold for invoking counsel; [[Berghuis v. Thompkins]] later applied the same unambiguous-invocation logic to the right to remain silent.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Davis v. United States*, 512 U.S. 452 (1994) — https://www.courtlistener.com/opinion/117863/davis-v-united-states/ — pinpoint: 459.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "73dce0e316a26299", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "513 U.S. 1008 (1994)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Davis v. United States", "year": "1994"}}
{"assertion_id": "95f5803c3e541f75", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A suspect must invoke the right to counsel UNAMBIGUOUSLY; an equivocal or ambiguous reference (\\\"maybe I should talk to a lawyer\\\") does…", "title": "Davis v. United States"}}
{"assertion_id": "fedba37ec9c547f8", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "Davis v. United States"}}
{"assertion_id": "b65806320893abc2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Davis v. United States"}}
{"assertion_id": "c18ecaf3aa079da9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1994-06-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Davis v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Davis v. United States", "varies_by_point": "false"}}
```

### lake record — Davis v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Davis v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Davis v. United States",
    "case_name_short": "Davis",
    "case_name_full": "Davis v. United States",
    "input_case_name": "Davis v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1994-06-24",
    "year": 1994,
    "docket": null,
    "cluster_id": 117863,
    "lead_opinion_id": 9433017,
    "sibling_ids": [
      117863,
      9433017,
      9433018
    ],
    "absolute_url": "/opinion/117863/davis-v-united-states/",
    "identity_method": "panel-cluster-rekey",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9148720,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147571,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147570,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147150,
        "score": 20,
        "case_name": "Davis v. United States"
      },
      {
        "cluster_id": 9147149,
        "score": 20,
        "case_name": "Davis v. United States"
      }
    ],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "512 U.S. 452",
      "volume": "512",
      "reporter": "U.S.",
      "page": "452",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "114 S. Ct. 2350",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "2350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 L. Ed. 2d 362",
        "volume": "129",
        "reporter": "L. Ed. 2d",
        "page": "362",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1994 U.S. LEXIS 4827",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "4827",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "512 U.S. 452",
        "volume": "512",
        "reporter": "U.S.",
        "page": "452",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "114 S. Ct. 2350",
        "volume": "114",
        "reporter": "S. Ct.",
        "page": "2350",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 L. Ed. 2d 362",
        "volume": "129",
        "reporter": "L. Ed. 2d",
        "page": "362",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1994 U.S. LEXIS 4827",
        "volume": "1994",
        "reporter": "U.S. LEXIS",
        "page": "4827",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "512 U.S. 452",
    "official_selection": {
      "court_class": "scotus",
      "selected": "512 U.S. 452",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-459",
      "page": null,
      "quote": "--- # Davis v. United States *512 U.S. 452 (1994)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background During a Naval Investigative Service custodial interrogation about a murder, Davis waived his rights and answered questions, then said that maybe he should talk to a lawyer. The agents asked clarifying questions; Davis said he did not want a lawyer, and questioning continued, producing incriminating statements. He moved to suppress, arguing his remark invoked his right to counsel. ## Issue Whether an ambiguous or equivocal reference to counsel during custodial interrogation requires police to stop questioning under *Edwards v. Arizona*. ## Rule No; the invocation of counsel must be unambiguous.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1994-06-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Davis v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9143409) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
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
      },
      "lane2_top_cited": {
        "query": "cites:(9143409)",
        "reviewed": 0,
        "cap": 25,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null
      },
      "lane3_recency": {
        "query": "cites:(9143409)",
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
    "complete_query": "cites:(9143409)",
    "indexed_citing_opinions": 0,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9143409,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 0,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/davis-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": null,
    "rows_cached": 0,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T02:18:01Z",
    "date_modified": "2026-07-09T23:22:52Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law",
      "panel cluster re-key -> cluster 117863 (evidence: S9 F-S9-DN-002 miskey-sweep; _run/s9/rekey-targets.jsonl 2026-07-09; stub cluster 9148721 -> merits 117863 (Davis v. United States, 512 U.S. 452, 1994))"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:20:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:20:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Davis v. United States

```
<opinion type="majority">
<author id="b504-4"><page-number citation-index="1" label="454">*454</page-number>Justice O’Connor</author>
<p id="A-h">delivered the opinion of the Court.</p>
<p id="b504-5">In <em>Edwards </em>v. Arizona, <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), we held that law enforcement officers must immediately cease questioning a suspect who has clearly asserted his right to have counsel present during custodial interrogation. In this case we decide how law enforcement officers should respond when a suspect makes a reference to counsel that is insufficiently clear to invoke the <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>prohibition on further questioning.</p>
<p id="b504-6">I</p>
<p id="b504-7">Pool brought trouble — not to River City, but to the Charleston Naval Base. Petitioner, a member of the United States Navy, spent the evening of October 2, 1988, shooting pool at a club on the base. Another sailor, Keith Shackleton, lost a game and a $30 wager to petitioner, but Shackleton refused to pay. After the club closed, Shackleton was beaten to death with a pool cue on a loading dock behind the commissary. The body was found early the next morning.</p>
<p id="b504-8">The investigation by the Naval Investigative Service (NIS) gradually focused on petitioner. Investigative agents determined that petitioner was at the club that evening, and that he was absent without authorization from his duty station the next morning. The agents also learned that only privately owned pool cues could be removed from the club premises, and that petitioner owned two cues — one of which had a bloodstain on it. The agents were told by various people that petitioner either had admitted committing the crime or had recounted details that clearly indicated his involvement in the killing.</p>
<p id="b504-9">On November 4, 1988, petitioner was interviewed at the NIS office. As required by military law, the agents advised petitioner that he was a suspect in the killing, that he was not required to make a statement, that any statement could be used against him at a trial by court-martial, and that he was entitled to speak with an attorney and have an attorney present during questioning. See Art. 31, Uniform Code of <page-number citation-index="1" label="455">*455</page-number>Military Justice (UCMJ), <span class="citation no-link">10 U.S.C. §831</span>; Mil. Rule Evid. 305; Manual for Courts-Martial A22-13 (1984). Petitioner waived his rights to remain silent and to counsel, both orally and in writing.</p>
<p id="b505-5">About an hour and a half into the interview, petitioner said, “Maybe I should talk to a lawyer.” App. 135. According to the uncontradicted testimony of one of the interviewing agents, the interview then proceeded as follows:</p>
<blockquote id="b505-6">“[We m]ade it very clear that we’re not here to violate his rights, that if he wants a lawyer, then we will stop any kind of questioning with him, that we weren’t going to pursue the matter unless we have it clarified is he asking for a lawyer or is he just making a comment about a lawyer, and he said, [‘]No, I’m not asking for a lawyer,’ and then he continued on, and said, ‘No, I don’t want a lawyer.’” <span class="citation no-link"><em>Id., </em>at 136</span>.</blockquote>
<p id="b505-7">After a short break, the agents reminded petitioner of his rights to remain silent and to counsel. The interview then continued for another hour, until petitioner said, “I think I want a lawyer before I say anything else.” <span class="citation no-link"><em>Id., </em>at 137</span>. At that point, questioning ceased.</p>
<p id="b505-8">At his general court-martial, petitioner moved to suppress statements made during the November 4 interview. The Military Judge denied the motion, holding that “the mention of a lawyer by [petitioner] during the course of the interrogation [was] not in the form of a request for counsel and . . . the agents properly determined that [petitioner] was not indicating a desire for or invoking his right to counsel.” <span class="citation no-link"><em>Id., </em>at 164</span>. Petitioner was convicted on one specification of unpremeditated murder, in violation of Art. 118, UCMJ, <span class="citation no-link">10 U. S. C. § 918</span>. He was sentenced to confinement for life, a dishonorable discharge, forfeiture of all pay and allowances, and a reduction to the lowest pay grade. The convening authority approved the findings and sentence. The Navy-<page-number citation-index="1" label="456">*456</page-number>Marine Corps Court of Military Review affirmed. App. to Pet. for Cert. 12a-15a.</p>
<p id="b506-5">The United States Court of Military Appeals granted discretionary review and affirmed. <span class="citation" data-id="8650321"><a href="/opinion/8668432/united-states-v-davis/" aria-description="Citation for case: United States v. Davis">36 M. J. 337</a></span> (1993). The court recognized that the state and federal courts have developed three different approaches to a suspect’s ambiguous or equivocal request for counsel:</p>
<blockquote id="b506-6">“Some jurisdictions have held that any mention of counsel, however ambiguous, is sufficient to require that all questioning cease. Others have attempted to define a threshold standard of clarity for invoking the right to counsel and have held that comments falling short of the threshold do not invoke the right to counsel. Some jurisdictions . . . have held that all interrogation about the offense must immediately cease whenever a suspect mentions counsel, but they allow interrogators to ask narrow questions designed to clarify the earlier statement and the [suspect’s] desires respecting counsel.” <span class="citation" data-id="8650321"><a href="/opinion/8668432/united-states-v-davis/#341" aria-description="Citation for case: United States v. Davis"><em>Id., </em>at 341</a></span> (internal quotation marks omitted).</blockquote>
<p id="b506-7">Applying the third approach, the court held that petitioner’s comment was ambiguous, and that the NIS agents properly clarified petitioner’s wishes with respect to counsel before continuing questioning him about the offense. <span class="citation" data-id="8650321"><a href="/opinion/8668432/united-states-v-davis/#341" aria-description="Citation for case: United States v. Davis"><em>Id., </em>at 341-342</a></span>.</p>
<p id="b506-8">Although we have twice previously noted the varying approaches the lower courts have adopted with respect to ambiguous or equivocal references to counsel during custodial interrogation, see <em>Connecticut </em>v. <em>Barrett, </em><span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#529" aria-description="Citation for case: Connecticut v. Barrett">479 U. S. 523, 529-530, n. 3</a></span> (1987); <em>Smith </em>v. <em>Illinois, </em><span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#96" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 96, n. 3</a></span> (1984) <em>(per curiam), </em>we have not addressed the issue on the merits. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./510/942/">510 U. S. 942</a></span> (1993), to do so.</p>
<p id="b506-9">II</p>
<p id="b506-10">The Sixth Amendment right to counsel attaches only at the initiation of adversary criminal proceedings, see <em>United </em><page-number citation-index="1" label="457">*457</page-number><em>States </em>v. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#188" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 188</a></span> (1984), and before proceedings are initiated a suspect in a criminal investigation has no constitutional right to the assistance of counsel. Nevertheless, we held in <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#469" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 469-473</a></span> (1966), that a suspect subject to custodial interrogation has the right to consult with an attorney and to have counsel present during questioning, and that the police must explain this right to him before questioning begins. The right to counsel established in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was one of a “series of recommended ‘procedural safeguards’... [that] were not themselves rights protected by the Constitution but were instead measures to insure that the right against compulsory self-incrimination was protected.” <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#443" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 443-444</a></span> (1974); see U. S. Const., Arndt. 5 (“No person . . . shall be compelled in any criminal case to be a witness against himself”).<footnotemark>*</footnotemark></p>
<p id="b508-4"><page-number citation-index="1" label="458">*458</page-number>The right to counsel recognized in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is sufficiently important to suspects in criminal investigations, we have held, that it “requires] the special protection of the knowing and intelligent waiver standard.” <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#483" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 483</a></span>. See <em>Oregon </em>v. <em>Bradshaw, </em><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1046" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1046-1047</a></span> (1983) (plurality opinion); <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1051" aria-description="Citation for case: Oregon v. Bradshaw"><em>id., </em>at 1051</a></span> (Powell, J., concurring in judgment). If the suspect effectively waives his right to counsel after receiving the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, law enforcement officers are free to question him. <em>North Carolina </em>v. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#372" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 372-376</a></span> (1979). But if a suspect requests counsel at any time during the interview, he is not subject to further questioning until a lawyer has been made available or the suspect himself reinitiates conversation. <em>Edwards </em>v. <em>Arizona, supra, </em>at 484-485. This “second layer of prophylaxis for the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel,” <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#176" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S. 171, 176</a></span> (1991), is “designed to prevent police from badgering a defendant into waiving his previously asserted <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights,” <em>Michigan </em>v. <em>Harvey, </em><span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990). To that end, we have held that a suspect who has invoked the right to counsel cannot be questioned regarding any offense unless an attorney is actually present. <em>Minnick </em>v. <em>Mississippi, </em><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U. S. 146</a></span> (1990); <em>Arizona </em>v. <em>Roberson, </em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988). “It remains clear, however, that this prohibition on further questioning — like other aspects of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>— is not itself required by the Fifth Amendment’s prohibition on coerced confessions, but is instead justified only by reference to its prophylactic purpose.” <em>Connecticut </em>v. <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#528" aria-description="Citation for case: Connecticut v. Barrett"><em>Barrett, supra, </em>at 528</a></span>.</p>
<p id="b508-5">The applicability of the “ ‘rigid’ prophylactic rule” of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>requires courts to “determine whether the accused <em>actually invoked </em>his right to counsel.” <em>Smith </em>v. <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#95" aria-description="Citation for case: Smith v. Illinois"><em>Illinois, supra, </em>at 95</a></span> (emphasis added), quoting <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 719</a></span> (1979). To avoid difficulties of proof and to <page-number citation-index="1" label="459">*459</page-number>provide guidance to officers conducting interrogations, this is an objective inquiry. See <em>Connecticut </em>v. <span class="citation" data-id="9430786"><a href="/opinion/111796/connecticut-v-barrett/#529" aria-description="Citation for case: Connecticut v. Barrett"><em>Barrett, supra, </em>at 529</a></span>. Invocation of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel “requires, at a minimum, some statement that can reasonably be construed to be an expression of a desire for the assistance of an attorney.” <em>McNeil </em>v. <em>Wisconsin, </em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/#178" aria-description="Citation for case: McNeil v. Wisconsin">501 U. S., at 178</a></span>. But if a suspect makes a reference to an attorney that is ambiguous or equivocal in that a reasonable officer in light of the circumstances would have understood only that the suspect <em>might </em>be invoking the right to counsel, our precedents do not require the cessation of questioning. See <em><span class="citation" data-id="9432329"><a href="/opinion/112622/mcneil-v-wisconsin/" aria-description="Citation for case: McNeil v. Wisconsin">ibid.</a></span> </em>(“[T]he <em>likelihood </em>that a suspect would wish counsel to be present is not the test for applicability of <em>Edwards”); Edwards </em>v. <em>Arizona, supra, </em>at 485 (impermissible for authorities “to re-interrogate an accused in custody if he has <em>clearly asserted </em>his right to counsel”) (emphasis added).</p>
<p id="b509-5">Rather, the suspect must unambiguously request counsel. As we have observed, “a statement either is such an assertion of the right to counsel or it is not.” <em>Smith </em>v. <em>Illinois, </em><span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#97" aria-description="Citation for case: Smith v. Illinois">469 U. S., at 97-98</a></span> (brackets and internal quotation marks omitted). Although a suspect need not “speak with the discrimination of an Oxford don,” <em>post, </em>at 476 (Souter, J., concurring in judgment), he must articulate his desire to have counsel present sufficiently clearly that a reasonable police officer in the circumstances would understand the statement to be a request for an attorney. If the statement fails to meet the requisite level of clarity, <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>does not require that the officers stop questioning the suspect. See <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#433" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 433, n. 4</a></span> (1986) (“[T]he interrogation must cease until an attorney is present <em>only </em>[i]f the individual states that he wants an attorney”) (citations and internal quotation marks omitted).</p>
<p id="b509-6">We decline petitioner’s invitation to extend <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>and require law enforcement officers to cease questioning immediately upon the making of an ambiguous or equivocal reference to an attorney. See <em>Arizona </em>v. <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#688" aria-description="Citation for case: Arizona v. Roberson"><em>Roberson, supra, </em>at 688</a></span> <page-number citation-index="1" label="460">*460</page-number>(Kennedy, J., dissenting) (“[T]he rule of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>is our rule, not a constitutional command; and it is our obligation to justify its expansion”). The rationale underlying <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>is that the police must respect a suspect’s wishes regarding his right to have an attorney present during custodial interrogation. But when the officers conducting the questioning reasonably do not know whether or not the suspect wants a lawyer, a rule requiring the immediate cessation of questioning “would transform the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>safeguards into wholly irrational obstacles to legitimate police investigative activity,” <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#102" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96, 102</a></span> (1975), because it would needlessly prevent the police from questioning a suspect in the absence of counsel even if the suspect did not wish to have a lawyer present. Nothing in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>requires the provision of counsel to a suspect who consents to answer questions without the assistance of a lawyer. In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself, we expressly rejected the suggestion “that each police station must have a ‘station house lawyer’ present at all times to advise prisoners,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>, and held instead that a suspect must be told of his right to have an attorney present and that he may not be questioned after invoking his right to counsel. We also noted that if a suspect is “indecisive in his request for counsel,” the officers need not always cease questioning. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#485" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 485</a></span>.</p>
<p id="b510-5">We recognize that requiring a clear assertion of the right to counsel might disadvantage some suspects who — because of fear, intimidation, lack of linguistic skills, or a variety of other reasons — will not clearly articulate their right to counsel although they actually want to have a lawyer present. But the primary protection afforded suspects subject to custodial interrogation is the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings themselves. “[F]ull comprehension of the rights to remain silent and request an attorney [is] sufficient to dispel whatever coercion is inherent in the interrogation process.” <em>Moran </em>v. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#427" aria-description="Citation for case: Moran v. Burbine"><em>Burbine, supra, </em>at 427</a></span>. A suspect who knowingly and voluntarily waives his right to counsel after having that right explained <page-number citation-index="1" label="461">*461</page-number>to him has indicated his willingness to deal with the police unassisted. Although <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>provides an additional protection — if a suspect subsequently requests an attorney, questioning must cease — it is one that must be affirmatively invoked by the suspect.</p>
<p id="b511-5">In considering how a suspect must invoke the right to counsel, we must consider the other side of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>equation: the need for effective law enforcement. Although the courts ensure compliance with the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requirements through the exclusionary rule, it is police officers who must actually decide whether or not they can question a suspect. The <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule — questioning must cease if the suspect asks for a lawyer — provides a bright line that can be applied by officers in the real world of investigation and interrogation without unduly hampering the gathering of information. But if we were to require questioning to cease if a suspect makes a statement that <em>might </em>be a request for an attorney, this clarity and ease of application would be lost. Police officers would be forced to make difficult judgment calls about whether the suspect in fact wants a lawyer even though he has not said so, with the threat of suppression if they guess wrong. We therefore hold that, after a knowing and voluntary waiver of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, law enforcement officers may continue questioning until and unless the suspect clearly requests an attorney.</p>
<p id="b511-6">Of course, when a suspect makes an ambiguous or equivocal statement it will often be good police practice for the interviewing officers to clarify whether or not he actually wants an attorney. That was the procedure followed by the NIS agents in this case. Clarifying questions help protect the rights of the suspect by ensuring that he gets an attorney if he wants one, and will minimize the chance of a confession being suppressed due to subsequent judicial second-guessing as to the meaning of the suspect’s statement regarding counsel. But we decline to adopt a rule requiring officers to ask clarifying questions. If the suspect’s state<page-number citation-index="1" label="462">*462</page-number>ment is not an unambiguous or unequivocal request for counsel, the officers have no obligation to stop questioning him.</p>
<p id="b512-5">To recapitulate: We held in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>that a suspect is entitled to the assistance of counsel during custodial interrogation even though the Constitution does not provide for such assistance. We held in <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>that if the suspect invokes the right to counsel at any time, the police must immediately cease questioning him until an attorney is present. But we are unwilling to create a third layer of prophylaxis to prevent police questioning when the suspect <em>might </em>want a lawyer. Unless the suspect actually requests an attorney, questioning may continue.</p>
<p id="b512-6">The courts below found that petitioner’s remark to the NIS agents — “Maybe I should talk to a lawyer” — was not a request for counsel, and we see no reason to disturb that conclusion. The NIS agents therefore were not required to stop questioning petitioner, though it was entirely proper for them to clarify whether petitioner in fact wanted a lawyer. Because there is no ground for suppression of petitioner’s statements, the judgment of the Court of Military Appeals is</p>
<p id="b512-7">
<em>Affirmed.</em>
</p>
<footnote label="*">
<p id="b507-5">We have never had occasion to consider whether the Fifth Amendment privilege against self-incrimination, or the attendant right to counsel during custodial interrogation, applies of its own force to the military, and we need not do so here. The President, exercising his authority to prescribe procedures for military criminal proceedings, see Art. 36(a), UCMJ, <span class="citation no-link">10 U. S. C. § 836</span>(a), has decreed that statements obtained in violation of the Self-Incrimination Clause are generally not admissible at trials by court-martial. Mil. Rules Evid. 304(a) and (c)(3). Because the Court of Military Appeals has held that our cases construing the Fifth Amendment right to counsel apply to military interrogations and control the admissibility of evidence at trials by court-martial, see, <em>e. g., United States </em>v. <em>McLaren, </em><span class="citation" data-id="8650768"><a href="/opinion/8668774/united-states-v-mclaren/#115" aria-description="Citation for case: United States v. McLaren">38 M. J. 112, 115</a></span> (1993); <em>United States </em>v. <em>Applewhite, </em><span class="citation" data-id="8647228"><a href="/opinion/8666011/united-states-v-applewhite/#198" aria-description="Citation for case: United States v. Applewhite">23 M. J. 196, 198</a></span> (1987), and the parties do not contest this point, we proceed on the assumption that our precedents apply to courts-martial just as they apply to state and federal criminal prosecutions.</p>
<p id="b507-6">We also note that the Government has not sought to rely in this case on <span class="citation no-link">18 U. S. C. §3501</span>, “the statute governing the admissibility of confessions in federal prosecutions,” <em>United States </em>v. <em>Alvarez-Sanchez, </em><span class="citation" data-id="9527039"><a href="/opinion/1087948/united-states-v-alvarez-sanchez/#351" aria-description="Citation for case: United States v. Alvarez-Sanchez">511 U. S. 350, 351</a></span> (1994), and we therefore decline the invitation of some <em>amici </em>to consider it. See Brief for Washington Legal Foundation et al. as <em>Amici Curiae </em>7-14. Although we will consider arguments raised only in an <em>amicus </em>brief, see <em>Teague </em>v. <em>Lane, </em><span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/#300" aria-description="Citation for case: Teague v. Lane">489 U. S. 288, 300</a></span> (1989) (plurality opinion), we are reluctant to do so when the issue is one of first impression involving <page-number citation-index="1" label="458">*458</page-number>the interpretation of a federal statute on which the Department of Justice expressly declines to take a position. See Tr. of Oral Arg. 44-47.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Delaware v. Prouse.md  (`case`, 6 assertions)

### content_page

```
---
title: "Delaware v. Prouse"
type: case
citation: "440 U.S. 648 (1979)"
parallel_cite: "99 S. Ct. 1391; 59 L. Ed. 2d 660"
neutral_cite: 1979 U.S. LEXIS 80
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-03-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-03-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Delaware v. Prouse
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110045/delaware-v-prouse/"
  cluster_id: 110045
  opinion_id: 110045
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Checkpoints and Roadblocks]]"
    role: "Related (cross-doctrine)"
related: ["[[Heien v. North Carolina]]", "[[City of Indianapolis v. Edmond]]", "[[Whren v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "reasonable-suspicion", "random-stop", "license-check"]
holding: "Random, suspicionless stops of motorists to check license and registration are unreasonable under the Fourth Amendment; an officer needs…"
lake:
  record_id: Delaware v. Prouse
  status: verified
  projected_at: 2026-07-06
---

# Delaware v. Prouse

*440 U.S. 648 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A patrolman, acting on no observed violation or articulable suspicion, stopped Prouse's car solely to check his license and registration; he smelled and then saw marijuana in plain view, leading to charges. Prouse moved to suppress, and the Delaware courts held the random, suspicionless stop unconstitutional.

## Issue
Whether police may stop a motorist to check his driver's license and registration without any articulable and reasonable suspicion of wrongdoing.

## Rule
No. "[W]e hold that except in those situations in which there is at least articulable and reasonable suspicion that a motorist is unlicensed or that an automobile is not registered, or that either the vehicle or an occupant is otherwise subject to seizure for violation of law, stopping an automobile and detaining the driver in order to check his driver's license and the registration of the automobile are unreasonable under the Fourth Amendment." — 440 U.S. 648, 663. ^pin-663

The Court left open less-intrusive, non-discretionary alternatives such as questioning all traffic at fixed roadblock-type checkpoints.

## Application
The officer stopped Prouse without observing any traffic or equipment violation and without any reasonable suspicion that he was unlicensed, the car unregistered, or anyone subject to seizure — the stop was admittedly random and at the officer's unbridled discretion. Because such a discretionary, suspicionless spot check is unreasonable, the stop was unconstitutional and the marijuana it produced should have been suppressed.

## Conclusion
The random, suspicionless license-check stop violated the Fourth Amendment; the suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Prouse* requires individualized suspicion for discretionary traffic stops while preserving non-discretionary checkpoints — a line developed in [[City of Indianapolis v. Edmond]] and complemented by the reasonable-mistake rule of [[Heien v. North Carolina]].

## Appears on
- [[Traffic Stops]] — *Key — Progeny / Refinement*

## Sources
- *Delaware v. Prouse*, 440 U.S. 648 (1979) — https://www.courtlistener.com/opinion/110045/delaware-v-prouse/ — pinpoint: 663.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "22d7463da500294c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "440 U.S. 648 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 80", "official_citation_present": true, "parallel_cite": "99 S. Ct. 1391; 59 L. Ed. 2d 660", "title": "Delaware v. Prouse", "year": "1979"}}
{"assertion_id": "0560617417148934", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Random, suspicionless stops of motorists to check license and registration are unreasonable under the Fourth Amendment; an officer needs…", "title": "Delaware v. Prouse"}}
{"assertion_id": "1027c18d0c309632", "dimension": "support", "kind": "home_role", "locator": {"home": "Checkpoints and Roadblocks"}, "payload": {"home": "Checkpoints and Roadblocks", "role": "Related (cross-doctrine)", "title": "Delaware v. Prouse"}}
{"assertion_id": "6f7a27814e3f8616", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Key — Progeny / Refinement", "title": "Delaware v. Prouse"}}
{"assertion_id": "43f83d500f5eb9e8", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Delaware v. Prouse"}}
{"assertion_id": "d92be3adf83536a9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-03-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Delaware v. Prouse", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Delaware v. Prouse", "varies_by_point": "false"}}
```

### lake record — Delaware v. Prouse

```json
{
  "schema_version": "s2.v1",
  "record_id": "Delaware v. Prouse",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Delaware v. Prouse",
    "case_name_short": "Prouse",
    "case_name_full": "Delaware v. Prouse",
    "input_case_name": "Delaware v. Prouse",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-03-27",
    "year": 1979,
    "docket": null,
    "cluster_id": 110045,
    "lead_opinion_id": 110045,
    "sibling_ids": [
      110045,
      9427509,
      9427510,
      9427511
    ],
    "absolute_url": "/opinion/110045/delaware-v-prouse/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "440 U.S. 648",
      "volume": "440",
      "reporter": "U.S.",
      "page": "648",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1391",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 660",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "660",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 80",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "80",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "440 U.S. 648",
        "volume": "440",
        "reporter": "U.S.",
        "page": "648",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1391",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1391",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "59 L. Ed. 2d 660",
        "volume": "59",
        "reporter": "L. Ed. 2d",
        "page": "660",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 80",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "80",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "440 U.S. 648",
    "official_selection": {
      "court_class": "scotus",
      "selected": "440 U.S. 648",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-663",
      "page": null,
      "quote": "--- # Delaware v. Prouse *440 U.S. 648 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A patrolman, acting on no observed violation or articulable suspicion, stopped Prouse's car solely to check his license and registration; he smelled and then saw marijuana in plain view, leading to charges. Prouse moved to suppress, and the Delaware courts held the random, suspicionless stop unconstitutional. ## Issue Whether police may stop a motorist to check his driver's license and registration without any articulable and reasonable suspicion of wrongdoing. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-03-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Delaware v. Prouse",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Delaware v. Prouse:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Marlon Juan Lall v. the State of Texas",
          "cluster_id": 10046849,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 9352626,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 6466320,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane1_negative"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mendenhall",
          "cluster_id": 110264,
          "cite": [
            "64 L. Ed. 2d 497",
            "100 S. Ct. 1870",
            "446 U.S. 544",
            "1980 U.S. LEXIS 102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baker v. McCollan",
          "cluster_id": 110132,
          "cite": [
            "61 L. Ed. 2d 433",
            "99 S. Ct. 2689",
            "443 U.S. 137",
            "1979 U.S. LEXIS 141"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Hodari D.",
          "cluster_id": 112579,
          "cite": [
            "113 L. Ed. 2d 690",
            "111 S. Ct. 1547",
            "499 U.S. 621",
            "1991 U.S. LEXIS 2397",
            "91 Cal. Daily Op. Serv. 2893",
            "59 U.S.L.W. 4335",
            "91 Daily Journal DAR 4665"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Texas",
          "cluster_id": 110128,
          "cite": [
            "61 L. Ed. 2d 357",
            "99 S. Ct. 2637",
            "443 U.S. 47",
            "1979 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Kennedy",
          "cluster_id": 110714,
          "cite": [
            "72 L. Ed. 2d 416",
            "102 S. Ct. 2083",
            "456 U.S. 667",
            "1982 U.S. LEXIS 111",
            "50 U.S.L.W. 4544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
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
        "journal_ref": "Delaware v. Prouse:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTkxNTc0NDAwMDAwJnM9NDc2MDAwMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110045+OR+9427509+OR+9427510+OR+9427511%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05ODUmcz0xNDU2NDAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110045+OR+9427509+OR+9427510+OR+9427511%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511)",
        "reviewed": 109,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 109,
        "triage_read": 2,
        "triage_snippet_classified": 107
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110045 OR 9427509 OR 9427510 OR 9427511)",
    "indexed_citing_opinions": 3221,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110045,
        "count": 2856,
        "count_source": "search"
      },
      {
        "opinion_id": 9427509,
        "count": 435,
        "count_source": "search"
      },
      {
        "opinion_id": 9427510,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427511,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5550,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/delaware-v-prouse.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkzMzEyODUmcz0xMDQ2MjY1NCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110045+OR+9427509+OR+9427510+OR+9427511%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110045,
        "cited_id": 90041,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 102505,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 107917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108767,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 274285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 299088,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 321729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 332182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 348709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1087989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1190270,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1332651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1367261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1442373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1471204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1500552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1518042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1701839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1778812,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 1893463,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 2170567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 2354841,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110045,
        "cited_id": 2378216,
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
    "date_created": "2026-07-05T02:20:37Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:20:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:20:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T02:24:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:20:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Delaware v. Prouse

```
<div>
<center><b><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U.S. 648</a></span> (1979)</b></center>
<center><h1>DELAWARE<br>
v.<br>
PROUSE.</h1></center>
<center>No. 77-1571.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 17, 1979.</center>
<center>Decided March 27, 1979.</center>
CERTIORARI TO THE SUPREME COURT OF DELAWARE.
<p><span class="star-pagination">*649</span> <i>Charles M. Oberly III</i> argued the cause for petitioner. With him on the brief were <i>Richard R. Wier, Jr.,</i> Attorney General of Delaware, and <i>Carolyn Berger, Fred S. Silverman,</i> and <i>Kathleen Molyneux,</i> Deputy Attorneys General.</p>
<p><i>David M. Lukoff</i> argued the cause for respondent. With him on the brief were <i>Richard M. Baumeister, Frank Askin,</i> and <i>Eric Neisser.</i><sup>[*]</sup></p>
<p><span class="star-pagination">*650</span> MR. JUSTICE WHITE delivered the opinion of the Court.</p>
<p>The question is whether it is an unreasonable seizure under the Fourth and Fourteenth Amendments to stop an automobile, being driven on a public highway, for the purpose of checking the driving license of the operator and the registration of the car, where there is neither probable cause to believe nor reasonable suspicion that the car is being driven contrary to the laws governing the operation of motor vehicles or that either the car or any of its occupants is subject to seizure or detention in connection with the violation of any other applicable law.</p>
<p></p>
<h2>I</h2>
<p>At 7:20 p. m. on November 30, 1976, a New Castle County, Del., patrolman in a police cruiser stopped the automobile occupied by respondent.<sup>[1]</sup> The patrolman smelled marihuana smoke as he was walking toward the stopped vehicle, and he seized marihuana in plain view on the car floor. Respondent was subsequently indicted for illegal possession of a controlled substance. At a hearing on respondent's motion to suppress the marihuana seized as a result of the stop, the patrolman testified that prior to stopping the vehicle he had observed neither traffic or equipment violations nor any suspicious activity, and that he made the stop only in order to check the driver's license and registration. The patrolman was not acting pursuant to any standards, guidelines, or procedures pertaining to document spot checks, promulgated by either his department or the State Attorney General. Characterizing the stop as "routine," the patrolman explained, "I saw the car <span class="star-pagination">*651</span> in the area and wasn't answering any complaints, so I decided to pull them off." App. A9. The trial court granted the motion to suppress, finding the stop and detention to have been wholly capricious and therefore violative of the Fourth Amendment.</p>
<p>The Delaware Supreme Court affirmed, noting first that "[t]he issue of the legal validity of systematic, roadblock-type stops of a number of vehicles for license and vehicle registration check is <i>not</i> now before the Court," <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1362" aria-description="Citation for case: State v. Prouse">382 A. 2d 1359, 1362</a></span> (1978) (emphasis in original). The court held that "a random stop of a motorist in the absence of specific articulable facts which justify the stop by indicating a reasonable suspicion that a violation of the law has occurred is constitutionally impermissible and violative of the Fourth and Fourteenth Amendments to the United States Constitution." <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1364" aria-description="Citation for case: State v. Prouse"><i>Id.,</i> at 1364</a></span>. We granted certiorari to resolve the conflict between this decision, which is in accord with decisions in five other jurisdictions,<sup>[2]</sup> and the contrary determination in six jurisdictions<sup>[3]</sup> that the Fourth Amendment does not prohibit the kind of automobile stop that occurred here. <span class="citation multiple-matches"><a href="/c/U.%20S./439/816/">439 U. S. 816</a></span> (1978).</p>
<p></p>
<h2>II</h2>
<p>Because the Delaware Supreme Court held that the stop at issue not only violated the Federal Constitution but also <span class="star-pagination">*652</span> was impermissible under Art. I, § 6, of the Delaware Constitution, it is urged that the judgment below was based on an independent and adequate state ground and that we therefore have no jurisdiction in this case. <i>Fox Film Corp.</i> v. <i>Muller,</i> <span class="citation" data-id="102505"><a href="/opinion/102505/fox-film-corp-v-muller/#210" aria-description="Citation for case: Fox Film Corp. v. Muller">296 U. S. 207, 210</a></span> (1935). At least, it is suggested, the matter is sufficiently uncertain that we should remand for clarification as to the ground upon which the judgment rested. <i>California</i> v. <i>Krivda,</i> <span class="citation" data-id="108622"><a href="/opinion/108622/california-v-krivda/#35" aria-description="Citation for case: California v. Krivda">409 U. S. 33, 35</a></span> (1972). Based on our reading of the opinion, however, we are satisfied that even if the State Constitution would have provided an adequate basis for the judgment, the Delaware Supreme Court did not intend to rest its decision independently on the State Constitution and that we have jurisdiction of this case.</p>
<p>As we understand the opinion below, Art I, § 6, of the Delaware Constitution will automatically be interpreted at least as broadly as the Fourth Amendment;<sup>[4]</sup> that is, every police practice authoritatively determined to be contrary to the Fourth and Fourteenth Amendments will, without further analysis, be held to be contrary to Art. I, § 6. This approach, which is consistent with previous opinions of the Delaware Supreme Court,<sup>[5]</sup> was followed in this case. The court analyzed <span class="star-pagination">*653</span> the various decisions interpreting the Federal Constitution, concluded that the Fourth Amendment foreclosed spot checks of automobiles, and summarily held that the State Constitution was therefore also infringed. This is one of those cases where "at the very least, the [state] court felt compelled by what it understood to be federal constitutional considerations to construe . . . its own law in the manner it did." <i>Zacchini</i> v. <i>Scripps-Howard Broadcasting Co.,</i> <span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/#568" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">433 U. S. 562, 568</a></span> (1977). Had state law not been mentioned at all, there would be no question about our jurisdiction, even though the State Constitution might have provided an independent and adequate state ground. <i><span class="citation" data-id="9426968"><a href="/opinion/109730/zacchini-v-scripps-howard-broadcasting-co/" aria-description="Citation for case: Zacchini v. Scripps-Howard Broadcasting Co.">Ibid.</a></span></i> The same result should follow here where the state constitutional holding depended upon the state court's view of the reach of the Fourth and Fourteenth Amendments. If the state court misapprehended federal law, "[i]t should be freed to decide . . . these suits according to its own local law." <i>Missouri ex rel. Southern R. Co.</i> v. <i>Mayfield,</i> <span class="citation" data-id="9527085"><a href="/opinion/1087989/missouri-ex-rel-southern-railway-co-v-mayfield/#5" aria-description="Citation for case: Missouri Ex Rel. Southern Railway Co. v. Mayfield">340 U. S. 1, 5</a></span> (1950).</p>
<p></p>
<h2>III</h2>
<p>The Fourth and Fourteenth Amendments are implicated in this case because stopping an automobile and detaining its occupants constitute a "seizure" within the meaning of those Amendments, even though the purpose of the stop is limited and the resulting detention quite brief. <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#556" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 556-558</a></span> (1976); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); cf. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16</a></span> (1968). The essential purpose of the proscriptions in the Fourth Amendment is to impose a standard <span class="star-pagination">*654</span> of "reasonableness"<sup>[6]</sup> upon the exercise of discretion by government officials, including law enforcement agents, in order " `to safeguard the privacy and security of individuals against arbitrary invasions. . . .' " <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 312</a></span> (1978), quoting <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967).<sup>[7]</sup> Thus, the permissibility of a particular law enforcement practice is judged by balancing its intrusion on the individual's Fourth Amendment interests against its promotion of legitimate governmental interests.<sup>[8]</sup> Implemented in this manner, the reasonableness standard usually requires, at a minimum, that the facts upon which an intrusion is based be capable of measurement against "an objective standard,"<sup>[9]</sup> whether this be probable cause<sup>[10]</sup> or a less stringent test.<sup>[11]</sup> In those situations in which the balance of interests precludes insistence upon "some quantum <span class="star-pagination">*655</span> of individualized suspicion,"<sup>[12]</sup> other safeguards are generally relied upon to assure that the individual's reasonable expectation of privacy is not "subject to the discretion of the official in the field," <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>. See <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San..."><i>id.,</i> at 534-535</a></span>; <i>Marshall</i> v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#320" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>Barlow's, Inc., supra,</i> at 320-321</a></span>; <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#322" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 322-323</a></span> (1972) (requiring warrants).</p>
<p>In this case, however, the State of Delaware urges that patrol officers be subject to no constraints in deciding which automobiles shall be stopped for a license and registration check because the State's interest in discretionary spot checks as a means of ensuring the safety of its roadways outweighs the resulting intrusion on the privacy and security of the persons detained.</p>
<p></p>
<h2>IV</h2>
<p>We have only recently considered the legality of investigative stops of automobiles where the officers making the stop have neither probable cause to believe nor reasonable suspicion that either the automobile or its occupants are subject to seizure under the applicable criminal laws. In <i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce, supra</a></span></i><i>,</i> Border Patrol agents conducting roving patrols in areas near the international border asserted statutory authority to stop at random any vehicle in order to determine whether it contained illegal aliens or was involved in smuggling operations. The practice was held to violate the Fourth Amendment, but the Court did not invalidate all warrantless automobile stops upon less than probable cause. Given "the importance of the governmental interest at stake, the minimal intrusion of a brief stop, and the absence of practical alternatives for policing the border," <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#881" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 881</a></span>, the Court analogized the roving-patrol stop to the on-the-street encounter addressed in <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> and held:</p>
<blockquote>"Except at the border and its functional equivalents, officers on roving patrol may stop vehicles only if they are <span class="star-pagination">*656</span> aware of specific articulable facts, together with rational inferences from those facts, that reasonably warrant suspicion that the vehicles contain aliens who may be illegally in the country." <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 884</a></span> (footnote omitted).</blockquote>
<p>Because "the nature of illegal alien traffic and the characteristics of smuggling operations tend to generate articulable grounds for identifying violators," <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>id.,</i> at 883</a></span>, "a requirement of reasonable suspicion for stops allows the Government adequate means of guarding the public interest and also protects residents of the border areas from indiscriminate official interference." <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Ibid.</a></span></i></p>
<p>The constitutionality of stops by Border Patrol agents was again before the Court in <i>United States</i> v. <i><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">Martinez-Fuerte, supra</a></span></i><i>,</i> in which we addressed the permissibility of checkpoint operations. This practice involved slowing all oncoming traffic "to a virtual, if not a complete, halt," <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#546" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 546</a></span>, at a highway roadblock, and referring vehicles chosen at the discretion of Border Patrol agents to an area for secondary inspection. See <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#546" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>id.,</i> at 546, 558</a></span>. Recognizing that the governmental interest involved was the same as that furthered by roving-patrol stops, the Court nonetheless sustained the constitutionality of the Border Patrol's checkpoint operations. The crucial distinction was the lesser intrusion upon the motorist's Fourth Amendment interests:</p>
<blockquote>"[The] objective intrusionthe stop itself, the questioning, and the visual inspectionalso existed in roving-patrol stops. But we view checkpoint stops in a different light because the subjective intrusionthe generating of concern or even fright on the part of lawful travelersis appreciably less in the case of a checkpoint stop." <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Id.,</i> at 558</a></span>.</blockquote>
<p>Although not dispositive,<sup>[13]</sup> these decisions undoubtedly provide <span class="star-pagination">*657</span> guidance in balancing the public interest against the individual's Fourth Amendment interests implicated by the practice of spot checks such as occurred in this case. We cannot agree that stopping or detaining a vehicle on an ordinary city street is less intrusive than a roving-patrol stop on a major highway and that it bears greater resemblance to a permissible stop and secondary detention at a checkpoint near the border. In this regard, we note that <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> was not limited to roving-patrol stops on limited-access roads, but applied to any roving-patrol stop by Border Patrol agents on any type of roadway on less than reasonable suspicion. See <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 882-883</a></span>; <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#894" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 894</a></span> (1975). We cannot assume that the physical and psychological intrusion visited upon the occupants of a vehicle by a random stop to check documents is of any less moment than that occasioned by a stop by border agents on roving patrol. Both of these stops generally entail law enforcement officers signaling a moving automobile to pull over to the side of the roadway, by means of a possibly unsettling show of authority. Both interfere with freedom of movement, are inconvenient, and consume time. Both may create substantial anxiety. For Fourth Amendment purposes, we also see insufficient resemblance between sporadic and random stops of individual vehicles making their way through city traffic and those stops occasioned by roadblocks where all vehicles are brought to a halt or to a near halt, and all are subjected to a show of the police power of the community. "At traffic checkpoints the motorist can see that other vehicles are being stopped, he can see visible signs of the officers' authority, and he is much less likely to be frightened or annoyed by the intrusion." <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#894" aria-description="Citation for case: United States v. Ortiz"><i>Id.,</i> at 894-895</a></span>, quoted in <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 558</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*658</span> V</h2>
<p>But the State of Delaware urges that even if discretionary spot checks such as occurred in this case intrude upon motorists as much as or more than do the roving patrols held impermissible in <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span>,</i> these stops are reasonable under the Fourth Amendment because the State's interest in the practice as a means of promoting public safety upon its roads more than outweighs the intrusion entailed. Although the record discloses no statistics concerning the extent of the problem of lack of highway safety, in Delaware or in the Nation as a whole, we are aware of the danger to life<sup>[14]</sup> and property posed by vehicular traffic and of the difficulties that even a cautious and an experienced driver may encounter. We agree that the States have a vital interest in ensuring that only those qualified to do so are permitted to operate motor vehicles, that these vehicles are fit for safe operation, and hence that licensing, registration, and vehicle inspection requirements are being observed. Automobile licenses are issued periodically to evidence that the drivers holding them are sufficiently familiar with the rules of the road and are physically qualified to operate a motor vehicle.<sup>[15]</sup> The registration requirement and, more pointedly, the related annual inspection requirement in Delaware<sup>[16]</sup> are designed to keep dangerous automobiles off the road. Unquestionably, these provisions, properly administered, are essential elements in a highway safety program. Furthermore, we note that the State of Delaware requires a minimum amount of insurance <span class="star-pagination">*659</span> coverage as a condition to automobile registration,<sup>[17]</sup> implementing its legitimate interest in seeing to it that its citizens have protection when involved in a motor vehicle accident.<sup>[18]</sup></p>
<p>The question remains, however, whether in the service of these important ends the discretionary spot check is a sufficiently productive mechanism to justify the intrusion upon Fourth Amendment interests which such stops entail. On the record before us, that question must be answered in the negative. Given the alternative mechanisms available, both those in use and those that might be adopted, we are unconvinced that the incremental contribution to highway safety of the random spot check justifies the practice under the Fourth Amendment.</p>
<p>The foremost method of enforcing traffic and vehicle safety regulations, it must be recalled, is acting upon observed violations. Vehicle stops for traffic violations occur countless times each day; and on these occasions, licenses and registration papers are subject to inspection and drivers without them will be ascertained. Furthermore, drivers without licenses are presumably the less safe drivers whose propensities may well exhibit themselves.<sup>[19]</sup> Absent some empirical data to the contrary, it must be assumed that finding an unlicensed driver among those who commit traffic violations is a much more likely event than finding an unlicensed driver by choosing randomly from the entire universe of drivers. If this were not so, licensing of drivers would hardly be an effective means of promoting roadway safety. It seems common sense that the <span class="star-pagination">*660</span> percentage of all drivers on the road who are driving without a license is very small and that the number of licensed drivers who will be stopped in order to find one unlicensed operator will be large indeed. The contribution to highway safety made by discretionary stops selected from among drivers generally will therefore be marginal at best. Furthermore, and again absent something more than mere assertion to the contrary, we find it difficult to believe that the unlicensed driver would not be deterred by the possibility of being involved in a traffic violation or having some other experience calling for proof of his entitlement to drive but that he would be deterred by the possibility that he would be one of those chosen for a spot check. In terms of actually discovering unlicensed drivers or deterring them from driving, the spot check does not appear sufficiently productive to qualify as a reasonable law enforcement practice under the Fourth Amendment.</p>
<p>Much the same can be said about the safety aspects of automobiles as distinguished from drivers. Many violations of minimum vehicle-safety requirements are observable, and something can be done about them by the observing officer, directly and immediately. Furthermore, in Delaware, as elsewhere, vehicles must carry and display current license plates,<sup>[20]</sup> which themselves evidence that the vehicle is properly registered;<sup>[21]</sup> and, under Delaware law, to qualify for annual registration a vehicle must pass the annual safety inspection<sup>[22]</sup> and be properly insured.<sup>[23]</sup> It does not appear, therefore, that a stop of a Delaware-registered vehicle is necessary in order to ascertain compliance with the State's registration requirements; and, because there is nothing to <span class="star-pagination">*661</span> show that a significant percentage of automobiles from other States do not also require license plates indicating current registration, there is no basis for concluding that stopping even out-of-state cars for document checks substantially promotes the State's interest.</p>
<p>The marginal contribution to roadway safety possibly resulting from a system of spot checks cannot justify subjecting every occupant of every vehicle on the roads to a seizure limited in magnitude compared to other intrusions but nonetheless constitutionally cognizableat the unbridled discretion of law enforcement officials. To insist neither upon an appropriate factual basis for suspicion directed at a particular automobile nor upon some other substantial and objective standard or rule to govern the exercise of discretion "would invite intrusions upon constitutionally guaranteed rights based on nothing more substantial than inarticulate hunches . . . ." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 22</a></span>. By hypothesis, stopping apparently safe drivers is necessary only because the danger presented by some drivers is not observable at the time of the stop. When there is not probable cause to believe that a driver is violating any one of the multitude of applicable traffic and equipment regulations<sup>[24]</sup>or other articulable basis amounting to reasonable suspicion that the driver is unlicensed or his vehicle unregisteredwe cannot conceive of any legitimate basis upon which a patrolman could decide that stopping a particular driver for a spot check would be more productive than stopping any other driver. This kind of standardless and unconstrained discretion is the evil the Court has discerned when in previous cases it has insisted that the discretion of the official in the field be circumscribed, at least to some extent. <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#270" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 270</a></span> (1973); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532-533</a></span>.</p>
<p></p>
<h2>
<span class="star-pagination">*662</span> VI</h2>
<p>The "grave danger" of abuse of discretion, <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#559" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 559</a></span>, does not disappear simply because the automobile is subject to state regulation resulting in numerous instances of police-citizen contact, <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 441</a></span> (1973). Only last Term we pointed out that "if the government intrudes . . . the privacy interest suffers whether the government's motivation is to investigate violations of criminal laws or breaches of other statutory or regulatory standards." <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#312" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S., at 312-313</a></span>. There are certain "relatively unique circumstances," <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#313" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>id.,</i> at 313</a></span>, in which consent to regulatory restrictions is presumptively concurrent with participation in the regulated enterprise. See <i>United States</i> v. <i>Biswell,</i> <span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972) (federal regulation of firearms); <i>Colonnade Catering Corp.</i> v. <i>United States,</i> <span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970) (federal regulation of liquor). Otherwise, regulatory inspections unaccompanied by any quantum of individualized, articulable suspicion must be undertaken pursuant to previously specified "neutral criteria." <i>Marshall</i> v. <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#323" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc."><i>Barlow's, Inc., supra,</i> at 323</a></span>.</p>
<p>An individual operating or traveling in an automobile does not lose all reasonable expectation of privacy simply because the automobile and its use are subject to government regulation.<sup>[25]</sup> Automobile travel is a basic, pervasive, and often necessary mode of transportation to and from one's home, workplace, and leisure activities. Many people spend more hours each day traveling in cars than walking on the streets. Undoubtedly, many find a greater sense of security and privacy in traveling in an automobile than they do in exposing themselves by pedestrian or other modes of travel. Were the <span class="star-pagination">*663</span> individual subject to unfettered governmental intrusion every time he entered an automobile, the security guaranteed by the Fourth Amendment would be seriously circumscribed. As <i>Terry</i> v. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio, supra</a></span></i><i>,</i> recognized, people are not shorn of all Fourth Amendment protection when they step from their homes onto the public sidewalks. Nor are they shorn of those interests when they step from the sidewalks into their automobiles. See <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/#146" aria-description="Citation for case: Adams v. Williams">407 U. S. 143, 146</a></span> (1972).</p>
<p></p>
<h2>VII</h2>
<p>Accordingly, we hold that except in those situations in which there is at least articulable and reasonable suspicion that a motorist is unlicensed or that an automobile is not registered, or that either the vehicle or an occupant is otherwise subject to seizure for violation of law, stopping an automobile and detaining the driver in order to check his driver's license and the registration of the automobile are unreasonable under the Fourth Amendment. This holding does not preclude the State of Delaware or other States from developing methods for spot checks that involve less intrusion or that do not involve the unconstrained exercise of discretion.<sup>[26]</sup> Questioning of all oncoming traffic at roadblock-type stops is one possible alternative. We hold only that persons in automobiles on public roadways may not for that reason alone have their travel and privacy interfered with at the unbridled discretion of police officers. The judgment below is affirmed.</p>
<p><i>So ordered.</i></p>
<p>MR. JUSTICE BLACKMUN, with whom MR. JUSTICE POWELL joins, concurring.</p>
<p>The Court, <i>ante,</i> this page, carefully protects from the reach of its decision other less intrusive spot checks "that do not involve <span class="star-pagination">*664</span> the unconstrained exercise of discretion." The roadblock stop for all traffic is given as an example. I necessarily assume that the Court's reservation also includes other not purely random stops (such as every 10th car to pass a given point) that equate with, but are less intrusive than, a 100% roadblock stop. And I would not regard the present case as a precedent that throws any constitutional shadow upon the necessarily somewhat individualized and perhaps largely random examinations by game wardens in the performance of their duties. In a situation of that type, it seems to me, the Court's balancing process, and the value factors under consideration, would be quite different.</p>
<p>With this understanding, I join the Court's opinion and its judgment.</p>
<p>MR. JUSTICE REHNQUIST, dissenting.</p>
<p>The Court holds, in successive sentences, that absent an articulable, reasonable suspicion of unlawful conduct, a motorist may not be subjected to a random license check, but that the States are free to develop "methods for spot checks that . . . do not involve the unconstrained exercise of discretion," such as "[q]uestioning . . . all oncoming traffic at road-block-type stops . . . ." <i>Ante,</i> at 663. Because motorists, apparently like sheep, are much less likely to be "frightened" or "annoyed" when stopped en masse, a highway patrolman needs neither probable cause nor articulable suspicion to stop <i>all</i> motorists on a particular thoroughfare, but he cannot without articulable suspicion stop <i>less</i> than all motorists. The Court thus elevates the adage "misery loves company" to a novel role in Fourth Amendment jurisprudence. The rule becomes "curiouser and curiouser" as one attempts to follow the Court's explanation for it.</p>
<p>As the Court correctly points out, people are not shorn of their Fourth Amendment protection when they step from their homes onto the public sidewalks or from the sidewalks into <span class="star-pagination">*665</span> their automobiles. But a random license check of a motorist operating a vehicle on highways owned and maintained by the State is quite different from a random stop designed to uncover violations of laws that have nothing to do with motor vehicles.<sup>[*]</sup> No one questions that the State may require the licensing of those who drive on its highways and the registration of vehicles which are driven on those highways. If it may insist on these requirements, it obviously may take steps necessary to enforce compliance. The reasonableness of the enforcement measure chosen by the State is tested by weighing its intrusion on the motorists' Fourth Amendment interests against its promotion of the State's legitimate interests. <i>E. g., </i><i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975).</p>
<p>In executing this balancing process, the Court concludes that given the alternative mechanisms available, discretionary spot checks are not a "sufficiently productive mechanism" to safeguard the State's admittedly "vital interest in ensuring that only those qualified to do so are permitted to operate motor vehicles, that these vehicles are fit for safe operation, and hence that licensing, registration, and vehicle inspection requirements are being observed." <i>Ante,</i> at 659, 658. Foremost among the alternative methods of enforcing traffic and vehicle <span class="star-pagination">*666</span> safety regulations, according to the Court, is acting upon observed violations, for "drivers without licenses are presumably the less safe drivers whose propensities may well exhibit themselves." <i>Ante,</i> at 659. Noting that "finding an unlicensed driver among those who commit traffic violations is a much more likely event than finding an unlicensed driver by choosing randomly from the entire universe of drivers," <i>ibid.,</i> the Court concludes that the contribution to highway safety made by random stops would be marginal at best. The State's primary interest, however, is in traffic safety, not in apprehending unlicensed motorists for the sake of apprehending unlicensed motorists. The whole point of enforcing motor vehicle safety regulations is to remove from the road the unlicensed driver before he demonstrates why he is unlicensed. The Court would apparently prefer that the State check licenses and vehicle registrations as the wreckage is being towed away.</p>
<p>Nor is the Court impressed with the deterrence rationale, finding it inconceivable that an unlicensed driver who is not deterred by the prospect of being involved in a traffic violation or other incident requiring him to produce a license would be deterred by the possibility of being subjected to a spot check. The Court arrives at its conclusion without the benefit of a shred of empirical data in this record suggesting that a system of random spot checks would fail to deter violators. In the absence of such evidence, the State's determination that random stops would serve a deterrence function should stand.</p>
<p>On the other side of the balance, the Court advances only the most diaphanous of citizen interests. Indeed, the Court does not say that these interests can never be infringed by the State, just that the State must infringe them en masse rather than citizen by citizen. To comply with the Fourth Amendment, the State need only subject <i>all</i> citizens to the same "anxiety" and "inconvenien[ce]" to which it now subjects only a few.</p>
<p><span class="star-pagination">*667</span> For constitutional purposes, the action of an individual law enforcement officer is the action of the State itself, <i>e. g., </i><i>Ex parte Virginia,</i> <span class="citation" data-id="90041"><a href="/opinion/90041/ex-parte-virginia/#346" aria-description="Citation for case: Ex Parte Virginia">100 U. S. 339, 346-347</a></span> (1880), and state acts are accompanied by a presumption of validity until shown otherwise. See, <i>e. g., </i><i>McDonald</i> v. <i>Board of Election,</i> <span class="citation" data-id="107917"><a href="/opinion/107917/mcdonald-v-board-of-election-commrs-of-chicago/" aria-description="Citation for case: McDonald v. Board of Election Comm&#x27;rs of Chicago">394 U. S. 802</a></span> (1969). Although a system of discretionary stops could conceivably be abused, the record before us contains no showing that such abuse is probable or even likely. Nor is there evidence in the record that a system of random license checks would fail adequately to further the State's interest in deterring and apprehending violators. Nevertheless, the Court concludes "[o]n the record before us" that the random spot check is not "a sufficiently productive mechanism to justify the intrusion upon Fourth Amendment interests which such stops entail." <i>Ante,</i> at 659. I think that the Court's approach reverses the presumption of constitutionality accorded acts of the States. The burden is not upon the State to demonstrate that its procedures are consistent with the Fourth Amendment, but upon respondent to demonstrate that they are not. "On this record" respondent has failed to make such a demonstration.</p>
<p>Neither the Court's opinion, nor the opinion of the Supreme Court of Delaware, suggests that the random stop made in this case was carried out in a manner inconsistent with the Equal Protection Clause of the Fourteenth Amendment. Absent an equal protection violation, the fact that random stops may entail "a possibly unsettling show of authority," <i>ante,</i> at 657, and "may create substantial anxiety," <i>ibid.,</i> seems an insufficient basis to distinguish for Fourth Amendment purposes between a roadblock stopping all cars and the random stop at issue here. Accordingly, I would reverse the judgment of the Supreme Court of Delaware.</p>
<h2>NOTES</h2>
<p>[*]  <i>Frank Carrington, Wayne W. Schmidt, Glen R. Murphy,</i> and <i>James P. Costello</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  In its opinion, the Delaware Supreme Court referred to respondent as the operator of the vehicle, see <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1361" aria-description="Citation for case: State v. Prouse">382 A. 2d 1359, 1361</a></span> (1978). However, the arresting officer testified: "I don't believe [respondent] was the driver. . . . As I recall, he was in the back seat . . . ," App. A12; and the trial court in its ruling on the motion to suppress referred to respondent as one of the four "occupants" of the vehicle, <i><span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/" aria-description="Citation for case: State v. Prouse">id.,</a></span></i> at A17. The vehicle was registered to respondent. <i><span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/" aria-description="Citation for case: State v. Prouse">Id.,</a></span></i> at A10.</p>
<p>[2]  <i>United States</i> v. <i>Montgomery,</i> 182 U. S. App. D. C. 426, <span class="citation" data-id="9464098"><a href="/opinion/348709/united-states-v-kevin-l-montgomery/" aria-description="Citation for case: United States v. Kevin L. Montgomery">561 F. 2d 875</a></span> (1977); <i>People</i> v. <i>Ingle,</i> 36 N. Y. 2d 413, <span class="citation" data-id="5529536"><a href="/opinion/5681169/people-v-ingle/" aria-description="Citation for case: People v. Ingle">330 N. E. 2d 39</a></span> (1975); <i>State</i> v. <i>Ochoa,</i> <span class="citation" data-id="9553424"><a href="/opinion/1190270/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">23 Ariz. App. 510</a></span>, <span class="citation" data-id="9553424"><a href="/opinion/1190270/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">534 P. 2d 441</a></span> (1975), rev'd on other grounds, <span class="citation" data-id="9604044"><a href="/opinion/1367261/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">112 Ariz. 582</a></span>, <span class="citation" data-id="9604044"><a href="/opinion/1367261/state-v-ochoa/" aria-description="Citation for case: State v. Ochoa">544 P. 2d 1097</a></span> (1976); <i>Commonwealth</i> v. <i>Swanger,</i> <span class="citation" data-id="1518042"><a href="/opinion/1518042/commonwealth-v-swanger/" aria-description="Citation for case: Commonwealth v. Swanger">453 Pa. 107</a></span>, <span class="citation" data-id="1518042"><a href="/opinion/1518042/commonwealth-v-swanger/" aria-description="Citation for case: Commonwealth v. Swanger">307 A. 2d 875</a></span> (1973); <i>United States</i> v. <i>Nicholas,</i> <span class="citation" data-id="299088"><a href="/opinion/299088/united-states-v-george-willie-nicholas-jr/" aria-description="Citation for case: United States v. George Willie Nicholas, Jr.">448 F. 2d 622</a></span> (CA8 1971). See also <i>United States</i> v. <i>Cupps,</i> <span class="citation" data-id="321729"><a href="/opinion/321729/united-states-v-hoyt-cupps-jr/" aria-description="Citation for case: United States v. Hoyt Cupps, Jr.">503 F. 2d 277</a></span> (CA6 1974).</p>
<p>[3]  <i>State</i> v. <i>Holmberg,</i> <span class="citation" data-id="9670456"><a href="/opinion/1701839/state-v-holmberg/" aria-description="Citation for case: State v. Holmberg">194 Neb. 337</a></span>, <span class="citation" data-id="9670456"><a href="/opinion/1701839/state-v-holmberg/" aria-description="Citation for case: State v. Holmberg">231 N. W. 2d 672</a></span> (1975); <i>State</i> v. <i>Allen,</i> <span class="citation" data-id="1332651"><a href="/opinion/1332651/state-v-allen/" aria-description="Citation for case: State v. Allen">282 N. C. 503</a></span>, <span class="citation" data-id="1332651"><a href="/opinion/1332651/state-v-allen/" aria-description="Citation for case: State v. Allen">194 S. E. 2d 9</a></span> (1973); <i>Palmore</i> v. <i>United States,</i> <span class="citation" data-id="2378216"><a href="/opinion/2378216/palmore-v-united-states/" aria-description="Citation for case: Palmore v. United States">290 A. 2d 573</a></span> (D. C. App. 1972), aff'd on jurisdictional grounds only, <span class="citation" data-id="9425255"><a href="/opinion/108767/palmore-v-united-states/" aria-description="Citation for case: Palmore v. United States">411 U. S. 389</a></span> (1973); <i>Leonard</i> v. <i>State,</i> <span class="citation" data-id="1778812"><a href="/opinion/1778812/leonard-v-state-of-texas/" aria-description="Citation for case: Leonard v. State of Texas">496 S. W. 2d 576</a></span> (Tex. Crim. App. 1973); <i>United States</i> v. <i>Jenkins,</i> <span class="citation" data-id="332182"><a href="/opinion/332182/united-states-v-james-jenkins-jr/" aria-description="Citation for case: United States v. James Jenkins, Jr.">528 F. 2d 713</a></span> (CA10 1975); <i>Myricks</i> v. <i>United States,</i> <span class="citation" data-id="274285"><a href="/opinion/274285/charles-james-myricks-v-united-states/" aria-description="Citation for case: Charles James Myricks v. United States">370 F. 2d 901</a></span> (CA5), cert. dismissed, <span class="citation multiple-matches"><a href="/c/U.%20S./386/1015/">386 U. S. 1015</a></span> (1967).</p>
<p>[4]  The court stated:
</p>
<p>"The Delaware Constitution Article I, § 6 is substantially similar to the Fourth Amendment and a violation of the latter is necessarily a violation of the former." <span class="citation" data-id="1442373"><a href="/opinion/1442373/state-v-prouse/#1362" aria-description="Citation for case: State v. Prouse">382 A. 2d, at 1362</a></span>, citing <i>State</i> v. <i>Moore,</i> <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">55 Del. 356</a></span>, <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">187 A. 2d 807</a></span> (1963).</p>
<p><i>Moore</i> was decided less than two years after <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), applied to the States the limitations previously imposed only on the Federal Government. In setting forth the approach reiterated in the opinion below, <i><span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">Moore</a></span></i> noted not only the common purposes and wording of the Fourth Amendment and the state constitutional provision, but also the overriding effect of the former. See <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/#362" aria-description="Citation for case: State v. Moore">55 Del., at 362-363</a></span>, <span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/#810" aria-description="Citation for case: State v. Moore">187 A. 2d, at 810-811</a></span>.</p>
<p>[5]  We have found only one case decided after <i>State</i> v. <i><span class="citation" data-id="2354841"><a href="/opinion/2354841/state-v-moore/" aria-description="Citation for case: State v. Moore">Moore, supra</a></span></i><i>,</i> in which the court relied solely on state law in upholding the validity of a search or seizure, and that case involved not only Del. Const. Art. I, § 6, but also state statutory requirements for issuance of a search warrant. <i>Rossitto</i> v. <i>State,</i> <span class="citation" data-id="2170567"><a href="/opinion/2170567/rossitto-v-state/" aria-description="Citation for case: Rossitto v. State">234 A. 2d 438</a></span> (1967). Moreover, every case holding a search or seizure to be contrary to the state constitutional provision relies on cases interpreting the Fourth Amendment and simultaneously concludes that the search or seizure is contrary to that provision. See, <i>e. g., </i><i>Young</i> v. <i>State,</i> <span class="citation" data-id="1893463"><a href="/opinion/1893463/young-v-state/" aria-description="Citation for case: Young v. State">339 A. 2d 723</a></span> (1975); <i>Freeman</i> v. <i>State,</i> <span class="citation" data-id="1500552"><a href="/opinion/1500552/freeman-v-state/" aria-description="Citation for case: Freeman v. State">317 A. 2d 540</a></span> (1974); cf. <i>Bertomeu</i> v. <i>State,</i> <span class="citation" data-id="1471204"><a href="/opinion/1471204/bertomeu-v-state/" aria-description="Citation for case: Bertomeu v. State">310 A. 2d 865</a></span> (1973).</p>
<p>[6]  See <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#315" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 315</a></span> (1978); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 439</a></span> (1973); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#539" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 539</a></span> (1967).</p>
<p>[7]  See also <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#554" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 554</a></span> (1976); <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#895" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 895</a></span> (1975); <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#270" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 270</a></span> (1973); <i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#97" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 97</a></span> (1964); <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#455" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 455-456</a></span> (1948).</p>
<p>[8]  See, <i>e. g., </i><i>United States</i> v. <i>Ramsey,</i> <span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/#616" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606, 616-619</a></span> (1977); <i>United States</i> v. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 555</a></span>; cases cited in n. 6, <i>supra.</i></p>
<p>[9]  <i>Terry</i> v. <i>Ohio, supra,</i> at 21. See also <i>Scott</i> v. <i>United States,</i> <span class="citation" data-id="9427183"><a href="/opinion/109860/scott-v-united-states/#137" aria-description="Citation for case: Scott v. United States">436 U. S. 128, 137</a></span> (1978); <i>Beck</i> v. <i>Ohio, supra,</i> at 96-97.</p>
<p>[10]  See, <i>e. g., </i><i>United States</i> v. <i>Santana,</i> <span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">427 U. S. 38</a></span> (1976); <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963) (warrantless arrests requiring probable cause); <i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra</a></span></i><i>; </i><i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925) (warrantless searches requiring probable cause). See also <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975).</p>
<p>[11]  See <i>Terry</i> v. <i>Ohio, supra</i><i>; </i><i>United States</i> v. <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce, supra</a></span></i><i>.</i>
</p>
<p>In addition, the Warrant Clause of the Fourth Amendment generally requires that prior to a search a neutral and detached magistrate ascertain that the requisite standard is met, see, <i>e. g., </i><i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978).</p>
<p>[12]  <i>United States</i> v. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#560" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 560</a></span>.</p>
<p>[13]  In addressing the constitutionality of Border Patrol practices, we reserved the question of the permissibility of state and local officials stopping motorists for document questioning in a manner similar to checkpoint detention, see <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S., at 560</a></span> n. 14, or roving-patrol operations, see <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 883</a></span> n. 8.</p>
<p>[14]  In 1977, 47,671 persons died in motor vehicle accidents in this country. U. S. Dept. of Transportation, Highway Safety A-9 (1977).</p>
<p>[15]  See, <i>e. g.,</i> Del. Code Ann., Tit. 21, §§ 2701, 2707 (1974 and Supp. 1977); § 2713 (1974) (Department of Public Safety "shall examine the applicant as to his physical and mental qualifications to operate a motor vehicle in such manner as not to jeopardize the safety of persons or property . . .").</p>
<p>[16]  § 2143 (a) (1974).</p>
<p>[17]  § 2118 (Supp. 1977); State of Delaware, Department of Public Safety, Division of Motor Vehicles, Driver's Manual 60 (1976).</p>
<p>[18]  It has been urged that additional state interests are the apprehension of stolen motor vehicles and of drivers under the influence of alcohol or narcotics. The latter interest is subsumed by the interest in roadway safety, as may be the former interest to some extent. The remaining governmental interest in controlling automobile thefts is not distinguishable from the general interest in crime control.</p>
<p>[19]  Cf. <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 883</a></span>.</p>
<p>[20]  Del. Code Ann., Tit. 21, § 2126 (1974).</p>
<p>[21]  §§ 2121 (b), (d) (1974).</p>
<p>[22]  See n. 16, <i>supra;</i> § 2109 (1974).</p>
<p>[23]  See n. 17, <i>supra;</i> § 2109 (1974).</p>
<p>[24]  See, <i>e. g.,</i> §§ 4101-4199B (1974 and Supp. 1977).</p>
<p>[25]  Cf. <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978) (warrant required for federal inspection under interstate commerce power of health and safety of workplace); <i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967) (warrant required for inspection of warehouse for municipal fire code violations); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967) (warrant required for inspection of residence for municipal fire code violations).</p>
<p>[26]  Nor does our holding today cast doubt on the permissibility of roadside truck weigh-stations and inspection checkpoints, at which some vehicles may be subject to further detention for safety and regulatory inspection than are others.</p>
<p>[*]  Indeed, this distinction was expressly recognized in <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span>, 883 n. 8 (1975):
</p>
<p>"Our decision in this case takes into account the special function of the Border Patrol, the importance of the governmental interests in policing the border area, the character of roving-patrol stops, and the availability of alternatives to random stops unsupported by reasonable suspicion. Border Patrol agents have no part in enforcing laws that regulate highway use, and their activities have nothing to do with an inquiry whether motorists and their vehicles are entitled, by virtue of compliance with laws governing highway usage, to be upon the public highways. Our decision thus does not imply that state and local enforcement agencies are without power to conduct such limited stops as are necessary to enforce laws regarding drivers' licenses, vehicle registration, truck weights, and similar matters."</p>

</div>
```

---
