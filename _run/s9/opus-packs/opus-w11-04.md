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

## GROUP: _overhaul2/lake/cases/Sorrells v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Sorrells v. United States"
type: case
citation: "287 U.S. 435 (1932)"
parallel_cite: "53 S. Ct. 210; 77 L. Ed. 413; 86 A.L.R. 249"
neutral_cite: 1932 U.S. LEXIS 30
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1932
date_decided: 1932-12-19
docket: 100
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1932-12-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Sorrells v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/101997/sorrells-v-united-states/"
  cluster_id: 101997
  opinion_id: 101997
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Anchor"
related: ["[[Sherman v. United States]]", "[[Hampton v. United States]]", "[[Jacobson v. United States]]", "[[Mathews v. United States]]"]
aliases: []
tags: ["case", "entrapment", "predisposition", "prohibition"]
holding: "Entrapment is a valid defense; it arises when government officials implant the criminal design in the mind of a person who had no…"
lake:
  record_id: Sorrells v. United States
  status: under_review
  projected_at: 2026-07-06
---

# Sorrells v. United States

*287 U.S. 435 (1932)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A Prohibition agent, posing as a fellow World War I veteran, visited Sorrells's home and—after bonding over their shared war service—repeatedly asked Sorrells to obtain liquor. Sorrells twice refused, then eventually procured a half-gallon of whiskey. He was convicted of possessing and selling liquor and asserted entrapment.

## Issue
Whether entrapment is a valid defense, and on what basis, when government agents induce an otherwise law-abiding person to commit a crime.

## Rule
Government inducement of an otherwise innocent person can defeat conviction. "Entrapment is the conception and planning of an offense by an officer, and his procurement of its commission by one who would not have perpetrated it except for the trickery, persuasion, or fraud of the officer." — 287 U.S. at 454. ^pin-454

The Court grounded the defense in statutory construction: Congress is not presumed to have intended its penal statutes to reach a person whose criminal design originated with the government rather than with himself.

## Application
The agent exploited a shared-veteran rapport and persistent entreaties to overcome Sorrells's repeated refusals; because the evidence permitted a finding that the criminal design originated with the government and that Sorrells was not otherwise disposed to the offense, the entrapment issue should have gone to the jury, and the Court reversed.

## Conclusion
Entrapment is a valid defense resting on the inference that Congress did not intend to punish persons lured into crime by its own officers; the conviction was reversed and [[Reading and Citing Cases#on-remand|remanded]] for the jury to decide entrapment.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The origin of the federal entrapment defense and its subjective (predisposition) test, applied in [[Sherman v. United States]] and reaffirmed in [[Jacobson v. United States]] and [[Mathews v. United States]]; the due-process outer boundary was addressed in [[Hampton v. United States]].

## Appears on
- [[Entrapment]] — *Key — Anchor*

## Sources
- *Sorrells v. United States*, 287 U.S. 435 (1932) — https://www.courtlistener.com/opinion/101997/sorrells-v-united-states/ — pinpoint: 454.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b1fb4701bea21f9e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Sorrells v. United States"}, "payload": {"all": [{"cite": "287 U.S. 435", "page": "435", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "287"}, {"cite": "53 S. Ct. 210", "page": "210", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "53"}, {"cite": "77 L. Ed. 413", "page": "413", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "77"}, {"cite": "1932 U.S. LEXIS 30", "page": "30", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1932"}, {"cite": "86 A.L.R. 249", "page": "249", "reporter": "A.L.R.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "86"}], "display": "287 U.S. 435", "official": {"cite": "287 U.S. 435", "page": "435", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "287"}, "official_selection_present": true, "record_id": "Sorrells v. United States"}}
{"assertion_id": "1d7e3b197aa62feb", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-454", "record_id": "Sorrells v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-454", "pinpoint_status": "slip-only", "quote": "--- # Sorrells v. United States *287 U.S. 435 (1932)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Prohibition agent, posing as a fellow World War I veteran, visited Sorrells's home and—after bonding over their shared war service—repeatedly asked Sorrells to obtain liquor. Sorrells twice refused, then eventually procured a half-gallon of whiskey. He was convicted of possessing and selling liquor and asserted entrapment. ## Issue Whether entrapment is a valid defense, and on what basis, when government agents induce an otherwise law-abiding person to commit a crime. ## Rule Government inducement of an otherwise innocent person can defeat conviction.", "quote_fidelity": "mismatch", "record_id": "Sorrells v. United States", "star_marker": null}}
{"assertion_id": "97025b9a83890ad3", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Sorrells v. United States"}, "payload": {"as_of_content": "1932-12-19", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Sorrells v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Sorrells v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Sorrells v. United States",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Sorrells v. United States",
    "case_name_short": "Sorrells",
    "case_name_full": "Sorrells v. United States",
    "input_case_name": "Sorrells v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1932-12-19",
    "year": 1932,
    "docket": "100",
    "cluster_id": 101997,
    "lead_opinion_id": 101997,
    "sibling_ids": [
      101997
    ],
    "absolute_url": "/opinion/101997/sorrells-v-united-states/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "287 U.S. 435",
      "volume": "287",
      "reporter": "U.S.",
      "page": "435",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "53 S. Ct. 210",
        "volume": "53",
        "reporter": "S. Ct.",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 413",
        "volume": "77",
        "reporter": "L. Ed.",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 A.L.R. 249",
        "volume": "86",
        "reporter": "A.L.R.",
        "page": "249",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1932 U.S. LEXIS 30",
        "volume": "1932",
        "reporter": "U.S. LEXIS",
        "page": "30",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "287 U.S. 435",
        "volume": "287",
        "reporter": "U.S.",
        "page": "435",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 S. Ct. 210",
        "volume": "53",
        "reporter": "S. Ct.",
        "page": "210",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "77 L. Ed. 413",
        "volume": "77",
        "reporter": "L. Ed.",
        "page": "413",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1932 U.S. LEXIS 30",
        "volume": "1932",
        "reporter": "U.S. LEXIS",
        "page": "30",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "86 A.L.R. 249",
        "volume": "86",
        "reporter": "A.L.R.",
        "page": "249",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "287 U.S. 435",
    "official_selection": {
      "court_class": "scotus",
      "selected": "287 U.S. 435",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-454",
      "page": null,
      "quote": "--- # Sorrells v. United States *287 U.S. 435 (1932)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A Prohibition agent, posing as a fellow World War I veteran, visited Sorrells's home and\u2014after bonding over their shared war service\u2014repeatedly asked Sorrells to obtain liquor. Sorrells twice refused, then eventually procured a half-gallon of whiskey. He was convicted of possessing and selling liquor and asserted entrapment. ## Issue Whether entrapment is a valid defense, and on what basis, when government agents induce an otherwise law-abiding person to commit a crime. ## Rule Government inducement of an otherwise innocent person can defeat conviction.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1932-12-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Sorrells v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Delgado-Marrero",
          "cluster_id": 2652872,
          "cite": [
            "744 F.3d 167",
            "2014 WL 522462"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Cordae Black",
          "cluster_id": 1086588,
          "cite": [
            "733 F.3d 294"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Delaine and Malisa Fitzpat",
          "cluster_id": 889950,
          "cite": [
            "2012 MT 300",
            "367 Mont. 385",
            "291 P.3d 1106",
            "2012 Mont. LEXIS 368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gutierrez",
          "cluster_id": 32172,
          "cite": [
            "343 F.3d 415",
            "2003 U.S. App. LEXIS 16694",
            "2003 WL 21940783"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Maffett",
          "cluster_id": 1986216,
          "cite": [
            "633 N.W.2d 339",
            "464 Mich. 878"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Reginald Dodd",
          "cluster_id": 770267,
          "cite": [
            "225 F.3d 340",
            "2000 U.S. App. LEXIS 21423"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Terry Lee Brooks",
          "cluster_id": 769099,
          "cite": [
            "215 F.3d 842",
            "2000 U.S. App. LEXIS 13688",
            "2000 WL 764784"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Richard D. Barnett Virgil R. Drake",
          "cluster_id": 766842,
          "cite": [
            "197 F.3d 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vazquez v. State",
          "cluster_id": 1799192,
          "cite": [
            "700 So. 2d 5",
            "1997 WL 361832"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Opn. No.",
          "cluster_id": 3594829,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Sandoval",
          "cluster_id": 603895,
          "cite": [
            "990 F.2d 481",
            "93 Daily Journal DAR 4205",
            "93 Cal. Daily Op. Serv. 2475",
            "1993 U.S. App. LEXIS 6759",
            "1993 WL 94342"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America, Appellant/cross-Appellee v. Jack Pardue, Michel Pardue, Appellee/cross-Appellant",
          "cluster_id": 597867,
          "cite": [
            "983 F.2d 835"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. American Trucking Associations",
          "cluster_id": 103369,
          "cite": [
            "310 U.S. 534",
            "60 S. Ct. 1059",
            "84 L. Ed. 1345",
            "1940 U.S. LEXIS 1049"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Russell",
          "cluster_id": 108768,
          "cite": [
            "36 L. Ed. 2d 366",
            "93 S. Ct. 1637",
            "411 U.S. 423",
            "1973 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Richmond Newspapers, Inc. v. Virginia",
          "cluster_id": 110339,
          "cite": [
            "65 L. Ed. 2d 973",
            "100 S. Ct. 2814",
            "448 U.S. 555",
            "1980 U.S. LEXIS 18",
            "6 Media L. Rep. (BNA) 1833"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee Valley Authority v. Hill",
          "cluster_id": 109897,
          "cite": [
            "57 L. Ed. 2d 117",
            "98 S. Ct. 2279",
            "437 U.S. 153",
            "1978 U.S. LEXIS 33",
            "8 Envtl. L. Rep. (Envtl. Law Inst.) 20513",
            "11 ERC (BNA) 1705"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Thiboutot",
          "cluster_id": 110322,
          "cite": [
            "65 L. Ed. 2d 555",
            "100 S. Ct. 2502",
            "448 U.S. 1",
            "1980 U.S. LEXIS 51"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sherman v. United States",
          "cluster_id": 105681,
          "cite": [
            "2 L. Ed. 2d 848",
            "78 S. Ct. 819",
            "356 U.S. 369",
            "1958 U.S. LEXIS 1024"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mathews v. United States",
          "cluster_id": 112012,
          "cite": [
            "99 L. Ed. 2d 54",
            "108 S. Ct. 883",
            "485 U.S. 58",
            "1988 U.S. LEXIS 943"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lopez v. United States",
          "cluster_id": 106622,
          "cite": [
            "10 L. Ed. 2d 462",
            "83 S. Ct. 1381",
            "373 U.S. 427",
            "1963 U.S. LEXIS 2618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hampton v. United States",
          "cluster_id": 109437,
          "cite": [
            "48 L. Ed. 2d 113",
            "96 S. Ct. 1646",
            "425 U.S. 484",
            "1976 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gore v. United States",
          "cluster_id": 105742,
          "cite": [
            "2 L. Ed. 2d 1405",
            "78 S. Ct. 1280",
            "357 U.S. 386",
            "1958 U.S. LEXIS 1801"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lewis v. United States",
          "cluster_id": 107312,
          "cite": [
            "17 L. Ed. 2d 312",
            "87 S. Ct. 424",
            "385 U.S. 206",
            "1966 U.S. LEXIS 3"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jacobson v. United States",
          "cluster_id": 112720,
          "cite": [
            "118 L. Ed. 2d 174",
            "112 S. Ct. 1535",
            "503 U.S. 540",
            "1992 U.S. LEXIS 2117"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cahan",
          "cluster_id": 1237532,
          "cite": [
            "282 P.2d 905",
            "44 Cal. 2d 434",
            "50 A.L.R. 2d 513",
            "1955 Cal. LEXIS 243"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re Avery W. Vial, Movant",
          "cluster_id": 741872,
          "cite": [
            "115 F.3d 1192",
            "1997 U.S. App. LEXIS 14166",
            "1997 WL 324385"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evans v. Jeff D. Ex Rel. Johnson",
          "cluster_id": 111627,
          "cite": [
            "89 L. Ed. 2d 747",
            "106 S. Ct. 1531",
            "475 U.S. 717",
            "1986 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Corbitt v. New Jersey",
          "cluster_id": 109956,
          "cite": [
            "58 L. Ed. 2d 466",
            "99 S. Ct. 492",
            "439 U.S. 212",
            "1978 U.S. LEXIS 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armstrong Paint & Varnish Works v. Nu-Enamel Corp.",
          "cluster_id": 103108,
          "cite": [
            "305 U.S. 315",
            "59 S. Ct. 191",
            "83 L. Ed. 195",
            "1938 U.S. LEXIS 1174",
            "39 U.S.P.Q. (BNA) 402"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Shuck",
          "cluster_id": 1060967,
          "cite": [
            "953 S.W.2d 662",
            "70 A.L.R. 5th 743",
            "1997 Tenn. LEXIS 487",
            "1997 WL 610824"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Raley v. Ohio",
          "cluster_id": 105925,
          "cite": [
            "3 L. Ed. 2d 1344",
            "79 S. Ct. 1257",
            "360 U.S. 423",
            "1959 U.S. LEXIS 754"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William Christopher Twigg, Iii, United States of America v. Henry Alfred Neville",
          "cluster_id": 361264,
          "cite": [
            "588 F.2d 373"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Burnet v. Guggenheim",
          "cluster_id": 102035,
          "cite": [
            "288 U.S. 280",
            "53 S. Ct. 369",
            "77 L. Ed. 748",
            "1933 U.S. LEXIS 40",
            "1 C.B. 374",
            "11 A.F.T.R. (P-H) 1392",
            "3 U.S. Tax Cas. (CCH) 1043"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haggar Co. v. Helvering, Com'r of Internal Revenue",
          "cluster_id": 103266,
          "cite": [
            "308 U.S. 389",
            "60 S. Ct. 337",
            "84 L. Ed. 340",
            "1940 U.S. LEXIS 1218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dennis",
          "cluster_id": 225410,
          "cite": [
            "183 F.2d 201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mohamed Kamara v. Attorney General of the United States",
          "cluster_id": 791578,
          "cite": [
            "420 F.3d 202",
            "2005 U.S. App. LEXIS 18576",
            "2005 WL 2063873"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sorrells v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(101997) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDI1MTg0MDAwMDAmcz0yMzEwMjY2JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28101997%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(101997)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTQmcz00NDMyNDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28101997%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(101997)",
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
    "complete_query": "cites:(101997)",
    "indexed_citing_opinions": 1231,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 101997,
        "count": 1231,
        "count_source": "search"
      }
    ],
    "citation_count": 1793,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/sorrells-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU5NTQ5NTEmcz00NTI1NDk5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28101997%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 101997,
        "cited_id": 85646,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 85698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 88029,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 88397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 88664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 89421,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 90036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 91233,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 93280,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 93298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94440,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 94604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 95894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 96230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 96460,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 96682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 97368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 98638,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 98755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 98794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 99608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 99734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 100892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 100923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 101251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3415789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3581964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3672124,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3673731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 101997,
        "cited_id": 3884966,
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
    "date_created": "2026-07-05T20:05:23Z",
    "date_modified": "2026-07-06T08:51:01Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:05:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:05:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:10:18Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:05:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Sorrells v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b504-6">
<span citation-index="1" class="star-pagination" label="438"> 
   *438
   </span>
  Mr. Chief Justice Hughes
 </author>
<p id="AGLB">
  delivered the opinion of the Court.
 </p>
<p id="b504-7">
  Defendant was indicted on two counts (1) for possessing and (2) for selling, on July 13, 1930, one-half gallon of whiskey in violation of the National Prohibition Act. He pleaded not guilty. Upon the trial he relied upon the defense of entrapment. The court refused to sustain the defense, denying a motion to direct a verdict in favor of defendant and also refusing to submit the issue of entrapment to the jury. The court ruled that “ as a matter of law ” there was no entrapment. Verdict of guilty followed, motions in arrest, and to set aside the verdict as contrary to the law and the evidence,' were denied, and defendant was sentenced to imprisonment for eighteen
  <span citation-index="1" class="star-pagination" label="439"> 
   *439
   </span>
  months. The Circuit Court of Appeals affirmed the judgment, 57 F. (2d) 973, and this Court granted a writ of certiorari limited to the question whether the evidence was sufficient to go to the jury upon the issue of entrapment.
 </p>
<p id="b505-5">
  The Government, while supporting the conclusion of the court below, also urges that the defense, if available, should have been pleaded in bar to further proceedings under the indictment and could not be raised under the plea of not guilty. This question of pleading appropriately awaits the consideration of the nature and grounds of the defense.
 </p>
<p id="b505-6">
  The substance of the testimony at the trial as to entrapment was as follows: For the Government, one Martin, a prohibition agent, testified that having resided for a time in Haywood County, North Carolina, where he posed as a tourist, he visited defendant’s home near Canton, on Sunday, July 13, 1930, accompanied by three residents of the county who knew the defendant well. He was introduced as a resident of Charlotte who was stopping for a time at Clyde. The witness ascertained that defendant was a veteran of the World War and a former member of the 30th Division A. E. F. Witness informed defendant that he was also an ex-service man and a former member of the same Division, which was true. Witness' asked defendant if he could get the witness some liquor and defendant stated that he did not have any. Later, there was a second request without result. One of those present, one Jones, was also an ex-service man and a former member of the 30th Division, and the conversation turned to the war experiences of the three. After this, witness asked defendant for a third time to get him some liquor, whereupon defendant left his home and after a few minutes came back with a half gallon of liquor for which the witness paid defendant five dollars. Martin also testified that he was “ the first and only person among those pres
  <span citation-index="1" class="star-pagination" label="440"> 
   *440
   </span>
  ent at the time who said anything about securing some liquor,” and that his purpose was to prosecute the defendant for procuring and selling it. The Government rested its case on Martin’s testimony.
 </p>
<p id="b506-6">
  Defendant called as witnesses the three persons who had accompanied the prohibition agent. In substance, they corroborated the latter’s story but with some additions. Jones, a railroad employee, testified that he had introduced the agent to the defendant “as a furniture dealer of Charlotte,” because the agent had so represented himself; that witness told defendant that the agent was “an old 30th Division man ” and the agent thereupon said to defendant that he “would like to get a half gallon of whiskey to take back to Charlotte to a friend of his that was in the furniture business with him,” and that defendant replied that he “ did not fool with whiskey ”; that the agent and his companions were at defendant’s home “ for probably an hour or an hour and a half and that during such time the agent asked the defendant three or four or probably five times to get him, the agent, some liquor.” Defendant said “ he would go and see if he could get a half gallon of liquor ” and he returned with it after an absence of “ between twenty and thirty minutes.” Jones added that at that time he had never heard of defendant being in the liquor business, that he and the defendant were “ two old buddies,” and that he believed “ one former war buddy would get liquor for another.”
 </p>
<p id="b506-7">
  Another witness, the timekeeper and assistant paymaster of the Champion Fibre Company at Canton, testified that defendant was an employee of that company and had been “ on his job continuously without missing a pay day since March, 1924.” Witness identified the time sheet showing this employment. This witness and three others who were neighbors of the defendant and had known him for many years testified to his good character.
 </p>
<p id="b507-5">
<span citation-index="1" class="star-pagination" label="441"> 
   *441
   </span>
  To rebut this testimony, the Government called three witnesses who testified that the defendant had the general reputation of a rum-runner. There was no evidence that the defendant had ever possessed or sold any intoxicating liquor prior to the transaction in question.
 </p>
<p id="b507-6">
  It is clear that the evidence was sufficient to warrant a finding that the act for which defendant was prosecuted was instigated by the prohibition agent, that it was the creature of his purpose, that defendant had no previous disposition to commit it but was an industrious, law-abiding citizen, and that the agent lured defendant, otherwise innocent, to its commission by repeated and persistent solicitation in which he succeeded by taking advantage of the sentiment aroused by reminiscences of their experiences as companions in arms in the World War. Such a gross abuse of authority given for the purpose of detecting and punishing crime, and not for the making of criminals, deserves the severest condemnation, but the question whether it precludes prosecution or affords a ground of defense, and, if so, upon what theory, has given rise to conflicting opinions.
 </p>
<p id="b507-7">
  It is well settled that the fact that officers or employees of the Government merely afford opportunities or facilities for the commission of the offense does not defeat the prosecution. Artifice and stratagem may be employed to catch those engaged in criminal enterprises.
  <em>
   Grimm
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94127"><a href="/opinion/94127/grimm-v-united-states/#610" aria-description="Citation for case: Grimm v. United States">156 U. S. 604, 610</a></span>;
  <em>
   Goode
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94294"><a href="/opinion/94294/goode-v-united-states/#669" aria-description="Citation for case: Goode v. United States">159 U. S. 663, 669</a></span>;
  <em>
   Rosen
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417701"><a href="/opinion/94359/rosen-v-united-states/#42" aria-description="Citation for case: Rosen v. United States">161 U. S. 29, 42</a></span>;
  <em>
   Andrews v. United States,
  </em>
  <span class="citation" data-id="94440"><a href="/opinion/94440/andrews-v-united-states/#423" aria-description="Citation for case: Andrews v. United States">162 U. S. 420, 423</a></span>;
  <em>
   Price
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="94604"><a href="/opinion/94604/price-v-united-states/#315" aria-description="Citation for case: Price v. United States">165 U. S. 311, 315</a></span>;
  <em>
   Bates
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8122456"><a href="/opinion/8160801/bates-v-united-states/#94" aria-description="Citation for case: Bates v. United States">10 Fed. 92, 94</a></span>, note, p. 97.
  <em>
   United States
  </em>
  v.
  <em>
   Reisenweber,
  </em>
  <span class="citation" data-id="8829953"><a href="/opinion/8844712/united-states-v-reisenweber/#526" aria-description="Citation for case: United States v. Reisenweber">288 Fed. 520, 526</a></span>;
  <em>
   Aultman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8830418"><a href="/opinion/8845169/aultman-v-united-states/" aria-description="Citation for case: Aultman v. United States">289 Fed. 251</a></span>.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The appropriate object of this permitted activity, frequently essential to the enforcement of the law, is to
  <span citation-index="1" class="star-pagination" label="442"> 
   *442
   </span>
  reveal the criminal design; to expose the illicit traffic, the prohibited publication, the fraudulent use of the mails, the illegal conspiracy, or other offenses, and thus to disclose the would-be violators of the law. A different question is presented when the criminal design originates with the officials of the Government, and they implant in the mind of an innocent person the disposition to commit the alleged offense and induce its commission in order that they may prosecute.
 </p>
<p id="b508-5">
  The Circuit Court of Appeals reached the conclusion that the defense of entrapment can be maintained only where, as a result of inducement, the accused is placed in the attitude of having committed ,a crime which he did not intend to commit, or where, by reason of the consent implied in the inducement, no crime has in fact been committed. 57 F. (2d) p. 974. As illustrating the first class, reference is made to the case of a sale of liquor to an Indian who was disguised so as to mislead the accused as to his identity.
  <em>
   United States
  </em>
  v.
  <em>
   Healy,
  </em>
  <span class="citation" data-id="8786735"><a href="/opinion/8802548/united-states-v-healy/" aria-description="Citation for case: United States v. Healy">202 Fed. 349</a></span>;
  <em>
   Voves
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="8807195"><a href="/opinion/8822500/voves-v-united-states/" aria-description="Citation for case: Voves v. United States">249 Fed. 191</a></span>. In the second class are found cases such as those of larceny or rape where want of consent is an element of the crime.
  <em>
   Regina
  </em>
  v.
  <em>
   Fletcher,
  </em>
  8 Cox C. C. 131;
  <em>
   Rex
  </em>
  v.
  <em>
   McDaniel,
  </em>
  Fost. 121, 127, 128;
  <em>
   Connor
  </em>
  v.
  <em>
   People,
  </em>
  <span class="citation" data-id="6562355"><a href="/opinion/6683158/connor-v-people/" aria-description="Citation for case: Connor v. People">18 Colo. 373</a></span> ; <span class="citation no-link">33 Pac. 159</span>;
  <em>
   Williams
  </em>
  v.
  <em>
   Georgia,
  </em>
  <span class="citation" data-id="5557787"><a href="/opinion/5707869/williams-v-state/" aria-description="Citation for case: Williams v. State">55 Ga. 391</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Whittier,
  </em>
  <span class="citation" data-id="8687089"><a href="/opinion/8703909/united-states-v-whittier/" aria-description="Citation for case: United States v. Whittier">5 Dill. 35</a></span>;
  <em>
   State
  </em>
  v.
  <em>
   Adams,
  </em>
  <span class="citation" data-id="3672124"><a href="/opinion/3925541/state-v-adams/" aria-description="Citation for case: State v. . Adams">115 N. C. 775</a></span>; <span class="citation" data-id="3672124"><a href="/opinion/3925541/state-v-adams/" aria-description="Citation for case: State v. . Adams">20 S. E. 722</a></span>. There may also be.physical conditions which are essential to the offense and which do not exist in the case of a trap, as, for example, in the case of a prosecution for burglary where it appears that by reason of the trap there is no breaking.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
<em>
   Rex
  </em>
  v.
  <em>
   Egginton,
  </em>
  2 Leach C. C. 913;
  <em>
   Regina
  </em>
  v.
  <em>
   Johnson,
  </em>
  Car. &amp; Mar. 218;
  <em>
   Saunders
  </em>
  v.
  <em>
   People,
  </em>
  <span class="citation" data-id="7928801"><a href="/opinion/7976263/saunders-v-people/" aria-description="Citation for case: Saunders v. People">38 Mich 218</a></span>;
  <em>
   People
  </em>
  v.
  <em>
   McCord,
  </em>
  <span class="citation" data-id="7934195"><a href="/opinion/7981425/people-v-mccord/" aria-description="Citation for case: People v. McCord">76 Mich. 200</a></span>; <span class="citation" data-id="7934195"><a href="/opinion/7981425/people-v-mccord/" aria-description="Citation for case: People v. McCord">42 N. W. 1106</a></span>;
  <em>
   Allen
  </em>
  v.
  <em>
   State,
  </em>
  <span class="citation" data-id="6507278"><a href="/opinion/6630823/allen-v-state/" aria-description="Citation for case: Allen v. State">40 Ala. 334</a></span>;
  <em>
   Love
  </em>
  v.
  <em>
   People,
  </em>
  160 Ill.
  <span citation-index="1" class="star-pagination" label="443"> 
   *443
   </span>
  501; <span class="citation" data-id="6966669"><a href="/opinion/7062620/love-v-people/" aria-description="Citation for case: Love v. People">43 N. E. 710</a></span>. But these decisions .applying accepted principles to particular offenses, do not reach, much less determine, the present question. Neither in reasoning nor in effect do they prescribe limits for the doctrine of entrapment.
 </p>
<p id="ACZY">
  While this Court has not spoken on the precise question (see
  <em>
   Casey
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418615"><a href="/opinion/101251/casey-v-united-states/#419" aria-description="Citation for case: Casey v. United States">276 U. S. 413, 419</a></span>, 423
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  ), the weight of authority in the lower federal courts is decidedly in favor of the view that in such case as the one before us the defense of entrapment is available. The Government concedes that its contention, in supporting the ruling of the Circuit Court of Appeals, is opposed by decisions in all the other Circuits except the Tenth Circuit, and no decision in that Circuit suggesting a different view has been brought to Our attention. See
  <em>
   Capuano
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 1st), 9 F. (2d) 41, 42;
  <em>
   United States
  </em>
  v.
  <em>
   Lynch
  </em>
  (S. D. N. Y., Hough, J.), <span class="citation" data-id="8811194"><a href="/opinion/8826376/united-states-v-lynch/#984" aria-description="Citation for case: United States v. Lynch">256 Fed. 983, 984</a></span>;
  <em>
   Lucadamo
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 2d), <span class="citation" data-id="8825386"><a href="/opinion/8840238/lucadamo-v-united-states/#657" aria-description="Citation for case: Lucadamo v. United States">280 Fed. 653, 657, 658</a></span>;
  <em>
   Zucker
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 3d), <span class="citation" data-id="8829829"><a href="/opinion/8844592/zucker-v-united-states/#15" aria-description="Citation for case: Zucker v. United States">288 Fed. 12, 15</a></span>;
  <em>
   Gargano
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 5th), 24 F. (2d) 625, 626;
  <em>
   Cermak
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 6th), 4 F. (2d) 99;
  <em>
   O’Brien
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 7th), 51 F. (2d) 674, 679, 680;
  <em>
   Butts
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 8th), <span class="citation" data-id="8820799"><a href="/opinion/8835759/butts-v-united-states/#38" aria-description="Citation for case: Butts v. United States">273 Fed. 35, 38</a></span>;
  <em>
   Woo Wai
  </em>
  v.
  <em>
   United States
  </em>
  (C. C. A. 9th), <span class="citation" data-id="8795796"><a href="/opinion/8811409/woo-wai-v-united-states/" aria-description="Citation for case: Woo Wai v. United States">223 Fed. 412</a></span>. And the Circuit Court of Appeals of the Fourth Circuit, in the instant case, was able to reach its conclusion only by declining to follow the rule which it had laid down in its earlier decision in
  <em>
   Newman
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9335893"><a href="/opinion/9340549/newman-v-states/#131" aria-description="Citation for case: Newman v. States">299 Fed. 128, 131</a></span>.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  It
  <span citation-index="1" class="star-pagination" label="444"> 
   *444
   </span>
  should be added that in many cases in.which the evidence has been found insufficient to support the defense of entrapment the availability of that defense, on a showing of such facts as are present here, has been recognized.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  The federal courts have generally approved the statement of Circuit Judge Sanborn in the leading case of
  <em>
   Butts
  </em>
  v.
  <em>
   United States, supra,
  </em>
  as follows: “ The first duties of the officers of the law are to prevent, not to punish crime. It is not their duty to incite to and create crime for the sole purpose of prosecuting and punishing it. Here the evidence strongly tends to prove, if it does not conclusively do so, that their first and chief endeavor was to cause, to create, crime in order to punish it, and it is unconscionable, contrary to public policy, and to the established law of the land to punish a man for the Commission of an offense of the like of which he had never been guilty, either in thought or in deed, and evidently never would have been guilty of if the officers .¡of the law had not inspired, incited, persuaded, and lured him to attempt to com
  <span citation-index="1" class="star-pagination" label="445"> 
   *445
   </span>
  xnit it.” The judgment in that case was reversed because of the * fatal error ’ of the trial court in refusing to instruct the jury to that effect. In
  <em>
   Newman
  </em>
  v.
  <em>
   United States, supra,
  </em>
  the applicable principle was thus stated by Circuit Judge Woods: “It is well settled that decoys may be used to entrap criminals, and to present opportunity to one intending or willing to commit crime. But decoys are not permissible to ensnare the innocent and law-abiding into the commission of crime. When the criminal design originates, not with the accused, but is conceived in the mind of the government officers, and the accused is by persuasion, deceitful representation, or inducement lured into the commission of a criminal act, the government is estopped by sound public policy from prosecution therefor.” These quotations sufficiently indicate the grounds of the decisions above cited.
 </p>
<p id="b511-6">
  The validity of the principle as thus stated and applied is challenged both upon theoretical and practical grounds. The argument, from the standpoint of principle, is that the court is called upon to try the accused for a particular offense which is defined by statute and that, if the evidence shows that this offense has knowingly been committed, it matters not that its commission was induced by officers of the Government in the manner and circumstances assumed. It is said that where one intentionally does an act in circumstances known to him, and the particular conduct is forbidden by the law in those circumstances, he intentionally breaks the law in the only sense in which the law considers intent.
  <em>
   Ellis
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9418092"><a href="/opinion/96682/ellis-v-united-states/#257" aria-description="Citation for case: Ellis v. United States">206 U. S. 246, 257</a></span>. Moreover, that as the statute is designed to redress ,a public wrong, and not a private injury, there is no ground for holding the Government estopped by the conduct of its officers from prosecuting the offender. To the suggestion of public policy the objectors answer that the legislature, acting within its constitutional au
  <span citation-index="1" class="star-pagination" label="446"> 
   *446
   </span>
  thority, is the arbiter of public
  <em>
   policy
  </em>
<a class="footnote" href="#fn6" id="fn6_ref">
<em>
    6
   </em>
</a>
<em>
</em>
  and that, where conduct is expressly forbidden and penalized by a valid statute, the courts are not at liberty to disregard the law and to bar a prosecution for its violation because they are of the opinion that the crime has been instigated by government officials.
 </p>
<p id="b512-5">
  It is manifest that these arguments rest entirely upon the letter of the statute. They take no account of the fact that its application in the circumstances under consideration is foreign to its purpose; that such an application is so shocking to the sense of justice that it has been urged that it is the duty of the court to stop the prosecution in the interest of the Government itself, to protect it from the illegal conduct of its officers and to preserve the purity of its courts.
  <em>
   Casey
  </em>
  v.
  <em>
   United States, supra.
  </em>
  But can an application of the statute having such an effect— creating a situation so contrary to the purpose of the law and so inconsistent with its proper enforcement as to invoke such a challenge — fairly be deemed to be within its intendment?
 </p>
<p id="b512-6">
  Literal interpretation of statutes at the expense of the reason of the law and producing absurd consequences or flagrant injustice has frequently been condemned. In
  <em>
   United States
  </em>
  v.
  <em>
   Palmer,
  </em>
  <span class="citation" data-id="8373757"><a href="/opinion/8403414/united-states-v-palmer/#631" aria-description="Citation for case: United States v. Palmer">3 Wheat. 610, 631</a></span>, Chief Justice Marshall, in construing the Act of' Congress of April 30, 1790, §8(1 Stat. 113) relating to robbery on the high seas, found that the words “ any person or persons ” were “ broad enough to comprehend every human being,” but he concluded that “ general words must not only be limited to- cases within the jurisdiction of the state, but also to those objects to which the legislature intended to apply them.” In
  <em>
   United States
  </em>
  v.
  <em>
   Kirby,
  </em>
  <span class="citation" data-id="88029"><a href="/opinion/88029/united-states-v-kirby/" aria-description="Citation for case: United States v. Kirby">7 Wall. 482</a></span>, the case arose under the Act of Congress of March 3, 1825
  <span citation-index="1" class="star-pagination" label="447"> 
   *447
   </span>
  (<span class="citation no-link">4 Stat. 104</span>) providing for the conviction of any person who “ shall knowingly and willfully obstruct or retard the passage of the mail, or of any driver or carrier . . . carrying the same.” Considering the purpose of the statute, the Court held that it had no application to the obstruction or retarding of the passage of the mail or of its carrier by reason of the arrest of the carrier upon a warrant issued by a state court. The Court said: “All laws should receive a sensible construction. General terms should be so limited in their application as not to lead to injustice, oppression, or an absurd consequence. It will always, therefore, be presumed that the legislature intended exceptions to its language which would avoid results of this character. The reason of the law in such cases should prevail over its letter.” And the Court supported this conclusion by reference to the classical illustrations found in Puffendorf and Plowden.
  <em>
   Id.,
  </em>
  pp. 486, 487.
 </p>
<p id="b513-4">
  Applying this principle in
  <em>
   Lau Ow Bew
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="93298"><a href="/opinion/93298/lau-ow-bew-v-united-states/" aria-description="Citation for case: Lau Ow Bew v. United States">144 U. S. 47</a></span>, the Court decided that a statute requiring the permission of the Chinese government, and identification by certificate, of “ every Chinese person other than a laborer,” entitled by treaty or the act of Congress to come within the United States, did not apply to Chinese merchants already domiciled in the United States, who had left the country for temporary purposes,
  <em>
   animo revertendi,
  </em>
  and sought to reenter it on their return to their business and their homes. And in
  <em>
   United States
  </em>
  v.
  <em>
   Katz,
  </em>
  <span class="citation" data-id="100892"><a href="/opinion/100892/united-states-v-katz/#362" aria-description="Citation for case: United States v. Katz">271 U. S. 354, 362</a></span>, construing § 10 of the National Prohibition Act so as to avoid an unreasonable application of its words, if taken literally, the Court again declared that “ general terms descriptive of a class of persons made subject to a criminal statute may and should be limited where the literal application of the statute would lead to extreme or absurd results, and where the legislative pur
  <span citation-index="1" class="star-pagination" label="448"> 
   *448
   </span>
  pose gathered from the whole Act would be satisfied by a more limited interpretation.”
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  See, to the same effect,
  <em>
   Heydenfeldt
  </em>
  v.
  <em>
   Daney Gold Mining Co.,
  </em>
  <span class="citation" data-id="89421"><a href="/opinion/89421/heydenfeldt-v-daney-gold-and-silver-mining-co/#638" aria-description="Citation for case: Heydenfeldt v. Daney Gold and Silver Mining Co.">93 U. S. 634, 638</a></span>;
  <em>
   Carlisle
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="88664"><a href="/opinion/88664/carlisle-v-united-states/#153" aria-description="Citation for case: Carlisle v. United States">16 Wall. 147, 153</a></span>;
  <em>
   Oates
  </em>
  v.
  <em>
   National Bank,
  </em>
  <span class="citation" data-id="90036"><a href="/opinion/90036/oates-v-national-bank/" aria-description="Citation for case: Oates v. National Bank">100 U. S. 239</a></span>;
  <em>
   Chew Heong
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9417392"><a href="/opinion/91233/chew-heong-v-united-states/#555" aria-description="Citation for case: Chew Heong v. United States">112 U. S. 536, 555</a></span>;
  <em>
   Holy Trinity Church
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="93280"><a href="/opinion/93280/church-of-the-holy-trinity-v-united-states/#459" aria-description="Citation for case: Church of the Holy Trinity v. United States">143 U. S. 457, 459-462</a></span>;
  <em>
   Hawaii
  </em>
  v.
  <em>
   Mankichi,
  </em>
  <span class="citation" data-id="9417915"><a href="/opinion/95894/hawaii-v-mankichi/#212" aria-description="Citation for case: Hawaii v. Mankichi">190 U. S. 197, 212-214</a></span>;
  <em>
   Jacobson
  </em>
  v.
  <em>
   Massachusetts,
  </em>
  <span class="citation" data-id="96230"><a href="/opinion/96230/jacobson-v-massachusetts/#39" aria-description="Citation for case: Jacobson v. Massachusetts">197 U. S. 11, 39</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Jin Fuey Moy,
  </em>
  <span class="citation" data-id="98755"><a href="/opinion/98755/united-states-v-jin-fuey-moy/#402" aria-description="Citation for case: United States v. Jin Fuey Moy">241 U. S. 394, 402</a></span>;
  <em>
   Baender
  </em>
  v.
  <em>
   Barnett,
  </em>
  <span class="citation" data-id="99734"><a href="/opinion/99734/baender-v-barnett/#226" aria-description="Citation for case: Baender v. Barnett">255 U. S. 224, 226</a></span>;
  <em>
   United States
  </em>
  v.
  <em>
   Chemical Foundation,
  </em>
  <span class="citation" data-id="100923"><a href="/opinion/100923/united-states-v-chemical-foundation-inc/#18" aria-description="Citation for case: United States v. Chemical Foundation, Inc.">272 U. S. 1, 18</a></span>.
 </p>
<p id="b514-6">
  We think that this established principle of construction is applicable here. We are unable to conclude that it was the intention of the Congress in enacting this statute that its processes of detection and enforcement should be abused by the instigation by government officials of an act on the part of persons otherwise innocent in order to lure them to its commission and to punish them. We are not forced by the letter to do violence to the spirit and purpose of the statute. This, we think, has been the underlying and controlling thought in the suggestions in judicial opinions that the Government in such a case is estopped to prosecute or that the courts should bar the prosecution. If the requirements of the highest public policy in the maintenance of the integrity
  <span citation-index="1" class="star-pagination" label="449"> 
   *449
   </span>
  of administration would preclude the enforcement of the statute in such circumstances as are present here, the same considerations justify the conclusion that the case lies outside the purview of the Act and that its general words should not be construed to demand a proceeding at once inconsistent with that policy and abhorrent to the sense of justice. This view does not derogate from the authority of the court to deal appropriately with abuses of its process and it obviates the objection to the exercise by the court of a dispensing power in forbidding the prosecution of one who is charged with conduct assumed to fall within the statute.
 </p>
<p id="b515-6">
  We are unable to approve the view that the court, although treating the statute as applicable despite the entrapment, and the defendant as guilty, has authority to grant immunity, .or to adopt a procedure to that end. It is the function of the court to construe the statute, not to defeat it as construed. Clemency is the function of the Executive.
  <em>
   Ex parte United States,
  </em>
  <span class="citation" data-id="98794"><a href="/opinion/98794/ex-parte-united-states/#42" aria-description="Citation for case: Ex Parte United States">242 U. S. 27, 42</a></span>. In that case, this Court decisively denied such authority to free guilty defendants, in holding that the court had no power to suspend sentences indefinitely. The Court, speaking by Chief Justice White, said — “ if it be that the plain legislative command fixing a specific punishment for crime is subject to be permanently set aside by an implied judicial power upon considerations extraneous to the legality of the conviction, it would seem necessarily to follow that there could be likewise implied a discretionary authority to permanently refuse to try a criminal charge because of the conclusion that a particular act made criminal by law ought not to be treated as criminal. And thus it would come to pass that the possession by the judicial department of power to permanently refuse to enforce a law would result in the destruction of the conceded powers of the other departments and hence leave no law to be enforced.” And while recognizing the hu
  <span citation-index="1" class="star-pagination" label="450"> 
   *450
   </span>
  mane considerations which had led judges to adopt the practice of suspending sentences indefinitely in certain cases, the Court found no ground for approving the practice “ since its exercise in the very ^nature of things amounts to a refusal by the judicial power to perform a duty resting upon it and, as a consequence thereof, to an interference with both the legislative and executive authority as fixed by the Constitution.”
  <em>
   Id.
  </em>
  pp. 51, 52. Where defendant has been duly indicted for an offense found to be within the statute, and the proper authorities seek to proceed with the prosecution, the court cannot refuse to try the case in the constitutional method because it desires to let the defendant go free.
 </p>
<p id="b516-5">
  Suggested analogies from procedure in civil cases are not helpful. When courts of law refuse to sustain alleged causes of action which grow out of illegal schemes, the applicable law itself denies the right to recover. Where courts of equity refuse equitable relief because complainants come with unclean hands, they are administering the principles of equitable jurisprudence governing equitable rights. But in a criminal prosecution, the statute defining the offense is necessarily the law of the case.
 </p>
<p id="b516-6">
  To construe statutes so as to .avoid absurd or glaringly unjust results, foreign to the legislative purpose, is, as we have seen, a traditional and appropriate function of the courts. Judicial nullification of statutes, admittedly valid and applicable, has, happily, no place in our system. The Congress by legislation can always, if it desires, alter the effect of judicial construction of statutes. We conceive it to be our duty to construe the statute here in question reasonably, and we hold that it is beyond our prerogative to give the statute an unreasonable construction, confessedly contrary to public policy, and then to decline to enforce it.
 </p>
<p id="b516-7">
  The conclusion we have reached upon these grounds carries its own limitation. We are dealing with a statu
  <span citation-index="1" class="star-pagination" label="451"> 
   *451
   </span>
  tory prohibition and we are simply concerned to ascertain whether in the light of a plain public policy and of the proper administration of justice, conduct induced as stated should be deemed to be within that prohibition. We have no occasion to consider hypothetical cases of crimes so heinous or revolting that the applicable law would admit of no exceptions. No such situation is presented here. The question in each case must be determined by the scope of the law considered in the light of what may fairly be deemed to be its object.
 </p>
<p id="b517-4">
  Objections to the defense of entrapment are also urged upon practical grounds. But considerations of mere convenience must yield to the essential demands of justice. The argument is pressed that if the defense is available it will lead to the introduction of issues of a collateral character relating to the activities of the officials of the- Government and to the conduct and purposes of the defendant previous to the alleged offense. For the defense of entrapment is not simply that the particular act was committed at the instance of government officials. That is often the case where the proper action of these officials leads to the revelation of criminal enterprises.
  <em>
   Grimm
  </em>
  v.
  <em>
   United States, supra.
  </em>
  The predisposition and criminal design of the defendant are relevant. But the issues raised and the evidence adduced must be pertinent to the controlling question whether the defendant is a person otherwise innocent whom the Government is seeking to punish for an alleged offense which is the product of the creative activity of its own officials. If that is the fact, common justice requires that the accused be permitted to prove it. The Government in such a case is in no position to object to evidence of the activities of its representatives in relation to the accused, and if the defendant seeks acquittal by reason of entrapment he cannot complain of an appropriate and searching inquiry into his own conduct and predisposition as bearing upon that issue. If in con
  <span citation-index="1" class="star-pagination" label="452"> 
   *452
   </span>
  sequence he suffers a disadvantage, he has brought it upon himself by reason of the nature of the defense.
 </p>
<p id="b518-5">
  What has been said indicates the answer to the contention of the Government that the defense of entrapment must be pleaded in bar to further proceedings under the indictment and cannot be raised under the plea of not guilty. This contention presupposes that the defense is available to the accused and relates only to the manner in which it shall be presented. The Government considers the defense as analogous to a plea of pardon or of
  <em>
   autrefois convict
  </em>
  or
  <em>
   autrefois acquit.
  </em>
  It is assumed that the accused is not denying his guilt but is setting up special facts in bar upon which he relies regardless of his guilt or innocence of the crime charged. This, as we have seen, is a misconception. The defense is available, not in the view that the accused though guilty may go free, but that the Government cannot be permitted to contend that he is guilty of a crime where the government officials are the instigators of his conduct. The federal courts in sustaining the defense in such circumstances have proceeded in the view that the defendant is not guilty. The practice of requiring a plea in bar has not obtained. Fundamentally, the question is whether the defense, if the facts bear it otit, takes the case out of the purview of the statute because it cannot be supposed that the Congress intended that the letter of its enactment should be used to support such a gross perversion of its purpose.
 </p>
<p id="b518-6">
  We are of the opinion that upon the evidence produced in the instant case the defense of entrapment was available and that the trial court was in error in holding that as a matter of law there was no entrapment and in refusing to submit the issue to the jury.
 </p>
<p id="b518-7">
  The judgment is reversed and the cause is remanded for further proceedings in conformity with this opinion.
 </p>
<p id="b518-8">
<em>
   Judgment reversed.
  </em>
</p>
<author id="b519-3">
<span citation-index="1" class="star-pagination" label="453"> 
   *453
   </span>
  Mr. Justice McReynolds
 </author>
<p id="AsVD">
  is of the opinion that the judgment below should be affirmed.
 </p>
<p id="b519-4">
  Separate opinion of
 </p>
<author id="AUGg">
  Mr. Justice Roberts.
 </author>
<p id="b519-5">
  The facts set forth in the court’s opinion establish that a prohibition enforcement officer instigated the commission of the crime charged. The courts below held that the showing was insufficient, as matter of law, to sustain the claim of entrapment, and that the jury were properly instructed to ignore that defense in their consideration of the case. A conviction resulted. The Government maintains that the issue of entrapment is not triable under the plea of not guilty, but should be raised by plea in bar or be adjudicated in some manner by the court rather than by the jury, and as the trial court properly decided the question, the record presents ho reversible error. I think, however, the judgment should be reversed, but for reasons and upon grounds other than those stated in the opinion of the court.
 </p>
<p id="b519-6">
  Of late the term “ entrapment ” has been adopted by the courts to signify instigation of crime by officers of government. The cases in which such incitement has been recognized as a defense have grown to an amazing total.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  The increasing frequency of the assertion that the defendant was entrapped is doubtless due to the creation by statute of many new crimes, (e. g., sale and transportation of liquor and narcotics) and the correlative establishment of special enforcement bodies for the detection and punishment of offenders. The efforts of members of these forces to obtain arrests and convictions have too often been marked by reprehensible methods.
 </p>
<p id="b519-7">
  Society is at war with the criminal classes, and courts have uniformly held that in waging this warfare the forces of prevention and detection may use traps, decoys, and
  <span citation-index="1" class="star-pagination" label="454"> 
   *454
   </span>
  deception to obtain evidence of the commission of crime. Resort to such means does not render an indictment thereafter found a nullity nor call for the exclusion of evidence so procured.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  3But the defense here asserted involves more than obtaining evidence by artifice or deception. Entrapment is the conception and planning of an offense by an officer, and his procurement of its commission by one who would not have perpetrated it except for the trickery, persuasion, or fraud of the officer. Federal and state courts have held that substantial proof of entrapment as thus defined calls for the submission of the issue to the jury and warrants an acquittal. The reasons assigned in support of this procedure have not been uniform. Thus it has been held that the acts of its officers estop the government to prove the offense. The result has also been justified by the mere statement of the rule that where entrapment is proved the defendant is not guilty of the crime charged. Often the defense has been permitted upon grounds of public policy, which the courts formulate by saying they will not permit their process to be used in aid of a scheme for the actual creation of a crime by those whose duty is to deter its commission.
 </p>
<p id="b520-5">
  This court has adverted to the doctrine,
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  but has not heretofore had occasion to determine its validity, the basis on which it should rest, or the procedure to be followed when it is involved. The present case affords the opportunity to settle these matters as respects the administration of the federal criminal law.
 </p>
<p id="b520-6">
  There is common agreement that where a law officer envisages a crime, plans it, and activates its commission by one not theretofore intending its perpetration, for the sole purpose of obtaining a victim through indictment, conviction and sentence, the consummation of so revolting a plan
  <span citation-index="1" class="star-pagination" label="455"> 
   *455
   </span>
  ought not to be permitted by any self-respecting tribunal. Equally true is this whether the offense is one at common law or merely a creature of statute. Public policy forbids such sacrifice of decency. The enforcement of this policy calls upon the court, in every instance where alleged entrapment of a defendant is brought to its notice, to ascertain the facts, to appraise their effect upon the administration of justice, and to make such order with respect to the further prosecution of the cause as the circumstances require.
 </p>
<p id="b521-6">
  This view calls for no distinction between crimes
  <em>
   mala in se
  </em>
  and statutory offenses of lesser gravity; requires no statutory construction, and attributes no merit to ,a guilty defendant; but frankly recognizes the true foundation of the doctrine in the public policy which protects the purity of government and its processes. Always the courts refuse their aid in civil cases to the perpetration and consummation of an illegal scheme. Invariably they hold a civil action must be abated if its basis is violation of the decencies of life, disregard of the rules, statutory or common law, which formulate the ethics of men’s relations to each other. Neither courts of equity nor those administering legal remedies tolerate the use of their process to consummate a wrong.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
  The doctrine of entrapment in criminal law is the analogue of the same rule applied in civil proceedings. And this is the real basis of the decisions approving the defense of entrapment, though in statement the rule is cloaked under a declaration that the government is estopped or the defendant has not been proved guilty.
 </p>
<p id="b521-7">
  A new method of rationalizing the defense is now asserted. ' This is to construe the act creating the offense by
  <span citation-index="1" class="star-pagination" label="456"> 
   *456
   </span>
  reading in a condition or proviso that if the offender shall have been entrapped into crime the law shall not apply to him. So, it is said, the true intent of the legislature will be effectuated. This seems a strained and unwarranted construction of the statute; and amounts, in fact, to judicial amendment. It is not merely broad construction, but addition of an element not contained in the legislation. The constituents of the offense are enumerated by the statute. If we assume the defendant to have been a person of upright purposes, law abiding, and not prone to crime, — induced against his own will and better judgment to become the instrument of the criminal purpose of another, — his action, so induced, none the less falls within the letter of the law and renders him amenable to its penalties.- Viewed in its true light entrapment is not a defense to him; his act, coupled with his intent to do the act, brings him within the definition of the law; he has no rights or equities by reason of his entrapment. It cannot truly be said that entrapment excuses him or contradicts the obvious fact of his commission of the offense. We cannot escape this conclusion by saying that where need arises the statute will be read as containing an implicit condition that it shall not apply in the case of entrapment. The effect of such construction is to add to the words of the statute a proviso which gives to the defendant a double defense under his plea of not guilty, namely, (a) that what he did does not fall within the definition of the statute, and (b) entrapment. This amounts to saying that one who with full intent commits the act defined by law as an offense, is nevertheless by virtue of the unspoken and implied mandate of the statute to be adjudged not guilty by reason of someone's else improper conduct. It is merely to adopt a form of words to justify action which ought to be based on the inherent right of the court not to be made the instrument of wrong.
 </p>
<p id="b522-5">
  It is said that this case warrants such a construction of the applicable act, but that the question whether a similar
  <span citation-index="1" class="star-pagination" label="457"> 
   *457
   </span>
  construction will be required in the case of other or more serious crimes is not before the court. Thus no guide or rule is announced as to when a statute shall be read as excluding a case of entrapment; and no principle of statutory construction is suggested which would enable us to say that it is excluded by some statutes and not by others.
 </p>
<p id="b523-6">
  The doctrine rests, rather, on a fundamental rule of public policy. The protection of its own functions and the preservation of the purity of its own temple belongs only to the court. It is the province of the court and of the court alone to protect itself and the government from such prostitution of the criminal law. The violation of the principles of justice by the entrapment of the unwary into crime should be dealt with by the court no matter by whom or at what stage of the proceedings the facts are brought to its attention.
  <a class="footnote" href="#fn5" id="fn5_ref">
   5
  </a>
  Quite properly it may discharge the prisoner upon a writ of
  <em>
   habeas
  </em>
  corpus.
  <a class="footnote" href="#fn6" id="fn6_ref">
   6
  </a>
  Equally well may it quash the indictment or entertain and try a plea in bar.6
  <a class="footnote" href="#fn7" id="fn7_ref">
   7
  </a>
  But its powers do not end there. Proof of entrapment, at any stage of the case, requires the court to stop the prosecution, direct that the indictment be quashed, and the defendant set at liberty.
  <a class="footnote" href="#fn8" id="fn8_ref">
   8
  </a>
  If in doubt as to the facts it may submit the issue of entrapment to a jury for advice. But whatever may be the finding upon such submission the power and the duty to act remain with the court and not with the jury.
 </p>
<p id="b524-4">
<span citation-index="1" class="star-pagination" label="458"> 
   *458
   </span>
  Such action does not grant immunity to a guilty defendant. But to afford him as his right a defense founded not on the statute, but on the court’s view of what the legislature is assumed to have meant, is to grant him unwarranted immunity. If the court may construe an act of Congress so as to create a defense for one whose guilt the act pronounces, no reason is apparent why the same statute may not be modified by a similar process of construction as to the penalty prescribed. But it is settled that this may not be done.
  <em>
   Ex parte United States,
  </em>
  <span class="citation" data-id="98794"><a href="/opinion/98794/ex-parte-united-states/" aria-description="Citation for case: Ex Parte United States">242 U. S. 27</a></span>. The broad distinction between the refusal to lend the aid of the court’s own processes to the consummation of a wrong and the attempt to modify by judicial legislation the mandate of the statute as to the punishment to be imposed after trial and conviction is so obvious as not to need discussion.
 </p>
<p id="b524-5">
  Recognition of the defense of entrapment as belonging to the defendant and as raising an issue for decision by the jury called to try him upon plea of the general issue, results in the trial of a false issue wholly outside the true rule which should be applied by the courts. It has been generally held, where the defendant has proved an entrapment, it is permissible for the government to show in rebuttal that the officer guilty of incitement of the crime had reasonable cause to believe the defendant was a person disposed to commit the offense. This procedure is approved by the opinion of the court. The proof received in rebuttal usually amounts to no more than that the defendant had a bad reputation, or that he had been previously convicted. Is the statute upon which the indictment is based to be further construed as removing the defense of entrapment from such a defendant?
 </p>
<p id="b524-6">
  Whatever may be the demerits of the defendant or his previous infractions of law these will not justify the instigation and creation of a new crime, as a means to reach him and punish him for his past misdemeanors. He has committed the crime in question, but, by supposition,
  <span citation-index="1" class="star-pagination" label="459"> 
   *459
   </span>
  only because of instigation and inducement by a government officer. To say that such conduct by an official of government is condoned and rendered innocuous by the fact that the defendant had a bad reputation or had previously transgressed is wholly to disregard the reason for refusing the processes of the court to consummate an abhorrent transaction. It is to discard the basis of the doctrine and in effect to weigh the equities as between the government and the defendant when there are in truth no equities belonging to the latter, and when the rule of action cannot rest on any estimate of the good which may come of the conviction of the offender by foul means. The accepted procedure, in effect, pivots conviction in such cases, not on the commission of the crime charged, but on the prior reputation or some former act or acts of the defendant not mentioned in the indictment.
 </p>
<p id="b525-4">
  The applicable principle is that courts must be closed to the trial of a crime instigated by the government’s own agents. No other issue, no comparison of equities as between the guilty official and the guilty defendant, has any place in the enforcement of this overruling principle of public policy.
 </p>
<p id="b525-5">
  The judgment should be reversed and the cause remanded to the District Court with instructions to quash the indictment and discharge the defendant.
 </p>
<judges id="b525-6">
  Mr. Justice Brandéis and Mr. Justice Stone concur in this opinion.
 </judges>















<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b507-8">
   See, also,
   <em>
    Regina
   </em>
   v.
   <em>
    <span class="citation" data-id="5557787"><a href="/opinion/5707869/williams-v-state/" aria-description="Citation for case: Williams v. State">Williams</a></span>,
   </em>
   1 Car. &amp; K. 195;
   <em>
    People
   </em>
   v.
   <em>
    Mills,
   </em>
   178 N Y. 274; <span class="citation" data-id="3581964"><a href="/opinion/3600589/people-v-mills/" aria-description="Citation for case: People v. . Mills">70 N. E. 786</a></span>;
   <em>
    People
   </em>
   v.
   <em>
    Ficke,
   </em>
   <span class="citation" data-id="3415789"><a href="/opinion/3419370/the-people-v-ficke/" aria-description="Citation for case: The People v. Ficke">343 Ill. 367</a></span>; <span class="citation" data-id="3415789"><a href="/opinion/3419370/the-people-v-ficke/" aria-description="Citation for case: The People v. Ficke">175 N. E. 543</a></span>.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b508-6">
   See note of Francis Wharton to
   <em>
    Bates
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8122456"><a href="/opinion/8160801/bates-v-united-states/" aria-description="Citation for case: Bates v. United States">10 Fed. 97</a></span>-99.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b509-7">
   Compare
   <em>
    Olmstead
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b509-8">
   See, also,
   <em>
    United States
   </em>
   v.
   <em>
    Adams,
   </em>
   <span class="citation" data-id="8848571"><a href="/opinion/8863027/united-states-v-adams/" aria-description="Citation for case: United States v. Adams">59 Fed. 674</a></span>;
   <em>
    Sam Yick
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8802472"><a href="/opinion/8817917/yick-v-united-states/#65" aria-description="Citation for case: Yick v. United States">240 Fed. 60, 65</a></span>;
   <em>
    United States
   </em>
   v.
   <em>
    Echols,
   </em>
   <span class="citation" data-id="8809555"><a href="/opinion/8824775/united-states-v-echols/" aria-description="Citation for case: United States v. Echols">253 Fed. 862</a></span>;
   <em>
    Peterson
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8810455"><a href="/opinion/8825662/peterson-v-united-states/" aria-description="Citation for case: Peterson v. United States">255 Fed. 433</a></span>;
   <em>
    Billingsley
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8821314"><a href="/opinion/8836257/billingsley-v-united-states/#89" aria-description="Citation for case: Billingsley v. United States">274 Fed. 86, 89</a></span>;
   <em>
    Luterman
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8826008"><a href="/opinion/8840847/luterman-v-united-states/#377" aria-description="Citation for case: Luterman v. United States">281 Fed. 374, 377</a></span>;
   <em>
    United States
   </em>
   v.
   <em>
    Pappagoda,
   </em>
   <span class="citation" data-id="8829885"><a href="/opinion/8844647/united-states-v-pappagoda/" aria-description="Citation for case: United States v. Pappagoda">288 Fed. 214</a></span>;
   <em>
    Ritter
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="8832845"><a href="/opinion/8847543/ritter-v-united-states/" aria-description="Citation for case: Ritter v. United States">293 Fed. 187</a></span>;
   <em>
    Di Salvo
   </em>
   v.
   <em>
    United States,
   </em>
   2 F. (2d) 222;
   <em>
    Silk
   </em>
   v.
   <span citation-index="1" class="star-pagination" label="444"> 
    *444
    </span>
<em>
    United States,
   </em>
   16 F. (2d) 568;
   <em>
    Jarl
   </em>
   v.
   <em>
    United States,
   </em>
   19 F. (2d) 891;
   <em>
    Corcoran
   </em>
   v.
   <em>
    United States,
   </em>
   19 F. (2d) 901;
   <em>
    United States
   </em>
   v.
   <em>
    Washington,
   </em>
   20 F. (2d) 160;
   <em>
    Cline
   </em>
   v.
   <em>
    United States,
   </em>
   20 F. (2d) 494;
   <em>
    United States ex rel. Hassel
   </em>
   v.
   <em>
    Mathues,
   </em>
   22 F. (2d) 979;
   <em>
    Driskill
   </em>
   v.
   <em>
    United States,
   </em>
   24 F. (2d) 525;
   <em>
    Ybor
   </em>
   v.
   <em>
    United States,
   </em>
   31 F. (2d) 42;
   <em>
    Robinson
   </em>
   v.
   <em>
    United States,
   </em>
   32 F. (2d) 505;
   <em>
    Vaccaro
   </em>
   v.
   <em>
    Collier,
   </em>
   38 F. (2d) 862;
   <em>
    Patton
   </em>
   v.
   <em>
    United States,
   </em>
   42 F. (2d) 68; and cases collected in note in
   <em>
    O’Brien
   </em>
   v.
   <em>
    United States,
   </em>
   51 F. (2d) 674, 678, including decisions of state courts. Compare
   <em>
    Rex
   </em>
   v.
   <em>
    Titley,
   </em>
   14 Cox C. C. 502;
   <em>
    Blaikie
   </em>
   v.
   <em>
    Linton,
   </em>
   18 Scottish Law Rep. 583; London Law Times, July 30, 1881, p. 223;
   <em>
    People
   </em>
   v.
   <em>
    Mills,
   </em>
   <span class="citation" data-id="3581964"><a href="/opinion/3600589/people-v-mills/" aria-description="Citation for case: People v. . Mills">178 N. Y. 274</a></span>; <span class="citation" data-id="3581964"><a href="/opinion/3600589/people-v-mills/" aria-description="Citation for case: People v. . Mills">70 N. E. 786</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Smith,
   </em>
   <span class="citation" data-id="3673731"><a href="/opinion/3927128/state-v-smith/" aria-description="Citation for case: State v. . Smith">152 N. C. 798</a></span>; <span class="citation" data-id="3673731"><a href="/opinion/3927128/state-v-smith/" aria-description="Citation for case: State v. . Smith">67 S. E. 508</a></span>;
   <em>
    Bauer
   </em>
   v.
   <em>
    Commonwealth,
   </em>
   <span class="citation" data-id="6815072"><a href="/opinion/6919457/bauer-v-commonwealth/" aria-description="Citation for case: Bauer v. Commonwealth">135 Va. 463</a></span>; <span class="citation" data-id="6815072"><a href="/opinion/6919457/bauer-v-commonwealth/" aria-description="Citation for case: Bauer v. Commonwealth">115 S. E. 514</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Gibbs,
   </em>
   <span class="citation" data-id="7975122"><a href="/opinion/8019675/state-v-gibbs/" aria-description="Citation for case: State v. Gibbs">109 Minn. 247</a></span>; <span class="citation" data-id="7975122"><a href="/opinion/8019675/state-v-gibbs/" aria-description="Citation for case: State v. Gibbs">123 N. W. 810</a></span>;
   <em>
    State
   </em>
   v.
   <em>
    Rippey,
   </em>
   127 S. C. 550; <span class="citation" data-id="3884966"><a href="/opinion/4123323/state-v-rippey/" aria-description="Citation for case: State v. Rippey">122 S. E. 397</a></span>. See, also, 18 A. L. R. Ann. 146; 28 Col. L. Rev. 1067; <span class="citation no-link">44 Harv. L. Rev. 109</span>; 2 So. Cal. L. Rev. 283 ; 41 Yale L. J. 1249; <span class="citation no-link">10 Va. L. Rev. 316</span>; <span class="citation no-link">9 Tex. L. Rev. 276</span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b510-6">
   See cases cited in note 4.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b512-7">
   See
   <em>
    Chicago B. &amp; Q. R. Co.
   </em>
   v.
   <em>
    McGuire,
   </em>
   <span class="citation" data-id="97368"><a href="/opinion/97368/chicago-burlington-quincy-railroad-v-mcguire/#565" aria-description="Citation for case: Chicago, Burlington &amp; Quincy Railroad v. McGuire">219 U. S. 549, 565</a></span>;
   <em>
    Green
   </em>
   v.
   <em>
    Frazier,
   </em>
   <span class="citation" data-id="99608"><a href="/opinion/99608/green-v-frazier/#240" aria-description="Citation for case: Green v. Frazier">253 U. S. 233, 240</a></span>.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b514-7">
   In
   <em>
    Hawaii
   </em>
   v.
   <em>
    Mankichi,
   </em>
   <span class="citation" data-id="9417915"><a href="/opinion/95894/hawaii-v-mankichi/#214" aria-description="Citation for case: Hawaii v. Mankichi">190 U. S. 197, 214</a></span>, the Court referred with approval to the following language of the Master of the Rolls (after-wards Lord Esher) in
   <em>
    Plumstead Board of Works
   </em>
   v.
   <em>
    Spackman,
   </em>
   L. R.
   <em>
    13 Q. B.
   </em>
   D. 878, 887: “If there are no means of avoiding such an interpretation of the statute,” (as will amount to a great hardship,) “ a judge must come to the conclusion that the legislature by inadvertence haa committed an act of legislative injustice; but to my mind a judge ought to struggle with all the intellect that he has, and with all the vigor of mind that he has, against such an interpretation of an act of Parliament; and, unless he is forced to come to a contrary conclusion, he ought to assume that it is impossible that the legislature could have so intended.”
  </p>
</div><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b519-8">
   See
   <em>
    O’Brien
   </em>
   v.
   <em>
    United States,
   </em>
   51 F. (2d) 674, footnote 1, p. 678.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b520-7">
   Compare
   <em>
    Olmstead
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>.
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b520-8">
<em>
    Casey
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="9418615"><a href="/opinion/101251/casey-v-united-states/" aria-description="Citation for case: Casey v. United States">276 U. S. 413</a></span>.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b521-8">
   See
   <em>
    Hannay
   </em>
   v.
   <em>
    Eve,
   </em>
   <span class="citation" data-id="84810"><a href="/opinion/84810/hannay-v-eve/#247" aria-description="Citation for case: Hannay v. Eve">3 Cranch 242, 247</a></span>;
   <em>
    Bank of United States
   </em>
   v.
   <em>
    Owens,
   </em>
   <span class="citation" data-id="85646"><a href="/opinion/85646/president-of-the-bank-of-the-united-states-v-owens/#538" aria-description="Citation for case: President of the Bank of the United States v. Owens">2 Pet. 527, 538</a></span>;
   <em>
    Bartle
   </em>
   v.
   <em>
    Nutt,
   </em>
   <span class="citation" data-id="85698"><a href="/opinion/85698/bartle-v-nutt/#188" aria-description="Citation for case: Bartle v. Nutt">4 Pet. 184, 188</a></span>;
   <em>
    Hanauer
   </em>
   v.
   <em>
    Doane,
   </em>
   <span class="citation" data-id="88397"><a href="/opinion/88397/hanauer-v-doane/#349" aria-description="Citation for case: Hanauer v. Doane">12 Wall. 342, 349</a></span>;
   <em>
    Trist
   </em>
   v.
   <em>
    Child,
   </em>
   <span class="citation" data-id="89027"><a href="/opinion/89027/trist-v-child/#448" aria-description="Citation for case: Trist v. Child">21 Wall. 441, 448</a></span>;
   <em>
    Hazelton
   </em>
   v.
   <em>
    Sheckells,
   </em>
   <span class="citation" data-id="96460"><a href="/opinion/96460/hazelton-v-sheckells/" aria-description="Citation for case: Hazelton v. Sheckells">202 U. S. 71</a></span>;
   <em>
    Crocker
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="98638"><a href="/opinion/98638/crocker-v-united-states/#78" aria-description="Citation for case: Crocker v. United States">240 U. S. 74, 78</a></span>.
  </p>
</div><div class="footnote" id="fn5" label="5">
<a class="footnote" href="#fn5_ref">
   5
  </a>
<p id="b523-7">
   Compare
   <em>
    Gambino
   </em>
   v.
   <em>
    United States,
   </em>
   <span class="citation" data-id="101180"><a href="/opinion/101180/gambino-v-united-states/#319" aria-description="Citation for case: Gambino v. United States">275 U. S. 310, 319</a></span>.
  </p>
</div><div class="footnote" id="fn6" label="6">
<a class="footnote" href="#fn6_ref">
   6
  </a>
<p id="b523-8">
   See
   <em>
    United States ex rel. Hassell
   </em>
   v.
   <em>
    Mathues,
   </em>
   22 F. (2d) 979.
  </p>
</div><div class="footnote" id="fn7" label="7">
<a class="footnote" href="#fn7_ref">
   7
  </a>
<p id="b523-9">
   Compare
   <em>
    United States
   </em>
   v.
   <em>
    Pappagoda,
   </em>
   <span class="citation" data-id="8829885"><a href="/opinion/8844647/united-states-v-pappagoda/" aria-description="Citation for case: United States v. Pappagoda">288 Fed. 214</a></span>;
   <em>
    Spring Drug Co.
   </em>
   v.
   <em>
    United States,
   </em>
   12 F. (2d) 852.
  </p>
</div><div class="footnote" id="fn8" label="8">
<a class="footnote" href="#fn8_ref">
   8
  </a>
<p id="b523-10">
   In
   <em>
    United States
   </em>
   v.
   <em>
    Echols,
   </em>
   <span class="citation" data-id="8809555"><a href="/opinion/8824775/united-states-v-echols/" aria-description="Citation for case: United States v. Echols">253 Fed. 862</a></span>, upon the tender of a plea of guilty, the court of its own motion examined the prisoner and the officers concerned in his arrest; and being satisfied that these officers had instigated the crime, declared that public policy required that the plea be refused and the case dismissed. In
   <em>
    United States
   </em>
   v.
   <em>
    Healy,
   </em>
   <span class="citation" data-id="8786735"><a href="/opinion/8802548/united-states-v-healy/" aria-description="Citation for case: United States v. Healy">202 Fed. 349</a></span>, a judgment and sentence were set aside and the defendant discharged upon the court’s ascertaining that the conviction was procured by entrapment.
  </p>
</div></div></opinion>
```

---

## GROUP: _overhaul2/lake/cases/South Dakota v. Neville.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: South Dakota v. Neville
type: case
citation: "459 U.S. 553 (1983)"
parallel_cite: "103 S. Ct. 916; 74 L. Ed. 2d 748; 51 U.S.L.W. 4148"
neutral_cite: 1983 U.S. LEXIS 129
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1983
date_decided: 1983-02-22
docket: No. 81-1453
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
  opinion_url: "https://www.courtlistener.com/opinion/110832/south-dakota-v-neville/"
  cluster_id: 110832
  opinion_id: null
  identity_checked: true
lake:
  record_id: South Dakota v. Neville
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Confessions, Interrogation & the Fifth Amendment]]"
    role: Anchor
related:
  - "[[Schmerber v. California]]"
tags:
  - case
  - fifth-amendment
  - self-incrimination
  - blood-alcohol-test
  - implied-consent
  - due-process
  - dwi
holding: "Admitting into evidence a drunk-driving suspect's refusal to submit to a blood-alcohol test does not violate the Fifth Amendment privilege against self-incrimination, because a refusal — offered as a choice by police after a lawful request — is not an act coerced by the officer; nor does admitting the refusal offend due process even though the officer did not warn the suspect that his refusal could be used against him at trial."
aliases:
  - South Dakota v. Neville
  - "South Dakota v. Neville (1983)"
---

# South Dakota v. Neville

*459 U.S. 553 (1983)* (No. 81-1453) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 110832 → combined opinion 110832 (O'Connor, J.; 459 U.S. 553, argued Dec. 8, 1982, decided Feb. 22, 1983). Rule quote string-matched to the CL opinion text 2026-07-07 (reporter star `*564`). S9 promotes. -->

## Background
Two Madison, South Dakota, officers stopped Neville for running a stop sign. He staggered getting out of the car, smelled of alcohol, had no license (revoked after a prior DWI), and failed field sobriety tests. After his arrest and *[[Miranda v. Arizona|Miranda]]* warnings, the officers asked him to submit to a blood-alcohol test and warned that he could lose his license if he refused. Neville refused, saying he was too drunk to pass the test, and refused again at the station. South Dakota law made a refusal admissible at trial, but Neville moved to suppress evidence of his refusal, and the South Dakota courts suppressed it as a violation of the privilege against self-incrimination.

## Issue
Whether admitting a suspect's refusal to take a blood-alcohol test violates the Fifth Amendment privilege against self-incrimination, and whether admitting the refusal denies due process when the officer did not warn that the refusal could be used against him.

## Rule
Building on *[[Schmerber v. California|Schmerber]]* (which allowed a State to compel a blood test itself), the Court reasoned that the privilege bars only *compelled* self-incrimination, and that offering a suspect the choice to take the test or have his refusal used against him is not the kind of coercion the Fifth Amendment forbids. It held: "We hold, therefore, that a refusal to take a blood-alcohol test, after a police officer has lawfully requested it, is not an act coerced by the officer, and thus is not protected by the privilege against self-incrimination." — 459 U.S. at 564. ^pin-564

## Application
Because the State could constitutionally have compelled the test outright, offering the milder alternative of refusal (with attendant penalties) was no less legitimate; the choice, though unpleasant, was not the "cruel trilemma" the privilege guards against. On the separate due-process question, the Court distinguished *[[Doyle v. Ohio]]*: the officer's warning that refusal could cost Neville his license carried no implicit assurance that the refusal would not be used against him at trial, so it was not fundamentally unfair to admit the refusal even absent an express warning.

## Conclusion
The judgment of the Supreme Court of South Dakota was **reversed** and the case [[Reading and Citing Cases#on-remand|remanded]]. O'Connor, J., delivered the opinion of the Court. Stevens, J., filed a [[Common Legal Terms#dissenting-opinion|dissenting opinion]], in which Marshall, J., joined.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Neville* is an anchor for the boundary of the Fifth Amendment privilege in the DWI context: a test refusal is not compelled testimony, so its admission is neither self-incrimination nor a due-process violation. Teach it with *[[Schmerber v. California]]* (compelled blood tests and the physical-evidence/testimony line) as the pair marking what the privilege does and does not reach when the State seeks blood-alcohol evidence.

## Appears on
- [[Confessions, Interrogation & the Fifth Amendment]] — *Anchor*

## Sources
- [*South Dakota v. Neville*, 459 U.S. 553 (1983)](https://www.courtlistener.com/opinion/110832/south-dakota-v-neville/) — pinpoint: 564 (O'Connor, J., for the Court; the CL opinion text places the quoted holding just after the reporter star `*564`, i.e., on page 564). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "28f98d65591c64ba", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "South Dakota v. Neville"}, "payload": {"all": [{"cite": "459 U.S. 553", "page": "553", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "459"}, {"cite": "103 S. Ct. 916", "page": "916", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "74 L. Ed. 2d 748", "page": "748", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "74"}, {"cite": "1983 U.S. LEXIS 129", "page": "129", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1983"}, {"cite": "51 U.S.L.W. 4148", "page": "4148", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "51"}], "display": "459 U.S. 553", "official": {"cite": "459 U.S. 553", "page": "553", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "459"}, "official_selection_present": true, "record_id": "South Dakota v. Neville"}}
{"assertion_id": "ad8585d109eb73c6", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "South Dakota v. Neville"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "South Dakota v. Neville", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — South Dakota v. Neville

```json
{
  "schema_version": "s2.v1",
  "record_id": "South Dakota v. Neville",
  "status": "under_review",
  "identity": {
    "case_name": "South Dakota v. Neville",
    "case_name_short": "Neville",
    "case_name_full": "South Dakota v. Neville",
    "input_case_name": "South Dakota v. Neville",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1983-02-22",
    "year": 1983,
    "docket": "No. 81-1453",
    "cluster_id": 110832,
    "lead_opinion_id": 9429007,
    "sibling_ids": [],
    "absolute_url": "/opinion/110832/south-dakota-v-neville/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "459 U.S. 553",
      "volume": "459",
      "reporter": "U.S.",
      "page": "553",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "103 S. Ct. 916",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "916",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "74 L. Ed. 2d 748",
        "volume": "74",
        "reporter": "L. Ed. 2d",
        "page": "748",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4148",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4148",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1983 U.S. LEXIS 129",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "459 U.S. 553",
        "volume": "459",
        "reporter": "U.S.",
        "page": "553",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 S. Ct. 916",
        "volume": "103",
        "reporter": "S. Ct.",
        "page": "916",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "74 L. Ed. 2d 748",
        "volume": "74",
        "reporter": "L. Ed. 2d",
        "page": "748",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1983 U.S. LEXIS 129",
        "volume": "1983",
        "reporter": "U.S. LEXIS",
        "page": "129",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 U.S.L.W. 4148",
        "volume": "51",
        "reporter": "U.S.L.W.",
        "page": "4148",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "459 U.S. 553",
    "official_selection": {
      "court_class": "scotus",
      "selected": "459 U.S. 553",
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
    "date_created": "2026-07-06T13:44:52Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:45:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "south-dakota-v-neville--110832",
      "to_record_id": "South Dakota v. Neville",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — South Dakota v. Neville

```
<opinion type="majority">
<author id="b714-6">Justice O’Connor</author>
<p id="A6k">delivered the opinion of the Court.</p>
<p id="b714-7"><em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), held that a State could force a defendant to submit to a blood-alcohol test without violating the defendant’s Fifth Amendment right against self-incrimination. We now address a question left open in <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California"><em>Schmerber, supra, </em>at 765, n. 9</a></span>, and hold that the admission into evidence of a defendant’s refusal to submit to such a test likewise does not offend the right against self-incrimination.</p>
<p id="b714-8">I</p>
<p id="b714-9">Two Madison, South Dakota, police officers stopped respondent’s car after they saw him fail to stop at a stop sign. The officers asked respondent for his driver’s license and asked him to get out of the car. As he left the car, respondent staggered and fell against the car to support himself. <page-number citation-index="1" label="555">*555</page-number>The officers smelled alcohol on his breath. Respondent did not have a driver’s license, and informed the officers that it was revoked after a previous driving-while-intoxicated conviction. The officers asked respondent to touch his finger to his nose and to walk a straight line. When respondent failed these field sobriety tests, he was placed under arrest and read his <em>Miranda </em>rights.<footnotemark>1</footnotemark> Respondent acknowledged that he understood his rights and agreed to talk without a lawyer present. App. 11. Reading from a printed card, the officers then asked respondent to submit to a blood-alcohol test and warned him that he could lose his license if he refused.<footnotemark>2</footnotemark> Respondent refused to take the test, stating “I’m too drunk, I won’t pass the test.” The officers again read the request to <page-number citation-index="1" label="556">*556</page-number>submit to a test, and then took respondent to the police station, where they read the request to submit a third time. Respondent continued to refuse to take the test, again saying he was too drunk to pass it.<footnotemark>3</footnotemark></p>
<p id="b716-5">South Dakota law specifically declares that refusal to submit to a blood-alcohol test “may be admissible into evidence at the trial.” S. D. Comp. Laws Ann. §32-23-10.1 (Supp. 1982).<footnotemark>4</footnotemark> Nevertheless, respondent sought to suppress all evidence of his refusal to take the blood-alcohol test. The Circuit Court granted the suppression motion for three reasons: the South Dakota statute allowing evidence of refusal violated respondent’s federal constitutional rights; the officers failed to advise respondent that the refusal could be used against him at trial; and the refusal was irrelevant to the issues before the court. The State appealed from the entire order. The South Dakota Supreme Court affirmed the suppression of the act of refusal on the grounds that § 32-23-10.1, which allows the introduction of this evidence, violated the federal and state privilege against self-incrimination.<footnotemark>5</footnotemark> <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/" aria-description="Citation for case: State v. Neville">312 N. W. 2d 723</a></span> (1981). The court reasoned that <page-number citation-index="1" label="557">*557</page-number>the refusal was a communicative act involving respondent’s testimonial capacities and that the State compelled this communication by forcing respondent “‘to choose between submitting to a perhaps unpleasant examination and producing <page-number citation-index="1" label="558">*558</page-number>testimonial evidence against himself,’” <em><span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/" aria-description="Citation for case: State v. Neville">id.,</a></span> </em>at 726 (quoting <em>State </em>v. <em>Andrews, </em><span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/#262" aria-description="Citation for case: State v. Andrews">297 Minn. 260, 262</a></span>, <span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/#864" aria-description="Citation for case: State v. Andrews">212 N. W. 2d 863, 864</a></span> (1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/881/">419 U. S. 881</a></span> (1974)).<footnotemark>6</footnotemark></p>
<p id="b718-8">Since other jurisdictions have found no Fifth Amendment violation from the admission of evidence of refusal to submit to blood-alcohol tests,<footnotemark>7</footnotemark> we granted certiorari to resolve the conflict. <span class="citation multiple-matches"><a href="/c/U.%20S./456/971/">456 U. S. 971</a></span> (1982).</p>
<p id="b718-9">HH hH</p>
<p id="b718-3">The situation underlying this case — that of the drunk driver — occurs with tragic frequency on our Nation’s highways. The carnage caused by drunk drivers is well documented and needs no detailed recitation here. This Court, although not having the daily contact with the problem that the state courts have, has repeatedly lamented the tragedy. See <em>Breithaupt </em>v. <em>Abram, </em><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/#439" aria-description="Citation for case: Breithaupt v. Abram">352 U. S. 432, 439</a></span> (1957) (“The increasing slaughter on our highways, most of which should be avoidable, now reaches the astounding figures only heard of on the battlefield”); <em>Tate </em>v. <em>Short, </em><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/#401" aria-description="Citation for case: Tate v. Short">401 U. S. 395, 401</a></span> (1971) (Blackmun, J., concurring) (deploring “traffic irresponsibility and the frightful carnage it spews upon our highways”); <em>Perez </em>v. <em>Campbell, </em><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/#657" aria-description="Citation for case: Perez. v. Campbell">402 U. S. 637, 657, 672</a></span> (1971) (Blackmun, J., concurring) (footnote omitted) (“The slaughter on the highways of this Nation exceeds the death toll of all our <page-number citation-index="1" label="559">*559</page-number>wars”); <em>Mackey </em>v. <em>Montrym, </em><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/#17" aria-description="Citation for case: MacKey v. Montrym">443 U. S. 1, 17-19</a></span> (1979) (recognizing the “compelling interest in highway safety”).</p>
<p id="b719-5">As part of its program to deter drinkers from driving, South Dakota has enacted an “implied consent” law. S. D. Comp. Laws Ann. § 32-23-10 (Supp. 1982). This statute declares that any person operating a vehicle in South Dakota is deemed to have consented to a chemical test of the alcoholic content of his blood if arrested for driving while intoxicated. In <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), this Court upheld a state-compelled blood test against a claim that it infringed the Fifth Amendment right against self-incrimination, made applicable to the States through the Fourteenth Amendment.<footnotemark>8</footnotemark> We recognized- that a coerced blood test infringed to some degree the “inviolability of the human personality” and the “requirement that the State procure the evidence against an accused ‘by its own independent labors,’ ” but noted the privilege has never been given the full scope suggested by the values it helps to protect. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#762" aria-description="Citation for case: Schmerber v. California">Id., at 762</a></span>. We therefore held that the privilege bars the State only from compelling “communications” or “testimony.” Since a blood test was “physical or real” evidence rather than testimonial evidence, we found it unprotected by the Fifth Amendment privilege.</p>
<p id="b719-6"><em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>then, clearly allows a State to force a person suspected of driving while intoxicated to submit to a blood-alcohol test.<footnotemark>9</footnotemark> South Dakota, however, has declined to authorize its police officers to administer a blood-alcohol test against the suspect’s will. Rather, to avoid violent confrontations, the South Dakota statute permits a suspect to <page-number citation-index="1" label="560">*560</page-number>refuse the test, and indeed requires police officers to inform the suspect of his right to refuse. S. D. Comp. Laws Ann. § 32-23-10 (Supp. 1982). This permission is not without a price, however. South Dakota law authorizes the Department of Public Safety, after providing the person who has refused the test an opportunity for a hearing, to revoke for one year both the person’s license to drive and any nonresident operating privileges he may possess. § 32-23-11. Such a penalty for refusing to take a blood-alcohol test is unquestionably legitimate, assuming appropriate procedural protections. See <em>Mackey </em>v. <em><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">Montrym, supra.</a></span></em></p>
<p id="b720-5">South Dakota further discourages the choice of refusal by allowing the refusal to be used against the defendant at trial. S. D. Comp. Laws. Ann. §§32-23-10.1 and 19-13-28.1 (Supp. 1982). <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>expressly reserved the question of whether evidence of refusal violated the privilege against self-incrimination. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California">384 U. S., at 765, n. 9</a></span>. The Court did indicate that general Fifth Amendment principles, rather than the particular holding of <em>Griffin </em>v. <em>California, </em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">380 U. S. 609</a></span> (1965), should control the inquiry. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#766" aria-description="Citation for case: Schmerber v. California">384 U. S., at 766, n. 9</a></span>.<footnotemark>10</footnotemark></p>
<p id="b720-6">Most courts applying general Fifth Amendment principles to the refusal to take a blood test have found no violation of the privilege against self-incrimination. Many courts, following the lead of Justice Traynor’s opinion for the California Supreme Court in <em>People </em>v. <em>Sudduth, </em><span class="citation" data-id="1390455"><a href="/opinion/1390455/people-v-sudduth/" aria-description="Citation for case: People v. Sudduth">65 Cal. 2d 543</a></span>, <span class="citation" data-id="1390455"><a href="/opinion/1390455/people-v-sudduth/" aria-description="Citation for case: People v. Sudduth">421 P. 2d 401</a></span> (1966), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./389/850/">389 U. S. 850</a></span> (1967), have reasoned that refusal to submit is a physical act rather than a communication and for this reason is not protected by the <page-number citation-index="1" label="561">*561</page-number>privilege.<footnotemark>11</footnotemark> As Justice Traynor explained more fully in the companion case of <em>People </em>v. <em>Ellis, </em><span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/" aria-description="Citation for case: People v. Ellis">65 Cal. 2d 529</a></span>, <span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/" aria-description="Citation for case: People v. Ellis">421 P. 2d 393</a></span> (1966) (refusal to display voice not testimonial), evidence of refusal to take a potentially incriminating test is similar to other circumstantial evidence of consciousness of guilt, such as escape from custody and suppression of evidence. The court below, relying on <em>Dudley </em>v. <em>State, </em><span class="citation" data-id="9641061"><a href="/opinion/1497914/dudley-v-state/" aria-description="Citation for case: Dudley v. State">548 S. W. 2d 706</a></span> (Tex. Crim. App. 1977), and <em>State </em>v. <em>Andrews, </em><span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/" aria-description="Citation for case: State v. Andrews">297 Minn. 260</a></span>, <span class="citation" data-id="9742543"><a href="/opinion/2231866/state-v-andrews/" aria-description="Citation for case: State v. Andrews">212 N. W. 2d 863</a></span> (1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/881/">419 U. S. 881</a></span> (1974), rejected this view. This minority view emphasizes that the refusal is “a tacit or overt expression and communication of defendant’s thoughts,” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#726" aria-description="Citation for case: State v. Neville">312 N. W. 2d, at 726</a></span>, and that the Constitution “simply forbids any compulsory revealing or communication of an accused person’s thoughts or mental processes, whether it is by acts, failure to act, words spoken or failure to speak.” <span class="citation" data-id="9641061"><a href="/opinion/1497914/dudley-v-state/#708" aria-description="Citation for case: Dudley v. State"><em>Dudley, supra, </em>at 708</a></span>.</p>
<p id="b721-5">While we find considerable force in the analogies to flight and suppression of evidence suggested by Justice Traynor, we decline to rest our decision on this ground. As we recognized in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>, </em>the distinction between real or physical evidence, on the one hand, and communications or testimony, on the other, is not readily drawn in many cases. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California">384 U. S., at 764</a></span>.<footnotemark>12</footnotemark> The situations arising from a refusal present a diffi<page-number citation-index="1" label="562">*562</page-number>cult gradation from a person who indicates refusal by complete inaction, to one who nods his head negatively, to one who states “I refuse to take the test,” to the respondent here, who stated “I’m too drunk, I won’t pass the test.” Since no impermissible coercion is involved when the suspect refuses to submit to take the test, regardless of the form of refusal, we prefer to rest our decision on this ground, and draw possible distinctions when necessary for decision in other circumstances.<footnotemark>13</footnotemark></p>
<p id="b722-5">As we stated in <em>Fisher </em>v. <em>United States, </em><span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/#397" aria-description="Citation for case: Fisher v. United States">425 U. S. 391, 397</a></span> (1976), “[t]he Court has held repeatedly that the Fifth Amendment is limited to prohibiting the use of ‘physical or moral compulsion’ exerted on the person asserting the privilege.” This coercion requirement comes directly from the constitutional language directing that no person “shall be <em>compelled </em>in any criminal case to be a witness against himself.” U. S. Const., Arndt. 5 (emphasis added). And as Professor Levy concluded in his history of the privilege, “[t]he element of compulsion or involuntariness was always an ingredient of the right and, before the right existed, of protests against incriminating interrogatories.” L. Levy, Origins of the Fifth Amendment 328 (1968).</p>
<p id="b722-6">Here, the State did not directly compel respondent to refuse the test, for it gave him the choice of submitting to the test or refusing. Of course, the fact the government gives a defendant or suspect a “choice” does not always resolve the <page-number citation-index="1" label="563">*563</page-number>compulsion inquiry. The classic Fifth Amendment violation — telling a defendant at trial to testify — does not, under an extreme view, compel the defendant to incriminate himself. He could submit to self-accusation, or testify falsely (risking perjury) or decline to testify (risking contempt). But the Court has long recognized that the Fifth Amendment prevents the State from forcing the choice of this “cruel trilemma” on the defendant. See <em>Murphy </em>v. <em>Waterfront Comm’n, </em><span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964). See also <em>New Jersey </em>v. <em>Portash, </em><span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 459</a></span> (1979) (telling a witness under a grant of legislative immunity to testify or face contempt sanctions is “the essence of coerced testimony”). Similarly, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>cautioned that the Fifth Amendment may bar the use of testimony obtained when the proffered alternative was to submit to a test so painful, dangerous, or severe, or so violative of religious beliefs, that almost inevitably a person would prefer “confession.” <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California">384 U. S., at 765, n. 9</a></span>.<footnotemark>14</footnotemark> Cf. <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 458</a></span> (1966) (unless compulsion inherent in custodial surroundings is dispelled, no statement is truly a product of free choice).</p>
<p id="b723-4">In contrast to these prohibited choices, the values behind the Fifth Amendment are not hindered when the State offers a suspect the choice of submitting to the blood-alcohol test or having his refusal used against him. The simple blood-alcohol test is so safe, painless, and commonplace, see <em>Schmerber, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#771" aria-description="Citation for case: Schmerber v. California">384 U. S., at 771</a></span>, that respondent concedes, as he must, that the State could legitimately compel the suspect, against his will, to accede to the test. Given, then, that the offer of taking a blood-alcohol test is clearly legitimate, the action becomes no <em>less </em>legitimate when the State offers a second option of refusing the test, with the attendant penalties for making that choice. Nor is this a case where the State has subtly coerced respondent into choosing the option it had no right to compel, rather than offering a true <page-number citation-index="1" label="564">*564</page-number>choice. To the contrary, the State wants respondent to choose to take the test, for the inference of intoxication arising from a positive blood-alcohol test is far stronger than that arising from a refusal to take the test.</p>
<p id="b724-4">We recognize, of course, that the choice to submit or refuse to take a blood-alcohol test will not be an easy or pleasant one for a suspect to make. But the criminal process often requires suspects and defendants to make difficult choices. See, <em>e. g., Crampton </em>v. <em>Ohio, </em>decided with <em>McGautha </em>v. <em>California, </em><span class="citation" data-id="9424551"><a href="/opinion/108329/mcgautha-v-california/#213" aria-description="Citation for case: McGautha v. California">402 U. S. 183, 213-217</a></span> (1971). We hold, therefore, that a refusal to take a blood-alcohol test, after a police officer has lawfully requested it, is not an act coerced by the officer, and thus is not protected by the privilege against self-incrimination.<footnotemark>15</footnotemark></p>
<p id="b724-5">III</p>
<p id="b724-6">Relying on <em>Doyle </em>v. <em>Ohio, </em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">426 U. S. 610</a></span> (1976), respondent also suggests that admission at trial of his refusal violates the Due Process Clause because respondent was not fully warned of the consequences of refusal. <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span> </em>held that the Due Process Clause prohibits a prosecutor from using a defendant’s silence after <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings to impeach his testimony at trial. Just a Term before, in <em>United States </em>v. <em>Hale, </em><span class="citation" data-id="9426137"><a href="/opinion/109289/united-states-v-hale/" aria-description="Citation for case: United States v. Hale">422 U. S. 171</a></span> (1975), we had determined under our supervisory power that the federal courts could not use such silence for impeachment because of its dubious probative value. Al<page-number citation-index="1" label="565">*565</page-number>though <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span> </em>mentioned this rationale in applying the rule to the States, <span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/#617" aria-description="Citation for case: Doyle v. Ohio">426 U. S., at 617</a></span>, the Court relied on the fundamental unfairness of implicitly assuring a suspect that his silence will not be used against him and then using his silence to impeach an explanation subsequently offered at trial. <span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/#618" aria-description="Citation for case: Doyle v. Ohio"><em>Id., </em>at 618</a></span>.</p>
<p id="b725-5">Unlike the situation in <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span>, </em>we do not think it fundamentally unfair for South Dakota to use the refusal to take the test as evidence of guilt, even though respondent was not specifically warned that his refusal could be used against him at trial. First, the right to silence underlying the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings is one of constitutional dimension, and thus cannot be unduly burdened. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona"><em>Miranda, supra, </em>at 468, n. 37</a></span>. Cf. <em>Fletcher </em>v. <em>Weir, </em><span class="citation" data-id="110668"><a href="/opinion/110668/fletcher-v-weir/" aria-description="Citation for case: Fletcher v. Weir">455 U. S. 603</a></span> (1982) (postarrest silence without <em>Miranda </em>warnings may be used to impeach trial testimony). Respondent’s right to refuse the blood-alcohol test, by contrast, is simply a matter of grace bestowed by the South Dakota Legislature.</p>
<p id="b725-6">Moreover, the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings emphasize the dangers of choosing to speak (“whatever you say can and will be used as evidence against you in court”), but give no warning of adverse consequences from choosing to remain silent. This imbalance in the delivery of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, we recognized in <em><span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/" aria-description="Citation for case: Doyle v. Ohio">Doyle</a></span>, </em>implicitly assures the suspect that his silence will not be used against him. The warnings challenged here, by contrast, contained no such misleading implicit assurances as to the relative consequences of his choice. The officers explained that, if respondent chose to submit to the test, he had the right to know the results- and could choose to take an additional test by a person chosen by him. The officers did not specifically warn respondent that the test results could be used against him at trial.<footnotemark>16</footnotemark> Explaining the consequences of <page-number citation-index="1" label="566">*566</page-number>the other option, the officers specifically warned respondent that failure to take the test could lead to loss of driving privileges for one year. It is true the officers did not inform respondent of the further consequence that evidence of refusal could be used against him in court,<footnotemark>17</footnotemark> but we think it unrealistic to say that the warnings given here implicitly assure a suspect that no consequences other than those mentioned will occur. Importantly, the warning that he could lose his driver’s license made it clear that refusing the test was not a “safe harbor,” free of adverse consequences.</p>
<p id="b726-5">While the State did not actually warn respondent that the test results could be used against him, we hold that such a failure to warn was not the sort of implicit promise to forgo use of evidence that would unfairly “trick” respondent if the evidence were later offered against him at trial. We therefore conclude that the use of evidence of refusal after these warnings comported with the fundamental fairness required by due process.</p>
<p id="b726-6">IV</p>
<p id="b726-7">The judgment of the South Dakota Supreme Court is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="b726-8">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b715-5"> The officer read the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warning from a printed card. He read: “You have the right to remain silent. You don’t have to talk to me unless you want to do so. If you want to talk to me I must advise you whatever you say can and will be used as evidence against you in court. You have the right to confer with a lawyer, and to have a lawyer present with you while you’re being questioned. If you want a lawyer but are unable to pay for one, a lawyer will be appointed to represent you free of any cost to you. Knowing these rights, do you want to talk to me without having a lawyer present? You may stop talking to me at any time. You may also demand a lawyer at any time.” App. 8. See <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467-473</a></span> (1966).</p>
</footnote>
<footnote label="2">
<p id="b715-6"> The card read: “I have arrested you for driving or being in actual physical control of a vehicle while under the influence of alcohol or drugs, a violation of S. D. C. L. 32-23-1. I request that you submit to a chemical test of your blood to determine your blood alcohol concentration. You have the right to refuse to submit to such a test and if you do refuse no test will be given. You have the right to a chemical test by a person of your own choosing at your own expense in addition to the test I have requested. You have the right to know the results of any chemical test. If you refuse the test I have requested, your driver’s license and any non-residence driving privilege may be revoked for one year after an opportunity to appear before a hearing officer to determine if your driver’s license or non-residence driving privilege shall be revoked. If your driver’s license or non-residence driving privileges are revoked by the hearing officer, you have the right to appeal to Circuit Court. Do you understand what I told you? Do you wish to submit to the chemical test I have requested?” App. 8-10.</p>
</footnote>
<footnote label="3">
<p id="b716-6"> Responding to other questions, respondent informed the officers that he had been drinking “close to one ease” by himself at home, and that his last drink was “about ten minutes ago.” Tr. of Preliminary Hearing 8.</p>
</footnote>
<footnote label="4">
<p id="b716-7"> South Dakota Comp. Laws Ann. §19-13-28.1 (Supp. 1982) likewise declares that, notwithstanding the general rule in South Dakota that the claim of a privilege is not a proper subject of comment by judge or counsel, evidence of refusal to submit to a chemical analysis of blood, urine, breath, or other bodily substance “is admissible into evidence” at a trial for driving under the influence of alcohol. A person “may not claim privilege against self-incrimination with regard to admission of refusal to submit to chemical analysis.” <em>Ibid.</em></p>
</footnote>
<footnote label="5">
<p id="b716-8"> As Justice Stevens emphasizes, <em>post, </em>at 567, the South Dakota Supreme Court clearly held that the statute violated the State as well as Federal Constitution. Although this would be an <em>adequate </em>state ground for decision, we do not read the opinion as resting on an <em>independent </em>state ground. Rather, we think the court determined that admission of this evidence violated the Fifth Amendment privilege against self-incrimination, and then concluded without further analysis that the state privilege was <page-number citation-index="1" label="557">*557</page-number>violated as well. In reaching its holding, the court first analyzed our decisions in <em>Schmerber </em>v. California, <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), and <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra.</a></span> </em>The court then described the issue for its review as being “[t]o determine whether the <em>Fifth Amendment </em>privilege against self-incrimination applies to refusal evidence,” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#725" aria-description="Citation for case: State v. Neville">312 N. W. 2d 723, 725</a></span> (1981) (emphasis added), and later asked “whether this testimonial evidence was compelled for purposes of applying the <em>Fifth Amendment </em>standard,” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#726" aria-description="Citation for case: State v. Neville">id., at 726</a></span> (emphasis added). The cases relied on by the court to resolve these issues analyze the <em>federal </em>privilege against self-incrimination.</p>
<p id="b717-6">The analysis of the court below was remarkably similar to that of the state-court opinion reviewed in <em>Delaware </em>v. <em>Prouse, </em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#651" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 651-653</a></span> (1979). That state-court opinion analyzed various decisions interpreting the Federal Constitution, concluded that the Fourth Amendment violated the police procedure at issue there, and then summarily held that the State Constitution was therefore also infringed. As we characterized their analysis, every police practice found to violate the Fourth Amendment would, without further analysis, be held to be contrary to the State Constitution as well. In such a situation, we concluded, this Court has jurisdiction to review the federal constitutional issue decided below.</p>
<p id="b717-7">Justice Stevens, while expressing general dissatisfaction with <em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span>, </em>attempts to distinguish it by noting that the state court there had said the State and Federal Constitutions are “ ‘substantially similar’ and that ‘a violation of the latter is necessarily a violation of the former.’ ” <em>Post, </em>at 571, n. 7. But the South Dakota Supreme Court made virtually identical statements. In a footnote, the court recognized the textual difference between the federal and state constitutional privileges against self-incrimination, but noted that this Court in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>had interpreted the Fifth Amendment prohibition “in light of the more liberal definition of ‘evidence’ as used in our state constitution.” <span class="citation" data-id="9678369"><a href="/opinion/1757041/state-v-neville/#726" aria-description="Citation for case: State v. Neville">312 N. W. 2d, at 726</a></span>, n. Therefore, the court concluded, “[s]ince the Fifth Amendment of the U. S. Constitution is broad enough to exclude this evidence, there is no need to draw a distinction at this time between S. D. Const. Art. VI, § 9 and the Fifth Amendment of the U. S. Constitution.” <em>Ibid. </em>The court could not have stated more clearly that it simply assumed that any violation of the Fifth Amendment privilege also violated, without further analysis, the state privilege. This was precisely the reasoning we found sufficient in <em><span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">Prouse</a></span> </em>to give us jurisdiction to hear the case and decide the federal constitutional issue.</p>
</footnote>
<footnote label="6">
<p id="b718-4"> The South Dakota Supreme Court also remanded for a determination whether respondent’s statement that he was too drunk to pass the test was made after a voluntary waiver of his right to remain silent. As yet, of course, there has been no final judgment in this ease. This Court nevertheless has jurisdiction under <span class="citation no-link">28 U. S. C. § 1257</span>(3) to review the federal constitutional issue which has been finally determined, because if the State ultimately prevails at trial, the federal issue will be mooted; and if the State loses at trial, governing state law, S. D. Comp. Laws Ann. §§ 23A-32-4 and 23A-32-5 (1979), prevents it from again presenting the federal claim for review. See <em>California </em>v. <em>Stewart </em>(decided with <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#498" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 498, n. 71</a></span> (1966)); <em>Cox Broadcasting Corp. </em>v. <em>Cohn, </em><span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#481" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S. 469, 481</a></span> (1975).</p>
</footnote>
<footnote label="7">
<p id="b718-5"> See, <em>e. g., </em>cases cited in nn. 11 and 13, <em>infra.</em></p>
</footnote>
<footnote label="8">
<p id="b719-7"><em> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>also rejected arguments that the coerced blood test violated the right to due process, the right to counsel, and the prohibition against unreasonable searches and seizures.</p>
</footnote>
<footnote label="9">
<p id="b719-8"> <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>did caution that due process concerns could be involved if the police initiated physical violence while administering the test, refused to respect a reasonable request to undergo a different form of testing, or responded to resistance with inappropriate force. 384 U. S., at 760, n. 4.</p>
</footnote>
<footnote label="10">
<p id="b720-7"> <em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span> </em>held that a prosecutor’s or trial court’s comments on a defendant’s refusal to take the witness stand impermissibly burdened the defendant’s Fifth Amendment right to refuse. Unlike the defendant’s situation in <em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span>, </em>a person suspected of drunk driving has no constitutional right to refuse to take a blood-alcohol test. The specific rule of <em><span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/" aria-description="Citation for case: Griffin v. California">Griffin</a></span> </em>is thus inapplicable.</p>
</footnote>
<footnote label="11">
<p id="b721-6"> See, <em>e. g., Newhouse </em>v. <em>Misterly, </em><span class="citation" data-id="286322"><a href="/opinion/286322/bettie-jane-newhouse-v-john-misterly-sheriff/" aria-description="Citation for case: Bettie Jane Newhouse v. John Misterly, Sheriff">415 F. 2d 514</a></span> (CA9 1969); <em>Hill </em>v. <em>State, </em><span class="citation" data-id="9935939"><a href="/opinion/1607970/hill-v-state/#324" aria-description="Citation for case: Hill v. State">366 So. 2d 318, 324-325</a></span> (Ala. 1979); <em>Campbell </em>v. <em>Superior Court, </em><span class="citation" data-id="9541082"><a href="/opinion/1158866/campbell-v-superior-court/" aria-description="Citation for case: Campbell v. Superior Court">106 Ariz. 542</a></span>, <span class="citation" data-id="9541082"><a href="/opinion/1158866/campbell-v-superior-court/" aria-description="Citation for case: Campbell v. Superior Court">479 P. 2d 685</a></span> (1971); <em>State </em>v. <em>Haze, </em><span class="citation" data-id="1161273"><a href="/opinion/1161273/state-v-haze/" aria-description="Citation for case: State v. Haze">218 Kan. 60</a></span>, <span class="citation" data-id="1161273"><a href="/opinion/1161273/state-v-haze/" aria-description="Citation for case: State v. Haze">542 P. 2d 720</a></span> (1975) (refusal to give handwriting exemplar); <em>City of Westerville </em>v. <em>Cunningham, </em><span class="citation" data-id="6754052"><a href="/opinion/6864305/city-of-westerville-v-cunningham/" aria-description="Citation for case: City of Westerville v. Cunningham">15 Ohio St. 2d 121</a></span>, <span class="citation" data-id="6754052"><a href="/opinion/6864305/city-of-westerville-v-cunningham/" aria-description="Citation for case: City of Westerville v. Cunningham">239 N. E. 2d 40</a></span> (1968).</p>
</footnote>
<footnote label="12">
<p id="b721-7"> The Court in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>pointed to the lie detector test as an example of evidence that is difficult to characterize as testimonial or real. Even though the test may seek to obtain physical evidence, we reasoned that to compel a person to submit to such testing “is to evoke the spirit and history of the Fifth Amendment.” 384 U. S., at 764. See also <em>People </em>v. <em>Ellis, </em><span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/#537" aria-description="Citation for case: People v. Ellis">65 Cal. 2d 529, 537</a></span>, and n. 9, <span class="citation" data-id="9616128"><a href="/opinion/1390403/people-v-ellis/#397" aria-description="Citation for case: People v. Ellis">421 P. 2d 393, 397</a></span>, and n. 9 (1966) (analyzing lie detector tests as within the Fifth Amendment privilege). A second example of seemingly physical evidence that nevertheless invokes Fifth Amendment protection was presented in <em>Estelle </em>v. <em>Smith, </em><span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454</a></span> (1981). There, we held that the Fifth Amendment privilege protected compelled <page-number citation-index="1" label="562">*562</page-number>disclosures during a court-ordered psychiatric examination. We specifically rejected the claim that the psychiatrist was observing the patient’s communications simply to infer facts of his mind, rather than to examine the truth of the patient’s statements.</p>
</footnote>
<footnote label="13">
<p id="b722-8"> Many courts have found no self-incrimination problem on the ground of no coercion, or on the analytically related ground that the State, if it can compel submission to the test, can qualify the right to refuse the test. See, <em>e. g., Welch </em>v. <em>District Court, </em><span class="citation" data-id="364649"><a href="/opinion/364649/gene-l-welch-v-district-court-of-vermont-unit-no-5-washington-county/" aria-description="Citation for case: Gene L. Welch v. District Court of Vermont Unit No. 5,...">594 F. 2d 903</a></span> (CA2 1979); <em>State </em>v. <em>Meints, </em><span class="citation" data-id="9516145"><a href="/opinion/2000371/state-v-meints/" aria-description="Citation for case: State v. Meints">189 Neb. 264</a></span>, <span class="citation" data-id="9516145"><a href="/opinion/2000371/state-v-meints/" aria-description="Citation for case: State v. Meints">202 N. W. 2d 202</a></span> (1972); <em>State </em>v. <em>Gardner, </em><span class="citation" data-id="1271135"><a href="/opinion/1271135/state-v-gardner/" aria-description="Citation for case: State v. Gardner">52 Ore. App. 663</a></span>, <span class="citation" data-id="1271135"><a href="/opinion/1271135/state-v-gardner/" aria-description="Citation for case: State v. Gardner">629 P. 2d 412</a></span> (1981); <em>State </em>v. <em>Brean, </em><span class="citation" data-id="1519760"><a href="/opinion/1519760/state-v-brean/" aria-description="Citation for case: State v. Brean">136 Vt. 147</a></span>, <span class="citation" data-id="1519760"><a href="/opinion/1519760/state-v-brean/" aria-description="Citation for case: State v. Brean">385 A. 2d 1085</a></span> (1978).</p>
</footnote>
<footnote label="14">
<p id="b723-5"> Nothing in the record suggests that respondent made or could sustain such a claim in this ease.</p>
</footnote>
<footnote label="15">
<p id="b724-7"> In the context of an arrest for driving while intoxicated, a police inquiry of whether the suspect will take a blood-alcohol test is not an interrogation within the meaning of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>As we stated in <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 301</a></span> (1980), police words or actions “normally attendant to arrest and custody” do not constitute interrogation. The police inquiry here is highly regulated by state law, and is presented in virtually the same words to all suspects. It is similar to a police request to submit to fingerprinting or photography. Respondent’s choice of refusal thus enjoys no prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>protection outside the basic Fifth Amendment protection. See generally Arenella, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span> </em>and the Privilege Against Self-Incrimination: A Reappraisal, <span class="citation no-link">20 Am. Crim. L. Rev. 31</span>, 56-58 (1982).</p>
</footnote>
<footnote label="16">
<p id="b725-7"> Even though the officers did not specifically advise respondent that the test results could be used against him in court, no one would seriously contend that this failure to warn would make the test results inadmissible, had respondent chosen to submit to the test. Cf. <em>Schneckloth </em>v. <em>Busta</em><page-number citation-index="1" label="566">*566</page-number><em>monte, </em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973) (knowledge of right to refuse not an essential part of proving effective consent to a search).</p>
</footnote>
<footnote label="17">
<p id="b726-12"> Since the State wants the suspect to submit to the test, it is in its interest fully to warn suspects of the consequences of refusal. We are informed that police officers in South Dakota now warn suspects that evidence of their refusal can be used against them in court. Tr. of Oral Arg. 16.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/South Dakota v. Opperman.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "South Dakota v. Opperman"
type: case
citation: "428 U.S. 364 (1976)"
parallel_cite: "96 S. Ct. 3092; 49 L. Ed. 2d 1000"
neutral_cite: 1976 U.S. LEXIS 15
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1976
date_decided: 1976-07-06
docket: 75-76
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1976-07-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: South Dakota v. Opperman
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109537/south-dakota-v-opperman/"
  cluster_id: 109537
  opinion_id: 109537
  identity_checked: true
homes:
  - page: "[[Inventory Searches]]"
    role: "Key — Anchor"
related: ["[[Colorado v. Bertine]]", "[[Florida v. Wells]]", "[[Cady v. Dombrowski]]", "[[Illinois v. Lafayette]]"]
aliases: []
tags: ["case", "fourth-amendment", "inventory", "impoundment", "administrative-search"]
holding: "An inventory search of a lawfully impounded vehicle conducted pursuant to standard police procedures, and not as a pretext concealing an…"
lake:
  record_id: South Dakota v. Opperman
  status: verified
  projected_at: 2026-07-06
---

# South Dakota v. Opperman

*428 U.S. 364 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Opperman's car was impounded for repeated overnight parking violations. Following standard department procedure, an officer inventoried the car using a standard form, opened the unlocked glove compartment, and found marijuana. Opperman was convicted and moved to suppress the marijuana as the product of a warrantless search.

## Issue
Whether a routine inventory search of a lawfully impounded vehicle, conducted under standard police procedures, is reasonable under the Fourth Amendment.

## Rule
Routine inventories under standardized procedures are reasonable. The Court emphasized that "there is no suggestion whatever that this standard procedure, essentially like that followed throughout the country, was a pretext concealing an investigatory police motive." — 428 U.S. at 376. ^pin-376

"On this record we conclude that in following standard police procedures, prevailing throughout the country and approved by the overwhelming majority of courts, the conduct of the police was not 'unreasonable' under the Fourth Amendment." — *Id.* ^pin-376a

## Application
The car was lawfully impounded; the inventory followed standard procedure and was prompted by valuables in plain view, with no indication it was a pretext for an investigatory search. On those facts, opening the glove compartment and inventorying the contents was reasonable, and the marijuana was admissible.

## Conclusion
The routine inventory under standard procedures was reasonable; the South Dakota Supreme Court's suppression order was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- The inventory doctrine was refined by [[Colorado v. Bertine]] (closed containers, opened under standardized criteria) and [[Florida v. Wells]] (no inventory used as a ruse for general rummaging); it draws on the vehicle-caretaking roots of [[Cady v. Dombrowski]] and parallels the booking inventory of an arrestee's effects in [[Illinois v. Lafayette]].

## Appears on
- [[Special Needs and Administrative Searches]] — *Key — Anchor*

## Sources
- *South Dakota v. Opperman*, 428 U.S. 364 (1976) — https://www.courtlistener.com/opinion/109537/south-dakota-v-opperman/ — pinpoint: 376.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3af4288baf269bae", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "South Dakota v. Opperman"}, "payload": {"all": [{"cite": "428 U.S. 364", "page": "364", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "428"}, {"cite": "96 S. Ct. 3092", "page": "3092", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "96"}, {"cite": "49 L. Ed. 2d 1000", "page": "1000", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "49"}, {"cite": "1976 U.S. LEXIS 15", "page": "15", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1976"}], "display": "428 U.S. 364", "official": {"cite": "428 U.S. 364", "page": "364", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "428"}, "official_selection_present": true, "record_id": "South Dakota v. Opperman"}}
{"assertion_id": "49716aae5d5421cc", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-376a", "record_id": "South Dakota v. Opperman"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-376a", "pinpoint_status": "slip-only", "quote": "On this record we conclude that in following standard police procedures, prevailing throughout the country and approved by the overwhelming majority of courts, the conduct of the police was not 'unreasonable' under the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "South Dakota v. Opperman", "star_marker": null}}
{"assertion_id": "671d131321840b00", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-376", "record_id": "South Dakota v. Opperman"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-376", "pinpoint_status": "slip-only", "quote": "--- # South Dakota v. Opperman *428 U.S. 364 (1976)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Opperman's car was impounded for repeated overnight parking violations. Following standard department procedure, an officer inventoried the car using a standard form, opened the unlocked glove compartment, and found marijuana. Opperman was convicted and moved to suppress the marijuana as the product of a warrantless search. ## Issue Whether a routine inventory search of a lawfully impounded vehicle, conducted under standard police procedures, is reasonable under the Fourth Amendment. ## Rule Routine inventories under standardized procedures are reasonable. The Court emphasized that", "quote_fidelity": "mismatch", "record_id": "South Dakota v. Opperman", "star_marker": null}}
{"assertion_id": "b0e79b22f58f355b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "South Dakota v. Opperman"}, "payload": {"as_of_content": "1976-07-06", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "South Dakota v. Opperman", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — South Dakota v. Opperman

```json
{
  "schema_version": "s2.v1",
  "record_id": "South Dakota v. Opperman",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "South Dakota v. Opperman",
    "case_name_short": "Opperman",
    "case_name_full": "South Dakota v. Opperman",
    "input_case_name": "South Dakota v. Opperman",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1976-07-06",
    "year": 1976,
    "docket": "75-76",
    "cluster_id": 109537,
    "lead_opinion_id": 109537,
    "sibling_ids": [
      109537,
      9426579,
      9426580,
      9426581
    ],
    "absolute_url": "/opinion/109537/south-dakota-v-opperman/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "428 U.S. 364",
      "volume": "428",
      "reporter": "U.S.",
      "page": "364",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "96 S. Ct. 3092",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3092",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1000",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1000",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1976 U.S. LEXIS 15",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "15",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "428 U.S. 364",
        "volume": "428",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "96 S. Ct. 3092",
        "volume": "96",
        "reporter": "S. Ct.",
        "page": "3092",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "49 L. Ed. 2d 1000",
        "volume": "49",
        "reporter": "L. Ed. 2d",
        "page": "1000",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1976 U.S. LEXIS 15",
        "volume": "1976",
        "reporter": "U.S. LEXIS",
        "page": "15",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "428 U.S. 364",
    "official_selection": {
      "court_class": "scotus",
      "selected": "428 U.S. 364",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-376",
      "page": null,
      "quote": "--- # South Dakota v. Opperman *428 U.S. 364 (1976)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Opperman's car was impounded for repeated overnight parking violations. Following standard department procedure, an officer inventoried the car using a standard form, opened the unlocked glove compartment, and found marijuana. Opperman was convicted and moved to suppress the marijuana as the product of a warrantless search. ## Issue Whether a routine inventory search of a lawfully impounded vehicle, conducted under standard police procedures, is reasonable under the Fourth Amendment. ## Rule Routine inventories under standardized procedures are reasonable. The Court emphasized that",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-376a",
      "page": null,
      "quote": "On this record we conclude that in following standard police procedures, prevailing throughout the country and approved by the overwhelming majority of courts, the conduct of the police was not 'unreasonable' under the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1976-07-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "South Dakota v. Opperman",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Rosario-Santiago",
          "cluster_id": 4666565,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
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
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kennebrew v. State",
          "cluster_id": 10366687,
          "cite": [
            "304 Ga. 406"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 4486934,
          "cite": [
            "2018 CO 27",
            "415 P.3d 815"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Ehiabhi",
          "cluster_id": 4434347,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Wallace",
          "cluster_id": 6239020,
          "cite": [
            "222 Cal. Rptr. 3d 795",
            "15 Cal. App. 5th 82",
            "2017 Cal. App. LEXIS 775"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane1_negative"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Finley",
          "cluster_id": 111880,
          "cite": [
            "95 L. Ed. 2d 539",
            "107 S. Ct. 1990",
            "481 U.S. 551",
            "1987 U.S. LEXIS 2058",
            "55 U.S.L.W. 4612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Mimms",
          "cluster_id": 109751,
          "cite": [
            "54 L. Ed. 2d 331",
            "98 S. Ct. 330",
            "434 U.S. 106",
            "1977 U.S. LEXIS 157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Chadwick",
          "cluster_id": 109714,
          "cite": [
            "53 L. Ed. 2d 538",
            "97 S. Ct. 2476",
            "433 U.S. 1",
            "1977 U.S. LEXIS 133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Jimeno",
          "cluster_id": 112595,
          "cite": [
            "114 L. Ed. 2d 297",
            "111 S. Ct. 1801",
            "500 U.S. 248",
            "1991 U.S. LEXIS 2910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Segura v. United States",
          "cluster_id": 111259,
          "cite": [
            "82 L. Ed. 2d 599",
            "104 S. Ct. 3380",
            "468 U.S. 796",
            "1984 U.S. LEXIS 150",
            "52 U.S.L.W. 5128"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vernonia School District 47J v. Acton",
          "cluster_id": 117964,
          "cite": [
            "132 L. Ed. 2d 564",
            "115 S. Ct. 2386",
            "515 U.S. 646",
            "1995 U.S. LEXIS 4275"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wiede v. State",
          "cluster_id": 1404049,
          "cite": [
            "214 S.W.3d 17",
            "2007 Tex. Crim. App. LEXIS 100",
            "2007 WL 257624"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nixon v. Administrator of General Services",
          "cluster_id": 109729,
          "cite": [
            "53 L. Ed. 2d 867",
            "97 S. Ct. 2777",
            "433 U.S. 425",
            "1977 U.S. LEXIS 24",
            "2 Media L. Rep. (BNA) 2025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Carney",
          "cluster_id": 111423,
          "cite": [
            "85 L. Ed. 2d 406",
            "105 S. Ct. 2066",
            "471 U.S. 386",
            "1985 U.S. LEXIS 8",
            "53 U.S.L.W. 4521"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "South Dakota v. Neville",
          "cluster_id": 110832,
          "cite": [
            "74 L. Ed. 2d 748",
            "103 S. Ct. 916",
            "459 U.S. 553",
            "1983 U.S. LEXIS 129",
            "51 U.S.L.W. 4148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Lafayette",
          "cluster_id": 110976,
          "cite": [
            "77 L. Ed. 2d 65",
            "103 S. Ct. 2605",
            "462 U.S. 640",
            "1983 U.S. LEXIS 71"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
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
        "journal_ref": "South Dakota v. Opperman:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDk4NzgwODAwMDAwJnM9NDQwNTI4MiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109537+OR+9426579+OR+9426580+OR+9426581%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01MTkmcz0xMTQyODQxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109537+OR+9426579+OR+9426580+OR+9426581%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581)",
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
    "complete_query": "cites:(109537 OR 9426579 OR 9426580 OR 9426581)",
    "indexed_citing_opinions": 2070,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109537,
        "count": 1793,
        "count_source": "search"
      },
      {
        "opinion_id": 9426579,
        "count": 336,
        "count_source": "search"
      },
      {
        "opinion_id": 9426580,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9426581,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3446,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/south-dakota-v-opperman.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxOTEyMzkmcz0xMDMyODM2MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109537+OR+9426579+OR+9426580+OR+9426581%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109537,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109069,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 109432,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 274387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 292850,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 296084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 302928,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 307000,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 310049,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 313477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 314840,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 332335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1141627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1153594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1185375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1207398,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1239412,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1256845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1271156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1273048,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1311789,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1312019,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1367368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1494540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1600787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1659036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1762007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1770477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 1868897,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 2060145,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 2350702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109537,
        "cited_id": 2353003,
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
    "date_created": "2026-07-05T20:10:19Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:10:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:10:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:13:20Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:10:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — South Dakota v. Opperman

```
<div>
<center><b><span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U.S. 364</a></span> (1976)</b></center>
<center><h1>SOUTH DAKOTA<br>
v.<br>
OPPERMAN.</h1></center>
<center>No. 75-76.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 29, 1976.</center>
<center>Decided July 6, 1976.</center>
CERTIORARI TO THE SUPREME COURT OF SOUTH DAKOTA.
<p><i>William J. Janklow,</i> Attorney General of South Dakota, argued the cause for petitioner. With him on the brief was <i>Earl R. Mettler,</i> Assistant Attorney General.</p>
<p><i>Robert C. Ulrich,</i> by appointment of the Court, 423 <span class="star-pagination">*365</span> U. S. 1012, argued the cause for respondent <i>pro hac vice.</i> With him on the brief were <i>Lee M. McCahren</i> and <i>John F. Hagemann.</i><sup>[*]</sup></p>
<p>MR. CHIEF JUSTICE BURGER delivered the opinion of the Court.</p>
<p>We review the judgment of the Supreme Court of South Dakota, holding that local police violated the Fourth Amendment to the Federal Constitution, as applicable to the States under the Fourteenth Amendment, when they conducted a routine inventory search of an automobile lawfully impounded by police for violations of municipal parking ordinances.</p>
<p></p>
<h2>(1)</h2>
<p>Local ordinances prohibit parking in certain areas of downtown Vermillion, S. D., between the hours of 2 a. m. and 6 a. m. During the early morning hours of December 10, 1973, a Vermillion police officer observed respondent's unoccupied vehicle illegally parked in the restricted zone. At approximately 3 a. m., the officer issued an overtime parking ticket and placed it on the car's windshield. The citation warned:</p>
<blockquote>"Vehicles in violation of any parking ordinance may be towed from the area."</blockquote>
<p>At approximately 10 o'clock on the same morning, another <span class="star-pagination">*366</span> officer issued a second ticket for an overtime parking violation. These circumstances were routinely reported to police headquarters, and after the vehicle was inspected, the car was towed to the city impound lot.</p>
<p>From outside the car at the impound lot, a police officer observed a watch on the dashboard and other items of personal property located on the back seat and back floorboard. At the officer's direction, the car door was then unlocked and, using a standard inventory form pursuant to standard police procedures, the officer inventoried the contents of the car, including the contents of the glove compartment, which was unlocked. There he found marihuana contained in a plastic bag. All items, including the contraband, were removed to the police department for safekeeping.<sup>[1]</sup> During the late afternoon of December 10, respondent appeared at the police department to claim his property. The marihuana was retained by police.</p>
<p>Respondent was subsequently arrested on charges of possession of marihuana. His motion to suppress the evidence yielded by the inventory search was denied; he was convicted after a jury trial and sentenced to a fine of $100 and 14 days' incarceration in the county jail. On appeal, the Supreme Court of South Dakota reversed <span class="star-pagination">*367</span> the conviction. 89 S. D. , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152</a></span>. The court concluded that the evidence had been obtained in violation of the Fourth Amendment prohibition against unreasonable searches and seizures. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./423/923/">423 U. S. 923</a></span> (1975), and we reverse.</p>
<p></p>
<h2>(2)</h2>
<p>This Court has traditionally drawn a distinction between automobiles and homes or offices in relation to the Fourth Amendment. Although automobiles are "effects" and thus within the reach of the Fourth Amendment, <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 439</a></span> (1973), warrantless examinations of automobiles have been upheld in circumstances in which a search of a home or office would not. <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#589" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 589</a></span> (1974); <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 439-440</a></span>; <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#48" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 48</a></span> (1970).</p>
<p>The reason for this well-settled distinction is twofold. First, the inherent mobility of automobiles creates circumstances of such exigency that, as a practical necessity, rigorous enforcement of the warrant requirement is impossible. <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153-154</a></span> (1925); <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#459" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 459-460</a></span> (1971). But the Court has also upheld warrantless searches where no immediate danger was presented that the car would be removed from the jurisdiction. <i>Chambers</i> v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Maroney, supra,</i> at 51-52</a></span>; <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967). Besides the element of mobility, less rigorous warrant requirements govern because the expectation of privacy with respect to one's automobile is significantly less than that relating to one's home or office.<sup>[2]</sup> In discharging their varied responsibilities <span class="star-pagination">*368</span> for ensuring the public safety, law enforcement officials are necessarily brought into frequent contact with automobiles. Most of this contact is distinctly noncriminal in nature. <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#442" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 442</a></span>. Automobiles, unlike homes, are subjected to pervasive and continuing governmental regulation and controls, including periodic inspection and licensing requirements. As an everyday occurrence, police stop and examine vehicles when license plates or inspection stickers have expired, or if other violations, such as exhaust fumes or excessive noise, are noted, or if headlights or other safety equipment are not in proper working order.</p>
<p>The expectation of privacy as to automobiles in further diminished by the obviously public nature of automobile travel. Only two Terms ago, the Court noted:</p>
<blockquote>"One has a lesser expectation of privacy in a motor vehicle because its function is transportation and it seldom serves as one's residence or as the repository of personal effects. . . . It travels public thoroughfares where both its occupants and its contents are in plain view." <i>Cardwell</i> v. <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis"><i>Lewis, supra,</i> at 590</a></span>.</blockquote>
<p>In the interests of public safety and as part of what the Court has called "community caretaking functions," <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 441</a></span>, automobiles are frequently taken into police custody. Vehicle accidents present one such occasion. To permit the uninterrupted flow of traffic and in some circumstances to preserve evidence, disabled or damaged vehicles will often be removed from the highways or streets at the behest of police engaged solely in caretaking and traffic-control activities. <span class="star-pagination">*369</span> Police will also frequently remove and impound automobiles which violate parking ordinances and which thereby jeopardize both the public safety and the efficient movement of vehicular traffic.<sup>[3]</sup> The authority of police to seize and remove from the streets vehicles impeding traffic or threatening public safety and convenience is beyond challenge.</p>
<p>When vehicles are impounded, local police departments generally follow a routine practice of securing and inventorying the automobiles' contents. These procedures developed in response to three distinct needs: the protection of the owner's property while it remains in police custody, <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9458066"><a href="/opinion/302928/united-states-v-william-elmer-mitchell/#961" aria-description="Citation for case: United States v. William Elmer Mitchell">458 F. 2d 960, 961</a></span> (CA9 1972); the protection of the police against claims or disputes over lost or stolen property, <i>United States</i> v. <i>Kelehar,</i> <span class="citation" data-id="307000"><a href="/opinion/307000/united-states-v-levy-alan-kelehar-aka-james-stone/#178" aria-description="Citation for case: United States v. Levy Alan Kelehar, A/K/A James Stone">470 F. 2d 176, 178</a></span> (CA5 1972); and the protection of the police from potential danger, <i>Cooper</i> v. <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California"><i>California, supra,</i> at 61-62</a></span>. The practice has been viewed as essential to respond to incidents of theft or vandalism. See <i>Cabbler</i> v. <i>Commonwealth,</i> <span class="citation" data-id="1256845"><a href="/opinion/1256845/cabbler-v-commonwealth/#522" aria-description="Citation for case: Cabbler v. Commonwealth">212 Va. 520, 522</a></span>, <span class="citation" data-id="1256845"><a href="/opinion/1256845/cabbler-v-commonwealth/#782" aria-description="Citation for case: Cabbler v. Commonwealth">184 S. E. 2d 781, 782</a></span> (1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./405/1073/">405 U. S. 1073</a></span> (1972); <i>Warrix</i> v. <i>State,</i> <span class="citation" data-id="1762007"><a href="/opinion/1762007/warrix-v-state/#376" aria-description="Citation for case: Warrix v. State">50 Wis. 2d 368, 376</a></span>, <span class="citation" data-id="1762007"><a href="/opinion/1762007/warrix-v-state/#194" aria-description="Citation for case: Warrix v. State">184 N. W. 2d 189, 194</a></span> (1971). In addition, police frequently attempt to determine whether a vehicle has been stolen and thereafter abandoned.</p>
<p>These caretaking procedures have almost uniformly been upheld by the state courts, which by virtue of the localized nature of traffic regulation have had considerable occasion to deal with the issue.<sup>[4]</sup> Applying the <span class="star-pagination">*370</span> Fourth Amendment standard of "reasonableness,"<sup>[5]</sup> the state courts have overwhelmingly concluded that, even if an inventory is characterized as a "search,"<sup>[6]</sup> the <span class="star-pagination">*371</span> intrusion is constitutionally permissible. See, <i>e. g., </i><i>City of St. Paul</i> v. <i>Myles,</i> <span class="citation" data-id="1239412"><a href="/opinion/1239412/city-of-st-paul-v-myles/#300" aria-description="Citation for case: City of St. Paul v. Myles">298 Minn. 298, 300-301</a></span>, <span class="citation" data-id="1239412"><a href="/opinion/1239412/city-of-st-paul-v-myles/#699" aria-description="Citation for case: City of St. Paul v. Myles">218 N. W. 2d 697, 699</a></span> (1974); <i>State</i> v. <i>Tully,</i> <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/#136" aria-description="Citation for case: State v. Tully">166 Conn. 126, 136</a></span>, <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/#609" aria-description="Citation for case: State v. Tully">348 A. 2d 603, 609</a></span> (1974); <i>People</i> v. <i>Trusty,</i> <span class="citation" data-id="9848553"><a href="/opinion/1273048/people-v-trusty/#296" aria-description="Citation for case: People v. Trusty">183 Colo. 291, 296-297</a></span>, <span class="citation" data-id="9848553"><a href="/opinion/1273048/people-v-trusty/#425" aria-description="Citation for case: People v. Trusty">516 P. 2d 423, 425-426</a></span> (1973); <i>People</i> v. <i>Sullivan,</i> 29 N. Y. 2d 69, 73, <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#466" aria-description="Citation for case: People v. Sullivan">272 N. E. 2d 464, 466</a></span> (1971); <i>Cabbler</i> v. <i><span class="citation" data-id="1256845"><a href="/opinion/1256845/cabbler-v-commonwealth/" aria-description="Citation for case: Cabbler v. Commonwealth">Commonwealth, supra</a></span></i><i>; </i><i>Warrix</i> v. <i>State, supra</i><i>; </i><i>State</i> v. <i>Wallen,</i> <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/" aria-description="Citation for case: State v. Wallen">185 Neb. 44</a></span>, <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/" aria-description="Citation for case: State v. Wallen">173 N. W. 2d 372</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./399/912/">399 U. S. 912</a></span> (1970); <i>State</i> v. <i>Criscola,</i> <span class="citation" data-id="1141627"><a href="/opinion/1141627/state-v-criscola/" aria-description="Citation for case: State v. Criscola">21 Utah 2d 272</a></span>, <span class="citation" data-id="1141627"><a href="/opinion/1141627/state-v-criscola/" aria-description="Citation for case: State v. Criscola">444 P. 2d 517</a></span> (1968); <i>State</i> v. <i>Montague,</i> <span class="citation" data-id="1207398"><a href="/opinion/1207398/state-v-montague/" aria-description="Citation for case: State v. Montague">73 Wash. 2d 381</a></span>, <span class="citation" data-id="1207398"><a href="/opinion/1207398/state-v-montague/" aria-description="Citation for case: State v. Montague">438 P. 2d 571</a></span> (1968); <i>People</i> v. <i>Clark,</i> <span class="citation" data-id="9719416"><a href="/opinion/2111286/people-v-clark/" aria-description="Citation for case: People v. Clark">32 Ill. App. 3d 898</a></span>, <span class="citation no-link">336 N. E. 2d 892</span> (1975); <i>State</i> v. <i>Achter,</i> <span class="citation" data-id="1770477"><a href="/opinion/1770477/state-v-achter/" aria-description="Citation for case: State v. Achter">512 S. W. 2d 894</a></span> (Mo. Ct. App. 1974); <i>Bennett</i> v. <i>State,</i> <span class="citation" data-id="9538969"><a href="/opinion/1153594/bennett-v-state/" aria-description="Citation for case: Bennett v. State">507 P. 2d 1252</a></span> (Okla. Crim. App. 1973); <i>People</i> v. <i>Willis,</i> <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">46 Mich. App. 436</a></span>, <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">208 N. W. 2d 204</a></span> (1973); <i>State</i> v. <i>All,</i> 17 N. C. App. 284, <span class="citation" data-id="1271156"><a href="/opinion/1271156/state-v-all/" aria-description="Citation for case: State v. All">193 S. E. 2d 770</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/866/">414 U. S. 866</a></span> (1973); <i>Godbee</i> v. <i>State,</i> <span class="citation" data-id="1659036"><a href="/opinion/1659036/godbee-v-state/" aria-description="Citation for case: Godbee v. State">224 So. 2d 441</a></span> (Fla. Dist. Ct. App. 1969). Even the seminal state decision relied on by the South Dakota Supreme Court in reaching the contrary result. <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation no-link">4 Cal. 2d 699</span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84</a></span> (1971), expressly approved police caretaking activities resulting in the securing of property within the officer's plain view.</p>
<p>The majority of the Federal Courts of Appeals have likewise sustained inventory procedures as reasonable police intrusions. As Judge Wisdom has observed:</p>
<blockquote>"[W]hen the police take custody of any sort of container [such as] an automobile . . . it is reasonable to search the container to itemize the property to be held by the police. [This reflects] the underlying principle that the fourth amendment proscribes only <i>unreasonable</i> searches." <i>United States</i> v. <i>Gravitt,</i> <span class="citation" data-id="313366"><a href="/opinion/313366/united-states-v-jerry-eugene-gravitt/#378" aria-description="Citation for case: United States v. Jerry Eugene Gravitt">484 F. 2d 375, 378</a></span> (CA5 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/1135/">414 U. S. 1135</a></span> (1974) (emphasis in original).</blockquote>
<p><span class="star-pagination">*372</span> See also <i>Cabbler</i> v. <i>Superintendent,</i> <span class="citation" data-id="332335"><a href="/opinion/332335/herbert-w-cabbler-v-superintendent-virginia-state-penitentiary/" aria-description="Citation for case: Herbert W. Cabbler v. Superintendent, Virginia State...">528 F. 2d 1142</a></span> (CA4 1975), cert. pending, No. 75-1463; <i>Barker</i> v. <i>Johnson,</i> <span class="citation" data-id="313477"><a href="/opinion/313477/daniel-barker-v-dale-johnson/" aria-description="Citation for case: Daniel Barker v. Dale Johnson">484 F. 2d 941</a></span> (CA6 1973); <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9458066"><a href="/opinion/302928/united-states-v-william-elmer-mitchell/" aria-description="Citation for case: United States v. William Elmer Mitchell">458 F. 2d 960</a></span> (CA9 1972); <i>United States</i> v. <i>Lipscomb,</i> <span class="citation" data-id="293775"><a href="/opinion/293775/united-states-v-robert-edward-lipscomb/" aria-description="Citation for case: United States v. Robert Edward Lipscomb">435 F. 2d 795</a></span> (CA5 1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/980/">401 U. S. 980</a></span> (1971); <i>United States</i> v. <i>Pennington,</i> <span class="citation" data-id="9456780"><a href="/opinion/296084/united-states-v-james-larry-pennington/" aria-description="Citation for case: United States v. James Larry Pennington">441 F. 2d 249</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/854/">404 U. S. 854</a></span> (1971); <i>United States</i> v. <i>Boyd,</i> <span class="citation multiple-matches"><a href="/c/F.%202d/436/1203/">436 F. 2d 1203</a></span> (CA5 1971); <i>Cotton</i> v. <i>United States,</i> <span class="citation" data-id="274387"><a href="/opinion/274387/gary-leland-cotton-v-united-states/" aria-description="Citation for case: Gary Leland Cotton v. United States">371 F. 2d 385</a></span> (CA9 1967). Accord, <i>Lowe</i> v. <i>Hopper,</i> <span class="citation" data-id="1367368"><a href="/opinion/1367368/lowe-v-hopper/#976" aria-description="Citation for case: Lowe v. Hopper">400 F. Supp. 970, 976-977</a></span> (SD Ga. 1975); <i>United States</i> v. <i>Spitalieri,</i> <span class="citation" data-id="1494540"><a href="/opinion/1494540/united-states-v-spitalieri/#169" aria-description="Citation for case: United States v. Spitalieri">391 F. Supp. 167, 169-170</a></span> (ND Ohio 1975); <i>United States</i> v. <i>Smith,</i> <span class="citation" data-id="1445531"><a href="/opinion/1445531/united-states-v-smith/" aria-description="Citation for case: United States v. Smith">340 F. Supp. 1023</a></span> (Conn. 1972); <i>United States</i> v. <i>Fuller,</i> <span class="citation" data-id="1868897"><a href="/opinion/1868897/united-states-v-fuller/" aria-description="Citation for case: United States v. Fuller">277 F. Supp. 97</a></span> (DC 1967), conviction aff'd, 139 U. S. App. D. C. 375, <span class="citation" data-id="292850"><a href="/opinion/292850/morris-fuller-v-united-states/" aria-description="Citation for case: Morris Fuller v. United States">433 F. 2d 533</a></span> (1970). These cases have recognized that standard inventories often include an examination of the glove compartment, since it is a customary place for documents of ownership and registration, <i>United States</i> v. <span class="citation" data-id="9456780"><a href="/opinion/296084/united-states-v-james-larry-pennington/#251" aria-description="Citation for case: United States v. James Larry Pennington"><i>Pennington, supra,</i> at 251</a></span>, as well as a place for the temporary storage of valuables.</p>
<p></p>
<h2>(3)</h2>
<p>The decisions of this Court point unmistakably to the conclusion reached by both federal and state courts that inventories pursuant to standard police procedures are reasonable. In the first such case, Mr. Justice Black made plain the nature of the inquiry before us:</p>
<blockquote>"But the question here is not whether the search was <i>authorized</i> by state law. The question is rather whether the search was <i>reasonable</i> under the Fourth Amendment." <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61</a></span> (emphasis added).</blockquote>
<p>And, in his last writing on the Fourth Amendment, Mr. Justice Black said:</p>
<blockquote>"[T]he Fourth Amendment does not require that every search be made pursuant to a warrant. It <span class="star-pagination">*373</span> prohibits only `<i>unreasonable</i> searches and seizures.' The relevant test <i>is not the reasonableness of the opportunity to procure a warrant,</i> but the reasonableness of the seizure under all the circumstances. The test of reasonableness cannot be fixed by <i>per se</i> rules; each case must be decided on its own facts." <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#509" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 509-510</a></span> (concurring and dissenting) (emphasis added).</blockquote>
<p>In applying the reasonableness standard adopted by the Framers, this Court has consistently sustained police intrusions into automobiles impounded or otherwise in lawful police custody where the process is aimed at securing or protecting the car and its contents. In <i>Cooper</i> v. <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">California, supra</a></span></i><i>,</i> the Court upheld the inventory of a car impounded under the authority of a state forfeiture statute. Even though the inventory was conducted in a distinctly criminal setting<sup>[7]</sup> and carried out a week after the car had been impounded, the Court nonetheless found that the car search, including examination of the glove compartment where contraband was found, was reasonable under the circumstances. This conclusion was reached despite the fact that no warrant had issued and probable cause to search for the contraband in the vehicle had not been established. The Court said in language explicitly applicable here:</p>
<blockquote>"It would be unreasonable to hold that the police, having to retain the car in their custody for such a length of time, had no right, even for their own protection, to search it." <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61-62</a></span>.<sup>[8]</sup></blockquote>
<p><span class="star-pagination">*374</span> In the following Term, the Court in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968), upheld the introduction of evidence, seized by an officer who, after conducting an inventory search of a car and while taking means to safeguard it, observed a car registration card lying on the metal stripping of the car door. Rejecting the argument that a warrant was necessary, the Court held that the intrusion was justifiable since it was "taken to protect the car while it was in police custody." <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States"><i>Id.,</i> at 236</a></span>.<sup>[9]</sup></p>
<p>Finally, in <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski, supra</a></span></i><i>,</i> the Court upheld a warrantless search of an automobile towed to a private garage even though no probable cause existed to believe that the vehicle contained fruits of a crime. The sole justification for the warrantless incursion was that it was incident to the caretaking function of the local police to protect the community's safety. Indeed, the protective search was instituted solely because local police "were under the impression" that the incapacitated driver, a Chicago police officer, was required to carry his service revolver at all times; the police had reasonable grounds to believe a weapon might be in the car, and thus available to vandals. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#436" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 436</a></span>. The Court carefully noted that the protective search was <span class="star-pagination">*375</span> carried out in accordance with <i>standard procedures</i> in the local police department, <i>ibid.,</i> a factor tending to ensure that the intrusion would be limited in scope to the extent necessary to carry out the caretaking function. See <i>United States</i> v. <i>Spitalieri,</i> <span class="citation" data-id="1494540"><a href="/opinion/1494540/united-states-v-spitalieri/#169" aria-description="Citation for case: United States v. Spitalieri">391 F. Supp., at 169</a></span>. In reaching this result, the Court in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> distinguished <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964), on the grounds that the holding, invalidating a car search conducted after a vagrancy arrest, "stands only for the proposition that the search challenged there could not be justified as one incident to an arrest." <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#444" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 444</a></span>. <i><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">Preston</a></span></i> therefore did not raise the issue of the constitutionality of a protective inventory of a car lawfully within police custody.</p>
<p>The holdings in <i>Cooper, Harris,</i> and <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> point the way to the correct resolution of this case. None of the three cases, of course, involves the precise situation presented here; but, as in all Fourth Amendment cases, we are obliged to look to all the facts and circumstances of this case in light of the principles set forth in these prior decisions.</p>
<blockquote>"[W]hether a search and seizure is unreasonable within the meaning of the Fourth Amendment depends upon the facts and circumstances of each case . . . ." <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#59" aria-description="Citation for case: Cooper v. California">386 U. S., at 59</a></span>.</blockquote>
<p>The Vermillion police were indisputably engaged in a caretaking search of a lawfully impounded automobile. Cf. <i>United States</i> v. <i>Lawson,</i> <span class="citation" data-id="314840"><a href="/opinion/314840/united-states-v-sam-meredith-lawson/#471" aria-description="Citation for case: United States v. Sam Meredith Lawson">487 F. 2d 468, 471</a></span> (CA8 1973). The inventory was conducted only after the car had been impounded for multiple parking violations. The owner, having left his car illegally parked for an extended period, and thus subject to impoundment, was not present to make other arrangements for the safekeeping of his belongings. The inventory itself was prompted by the presence in plain view of a number of <span class="star-pagination">*376</span> valuables inside the car. As in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span>,</i> there is no suggestion whatever that this standard procedure, essentially like that followed throughout the country, was a pretext concealing an investigatory police motive.<sup>[10]</sup></p>
<p>On this record we conclude that in following standard police procedures, prevailing throughout the country and approved by the overwhelming majority of courts, the conduct of the police was not "unreasonable" under the Fourth Amendment.</p>
<p>The judgment of the South Dakota Supreme Court is therefore reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>While I join the opinion of the Court, I add this opinion to express additional views as to why the search conducted in this case is valid under the Fourth and Fourteenth Amendments. This inquiry involves two distinct questions: (i) whether routine inventory searches are impermissible, and (ii) if not, whether they must be conducted pursuant to a warrant.</p>
<p></p>
<h2>
<span class="star-pagination">*377</span> I</h2>
<p>The central purpose of the Fourth Amendment is to safeguard the privacy and security of individuals against arbitrary invasions by government officials. See, <i>e. g., </i><i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528</a></span> (1967). None of our prior decisions is dispositive of the issue whether the Amendment permits routine inventory "searches"<sup>[1]</sup> of automobiles.<sup>[2]</sup> Resolution of this <span class="star-pagination">*378</span> question requires a weighing of the governmental and societal interests advanced to justify such intrusions against the constitutionally protected interest of the individual citizen in the privacy of his effects. <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 555; <i>United States</i> v. <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><i>Brignoni-Ponce, supra,</i> at 878-879</a></span>; <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#892" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 892</a></span> (1975); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 447-448</a></span> (1973); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968). Cf. <i>Camara</i> v. <i>Municipal Court, supra,</i> at 534-535. As noted in the Court's opinion, see <i>ante,</i> at 369, three interests generally have been advanced in support of inventory searches: (i) protection of the police from danger; (ii) protection of the police against claims and disputes over lost or stolen property; and (iii) protection of the owner's property while it remains in police custody.</p>
<p>Except in rare cases, there is little danger associated with impounding unsearched automobiles. But the occasional danger that may exist cannot be discounted entirely. See <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61-62</a></span> (1967). The harmful consequences in those rare cases may be great, and there does not appear to be any effective way of identifying in advance those circumstances or classes of automobile impoundments which represent a greater risk. Society also has an important interest in minimizing the number of false claims filed against police since they may diminish the community's respect for law enforcement generally and lower department morale, thereby impairing the effectiveness of the police.<sup>[3]</sup> It <span class="star-pagination">*379</span> is not clear, however, that inventories are a completely effective means of discouraging false claims, since there remains the possibility of accompanying such claims with an assertion that an item was stolen prior to the inventory or was intentionally omitted from the police records.</p>
<p>The protection of the owner's property is a significant interest for both the policeman and the citizen. It is argued that an inventory is not necessary since locked doors and rolled-up windows afford the same protection that the contents of a parked automobile normally enjoy.<sup>[4]</sup> But many owners might leave valuables in their automobile temporarily that they would not leave there unattended for the several days that police custody may last. There is thus a substantial gain in security if automobiles are inventoried and valuable items removed for storage. And, while the same security could be attained by posting a guard at the storage lot, that alternative may be prohibitively expensive, especially for smaller jurisdictions.<sup>[5]</sup></p>
<p>Against these interests must be weighed the citizen's interest in the privacy of the contents of his automobile. Although the expectation of privacy in an automobile is significantly less than the traditional expectation of privacy associated with the home, <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 561-562; <i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra,</a></span></i> at 896 n. 2; see <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590-591</a></span> (1974) (plurality opinion), the unrestrained search <span class="star-pagination">*380</span> of an automobile and its contents would constitute a serious intrusion upon the privacy of the individual in many circumstances. But such a search is not at issue in this case. As the Court's opinion emphasizes, the search here was limited to an inventory of the unoccupied automobile and was conducted strictly in accord with the regulations of the Vermillion Police Department.<sup>[6]</sup> Upholding searches of this type provides no general license for the police to examine all the contents of such automobiles.<sup>[7]</sup></p>
<p>I agree with the Court that the Constitution permits routine inventory searches, and turn next to the question whether they must be conducted pursuant to a warrant.</p>
<p></p>
<h2>
<span class="star-pagination">*381</span> II</h2>
<p>While the Fourth Amendment speaks broadly in terms of "unreasonable searches and seizures,"<sup>[8]</sup> the decisions of this Court have recognized that the definition of "reasonableness" turns, at least in part, on the more specific dictates of the Warrant Clause. See <i>United States</i> v. <i>United States District Court,</i> <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#315" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 315</a></span> (1972); <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#356" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 356</a></span> (1967); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528</a></span>. As the Court explained in <i>Katz</i> v. <i>United States, supra,</i> at 357, "[s]earches conducted without warrants have been held unlawful `notwithstanding facts unquestionably showing probable cause,' <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#33" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 33</a></span>, for the Constitution requires `that the deliberate, impartial judgment of a judicial officer . . . be interposed between the citizen and the police . . . .' <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#481" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 481-482</a></span>." Thus, although "[s]ome have argued that `[t]he relevant test is not whether it is reasonable to procure a search warrant, but whether the search was reasonable,' <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/#66" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56, 66</a></span> (1950)," "[t]his view has not been accepted." <i>United States</i> v. <i>United States District Court, supra,</i> at 315, and n. 16. See <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969). Except in a few carefully defined classes of cases, a search of private property without valid consent is "unreasonable" unless it has been authorized by a valid search warrant. See, <i>e. g., </i><i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269</a></span> (1973); <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span> (1964); <span class="star-pagination">*382</span> <i>Camara</i> v. <i>Municipal Court, supra,</i> at 528; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span> (1951); <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span> (1925).</p>
<p>Although the Court has validated warrantless searches of automobiles in circumstances that would not justify a search of a home or office, <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973); <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970); <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), these decisions establish no general "automobile exception" to the warrant requirement. See <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964). Rather, they demonstrate that " `for the purposes of the Fourth Amendment there is a constitutional difference between houses and cars,' " <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#439" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 439</a></span>, quoting <i>Chambers</i> v. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney"><i>Maroney, supra,</i> at 52</a></span>, a difference that may in some cases justify a warrantless search.<sup>[9]</sup></p>
<p>The routine inventory search under consideration in this case does not fall within any of the established exceptions to the warrant requirement.<sup>[10]</sup> But examination of the interests which are protected when searches are <span class="star-pagination">*383</span> conditioned on warrants issued by a judicial officer reveals that none of these is implicated here. A warrant may issue only upon "probable cause." In the criminal context the requirement of a warrant protects the individual's legitimate expectation of privacy against the overzealous police officer. "Its protection consists in requiring that those inferences [concerning probable cause] be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). See, <i>e. g., </i><i>United States</i> v. <i>United States District Court, supra,</i> at 316-318. Inventory searches, however, are not conducted in order to discover evidence of crime. The officer does not make a discretionary determination to search based on a judgment that certain conditions are present. Inventory searches are conducted in accordance with established police department rules or policy and occur whenever an automobile is seized. There are thus no special facts for a neutral magistrate to evaluate.</p>
<p>A related purpose of the warrant requirement is to prevent hindsight from affecting the evaluation of the reasonableness of a search. See <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 565; cf. <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span>, 455 n. 22 (1976) (MARSHALL, J., dissenting). In the case of an inventory search conducted in accordance with standard police department procedures, there is no significant danger of hindsight justification. The absence of a warrant will not impair the effectiveness of post-search review of the reasonableness of a particular inventory search.</p>
<p>Warrants also have been required outside the context of a criminal investigation. In <i>Camara</i> v. <i><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">Municipal Court</a></span></i><i>,</i> the Court held that, absent consent, a warrant was necessary to conduct an areawide building code inspection, <span class="star-pagination">*384</span> even though the search could be made absent cause to believe that there were violations in the particular buildings being searched. In requiring a warrant the Court emphasized that "[t]he practical effect of [the existing warrantless search procedures had been] to leave the occupant subject to the discretion of the official in the field," since</p>
<blockquote>"when [an] inspector demands entry, the occupant ha[d] no way of knowing whether enforcement of the municipal code involved require[d] inspection of his premises, no way of knowing the lawful limits of the inspector's power to search, and no way of knowing whether the inspector himself [was] acting under proper authorization." <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#532" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 532</a></span>.</blockquote>
<p>In the inventory search context these concerns are absent. The owner or prior occupant of the automobile is not present, nor, in many cases, is there any real likelihood that he could be located within a reasonable period of time. More importantly, no significant discretion is placed in the hands of the individual officer: he usually has no choice as to the subject of the search or its scope.<sup>[11]</sup></p>
<p>In sum, I agree with the Court that the routine inventory search in this case is constitutional.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN and MR. JUSTICE STEWART join, dissenting.</p>
<p>The Court today holds that the Fourth Amendment permits a routine police inventory search of the closed <span class="star-pagination">*385</span> glove compartment of a locked automobile impounded for ordinary traffic violations. Under the Court's holding, such a search may be made without attempting to secure the consent of the owner and without any particular reason to believe the impounded automobile contains contraband, evidence, or valuables, or presents any danger to its custodians or the public.<sup>[1]</sup> Because I believe this holding to be contrary to sound elaboration of established Fourth Amendment principles, I dissent.</p>
<p>As MR. JUSTICE POWELL recognizes, the requirement of a warrant aside, resolution of the question whether an inventory search of closed compartments inside a locked automobile can ever be justified as a constitutionally "reasonable" search<sup>[2]</sup> depends upon a reconciliation of the owner's constitutionally protected privacy interests against governmental intrusion, and legitimate governmental interests furthered by securing the car and its contents. <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-21</a></span> (1968); <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#534" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 534-535, 536-537</a></span> (1967). The Court fails clearly to articulate the reasons for its reconciliation of these interests in this case, but it is at least clear to me that the considerations <span class="star-pagination">*386</span> alluded to by the Court, and further discussed by MR. JUSTICE POWELL, are insufficient to justify the Court's result in this case.</p>
<p>To begin with, the Court appears to suggest by reference to a "diminished" expectation of privacy, <i>ante,</i> at 368, that a person's constitutional interest in protecting the integrity of closed compartments of his locked automobile may routinely be sacrificed to governmental interests requiring interference with that privacy that are less compelling than would be necessary to justify a search of similar scope of the person's home or office. This has never been the law. The Court correctly observes that some prior cases have drawn distinctions between automobiles and homes or offices in Fourth Amendment cases; but even as the Court's discussion makes clear, the reasons for distinction in those cases are not present here. Thus, <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42</a></span> (1970), and <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/" aria-description="Citation for case: Carroll v. United States">267 U. S. 132</a></span> (1925), permitted certain probable-cause searches to be carried out without warrants in view of the exigencies created by the mobility of automobiles, but both decisions reaffirmed that the standard of probable cause necessary to authorize such a search was no less than the standard applicable to search of a home or office. <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#51" aria-description="Citation for case: Chambers v. Maroney"><i>Chambers, supra,</i> at 51</a></span>; <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#155" aria-description="Citation for case: Carroll v. United States"><i>Carroll, supra,</i> at 155-156</a></span>.<sup>[3]</sup> In other contexts the Court has recognized that automobile travel sacrifices some privacy interests to the publicity of plain view, <i>e. g., </i><i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 590</a></span> (1974) (plurality opinion); cf. <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968). But this recognition, too, is inapposite here, for there is no question of plain view in <span class="star-pagination">*387</span> this case.<sup>[4]</sup> Nor does this case concern intrusions of the scope that the Court apparently assumes would ordinarily be permissible in order to insure the running safety of a car. While it may be that privacy expectations associated with automobile travel are in some regards less than those associated with a home or office, see <i>United States</i> v. <i>Martinez-Fuerte, post,</i> at 561-562, it is equally clear that "[t]he word `automobile' is not a talisman in whose presence the Fourth Amendment fades away . . . ," <i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span>, <span class="star-pagination">*388</span> 461 (1971).<sup>[5]</sup> Thus, we have recognized that "[a] <i>search,</i> even of an automobile, is a substantial invasion of privacy," <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/#896" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891, 896</a></span> (1975) (emphasis added), and accordingly or cases have consistently recognized that the nature and substantiality of interest required to justify <i>a search</i> of private areas of an automobile is no less than that necessary to justify an intrusion of similar scope into a home or office. See, <i>e. g., </i><i>United States</i> v. <i><span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">Ortiz, supra</a></span></i><i>; </i><i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#269" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 269-270</a></span> (1973); <i><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge, supra;</a></span> </i><i>Dyke</i> v. <i>Taylor Implement Mfg. Co.,</i> <span class="citation" data-id="9423697"><a href="/opinion/107687/dyke-v-taylor-implement-manufacturing-co/#221" aria-description="Citation for case: Dyke v. Taylor Implement Manufacturing Co.">391 U. S. 216, 221-222</a></span> (1968); <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/" aria-description="Citation for case: Preston v. United States">376 U. S. 364</a></span> (1964).<sup>[6]</sup></p>
<p><span class="star-pagination">*389</span> The Court's opinion appears to suggest that its result may in any event be justified because the inventory search procedure is a "reasonable" response to</p>
<blockquote>"three distinct needs: the protection of the owner's property while it remains in police custody . . . ; the protection of the police against claims or disputes over lost or stolen property . . . ; and the protection of the police from potential danger." <i>Ante,</i> at 369.<sup>[7]</sup></blockquote>
<p>This suggestion is flagrantly misleading, however, because the record of this case explicitly belies any relevance of the last two concerns. In any event it is my view that none of these "needs," separately or together, can suffice to justify the inventory search procedure approved by the Court.</p>
<p>First, this search cannot be justified in any way as a safety measure, forthough the Court ignores itthe sole purpose given by the State for the Vermillion police's inventory procedure was to secure <i>valuables,</i> Record 75, 98. Nor is there any indication that the officer's search in this case was tailored in any way to safety concerns, or that ordinarily it is so circumscribed. Even aside from the actual basis for the police practice in this case, however, I do not believe that any blanket safety argument could justify a program of routine <span class="star-pagination">*390</span> searches of the scope permitted here. As MR. JUSTICE POWELL recognizes, ordinarily "there is little danger associated with impounding unsearched automobiles," <i>ante,</i> at 378.<sup>[8]</sup> Thus, while the safety rationale may not be entirely discounted when it is actually relied upon, it surely cannot justify the search of every car upon the basis of undifferentiated possibility of harm; on the contrary, such an intrusion could ordinarily be justified only in those individual cases where the officer's inspection was prompted by specific circumstances indicating the possibility <span class="star-pagination">*391</span> of a particular danger. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21, 27</a></span>; cf. <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#448" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 448</a></span> (1973).</p>
<p>Second, the Court suggests that the search for valuables in the closed glove compartment might be justified as a measure to protect the police against lost property claims. Again, this suggestion is belied by the record, sincealthough the Court declines to discuss itthe South Dakota Supreme Court's interpretation of state law explicitly absolves the police, as "gratuitous depositors," from any obligation beyond inventorying objects in plain view and locking the car. 89 S. D. , , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/#159" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152, 159</a></span> (1975).<sup>[9]</sup> Moreover, as MR. JUSTICE POWELL notes, <i>ante,</i> at 378-379, it may well be doubted that an inventory procedure would in any event work significantly to minimize the frustrations of false claims.<sup>[10]</sup></p>
<p>Finally, the Court suggests that the public interest in protecting valuables that may be found inside a closed compartment of an impounded car may justify the inventory procedure. I recognize the genuineness of this governmental interest in protecting property from pilferage. But even if I assume that the posting of a guard would be fiscally impossible as an alternative means to <span class="star-pagination">*392</span> the same protective end,<sup>[11]</sup> I cannot agree with the Court's conclusion. The Court's result authorizesindeed it appears to requirethe routine search of nearly every<sup>[12]</sup> car impounded.<sup>[13]</sup> In my view, the Constitution does not permit such searches as a matter of routine; absent specific consent, such a search is permissible only in exceptional circumstances of particular necessity.</p>
<p>It is at least clear that any owner might prohibit the police from executing a protective search of his impounded car, since by hypothesis the inventory is conducted for the owner's benefit. Moreover, it is obvious that not everyone whose car is impounded would want it to be searched. Respondent himself proves this; but <span class="star-pagination">*393</span> one need not carry contraband to prefer that the police not examine one's private possessions. Indeed, that preference is the premise of the Fourth Amendment. Nevertheless, according to the Court's result the law may presume that each owner in respondent's position consents to the search. I cannot agree. In my view, the Court's approach is squarely contrary to the law of consent;<sup>[14]</sup> it ignores the duty, in the absence of consent, to analyze in each individual case whether there is a need to search a particular car for the protection of its owner which is sufficient to outweigh the particular invasion. It is clear to me under established principles that in order to override the absence of explicit consent, such a search must at least be conditioned upon the fulfillment of two requirements.<sup>[15]</sup> First, there must be specific cause to believe that a search of the scope to be undertaken is necessary in order to preserve the integrity of particular valuable property threatened by the impoundment:</p>
<blockquote>"[I]n justifying the particular intrusion the police officer must be able to point to specific and articulable facts which . . . reasonably warrant that intrusion." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 21</a></span>.</blockquote>
<p>Such a requirement of "specificity in the information upon which police action is predicated is the central teaching of this Court's Fourth Amendment jurisprudence," <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">id.,</a></span></i> at 21 n. 18, for "[t]he basic purpose of this <span class="star-pagination">*394</span> Amendment, as recognized in countless decisions of this Court, is to safeguard the privacy and security of individuals against arbitrary invasions by governmental officials." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S., at 528</a></span>. Cf. <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#883" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 883-884</a></span> (1975); <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#448" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 448</a></span>; <i>Terry</i> v. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Ohio, supra,</i> at 27</a></span>. Second, even where a search might be appropriate, such an intrusion may only follow the exhaustion and failure of reasonable efforts under the circumstances to identify and reach the owner of the property in order to facilitate alternative means of security or to obtain his consent to the search, for in this context the right to refuse the search remains with the owner. Cf. <i>Bumper</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U. S. 543</a></span> (1968).<sup>[16]</sup></p>
<p>Because the record in this case shows that the procedures followed by the Vermillion police in searching respondent's car fall far short of these standards, in my view the search was impermissible and its fruits must be suppressed. First, so far as the record shows, the police in this case had no reason to believe that the glove compartment of the impounded car contained particular property of any substantial value. Moreover, the owner had apparently thought it adequate to protect whatever he left in the car overnight on the street in a business area simply to lock the car, and there is nothing in the record to show that the impoundment <span class="star-pagination">*395</span> lot would prove a less secure location against pilferage,<sup>[17]</sup> cf. <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#707" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d 699, 707</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#89" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84, 89</a></span> (1971), particularly when it would seem likely that the owner would claim his car and its contents promptly, at least if it contained valuables worth protecting.<sup>[18]</sup> Even if the police had cause to believe that the impounded car's glove compartment contained particular valuables, however, they made no effort to secure the owner's consent to the search. Although the Court relies, as it must, upon the fact that respondent was not present to make other arrangements for the care of his belongings, <i>ante,</i> at 375, in my view that is not the end of the inquiry. Here the police readily ascertained the ownership of the vehicle, Record 98-99, yet they searched it immediately without taking any steps to locate respondent and procure his consent to the inventory or advise him to make alternative arrangements to safeguard his property, <i>id.,</i> at 32, 72, 73, 79. Such a failure is inconsistent with the rationale that the inventory procedure is carried out for the benefit of the owner.</p>
<p>The Court's result in this case elevates the conservation of property interestsindeed mere possibilities of property interestsabove the privacy and security interests <span class="star-pagination">*396</span> protected by the Fourth Amendment. For this reason I dissent. On the remand it should be clear in any event that this Court's holding does not preclude a contrary resolution of this case or others involving the same issues under any applicable state law. See <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#726" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 726</a></span> (1975) (MARSHALL, J., dissenting).</p>
<p>Statement of MR. JUSTICE WHITE.</p>
<p>Although I do not subscribe to all of my Brother MARSHALL'S dissenting opinion, particularly some aspects of his discussion concerning the necessity for obtaining the consent of the car owner, I agree with most of his analysis and conclusions and consequently dissent from the judgment of the Court.</p>
<h2>NOTES</h2>
<p>[*]  Briefs of <i>amici curiae</i> urging reversal were filed by <i>Evelle J. Younger,</i> Attorney General, <i>Jack R. Winkler,</i> Chief Assistant Attorney General, <i>S. Clark Moore,</i> Assistant Attorney General, and <i>Kent L. Richland</i> and <i>Robert R. Anderson,</i> Deputy Attorneys General, for the State of California; by <i>Theodore L. Sendak,</i> Attorney General, and <i>Donald P. Bogard,</i> Executive Assistant Attorney General, for the State of Indiana; by <i>Toney Anaya,</i> Attorney General, and <i>Warren O. F. Harris,</i> Deputy Attorney General, for the State of New Mexico; and by <i>Wayne W. Schmidt</i> for Americans for Effective Law Enforcement, Inc.</p>
<p>[1]  At respondent's trial, the officer who conducted the inventory testified as follows:
</p>
<p>"Q. And why did you inventory this car?</p>
<p>"A. Mainly for safekeeping, because we have had a lot of trouble in the past of people getting into the impound lot and breaking into cars and stealing stuff out of them.</p>
<p>"Q. Do you know whether the vehicles that were broken into . . . were locked or unlocked?</p>
<p>"A. Both of them were locked, they would be locked." Record 74. In describing the impound lot, the officer stated:</p>
<p>"A. It's the old county highway yard. It has a wooden fence partially around part of it, and kind of a dilapidated wire fence, a makeshift fence." <i>Id.,</i> at 73.</p>
<p>[2]  In <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967), and <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967), the Court held that a warrant was required to effect an unconsented administrative entry into and inspection of private dwellings or commercial premises to ascertain health or safety conditions. In contrast, this procedure has never been held applicable to automobile inspections for safety purposes.</p>
<p>[3]  The New York Court of Appeals has noted that in New York City alone, 108,332 cars were towed away for traffic violations during 1969. <i>People</i> v. <i>Sullivan,</i> 29 N. Y. 2d 69, 71, <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#465" aria-description="Citation for case: People v. Sullivan">272 N. E. 2d 464, 465</a></span> (1971).</p>
<p>[4]  In contrast to state officials engaged in everyday caretaking functions:
</p>
<p>"The contact with vehicles by federal law enforcement officers usually, if not always, involves the detection or investigation of crimes unrelated to the operation of a vehicle." <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#440" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433, 440</a></span> (1973).</p>
<p>[5]  In analyzing the issue of reasonableness <i>vel non,</i> the courts have not sought to determine whether a protective inventory was justified by "probable cause." The standard of probable cause is peculiarly related to criminal investigations, not routine, noncriminal procedures. See generally Note, Warrantless Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span>, 850-851 (1974). The probable-cause approach is unhelpful when analysis centers upon the reasonableness of routine administrative caretaking functions, particularly when no claim is made that the protective procedures are a subterfuge for criminal investigations.
</p>
<p>In view of the noncriminal context of inventory searches, and the inapplicability in such a setting of the requirement of probable cause, courts have heldand quite correctlythat search warrants are not required, linked as the warrant requirement textually is to the probable-cause concept. We have frequently observed that the warrant requirement assures that legal inferences and conclusions as to probable cause will be drawn by a neutral magistrate unrelated to the criminal investigative-enforcement process. With respect to noninvestigative police inventories of automobiles lawfully within governmental custody, however, the policies underlying the warrant requirement, to which MR. JUSTICE POWELL refers, are inapplicable.</p>
<p>[6]  Given the benign noncriminal context of the intrusion, see <i>Wyman</i> v. <i>James,</i> <span class="citation" data-id="9424375"><a href="/opinion/108223/wyman-v-james/#317" aria-description="Citation for case: Wyman v. James">400 U. S. 309, 317</a></span> (1971), some courts have concluded that an inventory does not constitute a search for Fourth Amendment purposes. See, <i>e. g., </i><i>People</i> v. <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#77" aria-description="Citation for case: People v. Sullivan"><i>Sullivan, supra,</i> at 77</a></span>, <span class="citation" data-id="5526670"><a href="/opinion/5678725/people-v-sullivan/#469" aria-description="Citation for case: People v. Sullivan">272 N. E. 2d, at 469</a></span>; <i>People</i> v. <i>Willis,</i> <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">46 Mich. App. 436</a></span>, <span class="citation" data-id="2060145"><a href="/opinion/2060145/people-v-willis/" aria-description="Citation for case: People v. Willis">208 N. W. 2d 204</a></span> (1973); <i>State</i> v. <i>Wallen,</i> <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/#49" aria-description="Citation for case: State v. Wallen">185 Neb. 44, 49-50</a></span>, <span class="citation" data-id="1600787"><a href="/opinion/1600787/state-v-wallen/#376" aria-description="Citation for case: State v. Wallen">173 N. W. 2d 372, 376</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./399/912/">399 U. S. 912</a></span> (1970). Other courts have expressed doubts as to whether the intrusion is classifiable as a search. <i>State</i> v. <i>All,</i> 17 N. C. App. 284, 286, <span class="citation" data-id="1271156"><a href="/opinion/1271156/state-v-all/#772" aria-description="Citation for case: State v. All">193 S. E. 2d 770, 772</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/866/">414 U. S. 866</a></span> (1973). Petitioner, however, has expressly abandoned the contention that the inventory in this case is exempt from the Fourth Amendment standard of reasonableness. Tr. of Oral Arg. 5.</p>
<p>[7]  In <i><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">Cooper</a></span>,</i> the owner had been arrested on narcotics charges, and the car was taken into custody pursuant to the state forfeiture statute. The search was conducted several months before the forfeiture proceedings were actually instituted.</p>
<p>[8]  There was, of course, no certainty at the time of the search that forfeiture proceedings would ever be held. Accordingly, there was no reason for the police to assume automatically that the automobile would eventually be forfeited to the State. Indeed, as the California Court of Appeal stated, "[T]he instant record nowhere discloses that forfeiture proceedings were instituted in respect to defendant's car . . . ." <i>People</i> v. <i>Cooper,</i> <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#596" aria-description="Citation for case: People v. Cooper">234 Cal. App. 2d 587, 596</a></span>, <span class="citation" data-id="2201439"><a href="/opinion/2201439/people-v-cooper/#489" aria-description="Citation for case: People v. Cooper">44 Cal. Rptr. 483, 489</a></span> (1965). No reason would therefore appear to limit <i>Cooper</i> to an impoundment pursuant to a forfeiture statute.</p>
<p>[9]  The Court expressly noted that the legality of the inventory was not presented, since the evidence was discovered at the point when the officer was taking protective measures to secure the automobile from the elements. But the Court clearly held that the officer acted properly in opening the car for protective reasons.</p>
<p>[10]  The inventory was not unreasonable in scope. Respondent's motion to suppress in state court challenged the inventory only as to items inside the car not in plain view. But once the policeman was lawfully inside the car to secure the personal property in plain view, it was not unreasonable to open the unlocked glove compartment, to which vandals would have had ready and unobstructed access once inside the car.
</p>
<p>The "consent" theory advanced by the dissent rests on the assumption that the inventory is exclusively for the protection of the car owner. It is not. The protection of the municipality and public officers from claims of lost or stolen property and the protection of the public from vandals who might find a firearm, <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski</a></span></i><i>,</i> or as here, contraband drugs, are also crucial.</p>
<p>[1]  Routine inventories of automobiles intrude upon an area in which the private citizen has a "reasonable expectation of privacy." <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#360" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 360</a></span> (1967) (Harlan, J., concurring). Thus, despite their benign purpose, when conducted by government officials they constitute "searches" for purposes of the Fourth Amendment. See <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, 18 n. 15 (1968); <i>United States</i> v. <i>Lawson,</i> <span class="citation" data-id="314840"><a href="/opinion/314840/united-states-v-sam-meredith-lawson/" aria-description="Citation for case: United States v. Sam Meredith Lawson">487 F. 2d 468</a></span> (CA8 1973); <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#709" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d 699, 709-710</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#90" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84, 90-91</a></span> (1971) (en banc). Cf. <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#591" aria-description="Citation for case: Cardwell v. Lewis">417 U. S. 583, 591</a></span> (1974) (plurality opinion).</p>
<p>[2]  The principal decisions relied on by the State to justify the inventory search in this case, <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">390 U. S. 234</a></span> (1968); <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967); and <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973), each relied in part on significant factors not found here. <i><span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> only involved an application of the "plain view" doctrine. In <i>Cooper</i> the Court validated an automobile search that took place one week after the vehicle was impounded on the theory that the police had a possessory interest in the car based on a state forfeiture statute requiring them to retain it some four months until the forfeiture sale. See <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61-62</a></span>. Finally, in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> the Court held that the search of an automobile trunk "which the officer reasonably believed to contain a gun" was not unreasonable within the meaning of the Fourth and Fourteenth Amendments. 413 U. S., at 448. See also <i>id.,</i> at 436-437. The police in a typical inventory search case, however, will have no reasonable belief as to the particular automobile's contents. And, although the police in this case knew with certainty that there were items of personal property within the exposed interior of the car <i>i. e.,</i> the watch on the dashboardsee <i>ante,</i> at 366, this information alone did not, in the circumstances of this case, provide additional justification for the search of the closed console glove compartment in which the contraband was discovered.</p>
<p>[3]  The interest in protecting the police from liability for lost or stolen property is not relevant in this case. Respondent's motion to suppress was limited to items inside the automobile not in plain view. And, the Supreme Court of South Dakota here held that the removal of objects in plain view, and the closing of windows and locking of doors, satisfied any duty the police department owed the automobile's owner to protect property in police possession. 89 S. D. , , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/#159" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152, 159</a></span> (1975).</p>
<p>[4]  See <i>Mozzetti</i> v. <i>Superior Court, supra,</i> at 709-710, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#90" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d, at 90-91</a></span>.</p>
<p>[5]  See Note, Warrantless Searches and Seizures of Automobiles, <span class="citation no-link">87 Harv. L. Rev. 835</span>, 853 (1974).</p>
<p>[6]  A complete "inventory report" is required of all vehicles impounded by the Vermillion Police Department. The standard inventory consists of a survey of the vehicle's exteriorwindows, fenders, trunk, and hoodapparently for damage, and its interior, to locate "valuables" for storage. As part of each inventory a standard report form is completed. The report in this case listed the items discovered in both the automobile's interior and the unlocked glove compartment. The only notation regarding the trunk was that it was locked. A police officer testified that all impounded vehicles are searched, that the search always includes the glove compartment, and that the trunk had not been searched in this case because it was locked. See Record 33-34, 73-79.</p>
<p>[7]  As part of their inventory search the police may discover materials such as letters or checkbooks that "touch upon intimate areas of an individual's personal affairs," and "reveal much about a person's activities, associations, and beliefs." <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#78" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 78-79</a></span> (1974) (POWELL, J., concurring). See also <i>Fisher</i> v. <i>United States,</i> <span class="citation" data-id="9426372"><a href="/opinion/109432/fisher-v-united-states/" aria-description="Citation for case: Fisher v. United States">425 U. S. 391</a></span>, 401 n. 7 (1976). In this case the police found, <i>inter alia,</i> "miscellaneous papers," a checkbook, an installment loan book, and a social security status card. Record 77. There is, however, no evidence in the record that in carrying out their established inventory duties the Vermillion police do other than search for and remove for storage such property without examining its contents.</p>
<p>[8]  The Amendment provides that
</p>
<p>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized."</p>
<p>[9]  This difference turns primarily on the mobility of the automobile and the impracticability of obtaining a warrant in many circumstances, <i>e. g., </i><i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#153" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 153-154</a></span> (1925). The lesser expectation of privacy in an automobile also is important. See <i>United States</i> v. <i>Ortiz,</i> <span class="citation" data-id="9426199"><a href="/opinion/109312/united-states-v-ortiz/" aria-description="Citation for case: United States v. Ortiz">422 U. S. 891</a></span>, 896 n. 2 (1975); <i>Cardwell</i> v. <i>Lewis,</i> <span class="citation" data-id="9425767"><a href="/opinion/109069/cardwell-v-lewis/#590" aria-description="Citation for case: Cardwell v. Lewis">417 U. S., at 590</a></span>; <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#279" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 279</a></span> (1973) (POWELL, J., concurring). See <i>Cady</i> v. <i>Dombrowski,</i> <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#441" aria-description="Citation for case: Cady v. Dombrowski">413 U. S., at 441-442</a></span>.</p>
<p>[10]  See, <i>e. g., </i><i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968); <i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-300</a></span> (1967); <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/" aria-description="Citation for case: Cooper v. California">386 U. S. 58</a></span> (1967); <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 174-177</a></span> (1949); <i>Carroll</i> v. <i>United States, supra,</i> at 153, 156. See also <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#454" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 454-456</a></span> (1948); <i>United States</i> v. <i>Mapp,</i> <span class="citation" data-id="310049"><a href="/opinion/310049/united-states-v-edward-mapp-aka-sonny-woods/#76" aria-description="Citation for case: United States v. Edward Mapp, A/K/A Sonny Woods">476 F. 2d 67, 76</a></span> (CA2 1973) (listing then-recognized exceptions to warrant requirement: (i) hot pursuit; (ii) plain-view doctrine; (iii) emergency situation; (iv) automobile search; (v) consent; and (vi) incident to arrest).</p>
<p>[11]  In this case, for example, the officer who conducted the search testified that the offending automobile was towed to the city impound lot after a second ticket had been issued for a parking violation. The officer further testified that all vehicles taken to the lot are searched in accordance with a "standard inventory sheet" and "all items [discovered in the vehicles] are removed for safekeeping." Record 74. See n. 6, <i>supra.</i></p>
<p>[1]  The Court does not consider, however, whether the police might open and search the glove compartment if it is locked, or whether the police might search a locked trunk or other compartment.</p>
<p>[2]  I agree with MR. JUSTICE POWELL's conclusion, <i>ante,</i> at 377 n. 1, that, as petitioner conceded, Tr. of Oral Arg. 5, the examination of the closed glove compartment in this case is a "search." See <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#530" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 530</a></span> (1967): "It is surely anomalous to say that the individual and his private property are fully protected by the Fourth Amendment only when the individual is suspected of criminal behavior." See also <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967), quoted in n. 5, <i>infra.</i> Indeed, the Court recognized in <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9423622"><a href="/opinion/107625/harris-v-united-states/#236" aria-description="Citation for case: Harris v. United States">390 U. S. 234, 236</a></span> (1968), that the procedure invoked here would constitute a search for Fourth Amendment purposes.</p>
<p>[3]  This is, of course, "probable cause in the sense of specific knowledge about a particular automobile." <i>Almeida-Sanchez</i> v. <i>United States,</i> <span class="citation" data-id="9425395"><a href="/opinion/108845/almeida-sanchez-v-united-states/#281" aria-description="Citation for case: Almeida-Sanchez v. United States">413 U. S. 266, 281</a></span> (1973) (POWELL, J., concurring).</p>
<p>[4]  In its opinion below, the Supreme Court of South Dakota stated that in its view the police were constitutionally justified in entering the car to remove, list, and secure objects in plain view from the outside of the car. 89 S. D. , , <span class="citation" data-id="9573888"><a href="/opinion/1311789/state-v-opperman/#158" aria-description="Citation for case: State v. Opperman">228 N. W. 2d 152, 158-159</a></span> (1975). This issue is not presented on certiorari here.
</p>
<p>Contrary to the Court's assertion, however, <i>ante,</i> at 375-376, the search of respondent's car was not in any way "prompted by the presence in plain view of a number of valuables inside the car." In fact, the record plainly states that every vehicle taken to the city impound lot was inventoried, Record 33, 74, 75, and that as a matter of "standard procedure," "every inventory search" would involve entry into the car's closed glove compartment. <i>Id.,</i> at 43, 44. See also Tr. of Oral Arg. 7. In any case, as MR. JUSTICE POWELL recognizes, <i>ante,</i> at 377-378, n. 2, entry to remove plain-view articles from the car could not justify a further search into the car's closed areas. Cf. <i>Chimel</i> v. <i>California,</i> <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 763, 764-768</a></span> (1969). Despite the Court's confusion on this pointfurther reflected by its discussion of <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d 699</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d 84</a></span> (1971), <i>ante,</i> at 371, and its reliance on state and lower federal-court cases approving nothing more than inventorying of plain-view items, <i>e. g., </i><i>Barker</i> v. <i>Johnson,</i> <span class="citation" data-id="313477"><a href="/opinion/313477/daniel-barker-v-dale-johnson/" aria-description="Citation for case: Daniel Barker v. Dale Johnson">484 F. 2d 941</a></span> (CA6 1973); <i>United States</i> v. <i>Mitchell,</i> <span class="citation" data-id="9458066"><a href="/opinion/302928/united-states-v-william-elmer-mitchell/" aria-description="Citation for case: United States v. William Elmer Mitchell">458 F. 2d 960</a></span> (CA9 1972); <i>United States</i> v. <i>Fuller,</i> <span class="citation" data-id="1868897"><a href="/opinion/1868897/united-states-v-fuller/" aria-description="Citation for case: United States v. Fuller">277 F. Supp. 97</a></span> (DC 1967), conviction aff'd, 139 U. S. App. D. C. 375, <span class="citation" data-id="292850"><a href="/opinion/292850/morris-fuller-v-united-states/" aria-description="Citation for case: Morris Fuller v. United States">433 F. 2d 533</a></span> (1970); <i>State</i> v. <i>Tully,</i> <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/" aria-description="Citation for case: State v. Tully">166 Conn. 126</a></span>, <span class="citation" data-id="9757435"><a href="/opinion/2350702/state-v-tully/" aria-description="Citation for case: State v. Tully">348 A. 2d 603</a></span> (1974); <i>State</i> v. <i>Achter,</i> <span class="citation" data-id="1770477"><a href="/opinion/1770477/state-v-achter/" aria-description="Citation for case: State v. Achter">512 S. W. 2d 894</a></span> (Mo. Ct. App. 1974); <i>State</i> v. <i>All,</i> 17 N. C. App. 284, <span class="citation" data-id="1271156"><a href="/opinion/1271156/state-v-all/" aria-description="Citation for case: State v. All">193 S. E. 2d 770</a></span>, cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./414/866/">414 U. S. 866</a></span> (1973)I must conclude that the Court's holding also permits the intrusion into a car and its console even in the absence of articles in plain view.</p>
<p>[5]  Moreover, as the Court observed in <i>Cooper</i> v. <i>California, supra,</i> at 61: " `[L]awful custody of an automobile does not of itself dispense with constitutional requirements of searches thereafter made of it.' "</p>
<p>[6]  It would be wholly unrealistic to say that there is no reasonable and actual expectation in maintaining the privacy of closed compartments of a locked automobile, when it is customary for people in this day to carry their most personal and private papers and effects in their automobiles from time to time. Cf. <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 352</a></span> (1967) (opinion of the Court); <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States"><i>id.,</i> at 361</a></span> (Harlan, J., concurring). Indeed, this fact is implicit in the very basis of the Court's holdingthat such compartments may contain valuables in need of safeguarding.
</p>
<p>MR. JUSTICE POWELL observes, <i>ante,</i> at 380, and n. 7, that the police would not be justified in sifting through papers secured under the procedure employed here. I agree with this, and I note that the Court's opinion does not authorize the inspection of suitcases, boxes, or other containers which might themselves be sealed, removed, and secured without further intrusion. See, <i>e. g., </i><i>United States</i> v. <i>Lawson,</i> <span class="citation" data-id="314840"><a href="/opinion/314840/united-states-v-sam-meredith-lawson/" aria-description="Citation for case: United States v. Sam Meredith Lawson">487 F. 2d 468</a></span> (CA8 1973); <i>State</i> v. <i>McDougal,</i> <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/" aria-description="Citation for case: State v. McDougal">68 Wis. 2d 399</a></span>, <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/" aria-description="Citation for case: State v. McDougal">228 N. W. 2d 671</a></span> (1975); <i>Mozzetti</i> v. <i>Superior Court, supra</i><i>.</i> But this limitation does not remedy the Fourth Amendment intrusion when the simple inventorying of closed areas discloses tokens, literature, medicines, or other things which on their face may "reveal much about a person's activities, associations, and beliefs," <i>California Bankers Assn.</i> v. <i>Shultz,</i> <span class="citation" data-id="9425671"><a href="/opinion/109005/california-bankers-assn-v-shultz/#78" aria-description="Citation for case: California Bankers Assn. v. Shultz">416 U. S. 21, 78-79</a></span> (1974) (POWELL, J., concurring).</p>
<p>[7]  The Court also observes that "[i]n addition, police frequently attempt to determine whether a vehicle has been stolen and thereafter abandoned." <i>Ante,</i> at 369. The Court places no reliance on this concern in this case, however, nor could it. There is no suggestion that the police suspected that respondent's car was stolen, or that their search was directed at, or stopped with, a determination of the car's ownership. Indeed, although the police readily identified the car as respondent's, Record 98-99, the record does not show that they ever sought to contact him.</p>
<p>[8]  The very premise of the State's chief argument, that the cars must be searched in order to protect valuables because no guard is posted around the vehicles, itself belies the argument that they must be searched at the city lot in order to protect the police there. These circumstances alone suffice to distinguish the dicta from <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S., at 61-62</a></span>, recited by the Court, <i>ante,</i> at 373.
</p>
<p>The Court suggests a further "crucial" justification for the search in this case: "protection of the <i>public</i> from vandals who might find a firearm, <i>Cady</i> v. <i>Dombrowski,</i> [<span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">413 U. S. 433</a></span> (1973)], or as here, contraband drugs" (emphasis added). <i>Ante,</i> at 376 n. 10. This rationale, too, is absolutely without support in this record. There is simply no indication the police were looking for dangerous items. Indeed, even though the police found shotgun shells in the interior of the car, they never opened the trunk to determine whether it might contain a shotgun. Cf. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady, supra</a></span></i><i>.</i> Aside from this, the suggestion is simply untenable as a matter of law. If this asserted rationale justifies search of all impounded automobiles, it must logically also justify the search of <i>all</i> automobiles, whether impounded or not, located in a similar area, for the argument is not based upon the custodial role of the police. See also <i>Cooper</i> v. <i>California, supra,</i> at 61, quoted in n. 5, <i>supra.</i> But this Court has never permitted the search of any car or home on the mere undifferentiated assumption that it might be vandalized and the vandals might find dangerous weapons or substances. Certainly <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski</a></span></i><i>,</i> permitting a limited search of a wrecked automobile where, <i>inter alia,</i> the police had a reasonable belief that the car contained a specific firearm, 413 U. S., at 448, does not so hold.</p>
<p>[9]  Even were the State to impose a higher standard of custodial responsibility upon the police, however, it is equally clear that such a requirement must be read in light of the Fourth Amendment's pre-eminence to require protective measures other than interior examination of closed areas.</p>
<p>[10]  Indeed, if such claims can be deterred at all, they might more effectively be deterred by sealing the doors and trunk of the car so that an unbroken seal would certify that the car had not been opened during custody. See <i>Cabbler</i> v. <i>Superintendent,</i> <span class="citation" data-id="2353003"><a href="/opinion/2353003/cabbler-v-superintendent-virginia-state-penitentiary/#700" aria-description="Citation for case: Cabbler v. Superintendent, Virginia State Penitentiary">374 F. Supp. 690, 700</a></span> (ED Va. 1974), rev'd, <span class="citation" data-id="332335"><a href="/opinion/332335/herbert-w-cabbler-v-superintendent-virginia-state-penitentiary/" aria-description="Citation for case: Herbert W. Cabbler v. Superintendent, Virginia State...">528 F. 2d 1142</a></span> (CA4 1975), cert. pending, No. 75-1463.</p>
<p>[11]  I do not believe, however, that the Court is entitled to make this assumption, there being no such indication in the record. Cf. <i>Cady</i> v. <span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/#447" aria-description="Citation for case: Cady v. Dombrowski"><i>Dombrowski, supra,</i> at 447</a></span>.</p>
<p>[12]  The Court makes clear, <i>ante,</i> at 375, that the police may not proceed to search an impounded car if the owner is able to make other arrangements for the safekeeping of his belongings. Additionally, while the Court does not require consent before a search, it does not hold that the police may proceed with such a search in the face of the owner's denial of permission. In my view, if the owner of the vehicle is in police custody or otherwise in communication with the police, his consent to the inventory is prerequisite to an inventory search. See <i>Cabbler</i> v. <i>Superintendent, supra,</i> at 700; cf. <i>State</i> v. <i>McDougal,</i> <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/#413" aria-description="Citation for case: State v. McDougal">68 Wis. 2d, at 413</a></span>, <span class="citation" data-id="9574032"><a href="/opinion/1312019/state-v-mcdougal/#678" aria-description="Citation for case: State v. McDougal">228 N. W. 2d, at 678</a></span>; <i>Mozzetti</i> v. <i>Superior Court,</i> <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#708" aria-description="Citation for case: Mozzetti v. Superior Court">4 Cal. 3d, at 708</a></span>, <span class="citation" data-id="9551815"><a href="/opinion/1185375/mozzetti-v-superior-court/#89" aria-description="Citation for case: Mozzetti v. Superior Court">484 P. 2d, at 89</a></span>.</p>
<p>[13]  In so requiring, the Court appears to recognize that a search of some, but not all, cars which there is no specific cause to believe contain valuables would itself belie any asserted property-securing purpose.
</p>
<p>The Court makes much of the fact that the search here was a routine procedure, and attempts to analogize <i>Cady</i> v. <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Dombrowski</a></span></i><i>.</i> But it is quite clear that the routine in <i><span class="citation" data-id="9425411"><a href="/opinion/108850/cady-v-dombrowski/" aria-description="Citation for case: Cady v. Dombrowski">Cady</a></span></i> was only to search where there was a reasonable belief that the car contained a dangerous weapon, 413 U. S., at 443; see <i>Dombrowski</i> v. <i>Cady,</i> <span class="citation" data-id="8783591"><a href="/opinion/8799464/dombrowski-v-cady/#532" aria-description="Citation for case: Dombrowski v. Cady">319 F. Supp. 530, 532</a></span> (ED Wis. 1970), not, as here, to search every car in custody without particular cause.</p>
<p>[14]  Even if it may be true that many persons would ordinarily consent to a protective inventory of their car upon its impoundment, this fact is not dispositive since even a majority lacks authority to consent to the search of <i>all</i> cars in order to assure the search of theirs. Cf. <i>United States</i> v. <i>Matlock,</i> <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/#171" aria-description="Citation for case: United States v. Matlock">415 U. S. 164, 171</a></span> (1974); <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span> (1964).</p>
<p>[15]  I need not consider here whether a warrant would be required in such a case.</p>
<p>[16]  Additionally, although not relevant on this record, since the inventory procedure is premised upon benefit to the owner, it cannot be executed in any case in which there is reason to believe the owner would prefer to forgo it. This principle, which is fully consistent with the Court's result today, requires, for example, that when the police harbor suspicions (amounting to less than probable cause) that evidence or contraband may be found inside the automobile, they may not inventory it, for they must presume that the owner would refuse to permit the search.</p>
<p>[17]  While evidence at the suppression hearing suggested that the inventory procedures were prompted by past thefts at the impound lot, the testimony refers to only two such thefts, see <i>ante,</i> at 366 n. 1, over an undisclosed period of time. There is no reason on this record to believe that the likelihood of pilferage at the lot was higher or lower than that on the street where respondent left his car with valuables in plain view inside. Moreover, the failure of the police to secure such frequently stolen items as the car's battery, suggests that the risk of loss from the impoundment was not in fact thought severe.</p>
<p>[18]  In fact respondent claimed his possessions about five hours after his car was removed from the street. Record 39, 93.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Spano v. New York.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Spano v. New York"
type: case
citation: "360 U.S. 315 (1959)"
parallel_cite: "79 S. Ct. 1202; 3 L. Ed. 2d 1265"
neutral_cite: 1959 U.S. LEXIS 751
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1959
date_decided: 1959-06-22
docket: 326
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1959-06-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Spano v. New York
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105917/spano-v-new-york/"
  cluster_id: 105917
  opinion_id: 105917
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brown v. Mississippi]]", "[[Chambers v. Florida]]", "[[Ashcraft v. Tennessee]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "confession", "voluntariness", "due-process"]
holding: "A confession produced by psychological pressure — here a friend's feigned distress plus persistent overnight questioning of a suspect…"
lake:
  record_id: Spano v. New York
  status: verified
  projected_at: 2026-07-06
---

# Spano v. New York

*360 U.S. 315 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Spano, a foreign-born man of limited education, was indicted for murder and surrendered with his retained lawyer, who instructed him to remain silent. Over an eight-hour overnight interrogation, police refused his repeated requests to consult his lawyer and enlisted a rookie-officer acquaintance, Bruno, to falsely tell Spano that Spano's call had jeopardized Bruno's job and family—until Spano confessed.

## Issue
Whether a confession obtained by prolonged overnight questioning and a false-friend appeal, after the suspect was indicted, had counsel, and asked to remain silent, was voluntary.

## Rule
Voluntariness is judged on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], and a confession produced by official pressure is involuntary. "We conclude that petitioner's will was overborne by official pressure, fatigue and sympathy falsely aroused, after considering all the facts in their post-indictment setting." — 360 U.S. at 323. ^pin-323

## Application
The combination of persistent overnight questioning, the repeated denial of Spano's requests to consult his lawyer, and the calculated use of Bruno's feigned distress overbore Spano's will. On those facts the confession was involuntary, and its admission violated due process, so the conviction was reversed.

## Conclusion
The confession was involuntary under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]]; the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Part of the due-process voluntariness line ([[Brown v. Mississippi]], [[Chambers v. Florida]], [[Ashcraft v. Tennessee]]); [[Colorado v. Connelly]] later held that coercive police activity is a necessary predicate to an involuntariness finding.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Spano v. New York*, 360 U.S. 315 (1959) — https://www.courtlistener.com/opinion/105917/spano-v-new-york/ — pinpoint: 323.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e5a02d9a9fa32bcc", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Spano v. New York"}, "payload": {"all": [{"cite": "360 U.S. 315", "page": "315", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "360"}, {"cite": "79 S. Ct. 1202", "page": "1202", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "79"}, {"cite": "3 L. Ed. 2d 1265", "page": "1265", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "3"}, {"cite": "1959 U.S. LEXIS 751", "page": "751", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1959"}], "display": "360 U.S. 315", "official": {"cite": "360 U.S. 315", "page": "315", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "360"}, "official_selection_present": true, "record_id": "Spano v. New York"}}
{"assertion_id": "d3d3d52177cb5ff6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-323", "record_id": "Spano v. New York"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-323", "pinpoint_status": "slip-only", "quote": "--- # Spano v. New York *360 U.S. 315 (1959)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Spano, a foreign-born man of limited education, was indicted for murder and surrendered with his retained lawyer, who instructed him to remain silent. Over an eight-hour overnight interrogation, police refused his repeated requests to consult his lawyer and enlisted a rookie-officer acquaintance, Bruno, to falsely tell Spano that Spano's call had jeopardized Bruno's job and family—until Spano confessed. ## Issue Whether a confession obtained by prolonged overnight questioning and a false-friend appeal, after the suspect was indicted, had counsel, and asked to remain silent, was voluntary. ## Rule Voluntariness is judged on the totality of the circumstances, and a confession produced by official pressure is involuntary.", "quote_fidelity": "mismatch", "record_id": "Spano v. New York", "star_marker": null}}
{"assertion_id": "aec2c90af9fd6210", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Spano v. New York"}, "payload": {"as_of_content": "1959-06-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Spano v. New York", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Spano v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Spano v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Spano v. New York",
    "case_name_short": "Spano",
    "case_name_full": "Spano v. New York",
    "input_case_name": "Spano v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1959-06-22",
    "year": 1959,
    "docket": "326",
    "cluster_id": 105917,
    "lead_opinion_id": 105917,
    "sibling_ids": [
      105917,
      9421842,
      9421843,
      9421844
    ],
    "absolute_url": "/opinion/105917/spano-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "360 U.S. 315",
      "volume": "360",
      "reporter": "U.S.",
      "page": "315",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "79 S. Ct. 1202",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1265",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1265",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1959 U.S. LEXIS 751",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "751",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "360 U.S. 315",
        "volume": "360",
        "reporter": "U.S.",
        "page": "315",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "79 S. Ct. 1202",
        "volume": "79",
        "reporter": "S. Ct.",
        "page": "1202",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 L. Ed. 2d 1265",
        "volume": "3",
        "reporter": "L. Ed. 2d",
        "page": "1265",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1959 U.S. LEXIS 751",
        "volume": "1959",
        "reporter": "U.S. LEXIS",
        "page": "751",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "360 U.S. 315",
    "official_selection": {
      "court_class": "scotus",
      "selected": "360 U.S. 315",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-323",
      "page": null,
      "quote": "--- # Spano v. New York *360 U.S. 315 (1959)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Spano, a foreign-born man of limited education, was indicted for murder and surrendered with his retained lawyer, who instructed him to remain silent. Over an eight-hour overnight interrogation, police refused his repeated requests to consult his lawyer and enlisted a rookie-officer acquaintance, Bruno, to falsely tell Spano that Spano's call had jeopardized Bruno's job and family\u2014until Spano confessed. ## Issue Whether a confession obtained by prolonged overnight questioning and a false-friend appeal, after the suspect was indicted, had counsel, and asked to remain silent, was voluntary. ## Rule Voluntariness is judged on the totality of the circumstances, and a confession produced by official pressure is involuntary.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1959-06-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Spano v. New York",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Jalonte Little v. United States",
          "cluster_id": 3153940,
          "cite": [
            "125 A.3d 1119",
            "2015 D.C. App. LEXIS 526"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
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
        "journal_ref": "Spano v. New York:lane1_negative"
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
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Sawyer",
          "cluster_id": 2521466,
          "cite": [
            "2004 OK CR 22",
            "92 P.3d 707",
            "2004 WL 1244992"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gomes v. State",
          "cluster_id": 2342281,
          "cite": [
            "9 S.W.3d 373",
            "1999 WL 1080989"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Riley v. Dorton",
          "cluster_id": 2966500,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zuliani v. State",
          "cluster_id": 2372052,
          "cite": [
            "903 S.W.2d 812",
            "1995 WL 410841"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Knotts",
          "cluster_id": 3990639,
          "cite": [
            "677 N.E.2d 358",
            "111 Ohio App. 3d 753"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Russell Ledbetter v. Ron Edwards, Warden",
          "cluster_id": 678531,
          "cite": [
            "35 F.3d 1062",
            "1994 U.S. App. LEXIS 26229",
            "1994 WL 511213"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane1_negative"
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
        "journal_ref": "Spano v. New York:lane1_negative"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Chapman v. California",
          "cluster_id": 107359,
          "cite": [
            "17 L. Ed. 2d 705",
            "87 S. Ct. 824",
            "386 U.S. 18",
            "1967 U.S. LEXIS 2198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Fulminante",
          "cluster_id": 112566,
          "cite": [
            "113 L. Ed. 2d 302",
            "111 S. Ct. 1246",
            "499 U.S. 279",
            "1991 U.S. LEXIS 1854"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Massiah v. United States",
          "cluster_id": 106822,
          "cite": [
            "12 L. Ed. 2d 246",
            "84 S. Ct. 1199",
            "377 U.S. 201",
            "1964 U.S. LEXIS 1277"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ker v. California",
          "cluster_id": 106641,
          "cite": [
            "10 L. Ed. 2d 726",
            "83 S. Ct. 1623",
            "374 U.S. 23",
            "1963 U.S. LEXIS 2473",
            "24 Ohio Op. 2d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nix v. Williams",
          "cluster_id": 111204,
          "cite": [
            "81 L. Ed. 2d 377",
            "104 S. Ct. 2501",
            "467 U.S. 431",
            "1984 U.S. LEXIS 101",
            "52 U.S.L.W. 4732"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. New Jersey",
          "cluster_id": 107260,
          "cite": [
            "16 L. Ed. 2d 882",
            "86 S. Ct. 1772",
            "384 U.S. 719",
            "1966 U.S. LEXIS 1127",
            "36 Ohio Op. 2d 439",
            "8 Ohio Misc. 324"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kirby v. Illinois",
          "cluster_id": 108554,
          "cite": [
            "32 L. Ed. 2d 411",
            "92 S. Ct. 1877",
            "406 U.S. 682",
            "1972 U.S. LEXIS 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kastigar v. United States",
          "cluster_id": 108541,
          "cite": [
            "32 L. Ed. 2d 212",
            "92 S. Ct. 1653",
            "406 U.S. 441",
            "1972 U.S. LEXIS 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Frye",
          "cluster_id": 626055,
          "cite": [
            "182 L. Ed. 2d 379",
            "132 S. Ct. 1399",
            "566 U.S. 134",
            "2012 U.S. LEXIS 2321"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lego v. Twomey",
          "cluster_id": 108429,
          "cite": [
            "30 L. Ed. 2d 618",
            "92 S. Ct. 619",
            "404 U.S. 477",
            "1972 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Waterfront Commission of New York Harbor",
          "cluster_id": 106864,
          "cite": [
            "12 L. Ed. 2d 678",
            "84 S. Ct. 1594",
            "378 U.S. 52",
            "1964 U.S. LEXIS 2229",
            "56 L.R.R.M. (BNA) 2544"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rogers v. Richmond",
          "cluster_id": 106192,
          "cite": [
            "5 L. Ed. 2d 760",
            "81 S. Ct. 735",
            "365 U.S. 534",
            "1961 U.S. LEXIS 1494"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
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
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maine v. Moulton",
          "cluster_id": 111546,
          "cite": [
            "88 L. Ed. 2d 481",
            "106 S. Ct. 477",
            "474 U.S. 159",
            "1985 U.S. LEXIS 147",
            "54 U.S.L.W. 4039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kuhlmann v. Wilson",
          "cluster_id": 111726,
          "cite": [
            "91 L. Ed. 2d 364",
            "106 S. Ct. 2616",
            "477 U.S. 436",
            "1986 U.S. LEXIS 65",
            "54 U.S.L.W. 4809"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Spano v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NjkyMDMyMDAwMDAmcz0xNzkzODc3JnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105917+OR+9421842+OR+9421843+OR+9421844%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 10,
        "triage_snippet_classified": 190
      },
      "lane2_top_cited": {
        "query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03MDEmcz0xMTIzODUmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105917+OR+9421842+OR+9421843+OR+9421844%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844)",
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
    "complete_query": "cites:(105917 OR 9421842 OR 9421843 OR 9421844)",
    "indexed_citing_opinions": 763,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105917,
        "count": 720,
        "count_source": "search"
      },
      {
        "opinion_id": 9421842,
        "count": 71,
        "count_source": "search"
      },
      {
        "opinion_id": 9421843,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9421844,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1164,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/spano-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjYzODczMjQmcz00NjUwNTM5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105917+OR+9421842+OR+9421843+OR+9421844%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105917,
        "cited_id": 102407,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103368,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104497,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105149,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105241,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 105750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105917,
        "cited_id": 1236300,
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
    "date_created": "2026-07-05T20:13:21Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T20:13:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T20:13:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T20:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T20:13:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Spano v. New York

```
<div>
<center><b><span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U.S. 315</a></span> (1959)</b></center>
<center><h1>SPANO<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 582.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 27, 1959.</center>
<center>Decided June 22, 1959.</center>
CERTIORARI TO THE COURT OF APPEALS OF NEW YORK.
<p><i>Herbert S. Siegal</i> argued the cause for petitioner. With him on the brief was <i>Rita D. Schechter.</i></p>
<p><i>Irving Anolik</i> argued the cause for respondent. With him on the brief were <i>Daniel V. Sullivan</i> and <i>Walter E. Dillon.</i></p>
<p>MR. CHIEF JUSTICE WARREN delivered the opinion of the Court.</p>
<p>This is another in the long line of cases presenting the question whether a confession was properly admitted into evidence under the Fourteenth Amendment. As in all such cases, we are forced to resolve a conflict between two fundamental interests of society; its interest in prompt and efficient law enforcement, and its interest in preventing the rights of its individual members from being abridged by unconstitutional methods of law enforcement. <span class="star-pagination">*316</span> Because of the delicate nature of the constitutional determination which we must make, we cannot escape the responsibility of making our own examination of the record. <i>Norris</i> v. <i>Alabama,</i> <span class="citation" data-id="102407"><a href="/opinion/102407/norris-v-alabama/" aria-description="Citation for case: Norris v. Alabama">294 U. S. 587</a></span>.</p>
<p>The State's evidence reveals the following: Petitioner Vincent Joseph Spano is a derivative citizen of this country, having been born in Messina, Italy. He was 25 years old at the time of the shooting in question and had graduated from junior high school. He had a record of regular employment. The shooting took place on January 22, 1957.</p>
<p>On that day, petitioner was drinking in a bar. The decedent, a former professional boxer weighing almost 200 pounds who had fought in Madison Square Garden, took some of petitioner's money from the bar. Petitioner followed him out of the bar to recover it. A fight ensued, with the decedent knocking petitioner down and then kicking him in the head three or four times. Shock from the force of these blows caused petitioner to vomit. After the bartender applied some ice to his head, petitioner left the bar, walked to his apartment, secured a gun, and walked eight or nine blocks to a candy store where the decedent was frequently to be found. He entered the store in which decedent, three friends of decedent, at least two of whom were ex-convicts, and a boy who was supervising the store were present. He fired five shots, two of which entered the decedent's body, causing his death. The boy was the only eyewitness; the three friends of decedent did not see the person who fired the shot. Petitioner then disappeared for the next week or so.</p>
<p>On February 1, 1957, the Bronx County Grand Jury returned an indictment for first-degree murder against petitioner. Accordingly, a bench warrant was issued for his arrest, commanding that he be forthwith brought before the court to answer the indictment, or, if the court had adjourned for the term, that he be delivered into the <span class="star-pagination">*317</span> custody of the Sheriff of Bronx County. See N. Y. Code Crim. Proc. § 301.</p>
<p>On February 3, 1957, petitioner called one Gaspar Bruno, a close friend of 8 or 10 years' standing who had attended school with him. Bruno was a fledgling police officer, having at that time not yet finished attending police academy. According to Bruno's testimony, petitioner told him "that he took a terrific beating, that the deceased hurt him real bad and he dropped him a couple of times and he was dazed; he didn't know what he was doing and that he went and shot at him." Petitioner told Bruno that he intended to get a lawyer and give himself up. Bruno relayed this information to his superiors.</p>
<p>The following day, February 4, at 7:10 p. m., petitioner, accompanied by counsel, surrendered himself to the authorities in front of the Bronx County Building, where both the office of the Assistant District Attorney who ultimately prosecuted his case and the courtroom in which he was ultimately tried were located. His attorney had cautioned him to answer no questions, and left him in the custody of the officers. He was promptly taken to the office of the Assistant District Attorney and at 7:15 p. m. the questioning began, being conducted by Assistant District Attorney Goldsmith, Lt. Gannon, Detectives Farrell, Lehrer and Motta, and Sgt. Clarke. The record reveals that the questioning was both persistent and continuous. Petitioner, in accordance with his attorney's instructions, steadfastly refused to answer. Detective Motta testified: "He refused to talk to me." "He just looked up to the ceiling and refused to talk to me." Detective Farrell testified:</p>
<blockquote>"Q. And you started to interrogate him?</blockquote>
<blockquote>"A. That is right.</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. What did he say?</blockquote>
<blockquote>
<span class="star-pagination">*318</span> "A. He said `you would have to see my attorney. I tell you nothing but my name."</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Did you continue to examine him?</blockquote>
<blockquote>"A. Verbally, yes, sir."</blockquote>
<p>He asked one officer, Detective Ciccone, if he could speak to his attorney, but that request was denied. Detective Ciccone testified that he could not find the attorney's name in the telephone book.<sup>[1]</sup> He was given two sandwiches, coffee and cake at 11 p. m.</p>
<p>At 12:15 a. m. on the morning of February 5, after five hours of questioning in which it became evident that petitioner was following his attorney's instructions, on the Assistant District Attorney's orders petitioner was transferred to the 46th Squad, Ryer Avenue Police Station. The Assistant District Attorney also went to the police station and to some extent continued to participate in the interrogation. Petitioner arrived at 12:30 and questioning was resumed at 12:40. The character of the questioning is revealed by the testimony of Detective Farrell:</p>
<blockquote>"Q. Who did you leave him in the room with?</blockquote>
<blockquote>"A. With Detective Lehrer and Sergeant Clarke came in and Mr. Goldsmith came in or Inspector Halk came in. It was back and forth. People just came in, spoke a few words to the defendant or they listened a few minutes and they left."</blockquote>
<p>But petitioner persisted in his refusal to answer, and again requested permission to see his attorney, this time from Detective Lehrer. His request was again denied.</p>
<p>It was then that those in charge of the investigation decided that petitioner's close friend, Bruno, could be of <span class="star-pagination">*319</span> use. He had been called out on the case around 10 or 11 p. m., although he was not connected with the 46th Squad or Precinct in any way. Although, in fact, his job was in no way threatened, Bruno was told to tell petitioner that petitioner's telephone call had gotten him "in a lot of trouble," and that he should seek to extract sympathy from petitioner for Bruno's pregnant wife and three children. Bruno developed this theme with petitioner without success, and petitioner, also without success, again sought to see his attorney, a request which Bruno relayed unavailingly to his superiors. After this first session with petitioner, Bruno was again directed by Lt. Gannon to play on petitioner's sympathies, but again no confession was forthcoming. But the Lieutenant a third time ordered Bruno falsely to importune his friend to confess, but again petitioner clung to his attorney's advice. Inevitably, in the fourth such session directed by the Lieutenant, lasting a full hour, petitioner succumbed to his friend's prevarications and agreed to make a statement. Accordingly, at 3:25 a. m. the Assistant District Attorney, a stenographer, and several other law enforcement officials entered the room where petitioner was being questioned, and took his statement in question and answer form with the Assistant District Attorney asking the questions. The statement was completed at 4:05 a. m.</p>
<p>But this was not the end. At 4:30 a. m. three detectives took petitioner to Police Headquarters in Manhattan. On the way they attempted to find the bridge from which petitioner said he had thrown the murder weapon. They crossed the Triborough Bridge into Manhattan, arriving at Police Headquarters at 5 a. m., and left Manhattan for the Bronx at 5:40 a. m. via the Willis Avenue Bridge. When petitioner recognized neither bridge as the one from which he had thrown the weapon, they reentered Manhattan via the Third Avenue Bridge, which petitioner stated was the right one, and then returned to <span class="star-pagination">*320</span> the Bronx well after 6 a. m. During that trip the officers also elicited a statement from petitioner that the deceased was always "on [his] back," "always pushing" him and that he was "not sorry" he had shot the deceased. All three detectives testified to that statement at the trial.</p>
<p>Court opened at 10 a. m. that morning, and petitioner was arraigned at 10:15.</p>
<p>At the trial, the confession was introduced in evidence over appropriate objections. The jury was instructed that it could rely on it only if it was found to be voluntary. The jury returned a guilty verdict and petitioner was sentenced to death. The New York Court of Appeals affirmed the conviction over three dissents, 4 N. Y. 2d 256, 173 N. Y. S. 2d 793, <span class="citation" data-id="5516991"><a href="/opinion/5669883/people-v-spano/" aria-description="Citation for case: People v. Spano">150 N. E. 2d 226</a></span>, and we granted certiorari to resolve the serious problem presented under the Fourteenth Amendment. <span class="citation multiple-matches"><a href="/c/U.%20S./358/919/">358 U. S. 919</a></span>.</p>
<p>Petitioner's first contention is that his absolute right to counsel in a capital case, <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, became operative on the return of an indictment against him, for at that time he was in every sense a defendant in a criminal case, the grand jury having found sufficient cause to believe that he had committed the crime. He argues accordingly that following indictment no confession obtained in the absence of counsel can be used without violating the Fourteenth Amendment. He seeks to distinguish <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, and <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>, on the ground that in those cases no indictment had been returned. We find it unnecessary to reach that contention, for we find use of the confession obtained here inconsistent with the Fourteenth Amendment under traditional principles.</p>
<p>The abhorrence of society to the use of involuntary confessions does not turn alone on their inherent untrust-worthiness. It also turns on the deep-rooted feeling that the police must obey the law while enforcing the law; that in the end life and liberty can be as much endangered <span class="star-pagination">*321</span> from illegal methods used to convict those thought to be criminals as from the actual criminals themselves. Accordingly, the actions of police in obtaining confessions have come under scrutiny in a long series of cases.<sup>[2]</sup> Those cases suggest that in recent years law enforcement officials have become increasingly aware of the burden which they share, along with our courts, in protecting fundamental rights of our citizenry, including that portion of our citizenry suspected of crime. The facts of no case recently in this Court have quite approached the brutal beatings in <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), or the 36 consecutive hours of questioning present in <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span> (1944). But as law enforcement officers become more responsible, and the methods used to extract confessions more sophisticated, our duty to enforce federal constitutional protections does not cease. It only becomes more difficult because of the more delicate judgments to be made. Our judgment here is that, on all the facts, this conviction cannot stand.</p>
<p>Petitioner was a foreign-born young man of 25 with no past history of law violation or of subjection to official interrogation, at least insofar as the record shows. He <span class="star-pagination">*322</span> had progressed only one-half year into high school and the record indicates that he had a history of emotional instability.<sup>[3]</sup> He did not make a narrative statement, but was subject to the leading questions of a skillful prosecutor in a question and answer confession. He was subjected to questioning not by a few men, but by many. They included Assistant District Attorney Goldsmith, one Hyland of the District Attorney's Office, Deputy Inspector Halks,<sup>[4]</sup> Lieutenant Gannon, Detective Ciccone, Detective Motta, Detective Lehrer, Detective Marshal, Detective Farrell, Detective Leira,<sup>[5]</sup> Detective Murphy, Detective Murtha, Sergeant Clarke, Patrolman Bruno and Stenographer Baldwin. All played some part, and the effect of such massive official interrogation must have been felt. Petitioner was questioned for virtually eight straight hours before he confessed, with his only respite being a transfer to an arena presumably considered more appropriate by the police for the task at hand. Nor was the questioning conducted during normal business hours, but began in early evening, continued into the night, and did not bear fruition until the not-too-early morning. The drama was not played out, with the final admissions obtained, until almost sunrise. In such circumstances slowly mounting fatigue does, and is calculated to, play its part. The questioners persisted in the face of his repeated refusals to answer on the advice of his <span class="star-pagination">*323</span> attorney, and they ignored his reasonable requests to contact the local attorney whom he had already retained and who had personally delivered him into the custody of these officers in obedience to the bench warrant.</p>
<p>The use of Bruno, characterized in this Court by counsel for the State as a "childhood friend" of petitioner's, is another factor which deserves mention in the totality of the situation. Bruno's was the one face visible to petitioner in which he could put some trust. There was a bond of friendship between them going back a decade into adolescence. It was with this material that the officers felt that they could overcome petitioner's will. They instructed Bruno falsely to state that petitioner's telephone call had gotten him into trouble, that his job was in jeopardy, and that loss of his job would be disastrous to his three children, his wife and his unborn child. And Bruno played this part of a worried father, harried by his superiors, in not one, but four different acts, the final one lasting an hour. Cf. <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span>. Petitioner was apparently unaware of John Gay's famous couplet:</p>
         "An open foe may prove a curse,
          But a pretended friend is worse,"
<p>and he yielded to his false friend's entreaties.</p>
<p>We conclude that petitioner's will was overborne by official pressure, fatigue and sympathy falsely aroused, after considering all the facts in their post-indictment setting.<sup>[6]</sup> Here a grand jury had already found sufficient cause to require petitioner to face trial on a charge of first-degree murder, and the police had an eyewitness to the shooting. The police were not therefore merely trying to solve a crime, or even to absolve a suspect. Compare <span class="star-pagination">*324</span> <i>Crooker</i> v. <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">California, supra</a></span></i><i>,</i> and <i>Cicenia</i> v. <i><span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">Lagay, supra</a></span></i><i>.</i> They were rather concerned primarily with securing a statement from defendant on which they could convict him. The undeviating intent of the officers to extract a confession from petitioner is therefore patent. When such an intent is shown, this Court has held that the confession obtained must be examined with the most careful scrutiny, and has reversed a conviction on facts less compelling than these. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>. Accordingly, we hold that petitioner's conviction cannot stand under the Fourteenth Amendment.</p>
<p>The State suggests, however, that we are not free to reverse this conviction, since there is sufficient other evidence in the record from which the jury might have found guilt, relying on <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">346 U. S. 156</a></span>. But <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 568</a></span>, authoritatively establishes that <i><span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">Stein</a></span></i> did not hold that a conviction may be sustained on the basis of other evidence if a confession found to be involuntary by this Court was used, even though limiting instructions were given. <i><span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">Stein</a></span></i> held only that when a confession is not found by this Court to be involuntary, this Court will not reverse on the ground that the jury might have found it involuntary and might have relied on it. The judgment must be</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE DOUGLAS, with whom MR. JUSTICE BLACK and MR. JUSTICE BRENNAN join, concurring.</p>
<p>While I join the opinion of the Court, I add what for me is an even more important ground of decision.</p>
<p>We have often divided on whether state authorities may question a suspect for hours on end when he has no lawyer present and when he has demanded that he have the benefit of legal advice. See <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, and cases cited. But here we deal not with a suspect but with a man who has been formally charged <span class="star-pagination">*325</span> with a crime. The question is whether after the indictment and before the trial the Government can interrogate the accused <i>in secret</i> when he asked for his lawyer and when his request was denied. This is a capital case; and under the rule of <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, the defendant was entitled to be represented by counsel. This representation by counsel is not restricted to the trial. As stated in <i>Powell</i> v. <i>Alabama, supra,</i> p. 57:</p>
<blockquote>"during perhaps the most critical period of the proceedings against these defendants, that is to say, from the time of their arraignment until the beginning of their trial, when consultation, thoroughgoing investigation and preparation were vitally important, the defendants did not have the aid of counsel in any real sense, although they were as much entitled to such aid during that period as at the trial itself."</blockquote>
<p>Depriving a person, formally charged with a crime, of counsel during the period prior to trial may be more damaging than denial of counsel during the trial itself.</p>
<p>We do not have here mere suspects who are being secretly interrogated by the police as in <i>Crooker</i> v. <i><span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">California, supra</a></span></i><i>,</i> nor witnesses who are being questioned in secret administrative or judicial proceedings as in <i>In re Groban,</i> <span class="citation" data-id="9421372"><a href="/opinion/105449/in-re-groban/" aria-description="Citation for case: In Re Groban">352 U. S. 330</a></span>, and <i>Anonymous Nos. 6 &amp; 7</i> v. <i>Baker, ante,</i> p. 287. This is a case of an accused, who is scheduled to be tried by a judge and jury, being tried in a preliminary way by the police. This is a kangaroo court procedure whereby the police produce the vital evidence in the form of a confession which is useful or necessary to obtain a conviction. They in effect deny him effective representation by counsel. This seems to me to be a flagrant violation of the principle announced in <i>Powell</i> v. <i>Alabama, supra</i><i>,</i> that the right of counsel extends to the preparation for trial, as well as to the trial itself. As Professor Chafee once said, "A person accused of crime <span class="star-pagination">*326</span> needs a lawyer right after his arrest probably more than at any other time." Chafee, Documents on Fundamental Human Rights, Pamphlet 2 (1951-1952), p. 541. When he is deprived of that right after indictment and before trial, he may indeed be denied effective representation by counsel at the only stage when legal aid and advice would help him. This <i>secret inquisition</i> by the police when defendant asked for and was denied counsel was as serious an invasion of his constitutional rights as the denial of a continuance in order to employ counsel was held to be in <i>Chandler</i> v. <i>Fretag,</i> <span class="citation" data-id="105241"><a href="/opinion/105241/chandler-v-warden-fretag/#10" aria-description="Citation for case: Chandler v. Warden Fretag">348 U. S. 3, 10</a></span>. What we said in <i>Avery</i> v. <i>Alabama,</i> <span class="citation" data-id="103272"><a href="/opinion/103272/avery-v-alabama/#446" aria-description="Citation for case: Avery v. Alabama">308 U. S. 444, 446</a></span>, has relevance here:</p>
<blockquote>". . . the denial of opportunity for appointed counsel to confer, to consult with the accused and to prepare his defense, could convert the appointment of counsel into a sham and nothing more than a formal compliance with the Constitution's requirement that an accused be given the assistance of counsel."</blockquote>
<p>I join with Judges Desmond, Fuld, and Van Voorhis of the New York Court of Appeals (4 N. Y. 2d 256, 266, 173 N. Y. S. 2d 793, 801, <span class="citation" data-id="5516991"><a href="/opinion/5669883/people-v-spano/#231" aria-description="Citation for case: People v. Spano">150 N. E. 2d 226, 231-232</a></span>), in asking, what use is a defendant's right to effective counsel at every stage of a criminal case if, while he is held awaiting trial, he can be questioned in the absence of counsel until he confesses? In that event the secret trial in the police precincts effectively supplants the public trial guaranteed by the Bill of Rights.</p>
<p>MR. JUSTICE STEWART, whom MR. JUSTICE DOUGLAS and MR. JUSTICE BRENNAN join, concurring.</p>
<p>While I concur in the opinion of the Court, it is my view that the absence of counsel when this confession was elicited was alone enough to render it inadmissible under the Fourteenth Amendment.</p>
<p><span class="star-pagination">*327</span> Let it be emphasized at the outset that this is not a case where the police were questioning a suspect in the course of investigating an unsolved crime. See <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>; <i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>. When the petitioner surrendered to the New York authorities he was under indictment for first degree murder.</p>
<p>Under our system of justice an indictment is supposed to be followed by an arraignment and a trial. At every stage in those proceedings the accused has an absolute right to a lawyer's help if the case is one in which a death sentence may be imposed. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>. Indeed the right to the assistance of counsel whom the accused has himself retained is absolute, whatever the offense for which he is on trial. <i>Chandler</i> v. <i>Fretag,</i> <span class="citation" data-id="105241"><a href="/opinion/105241/chandler-v-warden-fretag/" aria-description="Citation for case: Chandler v. Warden Fretag">348 U. S. 3</a></span>.</p>
<p>What followed the petitioner's surrender in this case was not arraignment in a court of law, but an all-night inquisition in a prosecutor's office, a police station, and an automobile. Throughout the night the petitioner repeatedly asked to be allowed to send for his lawyer, and his requests were repeatedly denied. He finally was induced to make a confession. That confession was used to secure a verdict sending him to the electric chair.</p>
<p>Our Constitution guarantees the assistance of counsel to a man on trial for his life in an orderly courtroom, presided over by a judge, open to the public, and protected by all the procedural safeguards of the law. Surely a Constitution which promises that much can vouchsafe no less to the same man under midnight inquisition in the squad room of a police station.</p>
<h2>NOTES</h2>
<p>[1]  How this could be so when the attorney's name, Tobias Russo, was concededly in the telephone book does not appear. The trial judge sustained objections by the Assistant District Attorney to questions designed to delve into this mystery.</p>
<p>[2]  <i>E. g., </i><i>Cicenia</i> v. <i>Lagay,</i> <span class="citation" data-id="9421694"><a href="/opinion/105750/cicenia-v-lagay/" aria-description="Citation for case: Cicenia v. Lagay">357 U. S. 504</a></span>; <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>; <i>Ashdown</i> v. <i>Utah,</i> <span class="citation" data-id="9421686"><a href="/opinion/105744/ashdown-v-utah/" aria-description="Citation for case: Ashdown v. Utah">357 U. S. 426</a></span>; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>; <i>Thomas</i> v. <i>Arizona,</i> <span class="citation" data-id="105683"><a href="/opinion/105683/thomas-v-arizona/" aria-description="Citation for case: Thomas v. Arizona">356 U. S. 390</a></span>; <i>Fikes</i> v. <i>Alabama,</i> <span class="citation" data-id="9421354"><a href="/opinion/105436/fikes-v-alabama/" aria-description="Citation for case: Fikes v. Alabama">352 U. S. 191</a></span>; <i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span>; <i>Stein</i> v. <i>New York,</i> <span class="citation" data-id="9420977"><a href="/opinion/105149/stein-v-new-york/" aria-description="Citation for case: Stein v. New York">346 U. S. 156</a></span>; <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span>; <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span>; <i>Gallegos</i> v. <i>Nebraska,</i> <span class="citation" data-id="9420632"><a href="/opinion/104933/gallegos-v-nebraska/" aria-description="Citation for case: Gallegos v. Nebraska">342 U. S. 55</a></span>; <i>Johnson</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="8920216"><a href="/opinion/8930122/johnson-v-pennsylvania/" aria-description="Citation for case: Johnson v. Pennsylvania">340 U. S. 881</a></span>; <i>Harris</i> v. <i>South Carolina,</i> <span class="citation" data-id="9420383"><a href="/opinion/104712/harris-v-south-carolina/" aria-description="Citation for case: Harris v. South Carolina">338 U. S. 68</a></span>; <i>Turner</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9420381"><a href="/opinion/104711/turner-v-pennsylvania/" aria-description="Citation for case: Turner v. Pennsylvania">338 U. S. 62</a></span>; <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49</a></span>; <i>Lee</i> v. <i>Mississippi,</i> <span class="citation" data-id="104497"><a href="/opinion/104497/lee-v-mississippi/" aria-description="Citation for case: Lee v. Mississippi">332 U. S. 742</a></span>; <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596</a></span>; <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>; <i>Lyons</i> v. <i>Oklahoma,</i> <span class="citation" data-id="9419526"><a href="/opinion/104010/lyons-v-oklahoma/" aria-description="Citation for case: Lyons v. Oklahoma">322 U. S. 596</a></span>; <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; <i>Ward</i> v. <i>Texas,</i> <span class="citation" data-id="103702"><a href="/opinion/103702/ward-v-texas/" aria-description="Citation for case: Ward v. Texas">316 U. S. 547</a></span>; <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>; <i>Vernon</i> v. <i>Alabama,</i> <span class="citation" data-id="8156474"><a href="/opinion/8194539/vernon-v-alabama/" aria-description="Citation for case: Vernon v. Alabama">313 U. S. 547</a></span>; <i>Lomax</i> v. <i>Texas,</i> <span class="citation" data-id="8156462"><a href="/opinion/8194527/lomax-v-texas/" aria-description="Citation for case: Lomax v. Texas">313 U. S. 544</a></span>; <i>White</i> v. <i>Texas,</i> <span class="citation" data-id="103368"><a href="/opinion/103368/white-v-texas/" aria-description="Citation for case: White v. Texas">310 U. S. 530</a></span>; <i>Canty</i> v. <i>Alabama,</i> <span class="citation" data-id="8155149"><a href="/opinion/8193214/canty-v-alabama/" aria-description="Citation for case: Canty v. Alabama">309 U. S. 629</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>.</p>
<p>[3]  Medical reports from New York City's Fordham Hospital introduced by defendant showed that he had suffered a cerebral concussion in 1955. He was described by a private physician in 1951 as "an extremely nervous tense individual who is emotionally unstable and maladjusted," and was found unacceptable for military service in 1951, primarily because of "Psychiatric disorder." He failed the Army's AFQT-1 intelligence test. His mother had been in mental hospitals on three separate occasions.</p>
<p>[4]  His name is sometimes spelled "Hawks."</p>
<p>[5]  Although each is referred to separately in the record, it may be that Detectives Lehrer and Leira are the same person.</p>
<p>[6]  <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, is not to the contrary. There, while petitioner had already been arraigned on an incest charge, his later questioning and confession concerned a murder.</p>

</div>
```

---
