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

## GROUP: content/cases/Sherman v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Sherman v. United States"
type: case
citation: "356 U.S. 369 (1958)"
parallel_cite: "78 S. Ct. 819; 2 L. Ed. 2d 848"
neutral_cite: 1958 U.S. LEXIS 1024
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1958
date_decided: 1958-05-19
docket: 87
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1958-05-19
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Sherman v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/105681/sherman-v-united-states/"
  cluster_id: 105681
  opinion_id: 105681
  identity_checked: true
homes:
  - page: "[[Entrapment]]"
    role: "Key — Progeny / Refinement"
related: ["[[Sorrells v. United States]]", "[[Hampton v. United States]]", "[[Jacobson v. United States]]", "[[Mathews v. United States]]"]
aliases: []
tags: ["case", "entrapment", "predisposition", "due-process"]
holding: "Entrapment is established as a matter of law when the government, through its informant, implants the criminal design in an…"
lake:
  record_id: Sherman v. United States
  status: verified
  projected_at: 2026-07-09
---

# Sherman v. United States

*356 U.S. 369 (1958)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A government informant, Kalchinian, met Sherman at a doctor's office where both were being treated for narcotics addiction and repeatedly asked Sherman to obtain drugs, appealing to sympathy until Sherman—a recovering addict—relented and supplied narcotics. Sherman was convicted and raised the defense of entrapment.

## Issue
Whether entrapment was established as a matter of law where a government informant induced a recovering addict to obtain narcotics.

## Rule
Entrapment turns on whether the government implanted the criminal design. "Entrapment occurs only when the criminal conduct was 'the product of the creative activity' of law-enforcement officials." — 356 U.S. at 372. ^pin-372

"To determine whether entrapment has been established, a line must be drawn between the trap for the unwary innocent and the trap for the unwary criminal." — [*Id.*](https://www.courtlistener.com/opinion/105681/sherman-v-united-states/#:~:text=To%20determine%20whether%20entrapment%20has) ^pin-372a

## Application
The informant repeatedly importuned Sherman, exploiting their shared struggle with addiction, and the prosecution's own evidence showed Sherman was not ready and willing but was worked upon until he yielded; on that record the criminal design originated with the government, and entrapment was established as a matter of law, so the Court reversed.

## Conclusion
Entrapment was established as a matter of law; the conviction was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Applies the subjective (predisposition) entrapment test of [[Sorrells v. United States]]; the predisposition focus was reaffirmed in [[Jacobson v. United States]] and [[Mathews v. United States]], and the due-process outer limit addressed in [[Hampton v. United States]].

## Appears on
- [[Entrapment]] — *Key — Progeny / Refinement*

## Sources
- *Sherman v. United States*, 356 U.S. 369 (1958) — https://www.courtlistener.com/opinion/105681/sherman-v-united-states/ — pinpoint: 372.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "c1139821438c315e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "356 U.S. 369 (1958)", "court": "U.S. Supreme Court", "neutral_cite": "1958 U.S. LEXIS 1024", "official_citation_present": true, "parallel_cite": "78 S. Ct. 819; 2 L. Ed. 2d 848", "title": "Sherman v. United States", "year": "1958"}}
{"assertion_id": "5fb06964a607dfc9", "dimension": "support", "kind": "home_role", "locator": {"home": "Entrapment"}, "payload": {"home": "Entrapment", "role": "Key — Progeny / Refinement", "title": "Sherman v. United States"}}
{"assertion_id": "63c67783dfcd42ee", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Entrapment is established as a matter of law when the government, through its informant, implants the criminal design in an…", "title": "Sherman v. United States"}}
{"assertion_id": "3f6fd8994ef542c7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Sherman v. United States"}}
{"assertion_id": "c1b1b01a74d52337", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1958-05-19", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Sherman v. United States", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Sherman v. United States", "varies_by_point": "false"}}
```

### lake record — Sherman v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Sherman v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Sherman v. United States",
    "case_name_short": "Sherman",
    "case_name_full": "Sherman v. United States",
    "input_case_name": "Sherman v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1958-05-19",
    "year": 1958,
    "docket": "87",
    "cluster_id": 105681,
    "lead_opinion_id": 105681,
    "sibling_ids": [
      105681,
      9421598,
      9421599
    ],
    "absolute_url": "/opinion/105681/sherman-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "356 U.S. 369",
      "volume": "356",
      "reporter": "U.S.",
      "page": "369",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "78 S. Ct. 819",
        "volume": "78",
        "reporter": "S. Ct.",
        "page": "819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 L. Ed. 2d 848",
        "volume": "2",
        "reporter": "L. Ed. 2d",
        "page": "848",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1958 U.S. LEXIS 1024",
        "volume": "1958",
        "reporter": "U.S. LEXIS",
        "page": "1024",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "356 U.S. 369",
        "volume": "356",
        "reporter": "U.S.",
        "page": "369",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 S. Ct. 819",
        "volume": "78",
        "reporter": "S. Ct.",
        "page": "819",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2 L. Ed. 2d 848",
        "volume": "2",
        "reporter": "L. Ed. 2d",
        "page": "848",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1958 U.S. LEXIS 1024",
        "volume": "1958",
        "reporter": "U.S. LEXIS",
        "page": "1024",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "356 U.S. 369",
    "official_selection": {
      "court_class": "scotus",
      "selected": "356 U.S. 369",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-372",
      "page": null,
      "quote": "--- # Sherman v. United States *356 U.S. 369 (1958)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A government informant, Kalchinian, met Sherman at a doctor's office where both were being treated for narcotics addiction and repeatedly asked Sherman to obtain drugs, appealing to sympathy until Sherman\u2014a recovering addict\u2014relented and supplied narcotics. Sherman was convicted and raised the defense of entrapment. ## Issue Whether entrapment was established as a matter of law where a government informant induced a recovering addict to obtain narcotics. ## Rule Entrapment turns on whether the government implanted the criminal design.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-372a",
      "page": null,
      "quote": "To determine whether entrapment has been established, a line must be drawn between the trap for the unwary innocent and the trap for the unwary criminal.",
      "star_marker": "372",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 6007,
      "fragment": "#:~:text=To%20determine%20whether%20entrapment%20has",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1958-05-19",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Sherman v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. James Barta",
          "cluster_id": 2774293,
          "cite": [
            "776 F.3d 931",
            "2015 WL 350672",
            "2015 U.S. App. LEXIS 1382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tony Clanton v. United States",
          "cluster_id": 776988,
          "cite": [
            "284 F.3d 420",
            "2002 U.S. App. LEXIS 4409",
            "2002 WL 431895"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jones v. Jones",
          "cluster_id": 16317,
          "cite": [
            "163 F.3d 285",
            "1998 U.S. App. LEXIS 31379",
            "1998 WL 879749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas",
          "cluster_id": 7058791,
          "cite": [
            "134 F.3d 975",
            "98 Daily Journal DAR 763",
            "98 Cal. Daily Op. Serv. 555",
            "48 Fed. R. Serv. 924",
            "1998 U.S. App. LEXIS 832",
            "1998 WL 19640"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dwayne A. Washington",
          "cluster_id": 735397,
          "cite": [
            "106 F.3d 983",
            "323 U.S. App. D.C. 175",
            "46 Fed. R. Serv. 719",
            "1997 U.S. App. LEXIS 3057"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane1_negative"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gelbard v. United States",
          "cluster_id": 108596,
          "cite": [
            "33 L. Ed. 2d 179",
            "92 S. Ct. 2357",
            "408 U.S. 41",
            "1972 U.S. LEXIS 103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
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
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. William D. Davis, United States of America v. Curry James Williams",
          "cluster_id": 679513,
          "cite": [
            "36 F.3d 1424",
            "94 Daily Journal DAR 13648",
            "1994 U.S. App. LEXIS 27168",
            "1994 WL 525969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Calvano",
          "cluster_id": 5679122,
          "cite": [
            "30 N.Y.2d 199",
            "282 N.E.2d 322",
            "331 N.Y.S.2d 430",
            "1972 N.Y. LEXIS 1393"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gordon Pennell",
          "cluster_id": 437507,
          "cite": [
            "737 F.2d 521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Norman Archer",
          "cluster_id": 314188,
          "cite": [
            "486 F.2d 670",
            "1973 U.S. App. LEXIS 7745"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States of America, in No. 81-1020 v. Jannotti, Harry P. United States of America, in No. 81-1021 v. Schwartz, George X",
          "cluster_id": 401021,
          "cite": [
            "673 F.2d 578",
            "1982 WL 602723"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brogan v. United States",
          "cluster_id": 118168,
          "cite": [
            "139 L. Ed. 2d 830",
            "118 S. Ct. 805",
            "522 U.S. 398",
            "1998 U.S. LEXIS 648"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur Ortiz",
          "cluster_id": 479010,
          "cite": [
            "804 F.2d 1161",
            "1986 U.S. App. LEXIS 33218"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Richard Scott McLernon Kido Yaqui, Sherri Louise Farrell, Miguel Angel Carranza, and Marco Antonio Valdez-Cota",
          "cluster_id": 443243,
          "cite": [
            "746 F.2d 1098"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Rafael Santana and Francis Fuentes",
          "cluster_id": 654192,
          "cite": [
            "6 F.3d 1",
            "1993 U.S. App. LEXIS 23810",
            "1993 WL 345746"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gendron",
          "cluster_id": 195225,
          "cite": [
            "18 F.3d 955",
            "1994 WL 50975"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul A. Gorin v. United States of America, Henry Grillo v. United States of America, Saul Glassman v. United States",
          "cluster_id": 259678,
          "cite": [
            "313 F.2d 641",
            "11 A.F.T.R.2d (RIA) 1044",
            "1963 U.S. App. LEXIS 6082"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brand",
          "cluster_id": 8439509,
          "cite": [
            "467 F.3d 179",
            "71 Fed. R. Serv. 672",
            "2006 U.S. App. LEXIS 25887",
            "2006 WL 2981524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Wayne Goodwin, Charles William Bullard and Grover Eugene Beaver",
          "cluster_id": 380170,
          "cite": [
            "625 F.2d 693",
            "1980 U.S. App. LEXIS 14147"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Moran",
          "cluster_id": 5607650,
          "cite": [
            "1 Cal. 3d 755",
            "463 P.2d 763",
            "83 Cal. Rptr. 411",
            "1970 Cal. LEXIS 345"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sherman v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(105681 OR 9421598 OR 9421599) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NTA1NTY4MDAwMDAmcz0xNjc2MTAxJnQ9byZkPTIwMjYtMDctMDUmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28105681+OR+9421598+OR+9421599%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 12,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 12,
        "triage_snippet_classified": 188
      },
      "lane2_top_cited": {
        "query": "cites:(105681 OR 9421598 OR 9421599)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzEmcz0zMjM5MTkmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28105681+OR+9421598+OR+9421599%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(105681 OR 9421598 OR 9421599)",
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
    "complete_query": "cites:(105681 OR 9421598 OR 9421599)",
    "indexed_citing_opinions": 1086,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 105681,
        "count": 1015,
        "count_source": "search"
      },
      {
        "opinion_id": 9421598,
        "count": 104,
        "count_source": "search"
      },
      {
        "opinion_id": 9421599,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1587,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/sherman-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjcwNjM3ODgmcz00ODQyODc1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28105681+OR+9421598+OR+9421599%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 105681,
        "cited_id": 94127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 101997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 225592,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 227266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 230073,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 230738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 232111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 233333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 241347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 1472575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 1477802,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 1479180,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 1498526,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 1548320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 105681,
        "cited_id": 1551253,
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
    "date_created": "2026-07-05T19:24:53Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:25:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:25:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:29:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:25:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Sherman v. United States

```
<div>
<center><b><span class="citation" data-id="9421598"><a href="/opinion/105681/sherman-v-united-states/" aria-description="Citation for case: Sherman v. United States">356 U.S. 369</a></span> (1958)</b></center>
<center><h1>SHERMAN<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 87.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 16, 1958.</center>
<center>Decided May 19, 1958.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*370</span> <i>Henry A. Lowenberg</i> argued the cause and filed a brief for petitioner.</p>
<p><i>James W. Knapp</i> argued the cause for the United States. On the brief were <i>Solicitor General Rankin, Warren Olney, III,</i> then Assistant Attorney General, <i>Beatrice Rosenberg</i> and <i>Robert G. Maysack.</i></p>
<p>MR. CHIEF JUSTICE WARREN delivered the opinion of the Court.</p>
<p>The issue before us is whether petitioner's conviction should be set aside on the ground that as a matter of law the defense of entrapment was established. Petitioner was convicted under an indictment charging three sales of narcotics in violation of <span class="citation no-link">21 U. S. C. § 174</span>. A previous conviction had been reversed on account of improper instructions as to the issue of entrapment. <span class="citation" data-id="230738"><a href="/opinion/230738/united-states-v-sherman/" aria-description="Citation for case: United States v. Sherman">200 F. 2d 880</a></span>. In the second trial, as in the first, petitioner's defense was <span class="star-pagination">*371</span> a claim of entrapment: an agent of the Federal Government induced him to take part in illegal transactions when otherwise he would not have done so.</p>
<p>In late August 1951, Kalchinian, a government informer, first met petitioner at a doctor's office where apparently both were being treated to be cured of narcotics addiction. Several accidental meetings followed, either at the doctor's office or at the pharmacy where both filled their prescriptions from the doctor. From mere greetings, conversation progressed to a discussion of mutual experiences and problems, including their attempts to overcome addiction to narcotics. Finally Kalchinian asked petitioner if he knew of a good source of narcotics. He asked petitioner to supply him with a source because he was not responding to treatment. From the first, petitioner tried to avoid the issue. Not until after a number of repetitions of the request, predicated on Kalchinian's presumed suffering, did petitioner finally acquiesce. Several times thereafter he obtained a quantity of narcotics which he shared with Kalchinian. Each time petitioner told Kalchinian that the total cost of narcotics he obtained was twenty-five dollars and that Kalchinian owed him fifteen dollars. The informer thus bore the cost of his share of the narcotics plus the taxi and other expenses necessary to obtain the drug. After several such sales Kalchinian informed agents of the Bureau of Narcotics that he had another seller for them. On three occasions during November 1951, government agents observed petitioner give narcotics to Kalchinian in return for money supplied by the Government.</p>
<p>At the trial the factual issue was whether the informer had convinced an otherwise unwilling person to commit a criminal act or whether petitioner was already predisposed to commit the act and exhibited only the natural hesitancy of one acquainted with the narcotics trade. <span class="star-pagination">*372</span> The issue of entrapment went to the jury,<sup>[1]</sup> and a conviction resulted. Petitioner was sentenced to imprisonment for ten years. The Court of Appeals for the Second Circuit affirmed. <span class="citation" data-id="241347"><a href="/opinion/241347/united-states-v-joseph-george-sherman/" aria-description="Citation for case: United States v. Joseph George Sherman">240 F. 2d 949</a></span>. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./353/935/">353 U. S. 935</a></span>.</p>
<p>In <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span>, this Court firmly recognized the defense of entrapment in the federal courts. The intervening years have in no way detracted from the principles underlying that decision. The function of law enforcement is the prevention of crime and the apprehension of criminals. Manifestly, that function does not include the manufacturing of crime. Criminal activity is such that stealth and strategy are necessary weapons in the arsenal of the police officer. However, "A different question is presented when the criminal design originates with the officials of the Government, and they implant in the mind of an innocent person the disposition to commit the alleged offense and induce its commission in order that they may prosecute." <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#442" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 442</a></span>. Then stealth and strategy become as objectionable police methods as the coerced confession and the unlawful search. Congress could not have intended that its statutes were to be enforced by tempting innocent persons into violations.</p>
<p>However, the fact that government agents "merely afford opportunities or facilities for the commission of the offense does not" constitute entrapment. Entrapment occurs only when the criminal conduct was "the product of the <i>creative</i> activity" of law-enforcement officials. (Emphasis supplied.) See <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#441" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 441, 451</a></span>. To determine whether entrapment has been established, a line must be drawn between the trap for the unwary innocent and the trap for the unwary criminal. The principles <span class="star-pagination">*373</span> by which the courts are to make this determination were outlined in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span>.</i> On the one hand, at trial the accused may examine the conduct of the government agent; and on the other hand, the accused will be subjected to an "appropriate and searching inquiry into his own conduct and predisposition" as bearing on his claim of innocence. See <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#451" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 451</a></span>.</p>
<p>We conclude from the evidence that entrapment was established as a matter of law. In so holding, we are not choosing between conflicting witnesses, nor judging credibility. Aside from recalling Kalchinian, who was the Government's witness, the defense called no witnesses. We reach our conclusion from the undisputed testimony of the prosecution's witnesses.</p>
<p>It is patently clear that petitioner was induced by Kalchinian. The informer himself testified that, believing petitioner to be undergoing a cure for narcotics addiction, he nonetheless sought to persuade petitioner to obtain for him a source of narcotics. In Kalchinian's own words we are told of the accidental, yet recurring, meetings, the ensuing conversations concerning mutual experiences in regard to narcotics addiction, and then of Kalchinian's resort to sympathy. One request was not enough, for Kalchinian tells us that additional ones were necessary to overcome, first, petitioner's refusal, then his evasiveness, and then his hesitancy in order to achieve capitulation. Kalchinian not only procured a source of narcotics but apparently also induced petitioner to return to the habit. Finally, assured of a catch, Kalchinian informed the authorities so that they could close the net. The Government cannot disown Kalchinian and insist it is not responsible for his actions. Although he was not being paid, Kalchinian was an active government informer who had but recently been the instigator of at least <span class="star-pagination">*374</span> two other prosecutions.<sup>[2]</sup> Undoubtedly the impetus for such achievements was the fact that in 1951 Kalchinian was himself under criminal charges for illegally selling narcotics and had not yet been sentenced.<sup>[3]</sup> It makes no difference that the sales for which petitioner was convicted occurred after a series of sales. They were not independent acts subsequent to the inducement but part of a course of conduct which was the product of the inducement. In his testimony the federal agent in charge of the case admitted that he never bothered to question Kalchinian about the way he had made contact with <span class="star-pagination">*375</span> petitioner. The Government cannot make such use of an informer and then claim disassociation through ignorance.</p>
<p>The Government sought to overcome the defense of entrapment by claiming that petitioner evinced a "ready complaisance" to accede to Kalchinian's request. Aside from a record of past convictions, which we discuss in the following paragraph, the Government's case is unsupported. There is no evidence that petitioner himself was in the trade. When his apartment was searched after arrest, no narcotics were found. There is no significant evidence that petitioner even made a profit on any sale to Kalchinian.<sup>[4]</sup> The Government's characterization of petitioner's hesitancy to Kalchinian's request as the natural wariness of the criminal cannot fill the evidentiary void.<sup>[5]</sup></p>
<p>The Government's additional evidence in the second trial to show that petitioner was ready and willing to sell narcotics should the opportunity present itself was petitioner's record of two past narcotics convictions. In 1942 petitioner was convicted of illegally selling narcotics; in 1946 he was convicted of illegally possessing them. However, a nine-year-old sales conviction and a five-year-old possession conviction are insufficient to prove petitioner had a readiness to sell narcotics at the time Kalchinian approached him, particularly when we must <span class="star-pagination">*376</span> assume from the record he was trying to overcome the narcotics habit at the time.</p>
<p>The case at bar illustrates an evil which the defense of entrapment is designed to overcome. The government informer entices someone attempting to avoid narcotics not only into carrying out an illegal sale but also into returning to the habit of use. Selecting the proper time, the informer then tells the government agent. The setup is accepted by the agent without even a question as to the manner in which the informer encountered the seller. Thus the Government plays on the weaknesses of an innocent party and beguiles him into committing crimes which he otherwise would not have attempted.<sup>[6]</sup> Law enforcement does not require methods such as this.</p>
<p>It has been suggested that in overturning this conviction we should reassess the doctrine of entrapment according to principles announced in the separate opinion of Mr. Justice Roberts in <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#453" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435, 453</a></span>. To do so would be to decide the case on grounds rejected by the majority in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> and, so far as the record shows, not raised here or below by the parties before us. We do not ordinarily decide issues not presented by the parties and there is good reason not to vary that practice in this case.</p>
<p>At least two important issues of law enforcement and trial procedure would have to be decided without the benefit of argument by the parties, one party being the Government. Mr. Justice Roberts asserted that although the defendant could claim that the Government had induced him to commit the crime, the Government could not reply by showing that the defendant's criminal conduct was due to his own readiness and not to the persuasion of government <span class="star-pagination">*377</span> agents. The handicap thus placed on the prosecution is obvious.<sup>[7]</sup> Furthermore, it was the position of Mr. Justice Roberts that the factual issue of entrapment now limited to the question of what the government agents didshould be decided by the judge, not the jury. Not only was this rejected by the Court in <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span>,</i> but where the issue has been presented to them, the Courts of Appeals have since <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> unanimously concluded that unless it can be decided as a matter of law, the issue of whether a defendant has been entrapped is for the jury as part of its function of determining the guilt or innocence of the accused.<sup>[8]</sup></p>
<p>To dispose of this case on the ground suggested would entail both overruling a leading decision of this Court and brushing aside the possibility that we would be <span class="star-pagination">*378</span> creating more problems than we would supposedly be solving.</p>
<p>The judgment of the Court of Appeals is reversed and the case is remanded to the District Court with instructions to dismiss the indictment.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE FRANKFURTER, whom MR. JUSTICE DOUGLAS, MR. JUSTICE HARLAN, and MR. JUSTICE BRENNAN join, concurring in the result.</p>
<p>Although agreeing with the Court that the undisputed facts show entrapment as a matter of law, I reach this result by a route different from the Court's.</p>
<p>The first case in which a federal court clearly recognized and sustained a claim of entrapment by government officers as a defense to an indictment was, apparently, <i>Woo Wai</i> v. <i>United States,</i> <span class="citation" data-id="8795796"><a href="/opinion/8811409/woo-wai-v-united-states/" aria-description="Citation for case: Woo Wai v. United States">223 F. 412</a></span>. Yet the basis of this defense, affording guidance for its application in particular circumstances, is as much in doubt today as it was when the defense was first recognized over forty years ago, although entrapment has been the decisive issue in many prosecutions. The lower courts have continued gropingly to express the feeling of outrage at conduct of law enforcers that brought recognition of the defense in the first instance, but without the formulated basis in reason that it is the first duty of courts to construct for justifying and guiding emotion and instinct.</p>
<p>Today's opinion does not promote this judicial desideratum, and fails to give the doctrine of entrapment the solid foundation that the decisions of the lower courts and criticism of learned writers have clearly shown is needed.<sup>[1]</sup> Instead it accepts without re-examination the <span class="star-pagination">*379</span> theory espoused in <i>Sorrells</i> v. <i>United States,</i> <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">287 U. S. 435</a></span>, over strong protest by Mr. Justice Roberts, speaking for Brandeis and Stone, JJ., as well as himself. The fact that since the <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> case the lower courts have either ignored its theory and continued to rest decision on the narrow facts of each case, or have failed after penetrating effort to define a satisfactory generalization, see, <i>e. g., </i><i>United States</i> v. <i>Becker,</i> <span class="citation" data-id="1472575"><a href="/opinion/1472575/united-states-v-becker/" aria-description="Citation for case: United States v. Becker">62 F. 2d 1007</a></span> (L. Hand, J.), is proof that the prevailing theory of the <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> case ought not to be deemed the last word. In a matter of this kind the Court should not rest on the first attempt at an explanation for what sound instinct counsels. It should not forego re-examination to achieve clarity of thought, because confused and inadequate analysis is too apt gradually to lead to a course of decisions that diverges from the true ends to be pursued.<sup>[2]</sup></p>
<p>It is surely sheer fiction to suggest that a conviction cannot be had when a defendant has been entrapped by government officers or informers because "Congress could not have intended that its statutes were to be enforced by tempting innocent persons into violations." In these cases raising claims of entrapment, the only legislative intention that can with any show of reason be extracted from the statute is the intention to make criminal precisely the conduct in which the defendant has engaged. That conduct includes all the elements necessary to constitute criminality. Without compulsion and "knowingly," <span class="star-pagination">*380</span> where that is requisite, the defendant has violated the statutory command. If he is to be relieved from the usual punitive consequences, it is on no account because he is innocent of the offense described. In these circumstances, conduct is not less criminal because the result of temptation, whether the tempter is a private person or a government agent or informer.</p>
<p>The courts refuse to convict an entrapped defendant, not because his conduct falls outside the proscription of the statute, but because, even if his guilt be admitted, the methods employed on behalf of the Government to bring about conviction cannot be countenanced. As Mr. Justice Holmes said in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#470" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 470</a></span> (dissenting), in another connection, "It is desirable that criminals should be detected, and to that end that all available evidence should be used. It also is desirable that the Government should not itself foster and pay for other crimes, when they are the means by which the evidence is to be obtained. . . . [F]or my part I think it a less evil that some criminals should escape than that the Government should play an ignoble part." Insofar as they are used as instrumentalities in the administration of criminal justice, the federal courts have an obligation to set their face against enforcement of the law by lawless means or means that violate rationally vindicated standards of justice, and to refuse to sustain such methods by effectuating them. They do this in the exercise of a recognized jurisdiction to formulate and apply "proper standards for the enforcement of the federal criminal law in the federal courts," <i>McNabb</i> v. <i>United States,</i> <span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#341" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 341</a></span>, an obligation that goes beyond the conviction of the particular defendant before the court. Public confidence in the fair and honorable administration of justice, upon which ultimately depends the rule of law, is the transcending value at stake.</p>
<p><span class="star-pagination">*381</span> The formulation of these standards does not in any way conflict with the statute the defendant has violated, or involve the initiation of a judicial policy disregarding or qualifying that framed by Congress. A false choice is put when it is said that either the defendant's conduct does not fall within the statute or he must be convicted. The statute is wholly directed to defining and prohibiting the substantive offense concerned and expresses no purpose, either permissive or prohibitory, regarding the police conduct that will be tolerated in the detection of crime. A statute prohibiting the sale of narcotics is as silent on the question of entrapment as it is on the admissibility of illegally obtained evidence. It is enacted, however, on the basis of certain presuppositions concerning the established legal order and the role of the courts within that system in formulating standards for the administration of criminal justice when Congress itself has not specifically legislated to that end. Specific statutes are to be fitted into an antecedent legal system.</p>
<p>It might be thought that it is largely an academic question whether the court's finding a bar to conviction derives from the statute or from a supervisory jurisdiction over the administration of criminal justice; under either theory substantially the same considerations will determine whether the defense of entrapment is sustained. But to look to a statute for guidance in the application of a policy not remotely within the contemplation of Congress at the time of its enactment is to distort analysis. It is to run the risk, furthermore, that the court will shirk the responsibility that is necessarily in its keeping, if Congress is truly silent, to accommodate the dangers of overzealous law enforcement and civilized methods adequate to counter the ingenuity of modern criminals. The reasons that actually underlie the defense of entrapment can too easily be lost sight of in the pursuit of a wholly fictitious congressional intent.</p>
<p><span class="star-pagination">*382</span> The crucial question, not easy of answer, to which the court must direct itself is whether the police conduct revealed in the particular case falls below standards, to which common feelings respond, for the proper use of governmental power. For answer it is wholly irrelevant to ask if the "intention" to commit the crime originated with the defendant or government officers, or if the criminal conduct was the product of "the creative activity" of law-enforcement officials. Yet in the present case the Court repeats and purports to apply these unrevealing tests. Of course in every case of this kind the intention that the particular crime be committed originates with the police, and without their inducement the crime would not have occurred. But it is perfectly clear from such decisions as the decoy letter cases in this Court, <i>e. g., </i><i>Grimm</i> v. <i>United States,</i> <span class="citation" data-id="94127"><a href="/opinion/94127/grimm-v-united-states/" aria-description="Citation for case: Grimm v. United States">156 U. S. 604</a></span>, where the police in effect simply furnished the opportunity for the commission of the crime, that this is not enough to enable the defendant to escape conviction.</p>
<p>The intention referred to, therefore, must be a general intention or predisposition to commit, whenever the opportunity should arise, crimes of the kind solicited, and in proof of such a predisposition evidence has often been admitted to show the defendant's reputation, criminal activities, and prior disposition. The danger of prejudice in such a situation, particularly if the issue of entrapment must be submitted to the jury and disposed of by a general verdict of guilty or innocent, is evident. The defendant must either forego the claim of entrapment or run the substantial risk that, in spite of instructions, the jury will allow a criminal record or bad reputation to weigh in its determination of guilt of the specific offense of which he stands charged. Furthermore, a test that looks to the character and predisposition of the defendant rather than the conduct of the police loses sight of the underlying reason for the defense of entrapment. No <span class="star-pagination">*383</span> matter what the defendant's past record and present inclinations to criminality, or the depths to which he has sunk in the estimation of society, certain police conduct to ensnare him into further crime is not to be tolerated by an advanced society. And in the present case it is clear that the Court in fact reverses the conviction because of the conduct of the informer Kalchinian, and not because the Government has failed to draw a convincing picture of petitioner's past criminal conduct. Permissible police activity does not vary according to the particular defendant concerned; surely if two suspects have been solicited at the same time in the same manner, one should not go to jail simply because he has been convicted before and is said to have a criminal disposition. No more does it vary according to the suspicions, reasonable or unreasonable, of the police concerning the defendant's activities. Appeals to sympathy, friendship, the possibility of exorbitant gain, and so forth, can no more be tolerated when directed against a past offender than against an ordinary law-abiding citizen. A contrary view runs afoul of fundamental principles of equality under law, and would espouse the notion that when dealing with the criminal classes anything goes. The possibility that no matter what his past crimes and general disposition the defendant might not have committed the particular crime unless confronted with inordinate inducements, must not be ignored. Past crimes do not forever outlaw the criminal and open him to police practices, aimed at securing his repeated conviction, from which the ordinary citizen is protected. The whole ameliorative hopes of modern penology and prison administration strongly counsel against such a view.</p>
<p>This does not mean that the police may not act so as to detect those engaged in criminal conduct and ready and willing to commit further crimes should the occasion arise. Such indeed is their obligation. It does mean <span class="star-pagination">*384</span> that in holding out inducements they should act in such a manner as is likely to induce to the commission of crime only these persons and not others who would normally avoid crime and through self-struggle resist ordinary temptations. This test shifts attention from the record and predisposition of the particular defendant to the conduct of the police and the likelihood, objectively considered, that it would entrap only those ready and willing to commit crime. It is as objective a test as the subject matter permits, and will give guidance in regulating police conduct that is lacking when the reasonableness of police suspicions must be judged or the criminal disposition of the defendant retrospectively appraised. It draws directly on the fundamental intuition that led in the first instance to the outlawing of "entrapment" as a prosecutorial instrument. The power of government is abused and directed to an end for which it was not constituted when employed to promote rather than detect crime and to bring about the downfall of those who, left to themselves, might well have obeyed the law. Human nature is weak enough and sufficiently beset by temptations without government adding to them and generating crime.</p>
<p>What police conduct is to be condemned, because likely to induce those not otherwise ready and willing to commit crime, must be picked out from case to case as new situations arise involving different crimes and new methods of detection. The <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> case involved persistent solicitation in the face of obvious reluctance, and appeals to sentiments aroused by reminiscences of experiences as companions in arms in the World War. Particularly reprehensible in the present case was the use of repeated requests to overcome petitioner's hesitancy, coupled with appeals to sympathy based on mutual experiences with narcotics addiction. Evidence of the setting in which the inducement took place is of course highly relevant in <span class="star-pagination">*385</span> judging its likely effect, and the court should also consider the nature of the crime involved, its secrecy and difficulty of detection, and the manner in which the particular criminal business is usually carried on.</p>
<p>As Mr. Justice Roberts convincingly urged in the <i><span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/" aria-description="Citation for case: Sorrells v. United States">Sorrells</a></span></i> case, such a judgment, aimed at blocking off areas of impermissible police conduct, is appropriate for the court and not the jury. "The protection of its own functions and the preservation of the purity of its own temple belongs only to the court. It is the province of the court and of the court alone to protect itself and the government from such prostitution of the criminal law. The violation of the principles of justice by the entrapment of the unwary into crime should be dealt with by the court no matter by whom or at what stage of the proceedings the facts are brought to its attention." <span class="citation" data-id="101997"><a href="/opinion/101997/sorrells-v-united-states/#457" aria-description="Citation for case: Sorrells v. United States">287 U. S., at 457</a></span> (separate opinion). Equally important is the consideration that a jury verdict, although it may settle the issue of entrapment in the particular case, cannot give significant guidance for official conduct for the future. Only the court, through the gradual evolution of explicit standards in accumulated precedents, can do this with the degree of certainty that the wise administration of criminal justice demands.</p>
<h2>NOTES</h2>
<p>[1]  The charge to the jury was not in issue here.</p>
<p>[2]  "Q. And it was your [Kalchinian's] job, was it not, while you were working with these agents to go out and try and induce somebody to sell you narcotics, isn't that true?
</p>
<p>.....</p>
<p>"A. No, it wasn't my job at all to do anything of the kind.</p>
<p>"Q. Do you remember this question [asked at the first trial] . . .</p>
<p>`Q. And it was your job while working with these agents to go out and try and induce a person to sell narcotics to you, isn't that correct?</p>
<p>A. I would say yes to that.' Do you remember that?</p>
<p>"A. If that is what I said, let it stand just that way.</p>
<p>.....</p>
<p>"Q. So when you testify now that it was not your job you are not telling the truth?</p>
<p>"A. I mean by job that nobody hired me for that. That is what I inferred, otherwise I meant the same thing in my answer to your question." R. 100.</p>
<p>[3]  "Q. But you had made a promise, an agreement, though, to co-operate with the Federal Bureau of Narcotics before you received a suspended sentence from the court?
</p>
<p>"A. [Kalchinian]. I had promised to cooperate in 1951.</p>
<p>"Q. And that was before your sentence?</p>
<p>"A. Yes, that was before my sentence." R. 99.</p>
<p>Kalchinian received a suspended sentence in 1952 after a statement by the United States Attorney to the Judge that he had been cooperative with the Government. R. 89, 98.</p>
<p>[4]  At one point Kalchinian did testify that he had previously received the same amount of narcotics at some unspecified lower price. He characterized this other price as "not quite" the price he paid petitioner. R. 80.</p>
<p>[5]  It is of interest to note that on the first appeal in this case the Court of Appeals came to the same conclusion as we do as to the evidence discussed so far. See <i>United States</i> v. <i>Sherman,</i> <span class="citation" data-id="230738"><a href="/opinion/230738/united-states-v-sherman/#883" aria-description="Citation for case: United States v. Sherman">200 F. 2d 880, 883</a></span>.</p>
<p>[6]  Cf. <i>e. g., </i><i>Lutfy</i> v. <i>United States,</i> <span class="citation" data-id="230073"><a href="/opinion/230073/lutfy-v-united-states/" aria-description="Citation for case: Lutfy v. United States">198 F. 2d 760</a></span>; <i>Wall</i> v. <i>United States,</i> <span class="citation" data-id="1477802"><a href="/opinion/1477802/wall-v-united-states/" aria-description="Citation for case: Wall v. United States">65 F. 2d 993</a></span>; <i>Butts</i> v. <i>United States,</i> <span class="citation" data-id="8820799"><a href="/opinion/8835759/butts-v-united-states/" aria-description="Citation for case: Butts v. United States">273 F. 35</a></span>.</p>
<p>[7]  In the first appeal of this case Judge Learned Hand stated: "Indeed, it would seem probable that, if there were no reply [to the claim of inducement], it would be impossible ever to secure convictions of any offences which consist of transactions that are carried on in secret." <i>United States</i> v. <i>Sherman,</i> <span class="citation" data-id="230738"><a href="/opinion/230738/united-states-v-sherman/#882" aria-description="Citation for case: United States v. Sherman">200 F. 2d 880, 882</a></span>.</p>
<p>[8]  For example, in the following cases the courts have, in affirming convictions, held that the issue of entrapment had been properly submitted to the jury. <i>United States</i> v. <i>Lindenfeld,</i> <span class="citation" data-id="1551253"><a href="/opinion/1551253/united-states-v-lindenfeld/" aria-description="Citation for case: United States v. Lindenfeld">142 F. 2d 829</a></span> (C. A. 2d Cir.); <i>United States</i> v. <i>Brandenburg,</i> <span class="citation" data-id="1548320"><a href="/opinion/1548320/united-states-v-brandenburg/" aria-description="Citation for case: United States v. Brandenburg">162 F. 2d 980</a></span> (C. A. 3d Cir.); <i>Demos</i> v. <i>United States,</i> <span class="citation" data-id="232111"><a href="/opinion/232111/demos-v-united-states/" aria-description="Citation for case: Demos v. United States">205 F. 2d 596</a></span> (C. A. 5th Cir.); <i>Nero</i> v. <i>United States,</i> <span class="citation" data-id="227266"><a href="/opinion/227266/nero-v-united-states/" aria-description="Citation for case: Nero v. United States">189 F. 2d 515</a></span> (C. A. 6th Cir.); <i>United States</i> v. <i>Cerone,</i> <span class="citation" data-id="6891078"><a href="/opinion/6992500/united-states-v-cerone/" aria-description="Citation for case: United States v. Cerone">150 F. 2d 382</a></span> (C. A. 7th Cir.); <i>Louie Hung</i> v. <i>United States,</i> <span class="citation" data-id="6880383"><a href="/opinion/6982438/hung-v-united-states/" aria-description="Citation for case: Hung v. United States">111 F. 2d 325</a></span> (C. A. 9th Cir.); <i>Ryles</i> v. <i>United States,</i> <span class="citation" data-id="225592"><a href="/opinion/225592/ryles-v-united-states/" aria-description="Citation for case: Ryles v. United States">183 F. 2d 944</a></span> (C. A. 10th Cir.); <i>Cratty</i> v. <i>United States,</i> 82 U. S. App. D. C. 236, <span class="citation" data-id="1498526"><a href="/opinion/1498526/cratty-v-united-states/" aria-description="Citation for case: Cratty v. United States">163 F. 2d 844</a></span>. And in the following cases the courts have reversed convictions where the issue of entrapment was either not submitted to the jury or was submitted on improper instructions. <i>United States</i> v. <i>Sherman,</i> <span class="citation" data-id="230738"><a href="/opinion/230738/united-states-v-sherman/" aria-description="Citation for case: United States v. Sherman">200 F. 2d 880</a></span> (C. A. 2d Cir.); <i>United States</i> v. <i>Sawyer,</i> <span class="citation" data-id="233333"><a href="/opinion/233333/united-states-v-sawyer/" aria-description="Citation for case: United States v. Sawyer">210 F. 2d 169</a></span> (C. A. 3d Cir.); <i>Wall</i> v. <i>United States,</i> <span class="citation" data-id="1477802"><a href="/opinion/1477802/wall-v-united-states/" aria-description="Citation for case: Wall v. United States">65 F. 2d 993</a></span> (C. A. 5th Cir.); <i>Lutfy</i> v. <i>United States,</i> <span class="citation" data-id="230073"><a href="/opinion/230073/lutfy-v-united-states/" aria-description="Citation for case: Lutfy v. United States">198 F. 2d 760</a></span> (C. A. 9th Cir.); <i>Yep</i> v. <i>United States,</i> <span class="citation" data-id="9637386"><a href="/opinion/1479180/yep-v-united-states/" aria-description="Citation for case: Yep v. United States">83 F. 2d 41</a></span> (C. A. 10th Cir.).</p>
<p>[1]  Excellent discussions of the problem can be found in Mikell, The Doctrine of Entrapment in the Federal Courts, <span class="citation no-link">90 U. Pa. L. Rev. 245</span>; Donnelly, Judicial Control of Informants, Spies, Stool Pigeons, and Agent Provocateurs, 60 Yale L. J. 1091, 1098-1115; Note, Entrapment by Government Officials, 28 Col. L. Rev. 1067.</p>
<p>[2]  It is of course not a rigid rule of this Court to restrict consideration of a case merely to arguments advanced by counsel. Presumably certiorari was not granted in this case simply to review the evidence under an accepted rule of law. The solution, when an issue of real importance to the administration of criminal justice has not been argued by counsel, is not to perpetuate a bad rule but to set the case down for reargument with a view to re-examining that rule.</p>

</div>
```

---

## GROUP: content/cases/Shipley v. California.md  (`case`, 5 assertions)

### content_page

```
---
title: "Shipley v. California"
type: case
citation: "395 U.S. 818 (1969)"
parallel_cite: "89 S. Ct. 2053; 23 L. Ed. 2d 732"
neutral_cite: 1969 U.S. LEXIS 1169
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1969
date_decided: 1969-06-23
docket: "540, Misc."
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1969-06-23
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Shipley v. California
  varies_by_point: false
  scope_note: "Per curiam, decided the same day as Chimel v. California; applies the search-incident-to-arrest limits. No negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107982/shipley-v-california/"
  cluster_id: 107982
  opinion_id: 107982
  identity_checked: true
homes:
  - page: "[[SIA Persons]]"
    role: "Key — Limiting (contemporaneity)"
related: ["[[Chimel v. California]]", "[[Agnello v. United States]]", "[[Go-Bart Importing Co. v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "home", "warrant-requirement"]
holding: "Police may not search a home as incident to an arrest made outside it; a search is incident to arrest only if substantially contemporaneous with the arrest and confined to the immediate vicinity of the arrest."
lake:
  record_id: Shipley v. California
  status: verified
  projected_at: 2026-07-06
---

# Shipley v. California

*395 U.S. 818 (1969)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police, informed that Shipley was involved in a robbery, went to his home while he was out; a 15-year-old who said she was his wife let them in, and they found stolen rings. The officers staked out the house and arrested Shipley as he stepped from his car — parked 15 to 20 feet from the house — late that night. After searching him and the car, they re-entered the house without a warrant and found a stolen jewelry case under a couch. The state courts upheld the second search as incident to the arrest.

## Issue
Whether police may search a person's home as incident to an arrest made outside the home, without a warrant.

## Rule
No. "The Court has consistently held that a search 'can be incident to an arrest only if it is substantially contemporaneous with the arrest and is confined to the *immediate* vicinity of the arrest.'" — 395 U.S. at 819–820 (quoting *Stoner v. California*, 376 U.S. at 486). ^pin-819

A home is not searchable as incident to an arrest made outside it: "the Constitution has never been construed by this Court to allow the police, in the absence of an emergency, to arrest a person *outside* his home and then take him inside for the purpose of conducting a warrantless search. . . . [I]t has always been assumed that one's house cannot lawfully be searched without a search warrant, except as an incident to a lawful arrest *therein*." — *Id.* at 820 (quoting *Agnello*, 269 U.S. at 32). ^pin-820

## Application
Shipley was arrested outside, by his car, not inside his home. Under *[[Chimel v. California]]* (decided the same day), the search of the house plainly exceeded the limits on [[Search Incident to Arrest|searches incident to arrest]]; and even apart from *[[Chimel v. California|Chimel]]*, no precedent justified it, because the search "extended without reasonable justification beyond the place in which he was arrested." There was no emergency, and the officers never obtained a warrant for the home.

## Conclusion
Reversed (per curiam). A warrantless search of the home, incident to an arrest made outside it, cannot be sustained under the Fourth and Fourteenth Amendments.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- Decided the same day as [[Chimel v. California]] and applying its limits; consistent with [[Agnello v. United States]] (SITA does not reach a separate home) and [[Go-Bart Importing Co. v. United States]] (no general exploratory search).

## Appears on
- [[SIA Persons]] — *Key — Limiting (contemporaneity)*

## Sources
- *Shipley v. California*, 395 U.S. 818 (1969) — https://www.courtlistener.com/opinion/107982/shipley-v-california/ — pinpoints: 819, 820.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "ef9a2c13b825f361", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "395 U.S. 818 (1969)", "court": "U.S. Supreme Court", "neutral_cite": "1969 U.S. LEXIS 1169", "official_citation_present": true, "parallel_cite": "89 S. Ct. 2053; 23 L. Ed. 2d 732", "title": "Shipley v. California", "year": "1969"}}
{"assertion_id": "998c612f55436638", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Key — Limiting (contemporaneity)", "title": "Shipley v. California"}}
{"assertion_id": "f78dd7944b78529a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Police may not search a home as incident to an arrest made outside it; a search is incident to arrest only if substantially contemporaneous with the arrest and confined to the immediate vicinity of the arrest.", "title": "Shipley v. California"}}
{"assertion_id": "7519ba6e14a7e24b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Shipley v. California"}}
{"assertion_id": "d7dd69d8008da613", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1969-06-23", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Shipley v. California", "field_i_validity": "good_law", "scope_note": "Per curiam, decided the same day as Chimel v. California; applies the search-incident-to-arrest limits. No negative treatment.", "title": "Shipley v. California", "varies_by_point": "false"}}
```

### lake record — Shipley v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Shipley v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Shipley v. California",
    "case_name_short": "Shipley",
    "case_name_full": "Shipley v. California",
    "input_case_name": "Shipley v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1969-06-23",
    "year": 1969,
    "docket": "540, Misc.",
    "cluster_id": 107982,
    "lead_opinion_id": 107982,
    "sibling_ids": [
      107982,
      9424104,
      9424105
    ],
    "absolute_url": "/opinion/107982/shipley-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "395 U.S. 818",
      "volume": "395",
      "reporter": "U.S.",
      "page": "818",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "89 S. Ct. 2053",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "2053",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 L. Ed. 2d 732",
        "volume": "23",
        "reporter": "L. Ed. 2d",
        "page": "732",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1969 U.S. LEXIS 1169",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1169",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "395 U.S. 818",
        "volume": "395",
        "reporter": "U.S.",
        "page": "818",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "89 S. Ct. 2053",
        "volume": "89",
        "reporter": "S. Ct.",
        "page": "2053",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 L. Ed. 2d 732",
        "volume": "23",
        "reporter": "L. Ed. 2d",
        "page": "732",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1969 U.S. LEXIS 1169",
        "volume": "1969",
        "reporter": "U.S. LEXIS",
        "page": "1169",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "395 U.S. 818",
    "official_selection": {
      "court_class": "scotus",
      "selected": "395 U.S. 818",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-819",
      "page": null,
      "quote": "--- # Shipley v. California *395 U.S. 818 (1969)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Police, informed that Shipley was involved in a robbery, went to his home while he was out; a 15-year-old who said she was his wife let them in, and they found stolen rings. The officers staked out the house and arrested Shipley as he stepped from his car \u2014 parked 15 to 20 feet from the house \u2014 late that night. After searching him and the car, they re-entered the house without a warrant and found a stolen jewelry case under a couch. The state courts upheld the second search as incident to the arrest. ## Issue Whether police may search a person's home as incident to an arrest made outside the home, without a warrant. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-820",
      "page": null,
      "quote": "the Constitution has never been construed by this Court to allow the police, in the absence of an emergency, to arrest a person *outside* his home and then take him inside for the purpose of conducting a warrantless search. . . . [I]t has always been assumed that one's house cannot lawfully be searched without a search warrant, except as an incident to a lawful arrest *therein*.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1969-06-23",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Shipley v. California",
    "varies_by_point": false,
    "scope_note": "Per curiam, decided the same day as Chimel v. California; applies the search-incident-to-arrest limits. No negative treatment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Johnson",
          "cluster_id": 4603999,
          "cite": [
            "119 N.E.3d 669",
            "481 Mass. 710"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Joseph Rodney Thomas",
          "cluster_id": 292358,
          "cite": [
            "432 F.2d 120"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Eugene E. Thweatt",
          "cluster_id": 293070,
          "cite": [
            "433 F.2d 1226",
            "140 U.S. App. D.C. 120",
            "1970 U.S. App. LEXIS 8425"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ralph F. Deleo",
          "cluster_id": 288700,
          "cite": [
            "422 F.2d 487"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Thornton v. State",
          "cluster_id": 1630935,
          "cite": [
            "451 S.W.2d 898",
            "1970 Tex. Crim. App. LEXIS 1399"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane1_negative"
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
        "journal_ref": "Shipley v. California:lane2_top_cited"
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
        "journal_ref": "Shipley v. California:lane2_top_cited"
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
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vale v. Louisiana",
          "cluster_id": 108183,
          "cite": [
            "26 L. Ed. 2d 409",
            "90 S. Ct. 1969",
            "399 U.S. 30",
            "1970 U.S. LEXIS 18"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Edwards",
          "cluster_id": 1423047,
          "cite": [
            "458 P.2d 713",
            "71 Cal. 2d 1096",
            "80 Cal. Rptr. 633",
            "1969 Cal. LEXIS 306"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cherry",
          "cluster_id": 1310686,
          "cite": [
            "257 S.E.2d 551",
            "298 N.C. 86",
            "1979 N.C. LEXIS 1366"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Orlando Vasquez, Carlos Sanchez, Fernando Eugenio Medina, Amparo Valencia Medina, Clara Inez Mesa and Hernando Mesa",
          "cluster_id": 386016,
          "cite": [
            "638 F.2d 507",
            "1980 U.S. App. LEXIS 11022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Montana v. Hall",
          "cluster_id": 111872,
          "cite": [
            "95 L. Ed. 2d 354",
            "107 S. Ct. 1825",
            "481 U.S. 400",
            "1987 U.S. LEXIS 1822",
            "55 U.S.L.W. 3727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas D. Harris",
          "cluster_id": 293551,
          "cite": [
            "435 F.2d 74"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clarence Williams and Arlene Jackson v. United States",
          "cluster_id": 287204,
          "cite": [
            "418 F.2d 159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paprskar v. State",
          "cluster_id": 2408008,
          "cite": [
            "484 S.W.2d 731",
            "1972 Tex. Crim. App. LEXIS 1935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Luis Marti and Lou Saks",
          "cluster_id": 288501,
          "cite": [
            "421 F.2d 1263",
            "1970 U.S. App. LEXIS 10891"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. United States",
          "cluster_id": 110612,
          "cite": [
            "454 U.S. 975",
            "102 S. Ct. 528",
            "50 U.S.L.W. 3343",
            "70 L. Ed. 2d 396",
            "1981 U.S. LEXIS 4345"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Adiel F. Gonzales v. Dr. George J. Beto, Director, Texas Department of Corrections, Joe Givas Acosta v. Dr. George J. Beto, Director, Texas Department of Corrections, and the Stateof Texas",
          "cluster_id": 289944,
          "cite": [
            "425 F.2d 963"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Simonson",
          "cluster_id": 4255842,
          "cite": [
            "148 A.3d 792",
            "2016 Pa. Super. 207",
            "2016 Pa. Super. LEXIS 527",
            "2016 WL 4743498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Diaz",
          "cluster_id": 8443247,
          "cite": [
            "854 F.3d 197",
            "2017 WL 1379188",
            "2017 U.S. App. LEXIS 6579"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Cullison",
          "cluster_id": 1600328,
          "cite": [
            "173 N.W.2d 533",
            "1970 Iowa Sup. LEXIS 742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sanchez",
          "cluster_id": 171758,
          "cite": [
            "555 F.3d 910",
            "2009 U.S. App. LEXIS 2474",
            "2009 WL 311267"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. State",
          "cluster_id": 1958185,
          "cite": [
            "256 A.2d 384",
            "7 Md. App. 505",
            "1969 Md. App. LEXIS 354"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Filmon v. State",
          "cluster_id": 1804266,
          "cite": [
            "336 So. 2d 586"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Anthony Carlo Cozzetti, United States of America v. Michael Miller, Also Known as Michael Rosenthal, United States of America v. Ronald Ernest Gilmour",
          "cluster_id": 296147,
          "cite": [
            "441 F.2d 344"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Shipley v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107982 OR 9424104 OR 9424105) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 75,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 75,
        "triage_read": 5,
        "triage_snippet_classified": 70
      },
      "lane2_top_cited": {
        "query": "cites:(107982 OR 9424104 OR 9424105)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNCZzPTIxODMxNDImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107982+OR+9424104+OR+9424105%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107982 OR 9424104 OR 9424105)",
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
    "complete_query": "cites:(107982 OR 9424104 OR 9424105)",
    "indexed_citing_opinions": 95,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107982,
        "count": 90,
        "count_source": "search"
      },
      {
        "opinion_id": 9424104,
        "count": 8,
        "count_source": "search"
      },
      {
        "opinion_id": 9424105,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 145,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/shipley-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wLjY5Njk1Mjc2JnM9MTIxMjQyOSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107982+OR+9424104+OR+9424105%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107982,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107982,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107982,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107982,
        "cited_id": 105502,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107982,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107982,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107982,
        "cited_id": 107102,
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
    "date_created": "2026-07-05T19:29:13Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:29:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:29:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:34:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:29:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Shipley v. California

```
<div>
<center><b><span class="citation" data-id="9424104"><a href="/opinion/107982/shipley-v-california/" aria-description="Citation for case: Shipley v. California">395 U.S. 818</a></span> (1969)</b></center>
<center><h1>SHIPLEY<br>
v.<br>
CALIFORNIA.</h1></center>
<center>No. 540, Misc.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Decided June 23, 1969.</center>
ON PETITION FOR WRIT OF CERTIORARI TO THE COURT OF APPEAL OF CALIFORNIA, SECOND APPELLATE DISTRICT.
<p><i>Kate Whyner</i> for petitioner.</p>
<p><i>Thomas C. Lynch,</i> Attorney General of California, <i>William E. James,</i> Assistant Attorney General, and <i>Marvin A. Bauer,</i> Deputy Attorney General, for respondent.</p>
<p>PER CURIAM.</p>
<p>The petitioner was convicted in California of robbery in the first degree, and the conviction was affirmed by the Court of Appeal, Second Appellate District. The California Supreme Court denied review. The petitioner seeks reversal of the judgment below on the ground that evidence introduced at his trial was seized in violation <span class="star-pagination">*819</span> of the Fourth and Fourteenth Amendments to the United States Constitution. Since we agree with the petitioner that the evidence was taken in the course of an unconstitutional search of his home, the judgment of the California Court of Appeal must be reversed. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>.</p>
<p>Informed that the petitioner had been involved in a robbery, police officers went to his residence. The petitioner was not at home, but a 15-year-old girl who identified herself as the petitioner's wife allowed the officers to enter and search her belongings. When several rings taken by the robbers were found, the officers "staked out" the house and awaited the petitioner's return. Upon his arrival late that night, he was immediately arrested as he alighted from his car. The officers searched the petitioner and the car, and then again entered and searched the house, where they discovered under a couch a jewelry case stolen in the robbery. The car was parked outside the house and 15 or 20 feet away from it, and the officers did not request permission to conduct the second search of the house. No warrant was ever obtained. The trial court nevertheless upheld the second search on the ground that it was incident to the petitioner's arrest, and the Court of Appeal agreed, holding that the area searched was "under the [petitioner's] effective control" at the time of the arrest.</p>
<p>Under our decision today in <i>Chimel</i> v. <i>California, ante,</i> p. 752, the search clearly exceeded Fourth Amendment limitations on searches incident to arrest. But even if <i>Chimel</i> were to have no retroactive applicationa question which we reserve for a case which requires its resolutionthere is no precedent of this Court that justifies the search in this case. The Court has consistently held that a search "can be incident to an arrest only if it is substantially contemporaneous with the arrest and is confined to the <i>immediate</i> vicinity of the arrest." <span class="star-pagination">*820</span> <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/#486" aria-description="Citation for case: Stoner v. California">376 U. S. 483, 486</a></span>. (Emphasis supplied.) At the very most, police officers have been permitted to search a four-room apartment in which the arrest took place. <i>Harris</i> v. <i>United States,</i> <span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span>. See also <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>. But the Constitution has never been construed by this Court to allow the police, in the absence of an emergency, to arrest a person <i>outside</i> his home and then take him inside for the purpose of conducting a warrantless search. On the contrary, "it has always been assumed that one's house cannot lawfully be searched without a search warrant, except as an incident to a lawful arrest <i>therein.</i>" <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#32" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 32</a></span>. (Emphasis supplied.) And in <i>James</i> v. <i>Louisiana,</i> <span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/" aria-description="Citation for case: James v. Louisiana">382 U. S. 36</a></span>, the Court held that the search of the petitioner's home after his arrest on the street two blocks away "cannot be regarded as incident to his arrest." <span class="citation" data-id="107102"><a href="/opinion/107102/james-v-louisiana/#37" aria-description="Citation for case: James v. Louisiana"><i>Id.,</i> at 37</a></span>. Since the thorough search of the petitioner's home extended without reasonable justification beyond the place in which he was arrested, it cannot be upheld under the Fourth and Fourteenth Amendments as incident to his arrest.<sup>[*]</sup></p>
<p>Accordingly, the motion for leave to proceed <i>in forma pauperis</i> and the petition for a writ of certiorari are granted, the judgment is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE BLACK concurs in granting certiorari but dissents from the reversal and remand of the judgment without a hearing.</p>
<p><span class="star-pagination">*821</span> MR. JUSTICE WHITE, dissenting.</p>
<p>I found inexplicable the Court's acceptance of the warrantless arrest in <i>Chimel</i> v. <i>California, ante,</i> p. 752, while at the same time holding the contemporaneous search invalid without considering the exigencies created by the arrest itself. See <i>id.,</i> p. 770 (dissenting opinion). Even more mystifying are the opinions and the orders issued in the instant case and six others which have been held pending the decision in <i>Chimel:</i> No. 837, <i>Von Cleef</i> v. <i>New Jersey, ante,</i> p. 814; No. 1097, Misc., <i>Harris</i> v. <i>Illinois, post,</i> p. 985; No. 1037, Misc., <i>Mahoney</i> v. <i>LaVallee, post,</i> p. 985; No. 500, <i>Schmear</i> v. <i>Gagnon, post,</i> p. 978; No. 550, Misc., <i>Jamison</i> v. <i>United States, post,</i> p. 986; and No. 395, Misc., <i>Chrisman</i> v. <i>California, post,</i> p. 985. I fear that the summary dispositions in these cases, which strain so hard to avoid deciding the retroactivity of <i>Chimel,</i> will only magnify the confusion in this important area of the law.</p>
<p>It is particularly hard to square the Court's summary reversal of Shipley's conviction, which invalidates a warrantless search of a house where the arrest was made in a detached garage, with the denials of certiorari in <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i>Mahoney.</i> In <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span>,</i> the arrest occurred in the lobby of a four-story apartment building; the ensuing search without a warrant involved an apartment on an upper floor. The chronology was reversed in <i>Mahoney</i> where petitioner was arrested in his apartment, but the accompanying search uncovered a gun in the building basement. This case, <i>Shipley,</i> purports to rest on pre-<i>Chimel</i> law, but certiorari in <i><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span></i> and <i>Mahoney</i> cannot be denied without assuming the nonretroactivity of <i>Chimel</i> and then determining that these cases do not deserve the same summary reversal given to <i>Shipley.</i> In <i>Schmear, Jamison,</i> and <i>Chrisman,</i> as in <i>Chimel,</i> the Court fails to find a substantial issue in the warrantless <span class="star-pagination">*822</span> arrest and its bearing on the warrantless search. Finally, the <i>per curiam</i> in <i>Von Cleef</i> invokes <i>Kremen</i> v. <i>United States,</i> <span class="citation" data-id="8931353"><a href="/opinion/8940894/kremen-v-united-states/" aria-description="Citation for case: Kremen v. United States">353 U. S. 346</a></span> (1957), without noting that the seizures in <i>Von Cleef</i> were limited to evidence and instrumentalities of the crimes being investigated and for which the arrests were made.</p>
<p>I join the grant of certiorari in this case but dissent from the summary reversal.</p>
<h2>NOTES</h2>
<p>[*]  Because of our disposition of the case on this ground, we find it unnecessary to consider the contentions of the petitioner that his "wife" did not voluntarily consent to the first search, and that the office lacked probable cause to arrest the petitioner.</p>

</div>
```

---

## GROUP: content/cases/Sibron v. New York.md  (`case`, 5 assertions)

### content_page

```
---
title: "Sibron v. New York"
type: case
citation: "392 U.S. 40 (1968)"
parallel_cite: "88 S. Ct. 1889; 20 L. Ed. 2d 917; 44 Ohio Op. 2d 402"
neutral_cite: 1968 U.S. LEXIS 1346
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-10
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-10
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Sibron v. New York
  varies_by_point: false
  scope_note: "Good law. A protective frisk is confined to a limited pat-down of outer clothing for weapons on reasonable grounds the suspect is armed and dangerous; reaching directly into a pocket for narcotics exceeds Terry. Decided the same day as, and as a companion to, Terry v. Ohio (consolidated with Peters v. New York)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107730/sibron-v-new-york/"
  cluster_id: 107730
  opinion_id: 107730
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Limiting"
related: ["[[Terry v. Ohio]]", "[[Peters v. New York]]", "[[Minnesota v. Dickerson]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "frisk", "scope-of-search", "weapons"]
holding: "A protective frisk must be a limited pat-down of outer clothing for weapons, justified by particular facts that the suspect is armed and dangerous; reaching into a pocket to search for narcotics exceeds the scope Terry allows."
lake:
  record_id: Sibron v. New York
  status: verified
  projected_at: 2026-07-06
---

# Sibron v. New York

*392 U.S. 40 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Patrolman Martin watched Nelson Sibron over an eight-hour period talking with several persons the officer knew to be narcotics addicts, but he heard none of the conversations. In a restaurant, Martin approached Sibron and said, "You know what I am after." When Sibron reached into his pocket, Martin thrust his own hand into the same pocket and pulled out glassine envelopes of heroin. Sibron was convicted of unlawful possession of heroin; New York defended the search as a self-protective frisk authorized by its stop-and-frisk statute (§ 180-a). The case was decided with *[[Terry v. Ohio]]* and the companion case *[[Peters v. New York]]*.

## Issue
Whether seizing heroin from a suspect's pocket can be sustained as a *[[Terry v. Ohio|Terry]]* self-protective frisk, where the officer reached directly into the pocket searching for narcotics without first conducting a limited pat-down for weapons and without particular facts indicating the suspect was armed and dangerous.

## Rule
No. A frisk must rest on reasonable grounds and be confined to weapons: "Before he places a hand on the person of a citizen in search of anything, he must have constitutionally adequate, reasonable grounds for doing so. In the case of the self-protective search for weapons, he must be able to point to particular facts from which he reasonably inferred that the individual was armed and dangerous." — 392 U.S. at 64. ^pin-64

Even assuming grounds to frisk existed, the *scope* of this search exceeded what *[[Terry v. Ohio|Terry]]* permits: "Even assuming *arguendo* that there were adequate grounds to search Sibron for weapons, the nature and scope of the search conducted by Patrolman Martin were so clearly unrelated to that justification as to render the heroin inadmissible." — *Id.* at 65. ^pin-65

"In this case, with no attempt at an initial limited exploration for arms, Patrolman Martin thrust his hand into Sibron's pocket and took from him envelopes of heroin. . . . The search was not reasonably limited in scope to the accomplishment of the only goal which might conceivably have justified its inception — the protection of the officer by disarming a potentially dangerous man." — *Id.* at 65–66. ^pin-65b

## Application
Martin pointed to no facts suggesting Sibron was armed; merely talking with known addicts "no more gives rise to reasonable fear of life or limb on the part of the police officer than it justifies an arrest." Nor did Martin claim he feared Sibron was reaching for a weapon — his statement "You know what I am after" and his hearing testimony showed he was searching for narcotics. Because he reached straight into the pocket for drugs without any initial pat-down for weapons, the search was unrelated to the only justification (officer safety) and the heroin was inadmissible.

## Conclusion
The heroin was the product of a search that exceeded the scope of a lawful *[[Terry v. Ohio|Terry]]* frisk, and the conviction was reversed. A protective frisk is limited to a pat-down for weapons supported by particular facts of danger; it may not be used as a search for evidence.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *[[Peters v. New York|Sibron]]*'s scope limit on the protective frisk remains good law alongside [[Terry v. Ohio]]; [[Minnesota v. Dickerson]] later held that contraband whose identity is immediately apparent by "plain feel" during a lawful weapons frisk may be seized, but that exception does not authorize the manipulating or pocket-reaching search *[[Peters v. New York|Sibron]]* condemned. Consolidated with [[Peters v. New York]], where a search on probable cause was upheld.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Limiting*

## Sources
- *Sibron v. New York*, 392 U.S. 40 (1968) — https://www.courtlistener.com/opinion/107730/sibron-v-new-york/ — pinpoints: 64, 65–66.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a146a5bc81589902", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "392 U.S. 40 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 1346", "official_citation_present": true, "parallel_cite": "88 S. Ct. 1889; 20 L. Ed. 2d 917; 44 Ohio Op. 2d 402", "title": "Sibron v. New York", "year": "1968"}}
{"assertion_id": "af38fa7071b6b382", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A protective frisk must be a limited pat-down of outer clothing for weapons, justified by particular facts that the suspect is armed and dangerous; reaching into a pocket to search for narcotics exceeds the scope Terry allows.", "title": "Sibron v. New York"}}
{"assertion_id": "d1ab2b850cce5a6e", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Limiting", "title": "Sibron v. New York"}}
{"assertion_id": "2eb8238c29b1048f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Sibron v. New York"}}
{"assertion_id": "a8c7b2c0fec758de", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-06-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Sibron v. New York", "field_i_validity": "good_law", "scope_note": "Good law. A protective frisk is confined to a limited pat-down of outer clothing for weapons on reasonable grounds the suspect is armed and dangerous; reaching directly into a pocket for narcotics exceeds Terry. Decided the same day as, and as a companion to, Terry v. Ohio (consolidated with Peters v. New York).", "title": "Sibron v. New York", "varies_by_point": "false"}}
```

### lake record — Sibron v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Sibron v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Sibron v. New York",
    "case_name_short": "Sibron",
    "case_name_full": "Sibron v. New York",
    "input_case_name": "Sibron v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": null,
    "cluster_id": 107730,
    "lead_opinion_id": 107730,
    "sibling_ids": [
      107730,
      9423756,
      9423757,
      9423758,
      9423759,
      9423760,
      9423761,
      9423762
    ],
    "absolute_url": "/opinion/107730/sibron-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 40",
      "volume": "392",
      "reporter": "U.S.",
      "page": "40",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 1889",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 917",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 402",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "402",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 1346",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1346",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 40",
        "volume": "392",
        "reporter": "U.S.",
        "page": "40",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 1889",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "1889",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 917",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "917",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 1346",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "1346",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "44 Ohio Op. 2d 402",
        "volume": "44",
        "reporter": "Ohio Op. 2d",
        "page": "402",
        "type": 2,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 40",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 40",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-64",
      "page": null,
      "quote": "When Sibron reached into his pocket, Martin thrust his own hand into the same pocket and pulled out glassine envelopes of heroin. Sibron was convicted of unlawful possession of heroin; New York defended the search as a self-protective frisk authorized by its stop-and-frisk statute (\u00a7 180-a). The case was decided with *Terry v. Ohio* and the companion case *Peters v. New York*. ## Issue Whether seizing heroin from a suspect's pocket can be sustained as a *Terry* self-protective frisk, where the officer reached directly into the pocket searching for narcotics without first conducting a limited pat-down for weapons and without particular facts indicating the suspect was armed and dangerous. ## Rule No. A frisk must rest on reasonable grounds and be confined to weapons:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-65",
      "page": null,
      "quote": "Even assuming *arguendo* that there were adequate grounds to search Sibron for weapons, the nature and scope of the search conducted by Patrolman Martin were so clearly unrelated to that justification as to render the heroin inadmissible.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-65b",
      "page": null,
      "quote": "In this case, with no attempt at an initial limited exploration for arms, Patrolman Martin thrust his hand into Sibron's pocket and took from him envelopes of heroin. . . . The search was not reasonably limited in scope to the accomplishment of the only goal which might conceivably have justified its inception \u2014 the protection of the officer by disarming a potentially dangerous man.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-10",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Sibron v. New York",
    "varies_by_point": false,
    "scope_note": "Good law. A protective frisk is confined to a limited pat-down of outer clothing for weapons on reasonable grounds the suspect is armed and dangerous; reaching directly into a pocket for narcotics exceeds Terry. Decided the same day as, and as a companion to, Terry v. Ohio (consolidated with Peters v. New York).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. K.B.",
          "cluster_id": 10581696,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Powell",
          "cluster_id": 9409078,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. McGann",
          "cluster_id": 4736928,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "D.L. v. Sheppard Pratt Health Sys.",
          "cluster_id": 4649052,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "D.L. v. Sheppard Pratt Health Sys.",
          "cluster_id": 4647891,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wanda Horn v. Timothy Arnold Horn",
          "cluster_id": 4522724,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Perez",
          "cluster_id": 7172931,
          "cite": [
            "96 N.E.3d 772",
            "31 N.Y.3d 964",
            "73 N.Y.S.3d 508"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Sean Garvin",
          "cluster_id": 4436829,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Steiner",
          "cluster_id": 4345072,
          "cite": [
            "847 F.3d 103",
            "102 Fed. R. Serv. 711",
            "2017 WL 437657",
            "2017 U.S. App. LEXIS 1823"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Gordon v. Loretta E. Lynch",
          "cluster_id": 3191464,
          "cite": [
            "422 U.S. App. D.C. 30",
            "817 F.3d 804",
            "2016 U.S. App. LEXIS 6175",
            "2016 WL 1319282"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Callahan v. Unified Govt of Wyandotte",
          "cluster_id": 3154974,
          "cite": [
            "806 F.3d 1022",
            "2015 U.S. App. LEXIS 19872",
            "2015 WL 7172922"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Missouri v. Nicholas Carr",
          "cluster_id": 2731166,
          "cite": [
            "441 S.W.3d 166",
            "2014 Mo. App. LEXIS 997",
            "2014 WL 4411614"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane1_negative"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "North Carolina v. Pearce",
          "cluster_id": 107978,
          "cite": [
            "23 L. Ed. 2d 656",
            "89 S. Ct. 2072",
            "395 U.S. 711",
            "1969 U.S. LEXIS 1165"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Benton v. Maryland",
          "cluster_id": 107980,
          "cite": [
            "23 L. Ed. 2d 707",
            "89 S. Ct. 2056",
            "395 U.S. 784",
            "1969 U.S. LEXIS 1167"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Spencer v. Kemna",
          "cluster_id": 118176,
          "cite": [
            "140 L. Ed. 2d 43",
            "118 S. Ct. 978",
            "523 U.S. 1",
            "1998 U.S. LEXIS 1597"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evitts v. Lucey",
          "cluster_id": 111302,
          "cite": [
            "83 L. Ed. 2d 821",
            "105 S. Ct. 830",
            "469 U.S. 387",
            "1985 U.S. LEXIS 42"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Powell v. McCormack",
          "cluster_id": 107969,
          "cite": [
            "23 L. Ed. 2d 491",
            "89 S. Ct. 1944",
            "395 U.S. 486",
            "1969 U.S. LEXIS 3103"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. De Bour",
          "cluster_id": 5682261,
          "cite": [
            "40 N.Y.2d 210",
            "386 N.Y.S.2d 375",
            "1976 N.Y. LEXIS 2873",
            "352 N.E.2d 562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Dickerson",
          "cluster_id": 112873,
          "cite": [
            "124 L. Ed. 2d 334",
            "113 S. Ct. 2130",
            "508 U.S. 366",
            "1993 U.S. LEXIS 4018"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
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
        "journal_ref": "Sibron v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDA3MTk2ODAwMDAwJnM9MjcwODMzNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107730+OR+9423756+OR+9423757+OR+9423758+OR+9423759+OR+9423760+OR+9423761+OR+9423762%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTcwJnM9MTExODM1JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28107730+OR+9423756+OR+9423757+OR+9423758+OR+9423759+OR+9423760+OR+9423761+OR+9423762%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762)",
        "reviewed": 44,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 44,
        "triage_read": 1,
        "triage_snippet_classified": 43
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107730 OR 9423756 OR 9423757 OR 9423758 OR 9423759 OR 9423760 OR 9423761 OR 9423762)",
    "indexed_citing_opinions": 2550,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107730,
        "count": 2329,
        "count_source": "search"
      },
      {
        "opinion_id": 9423756,
        "count": 293,
        "count_source": "search"
      },
      {
        "opinion_id": 9423757,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423758,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423759,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423760,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423761,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423762,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4328,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/sibron-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjU2ODcmcz0xMDM2MDczMiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28107730+OR+9423756+OR+9423757+OR+9423758+OR+9423759+OR+9423760+OR+9423761+OR+9423762%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107730,
        "cited_id": 91800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 101682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 103481,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 103610,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 103823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105176,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107360,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107483,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107679,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107730,
        "cited_id": 107689,
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
    "date_created": "2026-07-05T19:34:15Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:34:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:34:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:36:35Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:34:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Sibron v. New York

```
<div>
<center><b><span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U.S. 40</a></span> (1968)</b></center>
<center><h1>SIBRON<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 63.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 11-12, 1967.</center>
<center>Decided June 10, 1968.<sup>[*]</sup></center>
APPEAL FROM THE COURT OF APPEALS OF NEW YORK.
<p><span class="star-pagination">*42</span> <i>Kalman Finkel</i> and <i>Gretchen White Oberman</i> argued the cause and filed briefs for appellant in No. 63. <i>Robert Stuart Friedman</i> argued the cause and filed a brief for appellant in No. 74.</p>
<p><i>William I. Siegel</i> argued the cause for appellee in No. 63. With him on the brief was <i>Aaron E. Koota. James J. Duggan</i> argued the cause for appellee in No. 74. With him on the briefs was <i>Leonard Rubenfeld.</i></p>
<p><i>Michael Juviler</i> argued the cause for the District Attorney of New York County, as <i>amicus curiae,</i> in <span class="star-pagination">*43</span> No. 63. With him on the brief filed in both cases were <i>Frank S. Hogan</i> and <i>H. Richard Uviller. Mr. Siegel</i> argued the cause for the District Attorney of Kings County, as <i>amicus curiae,</i> in No. 74.</p>
<p>Briefs of <i>amici curiae,</i> urging reversal in both cases, were filed by <i>Jack Greenberg, James M. Nabrit III, Michael Meltsner, Melvyn Zarr,</i> and <i>Anthony G. Amsterdam</i> for the NAACP Legal Defense and Educational Fund, Inc., and by <i>Bernard A. Berkman, Melvin L. Wulf,</i> and <i>Alan H. Levine</i> for the American Civil Liberties Union et al.</p>
<p><i>Louis J. Lefkowitz, pro se, Samuel A. Hirshowitz,</i> First Assistant Attorney General, and <i>Maria L. Marcus</i> and <i>Brenda Soloff,</i> Assistant Attorneys General, filed a brief for the Attorney General of New York, as <i>amicus curiae,</i> urging affirmance in both cases.</p>
<p>MR. CHIEF JUSTICE WARREN delivered the opinion of the Court.</p>
<p>These are companion cases to No. 67, <i>Terry</i> v. <i>Ohio, ante,</i> p. 1, decided today. They present related questions under the Fourth and Fourteenth Amendments, but the cases arise in the context of New York's "stop-and-frisk" law, N. Y. Code Crim. Proc. § 180-a. This statute provides:</p>
<blockquote>"1. A police officer may stop any person abroad in a public place whom he reasonably suspects is committing, has committed or is about to commit a felony or any of the offenses specified in section five hundred fifty-two of this chapter, and may demand of him his name, address and an explanation of his actions.</blockquote>
<blockquote>"2. When a police officer has stopped a person for questioning pursuant to this section and reasonably <span class="star-pagination">*44</span> suspects that he is in danger of life or limb, he may search such person for a dangerous weapon. If the police officer finds such a weapon or any other thing the possession of which may constitute a crime, he may take and keep it until the completion of the questioning, at which time he shall either return it, if lawfully possessed, or arrest such person."</blockquote>
<p>The appellants, Sibron and Peters, were both convicted of crimes in New York state courts on the basis of evidence seized from their persons by police officers. The Court of Appeals of New York held that the evidence was properly admitted, on the ground that the searches which uncovered it were authorized by the statute. <i>People</i> v. <i>Sibron,</i> 18 N. Y. 2d 603, <span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">219 N. E. 2d 196</a></span>, 272 N. Y. S. 2d 374 (1966) (memorandum); <i>People</i> v. <i>Peters,</i> 18 N. Y. 2d 238, <span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">219 N. E. 2d 595</a></span>, 273 N. Y. S. 2d 217 (1966). Sibron and Peters have appealed their convictions to this Court, claiming that § 180-a is unconstitutional on its face and as construed and applied, because the searches and seizures which it was held to have authorized violated their rights under the Fourth Amendment, made applicable to the States by the Fourteenth. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). We noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./386/954/">386 U. S. 954</a></span> (1967); <span class="citation multiple-matches"><a href="/c/U.%20S./386/980/">386 U. S. 980</a></span> (1967), and consolidated the two cases for argument with No. 67.</p>
<p>The facts in these cases may be stated briefly. Sibron, the appellant in No. 63, was convicted of the unlawful possession of heroin.<sup>[1]</sup> He moved before trial to suppress <span class="star-pagination">*45</span> the heroin seized from his person by the arresting officer, Brooklyn Patrolman Anthony Martin. After the trial court denied his motion, Sibron pleaded guilty to the charge, preserving his right to appeal the evidentiary ruling.<sup>[2]</sup> At the hearing on the motion to suppress, Officer Martin testified that while he was patrolling his beat in uniform on March 9, 1965, he observed Sibron "continually from the hours of 4:00 P. M. to 12:00, midnight. . . in the vicinity of 742 Broadway." He stated that during this period of time he saw Sibron in conversation with six or eight persons whom he (Patrolman Martin) knew from past experience to be narcotics addicts. The officer testified that he did not overhear any of these conversations, and that he did not see anything pass between Sibron and any of the others. Late in the evening Sibron entered a restaurant. Patrolman Martin saw Sibron speak with three more known addicts inside the restaurant. Once again, nothing was overheard and nothing was seen to pass between Sibron and the addicts. Sibron sat down and ordered pie and coffee, and, as he was eating, Patrolman Martin approached him and told him to come outside. Once outside, the officer said to Sibron, "You know what I am after." According to the officer, Sibron "mumbled something and reached into his pocket." Simultaneously, Patrolman Martin thrust his hand into the same pocket, discovering several glassine envelopes, which, it turned out, contained heroin.</p>
<p>The State has had some difficulty in settling upon a <span class="star-pagination">*46</span> theory for the admissibility of these envelopes of heroin. In his sworn complaint Patrolman Martin stated:</p>
<blockquote>"As the officer approached the defendant, the latter being in the direction of the officer and seeing him, he did put his hand in his left jacket pocket and pulled out a tinfoil envelope and did attempt to throw same to the ground. The officer never losing sight of the said envelope seized it from the def[endan]t's left hand, examined it and found it to contain ten glascine [<i>sic</i>] envelopes with a white substance alleged to be Heroin."</blockquote>
<p>This version of the encounter, however, bears very little resemblance to Patrolman Martin's testimony at the hearing on the motion to suppress. In fact, he discarded the abandonment theory at the hearing.<sup>[3]</sup> Nor did the officer ever seriously suggest that he was in fear of bodily harm and that he searched Sibron in self-protection to find weapons.<sup>[4]</sup></p>
<p><span class="star-pagination">*47</span> The prosecutor's theory at the hearing was that Patrolman Martin had probable cause to believe that Sibron was in possession of narcotics because he had seen him conversing with a number of known addicts over an eight-hour period. In the absence of any knowledge on Patrolman Martin's part concerning the nature of the intercourse between Sibron and the addicts, however, the trial court was inclined to grant the motion to suppress. As the judge stated, "All he knows about the unknown men: They are narcotics addicts. They might have been talking about the World Series. They might have been talking about prize fights." The prosecutor, however, reminded the judge that Sibron had admitted on the stand, in Patrolman Martin's absence, that he had been talking to the addicts about narcotics. Thereupon, the trial judge changed his mind and ruled that the officer had probable cause for an arrest.</p>
<p>Section 180-a, the "stop-and-frisk" statute, was not mentioned at any point in the trial court. The Appellate Term of the Supreme Court affirmed the conviction without opinion. In the Court of Appeals of New York, Sibron's case was consolidated with the <i><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span></i> case, No. 74. The Court of Appeals held that the search in <i><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span></i> was justified under the statute, but it wrote no opinion in Sibron's case. The dissents of Judges Fuld and Van Voorhis, however, indicate that the court rested its holding on § 180-a. At any rate, in its Brief in Opposition <span class="star-pagination">*48</span> to the Jurisdictional Statement in this Court, the State sought to justify the search on the basis of the statute. After we noted probable jurisdiction, the District Attorney for Kings County confessed error.</p>
<p>Peters, the appellant in No. 74, was convicted of possessing burglary tools under circumstances evincing an intent to employ them in the commission of a crime.<sup>[5]</sup> The tools were seized from his person at the time of his arrest, and like Sibron he made a pretrial motion to suppress them. When the trial court denied the motion, he too pleaded guilty, preserving his right to appeal. Officer Samuel Lasky of the New York City Police Department testified at the hearing on the motion that he was at home in his apartment in Mount Vernon, New York, at about 1 p. m. on July 10, 1964. He had just finished taking a shower and was drying himself when he heard a noise at his door. His attempt to investigate was interrupted by a telephone call, but when he returned and looked through the peephole into the hall, Officer Lasky saw "two men tiptoeing out of the alcove toward the stairway." He immediately called the police, put on some civilian clothes and armed himself with his service revolver. Returning to the peephole, he saw "a tall man tiptoeing away from the alcove and followed by this shorter man, Mr. Peters, toward the stairway." Officer Lasky testified that he had lived in the 120-unit building for 12 years and that he did not recognize either of the men as tenants. Believing that he had happened upon the two men in the course of an attempted burglary,<sup>[6]</sup><span class="star-pagination">*49</span> Officer Lasky opened his door, entered the hallway and slammed the door loudly behind him. This precipitated a flight down the stairs on the part of the two men,<sup>[7]</sup> and Officer Lasky gave chase. His apartment was located on the sixth floor, and he apprehended Peters between the fourth and fifth floors. Grabbing Peters by the collar, he continued down another flight in unsuccessful pursuit of the other man. Peters explained his presence in the building to Officer Lasky by saying that he was visiting a girl friend. However, he declined to reveal the girl friend's name, on the ground that she was a married woman. Officer Lasky patted Peters down for weapons, and discovered a hard object in his pocket. He stated at the hearing that the object did not feel like a gun, but that it might have been a knife. He removed the object from Peters' pocket. It was an opaque plastic envelope, containing burglar's tools.</p>
<p>The trial court explicitly refused to credit Peters' testimony that he was merely in the building to visit his girl friend. It found that Officer Lasky had the requisite "reasonable suspicion" of Peters under § 180-a to stop him and question him. It also found that Peters' response was "clearly unsatisfactory," and that "under <span class="star-pagination">*50</span> the circumstances Lasky's action in frisking Peters for a dangerous weapon was reasonable, even though Lasky was himself armed." It held that the hallway of the apartment building was a "public place" within the meaning of the statute. The Appellate Division of the Supreme Court affirmed without opinion. The Court of Appeals also affirmed, essentially adopting the reasoning of the trial judge, with Judges Fuld and Van Voorhis dissenting separately.</p>
<p></p>
<h2>I.</h2>
<p>At the outset we must deal with the question whether we have jurisdiction in No. 63. It is asserted that because Sibron has completed service of the six-month sentence imposed upon him as a result of his conviction, the case has become moot under <i>St. Pierre</i> v. <i>United States,</i> <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">319 U. S. 41</a></span> (1943).<sup>[8]</sup> We have concluded that the case is not moot.</p>
<p><span class="star-pagination">*51</span> In the first place, it is clear that the broad dictum with which the Court commenced its discussion in <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span></i>that "the case is moot because, after petitioner's service of his sentence and its expiration, there was no longer a subject matter on which the judgment of this Court could operate" (<span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#42" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 42</a></span>)fails to take account of significant qualifications recognized in <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span></i> and developed in later cases. Only a few days ago we held unanimously that the writ of habeas corpus was available to test the constitutionality of a state conviction where the petitioner had been in custody when he applied for the writ, but had been released before this Court could adjudicate his claims. <i>Carafas</i> v. <i>LaVallee,</i> <span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968). On numerous occasions in the past this Court has proceeded to adjudicate the merits of criminal cases in which the sentence had been fully served or the probationary period during which a suspended sentence could be reimposed had terminated. <i>Ginsberg</i> v. <i>New York,</i> <span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629</a></span> (1968); <i>Pollard</i> v. <i>United States,</i> <span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/" aria-description="Citation for case: Pollard v. United States">352 U. S. 354</a></span> (1957); <i>United States</i> v. <i>Morgan,</i> <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">346 U. S. 502</a></span> (1954); <i>Fiswick</i> v. <i>United States,</i> <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211</a></span> (1946). Thus mere release of the prisoner does not mechanically foreclose consideration of the merits by this Court.</p>
<p><i>St. Pierre</i> itself recognized two possible exceptions to its "doctrine" of mootness, and both of them appear to us to be applicable here. The Court stated that "[i]t does not appear that petitioner could not have brought his case to this Court for review before the expiration of his sentence," noting also that because the petitioner's conviction was for contempt and because his controversy with the Government was a continuing one, there was a good chance that there would be "ample opportunity to review" the important question presented on the merits in a future proceeding. <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. This <span class="star-pagination">*52</span> was a plain recognition of the vital importance of keeping open avenues of judicial review of deprivations of constitutional right.<sup>[9]</sup> There was no way for Sibron to bring his case here before his six-month sentence expired. By statute he was precluded from obtaining bail pending appeal,<sup>[10]</sup> and by virtue of the inevitable delays of the New York court system, he was released less than a month after his newly appointed appellate counsel had been supplied with a copy of the transcript and roughly two months before it was physically possible to present his case to the first tier in the state appellate court system.<sup>[11]</sup> This was true despite the fact that he took all steps to perfect his appeal in a prompt, diligent, and timely manner.</p>
<p>Many deep and abiding constitutional problems are encountered primarily at a level of "low visibility" in the criminal processin the context of prosecutions for "minor" offenses which carry only short sentences.<sup>[12]</sup> We do not believe that the Constitution contemplates that <span class="star-pagination">*53</span> people deprived of constitutional rights at this level should be left utterly remediless and defenseless against repetitions of unconstitutional conduct. A State may not cut off federal review of whole classes of such cases by the simple expedient of a blanket denial of bail pending appeal. As <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span></i> clearly recognized, a State may not effectively deny a convict access to its appellate courts until he has been released and then argue that his case has been mooted by his failure to do what it alone prevented him from doing.<sup>[13]</sup></p>
<p>The second exception recognized in <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span></i> permits adjudication of the merits of a criminal case where "under either state or federal law further penalties or disabilities can be imposed . . . as a result of the judgment which <span class="star-pagination">*54</span> has . . . been satisfied." <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. Subsequent cases have expanded this exception to the point where it may realistically be said that inroads have been made upon the principle itself. <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span></i> implied that the burden was upon the convict to show the existence of collateral legal consequences. Three years later in <i>Fiswick</i> v. <i>United States,</i> <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211</a></span> (1946), however, the Court held that a criminal case had not become moot upon release of the prisoner, noting that the convict, an alien, might be subject to deportation for having committed a crime of "moral turpitude"even though it had never been held (and the Court refused to hold) that the crime of which he was convicted fell into this category. The Court also pointed to the fact that if the petitioner should in the future decide he wanted to become an American citizen, he might have difficulty proving that he was of "good moral character." <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#222" aria-description="Citation for case: Fiswick v. United States"><i>Id.,</i> at 222</a></span>.<sup>[14]</sup></p>
<p>The next case which dealt with the problem of collateral consequences was <i>United States</i> v. <i>Morgan,</i> <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">346 U. S. 502</a></span> (1954). There the convict had probably been subjected to a higher sentence as a recidivist by a state court on account of the old federal conviction which he sought to attack. But as the dissent pointed out, there was no indication that the recidivist increment would be removed from his state sentence upon invalidation of the federal conviction, <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#516" aria-description="Citation for case: United States v. Morgan"><i>id.,</i> at 516, n. 4</a></span>, and the Court chose to rest its holding that the case was not moot upon <span class="star-pagination">*55</span> a broader view of the matter. Without canvassing the possible disabilities which might be imposed upon Morgan or alluding specifically to the recidivist sentence, the Court stated:</p>
<blockquote>"Although the term has been served, the results of the conviction may persist. Subsequent convictions may carry heavier penalties, civil rights may be affected. As the power to remedy an invalid sentence exists, we think, respondent is entitled to an opportunity to attempt to show that this conviction was invalid." <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#512" aria-description="Citation for case: United States v. Morgan"><i>Id.,</i> at 512-513</a></span>.</blockquote>
<p>Three years later, in <i>Pollard</i> v. <i>United States,</i> <span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/" aria-description="Citation for case: Pollard v. United States">352 U. S. 354</a></span> (1957), the Court abandoned all inquiry into the actual existence of specific collateral consequences and in effect presumed that they existed. With nothing more than citations to <i><span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">Morgan</a></span></i> and <i><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">Fiswick</a></span>,</i> and a statement that "convictions may entail collateral legal disadvantages in the future," <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#358" aria-description="Citation for case: Fiswick v. United States"><i>id.,</i> at 358</a></span>, the Court concluded that "[t]he possibility of consequences collateral to the imposition of sentence is sufficiently substantial to justify our dealing with the merits." <i><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">Ibid.</a></span></i> The Court thus acknowledged the obvious fact of life that most criminal convictions do in fact entail adverse collateral legal consequences.<sup>[15]</sup> The mere "possibility" that this will be the case is enough to preserve a criminal case from ending "ignominiously in the limbo of mootness." <i>Parker</i> v. <i>Ellis,</i> <span class="citation" data-id="9421986"><a href="/opinion/106050/parker-v-ellis/#577" aria-description="Citation for case: Parker v. Ellis">362 U. S. 574, 577</a></span> (1960) (dissenting opinion).</p>
<p>This case certainly meets that test for survival. Without pausing to canvass the possibilities in detail, we note that New York expressly provides by statute that Sibron's conviction may be used to impeach his character should he choose to put it in issue at any future <span class="star-pagination">*56</span> criminal trial, N. Y. Code Crim. Proc. § 393-c, and that it must be submitted to a trial judge for his consideration in sentencing should Sibron again be convicted of a crime, N. Y. Code Crim. Proc. § 482. There are doubtless other collateral consequences. Moreover, we see no relevance in the fact that Sibron is a multiple offender. Morgan was a multiple offender, see <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#503" aria-description="Citation for case: United States v. Morgan">346 U. S. at 503-504</a></span>, and so was Pollard, see <span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/#355" aria-description="Citation for case: Pollard v. United States">352 U. S., at 355-357</a></span>. A judge or jury faced with a question of character, like a sentencing judge, may be inclined to forgive or at least discount a limited number of minor transgressions, particularly if they occurred at some time in the relatively distant past.<sup>[16]</sup> It is impossible for this Court to say at what point the number of convictions on a man's record renders his reputation irredeemable.<sup>[17]</sup> And even if we believed that an individual had reached that point, it would be impossible for us to say that he had no interest in beginning the process of redemption with the particular case sought to be adjudicated. We cannot foretell what opportunities might present themselves in the future for the removal of other convictions from an individual's record. The question of the validity of a criminal conviction can arise in many contexts, compare <i>Burgett</i> v. <i>Texas,</i> <span class="citation" data-id="9423521"><a href="/opinion/107540/burgett-v-texas/" aria-description="Citation for case: Burgett v. Texas">389 U. S. 109</a></span> (1967), and the sooner the issue is fully litigated the better for all concerned. It is always preferable to litigate a matter <span class="star-pagination">*57</span> when it is directly and principally in dispute, rather than in a proceeding where it is collateral to the central controversy. Moreover, litigation is better conducted when the dispute is fresh and additional facts may, if necessary, be taken without a substantial risk that witnesses will die or memories fade. And it is far better to eliminate the source of a potential legal disability than to require the citizen to suffer the possibly unjustified consequences of the disability itself for an indefinite period of time before he can secure adjudication of the State's right to impose it on the basis of some past action. Cf. <i>Peyton</i> v. <i>Rowe,</i> <span class="citation" data-id="107679"><a href="/opinion/107679/peyton-v-rowe/#64" aria-description="Citation for case: Peyton v. Rowe">391 U. S. 54, 64</a></span> (1968).<sup>[18]</sup></p>
<p>None of the concededly imperative policies behind the constitutional rule against entertaining moot controversies would be served by a dismissal in this case. There is nothing abstract, feigned, or hypothetical about Sibron's appeal. Nor is there any suggestion that either Sibron or the State has been wanting in diligence or fervor in the litigation. We have before us a fully developed record of testimony about contested historical facts, which reflects the "impact of actuality"<sup>[19]</sup> to a far greater degree than many controversies accepted for adjudication as a matter of course under the Federal Declaratory Judgment Act, <span class="citation no-link">28 U. S. C. § 2201</span>.</p>
<p><i>St. Pierre</i> v. <i>United States, supra</i><i>,</i> must be read in light of later cases to mean that a criminal case is moot only if it is shown that there is no possibility that any collateral legal consequences will be imposed on the basis of the challenged conviction. That certainly is not <span class="star-pagination">*58</span> the case here. Sibron "has a substantial stake in the judgment of conviction which survives the satisfaction of the sentence imposed on him." <i>Fiswick</i> v. <i>United States, supra,</i> at 222. The case is not moot.</p>
<p></p>
<h2>II.</h2>
<p>We deal next with the confession of error by the District Attorney for Kings County in No. 63. Confessions of error are, of course, entitled to and given great weight, but they do not "relieve this Court of the performance of the judicial function." <i>Young</i> v. <i>United States,</i> <span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/#258" aria-description="Citation for case: Young v. United States">315 U. S. 257, 258</a></span> (1942). It is the uniform practice of this Court to conduct its own examination of the record in all cases where the Federal Government or a State confesses that a conviction has been erroneously obtained. For one thing, as we noted in <i><span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/" aria-description="Citation for case: Young v. United States">Young</a></span>,</i> "our judgments are precedents, and the proper administration of the criminal law cannot be left merely to the stipulation of parties." <span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/#259" aria-description="Citation for case: Young v. United States">315 U. S., at 259</a></span>. See also <i>Marino</i> v. <i>Ragen,</i> <span class="citation" data-id="9420073"><a href="/opinion/104487/marino-v-ragen/" aria-description="Citation for case: Marino v. Ragen">332 U. S. 561</a></span> (1947). This consideration is entitled to special weight where, as in this case, we deal with a judgment of a State's highest court interpreting a state statute which is challenged on constitutional grounds. The need for such authoritative declarations of state law in sensitive constitutional contexts has been the very reason for the development of the abstention doctrine by this Court. See, <i>e. g., </i><i>Railroad Comm'n</i> v. <i>Pullman Co.,</i> <span class="citation" data-id="103481"><a href="/opinion/103481/railroad-commn-of-tex-v-pullman-co/" aria-description="Citation for case: Railroad Comm&#x27;n of Tex. v. Pullman Co.">312 U. S. 496</a></span> (1941). Such a judgment is the final product of a sovereign judicial system, and is deserving of respectful treatment by this Court. Moreover, in this case the confession of error on behalf of the entire state executive and judicial branches is made, not by a state official, but by the elected legal officer of one political subdivision within the State. The District Attorney for Kings County seems to have come late to the opinion that this conviction violated Sibron's constitutional <span class="star-pagination">*59</span> rights. For us to accept his view blindly in the circumstances, when a majority of the Court of Appeals of New York has expressed the contrary view, would be a disservice to the State of New York and an abdication of our obligation to lower courts to decide cases upon proper constitutional grounds in a manner which permits them to conform their future behavior to the demands of the Constitution. We turn to the merits.</p>
<p></p>
<h2>III.</h2>
<p>The parties on both sides of these two cases have urged that the principal issue before us is the constitutionality of § 180-a "on its face." We decline, however, to be drawn into what we view as the abstract and unproductive exercise of laying the extraordinarily elastic categories of § 180-a next to the categories of the Fourth Amendment in an effort to determine whether the two are in some sense compatible. The constitutional validity of a warrantless search is pre-eminently the sort of question which can only be decided in the concrete factual context of the individual case. In this respect it is quite different from the question of the adequacy of the procedural safeguards written into a statute which purports to authorize the issuance of search warrants in certain circumstances. See <i>Berger</i> v. <i>New York,</i> <span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). No search required to be made under a warrant is valid if the procedure for the issuance of the warrant is inadequate to ensure the sort of neutral contemplation by a magistrate of the grounds for the search and its proposed scope, which lies at the heart of the Fourth Amendment. <i>E. g., </i><i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). This Court held last Term in <i>Berger</i> v. <i>New York, supra</i><i>,</i> that N. Y. Code Crim Proc. § 813-a, which established a procedure for the issuance of search warrants to permit electronic eavesdropping, failed to <span class="star-pagination">*60</span> embody the safeguards demanded by the Fourth and Fourteenth Amendments.</p>
<p>Section 180-a, unlike § 813-a, deals with the substantive validity of certain types of seizures and searches without warrants. It purports to authorize police officers to "stop" people, "demand" explanations of them and "search [them] for dangerous weapon[s]" in certain circumstances upon "reasonable suspicion" that they are engaged in criminal activity and that they represent a danger to the policeman. The operative categories of § 180-a are not the categories of the Fourth Amendment, and they are susceptible of a wide variety of interpretations.<sup>[20]</sup> New York is, of course, free to develop its own <span class="star-pagination">*61</span> law of search and seizure to meet the needs of local law enforcement, see <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34</a></span> (1963), and in the process it may call the standards it employs by any names it may choose. It may not, however, authorize police conduct which trenches upon Fourth Amendment rights, regardless of the labels which it attaches to such conduct. The question in this Court upon review of a state-approved search or seizure "is not whether the search [or seizure] was authorized by state law. The question is rather whether the search was reasonable under the Fourth Amendment. Just as a search authorized by state law may be an unreasonable one under that amendment, so may a search not expressly authorized by state law be justified as a constitutionally reasonable one." <i>Cooper</i> v. <i>California,</i> <span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967).</p>
<p>Accordingly, we make no pronouncement on the facial constitutionality of § 180-a. The constitutional point <span class="star-pagination">*62</span> with respect to a statute of this peculiar sort, as the Court of Appeals of New York recognized, is "not so much . . . the language employed as . . . the conduct it authorizes." <i>People</i> v. <i>Peters,</i> 18 N. Y. 2d 238, 245, <span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/#599" aria-description="Citation for case: People v. Peters">219 N. E. 2d 595, 599</a></span>, 273 N. Y. S. 2d 217, 222 (1966). We have held today in <i>Terry</i> v. <i>Ohio, ante,</i> p. 1, that police conduct of the sort with which § 180-a deals must be judged under the Reasonable Search and Seizure Clause of the Fourth Amendment. The inquiry under that clause may differ sharply from the inquiry set up by the categories of § 180-a. Our constitutional inquiry would not be furthered here by an attempt to pronounce judgment on the words of the statute. We must confine our review instead to the reasonableness of the searches and seizures which underlie these two convictions.</p>
<p></p>
<h2>IV.</h2>
<p>Turning to the facts of Sibron's case, it is clear that the heroin was inadmissible in evidence against him. The prosecution has quite properly abandoned the notion that there was probable cause to arrest Sibron for any crime at the time Patrolman Martin accosted him in the restaurant, took him outside and searched him. The officer was not acquainted with Sibron and had no information concerning him. He merely saw Sibron talking to a number of known narcotics addicts over a period of eight hours. It must be emphasized that Patrolman Martin was completely ignorant regarding the content of these conversations, and that he saw nothing pass between Sibron and the addicts. So far as he knew, they might indeed "have been talking about the World Series." The inference that persons who talk to narcotics addicts are engaged in the criminal traffic in narcotics is simply not the sort of reasonable inference required to support an intrusion by the police upon an individual's personal security. Nothing resembling probable cause existed <span class="star-pagination">*63</span> until after the search had turned up the envelopes of heroin. It is axiomatic that an incident search may not precede an arrest and serve as part of its justification. <i>E. g., </i><i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#16" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 16-17</a></span> (1948). Thus the search cannot be justified as incident to a lawful arrest.</p>
<p>If Patrolman Martin lacked probable cause for an arrest, however, his seizure and search of Sibron might still have been justified at the outset if he had reasonable grounds to believe that Sibron was armed and dangerous. <i>Terry</i> v. <i>Ohio, ante,</i> p. 1. We are not called upon to decide in this case whether there was a "seizure" of Sibron inside the restaurant antecedent to the physical seizure which accompanied the search. The record is unclear with respect to what transpired between Sibron and the officer inside the restaurant. It is totally barren of any indication whether Sibron accompanied Patrolman Martin outside in submission to a show of force or authority which left him no choice, or whether he went voluntarily in a spirit of apparent cooperation with the officer's investigation. In any event, this deficiency in the record is immaterial, since Patrolman Martin obtained no new information in the interval between his initiation of the encounter in the restaurant and his physical seizure and search of Sibron outside.</p>
<p>Although the Court of Appeals of New York wrote no opinion in this case, it seems to have viewed the search here as a self-protective search for weapons and to have affirmed on the basis of § 180-a, which authorizes such a search when the officer "reasonably suspects that he is in danger of life or limb." The Court of Appeals has, at any rate, justified searches during field interrogation on the ground that "[t]he answer to the question propounded by the policeman may be a <span class="star-pagination">*64</span> bullet; in any case the exposure to danger could be very great." <i>People</i> v. <i>Rivera,</i> 14 N. Y. 2d 441, 446, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#35" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32, 35</a></span>, 252 N. Y. S. 2d 458, 463 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965). But the application of this reasoning to the facts of this case proves too much. The police officer is not entitled to seize and search every person whom he sees on the street or of whom he makes inquiries. Before he places a hand on the person of a citizen in search of anything, he must have constitutionally adequate, reasonable grounds for doing so. In the case of the self-protective search for weapons, he must be able to point to particular facts from which he reasonably inferred that the individual was armed and dangerous. <i>Terry</i> v. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio, supra.</a></span></i> Patrolman Martin's testimony reveals no such facts. The suspect's mere act of talking with a number of known narcotics addicts over an eight-hour period no more gives rise to reasonable fear of life or limb on the part of the police officer than it justifies an arrest for committing a crime. Nor did Patrolman Martin urge that when Sibron put his hand in his pocket, he feared that he was going for a weapon and acted in self-defense. His opening statement to Sibron"You know what I am after"made it abundantly clear that he sought narcotics, and his testimony at the hearing left no doubt that he thought there were narcotics in Sibron's pocket.<sup>[21]</sup></p>
<p><span class="star-pagination">*65</span> Even assuming <i>arguendo</i> that there were adequate grounds to search Sibron for weapons, the nature and scope of the search conducted by Patrolman Martin were so clearly unrelated to that justification as to render the heroin inadmissible. The search for weapons approved in <i>Terry</i> consisted solely of a limited patting of the outer clothing of the suspect for concealed objects which might be used as instruments of assault. Only when he discovered such objects did the officer in <i>Terry</i> place his hands in the pockets of the men he searched. In this case, with no attempt at an initial limited exploration for arms, Patrolman Martin thrust his hand into Sibron's pocket and took from him envelopes of heroin. His testimony shows that he was looking for narcotics, and he found them. The search was not reasonably limited in scope to the accomplishment of the only goal which might conceivably have justified its inceptionthe protection of the officer by disarming a potentially dangerous man. Such a search violates the guarantee of the Fourth <span class="star-pagination">*66</span> Amendment, which protects the sanctity of the person against unreasonable intrusions on the part of all government agents.</p>
<p></p>
<h2>V.</h2>
<p>We think it is equally clear that the search in Peters' case was wholly reasonable under the Constitution. The Court of Appeals of New York held that the search was made legal by § 180-a, since Peters was "abroad in a public place," and since Officer Lasky was reasonably suspicious of his activities and, once he had stopped Peters, reasonably suspected that he was in danger of life or limb, even though he held Peters at gun point. This may be the justification for the search under state law. We think, however, that for purposes of the Fourth Amendment the search was properly incident to a lawful arrest. By the time Officer Lasky caught up with Peters on the stairway between the fourth and fifth floors of the apartment building, he had probable cause to arrest him for attempted burglary. The officer heard strange noises at his door which apparently led him to believe that someone sought to force entry. When he investigated these noises he saw two men, whom he had never seen before in his 12 years in the building, tiptoeing furtively about the hallway. They were still engaged in these maneuvers after he called the police and dressed hurriedly. And when Officer Lasky entered the hallway, the men fled down the stairs. It is difficult to conceive of stronger grounds for an arrest, short of actual eyewitness observation of criminal activity. As the trial court explicitly recognized,<sup>[22]</sup> deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of <i>mens rea,</i> and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors <span class="star-pagination">*67</span> to be considered in the decision to make an arrest. <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949); <i>Husty</i> v. <i>United States,</i> <span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931); see <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 103</a></span> (1959).</p>
<p>As we noted in Sibron's case, a search incident to a lawful arrest may not precede the arrest and serve as part of its justification. It is a question of fact precisely when, in each case, the arrest took place. <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261-262</a></span> (1960). And while there was some inconclusive discussion in the trial court concerning when Officer Lasky "arrested" Peters, it is clear that the arrest had, for purposes of constitutional justification, already taken place before the search commenced. When the policeman grabbed Peters by the collar, he abruptly "seized" him and curtailed his freedom of movement on the basis of probable cause to believe that he was engaged in criminal activity. See <i>Henry</i> v. <i>United States, supra,</i> at 103. At that point he had the authority to search Peters, and the incident search was obviously justified "by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime." <i>Preston</i> v. <i>United States,</i> <span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). Moreover, it was reasonably limited in scope by these purposes. Officer Lasky did not engage in an unrestrained and thorough-going examination of Peters and his personal effects. He seized him to cut short his flight, and he searched him primarily for weapons. While patting down his outer clothing, Officer Lasky discovered an object in his pocket which might have been used as a weapon. He seized it and discovered it to be a potential instrument of the crime of burglary.</p>
<p>We have concluded that Peters' conviction fully comports with the commands of the Fourth and Fourteenth Amendments, and must be affirmed. The conviction in <span class="star-pagination">*68</span> No. 63, however, must be reversed, on the ground that the heroin was unconstitutionally admitted in evidence against the appellant.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE DOUGLAS, concurring in No. 63.</p>
<p>Officer Martin testified that on the night in question he observed appellant Sibron continually from 4 p. m. to 12 midnight and that during that eight-hour period, Sibron conversed with different persons each personally known to Martin as narcotics addicts. When Sibron entered a restaurant, Martin followed him inside where he observed Sibron talking to three other persons also personally known to Martin as narcotics addicts. At that point he approached Sibron and asked him to come outside. When Sibron stepped out, Martin said, "You know what I am after." Sibron then reached inside his pocket, and at the same time Martin reached into the same pocket and discovered several glassine envelopes which were found to contain heroin. Sibron was subsequently convicted of unlawful possession of heroin.</p>
<p>Consorting with criminals may in a particular factual setting be a basis for believing that a criminal project is underway. Yet talking with addicts without more rises no higher than suspicion. That is all we have here; and if it is sufficient for a "seizure" and a "search," then there is no such thing as privacy for this vast group of "sick" people.</p>
<p>MR. JUSTICE DOUGLAS, concurring in No. 74.</p>
<p>Officer Lasky testified that he resided in a multiple-dwelling apartment house in Mount Vernon, New York. His apartment was on the sixth floor. At about 1 in the afternoon, he had just stepped out of the shower and was drying himself when he heard a noise at his door. Just then his phone rang and he answered the call. <span class="star-pagination">*69</span> After hanging up, he looked through the peephole of his door and saw two men, one of whom was appellant, tip-toeing out of an alcove toward the stairway. He phoned his headquarters to report this occurrence, and then put on some clothes and proceeded back to the door. This time he saw a tall man tiptoeing away from the alcove, followed by appellant, toward the stairway. Lasky came out of his apartment, slammed the door behind him, and then gave chase, gun in hand, as the two men began to run down the stairs. He apprehended appellant on the stairway between the fourth and fifth floors, and asked what he was doing in the building. Appellant replied that he was looking for a girl friend, but refused to give her name, saying that she was a married woman. Lasky then "frisked" appellant for a weapon, and discovered in his right pants pocket a plastic envelope. The envelope contained a tension bar, 6 picks and 2 Allen wrenches with the short leg filed down to a screwdriver edge. Appellant was subsequently convicted for possession of burglary tools.</p>
<p>I would hold that at the time Lasky seized appellant, he had probable cause to believe that appellant was on some kind of burglary or housebreaking mission.<sup>[*]</sup> In my view he had probable cause to seize appellant and accordingly to conduct a limited search of his person for weapons.</p>
<p>MR. JUSTICE WHITE, concurring.</p>
<p>I join Parts I-IV of the Court's opinion. With respect to appellant Peters, I join the affirmance of his conviction, not because there was probable cause to arrest, a question I do not reach, but because there was probable cause to stop Peters for questioning and thus to frisk him for dangerous weapons. See my concurring <span class="star-pagination">*70</span> opinion in <i>Terry</i> v. <i>Ohio, ante,</i> p. 34. While patting down Peters' clothing the officer "discovered an object in his pocket which might have been used as a weapon." <i>Ante,</i> at 67. That object turned out to be a package of burglar's tools. In my view those tools were properly admitted into evidence.</p>
<p>MR. JUSTICE FORTAS, concurring.</p>
<p>1. I would construe <i>St. Pierre</i> v. <i>United States,</i> <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">319 U. S. 41</a></span> (1943), in light of later cases, to mean that a criminal case is moot <i>if it appears</i> that no collateral legal consequences will be imposed on the basis of the challenged conviction. (Cf. majority opinion, <i>ante,</i> at 57-58.)</p>
<p>2. I join without qualification in the Court's judgment and opinion concerning the standards to be used in determining whether § 180-a as applied to particular situations is constitutional. But I would explicitly reserve the possibility that a statute purporting to authorize a warrantless search might be so extreme as to justify our concluding that it is unconstitutional "on its face," regardless of the facts of the particular case. To the extent that the Court's opinion may indicate the contrary, I disagree. (Cf. majority opinion, <i>ante,</i> at 59-62.)</p>
<p>3. In Sibron's case (No. 63), I would conclude that we find nothing in the record of this case or pertinent principles of law to cause us to disregard the confession of error by counsel for Kings County. I would not discourage confessions of error nor would I disregard them. (Cf. majority opinion, pt. II, <i>ante,</i> at 58-59.)</p>
<p>MR. JUSTICE HARLAN, concurring in the result.</p>
<p>I fully agree with the results the Court has reached in these cases. They are, I think, consonant with and dictated by the decision in <i>Terry</i> v. <i>Ohio, ante,</i> p. 1. For reasons I do not understand, however, the Court has declined to rest the judgments here upon the principles <span class="star-pagination">*71</span> of <i>Terry.</i> In doing so it has, in at least one particular, made serious inroads upon the protection afforded by the Fourth and Fourteenth Amendments.</p>
<p>The Court is of course entirely correct in concluding that we should not pass upon the constitutionality of the New York stop-and-frisk law "on its face." The statute is certainly not unconstitutional on its face: that is, it does not plainly purport to authorize unconstitutional activities by policemen. Nor is it "constitutional on its face" if that expression means that any action now or later thought to fall within the terms of the statute is, <i>ipso facto,</i> within constitutional limits as well. No statute, state or federal, receives any such <i>imprimatur</i> from this Court.</p>
<p>This does not mean, however, that the statute should be ignored here. The State of New York has made a deliberate effort to deal with the complex problem of on-the-street policework. Without giving <i>carte blanche</i> to any particular verbal formulation, we should, I think, where relevant, indicate the extent to which that effort has been constitutionally successful. The core of the New York statute is the permission to stop any person reasonably suspected of crime. Under the decision in <i>Terry</i> a right to stop may indeed be premised on reasonable suspicion and does not require probable cause, and hence the New York formulation is to that extent constitutional. This does not mean that suspicion need not be "reasonable" in the constitutional as well as the statutory sense. Nor does it mean that this Court has approved more than a momentary stop or has indicated what questioning may constitutionally occur during a stop, for the cases before us do not raise these questions.<sup>[1]</sup></p>
<p><span class="star-pagination">*72</span> Turning to the individual cases, I agree that the conviction in No. 63, <i><span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">Sibron</a></span>,</i> should be reversed, and would do so upon the premises of <i>Terry.</i> At the outset, I agree that sufficient collateral legal consequences of Sibron's conviction have been shown to prevent this case from being moot, and I agree that the case should not be reversed simply on the State's confession of error.</p>
<p>The considerable confusion that has surrounded the "search" or "frisk" of Sibron that led to the actual recovery of the heroin seems to me irrelevant for our purposes. Officer Martin repudiated his first statement, which might conceivably have indicated a theory of "abandonment," see <i>ante,</i> at 45-46. No matter which of the other theories is adopted, it is clear that there was at least a forcible frisk, comparable to that which occurred in <i>Terry,</i> which requires constitutional justification.</p>
<p>Since carrying heroin is a crime in New York, probable cause to believe Sibron was carrying heroin would also have been probable cause to arrest him. As the Court says, Officer Martin clearly had neither. Although Sibron had had conversations with several known addicts, he had done nothing, during the several hours he was under surveillance, that made it "probable" that he was either carrying heroin himself or engaging in transactions with these acquaintances.</p>
<p>Nor were there here reasonable grounds for a <i>Terry</i>-type "stop" short of an arrest. I would accept, as an adequate general formula, the New York requirement that the officer must "reasonably suspect" that the person he stops "is committing, has committed or is about to commit a felony." N. Y. Code Crim. Proc. § 180-a. "On its face," this requirement is, if anything, more stringent than the requirement stated by the Court in <i>Terry:</i> "where a police officer observes unusual conduct which leads him reasonably to conclude in light of his experience that criminal activity may be afoot . . . ." <span class="star-pagination">*73</span> <i>Ante,</i> at 30. The interpretation of the New York statute is of course a matter for the New York courts, but any particular stop must meet the <i>Terry</i> standard as well.</p>
<p>The forcible encounter between Officer Martin and Sibron did not meet the <i>Terry</i> reasonableness standard. In the first place, although association with known criminals may, I think, properly be a factor contributing to the suspiciousness of circumstances, it does not, entirely by itself, create suspicion adequate to support a stop. There must be something at least in the activities of the person being observed or in his surroundings that affirmatively suggests particular criminal activity, completed, current, or intended. That was the case in <i>Terry,</i> but it palpably was not the case here. For eight continuous hours, up to the point when he interrupted Sibron eating a piece of pie, Officer Martin apparently observed not a single suspicious action and heard not a single suspicious word on the part of Sibron himself or any person with whom he associated. If anything, that period of surveillance pointed away from suspicion.</p>
<p>Furthermore, in <i>Terry,</i> the police officer judged that his suspect was about to commit a violent crime and that he had to assert himself in order to prevent it. Here there was no reason for Officer Martin to think that an incipient crime, or flight, or the destruction of evidence would occur if he stayed his hand; indeed, there was no more reason for him to intrude upon Sibron at the moment when he did than there had been four hours earlier, and no reason to think the situation would have changed four hours later. While no hard-and-fast rule can be drawn, I would suggest that one important factor, missing here, that should be taken into account in determining whether there are reasonable grounds for a forcible intrusion is whether there is any need for immediate action.</p>
<p><span class="star-pagination">*74</span> For these reasons I would hold that Officer Martin lacked reasonable grounds to intrude forcibly upon Sibron. In consequence, the essential premise for the right to conduct a self-protective frisk was lacking. See my concurring opinion in <i>Terry, ante,</i> p. 31. I therefore find it unnecessary to reach two further troublesome questions. First, although I think that, as in <i>Terry,</i> the right to frisk is automatic when an officer lawfully stops a person suspected of a crime whose nature creates a substantial likelihood that he is armed, it is not clear that suspected possession of narcotics falls into this category. If the nature of the suspected offense creates no reasonable apprehension for the officer's safety, I would not permit him to frisk unless other circumstances did so. Second, I agree with the Court that even where a self-protective frisk is proper, its scope should be limited to what is adequate for its purposes. I see no need here to resolve the question whether this frisk exceeded those bounds.</p>
<p>Turning now to No. 74, <i><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span>,</i> I agree that the conviction should be upheld, but here I would differ strongly and fundamentally with the Court's approach. The Court holds that the burglar's tools were recovered from Peters in a search incident to a lawful arrest. I do not think that Officer Lasky had anything close to probable cause to arrest Peters before he recovered the burglar's tools. Indeed, if probable cause existed here, I find it difficult to see why a different rationale was necessary to support the stop and frisk in <i>Terry</i> and why States such as New York have had to devote so much thought to the constitutional problems of field interrogation. This case will be the latest in an exceedingly small number of cases in this Court indicating what suffices for probable cause. While, as the Court noted in <i>Terry,</i> the influence of this Court on police tactics "in <span class="star-pagination">*75</span> the field" is necessarily limited, the influence of a decision here on hundreds of courts and magistrates who have to decide whether there is probable cause for a real arrest or a full search will be large.</p>
<p>Officer Lasky testified that at 1 o'clock in the afternoon he heard a noise at the door to his apartment. He did not testify, nor did any state court conclude, that this "led him to believe that someone sought to force entry." <i>Ante,</i> at 66. He looked out into the public hallway and saw two men whom he did not recognize, surely not a strange occurrence in a large apartment building. One of them appeared to be tip-toeing. Lasky did not testify that the other man was tip-toeing or that either of them was behaving "furtively." <i><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Ibid.</a></span></i> Lasky left his apartment and ran to them, gun in hand. He did not testify that there was any "flight," <i>ante,</i> at 66,<sup>[2]</sup> though flight at the approach of a gun-carrying stranger (Lasky was apparently not in uniform) is hardly indicative of <i>mens rea.</i></p>
<p>Probable cause to arrest means evidence that would warrant a prudent and reasonable man (such as a magistrate, actual or hypothetical) in believing that a particular person has committed or is committing a crime.<sup>[3]</sup><span class="star-pagination">*76</span> Officer Lasky had no extrinsic reason to think that a crime had been or was being committed, so whether it would have been proper to issue a warrant depends entirely on his statements of his observations of the men. Apart from his conclusory statement that he thought the men were burglars, he offered very little specific evidence. I find it hard to believe that if Peters had made good his escape and there were no report of a burglary in the neighborhood, this Court would hold it proper for a prudent neutral magistrate to issue a warrant for his arrest.<sup>[4]</sup></p>
<p>In the course of upholding Peters' conviction, the Court makes two other points that may lead to future confusion. The first concerns the "moment of arrest." If there is an escalating encounter between a policeman and a citizen, beginning perhaps with a friendly conversation but ending in imprisonment, and if evidence is developing during that encounter, it may be important to identify the moment of arrest, <i>i. e.,</i> the moment when the policeman was not permitted to proceed further unless he by then had probable cause. This moment-of-arrest problem is not, on the Court's premises, in any way involved in this case: the Court holds that Officer Lasky had probable cause to arrest at the moment he caught Peters, and hence probable cause clearly preceded anything that might be thought an arrest. The Court implies, however, that although there is no problem about whether the arrest of Peters occurred <span class="star-pagination">*77</span> <i>late</i> enough, <i>i. e.,</i> after probable cause developed, there might be a problem about whether it occurred <i>early</i> enough, <i>i. e.,</i> before Peters was searched. This seems to me a false problem. Of course, the fruits of a search may not be used to justify an arrest to which it is incident, but this means only that probable cause to arrest must precede the search. If the prosecution shows probable cause to arrest prior to a search of a man's person, it has met its total burden. There is <i>no</i> case in which a defendant may validly say, "Although the officer had a right to arrest me at the moment when he seized me and searched my person, the search is invalid because he did not in fact arrest me until afterwards."</p>
<p>This fact is important because, as demonstrated by <i>Terry,</i> not every curtailment of freedom of movement is an "arrest" requiring antecedent probable cause. At the same time, an officer who does have probable cause may of course seize and search immediately. Hence while certain police actions will undoubtedly turn an encounter into an arrest requiring antecedent probable cause, the prosecution must be able to date the arrest as <i>early</i> as it chooses following the development of probable cause.</p>
<p>The second possible source of confusion is the Court's statement that "Officer Lasky did not engage in an unrestrained and thorough-going examination of Peters and his personal effects." <i>Ante,</i> at 67. Since the Court found probable cause to arrest Peters, and since an officer arresting on probable cause is entitled to make a very full incident search,<sup>[5]</sup> I assume that this is merely a factual observation. As a factual matter, I agree with it.</p>
<p>Although the articulable circumstances are somewhat less suspicious here than they were in <i>Terry,</i> I would affirm on the <i>Terry</i> ground that Officer Lasky had reasonable <span class="star-pagination">*78</span> cause to make a forced stop. Unlike probable cause to arrest, reasonable grounds to stop do not depend on any degree of likelihood that a crime <i>has</i> been committed. An officer may forcibly intrude upon an incipient crime even where he could not make an arrest for the simple reason that there is nothing to arrest anyone for. Hence although Officer Lasky had small reason to believe that a crime had been committed, his right to stop Peters can be justified if he had a reasonable suspicion that Peters was about to attempt burglary.</p>
<p>It was clear that the officer had to act quickly if he was going to act at all, and, as stated above, it seems to me that where immediate action is obviously required, a police officer is justified in acting on rather less objectively articulable evidence than when there is more time for consideration of alternative courses of action. Perhaps more important, the Court's opinion in <i>Terry</i> emphasized the special qualifications of an experienced police officer. While "probable cause" to arrest or search has always depended on the existence of hard evidence that would persuade a "reasonable man," in judging on-the-street encounters it seems to me proper to take into account a police officer's trained instinctive judgment operating on a multitude of small gestures and actions impossible to reconstruct. Thus the statement by an officer that "he looked like a burglar to me" adds little to an affidavit filed with a magistrate in an effort to obtain a warrant. When the question is whether it was reasonable to take limited but forcible steps in a situation requiring immediate action, however, such a statement looms larger. A court is of course entitled to disbelieve the officer (who is subject to cross-examination), but when it believes him and when there are some articulable supporting facts, it is entitled to find action taken under fire to be reasonable.</p>
<p><span class="star-pagination">*79</span> Given Officer Lasky's statement of the circumstances, and crediting his experienced judgment as he watched the two men, the state courts were entitled to conclude, as they did, that Lasky forcibly stopped Peters on "reasonable suspicion." The frisk made incident to that stop was a limited one, which turned up burglar's tools. Although the frisk is constitutionally permitted only in order to protect the officer, if it is lawful the State is of course entitled to the use of any other contraband that appears.</p>
<p>For the foregoing reasons I concur in the result in these cases.</p>
<p>MR. JUSTICE BLACK, concurring in No. 74 and dissenting in No. 63.</p>
<p>I concur in the affirmance of the judgment against Peters but dissent from the reversal of No. 63, <i>Sibron</i> v. <i>New York,</i> and would affirm that conviction. Sibron was convicted of violating New York's anti-narcotics law on the basis of evidence seized from him by the police. The Court reverses on the ground that the narcotics were seized as the result of an unreasonable search in violation of the Fourth Amendment. The Court has decided today in <i>Terry</i> v. <i>Ohio</i> and in No. 74, <i>Peters</i> v. <i>New York,</i> that a policeman does not violate the Fourth Amendment when he makes a limited search for weapons on the person of a man who the policeman has probable cause to believe has a dangerous weapon on him with which he might injure the policeman or others or both, unless he is searched and the weapon is taken away from him. And, of course, under established principles it is not a violation of the Fourth Amendment for a policeman to search a person who he has probable cause to believe is committing a felony at the time. For both these reasons I think the seizure of the narcotics from Sibron was not unreasonable <span class="star-pagination">*80</span> under the Fourth Amendment. Because of a different emphasis on the facts, I find it necessary to restate them.</p>
<p>About 4 p. m. Patrolman Martin saw appellant Sibron in the vicinity of 742 Broadway. From then until 12 o'clock midnight Sibron remained there. During that time the policeman saw Sibron talking with six or eight persons whom the policeman knew from past experience to be narcotics addicts. Later, at about 12 o'clock, Sibron went into a restaurant and there the patrolman saw Sibron speak with three more known addicts. While Sibron was eating in the restaurant the policeman went to him and asked him to come out. Sibron came out. There the officer said to Sibron, "You know what I am after." Sibron mumbled something and reached into his left coat pocket. The officer also moved his hand to the pocket and seized what was in it, which turned out to be heroin. The patrolman testified at the hearing to suppress use of the heroin as evidence that he "thought he [Sibron] might have been" reaching for a gun.</p>
<p>Counsel for New York for some reason that I have not been able to understand, has attempted to confess errorthat is, that for some reason the search or seizure here violated the Fourth Amendment. I agree with the Court that we need not and should not accept this confession of error. But, unlike the Court, I think, for two reasons, that the seizure did not violate the Fourth Amendment and that the heroin was properly admitted in evidence.</p>
<p>First. I think there was probable cause for the policeman to believe that when Sibron reached his hand to his coat pocket, Sibron had a dangerous weapon which he might use if it were not taken away from him. This, according to the Court's own opinion, seems to have been the ground on which the Court of Appeals of New York justified the search, since it "affirmed on the <span class="star-pagination">*81</span> basis of § 180-a, which authorizes such a search when the officer `reasonably suspects that he is in danger of life or limb.' " <i>Ante,</i> at 63. And it seems to me to be a reasonable inference that when Sibron, who had been approaching and talking to addicts for eight hours, reached his hand quickly to his left coat pocket, he might well be reaching for a gun. And as the Court has emphasized today in its opinions in the other stop-and-frisk cases, a policeman under such circumstances has to act in a split second; delay may mean death for him. No one can know when an addict may be moved to shoot or stab, and particularly when he moves his hand hurriedly to a pocket where weapons are known to be habitually carried, it behooves an officer who wants to live to act at once as this officer did. It is true that the officer might also have thought Sibron was about to get heroin instead of a weapon. But the law enforcement officers all over the Nation have gained little protection from the courts through opinions here if they are now left helpless to act in self defense when a man associating intimately and continuously with addicts, upon meeting an officer, shifts his hand immediately to a pocket where weapons are constantly carried.</p>
<p>In appraising the facts as I have I realize that the Court has chosen to draw inferences different from mine and those drawn by the courts below. The Court for illustration draws inferences that the officer's testimony at the hearing continued upon the "plain premise that he had been looking for narcotics all the time." <i>Ante,</i> at 47, n. 4. But this Court is hardly, at this distance from the place and atmosphere of the trial, in a position to overturn the trial and appellate courts on its own independent finding of an unspoken "premise" of the officer's inner thoughts.</p>
<p>In acting upon its own findings and rejecting those of the lower state courts, this Court, sitting in the marble halls of the Supreme Court Building in Washington, <span class="star-pagination">*82</span> D. C., should be most cautious. Due to our holding in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, we are due to get for review literally thousands of cases raising questions like those before us here. If we are setting ourselves meticulously to review all such findings our task will be endless and many will rue the day when <i>Mapp</i> was decided. It is not only wise but imperative that where findings of the facts of reasonableness and probable cause are involved in such state cases, we should not overturn state court findings unless in the most extravagant and egregious errors. It seems fantastic to me even to suggest that this is such a case. I would leave these state court holdings alone.</p>
<p>Second, I think also that there was sufficient evidence here on which to base findings that after recovery of the heroin, in particular, an officer could reasonably believe there was probable cause to charge Sibron with violating New York's narcotics laws. As I have previously argued, there was, I think, ample evidence to give the officer probable cause to believe Sibron had a dangerous weapon and that he might use it. Under such circumstances the officer had a right to search him in the very limited fashion he did here. Since, therefore, this was a reasonable and justified search, the use of the heroin discovered by it was admissible in evidence.</p>
<p>I would affirm.</p>
<h2>NOTES</h2>
<p>[*]  Together with No. 74, <i>Peters</i> v. <i>New York,</i> argued on December 12, 1967, also on appeal from the same court.</p>
<p>[1]  N. Y. Pub. Health Law § 3305 makes the unauthorized possession of any narcotic drug unlawful, and §§ 1751 and 1751-a of the N. Y. Penal Law of 1909, then in effect, made the grade of the offense depend upon the amount of the drugs found in the possession of the defendant. The complaint in this case originally charged a felony, but the trial court granted the prosecutor's motion to reduce the charge on the ground that "the Laboratory report will indicate a misdemeanor charge." Sibron was convicted of a misdemeanor and sentenced to six months in jail.</p>
<p>[2]  N. Y. Code Crim. Proc. § 813-c provides that an order denying a motion to suppress evidence in a criminal case "may be reviewed on appeal from a judgment of conviction notwithstanding the fact that such judgment of conviction is predicated upon a plea of guilty."</p>
<p>[3]  Patrolman Martin stated several times that he put his hand into Sibron's pocket and seized the heroin before Sibron had any opportunity to remove his own hand from the pocket. The trial court questioned him on this point:
</p>
<p>"Q. Would you say at that time that he reached into his pocket and handed the packets to you? Is that what he did or did he drop the packets?</p>
<p>"A. He did not drop them. <i>I do not know what his intentions were.</i> He pushed his hand into his pocket.</p>
<p>"MR. JOSEPH [Prosecutor]: You intercepted it; didn't you, Officer?</p>
<p>"THE WITNESS: Yes." (Emphasis added.)</p>
<p>It is of course highly unlikely that Sibron, facing the officer at such close quarters, would have tried to remove the heroin from his pocket and throw it to the ground in the hope that he could escape responsibility for it.</p>
<p>[4]  The possibility that Sibron, who never, so far as appears from the record, offered any resistance, might have posed a danger to Patrolman Martin's safety was never even discussed as a potential justification for the search. The only mention of weapons by the officer in his entire testimony came in response to a leading question by Sibron's counsel, when Martin stated that he "thought he [Sibron] might have been" reaching for a gun. Even so, Patrolman Martin did not accept this suggestion by the opposition regarding the reason for his action; the discussion continued upon the plain premise that he had been looking for narcotics all the time.</p>
<p>[5]  N. Y. Pen. Law of 1909, § 408, made the possession of such tools under such circumstances a misdemeanor for first offenders and a felony for all those who have "been previously convicted of any crime." Peters was convicted of a felony under this section.</p>
<p>[6]  Officer Lasky testified that when he called the police immediately before leaving his apartment, he "told the Sergeant at the desk that two burglars were on my floor."</p>
<p>[7]  Officer Lasky testified that when he emerged from his apartment, "I slammed the door, I had my gun and I ran down the stairs after them." A sworn affidavit of the Assistant District Attorney, which was before the trial court when it ruled on the motion to suppress, stated that when apprehended Peters was "fleeing down the steps of the building." The trial court explicitly took note of the flight of Peters and his companion as a factor contributing to Officer Lasky's "reasonable suspicion" of them:
</p>
<p>"We think the testimony at the hearing does not require further laboring of this aspect of the matter, unless one is to believe that it is legitimately normal for a man to tip-toe about in the public hall of an apartment house while on a visit to his unidentified girl-friend, and, when observed by another tenant, to rapidly descend by stairway in the presence of elevators."</p>
<p>[8]  The first suggestion of mootness in this case came upon oral argument, when it was revealed for the first time that appellant had been released. This fact did not appear in the record, despite the fact that the release occurred well over two years before the case was argued here. Nor was mootness hinted at by the State in its Brief in Opposition to the Jurisdictional Statement in this Court where it took the position that the decision below was so clearly right that it did not merit further reviewor in its brief on the meritsin which it conceded that the decision below clearly violated Sibron's constitutional rights and urged that it was an aberrant interpretation which should not impair the constitutionality of the New York statute. Following the suggestion of mootness on oral argument, moreover, the State filed a brief in which it amplified its views as to why the case should be held moot, but added the extraordinary suggestion that this Court should ignore the problem and pronounce upon the constitutionality of a statute in a case which has become moot. Normally in these circumstances we would consider ourselves fully justified in foreclosing a party upon an issue; however, since the question goes to the very existence of a controversy for us to adjudicate, we have undertaken to review it.</p>
<p>[9]  Cf. <i>Fay</i> v. <i>Noia,</i> <span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#424" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 424</a></span> (1963):
</p>
<p>"[C]onventional notions of finality in criminal litigation cannot be permitted to defeat the manifest federal policy that federal constitutional rights of personal liberty shall not be denied without the fullest opportunity for plenary federal judicial review."</p>
<p>[10]  See N. Y. Code Crim. Proc. § 555 subd. 2.</p>
<p>[11]  Sibron was arrested on March 9, 1965, and was unable to make bail before trial because of his indigency. He thus remained in jail from that time until the expiration of his sentence (with good time credit) on July 10, 1965. He was convicted on April 23. His application for leave to proceed <i>in forma pauperis</i> was not granted until May 14, and his assigned appellate counsel was not provided with a transcript until June 11. The Appellate Term of the Supreme Court recessed on June 7 until September. Thus Sibron was released well before there had been any opportunity even to argue his case in the intermediate state appellate court. A decision by the Court of Appeals of New York was not had until July 10, 1966, the anniversary of Sibron's release.</p>
<p>[12]  Cf., <i>e. g., </i><i>Thompson</i> v. <i>City of Louisville,</i> <span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">362 U. S. 199</a></span> (1960).</p>
<p>[13]  In <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span></i> the Court noted that the petitioner could have taken steps to preserve his case, but that "he did not apply to this Court for a stay or a supersedeas." <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. Here however, it is abundantly clear that there is no procedure of which Sibron could have availed himself to prevent the expiration of his sentence long before this Court could hear his case. A supersedeas from this Court is a purely ancillary writ, and may issue only in connection with an appeal actually taken. <i>Ex parte Ralston,</i> <span class="citation" data-id="91800"><a href="/opinion/91800/ex-parte-ralston/" aria-description="Citation for case: Ex Parte Ralston">119 U. S. 613</a></span> (1887); Sup. Ct. Rule 18; see R. Robertson &amp; F. Kirkham, Jurisdiction of the Supreme Court of the United States § 435, at 883 (R. Wolfson &amp; P. Kurland ed., 1951). At the time Sibron completed service of his sentence, the only judgment outstanding was the conviction itself, rendered by the Criminal Court of the City of New York, County of Kings. This Court had no jurisdiction to hear an appeal from that judgment, since it was not rendered by the "highest court of a State in which a decision could be had," <span class="citation no-link">28 U. S. C. § 1257</span>, and there could be no warrant for interference with the orderly appellate processes of the state courts. Thus no supersedeas could have issued. Nor could this Court have ordered Sibron admitted to bail before the expiration of his sentence, since the offense was not bailable, <span class="citation no-link">18 U. S. C. § 3144</span>; see n. 10, <i>supra.</i> Thus this case is distinguishable from <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span></i> in that Sibron "could not have brought his case to this Court for review before the expiration of his sentence." <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>.</p>
<p>[14]  Compare <i>Ginsberg</i> v. <i>New York,</i> <span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/#633" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629, 633, n. 2</a></span> (1968), where this Court held that the mere possibility that the Commissioner of Buildings of the Town of Hempstead, New York, might "in his discretion" attempt in the future to revoke a license to run a luncheonette because of a single conviction for selling relatively inoffensive "girlie" magazines to a 16-year-old boy was sufficient to preserve a criminal case from mootness.</p>
<p>[15]  See generally Note, <span class="citation no-link">53 Va. L. Rev. 403</span> (1967).</p>
<p>[16]  We do not know from the record how many convictions Sibron had, for what crimes, or when they were rendered. At the hearing he admitted to a 1955 conviction for burglary and a 1957 misdemeanor conviction for possession of narcotics. He also admitted that he had other convictions, but none were specifically alluded to.</p>
<p>[17]  We note that there is a clear distinction between a general impairment of credibility, to which the Court referred in <i><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span>,</i> see <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>, and New York's specific statutory authorization for use of the conviction to impeach the "character" of a defendant in a criminal proceeding. The latter is a clear legal disability deliberately and specifically imposed by the legislature.</p>
<p>[18]  This factor has clearly been considered relevant by the Court in the past in determining the issue of mootness. See <i>Fiswick</i> v. <i>United States,</i> <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#221" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211, 221-222</a></span> (1946).</p>
<p>[19]  Frankfurter, A Note on Advisory Opinions, <span class="citation no-link">37 Harv. L. Rev. 1002</span>, 1006 (1924). See also <i>Parker</i> v. <i>Ellis,</i> <span class="citation" data-id="9421986"><a href="/opinion/106050/parker-v-ellis/#592" aria-description="Citation for case: Parker v. Ellis">362 U. S. 574, 592-593</a></span> (1960) (dissenting opinion).</p>
<p>[20]  It is not apparent, for example, whether the power to "stop" granted by the statute entails a power to "detain" for investigation or interrogation upon less than probable cause, or if so what sort of durational limitations upon such detention are contemplated. And while the statute's apparent grant of a power of compulsion indicates that many "stops" will constitute "seizures," it is not clear that all conduct analyzed under the rubric of the statute will either rise to the level of a "seizure" or be based upon less than probable cause. In No. 74, the <i><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span></i> case, for example, the New York courts justified the seizure of appellant under § 180-a, but we have concluded that there was in fact probable cause for an arrest when Officer Lasky seized Peters on the stairway. See <i>infra,</i> at 66. In any event, a pronouncement by this Court upon the abstract validity of § 180-a's "stop" category would be most inappropriate in these cases, since we have concluded that neither of them presents the question of the validity of a seizure of the person for purposes of interrogation upon less than probable cause.
</p>
<p>The statute's other categories are equally elastic, and it was passed too recently for the State's highest court to have ruled upon many of the questions involving potential intersections with federal constitutional guarantees. We cannot tell, for example, whether the officer's power to "demand" of a person an "explanation of his actions" contemplates either an obligation on the part of the citizen to answer or some additional power on the part of the officer in the event of a refusal to answer, or even whether the interrogation following the "stop" is "custodial." Compare <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). There are, moreover, substantial indications that the statutory category of a "search for a dangerous weapon" may encompass conduct considerably broader in scope than that which we approved in <i>Terry</i> v. <i>Ohio, ante,</i> p. 1. See <i>infra,</i> at 65-66. See also <i>People</i> v. <i>Taggart,</i> 20 N. Y. 2d 335, <span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/" aria-description="Citation for case: People v. Taggart">229 N. E. 2d 581</a></span>, 283 N. Y. S. 2d 1 (1967). At least some of the activity apparently permitted under the rubric of searching for dangerous weapons may thus be permissible under the Constitution only if the "reasonable suspicion" of criminal activity rises to the level of probable cause. Finally, it is impossible to tell whether the standard of "reasonable suspicion" connotes the same sort of specificity, reliability, and objectivity which is the touchstone of permissible governmental action under the Fourth Amendment. Compare <i>Terry</i> v. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio, supra,</a></span></i> with <i>People</i> v. <i><span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/" aria-description="Citation for case: People v. Taggart">Taggart, supra</a></span></i><i>.</i> In this connection we note that the searches and seizures in both <i><span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">Sibron</a></span></i> and <i><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span></i> were upheld by the Court of Appeals of New York as predicated upon "reasonable suspicion," whereas we have concluded that the officer in <i><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span></i> had probable cause for an arrest, while the policeman in <i><span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">Sibron</a></span></i> was not possessed of any information which would justify an intrusion upon rights protected by the Fourth Amendment.</p>
<p>[21]  It is argued in dissent that this Court has in effect overturned factual findings by the two courts below that the search in this case was a self-protective measure on the part of Patrolman Martin, who thought that Sibron might have been reaching for a gun. It is true, as we have noted, that the Court of Appeals of New York apparently rested its approval of the search on this view. The trial court, however, made no such finding of fact. The trial judge adopted the theory of the prosecution at the hearing on the motion to suppress. This theory was that there was probable cause to arrest Sibron for some crime having to do with narcotics. The fact which tipped the scales for the trial court had nothing to do with danger to the policeman. The judge expressly changed his original view and held the heroin admissible upon being reminded that Sibron had admitted on the stand that he spoke to the addicts about narcotics. This admission was not relevant on the issue of probable cause, and we do not understand the dissent to take the position that prior to the discovery of heroin, there was probable cause for an arrest.
</p>
<p>Moreover, Patrolman Martin himself never at any time put forth the notion that he acted to protect himself. As we have noted, this subject never came up, until on re-direct examination defense counsel raised the question whether Patrolman Martin thought Sibron was going for a gun. See n. 4, <i>supra.</i> This was the only reference to weapons at any point in the hearing, and the subject was swiftly dropped. In the circumstances an unarticulated "finding" by an appellate court which wrote no opinion, apparently to the effect that the officer's invasion of Sibron's person comported with the Constitution because of the need to protect himself, is not deserving of controlling deference.</p>
<p>[22]  See n. 7, <i>supra.</i></p>
<p>[*]  See N. Y. Pen. Code §§ 140.20, 140.25 (1967).</p>
<p>[1]  For a thoughtful study of many of these points, see ALI Model Code of Pre-Arraignment Procedure, Tentative Draft No. 1, §§ 2.01, 2.02, and the commentary on these sections appearing at 87-105.</p>
<p>[2]  It is true, as the Court states, that the New York courts attributed such a statement to him. The attribution seems to me unwarranted by the record.</p>
<p>[3]  <i>E. g., </i><i>Beck</i> v. <i>Ohio,</i> <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89</a></span>; <i>Rios</i> v. <i>United States,</i> <span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/" aria-description="Citation for case: Rios v. United States">364 U. S. 253</a></span>; <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span>. In <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States"><i>Henry, supra,</i> at 100</a></span>, the Court said that <span class="citation no-link">18 U. S. C. § 3052</span> "states the constitutional standard" for felony arrests by FBI agents without warrant. That section authorized agents to "make arrests without warrant for any offense against the United States committed in their presence, or for any felony cognizable under the laws of the United States if they have reasonable grounds to believe that the person to be arrested has committed or is committing such felony." Under <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, a parallel standard is applicable to warrantless arrests by state and local police.</p>
<p>[4]  Compare <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span>, in which the Court said there was "far from enough evidence . . . to justify a magistrate in issuing a warrant." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States"><i>Id.,</i> at 103</a></span>. Agents knew that a federal crime, theft of whisky from an interstate shipment, had been committed "in the neighborhood." Petitioner was observed driving into an alley, picking up packages, and driving away. I agree that these facts did not constitute probable cause, but find it hard to see that the evidence here was more impressive.</p>
<p>[5]  The leading case is <i>United States</i> v. <i>Rabinowitz,</i> <span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span>.</p>

</div>
```

---

## GROUP: content/cases/Silverman v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: "Silverman v. United States"
type: case
citation: "365 U.S. 505 (1961)"
parallel_cite: "81 S. Ct. 679; 5 L. Ed. 2d 734; 97 A.L.R. 2d 1277"
neutral_cite: 1961 U.S. LEXIS 1605
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1961
date_decided: 1961-03-06
docket: 66
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1961-03-06
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Silverman v. United States
  varies_by_point: false
  scope_note: "Pre-Katz trespass-based holding; the property-intrusion test was reaffirmed as an independent approach in United States v. Jones."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106187/silverman-v-united-states/"
  cluster_id: 106187
  opinion_id: 106187
  identity_checked: true
homes:
  - page: "[[Trespass]]"
    role: "Key — Progeny / Refinement"
related: ["[[Katz v. United States]]", "[[United States v. Jones]]", "[[Olmstead v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "trespass", "electronic-surveillance"]
holding: "A 'spike mike' physically penetrating the wall into the house was a search — an unauthorized physical intrusion into a constitutionally protected area, not measured by 'technical trespass' niceties."
lake:
  record_id: Silverman v. United States
  status: verified
  projected_at: 2026-07-09
---

# Silverman v. United States

*365 U.S. 505 (1961)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
To overhear conversations of Silverman and others suspected of a gambling operation, police drove a "spike mike" through a party wall until it contacted a heating duct, turning the home's duct system into a giant microphone. The overheard conversations were used against the petitioners at trial.

## Issue
Whether using a spike mike that physically penetrates a wall to listen to conversations inside a home is a Fourth Amendment search.

## Rule
A physical intrusion into the home to eavesdrop is a search. "[T]he eavesdropping was accomplished by means of an unauthorized physical penetration into the premises occupied by the petitioners." — 365 U.S. at 509. ^pin-509

The Court distinguished its earlier electronic-surveillance decisions because there the eavesdropping "had not been accomplished by means of an unauthorized physical encroachment within a constitutionally protected area." — [*Id.* at 510](https://www.courtlistener.com/opinion/106187/silverman-v-united-states/#:~:text=had%20not%20been%20accomplished%20by). ^pin-510

And the result did not depend on property-law technicalities: "In these circumstances we need not pause to consider whether or not there was a technical trespass under the local property law .... Inherent Fourth Amendment rights are not inevitably measurable in terms of ancient niceties of tort or real property law." — *Id.* at 511. ^pin-511

## Application
The officers heard the petitioners' conversations only by usurping part of the home's heating system—a physical intrusion into the house itself—so the surveillance was a search regardless of whether it amounted to a technical trespass. The evidence should have been suppressed, and the convictions were reversed.

## Conclusion
The spike-mike intrusion into the home was an unconstitutional search; the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Silverman*'s actual-intrusion holding predates [[Katz v. United States]], which supplemented it with the reasonable-expectation-of-privacy test; the property-based trespass approach *Silverman* exemplifies was reaffirmed as an independent test in [[United States v. Jones]], and it marks the boundary of the wiretap rule of [[Olmstead v. United States]].

## Appears on
- [[Trespass]] — *Key — Progeny / Refinement*

## Sources
- *Silverman v. United States*, 365 U.S. 505 (1961) — https://www.courtlistener.com/opinion/106187/silverman-v-united-states/ — pinpoints: 509, 510, 511.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "2b5251b01c4035f1", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "365 U.S. 505 (1961)", "court": "U.S. Supreme Court", "neutral_cite": "1961 U.S. LEXIS 1605", "official_citation_present": true, "parallel_cite": "81 S. Ct. 679; 5 L. Ed. 2d 734; 97 A.L.R. 2d 1277", "title": "Silverman v. United States", "year": "1961"}}
{"assertion_id": "01183af091dc1530", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A 'spike mike' physically penetrating the wall into the house was a search — an unauthorized physical intrusion into a constitutionally protected area, not measured by 'technical trespass' niceties.", "title": "Silverman v. United States"}}
{"assertion_id": "9a23ef6a8c82b7ca", "dimension": "support", "kind": "home_role", "locator": {"home": "Trespass"}, "payload": {"home": "Trespass", "role": "Key — Progeny / Refinement", "title": "Silverman v. United States"}}
{"assertion_id": "37f64db3836ba90e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Silverman v. United States"}}
{"assertion_id": "f9fed818bbcafd05", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1961-03-06", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Silverman v. United States", "field_i_validity": "good_law", "scope_note": "Pre-Katz trespass-based holding; the property-intrusion test was reaffirmed as an independent approach in United States v. Jones.", "title": "Silverman v. United States", "varies_by_point": "false"}}
```

### lake record — Silverman v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Silverman v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Silverman v. United States",
    "case_name_short": "Silverman",
    "case_name_full": "SILVERMAN Et Al. v. UNITED STATES",
    "input_case_name": "Silverman v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1961-03-06",
    "year": 1961,
    "docket": "66",
    "cluster_id": 106187,
    "lead_opinion_id": 106187,
    "sibling_ids": [
      106187,
      9422144,
      9422145,
      9422146
    ],
    "absolute_url": "/opinion/106187/silverman-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "365 U.S. 505",
      "volume": "365",
      "reporter": "U.S.",
      "page": "505",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "81 S. Ct. 679",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "679",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 734",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "734",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 A.L.R. 2d 1277",
        "volume": "97",
        "reporter": "A.L.R. 2d",
        "page": "1277",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1961 U.S. LEXIS 1605",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1605",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "365 U.S. 505",
        "volume": "365",
        "reporter": "U.S.",
        "page": "505",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 S. Ct. 679",
        "volume": "81",
        "reporter": "S. Ct.",
        "page": "679",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "5 L. Ed. 2d 734",
        "volume": "5",
        "reporter": "L. Ed. 2d",
        "page": "734",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1961 U.S. LEXIS 1605",
        "volume": "1961",
        "reporter": "U.S. LEXIS",
        "page": "1605",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 A.L.R. 2d 1277",
        "volume": "97",
        "reporter": "A.L.R. 2d",
        "page": "1277",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "365 U.S. 505",
    "official_selection": {
      "court_class": "scotus",
      "selected": "365 U.S. 505",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-509",
      "page": null,
      "quote": "through a party wall until it contacted a heating duct, turning the home's duct system into a giant microphone. The overheard conversations were used against the petitioners at trial. ## Issue Whether using a spike mike that physically penetrates a wall to listen to conversations inside a home is a Fourth Amendment search. ## Rule A physical intrusion into the home to eavesdrop is a search.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-510",
      "page": null,
      "quote": "had not been accomplished by means of an unauthorized physical encroachment within a constitutionally protected area.",
      "star_marker": "510",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11264,
      "fragment": "#:~:text=had%20not%20been%20accomplished%20by",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-511",
      "page": null,
      "quote": "In these circumstances we need not pause to consider whether or not there was a technical trespass under the local property law .... Inherent Fourth Amendment rights are not inevitably measurable in terms of ancient niceties of tort or real property law.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1961-03-06",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Silverman v. United States",
    "varies_by_point": false,
    "scope_note": "Pre-Katz trespass-based holding; the property-intrusion test was reaffirmed as an independent approach in United States v. Jones.",
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
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Grady",
          "cluster_id": 4649078,
          "cite": [
            "831 S.E.2d 542",
            "372 N.C. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turpin",
          "cluster_id": 4423584,
          "cite": [
            "2017 Ohio 7435",
            "96 N.E.3d 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Harte v. Board Comm'rs Cnty of Johnson",
          "cluster_id": 4411980,
          "cite": [
            "864 F.3d 1154",
            "2017 WL 3138494"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4409778,
          "cite": [
            "2017 COA 93"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Vasquez-Algarin",
          "cluster_id": 3199633,
          "cite": [
            "821 F.3d 467",
            "2016 U.S. App. LEXIS 7889",
            "2016 WL 1730540"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Edgar Parral-Dominguez",
          "cluster_id": 2819835,
          "cite": [
            "794 F.3d 440",
            "2015 U.S. App. LEXIS 12697",
            "2015 WL 4479530"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 2736404,
          "cite": [
            "152 So. 3d 619",
            "2014 Fla. App. LEXIS 14965",
            "2014 WL 4723562"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Thomas",
          "cluster_id": 1036878,
          "cite": [
            "726 F.3d 1086",
            "2013 U.S. App. LEXIS 16413",
            "2013 WL 4017239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane1_negative"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Forsyth",
          "cluster_id": 111481,
          "cite": [
            "86 L. Ed. 2d 411",
            "105 S. Ct. 2806",
            "472 U.S. 511",
            "1985 U.S. LEXIS 113",
            "53 U.S.L.W. 4798",
            "2 Fed. R. Serv. 3d 221"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alderman v. United States",
          "cluster_id": 107872,
          "cite": [
            "22 L. Ed. 2d 176",
            "89 S. Ct. 961",
            "394 U.S. 165",
            "1969 U.S. LEXIS 3287"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weatherford v. Bursey",
          "cluster_id": 109590,
          "cite": [
            "51 L. Ed. 2d 30",
            "97 S. Ct. 837",
            "429 U.S. 545",
            "1977 U.S. LEXIS 40"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. United States",
          "cluster_id": 112136,
          "cite": [
            "101 L. Ed. 2d 472",
            "108 S. Ct. 2529",
            "487 U.S. 533",
            "1988 U.S. LEXIS 2881",
            "56 U.S.L.W. 4801"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
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
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Ciraolo",
          "cluster_id": 111666,
          "cite": [
            "90 L. Ed. 2d 210",
            "106 S. Ct. 1809",
            "476 U.S. 207",
            "1986 U.S. LEXIS 154"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Silverman v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzI5OTU1MjAwMDAwJnM9MjY5OTY1NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106187+OR+9422144+OR+9422145+OR+9422146%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 15,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 15,
        "triage_snippet_classified": 185
      },
      "lane2_top_cited": {
        "query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NTEmcz0xMTA4ODImdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106187+OR+9422144+OR+9422145+OR+9422146%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 1,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106187 OR 9422144 OR 9422145 OR 9422146)",
    "indexed_citing_opinions": 819,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106187,
        "count": 741,
        "count_source": "search"
      },
      {
        "opinion_id": 9422144,
        "count": 94,
        "count_source": "search"
      },
      {
        "opinion_id": 9422145,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422146,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1326,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/silverman-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NzM0NDUmcz05NDUxMzU5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106187+OR+9422144+OR+9422145+OR+9422146%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106187,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 102883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 105021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 105194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 228400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
        "cited_id": 250199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106187,
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
    "date_created": "2026-07-05T19:36:36Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T19:36:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T19:36:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T19:43:15Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T19:36:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Silverman v. United States

```
<div>
<center><b><span class="citation" data-id="9422144"><a href="/opinion/106187/silverman-v-united-states/" aria-description="Citation for case: Silverman v. United States">365 U.S. 505</a></span> (1961)</b></center>
<center><h1>SILVERMAN ET AL.<br>
v.<br>
UNITED STATES.</h1></center>
<center>No. 66.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 5, 1960.</center>
<center>Decided March 6, 1961.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE DISTRICT OF COLUMBIA CIRCUIT.
<p><i>Edward Bennett Williams</i> argued the cause for petitioners. With him on the briefs was <i>Agnes A. Neill.</i></p>
<p><i>John F. Davis</i> argued the cause for the United States. On the briefs were <i>Solicitor General Rankin, Assistant Attorney General Wilkey, Beatrice Rosenberg, J. F. Bishop</i> and <i>Julia P. Cooper.</i></p>
<p><span class="star-pagination">*506</span> MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>The petitioners were tried and found guilty in the District Court for the District of Columbia upon three counts of an indictment charging gambling offenses under the District of Columbia Code. At the trial police officers were permitted to describe incriminating conversations engaged in by the petitioners at their alleged gambling establishment, conversations which the officers had overheard by means of an electronic listening device. The convictions were affirmed by the Court of Appeals, 107 U. S. App. D. C. 144, <span class="citation" data-id="9447215"><a href="/opinion/250199/julius-silverman-v-united-states-of-america-meyer-schwartz-v-united/" aria-description="Citation for case: Julius Silverman v. United States of America, Meyer...">275 F. 2d 173</a></span>, and we granted certiorari to consider the contention that the officers' testimony as to what they had heard through the electronic instrument should not have been admitted into evidence. <span class="citation multiple-matches"><a href="/c/U.%20S./363/801/">363 U. S. 801</a></span>.</p>
<p>The record shows that in the spring of 1958 the District of Columbia police had reason to suspect that the premises at 408 21st Street, N. W., in Washington, were being used as the headquarters of a gambling operation. They gained permission from the owner of the vacant adjoining row house to use it as an observation post. From this vantage point for a period of at least three consecutive days in April 1958, the officers employed a so-called "spike mike" to listen to what was going on within the four walls of the house next door.</p>
<p>The instrument in question was a microphone with a spike about a foot long attached to it, together with an amplifier, a power pack, and earphones. The officers inserted the spike under a baseboard in a second-floor room of the vacant house and into a crevice extending several inches into the party wall, until the spike hit something solid "that acted as a very good sounding board." The record clearly indicates that the spike made contact with a heating duct serving the house occupied <span class="star-pagination">*507</span> by the petitioners, thus converting their entire heating system into a conductor of sound. Conversations taking place on both floors of the house were audible to the officers through the earphones, and their testimony regarding these conversations, admitted at the trial over timely objection, played a substantial part in the petitioners' convictions.<sup>[1]</sup></p>
<p>Affirming the convictions, the Court of Appeals held that the trial court had not erred in admitting the officers' testimony. The court was of the view that the officers' use of the spike mike had violated neither the Communications Act of 1934, <span class="citation no-link">47 U. S. C. § 605</span>, cf. <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="9418943"><a href="/opinion/102883/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">302 U. S. 379</a></span>, nor the petitioners' rights under the Fourth Amendment, cf. <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span>.</p>
<p>In reaching these conclusions the court relied primarily upon our decisions in <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>, and <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>. Judge Washington dissented, believing that, even if the petitioners' Fourth Amendment rights had not been abridged, the officers' conduct had transgressed the standards of due process guaranteed by the Fifth Amendment. Cf. <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/" aria-description="Citation for case: Irvine v. California">347 U. S. 128</a></span>.</p>
<p>As to the inapplicability of § 605 of the Communications Act of 1934, we agree with the Court of Appeals. That section provides that ". . . no person not being <span class="star-pagination">*508</span> authorized by the sender shall intercept any communication and divulge or publish the existence, contents, substance, purport, effect, or meaning of such intercepted communication to any person . . . ." While it is true that much of what the officers heard consisted of the petitioners' share of telephone conversations, we cannot say that the officers intercepted these conversations within the meaning of the statute.</p>
<p>Similar contentions have been rejected here at least twice before. In <i>Irvine</i> v. <i>California,</i> <span class="citation" data-id="9421039"><a href="/opinion/105194/irvine-v-california/#131" aria-description="Citation for case: Irvine v. California">347 U. S. 128, 131</a></span>, the Court said: "Here the apparatus of the officers was not in any way connected with the telephone facilities, there was no interference with the communications system, there was no interception of any message. All that was heard through the microphone was what an eavesdropper, hidden in the hall, the bedroom, or the closet, might have heard. We do not suppose it is illegal to testify to what another person is heard to say merely because he is saying it into a telephone." In <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/#134" aria-description="Citation for case: Goldman v. United States">316 U. S. 129, 134</a></span>, it was said that "The listening in the next room to the words of [the petitioner] as he talked into the telephone receiver was no more the interception of a wire communication, within the meaning of the Act, than would have been the overhearing of the conversation by one sitting in the same room."</p>
<p>In presenting here the petitioners' Fourth Amendment claim, counsel has painted with a broad brush. We are asked to reconsider our decisions in <i>Goldman</i> v. <i>United States, supra</i><i>,</i> and <i>On Lee</i> v. <i>United States, supra</i><i>.</i> We are told that re-examination of the rationale of those cases, and of <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>, from which they stemmed, is now essential in the light of recent and projected developments in the science of electronics. We are favoured with a description of "a device known as the parabolic microphone which can pick up a conversation three hundred yards away." We are told of a <span class="star-pagination">*509</span> "still experimental technique whereby a room is flooded with a certain type of sonic wave," which, when perfected, "will make it possible to overhear everything said in a room without ever entering it or even going near it." We are informed of an instrument "which can pick up a conversation through an open office window on the opposite side of a busy street."<sup>[2]</sup></p>
<p>The facts of the present case, however, do not require us to consider the large questions which have been argued. We need not here contemplate the Fourth Amendment implications of these and other frightening paraphernalia which the vaunted marvels of an electronic age may visit upon human society. Nor do the circumstances here make necessary a re-examination of the Court's previous decisions in this area. For a fair reading of the record in this case shows that the eavesdropping was accomplished by means of an unauthorized physical penetration into the premises occupied by the petitioners. As Judge Washington pointed out without contradiction in the Court of Appeals: "Every inference, and what little direct evidence there was, pointed to the fact that the spike made contact with the heating duct, as the police admittedly hoped it would. Once the spike touched the heating duct, the duct became in effect a giant microphone, running through the entire house occupied by appellants." 107 U. S. App. D. C., at 150, <span class="citation" data-id="9447215"><a href="/opinion/250199/julius-silverman-v-united-states-of-america-meyer-schwartz-v-united/#179" aria-description="Citation for case: Julius Silverman v. United States of America, Meyer...">275 F. 2d, at 179</a></span>.</p>
<p>Eavesdropping accomplished by means of such a physical intrusion is beyond the pale of even those decisions in <span class="star-pagination">*510</span> which a closely divided Court has held that eavesdropping accomplished by other electronic means did not amount to an invasion of Fourth Amendment rights. In <i>Goldman</i> v. <i>United States, supra</i><i>,</i> the Court held that placing a detectaphone against an office wall in order to listen to conversations taking place in the office next door did not violate the Amendment. In <i>On Lee</i> v. <i>United States, supra</i><i>,</i> a federal agent, who was acquainted with the petitioner, entered the petitioner's laundry and engaged him in an incriminating conversation. The agent had a microphone concealed upon his person. Another agent, stationed outside with a radio receiving set, was tuned in on the conversation, and at the petitioner's subsequent trial related what he had heard. These circumstances were held not to constitute a violation of the petitioner's Fourth Amendment rights.</p>
<p>But in both <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> and <i><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">On Lee</a></span></i> the Court took pains explicitly to point out that the eavesdropping had not been accomplished by means of an unauthorized physical encroachment within a constitutionally protected area. In <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> there had in fact been a prior physical entry into the petitioner's office for the purpose of installing a different listening apparatus, which had turned out to be ineffective. The Court emphasized that this earlier physical trespass had been of no relevant assistance in the later use of the detectaphone in the adjoining office. <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/#134" aria-description="Citation for case: Goldman v. United States">316 U. S., at 134-135</a></span>. And in <i><span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">On Lee</a></span>,</i> as the Court said, ". . . no trespass was committed." The agent went into the petitioner's place of business "with the consent, if not by the implied invitation, of the petitioner." <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/#751" aria-description="Citation for case: On Lee v. United States">343 U. S., at 751-752</a></span>.</p>
<p>The absence of a physical invasion of the petitioner's premises was also a vital factor in the Court's decision in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438</a></span>. In holding that the wiretapping there did not violate the Fourth Amendment, the Court noted that "[t]he insertions <span class="star-pagination">*511</span> were made without trespass upon any property of the defendants. They were made in the basement of the large office building. The taps from house lines were made in the streets near the houses." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#457" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 457</a></span>. "There was no entry of the houses or offices of the defendants." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#464" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 464</a></span>. Relying upon these circumstances, the Court reasoned that "[t]he intervening wires are not part of [the defendant's] house or office any more than are the highways along which they are stretched." <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#465" aria-description="Citation for case: Olmstead v. United States">277 U. S., at 465</a></span>.</p>
<p>Here, by contrast, the officers overheard the petitioners' conversations only by usurping part of the petitioners' house or officea heating system which was an integral part of the premises occupied by the petitioners, a usurpation that was effected without their knowledge and without their consent. In these circumstances we need not pause to consider whether or not there was a technical trespass under the local property law relating to party walls.<sup>[3]</sup> Inherent Fourth Amendment rights are not inevitably measurable in terms of ancient niceties of tort or real property law. See <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#266" aria-description="Citation for case: Jones v. United States">362 U. S. 257, 266</a></span>; <i>On Lee</i> v. <i>United States, supra,</i> at 752; <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/#51" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48, 51</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#454" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 454</a></span>.</p>
<p>The Fourth Amendment, and the personal rights which it secures, have a long history. At the very core stands the right of a man to retreat into his own home and there be free from unreasonable governmental intrusion. <i>Entick</i> v. <i>Carrington,</i> 19 Howell's State Trials 1029, 1066; <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626-630</a></span>.<sup>[4]</sup> This <span class="star-pagination">*512</span> Court has never held that a federal officer may without warrant and without consent physically entrench into a man's office or home, there secretly observe or listen, and relate at the man's subsequent criminal trial what was seen or heard.</p>
<p>A distinction between the detectaphone employed in <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> and the spike mike utilized here seemed to the Court of Appeals too fine a one to draw. The court was "unwilling to believe that the respective rights are to be measured in fractions of inches." But decision here does not turn upon the technicality of a trespass upon a party wall as a matter of local law. It is based upon the reality of an actual intrusion into a constitutionally protected area. What the Court said long ago bears repeating now: "It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure." <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#635" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 635</a></span>. We find no occasion to re-examine <i><span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">Goldman</a></span></i> here, but we decline to go beyond it, by even a fraction of an inch.</p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE DOUGLAS, concurring.</p>
<p>My trouble with <i>stare decisis</i> in this field is that it leads us to a matching of cases on irrelevant facts. An electronic device on the outside wall of a house is a permissible invasion of privacy according to <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>, while an electronic device that penetrates the wall, as here, is not. Yet the invasion <span class="star-pagination">*513</span> of privacy is as great in one case as in the other. The concept of "an unauthorized physical penetration into the premises," on which the present decision rests, seems to me to be beside the point. Was not the wrong in both cases done when the intimacies of the home were tapped, recorded, or revealed? The depth of the penetration of the electronic deviceeven the degree of its remoteness from the inside of the houseis not the measure of the injury. There is in each such case a search that should be made, if at all, only on a warrant issued by a magistrate. I stated my views in <i>On Lee</i> v. <i>United States,</i> <span class="citation" data-id="9420768"><a href="/opinion/105021/on-lee-v-united-states/" aria-description="Citation for case: On Lee v. United States">343 U. S. 747</a></span>, and adhere to them. Our concern should not be with the trivialities of the local law of trespass, as the opinion of the Court indicates. But neither should the command of the Fourth Amendment be limited by nice distinctions turning on the kind of electronic equipment employed. Rather our sole concern should be with whether the privacy of the home was invaded. Since it was invaded here, and since no search warrant was obtained as required by the Fourth Amendment and Rule 41 of the Federal Rules of Criminal Procedure, I agree with the Court that the judgment of conviction must be set aside.</p>
<p>MR. JUSTICE CLARK and MR. JUSTICE WHITTAKER, concurring.</p>
<p>In view of the determination by the majority that the unauthorized physical penetration into petitioners' premises constituted sufficient trespass to remove this case from the coverage of earlier decisions, we feel obliged to join in the Court's opinion.</p>
<h2>NOTES</h2>
<p>[1]  Alleging that the conversations thus overheard had been the basis for a search warrant under which other incriminating evidence was discovered at 408 21st Street, N. W., the petitioners sought unsuccessfully to suppress the evidence obtained upon execution of the warrant. It is the Government's position that there were ample grounds to support the search warrant, even without what was overheard by means of the spike mike. We deal here only with the admissibility at the trial of the officers' testimony as to what they heard by means of the listening device, leaving a determination of the warrant's validity to abide the event of a new trial.</p>
<p>[2]  See Hearings before the Subcommittee on Constitutional Rights of the Committee on the Judiciary, United States Senate, 85th Cong., 2d Sess., on Wiretapping, Eavesdropping, and the Bill of Rights; Hearings before Subcommittee No. 5 of the Committee on the Judiciary, House of Representatives, 84th Cong., 1st Sess., on Wiretapping; Dash, Schwartz and Knowlton, The Eavesdroppers (Rutgers University Press, 1959), pp. 346-358.</p>
<p>[3]  See <i>Fowler</i> v. <i>Koehler,</i> 43 App. D. C. 349.</p>
<p>[4]  William Pitt's eloquent description of this right has been often quoted. The late Judge Jerome Frank made the point in more contemporary language: "A man can still control a small part of his environment, his house; he can retreat thence from outsiders, secure in the knowledge that they cannot get at him without disobeying the Constitution. That is still a sizable hunk of libertyworth protecting from encroachment. A sane, decent, civilized society must provide some such oasis, some shelter from public scrutiny, some insulated enclosure, some enclave, some inviolate place which is a man's castle." <i>United States</i> v. <i>On Lee,</i> <span class="citation" data-id="9443046"><a href="/opinion/228400/united-states-v-on-lee/#315" aria-description="Citation for case: United States v. On Lee">193 F. 2d 306, 315-316</a></span> (dissenting opinion).</p>

</div>
```

---
