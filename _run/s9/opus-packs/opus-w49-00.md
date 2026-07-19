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

## GROUP: content/cases/Pennsylvania v. Muniz.md  (`case`, 5 assertions)

### content_page

```
---
title: "Pennsylvania v. Muniz"
type: case
citation: "496 U.S. 582 (1990)"
parallel_cite: "110 S. Ct. 2638; 110 L. Ed. 2d 528"
neutral_cite: 1990 U.S. LEXIS 3211
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1990
date_decided: 1990-06-18
docket: 89-213
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1990-06-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Pennsylvania v. Muniz
  varies_by_point: false
  scope_note: "Good law (fractured opinion). The slurred manner of speech is non-testimonial; the 'sixth birthday' answer was testimonial and required suppression (custodial, unwarned); the routine biographical booking questions fall within a 'routine booking question' exception to Miranda."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112464/pennsylvania-v-muniz/"
  cluster_id: 112464
  opinion_id: 112464
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[Rhode Island v. Innis]]", "[[Schmerber v. California]]", "[[Illinois v. Perkins]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "testimonial", "booking-exception", "dui", "self-incrimination"]
holding: "The slurred manner of a DUI suspect's speech is non-testimonial physical evidence admissible without Miranda; but a question whose answer's content reveals the suspect's impaired mental state (the 'sixth birthday' question) elicits a testimonial response that must be suppressed if unwarned; routine biographical booking questions fall within a 'routine booking question' exception to Miranda interrogation."
lake:
  record_id: Pennsylvania v. Muniz
  status: verified
  projected_at: 2026-07-09
---

# Pennsylvania v. Muniz

*496 U.S. 582 (1990)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Muniz was arrested for driving under the influence and taken to a booking center, where the proceedings were videotaped. Without [[Miranda and Custodial Interrogation|Miranda warnings]], an officer asked him seven biographical questions — name, address, height, weight, eye color, date of birth, and current age — during which he stumbled over his address and age. The officer then asked, "Do you know what the date was of your sixth birthday?" and Muniz answered that he did not. His slurred speech and confused answers were used as evidence of intoxication. The Pennsylvania Superior Court held that the sixth-birthday answer (and other statements) should have been suppressed for lack of [[Miranda and Custodial Interrogation|Miranda warnings]].

## Issue
Whether, for a custodial DUI suspect questioned without [[Miranda and Custodial Interrogation|Miranda warnings]], (1) the slurred manner of his speech, (2) his answer to the "sixth birthday" question, and (3) his answers to routine biographical booking questions were testimonial and required suppression.

## Rule
**Slurring is non-testimonial.** "[A]ny slurring of speech and other evidence of lack of muscular coordination revealed by Muniz's responses . . . constitute nontestimonial components of those responses. Requiring a suspect to reveal the physical manner in which he articulates words . . . does not, without more, compel him to provide a 'testimonial' response for purposes of the privilege." — 496 U.S. at 590–591. ^pin-591

**The "sixth birthday" answer is testimonial.** Its content forced the trilemma of truth, falsity, or silence: "the incriminating inference of impaired mental faculties stemmed, not just from the fact that Muniz slurred his response, but also from a testimonial aspect of that response." — [*Id.* at 599](https://www.courtlistener.com/opinion/112464/pennsylvania-v-muniz/#:~:text=your-,sixth%20birthday). "[B]ecause we conclude that Muniz's response to the sixth birthday question was testimonial, the response should have been suppressed." — *Id.* at 600. ^pin-599

**Routine booking questions are exempt.** Muniz's "answers to th[e] first seven questions are . . . admissible because the questions fall within a 'routine booking question' exception which exempts from *Miranda*'s coverage questions to secure the 'biographical data necessary to complete booking or pretrial services.'" — *Id.* at 601. ^pin-601

## Application
The Commonwealth could use the slurred, uncoordinated manner of Muniz's speech as physical evidence of intoxication without [[Miranda and Custodial Interrogation|Miranda warnings]]. But the answer to the sixth-birthday question was different: its very content (that he could not supply the date) let the factfinder infer a confused mental state, so it was a testimonial communication that, taken in custody without warnings, had to be suppressed. The seven preceding biographical questions, though they produced incriminating fumbling, were asked to record routine booking data and so fell within the booking-question exception and were admissible.

## Conclusion
The slurring evidence and the biographical booking answers were admissible; the testimonial sixth-birthday answer should have been suppressed. The judgment of the Pennsylvania Superior Court was affirmed in part and reversed in part, and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (fractured opinion; the controlling holdings are stated above).
- No negative treatment. *Muniz* applies the testimonial/physical-evidence distinction of [[Schmerber v. California]] to custodial DUI questioning, defines interrogation through [[Rhode Island v. Innis]], and recognizes the routine-booking-question exception within the [[Miranda v. Arizona]] framework (decided the same Term as the [[Illinois v. Perkins]] undercover-questioning exception).

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Pennsylvania v. Muniz*, 496 U.S. 582 (1990) — https://www.courtlistener.com/opinion/112464/pennsylvania-v-muniz/ — pinpoints: 590–591, 599, 600, 601.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e3f8de97e5c06793", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "496 U.S. 582 (1990)", "court": "U.S. Supreme Court", "neutral_cite": "1990 U.S. LEXIS 3211", "official_citation_present": true, "parallel_cite": "110 S. Ct. 2638; 110 L. Ed. 2d 528", "title": "Pennsylvania v. Muniz", "year": "1990"}}
{"assertion_id": "714daf4e8490020a", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The slurred manner of a DUI suspect's speech is non-testimonial physical evidence admissible without Miranda; but a question whose answer's content reveals the suspect's impaired mental state (the 'sixth birthday' question) elicits a testimonial response that must be suppressed if unwarned; routine biographical booking questions fall within a 'routine booking question' exception to Miranda interrogation.", "title": "Pennsylvania v. Muniz"}}
{"assertion_id": "b05725dba4c96cb7", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Pennsylvania v. Muniz"}}
{"assertion_id": "55c5e90187711797", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Pennsylvania v. Muniz"}}
{"assertion_id": "f7ccd5de64465867", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1990-06-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Pennsylvania v. Muniz", "field_i_validity": "good_law", "scope_note": "Good law (fractured opinion). The slurred manner of speech is non-testimonial; the 'sixth birthday' answer was testimonial and required suppression (custodial, unwarned); the routine biographical booking questions fall within a 'routine booking question' exception to Miranda.", "title": "Pennsylvania v. Muniz", "varies_by_point": "false"}}
```

### lake record — Pennsylvania v. Muniz

```json
{
  "schema_version": "s2.v1",
  "record_id": "Pennsylvania v. Muniz",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Pennsylvania v. Muniz",
    "case_name_short": "Muniz",
    "case_name_full": "Pennsylvania v. Muniz",
    "input_case_name": "Pennsylvania v. Muniz",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1990-06-18",
    "year": 1990,
    "docket": "89-213",
    "cluster_id": 112464,
    "lead_opinion_id": 112464,
    "sibling_ids": [
      112464,
      9432075,
      9432076,
      9432077
    ],
    "absolute_url": "/opinion/112464/pennsylvania-v-muniz/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9093487,
        "score": 20,
        "case_name": "Pennsylvania v. Muniz"
      },
      {
        "cluster_id": 9093486,
        "score": 20,
        "case_name": "Pennsylvania v. Muniz"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "496 U.S. 582",
      "volume": "496",
      "reporter": "U.S.",
      "page": "582",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "110 S. Ct. 2638",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2638",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 528",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1990 U.S. LEXIS 3211",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3211",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "496 U.S. 582",
        "volume": "496",
        "reporter": "U.S.",
        "page": "582",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 S. Ct. 2638",
        "volume": "110",
        "reporter": "S. Ct.",
        "page": "2638",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "110 L. Ed. 2d 528",
        "volume": "110",
        "reporter": "L. Ed. 2d",
        "page": "528",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1990 U.S. LEXIS 3211",
        "volume": "1990",
        "reporter": "U.S. LEXIS",
        "page": "3211",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "496 U.S. 582",
    "official_selection": {
      "court_class": "scotus",
      "selected": "496 U.S. 582",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-591",
      "page": null,
      "quote": "question, and (3) his answers to routine biographical booking questions were testimonial and required suppression. ## Rule **Slurring is non-testimonial.**",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-599",
      "page": null,
      "quote": "sixth birthday",
      "star_marker": "586",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 3073,
      "fragment": "#:~:text=your-,sixth%20birthday",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-601",
      "page": null,
      "quote": "answers to th[e] first seven questions are . . . admissible because the questions fall within a 'routine booking question' exception which exempts from *Miranda*'s coverage questions to secure the 'biographical data necessary to complete booking or pretrial services.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1990-06-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Pennsylvania v. Muniz",
    "varies_by_point": false,
    "scope_note": "Good law (fractured opinion). The slurred manner of speech is non-testimonial; the 'sixth birthday' answer was testimonial and required suppression (custodial, unwarned); the routine biographical booking questions fall within a 'routine booking question' exception to Miranda.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Janvier",
          "cluster_id": 9494606,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
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
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "James Toler v. United States",
          "cluster_id": 4575476,
          "cite": [
            "198 A.3d 767"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Kirby. v. State",
          "cluster_id": 10366681,
          "cite": [
            "304 Ga. 472"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Brigido Zapien",
          "cluster_id": 4405817,
          "cite": [
            "861 F.3d 971",
            "2017 WL 2836162",
            "2017 U.S. App. LEXIS 11809"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Alfonzo Williams",
          "cluster_id": 4327223,
          "cite": [
            "842 F.3d 1143",
            "2016 U.S. App. LEXIS 21621",
            "2016 WL 7046754"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Boyd",
          "cluster_id": 4259208,
          "cite": [
            "360 Or. 302",
            "380 P.3d 941",
            "2016 Ore. LEXIS 612"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Tisa Farrow",
          "cluster_id": 3184707,
          "cite": [
            "2016 VT 30",
            "201 Vt. 437",
            "144 A.3d 1036",
            "2016 Vt. LEXIS 33",
            "2016 WL 932894"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chandler",
          "cluster_id": 7318545,
          "cite": [
            "164 F. Supp. 3d 368",
            "2016 U.S. Dist. LEXIS 17682",
            "2016 WL 614679"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cruz, Adelfo Ramirez",
          "cluster_id": 2950538,
          "cite": [
            "461 S.W.3d 531",
            "2015 Tex. Crim. App. LEXIS 561",
            "2015 WL 2236982"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Zaitar",
          "cluster_id": 2662455,
          "cite": [
            "858 F. Supp. 2d 103",
            "2012 WL 1570865",
            "2012 U.S. Dist. LEXIS 63313"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane1_negative"
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
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hiibel v. Sixth Judicial Dist. Court of Nev., Humboldt Cty.",
          "cluster_id": 136990,
          "cite": [
            "159 L. Ed. 2d 292",
            "124 S. Ct. 2451",
            "542 U.S. 177",
            "2004 U.S. LEXIS 4385",
            "17 Fla. L. Weekly Fed. S 406",
            "72 U.S.L.W. 4509"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Walton",
          "cluster_id": 2355344,
          "cite": [
            "41 S.W.3d 75",
            "2001 Tenn. LEXIS 222"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania v. Labron",
          "cluster_id": 118063,
          "cite": [
            "135 L. Ed. 2d 1031",
            "116 S. Ct. 2485",
            "518 U.S. 938",
            "1996 U.S. LEXIS 4268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evans v. State",
          "cluster_id": 1707183,
          "cite": [
            "725 So. 2d 613",
            "1997 WL 562044"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Morales",
          "cluster_id": 2629809,
          "cite": [
            "18 P.3d 11",
            "104 Cal. Rptr. 2d 582",
            "25 Cal. 4th 34",
            "2001 Daily Journal DAR 2253",
            "2001 Cal. Daily Op. Serv. 1805",
            "2001 Cal. LEXIS 1163"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Hubbell",
          "cluster_id": 1087666,
          "cite": [
            "147 L. Ed. 2d 24",
            "120 S. Ct. 2037",
            "530 U.S. 27",
            "2000 U.S. LEXIS 3768"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pirtle v. Morgan",
          "cluster_id": 7109731,
          "cite": [
            "313 F.3d 1160",
            "2002 WL 31840626"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Golphin",
          "cluster_id": 1274200,
          "cite": [
            "533 S.E.2d 168",
            "352 N.C. 364",
            "2000 N.C. LEXIS 618"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Robert Augustine D'anjou, A/K/A Dennis Dennison",
          "cluster_id": 663096,
          "cite": [
            "16 F.3d 604",
            "40 Fed. R. Serv. 515",
            "1994 U.S. App. LEXIS 2622",
            "1994 WL 46727"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
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
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florida v. Powell",
          "cluster_id": 1736,
          "cite": [
            "175 L. Ed. 2d 1009",
            "130 S. Ct. 1195",
            "559 U.S. 50",
            "2010 U.S. LEXIS 1898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnny Rivera, Elena Vila",
          "cluster_id": 568540,
          "cite": [
            "944 F.2d 1563",
            "1991 U.S. App. LEXIS 24889",
            "1991 WL 197347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nicholas v. Goord",
          "cluster_id": 8439101,
          "cite": [
            "430 F.3d 652",
            "2005 WL 3150611"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Pagan",
          "cluster_id": 2334891,
          "cite": [
            "950 A.2d 270",
            "597 Pa. 69",
            "2008 Pa. LEXIS 918"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Beshore",
          "cluster_id": 1979564,
          "cite": [
            "916 A.2d 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Balsys",
          "cluster_id": 118242,
          "cite": [
            "141 L. Ed. 2d 575",
            "118 S. Ct. 2218",
            "524 U.S. 666",
            "1998 U.S. LEXIS 4210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. JAVIER M.",
          "cluster_id": 2516018,
          "cite": [
            "33 P.3d 1",
            "131 N.M. 1",
            "2001 NMSC 030"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Bormann",
          "cluster_id": 2234021,
          "cite": [
            "777 N.W.2d 829",
            "279 Neb. 320"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffith v. State",
          "cluster_id": 2335950,
          "cite": [
            "55 S.W.3d 598",
            "2001 Tex. Crim. App. LEXIS 70",
            "2001 WL 1090773"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ramon Velarde-Gomez",
          "cluster_id": 775389,
          "cite": [
            "269 F.3d 1023",
            "2001 Daily Journal DAR 11297",
            "2001 Cal. Daily Op. Serv. 9050",
            "2001 U.S. App. LEXIS 22714",
            "2001 WL 1262610"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Pennsylvania v. Muniz:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjUyOTcyODAwMDAwJnM9MjQzMjc3NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112464+OR+9432075+OR+9432076+OR+9432077%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTImcz03ODAyMTYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112464+OR+9432075+OR+9432076+OR+9432077%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077)",
        "reviewed": 30,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 30,
        "triage_read": 2,
        "triage_snippet_classified": 28
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112464 OR 9432075 OR 9432076 OR 9432077)",
    "indexed_citing_opinions": 634,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112464,
        "count": 520,
        "count_source": "search"
      },
      {
        "opinion_id": 9432075,
        "count": 123,
        "count_source": "search"
      },
      {
        "opinion_id": 9432076,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432077,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 976,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/pennsylvania-v-muniz.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg4MzU2NiZzPTk1MTYyMDAmdD1vJmQ9MjAyNi0wNy0wNSZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28112464+OR+9432075+OR+9432076+OR+9432077%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112464,
        "cited_id": 97290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 105363,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 105528,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 106864,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107038,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107486,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 107487,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 108650,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 108709,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 108710,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 109292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 111878,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 112120,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 112123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 112152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 375540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 403655,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 424921,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 424960,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 521998,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1533585,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1702883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1782123,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1931990,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 1996025,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 2102837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 2259488,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112464,
        "cited_id": 2592211,
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
    "date_created": "2026-07-05T17:00:21Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:00:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:00:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:05:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:00:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Pennsylvania v. Muniz

```
<div>
<center><b><span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/" aria-description="Citation for case: Pennsylvania v. Muniz">496 U.S. 582</a></span> (1990)</b></center>
<center><h1>PENNSYLVANIA<br>
v.<br>
MUNIZ</h1></center>
<center>No. 89-213.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 27, 1990</center>
<center>Decided June 18, 1990</center>
CERTIORARI TO THE SUPERIOR COURT OF PENNSYLVANIA
<p><span class="star-pagination">*584</span> <i>J. Michael Eakin</i> argued the cause and filed a brief for petitioner.</p>
<p><i>Richard F. Maffett, Jr.,</i> argued the cause and filed a brief for respondent.<sup>[*]</sup></p>
<p>JUSTICE BRENNAN delivered the opinion of the Court, except as to Part III-C.</p>
<p>We must decide in this case whether various incriminating utterances of a drunken-driving suspect, made while performing a series of sobriety tests, constitute testimonial responses to custodial interrogation for purposes of the Self-Incrimination Clause of the Fifth Amendment.</p>
<p></p>
<h2>
<span class="star-pagination">*585</span> I</h2>
<p>During the early morning hours of November 30, 1986, a patrol officer spotted respondent Inocencio Muniz and a passenger parked in a car on the shoulder of a highway. When the officer inquired whether Muniz needed assistance, Muniz replied that he had stopped the car so he could urinate. The officer smelled alcohol on Muniz's breath and observed that Muniz's eyes were glazed and bloodshot and his face was flushed. The officer then directed Muniz to remain parked until his condition improved, and Muniz gave assurances that he would do so. But as the officer returned to his vehicle, Muniz drove off. After the officer pursued Muniz down the highway and pulled him over, the officer asked Muniz to perform three standard field sobriety tests: a "horizontal gaze nystagmus" test, a "walk and turn" test, and a "one leg stand" test.<sup>[1]</sup> Muniz performed these tests poorly, and he informed the officer that he had failed the tests because he had been drinking.</p>
<p>The patrol officer arrested Muniz and transported him to the West Shore facility of the Cumberland Country Central Booking Center. Following its routine practice for receiving persons suspected of driving while intoxicated, the booking center videotaped the ensuing proceedings. Muniz was informed that his actions and voice were being recorded, but he <span class="star-pagination">*586</span> was not at this time (nor had he been previously) advised of his rights under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Officer Hosterman first asked Muniz his name, address, height, weight, eye color, date of birth, and current age. He responded to each of these questions, stumbling over his address and age. The officer then asked Muniz, "Do you know what the date was of your sixth birthday?" After Muniz offered an inaudible reply, the officer repeated, "When you turned six years old, do you remember what the date was?" Muniz responded, "No, I don't."</p>
<p>Officer Hosterman next requested Muniz to perform each of the three sobriety tests that Muniz had been asked to perform earlier during the initial roadside stop. The videotape reveals that his eyes jerked noticeably during the gaze test, that he did not walk a very straight line, and that he could not balance himself on one leg for more than several seconds. During the latter two tests, he did not complete the requested verbal counts from 1 to 9 and from 1 to 30. Moreover, while performing these tests, Muniz "attempted to explain his difficulties in performing the various tasks, and often requested further clarification of the tasks he was to perform." <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#390" aria-description="Citation for case: Commonwealth v. Muniz">377 Pa. Super. 382, 390</a></span>, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d 419, 423</a></span> (1988).</p>
<p>Finally, Officer Deyo asked Muniz to submit to a breathalyzer test designed to measure the alcohol content of his expelled breath. Officer Deyo read to Muniz the Common-wealth's Implied Consent Law, <span class="citation no-link">75 Pa. Cons. Stat. § 1547</span> (1987), and explained that under the law his refusal to take the test would result in automatic suspension of his driver's license for one year. Muniz asked a number of questions about the law, commenting in the process about his state of inebriation. Muniz ultimately refused to take the breath test. At this point, Muniz was for the first time advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Muniz then signed a statement waiving his rights and admitted in response to further questioning that he had been driving while intoxicated.</p>
<p><span class="star-pagination">*587</span> Both the video and audio portions of the videotape were admitted into evidence at Muniz's bench trial,<sup>[2]</sup> along with the arresting officer's testimony that Muniz failed the roadside sobriety tests and made incriminating remarks at that time. Muniz was convicted of driving under the influence of alcohol in violation of <span class="citation no-link">75 Pa. Cons. Stat. § 3731</span>(a)(1) (1987). Muniz filed a motion for a new trial, contending that the court should have excluded the testimony relating to the field sobriety tests and the videotape taken at the booking center "because they were incriminating and completed prior to [Muniz's] receiving his Miranda warnings." App. to Pet. for Cert. C-5  C-6. The trial court denied the motion, holding that " `requesting a driver, suspected of driving under the influence of alcohol, to perform physical tests or take a breath analysis does not violate [his] privilege against self-incrimination because [the] evidence procured is of a physical nature rather than testimonial, and therefore no Miranda warnings are required.' " <i><span class="citation no-link">Id.,</span></i> at C-6, quoting <i>Commonwealth</i> v. <i>Benson,</i> <span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/#29" aria-description="Citation for case: Commonwealth v. Benson">280 Pa. Super. 20, 29</a></span>, <span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/#387" aria-description="Citation for case: Commonwealth v. Benson">421 A. 2d 383, 387</a></span> (1980).</p>
<p>On appeal, the Superior Court of Pennsylvania reversed. The appellate court agreed that when Muniz was asked "to submit to a field sobriety test, and later perform these tests before the videotape camera, no <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were required" because such sobriety tests elicit physical, rather than testimonial, evidence within the meaning of the Fifth Amendment. 377 Pa. Super., at 387, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#422" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 422</a></span>. The court concluded, however, that "when the physical nature of the tests begins to yield testimonial and communicative statements . . . the protections afforded by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> are invoked." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> The court explained that Muniz's answer to the question regarding his sixth birthday and the statements and inquiries he made while performing the physical <span class="star-pagination">*588</span> dexterity tests and discussing the breathalyzer test "are precisely the sort of testimonial evidence that we expressly protected in [previous cases]," <i>id.,</i> at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>, because they " `reveal[ed] his thought processes.' " <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#389" aria-description="Citation for case: Commonwealth v. Muniz"><i>Id.,</i> at 389</a></span>, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>. The court further explained: "[N]one of Muniz's utterances were spontaneous, voluntary verbalizations. Rather, they were clearly compelled by the questions and instructions presented to him during his detention at the Booking Center. Since the . . . responses and communications were elicited before Muniz received his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, they should have been excluded as evidence." <i>Id.,</i> at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>.<sup>[3]</sup> Concluding that the audio portion of the videotape should have been suppressed in its entirety, the court reversed Muniz's conviction and remanded the case for a new trial.<sup>[4]</sup> After the Pennsylvania Supreme Court denied the Commonwealth's application for review, <span class="citation no-link">522 Pa. 575</span>, <span class="citation no-link">559 A. 2d 36</span> (1989), we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./493/916/">493 U. S. 916</a></span> (1989).</p>
<p></p>
<h2>II</h2>
<p>The Self-Incrimination Clause of the Fifth Amendment<sup>[5]</sup> provides that no "person . . . shall be compelled in any criminal case to be a witness against himself." Although the text does not delineate the ways in which a person might be made <span class="star-pagination">*589</span> a "witness against himself," cf. <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761-762, n. 6</a></span> (1966), we have long held that the privilege does not protect a suspect from being compelled by the State to produce "real or physical evidence." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#764" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 764</a></span>. Rather, the privilege "protects an accused only from being compelled to testify against himself, or otherwise provide the State with evidence of a testimonial or communicative nature." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 761</a></span>. "[I]n order to be testimonial, an accused's communication must itself, explicitly or implicitly, relate a factual assertion or disclose information. Only then is a person compelled to be a `witness' against himself." <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 210</a></span> (1988).</p>
<p>In <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), we reaffirmed our previous understanding that the privilege against self-incrimination protects individuals not only from legal compulsion to testify in a criminal courtroom but also from "informal compulsion exerted by law-enforcement officers during in-custody questioning." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 461</a></span>. Of course, voluntary statements offered to police officers "remain a proper element in law enforcement." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#478" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 478</a></span>. But "without proper safeguards the process of in-custody interrogation of persons suspected or accused of crime contains inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 467</a></span>. Accordingly, we held that protection of the privilege against self-incrimination during pretrial questioning requires application of special "procedural safeguards." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#444" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 444</a></span>. "Prior to any questioning, the person must be warned that he has a right to remain silent, that any statement he does make may be used as evidence against him, and that he has a right to the presence of an attorney, either retained or appointed." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> Unless a suspect "voluntarily, knowingly and intelligently" waives these rights, <i>ibid.,</i> any incriminating responses to questioning may not be introduced into evidence in the prosecution's case in chief in a subsequent criminal proceeding.</p>
<p><span class="star-pagination">*590</span> This case implicates both the "testimonial" and "compulsion" components of the privilege against self-incrimination in the context of pretrial questioning. Because Muniz was not advised of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights until after the videotaped proceedings at the booking center were completed, any verbal statements that were both testimonial in nature and elicited during custodial interrogation should have been suppressed. We focus first on Muniz's responses to the initial informational questions, then on his questions and utterances while performing the physical dexterity and balancing tests, and finally on his questions and utterances surrounding the breathalyzer test.</p>
<p></p>
<h2>III</h2>
<p>In the initial phase of the recorded proceedings, Officer Hosterman asked Muniz his name, address, height, weight, eye color, date of birth, current age, and the date of his sixth birthday. Both the delivery and content of Muniz's answers were incriminating. As the state court found, "Muniz's videotaped responses . . . certainly led the finder of fact to infer that his confusion and failure to speak clearly indicated a state of drunkenness that prohibited him from safely operating his vehicle." 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>. The Commonwealth argues, however, that admission of Muniz's answers to these questions does not contravene Fifth Amendment principles because Muniz's statement regarding his sixth birthday was not "testimonial" and his answers to the prior questions were not elicited by custodial interrogation. We consider these arguments in turn.</p>
<p></p>
<h2>A</h2>
<p>We agree with the Commonwealth's contention that Muniz's answers are not rendered inadmissible by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> merely because the slurred nature of his speech was incriminating. The physical inability to articulate words in a clear manner due to "the lack of muscular coordination of his tongue and mouth," Brief for Petitioner 16, is not itself a testimonial <span class="star-pagination">*591</span> component of Muniz's responses to Officer Hosterman's introductory questions. In <i>Schmerber</i> v. <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">California, supra</a></span></i><i>,</i> we drew a distinction between "testimonial" and "real or physical evidence" for purposes of the privilege against self-incrimination. We noted that in <i>Holt</i> v. <i>United States,</i> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States">218 U. S. 245, 252-253</a></span> (1910), Justice Holmes had written for the Court that " `[t]he prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material.' " 384 U. S., at 763. We also acknowledged that "both federal and state courts have usually held that it offers no protection against compulsion to submit to fingerprinting, photographing, or measurements, to write or speak for identification, to appear in court, to stand, to assume a stance, to walk, or to make a particular gesture." <i>Id.,</i> at 764. Embracing this view of the privilege's contours, we held that "the privilege is a bar against compelling `communications' or `testimony,' but that compulsion which makes a suspect or accused the source of `real or physical evidence' does not violate it." <i>Ibid.</i> Using this "helpful framework for analysis," <i>ibid.,</i> we held that a person suspected of driving while intoxicated could be forced to provide a blood sample, because that sample was "real or physical evidence" outside the scope of the privilege and the sample was obtained in a manner by which "[p]etitioner's testimonial capacities were in no way implicated." <i>Id.,</i> at 765.</p>
<p>We have since applied the distinction between "real or physical" and "testimonial" evidence in other contexts where the evidence could be produced only through some volitional act on the part of the suspect. In <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U. S. 218</a></span> (1967), we held that a suspect could be compelled to participate in a lineup and to repeat a phrase provided by the police so that witnesses could view him and listen to his voice. We explained that requiring his presence and speech at a lineup reflected "compulsion of the accused to <span class="star-pagination">*592</span> exhibit his physical characteristics, not compulsion to disclose any knowledge he might have." <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade"><i>Id.,</i> at 222</a></span>; see <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade"><i>id.,</i> at 222-223</a></span> (suspect was "required to use his voice as an identifying physical characteristic"). In <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), we held that a suspect could be compelled to provide a handwriting exemplar, explaining that such an exemplar, "in contrast to the content of what is written, like the voice or body itself, is an identifying physical characteristic outside [the privilege's] protection." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 266-267</a></span>. And in <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1</a></span> (1973), we held that suspects could be compelled to read a transcript in order to provide a voice exemplar, explaining that the "voice recordings were to be used solely to measure the physical properties of the witnesses' voices, not for the testimonial or communicative content of what was to be said." <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio"><i>Id.,</i> at 7</a></span>.</p>
<p>Under <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> and its progeny, we agree with the Commonwealth that any slurring of speech and other evidence of lack of muscular coordination revealed by Muniz's responses to Officer Hosterman's direct questions constitute nontestimonial components of those responses. Requiring a suspect to reveal the physical manner in which he articulates words, like requiring him to reveal the physical properties of the sound produced by his voice, see <i><span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/" aria-description="Citation for case: United States v. Dionisio">Dionisio, supra,</a></span></i> does not, without more, compel him to provide a "testimonial" response for purposes of the privilege.</p>
<p></p>
<h2>B</h2>
<p>This does not end our inquiry, for Muniz's answer to the sixth birthday question was incriminating, not just because of his delivery, but also because of his answer's <i>content;</i> the trier of fact could infer from Muniz's answer (that he did not <i>know</i> the proper date) that his mental state was confused.<sup>[6]</sup><span class="star-pagination">*593</span> The Commonwealth and the United States as <i>amicus curiae</i> argue that this incriminating inference does not trigger the protections of the Fifth Amendment privilege because the inference concerns "the physiological functioning of [Muniz's] brain," Brief for Petitioner 21, which is asserted to be every bit as "real or physical" as the physiological makeup of his blood and the timbre of his voice.</p>
<p>But this characterization addresses the wrong question; that the "fact" to be inferred might be said to concern the physical status of Muniz's brain merely describes the way in which the inference is incriminating. The correct question for present purposes is whether the incriminating inference of mental confusion is drawn from a testimonial act or from physical evidence. In <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span>,</i> for example, we held that the police could compel a suspect to provide a blood sample in order to determine the physical makeup of his blood and thereby draw an inference about whether he was intoxicated. This compulsion was outside of the Fifth Amendment's protection, not simply because the evidence concerned the suspect's physical body, but rather because the evidence was <i>obtained</i> in a manner that did not entail any testimonial act on the part of the suspect: "Not even a shadow of testimonial compulsion upon or enforced communication by the accused was involved either in the extraction or in the chemical analysis." 384 U. S., at 765. In contrast, had the police instead asked the suspect directly whether his blood contained a high concentration of alcohol, his affirmative response would have been testimonial even though it would have been used to draw the same inference concerning his physiology. See <i>ibid.</i> ("[T]he blood test evidence . . . was neither [the suspect's] testimony nor evidence relating to some communicative act"). In this case, the question is not whether a suspect's "impaired mental faculties" can fairly be characterized as an aspect of his physiology, but rather whether Muniz's response <span class="star-pagination">*594</span> to the sixth birthday question that gave rise to the inference of such an impairment was testimonial in nature.<sup>[7]</sup></p>
<p>We recently explained in <i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">487 U. S. 201</a></span> (1988), that "in order to be testimonial, an accused's communication must itself, explicitly or implicitly, relate a factual assertion or disclose information." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 210</a></span>. We reached this conclusion after addressing our reasoning in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber, supra,</a></span></i> and its progeny:</p>
<blockquote>"The Court accordingly held that the privilege was not implicated in [the line of cases beginning with <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i>], because the suspect was not required `to disclose any knowledge he might have,' or `to speak his guilt.' <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade">388 U. S., at 222-223</a></span>. See <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio">410 U. S., at 7</a></span>; <i>Gilbert,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S., at 266-267</a></span>. It is the `extortion of information from the accused,' <i>Couch</i> v. <i>United States,</i> 409 U. S., at 328, the attempt to force him `to disclose the contents of his own mind,' <i>Curcio</i> v. <i>United States,</i> <span class="citation" data-id="105528"><a href="/opinion/105528/curcio-v-united-states/#128" aria-description="Citation for case: Curcio v. United States">354 U. S. 118, 128</a></span> (1957), that implicates the Self-Incrimination Clause. . . . `Unless some attempt is made to secure a communication  written, oral or otherwise  upon which reliance is to be placed as involving [the accused's] consciousness of the facts and the operations of his mind in expressing it, the demand made upon <span class="star-pagination">*595</span> him is not a testimonial one.' 8 Wigmore § 2265, p. 386." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States">487 U. S., at 210-211</a></span>.</blockquote>
<p>After canvassing the purposes of the privilege recognized in prior cases,<sup>[8]</sup> we concluded that "[t]hese policies are served when the privilege is asserted to spare the accused from having to reveal, directly or indirectly, his knowledge of facts relating him to the offense or from having to share his thoughts and beliefs with the Government."<sup>[9]</sup><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 213</a></span>.</p>
<p>This definition of testimonial evidence reflects an awareness of the historical abuses against which the privilege against self-incrimination was aimed. "Historically, the privilege was intended to prevent the use of legal compulsion to extract from the accused a sworn communication of facts which would incriminate him. Such was the process of the <span class="star-pagination">*596</span> ecclesiastical courts and the Star Chamber  the inquisitorial method of putting the accused upon his oath and compelling him to answer questions designed to uncover uncharged offenses, without evidence from another source. The major thrust of the policies undergirding the privilege is to prevent such compulsion." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#212" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 212</a></span> (citations omitted); see also <i>Andresen</i> v. <i>Maryland,</i> <span class="citation" data-id="9426530"><a href="/opinion/109522/andresen-v-maryland/#470" aria-description="Citation for case: Andresen v. Maryland">427 U. S. 463, 470-471</a></span> (1976). At its core, the privilege reflects our fierce " `unwillingness to subject those suspected of crime to the cruel trilemma of self-accusation, perjury or contempt,' " <i>Doe,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#212" aria-description="Citation for case: Doe v. United States">487 U. S., at 212</a></span> (citation omitted), that defined the operation of the Star Chamber, wherein suspects were forced to choose between revealing incriminating private thoughts and forsaking their oath by committing perjury. See <i>United States</i> v. <i>Nobles,</i> <span class="citation" data-id="9426145"><a href="/opinion/109292/united-states-v-nobles/#233" aria-description="Citation for case: United States v. Nobles">422 U. S. 225, 233</a></span> (1975) ("The Fifth Amendment privilege against compulsory self-incrimination . . . protects `a private inner sanctum of individual feeling and thought and proscribes state intrusion to extract self-condemnation' ") (quoting <i>Couch</i> v. <i>United States,</i> <span class="citation" data-id="9425074"><a href="/opinion/108650/couch-v-united-states/#327" aria-description="Citation for case: Couch v. United States">409 U. S. 322, 327</a></span> (1973)).</p>
<p>We need not explore the outer boundaries of what is "testimonial" today, for our decision flows from the concept's core meaning. Because the privilege was designed primarily to prevent "a recurrence of the Inquisition and the Star Chamber, even if not in their stark brutality," <i>Ullmann</i> v. <i>United States,</i> <span class="citation" data-id="9421245"><a href="/opinion/105363/ullmann-v-united-states/#428" aria-description="Citation for case: Ullmann v. United States">350 U. S. 422, 428</a></span> (1956), it is evident that a suspect is "compelled . . . to be a witness against himself" at least whenever he must face the modern-day analog of the historic trilemma  either during a criminal trial where a sworn witness faces the identical three choices, or during custodial interrogation where, as we explained in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the choices are analogous and hence raise similar concerns.<sup>[10]</sup> Whatever <span class="star-pagination">*597</span> else it may include, therefore, the definition of "testimonial" evidence articulated in <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe</a></span></i> must encompass all responses to questions that, if asked of a sworn suspect during a criminal trial, could place the suspect in the "cruel trilemma." This conclusion is consistent with our recognition in <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe</a></span></i> that "[t]he vast majority of verbal statements thus will be testimonial" because "[t]here are very few instances in which a verbal statement, either oral or written, will not convey information or assert facts." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States">487 U. S., at 213</a></span>. Whenever a suspect is asked for a response requiring him to communicate an express or implied assertion of fact or belief,<sup>[11]</sup> the suspect confronts the "trilemma" of truth, falsity, or silence, and hence the response (whether based on truth or falsity) contains a testimonial component.</p>
<p>This approach accords with each of our post-<span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California"><i>Schmerber</i></a></span> cases finding that a particular oral or written response to express or implied questioning was nontestimonial; the questions presented in these cases did not confront the suspects with this trilemma. As we noted in <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States"><i>Doe, supra,</i> at 210-211</a></span>, the cases upholding compelled writing and voice exemplars did not involve situations in which suspects were asked to communicate any personal beliefs or knowledge of facts, and therefore the suspects were not forced to choose between <span class="star-pagination">*598</span> truthfully or falsely revealing their thoughts. We carefully noted in <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">388 U. S. 263</a></span> (1967), for example, that a "mere handwriting exemplar, <i>in contrast to the content of what is written,</i> like the voice or body itself, is an identifying physical characteristic outside [the privilege's] protection." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 266-267</a></span> (emphasis added). Had the suspect been asked to provide a writing sample of his own composition, the content of the writing would have reflected his assertion of facts or beliefs and hence would have been testimonial; but in <i><span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/" aria-description="Citation for case: Gilbert v. California">Gilbert</a></span></i> "[n]o claim [was] made that the content of the exemplars was testimonial or communicative matter." <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#267" aria-description="Citation for case: Gilbert v. California"><i>Id.,</i> at 267</a></span>.<sup>[12]</sup> And in <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe</a></span>,</i> the suspect was asked merely to sign a consent form waiving a privacy interest in foreign bank records. Because the consent form spoke in the hypothetical and did not identify any particular banks, accounts, or private records, the form neither "communicate[d] any factual assertions, implicit or explicit, [n]or convey[ed] any information to the Government." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#215" aria-description="Citation for case: Doe v. United States">487 U. S., at 215</a></span>. We concluded, therefore, that compelled execution of the consent directive did not "forc[e] [the suspect] to express the contents of his mind," <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#210" aria-description="Citation for case: Doe v. United States"><i>id.,</i> at 210, n. 9</a></span>, but rather forced the suspect only to make a "nonfactual statement." <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#213" aria-description="Citation for case: Doe v. United States"><i>Id.,</i> at 213, n. 11</a></span>.</p>
<p>In contrast, the sixth birthday question in this case required a testimonial response. When Officer Hosterman <span class="star-pagination">*599</span> asked Muniz if he knew the date of his sixth birthday and Muniz, for whatever reason, could not remember or calculate that date, he was confronted with the trilemma. By hypothesis, the inherently coercive environment created by the custodial interrogation precluded the option of remaining silent, see n. 10, <i>supra.</i> Muniz was left with the choice of incriminating himself by admitting that he did not then know the date of his sixth birthday, or answering untruthfully by reporting a date that he did not then believe to be accurate (an incorrect guess would be incriminating as well as untruthful). The content of his truthful answer supported an inference that his mental faculties were impaired, because his assertion (he did not know the date of his sixth birthday) was different from the assertion (he knew the date was (correct date)) that the trier of fact might reasonably have expected a lucid person to provide. Hence, the incriminating inference of impaired mental faculties stemmed, not just from the fact that Muniz slurred his response, but also from a testimonial aspect of that response.<sup>[13]</sup></p>
<p><span class="star-pagination">*600</span> The state court held that the sixth birthday question constituted an unwarned interrogation for purposes of the privilege against self-incrimination, 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>, and that Muniz's answer was incriminating. <i><span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/" aria-description="Citation for case: Commonwealth v. Muniz">Ibid.</a></span></i> The Commonwealth does not question either conclusion. Therefore, because we conclude that Muniz's response to the sixth birthday question was testimonial, the response should have been suppressed.</p>
<p></p>
<h2>C</h2>
<p>The Commonwealth argues that the seven questions asked by Officer Hosterman just <i>prior</i> to the sixth birthday question  regarding Muniz's name, address, height, weight, eye color, date of birth, and current age  did not constitute custodial interrogation as we have defined the term in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and subsequent cases. In <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> the Court referred to "interrogation" as actual "questioning initiated by law enforcement officers." 384 U. S., at 444. We have since clarified that definition, finding that the "goals of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> safeguards could be effectuated if those safeguards extended not only to express questioning, but also to "its functional equivalent.' " <i>Arizona</i> v. <i>Mauro,</i> <span class="citation" data-id="9430952"><a href="/opinion/111878/arizona-v-mauro/#526" aria-description="Citation for case: Arizona v. Mauro">481 U. S. 520, 526</a></span> (1987). In <i>Rhode Island</i> v. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291</a></span> (1980), the Court defined the phrase "functional equivalent" of express questioning to include "any words or actions on the part of the police (other than those normally attendant to arrest and custody) <span class="star-pagination">*601</span> that the police should know are reasonably likely to elicit an incriminating response from the suspect. The latter portion of this definition focuses primarily upon the perceptions of the suspect, rather than the intent of the police." <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><i>Id.,</i> at 301</a></span> (footnotes omitted); see also <i>Illinois</i> v. <i>Perkins, ante,</i> at 296. However, "[a]ny knowledge the police may have had concerning the unusual susceptibility of a defendant to a particular form of persuasion might be an important factor in determining" what the police reasonably should have known. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#302" aria-description="Citation for case: Rhode Island v. Innis"><i>Innis, supra,</i> at 302, n. 8</a></span>. Thus, custodial interrogation for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> includes both express questioning and words or actions that, given the officer's knowledge of any special susceptibilities of the suspect, the officer knows or reasonably should know are likely to "have . . . the force of a question on the accused," <i>Harryman</i> v. <i>Estelle,</i> <span class="citation" data-id="9466546"><a href="/opinion/375540/burley-clifton-harryman-v-w-j-estelle-jr-director-texas-department/#874" aria-description="Citation for case: Burley Clifton Harryman v. W. J. Estelle, Jr., Director,...">616 F. 2d 870, 874</a></span> (CA5 1980), and therefore be reasonably likely to elicit an incriminating response.</p>
<p>We disagree with the Commonwealth's contention that Officer Hosterman's first seven questions regarding Muniz's name, address, height, weight, eye color, date of birth, and current age do not qualify as custodial interrogation as we defined the term in <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra,</a></span></i> merely because the questions were not intended to elicit information for investigatory purposes. As explained above, the <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span></i> test focuses primarily upon "the perspective of the suspect." <i>Perkins, ante,</i> at 296. We agree with <i>amicus</i> United States, however, that Muniz's answers to these first seven questions are nonetheless admissible because the questions fall within a "routine booking question" exception which exempts from <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s coverage questions to secure the " `biographical data necessary to complete booking or pretrial services.' " Brief for United States as <i>Amicus Curiae</i> 12, quoting <i>United States</i> v. <i>Horton,</i> <span class="citation" data-id="521998"><a href="/opinion/521998/united-states-v-derrick-deon-horton-aka-thomas-deon-hill-united-states/#181" aria-description="Citation for case: United States v. Derrick Deon Horton, A/K/A Thomas Deon...">873 F. 2d 180, 181, n. 2</a></span> (CA8 1989). The state court found that the first seven questions were "requested for record-keeping purposes only," App. B16, and therefore the questions appear reasonably related to the police's administrative <span class="star-pagination">*602</span> concerns.<sup>[14]</sup> In this context, therefore, the first seven questions asked at the booking center fall outside the protections of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> and the answers thereto need not be suppressed.</p>
<p></p>
<h2>IV</h2>
<p>During the second phase of the videotaped proceedings, Officer Hosterman asked Muniz to perform the same three sobriety tests that he had earlier performed at roadside prior to his arrest: the "horizontal gaze nystagmus" test, the "walk and turn" test, and the "one leg stand" test. While Muniz was attempting to comprehend Officer Hosterman's instructions and then perform the requested sobriety tests, Muniz made several audible and incriminating statements.<sup>[15]</sup> Muniz argued to the state court that both the videotaped performance of the physical tests themselves and the audiorecorded verbal statements were introduced in violation of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>The court refused to suppress the videotaped evidence of Muniz's paltry performance on the physical sobriety tests, reasoning that " `[r]equiring a driver to perform physical [sobriety] tests . . . does not violate the privilege against self-incrimination because the evidence procured is of a physical nature rather than testimonial.' " 377 Pa. Super., at 387, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 422</a></span> (quoting <i>Commonwealth</i> v. <i><span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/" aria-description="Citation for case: Commonwealth v. Benson">Benson</a></span>,</i> 280 Pa. <span class="star-pagination">*603</span> Super., at 29, <span class="citation" data-id="2259488"><a href="/opinion/2259488/commonwealth-v-benson/#387" aria-description="Citation for case: Commonwealth v. Benson">421 A. 2d, at 387</a></span>).<sup>[16]</sup> With respect to Muniz's verbal statements, however, the court concluded that "none of Muniz's utterances were spontaneous, voluntary verbalizations," 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>, and because they were "elicited before Muniz received his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, they should have been excluded as evidence." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i></p>
<p>We disagree. Officer Hosterman's dialogue with Muniz concerning the physical sobriety tests consisted primarily of carefully scripted instructions as to how the tests were to be performed. These instructions were not likely to be perceived as calling for any verbal response and therefore were not "words or actions" constituting custodial interrogation, with two narrow exceptions not relevant here.<sup>[17]</sup> The dialogue also contained limited and carefully worded inquiries as to whether Muniz understood those instructions, but these focused inquiries were necessarily "attendant to" the police <span class="star-pagination">*604</span> procedure held by the court to be legitimate. Hence, Muniz's incriminating utterances during this phase of the videotaped proceedings were "voluntary" in the sense that they were not elicited in response to custodial interrogation.<sup>[18]</sup> See <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#564" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 564, n. 15</a></span> (1983) (drawing analogy to "police request to submit to fingerprinting or photography" and holding that police inquiry whether suspect would submit to blood-alcohol test was not "interrogation within the meaning of <i>Miranda</i>").</p>
<p>Similarly, we conclude that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not require suppression of the statements Muniz made when asked to submit to a breathalyzer examination. Officer Deyo read Muniz a prepared script explaining how the test worked, the nature of Pennsylvania's Implied Consent Law, and the legal consequences that would ensue should he refuse. Officer Deyo then asked Muniz whether he understood the nature of the test and the law and whether he would like to submit to the test. Muniz asked Officer Deyo several questions concerning the legal consequences of refusal, which Deyo answered directly, and Muniz then commented upon his state of inebriation. 377 Pa. Super., at 387, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#422" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 422</a></span>. After offering to take the test only after waiting a couple of hours or drinking some water, Muniz ultimately refused.<sup>[19]</sup></p>
<p><span class="star-pagination">*605</span> We believe that Muniz's statements were not prompted by an interrogation within the meaning of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> and therefore the absence of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings does not require suppression of these statements at trial.<sup>[20]</sup> As did Officer Hosterman when administering the three physical sobriety tests, see <i>supra,</i> at 603-604, Officer Deyo carefully limited her role to providing Muniz with relevant information about the breathalyzer test and the Implied Consent Law. She questioned Muniz only as to whether he understood her instructions and wished to submit to the test. These limited and focused inquiries were necessarily "attendant to" the legitimate police procedure, see <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#564" aria-description="Citation for case: South Dakota v. Neville"><i>Neville, supra,</i> at 564, n. 15</a></span>, and were not likely to be perceived as calling for any incriminating response.<sup>[21]</sup></p>
<p></p>
<h2>V</h2>
<p>We agree with the state court's conclusion that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> requires suppression of Muniz's response to the question regarding the date of his sixth birthday, but we do not agree that the entire audio portion of the videotape must be suppressed.<sup>[22]</sup> Accordingly, the court's judgment reversing <span class="star-pagination">*606A</span> Muniz's conviction is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p><span class="star-pagination">*606B</span> CHIEF JUSTICE REHNQUIST, with whom JUSTICE WHITE, JUSTICE BLACKMUN, and JUSTICE STEVENS join, concurring in part, concurring in the result in part, and dissenting in part.</p>
<p>I join Parts I, II, III-A, and IV of the Court's opinion. In addition, although I agree with the conclusion in Part III-C that the seven "booking" questions should not be suppressed, I do so for a reason different from that of JUSTICE BRENNAN. I dissent from the Court's conclusion that Muniz's response to the "sixth birthday question" should have been suppressed.</p>
<p>The Court holds that the sixth birthday question Muniz was asked required a testimonial response, and that its admission at trial therefore violated Muniz's privilege against compulsory self-incrimination. The Court says:</p>
<blockquote>"When Officer Hosterman asked Muniz if he knew the date of his sixth birthday and Muniz, for whatever reason, could not remember or calculate that date, he was confronted with the trilemma [<i>i.e.,</i> the `"trilemma" of truth, falsity, or silence,' see <i>ante,</i> at 597]. . . . Muniz was left with the choice of incriminating himself by admitting that he did not then know the date of his sixth birthday, or answering untruthfully by reporting a date that he did not then believe to be accurate (an incorrect guess would be incriminating as well as untruthful)." <i>Ante,</i> at 598-599.</blockquote>
<p>As an assumption about human behavior, this statement is wrong. Muniz would no more have felt compelled to fabricate a false date than one who cannot read the letters on an eye chart feels compelled to fabricate false letters; nor does a wrong guess call into question a speaker's veracity. The Court's statement is also a flawed predicate on which to base its conclusion that Muniz's answer to this question was "testimonial" for purposes of the Fifth Amendment.</p>
<p><span class="star-pagination">*607</span> The need for the use of the human voice does not automatically make an answer testimonial, <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 222-223</a></span> (1967), any more than does the fact that a question calls for the exhibition of one's handwriting in written characters. <i>Gilbert</i> v. <i>California,</i> <span class="citation" data-id="9423477"><a href="/opinion/107487/gilbert-v-california/#266" aria-description="Citation for case: Gilbert v. California">388 U. S. 263, 266-267</a></span> (1967). In <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), we held that the extraction and chemical analysis of a blood sample involved no "shadow of testimonial compulsion upon or enforced communication by the accused." <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California"><i>Id.,</i> at 765</a></span>. All of these holdings were based on Justice Holmes' opinion in <i>Holt</i> v. <i>United States,</i> <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/" aria-description="Citation for case: Holt v. United States">218 U. S. 245</a></span> (1910), where he said for the Court that "the prohibition of compelling a man in a criminal court to be witness against himself is a prohibition of the use of physical or moral compulsion to extort communications from him, not an exclusion of his body as evidence when it may be material." <span class="citation" data-id="97290"><a href="/opinion/97290/holt-v-united-states/#252" aria-description="Citation for case: Holt v. United States"><i>Id.,</i> at 252-253</a></span>.</p>
<p>The sixth birthday question here was an effort on the part of the police to check how well Muniz was able to do a simple mathematical exercise. Indeed, had the question related only to the date of his birth, it presumably would have come under the "booking exception" to <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), to which the Court refers elsewhere in its opinion. The Court holds in this very case that Muniz may be required to perform a "horizontal gaze nystagmus" test, the "walk and turn" test, and the "one leg stand" test, all of which are designed to test a suspect's physical coordination. If the police may require Muniz to use his body in order to demonstrate the level of his physical coordination, there is no reason why they should not be able to require him to speak or write in order to determine his mental coordination. That was all that was sought here. Since it was permissible for the police to extract and examine a sample of Schmerber's blood to determine how much that part of his system had been affected by alcohol, I see no reason why they may not examine the functioning of Muniz's mental processes for the same purpose.</p>
<p><span class="star-pagination">*608</span> Surely if it were relevant, a suspect might be asked to take an eye examination in the course of which he might have to admit that he could not read the letters on the third line of the chart. At worst, he might utter a mistaken guess. Muniz likewise might have attempted to guess the correct response to the sixth birthday question instead of attempting to calculate the date or answer "I don't know." But the potential for giving a bad guess does not subject the suspect to the truth-falsity-silence predicament that renders a response testimonial and, therefore, within the scope of the Fifth Amendment privilege.</p>
<p>For substantially the same reasons, Muniz's responses to the videotaped "booking" questions were not testimonial and do not warrant application of the privilege. Thus, it is unnecessary to determine whether the questions fall within the "routine booking question" exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> JUSTICE BRENNAN recognizes.</p>
<p>I would reverse in its entirety the judgment of the Superior Court of Pennsylvania. But given the fact that five members of the Court agree that Muniz's response to the sixth birthday question should have been suppressed, I agree that the judgment of the Superior Court should be vacated so that, on remand, the court may consider whether admission of the response at trial was harmless error.</p>
<p>JUSTICE MARSHALL, concurring in part and dissenting in part.</p>
<p>I concur in Part III-B of the Court's opinion that the "sixth birthday question" required a testimonial response from respondent Muniz. For the reasons discussed below, see n. 1, <i>infra,</i> that question constituted custodial interrogation. Because the police did not apprise Muniz of his rights under <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), before asking the question, his response should have been suppressed.</p>
<p>I disagree, however, with JUSTICE BRENNAN's recognition in Part III-C of a "routine booking question" exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> Moreover, even were such an exception warranted, <span class="star-pagination">*609</span> it should not extend to booking questions that the police should know are reasonably likely to elicit incriminating responses. Because the police in this case should have known that the seven booking questions were reasonably likely to elicit incriminating responses and because those questions were not preceded by <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, Muniz's testimonial responses should have been suppressed.</p>
<p>I dissent from the Court's holding in Part IV that Muniz's testimonial statements in connection with the three sobriety tests and the breathalyzer test were not the products of custodial interrogation. The police should have known that the circumstances in which they confronted Muniz, combined with the detailed instructions and questions concerning the tests and the Commonwealth's Implied Consent Law, were reasonably likely to elicit an incriminating response, and therefore constituted the "functional equivalent" of express questioning. <i>Rhode Island</i> v. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 301</a></span> (1980). Muniz's statements to the police in connection with these tests thus should have been suppressed because he was not first given the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.</p>
<p>Finally, the officer's directions to Muniz to count aloud during two of the sobriety tests sought testimonial responses, and Muniz's responses were incriminating. Because Muniz was not informed of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights prior to the tests, those responses also should have been suppressed.</p>
<p></p>
<h2>I</h2>
<p></p>
<h2>A</h2>
<p>JUSTICE BRENNAN would create yet another exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>:</i> the "routine booking question" exception. See also <i>Illinois</i> v. <i>Perkins, ante,</i> p. 292 (creating exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> for custodial interrogation by an undercover police officer posing as the suspect's fellow prison inmate). Such exceptions undermine <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>'s fundamental principle that the doctrine should be clear so that it can be easily applied by both police and courts. See <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#441" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda, supra,</i> at 441-442</a></span>; <span class="star-pagination">*610</span> <i>Fare</i> v. <i>Michael C.,</i> <span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#718" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 718</a></span> (1979); <i>Perkins, ante,</i> at 308-309 (MARSHALL, J., dissenting). JUSTICE BRENNAN's position, were it adopted by a majority of the Court, would necessitate difficult, time-consuming litigation over whether particular questions asked during booking are "routine," whether they are necessary to secure biographical information, whether that information is itself necessary for recordkeeping purposes, and whether the questions are  despite their routine nature  designed to elicit incriminating testimony. The far better course would be to maintain the clarity of the doctrine by requiring police to preface all direct questioning of a suspect with <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings if they want his responses to be admissible at trial.</p>
<p></p>
<h2>B</h2>
<p>JUSTICE BRENNAN nonetheless asserts that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not apply to express questioning designed to secure " ` "biographical data necessary to complete booking or pretrial services," ' " <i>ante,</i> at 601 (citation omitted), so long as the questioning is not " `designed to elicit incriminatory admissions,' " <i>ante,</i> at 602, n. 14 (quoting Brief for United States as <i>Amicus Curiae</i> 13; citing <i>United States</i> v. <i>Avery,</i> <span class="citation" data-id="424921"><a href="/opinion/424921/united-states-v-ozzie-lee-avery-jr/#1024" aria-description="Citation for case: United States v. Ozzie Lee Avery, Jr.">717 F. 2d 1020, 1024-1025</a></span> (CA6 1983) (acknowledging that "[e]ven a relatively innocuous series of questions may, in light of the factual circumstances and the susceptibility of a particular suspect, be reasonably likely to elicit an incriminating response"); <i>United States</i> v. <i>Mata-Abundiz,</i> <span class="citation" data-id="424960"><a href="/opinion/424960/united-states-v-jesus-mata-abundiz/#1280" aria-description="Citation for case: United States v. Jesus Mata-Abundiz">717 F. 2d 1277, 1280</a></span> (CA9 1983) (holding that routine booking question exception does not apply if "the questions are reasonably likely to elicit an incriminating response in a particular situation"); <i>United States</i> v. <i>Glen-Archila,</i> <span class="citation" data-id="403655"><a href="/opinion/403655/united-states-v-homero-glen-archila-dudley-astor-may-mitchell/#816" aria-description="Citation for case: United States v. Homero Glen-Archila, Dudley Astor...">677 F. 2d 809, 816, n. 18</a></span> (CA11 1982) ("Even questions that usually are routine must be proceeded <i>[sic]</i> by <i>Miranda</i> warnings if they are intended to produce answers that are incriminating")). Even if a routine booking question exception to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> were warranted, that exception should not extend to any booking question <span class="star-pagination">*611</span> that the police should know is reasonably likely to elicit an incriminating response, cf. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span>, regardless of whether the question is "designed" to elicit an incriminating response. Although the police's intent to obtain an incriminating response is relevant to this inquiry, the key components of the analysis are the nature of the questioning, the attendant circumstances, and the perceptions of the suspect. Cf. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><i>id.,</i> at 301, n. 7</a></span>. Accordingly, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are required before the police may engage in any questioning reasonably likely to elicit an incriminating response.</p>
<p>Here, the police should have known that the seven booking questions  regarding Muniz's name, address, height, weight, eye color, date of birth, and age  were reasonably likely to elicit incriminating responses from a suspect whom the police believed to be intoxicated. Cf. <i>id.,</i> at 302, n. 8 ("Any knowledge the police may have had concerning the unusual susceptibility of a defendant to a particular form of persuasion might be an important factor in determining whether the police should have known that their words or actions were reasonably likely to elicit an incriminating response from the suspect"). Indeed, as the Court acknowledges, Muniz did in fact "stumbl[e] over his address and age," <i>ante,</i> at 586; more specifically, he was unable to give his address without looking at his license and initially told police the wrong age. Moreover, the very fact that, after a suspect has been arrested for driving under the influence, the Pennsylvania police regularly videotape the subsequent questioning strongly implies a purpose to the interrogation other than "recordkeeping." The seven questions in this case, then, do not fall within the routine booking question exception even under JUSTICE BRENNAN's standard.<sup>[1]</sup></p>
<p></p>
<h2>
<span class="star-pagination">*612</span> C</h2>
<p>Although JUSTICE BRENNAN does not address this issue, the booking questions sought "testimonial" responses for the same reason the sixth birthday question did: because the content of the answers would indicate Muniz's state of mind. <i>Ante,</i> at 598-599, and n. 12. See also <i>Estelle</i> v. <i>Smith,</i> <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#464" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454, 464-465</a></span> (1981). The booking questions, like the sixth birthday question, required Muniz to (1) answer correctly, indicating lucidity, (2) answer incorrectly, implying that his mental faculties were impaired, or (3) state that he did not know the answer, also indicating impairment. Muniz's initial incorrect response to the question about his age and his inability to give his address without looking at his license, like his inability to answer the sixth birthday question, in fact gave rise to the incriminating inference that his mental faculties were impaired. Accordingly, because the police did not inform Muniz of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights before asking the booking questions, his responses should have been suppressed.</p>
<p></p>
<h2>II</h2>
<p></p>
<h2>A</h2>
<p>The Court finds in Part IV of its opinion that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is inapplicable to Muniz's statements made in connection with the three sobriety tests and the breathalyzer examination because those statements (which were undoubtedly testimonial) were not the products of "custodial interrogation." In my view, however, the circumstances of this case  in particular, Muniz's apparent intoxication  rendered the officers' words and actions the "functional equivalent" of express questioning <span class="star-pagination">*613</span> because the police should have known that their conduct was "reasonably likely to evoke an incriminating response." <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis"><i>Innis, supra,</i> at 301</a></span>. As the Court recounts, <i>ante,</i> at 602-604, Officer Hosterman instructed Muniz how to perform the sobriety tests, inquired whether Muniz understood the instructions, and then directed Muniz to perform the tests. Officer Deyo later explained the breathalyzer examination and the nature of the Commonwealth's Implied Consent Law, and asked several times if Muniz understood the Law and wanted to take the examination. <i>Ante,</i> at 604. Although these words and actions might not prompt most sober persons to volunteer incriminating statements, Officers Hosterman and Deyo had good reason to believe  from the arresting officer's observations, App. 13-19 (testimony of Officer Spotts), from Muniz's failure of the three roadside sobriety tests, <i>id.,</i> at 19, and from their own observations  that Muniz was intoxicated. The officers thus should have known that Muniz was reasonably likely to have trouble understanding their instructions and their explanation of the Implied Consent Law, and that he was reasonably likely to indicate, in response to their questions, that he did not understand the tests or the Law. Moreover, because Muniz made several incriminating statements regarding his intoxication during and after the roadside tests, <i>id.,</i> at 20-21, the police should have known that the same tests at the booking center were reasonably likely to prompt similar incriminating statements.</p>
<p>The Court today, however, completely ignores Muniz's condition and focuses solely on the nature of the officers' words and actions. As the Court held in <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>,</i> however, the focus in the "functional equivalent" inquiry is on "the perceptions of the suspect," not on the officers' conduct viewed in isolation. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301</a></span>. Moreover, the <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span></i> Court emphasized that the officers' knowledge of any "unusual susceptibility" of a suspect to a particular means of eliciting information is relevant to the question whether they should have known that their conduct was reasonably likely to elicit <span class="star-pagination">*614</span> an incriminating response. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#302" aria-description="Citation for case: Rhode Island v. Innis"><i>Id.,</i> at 302, n. 8</a></span>; <i>supra,</i> at 610-611. See also <i>Arizona</i> v. <i>Mauro,</i> <span class="citation" data-id="9430952"><a href="/opinion/111878/arizona-v-mauro/#531" aria-description="Citation for case: Arizona v. Mauro">481 U. S. 520, 531</a></span> (1987) (STEVENS, J., dissenting) (police "interrogated" suspect by allowing him to converse with his wife "at a time when they knew [the conversation] was reasonably likely to produce an incriminating statement"). Muniz's apparent intoxication, then, and the police's knowledge of his statements during and after the roadside tests compel the conclusion that the police should have known that their words and actions were reasonably likely to elicit an incriminating response.<sup>[2]</sup> Muniz's statements were thus the product of custodial interrogation and should have been suppressed because Muniz was not first given the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.</p>
<p></p>
<h2>B</h2>
<p>The Court concedes that Officer Hosterman's directions that Muniz count aloud to 9 while performing the "walk and turn" test and to 30 while performing the "one leg stand" test constituted custodial interrogation. <i>Ante,</i> at 603, and n. 17. Also indisputable is the testimonial nature of the responses sought by those directions; the content of Muniz's counting, just like his answers to the sixth birthday and the booking questions, would provide the basis for an inference regarding his state of mind. Cf. <i>ante,</i> at 599; <i>supra,</i> at 612. The Court finds the admission at trial of Muniz's responses permissible, however, because they were not incriminating "except to the extent [they] exhibited a tendency to slur words, <span class="star-pagination">*615</span> which [the Court already found to be] nontestimonial [evidence]." <i>Ante,</i> at 603, n. 17. The Court's conclusion is wrong for two reasons. First, as a factual matter, Muniz's responses <i>were</i> incriminating for a reason other than his apparent slurring. Muniz did not count at all during the walk and turn test, supporting the inference that he was unable to do so.<sup>[3]</sup> And, contrary to the Court's assertion, <i>ibid.,</i> during the one leg stand test, Muniz incorrectly counted in Spanish from one to six, skipping the number two. Even if Muniz had not skipped "two," his failure to complete the count was incriminating in itself.</p>
<p>Second, and more importantly, Muniz's responses would have been "incriminating" for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> even if he had fully and accurately counted aloud during the two tests. As the Court stated in <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span>,</i> "[b]y `incriminating response' we refer to any response  whether inculpatory or exculpatory  that the <i>prosecution</i> may seek to introduce at trial." <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#301" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 301, n. 5</a></span>. See also <i>Miranda,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476-477</a></span> ("The privilege against self-incrimination protects the individual from being compelled to incriminate himself in any manner; it does not distinguish degrees of incrimination. Similarly, for precisely the same reason, no distinction may be drawn between inculpatory statements and statements alleged to be merely `exculpatory' "). Thus, <i>any</i> response by <span class="star-pagination">*616</span> Muniz that the prosecution sought to use against him was incriminating under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> That the majority thinks Muniz's responses were incriminating only because of his slurring is therefore irrelevant. Because Muniz did not receive the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, then, his responses should have been suppressed.</p>
<p></p>
<h2>III</h2>
<p>All of Muniz's responses during the videotaped session were prompted by questions that sought testimonial answers during the course of custodial interrogation. Because the police did not read Muniz the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings before he gave those responses, the responses should have been suppressed. I would therefore affirm the judgment of the state court.<sup>[4]</sup></p>
<h2>NOTES</h2>
<p>[*]  <i>Solicitor General Starr, Assistant Attorney General Dennis, Deputy Solicitor General Bryson,</i> and <i>Christopher J. Wright</i> filed a brief for the United States as <i>amicus curiae</i> urging reversal.</p>
<p>[1]  The "horizontal gaze nystagmus" test measures the extent to which a person's eyes jerk as they follow an object moving from one side of the person's field of vision to the other. The test is premised on the understanding that, whereas everyone's eyes exhibit some jerking while turning to the side, when the subject is intoxicated "the onset of the jerking occurs after fewer degrees of turning, and the jerking at more extreme angles becomes more distinct." 1 R. Erwin et al., Defense of Drunk Driving Cases § 8A.99, pp. 8A-43, 8A-45 (1989). The "walk and turn" test requires the subject to walk heel to toe along a straight line for nine paces, pivot, and then walk back heel to toe along the line for another nine paces. The subject is requires to count each pace aloud from one to nine. The "one leg stand" test requires the subject to stand on one leg with the other leg extended in the air for 30 seconds, while counting aloud from 1 to 30.</p>
<p>[2]  There was a 14-minute delay between the completion of the physical sobriety tests and the beginning of the breathalyzer test. During this period, Muniz briefly engaged in conversation with Officer Hosterman. This 14-minute segment of the videotape was not shown at trial. App. 29.</p>
<p>[3]  The court did not suppress Muniz's verbal admissions to the arresting officer during the roadside tests, ruling that Muniz was not taken into custody for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> until he was arrested after the roadside tests were completed. See <i>Pennsylvania</i> v. <i>Bruder,</i> <span class="citation" data-id="9431478"><a href="/opinion/112152/pennsylvania-v-bruder/" aria-description="Citation for case: Pennsylvania v. Bruder">488 U. S. 9</a></span> (1988).</p>
<p>[4]  The Superior Court's opinion refers to Art. 1, § 9, of the Pennsylvania Constitution but explains that this provision " `offers a protection against self-incrimination identical to that provided by the Fifth Amendment.' " 377 Pa. Super., at 386, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 421</a></span> (quoting <i>Commonwealth</i> v. <i>Conway,</i> <span class="citation" data-id="9648993"><a href="/opinion/1533585/commonwealth-v-conway/#498" aria-description="Citation for case: Commonwealth v. Conway">368 Pa. Super. 488, 498</a></span>, <span class="citation" data-id="9648993"><a href="/opinion/1533585/commonwealth-v-conway/#546" aria-description="Citation for case: Commonwealth v. Conway">534 A. 2d 541, 546</a></span> (1987)). The decision therefore does not rest on an independent and adequate state ground. See <i>Michigan</i> v. <i>Long,</i> <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983).</p>
<p>[5]  In <i>Malloy</i> v. <i>Hogan,</i> <span class="citation" data-id="9422839"><a href="/opinion/106862/malloy-v-hogan/" aria-description="Citation for case: Malloy v. Hogan">378 U. S. 1</a></span> (1964), we held the privilege against self-incrimination applicable to the States through the Fourteenth Amendment.</p>
<p>[6]  Under Pennsylvania law, driving under the influence of alcohol consists of driving while intoxicated to a degree " `which substantially impairs [the suspect's] judgment, or clearness of intellect, or any of the normal faculties essential to the safe operation of an automobile.' " <i>Commonwealth</i> v. <i>Griscavage,</i> <span class="citation" data-id="9707237"><a href="/opinion/1996025/commonwealth-v-griscavage/#545" aria-description="Citation for case: Commonwealth v. Griscavage">512 Pa. 540, 545</a></span>, <span class="citation" data-id="9707237"><a href="/opinion/1996025/commonwealth-v-griscavage/#1258" aria-description="Citation for case: Commonwealth v. Griscavage">517 A. 2d 1256, 1258</a></span> (1986) (emphasis deleted).</p>
<p>[7]  See, <i>e. g., </i><i>Doe</i> v. <i>United States,</i> <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#211" aria-description="Citation for case: Doe v. United States">487 U. S. 201, 211, n. 10</a></span> (1988) ("[T]he <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> line of cases does not draw a distinction between unprotected evidence sought for its physical characteristics and protected evidence sought for its [other] content. Rather, the Court distinguished between the suspect's being compelled himself to <i>serve as evidence</i> and the suspect's being compelled to <i>disclose or communicate information or facts</i> that might serve as or lead to incriminating evidence") (emphasis added); cf. <i>Baltimore Dept. of Social Services</i> v. <i>Bouknight,</i> <span class="citation" data-id="9431889"><a href="/opinion/112360/baltimore-city-department-of-social-services-v-bouknight/#555" aria-description="Citation for case: Baltimore City Department of Social Services v. Bouknight">493 U. S. 549, 555</a></span> (1990) (individual compelled to produce document or other tangible item to State "may not claim the [Fifth] Amendment's protections based upon the incrimination that may result from the contents or nature of the thing demanded" but may "clai[m] the benefits of the privilege because the act of production would amount to testimony").</p>
<p>[8]  See <i><span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/" aria-description="Citation for case: Doe v. United States">Doe, supra,</a></span></i> at 212-213 (quoting <i>Murphy</i> v. <i>Waterfront Comm'n of New York Harbor,</i> <span class="citation" data-id="9422843"><a href="/opinion/106864/murphy-v-waterfront-commission-of-new-york-harbor/#55" aria-description="Citation for case: Murphy v. Waterfront Commission of New York Harbor">378 U. S. 52, 55</a></span> (1964) (internal citations omitted)): "[T]he privilege is founded on `our unwillingness to subject those suspected of crime to the cruel trilemma of self-accusation, perjury or contempt; our preference for an accusatorial rather than an inquisitorial system of criminal justice; our fear that self-incriminating statements will be elicited by inhumane treatment and abuses; our sense of fair play which dictates "a fair state-individual balance by requiring the government . . . in its contest with the individual to shoulder the entire load," . . . ; our respect for the inviolability of the human personality and of the right of each individual "to a private enclave where he may lead a private life," . . . ; our distrust of self-deprecatory statements; and our realization that the privilege, while sometimes "a shelter to the guilty," is often "a protection to the innocent." ' "</p>
<p>[9]  This definition applies to both verbal and nonverbal conduct; nonverbal conduct contains a testimonial component whenever the conduct reflects the actor's communication of his thoughts to another. See <span class="citation" data-id="9431394"><a href="/opinion/112123/doe-v-united-states/#209" aria-description="Citation for case: Doe v. United States"><i>Doe, supra,</i> at 209-210</a></span>, and n. 8; <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#761" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 761, n. 5</a></span> (1966) ("A nod or head-shake is as much a `testimonial' or `communicative' act in this sense as are spoken words"); see also <i>Braswell</i> v. <i>United States,</i> <span class="citation" data-id="9431386"><a href="/opinion/112120/braswell-v-united-states/#122" aria-description="Citation for case: Braswell v. United States">487 U. S. 99, 122</a></span> (1988) (KENNEDY, J., dissenting) ("Those assertions [contained within the act of producing subpoenaed documents] can convey information about that individual's knowledge and state of mind as effectively as spoken statements, and the Fifth Amendment protects individuals from having such assertions compelled by their own acts").</p>
<p>[10]  During custodial interrogation, the pressure on the suspect to respond flows not from the threat of contempt sanctions, but rather from the "inherently compelling pressures which work to undermine the individual's will to resist and to compel him to speak where he would not otherwise do so freely." <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 467</a></span> (1966). Moreover, false testimony does not give rise directly to sanctions (either religious sanctions for lying under oath or prosecutions for perjury), but only indirectly (false testimony might itself prove incriminating, either because it links (albeit falsely) the suspect to the crime or because the prosecution might later prove at trial that the suspect lied to the police, giving rise to an inference of guilty conscience). Despite these differences, however, "[w]e are satisfied that all the principles embodied in the privilege apply to informal compulsion exerted by law-enforcement officers during in-custody questioning." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#461" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 461</a></span>; see <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona"><i>id.,</i> at 458</a></span> (noting "intimate connection between the privilege against self-incrimination and police custodial questioning").</p>
<p>[11]  As we explain <i>infra,</i> at 600-601, for purposes of custodial interrogation such a question may be either express, as in this case, or else implied through words or actions reasonably likely to elicit a response.</p>
<p>[12]  See also <i>United States</i> v. <i>Wade,</i> <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#222" aria-description="Citation for case: United States v. Wade">388 U. S. 218, 222-223</a></span> (1967) ("[T]o utter words purportedly uttered by the robber [and dictated to the suspect by the police] was not compulsion to utter statements of a `testimonial' nature; [the suspect] was required to use his voice as an identifying physical characteristic, not to speak his guilt" because the words did not reflect any facts or beliefs asserted by the suspect); <i>United States</i> v. <i>Dionisio,</i> <span class="citation" data-id="108709"><a href="/opinion/108709/united-states-v-dionisio/#7" aria-description="Citation for case: United States v. Dionisio">410 U. S. 1, 7</a></span> (1973) (where suspects were asked to create voice exemplars by reading already-prepared transcripts, the "voice recordings were to be used solely to measure the physical properties of the witnesses' voices, not for the testimonial or communicative content of what was to be said" because the content did not reflect any facts or beliefs asserted by the suspects).</p>
<p>[13]  The Commonwealth's protest that it had no investigatory interest in the actual date of Muniz's sixth birthday, see Tr. of Oral Arg. 18, is inapposite. The critical point is that the Commonwealth had an investigatory interest in Muniz's assertion of belief that was communicated by his answer to the question. Putting it another way, the Commonwealth may not have cared about the <i>correct</i> answer, but it cared about <i>Muniz's</i> answer. The incriminating inference stems from the then-existing contents of Muniz's mind as evidenced by his assertion of his knowledge at that time.
</p>
<p>This distinction is reflected in <i>Estelle</i> v. <i>Smith,</i> <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/" aria-description="Citation for case: Estelle v. Smith">451 U. S. 454</a></span> (1981), where we held that a defendant's answers to questions during a psychiatric examination were testimonial in nature. The psychiatrist asked a series of questions, some focusing on the defendant's account of the crime. After analyzing both the "statements [the defendant] made, and remarks he omitted." <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#464" aria-description="Citation for case: Estelle v. Smith"><i>id.,</i> at 464</a></span>, the psychiatrist made a prognosis as to the defendant's "future dangerousness" and testified to this effect at his capital sentencing hearing. The psychiatrist had no investigative interest in whether the defendant's account of the crime and other disclosures were either accurate or complete as a historical matter; rather, he relied on the remarks  both those made and omitted  to infer that the defendant would likely pose a threat to society in the future because of his state of mind. We nevertheless explained that the "Fifth Amendment privilege . . . is directly involved here because the State used as evidence against [the defendant] the <i>substance of his disclosures</i> during the pretrial psychiatric examination." <span class="citation" data-id="9428322"><a href="/opinion/110474/estelle-v-smith/#464" aria-description="Citation for case: Estelle v. Smith"><i>Id.,</i> at 464-465</a></span> (emphasis added). The psychiatrist may have presumed the defendant's remarks to be truthful for purposes of drawing his inferences as to the defendant's state of mind, see <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#561" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553, 561-562, n. 12</a></span> (1983), but that is true in Muniz's case as well: The incriminating inference of mental confusion is based on the premise that Muniz was responding truthfully to Officer Hosterman's question when he stated that he did not then know the date of his sixth birthday.</p>
<p>[14]  As <i>amicus</i> United States explains, "[r]ecognizing a `booking exception' to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> does not mean, of course, that any question asked during the booking process falls within that exception. Without obtaining a waiver of the suspect's <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights, the police may not ask questions, even during booking, that are designed to elicit incriminatory admissions." Brief for United States as <i>Amicus Curiae</i> 13. See, <i>e. g., </i><i>United States</i> v. <i>Avery,</i> <span class="citation" data-id="424921"><a href="/opinion/424921/united-states-v-ozzie-lee-avery-jr/#1024" aria-description="Citation for case: United States v. Ozzie Lee Avery, Jr.">717 F. 2d 1020, 1024-1025</a></span> (CA6 1983); <i>United States</i> v. <i>Mata-Abundiz,</i> <span class="citation" data-id="424960"><a href="/opinion/424960/united-states-v-jesus-mata-abundiz/#1280" aria-description="Citation for case: United States v. Jesus Mata-Abundiz">717 F. 2d 1277, 1280</a></span> (CA9 1983); <i>United States</i> v. <i>Glen-Archila,</i> <span class="citation" data-id="403655"><a href="/opinion/403655/united-states-v-homero-glen-archila-dudley-astor-may-mitchell/#816" aria-description="Citation for case: United States v. Homero Glen-Archila, Dudley Astor...">677 F. 2d 809, 816, n. 18</a></span> (CA11 1982).</p>
<p>[15]  Most of Muniz's utterances were not clearly discernible, though several of them suggested excuses as to why he could not perform the physical tests under these circumstances.</p>
<p>[16]  This conclusion is in accord with that of many other state courts, which have reasoned that standard sobriety tests measuring reflexes, dexterity, and balance do not require the performance of testimonial acts. See, <i>e. g., </i><i>Weatherford</i> v. <i>State,</i> <span class="citation" data-id="9682429"><a href="/opinion/1782123/weatherford-v-state/" aria-description="Citation for case: Weatherford v. State">286 Ark. 376</a></span>, <span class="citation" data-id="9682429"><a href="/opinion/1782123/weatherford-v-state/" aria-description="Citation for case: Weatherford v. State">692 S. W. 2d 605</a></span> (1985); <i>People</i> v. <i>Boudreau,</i> 115 App. Div. 2d 652, 496 N. Y. S. 2d 489 (1985); <i>Commonwealth</i> v. <i>Brennan,</i> <span class="citation" data-id="2102837"><a href="/opinion/2102837/commonwealth-v-brennan/" aria-description="Citation for case: Commonwealth v. Brennan">386 Mass. 772</a></span>, <span class="citation" data-id="2102837"><a href="/opinion/2102837/commonwealth-v-brennan/" aria-description="Citation for case: Commonwealth v. Brennan">438 N. E. 2d 60</a></span> (1982); <i>State</i> v. <i>Badon,</i> <span class="citation" data-id="1702883"><a href="/opinion/1702883/state-v-badon/" aria-description="Citation for case: State v. Badon">401 So. 2d 1178</a></span> (La. 1981); <i>State</i> v. <i>Arsenault,</i> 115 N. H. 109, <span class="citation" data-id="2263639"><a href="/opinion/2263639/state-v-arsenault/" aria-description="Citation for case: State v. Arsenault">336 A. 2d 244</a></span> (1975). Muniz does not challenge the state court's conclusion on this point, and therefore we have no occasion to review it.</p>
<p>[17]  The two exceptions consist of Officer Hosterman's requests that Muniz count aloud from 1 to 9 while performing the "walk and turn" test and that he count aloud from 1 to 30 while balancing during the "one leg stand" test. Muniz's counting at the officer's request qualifies as a response to custodial interrogation. However, as Muniz counted accurately (in Spanish) for the duration of his performance on the "one leg stand" test (though he did not complete it), his verbal response to this instruction was not incriminating except to the extent that it exhibited a tendency to slur words, which we have already explained is a nontestimonial component of his response. See <i>supra,</i> at 590-592. Muniz did not count during the "walk and turn" test, and he does not argue that his failure to do so has any independent incriminating significance. We therefore need not decide today whether Muniz's counting (or not counting) itself was "testimonial" within the meaning of the privilege.</p>
<p>[18]  We cannot credit the state court's contrary determination that Muniz's utterances (both during this phase of the proceedings and during the next when he was asked to provide a breath sample) were compelled rather than voluntary. 377 Pa. Super., at 390, <span class="citation" data-id="9697733"><a href="/opinion/1931990/commonwealth-v-muniz/#423" aria-description="Citation for case: Commonwealth v. Muniz">547 A. 2d, at 423</a></span>. The court did not explain how it reached this conclusion, nor did it cite <i><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis</a></span></i> or any other case defining custodial interrogation.</p>
<p>[19]  Muniz does not and cannot challenge the introduction into evidence of his refusal to submit to the breathalyzer test. In <i>South Dakota</i> v. <i>Neville,</i> <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553</a></span> (1983), we held that since submission to a blood test could itself be compelled, see <i>Schmerber</i> v. <i>California,</i> <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">384 U. S. 757</a></span> (1966), a State's decision to permit a suspect to refuse to take the test but then to comment upon that refusal at trial did not "compel" the suspect to incriminate himself and hence did not violate the privilege. <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#562" aria-description="Citation for case: South Dakota v. Neville"><i>Neville, supra,</i> at 562-564</a></span>. We see no reason to distinguish between chemical blood tests and breathalyzer tests for these purposes. Cf. <span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#765" aria-description="Citation for case: Schmerber v. California"><i>Schmerber, supra,</i> at 765-766, n. 9</a></span>.</p>
<p>[20]  We noted in <i><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/" aria-description="Citation for case: Schmerber v. California">Schmerber</a></span></i> that "there may be circumstances in which the pain, danger, or severity of an operation [or other test seeking physical evidence] would almost inevitably cause a person to prefer confession to undergoing the `search,' " 384 U. S., at 765, n. 9, and in such cases "[i]f it wishes to compel persons to submit to such attempts to discover evidence, the State may have to forgo the advantage of any <i>testimonial</i> products of administering the test." <i>Ibid.</i> See also <span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/#563" aria-description="Citation for case: South Dakota v. Neville"><i>Neville, supra,</i> at 563</a></span> ("Fifth Amendment may bar the use of testimony obtained when the proffered alternative was to submit to a test so painful, dangerous, or severe, or so violative of religious beliefs, that almost inevitably a person would prefer `confession' "). But Muniz claims no such extraordinary circumstance here.</p>
<p>[21]  See n. 18, <i>supra.</i></p>
<p>[22]  The parties have not asked us to decide whether any error in this case was harmless. The state court is free, of course, to consider this question upon remand.</p>
<p>[1]  The sixth birthday question also clearly constituted custodial interrogation because it was a form of "express questioning." <i>Rhode Island</i> v. <i>Innis,</i> <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#300" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 300-301</a></span> (1980). Furthermore, that question would not fall within JUSTICE BRENNAN's proposed routine booking question exception. The question serves no apparent recordkeeping need, as the police already possessed Muniz's date of birth. The absence of any administrative need for the question, moreover, suggests that the question was designed to obtain an incriminating response. Regardless of any administrative need for the question and regardless of the officer's intent, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were required because the police should have known that the question was reasonably likely to elicit an incriminating response. <i>Supra,</i> at 610-611.</p>
<p>[2]  An additional factor strongly suggests that the police expected Muniz to make incriminating statements. Pursuant to their routine in such cases, App. 28-29, the police allotted 20 minutes for the three sobriety tests and for "observation." Because Muniz finished the tests in approximately 6 minutes, the police required him to wait another 14 minutes before they asked him to submit to the breathalyzer examination. Given the absence of any apparent technical or administrative reason for the delay and the stated purpose of "observing" Muniz, the delay appears to have been designed in part to give Muniz the opportunity to make incriminating statements.</p>
<p>[3]  The Commonwealth could not use Muniz's failure to count against him regardless of whether his silence during the walk and turn test was itself testimonial in those circumstances. Cf. <i>ante,</i> at 603, n. 17. A defendant's silence in response to police questioning is not admissible at trial even if the silence is not, in the particular circumstances, a form of communicative conduct. <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#468" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 468, n. 37</a></span> (1966) ("[I]t is impermissible to penalize an individual for exercising his Fifth Amendment privilege when he is under police custodial interrogation. The prosecution may not, therefore, use at trial the fact that he stood mute or claimed his privilege in the face of accusation"). Cf. <i>Griffin</i> v. <i>California,</i> <span class="citation" data-id="6751630"><a href="/opinion/6862140/griffin-v-california/#615" aria-description="Citation for case: Griffin v. California">380 U. S. 609, 615</a></span> (1965) ("[T]he Fifth Amendment . . . forbids either comment by the prosecution on the accused's silence or instructions by the court that such silence is evidence of guilt").</p>
<p>[4]  I continue to have serious reservations about the Court's limitation of the Fifth Amendment privilege to "testimonial" evidence. See <i>United States</i> v. <i>Mara,</i> <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#32" aria-description="Citation for case: United States v. Mara">410 U. S. 19, 32-38</a></span> (1973) (MARSHALL, J., dissenting). I believe that privilege extends to <i>any</i> evidence that a person is compelled to furnish against himself. <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#33" aria-description="Citation for case: United States v. Mara"><i>Id.,</i> at 33-35</a></span>. At the very least, the privilege includes evidence that can be obtained only through the person's affirmative cooperation. <span class="citation" data-id="9425147"><a href="/opinion/108710/united-states-v-mara/#36" aria-description="Citation for case: United States v. Mara"><i>Id.,</i> at 36-37</a></span>. Of course, a person's refusal to incriminate himself also cannot be used against him. See n. 3, <i>supra.</i> Muniz's performance of the sobriety tests and his refusal to take the breathalyzer examination are thus protected by the Fifth Amendment under this interpretation. But cf. <i>ante,</i> at 604-605, n. 19. Because Muniz does not challenge the admission of the video portion of the videotape showing the sobriety tests or of his refusal to take the breathalyzer examination, however, those issues are not before this Court.</p>

</div>
```

---

## GROUP: content/cases/People v. Frederick.md  (`case`, 5 assertions)

### content_page

```
---
title: People v. Frederick
type: case
citation: "500 Mich. 228 (2017)"
parallel_cite: ""
neutral_cite: ""
court: Mich.
court_level: state
circuit: ""
year: 2017
date_decided: 2017-06-01
docket: 153115
authority_weight: "Persuasive — state, illustrative"
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
  opinion_url: "https://www.courtlistener.com/opinion/4396951/people-of-michigan-v-michael-christopher-frederick/"
  cluster_id: 4396951
  opinion_id: null
  identity_checked: false
lake:
  record_id: People v. Frederick
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Knock and Talk]]"
    role: Key
related:
  - "[[Knock and Talk]]"
  - "[[Florida v. Jardines]]"
tags:
  - case
  - fourth-amendment
  - knock-and-talk
  - curtilage
  - implied-license
  - jardines
  - trespass
  - michigan-supreme-court
holding: "The implied license that lets an officer approach a home and knock is time-sensitive and generally does not extend to predawn approaches; when officers conducted 4:00 and 5:30 a.m. 'knock and talks' at the defendants' homes, they exceeded that license and trespassed on Fourth-Amendment-protected property, and because the trespass was joined to information-gathering it was a search — so the consents that followed had to be analyzed for taint from the illegal search."
aliases:
  - People v. Frederick
  - "People v. Frederick (Mich. 2017)"
  - Michigan v. Frederick
---

# People v. Frederick

*500 Mich. 228 (2017)* (Docket Nos. 153115, 153117) · Michigan Supreme Court · **Persuasive — state, illustrative** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4396951 → unanimous opinion 4174204 (McCormack, J.; 500 Mich. 228, decided June 1, 2017). Citation recovered dual-leg (vLex + Justia), source web-dual-leg — CL cluster carries no citations[]. Rule quote string-matched to the CL opinion text 2026-07-07; slip-style pin (CL text carries the Michigan syllabus/opinion, not the 500 Mich. star pages) — S9 verifies the reporter pincite. -->

## Background
Seven officers of the Kent Area Narcotics Enforcement Team made unscheduled predawn visits to the homes of Michael Frederick and Todd Van Doorne on March 18, 2014, knocking on Frederick's door around 4:00 a.m. and Van Doorne's around 5:30 a.m. to question them about suspected marijuana butter. Each defendant, awakened with his family, consented to a search; marijuana products were recovered. The trial court denied suppression, reasoning that the predawn knocks were not a search and the consents were valid. A divided Court of Appeals affirmed.

## Issue
Whether a predawn "knock and talk" at a home exceeds the scope of the implied license to approach and knock, so that the officers' conduct is a Fourth Amendment search.

## Rule
The scope of a [[Knock and Talk|knock-and-talk]] is bounded by the implied license extended to any private citizen, which is time-sensitive; a private citizen would not be welcome to knock at 4:00 a.m., so officers who do so stray beyond the license and trespass on constitutionally protected [[Curtilage|curtilage]]. The court held: "The scope of the implied license to approach a house and knock is time-sensitive; it generally does not extend to predawn approaches. While approaching a home with the purpose of gathering information is not, standing alone, a Fourth Amendment search, when information-gathering is conjoined with a trespass, a Fourth Amendment search has occurred." — slip op. at 1. ^pin-slip1

## Application
Because the officers approached the homes during predawn hours — outside the hours at which a homeowner would expect an uninvited visitor — they exceeded the implied license and trespassed on Fourth-Amendment-protected property. Since the trespass was joined to their purpose of gathering information, each was a search under *[[Florida v. Jardines]]*. The court did not decide the ultimate suppression question; it [[Reading and Citing Cases#on-remand|remanded]] for the trial court to determine whether the defendants' consent was attenuated from the illegal searches.

## Conclusion
**Reversed and [[Reading and Citing Cases#on-remand|remanded]]** for the trial court to determine whether the consents were attenuated from the officers' illegal searches. Justice McCormack wrote for a unanimous court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Frederick* is a widely taught state-court application of *[[Florida v. Jardines|Jardines]]*: the implied license to knock has temporal limits, and a predawn approach converts a [[Knock and Talk|knock-and-talk]] into a trespassory search. It is persuasive, illustrative authority (Michigan Supreme Court) for the federal *[[Knock and Talk|knock-and-talk]]* doctrine, not binding federal precedent.

## Appears on
- [[Knock and Talk]] — *Key*

## Sources
- [*People v. Frederick*, 500 Mich. 228 (2017)](https://www.courtlistener.com/opinion/4396951/people-of-michigan-v-michael-christopher-frederick/) — pinpoint: slip op. at 1 (predawn approach exceeds the implied license; trespass-plus-information-gathering is a search). Rule quote string-matched to the CL opinion text 2026-07-07. Official cite 500 Mich. 228 (parallel 895 N.W.2d 541) recovered via two independent sources (vLex, Justia); the CL cluster carries no citations[].

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f4a0dff2ce2f0f12", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "500 Mich. 228 (2017)", "court": "Mich.", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "People v. Frederick", "year": "2017"}}
{"assertion_id": "27530e1ae30a9944", "dimension": "support", "kind": "home_role", "locator": {"home": "Knock and Talk"}, "payload": {"home": "Knock and Talk", "role": "Key", "title": "People v. Frederick"}}
{"assertion_id": "86335ac4c24d7712", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The implied license that lets an officer approach a home and knock is time-sensitive and generally does not extend to predawn approaches; when officers conducted 4:00 and 5:30 a.m. 'knock and talks' at the defendants' homes, they exceeded that license and trespassed on Fourth-Amendment-protected property, and because the trespass was joined to information-gathering it was a search — so the consents that followed had to be analyzed for taint from the illegal search.", "title": "People v. Frederick"}}
{"assertion_id": "0155c71f4a21b29d", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "People v. Frederick", "varies_by_point": "false"}}
{"assertion_id": "3c99596ebaa98d6f", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Persuasive — state, illustrative", "title": "People v. Frederick"}}
```

### lake record — People v. Frederick

```json
{
  "schema_version": "s2.v1",
  "record_id": "People v. Frederick",
  "status": "under_review",
  "identity": {
    "case_name": "People of Michigan v. Michael Christopher Frederick",
    "case_name_short": "",
    "case_name_full": "",
    "input_case_name": "People v. Frederick",
    "court": "Mich.",
    "court_id": null,
    "court_level": "state",
    "circuit": null,
    "state": "Michigan",
    "date_decided": "2017-06-01",
    "year": 2017,
    "docket": "153115",
    "cluster_id": 4396951,
    "lead_opinion_id": 4174204,
    "sibling_ids": [],
    "absolute_url": "/opinion/4396951/people-of-michigan-v-michael-christopher-frederick/",
    "identity_method": "frontier-identity",
    "expected_citation_found": false,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 4246807,
        "score": 90,
        "case_name": "People of Michigan v. Michael Christopher Frederick"
      },
      {
        "cluster_id": 4246793,
        "score": 90,
        "case_name": "People of Michigan v. Michael Christopher Frederick"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "500 Mich. 228",
      "volume": "500",
      "reporter": "Mich.",
      "page": "228",
      "type": 1,
      "selected_official": true,
      "source": "web-dual-leg"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "500 Mich. 228",
        "volume": "500",
        "reporter": "Mich.",
        "page": "228",
        "type": 1,
        "selected_official": true,
        "source": "web-dual-leg"
      }
    ],
    "display": "500 Mich. 228",
    "official_selection": {
      "court_class": "state",
      "selected": "500 Mich. 228",
      "reason": "web-dual-leg"
    },
    "web_legs": [
      {
        "source": "vLex",
        "url": "https://case-law.vlex.com/vid/people-v-frederick-no-885598045",
        "cite": "500 Mich. 228",
        "checked_date": "2026-07-07"
      },
      {
        "source": "Justia",
        "url": "https://law.justia.com/cases/michigan/supreme-court/2017/153115.html",
        "cite": "500 Mich. 228",
        "checked_date": "2026-07-07"
      }
    ]
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
    "date_created": "2026-07-07T18:21:34Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T18:23:04Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "people-v-frederick--4396951",
      "to_record_id": "People v. Frederick",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — People v. Frederick

```
                                                                                     Michigan Supreme Court
                                                                                           Lansing, Michigan




Syllabus
                                                                Chief Justice:       Justices:
                                                                Stephen J. Markman   Brian K. Zahra
                                                                                     Bridget M. McCormack
                                                                                     David F. Viviano
                                                                                     Richard H. Bernstein
                                                                                     Joan L. Larsen
                                                                                     Kurtis T. Wilder
This syllabus constitutes no part of the opinion of the Court but has been           Reporter of Decisions:
prepared by the Reporter of Decisions for the convenience of the reader.             Kathryn L. Loomis



                                            PEOPLE v FREDERICK
                                           PEOPLE v VAN DOORNE

             Docket Nos. 153115 and 153117. Argued on application for leave to appeal March 9,
       2017. Decided June 1, 2017.

               Michael Frederick and Todd Van Doorne were separately charged in the Kent Circuit
       Court with various drug offenses after seven officers from the Kent Area Narcotics Enforcement
       Team made unscheduled visits to the defendants’ respective homes during the predawn hours on
       March 18, 2014. Officers knocked on Frederick’s door around 4:00 a.m. and on Van Doorne’s
       door around 5:30 a.m. Officers woke defendants and their families for the purpose of
       questioning each defendant about marijuana butter that they suspected the defendants possessed.
       Both defendants subsequently consented to a search of their respective homes, and marijuana
       butter and other marijuana products were recovered from each home. Defendants moved to
       suppress the evidence, and the court, Dennis B. Leiber, J., denied both motions, concluding that
       the officers had not conducted a search by knocking on defendants’ doors during the predawn
       hours and that the subsequent consent searches were valid. Defendants sought interlocutory
       leave to appeal, which the Court of Appeals denied in separate unpublished orders, entered
       October 15, 2014 (Docket Nos. 323642 and 323643). Defendants sought leave to appeal in the
       Supreme Court. The Supreme Court, in lieu of granting leave to appeal, remanded the cases to
       the Court of Appeals for consideration as on leave granted and directed the Court of Appeals to
       address whether the “knock and talk” procedure conducted in these cases was consistent with the
       Fourth Amendment as articulated in Florida v Jardines, 569 US ___; 133 S Ct 1409 (2013).
       People v Frederick, 497 Mich 993 (2015); People v Van Doorne, 497 Mich 993 (2015). The
       Court of Appeals consolidated the two cases and issued a split opinion. 313 Mich App 457
       (2015). The majority concluded that the officers’ predawn “knock and talk” visits were within
       the scope of the public’s implied license because homeowners would be unsurprised to find a
       predawn visitor delivering a newspaper or seeking emergency assistance, but the dissenting
       judge concluded that the police conduct violated the Fourth Amendment because the searches,
       which occurred during hours at which a homeowner would not expect visitors, were outside the
       scope of a proper knock and talk procedure. Defendants sought leave to appeal, and the Supreme
       Court ordered and heard oral argument on whether to grant the application or take other action.
       499 Mich 952 (2016).

             In a unanimous opinion by Justice MCCORMACK, in lieu of granting leave to appeal, the
       Supreme Court held:
        The scope of the implied license to approach a house and knock is time-sensitive; it
generally does not extend to predawn approaches. While approaching a home with the purpose
of gathering information is not, standing alone, a Fourth Amendment search, when information-
gathering is conjoined with a trespass, a Fourth Amendment search has occurred. In these cases,
the police conduct exceeded the scope of the implied license to knock and talk because the
officers approached the defendants’ respective homes during the predawn hours; therefore, the
officers trespassed on Fourth-Amendment-protected property. And because the officers
trespassed while seeking information, they performed searches in violation of the Fourth
Amendment.

        1. The proper scope of a knock and talk is determined by the implied license that is
granted to the general public. Therefore, a police officer not armed with a warrant may approach
a home and knock precisely because that is no more than any private citizen might do. When
police officers stray beyond what any private citizen might do, they have strayed beyond the
bounds of a permissible knock and talk; in other words, the officers are trespassing. Just as there
is no implied license to bring a drug-sniffing dog to someone’s front porch, there is generally no
implied license to knock at someone’s door in the middle of the night. Background social norms
that invite a visitor to the front door typically do not extend to a visit in the middle of the night.
Accordingly, the scope of the implied license to approach a house and knock is time-sensitive; it
generally does not extend to predawn approaches. Additionally, while approaching a home with
the purpose of gathering information is not, standing alone, a Fourth Amendment search, when
information-gathering is conjoined with a trespass, a Fourth Amendment search has occurred. In
these cases, the police officers exceeded the scope of the implied license to knock and talk
because the officers approached defendants’ respective homes without warrants during the
predawn hours; therefore, the officers trespassed on Fourth-Amendment-protected property.
And because the officers trespassed while seeking information about defendants’ alleged
possession of marijuana butter, they performed searches in violation of the Fourth Amendment.

        2. Consent searches, when voluntary, are an exception to the warrant requirement. The
voluntariness question turns on whether a reasonable person would, under the totality of the
circumstances, feel able to choose whether to consent. Evidence obtained through an illegal
search or seizure is tainted by that initial illegality unless sufficiently attenuated from it. Thus,
even when consent is voluntary, if it is not attenuated from the unconstitutional search, the
evidence must be suppressed. Three factors are considered in determining whether consent is
sufficiently attenuated: (1) the temporal proximity of the illegal act and the alleged consent, (2)
the presence of intervening circumstances, and (3) the purpose and flagrancy of the official
misconduct. In these cases, because the trial court determined that there was no Fourth
Amendment violation, it did not consider whether the subsequent consent was attenuated from
the illegality. Therefore, the cases had to be remanded to the trial court for consideration of that
question in the first instance.

       Reversed and remanded to the Kent Circuit Court to determine whether defendants’
consent to search was attenuated from the officers’ illegal search.



                                     ©2017 State of Michigan
                                                                 Michigan Supreme Court
                                                                       Lansing, Michigan




OPINION
                                          Chief Justice:           Justices:
                                          Stephen J. Markman       Brian K. Zahra
                                                                   Bridget M. McCormack
                                                                   David F. Viviano
                                                                   Richard H. Bernstein
                                                                   Joan L. Larsen
                                                                   Kurtis T. Wilder

                                                           FILED June 1, 2017




                        STATE OF MICHIGAN

                               SUPREME COURT


PEOPLE OF THE STATE OF MICHIGAN,

         Plaintiff-Appellee,

v                                                   No. 153115

MICHAEL CHRISTOPHER FREDERICK,

         Defendant-Appellant.



PEOPLE OF THE STATE OF MICHIGAN,

         Plaintiff-Appellee,

v                                                   No. 153117

TODD RANDOLPH VAN DOORNE,

         Defendant-Appellant.


BEFORE THE ENTIRE BENCH
MCCORMACK, J.
       In these consolidated cases, we consider the constitutionality of two early morning

searches of the defendants’ homes. We conclude that the police conduct in both cases

was unconstitutional; these were not permissible “knock and talks,” but rather warrantless

searches. Because of these illegal searches, the defendants’ consent to search—even if

voluntary—is invalid unless it is sufficiently attenuated from the illegality. Accordingly,

we reverse the Court of Appeals’ contrary determination and remand these cases to the

Kent Circuit Court for further proceedings.

                      I. FACTS AND PROCEDURAL HISTORY

       During the predawn hours on March 18, 2014, seven officers from the Kent Area

Narcotics Enforcement Team (KANET) made unscheduled visits to the defendants’

homes. Both defendants were employees of the corrections division of the Kent County

Sheriff Department. Their names had come up in a criminal investigation, and KANET

decided to perform these early morning visits to the defendants’ homes rather than

waiting until daytime to speak with the defendants (or seeking search warrants). KANET

knocked on defendant Michael Frederick’s door around 4:00 a.m. and on defendant Todd

Van Doorne’s door around 5:30 a.m. Lieutenant Al Roetman, who was present at both

searches, testified that everyone appeared to be asleep at both houses.

       Both defendants and their families were surprised and alarmed by the intrusions.

Van Doorne considered arming himself, as did Frederick’s wife. Nonetheless, both

defendants answered the door after a few minutes of knocking—each thinking that there

must have been some sort of emergency.




                                              2
         Instead, each defendant found himself confronted with a group of police officers.

The officers asked each defendant about marijuana butter that they suspected the

defendants possessed.     After a conversation with each defendant, during which the

defendants were read their Miranda 1 rights, both defendants consented to a search of

their homes and signed a consent form to that effect.        Marijuana butter and other

marijuana products were recovered from each house.

         The defendants were charged with various drug offenses. Both moved to suppress

evidence of the marijuana products found in their homes. The trial court denied both

motions. The court concluded that KANET had not conducted a search by approaching

the home and knocking, and that the subsequent consent search was a valid, voluntary

search. The court distinguished Florida v Jardines, 569 US ___; 133 S Ct 1409; 185 L

Ed 2d 495 (2013), noting that the police here did not use a drug-sniffing dog or otherwise

try to search the home without knocking. Rather, because the police approached the

home and knocked, the trial court held that these were valid knock and talks.

         The defendants sought interlocutory leave to appeal, which the Court of Appeals

denied. The defendants then sought leave to appeal in this Court. In lieu of granting

leave to appeal, we remanded the cases to the Court of Appeals for consideration as on

leave granted. People v Frederick, 497 Mich 993 (2015); People v Van Doorne, 497

Mich 993 (2015). We directed the Court of Appeals to address “whether the ‘knock and

talk’ procedure conducted in [these cases] is consistent with US Const, Am IV, as



1
    Miranda v Arizona, 384 US 436; 86 S Ct 1602; 16 L Ed 2d 694 (1966).



                                             3
articulated in Florida v Jardines . . . .” Frederick, 497 Mich 993; Van Doorne, 497 Mich

993.

       On remand, the Court of Appeals issued a split opinion. The majority concluded

that the knock and talk procedures at issue were permitted by the Fourth Amendment.

People v Frederick, 313 Mich App 457, 461; 886 NW2d 1 (2015).              The majority

emphasized that the officers approached the home, knocked, and waited to be received,

and “Jardines plainly condones such conduct.” Id. at 469. Though the police visits here

occurred during the early morning hours, the majority concluded that they were

nonetheless within the scope of the implied license because homeowners would be

unsurprised to find a predawn visitor delivering a newspaper or seeking emergency

assistance. Id. at 481.

       Judge SERVITTO dissented. She concluded that the police conduct violated the

defendants’ Fourth Amendment rights. Id. at 496 (SERVITTO, J., dissenting). First, Judge

SERVITTO noted that the Jardines majority and dissent had seemed to agree, in dicta, that

nighttime visits would be outside the scope of the implied license. Id. at 487-488.

Further, Judge SERVITTO reasoned that the validity of a knock and talk is premised on

“the implied license a homeowner extends to the public-at-large.” Id. at 496. Because

the hours the police arrived at the defendants’ homes are not times at which most

homeowners expect visitors, she concluded that the visits were outside the scope of a

proper knock and talk. Id.




                                           4
                                     II. ANALYSIS

      In general, a search or seizure within a home or its curtilage without a warrant is

per se an unreasonable search under the Fourth Amendment. People v Champion, 452

Mich 92, 98; 549 NW2d 849 (1996); Katz v United States, 389 US 347, 357; 88 S Ct 507;

19 L Ed 2d 576 (1967). Two arguments have been presented as to why this police

conduct was lawful. First, the prosecution argues that the initial approach was a knock

and talk, not a search. Second, the prosecution argues that the search that followed that

initial approach was a consent search.

                                A. KNOCK AND TALK

      A “knock and talk,” when performed within its proper scope, is not a search at all.

Jardines, 569 US at ___; 133 S Ct at 1415. The proper scope of a knock and talk is

determined by the “implied license” that is granted to “solicitors, hawkers, and peddlers

of all kinds.” Id. at ___; 133 S Ct at 1415 (citation and quotation marks omitted). “Thus,

a police officer not armed with a warrant may approach a home and knock, precisely

because that is ‘no more than any private citizen might do.’ ” Id. at ___; 133 S Ct at

1416, quoting Kentucky v King, 563 US 452, 469; 131 S Ct 1849; 179 L Ed 2d 865

(2011).

      In Jardines, the police approached a house via the front walk with a drug dog.

Jardines, 569 US at ___; 133 S Ct at 1413. The dog alerted, indicating that it smelled

contraband, and eventually sat at the front door of the home, where the odor was

strongest. Id. Using this information, the police obtained a warrant, and their search of

the home revealed marijuana plants. Id.




                                            5
       Justice Scalia, writing for the Court, employed a property-rights framework 2 to

conclude that the prewarrant conduct of the police constituted a search. The Court

distinguished the case from King, in which the Court had held that a knock and talk was

not a search, because the police in Jardines, unlike the police in King, had trespassed;

although the public, and thus the police, generally have an implied license to “approach

the door by the front path, knock promptly, wait briefly to be received, and then (absent

invitation to linger longer) leave,” the police in Jardines had not complied with the scope

of that implied license. Id. at ___; 133 S Ct at 1415-1416. “[I]ntroducing a trained police

dog to explore the area around the home in hopes of discovering incriminating evidence


2
  In Katz v United States, 389 US 347, the Court broke with tradition by considering not
whether the government had trod on the defendant’s property interests, but rather whether
it had violated his privacy interests. Subsequently, the Court clarified that Katz had not
replaced the property-interests test; Katz merely added to it. Alderman v United States,
394 US 165, 180; 89 S Ct 961; 22 L Ed 2d 176 (1969) (“[W]e [do not] believe that Katz,
by holding that the Fourth Amendment protects persons and their private conversations,
was intended to withdraw any of the protection which the Amendment extends to the
home . . . .”).

         The Court reaffirmed the importance of the property-rights analysis in the Fourth
Amendment context in United States v Jones, 565 US 400; 132 S Ct 945; 181 L Ed 2d
911 (2012). In that case, the Court held that the warrantless installation of a GPS
tracking device on the exterior of a Jeep and subsequent tracking of the defendant’s
movements on public roads constituted a search, despite the Court’s earlier holdings that
tracking of a defendant’s movements on public roads was not a search. Id. at 404; cf.
United States v Knotts, 460 US 276; 103 S Ct 1081; 75 L Ed 2d 55 (1983) (holding that
no search occurred when law enforcement tracked on public roads the location of a
beeper that had been installed in a container before the defendant’s possession of the
container). The Jones Court distinguished Knotts on the ground that it did not involve a
trespass. Jones, 565 US at 409-410. The violation of Jones’s property rights, combined
with the subsequent information-gathering, constituted a search. Id. at 407-408. The
Court cautioned that “[t]respass alone does not qualify, but there must be conjoined with
that . . . an attempt to find something or to obtain information.” Id. at 408 n 5.



                                            6
is something else. There is no customary invitation to do that.” Id. at ___; 133 S Ct at

1416. Thus, the police had trespassed on Fourth-Amendment-protected property. 3 Id.

       Consistently with United States v Jones, 565 US 400; 132 S Ct 945; 181 L Ed 2d

911 (2012), the Jardines Court required not only a trespass, but also some attempted

information-gathering, to find that a search had occurred. Jardines, 569 US at ___; 133 S

Ct at 1414; Jones, 565 US at 408 n 5 (“[P]ost-Katz we have explained that an actual

trespass is neither necessary nor sufficient to establish a constitutional violation. . . .

Trespass alone does not qualify [as a search], but there must be conjoined with that . . . an

attempt to find something or to obtain information.”) (citations and quotation marks

omitted).   The Jardines Court concluded that the police conduct there included

information-gathering, such that the behavior constituted a warrantless search of the

curtilage. Jardines, 569 US at ___; 133 S Ct at 1417.

       It is also clear from Jones and Jardines that “information-gathering” is not

synonymous with a Fourth Amendment “search.” Both Jones and Jardines held that

conduct that would not amount to a search, standing alone, was nonetheless information-

gathering. The information-gathering in Jardines was the use of a drug-sniffing dog—

conduct that the Supreme Court of the United States has held is not a search when the

3
   The Jardines Court distinguished between trespasses that implicate the Fourth
Amendment and those that do not. For instance, police may trespass and search in open
fields without violating the Fourth Amendment because “an open field . . . is not one of
those protected areas enumerated in the Fourth Amendment.” Jones, 565 US at 411,
citing Oliver v United States, 466 US 170, 177; 104 S Ct 1735; 80 L Ed 2d 214 (1984).
But because the curtilage is part of the home, Oliver, 466 US at 180, and homes are
protected by the Fourth Amendment, trespassing on the curtilage implicates Fourth
Amendment protections.



                                             7
police have not trespassed. Id. at ___; 133 S Ct at 1414; Illinois v Caballes, 543 US 405,

410; 125 S Ct 834; 160 L Ed 2d 842 (2005) (holding that a dog sniff conducted during a

lawful traffic stop did not implicate legitimate privacy interests). Similarly, in Jones, the

information-gathering was the tracking of the defendant’s location on public streets—

conduct that the Supreme Court has also held is not a search when the police have not

trespassed. Jones, 565 US at 408 n 5; United States v Knotts, 460 US 276, 285; 103 S Ct

1081; 75 L Ed 2d 55 (1983) (holding that a person traveling in an automobile on public

roads has no reasonable expectation of privacy in his or her location). But information-

gathering that is not a search nevertheless becomes a search when it is combined with a

trespass on Fourth-Amendment-protected property. 4

       In Jardines, the majority and dissenting opinions address in dicta one issue that is

particularly relevant here.    In his dissent, Justice Alito noted that, “as a general

matter, . . . a visitor [may not] come to the front door in the middle of the night without

an express invitation.” Jardines, 569 US at ___; 133 S Ct at 1422 (Alito, J., dissenting).

In response, the majority opinion reasoned that the dissent “quite rightly” relied on the

fact that a nighttime knock would be alarming in concluding that nightime visits would

be outside the scope of the implied license. Id. at ___; 133 S Ct at 1416 n 3 (opinion of

the Court) (“We think a typical person would find it a cause for great alarm (the kind of



4
  For example, looking into the windows of a home from a sidewalk or other public area
is not a search. But it is information-gathering, such that, if the police trespass on the
home’s curtilage and peer through the windows from that vantage point, they have
conducted a search. The trespass converts conduct that would not otherwise constitute a
search into a search.



                                             8
reaction the dissent quite rightly relies upon to justify its no-night-visits rule) to find a

stranger snooping about his front porch with or without a dog.”) (citation, quotation

marks, and emphasis omitted). Thus, the Jardines Court apparently agreed, albeit in

dicta, that a nighttime visit would be outside the scope of the implied license (and thus a

trespass).

       We believe, as the Supreme Court suggested in Jardines, that the scope of the

implied license to approach a house and knock is time-sensitive. Id. at ___; 133 S Ct at

1416 n 3; id. at ___; 133 S Ct at 1422 (Alito, J., dissenting). Just as there is no implied

license to bring a drug-sniffing dog to someone’s front porch, there is generally no

implied license to knock at someone’s door in the middle of the night. See id. at ___; 133

S Ct at 1416 (opinion of the Court) (“There is no customary invitation to do that.”). This

custom was apparent to the investigating officers in this case. KANET officers testified

candidly that it would be inappropriate for Girl Scouts or other visitors to knock on the

door in the middle of the night, but evidently the officers believed that they were not

bound by these customs. 5     But a knock and talk is not considered a governmental

intrusion precisely because its contours are defined by what anyone may do. King, 563

US at 469 (“When law enforcement officers who are not armed with a warrant knock on

a door, they do no more than any private citizen might do.”). When the officers stray



5
  In fact, multiple KANET members testified that they performed knock and talks in the
middle of the night on a regular basis. Roetman testified that “[j]ust because it hits the
stroke of midnight doesn’t mean our case stops and we don’t keep going to people’s
homes, whether it’s a marijuana case or an armed robbery. . . . I don’t know what you’re
getting at.”



                                             9
beyond what any private citizen might do, they have strayed beyond the bounds of a

permissible knock and talk; in other words, the officers are trespassing. That is what

happened here. The reasoning that leads us to conclude that these visits were outside the

scope of the implied license is not nuanced or complicated. As the Jardines Court aptly

explained, Girl Scouts and trick-or-treaters regularly manage to abide by the terms of the

implied license. See Jardines, 569 US at ___; 133 S Ct at 1415 (“Complying with the

terms of that traditional invitation does not require fine-grained legal knowledge; it is

generally managed without incident by the Nation’s Girl Scouts and trick-or-treaters.”).

And, as any Girl Scout knows, the “background social norms that invite a visitor to the

front door,” id. at ___; 133 S Ct at 1416, typically do not extend to a visit in the middle of

the night. See United States v Lundin, 817 F3d 1151, 1159 (CA 9, 2016) (“[U]nexpected

visitors are customarily expected to knock on the front door of a home only during

normal waking hours.”). Thus, we hold that the police were trespassing when they

approached the defendants’ homes. 6

       The Court of Appeals majority reasoned that the implied license extended to

midnight visitors seeking emergency assistance or delivering the newspaper and therefore

it extended, too, to the police conduct here.         We find these examples unhelpful.

Newspaper delivery services have express permission to be on the property; therefore,



6
  We need not decide precisely what time the implied license to approach begins and
ends. In these cases, there were no circumstances that would lead a reasonable member
of the public to believe that the occupants of the respective homes welcomed visitors at
4:00 a.m. or 5:30 a.m. Accordingly, we believe it is clear that these approaches were
outside the scope of the implied license.



                                             10
their conduct is irrelevant when considering the implied license to approach a house. 7

And the fact that a visitor may approach a home in an emergency does not mean that a

visitor who is not in an emergency may approach. Emergencies justify conduct that

would otherwise be unacceptable; they are exceptions to the rule, not the rule. 8 Because

we conclude that the implied scope of the license does not extend to these predawn

approaches, we hold that the police were trespassing.

       Having concluded that the police conduct was a trespass on Fourth-Amendment-

protected property, we next turn to whether the police were seeking “to find something or

to obtain information,” such that the Fourth Amendment is implicated. Jones, 565 US at

408 n 5. A police officer walking through a neighborhood who takes a shortcut across

the corner of a homeowner’s lawn has trespassed. Yet that officer has not violated the

Fourth Amendment because, without some information-gathering, no search has

occurred. In these cases, however, the police were seeking information; therefore, their

conduct implicated the Fourth Amendment.         The KANET officers were not simply

cutting across the defendants’ lawns as a shortcut, stopping by to drop off a get-well-soon

basket, or visiting the homes to regretfully inform the defendants that a loved one had



7
  Moreover, most newspaper delivery services have permission to leave newspapers on
the property, not to approach the house and knock. Most homeowners would be
surprised—and likely indignant—if their newspaper delivery person rang the bell and
knocked for several minutes at 5:00 a.m. rather than simply leaving the paper.
8
  See Ploof v Putnam, 81 Vt 471; 71 A 188, 189 (1908) (“It is clear that an entry upon the
land of another may be justified by necessity . . . .”); Vincent v Lake Erie Transp Co, 109
Minn 456, 460; 124 NW 221 (1910) (holding that trespass onto the property of another
may be justified by necessity).



                                            11
been injured in an accident. The officers approached each house to obtain information

about the marijuana butter they suspected each defendant possessed.         This intent is

sufficient to satisfy the information-gathering prong of the Jones test.

       That the officers intended to get permission to search for the marijuana butter does

not alter our analysis. We agree with the prosecution that, as King established and

Jardines affirmed, “it is not a Fourth Amendment search to approach the home in order to

speak with the occupant, because all are invited to do that.         The mere purpose of

gathering information in the course of engaging in that permitted conduct does not cause

it to violate the Fourth Amendment.” Jardines, 569 US at ___; 133 S Ct at 1416 n 4

(citations, quotation marks, and emphasis omitted), citing King, 563 US at 469-470. True

enough; approaching a home with the purpose of gathering information is not, standing

alone, a Fourth Amendment search. King, 563 US at 469-470. But, as noted above,

when “conjoined” with a trespass, information-gathering—which need not qualify as a

search, standing alone—is all that is required to turn the trespass into a Fourth

Amendment search. Jones, 565 US at 408 n 5. The officers here plainly approached the

defendants’ homes for the purpose of gathering information. 9

       The fact that the officers sought to gather their information by speaking with the

homeowners rather than by peering through windows or rummaging through the bushes

is irrelevant. What matters is that they sought to gather information by way of a trespass

on Fourth-Amendment-protected property.           That they did.   The approaches of the


9
  Detective Todd Butler, one of the KANET members who participated in the knock and
talk, testified that “[t]he only reason we were there is because of the drugs.”



                                             12
defendants’ homes were not valid knock and talks, but rather searches under the Fourth

Amendment. And because the police did not have warrants or any other exception to the

warrant requirement, we conclude that the approaches violated the Fourth Amendment.

                                      B. CONSENT

       This is not the end of the analysis, however. During the invalid knock and talks,

each defendant consented to a search of his respective home. Consent searches, when

voluntary, are an exception to the warrant requirement. Schneckloth v Bustamonte, 412

US 218, 219; 93 S Ct 2041; 36 L Ed 2d 854 (1973). The voluntariness question turns on

whether a reasonable person would, under the totality of the circumstances, feel able to

choose whether to consent. Id. at 227.

       The defendants believe that their consent, even if voluntary, is irrelevant, given the

contemporaneous Fourth Amendment violation.           The prosecution views the Fourth

Amendment violation as irrelevant, given the subsequent consent. Neither is correct.

The defendants’ consent is not irrelevant—but neither is it evaluated separately from the

illegal searches.

       Rather, the defendants’ consent—even if voluntary—is invalid unless it is

sufficiently attenuated from the warrantless search. The Supreme Court has repeatedly

held that evidence obtained through an illegal search or seizure is tainted by that initial

illegality unless sufficiently attenuated from it. See Wong Sun v United States, 371 US

471, 486; 83 S Ct 407; 9 L Ed 2d 441 (1963) (holding that evidence acquired after an

illegal search must be suppressed unless the government shows that its acquisition of the

evidence resulted from “an intervening independent act of free will” sufficient “to purge




                                             13
the primary taint of the unlawful invasion”). That analysis has been applied to both

consensual statements and—particularly relevant here—consensual searches. Brown v

Illinois, 422 US 590, 602; 95 S Ct 2254; 45 L Ed 2d 416 (1975) (holding that when an

inculpatory statement follows an unlawful arrest, a finding of voluntariness does not

obviate the need to make a separate Fourth Amendment determination as to whether the

statement was “ ‘sufficiently an act of free will to purge the primary taint’ ”), quoting

Wong Sun, 371 US at 486; Florida v Royer, 460 US 491, 507-508; 103 S Ct 1319; 75 L

Ed 2d 229 (1983) (“Because we affirm the . . . conclusion that Royer was being illegally

detained when he consented to the search of his luggage, we agree that the consent was

tainted by the illegality and was ineffective to justify the search.”).

       Thus, even when consent is voluntary, if it is not attenuated from the

unconstitutional search, the evidence must be suppressed. Wong Sun, 371 US at 486;

Brown, 422 US at 602; Royer, 460 US at 507-508. The Supreme Court has identified

three factors to be considered in determining whether consent is sufficiently attenuated:

(1) the temporal proximity of the illegal act and the alleged consent, (2) the presence of

intervening circumstances, and (3) the purpose and flagrancy of the official misconduct.

Brown, 422 US at 603-604.

       In these cases, because the trial court determined that there was no Fourth

Amendment violation, it did not consider whether the subsequent consent was attenuated

from the illegality. Therefore, we remand to that court for consideration of that question

in the first instance.




                                              14
                                   III. CONCLUSION

       A proper application of Fourth Amendment jurisprudence requires us to reverse

the Court of Appeals. Because these knock and talks were outside the scope of the

implied license, the officers trespassed on Fourth-Amendment-protected property. And

because the officers trespassed while seeking information, they performed illegal

searches. Finally, because of these illegal searches, the defendants’ consent—even if

voluntary—is nonetheless invalid unless it was sufficiently attenuated from the illegality.

We therefore reverse the Court of Appeals and remand these cases to the Kent Circuit

Court to determine whether the defendants’ consent to search was attenuated from the

officers’ illegal search.


                                                       Bridget M. McCormack
                                                       Stephen J. Markman
                                                       Brian K. Zahra
                                                       David F. Viviano
                                                       Richard H. Bernstein
                                                       Joan L. Larsen
                                                       Kurtis T. Wilder




                                            15

```

---

## GROUP: content/cases/Perry v. New Hampshire.md  (`case`, 5 assertions)

### content_page

```
---
title: "Perry v. New Hampshire"
type: case
citation: ""
parallel_cite: "181 L. Ed. 2d 694; 132 S. Ct. 716; 565 U.S. 228; 23 Fla. L. Weekly Fed. S 60; 80 U.S.L.W. 4073"
neutral_cite: "2012 U.S. LEXIS 579; 2012 WL 75048"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-01-11
docket: 10-8974
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-01-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Perry v. New Hampshire
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/7350294/perry-v-new-hampshire/"
  cluster_id: 7350294
  opinion_id: 7268276
  identity_checked: true
homes:
  - page: "[[Eyewitness Identification]]"
    role: "Key — Progeny / Refinement"
related: ["[[Manson v. Brathwaite]]", "[[Neil v. Biggers]]", "[[United States v. Wade]]", "[[Gilbert v. California]]"]
aliases: []
tags: ["case", "due-process", "eyewitness-identification", "suggestive-identification", "reliability"]
holding: "The Due Process Clause requires a preliminary judicial screening of eyewitness-identification reliability ONLY when the suggestive…"
lake:
  record_id: Perry v. New Hampshire
  status: verified
  projected_at: 2026-07-06
---

# Perry v. New Hampshire

*565 U.S. 228 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Around 3 a.m., police responding to a report of a man breaking into cars took a description from a witness, Nubia Blandon, who — pointing out her apartment window — identified Perry, who was then standing in the parking lot beside an officer. The witness later could not pick Perry out of a photo array. Perry moved to suppress the identification as the product of unnecessarily suggestive circumstances, even though the police had not orchestrated the showup-like confrontation.

## Issue
Whether the Due Process Clause requires a preliminary judicial assessment of an eyewitness identification's reliability when the suggestive circumstances were not arranged by law enforcement.

## Rule
No. Pretrial reliability screening applies only to police-arranged suggestion. "We have not extended pretrial screening for reliability to cases in which the suggestive circumstances were not arranged by law enforcement officers. . . . When no improper law enforcement activity is involved, we hold, it suffices to test reliability through the rights and opportunities generally designed for that purpose, notably, the presence of counsel at postindictment lineups, vigorous cross-examination, protective rules of evidence, and jury instructions on both the fallibility of eyewitness identification and the requirement that guilt be proved beyond a reasonable doubt." — 565 U.S. 228 (slip op., at 2). ^pin-op2

"[T]he Due Process Clause does not require a preliminary judicial inquiry into the reliability of an eyewitness identification when the identification was not procured under unnecessarily suggestive circumstances arranged by law enforcement." — *Id.* (slip op., at 18–19). ^pin-op18

## Application
The suggestive circumstance here — the witness spontaneously pointing out her window to Perry as he stood beside an officer — was not arranged by the police; an officer had merely asked her for a description. Because there was no improper police arrangement, no preliminary judicial reliability screening was required, and admitting the identification did not render Perry's trial fundamentally unfair; its reliability was for the jury to weigh after cross-examination and instructions.

## Conclusion
Absent police-arranged suggestion, due process requires no pretrial reliability screening of an eyewitness identification; the New Hampshire Supreme Court's judgment was affirmed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**. *Perry* fixes the threshold for the [[Neil v. Biggers]]/[[Manson v. Brathwaite]] reliability inquiry at improper police arrangement.

## Appears on
- [[Eyewitness Identification]] — *Key — Progeny / Refinement*

## Sources
- *Perry v. New Hampshire*, 565 U.S. 228 (2012) — https://www.courtlistener.com/opinion/620671/perry-v-new-hampshire/ — pinpoints: slip op., at 2, 18–19 (CL carries the slip opinion).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e210bea4a99dd940", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2012 U.S. LEXIS 579; 2012 WL 75048", "official_citation_present": false, "parallel_cite": "181 L. Ed. 2d 694; 132 S. Ct. 716; 565 U.S. 228; 23 Fla. L. Weekly Fed. S 60; 80 U.S.L.W. 4073", "title": "Perry v. New Hampshire", "year": "2012"}}
{"assertion_id": "9bc8346e60d45e14", "dimension": "support", "kind": "home_role", "locator": {"home": "Eyewitness Identification"}, "payload": {"home": "Eyewitness Identification", "role": "Key — Progeny / Refinement", "title": "Perry v. New Hampshire"}}
{"assertion_id": "e0b6617a7d3199f9", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Due Process Clause requires a preliminary judicial screening of eyewitness-identification reliability ONLY when the suggestive…", "title": "Perry v. New Hampshire"}}
{"assertion_id": "9f8d5d98b2374b0e", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Perry v. New Hampshire"}}
{"assertion_id": "f61df15c6347f53f", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2012-01-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Perry v. New Hampshire", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Perry v. New Hampshire", "varies_by_point": "false"}}
```

### lake record — Perry v. New Hampshire

```json
{
  "schema_version": "s2.v1",
  "record_id": "Perry v. New Hampshire",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Perry v. New Hampshire",
    "case_name_short": "Perry",
    "case_name_full": "BARION PERRY v. NEW HAMPSHIRE",
    "input_case_name": "Perry v. New Hampshire",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-01-11",
    "year": 2012,
    "docket": "10-8974",
    "cluster_id": 7350294,
    "lead_opinion_id": 7268276,
    "sibling_ids": [
      7268276,
      7268277,
      7268278
    ],
    "absolute_url": "/opinion/7350294/perry-v-new-hampshire/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 620671,
        "score": 120,
        "case_name": "Perry v. New Hampshire"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "181 L. Ed. 2d 694",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 S. Ct. 716",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 228",
        "volume": "565",
        "reporter": "U.S.",
        "page": "228",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 Fla. L. Weekly Fed. S 60",
        "volume": "23",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 U.S.L.W. 4073",
        "volume": "80",
        "reporter": "U.S.L.W.",
        "page": "4073",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 579",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 75048",
        "volume": "2012",
        "reporter": "WL",
        "page": "75048",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "181 L. Ed. 2d 694",
        "volume": "181",
        "reporter": "L. Ed. 2d",
        "page": "694",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 579",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "579",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "132 S. Ct. 716",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "716",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 228",
        "volume": "565",
        "reporter": "U.S.",
        "page": "228",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "23 Fla. L. Weekly Fed. S 60",
        "volume": "23",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "60",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 U.S.L.W. 4073",
        "volume": "80",
        "reporter": "U.S.L.W.",
        "page": "4073",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 WL 75048",
        "volume": "2012",
        "reporter": "WL",
        "page": "75048",
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
      "id": "pin-op2",
      "page": null,
      "quote": "--- # Perry v. New Hampshire *565 U.S. 228 (2012)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Around 3 a.m., police responding to a report of a man breaking into cars took a description from a witness, Nubia Blandon, who \u2014 pointing out her apartment window \u2014 identified Perry, who was then standing in the parking lot beside an officer. The witness later could not pick Perry out of a photo array. Perry moved to suppress the identification as the product of unnecessarily suggestive circumstances, even though the police had not orchestrated the showup-like confrontation. ## Issue Whether the Due Process Clause requires a preliminary judicial assessment of an eyewitness identification's reliability when the suggestive circumstances were not arranged by law enforcement. ## Rule No. Pretrial reliability screening applies only to police-arranged suggestion.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-op18",
      "page": null,
      "quote": "[T]he Due Process Clause does not require a preliminary judicial inquiry into the reliability of an eyewitness identification when the identification was not procured under unnecessarily suggestive circumstances arranged by law enforcement.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-01-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Perry v. New Hampshire",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Dickson",
          "cluster_id": 4244499,
          "cite": [
            "141 A.3d 810",
            "322 Conn. 410",
            "2016 Conn. LEXIS 236"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Shepard-Fraser",
          "cluster_id": 2795991,
          "cite": [
            "784 F.3d 11",
            "97 Fed. R. Serv. 306",
            "2015 U.S. App. LEXIS 6692"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Newman",
          "cluster_id": 2791286,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Balderas v. State",
          "cluster_id": 5448260,
          "cite": [
            "517 S.W.3d 756",
            "2016 WL 6496715",
            "2016 Tex. Crim. App. LEXIS 1329"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Martinez",
          "cluster_id": 9998900,
          "cite": [
            "478 P.3d 880",
            "2021 NMSC 002"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Douglas Stewart v. O'Bell \"Tom\" Winn",
          "cluster_id": 4770981,
          "cite": [
            "967 F.3d 534"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Arizona v. Ronald Bruce Bigger",
          "cluster_id": 4957843,
          "cite": [
            "492 P.3d 1020",
            "251 Ariz. 402"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Espinal-Almeida",
          "cluster_id": 811894,
          "cite": [
            "699 F.3d 588",
            "2012 WL 5511702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robinson v. Cook",
          "cluster_id": 815781,
          "cite": [
            "706 F.3d 25",
            "2013 U.S. App. LEXIS 1532",
            "2013 WL 238772"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Robert Walden v. David Shinn",
          "cluster_id": 4863579,
          "cite": [
            "990 F.3d 1183"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Samuel Fields v. Scott Jordan",
          "cluster_id": 9437053,
          "cite": [
            "86 F.4th 218"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Arthur",
          "cluster_id": 2720361,
          "cite": [
            "764 F.3d 92",
            "2014 U.S. App. LEXIS 16240",
            "2014 WL 4177373"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Shields",
          "cluster_id": 6478700,
          "cite": [
            "511 P.3d 931"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 805413,
          "cite": [
            "689 F.3d 12",
            "2012 WL 3064841",
            "2012 U.S. App. LEXIS 15631"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. City of Cheyenne",
          "cluster_id": 9497271,
          "cite": [
            "99 F.4th 1206"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Aekins",
          "cluster_id": 9373586,
          "cite": [
            "207 N.E.3d 934",
            "2023 Ohio 322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremiah Edwards",
          "cluster_id": 6469003,
          "cite": [
            "34 F.4th 570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 2700836,
          "cite": [
            "2013 Ohio 756"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jeremiah Farmer",
          "cluster_id": 6619700,
          "cite": [
            "38 F.4th 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Johnson",
          "cluster_id": 4878853,
          "cite": [
            "953 N.W.2d 772",
            "308 Neb. 331"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Maine v. Matthew R. Davis",
          "cluster_id": 4526287,
          "cite": [
            "2018 ME 116",
            "191 A.3d 1147"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Elijah Vines",
          "cluster_id": 4957586,
          "cite": [
            "9 F.4th 500"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Pope",
          "cluster_id": 4777304,
          "cite": [
            "943 N.W.2d 294",
            "305 Neb. 912"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jonathan Wayne Daniels",
          "cluster_id": 9468693,
          "cite": [
            "91 F.4th 1083"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Perry v. New Hampshire:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(7268276 OR 7268277 OR 7268278) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 72,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 72,
        "triage_read": 3,
        "triage_snippet_classified": 69
      },
      "lane2_top_cited": {
        "query": "cites:(7268276 OR 7268277 OR 7268278)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00JnM9MTAxMTg1NTMmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%287268276+OR+7268277+OR+7268278%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(7268276 OR 7268277 OR 7268278)",
        "reviewed": 29,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 29,
        "triage_read": 0,
        "triage_snippet_classified": 29
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(7268276 OR 7268277 OR 7268278)",
    "indexed_citing_opinions": 88,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 7268276,
        "count": 88,
        "count_source": "search"
      },
      {
        "opinion_id": 7268277,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 7268278,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 847,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/perry-v-new-hampshire.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1NzYzNjgmcz05NDUxOTg5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%287268276+OR+7268277+OR+7268278%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": []
  },
  "off_cl_links": [],
  "provenance": {
    "cl_source": "U",
    "cl_api": "https://www.courtlistener.com/api/rest/v4",
    "built_by": "S2-BUILDER-AUTHORING",
    "build_run": "s2-build-96d841cbb12e",
    "date_created": "2026-07-05T17:07:49Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T17:08:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T17:08:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T17:11:13Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T17:08:11Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Perry v. New Hampshire

```
<opinion type="majority">
<p id="b802-5">OPINION OF THE COURT</p>
<p id="b802-6">[<span class="citation no-link">565 U.S. 231</span>]</p>
<author id="b802-7">Justice Ginsburg</author>
<p id="Augc">delivered the opinion of the Court.</p>
<p id="b802-8">In our system of justice, fair trial for persons charged with criminal offenses is secured by the Sixth Amendment, which</p>
<p id="b802-9">[<span class="citation no-link">565 U.S. 232</span>]</p>
<p id="b802-10">guarantees to defendants the right to counsel, compulsory process to obtain defense witnesses, and the opportunity to cross-examine witnesses for the prosecution. Those safeguards apart, admission of evidence in state trials is ordinarily governed by state law, and the reliability of relevant testimony typically falls within the province of the jury to determine. This Court has recognized, in addition, a due process check on the admission of eyewitness identification, applicable when the police have arranged suggestive circumstances leading the witness to identify a particular person as the perpetrator of a crime.</p>
<p id="b802-16">An identification infected by improper police influence, our case law holds, is not automatically excluded. Instead, the trial judge must screen the evidence for reliability pretrial. If there is “a very substantial likelihood of irreparable misidentification,” <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States">390 U.S. 377, 384</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span> (1968), the judge must disallow presentation of the evidence at trial. But if the indicia of reliability are strong enough to outweigh the corrupting <page-number citation-index="1" label="703">*703</page-number>effect of the police-arranged suggestive circumstances, the identification evidence ordinarily will be admitted, and the jury will ultimately determine its worth.</p>
<p id="b803-4">We have not extended pretrial screening for reliability to cases in which the suggestive circumstances were not arranged by law enforcement officers. Petitioner requests that we do so because of the grave risk that mistaken identification will yield a miscarriage of justice.<footnotemark>1</footnotemark> Our decisions,</p>
<p id="ANlU">[<span class="citation no-link">565 U.S. 233</span>]</p>
<p id="b803-5">however, turn on the presence of state action and aim to deter police from rigging identification procedures, for example, at a lineup, showup, or photograph array. When no improper law enforcement activity is involved, we hold, it suffices to test reliability through the rights and opportunities generally designed for that purpose, notably, the presence of counsel at postindictment lineups, vigorous cross-examination, protective rules of evidence, and jury instructions on both the fallibility of eyewitness identification and the requirement that guilt be proved beyond a reasonable doubt.</p>
<p id="b803-6">I</p>
<p id="b803-7">A</p>
<p id="b803-8">Around 3 a.m. on August 15, 2008, Joffre Ullon called the Nashua, New Hampshire, Police Department and reported that an African-American male was trying to break into cars parked in the lot of Ullon’s apartment building. Officer Nicole Clay responded to the call. Upon arriving at the parking lot, Clay heard what “sounded like a metal bat hitting the ground.” App. 37a-38a. She then saw petitioner Barion Perry standing between two cars. Perry walked toward Clay, holding two car-stereo amplifiers in his hands. A metal bat lay on the ground behind him. Clay asked Perry where the amplifiers came from. “[I] found them on the ground,” Perry responded. <span class="citation no-link">Id.,</span> at 39a.</p>
<p id="b803-10">Meanwhile, Ullon’s wife, Nubia Blandón, woke her neighbor, Alex Clavijo, and told him she had just seen someone break into his car. Clavijo immediately went downstairs to the parking lot to inspect the car. He first observed that one of the rear windows had been shattered. On further inspection, he discovered that the speakers and amplifiers from his car stereo were missing, as were his bat and</p>
<p id="b803-11">[<span class="citation no-link">565 U.S. 234</span>]</p>
<p id="b803-12">wrench. Clavijo then approached Clay and told her about Blandon’s alert and his own subsequent observations.</p>
<p id="b803-13">By this time, another officer had arrived at the scene. Clay asked Perry to stay in the parking lot with that officer, while she and Clavijo went to talk to Blandón. Clay and Clavijo then entered the apartment building and took the stairs to the fourth floor, where Blandon’s and Clavijo’s apart<page-number citation-index="1" label="704">*704</page-number>ments were located. They met Blan-dón in the hallway just outside the open door to her apartment.</p>
<p id="b804-4">Asked to describe what she had seen, Blandón stated that, around 2:30 a.m., she saw from her kitchen window a tall, African-American man roaming the parking lot and looking into cars. Eventually, the man circled Clavijo’s car, opened the trunk, and removed a large box.<footnotemark>2</footnotemark></p>
<p id="b804-5">Clay asked Blandón for a more specific description of the man. Blandón pointed to her kitchen window and said the person she saw breaking into Clavijo’s car was standing in the parking lot, next to the police officer. Perry’s arrest followed this identification.</p>
<p id="b804-6">About a month later, the police showed Blandón a photographic array that included a picture of Perry and asked her to point out the man who had broken into Clavijo’s car. Blandón was unable to identify Perry.</p>
<p id="b804-7">B</p>
<p id="b804-8">Perry was charged in New Hampshire state court with one count of theft by unauthorized taking and one count of criminal mischief.<footnotemark>3</footnotemark> Before trial, he moved to suppress Blandon’s identification on the ground that admitting it at trial would violate due process. Blandón witnessed what</p>
<p id="Ap5qT">[<span class="citation no-link">565 U.S. 235</span>]</p>
<p id="b804-9">amounted to a one-person showup in the parking lot, Perry asserted, which all but guaranteed that she would identify him as the culprit. <em><span class="citation no-link">Id.,</span> </em>at 15a-16a.</p>
<p id="b804-10">The New Hampshire Superior Court denied the motion. <em><span class="citation no-link">Id.,</span> </em>at 82a-88a. To determine whether due process prohibits the introduction of an out-of-court identification at trial, the Superior Court said, this Court’s decisions instruct a two-step inquiry. First, the trial court must decide whether the police used an unnecessarily suggestive identification procedure. <em><span class="citation no-link">Id.,</span> </em>at 85a. If they did, the court must next consider whether the improper identification procedure so tainted the resulting identification as to render it unreliable and therefore inadmissible. <em><span class="citation no-link">Ibid.</span> </em>(citing <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (1972), and <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (1977)).</p>
<p id="b804-12">Perry’s challenge, the Superior Court concluded, failed at step one: Blandon’s identification of Perry on the night of the crime did not result from an unnecessarily suggestive procedure “manufacture [d] ... by the police.” App. 86a-87a. Blandón pointed to Perry “spontaneously,” the court noted, “without any inducement from the police.” <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 85a-86a. Clay did not ask Blandón whether the man standing in the parking lot was the man Blandón had seen breaking into Clavijo’s car. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Ibid.</a></span> </em>Nor did Clay ask Blandón to move to the window from which she had observed the break-in. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 86a.</p>
<p id="b804-13">The Superior Court recognized that there were reasons to question the accuracy of Blandon’s identification: The parking lot was dark in some locations; Perry was standing next to a police officer; Perry was the only African American man in the vicinity; and Blandón was unable, later, to pick <page-number citation-index="1" label="705">*705</page-number>Perry out of a photographic array. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 86a-87a. But “[b]ecause the police procedures were not unnecessarily suggestive,” the court ruled that the reliability of Blandon’s testimony was for the jury to consider. <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Id.,</a></span> </em>at 87a.</p>
<p id="b805-4">[<span class="citation no-link">565 U.S. 236</span>]</p>
<p id="b805-5">At the ensuing trial, Blandón and Clay testified to Blandon’s out-of-court identification. The jury found Perry guilty of theft and not guilty of criminal mischief.</p>
<p id="b805-6">On appeal, Perry repeated his challenge to the admissibility of Blandon’s out-of-court identification. The trial court erred, Perry contended, in requiring an initial showing that the police arranged the suggestive identification procedure. Suggestive circumstances alone, Perry argued, suffice to trigger the court’s duty to evaluate the reliability of the resulting identification before allowing presentation of the evidence to the jury.</p>
<p id="b805-7">The New Hampshire Supreme Court rejected Perry’s argument and affirmed his conviction. <em><span class="citation no-link">Id.,</span> </em>at 9a-11a. Only where the police employ suggestive identification techniques, that court held, does the Due Process Clause require a trial court to assess the reliability of identification evidence before permitting a jury to consider it. <em><span class="citation no-link">Id.,</span> </em>at 10a-11a.</p>
<p id="b805-8">We granted certiorari to resolve a division of opinion on the question whether the Due Process Clause requires a trial judge to conduct a preliminary assessment of the reliability of an eyewitness identification made under suggestive circumstances not arranged by the police. <span class="citation multiple-matches"><a href="/c/U.S./563/1020/">563 U.S. 1020</a></span>, <span class="citation multiple-matches"><a href="/c/S.%20Ct./131/2932/">131 S. Ct. 2932</a></span>, <span class="citation multiple-matches"><a href="/c/L.%20Ed.%202d/180/224/">180 L. Ed. 2d 224</a></span> (2011).<footnotemark>4</footnotemark></p>
<p id="b805-10">[<span class="citation no-link">565 U.S. 237</span>]</p>
<p id="b805-11">II</p>
<p id="b805-12">A</p>
<p id="b805-13">The Constitution, our decisions indicate, protects a defendant against a conviction based on evidence of questionable reliability, not by prohibiting introduction of the evidence, but by affording the defendant means to persuade the jury that the evidence should be discounted as unworthy of credit. Constitutional safeguards available to defendants to counter the State’s evidence include the Sixth Amendment rights to counsel, <em>Gideon </em>v. <em>Wainwright, </em><span class="citation" data-id="8945501"><a href="/opinion/8954562/gideon-v-wainwright/#343" aria-description="Citation for case: Gideon v. Wainwright">372 U.S. 335, 343-345</a></span>, <span class="citation" data-id="106545"><a href="/opinion/106545/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">83 S. Ct. 792</a></span>, <span class="citation" data-id="106545"><a href="/opinion/106545/gideon-v-wainwright/" aria-description="Citation for case: Gideon v. Wainwright">9 L. Ed. 2d 799</a></span> (1963); compulsory process, <em>Taylor </em>v. <em>Illinois, </em><span class="citation" data-id="9431168"><a href="/opinion/111986/taylor-v-illinois/#408" aria-description="Citation for case: Taylor v. Illinois">484 U.S. 400, 408-409</a></span>, <span class="citation" data-id="9431168"><a href="/opinion/111986/taylor-v-illinois/" aria-description="Citation for case: Taylor v. Illinois">108 S. Ct. 646</a></span>, <span class="citation" data-id="9431168"><a href="/opinion/111986/taylor-v-illinois/" aria-description="Citation for case: Taylor v. Illinois">98 L. Ed. 2d 798</a></span> (1988); and confrontation plus cross-examination of witnesses, <em>Delaware </em>v. <em>Fensterer, </em><span class="citation" data-id="9430219"><a href="/opinion/111535/delaware-v-fensterer/#18" aria-description="Citation for case: Delaware v. Fensterer">474 U.S. 15, 18-20</a></span>, <span class="citation" data-id="9430219"><a href="/opinion/111535/delaware-v-fensterer/" aria-description="Citation for case: Delaware v. Fensterer">106 S. Ct. 292</a></span>, <span class="citation" data-id="9430219"><a href="/opinion/111535/delaware-v-fensterer/" aria-description="Citation for case: Delaware v. Fensterer">88 L. Ed. 2d 15</a></span> (1985) <em>(per curiam). </em>Apart from these guarantees, we have recognized, state and federal statutes and rules ordinarily govern the admissibility of evidence, and juries are assigned the task of determining the reliability of the evidence presented <page-number citation-index="1" label="706">*706</page-number>at trial. See <em>Kansas </em>v. <em>Ventris, </em><span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/#594" aria-description="Citation for case: Kansas v. Ventris">556 U.S. 586, 594</a></span>, n., <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">129 S. Ct. 1841</a></span>, <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">173 L. Ed. 2d 801</a></span> (2009) (“Our legal system ... is built on the premise that it is the province of the jury to weigh the credibility of competing witnesses.”). Only when evidence “is so extremely unfair that its admission violates fundamental conceptions of justice,” <em>Dowling </em>v. <em>United States, </em><span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/#352" aria-description="Citation for case: Dowling v. United States">493 U.S. 342, 352</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">110 S. Ct. 668</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">107 L. Ed. 2d 708</a></span> (1990) (internal quotation marks omitted), have we imposed a constraint tied to the Due Process Clause. See, <em>e.g., Napue </em>v. <em>Illinois, </em><span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/#269" aria-description="Citation for case: Napue v. Illinois">360 U.S. 264, 269</a></span>, <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">79 S. Ct. 1173</a></span>, <span class="citation" data-id="105912"><a href="/opinion/105912/napue-v-illinois/" aria-description="Citation for case: Napue v. Illinois">3 L. Ed. 2d 1217</a></span> (1959) (Due process prohibits the State’s “knowin[g] use [of] false evidence,” because such use violates “any concept of ordered liberty.”).</p>
<p id="b806-4">Contending that the Due Process Clause is implicated here, Perry relies on a series of decisions involving police-arranged identification procedures. In <em>Stovall </em>v. <em>Denno, </em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">388 U.S. 293</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">87 S. Ct. 1967</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">18 L. Ed. 2d 1199</a></span> (1967), first of those decisions, a witness identified the defendant as her assailant after police officers brought</p>
<p id="A7GA8">[<span class="citation no-link">565 U.S. 238</span>]</p>
<p id="b806-5">the defendant to the witness’ hospital room. <span class="citation no-link"><em>Id., </em>at 295</span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">87 S. Ct. 1967</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">18 L. Ed. 2d 1199</a></span>. At the time the witness made the identification, the defendant—the only African-American in the room—was handcuffed and surrounded by police officers. <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Ibid.</a></span> </em>Although the police-arranged showup was undeniably suggestive, the Court held that no due process violation occurred. <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/#302" aria-description="Citation for case: Stovall v. Denno"><em>Id., </em>at 302</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">87 S. Ct. 1967</a></span>, <span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">18 L. Ed. 2d 1199</a></span>. Crucial to the Court’s decision was the procedure’s necessity: The witness was the only person who could identify or exonerate the defendant; the witness could not leave her hospital room; and it was uncertain whether she would live to identify the defendant in more neutral circumstances. <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Ibid.</a></span></em></p>
<p id="b806-7">A year later, in <em>Simmons </em>v. <em>United States, </em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">390 U.S. 377</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span> (1968), the Court addressed a due process challenge to police use of a photographic array. When a witness identifies the defendant in a police-organized photo lineup, the Court ruled, the identification should be suppressed only where “the photographic identification procedure was so [unnecessarily] suggestive as to give rise to a very substantial likelihood of irreparable misidentification.” <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#384" aria-description="Citation for case: Simmons v. United States"><em>Id., </em>at 384-385</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span>. Satisfied that the photo array used by Federal Bureau of Investigation agents in <em><span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">Simmons</a></span> </em>was both necessary and unlikely to have led to a mistaken identification, the Court rejected the defendant’s due process challenge to admission of the identification. <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/#385" aria-description="Citation for case: Simmons v. United States"><em>Id., </em>at 385-386</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">88 S. Ct. 967</a></span>, <span class="citation" data-id="9423638"><a href="/opinion/107636/simmons-v-united-states/" aria-description="Citation for case: Simmons v. United States">19 L. Ed. 2d 1247</a></span>. In contrast,  the Court held in <em>Foster </em>v. <em>California, </em><span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">394 U.S. 440</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">89 S. Ct. 1127</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">22 L. Ed. 2d 402</a></span> (1969), that due process required the exclusion of an eyewitness identification obtained through police-arranged procedures that “made it all but inevitable that [the witness] would identify [the defendant].” <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/#443" aria-description="Citation for case: Foster v. California"><em>Id., </em>at 443</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">89 S. Ct. 1127</a></span>, <span class="citation" data-id="9423977"><a href="/opinion/107890/foster-v-california/" aria-description="Citation for case: Foster v. California">22 L. Ed. 2d 402</a></span>.</p>
<p id="b806-8">Synthesizing previous decisions,  we set forth in <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (1972), and reiterated in <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (1977), the approach appropriately used to determine whether the Due Process Clause requires suppression of an eyewitness identification tainted by police arrangement. The Court emphasized, first, that due process concerns arise only when law enforcement officers <page-number citation-index="1" label="707">*707</page-number>use an</p>
<p id="b807-4">[<span class="citation no-link">565 U.S. 239</span>]</p>
<p id="b807-5">identification procedure that is both suggestive and unnecessary. <em>Id., </em>at 107, 109, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>; <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 198</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>. Even when the police use such a procedure, the Court next said, suppression of the resulting identification is not the inevitable consequence. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112-113</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>; <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#198" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 198-199</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>.</p>
<p id="b807-6">A rule requiring automatic exclusion, the Court reasoned, would “g[o] too far,” for it would “kee[p] evidence from the jury that is reliable and relevant,” and “may result, on occasion, in the guilty going free.” <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>; see <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#113" aria-description="Citation for case: Manson v. Brathwaite"><em>id., </em>at 113</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (when an “identification is reliable despite an unnecessarily suggestive [police] identification procedure,” automatic exclusion “is a Draconian sanction,” one “that may frustrate rather than promote justice”).</p>
<p id="b807-7">Instead of mandating a <em>per se </em>exclusionary rule, the Court held that the Due Process Clause requires courts to assess, on a case-by-case basis, whether improper police conduct created a “substantial likelihood of misidentification.” <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#201" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 201</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>; see <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#116" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 116</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. “[R]eliability [of the eyewitness identification] is the linchpin” of that evaluation, the Court stated in <em>Brathwaite. Id., </em>at 114, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. Where the “indicators of [a witness’] ability to make an accurate identification” are “outweighed by the corrupting effect” of law enforcement suggestion, the identification should be suppressed. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite"><em>Id., </em>at 114, 116</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. Otherwise, the evidence (if admissible in all other respects) should be submitted to the jury.<footnotemark>5</footnotemark></p>
<p id="b807-9">Applying this “totality of the circumstances” approach, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#110" aria-description="Citation for case: Manson v. Brathwaite"><em>id., </em>at 110</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>, the Court held in <em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">Biggers</a></span> </em>that law enforcement’s use</p>
<p id="b807-10">[<span class="citation no-link">565 U.S. 240</span>]</p>
<p id="b807-11">of an unnecessarily suggestive showup did not require suppression of the victim’s identification of her assailant. <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U.S., at 199-200</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span>. Notwithstanding the improper procedure, the victim’s identification was reliable: She saw her assailant for a considerable period of time under adequate light, provided police with a detailed description of her attacker long before the showup, and had “no doubt” that the defendant was the person she had seen. <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#200" aria-description="Citation for case: Neil v. Biggers"><em>Id., </em>at 200</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (internal quotation marks omitted). Similarly, the Court concluded in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>that police use of an unnecessarily suggestive photo array did not require exclusion of the resulting identification. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 114-117</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. The witness, an undercover police officer, viewed the defendant in good light for several minutes, provided a thorough description of the suspect, and was certain of his identification. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#115" aria-description="Citation for case: Manson v. Brathwaite"><em>Id., </em>at 115</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d <page-number citation-index="1" label="708">*708</page-number>140</a></span>. Hence, the “indicators of [the witness’] ability to make an accurate identification [were] hardly outweighed by the corrupting effect of the challenged identification.” <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#116" aria-description="Citation for case: Manson v. Brathwaite"><em>Id., </em>at 116</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>.</p>
<p id="b808-4">B</p>
<p id="b808-5">Perry concedes that, in contrast to every case in the <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span> </em>line, law enforcement officials did not arrange the suggestive circumstances surrounding Blandon’s identification. See Brief for Petitioner 34; Tr. of Oral Arg. 5 (counsel for Perry) (“[W]e do not allege any manipulation or intentional orchestration by the police.”). He contends, however, that it was mere happenstance that each of the <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span> </em>cases involved improper police action. The rationale underlying our decisions, Perry asserts, supports a rule requiring trial judges to pre-screen eyewitness evidence for reliability any time an identification is made under suggestive circumstances. We disagree.</p>
<p id="b808-6">Perry’s argument depends, in large part, on the Court’s statement in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>that “reliability is the linchpin in determining the admissibility of identification testimony.” <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 114</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. If reliability is the linchpin of admissibility</p>
<p id="b808-7">[<span class="citation no-link">565 U.S. 241</span>]</p>
<p id="ATboI">under the Due Process Clause, Perry maintains, it should make no difference whether law enforcement was responsible for creating the suggestive circumstances that marred the identification.</p>
<p id="b808-8">Perry has removed our statement in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>from its mooring, and thereby attributes to the statement a meaning a fair reading of our opinion does not bear. As just explained, <em>supra, </em>at 238-239, 181 L. Ed. 2d, at 706-707,  the <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>Court’s reference to reliability appears in a portion of the opinion concerning the appropriate remedy <em>when the police use an unnecessarily suggestive identification procedure. </em>The Court adopted a judicial screen for reliability as a course preferable to a <em>per se </em>rule requiring exclusion of identification evidence whenever law enforcement officers employ an improper procedure. The due process check for reliability, <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>made plain, comes into play only after the defendant establishes improper police conduct. The very purpose of the check, the Court noted, was to avoid depriving the jury of identification evidence that is reliable, <em>notwithstanding </em>improper police conduct. <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112-113</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>.<footnotemark>6</footnotemark></p>
<p id="b808-10">Perry’s contention that improper police action was not essential to the reliability check <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>required is echoed by the dissent. <em>Post, </em>at 252, 181 L. Ed. 2d, at 715. Both ignore  a key premise of the <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>decision: A primary aim of excluding identification evidence obtained under unnecessarily suggestive circumstances, the Court said, is to deter law enforcement use of improper lineups, showups, and photo arrays in the first place. See <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#112" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 112</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>. Alerted to the prospect that identification evidence improperly obtained may be excluded, the Court reasoned, police officers will “guard <page-number citation-index="1" label="709">*709</page-number>against unnecessarily suggestive procedures.” <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Ibid.</a></span> </em>This deterrence rationale is inapposite in cases, like Perry’s, in which the police engaged in no improper conduct.</p>
<p id="b809-5"><em>Coleman </em>v. <em>Alabama, </em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">399 U.S. 1</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (1970), another decision in the <em><span class="citation" data-id="9423482"><a href="/opinion/107488/stovall-v-denno/" aria-description="Citation for case: Stovall v. Denno">Stovall</a></span> </em>line, similarly shows that the Court has linked the due process check, not to suspicion of eyewitness testimony generally, but only to improper police arrangement of the circumstances surrounding an identification. The defendants in <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Coleman</a></span> </em>contended that a witness’ in-court identifications violated due process, because a pretrial stationhouse lineup was “so unduly prejudicial and conducive to irreparable misidentification as fatally to taint [the later identifications].” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#3" aria-description="Citation for case: Coleman v. Alabama">399 U.S., at 3</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (plurality opinion). The Court rejected this argument. <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#5" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 5-6</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (plurality opinion), 13-14, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (Black, J., concurring), 22, n. 2, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (Burger, C. J., dissenting), 28, n. 2, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span> (Stewart, J., dissenting). No due process violation occurred, the plurality explained, because nothing “the police said or did prompted [the witness’] virtually spontaneous identification of [the defendants].” <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/#6" aria-description="Citation for case: Coleman v. Alabama"><em>Id., </em>at 6</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">90 S. Ct. 1999</a></span>, <span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">26 L. Ed. 2d 387</a></span>. True, Coleman was the only person in the lineup wearing a hat, the plurality noted, but “nothing in the record show[ed] that he was required to do so.” <em><span class="citation" data-id="9424314"><a href="/opinion/108182/coleman-v-alabama/" aria-description="Citation for case: Coleman v. Alabama">Ibid.</a></span> See </em>also <em>Colorado </em>v. <em>Connelly, </em><span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/#163" aria-description="Citation for case: Colorado v. Connelly">479 U.S. 157, 163, 167</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">107 S. Ct. 515</a></span>, <span class="citation" data-id="9430748"><a href="/opinion/111779/colorado-v-connelly/" aria-description="Citation for case: Colorado v. Connelly">93 L. Ed. 2d 473</a></span> (1986) (Where the “crucial element of police overreaching” is missing, the admissibility of an allegedly unreliable confession is “a matter to be governed by the evidentiary laws of the forum, . . . and not by the Due Process Clause.”).</p>
<p id="b809-9">Perry and the dissent place significant weight on <em>United States </em>v. <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">388 U.S. 218</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span> (1967), describing it as a decision not anchored to improper police conduct. See Brief for Petitioner 12, 15, 21-22, 28; <em>post, </em>at 250-253, 256-258, 181 L. Ed. 2d, at 714-716, 718-719. In fact,  the risk of police rigging was the very danger to which the Court responded in <em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">Wade</a></span> </em>when it recognized a defendant’s right to counsel at postindictment, police-organized identification procedures. 388 U.S., at 233, 235-236, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>. “[T]he confrontation <em>compelled by the State </em>between the accused and the</p>
<p id="A0bn">[<span class="citation no-link">565 U.S. 243</span>]</p>
<p id="b809-10">victim or witnesses,” the Court began, “is peculiarly riddled with innumerable dangers and variable factors which might seriously, even crucially, derogate from a fair trial.” <em>Id., </em>at 228, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span> (emphasis added). “A major factor contributing to the high incidence of miscarriage of justice from mistaken identification,” the Court continued, “has been the degree of suggestion inherent in the manner in which <em>the prosecution </em>presents the suspect to witnesses for pretrial identification.” <em>Ibid, </em>(emphasis added). To illustrate the improper suggestion it was concerned about, the Court pointed to police-designed lineups where “all in the lineup but the suspect were known to the identifying witness, . . . the other participants in [the] lineup were grossly dissimilar in appearance to the suspect, . . . only the suspect was required to wear distinctive clothing which the culprit allegedly wore, . . . the witness is told by the police that they have caught the culprit after <page-number citation-index="1" label="710">*710</page-number>which the defendant is brought before the witness alone or is viewed in jail, .. . the suspect is pointed out before or during a lineup, . . . the participants in the lineup are asked to try on an article of clothing which fits only the <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#233" aria-description="Citation for case: United States v. Wade"><em>suspect.” Id., </em>at 233</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>. Beyond genuine debate, then, prevention of unfair police practices prompted the Court to extend a defendant’s right to counsel to cover postindictment lineups and showups. <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#235" aria-description="Citation for case: United States v. Wade"><em>Id., </em>at 235</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>.</p>
<p id="b810-4">Perry’s argument, reiterated by the dissent, thus lacks support in the case law he cites. Moreover, his position would open the door to judicial preview, under the banner of due process, of most, if not all, eyewitness identifications. External suggestion is hardly the only factor that casts doubt on the trustworthiness of an eyewitness’ testimony. As one of Perry’s <em>amici </em>points out, many other factors bear on “the likelihood of misidentification,” <em>post, </em>at 258, 181 L. Ed. 2d, at 719—for example, the passage of time between exposure to and identification of the defendant, whether the witness was under stress when he first encountered the suspect, how much time the witness had to observe the suspect, how far the witness was</p>
<p id="ADT2">[<span class="citation no-link">565 U.S. 244</span>]</p>
<p id="b810-5">from the suspect, whether the suspect carried a weapon, and the race of the suspect and the witness. Brief for American Psychological Association as <em>Amicus Curiae </em>9-12. There is no reason why an identification made by an eyewitness with poor vision, for example, or one who harbors a grudge against the defendant, should be regarded as inherently more reliable, less of a “threat to the fairness of trial,” <em>post, </em>at 262, 181 L. Ed. 2d, at 722, than the identification Blandón made in this case. To embrace Perry’s view would thus entail a vast enlargement of the reach of due process as a constraint on the admission of evidence.</p>
<p id="b810-8">Perry maintains that the Court can limit the due process check he proposes to identifications made under “suggestive circumstances.” Tr. of Oral Arg. 11-14. Even if we could rationally distinguish suggestiveness from other factors bearing on the reliability of eyewitness evidence, Perry’s limitation would still involve trial courts, routinely, in preliminary examinations.  Most eyewitness identifications involve some element of suggestion. Indeed, all in-court identifications do. Out-of-court identifications volunteered by witnesses are also likely to involve suggestive circumstances. For example, suppose a witness identifies the defendant to police officers after seeing a photograph of the defendant in the press captioned “theft suspect,” or hearing a radio report implicating the defendant in the crime. Or suppose the witness knew that the defendant ran with the wrong crowd and saw him on the day and in the vicinity of the crime. Any of these circumstances might have “suggested” to the witness that the defendant was the person the witness observed committing the crime.</p>
<p id="b810-9">C</p>
<p id="b810-10">In urging a broadly applicable due process check on eyewitness identifications, Perry maintains that eyewitness identifications are a uniquely unreliable form of evidence. See Brief for Petitioner 17-22 (citing studies showing that</p>
<p id="b810-11">[<span class="citation no-link">565 U.S. 245</span>]</p>
<p id="b810-12">eyewitness mis-identifications are the leading cause of wrongful convictions); Brief for American Psychological Association as <em>Amicus Curiae </em>14-17 (describing research indicating that as many as <page-number citation-index="1" label="711">*711</page-number>one in three eyewitness identifications is inaccurate). See also <em>post, </em>at 262-265, 181 L. Ed. 2d, at 722-724. We do not doubt either the importance or the fallibility of eyewitness identifications. Indeed, in recognizing that defendants have a constitutional right to counsel at postindictment police lineups, we observed that “the annals of criminal law are rife with instances of mistaken identification.” <em>Wade, </em><span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/#228" aria-description="Citation for case: United States v. Wade">388 U.S., at 228</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">87 S. Ct. 1926</a></span>, <span class="citation" data-id="9423472"><a href="/opinion/107486/united-states-v-wade/" aria-description="Citation for case: United States v. Wade">18 L. Ed. 2d 1149</a></span>.</p>
<p id="b811-4">We have concluded in other contexts, however, that the potential unreliability of a type of evidence does not alone render its introduction at the defendant’s trial fundamentally unfair. See, <em>e.g., Ventris, </em><span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/#594" aria-description="Citation for case: Kansas v. Ventris">556 U.S., at 594</a></span>, n., <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">129 S. Ct. 1841</a></span>, <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">173 L. Ed. 2d 801</a></span> (declining to “craft a broa[d] exclusionary rule for uncorroborated statements obtained [from jailhouse snitches],” even though “rewarded informant testimony” may be inherently untrustworthy); <em>Dowling, </em><span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/#353" aria-description="Citation for case: Dowling v. United States">493 U.S., at 353</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">110 S. Ct. 668</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">107 L. Ed. 2d 708</a></span> (rejecting argument that the introduction of evidence concerning acquitted conduct is fundamentally unfair because such evidence is “inherently unreliable”). We reach a similar conclusion here: The fallibility of eyewitness evidence does not, without the taint of improper state conduct, warrant a due process rule requiring a trial court to screen such evidence for reliability before allowing the jury to assess its creditworthiness.</p>
<p id="b811-6">Our unwillingness to enlarge the domain of due process as Perry and the dissent urge rests, in large part, on our recognition that the jury, not the judge, traditionally determines the reliability of evidence. See <em>supra, </em>at 237, 181 L. Ed. 2d, at 705. We also take account of other safeguards built into our adversary system that caution juries against placing undue weight on eyewitness testimony of questionable reliability. These protections include the defendant’s Sixth Amendment right to confront the eyewitness. See <em>Maryland </em>v. <em>Craig, </em><span class="citation" data-id="9842114"><a href="/opinion/112489/maryland-v-craig/#845" aria-description="Citation for case: Maryland v. Craig">497 U.S. 836, 845</a></span>, <span class="citation" data-id="9842114"><a href="/opinion/112489/maryland-v-craig/" aria-description="Citation for case: Maryland v. Craig">110 S. Ct. 3157</a></span>, <span class="citation" data-id="9842114"><a href="/opinion/112489/maryland-v-craig/" aria-description="Citation for case: Maryland v. Craig">111 L. Ed. 2d 666</a></span> (1990) (“The central concern of the Confrontation Clause</p>
<p id="A-rq">[<span class="citation no-link">565 U.S. 246</span>]</p>
<p id="b811-7">is to ensure the reliability of the evidence against a criminal defendant.”). Another is the defendant’s right to the effective assistance of an attorney, who can expose the flaws in the eyewitness’ testimony during cross-examination and focus the jury’s attention on the fallibility of such testimony during opening and closing arguments. Eyewitness-specific jury instructions, which many federal and state courts have adopted,<footnotemark>7</footnotemark> likewise warn the jury to take care in appraising identification evidence. See, <em>e.g., </em><page-number citation-index="1" label="712">*712</page-number><em>United States </em>v. <em>Telfaire, </em><span class="citation" data-id="9458886"><a href="/opinion/306634/united-states-v-melvin-telfaire/#558" aria-description="Citation for case: United States v. Melvin Telfaire">469 F.2d 552, 558-559</a></span> (CADC 1972) <em>(per curiam) </em>(D. C. Circuit Model Jury Instructions) (“If the identification by the witness may have been influenced by the circumstances under which the defendant was presented to him for identification, you should scrutinize the identification with great care.”). See also <em>Ventris, </em><span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/#594" aria-description="Citation for case: Kansas v. Ventris">556 U.S., at 594</a></span>, n., <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">129 S. Ct. 1841</a></span>, <span class="citation" data-id="145880"><a href="/opinion/145880/kansas-v-ventris/" aria-description="Citation for case: Kansas v. Ventris">173 L. Ed. 2d 801</a></span> (citing jury instructions that informed jurors about the unreliability of uncorroborated jailhouse-informant testimony as a reason to</p>
<p id="b812-4">[<span class="citation no-link">565 U.S. 247</span>]</p>
<p id="b812-5">resist a ban on such testimony); <em>Dowling, </em><span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/#352" aria-description="Citation for case: Dowling v. United States">493 U.S., at 352-353</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">110 S. Ct. 668</a></span>, <span class="citation" data-id="9431876"><a href="/opinion/112352/dowling-v-united-states/" aria-description="Citation for case: Dowling v. United States">107 L. Ed. 2d 708</a></span>. The constitutional requirement that the government prove the defendant’s guilt beyond a reasonable doubt also impedes convictions based on dubious identification evidence.</p>
<p id="b812-6">State and Federal Rules of Evidence, moreover, permit trial judges to exclude relevant evidence if its probative value is substantially outweighed by its prejudicial impact or potential for misleading the jury. See, <em>e.g., </em>Fed. Rule Evid. 403; N.H. Rule Evid. 403 (2011). See also Tr. of Oral Arg. 19-22 (inquiring whether the standard Perry seeks differs materially from the one set out in Rule 403). In appropriate cases, some States also permit defendants to present expert testimony on the hazards of eyewitness identification evidence. See, <em>e.g., State </em>v. <em>Clopten, </em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/#33" aria-description="Citation for case: State v. Clopten">2009 UT 84, ¶ 33</a></span>, <span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/#1113" aria-description="Citation for case: State v. Clopten">223 P.3d 1103, 1113</a></span> (“We expect . . . that in cases involving eyewitness identification of strangers or near-strangers, trial courts will routinely admit expert testimony [on the dangers of such evidence].”).</p>
<p id="b812-7">Many of the safeguards just noted were at work at Perry’s trial. During her opening statement, Perry’s cour-tappointed attorney cautioned the jury about the vulnerability of Bland-on’s identification. App. 115a (Blan-dón, “the eyewitness that the State needs you to believe [,] can’t pick [Perry] out of a photo array. How carefully did she really see what was going on? . . . How well could she really see him?”). While cross-examining Blandón and Officer Clay, Perry’s attorney constantly brought up the weaknesses of Blandon’s identification. She highlighted: (1) the significant distance between Blandon’s window and the parking lot, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 226a; (2) the lateness of the hour, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 225a; (3) the van that partly obstructed Blandon’s view, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 226a; (4) Blandon’s concession that she was “so scared [she] really didn’t pay attention” to what Perry was wearing, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 233a; (5) Blandon’s inability to describe Perry’s facial features or other identifying marks, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 205a, 233a-235a; (6) Blandon’s failure to pick Perry out of a photo array, <em><span class="citation" data-id="9788258"><a href="/opinion/2592762/state-v-clopten/" aria-description="Citation for case: State v. Clopten">id.,</a></span> </em>at 235a; and (7)</p>
<p id="b812-9">[<span class="citation no-link">565 U.S. 248</span>]</p>
<p id="b812-10">Perry’s position next to a uniformed, gun-bearing police officer at the moment Blandón made her identification, <em><span class="citation no-link">id.,</span> </em>at 202a-205a. Perry’s counsel reminded the jury of these frailties during her summation. <em><span class="citation no-link">Id.,</span> </em>at 374a-375a (Blandón “wasn’t able to tell you much about who she saw .... She couldn’t pick [Perry] out of a lineup, out of a photo array .... [Blandón said] [t]hat guy that was with the police officer, that’s who was circling. Again, think about the context with the guns, the uniforms. Powerful, powerful context clues.”).</p>
<p id="b812-11">After closing arguments, the trial court read the jury a lengthy instruction on identification testimony and the factors the jury should consider <page-number citation-index="1" label="713">*713</page-number>when evaluating it. <em><span class="citation no-link">Id.,</span> </em>at 399a-40la. The court also instructed the jury that the defendant’s guilt must be proved beyond a reasonable doubt, <em><span class="citation no-link">id.,</span> </em>at 390a, 392a, 395a-396a, and specifically cautioned that “one of the things the State must prove [beyond a reasonable doubt] is the identification of the defendant as the person who committed the offense,” <em><span class="citation no-link">id.,</span> </em>at 398a-399a.</p>
<p id="b813-6">Given the safeguards generally applicable in criminal trials, protections availed of by the defense in Perry’s case, we hold that the introduction of Blandon’s eyewitness testimony, without a preliminary judicial assessment of its reliability, did not render Perry’s trial fundamentally unfair.</p>
<p id="Am26">* * *</p>
<p id="b813-11">For the foregoing reasons, we agree with the New Hampshire courts’ appraisal of our decisions. See <em>supra, </em>at 235-236, 181 L. Ed. 2d, at 704-705. Finding no convincing reason to alter our precedent, we hold that [16] the Due Process Clause does not require a preliminary judicial inquiry into the reliability of an eyewitness identification when the identification was not procured under unnecessarily suggestive circumstances arranged by law enforcement. Accordingly, the judgment of the New Hampshire Supreme Court is affirmed.</p>
<footnote label="1">
<p id="b803-14">. The dissent, too, appears to urge that all suggestive circumstances raise due process concerns warranting a pretrial ruling. See <em>post, </em>at 254, 257, 262-265, 181 L. Ed. 2d, at 717, 718, 722-724. Neither Perry nor the dissent, however, points to a single case in which we have required pretrial screening absent a police arranged identification procedure. Understandably so, for there are no such cases. Instead, the dissent surveys our decisions, heedless of the police arrangement that underlies every one of them, and inventing a “longstanding rule,’’ <em>post, </em>at 254, 181 L. Ed. 2d, at 717, that never existed. Nor are we, as the dissent suggests, imposing a <em>mens rea </em>requirement, <em>post, </em>at 250, 255, 181 L. Ed. 2d, at 714, 717, or otherwise altering our precedent in any way.  As our case law makes clear, what triggers due process concerns is police use of an unnecessarily suggestive identification procedure, whether or not they intended the arranged procedure to be suggestive.</p>
</footnote>
<footnote label="2">
<p id="b804-14">. The box, which Clay found on the ground near where she first encountered Perry, contained car-stereo speakers. App. 177a-178a.</p>
</footnote>
<footnote label="3">
<p id="b804-15">. The theft charge was based on the taking of items from Clavijo’s car, while the criminal mischief count was founded on the shattering of Clavijo’s car window.</p>
</footnote>
<footnote label="4">
<p id="b805-14">. Compare <em>United States </em>v. <em>Bouthot, </em><span class="citation" data-id="526035"><a href="/opinion/526035/united-states-v-joseph-t-bouthot/#1516" aria-description="Citation for case: United States v. Joseph T. Bouthot">878 F.2d 1506, 1516</a></span> (CA1 1989) (Due process requires federal courts to “scrutinize all suggestive identification procedures, not just those orchestrated by the police.’’); <em>Dunnigan </em>v. <em>Keane, </em><span class="citation" data-id="751771"><a href="/opinion/751771/richard-w-dunnigan-v-john-p-keane-superintendent-sing-sing/#128" aria-description="Citation for case: Richard W. Dunnigan v. John P. Keane, Superintendent,...">137 F.3d 117, 128</a></span> (CA2 1998) (same); <em>Thigpen </em>v. <em>Cory, </em><span class="citation" data-id="9475532"><a href="/opinion/478967/willie-arthur-thigpen-v-duane-cory/#895" aria-description="Citation for case: Willie Arthur Thigpen v. Duane Cory">804 F.2d 893, 895</a></span> (CA6 1986) (same), with <em>United States </em>v. <em>Kimberlin, </em><span class="citation" data-id="9475552"><a href="/opinion/479235/united-states-v-brett-c-kimberlin/#233" aria-description="Citation for case: United States v. Brett C. Kimberlin">805 F.2d 210, 233</a></span> (CA7 1986) (Due process check is required only in cases involving improper state action.); <em>United States </em>v. <em>Zeiler, </em><span class="citation" data-id="307083"><a href="/opinion/307083/united-states-v-william-edward-zeiler/#720" aria-description="Citation for case: United States v. William Edward Zeiler">470 F.2d 717, 720</a></span> (CA3 1972) (same); <em>State </em>v. <em>Addison, </em><span class="citation" data-id="2446404"><a href="/opinion/2446404/state-v-addison/#801" aria-description="Citation for case: State v. Addison">160 N.H. 792, 801</a></span>, <span class="citation" data-id="2446404"><a href="/opinion/2446404/state-v-addison/#125" aria-description="Citation for case: State v. Addison">8 A.3d 118, 125</a></span> (2010) (same); <em>State </em>v. <em>Reid, </em><span class="citation" data-id="9662547"><a href="/opinion/1636806/state-v-reid/#272" aria-description="Citation for case: State v. Reid">91 S.W.3d 247, 272</a></span> (Tenn. 2002) (same); <em>State </em>v. <em>Nordstrom, </em><span class="citation" data-id="2587271"><a href="/opinion/2587271/state-v-nordstrom/#241" aria-description="Citation for case: State v. Nordstrom">200 Ariz. 229, 241</a></span>, <span class="citation" data-id="2587271"><a href="/opinion/2587271/state-v-nordstrom/#729" aria-description="Citation for case: State v. Nordstrom">25 P.3d 717, 729</a></span> (2001) (same); <em>Semple </em>v. <em>State, </em><span class="citation" data-id="1226333"><a href="/opinion/1226333/semple-v-state/#417" aria-description="Citation for case: Semple v. State">271 Ga. 416, 417-418</a></span>, <span class="citation" data-id="1226333"><a href="/opinion/1226333/semple-v-state/#913" aria-description="Citation for case: Semple v. State">519 S.E.2d 912, 913-914</a></span> (1999) (same); <em>Harris </em>v. <em>State, </em><span class="citation" data-id="2232289"><a href="/opinion/2232289/harris-v-state/#581" aria-description="Citation for case: Harris v. State">619 N.E.2d 577, 581</a></span> (Ind. 1993) (same); <em>State </em>v. <em>Pailon, </em><span class="citation" data-id="2390875"><a href="/opinion/2390875/state-v-pailon/#862" aria-description="Citation for case: State v. Pailon">590 A.2d 858, 862-863</a></span> (R. I. 1991) (same); <em>Commonwealth </em>v. <em>Colon-Cruz, </em><span class="citation" data-id="2153683"><a href="/opinion/2153683/commonwealth-v-colon-cruz/#541" aria-description="Citation for case: Commonwealth v. Colon-Cruz">408 Mass. 533, 541-542</a></span>, <span class="citation" data-id="2153683"><a href="/opinion/2153683/commonwealth-v-colon-cruz/#805" aria-description="Citation for case: Commonwealth v. Colon-Cruz">562 N.E.2d 797, 805</a></span> (1990) (same); <em>State </em>v. <em>Brown, </em><span class="citation" data-id="6760622"><a href="/opinion/6869000/state-v-brown/#310" aria-description="Citation for case: State v. Brown">38 Ohio St. 3d 305, 310-311</a></span>, <span class="citation multiple-matches"><a href="/c/N.E.2d/528/523/">528 N.E.2d 523</a></span>, 533 (1988) (same); <em>Wilson </em>v. <em>Commonwealth, </em><span class="citation" data-id="1777225"><a href="/opinion/1777225/wilson-v-commonwealth/#857" aria-description="Citation for case: Wilson v. Commonwealth">695 S.W.2d 854, 857</a></span> (Ky. 1985) (same).</p>
</footnote>
<footnote label="5">
<p id="b807-12">. Among “factors to be considered’’ in evaluating a witness’ “ability to make an accurate identification,’’ the Court listed: “the opportunity of the witness to view the criminal at the time of the crime, the witness’ degree of attention, the accuracy of his prior description of the criminal, the level of certainty demonstrated at the confrontation, and the time between the crime and the confrontation.’’ <em>Manson </em>v. <em>Brathwaite, </em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#114" aria-description="Citation for case: Manson v. Brathwaite">432 U.S. 98, 114</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span> (1977) (citing <em>Neil </em>v. <em>Biggers, </em><span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/#199" aria-description="Citation for case: Neil v. Biggers">409 U.S. 188, 199-200</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">93 S. Ct. 375</a></span>, <span class="citation" data-id="9425063"><a href="/opinion/108639/neil-v-biggers/" aria-description="Citation for case: Neil v. Biggers">34 L. Ed. 2d 401</a></span> (1972)).</p>
</footnote>
<footnote label="6">
<p id="b808-11">. The Court’s description of the question presented in <em><span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">Brathwaite</a></span> </em>assumes that improper state action occurred: “[Does] the Due Process Clause of the Fourteenth Amendment compe[l] the exclusion, in a state criminal trial, apart from any consideration of reliability, of pretrial identification evidence obtained by a police procedure that was both suggestive and unnecessary.’’ <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/#99" aria-description="Citation for case: Manson v. Brathwaite">432 U.S., at 99</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">97 S. Ct. 2243</a></span>, <span class="citation" data-id="9426868"><a href="/opinion/109693/manson-v-brathwaite/" aria-description="Citation for case: Manson v. Brathwaite">53 L. Ed. 2d 140</a></span>.</p>
</footnote>
<footnote label="7">
<p id="b811-9">. See Model Crim. Jury Instr. No. 4.15 (CA3 2009); <em>United States </em>v. <em>Holley, </em><span class="citation" data-id="321228"><a href="/opinion/321228/united-states-v-albert-junior-holley/#277" aria-description="Citation for case: United States v. Albert Junior Holley">502 F.2d 273, 277-278</a></span> (CA4 1974); Pattern Crim. Jury Instr. No. 1.29 (CA5 2001); Pattern Crim. Jury Instr. No. 7.11 (CA6 2011); Fed. Crim. Jury Instr. No. 3.08 (CA7 1999); Model Crim. Jury Instr. for the District Courts No. 4.08 (CA8 2011); Model Crim. Jury Instr. No. 4.11 (CA9 2010); Pattern Crim. Jury Instr. No. 1.29 (CA10 2011); Pattern Jury Instr., Crim. Cases, Spec. Instr. No. 3 (CA11 2010); Rev. Ariz. Jury Instr., Crim., No. 39 (3d ed. 2008); 1 Judicial Council of Cal., Crim. Jury Instr., No. 315 (Summer 2011); Conn. Crim. Jury Instr. No. 2.6-4 (4th ed. 2007); 2 Ga. Suggested Pattern Jury Instr., Crim. Cases, No. 1.35.10 (4th ed. 2011); Ill. Pattern Jury Instr., Crim., No. 3.15 (Supp. 2011); Pattern Instr., Kan. 3d, Crim., No. 52.20 (2011); 1 Md. Crim. Jury Instr. &amp; Commentary §§ 2.56, 2.57(A), 2.57(B) (3d ed. 2009 and Supp. 2010); Mass. Crim. Model Jury Instr. No. 9.160 (2009); 10 Minn. Jury Instr. Guides, Crim., No. 3.19 (Supp. 2006); N.H. Crim. Jury Instr. No. 3.06 (1985); N.Y. Crim. Jury Instr. “Identification—One Witness’’ and “Identification—Witness Plus’’ (2d ed. 2011); Okla. Uniform Jury Instr., Crim., No. 9-19 (Supp. 2000); 1 Pa. Suggested Standard Crim. Jury Instr. No. 4.07B (2d ed. 2010); Term. Pattern Jury Instr., Crim., No. 42.05 (15th ed. 2011); Model <page-number citation-index="1" label="712">*712</page-number>Utah Jury Instr. CR404 (2d ed. 2011); Model Instructions from the Vt. Crim. Jury Instr. Comm. Nos. CR5-601, CR5-605 (2003); W. Va. Crim. Jury Instr. No. 5.05 (6th ed. 2003).</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Peters v. New York.md  (`case`, 6 assertions)

### content_page

```
---
title: "Peters v. New York"
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
  composite_basis_ref: Peters v. New York
  varies_by_point: false
  scope_note: "Good law. Decided in the same opinion as Sibron v. New York (and companion to Terry v. Ohio): where probable cause to arrest existed, the search was valid as a search incident to a lawful arrest. opinion_id shared with Sibron (consolidated)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/107730/sibron-v-new-york/"
  cluster_id: 107730
  opinion_id: 9423756
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Related (cross-doctrine)"
  - page: "[[SIA Persons]]"
    role: "Related (cross-doctrine)"
related: ["[[Sibron v. New York]]", "[[Terry v. Ohio]]", "[[Henry v. United States (1959)]]", "[[Brinegar v. United States]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "probable-cause", "terry-stop", "burglary"]
holding: "Where probable cause to arrest existed (furtive conduct and flight indicating attempted burglary), the search of the suspect was valid as incident to a lawful arrest, even though the formal arrest followed the seizure."
lake:
  record_id: Peters v. New York
  status: verified
  projected_at: 2026-07-06
---

# Peters v. New York

*392 U.S. 40 (1968)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Off-duty New York City officer Lasky, at home, heard noises at his apartment door that led him to believe someone was trying to force entry. Looking through the peephole, he saw two men — strangers he had never seen in his twelve years in the building — tiptoeing furtively in the hallway. He telephoned the police, dressed, and entered the hall with his service revolver; the men immediately fled down the stairs. Lasky caught Peters between the fourth and fifth floors, patted down his clothing, and felt a hard object in an opaque envelope, which proved to be burglar's tools. Peters was convicted of possessing burglar's tools and moved to suppress them. The case was decided in the same opinion as *[[Sibron v. New York]]*.

## Issue
Whether the burglar's tools were lawfully seized — specifically, whether Officer Lasky had probable cause to arrest Peters, so that the search was valid as incident to a lawful arrest rather than as a *[[Terry v. Ohio|Terry]]* frisk.

## Rule
Yes. The search was justified as incident to a lawful arrest supported by probable cause. "We think, however, that for purposes of the Fourth Amendment the search was properly incident to a lawful arrest. By the time Officer Lasky caught up with Peters on the stairway between the fourth and fifth floors of the apartment building, he had probable cause to arrest him for attempted burglary." — 392 U.S. at 66. ^pin-66

Furtive conduct and flight can supply that probable cause: "deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of *mens rea*, and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors to be considered in the decision to make an arrest." — *Id.* at 66–67. ^pin-66b

When the arrest is complete on probable cause, the officer may search: "When the policeman grabbed Peters by the collar, he abruptly 'seized' him . . . on the basis of probable cause . . . . At that point he had the authority to search Peters, and the incident search was obviously justified 'by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime.'" — *Id.* at 67 (quoting *Preston v. United States*). ^pin-67

## Application
Lasky's observations — strange noises at his door, two strangers tiptoeing furtively about the hallway, their continued maneuvers, and their flight the moment he entered — supplied probable cause to arrest for attempted burglary; the Court observed it was "difficult to conceive of stronger grounds for an arrest, short of actual eyewitness observation of criminal activity." When Lasky grabbed Peters by the collar, the arrest was, for constitutional purposes, already complete on probable cause, so the ensuing search — reasonably limited and conducted primarily for weapons — was a lawful search incident to that arrest, and the burglar's tools were admissible.

## Conclusion
The search was valid as incident to a lawful arrest founded on probable cause, and the conviction was affirmed. *Peters* marks the other side of the line drawn in [[Sibron v. New York]]: where probable cause to arrest has developed, a full [[Search Incident to Arrest|search incident to arrest]] is permissible — unlike the unjustified pocket search condemned in *[[Sibron v. New York|Sibron]]*.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. Companion to [[Sibron v. New York]] and [[Terry v. Ohio]]; applies the probable-cause standard of [[Brinegar v. United States]] and [[Henry v. United States (1959)]] (the arrest is dated to the seizure on probable cause) and the search-incident rationale later associated with [[Chimel v. California]].

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Related (cross-doctrine)*
- [[SIA Persons]] — *Related (cross-doctrine)*

## Sources
- *Peters v. New York* (decided with *Sibron v. New York*), 392 U.S. 40 (1968) — https://www.courtlistener.com/opinion/107730/sibron-v-new-york/ — pinpoints: 66–67.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "b322374c0fe14587", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "392 U.S. 40 (1968)", "court": "U.S. Supreme Court", "neutral_cite": "1968 U.S. LEXIS 1346", "official_citation_present": true, "parallel_cite": "88 S. Ct. 1889; 20 L. Ed. 2d 917; 44 Ohio Op. 2d 402", "title": "Peters v. New York", "year": "1968"}}
{"assertion_id": "060017efb463f560", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where probable cause to arrest existed (furtive conduct and flight indicating attempted burglary), the search of the suspect was valid as incident to a lawful arrest, even though the formal arrest followed the seizure.", "title": "Peters v. New York"}}
{"assertion_id": "66bf12f8af5c4b58", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Related (cross-doctrine)", "title": "Peters v. New York"}}
{"assertion_id": "d871d3bf24b6ce3a", "dimension": "support", "kind": "home_role", "locator": {"home": "Terry Stops and Reasonable Suspicion"}, "payload": {"home": "Terry Stops and Reasonable Suspicion", "role": "Related (cross-doctrine)", "title": "Peters v. New York"}}
{"assertion_id": "147d97d77b2d72e8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1968-06-10", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Peters v. New York", "field_i_validity": "good_law", "scope_note": "Good law. Decided in the same opinion as Sibron v. New York (and companion to Terry v. Ohio): where probable cause to arrest existed, the search was valid as a search incident to a lawful arrest. opinion_id shared with Sibron (consolidated).", "title": "Peters v. New York", "varies_by_point": "false"}}
{"assertion_id": "cb0d26e63e808a5d", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Peters v. New York"}}
```

### lake record — Peters v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Peters v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Sibron v. New York",
    "case_name_short": "Sibron",
    "case_name_full": "Sibron v. New York",
    "input_case_name": "Peters v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1968-06-10",
    "year": 1968,
    "docket": null,
    "cluster_id": 107730,
    "lead_opinion_id": 9423756,
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
    "canonical_name_match": false,
    "alternates": [],
    "reason_code": "caption_mismatch_canonical"
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
      "id": "pin-66",
      "page": null,
      "quote": "--- # Peters v. New York *392 U.S. 40 (1968)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Off-duty New York City officer Lasky, at home, heard noises at his apartment door that led him to believe someone was trying to force entry. Looking through the peephole, he saw two men \u2014 strangers he had never seen in his twelve years in the building \u2014 tiptoeing furtively in the hallway. He telephoned the police, dressed, and entered the hall with his service revolver; the men immediately fled down the stairs. Lasky caught Peters between the fourth and fifth floors, patted down his clothing, and felt a hard object in an opaque envelope, which proved to be burglar's tools. Peters was convicted of possessing burglar's tools and moved to suppress them. The case was decided in the same opinion as *Sibron v. New York*. ## Issue Whether the burglar's tools were lawfully seized \u2014 specifically, whether Officer Lasky had probable cause to arrest Peters, so that the search was valid as incident to a lawful arrest rather than as a *Terry* frisk. ## Rule Yes. The search was justified as incident to a lawful arrest supported by probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-66b",
      "page": null,
      "quote": "deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of *mens rea*, and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors to be considered in the decision to make an arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-67",
      "page": null,
      "quote": "When the policeman grabbed Peters by the collar, he abruptly 'seized' him . . . on the basis of probable cause . . . . At that point he had the authority to search Peters, and the incident search was obviously justified 'by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime.'",
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
    "composite_basis_ref": "Peters v. New York",
    "varies_by_point": false,
    "scope_note": "Good law. Decided in the same opinion as Sibron v. New York (and companion to Terry v. Ohio): where probable cause to arrest existed, the search was valid as a search incident to a lawful arrest. opinion_id shared with Sibron (consolidated).",
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane1_negative"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
        "journal_ref": "Peters v. New York:lane2_top_cited"
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
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/peters-v-new-york.jsonl",
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
    "date_created": "2026-07-05T18:14:17Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "input caption does not match CL canonical caption",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T18:15:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T18:15:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T18:19:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T18:15:32Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Peters v. New York

```
<opinion type="majority">
<author id="b85-7">MR. Chief Justice Warren</author>
<p id="AlL">delivered the opinion of the Court.</p>
<p id="b85-8">These are companion cases to No. 67, <em>Terry </em>v. <em>Ohio, ante, </em>p. 1, decided today. They present related questions under the Fourth and Fourteenth Amendments, but the cases arise in the context of New York’s “stop-and-frisk” law, N. Y. Code Crim. Proc. § 180-a. This statute provides:</p>
<blockquote id="b85-9">“1. A police officer may stop any person abroad in a public place whom he reasonably suspects is committing, has committed or is about to commit a felony or any of the offenses specified in section five hundred fifty-two of this chapter, and may demand of him his name, address and an explanation of his actions.</blockquote>
<blockquote id="b85-10">“2. When a police officer has stopped a person for questioning pursuant to this section and reasonably <page-number citation-index="1" label="44">*44</page-number>suspects that he is in danger of life or limb, he may-search such person for a dangerous weapon. If the police officer finds such a weapon or any other thing the possession of which may constitute a crime, he may take and keep it until the completion of the questioning, at which time he shall either return it, if lawfully possessed, or arrest such person.”</blockquote>
<p id="b86-5">The appellants, Sibron and Peters, were both convicted of crimes in New York state courts on the basis of evidence seized from their persons by police officers. The Court of Appeals of New York held that the evidence was properly admitted, on the ground that the searches which uncovered it were authorized by the statute. <em>People </em>v. <em>Sibron, </em>18 N. Y. 2d 603, <span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">219 N. E. 2d 196</a></span>, 272 N. Y. S. 2d 374 (1966) (memorandum); <em>People </em>v. <em>Peters, </em>18 N. Y. 2d 238, <span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">219 N. E. 2d 595</a></span>, 273 N. Y. S. 2d 217 (1966). Sibron and Peters have appealed their convictions to this Court, claiming that §. 180-a is unconstitutional on its face and as construed and applied, because the searches and seizures which it was held to have authorized violated their rights under the Fourth Amendment, made applicable to the States by the Fourteenth. <em>Mapp </em>v. <em>Ohio, </em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961). We noted probable jurisdiction, <span class="citation multiple-matches"><a href="/c/U.%20S./386/954/">386 U. S. 954</a></span> (1967); <span class="citation multiple-matches"><a href="/c/U.%20S./386/980/">386 U. S. 980</a></span> (1967), and consolidated the two cases for argument with No. 67.</p>
<p id="b86-6">The facts in these cases may be stated briefly. Sibron, the appellant in No. 63, was convicted of the unlawful possession of heroin.<footnotemark>1</footnotemark> He moved before trial to suppress <page-number citation-index="1" label="45">*45</page-number>the heroin seized from his person by the arresting officer, Brooklyn Patrolman Anthony Martin. After the trial court denied his motion, Sibron pleaded guilty to the charge, preserving his right to appeal the evidentiary ruling.<footnotemark>2</footnotemark> At the hearing on the motion to suppress, Officer Martin testified that while he was patrolling his beat in uniform on March 9, 1965, he observed Sibron “continually from the hours of 4:00 P. M. to 12:00, midnight ... in the vicinity of 742 Broadway.” He stated that during this period of time he saw Sibron in conversation with six or eight persons whom he (Patrolman Martin) knew from past experience to be narcotics addicts. The officer testified that he did not overhear any of these conversations, and that he did not see anything pass between Sibron and any of the others. Late in the evening Sibron entered a restaurant. Patrolman Martin saw Sibron speak with three more known addicts inside the restaurant. Once again, nothing was overheard and nothing was seen to pass between Sibron and the addicts. Sibron sat down and ordered pie and coffee, and, as he was eating, Patrolman Martin approached him and told him to come outside. Once outside, the officer said to Sibron, “You know what I am after.” According to the officer, Sibron “mumbled something and reached into his pocket.” Simultaneously, Patrolman Martin thrust his hand into the same pocket, discovering several glassine envelopes, which, it turned out, contained heroin.</p>
<p id="b87-5">The State has had some difficulty in settling upon a <page-number citation-index="1" label="46">*46</page-number>theory for the admissibility of these envelopes of heroin. In his sworn complaint Patrolman Martin stated:</p>
<blockquote id="b88-5">“As the officer approached the defendant, the latter being in the direction of the officer and seeing him, he did put his hand in his left jacket pocket and pulled out a tinfoil envelope and did attempt to throw same to the ground. The officer never losing sight of the said envelope seized it from the def[endan]t’s left hand, examined it and found it to contain ten glascine [sic] envelopes with a white substance alleged to be Heroin.”</blockquote>
<p id="b88-6">This version of the encounter, however, bears very little resemblance to Patrolman Martin’s testimony at the hearing on the motion to suppress. In fact, he discarded the abandonment theory at the hearing.<footnotemark>3</footnotemark> Nor did the officer ever seriously suggest that he was in fear of bodily harm and that he searched Sibron in self-protection to find weapons.<footnotemark>4</footnotemark></p>
<p id="b89-3"><page-number citation-index="1" label="47">*47</page-number>The prosecutor’s theory at the hearing was that Patrolman Martin had probable cause to believe that Sibron was in possession of narcotics because he had seen him conversing with a number of known addicts over an eight-hour period. In the absence of any knowledge on Patrolman Martin’s part concerning the nature of the intercourse between Sibron and the addicts, however, the trial court was inclined to grant the motion to suppress. As the judge stated, “All he knows about the unknown men: They are narcotics addicts. They might have been talking about the World Series. They might have been talking about prize fights.” The prosecutor, however, reminded the judge that Sibron had admitted on the stand, in Patrolman Martin’s absence, that he had been talking to the addicts about narcotics. Thereupon, the trial judge changed his mind and ruled that the officer had probable cause for an arrest.</p>
<p id="b89-4">Section 180-a, the “stop-and-frisk” statute, was not mentioned at any point in the trial court. The Appellate Term of the Supreme Court affirmed the conviction without opinion. In the Court of Appeals of New York, Sibron’s case was consolidated with the <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>case, No. 74. The Court of Appeals held that the search in <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>was justified under the statute, but it wrote no opinion in Sibron’s case. The dissents of Judges Fuld and Van Voorhis, however, indicate that the court rested its holding on § 180-a. At any rate, in its Brief in Oppo<page-number citation-index="1" label="48">*48</page-number>sition to the Jurisdictional Statement in this Court, the State sought to justify the search on the basis of the statute. After we noted probable jurisdiction, the District Attorney for Kings County confessed error.</p>
<p id="b90-6">Peters, the appellant in No. 74, was convicted of possessing burglary tools under circumstances evincing an intent to employ them in the commission of a crime.<footnotemark>5</footnotemark> The tools were seized from his person at the time of his arrest, and like Sibron he made a pretrial motion to suppress them. When the trial court denied the motion, he too pleaded guilty, preserving his right to appeal. Officer Samuel Lasky of the New York City Police Department testified at the hearing on the motion that he was at home in his apartment in Mount Vernon, New York, at about 1 p. m. on July 10, 1964. He had just finished taking a shower and was drying himself when he heard a noise at his door. His attempt to investigate was interrupted by a telephone call, but when he returned and looked through the peephole into the hall, Officer Lasky saw “two men tiptoeing out of the alcove toward the stairway.” He immediately called the police, put on some civilian clothes and armed himself with his service revolver. Returning to the peephole, he saw “a tall man tiptoeing away from the alcove and followed by this shorter man, Mr. Peters, toward the stairway.” Officer Lasky testified that he had lived in the 120-unit building for 12 years and that he did not recognize either of the men as tenants. Believing that he had happened upon the two men in the course of an attempted burglary,<footnotemark>6</footnotemark> <page-number citation-index="1" label="49">*49</page-number>Officer Lasky opened his door, entered the hallway and slammed the door loudly behind him. This precipitated a flight down the stairs on the part of the two men,<footnotemark>7</footnotemark> and Officer Lasky gave chase. His apartment was located on the sixth floor, and he apprehended Peters between the fourth and fifth floors. Grabbing Peters by the collar, he continued down another flight in unsuccessful pursuit of the other man. Peters explained his presence in the building to Officer Lasky by saying that he was visiting a girl friend. However, he declined to reveal the girl friend’s name, on the ground that she was a married woman. Officer Lasky patted Peters down for weapons, and discovered a hard object in his pocket. He stated at the hearing that the object did not feel like a gun, but that it might have been a knife. He removed the object from Peters’ pocket. It was an opaque plastic envelope, containing burglar’s tools.</p>
<p id="b91-5">The trial court explicitly refused to credit Peters’ testimony that he was merely in the building to visit his girl friend. It found that Officer Lasky had the requisite “reasonable suspicion” of Peters under § 180-a to stop him and question him. It also found that Peters’ response was “clearly unsatisfactory,” and that “under <page-number citation-index="1" label="50">*50</page-number>the circumstances Lasky’s action in frisking Peters for a dangerous weapon was reasonable, even though Lasky was himself armed.” It held that the hallway of the apartment building was a “public place” within the meaning of the statute. The Appellate Division of the Supreme Court affirmed without opinion. The Court of Appeals also affirmed, essentially adopting the reasoning of the trial judge, with Judges Fuld and Van Voorhis dissenting separately.</p>
<p id="b92-6">I.</p>
<p id="b92-7">At the outset we must deal with the question whether we have jurisdiction in No. 63. It is asserted that because Sibron has completed service of the six-month sentence imposed upon him as a result of his conviction, the case has become moot under <em>St. Pierre </em>v. <em>United States, </em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">319 U. S. 41</a></span> (1943).<footnotemark>8</footnotemark> We have concluded that the case is not moot.</p>
<p id="b93-4"><page-number citation-index="1" label="51">*51</page-number>In the first place, it is clear that the broad dictum with which the Court commenced its discussion in <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>— that “the case is moot because, after petitioner’s service of his sentence and its expiration, there was no longer a subject matter on which the judgment of this Court could operate” (<span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#42" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 42</a></span>) — fails to take account of significant qualifications recognized in <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>and developed in later cases. Only a few days ago we held unanimously that the writ of habeas corpus was available to test the constitutionality of a state conviction where the petitioner had been in custody when he applied for the writ, but had been released before this Court could adjudicate his claims. <em>Carafas </em>v. <em>LaVallee, </em><span class="citation" data-id="9423702"><a href="/opinion/107689/carafas-v-lavallee/" aria-description="Citation for case: Carafas v. LaVallee">391 U. S. 234</a></span> (1968). On numerous occasions in the past this Court has proceeded to adjudicate the merits of criminal cases in which the sentence had been fully served or the probationary period during which a suspended sentence could be reimposed had terminated. <em>Ginsberg </em>v. <em>New York, </em><span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629</a></span> (1968); <em>Pollard </em>v. <em>United States, </em><span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/" aria-description="Citation for case: Pollard v. United States">352 U. S. 354</a></span> (1957); <em>United States </em>v. <em>Morgan, </em><span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">346 U. S. 502</a></span> (1954); <em>Fiswick </em>v. <em>United States, </em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211</a></span> (1946). Thus mere release of the prisoner does not mechanically foreclose consideration of the merits by this Court.</p>
<p id="b93-5"><em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>itself recognized two possible exceptions to its “doctrine” of mootness, and both of them appear to us to be applicable here. The Court stated that “[i]t does not appear that petitioner could not have brought his case to this Court for review before the expiration of his sentence,” noting also that because the petitioner’s conviction was for contempt and because his controversy with the Government was a continuing one, there was a good chance that there would be “ample opportunity to review” the important question presented on the merits in a future proceeding. <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. This <page-number citation-index="1" label="52">*52</page-number>was a plain recognition of the vital importance of keeping open avenues of judicial review of deprivations of constitutional right.<footnotemark>9</footnotemark> There was no way for Sibron to bring his case here before his six-month sentence expired. By statute he was precluded from obtaining bail pending appeal,<footnotemark>10</footnotemark> and by virtue of the inevitable delays of the New York court system, he was released less than a month after his newly appointed appellate counsel had been supplied with a copy of the transcript and roughly two months before it was physically possible to present his case to the first tier in the state appellate court system.<footnotemark>11</footnotemark> This was true despite the fact that he took all steps to perfect his appeal in a prompt, diligent, and timely manner.</p>
<p id="b94-6">Many deep and abiding constitutional problems are encountered primarily at a level of “low visibility” in the criminal process — in the context of prosecutions for “minor” offenses which carry only short sentences.<footnotemark>12</footnotemark> We do not believe that the Constitution contemplates that <page-number citation-index="1" label="53">*53</page-number>people deprived of constitutional rights at this level should be left utterly remediless and defenseless against repetitions of unconstitutional conduct. A State may not cut off federal review of whole classes of such cases by the simple expedient of a blanket denial of bail pending appeal. As <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>clearly recognized, a State may not effectively deny a convict access to its appellate courts until he has been released and then argue that his case has been mooted by his failure to do what it alone prevented him from doing.<footnotemark>13</footnotemark></p>
<p id="b95-5">The second exception recognized in <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>permits adjudication of the merits of a criminal case where “under either state or federal law further penalties or disabilities can be imposed ... as a result of the judgment which <page-number citation-index="1" label="54">*54</page-number>has . . . been satisfied.” <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. Subsequent cases have expanded this exception to the point where it may realistically be said that inroads have been made upon the principle itself. <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>implied that the burden was upon the convict to show the existence of collateral legal consequences. Three years later in <em>Fiswick </em>v. <em>United States, </em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211</a></span> (1946), however, the Court held that a criminal case had not become moot upon release of the prisoner, noting that the convict, an alien, might be subject to deportation for having committed a crime of “moral turpitude” — even though it had never been held (and the Court refused to hold) that the crime of which he was convicted fell into this category. The Court also pointed to the fact that if the petitioner should in the future decide he wanted to become an American citizen, he might have difficulty proving that he was of “good moral character.” <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#222" aria-description="Citation for case: Fiswick v. United States"><em>Id., </em>at 222</a></span>.<footnotemark>14</footnotemark></p>
<p id="b96-4">The next case which dealt with the problem of collateral consequences was <em>United States </em>v. <em>Morgan, </em><span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">346 U. S. 502</a></span> (1954). There the convict had probably been subjected to a higher sentence as a recidivist by a state court on account of the old federal conviction which he sought to attack. But as the dissent pointed out, there was no indication that the recidivist increment would be removed from his state sentence upon invalidation of the federal conviction, <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#516" aria-description="Citation for case: United States v. Morgan"><em>id., </em>at 516, n. 4</a></span>, and the Court chose to rest its holding that the case was not moot upon <page-number citation-index="1" label="55">*55</page-number>a broader view of the matter. Without canvassing the possible disabilities which might be imposed upon Morgan or alluding specifically to the recidivist sentence, the Court stated:</p>
<blockquote id="b97-5">“Although the term has been served, the results of the conviction may persist. Subsequent convictions may carry heavier penalties, civil rights may be affected. As the power to remedy an invalid sentence exists, we think, respondent is entitled to an opportunity to attempt to show that this conviction was invalid.” <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#512" aria-description="Citation for case: United States v. Morgan"><em>Id., </em>at 512-513</a></span>.</blockquote>
<p id="b97-6">Three years later, in <em>Pollard </em>v. <em>United States, </em><span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/" aria-description="Citation for case: Pollard v. United States">352 U. S. 354</a></span> (1957), the Court abandoned all inquiry into the actual existence of specific collateral consequences and in effect presumed that they existed. With nothing more than citations to <em><span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/" aria-description="Citation for case: United States v. Morgan">Morgan</a></span> </em>and <em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">Fiswick</a></span>, </em>and a statement that “convictions may entail collateral legal disadvantages in the future,” <span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#358" aria-description="Citation for case: Fiswick v. United States"><em>id., </em>at 358</a></span>, the Court concluded that “[t]he possibility of consequences collateral to the imposition of sentence is sufficiently substantial to justify our dealing with the merits.” <em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/" aria-description="Citation for case: Fiswick v. United States">Ibid.</a></span> </em>The Court thus acknowledged the obvious fact of life that most criminal convictions do in fact entail adverse collateral legal consequences.<footnotemark>15</footnotemark> The mere “possibility” that this will be the case is enough to preserve a criminal case from ending “ignominiously in the limbo of mootness.” <em>Parker </em>v. <em>Ellis, </em><span class="citation" data-id="9421986"><a href="/opinion/106050/parker-v-ellis/#577" aria-description="Citation for case: Parker v. Ellis">362 U. S. 574, 577</a></span> (1960) (dissenting opinion).</p>
<p id="b97-7">This case certainly meets that test for survival. Without pausing to canvass the possibilities in detail, we note that New York expressly provides by statute that Sibron’s conviction may be used to impeach his character should he choose to put it in issue at any future <page-number citation-index="1" label="56">*56</page-number>criminal trial, N. Y. Code Crim. Proc. § 393-e, and that it must be submitted to a trial judge for his consideration in sentencing should Sibron again be convicted of a crime, N. Y. Code Crim. Proc. § 482. There are doubtless other collateral consequences. Moreover, we see no relevance in the fact that Sibron is a multiple offender. Morgan was a multiple offender, see <span class="citation" data-id="9421014"><a href="/opinion/105176/united-states-v-morgan/#503" aria-description="Citation for case: United States v. Morgan">346 U. S. at 503-504</a></span>, and so was Pollard, see <span class="citation" data-id="9421375"><a href="/opinion/105450/pollard-v-united-states/#355" aria-description="Citation for case: Pollard v. United States">352 U. S., at 355-357</a></span>. A judge or jury faced with a question of character, like a sentencing judge, may be inclined to forgive or at least discount a limited number of minor transgressions, particularly if they occurred at some time in the relatively distant past.<footnotemark>16</footnotemark> It is impossible for this Court to say at what point the number of convictions on a man’s record renders his reputation irredeemable.<footnotemark>17</footnotemark> And even if we believed that an individual had reached that point, it would be impossible for us to say that he had no interest in beginning the process of redemption with the particular case sought to be adjudicated. We cannot foretell what opportunities might present themselves in the future for the removal of other convictions from an individual’s record. The question of the validity of a criminal conviction can arise in many contexts, compare <em>Burgett </em>v. <em>Texas, </em><span class="citation" data-id="9423521"><a href="/opinion/107540/burgett-v-texas/" aria-description="Citation for case: Burgett v. Texas">389 U. S. 109</a></span> (1967), and the sooner the issue is fully litigated the better for all concerned. It is always preferable to litigate a matter <page-number citation-index="1" label="57">*57</page-number>when it is directly and principally in dispute, rather than in a proceeding where it is collateral to the central controversy. Moreover, litigation is better conducted when the dispute is fresh and additional facts may, if necessary, be taken without a substantial risk that witnesses will die or memories fade. And it is far better to eliminate the source of a potential legal disability than to require the citizen to suffer the possibly unjustified consequences of the disability itself for an indefinite period of time before he can secure adjudication of the State’s right to impose it on the basis of some past action. Cf. <em>Peyton </em>v. <em>Rowe, </em><span class="citation" data-id="107679"><a href="/opinion/107679/peyton-v-rowe/#64" aria-description="Citation for case: Peyton v. Rowe">391 U. S. 54, 64</a></span> (1968).<footnotemark>18</footnotemark></p>
<p id="b99-5">None of the concededly imperative policies behind the constitutional rule against entertaining moot controversies would be served by a dismissal in this case. There is nothing abstract, feigned, or hypothetical about Sibron’s appeal. Nor is there any suggestion that either Sibron or the State has been wanting in diligence or fervor in the litigation. We have before us a fully developed record of testimony about contested historical facts, which reflects the “impact of actuality” <footnotemark>19</footnotemark> to a far greater degree than many controversies accepted for adjudication as a matter of course under the Federal Declaratory Judgment Act, <span class="citation no-link">28 U. S. C. § 2201</span>.</p>
<p id="b99-6"><em>St. Pierre </em>v. <em>United States, supra, </em>must be read in light of later cases to mean that a criminal case is moot only if it is shown that there is no possibility that any collateral legal consequences will be imposed on the basis of the challenged conviction. That certainly is not <page-number citation-index="1" label="58">*58</page-number>the ease here. Sibron “has a substantial stake in the judgment of conviction which survives the satisfaction of the sentence imposed on him.” <em>Fiswick </em>v. <em>United States, supra, </em>at 222. The case is not moot.</p>
<p id="b100-6">II.</p>
<p id="b100-7">We deal next with the confession of error by the District Attorney for Kings County in No. 63. Confessions of error are, of course, entitled to and given great weight, but they do not “relieve this Court of the performance of the judicial function.” <em>Young </em>v. <em>United States, </em><span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/#258" aria-description="Citation for case: Young v. United States">315 U. S. 257, 258</a></span> (1942). It is the uniform practice of this Court to conduct its own examination of the record in all cases where the Federal Government or a State confesses that a conviction has been erroneously obtained. For one thing, as we noted in <em><span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/" aria-description="Citation for case: Young v. United States">Young</a></span>, </em>“our judgments are precedents, and the proper administration of the criminal law cannot be left merely to the stipulation of parties.” <span class="citation" data-id="103610"><a href="/opinion/103610/young-v-united-states/#259" aria-description="Citation for case: Young v. United States">315 U. S., at 259</a></span>. See also <em>Marino </em>v. <em>Ragen, </em><span class="citation" data-id="9420073"><a href="/opinion/104487/marino-v-ragen/" aria-description="Citation for case: Marino v. Ragen">332 U. S. 561</a></span> (1947). This consideration is entitled to special weight where, as in this case, we deal with a judgment of a State’s highest court interpreting a state statute which is challenged on constitutional grounds. The need for such authoritative declarations of state law in sensitive constitutional contexts has been the very reason for the development of the abstention doctrine by this Court. See, <em>e. g., Railroad Comm’n </em>v. <em>Pullman Co., </em><span class="citation" data-id="103481"><a href="/opinion/103481/railroad-commn-of-tex-v-pullman-co/" aria-description="Citation for case: Railroad Comm&#x27;n of Tex. v. Pullman Co.">312 U. S. 496</a></span> (1941). Such a judgment is the final product of a sovereign judicial system, and is deserving of respectful treatment by this Court. Moreover, in this case the confession of error on behalf of the entire state executive and judicial branches is made, not by a state official, but by the elected legal officer of one political subdivision within the State. The District Attorney for Kings County seems to have come late to the opinion that this conviction violated Sibron’s constitutional <page-number citation-index="1" label="59">*59</page-number>rights. For us to accept his view blindly in the circumstances, when a majority of the Court of Appeals of New York has expressed the contrary view, would be a disservice to the State of New York and an abdication of our obligation to lower courts to decide cases upon proper constitutional grounds in a manner which permits them to conform their future behavior to the demands of the Constitution. We turn to the merits.</p>
<p id="b101-5">III.</p>
<p id="b101-6">The parties on both sides of these two cases have urged that the principal issue before us is the constitutionality of § 180-a “on its face.” We decline, however, to be drawn into what we view as the abstract and unproductive exercise of laying the extraordinarily elastic categories of § 180-a next to the categories of the Fourth Amendment in an effort to determine whether the two are in some sense compatible. The constitutional validity of a warrantless search is pre-eminently the sort of question which can only be decided in the concrete factual context of the individual case. In this respect it is quite different from the question of the adequacy of the procedural safeguards written into a statute which purports to authorize the issuance of search warrants in certain circumstances. See <em>Berger </em>v. <em>New York, </em><span class="citation" data-id="9423459"><a href="/opinion/107483/berger-v-new-york/" aria-description="Citation for case: Berger v. New York">388 U. S. 41</a></span> (1967). No search required to be made under a warrant is valid if the procedure for the issuance of the warrant is inadequate to ensure the sort of neutral contemplation by a magistrate of the grounds for the search and its proposed scope, which lies at the heart of the Fourth Amendment. <em>E. g., Aguilar </em>v. <em>Texas, </em><span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964); <em>Giordenello </em>v. <em>United States, </em><span class="citation" data-id="9421690"><a href="/opinion/105748/giordenello-v-united-states/" aria-description="Citation for case: Giordenello v. United States">357 U. S. 480</a></span> (1958). This Court held last Term in <em>Berger </em>v. <em>New York, supra, </em>that N. Y. Code Crim Proc. § 813-a, which established a procedure for the issuance of search warrants to permit electronic eavesdropping, failed to <page-number citation-index="1" label="60">*60</page-number>embody the safeguards demanded by the Fourth and Fourteenth Amendments.</p>
<p id="b102-6">Section 180-a, unlike § 813-a, deals with the substantive validity of certain types of seizures and searches without warrants. It purports to authorize police officers to “stop” people, “demand” explanations of them and “search [them] for dangerous weapon [s]” in certain circumstances upon “reasonable suspicion” that they are engaged in criminal activity and that they represent a danger to the policeman. The operative categories of § 180-a are not the categories of the Fourth Amendment, and they are susceptible of a wide variety of interpretations.<footnotemark>20</footnotemark> New York is, of course, free to develop its own <page-number citation-index="1" label="61">*61</page-number>law of search and seizure to meet the needs of local law enforcement, see <em>Ker </em>v. <em>California, </em><span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/#34" aria-description="Citation for case: Ker v. California">374 U. S. 23, 34</a></span> (1963), and in the process it may call the standards it employs by any names it may choose. It may not, however, authorize police conduct which trenches upon Fourth Amendment rights, regardless of the labels which it attaches to such conduct. The question in this Court upon review of a state-approved search or seizure “is not whether the search [or seizure] was authorized by state law. The question is rather whether the search was reasonable under the Fourth Amendment. Just as a search authorized by state law may be an unreasonable one under that amendment, so may a search not expressly authorized by state law be justified as a constitutionally reasonable one.” <em>Cooper </em>v. <em>California, </em><span class="citation" data-id="9423351"><a href="/opinion/107360/cooper-v-california/#61" aria-description="Citation for case: Cooper v. California">386 U. S. 58, 61</a></span> (1967).</p>
<p id="b103-5">Accordingly, we make no pronouncement on the facial constitutionality of § 180-a. The constitutional point <page-number citation-index="1" label="62">*62</page-number>with respect to a statute of this peculiar sort, as the Court of Appeals of New York recognized, is “not so much . . . the language employed as . . . the conduct it authorizes.” <em>People </em>v. <em>Peters, </em>18 N. Y. 2d 238, 245, <span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/#599" aria-description="Citation for case: People v. Peters">219 N. E. 2d 595, 599</a></span>, 273 N. Y. S. 2d 217, 222 (1966). We have held today in <em>Terry </em>v. <em>Ohio, ante, </em>p. 1, that police conduct of the sort with which § 180-a deals must be judged under the Reasonable Search and Seizure Clause of the Fourth Amendment. The inquiry under that clause may differ sharply from the inquiry set up by the categories of § 180-a. Our constitutional inquiry would not be furthered here by an attempt to pronounce judgment on the words of the statute. We must confine our review instead to the reasonableness of the searches and seizures which underlie these two convictions.</p>
<p id="b104-4">IV.</p>
<p id="b104-5">Turning to the facts of Sibron’s case, it is clear that the heroin was inadmissible in evidence against him. The prosecution has quite properly abandoned the notion that there was probable cause to arrest Sibron for any crime at the time Patrolman Martin accosted him in the restaurant, took him outside and searched him. The officer was not acquainted with Sibron and had no information concerning him. He merely saw Sibron talking to a number of known narcotics addicts over a period of eight hours. It must be emphasized that Patrolman Martin was completely ignorant regarding the content .of these conversations, and that he saw nothing pass between Sibron and the addicts. So far as he knew, they might indeed “have been talking about the World Series.” The inference that persons who talk to narcotics addicts are engaged in the criminal traffic in narcotics is simply not the sort of reasonable inference required to support an intrusion by the police upon an individual’s personal security. Nothing resembling probable cause existed <page-number citation-index="1" label="63">*63</page-number>until after the search had turned up the envelopes of heroin. It is axiomatic that an incident search may not precede an arrest and serve as part of its justification. <em>E. g., Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/" aria-description="Citation for case: Henry v. United States">361 U. S. 98</a></span> (1959); <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#16" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 16-17</a></span> (1948). Thus the search cannot be justified as incident to a lawful arrest.</p>
<p id="b105-5">If Patrolman Martin lacked probable cause for an arrest, however, his seizure and search of Sibron might still have been justified at the outset if he had reasonable grounds to believe that Sibron was armed and dangerous. <em>Terry </em>v. <em>Ohio, ante, </em>p. 1. We are not called- upon to decide in this case whether there was a “seizure” of Sibron inside the restaurant antecedent to the physical seizure which accompanied the search. The record is unclear with respect to what transpired between Sibron and the officer inside the restaurant. It is totally barren of any indication whether Sibron accompanied Patrolman Martin outside in submission to a show of force or authority which left him no choice, or whether he went voluntarily in a spirit of apparent cooperation with the officer’s investigation. In any event, this deficiency in the record is immaterial, since Patrolman Martin obtained no new information in the interval between his initiation of the encounter in the restaurant and his physical seizure and search of Sibron outside.</p>
<p id="b105-6">Although the Court of Appeals of New York wrote no opinion in this case, it seems to have viewed the search here as a self-protective search for weapons and to have affirmed on the basis of § 180-a, which authorizes such a search when the officer “reasonably suspects that he is in danger of life or limb.” The Court of Appeals has, at any rate, justified searches during field interrogation on the ground that “[t]he answer to the question propounded by the policeman may be a <page-number citation-index="1" label="64">*64</page-number>bullet; in any case the exposure to danger could be very great.” <em>People </em>v. <em>Rivera, </em>14 N. Y. 2d 441, 446, <span class="citation" data-id="5521257"><a href="/opinion/5673750/people-v-rivera/#35" aria-description="Citation for case: People v. Rivera">201 N. E. 2d 32, 35</a></span>, 252 N. Y. S. 2d 458, 463 (1964), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./379/978/">379 U. S. 978</a></span> (1965). But the application of this reasoning to the facts of this case proves too much. The police officer is not entitled to seize and search every person whom he sees on the street or of whom he makes inquiries. Before he places a hand on the person of a citizen in search of anything, he must have constitutionally adequate, reasonable grounds for doing so. In the case of the self-protective search for weapons, he must be able to point to particular facts from which he reasonably inferred that the individual was armed and dangerous. <em>Terry </em>v. <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio, supra.</a></span> </em>Patrolman Martin's testimony reveals no such facts. The suspect’s mere act of talking with a number of known narcotics addicts over an eight-hour period no more gives rise to reasonable fear of life or limb on the part of the police officer than it justifies an arrest for committing a crime. Nor did Patrolman Martin urge that when Sibron put his hand in his pocket, he feared that he was going for a weapon and acted in self-defense. His opening statement to Sibron — “You know what I am after” — made it abundantly clear that he sought narcotics, and his testimony at the hearing left no doubt that he thought there were narcotics in Sibron’s pocket.<footnotemark>21</footnotemark></p>
<p id="b107-4"><page-number citation-index="1" label="65">*65</page-number>Even assuming <em>arguendo </em>that there were adequate grounds to search Sibron for weapons, the nature and scope of the search conducted by Patrolman Martin were so clearly unrelated to that justification as to render the heroin inadmissible. The search for weapons approved in <em>Terry </em>consisted solely of a limited patting of the outer clothing of the suspect for concealed objects which might be used as instruments of assault. Only when he discovered such objects did the officer in <em>Terry </em>place his hands in the pockets of the men he searched. In this case, with no attempt at an initial limited exploration for arms, Patrolman Martin thrust his hand into Sibron’s pocket and took from him envelopes of heroin. His testimony shows that he was looking for narcotics, and he found them. The search was not reasonably limited in scope to the accomplishment of the only goal which might conceivably have justified its inception — the protection of the officer by disarming a potentially dangerous man. Such a search violates the guarantee of the Fourth <page-number citation-index="1" label="66">*66</page-number>Amendment, which protects the sanctity of the person against unreasonable intrusions on the part of all government agents.</p>
<p id="b108-6">V.</p>
<p id="b108-7">We think it is equally clear that the search in Peters’ case was wholly reasonable under the Constitution. The Court of Appeals of New York held that the search was made legal by § 180-a, since Peters was “abroad in a public place,” and since Officer Lasky was reasonably suspicious of his activities and, once he had stopped Peters, reasonably suspected that he was in danger of life or limb, even though he held Peters at gun point. This may be the justification for the search under state law. We think, however, that for purposes of the Fourth Amendment the search was properly incident to a lawful arrest. By the time Officer Lasky caught up with Peters on the stairway between the fourth and fifth floors of the apartment building, he had probable cause to arrest him for attempted burglary. The officer heard strange noises at his door which apparently led him to believe that someone sought to force entry. When he investigated these noises he saw two men, whom he had never seen before in his 12 years in the building, tiptoeing furtively about the hallway. They were still engaged in these maneuvers after he called the police and dressed hurriedly. And when Officer Lasky entered the hallway, the men fled down the stairs. It is difficult to conceive of stronger grounds for an arrest, short of actual eyewitness observation of criminal activity. As the trial court explicitly recognized,<footnotemark>22</footnotemark> deliberately furtive actions and flight at the approach of strangers or law officers are strong indicia of <em>mens rea, </em>and when coupled with specific knowledge on the part of the officer relating the suspect to the evidence of crime, they are proper factors <page-number citation-index="1" label="67">*67</page-number>to be considered in the decision to make an arrest. <em>Brinegar </em>v. <em>United States, </em><span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160</a></span> (1949); <em>Husty </em>v. <em>United States, </em><span class="citation" data-id="101682"><a href="/opinion/101682/husty-v-united-states/" aria-description="Citation for case: Husty v. United States">282 U. S. 694</a></span> (1931); see <em>Henry </em>v. <em>United States, </em><span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#103" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 103</a></span> (1959).</p>
<p id="b109-5">As we noted in Sibron’s case, a search incident to a lawful arrest may not precede the arrest and serve as part of its justification. It is a question of fact precisely when, in each case, the arrest took place. <em>Rios </em>v. <em>United States, </em><span class="citation" data-id="106108"><a href="/opinion/106108/rios-v-united-states/#261" aria-description="Citation for case: Rios v. United States">364 U. S. 253, 261-262</a></span> (1960). And while there was some inconclusive discussion in the trial court concerning when Officer Lasky “arrested” Peters, it is clear that the arrest had, for purposes of constitutional justification, already taken place before the search commenced. When the policeman grabbed Peters by the collar, he abruptly “seized” him and curtailed his freedom of movement on the basis of probable cause to believe that he was engaged in criminal activity. See <em>Henry </em>v. <em>United States, supra, </em>at 103. At that point he had the authority to search Peters, and the incident search was obviously justified “by the need to seize weapons and other things which might be used to assault an officer or effect an escape, as well as by the need to prevent the destruction of evidence of the crime.” <em>Preston </em>v. <em>United States, </em><span class="citation" data-id="106771"><a href="/opinion/106771/preston-v-united-states/#367" aria-description="Citation for case: Preston v. United States">376 U. S. 364, 367</a></span> (1964). Moreover, it was reasonably limited in scope by these purposes. Officer Lasky did not engage in an unrestrained and thoroughgoing examination of Peters and his personal effects. He seized him to cut short his flight, and he searched him primarily for weapons. While patting down his outer clothing, Officer Lasky discovered an object in his pocket which might have been used as a weapon. He seized it and discovered it to be a potential instrument of the crime of burglary.</p>
<p id="b109-6">We have concluded that Peters’ conviction fully comports with the commands of the Fourth and Fourteenth Amendments, and must be affirmed. The conviction in <page-number citation-index="1" label="68">*68</page-number>No. 63, however, must be reversed, on the ground that the heroin was unconstitutionally admitted in evidence against the appellant.</p>
<p id="b110-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b86-7"> N. Y. Pub. Health Law § 3305 makes the unauthorized possession of any narcotic drug unlawful, and §§ <em>1751 </em>and 1751-a of the <em>N. </em>Y. Penal Law of 1909, then in effect, made the grade of the offense depend upon the amount of the drugs found in the possession of the defendant. The complaint in this case originally charged a felony, but the trial court granted the prosecutor’s motion to reduce the <page-number citation-index="1" label="45">*45</page-number>charge on the ground that “the Laboratory report will indicate a misdemeanor charge.” Sibron was convicted of a misdemeanor and sentenced to six months in jail.</p>
</footnote>
<footnote label="2">
<p id="b87-7"> N. Y. Code Crim. Proc. § 813-e provides that an order denying a motion to suppress evidence in a criminal case “may be reviewed on appeal from a judgment of conviction notwithstanding the fact that such judgment of conviction is predicated upon a plea of guilty.”</p>
</footnote>
<footnote label="3">
<p id="b88-7"> Patrolman Martin stated several times that he put his hand into Sibron’s pocket and seized the heroin before Sibron had any opportunity to remove his own hand from the pocket. The trial court questioned him on this point:</p>
<blockquote id="b88-8">“Q. Would you say at that time that he reached into his pocket and handed the packets to you? Is that what he did or did he drop the packets?</blockquote>
<blockquote id="b88-9">“A. He did not drop them. <em>I do not know what his intentions were. </em>He pushed his hand into his pocket.</blockquote>
<blockquote id="b88-10">“MR. Joseph [Prosecutor]: You intercepted it; didn’t you, Officer?</blockquote>
<blockquote id="b88-11">“The Witness: Yes.” (Emphasis added.)</blockquote>
<p id="b88-12">It is of course highly unlikely that Sibron, facing the officer at such close quarters, would have tried to remove the heroin from his pocket and throw it to the ground in the hope that he could escape responsibility for it.</p>
</footnote>
<footnote label="4">
<p id="b88-13"> The possibility that Sibron, who never, so far as appears from the record, offered any resistance, might have posed a danger to <page-number citation-index="1" label="47">*47</page-number>Patrolman Martin’s safety was never even discussed as a potential justification for the search. The only mention of weapons by the officer in his entire testimony came in response to a leading question by Sibron’s counsel, when Martin stated that he “thought he [Sibron] might have been” reaching for a gun. Even so, Patrolman Martin did not accept this suggestion by the opposition regarding the reason for his action; the discussion continued upon the plain premise that he had been looking for narcotics all the time.</p>
</footnote>
<footnote label="5">
<p id="b90-7"><em> </em>N. Y. Pen. Law of 1909, § 408, made the possession of such tools under such circumstances a misdemeanor for first offenders and a felony for all those who have “been previously convicted of any crime.” Peters was convicted of a felony under this section.</p>
</footnote>
<footnote label="6">
<p id="b90-8"> Officer Lasky testified that when he called the police immediately before leaving his apartment, he “told the Sergeant at the desk that two burglars were on my floor.”</p>
</footnote>
<footnote label="7">
<p id="b91-6"> Officer Lasky testified that when he emerged from his apartment, “I slammed the door, I had my gun and I ran down the stairs after them.” A sworn affidavit of the Assistant District Attorney, which was before the trial court when it ruled on the motion to suppress, stated that when apprehended Peters was “fleeing down the steps of the building.” The trial court explicitly took note of the flight of Peters and his companion as a factor contributing to Officer Lasky’s “reasonable suspicion” of them:</p>
<blockquote id="b91-7">“We think the testimony at the hearing does not require further laboring of this aspect of the matter, unless one is to believe that it is legitimately normal for a man to tip-toe about in the public hall of an apartment house while on a visit to his unidentified girl-friend, and, when observed by another tenant, to rapidly descend by stairway in the presence of elevators.”</blockquote>
</footnote>
<footnote label="8">
<p id="b92-8"> The first suggestion of mootness in this case came upon oral argument, when it was revealed for the first time that appellant had been released. This fact did not appear in the record, despite the fact that the release occurred well over two years before the case was argued here. Nor was mootness hinted at by the State in its Brief in Opposition to the Jurisdictional Statement in this Court— where it took the position that the decision below was so clearly right that it did not merit further review — or in its brief on the merits — in which it conceded that the decision below clearly violated Sibron’s constitutional rights and urged that it was an aberrant interpretation which should not impair the constitutionality of the New York statute. Following the suggestion of mootness on oral argument, moreover, the State filed a brief in which it amplified its views as to why the case should be held moot, but added the extraordinary suggestion that this Court should ignore the problem and pronounce upon the constitutionality of a statute in a case which has become moot. Normally in these circumstances we would consider ourselves fully justified in foreclosing a party upon an issue; however, since the question goes to the very existence of a controversy for us to adjudicate, we have undertaken to review it.</p>
</footnote>
<footnote label="9">
<p id="b94-7"> Cf. <em>Fay </em>v. <em>Noia, </em><span class="citation" data-id="9422554"><a href="/opinion/106548/fay-v-noia/#424" aria-description="Citation for case: Fay v. Noia">372 U. S. 391, 424</a></span> (1963):</p>
<blockquote id="b94-8">“[C]onventional notions of finality in criminal litigation cannot be permitted to defeat the manifest federal policy that federal constitutional rights of personal liberty shall not be denied without the fullest opportunity for plenary federal judicial review/'</blockquote>
</footnote>
<footnote label="10">
<p id="b94-9"> See N. Y. Code Crim. Proc. § 555 subd. 2.</p>
</footnote>
<footnote label="11">
<p id="b94-10"> Sibron was arrested on March 9, 1965, and was unable to make bail before trial because of his indigency. He thus remained in jail from that time until the expiration of his sentence (with good time credit) on July 10, 1965. He was convicted on April 23. His application for leave to proceed <em>in forma pauperis </em>was not granted until May 14, and his assigned appellate counsel was not provided with a transcript until June 11. The Appellate Term of the Supreme Court recessed on June 7 until September. Thus Sibron was released well before there had been any opportunity even to argue his case in the intermediate state appellate court. A decision by the Court of Appeals of New York was not had until July 10, 1966, the anniversary of Sibron's release.</p>
</footnote>
<footnote label="12">
<p id="b94-11"> Cf., <em>e. g., Thompson </em>v. <em>City of Louisville, </em><span class="citation" data-id="106017"><a href="/opinion/106017/thompson-v-city-of-louisville/" aria-description="Citation for case: Thompson v. City of Louisville">362 U. S. 199</a></span> (1960).</p>
</footnote>
<footnote label="13">
<p id="b95-6"> In <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>the Court noted that the petitioner could have taken steps to preserve his ease, but that “he did not apply to this Court for a stay or a supersedeas.” <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>. Here however, it is abundantly clear that there is no procedure of which Sibron could have availed himself to prevent the expiration of his sentence long before this Court could hear his case. A supersedeas from this Court is a purely ancillary writ, and may issue only in connection with an appeal actually taken. <em>Ex parte Ralston, </em><span class="citation" data-id="91800"><a href="/opinion/91800/ex-parte-ralston/" aria-description="Citation for case: Ex Parte Ralston">119 U. S. 613</a></span> (1887); Sup. Ct. Rule 18; see R. Robertson <em>&amp; F. </em>Kirkham, Jurisdiction of the Supreme Court of the United States § 435, at 883 (R. Wolfson &amp; P. Kurland ed., 1951). At the time Sibron completed service of his sentence, the only judgment outstanding was the conviction itself, rendered by the Criminal Court of the City of New York, County of Kings. This Court had no jurisdiction to hear an appeal from that judgment, since it was not rendered by the “highest court of a State in which a decision could be had,” <span class="citation no-link">28 U. S. C. § 1257</span>, and there could be no warrant for interference with the orderly appellate processes of the state courts. Thus no supersedeas could have issued. Nor could this Court have ordered Sibron admitted to bail before the expiration of his sentence, since the offense was not bailable, <span class="citation no-link">18 U. S. C. § 3144</span>; see n. 10, <em>supra. </em>Thus this case is distinguishable from <em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/" aria-description="Citation for case: St. Pierre v. United States">St. Pierre</a></span> </em>in that Sibron “could not have brought his ease to this Court for review before the expiration of his sentence.” <span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>.</p>
</footnote>
<footnote label="14">
<p id="b96-5"> Compare <em>Ginsberg </em>v. <em>New York, </em><span class="citation" data-id="9423666"><a href="/opinion/107663/ginsberg-v-new-york/#633" aria-description="Citation for case: Ginsberg v. New York">390 U. S. 629, 633, n. 2</a></span> (1968), where this Court held that the mere possibility that the Commissioner of Buildings of the Town of Hempstead, New York, might “in his discretion” attempt in the future to revoke a license to run a luncheonette because of a single conviction for selling relatively inoffensive “girlie” magazines to a 16-year-old boy was sufficient to preserve a criminal case from mootness.</p>
</footnote>
<footnote label="15">
<p id="b97-8"> See generally Note, <span class="citation no-link">53 Va. L. Rev. 403</span> (1967).</p>
</footnote>
<footnote label="16">
<p id="b98-6"> We do not know from the record how many convictions Sibron had, for what crimes, or when they were rendered. At the hearing he admitted to a 1955 conviction for burglary and a 1957 misdemeanor conviction for possession of narcotics. He also admitted that he had other convictions, but none were specifically alluded to.</p>
</footnote>
<footnote label="17">
<p id="b98-7"> We note that there is a clear distinction between a general impairment of credibility, to which the Court referred in <em>St. Pierre, see </em><span class="citation" data-id="103823"><a href="/opinion/103823/st-pierre-v-united-states/#43" aria-description="Citation for case: St. Pierre v. United States">319 U. S., at 43</a></span>, and New York’s specific statutory authorization for use of the conviction to impeach the “character” of a defendant in a criminal proceeding. The latter is a clear legal disability deliberately and specifically imposed by the legislature.</p>
</footnote>
<footnote label="18">
<p id="b99-7"> This factor has clearly been considered relevant by the Court in the past in determining the issue of mootness. See <em>Fiswick </em>v. <em>United States, </em><span class="citation" data-id="104336"><a href="/opinion/104336/fiswick-v-united-states/#221" aria-description="Citation for case: Fiswick v. United States">329 U. S. 211, 221-222</a></span> (1946).</p>
</footnote>
<footnote label="19">
<p id="b99-8"> Frankfurter, A Note on Advisory Opinions, <span class="citation no-link">37 Harv. L. Rev. 1002</span>, 1006 (1924). See also <em>Parker </em>v. <em>Ellis, </em><span class="citation" data-id="9421986"><a href="/opinion/106050/parker-v-ellis/#592" aria-description="Citation for case: Parker v. Ellis">362 U. S. 574, 592-593</a></span> (1960) (dissenting opinion).</p>
</footnote>
<footnote label="20">
<p id="b102-7"> It is not apparent, for example, whether the power to “stop” granted by the statute entails a power to “detain” for investigation or interrogation upon less than probable cause, or if so what sort of durational limitations upon such detention are contemplated. And while the statute’s apparent grant of a power of compulsion indicates that many “stops” will constitute “seizures,” it is not clear that all conduct analyzed under the rubric of the statute will either rise to the level of a “seizure” or be based upon less than probable cause. In No. 74, the <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>case, for example, the New York courts justified the seizure of appellant under § 180-a, but we have concluded that there was in fact probable cause for an arrest when Officer Lasky seized Peters on the stairway. See <em>infra, </em>at 66. In any event, a pronouncement by this Court upon the abstract validity of § 180-a’s “stop” category would be most inappropriate in these cases, since we have concluded that neither of them presents the question of the validity of a seizure of the person for purposes of interrogation upon less than probable cause.</p>
<p id="b102-8">The statute’s other categories are equally elastic, and it was passed too recent^ for the State’s highest court to have ruled upon many of the questions involving potential intersections with federal constitutional guarantees. We cannot tell, for example, whether the officer's power to “demand” of a person an “explanation of his actions” contemplates either an obligation on the part of the citizen to answer or some additional power on the part of the officer in the event of a refusal to answer, or even whether the interrogation following the “stop” is “custodial.” Compare <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. <page-number citation-index="1" label="61">*61</page-number>436</a></span> (1966). There are, moreover, substantial indications that the statutory category of a “search for a dangerous weapon” may encompass conduct considerably broader in scope than that which we approved in <em>Terry </em>v. <em>Ohio, ante, </em>p. 1. See <em>infra, </em>at 65-66. See also <em>People </em>v. <em>Taggart, </em>20 N. Y. 2d 335, <span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/" aria-description="Citation for case: People v. Taggart">229 N. E. 2d 581</a></span>, 283 N. Y. S. 2d 1 (1967). At least some of the activity apparently permitted under the rubric of searching for dangerous weapons may thus be permissible under the Constitution only if the “reasonable suspicion” of criminal activity rises to the level of probable cause. Finally, it is impossible to tell whether the standard of “reasonable suspicion” connotes the same sort of specificity, reliability, and objectivity which is the touchstone of permissible governmental action under the Fourth Amendment. Compare <em>Terry </em>v. <em><span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">Ohio, supra,</a></span> </em>with <em>People </em>v. <em><span class="citation" data-id="5523803"><a href="/opinion/5676096/people-v-taggart/" aria-description="Citation for case: People v. Taggart">Taggart, supra.</a></span> </em>In this connection we note that the searches and seizures in both <em><span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">Sibron</a></span> </em>and <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>were upheld by the Court of Appeals of New York as predicated upon “reasonable suspicion,” whereas we have concluded that the officer in <em><span class="citation" data-id="5522965"><a href="/opinion/5675337/people-v-peters/" aria-description="Citation for case: People v. Peters">Peters</a></span> </em>had probable cause for an arrest, while the policeman in <em><span class="citation" data-id="5523032"><a href="/opinion/5675381/people-v-sibron/" aria-description="Citation for case: People v. Sibron">Sibron</a></span> </em>was not possessed of any information which would justify an intrusion upon rights protected by the Fourth Amendment.</p>
</footnote>
<footnote label="21">
<p id="b106-6"><em> </em>It is argued in dissent that this Court has in effect overturned factual findings by the two courts below that the search in this case was a self-protective measure on the part of Patrolman Martin, who thought that Sibron might have been reaching for a gun. It is true, as we have noted, that the Court of Appeals of New York apparently rested its approval of the search on this view. The trial court, however, made no such finding of fact. The trial judge adopted the theory of the prosecution at the hearing on the motion to suppress. This theory was that there was probable cause to arrest Sibron for some crime having to do with narcotics. The fact <page-number citation-index="1" label="65">*65</page-number>which tipped the scales for the trial court had nothing to do with danger to the policeman. The judge expressly changed his original view and held the heroin admissible upon being reminded that Sibron had admitted on the stand that he spoke to the addicts about narcotics. This admission was not relevant on the issue of probable cause, and we do not understand the dissent to take the position that prior to the discovery of heroin, there was probable cause for an arrest.</p>
<p id="AqB">Moreover, Patrolman Martin himself never at any time put forth the notion that he acted to protect himself. As we have noted, this subject never came up, until on re-direct examination defense counsel raised the question whether Patrolman Martin thought Sibron was going for a gun. See n. 4, <em>supra. </em>This was the only reference to weapons at any point in the hearing, and the subject was swiftly dropped. In the circumstances an unarticulated “finding” by an appellate court which wrote no opinion, apparently to the effect that the officer’s invasion of Sibron’s person comported with the Constitution because of the need to protect himself, is not deserving of controlling deference.</p>
</footnote>
<footnote label="22">
<p id="b108-8"> See n. 7, <em>supra.</em></p>
</footnote>
</opinion>
```

---
