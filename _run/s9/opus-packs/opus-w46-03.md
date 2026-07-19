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

## GROUP: content/cases/McNeil v. Wisconsin.md  (`case`, 5 assertions)

### content_page

```
---
title: "McNeil v. Wisconsin"
type: case
citation: "501 U.S. 171 (1991)"
parallel_cite: "111 S. Ct. 2204; 115 L. Ed. 2d 158"
neutral_cite: 1991 U.S. LEXIS 3483
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1991
date_decided: 1991-06-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1991-06-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: McNeil v. Wisconsin
  varies_by_point: false
  scope_note: "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112622/mcneil-v-wisconsin/"
  cluster_id: 112622
  opinion_id: 9432329
  identity_checked: true
homes:
  - page: "[[Sixth Amendment Right to Counsel]]"
    role: "Key — Progeny / Refinement"
related: ["[[Edwards v. Arizona]]", "[[Michigan v. Jackson]]", "[[Montejo v. Louisiana]]", "[[Massiah v. United States]]"]
aliases: []
tags: ["case", "sixth-amendment", "right-to-counsel", "offense-specific", "miranda"]
holding: "The Sixth Amendment right to counsel is offense-specific, and a 6A invocation is NOT an invocation of the Fifth Amendment *Miranda-Edwards* right to counsel; the two are distinct."
lake:
  record_id: McNeil v. Wisconsin
  status: verified
  projected_at: 2026-07-06
---

# McNeil v. Wisconsin

*501 U.S. 171 (1991)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
McNeil appeared with a public defender at a bail hearing on a West Allis armed robbery. While he was jailed, police later gave him [[Miranda and Custodial Interrogation|Miranda warnings]] and questioned him about a separate set of crimes in Caledonia; he waived his rights and made incriminating statements. He argued that his courtroom appearance with counsel on the West Allis charge barred any police-initiated questioning on the uncharged Caledonia offenses.

## Issue
Whether an accused's invocation of the Sixth Amendment right to counsel at a proceeding on one charged offense also invokes the Fifth Amendment *[[Miranda v. Arizona|Miranda]]*-*[[Edwards v. Arizona|Edwards]]* right to counsel so as to bar police-initiated interrogation about other, uncharged offenses.

## Rule
No. "The Sixth Amendment right, however, is offense specific. It cannot be invoked once for all future prosecutions, for it does not attach until a prosecution is commenced." — 501 U.S. at 175. ^pin-175

Because the Sixth Amendment right is offense-specific, invoking it as to a charged offense does not invoke the distinct Fifth Amendment *[[Miranda v. Arizona|Miranda]]*-*[[Edwards v. Arizona|Edwards]]* right to counsel, which guards against custodial interrogation generally; the two rights serve different interests and are not interchangeable.

## Application
McNeil's Sixth Amendment right had attached and been invoked only as to the West Allis armed robbery with which he had been formally charged. His appearance with counsel on that charge did not invoke the separate Fifth Amendment *[[Miranda v. Arizona|Miranda]]* right; and because the Caledonia offenses were still uncharged, no Sixth Amendment right had attached to them. His subsequent *[[Miranda v. Arizona|Miranda]]* waivers before the Caledonia questioning were therefore valid.

## Conclusion
Affirmed; the statements were admissible.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *McNeil*'s offense-specific holding remains good law. It relied in part on [[Michigan v. Jackson]] (since **overruled** by [[Montejo v. Louisiana]]), but that later development does not disturb *McNeil*'s distinct holding that the Sixth Amendment right is offense-specific and separate from the *[[Miranda v. Arizona|Miranda]]* right.

## Appears on
- [[Sixth Amendment Right to Counsel]] — *Key — Progeny / Refinement*

## Sources
- *McNeil v. Wisconsin*, 501 U.S. 171 (1991) — https://www.courtlistener.com/opinion/112622/mcneil-v-wisconsin/ — pinpoint: 175.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "d1996d80ef9a8668", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "501 U.S. 171 (1991)", "court": "U.S. Supreme Court", "neutral_cite": "1991 U.S. LEXIS 3483", "official_citation_present": true, "parallel_cite": "111 S. Ct. 2204; 115 L. Ed. 2d 158", "title": "McNeil v. Wisconsin", "year": "1991"}}
{"assertion_id": "61f1fa18d72ba7d4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Sixth Amendment right to counsel is offense-specific, and a 6A invocation is NOT an invocation of the Fifth Amendment *Miranda-Edwards* right to counsel; the two are distinct.", "title": "McNeil v. Wisconsin"}}
{"assertion_id": "a4f6a8870b5a641c", "dimension": "support", "kind": "home_role", "locator": {"home": "Sixth Amendment Right to Counsel"}, "payload": {"home": "Sixth Amendment Right to Counsel", "role": "Key — Progeny / Refinement", "title": "McNeil v. Wisconsin"}}
{"assertion_id": "4ad5f04370275091", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1991-06-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "McNeil v. Wisconsin", "field_i_validity": "good_law", "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.", "title": "McNeil v. Wisconsin", "varies_by_point": "false"}}
{"assertion_id": "a1b9b5d51edb34da", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "McNeil v. Wisconsin"}}
```

### lake record — McNeil v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "McNeil v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "McNeil v. Wisconsin",
    "case_name_short": "McNeil",
    "case_name_full": "McNEIL v. WISCONSIN",
    "input_case_name": "McNeil v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1991-06-13",
    "year": 1991,
    "docket": null,
    "cluster_id": 112622,
    "lead_opinion_id": 9432329,
    "sibling_ids": [
      112622,
      9432329,
      9432330,
      9432331
    ],
    "absolute_url": "/opinion/112622/mcneil-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9104955,
        "score": 20,
        "case_name": "McNeil v. Wisconsin"
      },
      {
        "cluster_id": 9104954,
        "score": 20,
        "case_name": "McNeil v. Wisconsin"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "501 U.S. 171",
      "volume": "501",
      "reporter": "U.S.",
      "page": "171",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "111 S. Ct. 2204",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "2204",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 L. Ed. 2d 158",
        "volume": "115",
        "reporter": "L. Ed. 2d",
        "page": "158",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1991 U.S. LEXIS 3483",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3483",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "501 U.S. 171",
        "volume": "501",
        "reporter": "U.S.",
        "page": "171",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "111 S. Ct. 2204",
        "volume": "111",
        "reporter": "S. Ct.",
        "page": "2204",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "115 L. Ed. 2d 158",
        "volume": "115",
        "reporter": "L. Ed. 2d",
        "page": "158",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1991 U.S. LEXIS 3483",
        "volume": "1991",
        "reporter": "U.S. LEXIS",
        "page": "3483",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "501 U.S. 171",
    "official_selection": {
      "court_class": "scotus",
      "selected": "501 U.S. 171",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-175",
      "page": null,
      "quote": "--- # McNeil v. Wisconsin *501 U.S. 171 (1991)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background McNeil appeared with a public defender at a bail hearing on a West Allis armed robbery. While he was jailed, police later gave him Miranda warnings and questioned him about a separate set of crimes in Caledonia; he waived his rights and made incriminating statements. He argued that his courtroom appearance with counsel on the West Allis charge barred any police-initiated questioning on the uncharged Caledonia offenses. ## Issue Whether an accused's invocation of the Sixth Amendment right to counsel at a proceeding on one charged offense also invokes the Fifth Amendment *Miranda*-*Edwards* right to counsel so as to bar police-initiated interrogation about other, uncharged offenses. ## Rule No.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1991-06-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "McNeil v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Old as_of seeds as_of_treatment; S2 derivation re-derives and may downgrade.",
    "point_overrides": [],
    "edges": [
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
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Nader Abdallah",
          "cluster_id": 4574399,
          "cite": [
            "911 F.3d 201"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Guillermo Hernandez Ruiz v. State of Iowa",
          "cluster_id": 4501180,
          "cite": [
            "912 N.W.2d 435"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
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
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Saldierna",
          "cluster_id": 4332369,
          "cite": [
            "369 N.C. 401",
            "794 S.E.2d 474",
            "2016 N.C. LEXIS 1117"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
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
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ward v. Lamar University",
          "cluster_id": 5446494,
          "cite": [
            "484 S.W.3d 440",
            "2016 Tex. App. LEXIS 260",
            "2016 WL 145817"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vicki Ward v. Lamar University, Texas State University System and James Simmons",
          "cluster_id": 2979722,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Tio Sessoms v. D Runnels",
          "cluster_id": 2736109,
          "cite": [
            "768 F.3d 882",
            "2014 U.S. App. LEXIS 18237",
            "2014 WL 4668005"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Medunjanin",
          "cluster_id": 2675041,
          "cite": [
            "752 F.3d 576",
            "2014 U.S. App. LEXIS 9306",
            "2014 WL 2054016"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Doggett v. United States",
          "cluster_id": 112780,
          "cite": [
            "120 L. Ed. 2d 520",
            "112 S. Ct. 2686",
            "505 U.S. 647",
            "1992 U.S. LEXIS 4362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesbrook v. State",
          "cluster_id": 1473130,
          "cite": [
            "29 S.W.3d 103",
            "2000 Tex. Crim. App. LEXIS 86",
            "2000 WL 1346901"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Harris",
          "cluster_id": 1476684,
          "cite": [
            "859 A.2d 364",
            "181 N.J. 391",
            "2004 N.J. LEXIS 1080"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Lawrence",
          "cluster_id": 2501123,
          "cite": [
            "723 S.E.2d 326",
            "365 N.C. 506",
            "2012 WL 1242316",
            "2012 N.C. LEXIS 265"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Crittenden",
          "cluster_id": 2614001,
          "cite": [
            "885 P.2d 887",
            "9 Cal. 4th 83",
            "36 Cal. Rptr. 2d 474",
            "94 Daily Journal DAR 18013",
            "94 Cal. Daily Op. Serv. 9702",
            "1994 Cal. LEXIS 6570"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Guidry v. State",
          "cluster_id": 2342370,
          "cite": [
            "9 S.W.3d 133",
            "1999 Tex. Crim. App. LEXIS 145",
            "1999 WL 1144826"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Janecka v. State",
          "cluster_id": 1743739,
          "cite": [
            "937 S.W.2d 456",
            "1996 Tex. Crim. App. LEXIS 240",
            "1996 WL 682137"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Texas v. Cobb",
          "cluster_id": 118417,
          "cite": [
            "149 L. Ed. 2d 321",
            "121 S. Ct. 1335",
            "532 U.S. 162",
            "2001 U.S. LEXIS 2696"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanchez-Llamas v. Oregon",
          "cluster_id": 145628,
          "cite": [
            "165 L. Ed. 2d 557",
            "126 S. Ct. 2669",
            "548 U.S. 331",
            "2006 U.S. LEXIS 5177"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rothgery v. Gillespie County",
          "cluster_id": 145785,
          "cite": [
            "171 L. Ed. 2d 366",
            "128 S. Ct. 2578",
            "554 U.S. 191",
            "2008 U.S. LEXIS 5057",
            "21 Fla. L. Weekly Fed. S 429",
            "76 U.S.L.W. 4520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Sherwood",
          "cluster_id": 1995264,
          "cite": [
            "982 A.2d 483",
            "603 Pa. 92",
            "2009 Pa. LEXIS 2359"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Yousef",
          "cluster_id": 781722,
          "cite": [
            "327 F.3d 56",
            "61 Fed. R. Serv. 251",
            "2003 U.S. App. LEXIS 6437"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "MacK v. State",
          "cluster_id": 1751529,
          "cite": [
            "650 So. 2d 1289",
            "1994 WL 707272"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Billy Russell Clark v. Tim Murphy",
          "cluster_id": 782256,
          "cite": [
            "331 F.3d 1062",
            "2003 Cal. Daily Op. Serv. 4923",
            "2003 Daily Journal DAR 6263",
            "2003 U.S. App. LEXIS 11496",
            "2003 WL 21338911"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "McNeil v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzk5NTA3MjAwMDAwJnM9MjY3MzAxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112622+OR+9432329+OR+9432330+OR+9432331%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 10,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 11,
        "triage_snippet_classified": 189
      },
      "lane2_top_cited": {
        "query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjAmcz0xNDQ3ODgxJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28112622+OR+9432329+OR+9432330+OR+9432331%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331)",
        "reviewed": 39,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 39,
        "triage_read": 1,
        "triage_snippet_classified": 38
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112622 OR 9432329 OR 9432330 OR 9432331)",
    "indexed_citing_opinions": 1145,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112622,
        "count": 1017,
        "count_source": "search"
      },
      {
        "opinion_id": 9432329,
        "count": 152,
        "count_source": "search"
      },
      {
        "opinion_id": 9432330,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9432331,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1820,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/mcneil-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5MjQ5Nzkmcz0xMDExMTk0NiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28112622+OR+9432329+OR+9432330+OR+9432331%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112622,
        "cited_id": 103833,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 108554,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 110254,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 110475,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111193,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111546,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111614,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 111622,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112100,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112385,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 112513,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 484283,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 1190975,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112622,
        "cited_id": 2207530,
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
    "date_created": "2026-07-05T13:00:42Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:01:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:01:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:05:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:01:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — McNeil v. Wisconsin

```
<opinion type="majority">
<author id="b243-4"><page-number citation-index="1" label="173">*173</page-number>Justice Scalia</author>
<p id="AhX">delivered the opinion of the Court.</p>
<p id="b243-5">This case presents the question whether an accused’s invocation of his Sixth Amendment right to counsel during a judicial proceeding constitutes an invocation of his <em>Miranda </em>right to counsel.</p>
<p id="b243-6">I</p>
<p id="b243-7">Petitioner Paul McNeil was arrested in Omaha, Nebraska, in May 1987, pursuant to a warrant charging him with an armed robbery in West Allis, Wisconsin, a suburb of Milwaukee. Shortly after his arrest, two Milwaukee County deputy sheriffs arrived in Omaha to retrieve him. After advising him of his <em>Miranda </em>rights, the deputies sought to question him. He refused to answer any questions, but did not request an attorney. The deputies promptly ended the interview.</p>
<p id="b243-8">Once back in Wisconsin, petitioner was brought before a Milwaukee County Court Commissioner on the armed robbery charge. The Commissioner set bail and scheduled a preliminary examination. An attorney from the Wisconsin Public Defender’s Office represented petitioner at this initial appearance.</p>
<p id="b243-9">Later that evening, Detective Joseph Butts of the Milwaukee County Sheriff’s Department visited petitioner in jail. Butts had been assisting the Racine County, Wisconsin, police in their investigation of a murder, attempted murder, and armed burglary in the town of Caledonia; petitioner was a suspect. Butts advised petitioner of his <em>Miranda </em>rights, and petitioner signed a form waiving them. In this <page-number citation-index="1" label="174">*174</page-number>first interview, petitioner did not deny knowledge of the Caledonia crimes, but said that he had not been involved.</p>
<p id="b244-5">Butts returned two donia. He again began the encounter by advising petitioner of his <em>Miranda </em>rights and providing a waiver form. Petitioner placed his initials next to each of the warnings and signed the form. This time, petitioner admitted that he had been involved in the Caledonia crimes, which he described in detail. He also implicated two other men, Willie Pope and Lloyd Crowley. The statement was typed up by a detective and given to petitioner to review. Petitioner placed his initials next to every reference to himself and signed every page.</p>
<p id="b244-6">Butts and the Caledonia having in the meantime found and questioned Pope, who convinced them that he had not been involved in the Caledonia crimes. They again began the interview by administering the <em>Miranda </em>warnings and obtaining petitioner’s signature and initials on the waiver form. Petitioner acknowledged that he had lied about Pope’s involvement to minimize his own role in the Caledonia crimes and provided another statement recounting the events, which was transcribed, signed, and initialed as before.</p>
<p id="b244-7">The following day, petitioner was the Caledonia crimes and transferred to that jurisdiction. His pretrial motion to suppress the three incriminating statements was denied. He was convicted of second-degree murder, attempted first-degree murder, and armed robbery, and sentenced to 60 years in prison.</p>
<p id="b244-8">On appeal, petitioner argued that the trial court’s refusal to suppress the statements was reversible error. He contended that his courtroom appearance with an attorney for the West Allis crime constituted an invocation of the <em>Miranda </em>right to counsel, and that any subsequent waiver of that right during police-initiated questioning regarding <em>any </em>offense was invalid. Observing that the State’s Supreme <page-number citation-index="1" label="175">*175</page-number>Court had never addressed this issue, the Court of Appeals certified to that court the following question:</p>
<blockquote id="b245-5">“Does an accused’s request for counsel at an initial appearance on a charged offense constitute an invocation of his fifth amendment right to counsel that precludes police-initiated interrogation on unrelated, uncharged offenses?” App. 16.</blockquote>
<p id="b245-6">The Wisconsin Supreme Court answered “no.” <span class="citation" data-id="9736821"><a href="/opinion/2207530/state-v-mcneil/" aria-description="Citation for case: State v. McNeil">155 Wis. 2d 24</a></span>, <span class="citation" data-id="9736821"><a href="/opinion/2207530/state-v-mcneil/" aria-description="Citation for case: State v. McNeil">454 N. W. 2d 742</a></span> (1990). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./498/937/">498 U. S. 937</a></span> (1990).</p>
<p id="b245-7">II</p>
<p id="b245-8">The Sixth Amendment provides that “[i]n all criminal prosecutions, the accused shall enjoy the right ... to have the Assistance of Counsel for his defence.” In <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), we held that once this right to counsel has attached and has been invoked, any subsequent waiver during a police-initiated .custodial interview is ineffective. It is undisputed, and we accept for purposes of the present case, that at the time petitioner provided the incriminating statements at issue, his Sixth Amendment right had attached and had been invoked with respect to the <em>West Allis armed robbery, </em>for which he had been formally charged.</p>
<p id="b245-9">Sixth Amendment right, however, is offense specific. It cannot be invoked once for all future prosecutions, for it does not attach until a prosecution is commenced, that is, “ ‘at or after the initiation of adversary judicial criminal proceedings — whether by way of formal charge, preliminary hearing, indictment, information, or arraignment.’” <em>United States </em>v. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#188" aria-description="Citation for case: United States v. Gouveia">467 U. S. 180, 188</a></span> (1984) (quoting <em>Kirby </em>v. <em>Illinois, </em><span class="citation" data-id="9424906"><a href="/opinion/108554/kirby-v-illinois/#689" aria-description="Citation for case: Kirby v. Illinois">406 U. S. 682, 689</a></span> (1972) (plurality opinion)). And just as the right is offense specific, so also its <em>Michigan </em>v. <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>effect of invalidating subsequent waivers in police-initiated interviews is offense specific.</p>
<blockquote id="b245-10">“The police have an interest... in investigating new or additional crimes [after an individual is formally charged <page-number citation-index="1" label="176">*176</page-number>with one crime.] . . . [T]o exclude evidence pertaining to charges as to which the Sixth Amendment right to counsel had not attached at the time the evidence was obtained, simply because other charges were pending at that time, would unnecessarily frustrate the public’s interest in the investigation of criminal activities. . . .” <em>Maine </em>v. <em>Moulton, </em><span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#179" aria-description="Citation for case: Maine v. Moulton">474 U. S. 159, 179-180</a></span> (1985).</blockquote>
<blockquote id="b246-5">“Incriminating statements pertaining to other crimes, as <em>to </em>which the Sixth Amendment right has not yet attached, are, of course, admissible at a trial of those offenses.” <span class="citation" data-id="9430241"><a href="/opinion/111546/maine-v-moulton/#180" aria-description="Citation for case: Maine v. Moulton"><em>Id., </em>at 180, n. 16</a></span>.</blockquote>
<p id="b246-6">See also <em>Moran </em>v. <em>Burbine, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#431" aria-description="Citation for case: Moran v. Burbine">475 U. S. 412, 431</a></span> (1986). Because petitioner provided the statements at issue here before his Sixth Amendment right to counsel with respect to the <em>Caledonia offenses </em>had been (or even could have been) invoked, that right poses no bar to the admission of the statements in this case.</p>
<p id="b246-7">Petitioner relies, however, upon a different “right to counsel,” found not in the text of the Sixth Amendment, but in this Court’s jurisprudence relating to the Fifth Amendment guarantee that “[n]o person . . . shall be compelled in any criminal case to be a witness against himself.” In <em>Miranda </em>v. <em>Arizona, </em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), we established a number of prophylactic rights designed to counteract the “inherently compelling pressures” of custodial interrogation, including the right to have counsel present. <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>did not hold, however, that those rights could not be waived. On the contrary, the opinion recognized that statements elicited during custodial interrogation would be admissible if the prosecution could establish that the suspect “knowingly and intelligently waived his privilege against self-incrimination and his right to retained or appointed counsel.” <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#475" aria-description="Citation for case: Miranda v. Arizona"><em>Id., </em>at 475</a></span>.</p>
<p id="b246-8">In <em>Edwards </em>v. <em>Arizona, </em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S. 477</a></span> (1981), we established a second layer of prophylaxis for the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel: Once a suspect asserts the right, not only must the <page-number citation-index="1" label="177">*177</page-number>current interrogation cease, but he may not be approached for further interrogation “until counsel has been made available to him,” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">451 U. S., at 484</a></span>-485—which means, we have most recently held, that counsel must be present, <em>Minnick </em>v. <em>Mississippi, </em><span class="citation" data-id="9432173"><a href="/opinion/112513/minnick-v-mississippi/" aria-description="Citation for case: Minnick v. Mississippi">498 U. S. 146</a></span> (1990). If the police do subsequently initiate an encounter in the absence of counsel (assuming there has been no break in custody), the suspect’s statements are presumed involuntary and therefore inadmissible as substantive evidence at trial, even where the suspect executes a waiver and his statements would be considered voluntary under traditional standards. This is “designed to prevent police from badgering a defendant into waiving his previously asserted <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights,” <em>Michigan </em>v. <em>Harvey, </em><span class="citation" data-id="9431937"><a href="/opinion/112385/michigan-v-harvey/#350" aria-description="Citation for case: Michigan v. Harvey">494 U. S. 344, 350</a></span> (1990). The <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>rule, moreover, is <em>not </em>offense specific: Once a suspect invokes the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel for interrogation regarding one offense, he may not be reapproached regarding <em>any </em>offense unless counsel is present. <em>Arizona </em>v. <em>Roberson, </em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/" aria-description="Citation for case: Arizona v. Roberson">486 U. S. 675</a></span> (1988).</p>
<p id="b247-5">Having described the nature and effects of both the Sixth Amendment right to counsel and the <em>Miranda-Edwards </em>“Fifth Amendment” right to counsel, we come at last to the issue here: Petitioner seeks to prevail by combining the two of them. He contends that, although he expressly waived his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel on every occasion he was interrogated, those waivers were the invalid product of impermissible approaches, because his prior invocation of the offense-specific Sixth Amendment right with regard to the West Allis burglary was also an invocation of the nonoffense-specific <em>Miranda-Edwards </em>right. We think that is false as a matter of fact and inadvisable (if even permissible) as a contrary-to-fact presumption of policy.</p>
<p id="b247-6">As to the former: The purpose of the Sixth Amendment counsel guarantee — and hence the purpose of invoking it — is to “protec[t] the unaided layman at critical confrontations” with his “expert adversary,” the government, <em>after </em>“the ad<page-number citation-index="1" label="178">*178</page-number>verse positions of government and defendant have solidified” with respect to a particular alleged crime. <em>Gouveia, </em><span class="citation" data-id="9429629"><a href="/opinion/111193/united-states-v-gouveia/#189" aria-description="Citation for case: United States v. Gouveia">467 U. S., at 189</a></span>. The purpose of the <em>Miranda-Edwards </em>guarantee, on the other hand — and hence the purpose of invoking it — is to protect a quite different interest: the suspect’s “desire to deal with the police only through counsel,” <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona">Edwards, <em>supra, </em>at 484</a></span>. This is in one respect narrower than the interest protected by the Sixth Amendment guarantee (because it relates only to custodial interrogation) and in another respect broader (because it relates to interrogation regarding <em>any </em>suspected crime and attaches whether or not the “adversarial relationship” produced by a pending prosecution has yet arisen). To invoke the Sixth Amendment interest is, as a matter of <em>fact, not </em>to invoke the <em>Miranda-Edwards </em>interest. One might be quite willing to speak to the police without counsel present concerning many matters, but not the matter under prosecution. It can be said, perhaps, that it is <em>likely </em>that one who has asked for counsel’s assistance in defending against a prosecution would want counsel present for all custodial interrogation, even interrogation unrelated to the charge. That is not necessarily true, since suspects often believe that they can avoid the laying of charges by demonstrating an assurance of innocence through frank and unassisted answers to questions. But even if it were true, the <em>likelihood </em>that a suspect would wish counsel to be present is not the test for applicability of <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>. </em>The rule of that case applies only when the suspect “ha[s] <em>expressed” </em>his wish for the particular sort of lawyerly assistance that is the subject of <span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/#484" aria-description="Citation for case: Edwards v. Arizona"><em>Miranda. Edwards, supra, </em>at 484</a></span> (emphasis added). It requires, at a minimum, some statement that can reasonably be construed to be an expression of a desire for the assistance of an attorney <em>in dealing with custodial interrogation by the police. </em>Requesting the assistance of an attorney at a bail hearing does not bear that construction. “[T]o find that [the defendant] invoked his Fifth Amendment right to counsel on the present charges merely by requesting <page-number citation-index="1" label="179">*179</page-number>the appointment of counsel at his arraignment on the unrelated charge is to disregard the ordinary meaning of that request.” <em>State </em>v. <em>Stewart, </em><span class="citation" data-id="1190975"><a href="/opinion/1190975/state-v-stewart/#471" aria-description="Citation for case: State v. Stewart">113 Wash. 2d 462, 471</a></span>, <span class="citation" data-id="1190975"><a href="/opinion/1190975/state-v-stewart/#849" aria-description="Citation for case: State v. Stewart">780 P. 2d 844, 849</a></span> (1989), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./494/1020/">494 U. S. 1020</a></span> (1990).</p>
<p id="b249-5">Our holding in <em>Michigan </em>v. <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">475 U. S. 625</a></span> (1986), does not, as petitioner asserts, contradict the foregoing distinction; to the contrary, it <em>rests </em>upon it. That case, it will be recalled, held that after the Sixth Amendment right to counsel attaches and is invoked, any statements obtained from the accused during subsequent police-initiated custodial questioning regarding the charge at issue (even if the accused purports to waive his rights) are inadmissible. The State in <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>opposed that outcome on the ground that assertion of the Sixth Amendment right to counsel did not realistically constitute the <em>expression </em>(as <em>Edivards </em>required) of a wish to have counsel present during custodial interrogation. See 475 U. S., at 632-633. Our response to that contention was not that it <em>did </em>constitute such an expression, but that it <em>did not have to, </em>since the relevant question was not whether the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“Fifth Amendment” right had been <em>asserted, </em>but whether the Sixth Amendment right to counsel had been <em>waived. </em>We said that since our “settled approach to questions of waiver requires us to give a broad, rather than a narrow, interpretation to a defendant’s request for counsel, ... we <em>presume </em>that the defendant requests the lawyer’s services at every critical stage of the prosecution.” 475 U. S., at 633 (emphasis added). The holding of <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>implicitly rejects any equivalence in fact between invocation of the Sixth Amendment right to counsel and the expression necessary to trigger <em>Edivards. </em>If such invocation constituted a real (as opposed to merely a legally presumed) request for the assistance of counsel in custodial interrogation, it would have been quite unnecessary for <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>to go on to establish, as it did, a new Sixth Amendment rule of no police-<page-number citation-index="1" label="180">*180</page-number>initiated interrogation; we could simply have cited and relied upon <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span>.</em><footnotemark><em>1</em></footnotemark></p>
<p id="b250-5">There remains to though the assertion of the Sixth Amendment right to counsel does not <em>in fact </em>imply an assertion of the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>“Fifth Amendment” right, we should declare it to be. such as a matter of sound policy. Assuming we have such an expansive power under the Constitution, it would not wisely be exercised. Petitioner’s proposed rule has only insignificant advantages. If a suspect does not wish to communicate with the police except through an attorney, he can simply tell them that when they give him the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>warnings. There is not the remotest chance that he will feel “badgered” by their asking to talk to him without counsel present, since the subject will not be the charge on which he has already requested counsel’s assistance (for in that event <em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/" aria-description="Citation for case: Michigan v. Jackson">Jackson</a></span> </em>would preclude initiation of the interview) and he will not have rejected uncounseled interrogation on <em>any </em>subject before (for in that event <em><span class="citation" data-id="9428324"><a href="/opinion/110475/edwards-v-arizona/" aria-description="Citation for case: Edwards v. Arizona">Edwards</a></span> </em>would preclude initiation of the interview). The proposed rule would, however, seriously impede effective law enforcement. The Sixth Amendment right to <page-number citation-index="1" label="181">*181</page-number>counsel attaches at the first formal proceeding against an accused, and in most States, at least with respect to serious offenses, free counsel is made available at that time and ordinarily requested. Thus, if we were to adopt petitioner’s rule, most persons in pretrial custody for serious offenses would be <em>unapproachable </em>by police officers suspecting them of involvement in other crimes, <em>even though they have never expressed any unwillingness to be questioned. </em>Since the ready ability to obtain uncoerced confessions is not an evil but an unmitigated good, society would be the loser. Admissions of guilt resulting from valid <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>waivers “are more than merely ‘desirable’; they are essential to society’s compelling interest in finding, convicting, and punishing those who violate the law.” <em>Moran, </em><span class="citation" data-id="9842071"><a href="/opinion/111614/moran-v-burbine/#426" aria-description="Citation for case: Moran v. Burbine">475 U. S., at 426</a></span> (citation omitted).<footnotemark>2</footnotemark></p>
<p id="b251-5">Petitioner urges upon us the desirability of providing a “clear and unequivocal” guideline for the police: no police-initiated questioning of any person in custody who has requested counsel to assist him in defense or in interrogation. But the police do not need our assistance to establish such a <page-number citation-index="1" label="182">*182</page-number>guideline; they are free, if they wish, to adopt it on their own. Of course it <em>is </em>our task to establish guidelines for judicial review. We like <em>them </em>to be “clear and unequivocal,” see, <em>e. </em>g., <em>Roberson, </em><span class="citation" data-id="9431349"><a href="/opinion/112100/arizona-v-roberson/#681" aria-description="Citation for case: Arizona v. Roberson">486 U. S., at 681-682</a></span>, but only when they guide sensibly and in a direction we are authorized to go. Petitioner’s proposal would in our view do much more harm than good, and is not contained within, or even in furtherance of, the Sixth Amendment’s right to counsel or the Fifth Amendment’s right against compelled self-incrimination.<footnotemark>3</footnotemark></p>
<p id="b252-5">* * *</p>
<p id="b252-6">"This Court is forever adding new stories to the temples of constitutional law, and the temples have a way of collapsing when one story too many is added.” <em>Douglas </em>v. <em>Jeannette, </em><span class="citation" data-id="9419344"><a href="/opinion/103833/douglas-v-city-of-jeannette/#181" aria-description="Citation for case: Douglas v. City of Jeannette">319 U. S. 157, 181</a></span> (1943) (opinion of Jackson, J.). We decline to add yet another story to <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>. </em>The judgment of the Wisconsin Supreme Court is</p>
<p id="A4bd">
<em>Affirmed.</em>
</p>
<footnote label="1">
<p id="b250-6"> A footnote in <em>Jackson, </em><span class="citation" data-id="9430407"><a href="/opinion/111622/michigan-v-jackson/#633" aria-description="Citation for case: Michigan v. Jackson">475 U. S., at 633-634, n. 7</a></span>, quoted with approval statements by the Michigan Supreme Court to the effect that the average person does not ‘“understand and appreciate the subtle distinctions between the Fifth and Sixth Amendment rights to counsel,’” that it “‘makes little sense to afford relief from further interrogation to a defendant who asks a police officer for an attorney, but permit further interrogation to a defendant who makes an identical request to a judge,’ ” and that “ ‘[t]he simple fact that defendant has requested an attorney indicates that he does not believe that he is sufficiently capable of dealing with his adversaries singlehandedly.’” <em>Michigan </em>v. <em>Bladel, </em><span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#63" aria-description="Citation for case: People v. Bladel">421 Mich. 39, 63-64</a></span>, <span class="citation" data-id="9663090"><a href="/opinion/1640358/people-v-bladel/#67" aria-description="Citation for case: People v. Bladel">365 N. W. 2d 56, 67</a></span> (1984). Those observations were perhaps true in the context of deciding whether a request for the assistance of counsel in defending against a particular charge implied a desire to have that counsel serve as an “intermediary” for all further interrogation on that charge. They are assuredly not true in the quite different context of deciding whether such a request implies a desire never to undergo custodial interrogation, about anything, without counsel present.</p>
</footnote>
<footnote label="2">
<p id="b251-6"> The dissent condemns these sentiments as “revealing a preference for an inquisitorial system of justice.” <em>Post, </em>at 189. We cannot imagine what this means. What makes a system adversarial rather than inquisitorial is not the presence of counsel, much less the presence of counsel where the defendant has not requested it; but rather, the presence of a judge who does not (as an inquisitor does) conduct the factual and legal investigation himself, but instead decides on the basis of facts and arguments pro and con adduced by the parties. In the inquisitorial criminal process of the civil law, the defendant ordinarily has counsel; and in the adversarial criminal process of the common law, he sometimes does not. Our system of justice is, and has always been, an inquisitorial one at the investigatory stage (even the grand jury is an inquisitorial body), and no other disposition is conceivable. Even if detectives were to bring impartial magistrates around with them to all interrogations, there would be no decision for the impartial magistrate to umpire. If all the dissent means by a “preference for an inquisitorial system” is a preference not to require the presence of counsel during an investigatory interview where the interviewee has not requested it — that is a strange way to put it, but we are guilty.</p>
</footnote>
<footnote label="3">
<p id="b252-8"> The dissent predicts that the result in this case will routinely be circumvented when, “[i]n future preliminary hearings, competent counsel. . . make sure that they, or their clients, make a statement on the record” invoking the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel. <em>Post, </em>at 184. We have in fact never held that a person can invoke his <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>rights anticipatorily, in a context other than “custodial interrogation” — which a preliminary hearing will not always, or even usually, involve, cf. <em>Pennsylvania </em>v. <em>Muniz, </em><span class="citation" data-id="9432075"><a href="/opinion/112464/pennsylvania-v-muniz/#601" aria-description="Citation for case: Pennsylvania v. Muniz">496 U. S. 582, 601-602</a></span> (1990) (plurality opinion); <em>Rhode Island </em>v. <em>Innis, </em><span class="citation" data-id="9427901"><a href="/opinion/110254/rhode-island-v-innis/#298" aria-description="Citation for case: Rhode Island v. Innis">446 U. S. 291, 298-303</a></span> (1980). If the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel can be invoked at a preliminary hearing, it could be argued, there is no logical reason why it could not be invoked by a letter prior to arrest, or indeed even prior to identification as a suspect. Most rights must be asserted when the government seeks to take the action they protect against. The fact that we have allowed the <em><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span> </em>right to counsel, once asserted, to be effective with respect to future custodial interrogation does not necessarily mean that we will allow it to be asserted initially outside the context of custodial interrogation, with similar future effect. Assuming, however, that an assertion at arraignment would be effective, and would be routinely made, the mere fact that adherence to the principle of our decisions will not have substantial consequences is no reason to abandon that principle. It would remain intolerable that a person in custody who had expressed <em>no </em>objection to being questioned would be unapproachable.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Messerschmidt v. Millender.md  (`case`, 6 assertions)

### content_page

```
---
title: "Messerschmidt v. Millender"
type: case
citation: "565 U.S. 535 (2012)"
parallel_cite: "132 S. Ct. 1235; 182 L. Ed. 2d 47"
neutral_cite: 2012 U.S. LEXIS 1687
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2012
date_decided: 2012-02-22
docket: 10-704
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2012-02-22
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Messerschmidt v. Millender
  varies_by_point: false
  scope_note: Good law on qualified immunity for executing a magistrate-approved warrant later claimed to be overbroad.
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/623242/messerschmidt-v-millender/"
  cluster_id: 623242
  opinion_id: 623242
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Franks Challenges]]"
    role: "Related (cross-doctrine)"
related: ["[[Malley v. Briggs]]", "[[United States v. Leon]]", "[[Harlow v. Fitzgerald]]", "[[Pearson v. Callahan]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "warrant", "overbroad-warrant", "objective-reasonableness"]
holding: "Officers retain qualified immunity for obtaining and executing a facially overbroad warrant where their reliance on the magistrate's approval was objectively reasonable; the Malley exception is a high threshold."
lake:
  record_id: Messerschmidt v. Millender
  status: verified
  projected_at: 2026-07-09
---

# Messerschmidt v. Millender

*565 U.S. 535 (2012)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Jerry Bowen assaulted his former girlfriend with "a black sawed-off shotgun with a pistol grip" and fired at her as she fled, Detective Messerschmidt prepared a warrant to search Augusta Millender's home — where Bowen was thought to live — for **all firearms** and **all gang-related material**. The warrant was reviewed and approved by a supervisor, a deputy district attorney, and a magistrate before execution. The Millenders sued the officers under § 1983, alleging the warrant was unconstitutionally overbroad.

## Issue
Whether officers are entitled to [[Qualified Immunity|qualified immunity]] from a § 1983 damages suit for obtaining and executing a warrant later alleged to be overbroad, where a neutral magistrate approved the warrant.

## Rule
Officers are immune unless the warrant was so obviously deficient that no reasonable officer could have relied on it. A magistrate's approval is strong evidence of objective reasonableness, but it does not end the inquiry: "the fact that a neutral magistrate has issued a warrant authorizing the allegedly unconstitutional search or seizure does not end the inquiry into objective reasonableness." — 565 U.S. at 547. ^pin-547

The exception, drawn from [[Malley v. Briggs]] and [[United States v. Leon]], applies only where the affidavit is "so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable." — *Id.* (quoting *Leon*, 468 U.S. at 923). But "the threshold for establishing this exception is a high one, and it should be." — [*Id.*](https://www.courtlistener.com/opinion/623242/messerschmidt-v-millender/#:~:text=so%20lacking%20in%20indicia%20of) ^pin-547b

## Application
The warrant's authorization to seize all firearms and gang material was at least arguably supported: Bowen had used a firearm in the assault and was a known gang member, so an officer could reasonably believe the broad categories were tied to evidence of the crime and of Bowen's dangerousness and gang ties. Even if the warrant was in fact overbroad, the question was only whether reliance on it was objectively reasonable — and the additional review by a supervisor, a prosecutor, and the magistrate confirmed that this was not the rare case where every reasonable officer would have known the warrant should not issue.

## Conclusion
Reversed. The officers were entitled to [[Qualified Immunity|qualified immunity]]; their reliance on the approved warrant was not objectively unreasonable, so the *[[Malley v. Briggs|Malley]]* exception did not strip their immunity.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Messerschmidt* applies the [[Malley v. Briggs]] / [[United States v. Leon]] standard to the warrant-immunity question and sits within the qualified-immunity framework of [[Harlow v. Fitzgerald]] and [[Pearson v. Callahan]]. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Franks Challenges]] — *Related (cross-doctrine)*

## Sources
- *Messerschmidt v. Millender*, 565 U.S. 535 (2012) — https://www.courtlistener.com/opinion/623242/messerschmidt-v-millender/ — pinpoint: 547 (lead opinion id 9485385).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "e530e572e15a39dd", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "565 U.S. 535 (2012)", "court": "U.S. Supreme Court", "neutral_cite": "2012 U.S. LEXIS 1687", "official_citation_present": true, "parallel_cite": "132 S. Ct. 1235; 182 L. Ed. 2d 47", "title": "Messerschmidt v. Millender", "year": "2012"}}
{"assertion_id": "3dd6b5ff80735325", "dimension": "support", "kind": "home_role", "locator": {"home": "Franks Challenges"}, "payload": {"home": "Franks Challenges", "role": "Related (cross-doctrine)", "title": "Messerschmidt v. Millender"}}
{"assertion_id": "8f55f8eb4e3a1742", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Messerschmidt v. Millender"}}
{"assertion_id": "cbcef71975527330", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Officers retain qualified immunity for obtaining and executing a facially overbroad warrant where their reliance on the magistrate's approval was objectively reasonable; the Malley exception is a high threshold.", "title": "Messerschmidt v. Millender"}}
{"assertion_id": "19d1ef1493839fcc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Messerschmidt v. Millender"}}
{"assertion_id": "ff856448e735fe85", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2012-02-22", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Messerschmidt v. Millender", "field_i_validity": "good_law", "scope_note": "Good law on qualified immunity for executing a magistrate-approved warrant later claimed to be overbroad.", "title": "Messerschmidt v. Millender", "varies_by_point": "false"}}
```

### lake record — Messerschmidt v. Millender

```json
{
  "schema_version": "s2.v1",
  "record_id": "Messerschmidt v. Millender",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Messerschmidt v. Millender",
    "case_name_short": "Messerschmidt",
    "case_name_full": "MESSERSCHMIDT Et Al. v. MILLENDER, Executor of ESTATE OF MILLENDER, DECEASED, Et Al.",
    "input_case_name": "Messerschmidt v. Millender",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2012-02-22",
    "year": 2012,
    "docket": "10-704",
    "cluster_id": 623242,
    "lead_opinion_id": 623242,
    "sibling_ids": [
      623242,
      9485385,
      9485386,
      9485387,
      9485388
    ],
    "absolute_url": "/opinion/623242/messerschmidt-v-millender/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "565 U.S. 535",
      "volume": "565",
      "reporter": "U.S.",
      "page": "535",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "132 S. Ct. 1235",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 47",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "47",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2012 U.S. LEXIS 1687",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "132 S. Ct. 1235",
        "volume": "132",
        "reporter": "S. Ct.",
        "page": "1235",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "182 L. Ed. 2d 47",
        "volume": "182",
        "reporter": "L. Ed. 2d",
        "page": "47",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2012 U.S. LEXIS 1687",
        "volume": "2012",
        "reporter": "U.S. LEXIS",
        "page": "1687",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "565 U.S. 535",
        "volume": "565",
        "reporter": "U.S.",
        "page": "535",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "565 U.S. 535",
    "official_selection": {
      "court_class": "scotus",
      "selected": "565 U.S. 535",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-547",
      "page": null,
      "quote": "and fired at her as she fled, Detective Messerschmidt prepared a warrant to search Augusta Millender's home \u2014 where Bowen was thought to live \u2014 for **all firearms** and **all gang-related material**. The warrant was reviewed and approved by a supervisor, a deputy district attorney, and a magistrate before execution. The Millenders sued the officers under \u00a7 1983, alleging the warrant was unconstitutionally overbroad. ## Issue Whether officers are entitled to qualified immunity from a \u00a7 1983 damages suit for obtaining and executing a warrant later alleged to be overbroad, where a neutral magistrate approved the warrant. ## Rule Officers are immune unless the warrant was so obviously deficient that no reasonable officer could have relied on it. A magistrate's approval is strong evidence of objective reasonableness, but it does not end the inquiry:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-547b",
      "page": null,
      "quote": "so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable.",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 5024,
      "fragment": "#:~:text=so%20lacking%20in%20indicia%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2012-02-22",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Messerschmidt v. Millender",
    "varies_by_point": false,
    "scope_note": "Good law on qualified immunity for executing a magistrate-approved warrant later claimed to be overbroad.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Gregory Baldwin v. City of Estherville, Iowa Matt Reineke, Individually and in His Official Capacity as an Officer of the Estherville Police Department and Matt Hellickson, Individually and in His Official Capacity as an Officer of the Estherville Police Department",
          "cluster_id": 4512940,
          "cite": [
            "915 N.W.2d 259"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Lauren Graham v. C. Gagnon",
          "cluster_id": 4242146,
          "cite": [
            "831 F.3d 176",
            "2016 U.S. App. LEXIS 13672",
            "2016 WL 4011156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cion Peralta v. T. Dillard",
          "cluster_id": 814919,
          "cite": [
            "704 F.3d 1124",
            "2013 U.S. App. LEXIS 379",
            "2013 WL 57893"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane1_negative"
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
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "DiStiso ex rel. DiStiso v. Cook",
          "cluster_id": 807074,
          "cite": [
            "691 F.3d 226",
            "2012 WL 3570755"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Felders v. Malcom",
          "cluster_id": 2679716,
          "cite": [
            "755 F.3d 870",
            "2014 WL 2782368",
            "2014 U.S. App. LEXIS 11627"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Garcia v. Does 1-40",
          "cluster_id": 8442118,
          "cite": [
            "779 F.3d 84",
            "2014 U.S. App. LEXIS 24772",
            "2015 WL 737758"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Andy Thayer v. Ralph Chiczewski",
          "cluster_id": 808703,
          "cite": [
            "705 F.3d 237",
            "2012 U.S. App. LEXIS 26899",
            "2012 WL 6621169"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jonathan Davidson v. City of Stafford, Texas, et a",
          "cluster_id": 4346685,
          "cite": [
            "848 F.3d 384",
            "2017 WL 507305",
            "2017 U.S. App. LEXIS 2189"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bobby Bland v. B. Roberts",
          "cluster_id": 1041207,
          "cite": [
            "730 F.3d 368",
            "36 I.E.R. Cas. (BNA) 1045",
            "41 Media L. Rep. (BNA) 2445",
            "2013 WL 5228033",
            "2013 U.S. App. LEXIS 19268"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brittany Harris v. Kimberly Klare",
          "cluster_id": 4532638,
          "cite": [
            "902 F.3d 630"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Leona Mullins v. Oscar Cyranek",
          "cluster_id": 3153107,
          "cite": [
            "805 F.3d 760",
            "2015 FED App. 0273P",
            "2015 U.S. App. LEXIS 19485",
            "2015 WL 6859303"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stonecipher v. Valles",
          "cluster_id": 2681550,
          "cite": [
            "759 F.3d 1134",
            "2014 U.S. App. LEXIS 12384",
            "2014 WL 2937038"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Zalaski v. City of Hartford",
          "cluster_id": 1034747,
          "cite": [
            "723 F.3d 382",
            "2013 WL 3796448",
            "2013 U.S. App. LEXIS 14898"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Randy Cole v. Michael Hunter",
          "cluster_id": 4654098,
          "cite": [
            "935 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "April Smith v. Jason Munday",
          "cluster_id": 4345933,
          "cite": [
            "848 F.3d 248"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rex Chappell v. R. Mandeville",
          "cluster_id": 818032,
          "cite": [
            "706 F.3d 1052",
            "2013 WL 364203",
            "2013 U.S. App. LEXIS 2192"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Nathson Fields v. Lawrence Wharrie",
          "cluster_id": 2708971,
          "cite": [
            "740 F.3d 1107",
            "2014 WL 243245",
            "2014 U.S. App. LEXIS 1333"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Clint Small v. James McCrystal",
          "cluster_id": 820762,
          "cite": [
            "708 F.3d 997",
            "2013 WL 599567",
            "2013 U.S. App. LEXIS 3372"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Frank Snider, III v. Matthew Peters",
          "cluster_id": 2676418,
          "cite": [
            "752 F.3d 1149"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lal v. California",
          "cluster_id": 8441683,
          "cite": [
            "746 F.3d 1112",
            "2014 WL 1272781"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Paul Pavulak",
          "cluster_id": 812356,
          "cite": [
            "700 F.3d 651",
            "2012 U.S. App. LEXIS 24036",
            "2012 WL 5870742"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Turkmen v. Hasty",
          "cluster_id": 8442249,
          "cite": [
            "789 F.3d 218",
            "2015 U.S. App. LEXIS 10160",
            "2015 WL 3756331"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Eddie Ford v. City of Yakima",
          "cluster_id": 820004,
          "cite": [
            "706 F.3d 1188",
            "2013 U.S. App. LEXIS 2716",
            "2013 WL 485233"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ganek v. Leibowitz",
          "cluster_id": 4434937,
          "cite": [
            "874 F.3d 73",
            "2017 WL 4639594",
            "2017 U.S. App. LEXIS 20226"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wesby v. District of Columbia",
          "cluster_id": 2722589,
          "cite": [
            "412 U.S. App. D.C. 246",
            "765 F.3d 13",
            "2014 U.S. App. LEXIS 16893",
            "2014 WL 4290316"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Almighty Supreme Born Allah v. Milling",
          "cluster_id": 8443619,
          "cite": [
            "876 F.3d 48"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Thomas Avina v. United States",
          "cluster_id": 802109,
          "cite": [
            "681 F.3d 1127",
            "2012 WL 2099257",
            "2012 U.S. App. LEXIS 11876"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Messerschmidt v. Millender:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 137,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 137,
        "triage_read": 4,
        "triage_snippet_classified": 133
      },
      "lane2_top_cited": {
        "query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zNyZzPTgwNjExOCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28623242+OR+9485385+OR+9485386+OR+9485387+OR+9485388%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388)",
        "reviewed": 32,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 32,
        "triage_read": 0,
        "triage_snippet_classified": 32
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(623242 OR 9485385 OR 9485386 OR 9485387 OR 9485388)",
    "indexed_citing_opinions": 182,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 623242,
        "count": 127,
        "count_source": "search"
      },
      {
        "opinion_id": 9485385,
        "count": 59,
        "count_source": "search"
      },
      {
        "opinion_id": 9485386,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485387,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9485388,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 873,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/messerschmidt-v-millender.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2MzM0Nzkmcz05NDY3ODE5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28623242+OR+9485385+OR+9485386+OR+9485387+OR+9485388%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 623242,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 96405,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 101643,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 106865,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 109522,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 110959,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111143,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111263,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 112671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 118030,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 118289,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 131161,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 145777,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 173961,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 1122997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 623242,
        "cited_id": 1192791,
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
    "date_created": "2026-07-05T13:05:30Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:09:17Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:05:40Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Messerschmidt v. Millender

```
(Slip Opinion)              OCTOBER TERM, 2011                                       1

                                       Syllabus

         NOTE: Where it is feasible, a syllabus (headnote) will be released, as is
       being done in connection with this case, at the time the opinion is issued.
       The syllabus constitutes no part of the opinion of the Court but has been
       prepared by the Reporter of Decisions for the convenience of the reader.
       See United States v. Detroit Timber & Lumber Co., 200 U. S. 321, 337.


SUPREME COURT OF THE UNITED STATES

                                       Syllabus

MESSERSCHMIDT ET AL. v. MILLENDER, EXECUTOR OF
   ESTATE OF MILLENDER, DECEASED, ET AL.

CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR
                  THE NINTH CIRCUIT

  No. 10–704.     Argued December 5, 2011—Decided February 22, 2012
Shelly Kelly was afraid that she would be attacked by her boyfriend,
  Jerry Ray Bowen, while she moved out of her apartment. She there-
  fore requested police protection. Two officers arrived, but they were
  called away to an emergency. As soon as the officers left, Bowen
  showed up at the apartment, yelled “I told you never to call the cops
  on me bitch!” and attacked Kelly, attempting to throw her over a se-
  cond-story landing. After Kelly escaped to her car, Bowen pointed a
  sawed-off shotgun at her and threatened to kill her if she tried to
  leave. Kelly nonetheless sped away as Bowen fired five shots at the
  car, blowing out one of its tires.
     Kelly later met with Detective Curt Messerschmidt to discuss the
  incident. She described the attack in detail, mentioned that Bowen
  had previously assaulted her, that he had ties to the Mona Park
  Crips gang, and that he might be staying at the home of his former
  foster mother, Augusta Millender. Following this conversation, Mes-
  serschmidt conducted a detailed investigation, during which he con-
  firmed Bowen’s connection to the Millenders’ home, verified his
  membership in two gangs, and learned that Bowen had been arrested
  and convicted for numerous violent and firearm-related offenses.
  Based on this investigation, Messerschmidt drafted an application
  for a warrant authorizing a search of the Millenders’ home for all
  firearms and ammunition, as well as evidence indicating gang
  membership.
     Messerschmidt included two affidavits in the warrant application.
  The first detailed his extensive law enforcement experience and his
  specialized training in gang-related crimes. The second, expressly in-
  corporated into the search warrant, described the incident and ex-
2                  MESSERSCHMIDT v. MILLENDER

                                 Syllabus

    plained why Messerschmidt believed there was probable cause for the
    search. It also requested that the warrant be endorsed for night ser-
    vice because of Bowen’s gang ties. Before submitting the application
    to a magistrate for approval, Messerschmidt had it reviewed by his
    supervisor, Sergeant Robert Lawrence, as well as a police lieutenant
    and a deputy district attorney. Messerschmidt then submitted the
    application to a magistrate, who issued the warrant. The ensuing
    search uncovered only Millender’s shotgun, a California Social Ser-
    vices letter addressed to Bowen, and a box of .45-caliber ammunition.
       The Millenders filed an action under 42 U. S. C. §1983 against pe-
    titioners Messerschmidt and Lawrence, alleging that the officers had
    subjected them to an unreasonable search in violation of the Fourth
    Amendment. The District Court granted summary judgment to the
    Millenders, concluding that the firearm and gang-material aspects of
    the search warrant were overbroad and that the officers were not en-
    titled to qualified immunity from damages. The Ninth Circuit, sit-
    ting en banc, affirmed the denial of qualified immunity. The court
    held that the warrant’s authorization was unconstitutionally over-
    broad because the affidavits and warrant failed to establish probable
    cause that the broad categories of firearms, firearm-related material,
    and gang-related material were contraband or evidence of a crime,
    and that a reasonable officer would have been aware of the warrant’s
    deficiency.
Held: The officers are entitled to qualified immunity. Pp. 8−19.
    (a) Qualified immunity “protects government officials ‘from liability
 for civil damages insofar as their conduct does not violate clearly es-
 tablished statutory or constitutional rights of which a reasonable
 person would have known.’ ” Pearson v. Callahan, 555 U. S. 223, 231.
 Where the alleged Fourth Amendment violation involves a search or
 seizure pursuant to a warrant, the fact that a neutral magistrate has
 issued a warrant is the clearest indication that the officers acted in
 an objectively reasonable manner, or in “objective good faith.” United
 States v. Leon, 468 U. S. 897, 922–923. Nonetheless, that fact does
 not end the inquiry into objective reasonableness. The Court has rec-
 ognized an exception allowing suit when “it is obvious that no rea-
 sonably competent officer would have concluded that a warrant
 should issue.” Malley v. Briggs, 475 U. S. 335, 341. The “shield of
 immunity” otherwise conferred by the warrant, id., at 345, will be
 lost, for example, where the warrant was “based on an affidavit so
 lacking in indicia of probable cause as to render official belief in its
 existence entirely unreasonable.” Leon, 468 U. S., at 923. The
 threshold for establishing this exception is high. “[I]n the ordinary
 case, an officer cannot be expected to question the magistrate’s prob-
 able-cause determination” because “[i]t is the magistrate’s responsi-
                   Cite as: 565 U. S. ____ (2012)                    3

                              Syllabus

bility to determine whether the officer’s allegations establish proba-
ble cause and, if so, to issue a warrant comporting in form with the
requirements of the Fourth Amendment.” Leon, supra, at 921. Pp.
8−10.
   (b) This case does not fall within that narrow exception. It would
not be entirely unreasonable for an officer to believe that there was
probable cause to search for all firearms and firearm-related materi-
als. Under the circumstances set forth in the warrant, an officer
could reasonably conclude that there was a “fair probability” that the
sawed-off shotgun was not the only firearm Bowen owned, Illinois v.
Gates, 462 U. S. 213, 238, and that Bowen’s sawed-off shotgun was il-
legal. Cf. 26 U. S. C. §§ 5845(a), 5861(d). Given Bowen’s possession
of one illegal gun, his gang membership, willingness to use the gun to
kill someone, and concern about the police, it would not be unreason-
able for an officer to conclude that Bowen owned other illegal guns.
An officer also could reasonably believe that seizure of firearms was
necessary to prevent further assaults on Kelly. California law allows
a magistrate to issue a search warrant for items “in the possession of
any person with the intent to use them as a means of committing a
public offense,” Cal. Penal Code Ann. §1524(a)(3), and the warrant
application submitted by the officers specifically referenced this pro-
vision as a basis for the search. Pp. 10–12.
   (c) Regarding the warrant’s authorization to search for gang-
related materials, a reasonable officer could view Bowen’s attack as
motivated not by the souring of his romantic relationship with Kelly
but by a desire to prevent her from disclosing details of his gang ac-
tivity to the police. It would therefore not be unreasonable—based on
the facts set out in the affidavit—for an officer to believe that evi-
dence of Bowen’s gang affiliation would prove helpful in prosecuting
him for the attack on Kelly, in supporting additional, related charges
against Bowen for the assault, or in impeaching Bowen or rebutting
his defenses. Moreover, even if this were merely a domestic dispute,
a reasonable officer could still conclude that gang paraphernalia
found at the Millenders’ residence could demonstrate Bowen’s control
over the premises or his connection to other evidence found there.
Pp. 12−16.
   (d) The fact that the officers sought and obtained approval of the
warrant application from a superior and a deputy district attorney
before submitting it to the magistrate provides further support for
the conclusion that an officer could reasonably have believed that the
scope of the warrant was supported by probable cause. A contrary
conclusion would mean not only that Messerschmidt and Lawrence
were “plainly incompetent” in concluding that the warrant was sup-
ported by probable cause, Malley, supra, at 341, but that their super-
4                  MESSERSCHMIDT v. MILLENDER

                                  Syllabus

    visor, the deputy district attorney, and the magistrate were as well.
    Pp. 16−18.
       (e) In holding that the warrant in this case was so obviously defec-
    tive that no reasonable officer could have believed it to be valid, the
    court below erred in relying on Groh v. Ramirez, 540 U. S. 551.
    There, officers who carried out a warrant-approved search were not
    entitled to qualified immunity because the warrant failed to describe
    any of the items to be seized and “even a cursory reading of the war-
    rant” would have revealed this defect. Id., at 557. Here, in contrast,
    any arguable defect would have become apparent only upon a close
    parsing of the warrant application, and a comparison of the support-
    ing affidavit to the terms of the warrant to determine whether the af-
    fidavit established probable cause to search for all the items listed in
    the warrant. Unlike in Groh, any error here would not be one that
    “just a simple glance” would have revealed. Id. at 564. Pp. 18−19.
620 F. 3d 1016, reversed.

  ROBERTS, C. J., delivered the opinion of the Court, in which SCALIA,
KENNEDY, THOMAS, BREYER, and ALITO, JJ., joined. BREYER, J., filed a
concurring opinion. KAGAN, J., filed an opinion concurring in part and
dissenting in part. SOTOMAYOR, J., filed a dissenting opinion, in which
GINSBURG, J., joined.
                        Cite as: 565 U. S. ____ (2012)                              1

                             Opinion of the Court

     NOTICE: This opinion is subject to formal revision before publication in the
     preliminary print of the United States Reports. Readers are requested to
     notify the Reporter of Decisions, Supreme Court of the United States, Wash-
     ington, D. C. 20543, of any typographical or other formal errors, in order
     that corrections may be made before the preliminary print goes to press.


SUPREME COURT OF THE UNITED STATES
                                   _________________

                                   No. 10–704
                                   _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                              [February 22, 2012]


   CHIEF JUSTICE ROBERTS delivered the opinion of the
Court.
   Petitioner police officers conducted a search of respond-
ents’ home pursuant to a warrant issued by a neutral
magistrate. The warrant authorized a search for all guns
and gang-related material, in connection with the investi-
gation of a known gang member for shooting at his ex-
girlfriend with a pistol-gripped sawed-off shotgun, because
she had “call[ed] the cops” on him. App. 56. Respondents
brought an action seeking to hold the officers personally
liable under 42 U. S. C. §1983, alleging that the search
violated their Fourth Amendment rights because there
was not sufficient probable cause to believe the items
sought were evidence of a crime. In particular, respond-
ents argued that there was no basis to search for all
guns simply because the suspect owned and had used a
sawed-off shotgun, and no reason to search for gang mate-
rial because the shooting at the ex-girlfriend for “call[ing]
the cops” was solely a domestic dispute. The Court of
2             MESSERSCHMIDT v. MILLENDER

                     Opinion of the Court

Appeals for the Ninth Circuit held that the warrant was
invalid, and that the officers were not entitled to immu-
nity from personal liability because this invalidity was so
obvious that any reasonable officer would have recognized
it, despite the magistrate’s approval. We disagree and
reverse.
                               I

                               A

  Shelly Kelly decided to break off her romantic relation-
ship with Jerry Ray Bowen and move out of her apart-
ment, to which Bowen had a key. Kelly feared an attack
from Bowen, who had previously assaulted her and had
been convicted of multiple violent felonies. She therefore
asked officers from the Los Angeles County Sheriff’s De-
partment to accompany her while she gathered her things.
Deputies from the Sheriff ’s Department came to assist
Kelly but were called away to respond to an emergency
before the move was complete.
  As soon as the officers left, an enraged Bowen appeared
at the bottom of the stairs to the apartment, yelling “I told
you never to call the cops on me bitch!” App. 39, 56.
Bowen then ran up the stairs to Kelly, grabbed her by her
shirt, and tried to throw her over the railing of the second-
story landing. When Kelly successfully resisted, Bowen
bit her on the shoulder and attempted to drag her inside
the apartment by her hair. Kelly again managed to escape
Bowen’s grasp, and ran to her car. By that time, Bowen
had retrieved a black sawed-off shotgun with a pistol grip.
He ran in front of Kelly’s car, pointed the shotgun at her,
and told Kelly that if she tried to leave he would kill her.
Kelly leaned over, fully depressed the gas pedal, and sped
away. Bowen fired at the car a total of five times, blowing
out the car’s left front tire in the process, but Kelly man-
aged to escape.
  Kelly quickly located police officers and reported the
                 Cite as: 565 U. S. ____ (2012)          3

                     Opinion of the Court

assault. She told the police what had happened—that
Bowen had attacked her after becoming “angry because
she had called the Sheriff’s Department”—and she men-
tioned that Bowen was “an active member of the ‘Mona
Park Crips,’ ” a local street gang. Id., at 39. Kelly also
provided the officers with photographs of Bowen.
   Detective Curt Messerschmidt was assigned to investi-
gate the incident. Messerschmidt met with Kelly to obtain
details of the assault and information about Bowen. Kelly
described the attack and informed Messerschmidt that she
thought Bowen was staying at his foster mother’s home
at 2234 East 120th Street. Kelly also informed Messer-
schmidt of Bowen’s previous assaults on her and of his
gang ties.
   Messerschmidt then conducted a background check on
Bowen by consulting police records, California Depart-
ment of Motor Vehicles records, and the “cal-gang” data-
base. Based on this research, Messerschmidt confirmed
Bowen’s connection to the 2234 East 120th Street address.
He also confirmed that Bowen was an “active” member of
the Mona Park Crips and a “secondary” member of the
Dodge City Crips. Id., at 64. Finally, Messerschmidt
learned that Bowen had been arrested and convicted for
numerous violent and firearm-related offenses. Indeed, at
the time of the investigation, Bowen’s “rapsheet” spanned
over 17 printed pages, and indicated that he had been
arrested at least 31 times. Nine of these arrests were for
firearms offenses and six were for violent crimes, includ-
ing three arrests for assault with a deadly weapon (fire-
arm). Id., at 72–81.
   Messerschmidt prepared two warrants: one to authorize
Bowen’s arrest and one to authorize the search of 2234
East 120th Street. An attachment to the search warrant
described the property that would be the object of the
search:
4             MESSERSCHMIDT v. MILLENDER

                     Opinion of the Court

    “All handguns, rifles, or shotguns of any caliber, or
    any firearms capable of firing ammunition, or fire-
    arms or devices modified or designed to allow it [sic]
    to fire ammunition. All caliber of ammunition, miscel-
    laneous gun parts, gun cleaning kits, holsters which
    could hold or have held any caliber handgun being
    sought. Any receipts or paperwork, showing the pur-
    chase, ownership, or possession of the handguns being
    sought. Any firearm for which there is no proof of
    ownership. Any firearm capable of firing or cham-
    bered to fire any caliber ammunition.
    “Articles of evidence showing street gang membership
    or affiliation with any Street Gang to include but not
    limited to any reference to ‘Mona Park Crips’, includ-
    ing writings or graffiti depicting gang membership,
    activity or identity. Articles of personal property
    tending to establish the identity of person [sic] in con-
    trol of the premise or premises. Any photographs or
    photograph albums depicting persons, vehicles, weap-
    ons or locations, which may appear relevant to gang
    membership, or which may depict the item being
    sought and or believed to be evidence in the case being
    investigated on this warrant, or which may depict ev-
    idence of criminal activity. Additionally to include
    any gang indicia that would establish the persons be-
    ing sought in this warrant, affiliation or membership
    with the ‘Mona Park Crips’ street gang.” Id., at 52.

  Two affidavits accompanied Messerschmidt’s warrant ap-
plications. The first affidavit described Messerschmidt’s
extensive law enforcement experience, including that he
had served as a peace officer for 14 years, that he was
then assigned to a “specialized unit” “investigating gang
related crimes and arresting gang members for various
violations of the law,” that he had been involved in “hun-
                 Cite as: 565 U. S. ____ (2012)           5

                     Opinion of the Court

dreds of gang related incidents, contacts, and or arrests”
during his time on the force, and that he had “received
specialized training in the field of gang related crimes”
and training in “gang related shootings.” Id., at 53–54.
   The second affidavit—expressly incorporated into the
search warrant—explained why Messerschmidt believed
there was sufficient probable cause to support the war-
rant. That affidavit described the facts of the incident
involving Kelly and Bowen in great detail, including the
weapon used in the assault. The affidavit recounted that
Kelly had identified Bowen as the assailant and that she
thought Bowen might be found at 2234 East 120th Street.
It also reported that Messerschmidt had “conducted an
extensive background search on the suspect by utilizing
departmental records, state computer records, and other
police agency records,” and that from that information he
had concluded that Bowen resided at 2234 East 120th
Street. Id., at 58.
   The affidavit requested that the search warrant be
endorsed for night service because “information provided
by the victim and the cal-gang data base” indicated that
Bowen had “gang ties to the Mona Park Crip gang” and
that “night service would provide an added element of
safety to the community as well as for the deputy person-
nel serving the warrant.” Id., at 59. The affidavit con-
cluded by noting that Messerschmidt “believe[d] that the
items sought” would be in Bowen’s possession and that
“recovery of the weapon could be invaluable in the success-
ful prosecution of the suspect involved in this case, and
the curtailment of further crimes being committed.” Ibid.
   Messerschmidt submitted the warrants to his super-
visors—Sergeant Lawrence and Lieutenant Ornales—for
review. Deputy District Attorney Janet Wilson also re-
viewed the materials and initialed the search warrant,
indicating that she agreed with Messerschmidt’s assess-
ment of probable cause. Id., at 27, 47. Finally, Messer-
6             MESSERSCHMIDT v. MILLENDER

                    Opinion of the Court

schmidt submitted the warrants to a magistrate. The
magistrate approved the warrants and authorized night
service.
  The search warrant was served two days later by a team
of officers that included Messerschmidt and Lawrence.
Sheriff’s deputies forced open the front door of 2234 East
120th Street and encountered Augusta Millender—a
woman in her seventies—and Millender’s daughter and
grandson. As instructed by the police, the Millenders
went outside while the residence was secured but re-
mained in the living room while the search was conducted.
Bowen was not found in the residence. The search did,
however, result in the seizure of Augusta Millender’s
shotgun, a California Social Services letter addressed to
Bowen, and a box of .45-caliber ammunition.
  Bowen was arrested two weeks later after Messer-
schmidt found him hiding under a bed in a motel room.
                             B
   The Millenders filed suit in Federal District Court
against the County of Los Angeles, the sheriff ’s depart-
ment, the sheriff, and a number of individual officers,
including Messerschmidt and Lawrence. The complaint
alleged, as relevant here, that the search warrant was
invalid under the Fourth Amendment. It sought damages
from Messerschmidt and Lawrence, among others.
   The parties filed cross motions for summary judgment
on the validity of the search warrant. The District Court
found the warrant defective in two respects. The District
Court concluded that the warrant’s authorization to
search for firearms was unconstitutionally overbroad
because the “crime specified here was a physical assault
with a very specific weapon”—a black sawed-off shotgun
with a pistol grip—negating any need to “search for all
firearms.” Millender v. County of Los Angeles, Civ. No.
05–2298 (CD Cal., Mar. 15, 2007), App. to Pet. for Cert.
                 Cite as: 565 U. S. ____ (2012)            7

                     Opinion of the Court

106, 157, 2007 WL 7589200, *21. The court also found
the warrant overbroad with respect to the search for gang-
related materials, because there “was no evidence that the
crime at issue was gang-related.” App. to Pet. for Cert.
157. As a result, the District Court granted summary
judgment to the Millenders on their constitutional chal-
lenges to the firearm and gang material aspects of the
search warrant. Id., at 160. The District Court also re-
jected the officers’ claim that they were entitled to quali-
fied immunity from damages. Id., at 171.
   Messerschmidt and Lawrence appealed, and a divided
panel of the Court of Appeals for the Ninth Circuit re-
versed the District Court’s denial of qualified immunity.
564 F. 3d 1143 (2009). The court held that the officers
were entitled to qualified immunity because “they reason-
ably relied on the approval of the warrant by a deputy
district attorney and a judge.” Id., at 1145.
   The Court of Appeals granted rehearing en banc and
affirmed the District Court’s denial of qualified immunity.
620 F. 3d 1016 (CA9 2010). The en banc court concluded
that the warrant’s authorization was unconstitutionally
overbroad because the affidavit and the warrant failed to
“establish[ ] probable cause that the broad categories of
firearms, firearm-related material, and gang-related
material described in the warrant were contraband or
evidence of a crime.” Id., at 1033. In the en banc court’s
view, “the deputies had probable cause to search for a
single, identified weapon . . . . They had no probable cause
to search for the broad class of firearms and firearm-
related materials described in the warrant.” Id., at 1027.
In addition, “[b]ecause the deputies failed to establish any
link between gang-related materials and a crime, the
warrant authorizing the search and seizure of all gang-
related evidence [was] likewise invalid.” Id., at 1031.
Concluding that “a reasonable officer in the deputies’
position would have been well aware of this deficiency,”
8              MESSERSCHMIDT v. MILLENDER

                      Opinion of the Court

the en banc court held that the officers were not entitled to
qualified immunity. Id., at 1033–1035.
  There were two separate dissenting opinions. Judge
Callahan determined that “the officers had probable cause
to search for and seize any firearms in the home in which
Bowen, a gang member and felon, was thought to reside.”
Id., at 1036. She also concluded that “the officers reason-
ably relied on their superiors, the district attorney, and
the magistrate to correct” any overbreadth in the warrant,
and that the officers were entitled to qualified immunity
because their actions were not objectively unreasonable.
Id., at 1044, 1049. Judge Silverman also dissented, con-
cluding that the “deputies’ belief in the validity of . . . the
warrant was entirely reasonable” and that the “record
[wa]s totally devoid of any evidence that the deputies
acted other than in good faith.” Id., at 1050. Judge Tall-
man joined both dissents.
  We granted certiorari. 564 U. S. ___ (2011).
                              II
  The Millenders allege that they were subjected to an
unreasonable search in violation of the Fourth Amend-
ment because the warrant authorizing the search of their
home was not supported by probable cause. They seek
damages from Messerschmidt and Lawrence for their roles
in obtaining and executing this warrant. The validity of
the warrant is not before us. The question instead is
whether Messerschmidt and Lawrence are entitled to im-
munity from damages, even assuming that the warrant
should not have been issued.
  “The doctrine of qualified immunity protects govern-
ment officials ‘from liability for civil damages insofar as
their conduct does not violate clearly established statutory
or constitutional rights of which a reasonable person
would have known.’ ” Pearson v. Callahan, 555 U. S. 223,
231 (2009) (quoting Harlow v. Fitzgerald, 457 U. S. 800,
                     Cite as: 565 U. S. ____ (2012)                   9

                         Opinion of the Court

818 (1982)). Qualified immunity “gives government offi-
cials breathing room to make reasonable but mistaken
judgments,” and “protects ‘all but the plainly incompetent
or those who knowingly violate the law.’ ” Ashcroft v. al-
Kidd, 563 U. S. ___, ___ (2011) (slip op., at 12) (quoting
Malley v. Briggs, 475 U. S. 335, 341 (1986)). “[W]hether
an official protected by qualified immunity may be held
personally liable for an allegedly unlawful official action
generally turns on the ‘objective legal reasonableness’ of
the action, assessed in light of the legal rules that were
‘clearly established’ at the time it was taken.” Anderson v.
Creighton, 483 U. S. 635, 639 (1987) (citation omitted).
   Where the alleged Fourth Amendment violation involves
a search or seizure pursuant to a warrant, the fact that a
neutral magistrate has issued a warrant is the clearest
indication that the officers acted in an objectively reason-
able manner or, as we have sometimes put it, in “objective
good faith.” United States v. Leon, 468 U. S. 897, 922–923
(1984).1 Nonetheless, under our precedents, the fact that
a neutral magistrate has issued a warrant authorizing the
allegedly unconstitutional search or seizure does not end
the inquiry into objective reasonableness. Rather, we
have recognized an exception allowing suit when “it is
obvious that no reasonably competent officer would have
concluded that a warrant should issue.” Malley, 475 U. S.,
at 341. The “shield of immunity” otherwise conferred by
the warrant, id., at 345, will be lost, for example, where
the warrant was “based on an affidavit so lacking in indi-
cia of probable cause as to render official belief in its exist-
——————
   1 Although Leon involved the proper application of the exclusionary

rule to remedy a Fourth Amendment violation, we have held that “the
same standard of objective reasonableness that we applied in the con-
text of a suppression hearing in Leon defines the qualified immun-
ity accorded an officer” who obtained or relied on an allegedly invalid
warrant. Malley v. Briggs, 475 U. S. 335, 344 (1986) (citation omitted);
Groh v. Ramirez, 540 U. S. 551, 565, n. 8 (2004).
10               MESSERSCHMIDT v. MILLENDER

                          Opinion of the Court

ence entirely unreasonable.” Leon, 468 U. S., at 923 (in-
ternal quotation marks omitted).2
   Our precedents make clear, however, that the threshold
for establishing this exception is a high one, and it should
be. As we explained in Leon, “[i]n the ordinary case, an
officer cannot be expected to question the magistrate’s
probable-cause determination” because “[i]t is the magis-
trate’s responsibility to determine whether the officer’s
allegations establish probable cause and, if so, to issue a
warrant comporting in form with the requirements of the
Fourth Amendment.” Id., at 921; see also Malley, supra,
at 346, n. 9 (“It is a sound presumption that the magis-
trate is more qualified than the police officer to make a
probable cause determination, and it goes without saying
that where a magistrate acts mistakenly in issuing a
warrant but within the range of professional competence
of a magistrate, the officer who requested the warrant
cannot be held liable” (internal quotation marks and
citation omitted)).
                              III
  The Millenders contend, and the Court of Appeals held,
that their case falls into this narrow exception. According
to the Millenders, the officers “failed to provide any facts
or circumstances from which a magistrate could properly
conclude that there was probable cause to seize the broad
classes of items being sought,” and “[n]o reasonable officer
——————
  2 The dissent relies almost entirely on facts outside the affidavit,

including Messerschmidt’s deposition testimony, post, at 4, 11 (opinion
of SOTOMAYOR, J.), crime analysis forms, post, at 5, Kelly’s interview,
post, at 5–6, and n. 5, Messerschmidt’s notes regarding Kelly’s inter-
view, post, at 5–6, n. 5, and even several briefs filed in the District
Court and the Court of Appeals, post, at 8–9, 12. In contrast, the
dissent cites the probable cause affidavit itself only twice. See post, at
12. There is no contention before us that the affidavit was misleading
in omitting any of the facts on which the dissent relies. Cf. Leon, 468
U. S., at 923.
                 Cite as: 565 U. S. ____ (2012)          11

                     Opinion of the Court

would have presumed that such a warrant was valid.”
Brief for Respondents 27. We disagree.
                              A
   With respect to the warrant’s authorization to search for
and seize all firearms, the Millenders argue that “a rea-
sonably well-trained officer would have readily perceived
that there was no probable cause to search the house for
all firearms and firearm-related items.” Id., at 32. Noting
that “the affidavit indicated exactly what item was evi-
dence of a crime—the ‘black sawed off shotgun with a
pistol grip,’ ” they argue that “[n]o facts established that
Bowen possessed any other firearms, let alone that such
firearms (if they existed) were ‘contraband or evidence of a
crime.’ ” Ibid. (quoting App. 56).
   Even if the scope of the warrant were overbroad in
authorizing a search for all guns when there was infor-
mation only about a specific one, that specific one was a
sawed-off shotgun with a pistol grip, owned by a known
gang member, who had just fired the weapon five times in
public in an attempt to murder another person, on the
asserted ground that she had “call[ed] the cops” on him.
Id., at 56. Under these circumstances—set forth in the
warrant—it would not have been unreasonable for an
officer to conclude that there was a “fair probability” that
the sawed-off shotgun was not the only firearm Bowen
owned. Illinois v. Gates, 462 U. S. 213, 238 (1983). And
it certainly would have been reasonable for an officer to
assume that Bowen’s sawed-off shotgun was illegal. Cf. 26
U. S. C. §§5845(a), 5861(d). Evidence of one crime is not
always evidence of several, but given Bowen’s possession
of one illegal gun, his gang membership, his willingness
to use the gun to kill someone, and his concern about
the police, a reasonable officer could conclude that there
would be additional illegal guns among others that Bowen
12               MESSERSCHMIDT v. MILLENDER

                          Opinion of the Court

owned.3
   A reasonable officer also could believe that seizure of the
firearms was necessary to prevent further assaults on
Kelly. California law allows a magistrate to issue a search
warrant for items “in the possession of any person with
the intent to use them as a means of committing a public
offense,” Cal. Penal Code Ann. §1524(a)(3) (West 2011),
and the warrant application submitted by the officers
specifically referenced this provision as a basis for the
search. App. 48. Bowen had already attempted to murder
Kelly once with a firearm, and had yelled “I’ll kill you” as
she tried to escape from him. Id., at 56–57. A reasonable
officer could conclude that Bowen would make another
attempt on Kelly’s life and that he possessed other fire-
arms “with the intent to use them” to that end. Cal. Penal
Code Ann. §1524(a)(3).
   Given the foregoing, it would not have been “entirely
unreasonable” for an officer to believe, in the particular
circumstances of this case, that there was probable cause
to search for all firearms and firearm-related materials.
Leon, supra, at 923 (internal quotation marks omitted).
   With respect to the warrant’s authorization to search for
evidence of gang membership, the Millenders contend that
“no reasonable officer could have believed that the affida-
vit presented to the magistrate contained a sufficient basis
to conclude that the gang paraphernalia sought was con-
traband or evidence of a crime.” Brief for Respondents 28.
They argue that “the magistrate [could not] have reasona-
bly concluded, based on the affidavit, that Bowen’s gang
membership had anything to do with the crime under
investigation” because “[t]he affidavit described a ‘spousal
——————
   3 The dissent caricatures our analysis as being that “because Bowen

fired one firearm, it was reasonable for the police to conclude . . . that
[he] must have possessed others,” post, at 10 (opinion of SOTOMAYOR,
J.). This simply avoids coming to grips with the facts of the crime at
issue.
                     Cite as: 565 U. S. ____ (2012)                   13

                          Opinion of the Court

assault’ that ensued after Kelly decided to end her ‘on
going dating relationship’ with Bowen” and “[n]othing in
that description suggests that the crime was gang-
related.” Ibid. (quoting App. 55).
   This effort to characterize the case solely as a domes-
tic dispute, however, is misleading.        Cf. post, at 5
(SOTOMAYOR, J., dissenting); post, at 2 (KAGAN, J., concur-
ring in part and dissenting in part). Messerschmidt began
his affidavit in support of the warrant by explaining that
he “has been investigating an assault with a deadly weap-
on incident” and elaborated that the crime was a “spousal
assault and an assault with a deadly weapon.” App. 55
(emphasis added). The affidavit also stated that Bowen
was “a known Mona Park Crip gang member” “based on
information provided by the victim and the cal-gang data-
base,”4 and that he had attempted to murder Kelly after
becoming enraged that she had “call[ed] the cops on
[him].” Id., at 56, 58–59. A reasonable officer could cer-
tainly view Bowen’s attack as motivated not by the sour-
ing of his romantic relationship with Kelly but instead by
a desire to prevent her from disclosing details of his gang
activity to the police. She was, after all, no longer linked
with him as a girlfriend; he had assaulted her in the past;
and she had indeed called the cops on him. And, as the
affidavit supporting the warrant made clear, Kelly had in
fact given the police information about Bowen’s gang ties.
Id., at 59.5
——————
  4 Although the cal-gang database states that information contained

therein cannot be used to establish probable cause, see App. 64, the
affidavit makes clear that Kelly also provided this information to
Messerschmidt, id., at 59, as she did to the deputies who initially
responded to the attack, id., at 39 (describing Kelly’s statement that
Bowen was “an active member of the ‘Mona Park Crips’ ”). We there-
fore need not decide whether the cal-gang database’s disclaimer is
relevant to Fourth Amendment analysis.
  5 Contrary to the dissent’s suggestion, see post, at 5–6, n. 5 (opinion

of SOTOMAYOR, J.), the affidavit’s account of Bowen’s statements is
14               MESSERSCHMIDT v. MILLENDER

                          Opinion of the Court

   It would therefore not have been unreasonable—based
on the facts set out in the affidavit—for an officer to be-
lieve that evidence regarding Bowen’s gang affiliation
would prove helpful in prosecuting him for the attack on
Kelly. See Warden, Md. Penitentiary v. Hayden, 387 U. S.
294, 307 (1967) (holding that the Fourth Amendment
allows a search for evidence when there is “probable cause
. . . to believe that the evidence sought will aid in a partic-
ular apprehension or conviction”). Not only would such
evidence help to establish motive, either apart from or in
addition to any domestic dispute, it would also support the
bringing of additional, related charges against Bowen for
the assault. See, e.g., Cal. Penal Code Ann. §136.1(b)(1)
(West 1999) (It is a crime to “attempt[ ] to prevent or
dissuade another person who has been the victim of a
crime or who is witness to a crime from . . . [m]aking any
report of that victimization to any . . . law enforcement
officer”).6
——————
consistent with other accounts of the confrontation, in particular the
report prepared by the officers who spoke with Kelly immediately after
the attack. See App. 39 (stating that when Bowen “appeared at the
base of the stairs and began yelling at [Kelly,] [h]e was angry because
she had called the Sheriff ’s Department”). And at no point during this
litigation has the accuracy of the affidavit’s account of the attack been
called into question.
   6 The dissent relies heavily on Messerschmidt’s deposition, in which

he stated that Bowen’s crime was not a “gang crime.” See post, at 4–7.
Messerschmidt’s belief about the nature of the crime, however, is not
information he possessed but a conclusion he reached based on infor-
mation known to him. See Anderson v. Creighton, 483 U. S. 635, 641
(1987). We have “eschew[ed] inquiries into the subjective beliefs of law
enforcement officers who seize evidence pursuant to a subsequently
invalidated warrant.” United States v. Leon, 468 U. S. 897, 922, n. 23
(1984); see also Harlow v. Fitzgerald, 457 U. S. 800, 815–819 (1982). In
any event, as the dissent recognizes, the inquiry under our precedents
is whether “a reasonably well-trained officer in petitioner’s position
would have known that his affidavit failed to establish probable cause.”
Malley, 475 U. S., at 345 (emphasis added). Messerschmidt’s own
evaluation does not answer the question whether it would have been
                      Cite as: 565 U. S. ____ (2012)                    15

                          Opinion of the Court

   In addition, a reasonable officer could believe that evi-
dence demonstrating Bowen’s membership in a gang
might prove helpful in impeaching Bowen or rebutting
various defenses he could raise at trial. For example,
evidence that Bowen had ties to a gang that uses guns
such as the one he used to assault Kelly would certainly be
relevant to establish that he had familiarity with or access
to this type of weapon.
   Moreover, even if this were merely a domestic dispute, a
reasonable officer could still conclude that gang parapher-
nalia found at the Millenders’ residence would aid in
the prosecution of Bowen by, for example, demonstrating
Bowen’s connection to other evidence found there. The
warrant authorized a search for “any gang indicia that
would establish the persons being sought in this warrant,”
and “[a]rticles of personal property tending to establish
the identity of [the] person in control of the premise or
premises.” App. 52. Before the District Court, the Millen-
ders “acknowledge[d] that evidence of who controlled the
premises would be relevant if incriminating evidence were
found and it became necessary to tie that evidence to a
person, ” and the District Court approved that aspect of
the warrant on this basis. App. to Pet. for Cert. 158–159
(internal quotation marks omitted). Given Bowen’s known
gang affiliation, a reasonable officer could conclude that
gang paraphernalia found at the residence would be an
effective means of demonstrating Bowen’s control over the
premises or his connection to evidence found there.7
——————
unreasonable for an officer to have reached a different conclusion from
the facts in the affidavit. See n. 2, supra.
  7 The Fourth Amendment does not require probable cause to believe

evidence will conclusively establish a fact before permitting a search,
but only “probable cause . . . to believe the evidence sought will aid in a
particular apprehension or conviction.” Warden, Md. Penitentiary v.
Hayden, 387 U. S. 294, 307 (1967) (emphasis added). Even if gang
evidence might have turned out not to be conclusive because other
16               MESSERSCHMIDT v. MILLENDER

                         Opinion of the Court

   Whatever the use to which evidence of Bowen’s gang
involvement might ultimately have been put, it would not
have been “entirely unreasonable” for an officer to believe
that the facts set out in the affidavit established a fair
probability that such evidence would aid the prosecution
of Bowen for the criminal acts at issue. Leon, 468 U. S., at
923 (internal quotation marks omitted).
                              B
   Whether any of these facts, standing alone or taken
together, actually establish probable cause is a question
we need not decide. Qualified immunity “gives govern-
ment officials breathing room to make reasonable but
mistaken judgments.” al-Kidd, 563 U. S., at ___ (slip op.,
at 12). The officers’ judgment that the scope of the war-
rant was supported by probable cause may have been
mistaken, but it was not “plainly incompetent.” Malley,
475 U. S., at 341.
   On top of all this, the fact that the officers sought and
obtained approval of the warrant application from a supe-
rior and a deputy district attorney before submitting it to
the magistrate provides further support for the conclusion
that an officer could reasonably have believed that the
scope of the warrant was supported by probable cause.
Ibid. Before seeking to have the warrant issued by a
magistrate, Messerschmidt conducted an extensive inves-
tigation into Bowen’s background and the facts of the
crime. Based on this investigation, Messerschmidt pre-
pared a detailed warrant application that truthfully laid
——————
members of the Millender household also had gang ties, see post, at 8
(opinion of SOTOMAYOR, J.); post, at 2–3 (opinion of KAGAN, J.), a rea-
sonable officer could still conclude that evidence of gang membership
would help show Bowen’s connection to the residence. Such evidence
could, for example, have displayed Bowen’s gang moniker (“C Jay”)
or could have been identified by Kelly as belonging to Bowen. See
App. 64.
                 Cite as: 565 U. S. ____ (2012)           17

                     Opinion of the Court

out the pertinent facts. The only facts omitted—the offi-
cers’ knowledge of Bowen’s arrest and conviction records,
see supra, at 3—would only have strengthened the war-
rant. Messerschmidt then submitted the warrant applica-
tion for review by Lawrence, another superior officer, and
a deputy district attorney, all of whom approved the appli-
cation without any apparent misgivings. Only after this
did Messerschmidt seek the approval of a neutral magis-
trate, who issued the requested warrant. The officers thus
“took every step that could reasonably be expected of
them.” Massachusetts v. Sheppard, 468 U. S. 981, 989
(1984). In light of the foregoing, it cannot be said that “no
officer of reasonable competence would have requested the
warrant.” Malley, 475 U. S., at 346, n. 9. Indeed, a con-
trary conclusion would mean not only that Messerschmidt
and Lawrence were “plainly incompetent,” id., at 341, but
that their supervisor, the deputy district attorney, and the
magistrate were as well.
   The Court of Appeals, however, gave no weight to the
fact that the warrant had been reviewed and approved
by the officers’ superiors, a deputy district attorney, and a
neutral magistrate. Relying on Malley, the court held that
the officers had an “independent responsibility to ensure
there [was] at least a colorable argument for probable
cause.” 620 F. 3d, at 1034. It explained that “[t]he depu-
ties here had a responsibility to exercise their reasonable
professional judgment,” and that “in circumstances such
as these a neutral magistrate’s approval (and, a fortiori,
a non-neutral prosecutor’s) cannot absolve an officer of
liability.” Ibid. (citation omitted).
   We rejected in Malley the contention that an officer is
automatically entitled to qualified immunity for seeking a
warrant unsupported by probable cause, simply because
a magistrate had approved the application. 475 U. S., at
345. And because the officers’ superior and the deputy
district attorney are part of the prosecution team, their
18            MESSERSCHMIDT v. MILLENDER

                     Opinion of the Court

review also cannot be regarded as dispositive. But by
holding in Malley that a magistrate’s approval does not
automatically render an officer’s conduct reasonable, we
did not suggest that approval by a magistrate or review
by others is irrelevant to the objective reasonableness of
the officers’ determination that the warrant was valid.
Indeed, we expressly noted that we were not deciding
“whether [the officer’s] conduct in [that] case was in fact
objectively reasonable.” Id., at 345, n. 8. The fact that the
officers secured these approvals is certainly pertinent in
assessing whether they could have held a reasonable belief
that the warrant was supported by probable cause.
                             C
    In holding that the warrant in this case was so obvious-
ly defective that no reasonable officer could have believed
it was valid, the court below relied heavily on our decision
in Groh v. Ramirez, 540 U. S. 551 (2004), but that prece-
dent is far afield. There, we held that officers who carried
out a warrant-approved search were not entitled to quali-
fied immunity because the warrant in question failed to
describe the items to be seized at all. Id., at 557. We
explained that “[i]n the portion of the form that called for
a description of the ‘person or property’ to be seized, [the
applicant] typed a description of [the target’s] two-story
blue house rather than the alleged stockpile of firearms.”
Id., at 554. Thus, the warrant stated nonsensically that
“ ‘there is now concealed [on the specified premises] a
certain person or property, namely [a] single dwelling
residence two story in height which is blue in color and
has two additions attached to the east.’ ” Id., at 554–555,
n. 2 (bracketed material in original). Because “even a
cursory reading of the warrant in [that] case—perhaps
just a simple glance—would have revealed a glaring de-
ficiency that any reasonable police officer would have
known was constitutionally fatal,” id., at 564, we held that
                 Cite as: 565 U. S. ____ (2012)          19

                     Opinion of the Court

the officer was not entitled to qualified immunity.
   The instant case is not remotely similar. In contrast to
Groh, any defect here would not have been obvious from
the face of the warrant. Rather, any arguable defect
would have become apparent only upon a close parsing of
the warrant application, and a comparison of the affidavit
to the terms of the warrant to determine whether the
affidavit established probable cause to search for all the
items listed in the warrant. This is not an error that
“just a simple glance” would have revealed. Ibid. Indeed,
unlike in Groh, the officers here did not merely submit
their application to a magistrate. They also presented it
for review by a superior officer, and a deputy district
attorney, before submitting it to the magistrate. The fact
that none of the officials who reviewed the application
expressed concern about its validity demonstrates that
any error was not obvious. Groh plainly does not control
the result here.
                        *    *     *
  The question in this case is not whether the magistrate
erred in believing there was sufficient probable cause to
support the scope of the warrant he issued. It is instead
whether the magistrate so obviously erred that any rea-
sonable officer would have recognized the error. The
occasions on which this standard will be met may be rare,
but so too are the circumstances in which it will be appro-
priate to impose personal liability on a lay officer in the
face of judicial approval of his actions. Even if the war-
rant in this case were invalid, it was not so obviously
lacking in probable cause that the officers can be con-
sidered “plainly incompetent” for concluding otherwise.
Malley, supra, at 341. The judgment of the Court of Ap-
peals denying the officers qualified immunity must there-
fore be reversed.
                                           It is so ordered.
                  Cite as: 565 U. S. ____ (2012)            1

                     BREYER, J., concurring

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 10–704
                          _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                      [February 22, 2012]


   JUSTICE BREYER, concurring.
   The Court concludes that the officers acted reasonably
in searching the house for “ ‘all firearms and firearm-
related items.’ ” Ante, at 11–12 (emphasis deleted). In
support of this conclusion, it cites two sets of circum-
stances. First, the majority points to “Bowen’s possession
of one illegal gun, his gang membership, his willingness to
use the gun to kill someone, and his concern about the
police . . . .” Ante, at 11. Second, the majority notes that
“[a] reasonable officer also could believe that seizure of the
firearms was necessary to prevent further assaults on
Kelly,” because “Bowen had already attempted to murder
Kelly once with a firearm, and had yelled ‘I’ll kill you’ as
she tried to escape from him.” Ante, at 12. In my view,
given all these circumstances together, the officers could
reasonably have believed that the scope of their search
was supported by probable cause. On that basis, I concur.
                 Cite as: 565 U. S. ____ (2012)           1

                     Opinion of KAGAN, J.

SUPREME COURT OF THE UNITED STATES
                         _________________

                          No. 10–704
                         _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                     [February 22, 2012]


   JUSTICE KAGAN, concurring in part and dissenting in
part.
   Both the Court and the dissent view this case as an
all-or-nothing affair: The Court awards immunity across
the board to Messerschmidt and his colleagues, while the
dissent would grant them none at all. I think the right
answer lies in between, although the Court makes the
more far-reaching error.
   I agree with the Court that a reasonably competent
police officer could have thought this warrant valid in
authorizing a search for all firearms and related items.
See ante, at 11–12. The warrant application recounted
that a known gang member had used a sawed-off shot-
gun—an illegal weapon under California law, see Cal.
Penal Code Ann. §33215 (West 2012 Cum. Supp.)—to try
to kill another person. See App. 56–57, 59. Perhaps gang
ties plus possession of an unlawful gun plus use of that
gun to commit a violent assault do not add up to what was
needed for this search: probable cause to believe that
Bowen had additional illegal firearms (or legal firearms
that he intended to use to violate the law) at the place he
was staying. But because our and the Ninth Circuit’s
decisions leave that conclusion debatable, a reasonable
2             MESSERSCHMIDT v. MILLENDER

                     Opinion of KAGAN, J.

police officer could have found the warrant adequately
supported by “indicia of probable cause.” Malley v. Briggs,
475 U. S. 335, 345 (1986). So Messerschmidt and his
fellow officers should receive qualified immunity for their
search for firearms.
   The Court, however, goes astray when it holds that a
reasonable officer could have thought the warrant valid in
approving a search for evidence of “street gang member-
ship,” App. 52. Membership in even the worst gang does
not violate California law, so the officers could not search
for gang paraphernalia just to establish Bowen’s ties to
the Crips. Instead, the police needed probable cause to
believe that such items would provide evidence of an
actual crime—and as the Court acknowledges, see ante, at
12–14, the only crime mentioned in the warrant applica-
tion was the assault on Kelly. The problem for the Court
is that nothing in the application supports a link between
Bowen’s gang membership and that shooting. Contra the
Court’s elaborate theory-spinning, see ante, at 12–16,
Messerschmidt’s affidavit in fact characterized the violent
assault only as a domestic dispute, not as a gang-related
one, see App. 55 (describing the crime as a “spousal as-
sault and an assault with a deadly weapon”). And that
description is consistent with the most natural under-
standing of the events. The warrant application thus had
a hole at its very center: It lacked any explanation of how
gang items would (or even might) provide evidence of the
domestic assault the police were investigating.
   To fill this vacuum, the Court proposes an alternative,
but similarly inadequate justification—that gang para-
phernalia could have demonstrated Bowen’s connection to
the Millender residence and to any evidence of the assault
found there. The dissent rightly notes one difficulty with
this argument: The discovery of gang items would not
have established that Bowen was staying at the house,
given that several other gang members regularly did so.
                  Cite as: 565 U. S. ____ (2012)             3

                      Opinion of KAGAN, J.

See post, at 8–9 (opinion of SOTOMAYOR, J.). And even
setting that issue aside, the Court’s reasoning proves far
too much: It would sanction equally well a search for any
of Bowen’s possessions on the premises—a result impos-
sible to square with the Fourth Amendment. See, e.g.,
Andresen v. Maryland, 427 U. S. 463, 480 (1976) (disap-
proving “ ‘a general, exploratory rummaging in a person’s
belongings’ ” (quoting Coolidge v. New Hampshire, 403
U. S. 443, 467 (1971))). In authorizing a search for all
gang-related items, the warrant far outstripped the offic-
ers’ probable cause. Because a reasonable officer would
have recognized that defect, I would not award qualified
immunity to Messerschmidt and his colleagues for this
aspect of their search.
  Still more fundamentally, the Court errs in scolding the
Court of Appeals for failing to give “weight to the fact that
the warrant had been reviewed and approved by the offic-
ers’ superiors, a deputy district attorney, and a neutral
magistrate.” Ante, at 17. As the dissent points out,
see post, at 13–15, this Court’s holding in Malley is to
the opposite effect: An officer is not “entitled to rely on the
judgment of a judicial officer in finding that probable
cause exists and hence issuing the warrant.” 475 U. S., at
345. Malley made clear that qualified immunity turned
on the officer’s own “professional judgment,” considered
separately from the mistake of the magistrate. Id., at 346;
see ibid., n. 9 (“The officer . . . cannot excuse his own
default by pointing to the greater incompetence of the
magistrate”); id., at 350 (Powell, J., concurring in part and
dissenting in part) (objecting to the Court’s decision to
“give little evidentiary weight to the finding of probable
cause by a magistrate”). And what we said in Malley
about a magistrate’s authorization applies still more
strongly to the approval of other police officers or state
attorneys. All those individuals, as the Court puts it, are
“part of the prosecution team.” Ante, at 18. To make their
4             MESSERSCHMIDT v. MILLENDER

                    Opinion of KAGAN, J.

views relevant is to enable those teammates (whether
acting in good or bad faith) to confer immunity on each
other for unreasonable conduct—like applying for a war-
rant without anything resembling probable cause.
  For these reasons, I would reverse in part and affirm in
part the judgment of the Court of Appeals, and I would
remand this case for further proceedings.
                  Cite as: 565 U. S. ____ (2012)             1

                    SOTOMAYOR, J., dissenting

SUPREME COURT OF THE UNITED STATES
                          _________________

                           No. 10–704
                          _________________


  CURT MESSERSCHMIDT, ET AL., PETITIONERS v.

    BRENDA MILLENDER, AS EXECUTOR OF THE

       ESTATE OF AUGUSTA MILLENDER,

              DECEASED, ET AL. 

 ON WRIT OF CERTIORARI TO THE UNITED STATES COURT OF

            APPEALS FOR THE NINTH CIRCUIT

                      [February 22, 2012]


   JUSTICE SOTOMAYOR, with whom JUSTICE GINSBURG
joins, dissenting.
   The fundamental purpose of the Fourth Amendment’s
warrant clause is “to protect against all general searches.”
Go-Bart Importing Co. v. United States, 282 U. S. 344, 357
(1931). The Fourth Amendment was adopted specifically
in response to the Crown’s practice of using general war-
rants and writs of assistance to search “suspected places”
for evidence of smuggling, libel, or other crimes. Boyd v.
United States, 116 U. S. 616, 625–626 (1886). Early patri-
ots railed against these practices as “the worst instrument
of arbitrary power” and John Adams later claimed that
“the child Independence was born” from colonists’ opposi-
tion to their use. Id., at 625 (internal quotation marks
omitted).
   To prevent the issue of general warrants on “loose,
vague or doubtful bases of fact,” Go-Bart Importing Co.,
282 U. S., at 357, the Framers established the inviolable
principle that should resolve this case: “no Warrants shall
issue, but upon probable cause . . . and particularly de-
scribing the . . . things to be seized.” U. S. Const., Amdt. 4.
That is, the police must articulate an adequate reason to
search for specific items related to specific crimes.
2              MESSERSCHMIDT v. MILLENDER

                    SOTOMAYOR, J., dissenting

    In this case, police officers investigating a specific, non-
gang-related assault committed with a specific firearm (a
sawed-off shotgun) obtained a warrant to search for all
evidence related to “any Street Gang,” “[a]ny photographs
. . . which may depict evidence of criminal activity,” and
“any firearms.” App. 52. They did so for the asserted
reason that the search might lead to evidence related to
other gang members and other criminal activity, and that
other “[v]alid warrants commonly allow police to search
for ‘firearms and ammunition.’ ” See infra, at 8–9. That
kind of general warrant is antithetical to the Fourth
Amendment.
    The Court nonetheless concludes that the officers are
entitled to qualified immunity because their conduct was
“objectively reasonable.” I could not disagree more. All
13 federal judges who previously considered this case
had little difficulty concluding that the police officers’
search for any gang-related material violated the Fourth
Amendment. See App. to Pet. for Cert. 28–29, 45, n. 7,
73, 94, 157–158. And a substantial majority agreed that
the police’s search for both gang-related material and all
firearms not only violated the Fourth Amendment, but
was objectively unreasonable. Like them, I believe that
any “reasonably well-trained officer in petitioner’s position
would have known that his affidavit failed to establish
probable cause.” Malley v. Briggs, 475 U. S. 335, 345
(1986).
    The Court also hints that a police officer’s otherwise
unreasonable conduct may be excused by the approval of
a magistrate, or more disturbingly, another police officer.
Ante, at 16–18. That is inconsistent with our focus on the
objective reasonableness of an officer’s decision to submit
a warrant application to a magistrate, and we long ago
rejected it. See Malley, 475 U. S., at 345–346.
    The Court’s analysis bears little relationship to the
record in this case, our precedents, or the purposes under-
                     Cite as: 565 U. S. ____ (2012)                    3

                       SOTOMAYOR, J., dissenting

lying qualified immunity analysis. For all these reasons,
I respectfully dissent.
                             I
   The Court holds that a well-trained officer could have
reasonably concluded that there was probable cause to
search the Millenders’ residence for any evidence of affilia-
tion with “any Street Gang,” and “all handguns, rifles, or
shotguns of any caliber, or any firearms capable of firing
ammunition.” App. 52.1 I cannot agree.
                              A
   Most troubling is the Court’s determination that peti-
tioners reasonably could have concluded that they had
probable cause to search for all evidence of any gang affili-
ation in the Millenders’ home. The Court reaches this
result only by way of an unprecedented, post hoc recon-
struction of the crime that wholly ignores the police’s own
conclusions, as well as the undisputed facts presented to
the District Court.
   The Court primarily theorizes that “[a] reasonable of-
ficer could certainly view Bowen’s attack as motivated
not by the souring of his romantic relationship with Kelly
but instead by a desire to prevent her from disclosing
details of his gang activity to the police.” Ante, at 13. The
majority therefore dismisses as “misleading” the Millen-
ders’ characterization of the case as a “domestic dispute,”
insisting that Detective Messerschmidt could have rea-
sonably thought that the crime was gang related. See
ante, at 13–14.2
——————
  1 Not even the Court defends the warrant’s authorization to search for

“[a]ny photographs . . . which may depict evidence of criminal activity.”
  2 The Court implies Detective Messerschmidt did not consider the

crime “solely . . . a domestic dispute” because he labeled it a “spousal
assault and an assault with a deadly weapon.” Ante, at 13 (internal
quotation marks omitted). Solely domestic disputes often involve gun
violence, however. See Sorenson & Weibe, Weapons in the Lives of
4                MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

  The police flatly rejected that hypothesis, however, con-
cluding that the crime was a domestic dispute that was
not in any way gang related. Detective Messerschmidt’s
deposition is illustrative.
     “Q: So as far as you knew, it was just sort of a spousal-
     abuse-type case where the perpetrator happened to be
     in a gang, right?
     “A: Correct.
     “Q: So you didn’t have any reason to believe that the
     assault on Kelly was any sort of gang crime, did you?
     “A: No.” Record in No. CV 05–2298 DDP (RZx) (CD
     Cal.) (hereinafter Record), Doc. 51, (Exh. X), p. 120
     (hereinafter Deposition).3
The “Crime Analysis” forms prepared by the police like-
——————
Battered Women, 94 Am. J. Pub. Health 1412, 1413 (2004) (noting
more than one-third of female domestic violence shelter residents in
California reported having been threatened or harmed with a firearm).
That was the case here. In any event, the Court’s reading of Detective
Messerschmidt’s affidavit is incompatible with his testimony that the
crime was “just sort of a spousal-abuse-type case,” not a “gang crime.”
See supra this page.
  3 By suggesting that courts assessing qualified immunity should ig-

nore police officers’ testimony about the information they possessed at
the time of the search, ante, at 14–15, n. 6, the Court misreads Harlow
v. Fitzgerald, 457 U. S. 800, 815–819 (1982), and Anderson v.
Creighton, 483 U. S. 635, 645 (1987). In Harlow, we adopted a qualified
immunity test focusing on an officer’s objective good faith, rather than
whether the officer searched “with the malicious intention to cause a
deprivation of constitutional rights or other injury.” 457 U. S., at 815.
As we have explained, “examination of the information possessed by the
searching officials . . . does not reintroduce into qualified immunity
analysis the inquiry into officials’ subjective intent that Harlow sought
to minimize.” Anderson, 483 U. S., at 641. It is therefore highly
relevant that Detective Messerschmidt testified that he lacked “any
reason” to consider the crime gang related, supra this page, and pos-
sessed no “information” that there were handguns in the Millenders’
home, infra, at 11. Courts cannot ignore information in crime analysis
forms, ballistic reports, or victim interviews by labeling such infor-
mation “conclusions.”
                      Cite as: 565 U. S. ____ (2012)                     5

                       SOTOMAYOR, J., dissenting

wise identified Bowen as a “Mona Park Crip” gang mem-
ber, but did not check off “gang-related” as a motive for the
attack. See App. 41, 44 (Crime Analysis Supplemental
Form–M. O. Factors). And the District Court noted it was
undisputed that Detective Messerschmidt “had no reason
to believe Bowen’s crime was a ‘gang’ crime.” App. to Pet.
for Cert. 115.4
   The police’s conclusions matched the victim’s own ac-
count of the attack. Kelly asked police officers to help her
move out because Bowen “ha[d] a domestic violence on his
record,” had “hit [her] once or twice” already, had repeat-
edly threatened her “You’ll never leave me. I’ll kill you
if you leave me,” and she was “planning on breaking up”
with him. Record, Doc. 51 (Exh. C), pp. 5–6 (hereinafter
Kelly Interview). As Kelly described the confrontation, it
was only after she fled to her car in order to leave that
Bowen reemerged from their shared apartment with the
shotgun and told her “I’m gonna kill your ass right here if
you take off,” consistent with his prior threats. Id., at 7–8.
Every piece of information, therefore, accorded with Detec-
tive Messerschmidt’s conclusion: The crime was domestic
violence that was not gang related.5
——————
   4 The Court is wrong to imply that courts should not consider “facts

outside the affidavit,” but within the officers’ possession, when as-
sessing qualified immunity. Ante, at 10, n. 2. Our precedents make
clear that the objective reasonableness of an officer’s conduct is judged
“in light of clearly established law and the information the officers
possessed.” Wilson v. Layne, 526 U. S. 603, 615 (1999). If an officer
possesses information indicating that he lacks probable cause to search,
and that information was not presented to the neutral magistrate when
he approved the search, it is particularly likely that “a reasonably well
trained officer would have known that the search was illegal despite
the magistrate’s authorization.” United States v. Leon, 468 U. S. 897,
922, n. 23 (1984).
   5 To support its theory that Bowen attacked Kelly to keep her silent

about his gang activity, the majority relies principally on its claim that
Bowen yelled, “ ‘I told you never to call the cops on me bitch!’ ” ante, at
2, citing it no less than five times. See, ante, at 11 (Bowen “attempt[ed]
6                MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

   Unlike the Members of this Court, Detective Messer-
schmidt alone had 14 years of experience as a peace of-
ficer, “hundreds of hours of instruction on the dynamics of
gangs and gang trends,” received “specialized training in
the field of gang related crimes,” and had been “involved
in hundreds of gang related incidents, contacts, and or
arrests.” App. 53–54. The Court provides no justification
for sweeping aside the conclusions he reached on the basis
of his far greater expertise, let alone the facts found by the
District Court. We have repeatedly and recently warned
appellate courts, “far removed from the scene,” against
second-guessing the judgments made by the police or
reweighing the facts as they stood before the district court.
Ryburn v. Huff, 565 U. S. —, — (2012) (per curiam) (slip
op., at 6–8). The majority’s decision today is totally incon-
sistent with those principles.
   Qualified immunity analysis does not direct courts to
play the role of crime scene investigators, second-guessing
police officers’ determinations as to whether a crime was
committed with a handgun or a shotgun, or whether vio-
——————
to murder” Kelly “on the asserted ground that she had ‘call[ed] the cops’
on him”); see also ante, at 1, 13. Bowen, however, never made that
statement. Though it appears in the warrant application, the words
are Messerschmidt’s—taken from his own inaccurate notes of Kelly’s
account of the crime. What Kelly actually said during her interview
was that as soon as the police deputies left, Bowen “came out of no-
where talking about, ‘Did you call the police on me? You called the
police on me,’ ” to which Kelly responded “no one called the police on
you . . . . [I]nstead of arguing and fighting with you I just want to get
my shit done.” Kelly Interview 7; compare ibid. with Record, Doc. 51
(Exh. B), p. 3 (Messerschmidt’s narrative of interview with Kelly). Only
after Kelly started to leave did Bowen exclaim “oh it’s like that. It’s
like that,” retrieve a gun, and threaten to shoot her if she left. Kelly
Interview 7–8. That Bowen was “ ‘angry,’ ” ante, at 14, n. 5, because she
had called the sheriff's department for assistance reflected exactly what
Kelly and the police expected at the outset—that Bowen “would give
her a hard time about moving out.” App. 38 (sheriff’s department
incident report).
                 Cite as: 565 U. S. ____ (2012)           7

                   SOTOMAYOR, J., dissenting

lence was gang related or a domestic dispute. Indeed,
we have warned courts against asking “whether another
reasonable, or more reasonable, interpretation of the
events can be constructed five years after the fact.”
Hunter v. Bryant, 502 U. S. 224, 228 (1991) (per curiam).
The inquiry our precedents demand is not whether differ-
ent conclusions might conceivably be drawn from the
crime scene. Rather, it is whether “a reasonably well-
trained officer in petitioner’s position would have known
that his affidavit failed to establish probable cause.”
Malley, 475 U. S., at 345. The operative question in this
case, therefore, is whether—given that, as petitioners
comprehended, the crime itself was not gang related—a
reasonable officer nonetheless could have believed he had
probable cause to seek a warrant to search the suspect’s
residence for all evidence of affiliation not only with the
suspect’s street gang, but “any Street Gang.” He could
not.
  The Court offers two secondary explanations for why a
search for gang-related items might have been justified,
but they are equally unpersuasive. First, the majority
suggests that such evidence hypothetically “might prove
helpful in impeaching Bowen or rebutting various de-
fenses he could raise at trial.” Ante, at 15. That is a non-
starter. The Fourth Amendment does not permit the police
to search for evidence solely because it could be admissible
for impeachment or rebuttal purposes. If it did, the police
would be equally entitled to obtain warrants to rifle
through the papers of anyone reasonably suspected of a
crime for all evidence of his bad character, Fed. Rule Evid.
404(a)(2)(B)(i), or any evidence of any “crime, wrong, or
other act” that might prove the defendant’s “motive, op-
portunity, intent, preparation, plan, knowledge, identity,
absence of mistake, or lack of accident,” Fed. Rule Evid.
404(b)(2). Indeed, the majority’s rationale presumably
would authorize the police to search the residence of every
8               MESSERSCHMIDT v. MILLENDER

                      SOTOMAYOR, J., dissenting

member of Bowen’s street gang for similar weapons—
which likewise “might [have] prove[d] helpful in impeach-
ing Bowen or rebutting various defenses he could raise at
trial.” Ante, at 15. It has long been the case, however,
that such general searches, detached from probable cause,
are impermissible. See, e.g., Go-Bart Importing Co., 282
U. S., at 357. By their own admission, however, the offic-
ers were not searching for gang-related indicia to bolster
some hypothetical impeachment theory, but for other
reasons: because “photos sought re gang membership
could be linked with other gang members, evidencing
criminal activity as gang affiliation is an enhancement to
criminal charges.” App. 181; see also id., at 145. That
kind of fishing expedition for evidence of unidentified
criminal activity committed by unspecified persons was
the very evil the Fourth Amendment was intended to
prevent.
   Finally, the Court concludes that “even if this were
merely a domestic dispute, a reasonable officer could still
conclude that gang paraphernalia found at the Millenders’
residence would aid in the prosecution of Bowen by, for
example, demonstrating Bowen’s connection to other
[unspecified] evidence found there.” Ante, at 15. That is
difficult to understand. The police were well aware before
obtaining a warrant that “other persons associated with
the home, the Millender family members, were active
Mona Park Crip gang members.” App. 28. Simply finding
gang-related paraphernalia, therefore, would have done
little to establish probable cause that particular evidence
found in the home was connected to Bowen, rather than
any of the several other active gang members who resided
full time at the Millender home.6 Moreover, it would have
——————
  6 The Court suggests that even if gang-related evidence would be

inconclusive generally, evidence bearing Bowen’s particular gang mon-
iker could have demonstrated Bowen’s connection to the residence.
                     Cite as: 565 U. S. ____ (2012)                     9

                       SOTOMAYOR, J., dissenting

done nothing to establish that Bowen had committed the
non-gang-related crime specified in the warrant.7
                              B
   The Court also errs by concluding that petitioners could
have reasonably concluded that they had probable cause
to search for all firearms. Notably absent from the Court’s
discussion is any acknowledgment of the actual basis for
petitioners’ search. The police officers searched for all
firearms not for the reasons hypothesized by the majority,
but because they determined that “[v]alid warrants com-
monly allow police to search for ‘firearms and ammuni-
tion,’ ” and that “[h]ere, any caliber of shotgun or receipts
would show possession of and/or purchase of guns.” Id., at
144, 180–181; see also Brief for Appellant in No. 07–55518
(CA9), p. 41 (hereinafter CA9 Brief). It is small wonder
that the District Court found these arguments “nonsensi-
cal and unpersuasive.” App. to Pet. for Cert. 157. It bears
repeating that the Founders adopted the Fourth Amend-
ment to protect against searches for evidence of unspeci-
fied crimes. And merely possessing other firearms is not a
crime at all. See generally District of Columbia v. Heller,
554 U. S. 570 (2008).8
——————
But the warrant did not authorize a search for items bearing Bowen’s
moniker, but rather for items related to “any Street Gang,” including
countless street gangs of which Bowen was not a member. App. 52.
Even under the Court’s interpretation, therefore, the warrant was
hopelessly overbroad and invalid.
  7 The police also could not search for gang-related evidence for its own

sake. Mere membership in a gang is not a crime under California law.
See People v. Gardeley, 14 Cal. 4th 605, 623, 927 P. 2d 713, 725 (1996).
  8 Although the Court recites additional facts about Bowen’s back-

ground and arrest record, ante, at 2–3, none of these facts were dis-
closed to the magistrate. The police cannot rationalize a search post
hoc on the basis of information they failed to set forth in their warrant
application to a neutral magistrate. Rather, “[i]t is elementary that in
passing on the validity of a warrant, the reviewing court may consider
only information brought to the magistrate’s attention.” Aguilar v.
10               MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

   By justifying the officers’ actions on reasons of its own
invention, the Court ignores the reasons the officers actu-
ally gave, as well as the facts upon which this case was
decided below. The majority’s analysis—akin to a rational-
basis test—is thus far removed from what qualified
immunity analysis demands. Even if the police had
searched for the reasons the Court proposes, however, I
still would find it inappropriate to afford them qualified
immunity.
   The Court correctly recognizes that to satisfy the Fourth
Amendment the police were required to demonstrate
probable cause that (1) other firearms could be found at
the Millenders’ residence; and (2) such weapons were
illegal or were “ ‘possess[ed] . . . with the intent to use
them as a means of committing a public offense.’ ” Ante, at
12 (quoting Cal. Penal Code Ann. §1524(a)(3) (West
2011)). The warrant failed to establish either.
   The majority has little difficulty concluding that because
Bowen fired one firearm, it was reasonable for the police
to conclude not only that Bowen must have possessed
others, but that he must be storing these other weapons
at his 73-year-old former foster mother’s home.9 Again,
however, this is not what the police actually concluded, as
Detective Messerschmidt’s deposition makes clear.
     “Q: Did you have any reason to believe there would be

——————
Texas, 378 U. S. 108, 109, n. 1 (1964); see also United States v. Jacob-
sen, 466 U. S. 109, 112 (1984). Likewise, a police officer cannot obtain
qualified immunity for searching pursuant to a warrant by relying
upon facts outside that warrant, as evinced by Malley’s focus on
“whether a reasonably well-trained officer in petitioner’s position would
have known that his affidavit failed to establish probable cause.”
Malley v. Briggs, 475 U. S. 335, 345 (1986) (emphasis added).
  9 The majority ignores that Bowen retrieved the shotgun that he fired

from the apartment he shared with Kelly, not the Millenders’ home.
Kelly provided no indication that Bowen possessed other guns or that
he stored them at his former foster mother’s home.
                    Cite as: 565 U. S. ____ (2012)                  11

                      SOTOMAYOR, J., dissenting

     any automatic weapons in the house? 

     “A: No.

     “Q: Did you have any reason to believe there would be 

     any hand guns in the house? 

     “A: I wasn’t given information that there were.” Dep-
     osition 120.

   Undaunted, the majority finds that a well-trained officer
could have concluded on this information that he had
probable cause to search for “[a]ll hand guns, . . . [a]ll
caliber of ammunition, miscellaneous gun parts, gun
cleaning kits, holsters which could hold or have held any
caliber handgun being sought,” and “[a]ny receipts or
paperwork, showing the purchase, ownership, or posses-
sion of the handguns being sought.” App. 52. That is
puzzling. If any aspect of the Fourth Amendment is clear-
ly established, it is that the police cannot reasonably
search—even pursuant to a warrant—for items that they
do not have “any reason to believe” will be present. The
Court’s conclusion to the contrary simply reads the “prob-
able cause” requirement out of the Fourth Amendment.
   Even assuming that the police reasonably could have
concluded that Bowen possessed other guns and was
storing them at the Millenders’ home, I cannot agree that
the warrant provided probable cause to believe any weap-
on possessed in a home in which 10 persons regularly
lived—none of them the suspect in this case—was either
“contraband or evidence of a crime.” Ornelas v. United
States, 517 U. S. 690, 696 (1996). The warrant set forth no
specific facts or particularized explanation establishing
probable cause to believe that other guns found in the
home were connected to the crime specified in the warrant
or were otherwise illegal.10 While the Court hypothesizes
——————
  10 Augusta Millender was a 73-year-old grandmother living in a dan-

gerous part of Los Angeles. It would not have been unreasonable to
imagine that she validly possessed a weapon for self-defense, as turned
12                MESSERSCHMIDT v. MILLENDER

                      SOTOMAYOR, J., dissenting

that the police could have searched for all firearms to
uncover evidence of yet unnamed crimes, ante, at 11–12,
the warrant specified that the police were investigating
one particular crime—“an assault with a deadly weapon.”
App. 55. And the police officers confirmed that their
search was targeted to find the gun related to “the crime
at issue.” CA9 Brief 42; see also App. 52 (obtaining au-
thorization to search for “the item being sought and or
believed to be evidence in the case being investigated on
this warrant” (emphasis added)).
   The police told the Ninth Circuit that they searched for
all firearms not because, as the majority hypothesizes,
“there would be additional illegal guns among others that
Bowen owned,” ante, at 11–12, but on the dubious theory
that “Kelly could have been mistaken in her description of
the gun.” App. to Pet. for Cert. 20–21. The Ninth Circuit
properly dismissed that argument as carrying “little
force.” Id., at 21. Its finding is unimpeachable, given that
Kelly presented the police with a photograph of Bowen
holding the specific gun used in the crime, and the police,
the victim, and a witness to the crime all identified the
gun as a sawed-off shotgun. See id., at 20, 21, 24, 28.
   Finally, the majority suggests that the officers could
have reasonably believed that seizure of all firearms at the
Millenders’ residence was justified because those weapons
might be possessed by Bowen “ ‘with the intent to use
them as a means of committing a public offense.’ ” Ante, at
12. But the warrant specified that the police sought only
the shotgun used in this crime for that purpose. See App.
59 (statement of probable cause) (“Your Affiant also be-
lieves that the items sought will be in the possession of
Jerry Ray Bowen and the recovery of the weapon could be
invaluable in the successful prosecution of the suspect
involved in this case, and the curtailment of further
——————
out to be the case.
                     Cite as: 565 U. S. ____ (2012)                    13

                       SOTOMAYOR, J., dissenting

crimes being committed” (emphasis added)).
                               II
  The Court also finds error in the Court of Appeals’
failure to find “pertinent” the fact that the officer sought
approval of his warrant from a magistrate.11 Ante, at 18.
Whether Detective Messerschmidt presented his warrant
application to a magistrate surely would be “pertinent” to
demonstrating his subjective good faith.12 But qualified
immunity does not turn on whether an officer is motivated
by good intentions or malice, but rather on the “objective
reasonableness of an official’s conduct.” Harlow v. Fitz-
gerald, 457 U. S. 800, 818 (1982).
  The majority asserts, without citation, that the magis-
trate’s approval is relevant to objective reasonableness.
That view, however, is expressly contradicted by our hold-
ing in Malley v. Briggs, 475 U. S. 335. There, we found
that a police officer is not “entitled to rely on the judgment
of a judicial officer in finding that probable cause exists
and hence issuing the warrant,” and explained that “[that]
view of objective reasonableness is at odds with our devel-
opment of that concept in Harlow and [United States v.
Leon, 468 U. S. 897 (1984)].” Id., at 345. The appropriate
qualified immunity analysis, we held, was not whether an

——————
   11 Under California law, magistrates are the officials responsible for

issuing search warrants. Cal. Penal Code Ann. §1523 (West 2011).
   12 To be clear, no one suggests petitioners acted with malice or in-

tended to be “misleading in omitting . . . facts,” ante, at 10, n. 2, that
illustrate why it would have been objectively unreasonable to search for
the reasons the Court proposes. It is hardly surprising, for instance,
that Detective Messerschmidt did not include in his affidavit further
facts affirming that the crime was not gang related, given that he did
not believe the crime was gang related and did not search for gang-
related material for that reason. See supra, at 7–8. The affidavit and
warrant were perfectly consistent with the officers’ stated reasons for
their search—just not with the Court’s own theories.
14               MESSERSCHMIDT v. MILLENDER

                       SOTOMAYOR, J., dissenting

officer reasonably relied on a magistrate’s probable cause
determination, but rather “whether a reasonably well-
trained officer in petitioner’s position would have known
that his affidavit failed to establish probable cause and
that he should not have applied for the warrant.” Ibid.
(emphasis added).13 In such a case, “the officer’s applica-
tion for a warrant [would] not [be] objectively reasonable,
because it create[s] the unnecessary danger of an unlawful
arrest.” Ibid. When “no officer of reasonable competence
would have requested the warrant,” a “magistrate [who]
issues the warrant [makes] not just a reasonable mistake,
but an unacceptable error indicating gross incompetence
or neglect of duty.” Id., at 346, n. 9. In such cases, “[t]he
officer . . . cannot excuse his own default by pointing to the
greater incompetence of the magistrate.” Ibid.
   In cases in which it would be not only wrong but un-
reasonable for any well-trained officer to seek a warrant,
allowing a magistrate’s approval to immunize the police
officer’s unreasonable action retrospectively makes little
sense. By motivating an officer “to reflect, before submit-
ting a request for a warrant, upon whether he has a rea-
sonable basis for believing that his affidavit establishes
probable cause,” we recognized that our qualified immu-
nity precedents had the “desirable” effect of “reduc[ing] the
likelihood that the officer’s request for a warrant will be
premature,” leading to “a waste of judicial resources” or
“premature arrests.” Id., at 343. To the extent it proposes
to cut back upon Malley, the majority will promote the
opposite result—encouraging sloppy police work and ex-
acerbating the risk that searches will not comport with
the requirements of the Fourth Amendment.

——————
  13 Two  Justices wrote separately, disagreeing with the majority be-
cause they believed that “substantial weight should be accorded the
judge’s finding of probable cause.” Malley, 475 U. S., at 346 (Powell, J.,
joined by Rehnquist, C. J., concurring in part and dissenting in part).
                     Cite as: 565 U. S. ____ (2012)                    15

                       SOTOMAYOR, J., dissenting

   The Court also makes much of the fact that Detective
Messerschmidt sent his proposed warrant application to
two superior police officers and a district attorney for
review. Giving weight to that fact would turn the Fourth
Amendment on its head. This Court made clear in Malley
that a police officer acting unreasonably cannot obtain
qualified immunity on the basis of a neutral magistrate’s
approval. It would be passing strange, therefore, to im-
munize an officer’s conduct instead based upon the ap-
proval of other police officers and prosecutors.14 See John-
son v. United States, 333 U. S. 10, 14 (1948) (opinion of
Jackson, J.) (“When the right of privacy must reasonably
yield to the right of search is, as a rule, to be decided by a
judicial officer, not by a policeman or government en-
forcement agent”). The effect of the Court’s rule, however,
is to hold blameless the “plainly incompetent” action of the
police officer seeking a warrant because of the “plainly
incompetent” approval of his superiors and the district
attorney. See ante, at 16–18; see also ante, at 3–4 (opinion
of KAGAN, J.). Under the majority’s test, four wrongs
apparently make a right. I cannot agree, however, that
the “objective legal reasonableness of an official’s acts,”
Harlow, 457 U. S., at 819, turns on the number of police
officers or prosecutors who improperly sanction a search
that violates the Fourth Amendment.
                             III
  Police officers perform a difficult and essential service to
society, frequently at substantial risk to their personal
——————
  14 In the famous case of Wilkes v. Wood, Lofft 1, 98 Eng. Rep. 489

(C. P. 1763), one of the seminal events informing the Framers’ development
of the Fourth Amendment, the Undersecretary of State who searched
the home of John Wilkes pursuant to a general warrant was subjected
to monetary damages notwithstanding that his superior, Lord Halifax,
issued the warrant. See Boyd v. United States, 116 U. S. 616, 626
(1886).
16             MESSERSCHMIDT v. MILLENDER

                   SOTOMAYOR, J., dissenting

safety. And criminals like Bowen are not sympathetic
figures. But the Fourth Amendment “protects all, those
suspected or known to be offenders as well as the inno-
cent.” Go-Bart Importing Co., 282 U. S., at 357. And this
Court long ago recognized that efforts “to bring the guilty
to punishment, praiseworthy as they are, are not to be
aided by the sacrifice of those great principles established
by years of endeavor and suffering which have resulted
in their embodiment in the fundamental law of the land.”
Weeks v. United States, 232 U. S. 383, 393 (1914).
   Qualified immunity properly affords police officers protec-
tion so long as their conduct is objectively reasonable.
But it is not objectively reasonable for police investi-
gating a specific, non-gang-related assault committed with
a particular firearm to search for all evidence related to
“any Street Gang,” “photographs . . . which may depict
evidence of criminal activity,” and all firearms. The Court
reaches a contrary result not because it thinks that these
police officers’ stated reasons for searching were objective-
ly reasonable, but because it thinks different conclusions
might be drawn from the crime scene that reasonably
might have led different officers to search for different
reasons. That analysis, however, is far removed from
qualified immunity’s proper focus on whether petitioners
acted in an objectively reasonable manner.
   Because petitioners did not, I would affirm the judgment
of the Court of Appeals.

```

---

## GROUP: content/cases/Michigan v. Chesternut.md  (`case`, 5 assertions)

### content_page

```
---
title: "Michigan v. Chesternut"
type: case
citation: "486 U.S. 567 (1988)"
parallel_cite: "108 S. Ct. 1975; 100 L. Ed. 2d 565; 56 U.S.L.W. 4558"
neutral_cite: 1988 U.S. LEXIS 2582
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1988
date_decided: 1988-06-13
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1988-06-13
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Chesternut
  varies_by_point: false
  scope_note: "Good law. Police pursuit, without more, is not a seizure; whether a seizure occurred is judged by the Mendenhall objective test (would a reasonable person have believed he was not free to leave). California v. Hodari D. (1991) later refined the show-of-authority branch to require submission."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/"
  cluster_id: 112095
  opinion_id: 9431339
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Progeny"
related: ["[[United States v. Mendenhall]]", "[[California v. Hodari D.]]", "[[Florida v. Bostick]]", "[[United States v. Knotts]]"]
aliases: []
tags: ["case", "fourth-amendment", "seizure", "pursuit", "free-to-leave", "abandonment"]
holding: "Police pursuit, standing alone, is not a Fourth Amendment seizure; whether police conduct is a seizure is determined by the Mendenhall objective test — whether, in all the circumstances, a reasonable person would have believed he was not free to leave."
lake:
  record_id: Michigan v. Chesternut
  status: verified
  projected_at: 2026-07-09
---

# Michigan v. Chesternut

*486 U.S. 567 (1988)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers in a patrol car on routine patrol saw Chesternut standing on a corner; when he saw the cruiser approach, he ran. The officers drove alongside him for a short distance "to see where he was going." They did not activate a siren or flashers, command him to halt, display weapons, or drive aggressively to block his path. As the cruiser drove parallel to him, Chesternut discarded several packets, which the officers retrieved and (believing them to be narcotics) seized; he was then arrested. He moved to suppress the packets as the fruit of an unlawful seizure.

## Issue
Whether the officers' pursuit — driving alongside a fleeing pedestrian — was a Fourth Amendment "seizure," such that the packets Chesternut discarded during the pursuit were the fruit of that seizure.

## Rule
Whether police conduct is a seizure is governed by the objective Mendenhall test: "The test provides that the police can be said to have seized an individual 'only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.'" — 486 U.S. at 573 (quoting *United States v. Mendenhall*). ^pin-573

"The test is necessarily imprecise, because it is designed to assess the coercive effect of police conduct, taken as a whole, rather than to focus on particular details of that conduct in isolation." — [*Id.*](https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/#:~:text=The%20test%20is%20necessarily%20imprecise%2C) ^pin-573b

Applying it, the Court held: "we conclude that respondent was not seized by the police before he discarded the packets containing the controlled substance." — [*Id.* at 574](https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/#:~:text=we%20conclude%20that%20respondent%20was). ^pin-574

## Application
Although an officer called the conduct a "chase," that label did not make it a seizure: "the police conduct involved here would not have communicated to the reasonable person an attempt to capture or otherwise intrude upon respondent's freedom of movement. The record does not reflect that the police activated a siren or flashers; or that they commanded respondent to halt, or displayed any weapons; or that they operated the car in an aggressive manner to block respondent's course or otherwise control the direction or speed of his movement." — *Id.* at 575. ^pin-575

"While the very presence of a police car driving parallel to a running pedestrian could be somewhat intimidating, this kind of police presence does not, standing alone, constitute a seizure." — [*Id.* at 575–576](https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/#:~:text=While%20the%20very%20presence%20of). ^pin-575b

Because Chesternut had not been seized when he abandoned the packets, they were not the fruit of any seizure.

## Conclusion
The pursuit was not a seizure under the Mendenhall test, so the abandoned packets were admissible; the judgment suppressing them was reversed. Police pursuit, without a show of authority that would make a reasonable person believe he was not free to leave, is not a Fourth Amendment seizure.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Chesternut* applies the [[United States v. Mendenhall]] "free to leave" test to pursuits. [[California v. Hodari D.]] (1991) later clarified that, when a seizure is asserted on a *show of authority*, no seizure occurs until the suspect submits — reinforcing that mere pursuit is not a seizure. Compare [[Florida v. Bostick]] (free-to-leave adapted to confined settings).

## Appears on
- [[Seizure of the Person]] — *Progeny*

## Sources
- *Michigan v. Chesternut*, 486 U.S. 567 (1988) — https://www.courtlistener.com/opinion/112095/michigan-v-chesternut/ — pinpoints: 573, 574, 575–576.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "59a228dcecd194ee", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "486 U.S. 567 (1988)", "court": "U.S. Supreme Court", "neutral_cite": "1988 U.S. LEXIS 2582", "official_citation_present": true, "parallel_cite": "108 S. Ct. 1975; 100 L. Ed. 2d 565; 56 U.S.L.W. 4558", "title": "Michigan v. Chesternut", "year": "1988"}}
{"assertion_id": "020c5ffaf1315dbf", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Police pursuit, standing alone, is not a Fourth Amendment seizure; whether police conduct is a seizure is determined by the Mendenhall objective test — whether, in all the circumstances, a reasonable person would have believed he was not free to leave.", "title": "Michigan v. Chesternut"}}
{"assertion_id": "d7d06b1b96c8bc39", "dimension": "support", "kind": "home_role", "locator": {"home": "Seizure of the Person"}, "payload": {"home": "Seizure of the Person", "role": "Progeny", "title": "Michigan v. Chesternut"}}
{"assertion_id": "ae050a9bb18aa6d2", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1988-06-13", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Chesternut", "field_i_validity": "good_law", "scope_note": "Good law. Police pursuit, without more, is not a seizure; whether a seizure occurred is judged by the Mendenhall objective test (would a reasonable person have believed he was not free to leave). California v. Hodari D. (1991) later refined the show-of-authority branch to require submission.", "title": "Michigan v. Chesternut", "varies_by_point": "false"}}
{"assertion_id": "e0162838144649bd", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Chesternut"}}
```

### lake record — Michigan v. Chesternut

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Chesternut",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Chesternut",
    "case_name_short": "Chesternut",
    "case_name_full": "Michigan v. Chesternut",
    "input_case_name": "Michigan v. Chesternut",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1988-06-13",
    "year": 1988,
    "docket": null,
    "cluster_id": 112095,
    "lead_opinion_id": 9431339,
    "sibling_ids": [
      112095,
      9431339,
      9431340
    ],
    "absolute_url": "/opinion/112095/michigan-v-chesternut/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "486 U.S. 567",
      "volume": "486",
      "reporter": "U.S.",
      "page": "567",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "108 S. Ct. 1975",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 565",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4558",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4558",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1988 U.S. LEXIS 2582",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2582",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "486 U.S. 567",
        "volume": "486",
        "reporter": "U.S.",
        "page": "567",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "108 S. Ct. 1975",
        "volume": "108",
        "reporter": "S. Ct.",
        "page": "1975",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "100 L. Ed. 2d 565",
        "volume": "100",
        "reporter": "L. Ed. 2d",
        "page": "565",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1988 U.S. LEXIS 2582",
        "volume": "1988",
        "reporter": "U.S. LEXIS",
        "page": "2582",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 U.S.L.W. 4558",
        "volume": "56",
        "reporter": "U.S.L.W.",
        "page": "4558",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "486 U.S. 567",
    "official_selection": {
      "court_class": "scotus",
      "selected": "486 U.S. 567",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-573",
      "page": null,
      "quote": "such that the packets Chesternut discarded during the pursuit were the fruit of that seizure. ## Rule Whether police conduct is a seizure is governed by the objective Mendenhall test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-573b",
      "page": null,
      "quote": "The test is necessarily imprecise, because it is designed to assess the coercive effect of police conduct, taken as a whole, rather than to focus on particular details of that conduct in isolation.",
      "star_marker": "573",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 11700,
      "fragment": "#:~:text=The%20test%20is%20necessarily%20imprecise%2C",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-574",
      "page": null,
      "quote": "we conclude that respondent was not seized by the police before he discarded the packets containing the controlled substance.",
      "star_marker": "574",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 13830,
      "fragment": "#:~:text=we%20conclude%20that%20respondent%20was",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-575",
      "page": null,
      "quote": "that label did not make it a seizure:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-575b",
      "page": null,
      "quote": "While the very presence of a police car driving parallel to a running pedestrian could be somewhat intimidating, this kind of police presence does not, standing alone, constitute a seizure.",
      "star_marker": "575",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14988,
      "fragment": "#:~:text=While%20the%20very%20presence%20of",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1988-06-13",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Chesternut",
    "varies_by_point": false,
    "scope_note": "Good law. Police pursuit, without more, is not a seizure; whether a seizure occurred is judged by the Mendenhall objective test (would a reasonable person have believed he was not free to leave). California v. Hodari D. (1991) later refined the show-of-authority branch to require submission.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Wright",
          "cluster_id": 10658752,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
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
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 10018647,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Reed",
          "cluster_id": 4731165,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Shane S., a juvenile",
          "cluster_id": 4429246,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Fields",
          "cluster_id": 3203547,
          "cite": [
            "823 F.3d 20",
            "2016 U.S. App. LEXIS 8834",
            "2016 WL 2821485"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
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
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Amy Lyons",
          "cluster_id": 3069968,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane1_negative"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harris v. Reed",
          "cluster_id": 112205,
          "cite": [
            "103 L. Ed. 2d 308",
            "109 S. Ct. 1038",
            "489 U.S. 255",
            "1989 U.S. LEXIS 1044",
            "57 U.S.L.W. 4224"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stansbury v. California",
          "cluster_id": 117843,
          "cite": [
            "128 L. Ed. 2d 293",
            "114 S. Ct. 1526",
            "511 U.S. 318",
            "1994 U.S. LEXIS 3293"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brendlin v. California",
          "cluster_id": 145712,
          "cite": [
            "168 L. Ed. 2d 132",
            "127 S. Ct. 2400",
            "551 U.S. 249",
            "2007 U.S. LEXIS 7897"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Georgia v. Randolph",
          "cluster_id": 145669,
          "cite": [
            "164 L. Ed. 2d 208",
            "126 S. Ct. 1515",
            "547 U.S. 103",
            "2006 U.S. LEXIS 2498"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Drayton",
          "cluster_id": 121153,
          "cite": [
            "153 L. Ed. 2d 242",
            "122 S. Ct. 2105",
            "536 U.S. 194",
            "2002 U.S. LEXIS 4420"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Garcia-Cantu",
          "cluster_id": 1769810,
          "cite": [
            "253 S.W.3d 236",
            "2008 Tex. Crim. App. LEXIS 581",
            "2008 WL 1958956"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lanman v. Hinson",
          "cluster_id": 1455879,
          "cite": [
            "529 F.3d 673",
            "2008 U.S. App. LEXIS 12682",
            "2008 WL 2415926"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Hollman",
          "cluster_id": 5690698,
          "cite": [
            "79 N.Y.2d 181"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Crain v. State",
          "cluster_id": 2353970,
          "cite": [
            "315 S.W.3d 43",
            "2010 Tex. Crim. App. LEXIS 794",
            "2010 WL 2595077"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Ehly",
          "cluster_id": 1448102,
          "cite": [
            "854 P.2d 421",
            "317 Or. 66",
            "1993 Ore. LEXIS 91"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Retherford",
          "cluster_id": 4001886,
          "cite": [
            "639 N.E.2d 498",
            "93 Ohio App. 3d 586",
            "1994 Ohio App. LEXIS 1066"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Luedemann",
          "cluster_id": 2008176,
          "cite": [
            "857 N.E.2d 187",
            "222 Ill. 2d 530",
            "306 Ill. Dec. 94",
            "2006 Ill. LEXIS 1641"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 1676406,
          "cite": [
            "912 S.W.2d 227",
            "1995 Tex. Crim. App. LEXIS 115",
            "1995 WL 675559"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kaupp v. Texas",
          "cluster_id": 127919,
          "cite": [
            "155 L. Ed. 2d 814",
            "123 S. Ct. 1843",
            "538 U.S. 626",
            "2003 U.S. LEXIS 3670"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Strickler",
          "cluster_id": 2156861,
          "cite": [
            "757 A.2d 884",
            "563 Pa. 47",
            "2000 Pa. LEXIS 2114"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Daniel",
          "cluster_id": 1060655,
          "cite": [
            "12 S.W.3d 420",
            "2000 Tenn. LEXIS 52",
            "2000 WL 100069"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Emil Ewolski v. City of Brunswick",
          "cluster_id": 777338,
          "cite": [
            "287 F.3d 492",
            "2002 U.S. App. LEXIS 7129",
            "2002 WL 571329"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
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
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sewn Newton",
          "cluster_id": 786350,
          "cite": [
            "369 F.3d 659",
            "2004 U.S. App. LEXIS 10343",
            "2004 WL 1161747"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Chesternut:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112095 OR 9431339 OR 9431340) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjYzNDI3MjAwMDAwJnM9MjI3MDg3NCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112095+OR+9431339+OR+9431340%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 8,
        "triage_snippet_classified": 192
      },
      "lane2_top_cited": {
        "query": "cites:(112095 OR 9431339 OR 9431340)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMjkmcz03MDIyOTcmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112095+OR+9431339+OR+9431340%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112095 OR 9431339 OR 9431340)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 1,
        "triage_snippet_classified": 22
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112095 OR 9431339 OR 9431340)",
    "indexed_citing_opinions": 919,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112095,
        "count": 826,
        "count_source": "search"
      },
      {
        "opinion_id": 9431339,
        "count": 107,
        "count_source": "search"
      },
      {
        "opinion_id": 9431340,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1501,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-chesternut.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgwNjEyMDQmcz05MzU0MDA2JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112095+OR+9431339+OR+9431340%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112095,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110882,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 110890,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 1243152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 1853429,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112095,
        "cited_id": 2189647,
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
    "date_created": "2026-07-05T13:12:47Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:13:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:13:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:17:01Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:13:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Chesternut

```
<opinion type="majority">
<author id="b627-4"><page-number citation-index="1" label="569">*569</page-number>Justice Blackmun</author>
<p id="A7l">delivered the opinion of the Court.</p>
<p id="b627-5">In this case we review a determination by the Michigan Court of Appeals that any “investigatory pursuit” of a person undertaken by the police necessarily constitutes a seizure under the Fourth Amendment of the Constitution. We conclude that the police conduct in this case did not amount to a seizure, for it would not have communicated to a reasonable person that he was not at liberty to ignore the police presence and go about his business.</p>
<p id="b627-6">I</p>
<p id="b627-7">Early on the afternoon of December 19, 1984, four officers riding in a marked police cruiser were engaged in routine patrol duties in Metropolitan Detroit. As the cruiser came to an intersection, one of the officers observed a car pull over to the curb. A man got out of the car and approached respondent Michael Mose Chesternut, who was standing alone on the corner. When respondent saw the patrol car nearing the comer where he stood, he turned and began to run. As Officer Peltier, one of those in the car, later testified, the patrol car followed respondent around the corner “to see where he was going.” App. 25. The cruiser quickly caught up with respondent and drove alongside him for a short distance. As they drove beside him, the officers observed respondent discard a number of packets he pulled from his right-hand pocket. Officer Peltier got out of the cruiser to examine the packets. He discovered that they contained pills. While Peltier was engaged in this inspection, respondent, who had run only a few paces farther, stopped. Surmising on the basis of his experience as a paramedic that the pills contained codeine, Officer Peltier arrested respondent for the possession of narcotics and took him to the station house. During an ensuing search, the police discovered in respondent’s hatband another packet of pills, a packet containing heroin, and a hypodermic needle. Respondent was charged with knowingly and intentionally possessing heroin, tablets <page-number citation-index="1" label="570">*570</page-number>containing codeine, and tablets containing diazepam, all in violation of <span class="citation no-link">Mich. Comp. Laws §333.7403</span>(2) (1980).</p>
<p id="b628-4">At a preliminary hearing, at. which Officer Peltier was the only witness, respondent moved to dismiss the charges on the ground that he had been unlawfully seized during the police pursuit preceding his disposal of the packets. The presiding Magistrate granted the motion and dismissed the complaint.<footnotemark>1</footnotemark> Relying on <em>People </em>v. <em>Terrell, </em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">77 Mich. App. 676</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">259 N. W. 2d 187</a></span> (1977),<footnotemark>2</footnotemark> the Magistrate ruled from the bench that a police “chase” like the one involved in this case implicated Fourth Amendment protections and could not be justified by the mere fact that the suspect ran at the sight of the police. App. 31-35. Applying a clearly-erroneous standard to the Magistrate’s ruling, the trial court upheld the dismissal order. <em>Id., </em>at 2-10.</p>
<p id="b628-5">The Michigan Court of Appeals “reluctantly” affirmed, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#184" aria-description="Citation for case: People v. Chesternut">157 Mich. App. 181, 184</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#76" aria-description="Citation for case: People v. Chesternut">403 N. W. 2d 74, 76</a></span> (1986), noting that “although we find the result unfortunate, we cannot say that the lower court’s ruling was clearly erroneous under the present law or the facts presented.” <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#183" aria-description="Citation for case: People v. Chesternut"><em>Id., </em>at 183</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#75" aria-description="Citation for case: People v. Chesternut">403 N. W. <page-number citation-index="1" label="571">*571</page-number>2d, at 75</a></span>. Like the courts below it, the Court of Appeals rested its ruling on state precedents interpreting the Fourth Amendment.<footnotemark>3</footnotemark> The court determined, first, that any “investigatory pursuit” amounts to a seizure under <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1</a></span> (1968). “As soon as the officers began their pursuit,” the court explained, “defendant’s freedom was restricted.” <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#183" aria-description="Citation for case: People v. Chesternut">157 Mich. App., at 183</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#75" aria-description="Citation for case: People v. Chesternut">403 N. W. 2d, at 75</a></span>. The court went on to conclude that respondent’s flight from the police was insufficient, by itself, to give rise to the particularized suspicion necessary to justify this kind of seizure. Because “the police saw [respondent] do absolutely nothing illegal nor did they observe other suspicious activity,” the court determined that the investigatory pursuit had violated the Fourth Amendment’s prohibition against unreasonable seizures. <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#184" aria-description="Citation for case: People v. Chesternut"><em>Id., </em>at 184</a></span>, <span class="citation" data-id="1853429"><a href="/opinion/1853429/people-v-chesternut/#76" aria-description="Citation for case: People v. Chesternut">403 N. W. 2d, at 76</a></span>.</p>
<p id="b630-7"><page-number citation-index="1" label="572">*572</page-number>After the Michigan Supreme Court denied petitioner leave to appeal,<footnotemark>4</footnotemark> App. to Pet. for Cert. 9a, petitioner sought review here. We granted a 'writ of certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./484/895/">484 U. S. 895</a></span> (1987), to consider whether the officers’ pursuit of respondent constituted a seizure implicating Fourth Amendment protections, and, if so, whether the act of fleeing, by itself, was sufficient to constitute reasonable suspicion justifying that seizure. Because we conclude that the officers’ conduct did not constitute a seizure, we need not reach the second question.</p>
<p id="b630-8">h — I i</p>
<p id="Aov">A</p>
<p id="AMQ3">Petitioner argues that the Fourth Amendment is never implicated until an individual stops in response to the police’s show of authority. Thus, petitioner would have us rule that a lack of objective and particularized suspicion would not poison police conduct, no matter how coercive, as long as the police did not succeed in actually apprehending the individual. Respondent contends, in sharp contrast, that any and all police “chases” are Fourth Amendment seizures. Respondent would have us rule that the police may never pursue an individual absent a particularized and objective basis for suspecting that he is engaged in criminal activity.</p>
<p id="AHX2">Both petitioner and respondent, it seems to us, in their attempts to fashion a bright-line rule applicable to all investigatory pursuits, have failed to heed this Court’s clear direction that any assessment as to whether police conduct amounts to a seizure implicating the Fourth Amendment must take into account “ ‘all of the circumstances surrounding the incident’ ” in each individual case. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984), quoting <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554</a></span> (1980) (opinion of Stewart, J.). Rather than adopting either rule proposed by the parties and determining that an investigatory pursuit is or is not <em>necessarily </em>a <page-number citation-index="1" label="573">*573</page-number>seizure under the Fourth Amendment, we adhere to our traditional contextual approach, and determine only that, in this particular case, the police conduct in question did not amount to a seizure.</p>
<p id="b631-5">B</p>
<p id="b631-6">In <em>Terry </em>v. <em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/" aria-description="Citation for case: Terry v. Ohio">Ohio</a></span>, </em>the Court noted:</p>
<blockquote id="b631-7">“Obviously, not all personal intercourse between policemen and citizens involves ‘seizures’ of persons. Only when the officer, by means of physical force or show of authority, has in some way restrained the liberty of a citizen may we conclude that a ‘seizure’ has occurred.” <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#19" aria-description="Citation for case: Terry v. Ohio">392 U. S., at 19, n. 16</a></span>.</blockquote>
<p id="b631-8">A decade later in <em>United States </em>v. <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall</a></span>, </em>Justice Stewart, writing for himself and then Justice Rehnquist, first transposed this analysis into a test to be applied in determining whether “a person has been ‘seized’ within the meaning of the Fourth Amendment.” <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 554</a></span>.<footnotemark>5</footnotemark> The test provides that the police can be said to have seized an individual “only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave.” <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Ibid.</a></span> </em>The Court has since embraced this test. See <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 215</a></span>. See also <em>Florida </em>v. <em>Royer, </em><span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#502" aria-description="Citation for case: Florida v. Royer">460 U. S. 491, 502</a></span> (1983) (plurality opinion); <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#514" aria-description="Citation for case: Florida v. Royer"><em>id., </em>at 514</a></span> (Blackmun, J., dissenting).</p>
<p id="b631-9">The test is necessarily imprecise, because it is designed to assess the coercive effect of police conduct, taken as a whole, rather than to focus on particular details of that conduct in isolation. Moreover, what constitutes a restraint on liberty prompting a person to conclude that he is not free to “leave” will vary, not only with the particular police conduct at issue, but also with the setting in which the conduct occurs. Compare <em>United States </em>v. <em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Mendenhall, supra</a></span> </em>(consid<page-number citation-index="1" label="574">*574</page-number>ering whether police request to see identification and ticket of individual who stopped upon police’s approach constituted seizure), with <em>INS </em>v. <em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">Delgado, supra</a></span> </em>(considering whether INS “factory survey” conducted while employees continued to move about constituted seizure of entire work force).</p>
<p id="b632-5">While the test is flexible enough to be applied to the whole range of police conduct in an equally broad range of settings, it calls for consistent application from one police encounter to the next, regardless of the particular individual’s response to the actions of the police. The test’s objective standard-looking to the reasonable man’s interpretation of the conduct in question — allows the police to determine in advance whether the conduct contemplated will implicate the Fourth Amendment. 3 W. LaFave, Search and Seizure § 9.2(h), pp. 407-408 (2d ed. 1987 and Supp. 1988). This “reasonable person” standard also ensures that the scope of Fourth Amendment protection does not vary with the state of mind of the particular individual being approached.</p>
<p id="b632-6">C</p>
<p id="b632-7">Applying the Court’s test to the facts of this case, we conclude that respondent was not seized by the police before he discarded the packets containing the controlled substance. Although Officer Peltier referred to the police conduct as a “chase,” and the Magistrate who originally dismissed the complaint was impressed by this description,<footnotemark>6</footnotemark> the characterization is not enough, standing alone, to implicate Fourth Amendment protections. Contrary to respondent’s assertion that a chase necessarily communicates that detention is <page-number citation-index="1" label="575">*575</page-number>intended and imminent, Brief for Respondent 9, the police conduct involved here would not have communicated to the reasonable person an attempt to capture or otherwise intrude upon respondent’s freedom of movement.<footnotemark>7</footnotemark> The record does not reflect that the police activated a siren or flashers; or that they commanded respondent to halt, or displayed any weapons; or that they operated the car in an aggressive manner to block respondent’s course or otherwise control the direction or speed of his movement. Tr. of Oral Arg. 2, 11, 20.<footnotemark>8</footnotemark> While the very presence of a police car driving parallel to a running pedestrian could be somewhat intimidating, this kind of police presence does not, standing alone, constitute a seizure.<footnotemark>9</footnotemark> Cf. <em>United States </em>v. <em>Knotts, </em><span class="citation" data-id="9429102"><a href="/opinion/110882/united-states-v-knotts/" aria-description="Citation for case: United States v. Knotts">460 U. S. 276</a></span> (1983) <page-number citation-index="1" label="576">*576</page-number>(holding that continuous surveillance on public thoroughfares by visual observation and electronic “beeper” does not constitute seizure); <em>Florida </em>v. Royer, <span class="citation" data-id="9429117"><a href="/opinion/110890/florida-v-royer/#497" aria-description="Citation for case: Florida v. Royer">460 U. S., at 497</a></span> (plurality opinion) (noting that mere approach by law enforcement officers, identified as such, does not constitute seizure). Without more, the police conduct here — a brief acceleration to catch up with respondent, followed by a short drive alongside him — was not “so intimidating” that respondent could reasonably have believed that he was not free to disregard the police presence and go about his business. <em>INS </em>v. <em>Delgado, </em><span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#216" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S., at 216</a></span>. The police therefore were not required to have “a particularized and objective basis for suspecting [respondent] of criminal activity,” in order to pursue him. <em>United States </em>v. <em>Cortez, </em><span class="citation" data-id="9428131"><a href="/opinion/110377/united-states-v-cortez/#417" aria-description="Citation for case: United States v. Cortez">449 U. S. 411, 417-418</a></span> (1981).</p>
<p id="b634-9">J-H HH</p>
<p id="b634-1">Because respondent was not unlawfully seized during the initial police pursuit, we conclude that charges against him were improperly dismissed. Accordingly, we reverse the judgment of the Michigan Court of Appeals, and remand the case to that court for further proceedings not inconsistent with this opinion.</p>
<p id="b634-2">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b628-6"> The Magistrate did not independently consider whether the codeine pills, if lawfully seized, established probable cause justifying respondent’s arrest. The Fourth Amendment issue before us is therefore limited to the police conduct preceding and including respondent’s disposal of the packets.</p>
</footnote>
<footnote label="2">
<p id="b628-7"> In <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>a police officer got out of his unmarked car and “gave chase” on foot after allegedly observing the defendant stick his hand in his pocket and run at the sight of the officer. <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#678" aria-description="Citation for case: People v. Terrell">77 Mich. App., at 678</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188</a></span>. According to the officer, the defendant ran into an apartment building where the officer observed him drop a clear envelope containing a brown powdery substance. Having determined that the package might contain heroin, the officer arrested the defendant. At a pretrial hearing, the trial court granted the defendant’s motion to suppress the envelope and its contents. The Michigan Court of Appeals affirmed, finding that the police “investigatory pursuit” constituted a seizure that was unjustified by any particularized suspicion that the defendant was engaged in criminal activity. <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#679" aria-description="Citation for case: People v. Terrell"><em>Id., </em>at 679-680</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188-189</a></span>.</p>
</footnote>
<footnote label="3">
<p id="b629-5"> The Michigan Court of Appeals rested its holding on <em>People </em>v. <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell, supra,</a></span> </em>and <em>People </em>v. <em>Shabaz, </em><span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">424 Mich. 42</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d 451</a></span> (1985), cert. dism’d (in view of that respondent’s death), <span class="citation multiple-matches"><a href="/c/U.%20S./478/1017/">478 U. S. 1017</a></span> (1986), both of which were to the effect that the defendant in question had been seized in violation of the Fourth Amendment of the United States Constitution. In <em>Shabaz, </em>the Michigan Supreme Court quoted “Michigan’s analogous [constitutional] provision,” without elaboration, in a footnote following a recitation of the Fourth Amendment. <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#52" aria-description="Citation for case: People v. Shabaz">424 Mich., at 52, n. 4</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#455" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d, at 455, n. 4</a></span>. The Supreme Court said nothing to suggest that the Michigan Constitution’s seizure provision provided an independent source of relief, and the court’s entire analysis rested expressly on the Fourth Amendment and federal cases. Similarly, in <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>the Michigan Court of Appeals stated that the suppression of evidence and dismissal of charges against the defendant “was soundly based on existing law, state and Federal,” but made clear that the scope of the right in question was defined “by the Fourth Amendment’s general proscription against unreasonable searches and seizures.” <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#679" aria-description="Citation for case: People v. Terrell">77 Mich. App., at 679</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188</a></span>, citing <em>Terry </em>v. <em>Ohio, </em><span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968). In light of the bases for the courts’ decisions in <em>Shabaz </em>and <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>we readily conclude that the decision below likewise rests on the Michigan courts’ interpretation of the Federal Constitution and not on any adequate and independent state ground. See <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983). The defense in effect concedes this. See Tr. of Oral Arg. 38-39.</p>
</footnote>
<footnote label="4">
<p id="AJ6"> Two justices of the Michigan Supreme Court would have granted leave to appeal. See App. to Pet. for Cert. 10a.</p>
</footnote>
<footnote label="5">
<p id="b631-10"> Three other Justices, otherwise in the majority, chose not to reach the question whether the federal officers had seized respondent. <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#560" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 560</a></span> (opinion concurring in part and concurring in the judgment).</p>
</footnote>
<footnote label="6">
<p id="b632-8"> At the preliminary hearing, the Magistrate interrupted the State’s attorney, who was asserting that the police were simply performing routine patrolling duties, with the following:</p>
<blockquote id="b632-9">“That would be fine until the Officer said we were chasing him in the car, otherwise I would agree with you. My ears picked up when the Officer said that, you know. He said we went around. I asked him why were you chasing him in the car, why were you chasing him and he said because he was running and we wanted to see where he was going.” App. 29-30.</blockquote>
</footnote>
<footnote label="7">
<p id="b633-5"> As Officer Peltier explained, the goal of the “chase” was not to capture respondent, but “to see where he was going.” <em>Id., </em>at 25. Of course, the subjective intent of the officers is relevant to an assessment of the Fourth Amendment implications of police conduct only to the extent that that intent has been conveyed to the person confronted. <em>United States </em>v. <em>Mendenhall, </em><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S., at 554, n. 6</a></span> (opinion of Stewart, J.). See also 3 W. LaFave, Search and Seizure § 9.2(h), p. 407 (2d ed. 1987 and Supp. 1988) (uncommunicated intent of police irrelevant to determination of whether seizure occurred).</p>
</footnote>
<footnote label="8">
<p id="b633-6"> The facts of this case are not identical to the facts involved in both <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span> </em>and <em>Shabaz, </em>upon which the Michigan courts relied in finding a seizure in this case. In both <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span> </em>and <em>Shabaz, </em>a police officer got out of the car to chase the pedestrian suspect on foot, after which the defendant abandoned the inculpatory evidence. <em>People </em>v. <em>Terrell, </em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#678" aria-description="Citation for case: People v. Terrell">77 Mich. App., at 678</a></span>, <span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/#188" aria-description="Citation for case: People v. Terrell">259 N. W. 2d, at 188</a></span>; <em>People </em>v. <em>Shabaz, </em><span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#47" aria-description="Citation for case: People v. Shabaz">424 Mich., at 47-48</a></span>, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#453" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d, at 453</a></span>. In <em>Shabaz, </em>the State appears to have stipulated that the chase, whose clear object was to apprehend the defendant, constituted a seizure. <em>Id., </em>at 52, <span class="citation" data-id="9733829"><a href="/opinion/2189647/people-v-shabaz/#455" aria-description="Citation for case: People v. Shabaz">378 N. W. 2d, at 455</a></span>. While no similar stipulation was entered in <em><span class="citation" data-id="1243152"><a href="/opinion/1243152/people-v-terrell/" aria-description="Citation for case: People v. Terrell">Terrell</a></span>, </em>the goal of that chase appears to have been equally clear. We, of course, intimate no view as to the federal constitutional correctness of either of those Michigan state-court cases.</p>
</footnote>
<footnote label="9">
<p id="b633-7"> The United States, which has submitted a brief as <em>amicus curiae, </em>suggests that, in some circumstances, police pursuit “will amount to a stop from the outset or from an early point in the chase, if the police command the person to halt and indicate that he is not free to go.” Brief for United States as <em>Amicus Curiae </em>13. Of course, such circumstances are not before <page-number citation-index="1" label="576">*576</page-number>us in this case. We therefore leave to another day the determination of the circumstances in which police pursuit could amount to a seizure under the Fourth Amendment.</p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/Michigan v. Clifford.md  (`case`, 6 assertions)

### content_page

```
---
title: "Michigan v. Clifford"
type: case
citation: "464 U.S. 287 (1984)"
parallel_cite: "104 S. Ct. 641; 78 L. Ed. 2d 477; 52 U.S.L.W. 4056"
neutral_cite: 1984 U.S. LEXIS 14
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-01-11
docket: 82-357
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-01-11
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Michigan v. Clifford
  varies_by_point: false
  scope_note: "Plurality opinion (Powell, J., joined by Brennan, White, Marshall; Stevens, J., concurring in the judgment supplied the fifth vote on the result). The administrative-warrant / criminal-warrant framework for post-fire searches is the controlling teaching and is good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111057/michigan-v-clifford/"
  cluster_id: 111057
  opinion_id: 9429413
  identity_checked: true
homes:
  - page: "[[Emergency Aid]]"
    role: "Key — Limiting"
  - page: "[[Special Needs and Administrative Searches]]"
    role: "Related (cross-doctrine)"
related: ["[[Michigan v. Tyler]]", "[[Camara v. Municipal Court]]", "[[Mincey v. Arizona]]", "[[Coolidge v. New Hampshire]]"]
aliases: []
tags: ["case", "fourth-amendment", "fire", "administrative-warrant", "exigent-circumstances", "privacy-interests"]
holding: "Where reasonable privacy interests remain in fire-damaged property, a post-fire investigative search after the blaze is out and the scene is secured requires a warrant absent consent or a new exigency; an administrative warrant suffices to determine cause and origin, but a search whose primary object is to gather evidence of crime requires a criminal warrant on probable cause."
lake:
  record_id: Michigan v. Clifford
  status: verified
  projected_at: 2026-07-09
---

# Michigan v. Clifford

*464 U.S. 287 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A fire damaged the Cliffords' home in the early morning while they were away. Hours after the blaze was out and firefighters had left, an arson investigator and his partner arrived, entered the secured, uninhabitable house without a warrant or consent, and searched the basement (finding evidence of arson) and then the upstairs living areas. The Cliffords had arranged to have the house boarded up, and personal belongings remained inside.

## Issue
Whether a warrantless, nonconsensual post-fire investigative search of a private home — conducted after the fire is extinguished and officials have left the scene — violates the Fourth Amendment, and what kind of warrant such a search requires.

## Rule
If reasonable privacy interests remain, a warrant is required: "If reasonable privacy interests remain in the fire-damaged property, the warrant requirement applies, and any official entry must be made pursuant to a warrant in the absence of consent or exigent circumstances." — 464 U.S. at 293 (plurality). ^pin-293

The object of the search sets the type of warrant: "If the primary object is to determine the cause and origin of a recent fire, an administrative warrant will suffice. . . . If the primary object of the search is to gather evidence of criminal activity, a criminal search warrant may be obtained only on a showing of probable cause." — *Id.* at 294. ^pin-294

Applied to a home: "we hold that the Cliffords retained reasonable privacy interests in their fire-damaged residence and that the postfire investigations were subject to the warrant requirement." — [*Id.* at 295](https://www.courtlistener.com/opinion/111057/michigan-v-clifford/#:~:text=we%20hold%20that%20the%20Cliffords). ^pin-295

## Application
Although the home was fire-damaged and uninhabitable, the exterior and some upstairs rooms were largely intact, personal belongings remained, and the Cliffords had secured the house against intrusion — so, given the strong privacy expectations in a home, reasonable privacy interests survived. The blaze was long out, officials had left, and the State claimed no [[Exigent Circumstances and Hot Pursuit|exigency]], so the later warrantless basement and upstairs searches were subject to the warrant requirement; because they were conducted without a warrant or consent, they were unconstitutional.

## Conclusion
The post-fire warrantless searches violated the Fourth Amendment. *Clifford* refines *[[Michigan v. Tyler|Tyler]]*: once the fire is out and the scene is no longer an emergency, further investigation of premises in which privacy interests remain requires a warrant — administrative for cause-and-origin, criminal (on probable cause) for evidence of arson.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (plurality; Stevens, J., concurred in the judgment).
- **Refines** [[Michigan v. Tyler]] by drawing the line at the end of the fire-fighting [[Exigent Circumstances and Hot Pursuit|exigency]] and dividing post-fire searches into administrative (cause/origin) and criminal (evidence) warrant tracks. Parallels the no-crime-scene-exception rule of [[Mincey v. Arizona]]; the administrative-warrant standard traces to [[Camara v. Municipal Court]].

## Appears on
- [[Emergency Aid]] — *Key — Limiting*
- [[Special Needs and Administrative Searches]] — *Related (cross-doctrine)*

## Sources
- *Michigan v. Clifford*, 464 U.S. 287 (1984) — https://www.courtlistener.com/opinion/111057/michigan-v-clifford/ — pinpoints: 293, 294, 295.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "da64e6b40f25a5ad", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "464 U.S. 287 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 14", "official_citation_present": true, "parallel_cite": "104 S. Ct. 641; 78 L. Ed. 2d 477; 52 U.S.L.W. 4056", "title": "Michigan v. Clifford", "year": "1984"}}
{"assertion_id": "4b15184f43d41018", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Where reasonable privacy interests remain in fire-damaged property, a post-fire investigative search after the blaze is out and the scene is secured requires a warrant absent consent or a new exigency; an administrative warrant suffices to determine cause and origin, but a search whose primary object is to gather evidence of crime requires a criminal warrant on probable cause.", "title": "Michigan v. Clifford"}}
{"assertion_id": "583bb5dc70056478", "dimension": "support", "kind": "home_role", "locator": {"home": "Emergency Aid"}, "payload": {"home": "Emergency Aid", "role": "Key — Limiting", "title": "Michigan v. Clifford"}}
{"assertion_id": "d1ce1bd981d348c6", "dimension": "support", "kind": "home_role", "locator": {"home": "Special Needs and Administrative Searches"}, "payload": {"home": "Special Needs and Administrative Searches", "role": "Related (cross-doctrine)", "title": "Michigan v. Clifford"}}
{"assertion_id": "8acfb54a944dd25b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-01-11", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Michigan v. Clifford", "field_i_validity": "good_law", "scope_note": "Plurality opinion (Powell, J., joined by Brennan, White, Marshall; Stevens, J., concurring in the judgment supplied the fifth vote on the result). The administrative-warrant / criminal-warrant framework for post-fire searches is the controlling teaching and is good law.", "title": "Michigan v. Clifford", "varies_by_point": "false"}}
{"assertion_id": "f6eb9ac1abb5a2dc", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Michigan v. Clifford"}}
```

### lake record — Michigan v. Clifford

```json
{
  "schema_version": "s2.v1",
  "record_id": "Michigan v. Clifford",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Michigan v. Clifford",
    "case_name_short": "",
    "case_name_full": "MICHIGAN v. CLIFFORD Et Al.",
    "input_case_name": "Michigan v. Clifford",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-01-11",
    "year": 1984,
    "docket": "82-357",
    "cluster_id": 111057,
    "lead_opinion_id": 9429413,
    "sibling_ids": [
      111057,
      9429413,
      9429414,
      9429415
    ],
    "absolute_url": "/opinion/111057/michigan-v-clifford/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9350257,
        "score": 20,
        "case_name": "Michigan v. Clifford"
      }
    ],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "464 U.S. 287",
      "volume": "464",
      "reporter": "U.S.",
      "page": "287",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 641",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "641",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 L. Ed. 2d 477",
        "volume": "78",
        "reporter": "L. Ed. 2d",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4056",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4056",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 14",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "464 U.S. 287",
        "volume": "464",
        "reporter": "U.S.",
        "page": "287",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 641",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "641",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "78 L. Ed. 2d 477",
        "volume": "78",
        "reporter": "L. Ed. 2d",
        "page": "477",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 14",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "14",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4056",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4056",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "464 U.S. 287",
    "official_selection": {
      "court_class": "scotus",
      "selected": "464 U.S. 287",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-293",
      "page": null,
      "quote": "--- # Michigan v. Clifford *464 U.S. 287 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A fire damaged the Cliffords' home in the early morning while they were away. Hours after the blaze was out and firefighters had left, an arson investigator and his partner arrived, entered the secured, uninhabitable house without a warrant or consent, and searched the basement (finding evidence of arson) and then the upstairs living areas. The Cliffords had arranged to have the house boarded up, and personal belongings remained inside. ## Issue Whether a warrantless, nonconsensual post-fire investigative search of a private home \u2014 conducted after the fire is extinguished and officials have left the scene \u2014 violates the Fourth Amendment, and what kind of warrant such a search requires. ## Rule If reasonable privacy interests remain, a warrant is required:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-294",
      "page": null,
      "quote": "If the primary object is to determine the cause and origin of a recent fire, an administrative warrant will suffice. . . . If the primary object of the search is to gather evidence of criminal activity, a criminal search warrant may be obtained only on a showing of probable cause.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-295",
      "page": null,
      "quote": "we hold that the Cliffords retained reasonable privacy interests in their fire-damaged residence and that the postfire investigations were subject to the warrant requirement.",
      "star_marker": "295",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 14913,
      "fragment": "#:~:text=we%20hold%20that%20the%20Cliffords",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-01-11",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Michigan v. Clifford",
    "varies_by_point": false,
    "scope_note": "Plurality opinion (Powell, J., joined by Brennan, White, Marshall; Stevens, J., concurring in the judgment supplied the fifth vote on the result). The administrative-warrant / criminal-warrant framework for post-fire searches is the controlling teaching and is good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. O'Donnell",
          "cluster_id": 4427767,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane1_negative"
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
        "journal_ref": "Michigan v. Clifford:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Leland Earl Dart",
          "cluster_id": 443977,
          "cite": [
            "747 F.2d 263",
            "1984 U.S. App. LEXIS 17111"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane1_negative"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Welsh v. Wisconsin",
          "cluster_id": 111173,
          "cite": [
            "80 L. Ed. 2d 732",
            "104 S. Ct. 2091",
            "466 U.S. 740",
            "1984 U.S. LEXIS 82",
            "52 U.S.L.W. 4581"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Villarreal v. State",
          "cluster_id": 2365320,
          "cite": [
            "935 S.W.2d 134",
            "1996 Tex. Crim. App. LEXIS 237",
            "1996 WL 668593"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "New York v. Burger",
          "cluster_id": 111927,
          "cite": [
            "96 L. Ed. 2d 601",
            "107 S. Ct. 2636",
            "482 U.S. 691",
            "1987 U.S. LEXIS 2725",
            "55 U.S.L.W. 4890"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Montoya De Hernandez",
          "cluster_id": 111509,
          "cite": [
            "87 L. Ed. 2d 381",
            "105 S. Ct. 3304",
            "473 U.S. 531",
            "1985 U.S. LEXIS 120",
            "53 U.S.L.W. 5048"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Wharton",
          "cluster_id": 1196421,
          "cite": [
            "809 P.2d 290",
            "53 Cal. 3d 522",
            "280 Cal. Rptr. 631",
            "91 Daily Journal DAR 4957",
            "91 Cal. Daily Op. Serv. 3426",
            "1991 Cal. LEXIS 1608"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Silvers",
          "cluster_id": 2014870,
          "cite": [
            "587 N.W.2d 325",
            "255 Neb. 702",
            "1998 Neb. LEXIS 230"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Donald P. Rohrig",
          "cluster_id": 728738,
          "cite": [
            "98 F.3d 1506",
            "1996 U.S. App. LEXIS 28274",
            "1996 WL 627521"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Woods",
          "cluster_id": 1160907,
          "cite": [
            "981 P.2d 1019",
            "88 Cal. Rptr. 2d 88",
            "21 Cal. 4th 668"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
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
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Scott",
          "cluster_id": 5690717,
          "cite": [
            "79 N.Y.2d 474"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "California v. Rooney",
          "cluster_id": 111943,
          "cite": [
            "97 L. Ed. 2d 258",
            "107 S. Ct. 2852",
            "483 U.S. 307",
            "1987 U.S. LEXIS 2870"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Palmieri v. Pamela Lynch, AKA Pam Lynch, John Doe 1",
          "cluster_id": 788624,
          "cite": [
            "392 F.3d 73",
            "2004 U.S. App. LEXIS 25468",
            "2004 WL 2827676"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Doering v. State",
          "cluster_id": 1525226,
          "cite": [
            "545 A.2d 1281",
            "313 Md. 384",
            "1988 Md. LEXIS 115"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alexander v. City And County Of San Francisco",
          "cluster_id": 674655,
          "cite": [
            "29 F.3d 1355",
            "94 Cal. Daily Op. Serv. 5278",
            "94 Daily Journal DAR 9698",
            "1994 U.S. App. LEXIS 16752"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Michigan v. Clifford:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 181,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 181,
        "triage_read": 4,
        "triage_snippet_classified": 177
      },
      "lane2_top_cited": {
        "query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02NSZzPTEzNTU2NTQmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111057+OR+9429413+OR+9429414+OR+9429415%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415)",
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
    "complete_query": "cites:(111057 OR 9429413 OR 9429414 OR 9429415)",
    "indexed_citing_opinions": 233,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111057,
        "count": 212,
        "count_source": "search"
      },
      {
        "opinion_id": 9429413,
        "count": 24,
        "count_source": "search"
      },
      {
        "opinion_id": 9429414,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429415,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 346,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/michigan-v-clifford.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU1Mjk2MDUmcz03MzI3MDE1JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111057+OR+9429413+OR+9429414+OR+9429415%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111057,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 107474,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108077,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108533,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 109866,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 109876,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 110118,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111057,
        "cited_id": 110530,
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
    "date_created": "2026-07-05T13:17:01Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T13:17:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T13:17:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T13:21:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T13:17:30Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Michigan v. Clifford

```
<opinion type="majority">
<author id="b400-10">Justice Powell</author>
<p id="Akt">announced the judgment of the Court and delivered an opinion,</p>
<judges id="AL8">in which Justice Brennan, Justice White, and Justice Marshall joined.</judges>
<p id="b400-11">This case presents questions as to the authority of arson investigators, in the absence of exigent circumstances or consent, to enter a private residence without a warrant to investigate the cause of a recent fire.</p>
<p id="b401-3"><page-number citation-index="1" label="289">*289</page-number>Respondents, Raymond and Emma Jean Clifford, were arrested and charged with arson in connection with a fire at their private residence. At the preliminary examination held to establish probable cause for the alleged offense, the State introduced various pieces of physical evidence, most of which was obtained through a warrantless and nonconsensual search of the Cliffords’ fire-damaged home. Respondents moved to suppress this evidence on the ground that it was obtained in violation of their rights under the Fourth and Fourteenth Amendments. That motion was denied and respondents were bound over for trial. Before trial, they again moved to suppress the evidence obtained during the search. The trial court conducted an evidentiary hearing and denied the motion on the ground that exigent circumstances justified the search. The court certified its eviden-tiary ruling for interlocutory appeal and the Michigan Court of Appeals reversed.</p>
<p id="b401-4">That court held that there were no exigent circumstances justifying the search. Instead, it found that the warrantless entry and search of the Clifford residence were conducted pursuant to a policy of the Arson Division of the Detroit Fire Department that sanctioned such searches as long as the owner was not present, the premises were open to trespass, and the search occurred within a reasonable time of the fire. The Court of Appeals held that this policy was inconsistent with <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499</a></span> (1978), and that the warrantless nonconsensual search of the Cliffords’ residence violated their rights under the Fourth and Fourteenth Amendments. We granted certiorari to clarify doubt that appears to exist as to the application of our decision in <em>Tyler. </em><span class="citation multiple-matches"><a href="/c/U.%20S./459/1168/">459 U. S. 1168</a></span> (1983).</p>
<p id="b401-5">II</p>
<p id="b401-6">In the early morning hours of October 18, 1980, a fire erupted at the Clifford home. The Cliffords were out of town on a camping trip at the time. The fire was reported to the Detroit Fire Department, and fire units arrived on the <page-number citation-index="1" label="290">*290</page-number>scene about 5:40 a. m. The fire was extinguished and all fire officials and police left the premises at 7:04 a. m.</p>
<p id="b402-5">At 8 o’clock on the morning of the fire, Lieutenant Beyer, a fire investigator with the arson section of the Detroit Fire Department, received instructions to investigate the Clifford fire. He was informed that the Fire Department suspected arson. Because he had other assignments, Lieutenant Beyer did not proceed immediately to the Clifford residence. He and his partner finally arrived at the scene of the fire about 1 p. m. on October 18.</p>
<p id="b402-6">When they arrived, they found a work crew on the scene. The crew was boarding up the house and pumping some six inches of water out of the basement. A neighbor told the investigators that he had called Mr. Clifford and had been instructed to request the Cliffords’ insurance agent to send a boarding crew out to secure the house. The neighbor also advised that the Cliffords did not plan to return that day. While the investigators waited for the water to be pumped out, they found a Coleman fuel can in the driveway that was seized and marked as evidence.<footnotemark>1</footnotemark></p>
<p id="b402-7">By 1:30 p. m., the water had been pumped out of the basement and Lieutenant Beyer and his partner, without obtaining consent or an administrative warrant, entered the Clifford residence and began their investigation into the cause of the fire. Their search began in the basement and they quickly confirmed that the fire had originated there beneath the basement stairway. They detected a strong odor of fuel throughout the basement, and found two more Coleman fuel cans beneath the stairway. As they dug through the debris, the investigators also found a crock pot with attached wires leading to an electrical timer that was plugged into an outlet <page-number citation-index="1" label="291">*291</page-number>a few feet away. The timer was set to turn on at approximately 3:45 a. m. and to turn back off at approximately 9 a. m. It had stopped somewhere between 4 and 4:30 a. m. All of this evidence was seized and marked.</p>
<p id="b403-5">After determining that the fire had originated in the basement, Lieutenant Beyer and his partner searched the remainder of the house. The warrantless search that followed was extensive and thorough. The investigators called in a photographer to take pictures throughout the house. They searched through drawers and closets and found them full of old clothes. They inspected the rooms and noted that there were nails on the walls but no pictures. They found wiring and cassettes for a video tape machine but no machine.</p>
<p id="b403-6">Respondents moved to exclude all exhibits and testimony based on the basement and upstairs searches on the ground that they were searches to gather evidence of arson, that they were conducted without a warrant, consent, or exigent circumstances, and that they therefore were <em>per se </em>unreasonable under the Fourth and Fourteenth Amendments. Petitioner, on the other hand, argues that the entire search was reasonable and should be exempt from the warrant requirement.</p>
<p id="b403-7">Ill</p>
<p id="b403-8">In its petition for certiorari, the State does not challenge the state court’s finding that there were no exigent circumstances justifying the search of the Clifford home. Instead, it asks us to exempt from the warrant requirement all administrative investigations into the cause and origin of a fire. We decline to do so.</p>
<p id="b403-9">In <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span>, </em>we restated the Court’s position that administrative searches generally require warrants. <span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#504" aria-description="Citation for case: Michigan v. Tyler">436 U. S., at 504-508</a></span>. See <em>Marshall </em>v. <em>Barlow’s, Inc., </em><span class="citation" data-id="9427200"><a href="/opinion/109866/marshall-v-barlows-inc/" aria-description="Citation for case: Marshall v. Barlow&#x27;s, Inc.">436 U. S. 307</a></span> (1978); <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523</a></span> (1967); <em>See </em>v. <em>City of Seattle, </em><span class="citation" data-id="9423449"><a href="/opinion/107474/see-v-city-of-seattle/" aria-description="Citation for case: See v. City of Seattle">387 U. S. 541</a></span> (1967). We reaffirm that view again today. Except in certain carefully defined <page-number citation-index="1" label="292">*292</page-number>classes of cases,<footnotemark>2</footnotemark> the nonconsensual entry and search of property are governed by the warrant requirement of the Fourth and Fourteenth Amendments. The constitutionality of warrantless and nonconsensual entries onto fire-damaged premises, therefore, normally turns on several factors: whether there are legitimate privacy interests in the fire-damaged property that are protected by the Fourth Amendment; whether exigent circumstances justify the government intrusion regardless of any reasonable expectations of privacy; and, whether the object of the search is to determine the cause of fire or to gather evidence of criminal activity.</p>
<p id="b404-5">A</p>
<p id="b404-6">We observed in <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>that reasonable privacy expectations may remain in fire-damaged premises. “People may go on living in their homes or working in their offices after a fire. Even when that is impossible, private effects often remain on the fire-damaged premises.” <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#505" aria-description="Citation for case: Michigan v. Tyler">436 U. S., at 505</a></span>. Privacy expectations will vary with the type of property, the amount of fire damage, the prior and continued use of the premises, and in some cases the owner’s efforts to secure it against intruders. Some fires may be so devastating that no reasonable privacy interests remain in the ash and ruins, regardless of the owner’s subjective expectations. The test essentially is an objective one: whether “the expectation [is] one that society is prepared to recognize as ‘reasonable.’” <em>Katz </em>v. <em>United States, </em><span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#361" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 361</a></span> (1967) (Harlan, J., concurring). See also <em>Smith </em>v. <em>Maryland, </em><span class="citation" data-id="9427638"><a href="/opinion/110118/smith-v-maryland/#739" aria-description="Citation for case: Smith v. Maryland">442 U. S. 735, 739-741</a></span> (1979). If reasonable privacy interests remain in <page-number citation-index="1" label="293">*293</page-number>the fire-damaged property, the warrant requirement applies, and any official entry must be made pursuant to a warrant in the absence of consent or exigent circumstances.</p>
<p id="b405-5">B</p>
<p id="b405-6">A burning building of course creates an exigency that justifies a warrantless entry by fire officials to fight the blaze. Moreover, in <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>we held that once in the building, officials need no warrant to remain<footnotemark>3</footnotemark> for “a reasonable time to investigate the cause of a blaze after it has been extinguished.” 436 U. S., at 510. Where, however, reasonable expectations of privacy remain in the fire-damaged property, additional investigations begun after the fire has been extinguished and fire and police officials have left the scene, generally must be made pursuant to a warrant or the identification of.some new exigency.</p>
<p id="b405-7">The aftermath of a fire often presents exigencies that will not tolerate the delay necessary to obtain a warrant or to secure the owner’s consent to inspect fire-damaged premises.<footnotemark>4</footnotemark> Because determining the cause and origin of a fire serves a compelling public interest, the warrant requirement does not apply in such cases.</p>
<p id="b406-4"><page-number citation-index="1" label="294">*294</page-number>c</p>
<p id="b406-5">If a warrant is necessary, the object of the search determines the type of warrant required. If the primary object is to determine the cause and origin of a recent fire, an administrative warrant will suffice.<footnotemark>6</footnotemark> To obtain such a warrant, fire officials need show only that a fire of undetermined origin has occurred on the premises, that the scope of the proposed search is reasonable and will not intrude unnecessarily on the fire victim’s privacy, and that the search will be executed at a reasonable and convenient time.</p>
<p id="b406-6">If the primary object of the search is to gather evidence of criminal activity, a criminal search warrant may be obtained only on a showing of probable cause to believe that relevant evidence will be found in the place to be searched. If evidence of criminal activity is discovered during the course of a valid administrative search, it may be seized under the “plain view” doctrine. <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#465" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 465-466</a></span> (1971). This evidence then may be used to establish probable cause to obtain a criminal search warrant. Fire officials may not, however, rely on this evidence to expand the scope of their administrative search without first making a successful showing of probable cause to an independent judicial officer.</p>
<p id="b406-7">The object of the search is important even if exigent circumstances exist. Circumstances that justify a warrantless search for the cause of a fire may not justify a search to gather evidence of criminal activity once that cause has been determined. If, for example, the administrative search is justified by the immediate need to ensure against rekindling, the scope of the search may be no broader than reasonably <page-number citation-index="1" label="295">*295</page-number>necessary to achieve its end. A search to gather evidence of criminal activity not in plain view must be made pursuant to a criminal warrant upon a traditional showing of probable cause.<footnotemark>6</footnotemark></p>
<p id="b407-5">The searches of the Clifford home, at least arguably, can be viewed as two separate ones: the delayed search of the basement area, followed by the extensive search of the residential portion of the house. We now apply the principles outlined above to each of these searches.</p>
<p id="b407-6">IV</p>
<p id="b407-7">The Clifford home was a two-and-one-half story brick and frame residence. Although there was extensive damage to the lower interior structure, the exterior of the house and some of the upstairs rooms were largely undamaged by the fire, although there was some smoke damage. The firemen had broken out one of the doors and most of the windows in fighting the blaze. At the time Lieutenant Beyer and his partner arrived, the home was uninhabitable. But personal belongings remained, and the Cliffords had arranged to have the house secured against intrusion in their absence. Under these circumstances, and in light of the strong expectations of privacy associated with a home, we hold that the Cliffords retained reasonable privacy interests in their fire-damaged residence and that the postfire investigations were subject to the warrant requirement. Thus, the warrantless and non-consensual searches of both the basement and the upstairs areas of the house would have been valid only if exigent circumstances had justified the object and the scope of each.</p>
<p id="b408-4"><page-number citation-index="1" label="296">*296</page-number>A</p>
<p id="b408-5">As noted, the State does not claim that exigent circumstances justified its postfire searches. It argues that we either should exempt postfire searches from the warrant requirement or modify <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>to justify the warrantless searches in this case. We have rejected the State’s first argument and turn now to its second.</p>
<p id="b408-6">In <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span> </em>we upheld a warrantless postfire search of a furniture store, despite the absence of exigent circumstances, on the ground that it was a continuation of a valid search begun immediately after the fire. The investigation was begun as the last flames were being doused, but could not be completed because of smoke and darkness. The search was resumed promptly after the smoke cleared and daylight dawned. Because the postfire search was interrupted for reasons that were evident, we held that the early morning search was “no more than an actual continuation of the first, and the lack of a warrant thus did not invalidate the resulting seizure of evidence.” 436 U. S., at 511.</p>
<p id="b408-7">As the State conceded at oral argument, this case is distinguishable for several reasons. First, the challenged search was not a continuation of an earlier search. Between the time the firefighters had extinguished the blaze and left the scene and the arson investigators first arrived about 1 p. m. to begin their investigation, the Cliffords had taken steps to secure the privacy interests that remained in their residence against further intrusion. These efforts separate the entry made to extinguish the blaze from that made later by different officers to investigate its origin. Second, the privacy interests in the residence — particularly after the Cliffords had acted — were significantly greater than those in the fire-damaged furniture store, making the delay between the fire and the midday search unreasonable absent a warrant, consent, or exigent circumstances. We frequently have noted that privacy interests are especially strong in a private resi-<page-number citation-index="1" label="297">*297</page-number>deuce.<footnotemark>7</footnotemark> These facts — the interim efforts to secure the burned-out premises and the heightened privacy interests in the home — distinguish this case from <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler</a></span>. </em>At least where a homeowner has made a reasonable effort to secure his fire-damaged home after the blaze has been extinguished and the fire and police units have left the scene, we hold that a subsequent postfire search must be conducted pursuant to a warrant, consent, or the identification of some new exigency.<footnotemark>8</footnotemark> So long as the primary purpose is to ascertain the cause of the fire, an administrative warrant will suffice.</p>
<p id="b409-5">B</p>
<p id="b409-6">Because the cause of the fire was then known, the search of the upper portions of the house, described above, could only have been a search to gather evidence of the crime of arson. Absent exigent circumstances, such a search requires a criminal warrant.</p>
<p id="b409-7">Even if the midday basement search had been a valid administrative search, it would not have justified the upstairs search. The scope of such a search is limited to that reasonably necessary to determine the cause and origin of a fire and to ensure against rekindling. As soon as the investigators determined that the fire had originated in the basement and had been caused by the crock pot and timer found beneath <page-number citation-index="1" label="298">*298</page-number>the basement stairs, the scope of their search was limited to the basement area. Although the investigators could have used whatever evidence they discovered in the basement to establish probable cause to search the remainder of the house, they could not lawfully undertake that search without a prior judicial determination that a successful showing of probable cause had been made. Because there were no exigent circumstances justifying the upstairs search, and it was undertaken without a prior showing of probable cause before an independent judicial officer, we hold that this search of a home was unreasonable under the Fourth and Fourteenth Amendments, regardless of the validity of the basement search.<footnotemark>9</footnotemark></p>
<p id="b410-5">The warrantless intrusion into the upstairs regions of the Clifford house presents a telling illustration of the importance of prior judicial review of proposed administrative searches. If an administrative warrant had been obtained in this case, it presumably would have limited the scope of the proposed investigation and would have prevented the warrantless intrusion into the upper rooms of the Clifford home. An administrative search into the cause of a recent fire does not give fire officials license to roam freely through the fire victim’s private residence.</p>
<p id="b410-6">V</p>
<p id="b410-7">The only pieces of physical evidence that have been challenged on this interlocutory appeal are the three empty fuel <page-number citation-index="1" label="299">*299</page-number>cans, the electric crock pot, and the timer and attached cord. Respondents also have challenged the testimony of the investigators concerning the warrantless search of both the basement and the upstairs portions of the Clifford home. The discovery of two of the fuel cans, the crock pot, the timer and cord — as well as the investigators’ related testimony — were the product of the unconstitutional postfire search of the Cliffords’ residence. Thus, we affirm that portion of the judgment of the Michigan Court of Appeals that excluded that evidence. One of the fuel cans was discovered in plain view in the Cliffords’ driveway. This can was seen in plain view during the initial investigation by the firefighters. It would have been admissible whether it had been seized in the basement by the firefighters or in the driveway by the arson investigators. Exclusion of this evidence should be reversed.</p>
<p id="b411-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b402-8"> The can had been found in the basement by the fire officials who had fought the blaze. The firemen removed the can and put it by the side door where Lieutenant Beyer discovered it on his arrival.</p>
</footnote>
<footnote label="2">
<p id="b404-7"> See, <em>e. g., Donovan </em>v. <em>Dewey, </em><span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594</a></span> (1981) (heavily regulated business); <em>United States </em>v. <em>Biswell, </em><span class="citation" data-id="9424870"><a href="/opinion/108533/united-states-v-biswell/" aria-description="Citation for case: United States v. Biswell">406 U. S. 311</a></span> (1972) (same); <em>Colonnade Corp. </em>v. <em>United States, </em><span class="citation" data-id="9424185"><a href="/opinion/108077/colonnade-catering-corp-v-united-states/" aria-description="Citation for case: Colonnade Catering Corp. v. United States">397 U. S. 72</a></span> (1970) (same). The exceptions to the warrant requirement recognized in these cases are not applicable to the warrantless search in this case.</p>
</footnote>
<footnote label="3">
<p id="b405-8"> We do not suggest that firemen fighting a fire normally remain within a building. The circumstances, of course, vary. In many situations actual entry may be too hazardous until the fire has been wholly extinguished, and even then the danger of collapsing walls may exist. Thus, the effort to ascertain the cause of a fire may extend over a period of time with entry and reentry. The critical inquiry is whether reasonable expectations of privacy exist in the fire-damaged premises at a particular time, and if so, whether exigencies justify the reentries.</p>
</footnote>
<footnote label="4">
<p id="b405-9"> For example, an immediate threat that the blaze might rekindle presents an exigency that would justify a warrantless and nonconsensual postfire investigation. “Immediate investigation may also be necessary to preserve evidence from intentional or accidental destruction.” See <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 510</a></span> (1978).</p>
</footnote>
<footnote label="5">
<p id="b406-8"> Probable cause to issue an administrative warrant exists if reasonable legislative, administrative, or judicially prescribed standards for conducting an inspection are satisfied with respect to a particular dwelling. See particularly <em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/" aria-description="Citation for case: Michigan v. Tyler">Tyler, supra;</a></span> </em>see also <em>Camara </em>v. <em>Municipal Court, </em><span class="citation" data-id="107473"><a href="/opinion/107473/camara-v-municipal-court-of-city-and-county-of-san-francisco/#538" aria-description="Citation for case: Camara v. Municipal Court of City and County of San...">387 U. S. 523, 538</a></span> (1967).</p>
</footnote>
<footnote label="6">
<p id="b407-8"> The plain-view doctrine must be applied in light of the special circumstances that frequently accompany fire damage. In searching solely to ascertain the cause, firemen customarily must remove rubble or search other areas where the cause of fires is likely to be found. An object that comes into view during such a search may be preserved without a warrant.</p>
</footnote>
<footnote label="7">
<p id="b409-8"> See, <em>e. g., Payton </em>v. <em>New York, </em><span class="citation multiple-matches"><a href="/c/U.%20S./445/578/">445 U. S. 578</a></span>, 589-590 (1980); <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972). Reasonable expectations of privacy in fire-damaged premises will vary depending particularly on the type and use of the building involved. Expectations of privacy are particularly strong in private residences and offices. There may be, depending upon the circumstances, diminished privacy expectations in commercial premises.</p>
</footnote>
<footnote label="8">
<p id="b409-9"> This is not to suggest that individual expectations of privacy may prevail over interests of public safety. For example, when fire breaks out in an apartment unit of an apartment complex, the exigency exception may allow warrantless postfire investigations where necessary to ensure against any immediate danger of future fire hazard.</p>
</footnote>
<footnote label="9">
<p id="b410-8"> In many cases, there will be no bright line separating the firefighters’ investigation into the cause of a fire from a search for evidence of arson. The distinction will vary with the circumstances of the particular fire and generally will involve more than the lapse of time or the number of entries and reentries. For example, once the cause of a fire in a single-family dwelling is determined, the administrative search should end, and any broader investigation should be made pursuant to a criminal warrant. A fire in an apartment, on the other hand, may present complexities that make it necessary for officials to conduct more expansive searches, to remain on the premises for longer periods of time, and to make repeated entries and reentries into the building. See <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#510" aria-description="Citation for case: Michigan v. Tyler">436 U. S., at 510, n. 6</a></span>.</p>
</footnote>
</opinion>
```

---
