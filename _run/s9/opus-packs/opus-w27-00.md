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

## GROUP: content/cases/Beecher v. Alabama.md  (`case`, 5 assertions)

### content_page

```
---
title: "Beecher v. Alabama"
type: case
citation: "389 U.S. 35 (1967)"
parallel_cite: "88 S. Ct. 189; 19 L. Ed. 2d 35"
neutral_cite: 1967 U.S. LEXIS 435
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-10-23
docket: 92 Misc.
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-10-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Beecher v. Alabama
  varies_by_point: false
  scope_note: "Good law; per curiam. A confession extracted at gunpoint from a wounded suspect, and a later statement signed while drugged and in intense pain, are the product of gross coercion and involuntary."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107526/beecher-v-alabama/"
  cluster_id: 107526
  opinion_id: 9423505
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Townsend v. Sain]]", "[[Malloy v. Hogan]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "coercion", "per-curiam"]
holding: "A confession obtained at gunpoint from a wounded suspect threatened with death, and a second statement signed five days later while drugged on morphine and in intense pain with no break in the stream of events, are the product of gross coercion and involuntary; no conviction tainted by such a confession can stand."
lake:
  record_id: Beecher v. Alabama
  status: under_review
  projected_at: 2026-07-06
---

# Beecher v. Alabama

*389 U.S. 35 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Beecher, a state convict, escaped from a road gang; a woman's body was found nearby and he was charged with first-degree murder. Captured in Tennessee, he was shot in the right leg by police as he fled. While he lay wounded, the local Chief of Police pressed a loaded gun to his face and another officer pointed a rifle at his head; the Chief said, "If you don't tell the truth I am going to kill you," the second officer fired his rifle next to his ear, and Beecher immediately confessed. Five days later, in the prison hospital — his leg so infected it was later amputated, feverish, in intense pain, and in a "kind of slumber" from a morphine injection — two Alabama investigators prepared two detailed statements and he signed them. Both confessions were admitted at the trial that sentenced him to death.

## Issue
Whether confessions obtained at gunpoint from a wounded suspect, and re-obtained days later while he was drugged and in severe pain, were voluntary under the Due Process Clause.

## Rule
No — they were the product of gross coercion. "A realistic appraisal of the circumstances of *this* case compels the conclusion that this petitioner's confessions were the product of gross coercion. Under the Due Process Clause of the Fourteenth Amendment, no conviction tainted by a confession so obtained can stand." — 389 U.S. at 38. ^pin-38

The two confessions were a single coercive episode: from the gunpoint confession "until he was directed five days later to tell Alabama investigators 'what they wanted to know,' there was 'no break in the stream of events,'" because he remained "in pain, under the influence of drugs, and at the complete mercy of the prison hospital authorities." — *Id.* ^pin-38a

## Application
The uncontradicted facts compelled the conclusion of involuntariness even accepting the State's version of the hospital encounter. Beecher, "already wounded by the police, was ordered at gunpoint to speak his guilt or be killed"; the second set of statements followed without any break while he was feverish, in intense pain, and under morphine at the mercy of his custodians. Because his death sentence rested on confessions so obtained, the conviction could not stand.

## Conclusion
The confessions were the product of gross coercion and involuntary; [[Reading and Citing Cases#certiorari-cert|certiorari]] was granted and the judgment reversed. (Justice Black concurred in the reversal on Fifth-Amendment self-incrimination grounds under [[Malloy v. Hogan]].)

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Beecher* sits in the due-process coercion line anchored by [[Brown v. Mississippi]] and [[Chambers v. Florida]]; its drugged-and-in-pain branch parallels the drug-induced involuntariness of [[Townsend v. Sain]]. (A later [[Common Legal Terms#per-curiam|per curiam]], *Beecher v. Alabama*, 408 U.S. 234 (1972), again reversed after a retrial; this page concerns the 1967 decision.)

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Beecher v. Alabama*, 389 U.S. 35 (1967) (per curiam) — https://www.courtlistener.com/opinion/107526/beecher-v-alabama/ — pinpoints: 36–38.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "bc2532cccbdf7aee", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "389 U.S. 35 (1967)", "court": "U.S. Supreme Court", "neutral_cite": "1967 U.S. LEXIS 435", "official_citation_present": true, "parallel_cite": "88 S. Ct. 189; 19 L. Ed. 2d 35", "title": "Beecher v. Alabama", "year": "1967"}}
{"assertion_id": "0fb53d848027d7c6", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Beecher v. Alabama"}}
{"assertion_id": "bdb9da0f436831e5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession obtained at gunpoint from a wounded suspect threatened with death, and a second statement signed five days later while drugged on morphine and in intense pain with no break in the stream of events, are the product of gross coercion and involuntary; no conviction tainted by such a confession can stand.", "title": "Beecher v. Alabama"}}
{"assertion_id": "a8dbe81c84a7c810", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Beecher v. Alabama"}}
{"assertion_id": "db03bd0ebe6e8139", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1967-10-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Beecher v. Alabama", "field_i_validity": "good_law", "scope_note": "Good law; per curiam. A confession extracted at gunpoint from a wounded suspect, and a later statement signed while drugged and in intense pain, are the product of gross coercion and involuntary.", "title": "Beecher v. Alabama", "varies_by_point": "false"}}
```

### lake record — Beecher v. Alabama

```json
{
  "schema_version": "s2.v1",
  "record_id": "Beecher v. Alabama",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Beecher v. Alabama",
    "case_name_short": "Beecher",
    "case_name_full": "Beecher v. Alabama",
    "input_case_name": "Beecher v. Alabama",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-10-23",
    "year": 1967,
    "docket": "92 Misc.",
    "cluster_id": 107526,
    "lead_opinion_id": 9423505,
    "sibling_ids": [
      107526,
      9423505,
      9423506,
      9423507
    ],
    "absolute_url": "/opinion/107526/beecher-v-alabama/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "389 U.S. 35",
      "volume": "389",
      "reporter": "U.S.",
      "page": "35",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 189",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "189",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 35",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "35",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 435",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "435",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "389 U.S. 35",
        "volume": "389",
        "reporter": "U.S.",
        "page": "35",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 189",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "189",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 L. Ed. 2d 35",
        "volume": "19",
        "reporter": "L. Ed. 2d",
        "page": "35",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 435",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "435",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "389 U.S. 35",
    "official_selection": {
      "court_class": "scotus",
      "selected": "389 U.S. 35",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-38",
      "page": null,
      "quote": "from a morphine injection \u2014 two Alabama investigators prepared two detailed statements and he signed them. Both confessions were admitted at the trial that sentenced him to death. ## Issue Whether confessions obtained at gunpoint from a wounded suspect, and re-obtained days later while he was drugged and in severe pain, were voluntary under the Due Process Clause. ## Rule No \u2014 they were the product of gross coercion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-38a",
      "page": null,
      "quote": "until he was directed five days later to tell Alabama investigators 'what they wanted to know,' there was 'no break in the stream of events,'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-10-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Beecher v. Alabama",
    "varies_by_point": false,
    "scope_note": "Good law; per curiam. A confession extracted at gunpoint from a wounded suspect, and a later statement signed while drugged and in intense pain, are the product of gross coercion and involuntary.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Blackmon v. State",
          "cluster_id": 1606057,
          "cite": [
            "7 So. 3d 397",
            "2006 Ala. Crim. App. LEXIS 184",
            "2005 WL 1845273"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "McLeod v. State",
          "cluster_id": 1105770,
          "cite": [
            "718 So. 2d 727",
            "1998 WL 12623"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Burns",
          "cluster_id": 195186,
          "cite": [
            "15 F.3d 211",
            "1994 WL 26989"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Russell v. State",
          "cluster_id": 2467061,
          "cite": [
            "739 S.W.2d 923"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane1_negative"
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
        "journal_ref": "Beecher v. Alabama:lane1_negative"
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
        "journal_ref": "Beecher v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eakes v. State",
          "cluster_id": 1761034,
          "cite": [
            "387 So. 2d 855"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnny Daniel Beecher v. William Baxley, Attorney General of the State of Alabama, and Fred B. Simpson, District Attorney of Madison County, Alabama",
          "cluster_id": 343151,
          "cite": [
            "549 F.2d 974",
            "1977 U.S. App. LEXIS 14064"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Beecher v. State",
          "cluster_id": 1846726,
          "cite": [
            "320 So. 2d 716",
            "56 Ala. App. 212",
            "1974 Ala. Crim. App. LEXIS 1027"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane1_negative"
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
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
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
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
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
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
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
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
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
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
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
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
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
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chavez v. Martinez",
          "cluster_id": 127927,
          "cite": [
            "155 L. Ed. 2d 984",
            "123 S. Ct. 1994",
            "538 U.S. 760",
            "2003 U.S. LEXIS 4274"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harrison v. United States",
          "cluster_id": 107736,
          "cite": [
            "20 L. Ed. 2d 1047",
            "88 S. Ct. 2008",
            "392 U.S. 219",
            "1968 U.S. LEXIS 1349"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Orr v. Orr",
          "cluster_id": 110029,
          "cite": [
            "59 L. Ed. 2d 306",
            "99 S. Ct. 1102",
            "440 U.S. 268",
            "1979 U.S. LEXIS 65"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oursbourn v. State",
          "cluster_id": 2334003,
          "cite": [
            "259 S.W.3d 159",
            "2008 Tex. Crim. App. LEXIS 686",
            "2008 WL 2261744"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Terrazas",
          "cluster_id": 2278739,
          "cite": [
            "4 S.W.3d 720",
            "1999 Tex. Crim. App. LEXIS 93",
            "1999 WL 722548"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boulden v. Holman",
          "cluster_id": 107893,
          "cite": [
            "22 L. Ed. 2d 433",
            "89 S. Ct. 1138",
            "394 U.S. 478",
            "1969 U.S. LEXIS 2045"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 2085422,
          "cite": [
            "692 N.E.2d 1109",
            "181 Ill. 2d 297",
            "229 Ill. Dec. 898",
            "1998 Ill. LEXIS 5"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Mahnke",
          "cluster_id": 2222357,
          "cite": [
            "335 N.E.2d 660",
            "368 Mass. 662",
            "1975 Mass. LEXIS 1032"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Darwin v. Connecticut",
          "cluster_id": 107694,
          "cite": [
            "20 L. Ed. 2d 630",
            "88 S. Ct. 1488",
            "391 U.S. 346",
            "1968 U.S. LEXIS 1634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Martinez",
          "cluster_id": 1136193,
          "cite": [
            "463 P.2d 734",
            "1 Cal. 3d 641",
            "83 Cal. Rptr. 382",
            "1970 Cal. LEXIS 339"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. James Braxton",
          "cluster_id": 740246,
          "cite": [
            "112 F.3d 777",
            "1997 U.S. App. LEXIS 9999",
            "1997 WL 222813"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin Mark Abela v. William Martin, Director, Michigan Department of Corrections",
          "cluster_id": 787456,
          "cite": [
            "380 F.3d 915",
            "2004 U.S. App. LEXIS 18210",
            "2004 WL 1906171"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Price v. State",
          "cluster_id": 1707103,
          "cite": [
            "725 So. 2d 1003",
            "1997 WL 337140"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Honaker",
          "cluster_id": 1350219,
          "cite": [
            "454 S.E.2d 96",
            "193 W. Va. 51",
            "1994 W. Va. LEXIS 242"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Cristobal",
          "cluster_id": 777962,
          "cite": [
            "293 F.3d 134",
            "2002 U.S. App. LEXIS 10736",
            "2002 WL 1211881"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sparks",
          "cluster_id": 2491988,
          "cite": [
            "68 So. 3d 435",
            "2011 WL 1759847"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Beecher v. Alabama:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107526 OR 9423505 OR 9423506 OR 9423507) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 154,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 9,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 154,
        "triage_read": 9,
        "triage_snippet_classified": 145
      },
      "lane2_top_cited": {
        "query": "cites:(107526 OR 9423505 OR 9423506 OR 9423507)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MSZzPTE4NDI0NTAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107526+OR+9423505+OR+9423506+OR+9423507%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107526 OR 9423505 OR 9423506 OR 9423507)",
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
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107526 OR 9423505 OR 9423506 OR 9423507)",
    "indexed_citing_opinions": 177,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107526,
        "count": 164,
        "count_source": "search"
      },
      {
        "opinion_id": 9423505,
        "count": 17,
        "count_source": "search"
      },
      {
        "opinion_id": 9423506,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423507,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 283,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/beecher-v-alabama.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjIzNTE1OTImcz0xNjM4Njc0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107526+OR+9423505+OR+9423506+OR+9423507%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107526,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 102958,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 104440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 105256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 107419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107526,
        "cited_id": 2621051,
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
    "date_created": "2026-07-04T19:33:42Z",
    "date_modified": "2026-07-06T07:19:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T19:34:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T19:34:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T19:39:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T19:34:10Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Beecher v. Alabama

```
<opinion data-order="6" data-type="opinion" id="x999-1" type="majority">
<author id="b145-11">Per Curiam.</author>
<p id="b145-12">On the morning of June 15, 1964, the petitioner, a Negro convict in a state prison, escaped from a road gang in Camp Scottsboro, Alabama. On June 16, a woman’s lifeless body was found not more than a mile from the prison camp. The next day, the petitioner was captured in Tennessee; he was then returned to Jackson County, Alabama, where he was indicted, tried, and convicted on a charge of first degree murder. The jury fixed his punishment at death. After the Supreme Court of Alabama affirmed his conviction, he filed this petition for certiorari, contending that a coerced confession was used <page-number citation-index="1" label="36">*36</page-number>as evidence at his trial, in violation of the Due Process Clause of the Fourteenth Amendment.<footnotemark>1</footnotemark></p>
<p id="b146-6">The uncontradicted facts of record are these. Tennessee police officers saw the petitioner as he fled into an open field and fired a bullet into his right leg. He fell, and the local Chief of Police pressed a loaded gun to his face while another officer pointed a rifle against the side of his head. The Police Chief asked him whether he had raped and killed a white woman. When he said that he had not, the Chief called him a liar and said, “If you don't tell the truth I am going to kill you.” The other officer thep fired his rifle next to the petitioner’s ear, and the petitioner immediately confessed.<footnotemark>2</footnotemark> Later the same day he received an injection to ease the pain in his leg. He signed something the Chief of Police described as “extradition papers” after the officers told him that “it would be best ... to sign the papers before the gang of people came there and killed” him. He was then taken by ambulance from Tennessee to Kilby Prison in Montgomery, Alabama. By June 22, the petitioner’s right leg, which was later amputated, had become so swollen and his wound so painful that he required an injection of morphine every four hours. Less than an hour after one of these injections, two Alabama investigators visited him in the prison hospital. The medical assistant in charge told the petitioner to “cooperate” and, in the petitioner’s presence, he asked the investigators to inform him if the petitioner did not “tell them what they wanted to know.” The medical assistant then left the petitioner alone with the State’s investigators. In the course of a 90-minute “conversation,” the investi<page-number citation-index="1" label="37">*37</page-number>gators prepared two detailed statements similar to the confession the petitioner had given five days earlier at gunpoint in Tennessee. Still in a “kind of slumber” from his last morphine injection, feverish, and in intense pain, the petitioner signed the written confessions thus prepared for him.</p>
<p id="b147-5">These confessions were admitted in evidence over the petitioner’s objection.<footnotemark>3</footnotemark> Although there is some dispute as to precisely what occurred in the petitioner’s room at the prison hospital,<footnotemark>4</footnotemark> we need not resolve this evidentiary <page-number citation-index="1" label="38">*38</page-number>conflict, for even if we accept as accurate the State’s version of what transpired there, the uncontradicted facts set forth above lead to the inescapable conclusion that the petitioner’s confessions were involuntary. See <em>Davis </em>v. <em>North Carolina, </em><span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741-742</a></span>.</p>
<p id="b148-4">The petitioner, already wounded by the police, was ordered at gunpoint to speak his guilt or be killed. From that time until he was directed five days later to tell Alabama investigators “what they wanted to know,” there was “no break in the stream of events,” <em>Clewis </em>v. <em>Texas, </em><span class="citation" data-id="107419"><a href="/opinion/107419/clewis-v-texas/#710" aria-description="Citation for case: Clewis v. Texas">386 U. S. 707, 710</a></span>. For he was then still in pain, under the influence of drugs, and at the complete mercy of the prison hospital authorities. Compare <em>Reck </em>v. <em>Pate, </em><span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span>.</p>
<p id="b148-5">The State says that the facts in this case differ in some respects from those in previous cases where we have held confessions to be involuntary. But constitutional inquiry into the issue of voluntariness “requires more than a mere color-matching of cases,” <em>Reck </em>v. <em>Pate, </em><span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#442" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 442</a></span>. A realistic appraisal of the circumstances of <em>this </em>case compels the conclusion that this petitioner’s confessions were the product of gross coercion. Under the Due Process Clause of the Fourteenth Amendment, no conviction tainted by a confession so obtained can stand.</p>
<p id="b148-6">The motion for leave to proceed <em>in forma pauperis </em>and the petition for certiorari are granted and the judgment is reversed.</p>
<footnote label="1">
<p id="b146-7"> The petitioner also makes other Fourteenth Amendment claims. In light of our disposition of this case, we do not reach them.</p>
</footnote>
<footnote label="2">
<p id="b146-8"> Although this confession was not introduced at trial, its existence is of course vitally relevant to the voluntariness of petitioner’s later statements. See <em>United States </em>v. <em>Bayer, </em><span class="citation" data-id="9420019"><a href="/opinion/104440/united-states-v-bayer/#540" aria-description="Citation for case: United States v. Bayer">331 U. S. 532, 540-541</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b147-6"> Because part of the evidence bearing on the voluntariness of the confessions was introduced in a hearing on the petitioner’s motion for new trial, the State suggests that “[h]is complaint that the confession was improperly admitted now comes too late." That suggestion is clearly untenable. The petitioner objected when the confessions were first introduced; having overruled the objection, the trial court rejected the State’s claim that the issue could not be reviewed on a new trial motion; and the Supreme Court of Alabama found no state procedural bar to reaching the merits of the voluntariness claim and deciding it on the complete record. There can thus be no doubt here that the issue was raised "in [an] appropriate manner,” <em>Brown </em>v. <em>Mississippi, </em><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#286" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 286-287</a></span>. In any event, since the state court deemed the federal constitutional question to be before it, we could not treat the decision below as resting upon an adequate and independent state ground even if we were to conclude that the state court might properly have relied upon such a ground to avoid deciding the federal question. <em>Indiana ex rel. Anderson </em>v. <em>Brand, </em><span class="citation" data-id="9418953"><a href="/opinion/102958/indiana-ex-rel-anderson-v-brand/#98" aria-description="Citation for case: Indiana Ex Rel. Anderson v. Brand">303 U. S. 95, 98</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b147-7"> The investigators claimed at trial that they had told the petitioner, during their 90-minute talk with him, that he was under no obligation to speak and that anything he said could be used against him. One of the investigators stated that he had asked the petitioner whether he wanted an attorney, and had received a negative reply. Although the prepared statements that the petitioner signed refer to no such warnings, and although the conversation in question took place on the date of this Court’s decision in <em>Escobedo </em>v. <em>Illinois, </em><span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, the state courts accepted the investigators’ accounts of that conversation and rejected the petitioner’s contrary testimony as “not at all persuasive.”</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Bell v. Wolfish.md  (`case`, 6 assertions)

### content_page

```
---
title: Bell v. Wolfish
type: case
citation: "441 U.S. 520 (1979)"
parallel_cite: "99 S. Ct. 1861; 60 L. Ed. 2d 447"
neutral_cite: 1979 U.S. LEXIS 100
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-05-14
docket: 77-1829
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
  opinion_url: "https://www.courtlistener.com/opinion/110075/bell-v-wolfish/"
  cluster_id: 110075
  opinion_id: null
  identity_checked: true
lake:
  record_id: Bell v. Wolfish
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Key — Foundational (institutional-deference reasonableness balancing)"
  - page: "[[Inventory Searches]]"
    role: "Related (cross-doctrine)"
related:
  - "[[Florence v. County of Burlington]]"
  - "[[Maryland v. King]]"
  - "[[Illinois v. Lafayette]]"
  - "[[Hudson v. Palmer]]"
  - "[[Safford Unified School District v. Redding]]"
tags:
  - case
  - fourth-amendment
  - jail-search
  - pretrial-detainees
  - institutional-search
  - strip-search
  - reasonableness-balancing
holding: "Pretrial detainees retain Fourth Amendment protection, but the reasonableness of an institutional search is judged by balancing the need for the search against the intrusion it entails — weighing the scope of the intrusion, the manner in which it is conducted, the justification for initiating it, and the place in which it is conducted; on that test, and with deference to jail administrators, the Court upheld the Metropolitan Correctional Center's visual body-cavity inspections after contact visits and its other challenged conditions of pretrial confinement."
---

# Bell v. Wolfish

*441 U.S. 520 (1979)* (No. 77-1829) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the treatment framing below is authored orientation, not machine-certified. Identity cluster 110075 → 441 U.S. 520, No. 77-1829, decided 1979-05-14 (Rehnquist, J.); Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
Pretrial detainees at the federal Metropolitan Correctional Center (MCC) in New York City brought a class action challenging roughly twenty conditions and practices — double-bunking, the "publisher-only" rule on hardcover books, visual body-cavity inspections after contact visits, and searches of living areas outside the detainee's presence, among others. The District Court enjoined many of them, and the Second Circuit largely affirmed, holding under the Due Process Clause that detainees may be subjected only to restrictions that inhere in confinement or are justified by "compelling necessities of jail administration."

## Issue
What constitutional standard governs conditions and search practices imposed on pretrial detainees — and specifically, whether visual body-cavity inspections following contact visits are reasonable under the Fourth Amendment.

## Rule
Writing for the Court, Justice Rehnquist rejected the "compelling necessity" test: a condition that is not imposed as punishment and is reasonably related to a legitimate governmental objective does not offend due process. For the search practices, the Fourth Amendment supplies a balancing standard: "The test of reasonableness under the Fourth Amendment is not capable of precise definition or mechanical application. In each case it requires a balancing of the need for the particular search against the invasion of personal rights that the search entails. Courts must consider the scope of the particular intrusion, the manner in which it is conducted, the justification for initiating it, and the place in which it is conducted." — 441 U.S. at 559. ^pin-559

## Application
Applying that balance, the Court sustained the body-cavity inspections. However significant the intrusion, the security interest in detecting weapons, drugs, and other contraband smuggled in after contact visits was substantial, the inspections were conducted by trained officers in limited circumstances, and courts owe wide-ranging deference to the administrators who run detention facilities. The remaining challenged practices survived under the not-punishment / reasonable-relation standard for the same institutional reasons.

## Conclusion
**Reversed.** Rehnquist, J., wrote for the Court; Marshall, J., and Stevens, J. (joined by Brennan, J.), dissented. The MCC practices were constitutional.

## Treatment & subsequent history
**Good law — foundational.** *Bell v. Wolfish* is the root of the institutional-deference / reasonableness-balancing line for custodial searches. *[[Florence v. County of Burlington]]* extends it to jail-intake strip searches of arrestees entering the general population, and the *Wolfish* four-factor balance remains the frame for weighing the intrusion of an institutional search against the security need — the same custodial-intake reasoning that runs through *[[Maryland v. King]]*.

*Status note (⚪):* authored from a CourtListener-verified identity stub (two-key: cluster 110075 + 441 U.S. 520); renders under the ⚪ banner until S9 promotion.

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Foundational (institutional-deference reasonableness balancing)*

## Sources
- [*Bell v. Wolfish*, 441 U.S. 520 (1979)](https://www.courtlistener.com/opinion/110075/bell-v-wolfish/) — pinpoint: 559 (Fourth Amendment reasonableness-balancing test — the four *Wolfish* factors; Rehnquist, J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "efe5fabcfb0731cb", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "441 U.S. 520 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 100", "official_citation_present": true, "parallel_cite": "99 S. Ct. 1861; 60 L. Ed. 2d 447", "title": "Bell v. Wolfish", "year": "1979"}}
{"assertion_id": "2edb33714d1ca3d7", "dimension": "support", "kind": "home_role", "locator": {"home": "Inventory Searches"}, "payload": {"home": "Inventory Searches", "role": "Related (cross-doctrine)", "title": "Bell v. Wolfish"}}
{"assertion_id": "321eb47a4e7451cd", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Key — Foundational (institutional-deference reasonableness balancing)", "title": "Bell v. Wolfish"}}
{"assertion_id": "5bf0c1279388e8da", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Pretrial detainees retain Fourth Amendment protection, but the reasonableness of an institutional search is judged by balancing the need for the search against the intrusion it entails — weighing the scope of the intrusion, the manner in which it is conducted, the justification for initiating it, and the place in which it is conducted; on that test, and with deference to jail administrators, the Court upheld the Metropolitan Correctional Center's visual body-cavity inspections after contact visits and its other challenged conditions of pretrial confinement.", "title": "Bell v. Wolfish"}}
{"assertion_id": "4ddba069ea2c1ef2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Bell v. Wolfish", "varies_by_point": "false"}}
{"assertion_id": "5db0238db532fb4c", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Bell v. Wolfish"}}
```

### lake record — Bell v. Wolfish

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bell v. Wolfish",
  "status": "under_review",
  "identity": {
    "case_name": "Bell v. Wolfish",
    "case_name_short": "Wolfish",
    "case_name_full": "BELL, ATTORNEY GENERAL, Et Al. v. WOLFISH Et Al.",
    "input_case_name": "Bell v. Wolfish",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-05-14",
    "year": 1979,
    "docket": "77-1829",
    "cluster_id": 110075,
    "lead_opinion_id": 9427563,
    "sibling_ids": [],
    "absolute_url": "/opinion/110075/bell-v-wolfish/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "441 U.S. 520",
      "volume": "441",
      "reporter": "U.S.",
      "page": "520",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 1861",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1861",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 447",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "447",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 100",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "441 U.S. 520",
        "volume": "441",
        "reporter": "U.S.",
        "page": "520",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 1861",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "1861",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 447",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "447",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 100",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "100",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "441 U.S. 520",
    "official_selection": {
      "court_class": "scotus",
      "selected": "441 U.S. 520",
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
    "date_created": "2026-07-08T00:40:18Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [
      "W10 on-read identity re-verification 2026-07-07: docket 77-1829 confirmed verbatim from CL lead-opinion caption (html_with_citations)"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-08T00:40:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:40:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-08T00:40:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-08T00:40:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "bell-v-wolfish--110075",
      "to_record_id": "Bell v. Wolfish",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Bell v. Wolfish (truncated)

```
<opinion type="majority">
<author id="b581-4"><page-number citation-index="1" label="523">*523</page-number>Mr. Justice Rehnquist</author>
<p id="ASd">delivered the opinion of the Court.</p>
<p id="b581-5">Over the past five Terms, this Court has in several decisions considered constitutional challenges to prison conditions or practices by convicted prisoners.<footnotemark>1</footnotemark> This case requires us to examine the constitutional rights of pretrial detainees — those persons who have been charged with a crime but who have not yet been tried on the charge. The parties concede that to ensure their presence at trial, these persons legitimately may be incarcerated by the Government prior to a determination of their guilt or innocence, <em>infra, </em>at 533-535, and n. 15; see <span class="citation no-link">18 U. S. C. §§ 3146</span>, 3148, and it is the scope of their rights during this period of confinement prior to trial that is the primary focus of this case.</p>
<p id="b581-6">This lawsuit was brought as a class action in the United States District Court for the Southern District of New York to challenge numerous conditions of confinement and practices at the Metropolitan Correctional Center (MCC), a federally operated short-term custodial facility in New York City designed primarily to house pretrial detainees. The District Court, in the words of the Court of Appeals for the Second Circuit, “intervened broadly into almost every facet of the institution” and enjoined no fewer than 20 MCC practices on constitutional and statutory grounds. The Court ' of Appeals largely affirmed the District Court’s constitutional rulings and in the process held that under the Due Process Clause of the Fifth Amendment, pretrial detainees may “be subjected to only those 'restrictions and privations’ which 'inhere in their confinement itself or which are justified by <page-number citation-index="1" label="524">*524</page-number>compelling necessities of jail administration.’ ” <em>Wolfish </em>v. <em>Levi, </em><span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#124" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d 118, 124</a></span> (1978), quoting <em>Rhem </em>v. <em>Malcolm, </em><span class="citation" data-id="8895320"><a href="/opinion/8907862/rhem-v-malcolm/#336" aria-description="Citation for case: Rhem v. Malcolm">507 F. 2d 333, 336</a></span> (CA2 1974). We granted certiorari to consider the important constitutional questions raised by these decisions and to resolve an apparent conflict among the Circuits.<footnotemark>2</footnotemark> <span class="citation multiple-matches"><a href="/c/U.%20S./439/816/">439 U. S. 816</a></span> (1978). We now reverse.</p>
<p id="b582-5">I</p>
<p id="b582-6">The MCC was constructed in 1975 to replace the converted waterfront garage on West Street that had served as New York City’s federal jail since 1928. It is located adjacent to the Foley Square federal courthouse and has as its primary objective the housing of persons who are being detained in custody prior to trial for federal criminal offenses in the United States District Courts for the Southern and Eastern Districts of New York and for the District of New Jersey. Under the Bail Reform Act, <span class="citation no-link">18 U. S. C. § 3146</span>, a person in the federal system is committed to a detention facility only because no other less drastic means can reasonably ensure his presence at trial. In addition to pretrial detainees, the MCC also houses some convicted inmates who are awaiting sentencing or transportation to federal prison or who are serving generally relatively short sentences in a service capacity at the MCC, convicted prisoners who have been lodged at the facility under writs of habeas corpus <em>ad prosequendum </em>or <em>ad testificandum </em>issued to ensure their presence at upcoming trials, witnesses in protective custody, and persons incarcerated for contempt.<footnotemark>3</footnotemark></p>
<p id="b583-4"><page-number citation-index="1" label="525">*525</page-number>The MCC differs markedly from the familiar image of a jail; there are no barred cells, dank, colorless corridors, or clanging steel gates. It was intended to include the most advanced and innovative features of modern design of detention facilities. As the Court of Appeals stated: “{I]t represented the architectural embodiment of the best and most progressive penological planning.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#121" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 121</a></span>. The key design element of the 12-story structure is the “modular” or “unit” concept, whereby each floor designed to house inmates has one or two largely self-contained residential units that replace the traditional cellblock jail construction. Each unit in turn has several clusters or corridors of private rooms or dormitories radiating from a central 2-story “multipurpose” or common room, to which each inmate has free access approximately 16 hours a day. Because our analysis does not turn on the particulars of the MCC concept or design, we need not discuss them further.</p>
<p id="b583-5">When the MCC opened in August 1975, the planned capacity was 449 inmates, an increase of 50% over the former West Street facility. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#122" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>Id., </em>at 122</a></span>. Despite some dormitory accommodations, the MCC was designed primarily to house these inmates in 389 rooms, which originally were intended for single occupancy. While the MCC was under construction, however, the number of persons committed to pretrial detention began to rise at an “unprecedented” rate. <em><span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">Ibid.</a></span> </em>The Bureau of Prisons took several steps to accommodate this unexpected flow of persons assigned to the facility, but despite these efforts, the inmate population at the MCC rose above its planned capacity within a short time after its opening. To provide sleeping space for this increased population, the MCC <page-number citation-index="1" label="526">*526</page-number>replaced the single bunks in many of the individual rooms and dormitories with double bunks.<footnotemark>4</footnotemark> Also, each week some newly arrived inmates had to sleep on cots in the common areas until they could be transferred to residential rooms as space became available. See <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#127" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>id., </em>at 127-128</a></span>.</p>
<p id="b584-5">On November 28, 1975, less than four months after the MCC had opened, the named respondents initiated this action by filing in the District Court a petition for a writ of habeas corpus.<footnotemark>5</footnotemark> The District Court certified the case as a class action on behalf of all persons confined at the MCC, pretrial detainees and sentenced prisoners alike.<footnotemark>6</footnotemark> The petition served <page-number citation-index="1" label="527">*527</page-number>up a veritable potpourri of complaints that implicated virtually every facet of the institution’s conditions and practices. Respondents charged, <em>inter alia, </em>that they had been deprived of their statutory and constitutional rights because of overcrowded conditions, undue length of confinement, improper searches, inadequate recreational, educational, and employment opportunities, insufficient staff, and objectionable restrictions on the purchase and receipt of personal items and books.<footnotemark>7</footnotemark></p>
<p id="b585-5">In two opinions and a series of orders, the District Court enjoined numerous MCC practices and conditions. With respect to pretrial detainees, the court held that because they <page-number citation-index="1" label="528">*528</page-number>are “presumed to be innocent and held only to ensure their presence at trial, 'any deprivation or restriction of . . . rights beyond those which are necessary for confinement alone, must be justified by a compelling necessity.’ ” <em>United States ex rel. Wolfish </em>v. <em>Levi, </em><span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#124" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp. 114, 124</a></span> (1977), quoting <em>Detainees of Brooklyn House of Detention </em>v. <em>Malcolm, </em><span class="citation multiple-matches"><a href="/c/F.%202d/520/392/">520 F. 2d 392</a></span>, 397 (CA2 1975). And while acknowledging that the rights of sentenced inmates are to be measured by the different standard of the Eighth Amendment, the court declared that to house “an inferior minority of persons ... in ways found unconstitutional for the rest” would amount to cruel and unusual punishment. <em>United States ex rel. Wolfish </em>v. <em>United States, </em><span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#339" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp. 333, 339</a></span> (1977).<footnotemark>8</footnotemark></p>
<p id="b586-5">Applying these standards on cross-motions for partial summary judgment, the District Court enjoined the practice of housing two inmates in the individual rooms and prohibited enforcement of the so-called “publisher-only” rule, which at the time of the court’s ruling prohibited the receipt of all books and magazines mailed from outside the MCC except those sent directly from a publisher or a book club.<footnotemark>9</footnotemark> After a trial on the remaining issues, the District Court enjoined, <em>inter alia, </em>the doubling of capacity in the dormitory areas, the use of the common rooms to provide temporary sleeping accommodations, the prohibition against inmates’ receipt of packages containing food and items of personal property, and the practice of requiring inmates to expose their body cavities for visual inspection following contact visits. The court also <page-number citation-index="1" label="529">*529</page-number>granted relief in favor of pretrial detainees, but not convicted inmates, with respect to the requirement that detainees remain outside their rooms during routine inspections by MCC officials.<footnotemark>10</footnotemark></p>
<p id="b587-5">The Court of Appeals largely affirmed the District Court’s rulings, although it rejected that court’s Eighth Amendment analysis of conditions of confinement for convicted prisoners because the “parameters of judicial intervention into . . . conditions ... for sentenced prisoners are more restrictive than in the case of pretrial detainees.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#125" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 125</a></span>.<footnotemark>11</footnotemark> Ac<page-number citation-index="1" label="530">*530</page-number>cordingly, the court remanded the matter to the District Court for it to determine whether the housing for sentenced inmates at the MCC was constitutionally “adequate.” But the Court of Appeals approved the due process standard employed by the District Court in enjoining the conditions of pretrial confinement. It therefore held that the MCC had failed to make a showing of “compelling necessity” sufficient to justify housing two pretrial detainees in the individual rooms. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#126" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>Id., </em>at 126-127</a></span>. And for purposes of our review (since petitioners challenge only some of the Court of Appeals’ rulings), the court affirmed the District Court’s granting of relief against the “publisher-only” rule, the practice of conducting body-cavity searches after contact visits, the prohibition against receipt of packages of food and personal items from outside the institution, and the requirement that detainees remain outside their rooms during routine searches of the rooms by MCC officials. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#129" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>Id., </em>at 129-132</a></span>.<footnotemark>12</footnotemark></p>
<p id="b588-5">II</p>
<p id="b588-6">As a first step in our decision, we shall address “double-bunking” as it is referred to by the parties, since it is a condition of confinement that is alleged only to deprive pretrial detainees of their liberty without due process of law in contravention of the Fifth Amendment. We will treat in order the Court of Appeals’ standard of review, the analysis which we believe the Court of Appeals should have employed, <page-number citation-index="1" label="531">*531</page-number>and the conclusions to which our analysis leads us in the case of “double-bunking.”</p>
<p id="b589-5">A</p>
<p id="b589-6">The Court of Appeals did not dispute that the Government may permissibly incarcerate a person charged with a crime but not yet convicted to ensure his presence at trial. However, reasoning from the “premise that an individual is to be treated as innocent until proven guilty,” the court concluded that pretrial detainees retain the “rights afforded unincar-cerated individuals,” and that therefore it is not sufficient that the conditions of confinement for pretrial detainees “merely comport with contemporary standards of decency prescribed by the cruel and unusual punishment clause of the eighth amendment.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#124" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 124</a></span>. Rather, the court held, the Due Process Clause requires that pretrial detainees “be subjected to only those 'restrictions and privations’ which ‘inhere in their confinement itself or which are justified by compelling necessities of jail administration.’ ” <em>Ibid., </em>quoting <em>Rhem </em>v. <em>Malcolm, </em><span class="citation" data-id="8895320"><a href="/opinion/8907862/rhem-v-malcolm/#336" aria-description="Citation for case: Rhem v. Malcolm">507 F. 2d, at 336</a></span>. Under the Court of Appeals’ “compelling necessity” standard, “deprivation of the rights of detainees cannot be justified by the cries of fiscal necessity, . . . administrative convenience, ... or by the cold comfort that conditions in other jails are worse.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#124" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 124</a></span>. The court acknowledged, however, that it could not “ignore” our admonition in <em>Procunier </em>v. <em>Martinez, </em><span class="citation" data-id="9425693"><a href="/opinion/109016/procunier-v-martinez/#405" aria-description="Citation for case: Procunier v. Martinez">416 U. S. 396, 405</a></span> (1974), that “courts are ill equipped to deal with the increasingly urgent problems of prison administration,” and concluded that it would “not [be] wise for [it] to second-guess the expert administrators on matters on which they are better informed.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#124" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 124</a></span>.<footnotemark>13</footnotemark></p>
<p id="b590-4"><page-number citation-index="1" label="532">*532</page-number>Our fundamental disagreement with the Court of Appeals is that we fail to find a source in the Constitution for its compelling-necessity standard.<footnotemark>14</footnotemark> Both the Court of Appeals and the District Court seem to have relied on the “presumption of innocence” as the source of the detainee’s substantive right to be free from conditions of confinement that are not justified by compelling necessity. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#124" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 124</a></span>; <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#124" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 124</a></span>; accord, <em>Campbell </em>v. <em>McGruder, </em>188 U. S. App. D. C. 258, 266, <span class="citation" data-id="9464977"><a href="/opinion/358241/leonard-campbell-v-anderson-mcgruder-superintendent-detention-services/#529" aria-description="Citation for case: Leonard Campbell v. Anderson McGruder Superintendent,...">580 F. 2d 521, 529</a></span> (1978); <em>Detainees of Brooklyn House of Detention </em>v. <em>Malcolm, </em><span class="citation multiple-matches"><a href="/c/F.%202d/520/392/">520 F. 2d 392</a></span>, 397 (CA2 1975) ; <em>Rhem </em>v. <span class="citation" data-id="8895320"><a href="/opinion/8907862/rhem-v-malcolm/#336" aria-description="Citation for case: Rhem v. Malcolm"><em>Malcolm, supra, </em>at 336</a></span>. But see <em>Feeley </em>v. <em>Sampson, </em><span class="citation" data-id="9464513"><a href="/opinion/353029/leo-f-feeley-iv-v-george-sampson-etc/" aria-description="Citation for case: Leo F. Feeley, IV v. George Sampson, Etc.">570 F. 2d 364</a></span>, 369 n. 4 (CA1 1978); <em>Hampton </em>v. <em>Holmesburg Prison Officials, </em><span class="citation" data-id="341509"><a href="/opinion/341509/william-oscar-hampton-v-holmesburg-prison-officials-appeal-of-richard/" aria-description="Citation for case: William Oscar Hampton v. Holmesburg Prison Officials....">546 F. 2d 1077</a></span>, 1080 n. 1 (CA3 1976). But the presumption of innocence provides no support for such a rule.</p>
<p id="b591-4"><page-number citation-index="1" label="533">*533</page-number>The presumption of innocence is a doctrine that allocates the burden of proof in criminal trials; it also may serve as an admonishment to the jury to judge an accused’s guilt or innocence solely on the evidence adduced at trial and not on the basis of suspicions that may arise from the fact of his arrest, indictment, or custody, or from other matters not introduced as proof at trial. <em>Taylor </em>v. <em>Kentucky, </em><span class="citation" data-id="9427215"><a href="/opinion/109872/taylor-v-kentucky/#485" aria-description="Citation for case: Taylor v. Kentucky">436 U. S. 478, 485</a></span> (1978); see <em>Estelle </em>v. <em>Williams, </em><span class="citation" data-id="9426383"><a href="/opinion/109438/estelle-v-williams/" aria-description="Citation for case: Estelle v. Williams">425 U. S. 501</a></span> (1976); <em>In re Winship, </em><span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358</a></span> (1970); 9 J. Wigmore, Evidence § 2511 (3d ed. 1940). It is “an inaccurate, shorthand description of the right of the accused to 'remain inactive and secure, until the prosecution has taken up its burden and produced evidence and effected persuasion; . . .’ an ‘assumption’ that is indulged in the absence of contrary evidence.” <em>Taylor </em>v. <em><span class="citation" data-id="9427215"><a href="/opinion/109872/taylor-v-kentucky/" aria-description="Citation for case: Taylor v. Kentucky">Kentucky, supra,</a></span> </em>at 484 n. 12. Without question, the presumption of innocence plays an important role in our criminal justice system. “The principle that there is a presumption of innocence in favor of the accused is the undoubted law, axiomatic and elementary, and its enforcement lies at the foundation of the administration of our criminal law.” <em>Coffin </em>v. <em>United States, </em><span class="citation" data-id="94110"><a href="/opinion/94110/coffin-v-united-states/#453" aria-description="Citation for case: Coffin v. United States">156 U. S. 432, 453</a></span> (1895). But it has no application to a determination of the rights of a pretrial detainee during confinement before his trial has even begun.</p>
<p id="b591-5">The Court of Appeals also relied on what it termed the “indisputable rudiments of due process” in fashioning its compelling-necessity test. We do not doubt that the Due Process Clause protects a detainee from certain conditions and restrictions of pretrial detainment. See <em>infra, </em>at 535-540. Nonetheless, that Clause provides no basis for application of a compelling-necessity standard to conditions of pretrial confinement that are not alleged to infringe any other, more specific guarantee of the Constitution.</p>
<p id="b591-6">It is important to focus on what is at issue here. We are not concerned with the initial decision to detain an accused and the curtailment of liberty that such a decision necessarily <page-number citation-index="1" label="534">*534</page-number>entails. See <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 114</a></span> (1975) ; <em>United States </em>v. <em>Marion, </em><span class="citation" data-id="9424708"><a href="/opinion/108420/united-states-v-marion/#320" aria-description="Citation for case: United States v. Marion">404 U. S. 307, 320</a></span> (1971). Neither respondents nor the courts below question that the Government may permissibly detain a person suspected of committing a crime prior to a formal adjudication of guilt. See <em>Gerstein </em>v. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh"><em>Pugh, supra, </em>at 111-114</a></span>. Nor do they doubt that the Government has a substantial interest in ensuring that persons accused of crimes are available for trials and, ultimately, for service of their sentences, or that confinement of such persons pending trial is a legitimate means of furthering that interest. Tr. of Oral Arg. 27; see <em>Stack </em>v. <em>Boyle, </em><span class="citation" data-id="104925"><a href="/opinion/104925/stack-v-boyle/#4" aria-description="Citation for case: Stack v. Boyle">342 U. S. 1, 4</a></span> (1951).<footnotemark>15</footnotemark> Instead, what <em>is </em>at issue when an aspect of pretrial detention that is not alleged to violate any express guarantee of the Constitution is challenged, is the detainee’s right to be free from punishment, see <em>infra, </em>at 535-537, and his understandable desire to be as comfortable as possible during his confinement, both of which may conceivably coalesce at some point. It seems clear that the Court of Appeals did not rely on the detainee’s right to be free from punishment, but even if it had that right does not warrant adoption of that court’s compelling-necessity test. See <em>infra, </em>at 535-540. And to the extent the court relied on the detainee’s desire to be free from discomfort, it suffices to say that this desire simply does not rise to the level of those fundamental liberty interests delineated in cases such as <em>Roe </em>v. <em>Wade, </em><span class="citation" data-id="9425157"><a href="/opinion/108713/roe-v-wade/" aria-description="Citation for case: Roe v. Wade">410 U. S. 113</a></span> (1973) ; <page-number citation-index="1" label="535">*535</page-number><em>Eisenstadt </em>v. <em>Baird, </em><span class="citation" data-id="9424787"><a href="/opinion/108489/eisenstadt-v-baird/" aria-description="Citation for case: Eisenstadt v. Baird">405 U. S. 438</a></span> (1972); <em>Stanley </em>v. <em>Illinois, </em><span class="citation" data-id="9424810"><a href="/opinion/108497/stanley-v-illinois/" aria-description="Citation for case: Stanley v. Illinois">405 U. S. 645</a></span> (1972); <em>Griswold </em>v. <em>Connecticut, </em><span class="citation" data-id="9423065"><a href="/opinion/107082/griswold-v-connecticut/" aria-description="Citation for case: Griswold v. Connecticut">381 U. S. 479</a></span> (1965); <em>Meyer </em>v. <em>Nebraska, </em><span class="citation" data-id="100233"><a href="/opinion/100233/meyer-v-nebraska/" aria-description="Citation for case: Meyer v. Nebraska">262 U. S. 390</a></span> (1923).</p>
<p id="b593-6">B</p>
<p id="b593-7">In evaluating the constitutionality of conditions or restrictions of pretrial detention that implicate only the protection against deprivation of liberty without due process of law, we think that the proper inquiry is whether those conditions amount to punishment of the detainee.<footnotemark>16</footnotemark> For under the Due Process Clause, a detainee may not be punished prior to an adjudication of guilt in accordance with due process of law.<footnotemark>17</footnotemark> <page-number citation-index="1" label="536">*536</page-number>See <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651</a></span>, 671-672 n. 40, 674 (1977); <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#165" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S. 144, 165-167, 186</a></span> (1963); <em>Wong Wing </em>v. <em>United States, </em><span class="citation" data-id="9883065"><a href="/opinion/94479/wong-wing-v-united-states/#237" aria-description="Citation for case: Wong Wing v. United States">163 U. S. 228, 237</a></span> (1896). A person lawfully committed to pretrial detention has not been adjudged guilty of any crime. He has had only a “judicial determination of probable cause as a prerequisite to [the] extended restraint of [his] liberty following arrest.” <em>Gerstein </em>v. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh"><em>Pugh, supra, </em>at 114</a></span>; see <em>Virginia </em>v. <em>Paul, </em><span class="citation" data-id="93540"><a href="/opinion/93540/virginia-v-paul/#119" aria-description="Citation for case: Virginia v. Paul">148 U. S. 107, 119</a></span> (1893). And, if he is detained for a suspected violation of a federal law, he also has had a bail hearing. See <span class="citation no-link">18 U. S. C. §§ 3146</span>, 3148.<footnotemark>18</footnotemark> Under such circumstances, the Government concededly may detain him to ensure his presence at trial and may subject him to the restrictions and conditions of the detention facility so long as those conditions and restric<page-number citation-index="1" label="537">*537</page-number>tions do not amount to punishment, or otherwise violate the Constitution.</p>
<p id="b595-4">Not every disability imposed during pretrial detention amounts to “punishment” in the constitutional sense, however. Once the Government has exercised its conceded authority to detain a person pending trial, it obviously is entitled to employ devices that are calculated to effectuate this detention. Traditionally, this has meant confinement in a facility which, no matter how modern or how antiquated, results in restricting the movement of a detainee in a manner in which he would not be restricted if he simply were free to walk the streets pending trial. Whether it be called a jail, a prison, or a custodial center, the purpose of the facility is to detain. Loss of freedom of choice and privacy are inherent incidents of confinement in such a facility. And the fact that such detention interferes with the detainee’s understandable desire to live as comfortably as possible and with as little restraint as possible during confinement does not convert the conditions or restrictions of detention into “punishment.”</p>
<p id="b595-5">This Court has recognized a distinction between punitive measures that may not constitutionally be imposed prior to a determination of guilt and regulatory restraints that may. See, <em>e. g., Kennedy </em>v. <span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#168" aria-description="Citation for case: Kennedy v. Mendoza-Martinez"><em>Mendoza-Martinez, supra, </em>at 168</a></span>; Flemming v. <em>Nestor, </em><span class="citation" data-id="9422032"><a href="/opinion/106087/flemming-v-nestor/#613" aria-description="Citation for case: Flemming v. Nestor">363 U. S. 603, 613-614</a></span> (1960); <em>cf. DeVeau </em>v. <em>Braisted, </em><span class="citation" data-id="9421995"><a href="/opinion/106061/de-veau-v-braisted/#160" aria-description="Citation for case: De Veau v. Braisted">363 U. S. 144, 160</a></span> (1960). In <em>Kennedy </em>v. <em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">Mendoza-Martinez, supra,</a></span> </em>the Court examined the automatic forfeiture-of-citizenship provisions of the immigration laws to determine whether that sanction amounted to punishment or a mere regulatory restraint. While it is all but impossible to compress the distinction into a sentence or a paragraph, the Court there described the tests traditionally applied to determine whether a governmental act is punitive in nature:</p>
<blockquote id="b595-6">“Whether the sanction involves an affirmative disability or restraint, whether it has historically been regarded as a punishment, whether it comes into play only on a finding <page-number citation-index="1" label="538">*538</page-number>of <em>scienter, </em>whether its operation will promote the traditional aims of punishment — retribution and deterrence, whether the behavior to which it applies is already a crime, whether an alternative purpose to which it may rationally be connected is assignable for it, and whether it appears excessive in relation to the alternative purpose assigned are all relevant to the inquiry, and may often point in differing directions.” <span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#168" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S., at 168-169</a></span> (footnotes omitted).</blockquote>
<p id="b596-5">Because forfeiture of citizenship traditionally had been considered punishment and the legislative history of the forfeiture provisions “conclusively” showed that the measure was intended to be punitive, the Court held that forfeiture of citizenship in such circumstances constituted punishment that could not constitutionally be imposed without due process of law. <span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#167" aria-description="Citation for case: Kennedy v. Mendoza-Martinez"><em>Id., </em>at 167-170, 186</a></span>.</p>
<p id="b596-6">The factors identified in <em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">Mendoza-Martinez</a></span> </em>provide useful guideposts in determining whether particular restrictions and conditions accompanying pretrial detention amount to punishment in the constitutional sense of that word. A court must decide whether the disability is imposed for the purpose of punishment or whether it is but an incident of some other legitimate governmental purpose. See <em>Flemming </em>v. <span class="citation" data-id="9422032"><a href="/opinion/106087/flemming-v-nestor/#613" aria-description="Citation for case: Flemming v. Nestor"><em>Nestor, supra, </em>at 613-617</a></span>.<footnotemark>19</footnotemark> Absent a showing of an expressed intent to punish on the part of detention facility officials, that determination generally will turn on “whether an alternative purpose to which [the restriction] may rationally be connected is assignable for it, and whether it appears excessive in relation to the alternative purpose assigned [to it].” <em>Kennedy </em>v. <span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#168" aria-description="Citation for case: Kennedy v. Mendoza-Martinez"><em>Mendoza-Martinez, supra, </em>at 168-169</a></span>; see <em>Flemming </em>v. <page-number citation-index="1" label="539">*539</page-number><span class="citation" data-id="9422032"><a href="/opinion/106087/flemming-v-nestor/#617" aria-description="Citation for case: Flemming v. Nestor"><em>Nestor, supra, </em>at 617</a></span>. Thus, if a particular condition or restriction of pretrial detention is reasonably related to a legitimate governmental objective, it does not, without more, amount to “punishment.” <footnotemark>20</footnotemark> Conversely, if a restriction or condition is not reasonably related to a legitimate goal — if it is arbitrary or purposeless — a court permissibly may infer that the purpose of the governmental action is punishment that may not constitutionally be inflicted upon detainees <em>qua </em>detainees. See <em><span class="citation" data-id="9422032"><a href="/opinion/106087/flemming-v-nestor/" aria-description="Citation for case: Flemming v. Nestor">ibid.</a></span></em><footnotemark><em>21</em></footnotemark><em> </em>Courts must be mindful that these inquiries spring from constitutional requirements and that judicial answers to them must reflect that fact rather than a court’s idea of how best to operate a detention facility. Cf. <em>United States </em>v. <em>Lovasco, </em><span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#790" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 790</a></span> (1977); <em>United States </em>v. <em>Russell, </em><span class="citation" data-id="9425257"><a href="/opinion/108768/united-states-v-russell/#435" aria-description="Citation for case: United States v. Russell">411 U. S. 423, 435</a></span> (1973).</p>
<p id="b597-5">One further point requires discussion. The petitioners assert, and respondents concede, that the “essential objective of pretrial confinement is to insure the detainees’ presence at trial.” Brief for Petitioners 43; see Brief for Respondents 33. While this interest undoubtedly justifies the original decision to confine an individual in some manner, we do not accept <page-number citation-index="1" label="540">*540</page-number>respondents’ argument that the Government’s interest in ensuring a detainee’s presence at trial is the <em>only </em>objective that may justify restraints and conditions once the decision is lawfully made to confine a person. “If the government could confine or otherwise infringe the liberty of detainees only to the extent necessary to ensure their presence at trial, house arrest would in the end be the only constitutionally justified form of detention.” <em>Campbell </em>v. <em><span class="citation" data-id="9464977"><a href="/opinion/358241/leonard-campbell-v-anderson-mcgruder-superintendent-detention-services/" aria-description="Citation for case: Leonard Campbell v. Anderson McGruder Superintendent,...">McGruder</a></span>, </em>188 U. S. App. D. C., at 266, <span class="citation" data-id="9464977"><a href="/opinion/358241/leonard-campbell-v-anderson-mcgruder-superintendent-detention-services/#529" aria-description="Citation for case: Leonard Campbell v. Anderson McGruder Superintendent,...">580 F. 2d, at 529</a></span>. The Government also has legitimate interests that stem from its need to manage the facility in which the individual is detained. These legitimate operational concerns may require administrative measures that go beyond those that are, strictly speaking, necessary to ensure that the detainee shows up at trial. For example, the Government must be able to take steps to maintain security and order at the institution and make certain no weapons or illicit drugs reach detainees.<footnotemark>22</footnotemark> Restraints that are reasonably related to the institution’s interest in maintaining jail security do not, without more, constitute unconstitutional punishment, even if they are discomforting and are restrictions that the detainee would not have experienced had he been released while awaiting trial. We need not here attempt to detail the precise extent of the legitimate governmental interests that may justify conditions or restrictions of pretrial detention. It is enough simply to recognize that in addition to ensuring the detainees’ presence at trial, the effective management of the detention facility once the individual is confined is a valid objective that may justify imposition of conditions and restrictions of pretrial detention and dispel any inference that such restrictions are intended as punishment.<footnotemark>23</footnotemark></p>
<p id="b599-4"><page-number citation-index="1" label="541">*541</page-number>c</p>
<p id="b599-5">Judged by this analysis, respondents’ claim that “double-bunking” violated their due process rights fails. Neither the District Court nor the Court of Appeals intimated that it considered “double-bunking” to constitute punishment; instead, they found that it contravened the compelling-necessity test, which today we reject. On this record, we are convinced as a matter of law that “double-bunking” as practiced at the MCC did not amount to punishment and did not, therefore, violate respondents’ rights under the Due Process Clause of the Fifth Amendment.<footnotemark>24</footnotemark></p>
<p id="b599-6">Each of the rooms at the MCC that house pretrial detainees has a total floor space of approximately 75 square feet. Each of them designated for “double-bunking,” see n. 4, <em>supra, </em>contains a double bunkbed, certain other items of furniture, a wash basin, and an uncovered toilet. Inmates generally are locked into their rooms from 11 p.m. to 6:30 a.m. and for brief periods during the afternoon and evening head counts. During the rest of the day, they may move about freely between their rooms and the common areas.</p>
<p id="b599-7">Based on affidavits and a personal visit to the facility, the District Court concluded that the practice of “double-bunking” was unconstitutional. The court relied on two factors for its conclusion: (1) the fact that the rooms were designed to house only one inmate, <span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#336" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp., at 336-337</a></span>; and (2) its judg<page-number citation-index="1" label="542">*542</page-number>ment that confining two persons in one room or cell of this size constituted a “fundamental denia[l] of decency, privacy, personal security, and, simply, civilized humanity . . . .” <span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#339" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States"><em>Id., </em>at 339</a></span>. The Court of Appeals agreed with the District Court. In response to petitioners’ arguments that the rooms at the MCC were larger and more pleasant than the cells involved in the cases relied on by the District Court, the Court of Appeals stated:</p>
<blockquote id="b600-5">“ [W] e find the lack of privacy inherent in double-celling in rooms intended for one individual a far more compelling consideration than a comparison of square footage or the substitution of doors for bars, carpet for concrete, or windows for walls. The government has simply failed to show any substantial justification for double-celling.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#127" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 127</a></span>.</blockquote>
<p id="b600-6">We disagree with both the District Court and the Court of Appeals that there is some sort of “one man, one cell” principle lurking in the Due Process Clause of the Fifth Amendment. While confining a given number of people in a given amount of space in such a manner as to cause them to endure genuine privations and hardship over an extended period of time might raise serious questions under the Due Process Clause as to whether those conditions amounted to punishment, nothing even approaching such hardship is shown by this record.<footnotemark>25</footnotemark></p>
<p id="b601-4"><page-number citation-index="1" label="543">*543</page-number>Detainees are required to spend only seven or eight hours each day in their rooms, during most or all of which they presumably are sleeping. The rooms provide more than adequate space for sleeping.<footnotemark>26</footnotemark> During the remainder of the time, the detainees are free to move between their rooms and the common area. While “double-bunking” may have taxed some of the equipment or particular facilities in certain of the common areas, <em>United States ex rel. Wolfish </em>v. <em>United States, </em><span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#337" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp., at 337</a></span>, this does not mean that the conditions at the MCC failed to meet the standards required by the Constitution. Our conclusion in this regard is further buttressed by the detainees’ length of stay at the MCC. See <em>Hutto </em>v. <em>Finney, </em><span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/#686" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678, 686-687</a></span> (1978). Nearly all of the detainees are released within 60 days. See n. 3, <em>supra. </em>We simply do not believe that requiring a detainee to share toilet facilities and this admittedly rather small sleeping place with another person for generally a maximum period of 60 days violates the Constitution.<footnotemark>27</footnotemark></p>
<p id="b602-4"><page-number citation-index="1" label="544">*544</page-number>Ill</p>
<p id="b602-5">Respondents also challenged certain MCC restrictions and practices that were designed to promote security and order at the facility on the ground that these restrictions violated the Due Process Clause of the Fifth Amendment, and certain other constitutional guarantees, such as the First and Fourth Amendments. The Court of Appeals seemed to approach the challenges to security restrictions in a fashion different from the other contested conditions and restrictions. It stated that “once it has been determined that the mere fact of confinement of the detainee justifies the restrictions, the institution must be permitted to use reasonable means to insure that its legitimate interests in security are safeguarded.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#124" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 124</a></span>. The court might disagree with the choice of means to effectuate those interests, but it should not “second-guess the expert administrators on matters on which they are better informed .... Concern with minutiae of prison administration can only distract the court from detached consideration of the one overriding question presented to it: does the practice or condition violate the Constitution?” <em><span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">Id.,</a></span> </em>at 124—125. Nonetheless, the court affirmed the District Court’s injunction <page-number citation-index="1" label="545">*545</page-number>against several security restrictions. The court rejected the arguments of petitioners that these practices served the MCC’s interest in security and order and held that the practices were unjustified interferences with the retained constitutional rights of <em>both </em>detainees and convicted inmates. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#129" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>Id., </em>at 129-132</a></span>. In our view, the Court of Appeals failed to heed its own admonition not to “second-guess” prison administrators.</p>
<p id="b603-5">Our cases have established several general principles that inform our evaluation of the constitutionality of the restrictions at issue. First, we have held that convicted prisoners do not forfeit all constitutional protections by reason of their conviction and confinement in prison. See <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, </em><span class="citation" data-id="9426926"><a href="/opinion/109718/jones-v-north-carolina-prisoners-labor-union-inc/#129" aria-description="Citation for case: Jones v. North Carolina Prisoners&#x27; Labor Union, Inc.">433 U. S. 119, 129</a></span> (1977); <em>Meachum </em>v. <em>Fano, </em><span class="citation" data-id="9426509"><a href="/opinion/109510/meachum-v-fano/#225" aria-description="Citation for case: Meachum v. Fano">427 U. S. 215, 225</a></span> (1976); <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 555-556</a></span> (1974); <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#822" aria-description="Citation for case: Pell v. Procunier">417 U. S. 817, 822</a></span> (1974). “There is no iron curtain drawn between the Constitution and the prisons of this country.” <em>Wolff </em>v. <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell"><em>McDonnell, supra, </em>at 555-556</a></span>. So, for example, our cases have held that sentenced prisoners enjoy freedom of speech and religion under the First and Fourteenth Amendments, see <em>Pell </em>v. <em>Procunier, supra; Cruz </em>v. <em>Beto, </em><span class="citation" data-id="9424773"><a href="/opinion/108484/cruz-v-beto/" aria-description="Citation for case: Cruz v. Beto">405 U. S. 319</a></span> (1972); <em>Cooper </em>v. <em>Pate, </em><span class="citation" data-id="106889"><a href="/opinion/106889/cooper-v-pate/" aria-description="Citation for case: Cooper v. Pate">378 U. S. 546</a></span> (1964); that they are protected against invidious discrimination on the basis of race under the Equal Protection Clause of the Fourteenth Amendment, see <em>Lee </em>v. <em>Washington, </em><span class="citation" data-id="9423632"><a href="/opinion/107630/lee-v-washington/" aria-description="Citation for case: Lee v. Washington">390 U. S. 333</a></span> (1968); and that they may claim the protection of the Due Process Clause to prevent additional deprivation of life, liberty, or property without due process of law, see <em>Meachum </em>v. <em><span class="citation" data-id="9426509"><a href="/opinion/109510/meachum-v-fano/" aria-description="Citation for case: Meachum v. Fano">Fano, supra;</a></span> Wolff </em>v. <em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">McDonnell, supra.</a></span> A fortiori, </em>pretrial detainees, who have not been convicted of any crimes, retain at least those constitutional rights that we have held are enjoyed by convicted prisoners.</p>
<p id="b603-6">But our cases also have insisted on a second proposition: simply because prison inmates retain certain constitutional rights does not mean that these rights are not subject to restrictions and limitations. “Lawful incarceration brings <page-number citation-index="1" label="546">*546</page-number>about the necessary withdrawal or limitation of many privileges and rights, a retraction justified by the considerations underlying our penal system.” <em>Price </em>v. <em>Johnston, </em><span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/#285" aria-description="Citation for case: Price v. Johnston">334 U. S. 266, 285</a></span> (1948); see <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, supra, </em>at 125; <em>Wolff </em>v. <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#555" aria-description="Citation for case: Wolff v. McDonnell"><em>McDonnell, supra, </em>at 555</a></span>; <em>Pell </em>v. <em>Procunier, supra, </em>at 822. The fact of confinement as well as the legitimate goals and policies of the penal institution limits these retained constitutional rights. <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, supra, </em>at 125; <em>Pell </em>v. <em>Procunier, supra, </em>at 822. There must be a “mutual accommodation between institutional needs and objectives and the provisions of the Constitution that are of general application.” <em>Wolff </em>v. <span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#556" aria-description="Citation for case: Wolff v. McDonnell"><em>McDonnell, supra, </em>at 556</a></span>. This principle applies equally to pretrial detainees and convicted prisoners. A detainee simply does not possess the full range of freedoms of an unincarcerated individual.</p>
<p id="b604-5">Third, maintaining institutional security and preserving internal order and discipline are essential goals that may require limitation or retraction of the retained constitutional rights of both convicted prisoners and pretrial detainees.<footnotemark>28</footnotemark> “[Cjentral to all other corrections goals is the institutional <page-number citation-index="1" label="547">*547</page-number>consideration of internal security within the corrections facilities themselves.” <em>Pell </em>v. <em>Procunier, supra, </em>at 823; see <em>Jones v. North Carolina Prisoners’ Labor Union, supra, </em>at 129; <em>Procunier </em>v. <em>Martinez, </em><span class="citation" data-id="9425693"><a href="/opinion/109016/procunier-v-martinez/#412" aria-description="Citation for case: Procunier v. Martinez">416 U. S. 396, 412</a></span> (1974). Prison officials must be free to take appropriate action to ensure the safety of inmates and corrections personnel and to prevent escape or unauthorized entry. Accordingly, we have held that even when an institutional restriction infringes a specific constitutional guarantee, such as the First Amendment, the practice must be evaluated in the light of the central objective of prison administration, safeguarding institutional security. <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, supra, </em>at 129; <em>Pell </em>v. <em>Procunier, supra, </em>at 822, 826; <em>Procunier </em>v. <em>Martinez, supra, </em>at 412-414.</p>
<p id="b605-5">Finally, as the Court of Appeals correctly acknowledged, the problems that arise in the day-to-day operation of a corrections facility are not susceptible of easy solutions. Prison administrators therefore should be accorded wide-ranging deference in the adoption and execution of policies and practices that in their judgment are needed to preserve internal order and discipline and to maintain institutional security. <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, supra, </em>at 128; <em>Procunier </em>v. <em>Martinez, supra, </em>at 404-405; <em>Cruz </em>v. <span class="citation" data-id="9424773"><a href="/opinion/108484/cruz-v-beto/#321" aria-description="Citation for case: Cruz v. Beto"><em>Beto, supra, </em>at 321</a></span>; see <em>Meachum </em>v. <span class="citation" data-id="9426509"><a href="/opinion/109510/meachum-v-fano/#228" aria-description="Citation for case: Meachum v. Fano"><em>Fano, 427 </em>U. S., at 228-229</a></span>.<footnotemark>29</footnotemark> “Such <page-number citation-index="1" label="548">*548</page-number>considerations are peculiarly within the province and professional expertise of corrections officials, and, in the absence of substantial evidence in the record to indicate that the officials have exaggerated their response to these considerations, courts should ordinarily defer to their expert judgment in such matters.” <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#827" aria-description="Citation for case: Pell v. Procunier">417 U. S., at 827</a></span>.<footnotemark>30</footnotemark> We further observe that, on occasion, prison administrators may be “experts” only by Act of Congress or of a state legislature. But judicial deference is accorded not merely because the administrator ordinarily will, as a matter of fact in a particular case, have a better grasp of his domain than the reviewing judge, but also because the operation of our correctional facilities is peculiarly the province of the Legislative and Executive Branches of our Government, not the Judicial. <em>Procunier </em>v. <em>Martinez, supra, </em>at 405; cf. <em>Meachum </em>v. <span class="citation" data-id="9426509"><a href="/opinion/109510/meachum-v-fano/#229" aria-description="Citation for case: Meachum v. Fano"><em>Fano, supra, at </em>229</a></span>. With these teachings of our cases in mind, we turn to an examination of the MCC security practices that are alleged to violate the Constitution.</p>
<p id="b606-5">A</p>
<p id="b606-6">At the time of the lower courts’ decisions, the Bureau of Prisons’ “publisher-only” rule, which applies to all Bureau <page-number citation-index="1" label="549">*549</page-number>facilities, permitted inmates to receive books and magazines from outside the institution only if the materials were mailed directly from the publisher or a book club. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#129" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 129-130</a></span>. The warden of the MCC stated in an affidavit that “serious” security and administrative problems were caused when bound items were received by inmates from unidentified sources outside the facility. App. 24. He noted that in order to make a “proper and thorough” inspection of such items, prison officials would have to remove the covers of hardback books and to leaf through every page of all books and magazines to ensure that drugs, money, weapons, or other contraband were not secreted in the material. “This search process would take a substantial and inordinate amount of available staff time.” <em><span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">Ibid.</a></span> </em>However, “there is relatively little risk that material received directly from a publisher or book club would contain contraband, and therefore, the security problems are significantly reduced without a drastic drain on staff resources.” <em><span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">Ibid.</a></span></em></p>
<p id="b607-5">The Court of Appeals rejected these security and administrative justifications and affirmed the District Court’s order enjoining enforcement of the “publisher-only” rule at the MCC. The Court of Appeals held that the rule “severely and impermissibly restricts the reading material available to inmates” and therefore violates their First Amendment and due process rights. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#130" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 130</a></span>.</p>
<p id="b607-6">It is desirable at this point to place in focus the precise question that now is before this Court. Subsequent to the decision of the Court of Appeals, the Bureau of Prisons amended its “publisher-only” rule to permit the receipt of books and magazines from bookstores as well as publishers and book clubs. <span class="citation no-link">43 Fed. Reg. 30576</span> (1978) (to be codified in <span class="citation no-link">28 CFR §540.71</span>). In addition, petitioners have informed the Court that the Bureau proposes to amend the rule further to allow receipt of paperback books, magazines, and other soft-covered materials from any source. Brief for Petitioners 66 n. 49, 69, and n. 51. The Bureau regards hardback books as <page-number citation-index="1" label="550">*550</page-number>the “more dangerous source of risk to institutional security,” however, and intends to retain the prohibition against receipt of hardback books unless they are mailed directly from publishers, book clubs, or bookstores. <em>Id.., </em>at 69 n. 51. Accordingly, petitioners request this Court to review the District Court’s injunction only to the extent it enjoins petitioners from prohibiting receipt of hard-cover books that are not mailed directly from publishers, book clubs, or bookstores. <span class="citation no-link"><em>Id., </em>at 69</span>; Tr. of Oral Arg. 59-60.<footnotemark>31</footnotemark></p>
<p id="b608-5">We conclude that a prohibition against receipt of hardback books unless mailed directly from publishers, book clubs, or bookstores does not violate the First Amendment rights of MCC inmates. That limited restriction is a rational response by prison officials to an obvious security problem. It hardly <page-number citation-index="1" label="551">*551</page-number>needs to be emphasized that hardback books are especially serviceable for smuggling contraband into an institution; money, drugs, and weapons easily may be secreted in the bindings. <em>E. g., Woods </em>v. <em>Daggett, </em><span class="citation" data-id="338734"><a href="/opinion/338734/roger-lee-woods-v-loren-daggett-warden-united-states-penitentiary/" aria-description="Citation for case: Roger Lee Woods v. Loren Daggett, Warden United States...">541 F. 2d 237</a></span> (CA10 1976).<footnotemark>32</footnotemark> They also are difficult to search effectively. There is simply no evidence in the record to indicate that MCC officials have exaggerated their response to this security problem and to the administrative difficulties posed by the necessity of carefully inspecting each book mailed from unidentified sources. Therefore, the considered judgment of these experts must control in the absence of prohibitions far more sweeping than those involved here. See <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, </em><span class="citation" data-id="9426926"><a href="/opinion/109718/jones-v-north-carolina-prisoners-labor-union-inc/#128" aria-description="Citation for case: Jones v. North Carolina Prisoners&#x27; Labor Union, Inc.">433 U. S., at 128</a></span>; <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#827" aria-description="Citation for case: Pell v. Procunier">417 U. S., at 827</a></span>.</p>
<p id="b609-5">Our conclusion that this limited restriction on receipt of hardback books does not infringe the First Amendment rights of MCC inmates is influenced by several other factors. The rule operates in a neutral fashion, without regard to the content of the expression. <span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#828" aria-description="Citation for case: Pell v. Procunier"><em>Id., </em>at 828</a></span>. And there are alternative means of obtaining reading material that have not been shown to be burdensome or insufficient. “[W]e regard the <page-number citation-index="1" label="552">*552</page-number>available ‘alternative means of [communication as] a relevant factor’ in a case such as this where ‘we [are] called upon to balance First Amendment rights against [legitimate] governmental . . . interests.’ ” <span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#824" aria-description="Citation for case: Pell v. Procunier"><em>Id., </em>at 824</a></span>, quoting <em>Kleindienst </em>v. <em>Mandel, </em><span class="citation" data-id="9425024"><a href="/opinion/108612/kleindienst-v-mandel/#765" aria-description="Citation for case: Kleindienst v. Mandel">408 U. S. 753, 765</a></span> (1972); see <em>Cruz </em>v. <em>Beto, </em><span class="citation" data-id="9424773"><a href="/opinion/108484/cruz-v-beto/#321" aria-description="Citation for case: Cruz v. Beto">405 U. S., at 321</a></span>, 322 n. 2. The restriction, as it is now before us, allows soft-bound books and magazines to be received from any source and hardback books to be received from publishers, bookstores, and book clubs. In addition, the MCC has a “relatively large” library for use by inmates. <em>United States ex rel. Wolfish </em>v. <em>United States, </em><span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#340" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp., at 340</a></span>.<footnotemark>33</footnotemark> To the limited extent the rule might possibly increase the cost of obtaining published materials, this Court has held that where “other avenues” remain available for the receipt of materials by inmates, the loss of “cost advantages does not fundamentally implicate <em>free speech </em>values.” See <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, supra, </em>at 130-131. We are also ififluenced in our decision by the fact that the rule’s impact on pretrial detainees is limited to a maximum period of approximately 60 days. See n. 3, <em>supra. </em>In sum, considering all the circumstances, we view the rule, as we now find it, to be a “reasonable ‘time, place and manner’ regulatio[n that is] necessary to further significant governmental interests . . . .” <em>Grayned </em>v. <em>City of Rockford, </em><span class="citation" data-id="8980926"><a href="/opinion/8988822/grayned-v-city-of-rockford/#115" aria-description="Citation for case: Grayned v. City of Rockford">408 U. S. 104, 115</a></span> (1972); see <em>Cox </em>v. <em>New Hampshire, </em><span class="citation" data-id="103490"><a href="/opinion/103490/cox-v-new-hampshire/#575" aria-description="Citation for case: Cox v. New Hampshire">312 U. S. 569, 575-576</a></span> (1941); <em>Cox </em>v. <em>Louisiana, </em><span class="citation" data-id="106967"><a href="/opinion/106967/cox-v-louisiana/#554" aria-description="Citation for case: Cox v. Louisiana">379 U. S. 536, 554-555</a></span> (1965); <em>Adderley </em>v. <em>Florida, </em><span class="citation" data-id="9423277"><a href="/opinion/107291/adderley-v-florida/#46" aria-description="Citation for case: Adderley v. Florida">385 U. S. 39, 46-48</a></span> (1966).</p>
<p id="b611-4"><page-number citation-index="1" label="553">*553</page-number>B</p>
<p id="b611-5">Inmates at the MCC were not permitted to receive packages from outside the facility containing items of food or personal property, except for one package of food at Christmas. This rule was justified by MCC officials on three grounds. First, officials testified to “serious” security problems that arise from the introduction of such packages into the institution, the “traditional file in the cake kind of situation” as well as the concealment of drugs “in heels of shoes [and] seams of clothing.” App. 80; see <em>id., </em>at 24, 84-85. As in the case of the “publisher-only” rule, the warden testified that if such packages were allowed, the inspection process necessary to ensure the security of the institution would require a “substantial and inordinate amount of available staff time.” <em>Id., </em>at 24. Second, officials were concerned that the introduction of personal property into the facility would increase the risk of thefts, gambling, and inmate conflicts, the “age-old problem of you have it and I don’t.” <em>Id., </em>at 80; see <em>id., </em>at 85. Finally, they noted storage and sanitary problems that would result from inmates’ receipt of food packages. <em>Id., </em>at 67, 80. Inmates are permitted, however, to purchase certain items of food and personal property from the MCC commissary.<footnotemark>34</footnotemark></p>
<p id="b611-6">The District Court dismissed these justifications as “dire predictions.” It was unconvinced by the asserted security problems because other institutions allow greater ownership of personal property and receipt of packages than does the MCC. And because the MCC permitted inmates to purchase items in the commissary, the court could not accept official fears of increased theft, gambling, or conflicts if packages were allowed. Finally, it believed that sanitation could be assured by proper housekeeping regulations. Accordingly, it ordered the MCC to promulgate regulations to permit receipt of at least items of the kind that are available in the commissary. <page-number citation-index="1" label="554">*554</page-number><span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#152" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 152-153</a></span>. The Court of Appeals accepted the District Court’s analysis and affirmed, although it noted that the MCC could place a ceiling on the permissible dollar value of goods received and restrict the number of packages. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#132" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 132</a></span>.</p>
<p id="b612-5">Neither the District Court nor the Court of Appeals identified which provision of the Constitution was violated by this MCC restriction. We assume, for present purposes, that their decisions were based on the Due Process Clause of the Fifth Amendment, which provides protection for convicted prisoners and pretrial detainees alike against the deprivation of their property without due process of law. See <em>supra, </em>at 545. But as we have stated, these due process rights of prisoners and pretrial detainees are not absolute; they are subject to reasonable limitation or retraction in light of the legitimate security concerns of the institution.</p>
<p id="b612-6">We think that the District Court and the Court of Appeals have trenched too cavalierly into areas that are properly the concern of MCC officials. It is plain from their opinions that the lower courts simply disagreed with the judgment of MCC officials about the extent of the security interests affected and the means required to further those interests. But our decisions have time and again emphasized that this sort of unguided substitution of judicial judgment for that of the expert prison administrators on matters such as this is inappropriate. See <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union; Pell </em>v. <em>Procunier; Procunier </em>v. <em><span class="citation" data-id="9425693"><a href="/opinion/109016/procunier-v-martinez/" aria-description="Citation for case: Procunier v. Martinez">Martinez</a></span>. </em>We do not doubt that the rule devised by the District Court and modified by the Court of Appeals may be a reasonable way of coping with the problems of security, order, and sanitation. It simply is not, however, the only constitutionally permissible approach to these problems-. Certainly, the Due Process Clause does not mandate a “lowest common denominator” security standard, whereby a practice permitted at one penal institution must be permitted at all institutions.</p>
<p id="b613-4"><page-number citation-index="1" label="555">*555</page-number>Corrections officials concluded that permitting the introduction of packages of personal property and food would increase the risks of gambling, theft, and inmate fights over that which the institution already experienced by permitting certain items to be purchased from its commissary. “It is enough to say that they have not been conclusively shown to be wrong in this view.” <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, </em><span class="citation" data-id="9426926"><a href="/opinion/109718/jones-v-north-carolina-prisoners-labor-union-inc/#132" aria-description="Citation for case: Jones v. North Carolina Prisoners&#x27; Labor Union, Inc.">433 U. S., at 132</a></span>. It is also all too obvious that such packages are handy devices for the smuggling of contraband. There simply is no basis in this record for concluding that MCC officials have exaggerated their response to these serious problems or that this restriction is irrational. It does not therefore deprive the convicted inmates or pretrial detainees <footnotemark>35</footnotemark> of the MCC of their property without due process of law in contravention of the Fifth Amendment.</p>
<p id="b613-5">C</p>
<p id="b613-6">The MCC staff conducts unannounced searches of inmate living areas at irregular intervals. These searches generally are formal unit “shakedowns” during which all inmates are cleared of the residential units, and a team of guards searches each room. Prior to the District Court’s order, inmates were not permitted to watch the searches. Officials testified that permitting inmates to observe room inspections would lead to friction between the inmates and security guards and would allow the inmates to attempt to frustrate the search by distracting personnel and moving contraband from one room to another ahead of the search team.<footnotemark>36</footnotemark></p>
<p id="b614-4"><page-number citation-index="1" label="556">*556</page-number>The District Court held that this procedure could not stand as applied to pretrial detainees because MCC officials had not shown that the restriction was justified by “compelling necessity.” <footnotemark>37</footnotemark> The court stated that “[a]t least until or unless [petitioners] can show a pattern of violence or other disruptions taxing the powers of control — a kind of showing not remotely approached by the Warden’s expressions — the security argument for banishing inmates while their rooms are searched must be rejected.” <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#149" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 149</a></span>. It also noted that in many instances inmates suspected guards of thievery. <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#148" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi"><em>Id., </em>at 148-149</a></span>. The Court of Appeals agreed with the District Court. It saw “no reason whatsoever not to permit a detainee to observe the search of his room and belongings from a reasonable distance,” although the court permitted the removal of any detainee who became “obstructive.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#132" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 132</a></span>.</p>
<p id="b614-5">The Court of Appeals did not identify the constitutional provision on which it relied in invalidating the room-search rule. The District Court stated that the rule infringed the detainee’s interest in privacy and indicated that this interest in privacy was founded on the Fourth Amendment. <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#149" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 149-150</a></span>. It may well be argued that a person confined in a detention facility has no reasonable expectation of privacy with respect to his room or cell and that therefore the Fourth Amendment provides no protection for such a <page-number citation-index="1" label="557">*557</page-number>person. Cf. <em>Lanza </em>v. <em>New York, </em><span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#143" aria-description="Citation for case: Lanza v. New York">370 U. S. 139, 143-144</a></span> (1962). In any case, given the realities of institutional confinement, any reasonable expectation of privacy that a detainee retained necessarily would be of a diminished scope. <span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/#143" aria-description="Citation for case: Lanza v. New York"><em>Id., </em>at 143</a></span>. Assuming, <em>arguendo, </em>that a pretrial detainee retains such a diminished expectation of privacy after commitment to a custodial facility, we nonetheless find that the room-search rule does not violate the Fourth Amendment.</p>
<p id="b615-5">It is difficult to see how the detainee’s interest in privacy is infringed by the room-search rule. No one can rationally doubt that room searches represent an appropriate security measure and neither the District Court nor the Court of Appeals prohibited such searches. And even the most zealous advocate of prisoners’ rights would not suggest that a warrant is required to conduct such a search. Detainees’ drawers, beds, and personal items may be searched, even after the lower courts’ rulings. Permitting detainees to observe the searches does not lessen the invasion of their privacy; its only conceivable beneficial effect would be to prevent theft or misuse by those conducting the search. The room-search rule simply facilitates the safe and effective performance of the search which all concede may be conducted. The rule itself, then, does not render the searches “unreasonable” within the meaning of the Fourth Amendment.<footnotemark>38</footnotemark></p>
<p id="b616-4"><page-number citation-index="1" label="558">*558</page-number>D</p>
<p id="b616-5">Inmates at all Bureau of Prisons facilities, including the MCC, are required to expose their body cavities for visual inspection as a part of a strip search conducted after every contact visit with a person from outside the institution.<footnotemark>39</footnotemark> Corrections officials testified that visual cavity searches were necessary not only to discover but also to deter the smuggling of weapons, drugs, and other contraband into the institution. App. 70-72, 83-84. The District Court upheld the strip-search procedure but prohibited the body-cavity searches, absent probable cause to believe that the inmate is concealing contraband. <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#147" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 147-148</a></span>. Because petitioners proved only one instance in the MCC’s short history where contraband was found during a body-cavity search, the Court of Appeals affirmed. In its view, the “gross violation of personal privacy inherent in such a search cannot be outweighed by the government’s security interest in maintaining a practice of so little actual utility.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#131" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 131</a></span>.</p>
<p id="b616-6">Admittedly, this practice instinctively gives us the most pause. However, assuming for present purposes that inmates, both convicted prisoners and pretrial detainees, retain some Fourth Amendment rights upon commitment to a corrections facility, see <em>Lanza </em>v. <em>New <span class="citation" data-id="9422429"><a href="/opinion/106425/lanza-v-new-york/" aria-description="Citation for case: Lanza v. New York">York, supra;</a></span> Stroud </em>v. <em>United States, </em><span class="citation" data-id="99464"><a href="/opinion/99464/stroud-v-united-states/#21" aria-description="Citation for case: Stroud v. United States">251 U. S. 15, 21</a></span> (1919), we nonetheless conclude that these searches do not violate that Amendment. The Fourth Amendment prohibits only unreasonable searches, <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#147" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 147</a></span> (1925), and under the circumstances, we do not believe that these searches are unreasonable.</p>
<p id="b617-4"><page-number citation-index="1" label="559">*559</page-number>The test of reasonableness under the Fourth Amendment is not capable of precise definition or mechanical application. In each case it requires a balancing of the need for the particular search against the invasion of personal rights that the search entails. Courts must consider the scope of the particular intrusion, the manner in which it is conducted, the justification for initiating it, and the place in which it is conducted. <em>E. g., United States </em>v. <em>Ramsey, </em><span class="citation" data-id="9426823"><a href="/opinion/109675/united-states-v-ramsey/" aria-description="Citation for case: United States v. Ramsey">431 U. S. 606</a></span> (1977); <em>United States </em>v. <em>Martinez-Fuerte, </em><span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975); <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span> (1967); <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966). A detention facility is a unique place fraught with serious security dangers. Smuggling of money, drugs, weapons, and other contraband is all too common an occurrence. And inmate attempts to secrete these items into the facility by concealing them in body cavities are documented in this record, App. 71-76, and in other cases. <em>E. g., Ferraro </em>v. <em>United States, </em><span class="citation" data-id="362646"><a href="/opinion/362646/united-states-v-ferraro/" aria-description="Citation for case: United States v. Ferraro">590 F. 2d 335</a></span> (CA6 1978); <em>United States </em>v. <em>Park, </em><span class="citation" data-id="329773"><a href="/opinion/329773/united-states-v-loretta-mae-park/#1382" aria-description="Citation for case: United States v. Loretta Mae Park">521 F. 2d 1381, 1382</a></span> (CA9 1975). That there has been only one instance where an MCC inmate was discovered attempting to smuggle contraband into the institution on his person may be more a testament to the effectiveness of this search technique as a deterrent than to any lack of interest on the part of the inmates to secrete and import such items when the opportunity arises.<footnotemark>40</footnotemark></p>
<p id="b618-4"><page-number citation-index="1" label="560">*560</page-number>We do not underestimate the degree to which these searches may invade the personal privacy of inmates. Nor do we doubt, as the District Court noted, that on occasion a security guard may conduct the search in an abusive fashion. <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#147" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 147</a></span>. Such abuse cannot be condoned. The searches must be conducted in a reasonable manner. <em>Schmerber </em>v. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#771" aria-description="Citation for case: Schmerber v. California"><em>California, supra, </em>at 771-772</a></span>. But we deal here with the question whether visual body-cavity inspections as contemplated by the MCC rules can <em>ever </em>be conducted on less than probable cause. Balancing the significant and legitimate security interests of the institution against the privacy interests of the inmates, we conclude that they can.<footnotemark>41</footnotemark></p>
<p id="b618-5">IV</p>
<p id="b618-6">Nor do we think that the four MCC security restrictions and practices described in Part III, <em>supra, </em>constitute “punish<page-number citation-index="1" label="561">*561</page-number>ment” in violation of the rights of pretrial detainees under the Due Process Clause of the Fifth Amendment.<footnotemark>42</footnotemark> Neither the District Court nor the Court of Appeals suggested that these restrictions and practices were employed by MCC officials with an intent to punish the pretrial detainees housed there.<footnotemark>43</footnotemark> Respondents do not even make such a suggestion; they simply argue that the restrictions were greater than necessary to satisfy petitioners’ legitimate interest in maintaining security. Brief for Respondents 51-53. Therefore, the determination whether these restrictions and practices constitute punishment in the constitutional sense depends on whether they are rationally related to a legitimate nonpunitive governmental purpose and whether they appear excessive in relation to that purpose. See <em>supra, </em>at 538-539. Ensuring security and order at the institution is a permissible nonpunitive objective, whether the facility houses pretrial detainees, convicted inmates, or both. <em>Supra, </em>at 539-540; see <em>supra, </em>at 546-547, and n. 28. For the reasons set forth in Part III, <em>supra, </em>we think that these particular restrictions and practices were reasonable responses by MCC officials to legitimate security concerns. Respondents simply have not met their heavy <page-number citation-index="1" label="562">*562</page-number>burden of showing that these officials have exaggerated their response to the genuine security considerations that actuated these restrictions and practices. See n. 23, <em>supra. </em>And as might be expected of restrictions applicable to pretrial detainees, these restrictions were of only limited duration so far as the MCC pretrial detainees were concerned. See n. 3, <em>supra.</em></p>
<p id="b620-5">V</p>
<p id="b620-6">There was a time not too long ago when the federal judiciary took a completely “hands-off” approach to the problem of prison administration. In recent years, however, these courts largely have discarded this “hands-off” attitude and have waded into this complex arena. The deplorable conditions and Draconian restrictions of some of our Nation’s prisons are too well known to require recounting here, and the federal courts rightly have condemned these sordid aspects of our prison systems. But many of these same courts have, in the name of the Constitution, become increasingly enmeshed in the minutiae of prison operations. Judges, after all, are human. They, no less than others in our society, have a natural tendency to believe that their individual solutions to often intractable problems are better and more workable than those of the persons who are actually charged with and trained in the running of the particular institution under examination. But under the Constitution, the first question to be answered is not whose plan is best, but in what branch of the Government is lodged the authority to initially devise the plan. This does not mean that constitutional rights are not to be scrupulously observed. It does mean, however, that the inquiry of federal courts into prison management must be limited to the issue of whether a particular system violates any prohibition of the Constitution or, in the case of a federal prison, a statute. The wide range of “judgment calls” that meet constitutional and statutory requirements are confided to officials outside of the Judicial Branch of Government.</p>
<p id="b621-4"><page-number citation-index="1" label="563">*563</page-number>The judgment of the Court of Appeals is, accordingly, reversed, and the case is remanded for proceedings consistent with this opinion.</p>
<p id="b621-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b581-8"> See, <em>e. g., Hutto </em>v. <em>Finney, </em><span class="citation" data-id="9427304"><a href="/opinion/109919/hutto-v-finney/" aria-description="Citation for case: Hutto v. Finney">437 U. S. 678</a></span> (1978); <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, </em><span class="citation" data-id="9426926"><a href="/opinion/109718/jones-v-north-carolina-prisoners-labor-union-inc/" aria-description="Citation for case: Jones v. North Carolina Prisoners&#x27; Labor Union, Inc.">433 U. S. 119</a></span> (1977); <em>Bounds </em>v. <em>Smith, </em><span class="citation" data-id="9426761"><a href="/opinion/109643/bounds-v-smith/" aria-description="Citation for case: Bounds v. Smith">430 U. S. 817</a></span> (1977); <em>Meachum </em>v. <em>Fano, </em><span class="citation" data-id="9426509"><a href="/opinion/109510/meachum-v-fano/" aria-description="Citation for case: Meachum v. Fano">427 U. S. 215</a></span> (1976); <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539</a></span> (1974); <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/" aria-description="Citation for case: Pell v. Procunier">417 U. S. 817</a></span> (1974); <em>Procunier </em>v. <em>Martinez, </em><span class="citation" data-id="9425693"><a href="/opinion/109016/procunier-v-martinez/" aria-description="Citation for case: Procunier v. Martinez">416 U. S. 396</a></span> (1974).</p>
</footnote>
<footnote label="2">
<p id="b582-7"> See, <em>e. g., Norris </em>v. <span class="citation" data-id="360390"><a href="/opinion/360390/tyrone-norris-individually-and-on-behalf-of-all-others-similarly-situated/" aria-description="Citation for case: Tyrone Norris, Individually and on Behalf of All Others..."><em>Frame, 585 F. </em>2d 1183</a></span> (CA3 1978); <em>Campbell </em>v. <em>McGruder, </em>188 U. S. App. D. C. 258, <span class="citation" data-id="9464977"><a href="/opinion/358241/leonard-campbell-v-anderson-mcgruder-superintendent-detention-services/" aria-description="Citation for case: Leonard Campbell v. Anderson McGruder Superintendent,...">580 F. 2d 521</a></span> (1978); <em>Wolfish </em>v. <em>Levi, </em><span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d 118</a></span> (CA2 1978) (case below); <em>Feeley </em>v. <em>Sampson, </em><span class="citation" data-id="9464513"><a href="/opinion/353029/leo-f-feeley-iv-v-george-sampson-etc/" aria-description="Citation for case: Leo F. Feeley, IV v. George Sampson, Etc.">570 F. 2d 364</a></span> (CA1 1978); <em>Main Road </em>v. <em>Aytch, </em><span class="citation" data-id="8903896"><a href="/opinion/8915704/main-road-v-aytch/" aria-description="Citation for case: Main Road v. Aytch">565 F. 2d 54</a></span> (CA3 1977); <em>Patterson </em>v. <em>Morrisette, </em><span class="citation" data-id="8903801"><a href="/opinion/8915625/patterson-v-morrisette/" aria-description="Citation for case: Patterson v. Morrisette">564 F. 2d 1109</a></span> (CA4 1977); <em>Miller </em>v. <em>Carson, </em><span class="citation" data-id="9464196"><a href="/opinion/349561/richard-franklin-miller-v-dale-carson-individually-and-in-his-capacity-as/" aria-description="Citation for case: Richard Franklin Miller v. Dale Carson, Individually and...">563 F. 2d 741</a></span> (CA5 1977); <em>Duran </em>v. <em>Elrod, </em><span class="citation" data-id="339381"><a href="/opinion/339381/dan-duran-v-richard-elrod/" aria-description="Citation for case: Dan Duran v. Richard Elrod">542 F. 2d 998</a></span> (CA7 1976).</p>
</footnote>
<footnote label="3">
<p id="b582-8"> This group of nondetainees may comprise, on a daily basis, between 40% and 60% of the MCC population. <em>United States ex rel. Wolfish </em>v. <em>United States, </em><span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#335" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp. 333, 335</a></span> (SDNY 1977). Prior to the District <page-number citation-index="1" label="525">*525</page-number>Court’s order, 50% of <em>all </em>MCC inmates spent less than 30 days at the facility and 73% less than 60 days. <em>United States ex rel. Wolfish </em>v. <em>Levi, </em><span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#127" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp. 114, 127</a></span> (SDNY 1977). However, of the unsentenoed detainees, over half spent less than 10 days at the MCC, three-quarters were released within a month and more than 85% were released within 60 days, <em>Wolfish </em>v. <em>Levi, supra, </em>at 129 n. 25.</p>
</footnote>
<footnote label="4">
<p id="b584-6"> Of the 389 residential rooms at the MCC, 121 had been “designated” for “double-bunking” at the time of the District Court’s order. <span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#336" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp., at 336</a></span>. The number of rooms actually housing two inmates, however, never exceeded 73 and, of these, only 35 were rooms in units that housed pretrial detainees. Brief for Petitioners 7 n. 6; Brief for Respondents 11-12; App. 33-35 (affidavit of Larry Taylor, MCC Warden, dated Dec. 29, 1976).</p>
</footnote>
<footnote label="5">
<p id="b584-7"> It appears that the named respondents may now have been transferred or released from the MCC. See <em>United States ex rel. Wolfish </em>v. <em>Levi, supra, </em>at 119. “This case belongs, however, to that narrow class of cases in which the termination of a class representative’s claim does not moot the claims of the unnamed members of the class.” <em>Gerstein </em>v. <em>Pugh, </em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span>, 110 n. 11 (1975); see <em>Sosna </em>v. <em>Iowa, </em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">419 U. S. 393</a></span> (1975). The named respondents had a case or controversy at the time the complaint was filed and at the time the class action was certified by the District Court pursuant to Fed. Rule Civ. Proc. 23, and there remains a live controversy between petitioners and the members of the class represented by the named respondents. See <em>Sosna </em>v. <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#402" aria-description="Citation for case: Sosna v. Iowa"><em>Iowa, supra, </em>at 402</a></span>. Finally, because of the temporary nature of confinement at the MCC, the issues presented are, as in <em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">Sosna</a></span> </em>and <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>, </em>“capable of repetition, yet evading review.” <span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/#400" aria-description="Citation for case: Sosna v. Iowa">419 U. S., at 400-401</a></span>; <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S., at 110</a></span> n. 11; see <em>Kremens </em>v. <em>Bartley, </em><span class="citation" data-id="9426782"><a href="/opinion/109652/kremens-v-bartley/#133" aria-description="Citation for case: Kremens v. Bartley">431 U. S. 119, 133</a></span> (1977). Accordingly, the requirements of Art. Ill are met and the case is not moot.</p>
</footnote>
<footnote label="6">
<p id="b584-8"> Petitioners apparently never contested the propriety of respondents’ use of a writ of habeas corpus to challenge the conditions of their confinement, and petitioners do not raise that question in this Court. However, respondents did plead an alternative basis for jurisdiction in their “Amended Petition” in the District Court — namely, 28 U. S. C. § 1361— <page-number citation-index="1" label="527">*527</page-number>that arguably provides jurisdiction. And, at the time of the relevant orders of the District Court in this case, jurisdiction would have been provided by <span class="citation no-link">28 U. S. C. § 1331</span> (a). Thus, we leave to another day the question of the propriety of using a writ of habeas corpus to obtain review of the conditions of confinement, as distinct from the fact or length of the confinement itself. See <em>Preiser </em>v. <em>Rodriguez, </em><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/#499" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475, 499-500</a></span> (1973). See generally <em>Lake Country Estates, Inc. </em>v. <em>Tahoe Regional Planning Agency, </em><span class="citation" data-id="9427483"><a href="/opinion/110033/lake-country-estates-inc-v-tahoe-regional-planning-agency/" aria-description="Citation for case: Lake Country Estates, Inc. v. Tahoe Regional Planning Agency">440 U. S. 391</a></span> (1979).</p>
<p id="AZB">Similarly, petitioners do not contest the District Court’s certification of this case as a class action. For much the same reasons as identified above, there is no need in this case to reach the question whether Fed. Rule Civ. Proe. 23, providing for class actions, is applicable to petitions for habeas corpus relief. Accordingly, we express no opinion as to the correctness of the District Court’s action in this regard. See <em>Middendorf </em>v. <em>Henry, </em><span class="citation" data-id="9426338"><a href="/opinion/109414/middendorf-v-henry/#30" aria-description="Citation for case: Middendorf v. Henry">425 U. S. 25, 30</a></span> (1976).</p>
</footnote>
<footnote label="7">
<p id="b585-12"> The Court of Appeals described the breadth of this action as follows:</p>
<blockquote id="AaJ">“As an indication of the scope of this action, the amended petition also decried the inadequate phone service; 'strip’ searches; room searches outside the inmate’s presence; a prohibition against the receipt of packages or the use of personal typewriters; interference with, and monitoring of, personal mail; inadequate and arbitrary disciplinary and grievance procedures; inadequate classification of prisoners; improper treatment of non-English speaking inmates; unsanitary conditions; poor ventilation; inadequate and unsanitary food; the denial of furloughs, unannounced transfers; improper restrictions on religious freedom; and an insufficient and inadequately trained staff.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 123</a></span> n. 7.</blockquote>
</footnote>
<footnote label="8">
<p id="b586-6"> While most of the District Court’s rulings were based on constitutional grounds, the court also held that some of the actions of the Bureau of Prisons were subject to review under the Administrative Procedure Act (APA) and were “arbitrary and capricious” within the meaning of the APA. <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#122" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 122-123, 141</a></span>; see n. 11, <em>infra.</em></p>
</footnote>
<footnote label="9">
<p id="b586-7"> The District Court also enjoined confiscation of inmate property by prison officials without supplying a receipt and, except under specified circumstances, the reading and inspection of inmates’ outgoing and incoming mail. <span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#341" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp., at 341-344</a></span>. Petitioners do not challenge these rulings.</p>
</footnote>
<footnote label="10">
<p id="b587-6"> The District Court also granted respondents relief on the following issues: classification of inmates and movement between units; length of confinement; law library facilities; the commissary; use of personal typewriters; social and attorney visits; telephone service; inspection of inmates’ mail; inmate uniforms; availability of exercise for inmates in administrative detention; food service; access to the bathroom in the visiting area; special diets for Muslim inmates; and women’s “lock-in.” <span class="citation" data-id="1578049"><a href="/opinion/1578049/united-states-ex-rel-wolfish-v-levi/#125" aria-description="Citation for case: United States Ex Rel. Wolfish v. Levi">439 F. Supp., at 125-165</a></span>. None of these rulings are before this Court.</p>
</footnote>
<footnote label="11">
<p id="b587-7"> The Court of Appeals held that “[a]n institution’s obligation under the eighth amendment is at an end if it furnishes sentenced prisoners with adequate food, clothing, shelter, sanitation, medical care, and personal safety.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#125" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 125</a></span>.</p>
<p id="b587-8">The Court of Appeals also held that the District Court’s reliance on the APA was erroneous. See n. 8, <em>supra. </em>The Court of Appeals concluded that because the Bureau of Prisons’ enabling legislation vests broad discretionary powers in the Attorney General, the administration of federal prisons constitutes “ 'agency action . . . committed to agency discretion by law’ ” that is exempt from judicial review under the APA, at least in the absence of a breach of a specific statutory mandate. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#125" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 125</a></span>; see <span class="citation no-link">5 U. S. C. §701</span> (a)(2). Because of its holding that the APA was inapplicable to this case, the Court of Appeals reversed the District Court's rulings that the bathroom in the visiting area must be kept unlocked, that prison officials must make a certain level of local and long-distance telephone service available to MCC inmates, that the MCC must maintain unchanged its present schedule for social visits, and that the MCC must take commissary requests every other day. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#125" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi">573 F. 2d, at 125-126</a></span>, and n. 16. Respondents have not cross petitioned from the Court of Appeals’ disposition of the District Court’s Eighth Amendment and APA rulings.</p>
</footnote>
<footnote label="12">
<p id="b588-7"> Although the Court of Appeals held that doubling the capacity of the dormitories was unlawful, it remanded for the District Court to determine “whether any number of inmates in excess of rated capacity could be suitably quartered within the dormitories.” <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#128" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>Id., </em>at 128</a></span>. In view of the changed conditions resulting from this litigation, the court also remanded to the District Court for reconsideration of its order limiting incarceration of detainees at the MCC to a period less than 60 days. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#129" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>Id., </em>at 129</a></span>. The court reversed the District Court’s rulings that inmates be permitted to possess typewriters for their personal use in their rooms and that inmates not be required to wear uniforms. <span class="citation" data-id="354222"><a href="/opinion/354222/louis-wolfish-v-honorable-edward-levi/#132" aria-description="Citation for case: Louis Wolfish v. Honorable Edward Levi"><em>Id., </em>at 132-133</a></span>. None of these rulings are before the Court.</p>
</footnote>
<footnote label="13">
<p id="b589-7"> The NAACP Legal Defense and Educational Fund, Inc., as <em>amicus curiae, </em>argues that federal courts have inherent authority to correct conditions of pretrial confinement and that the practices at issue in this case violate the Attorney General’s alleged duty to provide inmates with “suitable quarters” under <span class="citation no-link">18 U. S. C. § 4042</span> (2). Brief for the NAACP <page-number citation-index="1" label="532">*532</page-number>Legal Defense and Educational Fund, Inc., as <em>Amicus Curiae </em>22-46. Neither argument was presented to or passed on by the lower courts; nor have they been urged by either party in this Court. Accordingly, we have no occasion to reach them in this case. <em>Knetsch </em>v. <em>United States, </em><span class="citation" data-id="9422074"><a href="/opinion/106129/knetsch-v-united-states/#370" aria-description="Citation for case: Knetsch v. United States">364 U. S. 361, 370</a></span> (1960).</p>
</footnote>
<footnote label="14">
<p id="b590-6"> As authority for its compelling-necessity test, the court cited three of its prior decisions, <em>Rhem </em>v. <em>Malcolm, </em><span class="citation" data-id="8895320"><a href="/opinion/8907862/rhem-v-malcolm/" aria-description="Citation for case: Rhem v. Malcolm">507 F. 2d 333</a></span> (CA2 1974) <em>(Rhem I); Detainees of Brooklyn House of Detention </em>v. <em>Malcolm, </em><span class="citation multiple-matches"><a href="/c/F.%202d/520/392/">520 F. 2d 392</a></span> (CA2 1975); and <em>Rhem </em>v. <em>Malcolm, </em><span class="citation" data-id="8898210"><a href="/opinion/8910516/rhem-v-malcolm/" aria-description="Citation for case: Rhem v. Malcolm">527 F. 2d 1041</a></span> (CA2 1975) <em>(Rhem II). Rhem I’s </em>support for the compelling-necessity test came from <em>Brenneman </em>v. <em>Madigan, </em><span class="citation" data-id="1691314"><a href="/opinion/1691314/brenneman-v-madigan/#142" aria-description="Citation for case: Brenneman v. Madigan">343 F. Supp. 128, 142</a></span> (ND Cal. 1972), which in turn cited no cases in support of its statement of the relevant test. <em>Detainees </em>found support for the compelling-necessity standard in <em>Shapiro </em>v. <em>Thompson, </em><span class="citation" data-id="9424000"><a href="/opinion/107901/shapiro-v-thompson/" aria-description="Citation for case: Shapiro v. Thompson">394 U. S. 618</a></span> (1969); <em>Tate </em>v. <em>Short, </em><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">401 U. S. 395</a></span> (1971); <em>Williams </em>v. <em>Illinois, </em><span class="citation" data-id="9424339"><a href="/opinion/108194/williams-v-illinois/" aria-description="Citation for case: Williams v. Illinois">399 U. S. 235</a></span> (1970); and <em>Shelton </em>v. <em>Tucker, </em><span class="citation" data-id="9422089"><a href="/opinion/106142/shelton-v-tucker/" aria-description="Citation for case: Shelton v. Tucker">364 U. S. 479</a></span> (1960). But <em><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">Tate</a></span> </em>and <em>Williams </em>dealt with equal protection challenges to imprisonment based on inability to pay fines or costs. Similarly, <em><span class="citation" data-id="9424000"><a href="/opinion/107901/shapiro-v-thompson/" aria-description="Citation for case: Shapiro v. Thompson">Shapiro</a></span> </em>concerned equal protection challenges to state welfare eligibility requirements found to violate the constitutional right to travel. In <em><span class="citation" data-id="9422089"><a href="/opinion/106142/shelton-v-tucker/" aria-description="Citation for case: Shelton v. Tucker">Shelton</a></span>, </em>the Court held that a school board policy requiring disclosure of personal associations violated the First and Fourteenth Amendment rights of a teacher. None of these cases support the court’s compelling-necessity test. Finally, <em>Rhem II </em>merely relied on <em>Rhem I </em>and <em>Detainees.</em></p>
</footnote>
<footnote label="15">
<p id="b592-5"> In order to imprison a person prior to trial, the Government must comply with constitutional requirements, <em>Gerstein </em>v. <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#114" aria-description="Citation for case: Gerstein v. Pugh"><em>Pugh, 420 U. S., </em>at 114</a></span>; <em>Stack </em>v. <em>Boyle, </em><span class="citation" data-id="104925"><a href="/opinion/104925/stack-v-boyle/#5" aria-description="Citation for case: Stack v. Boyle">342 U. S., at 5</a></span>, and any applicable statutory provisions, e. <em>g., </em><span class="citation no-link">18 U. S. C. §§ 3146</span>, 3148. Respondents do not allege that the Government failed to comply with the constitutional or statutory requisites to pretrial detention.</p>
<p id="b592-6">The only justification for pretrial detention asserted by the Government is to ensure the detainees’ presence at trial. Brief for Petitioners 43. Respondents do not question the legitimacy of this goal. Brief for Respondents 33; Tr. of Oral Arg. 27. We, therefore, have no occasion to consider whether any other governmental objectives may constitutionally justify pretrial detention.</p>
</footnote>
<footnote label="16">
<p id="b593-8"> The Court of Appeals properly relied on the Due Process Clause rather than the Eighth Amendment in considering the claims of pretrial detainees. Due process requires that a pretrial detainee not be punished. A sentenced inmate, on the other hand, may be punished, although that punishment may not be “cruel and unusual” under the Eighth Amendment. The Court recognized this distinction in <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#671" aria-description="Citation for case: Ingraham v. Wright">430 U. S. 651, 671-672, n. 40</a></span> (1977):</p>
<blockquote id="b593-9">“Eighth Amendment scrutiny is appropriate only after the State has complied with the constitutional guarantees traditionally associated with criminal prosecutions. See <em>United States </em>v. <em>Lovett, </em><span class="citation" data-id="104303"><a href="/opinion/104303/united-states-v-lovett/#317" aria-description="Citation for case: United States v. Lovett">328 U. S. 303, 317-318</a></span> (1946). . . . [T]he State does not acquire the power to punish with which the Eighth Amendment is concerned until after it has secured a formal adjudication of guilt in accordance with due process of law. Where the State seeks to impose punishment without such an adjudication, the pertinent constitutional guarantee is the Due Process Clause of the Fourteenth Amendment.”</blockquote>
</footnote>
<footnote label="17">
<p id="b593-10"> MR. Justice SteveNs in dissent claims that this holding constitutes a departure from our prior due process cases, specifically <em>Leis </em>v. <em>Flynt, </em><span class="citation" data-id="9427412"><a href="/opinion/109969/leis-v-flynt/" aria-description="Citation for case: Leis v. Flynt">439 U. S. 438</a></span> (1979), and <em>Paul </em>v. <em>Davis, </em><span class="citation" data-id="9426316"><a href="/opinion/109402/paul-v-davis/" aria-description="Citation for case: Paul v. Davis">424 U. S. 693</a></span> (1976). <em>Post, </em>at 580-581, and n. 6. But as the citations following our textual statement indicate, we leave prior decisional law as we find it and simply apply it to the case at bar. For example, in <em>Wong Wing </em>v. <em>United States, </em><span class="citation" data-id="9883065"><a href="/opinion/94479/wong-wing-v-united-states/#237" aria-description="Citation for case: Wong Wing v. United States">163 U. S. 228, 237</a></span> (1896), the Court held that the subjection of persons to punishment at hard labor must be preceded by a judicial trial to establish guilt. And in <em>Ingraham </em>v. <span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#674" aria-description="Citation for case: Ingraham v. Wright"><em>Wright, supra, </em>at 674</a></span>, we stated that “at least where school authorities, acting under color of state law, deliberately <page-number citation-index="1" label="536">*536</page-number>decide to <em>punish </em>a child for misconduct by restraining the child and inflicting appreciable physical pain, we hold that Fourteenth Amendment liberty interests are implicated.” (Emphasis supplied.) Thus, there is neither novelty nor inconsistency in our holding that the Fifth Amendment includes freedom from punishment within the liberty of which no person may be deprived without due process of law.</p>
<p id="Au3">We, of course, do not mean by the textual discussion of the rights of pretrial detainees to cast doubt on any historical exceptions to the general principle that punishment can only follow a determination of guilt after trial or plea — exceptions such as the power summarily to punish for contempt of court. See, <em>e. g., United States </em>v. <em>Wilson, </em><span class="citation" data-id="9426071"><a href="/opinion/109248/united-states-v-wilson/" aria-description="Citation for case: United States v. Wilson">421 U. S. 309</a></span> (1975); <em>Bloom </em>v. <em>Illinois, </em><span class="citation" data-id="9423694"><a href="/opinion/107686/bloom-v-illinois/" aria-description="Citation for case: Bloom v. Illinois">391 U. S. 194</a></span> (1968); <em>United States </em>v. <em>Barnett, </em><span class="citation" data-id="9422771"><a href="/opinion/106792/united-states-v-barnett/" aria-description="Citation for case: United States v. Barnett">376 U. S. 681</a></span> (1964); <em>Cooke </em>v. <em>United States, </em><span class="citation" data-id="100624"><a href="/opinion/100624/cooke-v-united-states/" aria-description="Citation for case: Cooke v. United States">267 U. S. 517</a></span> (1925); <em>Ex parte Terry, </em><span class="citation" data-id="92334"><a href="/opinion/92334/ex-parte-terry/" aria-description="Citation for case: Ex Parte Terry">128 U. S. 289</a></span> (1888); Fed. Rule Crim. Proc. 42.</p>
</footnote>
<footnote label="18">
<p id="b594-7"> The Bail Reform Act of 1966 establishes a liberal policy in favor of pretrial release. <span class="citation no-link">18 U. S. C. §§ 3146</span>, 3148. Section 3146 provides in pertinent part:</p>
<blockquote id="b594-8">“Any person charged with an offense, other than an offense punishable by death, shall, at his appearance before a judicial officer, be ordered released pending trial on his personal recognizance or upon the execution of an unsecured appearance bond in an amount specified by the judicial officer, unless the officer determines, in the exercise of his discretion, that such a release will not reasonably assure the appearance of the person as required.”</blockquote>
</footnote>
<footnote label="19">
<p id="b596-7"> As Mr. Justice Frankfurter stated in <em>United States </em>v. <em>Lovett, </em><span class="citation" data-id="104303"><a href="/opinion/104303/united-states-v-lovett/#324" aria-description="Citation for case: United States v. Lovett">328 U. S. 303, 324</a></span> (1946) (concurring opinion): “The fact that harm is inflicted by governmental authority does not make it punishment. Figuratively speaking all discomforting action may be deemed punishment because it deprives of what otherwise would be enjoyed. But there may be reasons other than punitive for such deprivation.”</p>
</footnote>
<footnote label="20">
<p id="b597-6"> This is not to say that the officials of a detention facility can justify punishment. They cannot. It is simply to say that in the absence of a showing of intent to punish, a court must look to see if a particular restriction or condition, which may on its face appear to be punishment, is instead but an incident of a legitimate nonpunitive governmental objective. See <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#168" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S., at 168</a></span>; <em>Flemming </em>v. <em>Nestor, </em><span class="citation" data-id="9422032"><a href="/opinion/106087/flemming-v-nestor/#617" aria-description="Citation for case: Flemming v. Nestor">363 U. S., at 617</a></span>. Retribution and deterrence are not legitimate nonpuni-tive governmental objectives. <em>Kennedy </em>v. <span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#168" aria-description="Citation for case: Kennedy v. Mendoza-Martinez"><em>Mendoza-Martinez, supra, </em>at 168</a></span>. Conversely, loading a detainee with chains and shackles and throwing him in a dungeon may ensure his presence at trial and preserve the security of the institution. But it would be difficult to conceive of a situation where conditions so harsh, employed to achieve objectives that could be accomplished in so many alternative and less harsh methods, would not support a conclusion that the purpose for which they were imposed was to punish.</p>
</footnote>
<footnote label="21">
<p id="b597-7"> “There is, of course, a <em>de minimis </em>level of imposition with which the Constitution is not concerned.” <em>Ingraham </em>v. <em>Wright, </em><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/#674" aria-description="Citation for case: Ingraham v. Wright">430 U. S., at 674</a></span>.</p>
</footnote>
<footnote label="22">
<p id="b598-5"> In fact, security measures may directly serve the Government’s interest in ensuring the detainee’s presence at trial. See <em>Feeley </em>v. <em>Sampson, </em><span class="citation" data-id="9464513"><a href="/opinion/353029/leo-f-feeley-iv-v-george-sampson-etc/#369" aria-description="Citation for case: Leo F. Feeley, IV v. George Sampson, Etc.">570 F. 2d, at 369</a></span>.</p>
</footnote>
<footnote label="23">
<p id="b598-6"> In determining whether restrictions or conditions are reasonably related to the Government’s interest in maintaining security and order and operating the institution in a manageable fashion, courts must heed <page-number citation-index="1" label="541">*541</page-number>our warning that “[s]uch considerations are peculiarly within the province and professional expertise of corrections officials, and, in the absence of substantial evidence in the record to indicate that the officials have exaggerated their response to these considerations, courts should ordinarily defer to their expert judgment in such matters.” <em>Pell </em>v. <em>Procunier, </em><span class="citation" data-id="9425783"><a href="/opinion/109079/pell-v-procunier/#827" aria-description="Citation for case: Pell v. Procunier">417 U. S., at 827</a></span>; see <em>Jones </em>v. <em>North Carolina Prisoners’ Labor Union, </em><span class="citation" data-id="9426926"><a href="/opinion/109718/jones-v-north-carolina-prisoners-labor-union-inc/" aria-description="Citation for case: Jones v. North Carolina Prisoners&#x27; Labor Union, Inc.">433 U. S. 119</a></span> (1977); <em>Meachum </em>v. <em>Fano, </em><span class="citation" data-id="9426509"><a href="/opinion/109510/meachum-v-fano/" aria-description="Citation for case: Meachum v. Fano">427 U. S. 215</a></span> (1976); <em>Procunier </em>v. <em>Martinez, </em><span class="citation" data-id="9425693"><a href="/opinion/109016/procunier-v-martinez/" aria-description="Citation for case: Procunier v. Martinez">416 U. S. 396</a></span> (1974).</p>
</footnote>
<footnote label="24">
<p id="b599-9"> The District Court found that there were no disputed issues of material fact with respect to respondents’ challenge to “double-bunking.” <span class="citation" data-id="1792154"><a href="/opinion/1792154/united-states-ex-rel-wolfish-v-united-states/#335" aria-description="Citation for case: United States Ex Rel. Wolfish v. United States">428 F. Supp., at 335</a></span>. We agree with the District Court in this determination.</p>
</footnote>
<footnote label="25">
<p id="b600-7"> Respondents seem to argue that “double-bunking” was unreasonable because petitioners were able to comply with the District Court’s order forbidding “double-bunking” and still accommodate the increased numbers of detainees simply by transferring all but a handful of sentenced inmates who had been assigned to the MCC for the purpose of performing certain services and by committing those tasks to detainees. Brief for Respondents 50. That petitioners were able to comply with the District Court’s order in this fashion does not mean that petitioners’ chosen method of coping with the increased inmate population — “double-bunking” — was unreasonable. Governmental action does not have to be the only alternative or even the best 

[...TRUNCATED 23774 of 143774 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: content/cases/Benn v. Lambert.md  (`case`, 5 assertions)

### content_page

```
---
title: "Benn v. Lambert"
type: case
citation: "283 F.3d 1040 (2002)"
parallel_cite: 2002 Daily Journal DAR 2161
neutral_cite: "2002 Cal. Daily Op. Serv. 1758; 2002 U.S. App. LEXIS 2899; 2002 WL 264622"
court: "U.S. Court of Appeals, Ninth Circuit"
court_level: coa
circuit: 9th
year: 2002
date_decided: 2002-02-26
docket: 00-99014
authority_weight: "Binding in-circuit — 9th Cir."
treatment:
  field_i_validity: good_law
  as_of_content: 2002-02-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Benn v. Lambert
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/776954/gary-benn-v-john-lambert-superintendent-of-the-washington-state/"
  cluster_id: 776954
  opinion_id: 9494850
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Giglio v. United States]]", "[[Kyles v. Whitley]]"]
aliases: ["Benn v. Lambert (9th Cir. 2002)"]
tags: ["case", "brady", "giglio", "exculpatory-evidence", "impeachment", "ninth-circuit", "habeas"]
holding: "Granted habeas relief: the prosecution suppressed BOTH material exculpatory evidence (expert evidence on the cause of the fire) AND…"
lake:
  record_id: Benn v. Lambert
  status: under_review
  projected_at: 2026-07-06
---

# Benn v. Lambert

*283 F.3d 1040 (9th Cir. 2002)* · U.S. Court of Appeals, Ninth Circuit · **Binding in-circuit — 9th Cir.** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Benn was convicted in Washington state court of two premeditated murders and sentenced to death. The prosecution's theory was that he killed to cover up an arson-insurance-fraud scheme, and it relied heavily on jailhouse informant Roy Patrick's account of Benn's alleged admissions and on circumstantial arson evidence. On federal [[Common Legal Terms#habeas-corpus|habeas]] review, Benn showed that the State had suppressed (1) expert/agency evidence indicating the fire may have been accidental — undermining the arson motive — and (2) impeachment evidence about Patrick's own criminal misconduct and repeated lies to police while serving as an informant. The district court granted [[Common Legal Terms#habeas-corpus|habeas]] relief and the State appealed.

## Issue
Whether the state court's conclusion that no *[[Brady v. Maryland|Brady]]* violation occurred was an unreasonable application of clearly established federal law, given the State's suppression of [[Brady and Giglio|exculpatory]] arson evidence and informant-impeachment evidence.

## Rule
A *[[Brady v. Maryland|Brady]]* violation has three elements — the evidence must be favorable to the accused ([[Brady and Giglio|exculpatory]] or impeaching), it must have been suppressed by the State (willfully or inadvertently), and prejudice must have ensued (a reasonable probability that disclosure would have changed the result, undermining confidence in the verdict). Applying that standard, the court held: "Because we hold that the state court's decision that there was no *Brady* violation in Benn's case constitutes an unreasonable application of clearly established Supreme Court law, we affirm." — 283 F.3d 1040, ¶ 1. ^pin-p1

Suppressed impeachment of a key informant can itself be material even where some impeachment was introduced: "Were there no other pieces of withheld evidence in this case, we would hold that the suppression of impeachment evidence about Patrick's criminal misconduct and repeated lies to the police, while acting as an informant, is, standing alone, sufficiently prejudicial to establish a *Brady* violation." — *Id.* ¶ 58. ^pin-p58

## Application
On these facts the State suppressed both categories of favorable evidence: expert evidence casting doubt on the arson theory at the heart of the prosecution's motive case, and substantial impeachment of the jailhouse informant whose testimony the prosecution leaned on. Assessed collectively, the withheld evidence materially undermined confidence in the verdict, so a *[[Brady v. Maryland|Brady]]* violation occurred and the state court's contrary ruling was an unreasonable application of clearly established law.

## Conclusion
The Ninth Circuit affirmed the grant of [[Common Legal Terms#habeas-corpus|habeas corpus]] relief; the conviction could not stand on a record from which material favorable evidence had been suppressed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding in-circuit — 9th Cir.**
- No negative treatment. *Benn* applies the [[Brady v. Maryland]] / [[Giglio v. United States]] framework (with the three-element formulation from *[[Strickler v. Greene]]*), holding that suppressed [[Brady and Giglio|exculpatory]] **and** impeachment evidence, evaluated cumulatively, can establish a *[[Brady v. Maryland|Brady]]* violation warranting [[Common Legal Terms#habeas-corpus|habeas]] relief.

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Benn v. Lambert*, 283 F.3d 1040 (9th Cir. 2002) — https://www.courtlistener.com/opinion/776954/gary-benn-v-john-lambert-superintendent-of-the-washington-state/ — pinpoints given as paragraph numbers (¶ 1, ¶ 58); CourtListener's text is paragraph-numbered without F.3d star pagination.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2b7dab530b28ee9d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "283 F.3d 1040 (2002)", "court": "U.S. Court of Appeals, Ninth Circuit", "neutral_cite": "2002 Cal. Daily Op. Serv. 1758; 2002 U.S. App. LEXIS 2899; 2002 WL 264622", "official_citation_present": true, "parallel_cite": "2002 Daily Journal DAR 2161", "title": "Benn v. Lambert", "year": "2002"}}
{"assertion_id": "0f4ec193fa7075b1", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Granted habeas relief: the prosecution suppressed BOTH material exculpatory evidence (expert evidence on the cause of the fire) AND…", "title": "Benn v. Lambert"}}
{"assertion_id": "205c543108ddd133", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Benn v. Lambert"}}
{"assertion_id": "0fbe2370dd0efa40", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding in-circuit — 9th Cir.", "title": "Benn v. Lambert"}}
{"assertion_id": "6e7b5e8924df846a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2002-02-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Benn v. Lambert", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Benn v. Lambert", "varies_by_point": "false"}}
```

### lake record — Benn v. Lambert

```json
{
  "schema_version": "s2.v1",
  "record_id": "Benn v. Lambert",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Gary Benn v. John Lambert, Superintendent of the Washington State Penitentiary",
    "case_name_short": "",
    "case_name_full": "Gary BENN, Petitioner-Appellee, v. John LAMBERT, Superintendent of the Washington State Penitentiary, Respondent-Appellant",
    "input_case_name": "Benn v. Lambert",
    "court": "U.S. Court of Appeals, Ninth Circuit",
    "court_id": "ca9",
    "court_level": "coa",
    "circuit": "9th",
    "state": null,
    "date_decided": "2002-02-26",
    "year": 2002,
    "docket": "00-99014",
    "cluster_id": 776954,
    "lead_opinion_id": 9494850,
    "sibling_ids": [
      776954,
      9494850,
      9494851
    ],
    "absolute_url": "/opinion/776954/gary-benn-v-john-lambert-superintendent-of-the-washington-state/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "283 F.3d 1040",
      "volume": "283",
      "reporter": "F.3d",
      "page": "1040",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "2002 Daily Journal DAR 2161",
        "volume": "2002",
        "reporter": "Daily Journal DAR",
        "page": "2161",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2002 Cal. Daily Op. Serv. 1758",
        "volume": "2002",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1758",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. App. LEXIS 2899",
        "volume": "2002",
        "reporter": "U.S. App. LEXIS",
        "page": "2899",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 WL 264622",
        "volume": "2002",
        "reporter": "WL",
        "page": "264622",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "283 F.3d 1040",
        "volume": "283",
        "reporter": "F.3d",
        "page": "1040",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Cal. Daily Op. Serv. 1758",
        "volume": "2002",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "1758",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 Daily Journal DAR 2161",
        "volume": "2002",
        "reporter": "Daily Journal DAR",
        "page": "2161",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 U.S. App. LEXIS 2899",
        "volume": "2002",
        "reporter": "U.S. App. LEXIS",
        "page": "2899",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2002 WL 264622",
        "volume": "2002",
        "reporter": "WL",
        "page": "264622",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "283 F.3d 1040",
    "official_selection": {
      "court_class": "coa",
      "selected": "283 F.3d 1040",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-p1",
      "page": null,
      "quote": "--- # Benn v. Lambert *283 F.3d 1040 (9th Cir. 2002)* \u00b7 U.S. Court of Appeals, Ninth Circuit \u00b7 **Binding in-circuit \u2014 9th Cir.** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Benn was convicted in Washington state court of two premeditated murders and sentenced to death. The prosecution's theory was that he killed to cover up an arson-insurance-fraud scheme, and it relied heavily on jailhouse informant Roy Patrick's account of Benn's alleged admissions and on circumstantial arson evidence. On federal habeas review, Benn showed that the State had suppressed (1) expert/agency evidence indicating the fire may have been accidental \u2014 undermining the arson motive \u2014 and (2) impeachment evidence about Patrick's own criminal misconduct and repeated lies to police while serving as an informant. The district court granted habeas relief and the State appealed. ## Issue Whether the state court's conclusion that no *Brady* violation occurred was an unreasonable application of clearly established federal law, given the State's suppression of exculpatory arson evidence and informant-impeachment evidence. ## Rule A *Brady* violation has three elements \u2014 the evidence must be favorable to the accused (exculpatory or impeaching), it must have been suppressed by the State (willfully or inadvertently), and prejudice must have ensued (a reasonable probability that disclosure would have changed the result, undermining confidence in the verdict). Applying that standard, the court held:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-p58",
      "page": null,
      "quote": "Were there no other pieces of withheld evidence in this case, we would hold that the suppression of impeachment evidence about Patrick's criminal misconduct and repeated lies to the police, while acting as an informant, is, standing alone, sufficiently prejudicial to establish a *Brady* violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2002-02-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Benn v. Lambert",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Yepiz",
          "cluster_id": 4331742,
          "cite": [
            "844 F.3d 1070",
            "2016 WL 7367827"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Randall Amado v. Terri Gonzalez",
          "cluster_id": 2683349,
          "cite": [
            "758 F.3d 1119",
            "2014 U.S. App. LEXIS 13710",
            "2014 WL 3377340"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mathew Musladin v. Anthony Lamarque, Warden",
          "cluster_id": 789867,
          "cite": [
            "403 F.3d 1072",
            "2005 U.S. App. LEXIS 5685",
            "2005 WL 797565"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michael Jon Bailey v. Diane Rae, Oregon State Board of Parole and Post Prison Supervision, Chairperson",
          "cluster_id": 783142,
          "cite": [
            "339 F.3d 1107",
            "2003 Daily Journal DAR 9669",
            "2003 Cal. Daily Op. Serv. 7250",
            "2003 U.S. App. LEXIS 16546",
            "2003 WL 21920243"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anton E. Barker v. Gary Fleming",
          "cluster_id": 791948,
          "cite": [
            "423 F.3d 1085",
            "2005 U.S. App. LEXIS 19372",
            "5 Cal. Daily Op. Serv. 8151"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gregory",
          "cluster_id": 2621432,
          "cite": [
            "147 P.3d 1201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alcala v. Woodford",
          "cluster_id": 8437569,
          "cite": [
            "334 F.3d 862",
            "2003 WL 21479370"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Brown",
          "cluster_id": 1272426,
          "cite": [
            "513 F.3d 1057",
            "2008 U.S. App. LEXIS 1266",
            "2008 WL 185528"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
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
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cross",
          "cluster_id": 2630721,
          "cite": [
            "132 P.3d 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ambrose Gill v. Robert J. Ayers, Warden Attorney General of the State of California",
          "cluster_id": 783480,
          "cite": [
            "342 F.3d 911",
            "2003 U.S. App. LEXIS 17979",
            "2003 Cal. Daily Op. Serv. 7843",
            "2003 WL 22020010"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hein v. Sullivan",
          "cluster_id": 1594,
          "cite": [
            "601 F.3d 897",
            "2010 U.S. App. LEXIS 7479",
            "2010 WL 1427588"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Milke v. Ryan",
          "cluster_id": 855224,
          "cite": [
            "711 F.3d 998",
            "2013 WL 979127",
            "2013 U.S. App. LEXIS 5102"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rodney J. Alcala v. Jeanne S. Woodford, Warden, of the California State Prison at San Quentin, Rodney J. Alcala v. Jeanne S. Woodford, Warden, of the California State Prison at San Quentin",
          "cluster_id": 782567,
          "cite": [
            "334 F.3d 862",
            "2003 Cal. Daily Op. Serv. 5645",
            "2003 Daily Journal DAR 7155",
            "2003 U.S. App. LEXIS 13039"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sivak v. Hardison",
          "cluster_id": 613265,
          "cite": [
            "658 F.3d 898",
            "2011 U.S. App. LEXIS 18568",
            "2011 WL 3907111"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mullen",
          "cluster_id": 2460107,
          "cite": [
            "259 P.3d 158",
            "171 Wash. 2d 881"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennison v. City and County of San Francisco",
          "cluster_id": 1196411,
          "cite": [
            "570 F.3d 1078",
            "2009 U.S. App. LEXIS 13882",
            "2009 WL 1758711"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jesse Gonzalez v. Robert Wong",
          "cluster_id": 618469,
          "cite": [
            "667 F.3d 965",
            "2011 U.S. App. LEXIS 24191",
            "2011 WL 6061514"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mejia v. Garcia",
          "cluster_id": 1199760,
          "cite": [
            "534 F.3d 1036",
            "2008 WL 2853384"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kohring",
          "cluster_id": 206598,
          "cite": [
            "637 F.3d 895",
            "2011 U.S. App. LEXIS 4763",
            "2011 WL 833263"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Price",
          "cluster_id": 1468715,
          "cite": [
            "566 F.3d 900",
            "2009 WL 1408117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roosevelt Moore v. M. Biter",
          "cluster_id": 1036737,
          "cite": [
            "725 F.3d 1184",
            "2013 WL 4011011",
            "2013 U.S. App. LEXIS 16321"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Albert Cunningham v. Robert Wong",
          "cluster_id": 814985,
          "cite": [
            "704 F.3d 1143",
            "2013 WL 69198",
            "2013 U.S. App. LEXIS 451"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James F. Horton, II v. Deneice Mayle, Warden",
          "cluster_id": 790305,
          "cite": [
            "408 F.3d 570",
            "2005 U.S. App. LEXIS 8121",
            "2004 WL 3327643"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jernigan",
          "cluster_id": 1446636,
          "cite": [
            "492 F.3d 1050",
            "2007 U.S. App. LEXIS 16185",
            "2007 WL 1965112"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Sublett",
          "cluster_id": 2630175,
          "cite": [
            "231 P.3d 231",
            "156 Wash. App. 160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Benjamin Wai Silva v. Jill Brown, Warden",
          "cluster_id": 791225,
          "cite": [
            "416 F.3d 980",
            "2005 U.S. App. LEXIS 15252",
            "2005 WL 1732765"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rene Blanco",
          "cluster_id": 788648,
          "cite": [
            "392 F.3d 382",
            "2004 U.S. App. LEXIS 26815",
            "2004 WL 2979747"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Benn v. Lambert:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(776954 OR 9494850 OR 9494851) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) AND court_id:(scotus OR ca9)",
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
        "triage_read": 4,
        "triage_snippet_classified": 74
      },
      "lane2_top_cited": {
        "query": "cites:(776954 OR 9494850 OR 9494851)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNiZzPTc4NTA2MSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28776954+OR+9494850+OR+9494851%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(776954 OR 9494850 OR 9494851)",
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
    "complete_query": "cites:(776954 OR 9494850 OR 9494851)",
    "indexed_citing_opinions": 127,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 776954,
        "count": 121,
        "count_source": "search"
      },
      {
        "opinion_id": 9494850,
        "count": 6,
        "count_source": "search"
      },
      {
        "opinion_id": 9494851,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 244,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/benn-v-lambert.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQyMzY2Mjgmcz0zMDY2MTgzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28776954+OR+9494850+OR+9494851%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 9494850,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 112845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 145122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 469158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 519281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 547559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 566407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 602901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 687686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 729651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 748634,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 754108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 755880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 765715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 768763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 771419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 1201923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 4711467,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 4711688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 6960900,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 7008694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 7009786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 9009924,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494850,
        "cited_id": 9434817,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 112845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 145122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 602901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 605585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 687686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 729651,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 748634,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 749834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 754108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 755880,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 765715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 768763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 771419,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 776953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 1186228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 1199674,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 776954,
        "cited_id": 1201923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 9494851,
        "cited_id": 4711467,
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
    "date_created": "2026-07-04T22:57:48Z",
    "date_modified": "2026-07-06T07:19:16Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T22:57:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T22:57:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:00:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T22:57:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Benn v. Lambert

```
<opinion type="majority">
<p id="b1040-7">OPINION</p>
<author id="b1040-8">REINHARDT, Circuit Judge.</author>
<p id="b1040-9">The State of Washington, through the superintendent of the Washington State Penitentiary, appeals the district court’s decision to grant Gary Michael Benn’s ha-beas corpus petition, arguing that the district judge erred in holding that the Washington State Supreme Court decision was contrary to or involved an unreasonable application of <em>Brady v. Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L.Ed.2d 215</a></span> (1963), and its progeny. Because we hold that the state court’s decision that there was no <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation in Benn’s case constitutes an unreasonable application of clearly established Supreme Court law, we affirm.</p>
<p id="b1040-10">I. FACTUAL BACKGROUND</p>
<p id="b1040-11">On February 10, 1988, Gary Michael Benn made a 911 call to the Pierce County Sheriffs Department from the home of his half-brother, Jack Dethlefsen, and reported finding his half-brother’s body as well as the body of his half-brother’s friend, Michael Nelson. Officer Junge of the Pierce County Sheriffs Department arrived at the scene three minutes later and observed the bodies of the two victims on the floor in the living room. Both men had been shot once in the chest and once in the back of the head. He checked them for vital signs and found none. The bodies were still warm and bleeding, suggesting that both men had been killed recently.</p>
<p id="b1040-13">There was a bullet hole in the couch in the living room consistent with someone having been shot while on the couch. There were also bloodstains that matched Dethlefsen’s blood type on both the couch itself and on a newspaper that was on it. The medical examiner testified that Deth-lefsen was shot in the chest while on the couch because only the chest wound would have allowed him to move around and end up on the floor where the police found him.</p>
<p id="b1040-14">There was a .45 caliber handgun on the floor between the two bodies and a baseball bat next to Dethlefsen’s body. Deth-lefseris head rested next to a gun cabinet and the glass face of the cabinet, which had a shotgun in it, had been broken. Police found a boot print that matched Benn’s boot on a piece of broken glass next to Dethlefsen’s elbow. There was also blood on one of Benn’s boots with spatter patterns consistent with Benn’s having shot Nelson in the head while standing next to his body.</p>
<p id="b1040-15">Benn was charged with two counts of premeditated murder with the aggravating circumstance that the murders were part of a common scheme or single act, and was given notice of the government’s intention to seek the death penalty. The defense conceded at trial that Benn had shot both Dethlefsen and Nelson, but claimed that the shootings were in self-defense after a spontaneous argument between Benn and Dethlefsen. The prosecution, however, contended that Benn had planned the killings primarily in order to cover up his participation with the victims in an arson-insurance-fraud scheme. At trial, the prosecution relied heavily on various incul-patory statements that Benn had allegedly made to Roy Patrick, a “jailhouse infor<page-number citation-index="1" label="1045">*1045</page-number>mant” who was in Benn’s cell block while Benn was awaiting trial, as well as on highly circumstantial evidence relating to the alleged arson.</p>
<p id="b1041-4">A. Additional Evidence at Trial</p>
<p id="b1041-5">On the day of the shootings, Benn had been at Larry Kilen’s barbershop before he went to Dethlefsen’s house. While at the barbershop, Benn spoke to Dethlefsen on the phone and Kilen heard him say “What the hell is going on? I will be right back — I will be right there. What’s the matter? What is that?” Benn told Kilen that Dethlefsen was drunk and wanted him to come over because he had fallen down. Multiple witnesses at trial testified that Dethlefsen was an alcoholic, and his autopsy revealed that he had a blood alcohol content of 0.07 at the time of his death. Similarly, Nelson’s autopsy revealed that he had a blood alcohol content of 0.11.</p>
<p id="b1041-6">Benn denied that he went to Dethlef-sen’s house with the intention of harming either Dethlefsen or Nelson. A police search of Benn’s car revealed that he had a .22 caliber pistol in the car that he had not taken inside the house with him. Benn did not testify at the trial and much of his version of the events was presented through statements he made to his brother, Monte Benn (“Monte”).</p>
<p id="b1041-7">Monte testified that Benn had described the following series of events to him: When Benn went into Dethlefsen’s house on the day of the shootings, he found a piece of paper on the kitchen counter with Gail Fisk’s phone number on it. Fisk was Benn’s ex girlfriend with whom he had been trying to reconcile. Benn thought that Dethlefsen and Nelson were harassing Fisk because he had seen Nelson’s car at Fisk’s house on occasion. Benn had questioned Dethlefsen about Fisk previously but Dethlefsen had denied harassing her. After Benn discovered the note with Fisk’s phone number on it, he took the note into the living room and confronted Dethlefsen. In response, Dethlefsen said, “Well Benny, you got me” and reached for the .45 caliber gun that he routinely kept on his living room coffee table. Benn then grabbed the gun and shot Dethlefsen in self-defense. After being shot, Dethlefsen moved toward the gun cabinet. Nelson then got up and threw a beer can at Benn. Benn remembered shooting Nelson, but did not remember much else.</p>
<p id="b1041-10">Monte testified that he got the impression that the shooting was in self-defense. He also told the jury that Dethlefsen had a reputation for violence in the community. Other evidence presented at the trial corroborated parts of Benn’s story. Experts testified that the path of the bullet that struck Dethlefsen’s chest and then entered the back of the couch was consistent with Dethlefsen being in the act of rising from the couch at the time he was first shot. Moreover, Deputy James Jones testified that Dethlefsen probably broke the glass face of the gun cabinet “as he fell ... after being wounded” or while he was “trying to get a weapon.” The defense theory was that Benn shot Dethlefsen a second time because Dethlefsen was trying to get another gun. During the investigation, the police also found an empty beer can underneath Nelson’s right knee. This was consistent with Benn’s claim that Nelson threw a beer can at him while he was standing next to the living room table near where the bodies were found.</p>
<p id="b1041-11">Roy Patrick, a “jail house informant” who shared a cell with Benn when Benn was awaiting trial, testified on behalf of the prosecution. According to Patrick’s testimony, Benn confessed to him and asked Patrick to help him find someone “on the outside” who would be willing to take the blame for the murders. Patrick testified that Benn drew diagrams of the murder scene and gave him details about the murder to relay to the person he found <page-number citation-index="1" label="1046">*1046</page-number>so that the person’s statements would be believable.</p>
<p id="b1042-4">The prosecution’s theory was that the shootings were part of a common plan or scheme. Patrick’s testimony provided critical support for that theory. Specifically, he testified that Benn told him about his involvement in a conspiracy with Deth-lefsen and Nelson to perpetrate an insurance fraud. According to Patrick’s testimony, Benn, Dethlefsen, and Nelson staged a “burglary” of Benn’s trailer and collected the insurance. Then, a few months later, they burned down the trailer and collected insurance again. Both times, however, Benn refused to share the proceeds with Dethlefsen and Nelson. Nelson and Dethlefsen then threatened to disclose the crimes to the police, and Benn killed them to keep them from doing so.</p>
<p id="b1042-5">Benn did in fact report a burglary of his trailer on October 12, 1987, but the only evidence of an insurance fraud with respect to that burglary (aside from Patrick’s testimony) was the fact that Benn reported that ivory carvings were taken in the burglary and the police recovered some ivory figures from Dethlefsen’s bedroom closet after he was killed. After the trial, however, a friend of the family stated that the half-brothers both owned ivory figures from Alaska.</p>
<p id="b1042-6">Similarly, there was a fire at Benn’s trailer on December 11, 1987, but there was little, if any, evidence, aside from Patrick’s testimony, that the fire was intentionally started. There was testimony that Dethlefsen, an electrician, had worked on the furnace in Benn’s trailer and that some possessions that Benn normally kept in the trailer were not there on the day of the fire. Additionally, Benn did tell Monte that he was nervous about fire insurance fraud charges being filed against him because he claimed more than he should have after the fire, but he never told Monte that he had started the fire. The prosecution emphasized that Benn sent in a payment for his home insurance on the day of the fire. According to the insurance agent, however, the payment was not late and it was to cover January and February insurance. Benn had already made payments to insure the trailer for December, the month of the fire.</p>
<p id="b1042-8">The defense attempted to prevent the arson-insurance-fraud theory from being mentioned at trial by arguing in a motion in limine that there was no evidence of arson. In ruling that the information was admissible, the trial court said “This is probably the key decision in this case.” The trial judge went on to state that:</p>
<blockquote id="A6l">So far as the probative value is concerned, it goes to the very heart of the case. It is the kind of evidence that the State must and needs to prove if it’s going to prove the aggravating factor that is involved in this case, and if it is going to prove premeditation. Without it, the State doesn’t have a case for aggravated murder, or maybe doesn’t have a case for pre-meditated murder. It is an essential ingredient.</blockquote>
<p id="b1042-9">In addition to testifying about Benn’s burglary-arson-insurance-fraud motive, Patrick also testified that Benn wanted to kill Dethlefsen because Dethlefsen had removed Benn from his will and had given Benn’s portion of his estate to a friend named William Hastings. Hastings testified that he was listed as a beneficiary in Dethlefsen’s will, although there was nothing in the estate because Dethlefsen was so much in debt. Hastings did, however, get $40,000 from a separate life insurance policy. Patrick did not say anything about a life insurance policy.</p>
<p id="b1042-10">Finally, Patrick testified that Benn told him that he had tried to hire someone named “Pete” to kill Dethlefsen for $500 but then changed his mind. Benn told Patrick that he wanted whoever took the rap for the murders to kill Pete. The pros<page-number citation-index="1" label="1047">*1047</page-number>ecution emphasized this point in closing arguments noting that Benn tried to “reach out” and kill someone from prison.</p>
<p id="b1043-5">The defense sought to impeach Patrick on cross-examination by establishing that Patrick was in jail with Benn because he had pled guilty to and was awaiting sentencing for second-degree arson. There was a 6 to 12 month sentencing range for this offense and the prosecution had originally asked for a 9 month sentence. Based on Patrick’s cooperation, he received 6 months rather than nine. With good time credits for his work in prison, however, Patrick would have needed to serve only an additional 35 days even if he had received the 9 month sentence originally sought by the prosecutors. Moreover, the prosecution downplayed the importance of the sentence reduction in closing arguments by stating “[t]he reward that he got was that in a 6 to 12 month sentence, he got six months instead of nine months. Big reward.”</p>
<p id="b1043-6">The defense also sought to impeach Patrick by eliciting testimony that Patrick had been ordered to pay costs and restitution for his arson conviction and had failed to do so; that he had previous convictions for fraud by wire, burglary, and arson; that he had been paid for his testimony as an informant; that the State was paying for his food and hotel expenses while he was testifying; and that the subpoena used to bring Patrick to the State of Washington for Benn’s trial protected him from arrest or criminal process while he was in town.</p>
<p id="b1043-10">During the trial, a third party told the defense that the police had executed a warrant to search Patrick’s hotel room based on a tip that Patrick was dealing drugs from the room. His room had been searched and crack pipes, a bong, rolling paper, a razor blade, and a copper brillo pad were recovered, but no arrests were made. The prosecution knew about this search and failed to disclose information about it to the defense. The defense did not learn the name of the confidential informant who had provided the information for the warrant until after the trial. At a later evidentiary hearing, the informant, Melvin Stevens, testified that Patrick was doing drugs while he was in Washington for Benn’s trial. Stevens also said that Patrick told him that Benn did not commit the murder, but that Patrick knew enough to convict him and needed the money.<footnotemark>1</footnotemark></p>
<p id="b1043-11">Walter “Pete” Hartman testified on behalf of the prosecution and said that Benn offered to pay him to kill Dethlefsen. Hartman said that he initially thought it was just talk and that he never took Benn up on his offer.<footnotemark>2</footnotemark> Denver Carter, a former <page-number citation-index="1" label="1048">*1048</page-number>roommate of Benn’s, testified for the prosecution as well and said that Benn admitted to Mm that he had shot Dethlefsen and Nelson. At one point, Carter said that Benn told him that a man named “Pete” owed him a favor and that Benn had a job for him, but that Benn never mentioned what the job was. Benn told Carter that, when Benn called Dethlefsen’s house on the day of the murder, no one was supposed to answer the phone, but <em>Benn </em>never explained what that meant.</p>
<p id="b1044-4">After deliberating for approximately seven and a half hours, the jury returned a verdict of guilty on both counts of premeditated murder. The jury also found that the murders were part of a common scheme or plan but did not find that they were the result of a single act of the defendant. The jury then recommended that Benn be sentenced to death, and he was.</p>
<p id="b1044-5">B. Evidence Revealed After Trial</p>
<p id="b1044-6">Although on December 16, 1988, over two years before the trial began, the defense requested that the prosecution disclose all evidence in its possession that was favorable to the defendant, a great deal of impeachment evidence relating to Patrick, as well as important exculpatory evidence relating to the alleged arson-insurance-fraud allegation, was not turned over to the defense until after both the guilt and penalty phases of the trial had ended.</p>
<p id="b1044-8">(1) <em>Impeachment Evidence Related to Patrick</em></p>
<p id="b1044-9">Even though the prosecuting attorneys had taken their first statements from Patrick over a year before the trial, Patrick’s identity was not disclosed to the defense until the day before trial when he was added to the witness list.<footnotemark>3</footnotemark> Pierce County Assistant Prosecuting Attorney Michael Johnson lied to the defense and stated that Patrick’s identity could not be disclosed because he was in a witness protection program. It was later discovered that he was never in such a program.</p>
<p id="b1044-10">The day that Benn’s trial was scheduled to begin, the defense brought to the court’s attention the fact that <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material relating to Patrick had not been provided. The defense noted specifically that it did not have information about Patrick’s prior contacts with the police, including whether Patrick had made statements in the past that had turned out to be incorrect. The trial court agreed and ordered the prosecution to turn over any written material relating to Patrick’s contacts with law enforcement in the year prior to the murders. No such material was ever produced. The court also stated that “the prosecutor would have an obligation to tell [the defense] if there’s prior situations where the informant had not been truthful.” Prosecutor Johnson acknowledged this obligation and stated that they “ha[d] been notified of no such situations, your Honor.” The prosecution never turned over any information that Patrick had en<page-number citation-index="1" label="1049">*1049</page-number>gaged in improper conduct while acting as an informant. It was later discovered that the prosecution did not attempt to obtain this information from any of the police detectives working on the case. Additionally, the defense later discovered that Detectives Ronald Lewis and Thomas Paduk-iewicz, both of whom supervised Patrick while he was assisting in law enforcement investigations, knew that Patrick had stolen both drugs and money during drug busts and that he had lied to the police about it. The defense was never told about this. Detective Padukiewicz had even gone so far as to write up a “deactivation memo” stating that Patrick could no longer work as an informant because he would not abide by department rules. The defense was never told about Patrick’s deactivation.</p>
<p id="b1045-5">The defense was also not informed that Patrick had broken into the evidence room of the California Bureau of Narcotics Enforcement while working as an informant and had stolen drugs that the police had previously seized. Nor was the defense told that, as a result of this offense, Patrick was charged with burglary and numerous counts of obstruction of justice and ultimately pled guilty to burglary.</p>
<p id="b1045-6">The state did not inform defense counsel that Patrick had admitted to making false charges while in prison on a fraud conviction in the early 1980’s. Patrick had believed that he could get his time reduced if he reported the presence of firearms within the prison. He therefore had shotguns smuggled into the prison and then told the officials that he had found them. The prison officials discovered the scheme, and Patrick’s prison sentence was extended.</p>
<p id="b1045-7">The prosecution failed to disclose that Patrick was given $150 during Benn’s trial as an advance payment for a video-tape that Patrick claimed he had in his possession, showing a prostitute being murdered by Benn and several other men. Patrick said that the video was related to the “Green River case,” a high profile serial murder investigation. Patrick never produced the tape, and the detectives working on the case said that they thought Patrick was lying about its existence, and that his story about Benn being involved in the “Green River” murders was “trash.” The detectives also stated that they had spoken with the prosecutors in Benn’s case about the tape and the money that was paid to Patrick. The prosecution, however, never told the defense about either the false tale of a “Green River” murder tape or the payment that Patrick had received.</p>
<p id="b1045-9">When Patrick was in Washington for Benn’s trial, he was stopped for a traffic offense and arrested because of some outstanding warrants. He called Prosecutor Johnson from jail, and Johnson ensured that he was released without being charged. The defense was never told about the arrest or Johnson’s actions.</p>
<p id="b1045-10">During the trial, the Fife County Police Department submitted police reports to the Pierce County prosecutor requesting that Patrick be charged with burglary. The prosecutor’s office entered an “NCF” (no charges filed) the same day that closing arguments ended in the penalty phase of Benn’s trial. This fact was never disclosed to the defense.</p>
<p id="b1045-11">During Benn’s trial, the prosecution arranged to postpone the filing of a warrant that was going to be issued because Patrick had violated probation. Patrick’s probation officer had been told by the prosecutors not to do anything on the violation report or the order to issue a bench warrant. The warrant did not issue until two weeks after the verdict in Benn’s case. The prosecution never told the defense that it had prevented the issuance of the warrant.</p>
<p id="b1045-12">Testimony at the state habeas evidentia-ry hearing revealed that Patrick had acted <page-number citation-index="1" label="1050">*1050</page-number>as an informant in a murder case prior to Benn’s trial, although at the trial he denied ever having done so previously. The defense was never told that Patrick had been an informant in a prior murder case and that in that case also he had claimed that the defendant had confessed to him while in jail.</p>
<p id="b1046-4">At trial, Patrick denied that he used drugs while acting as an informant; however, testimony at a post-conviction eviden-tiary hearing revealed that he continuously used drugs during his time. as an informant and that the police knew about it. This information was not disclosed to the defense.</p>
<p id="b1046-5">(2) <em>Exculpatory Evidence Related to the Arson-Insurance-Fraud Allegation</em></p>
<p id="b1046-6">The prosecution turned over two reports describing the December 11, 1987 fire at Benn’s trailer. The first was a February 12, 1988 report tentatively concluding that the fire was an accident. After this report was prepared, Deputy Fire Marshal Ted Thompson and Electrical Inspector Walter Erickson conducted a more thorough reexamination of the site. After the reexamination, Thompson and Erickson both conclusively determined that the fire in Benn’s trailer was accidental. According to Erickson, the Coleman furnace in Benn’s trailer was the same make and model as the one that he owned, and this particular make and model had been recalled by the manufacturer due to a flaw that causes fires. Moreover, Fire Marshal Thompson concluded that the fire was accidental because:</p>
<blockquote id="b1046-7">First, it is not uncommon for electrical heaters in older mobile homes to accidentally malfunction and cause fires. Second, there were no accelerants, such as gasoline in the trailer. Third, it is not uncommon for electrical heaters to malfunction in the winter .... Fourth, I opened up the front of the electrical heater and everything appeared to be in place; I observed nothing suspicious .... My fifth reason for determining the fire was accidental, not arson, was that I observed only one locale where the fire originated (the furnace), not multiple locales. Sixth, I saw no signs of forced entry, which are indicative of arson.</blockquote>
<p id="b1046-9">After the re-examination, a second and more detailed report was prepared on March 30, 1988. The second report, which was turned over to the defense, was misleading. Its only reference to the conclusions of Fire Marshal Thompson and Electrical Inspector Erickson was in a section stating that there was “no fault or failure” of the lead electrical wire and no evidence of tampering with the fuse panel. The March 30, 1988 report did not state that both the fire inspector and deputy marshal had concluded that the fire was accidental and could not have resulted from arson. Rather, it offered no definitive conclusion regarding the cause of the fire. It did not state that there had been a manufacturer’s recall of this type of furnace and that it was the same type of furnace that Erickson had in his own home. To the contrary, it suggested that Coleman furnaces did not cause fires. Specifically, the March report stated that A1 Pearson, the furnace technician, said that “he could find and think of no situation in which a furnace[such as a Coleman] had caused a fire in a mobile home.” Finally, the report did not relate the six reasons Fire Marshal Thompson gave for concluding that the fire was accidental.</p>
<p id="b1046-10">II. PROCEDURAL HISTORY</p>
<p id="b1046-11">Benn appealed his convictions as well as his capital sentence. His direct appeals were denied by the Washington Supreme Court in <em>Washington v. Benn, </em><span class="citation" data-id="9560518"><a href="/opinion/1201923/state-v-benn/" aria-description="Citation for case: State v. Benn">120 Wash.2d 631</a></span>, <span class="citation" data-id="9560518"><a href="/opinion/1201923/state-v-benn/" aria-description="Citation for case: State v. Benn">845 P.2d 289</a></span> (1993), with <page-number citation-index="1" label="1051">*1051</page-number>three justices dissenting. Benn then initiated state habeas corpus proceedings and an evidentiary hearing was held. The Washington Supreme Court denied the state habeas petition. <em>In re Benn, </em><span class="citation" data-id="4711467"><a href="/opinion/4907353/in-re-the-personal-restraint-of-benn/" aria-description="Citation for case: In re the Personal Restraint of Benn">134 Wash.2d 868</a></span>, <span class="citation multiple-matches"><a href="/c/P.2d/952/116/">952 P.2d 116</a></span> (1998). It did not deny that the state improperly withheld evidence to which Benn was entitled, but it found that the state’s actions were not prejudicial. <em>See id. </em>Two justices dissented, arguing that Benn should have received a new trial because of the state’s failure to turn over exculpatory and impeachment material. <em>Id.</em></p>
<p id="b1047-5">Benn filed a federal habeas petition in the Western District of Washington alleging 22 errors, including his allegation that the prosecution withheld crucial exculpatory and impeachment evidence in violation of his due process rights. The district court agreed with Benn that material evidence had been withheld in violation of his constitutional rights, granted his petition for a writ of habeas corpus, and ordered a new trial without even considering the 21 other grounds of error asserted in his petition. <em>Benn v. Wood, </em>No. C98-5131RDB, <span class="citation no-link">2000 WL 1031361</span> (W.D.Wash.June 30, 2000). The state now appeals the district court’s decision. We affirm the district court.</p>
<p id="b1047-8">III. STANDARD OF REVIEW</p>
<p id="b1047-9">We review a district court’s decision to grant a petition for a writ of habeas corpus <em>de novo. Miles v. Prunty, </em><span class="citation" data-id="765715"><a href="/opinion/765715/willie-lee-miles-v-kw-prunty-warden-attorney-general-of-the-state-of/#1105" aria-description="Citation for case: Willie Lee Miles v. K.W. Prunty, Warden Attorney General...">187 F.3d 1104, 1105</a></span> (9th Cir.1999). Because Benn’s petition was filed after April 24, 1996, the amendments to <span class="citation no-link">28 U.S.C. § 2254</span> under the Anti-Terrorism and Effective Death Penalty Act (“AEDPA”) apply. <em>Van Tran v. Lindsey, </em><span class="citation" data-id="768763"><a href="/opinion/768763/tuan-van-tran-v-gary-lindsey-warden-salinas-valley-state-prisons-state-of/#1148" aria-description="Citation for case: Tuan Van Tran v. Gary Lindsey, Warden Salinas Valley...">212 F.3d 1143, 1148</a></span> (9th Cir.2000).<footnotemark>4</footnotemark></p>
<p id="b1047-10">Under AEDPA, a federal court may grant a writ of 'habeas corpus to a state prisoner only if the state court’s decision is “contrary to, or involve[s] an unreasonable application of, clearly established Federal law, as determined by the Supreme Court of the United States” or is “based on an unreasonable determination of the facts in light of the evidence presented” in the state courts. <span class="citation no-link">28 U.S.C. § 2254</span>(d). A state court decision is “contrary to” clearly established federal law if it “failed to apply the correct controlling authority from the Supreme Court.” <em>Shackleford v. Hubbard, </em><span class="citation" data-id="771419"><a href="/opinion/771419/william-lee-shackleford-v-susan-hubbard-warden/#1077" aria-description="Citation for case: William Lee Shackleford v. Susan Hubbard, Warden">234 F.3d 1072, 1077</a></span> (9th Cir.2000); <em>see also Williams v. Taylor, </em><span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#405" aria-description="Citation for case: Williams v. Taylor">529 U.S. 362, 405-07</a></span>, <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/" aria-description="Citation for case: Williams v. Taylor">120 S.Ct. 1495</a></span>, <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/" aria-description="Citation for case: Williams v. Taylor">146 L.Ed.2d 389</a></span> (2000); <em>Packer v. Hill, </em><span class="citation" data-id="7008694"><a href="/opinion/7102904/packer-v-hill/" aria-description="Citation for case: Packer v. Hill">277 F.3d 1092</a></span> (9th Cir.2002).<footnotemark>5</footnotemark> A <page-number citation-index="1" label="1052">*1052</page-number>state court decision constitutes an “unreasonable application” of clearly established federal law “if the state court identifies the correct governing legal rule ... but unreasonably applies it to the facts of the particular state prisoner’s case.” <em>Williams, </em><span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#407" aria-description="Citation for case: Williams v. Taylor">529 U.S. at 407</a></span>,<span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/" aria-description="Citation for case: Williams v. Taylor">120 S.Ct. 1495</a></span>.<footnotemark>6</footnotemark></p>
<p id="b1048-4">In <em>In re Benn,</em><footnotemark><em>7</em></footnotemark><em> </em>the Washington Supreme Court applied the rule in <em>Brady v. Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L.Ed.2d 215</a></span> (1963), and its progeny<footnotemark>8</footnotemark> — a rule clearly established by controlling Supreme Court precedent. Therefore, the state court ruling is properly analyzed under the “unreasonable application” clause of AEDPA. To be “unreasonable” under AEDPA, the Washington Supreme Court decision must leave us “with a ‘firm conviction’ that one answer, the one rejected by the[state] court, was correct and the other, the application of the federal law that the [state] court adopted, was erroneous — in other words that clear error occurred.” <em>Van Tran, </em><span class="citation" data-id="768763"><a href="/opinion/768763/tuan-van-tran-v-gary-lindsey-warden-salinas-valley-state-prisons-state-of/#1153" aria-description="Citation for case: Tuan Van Tran v. Gary Lindsey, Warden Salinas Valley...">212 F.3d at 1153-54</a></span>. When analyzing the state court decision to determine if there was “clear error,” “we must first consider whether the state court erred; only after we have made that determination may we then consider whether any error involve[s] an unreasonable application of controlling law....” <em>Van Tran, </em><span class="citation" data-id="768763"><a href="/opinion/768763/tuan-van-tran-v-gary-lindsey-warden-salinas-valley-state-prisons-state-of/#1155" aria-description="Citation for case: Tuan Van Tran v. Gary Lindsey, Warden Salinas Valley...">212 F.3d at 1155</a></span>. Here, we conclude that the Washington Supreme Court erred in ruling that the prosecution’s failure to disclose critical impeachment and exculpatory evidence did not violate <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and its progeny. Because we also hold that the state court’s ruling was clearly erroneous and thus objectively unreasonable under AEDPA, Benn is entitled to habeas relief.</p>
<p id="b1048-8">IY. THE WASHINGTON SUPREME COURT’S OBJECTIVELY UNREASONABLE <em>BRADY </em>ERRORS</p>
<p id="b1048-9">A. Introduction</p>
<p id="b1048-10">In <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>the Supreme Court held that the “suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or punishment, irrespective of the good faith or bad faith of the prosecution.” <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland"><em>Id. </em>at 87</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span>. Supreme Court cases following <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>clearly established that the defendant must prove three elements in order to show a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation. First, the evidence at issue must be favorable to the accused, because it is either exculpatory or impeachment material. <em>See United States v. Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#676" aria-description="Citation for case: United States v. Bagley">473 U.S. 667, 676</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">87 L.Ed.2d 481</a></span> (1985). Second, the <page-number citation-index="1" label="1053">*1053</page-number>evidence must have been suppressed by the State, either willfully or inadvertently. <em>See United States v. Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#110" aria-description="Citation for case: United States v. Agurs">427 U.S. 97, 110</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">49 L.Ed.2d 342</a></span> (1976). Third, prejudice must result from the failure to disclose the evidence. <em>See Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley">473 U.S. at 678</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span>.</p>
<p id="b1049-5">Evidence is deemed prejudicial, or material, only if it undermines confidence in the outcome of the trial. <em>See Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#676" aria-description="Citation for case: United States v. Bagley">473 U.S. at 676</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span>; <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#111" aria-description="Citation for case: United States v. Agurs">427 U.S. at 111-12</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>.<footnotemark>9</footnotemark> For purposes of determining prejudice, the withheld evidence must be analyzed “in the context of the entire record.” <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U.S. at 112</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>. Moreover, we analyze all of the suppressed evidence together, using the same type of analysis that we employ to determine prejudice in ineffective assistance of counsel cases. <em>See Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley">473 U.S. at 682</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span> (opinion of Blackmun, J.);<footnotemark>10</footnotemark> <em>see also United States v. Shaffer, </em><span class="citation" data-id="469158"><a href="/opinion/469158/united-states-v-william-shaffer/#688" aria-description="Citation for case: United States v. William Shaffer">789 F.2d 682, 688-89</a></span> (9th Cir.1986) (analyzing collectively the prejudice resulting from the state’s suppression of four different pieces of impeachment material).</p>
<p id="b1049-6">The Supreme Court has not limited the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule to cases in which the defense has made a pretrial request for specific evidence. <em>See Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U.S. at 103-07</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>. In <em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">Agurs</a></span>, </em>the Court held that <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>applies where the defense makes a general request for exculpatory evidence and even where the defense does not make a request for such evidence at all. <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#106" aria-description="Citation for case: United States v. Agurs"><em>See id. </em>at 106</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>. Thus, the terms “suppression,” “withholding,” and “failure to disclose” have the same meaning for <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>purposes. Similarly, the disclosure requirements set forth in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>apply to a prosecutor even when the knowledge of the exculpatory evidence is in the hands of another prosecutor. <em>See Giglio v. United States, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U.S. 150, 154</a></span>, <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">92 S.Ct. 763</a></span>, <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">31 L.Ed.2d 104</a></span> (1972) (“The prosecutor’s office is an entity and as such it is the spokesman for the Government.”).</p>
<p id="b1049-10">Here, the state does not contest that it was required to disclose the extensive impeachment evidence pertaining to Patrick. It simply contends, as did the Washington Supreme Court, that the failure to produce that evidence did not result in prejudice under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>. </em>We conclude that the state court erred in that determination. Similarly, we conclude that it erred in holding that there was no <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em><page-number citation-index="1" label="1054">*1054</page-number>violation resulting from the prosecution’s failure to disclose exculpatory evidence about the cause of the fire at Benn’s trailer. Because we conclude that the suppressed impeachment evidence and the suppressed exculpatory evidence are each, standing alone, sufficiently prejudicial to merit relief under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>they are <em>a forti-ori </em>sufficiently prejudicial when analyzed together. We therefore hold that the state court erred when conducting its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>analysis. We also hold that the state court ruling was clearly erroneous and constitutes an “unreasonable application” of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and its progeny. Therefore, Benn is entitled to habeas relief.</p>
<p id="b1050-4">B. The Prosecution’s Failure to Disclose Critical Impeachment Evidence THAT COULD HAVE BEEN USED TO Undermine Patrick’s Credibility is Sufficient, Standing Alone, to Constitute a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>Violation.</p>
<p id="b1050-5">The prosecution failed to disclose multiple pieces of critical impeachment information that could have been used to undermine the credibility of Patrick, a prosecution witness whose testimony was crucial to the state’s claims of premeditation and common scheme or plan, as well as to the state’s theory regarding Benn’s principal motive for killing the two individuals. Because Patrick is a witness whose “ ‘reliability ... may well be determinative of guilt or innocence,’ nondisclosure of evidence affecting [his] credibility falls within [the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>] rule.” <em>Giglio, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#154" aria-description="Citation for case: Giglio v. United States">405 U.S. at 154</a></span>, <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">92 S.Ct. 763</a></span> (quoting <em>Napue v. Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U.S. 264, 269</a></span>, <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">79 S.Ct. 1173</a></span>, <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">3 L.Ed.2d 1217</a></span> (1959)); <em>see also Carriger v. Stewart, </em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/#479" aria-description="Citation for case: Carriger v. Stewart">132 F.3d 463, 479</a></span> (9th Cir.1997) (“Material evidence required to be disclosed includes evidence bearing on the credibility of government witnesses.”); <em>Shaffer, </em><span class="citation" data-id="469158"><a href="/opinion/469158/united-states-v-william-shaffer/#689" aria-description="Citation for case: United States v. William Shaffer">789 F.2d at 689</a></span> (“[Ejvidence affecting the credibility of a government witness has been held to be material under the Brady doctrine.”).</p>
<p id="b1050-7">(I) <em>Patrick’s history of misconduct while acting as an informant</em></p>
<p id="b1050-8">The prosecution failed to disclose evidence of Patrick’s persistent misconduct while acting as an informant, even though the trial judge explicitly ordered the state to disclose all such information to the defense. Specifically, the state failed to disclose: that Patrick, while acting as an informant, had stolen both drugs and money during drug busts and had lied to police about it; that a detective had written a deactivation memo stating that Patrick could no longer work as an informant because he could not be trusted to follow departmental rules; that Patrick, while acting as an informant, had broken into an evidence room and stolen drugs, resulting in burglary and obstruction of justice charges being filed against him; that Patrick had smuggled guns into a prison where he was housed, concealed his own involvement, and then told prison officials of the presence of the weapons in an effort to have his sentence reduced; and that although Patrick testified at trial that he did not ever use drugs, he continually did so during his time as an informant.</p>
<p id="b1050-9">The state does not contest that this evidence was impeachment material that was suppressed by the prosecution. Rather, it contends that the suppressed material was cumulative and its suppression harmless because Patrick was sufficiently impeached by questions about his history as a paid informant in drug cases, his prior convictions, the reduction in his arson sentence, and the fact that the state was paying his motel and food bills. <em>See United States v. Vgeri </em><span class="citation" data-id="693028"><a href="/opinion/693028/united-states-v-leonid-vgeri-united-states-of-america-v-ervin-stramarko/#880" aria-description="Citation for case: United States v. Leonid Vgeri, United States of America...">51 F.3d 876, 880</a></span> (9th Cir.1995) (undisclosed impeachment evidence is immaterial and cumulative when the witness is already sufficiently <page-number citation-index="1" label="1055">*1055</page-number>impeached); <em>see also Ortiz v. Stewart, </em><span class="citation" data-id="755880"><a href="/opinion/755880/ignacio-alberto-ortiz-petitioner-appellant-v-terry-stewart/#936" aria-description="Citation for case: Ignacio Alberto ORTIZ, Petitioner-Appellant, v. Terry...">149 F.3d 923, 936</a></span> (9th Cir.1998) (same).</p>
<p id="b1051-5">The undisclosed impeachment evidence in this case was substantial and was far more damaging to Patrick’s credibility than the impeachment evidence available to the defense at trial. If anything, the police-sanitized version of Patrick’s fifteen years of work as an informant increased his credibility in the eyes of the jurors. The jury was told only that the police routinely relied on Patrick for help with drug investigations. Information demonstrating that Patrick had regularly lied to the authorities while acting as an informant, was untrustworthy and deceptive, and was even willing to fabricate crimes in order to gain a benefit for himself would have severely undermined his credibility. The mere fact that a prosecution witness has a prior record, even when combined with other impeachment evidence that a defendant introduces, does not render otherwise critical impeachment evidence cumulative. <em>See, e.g., United States v. Steinberg, </em><span class="citation" data-id="729651"><a href="/opinion/729651/united-states-of-america-plaintiff-appellee-v-david-michael-steinberg/#1489" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellee, v. David...">99 F.3d 1486, 1489-92</a></span> (9th Cir.1996) (holding that the government’s failure to disclose that an informant had been involved in two illegal transactions involving counterfeit currency was material even though the informant had been impeached through questioning about a plea agreement that he had made with the government). In cases in which the witness is central to the prosecution’s case, the defendant’s conviction indicates that in all likelihood the impeachment evidence introduced at trial was insufficient to persuade a jury that the witness lacked credibility. Therefore, the suppressed impeachment evidence, assuming it meets the test for disclosure, takes on an even greater importance.</p>
<p id="b1051-6">For example, in <em>Carriger v. Stewart, </em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/#479" aria-description="Citation for case: Carriger v. Stewart">132 F.3d at 479</a></span>, we held that information that an informant had been unreliable in the past constituted material impeachment evidence for <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>purposes. Like Patrick, the informant in <em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/" aria-description="Citation for case: Carriger v. Stewart">Carriger</a></span> </em>came to the police with an offer of information and received a benefit for providing the information. <span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/#465" aria-description="Citation for case: Carriger v. Stewart"><em>Id. </em>at 465</a></span>. We stated that “[wjhen the state decides to rely on the testimony of such a witness, it is the state’s obligation to turn over all information bearing on that witness’s credibility.” <span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/#480" aria-description="Citation for case: Carriger v. Stewart"><em>Id. </em>at 480</a></span>. As we said, “[t]his must include the witness’s criminal record, including prison records, and any information therein which bears on credibility.” <em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/" aria-description="Citation for case: Carriger v. Stewart">Id.</a></span> </em>Like Patrick, the informant in <em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/" aria-description="Citation for case: Carriger v. Stewart">Carriger</a></span> </em>was impeached at trial with evidence of prior convictions. In fact, the defense’s impeachment of the informant in <em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/" aria-description="Citation for case: Carriger v. Stewart">Carriger</a></span> </em>was more extensive than Benn’s impeachment of Patrick. At Carriger’s trial, it was shown that the informant was a career burglar with six previous felonies, <span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/#480" aria-description="Citation for case: Carriger v. Stewart"><em>see id. </em>at 480</a></span>, whereas here, Patrick was impeached with only three previous convictions.</p>
<p id="b1051-8">In holding that the suppressed evidence was material in <em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/" aria-description="Citation for case: Carriger v. Stewart">Carriger</a></span>, </em>we stated that:</p>
<blockquote id="b1051-9">The district court erred when it concluded that Carriger had not been prejudiced by the withholding of the information because the jury already knew [that the informant] was a burglar testifying with immunity. The telling evidence that remained undisclosed included the length of [the informant’s] record ... and, more important, his long history of lying to the police.</blockquote>
<p id="b1051-10"><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/#481" aria-description="Citation for case: Carriger v. Stewart"><em>Id. </em>at 481</a></span>. Here, the defense was not informed of Patrick’s burglary and obstruction of justice charges, his fraudulent attempt to smuggle guns into a prison, or his multiple thefts of drugs and money; nor was it informed of the fact that Patrick provided false information to law enforcement. As a result, the jury was not told about Patrick’s record of criminal miscon<page-number citation-index="1" label="1056">*1056</page-number>duct while acting as an informant, nor that he had repeatedly lied to the police.</p>
<p id="b1052-4">The present case is also similar to <em>United States v. Brumel-Alvarez, </em><span class="citation" data-id="9009924"><a href="/opinion/9016822/united-states-v-brumel-alvarez/" aria-description="Citation for case: United States v. Brumel-Alvarez">991 F.2d 1452</a></span> (9th Cir.1992), in which the government’s principal witness was a police informant who had been involved in illegal drug operations for twenty-five years. The government withheld a memorandum that detailed false claims that the police informant had made to government agents. <span class="citation" data-id="9009924"><a href="/opinion/9016822/united-states-v-brumel-alvarez/#1459" aria-description="Citation for case: United States v. Brumel-Alvarez"><em>Id. </em>at 1459</a></span>. We stated that the informant’s credibility “was an important issue in the case” and that “[e]vidence that he lied during the investigation ... would be relevant to his credibility and the jury was entitled to know of it.” <span class="citation" data-id="9009924"><a href="/opinion/9016822/united-states-v-brumel-alvarez/#1463" aria-description="Citation for case: United States v. Brumel-Alvarez"><em>Id. </em>at 1463</a></span>; <em>see also United States v. Bernal-Obeso, </em><span class="citation" data-id="602901"><a href="/opinion/602901/united-states-v-filemon-bernal-obeso/#335" aria-description="Citation for case: United States v. Filemon Bernal-Obeso">989 F.2d 331, 335</a></span> (9th Cir.1993) (“[A] lie to the authorities paying for [an informant’s] services ... would be relevant evidence as to the informant’s credibility.”).</p>
<p id="b1052-5">Evidence that Patrick continually used drugs while acting as an informant and that the police knew about this but chose not to prosecute him would also be relevant to show his bias. If Patrick was continually receiving a benefit from the prosecution — the ability to use drugs without fear of criminal repercussions — that would have given him a motive to provide the prosecution with inculpatory information, even if he had to fabricate it.</p>
<p id="b1052-6">Finally, evidence that Patrick was using drugs during the trial would reflect on his competence and credibility as a witness. There was no evidence at trial to impeach Patrick’s competence or his ability to recollect or perceive the events. Thus, evidence of his drug use would have provided the defense with a new and different ground of impeachment.</p>
<p id="b1052-7">Were there no other pieces of withheld evidence in this case, we would hold that the suppression of impeachment evidence about Patrick’s criminal misconduct and repeated lies to the police, while acting as an informant, is, standing alone, sufficiently prejudicial to establish a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation. The fact that other impeachment evidence was introduced by the defense does not affect our conclusion. Where, as here, there is reason to believe that the jury relied on a witness’s testimony to reach its verdict despite the introduction of impeachment evidence at trial, and there is a reasonable probability that the suppressed impeachment evidence, when considered together with the disclosed impeachment evidence, would have affected the jury’s assessment of the witness’s credibility, the suppressed impeachment evidence is prejudicial. We need not further address the prejudice issue at this point, however, given our holding that the withheld impeachment evidence, when analyzed collectively, materially undermines our confidence in the verdict. <em>See </em>discussion of prejudice <em>infra </em>Section IV.B.5.</p>
<p id="b1052-9">(2) <em>Patrick’s false allegation about Benn</em></p>
<p id="b1052-10">There is one specific lie of Patrick’s that, standing alone, would be sufficient to constitute a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation. The prosecution failed to disclose that Patrick approached the police a week before trial claiming that he had a videotape showing that Benn was involved in a killing that was part of a notorious unsolved murder case (the Green River murders) unrelated to the Dethlef-sen-Nelson killings. The prosecution also failed to disclose that Patrick was given $150 to produce the tape, that he never did so, and that the detectives concluded that he was lying about the tape’s existence and about Benn’s involvement in the other murders. This evidence could have been used to show that Patrick was willing to lie <em>about Benn </em>and even to accuse him falsely of <em>murder, </em>if doing so would result in even a minimal benefit to him. In <em>Bernal-Obeso, </em><span class="citation" data-id="602901"><a href="/opinion/602901/united-states-v-filemon-bernal-obeso/#336" aria-description="Citation for case: United States v. Filemon Bernal-Obeso">989 F.2d at 336</a></span>, we described the difference between general evidence of un-<page-number citation-index="1" label="1057">*1057</page-number>trustworthiness and specific evidence that a witness has lied as follows: “All the other evidence used by the defense to punch holes in [the informant’s] credibility amounted only to circumstantial reasons why[the informant] might alter the truth to continue to feather his own nest. A lie would be direct proof of this concern, eliminating the need for inferences.”</p>
<p id="b1053-5">The evidence regarding the nonexistent videotape would have seriously impeached Patrick in a way that the evidence presented at trial could not, and even that the evidence of other lies could not. It provided direct proof that Patrick was willing to he specifically about Benn’s involvement in a murder and to accuse him falsely of a capital offense. Patrick, when confronted with his lies at the state habeas evidentiary hearing, confessed that “I would lie — I would always lie about me. I would always do that. I was a liar.” The jury, however, never heard that Patrick had lied about anything. The evidence regarding Patrick’s tale of the videotape was “direct proof’ of his lack of credibility, and the failure to disclose his fabrication was prejudicial.</p>
<p id="b1053-6">(3) <em>Patrick’s exposure to prosecution</em></p>
<p id="b1053-7">The <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>rule requires prosecutors to disclose any benefits that are given to a government informant, including any lenient treatment. <em>See, e.g., Giglio, </em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/#150" aria-description="Citation for case: Giglio v. United States">405 U.S. at 150</a></span>, <span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">92 S.Ct. 763</a></span> (failure to disclose promise of immunity). During Benn’s trial, Patrick was stopped for a traffic offense and arrested because he had outstanding warrants. He called the prosecutor from jail and the prosecutor arranged for him to be released without being charged. This benefit was never disclosed to the defense. Also during Benn’s trial, the Fife police department asked the prosecution to charge Patrick with burglary, but the prosecutor’s office dismissed the charges. Once again, this information was withheld from the defense. The prosecution also arranged to postpone the filing of a warrant that was supposed to issue because Patrick had violated his probation. The warrant was delayed for two weeks — until after the Benn trial ended. The government failed to inform defense counsel about this benefit as well.</p>
<p id="b1053-9">We have explained the reason why information regarding prosecution-provided benefits constitutes <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material. In <em>Singh v. Prunty, </em><span class="citation" data-id="754108"><a href="/opinion/754108/jaitsen-j-singh-petitioner-appellant-v-kw-prunty-warden-attorney/" aria-description="Citation for case: Jaitsen J. SINGH, Petitioner-Appellant, v. K.W. PRUNTY,...">142 F.3d 1157</a></span> (9th Cir.1998), we stated:</p>
<blockquote id="b1053-10">Disclosure of an agreement to provide such benefits, as well as evidence of the benefits themselves, could have allowed the jury to reasonably conclude that [the informant] had a motive other than altruism for testifying on behalf of the State. Such a finding could have substantially impeached [the informant’s] credibility as a witness.</blockquote>
<p id="b1053-11"><span class="citation" data-id="754108"><a href="/opinion/754108/jaitsen-j-singh-petitioner-appellant-v-kw-prunty-warden-attorney/#1162" aria-description="Citation for case: Jaitsen J. SINGH, Petitioner-Appellant, v. K.W. PRUNTY,..."><em>Id. </em>at 1162</a></span>. Here, too, a jury could have reasonably concluded that Patrick had “a motive other than altruism.”</p>
<p id="b1053-12">The state contends that the information regarding benefits was cumulative and immaterial because the defense cross-examined Patrick about his immunity from arrest during the trial and about the reduced sentence he received in exchange for his testimony. The reduced sentence that Patrick received did not provide any significant benefit to him. With good time credits for his. work in prison, Patrick would have served only an additional 35 days had he received the longer sentence originally sought by the prosecutors. In addition, the state effectively downplayed the importance of this benefit in closing arguments by stating, “[t]he reward that he got was that in a 6 to 12 month sentence, he got six months instead of nine months. Big reward.”</p>
<p id="b1053-13">Moreover, as we pointed out earlier, the state cannot satisfy its <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em><page-number citation-index="1" label="1058">*1058</page-number>obligation to disclose exculpatory and impeachment evidence “by making some evidence available and asserting that the rest would be cumulative. Rather, the state is obligated to disclose ‘all material information casting a shadow on a government witness’s credibility.’ ” <em>Carriger, </em><span class="citation" data-id="6960900"><a href="/opinion/7057172/carriger-v-stewart/#481" aria-description="Citation for case: Carriger v. Stewart">132 F.3d at 481-82</a></span> (internal citations omitted). Here, the number and nature of the undisclosed benefits was such that they would have impeached Patrick more effectively than the evidence that he was immune from arrest during the trial. The undisclosed benefits that Patrick received added significantly to the benefits that were disclosed and certainly would have “cast a shadow” on Patrick’s credibility. Thus, their suppression was material.</p>
<p id="b1054-4">(4) <em>Patrick’s experience as an informant</em></p>
<p id="b1054-5">At trial, Patrick denied that he had ever previously been an informant in a murder case, but in fact he had. The state argues that this undisclosed evidence about Patrick’s history was not material; however, in <em>Shaffer, </em><span class="citation" data-id="469158"><a href="/opinion/469158/united-states-v-william-shaffer/#689" aria-description="Citation for case: United States v. William Shaffer">789 F.2d at 689</a></span>, we stated that undisclosed evidence that an informant had previously participated in a heroin investigation was important impeachment evidence that could have been used to discredit the informant’s trial testimony that he had not previously participated in that type of investigation. The circumstances in <em>Bern </em>are identical.</p>
<p id="b1054-8">(5) <em>Prejudice Resulting from the Suppression of the Impeachment Evidence, Considered Collectively</em></p>
<p id="b1054-9">In determining whether the suppression of impeachment evidence is sufficiently prejudicial to rise to the level of a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation, we analyze the totality of the undisclosed evidence “in the context of the entire record.” <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#112" aria-description="Citation for case: United States v. Agurs">427 U.S. at 112</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>; <em>see also Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#682" aria-description="Citation for case: United States v. Bagley">473 U.S. at 682</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span> (opinion of Blackmun, J.).<footnotemark>11</footnotemark></p>
<p id="b1055-4"><page-number citation-index="1" label="1059">*1059</page-number>Because the withheld impeachment evidence would not simply have been cumulative of the impeachment evidence introduced at trial, but would have created substantial doubt as to Patrick’s credibility, it is important to analyze the significance of Patrick’s testimony to the prosecution’s ease. Patrick’s testimony was critical because it directly contradicted Benn’s evidence that he acted in self-defense and that he did not premeditate the killings. Moreover, it provided the only direct evidence of the aggravating factor of common scheme or plan. Patrick was the only witness to testify to the state’s primary theory that Benn killed Dethlefsen and Nelson for threatening to reveal an arson-insurance-fraud scheme. He was also the only witness to suggest that Benn wanted to kill Dethlefsen because Dethlef-sen changed his will so as to remove Benn as a beneficiary. Without those theories (and it is difficult to believe that the jury would have accepted the will theory), the only motive the prosecution suggested was that Benn was upset because he thought that Dethlefsen was harassing his ex-girlfriend — a motive that supported the defense’s theory (that Benn became upset when he saw a note with his ex-girlfriend’s phone number on it in Dethlefsen’s house and a spontaneous argument ensued) as much as the prosecution’s.</p>
<p id="b1055-5">Moreover, Patrick’s testimony that Benn attempted to hire someone to kill Hartman while in prison undercut Benn’s defense, because the jury was more likely to believe that Benn was guilty of premeditating the murders of Dethlefsen and Nelson after being told that he plotted to kill Hartman from prison.</p>
<p id="b1055-8">The state’s failure to disclose to the defense that Patrick was a potential witness prior to the day before trial exacerbated the harm that resulted from its failure to provide impeachment information about him, because the defense did not have sufficient time to investigate Patrick and prepare for cross-examination.</p>
<p id="b1055-9">The dissenting justices in the Washington Supreme Court’s state habeas case stated that the withheld information concerning Patrick was so significant that a new trial was required. <em>See In re Benn, </em><span class="citation" data-id="4711467"><a href="/opinion/4907353/in-re-the-personal-restraint-of-benn/#155" aria-description="Citation for case: In re the Personal Restraint of Benn">952 P.2d at 155-56</a></span>. The district court agreed with the Washington Supreme Court’s dissent that “[t]he significance of Patrick’s testimony cannot be over-stated.” <em>Benn v. Wood, </em><span class="citation no-link">2000 WL 1031361</span>, at *5 (W.D.Wash.2000). Both statements are correct.</p>
<p id="b1055-10">Analyzed collectively, the withheld impeachment evidence reveals that Patrick, a critical witness for the state, was “completely unreliable, a liar for hire, [and] ready to perjure himself for whatever advantage he could squeeze out of the system.” <em><span class="citation no-link">Id.</span> </em>We hold that the suppression of the impeachment evidence undermines confidence in the outcome of Benn’s trial and was therefore prejudicial. We further hold that the Washington Supreme Court’s decision to the contrary was clearly erroneous and constitutes an unreasonable application of clearly established Supreme Court law.</p>
<p id="b1056-3"><page-number citation-index="1" label="1060">*1060</page-number>C. The Prosecution’s Failure to Disclose Exculpatory Evidence that the Fire at Benn’s Trailer was Accidental and not the Result of Arson is Sufficient, Standing Alone, to constitute a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation.</p>
<p id="b1056-4">The prosecution failed to disclose that Deputy Fire Marshal Ted Thompson and Electrical Inspector Walter Erickson both conclusively determined that the fire in Benn’s trailer was accidental. The state did disclose its March 30, 1988 report stating on the basis of these experts’ investigation that there was “no fault or failure” of the lead electrical wire and no evidence of tampering with the fuse panel. The report did not state that the deputy fire marshal and electrical inspector had concluded that arson was <em>not </em>the cause of the trailer fire; that the furnace was the same type that Erickson had in his own home; or that there had been a manufacturer’s recall of this type of furnace because it tended to cause fires. Rather, the report suggested that Coleman furnaces did not cause fires.</p>
<p id="b1056-5">The experts’ conclusion that the fire was accidental, and the reasons therefor, was material evidence that could have served to rebut the arson-insurance-fraud theory that the prosecution offered to prove mo-five, premeditation, and the aggravating circumstance of common scheme or plan. We reject the Washington Supreme Court’s conclusion that the cause of the fire was not critical to the prosecution’s insurance fraud theory because, as the state trial court stated, the arson-insurance-fraud theory evidence was “the kind of evidence that the State must and needs to prove if it’s going to prove the aggravating factor that is involved in this case.... Without it, the State doesn’t have a case for aggravated murder. ...” The district court reiterated this point when it stated that evidence of the accidental nature of the fire, if presented to the jury, would have “gravely undercut[ ] the fear of police exposure” that the prosecution asserted led Benn to kill Dethlefsen and Nelson. <em>Benn v. Wood, </em><span class="citation no-link">2001 WL 1031361</span>, at 3113 *3 (W.D.Wash.2000).<footnotemark>12</footnotemark> The prosecutor also stressed the importance of the arson-fraud-insurance theory to the jury. In his closing argument, he stated: “And aggravating circumstances exist ... the common scheme or plan, the single act .... [H]e indeed wanted both men dead. He told the persons he confided in about the fact that Mike was threatening over the fire insurance money as well as Jack.”<footnotemark>13</footnotemark></p>
<p id="b1056-9">The state argues that its failure to disclose this exculpatory information did <page-number citation-index="1" label="1061">*1061</page-number>not constitute a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation because Benn was aware of the February 12, 1988 report in which the deputy fire marshal tentatively concluded that the fire was accidental. The February report’s tentative conclusion, however, was displaced by the conclusions in the later March 30, 1988 report. The March report suggested that, after further investigation, the experts had reached a different conclusion. Specifically, the report stated that A1 Pearson, a furnace technician, said that “he could find and think of no situation in which a furnace [such as a Coleman] had caused a fire in a mobile home.”</p>
<p id="b1057-5">The state, relying on <em>United States v. Marashi, </em><span class="citation" data-id="547559"><a href="/opinion/547559/united-states-v-s-mohammad-marashi/" aria-description="Citation for case: United States v. S. Mohammad Marashi">913 F.2d 724</a></span> (9th Cir.1990), and <em>United States v. Aichele, </em><span class="citation" data-id="9481951"><a href="/opinion/566407/united-states-v-richard-aichele/#764" aria-description="Citation for case: United States v. Richard Aichele">941 F.2d 761, 764</a></span> (9th Cir.1991), asserts that there was no <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation because Benn could have discovered the experts’ conclusions by interviewing them. <em><span class="citation" data-id="547559"><a href="/opinion/547559/united-states-v-s-mohammad-marashi/" aria-description="Citation for case: United States v. S. Mohammad Marashi">Marashi</a></span> </em>does not support the state’s position. There, we simply held that the prosecution’s failure to disclose an IRS agent’s notes revealing the identity of a private detective was not prejudicial to the defense because the defendant’s own conduct showed that the evidence was not material. We relied in part on the fact that the defendant had access to and chose not to interview the individual who hired the private detective as support for that holding. <em>Marashi, </em><span class="citation" data-id="547559"><a href="/opinion/547559/united-states-v-s-mohammad-marashi/#733" aria-description="Citation for case: United States v. S. Mohammad Marashi">913 F.2d at 733-34</a></span>. Here, contrary to <em><span class="citation" data-id="547559"><a href="/opinion/547559/united-states-v-s-mohammad-marashi/" aria-description="Citation for case: United States v. S. Mohammad Marashi">Marashi</a></span>, </em>there is no doubt of the materiality of the suppressed evidence.</p>
<p id="b1057-6"><em><span class="citation" data-id="9481951"><a href="/opinion/566407/united-states-v-richard-aichele/" aria-description="Citation for case: United States v. Richard Aichele">Aichele</a></span> </em>involved the obligation of a United States Attorney to turn over California State Department of Corrections files that were under the exclusive control of California officials. We held that because the United States Attorney had no control over the state’s files there was no <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation. <em>See also United States v. Santiago, </em><span class="citation" data-id="687686"><a href="/opinion/687686/united-states-v-richard-santiago-aka-chuco/#894" aria-description="Citation for case: United States v. Richard Santiago, A/K/A &quot;Chuco&quot;">46 F.3d 885, 894</a></span> (9th Cir.1995) (holding that the federal government did have an obligation to turn over information in the possession of the Bureau of Prisons and limiting the principle in <em><span class="citation" data-id="9481951"><a href="/opinion/566407/united-states-v-richard-aichele/" aria-description="Citation for case: United States v. Richard Aichele">Aichele</a></span> </em>to federal prosecutions in which material is held exclusively by a <em>state </em>agency). The <em><span class="citation" data-id="9481951"><a href="/opinion/566407/united-states-v-richard-aichele/" aria-description="Citation for case: United States v. Richard Aichele">Aichele</a></span> </em>court then added, by way of dictum, that if a defendant can ascertain the material on his own, there is no suppression. Certainly, that observation is over-broad, at the very least. We need not consider, however, whether the dictum in <em><span class="citation" data-id="9481951"><a href="/opinion/566407/united-states-v-richard-aichele/" aria-description="Citation for case: United States v. Richard Aichele">Aichele</a></span> </em>accurately states the law, particularly after <em>Kyles v. Whitley, </em><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">514 U.S. 419</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">115 S.Ct. 1555</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">131 L.Ed.2d 490</a></span> (1995), or what the limitations on that dictum might be. For whatever its merit, and we express no view, the <em><span class="citation" data-id="9481951"><a href="/opinion/566407/united-states-v-richard-aichele/" aria-description="Citation for case: United States v. Richard Aichele">Aichele</a></span> </em>dictum would not apply in circumstances such as those present here.</p>
<p id="b1057-8">In <em>Paradis v. Arave, </em><span class="citation" data-id="748634"><a href="/opinion/748634/donald-m-paradis-petitioner-appellant-v-aj-arave-warden-idaho-state/" aria-description="Citation for case: Donald M. PARADIS, Petitioner-Appellant, v. A.J. ARAVE,...">130 F.3d 385</a></span> (9th Cir.1997), a <em>post-Aichele </em>case, our <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>analysis was not affected by the defendant’s knowledge of and ability to interview the prosecution’s expert and obtain the undisclosed material. There, the medical expert testified at trial that the victim was killed in a creek where her body was found. That testimony contradicted the defense theory that the victim was killed by others at Paradis’ house when Paradis was not home and that Paradis then just helped dump the body in the creek. After the trial, defense counsel discovered that the prosecutor had written notes of the briefing conducted by the medical expert shortly after he performed the autopsy. The written notes showed that at that time the medical expert had expressed the opinion that the victim did <em>not </em>die in the creek. The prosecution did not disclose this fact. We held that the undisclosed material constituted impeachment evidence, although the defendant obviously knew of the expert’s existence and could have obtained the suppressed information from him. <em>Paradis, </em><span class="citation" data-id="748634"><a href="/opinion/748634/donald-m-paradis-petitioner-appellant-v-aj-arave-warden-idaho-state/#392" aria-description="Citation for case: Donald M. PARADIS, Petitioner-Appellant, v. A.J. ARAVE,...">130 F.3d at 392</a></span>.</p>
<p id="b1058-3"><page-number citation-index="1" label="1062">*1062</page-number>The facts in <em>Benn </em>are similar. Benn, like Paradis, knew of the experts’ existence but had been supplied with evidence by the state that the experts’ view supported the state’s theory. A defendant furnished with such inculpatory evidence by the state is not required to assume that the state has concealed material information and has thereby obligated him to ascertain the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>material on his own. In the case before us, moreover, the state not only failed to disclose the crucial information about the accidental nature of the fire, but it actually misled the defense by disclosing a part of the experts’ findings that, read alone, would lead to a conclusion directly opposite to the one they reached.</p>
<p id="b1058-4">Evidence that the fire in Benn’s trailer was <em>not </em>caused by arson and had been determined by fire officials to be accidental would have substantially undermined the state’s principal theory of motive and its main support for the aggravating factor of common scheme or plan, as well as its contention that the killings were premeditated. Thus, we hold that the state’s failure to disclose exculpatory evidence about the nature of the fire constitutes a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation, independent of the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation that resulted from the state’s suppression of impeachment evidence. We also hold that the state court ruling regarding the exculpatory evidence was clearly erroneous and thus constituted an “unreasonable application” of clearly established Supreme Court precedent.</p>
<p id="b1058-5">y. CONCLUSION</p>
<p id="b1058-6">In <em>Bemalr-Obeso, </em>we stated that “we expect prosecutors and investigators to take all reasonable measures to safeguard the system against treachery. This responsibility includes the duty as required by <em><span class="citation" data-id="108471"><a href="/opinion/108471/giglio-v-united-states/" aria-description="Citation for case: Giglio v. United States">Giglio</a></span> </em>to turn over to the defense in discovery all material information casting a shadow on a government witness’s credibility.” <span class="citation" data-id="602901"><a href="/opinion/602901/united-states-v-filemon-bernal-obeso/#334" aria-description="Citation for case: United States v. Filemon Bernal-Obeso">989 F.2d at 334</a></span>. Here, the state failed to take <em>any </em>measures to safeguard the system against treachery. To the contrary, the state suppressed material exculpatory and impeachment evidence that would have destroyed the credibility of its principal witness, severely undermined its theory of motive, and left it without substantial evidence of premeditation or an aggravating circumstance.</p>
<p id="b1058-8">Because the suppressed impeachment evidence and the suppressed exculpatory evidence are each, standing alone, sufficiently prejudicial to merit relief under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>, </em>they <em>a fortiori </em>are sufficiently prejudicial when analyzed together. Given the importance of both Patrick’s testimony and the arson-insurance-fraud theory to the prosecution’s case, as well as the sheer volume and damaging nature of the improperly withheld evidence, we conclude that the Washington Supreme Court’s determination that there was no <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation was clearly erroneous and constitutes an unreasonable application of Supreme Court precedent. To say that we have a firm conviction that the state court erred in its application of <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>and its progeny would be a gross understatement indeed. Because our holding of a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation necessarily comprehends a hplding that the <em>Brecht </em>prejudice standard is met, we hold that Benn is entitled to habeas relief. We affirm the district court’s decision granting Benn’s petition for a writ of habe-as corpus.</p>
<p id="b1058-9">AFFIRMED.</p>
<footnote label="1">
<p id="b1043-7">. As part of its factual findings following the post-conviction evidentiary hearing, the Pierce County Superior Court found that Stevens was not a credible witness.</p>
<p id="b1043-8">Sherrie Woodard was one of the individuals who was with Patrick when his hotel room was searched. She testified at the state court evidentiary hearing that Patrick told her that he planted drugs in places in order to make busts when he was working as an informant and that Detective Padukiewicz, Patrick's supervisor, knew about it. She also said that Patrick would keep some of the drugs from the busts and that the detectives knew about this as well. When Woodard went to Patrick’s hotel room during the Benn trial, she saw a large amount of money that Patrick said the police had given to him. Patrick also suggested to her that he was willing to lie to get out of trouble. She said Patrick’s reputation for truthfulness was not veiy good.</p>
<p id="b1043-13">Upon learning about the hotel room search during the trial, the defense moved for a continuance to have the opportunity to question Woodard and others involved in the hotel room search; however, the judge denied the motion.</p>
</footnote>
<footnote label="2">
<p id="b1043-14">. Benn directed his counsel at trial not to cross-examine Hartman "for fear that his family would be harmed.” Benn told his lawyer that he was convinced that Hartman was threatening his family even though his family said there were no such threats. The <page-number citation-index="1" label="1048">*1048</page-number>defense called no witnesses until rebuttal because of these fears. During the trial, Benn's competency was re-evaluated three different times with conflicting expert opinions about whether he was or was not competent. Each time, the trial court ultimately deemed him competent and allowed the proceedings to continue. Benn learned during the post-conviction proceedings that he could have impeached Hartman with the witness’s admitted intoxication and hearing difficulties at the time he spoke with Benn.</p>
</footnote>
<footnote label="3">
<p id="b1044-12">. Walter "Pete” Hartman and Denver Carter were also surprise witnesses who were not on the original witness lists. Both of these witnesses were "discovered” by the prosecution during the trial, well after opening statements had been delivered, and after the defense theory had been presented to the jury.</p>
</footnote>
<footnote label="4">
<p id="b1047-6">. In arguing that the district court should be reversed, the state asserts that the district court failed to state explicitly in its opinion how the state court decision was contrary to federal law and that this failure shows that the district court did not apply the AEDPA standard. The state is wrong for two reasons. First, the district court carefully described the AEDPA standard in a full paragraph at the beginning of its opinion and stated that Benn was not entitled to relief unless that standard was satisfied. <em>Benn v. Wood, </em>No. C98-5131RDB, <span class="citation no-link">2000 WL 1031361</span>, at *2 (W.D.Wash. June 30, 2000). After expressing his reluctance to overturn a Washington Supreme Court decision, Judge Burgess granted Benn habeas relief because the prosecution withheld material evidence in violation of <em>Brady v. Maryland, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83, 87</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">10 L.Ed.2d 215</a></span> (1963), and because the importance and sheer amount of withheld evidence <em>"seriously " </em>undermined confidence in the verdict. <em>Benn, </em><span class="citation no-link">2000 WL 1031361</span>, at *2. Thus, it appears that the district court did apply the AEDPA standard. Second, our review of the district court’s decision is <em>de novo. Miles v. Prunty, </em><span class="citation" data-id="765715"><a href="/opinion/765715/willie-lee-miles-v-kw-prunty-warden-attorney-general-of-the-state-of/#1105" aria-description="Citation for case: Willie Lee Miles v. K.W. Prunty, Warden Attorney General...">187 F.3d 1104, 1105</a></span> (9th Cir.1999). Thus, any error in applying the AEDPA standard would be of no consequence on this appeal.</p>
</footnote>
<footnote label="5">
<p id="b1047-12">. The addition, deletion, or alteration of a factor in a test established by the Supreme Court also constitutes a failure to apply controlling Supreme Court law under the "contrary to” clause of AEDPA. <em>See Williams v. Taylor, </em><span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/#405" aria-description="Citation for case: Williams v. Taylor">529 U.S. 362, 405-06</a></span>, <span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/" aria-description="Citation for case: Williams v. Taylor">120 S.Ct. 1495</a></span>, <page-number citation-index="1" label="1052">*1052</page-number><span class="citation" data-id="9434817"><a href="/opinion/145122/williams-v-taylor/" aria-description="Citation for case: Williams v. Taylor">146 L.Ed.2d 389</a></span> (2000); <em>Brown v. Mayle, </em><span class="citation" data-id="7009786"><a href="/opinion/7103945/brown-v-mayle/#1039" aria-description="Citation for case: Brown v. Mayle">283 F.3d 1019, at 1039</a></span> (9th Cir.2002).</p>
</footnote>
<footnote label="6">
<p id="b1048-6">.In both "contrary to” and "unreasonable application” cases, the erroneous state court ruling must also satisfy <em>Brecht v. Abrahamson, </em><span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/#637" aria-description="Citation for case: Brecht v. Abrahamson">507 U.S. 619, 637</a></span>, <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/" aria-description="Citation for case: Brecht v. Abrahamson">113 S.Ct. 1710</a></span>, <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/" aria-description="Citation for case: Brecht v. Abrahamson">123 L.Ed.2d 353</a></span> (1993) (requiring that the error have had a substantial or injurious effect on the verdict). <em>See Packer, </em><span class="citation" data-id="7008694"><a href="/opinion/7102904/packer-v-hill/#1102" aria-description="Citation for case: Packer v. Hill">277 F.3d 1092 at 1102</a></span>. Where, as here, however, the alleged error is a <em>Brady </em>violation, the petitioner need show only that the state court’s <em>Brady </em>ruling was erroneous under AEDPA, because a <em>Brady </em>error <em>a fortiori </em>satisfies <em>Brecht. See Kyles v. Whitley, </em><span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/#436" aria-description="Citation for case: Kyles v. Whitley">514 U.S. 419, 436</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">115 S.Ct. 1555</a></span>, <span class="citation" data-id="9433120"><a href="/opinion/117923/kyles-v-whitley/" aria-description="Citation for case: Kyles v. Whitley">131 L.Ed.2d 490</a></span> (1995) ("[0]nce there has been <em>Bagley </em>error ... it cannot subsequently be found harmless under <em>Brecht.’’)', Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#678" aria-description="Citation for case: United States v. Bagley">473 U.S. at 678</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span> (holding that, in order to establish a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>violation, a petitioner must show prejudice).</p>
</footnote>
<footnote label="7">
<p id="b1048-12">. We look to the Washington Supreme Court’s state habeas decision because, when conducting an AEDPA analysis, we examine the state court’s last reasoned decision. <em>See Shackleford v. Hubbard, </em><span class="citation" data-id="771419"><a href="/opinion/771419/william-lee-shackleford-v-susan-hubbard-warden/" aria-description="Citation for case: William Lee Shackleford v. Susan Hubbard, Warden">234 F.3d 1072</a></span>, 1079 n. 2 (9th Cir.2000).</p>
</footnote>
<footnote label="8">
<p id="b1048-13">. The state court cited to and appears to have applied (albeit clearly erroneously) <em>United States v. Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#676" aria-description="Citation for case: United States v. Bagley">473 U.S. 667, 676</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">87 L.Ed.2d 481</a></span> (1985), and <em>United States v. Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#110" aria-description="Citation for case: United States v. Agurs">427 U.S. 97, 110</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">49 L.Ed.2d 342</a></span> (1976), in addition to <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span>.</em></p>
</footnote>
<footnote label="9">
<p id="b1049-7">. The Supreme Court refers to the requirement that the defense establish that the suppressed evidence was prejudicial to the outcome as a "materiality” requirement and/or a “prejudice” requirement. <em>See Brady, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U.S. at 87</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span> (requiring that the suppressed evidence be "material” to guilt or punishment); <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#88" aria-description="Citation for case: Brady v. Maryland"><em>id. </em>at 88</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span> (referring to the state’s suppression of a confession as "prejudicial” to the defendant). The terms "material” and "prejudicial” are used interchangeably in <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>cases. Evidence is not "material” unless it is “prejudicial,” and not "prejudicial” unless it is “material.” Thus, for <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>purposes, the two terms have come to have the same meaning.</p>
</footnote>
<footnote label="10">
<p id="b1049-8">. Justice Blackmun's comparison of the prejudice inquiry under <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>to that under <em>Strickland v. Washington, </em><span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">466 U.S. 668</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S.Ct. 2052</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">80 L.Ed.2d 674</a></span> (1984), was joined by Justice O'Connor. Justices Brennan and Marshall dissented arguing for an even stricter standard of materiality that would have required reversal in all cases in which the prosecution suppressed exculpatory or impeachment evidence unless it was clear beyond a reasonable doubt that the withheld evidence would not have affected the outcome. <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#704" aria-description="Citation for case: Strickland v. Washington"><em>See id. </em>at 704</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S.Ct. 2052</a></span> (Marshall, J., dissenting). Justice Stevens would have applied different standards of materiality depending on whether the defendant made a request for <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>information or not. <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#711" aria-description="Citation for case: Strickland v. Washington"><em>See id. </em>at 711</a></span>, <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/" aria-description="Citation for case: Strickland v. Washington">104 S.Ct. 2052</a></span> (Stevens, J., dissenting). In a case such as Benn’s, in which the defense did make a <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>request, Justice Stevens would have applied a stricter materiality standard as well. <em>See <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">id.</a></span></em></p>
</footnote>
<footnote label="11">
<p id="b1054-6">. While the good faith or bad faith of the state is irrelevant when material impeachment evidence has been withheld from the defense, <em>see Brady, </em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U.S. at 87</a></span>, <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">83 S.Ct. 1194</a></span>, the Supreme Court applies a stricter standard of materiality — a standard of materiality that is more favorable to the defendant— when the prosecutor has knowingly relied on or condoned the use of perjured testimony, <em>see Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#680" aria-description="Citation for case: United States v. Bagley">473 U.S. at 680</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span> ("[T]he fact that testimony is perjured is considered material unless failure to disclose it would be harmless beyond a reasonable doubt.”); <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#103" aria-description="Citation for case: United States v. Agurs">427 U.S. at 103</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span> (holding that, under this "stricter” standard of materiality, a conviction "must be set aside if there is any reasonable likelihood that the false testimony could have affected the judgment of the jury”); <em>see also United States v. Endicott, </em><span class="citation" data-id="519281"><a href="/opinion/519281/united-states-v-rex-g-endicott/#455" aria-description="Citation for case: United States v. Rex G. Endicott">869 F.2d 452, 455</a></span> (9th Cir.1989) ("[I]f the prosecution knowingly uses perjured testimony, or if the prosecution knowingly fails to disclose that testimony used to convict a defendant was false, the conviction must be set aside if there is any reasonable likelihood that the false testimony could have affected the jury verdict."). The Court explained that a stricter standard of materiality is necessary in these cases because they involve "prosecu-torial misconduct and, more importantly .... 'a corruption of the truth-seeking function of the trial process.' ” <em>Bagley, </em><span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/#680" aria-description="Citation for case: United States v. Bagley">473 U.S. at 680</a></span>, <span class="citation" data-id="9430189"><a href="/opinion/111514/united-states-v-bagley/" aria-description="Citation for case: United States v. Bagley">105 S.Ct. 3375</a></span> (quoting <em>Agurs, </em><span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/#104" aria-description="Citation for case: United States v. Agurs">427 U.S. at 104</a></span>, <span class="citation" data-id="9426498"><a href="/opinion/109506/united-states-v-agurs/" aria-description="Citation for case: United States v. Agurs">96 S.Ct. 2392</a></span>); <em>see also Bernal—Obeso, </em><span class="citation" data-id="602901"><a href="/opinion/602901/united-states-v-filemon-bernal-obeso/#337" aria-description="Citation for case: United States v. Filemon Bernal-Obeso">989 F.2d at 337</a></span>.</p>
<p id="b1054-11">Here, there is evidence that the state lied to defense counsel when it "falsely claim[ed]” that Patrick was in a witness protection program. There is also evidence that the state knowingly allowed Patrick to commit perjury when it stood by and said nothing while Patrick perjured himself by stating that he did not use drugs while acting as an informant. Similarly, the prosecution said nothing when Patrick lied at trial about never having previously served as an informant in a murder case. There is also evidence of other prose-cutorial misconduct that corrupted the truth-seeking function of the trial. For example, the prosecution blatantly violated state discovery rules by failing to disclose Patrick's identity to the defense until the day before <page-number citation-index="1" label="1059">*1059</page-number>trial, even though the prosecution had recorded his statement over a year earlier; the prosecution did not even attempt to obtain information about Patrick’s informant history despite a court order to do so; and the detective who prepared the March 30, 1988 report "selectively omit[ted]” information that the fire was accidental. <em>See </em>discussion <em>supra </em>Section I.B.2. Consequently, a stricter standard of materiality applies to the <em><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">Brady</a></span> </em>analysis. It is, however, unnecessary to apply that standard in this case because the prejudice resulting from the suppression of the impeachment evidence here was so great that it would satisfy any rational standard of materiality.</p>
</footnote>
<footnote label="12">
<p id="b1056-6">. The state points out that Benn did tell his brother, Monte, that he was nervous about fire insurance fraud charges being filed against him because he claimed a greater financial loss than he incurred. However, as the district court observed, a threat to tell the police that a person claimed more than he should have after a fire is materially different from a threat to tell the police that the person conspired to commit an arson, played a role in starting the fire, and then claimed an excessive loss following the fire. <em>See Benn v. Wood, </em><span class="citation no-link">2001 WL 1031361</span>, at *3 (W.D.Wash.2000).</p>
</footnote>
<footnote label="13">
<p id="b1056-7">. At oral argument, the state contended that the mere fact that Benn shot both Dethlefsen and Nelson was sufficient to show a common scheme or plan and that the arson-insurance-fraud theory was, therefore, unnecessary. In order to prove a "common scheme or plan” under Washington state law, however, "there must be a nexus between the killings” that goes beyond the mere firing of the fatal shots. <em>Washington v. Finch, </em><span class="citation" data-id="4711688"><a href="/opinion/4907479/state-v-finch/" aria-description="Citation for case: State v. Finch">137 Wash.2d 792</a></span>, <span class="citation multiple-matches"><a href="/c/P.2d/975/967/">975 P.2d 967</a></span>, 994 (1999). Specifically, "[t]he term [common plan or scheme] refers to a larger criminal design, of which the charged crime is only part. To prove the existence of this aggravator the killings must be connected by a larger criminal plan. Thus, the 'nexus’ exists when an overarching criminal plan connects both murders.” <em>Id. </em>The arson-insurance-fraud scheme was what the state relied on to prove "an overarching criminal plan."</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Bennis v. Michigan.md  (`case`, 5 assertions)

### content_page

```
---
title: Bennis v. Michigan
type: case
citation: "516 U.S. 442 (1996)"
parallel_cite: "116 S. Ct. 994; 134 L. Ed. 2d 68"
neutral_cite: 1996 U.S. LEXIS 1565
court: U.S.
court_level: scotus
circuit: ""
year: 1996
date_decided: 1996-03-04
docket: 94-8729
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
  opinion_url: "https://www.courtlistener.com/opinion/118005/bennis-v-michigan/"
  cluster_id: 118005
  opinion_id: null
  identity_checked: true
lake:
  record_id: Bennis v. Michigan
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Key
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[United States v. James Daniel Good Real Property]]"
  - "[[Calero-Toledo v. Pearson Yacht Leasing Co.]]"
  - "[[Timbs v. Indiana]]"
  - "[[Culley v. Marshall]]"
tags:
  - case
  - civil-asset-forfeiture
  - innocent-owner
  - due-process
  - takings
holding: "The Due Process Clause and the Takings Clause do not require an innocent-owner defense to the forfeiture, as a public nuisance, of a jointly owned automobile used by one co-owner to commit a crime, even as against a co-owner who did not know of or consent to the misuse."
---

# Bennis v. Michigan

*516 U.S. 442 (1996)* (No. 94-8729) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 118005 → lead opinion 118005; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Tina Bennis co-owned a car with her husband, John Bennis. Detroit police caught John using the car for a sex act with a prostitute, and Michigan brought a proceeding to abate the vehicle as a public nuisance. The state courts ordered the car forfeited, extinguishing Tina's ownership interest even though she neither knew nor agreed that her husband would use the car that way. Tina argued that forfeiting her interest without regard to her innocence deprived her of property without due process and effected an uncompensated taking.

## Issue
Whether forfeiting the interest of an owner who did not know of, or consent to, another's criminal use of jointly owned property violates the Due Process Clause of the Fourteenth Amendment or the Takings Clause of the Fifth Amendment.

## Rule
Notice and an opportunity to be heard were provided; Tina's real claim was that her lack of knowledge should immunize her interest. The Court rejected that: "a long and unbroken line of cases holds that an owner's interest in property may be forfeited by reason of the use to which the property is put even though the owner did not know that it was to be put to such use." — 516 U.S. at 446. ^pin-446

Tracing the principle from *The Palmyra* (1827) through *Van Oster* and *Goldsmith-Grant*, the Court held it defeats a constitutional innocent-owner claim; and because property forfeited under the State's lawful process is not "taken" for public use, the Takings Clause was not implicated.

## Application
The abatement served forfeiture's deterrent and preventive purposes — discouraging owners from entrusting property to those who might misuse it and removing instruments of vice from circulation. Precedent squarely foreclosed a constitutional innocent-owner defense, so the extinguishment of Tina Bennis's interest, after notice and a hearing, offended neither due process nor the Takings Clause. Whether to create an innocent-owner exception was a matter of legislative grace, not constitutional command.

## Conclusion
The judgment of the Supreme Court of Michigan was **affirmed**. Rehnquist, C.J., delivered the opinion of the Court, joined by O'Connor, Scalia, Ginsburg, and Thomas, JJ.; Thomas, J., and Ginsburg, J., filed concurring opinions; Stevens, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], joined by Souter and Breyer, JJ.; Kennedy, J., filed a separate [[Common Legal Terms#dissenting-opinion|dissenting opinion]].

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Bennis* remains the controlling answer to the recurring officer question whether a jointly owned or leased vehicle can be forfeited despite a co-owner's innocence: the Constitution supplies no innocent-owner defense (statutes may). Its holding subsumes the innocent-lessor language of the earlier *Calero-Toledo v. Pearson Yacht Leasing Co.* (1974), which anticipated this rule in the context of a leased vessel; *Bennis* states it as a general square holding.

## Appears on
- [[Civil Asset Forfeiture]] — *Key*

## Sources
- [*Bennis v. Michigan*, 516 U.S. 442 (1996)](https://www.courtlistener.com/opinion/118005/bennis-v-michigan/) — pinpoint: 446 (Opinion of the Court, holding; Rehnquist, C.J.); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fc117c5898a29390", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "516 U.S. 442 (1996)", "court": "U.S.", "neutral_cite": "1996 U.S. LEXIS 1565", "official_citation_present": true, "parallel_cite": "116 S. Ct. 994; 134 L. Ed. 2d 68", "title": "Bennis v. Michigan", "year": "1996"}}
{"assertion_id": "a1af5e16d78388cc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Due Process Clause and the Takings Clause do not require an innocent-owner defense to the forfeiture, as a public nuisance, of a jointly owned automobile used by one co-owner to commit a crime, even as against a co-owner who did not know of or consent to the misuse.", "title": "Bennis v. Michigan"}}
{"assertion_id": "c365e9c5fa85027a", "dimension": "support", "kind": "home_role", "locator": {"home": "Civil Asset Forfeiture"}, "payload": {"home": "Civil Asset Forfeiture", "role": "Key", "title": "Bennis v. Michigan"}}
{"assertion_id": "2a156c21439cbde3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Bennis v. Michigan"}}
{"assertion_id": "3f17a3a2338a8d80", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Bennis v. Michigan", "varies_by_point": "false"}}
```

### lake record — Bennis v. Michigan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Bennis v. Michigan",
  "status": "under_review",
  "identity": {
    "case_name": "Bennis v. Michigan",
    "case_name_short": "Bennis",
    "case_name_full": "Bennis v. Michigan",
    "input_case_name": "Bennis v. Michigan",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1996-03-04",
    "year": 1996,
    "docket": "94-8729",
    "cluster_id": 118005,
    "lead_opinion_id": 9433258,
    "sibling_ids": [],
    "absolute_url": "/opinion/118005/bennis-v-michigan/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "516 U.S. 442",
      "volume": "516",
      "reporter": "U.S.",
      "page": "442",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 994",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 68",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "68",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1996 U.S. LEXIS 1565",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "1565",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "516 U.S. 442",
        "volume": "516",
        "reporter": "U.S.",
        "page": "442",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 994",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "994",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "134 L. Ed. 2d 68",
        "volume": "134",
        "reporter": "L. Ed. 2d",
        "page": "68",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1996 U.S. LEXIS 1565",
        "volume": "1996",
        "reporter": "U.S. LEXIS",
        "page": "1565",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "516 U.S. 442",
    "official_selection": {
      "court_class": "scotus",
      "selected": "516 U.S. 442",
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
    "date_created": "2026-07-07T13:24:15Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T13:24:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "bennis-v-michigan--118005",
      "to_record_id": "Bennis v. Michigan",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Bennis v. Michigan

```
<opinion type="majority">
<author id="b623-8">Chief Justice Rehnquist</author>
<p id="AZr">delivered the opinion of the Court.</p>
<p id="b623-9">Petitioner was a joint owner, with her husband, of an automobile in which her husband engaged in sexual activity with a prostitute. A Michigan court ordered the automobile forfeited as a public nuisance, with no offset for her interest, notwithstanding her lack of knowledge of her husband’s activity. We hold that the Michigan court order did not offend the Due Process Clause of the Fourteenth Amendment or the Takings Clause of the Fifth Amendment.</p>
<p id="b623-10">Detroit police arrested John Bennis after observing him engaged in a sexual act with a prostitute in the automobile while it was parked on a Detroit city street. Bennis was convicted of gross indecency.<footnotemark>1</footnotemark> The State then sued both <page-number citation-index="1" label="444">*444</page-number>Bennis and his wife, petitioner Tina B. Bennis, to have the car declared a public nuisance and abated as such under §§600.3801<footnotemark>2</footnotemark> and 600.3825<footnotemark>3</footnotemark> of Michigan’s Compiled Laws.</p>
<p id="b624-5">Petitioner defended against the abatement of her interest in the car on the ground that, when she entrusted her husband to use the car, she did not know that he would use it to violate Michigan’s indecency law. The Wayne County Circuit Court rejected this argument, declared the car a public nuisance, and ordered the car’s abatement. In reaching this disposition, the trial court judge recognized the remedial discretion he had under Michigan’s case law. App. 21. He <page-number citation-index="1" label="445">*445</page-number>took into account the couple’s ownership of “another automobile,” so they would not be left “without transportation.” <em>Id., </em>at 25. He also mentioned his authority to order the payment of one-half of the sale proceeds, after the deduction of costs, to “the innocent co-title holder.” <em>Id., </em>at 21. He declined to order such a division of sale proceeds in this case because of the age and value of the car (an 11-year-old Pontiac sedan recently purchased by John and Tina Bennis for $600); he commented in this regard: “[T]here’s practically nothing left minus costs in a situation such as this.” <em>Id., </em>at 25.</p>
<p id="b625-5">- The Michigan Court of Appeals reversed, holding that regardless of the language of Michigan Compiled Law § 600.3815(2),<footnotemark>4</footnotemark> Michigan Supreme Court precedent interpreting this section prevented the State from abating petitioner’s interest absent proof that she knew to what end the car would be used. Alternatively, the intermediate appellate court ruled that the conduct in question did not qualify as a public nuisance because only one occurrence was shown and there was no evidence of payment for the sexual act. <span class="citation" data-id="9739730"><a href="/opinion/2220815/state-ex-rel-wayne-county-prosecuting-attorney-v-bennis/" aria-description="Citation for case: STATE Ex Rel WAYNE COUNTY PROSECUTING ATTORNEY v. BENNIS">200 Mich. App. 670</a></span>, <span class="citation" data-id="9739730"><a href="/opinion/2220815/state-ex-rel-wayne-county-prosecuting-attorney-v-bennis/" aria-description="Citation for case: STATE Ex Rel WAYNE COUNTY PROSECUTING ATTORNEY v. BENNIS">504 N. W. 2d 731</a></span> (1993).</p>
<p id="b625-6">The Michigan Supreme Court reversed the Court of Appeals and reinstated the abatement in its entirety. <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">447 Mich. 719</a></span>, <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">527 N. W. 2d 483</a></span> (1994). It concluded as a matter of state law that the episode in the Bennis vehicle was an abatable nuisance. Rejecting the Court of Appeals’ interpretation of § 600.3815(2), the court then announced that, in order to abate an owner’s interest in a vehicle, Michigan does not need to prove that the owner knew or agreed that her vehicle would be used in a manner proscribed by § 600.3801 when she entrusted it to another user. <em>Id., </em>at 737, <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#492" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">527 N. W. 2d, at 492</a></span>. The court next addressed petitioner’s <page-number citation-index="1" label="446">*446</page-number>federal constitutional challenges to the State’s abatement scheme: The court assumed that petitioner did not know of or consent to the misuse of the Bennis car, and concluded in light of our decisions in <em>Van Oster </em>v. <em>Kansas, </em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/" aria-description="Citation for case: Van Oster v. Kansas">272 U. S. 465</a></span> (1926), and <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), that Michigan’s failure to provide an innocent-owner defense was “without constitutional consequence.” <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#740" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">447 Mich., at 740-741</a></span>, <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#493" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">527 N. W. 2d, at 493-494</a></span>. The Michigan Supreme Court specifically noted that, in its view, an owner’s interest may not be abated when “a vehicle is used without the owner’s consent.” <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#742" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS"><em>Id., </em>at 742, n. 36</a></span>, <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#495" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">527 N. W. 2d, at 495, n. 36</a></span>. Furthermore, the court confirmed the trial court’s description of the nuisance abatement proceeding as an “equitable action,” and considered it “critical” that the trial judge so comprehended the statute. <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#742" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS"><em>Id., </em>at 742</a></span>, <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#495" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">527 N. W. 2d, at 495</a></span>.</p>
<p id="b626-5">We granted certiorari in order to determine whether Michigan’s abatement scheme has deprived petitioner of her interest in the forfeited car without due process, in violation of the Fourteenth Amendment, or has taken her interest for public use without compensation, in violation of the Fifth Amendment as incorporated by the Fourteenth Amendment. <span class="citation multiple-matches"><a href="/c/U.%20S./515/1121/">515 U. S. 1121</a></span> (1995). We affirm.</p>
<p id="b626-6">The gravamen of petitioner’s due process claim is not that she was denied notice or an opportunity to contest the abatement of her car; she was accorded both. Cf. <em>United States </em>v. <em>James Daniel Good Real Property, </em><span class="citation" data-id="9432907"><a href="/opinion/112914/united-states-v-james-daniel-good-real-property/" aria-description="Citation for case: United States v. James Daniel Good Real Property">510 U. S. 43</a></span> (1993). Rather, she claims she was entitled to contest the abatement by showing she did not know her husband would use it to violate Michigan’s indecency law. But a long and unbroken line of cases holds that an owner’s interest in property may be forfeited by reason of the use to which the property is put even though the owner did not know that it was to be put to such use.</p>
<p id="b626-7">Our earliest opinion to this effect is Justice Story’s opinion for the Court in <em>The Palmyra, </em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">12 Wheat. 1</a></span> (1827). The Pal<page-number citation-index="1" label="447">*447</page-number>myra, which had been commissioned as a privateer by the King of Spain and had attacked a United States vessel, was captured by a United States warship and brought into Charleston, South Carolina, for adjudication. <span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#8" aria-description="Citation for case: The Palmyra"><em>Id., </em>at 8</a></span>. On the Government’s appeal from the Circuit Court’s acquittal of the vessel, it was contended by the owner that the vessel could not be forfeited until he was convicted for the priva-teering. The Court rejected this contention, explaining: “The thing is here primarily considered as the offender, or rather the offence is attached primarily to the thing.” <span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/#14" aria-description="Citation for case: The Palmyra"><em>Id., </em>at 14</a></span>. In another admiralty forfeiture decision 17 years later, Justice Story wrote for the Court that in <em>in rem </em>admiralty proceedings “the acts of the master and crew . . . bind the interest of the owner of the ship, <em>whether he be innocent or guilty; </em>and he impliedly submits to whatever the law denounces as a forfeiture attached to the ship by reason of their unlawful or wanton wrongs.” <em>Harmony </em>v. <em>United States, </em><span class="citation" data-id="86274"><a href="/opinion/86274/united-states-v-brig-malek-adhel/#234" aria-description="Citation for case: United States v. Brig Malek Adhel">2 How. 210, 234</a></span> (1844) (emphasis added).</p>
<p id="b627-5">In <em>Dobbins’s Distillery </em>v. <em>United States, </em><span class="citation" data-id="89720"><a href="/opinion/89720/dobbinss-distillery-v-united-states/#401" aria-description="Citation for case: Dobbins&#x27;s Distillery v. United States">96 U. S. 395, 401</a></span> (1878), this Court upheld the forfeiture of property used by a lessee in fraudulently avoiding federal alcohol taxes, observing: “Cases often arise where the property of the owner is forfeited on account of the fraud, neglect, or misconduct of those intrusted with its possession, care, and custody, even when the owner is otherwise without fault . . . and it has always been held . . . that the acts of [the possessors] bind the interest of the owner . . . whether he be innocent or guilty.”</p>
<p id="b627-6">In <em>Van Oster </em>v. <em>Kansas, </em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/" aria-description="Citation for case: Van Oster v. Kansas">272 U. S. 465</a></span> (1926), this Court upheld the forfeiture of a purchaser’s interest in a car misused by the seller. Van Oster purchased an automobile from a dealer but agreed that the dealer might retain possession for use in its business. The dealer allowed an associate to use the automobile, and the associate used it for the illegal transportation of intoxicating liquor. <span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/#465" aria-description="Citation for case: Van Oster v. Kansas"><em>Id., </em>at 465-466</a></span>. The State brought a forfeiture action pursuant to a Kansas stat<page-number citation-index="1" label="448">*448</page-number>ute, and Van Oster defended on the ground that the transportation of the liquor in the car was without her knowledge or authority. This Court rejected Van Oster’s claim:</p>
<blockquote id="b628-5">“It is not unknown or indeed uncommon for the law to visit upon the owner of property the unpleasant consequences of the unauthorized action of one to whom he has entrusted it. Much of the jurisdiction in admiralty, so much of the statute and common law of liens as enables a mere bailee to subject the bailed property to a lien, the power of a vendor of chattels in possession to sell and convey good title to a stranger, are familiar examples____They suggest that certain uses of property may be regarded as so undesirable that the owner surrenders his control at his peril. . . .</blockquote>
<blockquote id="b628-8">“It has long been settled that statutory forfeitures of property entrusted by the innocent owner or lienor to another who uses it in violation of the revenue laws of the United States is not a violation of the due process clause of the Fifth Amendment.” <span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/#467" aria-description="Citation for case: Van Oster v. Kansas"><em>Id., </em>at 467-468</a></span>.</blockquote>
<p id="b628-9">The <em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/" aria-description="Citation for case: Van Oster v. Kansas">Van Oster</a></span> </em>Court relied on <em>J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S. 505</a></span> (1921), in which the Court upheld the forfeiture of a seller’s interest in a car misused by the purchaser. The automobile was forfeited after the purchaser transported bootleg distilled spirits in it, and the selling dealership lost the title retained as security for unpaid purchase money. <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#508" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>Id., </em>at 508-509</a></span>. The Court discussed the arguments for and against allowing the forfeiture of the interest of an owner who was “without guilt,” <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#510" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>id., </em>at 510</a></span>, and concluded that “whether the reason for [the challenged forfeiture scheme] be artificial or real, it is too firmly fixed in the punitive and remedial jurisprudence of the country to be now displaced,” <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#511" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States"><em>id., </em>at 511</a></span>.<footnotemark>5</footnotemark></p>
<p id="b629-4"><page-number citation-index="1" label="449">*449</page-number>In <em>Calero-Toledo </em>v. <em>Pearson Yacht Leasing Co., </em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S. 663</a></span> (1974), the most recent decision on point, the Court reviewed the same cases discussed above, and concluded that “the innocence of the owner of property subject to forfeiture has almost uniformly been rejected as a defense.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#683" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>Id., </em>at 683</a></span>.. Petitioner is in the same position as the various owners involved in the forfeiture cases beginning with <em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">The Palmyra</a></span> </em>in 1827. She did not know that her car would be used in an illegal activity that would subject it to forfeiture. But under these cases the Due Process Clause of the Fourteenth Amendment does not protect her interest against forfeiture by the government.</p>
<p id="b629-5">Petitioner relies on a passage from <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span>, </em>that “it would be difficult to reject the constitutional claim of... an owner who proved not only that he was uninvolved in and unaware of the wrongful activity, but also that he had done <page-number citation-index="1" label="450">*450</page-number>all that reasonably could be expected to prevent the proscribed use of his property.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#689" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 689</a></span>. But she concedes that this comment was <em>obiter dictum, </em>and “[i]t is to the holdings of our cases, rather than their dicta, that we must attend.” <em>Kokkonen </em>v. <em>Guardian Life Ins. Co. of America, </em><span class="citation" data-id="117845"><a href="/opinion/117845/kokkonen-v-guardian-life-insurance-co-of-america/#379" aria-description="Citation for case: Kokkonen v. Guardian Life Insurance Co. of America">511 U. S. 375, 379</a></span> (1994). And the <em>holding </em>of <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>on this point was that the interest of a yacht rental company in one of its leased yachts could be forfeited because of its use for transportation of controlled substances, even though the company was “ ‘in no way . . . involved in the criminal enterprise carried on by [the] lessee’ and ‘had no knowledge that its property was being used in connection with or in violation of [Puerto Rican Law].’” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#668" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 668</a></span>. Petitioner has made no showing beyond that here.</p>
<p id="b630-5">Justice Stevens’ dissent argues that our cases treat contraband differently from instrumentalities used to convey contraband, like cars: Objects in the former class are forfeit-able “however blameless or unknowing their owners may be,” <em>post, </em>at 459, but with respect to an instrumentality in the latter class, an owner’s innocence is no defense only to the “principal use being made of that property,” <em>post, </em>at 461. However, this Court’s precedent has never made the due process inquiry depend on whether the use for which the instrumentality was forfeited was the principal use. If it had, perhaps cases like <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span>, </em>in which Justice Douglas noted in dissent that there was no showing that the “yacht had been notoriously used in smuggling drugs ... and so far as we know only one marihuana cigarette was found on the yacht,” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#693" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">416 U. S., at 693</a></span> (opinion dissenting in part), might have been decided differently.</p>
<p id="b630-6">The dissent also suggests that <em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">The Palmyra</a></span> </em>line of cases “would justify the confiscation of an ocean liner just because one of its passengers sinned while on board.” <em>Post, </em>at 462. None of pur cases have held that an ocean liner may be confiscated because of the activities of one passenger. We said in <em>Goldsmith-Grant, </em>and we repeat here, that “[w]hen such <page-number citation-index="1" label="451">*451</page-number>application shall be made it will be time enough to pronounce upon it.” <span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#512" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 512</a></span>.</p>
<p id="b631-5">Notwithstanding this well-established authority rejecting the innocent-owner defense, petitioner argues that we should in effect overrule it by importing a culpability requirement from cases having at best a tangential relation to the “innocent owner” doctrine in forfeiture cases. She cites <em>Foucha </em>v. <em>Louisiana, </em><span class="citation" data-id="9432531"><a href="/opinion/112731/foucha-v-louisiana/" aria-description="Citation for case: Foucha v. Louisiana">504 U. S. 71</a></span> (1992), for the proposition that a criminal defendant may not be punished for a crime if he is found to be not guilty. She also argues that our holding in <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">509 U. S. 602</a></span> (1993), that the Excessive Fines Clause<footnotemark>6</footnotemark> limits the scope of civil forfeiture judgments, “would be difficult to reconcile with any rule allowing truly innocent persons to be punished by civil forfeiture.” Brief for Petitioner 18-19, n. 12.</p>
<p id="b631-6">In <em><span class="citation" data-id="9432531"><a href="/opinion/112731/foucha-v-louisiana/" aria-description="Citation for case: Foucha v. Louisiana">Foucha</a></span> </em>the Court held that a defendant found not guilty by reason of insanity in a criminal trial could not be thereafter confined indefinitely by the State without a showing that he was either dangerous or mentally ill. Petitioner argues that our statement that in those circumstances a State has no “punitive interest” which would justify continued detention, <span class="citation" data-id="9432531"><a href="/opinion/112731/foucha-v-louisiana/#80" aria-description="Citation for case: Foucha v. Louisiana">504 U. S., at 80</a></span>, requires that Michigan demonstrate a punitive interest in depriving her of her interest in the forfeited car. But, putting aside the extent to which a forfeiture proceeding is “punishment” in the first place, <em><span class="citation" data-id="9432531"><a href="/opinion/112731/foucha-v-louisiana/" aria-description="Citation for case: Foucha v. Louisiana">Foucha</a></span> </em>did not purport to discuss, let alone overrule, <em><span class="citation" data-id="85513"><a href="/opinion/85513/the-palmyra/" aria-description="Citation for case: The Palmyra">The Palmyra</a></span> </em>line of cases.</p>
<p id="b631-7">In <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span>, </em>the Court held that because “forfeiture serves, at least in part, to punish the owner,” forfeiture proceedings are subject to the limitations of the Eighth Amendment’s prohibition against excessive fines. <span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#618" aria-description="Citation for case: Austin v. United States">509 U. S., at 618</a></span>. There was no occasion in that case to deal with the validity of the “innocent-owner defense,” other than to point out that if a forfeiture statute allows such a defense, the defense is <page-number citation-index="1" label="452">*452</page-number>additional evidence that the statute itself is “punitive” in motive. <span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#617" aria-description="Citation for case: Austin v. United States"><em>Id., </em>at 617-618</a></span>. In this case, however, Michigan’s Supreme Court emphasized with respect to the forfeiture proceeding at issue: “It is not contested that this is an equitable action,” in which the trial judge has discretion to consider “alternatives [to] abating the entire interest in the vehicle.” <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#742" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">447 Mich., at 742</a></span>, <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#495" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">527 N. W. 2d, at 495</a></span>.</p>
<p id="b632-5">In any event, for the reasons pointed out in <em><span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co.">Calero-Toledo</a></span> </em>and <em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/" aria-description="Citation for case: Van Oster v. Kansas">Van Oster</a></span>, </em>forfeiture also serves a deterrent purpose distinct from any punitive purpose. Forfeiture of property prevents illegal uses “both by preventing further illicit use of the [property] and by imposing an economic penalty, thereby rendering illegal behavior unprofitable.” <span class="citation" data-id="9425711"><a href="/opinion/109026/calero-toledo-v-pearson-yacht-leasing-co/#687" aria-description="Citation for case: Calero-Toledo v. Pearson Yacht Leasing Co."><em>Calero-Toledo, supra, </em>at 687</a></span>. This deterrent mechanism is hardly unique to forfeiture. For instance, because Michigan also deters dangerous driving by making a motor vehicle owner liable for the negligent operation of the vehicle by a driver who had the owner’s consent to use it, petitioner was also potentially liable for her husband’s use of the car in violation of Michigan negligence law. <span class="citation no-link">Mich. Comp. Laws §257.401</span> (1979). “The law thus builds a secondary defense against a forbidden use and precludes evasions by dispensing with the necessity of judicial inquiry as to collusion between the wrongdoer and the alleged innocent owner.” <em>Van Oster, </em><span class="citation" data-id="100943"><a href="/opinion/100943/van-oster-v-kansas/#467" aria-description="Citation for case: Van Oster v. Kansas">272 U. S., at 467-468</a></span>.</p>
<p id="b632-6">Petitioner also claims that the forfeiture in this case was a taking of private property for public use in violation of the Takings Clause of the Fifth Amendment, made applicable to the States by the Fourteenth Amendment. But if the forfeiture proceeding here in question did not violate the Fourteenth Amendment, the property in the automobile was transferred by virtue of that proceeding from petitioner to the State. The government may not be required to compensate an owner for property which it has already lawfully acquired under the exercise of governmental authority other than the power of eminent domain. <em>United States </em>v. <em>Fuller, </em><page-number citation-index="1" label="453">*453</page-number><span class="citation" data-id="9425088"><a href="/opinion/108659/united-states-v-fuller/#492" aria-description="Citation for case: United States v. Fuller">409 U. S. 488, 492</a></span> (1973); see <em>United States </em>v. <em>Rands, </em><span class="citation" data-id="107541"><a href="/opinion/107541/united-states-v-rands/#125" aria-description="Citation for case: United States v. Rands">389 U. S. 121, 125</a></span> (1967).</p>
<p id="b633-5">At bottom, petitioner’s claims depend on an argument that the Michigan forfeiture statute is unfair because it relieves prosecutors from the burden of separating co-owners who are complicit in the wrongful use of property from innocent co-owners. This argument, in the abstract, has considerable appeal, as we acknowledged in <em>Goldsmith-Grant, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/#510" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S., at 510</a></span>. Its force is reduced in the instant case, however, by the Michigan Supreme Court’s confirmation of the trial court’s remedial discretion, see <em>supra, </em>at 446, and petitioner’s recognition that Michigan may forfeit her and her husband’s car whether or not she is entitled to an offset for her interest in it, Tr. of Oral Arg. 7, 9.</p>
<p id="b633-6">We conclude today, as we concluded 75 years ago, that the cases authorizing actions of the kind at issue are “too firmly fixed in the punitive and remedial jurisprudence of the country to be now displaced.” <em>Goldsmith-Grant, supra, </em>at 511. The State here sought to deter illegal activity that contributes to neighborhood deterioration and unsafe streets. The Bennis automobile, it is conceded, facilitated and was used in criminal activity. Both the trial court and the Michigan Supreme Court followed our longstanding practice, and the judgment of the Supreme Court of Michigan is therefore</p>
<p id="b633-7">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b623-13"> <span class="citation no-link">Mich. Comp. Laws § 750</span>.338b (1979).</p>
</footnote>
<footnote label="2">
<p id="b624-6"> Section 600.3801 states in pertinent part:</p>
<blockquote id="b624-7">“Any building, vehicle, boat, aircraft, or place used for the purpose of lewdness, assignation or prostitution or gambling, or used by, or kept for the use of prostitutes or other disorderly persons, , . is declared a nuisance, . . . and all. . . nuisances shall be enjoined and abated as provided in this act and as provided in the court rules. Any person or his or her servant, agent, or employee who owns, leases, conducts, or maintains any building, vehicle, or place used for any of the purposes or acts set forth in this section is guilty of a nuisance.” <span class="citation no-link">Mich. Comp. Laws Ann. §600.3801</span> (West Supp. 1995).</blockquote>
</footnote>
<footnote label="3">
<p id="b624-9"> Section 600.3825 states in pertinent part:</p>
<blockquote id="b624-10">“(1) Order of abatement. If the existence of the nuisance is established in an action as provided in this chapter, an order of abatement shall be entered as a part of the judgment in the case, which order shall direct the removal from the building or place of all furniture, fixtures and contents therein and shall direct the sale thereof in the manner provided for the sale of chattels under execution ....</blockquote>
<blockquote id="b624-11">“(2) Vehicles, sale. Any vehicle, boat, or aircraft found by the court to be a nuisance within the meaning of this chapter, is subject to the same order and judgment as any furniture, fixtures and contents as herein provided.</blockquote>
<blockquote id="b624-12">“(&amp;) Sale of personalty, costs, liens, balance to state treasurer. Upon the sale of any furniture, fixtures, contents, vehicle, boat or aircraft as provided in this section, the officer executing the order of the court shall, after deducting the expenses of keeping such property and costs of such sale, pay all liens according to their priorities . . . , and shall pay the balance to the state treasurer to be credited to the general fund of the state.. ..” <span class="citation no-link">Mich. Comp. Laws §600.3825</span> (1979).</blockquote>
</footnote>
<footnote label="4">
<p id="b625-7"> “Proof of knowledge of the existence of the nuisance on the part of the defendants or any of them, is not required.” <span class="citation no-link">Mich. Comp. Laws §600.3815</span>(2) (1979).</p>
</footnote>
<footnote label="5">
<p id="b628-10"> In <em>Austin </em>v. <em>United States, </em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/#617" aria-description="Citation for case: Austin v. United States">509 U. S. 602, 617</a></span> (1993), the Court observed that <em>J. W. Goldsmith, Jr.-Grant Co. </em>v. <em>United States, </em><span class="citation" data-id="99692"><a href="/opinion/99692/j-w-goldsmith-jr-grant-co-v-united-states/" aria-description="Citation for case: J. W. Goldsmith, Jr.-Grant Co. v. United States">254 U. S. 505</a></span> (1921), “expressly reserved the question whether the [guilty-property] <page-number citation-index="1" label="449">*449</page-number>fiction could be employed to forfeit the property of a truly innocent owner.” This observation is quite mistaken. The <em>Goldsmith-Grant </em>Court expressly reserved opinion “as to whether the section can be extended to property <em>stolen </em>from the owner or otherwise taken from him <em>without his privity or consent.” Id., </em>at 512 (emphases added). In other words, the <em>Goldsmith-Grant </em>Court drew the very same distinction made by the Michigan Supreme Court in this case: “the distinction between the situation in which a vehicle is used without the owner’s consent,” and one in which, “although the owner consented to [another person’s] use, [the vehicle] is used in a <em>manner </em>to which the owner did not consent.” <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#742" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">447 Mich., at 742, n. 36</a></span>, <span class="citation" data-id="9569121"><a href="/opinion/1303744/michigan-ex-rel-wayne-county-prosecutor-v-bennis/#495" aria-description="Citation for case: MICHIGAN Ex Rel WAYNE COUNTY PROSECUTOR v. BENNIS">527 N. W. 2d, at 495, n. 36</a></span>. Because John Bennis co-owned the car at issue, petitioner cannot claim she was in the former situation.</p>
<p id="b629-7">The dissent, <em>post, </em>at 466-468, and n. 12, quoting <em>Peisch </em>v. <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#364" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C."><em>Ware, 4 </em>Cranch 347, 364</a></span> (1808), seeks to enlarge the reservation in <em>Goldsmith-Grant </em>into a general principle that “ ‘a forfeiture can only be applied to those cases in which the means that are prescribed for the prevention of a forfeiture may be employed.’” But <em><span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">Peisch</a></span> </em>was dealing with the same question reserved in <em>Goldsmith-Grant, </em>not any broader proposition: “If, by private theft, or open robbery, without any fault on his part, [an owner’s] property should be invaded, . . . the law cannot be understood to punish him with the forfeiture of that property.” <span class="citation" data-id="84871"><a href="/opinion/84871/peisch-and-others-v-ware-and-others-c/#364" aria-description="Citation for case: Peisch and Others v. WARE AND OTHERS &amp;C.">4 Cranch, at 364</a></span>.</p>
</footnote>
<footnote label="6">
<p id="b631-8"> U. S. Const., Amdt. 8.</p>
</footnote>
</opinion>
```

---
