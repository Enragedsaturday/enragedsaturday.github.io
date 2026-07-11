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

## GROUP: content/cases/Arizona v. Fulminante.md  (`case`, 5 assertions)

### content_page

```
---
title: "Arizona v. Fulminante"
type: case
citation: "499 U.S. 279 (1991)"
parallel_cite: "111 S. Ct. 1246; 113 L. Ed. 2d 302"
neutral_cite: 1991 U.S. LEXIS 1854
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-05-20
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-05-20
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Fulminante
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112566/arizona-v-fulminante/"
  cluster_id: 112566
  opinion_id: 112566
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Colorado v. Connelly]]", "[[Chambers v. Florida]]"]
aliases: []
tags: ["case", "due-process", "confessions", "voluntariness", "harmless-error"]
holding: "The admission of an involuntary/coerced confession is a \"trial error\" subject to harmless-error analysis under Chapman, not automatic…"
lake:
  record_id: Arizona v. Fulminante
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Fulminante

*499 U.S. 279 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Fulminante was suspected of murdering his stepdaughter. While later incarcerated on an unrelated federal charge, he was befriended by Anthony Sarivola, a fellow inmate who was secretly a paid FBI informant. Knowing Fulminante was receiving rough treatment from other inmates over a rumor that he was a child-killer, Sarivola offered to protect him if he told the truth about the murder. Fulminante confessed to Sarivola, and later to Sarivola's wife. Both confessions were admitted at his murder trial; he was convicted and sentenced to death.

## Issue
(1) Whether a confession given out of fear of violence from other inmates, in exchange for an informant's protection, was coerced in violation of due process; and (2) whether the erroneous admission of a coerced confession is subject to harmless-error analysis or instead requires automatic reversal.

## Rule
A credible threat of violence can render a confession involuntary — coercion may be mental, not only physical: "Our cases have made clear that a finding of coercion need not depend upon actual violence by a government agent; a credible threat is sufficient." — 499 U.S. at 287. ^pin-287

The Court then overruled the prior automatic-reversal rule for coerced confessions: "The Court today properly concludes that the admission of an 'involuntary' confession at trial is subject to harmless-error analysis." — *Id.* at 303. ^pin-303

A coerced confession is a "trial error," not a structural defect: "The admission of an involuntary confession—a classic 'trial error'—is markedly different from the other two constitutional violations referred to in the *Chapman* footnote as not being subject to harmless-error analysis." — [*Id.* at 309](https://www.courtlistener.com/opinion/112566/arizona-v-fulminante/#:~:text=though%20a%20%22-,trial%20error%2C). ^pin-309

## Application
On these facts the Court accepted the finding that Fulminante confessed out of fear of physical violence from other inmates — violence Sarivola, a government agent, offered to prevent only if Fulminante confessed — a credible threat that overbore his will and made the confession coerced. And although harmless-error review now applies to such confessions, the Court held that admitting *this* confession was not harmless [[Common Legal Terms#beyond-a-reasonable-doubt|beyond a reasonable doubt]], because the State could not show the jury would have convicted without it.

## Conclusion
The confession was coerced; harmless-error analysis applies to coerced confessions, but the error here was not harmless. The judgment of the Arizona Supreme Court — reversing the conviction and ordering a retrial without the confession — was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Fulminante* is the seminal modern statement that (a) a credible threat of violence can coerce a confession (mental coercion suffices), and (b) the erroneous admission of a coerced confession is "trial error" reviewable for harmlessness under *Chapman v. California*, in contrast to "structural defects" that defy harmless-error analysis.

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Arizona v. Fulminante*, 499 U.S. 279 (1991) — https://www.courtlistener.com/opinion/112566/arizona-v-fulminante/ — pinpoints: 287, 303, 309.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3a45dd065d92b255", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "499 U.S. 279 (1991)", "court": "U.S. Supreme Court", "neutral_cite": "1991 U.S. LEXIS 1854", "official_citation_present": true, "parallel_cite": "111 S. Ct. 1246; 113 L. Ed. 2d 302", "title": "Arizona v. Fulminante", "year": "1991"}}
{"assertion_id": "61caa157c6982d31", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The admission of an involuntary/coerced confession is a \\\"trial error\\\" subject to harmless-error analysis under Chapman, not automatic…", "title": "Arizona v. Fulminante"}}
{"assertion_id": "8ac4019df1111c3a", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Arizona v. Fulminante"}}
{"assertion_id": "68b7f88762fe1345", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1991-05-20", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arizona v. Fulminante", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Arizona v. Fulminante", "varies_by_point": "false"}}
{"assertion_id": "d1dbe92018feef80", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Fulminante"}}
```

### lake record — Arizona v. Fulminante

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Fulminante",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Fulminante",
    "case_name_short": "Fulminante",
    "case_name_full": "Arizona v. Fulminante",
    "input_case_name": "Arizona v. Fulminante",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-05-20",
    "year": 1991,
    "docket": null,
    "cluster_id": 112566,
    "lead_opinion_id": 112566,
    "sibling_ids": [
      112566,
      9432240,
      9432241,
      9432242
    ],
    "absolute_url": "/opinion/112566/arizona-v-fulminante/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9109110,
        "score": 10,
        "case_name": "Arizona v. Fulminante"
      },
      {
        "cluster_id": 9109109,
        "score": 10,
        "case_name": "Arizona v. Fulminante"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "499 U.S. 279",
      "volume": "499",
      "reporter": "U.S.",
      "page": "279",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 1246",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 302",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 1854",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "1854",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "499 U.S. 279",
        "volume": "499",
        "reporter": "U.S.",
        "page": "279",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 1246",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "1246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "113 L. Ed. 2d 302",
        "volume": "113",
        "reporter": "L. Ed. 2d",
        "page": "302",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 1854",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "1854",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "499 U.S. 279",
    "official_selection": {
      "court_class": "scotus",
      "selected": "499 U.S. 279",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-287",
      "page": null,
      "quote": "--- # Arizona v. Fulminante *499 U.S. 279 (1991)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Fulminante was suspected of murdering his stepdaughter. While later incarcerated on an unrelated federal charge, he was befriended by Anthony Sarivola, a fellow inmate who was secretly a paid FBI informant. Knowing Fulminante was receiving rough treatment from other inmates over a rumor that he was a child-killer, Sarivola offered to protect him if he told the truth about the murder. Fulminante confessed to Sarivola, and later to Sarivola's wife. Both confessions were admitted at his murder trial; he was convicted and sentenced to death. ## Issue (1) Whether a confession given out of fear of violence from other inmates, in exchange for an informant's protection, was coerced in violation of due process; and (2) whether the erroneous admission of a coerced confession is subject to harmless-error analysis or instead requires automatic reversal. ## Rule A credible threat of violence can render a confession involuntary \u2014 coercion may be mental, not only physical:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-303",
      "page": null,
      "quote": "The Court today properly concludes that the admission of an 'involuntary' confession at trial is subject to harmless-error analysis.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-309",
      "page": null,
      "quote": "trial error,",
      "star_marker": "291",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 33183,
      "fragment": "#:~:text=though%20a%20%22-,trial%20error%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-05-20",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Fulminante",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Louisiana v. Michael Steven White",
          "cluster_id": 10804933,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Chambers",
          "cluster_id": 10603767,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Chambers",
          "cluster_id": 10591292,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Watt",
          "cluster_id": 9459195,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jenkins v. State",
          "cluster_id": 10680001,
          "cite": [
            "894 S.E.2d 566",
            "317 Ga. 585"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Eric Calvin Tuazon v. the State of Texas",
          "cluster_id": 9380404,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Olano",
          "cluster_id": 112848,
          "cite": [
            "123 L. Ed. 2d 508",
            "113 S. Ct. 1770",
            "507 U.S. 725",
            "1993 U.S. LEXIS 2986"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heck v. Humphrey",
          "cluster_id": 117864,
          "cite": [
            "129 L. Ed. 2d 383",
            "114 S. Ct. 2364",
            "512 U.S. 477",
            "1994 U.S. LEXIS 4824"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lee",
          "cluster_id": 773551,
          "cite": [
            "252 F.3d 676",
            "2001 U.S. App. LEXIS 10698",
            "2001 WL 558079"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brecht v. Abrahamson",
          "cluster_id": 112845,
          "cite": [
            "123 L. Ed. 2d 353",
            "113 S. Ct. 1710",
            "507 U.S. 619",
            "1993 U.S. LEXIS 2981"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Puckett v. United States",
          "cluster_id": 145896,
          "cite": [
            "173 L. Ed. 2d 266",
            "129 S. Ct. 1423",
            "556 U.S. 129",
            "2009 U.S. LEXIS 2330"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neder v. United States",
          "cluster_id": 118298,
          "cite": [
            "144 L. Ed. 2d 35",
            "119 S. Ct. 1827",
            "527 U.S. 1",
            "1999 U.S. LEXIS 4007"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Mateo",
          "cluster_id": 2006639,
          "cite": [
            "811 N.E.2d 1053",
            "2 N.Y.3d 383",
            "779 N.Y.S.2d 399",
            "2 N.Y. 383",
            "2004 N.Y. LEXIS 263"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. United States",
          "cluster_id": 118106,
          "cite": [
            "137 L. Ed. 2d 718",
            "117 S. Ct. 1544",
            "520 U.S. 461",
            "1997 U.S. LEXIS 2847"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lockhart v. Fretwell",
          "cluster_id": 112807,
          "cite": [
            "122 L. Ed. 2d 180",
            "113 S. Ct. 838",
            "506 U.S. 364",
            "1993 U.S. LEXIS 1016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sullivan v. Louisiana",
          "cluster_id": 112868,
          "cite": [
            "124 L. Ed. 2d 182",
            "113 S. Ct. 2078",
            "508 U.S. 275",
            "1993 U.S. LEXIS 3741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lewis",
          "cluster_id": 4902617,
          "cite": [
            "281 Cal. Rptr. 3d 521",
            "491 P.3d 309",
            "11 Cal. 5th 952"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gaudin",
          "cluster_id": 117958,
          "cite": [
            "132 L. Ed. 2d 444",
            "115 S. Ct. 2310",
            "515 U.S. 506",
            "1995 U.S. LEXIS 4068"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Edwards v. Balisok",
          "cluster_id": 118112,
          "cite": [
            "137 L. Ed. 2d 906",
            "117 S. Ct. 1584",
            "520 U.S. 641",
            "1997 U.S. LEXIS 3075"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Dominguez Benitez",
          "cluster_id": 136986,
          "cite": [
            "159 L. Ed. 2d 157",
            "124 S. Ct. 2333",
            "542 U.S. 74",
            "2004 U.S. LEXIS 4177",
            "17 Fla. L. Weekly Fed. S 379",
            "72 U.S.L.W. 4478"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gonzalez-Lopez",
          "cluster_id": 145633,
          "cite": [
            "165 L. Ed. 2d 409",
            "126 S. Ct. 2557",
            "548 U.S. 140",
            "2006 U.S. LEXIS 5165",
            "19 Fla. L. Weekly Fed. S 368",
            "33 A.L.R. Fed. 2d 661",
            "74 U.S.L.W. 4453"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Breverman",
          "cluster_id": 1198942,
          "cite": [
            "960 P.2d 1094",
            "77 Cal. Rptr. 2d 870",
            "19 Cal. 4th 142",
            "98 Cal. Daily Op. Serv. 6812",
            "98 Daily Journal DAR 9358",
            "1998 Cal. LEXIS 5589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ewing v. California",
          "cluster_id": 127897,
          "cite": [
            "155 L. Ed. 2d 108",
            "123 S. Ct. 1179",
            "538 U.S. 11",
            "2003 U.S. LEXIS 1952"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mickens v. Taylor",
          "cluster_id": 118492,
          "cite": [
            "152 L. Ed. 2d 291",
            "122 S. Ct. 1237",
            "535 U.S. 162",
            "2002 U.S. LEXIS 2146"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bergerud",
          "cluster_id": 2592837,
          "cite": [
            "223 P.3d 686",
            "2010 WL 59254"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ward",
          "cluster_id": 2460345,
          "cite": [
            "256 P.3d 801",
            "292 Kan. 541",
            "2011 Kan. LEXIS 249"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Green v. State",
          "cluster_id": 1657475,
          "cite": [
            "934 S.W.2d 92",
            "1996 Tex. Crim. App. LEXIS 185",
            "1996 WL 512395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mendez v. State",
          "cluster_id": 1449351,
          "cite": [
            "138 S.W.3d 334",
            "2004 Tex. Crim. App. LEXIS 1031",
            "2004 WL 1462178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Esparza",
          "cluster_id": 131144,
          "cite": [
            "157 L. Ed. 2d 263",
            "124 S. Ct. 7",
            "540 U.S. 12",
            "2003 U.S. LEXIS 8191"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Washington v. Recuenco",
          "cluster_id": 145631,
          "cite": [
            "165 L. Ed. 2d 466",
            "126 S. Ct. 2546",
            "548 U.S. 212",
            "2006 U.S. LEXIS 5164"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Fulminante:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjc3MTEwNDAwMDAwJnM9OTM4MDQwNCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112566+OR+9432240+OR+9432241+OR+9432242%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03Mzgmcz00ODkxNDUzJnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112566+OR+9432240+OR+9432241+OR+9432242%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242)",
        "reviewed": 196,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 5,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 196,
        "triage_read": 5,
        "triage_snippet_classified": 191
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112566 OR 9432240 OR 9432241 OR 9432242)",
    "indexed_citing_opinions": 3674,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112566,
        "count": 3108,
        "count_source": "search"
      },
      {
        "opinion_id": 9432240,
        "count": 645,
        "count_source": "search"
      },
      {
        "opinion_id": 9432241,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432242,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6063,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-fulminante.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk0Njc4NDkmcz0xMDY0NDc2NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112566+OR+9432240+OR+9432241+OR+9432242%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112566,
        "cited_id": 94082,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 101031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 103301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104010,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104108,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105690,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105917,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106545,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106595,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 106881,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107261,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107318,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107359,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107684,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 107952,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108111,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108182,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108184,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108635,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110081,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 110933,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111095,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111194,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111625,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111687,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111750,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 111949,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112291,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112298,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 375540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 420788,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 457158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 463284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 466083,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 487141,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 1155888,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 1298321,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112566,
        "cited_id": 2499246,
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
    "date_created": "2026-07-04T18:14:58Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:15:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:15:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:20:38Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:15:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Fulminante

```
<div>
<center><b><span class="citation" data-id="9432240"><a href="/opinion/112566/arizona-v-fulminante/" aria-description="Citation for case: Arizona v. Fulminante">499 U.S. 279</a></span> (1991)</b></center>
<center><h1>ARIZONA<br>
v.<br>
FULMINANTE</h1></center>
<center>No. 89-839.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued October 10, 1990.</center>
<center>Decided March 26, 1991.</center>
CERTIORARI TO THE SUPREME COURT OF ARIZONA
<p><span class="star-pagination">*281</span> <i>Barbara M. Jarrett,</i> Senior Assistant Attorney General of Arizona, argued the cause for petitioner. With her on the briefs were <i>Robert K. Corbin,</i> Attorney General, and <i>Jessica Gifford Funkhouser.</i></p>
<p><i>Paul J. Larkin, Jr.,</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Joel M. Gershowitz.</i></p>
<p><i>Stephen R. Collins,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./495/902/">495 U. S. 902</a></span>, argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*282</span> JUSTICE WHITE delivered an opinion, Parts I, II, and IV of which are the opinion of the Court, and Part III of which is a dissenting opinion.<sup>[]</sup></p>
<p>The Arizona Supreme Court ruled in this case that respondent Oreste Fulminante's confession, received in evidence at his trial for murder, had been coerced and that its use against him was barred by the Fifth and Fourteenth Amendments to the United States Constitution. The court also held that the harmless-error rule could not be used to save the conviction. We affirm the judgment of the Arizona court, although for different reasons than those upon which that court relied.</p>
<p></p>
<h2>I</h2>
<p>Early in the morning of September 14, 1982, Fulminante called the Mesa, Arizona, Police Department to report that his 11-year-old stepdaughter, Jeneane Michelle Hunt, was missing. He had been caring for Jeneane while his wife, Jeneane's mother, was in the hospital. Two days later, Jeneane's body was found in the desert east of Mesa. She had been shot twice in the head at close range with a large caliber weapon, and a ligature was around her neck. Because of the decomposed condition of the body, it was impossible to tell whether she had been sexually assaulted.</p>
<p>Fulminante's statements to police concerning Jeneane's disappearance and his relationship with her contained a number of inconsistencies, and he became a suspect in her killing. When no charges were filed against him, Fulminante left Arizona for New Jersey. Fulminante was later convicted in New Jersey on federal charges of possession of a firearm by a felon.</p>
<p>Fulminante was incarcerated in the Ray Brook Federal Correctional Institution in New York. There he became <span class="star-pagination">*283</span> friends with another inmate, Anthony Sarivola, then serving a 60-day sentence for extortion. The two men came to spend several hours a day together. Sarivola, a former police officer, had been involved in loansharking for organized crime but then became a paid informant for the Federal Bureau of Investigation. While at Ray Brook, he masqueraded as an organized crime figure. After becoming friends with Fulminante, Sarivola heard a rumor that Fulminante was suspected of killing a child in Arizona. Sarivola then raised the subject with Fulminante in several conversations, but Fulminante repeatedly denied any involvement in Jeneane's death. During one conversation, he told Sarivola that Jeneane had been killed by bikers looking for drugs; on another occasion, he said he did not know what had happened. Sarivola passed this information on to an agent of the Federal Bureau of Investigation, who instructed Sarivola to find out more.</p>
<p>Sarivola learned more one evening in October 1983, as he and Fulminante walked together around the prison track. Sarivola said that he knew Fulminante was "starting to get some tough treatment and whatnot" from other inmates because of the rumor. App. 83. Sarivola offered to protect Fulminante from his fellow inmates, but told him, "`You have to tell me about it,' you know. I mean, in other words, `For me to give you any help.'" <i>Ibid.</i> Fulminante then admitted to Sarivola that he had driven Jeneane to the desert on his motorcycle, where he choked her, sexually assaulted her, and made her beg for her life, before shooting her twice in the head. <i>Id.,</i> at 84-85.</p>
<p>Sarivola was released from prison in November 1983. Fulminante was released the following May, only to be arrested the next month for another weapons violation. On September 4, 1984, Fulminante was indicted in Arizona for the first-degree murder of Jeneane.</p>
<p>Prior to trial, Fulminante moved to suppress the statement he had given Sarivola in prison, as well as a second confession <span class="star-pagination">*284</span> he had given to Donna Sarivola, then Anthony Sarivola's fiancée and later his wife, following his May 1984 release from prison. He asserted that the confession to Sarivola was coerced, and that the second confession was the "fruit" of the first. <i>Id.,</i> at 6-8. Following the hearing, the trial court denied the motion to suppress, specifically finding that, based on the stipulated facts, the confessions were voluntary. <i>Id.,</i> at 44, 63. The State introduced both confessions as evidence at trial, and on December 19, 1985, Fulminante was convicted of Jeneane's murder. He was subsequently sentenced to death.</p>
<p>Fulminante appealed, arguing, among other things, that his confession to Sarivola was the product of coercion and that its admission at trial violated his rights to due process under the Fifth and Fourteenth Amendments to the United States Constitution. After considering the evidence at trial as well as the stipulated facts before the trial court on the motion to suppress, the Arizona Supreme Court held that the confession was coerced, but initially determined that the admission of the confession at trial was harmless error, because of the overwhelming nature of the evidence against Fulminante. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">161 Ariz. 237</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">778 P. 2d 602</a></span> (1988). Upon Fulminante's motion for reconsideration, however, the court ruled that this Court's precedent precluded the use of the harmless-error analysis in the case of a coerced confession. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#262" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 262</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#627" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 627</a></span>. The court therefore reversed the conviction and ordered that Fulminante be retried without the use of the confession to Sarivola.<sup>[1]</sup> Because of differing <span class="star-pagination">*285</span> views in the state and federal courts over whether the admission at trial of a coerced confession is subject to a harmless-error analysis, we granted the State's petition for certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./494/1055/">494 U. S. 1055</a></span> (1990). Although a majority of this Court finds that such a confession is subject to a harmless-error analysis, for the reasons set forth below, we affirm the judgment of the Arizona court.</p>
<p></p>
<h2>II</h2>
<p>We deal first with the State's contention that the court below erred in holding Fulminante's confession to have been coerced. The State argues that it is the totality of the circumstances that determines whether Fulminante's confession was coerced, cf. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span> (1973), but contends that rather than apply this standard, the Arizona court applied a "but for" test, under which the court found that but for the promise given by Sarivola, Fulminante would not have confessed. Brief for Petitioner 14-15. In support of this argument, the State points to the Arizona court's reference to <i>Bram</i> v. <i>United States,</i> <span class="citation multiple-matches"><a href="/c/U.%20S./168/532/">168 U. S. 532</a></span> (1897). Although the Court noted in <i>Bram</i> that a confession cannot be obtained by "`any direct or implied promises, however slight, nor by the exertion of any improper influence,'" <i>id.,</i> at 542-543 (quoting 3 H. Smith &amp; A. Keep, Russell on Crimes and Misdemeanors 478 (6th ed. 1896)), it is clear that this passage from <i>Bram,</i> which under current precedent does not state the standard for determining the voluntariness of a confession, was not relied on by the Arizona court in reaching its conclusion. Rather, the court cited this language as part of a longer quotation from an Arizona case which accurately described the State's burden of proof for establishing voluntariness. See <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 244</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 609</a></span> (citing <i>State</i> v. <i>Thomas,</i> <span class="citation" data-id="1155888"><a href="/opinion/1155888/state-v-thomas/#227" aria-description="Citation for case: State v. Thomas">148 Ariz. 225, 227</a></span>, <span class="citation" data-id="1155888"><a href="/opinion/1155888/state-v-thomas/#397" aria-description="Citation for case: State v. Thomas">714 P. 2d 395, 397</a></span> (1986); <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#7" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 7</a></span> (1964); and <i>Bram, supra,</i> at 542-543). Indeed, the Arizona Supreme Court stated that a "determination regarding <span class="star-pagination">*286</span> the voluntariness of a confession . . . must be viewed in a totality of the circumstances," <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>, and under that standard plainly found that Fulminante's statement to Sarivola had been coerced.</p>
<p>In applying the totality of the circumstances test to determine that the confession to Sarivola was coerced, the Arizona Supreme Court focused on a number of relevant facts. First, the court noted that "because [Fulminante] was an alleged child murderer, he was in danger of physical harm at the hands of other inmates." <i><span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">Ibid.</a></span></i> In addition, Sarivola was aware that Fulminante had been receiving "`rough treatment from the guys.'" <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 244, n. 1</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#609" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 609, n. 1</a></span>. Using his knowledge of these threats, Sarivola offered to protect Fulminante in exchange for a confession to Jeneane's murder, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante"><i>id.,</i> at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>, and "[i]n response to Sarivola's offer of protection, [Fulminante] confessed." <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 244</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#609" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 609</a></span>. Agreeing with Fulminante that "Sarivola's promise was `extremely coercive,'" <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante"><i>id.,</i> at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>, the Arizona court declared: "[T]he confession was obtained as a direct result of extreme coercion and was tendered in the belief that the defendant's life was in jeopardy if he did not confess. This is a true coerced confession in every sense of the word." <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#262" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 262</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#627" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 627</a></span>.<sup>[2]</sup></p>
<p><span class="star-pagination">*287</span> We normally give great deference to the factual findings of the state court. <i>Davis</i> v. <i>North Carolina,</i> <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina">384 U. S. 737, 741</a></span> (1966); <i>Haynes</i> v. <i>Washington,</i> <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington">373 U. S. 503, 515</a></span> (1963); <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#603" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 603-604</a></span> (1961). Nevertheless, "the ultimate issue of `voluntariness' is a legal question requiring independent federal determination." <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#110" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 110</a></span> (1985). See also <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 398</a></span> (1978); <span class="citation" data-id="9423253"><a href="/opinion/107261/davis-v-north-carolina/#741" aria-description="Citation for case: Davis v. North Carolina"><i>Davis, supra,</i> at 741-742</a></span>; <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#515" aria-description="Citation for case: Haynes v. Washington"><i>Haynes, supra,</i> at 515</a></span>; <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#228" aria-description="Citation for case: Chambers v. Florida">309 U. S. 227, 228-229</a></span> (1940).</p>
<p>Although the question is a close one, we agree with the Arizona Supreme Court's conclusion that Fulminante's confession was coerced.<sup>[3]</sup> The Arizona Supreme Court found a credible threat of physical violence unless Fulminante confessed. Our cases have made clear that a finding of coercion need not depend upon actual violence by a government agent;<sup>[4]</sup> a credible threat is sufficient. As we have said, "coercion can be mental as well as physical, and . . . the blood of the accused is not the only hallmark of an unconstitutional inquisition." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 206</a></span> (1960). See also <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#584" aria-description="Citation for case: Culombe v. Connecticut"><i>Culombe, supra,</i> at 584</a></span>; <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 440-441</a></span> (1961); <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540</a></span> (1961); <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>, 561 <span class="star-pagination">*288</span> (1958); <i>Watts</i> v. <i>Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#52" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 52</a></span> (1949). As in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span>,</i> where the Court found that a confession was coerced because the interrogating police officer had promised that if the accused confessed, the officer would protect the accused from an angry mob outside the jailhouse door, <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#564" aria-description="Citation for case: Payne v. Arkansas">356 U. S., at 564-565, 567</a></span>, so too here, the Arizona Supreme Court found that it was fear of physical violence, absent protection from his friend (and Government agent) Sarivola, which motivated Fulminante to confess. Accepting the Arizona court's finding, permissible on this record, that there was a credible threat of physical violence, we agree with its conclusion that Fulminante's will was overborne in such a way as to render his confession the product of coercion.</p>
<p></p>
<h2>III</h2>
<p>Four of us, JUSTICES MARSHALL, BLACKMUN, STEVENS, and myself, would affirm the judgment of the Arizona Supreme Court on the ground that the harmless-error rule is inapplicable to erroneously admitted coerced confessions. We thus disagree with the Justices who have a contrary view.</p>
<p>The majority today abandons what until now the Court has regarded as the "axiomatic [proposition] that a defendant in a criminal case is deprived of due process of law if his conviction is founded, in whole or in part, upon an involuntary confession, without regard for the truth or falsity of the confession, <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534</a></span> [(1961)], and even though there is ample evidence aside from the confession to support the conviction. <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/" aria-description="Citation for case: Malinski v. New York">324 U. S. 401</a></span> [(1945)]; <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span> [(1952)]; <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span>." <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#376" aria-description="Citation for case: Jackson v. Denno">378 U. S. 368, 376</a></span> (1964). The Court has repeatedly stressed that the view that the admission of a coerced confession can be harmless error because of the other evidence to support the verdict is "an impermissible doctrine," <i>Lynumn</i> v. <i>Illinois,</i> <span class="citation" data-id="106558"><a href="/opinion/106558/lynumn-v-illinois/#537" aria-description="Citation for case: Lynumn v. Illinois">372 U. S. 528, 537</a></span> (1963); for "the admission in evidence, <span class="star-pagination">*289</span> over objection, of the coerced confession vitiates the judgment because it violates the Due Process Clause of the Fourteenth Amendment," <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas"><i>Payne, supra,</i> at 568</a></span>. See also <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#578" aria-description="Citation for case: Rose v. Clark">478 U. S. 570, 578, n. 6</a></span> (1986); <i>New Jersey</i> v. <i>Portash,</i> <span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash">440 U. S. 450, 459</a></span> (1979); <i>Lego</i> v. <i>Twomey,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#483" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 483</a></span> (1972); <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#23" aria-description="Citation for case: Chapman v. California">386 U. S. 18, 23</a></span>, and n. 8 (1967); <i>Haynes</i> v. <span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/#518" aria-description="Citation for case: Haynes v. Washington"><i>Washington, supra,</i> at 518</a></span>; <i>Blackburn</i> v. <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama"><i>Alabama, supra,</i> at 206</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#324" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 324</a></span> (1959); <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#475" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 475</a></span> (1953); <i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/#190" aria-description="Citation for case: Stroble v. California">343 U. S. 181, 190</a></span> (1952); <i>Gallegos</i> v. <i>Nebraska,</i> <span class="citation" data-id="9420632"><a href="/opinion/104933/gallegos-v-nebraska/#63" aria-description="Citation for case: Gallegos v. Nebraska">342 U. S. 55, 63</a></span> (1951); <i>Haley</i> v. <i>Ohio,</i> <span class="citation" data-id="9420075"><a href="/opinion/104491/haley-v-ohio/#599" aria-description="Citation for case: Haley v. Ohio">332 U. S. 596, 599</a></span> (1948); <i>Malinski</i> v. <i>New York,</i> <span class="citation" data-id="9419616"><a href="/opinion/104108/malinski-v-new-york/#404" aria-description="Citation for case: Malinski v. New York">324 U. S. 401, 404</a></span> (1945); <i>Lyons</i> v. <i>Oklahoma,</i> <span class="citation" data-id="9419526"><a href="/opinion/104010/lyons-v-oklahoma/#597" aria-description="Citation for case: Lyons v. Oklahoma">322 U. S. 596, 597, n. 1</a></span> (1944). As the decisions in <i><span class="citation" data-id="9422619"><a href="/opinion/106625/haynes-v-washington/" aria-description="Citation for case: Haynes v. Washington">Haynes</a></span></i> and <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne, supra,</a></span></i> show, the rule was the same even when another confession of the defendant had been properly admitted into evidence. Today, a majority of the Court, without any justification, cf. <i>Arizona</i> v. <i>Rumsey,</i> <span class="citation" data-id="9842058"><a href="/opinion/111194/arizona-v-rumsey/#212" aria-description="Citation for case: Arizona v. Rumsey">467 U. S. 203, 212</a></span> (1984), overrules this vast body of precedent without a word and in so doing dislodges one of the fundamental tenets of our criminal justice system.</p>
<p>In extending to coerced confessions the harmless-error rule of <i>Chapman</i> v. <i>California, supra</i><i>,</i> the majority declares that because the Court has applied that analysis to numerous other "trial errors," there is no reason that it should not apply to an error of this nature as well. The four of us remain convinced, however, that we should abide by our cases that have refused to apply the harmless-error rule to coerced confessions, for a coerced confession is fundamentally different from other types of erroneously admitted evidence to which the rule has been applied. Indeed, as the majority concedes, <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> itself recognized that prior cases "have indicated that there are some constitutional rights so basic to a fair trial that their infraction can <i>never</i> be treated as harmless error," and it placed in that category the constitutional rule against using a defendant's coerced confession against <span class="star-pagination">*290</span> him at his criminal trial. <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#23" aria-description="Citation for case: Chapman v. California">386 U. S., at 23</a></span>, and n. 8 (emphasis added). Moreover, cases since <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> have reiterated the rule that using a defendant's coerced confession against him is a denial of due process of law regardless of the other evidence in the record aside from the confession. <i>Lego</i> v. <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#483" aria-description="Citation for case: Lego v. Twomey"><i>Twomey, supra,</i> at 483</a></span>; <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 398</a></span>; <i>New Jersey</i> v. <span class="citation" data-id="9427490"><a href="/opinion/110038/new-jersey-v-portash/#459" aria-description="Citation for case: New Jersey v. Portash"><i>Portash, supra,</i> at 459</a></span>; <i>Rose</i> v. <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#577" aria-description="Citation for case: Rose v. Clark"><i>Clark, supra,</i> at 577, 578</a></span>, and n. 6.</p>
<p><i>Chapman</i> specifically noted three constitutional errors that could not be categorized as harmless error: using a coerced confession against a defendant in a criminal trial, depriving a defendant of counsel, and trying a defendant before a biased judge. The majority attempts to distinguish the use of a coerced confession from the other two errors listed in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> first by distorting the decision in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span>,</i> and then by drawing a meaningless dichotomy between "trial errors" and "structural defects" in the trial process. Viewing <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> as merely rejecting a test whereby the admission of a coerced confession could stand if there were "sufficient evidence," other than the confession, to support the conviction, the majority suggests that the Court in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> might have reached a different result had it been considering a harmless-error test. <i>Post,</i> at 309 (opinion of REHNQUIST, C. J.). It is clear, though, that in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> the Court recognized that <i>regardless</i> of the amount of other evidence, "the admission in evidence, over objection, of the coerced confession vitiates the judgment," because "where, as here, a coerced confession constitutes a part of the evidence before the jury and a general verdict is returned, no one can say what credit and weight the jury gave to the confession." <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas">356 U. S., at 568</a></span>. The inability to assess its effect on a conviction causes the admission at trial of a coerced confession to "defy analysis by `harmless-error' standards," cf. <i>post,</i> at 309 (opinion of REHNQUIST, C. J.), just as certainly as do deprivation of counsel and trial before a biased judge.</p>
<p><span class="star-pagination">*291</span> The majority also attempts to distinguish "trial errors" which occur "during the presentation of the case to the jury," <i>post,</i> at 307, and which it deems susceptible to harmless-error analysis, from "structural defects in the constitution of the trial mechanism," <i>post,</i> at 309, which the majority concedes cannot be so analyzed. This effort fails, for our jurisprudence on harmless error has not classified so neatly the errors at issue. For example, we have held susceptible to harmless-error analysis the failure to instruct the jury on the presumption of innocence, <i>Kentucky</i> v. <i>Whorton,</i> <span class="citation" data-id="9427578"><a href="/opinion/110081/kentucky-v-whorton/" aria-description="Citation for case: Kentucky v. Whorton">441 U. S. 786</a></span> (1979), while finding it impossible to analyze in terms of harmless error the failure to instruct a jury on the reasonable-doubt standard, <i>Jackson</i> v. <i>Virginia,</i> <span class="citation" data-id="9427680"><a href="/opinion/110138/jackson-v-virginia/#320" aria-description="Citation for case: Jackson v. Virginia">443 U. S. 307, 320, n. 14</a></span> (1979). These cases cannot be reconciled by labeling the former "trial error" and the latter not, for both concern the exact same stage in the trial proceedings. Rather, these cases can be reconciled only by considering the nature of the right at issue and the effect of an error upon the trial. A jury instruction on the presumption of innocence is not constitutionally required in every case to satisfy due process, because such an instruction merely offers an additional safeguard beyond that provided by the constitutionally required instruction on reasonable doubt. See <span class="citation" data-id="9427578"><a href="/opinion/110081/kentucky-v-whorton/#789" aria-description="Citation for case: Kentucky v. Whorton"><i>Whorton, supra,</i> at 789</a></span>; <i>Taylor</i> v. <i>Kentucky,</i> <span class="citation" data-id="9427215"><a href="/opinion/109872/taylor-v-kentucky/#488" aria-description="Citation for case: Taylor v. Kentucky">436 U. S. 478, 488-490</a></span> (1978). While it may be possible to analyze as harmless the omission of a presumption of innocence instruction when the required reasonable-doubt instruction has been given, it is impossible to assess the effect on the jury of the omission of the more fundamental instruction on reasonable doubt. In addition, omission of a reasonable-doubt instruction, though a "trial error," distorts the very structure of the trial because it creates the risk that the jury will convict the defendant even if the State has not met its required burden of proof. Cf. <i>Cool</i> v. <i>United States,</i> <span class="citation" data-id="9425051"><a href="/opinion/108635/cool-v-united-states/#104" aria-description="Citation for case: Cool v. United States">409 U. S. 100, 104</a></span> (1972); <i>In re Winship,</i> <span class="citation" data-id="9424220"><a href="/opinion/108111/in-re-winship/#364" aria-description="Citation for case: In Re WINSHIP">397 U. S. 358, 364</a></span> (1970).</p>
<p><span class="star-pagination">*292</span> These same concerns counsel against applying harmless-error analysis to the admission of a coerced confession. A defendant's confession is "probably the most probative and damaging evidence that can be admitted against him," <i>Cruz</i> v. <i>New York,</i> <span class="citation" data-id="9430920"><a href="/opinion/111864/cruz-v-new-york/#195" aria-description="Citation for case: Cruz v. New York">481 U. S. 186, 195</a></span> (1987) (WHITE, J., dissenting), so damaging that a jury should not be expected to ignore it even if told to do so, <i>Bruton</i> v. <i>United States,</i> <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#140" aria-description="Citation for case: Bruton v. United States">391 U. S. 123, 140</a></span> (1968) (WHITE, J., dissenting), and because in any event it is impossible to know what credit and weight the jury gave to the confession. Cf. <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#568" aria-description="Citation for case: Payne v. Arkansas"><i>Payne, supra,</i> at 568</a></span>. Concededly, this reason is insufficient to justify a <i>per se</i> bar to the use of <i>any</i> confession. Thus, <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), applied harmless-error analysis to a confession obtained and introduced in circumstances that violated the defendant's Sixth Amendment right to counsel.<sup>[5]</sup> Similarly, the Courts of Appeals have held that the introduction of incriminating statements taken from defendants in violation of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), is subject to treatment as harmless error.<sup>[6]</sup></p>
<p>Nevertheless, in declaring that it is "impossible to create a meaningful distinction between confessions elicited in violation of the Sixth Amendment and those in violation of the Fourteenth Amendment," <i>post,</i> at 312 (opinion of REHNQUIST, C. J.), the majority overlooks the obvious. Neither <i>Milton</i> v. <i><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">Wainwright</a></span></i> nor any of the other cases upon which <span class="star-pagination">*293</span> the majority relies involved a defendant's <i>coerced</i> confession, nor were there present in these cases the distinctive reasons underlying the exclusion of coerced incriminating statements of the defendant.<sup>[7]</sup> First, some coerced confessions may be untrustworthy. <i>Jackson</i> v. <i>Denno,</i> <span class="citation" data-id="9422864"><a href="/opinion/106881/jackson-v-denno/#385" aria-description="Citation for case: Jackson v. Denno">378 U. S., at 385-386</a></span>; <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#320" aria-description="Citation for case: Spano v. New York">360 U. S., at 320</a></span>. Consequently, admission of coerced confessions may distort the truth-seeking function of the trial upon which the majority focuses. More importantly, however, the use of coerced confessions, "whether true or false," is forbidden "because the methods used to extract them offend an underlying principle in the enforcement of our criminal law: that ours is an accusatorial and not an inquisitorial system  a system in which the State must establish guilt by evidence independently and freely secured and may not by coercion prove its charge against an accused out of his own mouth," <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S., at 540-541</a></span>; see also <i>Lego,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#485" aria-description="Citation for case: Lego v. Twomey">404 U. S., at 485</a></span>. This reflects the "strongly felt attitude of our society that important human values are sacrificed where an agency of the government, in the course of securing a conviction, wrings a confession out of an accused against his will," <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#206" aria-description="Citation for case: Blackburn v. Alabama">361 U. S., at 206-207</a></span>, as well as "the deep-rooted feeling that the police must obey the law while enforcing the law; that in the end life and liberty can be as much endangered from illegal methods used to convict those thought to be criminals as from the actual criminals themselves," <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#320" aria-description="Citation for case: Spano v. New York"><i>Spano, supra,</i> at 320-321</a></span>. Thus, permitting a coerced confession to be part of the evidence on which a jury is free to base its verdict of guilty is inconsistent with the thesis that ours is not an <span class="star-pagination">*294</span> inquisitorial system of criminal justice. Cf. <i>Chambers</i> v. <i>Florida,</i> <span class="citation" data-id="103301"><a href="/opinion/103301/chambers-v-florida/#235" aria-description="Citation for case: Chambers v. Florida">309 U. S., at 235-238</a></span>.</p>
<p>As the majority concedes, there are other constitutional errors that invalidate a conviction even though there may be no reasonable doubt that the defendant is guilty and would be convicted absent the trial error. For example, a judge in a criminal trial "is prohibited from entering a judgment of conviction or directing the jury to come forward with such a verdict, see <i>Sparf &amp; Hansen</i> v. <i>United States,</i> <span class="citation" data-id="9417675"><a href="/opinion/94082/sparf-v-united-states/#105" aria-description="Citation for case: Sparf v. United States">156 U. S. 51, 105</a></span> (1895); <i>Carpenters</i> v. <i>United States,</i> <span class="citation" data-id="9419949"><a href="/opinion/104387/united-brotherhood-of-carpenters-joiners-of-america-v-united-states/#408" aria-description="Citation for case: United Brotherhood of Carpenters &amp; Joiners of America v....">330 U. S. 395, 408</a></span> (1947), regardless of how overwhelmingly the evidence may point in that direction." <i>United States</i> v. <i>Martin Linen Supply Co.,</i> <span class="citation" data-id="9426742"><a href="/opinion/109631/united-states-v-martin-linen-supply-co/#572" aria-description="Citation for case: United States v. Martin Linen Supply Co.">430 U. S. 564, 572-573</a></span> (1977). A defendant is entitled to counsel at trial, <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963), and as <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> recognized, violating this right can never be harmless error. <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#23" aria-description="Citation for case: Chapman v. California">386 U. S., at 23</a></span>, and n. 8. See also <i>White</i> v. <i>Maryland,</i> <span class="citation" data-id="106595"><a href="/opinion/106595/white-v-maryland/" aria-description="Citation for case: White v. Maryland">373 U. S. 59</a></span> (1963), where a conviction was set aside because the defendant had not had counsel at a preliminary hearing without regard to the showing of prejudice. In <i>Vasquez</i> v. <i>Hillery,</i> <span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/" aria-description="Citation for case: Vasquez v. Hillery">474 U. S. 254</a></span> (1986), a defendant was found guilty beyond reasonable doubt, but the conviction had been set aside because of the unlawful exclusion of members of the defendant's race from the grand jury that indicted him, despite overwhelming evidence of his guilt. The error at the grand jury stage struck at fundamental values of our society and "undermine[d] the structural integrity of the criminal tribunal itself, and [was] not amenable to harmless-error review." <span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/#263" aria-description="Citation for case: Vasquez v. Hillery"><i>Id.,</i> at 263-264</a></span>. <i><span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/" aria-description="Citation for case: Vasquez v. Hillery">Vasquez</a></span>,</i> like <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> also noted that rule of automatic reversal when a defendant is tried before a judge with a financial interest in the outcome, <i>Tumey</i> v. <i>Ohio,</i> <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/#535" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510, 535</a></span> (1927), despite a lack of any indication that bias influenced the decision. <i>Waller</i> v. <i>Georgia,</i> <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#49" aria-description="Citation for case: Waller v. Georgia">467 U. S. 39, 49</a></span> (1984), recognized that violation of the guarantee of a public trial required reversal without any showing of prejudice and even though the values <span class="star-pagination">*295</span> of a public trial may be intangible and unprovable in any particular case.</p>
<p>The search for truth is indeed central to our system of justice, but "certain constitutional rights are not, and should not be, subject to harmless-error analysis because those rights protect important values that are unrelated to the truth-seeking function of the trial." <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#587" aria-description="Citation for case: Rose v. Clark">478 U. S., at 587</a></span> (STEVENS, J., concurring in judgment). The right of a defendant not to have his coerced confession used against him is among those rights, for using a coerced confession "abort[s] the basic trial process" and "render[s] a trial fundamentally unfair." <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#577" aria-description="Citation for case: Rose v. Clark"><i>Id.,</i> at 577, 578, n. 6</a></span>.</p>
<p>For the foregoing reasons the four of us would adhere to the consistent line of authority that has recognized as a basic tenet of our criminal justice system, before and after both <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> the prohibition against using a defendant's coerced confession against him at his criminal trial. <i>Stare decisis</i> is "of fundamental importance to the rule of law," <i>Welch</i> v. <i>Texas Dept. of Highways and Public Transportation,</i> <span class="citation" data-id="9431106"><a href="/opinion/111949/welch-v-texas-department-of-highways-public-transportation/#494" aria-description="Citation for case: Welch v. Texas Department of Highways &amp; Public...">483 U. S. 468, 494</a></span> (1987); the majority offers no convincing reason for overturning our long line of decisions requiring the exclusion of coerced confessions.</p>
<p></p>
<h2>IV</h2>
<p>Since five Justices have determined that harmless-error analysis applies to coerced confessions, it becomes necessary to evaluate under that ruling the admissibility of Fulminante's confession to Sarivola. Cf. <i>Pennsylvania</i> v. <i>Union Gas Co.,</i> <span class="citation" data-id="9431727"><a href="/opinion/112291/pennsylvania-v-union-gas-co/#45" aria-description="Citation for case: Pennsylvania v. Union Gas Co.">491 U. S. 1, 45</a></span> (1989) (WHITE, J., concurring in judgment in part and dissenting in part); <span class="citation" data-id="9431727"><a href="/opinion/112291/pennsylvania-v-union-gas-co/#57" aria-description="Citation for case: Pennsylvania v. Union Gas Co."><i>id.,</i> at 57</a></span> (O'CONNOR, J., dissenting). <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#24" aria-description="Citation for case: Chapman v. California">386 U. S., at 24</a></span>, made clear that "before a federal constitutional error can be held harmless, the court must be able to declare a belief that it was harmless beyond a reasonable doubt." The Court has the power to review the record <i>de novo</i> in order to determine an error's harmlessness. See <i>ibid.; </i><i>Satterwhite</i> v. <span class="star-pagination">*296</span> <i>Texas,</i> 486 U. S., at 258. In so doing, it must be determined whether the State has met its burden of demonstrating that the admission of the confession to Sarivola did not contribute to Fulminante's conviction. <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/#26" aria-description="Citation for case: Chapman v. California"><i>Chapman, supra,</i> at 26</a></span>. Five of us are of the view that the State has not carried its burden and accordingly affirm the judgment of the court below reversing respondent's conviction.</p>
<p>A confession is like no other evidence. Indeed, "the defendant's own confession is probably the most probative and damaging evidence that can be admitted against him. . . . [T]he admissions of a defendant come from the actor himself, the most knowledgeable and unimpeachable source of information about his past conduct. Certainly, confessions have profound impact on the jury, so much so that we may justifiably doubt its ability to put them out of mind even if told to do so." <i>Bruton</i> v. <i>United States,</i> <span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/#139" aria-description="Citation for case: Bruton v. United States">391 U. S., at 139-140</a></span> (WHITE, J., dissenting). See also <i>Cruz</i> v. <i>New York,</i> <span class="citation" data-id="9430920"><a href="/opinion/111864/cruz-v-new-york/#195" aria-description="Citation for case: Cruz v. New York">481 U. S., at 195</a></span> (WHITE, J., dissenting) (citing <i><span class="citation" data-id="9423688"><a href="/opinion/107684/bruton-v-united-states/" aria-description="Citation for case: Bruton v. United States">Bruton</a></span></i>). While some statements by a defendant may concern isolated aspects of the crime or may be incriminating only when linked to other evidence, a full confession in which the defendant discloses the motive for and means of the crime may tempt the jury to rely upon that evidence alone in reaching its decision. In the case of a coerced confession such as that given by Fulminante to Sarivola, the risk that the confession is unreliable, coupled with the profound impact that the confession has upon the jury, requires a reviewing court to exercise extreme caution before determining that the admission of the confession at trial was harmless.</p>
<p>In the Arizona Supreme Court's initial opinion, in which it determined that harmless-error analysis could be applied to the confession, the court found that the admissible second confession to Donna Sarivola rendered the first confession to Anthony Sarivola cumulative. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#245" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 245-246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#610" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 610-611</a></span>. The court also noted that circumstantial physical evidence concerning the wounds, the ligature around Jeneane's neck, the location of the body, and the presence of <span class="star-pagination">*297</span> motorcycle tracks at the scene corroborated the second confession. <i><span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/" aria-description="Citation for case: State v. Fulminante">Ibid.</a></span></i> The court concluded that "due to the overwhelming evidence adduced from the second confession, if there had not been a first confession, the jury would still have had the same basic evidence to convict" Fulminante. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#246" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#611" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 611</a></span>.</p>
<p>We have a quite different evaluation of the evidence. Our review of the record leads us to conclude that the State has failed to meet its burden of establishing, beyond a reasonable doubt, that the admission of Fulminante's confession to Anthony Sarivola was harmless error. Three considerations compel this result.</p>
<p>First, the transcript discloses that both the trial court and the State recognized that a successful prosecution depended on the jury believing the two confessions. Absent the confessions, it is unlikely that Fulminante would have been prosecuted at all, because the physical evidence from the scene and other circumstantial evidence would have been insufficient to convict. Indeed, no indictment was filed until nearly two years after the murder.<sup>[8]</sup> App. 2. Although the police had suspected Fulminante from the beginning, as the prosecutor acknowledged in his opening statement to the jury, "[W]hat brings us to Court, what makes this case fileable, and prosecutable and triable is that later, Mr. Fulminante confesses this crime to Anthony Sarivola and later, to Donna Sarivola, his wife." <i>Id.,</i> at 65-66. After trial began, during a renewed hearing on Fulminante's motion to suppress, the trial court opined, "You know, I think from what little I know about this trial, the character of this man [Sarivola] for truthfulness or untruthfulness and his credibility is the centerpiece of this case, is it not?" The prosecutor responded, "It's very important, there's no doubt." <i>Id.,</i> at 62. Finally, in his <span class="star-pagination">*298</span> closing argument, the prosecutor prefaced his discussion of the two confessions by conceding: "[W]e have a lot of [circumstantial] evidence that indicates that this is our suspect, this is the fellow that did it, but it's a little short as far as saying that it's proof that he actually put the gun to the girl's head and killed her. So it's a little short of that. We recognize that." 10 Tr. 75 (Dec. 17, 1985).</p>
<p>Second, the jury's assessment of the confession to Donna Sarivola could easily have depended in large part on the presence of the confession to Anthony Sarivola. Absent the admission at trial of the first confession, the jurors might have found Donna Sarivola's story unbelievable. Fulminante's confession to Donna Sarivola allegedly occurred in May 1984, on the day he was released from Ray Brook, as she and Anthony Sarivola drove Fulminante from New York to Pennsylvania. Donna Sarivola testified that Fulminante, whom she had never before met, confessed in detail about Jeneane's brutal murder in response to her casual question concerning why he was going to visit friends in Pennsylvania instead of returning to his family in Arizona. App. 167-168. Although she testified that she was "disgusted" by Fulminante's disclosures, <i>id.,</i> at 169, she stated that she took no steps to notify authorities of what she had learned, <i>id.,</i> at 172-173. In fact, she claimed that she barely discussed the matter with Anthony Sarivola, who was in the car and overheard Fulminante's entire conversation with Donna. <i>Id.,</i> at 174-175. Despite her disgust for Fulminante, Donna Sarivola later went on a second trip with him. <i>Id.,</i> at 173-174. Although Sarivola informed authorities that he had driven Fulminante to Pennsylvania, he did not mention Donna's presence in the car or her conversation with Fulminante. <i>Id.,</i> at 159-161. Only when questioned by authorities in June 1985 did Anthony Sarivola belatedly recall the confession to Donna more than a year before, and only then did he ask if she would be willing to discuss the matter with authorities. <i>Id.,</i> at 90-92.</p>
<p><span class="star-pagination">*299</span> Although some of the details in the confession to Donna Sarivola were corroborated by circumstantial evidence, many, including details that Jeneane was choked and sexually assaulted, were not. <i>Id.,</i> at 186-188. As to other aspects of the second confession, including Fulminante's motive and state of mind, the <i>only</i> corroborating evidence was the first confession to Anthony Sarivola.<sup>[9]</sup> No. CR 142821 (Super. Ct. Maricopa County, Ariz., Feb. 11, 1986), pp. 3-4. Thus, contrary to what the Arizona Supreme Court found, it is clear that the jury might have believed that the two confessions reinforced and corroborated each other. For this reason, one confession was <i>not</i> merely cumulative of the other. While in some cases two confessions, delivered on different occasions to different listeners, might be viewed as being independent of each other, cf. <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), it strains credulity to think that the jury so viewed the two confessions in this case, especially given the close relationship between Donna and Anthony Sarivola.</p>
<p><span class="star-pagination">*300</span> The jurors could also have believed that Donna Sarivola had a motive to lie about the confession in order to assist her husband. Anthony Sarivola received significant benefits from federal authorities, including payment for information, immunity from prosecution, and eventual placement in the federal Witness Protection Program. App. 79, 114, 129-131. In addition, the jury might have found Donna motivated by her own desire for favorable treatment, for she, too, was ultimately placed in the Witness Protection Program. <i>Id.,</i> at 176, 179-180.</p>
<p>Third, the admission of the first confession led to the admission of other evidence prejudicial to Fulminante. For example, the State introduced evidence that Fulminante knew of Sarivola's connections with organized crime in an attempt to explain why Fulminante would have been motivated to confess to Sarivola in seeking protection. <i>Id.,</i> at 45-48, 67. Absent the confession, this evidence would have had no relevance and would have been inadmissible at trial. The Arizona Supreme Court found that the evidence of Sarivola's connections with organized crime reflected on Sarivola's character, not Fulminante's, and noted that the evidence could have been used to impeach Sarivola. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#245" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 245-246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#610" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 610-611</a></span>. This analysis overlooks the fact that had the confession not been admitted, there would have been no reason for Sarivola to testify and thus no need to impeach his testimony. Moreover, we cannot agree that the evidence did not reflect on Fulminante's character as well, for it depicted him as someone who willingly sought out the company of criminals. It is quite possible that this evidence led the jury to view Fulminante as capable of murder.<sup>[10]</sup></p>
<p><span class="star-pagination">*301</span> Finally, although our concern here is with the effect of the erroneous admission of the confession on Fulminante's conviction, it is clear that the presence of the confession also influenced the sentencing phase of the trial. Under Arizona law, the trial judge is the sentencer. <span class="citation no-link">Ariz. Rev. Stat. Ann. § 13-703</span>(B) (1989). At the sentencing hearing, the admissibility of information regarding aggravating circumstances is governed by the rules of evidence applicable to criminal trials. § 13-703(C). In this case, "based upon admissible evidence produced at the trial," No. CR 142821, <i>supra,</i> at 2, the judge found that only one aggravating circumstance existed beyond a reasonable doubt, <i>i. e.,</i> that the murder was committed in "an <i>especially</i> heinous, cruel, and depraved manner." <i>Ibid.;</i> see § 13-703(F)(6). In reaching this conclusion, the judge relied heavily on evidence concerning the manner of the killing and Fulminante's motives and state of mind which could only be found in the two confessions. For example, in labeling the murder "cruel," the judge focused in part on Fulminante's alleged statements that he choked Jeneane and made her get on her knees and beg before killing her. No. CR 142821, <i>supra,</i> at 3. Although the circumstantial evidence was not inconsistent with this determination, neither was it sufficient to make such a finding beyond a reasonable doubt. Indeed, the sentencing judge acknowledged that the confessions were only partly corroborated by other evidence. <i>Ibid.</i></p>
<p>In declaring that Fulminante "acted with an especially heinous and depraved state of mind," the sentencing judge relied solely on the two confessions. <i>Id.,</i> at 4. While the judge found that the statements in the confessions regarding the alleged sexual assault on Jeneane should not be considered on the issue of cruelty because they were not corroborated by other evidence, the judge determined that they were worthy of belief on the issue of Fulminante's state of <span class="star-pagination">*302</span> mind. <i>Ibid.</i> The judge then focused on Anthony Sarivola's statement that Fulminante had made vulgar references to Jeneane during the first confession, and on Donna Sarivola's statement that Fulminante had made similar comments to her. <i>Ibid.</i> Finally, the judge stressed that Fulminante's alleged comments to the Sarivolas concerning torture, choking, and sexual assault, "whether they all occurred or not," <i>ibid.,</i> depicted "a man who was bragging and relishing the crime he committed." <i>Id.,</i> at 5.</p>
<p>Although the sentencing judge might have reached the same conclusions even without the confession to Anthony Sarivola, it is impossible to say so beyond a reasonable doubt. Furthermore, the judge's assessment of Donna Sarivola's credibility, and hence the reliability of the second confession, might well have been influenced by the corroborative effect of the erroneously admitted first confession. Indeed, the fact that the sentencing judge focused on the similarities between the two confessions in determining that they were reliable suggests that either of the confessions alone, even when considered with all the other evidence, would have been insufficient to permit the judge to find an aggravating circumstance beyond a reasonable doubt as a requisite prelude to imposing the death penalty.</p>
<p>Because a majority of the Court has determined that Fulminante's confession to Anthony Sarivola was coerced and because a majority has determined that admitting this confession was not harmless beyond a reasonable doubt, we agree with the Arizona Supreme Court's conclusion that Fulminante is entitled to a new trial at which the confession is not admitted. Accordingly the judgment of the Arizona Supreme Court is</p>
<p><i>Affirmed.</i></p>
<p>CHIEF JUSTICE REHNQUIST, with whom JUSTICE O'CONNOR joins, JUSTICE KENNEDY and JUSTICE SOUTER join as to Parts I and II, and JUSTICE SCALIA joins as to Parts II and <span class="star-pagination">*303</span> III, delivered the opinion of the Court with respect to Part II, and a dissenting opinion with respect to Parts I and III.</p>
<p>The Court today properly concludes that the admission of an "involuntary" confession at trial is subject to harmless-error analysis. Nonetheless, the independent review of the record which we are required to make shows that respondent Fulminante's confession was not in fact involuntary. And even if the confession were deemed to be involuntary, the evidence offered at trial, including a second, untainted confession by Fulminante, supports the conclusion that any error here was certainly harmless.</p>
<p></p>
<h2>I</h2>
<p>The question whether respondent Fulminante's confession was voluntary is one of federal law. "Without exception, the Court's confession cases hold that the ultimate issue of `voluntariness' is a legal question requiring independent federal determination." <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#110" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 110</a></span> (1985). In <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), we overturned a determination by the Supreme Court of Arizona that a statement of the defendant was voluntary, saying "we are not bound by the Arizona Supreme Court's holding that the statements were voluntary. Instead, this Court is under a duty to make an independent evaluation of the record." <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#398" aria-description="Citation for case: Mincey v. Arizona"><i>Id.,</i> at 398</a></span>.</p>
<p>The admissibility of a confession such as that made by respondent Fulminante depends upon whether it was voluntarily made. "The ultimate test remains that which has been the only clearly established test in Anglo-American courts for two hundred years: the test of voluntariness. Is the confession the product of an essentially free and unconstrained choice by its maker? If it is, if he has willed to confess, it may be used against him. If it is not, if his will has been overborne and his capacity for self-determination critically impaired, the use of his confession offends due process." <span class="star-pagination">*304</span> <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 602</a></span> (1961) (quoted in <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#225" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 225-226</a></span> (1973)).</p>
<p>In this case the parties stipulated to the basic facts at the hearing in the Arizona trial court on respondent's motion to suppress the confession. Anthony Sarivola, an inmate at the Ray Brook Prison, was a paid confidential informant for the FBI. While at Ray Brook, various rumors reached Sarivola that Oreste Fulminante, a fellow inmate who had befriended Sarivola, had killed his stepdaughter in Arizona. Sarivola passed these rumors on to his FBI contact, who told him "to find out more about it." Sarivola, having already discussed the rumors with respondent on several occasions, asked him whether the rumors were true, adding that he might be in a position to protect Fulminante from physical recriminations in prison, but that "[he] must tell him the truth." Fulminante then confessed to Sarivola that he had in fact killed his stepdaughter in Arizona, and provided Sarivola with substantial details about the manner in which he killed the child. At the suppression hearing, Fulminante stipulated to the fact that "[a]t no time did the defendant indicate he was in fear of other inmates nor did he ever seek Mr. Sarivola's `protection.'" App. 10. The trial court was also aware, through an excerpt from Sarivola's interview testimony which respondent appended to his reply memorandum, that Sarivola believed Fulminante's time was "running short" and that he would "have went out of the prison horizontally." <i>Id.,</i> at 28. The trial court found that respondent's confession was voluntary.</p>
<p>The Supreme Court of Arizona stated that the trial court committed no error in finding the confession voluntary based on the record before it. But it overturned the trial court's finding of voluntariness based on the more comprehensive trial record before it, which included, in addition to the facts stipulated at the suppression hearing, a statement made by Sarivola at the trial that "the defendant had been receiving `rough treatment from the guys, and if the defendant would <span class="star-pagination">*305</span> tell the truth, he could be protected.'" <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#244" aria-description="Citation for case: State v. Fulminante">161 Ariz. 237, 244, n. 1</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#609" aria-description="Citation for case: State v. Fulminante">778 P. 2d 602, 609, n. 1</a></span> (1989). It also had before it the presentence report, which showed that Fulminante was no stranger to the criminal justice system: He had six prior felony convictions and had been imprisoned on three prior occasions.</p>
<p>On the basis of the record before it, the Supreme Court stated:</p>
<blockquote>"Defendant contends that because he was an alleged child murderer, he was in danger of physical harm at the hands of other inmates. Sarivola was aware that defendant faced the possibility of retribution from other inmates, and that in return for the confession with respect to the victim's murder, Sarivola would protect him. Moreover, the defendant maintains that Sarivola's promise was `extremely coercive' because the `obvious' inference from the promise was that his life would be in jeopardy if he did not confess. We agree." <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#243" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 243</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#608" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 608</a></span>.</blockquote>
<p>Exercising our responsibility to make the independent examination of the record necessary to decide this federal question, I am at a loss to see how the Supreme Court of Arizona reached the conclusion that it did. Fulminante offered no evidence that he believed that his life was in danger or that he in fact confessed to Sarivola in order to obtain the proffered protection. Indeed, he had stipulated that "[a]t no time did the defendant indicate he was in fear of other inmates nor did he ever seek Mr. Sarivola's `protection.'" App. 10. Sarivola's testimony that he told Fulminante that "if [he] would tell the truth, he could be protected," adds little if anything to the substance of the parties' stipulation. The decision of the Supreme Court of Arizona rests on an assumption that is squarely contrary to this stipulation, and one that is not supported by any testimony of Fulminante.</p>
<p>The facts of record in the present case are quite different from those present in cases where we have found confessions <span class="star-pagination">*306</span> to be coerced and involuntary. Since Fulminante was unaware that Sarivola was an FBI informant, there existed none of "the danger of coercion result[ing] from the interaction of custody and official interrogation." <i>Illinois</i> v. <i>Perkins,</i> <span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/#297" aria-description="Citation for case: Illinois v. Perkins">496 U. S. 292, 297</a></span> (1990). The fact that Sarivola was a Government informant does not by itself render Fulminante's confession involuntary, since we have consistently accepted the use of informants in the discovery of evidence of a crime as a legitimate investigatory procedure consistent with the Constitution. See, <i>e. g., </i><i>Kuhlmann</i> v. <i>Wilson,</i> <span class="citation" data-id="9430620"><a href="/opinion/111726/kuhlmann-v-wilson/" aria-description="Citation for case: Kuhlmann v. Wilson">477 U. S. 436</a></span> (1986); <i>United States</i> v. <i>White,</i> <span class="citation" data-id="9883108"><a href="/opinion/108304/united-states-v-white/" aria-description="Citation for case: United States v. White">401 U. S. 745</a></span> (1971); <i>Hoffa</i> v. <i>United States,</i> <span class="citation" data-id="9423305"><a href="/opinion/107318/hoffa-v-united-states/#304" aria-description="Citation for case: Hoffa v. United States">385 U. S. 293, 304</a></span> (1966). The conversations between Sarivola and Fulminante were not lengthy, and the defendant was free at all times to leave Sarivola's company. Sarivola at no time threatened him or demanded that he confess; he simply requested that he speak the truth about the matter. Fulminante was an experienced habitue of prisons and presumably able to fend for himself. In concluding on these facts that Fulminante's confession was involuntary, the Court today embraces a more expansive definition of that term than is warranted by any of our decided cases.</p>
<p></p>
<h2>II</h2>
<p>Since this Court's landmark decision in <i>Chapman</i> v. <i>California,</i> <span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">386 U. S. 18</a></span> (1967), in which we adopted the general rule that a constitutional error does not automatically require reversal of a conviction, the Court has applied harmless-error analysis to a wide range of errors and has recognized that most constitutional errors can be harmless. See, <i>e. g., </i><i>Clemons</i> v. <i>Mississippi,</i> <span class="citation" data-id="9431962"><a href="/opinion/112400/clemons-v-mississippi/#752" aria-description="Citation for case: Clemons v. Mississippi">494 U. S. 738, 752-754</a></span> (1990) (unconstitutionally overbroad jury instructions at the sentencing stage of a capital case); <i>Satterwhite</i> v. <i>Texas,</i> <span class="citation" data-id="9431315"><a href="/opinion/112080/satterwhite-v-texas/" aria-description="Citation for case: Satterwhite v. Texas">486 U. S. 249</a></span> (1988) (admission of evidence at the sentencing stage of a capital case in violation of the Sixth Amendment Counsel Clause); <i>Carella</i> v. <i>California,</i> <span class="citation" data-id="9431750"><a href="/opinion/112298/carella-v-california/#266" aria-description="Citation for case: Carella v. California">491 U. S. 263, 266</a></span> (1989) <span class="star-pagination">*307</span> (jury instruction containing an erroneous conclusive presumption); <i>Pope</i> v. <i>Illinois,</i> <span class="citation" data-id="9430947"><a href="/opinion/111877/pope-v-illinois/#501" aria-description="Citation for case: Pope v. Illinois">481 U. S. 497, 501-504</a></span> (1987) (jury instruction misstating an element of the offense); <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/" aria-description="Citation for case: Rose v. Clark">478 U. S. 570</a></span> (1986) (jury instruction containing an erroneous rebuttable presumption); <i>Crane</i> v. <i>Kentucky,</i> <span class="citation" data-id="111687"><a href="/opinion/111687/crane-v-kentucky/#691" aria-description="Citation for case: Crane v. Kentucky">476 U. S. 683, 691</a></span> (1986) (erroneous exclusion of defendant's testimony regarding the circumstances of his confession); <i>Delaware</i> v. <i>Van Arsdall,</i> <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/" aria-description="Citation for case: Delaware v. Van Arsdall">475 U. S. 673</a></span> (1986) (restriction on a defendant's right to cross-examine a witness for bias in violation of the Sixth Amendment Confrontation Clause); <i>Rushen</i> v. <i>Spain,</i> <span class="citation" data-id="9429404"><a href="/opinion/111051/rushen-v-spain/#117" aria-description="Citation for case: Rushen v. Spain">464 U. S. 114, 117-118</a></span>, and n. 2 (1983) (denial of a defendant's right to be present at trial); <i>United States</i> v. <i>Hasting,</i> <span class="citation" data-id="9429194"><a href="/opinion/110933/united-states-v-hasting/" aria-description="Citation for case: United States v. Hasting">461 U. S. 499</a></span> (1983) (improper comment on defendant's silence at trial, in violation of the Fifth Amendment Self-Incrimination Clause); <i>Hopper</i> v. <i>Evans,</i> <span class="citation" data-id="9428768"><a href="/opinion/110711/hopper-v-evans/" aria-description="Citation for case: Hopper v. Evans">456 U. S. 605</a></span> (1982) (statute improperly forbidding trial court's giving a jury instruction on a lesser included offense in a capital case in violation of the Due Process Clause); <i>Kentucky</i> v. <i>Whorton,</i> <span class="citation" data-id="9427578"><a href="/opinion/110081/kentucky-v-whorton/" aria-description="Citation for case: Kentucky v. Whorton">441 U. S. 786</a></span> (1979) (failure to instruct the jury on the presumption of innocence); <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#232" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220, 232</a></span> (1977) (admission of identification evidence in violation of the Sixth Amendment Confrontation Clause); <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#231" aria-description="Citation for case: Brown v. United States">411 U. S. 223, 231-232</a></span> (1973) (admission of the out-of-court statement of a nontestifying codefendant in violation of the Sixth Amendment Confrontation Clause); <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972) (confession obtained in violation of <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964)); <i>Chambers</i> v. <i>Maroney,</i> <span class="citation" data-id="9424320"><a href="/opinion/108184/chambers-v-maroney/#52" aria-description="Citation for case: Chambers v. Maroney">399 U. S. 42, 52-53</a></span> (1970) (admission of evidence obtained in violation of the Fourth Amendment); <i>Coleman</i> v. <i>Alabama,</i> <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#10" aria-description="Citation for case: Coleman v. Alabama">399 U. S. 1, 10-11</a></span> (1970) (denial of counsel at a preliminary hearing in violation of the Sixth Amendment Counsel Clause).</p>
<p>The common thread connecting these cases is that each involved "trial error"error which occurred during the presentation of the case to the jury, and which may therefore <span class="star-pagination">*308</span> be quantitatively assessed in the context of other evidence presented in order to determine whether its admission was harmless beyond a reasonable doubt. In applying harmless-error analysis to these many different constitutional violations, the Court has been faithful to the belief that the harmless-error doctrine is essential to preserve the "principle that the central purpose of a criminal trial is to decide the factual question of the defendant's guilt or innocence, and promotes public respect for the criminal process by focusing on the underlying fairness of the trial rather than on the virtually inevitable presence of immaterial error." <span class="citation" data-id="9430412"><a href="/opinion/111625/delaware-v-van-arsdall/#681" aria-description="Citation for case: Delaware v. Van Arsdall"><i>Van Arsdall, supra,</i> at 681</a></span> (citations omitted).</p>
<p>In <i>Chapman</i> v. <i>California, supra</i><i>,</i> the Court stated:</p>
<blockquote>"Although our prior cases have indicated that there are some constitutional rights so basic to a fair trial that their infraction can never be treated as harmless error,8 this statement in <i>Fahy</i> itself belies any belief that all trial errors which violate the Constitution automatically call for reversal.</blockquote>
<blockquote>"8 See, <i>e. g., </i><i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (coerced confession); <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (right to counsel); <i>Tumey</i> v. <i>Ohio,</i> <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510</a></span> (impartial judge)."</blockquote>
<blockquote>
<i>Id.,</i> at 23.</blockquote>
<p>It is on the basis of this language in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> that JUSTICE WHITE in dissent concludes that the principle of <i>stare decisis</i> requires us to hold that an involuntary confession is not subject to harmless-error analysis. We believe that there are several reasons which lead to a contrary conclusion. In the first place, the quoted language from <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> does not by its terms adopt any such rule in that case. The language that "[a]lthough our prior cases have indicated," coupled with the relegation of the cases themselves to a footnote, is more appropriately regarded as a historical reference to the holdings of these cases. This view is buttressed by an examination of the opinion in <i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560</a></span> (1958), which is the case referred to for the proposition that <span class="star-pagination">*309</span> an involuntary confession may not be subject to harmless-error analysis. There the Court said:</p>
<blockquote>"Respondent suggests that, apart from the confession, there was adequate evidence before the jury to sustain the verdict. But where, as here, an involuntary confession constitutes a part of the evidence before the jury and a general verdict is returned, no one can say what credit and weight the jury gave to the confession. And in these circumstances this Court has uniformly held that even though there may have been sufficient evidence, apart from the coerced confession, to support a judgment of conviction, the admission in evidence, over objection, of the coerced confession vitiates the judgment because it violates the Due Process Clause of the Fourteenth Amendment." <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#567" aria-description="Citation for case: Payne v. Arkansas"><i>Id.,</i> at 567-568</a></span>.</blockquote>
<p>It is apparent that the State's argument which the Court rejected in <i><span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/" aria-description="Citation for case: Payne v. Arkansas">Payne</a></span></i> is not the harmless-error analysis later adopted in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> but a much more lenient rule which would allow affirmance of a conviction if the evidence other than the involuntary confession was sufficient to sustain the verdict. This is confirmed by the dissent of Justice Clark in that case, which adopted the more lenient test. Such a test would, of courseunlike the harmless-error testmake the admission of an involuntary confession virtually risk free for the State.</p>
<p>The admission of an involuntary confessiona classic "trial error"is markedly different from the other two constitutional violations referred to in the <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span></i> footnote as not being subject to harmless-error analysis. One of those violations, involved in <i>Gideon</i> v. <i>Wainwright,</i> <span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">372 U. S. 335</a></span> (1963), was the total deprivation of the right to counsel at trial. The other violation, involved in <i>Tumey</i> v. <i>Ohio,</i> <span class="citation" data-id="101031"><a href="/opinion/101031/tumey-v-ohio/" aria-description="Citation for case: Tumey v. Ohio">273 U. S. 510</a></span> (1927), was a judge who was not impartial. These are structural defects in the constitution of the trial mechanism, which defy analysis by "harmless-error" standards. The entire conduct of the trial from beginning to end is obviously <span class="star-pagination">*310</span> affected by the absence of counsel for a criminal defendant, just as it is by the presence on the bench of a judge who is not impartial. Since our decision in <i><span class="citation" data-id="9423348"><a href="/opinion/107359/chapman-v-california/" aria-description="Citation for case: Chapman v. California">Chapman</a></span>,</i> other cases have added to the category of constitutional errors which are not subject to harmless error the following: unlawful exclusion of members of the defendant's race from a grand jury, <i>Vasquez</i> v. <i>Hillery,</i> <span class="citation" data-id="9430252"><a href="/opinion/111552/vasquez-v-hillery/" aria-description="Citation for case: Vasquez v. Hillery">474 U. S. 254</a></span> (1986); the right to self-representation at trial, <i>McKaskle</i> v. <i>Wiggins,</i> <span class="citation" data-id="9429486"><a href="/opinion/111095/mckaskle-v-wiggins/#177" aria-description="Citation for case: McKaskle v. Wiggins">465 U. S. 168, 177-178, n. 8</a></span> (1984); and the right to public trial, <i>Waller</i> v. <i>Georgia,</i> <span class="citation" data-id="111186"><a href="/opinion/111186/waller-v-georgia/#49" aria-description="Citation for case: Waller v. Georgia">467 U. S. 39, 49, n. 9</a></span> (1984). Each of these constitutional deprivations is a similar structural defect affecting the framework within which the trial proceeds, rather than simply an error in the trial process itself. "Without these basic protections, a criminal trial cannot reliably serve its function as a vehicle for determination of guilt or innocence, and no criminal punishment may be regarded as fundamentally fair." <i>Rose</i> v. <i>Clark,</i> <span class="citation" data-id="9430690"><a href="/opinion/111750/rose-v-clark/#577" aria-description="Citation for case: Rose v. Clark">478 U. S., at 577-578</a></span> (citation omitted).</p>
<p>It is evident from a comparison of the constitutional violations which we have held subject to harmless error, and those which we have held not, that involuntary statements or confessions belong in the former category. The admission of an involuntary confession is a "trial error," similar in both degree and kind to the erroneous admission of other types of evidence. The evidentiary impact of an involuntary confession, and its effect upon the composition of the record, is indistinguishable from that of a confession obtained in violation of the Sixth Amendmentof evidence seized in violation of the Fourth Amendmentor of a prosecutor's improper comment on a defendant's silence at trial in violation of the Fifth Amendment. When reviewing the erroneous admission of an involuntary confession, the appellate court, as it does with the admission of other forms of improperly admitted evidence, simply reviews the remainder of the evidence against the defendant to determine whether the admission of the confession was harmless beyond a reasonable doubt.</p>
<p><span class="star-pagination">*311</span> Nor can it be said that the admission of an involuntary confession is the type of error which "transcends the criminal process." This Court has applied harmless-error analysis to the violation of other constitutional rights similar in magnitude and importance and involving the same level of police misconduct. For instance, we have previously held that the admission of a defendant's statements obtained in violation of the Sixth Amendment is subject to harmless-error analysis. In <i>Milton</i> v. <i>Wainwright,</i> <span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">407 U. S. 371</a></span> (1972), the Court held the admission of a confession obtained in violation of <i>Massiah</i> v. <i>United States,</i> <span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), to be harmless beyond a reasonable doubt. We have also held that the admission of an out-of-court statement by a nontestifying codefendant is subject to harmless-error analysis. <i>Brown</i> v. <i>United States,</i> <span class="citation" data-id="108760"><a href="/opinion/108760/brown-v-united-states/#231" aria-description="Citation for case: Brown v. United States">411 U. S., at 231-232</a></span>; <i>Schneble</i> v. <i>Florida,</i> <span class="citation" data-id="9424785"><a href="/opinion/108488/schneble-v-florida/" aria-description="Citation for case: Schneble v. Florida">405 U. S. 427</a></span> (1972); <i>Harrington</i> v. <i>California,</i> <span class="citation" data-id="9424056"><a href="/opinion/107952/harrington-v-california/" aria-description="Citation for case: Harrington v. California">395 U. S. 250</a></span> (1969). The inconsistent treatment of statements elicited in violation of the Sixth and Fourteenth Amendments, respectively, can be supported neither by evidentiary or deterrence concerns nor by a belief that there is something more "fundamental" about involuntary confessions. This is especially true in a case such as this one where there are no allegations of physical violence on behalf of the police. A confession obtained in violation of the Sixth Amendment has the same evidentiary impact as does a confession obtained in violation of a defendant's due process rights. Government misconduct that results in violations of the Fourth and Sixth Amendments may be at least as reprehensible as conduct that results in an involuntary confession. For instance, the prisoner's confession to an inmate-informer at issue in <i><span class="citation" data-id="9424959"><a href="/opinion/108585/milton-v-wainwright/" aria-description="Citation for case: Milton v. Wainwright">Milton</a></span>,</i> which the Court characterized as implicating the Sixth Amendment right to counsel, is similar on its facts to the one we face today. Indeed, experience shows that law enforcement violations of these constitutional guarantees can involve conduct as egregious as police conduct used to elicit statements in violation of the Fourteenth Amendment. It is thus <span class="star-pagination">*312</span> impossible to create a meaningful distinction between confessions elicited in violation of the Sixth Amendment and those in violation of the Fourteenth Amendment.</p>
<p>Of course an involuntary confession may have a more dramatic effect on the course of a trial than do other trial errorsin particular cases it may be devastating to a defendant but this simply means that a reviewing court will conclude in such a case that its admission was not harmless error; it is not a reason for eschewing the harmless-error test entirely. The Supreme Court of Arizona, in its first opinion in the present case, concluded that the admission of Fulminante's confession <i>was</i> harmless error. That court concluded that a second and more explicit confession of the crime made by Fulminante after he was released from prison was not tainted by the first confession, and that the second confession, together with physical evidence from the wounds (the victim had been shot twice in the head with a large calibre weapon at close range and a ligature was found around her neck) and other evidence introduced at trial rendered the admission of the first confession harmless beyond a reasonable doubt. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#245" aria-description="Citation for case: State v. Fulminante">161 Ariz., at 245-246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#610" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 610-611</a></span>.</p>
<p></p>
<h2>III</h2>
<p>I would agree with the finding of the Supreme Court of Arizona in its initial opinionin which it believed harmless-error analysis was applicable to the admission of involuntary confessionsthat the admission of Fulminante's confession was harmless. Indeed, this seems to me to be a classic case of harmless error: a second confession giving more details of the crime than the first was admitted in evidence and found to be free of any constitutional objection. Accordingly, I would affirm the holding of the Supreme Court of Arizona in its initial opinion and reverse the judgment which it ultimately rendered in this case.</p>
<p><span class="star-pagination">*313</span> JUSTICE KENNEDY, concurring in the judgment.</p>
<p>For the reasons stated by THE CHIEF JUSTICE, I agree that Fulminante's confession to Anthony Sarivola was not coerced. In my view, the trial court did not err in admitting this testimony. A majority of the Court, however, finds the confession coerced and proceeds to consider whether harmless-error analysis may be used when a coerced confession has been admitted at trial. With the case in this posture, it is appropriate for me to address the harmless-error issue.</p>
<p>Again for the reasons stated by THE CHIEF JUSTICE, I agree that harmless-error analysis should apply in the case of a coerced confession. That said, the court conducting a harmless-error inquiry must appreciate the indelible impact a full confession may have on the trier of fact, as distinguished, for instance, from the impact of an isolated statement that incriminates the defendant only when connected with other evidence. If the jury believes that a defendant has admitted the crime, it doubtless will be tempted to rest its decision on that evidence alone, without careful consideration of the other evidence in the case. Apart, perhaps, from a video-tape of the crime, one would have difficulty finding evidence more damaging to a criminal defendant's plea of innocence. For the reasons given by JUSTICE WHITE in Part IV of his opinion, I cannot with confidence find admission of Fulminante's confession to Anthony Sarivola to be harmless error.</p>
<p>The same majority of the Court does not agree on the three issues presented by the trial court's determination to admit Fulminante's first confession: whether the confession was inadmissible because coerced; whether harmless-error analysis is appropriate; and if so whether any error was harmless here. My own view that the confession was not coerced does not command a majority.</p>
<p>In the interests of providing a clear mandate to the Arizona Supreme Court in this capital case, I deem it proper to accept in the case now before us the holding of five Justices that the <span class="star-pagination">*314</span> confession was coerced and inadmissible. I agree with a majority of the Court that admission of the confession could not be harmless error when viewed in light of all the other evidence; and so I concur in the judgment to affirm the ruling of the Arizona Supreme Court.</p>
<h2>NOTES</h2>
<p>[*]  <i>Gregory U. Evans, Daniel B. Hales, Joseph A. Morris, George D. Webster, Jack E. Yelverton, Fred E. Inbau, Wayne W. Schmidt, Bernard J. Farber,</i> and <i>James P. Manak</i> filed a brief for Americans for Effective Law Enforcement, Inc., et al. as <i>amici curiae</i> urging reversal.
</p>
<p><i>H. Gerald Beaver</i> and <i>Richard B. Glazier</i> filed a brief for the National Association of Criminal Defense Lawyers as <i>amicus curiae</i> urging affirmance.</p>
<p>[]  JUSTICE MARSHALL, JUSTICE BLACKMUN, and JUSTICE STEVENS join this opinion in its entirety; JUSTICE SCALIA joins Parts I and II; and JUSTICE KENNEDY joins Parts I and IV.</p>
<p>[1]  In its initial opinion, the Arizona Supreme Court had determined that the second confession, to Donna Sarivola, was not the "fruit of the poisonous tree," because it was made six months after the confession to Sarivola; it occurred after Fulminante's need for protection from Sarivola presumably had ended; and it took place in the course of a casual conversation with someone who was not an agent of the State. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#246" aria-description="Citation for case: State v. Fulminante">161 Ariz. 237, 246</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#611" aria-description="Citation for case: State v. Fulminante">778 P. 2d 602, 611</a></span> (1988). The court adhered to this determination in its supplemental opinion. <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#262" aria-description="Citation for case: State v. Fulminante"><i>Id.,</i> at 262</a></span>, <span class="citation" data-id="9855485"><a href="/opinion/1298321/state-v-fulminante/#627" aria-description="Citation for case: State v. Fulminante">778 P. 2d, at 627</a></span>. This aspect of the Arizona Supreme Court's decision is not challenged here.</p>
<p>[2]  There are additional facts in the record, not relied upon by the Arizona Supreme Court, which also support a finding of coercion. Fulminante possesses low average to average intelligence; he dropped out of school in the fourth grade. Record 88i, 88o. He is short in stature and slight in build. <i>Id.,</i> at 88. Although he had been in prison before, <i>ibid.,</i> he had not always adapted well to the stress of prison life. While incarcerated at the age of 26, he had "felt threatened by the [prison] population," <i>id.,</i> at 88x, and he therefore requested that he be placed in protective custody. Once there, however, he was unable to cope with the isolation and was admitted to a psychiatric hospital. <i>Id.,</i> at 88t-88b1. The Court has previously recognized that factors such as these are relevant in determining whether a defendant's will has been overborne. See, <i>e. g., </i><i>Payne</i> v. <i>Arkansas,</i> <span class="citation" data-id="9421616"><a href="/opinion/105690/payne-v-arkansas/#567" aria-description="Citation for case: Payne v. Arkansas">356 U. S. 560, 567</a></span> (1958) (lack of education); <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#441" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 441</a></span> (1961) (low intelligence). Cf. <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span> (1973) (listing potential factors); <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#602" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 602</a></span> (1961) (same). In addition, we note that Sarivola's position as Fulminante's friend might well have made the latter particularly susceptible to the former's entreaties. See <i>Spano</i> v. <i>New York,</i> <span class="citation" data-id="9421842"><a href="/opinion/105917/spano-v-new-york/#323" aria-description="Citation for case: Spano v. New York">360 U. S. 315, 323</a></span> (1959).</p>
<p>[3]  Our prior cases have used the terms "coerced confession" and "involuntary confession" interchangeably "by way of convenient shorthand." <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#207" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 207</a></span> (1960). We use the former term throughout this opinion, as that is the term used by the Arizona Supreme Court.</p>
<p>[4]  The parties agree that Sarivola acted as an agent of the Government when he questioned Fulminante about the murder and elicited the confession. Brief for Petitioner 19; Brief for Respondent 2.</p>
<p>[5]  In <i>Satterwhite</i> v. <i>Texas,</i> <span class="citation" data-id="9431315"><a href="/opinion/112080/satterwhite-v-texas/" aria-description="Citation for case: Satterwhite v. Texas">486 U. S. 249</a></span> (1988), and <i>Moore</i> v. <i>Illinois,</i> <span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220</a></span> (1977), the harmless-error rule was applied to the admission of evidence in violation of the Sixth Amendment Counsel Clause, but in neither case did the error involve admitting a confession or an incriminating statement of the defendant, which was the case in <i>Milton</i> v. <i>Wainwright</i><i>.</i></p>
<p>[6]  <i>Howard</i> v. <i>Pung,</i> <span class="citation" data-id="515504"><a href="/opinion/515504/donald-wayne-howard-v-orville-pung-commissioner-of-corrections-and-frank/#1351" aria-description="Citation for case: Donald Wayne Howard v. Orville Pung, Commissioner of...">862 F. 2d 1348, 1351</a></span> (CA8 1988), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./492/920/">492 U. S. 920</a></span> (1989); <i>United States</i> v. <i>Johnson,</i> <span class="citation" data-id="487141"><a href="/opinion/487141/united-states-v-johnson-richard/#923" aria-description="Citation for case: United States v. Johnson, Richard">816 F. 2d 918, 923</a></span> (CA3 1987); <i>Bryant</i> v. <i>Vose,</i> <span class="citation" data-id="466083"><a href="/opinion/466083/clayton-m-bryant-v-george-a-vose-jr-superintendent-of-massachusetts/#367" aria-description="Citation for case: Clayton M. Bryant v. George A. Vose, Jr., Superintendent...">785 F. 2d 364, 367</a></span> (CA1), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./477/907/">477 U. S. 907</a></span> (1986); <i>Martin</i> v. <i>Wainwright,</i> <span class="citation" data-id="9473880"><a href="/opinion/457158/nollie-lee-martin-v-louie-l-wainwright/#932" aria-description="Citation for case: Nollie Lee Martin v. Louie L. Wainwright">770 F. 2d 918, 932</a></span> (CAll 1985), modified, <span class="citation" data-id="463284"><a href="/opinion/463284/nollie-lee-martin-v-louie-l-wainwright/" aria-description="Citation for case: Nollie Lee Martin v. Louie L. Wainwright">781 F. 2d 185</a></span>, cert. denied, <span class="citation" data-id="9058387"><a href="/opinion/9064759/martin-v-wainwright/" aria-description="Citation for case: Martin v. Wainwright">479 U. S. 909</a></span> (1986); <i>United States</i> v. <i>Ramirez,</i> <span class="citation" data-id="420788"><a href="/opinion/420788/united-states-v-roy-moreno-ramirez-united-states-of-america-v-robert-h/#542" aria-description="Citation for case: United States v. Roy Moreno Ramirez, United States of...">710 F. 2d 535, 542-543</a></span> (CA9 1983); <i>Harryman</i> v. <i>Estelle,</i> <span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/#875" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">616 F. 2d 870, 875</a></span> (CA5) (en banc), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./449/860/">449 U. S. 860</a></span> (1980).</p>
<p>[7]  The same can be said of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cases. As the Court has recognized, a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation "does not mean that the statements received have actually been coerced, but only that the courts will presume the privilege against compulsory self-incrimination has not been intelligently exercised." <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#310" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 310</a></span> (1985). See also <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984).</p>
<p>[8]  Although Fulminante had allegedly confessed to Donna Sarivola several months previously, police did not yet know of this confession, which Anthony Sarivola did not mention to them until June 1985. App. 90-92. They did, however, know of the first confession, which Fulminante had given to Anthony Sarivola nearly a year before.</p>
<p>[9]  The inadmissible confession to Anthony Sarivola was itself subject to serious challenge. Sarivola's lack of moral integrity was demonstrated by his testimony that he had worked for organized crime during the time he was a uniformed police officer. App. 74-75, 104-105. His overzealous approach to gathering information for which he would be paid by authorities, <i>id.,</i> at 79, was revealed by his admission that he had fabricated a tape recording in connection with an earlier, unrelated FBI investigation, <i>id.,</i> at 96-98. He received immunity in connection with the information he provided. <i>Id.,</i> at 129. His eagerness to get in and stay in the federal Witness Protection Program provided a motive for giving detailed information to authorities. <i>Id.,</i> at 114, 129-131. During his first report of the confession, Sarivola failed to hint at numerous details concerning an alleged sexual assault on Jeneane; he mentioned them for the first time more than a year later during further interrogation, at which he also recalled, for the first time, the confession to Donna Sarivola. <i>Id.,</i> at 90-92, 148-149. The impeaching effect of each of these factors was undoubtedly undercut by the presence of the second confession, which, not surprisingly, recounted a quite similar story and thus corroborated the first confession. Thus, each confession, though easily impeachable if viewed in isolation, became difficult to discount when viewed in conjunction with the other.</p>
<p>[10]  Fulminante asserts that other prejudicial evidence, including his prior felony convictions and incarcerations, and his prison reputation for untruthfulness, likewise would not have been admitted had the confession to Sarivola been excluded. Brief for Respondent 31-32. Because we find that the admission of the confession was not harmless in any event, we express no opinion as to the effect any of this evidence might have had on Fulminante's conviction.</p>

</div>
```

---

## GROUP: content/cases/Arizona v. Gant.md  (`case`, 6 assertions)

### content_page

```
---
title: "Arizona v. Gant"
type: case
citation: "556 U.S. 332 (2009)"
parallel_cite: "129 S. Ct. 1710; 173 L. Ed. 2d 485"
neutral_cite: 2009 U.S. LEXIS 3120
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-04-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-04-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Gant
  varies_by_point: false
  scope_note: "Gant itself cabins the broad reading of New York v. Belton; Gant is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145887/arizona-v-gant/"
  cluster_id: 145887
  opinion_id: 9435359
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Key — Anchor"
  - page: "[[Traffic Stops]]"
    role: "Related (cross-doctrine)"
related: ["[[New York v. Belton]]", "[[Chimel v. California]]", "[[Thornton v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search"]
holding: "Cabins Belton. A vehicle search incident to a recent occupant's arrest is permitted only when (1) the arrestee is unsecured and within…"
lake:
  record_id: Arizona v. Gant
  status: verified
  projected_at: 2026-07-06
---

# Arizona v. Gant

*556 U.S. 332 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Gant was arrested for driving on a suspended license. After he was handcuffed and locked in the back of a patrol car, officers searched his car and found cocaine in a jacket on the back seat. He moved to suppress the cocaine as the product of an unlawful [[Search Incident to Arrest|search incident to arrest]].

## Issue
Whether police may search the passenger compartment of a vehicle incident to a recent occupant's arrest when the arrestee has been secured and cannot reach the vehicle, and there is no reason to believe the vehicle contains evidence of the offense of arrest.

## Rule
A vehicle search incident to a recent occupant's arrest is allowed only on one of two independent justifications: "Police may search a vehicle incident to a recent occupant's arrest only if the arrestee is within reaching distance of the passenger compartment at the time of the search or it is reasonable to believe the vehicle contains evidence of the offense of arrest." — 556 U.S. at 351 (129 S. Ct. at 1723). ^pin-351

Absent those justifications, "a search of an arrestee's vehicle will be unreasonable unless police obtain a warrant or show that another exception to the warrant requirement applies." — *Id.* This reading cabins the broad understanding of [[New York v. Belton]] that had been taken to authorize a vehicle search whenever an occupant was arrested.

## Application
On these facts both justifications were absent. Gant had been handcuffed and locked in a patrol car before the search, so he was not within reaching distance of the passenger compartment; and he was arrested for driving on a suspended license — an offense for which the car would hold no evidence. Because neither the officer-safety/evidence-preservation rationale of *[[Chimel v. California|Chimel]]* nor the evidence-of-the-offense rationale applied, the [[Search Incident to Arrest|search incident to arrest]] was unreasonable.

## Conclusion
The vehicle search was unconstitutional; the judgment of the Arizona Supreme Court suppressing the evidence was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment of *Gant*. *Gant* itself **narrowed** the expansive reading of [[New York v. Belton]] (and [[Thornton v. United States]]) for vehicle [[Search Incident to Arrest|searches incident to arrest]], replacing automatic passenger-compartment searches with its two-justification test.

## Appears on
- [[SIA Vehicles]] — *Key — Anchor*
- [[Traffic Stops]] — *Related (cross-doctrine)*

## Sources
- *Arizona v. Gant*, 556 U.S. 332 (2009) — https://www.courtlistener.com/opinion/145887/arizona-v-gant/ — pinpoint: 351 (parallel 129 S. Ct. 1723).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "10880199e3227e55", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "556 U.S. 332 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 3120", "official_citation_present": true, "parallel_cite": "129 S. Ct. 1710; 173 L. Ed. 2d 485", "title": "Arizona v. Gant", "year": "2009"}}
{"assertion_id": "234655064af79630", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Cabins Belton. A vehicle search incident to a recent occupant's arrest is permitted only when (1) the arrestee is unsecured and within…", "title": "Arizona v. Gant"}}
{"assertion_id": "74bd3b47801872d2", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Related (cross-doctrine)", "title": "Arizona v. Gant"}}
{"assertion_id": "d4109bff6862ef1a", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Vehicles"}, "payload": {"home": "SIA Vehicles", "role": "Key — Anchor", "title": "Arizona v. Gant"}}
{"assertion_id": "730f214c81941130", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Gant"}}
{"assertion_id": "7e3644ceabae48a1", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-04-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arizona v. Gant", "field_i_validity": "good_law", "scope_note": "Gant itself cabins the broad reading of New York v. Belton; Gant is good law.", "title": "Arizona v. Gant", "varies_by_point": "false"}}
```

### lake record — Arizona v. Gant

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Gant",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Gant",
    "case_name_short": "Gant",
    "case_name_full": "Arizona v. Gant",
    "input_case_name": "Arizona v. Gant",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-04-21",
    "year": 2009,
    "docket": null,
    "cluster_id": 145887,
    "lead_opinion_id": 9435359,
    "sibling_ids": [
      145887,
      9435359,
      9435360,
      9435361
    ],
    "absolute_url": "/opinion/145887/arizona-v-gant/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "556 U.S. 332",
      "volume": "556",
      "reporter": "U.S.",
      "page": "332",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 1710",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1710",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 485",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 3120",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "556 U.S. 332",
        "volume": "556",
        "reporter": "U.S.",
        "page": "332",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 1710",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "1710",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "173 L. Ed. 2d 485",
        "volume": "173",
        "reporter": "L. Ed. 2d",
        "page": "485",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 3120",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "3120",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "556 U.S. 332",
    "official_selection": {
      "court_class": "scotus",
      "selected": "556 U.S. 332",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-351",
      "page": null,
      "quote": "--- # Arizona v. Gant *556 U.S. 332 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Gant was arrested for driving on a suspended license. After he was handcuffed and locked in the back of a patrol car, officers searched his car and found cocaine in a jacket on the back seat. He moved to suppress the cocaine as the product of an unlawful search incident to arrest. ## Issue Whether police may search the passenger compartment of a vehicle incident to a recent occupant's arrest when the arrestee has been secured and cannot reach the vehicle, and there is no reason to believe the vehicle contains evidence of the offense of arrest. ## Rule A vehicle search incident to a recent occupant's arrest is allowed only on one of two independent justifications:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-04-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Gant",
    "varies_by_point": false,
    "scope_note": "Gant itself cabins the broad reading of New York v. Belton; Gant is good law.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "Arizona v. Gant:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Williams",
          "cluster_id": 10027459,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Silvelo",
          "cluster_id": 4796646,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane1_negative"
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
        "journal_ref": "Arizona v. Gant:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Alleyne v. United States",
          "cluster_id": 903985,
          "cite": [
            "186 L. Ed. 2d 314",
            "133 S. Ct. 2151",
            "2013 U.S. LEXIS 4543",
            "570 U.S. 99",
            "81 U.S.L.W. 4444",
            "24 Fla. L. Weekly Fed. S 310",
            "2013 WL 2922116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisor v. Wilkie",
          "cluster_id": 4632953,
          "cite": [
            "588 U.S. 558",
            "139 S. Ct. 2400",
            "204 L. Ed. 2d 841",
            "2019 U.S. LEXIS 4397"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maryland v. King",
          "cluster_id": 873669,
          "cite": [
            "186 L. Ed. 2d 1",
            "133 S. Ct. 1958",
            "2013 U.S. LEXIS 4165",
            "569 U.S. 435",
            "24 Fla. L. Weekly Fed. S 234",
            "81 U.S.L.W. 4343",
            "2013 WL 2371466"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janus v. State, County, and Municipal Employees",
          "cluster_id": 4511640,
          "cite": [
            "585 U.S. 878",
            "138 S. Ct. 2448",
            "201 L. Ed. 2d 924",
            "2018 U.S. LEXIS 4028"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manigan",
          "cluster_id": 1031401,
          "cite": [
            "592 F.3d 621",
            "2010 U.S. App. LEXIS 1713",
            "2010 WL 298031"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rocha",
          "cluster_id": 4345763,
          "cite": [
            "295 Neb. 716",
            "890 N.W.2d 178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "v. Allen",
          "cluster_id": 4673511,
          "cite": [
            "2019 CO 88"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bailey v. United States",
          "cluster_id": 820749,
          "cite": [
            "185 L. Ed. 2d 19",
            "133 S. Ct. 1031",
            "568 U.S. 186",
            "2013 U.S. LEXIS 1075"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Utah v. Strieff",
          "cluster_id": 3214882,
          "cite": [
            "579 U.S. 232",
            "195 L. Ed. 2d 400",
            "2016 U.S. LEXIS 3926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Collins v. Virginia",
          "cluster_id": 4501697,
          "cite": [
            "584 U.S. 586",
            "138 S. Ct. 1663",
            "201 L. Ed. 2d 9",
            "2018 U.S. LEXIS 3210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Heller v. District of Columbia",
          "cluster_id": 614652,
          "cite": [
            "670 F.3d 1244",
            "399 U.S. App. D.C. 314",
            "2011 U.S. App. LEXIS 20130",
            "2011 WL 4551558"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. William L. Witt(074468)",
          "cluster_id": 2993869,
          "cite": [
            "223 N.J. 409",
            "126 A.3d 850",
            "2015 N.J. LEXIS 890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kevin M. Clark v. State of Indiana",
          "cluster_id": 1041668,
          "cite": [
            "994 N.E.2d 252",
            "2013 WL 5228498",
            "2013 Ind. LEXIS 700"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Swick",
          "cluster_id": 891802,
          "cite": [
            "2012 NMSC 18",
            "2 N.M. 30",
            "2012 NMSC 018"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Elias",
          "cluster_id": 2539936,
          "cite": [
            "339 S.W.3d 667",
            "2011 Tex. Crim. App. LEXIS 448",
            "2011 WL 1267248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
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
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ramos v. Louisiana",
          "cluster_id": 4746633,
          "cite": [
            "590 U.S. 83"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Gant:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg1ODcyMDAwMDAwJnM9MTAwMjEwMTAmdD1vJmQ9MjAyNi0wNy0wNCZwPTEx&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145887+OR+9435359+OR+9435360+OR+9435361%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTQmcz0yNjgxODE4JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28145887+OR+9435359+OR+9435360+OR+9435361%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361)",
        "reviewed": 117,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 117,
        "triage_read": 2,
        "triage_snippet_classified": 115
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145887 OR 9435359 OR 9435360 OR 9435361)",
    "indexed_citing_opinions": 1426,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145887,
        "count": 1166,
        "count_source": "search"
      },
      {
        "opinion_id": 9435359,
        "count": 280,
        "count_source": "search"
      },
      {
        "opinion_id": 9435360,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9435361,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2728,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-gant.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNDc0MjUmcz0xMDM1MjEwNCZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145887+OR+9435359+OR+9435360+OR+9435361%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145887,
        "cited_id": 30547,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 101899,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 104576,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 106447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 106964,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 112296,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 112384,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 112643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 130160,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 134735,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 134746,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 145630,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 145701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 195782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 498214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 520415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 593396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 719587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 721372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 762479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 789343,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 791442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 792893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 794927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 867371,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1057451,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1195099,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1223809,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1234081,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1399986,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1401546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1427013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 1983319,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2009627,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2080120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2112994,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2221553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2598312,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 2620702,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145887,
        "cited_id": 5538778,
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
    "date_created": "2026-07-04T18:20:38Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:20:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:20:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:25:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:20:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Gant

```
<opinion type="majority">
<author id="b435-4"><page-number citation-index="1" label="335">*335</page-number>Justice Stevens</author>
<p id="AEK">delivered the opinion of the Court.</p>
<p id="b435-5">After Rodney Gant was arrested for driving with a suspended license, handcuffed, and locked in the back of a patrol car, police officers searched his car and discovered cocaine in the pocket of a jacket on the backseat. Because Gant could not have accessed his ear to retrieve weapons or evidence at the time of the search, the Arizona Supreme Court held that the search-incident-to-arrest exception to the Fourth Amendment’s warrant requirement, as defined in <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), and applied to vehicle searches in <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), did not justify the search in this case. We agree with that conclusion.</p>
<p id="b435-6">Under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>police may search incident to arrest only the space within an arrestee’s “ ‘immediate control,’ ” meaning “the area from within which he might gain possession of a weapon or destructible evidence.” <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>. The safety and evidentiary justifications underlying Chimel's reaching-distance rule determine <em>Belton's </em>scope. Accordingly, we hold that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>does not authorize a vehicle search incident to a recent occupant’s arrest after the arrestee has been secured and cannot access the interior of the vehicle. Consistent with the holding in <em>Thornton </em>v. <em>United States, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">541 U. S. 615</a></span> (2004), and following the suggestion in Justice Scalia’s opinion concurring in the judgment in that case, <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#632" aria-description="Citation for case: Thornton v. United States"><em>id., </em>at 632</a></span>, we also conclude that circumstances unique to the automobile context justify a search incident to arrest when it is reasonable to believe that evidence of the offense of arrest might be found in the vehicle.</p>
<p id="b435-7">I</p>
<p id="b435-8">On August 25, 1999, acting on an anonymous tip that the residence at 2524 North Walnut Avenue was being used to sell drugs, Tucson police officers Griffith and Reed knocked on the front door and asked to speak to the owner. Gant answered the door and, after identifying himself, stated that <page-number citation-index="1" label="336">*336</page-number>he expected the owner to return later. The officers left the residence and conducted a records check, which revealed that Gant’s driver’s license had been suspended and there was an outstanding warrant for his arrest for driving with a suspended license.</p>
<p id="b436-5">When the officers returned to the house that evening, they found a man near the back of the house and a woman in a car parked in front of it. After a third officer arrived, they arrested the man for providing a false name and the woman for possessing drug paraphernalia. Both arrestees were handcuffed and secured in separate patrol cars when Gant arrived. The officers recognized his car as it entered the driveway, and Officer Griffith confirmed that Gant was the driver by shining a flashlight into the car as it drove by him. Gant parked at the end of the driveway, got out of his car, and shut the door. Griffith, who was about 30 feet away, called to Gant, and they approached each other, meeting 10-to-12 feet from Gant’s car. Griffith immediately arrested Gant and handcuffed him.</p>
<p id="b436-6">Because the other arrestees were secured in the only patrol cars at the scene, Griffith called for backup. When two more officers arrived, they locked Gant in the backseat of their vehicle. After Gant had been handcuffed and placed in the back of a patrol car, two officers searched his car: One of them found a gun, and the other discovered a bag of cocaine in the pocket of a jacket on the backseat.</p>
<p id="b436-7">Gant was charged with two offenses — possession of a narcotic drug for sale and possession of drug paraphernalia (1 <em>e., </em>the plastic bag in which the cocaine was found). He moved to suppress the evidence seized from his car on the ground that the warrantless search violated the Fourth Amendment. Among other things, Gant argued that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>did not authorize the search of his vehicle because he posed no threat to the officers after he was handcuffed in the patrol car and because he was arrested for a traffic offense for which no evidence could be found in his vehicle. When asked at the <page-number citation-index="1" label="337">*337</page-number>suppression hearing why the search was conducted, Officer Griffith responded: “Because the law says we can do it.” App. 75.</p>
<p id="b437-5">The trial court rejected the State’s contention that the officers had probable cause to search Gant’s car for contraband when the search began, <em>id., </em>at 18, 30, but it denied the motion to suppress. Relying on the fact that the police saw Gant commit the crime of driving without a license and apprehended him only shortly after he exited his ear, the court held that the search was permissible as a search incident to arrest. <em>Id., </em>at 37. A jury found Gant guilty on both drug counts, and he was sentenced to a 3-year term of imprisonment.</p>
<p id="b437-6">After protracted state-court proceedings, the Arizona Supreme Court concluded that the search of Gant’s car was unreasonable within the meaning of the Fourth Amendment. The court’s opinion discussed at length our decision in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>which held that police may search the passenger compartment of a vehicle and any containers therein as a contemporaneous incident of an arrest of the vehicle’s recent occupant. <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#3" aria-description="Citation for case: State v. Gant">216 Ariz. 1, 3-4</a></span>, 162 R 3d 640, 642-643 (2007) (citing <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>). The court distinguished <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>as a case concerning the permissible scope of a vehicle search incident to arrest and concluded that it did not answer “the threshold question whether the police may conduct a search incident to arrest at all once the scene is secure.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>, 162 R 3d, at 643. Relying on our earlier decision in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>the court observed that the search-ineident-toarrest exception to the warrant requirement is justified by interests in officer safety and evidence preservation. <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#4" aria-description="Citation for case: State v. Gant">216 Ariz., at 4</a></span>,<span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#643" aria-description="Citation for case: State v. Gant">162 P. 3d, at 643</a></span>. When “the justifications underlying <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>no longer exist because the scene is secure and the arrestee is handcuffed, secured in the back of a patrol ear, and under the supervision of an officer,” the court concluded, a “warrantless search of the arrestee’s car cannot be justified as necessary to protect the officers at the scene or <page-number citation-index="1" label="338">*338</page-number>prevent the destruction of evidence.” <em>Id., </em>at 5,<span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#644" aria-description="Citation for case: State v. Gant">162 P. 3d, at 644</a></span>. Accordingly, the court held that the search of Gant’s ear was unreasonable.</p>
<p id="b438-5">The dissenting justices would have upheld the search of Gant's car based on their view that “the validity of a <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>search . . . clearly does not depend on the presence of the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>rationales in a particular case.” <em>Id., </em>at 8, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#647" aria-description="Citation for case: State v. Gant">162 P. 3d, at 647</a></span>. Although they disagreed with the majority’s view of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>the dissenting justices acknowledged that “[t]he bright-line rule embraced in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>has long been criticized and probably merits reconsideration.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#10" aria-description="Citation for case: State v. Gant">216 Ariz., at 10</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#649" aria-description="Citation for case: State v. Gant">162 P. 3d, at 649</a></span>. They thus “add[ed their] voice[s] to the others that have urged the Supreme Court to revisit Belton.” <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#11" aria-description="Citation for case: State v. Gant"><em>Id., </em>at 11</a></span>, <span class="citation" data-id="9506247"><a href="/opinion/867371/state-v-gant/#650" aria-description="Citation for case: State v. Gant">162 P. 3d, at 650</a></span>.</p>
<p id="b438-6">The chorus that has called for us to revisit <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>includes courts, scholars, and Members of this Court who have questioned that decision’s clarity and its fidelity to Fourth Amendment principles. We therefore granted the State’s petition for certiorari. <span class="citation no-link">552 U. S. 1230</span> (2008).</p>
<p id="b438-7">II</p>
<p id="b438-8">Consistent with our precedent, our analysis begins, as it should in every case addressing the reasonableness of a warrantless search, with the basic rule that “searches conducted outside the judicial process, without prior approval by judge or magistrate, are <em>per se </em>unreasonable under the Fourth Amendment — subject only to a few specifically established and well-delineated exceptions.” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967) (footnote omitted). Among the exceptions to the warrant requirement is a search incident to a lawful arrest. See <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span> (1914). The exception derives from interests in officer safety and evidence preservation that are typically implicated in arrest situations. See <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#230" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 230-234</a></span> (1973); <em>Chimel, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California">395 U. S., at 763</a></span>.</p>
<p id="b439-4"><page-number citation-index="1" label="339">*339</page-number>In <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>we held that a search incident to arrest may only include “the arrestee’s person and the area ‘within his immediate control’ — construing that phrase to mean the area from within which he might gain possession of a weapon or destructible evidence.” <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Ibid.</a></span> </em>That limitation, which continues to define the boundaries of the exception, ensures that the scope of a search incident to arrest is commensurate with its purposes of protecting arresting officers and safeguarding any evidence of the offense of arrest that an arrestee might conceal or destroy. See <em>ibid, </em>(noting that searches incident to arrest are reasonable <em>“in order to </em>remove any weapons [the arrestee] might seek to use” and <em>“in order to prevent </em>[the] concealment or destruction” of evidence (emphasis added)). If there is no possibility that an arrestee could reach into the area that law enforcement officers seek to search, both justifications for the search-incident-to-arrest exception are absent and the rule does not apply. <em>E. g., Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367-368</a></span> (1964).</p>
<p id="b439-5">In <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>we considered ChimeVs application to the automobile context. A lone police officer in that case stopped a speeding car in which Belton was one of four occupants. While asking for the driver’s license and registration, the officer smelled burnt marijuana and observed an envelope on the car floor marked “Supergold” — a name he associated with marijuana. Thus having probable cause to believe the occupants had committed a drug offense, the officer ordered them out of the vehicle, placed them under arrest, and patted them down. Without handcuffing the arrestees,<footnotemark>1</footnotemark> the officer “ ‘split them up into four separate areas of the Thruway ... so they would not be in physical touching area of each other’ ” and searched the vehicle, including the pocket of a jacket on the backseat, in which he found cocaine. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#456" aria-description="Citation for case: New York v. Belton">453 U. S., at 456</a></span>.</p>
<p id="b440-4"><page-number citation-index="1" label="340">*340</page-number>The New York Court of Appeals found the search unconstitutional, concluding that after the occupants were arrested the vehicle and its contents were “safely within the exclusive custody and control of the police.” <em>State </em>v. <em>Belton, </em>50 N. Y. 2d 447, 452, <span class="citation" data-id="5533089"><a href="/opinion/5684296/people-v-belton/#423" aria-description="Citation for case: People v. Belton">407 N. E. 2d 420, 423</a></span> (1980). The State asked this Court to consider whether the exception recognized in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>permits an officer to search “a jacket found inside an automobile while the automobile’s four occupants, all under arrest, are standing unsecured around the vehicle.” Brief in No. 80-328, p. <em>i. </em>We granted certiorari because “courts ha[d] found no workable definition of ‘the area within the immediate control of the arrestee’ when that area arguably includes the interior of an automobile.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>.</p>
<p id="b440-5">In its brief, the State argued that the Court of Appeals erred in concluding that the jacket was under the officer’s exclusive control. Focusing on the number of arrestees and their proximity to the vehicle, the State asserted that it was reasonable for the officer to believe the arrestees could have accessed the vehicle and its contents, making the search permissible under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>. </em>Brief in No. 80-328, at 7-8. The United States, as <em>amicus curiae </em>in support of the State, argued for a more permissive standard, but it maintained that any search incident to arrest must be “ ‘substantially contemporaneous’ ” with the arrest — a requirement it deemed “satisfied if the search occurs during the period in which the arrest is being consummated and before the situation has so stabilized that it could be said that the arrest was completed.” Brief for United States as <em>Amicus Curiae </em>in <em>New York </em>v. <em>Belton, </em>O. T. 1980, No. 80-328, p. 14. There was no suggestion by the parties or <em>amici </em>that <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>authorizes a vehicle search incident to arrest when there is no realistic possibility that an arrestee could access his vehicle.</p>
<p id="b440-6">After considering these arguments, we held that when an officer lawfully arrests “the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the <page-number citation-index="1" label="341">*341</page-number>passenger compartment of the automobile” and any containers therein. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span> (footnote omitted). That holding was based in large part on our assumption “that articles inside the relatively narrow compass of the passenger compartment of an automobile are in fact generally, even if not inevitably, within ‘the area into which an arrestee might reach.’ ” <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Ibid.</a></span></em></p>
<p id="b441-5">The Arizona Supreme Court read our decision in <em>Belton </em>as merely delineating “the proper scope of a search of the interior of an automobile” incident to an arrest, <em>id., </em>at 459. That is, <em>when </em>the passenger compartment is within an arrestee’s reaching distance, <em>Belton </em>supplies the generalization that the entire compartment and any containers therein may be reached. On that view of <em>Belton, </em>the state court concluded that the search of Gant’s car was unreasonable because Gant clearly could not have accessed his car at the time of the search. It also found that no other exception to the warrant requirement applied in this case.</p>
<p id="b441-6">Gant now urges us to adopt the reading of <em>Belton </em>followed by the Arizona Supreme Court.</p>
<p id="b441-7">Ill</p>
<p id="b441-8">Despite the textual and evidentiary support for the Arizona Supreme Court’s reading of <em>Belton, </em>our opinion has been widely understood to allow a vehicle search incident to the arrest of a recent occupant even if there is no possibility the arrestee could gain access to the vehicle at the time of the search. This reading may be attributable to Justice Brennan’s dissent in <em>Belton, </em>in which he characterized the Court’s holding as resting on the “fiction... that the interior of a car is <em>always </em>within the immediate control of an arrestee who has recently been in the car.” <em>Id., </em>at 466. Under the majority’s approach, he argued, “the result would presumably be the same even if [the officer] had handcuffed Belton and his companions in the patrol car” before conducting the search. <em>Id., </em>at 468.</p>
<p id="b442-4"><page-number citation-index="1" label="342">*342</page-number>Since we decided <em>Belton, </em>Courts of Appeals have given different answers to the question whether a vehicle must be within an arrestee’s reach to justify a vehicle search incident to arrest,<footnotemark>2</footnotemark> but Justice Brennan’s reading of the Court’s opinion has predominated. As Justice O’Connor observed, “lower court decisions seem now to treat the ability to search a vehicle incident to the arrest of a recent occupant as a police entitlement rather than as an exception justified by the twin rationales of <em>Chimel.” Thornton, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#624" aria-description="Citation for case: Thornton v. United States">541 U. S., at 624</a></span> (opinion concurring in part). Justice Scalia has similarly noted that, although it is improbable that an arrestee could gain access to weapons stored in his vehicle after he has been handcuffed and secured in the backseat of a patrol car, cases allowing a search in “this precise factual scenario . . . are legion.” <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#628" aria-description="Citation for case: Thornton v. United States"><em>Id., </em>at 628</a></span> (opinion concurring in judgment) (collecting cases).<footnotemark>3</footnotemark> Indeed, some courts have upheld searches <page-number citation-index="1" label="343">*343</page-number>under <em>Belton </em>“even when . . . the handcuffed arrestee has already left the scene.” <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#628" aria-description="Citation for case: Thornton v. United States">541 U. S., at 628</a></span> (same).</p>
<p id="b443-5">Under this broad reading of <em>Belton, </em>a vehicle search would be authorized incident to every arrest of a recent occupant notwithstanding that in most cases the vehicle’s passenger compartment will not be within the arrestee’s reach at the time of the search. To read <em>Belton </em>as authorizing a vehicle search incident to every recent occupant’s arrest would thus untether the rule from the justifications underlying the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>exception — a result clearly incompatible with our statement in <em>Belton </em>that it “in no way alters the fundamental principles established in the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>case regarding the basic scope of searches incident to lawful custodial arrests.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460, n. 3</a></span>. Accordingly, we reject this reading of <em>Belton </em>and hold that the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>rationale authorizes police to search a vehicle incident to a recent occupant’s arrest only when the arrestee is unsecured and within reaching distance of the passenger compartment at the time of the search.<footnotemark>4</footnotemark></p>
<p id="b443-6">Although it does not follow from <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>we also conclude that circumstances unique to the vehicle context justify a search incident to a lawful arrest when it is “reasonable to believe evidence relevant to the crime of arrest might be found in the vehicle.” <em>Thornton, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#632" aria-description="Citation for case: Thornton v. United States">541 U. S., at 632</a></span> (Scalia, J., concurring in judgment). In many cases, as when a recent occupant is arrested for a traffic violation, there will be no reasonable basis to believe the vehicle contains relevant evidence. See, <em>e. g., Atwater </em>v. <em>Lago Vista, </em><span class="citation" data-id="9795084"><a href="/opinion/2620702/atwater-v-city-of-lago-vista/#324" aria-description="Citation for case: Atwater v. City of Lago Vista">532 U. S. 318, <page-number citation-index="1" label="344">*344</page-number>324</a></span> (2001); <em>Knowles </em>v. <em>Iowa, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#118" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113, 118</a></span> (1998). But in others, including <em>Belton </em>and <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>, </em>the offense of arrest will supply a basis for searching the passenger compartment of an arrestee’s vehicle and any containers therein.</p>
<p id="b444-5">Neither the possibility of access nor the likelihood of discovering offense-related evidence authorized the search in this case. Unlike in <em>Belton, </em>which involved a single officer confronted with four unsecured arrestees, the five officers in this case outnumbered the three arrestees, all of whom had been handcuffed and secured in separate patrol cars before the officers searched Gant’s car. Under those circumstances, Gant clearly was not within reaching distance of his car at the time of the search. An evidentiary basis for the search was also lacking in this case. Whereas Belton and Thornton were arrested for drug offenses, Gant was arrested for driving with a suspended license — an offense for which police could not expect to find evidence in the passenger compartment of Gant’s car. Cf. <em>Knowles, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#118" aria-description="Citation for case: Knowles v. Iowa">525 U. S., at 118</a></span>. Because police could not reasonably have believed either that Gant could have accessed his car at the time of the search or that evidence of the offense for which he was arrested might have been found therein, the search in this case was unreasonable.</p>
<p id="b444-6">IV</p>
<p id="b444-7">The State does not seriously disagree with the Arizona Supreme Court’s conclusion that Gant could not have accessed his vehicle at the time of the search, but it nevertheless asks us to uphold the search of his vehicle under the broad reading of <em>Belton </em>discussed above. The State argues that <em>Belton </em>searches are reasonable regardless of the possibility of access in a given case because that expansive rule correctly balances law enforcement interests, including the interest in a bright-line rule, with an arrestee’s limited privacy interest in his vehicle.</p>
<p id="b444-8">For several reasons, we reject the State’s argument. First, the State seriously undervalues the privacy interests <page-number citation-index="1" label="345">*345</page-number>at stake. Although we have recognized that a motorist’s privacy interest in his vehicle is less substantial than in his home, see <em>New York </em>v. Class, <span class="citation" data-id="9430353"><a href="/opinion/111600/new-york-v-class/#112" aria-description="Citation for case: New York v. Class">475 U. S. 106, 112-113</a></span> (1986), the former interest is nevertheless important and deserving of constitutional protection, see <em>Knowles, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa">525 U. S., at 117</a></span>. It is particularly significant that <em>Belton </em>searches authorize police officers to search not just the passenger compartment but every purse, briefcase, or other container within that space. A rule that gives police the power to conduct such a search whenever an individual is caught committing a traffic offense, when there is no basis for believing evidence of the offense might be found in the vehicle, creates a serious and recurring threat to the privacy of countless individuals. Indeed, the character of that threat implicates the central concern underlying the Fourth Amendment — the concern about giving police officers unbridled discretion to rummage at will among a person’s private effects.<footnotemark>5</footnotemark></p>
<p id="b445-5">At the same time as it undervalues these privacy concerns, the State exaggerates the clarity that its reading of <em>Belton </em>provides. Courts that have read <em>Belton </em>expansively are at odds regarding how close in time to the arrest and how prox<page-number citation-index="1" label="346">*346</page-number>imate to the arrestee’s vehicle an officer’s first contact with the arrestee must be to bring the encounter within Belton’s purview<footnotemark>6</footnotemark> and whether a search is reasonable when it commences or continues after the arrestee has been removed from the scene.<footnotemark>7</footnotemark> The rule has thus generated a great deal of uncertainty, particularly for a rule touted as providing a “bright line.” See 3 LaFave §7.1(c), at 514-524.</p>
<p id="b446-5">Contrary to the State’s suggestion, a broad reading of <em>Belton </em>is also unnecessary to protect law enforcement safety and evidentiary interests. Under our view, <em>Belton </em>and <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span> </em>permit an officer to conduct a vehicle search when an arrestee is within reaching distance of the vehicle or it is reasonable to believe the vehicle contains evidence of the offense of arrest. Other established exceptions to the warrant requirement authorize a vehicle search under additional circumstances when safety or evidentiary concerns demand. For instance, <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), permits an officer to search a vehicle’s passenger compartment when he has reasonable suspicion that an individual, whether or not the arrestee, is “dangerous” and might access the vehi<page-number citation-index="1" label="347">*347</page-number>cle to “gain immediate control of weapons.” <em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">Id.,</a></span> </em>at 1049 (citing <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#21" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 21</a></span> (1968)). If there is probable cause to believe a vehicle contains evidence of criminal activity, <em>United States </em>v. <em>Ross, </em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#820" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 820-821</a></span> (1982), authorizes a search of any area of the vehicle in which the evidence might be found. Unlike the searches permitted by Justice Scalia’s opinion concurring in the judgment in <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>, </em>which we conclude today are reasonable for purposes of the Fourth Amendment, <em><span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/" aria-description="Citation for case: United States v. Ross">Ross</a></span> </em>allows searches for evidence relevant to offenses other than the offense of arrest, and the scope of the search authorized is broader. Finally, there may be still other circumstances in which safety or evidentiary interests would justify a search. Cf. <em>Maryland </em>v. <em>Buie, </em><span class="citation" data-id="9431933"><a href="/opinion/112384/maryland-v-buie/#334" aria-description="Citation for case: Maryland v. Buie">494 U. S. 325, 334</a></span> (1990) (holding that, incident to arrest, an officer may conduct a limited protective sweep of those areas of a house in which he reasonably suspects a dangerous person may be hiding).</p>
<p id="b447-5">These exceptions together ensure that officers may search a vehicle when genuine safety or evidentiary concerns encountered during the arrest of a vehicle’s recent occupant justify a search. Construing <em>Belton </em>broadly to allow vehicle searches incident to any arrest would serve no purpose except to provide a police entitlement, and it is anathema to the Fourth Amendment to permit a warrantless search on that basis. For these reasons, we are unpersuaded by the State’s arguments that a broad reading of <em>Belton </em>would meaningfully further law enforcement interests and justify a substantial intrusion on individuals’ privacy.<footnotemark>8</footnotemark></p>
<p id="b448-4"><page-number citation-index="1" label="348">*348</page-number>V</p>
<p id="b448-5">Our dissenting colleagues argue that the doctrine of <em>stare decisis </em>requires adherence to a broad reading of <em>Belton </em>even though the justifications for searching a vehicle incident to arrest are in most cases absent.<footnotemark>9</footnotemark> The doctrine of <em>stare decisis </em>is of course “essential to the respect accorded to the judgments of the Court and to the stability of the law,” but it does not compel us to follow a past decision when its rationale no longer withstands “careful analysis.” <em>Lawrence </em>v. <em>Texas, </em><span class="citation" data-id="9434509"><a href="/opinion/130160/lawrence-v-texas/#577" aria-description="Citation for case: Lawrence v. Texas">539 U. S. 558, 577</a></span> (2003).</p>
<p id="b448-6">We have never relied on <em>stare decisis </em>to justify the continuance of an unconstitutional police practice. And we would be particularly loath to uphold an unconstitutional result in a case that is so easily distinguished from the decisions that arguably compel it. The safety and evidentiary interests that supported the search in <em>Belton </em>simply are not present in this case. Indeed, it is hard to imagine two cases that are factually more distinct, as <em>Belton </em>involved one officer confronted by four unsecured arrestees suspected of committing a drug offense, and this case involves several officers confronted with a securely detained arrestee apprehended for driving with a suspended license. This case is also distinguishable from <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>, </em>in which the petitioner was <page-number citation-index="1" label="349">*349</page-number>arrested for a drug offense. It is thus unsurprising that Members of this Court who concurred in the judgments in <em>Belton </em>and <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span> </em>also concur in the decision in this case.<footnotemark>10</footnotemark></p>
<p id="b449-5">We do not agree with the contention in Justice Alito’s dissent (hereinafter dissent) that consideration of police reliance interests requires a different result. Although it appears that the State’s reading of <em>Belton </em>has been widely taught in police academies and that law enforcement officers have relied on the rule in conducting vehicle searches during the past 28 years,* <footnotemark>11</footnotemark> many of these searches were not justified by the reasons underlying the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>exception. Countless individuals guilty of nothing more serious than a traffic violation have had their constitutional right to the security of their private effects violated as a result. The fact that the law enforcement community may view the State’s version of the <em>Belton </em>rule as an entitlement does not establish the sort of reliance interest that could outweigh the countervailing interest that all individuals share in having their constitutional rights fully protected. If it is clear that a practice is unlawful, individuals’ interest in its discontinuance clearly outweighs any law enforcement “entitlement” to its persistence. Cf. <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 393</a></span> (1978) (“[T]he mere fact that law enforcement may be made more efficient can never by itself justify disregard of the Fourth Amendment”). The dissent’s reference in this regard to the reliance interests cited in <em>Dickerson </em>v. <em>United States, </em><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000), is misplaced. See <em>post, </em>at 358-359. In ob<page-number citation-index="1" label="350">*350</page-number>serving that <em>“Miranda </em>has become embedded in routine police practice to the point where the warnings have become part of our national culture,” <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#443" aria-description="Citation for case: Dickerson v. United States">530 U. S., at 443</a></span>, the Court was referring not to police reliance on a rule requiring them to provide warnings but to the broader societal reliance on that individual right.</p>
<p id="b450-5">The dissent also ignores the checkered history of the search-incident-to-arrest exception. Police authority to search the place in which a lawful arrest is made was broadly asserted in <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/" aria-description="Citation for case: Marron v. United States">275 U. S. 192</a></span> (1927), and limited a few years later in <em>Go-Bart Importing Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344</a></span> (1931), and <em>United States </em>v. <em>Lefkowitz, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452</a></span> (1932). The limiting views expressed in <em>Go-Bart </em>and <em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/" aria-description="Citation for case: United States v. Lefkowitz">Lefkowitz</a></span> </em>were in turn abandoned in <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">331 U. S. 145</a></span> (1947), which upheld a search of a four-room apartment incident to the occupant’s arrest. Only a year later the Court in <em>Trupiano </em>v. <em>United States, </em><span class="citation" data-id="9420205"><a href="/opinion/104576/trupiano-v-united-states/#708" aria-description="Citation for case: Trupiano v. United States">334 U. S. 699, 708</a></span> (1948), retreated from that holding, noting that the search-incident-to-arrest exception is “a strictly limited” one that must be justified by “something more in the way of necessity than merely a lawful arrest.” And just two years after that, in <em>United States </em>v. <em>Rabinowitz, </em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">339 U. S. 56</a></span> (1950), the Court again reversed course and upheld the search of an entire apartment. Finally, our opinion in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>overruled <em><span class="citation" data-id="9420441"><a href="/opinion/104769/united-states-v-rabinowitz/" aria-description="Citation for case: United States v. Rabinowitz">Rabinowitz</a></span> </em>and what remained of <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>and established the present boundaries of the search-incident-to-arrest exception. Notably, none of the dissenters in <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>or the cases that preceded it argued that law enforcement reliance interests outweighed the interest in protecting individual constitutional rights so as to warrant fidelity to an unjustifiable rule.</p>
<p id="b450-6">The experience of the 28 years since we decided <em>Belton </em>has shown that the generalization underpinning the broad reading of that decision is unfounded. We now know that articles inside the passenger compartment are rarely “within 'the area into which an arrestee might reach,’ ” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at <page-number citation-index="1" label="351">*351</page-number>460</a></span>, and blind adherence to <em>Belton’s </em>faulty assumption would authorize myriad unconstitutional searches. The doctrine of <em>stare decisis </em>does not require us to approve routine constitutional violations.</p>
<p id="b451-5">VI</p>
<p id="b451-6">Police may search a vehicle incident to a recent occupant’s arrest only if the arrestee is within reaching distance of the passenger compartment at the time of the search or it is reasonable to believe the vehicle contains evidence of the offense of arrest. When these justifications are absent, a search of an arrestee’s vehicle will be unreasonable unless police obtain a warrant or show that another exception to the warrant requirement applies. The Arizona Supreme Court correctly held that this case involved an unreasonable search. Accordingly, the judgment of the State Supreme Court is affirmed.</p>
<p id="b451-7">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b439-6"> The officer was unable to handcuff the occupants because he had only one set of handcuffs. See Brief for Petitioner in <em>New York </em>v. <em>Belton, </em>O. T. 1980, No. 80-328, p. 3 (hereinafter Brief in No. 80-328).</p>
</footnote>
<footnote label="2">
<p id="b442-5"> Compare <em>United States </em>v. <em>Green, </em><span class="citation" data-id="30547"><a href="/opinion/30547/united-states-v-green/#379" aria-description="Citation for case: United States v. Green">324 F. 3d 375, 379</a></span> (CA5 2003) (holding that <em>Belton </em>did not authorize a search of an arrestee’s vehicle when he was handcuffed and lying facedown on the ground surrounded by four police officers 6-to-10 feet from the vehicle), <em>United States </em>v. <em>Edwards, </em><span class="citation" data-id="6994169"><a href="/opinion/7088754/united-states-v-edwards/#938" aria-description="Citation for case: United States v. Edwards">242 F. 3d 928, 938</a></span> (CA10 2001) (finding unauthorized a vehicle search conducted while the arrestee was handcuffed in the back of a patrol car), and <em>United States </em>v. <em>Vasey, </em><span class="citation" data-id="498214"><a href="/opinion/498214/united-states-v-michael-allen-vasey/#787" aria-description="Citation for case: United States v. Michael Allen Vasey">834 F. 2d 782, 787</a></span> (CA9 1987) (finding unauthorized a vehicle search conducted 30-to-45 minutes after an arrest and after the arrestee had been handcuffed and secured in the back of a police car), with <em>United States </em>v. <em>Hrasky, </em><span class="citation" data-id="9499027"><a href="/opinion/794927/united-states-v-zachary-hrasky/#1102" aria-description="Citation for case: United States v. Zachary Hrasky">453 F. 3d 1099, 1102</a></span> (CA8 2006) (upholding a search conducted an hour after the arrestee was apprehended and after he had been handcuffed and placed in the back of a patrol car), <em>United States </em>v. <em>Weaver, </em><span class="citation" data-id="792893"><a href="/opinion/792893/united-states-v-hollie-lynn-weaver-aka-hollie-lynn-brawner-maiden/#1106" aria-description="Citation for case: United States v. Hollie Lynn Weaver, A/K/A Hollie Lynn...">433 F. 3d 1104, 1106</a></span> (CA9 2006) (upholding a search conducted 10-to-15 minutes after an arrest and after the arrestee had been handcuffed and secured in the back of a patrol car), and <em>United States </em>v. <em>White, </em><span class="citation" data-id="520415"><a href="/opinion/520415/united-states-v-james-allen-white-jr/#44" aria-description="Citation for case: United States v. James Allen White, Jr.">871 F. 2d 41, 44</a></span> (CA6 1989) (upholding a search conducted after the arrestee had been handcuffed and secured in the back of a police cruiser).</p>
</footnote>
<footnote label="3">
<p id="b442-6"> The practice of searching vehicles incident to arrest after the arrestee has been handcuffed and secured in a patrol car has not abated since we decided <em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">Thornton</a></span>. </em>See, <em>e.g., United States </em>v. <em>Murphy, </em><span class="citation" data-id="168860"><a href="/opinion/168860/united-states-v-murphy/#717" aria-description="Citation for case: United States v. Murphy">221 Fed. Appx. 715, 717</a></span> (CA10 2007); <em>Hrasky, </em><span class="citation" data-id="9499027"><a href="/opinion/794927/united-states-v-zachary-hrasky/#1100" aria-description="Citation for case: United States v. Zachary Hrasky">453 F. 3d, at 1100</a></span>; <em>Weaver, </em><span class="citation" data-id="792893"><a href="/opinion/792893/united-states-v-hollie-lynn-weaver-aka-hollie-lynn-brawner-maiden/#1105" aria-description="Citation for case: United States v. Hollie Lynn Weaver, A/K/A Hollie Lynn...">433 F. 3d, at 1105</a></span>; <em>United States </em>v. <em>Williams, </em><span class="citation" data-id="9813827"><a href="/opinion/2973559/united-states-v-williams/#401" aria-description="Citation for case: United States v. Williams">170 Fed. Appx. 399, 401</a></span> (CA6 2006); <em>United States </em>v. <em>Dorsey, </em><span class="citation" data-id="9498265"><a href="/opinion/791442/united-states-v-nikos-delano-dorsey/#1041" aria-description="Citation for case: United States v. Nikos Delano Dorsey">418 F. 3d 1038, 1041</a></span> (CA9 2005); <em>United States </em>v. <page-number citation-index="1" label="343">*343</page-number><em>Osife, </em><span class="citation" data-id="789343"><a href="/opinion/789343/united-states-v-dale-juan-osife/#1144" aria-description="Citation for case: United States v. Dale Juan Osife">398 F. 3d 1143, 1144</a></span> (CA9 2005); <em>United States </em>v. <em>Sumrall, </em><span class="citation" data-id="165144"><a href="/opinion/165144/united-states-v-sumrall/#24" aria-description="Citation for case: United States v. Sumrall">115 Fed. Appx. 22, 24</a></span> (CA10 2004).</p>
</footnote>
<footnote label="4">
<p id="b443-9"> Because officers have many means of ensuring the safe arrest of vehicle occupants, it will be the rare case in which an officer is unable to fully effectuate an arrest so that a real possibility of access to the arrestee’s vehicle remains. Cf. 3 W. LaFave, Search and Seizure § 7.1(c), p. 525 (4th ed. 2004) (hereinafter LaFave) (noting that the availability of protective measures “ensur[es] the nonexistence of circumstances in which the arrestee’s ‘control’ of the car is in doubt”). But in such a case a search incident to arrest is reasonable under the Fourth Amendment.</p>
</footnote>
<footnote label="5">
<p id="b445-6"> See <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#84" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 84</a></span> (1987); <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#760" aria-description="Citation for case: Chimel v. California">395 U. S. 752, 760-761</a></span> (1969); <em>Stanford </em>v. <em>Texas, </em><span class="citation" data-id="106964"><a href="/opinion/106964/stanford-v-texas/#480" aria-description="Citation for case: Stanford v. Texas">379 U. S. 476, 480-484</a></span> (1965); <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#389" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 389-392</a></span> (1914); <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-625</a></span> (1886); see also 10 C. Adams, The Works of John Adams 247-248 (1856). Many have observed that a broad reading of <em>Belton </em>gives police limitless discretion to conduct exploratory searches. See 3 LaFave § 7.1(c), at 527 (observing that <em>Belton </em>creates the risk “that police will make custodial arrests which they otherwise would not make as a cover for a search which the Fourth Amendment otherwise prohibits”); see also <em>United States </em>v. <em>McLaughlin, </em><span class="citation" data-id="9491975"><a href="/opinion/762479/united-states-of-america-plaintiff-appellant-v-john-lee-mclaughlin/#894" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. John...">170 F. 3d 889, 894</a></span> (CA9 1999) (Trott, J., concurring) (observing that <em>Belton </em>has been applied to condone “purely exploratory searches of vehicles during which officers with no definite objective or reason for the search are allowed to rummage around in a ear to see what they might find”); <em>State </em>v. <em>Pallone, </em><span class="citation" data-id="9655955"><a href="/opinion/1581652/state-v-trawitzki/#87" aria-description="Citation for case: State v. Trawitzki">2001 WI 77, ¶¶ 87-90</a></span>,<span class="citation" data-id="9739954"><a href="/opinion/2221553/state-v-pallone/#203" aria-description="Citation for case: State v. Pallone">236 Wis. 2d 162, 203-204</a></span>, and n. 9, <span class="citation" data-id="9739954"><a href="/opinion/2221553/state-v-pallone/#588" aria-description="Citation for case: State v. Pallone">613 N. W. 2d 568, 588</a></span>, and n. 9 (2000) (Abrahamson, C. J., dissenting) (same); <em>State </em>v. <em>Pierce, </em>136 N. J. 184, 211, <span class="citation" data-id="9517913"><a href="/opinion/2009627/state-v-pierce/#961" aria-description="Citation for case: State v. Pierce">642 A. 2d 947, 961</a></span> (1994) (same).</p>
</footnote>
<footnote label="6">
<p id="b446-6"> Compare <em>United States </em>v. <em>Caseres, </em><span class="citation" data-id="1234081"><a href="/opinion/1234081/united-states-v-caseres/#1072" aria-description="Citation for case: United States v. Caseres">533 F. 3d 1064, 1072</a></span> (CA9 2008) (declining to apply <em>Belton </em>when the arrestee was approached by police after he had exited his vehicle and reached his residence), with <em>Rainey </em>v. <em>Commonwealth, </em><span class="citation" data-id="9620606"><a href="/opinion/1399986/rainey-v-commonwealth/#94" aria-description="Citation for case: Rainey v. Commonwealth">197 S. W. 3d 89, 94-95</a></span> (Ky. 2006) (applying <em>Belton </em>when the arrestee was apprehended 50 feet from the vehicle), and <em>Black </em>v. <em>State, </em><span class="citation" data-id="852893"><a href="/opinion/852893/black-v-state/#716" aria-description="Citation for case: Black v. State">810 N. E. 2d 713, 716</a></span> (Ind. 2004) (applying <em>Belton </em>when the arrestee was apprehended inside an auto repair shop and the vehicle was parked outside).</p>
</footnote>
<footnote label="7">
<p id="b446-7"> Compare <em>McLaughlin, </em><span class="citation" data-id="9491975"><a href="/opinion/762479/united-states-of-america-plaintiff-appellant-v-john-lee-mclaughlin/#890" aria-description="Citation for case: UNITED STATES of America, Plaintiff-Appellant, v. John...">170 F. 3d, at 890-891</a></span> (upholding a search that commenced five minutes after the arrestee was removed from the scene), <em>United States </em>v. <em>Snook, </em><span class="citation" data-id="721372"><a href="/opinion/721372/united-states-v-wayne-steven-snook/#608" aria-description="Citation for case: United States v. Wayne Steven Snook">88 F. 3d 605, 608</a></span> (CA8 1996) (same), and <em>United States </em>v. <em>Doward, </em><span class="citation" data-id="195782"><a href="/opinion/195782/united-states-v-doward/#793" aria-description="Citation for case: United States v. Doward">41 F. 3d 789, 793</a></span> (CA1 1994) (upholding a search that continued after the arrestee was removed from the scene), with <em>United States </em>v. <em>Lugo, </em><span class="citation" data-id="593396"><a href="/opinion/593396/united-states-v-david-m-lugo/#634" aria-description="Citation for case: United States v. David M. Lugo">978 F. 2d 631, 634</a></span> (CA10 1992) (holding invalid a search that commenced after the arrestee was removed from the scene), and <em>State </em>v. <em>Badgett, </em><span class="citation" data-id="7839713"><a href="/opinion/7892532/state-v-badgett/#427" aria-description="Citation for case: State v. Badgett">200 Conn. 412, 427-428</a></span>, <span class="citation" data-id="7839713"><a href="/opinion/7892532/state-v-badgett/#169" aria-description="Citation for case: State v. Badgett">512 A. 2d 160, 169</a></span> (1986) (holding invalid a search that continued after the arrestee was removed from the scene).</p>
</footnote>
<footnote label="8">
<p id="b447-6"> At least eight States have reached the same conclusion. Vermont, New Jersey, New Mexico, Nevada, Pennsylvania, New York, Oregon, and Wyoming have declined to follow a broad reading of <em>Belton </em>under their state constitutions. See <em>State </em>v. <em>Bander, </em><span class="citation multiple-matches"><a href="/c/Vt./181/392/">181 Vt. 392</a></span>, 401, <span class="citation multiple-matches"><a href="/c/A.%202d/924/38/">924 A. 2d 38</a></span>, 46-47 (2007); <em>State </em>v. <em>Eckel, </em>185 N. J. 523, 540, <span class="citation" data-id="2112994"><a href="/opinion/2112994/state-v-eckel/#1277" aria-description="Citation for case: State v. Eckel">888 A. 2d 1266, 1277</a></span> (2006); <em>Camacho </em>v. <em>State, </em><span class="citation" data-id="9788695"><a href="/opinion/2598312/camacho-v-state/#399" aria-description="Citation for case: Camacho v. State">119 Nev. 395, 399-400</a></span>, <span class="citation" data-id="9788695"><a href="/opinion/2598312/camacho-v-state/#373" aria-description="Citation for case: Camacho v. State">75 P. 3d 370, 373-374</a></span> (2003); <em>Vasquez </em>v. <em>State, </em><span class="citation" data-id="9793472"><a href="/opinion/2615534/vasquez-v-state/#488" aria-description="Citation for case: Vasquez v. State">990 P. 2d 476, 488-489</a></span> (Wyo. 1999); <em>State </em>v. <em>Arredondo, </em><span class="citation" data-id="1223809"><a href="/opinion/1223809/state-v-arredondo/" aria-description="Citation for case: State v. Arredondo">1997-NMCA-081</a></span>, 123 N. M. 628, 636 (Ct. App.), overruled on other grounds by <em>State </em>v. <em>Steinzig, </em><span class="citation" data-id="1401546"><a href="/opinion/1401546/state-v-steinzig/" aria-description="Citation for case: State v. Steinzig">1999-NMCA-107</a></span>, 127 N. M. 752 (Ct. App.); <page-number citation-index="1" label="348">*348</page-number><em>Commonwealth </em>v. <em>White, </em><span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#57" aria-description="Citation for case: Commonwealth v. White">543 Pa. 45, 57</a></span>, <span class="citation" data-id="9705016"><a href="/opinion/1983319/commonwealth-v-white/#902" aria-description="Citation for case: Commonwealth v. White">669 A. 2d 896, 902</a></span> (1995); <em>People </em>v. <em>Blasich, </em>73 N. Y. 2d 673, 678, <span class="citation" data-id="5538778"><a href="/opinion/5689505/people-v-blasich/#43" aria-description="Citation for case: People v. Blasich">541 N. E. 2d 40, 43</a></span> (1989); <em>State </em>v. <em>Fesler, </em><span class="citation" data-id="9627414"><a href="/opinion/1427013/state-v-fesler/#612" aria-description="Citation for case: State v. Fesler">68 Ore. App. 609, 612</a></span>, <span class="citation" data-id="9627414"><a href="/opinion/1427013/state-v-fesler/#1016" aria-description="Citation for case: State v. Fesler">685 P. 2d 1014, 1016-1017</a></span> (1984). And a Massachusetts statute provides that a search incident to arrest may be made only for the purposes of seizing weapons or evidence of the offense of arrest. See <em>Commonwealth </em>v. <em>Toole, </em><span class="citation" data-id="2080120"><a href="/opinion/2080120/commonwealth-v-toole/#161" aria-description="Citation for case: Commonwealth v. Toole">389 Mass. 159, 161-162</a></span>, <span class="citation" data-id="2080120"><a href="/opinion/2080120/commonwealth-v-toole/#1266" aria-description="Citation for case: Commonwealth v. Toole">448 N. E. 2d 1264, 1266-1267</a></span> (1983) (citing Mass. Gen. Laws, ch. 276, § 1 (West 2006)).</p>
</footnote>
<footnote label="9">
<p id="b448-14"> Justice Auto’s dissenting opinion also accuses us of “overruling]” <em>Belton </em>and <em>Thornton </em>v. <em>United States, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">541 U. S. 615</a></span> (2004), “even though respondent Gant has not asked us to do so.” <em>Post, </em>at 355. Contrary to that claim, the narrow reading of <em>Belton </em>we adopt today is precisely the result Gant has urged. That Justice Auto has chosen to describe this decision as overruling our earlier cases does not change the fact that the resulting rule of law is the one advocated by respondent.</p>
</footnote>
<footnote label="10">
<p id="b449-6"> Justice Stevens concurred in the judgment in <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#463" aria-description="Citation for case: New York v. Belton">453 U. S., at 463</a></span>, for the reasons stated in his dissenting opinion in <em>Robbins </em>v. <em>California, </em><span class="citation" data-id="9428483"><a href="/opinion/110558/robbins-v-california/#444" aria-description="Citation for case: Robbins v. California">453 U. S. 420, 444</a></span> (1981), Justice Thomas joined the Court’s opinion in <em>Thornton, </em><span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/" aria-description="Citation for case: Thornton v. United States">541 U. S. 615</a></span>, and Justice Scaua and Justice Ginsburg concurred in the judgment in that case, <span class="citation" data-id="9434613"><a href="/opinion/134746/thornton-v-united-states/#625" aria-description="Citation for case: Thornton v. United States"><em>id., </em>at 625</a></span>.</p>
</footnote>
<footnote label="11">
<p id="b449-7"> Because a broad reading of <em>Belton </em>has been widely accepted, the doctrine of qualified immunity will shield officers from liability for searches conducted in reasonable reliance on that understanding.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Arizona v. Hicks.md  (`case`, 6 assertions)

### content_page

```
---
title: "Arizona v. Hicks"
type: case
citation: "480 U.S. 321 (1987)"
parallel_cite: "107 S. Ct. 1149; 94 L. Ed. 2d 347; 55 U.S.L.W. 4258"
neutral_cite: 1987 U.S. LEXIS 1056
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1987
date_decided: 1987-03-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1987-03-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Hicks
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111834/arizona-v-hicks/"
  cluster_id: 111834
  opinion_id: 9430865
  identity_checked: true
homes:
  - page: "[[Plain View Doctrine]]"
    role: "Key — Anchor"
  - page: "[[Trespass]]"
    role: "Related (cross-doctrine)"
related: ["[[Coolidge v. New Hampshire]]", "[[Horton v. California]]", "[[Texas v. Brown]]"]
aliases: []
tags: ["case", "fourth-amendment", "plain-view", "search"]
holding: "Moving stereo equipment a few inches to read serial numbers was a SEARCH separate from the lawful entry, and 'immediately apparent'…"
lake:
  record_id: Arizona v. Hicks
  status: verified
  projected_at: 2026-07-09
---

# Arizona v. Hicks

*480 U.S. 321 (1987)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Police entered Hicks's apartment without a warrant under [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] — a bullet had been fired through the floor, injuring a man below — to look for the shooter, other victims, and weapons. Inside, an officer saw expensive stereo equipment that seemed out of place and suspected it was stolen. He moved the components to read and record their serial numbers, phoned them in, learned a turntable had been taken in an armed robbery, and the equipment was seized.

## Issue
Whether moving stereo equipment to read its serial numbers — done on reasonable suspicion during an exigent-circumstances entry — was a "search," and if so whether the [[Plain View Doctrine|plain-view doctrine]] required probable cause rather than mere reasonable suspicion.

## Rule
Moving the equipment to expose hidden information was a new search beyond the entry's justification: the moving of the components "did constitute a 'search' separate and apart from the search for ... the shooter, victims, and weapons that was the lawful objective of his entry into the apartment." — 480 U.S. at 324. ^pin-324

"A search is a search, even if it happens to disclose nothing but the bottom of a turntable." — [*Id.* at 325](https://www.courtlistener.com/opinion/111834/arizona-v-hicks/#:~:text=A%20search%20is%20a%20search%2C). ^pin-325

The [[Plain View Doctrine|plain-view doctrine]] requires probable cause: "We now hold that probable cause is required. To say otherwise would be to cut the 'plain view' doctrine loose from its theoretical and practical moorings." — *Id.* at 326. ^pin-326

## Application
The officer's lawful basis for being in the apartment was the shooting [[Exigent Circumstances and Hot Pursuit|exigency]]; turning the turntable to read a concealed serial number was unrelated to that [[Exigent Circumstances and Hot Pursuit|exigency]] and exposed information the officer could not otherwise see, so it was a separate search. Because the State conceded the officer had only reasonable suspicion — not probable cause — that the equipment was stolen, the [[Plain View Doctrine|plain-view doctrine]] could not justify the search on these facts, and it was unreasonable.

## Conclusion
Moving the equipment was an unreasonable search; the judgment of the Arizona Court of Appeals suppressing the evidence was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Hicks* fixes two plain-view rules: physically *moving* an object to expose hidden details is a search, and invoking the [[Plain View Doctrine|plain-view doctrine]] to examine or seize an item requires **probable cause** (the item's incriminating character must be "immediately apparent"). It works alongside [[Coolidge v. New Hampshire]] (origin of the doctrine) and [[Horton v. California]] (dropping the inadvertence requirement).

## Appears on
- [[Plain View Doctrine]] — *Key — Anchor*
- [[Trespass]] — *Related (cross-doctrine)*

## Sources
- *Arizona v. Hicks*, 480 U.S. 321 (1987) — https://www.courtlistener.com/opinion/111834/arizona-v-hicks/ — pinpoints: 324, 325, 326.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e9cd0520b0bb4ad2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "480 U.S. 321 (1987)", "court": "U.S. Supreme Court", "neutral_cite": "1987 U.S. LEXIS 1056", "official_citation_present": true, "parallel_cite": "107 S. Ct. 1149; 94 L. Ed. 2d 347; 55 U.S.L.W. 4258", "title": "Arizona v. Hicks", "year": "1987"}}
{"assertion_id": "07d374b789a47523", "dimension": "support", "kind": "home_role", "locator": {"home": "Plain View Doctrine"}, "payload": {"home": "Plain View Doctrine", "role": "Key — Anchor", "title": "Arizona v. Hicks"}}
{"assertion_id": "80bd3db1d634c8a8", "dimension": "support", "kind": "home_role", "locator": {"home": "Trespass"}, "payload": {"home": "Trespass", "role": "Related (cross-doctrine)", "title": "Arizona v. Hicks"}}
{"assertion_id": "c1454051816ec36e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Moving stereo equipment a few inches to read serial numbers was a SEARCH separate from the lawful entry, and 'immediately apparent'…", "title": "Arizona v. Hicks"}}
{"assertion_id": "6cb6bb896b2b627d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1987-03-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arizona v. Hicks", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Arizona v. Hicks", "varies_by_point": "false"}}
{"assertion_id": "e758c816540f0e89", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Hicks"}}
```

### lake record — Arizona v. Hicks

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Hicks",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Hicks",
    "case_name_short": "Hicks",
    "case_name_full": "Arizona v. Hicks",
    "input_case_name": "Arizona v. Hicks",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1987-03-03",
    "year": 1987,
    "docket": null,
    "cluster_id": 111834,
    "lead_opinion_id": 9430865,
    "sibling_ids": [
      111834,
      9430865,
      9430866,
      9430867,
      9430868,
      9430869,
      9430870
    ],
    "absolute_url": "/opinion/111834/arizona-v-hicks/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "480 U.S. 321",
      "volume": "480",
      "reporter": "U.S.",
      "page": "321",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "107 S. Ct. 1149",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 347",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4258",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4258",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1987 U.S. LEXIS 1056",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1056",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "480 U.S. 321",
        "volume": "480",
        "reporter": "U.S.",
        "page": "321",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "107 S. Ct. 1149",
        "volume": "107",
        "reporter": "S. Ct.",
        "page": "1149",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "94 L. Ed. 2d 347",
        "volume": "94",
        "reporter": "L. Ed. 2d",
        "page": "347",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1987 U.S. LEXIS 1056",
        "volume": "1987",
        "reporter": "U.S. LEXIS",
        "page": "1056",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "55 U.S.L.W. 4258",
        "volume": "55",
        "reporter": "U.S.L.W.",
        "page": "4258",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "480 U.S. 321",
    "official_selection": {
      "court_class": "scotus",
      "selected": "480 U.S. 321",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-324",
      "page": null,
      "quote": "and if so whether the plain-view doctrine required probable cause rather than mere reasonable suspicion. ## Rule Moving the equipment to expose hidden information was a new search beyond the entry's justification: the moving of the components",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-325",
      "page": null,
      "quote": "A search is a search, even if it happens to disclose nothing but the bottom of a turntable.",
      "star_marker": "325",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 7220,
      "fragment": "#:~:text=A%20search%20is%20a%20search%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-326",
      "page": null,
      "quote": "We now hold that probable cause is required. To say otherwise would be to cut the 'plain view' doctrine loose from its theoretical and practical moorings.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1987-03-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Hicks",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Martin v. State",
          "cluster_id": 10740496,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Bock (A169480)",
          "cluster_id": 10134134,
          "cite": [
            "310 Or. App. 329",
            "485 P.3d 931"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
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
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532255,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Nathan Ray Foreman v. State",
          "cluster_id": 4532252,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Barry Trynell Davis, Jr. v. State of Florida",
          "cluster_id": 4390534,
          "cite": [
            "217 So. 3d 1006",
            "42 Fla. L. Weekly Supp. 558",
            "2017 WL 1954979",
            "2017 Fla. LEXIS 1055"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Kaeppeler",
          "cluster_id": 3166351,
          "cite": [
            "473 Mass. 396",
            "42 N.E.3d 1090"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gamache",
          "cluster_id": 2814721,
          "cite": [
            "792 F.3d 194",
            "2015 U.S. App. LEXIS 11586",
            "2015 WL 4071911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Telshaw",
          "cluster_id": 2701202,
          "cite": [
            "2011 Ohio 3373",
            "195 Ohio App. 3d 596",
            "961 N.E.2d 223"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane1_negative"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Soldal v. Cook County",
          "cluster_id": 112795,
          "cite": [
            "121 L. Ed. 2d 450",
            "113 S. Ct. 538",
            "506 U.S. 56",
            "1992 U.S. LEXIS 7835",
            "92 Daily Journal DAR 16378",
            "61 U.S.L.W. 4019",
            "6 Fla. L. Weekly Fed. S 769",
            "92 Cal. Daily Op. Serv. 9794"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bradford",
          "cluster_id": 1239150,
          "cite": [
            "15 Cal. 4th 1229",
            "939 P.2d 259",
            "97 Daily Journal DAR 9003",
            "97 Cal. Daily Op. Serv. 5537",
            "65 Cal. Rptr. 2d 145",
            "1997 Cal. LEXIS 3699"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Grimstead",
          "cluster_id": 1376491,
          "cite": [
            "407 S.E.2d 47",
            "12 Va. App. 1066",
            "8 Va. Law Rep. 449",
            "1991 Va. App. LEXIS 205"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jose Luis Guzman and Sonia Cruz-Lazo",
          "cluster_id": 516479,
          "cite": [
            "864 F.2d 1512",
            "1988 U.S. App. LEXIS 17681",
            "1988 WL 138644"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zarnow v. CITY OF WICHITA FALLS, TEX.",
          "cluster_id": 152551,
          "cite": [
            "614 F.3d 161",
            "2010 U.S. App. LEXIS 16445",
            "2010 WL 3093443"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Bostic",
          "cluster_id": 2542685,
          "cite": [
            "148 P.3d 250",
            "2006 Colo. App. LEXIS 622",
            "2006 WL 1171864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Clark",
          "cluster_id": 1121458,
          "cite": [
            "857 P.2d 1099",
            "5 Cal. 4th 950",
            "22 Cal. Rptr. 2d 689",
            "93 Daily Journal DAR 11122",
            "93 Cal. Daily Op. Serv. 6528",
            "1993 Cal. LEXIS 4179"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ronald Tobin, Clifford Roger Ackerson, United States of America v. Ronald Tobin",
          "cluster_id": 554960,
          "cite": [
            "923 F.2d 1506",
            "1991 U.S. App. LEXIS 2683"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jones",
          "cluster_id": 2058953,
          "cite": [
            "830 N.E.2d 541",
            "215 Ill. 2d 261",
            "294 Ill. Dec. 129",
            "2005 Ill. LEXIS 632"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Champion",
          "cluster_id": 2032324,
          "cite": [
            "549 N.W.2d 849",
            "452 Mich. 92"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 5607944,
          "cite": [
            "21 Cal. 4th 668",
            "99 Cal. Daily Op. Serv. 6990",
            "99 Daily Journal DAR 8867",
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "1999 Cal. LEXIS 5534"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bridges",
          "cluster_id": 1060919,
          "cite": [
            "963 S.W.2d 487",
            "1997 Tenn. LEXIS 642",
            "1997 WL 804620"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Flamer v. State",
          "cluster_id": 1486303,
          "cite": [
            "585 A.2d 736",
            "1990 Del. LEXIS 408"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
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
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jones v. State",
          "cluster_id": 853051,
          "cite": [
            "783 N.E.2d 1132",
            "2003 WL 734194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Hicks:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQ4MTM0NDAwMDAwJnM9MjAxMDQ2MCZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111834+OR+9430865+OR+9430866+OR+9430867+OR+9430868+OR+9430869+OR+9430870%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNjgmcz02MDc4ODkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111834+OR+9430865+OR+9430866+OR+9430867+OR+9430868+OR+9430869+OR+9430870%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870)",
        "reviewed": 37,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 37,
        "triage_read": 1,
        "triage_snippet_classified": 36
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111834 OR 9430865 OR 9430866 OR 9430867 OR 9430868 OR 9430869 OR 9430870)",
    "indexed_citing_opinions": 951,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111834,
        "count": 821,
        "count_source": "search"
      },
      {
        "opinion_id": 9430865,
        "count": 148,
        "count_source": "search"
      },
      {
        "opinion_id": 9430866,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430867,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430868,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430869,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9430870,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1525,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-hicks.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MjQ5Nzkmcz0xMDAzMjc0NSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28111834+OR+9430865+OR+9430866+OR+9430867+OR+9430868+OR+9430869+OR+9430870%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111834,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 107898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110901,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111301,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 111600,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 365436,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 377016,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 403710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 434694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1172524,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1268637,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1286575,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1939307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1978640,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 1998068,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111834,
        "cited_id": 2056305,
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
    "date_created": "2026-07-04T18:25:14Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:25:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:25:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:30:31Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:25:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Hicks

```
<opinion type="majority">
<author id="b369-7"><page-number citation-index="1" label="323">*323</page-number>Justice Scalia</author>
<p id="ARf">delivered the opinion of the Court.</p>
<p id="b369-8">In <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443</a></span> (1971), we said that in certain circumstances a warrantless seizure by police of an item that comes within plain view during their lawful search of a private area may be reasonable under the Fourth Amendment. See <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 465-471</a></span> (plurality opinion); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#505" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 505-506</a></span> (Black, J., concurring and dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#521" aria-description="Citation for case: Coolidge v. New Hampshire"><em>id., </em>at 521-522</a></span> (White, J., concurring and dissenting). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./475/1107/">475 U. S. 1107</a></span> (1986), in the present case to decide whether this “plain view” doctrine may be invoked when the police have less than probable cause to believe that the item in question is evidence of a crime or is contraband.</p>
<p id="b369-9">HH</p>
<p id="b369-3">On April 18, 1984, a bullet was fired through the floor of respondent’s apartment, striking and injuring a man in the apartment below. Police officers arrived and entered respondent’s apartment to search for the shooter, for other victims, and for weapons. They found and seized three weapons, including a sawed-off rifle, and in the course of their search also discovered a stocking-cap mask.</p>
<p id="b369-4">One of the policemen, Officer Nelson, noticed two sets of expensive stereo components, which seemed out of place in the squalid and otherwise ill-appointed four-room apartment. Suspecting that they were stolen, he read and recorded their serial numbers — moving some of the components, including a Bang and Olufsen turntable, in order to do so — which he then reported by phone to his headquarters. On being advised that the turntable had been taken in an armed robbery, he seized it immediately. It was later determined that some of the other serial numbers matched those on other stereo equipment taken in the same armed robbery, and a warrant <page-number citation-index="1" label="324">*324</page-number>was obtained and executed to seize that equipment as well. Respondent was subsequently indicted for the robbery.</p>
<p id="b370-7">The state trial court granted respondent’s motion to suppress the evidence that had been seized. The Court of Appeals of Arizona affirmed. It was conceded that the initial entry and search, although warrantless, were justified by the exigent circumstance of the shooting. The Court of Appeals viewed the obtaining of the serial numbers, however, as an additional search, unrelated to that exigency. Relying upon a statement in <em>Mincey </em>v. <em>Arizona, </em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), that a “warrantless search must be ‘strictly circumscribed by the exigencies which justify its initiation,”’ <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona"><em>id., </em>at 393</a></span> (citation omitted), the Court of Appeals held that the police conduct violated the Fourth Amendment, requiring the evidence derived from that conduct to be excluded. <span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#534" aria-description="Citation for case: State v. Hicks">146 Ariz. 533, 534-535</a></span>, <span class="citation" data-id="1268637"><a href="/opinion/1268637/state-v-hicks/#332" aria-description="Citation for case: State v. Hicks">707 P. 2d 331, 332-333</a></span> (1985). Both courts-the trial court explicitly and the Court of Appeals by necessary implication — rejected the State’s contention that Officer Nelson’s actions were justified under the “plain view” doctrine of <em>Coolidge </em>v. <em>New <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Hampshire, supra.</a></span> </em>The Arizona Supreme Court denied review, and the State filed this petition.</p>
<p id="b370-8">r — 1 h — I</p>
<p id="b370-3">As an initial matter, the State argues that Officer Nelson s actions constituted neither a “search” nor a “seizure” within the meaning of the Fourth Amendment. We agree that the mere recording of the serial numbers did not constitute a seizure. To be sure, that was the first step in a process by which respondent was eventually deprived of the stereo equipment. In and of itself, however, it did not “meaningfully interfere” with respondent’s possessory interest in either the serial numbers or the equipment, and therefore did not amount to a seizure. See <em>Maryland </em>v. <em>Macon, </em><span class="citation" data-id="9430099"><a href="/opinion/111477/maryland-v-macon/#469" aria-description="Citation for case: Maryland v. MacOn">472 U. S. 463, 469</a></span> (1985).</p>
<p id="b370-4">Officer Nelson’s moving of the equipment, however, did constitute a “search” separate and apart from the search for <page-number citation-index="1" label="325">*325</page-number>the shooter, victims, and weapons that was the lawful objective of his entry into the apartment. Merely inspecting those parts of the turntable that came into view during the latter search would not have constituted an independent search, because it would have produced no additional invasion of respondent’s privacy interest. See <em>Illinois </em>v. <em>Andreas, </em><span class="citation" data-id="9429344"><a href="/opinion/111013/illinois-v-andreas/#771" aria-description="Citation for case: Illinois v. Andreas">463 U. S. 765, 771</a></span> (1983). But taking action, unrelated to the objectives of the authorized intrusion, which exposed to view concealed portions of the apartment or its contents, did produce a new invasion of respondent’s privacy unjustified by the exigent circumstance that validated the entry. This is why, contrary to Justice Powell’s suggestion, <em>post, </em>at 333, the “distinction between ‘looking’ at a suspicious object in plain view and ‘moving’ it even a few inches” is much more than trivial for purposes of the Fourth Amendment. It matters not that the search uncovered nothing of any great personal value to respondent — serial numbers rather than (what might conceivably have been hidden behind or under the equipment) letters or photographs. A search is a search, even if it happens to disclose nothing but the bottom of a turntable.</p>
<p id="b371-5">Ill</p>
<p id="b371-6">The remaining question is whether the search was “reasonable” under the Fourth Amendment.</p>
<p id="b371-7">On this aspect of the case we reject, at the outset, the apparent position of the Arizona Court of Appeals that because the officers’ action directed to the stereo equipment was unrelated to the justification for their entry into respondent’s apartment, it was <em>ipso facto </em>unreasonable. That lack of relationship <em>always </em>exists with regard to action validated under the “plain view” doctrine; where action is taken for the purpose justifying the entry, invocation of the doctrine is superfluous. <em>Mincey </em>v. <em><span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Arizona, supra,</a></span> </em>in saying that a warrantless search must be “strictly circumscribed by the exigencies which justify its initiation,” <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#393" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 393</a></span> (citation omitted), was addressing only the scope of the primary <page-number citation-index="1" label="326">*326</page-number>search itself, and was not overruling by implication the many cases acknowledging that the “plain view” doctrine can legitimate action beyond that scope.</p>
<p id="b372-5">We turn, then, to application of the doctrine to the facts of this case. “It is well established that under certain circumstances the police may <em>seize </em>evidence in plain view without a warrant,” <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 465</a></span> (plurality opinion) (emphasis added). Those circumstances include situations “[w]here the initial intrusion that brings the police within plain view of such [evidence] is supported ... by one of the recognized exceptions to the warrant requirement,” <em>ibid., </em>such as the exigent-circumstances intrusion here. It would be absurd to say that an object could lawfully be seized and taken from the premises, but could not be moved for closer examination. It is clear, therefore, that the search here was valid if the “plain view” doctrine would have sustained a seizure of the equipment.</p>
<p id="b372-6">There is no doubt it would have done so if Officer Nelson had probable cause to believe that the equipment was stolen. The State has conceded, however, that he had only a “reasonable suspicion,” by which it means something less than probable cause. See Brief for Petitioner 18-19.* We have not ruled on the question whether probable cause is required in order to invoke the “plain view” doctrine. Dicta in <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#587" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 587</a></span> (1980), suggested that the standard of probable cause must be met, but our later opinions in <em>Texas </em>v. <em>Brown, </em><span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/" aria-description="Citation for case: Texas v. Brown">460 U. S. 730</a></span> (1983), explicitly regarded the issue as unresolved, see <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#742" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 742, n. 7</a></span> (plurality opinion); <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#746" aria-description="Citation for case: Texas v. Brown"><em>id., </em>at 746</a></span> (Stevens, J., concurring in judgment).</p>
<p id="b372-7">We now hold that probable cause is required. To say otherwise would be to cut the “plain view” doctrine loose from its theoretical and practical moorings. The theory of that doctrine consists of extending to nonpublic places such as the <page-number citation-index="1" label="327">*327</page-number>home, where searches and seizures without a warrant are presumptively unreasonable, the police’s longstanding authority to make warrantless seizures in public places of such objects as weapons and contraband. See <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 586-587</a></span>. And the practical justification for that extension is the desirability of sparing police, whose viewing of the object in the course of a lawful search is as legitimate as it would have been in a public place, the inconvenience and the risk — to themselves or to preservation of the evidence — of going to obtain a warrant. See <em>Coolidge </em>v. <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#468" aria-description="Citation for case: Coolidge v. New Hampshire"><em>New Hampshire, supra, </em>at 468</a></span> (plurality opinion). Dispensing with the need for a warrant is worlds apart from permitting a lesser standard of <em>cause </em>for the seizure than a warrant would require, <em>i. e., </em>the standard of probable cause. No reason is apparent why an object should routinely be seizable on lesser grounds, during an unrelated search and seizure, than would have been needed to obtain a warrant for that same object if it had been known to be on the premises.</p>
<p id="b373-5">We do not say, of course, that a seizure can never be justified on less than probable cause. We have held that it can— where, for example, the seizure is minimally intrusive and operational necessities render it the only practicable means of detecting certain types of crime. See, <em>e. g., United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/" aria-description="Citation for case: United States v. Cortez">449 U. S. 411</a></span> (1981) (investigative detention of vehicle suspected to be transporting illegal aliens); <em>United States </em>v. <em>Brignoni-Ponce, </em><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975) (same); <em>United States </em>v. <em>Place, </em><span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#709" aria-description="Citation for case: United States v. Place">462 U. S. 696, 709</a></span>, and n. 9 (1983) (dictum) (seizure of suspected drug dealer’s luggage at airport to permit exposure to specially trained dog). No special operational necessities are relied on here, however — but rather the mere fact that the items in question came lawfully within the officer’s plain view. That alone cannot supplant the requirement of probable cause.</p>
<p id="b373-6">The same considerations preclude us from holding that, even though probable cause would have been necessary for a <em>seizure, </em>the <em>search </em>of objects in plain view that occurred here <page-number citation-index="1" label="328">*328</page-number>could be sustained on lesser grounds. A dwelling-place search, no less than a dwelling-place seizure, requires probable cause, and there is no reason in theory or practicality why application of the “plain view” doctrine would supplant that requirement. Although the interest protected by the Fourth Amendment injunction against unreasonable searches is quite different from that protected by its injunction against unreasonable seizures, see <em>Texas </em>v. <span class="citation" data-id="9429131"><a href="/opinion/110901/texas-v-brown/#747" aria-description="Citation for case: Texas v. Brown"><em>Brown, supra, </em>at 747-748</a></span> (Stevens, J., concurring in judgment), neither the one nor the other is of inferior worth or necessarily requires only lesser protection. We have not elsewhere drawn a categorical distinction between the two insofar as concerns the degree of justification needed to establish the reasonableness of police action, and we see no reason for a distinction in the particular circumstances before us here. Indeed, to treat searches more liberally would especially erode the plurality’s warning in <em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/" aria-description="Citation for case: Coolidge v. New Hampshire">Coolidge</a></span> </em>that “the ‘plain view’ doctrine may not be used to extend a general exploratory search from one object to another until something incriminating at last emerges.” <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#466" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S., at 466</a></span>. In short, whether legal authority to move the equipment could be found only as an inevitable concomitant of the authority to seize it, or also as a consequence of some independent power to search certain objects in plain view, probable cause to believe the equipment was stolen was required.</p>
<footnote label="*">
<p id="b372-8">Contrary to the suggestion in Justice O’Connor’s dissent, <em>post, </em>at 339, this concession precludes our considering whether the probable-cause standard was satisfied in this case.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Arizona v. Johnson.md  (`case`, 6 assertions)

### content_page

```
---
title: "Arizona v. Johnson"
type: case
citation: "555 U.S. 323 (2009)"
parallel_cite: "129 S. Ct. 781; 172 L. Ed. 2d 694"
neutral_cite: 2009 U.S. LEXIS 868
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2009
date_decided: 2009-01-26
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2009-01-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Arizona v. Johnson
  varies_by_point: false
  scope_note: "Good law. During a lawful traffic stop every occupant is seized for the stop's duration, so the first Terry condition is satisfied without separate suspicion that a passenger is committing a crime; to frisk that passenger the officer needs reasonable suspicion the passenger is armed and dangerous."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/145912/arizona-v-johnson/"
  cluster_id: 145912
  opinion_id: 145912
  identity_checked: true
homes:
  - page: "[[Traffic Stops]]"
    role: "Progeny"
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
related: ["[[Terry v. Ohio]]", "[[Brendlin v. California]]", "[[Maryland v. Wilson]]", "[[Pennsylvania v. Mimms]]"]
aliases: []
tags: ["case", "fourth-amendment", "traffic-stop", "frisk", "passenger", "terry-stop"]
holding: "During a lawful traffic stop, a passenger is seized for the duration of the stop (satisfying Terry's first condition without separate suspicion of the passenger's criminal activity); an officer may frisk the passenger on reasonable suspicion that the passenger is armed and dangerous."
lake:
  record_id: Arizona v. Johnson
  status: verified
  projected_at: 2026-07-06
---

# Arizona v. Johnson

*555 U.S. 323 (2009)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Members of an Arizona gang task force stopped a car near a Crips neighborhood in Tucson after a plate check showed the registration was suspended — a civil infraction warranting only a citation. The car had three occupants, including back-seat passenger Lemon Johnson. Officer Trevizo learned that Johnson was from a town with a Crips gang, had a police scanner in his jacket, and gave answers suggesting gang affiliation. Suspecting he was armed, she had him step out and patted him down, finding a gun. Johnson was convicted of unlawful gun possession; the Arizona Court of Appeals reversed, reasoning that because the encounter had become consensual and Johnson was not suspected of separate criminal activity, the frisk was unlawful.

## Issue
Whether, during a lawful traffic stop, an officer may frisk a passenger for weapons when the officer has reasonable suspicion the passenger is armed and dangerous but lacks suspicion that the passenger is independently engaged in criminal activity.

## Rule
Yes. A *[[Terry v. Ohio|Terry]]* stop and frisk requires two things: "The Court upheld 'stop and frisk' as constitutionally permissible if two conditions are met. First, the investigatory stop must be lawful. . . . Second, to proceed from a stop to a frisk, the police officer must reasonably suspect that the person stopped is armed and dangerous." — 555 U.S. at 326–327. ^pin-326

In the traffic-stop setting both conditions are satisfied on the stop alone plus armed-and-dangerous suspicion: "in a traffic-stop setting, the first *Terry* condition — a lawful investigatory stop — is met whenever it is lawful for police to detain an automobile and its occupants pending inquiry into a vehicular violation. The police need not have, in addition, cause to believe any occupant of the vehicle is involved in criminal activity. To justify a patdown of the driver or a passenger during a traffic stop, however, just as in the case of a pedestrian reasonably suspected of criminal activity, the police must harbor reasonable suspicion that the person subjected to the frisk is armed and dangerous." — *Id.* at 327. ^pin-327

That is so because "[f]or the duration of a traffic stop, . . . a police officer effectively seizes 'everyone in the vehicle,' the driver and all passengers." — *Id.* (quoting *Brendlin v. California*). ^pin-327b

## Application
The task-force officers lawfully stopped the car for a registration violation, and that stop seized all of its occupants — including Johnson — for its duration. Johnson therefore remained lawfully detained even though the officers had no suspicion he was independently committing a crime; the encounter had not become a consensual one merely because he was cooperative. Because Trevizo developed reasonable suspicion that Johnson was armed and dangerous (gang indicia, a scanner, evasive gang-related answers), she was entitled to pat him down for weapons. The Court reversed the Arizona Court of Appeals and [[Reading and Citing Cases#on-remand|remanded]], leaving the appeals court free to revisit whether Trevizo in fact had reasonable suspicion that Johnson was armed — a point that court had only assumed.

## Conclusion
The frisk did not require separate suspicion that the passenger was engaged in criminal activity; a lawful traffic stop seizes the passenger, and the frisk is justified by reasonable suspicion the passenger is armed and dangerous. Reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Johnson* confirms and combines [[Pennsylvania v. Mimms]], [[Maryland v. Wilson]], and [[Brendlin v. California]] for the traffic-stop context and applies the frisk standard of [[Terry v. Ohio]] to passengers.

## Appears on
- [[Traffic Stops]] — *Progeny*
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*

## Sources
- *Arizona v. Johnson*, 555 U.S. 323 (2009) — https://www.courtlistener.com/opinion/145912/arizona-v-johnson/ — pinpoints: 326–327.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "3f535552385c29b8", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "555 U.S. 323 (2009)", "court": "U.S. Supreme Court", "neutral_cite": "2009 U.S. LEXIS 868", "official_citation_present": true, "parallel_cite": "129 S. Ct. 781; 172 L. Ed. 2d 694", "title": "Arizona v. Johnson", "year": "2009"}}
{"assertion_id": "0204863fb6b4156a", "dimension": "support", "kind": "home_role", "locator": {"home": "Traffic Stops"}, "payload": {"home": "Traffic Stops", "role": "Progeny", "title": "Arizona v. Johnson"}}
{"assertion_id": "7d9c386d86ceb7bc", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "During a lawful traffic stop, a passenger is seized for the duration of the stop (satisfying Terry's first condition without separate suspicion of the passenger's criminal activity); an officer may frisk the passenger on reasonable suspicion that the passenger is armed and dangerous.", "title": "Arizona v. Johnson"}}
{"assertion_id": "c0bf8c21784ad4d7", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "Arizona v. Johnson"}}
{"assertion_id": "1541d05b1b394c54", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2009-01-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Arizona v. Johnson", "field_i_validity": "good_law", "scope_note": "Good law. During a lawful traffic stop every occupant is seized for the stop's duration, so the first Terry condition is satisfied without separate suspicion that a passenger is committing a crime; to frisk that passenger the officer needs reasonable suspicion the passenger is armed and dangerous.", "title": "Arizona v. Johnson", "varies_by_point": "false"}}
{"assertion_id": "dccd60e1f2622ef6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Arizona v. Johnson"}}
```

### lake record — Arizona v. Johnson

```json
{
  "schema_version": "s2.v1",
  "record_id": "Arizona v. Johnson",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Arizona v. Johnson",
    "case_name_short": "",
    "case_name_full": "Arizona v. Johnson",
    "input_case_name": "Arizona v. Johnson",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2009-01-26",
    "year": 2009,
    "docket": null,
    "cluster_id": 145912,
    "lead_opinion_id": 145912,
    "sibling_ids": [
      145912
    ],
    "absolute_url": "/opinion/145912/arizona-v-johnson/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "555 U.S. 323",
      "volume": "555",
      "reporter": "U.S.",
      "page": "323",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "129 S. Ct. 781",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "781",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 694",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2009 U.S. LEXIS 868",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "868",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "555 U.S. 323",
        "volume": "555",
        "reporter": "U.S.",
        "page": "323",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "129 S. Ct. 781",
        "volume": "129",
        "reporter": "S. Ct.",
        "page": "781",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "172 L. Ed. 2d 694",
        "volume": "172",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2009 U.S. LEXIS 868",
        "volume": "2009",
        "reporter": "U.S. LEXIS",
        "page": "868",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "555 U.S. 323",
    "official_selection": {
      "court_class": "scotus",
      "selected": "555 U.S. 323",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-326",
      "page": null,
      "quote": "--- # Arizona v. Johnson *555 U.S. 323 (2009)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Members of an Arizona gang task force stopped a car near a Crips neighborhood in Tucson after a plate check showed the registration was suspended \u2014 a civil infraction warranting only a citation. The car had three occupants, including back-seat passenger Lemon Johnson. Officer Trevizo learned that Johnson was from a town with a Crips gang, had a police scanner in his jacket, and gave answers suggesting gang affiliation. Suspecting he was armed, she had him step out and patted him down, finding a gun. Johnson was convicted of unlawful gun possession; the Arizona Court of Appeals reversed, reasoning that because the encounter had become consensual and Johnson was not suspected of separate criminal activity, the frisk was unlawful. ## Issue Whether, during a lawful traffic stop, an officer may frisk a passenger for weapons when the officer has reasonable suspicion the passenger is armed and dangerous but lacks suspicion that the passenger is independently engaged in criminal activity. ## Rule Yes. A *Terry* stop and frisk requires two things:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-327",
      "page": null,
      "quote": "in a traffic-stop setting, the first *Terry* condition \u2014 a lawful investigatory stop \u2014 is met whenever it is lawful for police to detain an automobile and its occupants pending inquiry into a vehicular violation. The police need not have, in addition, cause to believe any occupant of the vehicle is involved in criminal activity. To justify a patdown of the driver or a passenger during a traffic stop, however, just as in the case of a pedestrian reasonably suspected of criminal activity, the police must harbor reasonable suspicion that the person subjected to the frisk is armed and dangerous.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-327b",
      "page": null,
      "quote": "[f]or the duration of a traffic stop, . . . a police officer effectively seizes 'everyone in the vehicle,' the driver and all passengers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2009-01-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Arizona v. Johnson",
    "varies_by_point": false,
    "scope_note": "Good law. During a lawful traffic stop every occupant is seized for the stop's duration, so the first Terry condition is satisfied without separate suspicion that a passenger is committing a crime; to frisk that passenger the officer needs reasonable suspicion the passenger is armed and dangerous.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State of Iowa v. Juan Daniel Salcedo",
          "cluster_id": 4678847,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Juan Daniel Salcedo",
          "cluster_id": 4677110,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane1_negative"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. United States",
          "cluster_id": 803270,
          "cite": [
            "183 L. Ed. 2d 351",
            "132 S. Ct. 2492",
            "567 U.S. 387",
            "2012 U.S. LEXIS 4872",
            "80 U.S.L.W. 4539",
            "23 Fla. L. Weekly Fed. S 437",
            "2012 WL 2368661",
            "95 Empl. Prac. Dec. (CCH) 44,539",
            "115 Fair Empl. Prac. Cas. (BNA) 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Chavez-Barragan",
          "cluster_id": 4260741,
          "cite": [
            "2016 CO 66",
            "379 P.3d 330",
            "2016 WL 5375502"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Manuel De Jesus Ortega Melendr v. Joseph M. Arpaio",
          "cluster_id": 809224,
          "cite": [
            "695 F.3d 990",
            "2012 WL 4358727",
            "2012 U.S. App. LEXIS 20120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Erickson Meko Campbell",
          "cluster_id": 6357475,
          "cite": [
            "26 F.4th 860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kelly v. Borough of Carlisle",
          "cluster_id": 176451,
          "cite": [
            "622 F.3d 248",
            "38 Media L. Rep. (BNA) 2473",
            "2010 U.S. App. LEXIS 20430",
            "2010 WL 3835209"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Randall Lee Pals",
          "cluster_id": 4472392,
          "cite": [
            "805 N.W.2d 767",
            "2011 Iowa Sup. LEXIS 87"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
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
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lerma v. State",
          "cluster_id": 6241263,
          "cite": [
            "543 S.W.3d 184"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Hicks, M., Aplt.",
          "cluster_id": 4625130,
          "cite": [
            "208 A.3d 916"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leyva",
          "cluster_id": 891705,
          "cite": [
            "2011 NMSC 9",
            "250 P.3d 861",
            "149 N.M. 435",
            "2011 NMSC 009"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Lewis",
          "cluster_id": 626016,
          "cite": [
            "674 F.3d 1298",
            "2012 WL 967969"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Decarlos George",
          "cluster_id": 1085503,
          "cite": [
            "732 F.3d 296",
            "2013 WL 5630234",
            "2013 U.S. App. LEXIS 20902"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dancy v. McGinley",
          "cluster_id": 4327925,
          "cite": [
            "843 F.3d 93",
            "2016 U.S. App. LEXIS 21753",
            "2016 WL 7118403"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Colyar",
          "cluster_id": 2643140,
          "cite": [
            "2013 IL 111835"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. White",
          "cluster_id": 172784,
          "cite": [
            "584 F.3d 935",
            "2009 U.S. App. LEXIS 23296",
            "2009 WL 3381528"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Vinton",
          "cluster_id": 187527,
          "cite": [
            "594 F.3d 14",
            "389 U.S. App. D.C. 199",
            "2010 U.S. App. LEXIS 2450",
            "2010 WL 392347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Liberal v. Estrada",
          "cluster_id": 183026,
          "cite": [
            "632 F.3d 1064",
            "2011 U.S. App. LEXIS 957",
            "2011 WL 149348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Mark Dunbar (077839) (Monmouth and Statewide",
          "cluster_id": 4407425,
          "cite": [
            "229 N.J. 521",
            "163 A.3d 875",
            "2017 WL 2962256",
            "2017 N.J. LEXIS 747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kenneth Cochrane",
          "cluster_id": 814022,
          "cite": [
            "702 F.3d 334",
            "2012 U.S. App. LEXIS 25980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Palmer",
          "cluster_id": 3196774,
          "cite": [
            "820 F.3d 640",
            "2016 WL 1594793"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Gomez",
          "cluster_id": 8443636,
          "cite": [
            "877 F.3d 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estrada v. Rhode Island",
          "cluster_id": 204167,
          "cite": [
            "594 F.3d 56",
            "102 A.L.R. 6th 845",
            "2010 U.S. App. LEXIS 2390",
            "2010 WL 376978"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Arizona v. Johnson:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(145912) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTU3OTY0ODAwMDAwJnM9NDYyMDQyMiZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28145912%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 2,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 3,
        "triage_snippet_classified": 197
      },
      "lane2_top_cited": {
        "query": "cites:(145912)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04MyZzPTQ0NzY3OTAmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28145912%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(145912)",
        "reviewed": 85,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 85,
        "triage_read": 0,
        "triage_snippet_classified": 85
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(145912)",
    "indexed_citing_opinions": 743,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 145912,
        "count": 743,
        "count_source": "search"
      }
    ],
    "citation_count": 1709,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/arizona-v-johnson.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNjI2NDImcz0xMDM1NzIwOSZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28145912%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 145912,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 112631,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 118086,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 142878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 145712,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 145912,
        "cited_id": 2600240,
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
    "date_created": "2026-07-04T18:30:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T18:30:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T18:30:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T18:35:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T18:30:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Arizona v. Johnson

```
(Slip Opinion)              OCTOBER TERM, 2008                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                         ARIZONA v. JOHNSON

      CERTIORARI TO THE COURT OF APPEALS OF ARIZONA

 No. 07–1122. Argued December 9, 2008—Decided January 26, 2009
In Terry v. Ohio, 392 U. S. 1, this Court held that a “stop and frisk”
  may be conducted without violating the Fourth Amendment’s ban on
  unreasonable searches and seizures if two conditions are met. First,
  the investigatory stop (temporary detention) must be lawful, a re
  quirement met in an on-the-street encounter when a police officer
  reasonably suspects that the person apprehended is committing or
  has committed a crime. Second, to proceed from a stop to a frisk
  (patdown for weapons), the officer must reasonably suspect that the
  person stopped is armed and dangerous. For the duration of a traffic
  stop, the Court recently confirmed, a police officer effectively seizes
  “everyone in the vehicle,” the driver and all passengers. Brendlin v.
  California, 551 U. S. 249, 255.
     While patrolling near a Tucson neighborhood associated with the
  Crips gang, police officers serving on Arizona’s gang task force
  stopped an automobile for a vehicular infraction warranting a cita
  tion. At the time of the stop, the officers had no reason to suspect the
  car’s occupants of criminal activity. Officer Trevizo attended to re
  spondent Johnson, the back-seat passenger, whose behavior and
  clothing caused Trevizo to question him. After learning that Johnson
  was from a town with a Crips gang and had been in prison, Trevizo
  asked him get out of the car in order to question him further, out of
  the hearing of the front-seat passenger, about his gang affiliation.
  Because she suspected that he was armed, she patted him down for
  safety when he exited the car. During the patdown, she felt the butt
  of a gun. At that point, Johnson began to struggle, and Trevizo hand
  cuffed him. Johnson was charged with, inter alia, possession of a
  weapon by a prohibited possessor. The trial court denied his motion
  to suppress the evidence, concluding that the stop was lawful and
  that Trevizo had cause to suspect Johnson was armed and dangerous.
2                        ARIZONA v. JOHNSON

                                 Syllabus

    Johnson was convicted. The Arizona Court of Appeals reversed.
    While recognizing that Johnson was lawfully seized, the court found
    that, prior to the frisk, the detention had evolved into a consensual
    conversation about his gang affiliation. Trevizo, the court therefore
    concluded, had no right to pat Johnson down even if she had reason
    to suspect he was armed and dangerous. The Arizona Supreme
    Court denied review.
Held: Officer Trevizo’s patdown of Johnson did not violate the Fourth
 Amendment’s prohibition on unreasonable searches and seizures.
 Pp. 5–9.
    (a) Terry established that, in an investigatory stop based on rea
 sonably grounded suspicion of criminal activity, the police must be
 positioned to act instantly if they have reasonable cause to suspect
 that the persons temporarily detained are armed and dangerous. 392
 U. S., at 24. Because a limited search of outer clothing for weapons
 serves to protect both the officer and the public, a patdown is consti
 tutional. Id., at 23–24, 27, 30–31. Traffic stops, which “resemble, in
 duration and atmosphere, the kind of brief detention authorized in
 Terry,” Berkemer v. McCarty, 468 U. S. 420, 439, n. 29, are “especially
 fraught with danger to police officers,” Michigan v. Long, 463 U. S.
 1032, 1047, who may minimize the risk of harm by exercising “ ‘un
 questioned command of the situation,’ ” Maryland v. Wilson, 519 U. S.
 408, 414. Three decisions cumulatively portray Terry’s application in
 a traffic-stop setting. In Pennsylvania v. Mimms, 434 U. S. 106 (per
 curiam), the Court held that “once a motor vehicle has been lawfully
 detained for a traffic violation, the police officers may order the driver
 to get out of the vehicle without violating the Fourth Amendment,”
 id., at 111, n. 6, because the government’s “legitimate and weighty”
 interest in officer safety outweighs the “de minimis” additional intru
 sion of requiring a driver, already lawfully stopped, to exit the vehi
 cle, id., at 110–111. Citing Terry, the Court further held that a
 driver, once outside the stopped vehicle, may be patted down for
 weapons if the officer reasonably concludes that the driver might be
 armed and dangerous. 434 U. S., at 112. Wilson, 519 U. S., at 413,
 held that the Mimms rule applies to passengers as well as drivers,
 based on “the same weighty interest in officer safety.” Brendlin, 551
 U. S., at 263, held that a passenger is seized, just as the driver is,
 “from the moment [a car stopped by the police comes] to a halt on the
 side of the road.” A passenger’s motivation to use violence during the
 stop to prevent apprehension for a crime more grave than a traffic
 violation is just as great as that of the driver. 519 U. S., at 414. And
 as “the passengers are already stopped by virtue of the stop of the
 vehicle,” id., at 413–414, “the additional intrusion on the passenger is
 minimal,” id., at 415. Pp. 5–7.
                     Cite as: 555 U. S. ____ (2009)                     3

                                Syllabus

     (b) The Arizona Court of Appeals recognized that, initially, Johnson
  was lawfully detained incident to the legitimate stop of the vehicle in
  which he was a passenger, but concluded that once Officer Trevizo
  began questioning him on a matter unrelated to the traffic stop, pat
  down authority ceased to exist, absent reasonable suspicion that
  Johnson had engaged, or was about to engage, in criminal activity.
  The court portrayed the interrogation as consensual, and, Johnson
  emphasizes, Trevizo testified that Johnson could have refused to exit
  the vehicle and to submit to the patdown. But Trevizo also testified
  that she never advised Johnson he did not have to answer her ques
  tions or otherwise cooperate with her. A lawful roadside stop begins
  when a vehicle is pulled over for investigation of a traffic violation.
  The temporary seizure of driver and passengers ordinarily continues,
  and remains reasonable, for the duration of the stop. Normally, the
  stop ends when the police have no further need to control the scene,
  and inform the driver and passengers they are free to leave. An offi
  cer’s inquiries into matters unrelated to the justification for the traf
  fic stop do not convert the encounter into something other than a law
  ful seizure, so long as the inquiries do not measurably extend the
  stop’s duration. See Muehler v. Mena, 544 U. S. 93, 100–101. A rea
  sonable passenger would understand that during the time a car is
  lawfully stopped, he or she is not free to terminate the encounter
  with the police and move about at will. Nothing occurred in this case
  that would have conveyed to Johnson that, prior to the frisk, the traf
  fic stop had ended or that he was otherwise free “to depart without
  police permission.” Brendlin, 551 U. S., at 257. Trevizo was not re
  quired by the Fourth Amendment to give Johnson an opportunity to
  depart without first ensuring that, in so doing, she was not permit
  ting a dangerous person to get behind her. Pp. 7–9.
217 Ariz. 58, 170 P. 3d 667, reversed and remanded.

  GINSBURG, J., delivered the opinion for a unanimous Court.
                        Cite as: 555 U. S. ____ (2009)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 07–1122
                                   _________________


     ARIZONA, PETITIONER v. LEMON MONTREA 

                    JOHNSON 

   ON WRIT OF CERTIORARI TO THE COURT OF APPEALS OF 

                 ARIZONA, DIVISION TWO

                               [January 26, 2009]

  JUSTICE GINSBURG delivered the opinion of the Court.
  This case concerns the authority of police officers to
“stop and frisk” a passenger in a motor vehicle temporarily
seized upon police detection of a traffic infraction. In a
pathmarking decision, Terry v. Ohio, 392 U. S. 1 (1968),
the Court considered whether an investigatory stop (tem
porary detention) and frisk (patdown for weapons) may be
conducted without violating the Fourth Amendment’s ban
on unreasonable searches and seizures. The Court upheld
“stop and frisk” as constitutionally permissible if two
conditions are met. First, the investigatory stop must be
lawful. That requirement is met in an on-the-street en
counter, Terry determined, when the police officer rea
sonably suspects that the person apprehended is commit
ting or has committed a criminal offense. Second, to
proceed from a stop to a frisk, the police officer must rea
sonably suspect that the person stopped is armed and
dangerous.
  For the duration of a traffic stop, we recently confirmed,
a police officer effectively seizes “everyone in the vehicle,”
the driver and all passengers. Brendlin v. California, 551
2                  ARIZONA v. JOHNSON

                    Opinion of the Court

U. S. 249, 255 (2007). Accordingly, we hold that, in a
traffic-stop setting, the first Terry condition—a lawful
investigatory stop—is met whenever it is lawful for police
to detain an automobile and its occupants pending inquiry
into a vehicular violation. The police need not have, in
addition, cause to believe any occupant of the vehicle is
involved in criminal activity. To justify a patdown of the
driver or a passenger during a traffic stop, however, just
as in the case of a pedestrian reasonably suspected of
criminal activity, the police must harbor reasonable suspi
cion that the person subjected to the frisk is armed and
dangerous.
                              I
   On April 19, 2002, Officer Maria Trevizo and Detectives
Machado and Gittings, all members of Arizona’s gang task
force, were on patrol in Tucson near a neighborhood asso
ciated with the Crips gang. At approximately 9 p.m., the
officers pulled over an automobile after a license plate
check revealed that the vehicle’s registration had been
suspended for an insurance-related violation. Under
Arizona law, the violation for which the vehicle was
stopped constituted a civil infraction warranting a cita
tion. At the time of the stop, the vehicle had three occu
pants—the driver, a front-seat passenger, and a passenger
in the back seat, Lemon Montrea Johnson, the respondent
here. In making the stop the officers had no reason to
suspect anyone in the vehicle of criminal activity. See
App. 29–30.
   The three officers left their patrol car and approached
the stopped vehicle. Machado instructed all of the occu
pants to keep their hands visible. Id., at 14. He asked
whether there were any weapons in the vehicle; all re
sponded no. Id., at 15. Machado then directed the driver
to get out of the car. Gittings dealt with the front-seat
passenger, who stayed in the vehicle throughout the stop.
                 Cite as: 555 U. S. ____ (2009)            3

                     Opinion of the Court

See id., at 31. While Machado was getting the driver’s
license and information about the vehicle’s registra
tion and insurance, see id., at 42–43, Trevizo attended to
Johnson.
   Trevizo noticed that, as the police approached, Johnson
looked back and kept his eyes on the officers. Id., at 12.
When she drew near, she observed that Johnson was
wearing clothing, including a blue bandana, that she
considered consistent with Crips membership. Id., at 17.
She also noticed a scanner in Johnson’s jacket pocket,
which “struck [her] as highly unusual and cause [for]
concern,” because “most people” would not carry around a
scanner that way “unless they’re going to be involved in
some kind of criminal activity or [are] going to try to evade
the police by listening to the scanner.” Id., at 16. In
response to Trevizo’s questions, Johnson provided his
name and date of birth but said he had no identification
with him. He volunteered that he was from Eloy, Arizona,
a place Trevizo knew was home to a Crips gang. Johnson
further told Trevizo that he had served time in prison for
burglary and had been out for about a year. 217 Ariz. 58,
60, 170 P. 3d 667, 669 (App. 2007).
   Trevizo wanted to question Johnson away from the
front-seat passenger to gain “intelligence about the gang
[Johnson] might be in.” App. 19. For that reason, she
asked him to get out of the car. Ibid. Johnson complied.
Based on Trevizo’s observations and Johnson’s answers to
her questions while he was still seated in the car, Trevizo
suspected that “he might have a weapon on him.” Id., at
20. When he exited the vehicle, she therefore “patted him
down for officer safety.” Ibid. During the patdown, Tre
vizo felt the butt of a gun near Johnson’s waist. 217 Ariz.,
at 60, 170 P. 3d, at 669. At that point Johnson began to
struggle, and Trevizo placed him in handcuffs. Ibid.
   Johnson was charged in state court with, inter alia,
possession of a weapon by a prohibited possessor. He
4                   ARIZONA v. JOHNSON

                     Opinion of the Court

moved to suppress the evidence as the fruit of an unlawful
search. The trial court denied the motion, concluding that
the stop was lawful and that Trevizo had cause to suspect
Johnson was armed and dangerous. See App. 74–78. A
jury convicted Johnson of the gun-possession charge. See
217 Ariz., at 60–61, 170 P. 3d, at 669–670.
   A divided panel of the Arizona Court of Appeals re
versed Johnson’s conviction. Id., at 59, 170 P. 3d, at 668.
Recognizing that “Johnson was [lawfully] seized when the
officers stopped the car,” id., at 62, 170 P. 3d, at 671, the
court nevertheless concluded that prior to the frisk the
detention had “evolved into a separate, consensual en
counter stemming from an unrelated investigation by
Trevizo of Johnson’s possible gang affiliation,” id., at 64,
170 P. 3d, at 673. Absent “reason to believe Johnson was
involved in criminal activity,” the Arizona appeals court
held, Trevizo “had no right to pat him down for weapons,
even if she had reason to suspect he was armed and dan
gerous.” Ibid.
   Judge Espinosa dissented. He found it “highly unrealis
tic to conclude that merely because [Trevizo] was courte
ous and Johnson cooperative, the ongoing and virtually
simultaneous chain of events [had] somehow ‘evolved into
a consensual encounter’ in the few short moments in
volved.” Id., at 66, 170 P. 3d, at 675. Throughout the
episode, he stressed, Johnson remained “seized as part of
[a] valid traffic stop.” Ibid. Further, he maintained,
Trevizo “had a reasonable basis to consider [Johnson]
dangerous,” id., at 67, 170 P. 3d, at 676, and could there
fore ensure her own safety and that of others at the scene
by patting down Johnson for weapons.
   The Arizona Supreme Court denied review. No. CR–07–
0290–PR, 2007 Ariz. LEXIS 154 (Nov. 29, 2007). We
granted certiorari, 554 U. S. ___ (2008), and now reverse
the judgment of the Arizona Court of Appeals.
                 Cite as: 555 U. S. ____ (2009)            5

                     Opinion of the Court

                               II 

                               A

   We begin our consideration of the constitutionality of
Officer Trevizo’s patdown of Johnson by looking back to
the Court’s leading decision in Terry v. Ohio, 392 U. S. 1
(1968). Terry involved a stop for interrogation of men
whose conduct had attracted the attention of a patrolling
police officer. The officer’s observation led him reasonably
to suspect that the men were casing a jewelry shop in
preparation for a robbery. He conducted a patdown, which
disclosed weapons concealed in the men’s overcoat pockets.
This Court upheld the lower courts’ determinations that
the interrogation was warranted and the patdown, per
missible. See id., at 8.
   Terry established the legitimacy of an investigatory stop
“in situations where [the police] may lack probable cause
for an arrest.” Id., at 24. When the stop is justified by
suspicion (reasonably grounded, but short of probable
cause) that criminal activity is afoot, the Court explained,
the police officer must be positioned to act instantly on
reasonable suspicion that the persons temporarily de
tained are armed and dangerous. Ibid. Recognizing that
a limited search of outer clothing for weapons serves to
protect both the officer and the public, the Court held the
patdown reasonable under the Fourth Amendment. Id., at
23–24, 27, 30–31.
   “[M]ost traffic stops,” this Court has observed, “resem
ble, in duration and atmosphere, the kind of brief deten
tion authorized in Terry.” Berkemer v. McCarty, 468 U. S.
420, 439, n. 29 (1984). Furthermore, the Court has recog
nized that traffic stops are “especially fraught with danger
to police officers.” Michigan v. Long, 463 U. S. 1032, 1047
(1983). “ ‘The risk of harm to both the police and the occu
pants [of a stopped vehicle] is minimized,’ ” we have
stressed, “ ‘if the officers routinely exercise unquestioned
command of the situation.’ ” Maryland v. Wilson, 519 U. S.
6                   ARIZONA v. JOHNSON

                      Opinion of the Court

408, 414 (1997) (quoting Michigan v. Summers, 452 U. S.
692, 702–703 (1981)); see Brendlin, 551 U. S., at 258.
Three decisions cumulatively portray Terry’s application
in a traffic-stop setting: Pennsylvania v. Mimms, 434 U. S.
106 (1977) (per curiam); Maryland v. Wilson, 519 U. S. 408
(1997); and Brendlin v. California, 551 U. S. 249 (2007).
  In Mimms, the Court held that “once a motor vehicle
has been lawfully detained for a traffic violation, the police
officers may order the driver to get out of the vehicle
without violating the Fourth Amendment’s proscription of
unreasonable searches and seizures.” 434 U. S., at 111,
n. 6. The government’s “legitimate and weighty” interest
in officer safety, the Court said, outweighs the “de mini
mis” additional intrusion of requiring a driver, already
lawfully stopped, to exit the vehicle. Id., at 110–111.
Citing Terry as controlling, the Court further held that a
driver, once outside the stopped vehicle, may be patted
down for weapons if the officer reasonably concludes that
the driver “might be armed and presently dangerous.” 434
U. S., at 112.
  Wilson held that the Mimms rule applied to passengers
as well as to drivers. Specifically, the Court instructed
that “an officer making a traffic stop may order passengers
to get out of the car pending completion of the stop.” 519
U. S., at 415. “[T]he same weighty interest in officer
safety,” the Court observed, “is present regardless of
whether the occupant of the stopped car is a driver or
passenger.” Id., at 413.
  It is true, the Court acknowledged, that in a lawful
traffic stop, “[t]here is probable cause to believe that the
driver has committed a minor vehicular offense,” but
“there is no such reason to stop or detain the passengers.”
Ibid. On the other hand, the Court emphasized, the risk
of a violent encounter in a traffic-stop setting “stems not
from the ordinary reaction of a motorist stopped for a
speeding violation, but from the fact that evidence of a
                 Cite as: 555 U. S. ____ (2009)            7

                     Opinion of the Court

more serious crime might be uncovered during the stop.”
Id., at 414. “[T]he motivation of a passenger to employ
violence to prevent apprehension of such a crime,” the
Court stated, “is every bit as great as that of the driver.”
Ibid. Moreover, the Court noted, “as a practical matter,
the passengers are already stopped by virtue of the stop of
the vehicle,” id., at 413–414, so “the additional intrusion
on the passenger is minimal,” id., at 415.
  Completing the picture, Brendlin held that a passenger
is seized, just as the driver is, “from the moment [a car
stopped by the police comes] to a halt on the side of the
road.” 551 U. S., at 263. A passenger therefore has stand
ing to challenge a stop’s constitutionality. Id., at 256–259.
  After Wilson, but before Brendlin, the Court had stated,
in dictum, that officers who conduct “routine traffic
stop[s]” may “perform a ‘patdown’ of a driver and any
passengers upon reasonable suspicion that they may be
armed and dangerous.” Knowles v. Iowa, 525 U. S. 113,
117–118 (1998). That forecast, we now confirm, accurately
captures the combined thrust of the Court’s decisions in
Mimms, Wilson, and Brendlin.
                              B
  The Arizona Court of Appeals recognized that, initially,
Johnson was lawfully detained incident to the legitimate
stop of the vehicle in which he was a passenger. See 217
Ariz., at 64, 170 P. 3d, at 673. But, that court concluded,
once Officer Trevizo undertook to question Johnson on a
matter unrelated to the traffic stop, i.e., Johnson’s gang
affiliation, patdown authority ceased to exist, absent
reasonable suspicion that Johnson had engaged, or was
about to engage, in criminal activity. See id., at 65, 170
P. 3d, at 674. In support of the Arizona court’s portrayal
of Trevizo’s interrogation of Johnson as “consensual,”
Johnson emphasizes Trevizo’s testimony at the suppres
sion hearing. Responding to the prosecutor’s questions,
8                      ARIZONA v. JOHNSON

                         Opinion of the Court

Trevizo affirmed her belief that Johnson could have “re
fused to get out of the car” and “to turn around for the pat
down.” App. 41.
   It is not clear why the prosecutor, in opposing the sup
pression motion, sought to portray the episode as consen
sual. Cf. Florida v. Bostick, 501 U. S. 429 (1991) (holding
that police officers’ search of a bus passenger’s luggage can
be based on consent). In any event, Trevizo also testified
that she never advised Johnson he did not have to answer
her questions or otherwise cooperate with her. See App.
45. And during cross-examination, Trevizo did not dis
agree when defense counsel asked “in fact you weren’t
seeking [Johnson’s] permission . . . ?” Id., at 36. As the
dissenting judge observed, “consensual” is an “unrealistic”
characterization of the Trevizo-Johnson interaction.
“[T]he encounter . . . took place within minutes of the
stop”; the patdown followed “within mere moments” of
Johnson’s exit from the vehicle; beyond genuine debate,
the point at which Johnson could have felt free to leave
had not yet occurred. See 217 Ariz., at 66, 170 P. 3d, at
675.1
   A lawful roadside stop begins when a vehicle is pulled
over for investigation of a traffic violation. The temporary
seizure of driver and passengers ordinarily continues, and
remains reasonable, for the duration of the stop. Nor
mally, the stop ends when the police have no further need
to control the scene, and inform the driver and passengers
they are free to leave. See Brendlin, 551 U. S., at 258. An
officer’s inquiries into matters unrelated to the justifica
tion for the traffic stop, this Court has made plain, do not
——————
  1 The Court of Appeals majority did not assert that Johnson reasona

bly could have felt free to leave. Instead, the court said “a reasonable
person in Johnson’s position would have felt free to remain in the
vehicle.” 217 Ariz. 58, 64, 170 P. 3d 667, 673 (2007). That position,
however, appears at odds with our decision in Maryland v. Wilson, 519
U. S. 408 (1997). See supra, at 6–7.
                   Cite as: 555 U. S. ____ (2009)                  9

                       Opinion of the Court

convert the encounter into something other than a lawful
seizure, so long as those inquiries do not measurably
extend the duration of the stop. See Muehler v. Mena, 544
U. S. 93, 100–101 (2005).
  In sum, as stated in Brendlin, a traffic stop of a car
communicates to a reasonable passenger that he or she is
not free to terminate the encounter with the police and
move about at will. See 551 U. S., at 257. Nothing oc
curred in this case that would have conveyed to Johnson
that, prior to the frisk, the traffic stop had ended or that
he was otherwise free “to depart without police permis
sion.” Ibid. Officer Trevizo surely was not constitution
ally required to give Johnson an opportunity to depart the
scene after he exited the vehicle without first ensuring
that, in so doing, she was not permitting a dangerous
person to get behind her.2
                       *     *    *
  For the reasons stated, the judgment of the Arizona
Court of Appeals is reversed, and the case is remanded for
further proceedings not inconsistent with this opinion.

                                                    It is so ordered.




——————
 2 The  Arizona Court of Appeals assumed, “without deciding, that
Trevizo had reasonable suspicion that Johnson was armed and danger
ous.” 217 Ariz., at 64, 170 P. 3d, at 673. We do not foreclose the
appeals court’s consideration of that issue on remand.

```

---
