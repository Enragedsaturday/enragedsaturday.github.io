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

## GROUP: content/cases/Duckworth v. Eagan.md  (`case`, 5 assertions)

### content_page

```
---
title: "Duckworth v. Eagan"
type: case
citation: "492 U.S. 195 (1989)"
parallel_cite: "109 S. Ct. 2875; 106 L. Ed. 2d 166; 57 U.S.L.W. 4942"
neutral_cite: 1989 U.S. LEXIS 3196
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-06-26
docket: 88-317
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Duckworth v. Eagan
  varies_by_point: false
  scope_note: "Reasonably-conveys standard applied; reaffirmed in Florida v. Powell (2010); good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112322/duckworth-v-eagan/"
  cluster_id: 112322
  opinion_id: 9431819
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny"
related: ["[[California v. Prysock]]", "[[Florida v. Powell]]", "[[Miranda v. Arizona]]", "[[Michigan v. Tucker]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "warning-adequacy"]
holding: "Miranda warnings telling a suspect counsel will be appointed 'if and when you go to court' are not inadequate where, read in their totality, the warnings reasonably convey the right to counsel before and during questioning."
lake:
  record_id: Duckworth v. Eagan
  status: verified
  projected_at: 2026-07-09
---

# Duckworth v. Eagan

*492 U.S. 195 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Before questioning Eagan about a stabbing, Indiana police read him a Miranda waiver form that advised him of his right to remain silent, his right to a lawyer before and during questioning, and that a lawyer would be appointed for him "if and when you go to court." Eagan waived and made incriminating statements. The Seventh Circuit held the "if and when you go to court" language rendered the warnings constitutionally deficient.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]] that inform a suspect a lawyer will be appointed "if and when you go to court" are inadequate under *[[Miranda v. Arizona]]*.

## Rule
No. Warnings are measured for whether they reasonably convey the *[[Miranda v. Arizona|Miranda]]* rights, not for verbatim precision. "Reviewing courts therefore need not examine *Miranda* warnings as if construing a will or defining the terms of an easement. The inquiry is simply whether the warnings reasonably 'conve[y] to [a suspect] his rights as required by *Miranda*.'" — 492 U.S. at 203. ^pin-203

*[[Miranda v. Arizona|Miranda]]* "does not require that attorneys be producible on call," only that the suspect be told he has the right to counsel before and during questioning and that counsel will be appointed if he cannot afford one. — [*Id.* at 204](https://www.courtlistener.com/opinion/112322/duckworth-v-eagan/#:~:text=does%20not%20require%20that%20attorneys). ^pin-204

## Application
Read in their totality, the warnings given Eagan touched all the bases *[[Miranda v. Arizona|Miranda]]* requires: they told him of the right to counsel "before [the police] ask[ed] [him] questions" and the right to "stop answering at any time until [he] talk[ed] to a lawyer." The "if and when you go to court" advice accurately described Indiana's procedure for appointing counsel and merely anticipated a suspect's natural question about *when* counsel would be provided; it did not (as in the hypothetical condemned in *[[California v. Prysock|Prysock]]*) tie the right to counsel to a point *after* interrogation. "We hold that the initial warnings given to respondent, in their totality, satisfied *Miranda*." — [*Id.* at 205](https://www.courtlistener.com/opinion/112322/duckworth-v-eagan/#:~:text=before%20%5Bthe%20police%5D%20ask%5Bed%5D%20%5Bhim%5D). ^pin-205

## Conclusion
The warnings were adequate and the statements properly admitted. The Seventh Circuit's grant of [[Common Legal Terms#habeas-corpus|habeas]] relief was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Duckworth* applies the [[California v. Prysock]] "reasonably conveys" standard and was reaffirmed in [[Florida v. Powell]].

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny*

## Sources
- *Duckworth v. Eagan*, 492 U.S. 195 (1989) — https://www.courtlistener.com/opinion/112322/duckworth-v-eagan/ — pinpoints: 203, 204, 205.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "26288676f1dd0440", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "492 U.S. 195 (1989)", "court": "U.S. Supreme Court", "neutral_cite": "1989 U.S. LEXIS 3196", "official_citation_present": true, "parallel_cite": "109 S. Ct. 2875; 106 L. Ed. 2d 166; 57 U.S.L.W. 4942", "title": "Duckworth v. Eagan", "year": "1989"}}
{"assertion_id": "79e72286322b2fa4", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny", "title": "Duckworth v. Eagan"}}
{"assertion_id": "7a4b9aed0afd62f0", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Miranda warnings telling a suspect counsel will be appointed 'if and when you go to court' are not inadequate where, read in their totality, the warnings reasonably convey the right to counsel before and during questioning.", "title": "Duckworth v. Eagan"}}
{"assertion_id": "2467efc3aa558fa3", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Duckworth v. Eagan"}}
{"assertion_id": "b028ae4682e7d9f8", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1989-06-26", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Duckworth v. Eagan", "field_i_validity": "good_law", "scope_note": "Reasonably-conveys standard applied; reaffirmed in Florida v. Powell (2010); good law.", "title": "Duckworth v. Eagan", "varies_by_point": "false"}}
```

### lake record — Duckworth v. Eagan

```json
{
  "schema_version": "s2.v1",
  "record_id": "Duckworth v. Eagan",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Duckworth v. Eagan",
    "case_name_short": "Duckworth",
    "case_name_full": "Duckworth v. Eagan",
    "input_case_name": "Duckworth v. Eagan",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-06-26",
    "year": 1989,
    "docket": "88-317",
    "cluster_id": 112322,
    "lead_opinion_id": 9431819,
    "sibling_ids": [
      112322,
      9431819,
      9431820,
      9431821
    ],
    "absolute_url": "/opinion/112322/duckworth-v-eagan/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9083435,
        "score": 20,
        "case_name": "Duckworth v. Eagan"
      },
      {
        "cluster_id": 9083434,
        "score": 20,
        "case_name": "Duckworth v. Eagan"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "492 U.S. 195",
      "volume": "492",
      "reporter": "U.S.",
      "page": "195",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 2875",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "2875",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 L. Ed. 2d 166",
        "volume": "106",
        "reporter": "L. Ed. 2d",
        "page": "166",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4942",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4942",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 3196",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "3196",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "492 U.S. 195",
        "volume": "492",
        "reporter": "U.S.",
        "page": "195",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 2875",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "2875",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "106 L. Ed. 2d 166",
        "volume": "106",
        "reporter": "L. Ed. 2d",
        "page": "166",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 3196",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "3196",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4942",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4942",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "492 U.S. 195",
    "official_selection": {
      "court_class": "scotus",
      "selected": "492 U.S. 195",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-203",
      "page": null,
      "quote": "are inadequate under *Miranda v. Arizona*. ## Rule No. Warnings are measured for whether they reasonably convey the *Miranda* rights, not for verbatim precision.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-204",
      "page": null,
      "quote": "does not require that attorneys be producible on call,",
      "star_marker": "204",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 19336,
      "fragment": "#:~:text=does%20not%20require%20that%20attorneys",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-205",
      "page": null,
      "quote": "before [the police] ask[ed] [him] questions",
      "star_marker": "205",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 22526,
      "fragment": "#:~:text=before%20%5Bthe%20police%5D%20ask%5Bed%5D%20%5Bhim%5D",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Duckworth v. Eagan",
    "varies_by_point": false,
    "scope_note": "Reasonably-conveys standard applied; reaffirmed in Florida v. Powell (2010); good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "United States v. Larry Loucious",
          "cluster_id": 4347647,
          "cite": [
            "847 F.3d 1146",
            "2017 WL 510457",
            "2017 U.S. App. LEXIS 2166"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Luis Fernando Ortiz",
          "cluster_id": 4472662,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Frederick G. Jackson v. Matthew J. Frank, 1",
          "cluster_id": 784078,
          "cite": [
            "348 F.3d 658",
            "2003 U.S. App. LEXIS 22776",
            "2003 WL 22511145"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Dickerson",
          "cluster_id": 2967209,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ramirez",
          "cluster_id": 3958382,
          "cite": [
            "732 N.E.2d 1064",
            "135 Ohio App. 3d 89"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane1_negative"
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
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
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
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ylst v. Nunnemaker",
          "cluster_id": 112642,
          "cite": [
            "115 L. Ed. 2d 706",
            "111 S. Ct. 2590",
            "501 U.S. 797",
            "1991 U.S. LEXIS 3636"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
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
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "O'NEAL v. McAninch",
          "cluster_id": 117897,
          "cite": [
            "130 L. Ed. 2d 947",
            "115 S. Ct. 992",
            "513 U.S. 432",
            "1995 U.S. LEXIS 908"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
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
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Missouri v. Seibert",
          "cluster_id": 137002,
          "cite": [
            "159 L. Ed. 2d 643",
            "124 S. Ct. 2601",
            "542 U.S. 600",
            "2004 U.S. LEXIS 4578"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McFarland v. Scott",
          "cluster_id": 117873,
          "cite": [
            "129 L. Ed. 2d 666",
            "114 S. Ct. 2568",
            "512 U.S. 849",
            "1994 U.S. LEXIS 5085",
            "8 Fla. L. Weekly Fed. S 405",
            "62 U.S.L.W. 4713",
            "94 Cal. Daily Op. Serv. 5054",
            "94 Daily Journal DAR 9257"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Holt",
          "cluster_id": 5607876,
          "cite": [
            "15 Cal. 4th 619",
            "97 Daily Journal DAR 6322",
            "97 Cal. Daily Op. Serv. 3742",
            "63 Cal. Rptr. 2d 782",
            "937 P.2d 213",
            "1997 Cal. LEXIS 2309"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Withrow v. Williams",
          "cluster_id": 112847,
          "cite": [
            "123 L. Ed. 2d 407",
            "113 S. Ct. 1745",
            "507 U.S. 680",
            "1993 U.S. LEXIS 2980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Samayoa",
          "cluster_id": 5607879,
          "cite": [
            "15 Cal. 4th 795",
            "938 P.2d 2",
            "97 Daily Journal DAR 7699",
            "64 Cal. Rptr. 2d 400",
            "97 Cal. Daily Op. Serv. 4760",
            "1997 Cal. LEXIS 2966"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
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
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
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
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Willie Clisby, Cross-Appellant v. Charlie Jones, Warden, Holman Unit, Alabama Department of Corrections, Cross-Appellee",
          "cluster_id": 580810,
          "cite": [
            "960 F.2d 925",
            "1992 U.S. App. LEXIS 8906",
            "1992 WL 91127"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lawrence S. Bittaker v. Jeanne S. Woodford, Warden, California State Prison of San Quentin",
          "cluster_id": 782239,
          "cite": [
            "331 F.3d 715",
            "2003 Daily Journal DAR 6078",
            "61 Fed. R. Serv. 923",
            "2003 Cal. Daily Op. Serv. 4773",
            "2003 U.S. App. LEXIS 11298",
            "2003 WL 21297178"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wader",
          "cluster_id": 1447881,
          "cite": [
            "854 P.2d 80",
            "5 Cal. 4th 610",
            "20 Cal. Rptr. 2d 788",
            "93 Daily Journal DAR 8799",
            "93 Cal. Daily Op. Serv. 5245",
            "1993 Cal. LEXIS 3188"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Louisias",
          "cluster_id": 5845572,
          "cite": [
            "29 A.D.3d 1017",
            "815 N.Y.S.2d 727"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
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
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Enraca",
          "cluster_id": 844219,
          "cite": [
            "269 P.3d 543",
            "53 Cal. 4th 735",
            "137 Cal. Rptr. 3d 117",
            "2012 WL 360555",
            "2012 Cal. LEXIS 1078"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Noah H. Lundy v. Donal Campbell and Charles W. Burson",
          "cluster_id": 531249,
          "cite": [
            "888 F.2d 467"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wash",
          "cluster_id": 1158185,
          "cite": [
            "861 P.2d 1107",
            "6 Cal. 4th 215",
            "24 Cal. Rptr. 2d 421",
            "93 Cal. Daily Op. Serv. 8554",
            "93 Daily Journal DAR 14629",
            "1993 Cal. LEXIS 5807"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Smith",
          "cluster_id": 2632408,
          "cite": [
            "150 P.3d 1224",
            "54 Cal. Rptr. 3d 245",
            "40 Cal. 4th 483",
            "2007 Cal. Daily Op. Serv. 1275",
            "2007 Daily Journal DAR 1761",
            "2007 Cal. LEXIS 749"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dennis Rosa Collazo v. Wayne Estelle, Warden, California Mens Colony",
          "cluster_id": 565270,
          "cite": [
            "940 F.2d 411",
            "91 Daily Journal DAR 8681",
            "91 Cal. Daily Op. Serv. 5640",
            "1991 U.S. App. LEXIS 15265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Combs",
          "cluster_id": 2508099,
          "cite": [
            "101 P.3d 1007",
            "22 Cal. Rptr. 3d 61",
            "34 Cal. 4th 821",
            "2004 Cal. Daily Op. Serv. 11051",
            "2004 Daily Journal DAR 14981",
            "2004 Cal. LEXIS 11889"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Valdez",
          "cluster_id": 2507157,
          "cite": [
            "178 P.3d 1269",
            "2007 Colo. App. LEXIS 2493",
            "2007 WL 4531716"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Duckworth v. Eagan:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112322 OR 9431819 OR 9431820 OR 9431821) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz04OTkxNjQ4MDAwMDAmcz0yNjE2OTg5JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112322+OR+9431819+OR+9431820+OR+9431821%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 5,
        "triage_snippet_classified": 195
      },
      "lane2_top_cited": {
        "query": "cites:(112322 OR 9431819 OR 9431820 OR 9431821)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjQmcz0yOTQ3MTY3JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112322+OR+9431819+OR+9431820+OR+9431821%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112322 OR 9431819 OR 9431820 OR 9431821)",
        "reviewed": 17,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 17,
        "triage_read": 0,
        "triage_snippet_classified": 17
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112322 OR 9431819 OR 9431820 OR 9431821)",
    "indexed_citing_opinions": 362,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112322,
        "count": 308,
        "count_source": "search"
      },
      {
        "opinion_id": 9431819,
        "count": 55,
        "count_source": "search"
      },
      {
        "opinion_id": 9431820,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9431821,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 666,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/duckworth-v-eagan.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4MDgyNjImcz02NDgwNjk1JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112322+OR+9431819+OR+9431820+OR+9431821%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112322,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 105188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 106548,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 106862,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 107260,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 107883,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 107892,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 108997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 109439,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 109491,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 109540,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 110080,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 110138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 110143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 110556,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 110662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 110937,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 111214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 111364,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 111552,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 111726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 111779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 111956,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 112205,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 112303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 276591,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 286347,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 288454,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 291907,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 300429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 304664,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 305989,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 312948,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 398333,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 408067,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 498413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 504373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 876832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1095760,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1127188,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1143399,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1159462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1161202,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1164112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1324496,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1396567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1498770,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1635437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1951549,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1963066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 1977442,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 2071255,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 2099157,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 2116013,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 2146839,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 2218275,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112322,
        "cited_id": 2226296,
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
    "date_created": "2026-07-05T02:56:57Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T02:57:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T02:57:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:00:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T02:57:21Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Duckworth v. Eagan

```
<opinion type="majority">
<author id="b239-4"><page-number citation-index="1" label="197">*197</page-number>Chief Justice Rehnquist</author>
<p id="AOp">delivered the opinion of the Court.</p>
<p id="b239-5">Respondent confessed to stabbing a woman nine times after she refused to have sexual relations with him, and he was convicted of attempted murder. Before confessing, respondent was given warnings by the police, which included the advice that a lawyer would be appointed “if and when you go to court.” The United States Court of Appeals for the Seventh Circuit held that such advice did not comply with the requirements of <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). We disagree and reverse.</p>
<p id="b239-6">Late on May 16, 1982, respondent contacted a Chicago police officer he knew to report that he had seen the naked body of a dead woman lying on a Lake Michigan beach. Respondent denied any involvement in criminal activity. He then took several Chicago police officers to the beach, where the woman was crying for help. When she saw respondent, the woman exclaimed: “Why did you stab me? Why did you stab me?” Respondent told the officers that he had been with .the woman earlier that night, but that they had been attacked by several men who abducted the woman in a van.</p>
<p id="b239-7">The next morning, after realizing that the crime had been committed in Indiana, the Chicago police turned the investigation over to the Hammond, Indiana, Police Department. Respondent repeated to the Hammond police officers his story that he had been attacked on the lakefront, and that the woman had been abducted by several men. After he filled out a battery complaint at a local police station, respondent agreed to go to the Hammond police headquarters for further questioning.</p>
<p id="b239-8">At about 11 a. m., the Hammond police questioned respondent. Before doing so, the police read to respondent a waiver form, entitled “Voluntary Appearance; Advice of Rights,” and they asked him to sign it. The form provided:</p>
<blockquote id="b240-4"><page-number citation-index="1" label="198">*198</page-number>“Before we ask you any questions, you must understand your rights. You have the right to remain silent. Anything you say can be used against you in court. <em>You have a right to talk to a lawyer for advice before we ask you any questions, and to have him with you during questioning. </em>You have this right to the advice and presence of a lawyer even if you cannot afford to hire one. <em>We have no way of giving you a lawyer, but one will be appointed for you, if you wish, if and when you go to court. </em>If you wish to answer questions now without a lawyer present, you have the right to stop answering questions at any time. You also have the right to stop answering at any time until you’ve talked to a lawyer.” <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1555" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden">843 F. 2d 1554, 1555-1556</a></span> (CA7 1988) (emphasis added).<footnotemark>1</footnotemark></blockquote>
<p id="b240-5">Respondent signed the form and repeated his exculpatory explanation for his activities of the previous evening.</p>
<p id="b240-6">Respondent was then placed in the “lockup” at the Hammond police headquarters. Some 29 hours later, at about 4 p.m. on May 18, the police again interviewed respondent. Before this questioning, one of the officers read the following waiver form to respondent:</p>
<blockquote id="b240-7">“1. Before making this statement, I was advised that I have the right to remain silent and that anything I <page-number citation-index="1" label="199">*199</page-number>might say may or will be used against me in a court of law.</blockquote>
<blockquote id="b241-5">“2. That I have the right to consult with an attorney of my own choice before saying anything, and that an attorney may be present while I am making any statement or throughout the course of any conversation with any police officer if I so choose.</blockquote>
<blockquote id="b241-6">“3. That I can stop and request an attorney at any time during the course of the taking of any statement or during the course of any such conversation.</blockquote>
<blockquote id="b241-7">“4. That in the course of any conversation I can refuse to answer any further questions and remain silent, thereby terminating the conversation.</blockquote>
<blockquote id="b241-8">“5. That if I do not hire an attorney, one will be provided for me.” <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1556" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden"><em>Id., </em>at 1556</a></span>.</blockquote>
<p id="b241-9">Respondent read the form back to the officers and signed it. He proceeded to confess to stabbing the woman. The next morning, respondent led the officers to the Lake Michigan beach where they recovered the knife he had used in the stabbing and several items of clothing.</p>
<p id="b241-10">At trial, over respondent’s objection, the state court admitted his confession, his first statement denying any involvement in the crime, the knife, and the clothing. The jury found respondent guilty of attempted murder, but acquitted him of rape. He was sentenced to 35 years’ imprisonment. The conviction was upheld on appeal. <em>Eagan </em>v. <em>State, </em><span class="citation" data-id="9725807"><a href="/opinion/2146839/eagan-v-state/" aria-description="Citation for case: Eagan v. State">480 N. E. 2d 946</a></span> (Ind. 1985).</p>
<p id="b241-11">Respondent sought a writ of habeas corpus in the United States District Court for the Northern District of Indiana, claiming, <em>inter alia, </em>that his confession was inadmissible because the first waiver form did not comply with <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The District Court denied the petition, holding that the record “clearly manifests adherence to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>. . . espe-<page-number citation-index="1" label="200">*200</page-number>dally as to the so-called second statement.” App. to Pet. for Cert. A52.</p>
<p id="b242-5">A divided United States Court of Appeals for the Seventh Circuit reversed. <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden">843 F. 2d 1554</a></span> (1988). The majority held that the advice that counsel would be appointed “if and when you go to court,” which was included in the first warnings given to respondent, was “constitutionally defective because it denies an accused indigent a clear and unequivocal warning of the right to appointed counsel before any interrogation,” and “link[s] an indigent’s right to counsel before interrogation with a future event.” <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1557" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden"><em>Id., </em>at 1557</a></span>. The majority relied on the Seventh Circuit’s decision in <em>United States ex rel. Williams </em>v. <em>Twomey, </em><span class="citation" data-id="9458775"><a href="/opinion/305989/united-states-of-america-ex-rel-ruben-williams-v-john-twomey-and-peter/#1250" aria-description="Citation for case: United States of America Ex Rel. Ruben Williams v. John...">467 F. 2d 1248, 1250</a></span> (1972), which had condemned, as “misleading and confusing,” the inclusion of “if and when you go to court” language in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. Turning to the admissibility of respondent’s confession, the majority thought that “as a result of the first warning, [respondent] arguably believed that he could not secure a lawyer during interrogation” and that the second warning “did not explicitly correct this misinformation.” <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1558" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden">843 F. 2d, at 1558</a></span>. It therefore remanded the case for a determination whether respondent had knowingly and intelligently waived his right to an attorney during the second interview. The dissenting judge rejected the majority’s “formalistic, technical and unrealistic application of <em>Miranda” </em>and argued that the first warnings passed constitutional muster. <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1562" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden"><em>Id., </em>at 1562</a></span>., In any case, he thought that remand was not necessary because the record indicated that this case was covered by <em>Oregon </em>v. <em>Elstad, </em><span class="citation" data-id="9429930"><a href="/opinion/111364/oregon-v-elstad/" aria-description="Citation for case: Oregon v. Elstad">470 U. S. 298</a></span> (1985). <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1570" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden">843 F. 2d, at 1570-1571</a></span>.</p>
<p id="b242-7">The Court of Appeals denied rehearing en banc, with four judges dissenting from that order. App. to Pet. for Cert. A1-A2. We then granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./488/888/">488 U. S. 888</a></span> (1988), to resolve a conflict among the lower courts as to whether informing a suspect that an attorney would be appointed for him “if and when you go to court” renders <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warn<page-number citation-index="1" label="201">*201</page-number>ings inádequate.<footnotemark>2</footnotemark> We agree with the majority of the lower courts that it does not.<footnotemark>3</footnotemark></p>
<p id="b243-5">In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), the Court established certain procedural safeguards that require police to advise criminal suspects of their rights under the Fifth and Fourteenth Amendments before commencing custodial interrogation. In now-familiar words, the Court said that the <page-number citation-index="1" label="202">*202</page-number>suspect must be told that “he has the right to remain silent, that anything he says can be used against him in a court of law, that he has the right to the presence of an attorney, and that if he cannot afford an attorney one will be appointed for him prior to any questioning if he so desires.” <em>Id,., </em>at 479. The Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“presumed that interrogation in certain custodial circumstances is inherently coercive and . . . that statements made under those circumstances are inadmissible unless the suspect is specifically warned of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights and freely decides to forgo those rights.” <em>New York </em>v. <em>Quarles, </em><span class="citation" data-id="9429664"><a href="/opinion/111214/new-york-v-quarles/#654" aria-description="Citation for case: New York v. Quarles">467 U. S. 649, 654</a></span> (1984) (footnote omitted).</p>
<p id="b244-5">We have never insisted that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings be given in the exact form described in that decision.<footnotemark>4</footnotemark> In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself, the Court said that “[t]he warnings required and the waiver necessary in accordance with our opinion today are, <em>in the absence of a fully effective equivalent, </em>prerequisites to the admissibility of any statement made by a defendant.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#476" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 476</a></span> (emphasis added). See also <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#297" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 297</a></span> (1980) (referring to “the now familiar <em>Miranda </em>warnings ... or their equivalent”). In <em>California </em>v. <em>Prysock, </em><span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/" aria-description="Citation for case: California v. Prysock">453 U. S. 355</a></span> (1981) <em>(per curiam), </em>we stated that “the ‘rigidity’ of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>[does not] exten[d] to the precise formulation of the warnings given a criminal defendant,” and <page-number citation-index="1" label="203">*203</page-number>that “no talismanic incantation [is] required to satisfy its strictures.” <em>Id., </em>at 359.</p>
<p id="b245-5"><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>has not been limited to station house questioning, see <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra</a></span> </em>(police car), and the officer in the field may not always have access to printed <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, or he may inadvertently depart from routine practice, particularly if a suspect requests an elaboration of the warnings. The prophylactic <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings are “not themselves rights protected by the Constitution but [are] instead measures to in.sure that the right against compulsory self-incrimination [is] protected.” <em>Michigan </em>v. <em>Tucker, </em><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#444" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 444</a></span> (1974). Reviewing courts therefore need not examine <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings as if construing a will or defining the terms of an easement. The inquiry is simply whether the warnings reasonably “conve[y] to [a suspect] his rights as required by <em>Miranda.” Pry sock, supra, </em>at 361.</p>
<p id="b245-6">We think the initial warnings given to respondent touched all of the bases required by <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The police told respondent that he had the right to remain silent, that anything he said could be used against him in court, that he had the right to speak to an attorney before and during questioning, that he had “this right to the advice and presence of a lawyer even if [he could] not afford to hire one,” and that he had the “right to stop answering at any time until [he] talked to a lawyer.” <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1555" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden">843 F. 2d, at 1555-1556</a></span>. As noted, the police also added that they could not provide respondent with a lawyer, but that one would be appointed “if and when you go to court.” The Court of Appeals thought this “if and when you go to court” language suggested that “only those accused who can afford an attorney have the right to have one present before answering any questions,” and “implie[d] that if the accused does not ‘go to court/ <em>i. e.[,] </em>the government does not file charges, the accused is not entitled to [counsel] at all.” <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1557" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden"><em>Id., </em>at 1557</a></span>.</p>
<p id="b245-7">In our view, the Court of Appeals misapprehended the effect of the inclusion of “if and when you go to court” language <page-number citation-index="1" label="204">*204</page-number>in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. First, this instruction accurately described the procedure for the appointment of counsel in Indiana. Under Indiana law, counsel is appointed at the defendant’s initial appearance in court, <span class="citation no-link">Ind. Code § 35-33-7-6</span> (1988), and formal charges must be filed at or before that hearing, §35-33-7-3(a).<footnotemark>5</footnotemark> We think it must be relatively commonplace for a suspect, after receiving <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings, to ask <em>when </em>he will obtain counsel. The “if and when you go to court” advice simply anticipates that question.<footnotemark>6</footnotemark> Second, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>does not require that attorneys be producible on call, but only that the suspect be informed, as here, that he has the right to an attorney before and during questioning, and that an attorney would be appointed for him if he could not afford one.<footnotemark>7</footnotemark> The Court in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>emphasized that it was not suggesting that “each police station must have a ‘station house lawyer’ present at all times to advise prisoners.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>. If the police cannot provide appointed counsel, <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>requires only that the police not question a suspect unless he waives his right to counsel. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span> </em>Here, respondent did just that.</p>
<p id="b246-5">Respondent relies, Brief for Respondent 24-29, on language in <em>California </em>v. <em><span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/" aria-description="Citation for case: California v. Prysock">Prysock</a></span>, </em>where we suggested that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings would not be sufficient “if the reference to the right to appointed counsel was linked [to a] future point in time <em>after </em>the police interrogation.” <span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/#360" aria-description="Citation for case: California v. Prysock">453 U. S., at 360</a></span> (emphasis added). The Court of Appeals also referred to <em><span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/" aria-description="Citation for case: California v. Prysock">Prysock</a></span> </em>in finding deficient the initial warnings given to re<page-number citation-index="1" label="205">*205</page-number>spondent. <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1557" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden">843 F. 2d, at 1557</a></span>. But the vice referred to in <em><span class="citation" data-id="9428478"><a href="/opinion/110556/california-v-prysock/" aria-description="Citation for case: California v. Prysock">Prysock</a></span> </em>was that such warnings would not apprise the accused of his right to have an attorney present if he chose to answer questions. The warnings in this case did not suffer from that defect. Of the eight sentences in the initial warnings, one described respondent’s right to counsel “before [the police] ask[ed] [him] questions,” while another stated his right to “stop answering at any time until [he] talk[ed] to a lawyer.” <em>Id., </em>at 1555-1556. We hold that the initial warnings given to respondent, in their totality, satisfied <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>and therefore that his first statement denying his involvement in the crime, as well as the knife and the clothing, was properly admitted into evidence.</p>
<p id="b247-5">The Court of Appeals thought it necessary to remand this case for consideration of whether respondent’s second statement was tainted by the first warnings. <em>Id., </em>at 1557-1558. In view of our disposition of this case, we need not reach that question.<footnotemark>8</footnotemark> The judgment of the Court of Appeals is accordingly reversed, and the case is remanded for further proceedings consistent with our decision.</p>
<p id="b247-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b240-8"> The remainder of the form signed by respondent provided:</p>
<p id="b240-9">“I, <em>[Gary Eagan,] </em>have come to the Detective Bureau of the Hammond, Indiana Police Department, of my own choice to talk with Officers ... In [sic] regard to an investigation they are conducting. I know that I am not under arrest and that I can leave this office if I wish to do so.</p>
<p id="b240-10">“Prior to any questioning, I was furnished with the above statement of my rights.... I have (read) (had read to me) this statement of my rights. I understand what my rights are. I am willing to answer questions and make a statement. I do not want a lawyer. I understand and know what I am doing. No promises or threats have been made to me and no pressure of any kind has been used against me.” <span class="citation" data-id="9477462"><a href="/opinion/504373/gary-james-eagan-v-jack-r-duckworth-warden/#1560" aria-description="Citation for case: Gary James Eagan v. Jack R. Duckworth, Warden">843 F. 2d, at 1560, n. 2</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b243-6"> The majority of federal and state courts to consider the issue have held that warnings that contained “if and when you go to court” language satisfied <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>See <em>Wright </em>v. <em>North Carolina, </em><span class="citation" data-id="312948"><a href="/opinion/312948/nat-villiam-wright-v-state-of-north-carolina-and-david-henry-warden/#406" aria-description="Citation for case: Nat Villiam Wright v. State of North Carolina and David...">483 F. 2d 405, 406-407</a></span> (CA4 1973), cert. denied, <span class="citation" data-id="9425662"><a href="/opinion/108997/wright-v-north-carolina-et-al/" aria-description="Citation for case: Wright v. North Carolina Et Al.">415 U. S. 936</a></span> (1974); <em>Massimo </em>v. <em>United States, </em><span class="citation" data-id="304664"><a href="/opinion/304664/matthew-massimo-v-united-states/#1174" aria-description="Citation for case: Matthew Massimo v. United States">463 F. 2d 1171, 1174</a></span> (CA2 1972), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./409/1117/">409 U. S. 1117</a></span> (1973); <em>United States </em>v. <em>Lacy, </em><span class="citation multiple-matches"><a href="/c/F.%202d/446/511/">446 F. 2d 511</a></span>, 513 (CA5 1971); <em>State </em>v. <em>Sterling, </em><span class="citation" data-id="1127188"><a href="/opinion/1127188/state-v-sterling/#62" aria-description="Citation for case: State v. Sterling">377 So. 2d 58, 62-63</a></span> (La. 1979); <em>Harrell </em>v. <em>State, </em><span class="citation" data-id="1095760"><a href="/opinion/1095760/harrell-v-state/#645" aria-description="Citation for case: Harrell v. State">357 So. 2d 643, 645-646</a></span> (Miss. 1978); <em>Rowbotham </em>v. <em>State, </em><span class="citation" data-id="9542628"><a href="/opinion/1161202/rowbotham-v-state/#618" aria-description="Citation for case: Rowbotham v. State">542 P. 2d 610, 618-619</a></span> (Okla. Crim. App. 1975); <em>Grennier </em>v. <em>State, </em><span class="citation" data-id="1977442"><a href="/opinion/1977442/grennier-v-state/#213" aria-description="Citation for case: Grennier v. State">70 Wis. 2d 204, 213-215</a></span>, <span class="citation" data-id="1977442"><a href="/opinion/1977442/grennier-v-state/#321" aria-description="Citation for case: Grennier v. State">234 N. W. 2d 316, 321-322</a></span> (1975); <em>Schade </em>v. <em>State, </em><span class="citation" data-id="9544442"><a href="/opinion/1164112/schade-v-state/#915" aria-description="Citation for case: Schade v. State">512 P. 2d 907, 915-916</a></span> (Alaska 1973); <em>State </em>v. <em>Mumbaugh, </em><span class="citation" data-id="1396567"><a href="/opinion/1396567/state-v-mumbaugh/#596" aria-description="Citation for case: State v. Mumbaugh">107 Ariz. 589, 596-597</a></span>, <span class="citation" data-id="1396567"><a href="/opinion/1396567/state-v-mumbaugh/#450" aria-description="Citation for case: State v. Mumbaugh">491 P. 2d 443, 450-451</a></span> (1971); <em>People </em>v. <em>Campbell, </em><span class="citation" data-id="2116013"><a href="/opinion/2116013/people-v-campbell/#201" aria-description="Citation for case: People v. Campbell">26 Mich. App. 196, 201-202</a></span>, <span class="citation" data-id="2116013"><a href="/opinion/2116013/people-v-campbell/#6" aria-description="Citation for case: People v. Campbell">182 N. W. 2d 4, 6-7</a></span> (1970), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./401/945/">401 U. S. 945</a></span> (1971); <em>People </em>v. <em>Swift, </em>32 App. Div. 2d 183, 186-187, 300 N. Y. S. 2d 639, 643-644 (1969), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./396/1018/">396 U. S. 1018</a></span> (1970). Other courts, although not using the precise “if and when you go to court” language, have held <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>was satisfied by a warning that an attorney could not be appointed for a suspect until he appeared in court. See <em>United States </em>v. <em>Contreras, </em><span class="citation" data-id="398333"><a href="/opinion/398333/united-states-v-freddy-antonio-contreras/#979" aria-description="Citation for case: United States v. Freddy Antonio Contreras">667 F. 2d 976, 979</a></span> (CA11), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./459/849/">459 U. S. 849</a></span> (1982); <em>Coyote </em>v. <em>United States, </em><span class="citation" data-id="276591"><a href="/opinion/276591/willie-salt-coyote-v-united-states/#308" aria-description="Citation for case: Willie Salt Coyote v. United States">380 F. 2d 305, 308</a></span> (CA10), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./389/992/">389 U. S. 992</a></span> (1967); <em>State </em>v. <em>Maluia, </em><span class="citation" data-id="1143399"><a href="/opinion/1143399/state-v-maluia/#431" aria-description="Citation for case: State v. Maluia">56 Haw. 428, 431-435</a></span>, <span class="citation" data-id="1143399"><a href="/opinion/1143399/state-v-maluia/#1205" aria-description="Citation for case: State v. Maluia">539 P. 2d 1200, 1205-1207</a></span> (1975); <em>Emler v. State, </em><span class="citation" data-id="9741143"><a href="/opinion/2226296/emler-v-state/#243" aria-description="Citation for case: Emler v. State">259 Ind. 241, 243-244</a></span>, <span class="citation" data-id="9741143"><a href="/opinion/2226296/emler-v-state/#410" aria-description="Citation for case: Emler v. State">286 N. E. 2d 408, 410-411</a></span> (1972); <em>Jones </em>v. <em>State, </em><span class="citation" data-id="9662365"><a href="/opinion/1635437/jones-v-state/#343" aria-description="Citation for case: Jones v. State">69 Wis. 2d 337, 343-345</a></span>, <span class="citation" data-id="9662365"><a href="/opinion/1635437/jones-v-state/#682" aria-description="Citation for case: Jones v. State">230 N. W. 2d 677, 682-683</a></span> (1975).</p>
<p id="b243-7">On the other hand, a minority of federal and state courts, including the Seventh Circuit in this case, have held that “if and when you go to court” language did not satisfy <em>Miranda. </em>See <em>United States ex rel. Williams </em>v. <em>Twomey, </em><span class="citation" data-id="9458775"><a href="/opinion/305989/united-states-of-america-ex-rel-ruben-williams-v-john-twomey-and-peter/#1249" aria-description="Citation for case: United States of America Ex Rel. Ruben Williams v. John...">467 F. 2d 1248, 1249-1250</a></span> (CA7 1972); <em>Gilpin </em>v. <em>United States, </em><span class="citation" data-id="286347"><a href="/opinion/286347/eddie-huless-gilpin-v-united-states/#641" aria-description="Citation for case: Eddie Huless Gilpin v. United States">415 F. 2d 638, 641</a></span> (CA5 1969); <em>State </em>v. <em>Dess, </em><span class="citation" data-id="9507126"><a href="/opinion/876832/state-v-dess/#120" aria-description="Citation for case: State v. Dess">184 Mont. 116, 120-122</a></span>, <span class="citation" data-id="9507126"><a href="/opinion/876832/state-v-dess/#144" aria-description="Citation for case: State v. Dess">602 P. 2d 142, 144-145</a></span> (1979); <em>Commonwealth </em>v. <em>Johnson, </em><span class="citation" data-id="9700204"><a href="/opinion/1951549/commonwealth-v-johnson/#352" aria-description="Citation for case: Commonwealth v. Johnson">484 Pa. 349, 352-357</a></span>, <span class="citation" data-id="9700204"><a href="/opinion/1951549/commonwealth-v-johnson/#112" aria-description="Citation for case: Commonwealth v. Johnson">399 A. 2d 111, 112-114</a></span> (1979); <em>Square </em>v. <em>State, </em><span class="citation" data-id="9678553"><a href="/opinion/1758066/square-v-state/#550" aria-description="Citation for case: Square v. State">283 Ala. 548, 550</a></span>, <span class="citation" data-id="9678553"><a href="/opinion/1758066/square-v-state/#378" aria-description="Citation for case: Square v. State">219 So. 2d 377, 378-379</a></span> (1969).</p>
</footnote>
<footnote label="3">
<p id="b243-8"> Petitioner does not argue, and we therefore need not decide, whether <em>Stone </em>v. <em>Powell, </em><span class="citation" data-id="9426587"><a href="/opinion/109540/stone-v-powell/" aria-description="Citation for case: Stone v. Powell">428 U. S. 465</a></span> (1976), should be extended to bar relitigation on federal habeas of nonconstitutional claims under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
<footnote label="4">
<p id="b244-6"> For example, the standard <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings used by the Federal Bureau of Investigation provide as follows:</p>
<blockquote id="b244-7">“Before we ask you any questions, you must understand your rights.</blockquote>
<blockquote id="b244-8">“You have the right to remain silent.</blockquote>
<blockquote id="b244-9">“Anything you say can be used against you in court.</blockquote>
<blockquote id="b244-10">“You have the right to talk to a lawyer for advice before we ask you any questions and to have a lawyer with you during questioning.</blockquote>
<blockquote id="b244-11">“If you cannot afford a lawyer, one will be appointed for you before any questioning if you wish.</blockquote>
<blockquote id="b244-12">“If you decide to answer questions now without a lawyer present, you will still have the right to stop answering at any time. You also have the right to stop answering at any time until you talk to a lawyer.” Brief for United States as <em>Amicus Curiae </em>1-2, n. 1.</blockquote>
</footnote>
<footnote label="5">
<p id="b246-6"> In federal court, the defendant’s initial hearing, at which counsel is appointed, may occur before the filing of the indictment or information. Fed. Rules Crim. Proc. 5(a), (e).</p>
</footnote>
<footnote label="6">
<p id="b246-7"> At oral argument, the United States said that the federal law enforcement officials do not use this language in order to avoid “unnecessary litigation.” Tr. of Oral Arg. 16.</p>
</footnote>
<footnote label="7">
<p id="b246-8"> In <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>, </em>the Court stated that the FBI’s then-current practice of informing suspects “of a right to free counsel <em>if </em>they are unable to pay, and the availability of such counsel from the Judge,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#486" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 486</a></span>, was “consistent with the procedure which we delineate today,” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#484" aria-description="Citation for case: Miranda v. Arizona"><em>id., </em>at 484</a></span>.</p>
</footnote>
<footnote label="8">
<p id="b247-9"> Respondent argues that the second set of <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings he received were deficient. Brief for Respondent 38-40. These specific warnings have been upheld by the Seventh Circuit, <em>Richardson </em>v. <em>Duckworth, </em><span class="citation" data-id="498413"><a href="/opinion/498413/solomon-richardson-v-jack-r-duckworth-warden-and-indiana-attorney/" aria-description="Citation for case: Solomon Richardson v. Jack R. Duckworth, Warden, and...">834 F. 2d 1366</a></span> (CA7 1987), and the Indiana Supreme Court, <em>Robinson </em>v. <em>State, </em><span class="citation" data-id="2218275"><a href="/opinion/2218275/robinson-v-state/" aria-description="Citation for case: Robinson v. State">272 Ind. 312</a></span>, <span class="citation" data-id="2218275"><a href="/opinion/2218275/robinson-v-state/" aria-description="Citation for case: Robinson v. State">397 N. E. 2d 956</a></span> (1979), and we think they plainly comply with <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</em></p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Dunaway v. New York.md  (`case`, 7 assertions)

### content_page

```
---
title: "Dunaway v. New York"
type: case
citation: "442 U.S. 200 (1979)"
parallel_cite: "99 S. Ct. 2248; 60 L. Ed. 2d 824"
neutral_cite: 1979 U.S. LEXIS 126
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-05
docket: 78-5066
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-05
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Dunaway v. New York
  varies_by_point: false
  scope_note: "Foundational: a station-house detention for interrogation requires probable cause, and Miranda warnings alone do not attenuate the taint of an illegal arrest. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110096/dunaway-v-new-york/"
  cluster_id: 110096
  opinion_id: 110096
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Key — Progeny"
  - page: "[[Fruits & Attenuation]]"
    role: "Related (cross-doctrine)"
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Related (cross-doctrine)"
related: ["[[Brown v. Illinois]]", "[[Wong Sun v. United States]]", "[[Davis v. Mississippi]]", "[[Terry v. Ohio]]", "[[Kaupp v. Texas]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "probable-cause", "exclusionary-rule", "fruit-of-the-poisonous-tree", "interrogation"]
holding: "Involuntarily transporting a suspect to the station and detaining him for custodial interrogation, on less than probable cause, is a seizure tantamount to arrest requiring probable cause; the resulting confession is a fruit of the illegal seizure that Miranda warnings alone do not attenuate."
lake:
  record_id: Dunaway v. New York
  status: verified
  projected_at: 2026-07-09
---

# Dunaway v. New York

*442 U.S. 200 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Investigating a killing during an attempted robbery, Rochester police picked up Dunaway, drove him to the station, and questioned him after [[Miranda and Custodial Interrogation|Miranda warnings]]; he made incriminating statements and drew sketches implicating himself. He was never told he was under arrest, but he was not free to leave and would have been physically restrained had he tried. The State conceded the police lacked probable cause to arrest him. He moved to suppress the statements and sketches.

## Issue
Whether police may seize a suspect on less than probable cause, transport him to the station, and detain him for custodial interrogation consistent with the Fourth Amendment — and, if not, whether the resulting confession must be suppressed.

## Rule
No. A station-house detention for interrogation is a seizure that requires probable cause; it cannot be justified by a *[[Terry v. Ohio|Terry]]*-type balancing of interests. "[D]etention for custodial interrogation—regardless of its label—intrudes so severely on interests protected by the Fourth Amendment as necessarily to trigger the traditional safeguards against illegal arrest. We accordingly hold that the Rochester police violated the Fourth and Fourteenth Amendments when, without probable cause, they seized petitioner and transported him to the police station for interrogation." — 442 U.S. at 216. ^pin-216

A confession that follows the illegal seizure must be suppressed unless the taint is attenuated. Because the Fourth Amendment's interests are distinct from the Fifth's, "*Miranda* warnings, and the exclusion of a confession made without them, do not alone sufficiently deter a Fourth Amendment violation." — *Id.* at 217 (quoting *Brown v. Illinois*, 422 U.S. 590, 601). ^pin-217

Voluntariness is only the "threshold requirement"; the court must then weigh "[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct." — [*Id.* at 218](https://www.courtlistener.com/opinion/110096/dunaway-v-new-york/#:~:text=%22-,threshold%20requirement) (quoting *Brown*, 422 U.S. at 603–604). ^pin-218

## Application
The case was "virtually a replica" of *[[Brown v. Illinois|Brown]]*. Dunaway "was also admittedly seized without probable cause in the hope that something might turn up, and confessed without any intervening event of significance." — [*Id.* at 218](https://www.courtlistener.com/opinion/110096/dunaway-v-new-york/#:~:text=virtually%20a%20replica). ^pin-218b

Less than the requisite [[Fruits and Attenuation|attenuation]] existed: the confession followed promptly on the illegal detention, no significant intervening circumstance broke the chain, and the seizure-for-interrogation had a purposeful, investigatory quality. That the police were courteous and gave [[Miranda and Custodial Interrogation|Miranda warnings]] did not cure the Fourth Amendment violation, because Fifth Amendment voluntariness is merely the threshold of the [[Fruits and Attenuation|attenuation]] inquiry.

## Conclusion
The seizure was unconstitutional and the confession was its unattenuated fruit; the statements and sketches should have been suppressed, and the judgment was reversed and [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Dunaway* is the anchor for the rule that a custodial transport for interrogation requires probable cause, applied [[Common Legal Terms#per-curiam|per curiam]] in [[Kaupp v. Texas]], and it adopts the [[Brown v. Illinois]] [[Fruits and Attenuation|attenuation]] factors built on [[Wong Sun v. United States]]. It distinguishes the brief, limited intrusion permitted under [[Terry v. Ohio]].

## Appears on
- [[Seizure of the Person]] — *Key — Progeny*
- [[The Exclusionary Rule]] — *Related (cross-doctrine)*
- [[Miranda and Custodial Interrogation]] — *Related (cross-doctrine)*

## Sources
- *Dunaway v. New York*, 442 U.S. 200 (1979) — https://www.courtlistener.com/opinion/110096/dunaway-v-new-york/ — pinpoints: 216, 217, 218.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "8f0f66d21599b019", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "442 U.S. 200 (1979)", "court": "U.S. Supreme Court", "neutral_cite": "1979 U.S. LEXIS 126", "official_citation_present": true, "parallel_cite": "99 S. Ct. 2248; 60 L. Ed. 2d 824", "title": "Dunaway v. New York", "year": "1979"}}
{"assertion_id": "1add598e26964d2b", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Related (cross-doctrine)", "title": "Dunaway v. New York"}}
{"assertion_id": "39dfbae4eda89f7e", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Key — Progeny", "title": "Dunaway v. New York"}}
{"assertion_id": "60c22c53ba297c1f", "dimension": "support", "kind": "home_role", "locator": {"home": "Fruits & Attenuation"}, "payload": {"home": "Fruits & Attenuation", "role": "Related (cross-doctrine)", "title": "Dunaway v. New York"}}
{"assertion_id": "9087a1782e1109b5", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Involuntarily transporting a suspect to the station and detaining him for custodial interrogation, on less than probable cause, is a seizure tantamount to arrest requiring probable cause; the resulting confession is a fruit of the illegal seizure that Miranda warnings alone do not attenuate.", "title": "Dunaway v. New York"}}
{"assertion_id": "38c730404c7f74c2", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Dunaway v. New York"}}
{"assertion_id": "570a841cfdf36a87", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1979-06-05", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Dunaway v. New York", "field_i_validity": "good_law", "scope_note": "Foundational: a station-house detention for interrogation requires probable cause, and Miranda warnings alone do not attenuate the taint of an illegal arrest. Good law.", "title": "Dunaway v. New York", "varies_by_point": "false"}}
```

### lake record — Dunaway v. New York

```json
{
  "schema_version": "s2.v1",
  "record_id": "Dunaway v. New York",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Dunaway v. New York",
    "case_name_short": "Dunaway",
    "case_name_full": "Dunaway v. New York",
    "input_case_name": "Dunaway v. New York",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-05",
    "year": 1979,
    "docket": "78-5066",
    "cluster_id": 110096,
    "lead_opinion_id": 110096,
    "sibling_ids": [
      110096,
      9427599,
      9427600,
      9427601,
      9427602
    ],
    "absolute_url": "/opinion/110096/dunaway-v-new-york/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "442 U.S. 200",
      "volume": "442",
      "reporter": "U.S.",
      "page": "200",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2248",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2248",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 824",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "824",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 126",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "126",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "442 U.S. 200",
        "volume": "442",
        "reporter": "U.S.",
        "page": "200",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2248",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2248",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "60 L. Ed. 2d 824",
        "volume": "60",
        "reporter": "L. Ed. 2d",
        "page": "824",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 126",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "126",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "442 U.S. 200",
    "official_selection": {
      "court_class": "scotus",
      "selected": "442 U.S. 200",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-216",
      "page": null,
      "quote": "--- # Dunaway v. New York *442 U.S. 200 (1979)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Investigating a killing during an attempted robbery, Rochester police picked up Dunaway, drove him to the station, and questioned him after Miranda warnings; he made incriminating statements and drew sketches implicating himself. He was never told he was under arrest, but he was not free to leave and would have been physically restrained had he tried. The State conceded the police lacked probable cause to arrest him. He moved to suppress the statements and sketches. ## Issue Whether police may seize a suspect on less than probable cause, transport him to the station, and detain him for custodial interrogation consistent with the Fourth Amendment \u2014 and, if not, whether the resulting confession must be suppressed. ## Rule No. A station-house detention for interrogation is a seizure that requires probable cause; it cannot be justified by a *Terry*-type balancing of interests.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-217",
      "page": null,
      "quote": "*Miranda* warnings, and the exclusion of a confession made without them, do not alone sufficiently deter a Fourth Amendment violation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-218",
      "page": null,
      "quote": "threshold requirement",
      "star_marker": "217",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 36446,
      "fragment": "#:~:text=%22-,threshold%20requirement",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-218b",
      "page": null,
      "quote": "virtually a replica",
      "star_marker": "218",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 38800,
      "fragment": "#:~:text=virtually%20a%20replica",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-05",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Dunaway v. New York",
    "varies_by_point": false,
    "scope_note": "Foundational: a station-house detention for interrogation requires probable cause, and Miranda warnings alone do not attenuate the taint of an illegal arrest. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Evelyn",
          "cluster_id": 4786331,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Michele Hall v. District of Columbia",
          "cluster_id": 4418006,
          "cite": [
            "867 F.3d 138",
            "2017 WL 3443060",
            "2017 U.S. App. LEXIS 14888"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cruz",
          "cluster_id": 2834741,
          "cite": [
            "131 A.D.3d 970",
            "16 N.Y.S.3d 584",
            "2015 WL 5124984"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Pyon v. State",
          "cluster_id": 2791489,
          "cite": [
            "222 Md. App. 412",
            "112 A.3d 1130",
            "2015 Md. App. LEXIS 50"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane1_negative"
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
        "journal_ref": "Dunaway v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Tennessee v. Courtney Bishop",
          "cluster_id": 2655823,
          "cite": [
            "431 S.W.3d 22",
            "2014 WL 888198",
            "2014 Tenn. LEXIS 189"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Danielle Kelly v. State of Indiana",
          "cluster_id": 2644345,
          "cite": [
            "997 N.E.2d 1045",
            "2013 WL 6122278",
            "2013 Ind. LEXIS 904"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane1_negative"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Place",
          "cluster_id": 110979,
          "cite": [
            "77 L. Ed. 2d 110",
            "103 S. Ct. 2637",
            "462 U.S. 696",
            "1983 U.S. LEXIS 74",
            "51 U.S.L.W. 4844"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": [
            "173 L. Ed. 2d 485",
            "129 S. Ct. 1710",
            "556 U.S. 332",
            "2009 U.S. LEXIS 3120"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
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
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ohio v. Robinette",
          "cluster_id": 118066,
          "cite": [
            "136 L. Ed. 2d 347",
            "117 S. Ct. 417",
            "519 U.S. 33",
            "1996 U.S. LEXIS 6971"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Dunaway v. New York:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110096 OR 9427599 OR 9427600 OR 9427601 OR 9427602) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjgyMDAzMjAwMDAwJnM9MTczNDU2JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110096+OR+9427599+OR+9427600+OR+9427601+OR+9427602%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110096 OR 9427599 OR 9427600 OR 9427601 OR 9427602)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMDM3JnM9MTEwNzU0JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110096+OR+9427599+OR+9427600+OR+9427601+OR+9427602%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110096 OR 9427599 OR 9427600 OR 9427601 OR 9427602)",
        "reviewed": 24,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 24,
        "triage_read": 0,
        "triage_snippet_classified": 24
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110096 OR 9427599 OR 9427600 OR 9427601 OR 9427602)",
    "indexed_citing_opinions": 2331,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110096,
        "count": 2149,
        "count_source": "search"
      },
      {
        "opinion_id": 9427599,
        "count": 234,
        "count_source": "search"
      },
      {
        "opinion_id": 9427600,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9427601,
        "count": 1,
        "count_source": "search"
      },
      {
        "opinion_id": 9427602,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 3635,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/dunaway-v-new-york.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg0NjU2Mzkmcz05NDI5NzY4JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28110096+OR+9427599+OR+9427600+OR+9427601+OR+9427602%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110096,
        "cited_id": 99506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 100567,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 104716,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 105963,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 106641,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 107831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 108571,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 108801,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109302,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109304,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110096,
        "cited_id": 2589474,
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
    "date_created": "2026-07-05T03:00:34Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:00:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:00:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:04:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:00:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Dunaway v. New York

```
<div>
<center><b><span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U.S. 200</a></span> (1979)</b></center>
<center><h1>DUNAWAY<br>
v.<br>
NEW YORK.</h1></center>
<center>No. 78-5066.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 21, 1979.</center>
<center>Decided June 5, 1979.</center>
CERTIORARI TO THE APPELLATE DIVISION, SUPREME COURT OF NEW YORK, FOURTH JUDICIAL DEPARTMENT.
<p><span class="star-pagination">*202</span> <i>Edward J. Nowak</i> argued the cause for petitioner. With him on the brief was <i>James M. Byrnes.</i></p>
<p><i>Melvin Bressler</i> argued the cause for respondent. With him on the brief was <i>Lawrence T. Kurlander.</i><sup>[*]</sup></p>
<p>MR. JUSTICE BRENNAN delivered the opinion of the Court.</p>
<p>We decide in this case the question reserved 10 years ago in <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/" aria-description="Citation for case: Morales v. New York">396 U. S. 102</a></span> (1969), namely, "the question of the legality of custodial questioning on less than probable cause for a full-fledged arrest." <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/#106" aria-description="Citation for case: Morales v. New York"><i>Id.,</i> at 106</a></span>.</p>
<p></p>
<h2>I</h2>
<p>On March 26, 1971, the proprietor of a pizza parlor in Rochester, N. Y., was killed during an attempted robbery. On August 10, 1971, Detective Anthony Fantigrossi of the <span class="star-pagination">*203</span> Rochester Police was told by another officer that an informant had supplied a possible lead implicating petitioner in the crime. Fantigrossi questioned the supposed source of the leada jail inmate awaiting trial for burglarybut learned nothing that supplied "enough information to get a warrant" for petitioner's arrest. App. 60.<sup>[1]</sup> Nevertheless, Fantigrossi ordered other detectives to "pick up" petitioner and "bring him in." <i>Id.,</i> at 54. Three detectives located petitioner at a neighbor's house on the morning of August 11. Petitioner was taken into custody; although he was not told he was under arrest, he would have been physically restrained if he had attempted to leave. Opinion in <i>People</i> v. <i>Dunaway</i> (Monroe County Ct., Mar. 11, 1977), App. 116, 117. He was driven to police headquarters in a police car and placed in an interrogation room, where he was questioned by officers after being given the warnings required by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Petitioner waived counsel and eventually made statements and drew sketches that incriminated him in the crime.<sup>[2]</sup></p>
<p>At petitioner's jury trial for attempted robbery and felony murder, his motions to suppress the statements and sketches were denied, and he was convicted. On appeal, both the <span class="star-pagination">*204</span> Appellate Division of the Fourth Department and the New York Court of Appeals initially affirmed the conviction without opinion. 42 App. Div. 2d 689, 346 N. Y. S. 2d 779 (1973), aff'd, 35 N. Y. 2d 741, <span class="citation" data-id="5529302"><a href="/opinion/5680952/syracuse-teachers-assn-v-board-of-education/" aria-description="Citation for case: Syracuse Teachers Ass&#x27;n v. Board of Education">320 N. E. 2d 646</a></span> (1974). However, this Court granted certiorari, vacated the judgment, and remanded the case for further consideration in light of the Court's supervening decision in <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975). <span class="citation multiple-matches"><a href="/c/U.%20S./422/1053/">422 U. S. 1053</a></span> (1975). The petitioner in <i>Brown,</i> like petitioner Dunaway, made inculpatory statements after receiving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings during custodial interrogation following his seizurein that case a formal arreston less than probable cause. Brown's motion to suppress the statements was also denied and the statements were used to convict him. Although the Illinois Supreme Court recognized that Brown's arrest was unlawful, it affirmed the admission of the statements on the ground that the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings served to break the causal connection between the illegal arrest and the giving of the statements. This Court reversed, holding that the Illinois courts erred in adopting a <i>per se</i> rule that <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in and of themselves sufficed to cure the Fourth Amendment violation; rather the Court held that in order to use such statements, the prosecution must show not only that the statements meet the Fifth Amendment voluntariness standard, but also that the causal connection between the statements and the illegal arrest is broken sufficiently to purge the primary taint of the illegal arrest in light of the distinct policies and interests of the Fourth Amendment.</p>
<p>In compliance with the remand, the New York Court of Appeals directed the Monroe County Court to make further factual findings as to whether there was a detention of petitioner, whether the police had probable cause, "and, in the event there was a detention and probable cause is not found for such detention, to determine the further question as to whether the making of the confessions was rendered infirm <span class="star-pagination">*205</span> by the illegal arrest (see <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span>, <i>supra</i>)." <i>People</i> v. <i>Dunaway,</i> 38 N. Y. 2d 812, 813-814, <span class="citation" data-id="5530272"><a href="/opinion/5681821/people-v-dunaway/#584" aria-description="Citation for case: People v. Dunaway">345 N. E. 2d 583, 584</a></span> (1975).</p>
<p>The County Court determined after a supplementary suppression hearing that Dunaway's motion to suppress should have been granted. Although reaffirming that there had been "full compliance with the mandate of <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i>" the County Court found that "this case does not involve a situation where the defendant voluntarily appeared at police headquarters in response to a request of the police . . . ." App. 117. The State's attempt to justify petitioner's involuntary investigatory detention on the authority of <i>People</i> v. <i>Morales,</i> 22 N. Y. 2d 55, <span class="citation" data-id="6225763"><a href="/opinion/6357047/people-v-morales/" aria-description="Citation for case: People v. Morales">238 N. E. 2d 307</a></span> (1968) which upheld a similar detention on the basis of information amounting to less than probable cause for arrestwas rejected on the grounds that the precedential value of <i>Morales</i> was questionable,<sup>[3]</sup> and that the controlling authority was the "strong language" in <i>Brown</i> v. <i>Illinois</i> indicating "disdain for custodial questioning without probable cause to arrest."<sup>[4]</sup> The County Court further held that "the factual predicate in this case did not amount to probable cause sufficient to support the arrest of the defendant," that "the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings by themselves did not purge the taint of the defendant's <span class="star-pagination">*206</span> illegal seizure[,] <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois, supra</a></span></i><i>,</i> and [that] there was no claim or showing by the People of any attenuation of the defendant's illegal detention," App. 121. Accordingly petitioner's motion to suppress was granted. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Ibid.</a></span></i></p>
<p>A divided Appellate Division reversed. Although agreeing that the police lacked probable cause to arrest petitioner, the majority relied on the Court of Appeals' reaffirmation, subsequent to the County Court's decision, that "[l]aw enforcement officials may detain an individual upon reasonable suspicion for questioning for a reasonable and brief period of time under carefully controlled conditions which are ample to protect the individual's Fifth and Sixth Amendment rights." 61 App. Div. 2d 299, 302, 402 N. Y. S. 2d 490, 492 (1978), quoting <i>People</i> v. <i>Morales,</i> 42 N. Y. 2d 129, 135, <span class="citation" data-id="5531084"><a href="/opinion/5682523/people-v-morales/#251" aria-description="Citation for case: People v. Morales">366 N. E. 2d 248, 251</a></span> (1977). The Appellate Division also held that even if petitioner's detention were illegal, the taint of his illegal detention was sufficiently attenuated to allow the admission of his statements and sketches. The Appellate Division emphasized that petitioner was never threatened or abused by the police and purported to distinguish <i>Brown</i> v. <i>Illinois</i><i>.</i><sup>[5]</sup> The Court of Appeals dismissed petitioner's application for leave to appeal. App. 134.</p>
<p>We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./439/979/">439 U. S. 979</a></span> (1978), to clarify the Fourth Amendment's requirements as to the permissible grounds for custodial interrogation and to review the New York court's application of <i>Brown</i> v. <i>Illinois</i><i>.</i> We reverse.</p>
<p></p>
<h2>II</h2>
<p>We first consider whether the Rochester police violated the Fourth and Fourteenth Amendments when, without probable cause to arrest, they took petitioner into custody, transported <span class="star-pagination">*207</span> him to the police station, and detained him there for interrogation.</p>
<p>The Fourth Amendment, applicable to the States through the Fourteenth Amendment, <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961), provides: "The right of the people to be secure in their persons . . . against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue but upon probable cause . . . ." There can be little doubt that petitioner was "seized" in the Fourth Amendment sense when he was taken involuntarily to the police station.<sup>[6]</sup> And respondent State concedes that the police lacked probable cause to arrest petitioner before his incriminating statement during interrogation.<sup>[7]</sup> Nevertheless respondent contends that the seizure of petitioner did not amount to an arrest and was therefore permissible under the Fourth Amendment because the police had a "reasonable suspicion" that petitioner possessed "intimate knowledge about a serious and unsolved crime." Brief for Respondent 10. We disagree.</p>
<p>Before <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), the Fourth <span class="star-pagination">*208</span> Amendment's guarantee against unreasonable seizures of persons was analyzed in terms of arrest, probable cause for arrest, and warrants based on such probable cause. The basic principles were relatively simple and straightforward: The term "arrest" was synonymous with those seizures governed by the Fourth Amendment. While warrants were not required in all circumstances,<sup>[8]</sup> the requirement of probable cause, as elaborated in numerous precedents,<sup>[9]</sup> was treated as absolute.<sup>[10]</sup> The "long-prevailing standards" of probable cause embodied "the best compromise that has been found for accommodating [the] often opposing interests" in "safeguard[ing] citizens from rash and unreasonable interferences with privacy" and in "seek[ing] to give fair leeway for enforcing the law in the community's protection." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 176</a></span> (1949). The standard of probable cause thus represented the accumulated wisdom of precedent and experience as to the minimum justification necessary to make the kind of intrusion involved in an arrest "reasonable" under the Fourth Amendment. The standard applied to all arrests, without the need to "balance" the interests and circumstances involved in particular situations. Cf. <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967).</p>
<p><i>Terry</i> for the first time recognized an exception to the requirement that Fourth Amendment seizures of persons must <span class="star-pagination">*209</span> be based on probable cause. That case involved a brief, on-the-spot stop on the street and a frisk for weapons, a situation that did not fit comfortably within the traditional concept of an "arrest." Nevertheless, the Court held that even this type of "necessarily swift action predicated upon the on-the-spot observations of the officer on the beat" constituted a "serious intrusion upon the sanctity of the person, which may inflict great indignity and arouse strong resentment," <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 20, 17</a></span>, and therefore "must be tested by the Fourth Amendment's general proscription against unreasonable searches and seizures." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 20</a></span>. However, since the intrusion involved in a "stop and frisk" was so much less severe than that involved in traditional "arrests," the Court declined to stretch the concept of "arrest"and the general rule requiring probable cause to make arrests "reasonable" under the Fourth Amendmentto cover such intrusions. Instead, the Court treated the stop-and-frisk intrusion as a <i>sui generis</i> "rubric of police conduct," <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">ibid.</a></span></i> And to determine the justification necessary to make this specially limited intrusion "reasonable" under the Fourth Amendment, the Court balanced the limited violation of individual privacy involved against the opposing interests in crime prevention and detection and in the police officer's safety. <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#22" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 22-27</a></span>. As a consequence, the Court established "a narrowly drawn authority to permit a reasonable search for weapons for the protection of the police officer, where he has reason to believe that he is dealing with an armed and dangerous individual, regardless of whether he has probable cause to arrest the individual for a crime." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#27" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 27</a></span>.<sup>[11]</sup> Thus, <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> departed from traditional Fourth Amendment analysis in two respects. <span class="star-pagination">*210</span> First, it defined a special category of Fourth Amendment "seizures" so substantially less intrusive than arrests that the general rule requiring probable cause to make Fourth Amendment "seizures" reasonable could be replaced by a balancing test. Second, the application of this balancing test led the Court to approve this narrowly defined less intrusive seizure on grounds less rigorous than probable cause, but only for the purpose of a pat-down for weapons.</p>
<p>Because <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> involved an exception to the general rule requiring probable cause, this Court has been careful to maintain its narrow scope. <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> itself involved a limited, on-the-street frisk for weapons.<sup>[12]</sup> Two subsequent cases which applied <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> also involved limited weapons frisks. See <i>Adams</i> v. <i>Williams,</i> <span class="citation" data-id="9424935"><a href="/opinion/108571/adams-v-williams/" aria-description="Citation for case: Adams v. Williams">407 U. S. 143</a></span> (1972) (frisk for weapons on basis of reasonable suspicion); <i>Pennsylvania</i> v. <i>Mimms,</i> <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106</a></span> (1977) (order to get out of car is permissible <i>"de minimis"</i> intrusion after car is lawfully detained for traffic violations; frisk for weapons justified after "bulge" observed in jacket). <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873</a></span> (1975), applied <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> in the special context of roving border patrols stopping automobiles to check for illegal immigrants. The investigative stops usually consumed <span class="star-pagination">*211</span> less than a minute and involved "a brief question or two." 422 U. S., at 880. The Court stated that "[b]ecause of the limited nature of the intrusion, stops of this sort may be justified on facts that do not amount to the probable cause required for an arrest." <i>Ibid.</i><sup>[13]</sup> See also <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976) (fixed checkpoint to stop and check vehicles for aliens); <i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648</a></span> (1979) (random checks for drivers' licenses and proper vehicle registration not permitted on less than articulable reasonable suspicion).</p>
<p>Respondent State now urges the Court to apply a balancing test, rather than the general rule, to custodial interrogations, and to hold that "seizures" such as that in this case may be justified by mere "reasonable suspicion."<sup>[14]</sup><i>Terry</i> and its <span class="star-pagination">*212</span> progeny clearly do not support such a result. The narrow intrusions involved in those cases were judged by a balancing test rather than by the general principle that Fourth Amendment seizures must be supported by the "long-prevailing standards" of probable cause, <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#176" aria-description="Citation for case: Brinegar v. United States">338 U. S., at 176</a></span>, only because these intrusions fell far short of the kind of intrusion associated with an arrest. Indeed, <i><span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/" aria-description="Citation for case: United States v. Brignoni-Ponce">Brignoni-Ponce</a></span></i> expressly refused to extend <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> in the manner respondent now urges. The Court there stated: "The officer may question the driver and passengers about their citizenship and immigration status, and he may ask them to explain suspicious circumstances, <i>but any further detention or search must be based on consent or probable cause."</i> 422 U. S., at 881-882 (emphasis added). Accord, <i>United States</i> v. <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#567" aria-description="Citation for case: United States v. Martinez-Fuerte"><i>Martinez-Fuerte, supra,</i> at 567</a></span>.</p>
<p>In contrast to the brief and narrowly circumscribed intrusions involved in those cases, the detention of petitioner was in important respects indistinguishable from a traditional arrest. Petitioner was not questioned briefly where he was found. Instead, he was taken from a neighbor's home to a police car, transported to a police station, and placed in an interrogation room. He was never informed that he was "free to go"; indeed, he would have been physically restrained if he had refused to accompany the officers or had tried to escape their custody. The application of the Fourth Amendment's requirement of probable cause does not depend on whether an intrusion of this magnitude is termed an "arrest" under state law. The mere facts that petitioner was not told he was under arrest, was not "booked," and would not have had an arrest record if the interrogation had proved fruitless, while not insignificant for all purposes, see <i>Cupp</i> v. <i>Murphy,</i> <span class="citation" data-id="9425320"><a href="/opinion/108801/cupp-v-murphy/" aria-description="Citation for case: Cupp v. Murphy">412 U. S. 291</a></span> (1973), obviously do not make petitioner's <span class="star-pagination">*213</span> seizure even roughly analogous to the narrowly defined intrusions involved in <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> and its progeny. Indeed, any "exception" that could cover a seizure as intrusive as that in this case would threaten to swallow the general rule that Fourth Amendment seizures are "reasonable" only if based on probable cause.</p>
<p>The central importance of the probable-cause requirement to the protection of a citizen's privacy afforded by the Fourth Amendment's guarantees cannot be compromised in this fashion. "The requirement of probable cause has roots that are deep in our history." <i>Henry</i> v. <i>United States,</i> <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#100" aria-description="Citation for case: Henry v. United States">361 U. S. 98, 100</a></span> (1959). Hostility to seizures based on mere suspicion was a prime motivation for the adoption of the Fourth Amendment, and decisions immediately after its adoption affirmed that "common rumor or report, suspicion, or even `strong reason to suspect' was not adequate to support a warrant for arrest." <span class="citation" data-id="9421885"><a href="/opinion/105963/henry-v-united-states/#101" aria-description="Citation for case: Henry v. United States"><i>Id.,</i> at 101</a></span> (footnotes omitted). The familiar threshold standard of probable cause for Fourth Amendment seizures reflects the benefit of extensive experience accommodating the factors relevant to the "reasonableness" requirement of the Fourth Amendment, and provides the relative simplicity and clarity necessary to the implementation of a workable rule. See <i>Brinegar</i> v. <i>United States, supra,</i> at 175-176.</p>
<p>In effect, respondent urges us to adopt a multifactor balancing test of "reasonable police conduct under the circumstances" to cover all seizures that do not amount to technical arrests.<sup>[15]</sup> But the protections intended by the Framers could all too easily disappear in the consideration and balancing of the multifarious circumstances presented by different cases, especially when that balancing may be done in the first instance by police officers engaged in the "often competitive enterprise of ferreting out crime." <i>Johnson</i> v. <i>United States,</i> <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14</a></span> (1948). A single, familiar standard is essential to <span class="star-pagination">*214</span> guide police officers, who have only limited time and expertise to reflect on and balance the social and individual interests involved in the specific circumstances they confront.<sup>[16]</sup> Indeed, our recognition of these dangers, and our consequent reluctance to depart from the proved protections afforded by the general rule, are reflected in the narrow limitations emphasized in the cases employing the balancing test. For all but those narrowly defined intrusions, the requisite "balancing" has been performed in centuries of precedent and is embodied in the principle that seizures are "reasonable" only if supported by probable cause.</p>
<p>Moreover, two important decisions since <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> confirm the conclusion that the treatment of petitioner, whether or not it is technically characterized as an arrest, must be supported by probable cause. <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), decided the Term after <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span>,</i> considered whether fingerprints taken from a suspect detained without probable cause must be excluded from evidence. The State argued that the detention "was of a type which does not require probable cause," <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S., at 726</a></span>, because it occurred during an investigative, rather than accusatory, stage, and because it was for the sole purpose of taking fingerprints. Rejecting the State's first argument, the Court warned:</p>
<blockquote>"[T]o argue that the Fourth Amendment does not apply to the investigatory stage is fundamentally to misconceive the purposes of the Fourth Amendment. Investigatory seizures would subject unlimited numbers of innocent persons to the harassment and ignominy incident to involuntary detention. Nothing is more clear than that the Fourth Amendment was meant to prevent wholesale intrusions upon the personal security of our <span class="star-pagination">*215</span> citizenry, whether these intrusions be termed `arrests' or `investigatory detentions.'" <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi"><i>Id.,</i> at 726-727</a></span>.</blockquote>
<p>The State's second argument in <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span></i> was more substantial, largely because of the <i>distinctions</i> between taking fingerprints and interrogation:</p>
<blockquote>"Fingerprinting involves none of the probing into an individual's private life and thoughts that marks an interrogation or search. Nor can fingerprint detention be employed repeatedly to harass any individual, since the police need only one set of each person's prints. Furthermore, fingerprinting is an inherently more reliable and effective crime-solving tool than eyewitness identifications or confessions and is not subject to such abuses as the improper line-up and the `third degree.' Finally, because there is no danger of destruction of fingerprints, the limited detention need not come unexpectedly or at an inconvenient time." <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#727" aria-description="Citation for case: Davis v. Mississippi"><i>Id.,</i> at 727</a></span>.</blockquote>
<p>In <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>,</i> however, the Court found it unnecessary to decide the validity of a "narrowly circumscribed procedure for obtaining" the fingerprints of suspects without probable cause in part because, as the Court emphasized, "petitioner was not merely fingerprinted during the . . . detention but <i>also subjected to interrogation.</i>" <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#728" aria-description="Citation for case: Davis v. Mississippi"><i>Id.,</i> at 728</a></span> (emphasis added). The detention therefore violated the Fourth Amendment.</p>
<p><i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), similarly disapproved arrests made for "investigatory" purposes on less than probable cause. Although Brown's arrest had more of the trappings of a technical formal arrest than petitioner's, such differences in form must not be exalted over substance.<sup>[17]</sup><span class="star-pagination">*216</span> Once in the police station, Brown was taken to an interrogation room, and his experience was indistinguishable from petitioner's. Our condemnation of the police conduct in <i>Brown</i> fits equally the police conduct in this case:</p>
<blockquote>"The impropriety of the arrest was obvious; awareness of the fact was virtually conceded by the two detectives when they repeatedly acknowledged, in their testimony, that the purpose of their action was `for investigation' or for `questioning.' . . . The arrest, both in design and in execution, was investigatory. The detectives embarked upon this expedition for evidence in the hope that something might turn up." <i>Id.,</i> at 605.</blockquote>
<p>See also <i>id.,</i> at 602.</p>
<p>These passages from <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span></i> and <i>Brown</i> reflect the conclusion that detention for custodial interrogationregardless of its labelintrudes so severely on interests protected by the Fourth Amendment as necessarily to trigger the traditional safeguards against illegal arrest. We accordingly hold that the Rochester police violated the Fourth and Fourteenth Amendments when, without probable cause, they seized petitioner and transported him to the police station for interrogation.</p>
<p></p>
<h2>III</h2>
<p>There remains the question whether the connection between this unconstitutional police conduct and the incriminating statements and sketches obtained during petitioner's illegal detention was nevertheless sufficiently attenuated to permit the use at trial of the statements and sketches. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963); <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/" aria-description="Citation for case: Nardone v. United States">308 U. S. 338</a></span> (1939); <i>Silverthorne Lumber Co.</i> v. <i>United States,</i> <span class="citation" data-id="99506"><a href="/opinion/99506/silverthorne-lumber-co-v-united-states/" aria-description="Citation for case: Silverthorne Lumber Co. v. United States">251 U. S. 385</a></span> (1920).</p>
<p>The New York courts have consistently held, and petitioner does not contest, that proper <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given and that his statements were "voluntary" for purposes of the Fifth Amendment. But <i>Brown</i> v. <i><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">Illinois, supra</a></span></i><i>,</i> settled that <span class="star-pagination">*217</span> "[t]he exclusionary rule, . . . when utilized to effectuate the Fourth Amendment, serves interests and policies that are distinct from those it serves under the Fifth," 422 U. S., at 601, and held therefore that "<span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona"><i>Miranda</i></a></span> warnings, and the exclusion of a confession made without them, do not alone sufficiently deter a Fourth Amendment violation." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i></p>
<blockquote>"If <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, by themselves, were held to attenuate the taint of an unconstitutional arrest, regardless of how wanton and purposeful the Fourth Amendment violation, the effect of the exclusionary rule would be substantially diluted. . . . Arrests made without warrant or without probable cause, for questioning or `investigation,' would be encouraged by the knowledge that evidence derived therefrom could well be made admissible at trial by the simple expedient of giving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings." <i>Id.,</i> at 602.</blockquote>
<p>Consequently, although a confession after proper <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings may be found "voluntary" for purposes of the Fifth Amendment,<sup>[18]</sup> this type of "voluntariness" is merely a "threshold requirement" for Fourth Amendment analysis, 422 U. S., at 604. Indeed, if the Fifth Amendment has been violated, the Fourth Amendment issue would not have to be reached.</p>
<p>Beyond this threshold requirement, <i>Brown</i> articulated a test designed to vindicate the "distinct policies and interests of the Fourth Amendment." <i>Id.,</i> at 602. Following <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> the Court eschewed any <i>per se</i> or "but for" rule, and identified the relevant inquiry as "whether Brown's statements were obtained by exploitation of the illegality of his arrest," 422 U. S., at 600; see <i>Wong Sun</i> v. <i>United States, supra,</i> at 488. <i>Brown's</i> focus on "the causal connection between the illegality and the confession," 422 U. S., at 603, reflected the two policies behind the use of the exclusionary rule to effectuate <span class="star-pagination">*218</span> the Fourth Amendment. When there is a close causal connection between the illegal seizure and the confession, not only is exclusion of the evidence more likely to deter similar police misconduct in the future, but use of the evidence is more likely to compromise the integrity of the courts.</p>
<p><i>Brown</i> identified several factors to be considered "in determining whether the confession is obtained by exploitation of an illegal arrest[: t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct . . . . And the burden of showing admissibility rests, of course, on the prosecution." <i>Id.,</i> at 603-604.<sup>[19]</sup> Examining the case before it, the Court readily concluded that the State had failed to sustain its burden of showing the confession was admissible. In the "less than two hours" that elapsed between the arrest and the confession "there was no intervening event of significance whatsoever." <i>Ibid.</i> Furthermore, the arrest without probable cause had a "quality of purposefulness" in that it was an "expedition for evidence" admittedly undertaken "in the hope that something might turn up." <i>Id.,</i> at 605.</p>
<p>The situation in this case is virtually a replica of the situation in <i>Brown.</i> Petitioner was also admittedly seized without probable cause in the hope that something might turn up, and confessed without any intervening event of significance.<sup>[20]</sup> Nevertheless, three members of the Appellate Division purported to distinguish <i>Brown</i> on the ground that the police did not threaten or abuse petitioner (presumably putting aside his illegal seizure and detention) and that the police <span class="star-pagination">*219</span> conduct was "highly protective of defendant's Fifth and Sixth Amendment rights." 61 App. Div. 2d, at 303, 402 N. Y. S. 2d, at 493. This betrays a lingering confusion between "voluntariness" for purposes of the Fifth Amendment and the "causal connection" test established in <i>Brown.</i> Satisfying the Fifth Amendment is only the "threshold" condition of the Fourth Amendment analysis required by <i>Brown.</i> No intervening events broke the connection between petitioner's illegal detention and his confession. To admit petitioner's confession in such a case would allow "law enforcement officers to violate the Fourth Amendment with impunity, safe in the knowledge that they could wash their hands in the `procedural safeguards' of the Fifth."<sup>[21]</sup></p>
<p><i>Reversed.</i></p>
<p>MR. JUSTICE POWELL took no part in the consideration or decision of this case.</p>
<p>Mr. JUSTICE WHITE, concurring.</p>
<p>The opinion of the Court might be read to indicate that <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), is an almost unique exception to a hard-and-fast standard of probable cause. As our prior cases hold, however, the key principle of the Fourth Amendment is reasonablenessthe balancing of competing interests. <i>E. g., </i><i>Delaware</i> v. <i>Prouse,</i> <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#653" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 653-654</a></span> (1979); <i>Michigan</i> v. <i>Tyler,</i> <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#506" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 506</a></span> (1978); <i>Marshall</i> v. <i>Barlow's, Inc.,</i> <span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/#321" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307, 321-322</a></span> (1978); <i>United States</i> v. <i>Martinez-Fuerte,</i> <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#555" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 555</a></span> (1976); <i>United States</i> v. <i>Brignoni-Ponce,</i> <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975); <i>Terry</i> v. <i>Ohio, supra,</i> at 20-21; <i>Camara</i> v. <i>Municipal Court,</i> <span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#536" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 536-537</a></span> (1967). But if courts and law enforcement officials are to have workable rules, see <i>Rakas</i> v. <i>Illinois,</i> <span class="citation" data-id="9427384"><a href="/opinion/109953/rakas-v-illinois/#168" aria-description="Citation for case: Rakas v. Illinois">439 U. S. 128, 168</a></span> (1978) (dissenting opinion), this balancing must in large part be done on a categorical basisnot in an ad hoc, case-by-case <span class="star-pagination">*220</span> fashion by individual police officers. Cf. <i>Mincey</i> v. <i>Arizona,</i> <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#394" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385, 394-395</a></span> (1978). On the other hand, the need for rules of general applicability precludes neither the recognition in particular cases of extraordinary private or public interests, cf. <i>Zurcher</i> v. <i>Stanford Daily,</i> <span class="citation" data-id="9427224"><a href="/opinion/109876/zurcher-v-stanford-daily/#564" aria-description="Citation for case: Zurcher v. Stanford Daily">436 U. S. 547, 564-565</a></span> (1978), nor the generic recognition of certain exceptions to the normal rule of probable cause where more flexibility is essential. Cf., <i>e. g., </i><i>Terry</i> v. <i>Ohio, supra</i><i>.</i> It is enough, for me, that the police conduct here is similar enough to an arrest that the normal level of probable cause is necessary before the interests of privacy and personal security must give way.</p>
<p>MR. JUSTICE STEVENS, concurring.</p>
<p>Although I join the Court's opinion, I add this comment on the significance of two factors that may be considered when determining whether a confession has been obtained by exploitation of an illegal arrest.</p>
<p>The temporal relationship between the arrest and the confession may be an ambiguous factor. If there are no relevant intervening circumstances, a prolonged detention may well be a more serious exploitation of an illegal arrest than a short one. Conversely, even an immediate confession may have been motivated by a prearrest event such as a visit with a minister.</p>
<p>The flagrancy of the official misconduct is relevant, in my judgment, only insofar as it has a tendency to motivate the defendant. A midnight arrest with drawn guns will be equally frightening whether the police acted recklessly or in good faith. Conversely, a courteous command has the same effect on the arrestee whether the officer thinks he has probable cause or knows that he does not. In either event, if the Fourth Amendment is violated, the admissibility question will turn on the causal relationship between that violation and the defendant's subsequent confession.</p>
<p>I recognize that the deterrence rationale for the exclusionary <span class="star-pagination">*221</span> rule is sometimes interpreted quite differently.<sup>[1]</sup> Under that interpretation, exclusion is applied as a substitute for punishment of the offending officer; if he acted recklessly or flagrantly, punishment is appropriate, but if he acted in good faith, it is not.<sup>[2]</sup> But when evidence is excluded at a criminal trial, it is the broad societal interest in effective law enforcement that suffers. The justification for the exclusion of evidence obtained by improper methods is to motivate the law enforcement profession as a wholenot the aberrant individual officerto adopt and enforce regular procedures that will avoid the future invasion of the citizen's constitutional rights. For that reason, exclusionary rules should embody objective criteria rather than subjective considerations.</p>
<p>MR. JUSTICE REHNQUIST, with whom THE CHIEF JUSTICE joins, dissenting.</p>
<p>If the Court did no more in this case than it announced in the opening sentence of its opinion"decide . . . the question reserved 10 years ago in <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/" aria-description="Citation for case: Morales v. New York">396 U. S. 102</a></span> (1969), namely, `the question of the legality of custodial questioning on less than probable cause for a full-fledged arrest'" I would have little difficulty joining its opinion. The decision of this question, however, does not, contrary to the implication in the Court's opening sentence, decide this case. For the Court goes on to conclude that petitioner Dunaway was in fact "seized" within the meaning of the Fourth Amendment, and that the connection between Dunaway's purported detention and the evidence obtained therefrom was not sufficiently attenuated as to dissipate the taint of the alleged unlawful police conduct. <i>Ante,</i> at 207, 216-219. I cannot agree with either conclusion, and accordingly, I dissent.</p>
<p></p>
<h2>
<span class="star-pagination">*222</span> I</h2>
<p>There is obviously nothing in the Fourth Amendment that prohibits police from calling from their vehicle to a particular individual on the street and asking him to come over and talk with them; nor is there anything in the Fourth Amendment that prevents the police from knocking on the door of a person's house and when the person answers the door, inquiring whether he is willing to answer questions that they wish to put to him. "Obviously, not all personal intercourse between policemen and citizens involves `seizures' of persons." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span>, 19 n. 16 (1968). Voluntary questioning not involving any "seizure" for Fourth Amendment purposes may take place under any number of varying circumstances. And the occasions will not be few when a particular individual agrees voluntarily to answer questions that the police wish to put to him either on the street, at the station, or in his house, and later regrets his willingness to answer those questions. However, such morning-after regrets do not render involuntary responses that were voluntary at the time they were made. In my view, this is a case where the defendant voluntarily accompanied the police to the station to answer their questions.</p>
<p>In <i>Terry</i> v. <i>Ohio</i><i>,</i> the Court set out the test for determining whether a person has been "seized" for Fourth Amendment purposes. "Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a `seizure' has occurred." <i>Ibid.</i> In this case three police officers were dispatched to petitioner's house to question him about his participation in a robbery According to the testimony of the police officers, one officer approached a house where petitioner was thought to be located and knocked on the door. When a person answered the door, the officer identified himself and asked the individual his name. App. 97-98. After learning that the person who answered the door was <span class="star-pagination">*223</span> petitioner, the officer asked him if he would accompany the officers to police headquarters for questioning, and petitioner responded that he would. <i>Id.,</i> at 89-90; see 61 App. Div. 2d 299, 301, 402 N. Y. S. 2d 490, 491 (1978). Petitioner was not told that he was under arrest or in custody and was not warned not to resist or flee. No weapons were displayed and petitioner was not handcuffed. Each officer testified that petitioner was not touched or held during the trip downtown; his freedom of action was not in any way restrained by the police. App. 78-79, 99. In short, the police behavior in this case was entirely free of "physical force or show of authority."</p>
<p>The Court, however, categorically states in text that "[t]here can be little doubt that petitioner was `seized' in the Fourth Amendment sense when he was taken involuntarily to the police station." <i>Ante,</i> at 207. In an accompanying footnote, the Court states: "Respondent contends that petitioner accompanied the police voluntarily and therefore was not `seized.' . . . The County Court found otherwise . . . and the Appellate Division treated the case as an involuntary detention justified by reasonable suspicion." <i>Ante,</i> at 207 n. 6. The Court goes on to cite a commentary from the Tentative Draft of the ALI Model Code of Pre-Arraignment Procedure to the effect that a "request to come to [the] police station `may easily carry an implication of obligation, while the appearance itself, unless clearly stated to be voluntary, may be an awesome experience for the ordinary citizen.'" <i>Ibid.</i></p>
<p>The Court's heavy reliance on the conclusions of the Monroe County Court on this issue is misplaced, however. That court clearly did not apply the <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> standard in determining whether there had been a seizure. Instead, that court's conclusions were based solely on the facts that petitioner was in the physical custody of detectives until he reached police headquarters and that "had he attempted to leave the company of the said detectives, they would have physically restrained him (per stipulation of People at conclusion of hearing)." App. 117. But the fact that the officers accompanied <span class="star-pagination">*224</span> petitioner from his house to the station in no way vitiates the State's claim that petitioner acted voluntarily. Similarly, the unexpressed intentions of police officers as to hypothetical situations have little bearing on the question whether the police conduct, objectively viewed, restrained petitioner's liberty by show of force or authority.</p>
<p>The Appellate Division's opinion also can be of no assistance to the Court. The Court's opinion characterizes the Appellate Division's treatment of the case "as an involuntary detention justified by reasonable suspicion." <i>Ante,</i> at 207 n. 6. But the Appellate Division did not accept the County Court's conclusion that petitioner did not voluntarily accompany the police to the station. To the contrary, in its recitation of the facts, the Appellate Division recites the officers' testimony that petitioner voluntarily agreed to come downtown to talk with them. 61 App. Div. 2d, at 301, 302, 402 N. Y. S. 2d, at 491, 492. That the Appellate Division found that it was able to resolve the case on the basis of the Court of Appeals' decision in <i>People</i> v. <i>Morales,</i> 42 N. Y. 2d 129, <span class="citation" data-id="5531084"><a href="/opinion/5682523/people-v-morales/" aria-description="Citation for case: People v. Morales">366 N. E. 2d 248</a></span> (1977), does not mean that the Appellate Division decided that petitioner had been "seized" within the meaning of the Fourth Amendment.</p>
<p>Finally, the Court quotes the Model Code for Pre-Arraignment Procedure to support its assertion. <i>Ante,</i> at 207 n. 6. I do not dispute the fact that a police request to come to the station may indeed be an "awesome experience." But I do not think that that fact alone means that in every instance where a person assents to a police request to come to headquarters, there has been a "seizure" within the meaning of the Fourth Amendment. The question turns on whether the officer's conduct is objectively coercive or physically threatening, not on the mere fact that a person might in some measure feel cowed by the fact that a request is made by a police officer. Cf. <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495</a></span> (1977).<sup>[1]</sup></p>
<p><span class="star-pagination">*225</span> Therefore, although I agree that the police officers in this case did not have that degree of suspicion or probable cause that would have justified them in physically compelling petitioner to accompany them to the police station for questioning, I do not believe that the record demonstrates as a fact that this is what happened. No involuntary detention for questioning, was shown to have taken place. The Fourth Amendment, accordingly, does not require suppression of petitioner's statements.</p>
<p></p>
<h2>II</h2>
<p>Assuming, <i>arguendo,</i> that there was a "seizure" in this case, I still cannot agree with the Court that the Fourth Amendment requires suppression of petitioner's statements and sketches. Relying on <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), the Court concludes that this evidence must be suppressed primarily, it seems, because no intervening events broke the connection between petitioner's detention and his confession. <i>Ante,</i> at 219. In my view, the connection between petitioner's allegedly unlawful detention and the incriminating statements and sketches is sufficiently attenuated to permit their use at trial. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).</p>
<p><span class="star-pagination">*226</span> In <i>Brown</i> v. <i>Illinois, supra</i><i>,</i> we identified several factors to be considered in determining whether inculpatory statements were sufficiently a product of free will to be admissible under the Fourth Amendment. The voluntariness of the statements is a threshold requirement. That <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are given is "an important factor." 422 U. S., at 603-604. Also relevant are "[t]he temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct." <i>Ibid.</i> But the Court did not assign equal weight to each of these factors. Given the deterrent purposes of the exclusionary rule, the "purpose and flagrancy" of the police conduct is, in my view, the most important factor. Where police have acted in good faith and not in a flagrant manner, I would require no more than that proper <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings be given and that the statement be voluntary within the meaning of the Fifth Amendment. <i>Brown</i> v. <i>Illinois, supra,</i> at 612 (POWELL, J., concurring in part). "Absent aggravating circumstances, I would consider a statement given at the station house after one has been advised of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights to be sufficiently removed from the immediate circumstances of the illegal arrest to justify its admission at trial." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i></p>
<p>The Court concedes that petitioner received proper <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and that his statements were "voluntary" for purposes of the Fifth Amendment. <i>Ante,</i> at 216. And the police acted in good faith. App. 61; see <i>United States</i> v. <i>Peltier,</i> <span class="citation" data-id="9426173"><a href="/opinion/109302/united-states-v-peltier/#536" aria-description="Citation for case: United States v. Peltier">422 U. S. 531, 536-537</a></span> (1975). At the time of petitioner's detention, the New York Court of Appeals had held that custodial questioning on less than probable cause for an arrest was permissible under the Fourth Amendment. <i>People</i> v. <i>Morales,</i> 22 N. Y. 2d 55, <span class="citation" data-id="6225763"><a href="/opinion/6357047/people-v-morales/" aria-description="Citation for case: People v. Morales">238 N. E. 2d 307</a></span> (1968).<sup>[2]</sup> Petitioner <span class="star-pagination">*227</span> testified that the police never threatened or abused him. App. 35. Petitioner voluntarily gave his first statement to police about an hour after he reached the police station and then gave another statement to police the following day. Contrary to the Court's suggestion, the police conduct in this case was in no manner as flagrant as that of the police in <i>Brown</i> v. <i>Illinois, supra</i><i>.</i> See 422 U. S., at 605; n. 1, <i>supra.</i> Thus, in my view, the record convincingly demonstrates that the statements and sketches given police by petitioner were of sufficient free will as to purge the primary taint of his alleged illegal detention. I would, therefore, affirm the judgment of the Appellate Division of the Supreme Court of New York.</p>
<h2>NOTES</h2>
<p>[*]  <i>Richard Emery</i> and <i>Joel M. Gora</i> filed a brief for the American Civil Liberties Union et al. as <i>amici curiae</i> urging reversal.</p>
<p>[1]  See opinion in <i>People</i> v. <i><span class="citation" data-id="5530272"><a href="/opinion/5681821/people-v-dunaway/" aria-description="Citation for case: People v. Dunaway">Dunaway</a></span></i> (Monroe County Ct., Mar. 11, 1977), App. 116-117. An informant had reportedly told the other detective that one James Cole had said that he and someone named "Irving" had been involved in the crime. The informant did not know "Irving's" last name, but had identified a picture of petitioner Dunaway from a police file. After hearing this information, Fantigrossi interviewed Cole, who was in jail pending an indictment for burglary. Cole denied any involvement in the crime, but stated that he had been told about it two months earlier by another inmate, Hubert Adams. According to Cole, Adams had mentioned that his younger brother, Ba Ba Adams, had told him that he and a fellow named "Irving," also known as "Axelrod," had been involved in the crime.</p>
<p>[2]  See 61 App. Div. 2d 299, 301, 402 N. Y. S. 2d 490, 491 (1978). The first statement was made within an hour after Dunaway reached the police station; the following day he made a second, more complete statement.</p>
<p>[3]  We granted certiorari in <i>Morales</i> and noted that "[t]he ruling below, that the State may detain for custodial questioning on less than probable cause for a traditional arrest, is manifestly important, goes beyond our subsequent decisions in <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968), and <i>Sibron</i> v. <i>New York,</i> <span class="citation" data-id="9423756"><a href="/opinion/107730/sibron-v-new-york/" aria-description="Citation for case: Sibron v. New York">392 U. S. 40</a></span> (1968), and is claimed by petitioner to be at odds with <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969)." <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/#104" aria-description="Citation for case: Morales v. New York">396 U. S. 102, 104-105</a></span> (1969). Nevertheless, inadequacies in the record led us to remand for further development and to reserve the issue we decide today for a record that "squarely and necessarily presents the issue and fully illuminates the factual context in which the question arises." <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/#105" aria-description="Citation for case: Morales v. New York"><i>Id.,</i> at 105</a></span>. On remand, the New York courts determined that Morales had gone to the police voluntarily. <i>People</i> v. <i>Morales,</i> 42 N. Y. 2d 129, 137-138, <span class="citation" data-id="5531084"><a href="/opinion/5682523/people-v-morales/#252" aria-description="Citation for case: People v. Morales">366 N. E. 2d 248, 252-253</a></span> (1977).</p>
<p>[4]  App. 118; see <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#602" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 602, 605</a></span>.</p>
<p>[5]  61 App. Div. 2d, at 303-304, 402 N. Y. S. 2d, at 493. Two of the five members of the court dissented on this issue. <i>Id.,</i> at 304, 402 N. Y. S. 2d, at 493 (Denman, J., concurring); <i>id.,</i> at 305, 402 N. Y. S. 2d, at 494 (Cardamone, J., dissenting).</p>
<p>[6]  "It must be recognized that whenever a police officer accosts an individual and restrains his freedom to walk away, he has `seized' that person." <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16</a></span> (1968). Respondent contends that petitioner accompanied the police voluntarily and therefore was not "seized." Brief for Respondent 7-9. The County Court found otherwise, App. 117, quoted <i>supra,</i> at 205; and the Appellate Division treated the case as an involuntary detention justified by reasonable suspicion. See 61 App. Div. 2d, at 302-303, 402 N. Y. S. 2d, at 492. See also ALI, Model Code of Pre-Arraignment Procedure § 2.01 (3) and commentary, p. 91 (Tent. Draft No. 1, 1966) (request to come to police station "may easily carry an implication of obligation, while the appearance itself, unless clearly stated to be voluntary, may be an awesome experience for the ordinary citizen").</p>
<p>[7]  Both the County Court and the Appellate Division found that the police lacked probable cause, and respondent does not question those findings here. See 61 App. Div. 2d, at 302, 402 N. Y. S. 2d, at 492; App. 120, citing <i>Spinelli</i> v. <i>United States,</i> <span class="citation" data-id="9423895"><a href="/opinion/107831/spinelli-v-united-states/" aria-description="Citation for case: Spinelli v. United States">393 U. S. 410</a></span> (1969); <i>Aguilar</i> v. <i>Texas,</i> <span class="citation" data-id="9422845"><a href="/opinion/106865/aguilar-v-texas/" aria-description="Citation for case: Aguilar v. Texas">378 U. S. 108</a></span> (1964).</p>
<p>[8]  See, <i>e. g., </i><i>Warden</i> v. <i>Hayden,</i> <span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294</a></span> (1967) (hot pursuit); <i>United States</i> v. <i>Watson,</i> <span class="citation" data-id="9426247"><a href="/opinion/109352/united-states-v-watson/" aria-description="Citation for case: United States v. Watson">423 U. S. 411</a></span> (1976) (felony arrests in public places).</p>
<p>[9]  "Probable cause exists where `the facts and circumstances within their [the officers'] knowledge and of which they had reasonably trustworthy information [are] sufficient in themselves to warrant a man of reasonable caution in the belief that' an offense has been or is being committed [by the person to be arrested]." <i>Brinegar</i> v. <i>United States,</i> <span class="citation" data-id="9420390"><a href="/opinion/104716/brinegar-v-united-states/#175" aria-description="Citation for case: Brinegar v. United States">338 U. S. 160, 175-176</a></span> (1949), quoting <i>Carroll</i> v. <i>United States,</i> <span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#162" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 162</a></span> (1925). See generally 2 W. LaFave, Search and Seizure: A Treatise on the Fourth Amendment 436-480 (1978).</p>
<p>[10]  See <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#111" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 111-112</a></span> (1975); <i>Ker</i> v. <i>California,</i> <span class="citation" data-id="9422640"><a href="/opinion/106641/ker-v-california/" aria-description="Citation for case: Ker v. California">374 U. S. 23</a></span> (1963).</p>
<p>[11]  The Court stressed the limits of its holding: the police officer's belief that his safety or that of others is in danger must be objectively reasonable based on reasonable inferences from known factsso that it can be tested at the appropriate time by "the more detached, neutral scrutiny of a judge," 392 U. S., at 21, 27; and the extent of the intrusion must be carefully tailored to the rationale justifying it.</p>
<p>[12]  <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Terry</a></span></i> specifically declined to address "the constitutional propriety of an investigative 'seizure' upon less than probable cause for purposes of `detention' and/or interrogation." <i><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Id.,</a></span></i> at 19 n. 16. Mr. JUSTICE WHITE, in a concurring opinion, made these observations on the matter of interrogation during an investigative stop:
</p>
<p>"There is nothing in the Constitution which prevents a policeman from addressing questions to anyone on the streets. Absent special circumstances, the person approached may not be detained or frisked but may refuse to cooperate and go on his way. However, given the proper circumstances, such as those in this case, it seems to me the person may be briefly detained against his will while pertinent questions are directed to him. Of course, the person stopped is not obliged to answer, answers may not be compelled, and refusal to answer furnishes no basis for an arrest, although it may alert the officer to the need for continued observation." <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio"><i>Id.,</i> at 34</a></span>.</p>
<p>[13]  "[B]ecause of the importance of the governmental interest at stake, the minimal intrusion of a brief stop, and the absence of practical alternatives for policing the border, we hold that when an officer's observations lead him reasonably to suspect that a particular vehicle may contain aliens who are illegally in the country, he may stop the car briefly and investigate the circumstances that provoke suspicion." 422 U. S., at 881.</p>
<p>[14]  The factors that respondent would consider relevant in its balancing test, and the scope of the rule the test would produce, are not completely clear. The Appellate Division quoted two apparently different tests from the Court of Appeals opinion in <i>People</i> v. <i>Morales,</i> 42 N. Y. 2d 129, <span class="citation" data-id="5531084"><a href="/opinion/5682523/people-v-morales/" aria-description="Citation for case: People v. Morales">366 N. E. 2d 248</a></span> (1977):
</p>
<p>"`[L]aw enforcement officials may detain an individual upon reasonable suspicion for questioning for a reasonable and brief period of time under carefully controlled conditions which are ample to protect the individual's Fifth and Sixth Amendment rights' (<span class="citation" data-id="5531084"><a href="/opinion/5682523/people-v-morales/#135" aria-description="Citation for case: People v. Morales">42 NY2d, at p. 135</a></span>). `"[A] policeman's right to request information while discharging his law enforcement duties will hinge on the manner and intensity of the interference, the gravity of the crime involved and the circumstances attending the encounter'" (<span class="citation" data-id="5531084"><a href="/opinion/5682523/people-v-morales/#137" aria-description="Citation for case: People v. Morales">42 NY2d, at p. 137</a></span>, quoting from <i>People</i> v. <i>De Bour,</i> <span class="citation" data-id="5530768"><a href="/opinion/5682261/people-v-de-bour/#219" aria-description="Citation for case: People v. De Bour">40 NY2d 210, 219</a></span>)." 61 App. Div. 2d, at 302, 402 N. Y. S. 2d, at 492.</p>
<p>Then, in characterizing the case before it, the Appellate Division suggested yet a third "test":</p>
<p>"[T]his case involves a brief detention for interrogation based upon reasonable suspicion, where there was no formal accusation filed against defendant and where great public interest existed in solving a brutal crime which had remained unsolved for a period of almost five months." <span class="citation" data-id="5530768"><a href="/opinion/5682261/people-v-de-bour/#303" aria-description="Citation for case: People v. De Bour"><i>Id.,</i> at 303</a></span>, 402 N. Y. S. 2d, at 492.</p>
<p>[15]  See n. 14, <i>supra.</i></p>
<p>[16]  While the rule proposed by respondent is not entirely clear, the Appellate Division cited with approval a test that would require an officer to weigh before any custodial interrogation "the manner and intensity of the interference, the gravity of the crime involved and the circumstances attending the encounter." See n. 14, <i>supra.</i></p>
<p>[17]  The officers drew their guns, informed Brown that he was under arrest, and handcuffed him. But Brown, unlike petitioner, was not a teenager; and the police had a report that he possessed a pistol and had used it on occasion, 422 U. S., at 594. The police in this case would have resorted to similar measures if petitioner had resisted being taken into custody. App. 117.</p>
<p>[18]  But see <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#494" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 494-497</a></span> (1966) (decided with <i>Miranda</i> v. <i>Arizona</i>).</p>
<p>[19]  See generally, 3 LaFave, <i>supra</i> n. 9, at 630-638; Comment, 25 Emory L. J. 227, 239-244 (1976); Comment, 13 Houston L. Rev. 753, 763-770 (1976).</p>
<p>[20]  The cases are even parallel in that both Brown and petitioner made subsequent statements, see n. 2, <i>supra; </i><i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#595" aria-description="Citation for case: Brown v. Illinois">422 U. S., at 595-596</a></span>, which in each case were "clearly the result and the fruit of the first." <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/#605" aria-description="Citation for case: Brown v. Illinois"><i>Id.,</i> at 605</a></span>, and n. 12.</p>
<p>[21]  Comment, 25 Emory L. J. 227, 238 (1976).</p>
<p>[1]  See, <i>e. g.,</i> MR. JUSTICE REHNQUIST, dissenting, <i>post,</i> at 226.</p>
<p>[2]  I would agree that the officer's subjective state of mind is relevant when he is being sued for damages, but this case involves the question whether the evidence he has obtained is admissible at trial.</p>
<p>[1]  Neither <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969), nor <i>Brown</i> v. <i>Illinois,</i> <span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U. S. 590</a></span> (1975), which the Court treats as points of departure for today's opinion, supports the Court's conclusion that petitioner was "seized" within the meaning of the Fourth Amendment. In <i><span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">Davis</a></span>,</i> the State made no claim that Davis had voluntarily accompanied the police officers to headquarters. <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S., at 726</a></span>. Similarly, in <i>Brown</i> there could be no reasonable disagreement that the defendant had been "seized" for Fourth Amendment purposes. In <i>Brown,</i> two detectives of the Chicago police force broke into Brown's apartment and searched it. When Brown entered the apartment, he was told that he was under arrest, was held at gunpoint, and was searched. He then was handcuffed and escorted to the squad car that eventually took him to the police station. 422 U. S., at 593. No doubt this police activity was the cause of the Court's observation that "[t]he illegality here, moreover, had a quality of purposefulness. . . . The manner in which Brown's arrest was effected gives the appearance of having been calculated to cause surprise, fright, and confusion." <i>Id.,</i> at 605. No such circumstances occurred here.</p>
<p>[2]  This Court granted certiorari in <i>Morales,</i> but, as the Court points out, <i>ante,</i> at 205 n. 3, we ultimately reserved decision on the question of the legality of involuntary investigatory detention on less than probable cause. <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/" aria-description="Citation for case: Morales v. New York">396 U. S. 102</a></span> (1969).</p>

</div>
```

---

## GROUP: content/cases/Dupree v. Younger.md  (`case`, 5 assertions)

### content_page

```
---
title: Dupree v. Younger
type: case
citation: "598 U.S. 729 (2023)"
parallel_cite: ""
neutral_cite: ""
court: scotus
court_level: scotus
circuit: ""
year: 2023
date_decided: ""
docket: 22-210
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
  opinion_url: "https://www.courtlistener.com/opinion/10049685/dupree-v-younger/"
  cluster_id: 10049685
  opinion_id: null
  identity_checked: true
lake:
  record_id: Dupree v. Younger
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[Section 1983 Liability and Qualified Immunity]]"
    role: Recent development
related:
  - "[[Section 1983 Liability and Qualified Immunity]]"
tags:
  - case
  - section-1983
  - appellate-preservation
  - summary-judgment
  - prison-litigation
holding: "A post-trial motion under Rule 50 is not required to preserve for appellate review a purely legal issue resolved at summary judgment; a party who loses such an issue at summary judgment may appeal it without renewing the argument after trial."
---

# Dupree v. Younger

*598 U.S. 729 (2023)* (No. 22-210) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 10049685 → opinion 10516285; quote string-matched to the CL opinion text 2026-07-07. S9 promotes. -->

## Background
Kevin Younger, a Maryland pretrial detainee, was beaten by corrections officers and sued a supervising official, Neil Dupree, under 42 U.S.C. § 1983. Dupree raised a Prison Litigation Reform Act administrative-exhaustion defense, which the District Court rejected as a matter of law at summary judgment. The case proceeded to a jury trial that Younger won; Dupree did not re-raise the exhaustion issue in a post-trial motion. When Dupree appealed the summary-judgment ruling, the Fourth Circuit — bound by precedent holding that any issue rejected at summary judgment is not preserved unless renewed post-trial — dismissed the appeal.

## Issue
Whether a party must file a post-trial motion under Rule 50 to preserve for appellate review a purely legal issue that the district court resolved against it at summary judgment.

## Rule
Under *Ortiz v. Jordan*, a summary-judgment denial resting on the *sufficiency of the evidence* is not appealable after trial, because the trial record supersedes the summary-judgment record — so a sufficiency challenge must be renewed in a post-trial motion. A purely legal ruling is different: trials "wholly supplant pretrial factual rulings, but they leave pretrial legal rulings undisturbed," and nothing at trial gives the district court reason to reconsider a legal question. Accordingly, "a post-trial motion under Rule 50 is not required to preserve for appellate review a purely legal issue resolved at summary judgment." — 598 U.S. at 733–738. ^pin-733

## Application
Because a purely legal question is, by definition, answerable without reference to disputed facts, factual development at trial cannot change the district court's answer, and a renewal requirement would be an empty exercise — for litigants, a copy-and-paste of the summary-judgment motion; for courts, the tedium of denying the same motion twice. The Court declined to resolve whether the exhaustion issue Dupree actually raised was "purely legal," leaving that classification (and any other properly preserved arguments) for the Fourth Circuit [[Reading and Citing Cases#on-remand|on remand]].

## Conclusion
The judgment of the Fourth Circuit was **[[Reading and Citing Cases#vacated|vacated]]** and the case **[[Reading and Citing Cases#on-remand|remanded]]**. Barrett, J., delivered the opinion for a unanimous Court.

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the two-key verification, so it renders under the ⚪ banner until S9 promotion. *Dupree* is a civil-procedure decision that arises in the § 1983 setting; it governs how a defendant official preserves a legal defense (such as PLRA exhaustion) for appeal after losing it at summary judgment and then going to trial.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Recent development*

## Sources
- [*Dupree v. Younger*, 598 U.S. 729 (2023)](https://www.courtlistener.com/opinion/10049685/dupree-v-younger/) — pinpoint: 733–738 (Opinion of the Court, holding; anchor at the opinion's first page); quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "795c2ae658b270a6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "598 U.S. 729 (2023)", "court": "scotus", "neutral_cite": "", "official_citation_present": true, "parallel_cite": "", "title": "Dupree v. Younger", "year": "2023"}}
{"assertion_id": "54078364c34ea847", "dimension": "support", "kind": "home_role", "locator": {"home": "Section 1983 Liability and Qualified Immunity"}, "payload": {"home": "Section 1983 Liability and Qualified Immunity", "role": "Recent development", "title": "Dupree v. Younger"}}
{"assertion_id": "964e27486f9e4638", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A post-trial motion under Rule 50 is not required to preserve for appellate review a purely legal issue resolved at summary judgment; a party who loses such an issue at summary judgment may appeal it without renewing the argument after trial.", "title": "Dupree v. Younger"}}
{"assertion_id": "65088acfdbf80c8a", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Dupree v. Younger"}}
{"assertion_id": "6f8d9d4b69d1a75b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Dupree v. Younger", "varies_by_point": "false"}}
```

### lake record — Dupree v. Younger

```json
{
  "schema_version": "s2.v1",
  "record_id": "Dupree v. Younger",
  "status": "under_review",
  "identity": {
    "case_name": "Dupree v. Younger",
    "case_name_short": "Dupree",
    "case_name_full": "",
    "input_case_name": "Dupree v. Younger",
    "court": "scotus",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": null,
    "year": 2023,
    "docket": "22-210",
    "cluster_id": 10049685,
    "lead_opinion_id": 10516285,
    "sibling_ids": [],
    "absolute_url": "/opinion/10049685/dupree-v-younger/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "598 U.S. 729",
      "volume": "598",
      "reporter": "U.S.",
      "page": "729",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [],
    "vendor_neutral": [],
    "all": [
      {
        "cite": "598 U.S. 729",
        "volume": "598",
        "reporter": "U.S.",
        "page": "729",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "598 U.S. 729",
    "official_selection": {
      "court_class": "scotus",
      "selected": "598 U.S. 729",
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
    "date_created": "2026-07-06T12:11:27Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T12:11:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T12:11:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T12:11:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "dupree-v-younger--10049685",
      "to_record_id": "Dupree v. Younger",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Dupree v. Younger

```
                   PRELIMINARY PRINT

             Volume 598 U. S. Part 2
                             Pages 729–738




       OFFICIAL REPORTS
                                    OF


   THE SUPREME COURT
                                May 25, 2023


Page Proof Pending Publication


                   REBECCA A. WOMELDORF
                           reporter of decisions




    NOTICE: This preliminary print is subject to formal revision before
  the bound volume is published. Users are requested to notify the Reporter
  of Decisions, Supreme Court of the United States, Washington, D.C. 20543,
  pio@supremecourt.gov, of any typographical or other formal errors.
                         OCTOBER TERM, 2022                              729

                                  Syllabus


                      DUPREE v. YOUNGER

certiorari to the united states court of appeals for
                 the fourth circuit
       No. 22–210. Argued April 24, 2023—Decided May 25, 2023
Respondent Kevin Younger claims that during his pretrial detention in a
 Maryland state prison, petitioner Neil Dupree, then a correctional off-
 cer lieutenant, ordered three prison guards to attack him. Younger
 sued Dupree for damages under 42 U. S. C. § 1983, alleging excessive
 use of force. Prior to trial, Dupree moved for summary judgment
 under Federal Rule of Civil Procedure 56(a), arguing that Younger had
 failed to exhaust administrative remedies as required by law. Rule 56
 requires a district court to enter judgment on a claim or defense if there
 is “no genuine dispute as to any material fact and the movant is entitled
 to judgment as a matter of law.” The District Court denied the motion,
 fnding no dispute that the Maryland prison system had internally inves-
 tigated Younger's assault, and concluding that this inquiry satisfed
 Younger's exhaustion obligation. At trial, Dupree did not present evi-
Page Proof Pending Publication
 dence relating to his exhaustion defense. The jury found Dupree and
 four codefendants liable and awarded Younger $700,000 in damages.
 Dupree did not fle a post-trial motion under Rule 50(b), which allows a
 disappointed party to fle a renewed motion for judgment as a matter
 of law. He appealed a single issue to the Fourth Circuit: the District
 Court's rejection of his exhaustion defense. The Fourth Circuit—
 bound by its precedent which holds that any claim or defense rejected
 at summary judgment is not preserved for appellate review unless it
 was renewed in a post-trial motion—dismissed the appeal.
Held: A post-trial motion under Rule 50 is not required to preserve for
 appellate review a purely legal issue resolved at summary judgment.
 In Ortiz v. Jordan, the Court held that an order denying summary judg-
 ment on suffciency-of-the-evidence grounds is not appealable after trial.
 562 U. S. 180, 184. Because the factual record developed at trial “super-
 sedes the record existing at the time of the summary-judgment motion,”
 ibid., it follows that a party must raise a suffciency claim in a post-trial
 motion in order to preserve it for appeal, id., at 191–192. That motion
 allows the district court to take frst crack at the question that the
 appellate court will ultimately face: Was there suffcient evidence in the
 trial record to support the jury's verdict?
    The same is not true for pure questions of law resolved in an order
 denying summary judgment. These conclusions are not “supersede[d]”
730                      DUPREE v. YOUNGER

                                  Syllabus

  by later developments in the litigation, id., at 184, and so such rulings
  merge into the fnal judgment, at which point they are reviewable on
  appeal, Quackenbush v. Allstate Ins. Co., 517 U. S. 706, 712. The re-
  viewing court does not beneft from having a district court reexamine a
  purely legal pretrial ruling after trial, because nothing at trial will have
  given the district court any reason to question its prior analysis.
     Younger's counterarguments are unpersuasive. Ortiz does not hold,
  as Younger contends, that any order denying summary judgment—
  whether decided on legal or factual grounds—is unreviewable under 28
  U. S. C. § 1291. While an interlocutory order denying summary judg-
  ment is typically not immediately appealable, § 1291 does not insulate
  interlocutory orders from appellate scrutiny, but rather delays their re-
  view until fnal judgment. And while Younger insists there should be
  no two-track system of summary judgment, in which factual and legal
  claims follow different routes, nothing in Rule 56 supports his argument
  for uniformity. On the contrary, ftting the preservation rule to the
  rationale (factual or legal) underlying the summary-judgment order is
  consistent with the text of Rule 56. It also makes sense: Factual devel-
  opment at trial will not change the district court's pretrial answer to a
  purely legal question, so a post-trial motion requirement would amount
  to an empty exercise. Finally, while Younger predicts that a separate
Page Proof Pending Publication
  preservation rule for legal issues will prove unworkable because the
  line between factual and legal questions can be “vexing” for courts and
  litigants, Pullman-Standard v. Swint, 456 U. S. 273, 288, experience
  demonstrates that Younger overstates the need for a bright-line rule.
  “Courts of appeals have long found it possible to separate factual from
  legal matters.” Teva Pharmaceuticals USA, Inc. v. Sandoz, Inc., 574
  U. S. 318, 328. Here, the Court does not decide whether the issue
  Dupree raised on appeal is purely legal, and remands for the Fourth
  Circuit to evaluate that question in the frst instance. Pp. 733–738.
Vacated and remanded.
  Barrett, J., delivered the opinion for a unanimous Court.

  Andrew T. Tutt argued the cause for petitioner. With him
on the briefs were R. Stanton Jones, Sean A. Mirski, Dana
Or, and Aaron Bowling.
  Amy Mason Saharia argued the cause for respondent.
With her on the brief were Lisa S. Blatt, A. Joshua Podoll,
and Allen E. Honick.*
  *Briefs of amici curiae urging reversal were fled for the DRI Center
for Law and Public Policy by Matthew T. Nelson and Charles R. Quigg;
and for Law Professors by Steffen N. Johnson and Conor Tucker.
                       Cite as: 598 U. S. 729 (2023)                    731

                           Opinion of the Court

  Justice Barrett delivered the opinion of the Court.
   In Ortiz v. Jordan, we held that an order denying sum-
mary judgment on suffciency-of-the-evidence grounds is not
reviewable on appeal after a trial. 562 U. S. 180 (2011).
Thus, a party who wants to preserve a suffciency challenge
for review on appeal must raise it anew in a post-trial mo-
tion. The question presented in this case is whether this
preservation requirement extends to a purely legal issue re-
solved at summary judgment. The answer is no.

                                     I
                                    A
  The Federal Rules of Civil Procedure empower district
courts to direct the entry of judgment before, during, or
after trial. Before trial, the defendant can fle a motion to
dismiss the complaint based on certain defenses, such as lack
of jurisdiction or failure to state a claim upon which relief
Page Proof Pending Publication
can be granted. Fed. Rule Civ. Proc. 12(b). If the district
court denies that motion (or any other Rule 12 motion), the
case advances to discovery for the parties to marshal evi-
dence supporting their claims and defenses. During or after
that process, either party can move for summary judgment
under Rule 56, which requires a district court to enter judg-
ment on a claim or defense if there is “no genuine dispute as
to any material fact and the movant is entitled to judgment
as a matter of law.” Fed. Rule Civ. Proc. 56(a).
  If the plaintiff's claims survive summary judgment, the
case proceeds to trial. After the presentation of evidence,
but before the case is submitted to the jury, Rule 50(a)
authorizes either party to move for judgment as a matter
of law.1 This standard largely “mirrors” the summary-
judgment standard, the difference being that district courts
evaluate Rule 50(a) motions in light of the trial record rather
  1
   If the parties waive their rights to a jury or seek relief that does not
entitle them to a jury, the district court will hold a bench trial, which is
governed by Rule 52.
732                 DUPREE v. YOUNGER

                      Opinion of the Court

than the discovery record. Anderson v. Liberty Lobby, Inc.,
477 U. S. 242, 250–251 (1986).
  If the district court does not grant the motion, then the
jury will render a verdict. After the verdict, Rule 50(b)
permits a disappointed party to fle a renewed motion for
judgment as a matter of law (which may also include a re-
quest for a new trial under Rule 59). The next step for a
party who fails to obtain post-trial relief is an appeal.

                               B
   While Kevin Younger was being held as a pretrial detainee
in a Maryland state prison, three corrections offcers as-
saulted him. Younger believed that Neil Dupree, a former
lieutenant in the prison, had ordered the attack. He sued
Dupree and other prison offcials for damages under 42
U. S. C. § 1983, alleging that they had used excessive force in
violation of his Fourteenth Amendment due process rights.
Page Proof Pending Publication
   Dupree moved for summary judg ment, arguing that
Younger had failed to exhaust his administrative remedies
as required by the Prison Litigation Reform Act, 42 U. S. C.
§ 1997e(a). The District Court denied the motion. It noted
factual disagreements between the parties about whether
Younger had adhered to Maryland's Administrative Remedy
Procedure but concluded that it “need not resolve [those] dis-
putes.” Younger v. Green, Civ. No. 16–3269 (D Md., Dec. 19,
2019), App. to Pet. for Cert. 42a. Instead, the court ob-
served that there was “no dispute” that the Maryland prison
system had internally investigated Younger's assault. Ibid.
And it held that this inquiry satisfed Younger's exhaustion
obligation.
   The case then proceeded to a jury trial. Dupree did not
present any evidence relating to his exhaustion defense, nor
did he invoke exhaustion in his Rule 50(a) motion, which the
District Court denied. The jury found Dupree and four of
his codefendants liable and awarded Younger $700,000 in dam-
ages. Dupree did not fle a post-trial motion under Rule 50(b).
                       Cite as: 598 U. S. 729 (2023)                    733

                           Opinion of the Court

   Dupree appealed to the Fourth Circuit. He sought review
of a single issue: the District Court's rejection of his exhaus-
tion defense at summary judgment. Unfortunately for
Dupree, the appeal was over before it began. Fourth Cir-
cuit precedent maintains that a claim or defense rejected at
summary judgment is not preserved for appellate review un-
less it was renewed in a post-trial motion—even when the
issue is a purely legal one. Varghese v. Honeywell Int'l,
Inc., 424 F. 3d 411, 422–423 (2005). Bound by this prece-
dent, the panel dismissed the appeal.
   The Fourth Circuit's decision further cemented a confict
among the Courts of Appeals over whether a purely legal
challenge resolved at summary judgment must be renewed
in a post-trial motion in order to preserve that challenge
for appellate review. We granted certiorari to resolve the
disagreement.2 598 U. S. ––– (2023).
                                    II
Page Proof Pending
              A    Publication
   The jurisdiction of the Courts of Appeals under 28 U. S. C.
§ 1291 is limited to “appeals from . . . fnal decisions of the
  2
    Compare Rothstein v. Carriere, 373 F. 3d 275, 284 (CA2 2004) (post-
trial motion not required to preserve claims of purely legal error); Frank
C. Pollara Group, LLC v. Ocean View Inv. Holding, LLC, 784 F. 3d 177,
187 (CA3 2015) (same); In re AmTrust Financial Corp., 694 F. 3d 741,
750–751 (CA6 2012) (same); Chemetall GMBH v. ZR Energy, Inc., 320
F. 3d 714, 719–720 (CA7 2003) (same); Banuelos v. Construction Laborers'
Trust Funds for Southern Cal., 382 F. 3d 897, 902–903 (CA9 2004) (same);
Wolfgang v. Mid-America Motorsports, Inc., 111 F. 3d 1515, 1521 (CA10
1997) (same); Feld v. Feld, 688 F. 3d 779, 783 (CADC 2012) (same), with Ji
v. Bose Corp., 626 F. 3d 116, 127–128 (CA1 2010) (post-trial motion required
to preserve claims of pure legal error); Varghese v. Honeywell Int'l, Inc.,
424 F. 3d 411, 422–423 (CA4 2005) (same); Feld Motor Sports, Inc. v. Trax-
xas, L. P., 861 F. 3d 591, 596 (CA5 2017) (same); American Builders Ins.
Co. v. Southern-Owners Ins. Co., 56 F. 4th 938, 950 (CA11 2023) (same);
see also New York Marine & Gen. Ins. Co. v. Continental Cement Co., 761
F. 3d 830, 838–839 (CA8 2014) (post-trial motion not required to preserve
“preliminary” legal issues).
734                    DUPREE v. YOUNGER

                         Opinion of the Court

district courts.” Interlocutory orders—those that do not
dispose of the whole case, like denials of summary judg-
ment—are typically not immediately appealable under
§ 1291.3 Instead, the “general rule is that `a party is entitled
to a single appeal, to be deferred until fnal judgment has
been entered, in which claims of district court error at any
stage of the litigation may be ventilated.' ” Quackenbush v.
Allstate Ins. Co., 517 U. S. 706, 712 (1996); see also 15A
C. Wright, A. Miller, & E. Cooper, Federal Practice and Pro-
cedure § 3905.1 (3d ed. 2022) (generally, “an appeal from fnal
judgment opens the record and permits review of all rulings
that led up to the judgment”).
   Some interlocutory district-court rulings, however, are un-
reviewable after fnal judgment because they are overcome
by later developments in the litigation. As Ortiz explains,
one such ruling is the denial of summary judgment on
suffciency-of-the-evidence grounds. 562 U. S., at 184. Fac-
tual challenges depend on, well, the facts, which the parties
Page Proof Pending Publication
develop and clarify as the case progresses from summary
judgment to a jury verdict. Thus, “[o]nce the case proceeds
to trial, the full record developed in court supersedes the
record existing at the time of the summary-judgment mo-
tion.” Ibid. So after trial, a district court's assessment of
the facts based on the summary-judgment record becomes
“ancient history and [is] not subject to appeal.” Empress
Casino Joliet Corp. v. Balmoral Racing Club, Inc., 831 F. 3d
815, 823–824 (CA7 2016). Fact-dependent rulings must be
appraised in light of the complete trial record.
   It follows, Ortiz holds, that a party must raise a
suffciency-of-the-evidence claim in a post-trial motion to
preserve it for review on appeal. 562 U. S., at 191–192.
Appellate review, by its nature, requires a lower court deci-
sion to review. Freytag v. Commissioner, 501 U. S. 868, 895
  3
   The collateral-order doctrine recognizes exceptions to this rule. For
instance, an interlocutory order denying qualifed immunity is sometimes
immediately appealable. Mitchell v. Forsyth, 472 U. S. 511, 530 (1985).
                   Cite as: 598 U. S. 729 (2023)            735

                      Opinion of the Court

(1991) (Scalia, J., concurring in part and concurring in judg-
ment) (the “very word `review' presupposes that a litigant's
arguments have been raised and considered in the tribunal
of frst instance”). This is especially important for factual
challenges based on the trial record, which “cal[l] for the
judgment in the frst instance of the judge who saw and
heard the witnesses and has the feel of the case which no
appellate printed transcript can impart.” Cone v. West Vir-
ginia Pulp & Paper Co., 330 U. S. 212, 216 (1947). The fling
of a post-trial motion under Rule 50 allows the district court
to take frst crack at the question that the appellate court
will ultimately face: Was there suffcient evidence in the trial
record to support the jury's verdict? Absent such a motion,
“an appellate court is `powerless' to review the suffciency of
the evidence after trial.” Ortiz, 562 U. S., at 189 (quoting
Unitherm Food Systems, Inc. v. Swift-Eckrich, Inc., 546
U. S. 394, 405 (2006)).
                                B
Page     Proof Pending Publication
 Younger urges us to extend Ortiz's holding to cover pure
questions of law resolved in an order denying summary judg-
ment. We decline the invitation.
   While factual issues addressed in summary-judgment de-
nials are unreviewable on appeal, the same is not true of
purely legal issues—that is, issues that can be resolved with-
out reference to any disputed facts. Trials wholly supplant
pretrial factual rulings, but they leave pretrial legal rulings
undisturbed. The point of a trial, after all, is not to hash
out the law. Because a district court's purely legal conclu-
sions at summary judgment are not “supersede[d]” by later
developments in the litigation, Ortiz, 562 U. S., at 184, these
rulings follow the “general rule” and merge into the fnal
judgment, at which point they are reviewable on appeal,
Quackenbush, 517 U. S., at 712.
   That difference explains why a summary-judgment motion
is suffcient to preserve legal but not factual claims. As
Ortiz explains, an appellate court's review of factual chal-
736                  DUPREE v. YOUNGER

                      Opinion of the Court

lenges after a trial is rooted in the complete trial record,
which means that a district court's factual rulings based on
the obsolete summary-judgment record are useless. A dis-
trict court's resolution of a pure question of law, by contrast,
is unaffected by future developments in the case. From the
reviewing court's perspective, there is no beneft to having a
district court reexamine a purely legal issue after trial, be-
cause nothing at trial will have given the district court any
reason to question its prior analysis. We therefore hold that
a post-trial motion under Rule 50 is not required to preserve
for appellate review a purely legal issue resolved at sum-
mary judgment.
                                C
  Younger's counterarguments do not persuade us other-
wise. First, he argues that under Ortiz, an order denying
summary judgment is not a “fnal decision” under § 1291 and
cannot be appealed, regardless of whether the motion was
Page Proof Pending Publication
decided on legal or factual grounds. We agree that a denial
of summary judgment is “simply a step along the route to
fnal judgment,” and so is typically not immediately review-
able on appeal. Ortiz, 562 U. S., at 184. But § 1291 does
not insulate interlocutory orders from appellate scrutiny; it
simply delays review until fnal judgment. Richardson-
Merrell Inc. v. Koller, 472 U. S. 424, 430 (1985) (noting that
some errors in interlocutory orders “go uncorrected until the
appeal of a fnal judgment”). Indeed, the Ortiz Court ex-
pressly declined to address whether summary-judgment de-
nials on purely legal issues are reviewable. 562 U. S., at 190.
That caveat would have made little sense had the Court au-
thoritatively decided that all summary-judgment denials are
meaningless passthroughs that appellate courts should
ignore.
  Next, Younger complains that Dupree's rule creates a two-
track system of summary judgment, in which factual and
legal claims follow different routes. Summary judgment is
summary judgment, Younger insists, so the claims should all
                   Cite as: 598 U. S. 729 (2023)             737

                      Opinion of the Court

travel the same line. But nothing in Rule 56 demands such
uniformity. On the contrary, the Rule provides that sum-
mary judgment is appropriate when “the movant shows that
there is no genuine dispute as to any material fact and the
movant is entitled to judgment as a matter of law.” Fed.
Rule Civ. Proc. 56(a) (emphasis added). Rule 56 thus con-
templates that the court will sometimes deny the motion be-
cause the facts are genuinely in dispute and other times
because the law does not support the movant's position.
Fitting the preservation rule to the court's rationale (factual
or legal) is therefore consistent with the text.
   It also makes sense. Because a purely legal question is,
by defnition, one whose answer is independent of disputed
facts, factual development at trial will not change the district
court's answer. (Granted, the district court might back-
track, but if the question is purely legal, that is because of
law books, not trial exhibits.) So what would a repeat-
Page Proof Pending Publication
motion requirement for legal questions typically amount to?
For litigants, a copy and paste of summary-judgment mo-
tions into post-trial format. For district courts, the tedium
of saying no twice. There is no reason to force litigants and
district courts to undertake that empty exercise.
   Rule 56 aside, Younger insists that Rule 50 supports him.
Under this Rule, a district court can grant judgment as a
matter of law if it fnds that “a reasonable jury would not
have a legally suffcient evidentiary basis to fnd for the
party on that issue.” Fed. Rules Civ. Proc. 50(a), (b) (em-
phasis added). Therefore, Younger says, a Rule 50 motion
is an appropriate vehicle for raising purely legal issues once
a case proceeds to trial. Maybe so, but this argument is
beside the point: Even if a party can raise legal issues in a
Rule 50 motion, nothing in the Rule requires her to do so.
   Finally, Younger predicts that a separate preservation
rule for legal issues will prove unworkable because the line
between factual and legal questions can be “vexing” for
courts and litigants. Pullman-Standard v. Swint, 456 U. S.
738                 DUPREE v. YOUNGER

                     Opinion of the Court

273, 288 (1982). That's a fair concern, and it would not be
surprising if “prudent counsel . . . make sure to renew their
arguments in a Rule 50 motion” out of an abundance of cau-
tion. Feld v. Feld, 688 F. 3d 779, 783 (CADC 2012). But
Younger overstates the need for a bright-line rule in this
area. “Courts of appeals have long found it possible to sepa-
rate factual from legal matters.” Teva Pharmaceuticals
USA, Inc. v. Sandoz, Inc., 574 U. S. 318, 328 (2015). Though
there will be edge cases, the experience of the majority of
circuits demonstrates that the Courts of Appeals are up to
the task. See n. 2, supra. And for all the virtues of bright-
line rules, Younger's would come at a steep cost: the loss of
appellate review for unwary litigants who think it futile to
relitigate an already-rejected legal argument.
                             III
   The Fourth Circuit was wrong to hold that purely legal
issues resolved at summary judgment must be renewed in
Page Proof Pending Publication
a post-trial motion. We need not decide whether the issue
Dupree raised on appeal is purely legal—the Court of Ap-
peals may evaluate that and any other properly preserved
arguments in the frst instance. We therefore vacate the
judgment of the Court of Appeals and remand the case for
further proceedings consistent with this opinion.

                                            It is so ordered.
                            Reporter’s Note

  The attached opinion has been revised to refect the usual publication
and citation style of the United States Reports. The revised pagination
makes available the offcial United States Reports citation in advance of
publication. The syllabus has been prepared by the Reporter of Decisions
for the convenience of the reader and constitutes no part of the opinion of
the Court. A list of counsel who argued or fled briefs in this case, and
who were members of the bar of this Court at the time this case was
argued, has been inserted following the syllabus. Other revisions may
include adjustments to formatting, captions, citation form, and any errant
Page Proof Pending Publication
punctuation. The following additional edits were made:

p. 731, line 3, “appealable” is changed to “reviewable on appeal”
p. 731, line 4, “review on” is inserted after “for”
p. 733, line 1, the frst sentence of the paragraph is deleted and replaced
   with: “Dupree appealed to the Fourth Circuit. He sought review of a
   single issue: the District Court's rejection of his exhaustion defense at
   summary judgment.”
p. 734, in the last sentence of the full paragraph, “appeals” is changed
   to “rulings”
p. 734, line 31, “review on” is inserted before “appeal.”
p. 736, lines 19–20, “appealable” is changed to “reviewable on appeal”

```

---

## GROUP: content/cases/Edwards v. Arizona.md  (`case`, 5 assertions)

### content_page

```
---
title: "Edwards v. Arizona"
type: case
citation: "451 U.S. 477 (1981)"
parallel_cite: "101 S. Ct. 1880; 68 L. Ed. 2d 378"
neutral_cite: 1981 U.S. LEXIS 96
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1981
date_decided: 1981-06-22
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1981-05-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Edwards v. Arizona
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110475/edwards-v-arizona/"
  cluster_id: 110475
  opinion_id: 9428324
  identity_checked: true
homes:
  - page: "[[Miranda Waiver and Invocation]]"
    role: "Key — Anchor"
related: ["[[Arizona v. Roberson]]", "[[Miranda v. Arizona]]", "[[Davis v. United States]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "invocation", "right-to-counsel", "reinitiation", "bright-line-rule"]
holding: "Once an accused invokes his Fifth Amendment right to counsel, police may not reinitiate interrogation until counsel has been made…"
lake:
  record_id: Edwards v. Arizona
  status: verified
  projected_at: 2026-07-06
---

# Edwards v. Arizona

*451 U.S. 477 (1981)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After being given *[[Miranda v. Arizona|Miranda]]* warnings, Edwards invoked his right to counsel and questioning stopped. The next morning, before counsel was made available, different officers came to the jail, re-advised him, and obtained an incriminating statement. The Arizona courts held he had waived his right to counsel by talking; the Supreme Court granted review.

## Issue
Whether, once a suspect has invoked the right to counsel, a valid waiver can be shown merely because he later responds to further police-initiated interrogation.

## Rule
No; once counsel is invoked, police may not reinitiate interrogation. "[W]hen an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights." — 451 U.S. 477, 484. ^pin-484

"[A]n accused, such as Edwards, having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police." — *Id.* at 484–85. ^pin-484a

## Application
Edwards invoked counsel, yet the police — not Edwards — reopened the interrogation the next morning before any lawyer was provided. Because he had not himself initiated the renewed contact, the statement obtained through that police-initiated interrogation could not rest on a valid waiver and had to be suppressed on these facts.

## Conclusion
The police-initiated interrogation after Edwards invoked counsel violated his rights; the judgment was reversed. *Edwards* establishes the bright-line bar on reinitiating interrogation after a suspect invokes counsel.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Edwards* anchors the invocation-of-counsel rule; [[Arizona v. Roberson]] held the bar is not offense-specific, and [[Davis v. United States]] held the initial invocation must be unambiguous.

## Appears on
- [[Miranda Waiver and Invocation]] — *Key — Anchor*

## Sources
- *Edwards v. Arizona*, 451 U.S. 477 (1981) — https://www.courtlistener.com/opinion/110475/edwards-v-arizona/ — pinpoints: 484, 485.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "9b60689dc6571bfe", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "451 U.S. 477 (1981)", "court": "U.S. Supreme Court", "neutral_cite": "1981 U.S. LEXIS 96", "official_citation_present": true, "parallel_cite": "101 S. Ct. 1880; 68 L. Ed. 2d 378", "title": "Edwards v. Arizona", "year": "1981"}}
{"assertion_id": "7209a61262e02078", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Once an accused invokes his Fifth Amendment right to counsel, police may not reinitiate interrogation until counsel has been made…", "title": "Edwards v. Arizona"}}
{"assertion_id": "cd05772a6038b4e0", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda Waiver and Invocation"}, "payload": {"home": "Miranda Waiver and Invocation", "role": "Key — Anchor", "title": "Edwards v. Arizona"}}
{"assertion_id": "643409cecc26dbbe", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1981-05-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Edwards v. Arizona", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "Edwards v. Arizona", "varies_by_point": "false"}}
{"assertion_id": "e07b528a5cac7b5b", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Edwards v. Arizona"}}
```

### lake record — Edwards v. Arizona

```json
{
  "schema_version": "s2.v1",
  "record_id": "Edwards v. Arizona",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Edwards v. Arizona",
    "case_name_short": "Edwards",
    "case_name_full": "Edwards v. Arizona",
    "input_case_name": "Edwards v. Arizona",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1981-06-22",
    "year": 1981,
    "docket": null,
    "cluster_id": 110475,
    "lead_opinion_id": 9428324,
    "sibling_ids": [
      110475,
      9428324,
      9428325,
      9428326
    ],
    "absolute_url": "/opinion/110475/edwards-v-arizona/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9033394,
        "score": 20,
        "case_name": "Edwards v. Arizona"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "451 U.S. 477",
      "volume": "451",
      "reporter": "U.S.",
      "page": "477",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "101 S. Ct. 1880",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "1880",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 2d 378",
        "volume": "68",
        "reporter": "L. Ed. 2d",
        "page": "378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1981 U.S. LEXIS 96",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "96",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "451 U.S. 477",
        "volume": "451",
        "reporter": "U.S.",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "101 S. Ct. 1880",
        "volume": "101",
        "reporter": "S. Ct.",
        "page": "1880",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 L. Ed. 2d 378",
        "volume": "68",
        "reporter": "L. Ed. 2d",
        "page": "378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1981 U.S. LEXIS 96",
        "volume": "1981",
        "reporter": "U.S. LEXIS",
        "page": "96",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "451 U.S. 477",
    "official_selection": {
      "court_class": "scotus",
      "selected": "451 U.S. 477",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-484",
      "page": null,
      "quote": "--- # Edwards v. Arizona *451 U.S. 477 (1981)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background After being given *Miranda* warnings, Edwards invoked his right to counsel and questioning stopped. The next morning, before counsel was made available, different officers came to the jail, re-advised him, and obtained an incriminating statement. The Arizona courts held he had waived his right to counsel by talking; the Supreme Court granted review. ## Issue Whether, once a suspect has invoked the right to counsel, a valid waiver can be shown merely because he later responds to further police-initiated interrogation. ## Rule No; once counsel is invoked, police may not reinitiate interrogation.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-484a",
      "page": null,
      "quote": "[A]n accused, such as Edwards, having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made available to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1981-05-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Edwards v. Arizona",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Roberson",
          "cluster_id": 9481866,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane1_negative"
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
        "journal_ref": "Edwards v. Arizona:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 9352546,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 9329344,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Harvin",
          "cluster_id": 8465498,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Gonzalez",
          "cluster_id": 4892536,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Teague v. Lane",
          "cluster_id": 112206,
          "cite": [
            "103 L. Ed. 2d 334",
            "109 S. Ct. 1060",
            "489 U.S. 288",
            "1989 U.S. LEXIS 1043"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffith v. Kentucky",
          "cluster_id": 111785,
          "cite": [
            "93 L. Ed. 2d 649",
            "107 S. Ct. 708",
            "479 U.S. 314",
            "1987 U.S. LEXIS 283",
            "55 U.S.L.W. 4089"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Oregon v. Bradshaw",
          "cluster_id": 110987,
          "cite": [
            "77 L. Ed. 2d 405",
            "103 S. Ct. 2830",
            "462 U.S. 1039",
            "1983 U.S. LEXIS 82",
            "51 U.S.L.W. 4940"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Smith v. Illinois",
          "cluster_id": 111288,
          "cite": [
            "83 L. Ed. 2d 488",
            "105 S. Ct. 490",
            "469 U.S. 91",
            "1984 U.S. LEXIS 167",
            "53 U.S.L.W. 3430"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Saffle v. Parks",
          "cluster_id": 112390,
          "cite": [
            "108 L. Ed. 2d 415",
            "110 S. Ct. 1257",
            "494 U.S. 484",
            "1990 U.S. LEXIS 1178",
            "58 U.S.L.W. 4322"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Patterson v. Illinois",
          "cluster_id": 112127,
          "cite": [
            "101 L. Ed. 2d 261",
            "108 S. Ct. 2389",
            "487 U.S. 285",
            "1988 U.S. LEXIS 2876",
            "56 U.S.L.W. 4733"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
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
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Perkins",
          "cluster_id": 112452,
          "cite": [
            "110 L. Ed. 2d 243",
            "110 S. Ct. 2394",
            "496 U.S. 292",
            "1990 U.S. LEXIS 2885"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Coffman",
          "cluster_id": 2623595,
          "cite": [
            "96 P.3d 30",
            "17 Cal. Rptr. 3d 710",
            "34 Cal. 4th 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnick v. Mississippi",
          "cluster_id": 112513,
          "cite": [
            "112 L. Ed. 2d 489",
            "111 S. Ct. 486",
            "498 U.S. 146",
            "1990 U.S. LEXIS 6118"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leif Taylor v. Thomas M. Maddox, Interim Director George Galaza Cal Terhune",
          "cluster_id": 786028,
          "cite": [
            "366 F.3d 992",
            "2004 U.S. App. LEXIS 9068",
            "2004 WL 1043343"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Frye",
          "cluster_id": 5607916,
          "cite": [
            "18 Cal. 4th 894",
            "98 Cal. Daily Op. Serv. 5949",
            "959 P.2d 183",
            "98 Daily Journal DAR 8259",
            "77 Cal. Rptr. 2d 25",
            "1998 Cal. LEXIS 4688"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Edwards v. Arizona:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110475 OR 9428324 OR 9428325 OR 9428326) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTg1MDA4MDAwMDAwJnM9NDczODU5NyZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110475+OR+9428324+OR+9428325+OR+9428326%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110475 OR 9428324 OR 9428325 OR 9428326)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01ODQmcz0xMTExMTImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28110475+OR+9428324+OR+9428325+OR+9428326%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110475 OR 9428324 OR 9428325 OR 9428326)",
        "reviewed": 111,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 2,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 111,
        "triage_read": 2,
        "triage_snippet_classified": 109
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110475 OR 9428324 OR 9428325 OR 9428326)",
    "indexed_citing_opinions": 4273,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110475,
        "count": 3858,
        "count_source": "search"
      },
      {
        "opinion_id": 9428324,
        "count": 496,
        "count_source": "search"
      },
      {
        "opinion_id": 9428325,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9428326,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 6936,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/edwards-v-arizona.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjk1Njk4MTUmcz0xMDY5MDQ2NyZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28110475+OR+9428324+OR+9428325+OR+9428326%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110475,
        "cited_id": 103050,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 106822,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 109309,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 109336,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 109757,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 110065,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 110117,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 284316,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 343144,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 343316,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 352531,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 360916,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 365779,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 368063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 376877,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 377005,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 1166290,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 1186156,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 1372441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 1435218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 2118946,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110475,
        "cited_id": 2510431,
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
    "date_created": "2026-07-05T03:04:34Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T03:04:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T03:04:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T03:11:05Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T03:04:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Edwards v. Arizona

```
<opinion type="majority">
<author id="b544-11">Justice White</author>
<p id="AIEz">delivered the opinion of the Court.</p>
<p id="b544-12">We granted certiorari in this case, <span class="citation multiple-matches"><a href="/c/U.%20S./446/950/">446 U. S. 950</a></span> (1980), limited to Question 1 presented in the petition, which in relevant part was “whether the Fifth, Sixth, and Fourteenth Amendments require suppression of a post-arrest confession, which was obtained after Edwards had invoked his right to consult counsel before further interrogation . . .</p>
<p id="b544-13">I</p>
<p id="b544-14">On January 19, 1976, a sworn complaint was filed against Edwards in Arizona state court charging him with robbery, burglary, and first-degree murder.<footnotemark>1</footnotemark> An arrest warrant was issued pursuant to the complaint, and Edwards was arrested at his home later that same day. At the police station, he was informed of his rights as required by <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Petitioner stated that he understood his rights, and was willing to submit to questioning. After <page-number citation-index="1" label="479">*479</page-number>being told that another suspect already in custody had implicated him in the crime, Edwards denied involvement and gave a taped statement presenting an alibi defense. He then sought to “make a deal.” The interrogating officer told him that he wanted a statement, but that he did not have the authority to negotiate a deal. The officer provided Edwards with the telephone number of a county attorney. Petitioner made the call, but hung up after a few moments. Edwards then said: “I want an attorney before making a deal.” At that point, questioning ceased and Edwards was taken to county jail.</p>
<p id="b545-5">At 9:15 the next morning, two detectives, colleagues of the officer who had interrogated Edwards the previous night, came to the jail and asked to see Edwards. When the detention officer informed Edwards that the detectives wished to speak with him, he replied that he did not want to talk to anyone. The guard told him that “he had” to talk and then took him to meet with the detectives. The officers identified themselves, stated they wanted to talk to him, and informed him of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. Edwards was willing to talk, but he first wanted to hear the taped statement of the alleged accomplice who had implicated him.<footnotemark>2</footnotemark> After listening to the tape for several minutes, petitioner said that he would make a statement so long as it was not tape-recorded. The detectives informed him that the recording was irrelevant since they could testify in court concerning whatever he said. Edwards replied: “I’ll tell you anything you want to know, but I don’t want it on tape.” He thereupon implicated himself in the crime.</p>
<p id="b545-6">Prior to trial, Edwards moved to suppress his confession on the ground that his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights had been violated when the officers returned to question him after he had invoked his right to counsel. The trial court initially granted <page-number citation-index="1" label="480">*480</page-number>the motion to suppress,<footnotemark>3</footnotemark> but reversed its ruling when presented with a supposedly controlling decision of a higher Arizona court.<footnotemark>4</footnotemark> The court stated without explanation that it found Edwards’ statement to be voluntary. Edwards was tried twice and convicted.<footnotemark>5</footnotemark> Evidence concerning his confession was admitted at both trials.</p>
<p id="b546-5">On appeal, the Arizona Supreme Court held that Edwards had invoked both his right to remain silent and his right to counsel during the interrogation conducted on the night of January 19.<footnotemark>6</footnotemark> <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/" aria-description="Citation for case: State v. Edwards">122 Ariz. 206</a></span>, <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/" aria-description="Citation for case: State v. Edwards">594 P. 2d 72</a></span>. The court then went on to determine, however, that Edwards had waived both rights during the January 20 meeting when he voluntarily gave his statement to the detectives after again being informed that he need not answer questions and that he need not answer without the advice of counsel: “The trial court’s finding that the waiver and confession were voluntarily and knowingly made is upheld.” <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/#212" aria-description="Citation for case: State v. Edwards"><em>Id., </em>at 212</a></span>, <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/#78" aria-description="Citation for case: State v. Edwards">594 P. 2d, at 78</a></span>.</p>
<p id="b546-6">Because the use of Edward’s confession against him at his trial violated his rights under the Fifth and Fourteenth Amendments as construed in <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona, supra,</a></span> </em>we reverse the judgment of the Arizona Supreme Court.<footnotemark>7</footnotemark></p>
<p id="ATtZ"><page-number citation-index="1" label="481">*481</page-number>II</p>
<p id="Aue">In <em>Miranda </em>v. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span>, </em>the Court determined that the Fifth and Fourteenth Amendments’ prohibition against compelled self-incrimination required that custodial interrogation be <page-number citation-index="1" label="482">*482</page-number>preceded by advice to the putative defendant that he has the right to remain silent and also the right to the presence of an attorney. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#479" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 479</a></span>. The Court also indicated the procedures to be followed subsequent to the warnings. If the accused indicates that he wishes to remain silent, “the interrogation must cease.” If he requests counsel, “the interrogation must cease until an attorney is present.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 474</a></span>.</p>
<p id="b548-5"><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>thus declared that an accused has a Fifth and Fourteenth Amendment right to have counsel present during custodial interrogation. Here, the critical facts as found by the Arizona Supreme Court are that Edwards asserted his right to counsel and his right to remain silent on January 19, but that the police, without furnishing him counsel, returned the next morning to confront him and as a result of the meeting secured incriminating oral admissions. Contrary to the holdings of the state courts, Edwards insists that having exercised his right on the 19th to have counsel present during interrogation, he did not validly waive that right on the 20th. For the following reasons, we agree.</p>
<p id="b548-6">First, the Arizona Supreme Court .applied an erroneous standard for determining waiver where the accused has specifically invoked his right to counsel. It is reasonably clear under our cases that waivers of counsel must not only be voluntary, but must also constitute a knowing and intelligent relinquishment or abandonment of a known right or privilege, a matter which depends in each case “upon the particular facts and circumstances surrounding that case, including the background, experience, and conduct of the accused.” <em>Johnson </em>v. <em>Zerbst, </em><span class="citation" data-id="103050"><a href="/opinion/103050/johnson-v-zerbst/#464" aria-description="Citation for case: Johnson v. Zerbst">304 U. S. 458, 464</a></span> (1938). See <em>Faretta </em>v. <em>California, </em><span class="citation" data-id="9426191"><a href="/opinion/109309/faretta-v-california/#835" aria-description="Citation for case: Faretta v. California">422 U. S. 806, 835</a></span> (1975); <em>North Carolina </em>v. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#374" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369, 374-375</a></span> (1979); <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#404" aria-description="Citation for case: Brewer v. Williams">430 U. S. <page-number citation-index="1" label="483">*483</page-number>387, 404</a></span> (1977); <em>Fare </em>v. <em>Michael C., </em><span class="citation" data-id="9427635"><a href="/opinion/110117/fare-v-michael-c/#724" aria-description="Citation for case: Fare v. Michael C.">442 U. S. 707, 724-725</a></span> (1979).</p>
<p id="b549-5">Considering the proceedings in the state courts in the light of this standard, we note that in denying petitioner’s motion to suppress, the trial court found the admission to have been “voluntary,” App. 3, 95, without separately focusing on whether Edwards had knowingly and intelligently relinquished his right to counsel. The Arizona Supreme Court, in a section of its opinion entitled “Voluntariness of Waiver,” stated that in Arizona, confessions are prima facie involuntary and that the State had the burden of showing by a preponderance of the evidence that the confession was freely and voluntarily made. The court stated that the issue of voluntariness should be determined based on the totality of the circumstances as it related to whether an accused’s action was “knowing and intelligent and whether his will [was] overborne.” <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/#212" aria-description="Citation for case: State v. Edwards">122 Ariz., at 212</a></span>, <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/#78" aria-description="Citation for case: State v. Edwards">594 P. 2d, at 78</a></span>. Once the trial court determines that “the confession is voluntary, the finding will not be upset on appeal absent clear and manifest error.” <em><span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/" aria-description="Citation for case: State v. Edwards">Ibid.</a></span> </em>The court then upheld the trial court’s finding that the “waiver and confession were voluntarily and knowingly made.” <em><span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/" aria-description="Citation for case: State v. Edwards">Ibid.</a></span></em></p>
<p id="b549-6">In referring to the necessity to find Edwards’ confession knowing and intelligent, the State Supreme Court cited <em>Schneckloth </em>v. Bustamante, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#226" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 226</a></span> (1973). Yet, it is clear that <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span> </em>does not control the issue presented in this case. The issue in <em><span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">Schneckloth</a></span> </em>was under what conditions an individual could be found to have consented to a search and thereby waived his Fourth Amendment rights. The Court declined to impose the “intentional relinquishment or abandonment of a known right or privilege” standard and required only that the consent be voluntary under the totality of the circumstances. The Court specifically noted that the right to counsel was a prime example of those rights requiring the special protection of the knowing and intelligent waiver standard, <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#241" aria-description="Citation for case: Schneckloth v. Bustamonte"><em>id., </em>at 241</a></span>, but held that “[t]he considera<page-number citation-index="1" label="484">*484</page-number>tions that informed the Court’s holding in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>are simply inapplicable in the present case.” <em>Id., </em>at 246. <em>Schneck-loth </em>itself thus emphasized that the voluntariness of a consent or an admission on the one hand, and a knowing and intelligent waiver on the other, are discrete inquiries. Here, however sound the conclusion of the state courts as to the voluntariness of Edwards’ admission may be, neither the trial court nor the Arizona Supreme Court undertook to focus on whether Edwards understood his right to counsel and intelligently and knowingly relinquished it. It is thus apparent that the decision below misunderstood the requirement for finding a valid waiver of the right to counsel, once invoked.</p>
<p id="b550-5">Second, although we have held that after initially being advised of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, the accused may himself validly waive his rights and respond to interrogation, see <em>North Carolina </em>v. <span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/#372" aria-description="Citation for case: North Carolina v. Butler"><em>Butler, supra, </em>at 372-376</a></span>, the Court has strongly indicated that additional safeguards are necessary when the accused asks for counsel; and we now hold that when an accused has invoked his right to have counsel present during custodial interrogation, a valid waiver of that right cannot be established by showing only that he responded to further police-initiated custodial interrogation even if he has been advised of his rights.<footnotemark>8</footnotemark> We further hold that an accused, such as Edwards, having expressed his desire to deal with the police only through counsel, is not subject to further interrogation by the authorities until counsel has been made avail<page-number citation-index="1" label="485">*485</page-number>able to him, unless the accused himself initiates further communication, exchanges, or conversations with the police.</p>
<p id="b551-5"><em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>itself indicate'd that the assertion of the right to counsel was a significant event and that once exercised by the accused, “the interrogation must cease until an attorney is present.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#474" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 474</a></span>. Our later cases have not abandoned that view. In <em>Michigan </em>v. <em>Mosley, </em><span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/" aria-description="Citation for case: Michigan v. Mosley">423 U. S. 96</a></span> (1975), the Court noted that <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>had distinguished between the procedural safeguards triggered by a request to remain silent and a request for an attorney and had required that interrogation cease until an attorney was present only if the individual stated that he wanted counsel. <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#104" aria-description="Citation for case: Michigan v. Mosley">423 U. S., at 104, n. 10</a></span>; see also <span class="citation" data-id="9426230"><a href="/opinion/109336/michigan-v-mosley/#109" aria-description="Citation for case: Michigan v. Mosley"><em>id., </em>at 109-111</a></span> (White, J., concurring). In <em>Fare </em>v. <em>Michael C., supra, </em>at 719, the Court referred to <em>Miranda’s </em>“rigid rule that an accused’s request for an attorney is <em>per se </em>an invocation of his Fifth Amendment rights, requiring that all interrogation cease.” And just last Term, in a case where a suspect in custody had invoked his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel, the Court again referred to the “undisputed right” under <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>to remain silent and to be free of interrogation “until he had consulted with a lawyer.” <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#298" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 298</a></span> (1980). We reconfirm these views and, to lend them substance, emphasize that it is inconsistent with <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>and its progeny for the authorities, at their instance, to reinterrogate an accused in custody if he has clearly asserted his right to counsel.</p>
<p id="b551-6">In concluding that the fruits of the interrogation initiated by the police on January 20 could not be used against Edwards, we do not hold or imply that Edwards was powerless to countermand his election or that the authorities could in no event use any incriminating statements made by Edwards prior to his having access to counsel. Had Edwards initiated the meeting on January 20, nothing in the Fifth and Fourteenth Amendments would prohibit the police from merely listening to his voluntary, volunteered statements and using them against him at the trial. The Fifth Amendment right <page-number citation-index="1" label="486">*486</page-number>identified in <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>is the right to have counsel present at any custodial interrogation. Absent such interrogation, there would have been no infringement of the right that Edwards invoked and there would be no occasion to determine whether there had been a valid waiver. <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra,</a></span> </em>makes this sufficiently clear. <span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#298" aria-description="Citation for case: Rhode Island v. Innis">446 U. S., at 298, n. 2</a></span>.<footnotemark>9</footnotemark></p>
<p id="b552-5">But this is not what the facts of this case show. Here, the officers conducting the interrogation on the evening of Jan<page-number citation-index="1" label="487">*487</page-number>uary 19 ceased interrogation when Edwards requested counsel as he had been advised he had the right to do. The Arizona Supreme Court was of the opinion that this was a sufficient invocation of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights, and we are in accord. It is also clear that without making counsel available to Edwards, the police returned to him the next day. This was not at his suggestion or request. Indeed, Edwards informed the detention officer that he did not want to talk to anyone. At the meeting, the detectives told Edwards that they wanted to talk to him and again advised him of his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights. Edwards stated that he would talk, but what prompted this action does not appear. He listened at his own request to part of the taped statement made by one of his alleged accomplices and then made an incriminating statement, which was used against him at his trial. We think it is clear that Edwards was subjected to custodial interrogation on January 20 within the meaning of <em>Rhode Island </em>v. <em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/" aria-description="Citation for case: Rhode Island v. Innis">Innis, supra,</a></span> </em>and that this occurred at the instance of the authorities. His statement, made without having had access to counsel, did not amount to a valid waiver and hence was inadmissible.<footnotemark>10</footnotemark></p>
<p id="b553-6">Accordingly, the holding of the Arizona Supreme Court that Edwards had waived his right to counsel was infirm, and the judgment of that court is reversed.</p>
<p id="APQj">
<em>go Qr^ereg</em>
</p>
<footnote label="1">
<p id="b544-15"> The facts stated in text are for the most part taken from the opinion of the Supreme Court of Arizona.</p>
</footnote>
<footnote label="2">
<p id="b545-7"> It appears from the record that the detectives had brought the tape-recording with them.</p>
</footnote>
<footnote label="3">
<p id="b546-7"> The trial judge emphasized that the detectives had met with Edwards on January 20, without being requested by Edwards to do so, and concluded that they had ignored his request for counsel made the previous evening. App. 91-93.</p>
</footnote>
<footnote label="4">
<p id="b546-8"><em> </em>The case was <em>State </em>v. <em>Travis, </em><span class="citation" data-id="1186156"><a href="/opinion/1186156/state-v-travis/" aria-description="Citation for case: State v. Travis">26 Ariz. App. 24</a></span>, <span class="citation" data-id="1186156"><a href="/opinion/1186156/state-v-travis/" aria-description="Citation for case: State v. Travis">545 P. 2d 986</a></span> (1976).</p>
</footnote>
<footnote label="5">
<p id="b546-9"> The jury in the first trial was unable to reach a verdict.</p>
</footnote>
<footnote label="6">
<p id="b546-10"> This issue was disputed by the State. The court, while finding that the question was arguable, held that Edwards’ request for an attorney to assist him in negotiating a deal was “sufficiently clear” within the context of the interrogation that it “must be interpreted as a request for counsel and as a request to remain silent until counsel was present.” <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/#211" aria-description="Citation for case: State v. Edwards">122 Ariz., at 211</a></span>, <span class="citation" data-id="9629381"><a href="/opinion/1435218/state-v-edwards/#77" aria-description="Citation for case: State v. Edwards">594 P. 2d, at 77</a></span>.</p>
</footnote>
<footnote label="7">
<p id="pACuR"> We thus need not decide Edwards’ claim that the State deprived him of his right to counsel under the Sixth and Fourteenth Amendments as construed and applied in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964). In that ease, the Court held that the Sixth Amendment right to counsel arises whenever an accused has been indicted or adversary criminal proceedings <page-number citation-index="1" label="481">*481</page-number>have otherwise begun and that this right is violated when admissions are subsequently elicited from the accused in the absence of counsel. While initially conceding in its opening brief on the merits that Edwards’ right to counsel under <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>attached immediately after he was formally charged, the State in its supplemental brief and during oral argument took the position that under <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689-690</a></span> (1972), and <em>Moore </em>v. <em>Illinois, </em><span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#226" aria-description="Citation for case: Moore v. Illinois">434 U. S. 220, 226-227</a></span> (1977), the filing of the formal complaint did not constitute the “adversary judicial criminal proceedings” necessary to trigger the Sixth Amendment right to counsel. Under the State Constitution, “[n]o person shall be prosecuted criminally in any court of record for felony or misdemeanor, otherwise than by information or indictment; no person shall be prosecuted for felony by information without having had a preliminary examination before a magistrate or having waived such preliminary examination.” Ariz. Const., Art. 2, § 30. The State contends that the Sixth Amendment right to counsel does not attach until either the constitutionally required indictment or information is filed or at least no earlier than the preliminary hearing to which a defendant is entitled if the matter proceeds by complaint. Under Arizona law, a felony prosecution may be commenced by way of a complaint, Ariz. Rule of Criminal Procedure <em>22. </em>The complaint is a “written statement of the essential facts constituting a public offense, made upon oath before a magistrate,” Rule 2.3, upon which the magistrate either issues an arrest warrant or dismisses the complaint. Rule 2.4. Once arrested, the accused must be taken before the magistrate for a hearing. Rule 4.1. At that hearing, the magistrate ascertains the accused’s true name and address, and informs him of the charges against him, his right to counsel, his right to remain silent, and his right to a preliminary hearing if charged via complaint. Rule 4.2. Unless waived, the preliminary hearing must take place no later than 10 days after the defendant is placed in custody. Rule 5.1. The purpose of the hearing is to determine whether probable cause exists to hold the defendant for trial. Rule 5.3. Against this background and in support of its position, the State relies on <em>Moore </em>v. <em>Illinois, supra, </em>where after recognizing that under Illinois law “[t]he prosecution in this case was commenced . . . when the victim’s complaint was filed in court,” we noted that “adversary judicial criminal proceedings” were initiated when the ensuing preliminary hearing occurred. <span class="citation" data-id="9427017"><a href="/opinion/109757/moore-v-illinois/#228" aria-description="Citation for case: Moore v. Illinois"><em>Moore, supra, </em>at 228</a></span>. Cf. <em>United States </em>v. <em>Duvall, </em><span class="citation" data-id="336320"><a href="/opinion/336320/united-states-of-america-appellee-v-thomas-duvall-and-henry-jones/#20" aria-description="Citation for case: UNITED STATES of America, Appellee, v. Thomas DUVALL and...">537 F. 2d 15, 20-22</a></span> (CA2) (the filing of <page-number citation-index="1" label="482">*482</page-number>a complaint and the issuance of an arrest warrant does not trigger the right to counsel under the Sixth Amendment, that right accruing only upon further proceedings), cert, denied, <span class="citation multiple-matches"><a href="/c/U.%20S./426/950/">426 U. S. 950</a></span> (1976). The Arizona Supreme Court did not address the Sixth Amendment question, nor do we.</p>
</footnote>
<footnote label="8">
<p id="b550-6"> In <em>Brewer </em>v. <em>Williams, </em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387</a></span> (1977), where, as in <em>Massiah </em>v. <em>United States, </em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">377 U. S. 201</a></span> (1964), the Sixth Amendment right to- counsel had accrued, the Court held that a valid waiver of counsel rights should not be inferred from the mere response by the accused to overt or more subtle forms of interrogation' or other efforts to elicit incriminating information. In <em><span class="citation" data-id="9422796"><a href="/opinion/106822/massiah-v-united-states/" aria-description="Citation for case: Massiah v. United States">Massiah</a></span> </em>and <em><span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/" aria-description="Citation for case: Brewer v. Williams">Brewer</a></span>, </em>counsel had been engaged or appointed and the admissions in question were elicited in his absence. But in <em>McLeod </em>v. <em>Ohio, </em><span class="citation" data-id="107070"><a href="/opinion/107070/mcleod-v-ohio/" aria-description="Citation for case: McLEOD v. OHIO">381 U. S. 356</a></span> (1965), we summarily reversed a decision that the police could elicit information after indictment even though counsel had not yet been appointed.</p>
</footnote>
<footnote label="9">
<p id="b552-6"> If, as frequently would occur in the course of a meeting initiated by the accused, the conversation is not wholly one-sided, it is likely that the officers will say or do something that clearly would be “interrogation.” In that event, the question would be whether a valid waiver of the right to counsel and the right to silence had occurred, that is, whether the purported waiver was knowing and intelligent and found to be so under the totality of the circumstances, including the necessary fact that the accused, not the police, reopened the dialogue with the authorities.</p>
<p id="b552-7">Various decisions of the Courts of Appeals are to the effect that a valid waiver of an accused’s previously invoked Fifth Amendment right to counsel is possible. See, e. <em>g., White </em>v. <em>Finkbeiner, </em><span class="citation" data-id="9466321"><a href="/opinion/372605/eutues-white-v-fred-finkbeiner/#191" aria-description="Citation for case: Eutues White v. Fred Finkbeiner">611 F. 2d 186, 191</a></span> (CA7 1979) (“in certain instances, for various reasons, a person in custody who has previously requested counsel may knowingly and voluntarily decide that he no longer wishes to be represented by counsel”), cert, pending, No. 79-6601; <em>Kennedy </em>v. <em>Fairman, </em><span class="citation" data-id="376877"><a href="/opinion/376877/james-albert-kennedy-v-jay-fairman-warden-pontiac-correctional-center/" aria-description="Citation for case: James Albert Kennedy v. Jay Fairman, Warden, Pontiac...">618 F. 2d 1242</a></span> (CA7 1980); <em>United States </em>v. <em>Rodriguez-Gastelum, </em><span class="citation" data-id="9464487"><a href="/opinion/352531/united-states-v-guadalupe-rodriguez-gastelum/#486" aria-description="Citation for case: United States v. Guadalupe Rodriguez-Gastelum">569 F. 2d 482, 486</a></span> (CA9) (en banc) (stating that it makes no sense to hold that once an accused has requested counsel, “ [he] may never, until he has actually talked with counsel, change his mind and decide to speak with the police without an attorney being present”), cert, denied, <span class="citation multiple-matches"><a href="/c/U.%20S./436/919/">436 U. S. 919</a></span> (1978). See generally <em>Cobbs </em>v. <span class="citation" data-id="332367"><a href="/opinion/332367/james-l-cobbs-v-carl-robinson-warden-connecticut-state-prison/#1342" aria-description="Citation for case: James L. Cobbs v. Carl Robinson, Warden, Connecticut..."><em>Robinson, 528 </em>F. 2d 1331, 1342</a></span> (CA2 1975); <em>United States </em>v. <em>Grant, </em><span class="citation" data-id="9463510"><a href="/opinion/343144/united-states-v-elijah-ivory-joe-grant-united-states-of-america-v/" aria-description="Citation for case: United States v. Elijah Ivory Joe Grant, United States of...">549 F. 2d 942</a></span> (CA4 1977), vacated on other grounds <em>sub nom. Whitehead </em>v. <em>United States, </em><span class="citation multiple-matches"><a href="/c/U.%20S./435/912/">435 U. S. 912</a></span> (1978); <em>United States </em>v. <em>Hart, </em><span class="citation" data-id="377005"><a href="/opinion/377005/united-states-v-keith-lamont-hart/" aria-description="Citation for case: United States v. Keith Lamont Hart">619 F. 2d 325</a></span> (CA4 1980); <em>United States </em>v. <em>Hauck, </em><span class="citation" data-id="360916"><a href="/opinion/360916/united-states-v-gary-gust-hauck/" aria-description="Citation for case: United States v. Gary Gust Hauck">586 F. 2d 1296</a></span> (CA8 1978). The rule in the Fifth Circuit is that a knowing and intelligent waiver cannot be found once the Fifth Amendment right to counsel has been clearly invoked unless the accused initiates the renewed contact. See, <em>e. g., United States </em>v. <em>Massey, </em><span class="citation" data-id="343316"><a href="/opinion/343316/united-states-v-john-clayton-massey/" aria-description="Citation for case: United States v. John Clayton Massey">550 F. 2d 300</a></span> (1977); <em>United States </em>v. <em>Priest, </em><span class="citation" data-id="284316"><a href="/opinion/284316/united-states-v-cecil-knox-priest/" aria-description="Citation for case: United States v. Cecil Knox Priest">409 F. 2d 491</a></span> (1969). Waiver is possible, however, when the request for counsel is equivocal. <em>Nash </em>v. <em>Estelle, </em><span class="citation" data-id="9465736"><a href="/opinion/365779/ira-nash-jr-v-w-j-estelle-jr-director-texas-department-of/" aria-description="Citation for case: Ira Nash, Jr. v. W. J. Estelle, Jr., Director, Texas...">597 F. 2d 513</a></span> (CA5 1979) (en banc). See <em>Thompson </em>v. <em>Wainwright, </em><span class="citation" data-id="9465905"><a href="/opinion/368063/larry-thompson-v-louie-l-wainwright-secretary-department-of-offender/" aria-description="Citation for case: Larry Thompson v. Louie L. Wainwright, Secretary,...">601 F. 2d 768</a></span> (CA5 1979).</p>
</footnote>
<footnote label="10">
<p id="b553-9"> We need not decide whether there would have been a valid waiver of counsel had the events of January 20 been the first and only interrogation to which Edwards had been subjected. Cf. <em>North Carolina </em>v. <em>Butler, </em><span class="citation" data-id="9427547"><a href="/opinion/110065/north-carolina-v-butler/" aria-description="Citation for case: North Carolina v. Butler">441 U. S. 369</a></span> (1979).</p>
</footnote>
</opinion>
```

---
