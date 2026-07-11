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

## GROUP: _overhaul2/lake/cases/Boyd v. United States.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Boyd v. United States"
type: case
citation: "116 U.S. 616 (1886)"
parallel_cite: "6 S. Ct. 524; 29 L. Ed. 746; 3 A.F.T.R. (P-H) 2488"
neutral_cite: 1886 U.S. LEXIS 1806
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1886
date_decided: 1886-02-01
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 1886-02-01
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Boyd v. United States
  varies_by_point: true
  scope_note: "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment — the proposition for which it is cited here — remains good law and is frequently cited."
  point_overrides:
    - point: legacy-limited-boyd-v-united-states
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Warden v. Hayden
          cluster_id: 107465
          cite: 387 U.S. 294
          field_ii: limited
      scope_note: "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment — the proposition for which it is cited here — remains good law and is frequently cited."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/91573/boyd-v-united-states/"
  cluster_id: 91573
  opinion_id: 91573
  identity_checked: true
homes:
  - page: "[[Common Law Origins]]"
    role: "Key — Anchor"
related: ["[[Entick v. Carrington]]", "[[Warden v. Hayden]]"]
aliases: ["Boyd v. US"]
tags: ["case", "fourth-amendment", "common-law-origins", "fifth-amendment", "history"]
holding: "Recounts the founding history and adopts *Entick v. Carrington* as 'the true and ultimate expression of constitutional law' embodied in the Fourth Amendment."
lake:
  record_id: Boyd v. United States
  status: verified
  projected_at: 2026-07-06
---

# Boyd v. United States

*116 U.S. 616 (1886)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In a federal customs forfeiture proceeding, the government invoked a statute to compel Boyd to produce private business invoices for use against him. Boyd objected that the compelled production was both an unreasonable search and seizure and a form of compelled self-incrimination. To decide what the Fourth Amendment forbids, the Court turned to the English origins of the constitutional guarantee.

## Issue
What the Framers of the Fourth Amendment understood "unreasonable searches and seizures" to mean — and, in answering, whether *[[Entick v. Carrington]]* states the foundational principle the Amendment embodies.

## Rule
The Court adopted Lord Camden's judgment in *[[Entick v. Carrington]]* as the constitutional touchstone. Every American statesman of the founding era "considered it as the true and ultimate expression of constitutional law". — 116 U.S. at 626. ^pin-626

Accordingly, *[[Entick v. Carrington|Entick]]*'s "propositions were in the minds of those who framed the Fourth Amendment to the Constitution, and were considered as sufficiently explanatory of what was meant by unreasonable searches and seizures." — *Id.* at 626-627. ^pin-627

*(Note: the broader Boyd holding equating compelled production of papers with an unreasonable search and self-incrimination has since been limited — see Treatment below. The Entick/historical proposition stated here is undisturbed.)*

## Application
Reading the Fourth Amendment through *[[Entick v. Carrington|Entick]]*, the Court held that the statutory compulsion of Boyd's private papers, for use against him in the forfeiture, fell within the constitutional prohibition on unreasonable searches and ran together with the Fifth Amendment privilege; the judgment against Boyd was reversed.

## Conclusion
The compelled production violated the Fourth and Fifth Amendments. As a matter of doctrine the decision survives chiefly for its founding-era account of the Amendment's origins; its papers-production holding has not endured (see Treatment).

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited by** *Fisher v. United States* (compelled production of papers analyzed under act-of-production doctrine, not Boyd's broad Fourth/Fifth Amendment convertibility) and **abandoned in part by** [[Warden v. Hayden]] (rejecting the "mere evidence" rule).
- The portion for which this page cites *Boyd* — its adoption of [[Entick v. Carrington]] as the historical expression of the Fourth Amendment — remains good law and is regularly invoked.

## Appears on
- [[Common Law Origins]] — *Key — Anchor*

## Sources
- *Boyd v. United States*, 116 U.S. 616 (1886) — https://www.courtlistener.com/opinion/91573/boyd-v-united-states/ — pinpoints: 626, 627.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "05f85601f0b05d3f", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Boyd v. United States"}, "payload": {"all": [{"cite": "116 U.S. 616", "page": "616", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "116"}, {"cite": "6 S. Ct. 524", "page": "524", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "6"}, {"cite": "29 L. Ed. 746", "page": "746", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "29"}, {"cite": "1886 U.S. LEXIS 1806", "page": "1806", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1886"}, {"cite": "3 A.F.T.R. (P-H) 2488", "page": "2488", "reporter": "A.F.T.R. (P-H)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "3"}], "display": "116 U.S. 616", "official": {"cite": "116 U.S. 616", "page": "616", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "116"}, "official_selection_present": true, "record_id": "Boyd v. United States"}}
{"assertion_id": "3ee5e0e6ae73f8f3", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-626", "record_id": "Boyd v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-626", "pinpoint_status": "slip-only", "quote": "to mean — and, in answering, whether *Entick v. Carrington* states the foundational principle the Amendment embodies. ## Rule The Court adopted Lord Camden's judgment in *Entick v. Carrington* as the constitutional touchstone. Every American statesman of the founding era", "quote_fidelity": "mismatch", "record_id": "Boyd v. United States", "star_marker": null}}
{"assertion_id": "7148a86dca275da1", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-627", "record_id": "Boyd v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-627", "pinpoint_status": "slip-only", "quote": "propositions were in the minds of those who framed the Fourth Amendment to the Constitution, and were considered as sufficiently explanatory of what was meant by unreasonable searches and seizures.", "quote_fidelity": "mismatch", "record_id": "Boyd v. United States", "star_marker": null}}
{"assertion_id": "83dcccbd91c75b2d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Boyd v. United States"}, "payload": {"as_of_content": "1886-02-01", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "Boyd v. United States", "scope_note": "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment — the proposition for which it is cited here — remains good law and is frequently cited.", "varies_by_point": true}}
```

### lake record — Boyd v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Boyd v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Boyd v. United States",
    "case_name_short": "Boyd",
    "case_name_full": "Boyd v. United States",
    "input_case_name": "Boyd v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1886-02-01",
    "year": 1886,
    "docket": null,
    "cluster_id": 91573,
    "lead_opinion_id": 91573,
    "sibling_ids": [
      91573,
      9417418,
      9417419
    ],
    "absolute_url": "/opinion/91573/boyd-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "116 U.S. 616",
      "volume": "116",
      "reporter": "U.S.",
      "page": "616",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "6 S. Ct. 524",
        "volume": "6",
        "reporter": "S. Ct.",
        "page": "524",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 746",
        "volume": "29",
        "reporter": "L. Ed.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 A.F.T.R. (P-H) 2488",
        "volume": "3",
        "reporter": "A.F.T.R. (P-H)",
        "page": "2488",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1886 U.S. LEXIS 1806",
        "volume": "1886",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "116 U.S. 616",
        "volume": "116",
        "reporter": "U.S.",
        "page": "616",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "6 S. Ct. 524",
        "volume": "6",
        "reporter": "S. Ct.",
        "page": "524",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "29 L. Ed. 746",
        "volume": "29",
        "reporter": "L. Ed.",
        "page": "746",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1886 U.S. LEXIS 1806",
        "volume": "1886",
        "reporter": "U.S. LEXIS",
        "page": "1806",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "3 A.F.T.R. (P-H) 2488",
        "volume": "3",
        "reporter": "A.F.T.R. (P-H)",
        "page": "2488",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "116 U.S. 616",
    "official_selection": {
      "court_class": "scotus",
      "selected": "116 U.S. 616",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-626",
      "page": null,
      "quote": "to mean \u2014 and, in answering, whether *Entick v. Carrington* states the foundational principle the Amendment embodies. ## Rule The Court adopted Lord Camden's judgment in *Entick v. Carrington* as the constitutional touchstone. Every American statesman of the founding era",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-627",
      "page": null,
      "quote": "propositions were in the minds of those who framed the Fourth Amendment to the Constitution, and were considered as sufficiently explanatory of what was meant by unreasonable searches and seizures.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "1886-02-01",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Boyd v. United States",
    "varies_by_point": true,
    "scope_note": "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment \u2014 the proposition for which it is cited here \u2014 remains good law and is frequently cited.",
    "point_overrides": [
      {
        "point": "legacy-limited-boyd-v-united-states",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Warden v. Hayden",
            "cluster_id": 107465,
            "cite": "387 U.S. 294",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Boyd's holding that compelling production of private papers violates the Fourth/Fifth Amendments, and its 'mere evidence' rule, have been abandoned (Warden v. Hayden) and sharply limited (Fisher v. United States). Boyd's account of Entick v. Carrington as the historical foundation of the Fourth Amendment \u2014 the proposition for which it is cited here \u2014 remains good law and is frequently cited."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Warden v. Hayden",
          "cluster_id": 107465,
          "cite": "387 U.S. 294",
          "field_ii": "limited"
        },
        "field_ii": "limited",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "migration:limited"
      },
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
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Pittman",
          "cluster_id": 10160783,
          "cite": [
            "367 Or. 498",
            "479 P.3d 1028"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Krystal Wagner, Individually and as Administrator of the Estate of Shane Jensen v. State of Iowa and William L. Spece a/k/a Bill L. Spece",
          "cluster_id": 4844322,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Wheeler v. State",
          "cluster_id": 3182294,
          "cite": [
            "135 A.3d 282",
            "2016 Del. LEXIS 121",
            "2016 WL 825395"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane1_negative"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roe v. Wade",
          "cluster_id": 108713,
          "cite": [
            "35 L. Ed. 2d 147",
            "93 S. Ct. 705",
            "410 U.S. 113",
            "1973 U.S. LEXIS 159"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Bostick",
          "cluster_id": 112631,
          "cite": [
            "115 L. Ed. 2d 389",
            "111 S. Ct. 2382",
            "501 U.S. 429",
            "1991 U.S. LEXIS 3625",
            "59 U.S.L.W. 4708",
            "91 Daily Journal DAR 7328",
            "91 Cal. Daily Op. Serv. 4671",
            "1991 WL 105224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gerstein v. Pugh",
          "cluster_id": 109186,
          "cite": [
            "43 L. Ed. 2d 54",
            "95 S. Ct. 854",
            "420 U.S. 103",
            "1975 U.S. LEXIS 29",
            "19 Fed. R. Serv. 2d 1499"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griswold v. Connecticut",
          "cluster_id": 107082,
          "cite": [
            "14 L. Ed. 2d 510",
            "85 S. Ct. 1678",
            "381 U.S. 479",
            "1965 U.S. LEXIS 2282"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Weeks v. United States",
          "cluster_id": 98094,
          "cite": [
            "232 U.S. 383",
            "34 S. Ct. 341",
            "58 L. Ed. 652",
            "1914 U.S. LEXIS 1368"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Boyd v. United States:lane2_top_cited"
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
        "journal_ref": "Boyd v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(91573 OR 9417418 OR 9417419) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzE5MDY4ODAwMDAwJnM9MjMzMjY4NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%2891573+OR+9417418+OR+9417419%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 11,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(91573 OR 9417418 OR 9417419)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDM2JnM9MTA5NDMyJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%2891573+OR+9417418+OR+9417419%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(91573 OR 9417418 OR 9417419)",
        "reviewed": 33,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 33,
        "triage_read": 0,
        "triage_snippet_classified": 33
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(91573 OR 9417418 OR 9417419)",
    "indexed_citing_opinions": 2274,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 91573,
        "count": 2081,
        "count_source": "search"
      },
      {
        "opinion_id": 9417418,
        "count": 242,
        "count_source": "search"
      },
      {
        "opinion_id": 9417419,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3820,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/boyd-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg3OTQxNCZzPTk1MDA5NTImdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%2891573+OR+9417418+OR+9417419%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "LRU",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-04T20:12:41Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:13:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:13:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:31Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:13:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Boyd v. United States

```
<div>
<center><b><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U.S. 616</a></span> (1886)</b></center>
<center><h1>BOYD<br>
v.<br>
UNITED STATES.</h1></center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 11, 14, 1885.</center>
<center>Decided February 1, 1886.</center>
ERROR TO THE CIRCUIT COURT OF THE UNITED STATES FOR THE SOUTHERN DISTRICT OF NEW YORK.
<p><span class="star-pagination">*617</span> <i>Mr. Edwin B. Smith</i> for plaintiff in error. <i>Mr. Stephen G. Clarke</i> was with him on the brief.</p>
<p><i>Mr. Solicitor-General</i> for defendant in error.</p>
<p>MR. JUSTICE BRADLEY delivered the opinion of the court.</p>
<p>This was an information filed by the District Attorney of the United States in the District Court for the Southern District of New York, in July, 1884, in a cause of seizure and forfeiture of property, against thirty-five cases of plate glass, seized by the collector as forfeited to the United States, under § 12 of the "Act to amend the customs revenue laws, and to repeal moieties," passed June 22, 1874. <span class="citation no-link">18 Stat. 186</span>.</p>
<p>It is declared by that section that any owner, importer, consignee, &amp;c., who shall, with intent to defraud the revenue, make, or attempt to make, any entry of imported merchandise, by means of any fraudulent or false invoice, affidavit, letter or paper, or by means of any false statement, written or verbal, or who shall be guilty of any wilful act or omission by means whereof the United States shall be deprived of the lawful duties, or any portion thereof, accruing upon the merchandise, or any portion thereof, embraced or referred to in such invoice, affidavit, letter, paper, or statement, or affected by such act or omission, shall for each offence be fined in any sum not exceeding $5000 nor less than $50, or be imprisoned for any time not exceeding two years, or both; and, in addition to such fine, such merchandise shall be forfeited.</p>
<p>The charge was that the goods in question were imported <span class="star-pagination">*618</span> into the United States to the port of New York, subject to the payment of duties; and that the owners or agents of said merchandise, or other person unknown, committed the alleged fraud, which was described in the words of the statute. The plaintiffs in error entered a claim for the goods, and pleaded that they did not become forfeited in manner and form as alleged. On the trial of the cause it became important to show the quantity and value of the glass contained in twenty-nine cases previously imported. To do this the district attorney offered in evidence an order made by the District Judge under § 5 of the same act of June 22, 1874, directing notice under seal of the court to be given to the claimants, requiring them to produce the invoice of the twenty-nine cases. The claimants, in obedience to the notice, but objecting to its validity and to the constitutionality of the law, produced the invoice; and when it was offered in evidence by the district attorney they objected to its reception on the ground that, in a suit for forfeiture, no evidence can be compelled from the claimants themselves, and also that the statute, so far as it compels production of evidence to be used against the claimants is unconstitutional and void.</p>
<p>The evidence being received, and the trial closed, the jury found a verdict for the United States, condemning the thirty-five cases of glass which were seized, and judgment of forfeiture was given. This judgment was affirmed by the Circuit Court, and the decision of that court is now here for review.</p>
<p>As the question raised upon the order for the production by the claimants of the invoice of the twenty-nine cases of glass, and the proceedings had thereon, is not only an important one in the determination of the present case, but is a very grave question of constitutional law, involving the personal security, and privileges and immunities of the citizen, we will set forth the order at large. After the title of the court and term, it reads as follows, to wit:</p>
         "The United States of America           |
                    <i>against</i>                       &gt;
E.A.B., 1-35, Thirty-five Cases of Plate Glass.  |
<p>"Whereas the attorney of the United States for the Southern <span class="star-pagination">*619</span> District of New York has filed in this court a written motion in the above-entitled action, showing that said action is a suit or proceeding other than criminal, arising under the customs revenue laws of the United States, and not for penalties, now pending undetermined in this court, and that in his belief a certain invoice or paper belonging to and under the control of the claimants herein will tend to prove certain allegations set forth in said written motion, hereto annexed, made by him on behalf of the United States in said action, to wit, the invoice from the Union Plate Glass Company or its agents, covering the twenty-nine cases of plate glass marked G.H.B., imported from Liverpool, England, into the port of New York in the vessel Baltic, and entered by E.A. Boyd &amp; Sons at the office of the collector of customs of the port and collection district aforesaid on April 7th, 1884, on entry No. 47,108:</p>
<p>"Now, therefore, by virtue of the power in the said court vested by section 5 of the act of June 22, 1874, entitled `An act to amend the customs-revenue laws and to repeal moieties,' it is ordered that a notice under the seal of this court, and signed by the clerk thereof, be issued to the claimants, requiring them to produce the invoice or paper aforesaid before this court in the court-rooms thereof in the United States post-office and court-house building in the city of New York on October 16th, 1884, at eleven o'clock a.m., and thereafter at such other times as the court shall appoint, and that said United States attorney and his assistants and such persons as he shall designate shall be allowed before the court, and under its direction and in the presence of the attorneys for the claimants, if they shall attend, to make examination of said invoice or paper and to take copies thereof; but the claimants or their agents or attorneys shall have, subject to the order of the court, the custody of such invoice or paper, except pending such examination."</p>
<p>The 5th section of the act of June 22, 1874, under which this order was made, is in the following words, to wit:</p>
<p>"In all suits and proceedings other than criminal arising under any of the revenue laws of the United States, the attorney representing the government, whenever in his belief any <span class="star-pagination">*620</span> business book, invoice, or paper belonging to, or under the control of, the defendant or claimant, will tend to prove any allegation made by the United States, may make a written motion, particularly describing such book, invoice, or paper, and setting forth the allegation which he expects to prove; and thereupon the court in which suit or proceeding is pending may, at its discretion, issue a notice to the defendant or claimant to produce such book, invoice, or paper in court, at a day and hour to be specified in said notice, which, together with a copy of said motion, shall be served formally on the defendant or claimant by the United States marshal by delivering to him a certified copy thereof, or otherwise serving the same as original notices of suit in the same court are served; and if the defendant or claimant shall fail or refuse to produce such book, invoice, or paper in obedience to such notice, the allegations stated in the said motion shall be taken as confessed, unless his failure or refusal to produce the same shall be explained to the satisfaction of the court. And if produced the said attorney shall be permitted, under the direction of the court, to make examination (at which examination the defendant, or claimant, or his agent, may be present) of such entries in said book, invoice, or paper as relate to or tend to prove the allegation aforesaid, and may offer the same in evidence on behalf of the United States. But the owner of said books and papers, his agent or attorney, shall have, subject to the order of the court, the custody of them, except pending their examination in court as aforesaid." <span class="citation no-link">18 Stat. 187</span>.</p>
<p>This section was passed in lieu of the 2d section of the act of March 2, 1867, entitled "An act to regulate the Disposition of the Proceeds of Fines, Penalties, and Forfeitures incurred under the Laws relating to the Customs and for other Purposes," <span class="citation no-link">14 Stat. 547</span>, which section of said last-mentioned statute authorized the district judge, on complaint and affidavit that any fraud on the revenue had been committed by any person interested or engaged in the importation of merchandise, to issue his warrant to the marshal to enter any premises where any invoices, books, or papers were deposited relating to such merchandise, and take possession of such books and papers and <span class="star-pagination">*621</span> produce them before said judge, to be subject to his order, and allowed to be examined by the collector, and to be retained as long as the judge should deem necessary. This law being in force at the time of the revision, was incorporated into §§ 3091, 3092, 3093 of the Revised Statutes.</p>
<p>The section last recited was passed in lieu of the 7th section of the act of March 3, 1863, entitled "An act to prevent and punish Frauds upon the Revenue, to provide for the more certain and speedy Collection of Claims in Favor of the United States, and for other Purposes." <span class="citation no-link">12 Stat. 737</span>. The 7th section of this act was in substance the same as the 2d section of the act of 1867, except that the warrant was to be directed to the collector instead of the marshal. It was the first legislation of the kind that ever appeared on the statute book of the United States, and, as seen from its date, was adopted at a period of great national excitement, when the powers of the government were subjected to a severe strain to protect the national existence.</p>
<p>The clauses of the Constitution, to which it is contended that these laws are repugnant, are the Fourth and Fifth Amendments. The Fourth declares, "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized." The Fifth Article, amongst other things, declares that no person "shall be compelled in any criminal case to be a witness against himself."</p>
<p>But, in regard to the Fourth Amendment, it is contended that, whatever might have been alleged against the constitutionality of the acts of 1863 and 1867, that of 1874, under which the order in the present case was made, is free from constitutional objection, because it does not authorize the search and seizure of books and papers, but only requires the defendant or claimant to produce them. That is so; but it declares that if he does not produce them, the allegations which it is affirmed they will prove shall be taken as confessed. This is tantamount <span class="star-pagination">*622</span> to compelling their production; for the prosecuting attorney will always be sure to state the evidence expected to be derived from them as strongly as the case will admit of. It is true that certain aggravating incidents of actual search and seizure, such as forcible entry into a man's house and searching amongst his papers, are wanting, and to this extent the proceeding under the act of 1874 is a mitigation of that which was authorized by the former acts; but it accomplishes the substantial object of those acts in forcing from a party evidence against himself. It is our opinion, therefore, that a compulsory production of a man's private papers to establish a criminal charge against him, or to forfeit his property, is within the scope of the Fourth Amendment to the Constitution, in all cases in which a search and seizure would be; because it is a material ingredient, and effects the sole object and purpose of search and seizure.</p>
<p>The principal question, however, remains to be considered. Is a search and seizure, or, what is equivalent thereto, a compulsory production of a man's private papers, to be used in evidence against him in a proceeding to forfeit his property for alleged fraud against the revenue laws  is such a proceeding for such a purpose an "<i>unreasonable</i> search and seizure" within the meaning of the Fourth Amendment of the Constitution? or, is it a legitimate proceeding? It is contended by the counsel for the government, that it is a legitimate proceeding, sanctioned by long usage, and the authority of judicial decision. No doubt long usage, acquiesced in by the courts, goes a long way to prove that there is some plausible ground or reason for it in the law, or in the historical facts which have imposed a particular construction of the law favorable to such usage. It is a maxim that, <i>consuetudo est optimus interpres legum;</i> and another maxim that, <i>contemporanea expositio est optima et fortissima in lege.</i> But we do not find any long usage, or any contemporary construction of the Constitution, which would justify any of the acts of Congress now under consideration. As before stated, the act of 1863 was the first act in this country, and, we might say, either in this country or in England, so far as we have been able to ascertain, which authorized the <span class="star-pagination">*623</span> search and seizure of a man's private papers, or the compulsory production of them, for the purpose of using them in evidence against him in a criminal case, or in a proceeding to enforce the forfeiture of his property. Even the act under which the obnoxious writs of assistance were issued<sup>[*]</sup> did not go as far as this, but only authorized the examination of ships and vessels, and persons found therein, for the purpose of finding goods prohibited to be imported or exported, or on which the duties were not paid, and to enter into and search any suspected vaults, cellars, or warehouses for such goods. The search for and seizure of stolen or forfeited goods, or goods liable to duties and concealed to avoid the payment thereof, are totally different things from a search for and seizure of a man's private books and papers for the purpose of obtaining information therein contained, or of using them as evidence against him. The two things differ <i>toto clo.</i> In the one case, the government is entitled to the possession of the property; in the other it is not. The seizure of stolen goods is authorized by the common law; and the seizure of goods forfeited for a breach of the revenue laws, or concealed to avoid the duties payable on them, has been authorized by English statutes for at least two centuries past;<sup>[]</sup> and the like seizures have been authorized by our own revenue acts from the commencement of the government. The first statute passed by Congress to regulate the collection of duties, the act of July 31, 1789, <span class="citation no-link">1 Stat. 29</span>, 43, contains provisions to this effect. As this act was passed by the same Congress which proposed for adoption the original amendments to the Constitution, it is clear that the members of that body did not regard searches and seizures of this kind as "unreasonable," and they are not embraced within the prohibition of the amendment. So, also, the supervision authorized to be exercised by officers of the revenue over the manufacture or custody of excisable articles, and the entries thereof in books required by law <span class="star-pagination">*624</span> to be kept for their inspection, are necessarily excepted out of the category of unreasonable searches and seizures. So, also, the laws which provide for the search and seizure of articles and things which it is unlawful for a person to have in his possession for the purpose of issue or disposition, such as counterfeit coin, lottery tickets, implements of gambling, &amp;c., are not within this category. <i>Commonwealth</i> v. <i>Dana,</i> 2 Met. (Mass.) 329. Many other things of this character might be enumerated. The entry upon premises, made by a sheriff or other officer of the law, for the purpose of seizing goods and chattels by virtue of a judicial writ, such as an attachment, a sequestration, or an execution, is not within the prohibition of the Fourth or Fifth Amendment, or any other clause of the Constitution; nor is the examination of a defendant under oath after an ineffectual execution, for the purpose of discovering secreted property or credits, to be applied to the payment of a judgment against him, obnoxious to those amendments.</p>
<p>But, when examined with care, it is manifest that there is a total unlikeness of these official acts and proceedings to that which is now under consideration. In the case of stolen goods, the owner from whom they were stolen is entitled to their possession; and in the case of excisable or dutiable articles, the government has an interest in them for the payment of the duties thereon, and until such duties are paid has a right to keep them under observation, or to pursue and drag them from concealment; and in the case of goods seized on attachment or execution, the creditor is entitled to their seizure in satisfaction of his debt; and the examination of a defendant under oath to obtain a discovery of concealed property or credits is a proceeding merely civil to effect the ends of justice, and is no more than what the court of chancery would direct on a bill for discovery. Whereas, by the proceeding now under consideration, the court attempts to extort from the party his private books and papers to make him liable for a penalty or to forfeit his property.</p>
<p>In order to ascertain the nature of the proceedings intended by the Fourth Amendment to the Constitution under the terms "unreasonable searches and seizures," it is only necessary to <span class="star-pagination">*625</span> recall the contemporary or then recent history of the controversies on the subject, both in this country and in England. The practice had obtained in the colonies of issuing writs of assistance to the revenue officers, empowering them, in their discretion, to search suspected places for smuggled goods, which James Otis pronounced "the worst instrument of arbitrary power, the most destructive of English liberty, and the fundamental principles of law, that ever was found in an English law book;" since they placed "the liberty of every man in the hands of every petty officer."<sup>[*]</sup> This was in February, 1761, in Boston, and the famous debate in which it occurred was perhaps the most prominent event which inaugurated the resistance of the colonies to the oppressions of the mother country. "Then and there," said John Adams, "then and there was the first scene of the first act of opposition to the arbitrary claims of Great Britain. Then and there the child Independence was born."</p>
<p>These things, and the events which took place in England immediately following the argument about writs of assistance in Boston, were fresh in the memories of those who achieved our independence and established our form of government. In the period from 1762, when the North Briton was started by John Wilkes, to April, 1766, when the House of Commons passed resolutions condemnatory of general warrants, whether for the seizure of persons or papers, occurred the bitter controversy between the English government and Wilkes, in which the latter appeared as the champion of popular rights, and was, indeed, the pioneer in the contest which resulted in the abolition of some grievous abuses which had gradually crept into the administration of public affairs. Prominent and principal among these was the practice of issuing general <span class="star-pagination">*626</span> warrants by the Secretary of State, for searching private houses for the discovery and seizure of books and papers that might be used to convict their owner of the charge of libel. Certain numbers of the North Briton, particularly No. 45, had been very bold in denunciation of the government, and were esteemed heinously libellous. By authority of the secretary's warrant Wilkes's house was searched, and his papers were indiscriminately seized. For this outrage he sued the perpetrators and obtained a verdict of £1000 against Wood, one of the party who made the search, and £4000 against Lord Halifax, the Secretary of State who issued the warrant. The case, however, which will always be celebrated as being the occasion of Lord Camden's memorable discussion of the subject, was that of <i>Entick</i> v. <i>Carrington and Three Other King's Messengers,</i> reported at length in 19 Howell's State Trials, 1029. The action was trespass for entering the plaintiff's dwelling-house in November, 1762, and breaking open his desks, boxes, &amp;c., and searching and examining his papers. The jury rendered a special verdict, and the case was twice solemnly argued at the bar. Lord Camden pronounced the judgment of the court in Michaelmas Term, 1765, and the law as expounded by him has been regarded as settled from that time to this, and his great judgment on that occasion is considered as one of the landmarks of English liberty. It was welcomed and applauded by the lovers of liberty in the colonies as well as in the mother country. It is regarded as one of the permanent monuments of the British Constitution, and is quoted as such by the English authorities on that subject down to the present time.<sup>[*]</sup></p>
<p>As every American statesmen, during our revolutionary and formative period as a nation, was undoubtedly familiar with this monument of English freedom, and considered it as the true and ultimate expression of constitutional law, it may be confidently asserted that its propositions were in the minds <span class="star-pagination">*627</span> of those who framed the Fourth Amendment to the Constitution, and were considered as sufficiently explanatory of what was meant by unreasonable searches and seizures. We think, therefore, it is pertinent to the present subject of discussion to quote somewhat largely from this celebrated judgment.</p>
<p>After describing the power claimed by the Secretary of State for issuing general search warrants, and the manner in which they were executed, Lord Camden says: "Such is the power, and, therefore, one would naturally expect that the law to warrant it should be clear in proportion as the power is exorbitant. If it is law, it will be found in our books; if it is not to be found there, it is not law.</p>
<p>"The great end for which men entered into society was to secure their property. That right is preserved sacred and incommunicable in all instances where it has not been taken away or abridged by some public law for the good of the whole. The cases where this right of property is set aside by positive law are various. Distresses, executions, forfeitures, taxes, &amp;c., are all of this description, wherein every man by common consent gives up that right for the sake of justice and the general good. By the laws of England, every invasion of private property, be it ever so minute, is a trespass. No man can set his foot upon my ground without my license, but he is liable to an action though the damage be nothing; which is proved by every declaration in trespass where the defendant is called upon to answer for bruising the grass and even treading upon the soil. If he admits the fact, he is bound to show, by way of justification, that some positive law has justified or excused him. The justification is submitted to the judges, who are to look into the books, and see if such a justification can be maintained by the text of the statute law, or by the principles of the common law. If no such excuse can be found or produced, the silence of the books is an authority, against the defendant, and the plaintiff must have judgment. According to this reasoning, it is now incumbent upon the defendants to show the law by which this seizure is warranted. If that cannot be done, it is a trespass.</p>
<p>"Papers are the owner's goods and chattels; they are his <span class="star-pagination">*628</span> dearest property; and are so far from enduring a seizure, that they will hardly bear an inspection; and though the eye cannot by the laws of England be guilty of a trespass, yet where private papers are removed and carried away the secret nature of those goods will be an aggravation of the trespass, and demand more considerable damages in that respect. Where is the written law that gives any magistrate such a power? I can safely answer, there is none; and, therefore, it is too much for us, without such authority, to pronounce a practice legal which would be subversive of all the comforts of society.</p>
<p>"But though it cannot be maintained by any direct law, yet it bears a resemblance, as was urged, to the known case of search and seizure for stolen goods. I answer that the difference is apparent. In the one, I am permitted to seize my own goods, which are placed in the hands of a public officer, till the felon's conviction shall entitle me to restitution. In the other, the party's own property is seized before and without conviction, and he has no power to reclaim his goods, even after his innocence is declared by acquittal.</p>
<p>"The case of searching for stolen goods crept into the law by imperceptible practice. No less a person than my Lord Coke denied its legality, 4 Inst. 176; and, therefore, if the two cases resembled each other more than they do, we have no right, without an act of Parliament, to adopt a new practice in the criminal law, which was never yet allowed from all antiquity. Observe, too, the caution with which the law proceeds in this singular case. There must be a full charge upon oath of a theft committed. The owner must swear that the goods are lodged in such a place. He must attend at the execution of the warrant, to show them to the officer, who must see that they answer the description... .</p>
<p>"If it should be said that the same law which has with so much circumspection guarded the case of stolen goods from mischief, would likewise in this case protect the subject by adding proper checks; would require proofs beforehand; would call up the servant to stand by and overlook; would require him to take an exact inventory, and deliver a copy: my answer is, that all these precautions would have been long <span class="star-pagination">*629</span> since established by law, if the power itself had been legal; and that the want of them is an undeniable argument against the legality of the thing."</p>
<p>Then, after showing that these general warrants for search and seizure of papers originated with the Star Chamber, and never had any advocates in Westminster Hall except Chief Justice Scroggs and his associates, Lord Camden proceeds to add:</p>
<p>"Lastly, it is urged as an argument of utility, that such a search is a means of detecting offenders by discovering evidence. I wish some cases had been shown, where the law forceth evidence out of the owner's custody by process. There is no process against papers in civil causes. It has been often tried, but never prevailed. Nay, where the adversary has by force or fraud got possession of your own proper evidence, there is no way to get it back but by action. In the criminal law such a proceeding was never heard of; and yet there are some crimes, such, for instance, as murder, rape, robbery, and house-breaking, to say nothing of forgery and perjury, that are more atrocious than libelling. But our law has provided no paper-search in these cases to help forward the conviction. Whether this proceedeth from the gentleness of the law towards criminals, or from a consideration that such a power would be more pernicious to the innocent than useful to the public, I will not say. It is very certain that the law obligeth no man to accuse himself; because the necessary means of compelling self-accusation, falling upon the innocent as well as the guilty, would be both cruel and unjust; and it would seem, that search for evidence is disallowed upon the same principle. Then, too, the innocent would be confounded with the guilty."</p>
<p>After a few further observations, his Lordship concluded thus: "I have now taken notice of everything that has been urged upon the present point; and upon the whole we are all of opinion, that the warrant to seize and carry away the party's papers in the case of a seditious libel, is illegal and void."<sup>[*]</sup></p>
<p><span class="star-pagination">*630</span> The principles laid down in this opinion affect the very essence of constitutional liberty and security. They reach farther than the concrete form of the case then before the court, with its adventitious circumstances; they apply to all invasions on the part of the government and its employés of the sanctity of a man's home and the privacies of life. It is not the breaking of his doors, and the rummaging of his drawers, that constitutes the essence of the offence; but it is the invasion of his indefeasible right of personal security, personal liberty and private property, where that right has never been forfeited by his conviction of some public offence,  it is the invasion of this sacred right which underlies and constitutes the essence of Lord Camden's judgment. Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime or to forfeit his goods, is within the condemnation of that judgment. In this regard the Fourth and Fifth Amendments run almost into each other.</p>
<p>Can we doubt that when the Fourth and Fifth Amendments to the Constitution of the United States were penned and adopted, the language of Lord Camden was relied on as expressing the true doctrine on the subject of searches and seizures, and as furnishing the true criteria of the reasonable and "unreasonable" character of such seizures? Could the men who proposed those amendments, in the light of Lord Camden's opinion, have put their hands to a law like those of March 3, 1863, and March 2, 1867, before recited? If they could not, would they have approved the 5th section of the act of June 22, 1874, which was adopted as a substitute for the previous laws? It seems to us that the question cannot admit of a doubt. They never would have approved of them. The struggles against arbitrary power in which they had been engaged for more than twenty years, would have been too deeply engraved in their memories to have allowed them to approve of such insidious disguises of the old grievance which they had so deeply abhorred.</p>
<p>The views of the first Congress on the question of compelling <span class="star-pagination">*631</span> a man to produce evidence against himself may be inferred from a remarkable section of the judiciary act of 1789. The 15th section of that act introduced a great improvement in the law of procedure. The substance of it is found in § 724 of the Revised Statutes, and the section as originally enacted is as follows, to wit:</p>
<p>"All the said courts of the United States shall have power in the trial of actions at law, on motion and due notice thereof being given, to require the parties to produce books or writings in their possession or power, which contain evidence pertinent to the issue, <i>in cases and under circumstances where they might be compelled to produce the same by the ordinary rules of proceeding in chancery;</i> and if a plaintiff shall fail to comply with such order to produce books or writings, it shall be lawful for the courts respectively, on motion, to give the like judgment for the defendant as in cases of nonsuit; and if a defendant shall fail to comply with such order to produce books or writings, it shall be lawful for the courts respectively, on motion as aforesaid, to give judgment against him or her by default."<sup>[*]</sup></p>
<p>The restriction of this proceeding to "cases and under circumstances where they [the parties] might be compelled to produce the same [books or writings] by the ordinary rules of proceeding in chancery," shows the wisdom of the Congress of 1789. The court of chancery had for generations been weighing and balancing the rules to be observed in granting discovery on bills filed for that purpose, in the endeavor to fix upon such as would best secure the ends of justice. To go beyond the point to which that court had gone may well have been thought hazardous. Now it is elementary knowledge, that one cardinal rule of the court of chancery is never to decree a discovery which might tend to convict the party of a crime, or to forfeit his property.<sup>[]</sup> And any compulsory discovery by extorting the party's oath, or compelling the production of his <span class="star-pagination">*632</span> private books and papers, to convict him of crime, or to forfeit his property, is contrary to the principles of a free government. It is abhorrent to the instincts of an Englishman; it is abhorrent to the instincts of an American. It may suit the purposes of despotic power; but it cannot abide the pure atmosphere of political liberty and personal freedom.</p>
<p>It is proper to observe that when the objectionable features of the acts of 1863 and 1867 were brought to the attention of Congress, it passed an act to obviate them. By the act of February 25, 1868, <span class="citation no-link">15 Stat. 37</span>, entitled "An act for the Protection in certain Cases of Persons making Disclosures as Parties, or testifying as Witnesses," the substance of which is incorporated in § 860 of the Revised Statutes, it was enacted "that no answer or other pleading of any party, and no discovery, or evidence obtained by means of any judicial proceeding from any party or witness in this or any foreign country, shall be given in evidence, or in any manner used against such party or witness, or his property or estate, in any court of the United States, or in any proceeding by or before any officer of the United States, in respect to any crime, or for the enforcement of any penalty or forfeiture by reason of any act or omission of such party or witness."</p>
<p>This act abrogated and repealed the most objectionable part of the act of 1867 (which was then in force) and deprived the government officers of the convenient method afforded by it for getting evidence in suits of forfeiture; and this is probably the reason why the 5th section of the act of 1874 was afterwards passed. No doubt it was supposed that in this new form, couched as it was in almost the language of the 15th section of the old judiciary act, except leaving out the restriction to cases in which the court of chancery would decree a discovery, it would be free from constitutional objection. But we think it has been made to appear that this result has not been attained; and that the law, though very speciously worded, is still obnoxious to the prohibition of the Fourth Amendment of the Constitution, as well as of the Fifth.</p>
<p>It has been thought by some respectable members of the profession that the two acts, that of 1868 and that of 1874, as being in <i>pari materia,</i> might be construed together so as to restrict <span class="star-pagination">*633</span> the operation of the latter to cases other than those of forfeiture; and that such a construction of the two acts would obviate the necessity of declaring the act of 1874 unconstitutional. But as the act of 1874 was intended as a revisory act on the subject of revenue frauds and prosecutions therefor, and as it expressly repeals the 2d section of the act of 1867, but does not repeal the act of 1868, and expressly excepts criminal suits and proceedings, and does not except suits for penalties and forfeitures, it would hardly be admissible to consider the act of 1868 as having any influence over the construction of the act of 1874. For the purposes of this discussion we must regard the 5th section of the latter act as independent of the act of 1868.</p>
<p>Reverting then to the peculiar phraseology of this act, and to the information in the present case, which is founded on it, we have to deal with an act which expressly excludes criminal proceedings from its operation (though embracing civil suits for penalties and forfeitures), and with an information not technically a criminal proceeding, and neither, therefore, within the literal terms of the Fifth Amendment to the Constitution any more than it is within the literal terms of the Fourth. Does this relieve the proceedings or the law from being obnoxious to the prohibitions of either? We think not; we think they are within the spirit of both.</p>
<p>We have already noticed the intimate relation between the two amendments. They throw great light on each other. For the "unreasonable searches and seizures" condemned in the Fourth Amendment are almost always made for the purpose of compelling a man to give evidence against himself, which in criminal cases is condemned in the Fifth Amendment; and compelling a man "in a criminal case to be a witness against himself," which is condemned in the Fifth Amendment, throws light on the question as to what is an "unreasonable search and seizure" within the meaning of the Fourth Amendment. And we have been unable to perceive that the seizure of a man's private books and papers to be used in evidence against him is substantially different from compelling him to be a witness against himself. We think it is within the clear intent and meaning of those terms. We are also clearly of opinion that <span class="star-pagination">*634</span> proceedings instituted for the purpose of declaring the forfeiture of a man's property by reason of offences committed by him, though they may be civil in form, are in their nature criminal. In this very case, the ground of forfeiture as declared in the 12th section of the act of 1874, on which the information is based, consists of certain acts of fraud committed against the public revenue in relation to imported merchandise, which are made criminal by the statute; and it is declared, that the offender shall be fined not exceeding $5000 nor less than $50, or be imprisoned not exceeding two years, or both; and in addition to such fine such merchandise shall be forfeited. These are the penalties affixed to the criminal acts; the forfeiture sought by this suit being one of them. If an indictment had been presented against the claimants, upon conviction the forfeiture of the goods could have been included in the judgment. If the government prosecutor elects to waive an indictment, and to file a civil information against the claimants  that is, civil in form  can he by this device take from the proceeding its criminal aspect and deprive the claimants of their immunities as citizens, and extort from them a production of their private papers, or, as an alternative, a confession of guilt? This cannot be. The information, though technically a civil proceeding, is in substance and effect a criminal one. As showing the close relation between the civil and criminal proceedings on the same statute in such cases, we may refer to the recent case of <i>Coffey</i> v. <i>The United States, ante,</i> 436; in which we decided that an acquittal on a criminal information was a good plea in bar to a civil information for the forfeiture of goods, arising upon the same acts. As, therefore, suits for penalties and forfeitures incurred by the commission of offences against the law, are of this quasi-criminal nature, we think that they are within the reason of criminal proceedings for all the purposes of the Fourth Amendment of the Constitution, and of that portion of the Fifth Amendment which declares that no person shall be compelled in any criminal case to be a witness against himself; and we are further of opinion that a compulsory production of the private books and papers of the owner of goods sought to be forfeited in such a suit is compelling <span class="star-pagination">*635</span> him to be a witness against himself, within the meaning of the Fifth Amendment to the Constitution, and is the equivalent of a search and seizure  and an unreasonable search and seizure  within the meaning of the Fourth Amendment. Though the proceeding in question is divested of many of the aggravating incidents of actual search and seizure, yet, as before said, it contains their substance and essence, and effects their substantial purpose. It may be that it is the obnoxious thing in its mildest and least repulsive form; but illegitimate and unconstitutional practices get their first footing in that way, namely, by silent approaches and slight deviations from legal modes of procedure. This can only be obviated by adhering to the rule that constitutional provisions for the security of person and property should be liberally construed. A close and literal construction deprives them of half their efficacy, and leads to gradual depreciation of the right, as if it consisted more in sound than in substance. It is the duty of courts to be watchful for the constitutional rights of the citizen, and against any stealthy encroachments thereon. Their motto should be <i>obsta principiis.</i> We have no doubt that the legislative body is actuated by the same motives; but the vast accumulation of public business brought before it sometimes prevents it, on a first presentation, from noticing objections which become developed by time and the practical application of the objectionable law.</p>
<p>There have been several decisions in the Circuit and District Courts sustaining the constitutionality of the law under consideration, as well as the prior laws of 1863 and 1867. The principal of these are <i>Stockwell</i> v. <i>United States,</i> 3 Clifford, 284; <i>In re Platt and Boyd,</i> <span class="citation" data-id="8635885"><a href="/opinion/8656040/in-re-platt/" aria-description="Citation for case: In re Platt">7 Ben. 261</a></span>; <i>United States</i> v. <i>Hughes,</i> 12 Blatchford, 553; <i>United States</i> v. <i>Mason,</i> <span class="citation" data-id="8639082"><a href="/opinion/8659227/united-states-v-mason/" aria-description="Citation for case: United States v. Mason">6 Bissell, 350</a></span>; <i>United States</i> v. <i>Three Tons of Coal,</i> <span class="citation" data-id="8686970"><a href="/opinion/8703793/united-states-v-three-tons-of-coal/" aria-description="Citation for case: United States v. Three Tons of Coal">6 Bissell, 379</a></span>; <i>United States</i> v. <i>Distillery No. Twenty-eight,</i> <span class="citation" data-id="8638551"><a href="/opinion/8658698/united-states-v-distillery-no-twenty-eight/" aria-description="Citation for case: United States v. Distillery No. Twenty-Eight">6 Bissell, 483</a></span>. The first and leading case was that of <i>Stockwell</i> v. <i>United States</i><i>,</i> decided by Mr. Justice Clifford and Judge Shepley, the law under discussion being that of 1867. Justice Clifford delivered the opinion, and relied principally upon the collection statutes, which authorized the seizure of goods liable to duty, as being a contemporaneous <span class="star-pagination">*636</span> exposition of the amendments, and as furnishing precedents of analogous laws to that complained of. As we have already considered the bearing of these laws on the subject of discussion, it is unnecessary to say anything more in relation to them. The learned justice seemed to think that the power to institute such searches and seizures as the act of 1867 authorized, was necessary to the efficient collection of the revenue, and that no greater objection can be taken to a warrant to search for books, invoices, and other papers appertaining to an illegal importation than to one authorizing a search for the imported goods; and he concluded that, guarded as the new provision is, it is scarcely possible that the citizen can have any just ground of complaint. It seems to us that these considerations fail to meet the most serious objections to the validity of the law. The other cases followed that of <i>Stockwell</i> v. <i>United States</i> as a precedent, with more or less independent discussion of the subject. The case of <i><span class="citation" data-id="8635885"><a href="/opinion/8656040/in-re-platt/" aria-description="Citation for case: In re Platt">Platt and Boyd</a></span>,</i> decided in the District Court for the Southern District of New York, was also under the act of 1867, and the opinion in that case is quite an elaborate one; but, of course, the previous decision of the Circuit Court in the Stockwell case had a governing influence on the District Court. The other cases referred to were under the 5th section of the act of 1874. The case of <i>United States</i> v. <i>Hughes</i> came up, first, before Judge Blatchford in the District Court in 1875. <span class="citation" data-id="8638870"><a href="/opinion/8659015/united-states-v-hughes/" aria-description="Citation for case: United States v. Hughes">8 Ben. 29</a></span>. It was an action of debt to recover a penalty under the customs act, and the judge held that the 5th section of the act of 1874, in its application to suits for penalties incurred before the passage of the act, was an <i>ex post facto</i> law, and therefore, as to them, was unconstitutional and void; but he granted an order <i>pro forma</i> to produce the books and papers required, in order that the objection might come up on the offer to give them in evidence. They were produced in obedience to the order, and offered in evidence by the district attorney, but were not admitted. The district attorney then served upon one of the defendants a subpna <i>duces tecum,</i> requiring him to produce the books and papers; and this being declined, he moved for an order to compel him to produce them; but the Court refused to make such order. The books and <span class="star-pagination">*637</span> papers referred to had been seized under the act of 1867, but were returned to the defendants under a stipulation to produce them on the trial. The defendants relied not only on the unconstitutionality of the laws, but on the act of 1868, before referred to, which prohibited evidence obtained from a party by a judicial proceeding from being used against him in any prosecution for a crime, penalty, or forfeiture. Judgment being rendered for the defendant, the case was carried to the Circuit Court by writ of error, and, in that court, Mr. Justice Hunt held that the act of 1868 referred only to personal testimony or discovery obtained from a party or witness, and not to books or papers wrested from him; and, as to the constitutionality of the law, he merely referred to the case of Stockwell, and the judgment of the District Court was reversed. In view of what has been already said, we think it unnecessary to make any special observations on this decision. In <i>United States</i> v. <i><span class="citation" data-id="8639082"><a href="/opinion/8659227/united-states-v-mason/" aria-description="Citation for case: United States v. Mason">Mason</a></span></i><i>,</i> Judge Blodgett took the distinction that, in proceedings <i>in rem</i> for a forfeiture, the parties are not required by a proceeding under the act of 1874 to testify or furnish evidence against themselves, because the suit is not against them, but against the property. But where the owner of the property has been admitted as a claimant, we cannot see the force of this distinction; nor can we assent to the proposition that the proceeding is not, in effect, a proceeding against the owner of the property, as well as against the goods; for it is his breach of the laws which has to be proved to establish the forfeiture, and it is his property which is sought to be forfeited; and to require such an owner to produce his private books and papers, in order to prove his breach of the laws, and thus to establish the forfeiture of his property, is surely compelling him to furnish evidence against himself. In the words of a great judge, "Goods, as goods, cannot offend, forfeit, unlade, pay duties, or the like, but men whose goods they are."<sup>[*]</sup></p>
<p>The only remaining case decided in the United States courts <span class="star-pagination">*638</span> to which we shall advert is that of <i>United States</i> v. <i><span class="citation" data-id="8638551"><a href="/opinion/8658698/united-states-v-distillery-no-twenty-eight/" aria-description="Citation for case: United States v. Distillery No. Twenty-Eight">Distillery No. Twenty-eight</a></span></i><i>.</i> In that case Judge Gresham adds to the view of Judge Blodgett, in <i>United States</i> v. <i><span class="citation" data-id="8639082"><a href="/opinion/8659227/united-states-v-mason/" aria-description="Citation for case: United States v. Mason">Mason</a></span></i><i>,</i> the further suggestion, that as in a proceeding <i>in rem</i> the owner is not a party, he might be compelled by a subpna <i>duces tecum</i> to produce his books and papers like any other witness; and that the warrant or notice for search and seizure, under the act of 1874, does nothing more. But we cannot say that we are any better satisfied with this supposed solution of the difficulty. The assumption that the owner may be cited as a witness in a proceeding to forfeit his property seems to us gratuitous. It begs the question at issue. A witness, as well as a party, is protected by the law from being compelled to give evidence that tends to criminate him, or to subject his property to forfeiture. <i>Queen</i> v. <i>Newell,</i> Parker, 269; 1 Greenleaf on Evid., §§ 451-453. But, as before said, although the owner of goods, sought to be forfeited by a proceeding <i>in rem,</i> is not the nominal party, he is, nevertheless, the substantial party to the suit; he certainly is so, after making claim and defence; and, in a case like the present, he is entitled to all the privileges which appertain to a person who is prosecuted for a forfeiture of his property by reason of committing a criminal offence.</p>
<p>We find nothing in the decisions to change our views in relation to the principal question at issue.</p>
<p>We think that the notice to produce the invoice in this case, the order by virtue of which it was issued, and the law which authorized the order, were unconstitutional and void, and that the inspection by the district attorney of said invoice, when produced in obedience to said notice, and its admission in evidence by the court, were erroneous and unconstitutional proceedings. We are of opinion, therefore, that</p>
<p><i>The judgment of the Circuit Court should be reversed, and the cause remanded, with directions to award a new trial.</i></p>
<p>MR. JUSTICE MILLER, with whom was the CHIEF JUSTICE, concurring:</p>
<p>I concur in the judgment of the court, reversing that of the Circuit Court, and in so much of the opinion of this court as <span class="star-pagination">*639</span> holds the 5th section of the act of 1874 void as applicable to the present case.</p>
<p>I am of opinion that this is a criminal case within the meaning of that clause of the Fifth Amendment to the Constitution of the United States which declares that no person "shall be compelled in any criminal case to be a witness against himself."</p>
<p>And I am quite satisfied that the effect of the act of Congress is to compel the party on whom the order of the court is served to be a witness against himself. The order of the court under the statute is in effect a subpna <i>duces tecum,</i> and, though the penalty for the witness's failure to appear in court with the criminating papers is not fine and imprisonment, it is one which may be made more severe, namely, to have charges against him of a criminal nature, taken for confessed, and made the foundation of the judgment of the court. That this is within the protection which the Constitution intended against compelling a person to be a witness against himself, is, I think, quite clear.</p>
<p>But this being so, there is no reason why this court should assume that the action of the court below, in requiring a party to produce certain papers as evidence on the trial, authorizes an unreasonable search or seizure of the house, papers, or effects of that party.</p>
<p>There is in fact no search and no seizure authorized by the statute. No order can be made by the court under it which requires or permits anything more than service of notice on a party to the suit. That there may be no mistake as to the effect of the statute and the power to be exercised under it, I give the section here <i>verbatim:</i></p>
<p>"SEC. 5. That in all suits and proceedings other than criminal arising under any of the revenue laws of the United States, the attorney representing the Government, whenever, in his belief, any business book, invoice, or paper, belonging to or under the control of the defendant or claimant, will tend to prove any allegation made by the United States, may make a written motion, particularly describing such book, invoice, or paper, and setting forth the allegation which he expects to prove; and thereupon the court in which suit or proceeding is <span class="star-pagination">*640</span> pending may, at its discretion, issue a notice to the defendant or claimant to produce such book, invoice, or paper, in court, at a day and hour to be specified in said notice, which, together with a copy of said motion, shall be served formally on the defendant or claimant, by the United States marshal, by delivering to him a certified copy thereof, or otherwise serving the same as original notices of suit in the same court are served; and if the defendant or claimant shall fail or refuse to produce such book, invoice, or paper in obedience to such notice, the allegations stated in the said motion shall be taken as confessed, unless his failure or refusal to produce the same shall be explained to the satisfaction of the court. And if produced, the said attorney shall be permitted, under the direction of the court, to make examination (at which examination the defendant or claimant, or his agent, may be present) of such entries in said book, invoice, or paper as relate to or tend to prove the allegation aforesaid, and may offer the same in evidence on behalf of the United States. But the owner of said books and papers, his agent or attorney, shall have, subject to the order of the court, the custody of them, except pending their examination in court as aforesaid." <span class="citation no-link">18 Stat. 187</span>.</p>
<p>Nothing in the nature of a search is here hinted at. Nor is there any seizure, because the party is not required at any time to part with the custody of the papers. They are to be produced in court, and, when produced, the United States attorney is permitted, under the direction of the court, to make examination in presence of the claimant, and may offer in evidence such entries in the books, invoices, or papers as relate to the issue. The act is careful to say that "the owner of said books and papers, his agent or attorney, shall have, subject to the order of the court, the custody of them, except pending their examination in court as aforesaid."</p>
<p>The Fourth Amendment says: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrant shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched and the person or thing to be seized."</p>
<p><span class="star-pagination">*641</span> The things here forbidden are two  search and seizure. And not all searches nor all seizures are forbidden, but only those that are unreasonable. Reasonable searches, therefore, may be allowed, and if the thing sought be found, it may be seized.</p>
<p>But what search does this statute authorize? If the mere service of a notice to produce a paper to be used as evidence, which the party can obey or not as he chooses is a search, then a change has taken place in the meaning of words, which has not come within my reading, and which I think was unknown at the time the Constitution was made. The searches meant by the Constitution were such as led to seizure when the search was successful. But the statute in this case uses language carefully framed to forbid any seizure under it, as I have already pointed out.</p>
<p>While the framers of the Constitution had their attention drawn, no doubt, to the abuses of this power of searching private houses and seizing private papers, as practiced in England, it is obvious that they only intended to restrain the abuse, while they did not abolish the power. Hence it is only <i>unreasonable</i> searches and seizures that are forbidden, and the means of securing this protection was by abolishing searches under warrants, which were called general warrants, because they authorized searches in any place, for any thing.</p>
<p>This was forbidden, while searches founded on affidavits, and made under warrants which described the thing to be searched for, the person and place to be searched, are still permitted.</p>
<p>I cannot conceive how a statute aptly framed to require the production of evidence in a suit by mere service of notice on the party, who has that evidence in his possession, can be held to authorize an unreasonable search or seizure, when no seizure is authorized or permitted by the statute.</p>
<p>I am requested to say that the CHIEF JUSTICE concurs in this opinion.</p>
<h2>NOTES</h2>
<p>[*]  <i>Note by the Court.</i>  13 &amp; 14 Car. 2, c. 11, § 5.</p>
<p>[]  <i>Note by the Court.</i>  12 Car. 2, c. 19; 13 &amp; 14 Car. 2, c. 11; 6 &amp; 7 W. &amp; M., c. 1; 6 Geo. 1, c. 21; 26 Geo. 3, c. 59; 29 Geo. 3, c. 68, § 153; &amp;c.; and see the article "Excise, &amp;c.," in Burn's Justice, and Williams's Justice, <i>passim,</i> and Evans's Statutes, vol. 2, p. 221, sub-pages 176, 190, 225, 361, 431, 447.</p>
<p>[*]  <i>Note by the Court.</i>  Cooley's Constitutional Limitations, 301-303, (5th ed. 368, 369). A very full and interesting account of this discussion will be found in the works of John Adams, vol. 2, Appendix A, pp. 523-525; vol. 10, pp. 183, 233, 244, 256, &amp;c., and in Quincy's Reports, pp. 469-482: and see <i>Paxton's Case,</i> do. 51-57, which was argued in November of the same year (1761). An elaborate history of the writs of assistance is given in the Appendix to Quincy's Reports, above referred to, written by Horace Gray, Jr., Esq., now a member of this court.</p>
<p>[*]  <i>Note by the Court.</i>  See May's Constitutional History of England, vol. 3, (American ed., vol. 2) chap. 11; Broom's Constitutional Law, 558; Cox's Institutions of the English Government, 437.</p>
<p>[*]  <i>Note by the Court.</i>  See further as to searches and seizures, Story on the Constitution, §§ 1901, 1902, and notes; Cooley's Constitutional Limitations, 299, (5th ed. 365); Sedgwick on Stat. and Const. Law, 2d Ed. 498; Wharton Com. on Amer. Law, § 560; <i>Robinson</i> v. <i>Richardson,</i> <span class="citation no-link">13 Gray, 454</span>.</p>
<p>[*]  <i>Note by the Court.</i>  Sixty-two years later a similar act was passed in England, viz., the act of 14 and 15 Vict., c. 99, § 6. See Pollock on Power of Courts to compel production of Documents, 5.</p>
<p>[]  <i>Note by the Court.</i>  See Pollock on Production of Documents, 27; 77 Law. Lib 12 [8].</p>
<p>[*]  <i>Note by the Court.</i>  Vaughan, C.J., in <i>Sheppard</i> v. <i>Gosnold,</i> Vaugh. 159, 172, approved by Ch. Baron Parker in <i>Mitchell qui tam</i> v. <i>Torup,</i> Parker, 227, 236.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Brady v. Maryland.json  (`lake-record`, 3 assertions)

### content_page

```
---
title: "Brady v. Maryland"
type: case
citation: "373 U.S. 83 (1963)"
parallel_cite: "83 S. Ct. 1194; 10 L. Ed. 2d 215"
neutral_cite: 1963 U.S. LEXIS 1615
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-05-13
docket: 490
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-05-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brady v. Maryland
  varies_by_point: false
  scope_note: "Foundational disclosure rule; later refined (not undermined) by Giglio and United States v. Bagley."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106598/brady-v-maryland/"
  cluster_id: 106598
  opinion_id: 106598
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Anchor"
related: ["[[Giglio v. United States]]", "[[United States v. Bagley]]", "[[Kyles v. Whitley]]"]
aliases: ["Brady v. MD"]
tags: ["case", "due-process", "brady", "disclosure", "exculpatory-evidence"]
holding: "The prosecution's suppression of evidence favorable to the accused that is material to guilt or punishment violates due process —…"
lake:
  record_id: Brady v. Maryland
  status: verified
  projected_at: 2026-07-06
---

# Brady v. Maryland

*373 U.S. 83 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Brady and a companion, Boblit, were tried separately for a murder committed in the course of a robbery. Brady admitted participating but insisted Boblit did the actual killing. Before trial Brady's counsel asked to see Boblit's statements; the prosecution turned over several but withheld the one in which Boblit admitted the killing. Brady discovered the withheld confession only after he had been convicted and sentenced to death.

## Issue
Whether the prosecution's suppression of evidence favorable to the accused, requested by the defense and material to guilt or punishment, violates due process.

## Rule
"We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution." — 373 U.S. at 87. ^pin-87

## Application
Boblit's withheld confession was favorable to Brady and material to punishment — it bore directly on his comparative culpability and thus on the sentence. Because the State had suppressed it, due process was violated as to the punishment phase, although the Court agreed the violation did not require relitigating guilt where Brady had admitted his participation.

## Conclusion
The suppression of the favorable, material confession violated due process; the judgment limiting Brady's new trial to the question of punishment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The rule was **extended** to impeachment evidence by [[Giglio v. United States]] and its materiality standard elaborated by [[United States v. Bagley]] and [[Kyles v. Whitley]].

## Appears on
- [[Brady and Giglio]] — *Key — Anchor*

## Sources
- *Brady v. Maryland*, 373 U.S. 83 (1963) — https://www.courtlistener.com/opinion/106598/brady-v-maryland/ — pinpoint: 87.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "665339bf5dadebd9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brady v. Maryland"}, "payload": {"all": [{"cite": "373 U.S. 83", "page": "83", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "373"}, {"cite": "83 S. Ct. 1194", "page": "1194", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "10 L. Ed. 2d 215", "page": "215", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "10"}, {"cite": "1963 U.S. LEXIS 1615", "page": "1615", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1963"}], "display": "373 U.S. 83", "official": {"cite": "373 U.S. 83", "page": "83", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "373"}, "official_selection_present": true, "record_id": "Brady v. Maryland"}}
{"assertion_id": "7cc164fcef6de80e", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-87", "record_id": "Brady v. Maryland"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-87", "pinpoint_status": "slip-only", "quote": "--- # Brady v. Maryland *373 U.S. 83 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Brady and a companion, Boblit, were tried separately for a murder committed in the course of a robbery. Brady admitted participating but insisted Boblit did the actual killing. Before trial Brady's counsel asked to see Boblit's statements; the prosecution turned over several but withheld the one in which Boblit admitted the killing. Brady discovered the withheld confession only after he had been convicted and sentenced to death. ## Issue Whether the prosecution's suppression of evidence favorable to the accused, requested by the defense and material to guilt or punishment, violates due process. ## Rule", "quote_fidelity": "mismatch", "record_id": "Brady v. Maryland", "star_marker": null}}
{"assertion_id": "feacb14c9eb05127", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brady v. Maryland"}, "payload": {"as_of_content": "1963-05-13", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brady v. Maryland", "scope_note": "Foundational disclosure rule; later refined (not undermined) by Giglio and United States v. Bagley.", "varies_by_point": false}}
```

### lake record — Brady v. Maryland

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brady v. Maryland",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brady v. Maryland",
    "case_name_short": "Brady",
    "case_name_full": "Brady v. Maryland",
    "input_case_name": "Brady v. Maryland",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-05-13",
    "year": 1963,
    "docket": "490",
    "cluster_id": 106598,
    "lead_opinion_id": 106598,
    "sibling_ids": [
      106598,
      9422583,
      9422584
    ],
    "absolute_url": "/opinion/106598/brady-v-maryland/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "373 U.S. 83",
      "volume": "373",
      "reporter": "U.S.",
      "page": "83",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 1194",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "1194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 L. Ed. 2d 215",
        "volume": "10",
        "reporter": "L. Ed. 2d",
        "page": "215",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 1615",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1615",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "373 U.S. 83",
        "volume": "373",
        "reporter": "U.S.",
        "page": "83",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 1194",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "1194",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "10 L. Ed. 2d 215",
        "volume": "10",
        "reporter": "L. Ed. 2d",
        "page": "215",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 1615",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1615",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "373 U.S. 83",
    "official_selection": {
      "court_class": "scotus",
      "selected": "373 U.S. 83",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-87",
      "page": null,
      "quote": "--- # Brady v. Maryland *373 U.S. 83 (1963)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Brady and a companion, Boblit, were tried separately for a murder committed in the course of a robbery. Brady admitted participating but insisted Boblit did the actual killing. Before trial Brady's counsel asked to see Boblit's statements; the prosecution turned over several but withheld the one in which Boblit admitted the killing. Brady discovered the withheld confession only after he had been convicted and sentenced to death. ## Issue Whether the prosecution's suppression of evidence favorable to the accused, requested by the defense and material to guilt or punishment, violates due process. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-05-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brady v. Maryland",
    "varies_by_point": false,
    "scope_note": "Foundational disclosure rule; later refined (not undermined) by Giglio and United States v. Bagley.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Jevric",
          "cluster_id": 10873877,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Faretta v. California",
          "cluster_id": 109309,
          "cite": [
            "45 L. Ed. 2d 562",
            "95 S. Ct. 2525",
            "422 U.S. 806",
            "1975 U.S. LEXIS 83"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schlup v. Delo",
          "cluster_id": 117893,
          "cite": [
            "130 L. Ed. 2d 808",
            "115 S. Ct. 851",
            "513 U.S. 298",
            "1995 U.S. LEXIS 701",
            "1995 WL 20524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murray v. Carrier",
          "cluster_id": 111727,
          "cite": [
            "91 L. Ed. 2d 397",
            "106 S. Ct. 2639",
            "477 U.S. 478",
            "1986 U.S. LEXIS 66",
            "54 U.S.L.W. 4820"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'Sullivan v. Boerckel",
          "cluster_id": 118296,
          "cite": [
            "144 L. Ed. 2d 1",
            "119 S. Ct. 1728",
            "526 U.S. 838",
            "1999 U.S. LEXIS 4003"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pace v. DiGuglielmo",
          "cluster_id": 142891,
          "cite": [
            "161 L. Ed. 2d 669",
            "125 S. Ct. 1807",
            "544 U.S. 408",
            "2005 U.S. LEXIS 3705",
            "5 Cal. Daily Op. Serv. 3526",
            "73 U.S.L.W. 4304",
            "18 Fla. L. Weekly Fed. S 250"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martinez v. Ryan",
          "cluster_id": 625711,
          "cite": [
            "182 L. Ed. 2d 272",
            "132 S. Ct. 1309",
            "566 U.S. 1",
            "2012 U.S. LEXIS 2317"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Robbins",
          "cluster_id": 118332,
          "cite": [
            "145 L. Ed. 2d 756",
            "120 S. Ct. 746",
            "528 U.S. 259",
            "2000 U.S. LEXIS 825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
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
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. Collins",
          "cluster_id": 112808,
          "cite": [
            "122 L. Ed. 2d 203",
            "113 S. Ct. 853",
            "506 U.S. 390",
            "1993 U.S. LEXIS 1017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcetti v. Ceballos",
          "cluster_id": 145653,
          "cite": [
            "164 L. Ed. 2d 689",
            "126 S. Ct. 1951",
            "547 U.S. 410",
            "2006 U.S. LEXIS 4341"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caldwell v. Mississippi",
          "cluster_id": 111471,
          "cite": [
            "86 L. Ed. 2d 231",
            "105 S. Ct. 2633",
            "472 U.S. 320",
            "1985 U.S. LEXIS 96",
            "53 U.S.L.W. 4743"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brady v. Maryland:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106598 OR 9422583 OR 9422584) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzU0MjY1NjAwMDAwJnM9MTA3OTc2NzImdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106598+OR+9422583+OR+9422584%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106598 OR 9422583 OR 9422584)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjEyJnM9MjExNTk0NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28106598+OR+9422583+OR+9422584%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106598 OR 9422583 OR 9422584)",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNzYwNDAwMDAwMDAwJnM9MTA3MDY4MDQmdD1vJmQ9MjAyNi0wNy0wNiZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&filed_after=2023-07-06&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106598+OR+9422583+OR+9422584%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 1,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 1,
        "triage_snippet_classified": 199
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106598 OR 9422583 OR 9422584)",
    "indexed_citing_opinions": 19246,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106598,
        "count": 17003,
        "count_source": "search"
      },
      {
        "opinion_id": 9422583,
        "count": 2633,
        "count_source": "search"
      },
      {
        "opinion_id": 9422584,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 33964,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brady-v-maryland.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yLjQ2NzM5OTEmcz0yNDU4MzMzJnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106598+OR+9422583+OR+9422584%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106598,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 102863,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103332,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103727,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 103798,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104681,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 104695,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 105403,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 105566,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 106054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 106521,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 1932282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2204133,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2324852,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2333601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 2336815,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3482675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3486546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3486645,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3487541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106598,
        "cited_id": 3488520,
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
    "date_created": "2026-07-04T20:17:56Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:18:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:18:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:22:58Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:18:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brady v. Maryland

```
<div>
<center><b><span class="citation" data-id="9422583"><a href="/opinion/106598/brady-v-maryland/" aria-description="Citation for case: Brady v. Maryland">373 U.S. 83</a></span> (1963)</b></center>
<center><h1>BRADY<br>
v.<br>
MARYLAND.</h1></center>
<center>No. 490.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 18-19, 1963.</center>
<center>Decided May 13, 1963.</center>
CERTIORARI TO THE COURT OF APPEALS OF MARYLAND.
<p><span class="star-pagination">*84</span> <i>E. Clinton Bamberger, Jr.</i> argued the cause for petitioner. With him on the brief was <i>John Martin Jones, Jr.</i></p>
<p><i>Thomas W. Jamison III,</i> Special Assistant Attorney General of Maryland, argued the cause for respondent. With him on the brief were <i>Thomas B. Finan,</i> Attorney General, and <i>Robert C. Murphy,</i> Deputy Attorney General.</p>
<p>Opinion of the Court by MR. JUSTICE DOUGLAS, announced by MR. JUSTICE BRENNAN.</p>
<p>Petitioner and a companion, Boblit, were found guilty of murder in the first degree and were sentenced to death, their convictions being affirmed by the Court of Appeals of Maryland. <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">220 Md. 454</a></span>, <span class="citation" data-id="1505680"><a href="/opinion/1505680/boblit-v-state/" aria-description="Citation for case: Boblit v. State">154 A. 2d 434</a></span>. Their trials were separate, petitioner being tried first. At his trial Brady took the stand and admitted his participation in the crime, but he claimed that Boblit did the actual killing. And, in his summation to the jury, Brady's counsel conceded that Brady was guilty of murder in the first degree, asking only that the jury return that verdict "without capital punishment." Prior to the trial petitioner's counsel had requested the prosecution to allow him to examine Boblit's extrajudicial statements. Several of those statements were shown to him; but one dated July 9, 1958, in which Boblit admitted the actual homicide, was withheld by the prosecution and did not come to petitioner's notice until after he had been tried, convicted, and sentenced, and after his conviction had been affirmed.</p>
<p>Petitioner moved the trial court for a new trial based on the newly discovered evidence that had been suppressed by the prosecution. Petitioner's appeal from a denial of that motion was dismissed by the Court of Appeals without prejudice to relief under the Maryland <span class="star-pagination">*85</span> Post Conviction Procedure Act. <span class="citation" data-id="2324852"><a href="/opinion/2324852/brady-v-state/" aria-description="Citation for case: Brady v. State">222 Md. 442</a></span>, <span class="citation" data-id="2324852"><a href="/opinion/2324852/brady-v-state/" aria-description="Citation for case: Brady v. State">160 A. 2d 912</a></span>. The petition for post-conviction relief was dismissed by the trial court; and on appeal the Court of Appeals held that suppression of the evidence by the prosecution denied petitioner due process of law and remanded the case for a retrial of the question of punishment, not the question of guilt. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/" aria-description="Citation for case: Brady v. State">226 Md. 422</a></span>, 174 A 2d 167. The case is here on certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./371/812/">371 U. S. 812</a></span>.<sup>[1]</sup></p>
<p>The crime in question was murder committed in the perpetration of a robbery. Punishment for that crime in Maryland is life imprisonment or death, the jury being empowered to restrict the punishment to life by addition of the words "without capital punishment." 3 Md. Ann. Code, 1957, Art. 27, § 413. In Maryland, by reason of the state constitution, the jury in a criminal case are "the Judges of Law, as well as of fact." Art. XV, § 5. The question presented is whether petitioner was denied a federal right when the Court of Appeals restricted the new trial to the question of punishment.</p>
<p><span class="star-pagination">*86</span> We agree with the Court of Appeals that suppression of this confession was a violation of the Due Process Clause of the Fourteenth Amendment. The Court of Appeals relied in the main on two decisions from the Third Circuit Court of Appeals<i>United States ex rel. Almeida</i> v. <i>Baldi,</i> <span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">195 F. 2d 815</a></span>, and <i>United States ex rel. Thompson</i> v. <i>Dye,</i> 221 F. 2d 763which, we agree, state the correct constitutional rule.</p>
<p>This ruling is an extension of <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span>, where the Court ruled on what nondisclosure by a prosecutor violates due process:</p>
<blockquote>"It is a requirement that cannot be deemed to be satisfied by mere notice and hearing if a State has contrived a conviction through the pretense of a trial which in truth is but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury by the presentation of testimony known to be perjured. Such a contrivance by a State to procure the conviction and imprisonment of a defendant is as inconsistent with the rudimentary demands of justice as is the obtaining of a like result by intimidation."</blockquote>
<p>In <i>Pyle</i> v. <i>Kansas,</i> <span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/#215" aria-description="Citation for case: Pyle v. Kansas">317 U. S. 213, 215-216</a></span>, we phrased the rule in broader terms:</p>
<blockquote>"Petitioner's papers are inexpertly drawn, but they do set forth allegations that his imprisonment resulted from perjured testimony, knowingly used by the State authorities to obtain his conviction, and from the deliberate suppression by those same authorities of evidence favorable to him. These allegations sufficiently charge a deprivation of rights guaranteed by the Federal Constitution, and, if proven, would entitle petitioner to release from his present custody. <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>."</blockquote>
<p><span class="star-pagination">*87</span> The Third Circuit in the <i><span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">Baldi</a></span></i> case construed that statement in <i>Pyle</i> v. <i><span class="citation" data-id="103727"><a href="/opinion/103727/pyle-v-kansas/" aria-description="Citation for case: Pyle v. Kansas">Kansas</a></span></i> to mean that the "suppression of evidence favorable" to the accused was itself sufficient to amount to a denial of due process. <span class="citation" data-id="229184"><a href="/opinion/229184/united-states-ex-rel-almeida-v-baldi/#820" aria-description="Citation for case: United States Ex Rel. Almeida v. Baldi">195 F. 2d, at 820</a></span>. In <i>Napue</i> v. <i>Illinois,</i> <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U. S. 264, 269</a></span>, we extended the test formulated in <i>Mooney</i> v. <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan</a></span></i> when we said: "The same result obtains when the State, although not soliciting false evidence, allows it to go uncorrected when it appears." And see <i>Alcorta</i> v. <i>Texas,</i> <span class="citation" data-id="105566"><a href="/opinion/105566/alcorta-v-texas/" aria-description="Citation for case: Alcorta v. Texas">355 U. S. 28</a></span>; <i>Wilde</i> v. <i>Wyoming,</i> <span class="citation" data-id="106054"><a href="/opinion/106054/wilde-v-wyoming/" aria-description="Citation for case: Wilde v. Wyoming">362 U. S. 607</a></span>. Cf. <i>Durley</i> v. <i>Mayo,</i> <span class="citation" data-id="9421301"><a href="/opinion/105403/durley-v-mayo/#285" aria-description="Citation for case: Durley v. Mayo">351 U. S. 277, 285</a></span> (dissenting opinion).</p>
<p>We now hold that the suppression by the prosecution of evidence favorable to an accused upon request violates due process where the evidence is material either to guilt or to punishment, irrespective of the good faith or bad faith of the prosecution.</p>
<p>The principle of <i>Mooney</i> v. <i><span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan</a></span></i> is not punishment of society for misdeeds of a prosecutor but avoidance of an unfair trial to the accused. Society wins not only when the guilty are convicted but when criminal trials are fair; our system of the administration of justice suffers when any accused is treated unfairly. An inscription on the walls of the Department of Justice states the proposition candidly for the federal domain: "The United States wins its point whenever justice is done its citizens in the courts."<sup>[2]</sup> A prosecution that withholds evidence on demand of an accused which, if made available, <span class="star-pagination">*88</span> would tend to exculpate him or reduce the penalty helps shape a trial that bears heavily on the defendant. That casts the prosecutor in the role of an architect of a proceeding that does not comport with standards of justice, even though, as in the present case, his action is not "the result of guile," to use the words of the Court of Appeals. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#427" aria-description="Citation for case: Brady v. State">226 Md., at 427</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#169" aria-description="Citation for case: Brady v. State">174 A. 2d, at 169</a></span>.</p>
<p>The question remains whether petitioner was denied a constitutional right when the Court of Appeals restricted his new trial to the question of punishment. In justification of that ruling the Court of Appeals stated:</p>
<blockquote>"There is considerable doubt as to how much good Boblit's undisclosed confession would have done Brady if it had been before the jury. It clearly implicated Brady as being the one who wanted to strangle the victim, Brooks. Boblit, according to this statement, also favored killing him, but he wanted to do it by shooting. We cannot put ourselves in the place of the jury and assume what their views would have been as to whether it did or did not matter whether it was Brady's hands or Boblit's hands that twisted the shirt about the victim's neck. . . . [I]t would be `too dogmatic' for us to say that the jury would not have attached any significance to this evidence <i>in considering the punishment of the defendant Brady.</i>
</blockquote>
<blockquote>"Not without some doubt, we conclude that the withholding of this particular confession of Boblit's was prejudicial to the defendant Brady. . . .</blockquote>
<blockquote>"The appellant's sole claim of prejudice goes to the punishment imposed. <i>If Boblit's withheld confession had been before the jury, nothing in it could have reduced the appellant Brady's offense below murder in the first degree.</i> We, therefore, see no occasion to retry that issue." <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#429" aria-description="Citation for case: Brady v. State">226 Md., at 429-430</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#171" aria-description="Citation for case: Brady v. State">174 A. 2d, at 171</a></span>. (Italics added.)</blockquote>
<p><span class="star-pagination">*89</span> If this were a jurisdiction where the jury was not the judge of the law, a different question would be presented. But since it is, how can the Maryland Court of Appeals state that nothing in the suppressed confession could have reduced petitioner's offense "below murder in the first degree"? If, as a matter of Maryland law, juries in criminal cases could determine the admissibility of such evidence on the issue of innocence or guilt, the question would seem to be foreclosed.</p>
<p>But Maryland's constitutional provision making the jury in criminal cases "the Judges of Law" does not mean precisely what it seems to say.<sup>[3]</sup> The present status of that provision was reviewed recently in <i>Giles</i> v. <i>State,</i> <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/" aria-description="Citation for case: Giles v. State">229 Md. 370</a></span>, <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/" aria-description="Citation for case: Giles v. State">183 A. 2d 359</a></span>, appeal dismissed, <span class="citation multiple-matches"><a href="/c/U.%20S./372/767/">372 U. S. 767</a></span>, where the several exceptions, added by statute or carved out by judicial construction, are reviewed. One of those exceptions, material here, is that "Trial courts have always passed and still pass upon the admissibility of evidence the jury may consider on the issue of the innocence or guilt of the accused." <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/#383" aria-description="Citation for case: Giles v. State">229 Md., at 383</a></span>, <span class="citation" data-id="2336815"><a href="/opinion/2336815/giles-v-state/#365" aria-description="Citation for case: Giles v. State">183 A. 2d, at 365</a></span>. The cases cited make up a long line going back nearly a century. <i>Wheeler</i> v. <i>State,</i> <span class="citation" data-id="7894155"><a href="/opinion/7943451/wheeler-v-state/#570" aria-description="Citation for case: Wheeler v. State">42 Md. 563, 570</a></span>, stated that instructions to the jury were advisory only, "except in regard to questions as to what shall be considered as evidence." And the court "having such right, it follows of course, that it also has the right to prevent counsel from arguing against such an instruction." <i>Bell</i> v. <i>State,</i> <span class="citation" data-id="7895894"><a href="/opinion/7945112/bell-v-state/#120" aria-description="Citation for case: Bell v. State">57 Md. 108, 120</a></span>. And see <i>Beard</i> v. <i>State,</i> <span class="citation" data-id="7897944"><a href="/opinion/7947021/beard-v-state/#280" aria-description="Citation for case: Beard v. State">71 Md. 275, 280</a></span>, <span class="citation" data-id="7897944"><a href="/opinion/7947021/beard-v-state/#1045" aria-description="Citation for case: Beard v. State">17 A. 1044, 1045</a></span>; <i>Dick</i> v. <i>State,</i> <span class="citation" data-id="3488520"><a href="/opinion/3490537/dick-v-state/#21" aria-description="Citation for case: Dick v. State">107 Md. 11, 21</a></span>, <span class="citation" data-id="3488520"><a href="/opinion/3490537/dick-v-state/#290" aria-description="Citation for case: Dick v. State">68 A. 286, 290</a></span>. Cf. <i>Vogel</i> v. <i>State,</i> <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/" aria-description="Citation for case: Vogel v. State">163 Md. 267</a></span>, <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/" aria-description="Citation for case: Vogel v. State">162 A. 705</a></span>.</p>
<p><span class="star-pagination">*90</span> We usually walk on treacherous ground when we explore state law,<sup>[4]</sup> for state courts, state agencies, and state legislatures are its final expositors under our federal regime. But, as we read the Maryland decisions, it is the court, not the jury, that passes on the "admissibility of evidence" pertinent to "the issue of the innocence or guilt of the accused." <i>Giles</i> v. <i>State, supra</i><i>.</i> In the present case a unanimous Court of Appeals has said that nothing in the suppressed confession "could have reduced the appellant Brady's offense below murder in the first degree." We read that statement as a ruling on the admissibility of the confession on the issue of innocence or guilt. A sporting theory of justice might assume that if the suppressed confession had been used at the first trial, the judge's ruling that it was not admissible on the issue of innocence or guilt might have been flouted by the jury just as might have been done if the court had first admitted a confession and then stricken it from the record.<sup>[5]</sup> But we cannot raise that trial strategy to the dignity of a constitutional right and say that the deprival of this defendant of that sporting chance through the use of a <span class="star-pagination">*91</span> bifurcated trial (cf. <i>Williams</i> v. <i>New York,</i> <span class="citation" data-id="9420330"><a href="/opinion/104681/williams-v-new-york/" aria-description="Citation for case: Williams v. New York">337 U. S. 241</a></span>) denies him due process or violates the Equal Protection Clause of the Fourteenth Amendment.</p>
<p><i>Affirmed.</i></p>
<p>Separate opinion of MR. JUSTICE WHITE.</p>
<p>1. The Maryland Court of Appeals declared, "The suppression or withholding by the State of material evidence exculpatory to an accused is a violation of due process" without citing the United States Constitution or the Maryland Constitution which also has a due process clause.<sup>[*]</sup> We therefore cannot be sure which Constitution was invoked by the court below and thus whether the State, the only party aggrieved by this portion of the judgment, could even bring the issue here if it desired to do so. See <i>New York City</i> v. <i>Central Savings Bank,</i> <span class="citation" data-id="8154343"><a href="/opinion/8192409/new-york-city-v-central-savings-bank/" aria-description="Citation for case: New York City v. Central Savings Bank">306 U. S. 661</a></span>; <i>Minnesota</i> v. <i>National Tea Co.,</i> <span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/" aria-description="Citation for case: Minnesota v. National Tea Co.">309 U. S. 551</a></span>. But in any event, there is no cross-petition by the State, nor has it challenged the correctness of the ruling below that a new trial on punishment was called for by the requirements of due process. In my view, therefore, the Court should not reach the due process question which it decides. It certainly is not the case, as it may be suggested, that without it we would have only a state law question, for assuming the court below was correct in finding a violation of petitioner's rights in the suppression of evidence, the federal question he wants decided here still remains, namely, whether denying him a new trial on guilt as well as punishment deprives him of equal protection. There is thus a federal question to deal with in this Court, cf. <i>Bell</i> v. <i>Hood,</i> <span class="citation" data-id="9419809"><a href="/opinion/104272/bell-v-hood/" aria-description="Citation for case: Bell v. Hood">327 U. S. 678</a></span>, <span class="star-pagination">*92</span> wholly aside from the due process question involving the suppression of evidence. The majority opinion makes this unmistakably clear. Before dealing with the due process issue it says, "The question presented is whether petitioner was denied a federal right when the Court of Appeals restricted the new trial to the question of punishment." After discussing at some length and disposing of the suppression matter in federal constitutional terms it says the question still to be decided is the same as it was before: "The question remains whether petitioner was denied a constitutional right when the Court of Appeals restricted his new trial to the question of punishment."</p>
<p>The result, of course, is that the due process discussion by the Court is wholly advisory.</p>
<p>2. In any event the Court's due process advice goes substantially beyond the holding below. I would employ more confining language and would not cast in constitutional form a broad rule of criminal discovery. Instead, I would leave this task, at least for now, to the rulemaking or legislative process after full consideration by legislators, bench, and bar.</p>
<p>3. I concur in the Court's disposition of petitioner's equal protection argument.</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE BLACK joins, dissenting.</p>
<p>I think this case presents only a single federal question: did the order of the Maryland Court of Appeals granting a new trial, limited to the issue of punishment, violate petitioner's Fourteenth Amendment right to equal protection?<sup>[1]</sup> In my opinion an affirmative answer would <span class="star-pagination">*93</span> be required <i>if</i> the Boblit statement would have been admissible on the issue of guilt at petitioner's original trial. This indeed seems to be the clear implication of this Court's opinion.</p>
<p>The Court, however, holds that the Fourteenth Amendment was not infringed because it considers the Court of Appeals' opinion, and the other Maryland cases dealing with Maryland's constitutional provision making juries in criminal cases "the Judges of Law, as well as of fact," as establishing that the Boblit statement would not have been admissible at the original trial on the issue of petitioner's guilt.</p>
<p>But I cannot read the Court of Appeals' opinion with any such assurance. That opinion can as easily, and perhaps more easily, be read as indicating that the new trial limitation followed from the Court of Appeals' concept of its power, under § 645G of the Maryland Post Conviction Procedure Act, Md. Code, Art. 27 (1960 Cum. Supp.) and Rule 870 of the Maryland Rules of Procedure, to fashion appropriate relief meeting the peculiar circumstances of this case,<sup>[2]</sup> rather than from the view that the Boblit statement would have been relevant at the original trial only on the issue of punishment. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#430" aria-description="Citation for case: Brady v. State">226 Md., at 430</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#171" aria-description="Citation for case: Brady v. State">174 A. 2d, at 171</a></span>. This interpretation is indeed fortified by the Court of Appeals' earlier general discussion as to the admissibility of third-party confessions, which falls short of saying anything that is dispositive <span class="star-pagination">*94</span> of the crucial issue here. <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#427" aria-description="Citation for case: Brady v. State">226 Md., at 427-429</a></span>, <span class="citation" data-id="2204133"><a href="/opinion/2204133/brady-v-state/#170" aria-description="Citation for case: Brady v. State">174 A. 2d, at 170</a></span>.<sup>[3]</sup></p>
<p>Nor do I find anything in any of the other Maryland cases cited by the Court (<i>ante,</i> p. 89) which bears on the admissibility <i>vel non</i> of the Boblit statement on the issue of guilt. None of these cases suggests anything more relevant here than that a jury may not "overrule" the trial court on questions relating to the admissibility of evidence. Indeed they are by no means clear as to what happens if the jury in fact undertakes to do so. In this very case, for example, the trial court charged that "in the final analysis the jury are the judges of both the <i>law</i> and the facts, and the verdict in this case is <i>entirely</i> the jury's responsibility." (Emphasis added.)</p>
<p>Moreover, uncertainty on this score is compounded by the State's acknowledgment at the oral argument here that the withheld Boblit statement <i>would</i> have been admissible at the trial on the issue of guilt.<sup>[4]</sup></p>
<p>In this state of uncertainty as to the proper answer to the critical underlying issue of state law, and in view of the fact that the Court of Appeals did not in terms <span class="star-pagination">*95</span> address itself to the equal protection question, I do not see how we can properly resolve this case at this juncture. I think the appropriate course is to vacate the judgment of the State Court of Appeals and remand the case to that court for further consideration in light of the governing constitutional principle stated at the outset of this opinion. Cf. <i>Minnesota</i> v. <i>National Tea Co.,</i> <span class="citation" data-id="9419097"><a href="/opinion/103332/minnesota-v-national-tea-co/" aria-description="Citation for case: Minnesota v. National Tea Co.">309 U. S. 551</a></span>.</p>
<h2>NOTES</h2>
<p>[1]  Neither party suggests that the decision below is not a "final judgment" within the meaning of <span class="citation no-link">28 U. S. C. § 1257</span> (3), and no attack on the reviewability of the lower court's judgment could be successfully maintained. For the general rule that "Final judgment in a criminal case means sentence. The sentence is the judgment" (<i>Berman</i> v. <i>United States,</i> <span class="citation" data-id="102863"><a href="/opinion/102863/berman-v-united-states/#212" aria-description="Citation for case: Berman v. United States">302 U. S. 211, 212</a></span>) cannot be applied here. If in fact the Fourteenth Amendment entitles petitioner to a new trial on the issue of guilt as well as punishment the ruling below has seriously prejudiced him. It is the right to a trial on the issue of guilt "that presents a serious and unsettled question" (<i>Cohen</i> v. <i>Beneficial Loan Corp.,</i> <span class="citation" data-id="9420349"><a href="/opinion/104695/cohen-v-beneficial-industrial-loan-corp/#547" aria-description="Citation for case: Cohen v. Beneficial Industrial Loan Corp.">337 U. S. 541, 547</a></span>) that "is fundamental to the further conduct of the case" (<i>United States</i> v. <i>General Motors Corp.,</i> <span class="citation" data-id="9419563"><a href="/opinion/104054/united-states-v-general-motors-corp/#377" aria-description="Citation for case: United States v. General Motors Corp.">323 U. S. 373, 377</a></span>). This question is "independent of, and unaffected by" (<i>Radio Station WOW</i> v. <i>Johnson,</i> <span class="citation" data-id="9419695"><a href="/opinion/104183/radio-station-wow-inc-v-johnson/#126" aria-description="Citation for case: Radio Station Wow, Inc. v. Johnson">326 U. S. 120, 126</a></span>) what may transpire in a trial at which petitioner can receive only a life imprisonment or death sentence. It cannot be mooted by such a proceeding. See <i>Largent</i> v. <i>Texas,</i> <span class="citation" data-id="103798"><a href="/opinion/103798/largent-v-texas/#421" aria-description="Citation for case: Largent v. Texas">318 U. S. 418, 421-422</a></span>. Cf. <i>Local No. 438</i> v. <i>Curry,</i> <span class="citation" data-id="9422517"><a href="/opinion/106521/local-no-438-construction-general-laborers-union-v-curry/#549" aria-description="Citation for case: Local No. 438 Construction &amp; General Laborers&#x27; Union v....">371 U. S. 542, 549</a></span>.</p>
<p>[2]  Judge Simon E. Sobeloff when Solicitor General put the idea as follows in an address before the Judicial Conference of the Fourth Circuit on June 29, 1954:
</p>
<p>"The Solicitor General is not a neutral, he is an advocate; but an advocate for a client whose business is not merely to prevail in the instant case. My client's chief business is not to achieve victory but to establish justice. We are constantly reminded of the now classic words penned by one of my illustrious predecessors, Frederick William Lehmann, that the Government wins its point when justice is done in its courts."</p>
<p>[3]  See Dennis, Maryland's Antique Constitutional Thorn, 92 U. of Pa. L. Rev. 34, 39, 43; Prescott, Juries as Judges of the Law: Should the Practice be Continued, 60 Md. St. Bar Assn. Rept. 246, 253-254.</p>
<p>[4]  For one unhappy incident of recent vintage see <i>Oklahoma Packing Co.</i> v. <i>Oklahoma Gas &amp; Electric Co.,</i> <span class="citation" data-id="9419072"><a href="/opinion/103282/oklahoma-packing-co-v-oklahoma-gas-electric-co/" aria-description="Citation for case: Oklahoma Packing Co. v. Oklahoma Gas &amp; Electric Co.">309 U. S. 4</a></span>, that replaced an earlier opinion in the same case, <span class="citation no-link">309 U. S. 703</span>.</p>
<p>[5]  "In the matter of confessions a hybrid situation exists. It is the duty of the Court to determine from the proof, usually taken out of the presence of the jury, if they were freely and voluntarily made, etc., and admissible. If admitted, the jury is entitled to hear and consider proof of the circumstances surrounding their obtention, the better to determine their weight and sufficiency. The fact that the Court admits them clothes them with no presumption for the jury's purposes that they are either true or were freely and voluntarily made. However, after a confession has been admitted and read to the jury the judge may change his mind and strike it out of the record. Does he strike it out of the jury's mind?" Dennis, Maryland's Antique Constitutional Thorn, 92 U. of Pa. L. Rev. 34, 39. See also <i>Bell</i> v. <i>State, supra,</i> at 120; <i>Vogel</i> v. <i>State,</i> <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/#272" aria-description="Citation for case: Vogel v. State">163 Md., at 272</a></span>, <span class="citation" data-id="3486645"><a href="/opinion/3488709/vogel-v-state/#706" aria-description="Citation for case: Vogel v. State">162 A., at 706-707</a></span>.</p>
<p>[*]  Md. Const., Art. 23; <i>Home Utilities Co., Inc.,</i> v. <i>Revere Copper &amp; Brass, Inc.,</i> <span class="citation" data-id="2333601"><a href="/opinion/2333601/home-utilities-co-v-revere-copper-brass-inc/" aria-description="Citation for case: Home Utilities Co. v. Revere Copper &amp; Brass, Inc.">209 Md. 610</a></span>, <span class="citation" data-id="2333601"><a href="/opinion/2333601/home-utilities-co-v-revere-copper-brass-inc/" aria-description="Citation for case: Home Utilities Co. v. Revere Copper &amp; Brass, Inc.">122 A. 2d 109</a></span>; <i>Raymond</i> v. <i>State,</i> <span class="citation" data-id="3486546"><a href="/opinion/3488611/raymond-v-state-ex-rel-szydlouski/" aria-description="Citation for case: Raymond v. State Ex Rel. Szydlouski">192 Md. 602</a></span>, <span class="citation" data-id="3486546"><a href="/opinion/3488611/raymond-v-state-ex-rel-szydlouski/" aria-description="Citation for case: Raymond v. State Ex Rel. Szydlouski">65 A. 2d 285</a></span>; <i>County Comm'rs of Anne Arundel County</i> v. <i>English,</i> <span class="citation" data-id="3487541"><a href="/opinion/3489580/county-commissioners-v-english/" aria-description="Citation for case: County Commissioners v. English">182 Md. 514</a></span>, <span class="citation" data-id="3487541"><a href="/opinion/3489580/county-commissioners-v-english/" aria-description="Citation for case: County Commissioners v. English">35 A. 2d 135</a></span>; <i>Oursler</i> v. <i>Tawes,</i> <span class="citation" data-id="3482675"><a href="/opinion/3484836/oursler-v-tawes/" aria-description="Citation for case: Oursler v. Tawes">178 Md. 471</a></span>, <span class="citation" data-id="3482675"><a href="/opinion/3484836/oursler-v-tawes/" aria-description="Citation for case: Oursler v. Tawes">13 A. 2d 763</a></span>.</p>
<p>[1]  I agree with my Brother WHITE that there is no necessity for deciding in this case the broad due process questions with which the Court deals at pp. 86-88 of its opinion.</p>
<p>[2]  Section 645G provides in part: "If the court finds in favor of the petitioner, it shall enter an appropriate order with respect to the judgment or sentence in the former proceedings, and any supplementary orders as to rearraignment, retrial, custody, bail, discharge, correction of sentence, or other matters that may be necessary and proper." Rule 870 provides that the Court of Appeals "will either affirm or reverse the judgment from which the appeal was taken, or direct the manner in which it shall be modified, changed or amended."</p>
<p>[3]  It is noteworthy that the Court of Appeals did not indicate that it was limiting in any way the authority of <i>Day</i> v. <i>State,</i> <span class="citation" data-id="1932282"><a href="/opinion/1932282/day-v-state/" aria-description="Citation for case: Day v. State">196 Md. 384</a></span>, <span class="citation" data-id="1932282"><a href="/opinion/1932282/day-v-state/" aria-description="Citation for case: Day v. State">76 A. 2d 729</a></span>. In that case two defendants were jointly tried and convicted of felony murder. Each admitted participating in the felony but accused the other of the homicide. On appeal the defendants attacked the trial court's denial of a severance, and the State argued that neither defendant was harmed by the statements put in evidence at the joint trial because admission of the felony amounted to admission of guilt of felony murder. Nevertheless the Court of Appeals found an abuse of discretion and ordered separate new trials on all issues.</p>
<p>[4]  In response to a question from the Bench as to whether Boblit's statement, had it been offered at petitioner's original trial, would have been admissible for all purposes, counsel for the State, after some colloquy, stated: "It would have been, yes."</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Brendlin v. California.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Brendlin v. California"
type: case
citation: "551 U.S. 249 (2007)"
parallel_cite: "127 S. Ct. 2400; 168 L. Ed. 2d 132"
neutral_cite: 2007 U.S. LEXIS 7897
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2007
date_decided: 2007-06-18
docket: 06-8120
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2007-06-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brendlin v. California
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145712/brendlin-v-california/"
  cluster_id: 145712
  opinion_id: 145712
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rakas v. Illinois]]", "[[Delaware v. Prouse]]", "[[California v. Hodari D.]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "traffic-stop", "seizure", "passenger"]
holding: "When a vehicle is stopped, a passenger is seized just as the driver is, and so may challenge the constitutionality of the stop."
lake:
  record_id: Brendlin v. California
  status: verified
  projected_at: 2026-07-09
---

# Brendlin v. California

*551 U.S. 249 (2007)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A deputy stopped a car to verify a temporary operating permit, admitting there was nothing unusual about the permit and no reason to believe a violation. Bruce Brendlin was the front-seat passenger. The deputy recognized him, confirmed a parole-violation warrant, arrested him, and a search turned up methamphetamine-manufacturing materials. Brendlin moved to suppress, arguing the stop unlawfully seized him.

## Issue
Whether a passenger in a vehicle is "seized" by a traffic stop, so that he has [[Standing to Challenge a Search|standing to challenge]] the constitutionality of the stop.

## Rule
"When a police officer makes a traffic stop, the driver of the car is seized within the meaning of the Fourth Amendment." — 551 U.S. at 251. ^pin-251

"We hold that a passenger is seized as well and so may challenge the constitutionality of the stop." — [*Id.*](https://www.courtlistener.com/opinion/145712/brendlin-v-california/#:~:text=We%20hold%20that%20a%20passenger) ^pin-251b

## Application
When the deputy pulled the car over, a reasonable person in Brendlin's position as a passenger would not have believed he was free to leave; he was therefore seized at the moment the car stopped. Because the State conceded the stop itself lacked justification, Brendlin could challenge it and seek suppression of what the seizure produced.

## Conclusion
A passenger is seized by a traffic stop and may challenge it; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Brendlin* applies the seizure framework of [[California v. Hodari D.]] and [[Rakas v. Illinois]] to confirm passenger standing in vehicle stops.

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny / Refinement*

## Sources
- *Brendlin v. California*, 551 U.S. 249 (2007) — https://www.courtlistener.com/opinion/145712/brendlin-v-california/ — pinpoint: 251.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "45886aab36721de7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brendlin v. California"}, "payload": {"all": [{"cite": "551 U.S. 249", "page": "249", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "551"}, {"cite": "127 S. Ct. 2400", "page": "2400", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "127"}, {"cite": "168 L. Ed. 2d 132", "page": "132", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "168"}, {"cite": "2007 U.S. LEXIS 7897", "page": "7897", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2007"}], "display": "551 U.S. 249", "official": {"cite": "551 U.S. 249", "page": "249", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "551"}, "official_selection_present": true, "record_id": "Brendlin v. California"}}
{"assertion_id": "ab8526d1b1781ed6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-251", "record_id": "Brendlin v. California"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-251", "pinpoint_status": "slip-only", "quote": "by a traffic stop, so that he has standing to challenge the constitutionality of the stop. ## Rule", "quote_fidelity": "mismatch", "record_id": "Brendlin v. California", "star_marker": null}}
{"assertion_id": "ba9ac86d05d983b9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-251b", "record_id": "Brendlin v. California"}, "payload": {"fragment": "#:~:text=We%20hold%20that%20a%20passenger", "page": null, "pin_id": "pin-251b", "pinpoint_status": "slip-only", "quote": "We hold that a passenger is seized as well and so may challenge the constitutionality of the stop.", "quote_fidelity": "matched", "record_id": "Brendlin v. California", "star_marker": null}}
{"assertion_id": "deb681f8ca1a45b9", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brendlin v. California"}, "payload": {"as_of_content": "2007-06-18", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brendlin v. California", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "varies_by_point": false}}
```

### lake record — Brendlin v. California

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brendlin v. California",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brendlin v. California",
    "case_name_short": "Brendlin",
    "case_name_full": "Brendlin v. California",
    "input_case_name": "Brendlin v. California",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2007-06-18",
    "year": 2007,
    "docket": "06-8120",
    "cluster_id": 145712,
    "lead_opinion_id": 145712,
    "sibling_ids": [
      145712
    ],
    "absolute_url": "/opinion/145712/brendlin-v-california/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "551 U.S. 249",
      "volume": "551",
      "reporter": "U.S.",
      "page": "249",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "127 S. Ct. 2400",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "2400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "168 L. Ed. 2d 132",
        "volume": "168",
        "reporter": "L. Ed. 2d",
        "page": "132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2007 U.S. LEXIS 7897",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "7897",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "551 U.S. 249",
        "volume": "551",
        "reporter": "U.S.",
        "page": "249",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "127 S. Ct. 2400",
        "volume": "127",
        "reporter": "S. Ct.",
        "page": "2400",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "168 L. Ed. 2d 132",
        "volume": "168",
        "reporter": "L. Ed. 2d",
        "page": "132",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2007 U.S. LEXIS 7897",
        "volume": "2007",
        "reporter": "U.S. LEXIS",
        "page": "7897",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "551 U.S. 249",
    "official_selection": {
      "court_class": "scotus",
      "selected": "551 U.S. 249",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-251",
      "page": null,
      "quote": "by a traffic stop, so that he has standing to challenge the constitutionality of the stop. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-251b",
      "page": null,
      "quote": "We hold that a passenger is seized as well and so may challenge the constitutionality of the stop.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 7394,
      "fragment": "#:~:text=We%20hold%20that%20a%20passenger",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2007-06-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brendlin v. California",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Matta",
          "cluster_id": 4671437,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zachariah J. Marshall v. State of Indiana",
          "cluster_id": 4594526,
          "cite": [
            "117 N.E.3d 1254"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Buckley",
          "cluster_id": 4468007,
          "cite": [
            "90 N.E.3d 767",
            "478 Mass. 861"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Arizona v. Johnson",
          "cluster_id": 145912,
          "cite": [
            "172 L. Ed. 2d 694",
            "129 S. Ct. 781",
            "555 U.S. 323",
            "2009 U.S. LEXIS 868"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Zamudio",
          "cluster_id": 2634388,
          "cite": [
            "181 P.3d 105",
            "75 Cal. Rptr. 3d 289",
            "43 Cal. 4th 327",
            "2008 Cal. LEXIS 4431"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel v. City of Joliet",
          "cluster_id": 4376986,
          "cite": [
            "580 U.S. 357",
            "137 S. Ct. 911",
            "197 L. Ed. 2d 312",
            "2017 U.S. LEXIS 2021",
            "26 Fla. L. Weekly Fed. S 476",
            "85 U.S.L.W. 4130"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heien v. North Carolina",
          "cluster_id": 2760668,
          "cite": [
            "190 L. Ed. 2d 475",
            "135 S. Ct. 530",
            "2014 U.S. LEXIS 8306",
            "83 U.S.L.W. 4021",
            "25 Fla. L. Weekly Fed. S 20"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cindy Abbott v. Sangamon County",
          "cluster_id": 816250,
          "cite": [
            "705 F.3d 706",
            "2013 WL 322920",
            "2013 U.S. App. LEXIS 1963"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Letner and Tobin",
          "cluster_id": 2630926,
          "cite": [
            "235 P.3d 62",
            "50 Cal. 4th 99",
            "112 Cal. Rptr. 3d 746",
            "2010 Cal. LEXIS 7290"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Torres v. Madrid",
          "cluster_id": 4867542,
          "cite": [
            "592 U.S. 306",
            "141 S. Ct. 989",
            "209 L. Ed. 2d 190"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mark Atkinson v. City of Mountain View",
          "cluster_id": 819982,
          "cite": [
            "709 F.3d 1201",
            "2013 WL 462381",
            "2013 U.S. App. LEXIS 2703"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Woodard",
          "cluster_id": 2540788,
          "cite": [
            "341 S.W.3d 404",
            "2011 Tex. Crim. App. LEXIS 447",
            "2011 WL 1261320"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gonzalez Ex Rel. Gonzalez v. City of Anaheim",
          "cluster_id": 2658912,
          "cite": [
            "747 F.3d 789",
            "2014 WL 1274551",
            "2014 U.S. App. LEXIS 5895"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Henderson",
          "cluster_id": 1057155,
          "cite": [
            "2013 IL 114040"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Harmon",
          "cluster_id": 4670342,
          "cite": [
            "2019 COA 156"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maurice Lewis v. City of Chicago",
          "cluster_id": 4583974,
          "cite": [
            "914 F.3d 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wade, Christopher James",
          "cluster_id": 2947716,
          "cite": [
            "422 S.W.3d 661",
            "2013 WL 4820299",
            "2013 Tex. Crim. App. LEXIS 1314"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brooks v. Gaenzle",
          "cluster_id": 152652,
          "cite": [
            "614 F.3d 1213",
            "2010 U.S. App. LEXIS 16488",
            "2010 WL 3122800"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
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
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shaun J. Matz v. Rodney Klotka",
          "cluster_id": 2739950,
          "cite": [
            "769 F.3d 517",
            "2014 U.S. App. LEXIS 19074",
            "2014 WL 4960311"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Castleberry",
          "cluster_id": 2282066,
          "cite": [
            "332 S.W.3d 460",
            "2011 Tex. Crim. App. LEXIS 283",
            "2011 WL 709697"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Morris v. Noe",
          "cluster_id": 623700,
          "cite": [
            "672 F.3d 1185",
            "2012 WL 604170",
            "2012 U.S. App. LEXIS 3927"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Charles Waters v. B. Madson",
          "cluster_id": 4609057,
          "cite": [
            "921 F.3d 725"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cosby",
          "cluster_id": 2105166,
          "cite": [
            "898 N.E.2d 603",
            "231 Ill. 2d 262",
            "325 Ill. Dec. 556",
            "2008 Ill. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Thompson",
          "cluster_id": 2623710,
          "cite": [
            "166 P.3d 1015",
            "284 Kan. 763",
            "2007 Kan. LEXIS 487"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Johnson",
          "cluster_id": 2012814,
          "cite": [
            "927 N.E.2d 1179",
            "237 Ill. 2d 81",
            "340 Ill. Dec. 168",
            "2010 Ill. LEXIS 657"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Campbell",
          "cluster_id": 1353842,
          "cite": [
            "549 F.3d 364",
            "2008 U.S. App. LEXIS 24313",
            "2008 WL 5060374"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brendlin v. California:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145712) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTAwOTQwODAwMDAwJnM9NDQxMTk3NiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145712%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(145712)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDImcz0yNDc5NTE5JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145712%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145712)",
        "reviewed": 69,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 69,
        "triage_read": 0,
        "triage_snippet_classified": 69
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145712)",
    "indexed_citing_opinions": 780,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145712,
        "count": 780,
        "count_source": "search"
      }
    ],
    "citation_count": 1525,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brendlin-v-california.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMzUyMzYmcz0xMDMwMzI4MiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145712%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145712,
        "cited_id": 32811,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 108845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 109953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110351,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 111294,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112579,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 121153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 195379,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 558629,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 584528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 708240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 769930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 781879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 793575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 794964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 1254533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 1314003,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 1344951,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2150438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2177108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2226476,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2388757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2460636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2575734,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2581401,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145712,
        "cited_id": 2639027,
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
    "date_created": "2026-07-04T20:22:58Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:23:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:23:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:26:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:23:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brendlin v. California

```
(Slip Opinion)              OCTOBER TERM, 2006                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                     BRENDLIN v. CALIFORNIA

      CERTIORARI TO THE SUPREME COURT OF CALIFORNIA

      No. 06–8120. Argued April 23, 2007—Decided June 18, 2007
After officers stopped a car to check its registration without reason to
  believe it was being operated unlawfully, one of them recognized peti
  tioner Brendlin, a passenger in the car. Upon verifying that Brendlin
  was a parole violator, the officers formally arrested him and searched
  him, the driver, and the car, finding, among other things, metham
  phetamine paraphernalia. Charged with possession and manufac
  ture of that substance, Brendlin moved to suppress the evidence ob
  tained in searching his person and the car, arguing that the officers
  lacked probable cause or reasonable suspicion to make the traffic
  stop, which was an unconstitutional seizure of his person. The trial
  court denied the motion, but the California Court of Appeal reversed,
  holding that Brendlin was seized by the traffic stop, which was
  unlawful. Reversing, the State Supreme Court held that suppression
  was unwarranted because a passenger is not seized as a constitu
  tional matter absent additional circumstances that would indicate to
  a reasonable person that he was the subject of the officer’s investiga
  tion or show of authority.
Held: When police make a traffic stop, a passenger in the car, like the
 driver, is seized for Fourth Amendment purposes and so may chal
 lenge the stop’s constitutionality. Pp. 4–13.
    (a) A person is seized and thus entitled to challenge the govern
 ment’s action when officers, by physical force or a show of authority,
 terminate or restrain the person’s freedom of movement through
 means intentionally applied. Florida v. Bostick, 501 U. S. 429, 434;
 Brower v. County of Inyo, 489 U. S. 593, 597. There is no seizure
 without that person’s actual submission. See, e.g., California v. Ho
 dari D., 499 U. S. 621, 626, n. 2. When police actions do not show an
 unambiguous intent to restrain or when an individual’s submission
 takes the form of passive acquiescence, the test for telling when a
2                      BRENDLIN v. CALIFORNIA

                                  Syllabus

    seizure occurs is whether, in light of all the surrounding circum
    stances, a reasonable person would have believed he was not free to
    leave. E.g., United States v. Mendenhall, 446 U. S. 544, 554 (princi
    pal opinion). But when a person “has no desire to leave” for reasons
    unrelated to the police presence, the “coercive effect of the encounter”
    can be measured better by asking whether “a reasonable person
    would feel free to decline the officers’ requests or otherwise terminate
    the encounter.” Bostick, supra, at 435–436. Pp. 4–6.
       (b) Brendlin was seized because no reasonable person in his posi
    tion when the car was stopped would have believed himself free to
    “terminate the encounter” between the police and himself. Bostick,
    supra, at 436. Any reasonable passenger would have understood the
    officers to be exercising control to the point that no one in the car was
    free to depart without police permission. A traffic stop necessarily
    curtails a passenger’s travel just as much as it halts the driver, di
    verting both from the stream of traffic to the side of the road, and the
    police activity that normally amounts to intrusion on “privacy and
    personal security” does not normally (and did not here) distinguish
    between passenger and driver. United States v. Martinez-Fuerte, 428
    U. S. 543, 554. An officer who orders a particular car to pull over acts
    with an implicit claim of right based on fault of some sort, and a sen
    sible person would not expect the officer to allow people to come and
    go freely from the physical focal point of an investigation into faulty
    behavior or wrongdoing. If the likely wrongdoing is not the driving,
    the passenger will reasonably feel subject to suspicion owing to close
    association; but even when the wrongdoing is only bad driving, the
    passenger will expect to be subject to some scrutiny, and his attempt
    to leave would be so obviously likely to prompt an objection from the
    officer that no passenger would feel free to leave in the first place. It
    is also reasonable for passengers to expect that an officer at the scene
    of a crime, arrest, or investigation will not let people move around in
    ways that could jeopardize his safety. See, e.g., Maryland v. Wilson,
    519 U. S. 408, 414–415. The Court’s conclusion comports with the
    views of all nine Federal Courts of Appeals, and nearly every state
    court, to have ruled on the question. Pp. 6–9.
       (c) The State Supreme Court’s contrary conclusion reflects three
    premises with which this Court respectfully disagrees. First, the
    view that the police only intended to investigate the car’s driver and
    did not direct a show of authority toward Brendlin impermissibly
    shifts the issue from the intent of the police as objectively manifested
    to the motive of the police for taking the intentional action to stop the
    car. Applying the objective Mendenhall test resolves any ambiguity
    by showing that a reasonable passenger would understand that he
    was subject to the police display of authority. Second, the state
                    Cite as: 551 U. S. ____ (2007)                   3

                               Syllabus

  court’s assumption that Brendlin, as the passenger, had no ability to
  submit to the police show of authority because only the driver was in
  control of the moving car is unavailing. Brendlin had no effective
  way to signal submission while the car was moving, but once it came
  to a stop he could, and apparently did, submit by staying inside.
  Third, there is no basis for the state court’s fear that adopting the
  rule this Court applies would encompass even those motorists whose
  movement has been impeded due to the traffic stop of another car.
  An occupant of a car who knows he is stuck in traffic because another
  car has been pulled over by police would not perceive the show of au
  thority as directed at him or his car. Pp. 9–13.
    (d) The state courts are left to consider in the first instance
  whether suppression turns on any other issue. P. 13.
38 Cal. 4th 1107, 136 P. 3d 845, vacated and remanded.

  SOUTER, J., delivered the opinion for a unanimous Court.
                        Cite as: 551 U. S. ____ (2007)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 06–8120
                                   _________________


    BRUCE EDWARD BRENDLIN, PETITIONER v.

               CALIFORNIA 

    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                      CALIFORNIA

                                 [June 18, 2007] 


   JUSTICE SOUTER delivered the opinion of the Court.
   When a police officer makes a traffic stop, the driver of
the car is seized within the meaning of the Fourth
Amendment. The question in this case is whether the
same is true of a passenger. We hold that a passenger is
seized as well and so may challenge the constitutionality
of the stop.
                              I
  Early in the morning of November 27, 2001, Deputy
Sheriff Robert Brokenbrough and his partner saw a
parked Buick with expired registration tags. In his ensu
ing conversation with the police dispatcher, Brokenbrough
learned that an application for renewal of registration was
being processed. The officers saw the car again on the
road, and this time Brokenbrough noticed its display of a
temporary operating permit with the number “11,” indicat
ing it was legal to drive the car through November. App.
115. The officers decided to pull the Buick over to verify
that the permit matched the vehicle, even though, as
Brokenbrough admitted later, there was nothing unusual
about the permit or the way it was affixed. Brokenbrough
2                    BRENDLIN v. CALIFORNIA

                          Opinion of the Court

asked the driver, Karen Simeroth, for her license and saw
a passenger in the front seat, petitioner Bruce Brendlin,
whom he recognized as “one of the Brendlin brothers.” Id.,
at 65. He recalled that either Scott or Bruce Brendlin had
dropped out of parole supervision and asked Brendlin to
identify himself.1 Brokenbrough returned to his cruiser,
called for backup, and verified that Brendlin was a parole
violator with an outstanding no-bail warrant for his ar
rest. While he was in the patrol car, Brokenbrough saw
Brendlin briefly open and then close the passenger door of
the Buick. Once reinforcements arrived, Brokenbrough
went to the passenger side of the Buick, ordered him out of
the car at gunpoint, and declared him under arrest. When
the police searched Brendlin incident to arrest, they found
an orange syringe cap on his person. A patdown search of
Simeroth revealed syringes and a plastic bag of a green
leafy substance, and she was also formally arrested.
Officers then searched the car and found tubing, a scale,
and other things used to produce methamphetamine.
  Brendlin was charged with possession and manufacture
of methamphetamine, and he moved to suppress the evi
dence obtained in the searches of his person and the car as
fruits of an unconstitutional seizure, arguing that the
officers lacked probable cause or reasonable suspicion to
make the traffic stop. He did not assert that his Fourth
Amendment rights were violated by the search of Si
meroth’s vehicle, cf. Rakas v. Illinois, 439 U. S. 128 (1978),
but claimed only that the traffic stop was an unlawful
seizure of his person. The trial court denied the suppres
sion motion after finding that the stop was lawful and
Brendlin was not seized until Brokenbrough ordered him
out of the car and formally arrested him. Brendlin
——————
  1 The parties dispute the accuracy of the transcript of the suppression

hearing and disagree as to whether Brendlin gave his name or the false
name “Bruce Brown.” App. 115.
                      Cite as: 551 U. S. ____ (2007)                       3

                           Opinion of the Court

pleaded guilty, subject to appeal on the suppression issue,
and was sentenced to four years in prison.
   The California Court of Appeal reversed the denial of
the suppression motion, holding that Brendlin was seized
by the traffic stop, which they held unlawful. 8 Cal. Rptr.
3d 882 (2004) (officially depublished). By a narrow major
ity, the Supreme Court of California reversed. The State
Supreme Court noted California’s concession that the
officers had no reasonable basis to suspect unlawful opera
tion of the car, 38 Cal. 4th 1107, 1114, 136 P. 3d 845, 848
(2006),2 but still held suppression unwarranted because a
passenger “is not seized as a constitutional matter in the
absence of additional circumstances that would indicate to
a reasonable person that he or she was the subject of the
peace officer’s investigation or show of authority,” id., at
1111, 136 P. 3d, at 846. The court reasoned that Brendlin
was not seized by the traffic stop because Simeroth was its
exclusive target, id., at 1118, 136 P. 3d, at 851, that a
passenger cannot submit to an officer’s show of authority
while the driver controls the car, id., at 1118–1119, 135
P. 3d, at 851–852, and that once a car has been pulled off
the road, a passenger “would feel free to depart or other
wise to conduct his or her affairs as though the police were
not present,” id., at 1119, 136 P. 3d, at 852. In dissent,
Justice Corrigan said that a traffic stop entails the seizure
of a passenger even when the driver is the sole target of
police investigation because a passenger is detained for
the purpose of ensuring an officer’s safety and would not
feel free to leave the car without the officer’s permission.
Id., at 1125, 136 P. 3d, at 856.
   We granted certiorari to decide whether a traffic stop
——————
  2 California conceded that the police officers lacked reasonable suspi

cion to justify the traffic stop because a “ ‘vehicle with an application for
renewal of expired registration would be expected to have a temporary
operating permit.’ ” 38 Cal. 4th, at 1114, 136 P. 3d, at 848 (quoting
Brief for Respondent California in No. S123133 (Sup. Ct. Cal.), p. 24).
4                BRENDLIN v. CALIFORNIA

                     Opinion of the Court

subjects a passenger, as well as the driver, to Fourth
Amendment seizure, 549 U. S. __ (2007). We now vacate.
                              II 

                              A

   A person is seized by the police and thus entitled to
challenge the government’s action under the Fourth
Amendment when the officer, “ ‘by means of physical force
or show of authority,’ ” terminates or restrains his freedom
of movement, Florida v. Bostick, 501 U. S. 429, 434 (1991)
(quoting Terry v. Ohio, 392 U. S. 1, 19, n. 16 (1968)),
“through means intentionally applied,” Brower v. County
of Inyo, 489 U. S. 593, 597 (1989) (emphasis in original).
Thus, an “unintended person . . . [may be] the object of the
detention,” so long as the detention is “willful” and not
merely the consequence of “an unknowing act.” Id., at
596; cf. County of Sacramento v. Lewis, 523 U. S. 833, 844
(1998) (no seizure where a police officer accidentally
struck and killed a motorcycle passenger during a high-
speed pursuit). A police officer may make a seizure by a
show of authority and without the use of physical force,
but there is no seizure without actual submission; other
wise, there is at most an attempted seizure, so far as the
Fourth Amendment is concerned. See California v. Ho
dari D., 499 U. S. 621, 626, n. 2 (1991); Lewis, supra, at
844, 845, n. 7.
   When the actions of the police do not show an unambi
guous intent to restrain or when an individual’s submis
sion to a show of governmental authority takes the form of
passive acquiescence, there needs to be some test for
telling when a seizure occurs in response to authority, and
when it does not. The test was devised by Justice Stewart
in United States v. Mendenhall, 446 U. S. 544 (1980), who
wrote that a seizure occurs if “in view of all of the circum
stances surrounding the incident, a reasonable person
would have believed that he was not free to leave,” id., at
                 Cite as: 551 U. S. ____ (2007)            5

                     Opinion of the Court

554 (principal opinion). Later on, the Court adopted Jus
tice Stewart’s touchstone, see, e.g., Hodari D., supra, at
627; Michigan v. Chesternut, 486 U. S. 567, 573 (1988);
INS v. Delgado, 466 U. S. 210, 215 (1984), but added that
when a person “has no desire to leave” for reasons unre
lated to the police presence, the “coercive effect of the
encounter” can be measured better by asking whether “a
reasonable person would feel free to decline the officers’
requests or otherwise terminate the encounter,” Bostick,
supra, at 435–436; see also United States v. Drayton, 536
U. S. 194, 202 (2002).
   The law is settled that in Fourth Amendment terms a
traffic stop entails a seizure of the driver “even though the
purpose of the stop is limited and the resulting detention
quite brief.” Delaware v. Prouse, 440 U. S. 648, 653
(1979); see also Whren v. United States, 517 U. S. 806,
809–810 (1996). And although we have not, until today,
squarely answered the question whether a passenger is
also seized, we have said over and over in dicta that dur
ing a traffic stop an officer seizes everyone in the vehicle,
not just the driver. See, e.g., Prouse, supra, at 653
(“[S]topping an automobile and detaining its occupants
constitute a ‘seizure’ within the meaning of [the Fourth
and Fourteenth] Amendments”); Colorado v. Bannister,
449 U. S. 1, 4, n. 3 (1980) (per curiam) (“There can be no
question that the stopping of a vehicle and the detention of
its occupants constitute a ‘seizure’ within the meaning of
the Fourth Amendment”); Berkemer v. McCarty, 468 U. S.
420, 436–437 (1984) (“[W]e have long acknowledged that
stopping an automobile and detaining its occupants consti
tute a seizure” (internal quotation marks omitted)); United
States v. Hensley, 469 U. S. 221, 226 (1985) (“[S]topping a
car and detaining its occupants constitute a seizure”);
Whren, supra, at 809–810 (“Temporary detention of indi
viduals during the stop of an automobile by the police,
even if only for a brief period and for a limited purpose,
6                BRENDLIN v. CALIFORNIA

                     Opinion of the Court

constitutes a ‘seizure’ of ‘persons’ within the meaning of
[the Fourth Amendment]”).
  We have come closest to the question here in two cases
dealing with unlawful seizure of a passenger, and neither
time did we indicate any distinction between driver and
passenger that would affect the Fourth Amendment
analysis. Delaware v. Prouse considered grounds for
stopping a car on the road and held that Prouse’s suppres
sion motion was properly granted. We spoke of the arrest
ing officer’s testimony that Prouse was in the back seat
when the car was pulled over, see 440 U. S., at 650, n. 1,
described Prouse as an occupant, not as the driver, and
referred to the car’s “occupants” as being seized, id., at
653. Justification for stopping a car was the issue again in
Whren v. United States, where we passed upon a Fourth
Amendment challenge by two petitioners who moved to
suppress drug evidence found during the course of a traffic
stop. See 517 U. S., at 809. Both driver and passenger
claimed to have been seized illegally when the police
stopped the car; we agreed and held suppression unwar
ranted only because the stop rested on probable cause.
Id., at 809–810, 819.
                              B
  The State concedes that the police had no adequate
justification to pull the car over, see n. 2, supra, but ar
gues that the passenger was not seized and thus cannot
claim that the evidence was tainted by an unconstitutional
stop. We resolve this question by asking whether a rea
sonable person in Brendlin’s position when the car stopped
would have believed himself free to “terminate the en
counter” between the police and himself. Bostick, supra,
at 436. We think that in these circumstances any reason
able passenger would have understood the police officers
to be exercising control to the point that no one in the car
was free to depart without police permission.
                      Cite as: 551 U. S. ____ (2007)                     7

                          Opinion of the Court

   A traffic stop necessarily curtails the travel a passenger
has chosen just as much as it halts the driver, diverting
both from the stream of traffic to the side of the road, and
the police activity that normally amounts to intrusion on
“privacy and personal security” does not normally (and did
not here) distinguish between passenger and driver.
United States v. Martinez-Fuerte, 428 U. S. 543, 554
(1976). An officer who orders one particular car to pull
over acts with an implicit claim of right based on fault of
some sort, and a sensible person would not expect a police
officer to allow people to come and go freely from the
physical focal point of an investigation into faulty behavior
or wrongdoing. If the likely wrongdoing is not the driving,
the passenger will reasonably feel subject to suspicion
owing to close association; but even when the wrongdoing
is only bad driving, the passenger will expect to be subject
to some scrutiny, and his attempt to leave the scene would
be so obviously likely to prompt an objection from the
officer that no passenger would feel free to leave in the
first place. Cf. Drayton, supra, at 197–199, 203–204 (find
ing no seizure when police officers boarded a stationary
bus and asked passengers for permission to search for
drugs).3
   It is also reasonable for passengers to expect that a
police officer at the scene of a crime, arrest, or investiga
tion will not let people move around in ways that could
jeopardize his safety. In Maryland v. Wilson, 519 U. S.
408 (1997), we held that during a lawful traffic stop an
officer may order a passenger out of the car as a precau
——————
   3 Of course, police may also stop a car solely to investigate a passen

ger’s conduct. See, e.g., United States v. Rodriguez-Diaz, 161 F. Supp.
2d 627, 629, n. 1 (Md. 2001) (passenger’s violation of local seatbelt law);
People v. Roth, 85 P. 3d 571, 573 (Colo. App. 2003) (passenger’s viola
tion of littering ordinance). Accordingly, a passenger cannot assume,
merely from the fact of a traffic stop, that the driver’s conduct is the
cause of the stop.
8                    BRENDLIN v. CALIFORNIA

                         Opinion of the Court

tionary measure, without reasonable suspicion that the
passenger poses a safety risk. Id., at 414–415; cf. Pennsyl
vania v. Mimms, 434 U. S. 106 (1977) (per curiam) (driver
may be ordered out of the car as a matter of course). In
fashioning this rule, we invoked our earlier statement that
“ ‘[t]he risk of harm to both the police and the occupants is
minimized if the officers routinely exercise unquestioned
command of the situation.’ ” Wilson, supra, at 414 (quot
ing Michigan v. Summers, 452 U. S. 692, 702–703 (1981)).
What we have said in these opinions probably reflects a
societal expectation of “ ‘unquestioned [police] command’ ”
at odds with any notion that a passenger would feel free to
leave, or to terminate the personal encounter any other
way, without advance permission. Wilson, supra, at 414.4
    Our conclusion comports with the views of all nine
Federal Courts of Appeals, and nearly every state court, to
have ruled on the question. See United States v. Kimball,
25 F. 3d 1, 5 (CA1 1994); United States v. Mosley, 454
F. 3d 249, 253 (CA3 2006); United States v. Rusher, 966
F. 2d 868, 874, n. 4 (CA4 1992); United States v. Grant,
349 F. 3d 192, 196 (CA5 2003); United States v. Perez, 440
F. 3d 363, 369 (CA6 2006); United States v. Powell, 929
F. 2d 1190, 1195 (CA7 1991); United States v. Ameling,
328 F. 3d 443, 446–447, n. 3 (CA8 2003); United States v.
Twilley, 222 F. 3d 1092, 1095 (CA9 2000); United States v.
Eylicio-Montoya, 70 F. 3d 1158, 1163–1164 (CA10 1995);
State v. Bowers, 334 Ark. 447, 451–452, 976 S. W. 2d 379,
381–382 (1998); State v. Haworth, 106 Idaho 405, 405–
406, 679 P. 2d 1123, 1123–1124 (1984); People v. Bunch,
——————
   4 Although the State Supreme Court inferred from Brendlin’s decision

to open and close the passenger door during the traffic stop that he was
“awar[e] of the available options,” 38 Cal. 4th 1107, 1120, 136 P. 3d
845, 852 (2006), this conduct could equally be taken to indicate that
Brendlin felt compelled to remain inside the car. In any event, the test
is not what Brendlin felt but what a reasonable passenger would have
understood.
                    Cite as: 551 U. S. ____ (2007)                  9

                        Opinion of the Court

207 Ill. 2d 7, 13, 796 N. E. 2d 1024, 1029 (2003); State v.
Eis, 348 N. W. 2d 224, 226 (Iowa 1984); State v. Hodges,
252 Kan. 989, 1002–1005, 851 P. 2d 352, 361–362 (1993);
State v. Carter, 69 Ohio St. 3d 57, 63, 630 N. E. 2d 355,
360 (1994) (per curiam); State v. Harris, 206 Wis. 2d 243,
253–258, 557 N. W. 2d 245, 249–251 (1996). And the
treatise writers share this prevailing judicial view that a
passenger may bring a Fourth Amendment challenge to
the legality of a traffic stop. See, e.g., 6 W. LaFave, Search
and Seizure §11.3(e), pp. 194, 195, and n. 277 (4th ed.
2004 and Supp. 2007) (“If either the stopping of the car,
the length of the passenger’s detention thereafter, or the
passenger’s removal from it are unreasonable in a Fourth
Amendment sense, then surely the passenger has stand
ing to object to those constitutional violations and to have
suppressed any evidence found in the car which is their
fruit” (footnote omitted)); 1 W. Ringel, Searches & Sei
zures, Arrests and Confessions §11:20, p. 11–98 (2d ed.
2007) (“[A] law enforcement officer’s stop of an automobile
results in a seizure of both the driver and the passenger”).5
                             C
   The contrary conclusion drawn by the Supreme Court of
California, that seizure came only with formal arrest,
reflects three premises as to which we respectfully dis
agree. First, the State Supreme Court reasoned that
Brendlin was not seized by the stop because Deputy Sher
iff Brokenbrough only intended to investigate Simeroth
and did not direct a show of authority toward Brendlin.
The court saw Brokenbrough’s “flashing lights [as] di
rected at the driver,” and pointed to the lack of record
evidence that Brokenbrough “was even aware [Brendlin]
——————
  5 Only two State Supreme Courts, other than California’s, have stood
against this tide of authority. See People v. Jackson, 39 P. 3d 1174,
1184–1186 (Colo. 2002) (en banc); State v. Mendez, 137 Wash. 2d 208,
222–223, 970 P. 2d 722, 729 (1999) (en banc).
10                BRENDLIN v. CALIFORNIA

                     Opinion of the Court

was in the car prior to the vehicle stop.” 38 Cal. 4th, at
1118, 136 P. 3d, at 851. But that view of the facts ignores
the objective Mendenhall test of what a reasonable pas
senger would understand. To the extent that there is
anything ambiguous in the show of force (was it fairly seen
as directed only at the driver or at the car and its occu
pants?), the test resolves the ambiguity, and here it leads
to the intuitive conclusion that all the occupants were
subject to like control by the successful display of author
ity. The State Supreme Court’s approach, on the contrary,
shifts the issue from the intent of the police as objectively
manifested to the motive of the police for taking the inten
tional action to stop the car, and we have repeatedly re
jected attempts to introduce this kind of subjectivity into
Fourth Amendment analysis. See, e.g., Whren, 517 U. S.,
at 813 (“Subjective intentions play no role in ordinary,
probable-cause Fourth Amendment analysis”); Chesternut,
486 U. S., at 575, n. 7 (“[T]he subjective intent of the
officers is relevant to an assessment of the Fourth
Amendment implications of police conduct only to the
extent that that intent has been conveyed to the person
confronted”); Mendenhall, 446 U. S., at 554, n. 6 (principal
opinion) (disregarding a Government agent’s subjective
intent to detain Mendenhall); cf. Rakas, 439 U. S., at 132–
135 (rejecting the “target theory” of Fourth Amendment
standing, which would have allowed “any criminal defen
dant at whom a search was directed” to challenge the
legality of the search (internal quotation marks omitted)).
   California defends the State Supreme Court’s ruling on
this point by citing our cases holding that seizure requires
a purposeful, deliberate act of detention. See Brief for
Respondent 9–14. But Chesternut, supra, answers that
argument. The intent that counts under the Fourth
Amendment is the “intent [that] has been conveyed to the
person confronted,” id., at 575, n. 7, and the criterion of
willful restriction on freedom of movement is no invitation
                 Cite as: 551 U. S. ____ (2007)          11

                     Opinion of the Court

to look to subjective intent when determining who is
seized. Our most recent cases are in accord on this point.
In Lewis, 523 U. S. 833, we considered whether a seizure
occurred when an officer accidentally ran over a passenger
who had fallen off a motorcycle during a high-speed chase,
and in holding that no seizure took place, we stressed that
the officer stopped Lewis’s movement by accidentally
crashing into him, not “through means intentionally ap
plied.” Id., at 844 (emphasis deleted). We did not even
consider, let alone emphasize, the possibility that the
officer had meant to detain the driver only and not the
passenger. Nor is Brower, 489 U. S. 593, to the contrary,
where it was dispositive that “Brower was meant to be
stopped by the physical obstacle of the roadblock—and
that he was so stopped.” Id., at 599. California reads this
language to suggest that for a specific occupant of the car
to be seized he must be the motivating target of an offi
cer’s show of authority, see Brief for Respondent 12, as if
the thrust of our observation were that Brower, and not
someone else, was “meant to be stopped.” But our point
was not that Brower alone was the target but that officers
detained him “through means intentionally applied”; if the
car had had another occupant, it would have made sense
to hold that he too had been seized when the car collided
with the roadblock. Neither case, then, is at odds with our
holding that the issue is whether a reasonable passenger
would have perceived that the show of authority was at
least partly directed at him, and that he was thus not free
to ignore the police presence and go about his business.
  Second, the Supreme Court of California assumed that
Brendlin, “as the passenger, had no ability to submit to
the deputy’s show of authority” because only the driver
was in control of the moving vehicle. 38 Cal. 4th, at 1118,
1119, 136 P. 3d, at 852. But what may amount to submis
sion depends on what a person was doing before the show
of authority: a fleeing man is not seized until he is physi
12                   BRENDLIN v. CALIFORNIA

                          Opinion of the Court

cally overpowered, but one sitting in a chair may submit to
authority by not getting up to run away. Here, Brendlin
had no effective way to signal submission while the car
was still moving on the roadway, but once it came to a stop
he could, and apparently did, submit by staying inside.
   Third, the State Supreme Court shied away from the
rule we apply today for fear that it “would encompass even
those motorists following the vehicle subject to the traffic
stop who, by virtue of the original detention, are forced to
slow down and perhaps even come to a halt in order to
accommodate that vehicle’s submission to police author
ity.” Id., at 1120, 136 P. 3d, at 853. But an occupant of a
car who knows that he is stuck in traffic because another
car has been pulled over (like the motorist who can’t even
make out why the road is suddenly clogged) would not
perceive a show of authority as directed at him or his car.
Such incidental restrictions on freedom of movement
would not tend to affect an individual’s “sense of security
and privacy in traveling in an automobile.” Prouse, 440
U. S., at 662. Nor would the consequential blockage call
for a precautionary rule to avoid the kind of “arbitrary and
oppressive interference by [law] enforcement officials with
the privacy and personal security of individuals” that the
Fourth Amendment was intended to limit. Martinez-
Fuerte, 428 U. S., at 554.6
   Indeed, the consequence to worry about would not flow
from our conclusion, but from the rule that almost all
courts have rejected. Holding that the passenger in a
——————
   6 California claims that, under today’s rule, “all taxi cab and bus pas

sengers would be ‘seized’ under the Fourth Amendment when the cab
or bus driver is pulled over by the police for running a red light.” Brief
for Respondent 23. But the relationship between driver and passenger
is not the same in a common carrier as it is in a private vehicle, and the
expectations of police officers and passengers differ accordingly. In
those cases, as here, the crucial question would be whether a reason
able person in the passenger’s position would feel free to take steps to
terminate the encounter.
                    Cite as: 551 U. S. ____ (2007)                  13

                         Opinion of the Court

private car is not (without more) seized in a traffic stop
would invite police officers to stop cars with passengers
regardless of probable cause or reasonable suspicion of
anything illegal.7 The fact that evidence uncovered as a
result of an arbitrary traffic stop would still be admissible
against any passengers would be a powerful incentive to
run the kind of “roving patrols” that would still violate the
driver’s Fourth Amendment right. See, e.g., Almeida-
Sanchez v. United States, 413 U. S. 266, 273 (1973) (stop
and search by Border Patrol agents without a warrant or
probable cause violated the Fourth Amendment); Prouse,
supra, at 663 (police spot check of driver’s license and
registration without reasonable suspicion violated the
Fourth Amendment).
                        *    *     *
  Brendlin was seized from the moment Simeroth’s car
came to a halt on the side of the road, and it was error to
deny his suppression motion on the ground that seizure
occurred only at the formal arrest. It will be for the state
courts to consider in the first instance whether suppres
sion turns on any other issue. The judgment of the Su
preme Court of California is vacated, and the case is re
manded for further proceedings not inconsistent with this
opinion.
                                            It is so ordered.



——————
  7 Compare Delaware v. Prouse, 440 U. S. 648, 663 (1979) (requiring

“at least articulable and reasonable suspicion” to support random,
investigative traffic stops), and United States v. Brignoni-Ponce, 422
U. S. 873, 880–884 (1975) (same), with Whren v. United States, 517
U. S. 806, 810 (1996) (“[T]he decision to stop an automobile is reason
able where the police have probable cause to believe that a traffic
violation has occurred”), and Atwater v. Lago Vista, 532 U. S. 318, 354
(2001) (“If an officer has probable cause to believe that an individual
has committed even a very minor criminal offense in his presence, he
may, without violating the Fourth Amendment, arrest the offender”).

```

---

## GROUP: _overhaul2/lake/cases/Brewer v. Williams.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Brewer v. Williams"
type: case
citation: "430 U.S. 387 (1977)"
parallel_cite: "97 S. Ct. 1232; 51 L. Ed. 2d 424"
neutral_cite: 1977 U.S. LEXIS 64
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-05-16
docket: 74-1263
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-05-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brewer v. Williams
  varies_by_point: false
  scope_note: "Sixth Amendment holding intact; the sequel Nix v. Williams concerned the exclusionary remedy (inevitable discovery), not Brewer's right-to-counsel holding."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109624/brewer-v-williams/"
  cluster_id: 109624
  opinion_id: 109624
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Massiah v. United States]]", "[[Nix v. Williams]]", "[[Kirby v. Illinois]]"]
aliases: ["Brewer v. Williams (Williams I)"]
tags: ["case", "sixth-amendment", "right-to-counsel", "deliberate-elicitation", "interrogation"]
holding: "The detective's \"Christian burial speech\" was the functional equivalent of interrogation and deliberately elicited incriminating…"
lake:
  record_id: Brewer v. Williams
  status: verified
  projected_at: 2026-07-06
---

# Brewer v. Williams

*430 U.S. 387 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Williams, arraigned on an arrest warrant for the abduction of a child and represented by counsel in two cities, was being driven by detectives between them. Counsel had been assured Williams would not be questioned during the trip. Knowing Williams was deeply religious, a detective delivered the "Christian burial speech," suggesting the child deserved a Christian burial before snow hid the body. Williams then directed the officers to the body.

## Issue
Whether police violated the Sixth Amendment right to counsel by deliberately eliciting incriminating statements and disclosures from an arraigned, represented defendant, outside counsel's presence and without a valid waiver.

## Rule
The right had attached: "the right to counsel granted by the Sixth and Fourteenth Amendments means at least that a person is entitled to the help of a lawyer at or after the time that judicial proceedings have been initiated against him — 'whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.'" — 430 U.S. at 398. ^pin-398

And it was violated by deliberate elicitation: "There can be no serious doubt, either, that Detective Leaming deliberately and designedly set out to elicit information from Williams just as surely as — and perhaps more effectively than — if he had formally interrogated him." — *Id.* at 399. ^pin-399

## Application
Judicial proceedings had begun against Williams (a warrant, an arraignment, and commitment to jail), so the Sixth Amendment right had attached. The detective's "Christian burial speech" was a deliberate effort to draw out incriminating disclosures while Williams was isolated from his lawyers, and the State did not carry its burden of proving Williams knowingly and intelligently relinquished his right. The statements and the resulting evidence were obtained in violation of the right to counsel.

## Conclusion
The Sixth Amendment right to counsel was violated; the grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of the Sixth Amendment holding. [[Reading and Citing Cases#on-remand|On remand]] the same evidence was later held admissible under the inevitable-discovery exception in [[Nix v. Williams]] (Williams II) — a ruling about the *exclusionary remedy*, not about *Brewer*'s right-to-counsel rule.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *Brewer v. Williams*, 430 U.S. 387 (1977) — https://www.courtlistener.com/opinion/109624/brewer-v-williams/ — pinpoints: 398, 399.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e494bf740cea40fc", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brewer v. Williams"}, "payload": {"all": [{"cite": "430 U.S. 387", "page": "387", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "430"}, {"cite": "97 S. Ct. 1232", "page": "1232", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "51 L. Ed. 2d 424", "page": "424", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "51"}, {"cite": "1977 U.S. LEXIS 64", "page": "64", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "430 U.S. 387", "official": {"cite": "430 U.S. 387", "page": "387", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "430"}, "official_selection_present": true, "record_id": "Brewer v. Williams"}}
{"assertion_id": "4d4051735ee39605", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-398", "record_id": "Brewer v. Williams"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-398", "pinpoint_status": "slip-only", "quote": "suggesting the child deserved a Christian burial before snow hid the body. Williams then directed the officers to the body. ## Issue Whether police violated the Sixth Amendment right to counsel by deliberately eliciting incriminating statements and disclosures from an arraigned, represented defendant, outside counsel's presence and without a valid waiver. ## Rule The right had attached:", "quote_fidelity": "mismatch", "record_id": "Brewer v. Williams", "star_marker": null}}
{"assertion_id": "afd7efbdbf29e9ce", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-399", "record_id": "Brewer v. Williams"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-399", "pinpoint_status": "slip-only", "quote": "There can be no serious doubt, either, that Detective Leaming deliberately and designedly set out to elicit information from Williams just as surely as — and perhaps more effectively than — if he had formally interrogated him.", "quote_fidelity": "mismatch", "record_id": "Brewer v. Williams", "star_marker": null}}
{"assertion_id": "a376e68a26dfa09e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brewer v. Williams"}, "payload": {"as_of_content": "1977-05-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brewer v. Williams", "scope_note": "Sixth Amendment holding intact; the sequel Nix v. Williams concerned the exclusionary remedy (inevitable discovery), not Brewer's right-to-counsel holding.", "varies_by_point": false}}
```

### lake record — Brewer v. Williams

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brewer v. Williams",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brewer v. Williams",
    "case_name_short": "Brewer",
    "case_name_full": "Brewer, Warden v. Williams",
    "input_case_name": "Brewer v. Williams",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-05-16",
    "year": 1977,
    "docket": "74-1263",
    "cluster_id": 109624,
    "lead_opinion_id": 109624,
    "sibling_ids": [
      109624,
      9426723,
      9426724,
      9426725,
      9426726,
      9426727,
      9426728,
      9426729
    ],
    "absolute_url": "/opinion/109624/brewer-v-williams/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9013081,
        "score": 10,
        "case_name": "Brewer v. Williams"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "430 U.S. 387",
      "volume": "430",
      "reporter": "U.S.",
      "page": "387",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 1232",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "1232",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 L. Ed. 2d 424",
        "volume": "51",
        "reporter": "L. Ed. 2d",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 64",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "64",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "430 U.S. 387",
        "volume": "430",
        "reporter": "U.S.",
        "page": "387",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 1232",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "1232",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "51 L. Ed. 2d 424",
        "volume": "51",
        "reporter": "L. Ed. 2d",
        "page": "424",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 64",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "64",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "430 U.S. 387",
    "official_selection": {
      "court_class": "scotus",
      "selected": "430 U.S. 387",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-398",
      "page": null,
      "quote": "suggesting the child deserved a Christian burial before snow hid the body. Williams then directed the officers to the body. ## Issue Whether police violated the Sixth Amendment right to counsel by deliberately eliciting incriminating statements and disclosures from an arraigned, represented defendant, outside counsel's presence and without a valid waiver. ## Rule The right had attached:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-399",
      "page": null,
      "quote": "There can be no serious doubt, either, that Detective Leaming deliberately and designedly set out to elicit information from Williams just as surely as \u2014 and perhaps more effectively than \u2014 if he had formally interrogated him.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-05-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brewer v. Williams",
    "varies_by_point": false,
    "scope_note": "Sixth Amendment holding intact; the sequel Nix v. Williams concerned the exclusionary remedy (inevitable discovery), not Brewer's right-to-counsel holding.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Simpkins",
          "cluster_id": 10018645,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Simpkins",
          "cluster_id": 4731163,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Colon",
          "cluster_id": 4671866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Carter",
          "cluster_id": 7176175,
          "cite": [
            "110 N.E.3d 1219"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "John Turner v. United States",
          "cluster_id": 4480399,
          "cite": [
            "885 F.3d 949"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. Bergeron",
          "cluster_id": 3207734,
          "cite": [
            "824 F.3d 148",
            "2016 U.S. App. LEXIS 9732",
            "2016 WL 3031089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
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
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miller v. Deal",
          "cluster_id": 2735639,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Miller v. Deal",
          "cluster_id": 2687518,
          "cite": [
            "295 Ga. 504",
            "761 S.E.2d 274",
            "2014 WL 3396506",
            "2014 Ga. LEXIS 581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane1_negative"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Arizona",
          "cluster_id": 110475,
          "cite": [
            "68 L. Ed. 2d 378",
            "101 S. Ct. 1880",
            "451 U.S. 477",
            "1981 U.S. LEXIS 96"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rhode Island v. Innis",
          "cluster_id": 110254,
          "cite": [
            "64 L. Ed. 2d 297",
            "100 S. Ct. 1682",
            "446 U.S. 291",
            "1980 U.S. LEXIS 94"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cuyler v. Sullivan",
          "cluster_id": 110256,
          "cite": [
            "64 L. Ed. 2d 333",
            "100 S. Ct. 1708",
            "446 U.S. 335",
            "1980 U.S. LEXIS 96"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manson v. Brathwaite",
          "cluster_id": 109693,
          "cite": [
            "53 L. Ed. 2d 140",
            "97 S. Ct. 2243",
            "432 U.S. 98",
            "1977 U.S. LEXIS 116"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sumner v. Mata",
          "cluster_id": 110382,
          "cite": [
            "66 L. Ed. 2d 722",
            "101 S. Ct. 764",
            "449 U.S. 539",
            "1981 U.S. LEXIS 62",
            "49 U.S.L.W. 4133"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estelle v. Smith",
          "cluster_id": 110474,
          "cite": [
            "68 L. Ed. 2d 359",
            "101 S. Ct. 1866",
            "451 U.S. 454",
            "1981 U.S. LEXIS 95",
            "49 U.S.L.W. 4490"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson v. Keohane",
          "cluster_id": 117982,
          "cite": [
            "133 L. Ed. 2d 383",
            "116 S. Ct. 457",
            "516 U.S. 99",
            "1995 U.S. LEXIS 8315",
            "95 Cal. Daily Op. Serv. 8968"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wright v. West",
          "cluster_id": 112771,
          "cite": [
            "120 L. Ed. 2d 225",
            "112 S. Ct. 2482",
            "505 U.S. 277",
            "1992 U.S. LEXIS 3689"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Marin v. State",
          "cluster_id": 1471238,
          "cite": [
            "851 S.W.2d 275",
            "1993 Tex. Crim. App. LEXIS 57",
            "1993 WL 62078"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan v. Jackson",
          "cluster_id": 111622,
          "cite": [
            "89 L. Ed. 2d 631",
            "106 S. Ct. 1404",
            "475 U.S. 625",
            "1986 U.S. LEXIS 91",
            "54 U.S.L.W. 4334"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gannett Co. v. DePasquale",
          "cluster_id": 110140,
          "cite": [
            "61 L. Ed. 2d 608",
            "99 S. Ct. 2898",
            "443 U.S. 368",
            "1979 U.S. LEXIS 15",
            "5 Media L. Rep. (BNA) 1337"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
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
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kerry Heckman, on Behalf of Themselves and All Other Persons Similarly Situated v. Williamson County",
          "cluster_id": 895412,
          "cite": [
            "369 S.W.3d 137",
            "55 Tex. Sup. Ct. J. 803",
            "2012 WL 2052813",
            "2012 Tex. LEXIS 462"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gouveia",
          "cluster_id": 111193,
          "cite": [
            "81 L. Ed. 2d 146",
            "104 S. Ct. 2292",
            "467 U.S. 180",
            "1984 U.S. LEXIS 91",
            "52 U.S.L.W. 4659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Colorado v. Spring",
          "cluster_id": 111798,
          "cite": [
            "93 L. Ed. 2d 954",
            "107 S. Ct. 851",
            "479 U.S. 564",
            "1987 U.S. LEXIS 418",
            "55 U.S.L.W. 4162"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Henry",
          "cluster_id": 110300,
          "cite": [
            "65 L. Ed. 2d 115",
            "100 S. Ct. 2183",
            "447 U.S. 264",
            "1980 U.S. LEXIS 111"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brewer v. Williams:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109624 OR 9426723 OR 9426724 OR 9426725 OR 9426726 OR 9426727 OR 9426728 OR 9426729) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzA3NDA0ODAwMDAwJnM9ODg5Nzg4JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109624+OR+9426723+OR+9426724+OR+9426725+OR+9426726+OR+9426727+OR+9426728+OR+9426729%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 9,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(109624 OR 9426723 OR 9426724 OR 9426725 OR 9426726 OR 9426727 OR 9426728 OR 9426729)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00Mjkmcz0xNzMzMDQ1JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109624+OR+9426723+OR+9426724+OR+9426725+OR+9426726+OR+9426727+OR+9426728+OR+9426729%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109624 OR 9426723 OR 9426724 OR 9426725 OR 9426726 OR 9426727 OR 9426728 OR 9426729)",
        "reviewed": 35,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 35,
        "triage_read": 0,
        "triage_snippet_classified": 35
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109624 OR 9426723 OR 9426724 OR 9426725 OR 9426726 OR 9426727 OR 9426728 OR 9426729)",
    "indexed_citing_opinions": 1682,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109624,
        "count": 1519,
        "count_source": "search"
      },
      {
        "opinion_id": 9426723,
        "count": 222,
        "count_source": "search"
      },
      {
        "opinion_id": 9426724,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426725,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426726,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426727,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426728,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426729,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2627,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brewer-v-williams.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1Njc2JnM9OTQ1MDM0MyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109624+OR+9426723+OR+9426724+OR+9426725+OR+9426726+OR+9426727+OR+9426728+OR+9426729%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109624,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 103597,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106388,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 106883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 107874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108846,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109469,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 109573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 265534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 276175,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 279298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 280792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 281065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 282997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 286561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 293260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 293647,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 294040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 294723,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 300514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 303738,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 308692,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 319744,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 324438,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 324530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 325420,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 328787,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 332311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 333157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 339071,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 340098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 1669210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 2115457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 2510431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109624,
        "cited_id": 3580565,
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
    "date_created": "2026-07-04T20:26:28Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:26:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:26:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:31:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:26:43Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brewer v. Williams (truncated)

```
<div>
<center><b><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U.S. 387</a></span> (1977)</b></center>
<center><h1>BREWER, WARDEN<br>
v.<br>
WILLIAMS.</h1></center>
<center>No. 74-1263.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued October 4, 1976.</center>
<center>Decided March 23, 1977.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE EIGHTH CIRCUIT.
<p><span class="star-pagination">*388</span> <i>Richard C. Turner,</i> Attorney General of Iowa, and <i>Richard N. Winders,</i> Assistant Attorney General, argued the cause and filed briefs for petitioner.</p>
<p><span class="star-pagination">*389</span> <i>Robert Bartels</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./423/1044/">423 U. S. 1044</a></span>, argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p>MR. JUSTICE STEWART delivered the opinion of the Court.</p>
<p>An Iowa trial jury found the respondent, Robert Williams, guilty of murder. The judgment of conviction was affirmed in the Iowa Supreme Court by a closely divided vote. In a subsequent habeas corpus proceeding a Federal District <span class="star-pagination">*390</span> Court ruled that under the United States Constitution Williams is entitled to a new trial, and a divided Court of Appeals for the Eighth Circuit agreed. The question before us is whether the District Court and the Court of Appeals were wrong.</p>
<p></p>
<h2>I</h2>
<p>On the afternoon of December 24, 1968, a 10-year-old girl named Pamela Powers went with her family to the YMCA in Des Moines, Iowa, to watch a wrestling tournament in which her brother was participating. When she failed to return from a trip to the washroom, a search for her began. The search was unsuccessful.</p>
<p>Robert Williams, who had recently escaped from a mental hospital, was a resident of the YMCA. Soon after the girl's disappearance Williams was seen in the YMCA lobby carrying some clothing and a large bundle wrapped in a blanket. He obtained help from a 14-year-old boy in opening the street door of the YMCA and the door to his automobile parked outside. When Williams placed the bundle in the front seat of his car the boy "saw two legs in it and they were skinny and white." Before anyone could see what was in the bundle Williams drove away. His abandoned car was found the following day in Davenport, Iowa, roughly 160 miles east of Des Moines. A warrant was then issued in Des Moines for his arrest on a charge of abduction.</p>
<p>On the morning of December 26, a Des Moines lawyer named Henry McKnight went to the Des Moines police station and informed the officers present that he had just received a long-distance call from Williams, and that he had advised Williams to turn himself in to the Davenport police. Williams did surrender that morning to the police in Davenport, and they booked him on the charge specified in the arrest warrant and gave him the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>. The Davenport police then telephoned <span class="star-pagination">*391</span> their counterparts in Des Moines to inform them that Williams had surrendered. McKnight, the lawyer, was still at the Des Moines police headquarters, and Williams conversed with McKnight on the telephone. In the presence of the Des Moines chief of police and a police detective named Leaming, McKnight advised Williams that Des Moines police officers would be driving to Davenport to pick him up, that the officers would not interrogate him or mistreat him, and that Williams was not to talk to the officers about Pamela Powers until after consulting with McKnight upon his return to Des Moines. As a result of these conversations, it was agreed between McKnight and the Des Moines police officials that Detective Leaming and a fellow officer would drive to Davenport to pick up Williams, that they would bring him directly back to Des Moines, and that they would not question him during the trip.</p>
<p>In the meantime Williams was arraigned before a judge in Davenport on the outstanding arrest warrant. The judge advised him of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights and committed him to jail. Before leaving the courtroom, Williams conferred with a lawyer named Kelly, who advised him not to make any statements until consulting with McKnight back in Des Moines.</p>
<p>Detective Leaming and his fellow officer arrived in Davenport about noon to pick up Williams and return him to Des Moines. Soon after their arrival they met with Williams and Kelly, who, they understood, was acting as Williams' lawyer. Detective Leaming repeated the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, and told Williams:</p>
<blockquote>"[W]e both know that you're being represented here by Mr. Kelly and you're being represented by Mr. McKnight in Des Moines, and . . . I want you to remember this because we'll be visiting between here and Des Moines."</blockquote>
<p>Williams then conferred again with Kelly alone, and after this conference Kelly reiterated to Detective Leaming that <span class="star-pagination">*392</span> Williams was not to be questioned about the disappearance of Pamela Powers until after he had consulted with McKnight back in Des Moines. When Leaming expressed some reservations, Kelly firmly stated that the agreement with McKnight was to be carried outthat there was to be no interrogation of Williams during the automobile journey to Des Moines. Kelly was denied permission to ride in the police car back to Des Moines with Williams and the two officers.</p>
<p>The two detectives, with Williams in their charge, then set out on the 160-mile drive. At no time during the trip did Williams express a willingness to be interrogated in the absence of an attorney. Instead, he stated several times that "[w]hen I get to Des Moines and see Mr. McKnight, I am going to tell you the whole story." Detective Leaming knew that Williams was a former mental patient, and knew also that he was deeply religious.</p>
<p>The detective and his prisoner soon embarked on a wideranging conversation covering a variety of topics, including the subject of religion. Then, not long after leaving Davenport and reaching the interstate highway, Detective Leaming delivered what has been referred to in the briefs and oral arguments as the "Christian burial speech." Addressing Williams as "Reverend," the detective said:</p>
<blockquote>"I want to give you something to think about while we're traveling down the road. . . . Number one, I want you to observe the weather conditions, it's raining, it's sleeting, it's freezing, driving is very treacherous, visibility is poor, it's going to be dark early this evening. They are predicting several inches of snow for tonight, and I feel that you yourself are the only person that knows where this little girl's body is, that you yourself have only been there once, and if you get a snow on top of it you yourself may be unable to find it. And, since we will be going right past the area on the way into <span class="star-pagination">*393</span> Des Moines, I feel that we could stop and locate the body, that the parents of this little girl should be entitled to a Christian burial for the little girl who was snatched away from them on Christmas [E]ve and murdered. And I feel we should stop and locate it on the way in rather than waiting until morning and trying to come back out after a snow storm and possibly not being able to find it at all."</blockquote>
<p>Williams asked Detective Leaming why he thought their route to Des Moines would be taking them past the girl's body, and Leaming responded that he knew the body was in the area of Mitchellvillea town they would be passing on the way to Des Moines.<sup>[1]</sup> Leaming then stated: "I do not want you to answer me. I don't want to discuss it any further. Just think about it as we're riding down the road."</p>
<p>As the car approached Grinnell, a town approximately 100 miles west of Davenport, Williams asked whether the police had found the victim's shoes. When Detective Leaming replied that he was unsure, Williams directed the officers to a service station where he said he had left the shoes; a search for them proved unsuccessful. As they continued towards Des Moines, Williams asked whether the police had found the blanket, and directed the officers to a rest area where he said he had disposed of the blanket. Nothing was found. The car continued towards Des Moines, and as it approached Mitchellville, Williams said that he would show the officers where the body was. He then directed the police to the body of Pamela Powers.</p>
<p>Williams was indicted for first-degree murder. Before trial, his counsel moved to suppress all evidence relating to or resulting from any statements Williams had made during the automobile ride from Davenport to Des Moines. After <span class="star-pagination">*394</span> an evidentiary hearing the trial judge denied the motion. He found that "an agreement was made between defense counsel and the police officials to the effect that the Defendant was not to be questioned on the return trip to Des Moines," and that the evidence in question had been elicited from Williams during "a critical stage in the proceedings requiring the presence of counsel on his request." The judge ruled, however, that Williams had "waived his right to have an attorney present during the giving of such information."<sup>[2]</sup></p>
<p>The evidence in question was introduced over counsel's continuing objection at the subsequent trial. The jury found Williams guilty of murder, and the judgment of conviction was affirmed by the Iowa Supreme Court, a bare majority of whose members agreed with the trial court that Williams had "waived his right to the presence of his counsel" on the automobile ride from Davenport to Des Moines. <i>State</i> v. <i>Williams,</i> <span class="citation" data-id="9720125"><a href="/opinion/2115457/state-v-williams/#402" aria-description="Citation for case: State v. Williams">182 N. W. 2d 396, 402</a></span>. The four dissenting justices expressed the view that "when counsel and police have agreed defendant is not to be questioned until counsel is present and defendant has been advised not to talk and repeatedly has stated he will tell the whole story after he talks with counsel, the state should be required to make a stronger showing of intentional voluntary waiver than was made here." <span class="citation" data-id="9720125"><a href="/opinion/2115457/state-v-williams/#408" aria-description="Citation for case: State v. Williams"><i>Id.,</i> at 408</a></span>.</p>
<p>Williams then petitioned for a writ of habeas corpus in the United States District Court for the Southern District of Iowa. Counsel for the State and for Williams stipulated that "the case would be submitted on the record of facts and proceedings in the trial court, without taking of further testimony." The District Court made findings of fact as summarized above, and concluded as a matter of law that the evidence in question had been wrongly admitted at <span class="star-pagination">*395</span> Williams' trial. This conclusion was based on three alternative and independent grounds: (1) that Williams had been denied his constitutional right to the assistance of counsel; (2) that he had been denied the constitutional protections defined by this Court's decisions in <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span>, and <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span>; and (3) that in any event, his self-incriminatory statements on the automobile trip from Davenport to Des Moines had been involuntarily made. Further, the District Court ruled that there had been no waiver by Williams of the constitutional protections in question. <span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/" aria-description="Citation for case: Williams v. Brewer">375 F. Supp. 170</a></span>.</p>
<p>The Court of Appeals for the Eighth Circuit, with one judge dissenting, affirmed this judgment, <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d 227</a></span>, and denied a petition for rehearing en banc. We granted certiorari to consider the constitutional issues presented. <span class="citation multiple-matches"><a href="/c/U.%20S./423/1031/">423 U. S. 1031</a></span>.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>Before turning to those issues, we must consider the petitioner's threshold claim that the District Court disregarded the provisions of <span class="citation no-link">28 U. S. C. § 2254</span> (d) in making its findings of fact in this case. That statute, which codifies most of the criteria set out in <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span>, provides that, subject to enumerated exceptions, federal habeas corpus courts shall accept as correct the factual determinations made by the courts of the States.<sup>[3]</sup></p>
<p><span class="star-pagination">*396</span> We conclude that there was no disregard of § 2254 (d) in this case. Although either of the parties might well have requested an evidentiary hearing in the federal habeas corpus proceedings, <i>Townsend</i> v. <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#322" aria-description="Citation for case: Townsend v. Sain"><i>Sain, supra,</i> at 322</a></span>, they both instead voluntarily agreed in advance that the federal court should decide the case on the record made in the courts of the State. In so proceeding, the District Court made no <span class="star-pagination">*397</span> findings of fact in conflict with those of the Iowa courts. The District Court did make some additional findings of fact based upon its examination of the state-court record, among them the findings that Kelly, the Davenport lawyer, had requested permission to ride in the police car from Davenport to Des Moines and that Detective Leaming had refused this request. But the additional findings were conscientiously and carefully explained by the District Court, <span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/#175" aria-description="Citation for case: Williams v. Brewer">375 F. Supp., at 175-176</a></span>, and were reviewed and approved by the Court of Appeals, which expressly held that "the District Court correctly applied <span class="citation no-link">28 U. S. C. § 2254</span> in its resolution of the disputed evidentiary facts, and that the facts as found by the District Court had substantial basis in the record," <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/#231" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d, at 231</a></span>. The strictures of <span class="citation no-link">28 U. S. C. § 2254</span> (d) require no more.<sup>[4]</sup></p>
<p></p>
<h2>B</h2>
<p>As stated above, the District Court based its judgment in this case on three independent grounds. The Court of Appeals appears to have affirmed the judgment on two of those grounds.<sup>[5]</sup> We have concluded that only one of them need be considered here.</p>
<p>Specifically, there is no need to review in this case the doctrine of <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> a doctrine designed to secure the constitutional privilege against compulsory self-incrimination, <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#438" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 438-439</a></span>. It is equally unnecessary to evaluate the ruling of the District Court that Williams' self-incriminating statements were, indeed, involuntarily made. Cf. <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>. For it is clear that the judgment before us must in any event be affirmed upon the ground that Williams was deprived <span class="star-pagination">*398</span> of a different constitutional rightthe right to the assistance of counsel.</p>
<p>This right, guaranteed by the Sixth and Fourteenth Amendments, is indispensable to the fair administration of our adversary system of criminal justice. Its vital need at the pretrial stage has perhaps nowhere been more succinctly explained than in Mr. Justice Sutherland's memorable words for the Court 44 years ago in <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, 57:</p>
<blockquote>"[D]uring perhaps the most critical period of the proceedings against these defendants, that is to say, from the time of their arraignment until the beginning of their trial, when consultation, thoroughgoing investigation and preparation were vitally important, the defendants did not have the aid of counsel in any real sense, although they were as much entitled to such aid during that period as at the trial itself."</blockquote>
<p>There has occasionally been a difference of opinion within the Court as to the peripheral scope of this constitutional right. See <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682</a></span>; <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span>. But its basic contours, which are identical in state and federal contexts, <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>; <i>Argersinger</i> v. <i>Hamlin,</i> <span class="citation" data-id="9424926"><a href="/opinion/108567/argersinger-v-hamlin/" aria-description="Citation for case: Argersinger v. Hamlin">407 U. S. 25</a></span>, are too well established to require extensive elaboration here. Whatever else it may mean, the right to counsel granted by the Sixth and Fourteenth Amendments means at least that a person is entitled to the help of a lawyer at or after the time that judicial proceedings have been initiated against him"whether by way of formal charge, preliminary hearing, indictment, information, or arraignment." <i>Kirby</i> v. <i>Illinois, supra,</i> at 689. See <i>Powell</i> v. <i>Alabama, supra</i><i>; </i><i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span>; <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span>; <i>Gideon</i> v. <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Wainwright, supra</a></span></i><i>; </i><i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span>; <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span>; <i>United</i> <span class="star-pagination">*399</span> <i>States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span>; <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span>; <i>Coleman</i> v. <i>Alabama, supra</i><i>.</i></p>
<p>There can be no doubt in the present case that judicial proceedings had been initiated against Williams before the start of the automobile ride from Davenport to Des Moines. A warrant had been issued for his arrest, he had been arraigned on that warrant before a judge in a Davenport courtroom, and he had been committed by the court to confinement in jail. The State does not contend otherwise.</p>
<p>There can be no serious doubt, either, that Detective Leaming deliberately and designedly set out to elicit information from Williams just as surely asand perhaps more effectively thanif he had formally interrogated him. Detective Leaming was fully aware before departing for Des Moines that Williams was being represented in Davenport by Kelly and in Des Moines by McKnight. Yet he purposely sought during Williams' isolation from his lawyers to obtain as much incriminating information as possible. Indeed, Detective Leaming conceded as much when he testified at Williams' trial:</p>
<blockquote>"Q. In fact, Captain, whether he was a mental patient or not, you were trying to get all the information you could before he got to his lawyer, weren't you?</blockquote>
<blockquote>"A. I was sure hoping to find out where that little girl was, yes, sir.</blockquote>
<p></p>
<h2>.....</h2>
<blockquote>"Q. Well, I'll put it this way: You was [<i>sic</i>] hoping to get all the information you could before Williams got back to McKnight, weren't you?</blockquote>
<blockquote>"A. Yes, sir."<sup>[6]</sup></blockquote>
<p><span class="star-pagination">*400</span> The state courts clearly proceeded upon the hypothesis that Detective Leaming's "Christian burial speech" had been tantamount to interrogation. Both courts recognized that Williams had been entitled to the assistance of counsel at the time he made the incriminating statements.<sup>[7]</sup> Yet no such constitutional protection would have come into play if there had been no interrogation.</p>
<p>The circumstances of this case are thus constitutionally indistinguishable from those presented in <i>Massiah</i> v. <i>United States, supra</i><i>.</i> The petitioner in that case was indicted for violating the federal narcotics law. He retained a lawyer, pleaded not guilty, and was released on bail. While he was free on bail a federal agent succeeded by surreptitious means in listening to incriminating statements made by him. Evidence of these statements was introduced against the petitioner at his trial, and he was convicted. This Court reversed the conviction, holding "that the petitioner was denied the basic protections of that guarantee [the right to counsel] when there was used against him at his trial evidence of his own incriminating words, which federal agents had deliberately elicited from him after he had been indicted and in the absence of his counsel." <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/#206" aria-description="Citation for case: Massiah v. United States">377 U. S., at 206</a></span>.</p>
<p>That the incriminating statements were elicited surreptitiously in the <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> case, and otherwise here, is constitutionally irrelevant. See <i>ibid.; </i><i>McLeod</i> v. <i>Ohio,</i> <span class="citation" data-id="107070"><a href="/opinion/107070/mcleod-v-ohio/" aria-description="Citation for case: McLEOD v. OHIO">381 U. S. 356</a></span>; <i>United States</i> v. <i>Crisp,</i> <span class="citation" data-id="293647"><a href="/opinion/293647/united-states-v-donald-roy-crisp/#358" aria-description="Citation for case: United States v. Donald Roy Crisp">435 F. 2d 354, 358</a></span> (CA7); <span class="star-pagination">*401</span> <i>United States ex rel. O'Connor</i> v. <i>New Jersey,</i> <span class="citation" data-id="282997"><a href="/opinion/282997/united-states-of-america-ex-rel-michael-oconnor-v-the-state-of-new/#636" aria-description="Citation for case: United States of America Ex Rel. Michael O&#x27;COnnOr v. The...">405 F. 2d 632, 636</a></span> (CA3); <i>Hancock</i> v. <i>White,</i> <span class="citation" data-id="276175"><a href="/opinion/276175/parker-l-hancock-warden-new-hampshire-state-prison-v-charles-white/" aria-description="Citation for case: Parker L. Hancock, Warden, New Hampshire State Prison v....">378 F. 2d 479</a></span> (CA1). Rather, the clear rule of <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> is that once adversary proceedings have commenced against an individual, he has a right to legal representation when the government interrogates him.<sup>[8]</sup> It thus requires no wooden or technical application of the <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> doctrine to conclude that Williams was entitled to the assistance of counsel guaranteed to him by the Sixth and Fourteenth Amendments.</p>
<p></p>
<h2>III</h2>
<p>The Iowa courts recognized that Williams had been denied the constitutional right to the assistance of counsel.<sup>[9]</sup> They held, however, that he had waived that right during the course of the automobile trip from Davenport to Des Moines. The state trial court explained its determination of waiver as follows:</p>
<blockquote>"The time element involved on the trip, the general circumstances of it, and more importantly the absence on the Defendant's part of any assertion of his right or desire not to give information absent the presence of his attorney, are the main foundations for the Court's conclusion that he voluntarily waived such right."</blockquote>
<p><span class="star-pagination">*402</span> In its lengthy opinion affirming this determination, the Iowa Supreme Court applied "the totality-of-circumstances test for a showing of waiver of constitutionally-protected rights in the absence of an express waiver," and concluded that "evidence of the time element involved on the trip, the general circumstances of it, and the absence of any request or expressed desire for the aid of counsel before or at the time of giving information, were sufficient to sustain a conclusion that defendant did waive his constitutional rights as alleged." <span class="citation" data-id="9720125"><a href="/opinion/2115457/state-v-williams/#401" aria-description="Citation for case: State v. Williams">182 N. W. 2d, at 401, 402</a></span>.</p>
<p>In the federal habeas corpus proceeding the District Court, believing that the issue of waiver was not one of fact but of federal law, held that the Iowa courts had "applied the wrong constitutional standards" in ruling that Williams had waived the protections that were his under the Constitution. <span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/#182" aria-description="Citation for case: Williams v. Brewer">375 F. Supp., at 182</a></span>. The court held "that it is the <i>government</i> which bears a heavy burden . . . but that is the burden which explicitly was placed on [Williams] by the state courts." <i><span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/" aria-description="Citation for case: Williams v. Brewer">Ibid.</a></span></i> (emphasis in original). After carefully reviewing the evidence, the District Court concluded:</p>
<blockquote>"[U]nder the proper standards for determining waiver, there simply is no evidence to support a waiver. . . . [T]here is no affirmative indication . . . that [Williams] did waive his rights. . . . [T]he state courts' emphasis on the absence of a demand for counsel was not only legally inappropriate, but factually unsupportable as well, since Detective Leaming himself testified that [Williams], on several occasions during the trip, indicated that he would talk <i>after</i> he saw Mr. McKnight. Both these statements and Mr. Kelly's statement to Detective Leaming that [Williams] would talk only after seeing Mr. McKnight in Des Moines certainly were assertions of [Williams'] `right or desire not to give information absent the presence of his attorney . . . .' Moreover, the statements were obtained only after Detective <span class="star-pagination">*403</span> Leaming's use of psychology on a person whom he knew to be deeply religious and an escapee from a mental hospitalwith the specific intent to elicit incriminating statements. In the face of this evidence, the State has produced no affirmative evidence whatsoever to support its claim of waiver, and, a fortiori, it cannot be said that the State has met its `heavy burden' of showing a knowing and intelligent waiver of . . . Sixth Amendment rights." <span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/#182" aria-description="Citation for case: Williams v. Brewer"><i>Id.,</i> at 182-183</a></span> (emphasis in original; footnote omitted).</blockquote>
<p>The Court of Appeals approved the reasoning of the District Court:</p>
<blockquote>"A review of the record here . . . discloses no facts to support the conclusion of the state court that [Williams] had waived his constitutional rights other than that [he] had made incriminating statements. . . . The District Court here properly concluded that an incorrect constitutional standard had been applied by the state court in determining the issue of waiver. . . .</blockquote>
<p></p>
<h2>.....</h2>
<blockquote>"[T]his court recently held that an accused can voluntarily, knowingly and intelligently waive his right to have counsel present at an interrogation after counsel has been appointed. . . . The prosecution, however, has the weighty obligation to show that the waiver was knowingly and intelligently made. We quite agree with Judge Hanson that the state here failed to so show." <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/#233" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d, at 233</a></span>.</blockquote>
<p>The District Court and the Court of Appeals were correct in the view that the question of waiver was not a question of historical fact, but one which, in the words of Mr. Justice Frankfurter, requires "application of constitutional principles to the facts as found . . . ." <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span>, <span class="star-pagination">*404</span> 507 (separate opinion). See <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S., at 309</a></span> n. 6, 318; <i>Brookhart</i> v. <i>Janis,</i> <span class="citation" data-id="107209"><a href="/opinion/107209/brookhart-v-janis/#4" aria-description="Citation for case: Brookhart v. Janis">384 U. S. 1, 4</a></span>.</p>
<p>The District Court and the Court of Appeals were also correct in their understanding of the proper standard to be applied in determining the question of waiver as a matter of federal constitutional lawthat it was incumbent upon the State to prove "an intentional relinquishment or abandonment of a known right or privilege." <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S., at 464</a></span>. That standard has been reiterated in many cases. We have said that the right to counsel does not depend upon a request by the defendant, <i>Carnley</i> v. <i>Cochran,</i> <span class="citation" data-id="9422395"><a href="/opinion/106388/carnley-v-cochran/#513" aria-description="Citation for case: Carnley v. Cochran">369 U. S. 506, 513</a></span>; cf. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#471" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 471</a></span>, and that courts indulge in every reasonable presumption against waiver, <i>e. g., </i><i>Brookhart</i> v. <span class="citation" data-id="107209"><a href="/opinion/107209/brookhart-v-janis/#4" aria-description="Citation for case: Brookhart v. Janis"><i>Janis, supra,</i> at 4</a></span>; <i>Glasser</i> v. <i>United States,</i> <span class="citation" data-id="103597"><a href="/opinion/103597/glasser-v-united-states/#70" aria-description="Citation for case: Glasser v. United States">315 U. S. 60, 70</a></span>. This strict standard applies equally to an alleged waiver of the right to counsel whether at trial or at a critical stage of pretrial proceedings. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#238" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 238-240</a></span>; <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#237" aria-description="Citation for case: United States v. Wade">388 U. S., at 237</a></span>.</p>
<p>We conclude, finally, that the Court of Appeals was correct in holding that, judged by these standards, the record in this case falls far short of sustaining petitioner's burden. It is true that Williams had been informed of and appeared to understand his right to counsel. But waiver requires not merely comprehension but relinquishment, and Williams' consistent reliance upon the advice of counsel in dealing with the authorities refutes any suggestion that he waived that right. He consulted McKnight by long-distance telephone before turning himself in. He spoke with McKnight by telephone again shortly after being booked. After he was arraigned, Williams sought out and obtained legal advice from Kelly. Williams again consulted with Kelly after Detective Leaming and his fellow officer arrived in Davenport. Throughout, Williams was advised not to make any statements before seeing McKnight in Des Moines, and was <span class="star-pagination">*405</span> assured that the police had agreed not to question him. His statements while in the car that he would tell the whole story <i>after</i> seeing McKnight in Des Moines were the clearest expressions by Williams himself that he desired the presence of an attorney before any interrogation took place. But even before making these statements, Williams had effectively asserted his right to counsel by having secured attorneys at both ends of the automobile trip, both of whom, acting as his agents, had made clear to the police that no interrogation was to occur during the journey. Williams knew of that agreement and, particularly in view of his consistent reliance on counsel, there is no basis for concluding that he disavowed it.<sup>[10]</sup></p>
<p>Despite Williams' express and implicit assertions of his right to counsel, Detective Leaming proceeded to elicit incriminating statements from Williams. Leaming did not preface this effort by telling Williams that he had a right to the presence of a lawyer, and made no effort at all to ascertain whether Williams wished to relinquish that right. The circumstances of record in this case thus provide no reasonable basis for finding that Williams waived his right to the assistance of counsel.</p>
<p>The Court of Appeals did not hold, nor do we, that under the circumstances of this case Williams <i>could not,</i> without notice to counsel, have waived his rights under the Sixth and <span class="star-pagination">*406</span> Fourteenth Amendments.<sup>[11]</sup> It only held, as do we, that he did not.</p>
<p></p>
<h2>IV</h2>
<p>The crime of which Williams was convicted was senseless and brutal, calling for swift and energetic action by the police to apprehend the perpetrator and gather evidence with which he could be convicted. No mission of law enforcement officials is more important. Yet "[d]isinterested zeal for the public good does not assure either wisdom or right in the methods it pursues." <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#605" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 605</a></span> (Frankfurter, J., concurring in judgment). Although we do not lightly affirm the issuance of a writ of habeas corpus in this case, so clear a violation of the Sixth and Fourteenth Amendments as here occurred cannot be condoned. The pressures on state executive and judicial officers charged with the administration of the criminal law are great, especially when the crime is murder and the victim a small child. But it is precisely the predictability of those pressures that makes imperative a resolute loyalty to the guarantees that the Constitution extends to us all.</p>
<p>The judgment of the Court of Appeals is affirmed.<sup>[12]</sup></p>
<p><i>It is so ordered.</i><sup>[13]</sup></p>
<p>MR. JUSTICE MARSHALL, concurring.</p>
<p>I concur wholeheartedly in my Brother STEWART'S opinion for the Court, but add these words in light of the dissenting <span class="star-pagination">*407</span> opinions filed today. The dissenters have, I believe, lost sight of the fundamental constitutional backbone of our criminal law. They seem to think that Detective Leaming's actions were perfectly proper, indeed laudable, examples of "good police work." In my view, good police work is something far different from catching the criminal at any price. It is equally important that the police, as guardians of the law, fulfill their responsibility to obey its commands scrupulously. For "in the end life and liberty can be as much endangered from illegal methods used to convict those thought to be criminals as from the actual criminals themselves." <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#320" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 320-321</a></span> (1959).</p>
<p>In this case, there can be no doubt that Detective Leaming consciously and knowingly set out to violate Williams' Sixth Amendment right to counsel and his Fifth Amendment privilege against self-incrimination, as Leaming himself understood those rights. Leaming knew that Williams had been advised <span class="star-pagination">*408</span> by two lawyers not to make any statements to police until he conferred in Des Moines with his attorney there, Mr. McKnight. Leaming surely understood, because he had overheard McKnight tell Williams as much, that the location of the body would be revealed to police. Undoubtedly Leaming realized the way in which that information would be conveyed to the police: McKnight would learn it from his client and then he would lead police to the body. Williams would thereby be protected by the attorney-client privilege from incriminating himself by directly demonstrating his knowledge of the body's location, and the unfortunate Powers child could be given a "Christian burial."</p>
<p>Of course, this scenario would accomplish all that Leaming sought from his investigation except that it would not produce incriminating statements or actions from Williams. Accordingly, Leaming undertook his charade to pry such evidence from Williams. After invoking the no-passengers rule to prevent attorney Kelly from accompanying the prisoner, Leaming had Williams at his mercy: during the three- or four-hour trip he could do anything he wished to elicit a confession. The detective demonstrated once again "that the efficiency of the rack and the thumbscrew can be matched, given the proper subject, by more sophisticated modes of `persuasion.'" <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206</a></span> (1960).</p>
<p>Leaming knowingly isolated Williams from the protection of his lawyers and during that period he intentionally "persuaded" him to give incriminating evidence. It is this intentional police misconductnot good police practicethat the Court rightly condemns. The heinous nature of the crime is no excuse, as the dissenters would have it, for condoning knowing and intentional police transgression of the constitutional rights of a defendant. If Williams is to go freeand given the ingenuity of Iowa prosecutors on retrial or in a civil commitment proceeding, I doubt very much that there is any chance a dangerous criminal will be loosed on the streets, the <span class="star-pagination">*409</span> bloodcurdling cries of the dissents notwithstandingit will hardly be because he deserves it. It will be because Detective Leaming, knowing full well that he risked reversal of Williams' conviction, intentionally denied Williams the right of <i>every</i> American under the Sixth Amendment to have the protective shield of a lawyer between himself and the awesome power of the State.</p>
<p>I think it appropriate here to recall not Mr. Justice Cardozo's opinion in <i>People</i> v. <i>Defore,</i> <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">242 N. Y. 13</a></span>, <span class="citation" data-id="3580565"><a href="/opinion/3599253/people-v-defore/" aria-description="Citation for case: People v. Defore">150 N. E. 585</a></span> (1926), see opinion of THE CHIEF JUSTICE, <i>post,</i> at 416, and n. 1, but rather the closing words of Mr. Justice Brandeis' great dissent in <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#471" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 471, 485</a></span> (1928):</p>
<blockquote>"In a government of laws, existence of the government will be imperilled if it fails to observe the law scrupulously. Our Government is the potent, the omnipresent teacher. For good or for ill, it teaches the whole people by its example. Crime is contagious. If the Government becomes a lawbreaker, it breeds contempt for law; it invites every man to become a law unto himself; it invites anarchy. To declare that in the administration of the criminal law the end justifies the meansto declare that the Government may commit crimes in order to secure the conviction of a private criminalwould bring terrible retribution. Against that pernicious doctrine this Court should resolutely set its face."</blockquote>
<p>MR. JUSTICE POWELL, concurring.</p>
<p>As the dissenting opinion of THE CHIEF JUSTICE sharply illustrates, resolution of the issues in this case turns primarily on one's perception of the facts. There is little difference of opinion, among the several courts and numerous judges who have reviewed the case, as to the relevant constitutional principles: (i) Williams had the right to assistance of counsel; <span class="star-pagination">*410</span> (ii) once that right attached (it is conceded that it had in this case), the State could not properly interrogate Williams in the absence of counsel unless he voluntarily and knowingly waived the right; and (iii) the burden was on the State to show that Williams in fact had waived the right before the police interrogated him.</p>
<p>The critical factual issue is whether there had been a voluntary waiver, and this turns in large part upon whether there was interrogation. As my dissenting Brothers view the facts so differently from my own perception of them, I will repeat briefly the background, setting, and factual predicate to the incriminating statements by Williamseven though the opinion of the Court sets forth all of this quite accurately.</p>
<p></p>
<h2>I</h2>
<p>Prior to the automobile trip from Davenport to Des Moines, Williams had been arrested, booked, and carefully given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. It is settled constitutional doctrine that he then had the right to the assistance of counsel. His exercise of this right was evidenced uniquely in this case. Williams had consulted counsel prior to his arrest, and surrendered to the police on advice of counsel. At all times thereafter Williams, to the knowledge of the police, had two attorneys: McKnight, whom Williams consulted initially and who awaited his arrival in Des Moines, and Kelly, who had represented Williams in Davenport where he surrendered. Significantly, the recognition by the police of the status of counsel was evidenced by the <i>express agreement</i> between McKnight and the appropriate police officials that the officers who would drive Williams to Des Moines would not interrogate him in the absence of counsel.</p>
<p>The incriminating statements were made by Williams during the long ride while in the custody of two police officers, and in the absence of his retained counsel. The dissent of THE <span class="star-pagination">*411</span> CHIEF JUSTICE concludes that prior to these statements, Williams had "made a valid waiver" of his right to have counsel present. <i>Post,</i> at 417. This view disregards the record evidence clearly indicating that the police engaged in interrogation of Williams. For example, the District Court noted:</p>
<blockquote>"According to Detective Leaming's own testimony, the specific purpose of this conversation [which was initiated by Leaming and which preceded Williams' confession] was to obtain statements and information from [Williams] concerning the missing girl." <span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/#174" aria-description="Citation for case: Williams v. Brewer">375 F. Supp. 170, 174</a></span>.</blockquote>
<p>In support of that finding, the District Court quoted extensively from Leaming's testimony, including the following:</p>
<blockquote>"Q. In fact, Captain, whether [Williams] was a mental patient or not, you were trying to get all the information you could before he got to his lawyer, weren't you?</blockquote>
<blockquote>"A. I was sure hoping to find out where that little girl was, yes, sir.</blockquote>
<p></p>
<h2>.....</h2>
<blockquote>"Q. Well, I'll put it this way: You were hoping to get all the information you could before Williams got back to McKnight, weren't you?</blockquote>
<blockquote>"A. Yes, sir." <i><span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/" aria-description="Citation for case: Williams v. Brewer">Ibid.</a></span></i>
</blockquote>
<p>After finding, upon a full review of the facts, that there had been "interrogation," the District Court addressed the ultimate issue of "waiver" and concluded not only that the State had failed to carry its burden but also that</p>
<blockquote>"there is <i>nothing</i> in the record to indicate that [Williams] waived his Fifth and Sixth Amendment rights <i>except</i> the fact that statements eventually were obtained." <span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/#182" aria-description="Citation for case: Williams v. Brewer"><i>Id.,</i> at 182</a></span>. (Emphasis in original.)</blockquote>
<p>The Court of Appeals stated affirmatively that "the facts <span class="star-pagination">*412</span> as found by the District Court had substantial basis in the record." <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/#231" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d 227, 231</a></span>.<sup>[1]</sup></p>
<p>I join the opinion of the Court which also finds that the efforts of Detective Leaming "to elicit information from Williams," as conceded by counsel for petitioner at oral argument, <i>ante,</i> at 400 n. 6, were a skillful and effective form of interrogation. Moreover, the entire setting was conducive to the psychological coercion that was successfully exploited. Williams was known by the police to be a young man with quixotic religious convictions and a history of mental disorders. The date was the day after Christmas, the weather was ominous, and the setting appropriate for Detective Leaming's talk of snow concealing the body and preventing a "Christian burial." Williams was alone in the automobile with two police officers for several hours. It is clear from the record, as both of the federal courts below found, that there was no evidence of a knowing and voluntary waiver of the right to have counsel present beyond the fact that Williams ultimately confessed. It is settled law that an inferred waiver of a constitutional right is disfavored. <i>Estelle</i> v. <i>Williams,</i> <span class="citation" data-id="9426383"><a href="/opinion/109438/estelle-v-williams/#515" aria-description="Citation for case: Estelle v. Williams">425 U. S. 501, 515</a></span> (1976) (POWELL, J., concurring). I find no basis in the record of this caseor in the dissenting opinions <span class="star-pagination">*413</span> for disagreeing with the conclusion of the District Court that "the State has produced no affirmative evidence whatsoever to support its claim of waiver." <span class="citation" data-id="1669210"><a href="/opinion/1669210/williams-v-brewer/#183" aria-description="Citation for case: Williams v. Brewer">375 F. Supp., at 183</a></span>.</p>
<p>The dissenting opinion of THE CHIEF JUSTICE states that the Court's holding today "conclusively presumes a suspect is legally incompetent to change his mind and tell the truth until an attorney is present." <i>Post,</i> at 419. I find no justification for this view. On the contrary, the opinion of the Court is explicitly clear that the right to assistance of counsel may be waived, after it has attached, without notice to or consultation with counsel. <i>Ante,</i> at 405-406. We would have such a case here if petitioner had proved that the police officers refrained from coercion and interrogation, as they had agreed, and that Williams freely on his own initiative had confessed the crime.</p>
<p></p>
<h2>II</h2>
<p>In discussing the exclusionary rule, the dissenting opinion of THE CHIEF JUSTICE refers to <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976), decided last Term. In that case, we held that a federal court need not apply the exclusionary rule on habeas corpus review of a Fourth Amendment claim absent a showing that the state prisoner was denied an opportunity for a full and fair litigation of that claim at trial and on direct review.</p>
<p>This case also involves review on habeas corpus of a state conviction, and the decisions that the Court today affirms held that Williams' incriminating statements should have been excluded.<sup>[2]</sup> As <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> was decided subsequently to these <span class="star-pagination">*414</span> decisions, the courts below had no occasion to consider whether the principle enunciated in <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> may have been applicable in this case. That question has not been presented in the briefs or arguments submitted to us,<sup>[3]</sup> and we therefore have no occasion to consider the possible applicability of <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span>.</i> The applicability of the rationale of <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> in the Fifth and Sixth Amendment context raises a number of unresolved issues. Many Fifth and Sixth Amendment claims arise in the context of challenges to the fairness of a trial or to the integrity of the factfinding process. In contrast, Fourth Amendment claims uniformly involve evidence that is "typically reliable and often the most probative information bearing on the guilt or innocence of the defendant." <i>Stone</i> v. <i>Powell, supra,</i> at 490. Whether the rationale of <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> should be applied to those Fifth and Sixth Amendment claims or classes of claims that more closely parallel claims under the Fourth Amendment is a question as to which I intimate no view, and which should be resolved only after the implications of such a ruling have been fully explored.</p>
<p>MR. JUSTICE STEVENS, concurring.</p>
<p>MR. JUSTICE STEWART, in his opinion for the Court which I join, MR. JUSTICE POWELL, and MR. JUSTICE MARSHALL have <span class="star-pagination">*415</span> accurately explained the reasons why the law requires the result we reach today. Nevertheless, the strong language in the dissenting opinions prompts me to add this brief comment about the Court's function in a case such as this.</p>
<p>Nothing that we write, no matter how well reasoned or forcefully expressed, can bring back the victim of this tragedy or undo the consequences of the official neglect which led to the respondent's escape from a state mental institution. The emotional aspects of the case make it difficult to decide dispassionately, but do not qualify our obligation to apply the law with an eye to the future as well as with concern for the result in the particular case before us.</p>
<p>Underlying the surface issues in this case is the question whether a fugitive from justice can rely on his lawyer's advice given in connection with a decision to surrender voluntarily. The defendant placed his trust in an experienced Iowa trial lawyer who in turn trusted the Iowa law enforcement authorities to honor a commitment made during negotiations which led to the apprehension of a potentially dangerous person. Under any analysis, this was a critical stage of the proceeding in which the participation of an independent professional was of vital importance to the accused and to society. At this stageas in countless others in which the law profoundly affects the life of the individualthe lawyer is the essential medium through which the demands and commitments of the sovereign are communicated to the citizen. If, in the long run, we are seriously concerned about the individual's effective representation by counsel, the State cannot be permitted to dishonor its promise to this lawyer.<sup>[*]</sup></p>
<p>MR. CHIEF JUSTICE BURGER, dissenting.</p>
<p>The result in this case ought to be intolerable in any society which purports to call itself an organized society. It continues <span class="star-pagination">*416</span> the Courtby the narrowest marginon the much-criticized course of punishing the public for the mistakes and misdeeds of law enforcement officers, instead of punishing the officer directly, if in fact he is guilty of wrongdoing. It mechanically and blindly keeps reliable evidence from juries whether the claimed constitutional violation involves gross police misconduct or honest human error.</p>
<p>Williams is guilty of the savage murder of a small child; no member of the Court contends he is not. While in custody, and after no fewer than <i>five</i> warnings of his rights to silence and to counsel, he led police to the concealed body of his victim. The Court concedes Williams was not threatened or coerced and that he spoke and acted voluntarily and with full awareness of his constitutional rights. In the face of all this, the Court now holds that because Williams was prompted by the detective's statementnot interrogation but a statement the jury must not be told how the police found the body.</p>
<p>Today's holding fulfills Judge (later Mr. Justice) Cardozo's grim prophecy that someday some court might carry the exclusionary rule to the absurd extent that its operative effect would exclude evidence relating to the body of a murder victim because of the means by which it was found.<sup>[1]</sup> In so ruling <span class="star-pagination">*417</span> the Court regresses to playing a grisly game of "hide and seek," once more exalting the sporting theory of criminal justice which has been experiencing a decline in our jurisprudence. With JUSTICES WHITE, BLACKMUN, and REHNQUIST, I categorically reject the remarkable notion that the police in this case were guilty of unconstitutional misconduct, or any conduct justifying the bizarre result reached by the Court. Apart from a brief comment on the merits, however, I wish to focus on the irrationality of applying the increasingly discredited exclusionary rule to this case.</p>
<p></p>
<h2>(1)</h2>
<p><i>The Court Concedes Williams' Disclosures Were Voluntary</i></p>
<p>Under well-settled precedents which the Court freely acknowledges, it is very clear that Williams had made a valid waiver of his Fifth Amendment right to silence and his Sixth Amendment right to counsel when he led police to the child's body. Indeed, even under the Court's analysis I do not understand how a contrary conclusion is possible.</p>
<p>The Court purports to apply as the appropriate constitutional waiver standard the familiar "intentional relinquishment or abandonment of a known right or privilege" test of <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938). <i>Ante,</i> at 404. The Court assumes, without deciding, that Williams' conduct and statements were voluntary. It concedes, as it must, <i>ibid.,</i> that Williams had been informed of and fully understood his constitutional rights and the consequences of their waiver. Then, having either assumed or found every element necessary to make out a valid waiver under its own test, the <span class="star-pagination">*418</span> Court reaches the astonishing conclusion that no valid waiver has been demonstrated.</p>
<p>This remarkable result is compounded by the Court's failure to define what evidentiary showing the State failed to make. Only recently, in <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span>, 238 n. 25 (1973), the Court analyzed the distinction between a voluntary act and the waiver of a right; there MR. JUSTICE STEWART stated for the Court:</p>
<blockquote>"[T]he question whether a person has acted `voluntarily' is quite distinct from the question whether he has `waived' a trial right. The former question, as we made clear in <i>Brady</i> v. <i>United States,</i> 397 U. S. [742,] 749, can be answered only by examining all the relevant circumstances to determine if he has been coerced. The latter question turns on the extent of his knowledge."</blockquote>
<p>Similarly, in <i>McMann</i> v. <i>Richardson,</i> <span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/#766" aria-description="Citation for case: McMann v. Richardson">397 U. S. 759, 766</a></span> (1970), we said that since a guilty plea constituted a waiver of a host of constitutional rights, "it must be an intelligent act `done with sufficient awareness of the relevant circumstances and likely consequences.' " If the Court today applied these standards with fidelity to the <i><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span></i> and <i><span class="citation" data-id="9424256"><a href="/opinion/108138/mcmann-v-richardson/" aria-description="Citation for case: McMann v. Richardson">McMann</a></span></i> holdings it could not reach the result now announced.</p>
<p>The evidence is uncontradicted that Williams had abundant knowledge of his right to have counsel present and of his right to silence. Since the Court does not question his mental competence, it boggles the mind to suggest that Williams could not understand that leading police to the child's body would have other than the most serious consequences. All of the elements necessary to make out a valid waiver are shown by the record and acknowledged by the Court; we thus are left to guess how the Court reached its holding.</p>
<p>One plausible but unarticulated basis for the result reached is that once a suspect has asserted his right not to talk without the presence of an attorney, it becomes legally impossible <span class="star-pagination">*419</span> for him to waive that right until he has seen an attorney. But constitutional rights are <i>personal,</i> and an otherwise valid waiver should not be brushed aside by judges simply because an attorney was not present. The Court's holding operates to "imprison a man in his privileges," <i>Adams</i> v. <i>United States ex rel. McCann,</i> <span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#280" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 280</a></span> (1942); it conclusively presumes a suspect is legally incompetent to change his mind and tell the truth until an attorney is present. It denigrates an individual to a nonperson whose free will has become hostage to a lawyer so that until the lawyer consents, the suspect is deprived of any legal right or power to decide for himself that he wishes to make a disclosure. It denies that the rights to counsel and silence are personal, nondelegable, and subject to a waiver only by that individual.<sup>[2]</sup> The opinions in support of the Court's judgment do not enlighten us as to why police conductwhether good or badshould operate to suspend Williams' right to change his mind and "tell all" at once rather than waiting until he reached Des Moines.<sup>[3]</sup></p>
<p>In his concurring opinion MR. JUSTICE POWELL suggests that the result in this case turns on whether Detective Leaming's remarks constituted "interrogation," as he views them, or whether they were "statements" intended to prick the conscience of the accused. I find it most remarkable that a murder case should turn on judicial interpretation that a statement becomes a question simply because it is followed by an <span class="star-pagination">*420</span> incriminating disclosure from the suspect. The Court seems to be saying that since Williams said he would "tell the whole story" at Des Moines, the police should have been content and waited; of course, that would have been the wiser course, especially in light of the nuances of constitutional jurisprudence applied by the Court, but a murder case ought not turn on such tenuous strands.</p>
<p>In any case, the Court assures us, <i>ante,</i> at 405-406, this is not at all what it intends, and that a valid waiver was <i>possible</i> in these circumstances, but was not quite made. Here, of course, Williams did not confess to the murder in so many words; it was his conduct in guiding police to the body, not his words, which incriminated him. And the record is replete with evidence that Williams knew precisely what he was doing when he guided police to the body. The human urge to confess wrongdoing is, of course, normal in all save hardened, professional criminals, as psychiatrists and analysts have demonstrated. T. Reik, The Compulsion to Confess (1972).</p>
<p></p>
<h2>(2)</h2>
<p></p>
<h2><i>The Exclusionary Rule Should Not be Applied to Non-egregious Police Conduct</i></h2>
<p>Even if there was no waiver, and assuming a technical violation occurred, the Court errs gravely in mechanically applying the exclusionary rule without considering whether that Draconian judicial doctrine should be invoked in these circumstances, or indeed whether any of its conceivable goals will be furthered by its application here.</p>
<p>The obvious flaws of the exclusionary rule as a judicial remedy are familiar. See <i>Bivens</i> v. <i>Six Unknown Fed. Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#411" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 411</a></span> (1971) (BURGER, C. J., dissenting); <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#498" aria-description="Citation for case: Stone v. Powell">428 U. S. 465, 498-502</a></span> (1976) (BURGER, C. J., concurring); Oaks, Studying the Exclusionary Rule in Search and Seizure, <span class="citation no-link">37 U. Chi. L. Rev. 665</span> (1970); Williams, The Exclusionary Rule Under Foreign LawEngland, <span class="star-pagination">*421</span> 52 J. Crim. L. 272 (1961). Today's holding interrupts what has been a more rational perception of the constitutional and social utility of excluding reliable evidence from the truth-seeking process. In its Fourth Amendment context, we have now recognized that the exclusionary rule is in no sense a <i>personal</i> constitutional right, but a judicially conceived remedial device designed to safeguard and effectuate guaranteed legal rights generally. <i>Stone</i> v. <i>Powell, supra,</i> at 482; <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/#443" aria-description="Citation for case: United States v. Janis">428 U. S. 433, 443-447</a></span> (1976); <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347-348</a></span> (1974); see <i>Alderman</i> v. <i>United States,</i> <span class="citation" data-id="9423945"><a href="/opinion/107872/alderman-v-united-states/#174" aria-description="Citation for case: Alderman v. United States">394 U. S. 165, 174-175</a></span> (1969). We have repeatedly emphasized that deterrence of unconstitutional or otherwise unlawful police conduct is the only valid justification for excluding reliable and probative evidence from the criminal factfinding process. <i>Stone</i> v. <i>Powell, supra,</i> at 485-486; <i>United States</i> v. <i>Janis, supra,</i> at 446, 458-459, n. 35; <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 536-539</a></span> (1975).</p>
<p>Accordingly, unlawfully obtained evidence is not automatically excluded from the factfinding process in all circumstances.<sup>[4]</sup> In a variety of contexts we inquire whether application <span class="star-pagination">*422</span> of the rule will promote its objectives sufficiently to justify the enormous cost it imposes on society. "As with any remedial device, the application of the rule has been restricted to those areas where its remedial objectives are thought most efficaciously served." <i>United States</i> v. <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra"><i>Calandra, supra,</i> at 348</a></span>; accord, <i>Stone</i> v. <i>Powell, supra,</i> at 486-491; <i>United States</i> v. <i>Janis, supra</i><i>; </i><i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#606" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590, 606, 608-609</a></span> (1975) (POWELL, J., concurring in part); <i>United States</i> v. <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#538" aria-description="Citation for case: United States v. Peltier"><i>Peltier, supra,</i> at 538-539</a></span>.</p>
<p>This is, of course, the familiar balancing process applicable to cases in which important competing interests are at stake. It is a recognition, albeit belated, that "the policies behind the exclusionary rule are not absolute," <i>Stone</i> v. <i>Powell, supra,</i> at 488. It acknowledges that so serious an infringement of the crucial truth-seeking function of a criminal prosecution should be allowed only when imperative to safeguard constitutional rights. An important factor in this amalgam is whether the violation at issue may properly be classed as "egregious." <i>Brown</i> v. <i>Illinois, supra,</i> at 609 (POWELL, J., concurring in part). The Court understandably does not try to characterize the police actions here as "egregious."</p>
<p>Against this background, it is striking that the Court fails even to consider whether the benefits secured by application of the exclusionary rule in this case outweigh its obvious social costs. Perhaps the failure is due to the fact that this case arises not under the Fourth Amendment, but under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), and the Sixth Amendment right to counsel. The Court apparently perceives the function of the exclusionary rule to be so different in these varying contexts that it must be mechanically and uncritically <span class="star-pagination">*423</span> applied in all cases arising outside the Fourth Amendment.<sup>[5]</sup></p>
<p>But this is demonstrably not the case where police conduct collides with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s procedural safeguards rather than with the Fifth Amendment privilege against compulsory self-incrimination. Involuntary and coerced admissions are suppressed because of the inherent unreliability of a confession wrung from an unwilling suspect by threats, brutality, or other coercion. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#242" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S., at 242</a></span>; <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#638" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618, 638</a></span> (1965); <i>Stone</i> v. <i>Powell,</i> <span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/#496" aria-description="Citation for case: Stone v. Powell">428 U. S., at 496-497</a></span> (BURGER, C. J., concurring); <i>Kaufman</i> v. <i>United States,</i> <span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/#237" aria-description="Citation for case: Kaufman v. United States">394 U. S. 217, 237</a></span> (1969) (Black, J., dissenting). We can all agree on " `[t]he abhorrence of society to the use of involuntary confessions,' " <i>Linkletter</i> v. <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/#638" aria-description="Citation for case: Linkletter v. Walker"><i>Walker, supra,</i> at 638</a></span>, and the need to preserve the integrity of the human personality and individual free will. <i>Ibid.; </i><i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206-207</a></span> (1960).</p>
<p>But use of Williams' disclosures and their fruits carries no risk whatever of unreliability, for the body was found where he said it would be found. Moreover, since the Court makes no issue of voluntariness, no dangers are posed to individual dignity or free will. <i>Miranda's</i> safeguards are premised on presumed unreliability long associated with confessions extorted by brutality or threats; they are not personal constitutional rights, but are simply judicially created prophylactic measures. <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span> (1974); <i>Doyle</i> <span class="star-pagination">*424</span> v. <i>Ohio,</i> <span class="citation" data-id="9426459"><a href="/opinion/109491/doyle-v-ohio/#617" aria-description="Citation for case: Doyle v. Ohio">426 U. S. 610, 617</a></span> (1976); <i>Brown</i> v. <i>Illinois, supra,</i> at 606 (POWELL, J., concurring in part).</p>
<p>Thus, in cases where incriminating disclosures are voluntarily made without coercion, and hence not violative of the Fifth Amendment, but are obtained in violation of one of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> prophylaxes, suppression is no longer automatic. Rather, we weigh the deterrent effect on unlawful police conduct, together with the normative Fifth Amendment justifications for suppression, against "the strong interest under any system of justice of making available to the trier of fact all concededly relevant and trustworthy evidence which either party seeks to adduce. . . . We also `must consider society's interest in the effective prosecution of criminals . . . .' " <i>Michigan</i> v. <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#450" aria-description="Citation for case: Michigan v. Tucker"><i>Tucker, supra,</i> at 450</a></span>.<sup>[6]</sup> This individualized consideration or balancing process with respect to the exclusionary sanction is possible in this case, as in others, because Williams' incriminating disclosures are not infected with any element of compulsion the Fifth Amendment forbids; nor, as noted earlier, does this evidence pose any danger of unreliability to the factfinding process. In short, there is no reason to exclude this evidence.</p>
<p>Similarly, the exclusionary rule is not uniformly implicated in the Sixth Amendment, particularly its pretrial aspects. We have held that</p>
<blockquote>"the core purpose of the counsel guarantee was to assure `Assistance' at trial, when the accused was confronted with both the intricacies of the law and the advocacy of the public prosecutor." <i>United States</i> v. <i>Ash,</i> <span class="citation" data-id="9425398"><a href="/opinion/108846/united-states-v-ash/#309" aria-description="Citation for case: United States v. Ash">413 U. S. 300, 309</a></span> (1973).</blockquote>
<p>Thus, the right to counsel is fundamentally a "trial" right necessitated by the legal complexities of a criminal prosecution <span class="star-pagination">*425</span> and the need to offset, to the trier of fact, the power of the State as prosecutor. See <i>Schneckloth</i> v. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#241" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Bustamonte, supra,</i> at 241</a></span>. It is now thought that modern law enforcement involves pretrial confrontations at which the defendant's fate might effectively be sealed before the right of counsel could attach. In order to make meaningful the defendant's opportunity to a fair trial and to assistance of counsel at that trialthe core purposes of the counsel guaranteethe Court formulated a <i>per se</i> rule guaranteeing counsel at what it has characterized as "critical" pretrial proceedings where substantial rights might be endangered. <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#224" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 224-227</a></span> (1967); <i>Schneckloth</i> v. <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#238" aria-description="Citation for case: Schneckloth v. Bustamonte"><i>Bustamonte, supra,</i> at 238-239</a></span>.</p>
<p>As we have seen in the Fifth Amendment setting, violations of prophylactic rules designed to safeguard other constitutional guarantees and deter impermissible police conduct need not call for the automatic suppression of evidence without regard to the purposes served by exclusion; nor do Fourth Amendment violations merit uncritical suppression of evidence. In other situations we decline to suppress eyewitness identifications which are the products of unnecessarily suggestive lineups or photo displays unless there is a "very substantial likelihood of irreparable misidentification." <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, 384</a></span> (1968). Recognizing that "[i]t is the likelihood of misidentification which violates a defendant's right to due process," <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188, 198</a></span> (1972), we exclude evidence only when essential to safeguard the integrity of the truth-seeking process. The test, in short, is the reliability of the evidence.</p>
<p>So, too, in the Sixth Amendment sphere failure to have counsel in a pretrial setting should not lead to the "knee-jerk" suppression of relevant and reliable evidence. Just as even uncounseled "critical" pretrial confrontations may often be conducted fairly and not in derogation of Sixth Amendment values, <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#298" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293, 298-299</a></span> (1967), evidence <span class="star-pagination">*426</span> obtained in such proceedings should be suppressed only when its use would imperil the core values the Amendment was written to protect. Having extended Sixth Amendment concepts originally thought to relate to the trial itself to earlier periods when a criminal investigation is focused on a suspect, application of the drastic bar of exclusion should be approached with caution.</p>
<p>In any event, the fundamental purpose of the Sixth Amendment is to safeguard the fairness of the trial and the integrity of the factfinding process.<sup>[7]</sup> In this case, where the evidence of how the child's body was found is of unquestioned reliability, and since the Court accepts Williams' disclosures as voluntary and uncoerced, there is no issue either of fairness or evidentiary reliability to justify suppression of truth. It appears suppression is mandated here for no other reason than the Court's general impression that it may have a beneficial effect on future police conduct; indeed, the Court fails to say even that much in defense of its holding.</p>
<p>Thus, whether considered under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> or the Sixth Amendment, there is no more reason to exclude the evidence in this case than there was in <i>Stone</i> v. <i>Powell</i><i>;</i><sup>[8]</sup> that holding was <span class="star-pagination">*427</span> premised on the utter reliability of evidence sought to be suppressed, the irrelevancy of the constitutional claim to the criminal defendant's factual guilt or innocence, and the minimal deterrent effect of habeas corpus on police misconduct. This case, like <i>Stone</i> v. <i>Powell</i><i>,</i> comes to us by way of habeas corpus after a fair trial and appeal in the state courts. Relevant factors in this case are thus indistinguishable from those in <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span>,</i> and from those in other Fourth Amendment cases suggesting a balancing approach toward utilization of the exclusionary sanction. Rather than adopting a formalistic analysis varying with the constitutional provision invoked,<sup>[9]</sup> we should apply the exclusionary rule on the basis of its benefits and costs, at least in those cases where the police conduct at issue is far from being outrageous or egregious.</p>
<p>In his opinion, MR. JUSTICE POWELL intimates that he agrees there is little sense in applying the exclusionary sanction where the evidence suppressed is " `typically reliable and often the most probative information bearing on the guilt or innocence of the defendant.' " <i>Ante,</i> at 414. Since he seems to concede that the evidence in question is highly reliable and probative, his joining the Court's opinion can be explained only by an insistence that the "question has not been presented in the briefs or arguments submitted to us." <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Ibid.</a></span></i> But petitioner has directly challenged the applicability of the exclusionary rule to this case, Brief for Petitioner 31-32, and has invoked principles of comity and federalism against reversal of the conviction. <i>Id.,</i> at 69-73. Moreover, at oral argumentthe first opportunity to do sopetitioner argued <span class="star-pagination">*428</span> that our intervening decision in <i>Stone</i> v. <i>Powell</i> should be extended to this case, just as respondent argued that it should not. Tr. of Oral Arg. 26-27, 49-50.</p>
<p>At the least, if our intervening decision in <i><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">Stone</a></span></i> makes application of the exclusionary rule in this case an open question which "should be resolved only after the implications of such a ruling have been fully explored," the plainly proper course is to vacate the judgment of the Court of Appeals and remand the case for reconsideration in light of that case. Indeed, only recently we actually applied the intervening decision of <i>Washington</i> v. <i>Davis,</i> <span class="citation" data-id="9426431"><a href="/opinion/109469/washington-v-davis/" aria-description="Citation for case: Washington v. Davis">426 U. S. 229</a></span> (1976), to resolve the constitutional issue in <i>Arlington Heights</i> v. <i>Metropolitan Housing Dev. Corp.,</i> <span class="citation" data-id="9426633"><a href="/opinion/109573/village-of-arlington-heights-v-metropolitan-housing-development-corp/" aria-description="Citation for case: Village of Arlington Heights v. Metropolitan Housing...">429 U. S. 252</a></span> (1977). There, we found no difficulty in applying the intervening holding ourselves without a remand to give the Court of Appeals an opportunity to reconsider its holding; we reached the correct result directly, over MR. JUSTICE WHITE'S dissent urging a remand. Today, the Court declines either to apply the intervening case of <i>Stone</i> v. <i>Powell</i><i>,</i> which MR. JUSTICE POWELL admits may well be controlling, or to remand for reconsideration in light of that case; this is all the more surprising since MR. JUSTICE POWELL wrote <i>Stone</i> v. <i>Powell</i> and today makes the fifth vote for the Court's judgment.</p>
<p>The bizarre result reached by the Court today recalls Mr. Justice Black's strong dissent in <i>Kaufman</i> v. <i>United States,</i> 394 U. S., at 231. There, too, a defendant sought release after his conviction had been affirmed on appeal. There, as here, the defendant's guilt was manifest, and was not called into question by the constitutional claims presented. This Court granted relief because it thought reliable evidence had been unconstitutionally obtained. Mr. Justice Black's reaction, foreshadowing our long overdue holding in <i>Stone</i> v. <i>Powell</i><i>,</i> serves as a fitting conclusion to the views I have expressed:</p>
<blockquote>"It is seemingly becoming more and more difficult to gain acceptance for the proposition that punishment of <span class="star-pagination">*429</span> the guilty is desirable, other things being equal. One commentator, who attempted in vain to dissuade this Court from today's holding, thought it necessary to point out that there is `a strong public interest in convicting the guilty.' . . .</blockquote>
<blockquote>". . . I would not let any criminal conviction become invulnerable to collateral attack where there is left remaining the probability or possibility that constitutional commands related to the integrity of the fact-finding process have been violated. In such situations society has failed to perform its obligation to prove beyond a reasonable doubt that the defendant committed the crime. But it is quite a different thing to permit collateral attack on a conviction after a trial according to due process when the defendant clearly is, by the proof and by his own admission, guilty of the crime charged. . . . In collateral attacks whether by habeas corpus or by § 2255 proceedings, I would always require that the convicted defendant raise the kind of constitutional claim that casts some shadow of a doubt on his guilt. This defendant is permitted to attack his conviction collaterally although he conceded at the trial and does not now deny that he had robbed the savings and loan association and although the evidence makes absolutely clear that he knew what he was doing. Thus, his guilt being certain, surely he does not have a constitutional right to get a new trial. I cannot possibly agree with the Court." 394 U. S., at 240-242.</blockquote>
<p>Like Mr. Justice Black in <i><span class="citation" data-id="9423948"><a href="/opinion/107874/kaufman-v-united-states/" aria-description="Citation for case: Kaufman v. United States">Kaufman</a></span>,</i> I cannot possibly agree with the Court.</p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE BLACKMUN and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>The respondent in this case killed a 10-year-old child. The majority sets aside his conviction, holding that certain <span class="star-pagination">*430</span> statements of unquestioned reliability were unconstitutionally obtained from him, and under the circumstances probably makes it impossible to retry him. Because there is nothing in the Constitution or in our previous cases which requires the Court's action, I dissent.</p>
<p></p>
<h2>I</h2>
<p>The victim in this case disappeared from a YMCA building in Des Moines, Iowa, on Christmas Eve in 1968. Respondent was seen shortly thereafter carrying a bundle wrapped in a blanket from the YMCA to his car. His car was found in Davenport, Iowa, 160 miles away on Christmas Day. A warrant was then issued for his arrest. On the day after Christmas respondent surrendered himself voluntarily to local police in Davenport where he was arraigned. The Des Moines police, in turn, drove to Davenport, picked respondent up and drove him back to Des Moines. During the trip back to Des Moines respondent made statements evidencing his knowledge of the whereabouts of the victim's clothing and body and leading the police to the body. The statements were, of course, made without the presence of counsel since no counsel was in the police car. The issue in this case is whether respondentwho was entitled not to make any statements to the police without consultation with and/or presence of counsel<sup>[1]</sup>validly waived those rights.</p>
<p>The relevant facts are as follows. Before the Des Moines police officers arrived in Davenport, respondent was twice advised, once by Davenport police and once by a judge, of his right to counsel under <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span>,</i> 384 U. S. <span class="star-pagination">*431</span> 436 (1966). Respondent had in any event not only retained counsel prior to the arrival of the Des Moines police, but had consulted with that counsel on the subject of talking to the police. His attorney, Mr. McKnight, spoke with him from the Des Moines police office when respondent was in the Davenport police office. He advised respondent not to talk to the Des Moines police officers during the trip back to Des Moines, but told him that he was "going to have to tell the officers where she [the victim] is" when he arrived in Des Moines. Respondent also consulted with a lawyer in Davenport, who also advised him against talking to the police during the ride back to Des Moines. Thus, prior to the arrival of the Des Moines police, respondent had been effectively informed by at least four people that he need not talk to the police in the absence of counsel during his trip to Des Moines. Then, when the Des Moines police arrived, one of them advised respondent, <i>inter alia,</i> "that he had a right to an attorney present during any questioning." The Des Moines police officer asked respondent: "[D]o you fully understand that?" Respondent said that he did. The officer then "advised him that [the officer] wanted him to be sure to remember what [the officer] had just told him because it was a long ride back to Des Moines and he and [the officer] would be visiting." Respondent then consulted again with the Davenport attorney, who advised him not to make any statements to the police officers and so informed the officersdirecting them not to question him. After this series of warnings by two attorneys, two sets of police officers, and a judge, the trip to Des Moines commenced.</p>
<p>Sometime early in the trip one of the officers, Detective Leaming, said:</p>
<blockquote>"I want to give you something to think about while we're traveling down the road. . . . Number one, I want you to observe the weather conditions, it's raining, it's sleeting, it's freezing, driving is very treacherous, visibility <span class="star-pagination">*432</span> is poor, it's going to be dark early this evening. They are predicting several inches of snow for tonight, and I feel that you yourself are the only person that knows where this little girl's body is, that you yourself have only been there once, and if you get a snow on top of it you yourself may be unable to find it. And, since we will be going right past the area on the way into Des Moines, I feel that we could stop and locate the body, that the parents of this little girl should be entitled to a Christian burial for the little girl who was snatched away from them on Christmas [E]ve and murdered. And I feel we should stop and locate it on the way in rather than waiting until morning and trying to come back out after a snow storm and possibly not being able to find it at all."</blockquote>
<p>Respondent asked Detective Leaming why he thought their route to Des Moines would be taking them past the girl's body, and Leaming responded that he knew the body was in the area of Mitchellvillea town they would be passing on the way to Des Moines. Leaming then stated: "I do not want you to answer me. I don't want to discuss it any further. Just think about it as we're riding down the road." On several occasions during the trip, respondent told the officers that he would tell them the whole story when he got to Des Moines and saw Mr. McKnightan indication that he knew he was entitled to wait until his counsel was present before talking to the police.<sup>[2]</sup></p>
<p><span class="star-pagination">*433</span> Some considerable time thereafter,<sup>[3]</sup> without any prompting on the part of any state official so far as the record reveals, respondent asked whether the police had found the victim's shoes. The subject of the victim's clothing had never been broached by the police nor suggested by anything the police had said. So far as the record reveals, the subject was suggested to respondent solely by the fact that the police car was then about to pass the gas station where respondent had hidden the shoes. When the police said they were unsure whether they had found the shoes, respondent directed them to the gas station. When the car continued on its way to Des Moines, responded asked whether the blanket had been found. Once again this subject had not previously been broached. Respondent directed the officers to a rest area where he had left the blanket. When the car again continued, respondent said that he would direct the officers to the victim's body, and he did so.</p>
<p></p>
<h2>II</h2>
<p>The strictest test of waiver which might be applied to this case is that set forth in <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938), and quoted by the majority, <i>ante,</i> at 404. In order to show that a right has been waived under this test, the State must prove "an intentional relinquishment or abandonment of a known right or privilege." The majority creates no new rule preventing an accused who has retained a lawyer from waiving his right to the lawyer's presence during questioning. The majority simply finds that no waiver was <i>proved</i> in this case. I disagree. That respondent knew of his right not to say anything to the officers without advice and presence of counsel is established on this record to a moral <span class="star-pagination">*434</span> certainty. He was advised of the right by three officials of the Statetelling at least one that he understood the right and by two lawyers.<sup>[4]</sup> Finally, he further demonstrated his knowledge of the right by informing the police that he would tell them the story in the presence of McKnight when they arrived in Des Moines. The issue in this case, then, is whether respondent relinquished that right intentionally.</p>
<p>Respondent relinquished his right not to talk to the police about his crime when the car approached the place where he had hidden the victim's clothes. Men usually intend to do what they do, and there is nothing in the record to support the proposition that respondent's decision to talk was anything but an exercise of his own free will. Apparently, without any prodding from the officers, respondentwho had earlier said that he would tell the whole story when he arrived in Des Moinesspontaneously changed his mind about the timing of his disclosures when the car approached the places where he had hidden the evidence. However, even if his statements were influenced by Detective Leaming's above-quoted statement, respondent's decision to talk in the absence of counsel can hardly be viewed as the product of an overborne will. The statement by Leaming was not coercive; it was accompanied by a request that respondent not respond to it; and it was delivered hours before respondent decided to make any statement. Respondent's waiver was thus knowing and intentional.</p>
<p>The majority's contrary conclusion seems to rest on the fact that respondent "asserted" his right to counsel by retaining and consulting with one lawyer and by consulting with another. How this supports the conclusion that respondent's later relinquishment of his right not to talk in the <span class="star-pagination">*435</span> absence of counsel was unintentional is a mystery. The fact that respondent consulted with counsel on the question whether he should talk to the police in counsel's absence makes his later decision to talk in counsel's absence <i>better</i> informed and, if anything, more intelligent.</p>
<p>The majority recognizes that even after this "assertion" of his right to counsel, it would have found that respondent waived his right not to talk in counsel's absence if his waiver had been express<i>i. e.,</i> if the officers had asked him in the car whether he would be willing to answer questions in counsel's absence and if he had answered "yes." <i>Ante,</i> at 405. But waiver is not a formalistic concept. Waiver is shown whenever the facts establish that an accused knew of a right and intended to relinquish it. Such waiver, even if not express,<sup>[5]</sup> was plainly shown here. The only other conceivable <span class="star-pagination">*436</span> basis for the majority's holding is the implicit suggestion, <i>ante,</i> at 400-401, that the right involved in <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), as distinguished from the right involved in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), is a right not to be <i>asked</i> any questions in counsel's absence rather than a right not to <i>answer</i> any questions in counsel's absence, and that the right not to be <i>asked</i> questions must be waived <i>before</i> the questions are asked. Such waferthin distinctions cannot determine whether a guilty murderer should go free. The only conceivable purpose for the presence of counsel during questioning is to protect an accused from making incriminating <i>answers.</i> Questions, unanswered, have no significance at all. Absent coercion<sup>[6]</sup>no matter how the <span class="star-pagination">*437</span> right involved is definedan accused is amply protected by a rule requiring waiver before or simultaneously with the giving by him of an answer or the making by him of a statement.</p>
<p></p>
<h2>III</h2>
<p>The consequence of the majority's decision is, as the majority recognizes, extremely serious. A mentally disturbed killer whose guilt is not in question may be released. Why? Apparently the answer is that the majority believes that the law enforcement officers acted in a way which involves some risk of injury to society and that such conduct should be deterred. However, the officers' conduct did not, and was not likely to, jeopardize the fairness of respondent's trial or in any way risk the conviction of an innocent manthe risk against which the Sixth Amendment guarantee of assistance of counsel is designed to protect. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span> (1932); <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938); <i>Hamilton</i> v. <i>Alabama,</i> <span class="citation" data-id="106300"><a href="/opinion/106300/hamilton-v-alabama/" aria-description="Citation for case: Hamilton v. Alabama">368 U. S. 52</a></span> (1961); <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963); <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span> (1963); <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967); <i>Coleman</i> v. <i>Alabama,</i> 399 U. S. 1 <span class="star-pagination">*438</span> (1970); and <i>Argersinger</i> v. <i>Hamlin,</i> <span class="citation" data-id="9424926"><a href="/opinion/108567/argersinger-v-hamlin/" aria-description="Citation for case: Argersinger v. Hamlin">407 U. S. 25</a></span> (1972). But see <i>Massiah</i> v. <i>United States, supra</i><i>.</i> The police did nothing "wrong," let alone anything "unconstitutional." To anyone not lost in the intricacies of the prophylactic rules of <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> the result in this case seems utterly senseless; and for the reasons stated in Part II, <i>supra,</i> even applying those rules as well as the rule of <i>Massiah</i> v. <i>United States, supra</i><i>,</i> the statements made by respondent were properly admitted. In light of these considerations, the majority's protest that the result in this case is justified by a "clear violation" of the Sixth and Fourteenth Amendments has a distressing hollow ring. I respectfully dissent.</p>
<p>MR. JUSTICE BLACKMUN, with whom MR. JUSTICE WHITE and MR. JUSTICE REHNQUIST join, dissenting.</p>
<p>The State of Iowa, and 21 States and others, as <i>amici curiae,</i> strongly urge that this Court's procedural (as distinguished from constitutional) ruling in <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), be re-examined and overruled. I, however, agree with the Court, <i>ante,</i> at 397, that this is not now the case in which that issue need be considered.</p>
<p>What the Court chooses to do here, and with which I disagree, is to hold that respondent Williams' situation was in the mold of <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), that is, that it was dominated by a denial to Williams of his Sixth Amendment right to counsel after criminal proceedings had been instituted against him. The Court rules that the Sixth Amendment was violated because Detective Leaming "purposely sought during Williams' isolation from his lawyers to obtain as much incriminating information as possible." <i>Ante,</i> at 399, and POWELL, J., concurring, <i>ante,</i> at 410-413. I cannot regard that as unconstitutional <i>per se.</i></p>
<p>First, the police did not deliberately seek to isolate Williams from his lawyers so as to deprive him of the <span class="star-pagination">*439</span> assistance of counsel. Cf. <i>Escobedo</i> v. <i>Illinois,</i> <span class="citation" data-id="9422869"><a href="/opinion/106883/escobedo-v-illinois/" aria-description="Citation for case: Escobedo v. Illinois">378 U. S. 478</a></span> (1964). The isolation in this case was a necessary incident of transporting Williams to the county where the crime was committed.<sup>[1]</sup></p>
<p>Second, Leaming's purpose was not solely to obtain incriminating evidence. The victim had been missing for only two days, and the police could not be certain that she was dead. Leaming, of course, and in accord with his duty, was "hoping to find out where that little girl was," <i>ante,</i> at 399, but such motivation does not equate with an intention to evade the Sixth Amendment.<sup>[2]</sup> Moreover, the Court seems to me to place an undue emphasis, <i>ante,</i> at 392, 400, and aspersion on what it and the lower courts have chosen to call the "Christian burial speech," and on Williams' "deeply religious" convictions.</p>
<p>Third, not every attempt to elicit information should be regarded as "tantamount to interrogation," <i>ante,</i> at 400. I am not persuaded that Leaming's observations and comments, made as the police car traversed the snowy and slippery miles between Davenport and Des Moines that winter afternoon, were an interrogation, direct or subtle, of Williams. Contrary to this Court's statement, <i>ibid.,</i> the Iowa Supreme Court appears to me to have thought and held otherwise, <i>State</i> v. <i>Williams,</i> <span class="citation" data-id="9720125"><a href="/opinion/2115457/state-v-williams/#403" aria-description="Citation for case: State v. Williams">182 N. W. 2d 396, 403-405</a></span> (1970), and I agree. Williams, after all, was counseled by lawyers, and warned by the arraigning judge in Davenport and by the <span class="star-pagination">*440</span> police, and yet it was he who started the travel conversations and brought up the subject of the criminal investigation. Without further reviewing the circumstances of the trip, I would say it is clear there was no interrogation. In this respect, I am in full accord with Judge Webster in his vigorous dissent, <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/#234" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d 227, 234-237</a></span>, and with the views implicitly indicated by Chief Judge Gibson and Judge Stephenson, who joined him in voting for rehearing en banc.</p>
<p>In summary, it seems to me that the Court is holding that <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> is violated whenever police engage in any conduct, in the absence of counsel, with the subjective desire to obtain information from a suspect after arraignment. Such a rule is far too broad. Persons in custody frequently volunteer statements in response to stimuli other than interrogation. See, <i>e. g., </i><i>United States</i> v. <i>Cook,</i> <span class="citation" data-id="333157"><a href="/opinion/333157/united-states-v-bobby-cook-and-laurell-cook/#152" aria-description="Citation for case: United States v. Bobby Cook and Laurell Cook">530 F. 2d 145, 152-153</a></span> (CA7), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./426/909/">426 U. S. 909</a></span> (1976) (defendant engaged officers in conversation while being transported to magistrate); <i>United States</i> v. <i>Martin,</i> <span class="citation" data-id="325420"><a href="/opinion/325420/united-states-v-james-craig-martin/#150" aria-description="Citation for case: United States v. James Craig Martin">511 F. 2d 148, 150-151</a></span> (CA8 1975) (agent initiated conversation with suspect, provoking damaging admission); <i>United States</i> v. <i>Menichino,</i> <span class="citation" data-id="319744"><a href="/opinion/319744/united-states-v-andrew-carmen-menichino/#939" aria-description="Citation for case: United States v. Andrew Carmen Menichino">497 F. 2d 935, 939-941</a></span> (CA5 1974) (incriminating statements volunteered during booking process); <i>Haire</i> v. <i>Sarver,</i> <span class="citation" data-id="9456496"><a href="/opinion/294723/l-v-haire-v-robert-sarver-commissioner-of-corrections/" aria-description="Citation for case: L. v. Haire v. Robert Sarver, Commissioner of Corrections">437 F. 2d 1262</a></span> (CA8), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/910/">404 U. S. 910</a></span> (1971) (statements volunteered in response to questioning of defendant's wife). When there is no interrogation, such statements should be admissible as long as they are truly voluntary.<sup>[3]</sup></p>
<p>The <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> point thus being of no consequence, I would vacate the judgment of the Court of Appeals and remand <span class="star-pagination">*441</span> the case for consideration of the issue of voluntariness, in the constitutional sense, of Williams' statements, an issue the Court of Appeals did not reach when the case was before it.</p>
<p>One final word: I can understand the discomfiture the Court obviously suffers and expresses in Part IV of its opinion, <i>ante,</i> at 406, and the like discomfiture expressed by Justice (now United States District Judge) Stuart of the Iowa court in the dissent he felt compelled to make by this Court's precedents, <span class="citation" data-id="9720125"><a href="/opinion/2115457/state-v-williams/#406" aria-description="Citation for case: State v. Williams">182 N. W. 2d, at 406</a></span>. This was a brutal, tragic, and heinous crime inflicted upon a young girl on the afternoon of the day before Christmas. With the exclusionary rule operating as the Court effectuates it, the decision today probably means that, as a practical matter, no new trial will be possible at this date eight years after the crime, and that this respondent necessarily will go free. That, of course, is not the standard by which a case of this kind strictly is to be judged. But, as Judge Webster in dissent below observed, <span class="citation" data-id="9461373"><a href="/opinion/324530/robert-anthony-williams-aka-anthony-erthel-williams-v-lou-v-brewer/#237" aria-description="Citation for case: Robert Anthony Williams, A/K/A Anthony Erthel Williams v....">509 F. 2d, at 237</a></span>, placing the case in sensible and proper perspective: "The evidence of Williams' guilt was overwhelming. No challenge is made to the reliability of the fact-finding process." I am in full agreement with that observation.</p>
<h2>NOTES</h2>
<p>[*]  <i>William J. Guste, Jr.,</i> Attorney General, and <i>Walter L. Smith, Jr.,</i> Assistant Attorney General, filed a brief for the State of Louisiana as <i>amicus curiae.</i>
</p>
<p><i>Fred E. Inbau</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal, joined by <i>Wayne W. Schmidt</i> and by officials for their respective States as follows: <i>William J. Baxley,</i> Attorney General of Alabama; <i>Bruce E. Babbitt,</i> Attorney General of Arizona, and <i>Frank T. Galati,</i> Assistant Attorney General; <i>James Guy Tucker,</i> Attorney General of Arkansas; <i>Evelle J. Younger,</i> Attorney General of California, and <i>William E. James,</i> Senior Assistant Attorney General; <i>Robert L. Shevin,</i> Attorney General of Florida, and <i>E. J. Salcines, Jr.; Wayne L. Kidwell,</i> Attorney General of Idaho, and <i>Christopher D. Bray,</i> Deputy Attorney General; <i>William J. Scott,</i> Attorney General of Illinois, and <i>James B. Zagel,</i> Assistant Attorney General; <i>Theodore L. Sendak,</i> Attorney General of Indiana, and <i>Donald P. Bogard,</i> Executive Assistant Attorney General; <i>Francis B. Burch,</i> Attorney General of Maryland; <i>A. F. Summer,</i> Attorney General of Mississippi, and <i>Karen Gilfoy,</i> Assistant Attorney General; <i>Paul L. Douglas,</i> Attorney General of Nebraska, and <i>Melvin K. Kamerlohr,</i> Assistant Attorney General; <i>Robert List,</i> Attorney General of Nevada; <i>William F. Hyland,</i> Attorney General of New Jersey, and <i>Robert Del Tufo,</i> First Assistant Attorney General; <i>Louis J. Lefkowitz,</i> Attorney General of New York, and <i>Samuel A. Hirshowitz,</i> First Assistant Attorney General; <i>Allen I. Olson,</i> Attorney General of North Dakota; <i>Larry Derryberry,</i> Attorney General of Oklahoma, and <i>Robert McDonald; Daniel R. McLeod,</i> Attorney General of South Carolina; <i>Vernon B. Romney,</i> Attorney General of Utah, and <i>William W. Barrett,</i> Assistant Attorney General; <i>Andrew P. Miller,</i> Attorney General of Virginia, and <i>Reno S. Harp III,</i> Deputy Attorney General; <i>Chauncey H. Browning, Jr.,</i> Attorney General of West Virginia, and <i>David P. Cleek,</i> Assistant Attorney General; and <i>V. Frank Mendicino,</i> Attorney General of Wyoming, and <i>Gerald A. Stack,</i> Deputy Attorney General.</p>
<p>[1]  The fact of the matter, of course, was that Detective Leaming possessed no such knowledge.</p>
<p>[2]  The opinion of the trial court denying Williams' motion to suppress is unreported.</p>
<p>[3]  Title <span class="citation no-link">28 U. S. C. § 2254</span> (d) provides:
</p>
<p>"(d) In any proceeding instituted in a Federal court by an application for a writ of habeas corpus by a person in custody pursuant to the judgment of a State court, a determination after a hearing on the merits of a factual issue, made by a State court of competent jurisdiction in a proceeding to which the applicant for the writ and the State or an officer or agent thereof were parties, evidenced by a written finding, written opinion, or other reliable and adequate written indicia, shall be presumed to be correct, unless the applicant shall establish or it shall otherwise appear, or the respondent shall admit</p>
<p>"(1) that the merits of the factual dispute were not resolved in the State court hearing;</p>
<p>"(2) that the factfinding procedure employed by the State court was not adequate to afford a full and fair hearing;</p>
<p>"(3) that the material facts were not adequately developed at the State court hearing;</p>
<p>"(4) that the State court lacked jurisdiction of the subject matter or over the person of the applicant in the State court proceeding;</p>
<p>"(5) that the applicant was an indigent and the State court, in deprivation of his constitutional right, failed to appoint counsel to represent him in the State court proceeding;</p>
<p>"(6) that the applicant did not receive a full, fair, and adequate hearing in the State court proceeding; or</p>
<p>"(7) that the applicant was otherwise denied due process of law in the State court proceeding;</p>
<p>"(8) or unless that part of the record of the State court proceeding in which the determination of such factual issue was made, pertinent to a determination of the sufficiency of the evidence to support such factual determination, is produced as provided for hereinafter, and the Federal court on a consideration of such part of the record as a whole concludes that such factual determination is not fairly supported by the record:</p>
<p>"And in an evidentiary hearing in the proceeding in the Federal court, when due proof of such factual determination has been made, unless the existence of one or more of the circumstances respectively set forth in paragraphs numbered (1) to (7), inclusive, is shown by the applicant, otherwise appears, or is admitted by the respondent, or unless the court concludes pursuant to the provisions of paragraph numbered (8) that the record in the State court proceeding, considered as a whole, does not fairly support such factual determination, the burden shall rest upon the applicant to establish by convincing evidence that the factual determination by the State court was erroneous."</p>
<p>[4]  Whether Williams waived his constitutional rights was not, of course, a question of fact, but an issue of federal law. See discussion, <i>infra,</i> at 401-404.</p>
<p>[5]  The Court of Appeals did not address the District Court's ruling that Williams' statements had been made involuntarily.</p>
<p>[6]  Counsel for petitioner, in the course of oral argument in this Court, acknowledged that the "Christian burial speech" was tantamount to interrogation:
</p>
<p>"Q: But isn't the point, really, Mr. Attorney General, what you indicated earlier, and that is that the officer wanted to elicit information from Williams</p>
<p>"A: Yes, sir.</p>
<p>"Q: by whatever techniques he used, I would suppose a lawyer would consider that he were pursuing interrogation.</p>
<p>"A: It is, but it was very brief." Tr. of Oral Arg. 17.</p>
<p>[7]  The Iowa trial court expressly acknowledged Williams' "right to have an attorney present during the giving of such information." See <i>supra,</i> at 394. The Iowa Supreme Court also expressly acknowledged Williams' "right to the presence of his counsel." See <i>ibid.</i></p>
<p>[8]  The only other significant factual difference between the present case and <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span></i> is that here the police had <i>agreed</i> that they would not interrogate Williams in the absence of his counsel. This circumstance plainly provides petitioner with no argument for distinguishing away the protection afforded by <i><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span>.</i>
</p>
<p>It is argued that this agreement may not have been an enforceable one. But we do not deal here with notions of offer, acceptance, consideration, or other concepts of the law of contracts. We deal with constitutional law. And every court that has looked at this case ha

[...TRUNCATED 30311 of 150311 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
