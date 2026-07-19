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

## GROUP: content/cases/Minnick v. Mississippi.md  (`case`, 5 assertions)

### content_page

```
---
title: "Minnick v. Mississippi"
type: case
citation: "498 U.S. 146 (1990)"
parallel_cite: "111 S. Ct. 486; 112 L. Ed. 2d 489"
neutral_cite: 1990 U.S. LEXIS 6118
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-12-03
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-12-03
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Minnick v. Mississippi
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112513/minnick-v-mississippi/"
  cluster_id: 112513
  opinion_id: 112513
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Arizona v. Roberson]]", "[[Maryland v. Shatzer]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "edwards", "right-to-counsel", "invocation"]
holding: "Once counsel is invoked, Edwards bars police-initiated re-interrogation without counsel PRESENT — and that protection is not satisfied…"
lake:
  record_id: Minnick v. Mississippi
  status: verified
  projected_at: 2026-07-06
---

# Minnick v. Mississippi

*498 U.S. 146 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After his arrest, Minnick invoked his right to counsel during FBI questioning, and the interview stopped. He then consulted with appointed counsel. Days later, a state officer returned and, without counsel present, questioned him again; Minnick made incriminating statements.

## Issue
Whether the *[[Edwards v. Arizona|Edwards]]* bar on police-initiated interrogation after a request for counsel ends once the suspect has consulted with an attorney.

## Rule
No. "we now hold that when counsel is requested, interrogation must cease, and officials may not reinitiate interrogation without counsel present, whether or not the accused has consulted with his attorney." — 498 U.S. at 153. ^pin-153

## Application
Minnick invoked counsel during the FBI interview, so police could not reinitiate interrogation without counsel present. His intervening consultation with appointed counsel did not lift that protection; the later police-initiated questioning, conducted without counsel present, therefore violated the *[[Edwards v. Arizona|Edwards]]* rule, and his statements were inadmissible.

## Conclusion
Reversed; the statements were obtained in violation of *[[Edwards v. Arizona|Edwards]]* and could not be used.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Minnick* strengthens [[Edwards v. Arizona]] by holding that mere consultation with counsel does not end the bar; [[Maryland v. Shatzer]] later supplied a break-in-custody endpoint to the *[[Edwards v. Arizona|Edwards]]* protection.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Minnick v. Mississippi*, 498 U.S. 146 (1990) — https://www.courtlistener.com/opinion/112513/minnick-v-mississippi/ — pinpoint: 153.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "62df0b8b58d394e2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "498 U.S. 146 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 6118", "official_citation_present": true, "parallel_cite": "111 S. Ct. 486; 112 L. Ed. 2d 489", "title": "Minnick v. Mississippi", "year": "1990"}}
{"assertion_id": "472c738f39c27e19", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Once counsel is invoked, Edwards bars police-initiated re-interrogation without counsel PRESENT — and that protection is not satisfied…", "title": "Minnick v. Mississippi"}}
{"assertion_id": "807e3f3ec3916142", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "Minnick v. Mississippi"}}
{"assertion_id": "8a460562fb19f420", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-12-03", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Minnick v. Mississippi", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Minnick v. Mississippi", "varies_by_point": "false"}}
{"assertion_id": "e31c51adcc557709", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Minnick v. Mississippi"}}
```

### lake record — Minnick v. Mississippi

```json
{
  "schema_version": "s2.v1",
  "record_id": "Minnick v. Mississippi",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Minnick v. Mississippi",
    "case_name_short": "Minnick",
    "case_name_full": "Minnick v. Mississippi",
    "input_case_name": "Minnick v. Mississippi",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-12-03",
    "year": 1990,
    "docket": null,
    "cluster_id": 112513,
    "lead_opinion_id": 112513,
    "sibling_ids": [
      112513,
      9432173,
      9432174
    ],
    "absolute_url": "/opinion/112513/minnick-v-mississippi/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9099703,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9099702,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9099554,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9099553,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      },
      {
        "cluster_id": 9096960,
        "score": 20,
        "case_name": "Minnick v. Mississippi"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "498 U.S. 146",
      "volume": "498",
      "reporter": "U.S.",
      "page": "146",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 486",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 L. Ed. 2d 489",
        "volume": "112",
        "reporter": "L. Ed. 2d",
        "page": "489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 6118",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "6118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "498 U.S. 146",
        "volume": "498",
        "reporter": "U.S.",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 486",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "486",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "112 L. Ed. 2d 489",
        "volume": "112",
        "reporter": "L. Ed. 2d",
        "page": "489",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 6118",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "6118",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "498 U.S. 146",
    "official_selection": {
      "court_class": "scotus",
      "selected": "498 U.S. 146",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-153",
      "page": null,
      "quote": "--- # Minnick v. Mississippi *498 U.S. 146 (1990)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After his arrest, Minnick invoked his right to counsel during FBI questioning, and the interview stopped. He then consulted with appointed counsel. Days later, a state officer returned and, without counsel present, questioned him again; Minnick made incriminating statements. ## Issue Whether the *Edwards* bar on police-initiated interrogation after a request for counsel ends once the suspect has consulted with an attorney. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-12-03",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Minnick v. Mississippi",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. DeJong",
          "cluster_id": 2669581,
          "cite": null,
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
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
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Colby Alan Palmer",
          "cluster_id": 4472471,
          "cite": [
            "791 N.W.2d 840",
            "2010 Iowa Sup. LEXIS 144"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
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
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
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
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Plugh",
          "cluster_id": 2496,
          "cite": [
            "576 F.3d 135",
            "2009 U.S. App. LEXIS 16979",
            "2009 WL 2341966"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Martinez v. State",
          "cluster_id": 1450662,
          "cite": [
            "275 S.W.3d 29",
            "2008 WL 2840151"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Gobert",
          "cluster_id": 1947904,
          "cite": [
            "244 S.W.3d 861",
            "2008 Tex. App. LEXIS 742",
            "2008 WL 269448"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Robert Van Hook v. Carl S. Anderson, Warden",
          "cluster_id": 793987,
          "cite": [
            "444 F.3d 830",
            "2006 U.S. App. LEXIS 9628",
            "2006 WL 997203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "in the Matter of H v.",
          "cluster_id": 2847659,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Gregory Johnson, A/K/A Little Greg, United States of America v. Gregory Johnson, A/K/A Little Greg",
          "cluster_id": 789459,
          "cite": [
            "400 F.3d 187",
            "2005 WL 526889"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 117863,
          "cite": [
            "129 L. Ed. 2d 362",
            "114 S. Ct. 2350",
            "512 U.S. 452",
            "1994 U.S. LEXIS 4827"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNeil v. Wisconsin",
          "cluster_id": 112622,
          "cite": [
            "115 L. Ed. 2d 158",
            "111 S. Ct. 2204",
            "501 U.S. 171",
            "1991 U.S. LEXIS 3483"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dinkins v. State",
          "cluster_id": 1688238,
          "cite": [
            "894 S.W.2d 330",
            "1995 Tex. Crim. App. LEXIS 9",
            "1995 WL 40331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Acevedo",
          "cluster_id": 112608,
          "cite": [
            "114 L. Ed. 2d 619",
            "111 S. Ct. 1982",
            "500 U.S. 565",
            "1991 U.S. LEXIS 3016"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Muniz v. State",
          "cluster_id": 1471480,
          "cite": [
            "851 S.W.2d 238",
            "1993 Tex. Crim. App. LEXIS 5",
            "1993 WL 871"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Waidla",
          "cluster_id": 1316339,
          "cite": [
            "996 P.2d 46",
            "94 Cal. Rptr. 2d 396",
            "22 Cal. 4th 690",
            "22 Cal. 690",
            "2000 Daily Journal DAR 3605",
            "2000 Cal. Daily Op. Serv. 2687",
            "2000 Cal. LEXIS 2229"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Taylor v. State",
          "cluster_id": 1936088,
          "cite": [
            "672 So. 2d 1246",
            "1996 WL 197700"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holland v. State",
          "cluster_id": 1913318,
          "cite": [
            "705 So. 2d 307",
            "1997 WL 562038"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Balfour v. State",
          "cluster_id": 1858937,
          "cite": [
            "598 So. 2d 731",
            "1992 WL 64497"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ladner v. State",
          "cluster_id": 1106169,
          "cite": [
            "584 So. 2d 743",
            "1991 WL 134881"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Martin",
          "cluster_id": 2445914,
          "cite": [
            "5 A.3d 177",
            "607 Pa. 165",
            "2010 Pa. LEXIS 2866"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Simmons v. State",
          "cluster_id": 1652484,
          "cite": [
            "805 So. 2d 452",
            "2001 WL 1587933"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Duplantis v. State",
          "cluster_id": 1659824,
          "cite": [
            "644 So. 2d 1235",
            "1994 WL 590825"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Green",
          "cluster_id": 1730571,
          "cite": [
            "655 So. 2d 272",
            "1995 WL 312446"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. State",
          "cluster_id": 1868949,
          "cite": [
            "684 So. 2d 1213",
            "1996 WL 694199"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Abram v. State",
          "cluster_id": 1096122,
          "cite": [
            "606 So. 2d 1015",
            "1992 WL 223914"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lester v. State",
          "cluster_id": 1136432,
          "cite": [
            "692 So. 2d 755",
            "1997 WL 167015"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Minnick v. Mississippi:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112513 OR 9432173 OR 9432174) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM4OTYwMDAwMDAwJnM9MTY3MDIxMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112513+OR+9432173+OR+9432174%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112513 OR 9432173 OR 9432174)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xODUmcz0xNzQ3MDk5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112513+OR+9432173+OR+9432174%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112513 OR 9432173 OR 9432174)",
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
    "complete_query": "cites:(112513 OR 9432173 OR 9432174)",
    "indexed_citing_opinions": 541,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112513,
        "count": 492,
        "count_source": "search"
      },
      {
        "opinion_id": 9432173,
        "count": 63,
        "count_source": "search"
      },
      {
        "opinion_id": 9432174,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 848,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/minnick-v-mississippi.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc0NDk5MTkmcz0xMDI4MDE1MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112513+OR+9432173+OR+9432174%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112513,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 104710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 107209,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 109659,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 110987,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111288,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111355,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 112127,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 112385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112513,
        "cited_id": 1140464,
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
    "date_created": "2026-07-05T14:06:13Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:06:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:06:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:09:29Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:06:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Minnick v. Mississippi

```
<div>
<center><b><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U.S. 146</a></span> (1990)</b></center>
<center><h1>MINNICK<br>
v.<br>
MISSISSIPPI.</h1></center>
<center>No. 89-6332.</center>
<center><p><b>Supreme Court of the United States.</b></p></center>
<center>Argued October 3, 1990.</center>
<center>Decided December 3, 1990.</center>
CERTIORARI TO THE SUPREME COURT OF MISSISSIPPI.
<p><span class="star-pagination">*147</span> <i>Floyd Abrams</i> argued the cause for petitioner. With him on the briefs were <i>Anthony Paduano</i> and <i>Clive A. Stafford Smith.</i></p>
<p><i>Marvin L. White, Jr.,</i> Assistant Attorney General of Mississippi, argued the cause for respondent. With him on the brief was <i>Mike Moore,</i> Attorney General.<sup>[*]</sup></p>
<p>JUSTICE KENNEDY delivered the opinion of the Court.</p>
<p>To protect the privilege against self-incrimination guaranteed by the Fifth Amendment, we have held that the police must terminate interrogation of an accused in custody if the accused requests the assistance of counsel. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 474</a></span> (1966). We reinforced the protections of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477, 484-485</a></span> (1981), which held that once the accused requests counsel, officials may not reinitiate questioning "until counsel has been made available" to him. The issue in the case before us is whether <i>Edwards'</i> protection ceases once the suspect has consulted with an attorney.</p>
<p><span class="star-pagination">*148</span> Petitioner Robert Minnick and fellow prisoner James Dyess escaped from a county jail in Mississippi and, a day later, broke into a mobile home in search of weapons. In the course of the burglary they were interrupted by the arrival of the trailer's owner, Ellis Thomas, accompanied by Lamar Lafferty and Lafferty's infant son. Dyess and Minnick used the stolen weapons to kill Thomas and the senior Lafferty. Minnick's story is that Dyess murdered one victim and forced Minnick to shoot the other. Before the escapees could get away, two young women arrived at the mobile home. They were held at gunpoint, then bound hand and foot. Dyess and Minnick fled in Thomas' truck, abandoning the vehicle in New Orleans. The fugitives continued to Mexico, where they fought, and Minnick then proceeded alone to California. Minnick was arrested in Lemon Grove, California, on a Mississippi warrant, some four months after the murders.</p>
<p>The confession at issue here resulted from the last interrogation of Minnick while he was held in the San Diego jail, but we first recount the events which preceded it. Minnick was arrested on Friday, August 22, 1986. Petitioner testified that he was mistreated by local police during and after the arrest. The day following the arrest, Saturday, two Federal Bureau of Investigation (FBI) agents came to the jail to interview him. Petitioner testified that he refused to go to the interview, but was told he would "have to go down or else." App. 45. The FBI report indicates that the agents read petitioner his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, and that he acknowledged he understood his rights. He refused to sign a rights waiver form, however, and said he would not answer "very many" questions. Minnick told the agents about the jailbreak and the flight, and described how Dyess threatened and beat him. Early in the interview, he sobbed "[i]t was my life or theirs," but otherwise he hesitated to tell what happened at the trailer. The agents reminded him he did not have to answer questions without a lawyer present. According to the report, "Minnick stated `Come back Monday when I have a lawyer,' <span class="star-pagination">*149</span> and stated that he would make a more complete statement then with his lawyer present." App. 16. The FBI interview ended.</p>
<p>After the FBI interview, an appointed attorney met with petitioner. Petitioner spoke with the lawyer on two or three occasions, though it is not clear from the record whether all of these conferences were in person.</p>
<p>On Monday, August 25, Deputy Sheriff J. C. Denham of Clarke County, Mississippi, came to the San Diego jail to question Minnick. Minnick testified that his jailers again told him he would "have to talk" to Denham and that he "could not refuse." <i>Id.,</i> at 45. Denham advised petitioner of his rights, and petitioner again declined to sign a rights waiver form. Petitioner told Denham about the escape and then proceeded to describe the events at the mobile home. According to petitioner, Dyess jumped out of the mobile home and shot the first of the two victims, once in the back with a shotgun and once in the head with a pistol. Dyess then handed the pistol to petitioner and ordered him to shoot the other victim, holding the shotgun on petitioner until he did so. Petitioner also said that when the two girls arrived, he talked Dyess out of raping or otherwise hurting them.</p>
<p>Minnick was tried for murder in Mississippi. He moved to suppress all statements given to the FBI or other police officers, including Denham. The trial court denied the motion with respect to petitioner's statements to Denham, but suppressed his other statements. Petitioner was convicted on two counts of capital murder and sentenced to death.</p>
<p>On appeal, petitioner argued that the confession to Denham was taken in violation of his rights to counsel under the Fifth and Sixth Amendments. The Mississippi Supreme Court rejected the claims. With respect to the Fifth Amendment aspect of the case, the court found "the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> bright-line rule as to initiation" inapplicable. <span class="citation" data-id="1140464"><a href="/opinion/1140464/minnick-v-state/#83" aria-description="Citation for case: Minnick v. State">551 So. 2d 77, 83</a></span> (1988). Relying on language in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> indicating that the bar on interrogating the accused after a request for counsel <span class="star-pagination">*150</span> applies "`until counsel has been made available to him,'" <i>ibid.,</i> quoting <i>Edwards</i> v. <i>Arizona, supra,</i> at 484-485, the court concluded that "[s]ince counsel was made available to Minnick, his Fifth Amendment right to counsel was satisfied." <span class="citation" data-id="1140464"><a href="/opinion/1140464/minnick-v-state/#83" aria-description="Citation for case: Minnick v. State">551 So. 2d, at 83</a></span>. The court also rejected the Sixth Amendment claim, finding that petitioner waived his Sixth Amendment right to counsel when he spoke with Denham. <span class="citation" data-id="1140464"><a href="/opinion/1140464/minnick-v-state/#83" aria-description="Citation for case: Minnick v. State"><i>Id.,</i> at 83-85</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./495/903/">495 U. S. 903</a></span> (1990), and, without reaching any Sixth Amendment implications in the case, we decide that the Fifth Amendment protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> is not terminated or suspended by consultation with counsel.</p>
<p>In <i>Miranda</i> v. <i>Arizona, supra,</i> at 474, we indicated that once an individual in custody invokes his right to counsel, interrogation "must cease until an attorney is present"; at that point, "the individual must have an opportunity to confer with the attorney and to have him present during any subsequent questioning." <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> gave force to these admonitions, finding it "inconsistent with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and its progeny for the authorities, at their instance, to reinterrogate an accused in custody if he has clearly asserted his right to counsel." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#485" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 485</a></span>. We held that "when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><i>Id.,</i> at 484</a></span>. Further, an accused who requests an attorney, "having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><i>Id.,</i> at 484-485</a></span>.</p>
<p><i>Edwards</i> is "designed to prevent police from badgering a defendant into waiving his previously asserted <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights." <i>Michigan</i> v. <i>Harvey,</i> <span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990). <span class="star-pagination">*151</span> See also <i>Smith v. Illinois,</i> <span class="citation" data-id="9429796"><a href="/opinion/111288/smith-v-illinois/#98" aria-description="Citation for case: Smith v. Illinois">469 U. S. 91, 98</a></span> (1984). The rule ensures that any statement made in subsequent interrogation is not the result of coercive pressures. <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> conserves judicial resources which would otherwise be expended in making difficult determinations of voluntariness, and implements the protections of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in practical and straightforward terms.</p>
<p>The merit of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> decision lies in the clarity of its command and the certainty of its application. We have confirmed that the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule provides "`clear and unequivocal' guidelines to the law enforcement profession." <i>Arizona v. Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#682" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675, 682</a></span> (1988). Cf. <i>Moran v. Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#425" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 425-426</a></span> (1986). Even before <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> we noted that <i>Miranda's</i> "relatively rigid requirement that interrogation must cease upon the accused's request for an attorney . . . has the virtue of informing police and prosecutors with specificity as to what they may do in conducting custodial interrogation, and of informing courts under what circumstances statements obtained during such interrogation are not admissible. This gain in specificity, which benefits the accused and the State alike, has been thought to outweigh the burdens that the decision in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> imposes on law enforcement agencies and the courts by requiring the suppression of trustworthy and highly probative evidence even though the confession might be voluntary under traditional Fifth Amendment analysis." <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979). This pre-<span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona"><i>Edwards</i></a></span> explanation applies as well to <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and its progeny. <i>Arizona</i> v. <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#681" aria-description="Citation for case: Arizona v. Roberson"><i>Roberson, supra,</i> at 681-682</a></span>.</p>
<p>The Mississippi Supreme Court relied on our statement in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> that an accused who invokes his right to counsel "is not subject to further interrogation by the authorities until counsel has been made available to him . . . ." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span>. We do not interpret this language to mean, as the Mississippi court thought, that the protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> terminates once counsel has consulted with the suspect. In <span class="star-pagination">*152</span> context, the requirement that counsel be "made available" to the accused refers to more than an opportunity to consult with an attorney outside the interrogation room.</p>
<p>In <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> we focused on <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s instruction that when the accused invokes his right to counsel, "the interrogation must cease until an attorney is <i>present,"</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span> (emphasis added), agreeing with Edwards' contention that he had not waived his right "to have counsel <i>present</i> during custodial interrogation." <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#482" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 482</a></span> (emphasis added). In the sentence preceding the language quoted by the Mississippi Supreme Court, we referred to the "right to have counsel <i>present</i> during custodial interrogation," and in the sentence following, we again quoted the phrase "`interrogation must cease until an attorney is <i>present'"</i> from <i>Miranda.</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484-485</a></span> (emphasis added). The full sentence relied on by the Mississippi Supreme Court, moreover, says: "We further hold that an accused, such as Edwards, <i>having expressed his desire to deal with the police only through counsel,</i> is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police." <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Ibid.</a></span></i> (emphasis added).</p>
<p>Our emphasis on counsel's <i>presence</i> at interrogation is not unique to <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</i> It derives from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> where we said that in the cases before us "[t]he presence of counsel . . . would be the adequate protective device necessary to make the process of police interrogation conform to the dictates of the [Fifth Amendment] privilege. His presence would insure that statements made in the government-established atmosphere are not the product of compulsion." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#466" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 466</a></span>. See <i>Fare</i> v. <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#719" aria-description="Citation for case: Fare v. Michael C."><i>Michael C., supra,</i> at 719</a></span>. Our cases following <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> have interpreted the decision to mean that the authorities may not initiate questioning of the accused in counsel's absence. Writing for a plurality of the Court, for instance, then-JUSTICE REHNQUIST described the holding of <span class="star-pagination">*153</span> <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> to be "that subsequent incriminating statements made <i>without [Edwards'] attorney present</i> violated the rights secured to the defendant by the Fifth and Fourteenth Amendments to the United States Constitution." <i>Oregon v. Bradshaw,</i> <span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/#1043" aria-description="Citation for case: Oregon v. Bradshaw">462 U. S. 1039, 1043</a></span> (1983) (emphasis added). See also <i>Arizona</i> v. <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#680" aria-description="Citation for case: Arizona v. Roberson"><i>Roberson, supra,</i> at 680</a></span> ("The rule of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> case came as a corollary to <i>Miranda's</i> admonition that `[i]f the individual states that he wants an attorney, the interrogation must cease until an attorney is present"); <i>Shea v. Louisiana,</i> <span class="citation" data-id="9429912"><a href="/opinion/111355/shea-v-louisiana/#52" aria-description="Citation for case: Shea v. Louisiana">470 U. S. 51, 52</a></span> (1985) ("In <i>Edwards</i> v. <i>Arizona</i><i>,</i>. . . this Court ruled that a criminal defendant's rights under the Fifth and Fourteenth Amendments were violated by the use of his confession obtained by police-instigated interrogationwithout counsel presentafter he requested an attorney"). These descriptions of <i>Edwards'</i> holding are consistent with our statement that "[p]reserving the integrity of an accused's choice to communicate with police only through counsel is the essence of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and its progeny." <i>Patterson v. Illinois,</i> <span class="citation" data-id="9431404"><a href="/opinion/112127/patterson-v-illinois/#291" aria-description="Citation for case: Patterson v. Illinois">487 U. S. 285, 291</a></span> (1988). In our view, a fair reading of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and subsequent cases demonstrates that we have interpreted the rule to bar police-initiated interrogation unless the accused has counsel with him at the time of questioning. Whatever the ambiguities of our earlier cases on this point, we now hold that when counsel is requested, interrogation must cease, and officials may not reinitiate interrogation without counsel present, whether or not the accused has consulted with his attorney.</p>
<p>We consider our ruling to be an appropriate and necessary application of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule. A single consultation with an attorney does not remove the suspect from persistent attempts by officials to persuade him to waive his rights, or from the coercive pressures that accompany custody and that may increase as custody is prolonged. The case before us well illustrates the pressures, and abuses, that may be concomitants of custody. Petitioner testified that though he resisted, he was required to submit to both the FBI and the <span class="star-pagination">*154</span> Denham interviews. In the latter instance, the compulsion to submit to interrogation followed petitioner's unequivocal request during the FBI interview that questioning cease until counsel was present. The case illustrates also that consultation is not always effective in instructing the suspect of his rights. One plausible interpretation of the record is that petitioner thought he could keep his admissions out of evidence by refusing to sign a formal waiver of rights. If the authorities had complied with Minnick's request to have counsel present during interrogation, the attorney could have corrected Minnick's misunderstanding, or indeed counseled him that he need not make a statement at all. We decline to remove protection from police-initiated questioning based on isolated consultations with counsel who is absent when the interrogation resumes.</p>
<p>The exception to <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> here proposed is inconsistent with <i>Edwards'</i> purpose to protect the suspect's right to have counsel present at custodial interrogation. It is inconsistent as well with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> where we specifically rejected respondent's theory that the opportunity to consult with one's attorney would substantially counteract the compulsion created by custodial interrogation. We noted in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> that "[e]ven preliminary advice given to the accused by his own attorney can be swiftly overcome by the secret interrogation process. Thus the need for counsel to protect the Fifth Amendment privilege comprehends not merely a right to consult with counsel prior to questioning, but also to have counsel present during any questioning if the defendant so desires." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#470" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 470</a></span> (citation omitted).</p>
<p>The exception proposed, furthermore, would undermine the advantages flowing from <i>Edwards'</i> "clear and unequivocal" character. Respondent concedes that even after consultation with counsel, a second request for counsel should reinstate the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> protection. We are invited by this formulation to adopt a regime in which <i>Edwards'</i> protection could pass in and out of existence multiple times prior to arraignment, <span class="star-pagination">*155</span> at which point the same protection might reattach by virtue of our Sixth Amendment jurisprudence, see <i>Michigan v. Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986). Vagaries of this sort spread confusion through the justice system and lead to a consequent loss of respect for the underlying constitutional principle.</p>
<p>In addition, adopting the rule proposed would leave far from certain the sort of consultation required to displace <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</i> Consultation is not a precise concept, for it may encompass variations from a telephone call to say that the attorney is en route, to a hurried interchange between the attorney and client in a detention facility corridor, to a lengthy in-person conference in which the attorney gives full and adequate advice respecting all matters that might be covered in further interrogations. And even with the necessary scope of consultation settled, the officials in charge of the case would have to confirm the occurrence and, possibly, the extent of consultation to determine whether further interrogation is permissible. The necessary inquiries could interfere with the attorney-client privilege.</p>
<p>Added to these difficulties in definition and application of the proposed rule is our concern over its consequence that the suspect whose counsel is prompt would lose the protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> while the one whose counsel is dilatory would not. There is more than irony to this result. There is a strong possibility that it would distort the proper conception of the attorney's duty to the client and set us on a course at odds with what ought to be effective representation.</p>
<p>Both waiver of rights and admission of guilt are consistent with the affirmation of individual responsibility that is a principle of the criminal justice system. It does not detract from this principle, however, to insist that neither admissions nor waivers are effective unless there are both particular and systemic assurances that the coercive pressures of custody were not the inducing cause. The <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule sets forth a specific standard to fulfill these purposes, and we have declined <span class="star-pagination">*156</span> to confine it in other instances. See <i>Arizona v. Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988). It would detract from the efficacy of the rule to remove its protections based on consultation with counsel.</p>
<p><i>Edwards</i> does not foreclose finding a waiver of Fifth Amendment protections after counsel has been requested, provided the accused has initiated the conversation or discussions with the authorities; but that is not the case before us. There can be no doubt that the interrogation in question was initiated by the police; it was a formal interview which petitioner was compelled to attend. Since petitioner made a specific request for counsel before the interview, the police-initiated interrogation was impermissible. Petitioner's statement to Denham was not admissible at trial.</p>
<p>The judgment is reversed, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE SOUTER took no part in the consideration or decision of this case.</p>
<p>JUSTICE SCALIA, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>The Court today establishes an irrebuttable presumption that a criminal suspect, after invoking his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel, can <i>never</i> validly waive that right during any police-initiated encounter, even after the suspect has been provided multiple <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and has actually consulted his attorney. This holding builds on foundations already established in <i>Edwards</i> v. <i>Arizona,</i> <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), but "the rule of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> is our rule, not a constitutional command; and it is our obligation to justify its expansion." <i>Arizona v. Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#688" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675, 688</a></span> (1988) (KENNEDY, J., dissenting). Because I see no justification for applying the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> irrebuttable presumption when a criminal suspect has actually consulted with his attorney, I respectfully dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*157</span> I</h2>
<p>Some recapitulation of pertinent facts is in order, given the Court's contention that "[t]he case before us well illustrates the pressures, and abuses, that may be concomitants of custody." <i>Ante,</i> at 153. It is undisputed that the FBI agents who first interviewed Minnick on Saturday, August 23, 1986, advised him of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights before any questioning began. Although he refused to sign a waiver form, he agreed to talk to the agents, and described his escape from prison in Mississippi and the ensuing events. When he came to what happened at the trailer, however, Minnick hesitated. The FBI agents then reminded him that he did not have to answer questions without a lawyer present. Minnick indicated that he would finish his account on Monday, when he had a lawyer, and the FBI agents terminated the interview forthwith.</p>
<p>Minnick was then provided with an attorney, with whom he consulted several times over the weekend. As Minnick testified at a subsequent suppression hearing:</p>
<blockquote>"I talked to [my attorney] two different times andit might have been three different times . . . . He told me that first day that he was my lawyer and that he was appointed to me and to not to talk to nobody and not tell nobody nothing and to not sign no waivers and not sign no extradition papers or sign anything and that he was going to get a court order to have any of the policeI advised him of the FBI talking to me and he advised me not to tell anybody anything that he was going to get a court order drawn up to restrict anybody talking to me outside of the San Diego Police Department." App. 46-47.</blockquote>
<p>On Monday morning, Minnick was interviewed by Deputy Sheriff J. C. Denham, who had come to San Diego from Mississippi. Before the interview, Denham reminded Minnick of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Minnick again refused to sign a <span class="star-pagination">*158</span> waiver form, but he did talk with Denham and did not ask for his attorney. As Minnick recalled at the hearing, he and Denham</p>
<blockquote>"went through several different conversations about first, about how everybody was back in the county jail and what everybody was doing, had he heard from Mama and had he went and talked to Mama and had he seen my brother, Tracy, and several different other questions pertaining to such things as that. And, we went off into how the escape went down at the county jail . . . ." App. 50.</blockquote>
<p>Minnick then proceeded to describe his participation in the double murder at the trailer.</p>
<p>Minnick was later extradited and tried for murder in Mississippi. Before trial, he moved to suppress the statements he had given the FBI agents and Denham in the San Diego jail. The trial court granted the motion with respect to the statements made to the FBI agents, but ordered a hearing on the admissibility of the statements made to Denham. After receiving testimony from both Minnick and Denham, the court concluded that Minnick's confession had been "freely and voluntarily given from the evidence beyond a reasonable doubt," <i>id.,</i> at 25, and allowed Denham to describe Minnick's confession to the jury.</p>
<p>The Court today reverses the trial court's conclusion. It holds that, because Minnick had asked for counsel during the interview with the FBI agents, he could notas a matter of lawvalidly waive the right to have counsel present during the conversation initiated by Denham. That Minnick's original request to see an attorney had been honored, that Minnick had consulted with his attorney on several occasions, and that the attorney had specifically warned Minnick not to speak to the authorities, are irrelevant. That Minnick was familiar with the criminal justice system in general or <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in particular (he had previously been convicted of robbery in Mississippi and assault with a deadly <span class="star-pagination">*159</span> weapon in California) is also beside the point. The confession must be suppressed, not because it was "compelled," nor even because it was obtained from an individual who could realistically be assumed to be unaware of his rights, but simply because this Court sees fit to prescribe as a "systemic assuranc[e]," <i>ante,</i> at 155, that a person in custody who has once asked for counsel cannot thereafter be approached by the police unless counsel is present. Of course the Constitution's proscription of compelled testimony does not remotely authorize this incursion upon state practices; and even our recent precedents are not a valid excuse.</p>
<p></p>
<h2>II</h2>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), this Court declared that a criminal suspect has a right to have counsel present during custodial interrogation, as a prophylactic assurance that the "inherently compelling pressures," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span>, of such interrogation will not violate the Fifth Amendment. But <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> did not hold that these "inherently compelling pressures" precluded a suspect from waiving his right to have counsel present. On the contrary, the opinion recognized that a State could establish that the suspect "knowingly and intelligently waived . . . his right to retained or appointed counsel." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 475</a></span>. For this purpose, the Court expressly adopted the "high standar[d] of proof for the waiver of constitutional rights," <i>ibid.,</i> set forth in <i>Johnson</i> v. <i>Zerbst,</i> <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458</a></span> (1938).</p>
<p>The <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> waiver standard, and the means of applying it, are familiar: Waiver is "an intentional relinquishment or abandonment of a known right or privilege," <span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst"><i>id.,</i> at 464</a></span>; and whether such a relinquishment or abandonment has occurred depends "in each case, upon the particular facts and circumstances surrounding that case, including the background, experience, and conduct of the accused," <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">ibid.</a></span></i> We have applied the <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> approach in many contexts where a State bears the burden of showing a waiver of constitutional criminal <span class="star-pagination">*160</span> procedural rights. See, <i>e. g., </i><i>Faretta</i> v. <i>California,</i> <span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#835" aria-description="Citation for case: Faretta v. California">422 U. S. 806, 835</a></span> (1975) (right to the assistance of counsel at trial); <i>Brookhart</i> v. <i>Janis,</i> <span class="citation" data-id="107209"><a href="/opinion/107209/brookhart-v-janis/#4" aria-description="Citation for case: Brookhart v. Janis">384 U. S. 1, 4</a></span> (1966) (right to confront adverse witnesses); <i>Adams</i> v. <i>United States ex rel. McCann,</i> <span class="citation" data-id="9419274"><a href="/opinion/103735/adams-v-united-states-ex-rel-mccann/#275" aria-description="Citation for case: Adams v. United States Ex Rel. McCann">317 U. S. 269, 275-280</a></span> (1942) (right to trial by jury).</p>
<p>Notwithstanding our acknowledgment that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights are "not themselves rights protected by the Constitution but. . . instead measures to insure that the right against compulsory self-incrimination [is] protected," <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974), we have adhered to the principle that nothing less than the <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> standard for the waiver of constitutional rights applies to the waiver of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Until <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> however, we refrained from imposing on the States a <i>higher</i> standard for the waiver of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. For example, in <i>Michigan</i> v. <i>Mosley,</i> <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96</a></span> (1975), we rejected a proposed irrebuttable presumption that a criminal suspect, after invoking the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to remain silent, could not validly waive the right during any subsequent questioning by the police. In <i>North Carolina</i> v. <i>Butler,</i> <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369</a></span> (1979), we rejected a proposed rule that waivers of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights must be deemed involuntary absent an explicit assertion of waiver by the suspect. And in <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#723" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 723-727</a></span> (1979), we declined to hold that waivers of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights by juveniles are <i>per se</i> involuntary.</p>
<p><i>Edwards,</i> however, broke with this approach, holding that a defendant's waiver of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel, made in the course of a police-initiated encounter after he had requested counsel but before counsel had been provided, was <i>per se</i> involuntary. The case stands as a solitary exception to our waiver jurisprudence. It does, to be sure, have the desirable consequences described in today's opinion. In the narrow context in which it applies, it provides 100% assurance against confessions that are "the result of coercive pressures," <i>ante,</i> at 151; it "`prevent[s] police from badgering a <span class="star-pagination">*161</span> defendant,'" <i>ante,</i> at 150 (quoting <i>Michigan</i> v. <i>Harvey,</i> <span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990)); it "conserves judicial resources which would otherwise be expended in making difficult determinations of voluntariness," <i>ante,</i> at 151; and it provides "`"clear and unequivocal" guidelines to the law enforcement profession,'" <i><span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/" aria-description="Citation for case: Michigan v. Harvey">ibid.</a></span></i> (quoting <i>Arizona</i> v. <i>Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#682" aria-description="Citation for case: Arizona v. Roberson">486 U. S., at 682</a></span>). But so would a rule that simply excludes all confessions by all persons in police custody. The value of any prophylactic rule (assuming the authority to adopt a prophylactic rule) must be assessed not only on the basis of what is gained, but also on the basis of what is lost. In all other contexts we have thought the above-described consequences of abandoning <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> outweighed by "`the need for police questioning as a tool for effective enforcement of criminal laws,'" <i>Moran v. Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 426</a></span> (1986). "Admissions of guilt," we have said, "are more than merely `desirable'; they are essential to society's compelling interest in finding, convicting, and punishing those who violate the law." <i><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">Ibid.</a></span></i> (citation omitted).</p>
<p></p>
<h2>III</h2>
<p>In this case, of course, we have not been called upon to reconsider <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> but simply to determine whether its irrebuttable presumption should continue after a suspect has actually consulted with his attorney. Whatever justifications might support <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> are even less convincing in this context.</p>
<p>Most of the Court's discussion of <i>Edwardswhich</i> stresses repeatedly, in various formulations, the case's emphasis upon the "right `to have counsel <i>present</i> during custodial interrogation,'" <i>ante,</i> at 152, quoting <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#482" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 482</a></span> (emphasis added by the Court)is beside the point. The existence and the importance of the <i>Miranda-created</i> right "to have counsel <i>present"</i> are unquestioned here. What <i>is</i> questioned is why a State should not be given the opportunity to prove (under <i>Zerbst)</i> that the right was <i>voluntarily waived</i> by a suspect who, after having been read his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights twice and <span class="star-pagination">*162</span> having consulted with counsel at least twice, chose to speak to a police officer (and to admit his involvement in two murders) without counsel present.</p>
<p><i>Edwards</i> did not assert the principle that no waiver of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right "to have counsel <i>present"</i> is possible. It simply adopted the presumption that no waiver is <i>voluntary</i> in certain circumstances, and the issue before us today is how broadly those circumstances are to be defined. They should not, in my view, extend beyond the circumstances present in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> itselfwhere the suspect in custody asked to consult an attorney and was interrogated before that attorney had ever been provided. In those circumstances, the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule rests upon an assumption similar to that of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> itself: that when a suspect in police custody is first questioned he is likely to be ignorant of his rights and to feel isolated in a hostile environment. This likelihood is thought to justify special protection against unknowing or coerced waiver of rights. After a suspect has seen his request for an attorney honored, however, and has actually spoken with that attorney, the probabilities change. The suspect then knows that he has an advocate on his side, and that the police will permit him to consult that advocate. He almost certainly also has a heightened awareness (above what the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning itself will provide) of his right to remain silentsince at the earliest opportunity "any lawyer worth his salt will tell the suspect in no uncertain terms to make no statement to the police under any circumstances." <i>Watts v. Indiana,</i> <span class="citation" data-id="9420379"><a href="/opinion/104710/watts-v-indiana/#59" aria-description="Citation for case: Watts v. Indiana">338 U. S. 49, 59</a></span> (1949) (opinion of Jackson, J.).</p>
<p>Under these circumstances, an irrebuttable presumption that any police-prompted confession is the result of ignorance of rights, or of coercion, has no genuine basis in fact. After the first consultation, therefore, the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> exclusionary rule should cease to apply. Does this mean, as the Court implies, that the police will thereafter have license to "badger" the suspect? Only if all one means by "badger" is asking, without such insistence or frequency as would constitute coercion, <span class="star-pagination">*163</span> whether he would like to reconsider his decision not to confess. Nothing in the Constitution (the only basis for our intervention here) prohibits such inquiry, which may often produce the desirable result of a voluntary confession. If and when postconsultation police inquiry becomes so protracted or threatening as to constitute coercion, the <i><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst">Zerbst</a></span></i> standard will afford the needed protection.</p>
<p>One should not underestimate the extent to which the Court's expansion of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> constricts law enforcement. Today's ruling, that the invocation of a right to counsel permanently prevents a police-initiated waiver, makes it largely impossible for the police to urge a prisoner who has initially declined to confess to change his mindor indeed, even to ask whether he has changed his mind. Many persons in custody will invoke the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel during the first interrogation, so that the permanent prohibition will attach at once. Those who do not do so will almost certainly request or obtain counsel at arraignment. We have held that a general request for counsel, after the Sixth Amendment right has attached, also triggers the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> prohibition of police-solicited confessions, see <i>Michigan</i> v. <i>Jackson,</i> <span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), and I presume that the perpetuality of prohibition announced in today's opinion applies in that context as well. "Perpetuality" is not too strong a term, since, although the Court rejects one logical moment at which the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> presumption might end, it suggests no alternative. In this case Minnick was reapproached by the police three days after he requested counsel, but the result would presumably be the same if it had been three months, or three years, or even three decades. This perpetual irrebuttable presumption will apply, I might add, not merely to interrogations involving the original crime, but to those involving other subjects as well. See <i>Arizona</i> v. <i>Roberson,</i> <span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988).</p>
<p>Besides repeating the uncontroverted proposition that the suspect has a "right to have counsel <i>present,"</i> the Court stresses the clarity and simplicity that are achieved by today's <span class="star-pagination">*164</span> holding. Clear and simple rules are desirable, but only in pursuance of authority that we possess. We are authorized by the Fifth Amendment to exclude confessions that are "compelled," which we have interpreted to include confessions that the police obtain from a suspect in custody without a knowing and voluntary waiver of his right to remain silent. Undoubtedly some bright-line rules can be adopted to implement that principle, marking out the situations in which knowledge or voluntariness cannot possibly be established for example, a rule excluding confessions obtained after five hours of continuous interrogation. But a rule excluding all confessions that follow upon even the slightest police inquiry cannot conceivably be justified on this basis. It does not rest upon a reasonable prediction that all such confessions, or even most such confessions, will be unaccompanied by a knowing and voluntary waiver.</p>
<p>It can be argued that the same is true of the category of confessions excluded by the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule itself. I think that is so, but, as I have discussed above, the presumption of involuntariness is at least more plausible for that category. There is, in any event, a clear and rational line between that category and the present one, and I see nothing to be said for expanding upon a past mistake. Drawing a distinction between police-initiated inquiry before consultation with counsel and police-initiated inquiry after consultation with counsel is assuredly more reasonable than other distinctions <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> has already led us intosuch as the distinction between police-initiated inquiry after assertion of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to remain silent, and police-initiated inquiry after assertion of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to counsel, see Kamisar, The <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> and <i><span class="citation" data-id="9429286"><a href="/opinion/110987/oregon-v-bradshaw/" aria-description="Citation for case: Oregon v. Bradshaw">Bradshaw</a></span></i> Cases: The Court Giveth and the Court Taketh Away, in 5 The Supreme Court: Trends and Developments 153, 157 (J. Choper, Y. Kamisar, &amp; L. Tribe eds. 1984) ("[E]ither <i><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">Mosley</a></span></i> was wrongly decided or <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> was"); or the distinction between what is needed to prove waiver of the <span class="star-pagination">*165</span> <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> right to have counsel present and what is needed to prove waiver of rights found in the Constitution.</p>
<p>The rest of the Court's arguments can be answered briefly. The suggestion that it will either be impossible or ethically impermissible to determine whether a "consultation" between the suspect and his attorney has occurred is alarmist. Since, as I have described above, the main purpose of the consultation requirement is to eliminate the suspect's feeling of isolation and to assure him the presence of legal assistance, any discussion between him and an attorney whom he asks to contact, or who is provided to him, in connection with his arrest, will suffice. The precise content of the discussion is irrelevant.</p>
<p>As for the "irony" that "the suspect whose counsel is prompt would lose the protection of <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>,</i> while the one whose counsel is dilatory would not," <i>ante,</i> at 155: There seems to me no irony in applying a special protection only when it is needed. The <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> rule is premised on an (already tenuous) assumption about the suspect's psychological state, and when the event of consultation renders that assumption invalid the rule should no longer apply. One searching for ironies in the state of our law should consider, first, the irony created by <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> itself: The suspect in custody who says categorically "I do not wish to discuss this matter" can be asked to change his mind; but if he should say, more tentatively, "I do not think I should discuss this matter without my attorney present" he can no longer be approached. To that there is added, by today's decision, the irony that it will be far harder for the State to establish a knowing and voluntary waiver of Fifth Amendment rights by a prisoner who has already consulted with counsel than by a newly arrested suspect.</p>
<p>Finally, the Court's concern that <i>"Edwards'</i> protection could pass in and out of existence multiple times," <i>ante,</i> at 154, does not apply to the resolution of the matter I have proposed. <span class="star-pagination">*166</span> <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> would cease to apply, permanently, once consultation with counsel has occurred.</p>
<p></p>
<h2>* * *</h2>
<p>Today's extension of the <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> prohibition is the latest stage of prophylaxis built upon prophylaxis, producing a veritable fairyland castle of imagined constitutional restriction upon law enforcement. This newest tower, according to the Court, is needed to avoid "inconsisten[cy] with [the] purpose" of <i>Edwards'</i> prophylactic rule, <i>ante,</i> at 154, which was needed to protect <i>Miranda's</i> prophylactic right to have counsel present, which was needed to protect the right against <i>compelled self-incrimination</i> found (at last!) in the Constitution.</p>
<p>It seems obvious to me that, even in <i><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span></i> itself but surely in today's decision, we have gone far beyond any genuine concern about suspects who do not <i>know</i> their right to remain silent, or who have been <i>coerced</i> to abandon it. Both holdings are explicable, in my view, only as an effort to protect suspects against what is regarded as their own folly. The sharp-witted criminal would know better than to confess; why should the dull-witted suffer for his lack of mental endowment? Providing him an attorney at every stage where he might be induced or persuaded (though not coerced) to incriminate himself will even the odds. Apart from the fact that this protective enterprise is beyond our authority under the Fifth Amendment or any other provision of the Constitution, it is unwise. The procedural protections of the Constitution protect the guilty as well as the innocent, but it is not their objective to set the guilty free. That some clever criminals may employ those protections to their advantage is poor reason to allow criminals who have not done so to escape justice.</p>
<p>Thus, even if I were to concede that an honest confession is a foolish mistake, I would welcome rather than reject it; a rule that foolish mistakes do not count would leave most offenders <span class="star-pagination">*167</span> not only unconvicted but undetected. More fundamentally, however, it is wrong, and subtly corrosive of our criminal justice system, to regard an honest confession as a "mistake." While every person is entitled to stand silent, it is more virtuous for the wrongdoer to admit his offense and accept the punishment he deserves. Not only for society, but for the wrongdoer himself, "admissio[n] of guilt . . . , if not coerced, [is] inherently desirable," <i>United States v. Washington,</i> <span class="citation" data-id="9005791"><a href="/opinion/9012827/united-states-v-washington/#187" aria-description="Citation for case: United States v. Washington">431 U. S. 181, 187</a></span> (1977), because it advances the goals of both "justice <i>and</i> rehabilitation," <i>Michigan v. Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#448" aria-description="Citation for case: Michigan v. Tucker">417 U. S., at 448, n. 23</a></span> (emphasis added). A confession is rightly regarded by the Sentencing Guidelines as warranting a reduction of sentence, because it "demonstrates a recognition and affirmative acceptance of personal responsibility for . . . criminal conduct," U. S. Sentencing Commission, Guidelines Manual § 3E1.1 (1988), which is the beginning of reform. We should, then, rejoice at an honest confession, rather than pity the "poor fool" who has made it; and we should regret the attempted retraction of that good act, rather than seek to facilitate and encourage it. To design our laws on premises contrary to these is to abandon belief in either personal responsibility or the moral claim of just government to obedience. Cf. Caplan, Questioning <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> <span class="citation no-link">38 Vand. L. Rev. 1417</span>, 1471-1473 (1985). Today's decision is misguided, it seems to me, in so readily exchanging, for marginal, super-<span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/" aria-description="Citation for case: Johnson v. Zerbst"><i>Zerbst</i></a></span> protection against genuinely compelled testimony, investigators' ability to urge, or even ask, a person in custody to do what is right.</p>
<h2>NOTES</h2>
<p>[*]  <i>David W. DeBruin</i> and <i>Donald B. Verrilli, Jr.,</i> filed a brief for the Mississippi State Bar as <i>amicus curiae</i> urging reversal.
</p>
<p><i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Nina Goodman</i> filed a brief for the United States as <i>amicus curiae</i> urging affirmance.</p>

</div>
```

---

## GROUP: content/cases/Missouri v. McNeely.md  (`case`, 6 assertions)

### content_page

```
---
title: "Missouri v. McNeely"
type: case
citation: ""
parallel_cite: "133 S. Ct. 1552; 185 L. Ed. 2d 696; 569 U.S. 141; 81 U.S.L.W. 4250; 24 Fla. L. Weekly Fed. S 150"
neutral_cite: "2013 U.S. LEXIS 3160; 2013 WL 1628934"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2013
date_decided: 2013-04-17
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2013-04-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Missouri v. McNeely
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/858288/missouri-v-mcneely/"
  cluster_id: 858288
  opinion_id: 858288
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — Progeny / Refinement"
  - page: "[[SIA Alcohol Tests]]"
    role: "Related (cross-doctrine)"
related: ["[[Schmerber v. California]]", "[[Mitchell v. Wisconsin]]", "[[Birchfield v. North Dakota]]"]
aliases: []
tags: ["case", "fourth-amendment", "exigent-circumstances", "blood-draw", "dui", "warrant"]
holding: "The natural metabolization of alcohol is NOT a per se exigency justifying a warrantless DUI blood draw in every case; exigency must be…"
lake:
  record_id: Missouri v. McNeely
  status: verified
  projected_at: 2026-07-06
---

# Missouri v. McNeely

*569 U.S. 141 (2013)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
McNeely was stopped for speeding, showed signs of intoxication, and refused a breath test. Without seeking a warrant, the officer took him to a hospital and directed a blood draw over his objection. Missouri defended the warrantless draw on the theory that the body's natural elimination of alcohol always creates an [[Exigent Circumstances and Hot Pursuit|exigency]].

## Issue
Whether the natural metabolization of alcohol in the bloodstream categorically creates an [[Exigent Circumstances and Hot Pursuit|exigency]] that justifies a warrantless blood draw in every drunk-driving case.

## Rule
No. "We hold that in drunk-driving investigations, the natural dissipation of alcohol in the bloodstream does not constitute an exigency in every case sufficient to justify conducting a blood test without a warrant." — 569 U.S. at 156. ^pin-156

Whether a warrantless blood draw is justified by [[Exigent Circumstances and Hot Pursuit|exigency]] must instead be determined case by case on the [[Common Legal Terms#totality-of-the-circumstances|totality of the circumstances]].

## Application
Missouri relied solely on the [[Common Legal Terms#per-se|per se]] theory that dissipating alcohol always creates an [[Exigent Circumstances and Hot Pursuit|exigency]]; it did not show that obtaining a warrant in McNeely's case was impractical or that any other emergency was present. Because metabolization alone did not categorically justify the warrantless draw, and no case-specific [[Exigent Circumstances and Hot Pursuit|exigency]] was established, the blood draw was unreasonable.

## Conclusion
Affirmed; on these facts the warrantless blood draw was not justified by a [[Common Legal Terms#per-se|per se]] [[Exigent Circumstances and Hot Pursuit|exigency]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *McNeely* rejects a [[Common Legal Terms#per-se|per se]] [[Exigent Circumstances and Hot Pursuit|exigency]] rule and was later **refined by** [[Mitchell v. Wisconsin]], which addressed the distinct unconscious-driver scenario.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Progeny / Refinement*
- [[SIA Alcohol Tests]] — *Related (cross-doctrine)*

## Sources
- *Missouri v. McNeely*, 569 U.S. 141 (2013) — https://www.courtlistener.com/opinion/858288/missouri-v-mcneely/ — pinpoint: 156 (per the official U.S. Reports citation; CL carries the reporter text without inline star pagination).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "dd26063e4aaaa7db", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2013 U.S. LEXIS 3160; 2013 WL 1628934", "official_citation_present": false, "parallel_cite": "133 S. Ct. 1552; 185 L. Ed. 2d 696; 569 U.S. 141; 81 U.S.L.W. 4250; 24 Fla. L. Weekly Fed. S 150", "title": "Missouri v. McNeely", "year": "2013"}}
{"assertion_id": "47e452643314a7ec", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Alcohol Tests"}, "payload": {"home": "SIA Alcohol Tests", "role": "Related (cross-doctrine)", "title": "Missouri v. McNeely"}}
{"assertion_id": "5793d1d409ed6a3b", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The natural metabolization of alcohol is NOT a per se exigency justifying a warrantless DUI blood draw in every case; exigency must be…", "title": "Missouri v. McNeely"}}
{"assertion_id": "cb3f1939565de5a2", "dimension": "support", "kind": "home_role", "locator": {"home": "Destruction of Evidence"}, "payload": {"home": "Destruction of Evidence", "role": "Key — Progeny / Refinement", "title": "Missouri v. McNeely"}}
{"assertion_id": "0335f921b4dc8ab5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Missouri v. McNeely"}}
{"assertion_id": "e73ba1fcc9da521e", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2013-04-17", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Missouri v. McNeely", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Missouri v. McNeely", "varies_by_point": "false"}}
```

### lake record — Missouri v. McNeely

```json
{
  "schema_version": "s2.v1",
  "record_id": "Missouri v. McNeely",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Missouri v. McNeely",
    "case_name_short": "McNeely",
    "case_name_full": "MISSOURI, Petitioner v. Tyler G. McNEELY.",
    "input_case_name": "Missouri v. McNeely",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2013-04-17",
    "year": 2013,
    "docket": null,
    "cluster_id": 858288,
    "lead_opinion_id": 858288,
    "sibling_ids": [
      858288
    ],
    "absolute_url": "/opinion/858288/missouri-v-mcneely/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9239980,
        "score": 20,
        "case_name": "Missouri v. McNeely"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "133 S. Ct. 1552",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1552",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 696",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 141",
        "volume": "569",
        "reporter": "U.S.",
        "page": "141",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4250",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4250",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 150",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "150",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2013 U.S. LEXIS 3160",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "3160",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1628934",
        "volume": "2013",
        "reporter": "WL",
        "page": "1628934",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "133 S. Ct. 1552",
        "volume": "133",
        "reporter": "S. Ct.",
        "page": "1552",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "185 L. Ed. 2d 696",
        "volume": "185",
        "reporter": "L. Ed. 2d",
        "page": "696",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 U.S. LEXIS 3160",
        "volume": "2013",
        "reporter": "U.S. LEXIS",
        "page": "3160",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "569 U.S. 141",
        "volume": "569",
        "reporter": "U.S.",
        "page": "141",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "81 U.S.L.W. 4250",
        "volume": "81",
        "reporter": "U.S.L.W.",
        "page": "4250",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "24 Fla. L. Weekly Fed. S 150",
        "volume": "24",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "150",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2013 WL 1628934",
        "volume": "2013",
        "reporter": "WL",
        "page": "1628934",
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
      "id": "pin-156",
      "page": null,
      "quote": "--- # Missouri v. McNeely *569 U.S. 141 (2013)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background McNeely was stopped for speeding, showed signs of intoxication, and refused a breath test. Without seeking a warrant, the officer took him to a hospital and directed a blood draw over his objection. Missouri defended the warrantless draw on the theory that the body's natural elimination of alcohol always creates an exigency. ## Issue Whether the natural metabolization of alcohol in the bloodstream categorically creates an exigency that justifies a warrantless blood draw in every drunk-driving case. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2013-04-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Missouri v. McNeely",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
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
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Seneca Warrior Steeprock",
          "cluster_id": 10102625,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9493043,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Colby Davis Laub",
          "cluster_id": 9473742,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. McCarthy",
          "cluster_id": 10160868,
          "cite": [
            "369 Or. 129",
            "501 P.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Bohigian",
          "cluster_id": 4806187,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jerel Chinedu Igboji v. State",
          "cluster_id": 4789820,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hedgpeth",
          "cluster_id": 10160693,
          "cite": [
            "365 Or. 724",
            "452 P.3d 948"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "In re B.B.",
          "cluster_id": 6243638,
          "cite": [
            "567 S.W.3d 786"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gonzalez v. City of Schenectady",
          "cluster_id": 1038554,
          "cite": [
            "728 F.3d 149",
            "2013 U.S. App. LEXIS 17943",
            "2013 WL 4528864"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
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
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
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
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brokers' Choice of America, Inc. v. NBC Universal, Inc.",
          "cluster_id": 2682361,
          "cite": [
            "757 F.3d 1125",
            "2014 WL 3307834"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fitzgerald v. People",
          "cluster_id": 4385083,
          "cite": [
            "2017 CO 26",
            "394 P.3d 671",
            "2017 WL 1377349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thompson, Ex Parte Ronald",
          "cluster_id": 2949202,
          "cite": [
            "442 S.W.3d 325",
            "2014 Tex. Crim. App. LEXIS 969",
            "2014 WL 4627231"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Evans",
          "cluster_id": 4331789,
          "cite": [
            "153 A.3d 323",
            "2016 Pa. Super. 293",
            "2016 Pa. Super. LEXIS 778"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. McCumber",
          "cluster_id": 4370918,
          "cite": [
            "295 Neb. 941",
            "893 N.W.2d 411"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Caniglia v. Strom",
          "cluster_id": 4883694,
          "cite": [
            "593 U.S. 194",
            "209 L. Ed. 2d 604",
            "141 S. Ct. 1596"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Lemaricus Devall Davidson",
          "cluster_id": 4331383,
          "cite": [
            "509 S.W.3d 156",
            "2016 Tenn. LEXIS 913"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "James Williams v. Brian Maurer",
          "cluster_id": 4958226,
          "cite": [
            "9 F.4th 416"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. William Robert Bernard, Jr.",
          "cluster_id": 2778772,
          "cite": [
            "859 N.W.2d 762",
            "2015 Minn. LEXIS 46",
            "2015 WL 543160"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Michael R. Tullberg",
          "cluster_id": 2764887,
          "cite": [
            "359 Wis. 2d 421",
            "2014 WI 134",
            "857 N.W.2d 120",
            "2014 Wisc. LEXIS 951"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth, Aplt. v. Myers, D.",
          "cluster_id": 4410366,
          "cite": [
            "164 A.3d 1162",
            "2017 WL 3045867",
            "2017 Pa. LEXIS 1689"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Wurie",
          "cluster_id": 870435,
          "cite": [
            "728 F.3d 1",
            "2013 U.S. App. LEXIS 9937",
            "2013 WL 2129119"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Corrin Kathleen Reynolds",
          "cluster_id": 4318256,
          "cite": [
            "504 S.W.3d 283",
            "2016 Tenn. LEXIS 821"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 6243814,
          "cite": [
            "570 S.W.3d 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dean M. Blatterman",
          "cluster_id": 2798569,
          "cite": [
            "362 Wis. 2d 138",
            "2015 WI 46",
            "864 N.W.2d 26",
            "2015 Wisc. LEXIS 175"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Micah Abraham Wulff",
          "cluster_id": 3133317,
          "cite": [
            "157 Idaho 416",
            "337 P.3d 575",
            "2014 Ida. LEXIS 286"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mitchell v. Wisconsin",
          "cluster_id": 4633470,
          "cite": [
            "588 U.S. 840",
            "139 S. Ct. 2525",
            "2019 U.S. LEXIS 4400"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Christopher George Storm",
          "cluster_id": 4405282,
          "cite": [
            "898 N.W.2d 140",
            "2017 WL 2822483",
            "2017 Iowa Sup. LEXIS 81"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anne Marie Gennusa v. Brian Canova",
          "cluster_id": 2669144,
          "cite": [
            "748 F.3d 1103",
            "2014 WL 1363541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Kenneth Ray Washington III",
          "cluster_id": 4472220,
          "cite": [
            "832 N.W.2d 650",
            "2013 WL 2450146",
            "2013 Iowa Sup. LEXIS 69"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. McNeely:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(858288) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTI2NDI4ODAwMDAwJnM9NjIzOTYzMyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28858288%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(858288)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01NCZzPTkwMzQ4OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28858288%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(858288)",
        "reviewed": 77,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 4,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 77,
        "triage_read": 4,
        "triage_snippet_classified": 73
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(858288)",
    "indexed_citing_opinions": 808,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 858288,
        "count": 808,
        "count_source": "search"
      }
    ],
    "citation_count": 1552,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/missouri-v-mcneely.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkwODM5MzUmcz0xMDI3ODMzNCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28858288%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 858288,
        "cited_id": 1755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 104943,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 108854,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 111380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 111423,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112219,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112459,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 112608,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118103,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118326,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 118405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 145654,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 145669,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 145814,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 216733,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 622303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 1257859,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 1869975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2009694,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2035860,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2219022,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2586146,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 858288,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T14:13:34Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:17:00Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:13:49Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Missouri v. McNeely

```
(Slip Opinion)              OCTOBER TERM, 2012                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

                        MISSOURI v. MCNEELY

       CERTIORARI TO THE SUPREME COURT OF MISSOURI

    No. 11–1425. Argued January 9, 2013—Decided April 17, 2013
Respondent McNeely was stopped by a Missouri police officer for speed-
  ing and crossing the centerline. After declining to take a breath test
  to measure his blood alcohol concentration (BAC), he was arrested
  and taken to a nearby hospital for blood testing. The officer never at-
  tempted to secure a search warrant. McNeely refused to consent to
  the blood test, but the officer directed a lab technician to take a sam-
  ple. McNeely’s BAC tested well above the legal limit, and he was
  charged with driving while intoxicated (DWI). He moved to suppress
  the blood test result, arguing that taking his blood without a warrant
  violated his Fourth Amendment rights. The trial court agreed, con-
  cluding that the exigency exception to the warrant requirement did
  not apply because, apart from the fact that McNeely’s blood alcohol
  was dissipating, no circumstances suggested that the officer faced an
  emergency.      The State Supreme Court affirmed, relying on
  Schmerber v. California, 384 U. S. 757, in which this Court upheld a
  DWI suspect’s warrantless blood test where the officer “might rea-
  sonably have believed that he was confronted with an emergency, in
  which the delay necessary to obtain a warrant, under the circum-
  stances, threatened ‘the destruction of evidence,’ ” id., at 770. This
  case, the state court found, involved a routine DWI investigation
  where no factors other than the natural dissipation of blood alcohol
  suggested that there was an emergency, and, thus, the nonconsensu-
  al warrantless test violated McNeely’s right to be free from unrea-
  sonable searches of his person.
Held: The judgment is affirmed.
358 S. W. 3d 65, affirmed.
     JUSTICE SOTOMAYOR delivered the opinion of the Court with respect
  to Parts I, II–A, II–B, and IV, concluding that in drunk-driving inves-
  tigations, the natural dissipation of alcohol in the bloodstream does
2                        MISSOURI v. MCNEELY

                                  Syllabus

    not constitute an exigency in every case sufficient to justify conduct-
    ing a blood test without a warrant. Pp. 4–13, 20–23.
       (a) The principle that a warrantless search of the person is reason-
    able only if it falls within a recognized exception, see, e.g., United
    States v. Robinson, 414 U. S. 218, 224, applies here, where the search
    involved a compelled physical intrusion beneath McNeely’s skin and
    into his veins to obtain a blood sample to use as evidence in a crimi-
    nal investigation. One recognized exception “applies when ‘ “the exi-
    gencies of the situation” make the needs of law enforcement so com-
    pelling that [a] warrantless search is objectively reasonable.’ ”
    Kentucky v. King, 563 U. S. ___, ___. This Court looks to the totality
    of circumstances in determining whether an exigency exits. See
    Brigham City v. Stuart, 547 U. S. 398, 406. Applying this approach
    in Schmerber, the Court found a warrantless blood test reasonable af-
    ter considering all of the facts and circumstances of that case and
    carefully basing its holding on those specific facts, including that al-
    cohol levels decline after drinking stops and that testing was delayed
    while officers transported the injured suspect to the hospital and in-
    vestigated the accident scene. Pp. 4–8.
       (b) The State nonetheless seeks a per se rule, contending that exi-
    gent circumstances necessarily exist when an officer has probable
    cause to believe a person has been driving under the influence of al-
    cohol because BAC evidence is inherently evanescent. Though a per-
    son’s blood alcohol level declines until the alcohol is eliminated, it
    does not follow that the Court should depart from careful case-by-
    case assessment of exigency. When officers in drunk-driving investi-
    gations can reasonably obtain a warrant before having a blood sam-
    ple drawn without significantly undermining the efficacy of the
    search, the Fourth Amendment mandates that they do so. See
    McDonald v. United States, 335 U. S. 451, 456. Circumstances may
    make obtaining a warrant impractical such that the alcohol’s dissipa-
    tion will support an exigency, but that is a reason to decide each case
    on its facts, as in Schmerber, not to accept the “considerable overgen-
    eralization” that a per se rule would reflect, Richards v. Wisconsin,
    520 U. S. 385, 393. Blood testing is different in critical respects from
    other destruction-of-evidence cases. Unlike a situation where, e.g., a
    suspect has control over easily disposable evidence, see Cupp v. Mur-
    phy, 412 U. S. 291, 296, BAC evidence naturally dissipates in a grad-
    ual and relatively predictable manner. Moreover, because an officer
    must typically take a DWI suspect to a medical facility and obtain a
    trained medical professional’s assistance before having a blood test
    conducted, some delay between the time of the arrest or accident and
    time of the test is inevitable regardless of whether a warrant is ob-
    tained. The State’s rule also fails to account for advances in the 47
                     Cite as: 569 U. S. ____ (2013)                      3

                                Syllabus

  years since Schmerber was decided that allow for the more expedi-
  tious processing of warrant applications, particularly in contexts like
  drunk-driving investigations where the evidence supporting probable
  cause is simple. The natural dissipation of alcohol in the blood may
  support an exigency finding in a specific case, as it did in Schmerber,
  but it does not do so categorically. Pp. 8–13.
     (c) Because the State sought a per se rule here, it did not argue that
  there were exigent circumstances in this particular case. The argu-
  ments and the record thus do not provide the Court with an adequate
  framework for a detailed discussion of all the relevant factors that
  can be taken into account in determining the reasonableness of act-
  ing without a warrant. It suffices to say that the metabolization of
  alcohol in the bloodstream and the ensuing loss of evidence are
  among the factors that must be considered in deciding whether a
  warrant is required. Pp. 20–23.
     JUSTICE SOTOMAYOR, joined by JUSTICE SCALIA, JUSTICE GINSBURG,
  and JUSTICE KAGAN, concluded in Part III that other arguments ad-
  vanced by the State and amici in support of a per se rule are unper-
  suasive. Their concern that a case-by-case approach to exigency will
  not provide adequate guidance to law enforcement officers may make
  the desire for a bright-line rule understandable, but the Fourth
  Amendment will not tolerate adoption of an overly broad categorical
  approach in this context. A fact-intensive, totality of the circum-
  stances, approach is hardly unique within this Court’s Fourth
  Amendment jurisprudence. See, e.g., Illinois v. Wardlow, 528 U. S.
  119, 123–125. They also contend that the privacy interest implicated
  here is minimal. But motorists’ diminished expectation of privacy
  does not diminish their privacy interest in preventing a government
  agent from piercing their skin. And though a blood test conducted in
  a medical setting by trained personnel is less intrusive than other
  bodily invasions, this Court has never retreated from its recognition
  that any compelled intrusion into the human body implicates signifi-
  cant, constitutionally protected privacy interests. Finally, the gov-
  ernment’s general interest in combating drunk driving does not justi-
  fy departing from the warrant requirement without showing exigent
  circumstances that make securing a warrant impractical in a particu-
  lar case. Pp. 15–20.

  SOTOMAYOR, J., announced the judgment of the Court and delivered
the opinion of the Court with respect to Parts I, II–A, II–B, and IV, in
which SCALIA, KENNEDY, GINSBURG, and KAGAN, JJ., joined, and an
opinion with respect to Parts II–C and III, in which SCALIA, GINSBURG,
and KAGAN, JJ., joined. KENNEDY, J., filed an opinion concurring in
part. ROBERTS, C. J., filed an opinion concurring in part and dissenting
4                    MISSOURI v. MCNEELY

                             Syllabus

in part, in which BREYER and ALITO, JJ., joined. THOMAS, J., filed a
dissenting opinion.
                       Cite as: 569 U. S. ____ (2013)                              1

                            Opinion of the Court

    NOTICE: This opinion is subject to formal revision before publication in the
    preliminary print of the United States Reports. Readers are requested to
    notify the Reporter of Decisions, Supreme Court of the United States, Wash­
    ington, D. C. 20543, of any typographical or other formal errors, in order
    that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                  _________________

                                  No. 11–1425
                                  _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF

                                                 

                      MISSOURI


                                [April 17, 2013] 


  JUSTICE SOTOMAYOR announced the judgment of the
Court and delivered the opinion of the Court with respect
to Parts I, II–A, II–B, and IV, and an opinion with respect
to Parts II–C and III, in which JUSTICE SCALIA, JUSTICE
GINSBURG, and JUSTICE KAGAN join.
  In Schmerber v. California, 384 U. S. 757 (1966), this
Court upheld a warrantless blood test of an individual
arrested for driving under the influence of alcohol because
the officer “might reasonably have believed that he was
confronted with an emergency, in which the delay neces­
sary to obtain a warrant, under the circumstances, threat­
ened the destruction of evidence.” Id., at 770 (internal
quotation marks omitted). The question presented here
is whether the natural metabolization of alcohol in the
bloodstream presents a per se exigency that justifies an
exception to the Fourth Amendment’s warrant require­
ment for nonconsensual blood testing in all drunk-driving
cases. We conclude that it does not, and we hold, con­
sistent with general Fourth Amendment principles, that
exigency in this context must be determined case by case
based on the totality of the circumstances.
2                          MISSOURI v. MCNEELY

                             Opinion of the Court

                               I
   While on highway patrol at approximately 2:08 a.m., a
Missouri police officer stopped Tyler McNeely’s truck after
observing it exceed the posted speed limit and repeatedly
cross the centerline. The officer noticed several signs
that McNeely was intoxicated, including McNeely’s blood­
shot eyes, his slurred speech, and the smell of alcohol on his
breath. McNeely acknowledged to the officer that he had
consumed “a couple of beers” at a bar, App. 20, and he
appeared unsteady on his feet when he exited the truck.
After McNeely performed poorly on a battery of field­
sobriety tests and declined to use a portable breath-test
device to measure his blood alcohol concentration (BAC),
the officer placed him under arrest.
   The officer began to transport McNeely to the station
house. But when McNeely indicated that he would again
refuse to provide a breath sample, the officer changed
course and took McNeely to a nearby hospital for blood
testing. The officer did not attempt to secure a warrant.
Upon arrival at the hospital, the officer asked McNeely
whether he would consent to a blood test. Reading from
a standard implied consent form, the officer explained to
McNeely that under state law refusal to submit voluntar-
ily to the test would lead to the immediate revocation of his
driver’s license for one year and could be used against him
in a future prosecution. See Mo. Ann. Stat. §§577.020.1,
577.041 (West 2011). McNeely nonetheless refused. The
officer then directed a hospital lab technician to take a
blood sample, and the sample was secured at approxi­
mately 2:35 a.m. Subsequent laboratory testing measured
McNeely’s BAC at 0.154 percent, which was well above the
legal limit of 0.08 percent. See §577.012.1.
   McNeely was charged with driving while intoxicated
(DWI), in violation of §577.010.1 He moved to suppress
——————
    1 As   a result of his two prior drunk-driving convictions, McNeely was
                   Cite as: 569 U. S. ____ (2013)               3

                       Opinion of the Court

the results of the blood test, arguing in relevant part that,
under the circumstances, taking his blood for chemi­
cal testing without first obtaining a search warrant vio-
lated his rights under the Fourth Amendment. The trial
court agreed. It concluded that the exigency exception to
the warrant requirement did not apply because, apart from
the fact that “[a]s in all cases involving intoxication,
[McNeely’s] blood alcohol was being metabolized by his
liver,” there were no circumstances suggesting the officer
faced an emergency in which he could not practicably
obtain a warrant. No. 10CG–CR01849–01 (Cir. Ct. Cape
Giradeau Cty., Mo., Div. II, Mar. 3, 2011), App. to Pet.
for Cert. 43a. On appeal, the Missouri Court of Appeals
stated an intention to reverse but transferred the case
directly to the Missouri Supreme Court. No. ED 96402
(June 21, 2011), id., at 24a.
   The Missouri Supreme Court affirmed. 358 S. W. 3d 65
(2012) (per curiam). Recognizing that this Court’s decision
in Schmerber v. California, 384 U. S. 757, “provide[d] the
backdrop” to its analysis, the Missouri Supreme Court
held that “Schmerber directs lower courts to engage in
a totality of the circumstances analysis when determin­
ing whether exigency permits a nonconsensual, warrantless
blood draw.” 358 S. W. 3d, at 69, 74. The court further
concluded that Schmerber “requires more than the mere
dissipation of blood-alcohol evidence to support a warrant­
less blood draw in an alcohol-related case.” 358 S. W. 3d,
at 70. According to the court, exigency depends heavily on
the existence of additional “ ‘special facts,’ ” such as whether
an officer was delayed by the need to investigate an ac-
cident and transport an injured suspect to the hospital,
as had been the case in Schmerber. 358 S. W. 3d, at 70,
—————— 

charged with a class D felony under Missouri law, which carries a 

maximum imprisonment term of four years. See Mo. Ann. Stat.
     

§§558.011, 577.023.1(5), 577.023.3 (West 2011).

                                               

4                      MISSOURI v. MCNEELY

                          Opinion of the Court

74. Finding that this was “unquestionably a routine DWI
case” in which no factors other than the natural dissi­
pation of blood-alcohol suggested that there was an emer­
gency, the court held that the nonconsensual warrantless
blood draw violated McNeely’s Fourth Amendment right
to be free from unreasonable searches of his person. Id.,
at 74–75.
  We granted certiorari to resolve a split of authority on
the question whether the natural dissipation of alcohol in
the bloodstream establishes a per se exigency that suffices
on its own to justify an exception to the warrant require­
ment for nonconsensual blood testing in drunk-driving
investigations.2 See 567 U. S. ___ (2012). We now affirm.
                             II

                               

                             A

   The Fourth Amendment provides in relevant part that
“[t]he right of the people to be secure in their persons,
houses, papers, and effects, against unreasonable searches
and seizures, shall not be violated, and no Warrants shall
issue, but upon probable cause.” Our cases have held that
a warrantless search of the person is reasonable only if
it falls within a recognized exception. See, e.g., United
States v. Robinson, 414 U. S. 218, 224 (1973). That prin­
ciple applies to the type of search at issue in this case,
which involved a compelled physical intrusion beneath
McNeely’s skin and into his veins to obtain a sample of his
blood for use as evidence in a criminal investigation. Such
an invasion of bodily integrity implicates an individual’s
——————
  2 Compare 358 S. W. 3d 65 (2012) (case below), State v. Johnson, 744

N. W. 2d 340 (Iowa 2008) (same conclusion), and State v. Rodriguez,
2007 UT 15, 156 P. 3d 771 (same), with State v. Shriner, 751 N. W. 2d
538 (Minn. 2008) (holding that the natural dissipation of blood-alcohol
evidence alone constitutes a per se exigency), State v. Bohling, 173 Wis.
2d 529, 494 N. W. 2d 399 (1993) (same); State v. Woolery, 116 Idaho
368, 775 P. 2d 1210 (1989) (same).
                 Cite as: 569 U. S. ____ (2013)            5

                     Opinion of the Court

“most personal and deep-rooted expectations of privacy.”
Winston v. Lee, 470 U. S. 753, 760 (1985); see also Skinner
v. Railway Labor Executives’ Assn., 489 U. S. 602, 616
(1989).
   We first considered the Fourth Amendment restrictions
on such searches in Schmerber, where, as in this case, a
blood sample was drawn from a defendant suspected of
driving while under the influence of alcohol. 384 U. S., at
758. Noting that “[s]earch warrants are ordinarily re­
quired for searches of dwellings,” we reasoned that “absent
an emergency, no less could be required where intrusions
into the human body are concerned,” even when the search
was conducted following a lawful arrest. Id., at 770. We
explained that the importance of requiring authorization
by a “ ‘neutral and detached magistrate’ ” before allowing a
law enforcement officer to “invade another’s body in search
of evidence of guilt is indisputable and great.” Ibid. (quot­
ing Johnson v. United States, 333 U. S. 10, 13–14 (1948)).
   As noted, the warrant requirement is subject to ex­
ceptions. “One well-recognized exception,” and the one
at issue in this case, “applies when the exigencies of the
situation make the needs of law enforcement so compelling
that a warrantless search is objectively reasonable under
the Fourth Amendment.” Kentucky v. King, 563 U. S. ___,
___ (2011) (slip op., at 6) (internal quotation marks and
brackets omitted). A variety of circumstances may give
rise to an exigency sufficient to justify a warrantless
search, including law enforcement’s need to provide emer­
gency assistance to an occupant of a home, Michigan v.
Fisher, 558 U. S. 45, 47–48 (2009) (per curiam), engage in
“hot pursuit” of a fleeing suspect, United States v. San­
tana, 427 U. S. 38, 42–43 (1976), or enter a burning building
to put out a fire and investigate its cause, Michigan v.
Tyler, 436 U. S. 499, 509–510 (1978). As is relevant here,
we have also recognized that in some circumstances law
enforcement officers may conduct a search without a
6                  MISSOURI v. MCNEELY

                      Opinion of the Court

warrant to prevent the imminent destruction of evidence.
See Cupp v. Murphy, 412 U. S. 291, 296 (1973); Ker v.
California, 374 U. S. 23, 40–41 (1963) (plurality opinion).
While these contexts do not necessarily involve equiva-
lent dangers, in each a warrantless search is potentially
reasonable because “there is compelling need for official
action and no time to secure a warrant.” Tyler, 436 U. S.,
at 509.
   To determine whether a law enforcement officer faced
an emergency that justified acting without a warrant, this
Court looks to the totality of circumstances. See Brigham
City v. Stuart, 547 U. S. 398, 406 (2006) (finding officers’
entry into a home to provide emergency assistance “plain­
ly reasonable under the circumstances”); Illinois v. Mc-
Arthur, 531 U. S. 326, 331 (2001) (concluding that a war­
rantless seizure of a person to prevent him from returning
to his trailer to destroy hidden contraband was reasonable
“[i]n the circumstances of the case before us” due to exi­
gency); Cupp, 412 U. S., at 296 (holding that a limited
warrantless search of a suspect’s fingernails to preserve
evidence that the suspect was trying to rub off was justi­
fied “[o]n the facts of this case”); see also Richards v.
Wisconsin, 520 U. S. 385, 391–396 (1997) (rejecting a
per se exception to the knock-and-announce requirement
for felony drug investigations based on presumed exigen­
cy, and requiring instead evaluation of police conduct “in
a particular case”). We apply this “finely tuned approach”
to Fourth Amendment reasonableness in this context be-
cause the police action at issue lacks “the traditional
justification that . . . a warrant . . . provides.” Atwater v.
Lago Vista, 532 U. S. 318, 347, n. 16 (2001). Absent that
established justification, “the fact-specific nature of the
reasonableness inquiry,” Ohio v. Robinette, 519 U. S. 33,
39 (1996), demands that we evaluate each case of alleged
exigency based “on its own facts and circumstances.” Go-
Bart Importing Co. v. United States, 282 U. S. 344, 357
                    Cite as: 569 U. S. ____ (2013)                   7

                         Opinion of the Court

(1931).3
   Our decision in Schmerber applied this totality of the
circumstances approach. In that case, the petitioner had
suffered injuries in an automobile accident and was taken
to the hospital. 384 U. S., at 758. While he was there
receiving treatment, a police officer arrested the petitioner
for driving while under the influence of alcohol and or­
dered a blood test over his objection. Id., at 758–759.
After explaining that the warrant requirement applied
generally to searches that intrude into the human body,
we concluded that the warrantless blood test “in the pre­
sent case” was nonetheless permissible because the officer
“might reasonably have believed that he was confronted
with an emergency, in which the delay necessary to obtain
a warrant, under the circumstances, threatened ‘the de­
struction of evidence.’ ” Id., at 770 (quoting Preston v.
United States, 376 U. S. 364, 367 (1964)).
   In support of that conclusion, we observed that evidence
could have been lost because “the percentage of alcohol in
the blood begins to diminish shortly after drinking stops,
as the body functions to eliminate it from the system.”
384 U. S., at 770. We added that “[p]articularly in a case
such as this, where time had to be taken to bring the
accused to a hospital and to investigate the scene of the
accident, there was no time to seek out a magistrate and
secure a warrant.” Id., at 770–771. “Given these special
facts,” we found that it was appropriate for the police to
——————
  3 We have recognized a limited class of traditional exceptions to the

warrant requirement that apply categorically and thus do not require
an assessment of whether the policy justifications underlying the ex-
ception, which may include exigency-based considerations, are im­
plicated in a particular case. See, e.g., California v. Acevedo, 500
U. S. 565, 569–570 (1991) (automobile exception); United States v.
Robinson, 414 U. S. 218, 224–235 (1973) (searches of a person incident
to a lawful arrest). By contrast, the general exigency exception, which
asks whether an emergency existed that justified a warrantless search,
naturally calls for a case-specific inquiry.
8                  MISSOURI v. MCNEELY

                     Opinion of the Court

act without a warrant. Id., at 771. We further held that
the blood test at issue was a reasonable way to recover the
evidence because it was highly effective, “involve[d] vir­
tually no risk, trauma, or pain,” and was conducted in a
reasonable fashion “by a physician in a hospital environ­
ment according to accepted medical practices.” Ibid. And
in conclusion, we noted that our judgment that there had
been no Fourth Amendment violation was strictly based
“on the facts of the present record.” Id., at 772.
   Thus, our analysis in Schmerber fits comfortably within
our case law applying the exigent circumstances excep­
tion. In finding the warrantless blood test reasonable in
Schmerber, we considered all of the facts and circumstances
of the particular case and carefully based our holding on
those specific facts.
                             B
  The State properly recognizes that the reasonableness
of a warrantless search under the exigency exception to
the warrant requirement must be evaluated based on the
totality of the circumstances. Brief for Petitioner 28–29.
But the State nevertheless seeks a per se rule for blood
testing in drunk-driving cases. The State contends that
whenever an officer has probable cause to believe an
individual has been driving under the influence of alcohol,
exigent circumstances will necessarily exist because BAC
evidence is inherently evanescent. As a result, the State
claims that so long as the officer has probable cause and
the blood test is conducted in a reasonable manner, it is
categorically reasonable for law enforcement to obtain the
blood sample without a warrant.
  It is true that as a result of the human body’s natural
metabolic processes, the alcohol level in a person’s blood
begins to dissipate once the alcohol is fully absorbed and
continues to decline until the alcohol is eliminated. See
Skinner, 489 U. S., at 623; Schmerber, 384 U. S., at 770–
                 Cite as: 569 U. S. ____ (2013)            9

                     Opinion of the Court

771. Testimony before the trial court in this case indicated
that the percentage of alcohol in an individual’s blood
typically decreases by approximately 0.015 percent to 0.02
percent per hour once the alcohol has been fully absorbed.
App. 47. More precise calculations of the rate at which
alcohol dissipates depend on various individual character­
istics (such as weight, gender, and alcohol tolerance) and
the circumstances in which the alcohol was consumed.
See Stripp, Forensic and Clinical Issues in Alcohol Analy­
sis, in Forensic Chemistry Handbook 437–441 (L. Kobilin­
sky ed. 2012). Regardless of the exact elimination rate, it
is sufficient for our purposes to note that because an indi­
vidual’s alcohol level gradually declines soon after he stops
drinking, a significant delay in testing will negatively
affect the probative value of the results. This fact was
essential to our holding in Schmerber, as we recognized
that, under the circumstances, further delay in order to
secure a warrant after the time spent investigating the
scene of the accident and transporting the injured suspect
to the hospital to receive treatment would have threatened
the destruction of evidence. 384 U. S., at 770–771.
   But it does not follow that we should depart from careful
case-by-case assessment of exigency and adopt the cate­
gorical rule proposed by the State and its amici. In those
drunk-driving investigations where police officers can
reasonably obtain a warrant before a blood sample can be
drawn without significantly undermining the efficacy of
the search, the Fourth Amendment mandates that they
do so. See McDonald v. United States, 335 U. S. 451, 456
(1948) (“We cannot . . . excuse the absence of a search
warrant without a showing by those who seek exemption
from the constitutional mandate that the exigencies of the
situation made [the search] imperative”). We do not doubt
that some circumstances will make obtaining a warrant
impractical such that the dissipation of alcohol from the
bloodstream will support an exigency justifying a properly
10                 MISSOURI v. MCNEELY

                     Opinion of the Court

conducted warrantless blood test. That, however, is a
reason to decide each case on its facts, as we did in
Schmerber, not to accept the “considerable overgeneraliza­
tion” that a per se rule would reflect. Richards, 520 U. S.,
at 393.
   The context of blood testing is different in critical re­
spects from other destruction-of-evidence cases in which
the police are truly confronted with a “ ‘now or never’ ”
situation. Roaden v. Kentucky, 413 U. S. 496, 505 (1973).
In contrast to, for example, circumstances in which the
suspect has control over easily disposable evidence, see
Georgia v. Randolph, 547 U. S. 103, 116, n. 6 (2006);
Cupp, 412 U. S., at 296, BAC evidence from a drunk­
driving suspect naturally dissipates over time in a gradual
and relatively predictable manner. Moreover, because a
police officer must typically transport a drunk-driving
suspect to a medical facility and obtain the assistance of
someone with appropriate medical training before con­
ducting a blood test, some delay between the time of the
arrest or accident and the time of the test is inevitable
regardless of whether police officers are required to obtain
a warrant. See State v. Shriner, 751 N. W. 2d 538, 554
(Minn. 2008) (Meyer, J., dissenting). This reality under­
mines the force of the State’s contention, endorsed by the
dissent, see post, at 3 (opinion of THOMAS, J.), that we
should recognize a categorical exception to the warrant
requirement because BAC evidence “is actively being
destroyed with every minute that passes.” Brief for Peti­
tioner 27. Consider, for example, a situation in which the
warrant process will not significantly increase the delay
before the blood test is conducted because an officer can
take steps to secure a warrant while the suspect is being
transported to a medical facility by another officer. In
such a circumstance, there would be no plausible justifica­
tion for an exception to the warrant requirement.
   The State’s proposed per se rule also fails to account for
                     Cite as: 569 U. S. ____ (2013)                   11

                          Opinion of the Court

advances in the 47 years since Schmerber was decided
that allow for the more expeditious processing of warrant
applications, particularly in contexts like drunk-driving
investigations where the evidence offered to establish
probable cause is simple. The Federal Rules of Criminal
Procedure were amended in 1977 to permit federal magis­
trate judges to issue a warrant based on sworn testimony
communicated by telephone. See 91 Stat. 319. As amended,
the law now allows a federal magistrate judge to con-
sider “information communicated by telephone or other
reliable electronic means.” Fed. Rule Crim. Proc. 4.1.
States have also innovated. Well over a majority of States
allow police officers or prosecutors to apply for search
warrants remotely through various means, including
telephonic or radio communication, electronic communica­
tion such as e-mail, and video conferencing.4 And in addi­
——————
  4 See Ala. Rule Crim. Proc. 3.8(b) (2012–2013); Alaska Stat.

§12.35.015 (2012); Ariz. Rev. Stat. Ann. §§13–3914(C), 13–3915(D), (E)
(West 2010); Ark. Code Ann. §16–82–201 (2005); Cal. Penal Code Ann.
§1526(b) (West 2011); Colo. Rule Crim. Proc. 41(c)(3) (2012); Ga. Code
Ann. §17–5–21.1 (2008); Haw. Rules Penal Proc. 41(h)–(i) (2013); Idaho
Code §§19–4404, 19–4406 (Lexis 2004); Ind. Code §35–33–5–8 (2012);
Iowa Code §§321J.10(3), 462A.14D(3) (2009) (limited to specific circum­
stances involving accidents); Kan. Stat. Ann. §§22–2502(a), 22–2504
(2011 Cum. Supp.); La. Code Crim. Proc. Ann., Arts. 162.1(B), (D) (West
2003); Mich. Comp. Laws Ann. §§780.651(2)–(6) (West 2006); Minn.
Rules Crim. Proc. 33.05, 36.01–36.08 (2010 and Supp. 2013); Mont.
Code Ann. §§46–5–221, 46–5–222 (2012); Neb. Rev. Stat. §§29–814.01,
29–814.03, 29–814.05 (2008); Nev. Rev. Stat. §§179.045(2), (4) (2011);
N. H. Rev. Stat. Ann. §595–A:4–a (Lexis Supp. 2012); N. J. Rule Crim.
Proc. 3:5–3(b) (2013); N. M. Rules Crim. Proc. 5–211(F)(3), (G)(3) (Supp.
2012); N. Y. Crim. Proc. Law Ann. §§690.35(1), 690.36(1), 690.40(3),
690.45(1), (2) (West 2009); N. C. Gen. Stat. Ann. §15A–245(a)(3) (Lexis
2011); N. D. Rules Crim. Proc. 41(c)(2)–(3) (2012–2013); Ohio Rules
Crim. Proc. 41(C)(1)–(2) (2011); Okla. Stat. Ann., Tit. 22, §§1223.1,
1225(B) (West 2011); Ore. Rev. Stat. §§133.545(5)–(6) (2011); Pa. Rules
Crim. Proc. 203(A), (C) (2012); S. D. Codified Laws §§23A–35–4.2, 23A–
35–5, 23A–35–6 (2004); Utah Rule Crim. Proc. 40(l) (2012); Vt. Rules
Crim. Proc. 41(c)(4), (g)(2) (Supp. 2012); Va. Code Ann. §19.2–54 (Lexis
12                     MISSOURI v. MCNEELY

                         Opinion of the Court

tion to technology-based developments, jurisdictions have
found other ways to streamline the warrant process, such
as by using standard-form warrant applications for drunk­
driving investigations.5
   We by no means claim that telecommunications inno­
vations have, will, or should eliminate all delay from the
warrant-application process. Warrants inevitably take
some time for police officers or prosecutors to complete and
for magistrate judges to review. Telephonic and electronic
warrants may still require officers to follow time­
consuming formalities designed to create an adequate
record, such as preparing a duplicate warrant before
calling the magistrate judge. See Fed. Rule Crim. Proc.
4.1(b)(3). And improvements in communications technolo­
gy do not guarantee that a magistrate judge will be avail­
able when an officer needs a warrant after making a late­
night arrest. But technological developments that enable
police officers to secure warrants more quickly, and do so
without undermining the neutral magistrate judge’s es­
sential role as a check on police discretion, are relevant to
an assessment of exigency. That is particularly so in this
context, where BAC evidence is lost gradually and

—————— 

Supp. 2012); Wash. Super. Ct. Crim. Rule 2.3(c) (2002); Wis. Stat. 

§968.12(3) (2007–2008); Wyo. Stat. Ann. §31–6–102(d) (2011); see 

generally 2 W. LaFave, Search and Seizure §4.3(b), pp. 511–516, and
     

n. 29 (4th ed. 2004) (describing oral search warrants and collecting
state laws). Missouri requires that search warrants be in writing and
does not permit oral testimony, thus excluding telephonic warrants. Mo.
Ann. Stat. §§542.276.2(1), 542.276.3 (West Supp. 2012). State law does
permit the submission of warrant applications “by facsimile or other
electronic means.” §542.276.3.
  5 During the suppression hearing in this case, McNeely entered into

evidence a search-warrant form used in drunk-driving cases by the
prosecutor’s office in Cape Girardeau County, where the arrest took
place. App. 61–69. The arresting officer acknowledged that he had
used such forms in the past and that they were “readily available.” Id.,
at 41–42.
                     Cite as: 569 U. S. ____ (2013)                   13

                         Opinion of the Court
                       Opinion of SOTOMAYOR, J.

relatively predictably.6
  Of course, there are important countervailing concerns.
While experts can work backwards from the BAC at the
time the sample was taken to determine the BAC at the
time of the alleged offense, longer intervals may raise
questions about the accuracy of the calculation. For that
reason, exigent circumstances justifying a warrantless
blood sample may arise in the regular course of law en­
forcement due to delays from the warrant application
process. But adopting the State’s per se approach would
improperly ignore the current and future technological
developments in warrant procedures, and might well
diminish the incentive for jurisdictions “to pursue progres­
sive approaches to warrant acquisition that preserve the
protections afforded by the warrant while meeting the
legitimate interests of law enforcement.” State v. Rodri-
guez, 2007 UT 15, ¶46, 156 P. 3d 771, 779.
   In short, while the natural dissipation of alcohol in the
blood may support a finding of exigency in a specific case,
as it did in Schmerber, it does not do so categorically.
Whether a warrantless blood test of a drunk-driving sus­
pect is reasonable must be determined case by case based
on the totality of the circumstances.
                            C
  In an opinion concurring in part and dissenting in part,
THE CHIEF JUSTICE agrees that the State’s proposed per se
rule is overbroad because “[f]or exigent circumstances to
——————
  6 The dissent claims that a “50-state survey [is] irrelevant to the ac­

tual disposition of this case” because Missouri requires written warrant
applications. Post, at 8. But the per se exigency rule that the State
seeks and the dissent embraces would apply nationally because it
treats “the body’s natural metabolization of alcohol” as a sufficient
basis for a warrantless search everywhere and always. Post, at 1. The
technological innovations in warrant procedures that many States
have adopted are accordingly relevant to show that the per se rule is
overbroad.
14                  MISSOURI v. MCNEELY

                      Opinion of the Court
                    Opinion of SOTOMAYOR, J.

justify a warrantless search . . . there must . . . be ‘no time
to secure a warrant.’ ” Post, at 6 (quoting Tyler, 436 U. S.,
at 509). But THE CHIEF JUSTICE then goes on to suggest
his own categorical rule under which a warrantless blood
draw is permissible if the officer could not secure a war­
rant (or reasonably believed he could not secure a war­
rant) in the time it takes to transport the suspect to a
hospital or similar facility and obtain medical assistance.
Post, at 8–9. Although we agree that delay inherent to the
blood-testing process is relevant to evaluating exigency,
see supra, at 10, we decline to substitute THE CHIEF
JUSTICE’s modified per se rule for our traditional totality of
the circumstances analysis.
   For one thing, making exigency completely dependent
on the window of time between an arrest and a blood test
produces odd consequences. Under THE CHIEF JUSTICE’s
rule, if a police officer serendipitously stops a suspect near
an emergency room, the officer may conduct a noncon-
sensual warrantless blood draw even if all agree that a
warrant could be obtained with very little delay under the
circumstances (perhaps with far less delay than an aver­
age ride to the hospital in the jurisdiction). The rule
would also distort law enforcement incentives. As with
the State’s per se rule, THE CHIEF JUSTICE’s rule might
discourage efforts to expedite the warrant process because
it categorically authorizes warrantless blood draws so long
as it takes more time to secure a warrant than to obtain
medical assistance. On the flip side, making the require­
ment of independent judicial oversight turn exclusively on
the amount of time that elapses between an arrest and
BAC testing could induce police departments and individ­
ual officers to minimize testing delay to the detriment of
other values. THE CHIEF JUSTICE correctly observes that
“[t]his case involves medical personnel drawing blood at a
medical facility, not police officers doing so by the side of
the road.” Post, at 6–7, n. 2. But THE CHIEF JUSTICE does
                  Cite as: 569 U. S. ____ (2013)           15

                      Opinion of the Court
                    Opinion of SOTOMAYOR, J.

not say that roadside blood draws are necessarily un-
reasonable, and if we accepted THE CHIEF JUSTICE’s ap­
proach, they would become a more attractive option for the
police.
                              III
   The remaining arguments advanced in support of a
per se exigency rule are unpersuasive.
   The State and several of its amici, including the United
States, express concern that a case-by-case approach to
exigency will not provide adequate guidance to law en­
forcement officers deciding whether to conduct a blood test
of a drunk-driving suspect without a warrant. THE CHIEF
JUSTICE and the dissent also raise this concern. See post,
at 1, 9–10 (opinion of ROBERTS, C. J.); post, at 5–7 (opinion
of THOMAS, J.). While the desire for a bright-line rule is
understandable, the Fourth Amendment will not tolerate
adoption of an overly broad categorical approach that
would dilute the warrant requirement in a context where
significant privacy interests are at stake. Moreover, a
case-by-case approach is hardly unique within our Fourth
Amendment jurisprudence. Numerous police actions
are judged based on fact-intensive, totality of the circum­
stances analyses rather than according to categorical
rules, including in situations that are more likely to require
police officers to make difficult split-second judgments.
See, e.g., Illinois v. Wardlow, 528 U. S. 119, 123–125
(2000) (whether an officer has reasonable suspicion to
make an investigative stop and to pat down a suspect for
weapons under Terry v. Ohio, 392 U. S. 1 (1968)); Robi-
nette, 519 U. S., at 39–40 (whether valid consent has been
given to search); Tennessee v. Garner, 471 U. S. 1, 8–9, 20
(1985) (whether force used to effectuate a seizure, includ­
ing deadly force, is reasonable). As in those contexts, we
see no valid substitute for careful case-by-case evaluation
16                      MISSOURI v. MCNEELY

                          Opinion of the Court
                        Opinion of SOTOMAYOR, J.

of reasonableness here.7
   Next, the State and the United States contend that the
privacy interest implicated by blood draws of drunk­
driving suspects is relatively minimal. That is so, they
claim, both because motorists have a diminished expecta­
tion of privacy and because our cases have repeatedly
indicated that blood testing is commonplace in society and
typically involves “virtually no risk, trauma, or pain.”
Schmerber, 384 U. S., at 771. See also post, at 3, and n. 1
(opinion of THOMAS, J.).
   But the fact that people are “accorded less privacy in . . .
automobiles because of th[e] compelling governmental
need for regulation,” California v. Carney, 471 U. S. 386,
392 (1985), does not diminish a motorist’s privacy interest
in preventing an agent of the government from piercing
his skin. As to the nature of a blood test conducted in a
medical setting by trained personnel, it is concededly less
intrusive than other bodily invasions we have found un­
reasonable. See Winston, 470 U. S., at 759–766 (surgery
to remove a bullet); Rochin v. California, 342 U. S. 165,
172–174 (1952) (induced vomiting to extract narcotics
capsules ingested by a suspect violated the Due Process
Clause). For that reason, we have held that medically
drawn blood tests are reasonable in appropriate circum­
stances. See Skinner, 489 U. S., at 618–633 (upholding
——————
  7 The dissent contends that officers in the field will be unable to apply

the traditional totality of the circumstances test in this context because
they will not know all of the relevant facts at the time of an arrest.
See post, at 6. But because “[t]he police are presumably familiar with
the mechanics and time involved in the warrant process in their partic­
ular jurisdiction,” post, at 8 (opinion of ROBERTS, C. J.), we expect that
officers can make reasonable judgments about whether the warrant
process would produce unacceptable delay under the circumstances.
Reviewing courts in turn should assess those judgments “ ‘from the
perspective of a reasonable officer on the scene, rather than with the
20/20 vision of hindsight.’ ” Ryburn v. Huff, 565 U. S. ___, ___ (2012)
(per curiam) (slip op., at 8).
                     Cite as: 569 U. S. ____ (2013)                    17

                         Opinion of the Court
                       Opinion of SOTOMAYOR, J.

warrantless blood testing of railroad employees involved
in certain train accidents under the “special needs” doc­
trine); Schmerber, 384 U. S., at 770–772. We have never
retreated, however, from our recognition that any com­
pelled intrusion into the human body implicates signifi­
cant, constitutionally protected privacy interests.
   Finally, the State and its amici point to the compelling
governmental interest in combating drunk driving and
contend that prompt BAC testing, including through blood
testing, is vital to pursuit of that interest. They argue
that is particularly so because, in addition to laws that
make it illegal to operate a motor vehicle under the influ­
ence of alcohol, all 50 States and the District of Columbia
have enacted laws that make it per se unlawful to operate
a motor vehicle with a BAC of over 0.08 percent. See
National Highway Traffic Safety Admin. (NHTSA), Al­
cohol and Highway Safety: A Review of the State of
Knowledge 167 (No. 811374, Mar. 2011) (NHTSA Re­
view).8 To enforce these provisions, they reasonably as­
sert, accurate BAC evidence is critical. See also post, at
4–5 (opinion of ROBERTS, C. J.); post, at 4–5 (opinion of
THOMAS, J.).
   “No one can seriously dispute the magnitude of the
drunken driving problem or the States’ interest in eradi­
cating it.” Michigan Dept. of State Police v. Sitz, 496 U. S.
444, 451 (1990). Certainly we do not. While some pro­
gress has been made, drunk driving continues to exact a

——————
  8 Pursuant to congressional directive, the NHTSA conditions federal

highway grants on States’ adoption of laws making it a per se offense to
operate a motor vehicle with a BAC of 0.08 percent or greater. See 23
U. S. C. §163(a); 23 CFR §1225.1 (2012). Several federal prohibitions
on drunk driving also rely on the 0.08 percent standard. E.g., 32 CFR
§§234.17(c)(1)(ii), 1903.4(b)(1)(i)–(ii); 36 CFR §4.23(a)(2). In addition,
32 States and the District of Columbia have adopted laws that impose
heightened penalties for operating a motor vehicle at or above a BAC of
0.15 percent. See NHTSA Review 175.
18                 MISSOURI v. MCNEELY

                     Opinion of the Court
                   Opinion of SOTOMAYOR, J.

terrible toll on our society. See NHTSA, Traffic Safety
Facts, 2011 Data 1 (No. 811700, Dec. 2012) (reporting that
9,878 people were killed in alcohol-impaired driving
crashes in 2011, an average of one fatality every 53
minutes).
  But the general importance of the government’s interest
in this area does not justify departing from the warrant
requirement without showing exigent circumstances that
make securing a warrant impractical in a particular case.
To the extent that the State and its amici contend that
applying the traditional Fourth Amendment totality-of­
the-circumstances analysis to determine whether an exi­
gency justified a warrantless search will undermine the
governmental interest in preventing and prosecuting
drunk-driving offenses, we are not convinced.
  As an initial matter, States have a broad range of legal
tools to enforce their drunk-driving laws and to secure
BAC evidence without undertaking warrantless noncon­
sensual blood draws. For example, all 50 States have
adopted implied consent laws that require motorists, as a
condition of operating a motor vehicle within the State, to
consent to BAC testing if they are arrested or otherwise
detained on suspicion of a drunk-driving offense. See
NHTSA Review 173; supra, at 2 (describing Missouri’s
implied consent law). Such laws impose significant conse­
quences when a motorist withdraws consent; typically the
motorist’s driver’s license is immediately suspended or
revoked, and most States allow the motorist’s refusal to
take a BAC test to be used as evidence against him in a
subsequent criminal prosecution. See NHTSA Review
173–175; see also South Dakota v. Neville, 459 U. S. 553,
554, 563–564 (1983) (holding that the use of such an ad­
verse inference does not violate the Fifth Amendment
right against self-incrimination).
  It is also notable that a majority of States either place
significant restrictions on when police officers may obtain
                     Cite as: 569 U. S. ____ (2013)                  19

                         Opinion of the Court
                       Opinion of SOTOMAYOR, J.

a blood sample despite a suspect’s refusal (often limiting
testing to cases involving an accident resulting in death or
serious bodily injury) or prohibit nonconsensual blood
tests altogether.9 Among these States, several lift re­
strictions on nonconsensual blood testing if law enforce­
ment officers first obtain a search warrant or similar court
order.10 Cf. Bullcoming v. New Mexico, 564 U. S. ___, ___
——————
  9 See Ala. Code §32–5–192(c) (2010); Alaska Stat. §§28.35.032(a),

28.35.035(a) (2012); Ariz. Rev. Stat. Ann. §28–1321(D)(1) (West 2012);
Ark. Code Ann. §§5–65–205(a)(1), 5–65–208(a)(1) (Supp. 2011);
Conn. Gen. Stat. §§14–227b(b), 14–227c(b) (2011); Fla. Stat. Ann.
§316.1933(1)(a) (West 2006); Ga. Code Ann. §§40–5–67.1(d), (d.1)
(2011); Haw. Rev. Stat. §291E–15 (2009 Cum. Supp.), §§291E–21(a),
291E–33 (2007), §291E–65 (2009 Cum. Supp.); Iowa Code §§321J.9(1),
321J.10(1), 321J.10A(1) (2009); Kan. Stat. Ann. §§8–1001(b), (d) (2001);
Ky. Rev. Stat. Ann. §189A.105(2) (Lexis Supp. 2012); La. Rev. Stat.
Ann. §§32:666.A(1)(a)(i), (2) (Supp. 2013); Md. Transp. Code Ann. §§16–
205.1(b)(i)(1), (c)(1) (Lexis 2012); Mass. Gen. Laws Ann., ch. 90,
§§24(1)(e), (f)(1) (West 2012); Mich. Comp. Laws Ann. §257.625d(1)
(West 2006); Miss. Code Ann. §63–11–21 (1973–2004); Mont. Code Ann.
§§61–8–402(4), (5) (2011); Neb. Rev. Stat. §60–498.01(2) (2012
Cum. Supp.), §60–6,210 (2010); N. H. Rev. Stat. Ann. §§265–A:14(I),
265–A:16 (West 2012 Cum. Supp.); N. M. Stat. Ann. §66–8–111(A)
(LexisNexis 2009); N. Y. Veh. & Traf. Law Ann. §§1194(2)(b)(1), 1194(3)
(West 2011); N. D. Cent. Code Ann. §39–20–01.1(1) (Lexis Supp. 2011),
§39–20–04(1) (Lexis 2008); Okla. Stat., Tit. 47, §753 (West Supp. 2013);
Ore. Rev. Stat. §813.100(2) (2011); 75 Pa. Cons. Stat. §1547(b)(1)
(2004); R. I. Gen. Laws §§31–27–2.1(b), 31–27–2.9(a) (Lexis 2010); S. C.
Code Ann. §56–5–2950(B) (Supp. 2011); Tenn. Code Ann. §§55–10–
406(a)(4), (f) (2012); Tex. Transp. Code Ann. §§724.012(b), 724.013
(West 2011); Vt. Stat. Ann., Tit. 23, §§1202(b), (f) (2007); Wash. Rev.
Code §§46.20.308 (2)–(3), (5) (2012); W. Va. Code Ann. §17C–5–7 (Lexis
Supp. 2012); Wyo. Stat. Ann. §31–6–102(d) (Lexis 2011).
  10 See Ariz. Rev. Stat. Ann. §28–1321(D)(1) (West 2012); Ga. Code

Ann. §§40–5–67.1(d), (d.1) (2011); Ky. Rev. Stat. Ann. §189A.105(2)(b)
(Lexis Supp. 2012); Mich. Comp. Laws Ann. §257.625d(1) (West 2006);
Mont. Code Ann. §61–8–402(5) (2011); N. M. Stat. Ann. §66–8–111(A)
(LexisNexis 2009); N. Y. Veh. & Traf. Law Ann. §§1194(2)(b)(1), 1194(3)
(West 2011); Ore. Rev. Stat. 813.320(2)(b) (2011); R. I. Gen. Laws §31–
27–2.9(a) (Lexis 2010); Tenn. Code Ann. §55–10–406(a)(4) (2012); Vt.
Stat. Ann., Tit. 23, §1202(f) (2007); Wash. Rev. Code §46.20.308(1)
20                    MISSOURI v. MCNEELY

                         Opinion of the Court

(2011) (slip op., at 3) (noting that the blood test was ob­
tained pursuant to a warrant after the petitioner refused a
breath test). We are aware of no evidence indicating that
restrictions on nonconsensual blood testing have compro­
mised drunk-driving enforcement efforts in the States that
have them. And in fact, field studies in States that permit
nonconsensual blood testing pursuant to a warrant have
suggested that, although warrants do impose administra­
tive burdens, their use can reduce breath-test-refusal
rates and improve law enforcement’s ability to recover
BAC evidence. See NHTSA, Use of Warrants for Breath
Test Refusal: Case Studies 36–38 (No. 810852, Oct. 2007).
   To be sure, “States [may] choos[e] to protect privacy
beyond the level that the Fourth Amendment requires.”
Virginia v. Moore, 553 U. S. 164, 171 (2008). But wide­
spread state restrictions on nonconsensual blood testing
provide further support for our recognition that compelled
blood draws implicate a significant privacy interest. They
also strongly suggest that our ruling today will not “se­
verely hamper effective law enforcement.” Garner, 471
U. S., at 19.
                            IV
  The State argued before this Court that the fact that
alcohol is naturally metabolized by the human body cre­
ates an exigent circumstance in every case. The State did
not argue that there were exigent circumstances in this
particular case because a warrant could not have been
obtained within a reasonable amount of time. In his
testimony before the trial court, the arresting officer did
—————— 

(2012); W. Va. Code Ann. §17C–5–7 (Supp. 2012) (as interpreted in
     

State v. Stone, 229 W. Va. 271, ___, 728 S. E. 2d 155, 167–168 (2012)); 

Wyo. Stat. Ann. §31–6–102(d) (2011); see also State v. Harris, 763 

N. W. 2d 269, 273–274 (Iowa 2009) (per curiam) (recognizing that Iowa
law imposes a warrant requirement subject to a limited case-specific
exigency exception).
                     Cite as: 569 U. S. ____ (2013)                  21

                         Opinion of the Court

not identify any other factors that would suggest he faced
an emergency or unusual delay in securing a warrant.
App. 40. He testified that he made no effort to obtain
a search warrant before conducting the blood draw even
though he was “sure” a prosecuting attorney was on call
and even though he had no reason to believe that a magis­
trate judge would have been unavailable. Id., at 39, 41–
42. The officer also acknowledged that he had obtained
search warrants before taking blood samples in the past
without difficulty. Id., at 42. He explained that he elected
to forgo a warrant application in this case only because he
believed it was not legally necessary to obtain a warrant.
Id., at 39–40. Based on this testimony, the trial court
concluded that there was no exigency and specifically
found that, although the arrest took place in the middle of
the night, “a prosecutor was readily available to apply for
a search warrant and a judge was readily available to
issue a warrant.” App. to Pet. for Cert. 43a.11
   The Missouri Supreme Court in turn affirmed that
judgment, holding first that the dissipation of alcohol did
not establish a per se exigency, and second that the State
could not otherwise satisfy its burden of establishing
exigent circumstances. 358 S. W. 3d, at 70, 74–75. In
petitioning for certiorari to this Court, the State chal­
lenged only the first holding; it did not separately contend
that the warrantless blood test was reasonable regardless
of whether the natural dissipation of alcohol in a suspect’s
blood categorically justifies dispensing with the warrant
——————
  11 No findings were made by the trial court concerning how long a
warrant would likely have taken to issue under the circumstances. The
minimal evidence presented on this point was not uniform. A second
patrol officer testified that in a typical DWI case, it takes between 90
minutes and 2 hours to obtain a search warrant following an arrest.
App. 53–54. McNeely, however, also introduced an exhibit document­
ing six recent search warrant applications for blood testing in Cape
Girardeau County that had shorter processing times. Id., at 70.
22                  MISSOURI v. MCNEELY

                      Opinion of the Court

requirement. See Pet. for Cert. i.
   Here and in its own courts the State based its case on
an insistence that a driver who declines to submit to test­
ing after being arrested for driving under the influence of
alcohol is always subject to a nonconsensual blood test
without any precondition for a warrant. That is incorrect.
   Although the Missouri Supreme Court referred to this
case as “unquestionably a routine DWI case,” 358 S. W.
3d, at 74, the fact that a particular drunk-driving stop is
“routine” in the sense that it does not involve “ ‘special
facts,’ ” ibid., such as the need for the police to attend to a
car accident, does not mean a warrant is required. Other
factors present in an ordinary traffic stop, such as the
procedures in place for obtaining a warrant or the avail­
ability of a magistrate judge, may affect whether the police
can obtain a warrant in an expeditious way and therefore
may establish an exigency that permits a warrantless
search. The relevant factors in determining whether a
warrantless search is reasonable, including the practical
problems of obtaining a warrant within a timeframe that
still preserves the opportunity to obtain reliable evidence,
will no doubt vary depending upon the circumstances in
the case.
   Because this case was argued on the broad proposition
that drunk-driving cases present a per se exigency, the
arguments and the record do not provide the Court with
an adequate analytic framework for a detailed discussion
of all the relevant factors that can be taken into account in
determining the reasonableness of acting without a war­
rant. It suffices to say that the metabolization of alcohol
in the bloodstream and the ensuing loss of evidence are
among the factors that must be considered in deciding
whether a warrant is required. No doubt, given the large
number of arrests for this offense in different jurisdictions
nationwide, cases will arise when anticipated delays in
obtaining a warrant will justify a blood test without judi­
                 Cite as: 569 U. S. ____ (2013)           23

                     Opinion of the Court

cial authorization, for in every case the law must be con­
cerned that evidence is being destroyed. But that inquiry
ought not to be pursued here where the question is not
properly before this Court. Having rejected the sole ar­
gument presented to us challenging the Missouri Supreme
Court’s decision, we affirm its judgment.
                        *     *     *
  We hold that in drunk-driving investigations, the natu­
ral dissipation of alcohol in the bloodstream does not con-
stitute an exigency in every case sufficient to justify
conducting a blood test without a warrant.
  The judgment of the Missouri Supreme Court is
affirmed.
                                            It is so ordered.
                  Cite as: 569 U. S. ____ (2013)            1

                 KENNEDY, J., concurring in part

SUPREME COURT OF THE UNITED STATES
                          _________________

                          No. 11–1425
                          _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                      MISSOURI

                         [April 17, 2013] 


   JUSTICE KENNEDY, concurring in part.
   I join Parts I, II–A, II–B, and IV of the opinion for the
Court.
   For the reasons stated below this case does not call for
the Court to consider in detail the issue discussed in Part
II–C and the separate opinion by THE CHIEF JUSTICE.
   As to Part III, much that is noted with respect to the
statistical and survey data will be of relevance when this
issue is explored in later cases. The repeated insistence in
Part III that every case be determined by its own circum-
stances is correct, of course, as a general proposition; yet
it ought not to be interpreted to indicate this question is
not susceptible of rules and guidelines that can give im-
portant, practical instruction to arresting officers, in-
struction that in any number of instances would allow a
warrantless blood test in order to preserve the critical
evidence.
   States and other governmental entities which enforce
the driving laws can adopt rules, procedures, and protocols
that meet the reasonableness requirements of the Fourth
Amendment and give helpful guidance to law enforcement
officials. And this Court, in due course, may find it appro-
priate and necessary to consider a case permitting it to
provide more guidance than it undertakes to give today.
   As the opinion of the Court is correct to note, the instant
case, by reason of the way in which it was presented and
2                  MISSOURI v. MCNEELY

                KENNEDY, J., concurring in part

decided in the state courts, does not provide a framework
where it is prudent to hold any more than that always
dispensing with a warrant for a blood test when a driver is
arrested for being under the influence of alcohol is incon-
sistent with the Fourth Amendment.
                 Cite as: 569 U. S. ____ (2013)           1

                   Opinion of ROBERTS, C. J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 11–1425
                         _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                      MISSOURI


                        [April 17, 2013] 


   CHIEF JUSTICE ROBERTS, with whom JUSTICE BREYER
and JUSTICE ALITO join, concurring in part and dissenting
in part.
   A police officer reading this Court’s opinion would have
no idea—no idea—what the Fourth Amendment requires
of him, once he decides to obtain a blood sample from a
drunk driving suspect who has refused a breathalyzer
test. I have no quarrel with the Court’s “totality of the
circumstances” approach as a general matter; that is what
our cases require. But the circumstances in drunk driving
cases are often typical, and the Court should be able to
offer guidance on how police should handle cases like the
one before us.
   In my view, the proper rule is straightforward. Our
cases establish that there is an exigent circumstances
exception to the warrant requirement. That exception
applies when there is a compelling need to prevent the
imminent destruction of important evidence, and there is
no time to obtain a warrant. The natural dissipation of
alcohol in the bloodstream constitutes not only the immi-
nent but ongoing destruction of critical evidence. That
would qualify as an exigent circumstance, except that
there may be time to secure a warrant before blood can be
drawn. If there is, an officer must seek a warrant. If an
officer could reasonably conclude that there is not, the
exigent circumstances exception applies by its terms, and
2                  MISSOURI v. MCNEELY

                    Opinion of ROBERTS, C. J.

the blood may be drawn without a warrant.
                           I
    The Fourth Amendment provides:
     “The right of the people to be secure in their persons,
     houses, papers, and effects, against unreasonable
     searches and seizures, shall not be violated, and no
     Warrants shall issue, but upon probable cause, sup-
     ported by Oath or affirmation, and particularly de-
     scribing the place to be searched, and the persons or
     things to be seized.”
That language does not state that warrants are required
prior to searches, but this Court has long held that war-
rants must generally be obtained. See Kentucky v. King,
563 U. S. ___, ___ (2011) (slip op., at 5). We have also held
that bodily intrusions like blood draws constitute searches
and are subject to the warrant requirement.               See
Schmerber v. California, 384 U. S. 757, 767, 770 (1966).
   However, “the ultimate touchstone of the Fourth
Amendment is ‘reasonableness,’ ” Brigham City v. Stuart,
547 U. S. 398, 403 (2006), and thus “the warrant require-
ment is subject to certain reasonable exceptions,” King,
563 U. S., at ___ (slip op., at 6). One of those exceptions is
known as the “exigent circumstances exception,” which
“applies when the exigencies of the situation make the
needs of law enforcement so compelling that a warrantless
search is objectively reasonable under the Fourth
Amendment.” Ibid. (internal quotation marks and altera-
tions omitted).
   Within the exigent circumstances exception, we have
identified several sets of exigent circumstances excusing
the need for a warrant. For example, there is an emergency
aid exception to the warrant requirement. In Brigham
City, supra, at 403, we held that “law enforcement officers
may enter a home without a warrant to render emergency
                 Cite as: 569 U. S. ____ (2013)           3

                   Opinion of ROBERTS, C. J.

assistance to an injured occupant or to protect an occupant
from imminent injury.” There is also a fire exception to
the warrant requirement. In Michigan v. Tyler, 436 U. S.
499, 509 (1978), we held that “[a] burning building clearly
presents an exigency of sufficient proportions to render
a warrantless entry ‘reasonable.’ ” And there is a hot pur-
suit exception to the warrant requirement as well. In
United States v. Santana, 427 U. S. 38 (1976), and War-
den, Md. Penitentiary v. Hayden, 387 U. S. 294 (1967), we
recognized “the right of police, who had probable cause to
believe that an armed robber had entered a house a few
minutes before, to make a warrantless entry to arrest the
robber and to search for weapons.” Santana, supra, at 42.
In each of these cases, the requirement that we base our
decision on the “totality of the circumstances” has not
prevented us from spelling out a general rule for the police
to follow.
  The exigency exception most on point here is the one for
imminent destruction of evidence. We have affirmed on
several occasions that “law enforcement officers may make
a warrantless entry onto private property . . . to prevent
the imminent destruction of evidence.” Brigham City,
supra, at 403 (citing Ker v. California, 374 U. S. 23, 40
(1963) (plurality opinion)); see also, e.g., King, supra, at
___ (slip op., at 6). For example, in Ker, the police had
reason to believe that the defendant was in possession of
marijuana and was expecting police pursuit. We upheld
the officers’ warrantless entry into the defendant’s home,
with the plurality explaining that the drugs “could be
quickly and easily destroyed” or “distributed or hidden
before a warrant could be obtained at that time of night.”
374 U. S., at 40, 42.
  As an overarching principle, we have held that if there
is a “compelling need for official action and no time to
secure a warrant,” the warrant requirement may be ex-
4                  MISSOURI v. MCNEELY

                    Opinion of ROBERTS, C. J.

cused. Tyler, supra, at 509. The question here is whether
and how this principle applies in the typical case of a
police officer stopping a driver on suspicion of drunk
driving.
                                II

                                  

                                A

   The reasonable belief that critical evidence is being
destroyed gives rise to a compelling need for blood draws
in cases like this one. Here, in fact, there is not simply
a belief that any alcohol in the bloodstream will be de-
stroyed; it is a biological certainty. Alcohol dissipates from
the bloodstream at a rate of 0.01 percent to 0.025 percent
per hour. Stripp, Forensic and Clinical Issues in Alcohol
Analysis, in Forensic Chemistry Handbook 440 (L. Kobil-
insky ed. 2012). Evidence is literally disappearing by the
minute. That certainty makes this case an even stronger
one than usual for application of the exigent circumstances
exception.
   And that evidence is important. A serious and deadly
crime is at issue. According to the Department of Trans-
portation, in 2011, one person died every 53 minutes due
to drinking and driving. National Highway Traffic Safety
Admin. (NHTSA), Traffic Safety Facts, 2011 Data 1 (No.
811700, Dec. 2012). No surprise then that drinking and
driving is punished severely, including with jail time. See
generally Dept. of Justice, Bureau of Justice Statistics, L.
Maruschak, Special Report, DWI Offenders under Correc-
tional Supervision (1999). McNeely, for instance, faces up
to four years in prison. See App. 22–23 (citing Mo. Ann.
Stat. §§558.011, 577.010, 577.023 (West 2011)).
   Evidence of a driver’s blood alcohol concentration (BAC)
is crucial to obtain convictions for such crimes. All 50
States and the District of Columbia have laws providing
that it is per se illegal to drive with a BAC of 0.08 percent
or higher. Most States also have laws establishing addi-
                 Cite as: 569 U. S. ____ (2013)           5

                   Opinion of ROBERTS, C. J.

tional penalties for drivers who drive with a “high BAC,”
often defined as 0.15 percent or above. NHTSA, Digest
of Impaired Driving and Selected Beverage Control Laws,
pp. vii, x–xviii (No. 811673, Oct. 2012). BAC evidence
clearly matters. And when drivers refuse breathalyzers,
as McNeely did here, a blood draw becomes necessary to
obtain that evidence.
   The need to prevent the imminent destruction of BAC
evidence is no less compelling because the incriminating
alcohol dissipates over a limited period of time, rather
than all at once. As noted, the concentration of alcohol
 can make a difference not only between guilt and inno-
cence, but between different crimes and different degrees
of punishment. The officer is unlikely to know precisely
when the suspect consumed alcohol or how much; all he
knows is that critical evidence is being steadily lost. Fire
can spread gradually, but that does not lessen the need
and right of the officers to respond immediately. See
Tyler, supra.
   McNeely contends that there is no compelling need for a
warrantless blood draw, because if there is some alcohol
left in the blood by the time a warrant is obtained, the
State can use math and science to work backwards and
identify a defendant’s BAC at the time he was driving.
See Brief for Respondent 44–46. But that’s not good
enough. We have indicated that exigent circumstances
justify warrantless entry when drugs are about to be
flushed down the toilet. See, e.g., King, 563 U. S., at ___–
___ (slip op., at 7–8). We have not said that, because there
could well be drug paraphernalia elsewhere in the home,
or because a defendant’s co-conspirator might testify to
the amount of drugs involved, the drugs themselves are
not crucial and there is no compelling need for warrantless
entry.
   The same approach should govern here. There is a
6                       MISSOURI v. MCNEELY

                        Opinion of ROBERTS, C. J.

compelling need to search because alcohol—the nearly
conclusive evidence of a serious crime—is dissipating from
the bloodstream. The need is no less compelling because
the police might be able to acquire second-best evidence
some other way.1
                             B
  For exigent circumstances to justify a warrantless
search, however, there must also be “no time to secure a
warrant.” Tyler, 436 U. S., at 509; see Schmerber, 384
U. S., at 771 (warrantless search legal when “there was no
time to seek out a magistrate and secure a warrant”). In
this respect, obtaining a blood sample from a suspected
drunk driver differs from other exigent circumstances
cases.
  Importantly, there is typically delay between the mo-
ment a drunk driver is stopped and the time his blood can
be drawn. Drunk drivers often end up in an emergency
room, but they are not usually pulled over in front of one.
In most exigent circumstances situations, police are just
outside the door to a home. Inside, evidence is about to be
destroyed, a person is about to be injured, or a fire has
broken out. Police can enter promptly and must do so to
respond effectively to the emergency. But when police pull
a person over on suspicion of drinking and driving, they
cannot test his blood right away.2 There is a time-
——————
    1 Andthat second-best evidence may prove useless. When experts
have worked backwards to identify a defendant’s BAC at the time he
was driving, defense attorneys have objected to that evidence, courts
have at times rejected it, and juries may be suspicious of it. See, e.g., 1
D. Nichols & F. Whited, Drinking/Driving Litigation §2:9, pp. 2–130 to
2–137 (2d ed. 2006) (noting counsel objections to such evidence); State
v. Eighth Judicial District Court, 127 Nev. ___, 267 P. 3d 777 (2011)
(affirming rejection of such evidence); L. Taylor & S. Oberman, Drunk
Driving Defense §6.03 (7th ed. 2010) (describing ways to undermine
such evidence before a jury).
  2 This case involves medical personnel drawing blood at a medical
                     Cite as: 569 U. S. ____ (2013)                   7

                       Opinion of ROBERTS, C. J.

consuming obstacle to their search, in the form of a trip
to the hospital and perhaps a wait to see a medical pro-
fessional. In this case, for example, approximately 25
minutes elapsed between the time the police stopped
McNeely and the time his blood was drawn. App. 36, 38.
  As noted, the fact that alcohol dissipates gradually from
the bloodstream does not diminish the compelling need for
a search—critical evidence is still disappearing. But the
fact that the dissipation persists for some time means that
the police—although they may not be able to do anything
about it right away—may still be able to respond to the
ongoing destruction of evidence later on.
  There might, therefore, be time to obtain a warrant in
many cases. As the Court explains, police can often re-
quest warrants rather quickly these days. At least 30
States provide for electronic warrant applications. See
ante, at 10–12, and n. 4. In many States, a police officer
can call a judge, convey the necessary information, and be
authorized to affix the judge’s signature to a warrant.
See, e.g., Ala. Rule Crim. Proc. 3.8(b) (2012–2013); Alaska
Stat. §12.35.015 (2012); Idaho Code §§19–4404, 19–4406
(Lexis 2004); Minn. Rules Crim. Proc. 36.01–36.08 (2010
and Supp. 2013); Mont. Code Ann. §46–5–222 (2012); see
——————
facility, not police officers doing so by the side of the road. See
Schmerber v. California, 384 U. S. 757, 771–772 (1966) (“Petitioner’s
blood was taken by a physician in a hospital environment according to
accepted medical practices. We are thus not presented with the serious
questions which would arise if a search involving use of a medical
technique, even of the most rudimentary sort, were made by other than
medical personnel or in other than a medical environment—for exam-
ple, if it were administered by police in the privacy of the station-
house”); Brief for Respondent 53, and n. 21 (describing roadside blood
draws in Arizona). A plurality of the Court suggests that my approach
could make roadside blood draws a more attractive option for police,
but such a procedure would pose practical difficulties and, as the Court
noted in Schmerber, would raise additional and serious Fourth
Amendment concerns. See ante, at 14–15.
8                  MISSOURI v. MCNEELY

                   Opinion of ROBERTS, C. J.

generally NHTSA, Use of Warrants for Breath Test Re-
fusal: Case Studies 6–32 (No. 810852, Oct. 2007) (overview
of procedures in Arizona, Michigan, Oregon, and Utah).
Utah has an e-warrant procedure where a police officer
enters information into a system, the system notifies
a prosecutor, and upon approval the officer forwards
the information to a magistrate, who can electronically re-
turn a warrant to the officer. Utah, e-Warrants: Cross
Boundary Collaboration 1 (2008). Judges have been known
to issue warrants in as little as five minutes. Bergreen,
Faster Warrant System Hailed, Salt Lake Tribune, Dec.
26, 2008, p. B1, col. 1. And in one county in Kansas, police
officers can e-mail warrant requests to judges’ iPads;
judges have signed such warrants and e-mailed them back
to officers in less than 15 minutes. Benefiel, DUI Search
Warrants: Prosecuting DUI Refusals, 9 Kansas Prosecutor
17, 18 (Spring 2012). The police are presumably familiar
with the mechanics and time involved in the warrant
process in their particular jurisdiction.
                              III

                                 

                               A

  In a case such as this, applying the exigent circum-
stances exception to the general warrant requirement of
the Fourth Amendment seems straightforward: If there is
time to secure a warrant before blood can be drawn, the
police must seek one. If an officer could reasonably con-
clude that there is not sufficient time to seek and receive a
warrant, or he applies for one but does not receive a re-
sponse before blood can be drawn, a warrantless blood
draw may ensue. See Tyler, supra, at 509; see also Illinois
v. Rodriguez, 497 U. S. 177, 185–186 (1990) (“in order to
satisfy the ‘reasonableness’ requirement of the Fourth
Amendment, what is generally demanded of the many
factual determinations that must regularly be made by . . .
police officer[s] conducting a search or seizure under one of
                 Cite as: 569 U. S. ____ (2013)            9

                   Opinion of ROBERTS, C. J.

the exceptions to the warrant requirement . . . is not that
they always be correct, but that they always be reasona-
ble”); Terry v. Ohio, 392 U. S. 1, 20 (1968) (“police must,
whenever practicable, obtain advance judicial approval of
searches and seizures through the warrant procedure”).
   Requiring police to apply for a warrant if practicable
increases the likelihood that a neutral, detached judicial
officer will review the case, helping to ensure that there is
probable cause for any search and that any search is
reasonable. We have already held that forced blood draws
can be constitutional—that such searches can be reasonable—
but that does not change the fact that they are significant
bodily intrusions. See Schmerber, 384 U. S., at 770 (up-
holding a warrantless forced blood draw but noting the
“importance of informed, detached and deliberate deter-
minations of the issue whether or not to invade another’s
body in search of evidence of guilt” as “indisputable and
great”). Requiring a warrant whenever practicable helps
ensure that when blood draws occur, they are indeed
justified.
   At the same time, permitting the police to act without a
warrant to prevent the imminent destruction of evidence
is well established in Fourth Amendment law. There is no
reason to preclude application of that exception in drunk
driving cases simply because it may take the police some
time to be able to respond to the undoubted destruction of
evidence, or because the destruction occurs continuously
over an uncertain period.
   And that is so even in situations where police have
requested a warrant but do not receive a timely response.
An officer who reasonably concluded there was no time to
secure a warrant may have blood drawn from a suspect
upon arrival at a medical facility. There is no reason an
officer should be in a worse position, simply because he
sought a warrant prior to his arrival at the hospital.
10                 MISSOURI v. MCNEELY

                   Opinion of ROBERTS, C. J.

                             B
   The Court resists the foregoing, contending that the
question presented somehow inhibits such a focused anal-
ysis in this case. See ante, at 20–23. It does not. The
question presented is whether a warrantless blood draw is
permissible under the Fourth Amendment “based upon
the natural dissipation of alcohol in the bloodstream.”
Pet. for Cert. i. The majority answers “It depends,” and
so do I. The difference is that the majority offers no ad-
ditional guidance, merely instructing courts and police
officers to consider the totality of the circumstances. I
believe more meaningful guidance can be provided about
how to handle the typical cases, and nothing about the
question presented prohibits affording that guidance.
   A plurality of the Court also expresses concern that my
approach will discourage state and local efforts to expedite
the warrant application process. See ante, at 14. That is
not plausible: Police and prosecutors need warrants in a
wide variety of situations, and often need them quickly.
They certainly would not prefer a slower process, just
because that might obviate the need to ask for a warrant
in the occasional drunk driving case in which a blood draw
is necessary. The plurality’s suggestion also overlooks the
interest of law enforcement in the protection a warrant
provides.
   The Court is correct when it says that every case must
be considered on its particular facts. But the pertinent
facts in drunk driving cases are often the same, and the
police should know how to act in recurring factual situa-
tions. Simply put, when a drunk driving suspect fails field
sobriety tests and refuses a breathalyzer, whether a war-
rant is required for a blood draw should come down to
whether there is time to secure one.
   Schmerber itself provides support for such an analysis.
The Court there made much of the fact that “there was no
                 Cite as: 569 U. S. ____ (2013)         11

                   Opinion of ROBERTS, C. J.

time to seek out a magistrate and secure a warrant.” 384
U. S., at 771. It did so in an era when cell phones and
e-mail were unknown. It follows quite naturally that if
cell phones and e-mail mean that there is time to contact
a magistrate and secure a warrant, that must be done. At
the same time, there is no need to jettison the well-
established exception for the imminent destruction of
evidence, when the officers are in a position to do some-
thing about it.
                        *    *    *
  Because the Missouri courts did not apply the rule I
describe above, and because this Court should not do so in
the first instance, I would vacate and remand for further
proceedings in the Missouri courts.
                 Cite as: 569 U. S. ____ (2013)            1

                    THOMAS, J., dissenting

SUPREME COURT OF THE UNITED STATES
                         _________________

                         No. 11–1425
                         _________________


   MISSOURI, PETITIONER v. TYLER G. MCNEELY
    ON WRIT OF CERTIORARI TO THE SUPREME COURT OF 

                      MISSOURI


                        [April 17, 2013] 


  JUSTICE THOMAS, dissenting.
  This case requires the Court to decide whether the
Fourth Amendment prohibits an officer from obtaining a
blood sample without a warrant when there is probable
cause to believe that a suspect has been driving under the
influence of alcohol. Because the body’s natural meta­
bolization of alcohol inevitably destroys evidence of the
crime, it constitutes an exigent circumstance. As a result, I
would hold that a warrantless blood draw does not violate
the Fourth Amendment.
                             I

                             A

  The Fourth Amendment states that “[t]he right of the
people to be secure in their persons . . . against unreason­
able searches and seizures, shall not be violated, and no
Warrants shall issue, but upon probable cause.” Before a
search occurs, “a warrant must generally be secured,”
Kentucky v. King, 563 U. S. ___, ___ (2011) (slip op., at 5),
but “this presumption may be overcome in some circum­
stances because ‘[t]he ultimate touchstone of the Fourth
Amendment is “reasonableness.” ’ ” Ibid. (quoting Brig­
ham City v. Stuart, 547 U. S. 398, 403 (2006); alteration
in original).
  The presence of “exigent circumstances” is one such
exception to the warrant requirement. Exigency applies
2                  MISSOURI v. MCNEELY

                     THOMAS, J., dissenting

when “ ‘the needs of law enforcement [are] so compelling
that [a] warrantless search is objectively reasonable under
the Fourth Amendment.’ ” 563 U. S., at ___ (slip op., at 6)
(quoting Mincey v. Arizona, 437 U. S. 385, 394 (1978);
second alteration in original). Thus, when exigent circum­
stances are present, officers may take actions that would
typically require a warrant, such as entering a home in
hot pursuit of a fleeing suspect. 563 U. S., at ___ (slip op.,
at 6). As relevant in this case, officers may also conduct
a warrantless search when they have probable cause to
believe that failure to act would result in “ ‘imminent
destruction of evidence.’ ” Ibid. (quoting Brigham City,
supra, at 403).
                              B
   Once police arrest a suspect for drunk driving, each
passing minute eliminates probative evidence of the crime.
The human liver eliminates alcohol from the bloodstream
at a rate of approximately 0.015 percent to 0.020 percent
per hour, ante, at 8, with some heavy drinkers as high as
0.022 percent per hour, Brief for Petitioner 21 (citing
medical studies), depending on, among other things, a per-
son’s sex, weight, body type, and drinking history. Ante,
at 8–9; Brief for United States as Amicus Curiae 23.
The Court has acknowledged this fact since Schmerber v.
California, 384 U. S. 757, 770 (1966) (“We are told that the
percentage of alcohol in the blood begins to diminish shortly
after drinking stops, as the body functions to eliminate
it from the system”). In that case, the Court recognized
that destruction of evidence is inherent in drunk-driving
cases and held that an officer investigating a drunk­
driving crime “might reasonably [believe] that he [is]
confronted with an emergency, in which the delay neces­
sary to obtain a warrant, under the circumstances, threat­
en[s] ‘the destruction of evidence.’ ” Ibid. (quoting Preston
v. United States, 376 U. S. 364, 367 (1964)). The Court
                    Cite as: 569 U. S. ____ (2013)                   3

                        THOMAS, J., dissenting

explained that drawing a person’s blood is “a highly ef-
fective means of determining the degree to which [he] is
under the influence of alcohol” and is a reasonable proce­
dure because blood tests are “commonplace” and “involv[e]
virtually no risk, trauma, or pain.”1 384 U. S., at 771. The
Court, therefore, held that dissipation of alcohol in the
blood constitutes an exigency that allows a blood draw
without a warrant.
   The rapid destruction of evidence acknowledged by the
parties, the majority, and Schmerber’s exigency determi­
nation occurs in every situation where police have probable
cause to arrest a drunk driver. In turn, that destruction
of evidence implicates the exigent-circumstances doctrine.
See Cupp v. Murphy, 412 U. S. 291 (1973). In Cupp,
officers questioning a murder suspect observed a spot on
the suspect’s finger that they believed might be dried
blood. Id., at 292. After the suspect began making obvi­
ous efforts to remove the spots from his hands, the officers
took samples without obtaining either his consent or a
warrant. Id., at 296. Following a Fourth Amendment
challenge to this search, the Court held that the “ready
destructibility of the evidence” and the suspect’s observed
efforts to destroy it “justified the police in subjecting him
to the very limited search necessary to preserve the highly
evanescent evidence they found under his fingernails.”
Ibid.
   In this case, a similar exigency is present. Just as the
suspect’s efforts to destroy “highly evanescent evidence”
gave rise to the exigency in Cupp, the natural metaboliza­
tion of blood alcohol concentration (BAC) creates an exi­
gency once police have probable cause to believe the driver

——————
  1 Neither party has challenged this determination, which this Court
has reaffirmed several times. See, e.g., Skinner v. Railway Labor
Executives’ Assn., 489 U. S. 602, 625 (1989); Winston v. Lee, 470 U. S.
753, 761–763 (1985).
4                  MISSOURI v. MCNEELY

                    THOMAS, J., dissenting

is drunk. It naturally follows that police may conduct a
search in these circumstances.
   A hypothetical involving classic exigent circumstances
further illustrates the point. Officers are watching a
warehouse and observe a worker carrying bundles from
the warehouse to a large bonfire and throwing them into
the blaze. The officers have probable cause to believe
the bundles contain marijuana. Because there is only one
person carrying the bundles, the officers believe it will
take hours to completely destroy the drugs. During that
time the officers likely could obtain a warrant. But it is
clear that the officers need not sit idly by and watch the
destruction of evidence while they wait for a warrant. The
fact that it will take time for the evidence to be destroyed
and that some evidence may remain by the time the offi­
cers secure a warrant are not relevant to the exigency.
However, the ever-diminishing quantity of drugs may
have an impact on the severity of the crime and the
length of the sentence. See, e.g., 21 U. S. C. §841(b)(1)(D)
(lower penalties for less than 50 kilograms of marijuana);
United States Sentencing Commission, Guidelines Manual
§2D1.1(c) (Nov. 2012) (drug quantity table tying base
offense level to drug amounts). Conducting a warrantless
search of the warehouse in this situation would be entirely
reasonable.
   The same obtains in the drunk-driving context. Just
because it will take time for the evidence to be completely
destroyed does not mean there is no exigency. Congress
has conditioned federal highway grants on states’ adoption
of laws penalizing the operation of a motor vehicle “with a
blood alcohol concentration of 0.08 percent or greater.” 23
U. S. C. §163(a). See also 23 CFR §1225.1 (2012). All 50
States have acceded to this condition. National Highway
Traffic Safety Admin. (NHTSA), Alcohol and Highway
Safety: A Review of the State of Knowledge 167 (No.
811374, Mar. 2011) (NHTSA State Review); Mo. Ann.
                 Cite as: 569 U. S. ____ (2013)           5

                    THOMAS, J., dissenting

Stat. §§577.012(1)–(2) (West 2011) (establishing Missouri’s
0.08 percent BAC standard). Moreover, as of 2005, 32
States and the District of Columbia imposed additional
penalties for BAC levels of 0.15 percent or higher. NHTSA
State Review 175. Missouri is one such State. See, e.g.,
Mo. Stat. Ann. §§577.010(3)–(4), 577.012(4)–(5) (suspended
sentence unavailable even for first offenders with BAC
above 0.15 percent unless they complete drug treatment;
mandatory jail time if treatment is not completed). As a
result, the level of intoxication directly bears on enforce­
ment of these laws. Nothing in the Fourth Amendment
requires officers to allow evidence essential to enforcement
of drunk-driving laws to be destroyed while they wait for a
warrant to issue.
                              II
  In today’s decision, the Court elides the certainty of
evidence destruction in drunk-driving cases and focuses
primarily on the time necessary for destruction. In doing
so, it turns the exigency inquiry into a question about the
amount of evidentiary destruction police must permit
before they may act without a warrant. That inquiry is
inconsistent with the actual exigency at issue: the un­
contested destruction of evidence due to metabolization of
alcohol. See Part I, supra. Moreover, the Court’s facts­
and-circumstances analysis will be difficult to administer,
a particularly important concern in the Fourth Amend­
ment context.
  The Court’s judgment reflects nothing more than a
vague notion that everything will come out right most of
the time so long as the delay is not too lengthy. Ante, at
12 (justifying delays in part because “BAC evidence is lost
gradually and relatively predictably”); ante, at 10 (same,
quoting Brief for Petitioner 27). But hard percentage lines
have meaningful legal consequences in the drunk-driving
context. The fact that police will be able to retrieve some
6                   MISSOURI v. MCNEELY

                     THOMAS, J., dissenting

evidence before it is all destroyed is simply not relevant to
the exigency inquiry.
   The majority believes that, absent special facts and
circumstances, some destruction of evidence is acceptable.
See ante, at 9 (“sufficient for our purposes to note that . . .
significant delay in testing will negatively affect the pro­
bative value” (emphasis added)). This belief must rest
on the assumption that whatever evidence remains once a
warrant is obtained will be sufficient to prosecute the
suspect. But that assumption is clearly wrong. Suspects’
initial levels of intoxication and the time necessary to
obtain warranted blood draws will vary widely from case
to case. Even a slight delay may significantly affect pro­
bative value in borderline cases of suspects who are mod­
erately intoxicated or suspects whose BAC is near a statu­
tory threshold that triggers a more serious offense. See
supra, at 4–5 (discussing laws penalizing heightened BAC
levels). Similarly, the time to obtain a warrant can be ex­
pected to vary, and there is no reason to believe it will
do so in a predictable fashion.
   Further, the Court nowhere explains how an officer in
the field is to apply the facts-and-circumstances test it
adopts. First, officers do not have the facts needed to
assess how much time can pass before too little evidence
remains. They will never know how intoxicated a suspect
is at the time of arrest. Otherwise, there would be no need
for testing. Second, they will not know how long it will
take to roust a magistrate from his bed, reach the hospital,
or obtain a blood sample once there. As the Minnesota
Supreme Court recognized in rejecting arguments like
those adopted by the Court today:
    “[T]he officer has no control over how long it would
    take to travel to a judge or the judge’s availability.
    The officer also may not know the time of the sus­
    pect’s last drink, the amount of alcohol consumed, or
                     Cite as: 569 U. S. ____ (2013)                     7

                         THOMAS, J., dissenting

     the rate at which the suspect will metabolize alcohol.
     Finally, an officer cannot know how long it will take to
     obtain the blood sample once the suspect is brought
     to the hospital. Under a totality of the circumstances
     test, an officer would be called upon to speculate on
     each of these considerations and predict how long the
     most probative evidence of the defendant’s blood­
     alcohol level would continue to exist before a blood
     sample was no longer reliable.” State v. Shriner, 751
     N. W. 2d 538, 549 (2008) (footnote omitted).
The Court should not adopt a rule that requires police to
guess whether they will be able to obtain a warrant before
“too much” evidence is destroyed, for the police lack reli-
able information concerning the relevant variables.2
   This case demonstrates the uncertainty officers face
with regard to the delay caused by obtaining a warrant.
The arresting officer clearly had probable cause to believe
respondent was drunk, but there was no way for the of­
ficer to quantify the level of intoxication to determine how
quickly he needed to act in order to obtain probative evi­
dence. Another officer testified at respondent’s trial that
it typically took 1 ½ to 2 hours to obtain a drunk-driving
warrant at night in Cape Girardeau County, Missouri.
See App. 53–54. Respondent submitted an exhibit sum­
marizing six late afternoon and nighttime drunk-driving
search warrants that suggests the time may be shorter.
——————
  2 Because the Court’s position is likely to result in delay in obtaining

BAC evidence, it also increases the likelihood that prosecutors will be
forced to estimate the amount of alcohol in a defendant’s bloodstream
using BAC numbers obtained hours later. In practice, this backwards
extrapolation is likely to devolve into a battle of the experts, as each
side seeks to show that stale evidence supports its position. There is no
need for this outcome. Police facing inevitable destruction situations
need not forgo collecting the most accurate available evidence simply
because they might be able to use an expert witness and less persuasive
evidence to approximate what they lost.
8                    MISSOURI v. MCNEELY

                       THOMAS, J., dissenting

Brief for Respondent 56; App. 70. Ultimately this factual
tiff is beside the point; the spotty evidence regarding
timing itself illustrates the fact that delays in obtaining
warrants are unpredictable and potentially lengthy. A
rule that requires officers (and ultimately courts) to bal­
ance transportation delays, hospital availability, and ac-
cess to magistrates is not a workable rule for cases where
natural processes inevitably destroy the evidence with
every passing minute.
   The availability of telephonic warrant applications is
not an answer to this conundrum. See ante, at 10–12,
and n. 4. For one thing, Missouri still requires written
warrant applications and affidavits, Mo. Ann. Stat.
§§542.276.2(1), 542.276.2.3 (West Supp. 2012), rendering
the Court’s 50-State survey irrelevant to the actual dispo­
sition of this case. Ante, at 11, n. 4. But even if telephonic
applications were available in Missouri, the same difficul­
ties would arise. As the majority correctly recognizes,
“[w]arrants inevitably take some time for police officers
or prosecutors to complete and for magistrate judges to
review.” Ante, at 12. During that time, evidence is de­
stroyed, and police who have probable cause to believe a
crime has been committed should not have to guess how
long it will take to secure a warrant.

                          *    *    * 

    For the foregoing reasons, I respectfully dissent. 


```

---

## GROUP: content/cases/Missouri v. Seibert.md  (`case`, 5 assertions)

### content_page

```
---
title: "Missouri v. Seibert"
type: case
citation: "542 U.S. 600 (2004)"
parallel_cite: "124 S. Ct. 2601; 159 L. Ed. 2d 643"
neutral_cite: 2004 U.S. LEXIS 4578
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-06-28
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2004-06-28
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Missouri v. Seibert
  varies_by_point: false
  scope_note: "Plurality opinion; Justice Kennedy's concurrence in the judgment is generally treated as controlling."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/137002/missouri-v-seibert/"
  cluster_id: 137002
  opinion_id: 137002
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Oregon v. Elstad]]", "[[Miranda v. Arizona]]", "[[Dickerson v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "two-step", "question-first", "waiver"]
holding: "A deliberate \"question-first, warn-later\" two-step interrogation is invalid."
lake:
  record_id: Missouri v. Seibert
  status: verified
  projected_at: 2026-07-06
---

# Missouri v. Seibert

*542 U.S. 600 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Following a deliberate department protocol, officers interrogated Seibert without *[[Miranda v. Arizona|Miranda]]* warnings until she confessed to involvement in a fire that killed a man, then gave her the warnings and led her to repeat the same confession. Both statements were obtained in a single, continuous interrogation.

## Issue
Whether a confession repeated after *[[Miranda v. Arizona|Miranda]]* warnings is admissible when officers deliberately used a two-step "question-first, warn-later" interrogation technique.

## Rule
No (plurality). "Because this midstream recitation of warnings after interrogation and unwarned confession could not effectively comply with *Miranda*'s constitutional requirement, we hold that a statement repeated after a warning in such circumstances is inadmissible." — 542 U.S. at 604 (plurality opinion). ^pin-604

Justice Kennedy, concurring in the judgment on the narrower ground generally treated as controlling, would suppress the postwarning statement where a two-step interrogation was used deliberately to undermine *[[Miranda v. Arizona|Miranda]]*, unless curative measures were taken.

## Application
The officers here followed a deliberate protocol of questioning Seibert until she confessed and only then administering the warnings before having her repeat the confession. Because the midstream warnings came only after she had already confessed under unwarned interrogation, they could not function effectively, and her repeated, postwarning confession was inadmissible.

## Conclusion
Affirmed; the postwarning statement was suppressed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Kennedy's concurrence controlling).
- No negative treatment. *Seibert* is distinguished from the good-faith, non-deliberate two-step sequence approved in [[Oregon v. Elstad]].

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Progeny / Refinement*

## Sources
- *Missouri v. Seibert*, 542 U.S. 600 (2004) — https://www.courtlistener.com/opinion/137002/missouri-v-seibert/ — pinpoint: 604 (plurality opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "966ab7deb0c24d1d", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "542 U.S. 600 (2004)", "court": "U.S. Supreme Court", "neutral_cite": "2004 U.S. LEXIS 4578", "official_citation_present": true, "parallel_cite": "124 S. Ct. 2601; 159 L. Ed. 2d 643", "title": "Missouri v. Seibert", "year": "2004"}}
{"assertion_id": "2b33569b09a13ed8", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Progeny / Refinement", "title": "Missouri v. Seibert"}}
{"assertion_id": "aeb6288a3e363246", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A deliberate \\\"question-first, warn-later\\\" two-step interrogation is invalid.", "title": "Missouri v. Seibert"}}
{"assertion_id": "bf312f1cfa5142fc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Missouri v. Seibert"}}
{"assertion_id": "cd4e1bb8442f5758", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2004-06-28", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Missouri v. Seibert", "field_i_validity": "good_law", "scope_note": "Plurality opinion; Justice Kennedy's concurrence in the judgment is generally treated as controlling.", "title": "Missouri v. Seibert", "varies_by_point": "false"}}
```

### lake record — Missouri v. Seibert

```json
{
  "schema_version": "s2.v1",
  "record_id": "Missouri v. Seibert",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Missouri v. Seibert",
    "case_name_short": "Seibert",
    "case_name_full": "Missouri v. Seibert",
    "input_case_name": "Missouri v. Seibert",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-06-28",
    "year": 2004,
    "docket": null,
    "cluster_id": 137002,
    "lead_opinion_id": 137002,
    "sibling_ids": [
      137002,
      9434682,
      9434683,
      9434684,
      9434685
    ],
    "absolute_url": "/opinion/137002/missouri-v-seibert/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "542 U.S. 600",
      "volume": "542",
      "reporter": "U.S.",
      "page": "600",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 2601",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 643",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 4578",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "542 U.S. 600",
        "volume": "542",
        "reporter": "U.S.",
        "page": "600",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2601",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2601",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "159 L. Ed. 2d 643",
        "volume": "159",
        "reporter": "L. Ed. 2d",
        "page": "643",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 4578",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "4578",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "542 U.S. 600",
    "official_selection": {
      "court_class": "scotus",
      "selected": "542 U.S. 600",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-604",
      "page": null,
      "quote": "interrogation technique. ## Rule No (plurality).",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2004-06-28",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Missouri v. Seibert",
    "varies_by_point": false,
    "scope_note": "Plurality opinion; Justice Kennedy's concurrence in the judgment is generally treated as controlling.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Yaeger",
          "cluster_id": 10134256,
          "cite": [
            "311 Or. App. 626",
            "492 P.3d 668"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chhay Lim",
          "cluster_id": 4522500,
          "cite": [
            "897 F.3d 673"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Abbott",
          "cluster_id": 10366844,
          "cite": [
            "303 Ga. 297"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Kasey A. Smith",
          "cluster_id": 4442984,
          "cite": [
            "162 Idaho 878",
            "406 P.3d 890"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Phillips v. People",
          "cluster_id": 4636609,
          "cite": [
            "2019 CO 72",
            "443 P.3d 1016"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Williams",
          "cluster_id": 1801669,
          "cite": [
            "49 Cal. 4th 405",
            "2010 D.A.R. 10",
            "111 Cal. Rptr. 3d 589",
            "233 P.3d 1000",
            "2010 Cal. LEXIS 5970"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
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
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lam Thanh Nguyen",
          "cluster_id": 2827119,
          "cite": [
            "61 Cal. 4th 1015",
            "354 P.3d 90",
            "191 Cal. Rptr. 3d 182",
            "2015 Cal. LEXIS 5407"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hale",
          "cluster_id": 6897940,
          "cite": [
            "119 Ohio St. 3d 118",
            "892 N.E.2d 864"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Leger",
          "cluster_id": 1592017,
          "cite": [
            "936 So. 2d 108",
            "2006 WL 1883421"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Scott",
          "cluster_id": 844257,
          "cite": [
            "257 P.3d 703",
            "52 Cal. 4th 452",
            "129 Cal. Rptr. 3d 91",
            "2011 Cal. LEXIS 8086"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. San Nicolas",
          "cluster_id": 2507905,
          "cite": [
            "101 P.3d 509",
            "21 Cal. Rptr. 3d 612",
            "34 Cal. 4th 614",
            "2004 Daily Journal DAR 14410",
            "2004 Cal. Daily Op. Serv. 10643",
            "2004 Cal. LEXIS 11655"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bobby v. Dixon",
          "cluster_id": 616807,
          "cite": [
            "181 L. Ed. 2d 328",
            "132 S. Ct. 26",
            "565 U.S. 23",
            "2011 U.S. LEXIS 7926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Meier Jason Brown",
          "cluster_id": 77264,
          "cite": [
            "441 F.3d 1330",
            "69 Fed. R. Serv. 738",
            "2006 U.S. App. LEXIS 6052",
            "2006 WL 587875"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Eichinger",
          "cluster_id": 2091853,
          "cite": [
            "915 A.2d 1122",
            "591 Pa. 1",
            "2007 Pa. LEXIS 357"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Paulman",
          "cluster_id": 2021621,
          "cite": [
            "833 N.E.2d 239",
            "5 N.Y.3d 122",
            "800 N.Y.S.2d 96",
            "2005 NY Slip Op 5452",
            "2005 N.Y. LEXIS 1459"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Tashiri Wayne Williams",
          "cluster_id": 793121,
          "cite": [
            "435 F.3d 1148",
            "2006 U.S. App. LEXIS 2235",
            "2006 WL 213852"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Lopez",
          "cluster_id": 2060903,
          "cite": [
            "892 N.E.2d 1047",
            "229 Ill. 2d 322",
            "323 Ill. Dec. 55",
            "2008 Ill. LEXIS 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Unkart, Rodney Gale",
          "cluster_id": 2948085,
          "cite": [
            "400 S.W.3d 94",
            "2013 WL 2419497",
            "2013 Tex. Crim. App. LEXIS 818"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hoffner v. Bradshaw",
          "cluster_id": 175794,
          "cite": [
            "622 F.3d 487",
            "2010 U.S. App. LEXIS 19747",
            "2010 WL 3724790"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Blank",
          "cluster_id": 1620393,
          "cite": [
            "955 So. 2d 90",
            "2007 WL 1108842"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Hillary Lee Tyler",
          "cluster_id": 2812907,
          "cite": [
            "867 N.W.2d 136",
            "2015 Iowa Sup. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Caro",
          "cluster_id": 4629272,
          "cite": [
            "248 Cal. Rptr. 3d 96",
            "7 Cal. 5th 463",
            "442 P.3d 316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Antonio Rodriguez-Preciado, AKA Tony Rodriguez-Preciado",
          "cluster_id": 789441,
          "cite": [
            "399 F.3d 1118",
            "2005 U.S. App. LEXIS 3634",
            "2005 WL 502860"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Antwion Thompson v. D. Runnel",
          "cluster_id": 815924,
          "cite": [
            "705 F.3d 1089",
            "2013 WL 263909",
            "2013 U.S. App. LEXIS 1585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Stanley Street",
          "cluster_id": 77537,
          "cite": [
            "472 F.3d 1298",
            "2006 WL 3734533"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicole Harris v. Sheryl Thompson",
          "cluster_id": 810477,
          "cite": [
            "698 F.3d 609",
            "2012 WL 4944325",
            "2012 U.S. App. LEXIS 21727"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Knapp",
          "cluster_id": 1713730,
          "cite": [
            "2005 WI 127",
            "700 N.W.2d 899",
            "285 Wis. 2d 86",
            "2005 Wisc. LEXIS 395"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Dupree",
          "cluster_id": 3192634,
          "cite": [
            "304 Kan. 43",
            "371 P.3d 862",
            "2016 WL 1391917",
            "2016 Kan. LEXIS 154"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Missouri v. Seibert:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDQzNDg0ODAwMDAwJnM9MzAwNTU4NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28137002+OR+9434682+OR+9434683+OR+9434684+OR+9434685%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05OSZzPTc5ODA2MyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28137002+OR+9434682+OR+9434683+OR+9434684+OR+9434685%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685)",
        "reviewed": 42,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 42,
        "triage_read": 0,
        "triage_snippet_classified": 42
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(137002 OR 9434682 OR 9434683 OR 9434684 OR 9434685)",
    "indexed_citing_opinions": 863,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 137002,
        "count": 742,
        "count_source": "search"
      },
      {
        "opinion_id": 9434682,
        "count": 130,
        "count_source": "search"
      },
      {
        "opinion_id": 9434683,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434684,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434685,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1541,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/missouri-v-seibert.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4OTUxNTMmcz0xMDU4MTUwNyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28137002+OR+9434682+OR+9434683+OR+9434684+OR+9434685%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 137002,
        "cited_id": 102604,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 107577,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 107913,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 108272,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 108429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 110556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 110760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111204,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 112322,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 118036,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 118380,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 127927,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 198872,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 528515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 575188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 583447,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 766929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 775079,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 1173989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 1378981,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 1890935,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 2499246,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 137002,
        "cited_id": 2588587,
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
    "date_created": "2026-07-05T14:17:00Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:17:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:17:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:21:07Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:17:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Missouri v. Seibert

```
<div>
<center><b><span class="citation" data-id="9434682"><a href="/opinion/137002/missouri-v-seibert/" aria-description="Citation for case: Missouri v. Seibert">542 U.S. 600</a></span> (2004)</b></center>
<center><h1>MISSOURI<br>
v.<br>
SEIBERT.</h1></center>
<center>No. 02-1371.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued December 9, 2003.</center>
<center>Decided June 28, 2004.</center>
CERTIORARI TO THE SUPREME COURT OF MISSOURI.
<p><span class="star-pagination">*601</span> <span class="star-pagination">*602</span> <span class="star-pagination">*603</span> SOUTER, J., announced the judgment of the Court and delivered an opinion, in which STEVENS, GINSBURG, and BREYER, JJ., joined. BREYER, J., filed a concurring opinion, <i>post,</i> p. 617. KENNEDY, J., filed an opinion concurring in the judgment, <i>post,</i> p. 618. O'CONNOR, J., filed a dissenting opinion, in which REHNQUIST, C. J., and SCALIA and THOMAS, JJ., joined, <i>post,</i> p. 622.</p>
<p><i>Karen K. Mitchell,</i> Chief Deputy Attorney General of Missouri, argued the cause for petitioner. With her on the briefs were <i>Jeremiah W. (Jay) Nixon,</i> Attorney General, <i>James R. Layton,</i> State Solicitor, and <i>Shaun J. Mackelprang</i> and <i>Karen P. Hess,</i> Assistant Attorneys General.</p>
<p><i>Irving L. Gornstein</i> argued the cause for the United States as <i>amicus curiae</i> urging reversal. With him on the brief were <i>Solicitor General Olson, Acting Assistant Attorney General Wray, Deputy Solicitor General Dreeben,</i> and <i>Jonathan L. Marcus.</i></p>
<p><i>Amy M. Bartholow</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p><span class="star-pagination">*604</span> JUSTICE SOUTER announced the judgment of the Court and delivered an opinion, in which JUSTICE STEVENS, JUSTICE GINSBURG, and JUSTICE BREYER join.</p>
<p>This case tests a police protocol for custodial interrogation that calls for giving no warnings of the rights to silence and counsel until interrogation has produced a confession. Although such a statement is generally inadmissible, since taken in violation of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the interrogating officer follows it with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and then leads the suspect to cover the same ground a second time. The question here is the admissibility of the repeated statement. Because this midstream recitation of warnings after interrogation and unwarned confession could not effectively comply with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s constitutional requirement, we hold that a statement repeated after a warning in such circumstances is inadmissible.</p>
<p></p>
<h2>I</h2>
<p>Respondent Patrice Seibert's 12-year-old son Jonathan had cerebral palsy, and when he died in his sleep she feared charges of neglect because of bedsores on his body. In her presence, two of her teenage sons and two of their friends devised a plan to conceal the facts surrounding Jonathan's death by incinerating his body in the course of burning the family's mobile home, in which they planned to leave Donald Rector, a mentally ill teenager living with the family, to avoid any appearance that Jonathan had been unattended. Seibert's son Darian and a friend set the fire, and Donald died.</p>
<p>Five days later, the police awakened Seibert at 3 a.m. at a hospital where Darian was being treated for burns. In arresting her, Officer Kevin Clinton followed instructions from Rolla, Missouri, Officer Richard Hanrahan that he refrain from giving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. After Seibert had been taken to the police station and left alone in an interview room for 15 to 20 minutes, Officer Hanrahan questioned her <span class="star-pagination">*605</span> without <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings for 30 to 40 minutes, squeezing her arm and repeating "Donald was also to die in his sleep." App. 59 (internal quotation marks omitted). After Seibert finally admitted she knew Donald was meant to die in the fire, she was given a 20-minute coffee and cigarette break. Officer Hanrahan then turned on a tape recorder, gave Seibert the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, and obtained a signed waiver of rights from her. He resumed the questioning with "Ok, 'trice, we've been talking for a little while about what happened on Wednesday the twelfth, haven't we?," App. 66, and confronted her with her prewarning statements:</p>
<blockquote>Hanrahan: "Now, in discussion you told us, you told us that there was a[n] understanding about Donald."</blockquote>
<blockquote>Seibert: "Yes."</blockquote>
<blockquote>Hanrahan: "Did that take place earlier that morning?"</blockquote>
<blockquote>Seibert: "Yes."</blockquote>
<blockquote>Hanrahan: "And what was the understanding about Donald?"</blockquote>
<blockquote>Seibert: "If they could get him out of the trailer, to take him out of the trailer."</blockquote>
<blockquote>Hanrahan: "And if they couldn't?"</blockquote>
<blockquote>Seibert: "I, I never even thought about it. I just figured they would."</blockquote>
<blockquote>Hanrahan: "`Trice, didn't you tell me that he was supposed to die in his sleep?"</blockquote>
<blockquote>Seibert: "If that would happen, 'cause he was on that new medicine, you know. . . ."</blockquote>
<blockquote>Hanrahan: "The Prozac? And it makes him sleepy. So he was supposed to die in his sleep?"</blockquote>
<blockquote>Seibert: "Yes." <i>Id.,</i> at 70.</blockquote>
<p>After being charged with first-degree murder for her role in Donald's death, Seibert sought to exclude both her prewarning and postwarning statements. At the suppression hearing, Officer Hanrahan testified that he made a "conscious <span class="star-pagination">*606</span> decision" to withhold <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, thus resorting to an interrogation technique he had been taught: question first, then give the warnings, and then repeat the question "until I get the answer that she's already provided once." App. 31-34. He acknowledged that Seibert's ultimate statement was "largely a repeat of information . . . obtained" prior to the warning. <i>Id.,</i> at 30.</p>
<p>The trial court suppressed the prewarning statement but admitted the responses given after the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> recitation. A jury convicted Seibert of second-degree murder. On appeal, the Missouri Court of Appeals affirmed, treating this case as indistinguishable from <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985). No. 23729, <span class="citation no-link">2002 WL 114804</span> (Jan. 30, 2002) (not released for publication).</p>
<p>The Supreme Court of Missouri reversed, holding that "[i]n the circumstances here, where the interrogation was nearly continuous, . . . the second statement, clearly the product of the invalid first statement, should have been suppressed." <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#701" aria-description="Citation for case: State v. Seibert">93 S. W. 3d 700, 701</a></span> (2002) (en banc). The court distinguished <i>Elstad</i> on the ground that warnings had not intentionally been withheld there, <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#704" aria-description="Citation for case: State v. Seibert">93 S. W. 3d, at 704</a></span>, and reasoned that "Officer Hanrahan's intentional omission of a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning was intended to deprive Seibert of the opportunity knowingly and intelligently to waive her <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights," <i>id.,</i> at 706. Since there were "no circumstances that would seem to dispel the effect of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation," the court held that the postwarning confession was involuntary and therefore inadmissible. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> To allow the police to achieve an "end run" around <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the court explained, would encourage <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violations and diminish <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s role in protecting the privilege against self-incrimination. <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#706" aria-description="Citation for case: State v. Seibert">93 S. W. 3d, at 706-707</a></span>. Three judges dissented, taking the view that <i>Elstad</i> applied even though the police intentionally withheld <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before the initial statement, and believing that "Seibert's unwarned responses to Officer Hanrahan's questioning did not prevent <span class="star-pagination">*607</span> her from waiving her rights and confessing." <span class="citation" data-id="9692268"><a href="/opinion/1890935/state-v-seibert/#708" aria-description="Citation for case: State v. Seibert">93 S. W. 3d, at 708</a></span> (opinion of Benton, J.).</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./538/1031/">538 U. S. 1031</a></span> (2003), to resolve a split in the Courts of Appeals. Compare <i>United States</i> v. <i>Gale,</i> <span class="citation" data-id="575188"><a href="/opinion/575188/united-states-v-theodore-k-gale/#1418" aria-description="Citation for case: United States v. Theodore K. Gale">952 F. 2d 1412, 1418</a></span> (CADC 1992) (while "deliberate `end run' around <i>Miranda</i>" would provide cause for suppression, case involved no conduct of that order); <i>United States</i> v. <i>Carter,</i> <span class="citation" data-id="9479453"><a href="/opinion/528515/united-states-v-terry-gene-carter/#373" aria-description="Citation for case: United States v. Terry Gene Carter">884 F. 2d 368, 373</a></span> (CA8 1989) ("<i>Elstad</i> did not go so far as to fashion a rule permitting this sort of end run around <i>Miranda</i>"), with <i>United States</i> v. <i>Orso,</i> <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1034" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F. 3d 1030, 1034-1039</a></span> (CA9 2001) (en banc) (rejecting argument that "tainted fruit" analysis applies because deliberate withholding of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings constitutes an "improper tactic"); <i>United States</i> v. <i>Esquilin,</i> <span class="citation" data-id="198872"><a href="/opinion/198872/united-states-v-esquilin/#319" aria-description="Citation for case: United States v. Esquilin">208 F. 3d 315, 319-321</a></span> (CA1 2000) (similar). We now affirm.</p>
<p></p>
<h2>II</h2>
<p>"In criminal trials, in the courts of the United States, wherever a question arises whether a confession is incompetent because not voluntary, the issue is controlled by that portion of the Fifth Amendment . . . commanding that no person `shall be compelled in any criminal case to be a witness against himself.'" <i>Bram</i> v. <i>United States,</i> <span class="citation" data-id="9417767"><a href="/opinion/94782/bram-v-united-states/#542" aria-description="Citation for case: Bram v. United States">168 U. S. 532, 542</a></span> (1897). A parallel rule governing the admissibility of confessions in state courts emerged from the Due Process Clause of the Fourteenth Amendment, see, <i>e. g., </i><i>Brown</i> v. <i>Mississippi,</i> <span class="citation" data-id="102604"><a href="/opinion/102604/brown-v-mississippi/" aria-description="Citation for case: Brown v. Mississippi">297 U. S. 278</a></span> (1936), which governed state cases until we concluded in <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/#8" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1, 8</a></span> (1964), that "[t]he Fourteenth Amendment secures against state invasion the same privilege that the Fifth Amendment guarantees against federal infringementthe right of a person to remain silent unless he chooses to speak in the unfettered exercise of his own will, and to suffer no penalty . . . for such silence." In unifying the Fifth and Fourteenth Amendment voluntariness tests, <i><span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">Malloy</a></span></i> "made clear what had already become apparentthat the substantive and procedural safeguards <span class="star-pagination">*608</span> surrounding admissibility of confessions in state cases had become exceedingly exacting, reflecting all the policies embedded in the privilege" against self-incrimination. <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona">384 U.S., at 464</a></span>.</p>
<p>In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> we explained that the "voluntariness doctrine in the state cases . . . encompasses all interrogation practices which are likely to exert such pressure upon an individual as to disable him from making a free and rational choice," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 464-465</a></span>. We appreciated the difficulty of judicial enquiry <i>post hoc</i> into the circumstances of a police interrogation, <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#444" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 444</a></span> (2000), and recognized that "the coercion inherent in custodial interrogation blurs the line between voluntary and involuntary statements, and thus heightens the risk" that the privilege against self-incrimination will not be observed, <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#435" aria-description="Citation for case: Dickerson v. United States"><i>id.,</i> at 435</a></span>. Hence our concern that the "traditional totality-of-the-circumstances" test posed an "unacceptably great" risk that involuntary custodial confessions would escape detection. <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#442" aria-description="Citation for case: Dickerson v. United States"><i>Id.,</i> at 442</a></span>.</p>
<p>Accordingly, "to reduce the risk of a coerced confession and to implement the Self-Incrimination Clause," <i>Chavez</i> v. <i>Martinez,</i> <span class="citation" data-id="9434450"><a href="/opinion/127927/chavez-v-martinez/#790" aria-description="Citation for case: Chavez v. Martinez">538 U. S. 760, 790</a></span> (2003) (KENNEDY, J., concurring in part and dissenting in part), this Court in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> concluded that "the accused must be adequately and effectively apprised of his rights and the exercise of those rights must be fully honored," <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> conditioned the admissibility at trial of any custodial confession on warning a suspect of his rights: failure to give the prescribed warnings and obtain a waiver of rights before custodial questioning generally requires exclusion of any statements obtained.<sup>[1]</sup> Conversely, giving the warnings and getting a <span class="star-pagination">*609</span> waiver has generally produced a virtual ticket of admissibility; maintaining that a statement is involuntary even though given after warnings and voluntary waiver of rights requires unusual stamina, and litigation over voluntariness tends to end with the finding of a valid waiver. See <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#433" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 433, n. 20</a></span> (1984) ("[C]ases in which a defendant can make a colorable argument that a self-incriminating statement was `compelled' despite the fact that the law enforcement authorities adhered to the dictates of <i>Miranda</i> are rare"). To point out the obvious, this common consequence would not be common at all were it not that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are customarily given under circumstances allowing for a real choice between talking and remaining silent.</p>
<p></p>
<h2>III</h2>
<p>There are those, of course, who preferred the old way of doing things, giving no warnings and litigating the voluntariness of any statement in nearly every instance. In the aftermath of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> Congress even passed a statute seeking to restore that old regime, <span class="citation no-link">18 U. S. C. § 3501</span>, although the Act lay dormant for years until finally invoked and challenged in <i>Dickerson</i> v. <i>United States, supra</i><i>. Dickerson</i> reaffirmed <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and held that its constitutional character prevailed against the statute.</p>
<p>The technique of interrogating in successive, unwarned and warned phases raises a new challenge to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Although we have no statistics on the frequency of this practice, it is not confined to Rolla, Missouri. An officer of that police department testified that the strategy of withholding <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings until after interrogating and drawing out a confession was promoted not only by his own department, but by a national police training organization and other departments in which he had worked. App. 31-32. Consistently with the officer's testimony, the Police Law Institute, for example, instructs that "officers may conduct a two-stage interrogation. . . . At any point during the pre-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> interrogation, <span class="star-pagination">*610</span> usually after arrestees have confessed, officers may then read the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and ask for a waiver. If the arrestees waive their <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, officers will be able to repeat any <i>subsequent</i> incriminating statements later in court." Police Law Institute, Illinois Police Law Manual 83 (Jan. 2001-Dec. 2003) (available in Clerk of Court's case file) (hereinafter Police Law Manual) (emphasis in original).<sup>[2]</sup><span class="star-pagination">*611</span> The upshot of all this advice is a question-first practice of some popularity, as one can see from the reported cases describing its use, sometimes in obedience to departmental policy.<sup>[3]</sup></p>
<p></p>
<h2>IV</h2>
<p>When a confession so obtained is offered and challenged, attention must be paid to the conflicting objects of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and question-first. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> addressed "interrogation practices . . . likely . . . to disable [an individual] from making a free and rational choice" about speaking, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#464" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 464-465</a></span>, and held that a suspect must be "adequately and effectively" advised of the choice the Constitution guarantees, <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span>. The object of question-first is to render <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings ineffective by waiting for a particularly opportune time to give them, after the suspect has already confessed.</p>
<p>Just as "no talismanic incantation [is] required to satisfy [<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span>'s] strictures," <i>California</i> v. <i>Prysock,</i> <span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/#359" aria-description="Citation for case: California v. Prysock">453 U. S. 355, 359</a></span> (1981) <i>(per curiam)</i><i>,</i> it would be absurd to think that mere recitation of the litany suffices to satisfy <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in every conceivable circumstance. "The inquiry is simply whether the warnings reasonably `conve[y] to [a suspect] his rights as required by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i>'" <i>Duckworth</i> v. <i>Eagan,</i> <span class="citation" data-id="9431819"><a href="/opinion/112322/duckworth-v-eagan/#203" aria-description="Citation for case: Duckworth v. Eagan">492 U. S. 195, 203</a></span> (1989) (quoting <span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/#361" aria-description="Citation for case: California v. Prysock"><i>Prysock, supra,</i> at 361</a></span>). The threshold issue when interrogators question first and warn later is thus whether it would be reasonable to find that in these circumstances the warnings could function "effectively" <span class="star-pagination">*612</span> as <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires. Could the warnings effectively advise the suspect that he had a real choice about giving an admissible statement at that juncture? Could they reasonably convey that he could choose to stop talking even if he had talked earlier? For unless the warnings could place a suspect who has just been interrogated in a position to make such an informed choice, there is no practical justification for accepting the formal warnings as compliance with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> or for treating the second stage of interrogation as distinct from the first, unwarned and inadmissible segment.<sup>[4]</sup></p>
<p>There is no doubt about the answer that proponents of question-first give to this question about the effectiveness of <span class="star-pagination">*613</span> warnings given only after successful interrogation, and we think their answer is correct. By any objective measure, applied to circumstances exemplified here, it is likely that if the interrogators employ the technique of withholding warnings until after interrogation succeeds in eliciting a confession, the warnings will be ineffective in preparing the suspect for successive interrogation, close in time and similar in content. After all, the reason that question-first is catching on is as obvious as its manifest purpose, which is to get a confession the suspect would not make if he understood his rights at the outset; the sensible underlying assumption is that with one confession in hand before the warnings, the interrogator can count on getting its duplicate, with trifling additional trouble. Upon hearing warnings only in the aftermath of interrogation and just after making a confession, a suspect would hardly think he had a genuine right to remain silent, let alone persist in so believing once the police began to lead him over the same ground again.<sup>[5]</sup> A more likely reaction on a suspect's part would be perplexity about the reason for discussing rights at that point, bewilderment being an unpromising frame of mind for knowledgeable decision. What is worse, telling a suspect that "anything you say can and will be used against you," without expressly excepting the statement just given, could lead to an entirely reasonable inference that what he has just said will be used, with subsequent silence being of no avail. Thus, when <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are inserted in the midst of coordinated and continuing interrogation, they are likely to mislead and "depriv[e] <span class="star-pagination">*614</span> a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them." <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#424" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 424</a></span> (1986). By the same token, it would ordinarily be unrealistic to treat two spates of integrated and proximately conducted questioning as independent interrogations subject to independent evaluation simply because <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings formally punctuate them in the middle.</p>
<p></p>
<h2>V</h2>
<p>Missouri argues that a confession repeated at the end of an interrogation sequence envisioned in a question-first strategy is admissible on the authority of <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), but the argument disfigures that case. In <i>Elstad,</i> the police went to the young suspect's house to take him into custody on a charge of burglary. Before the arrest, one officer spoke with the suspect's mother, while the other one joined the suspect in a "brief stop in the living room," <i>id.,</i> at 315, where the officer said he "felt" the young man was involved in a burglary, <i>id.,</i> at 301 (internal quotation marks omitted). The suspect acknowledged he had been at the scene. <i>Ibid.</i> This Court noted that the pause in the living room "was not to interrogate the suspect but to notify his mother of the reason for his arrest," <i>id.,</i> at 315, and described the incident as having "none of the earmarks of coercion," <i>id.,</i> at 316. The Court, indeed, took care to mention that the officer's initial failure to warn was an "oversight" that "may have been the result of confusion as to whether the brief exchange qualified as `custodial interrogation' or . . . may simply have reflected . . . reluctance to initiate an alarming police procedure before [an officer] had spoken with respondent's mother." <i>Id.,</i> at 315-316. At the outset of a later and systematic station house interrogation going well beyond the scope of the laconic prior admission, the suspect was given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and made a full confession. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#301" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 301, 314-315</a></span>. In holding the <span class="star-pagination">*615</span> second statement admissible and voluntary, <i>Elstad</i> rejected the "cat out of the bag" theory that any short, earlier admission, obtained in arguably innocent neglect of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> determined the character of the later, warned confession, <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#311" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 311-314</a></span>; on the facts of that case, the Court thought any causal connection between the first and second responses to the police was "speculative and attenuated," <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#313" aria-description="Citation for case: Oregon v. Elstad"><i>id.,</i> at 313</a></span>. Although the <i>Elstad</i> Court expressed no explicit conclusion about either officer's state of mind, it is fair to read <i>Elstad</i> as treating the living room conversation as a good-faith <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> mistake, not only open to correction by careful warnings before systematic questioning in that particular case, but posing no threat to warn-first practice generally. See <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 309</a></span> (characterizing the officers' omission of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings as "a simple failure to administer the warnings, unaccompanied by any actual coercion or other circumstances calculated to undermine the suspect's ability to exercise his free will"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#318" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 318, n. 5</a></span> (Justice Brennan's concern in dissent that <i>Elstad</i> would invite question-first practice "distorts the reasoning and holding of our decision, but, worse, invites trial courts and prosecutors to do the same").</p>
<p>The contrast between <i>Elstad</i> and this case reveals a series of relevant facts that bear on whether <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings delivered midstream could be effective enough to accomplish their object: the completeness and detail of the questions and answers in the first round of interrogation, the overlapping content of the two statements, the timing and setting of the first and the second, the continuity of police personnel, and the degree to which the interrogator's questions treated the second round as continuous with the first. In <i>Elstad,</i> it was not unreasonable to see the occasion for questioning at the station house as presenting a markedly different experience from the short conversation at home; since a reasonable person in the suspect's shoes could have seen the station house questioning as a new and distinct experience, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> <span class="star-pagination">*616</span> warnings could have made sense as presenting a genuine choice whether to follow up on the earlier admission.</p>
<p>At the opposite extreme are the facts here, which by any objective measure reveal a police strategy adapted to undermine the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.<sup>[6]</sup> The unwarned interrogation was conducted in the station house, and the questioning was systematic, exhaustive, and managed with psychological skill. When the police were finished there was little, if anything, of incriminating potential left unsaid. The warned phase of questioning proceeded after a pause of only 15 to 20 minutes, in the same place as the unwarned segment. When the same officer who had conducted the first phase recited the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, he said nothing to counter the probable misimpression that the advice that anything Seibert said could be used against her also applied to the details of the inculpatory statement previously elicited. In particular, the police did not advise that her prior statement could not be used.<sup>[7]</sup> Nothing was said or done to dispel the oddity of warning about legal rights to silence and counsel right after the police had led her through a systematic interrogation, and any uncertainty on her part about a right to stop talking about matters previously discussed would only have been aggravated by the way Officer Hanrahan set the scene by saying "we've been talking for a little while about what happened on Wednesday the twelfth, haven't we?" App. 66. The impression that the further questioning was a mere continuation of the earlier questions and responses was fostered by references back to the confession already given. It <span class="star-pagination">*617</span> would have been reasonable to regard the two sessions as parts of a continuum, in which it would have been unnatural to refuse to repeat at the second stage what had been said before. These circumstances must be seen as challenging the comprehensibility and efficacy of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to the point that a reasonable person in the suspect's shoes would not have understood them to convey a message that she retained a choice about continuing to talk.<sup>[8]</sup></p>
<p></p>
<h2>VI</h2>
<p>Strategists dedicated to draining the substance out of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> cannot accomplish by training instructions what <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span></i> held Congress could not do by statute. Because the question-first tactic effectively threatens to thwart <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s purpose of reducing the risk that a coerced confession would be admitted, and because the facts here do not reasonably support a conclusion that the warnings given could have served their purpose, Seibert's postwarning statements are inadmissible. The judgment of the Supreme Court of Missouri is affirmed.</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE BREYER, concurring.</p>
<p>In my view, the following simple rule should apply to the two-stage interrogation technique: Courts should exclude the "fruits" of the initial unwarned questioning unless the failure to warn was in good faith. Cf. <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298, 309, 318, n. 5</a></span> (1985); <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/" aria-description="Citation for case: United States v. Leon">468 U. S. 897</a></span> (1984). I believe this is a sound and workable approach to the problem this case presents. Prosecutors and judges have long understood how to apply the "fruits" approach, which they use in other areas of law. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). And in the workaday <span class="star-pagination">*618</span> world of criminal law enforcement the administrative simplicity of the familiar has significant advantages over a more complex exclusionary rule. Cf. <i>post,</i> at 628-629 (O'CONNOR, J., dissenting).</p>
<p>I believe the plurality's approach in practice will function as a "fruits" test. The truly "effective" <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings on which the plurality insists, <i>ante,</i> at 615, will occur only when certain circumstances  a lapse in time, a change in location or interrogating officer, or a shift in the focus of the questioning  intervene between the unwarned questioning and any postwarning statement. Cf. <i>Taylor</i> v. <i>Alabama,</i> <span class="citation" data-id="9428855"><a href="/opinion/110760/taylor-v-alabama/#690" aria-description="Citation for case: Taylor v. Alabama">457 U. S. 687, 690</a></span> (1982) (evidence obtained subsequent to a constitutional violation must be suppressed as "fruit of the poisonous tree" unless "intervening events break the causal connection").</p>
<p>I consequently join the plurality's opinion in full. I also agree with JUSTICE KENNEDY'S opinion insofar as it is consistent with this approach and makes clear that a good-faith exception applies. See <i>post,</i> at 622 (opinion concurring in judgment).</p>
<p>JUSTICE KENNEDY, concurring in the judgment.</p>
<p>The interrogation technique used in this case is designed to circumvent <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). It undermines the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning and obscures its meaning. The plurality opinion is correct to conclude that statements obtained through the use of this technique are inadmissible. Although I agree with much in the careful and convincing opinion for the plurality, my approach does differ in some respects, requiring this separate statement.</p>
<p>The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule has become an important and accepted element of the criminal justice system. See <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428</a></span> (2000). At the same time, not every violation of the rule requires suppression of the evidence obtained. Evidence is admissible when the central <span class="star-pagination">*619</span> concerns of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are not likely to be implicated and when other objectives of the criminal justice system are best served by its introduction. Thus, we have held that statements obtained in violation of the rule can be used for impeachment, so that the truth-finding function of the trial is not distorted by the defense, see <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971); that there is an exception to protect countervailing concerns of public safety, see <i>New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984); and that physical evidence obtained in reliance on statements taken in violation of the rule is admissible, see <i>United States</i> v. <i>Patane, post,</i> p. 630. These cases, in my view, are correct. They recognize that admission of evidence is proper when it would further important objectives without compromising <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s central concerns. Under these precedents, the scope of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> suppression remedy depends on a consideration of those legitimate interests and on whether admission of the evidence under the circumstances would frustrate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s central concerns and objectives.</p>
<p><i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), reflects this approach. In <i>Elstad,</i> a suspect made an initial incriminating statement at his home. The suspect had not received a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning before making the statement, apparently because it was not clear whether the suspect was in custody at the time. The suspect was taken to the station house, where he received a proper warning, waived his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, and made a second statement. He later argued that the postwarning statement should be suppressed because it was related to the unwarned first statement, and likely induced or caused by it. The Court held that, although a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation made the first statement inadmissible, the postwarning statements could be introduced against the accused because "neither the general goal of deterring improper police conduct nor the Fifth Amendment goal of assuring trustworthy evidence would be served by suppression" <span class="star-pagination">*620</span> given the facts of that case. <i><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">Elstad, supra,</a></span></i> at 308 (citing <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#445" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 445</a></span> (1974)).</p>
<p>In my view, <i>Elstad</i> was correct in its reasoning and its result. <i>Elstad</i> reflects a balanced and pragmatic approach to enforcement of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning. An officer may not realize that a suspect is in custody and warnings are required. The officer may not plan to question the suspect or may be waiting for a more appropriate time. Skilled investigators often interview suspects multiple times, and good police work may involve referring to prior statements to test their veracity or to refresh recollection. In light of these realities it would be extravagant to treat the presence of one statement that cannot be admitted under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> as sufficient reason to prohibit subsequent statements preceded by a proper warning. See <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#309" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 309</a></span> ("It is an unwarranted extension of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> to hold that a simple failure to administer the warnings . . . so taints the investigatory process that a subsequent voluntary and informed waiver is ineffective for some indeterminate period"). That approach would serve "neither the general goal of deterring improper police conduct nor the Fifth Amendment goal of assuring trustworthy evidence would be served by suppression of the . . . testimony." <i>Id.,</i> at 308.</p>
<p>This case presents different considerations. The police used a two-step questioning technique based on a deliberate violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning was withheld to obscure both the practical and legal significance of the admonition when finally given. As JUSTICE SOUTER points out, the two-step technique permits the accused to conclude that the right not to respond did not exist when the earlier incriminating statements were made. The strategy is based on the assumption that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings will tend to mean less when recited midinterrogation, after inculpatory statements have already been obtained. This tactic relies on an intentional misrepresentation of the protection that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> <span class="star-pagination">*621</span> offers and does not serve any legitimate objectives that might otherwise justify its use.</p>
<p>Further, the interrogating officer here relied on the defendant's prewarning statement to obtain the postwarning statement used against her at trial. The postwarning interview resembled a cross-examination. The officer confronted the defendant with her inadmissible prewarning statements and pushed her to acknowledge them. See App. 70 ("`Trice, didn't you tell me that he was supposed to die in his sleep?"). This shows the temptations for abuse inherent in the two-step technique. Reference to the prewarning statement was an implicit suggestion that the mere repetition of the earlier statement was not independently incriminating. The implicit suggestion was false.</p>
<p>The technique used in this case distorts the meaning of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and furthers no legitimate countervailing interest. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule would be frustrated were we to allow police to undermine its meaning and effect. The technique simply creates too high a risk that postwarning statements will be obtained when a suspect was deprived of "knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them." <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#423" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 423-424</a></span> (1986). When an interrogator uses this deliberate, two-step strategy, predicated upon violating <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> during an extended interview, postwarning statements that are related to the substance of prewarning statements must be excluded absent specific, curative steps.</p>
<p>The plurality concludes that whenever a two-stage interview occurs, admissibility of the postwarning statement should depend on "whether [the] <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings delivered midstream could have been effective enough to accomplish their object" given the specific facts of the case. <i>Ante,</i> at 615. This test envisions an objective inquiry from the perspective of the suspect, and applies in the case of both intentional and unintentional two-stage interrogations. <span class="star-pagination">*622</span> <i>Ante,</i> at 615-617. In my view, this test cuts too broadly. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s clarity is one of its strengths, and a multifactor test that applies to every two-stage interrogation may serve to undermine that clarity. Cf. <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#430" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 430</a></span> (1984). I would apply a narrower test applicable only in the infrequent case, such as we have here, in which the two-step interrogation technique was used in a calculated way to undermine the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning.</p>
<p>The admissibility of postwarning statements should continue to be governed by the principles of <i>Elstad</i> unless the deliberate two-step strategy was employed. If the deliberate two-step strategy has been used, postwarning statements that are related to the substance of prewarning statements must be excluded unless curative measures are taken before the postwarning statement is made. Curative measures should be designed to ensure that a reasonable person in the suspect's situation would understand the import and effect of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning and of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> waiver. For example, a substantial break in time and circumstances between the prewarning statement and the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning may suffice in most circumstances, as it allows the accused to distinguish the two contexts and appreciate that the interrogation has taken a new turn. Cf. <i>Westover</i> v. <i>United States,</i> decided with <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Alternatively, an additional warning that explains the likely inadmissibility of the prewarning custodial statement may be sufficient. No curative steps were taken in this case, however, so the postwarning statements are inadmissible and the conviction cannot stand.</p>
<p>For these reasons, I concur in the judgment of the Court.</p>
<p>JUSTICE O'CONNOR, with whom THE CHIEF JUSTICE, JUSTICE SCALIA, and JUSTICE THOMAS join, dissenting.</p>
<p>The plurality devours <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), even as it accuses petitioner's argument of "disfigur[ing]" that decision. <i>Ante,</i> at 614. I believe that we <span class="star-pagination">*623</span> are bound by <i>Elstad</i> to reach a different result, and I would vacate the judgment of the Supreme Court of Missouri.</p>
<p></p>
<h2>I</h2>
<p>On two preliminary questions I am in full agreement with the plurality. First, the plurality appropriately follows <i>Elstad</i> in concluding that Seibert's statement cannot be held inadmissible under a "fruit of the poisonous tree" theory. <i>Ante,</i> at 612, n. 4 (internal quotation marks omitted). Second, the plurality correctly declines to focus its analysis on the subjective intent of the interrogating officer.</p>
<p></p>
<h2>A</h2>
<p>This Court has made clear that there simply is no place for a robust deterrence doctrine with regard to violations of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). See <i>Dickerson</i> v. <i>United States,</i> <span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/#441" aria-description="Citation for case: Dickerson v. United States">530 U. S. 428, 441</a></span> (2000) ("Our decision in <i>[Elstad]</i>  refusing to apply the traditional `fruits' doctrine developed in Fourth Amendment cases  . . . simply recognizes the fact that unreasonable searches under the Fourth Amendment are different from unwarned interrogation under the Fifth Amendment"); <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#306" aria-description="Citation for case: Oregon v. Elstad"><i>Elstad, supra,</i> at 306</a></span> (unlike the Fourth Amendment exclusionary rule, the "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> exclusionary rule . . . serves the Fifth Amendment and sweeps more broadly than the Fifth Amendment itself"); see also <i>United States</i> v. <i>Patane, post,</i> at 644-645 (KENNEDY, J., concurring in judgment) (refusal to suppress evidence obtained following an unwarned confession in <i>Elstad, New York</i> v. <i>Quarles,</i> <span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">467 U. S. 649</a></span> (1984), and <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), was based on "our recognition that the concerns underlying the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> . . . rule must be accommodated to other objectives of the criminal justice system"). Consistent with that view, the Court today refuses to apply the traditional "fruits" analysis to the physical fruit of a claimed <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation. <i>Patane, post,</i> p. 630. The plurality <span class="star-pagination">*624</span> correctly refuses to apply a similar analysis to testimonial fruits.</p>
<p>Although the analysis the plurality ultimately espouses examines the same facts and circumstances that a "fruits" analysis would consider (such as the lapse of time between the two interrogations and change of questioner or location), it does so for entirely different reasons. The fruits analysis would examine those factors because they are relevant to the balance of deterrence value versus the "drastic and socially costly course" of excluding reliable evidence. <i>Nix</i> v. <i>Williams,</i> <span class="citation" data-id="9429647"><a href="/opinion/111204/nix-v-williams/#442" aria-description="Citation for case: Nix v. Williams">467 U. S. 431, 442-443</a></span> (1984). The plurality, by contrast, looks to those factors to inform the <i>psychological</i> judgment regarding whether the suspect has been informed effectively of her right to remain silent. The analytical underpinnings of the two approaches are thus entirely distinct, and they should not be conflated just because they function similarly in practice. Cf. <i>ante,</i> at 617-618 (BREYER, J., concurring).</p>
<p></p>
<h2>B</h2>
<p>The plurality's rejection of an intent-based test is also, in my view, correct. Freedom from compulsion lies at the heart of the Fifth Amendment, and requires us to assess whether a suspect's decision to speak truly was voluntary. Because voluntariness is a matter of the suspect's state of mind, we focus our analysis on the way in which suspects experience interrogation. See generally <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#455" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 455</a></span> (summarizing psychological tactics used by police that "undermin[e]" the suspect's "will to resist," and noting that "the very fact of custodial interrogation . . . trades on the weakness of individuals"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 467</a></span> ("[I]n-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely").</p>
<p>Thoughts kept inside a police officer's head cannot affect that experience. See <i>Moran</i> v. <i>Burbine,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412</a></span>, 422 <span class="star-pagination">*625</span> (1986) ("Events occurring outside of the presence of the suspect and entirely unknown to him surely can have no bearing on the capacity to comprehend and knowingly relinquish a constitutional right"). In <i><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/" aria-description="Citation for case: Moran v. Burbine">Moran</a></span>,</i> an attorney hired by the suspect's sister had been trying to contact the suspect and was told by the police, falsely, that they would not begin an interrogation that night. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#416" aria-description="Citation for case: Moran v. Burbine"><i>Id.,</i> at 416-418</a></span>. The suspect was not aware that an attorney had been hired for him. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#417" aria-description="Citation for case: Moran v. Burbine"><i>Id.,</i> at 417</a></span>. We rejected an analysis under which a different result would obtain for "the same defendant, armed with the same information and confronted with precisely the same police conduct" if something not known to the defendant  such as the fact that an attorney was attempting to contact him  had been different. <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine"><i>Id.,</i> at 422</a></span>. The same principle applies here. A suspect who experienced the exact same interrogation as Seibert, save for a difference in the undivulged, subjective intent of the interrogating officer when he failed to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, would not experience the interrogation any differently. "[W]hether intentional or inadvertent, the state of mind of the police is irrelevant to the question of the intelligence and voluntariness of respondent's election to abandon his rights. Although highly inappropriate, even deliberate deception of an attorney could not possibly affect a suspect's decision to waive his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights unless he were at least aware of the incident." <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#423" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 423</a></span>. Cf. <i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#324" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 324-325</a></span> (1994) <i>(per curiam)</i> (police officer's subjective intent is irrelevant to whether suspect is in custody for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes; "one cannot expect the person under interrogation to probe the officer's innermost thoughts").</p>
<p>Because the isolated fact of Officer Hanrahan's intent could not have had any bearing on Seibert's "capacity to comprehend and knowingly relinquish" her right to remain silent, <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#422" aria-description="Citation for case: Moran v. Burbine"><i>Moran, supra,</i> at 422</a></span>, it could not by itself affect the voluntariness of her confession. Moreover, recognizing an exception to <i>Elstad</i> for intentional violations would require focusing <span class="star-pagination">*626</span> constitutional analysis on a police officer's subjective intent, an unattractive proposition that we all but uniformly avoid. In general, "we believe that `sending state and federal courts on an expedition into the minds of police officers would produce a grave and fruitless misallocation of judicial resources.'" <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 922, n. 23</a></span> (1984) (quoting <i>Massachusetts</i> v. <i>Painten,</i> <span class="citation" data-id="9423573"><a href="/opinion/107577/massachusetts-v-painten/#565" aria-description="Citation for case: Massachusetts v. Painten">389 U. S. 560, 565</a></span> (1968) <i>(per curiam)</i> (White, J., dissenting)). This case presents the uncommonly straightforward circumstance of an officer openly admitting that the violation was intentional. But the inquiry will be complicated in other situations probably more likely to occur. For example, different officers involved in an interrogation might claim different states of mind regarding the failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. Even in the simple case of a single officer who claims that a failure to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings was inadvertent, the likelihood of error will be high. See W. LaFave, Search and Seizure § 1.4(e), p. 124 (3d ed. 1996) ("[T]here is no reason to believe that courts can with any degree of success determine in which instances the police had an ulterior motive").</p>
<p>These evidentiary difficulties have led us to reject an intent-based test in several criminal procedure contexts. For example, in <i>New York</i> v. <i><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/" aria-description="Citation for case: New York v. Quarles">Quarles, supra</a></span></i><i>,</i> one of the factors that led us to reject an inquiry into the subjective intent of the police officer in crafting a test for the "public safety" exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> was that officers' motives will be "largely unverifiable." 467 U. S., at 656. Similarly, our opinion in <i>Whren</i> v. <i>United States,</i> <span class="citation" data-id="118036"><a href="/opinion/118036/whren-v-united-states/#813" aria-description="Citation for case: Whren v. United States">517 U. S. 806, 813-814</a></span> (1996), made clear that "the evidentiary difficulty of establishing subjective intent" was one of the reasons (albeit not the principal one) for refusing to consider intent in Fourth Amendment challenges generally.</p>
<p>For these reasons, I believe that the approach espoused by JUSTICE KENNEDY is ill advised. JUSTICE KENNEDY would extend <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s exclusionary rule to any case in which the use of the "two-step interrogation technique" was "deliberate" <span class="star-pagination">*627</span> or "calculated." <i>Ante,</i> at 622 (opinion concurring in judgment). This approach untethers the analysis from facts knowable to, and therefore having any potential directly to affect, the suspect. Far from promoting "clarity," <i>ibid.,</i> the approach will add a third step to the suppression inquiry. In virtually every two-stage interrogation case, in addition to addressing the standard <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and voluntariness questions, courts will be forced to conduct the kind of difficult, state-of-mind inquiry that we normally take pains to avoid.</p>
<p></p>
<h2>II</h2>
<p>The plurality's adherence to <i>Elstad,</i> and mine to the plurality, end there. Our decision in <i>Elstad</i> rejected two lines of argument advanced in favor of suppression. The first was based on the "fruit of the poisonous tree" doctrine, discussed above. The second was the argument that the "lingering compulsion" inherent in a defendant's having let the "cat out of the bag" required suppression. <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#311" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 311</a></span>. The Court of Appeals of Oregon, in accepting the latter argument, had endorsed a theory indistinguishable from the one today's plurality adopts: "[T]he coercive impact of the unconstitutionally obtained statement remains, because in a defendant's mind it has sealed his fate. It is this impact that must be dissipated in order to make a subsequent confession admissible." <i>State</i> v. <i>Elstad,</i> <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#677" aria-description="Citation for case: State v. Elstad">61 Ore. App. 673, 677</a></span>, <span class="citation" data-id="9547859"><a href="/opinion/1173989/state-v-elstad/#554" aria-description="Citation for case: State v. Elstad">658 P.2d 552, 554</a></span> (1983).</p>
<p>We rejected this theory outright. We did so not because we refused to recognize the "psychological impact of the suspect's conviction that he has let the cat out of the bag," but because we refused to "endo[w]" those "psychological effects" with "constitutional implications." <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#311" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 311</a></span>. To do so, we said, would "effectively immuniz[e] a suspect who responds to pre-<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warning questions from the consequences of his subsequent informed waiver," an immunity that "comes at a high cost to legitimate law enforcement activity, while adding little desirable protection to the individual's <span class="star-pagination">*628</span> interest in not being <i>compelled</i> to testify against himself." <i>Id.,</i> at 312. The plurality might very well think that we struck the balance between Fifth Amendment rights and law enforcement interests incorrectly in <i>Elstad;</i> but that is not normally a sufficient reason for ignoring the dictates of <i>stare decisis.</i></p>
<p>I would analyze the two-step interrogation procedure under the voluntariness standards central to the Fifth Amendment and reiterated in <i>Elstad. Elstad</i> commands that if Seibert's first statement is shown to have been involuntary, the court must examine whether the taint dissipated through the passing of time or a change in circumstances: "When a prior statement is actually coerced, the time that passes between confessions, the change in place of interrogations, and the change in identity of the interrogators all bear on whether that coercion has carried over into the second confession." <i>Id.,</i> at 310 (citing <i>Westover</i> v. <i>United States,</i> decided with <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#494" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 494</a></span>). In addition, Seibert's second statement should be suppressed if she showed that it was involuntary despite the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. <i>Elstad, supra,</i> at 318 ("The relevant inquiry is whether, in fact, the second statement was also voluntarily made. As in any such inquiry, the finder of fact must examine the surrounding circumstances and the entire course of police conduct with respect to the suspect in evaluating the voluntariness of his statements"). Although I would leave this analysis for the Missouri courts to conduct on remand, I note that, unlike the officers in <i>Elstad,</i> Officer Hanrahan referred to Seibert's unwarned statement during the second part of the interrogation when she made a statement at odds with her unwarned confession. App. 70 ("`Trice, didn't you tell me that he was supposed to die in his sleep?"); cf. <i>Elstad, supra,</i> at 316 (officers did not "exploit the unwarned admission to pressure respondent into waiving his right to remain silent"). Such a tactic may bear on the voluntariness inquiry. Cf. <i>Frazier</i> v. <i>Cupp,</i> <span class="citation" data-id="107913"><a href="/opinion/107913/frazier-v-cupp/#739" aria-description="Citation for case: Frazier v. Cupp">394 U. S. 731, 739</a></span> (1969) (fact that police had falsely <span class="star-pagination">*629</span> told a suspect that his accomplice had already confessed was "relevant" to the voluntariness inquiry); <i>Moran,</i> <span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#423" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 423-424</a></span> (in discussing police deception, stating that simply withholding information is "relevant to the constitutional validity of a waiver if it deprives a defendant of knowledge essential to his ability to understand the nature of his rights and the consequences of abandoning them"); <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 476</a></span>.</p>
<p></p>
<h2>*   *   *</h2>
<p>Because I believe that the plurality gives insufficient deference to <i>Elstad</i> and that JUSTICE KENNEDY places improper weight on subjective intent, I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging affirmance were filed for the American Civil Liberties Union et al. by <i>Jonathan L. Abram, Christopher T. Handman, William H. Johnson, Steven R. Shapiro,</i> and <i>Lisa Kemler;</i> and for Michael R. Bromwich et al. by <i>George A. Cumming, Jr., Charles D. Weisselberg, Stephen J. Schulhofer, Kirsten D. Levingston, Frederick A. O. Schwarz, Jr.,</i> and <i>Tom Gerety.</i></p>
<p>[1]  "[T]he burden of showing admissibility rests, of course, on the prosecution." <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#604" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590, 604</a></span> (1975). The prosecution bears the burden of proving, at least by a preponderance of the evidence, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> waiver, <i>Colorado</i> v. <i>Connelly,</i> <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#169" aria-description="Citation for case: Colorado v. Connelly">479 U. S. 157, 169</a></span> (1986), and the voluntariness of the confession, <i>Lego</i> v. <i>Twomey,</i> <span class="citation" data-id="9424726"><a href="/opinion/108429/lego-v-twomey/#489" aria-description="Citation for case: Lego v. Twomey">404 U. S. 477, 489</a></span> (1972).</p>
<p>[2]  Emphasizing the impeachment exception to the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rule approved by this Court, <i>Harris</i> v. <i>New York,</i> <span class="citation" data-id="9424454"><a href="/opinion/108272/harris-v-new-york/" aria-description="Citation for case: Harris v. New York">401 U. S. 222</a></span> (1971), some training programs advise officers to omit <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings altogether or to continue questioning after the suspect invokes his rights. See, <i>e. g.,</i> Police Law Manual 83 ("There is no need to give a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning before asking questions if . . . the answers given . . . will not be required by the prosecutor during the prosecution's case-in-chief"); California Commission on Peace Officer Standards and Training, Video Training Programs for California Law Enforcement, Miranda: Post-Invocation Questioning (broadcast July 11, 1996) ("We . . . have been encouraging you to continue to question a suspect after they've invoked their <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights"); D. Zulawski &amp; D. Wicklander, Practical Aspects of Interview and Interrogation 50-51 (2d ed. 2002) (describing the practice of "[b]eachheading" as useful for impeachment purpose (emphasis deleted)); see also Weisselberg, Saving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> <span class="citation no-link">84 Cornell L. Rev. 109</span>, 110, 132-139 (1998) (collecting California training materials encouraging questioning "outside <i>Miranda</i>"). This training is reflected in the reported cases involving deliberate questioning after invocation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. See, <i>e. g., </i><i>California Attorneys for Criminal Justice</i> v. <i>Butts,</i> <span class="citation" data-id="6984365"><a href="/opinion/7079352/california-attorneys-for-criminal-justice-v-butts/#1042" aria-description="Citation for case: California Attorneys for Criminal Justice v. Butts">195 F. 3d 1039, 1042-1044</a></span> (CA9 1999); <i>Henry</i> v. <i>Kernan,</i> <span class="citation" data-id="766929"><a href="/opinion/766929/bobby-henry-v-peggy-kernan-warden-daniel-e-lungren-attorney-general/#1026" aria-description="Citation for case: Bobby Henry v. Peggy Kernan, Warden Daniel E. Lungren,...">197 F. 3d 1021, 1026</a></span> (CA9 1999); <i>People</i> v. <i>Neal,</i> <span class="citation" data-id="9787381"><a href="/opinion/2588587/people-v-neal/#68" aria-description="Citation for case: People v. Neal">31 Cal. 4th 63, 68</a></span>, <span class="citation" data-id="9787381"><a href="/opinion/2588587/people-v-neal/#282" aria-description="Citation for case: People v. Neal">72 P. 3d 280, 282</a></span> (2003); <i>People</i> v. <i>Peevy,</i> <span class="citation" data-id="9609905"><a href="/opinion/1378981/people-v-peevy/#1189" aria-description="Citation for case: People v. Peevy">17 Cal. 4th 1184, 1189</a></span>, <span class="citation" data-id="9609905"><a href="/opinion/1378981/people-v-peevy/#1215" aria-description="Citation for case: People v. Peevy">953 P. 2d 1212, 1215</a></span> (1998). Scholars have noted the growing trend of such practices. See, <i>e. g.,</i> Leo, Questioning the Relevance of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> in the Twenty-First Century, <span class="citation no-link">99 Mich. L. Rev. 1000</span>, 1010 (2001); Weisselberg, In the Stationhouse After <i><span class="citation" data-id="9433984"><a href="/opinion/118380/dickerson-v-united-states/" aria-description="Citation for case: Dickerson v. United States">Dickerson</a></span>,</i> <span class="citation no-link">99 Mich. L. Rev. 1121</span>, 1123-1154 (2001).
</p>
<p>It is not the case, of course, that law enforcement educators en masse are urging that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> be honored only in the breach. See, <i>e. g.,</i> C. O'Hara &amp; G. O'Hara, Fundamentals of Criminal Investigation 133 (7th ed. 2003) (instructing police to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before conducting custodial interrogation); F. Inbau, J. Reid, &amp; J. Buckley, Criminal Interrogation and Confessions 221 (3d ed. 1986) (hereinafter Inbau, Reid, &amp; Buckley) (same); John Reid &amp; Associates, Interviewing &amp; Interrogation: The Reid Technique 61 (1991) (same). Most police manuals do not advocate the question-first tactic, because they understand that <i>Oregon</i> v. <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985), involved an officer's good-faith failure to warn. See, <i>e. g.,</i> Inbau, Reid, &amp; Buckley 241 (<i>Elstad</i>'s "facts as well as [its] specific holding" instruct that "where an interrogator has failed to administer the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in the mistaken belief that, under the circumstances of the particular case, the warnings were not required, . . . corrective measures . . . salvage an interrogation opportunity").</p>
<p>[3]  See, <i>e. g., </i><i>United States</i> v. <i>Orso,</i> <span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/#1032" aria-description="Citation for case: United States v. Jody Myesha Orso">266 F. 3d 1030, 1032-1033</a></span> (CA9 2001) (en banc); <i>Pope</i> v. <i>Zenon,</i> <span class="citation" data-id="707574"><a href="/opinion/707574/charles-s-pope-petitioner-appellant-v-carl-zenon-superintendent-osci/#1023" aria-description="Citation for case: Charles S. POPE, Petitioner-Appellant, v. Carl ZENON,...">69 F. 3d 1018, 1023-1024</a></span> (CA9 1995), overruled by <i><span class="citation" data-id="9494408"><a href="/opinion/775079/united-states-v-jody-myesha-orso/" aria-description="Citation for case: United States v. Jody Myesha Orso">Orso, supra;</a></span> </i><i>Cooper</i> v. <i>Dupnik,</i> <span class="citation" data-id="9000842"><a href="/opinion/9008075/cooper-v-dupnik/#1224" aria-description="Citation for case: Cooper v. Dupnik">963 F. 2d 1220, 1224-1227, 1249</a></span> (CA9 1992) (en banc); <i>United States</i> v. <i>Carter,</i> <span class="citation" data-id="9479453"><a href="/opinion/528515/united-states-v-terry-gene-carter/#373" aria-description="Citation for case: United States v. Terry Gene Carter">884 F. 2d 368, 373</a></span> (CA9 1989); <i>United States</i> v. <i>Esquilin,</i> <span class="citation" data-id="198872"><a href="/opinion/198872/united-states-v-esquilin/#317" aria-description="Citation for case: United States v. Esquilin">208 F. 3d 315, 317</a></span> (CA1 2000); <i>Davis</i> v. <i>United States,</i> <span class="citation" data-id="9694229"><a href="/opinion/1907111/davis-v-united-states/#1165" aria-description="Citation for case: Davis v. United States">724 A. 2d 1163, 1165-1166</a></span> (D. C. App. 1998).</p>
<p>[4]  Respondent Seibert argues that her second confession should be excluded from evidence under the doctrine known by the metaphor of the "fruit of the poisonous tree," developed in the Fourth Amendment context in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963): evidence otherwise admissible but discovered as a result of an earlier violation is excluded as tainted, lest the law encourage future violations. But the Court in <i>Elstad</i> rejected the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> fruits doctrine for analyzing the admissibility of a subsequent warned confession following "an initial failure . . . to administer the warnings required by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i>" <i>Elstad,</i> <span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/#300" aria-description="Citation for case: Oregon v. Elstad">470 U. S., at 300</a></span>. In <i>Elstad,</i> "a simple failure to administer the warnings, unaccompanied by any actual coercion or other circumstances calculated to undermine the suspect's ability to exercise his free will," did not "so tain[t] the investigatory process that a subsequent voluntary and informed waiver is ineffective for some indeterminate period. Though <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires that the unwarned admission must be suppressed, the admissibility of any subsequent statement should turn in these circumstances solely on whether it is knowingly and voluntarily made." <i>Id.,</i> at 309. <i>Elstad</i> held that "a suspect who has once responded to unwarned yet uncoercive questioning is not thereby disabled from waiving his rights and confessing after he has been given the requisite <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings." <i>Id.,</i> at 318. In a sequential confession case, clarity is served if the later confession is approached by asking whether in the circumstances the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings given could reasonably be found effective. If yes, a court can take up the standard issues of voluntary waiver and voluntary statement; if no, the subsequent statement is inadmissible for want of adequate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, because the earlier and later statements are realistically seen as parts of a single, unwarned sequence of questioning.</p>
<p>[5]  It bears emphasizing that the effectiveness <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> assumes the warnings can have must potentially extend through the repeated interrogation, since a suspect has a right to stop at any time. It seems highly unlikely that a suspect could retain any such understanding when the interrogator leads him a second time through a line of questioning the suspect has already answered fully. The point is not that a later unknowing or involuntary confession cancels out an earlier, adequate warning; the point is that the warning is unlikely to be effective in the question-first sequence we have described.</p>
<p>[6]  Because the intent of the officer will rarely be as candidly admitted as it was here (even as it is likely to determine the conduct of the interrogation), the focus is on facts apart from intent that show the question-first tactic at work.</p>
<p>[7]  We do not hold that a formal addendum warning that a previous statement could not be used would be sufficient to change the character of the question-first procedure to the point of rendering an ensuing statement admissible, but its absence is clearly a factor that blunts the efficacy of the warnings and points to a continuing, not a new, interrogation.</p>
<p>[8]  Because we find that the warnings were inadequate, there is no need to assess the actual voluntariness of the statement.</p>

</div>
```

---

## GROUP: content/cases/Mitchell v. Wisconsin.md  (`case`, 6 assertions)

### content_page

```
---
title: "Mitchell v. Wisconsin"
type: case
citation: "588 U.S. 840 (2019)"
parallel_cite: "139 S. Ct. 2525; 204 L. Ed. 2d 1040"
neutral_cite: ""
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2019
date_decided: 2019-06-27
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2019-06-27
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Mitchell v. Wisconsin
  varies_by_point: false
  scope_note: "Plurality opinion (Alito, J.); judgment supported by Thomas, J., concurring in the judgment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/9231242/mitchell-v-wisconsin/"
  cluster_id: 9231242
  opinion_id: 9226047
  identity_checked: true
homes:
  - page: "[[Destruction of Evidence]]"
    role: "Key — Progeny / Refinement"
  - page: "[[SIA Alcohol Tests]]"
    role: "Related (cross-doctrine)"
related: ["[[Missouri v. McNeely]]", "[[Schmerber v. California]]", "[[Birchfield v. North Dakota]]"]
aliases: []
tags: ["case", "fourth-amendment", "exigent-circumstances", "blood-draw", "dui", "unconscious-driver"]
holding: "When police have probable cause for DUI and the driver's unconsciousness/stupor forces hospitalization before a breath test can be…"
lake:
  record_id: Mitchell v. Wisconsin
  status: verified
  projected_at: 2026-07-06
---

# Mitchell v. Wisconsin

*588 U.S. 840 (2019)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Mitchell was arrested for drunk driving and grew too lethargic for a breath test, so officers took him to a hospital, where he became unconscious. Without a warrant, the officers directed a blood draw, which showed a blood-alcohol concentration well above the legal limit.

## Issue
Whether police may conduct a warrantless blood draw on an unconscious drunk-driving suspect who cannot be given a breath test.

## Rule
Generally yes (plurality). "When police have probable cause to believe a person has committed a drunk-driving offense and the driver's unconsciousness or stupor requires him to be taken to the hospital or similar facility before police have a reasonable opportunity to administer a standard evidentiary breath test, they may almost always order a warrantless blood test to measure the driver's BAC without offending the Fourth Amendment." — 139 S. Ct. at 2539 (plurality opinion). ^pin-2539

## Application
Mitchell was unconscious and so could not take a breath test, and his condition required hospitalization; the officers had probable cause to believe he had driven drunk. Under the plurality's rule, the [[Exigent Circumstances and Hot Pursuit|exigencies]] attending an unconscious driver almost always justify a warrantless blood draw. Because Mitchell had not had a chance to show that his was the unusual case in which a warrant would not have interfered with other pressing duties, the Court [[Reading and Citing Cases#on-remand|remanded]] for that purpose.

## Conclusion
[[Reading and Citing Cases#vacated|Vacated]] and [[Reading and Citing Cases#on-remand|remanded]]; the warrantless blood draw was generally permissible, subject to Mitchell's opportunity to show that his was an unusual case.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (Alito plurality; Thomas, J., concurring in the judgment).
- No negative treatment. *Mitchell* builds on the [[Exigent Circumstances and Hot Pursuit|exigency]] analysis of [[Missouri v. McNeely]] and [[Schmerber v. California]] for the unconscious-driver context.

## Appears on
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Progeny / Refinement*
- [[SIA Alcohol Tests]] — *Related (cross-doctrine)*

## Sources
- *Mitchell v. Wisconsin*, 588 U.S. 840 (2019) — https://www.courtlistener.com/opinion/9231242/mitchell-v-wisconsin/ — pinpoint: 139 S. Ct. 2539 (plurality, Part IV). (CL carries the official reporter text; cluster 9231242 → lead opinion 9226047. The pinpoint uses the S. Ct. reporter page carried in the CL text.)

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "206f9fb674cf335c", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "588 U.S. 840 (2019)", "court": "U.S. Supreme Court", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "139 S. Ct. 2525; 204 L. Ed. 2d 1040", "title": "Mitchell v. Wisconsin", "year": "2019"}}
{"assertion_id": "1d9127ac4b8fa899", "dimension": "support", "kind": "home_role", "locator": {"home": "Destruction of Evidence"}, "payload": {"home": "Destruction of Evidence", "role": "Key — Progeny / Refinement", "title": "Mitchell v. Wisconsin"}}
{"assertion_id": "5216ace5957d0c70", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "When police have probable cause for DUI and the driver's unconsciousness/stupor forces hospitalization before a breath test can be…", "title": "Mitchell v. Wisconsin"}}
{"assertion_id": "b9b4711466c88a53", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Alcohol Tests"}, "payload": {"home": "SIA Alcohol Tests", "role": "Related (cross-doctrine)", "title": "Mitchell v. Wisconsin"}}
{"assertion_id": "3a8a1856a65f2688", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Mitchell v. Wisconsin"}}
{"assertion_id": "a15757db58213f9a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2019-06-27", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Mitchell v. Wisconsin", "field_i_validity": "good_law", "scope_note": "Plurality opinion (Alito, J.); judgment supported by Thomas, J., concurring in the judgment.", "title": "Mitchell v. Wisconsin", "varies_by_point": "false"}}
```

### lake record — Mitchell v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "Mitchell v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Mitchell v. Wisconsin",
    "case_name_short": "",
    "case_name_full": "Gerald P. MITCHELL v. WISCONSIN",
    "input_case_name": "Mitchell v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2019-06-27",
    "year": 2019,
    "docket": null,
    "cluster_id": 9231242,
    "lead_opinion_id": 9226047,
    "sibling_ids": [
      9226047,
      9226048
    ],
    "absolute_url": "/opinion/9231242/mitchell-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4633470,
        "score": 120,
        "case_name": "Mitchell v. Wisconsin"
      },
      {
        "cluster_id": 9339798,
        "score": 20,
        "case_name": "Mitchell v. Wisconsin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "588 U.S. 840",
      "volume": "588",
      "reporter": "U.S.",
      "page": "840",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 2525",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "2525",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "204 L. Ed. 2d 1040",
        "volume": "204",
        "reporter": "L. Ed. 2d",
        "page": "1040",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "588 U.S. 840",
        "volume": "588",
        "reporter": "U.S.",
        "page": "840",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 2525",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "2525",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "204 L. Ed. 2d 1040",
        "volume": "204",
        "reporter": "L. Ed. 2d",
        "page": "1040",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "588 U.S. 840",
    "official_selection": {
      "court_class": "scotus",
      "selected": "588 U.S. 840",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-2539",
      "page": null,
      "quote": "--- # Mitchell v. Wisconsin *588 U.S. 840 (2019)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Mitchell was arrested for drunk driving and grew too lethargic for a breath test, so officers took him to a hospital, where he became unconscious. Without a warrant, the officers directed a blood draw, which showed a blood-alcohol concentration well above the legal limit. ## Issue Whether police may conduct a warrantless blood draw on an unconscious drunk-driving suspect who cannot be given a breath test. ## Rule Generally yes (plurality).",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2019-06-27",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Mitchell v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Alito, J.); judgment supported by Thomas, J., concurring in the judgment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Portulano",
          "cluster_id": 10135231,
          "cite": [
            "320 Or. App. 335",
            "514 P.3d 93"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Dawn M. Prado",
          "cluster_id": 4893130,
          "cite": [
            "960 N.W.2d 869",
            "2021 WI 64"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Miller",
          "cluster_id": 8248921,
          "cite": [
            "978 N.W.2d 19",
            "312 Neb. 17"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fuld v. Palestine Liberation Organization",
          "cluster_id": 9425200,
          "cite": [
            "82 F.4th 74"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nelson",
          "cluster_id": 9508065,
          "cite": [
            "970 N.W.2d 814",
            "2022 S.D. 12"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "L.B. v. United States",
          "cluster_id": 7857259,
          "cite": [
            "515 P.3d 818",
            "409 Mont. 505",
            "2022 MT 166"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Randall J. Weddle",
          "cluster_id": 4721814,
          "cite": [
            "224 A.3d 1035",
            "2020 ME 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Anderson",
          "cluster_id": 9498858,
          "cite": [
            "101 F.4th 586"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yancy Kevin Dieter",
          "cluster_id": 10109472,
          "cite": [
            "948 N.W.2d 431",
            "393 Wis. 2d 796",
            "2020 WI App 49"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Manubolu",
          "cluster_id": 5093549,
          "cite": [
            "13 F.4th 57"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Joshua Parks v. State of Arkansas",
          "cluster_id": 10607297,
          "cite": [
            "599 S.W.3d 382",
            "2020 Ark. App. 267"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Gerald P. Mitchell",
          "cluster_id": 10110635,
          "cite": [
            "978 N.W.2d 231",
            "404 Wis. 2d 103",
            "2022 WI App 31"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "The PEOPLE of the State of Colorado v. Glen Gary MONTOYA",
          "cluster_id": 10613799,
          "cite": [
            "546 P.3d 605"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Donnie Gene Richards",
          "cluster_id": 10109475,
          "cite": [
            "948 N.W.2d 359",
            "393 Wis. 2d 772",
            "2020 WI App 48"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Castro",
          "cluster_id": 10883712,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Valencia",
          "cluster_id": 10806666,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Denham",
          "cluster_id": 10797878,
          "cite": [
            "197 Wash. 2d 759",
            "489 P.3d 1138"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Indiana v. Dennis R Poland, Jr.",
          "cluster_id": 10681794,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Forrest R. Stewart v. State of Arkansas",
          "cluster_id": 10607993,
          "cite": [
            "611 S.W.3d 720",
            "2020 Ark. App. 515"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Louisiana v. Joseph W. Miller",
          "cluster_id": 10580798,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Mitchell v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(9226047 OR 9226048) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 36,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 36,
        "triage_read": 1,
        "triage_snippet_classified": 35
      },
      "lane2_top_cited": {
        "query": "cites:(9226047 OR 9226048)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9NjQ0OTA2OSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%289226047+OR+9226048%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 20,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(9226047 OR 9226048)",
        "reviewed": 14,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 14,
        "triage_read": 0,
        "triage_snippet_classified": 14
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(9226047 OR 9226048)",
    "indexed_citing_opinions": 46,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 9226047,
        "count": 46,
        "count_source": "search"
      },
      {
        "opinion_id": 9226048,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 153,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mitchell-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc2NTg0MTQmcz02NDQ5MDY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%289226047+OR+9226048%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T14:21:08Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T14:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T14:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T14:24:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T14:21:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Mitchell v. Wisconsin (truncated)

```
<opinion type="majority">
<p id="p-12">I</p>
<p id="p-13">A</p>
<p id="p-14">In <em>Birchfield</em> v. <em>North Dakota</em> , 579 U.S. ----, <extracted-citation case-ids="12597986" index="0" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct. 2160</a></span></extracted-citation>, <extracted-citation case-ids="12597986" index="1" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">195 L.Ed.2d 560</a></span></extracted-citation> (2016), we recounted the country's efforts over the years to address the terrible problem of drunk driving. Today, "all States have laws that prohibit motorists from driving with a [BAC] that exceeds a specified level." <em><extracted-citation case-ids="12597986" index="2" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12597986" index="3" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2166</a></span></extracted-citation>. And to help enforce BAC limits, every State has passed what are popularly called implied-consent laws. <em><extracted-citation case-ids="12597986" index="4" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Ibid.</a></span></extracted-citation></em> As "a condition of the privilege of" using the public roads, these laws require that drivers submit to BAC testing "when there is sufficient reason to believe they are violating the State's drunk-driving laws." <em><extracted-citation case-ids="12597986" index="5" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, ----, <extracted-citation case-ids="12597986" index="6" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2166" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2166</a></span>, 2169</extracted-citation>).</p>
<p id="p-15">Wisconsin's implied-consent law is much like those of the other 49 States and the District of Columbia. It deems drivers to have consented to breath or blood tests if an officer has reason to believe they have committed one of several drug- or alcohol-related offenses.<footnotemark>1</footnotemark> See <extracted-citation index="7" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"><span class="citation no-link">Wis. Stat. §§ 343.305</span></extracted-citation>(2), (3). Officers seeking to conduct a BAC test must read aloud a statement declaring their intent to administer the test and advising drivers of their options and the implications of their choice. § 343.305(4). If a driver's BAC level proves too high, his license will be suspended; but if he refuses testing, his license will be <em>revoked</em> and his refusal may be used against him in court. See <em>ibid</em> . No <a class="page-label" data-citation-index="1" data-label="2532" href="#p2532" id="p2532">*2532</a>test will be administered if a driver refuses-or, as the State would put it, "withdraws" his statutorily presumed consent. But "[a] person who is unconscious or otherwise not capable of withdrawing consent is presumed not to have" withdrawn it. § 343.305(3)(b). See also §§ 343.305(3)(ar) 1-2. More than half the States have provisions like this one regarding unconscious drivers.</p>
<p id="p-16">B</p>
<p id="p-17">The sequence of events that gave rise to this case began when Officer Alexander Jaeger of the Sheboygan Police Department received a report that petitioner Gerald Mitchell, appearing to be very drunk, had climbed into a van and driven off. Jaeger soon found Mitchell wandering near a lake. Stumbling and slurring his words, Mitchell could hardly stand without the support of two officers. Jaeger judged a field sobriety test hopeless, if not dangerous, and gave Mitchell a preliminary breath test. It registered a BAC level of 0.24%, triple the legal limit for driving in Wisconsin. Jaeger arrested Mitchell for operating a vehicle while intoxicated and, as is standard practice, drove him to a police station for a more reliable breath test using better equipment.</p>
<p id="p-18">On the way, Mitchell's condition continued to deteriorate-so much so that by the time the squad car had reached the station, he was too lethargic even for a breath test. Jaeger therefore drove Mitchell to a nearby hospital for a blood test; Mitchell lost consciousness on the ride over and had to be wheeled in. Even so, Jaeger read aloud to a slumped Mitchell the standard statement giving drivers a chance to refuse BAC testing. Hearing no response, Jaeger asked hospital staff to draw a blood sample. Mitchell remained unconscious while the sample was taken, and analysis of his blood showed that his BAC, about 90 minutes after his arrest, was 0.222%.</p>
<p id="p-19">Mitchell was charged with violating two related drunk-driving provisions. See §§ 346.63(1)(a), (b). He moved to suppress the results of the blood test on the ground that it violated his Fourth Amendment right against "unreasonable searches" because it was conducted without a warrant. Wisconsin chose to rest its response on the notion that its implied-consent law (together with Mitchell's free choice to drive on its highways) rendered the blood test a consensual one, thus curing any Fourth Amendment problem. In the end, the trial court denied Mitchell's motion to suppress, and a jury found him guilty of the charged offenses. The intermediate appellate court certified two questions to the Wisconsin Supreme Court: first, whether compliance with the State's implied-consent law was sufficient to show that Mitchell's test was consistent with the Fourth Amendment and, second, whether a warrantless blood draw from an unconscious person violates the Fourth Amendment. See <extracted-citation case-ids="12556993" index="8" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">2018 WI 84</a></span></extracted-citation>, ¶15, <extracted-citation case-ids="12556993" index="9" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">383 Wis.2d 192</a></span></extracted-citation>, 202-203, <extracted-citation case-ids="12556993" index="10" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">914 N.W.2d 151</a></span></extracted-citation>, 155-156 (2018). The Wisconsin Supreme Court affirmed Mitchell's convictions, and we granted certiorari, 586 U.S. ----, <extracted-citation case-ids="12624625,12624626,12624627,12624628,12624629,12624630" index="11" url="https://cite.case.law/s-ct/139/915/"><span class="citation" data-id="9335135"><a href="/opinion/9339797/simply-wireless-inc-v-t-mobile-us-inc/" aria-description="Citation for case: Simply Wireless, Inc. v. T-Mobile U.S., Inc.">139 S.Ct. 915</a></span></extracted-citation>, <extracted-citation case-ids="12624626" index="12" url="https://cite.case.law/s-ct/139/915/12624626/"><span class="citation" data-id="9335136"><a href="/opinion/9339798/mitchell-v-wisconsin/" aria-description="Citation for case: Mitchell v. Wisconsin">202 L.Ed.2d 642</a></span></extracted-citation> (2019), to decide "[w]hether a statute authorizing a blood draw from an unconscious motorist provides an exception to the Fourth Amendment warrant requirement," Pet. for Cert. ii.</p>
<p id="p-20">II</p>
<p id="p-21">In considering Wisconsin's implied-consent law, we do not write on a blank slate. "Our prior opinions have referred approvingly to the general concept of implied-consent laws that impose civil penalties and evidentiary consequences on motorists who refuse to comply." <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="13" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2185</a></span></extracted-citation>. But <a class="page-label" data-citation-index="1" data-label="2533" href="#p2533" id="p2533">*2533</a>our decisions have not rested on the idea that these laws do what their popular name might seem to suggest-that is, create actual consent to all the searches they authorize. Instead, we have based our decisions on the precedent regarding the specific constitutional claims in each case, while keeping in mind the wider regulatory scheme developed over the years to combat drunk driving. That scheme is centered on legally specified BAC limits for drivers-limits enforced by the BAC tests promoted by implied-consent laws.</p>
<p id="p-22">Over the last 50 years, we have approved many of the defining elements of this scheme. We have held that forcing drunk-driving suspects to undergo a blood test does not violate their constitutional right against self-incrimination. See <em>Schmerber v. California</em> , <extracted-citation case-ids="12047531" index="14" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span></extracted-citation>, 765, <extracted-citation case-ids="12047531" index="15" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="16" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">16 L.Ed.2d 908</a></span></extracted-citation> (1966). Nor does using their refusal against them in court. See <em>South Dakota v. Neville</em> , <extracted-citation case-ids="6200055" index="17" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U.S. 553</a></span></extracted-citation>, 563, <extracted-citation case-ids="6200055" index="18" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>, <extracted-citation case-ids="6200055" index="19" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">74 L.Ed.2d 748</a></span></extracted-citation> (1983). And punishing that refusal with automatic license revocation does not violate drivers' due process rights if they have been arrested upon probable cause, <em>Mackey v. Montrym</em> , <extracted-citation case-ids="6179408" index="20" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">443 U.S. 1</a></span></extracted-citation>, <extracted-citation case-ids="6179408" index="21" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">99 S.Ct. 2612</a></span></extracted-citation>, <extracted-citation case-ids="6179408" index="22" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">61 L.Ed.2d 321</a></span></extracted-citation> (1979) ; on the contrary, this kind of summary penalty is "unquestionably legitimate." <em>Neville</em> , <em>supra</em> , at 560, <extracted-citation case-ids="6200055" index="23" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>.</p>
<p id="p-23">These cases generally concerned the Fifth and Fourteenth Amendments, but motorists charged with drunk driving have also invoked the Fourth Amendment's ban on "unreasonable searches" since BAC tests are "searches." See <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="24" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2173</a></span></extracted-citation>. Though our precedent normally requires a warrant for a lawful search, there are well-defined exceptions to this rule. In <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , we applied precedent on the "search-incident-to-arrest" exception to BAC testing of conscious drunk-driving suspects. We held that their drunk-driving arrests, taken alone, justify warrantless breath tests but not blood tests, since breath tests are less intrusive, just as informative, and (in the case of conscious suspects) readily available. <em><extracted-citation case-ids="12597986" index="25" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12597986" index="26" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span>-85</extracted-citation>.</p>
<p id="p-24">We have also reviewed BAC tests under the "exigent circumstances" exception-which, as noted, allows warrantless searches "to prevent the imminent destruction of evidence." <em>Missouri v. McNeely</em> , <extracted-citation case-ids="12697040" index="27" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S. 141</a></span></extracted-citation>, 149, <extracted-citation case-ids="12697040" index="28" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="29" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">185 L.Ed.2d 696</a></span></extracted-citation> (2013). In <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , we were asked if this exception covers BAC testing of drunk-driving suspects in light of the fact that blood-alcohol evidence is always dissipating due to "natural metabolic processes." <em><extracted-citation case-ids="12697040" index="30" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 152, <extracted-citation case-ids="12697040" index="31" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. We answered that the fleeting quality of BAC evidence alone is not enough. <em><extracted-citation case-ids="12697040" index="32" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 156, <extracted-citation case-ids="12697040" index="33" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. But in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> it <em>did</em> justify a blood test of a drunk driver who had gotten into a car accident that gave police other pressing duties, for then the "<em>further</em> delay" caused by a warrant application really "<em>would</em> have threatened the destruction of evidence." <em>McNeely</em> , <em>supra</em> , at 152, <extracted-citation case-ids="12697040" index="34" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (emphasis added).</p>
<p id="p-25">Like <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , this case sits much higher than <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> on the exigency spectrum. <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> was about the minimum degree of urgency common to all drunk-driving cases. In <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , a car accident heightened that urgency. And here Mitchell's medical condition did just the same.</p>
<p id="p-26">Mitchell's stupor and eventual unconsciousness also deprived officials of a reasonable opportunity to administer a breath test. To be sure, Officer Jaeger managed to conduct "a preliminary breath test" using a portable machine when he first encountered Mitchell at the lake. App. to Pet.</p>
<p id="p-27"><a class="page-label" data-citation-index="1" data-label="2534" href="#p2534" id="p2534">*2534</a>for Cert. 60a. But he had no reasonable opportunity to give Mitchell a breath test using "evidence-grade breath testing machinery." <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="35" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2192" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2192</a></span></extracted-citation> (SOTOMAYOR, J., concurring in part and dissenting in part). As a result, it was reasonable for Jaeger to seek a better breath test at the station; he acted with reasonable dispatch to procure one; and when Mitchell's condition got in the way, it was reasonable for Jaeger to pursue a blood test. As Justice SOTOMAYOR explained in her partial dissent in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> :</p>
<blockquote id="p-28">"There is a common misconception that breath tests are conducted roadside, immediately after a driver is arrested. While some preliminary testing is conducted roadside, reliability concerns with roadside tests confine their use in most circumstances to establishing probable cause for an arrest.... The standard evidentiary breath test is conducted after a motorist is arrested and transported to a police station, governmental building, or mobile testing facility where officers can access reliable, evidence-grade breath testing machinery." <em><extracted-citation case-ids="12597986" index="36" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12597986" index="37" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2192</a></span></extracted-citation>.</blockquote>
<p id="p-29">Because the "standard evidentiary breath test is conducted after a motorist is arrested and transported to a police station" or another appropriate facility, <em><extracted-citation case-ids="12597986" index="38" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">ibid.</a></span></extracted-citation></em> , the important question here is what officers may do when a driver's unconsciousness (or stupor) eliminates any reasonable opportunity for <em>that</em> kind of breath test.</p>
<p id="p-30">III</p>
<p id="p-31">The Fourth Amendment guards the "right of the people to be secure in their persons ... against unreasonable searches" and provides that "no Warrants shall issue, but upon probable cause." A blood draw is a search of the person, so we must determine if its administration here without a warrant was reasonable. See <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S. at ----, <extracted-citation case-ids="12597986" index="39" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2174</a></span></extracted-citation>. Though we have held that a warrant is normally required, we have also "made it clear that there are exceptions to the warrant requirement." <em>Illinois v. McArthur</em> , <extracted-citation case-ids="9505639" index="40" url="https://cite.case.law/us/531/326/#p330"><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">531 U.S. 326</a></span></extracted-citation>, 330, <extracted-citation case-ids="9505639" index="41" url="https://cite.case.law/us/531/326/#p330"><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">121 S.Ct. 946</a></span></extracted-citation>, <extracted-citation case-ids="9505639" index="42" url="https://cite.case.law/us/531/326/#p330"><span class="citation" data-id="9434039"><a href="/opinion/118405/illinois-v-mcarthur/" aria-description="Citation for case: Illinois v. McArthur">148 L.Ed.2d 838</a></span></extracted-citation> (2001). And under the exception for exigent circumstances, a warrantless search is allowed when " 'there is compelling need for official action and no time to secure a warrant.' " <em>McNeely</em> , <em>supra</em> , at 149, <extracted-citation case-ids="12697040" index="43" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (quoting <em>Michigan v. Tyler</em> , <extracted-citation case-ids="1490288" index="44" url="https://cite.case.law/us/436/499/#p509"><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">436 U.S. 499</a></span></extracted-citation>, 509, <extracted-citation case-ids="1490288" index="45" url="https://cite.case.law/us/436/499/#p509"><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">98 S.Ct. 1942</a></span></extracted-citation>, <extracted-citation case-ids="1490288" index="46" url="https://cite.case.law/us/436/499/#p509"><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">56 L.Ed.2d 486</a></span></extracted-citation> (1978) ). In <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , we considered how the exigent-circumstances exception applies to the broad category of cases in which a police officer has probable cause to believe that a motorist was driving under the influence of alcohol, and we do not revisit that question. Nor do we settle whether the exigent-circumstances exception covers the specific facts of this case.<footnotemark>2</footnotemark> Instead, we address how the exception <a class="page-label" data-citation-index="1" data-label="2535" href="#p2535" id="p2535">*2535</a>bears on the category of cases encompassed by the question on which we granted certiorari-those involving unconscious drivers.<footnotemark>3</footnotemark> In those cases, the need for a blood test is compelling, and an officer's duty to attend to more pressing needs may leave no time to seek a warrant.</p>
<p id="p-32">A</p>
<p id="p-33">The importance of the needs served by BAC testing is hard to overstate. The bottom line is that BAC tests are needed for enforcing laws that save lives. The specifics, in short, are these: Highway safety is critical; it is served by laws that criminalize driving with a certain BAC level; and enforcing these legal BAC limits requires efficient testing to obtain BAC evidence, which naturally dissipates. So BAC tests are crucial links in a chain on which vital interests hang. And when a breath test is unavailable to advance those aims, a blood test becomes essential. Here we add a word about each of these points.</p>
<p id="p-34"><em>First</em> , highway safety is a vital public interest. For decades, we have strained our vocal chords to give adequate expression to the stakes. We have called highway safety a "compelling interest," <em>Mackey</em> , <extracted-citation case-ids="6179408" index="47" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">443 U.S., at 19</a></span></extracted-citation>, <extracted-citation case-ids="6179408" index="48" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">99 S.Ct. 2612</a></span></extracted-citation> ; we have called it "paramount," <em><extracted-citation case-ids="6179408" index="49" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">id.</a></span></extracted-citation></em> , at 17, <extracted-citation case-ids="6179408" index="50" url="https://cite.case.law/us/443/1/"><span class="citation" data-id="9427652"><a href="/opinion/110126/mackey-v-montrym/" aria-description="Citation for case: MacKey v. Montrym">99 S.Ct. 2612</a></span></extracted-citation>. Twice we have referred to the effects of irresponsible driving as "slaughter" comparable to the ravages of war. <em>Breithaupt v. Abram</em> , <extracted-citation case-ids="6161761" index="51" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">352 U.S. 432</a></span></extracted-citation>, 439, <extracted-citation case-ids="6161761" index="52" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">77 S.Ct. 408</a></span></extracted-citation>, <extracted-citation case-ids="6161761" index="53" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">1 L.Ed.2d 448</a></span></extracted-citation> (1957) ; <em>Perez v. Campbell</em> , <extracted-citation case-ids="11735156" index="54" url="https://cite.case.law/us/402/637/#p657"><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/" aria-description="Citation for case: Perez. v. Campbell">402 U.S. 637</a></span></extracted-citation>, 657, 672, <extracted-citation case-ids="11735156" index="55" url="https://cite.case.law/us/402/637/#p657"><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/" aria-description="Citation for case: Perez. v. Campbell">91 S.Ct. 1704</a></span></extracted-citation>, <extracted-citation case-ids="11735156" index="56" url="https://cite.case.law/us/402/637/#p657"><span class="citation" data-id="9424589"><a href="/opinion/108350/perez-v-campbell/" aria-description="Citation for case: Perez. v. Campbell">29 L.Ed.2d 233</a></span></extracted-citation> (1971) (Blackmun, J., concurring in result in part and dissenting in part). We have spoken of "carnage," <em>Neville</em> , <extracted-citation case-ids="6200055" index="57" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U.S., at 558</a></span>-559</extracted-citation>, <extracted-citation case-ids="6200055" index="58" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>, and even "frightful carnage," <em>Tate v. Short</em> , <extracted-citation case-ids="11712570" index="59" url="https://cite.case.law/us/401/395/#p401"><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">401 U.S. 395</a></span></extracted-citation>, 401, <extracted-citation case-ids="11712570" index="60" url="https://cite.case.law/us/401/395/#p401"><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">91 S.Ct. 668</a></span></extracted-citation>, <extracted-citation case-ids="11712570" index="61" url="https://cite.case.law/us/401/395/#p401"><span class="citation" data-id="9424475"><a href="/opinion/108282/tate-v-short/" aria-description="Citation for case: Tate v. Short">28 L.Ed.2d 130</a></span></extracted-citation> (1971) (Blackmun, J., concurring). The frequency of preventable collisions, we have said, is "tragic," <em>Neville</em> , <em>supra</em> , at 558, <extracted-citation case-ids="6200055" index="62" url="https://cite.case.law/us/459/553/#p563"><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">103 S.Ct. 916</a></span></extracted-citation>, and "astounding,"</p>
<p id="p-35"><a class="page-label" data-citation-index="1" data-label="2536" href="#p2536" id="p2536">*2536</a><em>Breithaupt</em> , <em>supra</em> , at 439, <extracted-citation case-ids="6161761" index="63" url="https://cite.case.law/us/352/432/#p439"><span class="citation" data-id="9421383"><a href="/opinion/105456/breithaupt-v-abram/" aria-description="Citation for case: Breithaupt v. Abram">77 S.Ct. 408</a></span></extracted-citation>. And behind this fervent language lie chilling figures, all captured in the fact that from 1982 to 2016, alcohol-related accidents took roughly 10,000 to 20,000 lives in this Nation <em>every single year</em> . See National Highway Traffic Safety Admin. (NHTSA), Traffic Safety Facts 2016, p. 40 (May 2018). In the best years, that would add up to more than one fatality per hour.</p>
<p id="p-36"><em>Second</em> , when it comes to fighting these harms and promoting highway safety, federal and state lawmakers have long been convinced that specified BAC limits make a big difference. States resorted to these limits when earlier laws that included no "statistical definition of intoxication" proved ineffectual or hard to enforce. See <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ---- - ----, <extracted-citation case-ids="12597986" index="64" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2167</a></span></extracted-citation>. The maximum permissible BAC, initially set at 0.15%, was first lowered to 0.10% and then to 0.08%. <em><extracted-citation case-ids="12597986" index="65" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, ---- - ----, <extracted-citation case-ids="12597986" index="66" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2167" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2167</a></span>, 2168-69</extracted-citation>. Congress encouraged this process by conditioning the award of federal highway funds on the establishment of a BAC limit of 0.08%, see 23 U.S. C. § 163(a) ; <extracted-citation index="67" url="https://cite.case.law/citations/?q=23%20C.F.R.%20%C2%A7%201225.1"><span class="citation no-link">23 CFR § 1225.1</span></extracted-citation> (2012), and every State has adopted this limit.<footnotemark>4</footnotemark> Not only that, many States, including Wisconsin, have passed laws imposing increased penalties for recidivists or for drivers with a BAC level that exceeds a higher threshold. See <extracted-citation index="68" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%20346.65"><span class="citation no-link">Wis. Stat. § 346.65</span></extracted-citation>(2)(am) ; <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , 579 U.S., at ----, <extracted-citation case-ids="12597986" index="69" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2169</a></span></extracted-citation>.</p>
<p id="p-37">There is good reason to think this strategy has worked. As we noted in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , these tougher measures corresponded with a dramatic drop in highway deaths and injuries: From the mid-1970's to the mid-1980's, "the number of annual fatalities averaged 25,000; by 2014 ..., the number had fallen to below 10,000." <em><extracted-citation case-ids="12597986" index="70" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12597986" index="71" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2169</a></span></extracted-citation>.</p>
<p id="p-38"><em>Third</em> , enforcing BAC limits obviously requires a test that is accurate enough to stand up in court, <em><extracted-citation case-ids="12597986" index="72" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">id.</a></span></extracted-citation></em> , at ---- - ----, <extracted-citation case-ids="12597986" index="73" url="https://cite.case.law/s-ct/136/2160/">136 S.Ct., at </extracted-citation>2167-68 ; see also <em>McNeely</em> , <extracted-citation case-ids="12697040" index="74" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 159</a></span>-160</extracted-citation>, <extracted-citation case-ids="12697040" index="75" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (plurality opinion). And we have recognized that "[e]xtraction of blood samples for testing is a highly effective means of" measuring "the influence of alcohol." <em>Schmerber</em> , <extracted-citation case-ids="12047531" index="76" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 771</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="77" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</p>
<p id="p-39">Enforcement of BAC limits also requires prompt testing because it is "a biological certainty" that "[a]lcohol dissipates from the bloodstream at a rate of 0.01 percent to 0.025 percent per hour.... Evidence is literally disappearing by the minute." <em>McNeely</em> , <extracted-citation case-ids="12697040" index="78" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 169</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="79" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of ROBERTS, C.J.). As noted, the ephemeral nature of BAC was "essential to our holding in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> ," which itself allowed a warrantless blood test for BAC. <em><extracted-citation case-ids="12697040" index="80" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.</a></span></extracted-citation></em> , at 152, <extracted-citation case-ids="12697040" index="81" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of the Court). And even when we later held that the exigent-circumstances exception would not permit a warrantless blood draw in <em>every</em> drunk-driving case, we acknowledged that delays in BAC testing can "raise questions about ... accuracy." <em><extracted-citation case-ids="12697040" index="82" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 156, <extracted-citation case-ids="12697040" index="83" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</p>
<p id="p-40">It is no wonder, then, that the implied-consent laws that incentivize prompt BAC testing have been with us for 65 years and now exist in all 50 States. <em>Birchfield</em> , <em>supra</em> , at ----, <extracted-citation case-ids="12597986" index="84" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2169</a></span></extracted-citation>. These laws and the BAC tests they require are tightly linked to a regulatory scheme that serves the most pressing of interests.</p>
<p id="p-41">Finally, when a breath test is unavailable to promote those interests, "a blood draw becomes necessary."</p>
<p id="p-42"><a class="page-label" data-citation-index="1" data-label="2537" href="#p2537" id="p2537">*2537</a><em>McNeely</em> , <extracted-citation case-ids="12697040" index="85" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 170</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="86" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of ROBERTS, C.J.). Thus, in the case of unconscious drivers, who cannot blow into a breathalyzer, blood tests are essential for achieving the compelling interests described above.</p>
<p id="p-43">Indeed, not only is the link to pressing interests here tighter; the interests themselves are greater: Drivers who are drunk enough to pass out at the wheel or soon afterward pose a much greater risk. It would be perverse if the more wanton behavior were rewarded-if the more harrowing threat were harder to punish.</p>
<p id="p-44">For these reasons, there clearly is a "compelling need" for a blood test of drunk-driving suspects whose condition deprives officials of a reasonable opportunity to conduct a breath test. <em><extracted-citation case-ids="12697040" index="87" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="87" url="https://cite.case.law/us/569/141/#p149"> at 149</extracted-citation>, <extracted-citation case-ids="12697040" index="88" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of the Court) (internal quotation marks omitted). The only question left, under our exigency doctrine, is whether this compelling need justifies a warrantless search because there is, furthermore, " 'no time to secure a warrant.' " <em><extracted-citation case-ids="12697040" index="89" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Ibid.</a></span></extracted-citation></em></p>
<p id="p-45">B</p>
<p id="p-46">We held that there was no time to secure a warrant before a blood test of a drunk-driving suspect in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> because the officer there could "reasonably have believed that he was confronted with an emergency, in which the delay necessary to obtain a warrant, under the circumstances, threatened the destruction of evidence." <extracted-citation case-ids="12047531" index="90" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 770</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="91" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation> (internal quotation marks omitted). So even if the constant dissipation of BAC evidence <em>alone</em> does not create an exigency, see <em>McNeely</em> , <em>supra</em> , at 150-151, <extracted-citation case-ids="12697040" index="92" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> shows that it does so when combined with other pressing needs:</p>
<blockquote id="p-47">"We are told that [1] the percentage of alcohol in the blood begins to diminish shortly after drinking stops, as the body functions to eliminate it from the system. Particularly in a case such as this, where [2] time had to be taken to bring the accused to a hospital and to investigate the scene of the accident, there was no time to seek out a magistrate and secure a warrant. Given these special facts, we conclude that the attempt to secure evidence of blood-alcohol content in this case [without a warrant] was ... appropriate ...." <extracted-citation case-ids="12047531" index="93" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 770</a></span>-771</extracted-citation>, <extracted-citation case-ids="12047531" index="94" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</blockquote>
<p id="p-48">Thus, exigency exists when (1) BAC evidence is dissipating and (2) some other factor creates pressing health, safety, or law enforcement needs that would take priority over a warrant application. Both conditions are met when a drunk-driving suspect is unconscious, so <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> controls: With such suspects, too, a warrantless blood draw is lawful.</p>
<p id="p-49">1</p>
<p id="p-50">In <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , the extra factor giving rise to urgent needs that would only add to the delay caused by a warrant application was a car accident; here it is the driver's unconsciousness. Indeed, unconsciousness does not just create pressing needs; it is <em>itself</em> a medical emergency.<footnotemark>5</footnotemark> It means that the suspect will have to be rushed to the hospital or similar facility not just for the blood test itself but for urgent medical care.<footnotemark>6</footnotemark> Police can reasonably anticipate that such a driver might require monitoring, <a class="page-label" data-citation-index="1" data-label="2538" href="#p2538" id="p2538">*2538</a>positioning, and support on the way to the hospital;<footnotemark>7</footnotemark> that his blood may be drawn anyway, for diagnostic purposes, immediately on arrival;<footnotemark>8</footnotemark> and that immediate medical treatment could delay (or otherwise distort the results of) a blood draw conducted later, upon receipt of a warrant, thus reducing its evidentiary value. See <em>McNeely</em> , <em>supra</em> , at 156, <extracted-citation case-ids="12697040" index="95" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (plurality opinion). All of that sets this case apart from the uncomplicated drunk-driving scenarios addressed in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> . Just as the ramifications of a car accident pushed <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> over the line into exigency, so does the condition of an unconscious driver bring his blood draw under the exception. In such a case, as in <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , an officer could "reasonably have believed that he was confronted with an emergency." <extracted-citation case-ids="12047531" index="96" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 770</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="97" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</p>
<p id="p-51">Indeed, in many unconscious-driver cases, the exigency will be <em>more</em> acute, as elaborated in the briefing and argument in this case. A driver so drunk as to lose consciousness is quite likely to crash, especially if he passes out before managing to park. And then the accident might give officers a slew of urgent tasks beyond that of securing (and working around) medical care for the suspect. Police may have to ensure that others who are injured receive prompt medical attention; they may have to provide first aid themselves until medical personnel arrive at the scene. In some cases, they may have to deal with fatalities. They may have to preserve evidence at the scene and block or redirect traffic to prevent further accidents. These pressing matters, too, would require responsible officers to put off applying for a warrant, and that would only exacerbate the delay-and imprecision-of any subsequent BAC test.</p>
<p id="p-52">In sum, all these rival priorities would put officers, who must often engage in a form of triage, to a dilemma. It would force them to choose between prioritizing a warrant application, to the detriment of critical health and safety needs, and delaying the warrant application, and thus the BAC test, to the detriment of its evidentiary value and all the compelling interests served by BAC limits. This is just the kind of scenario for which the exigency rule was born-just the kind of grim dilemma it lives to dissolve.</p>
<p id="p-53">2</p>
<p id="p-54">Mitchell objects that a warrantless search is unnecessary in cases involving unconscious drivers because warrants these days can be obtained faster and <a class="page-label" data-citation-index="1" data-label="2539" href="#p2539" id="p2539">*2539</a>more easily. But even in our age of rapid communication,</p>
<blockquote id="p-55">"[w]arrants inevitably take some time for police officers or prosecutors to complete and for magistrate judges to review. Telephonic and electronic warrants may still require officers to follow time-consuming formalities designed to create an adequate record, such as preparing a duplicate warrant before calling the magistrate judge.... And improvements in communications technology do not guarantee that a magistrate judge will be available when an officer needs a warrant after making a late-night arrest." <em>McNeely</em> , <extracted-citation case-ids="12697040" index="98" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 155</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="99" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</blockquote>
<p id="p-56">In other words, with better technology, the time required has shrunk, but it has not disappeared. In the emergency scenarios created by unconscious drivers, forcing police to put off other tasks for even a relatively short period of time may have terrible collateral costs. That is just what it means for these situations to <em>be</em> emergencies.</p>
<p id="p-57">IV</p>
<p id="p-58">When police have probable cause to believe a person has committed a drunk-driving offense and the driver's unconsciousness or stupor requires him to be taken to the hospital or similar facility before police have a reasonable opportunity to administer a standard evidentiary breath test, they may almost always order a warrantless blood test to measure the driver's BAC without offending the Fourth Amendment. We do not rule out the possibility that in an unusual case a defendant would be able to show that his blood would not have been drawn if police had not been seeking BAC information, and that police could not have reasonably judged that a warrant application would interfere with other pressing needs or duties. Because Mitchell did not have a chance to attempt to make that showing, a remand for that purpose is necessary.</p>
<p id="p-59">* * *</p>
<p id="p-60">The judgment of the Supreme Court of Wisconsin is vacated, and the case is remanded for further proceedings.</p>
<p id="p-61">It is so ordered.</p>
<p id="p-62">Justice THOMAS, concurring in the judgment.</p>
<p id="p-63">Today, the plurality adopts a difficult-to-administer rule: Exigent circumstances are generally present when police encounter a person suspected of drunk driving-except when they aren't. Compare <em>ante</em> , at 2537, with <em>ante</em> , at 2539. The plurality's presumption will rarely be rebutted, but it will nevertheless burden both officers and courts who must attempt to apply it. "The better (and far simpler) way to resolve" this case is to apply "the <em>per se</em> rule" I proposed in <em>Missouri v. McNeely</em> , <extracted-citation case-ids="12697040" index="100" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S. 141</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="101" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="102" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">185 L.Ed.2d 696</a></span></extracted-citation> (2013) (dissenting opinion). <em>Birchfield</em> v. <em>North Dakota</em> , 579 U.S. ----, ----, <extracted-citation case-ids="12597986" index="103" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct. 2160</a></span></extracted-citation>, 2197, <extracted-citation case-ids="12597986" index="104" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">195 L.Ed.2d 560</a></span></extracted-citation> (2016) (THOMAS, J., concurring in judgment in part and dissenting in part). Under that rule, the natural metabolization of alcohol in the blood stream " 'creates an exigency once police have probable cause to believe the driver is drunk,' " regardless of whether the driver is conscious. <em><extracted-citation case-ids="12597986" index="105" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12597986" index="106" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2198</a></span></extracted-citation>. Because I am of the view that the Wisconsin Supreme Court should apply that rule on remand, I concur only in the judgment.</p>
<p id="p-64">I</p>
<p id="p-65">The Fourth Amendment provides that "[t]he right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated." Although the Fourth Amendment does not, by its text, <a class="page-label" data-citation-index="1" data-label="2540" href="#p2540" id="p2540">*2540</a>require that searches be supported by a warrant, see <em>Groh v. Ramirez</em> , <extracted-citation case-ids="8897610" index="107" url="https://cite.case.law/us/540/551/#p571"><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/" aria-description="Citation for case: Groh v. Ramirez">540 U.S. 551</a></span></extracted-citation>, 571-573, <extracted-citation case-ids="8897610" index="108" url="https://cite.case.law/us/540/551/#p571"><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/" aria-description="Citation for case: Groh v. Ramirez">124 S.Ct. 1284</a></span></extracted-citation>, <extracted-citation case-ids="8897610" index="109" url="https://cite.case.law/us/540/551/#p571"><span class="citation" data-id="9434540"><a href="/opinion/131161/groh-v-ramirez/" aria-description="Citation for case: Groh v. Ramirez">157 L.Ed.2d 1068</a></span></extracted-citation> (2004) (THOMAS, J., dissenting), "this Court has inferred that a warrant must generally be secured" for a search to comply with the Fourth Amendment, <em>Kentucky v. King</em> , <extracted-citation case-ids="5911971,12458997" index="110" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S. 452</a></span></extracted-citation>, 459, <extracted-citation case-ids="5911971,12458997" index="111" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="112" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span></extracted-citation> (2011). We have also recognized, however, that this warrant presumption "may be overcome in some circumstances because '[t]he ultimate touchstone of the Fourth Amendment is "reasonableness." ' " <em><extracted-citation case-ids="5911971,12458997" index="113" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">Ibid.</a></span></extracted-citation></em> Accordingly, we have held that "the warrant requirement is subject to certain reasonable exceptions." <em><extracted-citation case-ids="5911971,12458997" index="114" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">Ibid.</a></span></extracted-citation></em></p>
<p id="p-66">In recent years, this Court has twice considered whether warrantless blood draws fall within an exception to the warrant requirement. First, in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , a divided court held that the natural metabolization of alcohol in the bloodstream does not present a <em>per se</em> exigency that justifies an exception to the Fourth Amendment's warrant requirement. <extracted-citation case-ids="12697040" index="115" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 145</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="116" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. Then, in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , we held that blood draws may not be administered as a search incident to a lawful arrest for drunk driving. 579 U.S., at ----, <extracted-citation case-ids="12597986" index="117" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span>-85</extracted-citation>. The question we face in this case is whether the blood draw here fell within one of the "reasonable exceptions" to the warrant requirement.</p>
<p id="p-67">II</p>
<p id="p-68">The "exigent circumstances" exception applies when "the needs of law enforcement [are] so compelling that [a] warrantless search is objectively reasonable under the Fourth Amendment." <em>King</em> , <extracted-citation case-ids="5911971,12458997" index="118" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S., at 460</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="119" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation> (internal quotation marks omitted). Applying this doctrine, the Court has held that officers may conduct a warrantless search when failure to act would result in "the imminent destruction of evidence." <em><extracted-citation case-ids="5911971,12458997" index="120" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">Ibid.</a></span></extracted-citation></em> (internal quotation marks omitted).</p>
<p id="p-69">As I have explained before, "the imminent destruction of evidence" is a risk in every drunk-driving arrest and thus "implicates the exigent-circumstances doctrine." <em>McNeely</em> , <extracted-citation case-ids="12697040" index="121" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 178</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="122" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. "Once police arrest a suspect for drunk driving, each passing minute eliminates probative evidence of the crime" as alcohol dissipates from the bloodstream. <em><extracted-citation case-ids="12697040" index="123" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.</a></span></extracted-citation></em> , at 177, <extracted-citation case-ids="12697040" index="124" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. In many States, this "rapid destruction of evidence," <em><extracted-citation case-ids="12697040" index="125" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="125" url="https://cite.case.law/us/569/141/#p149"> at 178</extracted-citation>, <extracted-citation case-ids="12697040" index="126" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, is particularly problematic because the penalty for drunk driving depends in part on the driver's blood alcohol concentration, see <em>ante</em> , at 2536. Because the provisions of Wisconsin law at issue here allow blood draws only when the driver is suspected of impaired driving, <em>ante</em> , at 2531 - 2532, they fit easily within the exigency exception to the warrant requirement.</p>
<p id="p-70">Instead of adopting this straightforward rule, the plurality makes a flawed distinction between ordinary drunk-driving cases in which blood alcohol concentration evidence "is dissipating" and those that also include "some other [pressing] factor." <em>Ante</em> , at 2533, 2537, 2539. But whether "some other factor creates pressing health, safety, or law-enforcement needs that would take priority over a warrant application" is irrelevant. <em>Ante</em> , at 2537. When police have probable cause to conclude that an individual was driving drunk, probative evidence is dissipating by the minute. And that evidence dissipates regardless of whether police had another reason to draw the driver's blood or whether "a warrant application would interfere with other pressing needs or duties." <em>Ante</em> , at 2539. The destruction of evidence alone is sufficient to justify a warrantless search based on exigent circumstances. See generally <a class="page-label" data-citation-index="1" data-label="2541" href="#p2541" id="p2541">*2541</a><em>McNeely</em> , <extracted-citation case-ids="12697040" index="127" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 176</a></span>-179</extracted-citation>, <extracted-citation case-ids="12697040" index="128" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of THOMAS, J.).</p>
<p id="p-71">Presumably, the plurality draws these lines to avoid overturning <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> . See <em><extracted-citation case-ids="12697040" index="129" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.</a></span></extracted-citation></em> , at 156, <extracted-citation case-ids="12697040" index="130" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (majority opinion) (holding that "the natural dissipation of alcohol in the blood" does not "categorically" support a finding of exigency). But <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> was wrongly decided, see <em><extracted-citation case-ids="12697040" index="131" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.</a></span></extracted-citation></em> , at 176-183, <extracted-citation case-ids="12697040" index="132" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (opinion of THOMAS, J.), and our decision in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> has already undermined its rationale. Specifically, the Court determined in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> that "[t]he context of blood testing is different in critical respects from other destruction-of-evidence cases in which the police are truly confronted with a now or never situation." <extracted-citation case-ids="12697040" index="133" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 153</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="134" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (majority opinion) (internal quotation marks omitted). But the Court stated in <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> that a distinction between "an arrestee's active destruction of evidence and the loss of evidence due to a natural process makes little sense." 579 U.S., at ----, <extracted-citation case-ids="12597986" index="135" url="https://cite.case.law/s-ct/136/2160/">136 S.Ct., at </extracted-citation>2182 ; see also <em>ante</em> , at 2536 - 2537. Moreover, to the extent <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> was grounded in the belief that a <em>per se</em> rule was inconsistent with the "case by case," "totality of the circumstances" analysis ordinarily applied in exigent-circumstances cases, see <extracted-citation case-ids="12697040" index="136" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 156</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="137" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, that rationale was suspect from the start. That the exigent-circumstances exception might ordinarily require "an evaluation of the particular facts of each case," <em>Birchfield</em> , <em>supra</em> , at ----, <extracted-citation case-ids="12597986" index="138" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2183</a></span></extracted-citation>, does not foreclose us from recognizing that a certain, dispositive fact is always present in some categories of cases. In other words, acknowledging that destruction of evidence is at issue in every drunk-driving case does not undermine the general totality-of-the-circumstances approach that <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> and <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> endorsed. Cf. <em>ante</em> , at 2535, n. 3.</p>
<p id="p-72">* * *</p>
<p id="p-73">The Court has consistently held that police officers may perform searches without a warrant when destruction of evidence is a risk. <em>United States v. Banks</em> , <extracted-citation case-ids="8896811" index="139" url="https://cite.case.law/us/540/31/#p38"><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/" aria-description="Citation for case: United States v. Banks">540 U.S. 31</a></span></extracted-citation>, 38, <extracted-citation case-ids="8896811" index="140" url="https://cite.case.law/us/540/31/#p38"><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/" aria-description="Citation for case: United States v. Banks">124 S.Ct. 521</a></span></extracted-citation>, <extracted-citation case-ids="8896811" index="141" url="https://cite.case.law/us/540/31/#p38"><span class="citation" data-id="131146"><a href="/opinion/131146/united-states-v-banks/" aria-description="Citation for case: United States v. Banks">157 L.Ed.2d 343</a></span></extracted-citation> (2003) ; <em>Richards v. Wisconsin</em> , <extracted-citation case-ids="11652004" index="142" url="https://cite.case.law/us/520/385/#p395"><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">520 U.S. 385</a></span></extracted-citation>, 395, <extracted-citation case-ids="11652004" index="143" url="https://cite.case.law/us/520/385/#p395"><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">117 S.Ct. 1416</a></span></extracted-citation>, <extracted-citation case-ids="11652004" index="144" url="https://cite.case.law/us/520/385/#p395"><span class="citation" data-id="118103"><a href="/opinion/118103/richards-v-wisconsin/" aria-description="Citation for case: Richards v. Wisconsin">137 L.Ed.2d 615</a></span></extracted-citation> (1997) ; <em>Cupp v. Murphy</em> , <extracted-citation case-ids="6172131" index="145" url="https://cite.case.law/us/412/291/#p295"><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U.S. 291</a></span></extracted-citation>, 295-296, <extracted-citation case-ids="6172131" index="146" url="https://cite.case.law/us/412/291/#p295"><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">93 S.Ct. 2000</a></span></extracted-citation>, <extracted-citation case-ids="6172131" index="147" url="https://cite.case.law/us/412/291/#p295"><span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">36 L.Ed.2d 900</a></span></extracted-citation> (1973) ; <em>Schmerber v. California</em> , <extracted-citation case-ids="12047531" index="148" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span></extracted-citation>, 770-772, <extracted-citation case-ids="12047531" index="149" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="150" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">16 L.Ed.2d 908</a></span></extracted-citation> (1966). The rule should be no different in drunk-driving cases. Because the plurality instead adopts a rule more likely to confuse than clarify, I concur only in the judgment.</p>
<p id="p-74">Justice SOTOMAYOR, with whom Justice GINSBURG and Justice KAGAN join, dissenting.</p>
<p id="p-75">The plurality's decision rests on the false premise that today's holding is necessary to spare law enforcement from a choice between attending to emergency situations and securing evidence used to enforce state drunk-driving laws. Not so. To be sure, drunk driving poses significant dangers that Wisconsin and other States must be able to curb. But the question here is narrow: What must police do before ordering a blood draw of a person suspected of drunk driving who has become unconscious? Under the Fourth Amendment, the answer is clear: If there is time, get a warrant.</p>
<p id="p-76">The State of Wisconsin conceded in the state courts that it had time to get a warrant to draw Gerald Mitchell's blood, and that should be the end of the matter. Because the plurality needlessly casts aside the established protections of the warrant requirement in favor of a brand new presumption of exigent circumstances that Wisconsin does not urge, that the state courts did not consider, and that <a class="page-label" data-citation-index="1" data-label="2542" href="#p2542" id="p2542">*2542</a>contravenes this Court's precedent, I respectfully dissent.</p>
<p id="p-77">I</p>
<p id="p-78">In May 2013, Wisconsin police received a report that Gerald Mitchell, seemingly intoxicated, had driven away from his apartment building. A police officer later found Mitchell walking near a lake, slurring his speech and walking with difficulty. His van was parked nearby. The officer administered a preliminary breath test, which revealed a blood-alcohol concentration (BAC) of 0.24%. The officer arrested Mitchell for operating a vehicle while intoxicated.</p>
<p id="p-79">Once at the police station, the officer placed Mitchell in a holding cell, where Mitchell began to drift into either sleep or unconsciousness. At that point, the officer decided against administering a more definitive breath test and instead took Mitchell to the hospital for a blood test. Mitchell became fully unconscious on the way. At the hospital, the officer read Mitchell a notice, required by Wisconsin's so-called "implied consent" law, which gave him the opportunity to refuse BAC testing. See <extracted-citation index="151" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"><span class="citation no-link">Wis. Stat. § 343.305</span></extracted-citation> (2016). But Mitchell was too incapacitated to respond. The officer then asked the hospital to test Mitchell's blood. Mitchell's blood was drawn about 90 minutes after his arrest, and the test revealed a BAC of 0.22%<footnotemark>1</footnotemark> At no point did the officer attempt to secure a warrant.</p>
<p id="p-80">Mitchell was charged with violating two Wisconsin drunk-driving laws. See §§ 346.63(1)(a), (b). He moved to suppress the blood-test results, arguing that the warrantless blood draw was an unreasonable search under the Fourth Amendment. In response, Wisconsin conceded that exigent circumstances did not justify the warrantless blood draw. As the State's attorney told the trial court, "There is nothing to suggest that this is a blood draw on a[n] exigent circumstances situation when there has been a concern for exigency. This is not that case." App. 134. Instead, Wisconsin argued that the warrantless blood draw was lawful because of Wisconsin's implied-consent statute. <em><extracted-citation index="152" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">Id.,</extracted-citation></em><extracted-citation index="152" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 133</extracted-citation>.</p>
<p id="p-81">The trial court denied Mitchell's motion to suppress, and a jury convicted him of the charged offenses. On appeal, the State Court of Appeals noted that Wisconsin had "expressly disclaimed that it was relying on exigent circumstances to justify the draw," <em><extracted-citation index="153" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">id.,</extracted-citation></em><extracted-citation index="153" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 64</extracted-citation>, and that this case offered a chance to clarify the law on implied consent because the case "is not susceptible to resolution on the ground of exigent circumstances," <em><extracted-citation index="154" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">id.,</extracted-citation></em><extracted-citation index="154" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 66</extracted-citation>. The Court of Appeals then certified the appeal to the Wisconsin Supreme Court, identifying the sole issue on appeal as "whether the warrantless blood draw of an unconscious motorist pursuant to Wisconsin's implied consent law, where no exigent circumstances exist or have been argued, violates the Fourth Amendment." <em><extracted-citation index="155" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305">Id.,</extracted-citation></em><extracted-citation index="155" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"> at 61</extracted-citation>.</p>
<p id="p-82">On certification from the state appellate court, the Supreme Court of Wisconsin upheld the search.<footnotemark>2</footnotemark> The Court granted certiorari to decide whether a statute like Wisconsin's, which allows police to draw <a class="page-label" data-citation-index="1" data-label="2543" href="#p2543" id="p2543">*2543</a>blood from an unconscious drunk-driving suspect, provides an exception to the Fourth Amendment's warrant requirement.</p>
<p id="p-83">II</p>
<p id="p-84">The Fourth Amendment guarantees "[t]he right of the people to be secure in their persons ... against unreasonable searches and seizures." When the aim of a search is to uncover evidence of a crime, the Fourth Amendment generally requires police to obtain a warrant. <em>Vernonia School Dist. 47J v. Acton</em> , <extracted-citation case-ids="1564392" index="156" url="https://cite.case.law/us/515/646/#p653"><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">515 U.S. 646</a></span></extracted-citation>, 653, <extracted-citation case-ids="1564392" index="157" url="https://cite.case.law/us/515/646/#p653"><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">115 S.Ct. 2386</a></span></extracted-citation>, <extracted-citation case-ids="1564392" index="158" url="https://cite.case.law/us/515/646/#p653"><span class="citation" data-id="9433198"><a href="/opinion/117964/vernonia-school-district-47j-v-acton/" aria-description="Citation for case: Vernonia School District 47J v. Acton">132 L.Ed.2d 564</a></span></extracted-citation> (1995).</p>
<p id="p-85">The warrant requirement is not a mere formality; it ensures that necessary judgment calls are made " 'by a neutral and detached magistrate,' " not " 'by the officer engaged in the often competitive enterprise of ferreting out crime.' " <em>Schmerber v. California</em> , <extracted-citation case-ids="12047531" index="159" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S. 757</a></span></extracted-citation>, 770, <extracted-citation case-ids="12047531" index="160" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="161" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">16 L.Ed.2d 908</a></span></extracted-citation> (1966). A warrant thus serves as a check against searches that violate the Fourth Amendment by ensuring that a police officer is not made the sole interpreter of the Constitution's protections. Accordingly, a search conducted without a warrant is "<em>per se</em> unreasonable under the Fourth Amendment-subject only to a few specifically established and well-delineated exceptions." <em>Katz v. United States</em> , <extracted-citation case-ids="11339173" index="162" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">389 U.S. 347</a></span></extracted-citation>, 357, <extracted-citation case-ids="11339173" index="163" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">88 S.Ct. 507</a></span></extracted-citation>, <extracted-citation case-ids="11339173" index="164" url="https://cite.case.law/us/389/347/#p357"><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">19 L.Ed.2d 576</a></span></extracted-citation> (1967) (footnote omitted); see <em>Riley v. California</em> , <extracted-citation index="165" url="https://cite.case.law/citations/?q=573%20U.S.%20373"><span class="citation no-link">573 U.S. 373</span></extracted-citation>, 382, <extracted-citation case-ids="12581677" index="166" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="167" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014) ("In the absence of a warrant, a search is reasonable only if it falls within a specific exception to the warrant requirement").</p>
<p id="p-86">The carefully circumscribed exceptions to the warrant requirement, as relevant here, include the exigent-circumstances exception, which applies when " 'the exigencies of the situation' make the needs of law enforcement so compelling that [a] warrantless search is objectively reasonable," <em>Kentucky v. King</em> , <extracted-citation case-ids="5911971,12458997" index="168" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">563 U.S. 452</a></span></extracted-citation>, 460, <extracted-citation case-ids="5911971,12458997" index="169" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">131 S.Ct. 1849</a></span></extracted-citation>, <extracted-citation case-ids="5911971,12458997" index="170" url="https://cite.case.law/us/563/452/"><span class="citation" data-id="9441559"><a href="/opinion/216733/kentucky-v-king/" aria-description="Citation for case: Kentucky v. King">179 L.Ed.2d 865</a></span></extracted-citation> (2011) (some internal quotation marks omitted); the consent exception for cases where voluntary consent is given to the search, see, <em>e.g.,</em> <em>Georgia v. Randolph</em> , <extracted-citation case-ids="3275967" index="171" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">547 U.S. 103</a></span></extracted-citation>, 109, <extracted-citation case-ids="3275967" index="172" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="173" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">164 L.Ed.2d 208</a></span></extracted-citation> (2006) ; and the exception for "searches incident to arrest," see, <em>e.g.,</em> <em>Riley</em> , <extracted-citation index="174" url="https://cite.case.law/citations/?q=573%20U.S.%20373">573 U.S., at 382</extracted-citation>, <extracted-citation case-ids="12581677" index="175" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>.</p>
<p id="p-87">A</p>
<p id="p-88">Blood draws are "searches" under the Fourth Amendment. The act of drawing a person's blood, whether or not he is unconscious, "involve[s] a compelled physical intrusion beneath [the] skin and into [a person's] veins," all for the purpose of extracting evidence for a criminal investigation. <em>Missouri v. McNeely</em> , <extracted-citation case-ids="12697040" index="176" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S. 141</a></span></extracted-citation>, 148, <extracted-citation case-ids="12697040" index="177" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="178" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">185 L.Ed.2d 696</a></span></extracted-citation> (2013). The blood draw also "places in the hands of law enforcement authorities a sample that can be preserved and from which it is possible to extract information beyond a simple BAC reading," <em>Birchfield</em> v. <em>North Dakota</em> , 579 U.S. ----, ----, <extracted-citation case-ids="12597986" index="179" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct. 2160</a></span></extracted-citation>, 2178, <extracted-citation case-ids="12597986" index="180" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">195 L.Ed.2d 560</a></span></extracted-citation> (2016), such as whether a person is pregnant, is taking certain medications, or suffers from an illness. That "invasion of bodily integrity" disturbs "an individual's 'most personal and deep-rooted expectations of privacy.' " <em>McNeely</em> , <extracted-citation case-ids="12697040" index="181" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 148</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="182" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</p>
<p id="p-89">For decades, this Court has stayed true to the Fourth Amendment's warrant requirement and the narrowness of its exceptions, even in the face of attempts categorically to exempt blood testing from its protections. In <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> , a man was hospitalized following a car accident. <extracted-citation case-ids="12047531" index="183" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U.S., at 758</a></span></extracted-citation>, <extracted-citation case-ids="12047531" index="184" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>. At the scene of the accident and later at the hospital, a police officer noticed signs of intoxication, and he arrested Schmerber for drunk driving.</p>
<p id="p-90"><a class="page-label" data-citation-index="1" data-label="2544" href="#p2544" id="p2544">*2544</a><em><extracted-citation case-ids="12047531" index="185" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="185" url="https://cite.case.law/us/384/757/#p765"> at 768-769</extracted-citation>, <extracted-citation case-ids="12047531" index="186" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>. Without obtaining a warrant, the officer ordered a blood draw to measure Schmerber's BAC, and Schmerber later challenged the blood test as an unreasonable search under the Fourth Amendment. <em><extracted-citation case-ids="12047531" index="187" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="187" url="https://cite.case.law/us/384/757/#p765"> at 758-759</extracted-citation>, <extracted-citation case-ids="12047531" index="188" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>. The Court reinforced that search warrants are "ordinarily required ... where intrusions into the human body are concerned," <em><extracted-citation case-ids="12047531" index="189" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="189" url="https://cite.case.law/us/384/757/#p765"> at 770</extracted-citation>, <extracted-citation case-ids="12047531" index="190" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>, but it ultimately held that exigent circumstances justified the particular search at issue because certain "special facts"-namely, an unusual delay caused by the investigation at the scene and the subsequent hospital trip-left the police with "no time to seek out a magistrate and secure a warrant" before losing the evidence. <em><extracted-citation case-ids="12047531" index="191" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12047531" index="191" url="https://cite.case.law/us/384/757/#p765"> at 770-771</extracted-citation>, <extracted-citation case-ids="12047531" index="192" url="https://cite.case.law/us/384/757/#p765"><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">86 S.Ct. 1826</a></span></extracted-citation>.</p>
<p id="p-91">More recently, in <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> , the Court held that blood tests are not categorically exempt from the warrant requirement, explaining that exigency "must be determined case by case based on the totality of the circumstances." <extracted-citation case-ids="12697040" index="193" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 156</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="194" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>. "[T]he natural dissipation of alcohol in the blood may support a finding of exigency in a specific case," but "it does not do so categorically." <em>Ibid</em> . If officers "can reasonably obtain a warrant before a blood sample can be drawn without significantly undermining the efficacy of the search," the Court made clear, "the Fourth Amendment mandates that they do so." <em><extracted-citation case-ids="12697040" index="195" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="195" url="https://cite.case.law/us/569/141/#p149"> at 152</extracted-citation>, <extracted-citation case-ids="12697040" index="196" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> ; see <em><extracted-citation case-ids="12697040" index="197" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">id.,</a></span></extracted-citation></em><extracted-citation case-ids="12697040" index="197" url="https://cite.case.law/us/569/141/#p149"> at 167</extracted-citation>, <extracted-citation case-ids="12697040" index="198" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation> (ROBERTS, C.J., concurring in part and dissenting in part) ("The natural dissipation of alcohol in the bloodstream ... would qualify as an exigent circumstance, except that there may be time to secure a warrant before blood can be drawn. If there is, an officer must seek a warrant").</p>
<p id="p-92">In <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , the Court rejected another attempt categorically to exempt blood draws from the warrant requirement. 579 U.S., at ----, <extracted-citation case-ids="12597986" index="199" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span></extracted-citation>. The Court considered whether warrantless breath and blood tests to determine a person's BAC level were permissible as searches incident to arrest. The Court held that warrantless breath tests were permitted because they are insufficiently intrusive to outweigh the State's need for BAC testing. See <em><extracted-citation case-ids="12597986" index="200" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">ibid.</a></span></extracted-citation></em> As to blood tests, however, the Court held the opposite: Because they are significantly more intrusive than breath tests, the warrant requirement applies unless particular exigent circumstances prevent officers from obtaining a warrant. <em><extracted-citation case-ids="12597986" index="201" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Ibid.</a></span></extracted-citation></em> ; see <em><extracted-citation case-ids="12597986" index="202" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">id.</a></span></extracted-citation></em> , at ----, <extracted-citation case-ids="12597986" index="203" url="https://cite.case.law/s-ct/136/2160/"><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/#2184" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">136 S.Ct., at 2184</a></span></extracted-citation> ("Nothing prevents the police from seeking a warrant for a blood test when there is sufficient time to do so in the particular circumstances or from relying on the exigent circumstances exception ... when there is not").<footnotemark>3</footnotemark></p>
<p id="p-93">B</p>
<p id="p-94">Those cases resolve this one. <em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></em> and <em><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">McNeely</a></span></em> establish that there is no categorical exigency exception for blood draws, although exigent circumstances might justify a warrantless blood draw on the facts of a particular case. And from <em><span class="citation" data-id="3216391"><a href="/opinion/3216497/birchfield-v-n-dakota-william-robert-bernard/" aria-description="Citation for case: Birchfield v. N. Dakota. William Robert Bernard">Birchfield</a></span></em> , we know that warrantless blood draws cannot be justified as searches incident to arrest. The lesson is straightforward: Unless there is too little time to do so, police officers must get a warrant before <a class="page-label" data-citation-index="1" data-label="2545" href="#p2545" id="p2545">*2545</a>ordering a blood draw. See 579 U.S., at ----, <extracted-citation case-ids="12597986" index="204" url="https://cite.case.law/s-ct/136/2160/">136 S.Ct., at </extracted-citation>2184 ; <em>McNeely</em> , <extracted-citation case-ids="12697040" index="205" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">569 U.S., at 152</a></span></extracted-citation>, <extracted-citation case-ids="12697040" index="206" url="https://cite.case.law/us/569/141/#p149"><span class="citation" data-id="858288"><a href="/opinion/858288/missouri-v-mcneely/" aria-description="Citation for case: Missouri v. McNeely">133 S.Ct. 1552</a></span></extracted-citation>.</p>
<p id="p-95">Against this precedential backdrop, Wisconsin's primary argument has always been that Mitchell consented to the blood draw through the State's "implied-consent law." Under that statute, a motorist who drives on the State's roads is "deemed" to have consented to a blood draw, breath test, and urine test, and that supposed consent allows a warrantless blood draw from an unconscious motorist as long as the police have probable cause to believe that the motorist has violated one of the State's impaired driving statutes. See <extracted-citation index="207" url="https://cite.case.law/citations/?q=Wis.%20Stat.%20%C2%A7%C2%A7%20343.305"><span class="citation no-link">Wis. Stat. § 343.305</span></extracted-citation>.</p>
<p id="p-96">The plurality does not rely on the consent exception here. See <em>ante</em> , at 2532. With that sliver of the plurality's reasoning I agree. I would go further and hold that the state statute, however phrased, cannot itself create the actual and informed consent that the Fourth Amendment requires. See <em>Randolph</em> , <extracted-citation case-ids="3275967" index="208" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">547 U.S., at 109</a></span></extracted-citation>, <extracted-citation case-ids="3275967" index="209" url="https://cite.case.law/us/547/103/#p109"><span class="citation" data-id="9434962"><a href="/opinion/145669/georgia-v-randolph/" aria-description="Citation for case: Georgia v. Randolph">126 S.Ct. 1515</a></span></extracted-citation> (describing the "voluntary consent" exception to the warrant requirement as " 'jealously and carefully drawn' "); <em>Bumper v. North Carolina</em> , <extracted-citation case-ids="1767611" index="210" url="https://cite.case.law/us/391/543/#p548"><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">391 U.S. 543</a></span></extracted-citation>, 548, <extracted-citation case-ids="1767611" index="211" url="https://cite.case.law/us/391/543/#p548"><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">88 S.Ct. 1788</a></span></extracted-citation>, <extracted-citation case-ids="1767611" index="212" url="https://cite.case.law/us/391/543/#p548"><span class="citation" data-id="9423732"><a href="/opinion/107716/bumper-v-north-carolina/" aria-description="Citation for case: Bumper v. North Carolina">20 L.Ed.2d 797</a></span></extracted-citation> (1968) (stating that consent must be "freely and voluntarily given"); see also <em>Schneckloth v. Bustamonte</em> , <extracted-citation case-ids="6172008" index="213" url="https://cite.case.law/us/412/218/#p226"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U.S. 218</a></span></extracted-citation>, 226-227, <extracted-citation case-ids="6172008" index="214" url="https://cite.case.law/us/412/218/#p226"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">93 S.Ct. 2041</a></span></extracted-citation>, <extracted-citation case-ids="6172008" index="215" url="https://cite.case.law/us/412/218/#p226"><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">36 L.Ed.2d 854</a></span></extracted-citation> (1973) (explaining that the existence of consent must "be determined from the totality of all the circumstances"). That should be the end of this case.</p>
<p id="p-97">III</p>
<p id="p-98">Rather than simply applying this Court's precedents to address-and reject-Wisconsin's implied-consent theory, the plurality today takes the extraordinary step of relying on an issue, exigency, that Wisconsin has affirmatively waived.<footnotemark>4</footnotemark> Wisconsin has not once, in any of its briefing before this Court or the state courts, argued that exigent circumstances were present here. In fact, in the state proceedings, Wisconsin "conceded" that the exigency exception does not justify the warrantless blood draw in this case. App. 66; see <extracted-citation case-ids="12556993" index="216" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">2018 WI 84</a></span></extracted-citation>, ¶12, <extracted-citation case-ids="12556993" index="217" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">383 Wis.2d 192</a></span></extracted-citation>, 202, <extracted-citation case-ids="12556993" index="218" url="https://cite.case.law/nw2d/914/151/"><span class="citation" data-id="9886762"><a href="/opinion/4513691/state-v-gerald-p-mitchell/" aria-description="Citation for case: State v. Gerald P. Mitchell">914 N.W.2d 151</a></span></extracted-citation>, 155 ("The State expressly stated that it was not relying on exigent circumstances to justify the blood draw"). Accordingly, the state courts proceeded on the acknowledgment that no exigency is at issue here. As the Wisconsin Court of Appeals put it:</p>
<blockquote id="p-99">"In particular, this case is not susceptible to resolution on the ground of exigent circumstances. No testimony was received that would support the conclusion that exigent circumstances justified the warrantless blood draw. [The officer] expressed agnosticism as to how long it would have taken to obtain a warrant, and he never once testified (or even implied) that there was no time to get a warrant." App. 66.</blockquote>
<p id="p-100">The exigency issue is therefore waived-that is, knowingly and intentionally abandoned, <a class="page-label" data-citation-index="1" data-label="2546" href="#p2546" id="p2546">*2546</a>see <em>Wood v. Milyard</em> , <extracted-citation case-ids="12189545" index="219" url="https://cite.case.law/us/566/463/#p474"><span class="citation" data-id="9499833"><a href="/opinion/798510/wood-v-milyard/" aria-description="Citation for case: Wood v. Milyard">566 U.S. 463</a></span></extracted-citation>, 474, <extracted-citation case-ids="12189545" index="220" url="https://cite.case.law/us/566/463/#p474"><span class="citation" data-id="9499833"><a href="/opinion/798510/wood-v-milyard/" aria-description="Citation for case: Wood v. Milyard">132 S.Ct. 1826</a></span></extracted-citation>, <extracted-citation case-ids="12189545" index="221" url="https://cite.case.law/us/566/463/#p474"><span class="citation" data-id="9499833"><a href="/opinion/798510/wood-v-milyard/" aria-description="Citation for case: Wood v. Milyard">182 L.Ed.2d 733</a></span></extracted-citation> (2012) -and the Court should not have considered it. See, <em>e.g.,</em> <em>Heckler v. Campbell</em> , <extracted-citation case-ids="11298743" index="222" url="https://cite.

[...TRUNCATED 77939 of 197939 chars for pack size; the Codex lane saw the full text — flag any check that needs the tail...]
```

---
