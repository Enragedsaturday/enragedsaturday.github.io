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

## GROUP: _overhaul2/lake/cases/Garrity v. New Jersey.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Garrity v. New Jersey"
type: case
citation: "385 U.S. 493 (1967)"
parallel_cite: "87 S. Ct. 616; 17 L. Ed. 2d 562"
neutral_cite: 1967 U.S. LEXIS 2882
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1967
date_decided: 1967-01-23
docket: 13
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1967-01-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Garrity v. New Jersey
  varies_by_point: false
  scope_note: "Good law; foundation of the 'Garrity rule' / Garrity warnings for compelled public-employee statements."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107336/garrity-v-new-jersey/"
  cluster_id: 107336
  opinion_id: 107336
  identity_checked: true
homes:
  - page: "[[Public-Employee Compelled Statements (Garrity)]]"
    role: "Key — Anchor"
related: ["[[Gardner v. Broderick]]", "[[Lefkowitz v. Turley]]", "[[Kalkines v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "self-incrimination", "public-employee", "garrity", "compelled-statements"]
holding: "Statements compelled from a public employee under threat of removal from office are involuntary, and the Fourteenth Amendment bars their use against the employee in a subsequent criminal prosecution (the Garrity rule)."
lake:
  record_id: Garrity v. New Jersey
  status: verified
  projected_at: 2026-07-09
---

# Garrity v. New Jersey

*385 U.S. 493 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
New Jersey police officers were investigated for fixing traffic tickets. Before questioning, each officer was warned that anything he said could be used against him in a criminal proceeding, that he could refuse to answer to avoid self-incrimination, but that under a state forfeiture-of-office statute a refusal to answer would cost him his job. The officers answered, and their statements were used to convict them of conspiracy to obstruct the administration of the traffic laws. They challenged the convictions as resting on coerced statements.

## Issue
Whether statements obtained from public employees under threat of removal from office are made voluntarily, such that they may be used against the employees in a subsequent criminal prosecution consistent with the Fourteenth Amendment.

## Rule
No. The threat of discharge renders such statements involuntary. "The choice given petitioners was either to forfeit their jobs or to incriminate themselves. The option to lose their means of livelihood or to pay the penalty of self-incrimination is the antithesis of free choice to speak out or to remain silent." — 385 U.S. at 497. ^pin-497

The Court therefore held: "We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic." — [*Id.* at 500](https://www.courtlistener.com/opinion/107336/garrity-v-new-jersey/#:~:text=We%20now%20hold%20the%20protection). ^pin-500

## Application
Each officer was confronted with the choice to answer the investigators' questions or lose his job under the forfeiture statute. Faced with self-incrimination on one side and loss of livelihood on the other, the officers' answers were the product of coercion rather than free will, much like the pressures condemned in *[[Miranda v. Arizona|Miranda]]*. Because the convictions rested on these compelled statements, they could not stand.

## Conclusion
The statements were coerced and inadmissible in the criminal prosecutions; the convictions were reversed. *Garrity* establishes that a public employer may not compel an employee, on pain of job loss, to make statements that are then used against him in a criminal case — the foundation of the "Garrity rule" and [[Public-Employee Compelled Statements (Garrity)|Garrity warnings]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Garrity* is good law and anchors the public-employee compelled-statement line, refined by [[Gardner v. Broderick]] and [[Lefkowitz v. Turley]] (a public employee may be compelled to answer narrowly job-related questions only under a grant of use immunity, and may not be fired merely for asserting the privilege) and the federal [[Kalkines v. United States]] warning.

## Appears on
- [[Public-Employee Compelled Statements (Garrity)]] — *Key — Anchor*

## Sources
- *Garrity v. New Jersey*, 385 U.S. 493 (1967) — https://www.courtlistener.com/opinion/107336/garrity-v-new-jersey/ — pinpoints: 497, 500.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "154007b25d752e77", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Garrity v. New Jersey"}, "payload": {"all": [{"cite": "385 U.S. 493", "page": "493", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "385"}, {"cite": "87 S. Ct. 616", "page": "616", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "87"}, {"cite": "17 L. Ed. 2d 562", "page": "562", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "17"}, {"cite": "1967 U.S. LEXIS 2882", "page": "2882", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1967"}], "display": "385 U.S. 493", "official": {"cite": "385 U.S. 493", "page": "493", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "385"}, "official_selection_present": true, "record_id": "Garrity v. New Jersey"}}
{"assertion_id": "481b1976c6f4b88c", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-500", "record_id": "Garrity v. New Jersey"}, "payload": {"fragment": "#:~:text=We%20now%20hold%20the%20protection", "page": null, "pin_id": "pin-500", "pinpoint_status": "star-verified", "quote": "We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.", "quote_fidelity": "matched", "record_id": "Garrity v. New Jersey", "star_marker": "500"}}
{"assertion_id": "5430e9e74cd939bf", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-497", "record_id": "Garrity v. New Jersey"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-497", "pinpoint_status": "slip-only", "quote": "--- # Garrity v. New Jersey *385 U.S. 493 (1967)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New Jersey police officers were investigated for fixing traffic tickets. Before questioning, each officer was warned that anything he said could be used against him in a criminal proceeding, that he could refuse to answer to avoid self-incrimination, but that under a state forfeiture-of-office statute a refusal to answer would cost him his job. The officers answered, and their statements were used to convict them of conspiracy to obstruct the administration of the traffic laws. They challenged the convictions as resting on coerced statements. ## Issue Whether statements obtained from public employees under threat of removal from office are made voluntarily, such that they may be used against the employees in a subsequent criminal prosecution consistent with the Fourteenth Amendment. ## Rule No. The threat of discharge renders such statements involuntary.", "quote_fidelity": "mismatch", "record_id": "Garrity v. New Jersey", "star_marker": null}}
{"assertion_id": "6678172268a0df95", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Garrity v. New Jersey"}, "payload": {"as_of_content": "1967-01-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Garrity v. New Jersey", "scope_note": "Good law; foundation of the 'Garrity rule' / Garrity warnings for compelled public-employee statements.", "varies_by_point": false}}
```

### lake record — Garrity v. New Jersey

```json
{
  "schema_version": "s2.v1",
  "record_id": "Garrity v. New Jersey",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Garrity v. New Jersey",
    "case_name_short": "Garrity",
    "case_name_full": "GARRITY Et Al. v. NEW JERSEY",
    "input_case_name": "Garrity v. New Jersey",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1967-01-23",
    "year": 1967,
    "docket": "13",
    "cluster_id": 107336,
    "lead_opinion_id": 107336,
    "sibling_ids": [
      107336,
      9423318,
      9423319
    ],
    "absolute_url": "/opinion/107336/garrity-v-new-jersey/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "385 U.S. 493",
      "volume": "385",
      "reporter": "U.S.",
      "page": "493",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "87 S. Ct. 616",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 562",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "562",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1967 U.S. LEXIS 2882",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "385 U.S. 493",
        "volume": "385",
        "reporter": "U.S.",
        "page": "493",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "87 S. Ct. 616",
        "volume": "87",
        "reporter": "S. Ct.",
        "page": "616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "17 L. Ed. 2d 562",
        "volume": "17",
        "reporter": "L. Ed. 2d",
        "page": "562",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1967 U.S. LEXIS 2882",
        "volume": "1967",
        "reporter": "U.S. LEXIS",
        "page": "2882",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "385 U.S. 493",
    "official_selection": {
      "court_class": "scotus",
      "selected": "385 U.S. 493",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-497",
      "page": null,
      "quote": "--- # Garrity v. New Jersey *385 U.S. 493 (1967)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background New Jersey police officers were investigated for fixing traffic tickets. Before questioning, each officer was warned that anything he said could be used against him in a criminal proceeding, that he could refuse to answer to avoid self-incrimination, but that under a state forfeiture-of-office statute a refusal to answer would cost him his job. The officers answered, and their statements were used to convict them of conspiracy to obstruct the administration of the traffic laws. They challenged the convictions as resting on coerced statements. ## Issue Whether statements obtained from public employees under threat of removal from office are made voluntarily, such that they may be used against the employees in a subsequent criminal prosecution consistent with the Fourteenth Amendment. ## Rule No. The threat of discharge renders such statements involuntary.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-500",
      "page": null,
      "quote": "We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.",
      "star_marker": "500",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15381,
      "fragment": "#:~:text=We%20now%20hold%20the%20protection",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1967-01-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Garrity v. New Jersey",
    "varies_by_point": false,
    "scope_note": "Good law; foundation of the 'Garrity rule' / Garrity warnings for compelled public-employee statements.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Gideon",
          "cluster_id": 4632199,
          "cite": [
            "2019 Ohio 2482",
            "130 N.E.3d 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Allen",
          "cluster_id": 4409967,
          "cite": [
            "864 F.3d 63",
            "2017 U.S. App. LEXIS 12942",
            "2017 WL 3040201"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gregory Wayne Powell",
          "cluster_id": 4348676,
          "cite": [
            "161 Idaho 774",
            "391 P.3d 659",
            "2017 WL 587254",
            "2017 Ida. App. LEXIS 17"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Von Behren",
          "cluster_id": 3202148,
          "cite": [
            "822 F.3d 1139",
            "2016 U.S. App. LEXIS 8567",
            "2016 WL 2641270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
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
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Patrick Smith v. State",
          "cluster_id": 2854959,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Korey Demaine Walker v. State",
          "cluster_id": 2855445,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Spielbauer v. County of Santa Clara",
          "cluster_id": 5608087,
          "cite": [
            "45 Cal. 4th 704",
            "199 P.3d 1125",
            "88 Cal. Rptr. 3d 590",
            "28 I.E.R. Cas. (BNA) 1254",
            "2009 Cal. LEXIS 1010"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Aguilera v. Baca",
          "cluster_id": 1390016,
          "cite": [
            "510 F.3d 1161",
            "27 I.E.R. Cas. (BNA) 31",
            "2007 U.S. App. LEXIS 29804",
            "2007 WL 4531990"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sher v. U.S. Department of Veterans Affairs",
          "cluster_id": 202763,
          "cite": [
            "488 F.3d 489",
            "26 I.E.R. Cas. (BNA) 243",
            "2007 U.S. App. LEXIS 12365",
            "90 Empl. Prac. Dec. (CCH) 43,067",
            "100 Fair Empl. Prac. Cas. (BNA) 1495",
            "2007 WL 1532655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In Re GAULT",
          "cluster_id": 107439,
          "cite": [
            "18 L. Ed. 2d 527",
            "87 S. Ct. 1428",
            "387 U.S. 1",
            "1967 U.S. LEXIS 1478",
            "40 Ohio Op. 2d 378"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Baxter v. Palmigiano",
          "cluster_id": 109429,
          "cite": [
            "47 L. Ed. 2d 810",
            "96 S. Ct. 1551",
            "425 U.S. 308",
            "1976 U.S. LEXIS 115"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dunn v. Blumstein",
          "cluster_id": 108485,
          "cite": [
            "31 L. Ed. 2d 274",
            "92 S. Ct. 995",
            "405 U.S. 330",
            "1972 U.S. LEXIS 75"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Murphy",
          "cluster_id": 111105,
          "cite": [
            "79 L. Ed. 2d 409",
            "104 S. Ct. 1136",
            "465 U.S. 420",
            "1984 U.S. LEXIS 33",
            "52 U.S.L.W. 4246"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cox Broadcasting Corp. v. Cohn",
          "cluster_id": 109207,
          "cite": [
            "43 L. Ed. 2d 328",
            "95 S. Ct. 1029",
            "420 U.S. 469",
            "1975 U.S. LEXIS 139",
            "32 Rad. Reg. 2d (P & F) 1511",
            "1 Media L. Rep. (BNA) 1819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Turley",
          "cluster_id": 108882,
          "cite": [
            "38 L. Ed. 2d 274",
            "94 S. Ct. 316",
            "414 U.S. 70",
            "1973 U.S. LEXIS 132"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McGautha v. California",
          "cluster_id": 108329,
          "cite": [
            "28 L. Ed. 2d 711",
            "91 S. Ct. 1454",
            "402 U.S. 183",
            "1971 U.S. LEXIS 107"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKune v. Lile",
          "cluster_id": 121146,
          "cite": [
            "153 L. Ed. 2d 47",
            "122 S. Ct. 2017",
            "536 U.S. 24",
            "2002 U.S. LEXIS 4206"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maness v. Meyers",
          "cluster_id": 109130,
          "cite": [
            "42 L. Ed. 2d 574",
            "95 S. Ct. 584",
            "419 U.S. 449",
            "1975 U.S. LEXIS 20"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Parker v. North Carolina",
          "cluster_id": 108139,
          "cite": [
            "25 L. Ed. 2d 785",
            "90 S. Ct. 1458",
            "397 U.S. 790",
            "1970 U.S. LEXIS 47"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lefkowitz v. Cunningham",
          "cluster_id": 109683,
          "cite": [
            "53 L. Ed. 2d 1",
            "97 S. Ct. 2132",
            "431 U.S. 801",
            "1977 U.S. LEXIS 19"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gardner v. Broderick",
          "cluster_id": 107738,
          "cite": [
            "20 L. Ed. 2d 1082",
            "88 S. Ct. 1913",
            "392 U.S. 273",
            "1968 U.S. LEXIS 1351"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garner v. United States",
          "cluster_id": 109400,
          "cite": [
            "47 L. Ed. 2d 370",
            "96 S. Ct. 1178",
            "424 U.S. 648",
            "1976 U.S. LEXIS 138"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Mandujano",
          "cluster_id": 109442,
          "cite": [
            "48 L. Ed. 2d 212",
            "96 S. Ct. 1768",
            "425 U.S. 564",
            "1976 U.S. LEXIS 6"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelley v. Johnson",
          "cluster_id": 109423,
          "cite": [
            "47 L. Ed. 2d 708",
            "96 S. Ct. 1440",
            "425 U.S. 238",
            "1976 U.S. LEXIS 35",
            "11 Empl. Prac. Dec. (CCH) 10,788"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis v. Higgins",
          "cluster_id": 112534,
          "cite": [
            "112 L. Ed. 2d 969",
            "111 S. Ct. 865",
            "498 U.S. 439",
            "1991 U.S. LEXIS 1142"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Uniformed Sanitation Men Ass'n v. Commissioner of Sanitation of New York",
          "cluster_id": 107739,
          "cite": [
            "20 L. Ed. 2d 1089",
            "88 S. Ct. 1917",
            "392 U.S. 280",
            "1968 U.S. LEXIS 1352"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kenneth Wynder v. James W. McMahon David Spahl, Robert Jones, Louis B. Barbaria, Craig Masterson, Individually, John Keats, Marine Midland Bank",
          "cluster_id": 785304,
          "cite": [
            "360 F.3d 73",
            "2004 U.S. App. LEXIS 3906",
            "93 Fair Empl. Prac. Cas. (BNA) 596",
            "2004 WL 370665"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Byers",
          "cluster_id": 108335,
          "cite": [
            "29 L. Ed. 2d 9",
            "91 S. Ct. 1535",
            "402 U.S. 424",
            "1971 U.S. LEXIS 128"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 1670023,
          "cite": [
            "755 N.W.2d 664",
            "279 Mich. App. 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles E. Egger v. Harlan C. Phillips",
          "cluster_id": 420747,
          "cite": [
            "710 F.2d 292"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Selective Service System v. Minnesota Public Interest Research Group",
          "cluster_id": 111260,
          "cite": [
            "82 L. Ed. 2d 632",
            "104 S. Ct. 3348",
            "468 U.S. 841",
            "1984 U.S. LEXIS 151",
            "52 U.S.L.W. 5140"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salinas v. Texas",
          "cluster_id": 903977,
          "cite": [
            "186 L. Ed. 2d 376",
            "133 S. Ct. 2174",
            "2013 U.S. LEXIS 4697",
            "570 U.S. 178",
            "81 U.S.L.W. 4467",
            "24 Fla. L. Weekly Fed. S 294",
            "2013 WL 2922119"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Avant v. Clifford",
          "cluster_id": 1549504,
          "cite": [
            "341 A.2d 629",
            "67 N.J. 496",
            "1975 N.J. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sheldon L. Wulf v. The City of Wichita, Gene Denton, and Richard Lamunyon",
          "cluster_id": 528293,
          "cite": [
            "883 F.2d 842"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Garrity v. New Jersey:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107336 OR 9423318 OR 9423319) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTQ2MDk2MDAwMDAwJnM9NDExMzg5MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107336+OR+9423318+OR+9423319%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(107336 OR 9423318 OR 9423319)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0xMTIzNjAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107336+OR+9423318+OR+9423319%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107336 OR 9423318 OR 9423319)",
        "reviewed": 22,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 22,
        "triage_read": 0,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107336 OR 9423318 OR 9423319)",
    "indexed_citing_opinions": 1024,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107336,
        "count": 906,
        "count_source": "search"
      },
      {
        "opinion_id": 9423318,
        "count": 134,
        "count_source": "search"
      },
      {
        "opinion_id": 9423319,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1543,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/garrity-v-new-jersey.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc5NzUwMzUmcz04NDA0NDA5JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107336+OR+9423318+OR+9423319%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107336,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 97150,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 99227,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 99901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 101688,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 102991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 104061,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105229,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105743,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106007,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107033,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107064,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 228335,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 2286396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107336,
        "cited_id": 2402426,
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
    "date_created": "2026-07-05T05:12:44Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:12:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:12:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:18:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:12:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Garrity v. New Jersey

```
<div>
<center><b><span class="citation" data-id="9423318"><a href="/opinion/107336/garrity-v-new-jersey/" aria-description="Citation for case: Garrity v. New Jersey">385 U.S. 493</a></span> (1967)</b></center>
<center><h1>GARRITY ET AL.<br>
v.<br>
NEW JERSEY.</h1></center>
<center>No. 13.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 10, 1966.</center>
<center>Decided January 16, 1967.</center>
APPEAL FROM THE SUPREME COURT OF NEW JERSEY.
<p><span class="star-pagination">*494</span> <i>Daniel L. O'Connor</i> argued the cause for appellants. With him on the brief was <i>Eugene Gressman.</i></p>
<p><i>Alan B. Handler,</i> First Assistant Attorney General of New Jersey, argued the cause for appellee. With him on the brief were <i>Arthur J. Sills,</i> Attorney General, and <i>Norman Heine.</i></p>
<p>MR. JUSTICE DOUGLAS delivered the opinion of the Court.</p>
<p>Appellants were police officers in certain New Jersey boroughs. The Supreme Court of New Jersey ordered that alleged irregularities in handling cases in the municipal courts of those boroughs be investigated by the Attorney General, invested him with broad powers of inquiry and investigation, and directed him to make a report to the court. The matters investigated concerned alleged fixing of traffic tickets.</p>
<p>Before being questioned, each appellant was warned (1) that anything he said might be used against him in any state criminal proceeding; (2) that he had the privilege to refuse to answer if the disclosure would tend to incriminate him; but (3) that if he refused to answer he would be subject to removal from office.<sup>[1]</sup></p>
<p><span class="star-pagination">*495</span> Appellants answered the questions. No immunity was granted, as there is no immunity statute applicable in these circumstances. Over their objections, some of the answers given were used in subsequent prosecutions for conspiracy to obstruct the administration of the traffic laws. Appellants were convicted and their convictions were sustained over their protests that their statements were coerced,<sup>[2]</sup> by reason of the fact that, if they refused to answer, they could lose their positions with the police department. See 44 N. J. 209, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/" aria-description="Citation for case: State v. Naglee">207 A. 2d 689</a></span>, 44 N. J. 259, <span class="citation" data-id="2286396"><a href="/opinion/2286396/state-v-holroyd/" aria-description="Citation for case: State v. Holroyd">208 A. 2d 146</a></span>.</p>
<p>We postponed the question of jurisdiction to a hearing on the merits. <span class="citation multiple-matches"><a href="/c/U.%20S./383/941/">383 U. S. 941</a></span>. The statute whose validity was sought to be "drawn in question," <span class="citation no-link">28 U. S. C. § 1257</span> (2), was the forfeiture statute.<sup>[3]</sup> But the New <span class="star-pagination">*496</span> Jersey Supreme Court refused to reach that question (44 N. J., at 223, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/#697" aria-description="Citation for case: State v. Naglee">207 A. 2d, at 697</a></span>), deeming the voluntariness of the statements as the only issue presented. <i>Id.,</i> at 220-222, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/#695" aria-description="Citation for case: State v. Naglee">207 A. 2d, at 695-696</a></span>. The statute is therefore too tangentially involved to satisfy <span class="citation no-link">28 U. S. C. § 1257</span> (2), for the only bearing it had was whether, valid or not, the fear of being discharged under it for refusal to answer on the one hand and the fear of self-incrimination on the other was "a choice between the rock and the whirlpool"<sup>[4]</sup> which made the statements products of coercion in violation of the Fourteenth Amendment. We therefore dismiss the appeal, treat the papers as a petition for certiorari (<span class="citation no-link">28 U. S. C. § 2103</span>), grant the petition and proceed to the merits.</p>
<p>We agree with the New Jersey Supreme Court that the forfeiture-of-office statute is relevant here only for the bearing it has on the voluntary character of the statements used to convict petitioners in their criminal prosecutions.</p>
<p>The choice imposed on petitioners was one between self-incrimination or job forfeiture. Coercion that vitiates a confession under <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, and related cases can be "mental as well as physical"; "the blood of the accused is not the only hallmark of an unconstitutional inquisition." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206</a></span>. Subtle pressures (<i>Leyra</i> v. <i>Denno,</i> <span class="citation" data-id="9421089"><a href="/opinion/105229/leyra-v-denno/" aria-description="Citation for case: Leyra v. Denno">347 U. S. 556</a></span>; <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>) may be as telling as coarse and vulgar ones. The question is whether the accused was deprived of his "free choice to admit, to deny, or to refuse to answer." <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California">314 U. S. 219, 241</a></span>.</p>
<p>We adhere to <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, a civil forfeiture action against property. A statute offered <span class="star-pagination">*497</span> the owner an election between producing a document or forfeiture of the goods at issue in the proceeding. This was held to be a form of compulsion in violation of both the Fifth Amendment and the Fourth Amendment. <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#634" aria-description="Citation for case: Boyd v. United States"><i>Id.,</i> at 634-635</a></span>. It is that principle that we adhere to and apply in <i>Spevack</i> v. <i>Klein</i><i>, post,</i> p. 511.</p>
<p>The choice given petitioners was either to forfeit their jobs or to incriminate themselves. The option to lose their means of livelihood or to pay the penalty of self-incrimination is the antithesis of free choice to speak out or to remain silent. That practice, like interrogation practices we reviewed in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 464-465</a></span>, is "likely to exert such pressure upon an individual as to disable him from making a free and rational choice." We think the statements were infected by the coercion<sup>[5]</sup> inherent in this scheme of questioning <span class="star-pagination">*498</span> and cannot be sustained as voluntary under our prior decisions.</p>
<p>It is said that there was a "waiver." That, however, is a federal question for us to decide. <i>Union Pac. R. R. Co.</i> v. <i>Pub. Service Comm.,</i> <span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/#69" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission">248 U. S. 67, 69-70</a></span>; <i>Stevens</i> v. <i>Marks,</i> <span class="citation" data-id="9423156"><a href="/opinion/107173/stevens-v-marks/#243" aria-description="Citation for case: Stevens v. Marks">383 U. S. 234, 243-244</a></span>. The Court in <i>Union Pac. R. R. Co.</i> v. <i>Pub. Service <span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission">Comm., supra</a></span></i><i>,</i> in speaking of a certificate exacted under protest and in violation of the Commerce Clause, said:</p>
<blockquote>"Were it otherwise, as conduct under duress involves a choice, it always would be possible for a State to impose an unconstitutional burden by the threat of penalties worse than it in case of a failure to accept it, and then to declare the acceptance voluntary . . . ." <span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/#70" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission"><i>Id.,</i> at 70</a></span>.</blockquote>
<p>Where the choice is "between the rock and the whirlpool," duress is inherent in deciding to "waive" one or the other.</p>
<blockquote>"It always is for the interest of a party under duress to choose the lesser of two evils. But the fact that a choice was made according to interest does not exclude duress. It is the characteristic of duress properly so called." <i><span class="citation" data-id="99227"><a href="/opinion/99227/union-pacific-railroad-v-public-service-commission/" aria-description="Citation for case: Union Pacific Railroad v. Public Service Commission">Ibid.</a></span></i>
</blockquote>
<p><span class="star-pagination">*499</span> In that case appellant paid under protest. In these cases also, though petitioners succumbed to compulsion, they preserved their objections, raising them at the earliest possible point. Cf. <i>Abie State Bank</i> v. <i>Bryan,</i> <span class="citation" data-id="101688"><a href="/opinion/101688/abie-state-bank-v-bryan/#776" aria-description="Citation for case: Abie State Bank v. Bryan">282 U. S. 765, 776</a></span>. The cases are therefore quite different from the situation where one who is anxious to make a clean breast of the whole affair volunteers the information.</p>
<p>Mr. Justice Holmes in <i>McAuliffe</i> v. <i>New Bedford,</i> <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen">155 Mass. 216</a></span>, <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen">29 N. E. 517</a></span>, stated a dictum on which New Jersey heavily relies:</p>
<blockquote>"The petitioner may have a constitutional right to talk politics, but he has no constitutional right to be a policeman. There are few employments for hire in which the servant does not agree to suspend his constitutional right of free speech, as well as of idleness, by the implied terms of his contract. The servant cannot complain, as he takes the employment on the terms which are offered him. On the same principle, the city may impose any reasonable condition upon holding offices within its control." <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/#220" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen"><i>Id.,</i> at 220</a></span>, <span class="citation" data-id="6424016"><a href="/opinion/6550282/mcauliffe-v-mayor-and-board-of-aldermen/#517" aria-description="Citation for case: McAuliffe v. Mayor and Board of Aldermen">29 N. E., at 517-518</a></span>.</blockquote>
<p>The question in this case, however, is not cognizable in those terms. Our question is whether a State, contrary to the requirement of the Fourteenth Amendment, can use the threat of discharge to secure incriminatory evidence against an employee.</p>
<p>We held in <i>Slochower</i> v. <i>Board of Education,</i> <span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City">350 U. S. 551</a></span>, that a public school teacher could not be discharged merely because he had invoked the Fifth Amendment privilege against self-incrimination when questioned by a congressional committee:</p>
<blockquote>"The privilege against self-incrimination would be reduced to a hollow mockery if its exercise could be taken as equivalent either to a confession of <span class="star-pagination">*500</span> guilt or a conclusive presumption of perjury. . . . The privilege serves to protect the innocent who otherwise might be ensnared by ambiguous circumstances." <span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/#557" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City"><i>Id.,</i> at 557-558</a></span>.</blockquote>
<p>We conclude that policemen, like teachers and lawyers, are not relegated to a watered-down version of constitutional rights.</p>
<p>There are rights of constitutional stature whose exercise a State may not condition by the exaction of a price. Engaging in interstate commerce is one. <i>Western Union Tel. Co.</i> v. <i>Kansas,</i> <span class="citation" data-id="9418165"><a href="/opinion/97150/western-union-telegraph-co-v-kansas-ex-rel-coleman/" aria-description="Citation for case: Western Union Telegraph Co. v. Kansas Ex Rel. Coleman">216 U. S. 1</a></span>. Resort to the federal courts in diversity of citizenship cases is another. <i>Terral</i> v. <i>Burke Constr. Co.,</i> <span class="citation" data-id="99901"><a href="/opinion/99901/terral-v-burke-construction-co/" aria-description="Citation for case: Terral v. Burke Construction Co.">257 U. S. 529</a></span>. Assertion of a First Amendment right is still another. <i>Lovell</i> v. <i>City of Griffin,</i> <span class="citation" data-id="102991"><a href="/opinion/102991/lovell-v-city-of-griffin/" aria-description="Citation for case: Lovell v. City of Griffin">303 U. S. 444</a></span>; <i>Murdock</i> v. <i>Pennsylvania,</i> <span class="citation" data-id="9419338"><a href="/opinion/103831/murdock-v-pennsylvania/" aria-description="Citation for case: Murdock v. Pennsylvania">319 U. S. 105</a></span>; <i>Thomas</i> v. <i>Collins,</i> <span class="citation" data-id="9419572"><a href="/opinion/104061/thomas-v-collins/" aria-description="Citation for case: Thomas v. Collins">323 U. S. 516</a></span>; <i>Lamont</i> v. <i>Postmaster General,</i> <span class="citation" data-id="9423040"><a href="/opinion/107064/lamont-v-postmaster-general/#305" aria-description="Citation for case: Lamont v. Postmaster General">381 U. S. 301, 305-306</a></span>. The imposition of a burden on the exercise of a Twenty-fourth Amendment right is also banned. <i>Harman</i> v. <i>Forssenius,</i> <span class="citation" data-id="107033"><a href="/opinion/107033/harman-v-forssenius/" aria-description="Citation for case: Harman v. Forssenius">380 U. S. 528</a></span>. We now hold the protection of the individual under the Fourteenth Amendment against coerced statements prohibits use in subsequent criminal proceedings of statements obtained under threat of removal from office, and that it extends to all, whether they are policemen or other members of our body politic.</p>
<p><i>Reversed.</i></p>
<p>[For dissenting opinion of MR. JUSTICE WHITE, see <i>post,</i> p. 530.]</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE CLARK and MR. JUSTICE STEWART join, dissenting.</p>
<p>The majority opinion here and the plurality opinion in <i>Spevack</i> v. <i>Klein</i><i>, post,</i> p. 511, stem from fundamental misconceptions about the logic and necessities of the <span class="star-pagination">*501</span> constitutional privilege against self-incrimination. I fear that these opinions will seriously and quite needlessly hinder the protection of other important public values. I must dissent here, as I do in <i>Spevack.</i></p>
<p>The majority employs a curious mixture of doctrines to invalidate these convictions, and I confess to difficulty in perceiving the intended relationships among the various segments of its opinion. I gather that the majority believes that the possibility that these policemen might have been discharged had they refused to provide information pertinent to their public responsibilities is an impermissible "condition" imposed by New Jersey upon petitioners' privilege against self-incrimination. From this premise the majority draws the conclusion that the statements obtained from petitioners after a warning that discharge was possible were inadmissible. Evidently recognizing the weakness of its conclusion, the majority attempts to bring to its support illustrations from the lengthy series of cases in which this Court, in light of all the relevant circumstances, has adjudged the voluntariness <i>in fact</i> of statements obtained from accused persons.</p>
<p>The majority is apparently engaged in the delicate task of riding two unruly horses at once: it is presumably arguing simultaneously that the statements were involuntary as a matter of fact, in the same fashion that the statements in <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, and <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>, were thought to be involuntary, and that the statements were inadmissible as a matter of law, on the premise that they were products of an impermissible condition imposed on the constitutional privilege. These are very different contentions and require separate replies, but in my opinion both contentions are plainly mistaken, for reasons that follow.</p>
<p></p>
<h2>
<span class="star-pagination">*502</span> I.</h2>
<p>I turn first to the suggestion that these statements were involuntary in fact. An assessment of the voluntariness of the various statements in issue here requires a more comprehensive examination of the pertinent circumstances than the majority has undertaken.</p>
<p>The petitioners were at all material times policemen in the boroughs of Bellmawr and Barrington, New Jersey. Garrity was Bellmawr's chief of police and Virtue one of its police officers; Holroyd, Elwell, and Murray were police officers in Barrington. Another defendant below, Mrs. Naglee, the clerk of Bellmawr's municipal court, has since died. In June 1961 the New Jersey Supreme Court <i>sua sponte</i> directed the State's Attorney General to investigate reports of traffic ticket fixing in Bellmawr and Barrington. Subsequent investigations produced evidence that the petitioners, in separate conspiracies, had falsified municipal court records, altered traffic tickets, and diverted moneys produced from bail and fines to unauthorized purposes. In the course of these investigations the State obtained two sworn statements from each of the petitioners; portions of those statements were admitted at trial. The petitioners were convicted in two separate trials of conspiracy to obstruct the proper administration of the state motor traffic laws, the cases being now consolidated for purposes of our review. The Supreme Court of New Jersey affirmed all the convictions.</p>
<p>The first statements were taken from the petitioners by the State's Deputy Attorney General in August and November 1961. All of the usual indicia of duress are wholly absent. As the state court noted, there was "no physical coercion, no overbearing tactics of psychological persuasion, no lengthy incommunicado detention, or efforts to humiliate or ridicule the defendants." 44 N. J. <span class="star-pagination">*503</span> 209, 220, <span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/#695" aria-description="Citation for case: State v. Naglee">207 A. 2d 689, 695</a></span>. The state court found no evidence that any of the petitioners were reluctant to offer statements, and concluded that the interrogations were conducted with a "high degree of civility and restraint." <i><span class="citation" data-id="2402426"><a href="/opinion/2402426/state-v-naglee/" aria-description="Citation for case: State v. Naglee">Ibid.</a></span></i></p>
<p>These conclusions are fully substantiated by the record. The statements of the Bellmawr petitioners were taken in a room in the local firehouse, for which Chief Garrity himself had made arrangements. None of the petitioners were in custody before or after the depositions were taken; each apparently continued to pursue his ordinary duties as a public official of the community. The statements were recorded by a court stenographer, who testified that he witnessed no indications of unwillingness or even significant hesitation on the part of any of the petitioners. The Bellmawr petitioners did not have counsel present, but the Deputy Attorney General testified without contradiction that Garrity had informed him as they strolled between Garrity's office and the firehouse that he had arranged for counsel, but thought that none would be required at that stage. The interrogations were not excessively lengthy, and reasonable efforts were made to assure the physical comfort of the witnesses. Mrs. Naglee, the clerk of the Bellmawr municipal court, who was known to suffer from a heart ailment, was assured that questioning would cease if she felt any discomfort.</p>
<p>The circumstances in which the depositions of the Barrington petitioners were taken are less certain, for the New Jersey Supreme Court found that there was an informal agreement at the Barrington trial that the defendants would argue simply that the possibility of dismissal made the statements "involuntary as a matter of law." The defense did not contend that the statements were the result of physical or mental coercion, or that the wills of the Barrington petitioners were overborne. Accordingly, the State was never obliged to offer evidence <span class="star-pagination">*504</span> of the voluntariness in fact of the statements. We are, however, informed that the three Barrington petitioners had counsel present as their depositions were taken. Insofar as the majority suggests that the Barrington statements are involuntary in fact, in the fashion of <i><span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">Chambers</a></span></i> or <i><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">Haynes</a></span>,</i> it has introduced a factual contention never urged by the Barrington petitioners and never considered by the courts of New Jersey.</p>
<p>As interrogation commenced, each of the petitioners was sworn, carefully informed that he need not give any information, reminded that any information given might be used in a subsequent criminal prosecution, and warned that as a police officer he was subject to a proceeding to discharge him if he failed to provide information relevant to his public responsibilities. The cautionary statements varied slightly, but all, except that given to Mrs. Naglee, included each of the three warnings.<sup>[1]</sup> Mrs. Naglee was <span class="star-pagination">*505</span> not told that she could be removed from her position at the court if she failed to give information pertinent to the discharge of her duties. All of the petitioners consented to give statements, none displayed any significant hesitation, and none suggested that the decision to offer information was motivated by the possibility of discharge.</p>
<p>A second statement was obtained from each of the petitioners in September and December 1962. These statements were not materially different in content or circumstances from the first. The only significant distinction was that the interrogator did not advert even obliquely to any possibility of dismissal. All the petitioners were cautioned that they were entitled to remain silent, and there was no evidence whatever of physical or mental coercion.</p>
<p>All of the petitioners testified at trial, and gave evidence essentially consistent with the statements taken from them. At a preliminary hearing conducted at the Bellmawr trial to determine the voluntariness of the statements, the Bellmawr petitioners offered no evidence beyond proof of the warning given them.</p>
<p>The standards employed by the Court to assess the voluntariness of an accused's statements have reflected a number of values, and thus have emphasized a variety of factual criteria. The criteria employed have included threats of imminent danger, <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>, physical deprivations, <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/" aria-description="Citation for case: Reck v. Pate">367 U. S. 433</a></span>, repeated or extended interrogation, <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227</a></span>, limits on access to counsel or friends, <i>Crooker</i> v. <i>California,</i> <span class="citation" data-id="9421688"><a href="/opinion/105745/crooker-v-california/" aria-description="Citation for case: Crooker v. California">357 U. S. 433</a></span>, length and illegality of detention under state law, <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>, individual weakness or incapacity, <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span>, and the adequacy of warnings of constitutional rights, <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737</a></span>. Whatever the criteria employed, the duty of the Court has been "to examine the entire <span class="star-pagination">*506</span> record," and thereby to determine whether the accused's will "was overborne by the sustained pressures upon him." <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741, 739</a></span>.</p>
<p>It would be difficult to imagine interrogations to which these criteria of duress were more completely inapplicable, or in which the requirements which have subsequently been imposed by this Court on police questioning were more thoroughly satisfied. Each of the petitioners received a complete and explicit reminder of his constitutional privilege. Three of the petitioners had counsel present; at least a fourth had consulted counsel but freely determined that his presence was unnecessary. These petitioners were not in any fashion "swept from familiar surroundings into police custody, surrounded by antagonistic forces, and subjected to the techniques of persuasion . . . ." <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 461</a></span>. I think it manifest that, under the standards developed by this Court to assess voluntariness, there is no basis for saying that any of these statements were made involuntarily.</p>
<p></p>
<h2>II.</h2>
<p>The issue remaining is whether the statements were inadmissible because they were "involuntary as a matter of law," in that they were given after a warning that New Jersey policemen may be discharged for failure to provide information pertinent to their public responsibilities. What is really involved on this score, however, is not in truth a question of "voluntariness" at all, but rather whether the condition imposed by the State on the exercise of the privilege against self-incrimination, namely dismissal from office, in this instance serves in itself to render the statements inadmissible. Absent evidence of involuntariness in fact, the admissibility of these statements thus hinges on the validity of the consequence which the State acknowledged might have resulted if the statements had not been given. If the consequence is <span class="star-pagination">*507</span> constitutionally permissible, there can surely be no objection if the State cautions the witness that it may follow if he remains silent. If both the consequence and the warning are constitutionally permissible, a witness is obliged, in order to prevent the use of his statements against him in a criminal prosecution, to prove under the standards established since <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>, that as a matter of fact the statements were involuntarily made. The central issues here are therefore identical to those presented in <i>Spevack</i> v. <i>Klein, supra</i><i>:</i> whether consequences may properly be permitted to result to a claimant after his invocation of the constitutional privilege, and if so, whether the consequence in question is permissible. For reasons which I have stated in <i>Spevack</i> v. <i>Klein</i><i>,</i> in my view nothing in the logic or purposes of the privilege demands that all consequences which may result from a witness' silence be forbidden merely because that silence is privileged. The validity of a consequence depends both upon the hazards, if any, it presents to the integrity of the privilege and upon the urgency of the public interests it is designed to protect.</p>
<p>It can hardly be denied that New Jersey is permitted by the Constitution to establish reasonable qualifications and standards of conduct for its public employees. Nor can it be said that it is arbitrary or unreasonable for New Jersey to insist that its employees furnish the appropriate authorities with information pertinent to their employment. Cf. <i>Beilan</i> v. <i>Board of Education,</i> <span class="citation" data-id="9421681"><a href="/opinion/105743/beilan-v-board-of-public-ed-school-dist-of-philadelphia/" aria-description="Citation for case: Beilan v. Board of Public Ed., School Dist. of Philadelphia">357 U. S. 399</a></span>; <i>Slochower</i> v. <i>Board of Education,</i> <span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City">350 U. S. 551</a></span>. Finally, it is surely plain that New Jersey may in particular require its employees to assist in the prevention and detection of unlawful activities by officers of the state government. The urgency of these requirements is the more obvious here, where the conduct in question is that of officials directly entrusted with the administration of justice. The importance for our systems of justice <span class="star-pagination">*508</span> of the integrity of local police forces can scarcely be exaggerated. Thus, it need only be recalled that this Court itself has often intervened in state criminal prosecutions precisely on the ground that this might encourage high standards of police behavior. See, <i>e. g., </i><i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra</a></span></i><i>.</i> It must be concluded, therefore, that the sanction at issue here is reasonably calculated to serve the most basic interests of the citizens of New Jersey.</p>
<p>The final question is the hazard, if any, which this sanction presents to the constitutional privilege. The purposes for which, and the circumstances in which, an officer's discharge might be ordered under New Jersey law plainly may vary. It is of course possible that discharge might in a given case be predicated on an imputation of guilt drawn from the use of the privilege, as was thought by this Court to have occurred in <i>Slochower</i> v. <i>Board of Education, supra</i><i>.</i> But from our vantage point, it would be quite improper to assume that New Jersey will employ these procedures for purposes other than to assess in good faith an employee's continued fitness for public employment. This Court, when a state procedure for investigating the loyalty and fitness of public employees might result either in the <i><span class="citation" data-id="9421254"><a href="/opinion/105377/slochower-v-board-of-higher-ed-of-new-york-city/" aria-description="Citation for case: Slochower v. Board of Higher Ed. of New York City">Slochower</a></span></i> situation or in an assessment in good faith of an employee, has until today consistently paused to examine the actual circumstances of each case. <i>Beilan</i> v. <i>Board of Education, supra</i><i>; </i><i>Nelson</i> v. <i>Los Angeles County,</i> <span class="citation" data-id="9421934"><a href="/opinion/106007/nelson-v-county-of-los-angeles/" aria-description="Citation for case: Nelson v. County of Los Angeles">362 U. S. 1</a></span>. I am unable to see any justification for the majority's abandonment of that process; it is well calculated both to protect the essential purposes of the privilege and to guarantee the most generous opportunities for the pursuit of other public values. The majority's broad prohibition, on the other hand, extends the scope of the privilege beyond its essential purposes, and seriously hampers the protection of other important values. Despite the majority's <span class="star-pagination">*509</span> disclaimer, it is quite plain that the logic of its prohibitory rule would in this situation prevent the discharge of these policemen. It would therefore entirely forbid a sanction which presents, at least on its face, no hazard to the purposes of the constitutional privilege, and which may reasonably be expected to serve important public interests. We are not entitled to assume that discharges will be used either to vindicate impermissible inferences of guilt or to penalize privileged silence, but must instead presume that this procedure is only intended and will only be used to establish and enforce standards of conduct for public employees.<sup>[2]</sup> As such, it does not minimize or endanger the petitioners' constitutional privilege against self-incrimination.<sup>[3]</sup></p>
<p><span class="star-pagination">*510</span> I would therefore conclude that the sanction provided by the State is constitutionally permissible. From this, it surely follows that the warning given of the possibility of discharge is constitutionally unobjectionable. Given the constitutionality both of the sanction and of the warning of its application, the petitioners would be constitutionally entitled to exclude the use of their statements as evidence in a criminal prosecution against them only if it is found that the statements were, when given, involuntary in fact. For the reasons stated above, I cannot agree that these statements were involuntary in fact.</p>
<p>I would affirm the judgments of the Supreme Court of New Jersey.</p>
<h2>NOTES</h2>
<p>[1]  "Any person holding or who has held any elective or appointive public office, position or employment (whether state, county or municipal), who refuses to testify upon matters relating to the office, position or employment in any criminal proceeding wherein he is a defendant or is called as a witness on behalf of the prosecution, upon the ground that his answer may tend to incriminate him or compel him to be a witness against himself or refuses to waive immunity when called by a grand jury to testify thereon or who willfully refuses or fails to appear before any court, commission or body of this state which has the right to inquire under oath upon matters relating to the office, position or employment of such person or who, having been sworn, refuses to testify or to answer any material question upon the ground that his answer may tend to incriminate him or compel him to be a witness against himself, shall, if holding elective or public office, position or employment, be removed therefrom or shall thereby forfeit his office, position or employment and any vested or future right of tenure or pension granted to him by any law of this state provided the inquiry relates to a matter which occurred or arose within the preceding five years. Any person so forfeiting his office, position or employment shall not thereafter be eligible for election or appointment to any public office, position or employment in this state." N. J. Rev. Stat. § 2A:81-17.1 (Supp. 1965).</p>
<p>[2]  At the trial the court excused the jury and conducted a hearing to determine whether, <i>inter alia,</i> the statements were voluntary. The State offered witnesses who testified as to the manner in which the statements were taken; the appellants did not testify at that hearing. The court held the statements to be voluntary.</p>
<p>[3]  N. 1, <i>supra.</i></p>
<p>[4]  <i>Stevens</i> v. <i>Marks,</i> <span class="citation" data-id="9423156"><a href="/opinion/107173/stevens-v-marks/#243" aria-description="Citation for case: Stevens v. Marks">383 U. S. 234, 243</a></span>, quoting from <i>Frost Trucking Co.</i> v. <i>Railroad Comm'n,</i> <span class="citation" data-id="9418562"><a href="/opinion/100914/frost-frost-trucking-co-v-railroad-commn-of-cal/#593" aria-description="Citation for case: Frost &amp; Frost Trucking Co. v. Railroad Comm&#x27;n of Cal.">271 U. S. 583, 593</a></span>.</p>
<p>[5]  Cf. Lamm, The 5th Amendment and Its Equivalent in Jewish Law, 17 Decalogue Jour. 1 (Jan.-Feb. 1967):
</p>
<p>"It should be pointed out, at the very outset, that the Halakhah does not distinguish between voluntary and forced confessions, for reasons which will be discussed later. And it is here that one of the basic differences between Constitutional and Talmudic Law arises. According to the Constitution, a man cannot be compelled to testify against himself. The provision against self-incrimination is a privilege of which a citizen may or may not avail himself, as he wishes. The Halakhah, however, does not permit self-incriminating testimony. It is inadmissible, even if voluntarily offered. Confession, in other than a religious context, or financial cases completely free from any traces of criminality, is simply not an instrument of the Law. The issue, then, is not compulsion, but the whole idea of legal confession.</p>
<p>.....</p>
<p>"The Halakhah, then, is obviously concerned with protecting the confessant from his own aberrations which manifest themselves, either as completely fabricated confessions, or as exaggerations of the real facts. . . . While certainly not all, or even most criminal confessions are directly attributable, in whole or part, to the Death Instinct, the Halakhah is sufficiently concerned with the minority of instances, where such is the case, to disqualify all criminal confessions and to discard confession as a legal instrument. Its function is to ensure the total victory of the Life Instinct over its omnipresent antagonist. Such are the conclusions to be drawn from Maimonides' interpretation of the Halakhah's equivalent of the Fifth Amendment.</p>
<p>"In summary, therefore, the Constitutional ruling on self-incrimination concerns only forced confessions, and its restricted character is a result of its historical evolution as a civilized protest against the use of torture in extorting confessions. The Halakhie ruling, however, is much broader and discards confessions in toto, and this because of its psychological insight and its concern for saving man from his own destructive inclinations." <i>Id.,</i> at 10, 12.</p>
<p>[1]  The warning given to Chief Garrity is typical. "I want to advise you that anything you say must be said of your own free will and accord without any threats or promises or coercion, and anything you say may be, of course, used against you or any other person in any subsequent criminal proceedings in the courts of our state.
</p>
<p>"You do have, under our law, as you probably know, a privilege to refuse to make any disclosure which may tend to incriminate you. If you make a disclosure with knowledge of this right or privilege, voluntarily, you thereby waive that right or privilege in relation to any other questions which I might put to you relevant to such disclosure in this investigation.</p>
<p>"This right or privilege which you have is somewhat limited to the extent that you as a police officer under the laws of our state, may be subjected to a proceeding to have you removed from office if you refuse to answer a question put to you under oath pertaining to your office or your function within that office. It doesn't mean, however, you can't exercise the right. You do have the right."</p>
<p>A. "No, I will cooperate."</p>
<p>Q. "Understanding this, are you willing to proceed at this time and answer any questions?"</p>
<p>A. "Yes."</p>
<p>[2]  The legislative history of N. J. Rev. Stat. 2A:81-17.1 provides nothing which clearly indicates the purposes of the statute, beyond what is to be inferred from its face. In any event, the New Jersey Supreme Court noted below that the State would be entitled, even without the statutory authorization, to discharge state employees who declined to provide information relevant to their official responsibilities. There is therefore nothing to which this Court could properly now look to forecast the purposes for which or circumstances in which New Jersey might discharge those who have invoked the constitutional privilege.</p>
<p>[3]  The late Judge Jerome Frank thus once noted, in the course of a spirited defense of the privilege, that it would be entirely permissible to discharge police officers who decline, on grounds of the privilege, to disclose information pertinent to their public responsibilities. Judge Frank quoted the following with approval:
</p>
<p>" `<i>Duty required them to answer. Privilege permitted them to refuse to answer. They chose to exercise the privilege, but the exercise of such privilege was wholly inconsistent with their duty as police officers.</i> They claim that they had a constitutional right to refuse to answer under the circumstances, but . . . <i>they had no constitutional right to remain police officers</i> in the face of their clear violation of the duty imposed upon them.' Christal v. Police Commission of San Francisco." Citing <span class="citation" data-id="1400422"><a href="/opinion/1400422/christal-v-police-commission/" aria-description="Citation for case: Christal v. Police Commission">33 Cal. App. 2d 564</a></span>, <span class="citation" data-id="1400422"><a href="/opinion/1400422/christal-v-police-commission/" aria-description="Citation for case: Christal v. Police Commission">92 P. 2d 416</a></span>. (Emphasis added by Judge Frank.) <i>United States</i> v. <i>Field,</i> <span class="citation" data-id="9443042"><a href="/opinion/228335/united-states-v-field/#106" aria-description="Citation for case: United States v. Field">193 F. 2d 92, 106</a></span> (separate opinion).</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Georgia v. Randolph.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Georgia v. Randolph"
type: case
citation: "547 U.S. 103 (2006)"
parallel_cite: "126 S. Ct. 1515; 164 L. Ed. 2d 208"
neutral_cite: 2006 U.S. LEXIS 2498
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2006
date_decided: 2006-03-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2006-03-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Georgia v. Randolph
  varies_by_point: false
  scope_note: "Confined to a physically present objector by Fernandez v. California (2014)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145669/georgia-v-randolph/"
  cluster_id: 145669
  opinion_id: 145669
  identity_checked: true
homes:
  - page: "[[Consent Searches]]"
    role: "Key — Anchor"
related: ["[[Fernandez v. California]]", "[[Illinois v. Rodriguez]]", "[[United States v. Matlock]]"]
aliases: []
tags: ["case", "fourth-amendment", "consent", "co-occupant", "third-party-consent", "present-objector"]
holding: "A PHYSICALLY PRESENT co-occupant's express refusal to consent prevails over another occupant's consent, rendering the warrantless search…"
lake:
  record_id: Georgia v. Randolph
  status: verified
  projected_at: 2026-07-06
---

# Georgia v. Randolph

*547 U.S. 103 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Scott Randolph's estranged wife told police that he used cocaine and that there was drug evidence in their home. When officers asked Randolph for consent to search, he expressly refused; his wife, present at the scene, then consented and led the officers to the evidence. Randolph moved to suppress, arguing that his present, express refusal made the search unreasonable as to him.

## Issue
Whether one occupant's consent to a warrantless search of a shared home is valid against a co-occupant who is physically present and expressly refuses consent.

## Rule
No. A physically present co-occupant's express refusal defeats another occupant's consent. "We therefore hold that a warrantless search of a shared dwelling for evidence over the express refusal of consent by a physically present resident cannot be justified as reasonable as to him on the basis of consent given to the police by another resident." — 547 U.S. at 120. ^pin-120

## Application
Randolph stood at the door and expressly told the officers they could not search, and only then did his wife consent. Because Randolph was physically present and expressly refused, his co-tenant's consent could not make the search reasonable as to him, and the evidence found in the home had to be suppressed.

## Conclusion
The warrantless search was unreasonable as to the present, objecting co-occupant; the suppression was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Confined to a physically present objector** by [[Fernandez v. California]]: once the objecting occupant is lawfully removed (e.g., by arrest), the remaining occupant's consent again controls. *Randolph*'s core present-objector rule is otherwise undisturbed.

## Appears on
- [[Consent Searches]] — *Key — Anchor*

## Sources
- *Georgia v. Randolph*, 547 U.S. 103 (2006) — https://www.courtlistener.com/opinion/145669/georgia-v-randolph/ — pinpoint: 120.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "409d9ddd6fc2470b", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Georgia v. Randolph"}, "payload": {"all": [{"cite": "547 U.S. 103", "page": "103", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "547"}, {"cite": "126 S. Ct. 1515", "page": "1515", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "126"}, {"cite": "164 L. Ed. 2d 208", "page": "208", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "164"}, {"cite": "2006 U.S. LEXIS 2498", "page": "2498", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2006"}], "display": "547 U.S. 103", "official": {"cite": "547 U.S. 103", "page": "103", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "547"}, "official_selection_present": true, "record_id": "Georgia v. Randolph"}}
{"assertion_id": "bafaead73dedc487", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-120", "record_id": "Georgia v. Randolph"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-120", "pinpoint_status": "slip-only", "quote": "--- # Georgia v. Randolph *547 U.S. 103 (2006)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Scott Randolph's estranged wife told police that he used cocaine and that there was drug evidence in their home. When officers asked Randolph for consent to search, he expressly refused; his wife, present at the scene, then consented and led the officers to the evidence. Randolph moved to suppress, arguing that his present, express refusal made the search unreasonable as to him. ## Issue Whether one occupant's consent to a warrantless search of a shared home is valid against a co-occupant who is physically present and expressly refuses consent. ## Rule No. A physically present co-occupant's express refusal defeats another occupant's consent.", "quote_fidelity": "mismatch", "record_id": "Georgia v. Randolph", "star_marker": null}}
{"assertion_id": "50965a191184c99f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Georgia v. Randolph"}, "payload": {"as_of_content": "2006-03-22", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Georgia v. Randolph", "scope_note": "Confined to a physically present objector by Fernandez v. California (2014).", "varies_by_point": false}}
```

### lake record — Georgia v. Randolph

```json
{
  "schema_version": "s2.v1",
  "record_id": "Georgia v. Randolph",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Georgia v. Randolph",
    "case_name_short": "Randolph",
    "case_name_full": "Georgia v. Randolph",
    "input_case_name": "Georgia v. Randolph",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2006-03-22",
    "year": 2006,
    "docket": null,
    "cluster_id": 145669,
    "lead_opinion_id": 145669,
    "sibling_ids": [
      145669,
      9434962,
      9434963,
      9434964,
      9434965,
      9434966,
      9434967
    ],
    "absolute_url": "/opinion/145669/georgia-v-randolph/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "547 U.S. 103",
      "volume": "547",
      "reporter": "U.S.",
      "page": "103",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "126 S. Ct. 1515",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 208",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "208",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2006 U.S. LEXIS 2498",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2498",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "547 U.S. 103",
        "volume": "547",
        "reporter": "U.S.",
        "page": "103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "126 S. Ct. 1515",
        "volume": "126",
        "reporter": "S. Ct.",
        "page": "1515",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "164 L. Ed. 2d 208",
        "volume": "164",
        "reporter": "L. Ed. 2d",
        "page": "208",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2006 U.S. LEXIS 2498",
        "volume": "2006",
        "reporter": "U.S. LEXIS",
        "page": "2498",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "547 U.S. 103",
    "official_selection": {
      "court_class": "scotus",
      "selected": "547 U.S. 103",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-120",
      "page": null,
      "quote": "--- # Georgia v. Randolph *547 U.S. 103 (2006)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Scott Randolph's estranged wife told police that he used cocaine and that there was drug evidence in their home. When officers asked Randolph for consent to search, he expressly refused; his wife, present at the scene, then consented and led the officers to the evidence. Randolph moved to suppress, arguing that his present, express refusal made the search unreasonable as to him. ## Issue Whether one occupant's consent to a warrantless search of a shared home is valid against a co-occupant who is physically present and expressly refuses consent. ## Rule No. A physically present co-occupant's express refusal defeats another occupant's consent.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2006-03-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Georgia v. Randolph",
    "varies_by_point": false,
    "scope_note": "Confined to a physically present objector by Fernandez v. California (2014).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. White",
          "cluster_id": 4396241,
          "cite": [
            "799 S.E.2d 494",
            "293 Va. 411",
            "2017 WL 2376924",
            "2017 Va. LEXIS 78"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
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
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Rush",
          "cluster_id": 3164356,
          "cite": [
            "808 F.3d 1007",
            "2015 U.S. App. LEXIS 22212",
            "2015 WL 9269763"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Timmie Bradley v. State of Indiana",
          "cluster_id": 2950910,
          "cite": [
            "44 N.E.3d 7",
            "2015 Ind. App. LEXIS 631",
            "2015 WL 5438394"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
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
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Bodie Witzlib",
          "cluster_id": 2825238,
          "cite": [
            "796 F.3d 799",
            "2015 U.S. App. LEXIS 13811",
            "2015 WL 4664340"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
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
        "journal_ref": "Georgia v. Randolph:lane1_negative"
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
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States of America v. Frederick Drane",
          "cluster_id": 10697016,
          "cite": [
            "2014 DNH 150"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fadul",
          "cluster_id": 7306139,
          "cite": [
            "16 F. Supp. 3d 270",
            "2014 WL 1584044"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "MacDonald v. Town of Eastham",
          "cluster_id": 2656464,
          "cite": [
            "745 F.3d 8",
            "2014 WL 944707",
            "2014 U.S. App. LEXIS 4618"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Adams",
          "cluster_id": 2648986,
          "cite": [
            "740 F.3d 40",
            "2014 U.S. App. LEXIS 631",
            "113 A.F.T.R.2d (RIA) 522",
            "2014 WL 112937"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Omar Arreguin",
          "cluster_id": 2643845,
          "cite": [
            "735 F.3d 1168",
            "2013 U.S. App. LEXIS 23506"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. McNeely",
          "cluster_id": 858288,
          "cite": [
            "185 L. Ed. 2d 696",
            "133 S. Ct. 1552",
            "569 U.S. 141",
            "2013 U.S. LEXIS 3160",
            "81 U.S.L.W. 4250",
            "24 Fla. L. Weekly Fed. S 150",
            "2013 WL 1628934"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 2599941,
          "cite": [
            "140 P.3d 657",
            "47 Cal. Rptr. 3d 326",
            "39 Cal. 4th 641",
            "2006 Daily Journal DAR 10936",
            "2006 Cal. LEXIS 9521"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Stone",
          "cluster_id": 4958214,
          "cite": [
            "2021 COA 104"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cortez v. McCauley",
          "cluster_id": 167088,
          "cite": [
            "478 F.3d 1108",
            "2007 WL 503819"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 1670023,
          "cite": [
            "755 N.W.2d 664",
            "279 Mich. App. 116"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Safford Unified School District 1 v. Redding",
          "cluster_id": 145852,
          "cite": [
            "174 L. Ed. 2d 354",
            "129 S. Ct. 2633",
            "557 U.S. 364",
            "2009 U.S. LEXIS 4735",
            "21 Fla. L. Weekly Fed. S 1011",
            "77 U.S.L.W. 4591"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gates v. Texas Deparment of Protective & Regulatory Services",
          "cluster_id": 62905,
          "cite": [
            "537 F.3d 404",
            "2008 WL 2875378"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Shover",
          "cluster_id": 2635828,
          "cite": [
            "217 P.3d 901",
            "2009 Colo. App. LEXIS 212",
            "2009 WL 399727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Luna v. State",
          "cluster_id": 1488102,
          "cite": [
            "268 S.W.3d 594",
            "2008 Tex. Crim. App. LEXIS 1672",
            "2008 WL 4724087"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Villarreal, David",
          "cluster_id": 2948963,
          "cite": [
            "475 S.W.3d 784",
            "2014 Tex. Crim. App. LEXIS 1898",
            "2014 WL 6734178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. McKnight",
          "cluster_id": 4621444,
          "cite": [
            "2019 CO 36",
            "446 P.3d 397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Meekins v. State",
          "cluster_id": 2544137,
          "cite": [
            "340 S.W.3d 454",
            "2011 Tex. Crim. App. LEXIS 592",
            "2011 WL 1663151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fernandez v. California",
          "cluster_id": 2654534,
          "cite": [
            "188 L. Ed. 2d 25",
            "134 S. Ct. 1126",
            "2014 U.S. LEXIS 1636",
            "82 U.S.L.W. 4102",
            "571 U.S. 292",
            "24 Fla. L. Weekly Fed. S 553",
            "2014 WL 700100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez",
          "cluster_id": 2380403,
          "cite": [
            "240 P.3d 448",
            "2010 Colo. App. LEXIS 213",
            "2010 WL 547625"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas McClish v. Richard B. Nugent",
          "cluster_id": 77659,
          "cite": [
            "483 F.3d 1231",
            "2007 U.S. App. LEXIS 8294",
            "2007 WL 1063337"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
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
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ryburn v. Huff",
          "cluster_id": 622303,
          "cite": [
            "181 L. Ed. 2d 966",
            "132 S. Ct. 987",
            "565 U.S. 469",
            "2012 U.S. LEXIS 910"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Karen Fitzgerald v. M. Santoro",
          "cluster_id": 819861,
          "cite": [
            "707 F.3d 725",
            "2013 WL 452446",
            "2013 U.S. App. LEXIS 2600"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wilson",
          "cluster_id": 147086,
          "cite": [
            "605 F.3d 985",
            "390 U.S. App. D.C. 368",
            "82 Fed. R. Serv. 940",
            "2010 U.S. App. LEXIS 10558",
            "2010 WL 2036304"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glenn v. Com.",
          "cluster_id": 1058555,
          "cite": [
            "654 S.E.2d 910",
            "275 Va. 123",
            "2008 Va. LEXIS 16"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Georgia v. Randolph:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzcxNjg2NDAwMDAwJnM9OTA0NTQ2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145669+OR+9434962+OR+9434963+OR+9434964+OR+9434965+OR+9434966+OR+9434967%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 13,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 13,
        "triage_snippet_classified": 187
      },
      "lane2_top_cited": {
        "query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OCZzPTI2NzQ4NDEmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145669+OR+9434962+OR+9434963+OR+9434964+OR+9434965+OR+9434966+OR+9434967%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967)",
        "reviewed": 40,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 40,
        "triage_read": 0,
        "triage_snippet_classified": 40
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145669 OR 9434962 OR 9434963 OR 9434964 OR 9434965 OR 9434966 OR 9434967)",
    "indexed_citing_opinions": 692,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145669,
        "count": 583,
        "count_source": "search"
      },
      {
        "opinion_id": 9434962,
        "count": 123,
        "count_source": "search"
      },
      {
        "opinion_id": 9434963,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434964,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434965,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434966,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434967,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1204,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/georgia-v-randolph.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4NjY4Njgmcz0xMDYwMDA0NiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145669+OR+9434962+OR+9434963+OR+9434964+OR+9434965+OR+9434966+OR+9434967%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145669,
        "cited_id": 99820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 105731,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 106197,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 106990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 109433,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110212,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110314,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 111257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112416,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118226,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 118443,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 162237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 197429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 272739,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 299112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 351740,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 364861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 552251,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 702612,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 799991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1147536,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1211487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1298391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1366935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 1449748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145669,
        "cited_id": 3878196,
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
    "date_created": "2026-07-05T05:18:41Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:22:22Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:18:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Georgia v. Randolph

```
(Slip Opinion)              OCTOBER TERM, 2005                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                        GEORGIA v. RANDOLPH

        CERTIORARI TO THE SUPREME COURT OF GEORGIA

  No. 04–1067. Argued November 8, 2005—Decided March 22, 2006
Respondent’s estranged wife gave police permission to search the mari-
  tal residence for items of drug use after respondent, who was also
  present, had unequivocally refused to give consent. Respondent was
  indicted for possession of cocaine, and the trial court denied his mo-
  tion to suppress the evidence as products of a warrantless search un-
  authorized by consent. The Georgia Court of Appeals reversed. In
  affirming, the State Supreme Court held that consent given by one
  occupant is not valid in the face of the refusal of another physically
  present occupant, and distinguished United States v. Matlock, 415
  U. S. 164, which recognized the permissibility of an entry made with
  the consent of one co-occupant in the other’s absence.
Held: In the circumstances here at issue, a physically present co-
 occupant’s stated refusal to permit entry renders warrantless entry
 and search unreasonable and invalid as to him. Pp. 4–19.
    (a) The Fourth Amendment recognizes a valid warrantless entry
 and search of a premises when the police obtain the voluntary con-
 sent of an occupant who shares, or is reasonably believed to share,
 common authority over the property, and no present co-tenant ob-
 jects. Matlock, supra, at 170; Illinois v. Rodriguez, 497 U. S. 177,
 186. The constant element in assessing Fourth Amendment reason-
 ableness in such cases is the great significance given to widely shared
 social expectations, which are influenced by property law but not con-
 trolled by its rules. Thus, Matlock not only holds that a solitary co-
 inhabitant may sometimes consent to a search of shared premises,
 but also stands for the proposition that the reasonableness of such a
 search is in significant part a function of commonly held understand-
 ings about the authority that co-inhabitants may exercise in ways
 that affect each other’s interests. Pp. 4–6.
    (b) Matlock’s example of common understanding is readily appar-
2                        GEORGIA v. RANDOLPH

                                  Syllabus

    ent. The assumption tenants usually make about their common au-
    thority when they share quarters is that any one of them may admit
    visitors, with the consequence that a guest obnoxious to one may be
    admitted in his absence. Matlock placed no burden on the police to
    eliminate the possibility of atypical arrangements, absent reason to
    doubt that the regular scheme was in place. Pp. 6–8.
       (c) This Court took a step toward addressing the issue here when it
    held in Minnesota v. Olson, 495 U. S. 91, that overnight houseguests
    have a legitimate expectation of privacy in their temporary quarters.
    If that customary expectation is a foundation of a houseguest’s
    Fourth Amendment rights, it should follow that an inhabitant of
    shared premises may claim at least as much. In fact, a co-inhabitant
    naturally has an even stronger claim. No sensible person would en-
    ter shared premises based on one occupant’s invitation when a fellow
    tenant said to stay out. Such reticence would show not timidity but a
    realization that when people living together disagree over the use of
    their common quarters, a resolution must come through voluntary
    accommodation, not by appeals to authority. Absent some recognized
    hierarchy, e.g., parent and child, there is no societal or legal under-
    standing of superior and inferior as between co-tenants. Pp. 8–10.
       (d) Thus, a disputed invitation, without more, gives an officer no
    better claim to reasonableness in entering than the officer would
    have absent any consent. Disputed permission is no match for the
    Fourth Amendment central value of “respect for the privacy of the
    home,” Wilson v. Layne, 526 U. S. 603, 610, and the State’s other
    countervailing claims do not add up to outweigh it.
       A co-tenant who has an interest in bringing criminal activity to
    light or in deflecting suspicion from himself can, e.g., tell the police
    what he knows, for use before a magistrate in getting a warrant.
    This case, which recognizes limits on evidentiary searches, has no
    bearing on the capacity of the police, at the invitation of one tenant,
    to enter a dwelling over another tenant’s objection in order to protect
    a resident from domestic violence. Though alternatives to disputed
    consent will not always open the door to search for evidence that the
    police suspect is inside, nothing in social custom or its reflection in
    private law argues for placing a higher value on delving into private
    premises to search for evidence in the face of disputed consent, than
    on requiring clear justification before the government searches pri-
    vate living quarters over a resident’s objection. Pp. 10–16.
       (e) There are two loose ends. First, while Matlock’s explanation for
    the constitutional sufficiency of a co-tenant’s consent to enter and
    search recognized a co-inhabitant’s “right to permit the inspection in
    his own right,” 415 U. S., at 171, n. 7, the right to admit the police is
    not a right as understood under property law. It is, instead, the au-
                      Cite as: 547 U. S. ____ (2006)                       3

                                 Syllabus

  thority recognized by customary social usage as having a substantial
  bearing on Fourth Amendment reasonableness in specific circum-
  stances. The question here is whether customary social understand-
  ing accords the consenting tenant authority to prevail over the co-
  tenant’s objection, a question Matlock did not answer. Second, a fine
  line must be drawn to avoid undercutting Matlock—where the defen-
  dant, though not present, was in a squad car not far away—and Rod-
  riguez—where the defendant was asleep in the apartment and could
  have been roused by a knock on the door; if a potential defendant
  with self-interest in objecting is in fact at the door and objects, the co-
  tenant’s permission does not suffice for a reasonable search, whereas
  the potential objector, nearby but not part of the threshold colloquy,
  loses out. Such formalism is justified. So long as there is no evidence
  that the police have removed the potentially objecting tenant from
  the entrance specifically to avoid a possible objection, there is practi-
  cal value in the simple clarity of complementary rules, one recogniz-
  ing the co-tenant’s permission when no fellow occupant is on hand,
  the other according dispositive weight to the fellow occupant’s ex-
  pressed contrary indication. Pp. 16–18.
     (f) Here, respondent’s refusal is clear, and nothing in the record
  justifies the search on grounds independent of his wife’s consent.
  Pp. 18–19.
278 Ga. 614, 604 S. E. 2d 835, affirmed.

   SOUTER, J., delivered the opinion of the Court, in which STEVENS,
KENNEDY, GINSBURG, and BREYER, JJ., joined. STEVENS, J., and BREYER,
J., filed concurring opinions. ROBERTS, C. J., filed a dissenting opinion,
in which SCALIA, J., joined. SCALIA, J., and THOMAS, J., filed dissenting
opinions. ALITO, J., took no part in the consideration or decision of the
case.
                       Cite as: 547 U. S. ____ (2006)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash-
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 04–1067
                                  _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                               [March 22, 2006]

   JUSTICE SOUTER delivered the opinion of the Court.
   The Fourth Amendment recognizes a valid warrantless
entry and search of premises when police obtain the vol-
untary consent of an occupant who shares, or is reasona-
bly believed to share, authority over the area in common
with a co-occupant who later objects to the use of evidence
so obtained. Illinois v. Rodriguez, 497 U. S. 177 (1990);
United States v. Matlock, 415 U. S. 164 (1974). The ques-
tion here is whether such an evidentiary seizure is like-
wise lawful with the permission of one occupant when the
other, who later seeks to suppress the evidence, is present
at the scene and expressly refuses to consent. We hold
that, in the circumstances here at issue, a physically
present co-occupant’s stated refusal to permit entry pre-
vails, rendering the warrantless search unreasonable and
invalid as to him.
                            I
  Respondent Scott Randolph and his wife, Janet, sepa-
rated in late May 2001, when she left the marital resi-
dence in Americus, Georgia, and went to stay with her
parents in Canada, taking their son and some belongings.
In July, she returned to the Americus house with the
2                 GEORGIA v. RANDOLPH

                     Opinion of the Court

child, though the record does not reveal whether her object
was reconciliation or retrieval of remaining possessions.
   On the morning of July 6, she complained to the police
that after a domestic dispute her husband took their son
away, and when officers reached the house she told them
that her husband was a cocaine user whose habit had
caused financial troubles. She mentioned the marital
problems and said that she and their son had only recently
returned after a stay of several weeks with her parents.
Shortly after the police arrived, Scott Randolph returned
and explained that he had removed the child to a
neighbor’s house out of concern that his wife might take
the boy out of the country again; he denied cocaine use,
and countered that it was in fact his wife who abused
drugs and alcohol.
   One of the officers, Sergeant Murray, went with Janet
Randolph to reclaim the child, and when they returned
she not only renewed her complaints about her husband’s
drug use, but also volunteered that there were “ ‘items of
drug evidence’ ” in the house. Brief for Petitioner 3. Ser-
geant Murray asked Scott Randolph for permission to
search the house, which he unequivocally refused.
   The sergeant turned to Janet Randolph for consent to
search, which she readily gave. She led the officer up-
stairs to a bedroom that she identified as Scott’s, where
the sergeant noticed a section of a drinking straw with a
powdery residue he suspected was cocaine. He then left
the house to get an evidence bag from his car and to call
the district attorney’s office, which instructed him to stop
the search and apply for a warrant. When Sergeant
Murray returned to the house, Janet Randolph withdrew
her consent. The police took the straw to the police sta-
tion, along with the Randolphs. After getting a search
warrant, they returned to the house and seized further
evidence of drug use, on the basis of which Scott Randolph
was indicted for possession of cocaine.
                  Cite as: 547 U. S. ____ (2006)            3

                      Opinion of the Court

   He moved to suppress the evidence, as products of a
warrantless search of his house unauthorized by his wife’s
consent over his express refusal. The trial court denied
the motion, ruling that Janet Randolph had common
authority to consent to the search.
   The Court of Appeals of Georgia reversed, 264 Ga. App.
396, 590 S. E. 2d 834 (2003), and was itself sustained by
the State Supreme Court, principally on the ground that
“the consent to conduct a warrantless search of a residence
given by one occupant is not valid in the face of the refusal
of another occupant who is physically present at the scene
to permit a warrantless search.” 278 Ga. 614, 604 S. E. 2d
835, 836 (2004). The Supreme Court of Georgia acknowl-
edged this Court’s holding in Matlock, 415 U. S. 164, that
“the consent of one who possesses common authority over
premises or effects is valid as against the absent, noncon-
senting person with whom that authority is shared,” id., at
170, and found Matlock distinguishable just because Scott
Randolph was not “absent” from the colloquy on which the
police relied for consent to make the search. The State
Supreme Court stressed that the officers in Matlock had not
been “faced with the physical presence of joint occupants,
with one consenting to the search and the other objecting.”
278 Ga., at 615, 604 S. E. 2d, at 837. It held that an indi-
vidual who chooses to live with another assumes a risk no
greater than “ ‘an inability to control access to the premises
during [his] absence,’ ” ibid. (quoting 3 W. LaFave, Search
and Seizure §8.3(d), p. 731 (3d ed. 1996) (hereinafter La-
Fave)), and does not contemplate that his objection to a
request to search commonly shared premises, if made, will
be overlooked.
   We granted certiorari to resolve a split of authority on
whether one occupant may give law enforcement effective
consent to search shared premises, as against a co-tenant
4                      GEORGIA v. RANDOLPH

                          Opinion of the Court

who is present and states a refusal to permit the search.1
544 U. S. 973 (2005). We now affirm.
                              II
   To the Fourth Amendment rule ordinarily prohibiting
the warrantless entry of a person’s house as unreasonable
per se, Payton v. New York, 445 U. S. 573, 586 (1980); Coo-
lidge v. New Hampshire, 403 U. S. 443, 454–455 (1971), one
“jealously and carefully drawn” exception, Jones v. United
States, 357 U. S. 493, 499 (1958), recognizes the validity of
searches with the voluntary consent of an individual pos-
sessing authority, Rodriguez, 497 U. S., at 181. That person
might be the householder against whom evidence is sought,
Schneckloth v. Bustamonte, 412 U. S. 218, 222 (1973), or a
fellow occupant who shares common authority over prop-
erty, when the suspect is absent, Matlock, supra, at 170, and
the exception for consent extends even to entries and
searches with the permission of a co-occupant whom the
police reasonably, but erroneously, believe to possess shared
authority as an occupant, Rodriguez, supra, at 186. None of
our co-occupant consent-to-search cases, however, has pre-
sented the further fact of a second occupant physically
present and refusing permission to search, and later moving
to suppress evidence so obtained.2 The significance of such
——————
    1 All
        four Courts of Appeals to have considered this question have
concluded that consent remains effective in the face of an express
objection. See United States v. Morning, 64 F. 3d 531, 533–536 (CA9
1995); United States v. Donlin, 982 F. 2d 31, 33 (CA1 1992); United
States v. Hendrix, 595 F. 2d 883, 885 (CADC 1979) (per curiam); United
States v. Sumlin, 567 F. 2d 684, 687–688 (CA6 1977). Of the state
courts that have addressed the question, the majority have reached
that conclusion as well. See, e.g., Love v. State, 355 Ark. 334, 342, 138
S. W. 3d 676, 680 (2003); Laramie v. Hysong, 808 P. 2d 199, 203–205
(Wyo. 1991); but cf. State v. Leach, 113 Wash. 2d 735, 744, 782 P. 2d
1035, 1040 (1989) (en banc) (requiring consent of all present co-
occupants).
  2 Mindful of the multiplicity of living arrangements, we vary the

terms used to describe residential co-occupancies. In so doing we do not
                    Cite as: 547 U. S. ____ (2006)                  5

                        Opinion of the Court

a refusal turns on the underpinnings of the co-occupant
consent rule, as recognized since Matlock.
                              A
  The defendant in that case was arrested in the yard of a
house where he lived with a Mrs. Graff and several of her
relatives, and was detained in a squad car parked nearby.
When the police went to the door, Mrs. Graff admitted
them and consented to a search of the house. 415 U. S., at
166. In resolving the defendant’s objection to use of the
evidence taken in the warrantless search, we said that
“the consent of one who possesses common authority over
premises or effects is valid as against the absent, noncon-
senting person with whom that authority is shared.” Id.,
at 170. Consistent with our prior understanding that
Fourth Amendment rights are not limited by the law of
property, cf. Katz v. United States, 389 U. S. 347, 352–353
(1967), we explained that the third party’s “common au-
thority” is not synonymous with a technical property
interest:
     “The authority which justified the third-party consent
     does not rest upon the law of property, with its atten-
     dant historical and legal refinement, but rests rather
     on mutual use of the property by persons generally
     having joint access or control for most purposes, so
     that it is reasonable to recognize that any of the co-
     inhabitants has the right to permit the inspection in
     his own right and that the others have assumed the
     risk that one of their number might permit the com-
     mon area to be searched.” 415 U. S., at 171, n. 7 (cita-
     tions omitted).
See also Frazier v. Cupp, 394 U. S. 731, 740 (1969) (“[I]n
allowing [his cousin to share use of a duffel bag] and in
——————
mean, however, to suggest that the rule to be applied to them is simi-
larly varied.
6                  GEORGIA v. RANDOLPH

                      Opinion of the Court

leaving it in his house, [the suspect] must be taken to have
assumed the risk that [the cousin] would allow someone
else to look inside”). The common authority that counts
under the Fourth Amendment may thus be broader than
the rights accorded by property law, see Rodriguez, supra,
at 181–182 (consent is sufficient when given by a person
who reasonably appears to have common authority but
who, in fact, has no property interest in the premises
searched), although its limits, too, reflect specialized
tenancy arrangements apparent to the police, see Chap-
man v. United States, 365 U. S. 610 (1961) (landlord could
not consent to search of tenant’s home).
  The constant element in assessing Fourth Amendment
reasonableness in the consent cases, then, is the great
significance given to widely shared social expectations,
which are naturally enough influenced by the law of prop-
erty, but not controlled by its rules. Cf. Rakas v. Illinois,
439 U. S. 128, 144, n. 12 (1978) (an expectation of privacy is
reasonable if it has “a source outside of the Fourth Amend-
ment, either by reference to concepts of real or personal
property law or to understandings that are recognized and
permitted by society”). Matlock accordingly not only holds
that a solitary co-inhabitant may sometimes consent to a
search of shared premises, but stands for the proposition
that the reasonableness of such a search is in significant
part a function of commonly held understanding about the
authority that co-inhabitants may exercise in ways that
affect each other’s interests.
                               B
  Matlock’s example of common understanding is readily
apparent. When someone comes to the door of a domestic
dwelling with a baby at her hip, as Mrs. Graff did, she
shows that she belongs there, and that fact standing alone
is enough to tell a law enforcement officer or any other
visitor that if she occupies the place along with others, she
                 Cite as: 547 U. S. ____ (2006)            7

                     Opinion of the Court

probably lives there subject to the assumption tenants
usually make about their common authority when they
share quarters. They understand that any one of them
may admit visitors, with the consequence that a guest
obnoxious to one may nevertheless be admitted in his
absence by another. As Matlock put it, shared tenancy is
understood to include an “assumption of risk,” on which
police officers are entitled to rely, and although some
group living together might make an exceptional ar-
rangement that no one could admit a guest without the
agreement of all, the chance of such an eccentric scheme is
too remote to expect visitors to investigate a particular
household’s rules before accepting an invitation to come
in. So, Matlock relied on what was usual and placed no
burden on the police to eliminate the possibility of atypical
arrangements, in the absence of reason to doubt that the
regular scheme was in place.
  It is also easy to imagine different facts on which, if
known, no common authority could sensibly be suspected.
A person on the scene who identifies himself, say, as a
landlord or a hotel manager calls up no customary under-
standing of authority to admit guests without the consent
of the current occupant. See Chapman v. United States,
supra (landlord); Stoner v. California, 376 U. S. 483 (1964)
(hotel manager). A tenant in the ordinary course does not
take rented premises subject to any formal or informal
agreement that the landlord may let visitors into the
dwelling, Chapman, supra, at 617, and a hotel guest cus-
tomarily has no reason to expect the manager to allow
anyone but his own employees into his room, see Stoner,
supra, at 489; see also United States v. Jeffers, 342 U. S.
48, 51 (1951) (hotel staff had access to room for purposes
of cleaning and maintenance, but no authority to admit
police). In these circumstances, neither state-law property
rights, nor common contractual arrangements, nor any
other source points to a common understanding of author-
8                  GEORGIA v. RANDOLPH

                     Opinion of the Court

ity to admit third parties generally without the consent of
a person occupying the premises. And when it comes to
searching through bureau drawers, there will be instances
in which even a person clearly belonging on premises as
an occupant may lack any perceived authority to consent;
“a child of eight might well be considered to have the
power to consent to the police crossing the threshold into
that part of the house where any caller, such as a pollster
or salesman, might well be admitted,” 4 LaFave §8.4(c), at
207 (4th ed. 2004), but no one would reasonably expect
such a child to be in a position to authorize anyone to
rummage through his parents’ bedroom.
                               C
   Although we have not dealt directly with the reason-
ableness of police entry in reliance on consent by one
occupant subject to immediate challenge by another, we
took a step toward the issue in an earlier case dealing
with the Fourth Amendment rights of a social guest ar-
rested at premises the police entered without a warrant or
the benefit of any exception to the warrant requirement.
Minnesota v. Olson, 495 U. S. 91 (1990), held that over-
night houseguests have a legitimate expectation of privacy
in their temporary quarters because “it is unlikely that
[the host] will admit someone who wants to see or meet
with the guest over the objection of the guest,” id., at 99.
If that customary expectation of courtesy or deference is a
foundation of Fourth Amendment rights of a houseguest,
it presumably should follow that an inhabitant of shared
premises may claim at least as much, and it turns out that
the co-inhabitant naturally has an even stronger claim.
   To begin with, it is fair to say that a caller standing at
the door of shared premises would have no confidence that
one occupant’s invitation was a sufficiently good reason to
enter when a fellow tenant stood there saying, “stay out.”
Without some very good reason, no sensible person would
                     Cite as: 547 U. S. ____ (2006)                     9

                          Opinion of the Court

go inside under those conditions. Fear for the safety of the
occupant issuing the invitation, or of someone else inside,
would be thought to justify entry, but the justification
then would be the personal risk, the threats to life or limb,
not the disputed invitation.3
   The visitor’s reticence without some such good reason
would show not timidity but a realization that when peo-
ple living together disagree over the use of their common
quarters, a resolution must come through voluntary ac-
commodation, not by appeals to authority. Unless the
people living together fall within some recognized hierar-
chy, like a household of parent and child or barracks
housing military personnel of different grades, there is no
societal understanding of superior and inferior, a fact
reflected in a standard formulation of domestic property
law, that “[e]ach cotenant . . . has the right to use and
enjoy the entire property as if he or she were the sole
owner, limited only by the same right in the other coten-
ants.” 7 R. Powell, Powell on Real Property §50.03[1],
p. 50–14 (M. Wolf gen. ed. 2005). The want of any recog-
nized superior authority among disagreeing tenants is also
reflected in the law’s response when the disagreements
cannot be resolved. The law does not ask who has the
better side of the conflict; it simply provides a right to any
co-tenant, even the most unreasonable, to obtain a decree
partitioning the property (when the relationship is one of
co-ownership) and terminating the relationship. See, e.g.,
2 H. Tiffany, Real Property §§468, 473, 474, pp. 297, 307–
309 (3d ed. 1939 and 2006 Cum. Supp.). And while a
decree of partition is not the answer to disagreement
among rental tenants, this situation resembles co-
——————
   3 Cf. Mincey v. Arizona, 437 U. S. 385, 393 (1978) (acknowledging the

right of police to respond to emergency situations “threatening life or
limb” and indicating that police may conduct a warrantless search pro-
vided that the search is “ ‘strictly circumscribed by the exigencies which
justify its initiation’ ”).
10                       GEORGIA v. RANDOLPH

                            Opinion of the Court

ownership in lacking the benefit of any understanding
that one or the other rental co-tenant has a superior claim
to control the use of the quarters they occupy together. In
sum, there is no common understanding that one co-
tenant generally has a right or authority to prevail over
the express wishes of another, whether the issue is the
color of the curtains or invitations to outsiders.
                              D
   Since the co-tenant wishing to open the door to a third
party has no recognized authority in law or social practice
to prevail over a present and objecting co-tenant, his
disputed invitation, without more, gives a police officer no
better claim to reasonableness in entering than the officer
would have in the absence of any consent at all. Accord-
ingly, in the balancing of competing individual and gov-
ernmental interests entailed by the bar to unreasonable
searches, Camara v. Municipal Court of City and County of
San Francisco, 387 U. S. 523, 536–537 (1967), the coopera-
tive occupant’s invitation adds nothing to the govern-
ment’s side to counter the force of an objecting individual’s
claim to security against the government’s intrusion into
his dwelling place. Since we hold to the “centuries-old
principle of respect for the privacy of the home,” Wilson v.
Layne, 526 U. S. 603, 610 (1999), “it is beyond dispute that
the home is entitled to special protection as the center of
the private lives of our people,” Minnesota v. Carter, 525
U. S. 83, 99 (1998) (KENNEDY, J., concurring). We have,
after all, lived our whole national history with an under-
standing of “the ancient adage that a man’s home is his
castle [to the point that t]he poorest man may in his cot-
tage bid defiance to all the forces of the Crown,” Miller v.
United States, 357 U. S. 301, 307 (1958) (internal quota-
tion marks omitted).4
——————
 4 In   the dissent’s view, the centuries of special protection for the pri-
                     Cite as: 547 U. S. ____ (2006)                    11

                          Opinion of the Court

  Disputed permission is thus no match for this central
value of the Fourth Amendment, and the State’s other
countervailing claims do not add up to outweigh it.5 Yes,
we recognize the consenting tenant’s interest as a citizen
in bringing criminal activity to light, see Coolidge, 403
U. S., at 488 (“[I]t is no part of the policy underlying the
Fourth . . . Amendmen[t] to discourage citizens from aiding
to the utmost of their ability in the apprehension of crimi-
nals”). And we understand a co-tenant’s legitimate self-
interest in siding with the police to deflect suspicion raised
by sharing quarters with a criminal, see 4 LaFave §8.3(d),
at 162, n. 72 (“The risk of being convicted of possession of
drugs one knows are present and has tried to get the other
occupant to remove is by no means insignificant”); cf.
Schneckloth, 412 U. S., at 243 (evidence obtained pursuant
to a consent search “may insure that a wholly innocent
person is not wrongly charged with a criminal offense”).
  But society can often have the benefit of these interests
without relying on a theory of consent that ignores an
inhabitant’s refusal to allow a warrantless search. The co-
tenant acting on his own initiative may be able to deliver
evidence to the police, Coolidge, supra, at 487–489 (sus-
——————
vacy of the home are over. The principal dissent equates inviting the
police into a co-tenant’s home over his contemporaneous objection with
reporting a secret, post, at 13–14 (opinion of ROBERTS, C. J.), and the
emphasis it places on the false equation suggests a deliberate intent to
devalue the importance of the privacy of a dwelling place. The same
attitude that privacy of a dwelling is not special underlies the dissent’s
easy assumption that privacy shared with another individual is privacy
waived for all purposes including warrantless searches by the police.
Post, at 5.
  5 A generalized interest in expedient law enforcement cannot, without

more, justify a warrantless search. See Mincey, supra, at 393 (“[T]he
privacy of a person’s home and property may not be totally sacrificed in
the name of maximum simplicity in enforcement of the criminal law”);
Coolidge v. New Hampshire, 403 U. S. 443, 481 (1971) (“The warrant
requirement . . . is not an inconvenience to be somehow ‘weighed’ against
the claims of police efficiency”).
12                     GEORGIA v. RANDOLPH

                          Opinion of the Court

pect’s wife retrieved his guns from the couple’s house and
turned them over to the police), and can tell the police
what he knows, for use before a magistrate in getting a
warrant.6 The reliance on a co-tenant’s information in-
stead of disputed consent accords with the law’s general
partiality toward “police action taken under a warrant [as
against] searches and seizures without one,” United States
v. Ventresca, 380 U. S. 102, 107 (1965); “the informed and
deliberate determinations of magistrates empowered to
issue warrants as to what searches and seizures are permis-
sible under the Constitution are to be preferred over the
hurried action of officers,” United States v. Lefkowitz, 285
U. S. 452, 464 (1932).
   Nor should this established policy of Fourth Amendment
law be undermined by the principal dissent’s claim that it
shields spousal abusers and other violent co-tenants who
will refuse to allow the police to enter a dwelling when
their victims ask the police for help, post, at 12 (opinion of
ROBERTS, C. J.) (hereinafter the dissent). It is not that the
——————
   6 Sometimes, of course, the very exchange of information like this in

front of the objecting inhabitant may render consent irrelevant by
creating an exigency that justifies immediate action on the police’s part;
if the objecting tenant cannot be incapacitated from destroying easily
disposable evidence during the time required to get a warrant, see
Illinois v. McArthur, 531 U. S. 326, 331–332 (2001) (denying suspect
access to his trailer home while police applied for a search warrant), a
fairly perceived need to act on the spot to preserve evidence may justify
entry and search under the exigent circumstances exception to the
warrant requirement, cf. Schmerber v. California, 384 U. S. 757, 770–
771 (1966) (warrantless search permitted when “the delay necessary to
obtain a warrant . . . threatened the destruction of evidence” (internal
quotation marks omitted)).
   Additional exigent circumstances might justify warrantless searches.
See, e.g., Warden, Md. Penitentiary v. Hayden, 387 U. S. 294, 298
(1967) (hot pursuit); Chimel v. California, 395 U. S. 752 (1969) (protect-
ing the safety of the police officers); Michigan v. Tyler, 436 U. S. 499
(1978) (imminent destruction to building); Johnson v. United States,
333 U. S. 10, 15 (1948) (likelihood that suspect will imminently flee).
                 Cite as: 547 U. S. ____ (2006)           13

                     Opinion of the Court

dissent exaggerates violence in the home; we recognize
that domestic abuse is a serious problem in the United
States. See U. S. Dept. of Justice, National Institute of
Justice, P. Tjaden & N. Thoennes, Full Report of the
Prevalence, Incidence, and Consequence of Violence
Against Women 25–26 (2000) (noting that over 20 million
women and 6 million men will, in the course of their life-
times, be the victims of intimate-partner abuse); U. S.
Dept. of Health and Human Services, Centers for Disease
Control and Prevention, National Center for Injury Pre-
vention and Control, Costs of Intimate Partner Violence
Against Women in the United States 19 (2003) (finding
that nearly 5.3 million intimate partner victimizations,
which result in close to 2 million injuries and 1300 deaths,
occur among women in the United States each year); U. S.
Dept. of Justice, Bureau of Justice Statistics, Crime Data
Brief, C. Rennison, Intimate Partner Violence, 1993–2001
(Feb. 2003) (noting that in 2001 intimate partner violence
made up 20% of violent crime against women); see also
Becker, The Politics of Women’s Wrongs and the Bill of
“Rights”: A Bicentennial Perspective, 59 U. Chi. L. Rev.
454, 507–508 (1992) (noting that women may feel physical
insecurity in their homes as a result of abuse from domes-
tic partners).
   But this case has no bearing on the capacity of the police
to protect domestic victims. The dissent’s argument rests
on the failure to distinguish two different issues: when the
police may enter without committing a trespass, and when
the police may enter to search for evidence. No question
has been raised, or reasonably could be, about the author-
ity of the police to enter a dwelling to protect a resident
from domestic violence; so long as they have good reason
to believe such a threat exists, it would be silly to suggest
that the police would commit a tort by entering, say, to
give a complaining tenant the opportunity to collect be-
longings and get out safely, or to determine whether vio-
14                     GEORGIA v. RANDOLPH

                          Opinion of the Court

lence (or threat of violence) has just occurred or is about to
(or soon will) occur, however much a spouse or other co-
tenant objected. (And since the police would then be
lawfully in the premises, there is no question that they
could seize any evidence in plain view or take further
action supported by any consequent probable cause, see
Texas v. Brown, 460 U. S. 730, 737–739 (1983) (plurality
opinion).) Thus, the question whether the police might
lawfully enter over objection in order to provide any pro-
tection that might be reasonable is easily answered yes.
See 4 LaFave §8.3(d), at 161 (“[E]ven when . . . two per-
sons quite clearly have equal rights in the place, as where
two individuals are sharing an apartment on an equal
basis, there may nonetheless sometimes exist a basis for
giving greater recognition to the interests of one over the
other. . . . [W]here the defendant has victimized the third-
party . . . the emergency nature of the situation is such
that the third-party consent should validate a warrantless
search despite defendant’s objections” (internal quotation
marks omitted; third omission in original)). The un-
doubted right of the police to enter in order to protect a
victim, however, has nothing to do with the question in
this case, whether a search with the consent of one co-
tenant is good against another, standing at the door and
expressly refusing consent.7
   None of the cases cited by the dissent support its im-
probable view that recognizing limits on merely eviden-
tiary searches would compromise the capacity to protect a
fearful occupant. In the circumstances of those cases,
——————
   7 We understand the possibility that a battered individual will be

afraid to express fear candidly, but this does not seem to be a reason to
think such a person would invite the police into the dwelling to search
for evidence against another. Hence, if a rule crediting consent over
denial of consent were built on hoping to protect household victims, it
would distort the Fourth Amendment with little, if any, constructive
effect on domestic abuse investigations.
                 Cite as: 547 U. S. ____ (2006)          15

                     Opinion of the Court

there is no danger that the fearful occupant will be kept
behind the closed door of the house simply because the
abusive tenant refuses to consent to a search. See United
States v. Donlin, 982 F. 2d 31, 32 (CA1 1992) (victimized
individual was already outside of her apartment when
police arrived and, for all intents and purposes, within the
protective custody of law enforcement officers); United
States v. Hendrix, 595 F. 2d 883, 885–886 (CADC 1979)
(per curiam) (even if the consent of the threatened co-
occupant did not justify a warrantless search, the police
entry    was      nevertheless    allowable   on    exigent-
circumstances grounds); People v. Sanders, 904 P. 2d
1311, 1313–1315 (Colo. 1995) (victimized individual gave
her consent-to-search away from her home and was not
present at the time of the police visit; alternatively, exi-
gent circumstances existed to satisfy the warrantless
exception); Brandon v. State, 778 P. 2d 221, 223–224
(Alaska App. 1989) (victimized individual consented away
from her home and was not present at the time of the
police visit); United States v. Davis, 290 F. 3d 1239, 1241
(CA10 2002) (immediate harm extinguished after husband
“order[ed]” wife out of the home).
   The dissent’s red herring aside, we know, of course, that
alternatives to disputed consent will not always open the
door to search for evidence that the police suspect is in-
side. The consenting tenant may simply not disclose
enough information, or information factual enough, to add
up to a showing of probable cause, and there may be no
exigency to justify fast action. But nothing in social cus-
tom or its reflection in private law argues for placing a
higher value on delving into private premises to search for
evidence in the face of disputed consent, than on requiring
clear justification before the government searches private
living quarters over a resident’s objection. We therefore
hold that a warrantless search of a shared dwelling for
evidence over the express refusal of consent by a physi-
16                    GEORGIA v. RANDOLPH

                         Opinion of the Court

cally present resident cannot be justified as reasonable as
to him on the basis of consent given to the police by an-
other resident.8
                             E
  There are two loose ends, the first being the explanation
given in Matlock for the constitutional sufficiency of a co-
tenant’s consent to enter and search: it “rests . . . on mu-
tual use of the property by persons generally having joint
access or control for most purposes, so that it is reasonable
to recognize that any of the co-inhabitants has the right to
permit the inspection in his own right . . . .” 415 U. S., at
171, n. 7. If Matlock’s co-tenant is giving permission “in
his own right,” how can his “own right” be eliminated by
another tenant’s objection? The answer appears in the
very footnote from which the quoted statement is taken:
the “right” to admit the police to which Matlock refers is
not an enduring and enforceable ownership right as un-
derstood by the private law of property, but is instead the
authority recognized by customary social usage as having
a substantial bearing on Fourth Amendment reasonable-
ness in specific circumstances. Thus, to ask whether the
consenting tenant has the right to admit the police when a
physically present fellow tenant objects is not to question
whether some property right may be divested by the mere
objection of another. It is, rather, the question whether
customary social understanding accords the consenting
tenant authority powerful enough to prevail over the co-
tenant’s objection. The Matlock Court did not purport to
answer this question, a point made clear by another
statement (which the dissent does not quote): the Court
——————
  8 The dissent is critical that our holding does not pass upon the con-

stitutionality of such a search as to a third tenant against whom the
government wishes to use evidence seized after a search with consent of
one co-tenant subject to the contemporaneous objection of another, post,
at 11. We decide the case before us, not a different one.
                  Cite as: 547 U. S. ____ (2006)           17

                      Opinion of the Court

described the co-tenant’s consent as good against “the
absent, nonconsenting” resident.” Id., at 170.
   The second loose end is the significance of Matlock and
Rodriguez after today’s decision. Although the Matlock
defendant was not present with the opportunity to object,
he was in a squad car not far away; the Rodriguez defen-
dant was actually asleep in the apartment, and the police
might have roused him with a knock on the door before
they entered with only the consent of an apparent co-
tenant. If those cases are not to be undercut by today’s
holding, we have to admit that we are drawing a fine line;
if a potential defendant with self-interest in objecting is in
fact at the door and objects, the co-tenant’s permission
does not suffice for a reasonable search, whereas the
potential objector, nearby but not invited to take part in
the threshold colloquy, loses out.
   This is the line we draw, and we think the formalism is
justified. So long as there is no evidence that the police
have removed the potentially objecting tenant from the
entrance for the sake of avoiding a possible objection,
there is practical value in the simple clarity of complemen-
tary rules, one recognizing the co-tenant’s permission
when there is no fellow occupant on hand, the other ac-
cording dispositive weight to the fellow occupant’s con-
trary indication when he expresses it. For the very reason
that Rodriguez held it would be unjustifiably impractical
to require the police to take affirmative steps to confirm
the actual authority of a consenting individual whose
authority was apparent, we think it would needlessly limit
the capacity of the police to respond to ostensibly legiti-
mate opportunities in the field if we were to hold that
reasonableness required the police to take affirmative
steps to find a potentially objecting co-tenant before acting
on the permission they had already received. There is no
ready reason to believe that efforts to invite a refusal
would make a difference in many cases, whereas every co-
18                    GEORGIA v. RANDOLPH

                         Opinion of the Court

tenant consent case would turn into a test about the ade-
quacy of the police’s efforts to consult with a potential
objector. Better to accept the formalism of distinguishing
Matlock from this case than to impose a requirement,
time-consuming in the field and in the courtroom, with no
apparent systemic justification. The pragmatic decision to
accept the simplicity of this line is, moreover, supported by
the substantial number of instances in which suspects who
are asked for permission to search actually consent,9 albeit
imprudently, a fact that undercuts any argument that the
police should try to locate a suspected inhabitant because
his denial of consent would be a foregone conclusion.
                             III
   This case invites a straightforward application of the
rule that a physically present inhabitant’s express refusal
of consent to a police search is dispositive as to him, re-
gardless of the consent of a fellow occupant. Scott
Randolph’s refusal is clear, and nothing in the record
justifies the search on grounds independent of Janet
Randolph’s consent. The State does not argue that she
gave any indication to the police of a need for protection
inside the house that might have justified entry into the
portion of the premises where the police found the pow-
dery straw (which, if lawfully seized, could have been used
when attempting to establish probable cause for the war-
rant issued later). Nor does the State claim that the entry
and search should be upheld under the rubric of exigent
circumstances, owing to some apprehension by the police
——————
  9 See 4 LaFave §8.1, at 4 (“The so-called consent search is frequently
relied upon by police as a means of investigating suspected criminal
conduct” (footnote omitted)); Strauss, Reconstructing Consent, 92 J.
Crim. L. & C. 211, 214 (2001–2002) (“Although precise figures detailing
the number of searches conducted pursuant to consent are not—and
probably can never be—available, there is no dispute that these type of
searches affect tens of thousands, if not hundreds of thousands, of
people every year” (footnote omitted)).
                 Cite as: 547 U. S. ____ (2006)           19

                     Opinion of the Court

officers that Scott Randolph would destroy evidence of
drug use before any warrant could be obtained.
  The judgment of the Supreme Court of Georgia is there-
fore affirmed.
                                           It is so ordered.

  JUSTICE ALITO took no part in the consideration or
decision of this case.
                    Cite as: 547 U. S. ____ (2006)                   1

                       STEVENS, J., concurring

SUPREME COURT OF THE UNITED STATES
                             _________________

                             No. 04–1067
                             _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                           [March 22, 2006]

   JUSTICE STEVENS, concurring.
   The study of history for the purpose of ascertaining the
original understanding of constitutional provisions is much
like the study of legislative history for the purpose of ascer-
taining the intent of the lawmakers who enact statutes. In
both situations the facts uncovered by the study are usually
relevant but not necessarily dispositive. This case illus-
trates why even the most dedicated adherent to an ap-
proach to constitutional interpretation that places primary
reliance on the search for original understanding would
recognize the relevance of changes in our society.
   At least since 1604 it has been settled that in the ab-
sence of exigent circumstances, a government agent has no
right to enter a “house” or “castle” unless authorized to do
so by a valid warrant. See Semayne’s Case, 5 Co. Rep.
91a, 77 Eng. Rep. 194 (K.B.). Every occupant of the home
has a right—protected by the common law for centuries
and by the Fourth Amendment since 1791—to refuse
entry. When an occupant gives his or her consent to enter,
he or she is waiving a valuable constitutional right. To be
sure that the waiver is voluntary, it is sound practice—a
practice some Justices of this Court thought necessary to
make the waiver voluntary1—for the officer to advise the
——————
  1 See, e.g., Schneckloth v. Bustamonte, 412 U. S. 218, 284–285 (1973)

(Marshall, J., dissenting) (pointing out that it is hard to comprehend
“how a decision made without knowledge of available alternatives can
2                      GEORGIA v. RANDOLPH

                        STEVENS, J., concurring

occupant of that right.2 The issue in this case relates to
the content of the advice that the officer should provide
when met at the door by a man and a woman who are
apparently joint tenants or joint owners of the property.
  In the 18th century, when the Fourth Amendment was
adopted, the advice would have been quite different from
what is appropriate today. Given the then-prevailing
dramatic differences between the property rights of the
husband and the far lesser rights of the wife, only the
consent of the husband would matter. Whether “the mas-
ter of the house” consented or objected, his decision would
control. Thus if “original understanding” were to govern
the outcome of this case, the search was clearly invalid
because the husband did not consent. History, however, is
not dispositive because it is now clear, as a matter of
constitutional law, that the male and the female are equal
partners. Reed v. Reed, 404 U. S. 71 (1971).
  In today’s world the only advice that an officer could
properly give should make it clear that each of the part-
ners has a constitutional right that he or she may inde-
pendently assert or waive. Assuming that both spouses
are competent, neither one is a master possessing the
power to override the other’s constitutional right to deny
entry to their castle.
  With these observations, I join the Court’s opinion.
——————
be treated as choice at all,” and arguing that “[i]f consent to search
means that a person has chosen to forego his right to exclude the police
from the place they seek to search, it follows that his consent cannot be
considered a meaningful choice unless he knew that he could in fact
exclude the police”).
  2 Such advice is surely preferable to an officer’s expression of his or

her desire to enter and to search in words that may be construed either
as a command or a question. See id., at 275–276 (Douglas, J., dissenting)
(noting that “ ‘[u]nder many circumstances a reasonable person might
read an officer’s “May I” as the courteous expression of a demand
backed by force of law.’ ” (quoting Bustamonte v. Schneckloth, 448 F. 2d
669, 701 (CA9 1971))).
                  Cite as: 547 U. S. ____ (2006)            1

                     BREYER, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 04–1067
                          _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                        [March 22, 2006]

   JUSTICE BREYER, concurring.
   If Fourth Amendment law forced us to choose between
two bright-line rules, (1) a rule that always found one
tenant’s consent sufficient to justify a search without a
warrant and (2) a rule that never did, I believe we should
choose the first. That is because, as THE CHIEF JUSTICE’s
dissent points out, a rule permitting such searches can
serve important law enforcement needs (for example, in
domestic abuse cases) and the consenting party’s joint
tenancy diminishes the objecting party’s reasonable expec-
tation of privacy.
   But the Fourth Amendment does not insist upon bright-
line rules. Rather, it recognizes that no single set of legal
rules can capture the ever changing complexity of human
life. It consequently uses the general terms “unreasonable
searches and seizures.” And this Court has continuously
emphasized that “[r]easonableness . . . is measured . . . by
examining the totality of the circumstances.” Ohio v.
Robinette, 519 U. S. 33, 39 (1996); see also Illinois v. Ward-
low, 528 U. S. 119, 136 (2000) (STEVENS, J., concurring in
part and dissenting in part); Florida v. Bostick, 501 U. S.
429, 439 (1991); Michigan v. Chesternut, 486 U. S. 567, 572–
573 (1988); Florida v. Royer, 460 U. S. 491, 506 (1983) (plu-
rality opinion).
   The circumstances here include the following: The
search at issue was a search solely for evidence. The
2                  GEORGIA v. RANDOLPH

                    BREYER, J., concurring

objecting party was present and made his objection known
clearly and directly to the officers seeking to enter the
house. The officers did not justify their search on grounds
of possible evidence destruction. Cf. Thornton v. United
States, 541 U. S. 615, 620–622 (2004); Skinner v. Railway
Labor Executives’ Assn., 489 U. S. 602, 623 (1989); Schmer-
ber v. California, 384 U. S. 757, 770–771 (1966). And, as far
as the record reveals, the officers might easily have se-
cured the premises and sought a warrant permitting them
to enter. See Illinois v. McArthur, 531 U. S. 326 (2001).
Thus, the “totality of the circumstances” present here do
not suffice to justify abandoning the Fourth Amendment’s
traditional hostility to police entry into a home without a
warrant.
   I stress the totality of the circumstances, however,
because, were the circumstances to change significantly,
so should the result. The Court’s opinion does not apply
where the objector is not present “and object[ing].” Ante,
at 17.
   Moreover, the risk of an ongoing crime or other exigent
circumstance can make a critical difference. Consider,
for example, instances of domestic abuse. See ante, at
13. “Family disturbance calls . . . constitute the largest
single category of calls received by police departments
each year.” Mederer & Gelles, Compassion or Control:
Intervention in Cases of Wife Abuse, 4 Journal of
Interpersonal Violence 25 (Mar. 1989) (emphasis deleted);
see also, e.g., Office of the Attorney General, California
Criminal Justice Statistics Center, Domestic Violence
Related Calls for Assistance, 1987–2003, County
by Year, http://ag.ca.gov/cjsc/publications/misc/dvsr/tabs/
8703.pdf (as visited Mar. 1, 2006, and available in Clerk of
Court’s case file) (providing data showing that California
police received an average of 207,848 domestic violence
related calls each year); Cessato, Defenders Against Do-
mestic Abuse, Washington Post, Aug. 25, 2002, p. B8 (“In
                  Cite as: 547 U. S. ____ (2006)            3

                     BREYER, J., concurring

the District [of Columbia], police report that almost half of
roughly 39,000 violent crime calls received in 2000 in-
volved domestic violence”); Zorza, Women Battering: High
Costs and the State of the Law, Clearinghouse Review,
p. 385 (Special Issue 1994) (“One-third of all police time is
spent responding to domestic disturbance calls”). And,
law enforcement officers must be able to respond effec-
tively when confronted with the possibility of abuse.
   If a possible abuse victim invites a responding officer to
enter a home or consents to the officer’s entry request,
that invitation (or consent) itself could reflect the victim’s
fear about being left alone with an abuser. It could also
indicate the availability of evidence, in the form of an
immediate willingness to speak, that might not otherwise
exist. In that context, an invitation (or consent) would
provide a special reason for immediate, rather than later,
police entry. And, entry following invitation or consent by
one party ordinarily would be reasonable even in the face
of direct objection by the other. That being so, contrary to
the THE CHIEF JUSTICE’s suggestion, post, at 13, today’s
decision will not adversely affect ordinary law enforcement
practices.
   Given the case-specific nature of the Court’s holding,
and with these understandings, I join the Court’s holding
and its opinion.
                 Cite as: 547 U. S. ____ (2006)           1

                   ROBERTS, C. J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1067
                         _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                       [March 22, 2006]

   CHIEF JUSTICE ROBERTS, with whom JUSTICE SCALIA
joins, dissenting.
   The Court creates constitutional law by surmising what
is typical when a social guest encounters an entirely atypi-
cal situation. The rule the majority fashions does not
implement the high office of the Fourth Amendment to
protect privacy, but instead provides protection on a ran-
dom and happenstance basis, protecting, for example, a co-
occupant who happens to be at the front door when the
other occupant consents to a search, but not one napping
or watching television in the next room. And the cost of
affording such random protection is great, as demon-
strated by the recurring cases in which abused spouses
seek to authorize police entry into a home they share with
a nonconsenting abuser.
   The correct approach to the question presented is clearly
mapped out in our precedents: The Fourth Amendment
protects privacy. If an individual shares information,
papers, or places with another, he assumes the risk that
the other person will in turn share access to that informa-
tion or those papers or places with the government. And
just as an individual who has shared illegal plans or in-
criminating documents with another cannot interpose an
objection when that other person turns the information
over to the government, just because the individual hap-
pens to be present at the time, so too someone who shares
2                  GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

a place with another cannot interpose an objection when
that person decides to grant access to the police, simply
because the objecting individual happens to be present.
  A warrantless search is reasonable if police obtain the
voluntary consent of a person authorized to give it. Co-
occupants have “assumed the risk that one of their num-
ber might permit [a] common area to be searched.” United
States v. Matlock, 415 U. S. 164, 171, n. 7 (1974). Just as
Mrs. Randolph could walk upstairs, come down, and turn
her husband’s cocaine straw over to the police, she can
consent to police entry and search of what is, after all, her
home, too.
                               I
   In Illinois v. Rodriguez, 497 U. S. 177 (1990), this Court
stated that “[w]hat [a person] is assured by the Fourth
Amendment . . . is not that no government search of his
house will occur unless he consents; but that no such
search will occur that is ‘unreasonable.’ ” Id., at 183. One
element that can make a warrantless government search
of a home “ ‘reasonable’ ” is voluntary consent. Id., at 184;
Schneckloth v. Bustamonte, 412 U. S. 218, 219 (1973).
Proof of voluntary consent “is not limited to proof that
consent was given by the defendant,” but the government
“may show that permission to search was obtained from a
third party who possessed common authority over or other
sufficient relationship to the premises.” Matlock, supra, at
171. Today’s opinion creates an exception to this other-
wise clear rule: A third-party consent search is unreason-
able, and therefore constitutionally impermissible, if the
co-occupant against whom evidence is obtained was pre-
sent and objected to the entry and search.
   This exception is based on what the majority describes
as “widely shared social expectations” that “when people
living together disagree over the use of their common
quarters, a resolution must come through voluntary ac-
                 Cite as: 547 U. S. ____ (2006)            3

                   ROBERTS, C. J., dissenting

commodation.” Ante, at 6, 9. But this fundamental predi-
cate to the majority’s analysis gets us nowhere: Does the
objecting cotenant accede to the consenting cotenant’s
wishes, or the other way around? The majority’s assump-
tion about voluntary accommodation simply leads to the
common stalemate of two gentlemen insisting that the
other enter a room first.
   Nevertheless, the majority is confident in assuming—
confident enough to incorporate its assumption into the
Constitution—that an invited social guest who arrives at
the door of a shared residence, and is greeted by a dis-
agreeable co-occupant shouting “ ‘stay out,’ ” would simply
go away. Ante, at 8. The Court observes that “no sensible
person would go inside under those conditions,” ante, at 8–
9, and concludes from this that the inviting co-occupant
has no “authority” to insist on getting her way over the
wishes of her co-occupant, ante, at 10. But it seems
equally accurate to say—based on the majority’s conclu-
sion that one does not have a right to prevail over the
express wishes of his co-occupant—that the objector has
no “authority” to insist on getting his way over his co-
occupant’s wish that her guest be admitted.
   The fact is that a wide variety of differing social situa-
tions can readily be imagined, giving rise to quite different
social expectations. A relative or good friend of one of two
feuding roommates might well enter the apartment over
the objection of the other roommate. The reason the in-
vitee appeared at the door also affects expectations: A
guest who came to celebrate an occupant’s birthday, or one
who had traveled some distance for a particular reason,
might not readily turn away simply because of a room-
mate’s objection. The nature of the place itself is also
pertinent: Invitees may react one way if the feuding
roommates share one room, differently if there are com-
mon areas from which the objecting roommate could read-
ily be expected to absent himself. Altering the numbers
4                  GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

might well change the social expectations: Invitees might
enter if two of three co-occupants encourage them to do so,
over one dissenter.
   The possible scenarios are limitless, and slight varia-
tions in the fact pattern yield vastly different expecta-
tions about whether the invitee might be expected to
enter or to go away. Such shifting expectations are not a
promising foundation on which to ground a constitutional
rule, particularly because the majority has no support for
its basic assumption—that an invited guest encountering
two disagreeing co-occupants would flee—beyond a hunch
about how people would typically act in an atypical
situation.
   And in fact the Court has not looked to such expecta-
tions to decide questions of consent under the Fourth
Amendment, but only to determine when a search has
occurred and whether a particular person has standing to
object to a search. For these latter inquiries, we ask
whether a person has a subjective expectation of privacy
in a particular place, and whether “the expectation [is] one
that society is prepared to recognize as ‘reasonable.’ ” Katz
v. United States, 389 U. S. 347, 361 (1967) (Harlan, J.,
concurring); see Minnesota v. Olson, 495 U. S. 91, 95–96,
100 (1990) (extending Katz test to standing inquiry). But
the social expectations concept has not been applied to all
questions arising under the Fourth Amendment, least of
all issues of consent. A criminal might have a strong
expectation that his longtime confidant will not allow the
government to listen to their private conversations, but
however profound his shock might be upon betrayal, gov-
ernment monitoring with the confidant’s consent is rea-
sonable under the Fourth Amendment. See United States
v. White, 401 U. S. 745, 752 (1971).
   The majority suggests that “widely shared social expecta-
tions” are a “constant element in assessing Fourth Amend-
ment reasonableness,” ante, at 6 (citing Rakas v. Illinois,
                  Cite as: 547 U. S. ____ (2006)              5

                    ROBERTS, C. J., dissenting

439 U. S. 128, 144, n. 12 (1978)), but that is not the case; the
Fourth Amendment precedents the majority cites refer
instead to a “legitimate expectation of privacy.” Ibid.
(emphasis added; internal quotation marks omitted).
Whatever social expectation the majority seeks to protect,
it is not one of privacy. The very predicate giving rise to
the question in cases of shared information, papers, con-
tainers, or places is that privacy has been shared with
another. Our common social expectations may well be
that the other person will not, in turn, share what we have
shared with them with another—including the police—but
that is the risk we take in sharing. If two friends share a
locker and one keeps contraband inside, he might trust
that his friend will not let others look inside. But by
sharing private space, privacy has “already been frus-
trated” with respect to the lockermate. United States v.
Jacobsen, 466 U. S. 109, 117 (1984). If two roommates
share a computer and one keeps pirated software on a
shared drive, he might assume that his roommate will not
inform the government. But that person has given up his
privacy with respect to his roommate by saving the soft-
ware on their shared computer.
   A wide variety of often subtle social conventions may
shape expectations about how we act when another
shares with us what is otherwise private, and those con-
ventions go by a variety of labels—courtesy, good man-
ners, custom, protocol, even honor among thieves. The
Constitution, however, protects not these but privacy, and
once privacy has been shared, the shared information,
documents, or places remain private only at the discretion
of the confidant.
                            II
  Our cases reflect this understanding. In United States
v. White, we held that one party to a conversation can
consent to government eavesdropping, and statements
6                  GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

made by the other party will be admissible at trial. 401
U. S., at 752. This rule is based on privacy: “Inescapably,
one contemplating illegal activities must realize and risk
that his companions may be reporting to the police. . . . [I]f
he has no doubts, or allays them, or risks what doubt he
has, the risk is his.” Ibid.
   The Court has applied this same analysis to objects and
places as well. In Frazier v. Cupp, 394 U. S. 731 (1969), a
duffel bag “was being used jointly” by two cousins. Id., at
740. The Court held that the consent of one was effective
to result in the seizure of evidence used against both: “[I]n
allowing [his cousin] to use the bag and in leaving it in his
house, [the defendant] must be taken to have assumed the
risk that [his cousin] would allow someone else to look
inside.” Ibid.
   As the Court explained in United States v. Jacobsen,
supra:
    “It is well settled that when an individual reveals pri-
    vate information to another, he assumes the risk that
    his confidant will reveal that information to the au-
    thorities, and if that occurs the Fourth Amendment
    does not prohibit governmental use of that informa-
    tion. Once frustration of the original expectation of
    privacy occurs, the Fourth Amendment does not pro-
    hibit governmental use of the now nonprivate infor-
    mation: ‘This Court has held repeatedly that the
    Fourth Amendment does not prohibit the obtaining of
    information revealed to a third party and conveyed by
    him to Government authorities, even if the informa-
    tion is revealed on the assumption that it will be used
    only for a limited purpose and the confidence placed in
    a third party will not be betrayed.’ ” Id., at 117 (quot-
    ing United States v. Miller, 425 U. S. 435, 443 (1976)).
  The same analysis applies to the question whether our
privacy can be compromised by those with whom we share
                 Cite as: 547 U. S. ____ (2006)            7

                   ROBERTS, C. J., dissenting

common living space. If a person keeps contraband in
common areas of his home, he runs the risk that his co-
occupants will deliver the contraband to the police. In
Coolidge v. New Hampshire, 403 U. S. 443 (1971), Mrs.
Coolidge retrieved four of her husband’s guns and the
clothes he was wearing the previous night and handed them
over to police. We held that these items were properly
admitted at trial because “when Mrs. Coolidge of her own
accord produced the guns and clothes for inspection, . . . it
was not incumbent on the police to stop her or avert their
eyes.” Id., at 489.
   Even in our most private relationships, our observable
actions and possessions are private at the discretion of
those around us. A husband can request that his wife not
tell a jury about contraband that she observed in their
home or illegal activity to which she bore witness, but it is
she who decides whether to invoke the testimonial marital
privilege. Trammel v. United States, 445 U. S. 40, 53
(1980). In Trammel, we noted that the former rule prohib-
iting a wife from testifying about her husband’s observable
wrongdoing at his say so “goes far beyond making ‘every
man’s house his castle,’ and permits a person to convert
his house into ‘a den of thieves.’ ” Id., at 51–52 (quoting 5
J. Bentham, Rationale of Judicial Evidence 340 (1827)).
   There is no basis for evaluating physical searches of
shared space in a manner different from how we evaluated
the privacy interests in the foregoing cases, and in fact the
Court has proceeded along the same lines in considering
such searches. In Matlock, police arrested the defendant
in the front yard of a house and placed him in a squad car,
and then obtained permission from Mrs. Graff to search a
shared bedroom for evidence of Matlock’s bank robbery.
415 U. S., at 166. Police certainly could have assumed
that Matlock would have objected were he consulted as he
sat handcuffed in the squad car outside. And in Rodri-
guez, where Miss Fischer offered to facilitate the arrest of
8                     GEORGIA v. RANDOLPH

                       ROBERTS, C. J., dissenting

her sleeping boyfriend by admitting police into an apart-
ment she apparently shared with him, 497 U. S., at 179,
police might have noted that this entry was undoubtedly
contrary to Rodriguez’s social expectations. Yet both of
these searches were reasonable under the Fourth
Amendment because Mrs. Graff had authority, and Miss
Fischer apparent authority, to admit others into areas
over which they exercised control, despite the almost
certain wishes of their present co-occupants.
   The common thread in our decisions upholding searches
conducted pursuant to third-party consent is an under-
standing that a person “assume[s] the risk” that those who
have access to and control over his shared property might
consent to a search. Matlock, 415 U. S., at 171, n. 7. In
Matlock, we explained that this assumption of risk is
derived from a third party’s “joint access or control for
most purposes” of shared property. Ibid. And we con-
cluded that shared use of property makes it “reasonable to
recognize that any of the co-inhabitants has the right to
permit the inspection in his own right.” Ibid.
   In this sense, the risk assumed by a joint occupant is
comparable to the risk assumed by one who reveals pri-
vate information to another. If a person has incriminating
information, he can keep it private in the face of a request
from police to share it, because he has that right under the
Fifth Amendment. If a person occupies a house with
incriminating information in it, he can keep that informa-
tion private in the face of a request from police to search
the house, because he has that right under the Fourth
Amendment. But if he shares the information—or the
house—with another, that other can grant access to the
police in each instance.1
——————
  1 The majority considers this comparison to be a “false equation,” and

even discerns “a deliberate intent to devalue the importance of the
privacy of a dwelling place.” Ante, at 10–11, n. 4. But the differences
                      Cite as: 547 U. S. ____ (2006)                     9

                        ROBERTS, C. J., dissenting

  To the extent a person wants to ensure that his posses-
sions will be subject to a consent search only due to his
own consent, he is free to place these items in an area over
which others do not share access and control, be it a pri-
vate room or a locked suitcase under a bed. Mr. Randolph
acknowledged this distinction in his motion to suppress,
where he differentiated his law office from the rest of the
Randolph house by describing it as an area that “was
solely in his control and dominion.” App. 3. As to a “com-
mon area,” however, co-occupants with “joint access or
control” may consent to an entry and search. Matlock,
supra, at 171, n. 7.
  By emphasizing the objector’s presence and noting an
occupant’s understanding that obnoxious guests might “be
admitted in [one’s] absence,” ante, at 7, the majority ap-
pears to resurrect an agency theory of consent suggested
in our early cases. See Stoner v. California, 376 U. S. 483,
——————
between the majority and this dissent reduce to this: Under the major-
ity’s view, police may not enter and search when an objecting co-
occupant is present at the door, but they may do so when he is asleep in
the next room; under our view, the co-occupant’s consent is effective in
both cases. It seems a bit overwrought to characterize the former
approach as affording great protection to a man in his castle, the latter
as signaling that “the centuries of special protection for the privacy of
the home are over.” Ibid. The Court in United States v. Matlock, 415
U. S. 164 (1974), drew the same comparison the majority faults today,
see id., at 171, n. 7, and the “deliberate intent” the majority ascribes to
this dissent is apparently shared by all Courts of Appeals and the great
majority of State Supreme Courts to have considered the question, see
ante, at 4, n. 1.
   The majority also mischaracterizes this dissent as assuming that
“privacy shared with another individual is privacy waived for all
purposes including warrantless searches by the police.” Ante, at 11,
n. 4. The point, of course, is not that a person waives his privacy by
sharing space with others such that police may enter at will, but that
sharing space necessarily entails a limited yielding of privacy to the
person with whom the space is shared, such that the other person
shares authority to consent to a search of the shared space. See supra,
at 2, 5–10.
10                 GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

489 (1964) (stating that a hotel clerk could not consent to a
search of a guest’s room because the guest had not waived
his rights “by word or deed, either directly or through an
agent”); Chapman v. United States, 365 U. S. 610, 616–
617 (1961). This agency theory is belied by the facts of
Matlock and Rodriguez—both defendants were present but
simply not asked for consent—and the Court made clear in
those cases that a co-occupant’s authority to consent
rested not on an absent occupant’s delegation of choice to
an agent, but on the consenting co-occupant’s “joint access
or control” of the property. Matlock, supra, at 171, n. 7;
see Rodriguez, supra, at 181; United States v. McAlpine,
919 F. 2d 1461, 1464, n. 2 (CA10 1990) (“[A]gency analysis
[was] put to rest by the Supreme Court’s reasoning in
Matlock”).
  The law acknowledges that although we might not
expect our friends and family to admit the government
into common areas, sharing space entails risk. A person
assumes the risk that his co-occupants—just as they
might report his illegal activity or deliver his contraband
to the government—might consent to a search of areas
over which they have access and control. See United
States v. Karo, 468 U. S. 705, 726 (1984) (O’Connor, J.,
concurring in part and concurring in judgment) (finding it
a “relatively easy case . . . when two persons share identi-
cal, overlapping privacy interests in a particular place,
container, or conversation. Here both share the power to
surrender each other’s privacy to a third party”).
                             III
  The majority states its rule as follows: “[A] warrantless
search of a shared dwelling for evidence over the express
refusal of consent by a physically present resident cannot
be justified as reasonable as to him on the basis of consent
given to the police by another resident.” Ante, at 15–16.
  Just as the source of the majority’s rule is not privacy, so
                  Cite as: 547 U. S. ____ (2006)           11

                   ROBERTS, C. J., dissenting

too the interest it protects cannot reasonably be described as
such. That interest is not protected if a co-owner happens to
be absent when the police arrive, in the backyard gardening,
asleep in the next room, or listening to music through ear-
phones so that only his co-occupant hears the knock on the
door. That the rule is so random in its application confirms
that it bears no real relation to the privacy protected by the
Fourth Amendment. What the majority’s rule protects is
not so much privacy as the good luck of a co-owner who just
happens to be present at the door when the police arrive.
Usually when the development of Fourth Amendment
jurisprudence leads to such arbitrary lines, we take it as a
signal that the rules need to be rethought. See California v.
Acevedo, 500 U. S. 565, 574, 580 (1991). We should not
embrace a rule at the outset that its sponsors appreciate will
result in drawing fine, formalistic lines. See ante, at 17.
   Rather than draw such random and happenstance lines—
and pretend that the Constitution decreed them—the more
reasonable approach is to adopt a rule acknowledging that
shared living space entails a limited yielding of privacy to
others, and that the law historically permits those to whom
we have yielded our privacy to in turn cooperate with the
government. Such a rule flows more naturally from our
cases concerning Fourth Amendment reasonableness and is
logically grounded in the concept of privacy underlying that
Amendment.
   The scope of the majority’s rule is not only arbitrary but
obscure as well. The majority repeats several times that a
present co-occupant’s refusal to permit entry renders the
search unreasonable and invalid “as to him.” Ante, at 1, 15–
16, 18. This implies entry and search would be reasonable
“as to” someone else, presumably the consenting co-occupant
and any other absent co-occupants. The normal Fourth
Amendment rule is that items discovered in plain view are
admissible if the officers were legitimately on the premises;
if the entry and search were reasonable “as to” Mrs.
12                 GEORGIA v. RANDOLPH

                   ROBERTS, C. J., dissenting

Randolph, based on her consent, it is not clear why the
cocaine straw should not be admissible “as to” Mr.
Randolph, as discovered in plain view during a legitimate
search “as to” Mrs. Randolph. The majority’s differentiation
between entry focused on discovering whether domestic
violence has occurred (and the consequent authority to seize
items in plain view), and entry focused on searching for
evidence of other crime, is equally puzzling. See ante, at 13–
14. This Court has rejected subjective motivations of police
officers in assessing Fourth Amendment questions, see
Whren v. United States, 517 U. S. 806, 812–813 (1996), with
good reason: The police do not need a particular reason to
ask for consent to search, whether for signs of domestic
violence or evidence of drug possession.
   While the majority’s rule protects something random, its
consequences are particularly severe. The question pre-
sented often arises when innocent cotenants seek to disasso-
ciate or protect themselves from ongoing criminal activity.
See, e.g., United States v. Hendrix, 595 F. 2d 883, 884
(CADC 1979) (wife asked police “to get her baby and take
[a] sawed-off shotgun out of her house”); People v. Cosme,
48 N. Y. 2d 286, 288–289, 293, 397 N. E. 2d 1319, 1320,
1323 (1979) (woman asked police to remove cocaine and a
gun from a shared closet); United States v. Botsch, 364
F. 2d 542, 547 (CA2 1966). Under the majority’s rule,
there will be many cases in which a consenting co-
occupant’s wish to have the police enter is overridden by
an objection from another present co-occupant. What does
the majority imagine will happen, in a case in which the
consenting co-occupant is concerned about the other’s
criminal activity, once the door clicks shut? The objecting
co-occupant may pause briefly to decide whether to de-
stroy any evidence of wrongdoing or to inflict retribution
on the consenting co-occupant first, but there can be little
doubt that he will attend to both in short order. It is no
answer to say that the consenting co-occupant can depart
                      Cite as: 547 U. S. ____ (2006)                     13

                        ROBERTS, C. J., dissenting

with the police; remember that it is her home, too, and the
other co-occupant’s very presence, which allowed him to
object, may also prevent the consenting co-occupant from
doing more than urging the police to enter.
   Perhaps the most serious consequence of the majority’s
rule is its operation in domestic abuse situations, a context
in which the present question often arises. See Rodriguez,
497 U. S., at 179; United States v. Donlin, 982 F. 2d 31
(CA1 1992); Hendrix, supra; People v. Sanders, 904 P. 2d
1311 (Colo. 1995) (en banc); Brandon v. State, 778 P. 2d
221 (Alaska App. 1989). While people living together
might typically be accommodating to the wishes of their
cotenants, requests for police assistance may well come
from coinhabitants who are having a disagreement. The
Court concludes that because “no sensible person would go
inside” in the face of disputed consent, ante, at 8–9, and
the consenting cotenant thus has “no recognized author-
ity” to insist on the guest’s admission, ante, at 10, a “police
officer [has] no better claim to reasonableness in entering
than the officer would have in the absence of any consent
at all,” ibid. But the police officer’s superior claim to enter
is obvious: Mrs. Randolph did not invite the police to join
her for dessert and coffee; the officer’s precise purpose in
knocking on the door was to assist with a dispute between
the Randolphs—one in which Mrs. Randolph felt the need
for the protective presence of the police. The majority’s
rule apparently forbids police from entering to assist with
a domestic dispute if the abuser whose behavior prompted
the request for police assistance objects.2
——————
   2 In response to this concern, the majority asserts that its rule applies

“merely [to] evidentiary searches.” Ante, at 14. But the fundamental
premise of the majority’s argument is that an inviting co-occupant has
“no recognized authority” to “open the door” over a co-occupant’s objec-
tion. Ante, at 10; see also ante, at 1 (“[A] physically present co-
occupant’s stated refusal to permit entry prevails, rendering the war-
rantless search unreasonable and invalid as to him” (emphasis added));
14                     GEORGIA v. RANDOLPH

                       ROBERTS, C. J., dissenting

   The majority acknowledges these concerns, but dis-
misses them on the ground that its rule can be expected to
give rise to exigent situations, and police can then rely on
an exigent circumstances exception to justify entry. Ante,
at 12, n. 6. This is a strange way to justify a rule, and the
fact that alternative justifications for entry might arise
does not show that entry pursuant to consent is unreason-
able. In addition, it is far from clear that an exception for
emergency entries suffices to protect the safety of occu-
pants in domestic disputes. See, e.g., United States v.
Davis, 290 F. 3d 1239, 1240–1241 (CA10 2002) (finding no
exigent circumstances justifying entry when police re-
sponded to a report of domestic abuse, officers heard no
noise upon arrival, defendant told officers that his wife
was out of town, and wife then appeared at the door seem-
ingly unharmed but resisted husband’s efforts to close the
door).
   Rather than give effect to a consenting spouse’s author-
ity to permit entry into her house to avoid such situations,
the majority again alters established Fourth Amendment
rules to defend giving veto power to the objecting spouse.
In response to the concern that police might be turned
away under its rule before entry can be justified based on
exigency, the majority creates a new rule: A “good reason”
to enter, coupled with one occupant’s consent, will ensure
——————
ante, at 8 (“[A] caller standing at the door of shared premises would
have no confidence . . . to enter when a fellow tenant stood there saying
‘stay out’ ” (emphasis added)); ante, at 10 (“[A] disputed invitation,
without more, gives a police officer no . . . claim to reasonableness in
entering” (emphasis added)). The point is that the majority’s rule
transforms what may have begun as a request for consent to conduct an
evidentiary search into something else altogether, by giving veto power
over the consenting co-occupant’s wishes to an occupant who would
exclude the police from entry. The majority would afford the now quite
vulnerable consenting co-occupant sufficient time to gather her belong-
ings and leave, see ante, at 13, apparently putting to one side the fact
that it is her castle, too.
                 Cite as: 547 U. S. ____ (2006)           15

                   ROBERTS, C. J., dissenting

that a police officer is “lawfully in the premises.” Ante, at
13, 14. As support for this “consent plus a good reason”
rule, the majority cites a treatise, which itself refers only
to emergency entries. Ante, at 14 (citing 4 W. LaFave,
Search and Seizure §8.3(d), p. 161 (4th ed. 2004)). For the
sake of defending what it concedes are fine, formalistic
lines, the majority spins out an entirely new framework
for analyzing exigent circumstances. Police may now
enter with a “good reason” to believe that “violence (or
threat of violence) has just occurred or is about to (or soon
will) occur.” Ante, at 13–14. And apparently a key factor
allowing entry with a “good reason” short of exigency is
the very consent of one co-occupant the majority finds so
inadequate in the first place.
   The majority’s analysis alters a great deal of established
Fourth Amendment law. The majority imports the con-
cept of “social expectations,” previously used only to de-
termine when a search has occurred and whether a par-
ticular person has standing to object to a search, into
questions of consent. Ante, at 6, 8. To determine whether
entry and search are reasonable, the majority considers a
police officer’s subjective motive in asking for consent,
which we have otherwise refrained from doing in assess-
ing Fourth Amendment questions. Ante, at 13–14. And
the majority creates a new exception to the warrant re-
quirement to justify warrantless entry short of exigency in
potential domestic abuse situations. Ibid.
   Considering the majority’s rule is solely concerned with
protecting a person who happens to be present at the door
when a police officer asks his co-occupant for consent to
search, but not one who is asleep in the next room or in
the backyard gardening, the majority has taken a great
deal of pain in altering Fourth Amendment doctrine, for
precious little (if any) gain in privacy. Perhaps one day, as
the consequences of the majority’s analytic approach
become clearer, today’s opinion will be treated the same
16                 GEORGIA v. RANDOLPH

                    ROBERTS, C. J., dissenting

way the majority treats our opinions in Matlock and Rod-
riguez—as a “loose end” to be tied up. Ante, at 17.
   One of the concurring opinions states that if it had to
choose between a rule that a cotenant’s consent was valid or
a rule that it was not, it would choose the former. Ante, at 1
(opinion of BREYER, J.). The concurrence advises, however,
that “no single set of legal rules can capture the ever chang-
ing complexity of human life,” ibid., and joins what becomes
the majority opinion, “[g]iven the case-specific nature of the
Court’s holding,” ante, at 3. What the majority establishes,
in its own terms, is “the rule that a physically present in-
habitant’s express refusal of consent to a police search is
dispositive as to him, regardless of the consent of a fellow
occupant.” Ante, at 18 (emphases added). The concurrence
joins with the apparent “understandin[g]” that the major-
ity’s “rule” is not a rule at all, but simply a “case-specific”
holding. Ante, at 3 (opinion of BREYER, J.). The end result
is a complete lack of practical guidance for the police in the
field, let alone for the lower courts.
                         *     *    *
  Our third-party consent cases have recognized that a
person who shares common areas with others “assume[s]
the risk that one of their number might permit the common
area to be searched.” Matlock, 415 U. S., at 171, n. 7. The
majority reminds us, in high tones, that a man’s home is his
castle, ante, at 10, but even under the majority’s rule, it is
not his castle if he happens to be absent, asleep in the keep,
or otherwise engaged when the constable arrives at the
gate. Then it is his co-owner’s castle. And, of course, it is
not his castle if he wants to consent to entry, but his co-
owner objects. Rather than constitutionalize such an arbi-
trary rule, we should acknowledge that a decision to share
a private place, like a decision to share a secret or a confi-
dential document, necessarily entails the risk that those
with whom we share may in turn choose to share—for their
                 Cite as: 547 U. S. ____ (2006)        17

                   ROBERTS, C. J., dissenting

own protection or for other reasons—with the police.
  I respectfully dissent.
                  Cite as: 547 U. S. ____ (2006)             1

                      SCALIA, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 04–1067
                          _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                        [March 22, 2006]

   JUSTICE SCALIA, dissenting.
   I join the dissent of THE CHIEF JUSTICE, but add these
few words in response to JUSTICE STEVENS’ concurrence.
   It is not as clear to me as it is to JUSTICE STEVENS that,
at the time the Fourth Amendment was adopted, a police
officer could enter a married woman’s home over her
objection, and could not enter with only her consent. Nor
is it clear to me that the answers to these questions de-
pended solely on who owned the house. It is entirely clear,
however, that if the matter did depend solely on property
rights, a latter-day alteration of property rights would also
produce a latter-day alteration of the Fourth Amendment
outcome—without altering the Fourth Amendment itself.
   JUSTICE STEVENS’ attempted critique of originalism
confuses the original import of the Fourth Amendment
with the background sources of law to which the Amend-
ment, on its original meaning, referred. From the date of
its ratification until well into the 20th century, violation of
the Amendment was tied to common-law trespass. See
Kyllo v. United States, 533 U. S. 27, 31–32 (2001); see also
California v. Acevedo, 500 U. S. 565, 581, 583 (1991)
(SCALIA, J., concurring in judgment). On the basis of that
connection, someone who had power to license the search
of a house by a private party could authorize a police
search. See 1 Restatement of Torts §167, and Comment b
(1934); see also Williams v. Howard, 110 S. C. 82, 96 S. E.
2                  GEORGIA v. RANDOLPH

                     SCALIA, J., dissenting

251 (1918); Fennemore v. Armstrong, 29 Del. 35, 96 A. 204
(Super. Ct. 1915). The issue of who could give such con-
sent generally depended, in turn, on “historical and legal
refinements” of property law. United States v. Matlock,
415 U. S. 164, 171, n. 7 (1974). As property law developed,
individuals who previously could not authorize a search
might become able to do so, and those who once could grant
such consent might no longer have that power. But changes
in the law of property to which the Fourth Amendment
referred would not alter the Amendment’s meaning: that
anyone capable of authorizing a search by a private party
could consent to a warrantless search by the police.
   There is nothing new or surprising in the proposition
that our unchanging Constitution refers to other bodies of
law that might themselves change. The Fifth Amendment
provides, for instance, that “private property” shall not “be
taken for public use, without just compensation”; but it
does not purport to define property rights. We have con-
sistently held that “the existence of a property interest is
determined by reference to ‘existing rules or understand-
ings that stem from an independent source such as state
law.’ ” Phillips v. Washington Legal Foundation, 524 U. S.
156, 164 (1998) (quoting Board of Regents of State Colleges
v. Roth, 408 U. S. 564, 577 (1972)). The same is true of the
Fourteenth Amendment Due Process Clause’s protection of
“property.” See Castle Rock v. Gonzales, 545 U. S. ___, ___
(2005). This reference to changeable law presents no prob-
lem for the originalist. No one supposes that the meaning of
the Constitution changes as States expand and contract
property rights. If it is indeed true, therefore, that a wife
in 1791 could not authorize the search of her husband’s
house, the fact that current property law provides other-
wise is no more troublesome for the originalist than the
well established fact that a State must compensate its
takings of even those property rights that did not exist at
the time of the Founding.
                 Cite as: 547 U. S. ____ (2006)          3

                     SCALIA, J., dissenting

  In any event, JUSTICE STEVENS’ panegyric to the equal
rights of women under modern property law does not
support his conclusion that “[a]ssuming . . . both spouses
are competent, neither one is a master possessing the
power to override the other’s constitutional right to deny
entry to their castle.” Ante, at 2–3. The issue at hand is
what to do when there is a conflict between two equals.
Now that women have authority to consent, as JUSTICE
STEVENS claims men alone once did, it does not follow that
the spouse who refuses consent should be the winner of the
contest. JUSTICE STEVENS could just as well have followed
the same historical developments to the opposite conclu-
sion: Now that “the male and the female are equal part-
ners,” ante, at 2, and women can consent to a search of
their property, men can no longer obstruct their wishes.
Men and women are no more “equal” in the majority’s
regime, where both sexes can veto each other’s consent,
than on the dissent’s view, where both sexes cannot.
  Finally, I must express grave doubt that today’s decision
deserves JUSTICE STEVENS’ celebration as part of the
forward march of women’s equality. Given the usual
patterns of domestic violence, how often can police be
expected to encounter the situation in which a man urges
them to enter the home while a woman simultaneously
demands that they stay out? The most common practical
effect of today’s decision, insofar as the contest between
the sexes is concerned, is to give men the power to stop
women from allowing police into their homes—which is,
curiously enough, precisely the power that JUSTICE
STEVENS disapprovingly presumes men had in 1791.
                 Cite as: 547 U. S. ____ (2006)           1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 04–1067
                         _________________


 GEORGIA, PETITIONER v. SCOTT FITZ RANDOLPH
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF
                       GEORGIA
                       [March 22, 2006]

  JUSTICE THOMAS, dissenting.
  The Court has long recognized that “[i]t is an act of
responsible citizenship for individuals to give whatever
information they may have to aid in law enforcement.”
Miranda v. Arizona, 384 U. S. 436, 477–478 (1966). Con-
sistent with this principle, the Court held in Coolidge v.
New Hampshire, 403 U. S. 443 (1971), that no Fourth
Amendment search occurs where, as here, the spouse of an
accused voluntarily leads the police to potential evidence
of wrongdoing by the accused. Id., at 486–490. Because
Coolidge squarely controls this case, the Court need not
address whether police could permissibly have conducted a
general search of the Randolph home, based on Mrs.
Randolph’s consent. I respectfully dissent.
  In the instant case, Mrs. Randolph told police respond-
ing to a domestic dispute that respondent was using a
substantial quantity of cocaine. Upon police request, she
consented to a general search of her residence to investi-
gate her statements. However, as the Court’s recitation of
the facts demonstrates, ante, at 2, the record is clear that
no such general search occurred. Instead, Sergeant Brett
Murray asked Mrs. Randolph where the cocaine was
located, and she showed him to an upstairs bedroom,
where he saw the “piece of cut straw” on a dresser. Cor-
rected Tr. of Motion to Suppression Hearing in Case No.
2001R–699 (Super. Ct. Sumter Cty., Ga., Oct. 3, 2002), pp.
2                 GEORGIA v. RANDOLPH

                    THOMAS, J., dissenting

8–9. Upon closer examination, Sergeant Murray observed
white residue on the straw, and concluded the straw had
been used for ingesting cocaine. Id., at 8. He then col-
lected the straw and the residue as evidence. Id., at 9.
   Sergeant Murray’s entry into the Randolphs’ home at
the invitation of Mrs. Randolph to be shown evidence of
respondent’s cocaine use does not constitute a Fourth
Amendment search. Under this Court’s precedents, only
the action of an agent of the government can constitute a
search within the meaning of the Fourth Amendment,
because that Amendment “was intended as a restraint
upon the activities of sovereign authority, and was not
intended to be a limitation upon other than governmental
agencies.” Burdeau v. McDowell, 256 U. S. 465, 475 (1921)
(emphasis added). See also Coolidge, 403 U. S., at 487.
Applying this principle in Coolidge, the Court held that
when a citizen leads police officers into a home shared
with her spouse to show them evidence relevant to their
investigation into a crime, that citizen is not acting as an
agent of the police, and thus no Fourth Amendment search
has occurred. Id., at 488–498.
   Review of the facts in Coolidge clearly demonstrates
that it governs this case. While the police interrogated
Coolidge as part of their investigation into a murder, two
other officers were sent to his house to speak with his
wife. Id., at 485. During the course of questioning Mrs.
Coolidge, the police asked whether her husband owned
any guns. Id., at 486. Mrs. Coolidge replied in the af-
firmative, and offered to retrieve the weapons for the
police, apparently operating under the assumption that
doing so would help to exonerate her husband. Ibid. The
police accompanied Mrs. Coolidge to the bedroom to collect
the guns, as well as clothing that Mrs. Coolidge told them
her husband had been wearing the night of the murder.
Ibid.
   Before this Court, Coolidge argued that the evidence of
                     Cite as: 547 U. S. ____ (2006)                     3

                         THOMAS, J., dissenting

the guns and clothing should be suppressed as the product
of an unlawful search because Mrs. Coolidge was acting as
an “ ‘instrument,’ ” or agent, of the police by complying
with a “ ‘demand’ ” made by them. Id., at 487. The Court
recognized that, had Mrs. Coolidge sought out the guns to
give to police wholly on her own initiative, “there can be no
doubt under existing law that the articles would later
have been admissible in evidence.” Ibid. That she did so
in cooperation with police pursuant to their request did
not transform her into their agent; after all, “it is no part
of the policy underlying the Fourth and Fourteenth
Amendments to discourage citizens from aiding to the
utmost of their ability in the apprehension of criminals.”
Id., at 488. Because the police were “acting normally and
properly” when they asked about any guns, and question-
ing Mrs. Coolidge about the clothing was “logical and in no
way coercive,” the Fourth Amendment did not require
police to “avert their eyes” when Mrs. Coolidge produced
the guns and clothes for inspection.1 Id., at 488–489.
   This case is indistinguishable from Coolidge, compelling
the conclusion that Mrs. Randolph was not acting as an
agent of the police when she admitted Sergeant Murray
into her home and led him to the incriminating evidence.2
——————
  1 Although  the Court has described Coolidge as a “third-party con-
sent” case, United States v. Matlock, 415 U. S. 164, 171 (1974), the
Court’s opinion, by its own terms, does not rest on its conception of Mrs.
Coolidge’s authority to consent to a search of her house or the possible
relevance of Mr. Coolidge’s absence from the scene. Coolidge, 403 U. S.,
at 487 (“[W]e need not consider the petitioner’s further argument that
Mrs. Coolidge could not or did not ‘waive’ her husband’s constitutional
protection against unreasonable searches and seizures”). See also
Walter v. United States, 447 U. S. 649, 660–661, n. 2 (1980) (White, J.,
concurring in part and concurring in judgment) (“Similarly, in Coolidge
v. New Hampshire, the Court held that a wife’s voluntary action in
turning over to police her husband’s guns and clothing did not consti-
tute a search and seizure by the government”).
  2 The Courts of Appeals have disagreed over the appropriate inquiry
4                     GEORGIA v. RANDOLPH

                        THOMAS, J., dissenting

Just as Mrs. Coolidge could, of her own accord, have of-
fered her husband’s weapons and clothing to the police
without implicating the Fourth Amendment, so too could
Mrs. Randolph have simply retrieved the straw from the
house and given it to Sergeant Murray. Indeed, the ma-
jority appears to concede as much. Ante, at 11-12 (“The co-
tenant acting on his own initiative may be able to deliver
evidence to the police, Coolidge, supra, at 487–489 . . . ,
and can tell the police what he knows, for use before a
magistrate in getting a warrant”). Drawing a constitu-
tionally significant distinction between what occurred here
and Mrs. Randolph’s independent production of the rele-
vant evidence is both inconsistent with Coolidge and
unduly formalistic.3
   Accordingly, the trial court appropriately denied re-
spondent’s motion to suppress the evidence Mrs. Randolph
provided to the police and the evidence obtained as a
result of the consequent search warrant. I would therefore
reverse the judgment of the Supreme Court of Georgia.




——————
to be performed in determining whether involvement of the police
transforms a private individual into an agent or instrument of the
police. See United States v. Pervaz, 118 F. 3d 1, 5–6 (CA1 1997) (sum-
marizing approaches of various Circuits). The similarity between this
case and Coolidge avoids any need to resolve this broader dispute in the
present case.
  3 That Sergeant Murray, unlike the officers in Coolidge, may have

intended to perform a general search of the house is inconsequential, as
he ultimately did not do so; he viewed only those items shown to him by
Mrs. Randolph. Nor is it relevant that, while Mrs. Coolidge intended to
aid the police in apprehending a criminal because she believed doing so
would exonerate her husband, Mrs. Randolph believed aiding the police
would implicate her husband.

```

---

## GROUP: _overhaul2/lake/cases/Gerstein v. Pugh.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Gerstein v. Pugh"
type: case
citation: "420 U.S. 103 (1975)"
parallel_cite: "95 S. Ct. 854; 43 L. Ed. 2d 54; 19 Fed. R. Serv. 2d 1499"
neutral_cite: 1975 U.S. LEXIS 29
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1975
date_decided: 1975-02-18
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1975-02-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Gerstein v. Pugh
  varies_by_point: false
  scope_note: "Good law. The Fourth Amendment requires a prompt judicial determination of probable cause as a prerequisite to extended pretrial detention of a person arrested without a warrant; the determination need not be adversarial. Implemented by County of Riverside v. McLaughlin (48-hour presumption)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109186/gerstein-v-pugh/"
  cluster_id: 109186
  opinion_id: 9425988
  identity_checked: true
homes:
  - page: "[[Prompt Probable-Cause Determination]]"
    role: "Key — Anchor (prompt judicial PC determination after a warrantless arrest)"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[County of Riverside v. McLaughlin]]", "[[Coolidge v. New Hampshire]]", "[[Payton v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "arrest", "probable-cause", "pretrial-detention", "gerstein-hearing"]
holding: "A person arrested without a warrant is entitled under the Fourth Amendment to a prompt judicial determination of probable cause as a prerequisite to any extended pretrial restraint of liberty; the determination need not be an adversary hearing."
lake:
  record_id: Gerstein v. Pugh
  status: verified
  projected_at: 2026-07-09
---

# Gerstein v. Pugh

*420 U.S. 103 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Under Florida procedure, a person arrested without a warrant and charged by a prosecutor's information could be jailed or otherwise restrained pending trial without any judicial determination of probable cause. Pugh and other detainees, held on informations without any such hearing, brought a class action challenging the practice. The State defended on the ground that the prosecutor's decision to file an information was itself a sufficient determination of probable cause to justify detention.

## Issue
Whether the Fourth Amendment requires a judicial determination of probable cause before a person arrested without a warrant may be subjected to extended pretrial detention, and if so, whether that determination must take the form of an adversary hearing.

## Rule
A prompt judicial probable-cause determination is required. An officer's on-scene probable cause justifies the arrest and a brief booking detention, but not prolonged custody: "a policeman's on-the-scene assessment of probable cause provides legal justification for arresting a person suspected of crime, and for a brief period of detention to take the administrative steps incident to arrest. Once the suspect is in custody, however, the reasons that justify dispensing with the magistrate's neutral judgment evaporate." — 420 U.S. at 113–114. ^pin-113

"Accordingly, we hold that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest." — [*Id.* at 114](https://www.courtlistener.com/opinion/109186/gerstein-v-pugh/#:~:text=Accordingly%2C%20we%20hold%20that%20the). ^pin-114

The hearing may be informal and need not be adversarial, but it must be prompt: "it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty, and this determination must be made by a judicial officer either before or promptly after arrest." — *Id.* at 125. ^pin-125

## Application
Florida's reliance on the prosecutor's information could not satisfy the Fourth Amendment, because a prosecutor — charged with law enforcement — is not the "neutral and detached" magistrate the Constitution requires (per *[[Coolidge v. New Hampshire|Coolidge]]* and *Shadwick*). A warrantless arrestee held only on an information therefore received no constitutionally adequate probable-cause check. The Court required a prompt judicial determination but rejected the District Court's decree to the extent it demanded a full adversary hearing, holding the probable-cause determination need not afford counsel, confrontation, or cross-examination.

## Conclusion
The Fourth Amendment requires a timely judicial determination of probable cause as a prerequisite to extended pretrial detention of a warrantless arrestee, so Florida's information-only procedure was invalid; but because the determination need not be adversarial, the judgment was affirmed in part and reversed in part. This requirement is the "Gerstein hearing."

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Gerstein*'s "promptly after arrest" requirement is implemented by [[County of Riverside v. McLaughlin]], which set a presumptive 48-hour window for the judicial probable-cause determination. The neutral-magistrate principle traces to [[Coolidge v. New Hampshire]]; *Gerstein* concerns post-arrest detention and is distinct from the in-home arrest-warrant rule of [[Payton v. New York]].

## Appears on
- [[Prompt Probable-Cause Determination]] — *Key — Anchor*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Gerstein v. Pugh*, 420 U.S. 103 (1975) — https://www.courtlistener.com/opinion/109186/gerstein-v-pugh/ — pinpoints: 113–114, 125.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e76706f94adf2c09", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Gerstein v. Pugh"}, "payload": {"all": [{"cite": "420 U.S. 103", "page": "103", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "420"}, {"cite": "95 S. Ct. 854", "page": "854", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "95"}, {"cite": "43 L. Ed. 2d 54", "page": "54", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "43"}, {"cite": "1975 U.S. LEXIS 29", "page": "29", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1975"}, {"cite": "19 Fed. R. Serv. 2d 1499", "page": "1499", "reporter": "Fed. R. Serv. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "19"}], "display": "420 U.S. 103", "official": {"cite": "420 U.S. 103", "page": "103", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "420"}, "official_selection_present": true, "record_id": "Gerstein v. Pugh"}}
{"assertion_id": "36cb1f8305b40c8a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-114", "record_id": "Gerstein v. Pugh"}, "payload": {"fragment": "#:~:text=Accordingly%2C%20we%20hold%20that%20the", "page": null, "pin_id": "pin-114", "pinpoint_status": "star-verified", "quote": "Accordingly, we hold that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest.", "quote_fidelity": "matched", "record_id": "Gerstein v. Pugh", "star_marker": "114"}}
{"assertion_id": "bbc2a8fbf5f6f621", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-125", "record_id": "Gerstein v. Pugh"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-125", "pinpoint_status": "slip-only", "quote": "it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty, and this determination must be made by a judicial officer either before or promptly after arrest.", "quote_fidelity": "mismatch", "record_id": "Gerstein v. Pugh", "star_marker": null}}
{"assertion_id": "fcb6c8b14eeeff05", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-113", "record_id": "Gerstein v. Pugh"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-113", "pinpoint_status": "slip-only", "quote": "--- # Gerstein v. Pugh *420 U.S. 103 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Under Florida procedure, a person arrested without a warrant and charged by a prosecutor's information could be jailed or otherwise restrained pending trial without any judicial determination of probable cause. Pugh and other detainees, held on informations without any such hearing, brought a class action challenging the practice. The State defended on the ground that the prosecutor's decision to file an information was itself a sufficient determination of probable cause to justify detention. ## Issue Whether the Fourth Amendment requires a judicial determination of probable cause before a person arrested without a warrant may be subjected to extended pretrial detention, and if so, whether that determination must take the form of an adversary hearing. ## Rule A prompt judicial probable-cause determination is required. An officer's on-scene probable cause justifies the arrest and a brief booking detention, but not prolonged custody:", "quote_fidelity": "mismatch", "record_id": "Gerstein v. Pugh", "star_marker": null}}
{"assertion_id": "0f08164b8325ca7d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Gerstein v. Pugh"}, "payload": {"as_of_content": "1975-02-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Gerstein v. Pugh", "scope_note": "Good law. The Fourth Amendment requires a prompt judicial determination of probable cause as a prerequisite to extended pretrial detention of a person arrested without a warrant; the determination need not be adversarial. Implemented by County of Riverside v. McLaughlin (48-hour presumption).", "varies_by_point": false}}
```

### lake record — Gerstein v. Pugh

```json
{
  "schema_version": "s2.v1",
  "record_id": "Gerstein v. Pugh",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Gerstein v. Pugh",
    "case_name_short": "Gerstein",
    "case_name_full": "GERSTEIN v. PUGH Et Al.",
    "input_case_name": "Gerstein v. Pugh",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1975-02-18",
    "year": 1975,
    "docket": null,
    "cluster_id": 109186,
    "lead_opinion_id": 9425988,
    "sibling_ids": [
      109186,
      9425988,
      9425989
    ],
    "absolute_url": "/opinion/109186/gerstein-v-pugh/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "420 U.S. 103",
      "volume": "420",
      "reporter": "U.S.",
      "page": "103",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "95 S. Ct. 854",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "43 L. Ed. 2d 54",
        "volume": "43",
        "reporter": "L. Ed. 2d",
        "page": "54",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 Fed. R. Serv. 2d 1499",
        "volume": "19",
        "reporter": "Fed. R. Serv. 2d",
        "page": "1499",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1975 U.S. LEXIS 29",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "29",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "420 U.S. 103",
        "volume": "420",
        "reporter": "U.S.",
        "page": "103",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 S. Ct. 854",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "854",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "43 L. Ed. 2d 54",
        "volume": "43",
        "reporter": "L. Ed. 2d",
        "page": "54",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1975 U.S. LEXIS 29",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "29",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "19 Fed. R. Serv. 2d 1499",
        "volume": "19",
        "reporter": "Fed. R. Serv. 2d",
        "page": "1499",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "420 U.S. 103",
    "official_selection": {
      "court_class": "scotus",
      "selected": "420 U.S. 103",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-113",
      "page": null,
      "quote": "--- # Gerstein v. Pugh *420 U.S. 103 (1975)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Under Florida procedure, a person arrested without a warrant and charged by a prosecutor's information could be jailed or otherwise restrained pending trial without any judicial determination of probable cause. Pugh and other detainees, held on informations without any such hearing, brought a class action challenging the practice. The State defended on the ground that the prosecutor's decision to file an information was itself a sufficient determination of probable cause to justify detention. ## Issue Whether the Fourth Amendment requires a judicial determination of probable cause before a person arrested without a warrant may be subjected to extended pretrial detention, and if so, whether that determination must take the form of an adversary hearing. ## Rule A prompt judicial probable-cause determination is required. An officer's on-scene probable cause justifies the arrest and a brief booking detention, but not prolonged custody:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-114",
      "page": null,
      "quote": "Accordingly, we hold that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest.",
      "star_marker": "114",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17194,
      "fragment": "#:~:text=Accordingly%2C%20we%20hold%20that%20the",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-125",
      "page": null,
      "quote": "it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty, and this determination must be made by a judicial officer either before or promptly after arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1975-02-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Gerstein v. Pugh",
    "varies_by_point": false,
    "scope_note": "Good law. The Fourth Amendment requires a prompt judicial determination of probable cause as a prerequisite to extended pretrial detention of a person arrested without a warrant; the determination need not be adversarial. Implemented by County of Riverside v. McLaughlin (48-hour presumption).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Winegarner",
          "cluster_id": 9372588,
          "cite": [
            "208 N.E.3d 88",
            "2023 Ohio 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Preston P., a juvenile",
          "cluster_id": 4692950,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell v. Wolfish",
          "cluster_id": 110075,
          "cite": [
            "60 L. Ed. 2d 447",
            "99 S. Ct. 1861",
            "441 U.S. 520",
            "1979 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Salerno",
          "cluster_id": 111891,
          "cite": [
            "95 L. Ed. 2d 697",
            "107 S. Ct. 2095",
            "481 U.S. 739",
            "1987 U.S. LEXIS 2259",
            "55 U.S.L.W. 4663"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hewitt v. Helms",
          "cluster_id": 110829,
          "cite": [
            "74 L. Ed. 2d 675",
            "103 S. Ct. 864",
            "459 U.S. 460",
            "1983 U.S. LEXIS 3",
            "51 U.S.L.W. 4124"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Middlesex County Ethics Committee v. Garden State Bar Ass'n",
          "cluster_id": 110750,
          "cite": [
            "73 L. Ed. 2d 116",
            "102 S. Ct. 2515",
            "457 U.S. 423",
            "1982 U.S. LEXIS 2638",
            "50 U.S.L.W. 4712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ingraham v. Wright",
          "cluster_id": 109635,
          "cite": [
            "51 L. Ed. 2d 711",
            "97 S. Ct. 1401",
            "430 U.S. 651",
            "1977 U.S. LEXIS 74"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Mosley",
          "cluster_id": 109336,
          "cite": [
            "46 L. Ed. 2d 313",
            "96 S. Ct. 321",
            "423 U.S. 96",
            "1975 U.S. LEXIS 100"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wilkinson v. Austin",
          "cluster_id": 799975,
          "cite": [
            "162 L. Ed. 2d 174",
            "125 S. Ct. 2384",
            "545 U.S. 209",
            "2005 U.S. LEXIS 4839"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reno v. Flores",
          "cluster_id": 112833,
          "cite": [
            "123 L. Ed. 2d 1",
            "113 S. Ct. 1439",
            "507 U.S. 292",
            "1993 U.S. LEXIS 2399"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States Parole Commission v. Geraghty",
          "cluster_id": 110228,
          "cite": [
            "63 L. Ed. 2d 479",
            "100 S. Ct. 1202",
            "445 U.S. 388",
            "1980 U.S. LEXIS 12",
            "29 Fed. R. Serv. 2d 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Hunt",
          "cluster_id": 110660,
          "cite": [
            "71 L. Ed. 2d 353",
            "102 S. Ct. 1181",
            "455 U.S. 478",
            "1982 U.S. LEXIS 77"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Vasquez v. Hillery",
          "cluster_id": 111552,
          "cite": [
            "88 L. Ed. 2d 598",
            "106 S. Ct. 617",
            "474 U.S. 254",
            "1986 U.S. LEXIS 40",
            "54 U.S.L.W. 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Riverside v. McLaughlin",
          "cluster_id": 112585,
          "cite": [
            "114 L. Ed. 2d 49",
            "111 S. Ct. 1661",
            "500 U.S. 44",
            "1991 U.S. LEXIS 2528"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Castaneda v. Partida",
          "cluster_id": 109627,
          "cite": [
            "51 L. Ed. 2d 498",
            "97 S. Ct. 1272",
            "430 U.S. 482",
            "1977 U.S. LEXIS 67"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
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
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Sims",
          "cluster_id": 110105,
          "cite": [
            "60 L. Ed. 2d 994",
            "99 S. Ct. 2371",
            "442 U.S. 415",
            "1979 U.S. LEXIS 110"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Gerstein v. Pugh:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109186 OR 9425988 OR 9425989) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI3NTUyMDAwMDAwJnM9NDUwMjIxMCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109186+OR+9425988+OR+9425989%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(109186 OR 9425988 OR 9425989)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05ODcmcz0xMTE1OTgmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109186+OR+9425988+OR+9425989%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109186 OR 9425988 OR 9425989)",
        "reviewed": 83,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 83,
        "triage_read": 0,
        "triage_snippet_classified": 83
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109186 OR 9425988 OR 9425989)",
    "indexed_citing_opinions": 2518,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109186,
        "count": 2222,
        "count_source": "search"
      },
      {
        "opinion_id": 9425988,
        "count": 333,
        "count_source": "search"
      },
      {
        "opinion_id": 9425989,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4362,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/gerstein-v-pugh.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxNzAwMjcmcz0xMDMxNDQ2MCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109186+OR+9425988+OR+9425989%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109186,
        "cited_id": 91470,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 91772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 97944,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 98209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 100977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 101974,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 103791,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 104977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105749,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105820,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106087,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106391,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107058,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107394,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108266,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108341,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108606,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108772,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108785,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109097,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109136,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 109137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 279699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 286155,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 296631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 306786,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 313021,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1447830,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1624670,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1628605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1720793,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1724472,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1725389,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1764878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1795762,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1807359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109186,
        "cited_id": 1843924,
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
    "date_created": "2026-07-05T05:22:22Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:27:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:22:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Gerstein v. Pugh

```
<opinion type="majority">
<author id="b191-4"><page-number citation-index="1" label="105">*105</page-number>Mr. Justice Powell</author>
<p id="AnR">delivered the opinion of the Court.</p>
<p id="b191-5">The issue in this case is whether a person arrested and held for trial under a prosecutor’s information is constitutionally entitled to a judicial determination of probable cause for pretrial restraint of liberty.</p>
<p id="b191-6">I</p>
<p id="b191-7">In March 1971 respondents Pugh and Henderson were arrested in Dade County, Fla. Each was charged with several offenses under a prosecutor’s information.<footnotemark>1</footnotemark> Pugh was denied bail because one of the charges against him carried a potential life sentence, and Henderson remained in custody because he was unable to post a $4,500 bond.</p>
<p id="b191-8">In Florida, indictments are required only for prosecution of capital offenses. Prosecutors may charge all other crimes by information, without a prior preliminary hearing and without obtaining leave of court. Fla. Rule Crim. Proc. 3.140 (a); <em>State </em>v. <em>Hernandez, </em><span class="citation" data-id="1628605"><a href="/opinion/1628605/state-v-hernandez/" aria-description="Citation for case: State v. Hernandez">217 So. 2d 109</a></span> (Fla. 1968); <em>Di Bona </em>v. <em>State, </em><span class="citation" data-id="1720793"><a href="/opinion/1720793/di-bona-v-state/" aria-description="Citation for case: Di Bona v. State">121 So. 2d 192</a></span> (Fla. App. 1960). At the time respondents were arrested, a Florida rule seemed to authorize adversary preliminary hearings to test probable cause for detention in all cases. Fla. Rule Crim. Proc. 1.122 (before amendment in 1972). <page-number citation-index="1" label="106">*106</page-number>But the Florida courts had held that the filing of an information foreclosed the suspect’s right to a preliminary-hearing. See <em>State ex rel. Hardy </em>v. <em>Blount, </em><span class="citation" data-id="1764878"><a href="/opinion/1764878/state-ex-rel-hardy-v-blount/" aria-description="Citation for case: State Ex Rel. Hardy v. Blount">261 So. 2d 172</a></span> (Fla. 1972).<footnotemark>2</footnotemark> They had also held that habeas corpus could not be used, except perhaps in exceptional circumstances, to test the probable cause for detention under an information. See <em>Sullivan </em>v. <em>State ex rel. McCrory, </em><span class="citation" data-id="1843924"><a href="/opinion/1843924/sullivan-v-state-ex-rel-mccrory/#797" aria-description="Citation for case: Sullivan v. State Ex Rel. McCrory">49 So. 2d 794, 797</a></span> (Fla. 1951). The only possible methods for obtaining a judicial determination of probable cause were a special statute allowing a preliminary hearing after 30 days, <span class="citation no-link">Fla. Stat. Ann. §907.045</span> (1973),<footnotemark>3</footnotemark> and arraignment, which the District Court found was often delayed a month or more after arrest. <em>Pugh </em>v. <em>Rainwater, </em><span class="citation" data-id="1624670"><a href="/opinion/1624670/pugh-v-rainwater/#1110" aria-description="Citation for case: Pugh v. Rainwater">332 F. Supp. 1107, 1110</a></span> (SD Fla. 1971).<footnotemark>4</footnotemark> As a result, a person charged by information could be detained for a substantial period solely on the decision of a prosecutor.</p>
<p id="b192-5">Respondents Pugh and Henderson filed a class action against Dade County officials in the Federal District <page-number citation-index="1" label="107">*107</page-number>Court,<footnotemark>5</footnotemark> claiming a constitutional right to a judicial hearing on the issue of probable cause and requesting declaratory and injunctive relief.<footnotemark>6</footnotemark> Respondents Turner and Faulk, also in custody under informations, subsequently intervened.<footnotemark>7</footnotemark> Petitioner Gerstein, the State Attorney for Dade County, was one of several defendants.<footnotemark>8</footnotemark></p>
<p id="b193-5">After an initial delay while the Florida Legislature considered a bill that would have afforded preliminary hearings to persons charged by information, the District Court granted the relief sought. <em>Pugh </em>v. <em><span class="citation" data-id="1624670"><a href="/opinion/1624670/pugh-v-rainwater/" aria-description="Citation for case: Pugh v. Rainwater">Rainwater, supra.</a></span> </em>The court certified the case as a class action under Fed. Rule Civ. Proc. 23 (b) (2), and held that the Fourth and Fourteenth Amendments give all arrested persons charged by information a right to a judicial hearing on the question of probable cause. The District Court ordered the Dade County defendants to give the named plaintiffs an immediate preliminary hearing to determine probable <page-number citation-index="1" label="108">*108</page-number>cause for further detention.<footnotemark>9</footnotemark> It also ordered them to submit a plan providing preliminary hearings in all cases instituted by information.</p>
<p id="b194-5">The defendants submitted a plan prepared by Sheriff E. Wilson Purdy, and the District Court adopted it with modifications. The final order prescribed a detailed post-arrest procedure. <span class="citation" data-id="1795762"><a href="/opinion/1795762/pugh-v-rainwater/" aria-description="Citation for case: Pugh v. Rainwater">336 F. Supp. 490</a></span> (SD Fla. 1972). Upon arrest the accused would be taken before a magistrate for a “first appearance hearing.” The magistrate would explain the charges, advise the accused of his rights, appoint counsel if he was indigent, and proceed with a probable cause determination unless either the prosecutor or the accused was unprepared. If either requested more time, the magistrate would set the date for a “preliminary hearing,” to be held within four days if the accused was in custody and within 10 days if he had been released pending trial. The order provided sanctions for failure to hold the hearing at prescribed times. At the “preliminary hearing” the accused would be entitled to counsel, and he would be allowed to confront and cross-examine adverse witnesses, to summon favorable witnesses, and to have a transcript made on request. If the magistrate found no probable cause, the accused would be discharged. He then could not be charged with the same offense by complaint or information, but only by indictment returned within 30 days.</p>
<p id="b195-4"><page-number citation-index="1" label="109">*109</page-number>The Court of Appeals for the Fifth Circuit stayed the District Court's order pending appeal, but while the case was awaiting decision, the Dade County judiciary voluntarily adopted a similar procedure of its own. Upon learning of this development, the Court of Appeals remanded the case for specific findings on the constitutionality of the new Dade County system. Before the District Court issued its findings, however, the Florida Supreme Court amended the procedural rules governing preliminary hearings statewide, and the parties agreed that the District Court should direct its inquiry to the new rules rather than the Dade County procedures.</p>
<p id="b195-5">Under the amended rules every arrested person must be taken before a judicial officer within 24 hours. Fla. Rule Crim. Proc. 3.130 (b). This “first appearance” is similar to the “first appearance hearing” ordered by the District Court in all respects but the crucial one: the magistrate does not make a determination of probable cause. The rule amendments also changed the procedure for preliminary hearings, restricting them to felony charges and codifying the rule that no hearings are available to persons charged by information or indictment. Rule 3.131; see <em>In re Rule 3.131 </em>(b), <em>Florida Rules of Criminal Procedure, </em><span class="citation" data-id="1724472"><a href="/opinion/1724472/in-re-rule-3131-b-florida-rules-of-criminal-pro/" aria-description="Citation for case: In Re Rule 3.131 (B), Florida Rules of Criminal Pro.">289 So. 2d 3</a></span> (Fla. 1974).</p>
<p id="b195-6">In a supplemental opinion the District Court held that the amended rules had not answered the basic constitutional objection, since a defendant charged by information still could be detained pending trial without a judicial determination of probable cause. <span class="citation" data-id="1447830"><a href="/opinion/1447830/pugh-v-rainwater/" aria-description="Citation for case: Pugh v. Rainwater">355 F. Supp. 1286</a></span> (SD Fla. 1973). Reaffirming its original ruling, the District Court declared that the continuation of this practice was unconstitutional.<footnotemark>10</footnotemark> The Court of Appeals <page-number citation-index="1" label="110">*110</page-number>affirmed, <span class="citation multiple-matches"><a href="/c/F.%202d/483/778/">483 F. 2d 778</a></span> (1973), modifying the District Court’s decree in minor particulars and suggesting that the form of preliminary hearing provided by the amended Florida rules would be acceptable, as long as it was provided to all defendants in custody pending trial. <em>Id., </em>at 788-789.</p>
<p id="b196-5">State Attorney Gerstein petitioned for review, and we granted certiorari because of the importance of the issue.<footnotemark>11</footnotemark> <page-number citation-index="1" label="111">*111</page-number><span class="citation multiple-matches"><a href="/c/U.%20S./414/1062/">414 U. S. 1062</a></span> (1973). We affirm in part and reverse in part.</p>
<p id="b197-5">II</p>
<p id="b197-6">As framed by the proceedings below, this case presents two issues: whether a person arrested and held for trial on an information is entitled to a judicial determination of probable cause for detention, and if so, whether the adversary hearing ordered by the District Court and approved by the Court of Appeals is required by the Constitution.</p>
<p id="b197-7">A</p>
<p id="b197-8">Both the standards and procedures for arrest and detention have been derived from the Fourth Amendment and its common-law antecedents. See <em>Cupp </em>v. <em>Murphy, </em><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/#294" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291, 294-295</a></span> (1973); <em>Ex parte Bollman, </em><span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch 75</a></span> (1807); <em>Ex parte Burford, </em><span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span> (1806). The standard for arrest is probable cause, defined in terms of facts and circumstances “sufficient to warrant a prudent man in believing that the [suspect] had committed or was committing an offense.” <page-number citation-index="1" label="112">*112</page-number><em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91</a></span> (1964). See also <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-176</a></span> (1949). This standard, like those for searches and seizures, represents a necessary accommodation between the individual’s right to liberty and the State’s duty to control crime.</p>
<blockquote id="b198-5">“These long-prevailing standards seek to safeguard citizens from rash and unreasonable interferences with privacy and from unfounded charges of crime. They also seek to give fair leeway for enforcing the law in the community’s protection. Because many situations which confront officers in the course of executing their duties are more or less ambiguous, room must be allowed for some mistakes on their part. But the mistakes must be those of reasonable men, acting on facts leading sensibly to their conclusions of probability. The rule of probable cause is a practical, nontechnical conception affording the best compromise that has been found for accommodating these often opposing interests. Requiring more would unduly hamper law enforcement. To allow less would be to leave law-abiding citizens at the mercy of the officers’ whim or caprice.” <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States"><em>Id., </em>at 176</a></span>.</blockquote>
<p id="b198-6">To implement the Fourth Amendment’s protection against unfounded invasions of liberty and privacy, the Court has required that the existence of probable cause be decided by a neutral and detached magistrate whenever possible. The classic statement of this principle appears in <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948):</p>
<blockquote id="b198-7">“The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its pro<page-number citation-index="1" label="113">*113</page-number>tection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.”</blockquote>
<p id="b199-5">See also <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20-22</a></span> (1968).<footnotemark>12</footnotemark></p>
<p id="b199-6">Maximum protection of individual rights could be assured by requiring a magistrate’s review of the factual justification prior to any arrest, but such a requirement would constitute an intolerable handicap for legitimate law enforcement. Thus, while the Court has expressed a preference for the use of arrest warrants when feasible, <em>Beck </em>v. <em>Ohio, supra, </em>at 96; <em>Wong Sun </em>v. <em>United States, </em><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, 479-482</a></span> (1963), it has never invalidated an arrest supported by probable cause solely because the officers failed to secure a warrant. See <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963); <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/" aria-description="Citation for case: Draper v. United States">358 U. S. 307</a></span> (1959); <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#705" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 705</a></span> (1948).<footnotemark>13</footnotemark></p>
<p id="b199-7">Under this practical compromise, a policeman’s on-the-scene assessment of probable cause provides legal justifi<page-number citation-index="1" label="114">*114</page-number>cation for arresting a person suspected of crime, and for a brief period of detention to take the administrative steps incident to arrest. Once the suspect is in custody, however, the reasons that justify dispensing with the magistrate's neutral judgment evaporate. There no longer is any danger that the suspect will escape or commit further crimes while the police submit their evidence to a magistrate. And, while the State's reasons for taking summary action subside, the suspect's need for a neutral determination of probable cause increases significantly. The consequences of prolonged detention may be more serious than the interference occasioned by arrest. Pretrial confinement may imperil the suspect’s job, interrupt his source of income, and impair his family relationships. See R. Goldfarb, Ransom 32-91 (1965); L. Katz, Justice Is the Crime 51-62 (1972). Even pretrial release may be accompanied by burdensome conditions that effect a significant restraint of liberty. See, <em>e. g., </em><span class="citation no-link">18 U. S. C. §§ 3146</span> (a)(2), (5). When the stakes are this high, the detached judgment of a neutral magistrate is essential if the Fourth Amendment is to furnish meaningful protection from unfounded interference with liberty. Accordingly, we hold that the Fourth Amendment requires a judicial determination of probable cause as a prerequisite to extended restraint of liberty following arrest.</p>
<p id="b200-5">This result has historical support in the common law that has guided interpretation of the Fourth Amendment. See <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#149" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 149</a></span> (1925). At common law it was customary, if not obligatory, for an arrested person to be brought before a justice of the peace shortly after arrest. 2 M. Hale, Pleas of the Crown 77, 81, 95, 121 (1736); 2 W. Hawkins, Pleas of the Crown 116-117 (4th ed. 1762). See <em>siso Kurtz v. Moffitt, </em><span class="citation" data-id="91470"><a href="/opinion/91470/kurtz-v-moffitt/#498" aria-description="Citation for case: Kurtz v. Moffitt">115 U. S. 487, 498-499</a></span> (1885).<footnotemark>14</footnotemark> The justice of the peace <page-number citation-index="1" label="115">*115</page-number>would “examine” the prisoner and the witnesses to determine whether there was reason to believe the prisoner had committed a crime. If there was, the suspect would be committed to jail or bailed pending trial. If not, he would be discharged from custody. 1 M. Hale, <em>supra, </em>at 583-586; 2 W. Hawkins, <em>supra, </em>at 116-119; 1 J. Stephen, History of the Criminal Law of England 233 (1883).<footnotemark>15</footnotemark> The initial determination of probable cause also could be reviewed by higher courts on a writ of habeas corpus. 2 W. Hawkins, <em>supra, </em>at 112-115; 1 J. Stephen, <em>supra, </em>at 243; see <em>Ex parte Bollman, </em><span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/#97" aria-description="Citation for case: Ex Parte Bollman and Swartwout">4 Cranch, at 97-101</a></span>. This practice furnished the model for criminal procedure in America immediately following the adoption of the <page-number citation-index="1" label="116">*116</page-number>Fourth Amendment, see <span class="citation" data-id="9416259"><a href="/opinion/84842/ex-parte-bollman-and-swartwout/" aria-description="Citation for case: Ex Parte Bollman and Swartwout"><em>Ex parte Bollman, </em>supra;</a></span><footnotemark>16</footnotemark> <em>Ex parte Burford, </em><span class="citation" data-id="84827"><a href="/opinion/84827/ex-parte-burford/" aria-description="Citation for case: Ex Parte Burford">3 Cranch 448</a></span> (1806); <em>United States </em>v. <em>Hamilton, </em><span class="citation" data-id="84684"><a href="/opinion/84684/united-states-v-hamilton/" aria-description="Citation for case: United States v. Hamilton">3 Dall. 17</a></span> (1795), and there are indications that the Framers of the Bill of Rights regarded it as a model for a “reasonable” seizure. See <em>Draper </em>v. <em>United States, </em><span class="citation" data-id="9421741"><a href="/opinion/105820/draper-v-united-states/#317" aria-description="Citation for case: Draper v. United States">358 U. S., at 317-320</a></span> (Douglas, J., dissenting).<footnotemark>17</footnotemark></p>
<p id="b202-5">B</p>
<p id="b202-6">Under the Florida procedures challenged here, a person arrested without a warrant and charged by information may be jailed or subjected to other restraints pending trial without any opportunity for a probable cause determination.<footnotemark>18</footnotemark> Petitioner defends this practice on the <page-number citation-index="1" label="117">*117</page-number>ground that the prosecutor's decision to file an information is itself a determination of probable cause that furnishes sufficient reason to detain a defendant pending trial. Although a conscientious decision that the evidence warrants prosecution affords a measure of protection against unfounded detention, we do not think prosecutorial judgment standing alone meets the requirements of the Fourth Amendment. Indeed, we think the Court's previous decisions compel disapproval of the Florida procedure. In <em>Albrecht </em>v. <em>United States, </em><span class="citation" data-id="100977"><a href="/opinion/100977/albrecht-v-united-states/#5" aria-description="Citation for case: Albrecht v. United States">273 U. S. 1, 5</a></span> (1927), the Court held that an arrest warrant issued solely upon a United States Attorney’s information was invalid because the accompanying affidavits were defective. Although the Court’s opinion did not explicitly state that the prosecutor’s official oath could not furnish probable cause, that conclusion was implicit in the judgment that the arrest was illegal under the Fourth Amendment.<footnotemark>19</footnotemark> More recently, in <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#449" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 449-453</a></span> (1971), the Court held that a prosecutor’s responsibility to law enforcement is inconsistent with the constitutional role of a neutral and detached magistrate. We reaffirmed that principle in <em>Shad-</em><page-number citation-index="1" label="118">*118</page-number><em>wick </em>v. <em>City of Tampa, </em><span class="citation" data-id="108582"><a href="/opinion/108582/shadwick-v-city-of-tampa/" aria-description="Citation for case: Shadwick v. City of Tampa">407 U. S. 345</a></span> (1972), and held that probable cause for the issuance of an arrest warrant must be determined by someone independent of police and prosecution. See also <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#317" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 317</a></span> (1972).<footnotemark>20</footnotemark> The reason for this separation of functions was expressed by Mr. Justice Frankfurter in a similar context:</p>
<blockquote id="b204-5">“A democratic society, in which respect for the dignity of all men is central, naturally guards against the misuse of the law enforcement process. Zeal in tracking down crime is not in itself an assurance of soberness of judgment. Disinterestedness in law enforcement does not alone prevent disregard of cherished liberties. Experience has therefore counseled that safeguards must be provided against the dangers of the overzealous as well as the despotic. The awful instruments of the criminal law cannot be entrusted to a single functionary. The complicated process of criminal justice is therefore divided into different parts, responsibility for which is separately vested in the various participants upon whom the criminal law relies for its vindication.” <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#343" aria-description="Citation for case: McNabb v. United States">318 U. S. 332, 343</a></span> (1943).</blockquote>
<p id="b204-6">In holding that the prosecutor’s assessment of probable <page-number citation-index="1" label="119">*119</page-number>cause is not sufficient alone to justify restraint of liberty pending trial, we do not imply that the accused is entitled to judicial oversight or review of the decision to prosecute. Instead, we adhere to the Court’s prior holding that a judicial hearing is not prerequisite to prosecution by information. <em>Beck </em>v. <em>Washington, </em><span class="citation" data-id="9422400"><a href="/opinion/106391/beck-v-washington/#545" aria-description="Citation for case: Beck v. Washington">369 U. S. 541, 545</a></span> (1962); <em>Lem Woon </em>v. <em>Oregon, </em><span class="citation" data-id="97944"><a href="/opinion/97944/lem-woon-v-oregon/" aria-description="Citation for case: Lem Woon v. Oregon">229 U. S. 586</a></span> (1913). Nor do we retreat from the established rule that illegal arrest or detention does not void a subsequent conviction. <em>Frisbie </em>v. <em>Collins, </em><span class="citation" data-id="104977"><a href="/opinion/104977/frisbie-v-collins/" aria-description="Citation for case: Frisbie v. Collins">342 U. S. 519</a></span> (1952); <em>Ker </em>v. <em>Illinois, </em><span class="citation" data-id="91772"><a href="/opinion/91772/ker-v-illinois/" aria-description="Citation for case: Ker v. Illinois">119 U. S. 436</a></span> (1886). Thus, as the Court of Appeals noted below, although a suspect who is presently detained may challenge the probable cause for that confinement, a conviction will not be vacated on the ground that the defendant was detained pending trial without a determination of probable cause. 483 F. 2d, at 786-787. Compare <em>Scarbrough </em>v. <em>Dutton, </em><span class="citation" data-id="9453521"><a href="/opinion/279699/charlie-h-scarbrough-v-a-l-dutton-warden-georgia-state-prison/" aria-description="Citation for case: Charlie H. Scarbrough v. A. L. Dutton, Warden, Georgia...">393 F. 2d 6</a></span> (CA5 1968), with <em>Brown </em>v. <em>Fauntleroy, </em>143 U. S. App. D. C. 116, <span class="citation" data-id="9456898"><a href="/opinion/296631/larry-daniel-brown-v-honorable-john-fauntleroy/" aria-description="Citation for case: Larry Daniel Brown v. Honorable John Fauntleroy">442 F. 2d 838</a></span> (1971), and <em>Cooley </em>v. <em>Stone, </em>134 U. S. App. D. C. 317, <span class="citation" data-id="286155"><a href="/opinion/286155/ronald-clifton-cooley-v-william-j-stone/" aria-description="Citation for case: Ronald Clifton Cooley v. William J. Stone">414 F. 2d 1213</a></span> (1969).</p>
<p id="b205-5">Ill</p>
<p id="b205-6">Both the District Court and the Court of Appeals held that the determination of probable cause must be accompanied by the full panoply of adversary safeguards — counsel, confrontation, cross-examination, and compulsory process for witnesses. A full preliminary hearing of this sort is modeled after the procedure used in many States to determine whether the evidence justifies going to trial under an information or presenting the case to a grand jury. See <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970); Y. Kamisar, W. LaFave &amp; J. Israel, Modern Criminal Procedure 957-967, 996-1000 (4th ed. 1974). The standard of proof required of the prosecution is usually referred to as “probable cause,” but in some jurisdictions it may approach a prima facie case of guilt. <page-number citation-index="1" label="120">*120</page-number>ALI, Model Code of Pre-arraignment Procedure, Commentary on Art. 330, pp. 90-91 (Tent. Draft No. 5, 1972). When the hearing takes this form, adversary procedures are customarily employed. The importance of the issue to both the State and the accused justifies the presentation of witnesses and full exploration of their testimony on cross-examination. This kind of hearing also requires appointment of counsel for indigent defendants. <em>Coleman </em>v. <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Alabama, supra.</a></span> </em>And, as the hearing assumes increased importance and the procedures become more complex, the likelihood that it can be held promptly after arrest diminishes. See ALI, Model Code of Pre-arraignment Procedure, <em>supra, </em>at 33-34.</p>
<p id="b206-5">These adversary safeguards are not essential for the probable cause determination required by the Fourth Amendment. The sole issue is whether there is probable cause for detaining the arrested person pending further proceedings. This issue can be determined reliably without an adversary hearing. The standard is the same as that for arrest.<footnotemark>21</footnotemark> That standard — probable cause to believe the suspect has committed a crime — traditionally has been decided by a magistrate in a nonadversary proceeding on hearsay and written testimony, and the Court has approved these informal modes of proof.</p>
<blockquote id="b206-6">“Guilt in a criminal case must be proved beyond a reasonable doubt and by evidence confined to that which long experience in the common-law tradition, <page-number citation-index="1" label="121">*121</page-number>to some extent embodied in the Constitution, has crystallized into rules of evidence consistent with that standard. These rules are historically grounded rights of our system, developed to safeguard men from dubious and unjust convictions, with resulting forfeitures of life, liberty and property.</blockquote>
<blockquote id="b207-5">“In dealing with probable cause, however, as the very name implies, we deal with probabilities. These are not technical; they are the factual and practical considerations of everyday life on which reasonable and prudent men, not legal technicians, act. The standard of proof is accordingly correlative to what must be proved.” <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#174" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 174-175</a></span>.</blockquote>
<p id="b207-6">Cf. <em>McCray </em>v. <em>Illinois, </em><span class="citation" data-id="9423372"><a href="/opinion/107394/mccray-v-illinois/" aria-description="Citation for case: McCray v. Illinois">386 U. S. 300</a></span> (1967).</p>
<p id="b207-7">The use of an informal procedure is justified not only by the lesser consequences of a probable cause determination but also by the nature of the determination itself. It does not require the fine resolution of conflicting evidence that a reasonable-doubt or even a preponderance standard demands, and credibility determinations are seldom crucial in deciding whether the evidence supports a reasonable belief in guilt. See F. Miller, Prosecution: The Decision to Charge a Suspect with a Crime 64— 109 (1969).<footnotemark>22</footnotemark> This is not to say that confrontation and <page-number citation-index="1" label="122">*122</page-number>cross-examination might not enhance the reliability of probable cause determinations in some cases. In most cases, however, their value would be too slight to justify holding, as a matter of constitutional principle, that these formalities and safeguards designed for trial must also be employed in making the Fourth Amendment determination of probable cause.<footnotemark>23</footnotemark></p>
<p id="b208-5">Because of its limited function and its nonadversary character, the probable cause determination is not a “critical stage” in the prosecution that would require appointed counsel. The Court has identified as “critical stages” those pretrial procedures that would impair defense on the merits if the accused is required to proceed without counsel. <em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970); <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#226" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 226-227</a></span> (1967). In <em>Coleman </em>v. <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Alabama</a></span>, </em>where the Court held that a preliminary hearing was a critical stage of an Alabama prosecution, the majority and concurring opinions identified two critical factors that distinguish the Alabama preliminary hearing from the probable cause determination required by the Fourth Amendment. First, <page-number citation-index="1" label="123">*123</page-number>under Alabama law the function of the preliminary hearing was to determine whether the evidence justified charging the suspect with an offense. A finding of no probable cause could mean that he would not be tried at.all. The Fourth Amendment probable cause determination is addressed only to pretrial custody. To be sure, pretrial custody may affect to some extent the defendant’s ability to assist in preparation of his defense, but this does not present the high probability of substantial harm identified as controlling in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>and <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span>. </em>Second, Alabama allowed the suspect to confront and cross-examine prosecution witnesses at the preliminary hearing. The Court noted that the suspect’s defense on the merits could be compromised if he had no legal assistance for exploring or preserving the witnesses’ testimony. This consideration does not apply when the prosecution is not required to produce witnesses for cross-examination.</p>
<p id="b209-5">Although we conclude that the Constitution does not require an adversary determination of probable cause, we recognize that state systems of criminal procedure vary widely. There is no single preferred pretrial procedure, and the nature of the probable cause determination usually will be shaped to accord with a State’s pretrial procedure viewed as a whole. While we limit our holding to the precise requirement of the Fourth Amendment, we recognize the desirability of flexibility and experimentation by the States. It may be found desirable, for example, to make the probable cause determination at the suspect’s first appearance before a judicial officer,<footnotemark>24</footnotemark> <page-number citation-index="1" label="124">*124</page-number>see <em>McNabb </em>v. <em>United States, </em><span class="citation" data-id="9419320"><a href="/opinion/103791/mcnabb-v-united-states/#342" aria-description="Citation for case: McNabb v. United States">318 U. S., at 342-344</a></span>, or the determination may be incorporated into the procedure for setting bail or fixing other conditions of pretrial release. In some States, existing procedures may satisfy the requirement of the Fourth Amendment. Others may require only minor adjustment, such as acceleration of existing preliminary hearings. Current proposals for criminal procedure reform suggest other ways of testing probable cause for detention.<footnotemark>25</footnotemark> Whatever <page-number citation-index="1" label="125">*125</page-number>procedure a State may adopt, it must provide a fair and reliable determination of probable cause as a condition for any significant pretrial restraint of liberty,<footnotemark>26</footnotemark> and this determination must be made by a judicial officer either before or promptly after arrest.<footnotemark>27</footnotemark></p>
<p id="b212-4"><page-number citation-index="1" label="126">*126</page-number>IV</p>
<p id="b212-5">We agree with the Court of Appeals that the Fourth Amendment requires a timely judicial determination of probable cause as a prerequisite to detention, and we accordingly affirm that much of the judgment. As we do not agree that the Fourth Amendment requires the adversary hearing outlined in the District Court’s decree, we reverse in part and remand to the Court of Appeals for further proceedings consistent with this opinion.</p>
<p id="b212-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b191-10"> Respondent Pugh was arrested on March 3, 1971. On March 16 an information was filed charging him with robbery, carrying a concealed weapon, and possession of a firearm during commission of a felony. Respondent Henderson was arrested on March 2, and charged by information on March 19 with the offenses of breaking and entering and assault and battery. The record does not indicate whether there was an arrest warrant in either case.</p>
</footnote>
<footnote label="2">
<p id="b192-6"> Florida law also denies preliminary hearings to persons confined under indictment, see <em>Sangaree </em>v. <em>Hamlin, </em><span class="citation" data-id="1807359"><a href="/opinion/1807359/sangaree-v-hamlin/" aria-description="Citation for case: Sangaree v. Hamlin">235 So. 2d 729</a></span> (Fla. 1970) ; Fla. Rule Crim. Proc. 3.131 (a); but that procedure is not challenged in this case. See <em>infra, </em>at 117 n. 19.</p>
</footnote>
<footnote label="3">
<p id="b192-7"> This statute may have been construed to make the hearing permissive instead of mandatory. See <em>Evans </em>v. <em>State, </em><span class="citation" data-id="1725389"><a href="/opinion/1725389/evans-v-state/" aria-description="Citation for case: Evans v. State">197 So. 2d 323</a></span> (Fla. App. 1967); Fla. Op. Atty. Gen. 067-29 (1967). But cf. <em>Karz </em>v. <em>Overton, </em><span class="citation" data-id="7444015"><a href="/opinion/7520111/karz-v-overton/" aria-description="Citation for case: Karz v. Overton">249 So. 2d 763</a></span> (Fla. App. 1971). It may also have been superseded by the subsequent amendments to the Rules of Criminal Procedure. <em>In re Florida Rules of Criminal Procedure, </em><span class="citation" data-id="1917909"><a href="/opinion/1917909/in-re-florida-rules-of-criminal-procedure/" aria-description="Citation for case: In Re Florida Rules of Criminal Procedure">272 So. 2d 65</a></span> (1972).</p>
</footnote>
<footnote label="4">
<p id="b192-8"> The Florida rules do not suggest that the issue of probable cause can be raised at arraignment, Fla. Rule Crim. Proc. 3.160, but counsel for petitioner represented at oral argument that arraignment affords the suspect an opportunity to “attack the sufficiency of the evidence to hold him.” Tr. of Oral Arg. 17 (Mar. 25, 1974). The Court of Appeals assumed, without deciding, that this was true. <span class="citation multiple-matches"><a href="/c/F.%202d/483/778/">483 F. 2d 778</a></span>, 781 n. 8 (CA5 1973).</p>
</footnote>
<footnote label="5">
<p id="b193-6"> The complaint was framed under <span class="citation no-link">42 U. S. C. § 1983</span>, and jurisdiction in the District Court was based on <span class="citation no-link">28 U. S. C. § 1343</span> (3).</p>
</footnote>
<footnote label="6">
<p id="b193-7"> Respondents did not ask for release from state custody, even as an alternative remedy. They asked only that the state authorities be ordered to give them a probable cause determination. This was also the only relief that the District Court ordered for the named respondents. <span class="citation" data-id="1624670"><a href="/opinion/1624670/pugh-v-rainwater/#1115" aria-description="Citation for case: Pugh v. Rainwater">332 F. Supp. 1107, 1115-1116</a></span>, (SD Fla. 1971). Because release was neither asked nor ordered, the lawsuit did not come within the class of cases for which habeas corpus is the exclusive remedy. <em>Preiser </em>v. <em>Rodriguez, </em><span class="citation" data-id="9425260"><a href="/opinion/108772/preiser-v-rodriguez/" aria-description="Citation for case: Preiser v. Rodriguez">411 U. S. 475</a></span> (1973); see <em>Wolff </em>v. <em>McDonnell, </em><span class="citation" data-id="9425837"><a href="/opinion/109097/wolff-v-mcdonnell/#55" aria-description="Citation for case: Wolff v. McDonnell">418 U. S. 539, 55-555</a></span> (1974).</p>
</footnote>
<footnote label="7">
<p id="b193-8"><em> </em>Turner was being held on a charge of auto theft, following arrest on March 11, 1971. Faulk was arrested on March 19 on charges of soliciting a ride and possession of marihuana.</p>
</footnote>
<footnote label="8">
<p id="b193-9"> The named defendants included justices of the peace and judges of small-claims courts, who were authorized to hold preliminary hearings in criminal cases, and a group of law enforcement officers with power to make arrests in Dade County. Gerstein was the only one who petitioned for certiorari.</p>
</footnote>
<footnote label="9">
<p id="b194-6"> The District Court correctly held that respondents’ claim for relief was not barred by the equitable restrictions on federal intervention in state prosecutions, <em>Younger </em>v. <em>Harris, </em><span class="citation" data-id="9424435"><a href="/opinion/108263/younger-v-harris/" aria-description="Citation for case: Younger v. Harris">401 U. S. 37</a></span> (1971). The injunction was not directed at the state prosecutions as such, but only at the legality of pretrial detention without a judicial hearing, an issue that could not be raised in defense of the criminal prosecution. The order to hold preliminary hearings could not prejudice the conduct of the trial on the merits. See <em>Conover </em>v. <em>Montemuro, </em><span class="citation" data-id="8890009"><a href="/opinion/8903008/conover-v-montemuro/#1082" aria-description="Citation for case: Conover v. Montemuro">477 F. 2d 1073, 1082</a></span> (CA3 1972); cf. <em>Perez </em>v. <em>Ledesma, </em><span class="citation" data-id="9424442"><a href="/opinion/108266/perez-v-ledesma/" aria-description="Citation for case: Perez v. Ledesma">401 U. S. 82</a></span> (1971); <em>Stefanelli </em>v. <em>Minard, </em><span class="citation" data-id="9420643"><a href="/opinion/104937/stefanelli-v-minard/" aria-description="Citation for case: Stefanelli v. Minard">342 U. S. 117</a></span> (1951).</p>
</footnote>
<footnote label="10">
<p id="b195-7"> Although this ruling held a statewide “legislative rule” unconstitutional, it was not outside the jurisdiction of a single judge by virtue of <span class="citation no-link">28 U. S. C. §2281</span>. The original complaint did not ask for <page-number citation-index="1" label="110">*110</page-number>an injunction against enforcement of any state statute or legislative rule of statewide application, since the practice of denying preliminary hearings to persons charged by information was then embodied only in judicial decisions. The District Court therefore had jurisdiction to issue the initial injunction, and the Court of Appeals had jurisdiction over the appeal. On remand, the constitutionality of a state “statute” was drawn into question for the first time when the criminal rules were amended. The District Court’s supplemental opinion can fairly be read as a declaratory judgment that the amended rules were unconstitutional; the injunctive decree was never amended to incorporate that holding; and the opinion in the Court of Appeals is not inconsistent with the conclusion that the District Court did not enjoin enforcement of the statewide rule. See 483 F. 2d, at 788-790. Accordingly, a district court of three judges was not required for the issuance of this order. See <em>Kennedy </em>v. <em>Mendoza-Martinez, </em><span class="citation" data-id="9422536"><a href="/opinion/106534/kennedy-v-mendoza-martinez/#152" aria-description="Citation for case: Kennedy v. Mendoza-Martinez">372 U. S. 144, 152-155</a></span> (1963); <em>Flemming </em>v. <em>Nestor, </em><span class="citation" data-id="9422032"><a href="/opinion/106087/flemming-v-nestor/#606" aria-description="Citation for case: Flemming v. Nestor">363 U.S. 603, 606-608</a></span> (1960).</p>
</footnote>
<footnote label="11">
<p id="b196-7"> At oral argument counsel informed us that the named respondents have been convicted. Their pretrial detention therefore has ended. This case belongs, however, to that narrow class of cases in which the termination of a class representative’s claim does not moot the claims of the unnamed members of the class. See <em>Sosna </em>v. <em>Iowa, </em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">419 U. S. 393</a></span> (1975). Pretrial detention is by nature temporary, and it is most unlikely that any given individual could have his constitutional claim decided on appeal before he is either released or convicted. The individual could nonetheless suffer repeated deprivations, and it is certain that other persons similarly situated will be detained under the allegedly unconstitutional procedures. The claim, in short, is one that is distinctly “capable of repetition, yet evading review.”</p>
<p id="b196-8">At the time the complaint was filed, the named respondents were <page-number citation-index="1" label="111">*111</page-number>members of a class of persons detained without a judicial probable cause determination, but the record does not indicate whether any of them were still in custody awaiting trial when the District Court certified the class. Such a showing ordinarily would be required to avoid mootness under <em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">Sosna</a></span>. </em>But this case is a suitable exception to that requirement. See <em><span class="citation" data-id="9425895"><a href="/opinion/109128/sosna-v-iowa/" aria-description="Citation for case: Sosna v. Iowa">Sosna, supra,</a></span> </em>at 402 n. 11; cf. <em>Rivera </em>v. <em>Freeman, </em><span class="citation" data-id="306786"><a href="/opinion/306786/rosa-rivera-v-the-honorable-marvin-a-freeman-judge-of-the-superior-court/#1162" aria-description="Citation for case: Rosa Rivera v. The Honorable Marvin A. Freeman, Judge of...">469 F. 2d 1159, 1162-1163</a></span> (CA9 1972). The length of pretrial custody cannot be ascertained at the outset, and it may be ended at any time by release on recognizance, dismissal of the charges, or a guilty plea, as well as by acquittal or conviction after trial. It is by no means certain that any given individual, named as plaintiff, would be in pretrial custody long enough for a district judge to certify the class. Moreover, in this case the constant existence of a class of persons suffering the deprivation is certain. The attorney representing the named respondents is a public defender, and we can safely assume that he has other clients with a continuing live interest in the case.</p>
</footnote>
<footnote label="12">
<p id="b199-8"> We reiterated this principle in <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297</a></span> (1972). In terms that apply equally to arrests, we described the “very heart of the Fourth Amendment directive” as a requirement that “where practical, a governmental search and seizure should represent both the efforts of the officer to gather evidence of wrongful acts and the judgment of the magistrate that the collected evidence is sufficient to justify invasion of a citizen's private premises or conversation.” <span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#316" aria-description="Citation for case: United States v. United States District Court for the..."><em>Id., </em>at 316</a></span>.</p>
</footnote>
<footnote label="13">
<p id="b199-9"> Another aspect of <em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/" aria-description="Citation for case: Trupiano v. United States">Trupiano</a></span> </em>was overruled in <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950), which was overruled in turn by <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969).</p>
<p id="b199-10">The issue of warrantless arrest that has generated the most controversy, and that remains unsettled, is whether and under what circumstances an officer may enter a suspect’s home to make a war-rantless arrest. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-481</a></span> (1971); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#510" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 510-512</a></span>, and n. 1 (White, J., <em>dissenting); Jones </em>v. <em>United States, </em><span class="citation" data-id="9421692"><a href="/opinion/105749/jones-v-united-states/#499" aria-description="Citation for case: Jones v. United States">357 U. S. 493, 499-500</a></span> (1958).</p>
</footnote>
<footnote label="14">
<p id="b200-6"> The primary motivation for the requirement seems to have been the penalty for allowing an offender to escape, if he had in fact <page-number citation-index="1" label="115">*115</page-number>committed the crime, and the fear of liability for false imprisonment, if he had not. But Hale also recognized that a judicial warrant of commitment, called a <em>mittimus, </em>was required for more than brief detention.</p>
<p id="b201-6">“When a private person hath arrested a felon, or one suspected of felony, he may detain him in custody till he can reasonably dismiss himself of him; but with as much speed as conveniently he can, he may do either of these things.</p>
<p id="b201-7">“1. He may carry him to the common gaol, . . . but that is now rarely done.</p>
<p id="b201-8">“2. He may deliver him to the constable of the vill, who may either carry him to the common gaol, ... or to a justice of peace to be examined, and farther proceeded against as case shall require. . . .</p>
<p id="b201-9">“3. Or he may carry him immediately to any justice of peace of the county where he is taken, who upon examination may discharge, bail, or commit him, as the case shall require.</p>
<p id="b201-10">“And the bringing the offender either by the constable or private person to a justice of peace is most usual and safe, because a gaoler will expect a <em>Mittimus </em>for his warrant of detaining.” 1 M. Hale, Pleas of the Crown 589-590 (1736).</p>
</footnote>
<footnote label="15">
<p id="b201-11"> The examination of the prisoner was inquisitorial, and the witnesses were questioned outside the prisoner’s presence. Although this method of proceeding was considered quite harsh, 1 J. Stephen, <em>supra, </em>at 219-225, it was well established that the prisoner was entitled to be discharged if the investigation turned up insufficient evidence of his guilt. <em>Id., </em>at 233.</p>
</footnote>
<footnote label="16">
<p id="b202-7"> In <em>Ex parte Bollman, </em>two men charged in the Aaron Burr case were committed following an examination in the Circuit Court of the District of Columbia. They filed a petition for writ of habeas corpus in the Supreme Court. The Court, in an opinion by Mr. Chief Justice Marshall, affirmed its jurisdiction to issue habeas corpus to persons in custody by order of federal trial courts. Then, following arguments on the Fourth Amendment requirement of probable cause, the Court surveyed the evidence against the prisoners and held that it did not establish probable cause that they were guilty of treason. The prisoners were discharged.</p>
</footnote>
<footnote label="17">
<p id="b202-8"> See also N. Lasson, The History and Development of the Fourth Amendment to the United States Constitution 15-16 (1937). A similar procedure at common law, the warrant for recovery of stolen goods, is said to have furnished the model for a “reasonable” search under the Fourth Amendment. The victim was required to appear before a justice of the peace and make an oath of probable cause that his goods could be found in a particular place. After the warrant was executed, and the goods seized, the victim and the alleged thief would appear before the justice of the peace for a prompt determination of the cause for seizure of the goods and detention of the thief. 2 M. Hale, <em>supra, </em>at 149-152; T. Taylor, Two Studies in Constitutional Interpretation 2A-25, 39-40 (1969); see <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 626-629</a></span> (1886).</p>
</footnote>
<footnote label="18">
<p id="b202-9"> A person arrested under a warrant would have received a prior judicial determination of probable cause. Under Fla. Rule Crim. <page-number citation-index="1" label="117">*117</page-number>Proc. 3.120, a warrant may be issued upon a sworn complaint that states facts showing that the suspect has committed a crime. The magistrate may also take testimony under oath to determine if there is reasonable ground to believe the complaint is true.</p>
</footnote>
<footnote label="19">
<p id="b203-6"> By contrast, the Court has held that an indictment, “fair upon its face,” and returned by a “properly constituted grand jury,” conclusively determines the existence of probable cause and requires issuance of an arrest warrant without further inquiry. <em>Ex parte United States, </em><span class="citation" data-id="101974"><a href="/opinion/101974/ex-parte-united-states/#250" aria-description="Citation for case: Ex Parte United States">287 U. S. 241, 250</a></span> (1932). See also <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#487" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 487</a></span> (1958). The willingness to let a grand jury’s judgment substitute for that of a neutral and detached magistrate is attributable to the grand jury’s relationship to the courts and its historical role of protecting individuals from unjust prosecution. See <em>United States </em>v. <em>Calandra, </em><span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#342" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 342-346</a></span> (1974).</p>
</footnote>
<footnote label="20">
<p id="b204-7"> The Court had earlier reached a different result in <em>Ocampo </em>v. <em>United States, </em><span class="citation" data-id="98209"><a href="/opinion/98209/ocampo-v-united-states/" aria-description="Citation for case: Ocampo v. United States">234 U. S. 91</a></span> (1914), a criminal appeal from the Philippine Islands. Interpreting a statutory guarantee substantially identical to the Fourth Amendment, Act of July 1, 1902, § 5, <span class="citation no-link">32 Stat. 693</span>, the Court held that an arrest warrant could issue solely upon a prosecutor’s information. The Court has since held that interpretation of a statutory guarantee applicable to the Philippines is not conclusive for interpretation of a cognate provision in the Federal Constitution, <em>Green </em>v. <em>United States, </em><span class="citation" data-id="9421521"><a href="/opinion/105594/green-v-united-states/#194" aria-description="Citation for case: Green v. United States">355 U. S. 184, 194-198</a></span> (1957). Even if it were, the result reached in <em><span class="citation" data-id="98209"><a href="/opinion/98209/ocampo-v-united-states/" aria-description="Citation for case: Ocampo v. United States">Ocampo</a></span> </em>is incompatible with the later holdings of <em>Albrecht, Coolidge, </em>and <em>Shadwick.</em></p>
</footnote>
<footnote label="21">
<p id="b206-7"> Because the standards are identical, ordinarily there is no need for further investigation before the probable cause determination can be made.</p>
<blockquote id="b206-8">“Presumably, whomever the police arrest they must arrest on 'probable cause.' It is not the function of the police to arrest, as it were, at large and to use an interrogating process at police headquarters in order to determine whom they should charge before a committing magistrate on 'probable cause.’ ” <em>Mallory </em>v. <em>United States, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/#456" aria-description="Citation for case: Mallory v. United States">354 U. S. 449, 456</a></span> (1957).</blockquote>
</footnote>
<footnote label="22">
<p id="b207-8"> In <em>Morrissey </em>v. <em>Brewer, </em><span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/" aria-description="Citation for case: Morrissey v. Brewer">408 U. S. 471</a></span> (1972), and <em>Gagnon </em>v. <em>Scarpelli, </em><span class="citation" data-id="9425285"><a href="/opinion/108785/gagnon-v-scarpelli/" aria-description="Citation for case: Gagnon v. Scarpelli">411 U. S. 778</a></span> (1973), we held that a parolee or probationer arrested prior to revocation is entitled to an informal preliminary hearing at the place of arrest, with some provision for live testimony. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#487" aria-description="Citation for case: Morrissey v. Brewer">408 U. S., at 487</a></span>; 411 U. S., at 786. That preliminary hearing, more than the probable cause determination required by the Fourth Amendment, serves the purpose of gathering and preserving live testimony, since the final revocation hearing frequently is held at some distance from the place where the violation occurred. <span class="citation" data-id="9425003"><a href="/opinion/108606/morrissey-v-brewer/#485" aria-description="Citation for case: Morrissey v. Brewer">408 U. S., at 485</a></span>; 411 U. S., at 782-783, n. 5. Moreover, revocation <page-number citation-index="1" label="122">*122</page-number>proceedings may offer less protection from initial error than the more formal criminal process, where violations are defined by statute and the prosecutor has a professional duty not to charge a suspect with crime unless he is satisfied of probable cause. See ABA Code of Professional Responsibility DR 7-103 (A) (Final Draft 1969) (a prosecutor “shall not institute or cause to be instituted criminal charges when he knows or it is obvious that the charges are not supported by probable cause”); American Bar Association Project on Standards for Criminal Justice, The Prosecution Function §§ 1.1, 3.4, 3.9 (1974); American College of Trial Lawyers, Code of Trial Conduct, Rule 4 (c) (1963).</p>
</footnote>
<footnote label="23">
<p id="b208-7"> Criminal justice is already overburdened by the volume of cases and the complexities of our system. The processing of misdemeanors, in particular, and the early stages of prosecution generally are marked by delays that can seriously affect the quality of justice. A constitutional doctrine requiring adversary hearings for all persons detained pending trial could exacerbate the problem of pretrial delay.</p>
</footnote>
<footnote label="24">
<p id="b209-6"> Several States already authorize a determination of probable cause at this stage or immediately thereafter. See, <em>e. g., </em>Hawaii Rev. Stat. §§ 708-9 (5), 710-7 (1968); Vt. Rules Crim. Proc. 3 (b), 5 (c). This Court has interpreted the Federal Rules of Criminal Procedure to require a determination of probable cause at the first appearance. <em>Jaben </em>v. <em>United States, </em><span class="citation" data-id="9423037"><a href="/opinion/107058/jaben-v-united-states/#218" aria-description="Citation for case: Jaben v. United States">381 U. S. 214, 218</a></span> (1965); <em>Mallory </em>v. <em>United States, </em><span class="citation" data-id="105545"><a href="/opinion/105545/mallory-v-united-states/#454" aria-description="Citation for case: Mallory v. United States">354 U. S., at 454</a></span>.</p>
</footnote>
<footnote label="25">
<p id="b210-5"> Under the Uniform Rules of Criminal Procedure (Proposed Final Draft 1974), a person arrested without a warrant is entitled, “without unnecessary delay,” to a first appearance before a magistrate and a determination that grounds exist for issuance of an arrest warrant. The determination may be made on affidavits or testimony, in the presence of the accused. Rule 311. Persons who remain in custody for inability to qualify for pretrial release are offered another opportunity for a probable cause determination at the detention hearing, held no more than five days after arrest. This is an adversary hearing, and the parties may summon witnesses, but reliable hearsay evidence may be considered. Rule 344.</p>
<p id="b210-6">The ALI Model Code of Pre-arraignment Procedure (Tent. Draft No. 5, 1972, and Tent. Draft No. 5A, 1973) also provides a first appearance, at which a warrantless arrest must be supported by a reasonably detailed written statement of facts. §310.1. The magistrate may make a determination of probable cause to hold the accused, but he is not required to do so and the accused may request an attorney for an “adjourned session” of the first appearance to be held within two “court days.” At that session, the magistrate makes a determination of probable cause upon a combination of written and live testimony:</p>
<blockquote id="b210-7">“The arrested person may present written and testimonial evidence and arguments for his discharge and the state may present additional written and testimonial evidence and arguments that there is reasonable cause to believe that he has committed the crime of which he is accused. The state’s submission may be made by means of affidavits; and no witnesses shall be required to appear unless the court, in the light of the evidence and arguments submitted by the parties, determines that there is a basis for believing that the appearance of one or more witnesses for whom the arrested person seeks <page-number citation-index="1" label="125">*125</page-number>subpoenas might lead to a finding that there is no reasonable cause.” § 310.2 (2) (Tent. Draft No. 5A, 1973).</blockquote>
</footnote>
<footnote label="26">
<p id="b211-6"> Because the probable cause determination is not a constitutional prerequisite to the charging decision, it is required only for those suspects who suffer restraints on liberty other than the condition that they appear for trial. There are many kinds of pretrial release and many degrees of conditional liberty. See <span class="citation no-link">18 U. S. C. § 3146</span>; American Bar Association Project on Standards for Criminal Justice, Pretrial Release § 5.2 (1974); Uniform Rules of Criminal Procedure, Rule 341 (Proposed Final Draft 1974). We cannot define specifically those that would require a prior probable cause determination, but the key factor is significant restraint on liberty.</p>
</footnote>
<footnote label="27">
<p id="b211-7"> In his concurring opinion, Mr. Justice Stewart objects to the Court's choice of the Fourth Amendment as the rationale for decision and suggests that the Court offers less procedural protection to a person in jail than it requires in certain civil cases. Here we deal with the complex procedures of a criminal case and a threshold right guaranteed by the Fourth Amendment. The historical basis of the probable cause requirement is quite different from the relatively recent application of variable procedural due process in debtor-creditor disputes and termination of government-created benefits. The Fourth Amendment was tailored explicitly for the criminal justice system, and its balance between individual and public interests always has been thought to define the “process that is due” for seizures of person or property in criminal cases, including the detention of suspects pending trial. Part II-A, <em>supra. </em>Moreover, the Fourth Amendment probable cause determination is in fact only the <em>first </em>stage of an elaborate system, unique in jurisprudence, designed to safeguard the rights of those accused of criminal conduct. The relatively simple civil procedures (e. <em>g., </em>prior interview with school principal before suspension) presented in the cases cited in the concurring opinion are inapposite and irrelevant in the wholly different context of the criminal justice system.</p>
<p id="b211-8">It would not be practicable to follow the further suggestion implicit in Mr. Justice Stewart’s concurring opinion that we leave for <page-number citation-index="1" label="126">*126</page-number>another day determination of the procedural safeguards that are required in making a probable cause determination under the Fourth Amendment. The judgment under review both declares the right not to be detained without a probable cause determination and affirms the District Court’s order prescribing an adversary hearing for the implementation of that right. The circumstances of the case thus require a decision on both issues.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Giglio v. United States.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Giglio v. United States"
type: case
citation: "405 U.S. 150 (1972)"
parallel_cite: "92 S. Ct. 763; 31 L. Ed. 2d 104"
neutral_cite: 1972 U.S. LEXIS 83
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1972
date_decided: 1972-02-24
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1972-02-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Giglio v. United States
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/108471/giglio-v-united-states/"
  cluster_id: 108471
  opinion_id: 108471
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Anchor"
related: ["[[Brady v. Maryland]]", "[[Napue v. Illinois]]", "[[Benn v. Lambert]]"]
aliases: ["Giglio v. US"]
tags: ["case", "brady", "giglio", "impeachment", "disclosure", "witness-credibility"]
holding: "Impeachment evidence falls within the Brady rule: nondisclosure of evidence affecting a key witness's credibility — including a promise…"
lake:
  record_id: Giglio v. United States
  status: verified
  projected_at: 2026-07-06
---

# Giglio v. United States

*405 U.S. 150 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Giglio was convicted of passing forged money orders almost entirely on the testimony of an accomplice, Robert Taliento, who had not been indicted. After trial, the defense learned that a prosecutor had promised Taliento he would not be prosecuted if he cooperated and testified — a promise the trial prosecutor never disclosed, and which had been denied at trial.

## Issue
Whether the Government's failure to disclose a promise of leniency made to its key witness — evidence going only to the witness's credibility — violates due process and requires a new trial.

## Rule
Impeachment evidence is governed by the Brady disclosure rule when the witness's credibility is central to the case. "When the 'reliability of a given witness may well be determinative of guilt or innocence,' nondisclosure of evidence affecting credibility falls within this general rule." — 405 U.S. at 154. ^pin-154

Because the prosecutor's office speaks as one for the Government, a promise made by one prosecutor is attributed to the Government even if the trial attorney was unaware of it; a new trial is required where the undisclosed evidence was material — that is, where it could in any reasonable likelihood have affected the jury's judgment.

## Application
Taliento was the Government's essential witness, so his reliability could well determine guilt or innocence. The undisclosed promise not to prosecute him gave him a powerful motive to testify favorably, and the jury was entitled to know of it. That one prosecutor made the promise while the trial prosecutor was unaware did not excuse the nondisclosure, and on this record the evidence was material — so Giglio was entitled to a new trial.

## Conclusion
The failure to disclose the leniency promise to a key witness required a new trial; the conviction was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Giglio* extends [[Brady v. Maryland]] to impeachment evidence and charges the prosecution with knowledge held by any of its attorneys; the framework is applied in [[Benn v. Lambert]].

## Appears on
- [[Brady and Giglio]] — *Key — Anchor*

## Sources
- *Giglio v. United States*, 405 U.S. 150 (1972) — https://www.courtlistener.com/opinion/108471/giglio-v-united-states/ — pinpoint: 154.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d185bc7b3b882a68", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Giglio v. United States"}, "payload": {"all": [{"cite": "405 U.S. 150", "page": "150", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "405"}, {"cite": "92 S. Ct. 763", "page": "763", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "92"}, {"cite": "31 L. Ed. 2d 104", "page": "104", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "31"}, {"cite": "1972 U.S. LEXIS 83", "page": "83", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1972"}], "display": "405 U.S. 150", "official": {"cite": "405 U.S. 150", "page": "150", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "405"}, "official_selection_present": true, "record_id": "Giglio v. United States"}}
{"assertion_id": "ec52d54228d99b0f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-154", "record_id": "Giglio v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-154", "pinpoint_status": "slip-only", "quote": "--- # Giglio v. United States *405 U.S. 150 (1972)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Giglio was convicted of passing forged money orders almost entirely on the testimony of an accomplice, Robert Taliento, who had not been indicted. After trial, the defense learned that a prosecutor had promised Taliento he would not be prosecuted if he cooperated and testified — a promise the trial prosecutor never disclosed, and which had been denied at trial. ## Issue Whether the Government's failure to disclose a promise of leniency made to its key witness — evidence going only to the witness's credibility — violates due process and requires a new trial. ## Rule Impeachment evidence is governed by the Brady disclosure rule when the witness's credibility is central to the case.", "quote_fidelity": "mismatch", "record_id": "Giglio v. United States", "star_marker": null}}
{"assertion_id": "5b18132ede0912d2", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Giglio v. United States"}, "payload": {"as_of_content": "1972-02-24", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Giglio v. United States", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Giglio v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Giglio v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Giglio v. United States",
    "case_name_short": "Giglio",
    "case_name_full": "Giglio v. United States",
    "input_case_name": "Giglio v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1972-02-24",
    "year": 1972,
    "docket": null,
    "cluster_id": 108471,
    "lead_opinion_id": 108471,
    "sibling_ids": [
      108471
    ],
    "absolute_url": "/opinion/108471/giglio-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "405 U.S. 150",
      "volume": "405",
      "reporter": "U.S.",
      "page": "150",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "92 S. Ct. 763",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "763",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "31 L. Ed. 2d 104",
        "volume": "31",
        "reporter": "L. Ed. 2d",
        "page": "104",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1972 U.S. LEXIS 83",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "405 U.S. 150",
        "volume": "405",
        "reporter": "U.S.",
        "page": "150",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 S. Ct. 763",
        "volume": "92",
        "reporter": "S. Ct.",
        "page": "763",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "31 L. Ed. 2d 104",
        "volume": "31",
        "reporter": "L. Ed. 2d",
        "page": "104",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1972 U.S. LEXIS 83",
        "volume": "1972",
        "reporter": "U.S. LEXIS",
        "page": "83",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "405 U.S. 150",
    "official_selection": {
      "court_class": "scotus",
      "selected": "405 U.S. 150",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-154",
      "page": null,
      "quote": "--- # Giglio v. United States *405 U.S. 150 (1972)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Giglio was convicted of passing forged money orders almost entirely on the testimony of an accomplice, Robert Taliento, who had not been indicted. After trial, the defense learned that a prosecutor had promised Taliento he would not be prosecuted if he cooperated and testified \u2014 a promise the trial prosecutor never disclosed, and which had been denied at trial. ## Issue Whether the Government's failure to disclose a promise of leniency made to its key witness \u2014 evidence going only to the witness's credibility \u2014 violates due process and requires a new trial. ## Rule Impeachment evidence is governed by the Brady disclosure rule when the witness's credibility is central to the case.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1972-02-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Giglio v. United States",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Giglio v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Graham v. District Attorney for the Hampden District",
          "cluster_id": 9468079,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane1_negative"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCleskey v. Zant",
          "cluster_id": 112573,
          "cite": [
            "113 L. Ed. 2d 517",
            "111 S. Ct. 1454",
            "499 U.S. 467",
            "1991 U.S. LEXIS 2218",
            "59 U.S.L.W. 4288",
            "91 Cal. Daily Op. Serv. 2680",
            "91 Daily Journal DAR 4340"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heckler v. Community Health Services of Crawford County, Inc.",
          "cluster_id": 111187,
          "cite": [
            "81 L. Ed. 2d 42",
            "104 S. Ct. 2218",
            "467 U.S. 51",
            "1984 U.S. LEXIS 87",
            "52 U.S.L.W. 4621"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Valenzuela-Bernal",
          "cluster_id": 110797,
          "cite": [
            "73 L. Ed. 2d 1193",
            "102 S. Ct. 3440",
            "458 U.S. 858",
            "1982 U.S. LEXIS 159",
            "50 U.S.L.W. 5108"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pettit",
          "cluster_id": 1250971,
          "cite": [
            "171 Wis. 2d 627",
            "492 N.W.2d 633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ruiz",
          "cluster_id": 121166,
          "cite": [
            "153 L. Ed. 2d 586",
            "122 S. Ct. 2450",
            "536 U.S. 622",
            "2002 U.S. LEXIS 4650"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
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
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Roberson",
          "cluster_id": 112100,
          "cite": [
            "100 L. Ed. 2d 704",
            "108 S. Ct. 2093",
            "486 U.S. 675",
            "1988 U.S. LEXIS 2726",
            "56 U.S.L.W. 4590"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Van de Kamp v. Goldstein",
          "cluster_id": 145911,
          "cite": [
            "172 L. Ed. 2d 706",
            "129 S. Ct. 855",
            "555 U.S. 335",
            "2009 U.S. LEXIS 1003"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ash",
          "cluster_id": 108846,
          "cite": [
            "37 L. Ed. 2d 619",
            "93 S. Ct. 2568",
            "413 U.S. 300",
            "1973 U.S. LEXIS 45"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Haley v. City of Boston",
          "cluster_id": 613874,
          "cite": [
            "657 F.3d 39",
            "2011 U.S. App. LEXIS 19223",
            "2011 WL 4347027"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Marshall",
          "cluster_id": 1969802,
          "cite": [
            "690 A.2d 1",
            "148 N.J. 89",
            "1997 N.J. LEXIS 70"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Blake v. State",
          "cluster_id": 9423249,
          "cite": [
            "485 Md. 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Giglio v. United States:lane3_recency"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(108471) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjQ5Mjg5NjAwMDAwJnM9NjQ1ODQxOCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28108471%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(108471)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00MTQmcz03MDUyNTc4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28108471%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(108471)",
        "reviewed": 187,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 187,
        "triage_read": 3,
        "triage_snippet_classified": 184
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(108471)",
    "indexed_citing_opinions": 4151,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 108471,
        "count": 4151,
        "count_source": "search"
      }
    ],
    "citation_count": 7011,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/giglio-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0MzU1MyZzPTEwNjI0NTY2JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28108471%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 108471,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 108471,
        "cited_id": 279213,
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
    "date_created": "2026-07-05T05:27:48Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T05:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T05:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T05:31:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T05:28:03Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Giglio v. United States

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b294-12">
  Mr. Chief Justice Burger
 </author>
<p id="AL2">
  delivered the opinion of the Court.
 </p>
<p id="b294-13">
  Petitioner was convicted of passing forged money orders and sentenced to five years’ imprisonment. While appeal was pending in the Court of Appeals, defense counsel discovered new evidence indicating that the Government
  <span citation-index="1" class="star-pagination" label="151"> 
   *151
   </span>
  had failed to disclose an alleged promise made to its key-witness that he would not be prosecuted if he testified for the Government. We granted certiorari to determine whether the evidence not disclosed was such as to require a new trial under the due process criteria of
  <em>
   Napue
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), and
  <em>
   Brady
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U. S. 83</a></span> (1963).
 </p>
<p id="b295-5">
  The controversy in this case centers around the testimony of Robert Taliento, petitioner’s alleged cocon-spirator in the offense and the only witness linking petitioner with the crime. The Government’s evidence at trial showed that in June 1966 officials at the Manufacturers Hanover Trust Co. discovered that Taliento, as teller at the bank, had cashed several forged money orders. Upon questioning by FBI agents, he confessed supplying petitioner with one of the bank’s customer signature cards used by Giglio to forge $2,300 in money orders; Taliento then processed these money orders through the regular channels of the bank. Taliento related this story to the grand jury and petitioner was indicted; thereafter, he was named as a coconspirator with petitioner but was not indicted.
 </p>
<p id="b295-6">
  Trial commenced two years after indictment. Taliento testified, identifying petitioner as the instigator of the scheme. Defense counsel vigorously cross-examined, seeking to discredit his testimony by revealing possible agreements or arrangements for prosecutorial leniency:
 </p>
<blockquote id="b295-7">
  “[Counsel.] Did anybody tell you at any time that if you implicated somebody else in this case that you yourself would not be prosecuted?
 </blockquote>
<blockquote id="b295-8">
  “[Taliento.] Nobody told me I wouldn’t be prosecuted.
 </blockquote>
<blockquote id="b295-9">
  “Q. They told you you might not be prosecuted?
 </blockquote>
<blockquote id="b295-10">
  “A. I believe I still could be prosecuted.
 </blockquote>
<blockquote id="b296-4">
<span citation-index="1" class="star-pagination" label="152"> 
   *152
   </span>
  “Q. Were you ever arrested in this case or charged with anything in connection with these money orders that you testified to?
 </blockquote>
<blockquote id="b296-5">
  “A. Not at that particular time.
 </blockquote>
<blockquote id="b296-6">
  “Q. To this date, have you been charged with any crime?
 </blockquote>
<blockquote id="b296-7">
  “A. Not that I know of, unless they are still going to prosecute.”
 </blockquote>
<p id="b296-8">
  In summation, the Government attorney stated, “[Tali-ento] received no promises that he would not be indicted.”
 </p>
<p id="b296-9">
  The issue now before the Court arose on petitioner’s motion for new trial based on newly discovered evidence. An affidavit filed by the Government as part of its opposition to a new trial confirms petitioner’s claim that a promise was made to Taliento by one assistant, DiPaola,
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  that if he testified before the grand jury and at trial he would not be prosecuted.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  DiPaola presented the Government’s case to the grand jury but did not try the case in the District Court, and Golden, the assistant who took over the case for trial, filed an affidavit stating that DiPaola assured him before the trial that no promises of immunity had been made to Taliento.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  The United
  <span citation-index="1" class="star-pagination" label="153"> 
   *153
   </span>
  States Attorney, Hoey, filed an affidavit stating that he had personally consulted with Taliento and his attorney shortly before trial to emphasize that Taliento would definitely be prosecuted if he did not testify and that if he did testify he would be obliged to rely on the “good judgment and conscience of the Government” as to whether he would be prosecuted.
  <a class="footnote" href="#fn4" id="fn4_ref">
   4
  </a>
</p>
<p id="b297-5">
  The District Court did not undertake to resolve the apparent conflict between the two Assistant United States Attorneys, DiPaola and Golden, but proceeded on the theory that even if a promise had been made by DiPaola it was not authorized and its disclosure to the jury would not have affected its verdict. We need not concern ourselves with the differing versions of the events as described by the two assistants in their affidavits. The heart of the matter is that one Assistant United States Attorney — the first one who dealt with Taliento— now states that he promised Taliento that he would not be prosecuted if he cooperated with the Government.
 </p>
<p id="b297-6">
  As long ago as
  <em>
   Mooney
  </em>
  v.
  <em>
   Holohan,
  </em>
  <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span> (1935), this Court made clear that deliberate deception of a. court and jurors by the presentation of known false evidence \s&gt; incompatible with “rudimentary demands of justice.” This was reaffirmed in
  <em>
   Pyle
  </em>
  v.
  <em>
   Kansas,
  </em>
  <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213</a></span> (1942). In
  <em>
   Napue
  </em>
  v.
  <em>
   Illinois,
  </em>
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264</a></span> (1959), we said, “[t]he same result obtains when the State, although not soliciting false evidence, allows it to go uncorrected when it appears.”
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><em>
   Id.,
  </em>
  at 269</a></span>. Thereafter
  <em>
   Brady
  </em>
  v.
  <em>
   Maryland,
  </em>
  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland">373 U. S., at 87</a></span>, held that suppression of material evidence justifies a new trial “irrespective of the good faith or bad faith of the prosecution.” See Ameri
  <span citation-index="1" class="star-pagination" label="154"> 
   *154
   </span>
  can Bar Association, Project on Standards for Criminal Justice, Prosecution Function and the Defense Function §3.11 (a). When the “reliability of a given witness may well be determinative of guilt or innocence,” nondisclosure of evidence affecting credibility falls within this general rule.
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois"><em>
   Napue, supra,
  </em>
  at 269</a></span>. We do not, however, automatically require a new trial whenever “a combing of the prosecutors’ files after the trial has disclosed evidence possibly useful to the defense but not likely to have changed the verdict . . . .”
  <em>
   United States
  </em>
  v.
  <em>
   Keogh,
  </em>
  <span class="citation" data-id="279213"><a href="/opinion/279213/united-states-v-james-vincent-keogh/#148" aria-description="Citation for case: United States v. James Vincent Keogh">391 F. 2d 138, 148</a></span> (CA2 1968). A finding of materiality of the evidence is required under
  <span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/#87" aria-description="Citation for case: Brady v. Maryland"><em>
   Brady, supra,
  </em>
  at 87</a></span>. A new trial is required if “the false testimony could ... in any reasonable likelihood have affected the judgment of the jury . . . .”
  <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#271" aria-description="Citation for case: Napue v. Illinois"><em>
   Napue, supra,
  </em>
  at 271</a></span>.
 </p>
<p id="b298-5">
  In the circumstances shown by this record, neither DiPaola’s authority nor his failure to inform his superiors or his associates is controlling. Moreover, whether the nondisclosure was a result of negligence or design, it is the responsibility of the prosecutor. The prosecutor’s office is an entity and as such it is the spokesman for the Government. A promise made by one attorney must be attributed, for these purposes, to the Government. See Restatement (Second) of Agency § 272. See also American Bar Association, Project on Standards for Criminal Justice, Discovery and Procedure Before Trial §2.1 (d). To the extent this places a burden on the large prosecution offices, procedures and regulations can be established to carry that burden and to insure communication of all relevant information on each case to every lawyer who deals with it.
 </p>
<p id="b298-6">
  Here the Government’s case depended almost entirely on Taliento’s testimony; without it there could have been no indictment and no evidence to carry the case to the jury. Taliento’s credibility as a witness was therefore
  <span citation-index="1" class="star-pagination" label="155"> 
   *155
   </span>
  an important issue in the case, and evidence of any-understanding or agreement as to a future prosecution would be relevant to his credibility and the jury was entitled to know of it.
 </p>
<p id="b299-5">
  For these reasons, the due process requirements enunciated in
  <em>
   <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">Napue</a></span>
  </em>
  and the other cases cited earlier require a new trial, and the judgment of conviction is therefore reversed and the case is remanded for further proceedings consistent with this opinion.
 </p>
<p id="b299-6">
<em>
   Reversed and remanded.
  </em>
</p>
<p id="b299-7">
  Mr. Justice Powell and Mr. Justice Rehnquist took no part in the consideration or decision of this case.
 </p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b296-10">
   During oral argument in this Court it was stated that DiPaola was on the staff of the United States Attorney when he made the affidavit in 1969 and remained on that staff until recently.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b296-11">
   DiPaola’s affidavit reads, in part, as follows :
  </p>
<blockquote id="b296-12">
   “It was agreed that if ROBERT EDWARD TALIENTO would testify before the Grand Jury as a witness for the Government, . . . he would not be . . . indicted. ... It was further agreed and understood that he, ROBERT EDWARD TALIENTO, would sign a Waiver of Immunity from prosecution before the Grand Jury, and that if he eventually testified as a witness for the Government at the trial of the defendant, JOHN GIGLIO, he would not be prosecuted.”
  </blockquote>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b296-13">
   Golden’s affidavit reads, in part, as follows:
  </p>
<blockquote id="b296-14">
   “Mr. DiPaola . . . advised that Mr. Taliento had not been granted immunity but that he had not indicted him because Robert Taliento was very young at the time of the alleged occurrence and obviously had been overreached by the defendant Giglio.”
  </blockquote>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b297-7">
   The Hoey affidavit, standing alone, contains at least an implication that the Government would reward the cooperation of the witness, and hence tends to confirm rather than refute the existence of some understanding for leniency.
  </p>
</div></div></opinion>
```

---
