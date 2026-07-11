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

## GROUP: _overhaul2/lake/cases/Malloy v. Hogan.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Malloy v. Hogan"
type: case
citation: "378 U.S. 1 (1964)"
parallel_cite: "84 S. Ct. 1489; 12 L. Ed. 2d 653"
neutral_cite: 1964 U.S. LEXIS 993
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1964
date_decided: 1964-06-15
docket: 110
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1964-06-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Malloy v. Hogan
  varies_by_point: false
  scope_note: "Foundational incorporation of the Fifth Amendment privilege against the States; good law and the constitutional predicate for Miranda. Overruled Twining and Adamson on this point."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106862/malloy-v-hogan/"
  cluster_id: 106862
  opinion_id: 106862
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (cross-doctrine)"
related: ["[[Miranda v. Arizona]]", "[[Mapp v. Ohio]]", "[[Brown v. Mississippi]]", "[[Wolf v. Colorado]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "incorporation", "self-incrimination", "voluntariness"]
holding: "The Fifth Amendment privilege against self-incrimination is enforceable against the States through the Fourteenth Amendment by the same standards that apply to the Federal Government; Twining and Adamson are overruled to that extent."
lake:
  record_id: Malloy v. Hogan
  status: verified
  projected_at: 2026-07-06
---

# Malloy v. Hogan

*378 U.S. 1 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Malloy, on probation for a state gambling misdemeanor, was called before a state inquiry into gambling. He refused to answer questions about his arrest and associates, invoking the privilege against self-incrimination. The Connecticut courts, relying on *Twining v. New Jersey* and *Adamson v. California*, held the privilege did not bind the State, found the questions non-incriminatory, and held him in contempt — imprisoning him until he answered. He sought [[Common Legal Terms#habeas-corpus|habeas corpus]].

## Issue
Whether the Fifth Amendment privilege against self-incrimination is safeguarded against state action by the Fourteenth Amendment, and by what standard.

## Rule
The privilege is incorporated against the States. "We hold today that the Fifth Amendment's exception from compulsory self-incrimination is also protected by the Fourteenth Amendment against abridgment by the States." — 378 U.S. at 6. ^pin-6

"The Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringement—the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty . . . for such silence." — *Id.* at 8. ^pin-8

The same standard governs in both forums: the Fourteenth Amendment does not apply to the States merely "a 'watered-down, subjective version of the individual guarantees of the Bill of Rights.'" — *Id.* at 10–11. ^pin-10

## Application
Because the privilege binds the States by the same standard as the Federal Government, Connecticut could not imprison Malloy for contempt for declining to answer questions that might incriminate him, and its courts erred in measuring his claim against a less stringent, "watered-down" standard. Applying the federal test, his refusal was justified because truthful answers could have furnished a link in a chain of evidence connecting him to crime; the state inquiry could not compel him on pain of imprisonment.

## Conclusion
The Fifth Amendment privilege is enforceable against the States through the Fourteenth Amendment by the same standards as in federal proceedings; the contempt judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]]. *Twining* and *Adamson* were overruled to the extent they held otherwise.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Malloy* is a foundational incorporation decision: it harmonized the confession-voluntariness standard (rooted in [[Brown v. Mississippi]]) with the Fifth Amendment privilege and supplied the constitutional predicate for [[Miranda v. Arizona]] two years later. It draws on [[Mapp v. Ohio]] (which overruled [[Wolf v. Colorado]]) for the parallel incorporation of the Fourth Amendment.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*
- [[Miranda and Custodial Interrogation]] — *Related (cross-doctrine)*

## Sources
- *Malloy v. Hogan*, 378 U.S. 1 (1964) — https://www.courtlistener.com/opinion/106862/malloy-v-hogan/ — pinpoints: 6, 8, 10–11.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a0efbd6bf180bf43", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Malloy v. Hogan"}, "payload": {"all": [{"cite": "378 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "378"}, {"cite": "84 S. Ct. 1489", "page": "1489", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "84"}, {"cite": "12 L. Ed. 2d 653", "page": "653", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "12"}, {"cite": "1964 U.S. LEXIS 993", "page": "993", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1964"}], "display": "378 U.S. 1", "official": {"cite": "378 U.S. 1", "page": "1", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "378"}, "official_selection_present": true, "record_id": "Malloy v. Hogan"}}
{"assertion_id": "00b52bad7b4c7b2a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-8", "record_id": "Malloy v. Hogan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-8", "pinpoint_status": "slip-only", "quote": "The Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringement—the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty . . . for such silence.", "quote_fidelity": "mismatch", "record_id": "Malloy v. Hogan", "star_marker": null}}
{"assertion_id": "89c9f2c45dd122c5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-6", "record_id": "Malloy v. Hogan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-6", "pinpoint_status": "slip-only", "quote": "--- # Malloy v. Hogan *378 U.S. 1 (1964)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Malloy, on probation for a state gambling misdemeanor, was called before a state inquiry into gambling. He refused to answer questions about his arrest and associates, invoking the privilege against self-incrimination. The Connecticut courts, relying on *Twining v. New Jersey* and *Adamson v. California*, held the privilege did not bind the State, found the questions non-incriminatory, and held him in contempt — imprisoning him until he answered. He sought habeas corpus. ## Issue Whether the Fifth Amendment privilege against self-incrimination is safeguarded against state action by the Fourteenth Amendment, and by what standard. ## Rule The privilege is incorporated against the States.", "quote_fidelity": "mismatch", "record_id": "Malloy v. Hogan", "star_marker": null}}
{"assertion_id": "f2e15779bc2b5a97", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-10", "record_id": "Malloy v. Hogan"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-10", "pinpoint_status": "slip-only", "quote": "a 'watered-down, subjective version of the individual guarantees of the Bill of Rights.'", "quote_fidelity": "mismatch", "record_id": "Malloy v. Hogan", "star_marker": null}}
{"assertion_id": "20d6f51e86a5952e", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Malloy v. Hogan"}, "payload": {"as_of_content": "1964-06-15", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Malloy v. Hogan", "scope_note": "Foundational incorporation of the Fifth Amendment privilege against the States; good law and the constitutional predicate for Miranda. Overruled Twining and Adamson on this point.", "varies_by_point": false}}
```

### lake record — Malloy v. Hogan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Malloy v. Hogan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Malloy v. Hogan",
    "case_name_short": "Malloy",
    "case_name_full": "Malloy v. Hogan, Sheriff",
    "input_case_name": "Malloy v. Hogan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1964-06-15",
    "year": 1964,
    "docket": "110",
    "cluster_id": 106862,
    "lead_opinion_id": 106862,
    "sibling_ids": [
      106862,
      9422839,
      9422840
    ],
    "absolute_url": "/opinion/106862/malloy-v-hogan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "378 U.S. 1",
      "volume": "378",
      "reporter": "U.S.",
      "page": "1",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "84 S. Ct. 1489",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 653",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "653",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1964 U.S. LEXIS 993",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "993",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "378 U.S. 1",
        "volume": "378",
        "reporter": "U.S.",
        "page": "1",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 S. Ct. 1489",
        "volume": "84",
        "reporter": "S. Ct.",
        "page": "1489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "12 L. Ed. 2d 653",
        "volume": "12",
        "reporter": "L. Ed. 2d",
        "page": "653",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1964 U.S. LEXIS 993",
        "volume": "1964",
        "reporter": "U.S. LEXIS",
        "page": "993",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "378 U.S. 1",
    "official_selection": {
      "court_class": "scotus",
      "selected": "378 U.S. 1",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-6",
      "page": null,
      "quote": "--- # Malloy v. Hogan *378 U.S. 1 (1964)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Malloy, on probation for a state gambling misdemeanor, was called before a state inquiry into gambling. He refused to answer questions about his arrest and associates, invoking the privilege against self-incrimination. The Connecticut courts, relying on *Twining v. New Jersey* and *Adamson v. California*, held the privilege did not bind the State, found the questions non-incriminatory, and held him in contempt \u2014 imprisoning him until he answered. He sought habeas corpus. ## Issue Whether the Fifth Amendment privilege against self-incrimination is safeguarded against state action by the Fourteenth Amendment, and by what standard. ## Rule The privilege is incorporated against the States.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-8",
      "page": null,
      "quote": "The Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringement\u2014the right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty . . . for such silence.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-10",
      "page": null,
      "quote": "a 'watered-down, subjective version of the individual guarantees of the Bill of Rights.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1964-06-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Malloy v. Hogan",
    "varies_by_point": false,
    "scope_note": "Foundational incorporation of the Fifth Amendment privilege against the States; good law and the constitutional predicate for Miranda. Overruled Twining and Adamson on this point.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Williams",
          "cluster_id": 10829752,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Deonte WB Ellison",
          "cluster_id": 9372742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8244686,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 8242363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Butler v. State",
          "cluster_id": 7861363,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 9231323,
          "cite": [
            "140 S. Ct. 1390",
            "206 L. Ed. 2d 583"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Vasquez-Santiago",
          "cluster_id": 10133179,
          "cite": [
            "301 Or. App. 90",
            "456 P.3d 270"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jamie Peterson v. David Heymes",
          "cluster_id": 4642776,
          "cite": [
            "931 F.3d 546"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Heffington v. Moser",
          "cluster_id": 4531554,
          "cite": [
            "192 A.3d 900",
            "238 Md. App. 509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane1_negative"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Boykin v. Alabama",
          "cluster_id": 107951,
          "cite": [
            "23 L. Ed. 2d 274",
            "89 S. Ct. 1709",
            "395 U.S. 238",
            "1969 U.S. LEXIS 1434"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "In Re WINSHIP",
          "cluster_id": 108111,
          "cite": [
            "25 L. Ed. 2d 368",
            "90 S. Ct. 1068",
            "397 U.S. 358",
            "1970 U.S. LEXIS 56"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Daniels v. Williams",
          "cluster_id": 111555,
          "cite": [
            "88 L. Ed. 2d 662",
            "106 S. Ct. 662",
            "474 U.S. 327",
            "1986 U.S. LEXIS 43",
            "54 U.S.L.W. 4090"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brady v. United States",
          "cluster_id": 108137,
          "cite": [
            "25 L. Ed. 2d 747",
            "90 S. Ct. 1463",
            "397 U.S. 742",
            "1970 U.S. LEXIS 45"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clewis v. State",
          "cluster_id": 2462780,
          "cite": [
            "922 S.W.2d 126",
            "1996 Tex. Crim. App. LEXIS 11",
            "1996 WL 37908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Furman v. Georgia",
          "cluster_id": 108605,
          "cite": [
            "33 L. Ed. 2d 346",
            "92 S. Ct. 2726",
            "408 U.S. 238",
            "1972 U.S. LEXIS 169"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pointer v. Texas",
          "cluster_id": 107014,
          "cite": [
            "13 L. Ed. 2d 923",
            "85 S. Ct. 1065",
            "380 U.S. 400",
            "1965 U.S. LEXIS 1481"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ashe v. Swenson",
          "cluster_id": 108114,
          "cite": [
            "25 L. Ed. 2d 469",
            "90 S. Ct. 1189",
            "397 U.S. 436",
            "1970 U.S. LEXIS 54"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. California",
          "cluster_id": 107038,
          "cite": [
            "14 L. Ed. 2d 106",
            "85 S. Ct. 1229",
            "380 U.S. 609",
            "1965 U.S. LEXIS 1346"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duncan v. Louisiana",
          "cluster_id": 107685,
          "cite": [
            "20 L. Ed. 2d 491",
            "88 S. Ct. 1444",
            "391 U.S. 145",
            "1968 U.S. LEXIS 1631",
            "45 Ohio Op. 2d 198"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
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
        "journal_ref": "Malloy v. Hogan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106862 OR 9422839 OR 9422840) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTE2MjMzNjAwMDAwJnM9NDQ2MDI4MyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106862+OR+9422839+OR+9422840%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(106862 OR 9422839 OR 9422840)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xOTM0JnM9MTE4MzgwJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106862+OR+9422839+OR+9422840%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106862 OR 9422839 OR 9422840)",
        "reviewed": 79,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 79,
        "triage_read": 1,
        "triage_snippet_classified": 78
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106862 OR 9422839 OR 9422840)",
    "indexed_citing_opinions": 2305,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106862,
        "count": 2083,
        "count_source": "search"
      },
      {
        "opinion_id": 9422839,
        "count": 274,
        "count_source": "search"
      },
      {
        "opinion_id": 9422840,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3675,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/malloy-v-hogan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNzc4NzImcz0xMDM2NzYzOSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28106862+OR+9422839+OR+9422840%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106862,
        "cited_id": 89245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 89309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 89446,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 89675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 92032,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 92834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93208,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93324,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 93930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94410,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 94828,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 95204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 98977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 100708,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 101836,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102601,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102879,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 102991,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103561,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 103981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104455,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104675,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104849,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 104912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105306,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105741,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106109,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106142,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106223,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106240,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106761,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 106803,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 2354861,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 2621051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106862,
        "cited_id": 3321596,
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
    "date_created": "2026-07-05T11:27:51Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:28:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:28:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:31:25Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:28:02Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Malloy v. Hogan

```
<div>
<center><b><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U.S. 1</a></span> (1964)</b></center>
<center><h1>MALLOY<br>
v.<br>
HOGAN, SHERIFF.</h1></center>
<center>No. 110.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 5, 1964.</center>
<center>Decided June 15, 1964.</center>
CERTIORARI TO THE SUPREME COURT OF ERRORS OF CONNECTICUT.
<p><span class="star-pagination">*2</span> <i>Harold Strauch</i> argued the cause and filed a brief for petitioner.</p>
<p><i>John D. LaBelle,</i> State's Attorney for Connecticut, argued the cause for respondent. With him on the brief were <i>George D. Stoughton</i> and <i>Harry W. Hultgren, Jr.,</i> Assistant State's Attorneys.</p>
<p><i>Melvin L. Wulf</i> filed a brief for the American Civil Liberties Union, as <i>amicus curiae,</i> urging reversal.</p>
<p>Briefs of <i>amici curiae,</i> urging affirmance, were filed by <i>Stanley Mosk,</i> Attorney General of California, <i>William E. James,</i> Assistant Attorney General, and <i>Gordon Ringer,</i> Deputy Attorney General, for the State of California; and by <i>Frank S. Hogan, Edward S. Silver, H. Richard Uviller, Michael R. Juviler, Aaron E. Koota</i> and <i>Irving P. Seidman</i> for the National District Attorneys' Association.</p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>In this case we are asked to reconsider prior decisions holding that the privilege against self-incrimination is not safeguarded against state action by the Fourteenth Amendment. <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>; <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>.<sup>[1]</sup></p>
<p><span class="star-pagination">*3</span> The petitioner was arrested during a gambling raid in 1959 by Hartford, Connecticut, police. He pleaded guilty to the crime of pool selling, a misdemeanor, and was sentenced to one year in jail and fined $500. The sentence was ordered to be suspended after 90 days, at which time he was to be placed on probation for two years. About 16 months after his guilty plea, petitioner was ordered to testify before a referee appointed by the Superior Court of Hartford County to conduct an inquiry into alleged gambling and other criminal activities in the county. The petitioner was asked a number of questions related to events surrounding his arrest and conviction. He refused to answer any question "on the grounds it may tend to incriminate me." The Superior Court adjudged him in contempt, and committed him to prison until he was willing to answer the questions. Petitioner's application for a writ of habeas corpus was denied by the Superior Court, and the Connecticut Supreme Court of Errors affirmed. <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">150 Conn. 220</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d 744</a></span>. The latter court held that the Fifth Amendment's privilege against self-incrimination was not available to a witness in a state proceeding, that the Fourteenth Amendment extended no privilege to him, and that the petitioner had not properly invoked the privilege available under the Connecticut Constitution. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./373/948/">373 U. S. 948</a></span>. We reverse. We hold that the Fourteenth Amendment guaranteed the petitioner the protection of the Fifth Amendment's privilege against self-incrimination, and that under the applicable federal standard, the Connecticut Supreme Court of Errors erred in holding that the privilege was not properly invoked.</p>
<p><span class="star-pagination">*4</span> The extent to which the Fourteenth Amendment prevents state invasion of rights enumerated in the first eight Amendments has been considered in numerous cases in this Court since the Amendment's adoption in 1868. Although many Justices have deemed the Amendment to incorporate all eight of the Amendments,<sup>[2]</sup> the view which has thus far prevailed dates from the decision in 1897 in <i>Chicago, B. &amp; Q. R. Co.</i> v. <i>Chicago,</i> <span class="citation" data-id="9417760"><a href="/opinion/94648/chicago-burlington-quincy-railroad-v-chicago/" aria-description="Citation for case: Chicago, Burlington &amp; Quincy Railroad v. Chicago">166 U. S. 226</a></span>, which held that the Due Process Clause requires the States to pay just compensation for private property taken for public use.<sup>[3]</sup> It was on the authority of that decision that the Court said in 1908 in <i>Twining</i> v. <i>New <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Jersey, supra</a></span></i><i>,</i> that "it is possible that some of the personal rights safeguarded by the first eight Amendments <span class="star-pagination">*5</span> against National action may also be safeguarded against state action, because a denial of them would be a denial of due process of law." <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#99" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 99</a></span>.</p>
<p>The Court has not hesitated to re-examine past decisions according the Fourteenth Amendment a less central role in the preservation of basic liberties than that which was contemplated by its Framers when they added the Amendment to our constitutional scheme. Thus, although the Court as late as 1922 said that "neither the Fourteenth Amendment nor any other provision of the Constitution of the United States imposes upon the States any restrictions about `freedom of speech' . . . ," <i>Prudential Ins. Co.</i> v. <i>Cheek,</i> <span class="citation" data-id="100023"><a href="/opinion/100023/prudential-insurance-co-of-america-v-cheek/#543" aria-description="Citation for case: Prudential Insurance Co. of America v. Cheek">259 U. S. 530, 543</a></span>, three years later <i>Gitlow</i> v. <i>New York,</i> <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/" aria-description="Citation for case: Gitlow v. New York">268 U. S. 652</a></span>, initiated a series of decisions which today hold immune from state invasion every First Amendment protection for the cherished rights of mind and spiritthe freedoms of speech, press, religion, assembly, association, and petition for redress of grievances.<sup>[4]</sup></p>
<p>Similarly, <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319</a></span>, decided in 1937, suggested that the rights secured by the Fourth Amendment were not protected against state action, citing, <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#324" aria-description="Citation for case: Palko v. Connecticut">302 U. S., at 324</a></span>, the statement of the Court in 1914 in <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 398</a></span>, that "the Fourth Amendment is not directed to individual misconduct of [state] officials." In 1961, however, the <span class="star-pagination">*6</span> Court held that in the light of later decisions,<sup>[5]</sup> it was taken as settled that ". . . the Fourth Amendment's right of privacy has been declared enforceable against the States through the Due Process Clause of the Fourteenth. . . ." <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 655</a></span>. Again, although the Court held in 1942 that in a state prosecution for a noncapital offense, "appointment of counsel is not a fundamental right," <i>Betts</i> v. <i>Brady,</i> <span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/#471" aria-description="Citation for case: Betts v. Brady">316 U. S. 455, 471</a></span>; cf. <i>Powell</i> v. <i>Alabama,</i> <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>, only last Term this decision was re-examined and it was held that provision of counsel in all criminal cases was "a fundamental right, essential to a fair trial," and thus was made obligatory on the States by the Fourteenth Amendment. <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#343" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 343-344</a></span>.<sup>[6]</sup></p>
<p>We hold today that the Fifth Amendment's exception from compulsory self-incrimination is also protected by the Fourteenth Amendment against abridgment by the States. Decisions of the Court since <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> and <i><span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">Adamson</a></span></i> have departed from the contrary view expressed in those cases. We discuss first the decisions which forbid the use of coerced confessions in state criminal prosecutions.</p>
<p><i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span>, was the first case in which the Court held that the Due Process Clause prohibited the States from using the accused's coerced confessions against him. The Court in <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i> felt impelled, in light of <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> to say that its conclusion did not involve the privilege against self-incrimination. "Compulsion by torture to extort a confession is a different matter." <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S., at 285</a></span>. But this distinction was soon <span class="star-pagination">*7</span> abandoned, and today the admissibility of a confession in a state criminal prosecution is tested by the same standard applied in federal prosecutions since 1897, when, in <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/" aria-description="Citation for case: Bram v. United States">168 U. S. 532</a></span>, the Court held that "[i]n criminal trials, in the courts of the United States, wherever a question arises whether a confession is incompetent because not voluntary, the issue is controlled by that portion of the Fifth Amendment to the Constitution of the United States, commanding that no person `shall be compelled in any criminal case to be a witness against himself.' " <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States"><i>Id.,</i> at 542</a></span>. Under this test, the constitutional inquiry is not whether the conduct of state officers in obtaining the confession was shocking, but whether the confession was "free and voluntary: that is, [it] must not be extracted by any sort of threats or violence, nor obtained by any direct or implied promises, however slight, nor by the exertion of any improper influence. . . ." <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States"><i>Id.,</i> at 542-543</a></span>; see also <i>Hardy</i> v. <i>United States,</i> <span class="citation" data-id="2621051"><a href="/opinion/2621051/hardy-v-united-states/#229" aria-description="Citation for case: Hardy v. United States">186 U. S. 224, 229</a></span>; <i>Wan</i> v. <i>United States,</i> <span class="citation" data-id="100471"><a href="/opinion/100471/ziang-sung-wan-v-united-states/#14" aria-description="Citation for case: Ziang Sung Wan v. United States">266 U. S. 1, 14</a></span>; <i>Smith</i> v. <i>United States,</i> <span class="citation" data-id="105256"><a href="/opinion/105256/smith-v-united-states/#150" aria-description="Citation for case: Smith v. United States">348 U. S. 147, 150</a></span>. In other words the person must not have been compelled to incriminate himself. We have held inadmissible even a confession secured by so mild a whip as the refusal, under certain circumstances, to allow a suspect to call his wife until he confessed. <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>.</p>
<p>The marked shift to the federal standard in state cases began with <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, where the Court spoke of the accused's "free choice to admit, to deny, or to refuse to answer." <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#241" aria-description="Citation for case: Lisenba v. California"><i>Id.,</i> at 241</a></span>. See <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>; <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span>; <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>. The shift reflects recognition that the American system of criminal prosecution is accusatorial, not inquisitorial, and that the Fifth Amendment privilege is its essential mainstay. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>, <span class="star-pagination">*8</span> 541. Governments, state and federal, are thus constitutionally compelled to establish guilt by evidence independently and freely secured, and may not by coercion prove a charge against an accused out of his own mouth. Since the Fourteenth Amendment prohibits the States from inducing a person to confess through "sympathy falsely aroused," <i>Spano</i> v. <i>New York, supra,</i> at 323, or other like inducement far short of "compulsion by torture," <i>Haynes</i> v. <i><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">Washington, supra</a></span></i><i>,</i> it follows <i>a fortiori</i> that it also forbids the States to resort to imprisonment, as here, to compel him to answer questions that might incriminate him. The Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringementthe right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty, as held in <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> for such silence.</p>
<p>This conclusion is fortified by our recent decision in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, overruling <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25</a></span>, which had held "that in a prosecution in a State court for a State crime the Fourteenth Amendment does not forbid the admission of evidence obtained by an unreasonable search and seizure," <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#33" aria-description="Citation for case: Wolf v. Colorado">338 U. S., at 33</a></span>. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> held that the Fifth Amendment privilege against self-incrimination implemented the Fourth Amendment in such cases, and that the two guarantees of personal security conjoined in the Fourteenth Amendment to make the exclusionary rule obligatory upon the States. We relied upon the great case of <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, decided in 1886, which, considering the Fourth and Fifth Amendments as running "almost into each other," <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States"><i>id.,</i> at 630</a></span>, held that "Breaking into a house and opening boxes and drawers are circumstances of aggravation; but any forcible and compulsory extortion of a man's own testimony or of his private papers to be used as evidence to convict him of crime or to forfeit his goods, is within <span class="star-pagination">*9</span> the condemnation of [those Amendments] . . . ." At 630. We said in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>:</i></p>
<blockquote>"We find that, as to the Federal Government, the Fourth and Fifth Amendments and, as to the States, the freedom from unconscionable invasions of privacy and the freedom from convictions based upon coerced confessions do enjoy an `intimate relation' in their perpetuation of `principles of humanity and civil liberty [secured] . . . only after years of struggle,' <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-544</a></span>. . . . The philosophy of each Amendment and of each freedom is complementary to, although not dependent upon, that of the other in its sphere of influencethe very least that together they assure in either sphere is that no man is to be convicted on unconstitutional evidence." <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 656-657</a></span>.</blockquote>
<p>In thus returning to the <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> view that the privilege is one of the "principles of a free government," <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#632" aria-description="Citation for case: Boyd v. United States">116 U. S., at 632</a></span>,<sup>[7]</sup><i>Mapp</i> necessarily repudiated the <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> concept of the privilege as a mere rule of evidence "best defended not as an unchangeable principle of universal justice but as a law proved by experience to be expedient." <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#113" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 113</a></span>.</p>
<p>The respondent Sheriff concedes in his brief that under our decisions, particularly those involving coerced <span class="star-pagination">*10</span> confessions, "the accusatorial system has become a fundamental part of the fabric of our society and, hence, is enforceable against the States."<sup>[8]</sup> The State urges, however, that the availability of the federal privilege to a witness in a state inquiry is to be determined according to a less stringent standard than is applicable in a federal proceeding. We disagree. We have held that the guarantees of the First Amendment, <i>Gitlow</i> v. <i>New York, supra</i><i>; </i><i>Cantwell</i> v. <i>Connecticut,</i> <span class="citation" data-id="103355"><a href="/opinion/103355/cantwell-v-connecticut/" aria-description="Citation for case: Cantwell v. Connecticut">310 U. S. 296</a></span>; <i>Louisiana ex rel. Gremillion</i> v. <i>NAACP,</i> <span class="citation" data-id="9422214"><a href="/opinion/106240/louisiana-ex-rel-gremillion-v-national-assn-for-the-advancement-of/" aria-description="Citation for case: Louisiana Ex Rel. Gremillion v. National Ass&#x27;n for the...">366 U. S. 293</a></span>, the prohibition of unreasonable searches and seizures of the Fourth Amendment, <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, and the right to counsel guaranteed by the Sixth Amendment, <i>Gideon</i> v. <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Wainwright, supra</a></span></i><i>,</i> are all to be enforced against the States under the Fourteenth Amendment according to the same standards that protect those personal rights against federal encroachment. In the coerced confession cases, involving the policies of the privilege itself, there has been no suggestion that a confession might be considered coerced if used in a federal but not a state tribunal. The Court thus has rejected the notion that the Fourteenth Amendment applies to the States only a "watered-down, subjective version of the individual <span class="star-pagination">*11</span> guarantees of the Bill of Rights, "<i>Ohio ex rel. Eaton</i> v. <i>Price,</i> <span class="citation" data-id="106109"><a href="/opinion/106109/ohio-ex-rel-eaton-v-price/#275" aria-description="Citation for case: Ohio Ex Rel. Eaton v. Price">364 U. S. 263, 275</a></span> (dissenting opinion). If <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117</a></span>, and <i>Adamson</i> v. <i>California, supra</i><i>,</i> suggest such an application of the privilege against self-incrimination, that suggestion cannot survive recognition of the degree to which the <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> view of the privilege has been eroded. What is accorded is a privilege of refusing to incriminate one's self, and the feared prosecution may be by either federal or state authorities. <i>Murphy</i> v. <i>Waterfront Comm'n, post,</i> p. 52. It would be incongruous to have different standards determine the validity of a claim of privilege based on the same feared prosecution, depending on whether the claim was asserted in a state or federal court. Therefore, the same standards must determine whether an accused's silence in either a federal or state proceeding is justified.</p>
<p>We turn to the petitioner's claim that the State of Connecticut denied him the protection of his federal privilege. It must be considered irrelevant that the petitioner was a witness in a statutory inquiry and not a defendant in a criminal prosecution, for it has long been settled that the privilege protects witnesses in similar federal inquiries. <i>Counselman</i> v. <i>Hitchcock,</i> <span class="citation" data-id="93234"><a href="/opinion/93234/counselman-v-hitchcock/" aria-description="Citation for case: Counselman v. Hitchcock">142 U. S. 547</a></span>; <i>McCarthy</i> v. <i>Arndstein,</i> <span class="citation" data-id="100474"><a href="/opinion/100474/mccarthy-v-arndstein/" aria-description="Citation for case: McCarthy v. Arndstein">266 U. S. 34</a></span>; <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479</a></span>. We recently elaborated the content of the federal standard in <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman</a></span>:</i></p>
<blockquote>"The privilege afforded not only extends to answers that would in themselves support a conviction . . . but likewise embraces those which would furnish a link in the chain of evidence needed to prosecute . . . . [I]f the witness, upon interposing his claim, were required to prove the hazard . . . he would be compelled to surrender the very protection which the privilege is designed to guarantee. To sustain the privilege, it need only be evident from the implications of the question, in the setting in which it is <span class="star-pagination">*12</span> asked, that a responsive answer to the question or an explanation of why it cannot be answered might be dangerous because injurious disclosure could result." <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S., at 486-487</a></span>.</blockquote>
<p>We also said that, in applying that test, the judge must be</p>
<blockquote>" `<i>perfectly clear,</i> from a careful consideration of all the circumstances in the case, that the witness is mistaken, and that the answer[s] <i>cannot possibly</i> have such tendency' to incriminate." <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#488" aria-description="Citation for case: Hoffman v. United States">341 U. S., at 488</a></span>.</blockquote>
<p>The State of Connecticut argues that the Connecticut courts properly applied the federal standards to the facts of this case. We disagree.</p>
<p>The investigation in the course of which petitioner was questioned began when the Superior Court in Hartford County appointed the Honorable Ernest A. Inglis, formerly Chief Justice of Connecticut, to conduct an inquiry into whether there was reasonable cause to believe that crimes, including gambling, were being committed in Hartford County. Petitioner appeared on January 16 and 25, 1961, and in both instances he was asked substantially the same questions about the circumstances surrounding his arrest and conviction for pool selling in late 1959. The questions which petitioner refused to answer may be summarized as follows: (1) for whom did he work on September 11, 1959; (2) who selected and paid his counsel in connection with his arrest on that date and subsequent conviction; (3) who selected and paid his bondsman; (4) who paid his fine; (5) what was the name of the tenant of the apartment in which he was arrested; and (6) did he know John Bergoti. The Connecticut Supreme Court of Errors ruled that the answers to these questions could not tend to incriminate him because the defenses of double jeopardy and the running of the one-year statute of limitations on misdemeanors would defeat any prosecution growing out of his answers to the first <span class="star-pagination">*13</span> five questions. As for the sixth question, the court held that petitioner's failure to explain how a revelation of his relationship with Bergoti would incriminate him vitiated his claim to the protection of the privilege afforded by state law.</p>
<p>The conclusions of the Court of Errors, tested by the federal standard, fail to take sufficient account of the setting in which the questions were asked. The interrogation was part of a wide-ranging inquiry into crime, including gambling, in Hartford. It was admitted on behalf of the State at oral argumentand indeed it is obvious from the questions themselvesthat the State desired to elicit from the petitioner the identity of the person who ran the pool-selling operation in connection with which he had been arrested in 1959. It was apparent that petitioner might apprehend that if this person were still engaged in unlawful activity, disclosure of his name might furnish a link in a chain of evidence sufficient to connect the petitioner with a more recent crime for which he might still be prosecuted.<sup>[9]</sup></p>
<p>Analysis of the sixth question, concerning whether petitioner knew John Bergoti, yields a similar conclusion. In the context of the inquiry, it should have been apparent to the referee that Bergoti was suspected by the State to be involved in some way in the subject matter of the investigation. An affirmative answer to the question <span class="star-pagination">*14</span> might well have either connected petitioner with a more recent crime, or at least have operated as a waiver of his privilege with reference to his relationship with a possible criminal. See <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="9420532"><a href="/opinion/104849/rogers-v-united-states/" aria-description="Citation for case: Rogers v. United States">340 U. S. 367</a></span>. We conclude, therefore, that as to each of the questions, it was "evident from the implications of the question, in the setting in which it [was] asked, that a responsive answer to the question or an explanation of why it [could not] be answered might be dangerous because injurious disclosure could result," <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S., at 486-487</a></span>; see <i>Singleton</i> v. <i>United States,</i> <span class="citation" data-id="8922391"><a href="/opinion/8932238/singleton-v-united-states/" aria-description="Citation for case: Singleton v. United States">343 U. S. 944</a></span>.</p>
<p><i>Reversed.</i></p>
<p>While MR. JUSTICE DOUGLAS joins the opinion of the Court, he also adheres to his concurrence in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#345" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 345</a></span>.</p>
<p>MR. JUSTICE HARLAN, whom MR. JUSTICE CLARK joins, dissenting.</p>
<p>Connecticut has adjudged this petitioner in contempt for refusing to answer questions in a state inquiry. The courts of the State, whose laws embody a privilege against self-incrimination, refused to recognize the petitioner's claim of privilege, finding that the questions asked him were not incriminatory. This Court now holds the contempt adjudication unconstitutional because, it is decided: (1) the Fourteenth Amendment makes the Fifth Amendment privilege against self-incrimination applicable to the States; (2) the federal standard justifying a claim of this privilege likewise applies to the States; and (3) judged by that standard the petitioner's claim of privilege should have been upheld.</p>
<p>Believing that the reasoning behind the Court's decision carries extremely mischievous, if not dangerous, consequences for our federal system in the realm of criminal <span class="star-pagination">*15</span> law enforcement, I must dissent. The importance of the issue presented and the serious incursion which the Court makes on time-honored, basic constitutional principles justify a full exposition of my reasons.</p>
<p></p>
<h2>I.</h2>
<p>I can only read the Court's opinion as accepting in fact what it rejects in theory: the application to the States, via the Fourteenth Amendment, of the forms of federal criminal procedure embodied within the first eight Amendments to the Constitution. While it is true that the Court deals today with only one aspect of state criminal procedure, and rejects the wholesale "incorporation" of such federal constitutional requirements, the logical gap between the Court's premises and its novel constitutional conclusion can, I submit, be bridged only by the additional premise that the Due Process Clause of the Fourteenth Amendment is a shorthand directive to this Court to pick and choose among the provisions of the first eight Amendments and apply those chosen, freighted with their entire accompanying body of federal doctrine, to law enforcement in the States.</p>
<p>I accept and agree with the proposition that continuing re-examination of the constitutional conception of Fourteenth Amendment "due process" of law is required, and that development of the community's sense of justice may in time lead to expansion of the protection which due process affords. In particular in this case, I agree that principles of justice to which due process gives expression, as reflected in decisions of this Court, prohibit a State, as the Fifth Amendment prohibits the Federal Government, from imprisoning a person <i>solely</i> because he refuses to give evidence which may incriminate him under the laws of the State.<sup>[1]</sup> I do not understand, however, <span class="star-pagination">*16</span> how this process of re-examination, which must refer always to the guiding standard of due process of law, including, of course, reference to the particular guarantees of the Bill of Rights, can be short-circuited by the simple device of incorporating into due process, without critical examination, the whole body of law which surrounds a specific prohibition directed against the Federal Government. The consequence of such an approach to due process as it pertains to the States is inevitably disregard of all relevant differences which may exist between state and federal criminal law and its enforcement. The ultimate result is compelled uniformity, which is inconsistent with the purpose of our federal system and which is achieved either by encroachment on the States' sovereign <span class="star-pagination">*17</span> powers or by dilution in federal law enforcement of the specific protections found in the Bill of Rights.</p>
<p></p>
<h2>II.</h2>
<p>As recently as 1961, this Court reaffirmed that "the Fifth Amendment's privilege against self-incrimination," <i>ante,</i> p. 3, was not applicable against the States. <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117</a></span>. The question had been most fully explored in <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>. Since 1908, when <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> was decided, this Court has adhered to the view there expressed that "the exemption from compulsory self-incrimination in the courts of the States is not secured by any part of the Federal Constitution," <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#114" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 114</a></span>. <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span>; <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 285</a></span>; <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#324" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 324</a></span>; <i>Adamson</i> v. <i>California,</i> <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S. 46</a></span>; <i>Knapp</i> v. <i>Schweitzer,</i> <span class="citation" data-id="9421673"><a href="/opinion/105741/knapp-v-schweitzer/#374" aria-description="Citation for case: Knapp v. Schweitzer">357 U. S. 371, 374</a></span>; <i><span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">Cohen, supra</a></span></i><i>.</i> Although none of these cases involved a commitment to prison for refusing to incriminate oneself under state law, and they are relevantly distinguishable from this case on that narrow ground,<sup>[2]</sup> it is perfectly clear from them that until today it has been regarded as settled law that the <i>Fifth Amendment</i> privilege did not, by any process of reasoning, apply <i>as such</i> to the States.</p>
<p>The Court suggests that this consistent line of authority has been undermined by the concurrent development of constitutional doctrine in the areas of coerced confessions and search and seizure. This is <i>post facto</i> reasoning at best. Certainly there has been no intimation until now that <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> has been tacitly overruled.</p>
<p>It was in <i>Brown</i> v. <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Mississippi, supra</a></span></i><i>,</i> that this Court first prohibited the use of a coerced confession in a state criminal trial. The petitioners in <i><span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">Brown</a></span></i> had been tortured <span class="star-pagination">*18</span> until they confessed. The Court was hardly making an artificial distinction when it said:</p>
<blockquote>". . . [T]he question of the right of the State to withdraw the privilege against self-incrimination is not here involved. The compulsion to which the quoted statements [from <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> and <i><span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/" aria-description="Citation for case: Snyder v. Massachusetts">Snyder, supra,</a></span></i>] refer is that of the <i>processes of justice</i> by which the accused may be called as a witness and required to testify. <i>Compulsion by torture</i> to extort a confession is a different matter."<sup>[3]</sup> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S., at 285</a></span>. (Emphasis supplied.)</blockquote>
<p>The majority is simply wrong when it asserts that this perfectly understandable distinction "was soon abandoned," <i>ante,</i> pp. 6-7. In none of the cases cited, <i>ante,</i> pp. 7-8, in which was developed the full sweep of the constitutional prohibition against the use of coerced confessions at state trials, was there anything to suggest that the Fifth Amendment was being made applicable to state proceedings. In <i>Lisenba</i> v. <i>California,</i> <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/" aria-description="Citation for case: Lisenba v. California">314 U. S. 219</a></span>, the privilege against self-incrimination is not mentioned. The relevant question before the Court was whether "the evidence [of coercion] requires that we set aside the finding of two courts and a jury, and adjudge the admission of the confessions so fundamentally unfair, so contrary to the common concept of ordered liberty, as to amount to a taking of life without due process of law." <span class="citation" data-id="9419181"><a href="/opinion/103561/lisenba-v-california/#238" aria-description="Citation for case: Lisenba v. California"><i>Id.,</i> at 238</a></span>. The question was the same in <i>Ashcraft</i> v. <i>Tennessee,</i> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/" aria-description="Citation for case: Ashcraft v. Tennessee">322 U. S. 143</a></span>; the Court there adverted to the "third degree," <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#150" aria-description="Citation for case: Ashcraft v. Tennessee"><i>e. g., id.,</i> at 150, note 5</a></span>, and "secret inquisitorial practices," <span class="star-pagination">*19</span> <span class="citation" data-id="9419494"><a href="/opinion/103981/ashcraft-v-tennessee/#152" aria-description="Citation for case: Ashcraft v. Tennessee"><i>id.,</i> at 152</a></span>. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span>, is the same; the privilege against self-incrimination is not mentioned.<sup>[4]</sup> So too in <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/" aria-description="Citation for case: Spano v. New York">360 U. S. 315</a></span>; <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528</a></span>; and <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503</a></span>. Finally, in <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span>, although the Court did recognize that "ours is an accusatorial and not an inquisitorial system," <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#541" aria-description="Citation for case: Rogers v. Richmond"><i>id.,</i> at 541</a></span>, it is clear that the Court was concerned only with the problem of coerced confessions, see <i>ibid.;</i> the opinion includes nothing to support the Court's assertion here, <i>ante,</i> p. 7, that "the Fifth Amendment privilege is . . . [the] essential mainstay" of our system.</p>
<p>In <i><span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">Adamson, supra,</a></span></i> the Court made it explicit that it did not regard the increasingly strict standard for determining the admissibility at trial of an out-of-court confession as undermining the holding of <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>.</i> After stating that "the due process clause does not protect, by virtue of its mere existence, the accused's freedom from giving testimony by compulsion in state trials that is secured to him against federal interference by the Fifth Amendment," the Court said: "The due process clause forbids compulsion to testify by fear of hurt, torture or exhaustion. It forbids any other type of coercion that falls within the scope of due process." <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">332 U. S., at 54</a></span> <span class="star-pagination">*20</span> (footnotes omitted). Plainly, the Court regarded these two lines of cases as distinct. See also <i>Palko</i> v. <i>Connecticut, supra,</i> at 326, to the same effect.<sup>[5]</sup><i><span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/" aria-description="Citation for case: Cohen v. Hurley">Cohen, supra,</a></span></i> which adhered to <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> was decided after all but a few of the confession cases which the Court mentions.</p>
<p>The coerced confession cases are relevant to the problem of this case not because they overruled <i>Twining sub silentio,</i> but rather because they applied the same standard of fundamental fairness which is applicable here. The recognition in them that federal supervision of state criminal procedures must be directly based on the requirements of due process is entirely inconsistent with the theory here espoused by the majority. The parallel treatment of federal and state cases involving coerced confessions resulted from the fact that the same demand of due process was applicable in both; it was not the consequence of the automatic engrafting of federal law construing constitutional provisions inapplicable to the States onto the Fourteenth Amendment.</p>
<p>The decision in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, that evidence unconstitutionally seized, see <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#28" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 28</a></span>, may not be used in a state criminal trial furnishes no "fortification," see <i>ante,</i> p. 8, for today's decision. The very passage from the <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> opinion which the Court quotes, <i>ante,</i> p. 9, makes explicit the distinct bases of the exclusionary rule as applied in federal and state courts:</p>
<blockquote>"We find that, as to the Federal Government, the Fourth and Fifth Amendments and, as to the States, the freedom from unconscionable invasions of privacy and the freedom from convictions based upon coerced confessions do enjoy an `intimate relation' <span class="star-pagination">*21</span> in their perpetuation of `principles of humanity and civil liberty [secured] . . . only after years of struggle,' <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#543" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 543-544</a></span> (1897)." <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#656" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 656-657</a></span> (footnote omitted). See also <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#655" aria-description="Citation for case: Mapp v. Ohio"><i>id.,</i> at 655</a></span>.</blockquote>
<p>Although the Court discussed <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">116 U. S. 616</a></span>, a federal case involving both the Fourth and Fifth Amendments, nothing in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> supports the statement, <i>ante,</i> p. 8, that the Fifth Amendment was part of the basis for extending the exclusionary rule to the States. The elaboration of <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span></i> in <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span>, did in my view make the Fourth Amendment applicable to the States through the Fourteenth; but there is nothing in it to suggest that the Fifth Amendment went along as baggage.</p>
<p></p>
<h2>III.</h2>
<p>The previous discussion shows that this Court's decisions do not dictate the "incorporation" of the Fifth Amendment's privilege against self-incrimination into the Fourteenth Amendment. Approaching the question more broadly, it is equally plain that the line of cases exemplified by <i>Palko</i> v. <i>Connecticut, supra</i><i>,</i> in which this Court has reconsidered the requirements which the Due Process Clause imposes on the States in the light of current standards, furnishes no general theoretical framework for what the Court does today.</p>
<p>The view of the Due Process Clause of the Fourteenth Amendment which this Court has consistently accepted and which has "thus far prevailed," <i>ante,</i> p. 4, is that its requirements are as "old as a principle of civilized government," <i>Munn</i> v. <i>Illinois,</i> <span class="citation" data-id="9417073"><a href="/opinion/89446/munn-v-illinois/#123" aria-description="Citation for case: Munn v. Illinois">94 U. S. 113, 123</a></span>, the specific applications of which must be ascertained "by the gradual process of judicial inclusion and exclusion . . . ," <i>Davidson</i> v. <i>New Orleans,</i> <span class="citation" data-id="9841711"><a href="/opinion/89675/davidson-v-new-orleans/#104" aria-description="Citation for case: Davidson v. New Orleans">96 U. S. 97, 104</a></span>. Due process requires "observance of those general rules established in our system of jurisprudence for the security of private <span class="star-pagination">*22</span> rights." <i>Hagar</i> v. <i>Reclamation District No. 108,</i> <span class="citation" data-id="91153"><a href="/opinion/91153/hagar-v-reclamation-district-no-108/#708" aria-description="Citation for case: Hagar v. Reclamation District No. 108">111 U. S. 701, 708</a></span>. See <i>Hurtado</i> v. <i>California,</i> <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/#537" aria-description="Citation for case: Hurtado v. California">110 U. S. 516, 537</a></span>.</p>
<blockquote>"This court has never attempted to define with precision the words `due process of law' . . . . It is sufficient to say that there are certain immutable principles of justice which inhere in the very idea of free government which no member of the Union may disregard . . . ." <i>Holden</i> v. <i>Hardy,</i> <span class="citation" data-id="94828"><a href="/opinion/94828/holden-v-hardy/#389" aria-description="Citation for case: Holden v. Hardy">169 U. S. 366, 389</a></span>.</blockquote>
<p>It followed from this recognition that due process encompassed the fundamental safeguards of the individual against the abusive exercise of governmental power that some of the restraints on the Federal Government which were specifically enumerated in the Bill of Rights applied also against the States. But, while inclusion of a particular provision in the Bill of Rights might provide historical evidence that the right involved was traditionally regarded as fundamental, inclusion of the right in due process was otherwise entirely independent of the first eight Amendments:</p>
<blockquote>". . . [I]t is possible that some of the personal rights safeguarded by the first eight Amendments against National action may also be safeguarded against state action, because a denial of them would be a denial of due process of law. . . . <i>If this is so, it is not because those rights are enumerated in the first eight Amendments, but because they are of such a nature that they are included in the conception of due process of law.</i>" <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#99" aria-description="Citation for case: Twining v. New Jersey"><i>Twining, supra,</i> at 99</a></span>. (Emphasis supplied.)</blockquote>
<p>Relying heavily on <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span>,</i> Mr. Justice Cardozo provided what may be regarded as a classic expression of this approach in <i>Palko</i> v. <i>Connecticut, supra</i><i>.</i> After considering a number of individual rights (including the right <span class="star-pagination">*23</span> not to incriminate oneself) which were "not of the very essence of a scheme of ordered liberty," <i>id.,</i> at 325, he said:</p>
<blockquote>"We reach a different plane of social and moral values when we pass to the privileges and immunities that have been taken over from the earlier articles of the federal bill of rights and brought within the Fourteenth Amendment by a process of absorption. These in their origin were effective against the federal government alone. If the Fourteenth Amendment has absorbed them, the process of absorption has had its source in the belief that neither liberty nor justice would exist if they were sacrificed." <i>Id.,</i> at 326.</blockquote>
<p>Further on, Mr. Justice Cardozo made the independence of the Due Process Clause from the provisions of the first eight Amendments explicit:</p>
<blockquote>"Fundamental . . . in the concept of due process, and so in that of liberty, is the thought that condemnation shall be rendered only after trial. <i>Scott</i> v. <i>McNeal,</i> <span class="citation" data-id="93930"><a href="/opinion/93930/scott-v-mcneal/" aria-description="Citation for case: Scott v. McNeal">154 U. S. 34</a></span>; <i>Blackmer</i> v. <i>United States,</i> <span class="citation" data-id="101836"><a href="/opinion/101836/blackmer-v-united-states/" aria-description="Citation for case: Blackmer v. United States">284 U. S. 421</a></span>. The hearing, moreover, must be a real one, not a sham or a pretense. <i>Moore</i> v. <i>Dempsey,</i> <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86</a></span>; <i>Mooney</i> v. <i>Holohan,</i> <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103</a></span>. For that reason, ignorant defendants in a capital case were held to have been condemned unlawfully when in truth, though not in form, they were refused the aid of counsel. <i>Powell</i> v. <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/#67" aria-description="Citation for case: Powell v. Alabama"><i>Alabama, supra,</i> pp. 67, 68</a></span>. The decision did not turn upon the fact that the benefit of counsel would have been guaranteed to the defendants by the provisions of the Sixth Amendment if they had been prosecuted in a federal court. The decision turned upon the fact that in the particular situation laid before us in the evidence the benefit of counsel was essential to the substance of a hearing." <i>Id.,</i> at 327.</blockquote>
<p><span class="star-pagination">*24</span> It is apparent that Mr. Justice Cardozo's metaphor of "absorption" was <i>not</i> intended to suggest the transplantation of case law surrounding the specifics of the first eight Amendments to the very different soil of the Fourteenth Amendment's Due Process Clause. For, as he made perfectly plain, what the Fourteenth Amendment requires of the States does not basically depend on what the first eight Amendments require of the Federal Government.</p>
<p>Seen in proper perspective, therefore, the fact that First Amendment protections have generally been given equal scope in the federal and state domains or that in some areas of criminal procedure the Due Process Clause demands as much of the States as the Bill of Rights demands of the Federal Government, is only tangentially relevant to the question now before us. It is toying with constitutional principles to assert that the Court has "rejected the notion that the Fourteenth Amendment applies to the states only a `watered-down, subjective version of the individual guarantees of the Bill of Rights,' " <i>ante,</i> pp. 10-11. What the Court has, with the single exception of the <i><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">Ker</a></span></i> case, <i>supra,</i> p. 21; see <i>infra,</i> p. 26, consistently rejected is the notion that the Bill of Rights, as such, applies to the States in any aspect at all.</p>
<p>If one attends to those areas to which the Court points, <i>ante,</i> p. 10, in which the prohibitions against the state and federal governments have moved in parallel tracks, the cases in fact reveal again that the Court's usual approach has been to ground the prohibitions against state action squarely on due process, without intermediate reliance on any of the first eight Amendments. Although more recently the Court has referred to the First Amendment to describe the protection of free expression against state infringement, earlier cases leave no doubt that such references are "shorthand" for doctrines developed by another <span class="star-pagination">*25</span> route. In <i>Gitlow</i> v. <i>New York,</i> <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/#666" aria-description="Citation for case: Gitlow v. New York">268 U. S. 652, 666</a></span>, for example, the Court said:</p>
<blockquote>"For present purposes we may and do assume that freedom of speech and of the presswhich are protected by the First Amendment from abridgment by Congressare among the fundamental personal rights and `liberties' protected by the due process clause of the Fourteenth Amendment from impairment by the States."</blockquote>
<p>The Court went on to consider the extent of those freedoms in the context of state interests. Mr. Justice Holmes, in dissent, said:</p>
<blockquote>"The general principle of free speech, it seems to me, must be taken to be included in the Fourteenth Amendment, in view of the scope that has been given to the word `liberty' as there used, although perhaps it may be accepted with a somewhat larger latitude of interpretation than is allowed to Congress by the sweeping language that governs or ought to govern the laws of the United States." <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/#672" aria-description="Citation for case: Gitlow v. New York"><i>Id.,</i> at 672</a></span>.</blockquote>
<p>Chief Justice Hughes, in <i>De Jonge</i> v. <i>Oregon,</i> <span class="citation" data-id="102728"><a href="/opinion/102728/de-jonge-v-oregon/#364" aria-description="Citation for case: De Jonge v. Oregon">299 U. S. 353, 364</a></span>, gave a similar analysis:</p>
<blockquote>"Freedom of speech and of the press are fundamental rights which are safeguarded by the due process clause of the Fourteenth Amendment of the Federal Constitution. . . . The right of peaceable assembly is a right cognate to those of free speech and free press and is equally fundamental. As this Court said in <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542</a></span>, 552: `The very idea of a government, republican in form, implies a right on the part of its citizens to meet peaceably for consultation in respect to public affairs and to petition for a redress of grievances.' The First Amendment of the Federal Constitution expressly guarantees that right against abridgment <span class="star-pagination">*26</span> by Congress. But explicit mention there does not argue exclusion elsewhere. For the right is one that cannot be denied without violating those fundamental principles of liberty and justice which lie at the base of all civil and political institutions,principles which the Fourteenth Amendment embodies in the general terms of its due process clause."</blockquote>
<p>The coerced confession and search and seizure cases have already been considered. The former, decided always directly on grounds of fundamental fairness, furnish no support for the Court's present views. <i>Ker</i> v. <i>California, supra</i><i>,</i> did indeed incorporate the Fourth Amendment's protection against invasions of privacy into the Due Process Clause. But that case should be regarded as the exception which proves the rule.<sup>[6]</sup> The right to counsel in state criminal proceedings, which this Court assured in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span>, does not depend on the Sixth Amendment. In <i>Betts</i> v. <i>Brady,</i> <span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/#462" aria-description="Citation for case: Betts v. Brady">316 U. S. 455, 462</a></span>, this Court had said:</p>
<blockquote>"Due process of law is secured against invasion by the federal Government by the Fifth Amendment, and is safeguarded against state action in identical words by the Fourteenth. The phrase formulates a concept less rigid and more fluid than those envisaged in other specific and particular provisions of the Bill of Rights. Its application is less a matter of rule. Asserted denial is to be tested by an appraisal of the totality of facts in a given case. That which may, in one setting, constitute a denial of fundamental fairness, shocking to the universal sense of justice, may, in other circumstances, and in the light of other considerations, fall short of such denial." (Footnote omitted.)</blockquote>
<p><span class="star-pagination">*27</span> Although <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Gideon</a></span></i> overruled <i><span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/" aria-description="Citation for case: Betts v. Brady">Betts</a></span>,</i> the constitutional approach in both cases was the same. <i><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">Gideon</a></span></i> was based on the Court's conclusion, contrary to that reached in <i><span class="citation" data-id="103694"><a href="/opinion/103694/betts-v-brady/" aria-description="Citation for case: Betts v. Brady">Betts</a></span>,</i> that the appointment of counsel for an indigent criminal defendant <i>was</i> essential to the conduct of a fair trial, and was therefore part of due process. 372 U. S., at 342-345.</p>
<p>The Court's approach in the present case is in fact nothing more or less than "incorporation" in snatches. If, however, the Due Process Clause <i>is</i> something more than a reference to the Bill of Rights and protects only those rights which derive from fundamental principles, as the majority purports to believe, it is just as contrary to precedent and just as illogical to incorporate the provisions of the Bill of Rights one at a time as it is to incorporate them all at once.</p>
<p></p>
<h2>IV.</h2>
<p>The Court's undiscriminating approach to the Due Process Clause carries serious implications for the sound working of our federal system in the field of criminal law.</p>
<p>The Court concludes, almost without discussion, that "the same standards must determine whether an accused's silence in either a federal or state proceeding is justified," <i>ante,</i> p. 11. About all that the Court offers in explanation of this conclusion is the observation that it would be "incongruous" if different standards governed the assertion of a privilege to remain silent in state and federal tribunals. Such "incongruity," however, is at the heart of our federal system. The powers and responsibilities of the state and federal governments are not congruent; under our Constitution, they are not intended to be. Why should it be thought, as an <i>a priori</i> matter, that limitations on the investigative power of the States are in all respects identical with limitations on the investigative power of the Federal Government? This certainly <span class="star-pagination">*28</span> does not follow from the fact that we deal here with constitutional requirements; for the provisions of the Constitution which are construed are different.</p>
<p>As the Court pointed out in <i>Abbate</i> v. <i>United States,</i> <span class="citation" data-id="9421783"><a href="/opinion/105860/abbate-v-united-states/#195" aria-description="Citation for case: Abbate v. United States">359 U. S. 187, 195</a></span>, "the States under our federal system have the principal responsibility for defining and prosecuting crimes." The Court endangers this allocation of responsibility for the prevention of crime when it applies to the States doctrines developed in the context of federal law enforcement, without any attention to the special problems which the States as a group or particular States may face. If the power of the States to deal with local crime is unduly restricted, the likely consequence is a shift of responsibility in this area to the Federal Government, with its vastly greater resources. Such a shift, if it occurs, may in the end serve to weaken the very liberties which the Fourteenth Amendment safeguards by bringing us closer to the monolithic society which our federalism rejects. Equally dangerous to our liberties is the alternative of watering down protections against the Federal Government embodied in the Bill of Rights so as not unduly to restrict the powers of the States. The dissenting opinion in <i>Aguilar</i> v. <i>Texas, post,</i> p. 116, evidences that this danger is not imaginary. See my concurring opinion in <i>Aguilar, <span class="citation" data-id="9421783"><a href="/opinion/105860/abbate-v-united-states/" aria-description="Citation for case: Abbate v. United States">ibid.</a></span></i></p>
<p>Rather than insisting, almost by rote, that the Connecticut court, in considering the petitioner's claim of privilege, was required to apply the "federal standard," the Court should have fulfilled its responsibility under the Due Process Clause by inquiring whether the proceedings below met the demands of fundamental fairness which due process embodies. Such an approach may not satisfy those who see in the Fourteenth Amendment a set of easily applied "absolutes" which can afford a haven from unsettling doubt. It is, however, truer to the spirit which requires this Court constantly to re-examine fundamental <span class="star-pagination">*29</span> principles and at the same time enjoins it from reading its own preferences into the Constitution.</p>
<p>The Connecticut Supreme Court of Errors gave full and careful consideration to the petitioner's claim that he would incriminate himself if he answered the questions put to him. It noted that its decisions "from a time antedating the adoption of . . . [the Connecticut] constitution in 1818" had upheld a privilege to refuse to answer incriminating questions. <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#223" aria-description="Citation for case: Malloy v. Hogan">150 Conn. 220, 223</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#746" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d 744, 746</a></span>. Stating that federal cases treating the Fifth Amendment privilege had "persuasive force" in interpreting its own constitutional provision, and citing <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479</a></span>, in particular, the Supreme Court of Errors described the requirements for assertion of the privilege by quoting from one of its own cases, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#225" aria-description="Citation for case: Malloy v. Hogan">150 Conn., at 225</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 747</a></span>:</p>
<blockquote>"[A] witness . . . has the right to refuse to answer any question which would tend to incriminate him. But a mere claim on his part that the evidence will tend to incriminate him is not sufficient. . . . [He having] made his claim, it is then . . . [necessary for the judge] to determine in the exercise of a legal discretion whether, from the circumstances of the case and the nature of the evidence which the witness is called upon to give, there is reasonable ground to apprehend danger of criminal liability from his being compelled to answer. That danger `must be real and appreciable, with reference to the ordinary operation of law in the ordinary course of things not a danger of an imaginary and unsubstantial character, having reference to some extraordinary and barely possible contingency, so improbable that no reasonable man would suffer it to influence his conduct. We think that a merely remote and naked possibility, out of the ordinary course of law and such as no reasonable man would be affected by, <span class="star-pagination">*30</span> should not be suffered to obstruct the administration of justice. The object of the law is to afford to a party, called upon to give evidence in a proceeding <i>inter alios,</i> protection against being brought by means of his own evidence within the penalties of the law. But it would be to convert a salutary protection into a means of abuse if it were to be held that a mere imaginary possibility of danger, however remote and improbable, was sufficient to justify the withholding of evidence essential to the ends of justice.' Cockburn, C. J., in <i>Regina</i> v. <i>Boyes,</i> 1 B. &amp; S. 311, 330 . . . ." <i>McCarthy</i> v. <i>Clancy,</i> <span class="citation" data-id="3321596"><a href="/opinion/3326204/mccarthy-v-clancy/#488" aria-description="Citation for case: McCarthy v. Clancy">110 Conn. 482, 488-489</a></span>, <span class="citation" data-id="3321596"><a href="/opinion/3326204/mccarthy-v-clancy/#555" aria-description="Citation for case: McCarthy v. Clancy">148 A. 551, 555</a></span>.</blockquote>
<p>The court carefully applied the above standard to each question which the petitioner was asked. It dealt first with the question whether he knew John Bergoti. The court said:</p>
<blockquote>"Bergoti is nowhere described or in any way identified, either as to his occupation, actual or reputed, or as to any criminal record he may have had. . . . Malloy made no attempt even to suggest to the court how an answer to the question whether he knew Bergoti could possibly incriminate him. . . . On this state of the record the question was proper, and Malloy's claim of privilege, made without explanation, was correctly overruled. Malloy 'chose to keep the door tightly closed and to deny the court the smallest glimpse of the danger he apprehended. He cannot then complain that we see none.' <i>In re Pillo,</i> 11 N. J. 8, 22, <span class="citation" data-id="2335877"><a href="/opinion/2335877/in-re-pillo/" aria-description="Citation for case: In Re Pillo">93 A. 2d 176</a></span> . . . ." <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#226" aria-description="Citation for case: Malloy v. Hogan">150 Conn., at 226-227</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#748" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 748</a></span>.</blockquote>
<p>The remaining questions are summarized in the majority's opinion, <i>ante,</i> p. 12. All of them deal with the circumstances surrounding the petitioner's conviction on a gambling charge in 1959. The court declined to decide <span class="star-pagination">*31</span> "whether, on their face and apart from any consideration of Malloy's immunity from prosecution, the questions should or should not have been answered in the light of his failure to give any hint of explanation as to how answers to them could incriminate him." <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#227" aria-description="Citation for case: Malloy v. Hogan">150 Conn., at 227</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#748" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 748</a></span>. The court considered the State's claim that the petitioner's prior conviction was sufficient to clothe him with immunity from prosecution for other crimes to which the questions might pertain, but declined to rest its decision on that basis. <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#227" aria-description="Citation for case: Malloy v. Hogan"><i>Id.,</i> at 227-229</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#748" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 748-749</a></span>. The court concluded, however, that the running of the statute of limitations on misdemeanors committed in 1959 and the absence of any indication that Malloy had engaged in any crime other than a misdemeanor removed all appearance of danger of incrimination from the questions propounded concerning the petitioner's activities in 1959. The court summarized this conclusion as follows:</p>
<blockquote>"In all this, Malloy confounds vague and improbable possibilities of prosecution with reasonably appreciable ones. Under claims like his, it would always be possible to work out some finespun and improbable theory from which an outside chance of prosecution could be envisioned. Such claims are not enough to support a claim of privilege, at least where, as here, a witness suggests no rational explanation of his fears of incrimination, and the questions themselves, under all the circumstances, suggest none." <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#230" aria-description="Citation for case: Malloy v. Hogan"><i>Id.,</i> at 230-231</a></span>, <span class="citation" data-id="2354861"><a href="/opinion/2354861/malloy-v-hogan/#750" aria-description="Citation for case: Malloy v. Hogan">187 A. 2d, at 750</a></span>.</blockquote>
<p>Peremptorily rejecting all of the careful analysis of the Connecticut court, this Court creates its own "finespun and improbable theory" about how these questions might have incriminated the petitioner. With respect to his acquaintance with Bergoti, this Court says only:</p>
<blockquote>"In the context of the inquiry, it should have been apparent to the referee that Bergoti was suspected <span class="star-pagination">*32</span> by the State to be involved in some way in the subject matter of the investigation. An affirmative answer to the question might well have either connected petitioner with a more recent crime, or at least have operated as a waiver of his privilege with reference to his relationship with a possible criminal." <i>Ante,</i> pp. 13-14.</blockquote>
<p>The other five questions, treated at length in the Connecticut court's opinion, get equally short shrift from this Court; it takes the majority, unfamiliar with Connecticut law and far removed from the proceedings below, only a dozen lines to consider the questions and conclude that they were incriminating:</p>
<blockquote>"The interrogation was part of a wide-ranging inquiry into crime, including gambling, in Hartford. It was admitted on behalf of the State at oral argument and indeed it is obvious from the questions themselvesthat the State desired to elicit from the petitioner the identity of the person who ran the pool-selling operation in connection with which he had been arrested in 1959. It was apparent that petitioner might apprehend that if this person were still engaged in unlawful activity, disclosure of his name might furnish a link in a chain of evidence sufficient to connect the petitioner with a more recent crime for which he might still be prosecuted." (Footnote omitted.) <i>Ante,</i> p. 13.</blockquote>
<p>I do not understand how anyone could read the opinion of the Connecticut court and conclude that the state law which was the basis of its decision or the decision itself was lacking in fundamental fairness. The truth of the matter is that under any standardstate or federalthe commitment for contempt was proper. Indeed, as indicated above, there is every reason to believe that the Connecticut court did apply the <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman</a></span></i> standard <span class="star-pagination">*33</span> quoted approvingly in the majority's opinion. I entirely agree with my Brother WHITE, <i>post,</i> pp. 36-38, that if the matter is viewed only from the standpoint of the federal standard, such standard was fully satisfied. The Court's reference to a federal standard is, to put it bluntly, simply an excuse for the Court to substitute its own superficial assessment of the facts and state law for the careful and better informed conclusions of the state court. No one who scans the two opinions with an objective eye will, I think, reach any other conclusion.</p>
<p>I would affirm.</p>
<p>MR. JUSTICE WHITE, with whom MR. JUSTICE STEWART joins, dissenting.</p>
<p></p>
<h2>I.</h2>
<p>The Fifth Amendment safeguards an important complex of values, but it is difficult for me to perceive how these values are served by the Court's holding that the privilege was properly invoked in this case. While purporting to apply the prevailing federal standard of incrimination the same standard of incrimination that the Connecticut courts appliedthe Court has all but stated that a witness' invocation of the privilege to any question is to be automatically, and without more, accepted. With deference, I prefer the rule permitting the judge rather than the witness to determine when an answer sought is incriminating.</p>
<p>The established rule has been that the witness' claim of the privilege is not final, for the privilege qualifies a citizen's general duty of disclosure only when his answers would subject him to danger from the criminal law. The privilege against self-incrimination or any other evidentiary privilege does not protect silence which is solely an expression of political protest, a desire not to inform, a fear of social obloquy or economic disadvantage or fear of prosecution for future crimes. <i>Smith</i> v. <i>United States,</i> <span class="star-pagination">*34</span> <span class="citation" data-id="104675"><a href="/opinion/104675/smith-v-united-states/#147" aria-description="Citation for case: Smith v. United States">337 U. S. 137, 147</a></span>; <i>Brown</i> v. <i>Walker,</i> <span class="citation" data-id="9417708"><a href="/opinion/94410/brown-v-walker/#605" aria-description="Citation for case: Brown v. Walker">161 U. S. 591, 605</a></span>. If the general duty to testify when subpoenaed is to remain and the privilege is to be retained as a protection against compelled incriminating answers, the trial judge must be permitted to make a meaningful determination of when answers tend to incriminate. See <i>The Queen</i> v. <i>Boyes,</i> 1 B. &amp; S. 311, 329-330 (1861); <i>Mason</i> v. <i>United States,</i> <span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">244 U. S. 362</a></span>. I do not think today's decision permits such a determination.</p>
<p>Answers which would furnish a lead to other evidence needed to prosecute or convict a claimant of a crime clue evidencecannot be compelled, but "this protection must be confined to instances where the witness has reasonable cause to apprehend danger from a direct answer." <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/#486" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479, at 486</a></span>; <i>Mason</i> v. <i>United States,</i> <span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">244 U. S. 362</a></span>. Of course the witness is not required to disclose so much of the danger as to render his privilege nugatory. But that does not justify a flat rule of no inquiry and automatic acceptance of the claim of privilege. In determining whether the witness has a reasonable apprehension, the test in the federal courts has been that the judge is to decide from the circumstances of the case, his knowledge of matters surrounding the inquiry and the nature of the evidence which is demanded from the witness. <i>Hoffman</i> v. <i>United States,</i> <span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">341 U. S. 479</a></span>; <i>Mason</i> v. <i>United States,</i> <span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">244 U. S. 362</a></span>. Cf. <i>Rogers</i> v. <i>United States,</i> <span class="citation" data-id="9420532"><a href="/opinion/104849/rogers-v-united-states/" aria-description="Citation for case: Rogers v. United States">340 U. S. 367</a></span>. This rule seeks and achieves a workable accommodation between what are obviously important competing interests. As Mr. Chief Justice Marshall said: "The principle which entitles the United States to the testimony of every citizen, and the principle by which every witness is privileged not to accuse himself, can neither of them be entirely disregarded. . . . When a question is propounded, it belongs to the court to consider and to decide whether any direct answer to it can implicate the witness." <i>In</i> <span class="star-pagination">*35</span> <i>re Willie,</i> 25 Fed. Cas. No. 14,692e, at 39-40. I would not only retain this rule but apply it in its present form. Under this test, Malloy's refusals to answer some, if not all, of the questions put to him were clearly not privileged.</p>
<p></p>
<h2>II.</h2>
<p>In November 1959, Malloy was arrested in a gambling raid in Hartford and was convicted of pool selling, an offense defined as occupying and keeping a building containing gambling apparatus. After a 90-day jail term, his one-year sentence was suspended and Malloy was placed on probation for two years. In early 1961, Malloy was summoned to appear in an investigation into whether crimes, including gambling, had been committed in Hartford County, and was asked various questions obviously and solely designed to ascertain who Malloy's associates were in connection with his pool-selling activities in Hartford in 1959. Malloy initially refused to answer virtually all the questions put to him, including such innocuous ones as whether he was the William Malloy arrested and convicted of pool selling in 1959. After he was advised to consult with counsel and did so, he declined to answer each one of the following questions on the ground that it would tend to incriminate him:</p>
<blockquote>"Q. Now, on September 11, 1959, when you were arrested at 600 Asylum Street, and the same arrest for which you were convicted in the Superior Court on November 5, 1959, for whom were you working?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. On September 11, 1959, when you were arrested, and the same arrest for which you were convicted in the Superior Court on November 5, 1959, who furnished the money to pay your fine when you were convicted in the Superior Court?</blockquote>
<blockquote>.....</blockquote>
<blockquote>
<span class="star-pagination">*36</span> "Q. After your arrest on September 11, 1959, and the same arrest for which you were convicted on November 5, 1959, who selected your bondsman?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. As a result of your arrest on September 11, 1959, and the same arrest for which you were convicted on November 5, 1959, who furnished the money to pay your fine?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Do you know whose apartment it was [that you were arrested in on September 11, 1959]?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. Do you know John Bergoti?</blockquote>
<blockquote>.....</blockquote>
<blockquote>"Q. I ask you again, Mr. Malloy, now, so there will be no misunderstanding of what I want to know. When you were arrested on September 11, 1959, at 600 Asylum Street in Hartford, and the same arrest for which you were convicted in Superior Court on November 5, 1959, for whom were you working?"</blockquote>
<p>It was for refusing to answer these questions that Malloy was cited for contempt, the Connecticut courts noting that the privilege does not protect one against informing on friends or associates.</p>
<p>These were not wholly innocuous questions on their face, but they clearly were in light of the finding, of which Malloy was told, that he was immune from prosecution for any pool-selling activities in 1959. As the Connecticut Supreme Court of Errors found, the State bore its burden of proving that the statute of limitations barred any prosecution for any type of violation of the state pool-selling statute in 1959. Malloy advanced the claim before the Connecticut courts, and again before this Court, that he could perhaps be prosecuted for a conspiracy and that the statute of limitations on a felony was <span class="star-pagination">*37</span> five years. But the Connecticut courts were unable to find any state statute which Malloy's gambling activities in 1959 in Hartford, the subject of the inquiry, could have violated and Malloy has not yet pointed to one. Beyond this Malloy declined to offer any explanation or hint at how the answers sought could have incriminated him. In these circumstances it is wholly speculative to find that the questions about others, not Malloy, posed a substantial hazard of criminal prosecution to Malloy. Theoretically, under some unknown but perhaps possible conditions any fact is potentially incriminating. But if this be the rule, there obviously is no reason for the judge, rather than the witness, to pass on the claim of privilege. The privilege becomes a general one against answering distasteful questions.</p>
<p>The Court finds that the questions were incriminating because petitioner "might apprehend that if [his associates in 1959] were still engaged in unlawful activity, disclosure of [their names] might furnish a link in a chain of evidence sufficient to connect the petitioner with a more recent crime for which he might still be prosecuted." <i>Ante,</i> p. 13. The assumption necessary to the above reasoning is that all persons, or all who have committed a misdemeanor, are continuously engaged in crime. This is but another way of making the claim of privilege automatic. It is not only unrealistic generally but peculiarly inappropriate in this case. Unlike cases relied on by the Court, like <i>Hoffman</i> v. <i>United States, supra</i><i>,</i> where the claimant was known to be involved in rackets in the area, which were the subject of the inquiry, and had a "broadly published police record," Malloy had no record as a felon. He had engaged once in an unlawful activitypool sellinga misdemeanor and was given a suspended sentence. He had been on probation since that time and was on probation at the time of the inquiry. Again, unlike <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman</a></span>,</i> nothing in these questions indicates petitioner <span class="star-pagination">*38</span> was called because he was suspected of criminal activities after 1959. There is no support at all in this record for the cynical assumption that he had committed criminal acts after his release in 1960.</p>
<p>Even on the Court's assumption that persons convicted of a misdemeanor are necessarily suspect criminals, sustaining the privilege in these circumstances is unwarranted, for Malloy placed no reliance on this theory in the courts below or in this Court. In order to allow the judge passing on the claim to understand how the answers sought are incriminating, I would at least require the claimant to state his grounds for asserting the privilege to questions seemingly irrelevant to any incriminating matters.</p>
<p>Adherence to the federal standard of incrimination stated in <i><span class="citation" data-id="98977"><a href="/opinion/98977/mason-v-united-states/" aria-description="Citation for case: Mason v. United States">Mason</a></span></i> and <i><span class="citation" data-id="104912"><a href="/opinion/104912/hoffman-v-united-states/" aria-description="Citation for case: Hoffman v. United States">Hoffman, supra,</a></span></i> in form only, while its content is eroded in application, is hardly an auspicious beginning for application of the privilege to the States. As was well stated in a closely analogous situation, "[t]o continue a rule which is honored by this Court only with lip service is not a healthy thing and in the long run will do disservice to the federal system." <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#351" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, at 351</a></span> (HARLAN, J., concurring).</p>
<p>I would affirm.</p>
<h2>NOTES</h2>
<p>[1]  In both cases the question was whether comment upon the failure of an accused to take the stand in his own defense in a state prosecution violated the privilege. It was assumed, but not decided, in both cases that such comment in a federal prosecution for a federal offense would infringe the provision of the Fifth Amendment that "no person. . . shall be compelled in any criminal case to be a witness against himself." For other statements by the Court that the Fourteenth Amendment does not apply the federal privilege in state proceedings, see <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/#127" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117, 127-129</a></span>; <i>Snyder</i> v. <i>Massachusetts,</i> <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span>.</p>
<p>[2]  Ten Justices have supported this view. See <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#346" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335, 346</a></span> (opinion of MR. JUSTICE DOUGLAS). The Court expressed itself as unpersuaded to this view in <i>In re Kemmler,</i> <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/#448" aria-description="Citation for case: In Re Kemmler">136 U. S. 436, 448-449</a></span>; <i>McElvaine</i> v. <i>Brush,</i> <span class="citation" data-id="93208"><a href="/opinion/93208/mcelvaine-v-brush/#158" aria-description="Citation for case: McElvaine v. Brush">142 U. S. 155, 158-159</a></span>; <i>Maxwell</i> v. <i>Dow,</i> <span class="citation" data-id="9417812"><a href="/opinion/95204/maxwell-v-dow/#597" aria-description="Citation for case: Maxwell v. Dow">176 U. S. 581, 597-598</a></span>; <i>Twining</i> v. <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#96" aria-description="Citation for case: Twining v. New Jersey"><i>New Jersey, supra,</i> p. 96</a></span>. See <i>Spies</i> v. <i>Illinois,</i> <span class="citation" data-id="92032"><a href="/opinion/92032/spies-v-illinois/" aria-description="Citation for case: Spies v. Illinois">123 U. S. 131</a></span>. Decisions that particular guarantees were not safeguarded against state action by the Privileges and Immunities Clause or other provision of the Fourteenth Amendment are: <i>United States</i> v. <i>Cruikshank,</i> <span class="citation" data-id="9417049"><a href="/opinion/89309/united-states-v-cruikshank/#551" aria-description="Citation for case: United States v. Cruikshank">92 U. S. 542, 551</a></span>; <i>Prudential Ins. Co.</i> v. <i>Cheek,</i> <span class="citation" data-id="100023"><a href="/opinion/100023/prudential-insurance-co-of-america-v-cheek/#543" aria-description="Citation for case: Prudential Insurance Co. of America v. Cheek">259 U. S. 530, 543</a></span> (First Amendment); <i>Presser</i> v. <i>Illinois,</i> <span class="citation" data-id="91528"><a href="/opinion/91528/presser-v-illinois/#265" aria-description="Citation for case: Presser v. Illinois">116 U. S. 252, 265</a></span> (Second Amendment); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#398" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 398</a></span> (Fourth Amendment); <i>Hurtado</i> v. <i>California,</i> <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/#538" aria-description="Citation for case: Hurtado v. California">110 U. S. 516, 538</a></span> (Fifth Amendment requirement of grand jury indictments); <i>Palko</i> v. <i>Connecticut,</i> <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#328" aria-description="Citation for case: Palko v. Connecticut">302 U. S. 319, 328</a></span> (Fifth Amendment double jeopardy); <i>Maxwell</i> v. <span class="citation" data-id="9417812"><a href="/opinion/95204/maxwell-v-dow/#595" aria-description="Citation for case: Maxwell v. Dow"><i>Dow, supra,</i> at 595</a></span> (Sixth Amendment jury trial); <i>Walker</i> v. <i>Sauvinet,</i> <span class="citation" data-id="89245"><a href="/opinion/89245/walker-v-sauvinet/#92" aria-description="Citation for case: Walker v. Sauvinet">92 U. S. 90, 92</a></span> (Seventh Amendment jury trial); <i>In re <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">Kemmler, supra</a></span></i><i>; </i><i>McElvaine</i> v. <i><span class="citation" data-id="93208"><a href="/opinion/93208/mcelvaine-v-brush/" aria-description="Citation for case: McElvaine v. Brush">Brush, supra</a></span></i><i>; </i><i>O'Neil</i> v. <i>Vermont,</i> <span class="citation" data-id="9841791"><a href="/opinion/93324/oneil-v-vermont/#332" aria-description="Citation for case: O&#x27;Neil v. Vermont">144 U. S. 323, 332</a></span> (Eighth Amendment prohibition against cruel and unusual punishment).</p>
<p>[3]  In <i>Barron</i> v. <i>Baltimore,</i> <span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span>, decided before the adoption of the Fourteenth Amendment, Chief Justice Marshall, speaking for the Court, held that this right was not secured against state action by the Fifth Amendment's provision: "Nor shall private property be taken for public use, without just compensation."</p>
<p>[4]  <i>E. g., </i><i>Gitlow</i> v. <i>New York,</i> <span class="citation" data-id="100708"><a href="/opinion/100708/gitlow-v-new-york/#666" aria-description="Citation for case: Gitlow v. New York">268 U. S. 652, 666</a></span> (speech and press); <i>Lovell</i> v. <i>City of Griffin,</i> <span class="citation" data-id="102991"><a href="/opinion/102991/lovell-v-city-of-griffin/#450" aria-description="Citation for case: Lovell v. City of Griffin">303 U. S. 444, 450</a></span> (speech and press); <i>New York Times Co.</i> v. <i>Sullivan,</i> <span class="citation" data-id="9422744"><a href="/opinion/106761/new-york-times-co-v-sullivan/" aria-description="Citation for case: New York Times Co. v. Sullivan">376 U. S. 254</a></span> (speech and press); <i>Staub</i> v. <i>City of Baxley,</i> <span class="citation" data-id="9421529"><a href="/opinion/105608/staub-v-city-of-baxley/#321" aria-description="Citation for case: Staub v. City of Baxley">355 U. S. 313, 321</a></span> (speech); <i>Grosjean</i> v. <i>American Press Co.,</i> <span class="citation" data-id="102601"><a href="/opinion/102601/grosjean-v-american-press-co/#244" aria-description="Citation for case: Grosjean v. American Press Co.">297 U. S. 233, 244</a></span> (press); <i>Cantwell</i> v. <i>Connecticut,</i> <span class="citation" data-id="103355"><a href="/opinion/103355/cantwell-v-connecticut/#303" aria-description="Citation for case: Cantwell v. Connecticut">310 U. S. 296, 303</a></span> (religion); <i>De Jonge</i> v. <i>Oregon,</i> <span class="citation" data-id="102728"><a href="/opinion/102728/de-jonge-v-oregon/#364" aria-description="Citation for case: De Jonge v. Oregon">299 U. S. 353, 364</a></span> (assembly); <i>Shelton</i> v. <i>Tucker,</i> <span class="citation" data-id="9422089"><a href="/opinion/106142/shelton-v-tucker/#486" aria-description="Citation for case: Shelton v. Tucker">364 U. S. 479, 486</a></span> (association); <i>Louisiana ex rel. Gremillion</i> v. <i>NAACP,</i> <span class="citation" data-id="9422214"><a href="/opinion/106240/louisiana-ex-rel-gremillion-v-national-assn-for-the-advancement-of/#296" aria-description="Citation for case: Louisiana Ex Rel. Gremillion v. National Ass&#x27;n for the...">366 U. S. 293, 296</a></span> (association); <i>NAACP</i> v. <i>Button,</i> <span class="citation" data-id="9422512"><a href="/opinion/106514/national-assn-for-the-advancement-of-colored-people-v-button/" aria-description="Citation for case: National Ass&#x27;n for the Advancement of Colored People v....">371 U. S. 415</a></span> (association and speech); <i>Brotherhood of Railroad Trainmen</i> v. <i>Virginia ex rel. Virginia State Bar,</i> <span class="citation" data-id="9422774"><a href="/opinion/106803/brotherhood-of-railroad-trainmen-v-virginia-ex-rel-virginia-state-bar/" aria-description="Citation for case: Brotherhood of Railroad Trainmen v. Virginia Ex Rel....">377 U. S. 1</a></span> (association).</p>
<p>[5]  See <i>Wolf</i> v. <i>Colorado,</i> <span class="citation" data-id="9420374"><a href="/opinion/104709/wolf-v-colorado/#27" aria-description="Citation for case: Wolf v. Colorado">338 U. S. 25, 27-28</a></span>; <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#213" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 213</a></span>.</p>
<p>[6]  See also <i>Robinson</i> v. <i>California,</i> <span class="citation" data-id="9422471"><a href="/opinion/106451/robinson-v-california/#666" aria-description="Citation for case: Robinson v. California">370 U. S. 660, 666</a></span>, which, despite <i>In re <span class="citation" data-id="92834"><a href="/opinion/92834/in-re-kemmler/" aria-description="Citation for case: In Re Kemmler">Kemmler, supra</a></span></i><i>; </i><i>McElvaine</i> v. <i><span class="citation" data-id="93208"><a href="/opinion/93208/mcelvaine-v-brush/" aria-description="Citation for case: McElvaine v. Brush">Brush, supra</a></span></i><i>; </i><i>O'Neil</i> v. <i><span class="citation" data-id="9841791"><a href="/opinion/93324/oneil-v-vermont/" aria-description="Citation for case: O&#x27;Neil v. Vermont">Vermont, supra</a></span></i><i>,</i> made applicable to the States the Eighth Amendment's ban on cruel and unusual punishments.</p>
<p>[7]  <i><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/" aria-description="Citation for case: Boyd v. United States">Boyd</a></span></i> had said of the privilege, ". . . any compulsory discovery by extorting the party's oath . . . to convict him of crime . . . is contrary to the principles of a free government. It is abhorrent to the instincts of an Englishman; it is abhorrent to the instincts of an American. It may suit the purposes of despotic power; but it cannot abide the pure atmosphere of political liberty and personal freedom." 116 U. S., at 631-632.
</p>
<p>Dean Griswold has said: "I believe the Fifth Amendment is, and has been through this period of crisis, an expression of the moral striving of the community. It has been a reflection of our common conscience, a symbol of the America which stirs our hearts." The Fifth Amendment Today 73 (1955).</p>
<p>[8]  The brief states further:
</p>
<p>"Underlying the decisions excluding coerced confessions is the implicit assumption that an accused is privileged against incriminating himself, either in the jail house, the grand jury room, or on the witness stand in a public trial. . . .</p>
<p>". . . It is fundamentally inconsistent to suggest, as the Court's opinions now suggest, that the State is entirely free to compel an accused to incriminate himself before a grand jury, or at the trial, but cannot do so in the police station. Frank recognition of the fact that the Due Process Clause prohibits the States from enforcing their laws by compelling the accused to confess, regardless of where such compulsion occurs, would not only clarify the principles involved in confession cases, but would assist the States significantly in their efforts to comply with the limitations placed upon them by the Fourteenth Amendment."</p>
<p>[9]  See <i>Greenberg</i> v. <i>United States,</i> <span class="citation" data-id="8922268"><a href="/opinion/8932115/greenberg-v-united-states/" aria-description="Citation for case: Greenberg v. United States">343 U. S. 918</a></span>, reversing <i>per curiam,</i> <span class="citation" data-id="228036"><a href="/opinion/228036/united-states-v-greenberg/" aria-description="Citation for case: United States v. Greenberg">192 F. 2d 201</a></span>; <i>Singleton</i> v. <i>United States,</i> <span class="citation" data-id="8922391"><a href="/opinion/8932238/singleton-v-united-states/" aria-description="Citation for case: Singleton v. United States">343 U. S. 944</a></span>, reversing <i>per curiam,</i> <span class="citation" data-id="228448"><a href="/opinion/228448/united-states-v-singleton/" aria-description="Citation for case: United States v. Singleton">193 F. 2d 464</a></span>. In <i>United States</i> v. <i>Coffey,</i> <span class="citation" data-id="229980"><a href="/opinion/229980/united-states-v-coffey/" aria-description="Citation for case: United States v. Coffey">198 F. 2d 438</a></span> (C. A. 3d Cir.), cited with approval in <i>Emspak</i> v. <i>United States,</i> <span class="citation" data-id="9421180"><a href="/opinion/105306/emspak-v-united-states/" aria-description="Citation for case: Emspak v. United States">349 U. S. 190</a></span>, the Court of Appeals for the Third Circuit stated:
</p>
<p>"in determining whether the witness really apprehends danger in answering a question, the judge cannot permit himself to be skeptical; rather must he be acutely aware that in the deviousness of crime and its detection incrimination may be approached and achieved by obscure and unlikely lines of inquiry." <span class="citation" data-id="229980"><a href="/opinion/229980/united-states-v-coffey/#440" aria-description="Citation for case: United States v. Coffey">198 F. 2d, at 440-441</a></span>.</p>
<p>[1]  That precise question has not heretofore been decided by this Court. <i>Twining</i> v. <i>New Jersey,</i> <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78</a></span>, and the cases which followed it, see <i>infra,</i> p. 17, all involved issues not precisely similar. Although the Court has stated broadly that an individual could "be required to incriminate himself in . . . state proceedings," <i>Cohen</i> v. <i>Hurley,</i> <span class="citation" data-id="9422196"><a href="/opinion/106223/cohen-v-hurley/#127" aria-description="Citation for case: Cohen v. Hurley">366 U. S. 117, 127</a></span>, the context in which such statements were made was that the State had in each case recognized the right to remain silent. In <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining, supra,</a></span></i> until now the primary authority, the Court noted that "all the States of the Union have, from time to time, with varying form but uniform meaning, included the privilege in their constitutions, except the States of New Jersey and Iowa, and in those States it is held to be part of the existing law." <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#92" aria-description="Citation for case: Twining v. New Jersey">211 U. S., at 92</a></span>.
</p>
<p>While I do not believe that the coerced confession cases furnish any basis for incorporating the Fifth Amendment into the Fourteenth, see <i>infra,</i> pp. 17-20, they do, it seems to me, carry an implication that coercion to incriminate oneself, even when under the forms of law, cf. <i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/#285" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278, 285</a></span>, discussed <i>infra,</i> pp. 17-18, is inconsistent with due process. Since every State already recognizes a privilege against self-incrimination so defined, see VIII Wigmore, Evidence (McNaughton rev. 1961), § 2252, the effect of including such a privilege in due process is only to create the possibility that a federal question, to be decided under the Due Process Clause, would be raised by a State's refusal to accept a claim of the privilege.</p>
<p>[2]  See note <span class="citation" data-id="91153"><a href="/opinion/91153/hagar-v-reclamation-district-no-108/" aria-description="Citation for case: Hagar v. Reclamation District No. 108">1, <i>supra.</i></a></span></p>
<p>[3]  Nothing in the opinion in <i>Brown</i> supports the Court's intimation here, <i>ante,</i> p. 6, that if <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> had not been on the books, reversal of the convictions would have been based on the Fifth Amendment. The Court made it plain in <i>Brown</i> that it regarded the trial use of a confession extracted by torture as on a par with domination of a trial by a mob, see, <i>e. g., </i><i>Moore</i> v. <i>Dempsey,</i> <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86</a></span>, where the trial "is a mere pretense," 297 U. S., at 286.</p>
<p>[4]  "And so, when a conviction in a state court is properly here for review, under a claim that a right protected by the Fourteenth Amendment has been denied, the question is not whether the record can be found to disclose an infraction of one of the specific provisions of the first eight amendments. To come concretely to the present case, the question is not whether the record permits a finding, by a tenuous process of psychological assumptions and reasoning, that Malinski by means of a confession was forced to self-incrimination in defiance of the Fifth Amendment. The exact question is whether the criminal proceedings which resulted in his conviction deprived him of the due process of law by which he was constitutionally entitled to have his guilt determined." <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#416" aria-description="Citation for case: Malinski v. New York"><i>Malinski, supra,</i> at 416</a></span> (opinion of Frankfurter, J.).</p>
<p>[5]  In <i><span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/" aria-description="Citation for case: Adamson v. California">Adamson</a></span></i> and <i><span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/" aria-description="Citation for case: Palko v. Connecticut">Palko, supra,</a></span></i> which adhered to the rule announced in <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining, supra,</a></span></i> the Court cited some of the very cases now relied on by the majority to show that <i><span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/" aria-description="Citation for case: Twining v. New Jersey">Twining</a></span></i> was gradually being eroded. <span class="citation" data-id="9420036"><a href="/opinion/104455/adamson-v-california/#54" aria-description="Citation for case: Adamson v. California">332 U. S., at 54</a></span>, notes 12, 13; <span class="citation" data-id="102879"><a href="/opinion/102879/palko-v-connecticut/#325" aria-description="Citation for case: Palko v. Connecticut">302 U. S., at 325, 326</a></span>.</p>
<p>[6]  Cf. the majority and dissenting opinions in <i>Aguilar</i> v. <i>Texas, post,</i> p. 108.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Mancusi v. DeForte.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Mancusi v. DeForte"
type: case
citation: "392 U.S. 364 (1968)"
parallel_cite: "88 S. Ct. 2120; 20 L. Ed. 2d 1154; 68 L.R.R.M. (BNA) 2449"
neutral_cite: 1968 U.S. LEXIS 3075
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1968
date_decided: 1968-06-17
docket: 844
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1968-06-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mancusi v. DeForte
  varies_by_point: false
  scope_note: "The holding that an employee can have a reasonable expectation of privacy in a shared workplace survives; Rakas v. Illinois (1978) recast 'standing' as a substantive REP merits question but did not disturb this result."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/"
  cluster_id: 107745
  opinion_id: 107745
  identity_checked: true
homes:
  - page: "[[Standing to Challenge a Search]]"
    role: "Key — Progeny"
related: ["[[Jones v. United States]]", "[[Katz v. United States]]", "[[Rakas v. Illinois]]", "[[O'Connor v. Ortega]]", "[[Minnesota v. Carter]]"]
aliases: []
tags: ["case", "fourth-amendment", "standing", "expectation-of-privacy", "workplace", "shared-office"]
holding: "A union official has Fourth Amendment standing to challenge a warrantless search of the office he shares with other officials, because capacity to claim the Amendment turns on a reasonable expectation of freedom from governmental intrusion in the area, not on a property right."
lake:
  record_id: Mancusi v. DeForte
  status: verified
  projected_at: 2026-07-09
---

# Mancusi v. DeForte

*392 U.S. 364 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
DeForte, a vice president of a Teamsters local, was charged with conspiracy, coercion, and extortion. State officials, armed only with a district attorney's subpoena and no warrant, entered the single large office DeForte shared with other union officials and, over his objection, seized union records that were in his custody. The records were used to convict him. On [[Common Legal Terms#habeas-corpus|habeas]], he claimed the warrantless search violated his Fourth Amendment rights.

## Issue
Whether DeForte had [[Standing to Challenge a Search|Fourth Amendment standing]] to challenge the warrantless search and seizure of union records taken from the office he shared with other union officials.

## Rule
Standing turns on a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the area, not on ownership. "[C]apacity to claim the protection of the Amendment depends not upon a property right in the invaded place but upon whether the area was one in which there was a reasonable expectation of freedom from governmental intrusion." — 392 U.S. at 368 (citing *Katz v. United States*, 389 U.S. 347, 352). ^pin-368

"We hold that in these circumstances DeForte had Fourth Amendment standing to object to the admission of the papers at his trial." — [*Id.* at 369](https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/#:~:text=We%20hold%20that%20in%20these). ^pin-369

## Application
DeForte shared one large room with other union officials, spent considerable time there, and had custody of the records when they were seized. Even without a private office, "DeForte still could reasonably have expected that only those persons and their personal or business guests would enter the office, and that records would not be touched except with their permission or that of union higher-ups." — [*Id.* at 369](https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/#:~:text=DeForte%20still%20could%20reasonably%20have). ^pin-369b

That expectation "was inevitably defeated by the entrance of state officials, their conduct of a general search, and their removal of records which were in DeForte's custody." Because he had a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in the shared office, he had standing; and the warrantless search on a bare DA subpoena was unreasonable.

## Conclusion
DeForte had [[Standing to Challenge a Search|Fourth Amendment standing]] and the search was unreasonable; the grant of [[Common Legal Terms#habeas-corpus|habeas corpus]] relief was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of the result. *Mancusi* applies [[Katz v. United States]] to the standing question and relies on [[Jones v. United States]]'s loosening of the ownership requirement. [[Rakas v. Illinois]] (1978) abandoned the broad "legitimately on premises" formula and recast standing as a substantive expectation-of-privacy inquiry, but *Mancusi*'s holding that an employee can have a [[Reasonable Expectation of Privacy|reasonable expectation of privacy]] in a shared workplace endures and underlies [[O'Connor v. Ortega]]; cf. [[Minnesota v. Carter]].

## Appears on
- [[Standing to Challenge a Search]] — *Key — Progeny*

## Sources
- *Mancusi v. DeForte*, 392 U.S. 364 (1968) — https://www.courtlistener.com/opinion/107745/mancusi-v-deforte/ — pinpoints: 368, 369.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e9b1871ad8108be7", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Mancusi v. DeForte"}, "payload": {"all": [{"cite": "392 U.S. 364", "page": "364", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "392"}, {"cite": "88 S. Ct. 2120", "page": "2120", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "88"}, {"cite": "20 L. Ed. 2d 1154", "page": "1154", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "20"}, {"cite": "1968 U.S. LEXIS 3075", "page": "3075", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1968"}, {"cite": "68 L.R.R.M. (BNA) 2449", "page": "2449", "reporter": "L.R.R.M. (BNA)", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "68"}], "display": "392 U.S. 364", "official": {"cite": "392 U.S. 364", "page": "364", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "392"}, "official_selection_present": true, "record_id": "Mancusi v. DeForte"}}
{"assertion_id": "23aa56a1faa4574a", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-368", "record_id": "Mancusi v. DeForte"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-368", "pinpoint_status": "slip-only", "quote": "--- # Mancusi v. DeForte *392 U.S. 364 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DeForte, a vice president of a Teamsters local, was charged with conspiracy, coercion, and extortion. State officials, armed only with a district attorney's subpoena and no warrant, entered the single large office DeForte shared with other union officials and, over his objection, seized union records that were in his custody. The records were used to convict him. On habeas, he claimed the warrantless search violated his Fourth Amendment rights. ## Issue Whether DeForte had Fourth Amendment standing to challenge the warrantless search and seizure of union records taken from the office he shared with other union officials. ## Rule Standing turns on a reasonable expectation of privacy in the area, not on ownership.", "quote_fidelity": "mismatch", "record_id": "Mancusi v. DeForte", "star_marker": null}}
{"assertion_id": "5e76d8b8421a8838", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-369b", "record_id": "Mancusi v. DeForte"}, "payload": {"fragment": "#:~:text=DeForte%20still%20could%20reasonably%20have", "page": null, "pin_id": "pin-369b", "pinpoint_status": "star-verified", "quote": "DeForte still could reasonably have expected that only those persons and their personal or business guests would enter the office, and that records would not be touched except with their permission or that of union higher-ups.", "quote_fidelity": "matched", "record_id": "Mancusi v. DeForte", "star_marker": "369"}}
{"assertion_id": "5eff08cfa22c2d66", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-369", "record_id": "Mancusi v. DeForte"}, "payload": {"fragment": "#:~:text=We%20hold%20that%20in%20these", "page": null, "pin_id": "pin-369", "pinpoint_status": "star-verified", "quote": "We hold that in these circumstances DeForte had Fourth Amendment standing to object to the admission of the papers at his trial.", "quote_fidelity": "matched", "record_id": "Mancusi v. DeForte", "star_marker": "369"}}
{"assertion_id": "c9b771e53b96344f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Mancusi v. DeForte"}, "payload": {"as_of_content": "1968-06-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Mancusi v. DeForte", "scope_note": "The holding that an employee can have a reasonable expectation of privacy in a shared workplace survives; Rakas v. Illinois (1978) recast 'standing' as a substantive REP merits question but did not disturb this result.", "varies_by_point": false}}
```

### lake record — Mancusi v. DeForte

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mancusi v. DeForte",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mancusi v. DeForte",
    "case_name_short": "Mancusi",
    "case_name_full": "MANCUSI, WARDEN v. DeFORTE",
    "input_case_name": "Mancusi v. DeForte",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-17",
    "year": 1968,
    "docket": "844",
    "cluster_id": 107745,
    "lead_opinion_id": 107745,
    "sibling_ids": [
      107745,
      9423796,
      9423797,
      9423798
    ],
    "absolute_url": "/opinion/107745/mancusi-v-deforte/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 8970275,
        "score": 20,
        "case_name": "Mancusi v. DeForte"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "392 U.S. 364",
      "volume": "392",
      "reporter": "U.S.",
      "page": "364",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "88 S. Ct. 2120",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "2120",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1154",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1154",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L.R.R.M. (BNA) 2449",
        "volume": "68",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2449",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1968 U.S. LEXIS 3075",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "392 U.S. 364",
        "volume": "392",
        "reporter": "U.S.",
        "page": "364",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "88 S. Ct. 2120",
        "volume": "88",
        "reporter": "S. Ct.",
        "page": "2120",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "20 L. Ed. 2d 1154",
        "volume": "20",
        "reporter": "L. Ed. 2d",
        "page": "1154",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1968 U.S. LEXIS 3075",
        "volume": "1968",
        "reporter": "U.S. LEXIS",
        "page": "3075",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L.R.R.M. (BNA) 2449",
        "volume": "68",
        "reporter": "L.R.R.M. (BNA)",
        "page": "2449",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "392 U.S. 364",
    "official_selection": {
      "court_class": "scotus",
      "selected": "392 U.S. 364",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-368",
      "page": null,
      "quote": "--- # Mancusi v. DeForte *392 U.S. 364 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background DeForte, a vice president of a Teamsters local, was charged with conspiracy, coercion, and extortion. State officials, armed only with a district attorney's subpoena and no warrant, entered the single large office DeForte shared with other union officials and, over his objection, seized union records that were in his custody. The records were used to convict him. On habeas, he claimed the warrantless search violated his Fourth Amendment rights. ## Issue Whether DeForte had Fourth Amendment standing to challenge the warrantless search and seizure of union records taken from the office he shared with other union officials. ## Rule Standing turns on a reasonable expectation of privacy in the area, not on ownership.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-369",
      "page": null,
      "quote": "We hold that in these circumstances DeForte had Fourth Amendment standing to object to the admission of the papers at his trial.",
      "star_marker": "369",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 10264,
      "fragment": "#:~:text=We%20hold%20that%20in%20these",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-369b",
      "page": null,
      "quote": "DeForte still could reasonably have expected that only those persons and their personal or business guests would enter the office, and that records would not be touched except with their permission or that of union higher-ups.",
      "star_marker": "369",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13112,
      "fragment": "#:~:text=DeForte%20still%20could%20reasonably%20have",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1968-06-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mancusi v. DeForte",
    "varies_by_point": false,
    "scope_note": "The holding that an employee can have a reasonable expectation of privacy in a shared workplace survives; Rakas v. Illinois (1978) recast 'standing' as a substantive REP merits question but did not disturb this result.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Jeffrey Brian Ziegler",
          "cluster_id": 796647,
          "cite": [
            "474 F.3d 1184",
            "2007 U.S. App. LEXIS 1953",
            "2007 WL 222167"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grays v. State",
          "cluster_id": 5261713,
          "cite": [
            "905 S.W.2d 54",
            "1995 Tex. App. LEXIS 1833",
            "1995 WL 478381"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Juan Delgado, Dagoberto Silva, Henry Escobar",
          "cluster_id": 542046,
          "cite": [
            "903 F.2d 1495",
            "30 Fed. R. Serv. 1038",
            "1990 U.S. App. LEXIS 10078",
            "1990 WL 75081"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Schowengerdt v. General Dynamics Corp.",
          "cluster_id": 8961234,
          "cite": [
            "823 F.2d 1328",
            "2 I.E.R. Cas. (BNA) 545"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Dale Dunn",
          "cluster_id": 454693,
          "cite": [
            "766 F.2d 880"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane1_negative"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jenkins v. McKeithen",
          "cluster_id": 107964,
          "cite": [
            "23 L. Ed. 2d 404",
            "89 S. Ct. 1843",
            "395 U.S. 411",
            "1969 U.S. LEXIS 3175",
            "71 L.R.R.M. (BNA) 2385"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rawlings v. Kentucky",
          "cluster_id": 110326,
          "cite": [
            "65 L. Ed. 2d 633",
            "100 S. Ct. 2556",
            "448 U.S. 98",
            "1980 U.S. LEXIS 142"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Maryland",
          "cluster_id": 110118,
          "cite": [
            "61 L. Ed. 2d 220",
            "99 S. Ct. 2577",
            "442 U.S. 735",
            "1979 U.S. LEXIS 134"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
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
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'CONNOR v. Ortega",
          "cluster_id": 111851,
          "cite": [
            "94 L. Ed. 2d 714",
            "107 S. Ct. 1492",
            "480 U.S. 709",
            "1987 U.S. LEXIS 1507",
            "1 I.E.R. Cas. (BNA) 1617",
            "55 U.S.L.W. 4405",
            "42 Empl. Prac. Dec. (CCH) 36,891"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Payner",
          "cluster_id": 110317,
          "cite": [
            "65 L. Ed. 2d 468",
            "100 S. Ct. 2439",
            "447 U.S. 727",
            "1980 U.S. LEXIS 136"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cupp v. Murphy",
          "cluster_id": 108801,
          "cite": [
            "36 L. Ed. 2d 900",
            "93 S. Ct. 2000",
            "412 U.S. 291",
            "1973 U.S. LEXIS 63"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaufman v. United States",
          "cluster_id": 107874,
          "cite": [
            "22 L. Ed. 2d 227",
            "89 S. Ct. 1068",
            "394 U.S. 217",
            "1969 U.S. LEXIS 2158"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul v. Oates",
          "cluster_id": 348314,
          "cite": [
            "560 F.2d 45",
            "1 Fed. R. Serv. 718",
            "1977 U.S. App. LEXIS 13091"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bliss v. Franco",
          "cluster_id": 167399,
          "cite": [
            "446 F.3d 1036",
            "64 Fed. R. Serv. 3d 781",
            "2006 U.S. App. LEXIS 10342",
            "2006 WL 1075595"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Burton",
          "cluster_id": 2223932,
          "cite": [
            "848 N.E.2d 454",
            "6 N.Y.3d 584",
            "815 N.Y.S.2d 7"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hector Vega-Rodriguez v. Puerto Rico Telephone Company",
          "cluster_id": 739069,
          "cite": [
            "110 F.3d 174",
            "12 I.E.R. Cas. (BNA) 1253",
            "1997 U.S. App. LEXIS 6517",
            "1997 WL 154362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lorenzana v. Superior Court",
          "cluster_id": 1183387,
          "cite": [
            "511 P.2d 33",
            "9 Cal. 3d 626",
            "108 Cal. Rptr. 585",
            "1973 Cal. LEXIS 214"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Byrd v. United States",
          "cluster_id": 4497658,
          "cite": [
            "584 U.S. 395",
            "138 S. Ct. 1518",
            "200 L. Ed. 2d 805",
            "2018 U.S. LEXIS 2803"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert G. Baker v. United States",
          "cluster_id": 281912,
          "cite": [
            "401 F.2d 958",
            "131 U.S. App. D.C. 7",
            "22 A.F.T.R.2d (RIA) 5342",
            "1968 U.S. App. LEXIS 5836"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Alston",
          "cluster_id": 2283490,
          "cite": [
            "440 A.2d 1311",
            "88 N.J. 211",
            "1981 N.J. LEXIS 1677"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mancusi v. DeForte:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zMjU3MjgwMDAwMDAmcz0zNzcxNDMmdD1vJmQ9MjAyNi0wNy0wNSZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28107745+OR+9423796+OR+9423797+OR+9423798%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 6,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzImcz0zNjIyNzQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28107745+OR+9423796+OR+9423797+OR+9423798%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798)",
        "reviewed": 2,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 2,
        "triage_read": 0,
        "triage_snippet_classified": 2
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(107745 OR 9423796 OR 9423797 OR 9423798)",
    "indexed_citing_opinions": 507,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 107745,
        "count": 468,
        "count_source": "search"
      },
      {
        "opinion_id": 9423796,
        "count": 47,
        "count_source": "search"
      },
      {
        "opinion_id": 9423797,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9423798,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 745,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mancusi-v-deforte.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjQxODcwODgmcz03MzA2NzcwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28107745+OR+9423796+OR+9423797+OR+9423798%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 107745,
        "cited_id": 96015,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 96424,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 97431,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 97758,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 99745,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 100203,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 103663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104313,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 104932,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 105748,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 106777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107084,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 263829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
        "cited_id": 276492,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 107745,
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
    "date_created": "2026-07-05T11:31:25Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:31:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:31:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:35:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:31:48Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mancusi v. DeForte

```
<div>
<center><b><span class="citation" data-id="9423796"><a href="/opinion/107745/mancusi-v-deforte/" aria-description="Citation for case: Mancusi v. DeForte">392 U.S. 364</a></span> (1968)</b></center>
<center><h1>MANCUSI, WARDEN<br>
v.<br>
DeFORTE.</h1></center>
<center>No. 844.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued April 25, 1968.</center>
<center>Decided June 17, 1968.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><i>Michael H. Rauch,</i> Assistant Attorney General of New York, argued the cause for petitioner. With him on the brief were <i>Louis J. Lefkowitz,</i> Attorney General, and <i>Samuel A. Hirshowitz,</i> First Assistant Attorney General.</p>
<p><span class="star-pagination">*365</span> <i>James L. Lekin</i> argued the cause and filed a brief for respondent.</p>
<p>MR. JUSTICE HARLAN delivered the opinion of the Court.</p>
<p>In 1959 the respondent, Frank DeForte, a vice president of Teamsters Union Local 266, was indicted in Nassau County, New York, on charges of conspiracy, coercion, and extortion, it being alleged that he had misused his union office to "organize" owners of juke boxes and compel them to pay tribute. Prior to the return of the indictment, the Nassau County District Attorney's office issued a subpoena <i>duces tecum</i> to Local 266, calling upon it to produce certain books and records. The subpoena was served upon the Union at its offices. When the Union refused to comply, the state officials who had served the subpoena conducted a search and seized union records from an office shared by DeForte and several other union officials. The search and seizure were without a warrant and took place despite the protests of DeForte, who was present in the office at the time. Over DeForte's objection, the seized material was admitted against him at trial. He was convicted.</p>
<p>On direct appeal to the New York courts,<sup>[1]</sup> DeForte unsuccessfully argued, <i>inter alia,</i> that the seized material was constitutionally inadmissible in state proceedings under the rule laid down in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span>, because the search and seizure occurred without a warrant.<sup>[2]</sup> DeForte subsequently brought a federal habeas <span class="star-pagination">*366</span> corpus proceeding, in which he made the same contention. The United States District Court for the Western District of New York denied the writ, <span class="citation" data-id="8756522"><a href="/opinion/8772945/united-states-ex-rel-deforte-v-mancusi/" aria-description="Citation for case: United States ex rel. DeForte v. Mancusi">261 F. Supp. 579</a></span>, but on appeal the Court of Appeals for the Second Circuit reversed and directed that the writ issue. <span class="citation" data-id="276492"><a href="/opinion/276492/united-states-of-america-ex-rel-frank-deforte-v-vincent-r-mancusi/" aria-description="Citation for case: United States of America Ex Rel. Frank Deforte v. Vincent...">379 F. 2d 897</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./390/903/">390 U. S. 903</a></span>, to consider the State's<sup>[3]</sup> contention that the Court of Appeals erred in upsetting this state conviction. Concluding that the Court of Appeals was right, we affirm.</p>
<p></p>
<h2>I.</h2>
<p>It is desirable at the outset to make clear what is and what is not involved in this case. The decision below was based solely upon a finding that DeForte's Fourth and Fourteenth Amendment rights, see <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#30" aria-description="Citation for case: Ker v. California">374 U. S. 23, 30-34</a></span>, were violated by the search and seizure, and that the seized material was therefore inadmissible under <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>.</i> It is on this ground alone that DeForte argues for affirmance. Consequently, there is no occasion to consider whether DeForte might successfully have asserted his Fifth Amendment right against self-incrimination with respect to the use against him of the seized records. Cf. <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/" aria-description="Citation for case: United States v. White">322 U. S. 694</a></span>; <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">221 U. S. 361</a></span>. Nor is there any need to inquire whether DeForte could have asserted a Fourth or Fifth Amendment claim on behalf of the Union, for he did not do so. Moreover, this is not a case in which it is necessary to decide whether the traditional doctrine that Fourth Amendment rights "are personal rights, and . . . may be enforced by exclusion of evidence only at the instance of one whose own protection was infringed by the search and seizure," <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#389" aria-description="Citation for case: Simmons v. United States">390 U. S. 377, at 389</a></span>, should be modified. Cf. <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#390" aria-description="Citation for case: Simmons v. United States"><i>id.,</i> at 390, n. 12</a></span>. For DeForte claims <span class="star-pagination">*367</span> that under the traditional rule he does have standing to challenge the admission against him at trial of union records seized from the office where he worked. The questions for decision, then, are whether DeForte has Fourth Amendment standing to object to the seizure of the records and, if so, whether the search was one prohibited by the Fourth Amendment.</p>
<p></p>
<h2>II.</h2>
<p>We deal, first, with the question of "standing." The Fourth Amendment guarantees that "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." The papers which were seized in this case belonged not to DeForte but to the Union. Hence, DeForte can have personal standing only if, as to him, the search violated the "right of the people to be secure in their . . . houses . . . ."<sup>[4]</sup> This Court has held that the word "houses," as it appears in the Amendment, is not to be taken literally, and that the protection of the Amendment may extend to commercial premises. See, <i>e. g., </i><i>See</i> v. <i>Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span>; <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>.</p>
<p>Furthermore, the Amendment does not shield only those who have title to the searched premises. It was <span class="star-pagination">*368</span> settled even before our decision in <i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span>, that one with a possessory interest in the premises might have standing. See, <i>e. g., </i><i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>. In <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> even that requirement was loosened, and we held that "anyone legitimately on premises where a search occurs may challenge its legality . . . when its fruits are proposed to be used against him." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S., at 267</a></span>.<sup>[5]</sup> The Court's recent decision in <i>Katz</i> v. <i>United States,</i> <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U. S. 347</a></span>, also makes it clear that capacity to claim the protection of the Amendment depends not upon a property right in the invaded place but upon whether the area was one in which there was a reasonable expectation of freedom from governmental intrusion. See <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#352" aria-description="Citation for case: Katz v. United States">389 U. S., at 352</a></span>. The crucial issue, therefore, is whether, in light of all the circumstances, DeForte's office was such a place.</p>
<p>The record reveals that the office where DeForte worked consisted of one large room, which he shared with several other union officials. The record does not show from what part of the office the records were taken, and DeForte does not claim that it was a part reserved for his exclusive personal use. The parties have stipulated that DeForte spent "a considerable amount of time" in <span class="star-pagination">*369</span> the office, and that he had custody of the papers at the moment of their seizure.<sup>[6]</sup></p>
<p>We hold that in these circumstances DeForte had Fourth Amendment standing to object to the admission of the papers at his trial. It has long been settled that one has standing to object to a search of his office, as well as of his home. See, <i>e. g., </i><i>Gouled</i> v. <i>United States,</i> <span class="citation" data-id="99745"><a href="/opinion/99745/gouled-v-united-states/" aria-description="Citation for case: Gouled v. United States">255 U. S. 298</a></span>; <i>United States</i> v. <i>Lefkowitz,</i> <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span>; <i>Goldman</i> v. <i>United States,</i> <span class="citation" data-id="9419245"><a href="/opinion/103664/goldman-v-united-states/" aria-description="Citation for case: Goldman v. United States">316 U. S. 129</a></span>; cf. <i>Lopez</i> v. <i>United States,</i> <span class="citation" data-id="9422613"><a href="/opinion/106622/lopez-v-united-states/" aria-description="Citation for case: Lopez v. United States">373 U. S. 427</a></span>; <i>Osborn</i> v. <i>United States,</i> <span class="citation" data-id="9423307"><a href="/opinion/107319/osborn-v-united-states/" aria-description="Citation for case: Osborn v. United States">385 U. S. 323</a></span>. Since the Court in <i>Jones</i> v. <i>United States, supra</i><i>,</i> explicitly did away with the requirement that to establish standing one must show legal possession or ownership of the searched premises, see <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#265" aria-description="Citation for case: Jones v. United States">362 U. S., at 265-267</a></span>, it seems clear that if DeForte had occupied a "private" office in the union headquarters, and union records had been seized from a desk or a filing cabinet in that office, he would have had standing. Cf. <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span>; <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>. In such a "private" office, DeForte would have been entitled to expect that he would not be disturbed except by personal or business invitees, and that records would not be taken except with his permission or that of his union superiors. It seems to us that the situation was not fundamentally changed because DeForte shared an office with other union officers. DeForte still could reasonably have expected that only those persons and their personal or business guests would enter the office, and that records would not be touched except with their permission or that of union higher-ups. This expectation was inevitably defeated by the entrance of state officials, their conduct of a general search, and their removal of records which were in DeForte's custody. It is, of course, irrelevant that the <span class="star-pagination">*370</span> Union or some of its officials might validly have consented to a search of the area where the records were kept, regardless of DeForte's wishes, for it is not claimed that any such consent was given, either expressly or by implication.</p>
<p>Our conclusion that DeForte had standing finds strong support in <i>Jones</i> v. <i>United States, supra</i><i>.</i> Jones was the occasional occupant of an apartment to which the owner had given him a key. The police searched the apartment while Jones was present, and seized narcotics which they found in a bird's nest in an awning outside a window. Thus, like DeForte, Jones was not the owner of the searched premises. Like DeForte, Jones had little expectation of absolute privacy, since the owner and those authorized by him were free to enter. There was no indication that the area of the apartment near the bird's nest had been set off for Jones' personal use, so that he might have expected more privacy there than in the rest of the apartment; in this, it was like the part of DeForte's office where the union records were kept. Hence, we think that our decision that Jones had standing clearly points to the result which we reach here.</p>
<p></p>
<h2>III.</h2>
<p>The remaining question is whether the search of DeForte's office was "unreasonable" within the meaning of the Fourth Amendment. The State does not deny that the search and seizure were without a warrant, and it is settled for purposes of the Amendment that "except in certain carefully defined classes of cases, a search of private property without proper consent is `unreasonable' unless it has been authorized by a valid search warrant." <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#528" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 528-529</a></span>.<sup>[7]</sup> We <span class="star-pagination">*371</span> think it plain that the state officials' possession of a district attorney's subpoena of the kind involved here<sup>[8]</sup> does not bring this case within one of those "carefully defined classes." The State has not attempted to justify the search and seizure on that ground, and the New York courts have themselves said as a matter of state law that "[a district attorney's] subpoena duces tecum confers no right to seize the property referred to in the subpoena. . . ." <i>Amalgamated Union, Local 224</i> v. <i>Levine,</i> <span class="citation" data-id="6178892"><a href="/opinion/6310518/amalgamated-union-v-levine/#417" aria-description="Citation for case: Amalgamated Union v. Levine">31 Misc. 2d 416, 417</a></span>, 219 N. Y. S. 2d 851, 853.<sup>[9]</sup></p>
<p>Moreover, the subpoena involved here could not in any event qualify as a valid search warrant under the Fourth Amendment, for it was issued by the District Attorney himself,<sup>[10]</sup> and thus omitted the indispensable condition that "the inferences from the facts which lead to the complaint `. . . be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime.' <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span>." <i>Giordenello</i> v. <i>United States,</i> <span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/#486" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480, 486</a></span>. In <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span>, a corporate office was searched for papers which the corporation had refused to deliver in response to a New York District Attorney's subpoena, apparently similar to the one in this case. Speaking for the Court, Mr. Justice Holmes not only held that the seizure of the papers was unjustified but characterized it as "an outrage." <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States"><i>Id.,</i> at 391</a></span>. <span class="star-pagination">*372</span> The objections of both the corporation and the officer were sustained. Thus, there can be no doubt that under this Court's past decisions<sup>[11]</sup> the search of DeForte's office was "unreasonable" within the meaning of the Fourth Amendment.<sup>[12]</sup></p>
<p>The judgment of the Court of Appeals is</p>
<p><i>Affirmed.</i></p>
<p>MR. JUSTICE BLACK, with whom MR. JUSTICE STEWART joins, dissenting.</p>
<p>Until this case was decided just now it has been the law in this country, since the federal Fourth Amendment exclusionary rule was adopted in 1914, that a defendant on trial for a crime has no standing or substantive right to object to the use of papers and documents against him on the ground that those papers, belonging to someone else, had been taken from the owner in violation of the Fourth Amendment. Heretofore successful objection to use of such papers as evidence has been left to the owner whose constitutional rights had been invaded. In <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">221 U. S. 361</a></span>, decided in 1911, this Court in an exhaustive opinion by Mr. Justice Hughes, later Chief Justice, applied that principle by denying the benefit of the Fourth and Fifth Amendments to a corporate <span class="star-pagination">*373</span> officer, even one who had helped to prepare the corporate papers summoned to be produced.<sup>[1]</sup> In <i>United States</i> v. <i>White,</i> <span class="citation" data-id="104016"><a href="/opinion/104016/united-states-v-white/" aria-description="Citation for case: United States v. White">322 U. S. 694</a></span>, decided in 1944, this Court applied the same principle in rejecting a claim of a union officer that the use of union papers and documents against him under a subpoena <i>duces tecum</i> would incriminate him. And indeed the Court in today creating its new rule is unable to cite a single previous opinion of this Court <i>holding</i> to the contrary.</p>
<p>In creating this new rule against the use of papers and documents which speak truthfully for themselves, the Court is putting up new hurdles and barriers bound to save many criminals from conviction. I should not object to this new rule, however, if I thought it was or could be justified by the Fourth or any other constitutional amendment. But I do not think it can. The exclusionary rule itself, even as it applies to the exclusion of the defendant's own property when illegally seized, has had only a precarious tenure in this Court. See <i>Adams</i> v. <i>New York,</i> <span class="citation" data-id="96015"><a href="/opinion/96015/adams-v-new-york/" aria-description="Citation for case: Adams v. New York">192 U. S. 585</a></span> (1904); <i>Weeks</i> v. <i>United States,</i> <span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/" aria-description="Citation for case: Weeks v. United States">232 U. S. 383</a></span> (1914); and my concurring opinion in <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#661" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643, 661</a></span> (1961). I wish to repeat here what I have indicated before, that this seems to me a rather inopportune time to create a single rule more than the Constitution plainly requires to block conviction of guilty persons by keeping out probably the most reliable kind of evidence that can be offered.</p>
<p>A corporate or union official suffers no personal injury when the business office he occupies as an agent of the <span class="star-pagination">*374</span> corporation or union is invaded and when records he has prepared and safeguarded as an agent are seized. The invasion by the Government may disrupt the functioning of the office, prevent employees from performing their duties, and result in disclosure of business matters the company or union wished to keep secret. But all these are injuries only to the corporation or union as such. The organization has every right to challenge such intrusions whenever they occurif the seizure is illegal, the records obtained can be suppressed in a prosecution against the organization, and if no prosecution is initiated, the organization can obtain return of all the documents by bringing a civil action. See, <i>e. g., </i><i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931). Such intrusions, however, involve absolutely no invasion of the "personal privacy" or security of the agent or employee as an individual, and he accordingly has no right to seek suppression of records that the corporation or union itself has made no effort to regain.</p>
<p>The cases decided by this Court have, until today, uniformly supported this view and rejected the sweeping new exclusionary rule now advanced by the Court. Nor in my judgment does any one of the cases relied on by the Court provide support for its holding. The Court's basic premise is that if the union papers had been taken directly from a desk used by DeForte in a union office used only by him, his standing would have been clear, without regard to any other circumstances. I have found no past decision by this Court to that effect. Neither <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920), nor <i>Go-Bart Importing Co.</i> v. <i>United States,</i> <span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931), mentions the question of standing at all, and it is hard to see how the Court's inference can be drawn from these cases since in both the party seeking suppression of the documents was in fact the owner of <span class="star-pagination">*375</span> them. Although in <i>Silverthorne</i> the objections had been raised by both the corporation and one of its officers, standing was never even mentioned from the beginning to the end of the opinion, and the Court treated both parties as the "owners" of the documents. <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/#391" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S., at 391</a></span>. Consequently, the Court's use of Mr. Justice Holmes' reference to "outrage" in no way supports the Court's holding today, directly or indirectly.</p>
<p><i>Jones</i> v. <i>United States,</i> <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">362 U. S. 257</a></span> (1960), also fails to sustain the Court's position. In that case the petitioner had been arrested in a friend's apartment and was charged with possession of narcotics found there. This Court was troubled about the "dilemma" that would be created by requiring the petitioner, in order to secure suppression of the narcotics, to swear that they were taken from his possession, thus confessing his guilt of the very offense charged against him. To avoid this situation the Court held that petitioner could make his motion to suppress without swearing to possession, either because of the dilemma itself or because as a guest in the apartment he had the "legally requisite interest in the premises." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States">362 U. S., at 263</a></span>. The Court today puts great stress on the statement in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> that "anyone legitimately on premises where a search occurs may challenge its legality . . . when its fruits are proposed to be used against him." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#267" aria-description="Citation for case: Jones v. United States">362 U. S., at 267</a></span>. With deference I must point out that this sweeping dictum is taken somewhat out of context and cannot possibly have the literal meaning attributed to it. It would be quite a hyperbole, I think, to say that the <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> opinion suggested that just any person who happened to be in a house against which an unreasonable search was perpetrated could ask to have all evidence obtained by that search excluded from evidence against him. As was asked by the court below, would that dictum enable a <span class="star-pagination">*376</span> janitor to escape the use of evidence illegally seized from his boss? The Court apparently recognizes this problem even now, for DeForte clearly was "legitimately on [the] premises" and thus his standing should be obvious, under its reading of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>,</i> without the Court's extended discussion of "reasonable expectation" and the related limiting tests. This reasoning in terms of "expectations," however, requires conferring standing without regard to whether the agent happens to be present at the time of the search or not, a rather remarkable consequence of the statement in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>.</i> In fact the Court's opinion indicates to me that the Court is preparing the way to use <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> to eliminate entirely the requirement for standing to raise a search and seizure question and to permit a search to be challenged at any time, at any place, and under all circumstances, regardless of the defendant's relationship to the person or place searched or to the things seized. Any such step would elevate the Fourth Amendment to a position of importance far above that of any other constitutional provision, compare <i>Flast</i> v. <i>Cohen, ante,</i> p. 83, and would make it more difficult for the government to convict guilty persons who can make no claim to redress in any form since they suffered no invasion of any kind by the search itself. I would prefer to return to <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> itself, where we made quite clear throughout the opinion that while common-law concepts of property ownership were not controlling, standing was not automatically conferred on "anyone legitimately on [the] premises." We stressed:</p>
<blockquote>"In order to qualify as a `person aggrieved by an unlawful search and seizure' one must have been a victim of a search or seizure, one against whom the search was directed, as distinguished from one who claims prejudice only through the use of evidence gathered as a consequence of a search or seizure directed at someone else." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#261" aria-description="Citation for case: Jones v. United States">362 U. S., at 261</a></span>.</blockquote>
<p><span class="star-pagination">*377</span> In the present case I think it is entirely clear that the search was not "directed" against DeForte personally, but was addressed to and aimed at the Union and designed to secure from the Union papers belonging to the Union. The search occurred in a large room, which DeForte shared with a number of others, and the records were not taken from files and drawers used exclusively by him for his own private purposes. The police had been investigating a large conspiracy perpetrated through the Union and at the time were primarily interested in getting more information about the operation of the Union. The records taken were those that had been listed in a subpoena addressed to the Union itself, and since the Union had raised no objection to the subpoena, it was under a duty to turn over the records. Compare <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span> (1906).</p>
<p>Undoubtedly, I suppose, even if the Union's papers here should be returned either to the Union or to the defendant, the State could, on a new trial, summon the papers and get them and use them.<sup>[2]</sup> A rule which encourages such circumvention as that is hardly the kind of principle to which this great Court should give birth. I disclaim any responsibility whatever for the new rule.</p>
<p>MR. JUSTICE WHITE, dissenting.</p>
<p>Although the Fourth Amendment perhaps protects the individual's private desk in a union office shared with other officers or employees, I dissent from the Court's extension of the protected area to the office door.</p>
<h2>NOTES</h2>
<p>[1]  Those appeals culminated in a petition for certiorari to this Court, which was denied <i>sub nom. De Grandis</i> v. <i>New York,</i> <span class="citation" data-id="8947816"><a href="/opinion/8956781/de-grandis-v-new-york/" aria-description="Citation for case: De Grandis v. New York">375 U. S. 868</a></span>.</p>
<p>[2]  DeForte's petition for certiorari following direct appeal was denied in 1963, more than two years after the Court's decision in <i>Mapp</i> v. <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio</a></span></i><i>.</i> Under the rule laid down in <i>Linkletter</i> v. <i>Walker,</i> <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S. 618</a></span>, DeForte is entitled to invoke the exclusionary principle established in <i><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Mapp</a></span>.</i> See <span class="citation" data-id="9423077"><a href="/opinion/107084/linkletter-v-walker/" aria-description="Citation for case: Linkletter v. Walker">381 U. S., at 622</a></span> and n. 5.</p>
<p>[3]  The petitioner, Mancusi, is the warden of the New York State prison in which DeForte is confined.</p>
<p>[4]  The fact that the seized papers belonged to the Union does not imply of itself that an individual could never have personal standing to object to their admission against him. For example, state officers conceivably might have seized the papers during a search of DeForte's home, and in that event we think it clear that he would have had standing. <i>Wilson</i> v. <i>United States,</i> <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">221 U. S. 361</a></span>, is by no means to the contrary, for in that case there was no physical search at all. The only Fourth Amendment standing question in <i><span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/" aria-description="Citation for case: Wilson v. United States">Wilson</a></span></i> was whether a corporate officer had personal standing to object to a subpoena <i>duces tecum</i> addressed to the corporation, on the ground that it was overbroad. See <span class="citation" data-id="9418210"><a href="/opinion/97431/wilson-v-united-states/#375" aria-description="Citation for case: Wilson v. United States">221 U. S., at 375-376</a></span>.</p>
<p>[5]  The petitioner contends that this holding was not intended to have general application, but that it was devised solely to solve the particular dilemma presented in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span>:</i> that of a defendant who was charged with a possessory offense and consequently might have to concede his guilt in order to establish standing in the usual way. However, this limited reading of <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> overlooks the fact that in <i><span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/" aria-description="Citation for case: Jones v. United States">Jones</a></span></i> standing was held to exist on two distinct grounds: "(1) [The circumstance that] possession both convicts and confers standing, eliminates any necessity for a preliminary showing of an interest in the premises searched or the property seized . . . . (2) <i>Even were this not a prosecution turning on illicit possession,</i> the legally requisite interest in the premises was here satisfied . . . ." <span class="citation" data-id="106022"><a href="/opinion/106022/jones-v-united-states/#263" aria-description="Citation for case: Jones v. United States">362 U. S., at 263</a></span>. (Emphasis added.) Thus, the second branch of the holding, with which we are here concerned, was explicitly stated to be of general effect.</p>
<p>[6]  See Joint Appendix 51-52.</p>
<p>[7]  See also <i>Stoner</i> v. <i>California,</i> <span class="citation" data-id="9422755"><a href="/opinion/106777/stoner-v-california/" aria-description="Citation for case: Stoner v. California">376 U. S. 483</a></span>; <i>United States</i> v. <i>Jeffers,</i> <span class="citation" data-id="104932"><a href="/opinion/104932/united-states-v-jeffers/" aria-description="Citation for case: United States v. Jeffers">342 U. S. 48</a></span>; <i>McDonald</i> v. <i>United States,</i> <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span>; <i>Agnello</i> v. <i>United States,</i> <span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/" aria-description="Citation for case: Agnello v. United States">269 U. S. 20</a></span>.</p>
<p>[8]  A copy of the subpoena appears in the Joint Appendix, at 22. The subpoena was signed by the District Attorney and directed to the Union as a witness in a criminal action. It ordered the Union to appear before the District Attorney forthwith, and to bring with it specified union records. The subpoena appears to have been issued under the authority of N. Y. Code Crim. Proc. §§ 609-613.</p>
<p>[9]  See also <i>In re Atlas Lathing Corp.,</i> <span class="citation" data-id="5426289"><a href="/opinion/5584153/atlas-lathing-corp-v-bennett/" aria-description="Citation for case: Atlas Lathing Corp. v. Bennett">176 Misc. 959</a></span>, 29 N. Y. S. 2d 458; Hagan, Impounding and the Subpoena Duces Tecum, 26 Brooklyn L. Rev. 199, 210-211 (1960).</p>
<p>[10]  See n. 8, <i>supra.</i></p>
<p>[11]  The Court's opinion in <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span>, does contain dicta to the effect that there is a lesser right to privacy when government officials have a "right" to inspect the seized items. See, <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/#593" aria-description="Citation for case: Davis v. United States"><i>e. g., id.,</i> at 593</a></span>. However, the only holding in <i><span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">Davis</a></span></i> was that there had been a valid consent to the search; the case "did not involve a search warrant issue." <i>See</i> v. <i>City of Seattle,</i> <span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/#545" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541, 545, n. 7</a></span>.</p>
<p>[12]  It is, of course, immaterial that the State might have been able to obtain the same papers by means which did not violate the Fourth Amendment. As Mr. Justice Holmes stated in <i>Silverthorne Lumber Co.</i> v. <i>United States, supra,</i> at 392: "[T]he rights . . . against unlawful search and seizure are to be protected even if the same result might have been achieved in a lawful way."</p>
<p>[1]  See also <i>Hale</i> v. <i>Henkel,</i> <span class="citation" data-id="9418026"><a href="/opinion/96424/hale-v-henkel/" aria-description="Citation for case: Hale v. Henkel">201 U. S. 43</a></span> (1906); <i>Grant</i> v. <i>United States,</i> <span class="citation" data-id="97758"><a href="/opinion/97758/grant-v-united-states/" aria-description="Citation for case: Grant v. United States">227 U. S. 74</a></span> (1913); <i>Essgee Co.</i> v. <i>United States,</i> <span class="citation" data-id="100203"><a href="/opinion/100203/essgee-co-of-china-v-united-states/" aria-description="Citation for case: Essgee Co. of China v. United States">262 U. S. 151</a></span> (1923); <i>Goldstein</i> v. <i>United States,</i> <span class="citation" data-id="9419243"><a href="/opinion/103663/goldstein-v-united-states/" aria-description="Citation for case: Goldstein v. United States">316 U. S. 114</a></span> (1942); <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9419858"><a href="/opinion/104313/davis-v-united-states/" aria-description="Citation for case: Davis v. United States">328 U. S. 582</a></span> (1946); <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <i>Wild</i> v. <i>Brewer,</i> <span class="citation" data-id="9449961"><a href="/opinion/263829/albert-j-wild-v-bennett-y-brewer-revenue-agent-of-the-internal-revenue/" aria-description="Citation for case: Albert J. Wild v. Bennett Y. Brewer, Revenue Agent of the...">329 F. 2d 924</a></span> (C. A. 9th Cir. 1964).</p>
<p>[2]  Since the State had obtained a subpoena for these documents even before the search, the new subpoena would not be an invalid "fruit" of the illegal seizure. Compare <i><span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">Silverthorne, supra</a></span></i><i>.</i></p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Manson v. Brathwaite.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Manson v. Brathwaite"
type: case
citation: "432 U.S. 98 (1977)"
parallel_cite: "97 S. Ct. 2243; 53 L. Ed. 2d 140"
neutral_cite: 1977 U.S. LEXIS 116
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1977
date_decided: 1977-06-16
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1977-06-16
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Manson v. Brathwaite
  varies_by_point: false
  scope_note: "Reliability/totality standard intact; Perry v. New Hampshire (2012) confirmed the due-process screen applies only where police arranged the suggestive circumstances, without disturbing the Manson reliability factors."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109693/manson-v-brathwaite/"
  cluster_id: 109693
  opinion_id: 109693
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Anchor"
related: ["[[Neil v. Biggers]]", "[[Stovall v. Denno]]", "[[United States v. Wade]]", "[[Perry v. New Hampshire]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "suggestive-procedure", "reliability"]
holding: "There is no per se rule excluding identifications from unnecessarily suggestive procedures; reliability is the linchpin, assessed under…"
lake:
  record_id: Manson v. Brathwaite
  status: verified
  projected_at: 2026-07-09
---

# Manson v. Brathwaite

*432 U.S. 98 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
An undercover officer, Glover, bought heroin from a seller he viewed for a few minutes at an apartment door. He described the seller to another officer, who left a single police photograph of Brathwaite on Glover's desk; Glover identified it days later, and again identified Brathwaite at trial. Brathwaite argued the single-photo procedure was impermissibly suggestive and required exclusion of the identification.

## Issue
Whether due process requires a [[Common Legal Terms#per-se|per se]] rule excluding identification evidence derived from an unnecessarily suggestive procedure, or whether admissibility turns on the reliability of the identification under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Rule
No [[Common Legal Terms#per-se|per se]] exclusion; reliability governs. "reliability is the linchpin in determining the admissibility of identification testimony for both pre- and post-*Stovall* confrontations." — 432 U.S. at 114. ^pin-114

The reliability factors, drawn from *[[Neil v. Biggers]]*, are "the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation. Against these factors is to be weighed the corrupting effect of the suggestive identification itself." — [*Id.*](https://www.courtlistener.com/opinion/109693/manson-v-brathwaite/#:~:text=the%20opportunity%20of%20the%20witness) ^pin-114a

## Application
Even assuming the single-photograph display was suggestive, Glover's identification was reliable under the *Biggers* factors: as a trained officer he had a good, close opportunity to view the seller in daylight, paid careful attention, gave an accurate description, was certain in identifying the photograph, and made the identification only days after the crime. Weighed against the limited corrupting effect of the procedure, those indicia of reliability made the identification admissible.

## Conclusion
Reversed in favor of admissibility: identification evidence from a suggestive procedure is admitted when, under the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]], it is nonetheless reliable.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Manson* (with [[Neil v. Biggers]]) sets the governing due-process test for suggestive identifications. [[Perry v. New Hampshire]] (2012) later clarified that this due-process screen is triggered only when the suggestive circumstances were **arranged by law enforcement**, without disturbing *Manson*'s reliability framework.

## Appears on
- [[Eyewitness Identification]] — *Key — Anchor*

## Sources
- *Manson v. Brathwaite*, 432 U.S. 98 (1977) — https://www.courtlistener.com/opinion/109693/manson-v-brathwaite/ — pinpoint: 114.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd4364d121293fce", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Manson v. Brathwaite"}, "payload": {"all": [{"cite": "432 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "432"}, {"cite": "97 S. Ct. 2243", "page": "2243", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "97"}, {"cite": "53 L. Ed. 2d 140", "page": "140", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "53"}, {"cite": "1977 U.S. LEXIS 116", "page": "116", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1977"}], "display": "432 U.S. 98", "official": {"cite": "432 U.S. 98", "page": "98", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "432"}, "official_selection_present": true, "record_id": "Manson v. Brathwaite"}}
{"assertion_id": "4e6d744dc579bd2f", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-114a", "record_id": "Manson v. Brathwaite"}, "payload": {"fragment": "#:~:text=the%20opportunity%20of%20the%20witness", "page": null, "pin_id": "pin-114a", "pinpoint_status": "star-verified", "quote": "the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation. Against these factors is to be weighed the corrupting effect of the suggestive identification itself.", "quote_fidelity": "matched", "record_id": "Manson v. Brathwaite", "star_marker": "114"}}
{"assertion_id": "999c2d91112059fd", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-114", "record_id": "Manson v. Brathwaite"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-114", "pinpoint_status": "slip-only", "quote": "--- # Manson v. Brathwaite *432 U.S. 98 (1977)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An undercover officer, Glover, bought heroin from a seller he viewed for a few minutes at an apartment door. He described the seller to another officer, who left a single police photograph of Brathwaite on Glover's desk; Glover identified it days later, and again identified Brathwaite at trial. Brathwaite argued the single-photo procedure was impermissibly suggestive and required exclusion of the identification. ## Issue Whether due process requires a per se rule excluding identification evidence derived from an unnecessarily suggestive procedure, or whether admissibility turns on the reliability of the identification under the totality of the circumstances. ## Rule No per se exclusion; reliability governs.", "quote_fidelity": "mismatch", "record_id": "Manson v. Brathwaite", "star_marker": null}}
{"assertion_id": "f362b824d2be4338", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Manson v. Brathwaite"}, "payload": {"as_of_content": "1977-06-16", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Manson v. Brathwaite", "scope_note": "Reliability/totality standard intact; Perry v. New Hampshire (2012) confirmed the due-process screen applies only where police arranged the suggestive circumstances, without disturbing the Manson reliability factors.", "varies_by_point": false}}
```

### lake record — Manson v. Brathwaite

```json
{
  "schema_version": "s2.v1",
  "record_id": "Manson v. Brathwaite",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Manson v. Brathwaite",
    "case_name_short": "Manson",
    "case_name_full": "Manson, Correction Commissioner v. Brathwaite",
    "input_case_name": "Manson v. Brathwaite",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1977-06-16",
    "year": 1977,
    "docket": null,
    "cluster_id": 109693,
    "lead_opinion_id": 109693,
    "sibling_ids": [
      109693,
      9426868,
      9426869,
      9426870
    ],
    "absolute_url": "/opinion/109693/manson-v-brathwaite/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9011220,
        "score": 20,
        "case_name": "Manson v. Brathwaite"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "432 U.S. 98",
      "volume": "432",
      "reporter": "U.S.",
      "page": "98",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "97 S. Ct. 2243",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2243",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 140",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "140",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1977 U.S. LEXIS 116",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "116",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "432 U.S. 98",
        "volume": "432",
        "reporter": "U.S.",
        "page": "98",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "97 S. Ct. 2243",
        "volume": "97",
        "reporter": "S. Ct.",
        "page": "2243",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "53 L. Ed. 2d 140",
        "volume": "53",
        "reporter": "L. Ed. 2d",
        "page": "140",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1977 U.S. LEXIS 116",
        "volume": "1977",
        "reporter": "U.S. LEXIS",
        "page": "116",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "432 U.S. 98",
    "official_selection": {
      "court_class": "scotus",
      "selected": "432 U.S. 98",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-114",
      "page": null,
      "quote": "--- # Manson v. Brathwaite *432 U.S. 98 (1977)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background An undercover officer, Glover, bought heroin from a seller he viewed for a few minutes at an apartment door. He described the seller to another officer, who left a single police photograph of Brathwaite on Glover's desk; Glover identified it days later, and again identified Brathwaite at trial. Brathwaite argued the single-photo procedure was impermissibly suggestive and required exclusion of the identification. ## Issue Whether due process requires a per se rule excluding identification evidence derived from an unnecessarily suggestive procedure, or whether admissibility turns on the reliability of the identification under the totality of the circumstances. ## Rule No per se exclusion; reliability governs.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-114a",
      "page": null,
      "quote": "the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation. Against these factors is to be weighed the corrupting effect of the suggestive identification itself.",
      "star_marker": "114",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 39257,
      "fragment": "#:~:text=the%20opportunity%20of%20the%20witness",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1977-06-16",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Manson v. Brathwaite",
    "varies_by_point": false,
    "scope_note": "Reliability/totality standard intact; Perry v. New Hampshire (2012) confirmed the due-process screen applies only where police arranged the suggestive circumstances, without disturbing the Manson reliability factors.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Traynham v. State",
          "cluster_id": 10021058,
          "cite": [
            "243 Md. App. 717"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Myers v. State",
          "cluster_id": 10021078,
          "cite": [
            "243 Md. App. 154"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McComb",
          "cluster_id": 4394880,
          "cite": [
            "2017 Ohio 4010",
            "91 N.E.3d 255"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane1_negative"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
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
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cunningham",
          "cluster_id": 2587254,
          "cite": [
            "25 P.3d 519",
            "108 Cal. Rptr. 2d 291",
            "25 Cal. 4th 926"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Owens",
          "cluster_id": 111992,
          "cite": [
            "98 L. Ed. 2d 951",
            "108 S. Ct. 838",
            "484 U.S. 554",
            "1988 U.S. LEXIS 940",
            "56 U.S.L.W. 4160"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chipp",
          "cluster_id": 5689934,
          "cite": [
            "75 N.Y.2d 327",
            "552 N.E.2d 608",
            "553 N.Y.S.2d 72",
            "1990 N.Y. LEXIS 230"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jenkins",
          "cluster_id": 1195356,
          "cite": [
            "997 P.2d 1044",
            "95 Cal. Rptr. 2d 377",
            "22 Cal. 4th 900"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bryant, Smith and Wheeler",
          "cluster_id": 2720490,
          "cite": [
            "60 Cal. 4th 335",
            "178 Cal. Rptr. 3d 185",
            "334 P.3d 573",
            "2014 Cal. LEXIS 6110"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McDaniel v. Brown",
          "cluster_id": 1750,
          "cite": [
            "175 L. Ed. 2d 582",
            "130 S. Ct. 665",
            "558 U.S. 120",
            "2010 U.S. LEXIS 3"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gimmy v. People",
          "cluster_id": 1231296,
          "cite": [
            "645 P.2d 262",
            "1982 Colo. LEXIS 568"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Malloy",
          "cluster_id": 5685415,
          "cite": [
            "55 N.Y.2d 296",
            "434 N.E.2d 237",
            "449 N.Y.S.2d 168",
            "1982 N.Y. LEXIS 3140"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Schevers",
          "cluster_id": 1191968,
          "cite": [
            "979 P.2d 659",
            "132 Idaho 786",
            "1999 Ida. App. LEXIS 10"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Moore v. Illinois",
          "cluster_id": 109757,
          "cite": [
            "54 L. Ed. 2d 424",
            "98 S. Ct. 458",
            "434 U.S. 220",
            "1977 U.S. LEXIS 163"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gregory v. City of Louisville",
          "cluster_id": 2973641,
          "cite": [
            "444 F.3d 725",
            "2006 WL 909935"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Prudholm",
          "cluster_id": 1956631,
          "cite": [
            "446 So. 2d 729"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Arias",
          "cluster_id": 1179776,
          "cite": [
            "13 Cal. 4th 92",
            "913 P.2d 980",
            "51 Cal. Rptr. 2d 770",
            "96 Daily Journal DAR 4243",
            "96 Cal. Daily Op. Serv. 2575",
            "1996 Cal. LEXIS 1572"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ibarra v. State",
          "cluster_id": 1960811,
          "cite": [
            "11 S.W.3d 189",
            "1999 Tex. Crim. App. LEXIS 117",
            "1999 WL 956173"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. State",
          "cluster_id": 2428074,
          "cite": [
            "827 S.W.2d 949",
            "1992 Tex. Crim. App. LEXIS 106",
            "1992 WL 79216"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Madden v. State",
          "cluster_id": 2381074,
          "cite": [
            "799 S.W.2d 683",
            "1990 WL 130495"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Murad Nersesian",
          "cluster_id": 492031,
          "cite": [
            "824 F.2d 1294",
            "23 Fed. R. Serv. 487",
            "1987 U.S. App. LEXIS 8418"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Boyer",
          "cluster_id": 2515839,
          "cite": [
            "133 P.3d 581",
            "42 Cal. Rptr. 3d 677",
            "38 Cal. 4th 412",
            "2006 Daily Journal DAR 5671",
            "2006 Cal. Daily Op. Serv. 3863",
            "2006 Cal. LEXIS 5397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Loserth v. State",
          "cluster_id": 1494741,
          "cite": [
            "963 S.W.2d 770",
            "1998 Tex. Crim. App. LEXIS 22",
            "1998 WL 75681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Yeoman",
          "cluster_id": 2588519,
          "cite": [
            "72 P.3d 1166",
            "2 Cal. Rptr. 3d 186",
            "31 Cal. 4th 93",
            "2003 Cal. Daily Op. Serv. 6313",
            "2003 Daily Journal DAR 7888",
            "2003 Cal. LEXIS 4823"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hansen v. State",
          "cluster_id": 1829968,
          "cite": [
            "592 So. 2d 114",
            "1991 WL 280025"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Manson v. Brathwaite:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDkyNTYwMDAwMDAwJnM9NDM4NDIxMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109693+OR+9426868+OR+9426869+OR+9426870%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 3,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 4,
        "triage_snippet_classified": 196
      },
      "lane2_top_cited": {
        "query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zODAmcz0yNDM0MDI3JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28109693+OR+9426868+OR+9426869+OR+9426870%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870)",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 0,
        "triage_snippet_classified": 52
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109693 OR 9426868 OR 9426869 OR 9426870)",
    "indexed_citing_opinions": 3221,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109693,
        "count": 2827,
        "count_source": "search"
      },
      {
        "opinion_id": 9426868,
        "count": 433,
        "count_source": "search"
      },
      {
        "opinion_id": 9426869,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426870,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 5121,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/manson-v-brathwaite.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjU2ODcmcz0xMDM2MDcxNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109693+OR+9426868+OR+9426869+OR+9426870%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109693,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 107890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 108639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109539,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 109682,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 270486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 284140,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 288139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 308320,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 314070,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 324941,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 1436230,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 1801408,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 2221090,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 2222943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109693,
        "cited_id": 2611155,
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
    "date_created": "2026-07-05T11:35:13Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T11:35:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T11:35:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T11:39:19Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T11:35:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Manson v. Brathwaite (truncated)

```
<div>
<center><b><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98</a></span> (1977)</b></center>
<center><h1>MANSON, CORRECTION COMMISSIONER<br>
v.<br>
BRATHWAITE.</h1></center>
<center>No. 75-871.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued November 29, 1976.</center>
<center>Decided June 16, 1977.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SECOND CIRCUIT.
<p><span class="star-pagination">*99</span> <i>Bernard D. Gaffney</i> argued the cause for petitioner. With him on the brief was <i>George D. Stoughton.</i></p>
<p><i>David S. Golub</i> argued the cause for respondent. With him on the brief were <i>Frederick H. Weisberg, Richard A. Silver,</i> and <i>Jay H. Sandak.</i></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case presents the issue as to whether the Due Process Clause of the Fourteenth Amendment compels the exclusion, in a state criminal trial, apart from any consideration of reliability, of pretrial identification evidence obtained by a police procedure that was both suggestive and unnecessary. This Court's decisions in <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967), and <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972), are particularly implicated.</p>
<p></p>
<h2>I</h2>
<p>Jimmy D. Glover, a full-time trooper of the Connecticut State Police, in 1970 was assigned to the Narcotics Division in an undercover capacity. On May 5 of that year, about <span class="star-pagination">*100</span> 7:45 p. m., e. d. t., and while there was still daylight, Glover and Henry Alton Brown, an informant, went to an apartment building at 201 Westland, in Hartford, for the purpose of purchasing narcotics from "Dickie Boy" Cicero, a known narcotics dealer. Cicero, it was thought, lived on the third floor of that apartment building. Tr. 45-46, 68.<sup>[1]</sup> Glover and Brown entered the building, observed by backup Officers D'Onofrio and Gaffey, and proceeded by stairs to the third floor. Glover knocked at the door of one of the two apartments served by the stairway.<sup>[2]</sup> The area was illuminated by natural light from a window in the third floor hallway. <i>Id.,</i> at 27-28. The door was opened 12 to 18 inches in response to the knock. Glover observed a man standing at the door and, behind him, a woman. Brown identified himself. Glover then asked for "two things" of narcotics. <i>Id.,</i> at 29. The man at the door held out his hand, and Glover gave him two $10 bills. The door closed. Soon the man returned and handed Glover two glassine bags.<sup>[3]</sup> While the door was open, Glover stood within two feet of the person from whom he made the purchase and observed his face. Five to seven minutes elapsed from the <span class="star-pagination">*101</span> time the door first opened until it closed the second time. <i>Id.,</i> at 30-33.</p>
<p>Glover and Brown then left the building. This was about eight minutes after their arrival. Glover drove to headquarters where he described the seller to D'Onofrio and Gaffey. Glover at that time did not know the identity of the seller. <i>Id.,</i> at 36. He described him as being "a colored man, approximately five feet eleven inches tall, dark complexion, black hair, short Afro style, and having high cheekbones, and of heavy build. He was wearing at the time blue pants and a plaid shirt." <i>Id.,</i> at 36-37. D'Onofrio, suspecting from this description that respondent might be the seller, obtained a photograph of respondent from the Records Division of the Hartford Police Department. He left it at Glover's office. D'Onofrio was not acquainted with respondent personally, but did know him by sight and had seen him "[s]everal times" prior to May 5. <i>Id.,</i> at 63-65. Glover, when alone, viewed the photograph for the first time upon his return to headquarters on May 7; he identified the person shown as the one from whom he had purchased the narcotics. <i>Id.,</i> at 36-38.</p>
<p>The toxicological report on the contents of the glassine bags revealed the presence of heroin. The report was dated July 16, 1970. <i>Id.,</i> at 75-76.</p>
<p>Respondent was arrested on July 27 while visiting at the apartment of a Mrs. Ramsey on the third floor of 201 Westland. This was the apartment at which the narcotics sale had taken place on May 5.<sup>[4]</sup></p>
<p>Respondent was charged, in a two-count information, with possession and sale of heroin, in violation of Conn. Gen. Stat. (Rev. of 1958, as amended in 1969), §§ 19-481a and 19-480a <span class="star-pagination">*102</span> (1977).<sup>[5]</sup> At his trial in January 1971, the photograph from which Glover had identified respondent was received in evidence without objection on the part of the defense. Tr. 38. Glover also testified that, although he had not seen respondent in the eight months that had elapsed since the sale, "there [was] no doubt whatsoever" in his mind that the person shown on the photograph was respondent. <i>Id.,</i> at 41-42. Glover also made a positive in-court identification without objection. <i>Id.,</i> at 37-38.</p>
<p>No explanation was offered by the prosecution for the failure to utilize a photographic array or to conduct a lineup.</p>
<p>Respondent, who took the stand in his own defense, testified that on May 5, the day in question, he had been ill at his Albany Avenue apartment ("a lot of back pains, muscle spasms . . . a bad heart . . . high blood pressure . . . neuralgia in my face, and sinus," <i>id.,</i> at 106), and that at no time on that particular day had he been at 201 Westland. <i>Id.,</i> at 106, 113-114. His wife testified that she recalled, after her husband had refreshed her memory, that he was home all day on May 5. <i>Id.,</i> at 164-165. Doctor Wesley M. Vietzke, an internist and assistant professor of medicine at the University of Connecticut, testified that respondent had consulted him on April 15, 1970, and that he took a medical history from him, heard his complaints about his back and facial pain, and discovered that he had high blood pressure. <i>Id.,</i> at 129-131. The physician found respondent, subjectively, "in great discomfort." <i>Id.,</i> at 135. Respondent in fact underwent surgery for a herniated disc at L5 and S1 on August 17. <i>Id.,</i> at 157.</p>
<p>The jury found respondent guilty on both counts of the information. He received a sentence of not less than six nor <span class="star-pagination">*103</span> more than nine years. His conviction was affirmed <i>per curiam</i> by the Supreme Court of Connecticut. <i>State</i> v. <i>Brathwaite,</i> <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/" aria-description="Citation for case: State v. Brathwaite">164 Conn. 617</a></span>, <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/" aria-description="Citation for case: State v. Brathwaite">325 A. 2d 284</a></span> (1973). That court noted the absence of an objection to Glover's in-court identification and concluded that respondent "has not shown that substantial injustice resulted from the admission of this evidence." <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/#619" aria-description="Citation for case: State v. Brathwaite"><i>Id.,</i> at 619</a></span>, <span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/#285" aria-description="Citation for case: State v. Brathwaite">325 A. 2d, at 285</a></span>. Under Connecticut law, substantial injustice must be shown before a claim of error not made or passed on by the trial court will be considered on appeal. <i><span class="citation" data-id="1436230"><a href="/opinion/1436230/state-v-brathwaite/" aria-description="Citation for case: State v. Brathwaite">Ibid.</a></span></i></p>
<p>Fourteen months later, respondent filed a petition for habeas corpus in the United States District Court for the District of Connecticut. He alleged that the admission of the identification testimony at his state trial deprived him of due process of law to which he was entitled under the Fourteenth Amendment. The District Court, by an unreported written opinion based on the court's review of the state trial transcript,<sup>[6]</sup> dismissed respondent's petition. On appeal, the United States Court of Appeals for the Second Circuit reversed, with instructions to issue the writ unless the State gave notice of a desire to retry respondent and the new trial occurred within a reasonable time to be fixed by the District Judge.<sup>[7]</sup> <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d 363</a></span> (1975).</p>
<p>In brief summary, the court felt that evidence as to the photograph should have been excluded, regardless of reliability, <span class="star-pagination">*104</span> because the examination of the single photograph was unnecessary and suggestive. And, in the court's view, the evidence was unreliable in any event. We granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./425/957/">425 U. S. 957</a></span> (1976).</p>
<p></p>
<h2>II</h2>
<p><i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno, supra</a></span></i><i>,</i> decided in 1967, concerned a petitioner who had been convicted in a New York court of murder. He was arrested the day following the crime and was taken by the police to a hospital where the victim's wife, also wounded in the assault, was a patient. After observing Stovall and hearing him speak, she identified him as the murderer. She later made an in-court identification. On federal habeas, Stovall claimed the identification testimony violated his Fifth, Sixth, and Fourteenth Amendment rights. The District Court dismissed the petition, and the Court of Appeals, en banc, affirmed. This Court also affirmed. On the identification issue, the Court reviewed the practice of showing a suspect singly for purposes of identification, and the claim that this was so unnecessarily suggestive and conducive to irreparable mistaken identification that it constituted a denial of due process of law. The Court noted that the practice "has been widely condemned," <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S., at 302</a></span>, but it concluded that "a claimed violation of due process of law in the conduct of a confrontation depends on the totality of the circumstances surrounding it." <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Ibid.</a></span></i> In that case, showing Stovall to the victim's spouse "was imperative." The Court then quoted the observations of the Court of Appeals, <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/#735" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d 731, 735</a></span> (CA2 1966), to the effect that the spouse was the only person who could possibly exonerate the accused; that the hospital was not far from the courthouse and jail; that no one knew how long she might live; that she was not able to visit the jail; and that taking Stovall to the hospital room was the only feasible procedure, and, under the circumstances, "`the usual police station line-up . . . was out of the question.'" <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S., at 302</a></span>.</p>
<p><span class="star-pagination">*105</span> <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers, supra</a></span></i><i>,</i> decided in 1972, concerned a respondent who had been convicted in a Tennessee court of rape, on evidence consisting in part of the victim's visual and voice identification of Biggers at a station-house showup seven months after the crime. The victim had been in her assailant's presence for some time and had directly observed him indoors and under a full moon outdoors. She testified that she had "no doubt" that Biggers was her assailant. She previously had given the police a description of the assailant. She had made no identification of others presented at previous showups, lineups, or through photographs. On federal habeas, the District Court held that the confrontation was so suggestive as to violate due process. The Court of Appeals affirmed. This Court reversed on that issue, and held that the evidence properly had been allowed to go to the jury. The Court reviewed <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and certain later cases where it had considered the scope of due process protection against the admission of evidence derived from suggestive identification procedures, namely, <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968); <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span> (1969); and <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970).<sup>[8]</sup> The Court concluded that <span class="star-pagination">*106</span> general guidelines emerged from these cases "as to the relationship between suggestiveness and misidentification." The "admission of evidence of a showup without more does not violate due process." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198</a></span>. The Court expressed concern about the lapse of seven months between the crime and the confrontation and observed that this "would be a seriously negative factor in most cases." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#201" aria-description="Citation for case: Neil v. Biggers"><i>Id.,</i> at 201</a></span>. The "central question," however, was "whether under the `totality of the circumstances' the identification was reliable even though the confrontation procedure was suggestive." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers"><i>Id.,</i> at 199</a></span>. Applying that test, the Court found "no substantial likelihood of misidentification. The evidence was properly allowed to go to the jury." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#201" aria-description="Citation for case: Neil v. Biggers"><i>Id.,</i> at 201</a></span>.</p>
<p><i>Biggers</i> well might be seen to provide an unambiguous answer to the question before us: The admission of testimony concerning a suggestive and unnecessary identification procedure does not violate due process so long as the identification possesses sufficient aspects of reliability.<sup>[9]</sup> In one passage, <span class="star-pagination">*107</span> however, the Court observed that the challenged procedure occurred pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> and that a strict rule would make little sense with regard to a confrontation that preceded the Court's first indication that a suggestive procedure might lead to the exclusion of evidence. <i>Id.,</i> at 199. One perhaps might argue that, by implication, the Court suggested that a different rule could apply post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall.</i></a></span> The question before us, then, is simply whether the <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> analysis applies to post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontations as well to those pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall.</i></a></span></p>
<p></p>
<h2>III</h2>
<p>In the present case the District Court observed that the "sole evidence tying Brathwaite to the possession and sale of the heroin consisted in his identifications by the police undercover agent, Jimmy Glover." App. to Pet. for Cert. 6a. On the constitutional issue, the court stated that the first inquiry was whether the police used an impermissibly suggestive procedure in obtaining the out-of-court identification. If so, the second inquiry is whether, under all the circumstances, that suggestive procedure gave rise to a substantial likelihood of irreparable misidentification. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Id.,</a></span></i> at 9a. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> were cited. The court noted that in the Second Circuit, its controlling court, it was clear that "this type of identification procedure [display of a single photograph] is impermissibly <span class="star-pagination">*108</span> suggestive," and turned to the second inquiry. App. to Pet. for Cert. 9a. The factors <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> specified for consideration were recited and applied. The court concluded that there was no substantial likelihood of irreparable misidentification. It referred to the facts: Glover was within two feet of the seller. The duration of the confrontation was at least a "couple of minutes." There was natural light from a window or skylight and there was adequate light to see clearly in the hall. Glover "certainly was paying attention to identify the seller." <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Id.,</a></span></i> at 10a. He was a trained police officer who realized that later he would have to find and arrest the person with whom he was dealing. He gave a detailed description to D'Onofrio. The reliability of this description was supported by the fact that it enabled D'Onofrio to pick out a single photograph that was thereafter positively identified by Glover. Only two days elapsed between the crime and the photographic identification. Despite the fact that another eight months passed before the in-court identification, Glover had "no doubt" that Brathwaite was the person who had sold him heroin.</p>
<p>The Court of Appeals confirmed that the exhibition of the single photograph to Glover was "impermissibly suggestive," <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#366" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 366</a></span>, and felt that, in addition, "it was unnecessarily so." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#367" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of..."><i>Id.,</i> at 367</a></span>. There was no emergency and little urgency. The court said that prior to the decision in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> except in cases of harmless error, "a conviction secured as the result of admitting an identification obtained by impermissibly suggestive and unnecessary measures could not stand." <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Ibid.</a></span></i> It noted what it felt might be opposing inferences to be drawn from passages in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> but concluded that the case preserved the principle "requiring the exclusion of identifications resulting from `unnecessarily suggestive confrontation'" in post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> situations. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#368" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 368</a></span>. The court also concluded that for post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identifications, <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> had not changed the existing rule. Thus: "Evidence of an identification unnecessarily obtained by impermissibly <span class="star-pagination">*109</span> suggestive means must be excluded under <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> . . . . No rules less stringent than these can force police administrators and prosecutors to adopt procedures that will give fair assurance against the awful risks of misidentification." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 371</a></span>. Finally, the court said, even if this conclusion were wrong, the writ, nevertheless, should issue. It took judicial notice that on May 5, 1970, sunset at Hartford was at 7:53 p. m. It characterized Glover's duty as an undercover agent as one "to cause arrests to be made," and his description of the suspect as one that "could have applied to hundreds of Hartford black males." <i><span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">Ibid.</a></span></i> The in-court identification had "little meaning," for Brathwaite was at the counsel table. The fact that respondent was arrested in the very apartment where the sale was made was subject to a "not implausible" explanation from the respondent, "although evidently not credited by the jury." And the court was troubled by "the long and unexplained delay" in the arrest. It was too great a danger that the respondent was convicted because he was a man D'Onofrio had previously observed near the scene, was thought to be a likely offender, and was arrested when he was known to be in Mrs. Ramsey's apartment, rather than because Glover "really remembered him as the seller." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of..."><i>Id.,</i> at 371-372</a></span>.</p>
<p></p>
<h2>IV</h2>
<p>Petitioner at the outset acknowledges that "the procedure in the instant case was suggestive [because only one photograph was used] and unnecessary" [because there was no emergency or exigent circumstance]. Brief for Petitioner 10; Tr. of Oral Arg. 7. The respondent, in agreement with the Court of Appeals, proposes a <i>per se</i> rule of exclusion that he claims is dictated by the demands of the Fourteenth Amendment's guarantee of due process. He rightly observes that this is the first case in which this Court has had occasion to rule upon strictly post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> out-of-court identification evidence of the challenged kind.</p>
<p><span class="star-pagination">*110</span> Since the decision in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> the Courts of Appeals appear to have developed at least two approaches to such evidence. See Pulaski, <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>:</i> The Supreme Court Dismantles the <i>Wade</i> Trilogy's Due Process Protection, <span class="citation no-link">26 Stan. L. Rev. 1097</span>, 1111-1114 (1974). The first, or <i>per se</i> approach, employed by the Second Circuit in the present case, focuses on the procedures employed and requires exclusion of the out-of-court identification evidence, without regard to reliability, whenever it has been obtained through unnecessarily suggested confrontation procedures.<sup>[10]</sup> The justifications advanced are the elimination of evidence of uncertain reliability, deterrence of the police and prosecutors, and the stated "fair assurance against the awful risks of misidentification." <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 371</a></span>. See <i>Smith</i> v. <i>Coiner,</i> <span class="citation" data-id="308320"><a href="/opinion/308320/edward-lee-smith-v-ira-m-coiner-warden-of-the-west-virginia-state/#882" aria-description="Citation for case: Edward Lee Smith v. Ira M. Coiner, Warden of the West...">473 F. 2d 877, 882</a></span> (CA4), cert. denied <i>sub nom. </i><i>Wallace</i> v. <i>Smith,</i> <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/" aria-description="Citation for case: Wallace v. Smith">414 U. S. 1115</a></span> (1973).</p>
<p>The second, or more lenient, approach is one that continues to rely on the totality of the circumstances. It permits the admission of the confrontation evidence if, despite the suggestive aspect, the out-of-court identification possesses certain features of reliability. Its adherents feel that the <i>per se</i> approach is not mandated by the Due Process Clause of the Fourteenth Amendment. This second approach, in contrast to the other, is ad hoc and serves to limit the societal costs imposed by a sanction that excludes relevant evidence from consideration and evaluation by the trier of fact. See <i>United States ex rel. Kirby</i> v. <i>Sturges,</i> <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#407" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 407-408</a></span> (CA7) (opinion by Judge, now MR. JUSTICE, STEVENS), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./421/1016/">421 U. S. 1016</a></span> (1975); <i>Stanley</i> v. <i>Cox,</i> 486 F. 2d 48 <span class="star-pagination">*111</span> (CA4 1973), cert. denied <i>sub nom. Stanley</i> v. <i>Slayton,</i> <span class="citation" data-id="8990231"><a href="/opinion/8997836/stanley-v-slayton/" aria-description="Citation for case: Stanley v. Slayton">416 U. S. 958</a></span> (1974).<sup>[11]</sup></p>
<p>MR. JUSTICE STEVENS, in writing for the Seventh Circuit in <i><span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">Kirby, supra,</a></span></i> observed: "There is surprising unanimity among scholars in regarding such a rule [the <i>per se</i> approach] as essential to avoid serious risk of miscarriage of justice." <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#405" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d, at 405</a></span>. He pointed out that well-known federal judges have taken the position that "evidence of, or derived from, a showup identification should be inadmissible unless the prosecutor can justify his failure to use a more reliable identification procedure." <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#406" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R...."><i>Id.,</i> at 406</a></span>. Indeed, the ALI Model Code of Pre-Arraignment Procedure §§ 160.1 and 160.2 (1975) (hereafter Model Code) frowns upon the use of a showup or the display of only a single photograph.</p>
<p>The respondent here stresses the same theme and the need for deterrence of improper identification practice, a factor he regards as pre-eminent. Photographic identification, it is said, continues to be needlessly employed. He notes that the legislative regulation "the Court had hoped [<i>United States</i> v.] <i>Wade</i>[, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#239" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 239</a></span> (1967),] would engender," Brief for Respondent 15, has not been forthcoming. He argues that a totality rule cannot be expected to have a significant deterrent impact; only a strict rule of exclusion will have direct and immediate impact on law enforcement agents. Identification evidence is so convincing to the jury that sweeping exclusionary rules are required. Fairness of the trial is threatened by suggestive confrontation evidence, and thus, it is said, an exclusionary rule has an established constitutional predicate.</p>
<p>There are, of course, several interests to be considered and taken into account. The driving force behind <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), <i>Gilbert</i> v. <i>California,</i> 388 <span class="star-pagination">*112</span> U. S. 263 (1967) (right to counsel at a post-indictment lineup), and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> all decided on the same day, was the Court's concern with the problems of eyewitness identification. Usually the witness must testify about an encounter with a total stranger under circumstances of emergency or emotional stress. The witness' recollection of the stranger can be distorted easily by the circumstances or by later actions of the police. Thus, <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and its companion cases reflect the concern that the jury not hear eyewitness testimony unless that evidence has aspects of reliability. It must be observed that both approaches before us are responsive to this concern. The <i>per se</i> rule, however, goes too far since its application automatically and peremptorily, and without consideration of alleviating factors, keeps evidence from the jury that is reliable and relevant.</p>
<p>The second factor is deterrence. Although the <i>per se</i> approach has the more significant deterrent effect, the totality approach also has an influence on police behavior. The police will guard against unnecessarily suggestive procedures under the totality rule, as well as the <i>per se</i> one, for fear that their actions will lead to the exclusion of identifications as unreliable.<sup>[12]</sup></p>
<p>The third factor is the effect on the administration of justice. Here the <i>per se</i> approach suffers serious drawbacks. Since it denies the trier reliable evidence, it may result, on occasion, in the guilty going free. Also, because of its rigidity, the <i>per se</i> approach may make error by the trial judge more likely than the totality approach. And in those cases in which the admission of identification evidence is error under the <i>per se</i> approach but not under the totality approach <span class="star-pagination">*113</span> cases in which the identification is reliable despite an unnecessarily suggestive identification procedurereversal is a Draconian sanction.<sup>[13]</sup> Certainly, inflexible rules of exclusion that may frustrate rather than promote justice have not been viewed recently by this Court with unlimited enthusiasm. See, for example, the several opinions in <i>Brewer</i> v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977). See also <i>United States</i> v. <i>Janis,</i> <span class="citation" data-id="9426584"><a href="/opinion/109539/united-states-v-janis/" aria-description="Citation for case: United States v. Janis">428 U. S. 433</a></span> (1976).</p>
<p>It is true, as has been noted, that the Court in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> referred to the pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> character of the confrontation in that case. <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 199</a></span>. But that observation was only one factor in the judgmental process. It does not translate into a holding that post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontation evidence automatically is to be excluded.</p>
<p>The standard, after all, is that of fairness as required by the Due Process Clause of the Fourteenth Amendment. See <i>United States</i> v. <i>Lovasco,</i> <span class="citation" data-id="9426843"><a href="/opinion/109682/united-states-v-lovasco/#790" aria-description="Citation for case: United States v. Lovasco">431 U. S. 783, 790</a></span> (1977); <i>Rochin</i> v. <i>California,</i> <span class="citation" data-id="9420649"><a href="/opinion/104943/rochin-v-california/#170" aria-description="Citation for case: Rochin v. California">342 U. S. 165, 170-172</a></span> (1952). <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> with its reference to "the totality of the circumstances," 388 U. S., at 302, and <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> with its continuing stress on the same totality, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 199</a></span>, did not, singly or together, establish a strict exclusionary rule or new standard of due process. Judge Leventhal, although speaking pre-<span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers"><i>Biggers</i></a></span> and of a pre-<span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade"><i>Wade</i></a></span> situation, correctly has described <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> as protecting an <i>evidentiary</i> interest and, at the same time, as recognizing the limited extent of that interest in our adversary system.<sup>[14]</sup></p>
<p><span class="star-pagination">*114</span> We therefore conclude that reliability is the linchpin in determining the admissibility of identification testimony for both pre- and post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontations. The factors to be considered are set out in <i>Biggers.</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 199-200</a></span>. These include the opportunity of the witness to view the criminal at the time of the crime, the witness' degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation. Against these factors is to be weighed the corrupting effect of the suggestive identification itself.</p>
<p></p>
<h2>V</h2>
<p>We turn, then, to the facts of this case and apply the analysis:</p>
<p>1. The opportunity to view. Glover testified that for two to three minutes he stood at the apartment door, within two feet of the respondent. The door opened twice, and each time the man stood at the door. The moments passed, the conversation took place, and payment was made. Glover looked directly at his vendor. It was near sunset, to be sure, but the sun had not yet set, so it was not dark or even dusk or twilight. Natural light from outside entered the hallway through a window. There was natural light, as well, from inside the apartment.</p>
<p><span class="star-pagination">*115</span> 2. The degree of attention. Glover was not a casual or passing observer, as is so often the case with eyewitness identification. Trooper Glover was a trained police officer on dutyand specialized and dangerous dutywhen he called at the third floor of 201 Westland in Hartford on May 5, 1970. Glover himself was a Negro and unlikely to perceive only general features of "hundreds of Hartford black males," as the Court of Appeals stated. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#371" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 371</a></span>. It is true that Glover's duty was that of ferreting out narcotics offenders and that he would be expected in his work to produce results. But it is also true that, as a specially trained, assigned, and experienced officer, he could be expected to pay scrupulous attention to detail, for he knew that subsequently he would have to find and arrest his vendor. In addition, he knew that his claimed observations would be subject later to close scrutiny and examination at any trial.</p>
<p>3. The accuracy of the description. Glover's description was given to D'Onofrio within minutes after the transaction. It included the vendor's race, his height, his build, the color and style of his hair, and the high cheekbone facial feature. It also included clothing the vendor wore. No claim has been made that respondent did not possess the physical characteristics so described. D'Onofrio reacted positively at once. Two days later, when Glover was alone, he viewed the photograph D'Onofrio produced and identified its subject as the narcotics seller.</p>
<p>4. The witness' level of certainty. There is no dispute that the photograph in question was that of respondent. Glover, in response to a question whether the photograph was that of the person from whom he made the purchase, testified: "There is no question whatsoever." Tr. 38. This positive assurance was repeated. <i>Id.,</i> at 41-42.</p>
<p>5. The time between the crime and the confrontation. Glover's description of his vendor was given to D'Onofrio <span class="star-pagination">*116</span> within minutes of the crime. The photographic identification took place only two days later. We do not have here the passage of weeks or months between the crime and the viewing of the photograph.</p>
<p>These indicators of Glover's ability to make an accurate identification are hardly outweighed by the corrupting effect of the challenged identification itself. Although identifications arising from single-photograph displays may be viewed in general with suspicion, see <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383</a></span>, we find in the instant case little pressure on the witness to acquiesce in the suggestion that such a display entails. D'Onofrio had left the photograph at Glover's office and was not present when Glover first viewed it two days after the event. There thus was little urgency and Glover could view the photograph at his leisure. And since Glover examined the photograph alone, there was no coercive pressure to make an identification arising from the presence of another. The identification was made in circumstances allowing care and reflection.</p>
<p>Although it plays no part in our analysis, all this assurance as to the reliability of the identification is hardly undermined by the facts that respondent was arrested in the very apartment where the sale had taken place, and that he acknowledged his frequent visits to that apartment.<sup>[15]</sup></p>
<p>Surely, we cannot say that under all the circumstances of this case there is "a very substantial likelihood of irreparable misidentification." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States"><i>Id.,</i> at 384</a></span>. Short of that point, such evidence is for the jury to weigh. We are content to rely upon the good sense and judgment of American juries, for evidence with some element of untrustworthiness is customary grist for the jury mill. Juries are not so susceptible that they cannot measure intelligently the weight of identification testimony that has some questionable feature.</p>
<p><span class="star-pagination">*117</span> Of course, it would have been better had D'Onofrio presented Glover with a photographic array including "so far as practicable . . . a reasonable number of persons similar to any person then suspected whose likeness is included in the array." Model Code § 160.2 (2). The use of that procedure would have enhanced the force of the identification at trial and would have avoided the risk that the evidence would be excluded as unreliable. But we are not disposed to view D'Onofrio's failure as one of constitutional dimension to be enforced by a rigorous and unbending exclusionary rule. The defect, if there be one, goes to weight and not to substance.<sup>[16]</sup></p>
<p>We conclude that the criteria laid down in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> are to be applied in determining the admissibility of evidence offered by the prosecution concerning a post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identification, and that those criteria are satisfactorily met and complied with here.</p>
<p>The judgment of the Court of Appeals is reversed.</p>
<p><i>It is so ordered.</i></p>
<p>MR. JUSTICE STEVENS, concurring.</p>
<p>While I join the Court's opinion, I would emphasize two points.</p>
<p>First, as I indicated in my opinion in <i>United States ex rel. Kirby</i> v. <i>Sturges,</i> <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#405" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 405-406</a></span> (CA7 1975), the arguments in favor of fashioning new rules to minimize the danger of convicting the innocent on the basis of unreliable eyewitness testimony carry substantial force. Nevertheless, <span class="star-pagination">*118</span> for the reasons stated in that opinion, as well as those stated by the Court today, I am persuaded that this rulemaking function can be performed "more effectively by the legislative process than by a somewhat clumsy judicial fiat," <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#408" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R...."><i>id.,</i> at 408</a></span>, and that the Federal Constitution does not foreclose experimentation by the States in the development of such rules.</p>
<p>Second, in evaluating the admissibility of particular identification testimony it is sometimes difficult to put other evidence of guilt entirely to one side.<sup>[*]</sup> MR. JUSTICE BLACKMUN'S opinion for the Court carefully avoids this pitfall and correctly relies only on appropriate indicia of the reliability of the identification itself. Although I consider the factual question in this case extremely close, I am persuaded that the Court has resolved it properly.</p>
<p>MR. JUSTICE MARSHALL, with whom MR. JUSTICE BRENNAN joins, dissenting.</p>
<p>Today's decision can come as no surprise to those who have been watching the Court dismantle the protections against mistaken eyewitness testimony erected a decade ago in <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967); <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967); and <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span> (1967). But it is still distressing to see the Court virtually ignore the teaching of experience embodied in those decisions and blindly uphold the conviction of a defendant who may well be innocent.</p>
<p></p>
<h2>
<span class="star-pagination">*119</span> I</h2>
<p>The magnitude of the Court's error can be seen by analyzing the cases in the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> trilogy and the decisions following it. The foundation of the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> trilogy was the Court's recognition of the "high incidence of miscarriage of justice" resulting from the admission of mistaken eyewitness identification evidence at criminal trials. <i>United States</i> v. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade"><i>Wade, supra,</i> at 228</a></span>. Relying on numerous studies made over many years by such scholars as Professor Wigmore and Mr. Justice Frankfurter, the Court concluded that "[t]he vagaries of eyewitness identification are well-known; the annals of criminal law are rife with instances of mistaken identification." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i> It is, of course, impossible to control one source of such errorsthe faulty perceptions and unreliable memories of witnessesexcept through vigorously contested trials conducted by diligent counsel and judges. The Court in the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> cases acted, however, to minimize the more preventable threat posed to accurate identification by "the degree of suggestion inherent in the manner in which the prosecution presents the suspect to witnesses for pretrial identification." <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Ibid.</a></span></i></p>
<p>The Court did so in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert</i> v. <i>California</i> by prohibiting the admission at trial of evidence of pretrial confrontations at which an accused was not represented by counsel. Further protection was afforded by holding that an in-court identification following an uncounseled lineup was allowable only if the prosecution could clearly and convincingly demonstrate that it was not tainted by the constitutional violation. Only in this way, the Court held, could confrontations fraught with the danger of misidentification be made fairer, and could Sixth Amendment rights to assistance of counsel and confrontation of witnesses at trial be effectively preserved. The crux of the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> decisions, however, was the unusual threat to the truth-seeking process posed by the frequent untrustworthiness of eyewitness identification <span class="star-pagination">*120</span> testimony. This, combined with the fact that juries unfortunately are often unduly receptive to such evidence,<sup>[1]</sup> is the fundamental fact of judicial experience ignored by the Court today.</p>
<p><i>Stovall</i> v. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Denno</a></span></i><i>,</i> while holding that the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> prophylactic rules were not retroactive, was decided at the same time and reflects the same concerns about the reliability of identification testimony. <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> recognized that, regardless of Sixth Amendment principles, "the conduct of a confrontation" may be "so unnecessarily suggestive and conducive to irreparable mistaken identification" as to deny due process of law. 388 U. S., at 301-302. The pretrial confrontation in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> was plainly suggestive,<sup>[2]</sup> and evidence of it was introduced at trial along with the witness' in-court identification. The Court ruled that there had been no violation of due process, however, because the unusual necessity for the procedure<sup>[3]</sup> outweighed the danger of suggestion.</p>
<p><i>Stovall</i> thus established a due proceess right of criminal suspects to be free from confrontations that, under all the circumstances, are unnecessarily suggestive. The right was enforceable by exclusion at trial of evidence of the constitutionally invalid identification. Comparison with <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert</i> confirms this interpretation. Where their Sixth <span class="star-pagination">*121</span> Amendment holding did not apply, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> found an analogous Fourteenth Amendment right to a lineup conducted in a fundamentally fair manner. This interpretation is reinforced by the Court's statement that "a claimed violation of due process of law <i>in the conduct of a confrontation</i> depends on the totality of the circumstances surrounding it." 388 U. S., at 302 (emphasis added). Significantly, several years later, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> was viewed in precisely the same way, even as the Court limited <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i>Gilbert</i> to post-indictment confrontations: "The Due Process Clause . . . <i>forbids a lineup</i> that is unnecessarily suggestive and conducive to irreparable mistaken identification. <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U. S. 293</a></span>; <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span>." <i>Kirby</i> v. <i>Illinois,</i> <span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#691" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 691</a></span> (1972) (emphasis added).<sup>[4]</sup></p>
<p>The development of due process protections against mistaken identification evidence, begun in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> was continued in <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U. S. 377</a></span> (1968). There, the Court developed a different rule to deal with the admission of in-court identification testimony that the accused claimed had been fatally tainted by a previous suggestive confrontation. In <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> the exclusionary effect of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> had already been accomplished, since the prosecution made no use of the suggestive confrontation. <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> therefore, did not deal with the constitutionality of the pretrial identification procedure. The only question was the impact of the <span class="star-pagination">*122</span> Due Process Clause on an in-court identification that was not itself unnecessarily suggestive. <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> held that due process was violated by the later identification if the pretrial procedure had been "so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. This test focused, not on the necessity for the challenged pretrial procedure, but on the degree of suggestiveness that it entailed. In applying this test, the Court understandably considered the circumstances surrounding the witnesses' initial opportunity to view the crime. Finding that any suggestion in the pretrial confrontation had not affected the fairness of the in-court identification, <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> rejected petitioner's due process attack on his conviction.</p>
<p>Again, comparison with the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> cases is instructive. The inquiry mandated by <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> is similar to the independent-source test used in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> where an in-court identification is sought following an uncounseled lineup. In both cases, the issue is whether the witness is identifying the defendant solely on the basis of his memory of events at the time of the crime, or whether he is merely remembering the person he picked out in a pretrial procedure. Accordingly, in both situations, the relevant inquiry includes factors bearing on the accuracy of the witness' identification, including his opportunity to view the crime.</p>
<p>Thus, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> established two different due process tests for two very different situations. Where the prosecution sought to use evidence of a questionable pretrial identification, <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> required its exclusion, because due process had been violated by the confrontation, unless the necessity for the unduly suggestive procedure outweighed its potential for generating an irreparably mistaken identification. The <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> test, on the other hand, was directed to ascertaining due process violations in the introduction of in-court identification testimony that the defendant claimed was tainted by pretrial procedures. In the latter situation, a <span class="star-pagination">*123</span> court could consider the reliability of the identification under all the circumstances.<sup>[5]</sup></p>
<p>This distinction between <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> was preserved in two succeeding cases. <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U. S. 440</a></span> (1969), like <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> involved both unduly suggestive pretrial procedures, evidence of which was introduced at trial, and a tainted in-court identification. Accordingly, <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span></i> applied the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> test, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#442" aria-description="Citation for case: Foster v. California">394 U. S., at 442</a></span>, and held that the police "<i>procedure</i> so undermined the reliability of the eyewitness identification as to violate due process." <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California"><i>Id.,</i> at 443</a></span> (emphasis added). In contrast, in <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1</a></span> (1970), where the witness' pretrial identification was not used to bolster his in-court identification, the plurality opinion applied the test enunciated in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>.</i> It concluded that an in-court identification did not violate due process because it did not stem from an allegedly suggestive lineup.</p>
<p>The Court inexplicably seemed to erase the distinction between <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> situations in <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span> (1972). In <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> there was a pretrial confrontation that was clearly both suggestive and unnecessary.<sup>[6]</sup> Evidence of this, together with an in-court identification, was admitted at trial. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> was, in short, a case plainly cast in the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> mold. Yet the Court, without explanation or apparent recognition of the distinction, applied the <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> <span class="star-pagination">*124</span> test. The Court stated: "[T]he primary evil to be avoided is `a very substantial likelihood of irreparable misidentification.' <i>Simmons</i> v. <i>United States,</i> <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. . . . It is the likelihood of misidentification which violates a defendant's right to due process . . . ." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198</a></span>. While this statement accurately describes the lesson of <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> it plainly ignores the teaching of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span></i> that an unnecessarily suggestive pretrial confrontation itself violates due process.</p>
<p>But the Court did not simply disregard the due process analysis of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i> It went on to take the <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> standard for assessing the constitutionality of an in-court identification "`a very substantial likelihood of irreparable misidentification'" and transform it into the "standard for the admissibility of testimony concerning [an] out-of-court identification." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198</a></span>. It did so by deleting the word "irreparable" from the <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> formulation. This metamorphosis could be accomplished, however, only by ignoring the fact that <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> fortified only months earlier by <i>Kirby</i> v. <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Illinois</a></span>,</i> see <i>supra,</i> at 121, had established a test for precisely the same situation that focused on the need for the suggestive procedure. It is not surprising that commentators almost unanimously mourned the demise of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> in the <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> decision.<sup>[7]</sup></p>
<p></p>
<h2>II</h2>
<p>Apparently, the Court does not consider <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> controlling in this case. I entirely agree, since I believe that <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> <span class="star-pagination">*125</span> was wrongly decided. The Court, however, concludes that <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> is distinguishable because it, like the identification decisions that preceded it, involved a pre-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontation, and because a paragraph in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> itself, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 198-199</a></span>, seems to distinguish between pre- and post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> confrontations. Accordingly, in determining the admissibility of the post-<span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno"><i>Stovall</i></a></span> identification in this case, the Court considers two alternatives, a <i>per se</i> exclusionary rule and a totality-of-the-circumstances approach. <i>Ante,</i> at 110-111. The Court weighs three factors in deciding that the totality approach, which is essentially the test used in <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> should be applied. <i>Ante,</i> at 111-113. In my view, the Court wrongly evaluates the impact of these factors.</p>
<p>First, the Court acknowledges that one of the factors, deterrence of police use of unnecessarily suggestive identification procedures, favors the <i>per se</i> rule. Indeed, it does so heavily, for such a rule would make it unquestionably clear to the police they must never use a suggestive procedure when a fairer alternative is available. I have no doubt that conduct would quickly conform to the rule.</p>
<p>Second, the Court gives passing consideration to the dangers of eyewitness identification recognized in the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> trilogy. It concludes, however, that the grave risk of error does not justify adoption of the <i>per se</i> approach because that would too often result in exclusion of relevant evidence. In my view, this conclusion totally ignores the lessons of <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>.</i> The dangers of mistaken identification are, as <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> held, simply too great to permit unnecessarily suggestive identifications. Neither <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> nor the Court's opinion today points to any contrary empirical evidence. Studies since <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> have only reinforced the validity of its assessment of the dangers of identification testimony.<sup>[8]</sup> While the Court is "content to <span class="star-pagination">*126</span> rely on the good sense and judgment of American juries," <i>ante,</i> at 116, the impetus for <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> was repeated miscarriages of justice resulting from juries' willingness to credit inaccurate eyewitness testimony.</p>
<p>Finally, the Court errs in its assessment of the relative impact of the two approaches on the administration of justice. The Court relies most heavily on this factor, finding that "reversal is a Draconian sanction" in cases where the identification is reliable despite an unnecessarily suggestive procedure used to obtain it. Relying on little more than a strong distaste for "inflexible rules of exclusion," the Court rejects the <i>per se</i> test. <i>Ante,</i> at 113. In so doing, the Court disregards two significant distinctions between the <i>per se</i> rule advocated in this case and the exclusionary remedies for certain other constitutional violations.</p>
<p>First, the <i>per se</i> rule here is not "inflexible." Where evidence is suppressed, for example, as the fruit of an unlawful search, it may well be forever lost to the prosecution. Identification evidence, however, can by its very nature be readily and effectively reproduced. The in-court identification, permitted under <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> and <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> if it has a source independent of an uncounseled or suggestive procedure, is one example. Similarly, when a prosecuting attorney learns that there has been a suggestive confrontation, he can easily arrange another <span class="star-pagination">*127</span> lineup conducted under scrupulously fair conditions. Since the same factors are evaluated in applying both the Court's totality test and the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i>-<span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States"><i>Simmons</i></a></span> independent-source inquiry, any identification which is "reliable" under the Court's test will support admission of evidence concerning such a fairly conducted lineup. The evidence of an additional, properly conducted confrontation will be more persuasive to a jury, thereby increasing the chance of a justified conviction where a reliable identification was tainted by a suggestive confrontation. At the same time, however, the effect of an unnecessarily suggestive identificationwhich has no value whatsoever in the law enforcement processwill be completely eliminated.</p>
<p>Second, other exclusionary rules have been criticized for preventing jury consideration of relevant and usually reliable evidence in order to serve interests unrelated to guilt or innocence, such as discouraging illegal searches or denial of counsel. Suggestively obtained eyewitness testimony is excluded, in contrast, precisely because of its unreliability and concomitant irrelevance. Its exclusion both protects the integrity of the truth-seeking function of the trial and discourages police use of needlessly inaccurate and ineffective investigatory methods.</p>
<p>Indeed, impermissibly suggestive identifications are not merely worthless law enforcement tools. They pose a grave threat to society at large in a more direct way than most governmental disobedience of the law, see <i>Olmstead</i> v. <i>United States,</i> <span class="citation" data-id="9418652"><a href="/opinion/101320/olmstead-v-united-states/#471" aria-description="Citation for case: Olmstead v. United States">277 U. S. 438, 471, 485</a></span> (1928) (Brandeis, J., dissenting). For if the police and the public erroneously conclude, on the basis of an unnecessarily suggestive confrontation, that the right man has been caught and convicted, the real outlaw must still remain at large. Law enforcement has failed in its primary function and has left society unprotected from the depredations of an active criminal.</p>
<p><span class="star-pagination">*128</span> For these reasons, I conclude that adoption of the <i>per se</i> rule would enhance, rather than detract from, the effective administration of justice. In my view, the Court's totality test will allow seriously unreliable and misleading evidence to be put before juries. Equally important, it will allow dangerous criminals to remain on the streets while citizens assume that police action has given them protection. According to my calculus, all three of the factors upon which the Court relies point to acceptance of the <i>per se</i> approach.</p>
<p>Even more disturbing than the Court's reliance on the totality test, however, is the analysis it uses, which suggests a reinterpretation of the concept of due process of law in criminal cases. The decision suggests that due process violations in identification procedures may not be measured by whether the government employed procedures violating standards of fundamental fairness. By relying on the probable accuracy of a challenged identification, instead of the necessity for its use, the Court seems to be ascertaining whether the defendant was probably guilty. Until today, I had thought that "Equal justice under law" meant that the existence of constitutional violations did not depend on the race, sex, religion, nationality, or likely guilt of the accused. The Due Process Clause requires adherence to the same high standard of fundamental fairness in dealing with every criminal defendant, whatever his personal characteristics and irrespective of the strength of the State's case against him. Strong evidence that the defendant is guilty should be relevant only to the determination whether an error of constitutional magnitude was nevertheless harmless beyond a reasonable doubt. See <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967). By importing the question of guilt into the initial determination of whether there was a constitutional violation, the apparent effect of the Court's decision is to undermine the protection afforded by the Due Process Clause. "It is therefore important to note that the state courts remain free, in interpreting state constitutions, to <span class="star-pagination">*129</span> guard against the evil clearly identified by this case." <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#499" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 499</a></span> (1977) (MARSHALL, J., dissenting).<sup>[9]</sup></p>
<p></p>
<h2>III</h2>
<p>Despite my strong disagreement with the Court over the proper standards to be applied in this case, I am pleased that its application of the totality test does recognize the continuing vitality of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i> In assessing the reliability of the identification, the Court mandates weighing "the corrupting effect of the suggestive identification itself" against the "indicators of [a witness'] ability to make an accurate identification." <i>Ante,</i> at 114, 116. The Court holds, as <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> failed to, that a due process identification inquiry must take account of the suggestiveness of a confrontation and the likelihood that it led to misidentification, as recognized in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> and <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>.</i> Thus, even if a witness did have an otherwise adequate opportunity to view a criminal, the later use of a highly suggestive identification procedure can render his testimony inadmissible. Indeed, it is my view that, assuming applicability of the totality test enunciated by the Court, the facts of the present case require that result.</p>
<p>I consider first the opportunity that Officer Glover had to view the suspect. Careful review of the record shows that he could see the heroin seller only for the time it took to speak three sentences of four or five short words, to hand over some money, Tr. 29-30, and later after the door reopened, to receive the drugs in return, <i>id.,</i> at 30, 31-32. The entire face-to-face transaction could have taken as little as 15 or 20 seconds. But during this time, Glover's attention was not focused exclusively on the seller's face. He observed that the door <span class="star-pagination">*130</span> was opened 12 to 18 inches, <i>id.,</i> at 29, that there was a window in the room behind the door, <i>id.,</i> at 33, and, most importantly, that there was a woman standing behind the man, <i>id.,</i> at 29, 30. Glover was, of course, also concentrating on the details of the transactionhe must have looked away from the seller's face to hand him the money and receive the drugs. The observation during the conversation thus may have been as brief as 5 or 10 seconds.</p>
<p>As the Court notes, Glover was a police officer trained in and attentive to the need for making accurate identifications. Nevertheless, both common sense and scholarly study indicate that while a trained observer such as a police officer "is somewhat less likely to make an erroneous identification than the average untrained observer, the mere fact that he has been so trained is no guarantee that he is correct in a specific case. His identification testimony should be scrutinized just as carefully as that of the normal witness." <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 14; see also Levine &amp; Tapp, <i>supra,</i> n. 8, at 1088. Moreover, "identifications made by policemen in highly competitive activities, such as undercover narcotic agents . . . , should be scrutinized with special care." <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 14. Yet it is just such a searching inquiry that the Court fails to make here.</p>
<p>Another factor on which the Court reliesthe witness' degree of certainty in making the identificationis worthless as an indicator that he is correct.<sup>[10]</sup> Even if Glover had been unsure initially about his identification of respondent's picture, by the time he was called at trial to present a key piece of evidence for the State that paid his salary, it is impossible to imagine his responding negatively to such questions as "is there any doubt in your mind whatsoever" that the identification was correct. Tr. 34, 41-42. As the Court noted in <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span>:</i> "`It is a matter of common experience that, once a <span class="star-pagination">*131</span> witness has picked out the accused at the [pretrial confrontation], he is not likely to go back on his word later on.'" 388 U. S., at 229, quoting Williams &amp; Hammelmann, Identification ParadesI, Crim. L. Rev. 479, 482 (1963).</p>
<p>Next, the Court finds that because the identification procedure took place two days after the crime, its reliability is enhanced. While such temporal proximity makes the identification more reliable than one occurring months later, the fact is that the greatest memory loss occurs within hours after an event. After that, the dropoff continues much more slowly.<sup>[11]</sup> Thus, the reliability of an identification is increased only if it was made within several hours of the crime. If the time gap is any greater, reliability necessarily decreases.</p>
<p>Finally, the Court makes much of the fact that Glover gave a description of the seller to D'Onofrio shortly after the incident. Despite the Court's assertion that because "Glover himself was a Negro and unlikely to perceive only general features of `hundreds of Hartford black males,' as the Court of Appeals stated," <i>ante,</i> at 115, the description given by Glover was actually no more than a general summary of the seller's appearance. See <i>ante,</i> at 101. We may discount entirely the seller's clothing, for that was of no significance later in the proceeding. Indeed, to the extent that Glover noticed clothes, his attention was diverted from the seller's face. Otherwise, Glover merely described vaguely the seller's height, skin color, hairstyle, and build. He did say that the <span class="star-pagination">*132</span> seller had "high cheekbones," but there is no other mention of facial features, nor even an estimate of age. Conspicuously absent is any indication that the seller was a native of the West Indies, certainly something which a member of the black community could immediately recognize from both appearance and accent.<sup>[12]</sup></p>
<p>From all of this, I must conclude that the evidence of Glover's ability to make an accurate identification is far weaker than the Court finds it. In contrast, the procedure used to identify respondent was both extraordinarily suggestive and strongly conducive to error. In dismissing "the corrupting effect of the suggestive identification" procedure here, <i>ante,</i> at 116, the Court virtually grants the police license to convict the innocent. By displaying a single photograph of respondent to the witness Glover under the circumstances in this record almost everything that could have been done wrong was done wrong.</p>
<p>In the first place, there was no need to use a photograph at all. Because photos are static, two-dimensional, and often outdated, they are "clearly inferior in reliability" to corporeal procedures. <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 70; <i>People</i> v. <i>Gould,</i> <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#631" aria-description="Citation for case: People v. Gould">54 Cal. 2d 621, 631</a></span>, <span class="citation" data-id="1801408"><a href="/opinion/1801408/people-v-gould/#870" aria-description="Citation for case: People v. Gould">354 P. 2d 865, 870</a></span> (1960). While the use of photographs is justifiable and often essential where the police have no knowledge of an offender's identity, the poor reliability of photos makes their use inexcusable where any other means of identification is available. Here, since Detective D'Onofrio believed that he knew the seller's identity, see <i>ante,</i> at 101, 115, further investigation without resort to a photographic showup was easily possible. With little inconvenience, a corporeal <span class="star-pagination">*133</span> lineup including Brathwaite might have been arranged.<sup>[13]</sup> Properly conducted, such a procedure would have gone far to remove any doubt about the fairness and accuracy of the identification.<sup>[14]</sup></p>
<p>Worse still than the failure to use an easily available corporeal identification was the display to Glover of only a single picture, rather than a photo array. With good reason, such single-suspect procedures have "been widely condemned." <i>Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno">388 U. S., at 302</a></span>. They give no assurance that the witness can identify the criminal from among a number of persons of similar appearance, surely the strongest evidence that there was no misidentification. In <i>Simmons</i> v. <i>United States</i><i>,</i> our first decision involving photographic identification, we recognized the danger that a witness seeing a suggestively displayed picture will "retain in his memory the image of the photograph rather than of the person actually seen." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383-384</a></span>. "Subsequent identification of the accused then shows nothing except that the picture was a good likeness." Williams &amp; Hammelmann, <i>supra,</i> n. 1, at 484. As <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> warned, the danger of error is at its greatest when "the police display to the witness only the picture of a single individual . . . [and] is also heightened if the police indicate to the witness that they have other evidence that . . . the perso[n] pictured committed the crime." <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383</a></span>. <span class="star-pagination">*134</span> See also ALI, Model Code of Pre-Arraignment Procedure §§ 160.2 (2), (5) (1975).</p>
<p>The use of a single picture (or the display of a single live suspect, for that matter) is a grave error, of course, because it dramatically suggests to the witness that the person shown must be the culprit. Why else would the police choose the person? And it is deeply ingrained in human nature to agree with the expressed opinions of othersparticularly others who should be more knowledgeablewhen making a difficult decision.<sup>[15]</sup> In this case, moreover, the pressure was not limited to that inherent in the display of a single photograph. Glover, the identifying witness, was a state police officer on special assignment. He knew that D'Onofrio, an experienced Hartford narcotics detective, presumably familiar with local drug operations, believed respondent to be the seller. There was at work, then, both loyalty to another police officer and deference to a better-informed colleague.<sup>[16]</sup> Finally, of course, there was Glover's knowledge that without an identification <span class="star-pagination">*135</span> and arrest, government funds used to buy heroin had been wasted.</p>
<p>The Court discounts this overwhelming evidence of suggestiveness, however. It reasons that because D'Onofrio was not present when Glover viewed the photograph, there was "little pressure on the witness to acquiesce in the suggestion." <i>Ante,</i> at 116. That conclusion blinks psychological reality.<sup>[17]</sup> There is no doubt in my mind that even in D'Onofrio's absence, a clear and powerful message was telegraphed to Glover as he looked at respondent's photograph. He was emphatically told that "<i>this</i> is the man," and he responded by identifying respondent then and at trial "whether or not he was in fact `the man.'" <i>Foster</i> v. <i>California,</i> <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California">394 U. S., at 443</a></span>.<sup>[18]</sup></p>
<p>I must conclude that this record presents compelling evidence that there was "a very substantial likelihood of misidentification" of respondent Brathwaite. The suggestive <span class="star-pagination">*136</span> display of respondent's photograph to the witness Glover likely erased any independent memory that Glover had retained of the seller from his barely adequate opportunity to observe the criminal.</p>
<p></p>
<h2>IV</h2>
<p>Since I agree with the distinguished panel of the Court of Appeals that the legal standard of <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> should govern this case, but that even if it does not, the facts here reveal a substantial likelihood of misidentification in violation of respondent's right to due process of law, I would affirm the grant of habeas corpus relief. Accordingly, I dissent from the Court's reinstatement of respondent's conviction.</p>
<h2>NOTES</h2>
<p>[1]  The references are to the transcript of the trial in the Superior Court of Hartford County, Conn. The United States District Court, on federal habeas, pursuant to agreement of the parties, Tr. of Oral Arg. 23, conducted no evidentiary hearing.</p>
<p>[2]  It appears that the door on which Glover knocked may not have been that of the Cicero apartment. Petitioner concedes, in any event, that the transaction effected "was with some other person than had been intended." <i>Id.,</i> at 4.</p>
<p>[3]  This was Glover's testimony. Brown later was called as a witness for the prosecution. He testified on direct examination that, due to his then use of heroin, he had no clear recollection of the details of the incident. Tr. 81-82. On cross-examination, as in an interview with defense counsel the preceding day, he said that it was a woman who opened the door, received the money, and thereafter produced the narcotics. <i>Id.,</i> at 84, 86-87. On redirect, he acknowledged that he was using heroin daily at the time, that he had had some that day, and that there was "an inability to recall and remember events." <i>Id.,</i> at 88-89.</p>
<p>[4]  Respondent testified: "Lots of times I have been there before in that building." He also testified that Mrs. Ramsey was a friend of his wife, that her apartment was the only one in the building he ever visited, and that he and his family, consisting of his wife and five children, did not live there but at 453 Albany Avenue, Hartford. <i>Id.,</i> at 111-113.</p>
<p>[5]  These statutes have since been amended in ways that do not affect the present litigation. See <span class="citation no-link">1971 Conn. Pub. Acts 812</span>, § 1; <span class="citation no-link">1972 Conn. Pub. Acts 278</span>, §§ 25 and 26; Conn. Pub. Acts 73-137, § 10; Conn. Pub. Acts 74-332, §§ 1 and 3; Conn. Pub. Acts 75-567, § 65.</p>
<p>[6]  Neither party submitted a request to the District Court for an independent factual hearing on respondent's claims. See n. 1, <i>supra.</i></p>
<p>[7]  Although no objection was made in the state trial to the admission of the identification testimony and the photograph, the issue of their propriety as evidence was raised on the appeal to the Supreme Court of Connecticut. Petitioner has asserted no claims related to the failure of the respondent either to exhaust state remedies or to make contemporaneous objections. The District Court and the Court and the Court of Appeals, each for a somewhat different reason, App. to Pet. for Cert. 7a-8a; <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#366" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 366</a></span>, concluded that the merits were properly before them. We are not inclined now to rule otherwise.</p>
<p>[8]  <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> involved photographs, mostly group ones, shown to bank-teller victims who made in-court identifications. The Court discussed the "chance of misidentification," <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#383" aria-description="Citation for case: Simmons v. United States">390 U. S., at 383</a></span>; declined to prohibit the procedure "either in the exercise of our supervisory power or, still less, as a matter of constitutional requirement," <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States"><i>id.,</i> at 384</a></span>; and held that each case must be considered on its facts and that a conviction would be set aside only if the identification procedure "was so impermissibly suggestive as to give rise to a very substantial likelihood of irreparable misidentification." <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Ibid.</a></span></i> The out-of-court identification was not offered. Mr. Justice Black would have denied Simmons' due process claim as frivolous. <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#395" aria-description="Citation for case: Simmons v. United States"><i>Id.,</i> at 395-396</a></span>.
</p>
<p><i>Foster</i> concerned repeated confrontations between a suspect and the manager of an office that had been robbed. At a second lineup, but not at the first and not at a personal one-to-one confrontation, the manager identified the suspect. At trial he testified as to this and made an in-court identification. The Court reaffirmed the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> standard and then concluded that the repeated confrontations were so suggestive as to violate due process. The case was remanded for the state courts to consider the question of harmless error.</p>
<p>In <i><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span></i> a plurality of the Court was of the view that the trial court did not err when it found that the victim's in-court identifications did not stem from a lineup procedure so impermissibly suggestive as to give rise to a substantial likelihood of misidentification. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#5" aria-description="Citation for case: Coleman v. Alabama">399 U. S., at 5-6</a></span>.</p>
<p>[9]  MR. JUSTICE MARSHALL argues in dissent that our cases have "established two different due process tests for two very different situations." <i>Post,</i> at 122. Pretrial identifications are to be covered by <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> which is said to require exclusion of evidence concerning unnecessarily suggestive pretrial identifications without regard to reliability. In-court identifications, on the other hand, are to be governed by <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span></i> and admissibility turns on reliability. The Court's cases are sorted into one category or the other. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>,</i> which clearly adopts the reliability of the identification as the guiding factor in the admissibility of both pretrial and in-court identifications, is condemned for mixing the two lines and for adopting a uniform rule.
</p>
<p>Although it must be acknowledged that our cases are not uniform in their emphasis, they hardly suggest the formal structure the dissent would impose on them. If our cases truly established two different rules, one might expect at some point at least passing reference to the fact. There is none. And if <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> departed so grievously from the past cases, it is surprising that there was not at least some mention of the point in MR. JUSTICE BRENNAN'S dissent. In fact, the cases are not so readily sorted as the dissent suggests. Although <i><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">Foster</a></span></i> involved both in-court and out-of-court identifications, the Court seemed to apply only a single standard for both. And although <i><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span></i> involved only an in-court identification, the plurality cited <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> for the guiding rule that the claim was to be assessed on the "totality of the surrounding circumstances." <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#4" aria-description="Citation for case: Coleman v. Alabama">399 U. S., at 4</a></span>. Thus, <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span></i> is not properly seen as a departure from the past cases, but as a synthesis of them.</p>
<p>[10]  Although the <i>per se</i> approach demands the exclusion of testimony concerning unnecessarily suggestive identifications, it does permit the admission of testimony concerning a subsequent identification, including an in-court identification, if the subsequent identification is determined to be reliable. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#367" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 367</a></span>. The totality approach, in contrast, is simpler: if the challenged identification is reliable, then testimony as to it and any identification in its wake is admissible.</p>
<p>[11]  The Fourth Circuit's then very recent decision in <i>Smith</i> v. <i>Coiner,</i> <span class="citation" data-id="308320"><a href="/opinion/308320/edward-lee-smith-v-ira-m-coiner-warden-of-the-west-virginia-state/" aria-description="Citation for case: Edward Lee Smith v. Ira M. Coiner, Warden of the West...">473 F. 2d 877</a></span> (1973), was described as one applying the second, or totality, test. <span class="citation" data-id="8891137"><a href="/opinion/8904042/stanley-v-cox/#55" aria-description="Citation for case: Stanley v. Cox">486 F. 2d, at 55</a></span>.</p>
<p>[12]  The interest in obtaining convictions of the guilty also urges the police to adopt procedures that show the resulting identification to be accurate. Suggestive procedures often will vitiate the weight of the evidence at trial and the jury may tend to discount such evidence. Cf. McGowan, Constitutional Interpretation and Criminal Identification, <span class="citation no-link">12 Wm. &amp; Mary L. Rev. 235</span>, 241 (1970).</p>
<p>[13]  Unlike a warrantless search, a suggestive preindictment identification procedure does not in itself intrude upon a constitutionally protected interest. Thus, considerations urging the exclusion of evidence deriving from a constitutional violation do not bear on the instant problem. See <i>United States ex rel. Kirby</i> v. <i>Sturges,</i> <span class="citation" data-id="324941"><a href="/opinion/324941/united-states-of-america-ex-rel-thomas-kirby-v-david-r-sturges-chairman/#406" aria-description="Citation for case: United States of America Ex Rel. Thomas Kirby v. David R....">510 F. 2d 397, 406</a></span> (CA7 1975).</p>
<p>[14]  "In essence what the <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> due process right protects is an evidentiary interest. . . .
</p>
<p>"It is part of our adversary system that we accept at trial much evidence that has strong elements of untrustworthinessan obvious example being the testimony of witnesses with a bias. While identification testimony is significant evidence, such testimony is still only evidence, and, unlike the presence of counsel, is not a factor that goes to the very heart the `integrity'of the adversary process.</p>
<p>"Counsel can both cross-examine the identification witnesses and argue in summation as to factors causing doubts as to the accuracy of the identificationincluding reference to both any suggestibility in the identification procedure and any countervailing testimony such as alibi." <i>Clemons</i> v. <i>United States,</i> 133 U. S. App. D. C. 27, 48, <span class="citation" data-id="9454404"><a href="/opinion/284140/malcus-t-clemons-v-united-states-of-america-david-e-clark-v-united/#1251" aria-description="Citation for case: Malcus T. Clemons v. United States of America, David E....">408 F. 2d 1230, 1251</a></span> (1968) (concurring opinion) (footnote omitted), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./394/964/">394 U. S. 964</a></span> (1969).</p>
<p>[15]  Mrs. Ramsey was not a witness at the trial.</p>
<p>[16]  We are not troubled, as was the Court of Appeals, by the "long and unexplained delay" in respondent's arrest. <span class="citation" data-id="331631"><a href="/opinion/331631/nowell-a-brathwaite-v-john-r-manson-commissioner-of-correction-of-the/#372" aria-description="Citation for case: Nowell A. Brathwaite v. John R. Manson, Commissioner of...">527 F. 2d, at 372</a></span>. That arrest took place on July 27. The toxicological report verifying the substance sold as heroin had issued only 11 days earlier, on July 16. Those 11 days after verification of the contents of the glassine bags do not constitute, for us, a "long" period. And with the positive toxicological report having been received within a fortnight, the arrest's delay perhaps is not "unexplained."</p>
<p>[*]  In this case, for example, the fact that the defendant was a regular visitor to the apartment where the drug transaction occurred tends to confirm his guilt. In the <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span></i> case, where the conviction was for robbery, the fact that papers from the victim's wallet were found in the possession of the defendant made it difficult to question the reliability of the identification. These facts should not, however, be considered to support the admissibility of eyewitness testimony when applying the criteria identified in <i>Neil</i> v. <i>Biggers,</i> <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U. S. 188</a></span>. Properly analyzed, however, such facts would be relevant to a question whether error, if any, in admitting identification testimony was harmless.</p>
<p>[1]  See, <i>e. g.,</i> P. Wall, Eye-Witness Identification in Criminal Cases 19-23 (1965); N. Sobel, Eye-Witness Identification: Legal and Practical Problems, §§ 3.01, 3.02, 30 (1972); Hammelmann &amp; Williams, Identification ParadesII, Crim. L. Rev. 545, 550 (1963).</p>
<p>[2]  The accused, a Negro, was brought handcuffed by seven white police officers and employees of the District Attorney to the hospital room of the only witness to a murder. As the Court said of this encounter: "It is hard to imagine a situation more clearly conveying the suggestion to the witness that the one presented is believed to be guilty by the police. See Frankfurter, The Case of Sacco and Vanzetti 31-32." <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#234" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 234</a></span> (1967).</p>
<p>[3]  The police reasonably feared that the witness might die before any less suggestive confrontation could be arranged.</p>
<p>[4]  See also, McGowan, Constitutional Interpretation and Criminal Identification, <span class="citation no-link">12 Wm. &amp; Mary L. Rev. 235</span>, 240 (1970).
</p>
<p>If the test enunciated in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> permitted any consideration of the witness' opportunity to observe the offender at the time of the crime, it was only in the narrowly circumscribed context of ascertaining the extent to which the challenged procedure was "conducive to irreparable mistaken identification." It is noteworthy, however, that in applying its test in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>,</i> the Court did not advert to the significant circumstantial evidence of guilt, see <i>United States ex rel. Stovall</i> v. <i>Denno,</i> <span class="citation" data-id="9451306"><a href="/opinion/270486/united-states-ex-rel-theodore-r-stovall-v-honorable-wilfred-denno-as/#733" aria-description="Citation for case: United States Ex Rel. Theodore R. Stovall v. Honorable...">355 F. 2d 731, 733-734</a></span> (CA2 1966), nor discuss any factors bearing on the witness' opportunity to view the assailant.</p>
<p>[5]  Mr. Justice Harlan, writing for the Court in <i><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span>,</i> acknowledged that there was a distinction between that case and <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i> After describing the factual setting and the applicable due process test, he noted that "[t]his standard accords with our resolution of a similar issue in <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span>.</i>" <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U. S., at 384</a></span>. He pointedly did not say that the cases were the same, nor did he rely on <i><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span></i> to set the standard.</p>
<p>[6]  "The showup itself consisted of two detectives walking respondent past the victim." <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#195" aria-description="Citation for case: Neil v. Biggers">409 U. S., at 195</a></span>. The police also ordered respondent to repeat the words used by the criminal. Inadequate efforts were made to secure participants for a lineup, and there was no pressing need to use a showup.</p>
<p>[7]  See, <i>e. g.,</i> N. Sobel, <i>supra,</i> n. 1, §§ 37, 38 (Supp. 1977); Grano, <i>Kirby, Biggers,</i> and <i>Ash:</i> Do Any Constitutional Safeguards Remain Against the Danger of Convicting the Innocent? <span class="citation no-link">72 Mich. L. Rev. 717</span> (1974); M. Hartman &amp; N. Goldberg, The Death of the Warren Court, The Doctrine of Suggestive Identification, 32 NLADA Briefcase 78 (1974); Pulaski, <i>Neil</i> v. <i><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span>:</i> The Supreme Court Dismantles the <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> Trilogy's Due Process Protection, <span class="citation no-link">26 Stan. L. Rev. 1097</span> (1974); Recent Developments, Identification: Unnecessary Suggestiveness May Not Violate Due Process, <span class="citation no-link">73 Colum. L. Rev. 1168</span> (1973).</p>
<p>[8]  See, <i>e. g., </i><i>People</i> v. <i>Anderson,</i> <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#172" aria-description="Citation for case: People v. Anderson">389 Mich. 155, 172-180, 192-220</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#468" aria-description="Citation for case: People v. Anderson">205 N. W. 2d 461, 468-472, 479-494, 485</a></span> (1973); Levine &amp; Tapp, The Psychology of Criminal Identification: The Gap From <i><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span></i> to <i><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/" aria-description="Citation for case: Kirby v. Illinois">Kirby</a></span>,</i> <span class="citation no-link">121 U. Pa. L. Rev. 1079</span> (1973); O'Connor, "That's the Man": A Sobering Study of Eyewitness Identification and the Polygraph, <span class="citation no-link">49 St. John's L. Rev. 1</span> (1974); McGowan, <i>supra,</i> n. 4, at 238-239; Grano, <i>supra,</i> n. 7, at 723-724, 768-770; Recent Developments, <i>supra,</i> n. 7, at 1169 n. 11.
</p>
<p>Moreover, as the exhaustive opinion of the Michigan Supreme Court in <i>People</i> v. <i><span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">Anderson, supra</a></span></i><i>,</i> noted:</p>
<p>"For a number of obvious reasons, however, including the fact that there is no on-going systematic study of the problem, the reported cases of misidentification are in every likelihood only the top of the iceberg. The writer of this opinion, for example, was able to turn up three very recent unreported cases right here in Michigan in the course of a few hours' inquiry." <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#179" aria-description="Citation for case: People v. Anderson">389 Mich., at 179-180</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#472" aria-description="Citation for case: People v. Anderson">205 N. W. 2d, at 472</a></span>.</p>
<p>[9]  See also <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 499</a></span> n. 6; <i>United States</i> v. <i>Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#193" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 193-194</a></span> (1977) (BRENNAN, J., dissenting); Brennan, State Constitutions and the Protection of Individual Rights, <span class="citation no-link">90 Harv. L. Rev. 489</span> (1977). Cf. <i>People</i> v. <i><span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/" aria-description="Citation for case: People v. Anderson">Anderson, supra</a></span></i><i>; </i><i>Commonwealth</i> v. <i>Botelho,</i>  Mass. , <span class="citation" data-id="2221090"><a href="/opinion/2221090/commonwealth-v-botelho/" aria-description="Citation for case: Commonwealth v. Botelho">343 N. E. 2d 876</a></span> (1976).</p>
<p>[10]  See, <i>e. g.,</i> <span class="citation" data-id="8988513"><a href="/opinion/8996170/wallace-v-smith/#1" aria-description="Citation for case: Wallace v. Smith">Wall, <i>supra,</i> n. 1</a></span>, at 15-16; <i>People</i> v. <i>Anderson,</i> <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#217" aria-description="Citation for case: People v. Anderson">389 Mich., at 217-220</a></span>, <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#493" aria-description="Citation for case: People v. Anderson">205 N. W. 2d, at 493-494</a></span>; O'Connor, <i>supra,</i> n. 8, at 4-6.</p>
<p>[11]  See, <i>e. g.,</i> Levine &amp; Tapp, <i>supra,</i> n. 8, at 1100-1101; Note, Pretrial Identification ProceduresWade to Gilbert to Stovall: Lower Courts Bobble the Ball, <span class="citation no-link">55 Minn. L. Rev. 779</span>, 789 (1971); <i>People</i> v. <span class="citation" data-id="9740327"><a href="/opinion/2222943/people-v-anderson/#214" aria-description="Citation for case: People v. Anderson"><i>Anderson, supra,</i> at 214-215</a></span>, <span class=

[...TRUNCATED 5469 of 125469 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---

## GROUP: _overhaul2/lake/cases/Manuel v. City of Joliet.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Manuel v. City of Joliet
type: case
citation: "580 U.S. 357 (2017)"
parallel_cite: "137 S. Ct. 911; 197 L. Ed. 2d 312; 26 Fla. L. Weekly Fed. S 476; 85 U.S.L.W. 4130"
neutral_cite: 2017 U.S. LEXIS 2021
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-03-21
docket: No. 14-9496
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
  opinion_url: "https://www.courtlistener.com/opinion/4376986/manuel-v-city-of-joliet/"
  cluster_id: 4376986
  opinion_id: null
  identity_checked: true
lake:
  record_id: Manuel v. City of Joliet
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Malicious Prosecution under the Fourth Amendment]]"
    role: Anchor
related:
  - "[[Malicious Prosecution under the Fourth Amendment]]"
  - "[[Thompson v. Clark]]"
  - "[[Heck v. Humphrey]]"
tags:
  - case
  - fourth-amendment
  - pretrial-detention
  - malicious-prosecution
  - fabricated-evidence
  - section-1983
holding: "The Fourth Amendment governs a § 1983 claim for unlawful pretrial detention, including detention that continues after the start of legal process, where the legal process — here a judge's probable-cause determination resting on fabricated evidence — did not rest on genuine probable cause."
aliases:
  - Manuel v. City of Joliet
  - "Manuel v. City of Joliet (2017)"
---

# Manuel v. City of Joliet

*580 U.S. 357 (2017)* (No. 14-9496) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4376986 → majority opinion 9873459 (Kagan, J.; 580 U.S. 357, decided Mar. 21, 2017). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text carries S. Ct. star-pagination (parallel 137 S. Ct. 911), so the pin is to 137 S. Ct. at 920 (page-label `*920` precedes the "Our holding" sentence) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Elijah Manuel was arrested during a traffic stop in Joliet, Illinois. Officers claimed a pill in his possession tested positive for ecstasy; in fact both the field test and a later laboratory test were negative. Relying on the officers' fabricated report, a county-court judge found probable cause and ordered Manuel detained. He remained jailed for roughly 48 days before the charge was dismissed. Manuel sued under § 1983, alleging his pretrial detention violated the Fourth Amendment. The Seventh Circuit held that once legal process began, a claim challenging detention sounded only in the Due Process Clause, not the Fourth Amendment, and dismissed.

## Issue
Whether the Fourth Amendment governs a claim for unlawful pretrial detention that continues after the start of legal process.

## Rule
The Court held that the Fourth Amendment's protection against detention absent probable cause is not switched off when legal process begins: "Our holding — that the Fourth Amendment governs a claim for unlawful pretrial detention even beyond the start of legal process — does not exhaust the disputed legal issues in this case." — 137 S. Ct. at 920. ^pin-920

## Application
Pretrial detention is a "seizure," and the Fourth Amendment requires that a seizure rest on probable cause both before and after the onset of legal process. Where the legal process itself is corrupted — a judge's probable-cause finding is procured by fabricated evidence — it cannot cleanse the ensuing detention of its Fourth Amendment defect. Manuel could therefore pursue a Fourth Amendment claim for the detention that followed the judge's tainted probable-cause ruling. The Court [[Reading and Citing Cases#on-remand|remanded]], leaving to the Seventh Circuit the questions of the claim's precise contours and, in particular, when it accrues for limitations purposes.

## Conclusion
The judgment was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Kagan, J., delivered the opinion of the Court; Alito, J. (joined by Thomas, J.), and Thomas, J., dissented.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Manuel* supplies the constitutional footing for what many courts call a "Fourth Amendment malicious-prosecution" claim: unlawful pretrial detention is a seizure governed by the Fourth Amendment, even after legal process begins. It expressly left open the claim's elements and accrual; the accrual point for the related fabricated-evidence claim was addressed in *[[McDonough v. Smith]]* (2019), and the favorable-termination element of a Fourth Amendment malicious-prosecution claim was settled in *[[Thompson v. Clark]]* (2022). Teach *Manuel* as the anchor and those cases as the build-out.

## Appears on
- [[Malicious Prosecution under the Fourth Amendment]] — *Anchor*

## Sources
- [*Manuel v. City of Joliet*, 580 U.S. 357 (2017)](https://www.courtlistener.com/opinion/4376986/manuel-v-city-of-joliet/) — pinpoint: 137 S. Ct. 911, 920 (Kagan, J., for the Court; the CL opinion text is paginated to the parallel S. Ct. reporter, with the page-label `*920` immediately preceding the "Our holding" sentence — the U.S. Reports star-pagination is not present in the CL text). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "579a5db679d79a1a", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Manuel v. City of Joliet"}, "payload": {"all": [{"cite": "580 U.S. 357", "page": "357", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "580"}, {"cite": "137 S. Ct. 911", "page": "911", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "137"}, {"cite": "197 L. Ed. 2d 312", "page": "312", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "197"}, {"cite": "2017 U.S. LEXIS 2021", "page": "2021", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2017"}, {"cite": "26 Fla. L. Weekly Fed. S 476", "page": "476", "reporter": "Fla. L. Weekly Fed. S", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "26"}, {"cite": "85 U.S.L.W. 4130", "page": "4130", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "85"}], "display": "580 U.S. 357", "official": {"cite": "580 U.S. 357", "page": "357", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "580"}, "official_selection_present": true, "record_id": "Manuel v. City of Joliet"}}
{"assertion_id": "3e2633fd758ce82b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Manuel v. City of Joliet"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Manuel v. City of Joliet", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Manuel v. City of Joliet

```json
{
  "schema_version": "s2.v1",
  "record_id": "Manuel v. City of Joliet",
  "status": "under_review",
  "identity": {
    "case_name": "Manuel v. City of Joliet",
    "case_name_short": "Manuel",
    "case_name_full": "Elijah MANUEL, Petitioner v. CITY OF JOLIET, ILLINOIS, Et Al.",
    "input_case_name": "Manuel v. City of Joliet",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-03-21",
    "year": 2017,
    "docket": "No. 14-9496",
    "cluster_id": 4376986,
    "lead_opinion_id": 9873459,
    "sibling_ids": [],
    "absolute_url": "/opinion/4376986/manuel-v-city-of-joliet/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "580 U.S. 357",
      "volume": "580",
      "reporter": "U.S.",
      "page": "357",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "137 S. Ct. 911",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "197 L. Ed. 2d 312",
        "volume": "197",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 476",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4130",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4130",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 2021",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "2021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "580 U.S. 357",
        "volume": "580",
        "reporter": "U.S.",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 911",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "911",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "197 L. Ed. 2d 312",
        "volume": "197",
        "reporter": "L. Ed. 2d",
        "page": "312",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 2021",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "2021",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 476",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "476",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4130",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4130",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "580 U.S. 357",
    "official_selection": {
      "court_class": "scotus",
      "selected": "580 U.S. 357",
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
    "date_created": "2026-07-06T13:14:47Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:14:57Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "manuel-v-city-of-joliet--4376986",
      "to_record_id": "Manuel v. City of Joliet",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Manuel v. City of Joliet

```
<opinion type="majority">
<author id="p-10">Justice KAGAN delivered the opinion of the Court.</author>
<p id="p-11">Petitioner Elijah Manuel was held in jail for some seven weeks after a judge relied on allegedly fabricated evidence to find probable cause that he had committed a crime. The primary question in this case is whether Manuel may bring a claim based on the Fourth Amendment to contest the legality of his pretrial confinement. Our answer follows from settled precedent. The Fourth Amendment, this Court has recognized, establishes "the standards and procedures" governing pretrial detention. See, <em>e.g.,</em> <em>Gerstein v. Pugh,</em> <extracted-citation case-ids="11642843" index="0" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S. 103</a></span></extracted-citation>, 111, <extracted-citation case-ids="11642843" index="1" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>, <extracted-citation case-ids="11642843" index="2" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">43 L.Ed.2d 54</a></span></extracted-citation> (1975). And those constitutional protections apply even after the start of "legal process" in a criminal case-here, that is, after the judge's determination of probable cause. See <em>Albright v. Oliver,</em> <extracted-citation case-ids="231967" index="3" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S. 266</a></span></extracted-citation>, 274, <extracted-citation case-ids="231967" index="4" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="5" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">127 L.Ed.2d 114</a></span></extracted-citation> (1994) (plurality opinion); <em><extracted-citation case-ids="231967" index="6" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="6" url="https://cite.case.law/us/510/266/#p274"> at 290</extracted-citation>, <extracted-citation case-ids="231967" index="7" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (Souter, J., concurring in judgment). Accordingly, we hold today that Manuel may challenge his pretrial detention on the ground that it violated the Fourth Amendment (while we <a class="page-label" data-citation-index="1" data-label="915" href="#p915" id="p915">*915</a>leave all other issues, including one about that claim's timeliness, to the court below).</p>
<p id="p-12">I</p>
<p id="p-13">Shortly after midnight on March 18, 2011, Manuel was riding through Joliet, Illinois, in the passenger seat of a Dodge Charger, with his brother at the wheel. A pair of Joliet police officers pulled the car over when the driver failed to signal a turn. See App. 90. According to the complaint in this case, one of the officers dragged Manuel from the car, called him a racial slur, and kicked and punched him as he lay on the ground. See <em>id.,</em> at 31-32, 63.<footnotemark>1</footnotemark> The policeman then searched Manuel and found a vitamin bottle containing pills. See <em>id.,</em> at 64. Suspecting that the pills were actually illegal drugs, the officers conducted a field test of the bottle's contents. The test came back negative for any controlled substance, leaving the officers with no evidence that Manuel had committed a crime. See <em>id.,</em> at 69. Still, the officers arrested Manuel and took him to the Joliet police station. See <em>id.,</em> at 70.</p>
<p id="p-14">There, an evidence technician tested the pills once again, and got the same (negative) result. See <em>ibid.</em> But the technician lied in his report, claiming that one of the pills was "found to be ... positive for the probable presence of ecstasy." <em>Id.,</em> at 92. Similarly, one of the arresting officers wrote in his report that "[f]rom [his] training and experience, [he] knew the pills to be ecstasy." <em>Id.,</em> at 91. On the basis of those statements, another officer swore out a criminal complaint against Manuel, charging him with unlawful possession of a controlled substance. See <em>id.,</em> at 52-53.</p>
<p id="p-15">Manuel was brought before a county court judge later that day for a determination of whether there was probable cause for the charge, as necessary for further detention. See <em>Gerstein,</em> <extracted-citation case-ids="11642843" index="8" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S., at 114</a></span></extracted-citation>, <extracted-citation case-ids="11642843" index="9" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation> (requiring a judicial finding of probable cause following a warrantless arrest to impose any significant pretrial restraint on liberty); Ill. Comp. Stat., ch. 725, § 5/109-1 (West 2010) (implementing that constitutional rule). The judge relied exclusively on the criminal complaint-which in turn relied exclusively on the police department's fabrications-to support a finding of probable cause. Based on that determination, he sent Manuel to the county jail to await trial. In the somewhat obscure legal lingo of this case, Manuel's subsequent detention was thus pursuant to "legal process"-because it followed from, and was authorized by, the judge's probable-cause determination.<footnotemark>2</footnotemark></p>
<p id="p-16">While Manuel sat in jail, the Illinois police laboratory reexamined the seized pills, and on April 1, it issued a report concluding (just as the prior two tests had) that they contained no controlled substances. See App. 51. But for unknown reasons, the prosecution-and, critically for this case, Manuel's detention-continued for more than another month. Only on May 4 did an Assistant State's Attorney seek dismissal of the drug charge. See <em>id.,</em> at 48, 101. The County Court immediately granted the request, and Manuel was <a class="page-label" data-citation-index="1" data-label="916" href="#p916" id="p916">*916</a>released the next day. In all, he had spent 48 days in pretrial detention.</p>
<p id="p-17">On April 22, 2013, Manuel brought this lawsuit under <extracted-citation index="10" url="https://cite.case.law/citations/?q=42%20U.S.C.%20%C2%A7%201983"><span class="citation no-link">42 U.S.C. § 1983</span></extracted-citation> against the City of Joliet and several of its police officers (collectively, the City). Section 1983 creates a "species of tort liability," <em>Imbler v. Pachtman,</em> <extracted-citation case-ids="12026708" index="11" url="https://cite.case.law/us/424/409/#p417"><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">424 U.S. 409</a></span></extracted-citation>, 417, <extracted-citation case-ids="12026708" index="12" url="https://cite.case.law/us/424/409/#p417"><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">96 S.Ct. 984</a></span></extracted-citation>, <extracted-citation case-ids="12026708" index="13" url="https://cite.case.law/us/424/409/#p417"><span class="citation" data-id="9426281"><a href="/opinion/109387/imbler-v-pachtman/" aria-description="Citation for case: Imbler v. Pachtman">47 L.Ed.2d 128</a></span></extracted-citation> (1976), for "the deprivation of any rights, privileges, or immunities secured by the Constitution," § 1983. Manuel's complaint alleged that the City violated his Fourth Amendment rights in two ways-first by arresting him at the roadside without any reason, and next by "detaining him in police custody" for almost seven weeks based entirely on made-up evidence. See App. 79-80.<footnotemark>3</footnotemark></p>
<p id="p-18">The District Court dismissed Manuel's suit. See <extracted-citation index="14" url="https://cite.case.law/citations/?q=2014%20WL%20551626"><span class="citation no-link">2014 WL 551626</span></extracted-citation> (N.D.Ill., Feb. 12, 2014). The court first held that the applicable two-year statute of limitations barred Manuel's claim for unlawful arrest, because more than two years had elapsed between the date of his arrest (March 18, 2011) and the filing of his complaint (April 22, 2013). But the court relied on another basis in rejecting Manuel's challenge to his subsequent detention (which stretched from March 18 to May 5, 2011). Binding Circuit precedent, the District Court explained, made clear that pretrial detention following the start of legal process could not give rise to a Fourth Amendment claim. See <em><extracted-citation index="15" url="https://cite.case.law/citations/?q=2014%20WL%20551626"><span class="citation no-link">id.,</span></extracted-citation></em> at *1 (citing, <em>e.g.,</em> <em>Newsome v. McCabe,</em> <extracted-citation case-ids="11088221" index="16" url="https://cite.case.law/f3d/256/747/#p750"><span class="citation" data-id="773982"><a href="/opinion/773982/james-newsome-v-john-mccabe-and-raymond-mcnally/" aria-description="Citation for case: James Newsome v. John McCabe and Raymond McNally">256 F.3d 747</a></span></extracted-citation>, 750 (C.A.7 2001) ). According to that line of decisions, a § 1983 plaintiff challenging such detention must allege a breach of the Due Process Clause-and must show, to recover on that theory, that state law fails to provide an adequate remedy. See <extracted-citation index="17" url="https://cite.case.law/citations/?q=2014%20WL%20551626"><span class="citation no-link">2014 WL 551626</span></extracted-citation>, at *1-*2. Because Manuel's complaint rested solely on the Fourth Amendment-and because, in any event, Illinois's remedies were robust enough to preclude the due process avenue-the District Court found that Manuel had no way to proceed. See <em>ibid</em> .</p>
<p id="p-19">The Court of Appeals for the Seventh Circuit affirmed the dismissal of Manuel's claim for unlawful detention (the only part of the District Court's decision Manuel appealed). See <extracted-citation index="18" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx. 641</a></span></extracted-citation> (2015). Invoking its prior caselaw, the Court of Appeals reiterated that such claims could not be brought under the Fourth Amendment. Once a person is detained pursuant to legal process, the court stated, "the Fourth Amendment falls out of the picture and the detainee's claim that the detention is improper becomes [one of] due process." <em><extracted-citation index="19" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">Id.,</a></span></extracted-citation></em><extracted-citation index="19" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"> at 643-644</extracted-citation> (quoting <em>Llovet v. Chicago,</em> <extracted-citation case-ids="4151176" index="20" url="https://cite.case.law/f3d/761/759/#p763"><span class="citation" data-id="8413043"><a href="/opinion/8441868/llovet-v-city-of-chicago/" aria-description="Citation for case: Llovet v. City of Chicago">761 F.3d 759</a></span></extracted-citation>, 763 (C.A.7 2014) ). And again: "When, after the arrest[,] a person is not let go when he should be, the Fourth Amendment gives way to the due process clause as a basis for challenging his detention." <extracted-citation index="21" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span></extracted-citation> (quoting <em>Llovet,</em> <extracted-citation case-ids="4151176" index="22" url="https://cite.case.law/f3d/761/759/#p763">761 F.3d, at </extracted-citation>764 ). So the Seventh Circuit held that Manuel's complaint, in alleging only a Fourth Amendment violation, rested on the wrong part of the Constitution: A person detained following the onset of legal process could at most (although, the court agreed, <em>not</em> in Illinois) challenge his pretrial confinement via the Due Process Clause. See <extracted-citation index="23" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span>-644</extracted-citation>.</p>
<p id="p-20"><a class="page-label" data-citation-index="1" data-label="917" href="#p917" id="p917">*917</a>The Seventh Circuit recognized that its position makes it an outlier among the Courts of Appeals, with ten others taking the opposite view. See <em><extracted-citation index="24" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">id.,</a></span></extracted-citation></em> at 643 ; <em>Hernandez-Cuevas v. Taylor,</em> <extracted-citation case-ids="4065880" index="25" url="https://cite.case.law/f3d/723/91/#p99"><span class="citation" data-id="1034188"><a href="/opinion/1034188/hernandez-cuevas-v-taylor/" aria-description="Citation for case: Hernandez-Cuevas v. Taylor">723 F.3d 91</a></span></extracted-citation>, 99 (C.A.1 2013) ("[T]here is now broad consensus among the circuits that the Fourth Amendment right to be free from seizure but upon probable cause extends through the pretrial period").<footnotemark>4</footnotemark> Still, the court decided, Manuel had failed to offer a sufficient reason for overturning settled Circuit precedent; his argument, albeit "strong," was "better left for the Supreme Court." <extracted-citation index="26" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span></extracted-citation>.</p>
<p id="p-21">On cue, we granted certiorari. 577 U.S. ----, <extracted-citation case-ids="12602162,12602163,12602164,12602165,12602166,12602167" index="27" url="https://cite.case.law/s-ct/136/890/"><span class="citation multiple-matches"><a href="/c/S.Ct./136/890/">136 S.Ct. 890</a></span></extracted-citation>, <extracted-citation case-ids="12602162,12602163,12602164,12602165,12602166,12602167" index="28" url="https://cite.case.law/s-ct/136/890/"><span class="citation multiple-matches"><a href="/c/L.Ed.2d/193/783/">193 L.Ed.2d 783</a></span></extracted-citation> (2016).</p>
<p id="p-22">II</p>
<p id="p-23">The Fourth Amendment protects "[t]he right of the people to be secure in their persons ... against unreasonable ... seizures." Manuel's complaint seeks just that protection. Government officials, it recounts, detained-which is to say, "seiz[ed]"-Manuel for 48 days following his arrest. See App. 79-80; <em>Brendlin v. California,</em> <extracted-citation case-ids="3573063" index="29" url="https://cite.case.law/us/551/249/#p254"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">551 U.S. 249</a></span></extracted-citation>, 254, <extracted-citation case-ids="3573063" index="30" url="https://cite.case.law/us/551/249/#p254"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">127 S.Ct. 2400</a></span></extracted-citation>, <extracted-citation case-ids="3573063" index="31" url="https://cite.case.law/us/551/249/#p254"><span class="citation" data-id="145712"><a href="/opinion/145712/brendlin-v-california/" aria-description="Citation for case: Brendlin v. California">168 L.Ed.2d 132</a></span></extracted-citation> (2007) ("A person is seized" whenever officials "restrain[ ] his freedom of movement" such that he is "not free to leave"). And that detention was "unreasonable," the complaint continues, because it was based solely on false evidence, rather than supported by probable cause. See App. 79-80; <em>Bailey v. United States,</em> <extracted-citation case-ids="12407374" index="32" url="https://cite.case.law/us/568/186/#p192"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">568 U.S. 186</a></span></extracted-citation>, 192, <extracted-citation case-ids="12407374" index="33" url="https://cite.case.law/us/568/186/#p192"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">133 S.Ct. 1031</a></span></extracted-citation>, <extracted-citation case-ids="12407374" index="34" url="https://cite.case.law/us/568/186/#p192"><span class="citation" data-id="9502775"><a href="/opinion/820749/bailey-v-united-states/" aria-description="Citation for case: Bailey v. United States">185 L.Ed.2d 19</a></span></extracted-citation> (2013) ( "[T]he general rule [is] that Fourth Amendment seizures are 'reasonable' only if based on probable cause to believe that the individual has committed a crime"). By their respective terms, then, Manuel's claim fits the Fourth Amendment, and the Fourth Amendment fits Manuel's claim, as hand in glove.</p>
<p id="p-24">This Court decided some four decades ago that a claim challenging pretrial detention fell within the scope of the Fourth Amendment. In <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</em> two persons arrested without a warrant brought a § 1983 suit complaining that they had been held in custody for "a substantial period solely on the decision of a prosecutor." <extracted-citation case-ids="11642843" index="35" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U.S., at 106</a></span></extracted-citation>, <extracted-citation case-ids="11642843" index="36" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. The Court looked to the Fourth Amendment to analyze-and uphold-their claim that such a pretrial restraint on liberty is unlawful unless a judge (or grand jury) first makes a reliable finding of probable cause. See <em><extracted-citation case-ids="11642843" index="37" url="https://cite.case.law/us/420/103/#p111">id.,</extracted-citation></em><extracted-citation case-ids="11642843" index="37" url="https://cite.case.law/us/420/103/#p111"> at 114, 117, n. 19</extracted-citation>, <extracted-citation case-ids="11642843" index="38" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. The Fourth Amendment, we began, establishes the minimum constitutional "standards and procedures" not just for arrest but also for ensuing "detention." <em><extracted-citation case-ids="11642843" index="39" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="39" url="https://cite.case.law/us/420/103/#p111"> at 111</extracted-citation>, <extracted-citation case-ids="11642843" index="40" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. In choosing that Amendment "as the rationale for decision," the Court responded to a concurring Justice's view that the Due Process Clause offered the better framework: The Fourth Amendment, the majority countered, was "tailored explicitly for the criminal justice system, and it[ ] always has been thought to define" the appropriate process "for seizures of person[s] ... in criminal cases, including the detention of suspects pending trial." <em><extracted-citation case-ids="11642843" index="41" url="https://cite.case.law/us/420/103/#p111">Id.,</extracted-citation></em><extracted-citation case-ids="11642843" index="41" url="https://cite.case.law/us/420/103/#p111"> at 125, n. 27</extracted-citation>, <extracted-citation case-ids="11642843" index="42" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. That Amendment, standing alone, guaranteed "a fair and reliable determination of probable cause as a condition for any significant <a class="page-label" data-citation-index="1" data-label="918" href="#p918" id="p918">*918</a>pretrial restraint." <em><extracted-citation case-ids="11642843" index="43" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="43" url="https://cite.case.law/us/420/103/#p111"> at 125</extracted-citation>, <extracted-citation case-ids="11642843" index="44" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>. Accordingly, those detained prior to trial without such a finding could appeal to "the Fourth Amendment's protection against unfounded invasions of liberty." <em><extracted-citation case-ids="11642843" index="45" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="45" url="https://cite.case.law/us/420/103/#p111"> at 112</extracted-citation>, <extracted-citation case-ids="11642843" index="46" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation> ; see <em><extracted-citation case-ids="11642843" index="47" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">id.,</a></span></extracted-citation></em><extracted-citation case-ids="11642843" index="47" url="https://cite.case.law/us/420/103/#p111"> at 114</extracted-citation>, <extracted-citation case-ids="11642843" index="48" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation>.<footnotemark>5</footnotemark></p>
<p id="p-25">And so too, a later decision indicates, those objecting to a pretrial deprivation of liberty may invoke the Fourth Amendment when (as here) that deprivation occurs after legal process commences. The § 1983 plaintiff in <em><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">Albright</a></span></em> complained of various pretrial restraints imposed after a court found probable cause to issue an arrest warrant, and then bind him over for trial, based on a policeman's unfounded charges. See <extracted-citation case-ids="231967" index="49" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 268</a></span>-269</extracted-citation>, <extracted-citation case-ids="231967" index="50" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (plurality opinion). For uncertain reasons, Albright ignored the Fourth Amendment in drafting his complaint; instead, he alleged that the defendant officer had infringed his substantive due process rights. This Court rejected that claim, with five Justices in two opinions remitting Albright to the Fourth Amendment. See <em><extracted-citation case-ids="231967" index="51" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="51" url="https://cite.case.law/us/510/266/#p274"> at 271</extracted-citation>, <extracted-citation case-ids="231967" index="52" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (plurality opinion) ("We hold that it is the Fourth Amendment ... under which [his] claim must be judged"); <em><extracted-citation case-ids="231967" index="53" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="53" url="https://cite.case.law/us/510/266/#p274"> at 290</extracted-citation>, <extracted-citation case-ids="231967" index="54" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (Souter, J., concurring in judgment) ("[I]njuries like those [he] alleges are cognizable in § 1983 claims founded upon ... the Fourth Amendment"). "The Framers," the plurality wrote, "considered the matter of pretrial deprivations of liberty and drafted the Fourth Amendment to address it." <em><extracted-citation case-ids="231967" index="55" url="https://cite.case.law/us/510/266/#p274">Id.,</extracted-citation></em><extracted-citation case-ids="231967" index="55" url="https://cite.case.law/us/510/266/#p274"> at 274</extracted-citation>, <extracted-citation case-ids="231967" index="56" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>. That the deprivations at issue were pursuant to legal process made no difference, given that they were (allegedly) unsupported by probable cause; indeed, neither of the two opinions so much as mentioned that procedural circumstance. Relying on <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span>,</em> the plurality stated that the Fourth Amendment remained the "relevan[t]" constitutional provision to assess the "deprivations of liberty"-most notably, pretrial detention-"that go hand in hand with criminal prosecutions." <extracted-citation case-ids="231967" index="57" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 274</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="58" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> ; see <em><extracted-citation case-ids="231967" index="59" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">id.,</a></span></extracted-citation></em><extracted-citation case-ids="231967" index="59" url="https://cite.case.law/us/510/266/#p274"> at 290</extracted-citation>, <extracted-citation case-ids="231967" index="60" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (Souter, J., concurring in judgment) ("[R]ules of recovery for such harms have naturally coalesced under the Fourth Amendment").</p>
<p id="p-26">As reflected in <em><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">Albright</a></span></em> 's tracking of <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em> 's analysis, pretrial detention can violate the Fourth Amendment not only when it precedes, but also when it follows, the start of legal process in a criminal case. The Fourth Amendment prohibits government officials from detaining a person in the absence of probable cause. See <em>supra,</em> at 917. That can happen when the police hold someone without any reason before the formal onset of a criminal proceeding. But it also can occur when legal process itself goes wrong-when, for example, a judge's probable-cause determination is predicated solely on a police officer's false statements. Then, too, a person is confined without constitutionally adequate justification. Legal process <a class="page-label" data-citation-index="1" data-label="919" href="#p919" id="p919">*919</a>has gone forward, but it has done nothing to satisfy the Fourth Amendment's probable-cause requirement. And for that reason, it cannot extinguish the detainee's Fourth Amendment claim-or somehow, as the Seventh Circuit has held, convert that claim into one founded on the Due Process Clause. See <extracted-citation index="61" url="https://cite.case.law/citations/?q=590%20Fed.%20Appx.%20641"><span class="citation" data-id="2774281"><a href="/opinion/2774281/elijah-manuel-v-city-of-joliet/" aria-description="Citation for case: Elijah Manuel v. City of Joliet">590 Fed.Appx., at 643</a></span>-644</extracted-citation>. If the complaint is that a form of legal process resulted in pretrial detention unsupported by probable cause, then the right allegedly infringed lies in the Fourth Amendment.<footnotemark>6</footnotemark></p>
<p id="p-27">For that reason, and contrary to the Seventh Circuit's view, Manuel stated a Fourth Amendment claim when he sought relief not merely for his (pre-legal-process) arrest, but also for his (post-legal-process) pretrial detention.<footnotemark>7</footnotemark> Consider again the facts alleged in this case. Police officers initially arrested Manuel without probable cause, based solely on his possession of pills that had field tested negative for an illegal substance. So (putting timeliness issues aside) Manuel could bring a claim for wrongful arrest under the Fourth Amendment. And the same is true (again, disregarding timeliness) as to a claim for wrongful detention-because Manuel's subsequent weeks in custody were <em>also</em> unsupported by probable cause, and so <em>also</em> constitutionally unreasonable. No evidence of Manuel's criminality had come to light in between the roadside arrest and the County Court proceeding initiating legal process; to the contrary, yet another test of Manuel's pills had come back negative in that period. All that the judge had before him were police fabrications about the pills' content. The judge's order holding Manuel for trial therefore lacked any proper basis. And that means Manuel's ensuing pretrial detention, no less than his original arrest, violated his Fourth Amendment rights. Or put just a bit differently: Legal process did not expunge Manuel's Fourth Amendment claim because the process he received failed to establish what that Amendment makes essential for pretrial <a class="page-label" data-citation-index="1" data-label="920" href="#p920" id="p920">*920</a>detention-probable cause to believe he committed a crime.<footnotemark>8</footnotemark></p>
<p id="p-28">III</p>
<p id="p-29">Our holding-that the Fourth Amendment governs a claim for unlawful pretrial detention even beyond the start of legal process-does not exhaust the disputed legal issues in this case. It addresses only the threshold inquiry in a § 1983 suit, which requires courts to "identify the specific constitutional right" at issue. <em>Albright,</em> <extracted-citation case-ids="231967" index="62" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 271</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="63" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation>. After pinpointing that right, courts still must determine the elements of, and rules associated with, an action seeking damages for its violation. See, <em>e.g.,</em> <em>Carey v. Piphus,</em> <extracted-citation case-ids="2517" index="64" url="https://cite.case.law/us/435/247/#p257"><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/" aria-description="Citation for case: Carey v. Piphus">435 U.S. 247</a></span></extracted-citation>, 257-258, <extracted-citation case-ids="2517" index="65" url="https://cite.case.law/us/435/247/#p257"><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/" aria-description="Citation for case: Carey v. Piphus">98 S.Ct. 1042</a></span></extracted-citation>, <extracted-citation case-ids="2517" index="66" url="https://cite.case.law/us/435/247/#p257"><span class="citation" data-id="109815"><a href="/opinion/109815/carey-v-piphus/" aria-description="Citation for case: Carey v. Piphus">55 L.Ed.2d 252</a></span></extracted-citation> (1978). Here, the parties particularly disagree over the accrual date of Manuel's Fourth Amendment claim-that is, the date on which the applicable two-year statute of limitations began to run. The timeliness of Manuel's suit hinges on the choice between their proposed dates. But with the following brief comments, we remand that issue to the court below.</p>
<p id="p-30">In defining the contours and prerequisites of a § 1983 claim, including its rule of accrual, courts are to look first to the common law of torts. See <em><extracted-citation case-ids="2517" index="67" url="https://cite.case.law/us/435/247/#p257">ibid.</extracted-citation></em> (explaining that tort principles "provide the appropriate starting point" in specifying the conditions for recovery under § 1983 ); <em>Wallace v. Kato,</em> <extracted-citation case-ids="3553763" index="68" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. 384</a></span></extracted-citation>, 388-390, <extracted-citation case-ids="3553763" index="69" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="70" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">166 L.Ed.2d 973</span></extracted-citation> (2007) (same for accrual dates in particular). Sometimes, that review of common law will lead a court to adopt wholesale the rules that would apply in a suit involving the most analogous tort. See <em><extracted-citation case-ids="3553763" index="71" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">id.,</span></extracted-citation></em><extracted-citation case-ids="3553763" index="71" url="https://cite.case.law/us/549/384/#p388"> at 388-390</extracted-citation>, <extracted-citation case-ids="3553763" index="72" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> ;</p>
<p id="p-31"><a class="page-label" data-citation-index="1" data-label="921" href="#p921" id="p921">*921</a><em>Heck v. Humphrey,</em> <extracted-citation case-ids="39868" index="73" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">512 U.S. 477</a></span></extracted-citation>, 483-487, <extracted-citation case-ids="39868" index="74" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>, <extracted-citation case-ids="39868" index="75" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">129 L.Ed.2d 383</a></span></extracted-citation> (1994). But not always. Common-law principles are meant to guide rather than to control the definition of § 1983 claims, serving "more as a source of inspired examples than of prefabricated components." <em>Hartman v. Moore,</em> <extracted-citation case-ids="3275855" index="76" url="https://cite.case.law/us/547/250/#p258"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">547 U.S. 250</a></span></extracted-citation>, 258, <extracted-citation case-ids="3275855" index="77" url="https://cite.case.law/us/547/250/#p258"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">126 S.Ct. 1695</a></span></extracted-citation>, <extracted-citation case-ids="3275855" index="78" url="https://cite.case.law/us/547/250/#p258"><span class="citation" data-id="9434955"><a href="/opinion/145662/hartman-v-moore/" aria-description="Citation for case: Hartman v. Moore">164 L.Ed.2d 441</a></span></extracted-citation> (2006) ; see <em>Rehberg v. Paulk,</em> <extracted-citation case-ids="12189183" index="79" url="https://cite.case.law/us/566/356/#p366"><span class="citation" data-id="626447"><a href="/opinion/626447/rehberg-v-paulk/" aria-description="Citation for case: Rehberg v. Paulk">566 U.S. 356</a></span></extracted-citation>, 366, <extracted-citation case-ids="12189183" index="80" url="https://cite.case.law/us/566/356/#p366"><span class="citation" data-id="626447"><a href="/opinion/626447/rehberg-v-paulk/" aria-description="Citation for case: Rehberg v. Paulk">132 S.Ct. 1497</a></span></extracted-citation>, <extracted-citation case-ids="12189183" index="81" url="https://cite.case.law/us/566/356/#p366"><span class="citation" data-id="626447"><a href="/opinion/626447/rehberg-v-paulk/" aria-description="Citation for case: Rehberg v. Paulk">182 L.Ed.2d 593</a></span></extracted-citation> (2012) (noting that " § 1983 is [not] simply a federalized amalgamation of pre-existing common-law claims"). In applying, selecting among, or adjusting common-law approaches, courts must closely attend to the values and purposes of the constitutional right at issue.</p>
<p id="p-32">With these precepts as backdrop, Manuel and the City offer competing views about what accrual rule should govern a § 1983 suit challenging post-legal-process pretrial detention. According to Manuel, that Fourth Amendment claim accrues only upon the dismissal of criminal charges-here, on May 4, 2011, less than two years before he brought his suit. See Reply Brief 2; Brief for United States as <em>Amicus Curiae</em> 24-25, n. 16 (taking the same position). Relying on this Court's caselaw, Manuel analogizes his claim to the common-law tort of malicious prosecution. See Reply Brief 9; <em>Wallace,</em> <extracted-citation case-ids="3553763" index="82" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S., at 389</a></span>-390</extracted-citation>, <extracted-citation case-ids="3553763" index="83" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>. An element of that tort is the "termination of the ... proceeding in favor of the accused"; and accordingly, the statute of limitations does not start to run until that termination takes place. <em>Heck,</em> <extracted-citation case-ids="39868" index="84" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/#484" aria-description="Citation for case: Heck v. Humphrey">512 U.S., at 484</a></span>, 489</extracted-citation>, <extracted-citation case-ids="39868" index="85" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation>. Manuel argues that following the same rule in suits like his will avoid "conflicting resolutions" in § 1983 litigation and criminal proceedings by "preclud[ing] the possibility of the claimant succeeding in the tort action after having been convicted in the underlying criminal prosecution." <em><extracted-citation case-ids="39868" index="86" url="https://cite.case.law/us/512/477/#p483">Id.,</extracted-citation></em><extracted-citation case-ids="39868" index="86" url="https://cite.case.law/us/512/477/#p483"> at 484, 486</extracted-citation>, <extracted-citation case-ids="39868" index="87" url="https://cite.case.law/us/512/477/#p483"><span class="citation" data-id="9433019"><a href="/opinion/117864/heck-v-humphrey/" aria-description="Citation for case: Heck v. Humphrey">114 S.Ct. 2364</a></span></extracted-citation> ; see Reply Brief 10-11; Brief for United States as <em>Amicus Curiae</em> 24-25, n. 16. In support of Manuel's position, all but two of the ten Courts of Appeals that have recognized a Fourth Amendment claim like his have incorporated a "favorable termination" element and so pegged the statute of limitations to the dismissal of the criminal case. See n. 4, <em>supra</em> .<footnotemark>9</footnotemark> That means in the great majority of Circuits, Manuel's claim would be timely.</p>
<p id="p-33">The City, however, contends that any such Fourth Amendment claim accrues (and the limitations period starts to run) on the date of the initiation of legal process-here, on March 18, 2011, <em>more</em> than two years before Manuel filed suit. See Brief for Respondents 33. According to the City, the most analogous tort to Manuel's constitutional claim is not malicious prosecution but false arrest, which accrues when legal process commences. See Tr. of Oral Arg. 47; <em>Wallace,</em> <extracted-citation case-ids="3553763" index="88" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S., at 389</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="89" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation> (noting accrual rule for false arrest suits). And even if malicious prosecution were the better comparison, the City continues, a court should decline to adopt that tort's favorable-termination element and associated accrual rule in adjudicating a § 1983 claim involving pretrial detention. That element, the City argues, "make[s] little sense" in this context because "the Fourth Amendment is concerned not with the outcome of a prosecution, but with the legality of searches and seizures." Brief for Respondents 16. And finally, the City contends that Manuel forfeited an alternative theory for treating his date of release as the date of accrual: to wit, that his pretrial detention "constitute[d] a continuing Fourth Amendment violation," each day of which triggered the statute of limitations anew.</p>
<p id="p-34"><a class="page-label" data-citation-index="1" data-label="922" href="#p922" id="p922">*922</a><em>Id.,</em> at 29, and n. 6; see Tr. of Oral Arg. 36; see also <em>Albright,</em> <extracted-citation case-ids="231967" index="90" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 280</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="91" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (GINSBURG, J., concurring) (propounding a similar view). So Manuel, the City concludes, lost the opportunity to recover for his pretrial detention by waiting too long to file suit.</p>
<p id="p-35">We leave consideration of this dispute to the Court of Appeals. "[W]e are a court of review, not of first view." <em>Cutter v. Wilkinson,</em> <extracted-citation case-ids="5868782" index="92" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">544 U.S. 709</a></span></extracted-citation>, 718, n. 7, <extracted-citation case-ids="5868782" index="93" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">125 S.Ct. 2113</a></span></extracted-citation>, <extracted-citation case-ids="5868782" index="94" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">161 L.Ed.2d 1020</a></span></extracted-citation> (2005). Because the Seventh Circuit wrongly held that Manuel lacked any Fourth Amendment claim once legal process began, the court never addressed the elements of, or rules applicable to, such a claim. And in particular, the court never confronted the accrual issue that the parties contest here.<footnotemark>10</footnotemark> On remand, the Court of Appeals should decide that question, unless it finds that the City has previously waived its timeliness argument. See Reply to Brief in Opposition 1-2 (addressing the possibility of waiver); Tr. of Oral Arg. 40-44 (same). And so too, the court may consider any other still-live issues relating to the contours of Manuel's Fourth Amendment claim for unlawful pretrial detention.</p>
<p id="p-36">For the reasons stated, we reverse the judgment of the Seventh Circuit and remand the case for further proceedings consistent with this opinion.</p>
<p id="p-37"><em>It is so ordered.</em></p>
<footnote label="1">
<p id="p-85">Because we here review an order dismissing Manuel's suit, we accept as true all the factual allegations in his complaint. See, <em>e.g.,</em> <em>Leatherman v. Tarrant County Narcotics Intelligence and Coordination Unit,</em> <extracted-citation case-ids="6224800" index="95" url="https://cite.case.law/us/507/163/#p164"><span class="citation" data-id="112825"><a href="/opinion/112825/leatherman-v-tarrant-county-narcotics-intelligence-and-coordination-unit/" aria-description="Citation for case: Leatherman v. Tarrant County Narcotics Intelligence and...">507 U.S. 163</a></span></extracted-citation>, 164, <extracted-citation case-ids="6224800" index="96" url="https://cite.case.law/us/507/163/#p164"><span class="citation" data-id="112825"><a href="/opinion/112825/leatherman-v-tarrant-county-narcotics-intelligence-and-coordination-unit/" aria-description="Citation for case: Leatherman v. Tarrant County Narcotics Intelligence and...">113 S.Ct. 1160</a></span></extracted-citation>, <extracted-citation case-ids="6224800" index="97" url="https://cite.case.law/us/507/163/#p164"><span class="citation" data-id="112825"><a href="/opinion/112825/leatherman-v-tarrant-county-narcotics-intelligence-and-coordination-unit/" aria-description="Citation for case: Leatherman v. Tarrant County Narcotics Intelligence and...">122 L.Ed.2d 517</a></span></extracted-citation> (1993).</p>
</footnote>
<footnote label="2">
<p id="p-86">Although not addressed in Manuel's complaint, the police department's alleged fabrications did not stop at this initial hearing on probable cause. About two weeks later, on March 30, a grand jury indicted Manuel based on similar false evidence: testimony from one of the arresting officers that "[t]he pills field tested positive" for ecstasy. App. 96 (grand jury minutes).</p>
</footnote>
<footnote label="3">
<p id="p-87">Manuel's allegation of unlawful detention concerns only the period after the onset of legal process-here meaning, again, after the County Court found probable cause that he had committed a crime. See <em>supra,</em> at 915 - 916. The police also held Manuel in custody for several hours between his warrantless arrest and his first appearance in court. But throughout this litigation, Manuel has treated that short period as part and parcel of the initial unlawful arrest. See, <em>e.g.,</em> Reply Brief 1.</p>
</footnote>
<footnote label="4">
<p id="p-88">See also <em>Singer v. Fulton County Sheriff,</em> <extracted-citation case-ids="7414152" index="98" url="https://cite.case.law/f3d/63/110/#p114"><span class="citation" data-id="6935799"><a href="/opinion/7033453/singer-v-fulton-county-sheriff/" aria-description="Citation for case: Singer v. Fulton County Sheriff">63 F.3d 110</a></span></extracted-citation>, 114-118 (C.A.2 1995) ; <em>McKenna v. Philadelphia,</em> <extracted-citation case-ids="4061656" index="99" url="https://cite.case.law/f3d/582/447/#p461"><span class="citation" data-id="1349366"><a href="/opinion/1349366/mckenna-v-city-of-philadelphia/" aria-description="Citation for case: McKenna v. City of Philadelphia">582 F.3d 447</a></span></extracted-citation>, 461 (C.A.3 2009) ; <em>Lambert v. Williams,</em> <extracted-citation case-ids="11239127" index="100" url="https://cite.case.law/f3d/223/257/#p260"><span class="citation" data-id="2967278"><a href="/opinion/2967278/lambert-v-williams/" aria-description="Citation for case: Lambert v. Williams">223 F.3d 257</a></span></extracted-citation>, 260-262 (C.A.4 2000) ; <em>Castellano v. Fragozo,</em> <extracted-citation case-ids="9298683" index="101" url="https://cite.case.law/f3d/352/939/#p953"><span class="citation" data-id="8408477"><a href="/opinion/8437970/castellano-v-fragozo/" aria-description="Citation for case: Castellano v. Fragozo">352 F.3d 939</a></span></extracted-citation>, 953-954, 959-960 (C.A.5 2003) (en banc); <em>Sykes v. Anderson,</em> <extracted-citation case-ids="3801091" index="102" url="https://cite.case.law/f3d/625/294/#p308"><span class="citation" data-id="178987"><a href="/opinion/178987/sykes-v-anderson/" aria-description="Citation for case: Sykes v. Anderson">625 F.3d 294</a></span></extracted-citation>, 308-309 (C.A.6 2010) ; <em>Galbraith v. County of Santa Clara,</em> <extracted-citation case-ids="11357676" index="103" url="https://cite.case.law/f3d/307/1119/#p1126"><span class="citation" data-id="7014886"><a href="/opinion/7108812/galbraith-v-county-of-santa-clara/" aria-description="Citation for case: Galbraith v. County of Santa Clara">307 F.3d 1119</a></span></extracted-citation>, 1126-1127 (C.A.9 2002) ; <em>Wilkins v. De</em> -<em>Reyes,</em> <extracted-citation case-ids="3582012" index="104" url="https://cite.case.law/f3d/528/790/#p797"><span class="citation" data-id="170833"><a href="/opinion/170833/wilkins-v-dereyes/" aria-description="Citation for case: Wilkins v. DeReyes">528 F.3d 790</a></span></extracted-citation>, 797-799 (C.A.10 2008) ; <em>Whiting v. Traylor,</em> <extracted-citation case-ids="571886" index="105" url="https://cite.case.law/f3d/85/581/#p584"><span class="citation" data-id="70957"><a href="/opinion/70957/whiting-v-traylor/" aria-description="Citation for case: Whiting v. Traylor">85 F.3d 581</a></span></extracted-citation>, 584-586 (C.A.11 1996) ; <em>Pitt v. District of Columbia,</em> <extracted-citation case-ids="3564507,3471212" index="106" url="https://cite.case.law/f3d/491/494/"><span class="citation" data-id="798179"><a href="/opinion/798179/christopher-g-pitt-sr-and-tela-hansom-pitt-v-district-of-columbia/" aria-description="Citation for case: Christopher G. Pitt, Sr. And Tela Hansom-Pitt v. District...">491 F.3d 494</a></span></extracted-citation>, 510-511 (C.A.D.C.2007).</p>
</footnote>
<footnote label="5">
<p id="p-89">The Court repeated the same idea in a follow-on decision to <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em>. In <em>County of Riverside v. McLaughlin,</em> <extracted-citation case-ids="6216695" index="107" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U.S. 44</a></span></extracted-citation>, 47, <extracted-citation case-ids="6216695" index="108" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">111 S.Ct. 1661</a></span></extracted-citation>, <extracted-citation case-ids="6216695" index="109" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">114 L.Ed.2d 49</a></span></extracted-citation> (1991), we considered how quickly a jurisdiction must provide the probable-cause determination that <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em> demanded "as a prerequisite to an extended pretrial detention." In holding that the decision should occur within 48 hours of an arrest, the majority understood its "task [as] articulat[ing] more clearly the boundaries of what is permissible under the Fourth Amendment." <extracted-citation case-ids="6216695" index="110" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">500 U.S., at 56</a></span></extracted-citation>, <extracted-citation case-ids="6216695" index="111" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">111 S.Ct. 1661</a></span></extracted-citation>. In arguing for still greater speed, the principal dissent invoked the original meaning of "the Fourth Amendment's prohibition of 'unreasonable seizures,' insofar as it applies to seizure of the person." <em><extracted-citation case-ids="6216695" index="112" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="6216695" index="112" url="https://cite.case.law/us/500/44/#p47"> at 60</extracted-citation>, <extracted-citation case-ids="6216695" index="113" url="https://cite.case.law/us/500/44/#p47"><span class="citation" data-id="9432264"><a href="/opinion/112585/county-of-riverside-v-mclaughlin/" aria-description="Citation for case: County of Riverside v. McLaughlin">111 S.Ct. 1661</a></span></extracted-citation> (Scalia, J., dissenting). The difference between the two opinions was significant, but the commonality still more so: All Justices agreed that the Fourth Amendment provides the appropriate lens through which to view a claim involving pretrial detention.</p>
</footnote>
<footnote label="6">
<p id="p-90">The opposite view would suggest an untenable result: that a person arrested pursuant to a warrant could not bring a Fourth Amendment claim challenging the reasonableness of even his arrest, let alone any subsequent detention. An arrest warrant, after all, is a way of initiating legal process, in which a magistrate finds probable cause that a person committed a crime. See <em>Wallace v. Kato,</em> <extracted-citation case-ids="3553763" index="114" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">549 U.S. 384</a></span></extracted-citation>, 389, <extracted-citation case-ids="3553763" index="115" url="https://cite.case.law/us/549/384/#p388"><span class="citation" data-id="9435115"><a href="/opinion/145756/wallace-v-kato/" aria-description="Citation for case: Wallace v. Kato">127 S.Ct. 1091</a></span></extracted-citation>, <extracted-citation case-ids="3553763" index="116" url="https://cite.case.law/us/549/384/#p388"><span class="citation no-link">166 L.Ed.2d 973</span></extracted-citation> (2007) (explaining that the seizure of a person was "without legal process" because police officers "did not have a warrant for his arrest"); W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts § 119, pp. 871, 886 (5th ed. 1984) (similar). If legal process is the cut-off point for the Fourth Amendment, then someone arrested (as well as later held) under a warrant procured through false testimony would have to look to the Due Process Clause for relief. But that runs counter to our caselaw. See, <em>e.g.,</em> <em>Whiteley v. Warden, Wyo. State Penitentiary,</em> <extracted-citation case-ids="11714156" index="117" url="https://cite.case.law/us/401/560/#p568"><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">401 U.S. 560</a></span></extracted-citation>, 568-569, <extracted-citation case-ids="11714156" index="118" url="https://cite.case.law/us/401/560/#p568"><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">91 S.Ct. 1031</a></span></extracted-citation>, <extracted-citation case-ids="11714156" index="119" url="https://cite.case.law/us/401/560/#p568"><span class="citation" data-id="9424493"><a href="/opinion/108297/whiteley-v-warden-wyoming-state-penitentiary/" aria-description="Citation for case: Whiteley v. Warden, Wyoming State Penitentiary">28 L.Ed.2d 306</a></span></extracted-citation> (1971) (holding that an arrest violated the Fourth Amendment because a magistrate's warrant was not backed by probable cause). And if the Seventh Circuit would reply that arrest warrants are somehow different-that there is legal process and then again there is <em>legal process</em> -the next (and in our view unanswerable) question would be why.</p>
</footnote>
<footnote label="7">
<p id="p-91">Even the City no longer appears to contest that conclusion. On multiple occasions during oral argument in this Court, the City agreed that "a Fourth Amendment right ... survive[d] the initiation of process" at the hearing in which the county judge found probable cause and ordered detention. Tr. of Oral Arg. 31; see <em>id.,</em> at 33 (concurring with the statement that "once [an] individual is brought ... before a magistrate, and the magistrate using the same bad evidence says, stay here in jail ... until we get to trial, that that period is a violation of the Fourth Amendment"); <em>id.,</em> at 51 (stating that a detainee has "a Fourth Amendment claim" if "misstatements at [such a probable-cause hearing] led to ongoing pretrial seizure").</p>
</footnote>
<footnote label="8">
<p id="p-92">The dissent goes some way toward claiming that a different kind of pretrial legal process-a grand jury indictment or preliminary examination-does expunge such a Fourth Amendment claim. See <em>post,</em> at 927, n. 4 (opinion of ALITO, J.) (raising but "not decid[ing] that question"); <em>post,</em> at 927 - 928 (suggesting an answer nonetheless). The effect of that view would be to cut off Manuel's claim on the date of his grand jury indictment (March 30)-even though that indictment (like the County Court's probable-cause proceeding) was entirely based on false testimony and even though Manuel remained in detention for 36 days longer. See n. 2, <em>supra</em>. Or said otherwise-even though the legal process he received failed to establish the probable cause necessary for his continued confinement. We can see no principled reason to draw that line. Nothing in the nature of the legal proceeding establishing probable cause makes a difference for purposes of the Fourth Amendment: Whatever its precise form, if the proceeding is tainted-as here, by fabricated evidence-and the result is that probable cause is lacking, then the ensuing pretrial detention violates the confined person's Fourth Amendment rights, for all the reasons we have stated. By contrast (and contrary to the dissent's suggestion, see <em>post,</em> at 927, n. 3), once a trial has occurred, the Fourth Amendment drops out: A person challenging the sufficiency of the evidence to support both a conviction and any ensuing incarceration does so under the Due Process Clause of the Fourteenth Amendment. See <em>Jackson v. Virginia,</em> <extracted-citation case-ids="6182418" index="120" url="https://cite.case.law/us/443/307/#p318"><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">443 U.S. 307</a></span></extracted-citation>, 318, <extracted-citation case-ids="6182418" index="121" url="https://cite.case.law/us/443/307/#p318"><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">99 S.Ct. 2781</a></span></extracted-citation>, <extracted-citation case-ids="6182418" index="122" url="https://cite.case.law/us/443/307/#p318"><span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/" aria-description="Citation for case: Jackson v. Virginia">61 L.Ed.2d 560</a></span></extracted-citation> (1979) (invalidating a conviction under the Due Process Clause when "the record evidence could [not] reasonably support a finding of guilt beyond a reasonable doubt"); <em>Thompson v. Louisville,</em> <extracted-citation case-ids="6162984" index="123" url="https://cite.case.law/us/362/199/#p204"><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">362 U.S. 199</a></span></extracted-citation>, 204, <extracted-citation case-ids="6162984" index="124" url="https://cite.case.law/us/362/199/#p204"><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">80 S.Ct. 624</a></span></extracted-citation>, <extracted-citation case-ids="6162984" index="125" url="https://cite.case.law/us/362/199/#p204"><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">4 L.Ed.2d 654</a></span></extracted-citation> (1960) (striking a conviction under the same provision when "the record [wa]s entirely lacking in evidence" of guilt-such that it could not even establish probable cause). <em><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Gerstein</a></span></em> and <em><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">Albright</a></span>,</em> as already suggested, both reflected and recognized that constitutional division of labor. See <em>supra,</em> at 917 - 918. In their words, the Framers "drafted the Fourth Amendment" to address "the matter of <em>pretrial</em> deprivations of liberty," <em>Albright,</em> <extracted-citation case-ids="231967" index="126" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">510 U.S., at 274</a></span></extracted-citation>, <extracted-citation case-ids="231967" index="127" url="https://cite.case.law/us/510/266/#p274"><span class="citation" data-id="9432926"><a href="/opinion/112924/albright-v-oliver/" aria-description="Citation for case: Albright v. Oliver">114 S.Ct. 807</a></span></extracted-citation> (emphasis added), and the Amendment thus provides "standards and procedures" for "the detention of suspects <em>pending trial,</em> " <em>Gerstein,</em> <extracted-citation case-ids="11642843" index="128" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#125" aria-description="Citation for case: Gerstein v. Pugh">420 U.S., at 125</a></span>, n. 27</extracted-citation>, <extracted-citation case-ids="11642843" index="129" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">95 S.Ct. 854</a></span></extracted-citation> (emphasis added).</p>
</footnote>
<footnote label="9">
<p id="p-93">The two exceptions-the Ninth and D.C. Circuits-have not yet weighed in on whether a Fourth Amendment claim like Manuel's includes a "favorable termination" element.</p>
</footnote>
<footnote label="10">
<p id="p-94">The dissent would have us address these questions anyway, on the ground that "the conflict on the malicious prosecution question was the centerpiece of Manuel's argument in favor of certiorari." <em>Post,</em> at 923. But the decision below did not implicate a "conflict on the malicious prosecution question"-because the Seventh Circuit, in holding that detainees like Manuel could not bring a Fourth Amendment claim at all, never considered whether (and, if so, how) that claim should resemble the malicious prosecution tort. Nor did Manuel's petition for certiorari suggest otherwise. The principal part of his question presented-mirroring the one and only Circuit split involving the decision below-reads as follows: "[W]hether an individual's Fourth Amendment right to be free from unreasonable seizure continues beyond legal process." Pet. for Cert. i. That is exactly the issue we have resolved. The rest of Manuel's question did indeed express a view as to what would follow from an affirmative answer ("so as to allow a malicious prosecution claim"). <em><extracted-citation case-ids="11642843" index="130" url="https://cite.case.law/us/420/103/#p111"><span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">Ibid.</a></span></extracted-citation></em> (And as the dissent notes, the Seventh Circuit recounted that he made the same argument in that court. See <em>post,</em> at 923 -924, n. 1.) But as to that secondary issue, we think (for all the reasons just stated) that Manuel jumped the gun. See <em>supra,</em> at 920 - 922. And contra the dissent, his doing so provides no warrant for our doing so too.</p>
<p id="p-95">* * *</p>
</footnote>
</opinion>
```

---
