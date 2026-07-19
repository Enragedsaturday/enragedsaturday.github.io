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

## GROUP: content/cases/Thompson v. Keohane.md  (`case`, 5 assertions)

### content_page

```
---
title: "Thompson v. Keohane"
type: case
citation: "516 U.S. 99 (1995)"
parallel_cite: "116 S. Ct. 457; 133 L. Ed. 2d 383"
neutral_cite: "1995 U.S. LEXIS 8315; 95 Cal. Daily Op. Serv. 8968"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1995
date_decided: 1995-11-29
docket: 94-6615
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1995-11-29
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Thompson v. Keohane
  varies_by_point: false
  scope_note: "Good law; the Miranda custody inquiry is objective (would a reasonable person feel free to terminate the interrogation and leave) and is a mixed question of law and fact. The §2254(d) habeas-review framework was later changed by AEDPA (1996); see Yarborough v. Alvarado for custody under AEDPA deference."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/117982/thompson-v-keohane/"
  cluster_id: 117982
  opinion_id: 117982
  identity_checked: true
homes:
  - page: "[[Miranda and Custodial Interrogation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Miranda v. Arizona]]", "[[California v. Beheler]]", "[[Stansbury v. California]]", "[[Yarborough v. Alvarado]]"]
aliases: []
tags: ["case", "fifth-amendment", "miranda", "custody", "objective-test", "habeas", "standard-of-review"]
holding: "The Miranda 'in custody' determination involves two inquiries — the circumstances of the interrogation (factual) and whether, given those circumstances, a reasonable person would have felt free to terminate the interrogation and leave (objective). The ultimate custody determination is a mixed question of law and fact qualifying for independent federal review."
lake:
  record_id: Thompson v. Keohane
  status: verified
  projected_at: 2026-07-06
---

# Thompson v. Keohane

*516 U.S. 99 (1995)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Thompson, suspected in the death of his former wife, was questioned by Alaska state troopers at their headquarters; he came voluntarily and was told he was free to leave and not under arrest. After a roughly two-hour interview in which the troopers confronted him with evidence, he made incriminating statements and was then arrested. The Alaska courts found he had not been "in custody" and admitted the statements. On federal [[Common Legal Terms#habeas-corpus|habeas]] review, the courts below treated the state court's no-custody finding as a factual determination entitled to a presumption of correctness under 28 U.S.C. §2254(d).

## Issue
Whether a state court's "in custody" determination for Miranda purposes is a factual finding entitled to the §2254(d) presumption of correctness, or a mixed question of law and fact subject to independent federal review — and what the custody inquiry requires.

## Rule
The custody inquiry is objective and two-part. "Two discrete inquiries are essential to the determination: first, what were the circumstances surrounding the interrogation; and second, given those circumstances, would a reasonable person have felt he or she was not at liberty to terminate the interrogation and leave. Once the scene is set and the players' lines and actions are reconstructed, the court must apply an objective test to resolve 'the ultimate inquiry': '[was] there a "formal arrest or restraint on freedom of movement" of the degree associated with a formal arrest.'" — 516 U.S. at 112 (quoting [[California v. Beheler]], 463 U.S. 1121, 1125 (1983)). ^pin-112

The first inquiry is factual and presumed correct under §2254(d), but the ultimate custody determination is legal: "This ultimate determination, we hold, presents a 'mixed question of law and fact' qualifying for independent review." — *Id.* at 112–113. ^pin-113

## Application
The "scene-setting" facts of Thompson's interrogation — where it occurred, what was said and done — are factual findings entitled to deference. But whether those circumstances amounted to custody turns on applying the objective reasonable-person standard, a task on which the state court is not "in an appreciably better position than the federal habeas court." Because the courts below had deferred to the state custody finding rather than reviewing it independently, the Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for that independent determination.

## Conclusion
The Miranda custody determination is an objective, mixed question of law and fact warranting independent federal review; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *Thompson* fixes the **objective** custody standard (reasonable person free to terminate and leave) in the [[Miranda v. Arizona]] line, building on [[California v. Beheler]] and the reasonable-person framing later confirmed in [[Stansbury v. California]]. The §2254(d) [[Common Legal Terms#habeas-corpus|habeas]]-review framework it applied was **later changed by AEDPA (1996)**; [[Yarborough v. Alvarado]] subsequently addressed a custody determination under AEDPA's deferential standard.

## Appears on
- [[Miranda and Custodial Interrogation]] — *Key — Progeny / Refinement*

## Sources
- *Thompson v. Keohane*, 516 U.S. 99 (1995) — https://www.courtlistener.com/opinion/117982/thompson-v-keohane/ — pinpoints: 112, 113.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "20306af86dc6902b", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "516 U.S. 99 (1995)", "court": "U.S. Supreme Court", "neutral_cite": "1995 U.S. LEXIS 8315; 95 Cal. Daily Op. Serv. 8968", "official_citation_present": true, "parallel_cite": "116 S. Ct. 457; 133 L. Ed. 2d 383", "title": "Thompson v. Keohane", "year": "1995"}}
{"assertion_id": "a5f5c348608c7b60", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The Miranda 'in custody' determination involves two inquiries — the circumstances of the interrogation (factual) and whether, given those circumstances, a reasonable person would have felt free to terminate the interrogation and leave (objective). The ultimate custody determination is a mixed question of law and fact qualifying for independent federal review.", "title": "Thompson v. Keohane"}}
{"assertion_id": "abd3d0c68652f41b", "dimension": "support", "kind": "home_role", "locator": {"home": "Miranda and Custodial Interrogation"}, "payload": {"home": "Miranda and Custodial Interrogation", "role": "Key — Progeny / Refinement", "title": "Thompson v. Keohane"}}
{"assertion_id": "17b69fcc732922b5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Thompson v. Keohane"}}
{"assertion_id": "d2502b73000252c9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1995-11-29", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Thompson v. Keohane", "field_i_validity": "good_law", "scope_note": "Good law; the Miranda custody inquiry is objective (would a reasonable person feel free to terminate the interrogation and leave) and is a mixed question of law and fact. The §2254(d) habeas-review framework was later changed by AEDPA (1996); see Yarborough v. Alvarado for custody under AEDPA deference.", "title": "Thompson v. Keohane", "varies_by_point": "false"}}
```

### lake record — Thompson v. Keohane

```json
{
  "schema_version": "s2.v1",
  "record_id": "Thompson v. Keohane",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Thompson v. Keohane",
    "case_name_short": "Thompson",
    "case_name_full": "THOMPSON v. KEOHANE, WARDEN, Et Al.",
    "input_case_name": "Thompson v. Keohane",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1995-11-29",
    "year": 1995,
    "docket": "94-6615",
    "cluster_id": 117982,
    "lead_opinion_id": 117982,
    "sibling_ids": [
      117982,
      9433228,
      9433229
    ],
    "absolute_url": "/opinion/117982/thompson-v-keohane/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "516 U.S. 99",
      "volume": "516",
      "reporter": "U.S.",
      "page": "99",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "116 S. Ct. 457",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "457",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "133 L. Ed. 2d 383",
        "volume": "133",
        "reporter": "L. Ed. 2d",
        "page": "383",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1995 U.S. LEXIS 8315",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "8315",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 Cal. Daily Op. Serv. 8968",
        "volume": "95",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "8968",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "516 U.S. 99",
        "volume": "516",
        "reporter": "U.S.",
        "page": "99",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "116 S. Ct. 457",
        "volume": "116",
        "reporter": "S. Ct.",
        "page": "457",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "133 L. Ed. 2d 383",
        "volume": "133",
        "reporter": "L. Ed. 2d",
        "page": "383",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1995 U.S. LEXIS 8315",
        "volume": "1995",
        "reporter": "U.S. LEXIS",
        "page": "8315",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 Cal. Daily Op. Serv. 8968",
        "volume": "95",
        "reporter": "Cal. Daily Op. Serv.",
        "page": "8968",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "516 U.S. 99",
    "official_selection": {
      "court_class": "scotus",
      "selected": "516 U.S. 99",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-112",
      "page": null,
      "quote": "determination for Miranda purposes is a factual finding entitled to the \u00a72254(d) presumption of correctness, or a mixed question of law and fact subject to independent federal review \u2014 and what the custody inquiry requires. ## Rule The custody inquiry is objective and two-part.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-113",
      "page": null,
      "quote": "This ultimate determination, we hold, presents a 'mixed question of law and fact' qualifying for independent review.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1995-11-29",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Thompson v. Keohane",
    "varies_by_point": false,
    "scope_note": "Good law; the Miranda custody inquiry is objective (would a reasonable person feel free to terminate the interrogation and leave) and is a mixed question of law and fact. The \u00a72254(d) habeas-review framework was later changed by AEDPA (1996); see Yarborough v. Alvarado for custody under AEDPA deference.",
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
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fisher",
          "cluster_id": 9427178,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Chilcoff",
          "cluster_id": 9417570,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Earl",
          "cluster_id": 9404588,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
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
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Hallford",
          "cluster_id": 4444995,
          "cite": [
            "280 F. Supp. 3d 170"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hammonds",
          "cluster_id": 4430449,
          "cite": [
            "804 S.E.2d 438",
            "370 N.C. 158",
            "2017 WL 4322423",
            "2017 N.C. LEXIS 702"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Soto",
          "cluster_id": 4401346,
          "cite": [
            "2017 Ohio 4348",
            "93 N.E.3d 204"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Candelario-Santana",
          "cluster_id": 4248720,
          "cite": [
            "834 F.3d 8",
            "2016 U.S. App. LEXIS 15115",
            "2016 WL 4376420"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Jovan'z Smith v. Ken Clark",
          "cluster_id": 3134205,
          "cite": [
            "804 F.3d 983",
            "2015 U.S. App. LEXIS 18335",
            "2015 WL 6387862"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Deal",
          "cluster_id": 2811812,
          "cite": [
            "2015 SD 51",
            "866 N.W.2d 141",
            "2015 S.D. LEXIS 88",
            "2015 WL 3898050"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Williams v. Taylor",
          "cluster_id": 145122,
          "cite": [
            "146 L. Ed. 2d 389",
            "120 S. Ct. 1495",
            "529 U.S. 362",
            "2000 U.S. LEXIS 2837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ornelas v. United States",
          "cluster_id": 118030,
          "cite": [
            "134 L. Ed. 2d 911",
            "116 S. Ct. 1657",
            "517 U.S. 690",
            "1996 U.S. LEXIS 3391"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Yarborough v. Alvarado",
          "cluster_id": 134748,
          "cite": [
            "158 L. Ed. 2d 938",
            "124 S. Ct. 2140",
            "541 U.S. 652",
            "2004 U.S. LEXIS 3843"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
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
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
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
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. State",
          "cluster_id": 2419717,
          "cite": [
            "947 S.W.2d 240",
            "1997 Tex. Crim. App. LEXIS 43",
            "1997 WL 292676"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
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
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Minjarez",
          "cluster_id": 2623400,
          "cite": [
            "81 P.3d 348",
            "2003 WL 22938909"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Howes v. Fields",
          "cluster_id": 623144,
          "cite": [
            "182 L. Ed. 2d 17",
            "132 S. Ct. 1181",
            "565 U.S. 499",
            "2012 U.S. LEXIS 1077",
            "2012 WL 538280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Beverly A. Seymour v. Diane Walker,respondent-Appellee",
          "cluster_id": 770145,
          "cite": [
            "224 F.3d 542",
            "2000 U.S. App. LEXIS 20170",
            "2000 WL 1154017"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ochoa",
          "cluster_id": 2609413,
          "cite": [
            "966 P.2d 442",
            "79 Cal. Rptr. 2d 408",
            "19 Cal. 4th 353"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
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
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tax Analysts v. Internal Revenue Service",
          "cluster_id": 743062,
          "cite": [
            "117 F.3d 607",
            "326 U.S. App. D.C. 53",
            "38 Fed. R. Serv. 3d 849",
            "80 A.F.T.R.2d (RIA) 5152",
            "1997 U.S. App. LEXIS 17044"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herrera v. State",
          "cluster_id": 1872663,
          "cite": [
            "241 S.W.3d 520",
            "2007 Tex. Crim. App. LEXIS 1675",
            "2007 WL 4146707"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Cromer",
          "cluster_id": 2585551,
          "cite": [
            "15 P.3d 243",
            "103 Cal. Rptr. 2d 23",
            "24 Cal. 4th 889"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
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
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Matheny",
          "cluster_id": 2637091,
          "cite": [
            "46 P.3d 453",
            "2002 WL 1009210"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Martin H. Tankleff v. D.A. Senkowski, Superintendent of Clinton Correctional Facility",
          "cluster_id": 751346,
          "cite": [
            "135 F.3d 235",
            "1998 U.S. App. LEXIS 348"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Valdez v. Cockrell",
          "cluster_id": 7102203,
          "cite": [
            "274 F.3d 941",
            "2001 U.S. App. LEXIS 25890",
            "2001 WL 1530153"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Connor v. State",
          "cluster_id": 1960654,
          "cite": [
            "803 So. 2d 598",
            "2001 WL 1013245"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "U. S. Bank N. A. v. Village at Lakeridge, LLC",
          "cluster_id": 4474474,
          "cite": [
            "583 U.S. 387",
            "138 S. Ct. 960",
            "200 L. Ed. 2d 218",
            "2018 U.S. LEXIS 1520"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Francis S. v. Stone",
          "cluster_id": 7080910,
          "cite": [
            "221 F.3d 100",
            "2000 WL 1120432"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Alfred R. Dyer v. Arthur Calderon, Warden, of California State Prison at San Quentin",
          "cluster_id": 756751,
          "cite": [
            "151 F.3d 970",
            "98 Daily Journal DAR 8548",
            "98 Cal. Daily Op. Serv. 6157",
            "1998 U.S. App. LEXIS 18171",
            "1998 WL 448039"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Keohane:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(117982 OR 9433228 OR 9433229) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDMzNzIxNjAwMDAwJnM9MjgwNjM5OCZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28117982+OR+9433228+OR+9433229%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(117982 OR 9433228 OR 9433229)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yMDYmcz0xMjUxNTg5JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28117982+OR+9433228+OR+9433229%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 23,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(117982 OR 9433228 OR 9433229)",
        "reviewed": 47,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 3,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 47,
        "triage_read": 3,
        "triage_snippet_classified": 44
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(117982 OR 9433228 OR 9433229)",
    "indexed_citing_opinions": 979,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 117982,
        "count": 812,
        "count_source": "search"
      },
      {
        "opinion_id": 9433228,
        "count": 187,
        "count_source": "search"
      },
      {
        "opinion_id": 9433229,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1729,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/thompson-v-keohane.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyMTM5OTUmcz0xMDMzMzc1MiZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28117982+OR+9433228+OR+9433229%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 117982,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 105243,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 106284,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 106544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 109221,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 109587,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 109624,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 110256,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 110667,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 110698,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 110954,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111023,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111051,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111112,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111249,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111303,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111373,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 111542,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112137,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112152,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112206,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112387,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112452,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112457,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112477,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112705,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112728,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112845,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 112847,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 117843,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 561218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 574996,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 597894,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 677390,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 687663,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 1121449,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 1160128,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 117982,
        "cited_id": 1175340,
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
    "date_created": "2026-07-05T21:33:22Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:33:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:33:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:37:54Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:33:45Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Thompson v. Keohane

```
<div>
<center><b><span class="citation" data-id="9433228"><a href="/opinion/117982/thompson-v-keohane/" aria-description="Citation for case: Thompson v. Keohane">516 U.S. 99</a></span> (1995)</b></center>
<center><h1>THOMPSON<br>
v.<br>
KEOHANE, WARDEN, et al.</h1></center>
<center>No. 94-6615.</center>
<center><p><b>United States Supreme Court.</b></p></center>
<center>Argued October 11, 1995.</center>
<center>Decided November 29, 1995.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*100</span> Ginsburg, J., delivered the opinion of the Court, in which Stevens, O'Connor, Scalia, Kennedy, Souter, and Breyer, JJ., joined. Thomas, J., filed a dissenting opinion, in which Rehnquist, C. J., joined, <i>post,</i> p. 116.</p>
<p><span class="star-pagination">*101</span> <i>Julie R. O'Sullivan,</i> by appointment of the Court, <span class="citation multiple-matches"><a href="/c/U.%20S./513/1137/">513 U. S. 1137</a></span>, argued the cause and filed briefs for petitioner.</p>
<p><i>Cynthia M. Hora,</i> Assistant Attorney General of Alaska, argued the cause for respondents. With her on the brief was <i>Bruce M. Botelho,</i> Attorney General, <i>pro se.</i><sup>[*]</sup></p>
<p>Justice Ginsburg, delivered the opinion of the Court.</p>
<p>During a two-hour, tape-recorded session at Alaska state trooper headquarters, petitioner Carl Thompson confessed that he killed his former wife. Thompson's confession was placed in evidence at the ensuing Alaska state-court trial, <span class="star-pagination">*102</span> and he was convicted of first-degree murder. Challenging his conviction in a federal habeas corpus proceeding, Thompson maintained that the Alaska troopers gained his confession without according him the warnings <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966), requires: that he could remain silent; that anything he said could be used against him in court; and that he was entitled to an attorney, either retained or appointed.</p>
<p><i>Miranda</i> warnings are due only when a suspect interrogated by the police is "in custody." The state trial and appellate courts determined that Thompson was not "in custody" when he confessed. The statute governing federal habeas corpus proceedings, <span class="citation no-link">28 U. S. C. § 2254</span>, directs that, ordinarily, state-court fact findings "shall be presumed to be correct." § 2254(d). The question before this Court is whether the state-court determination that Thompson was not "in custody" when he confessed is a finding of fact warranting a presumption of correctness, or a matter of law calling for independent review in federal court. We hold that the issue whether a suspect is "in custody," and therefore entitled to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, presents a mixed question of law and fact qualifying for independent review.</p>
<p></p>
<h2>I</h2>
<p>On September 10, 1986, two moose hunters discovered the body of a dead woman floating in a gravel pit lake on the outskirts of Fairbanks, Alaska. The woman had been stabbed 29 times. Notified by the hunters, the Alaska state troopers issued a press release seeking assistance in identifying the body. Thompson called the troopers on September 11 to inform them that his former wife, Dixie Thompson, fit the description in the press release and that she had been missing for about a month. Through a dental examination, the troopers conclusively established that the corpse was Dixie Thompson. On September 15, a trooper called <span class="star-pagination">*103</span> Thompson and asked him to come to headquarters, purportedly to identify personal items the troopers thought belonged to Dixie Thompson. It is now undisputed, however, that the trooper's primary reason for contacting Thompson was to question him about the murder.</p>
<p>Thompson drove to the troopers' headquarters in his pickup truck and, upon arriving, immediately identified the items as Dixie's. He remained at headquarters, however, for two more hours while two unarmed troopers continuously questioned him in a small interview room and tape-recorded the exchange. The troopers did not inform Thompson of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. Although they constantly assured Thompson he was free to leave, they also told him repeatedly that they knew he had killed his former wife. Informing Thompson that execution of a search warrant was underway at his home, and that his truck was about to be searched pursuant to another warrant, the troopers asked questions that invited a confession. App. 43-79.<sup>[1]</sup> Eventually, Thompson told the troopers he killed Dixie.</p>
<p><span class="star-pagination">*104</span> As promised, the troopers permitted Thompson to leave, but impounded his truck. Left without transportation, Thompson accepted the troopers' offer of a ride to his friend's <span class="star-pagination">*105</span> house. Some two hours later, the troopers arrested Thompson and charged him with first-degree murder.</p>
<p>The Alaska trial court, without holding an evidentiary hearing, denied Thompson's motion to suppress his September 15 statements. Tr. 118 (Dec. 12, 1986); Tr. 142 (Mar. 18, 1987). Deciding the motion on the papers submitted, the trial court ruled that Thompson was not "in custody" for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes, therefore the troopers had no obligation to inform him of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. App. 8-9.<sup>[2]</sup> Applying an objective test to resolve the "in custody" question, the court asked whether "`a reasonable person would feel he was not free to leave and break off police questioning.' " <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></i> , at 7 (quoting <i>Hunter</i> v. <i>State,</i> <span class="citation" data-id="9538452"><a href="/opinion/1150403/hunter-v-state/#895" aria-description="Citation for case: Hunter v. State">590 P. 2d 888, 895</a></span> (Alaska 1979)). These features, the court indicated, were key: Thompson arrived at the station in response to a trooper's request; two unarmed troopers in plain clothes questioned him; Thompson was told he was free to go at any time; and he was not arrested at the conclusion of the interrogation. App. 7-8. Although the trial court held that, under the totality of the circumstances, a reasonable person would have felt free to leave, it also observed that the troopers' subsequent actionsreleasing and shortly thereafter arresting Thompsonrendered the question "very close." <i><span class="citation" data-id="9538452"><a href="/opinion/1150403/hunter-v-state/" aria-description="Citation for case: Hunter v. State">Id.</a></span></i> , at 8-9.</p>
<p>After a trial, at which the prosecution played the taperecorded confession, the jury found Thompson guilty of first-degree murder and tampering with evidence. The Court of Appeals of Alaska affirmed Thompson's conviction, concluding, among other things, that the troopers had not placed Thompson "in custody," and therefore had no obligation to give him <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. <i>Thompson</i> v. <i>State,</i>  <span class="star-pagination">*106</span> <span class="citation" data-id="1175340"><a href="/opinion/1175340/thompson-v-state/#131" aria-description="Citation for case: Thompson v. State">768 P. 2d 127, 131</a></span> (Alaska App. 1989).<sup>[3]</sup> The Alaska Supreme Court denied discretionary review. App. 24.</p>
<p>Thompson filed a petition for a writ of habeas corpus in the United States District Court for the District of Alaska. The District Court denied the writ, according a presumption of correctness under <span class="citation no-link">28 U. S. C. § 2254</span>(d) to the state court's conclusion that, when Thompson confessed, he was not yet "in custody" for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes. App. 37. The Court of Appeals for the Ninth Circuit affirmed without publishing an opinion. <span class="citation multiple-matches"><a href="/c/F.%203d/34/1073/">34 F. 3d 1073</a></span> (1994). Based on Circuit precedent,<sup>[4]</sup> the court held that "a state court's determination that a defendant was not in custody for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> is a question of fact entitled to the presumption of correctness under <span class="citation no-link">28 U. S. C. § 2254</span>(d)." App. 41.</p>
<p>Federal Courts of Appeals disagree on the issue Thompson asks us to resolve: whether state-court "in custody" determinations are matters of fact entitled to a presumption of correctness under <span class="citation no-link">28 U. S. C. § 2254</span>(d), or mixed questions of law and fact warranting independent review by the federal habeas court. Compare <i>Feltrop</i> v. <i>Delo,</i> <span class="citation" data-id="9487773"><a href="/opinion/687663/ralph-c-feltrop-v-paul-k-delo/#773" aria-description="Citation for case: Ralph C. Feltrop v. Paul K. Delo">46 F. 3d 766, 773</a></span> (CA8 1995) (applying presumption of correctness), with <i>Jacobs</i> v. <i>Singletary,</i> <span class="citation" data-id="574996"><a href="/opinion/574996/sonia-jacobs-aka-sonia-linder-v-harry-k-singletary-marta-villacorta/#1291" aria-description="Citation for case: Sonia Jacobs A/K/A Sonia Linder v. Harry K. Singletary,...">952 F. 2d 1282, 1291</a></span> (CA11 1992) (conducting independent review). Because uniformity among federal courts is important on questions of this order, we granted certiorari to end the division of authority. 513 U. S. <span class="star-pagination">*107</span> 1126 (1995). We now hold that the <span class="citation no-link">28 U. S. C. § 2254</span>(d) presumption does not apply to "in custody" rulings; accordingly, we vacate the Ninth Circuit's judgment.</p>
<p></p>
<h2>II</h2>
<p>"[I]n-custody interrogation[s]," this Court recognized in <i>Miranda</i> v. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Arizona</a></span></i><i>,</i> place "inherently compelling pressures" on the persons interrogated. <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#467" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 467</a></span>. To safeguard the uncounseled individual's Fifth Amendment privilege against self-incrimination, the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> Court held, suspects interrogated while in police custody must be told that they have a right to remain silent, that anything they say may be used against them in court, and that they are entitled to the presence of an attorney, either retained or appointed, at the interrogation. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></i> , at 444. The Court defined "custodial interrogation" as "questioning initiated by law enforcement officers after a person has been taken into custody or otherwise deprived of his freedom of action in any significant way." <i>Ibid.;</i> see also <i>Oregon</i> v. <i>Mathiason,</i>  <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495</a></span> (1977) <i>(per curiam)</i> (duty to give <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i>  warnings is triggered "only where there has been such a restriction on a person's freedom as to render him `in custody' ") (quoted in <i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 322</a></span> (1994) <i>(per curiam)</i> ). Our task in petitioner Thompson's case is to identify the standard governing federal habeas courts' review of state-court "in custody" determinations.<sup>[5]</sup></p>
<p></p>
<h2>A</h2>
<p>Section 2254 governs federal habeas corpus proceedings instituted by persons in custody pursuant to the judgment of a state court. In such proceedings, § 2254(d) declares, <span class="star-pagination">*108</span> state-court determinations of "a factual issue" "shall be presumed to be correct" absent one of the enumerated exceptions.<sup>[6]</sup> This provision, added in a 1966 amendment, Act of <span class="star-pagination">*109</span> Nov. 2, 1966, <span class="citation no-link">Pub. L. 89-711, 80</span> Stat. 1105-1106, received the Court's close attention in <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104</a></span> (1985). As the <i><span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/" aria-description="Citation for case: Miller v. Fenton">Miller</a></span></i> Court observed, § 2254(d) "was an almost verbatim codification of the standards delineated in <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), for determining when a district court must hold an evidentiary hearing before acting on a habeas petition." <i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#111" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 111</a></span>.<sup>[7]</sup><i>Townsend</i> counseled that, if the habeas petitioner has had in state court "a full and fair hearing . . . resulting in reliable findings," the federal court "ordinarily should . . . accept the facts as found" by the state tribunal. <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#318" aria-description="Citation for case: Townsend v. Sain">372 U. S., at 318</a></span>. Section 2254(d) essentially "elevated [the <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span></i> Court's] exhortation into a mandatory presumption of correctness." <i>Miller</i> , <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#111" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 111-112</a></span>; see also <i><span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/" aria-description="Citation for case: Miller v. Fenton">id.</a></span></i> , at 112 (emphasizing respect appropriately accorded "a coequal state judiciary" and citing <i>Culombe</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422274"><a href="/opinion/106284/culombe-v-connecticut/#605" aria-description="Citation for case: Culombe v. Connecticut">367 U. S. 568, 605</a></span> (1961) (opinion of Frankfurter, J.)).</p>
<p>Just as <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span></i> `s instruction on the respect appropriately accorded state-court fact findings is now captured in the § 2254(d) presumption, so we have adhered to <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span></i> `s definition of the § 2254(d) term "factual issue."<sup>[8]</sup> The <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span></i> Court explained that by "`issues of fact,' " it meant <span class="star-pagination">*110</span> "basic, primary, or historical facts: facts `in the sense of a recital of external events and the credibility of their narrators . . . .' " <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#309" aria-description="Citation for case: Townsend v. Sain">372 U. S., at 309</a></span>, n. 6 (quoting <i>Brown</i> v. <i>Allen,</i>  <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#506" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 506</a></span> (1953) (opinion of Frankfurter, J.)). "Socalled mixed questions of fact and law, which require the application of a legal standard to the historical-fact determinations," the <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span></i> Court added, "are not facts in this sense." <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#309" aria-description="Citation for case: Townsend v. Sain">372 U. S., at 309, n. 6</a></span>.<sup>[9]</sup> In applying § 2254(d), we have reaffirmed that "basic, primary, or historical facts" are the "factual issue[s]" to which the statutory presumption of correctness dominantly relates. See, <i>e. g., </i><i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#112" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 112</a></span> ("[S]ubsidiary factual questions" in alleged involuntariness of confession cases are subject to the § 2254(d) presumption, but "the ultimate question"requiring a "totality of the circumstances" assessment"is a matter for independent federal determination."); <i>Cuyler</i> v. <i>Sullivan,</i> <span class="citation" data-id="9427906"><a href="/opinion/110256/cuyler-v-sullivan/#342" aria-description="Citation for case: Cuyler v. Sullivan">446 U. S. 335, 342</a></span> (1980) ("mixed determination[s] of law and fact" generally are not subject to the § 2254(d) presumption of correctness).</p>
<p>It must be acknowledged, however, "that the Court has not charted an entirely clear course in this area." <i>Miller,</i>  <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#113" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 113</a></span>. In regard to § 2254(d), as in other contexts,<sup>[10]</sup> the proper characterization of a question as one of <span class="star-pagination">*111</span> fact or law is sometimes slippery. See <i>ibid.; </i><i>Wainwright</i> v. <i>Witt,</i> <span class="citation" data-id="9429820"><a href="/opinion/111303/wainwright-v-witt/#429" aria-description="Citation for case: Wainwright v. Witt">469 U. S. 412, 429</a></span> (1985) ("It will not always be easy to separate questions of `fact' from `mixed questions of law and fact' for § 2254(d) purposes . .. ."). Two lines of decisions compose the Court's § 2254(d) law/fact jurisprudence.</p>
<p>In several cases, the Court has classified as "factual issues" within § 2254(d)'s compass questions extending beyond the determination of "what happened." This category notably includes: competency to stand trial (<i>e. g., </i><i>Maggio</i> v. <i>Fulford,</i>  <span class="citation" data-id="9429223"><a href="/opinion/110954/maggio-v-fulford/#117" aria-description="Citation for case: Maggio v. Fulford">462 U. S. 111, 117</a></span> (1983) <i>(per curiam)</i> ); and juror impartiality (<i>e. g., </i><i>Witt</i> , <span class="citation" data-id="9429820"><a href="/opinion/111303/wainwright-v-witt/#429" aria-description="Citation for case: Wainwright v. Witt">469 U. S., at 429</a></span>; <i>Patton</i> v. <i>Yount,</i> <span class="citation" data-id="9429681"><a href="/opinion/111228/patton-v-yount/#1036" aria-description="Citation for case: Patton v. Yount">467 U. S. 1025, 1036</a></span> (1984); <i>Rushen</i> v. <i>Spain,</i> <span class="citation" data-id="9429404"><a href="/opinion/111051/rushen-v-spain/#120" aria-description="Citation for case: Rushen v. Spain">464 U. S. 114, 120</a></span> (1983)). While these issues encompass more than "basic, primary, or historical facts," their resolution depends heavily on the trial court's appraisal of witness credibility and demeanor. See, <i>e. g., </i><i>Witt,</i> <span class="citation" data-id="9429820"><a href="/opinion/111303/wainwright-v-witt/#429" aria-description="Citation for case: Wainwright v. Witt">469 U. S., at 429</a></span> (Although the trial court is "applying some kind of legal standard to what [it] sees and hears," its "predominant function in determining juror bias involves credibility findings whose basis cannot be easily discerned from an appellate record."). This Court has reasoned that a trial court is better positioned to make decisions of this genre, and has therefore accorded the judgment of the jurist-observer "presumptive weight." <i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#114" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 114</a></span> (when an "issue involves the credibility of witnesses and therefore turns largely on an evaluation of demeanor, there are compelling and familiar justifications for leaving the process of applying law to fact to the trial court").</p>
<p>On the other hand, the Court has ranked as issues of law for § 2254(d) purposes: the voluntariness of a confession (<i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#116" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 116</a></span>); the effectiveness of counsel's assistance (<i>Strickland</i> v. <i>Washington,</i> <span class="citation" data-id="9429592"><a href="/opinion/111170/strickland-v-washington/#698" aria-description="Citation for case: Strickland v. Washington">466 U. S. 668, 698</a></span> (1984)); and the potential conflict of interest arising out of an attorney's representation of multiple defendants (<i>Cuyler,</i> <span class="citation" data-id="9427906"><a href="/opinion/110256/cuyler-v-sullivan/#341" aria-description="Citation for case: Cuyler v. Sullivan">446 U. S., at 341-342</a></span>). "What happened" issues in these cases warranted a presumption of correctness, but the Court declared "the ultimate question" outside § 2254(d)'s domain <span class="star-pagination">*112</span> because of its "uniquely legal dimension." <i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#116" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 116</a></span>; see also <i>Sumner</i> v. <i>Mata,</i> <span class="citation" data-id="9428697"><a href="/opinion/110667/sumner-v-mata/#597" aria-description="Citation for case: Sumner v. Mata">455 U. S. 591, 597</a></span> (1982) <i>(per curiam)</i> ("[T]he constitutionality of the pretrial identification procedures used in this case is a mixed question of law and fact that is not governed by § 2254(d)."); <i>Brewer</i>  v. <i>Williams,</i> <span class="citation" data-id="9426723"><a href="/opinion/109624/brewer-v-williams/#397" aria-description="Citation for case: Brewer v. Williams">430 U. S. 387, 397</a></span>, and n. 4, 403-404 (1977) (waiver of Sixth Amendment right to assistance of counsel is not a question of historical fact, but rather requires application of constitutional principles to facts).</p>
<p></p>
<h2>B</h2>
<p>The ultimate "in custody" determination for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes, we are persuaded, fits within the latter class of cases. Two discrete inquiries are essential to the determination: first, what were the circumstances surrounding the interrogation; and second, given those circumstances,<sup>[11]</sup> would a reasonable person have felt he or she was not at liberty to terminate the interrogation and leave. Once the scene is set and the players' lines and actions are reconstructed, the court must apply an objective test to resolve "the ultimate inquiry": "[was] there a `formal arrest or restraint on freedom of movement' of the degree associated with a formal arrest." <i>California</i> v. <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983) <i>(per curiam)</i> (quoting <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 495</a></span>). The first inquiry, all agree, is distinctly factual. State-court findings on these scene- and action-setting questions attract a presumption of correctness under <span class="citation no-link">28 U. S. C. § 2254</span>(d). The second inquiry, however, calls for application of the controlling legal standard to the historical facts. This ultimate <span class="star-pagination">*113</span> determination, we hold, presents a "mixed question of law and fact" qualifying for independent review.</p>
<p>The practical considerations that have prompted the Court to type questions like juror bias and competency as "factual issue[s]," and therefore governed by § 2254(d)'s presumption of correctness, are not dominant here. As this case illustrates, the trial court's superior capacity to resolve credibility issues is not dispositive of the "in custody" inquiry.<sup>[12]</sup> Credibility determinations, as in the case of the alleged involuntariness of a confession, see <i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#112" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 112</a></span>, may sometimes contribute to the establishment of the historical facts and thus to identification of the "totality of the circumstances." But the crucial question entails an evaluation made after determination of those circumstances: if encountered by a "reasonable person," would the identified circumstances add up to custody as defined in <i>Miranda?</i><sup>[13]</sup><span class="star-pagination">*114</span> See <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 442</a></span> (1984) (court must assess "how a reasonable man in the suspect's position would have understood his situation"); cf. <i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#116" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 116-117</a></span> ("[A]ssessments of credibility and demeanor are not crucial to the proper resolution of the ultimate issue of `voluntariness.' ").</p>
<p>Unlike the <i>voir dire</i> of a juror, <i>Patton,</i> <span class="citation" data-id="9429681"><a href="/opinion/111228/patton-v-yount/#1038" aria-description="Citation for case: Patton v. Yount">467 U. S., at 1038</a></span>, or the determination of a defendant's competency, <i>Maggio,</i>  <span class="citation" data-id="9429223"><a href="/opinion/110954/maggio-v-fulford/#117" aria-description="Citation for case: Maggio v. Fulford">462 U. S., at 117</a></span>, which "take[s] place in open court on a full record," <i>Miller,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#117" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 117</a></span>, the trial court does not have a first-person vantage on whether a defendant was "in custody" for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes. See <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#117" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 117</a></span> (police interrogations yielding confessions ordinarily occur, not in court, but in an "inherently more coercive environment"). Furthermore, in fathoming the state of mind of a potential juror or a defendant in order to answer the questions, "Is she free of bias?," "Is he competent to stand trial?," the trial court makes an individual-specific decision, one unlikely to have precedential value.<sup>[14]</sup> In contrast, "in custody" determinations do guide future decisions.<sup>[15]</sup> We thus conclude <span class="star-pagination">*115</span> that once the historical facts are resolved, the state court is not "in an appreciably better position than the federal habeas court to make [the ultimate] determination" of the consistency of the law enforcement officer's conduct with the federal <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning requirement. See <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#117" aria-description="Citation for case: Miller v. Fenton">474 U. S., at 117</a></span>.</p>
<p>Notably, we have treated the "in custody" question as one of law when States complained that their courts had erroneously expanded the meaning of "custodial interrogation." See <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1121" aria-description="Citation for case: California v. Beheler">463 U. S., at 1121-1125</a></span> (summarily reversing California Court of Appeal's judgment that respondent was "in custody"); <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#494" aria-description="Citation for case: Oregon v. Mathiason">429 U. S., at 494-496</a></span> (summarily reversing Oregon Supreme Court's determination that respondent was "in custody"); cf. <i>Oregon</i> v. <i>Hass,</i> <span class="citation" data-id="9426039"><a href="/opinion/109221/oregon-v-hass/#719" aria-description="Citation for case: Oregon v. Hass">420 U. S. 714, 719</a></span> (1975) ("[A] State may not impose . . . greater restrictions [on police activity] as a matter of <i>federal constitutional law</i>  when this Court specifically refrains from imposing them."). It would be anomalous to type the question differently when an individual complains that the state courts had erroneously constricted the circumstances that add up to an "in custody" conclusion.</p>
<p>Classifying "in custody" as a determination qualifying for independent review should serve legitimate law enforcement interests as effectively as it serves to ensure protection of the right against self-incrimination. As our decisions bear out, the law declaration aspect of independent review potentially may guide police, unify precedent, and stabilize the law. See, <i>e. g., </i><i>Berkemer,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#436" aria-description="Citation for case: Berkemer v. McCarty">468 U. S., at 436-439</a></span> (routine traffic stoptypically temporary, brief, and publicdoes not place driver "in custody" for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warning purposes); see also Monaghan, Constitutional Fact Review, <span class="citation no-link">85 Colum. L. Rev. 229</span>, 273-276 (1985) ("norm elaboration occurs best when the Court has power to consider fully a series of closely <span class="star-pagination">*116</span> related situations"; case-by-case elaboration when a constitutional right is implicated may more accurately be described as law declaration than as law application).</p>
<p></p>
<h2>* * *</h2>
<p>Applying § 2254(d)'s presumption of correctness to the Alaska court's "in custody" determination, both the District Court and the Court of Appeals ruled that Thompson was not "in custody" and thus not entitled to <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. Because we conclude that state-court "in custody" determinations warrant independent review by a federal habeas court, the judgment of the United States Court of Appeals for the Ninth Circuit is vacated, and the case is remanded for further proceedings consistent with this opinion.</p>
<p><i>It is so ordered.</i> </p>
<p>Justice Thomas, with whom The Chief Justice joins, dissenting.</p>
<p>Carl Thompson murdered his ex-wife, stabbing her 29 times. He then wrapped her body in chains and a bedspread and tossed the corpse into a water-filled gravel pit. As part of their investigation, police officers in Fairbanks, Alaska, questioned Thompson about his role in the murder, and Thompson confessed. Thompson was repeatedly told that he could leave the interview and was, in fact, permitted to leave at the close of questioning. I believe that the Alaska trial judgewho first decided this question almost a decade agowas in a far better position than a federal habeas court to determine whether Thompson was "in custody" for purposes of <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). So long as that judgment finds fair support in the record, I would presume that it is correct. I dissent.</p>
<p>To determine whether a person is "in custody" under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>,</i> "a court must examine all of the circumstances surrounding the interrogation, but `the ultimate inquiry is simply whether there [was] a "formal arrest or restraint on <span class="star-pagination">*117</span> freedom of movement" of the degree associated with a formal arrest.' " <i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 322</a></span> (1994) (quoting <i>California</i> v. <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1125" aria-description="Citation for case: California v. Beheler">463 U. S. 1121, 1125</a></span> (1983) <i>(per curiam)</i><i>,</i> quoting in turn <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495</a></span> (1977) <i>(per curiam)</i> ). "`[T]he only relevant inquiry is how a reasonable man in the suspect's position would have understood his situation.' " <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/" aria-description="Citation for case: Stansbury v. California">511 U. S., at 324</a></span> (quoting <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#442" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 442</a></span> (1984)).</p>
<p>I agree with the majority that a legal standard must be applied by a state trial judge in making the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody inquiry. In light of our more recent decisions applying § 2254(d), however, I do not agree that the standards articulated in <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293</a></span> (1963), overruled in part by <i>Keeney</i> v. <i>Tamayo-Reyes,</i> <span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/#5" aria-description="Citation for case: Keeney v. Tamayo-Reyes">504 U. S. 1, 5</a></span> (1992), for distinguishing factual issues from mixed questions of law and fact, dictate a result either way in this case. See, <i>e. g., </i><i>Wainwright</i> v. <i>Witt,</i> <span class="citation" data-id="9429820"><a href="/opinion/111303/wainwright-v-witt/#429" aria-description="Citation for case: Wainwright v. Witt">469 U. S. 412, 429</a></span> (1985) (juror bias determination is a question of fact, even though "[t]he trial judge is of course applying some kind of legal standard to what he sees and hears"); <i>Patton</i> v. <i>Yount,</i> <span class="citation" data-id="9429681"><a href="/opinion/111228/patton-v-yount/#1037" aria-description="Citation for case: Patton v. Yount">467 U. S. 1025, 1037, n. 12</a></span> (1984) (juror bias is a question of fact although "[t]here are, of course, factual and legal questions to be considered in deciding whether a juror is qualified"). Because the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody issue "falls somewhere between a pristine legal standard and a simple historical fact," we must decide, "as a matter of the sound administration of justice, [which] judicial actor is better positioned . . . to decide the issue in question." <i>Miller</i> v. <i>Fenton,</i> <span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/#114" aria-description="Citation for case: Miller v. Fenton">474 U. S. 104, 114</a></span> (1985).</p>
<p>The state trial judge is, in my estimation, the bestpositioned judicial actor to decide the relatively straightforward and fact-laden question of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody. See <i>California</i> v. <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/#1128" aria-description="Citation for case: California v. Beheler"><i>Beheler, supra,</i> at 1128</a></span> (Stevens, J., dissenting) (state "courts are far better equipped than we are to assess the police practices that are highly relevant to the determination whether particular circumstances amount to custodial <span class="star-pagination">*118</span> interrogation"). In making the custody determination, the state trial judge must consider a complex of diverse and case-specific factors in an effort to gain an overall sense of the defendant's situation at the time of the interrogation. These factors include, at a minimum, the location, timing, and length of the interview, the nature and tone of the questioning, whether the defendant came to the place of questioning voluntarily, the use of physical contact or physical restraint, and the demeanor of all of the key players, both during the interview and in any proceedings held in court. In assessing all of these facts, the state trial judge will often take live testimony, consider documentary evidence, and listen to audiotapes or watch videotapes of the interrogation. Assessments of credibility and demeanor are crucial to the ultimate determination, for the trial judge will often have to weigh conflicting accounts of what transpired. The trial judge is also likely to draw inferences, which are similarly entitled to deference, from "physical or documentary evidence or . . . other facts." <i>Anderson</i> v. <i>Bessemer City,</i> <span class="citation" data-id="9429949"><a href="/opinion/111373/anderson-v-city-of-bessemer-city/#574" aria-description="Citation for case: Anderson v. City of Bessemer City">470 U. S. 564, 574</a></span> (1985). The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody inquiry is thus often a matter of "shades and degrees," <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/#712" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680, 712</a></span> (1993) (O'Connor, J., concurring in part and dissenting in part), that requires the state trial judge to make any number of "`fact-intensive, close calls.' " <i>Cooter &amp; Gell</i> v. <i>Hartmarx Corp.,</i> <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/#404" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp.">496 U. S. 384, 404</a></span> (1990) (citation omitted).</p>
<p>The majority is quite right that the test contains an objective componenthow a "reasonable man in the suspect's position would have understood his situation," <i>Stansbury</i> v. <i>California, supra,</i> at 324but this alone cannot be dispositive of whether the determination should be reviewed deferentially. See, <i>e. g., </i><i>Cooter &amp; Gell</i> v. <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/#402" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp."><i>Hartmarx Corp., supra,</i>  at 402</a></span> (Rule 11 and negligence determinations, both of which involve objective tests, are subject to deferential review). "[T]he line between pure facts . . . and . . . the application to them of a legal standard that is as non-technicalas commonsensicalas reasonableness is a faint one." <i>United</i>  <span class="star-pagination">*119</span> <i>States</i> v. <i>Humphrey,</i> <span class="citation" data-id="9487284"><a href="/opinion/677390/medicare-medicaid-guide-p-42636-united-states-of-america-v-charles/#559" aria-description="Citation for case: Medicare &amp; Medicaid Guide P 42,636 United States of...">34 F. 3d 551, 559</a></span> (CA7 1994) (Posner, C. J., concurring). It distorts reality to say that all of the subtle, factbound assessments that go into determining what it was like to be in the suspect's shoes simply go out the window when it comes time for the "ultimate inquiry," <i>ante,</i>  at 112, of how a reasonable person would have assessed the situation. "The state trial court [is] in the unique position, after observing [the defendant] and listening to the evidence presented at trial, to determine whether a reasonable person in [defendant's] position would have felt free to leave the police station." <i>Purvis</i> v. <i>Dugger,</i> <span class="citation" data-id="9481615"><a href="/opinion/561218/john-gordon-purvis-v-richard-l-dugger/#1419" aria-description="Citation for case: John Gordon Purvis v. Richard L. Dugger">932 F. 2d 1413, 1419</a></span> (CA11 1991), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./503/940/">503 U. S. 940</a></span> (1992). It is only in light of these case-specific determinations that the reasonable person test can be meaningfully applied. See <i>Cooter &amp; Gell</i> v. <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/#402" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp."><i>Hartmarx Corp., supra,</i> at 402</a></span> ("Familiar with the issues and litigants, the [trial] court is better situated than the court of appeals to marshal the pertinent facts and apply the factdependent legal standard").</p>
<p>For these reasons, I have no doubt that the state trier of fact is best situated to put himself in the suspect's shoes, and consequently is in a better position to determine what it would have been like for a reasonable man to be in the suspect's shoes. Federal habeas courts, often reviewing the cold record as much as a decade after the initial determination, are in an inferior position to make this assessment. Though some of the state court's factual determinations may, perhaps, be reflected on the record, many of the case-specific assessments that underlie the state trial judge's ultimate determination are subtle, difficult to reduce to writing, and unlikely to be preserved in any meaningful way for review on appeal. "State courts are fully qualified to identify constitutional error and evaluate its prejudicial effect." <i>Brecht</i> v. <i>Abrahamson,</i> <span class="citation" data-id="9432778"><a href="/opinion/112845/brecht-v-abrahamson/#636" aria-description="Citation for case: Brecht v. Abrahamson">507 U. S. 619, 636</a></span> (1993). "Absent indication to the contrary, state courts should be presumed to have applied federal law as faithfully as federal courts." <i>Withrow</i>  v. <i>Williams, supra,</i> at 723 (Scalia, J., concurring in part and <span class="star-pagination">*120</span> dissenting in part). We insult our colleagues in the States when we imply, as we do today, that state judges are not sufficiently competent and reliable to make a decision as straightforward as whether a person was in custody for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i> See 507 U. S., at 714 (O'Connor, J., concurring in part and dissenting in part) ("We can depend on law enforcement officials to administer <i>[Miranda]</i> warnings in the first instance and the state courts to provide a remedy when law enforcement officers err").<sup>[1]</sup></p>
<p>I also see no reason to remand this case to the Ninth Circuit for further analysis. There is no dispute that Thompson came to the police station voluntarily. There is no dispute that he was repeatedly told he could leave the police station at any time. And it is also clear that he left the police station freely at the end of the interrogation. In <i>California</i> v. <i>Beheler,</i> <span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">463 U. S. 1121</a></span> (1983) <i>(per curiam)</i><i>,</i> we held that a person is not in custody if "the suspect is not placed under arrest, voluntarily comes to the police station, and is allowed to leave unhindered by police after a brief interview." <i><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">Ibid.</a></span></i>  And in <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492</a></span> (1977) <i>(per curiam)</i><i>,</i> we found it "clear" that the defendant was not in <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> custody where he "came voluntarily to the police <span class="star-pagination">*121</span> station, . . . was immediately informed that he was not under arrest," and "[a]t the close of a<sup>[1]</sup>20442-hour interview . . . did in fact leave the police station without hindrance." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#495" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 495</a></span>; see also <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">ibid.</a></span></i> ("Nor is the requirement of warnings to be imposed simply because the questioning takes place in the station house, or because the questioned person is one whom the police suspect"). Because Thompson cannot establish a <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> violation even under <i>de novo</i> review, I would resolve that question now, and avoid putting the State of Alaska to the uncertainty and expense of defending for the sixth time in nine years an eminently reasonable judgment secured against a confessed murderer.<sup>[2]</sup></p>
<p>I respectfully dissent.</p>
<h2>NOTES</h2>
<p>[*]   Briefs of <i>amici curiae</i> urging affirmance were filed for the State of Florida et al. by <i>Robert A. Butterworth,</i> Attorney General of Florida, and <i>Carolyn J. Mosley,</i> Assistant Attorney General, <i>Grant Woods,</i> Attorney General of Arizona, <i>Daniel E. Lungren,</i> Attorney General of California, <i>Gale A. Norton,</i> Attorney General of Colorado, <i>John M. Bailey,</i> Chief State's Attorney of Connecticut, <i>M. Jane Brady,</i> Attorney General of Delaware, <i>Margery S. Bronster,</i> Attorney General of Hawaii, <i>Alan G. Lance,</i>  Attorney General of Idaho, <i>Pamela Carter,</i> Attorney General of Indiana, <i>Tom Miller,</i> Attorney General of Iowa, <i>Carla J. Stovall,</i> Attorney General of Kansas, <i>Chris Gorman,</i> Attorney General of Kentucky, <i>Richard P. Ieyoub,</i> Attorney General of Louisiana, <i>Andrew Ketterer,</i> Attorney General of Maine, <i>J. Joseph Curran, Jr.,</i> Attorney General of Maryland, <i>Frank J. Kelley,</i> Attorney General of Michigan, <i>Hubert H. Humphrey III,</i> Attorney General of Minnesota, <i>Mike Moore,</i> Attorney General of Mississippi, <i>Jerimiah W. "Jay" Nixon,</i> Attorney General of Missouri, <i>Joseph P. Mazurek,</i> Attorney General of Montana, <i>Don Stenberg,</i> Attorney General of Nebraska, <i>Frankie Sue Del Papa,</i> Attorney General of Nevada, <i>Jeffrey R. Howard,</i> Attorney General of New Hampshire, <i>Deborah T. Poritz,</i> Attorney General of New Jersey, <i>Dennis C. Vacco,</i> Attorney General of New York, <i>Michael F. Easley,</i> Attorney General of North Carolina, <i>Betty D. Montgomery,</i> Attorney General of Ohio, <i>Drew Edmondson,</i> Attorney General of Oklahoma, <i>Ernest D. Preate, Jr.,</i> Attorney General of Pennsylvania, <i>Charles Molony Condon,</i> Attorney General of South Carolina, <i>Mark Barnette,</i> Attorney General of South Dakota, <i>Charles W. Burson,</i> Attorney General of Tennessee, <i>Dan Morales,</i> Attorney General of Texas, <i>Jan Graham,</i> Attorney General of Utah, <i>Jeffrey L. Amestoy,</i> Attorney General of Vermont, <i>James S. Gilmore III,</i> Attorney General of Virginia, and <i>Christine O. Gregoire,</i> Attorney General of Washington; and for the Criminal Justice Legal Foundation by <i>Kent S. Scheidegger.</i> </p>
<p>[1]  These passages from the transcript of the tape-recorded interrogation indicate the tenor of the questioning:
</p>
<p>"Q Do you knowof course, I don't mean to take up a lot of your time, youyou can leave any time that you want to, if you've got something else going on.</p>
<p>"A Oh no (indiscernible) around here, no.</p>
<p>"Q I know we called you and probably woke you up and. . . .</p>
<p>"A No, I was just laying there.</p>
<p>"Q Okay. But you know, you can go any time you want to. We got ayou know, we're trying totrying to crack on this thing, and II don't imagine it's any secret to you that there are some of youryour friends or associates who have been kind of calling up and saying, you know, they've been pointing at you. . . .</p>
<p>"A Yeah, that (indiscernible) guy you know and we've been friends for ten years, you know, and this guy is starting to say stuff that I never even said. . . ." App. 44-45.</p>
<p>"Q . . . And I'm willing to work with you on this thing to make the best of a bad situation. I can't tell you that this isn't a bad situation. I mean you're free to get up and walk out of here now andand never talk to me again. But what I'm telling you now is this is probably the last chance we'll have tofor you to say something that other people are gonna believe because let's justlet's just say that there's enough (indiscernible) here already that we canwe can prove conclusively beyond a reasonable doubt thatthat you were responsible for this thingthis thing. Well really there's a lot that she's responsible for, but you're the guy that's stuck with the problem. . . .</p>
<p>"A I've already told you the story.</p>
<p>"Q . . . Well you haven't told me the critical part and you haven't told me the part about where Dixie gets killed.</p>
<p>"A And I don't know about that. That's your guys' job. You're supposed to know that.</p>
<p>"Q Well like I told you, we know the who, the where, the when, the how. The thing we don't know is the why. And that'sthat's the thing we've got to kind of get straight here today between you and I. See I know that you did this thing. There'sthere's no question in my mind about that. I can see it. I can see it when I'm looking at you. And I know that you care about Dixie. I mean this isn't something that you wanted to happen. . . .</p>
<p>. . . . .</p>
<p>"Q . . . I think that now it's the time for you to come honest about this thing, because if you turn around later and try to. . . .</p>
<p>"A I am being honest about it.</p>
<p>"Q No, you haven't. You told part of the truth and you told a lot of it, but you haven't told all of it. . . . I mean youryou're not probably lying directly to me, but you're lying by omission . . . . I can tell you that right now there's a search warrant being served out at [your home] and a search warrant for your truck is gonna be served and we've got a forensic expert up fromfrom Anchorage . . . .</p>
<p>"A Huh.</p>
<p>"Q . . . And I don't believe that you're a bad person. I really don't. . . . [W]hat happened here was never planned, what happened here was one of these things that just happen. . . . And when it happened you're stuck with thisI mean you're stuck with a hell of a mess now. She's gotshe's finally got you into more trouble than she can possibly imagine. I mean she's brought this thing on you. She causes that. . . . I mean I don't know whether she started the thing by grabbing the knife and saying she was gonna (indiscernible) at you and it got turned around or just what happened. I mean I don't know those things. . . ." <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Id.</a></span></i> , at 49-51.</p>
<p>[2]  The trial court also rejected Thompson's contention that his confession was involuntary. On both direct and habeas review, Thompson unsuccessfully asserted the involuntariness of his confession. His petition to this Court, however, does not present that issue.</p>
<p>[3]  It is unclear in this case what deference the Alaska appellate court accorded to the trial court's conclusion that petitioner was not "in custody"; in later decisions, the Alaska Court of Appeals reviewed the trial courts' "in custody" determinations for "clear error." See <i>Higgins</i> v. <i>State,</i> <span class="citation" data-id="1160128"><a href="/opinion/1160128/higgins-v-state/#971" aria-description="Citation for case: Higgins v. State">887 P. 2d 966, 971</a></span> (Alaska App. 1994); <i>McKillop</i> v. <i>State,</i> <span class="citation" data-id="1121449"><a href="/opinion/1121449/mckillop-v-state/#361" aria-description="Citation for case: McKillop v. State">857 P. 2d 358, 361</a></span> (Alaska App. 1993).</p>
<p>[4]  The panel relied on <i>Krantz</i> v. <i>Briggs,</i> <span class="citation" data-id="597894"><a href="/opinion/597894/richard-h-krantz-v-phillip-briggs-superintendent-cook-inlet-pretrial/#964" aria-description="Citation for case: Richard H. Krantz v. Phillip Briggs, Superintendent, Cook...">983 F. 2d 961, 964</a></span> (CA9 1993), which held that state-court "in custody" determinations warrant a presumption of correctness under § 2254(d) if the state court made factfindings after a hearing on the merits.</p>
<p>[5]  Claims that state courts have incorrectly decided <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> issues, as <i>Withrow</i> v. <i>Williams,</i> <span class="citation" data-id="9432786"><a href="/opinion/112847/withrow-v-williams/" aria-description="Citation for case: Withrow v. Williams">507 U. S. 680</a></span> (1993), confirms, are appropriately considered in federal habeas review.</p>
<p>[6]  Section 2254(d) lists eight exceptions to the presumption of correctness. In full, <span class="citation no-link">28 U. S. C. § 2254</span>(d) reads:
</p>
<p>"In any proceeding instituted in a Federal court by an application for a writ of habeas corpus by a person in custody pursuant to the judgment of a State court, a determination after a hearing on the merits of a factual issue, made by a State court of competent jurisdiction in a proceeding to which the applicant for the writ and the State or an officer or agent thereof were parties, evidenced by a written finding, written opinion, or other reliable and adequate written indicia, shall be presumed to be correct, unless the applicant shall establish or it shall otherwise appear, or the respondent shall admit</p>
<p>"(1) that the merits of the factual dispute were not resolved in the State court hearing;</p>
<p>"(2) that the factfinding procedure employed by the State court was not adequate to afford a full and fair hearing;</p>
<p>"(3) that the material facts were not adequately developed at the State court hearing;</p>
<p>"(4) that the State court lacked jurisdiction of the subject matter or over the person of the applicant in the State court proceeding;</p>
<p>"(5) that the applicant was an indigent and the State court, in deprivation of his constitutional right, failed to appoint counsel to represent him in the State court proceeding;</p>
<p>"(6) that the applicant did not receive a full, fair, and adequate hearing in the State court proceeding; or</p>
<p>"(7) that the applicant was otherwise denied due process of law in the State court proceeding;</p>
<p>"(8) or unless that part of the record of the State court proceeding in which the determination of such factual issue was made, pertinent to a determination of the sufficiency of the evidence to support such factual determination, is produced as provided for hereinafter, and the Federal court on a consideration of such part of the record as a whole concludes that such factual determination is not fairly supported by the record: "And in an evidentiary hearing in the proceeding in the Federal court, when due proof of such factual determination has been made, unless the existence of one or more of the circumstances respectively set forth in paragraphs numbered (1) to (7), inclusive, is shown by the applicant, otherwise appears, or is admitted by the respondent, or unless the court concludes pursuant to the provisions of paragraph numbered (8) that the record in the State court proceeding, considered as a whole, does not fairly support such factual determination, the burden shall rest upon the applicant to establish by convincing evidence that the factual determination by the State court was erroneous."</p>
<p>[7]  The list of circumstances warranting an evidentiary hearing in a federal habeas proceeding set out in H. R. Rep. No. 1384, 88th Cong., 2d Sess., 25 (1964), is similar to the list set out in <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/#313" aria-description="Citation for case: Townsend v. Sain">372 U. S. 293, 313</a></span> (1963). The legislative history further indicates that the House Judiciary Committee, in framing its recommendations, was mindful of the Court's recent precedent, including <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span>.</i> H. R. Rep. No. 1384, <i>supra,</i> at 24-25. See also 1 J. Liebman &amp; R. Hertz, Federal Habeas Corpus Practice and Procedure § 20.1a, pp. 537-538 (2d ed. 1994) (description of interplay between habeas statute and <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span></i> ).</p>
<p>[8]  <i>Keeney</i> v. <i>Tamayo-Reyes,</i> <span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/" aria-description="Citation for case: Keeney v. Tamayo-Reyes">504 U. S. 1</a></span> (1992), partially overruled <i><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">Townsend</a></span></i> on a point not relevant here; <i><span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/" aria-description="Citation for case: Keeney v. Tamayo-Reyes">Keeney</a></span></i> held that a "cause-andprejudice" standard, rather than the "deliberate by-pass" standard, is the correct standard for excusing a habeas petitioner's failure to develop a material fact in state-court proceedings. <span class="citation" data-id="9432524"><a href="/opinion/112728/keeney-v-tamayo-reyes/#5" aria-description="Citation for case: Keeney v. Tamayo-Reyes">504 U. S., at 5-6</a></span>.</p>
<p>[9]  See also <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#507" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 507</a></span> (1953) (opinion of Frankfurter, J.) ("Where the ascertainment of the historical facts does not dispose of the claim but calls for interpretation of the legal significance of such facts, the District Judge must exercise his own judgment on this blend of facts and their legal values. Thus, so-called mixed questions or the application of constitutional principles to the facts as found leave the duty of adjudication with the federal judge.") (citation omitted).</p>
<p>[10]  See, <i>e. g., </i><i>Cooter &amp; Gell</i> v. <i>Hartmarx Corp.</i> , <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/#401" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp.">496 U. S. 384, 401</a></span> (1990) (observing in regard to appellate review of sanctions imposed under Fed. Rule Civ. Proc. 11: "The Court has long noted the difficulty of distinguishing between legal and factual issues."); <i>Pullman-Standard</i> v. <i>Swint,</i> <span class="citation" data-id="9428745"><a href="/opinion/110698/pullman-standard-v-swint/#288" aria-description="Citation for case: Pullman-Standard v. Swint">456 U. S. 273, 288</a></span> (1982) (acknowledging, in relation to appellate review of intent determinations in Title VII cases, "the vexing nature of the distinction between questions of fact and questions of law").</p>
<p>[11]  The "totality of the circumstances" cast of the "in custody" determination, contrary to respondents' suggestions, does not mean deferential review is in order. See, <i>e. g., </i><i>Miller</i> v.<span class="citation" data-id="9842069"><a href="/opinion/111542/miller-v-fenton/" aria-description="Citation for case: Miller v. Fenton"><i>Fenton,</i></a></span> 474 U. S.104, 117 (1985) (state-court determination "whether, under the totality of the circumstances, the confession was obtained in a manner consistent with the Constitution" qualifies for independent review by federal habeas court).</p>
<p>[12]  As earlier observed, see <i>supra,</i> at 105, the trial court decided Thompson's motion to suppress his September 15 statements on the papers submitted without holding an evidentiary hearing.</p>
<p>[13]  Respondents observe that "reasonable person" assessments, most prominently to gauge negligence in personal injury litigation, fall within the province of fact triers. See, <i>e. g., </i><i>Cooter &amp; Gell</i> , <span class="citation" data-id="9432057"><a href="/opinion/112457/cooter-gell-v-hartmarx-corp/#402" aria-description="Citation for case: Cooter &amp; Gell v. Hartmarx Corp.">496 U. S., at 402</a></span> (negligence determinations "generally reviewed deferentially"); <i>McAllister</i> v. <i>United States,</i> <span class="citation" data-id="105243"><a href="/opinion/105243/mcallister-v-united-states/#20" aria-description="Citation for case: McAllister v. United States">348 U. S. 19, 20-23</a></span> (1954) (District Court finding of negligence was not "clearly erroneous"); 9A C. Wright &amp; A. Miller, Federal Practice and Procedures § 2590 (2d ed. 1995). Traditionally, our legal system has entrusted negligence questions to jurors, inviting them to apply community standards. See W. Keeton, D. Dobbs, R. Keeton, &amp; D. Owen, Prosser and Keeton on Law of Torts § 37, pp. 235-237 (5th ed. 1984). For that reason, "[t]he question usually is said to be one of fact," although "it should be apparent that the function of the jury in fixing the standard differs from that of the judge only in that it cannot be reduced to anything approaching a definite rule." <i>Id.</i> , at 237.
</p>
<p>Judges alone make "in custody" assessments for <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> purposes, and they do so with a view to identifying recurrent patterns, and advancing uniform outcomes. If they cannot supply "a definite rule," they nonetheless can reduce the area of uncertainty. See, <i>e. g., </i><i>Illinois</i> v. <i>Perkins,</i> <span class="citation" data-id="9432050"><a href="/opinion/112452/illinois-v-perkins/#296" aria-description="Citation for case: Illinois v. Perkins">496 U. S. 292, 296</a></span> (1990) (<i>Miranda</i> warnings not required prior to questioning of incarcerated individual by undercover agent because suspect, unaware of police presence, is not coerced); <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/#436" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420, 436-439</a></span> (1984) (nature of suspected offense is irrelevant to duty to administer <i>Miranda</i> warnings); <i>Oregon</i> v. <i>Mathiason,</i> <span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/#495" aria-description="Citation for case: Oregon v. Mathiason">429 U. S. 492, 495-496</a></span> (1977) <i>(per curiam)</i> (fact that interrogation occurs at police station does not, in itself, require <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings).</p>
<p>[14]  In other contexts, we have similarly concluded that the likely absence of precedential value cuts against requiring plenary appellate review of a district court's determination. For example, in <i>Cooter &amp; Gell</i> v. <i>Hartmarx Corp</i><i>.,</i> a decision confirming that the abuse-of-discretion standard applies to appellate review of sanctions under Federal Rule of Civil Procedure 11, we observed that plenary review would likely "`fail to produce the normal law-clarifying benefits that come from an appellate decision on a question of law . . . .' " 496 U. S., at 404 (quoting <i>Pierce</i> v. <i>Underwood,</i>  <span class="citation" data-id="9431437"><a href="/opinion/112137/pierce-v-underwood/#561" aria-description="Citation for case: Pierce v. Underwood">487 U. S. 552, 561</a></span> (1988)).</p>
<p>[15]  See, <i>e. g., </i><i>Stansbury</i> v. <i>California,</i> <span class="citation" data-id="9432992"><a href="/opinion/117843/stansbury-v-california/#322" aria-description="Citation for case: Stansbury v. California">511 U. S. 318, 322-324</a></span> (1994) <i>(per curiam)</i> (review of precedent demonstrated a "well settled" principle: officer's undisclosed, subjective belief that person questioned is a suspect is irrelevant to objective "in custody" determination); <i>Pennsylvania</i>  v. <i>Bruder,</i> <span class="citation" data-id="9431478"><a href="/opinion/112152/pennsylvania-v-bruder/#11" aria-description="Citation for case: Pennsylvania v. Bruder">488 U. S. 9, 11</a></span> (1988) <i>(per curiam)</i> (summary reversal appropriate because state-court decision was contrary to rule of <i>Berkemer</i> v. <i>McCarty,</i> <span class="citation" data-id="9429728"><a href="/opinion/111249/berkemer-v-mccarty/" aria-description="Citation for case: Berkemer v. McCarty">468 U. S. 420</a></span> (1984), that ordinary traffic stops do not involve "custody" for purposes of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> ).</p>
<p>[1]  The majority believes that federal oversight of state-court custody judgments is necessary to "advanc[e] uniform outcomes," and when that cannot be achieved, to"reduce the area of uncertainty." <i>Ante,</i> at 113, n. 13. While uniformity of outcome is a virtue worth pursuing generally, we determined in a line of cases beginning with <i>Teague</i> v. <i>Lane</i> , <span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/" aria-description="Citation for case: Teague v. Lane">489 U. S. 288</a></span> (1989) (plurality opinion), that on habeas, uniformity must give way to concerns of comity and finality. See <span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/#310" aria-description="Citation for case: Teague v. Lane"><i>id.,</i> at 310</a></span> ("The `costs imposed upon the State[s] by retroactive application of new rules of constitutional law on habeas corpus . . . generally far outweigh the benefits of this application' ") (quoting <i>Solem</i> v. <i>Stumes,</i> <span class="citation" data-id="9429516"><a href="/opinion/111112/solem-v-stumes/#654" aria-description="Citation for case: Solem v. Stumes">465 U. S. 638, 654</a></span> (1984) (Powell, J., concurring in judgment)). Federal habeas review is not the time for fine-tuning constitutional rules of criminal procedure at the expense of valid state convictions based on reasonable applications of then-existing law. See <i>Butler</i> v. <i>McKellar,</i> <span class="citation" data-id="9431941"><a href="/opinion/112387/butler-v-mckellar/#414" aria-description="Citation for case: Butler v. McKellar">494 U. S. 407, 414</a></span> (1990) ("The `new rule' principle . . . validates reasonable, good-faith interpretations of existing precedents made by state courts").</p>
<p>[1]  To the extent Thompson's claim has any merit at all, it seems certain that relief is barred by our decision in <i>Teague</i> v. <span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/#301" aria-description="Citation for case: Teague v. Lane"><i>Lane, supra,</i> at 301, 310</a></span> (plurality opinion), and its progeny. "The interests in finality, predictability, and comity underlying our new rule jurisprudence may be undermined to an equal degree by the invocation of a rule that was not dictated by precedent as by the application of an old rule in a manner that was not dictated by precedent." <i>Stringer</i> v. <i>Black,</i> <span class="citation" data-id="9432489"><a href="/opinion/112705/stringer-v-black/#228" aria-description="Citation for case: Stringer v. Black">503 U. S. 222, 228</a></span> (1992). In this case, it is clear that "granting the relief sought would create a new rule because the prior decision is applied in a novel setting, thereby extending the precedent." <i><span class="citation" data-id="9432489"><a href="/opinion/112705/stringer-v-black/" aria-description="Citation for case: Stringer v. Black">Ibid.</a></span></i> In light of <i><span class="citation" data-id="9429374"><a href="/opinion/111023/california-v-beheler/" aria-description="Citation for case: California v. Beheler">Beheler</a></span></i> and <i><span class="citation" data-id="9426651"><a href="/opinion/109587/oregon-v-mathiason/" aria-description="Citation for case: Oregon v. Mathiason">Mathiason</a></span>,</i> the State's judgment was, at the very least, reasonable. And "<span class="citation" data-id="9431581"><a href="/opinion/112206/teague-v-lane/" aria-description="Citation for case: Teague v. Lane"><i>Teague</i></a></span> insulates on habeas review the state courts' ` "reasonable, good-faith interpretations of existing precedents."` " <i>Wright</i> v. <i>West,</i> <span class="citation" data-id="9432630"><a href="/opinion/112771/wright-v-west/#292" aria-description="Citation for case: Wright v. West">505 U. S. 277, 292, n. 8</a></span> (1992) (opinion of Thomas, J.) (quoting <i>Sawyer</i> v. <i>Smith,</i> <span class="citation" data-id="9432105"><a href="/opinion/112477/sawyer-v-smith/#234" aria-description="Citation for case: Sawyer v. Smith">497 U. S. 227, 234</a></span> (1990), quoting in turn <i>Butler</i> v. <span class="citation" data-id="9431941"><a href="/opinion/112387/butler-v-mckellar/#414" aria-description="Citation for case: Butler v. McKellar"><i>McKellar, supra,</i> at 414</a></span>).</p>

</div>
```

---

## GROUP: content/cases/Thompson v. Louisiana.md  (`case`, 5 assertions)

### content_page

```
---
title: "Thompson v. Louisiana"
type: case
citation: "469 U.S. 17 (1984)"
parallel_cite: "105 S. Ct. 409; 83 L. Ed. 2d 246"
neutral_cite: 1984 U.S. LEXIS 161
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-11-26
docket: 83-6775
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1985-01-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Thompson v. Louisiana
  varies_by_point: false
  scope_note: "Per curiam (announced January 21, 1985; reported at 469 U.S. 17, O.T. 1984). Reaffirms Mincey v. Arizona; no negative treatment."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111282/thompson-v-louisiana/"
  cluster_id: 111282
  opinion_id: 111282
  identity_checked: true
homes:
  - page: "[[Securing the Scene]]"
    role: "Related (cross-doctrine)"
related: ["[[Mincey v. Arizona]]", "[[Flippo v. West Virginia]]", "[[Michigan v. Tyler]]"]
aliases: []
tags: ["case", "fourth-amendment", "crime-scene", "warrant-requirement", "homicide", "emergency-aid", "plain-view"]
holding: "There is no 'murder-scene exception' to the warrant requirement; a warrantless two-hour general search of a homicide scene in a private home is unreasonable, even though shorter than the four-day search in Mincey, and the victim's call for help does not diminish her expectation of privacy."
lake:
  record_id: Thompson v. Louisiana
  status: verified
  projected_at: 2026-07-10
---

# Thompson v. Louisiana

*469 U.S. 17 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
The petitioner shot her husband, then attempted suicide, then changed her mind and telephoned her daughter, who called the police. Police arrived, found the husband dead and the petitioner injured, transported her to the hospital, and conducted a brief "victim-or-suspect" search. Homicide investigators then arrived and conducted a two-hour general, warrantless search of the home — the same day as the killing — seizing evidence used against her. The Louisiana courts upheld the search, distinguishing *[[Mincey v. Arizona|Mincey]]* and finding a diminished expectation of privacy.

## Issue
Whether a warrantless two-hour general search of a private home that is a recent homicide scene falls within an exception to the warrant requirement.

## Rule
No — there is no murder-scene exception: in *[[Mincey v. Arizona|Mincey]]* "we unanimously rejected the contention that one of the exceptions to the Warrant Clause is a 'murder scene exception,'" and "we held that 'the "murder scene exception" . . . is inconsistent with the Fourth and Fourteenth Amendments — that the warrantless search of Mincey's apartment was not constitutionally permissible simply because a homicide had recently occurred there.' . . . *Mincey* is squarely on point in the instant case." — 469 U.S. at 21. ^pin-21

The brevity of the search did not save it: "A 2-hour general search remains a significant intrusion on petitioner's privacy and therefore may only be conducted subject to the constraints — including the warrant requirement — of the Fourth Amendment." — *Id.* ^pin-21a

## Application
That the search lasted two hours (not four days, as in *[[Mincey v. Arizona|Mincey]]*) and occurred the same day did not matter — nothing in *[[Mincey v. Arizona|Mincey]]* turned on duration or timing. Nor did the petitioner's call for medical help diminish her expectation of privacy or convert her home into a public place: police could seize evidence in plain view while assisting her or during the limited victim-or-suspect search, but the evidence here was found in neither. The later general warrantless search therefore violated the Fourth Amendment.

## Conclusion
Reversed and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). A recent homicide does not, by itself, justify a warrantless general search of the scene; *[[Mincey v. Arizona|Mincey]]* controls.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Thompson* reaffirms [[Mincey v. Arizona]] and is reaffirmed in turn by [[Flippo v. West Virginia]] (no general "crime-scene exception"); it parallels the post-fire warrant rule of [[Michigan v. Tyler]].

## Appears on
- [[Securing the Scene]] — *Related (cross-doctrine)*

## Sources
- *Thompson v. Louisiana*, 469 U.S. 17 (1984) — https://www.courtlistener.com/opinion/111282/thompson-v-louisiana/ — pinpoint: 21.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "28ea98059afab534", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "469 U.S. 17 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 161", "official_citation_present": true, "parallel_cite": "105 S. Ct. 409; 83 L. Ed. 2d 246", "title": "Thompson v. Louisiana", "year": "1984"}}
{"assertion_id": "1f407e43b7840e77", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "There is no 'murder-scene exception' to the warrant requirement; a warrantless two-hour general search of a homicide scene in a private home is unreasonable, even though shorter than the four-day search in Mincey, and the victim's call for help does not diminish her expectation of privacy.", "title": "Thompson v. Louisiana"}}
{"assertion_id": "55b7d93e65d71077", "dimension": "support", "kind": "home_role", "locator": {"home": "Securing the Scene"}, "payload": {"home": "Securing the Scene", "role": "Related (cross-doctrine)", "title": "Thompson v. Louisiana"}}
{"assertion_id": "65330046e05803c7", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Thompson v. Louisiana"}}
{"assertion_id": "c253b2611f54b0ac", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1985-01-21", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Thompson v. Louisiana", "field_i_validity": "good_law", "scope_note": "Per curiam (announced January 21, 1985; reported at 469 U.S. 17, O.T. 1984). Reaffirms Mincey v. Arizona; no negative treatment.", "title": "Thompson v. Louisiana", "varies_by_point": "false"}}
```

### lake record — Thompson v. Louisiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Thompson v. Louisiana",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Thompson v. Louisiana",
    "case_name_short": "Thompson",
    "case_name_full": "Thompson v. Louisiana",
    "input_case_name": "Thompson v. Louisiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-11-26",
    "year": 1984,
    "docket": "83-6775",
    "cluster_id": 111282,
    "lead_opinion_id": 111282,
    "sibling_ids": [
      111282
    ],
    "absolute_url": "/opinion/111282/thompson-v-louisiana/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "469 U.S. 17",
      "volume": "469",
      "reporter": "U.S.",
      "page": "17",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "105 S. Ct. 409",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 246",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 161",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "161",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "469 U.S. 17",
        "volume": "469",
        "reporter": "U.S.",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "105 S. Ct. 409",
        "volume": "105",
        "reporter": "S. Ct.",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 L. Ed. 2d 246",
        "volume": "83",
        "reporter": "L. Ed. 2d",
        "page": "246",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 161",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "161",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "469 U.S. 17",
    "official_selection": {
      "court_class": "scotus",
      "selected": "469 U.S. 17",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-21",
      "page": null,
      "quote": "search. Homicide investigators then arrived and conducted a two-hour general, warrantless search of the home \u2014 the same day as the killing \u2014 seizing evidence used against her. The Louisiana courts upheld the search, distinguishing *Mincey* and finding a diminished expectation of privacy. ## Issue Whether a warrantless two-hour general search of a private home that is a recent homicide scene falls within an exception to the warrant requirement. ## Rule No \u2014 there is no murder-scene exception: in *Mincey*",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-21a",
      "page": null,
      "quote": "A 2-hour general search remains a significant intrusion on petitioner's privacy and therefore may only be conducted subject to the constraints \u2014 including the warrant requirement \u2014 of the Fourth Amendment.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1985-01-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Thompson v. Louisiana",
    "varies_by_point": false,
    "scope_note": "Per curiam (announced January 21, 1985; reported at 469 U.S. 17, O.T. 1984). Reaffirms Mincey v. Arizona; no negative treatment.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "DuBose v. State",
          "cluster_id": 2468681,
          "cite": [
            "915 S.W.2d 493",
            "1996 Tex. Crim. App. LEXIS 17",
            "1996 WL 61148"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nields",
          "cluster_id": 6889107,
          "cite": [
            "93 Ohio St. 3d 6",
            "752 N.E.2d 859"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Brown",
          "cluster_id": 2185565,
          "cite": [
            "749 N.E.2d 170",
            "96 N.Y.2d 80",
            "725 N.Y.S.2d 601",
            "2001 N.Y. LEXIS 576"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bilida v. McCleod",
          "cluster_id": 198914,
          "cite": [
            "211 F.3d 166",
            "2000 WL 528014"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Charles E. Hamilton, United States of America v. Charles Eugene Hamilton",
          "cluster_id": 471363,
          "cite": [
            "792 F.2d 837",
            "1986 U.S. App. LEXIS 26235",
            "55 U.S.L.W. 2042"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Magnano",
          "cluster_id": 7892883,
          "cite": [
            "204 Conn. 259",
            "528 A.2d 760",
            "1987 Conn. LEXIS 919"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Nields",
          "cluster_id": 10685735,
          "cite": [
            "2001 Ohio 1291",
            "93 Ohio St. 3d 6"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Snell",
          "cluster_id": 6577780,
          "cite": [
            "428 Mass. 766",
            "705 N.E.2d 236",
            "1999 Mass. LEXIS 20"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Brock",
          "cluster_id": 2291360,
          "cite": [
            "327 S.W.3d 645",
            "2009 Tenn. Crim. App. LEXIS 496",
            "2009 WL 1850883"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNair v. Commonwealth",
          "cluster_id": 1066057,
          "cite": [
            "521 S.E.2d 303",
            "31 Va. App. 76"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Peters",
          "cluster_id": 6579960,
          "cite": [
            "453 Mass. 818",
            "905 N.E.2d 1111",
            "2009 Mass. LEXIS 75"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Riggs v. State",
          "cluster_id": 1788217,
          "cite": [
            "918 So. 2d 274",
            "2005 WL 3429537"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hunt",
          "cluster_id": 2707112,
          "cite": [
            "2013 Ohio 5326"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. State",
          "cluster_id": 1510723,
          "cite": [
            "856 S.W.2d 177",
            "1993 Tex. Crim. App. LEXIS 130",
            "1993 WL 216682"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Roberts v. State",
          "cluster_id": 2247920,
          "cite": [
            "599 N.E.2d 595",
            "1992 Ind. LEXIS 217",
            "1992 WL 235329"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Evans v. Solomon",
          "cluster_id": 2528123,
          "cite": [
            "681 F. Supp. 2d 233",
            "2010 U.S. Dist. LEXIS 3744",
            "2010 WL 276189"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Phillips.",
          "cluster_id": 4301195,
          "cite": [
            "138 Haw. 321",
            "382 P.3d 133",
            "2016 Haw. LEXIS 234"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Ricky Johnson A/K/A Richard Lamar Union and Durand M. Banner, Defendants",
          "cluster_id": 515470,
          "cite": [
            "862 F.2d 1135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Howard",
          "cluster_id": 3939487,
          "cite": [
            "600 N.E.2d 809",
            "75 Ohio App. 3d 760",
            "1991 Ohio App. LEXIS 4072"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "City of Parma v. Jackson",
          "cluster_id": 3997307,
          "cite": [
            "568 N.E.2d 702",
            "58 Ohio App. 3d 17",
            "1989 Ohio App. LEXIS 1128"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. MacIoce",
          "cluster_id": 2116073,
          "cite": [
            "197 Cal. App. 3d 262",
            "242 Cal. Rptr. 771",
            "1987 Cal. App. LEXIS 2470"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Spears",
          "cluster_id": 1864316,
          "cite": [
            "560 So. 2d 1145",
            "1989 Ala. Crim. App. LEXIS 2368"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Maldonado Garcia",
          "cluster_id": 1423605,
          "cite": [
            "655 F. Supp. 1363",
            "1987 U.S. Dist. LEXIS 2124"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Terrance Baker",
          "cluster_id": 9371555,
          "cite": [
            "58 F.4th 1109"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thompson v. Louisiana:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111282) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 46,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 46,
        "triage_read": 0,
        "triage_snippet_classified": 46
      },
      "lane2_top_cited": {
        "query": "cites:(111282)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0zJnM9MTg1OTUwMCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mw%3D%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28111282%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111282)",
        "reviewed": 6,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 6,
        "triage_read": 0,
        "triage_snippet_classified": 6
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111282)",
    "indexed_citing_opinions": 59,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111282,
        "count": 59,
        "count_source": "search"
      }
    ],
    "citation_count": 327,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/thompson-v-louisiana.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjIzNjM0NjYmcz02NTc5OTYwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111282%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111282,
        "cited_id": 107564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 108183,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 108967,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 109537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 109714,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 109905,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 110530,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 110719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 110979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 111173,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111282,
        "cited_id": 1131848,
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
    "date_created": "2026-07-05T21:37:54Z",
    "date_modified": "2026-07-10T00:12:42Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:38:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:38:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:42:16Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:38:42Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Thompson v. Louisiana

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b160-7">
<span citation-index="1" class="star-pagination" label="18"> 
   *18
   </span>
  Per Curiam.
 </author>
<p id="b160-8">
  In this case, the Louisiana Supreme Court upheld the validity of a warrantless “murder scene” search of petitioner’s home. Because this holding is in direct conflict with our opinion in
  <em>
   Mincey
  </em>
  v.
  <em>
   Arizona,
  </em>
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), we reverse.
 </p>
<p id="b160-9">
  I
 </p>
<p id="b160-10">
  The Louisiana Supreme Court states the facts as follows:
 </p>
<blockquote id="AVJ">
  “On May 18, 1982, several deputies from the Jefferson Parish Sheriff’s Department arrived at [petitioner’s] home in response to a report by the [petitioner’s] daughter of a homicide. The deputies entered the house, made a cursory search and discovered [petitioner’s] husband dead of a gunshot wound in a bedroom and the [petitioner] lying unconscious in another bedroom due to an apparent drug overdose. According to the [petitioner’s] daughter, the [petitioner] had shot her husband, then ingested a quantity of pills in a suicide attempt, and then, changing her mind, called her daughter, informed her of the situation and requested help. The daughter then contacted the police. Upon their arrival, the daughter admitted them into the house and directed them to the rooms containing the [petitioner] and the victim. The deputies immediately transported the then unconscious [petitioner] to a hospital and secured the scene. Thirty-five minutes later two members of the homicide unit of the Jefferson Parish Sheriff’s Office arrived and conducted a follow-up investigation of the homicide and attempted suicide.
 </blockquote>
<blockquote id="b160-11">
  “The homicide investigators entered the residence and commenced what they described at the motion to suppress hearing as a ‘general exploratory search for evidence of a crime.’ During their search, which lasted
  <span citation-index="1" class="star-pagination" label="19"> 
   *19
   </span>
  approximately two hours, the detectives examined each room of the house.” <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/#668" aria-description="Citation for case: State v. Thompson">448 So. 2d 666, 668</a></span> (1984).
 </blockquote>
<p id="b161-5">
  Petitioner was subsequently indicted for the second-degree murder of her husband. She moved to suppress three items of evidence discovered during the search, including a pistol found inside a chest of drawers in the same room as the deceased’s body, a torn up note found in a wastepaper basket in an adjoining bathroom, and another letter (alleged to be a suicide note) found folded up inside an envelope containing a Christmas card on the top of a chest of drawers. All of this evidence was found in the “general exploratory search for evidence” conducted by two homicide investigators who arrived at the scene approximately 35 minutes after petitioner was sent to the hospital. See
  <em>
   <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/" aria-description="Citation for case: State v. Thompson">ibid.</a></span>
  </em>
  By the time those investigators arrived, the officers who originally arrived at the scene had already searched the premises for other victims or suspects. See
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#392" aria-description="Citation for case: Mincey v. Arizona"><em>
   Mincey, supra,
  </em>
  at 392</a></span>. The investigators testified that they had time to secure a warrant before commencing the search, see <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/#668" aria-description="Citation for case: State v. Thompson">448 So. 2d, at 668</a></span>, and that no one had given consent to the search, see App. C to Pet. for Cert. 7-8, 16, 19-20 (transcript of testimony of Detectives Zinna and Masson at suppression hearing).
 </p>
<p id="b161-6">
  The trial court originally denied petitioner’s motion to suppress. However, the trial court then granted petitioner’s motion for reconsideration and partially reversed its former decision, holding that the gun and the suicide letter found in the Christmas card were obtained in violation of the Fourth Amendment and therefore must be suppressed. The Louisiana Court of Appeal denied the State’s application for a writ of review. A sharply divided Louisiana Supreme Court subsequently held all of the evidence seized to be admissible.
 </p>
<p id="b161-7">
  II
 </p>
<p id="b161-8">
  As we stated in
  <em>
   United States
  </em>
  v.
  <em>
   Chadwick,
  </em>
  <span class="citation" data-id="9426913"><a href="/opinion/109714/united-states-v-chadwick/#9" aria-description="Citation for case: United States v. Chadwick">433 U. S. 1, 9</a></span> (1977), “in this area we do not write on a clean slate.” In a long line of cases, this Court has stressed that “searches
  <span citation-index="1" class="star-pagination" label="20"> 
   *20
   </span>
  conducted outside the judicial process, without prior approval by judge or magistrate, are
  <em>
   per se
  </em>
  unreasonable under the Fourth Amendment — subject only to a few specifically established and well delineated exceptions.”
  <em>
   Katz
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States">389 U. S. 347, 357</a></span> (1967) (footnotes omitted). This was not a principle freshly coined for the occasion in
  <em>
   <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,
  </em>
  but rather represented this Court’s longstanding understanding of the relationship between the two Clauses of the Fourth Amendment.
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  See
  <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/#357" aria-description="Citation for case: Katz v. United States"><em>
   Katz, supra,
  </em>
  at 357</a></span>, nn. 18 and 19. Since the time of
  <em>
   <span class="citation" data-id="9423552"><a href="/opinion/107564/katz-v-united-states/" aria-description="Citation for case: Katz v. United States">Katz</a></span>,
  </em>
  this Court has recognized the existence of additional exceptions. See,
  <em>
   e. g., Donovan
  </em>
  v.
  <em>
   Dewey,
  </em>
  <span class="citation" data-id="9428427"><a href="/opinion/110530/donovan-v-dewey/" aria-description="Citation for case: Donovan v. Dewey">452 U. S. 594</a></span> (1981);
  <em>
   United States
  </em>
  v.
  <em>
   Martinez-Fuerte,
  </em>
  <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543</a></span> (1976);
  <em>
   South Dakota
  </em>
  v.
  <em>
   Opperman,
  </em>
  <span class="citation" data-id="9426579"><a href="/opinion/109537/south-dakota-v-opperman/" aria-description="Citation for case: South Dakota v. Opperman">428 U. S. 364</a></span> (1976). However, we have consistently reaffirmed our understanding that in all cases outside the exceptions to the warrant requirement the Fourth
  <em>
   Amendment
  </em>
  requires the interposition of a neutral and detached magistrate between the police and the “persons, houses, papers, and effects” of citizens. See,
  <em>
   e. g., Welsh
  </em>
  v.
  <em>
   Wisconsin,
  </em>
  <span class="citation" data-id="9429597"><a href="/opinion/111173/welsh-v-wisconsin/#748" aria-description="Citation for case: Welsh v. Wisconsin">466 U. S. 740, 748-750</a></span> (1984);
  <em>
   United States
  </em>
  v.
  <em>
   Place,
  </em>
  <span class="citation" data-id="9429264"><a href="/opinion/110979/united-states-v-place/#701" aria-description="Citation for case: United States v. Place">462 U. S. 696, 701-702</a></span> (1983);
  <em>
   United States
  </em>
  v.
  <em>
   Ross,
  </em>
  <span class="citation" data-id="9428782"><a href="/opinion/110719/united-states-v-ross/#824" aria-description="Citation for case: United States v. Ross">456 U. S. 798, 824-825</a></span> (1982);
  <em>
   Steagald
  </em>
  v.
  <em>
   United States,
  </em>
  <span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U. S. 204, 211-212</a></span> (1981);
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#390" aria-description="Citation for case: Mincey v. Arizona"><em>
   Mincey, supra,
  </em>
  at 390</a></span>;
  <em>
   Coolidge
  </em>
  v.
  <em>
   New Hampshire,
  </em>
  <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-475</a></span> (1971) (plurality opinion);
  <em>
   Vale
  </em>
  v.
  <em>
   Louisiana,
  </em>
  <span class="citation" data-id="9424318"><a href="/opinion/108183/vale-v-louisiana/#34" aria-description="Citation for case: Vale v. Louisiana">399 U. S. 30, 34</a></span> (1970);
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968).
 </p>
<p id="b162-5">
  A
 </p>
<p id="b162-6">
  Although the homicide investigators in this case may well have had probable cause to search the premises, it is un
  <span citation-index="1" class="star-pagination" label="21"> 
   *21
   </span>
  disputed that they did not obtain a warrant.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  Therefore, for the search to be valid, it must fall within one of the narrow and specifically delineated exceptions to the warrant requirement. In
  <em>
   Mincey
  </em>
  v. Arizona, <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">437 U. S. 385</a></span> (1978), we unanimously rejected the contention that one of the exceptions to the Warrant Clause is a “murder scene exception.” Although we noted that police may make warrantless entries on premises where “they reasonably believe that a person within is in need of immediate aid,”
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#392" aria-description="Citation for case: Mincey v. Arizona"><em>
   id.,
  </em>
  at 392</a></span>, and that “they may make a prompt warrantless search of the area to see if there are other victims or if a killer is still on the premises,”
  <em>
   ibid.,
  </em>
  we held that “the ‘murder scene exception’... is inconsistent with the Fourth and Fourteenth Amendments — that the warrantless search of Mincey’s apartment was not constitutionally permissible simply because a homicide had recently occurred there.”
  <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#395" aria-description="Citation for case: Mincey v. Arizona"><em>
   Id.,
  </em>
  at 395</a></span>.
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>
  </em>
  is squarely on point in the instant case.
 </p>
<p id="b163-5">
  B
 </p>
<p id="b163-6">
  The Louisiana Supreme Court attempted to distinguish
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>
  </em>
  in several ways. The court noted that
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>
  </em>
  involved a 4-day search of the premises, while the search in this case took only two hours and was conducted on the same day as the murder. See <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/#671" aria-description="Citation for case: State v. Thompson">448 So. 2d, at 671</a></span>. Although we agree that the scope of the intrusion was certainly greater in
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>
  </em>
  than here, nothing in
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>
  </em>
  turned on the length of time taken in the search or the date on which it was conducted. A 2-hour general search remains a significant intrusion on petitioner’s privacy and therefore may only be conducted subject to the constraints — including the warrant requirement — of the Fourth Amendment.
 </p>
<p id="b164-4">
<span citation-index="1" class="star-pagination" label="22"> 
   *22
   </span>
  The Louisiana Supreme Court also believed that petitioner had a “diminished” expectation of privacy in her home, thus validating a search that otherwise would have been unconstitutional. <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/#671" aria-description="Citation for case: State v. Thompson">448 So. 2d, at 671</a></span>. The court noted that petitioner telephoned her daughter to request assistance. The daughter then called the police and let them in the residence. These facts, according to the court, demonstrated a diminished expectation of privacy in petitioner’s dwelling and therefore legitimated the warrantless search.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
</p>
<p id="b164-5">
  Petitioner’s attempt to get medical assistance does not evidence a diminished expectation of privacy on her part. To be sure, this action would have justified the authorities in seizing evidence under the plain-view doctrine while they were in petitioner’s house to offer her assistance. In addition, the same doctrine may justify seizure of evidence obtained in the limited “victim-or-suspect” search discussed in
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>.
  </em>
  However, the evidence at issue here was not discovered in plain view while the police were assisting petitioner to the hospital, nor was it discovered during the “victim-or-suspect” search that had been completed by the time the homicide investigators arrived. Petitioner’s call for help can hardly be seen as an invitation to the general public that would have converted her home into the sort of public place for which no warrant to search would be necessary. Therefore, the Louisiana Supreme Court’s diminished-expectation-of-privacy argument fails to distinguish this case from
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>,
  </em>
<a class="footnote" href="#fn4" id="fn4_ref">
<em>
    4
   </em>
</a>
</p>
<p id="b165-4">
<span citation-index="1" class="star-pagination" label="23"> 
   *23
   </span>
  The State contends that there was a sufficient element of consent in this case to distinguish it from the facts of
  <em>
   <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>.
  </em>
  The Louisiana Supreme Court’s decision does not attempt to validate the search as consensual, although it attempts to support its diminished-expectation-of-privacy argument by reference to the daughter’s “apparent authority” over the premises when she originally permitted the police to enter. <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/#671" aria-description="Citation for case: State v. Thompson">448 So. 2d, at 671</a></span>. Because the issue of consent is ordinarily a factual issue unsuitable for our consideration in the first instance, we express no opinion as to whether the search at issue here might be justified as consensual. However, we note that both homicide investigators explicitly testified that they had received no consent to search. Any claim of valid consent in this case would have to be measured against the standards of
  <em>
   United States
  </em>
  v.
  <em>
   Matlock,
  </em>
  <span class="citation" data-id="9425606"><a href="/opinion/108967/united-states-v-matlock/" aria-description="Citation for case: United States v. Matlock">415 U. S. 164</a></span> (1974), and
  <em>
   Schneckcloth
  </em>
  v.
  <em>
   Bustamonte,
  </em>
  <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218</a></span> (1973).
 </p>
<p id="b165-5">
  Ill
 </p>
<p id="b165-6">
  For the reasons stated above, petitioner’s motion for leave to proceed
  <em>
   informa pauperis
  </em>
  is granted, the petition for writ of certiorari is granted, the judgment of the Louisiana Supreme Court is reversed, and the cause is remanded for further proceedings not inconsistent with this opinion.
 </p>
<p id="b165-7">
<em>
   It is so ordered.
  </em>
</p>




<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b162-7">
   “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and persons or things to be seized.” U. S. Const., Amdt. 4.
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b163-7">
   Indeed Chief Justice Dixon’s dissent in this case in the Louisiana Supreme Court reads in its entirety as follows: “I respectfully dissent. All it would take to make this search legal is a warrant.” <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/#673" aria-description="Citation for case: State v. Thompson">448 So. 2d 666, 673</a></span> (1984).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b164-6">
   The Louisiana Supreme Court seemed to believe that the fact that “both parties with authority over the premises [petitioner and her husband] were either dead or unconscious and in an apparently grave condition,”
   <span class="citation" data-id="1131848"><a href="/opinion/1131848/state-v-thompson/#671" aria-description="Citation for case: State v. Thompson"><em>
    id.,
   </em>
   at 671</a></span>, in some way diminished petitioner’s expectation of privacy in the premises. Yet neither petitioner’s unavailability nor the death of her husband have any bearing on petitioner’s continuing privacy interests.
  </p>
</div><div class="footnote" id="fn4" label="4">
<a class="footnote" href="#fn4_ref">
   4
  </a>
<p id="b164-7">
   The Louisiana court’s argument in fact closely resembles an argument we rejected in
   <em>
    <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/" aria-description="Citation for case: Mincey v. Arizona">Mincey</a></span>.
   </em>
   See <span class="citation" data-id="9427279"><a href="/opinion/109905/mincey-v-arizona/#391" aria-description="Citation for case: Mincey v. Arizona">437 U. S., at 391-392</a></span>.
  </p>
</div></div></opinion>
```

---

## GROUP: content/cases/Townsend v. Sain.md  (`case`, 5 assertions)

### content_page

```
---
title: "Townsend v. Sain"
type: case
citation: "372 U.S. 293 (1963)"
parallel_cite: "83 S. Ct. 745; 9 L. Ed. 2d 770"
neutral_cite: 1963 U.S. LEXIS 1941
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1963
date_decided: 1963-03-18
docket: 8
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1963-03-18
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Townsend v. Sain
  varies_by_point: false
  scope_note: "Good law on the confession-voluntariness holding (a drug/'truth serum'-induced confession not the product of a free intellect is inadmissible). The separate federal-habeas evidentiary-hearing standard (the Townsend circumstances/deliberate-bypass) was abrogated by Keeney v. Tamayo-Reyes, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. §2254(e)(2)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/106544/townsend-v-sain/"
  cluster_id: 106544
  opinion_id: 106544
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Progeny / Refinement"
related: ["[[Rogers v. Richmond]]", "[[Beecher v. Alabama]]", "[[Lynumn v. Illinois]]", "[[Brown v. Mississippi]]"]
aliases: []
tags: ["case", "fifth-amendment", "fourteenth-amendment", "confessions", "voluntariness", "due-process", "coercion", "habeas"]
holding: "A confession that is the product of a drug having the effect of a 'truth serum' (scopolamine/hyoscine), administered to a suspect, is involuntary and inadmissible if it was not the product of a rational intellect and free will — regardless of whether the drug was administered by persons unaware of its properties and regardless of the confession's reliability."
lake:
  record_id: Townsend v. Sain
  status: verified
  projected_at: 2026-07-09
---

# Townsend v. Sain

*372 U.S. 293 (1963)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Townsend, a 19-year-old heroin addict of very low intelligence (described as "near mental defective"), was arrested for murder and robbery. During interrogation he developed narcotic-withdrawal symptoms, and a police physician injected him with phenobarbital and hyoscine — hyoscine being the same as scopolamine, a drug with the claimed properties of a "truth serum." The medication relieved his symptoms and he promptly confessed to several crimes. The identity of hyoscine as scopolamine, and scopolamine's reputation as a "truth serum," were not disclosed at the [[Common Legal Terms#suppression-hearing|suppression hearing]]. The state courts upheld the confession; a federal district court then denied [[Common Legal Terms#habeas-corpus|habeas corpus]] without an evidentiary hearing.

## Issue
Whether a confession produced after a suspect is injected with a drug having "truth serum" properties can be voluntary under the Due Process Clause — and the standards governing when a federal [[Common Legal Terms#habeas-corpus|habeas]] court must hold an evidentiary hearing.

## Rule
A drug-induced confession that is not the product of a free intellect is inadmissible. "If an individual's 'will was overborne' or if his confession was not 'the product of a rational intellect and a free will,' his confession is inadmissible because coerced. These standards are applicable whether a confession is the product of physical intimidation or psychological pressure and, of course, are equally applicable to a drug-induced statement. It is difficult to imagine a situation in which a confession would be less the product of a free intellect, less voluntary, than when brought about by a drug having the effect of a 'truth serum.' . . . Any questioning by police officers which *in fact* produces a confession which is not the product of a free intellect renders that confession inadmissible." — 372 U.S. at 307–308. ^pin-307

Reliability is irrelevant: "whether scopolamine produces true confessions or false confessions, if it in fact caused Townsend to make statements, those statements were constitutionally inadmissible." — [*Id.* at 308](https://www.courtlistener.com/opinion/106544/townsend-v-sain/#:~:text=whether%20scopolamine%20produces%20true%20confessions) n.5. ^pin-308

## Application
On these facts the Court did not itself find the confession involuntary; it held that Townsend's [[Common Legal Terms#habeas-corpus|habeas]] petition alleged facts that, if true, would establish that the hyoscine injection rendered his confession the involuntary product of a debilitated will — a question the district court could not resolve without hearing evidence. Because a material factual dispute existed (whether the drug in fact caused the confessions) and the [[Common Legal Terms#suppression-hearing|suppression hearing]] had not been a full and fair adjudication of it, the district court erred in dismissing the petition without an evidentiary hearing; the case was [[Reading and Citing Cases#on-remand|remanded]] for one.

## Conclusion
A confession caused by a "truth serum" drug, not the product of a free intellect, is inadmissible regardless of reliability; the judgment was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] for an evidentiary hearing on whether the drug in fact produced Townsend's confessions.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**, on the confession-voluntariness holding.
- **[[Common Legal Terms#habeas-corpus|Habeas]]-procedure caveat (home-by-holding):** *Townsend* also set the standards for when a federal [[Common Legal Terms#habeas-corpus|habeas]] court must hold an evidentiary hearing. That **procedural** holding (the deliberate-bypass branch) was **abrogated** by *Keeney v. Tamayo-Reyes*, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. §2254(e)(2). This page homes the case by its **confession-voluntariness** ratio, which remains good law.
- The voluntariness holding extends the coercion-not-reliability principle of [[Rogers v. Richmond]] and the overborne-will test of [[Lynumn v. Illinois]] to drug-induced statements, paralleling the drugged-confession branch of [[Beecher v. Alabama]] in the due-process line anchored by [[Brown v. Mississippi]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Progeny / Refinement*

## Sources
- *Townsend v. Sain*, 372 U.S. 293 (1963) — https://www.courtlistener.com/opinion/106544/townsend-v-sain/ — pinpoints: 307–308.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "84cc8c6244a3f8fe", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "372 U.S. 293 (1963)", "court": "U.S. Supreme Court", "neutral_cite": "1963 U.S. LEXIS 1941", "official_citation_present": true, "parallel_cite": "83 S. Ct. 745; 9 L. Ed. 2d 770", "title": "Townsend v. Sain", "year": "1963"}}
{"assertion_id": "98875786ee529040", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "A confession that is the product of a drug having the effect of a 'truth serum' (scopolamine/hyoscine), administered to a suspect, is involuntary and inadmissible if it was not the product of a rational intellect and free will — regardless of whether the drug was administered by persons unaware of its properties and regardless of the confession's reliability.", "title": "Townsend v. Sain"}}
{"assertion_id": "a8a9c41ca0ed413a", "dimension": "support", "kind": "home_role", "locator": {"home": "Due-Process Voluntariness of Confessions"}, "payload": {"home": "Due-Process Voluntariness of Confessions", "role": "Key — Progeny / Refinement", "title": "Townsend v. Sain"}}
{"assertion_id": "116411e05489a765", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1963-03-18", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Townsend v. Sain", "field_i_validity": "good_law", "scope_note": "Good law on the confession-voluntariness holding (a drug/'truth serum'-induced confession not the product of a free intellect is inadmissible). The separate federal-habeas evidentiary-hearing standard (the Townsend circumstances/deliberate-bypass) was abrogated by Keeney v. Tamayo-Reyes, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. §2254(e)(2).", "title": "Townsend v. Sain", "varies_by_point": "false"}}
{"assertion_id": "fd9081e449acbff5", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Townsend v. Sain"}}
```

### lake record — Townsend v. Sain

```json
{
  "schema_version": "s2.v1",
  "record_id": "Townsend v. Sain",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Townsend v. Sain",
    "case_name_short": "Townsend",
    "case_name_full": "TOWNSEND v. SAIN, SHERIFF, Et Al.",
    "input_case_name": "Townsend v. Sain",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1963-03-18",
    "year": 1963,
    "docket": "8",
    "cluster_id": 106544,
    "lead_opinion_id": 106544,
    "sibling_ids": [
      106544,
      9422545,
      9422546,
      9422547
    ],
    "absolute_url": "/opinion/106544/townsend-v-sain/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "372 U.S. 293",
      "volume": "372",
      "reporter": "U.S.",
      "page": "293",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "83 S. Ct. 745",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "745",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 770",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "770",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1963 U.S. LEXIS 1941",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "372 U.S. 293",
        "volume": "372",
        "reporter": "U.S.",
        "page": "293",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "83 S. Ct. 745",
        "volume": "83",
        "reporter": "S. Ct.",
        "page": "745",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "9 L. Ed. 2d 770",
        "volume": "9",
        "reporter": "L. Ed. 2d",
        "page": "770",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1963 U.S. LEXIS 1941",
        "volume": "1963",
        "reporter": "U.S. LEXIS",
        "page": "1941",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "372 U.S. 293",
    "official_selection": {
      "court_class": "scotus",
      "selected": "372 U.S. 293",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-307",
      "page": null,
      "quote": "properties can be voluntary under the Due Process Clause \u2014 and the standards governing when a federal habeas court must hold an evidentiary hearing. ## Rule A drug-induced confession that is not the product of a free intellect is inadmissible.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-308",
      "page": null,
      "quote": "whether scopolamine produces true confessions or false confessions, if it in fact caused Townsend to make statements, those statements were constitutionally inadmissible.",
      "star_marker": "334",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 81892,
      "fragment": "#:~:text=whether%20scopolamine%20produces%20true%20confessions",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1963-03-18",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Townsend v. Sain",
    "varies_by_point": false,
    "scope_note": "Good law on the confession-voluntariness holding (a drug/'truth serum'-induced confession not the product of a free intellect is inadmissible). The separate federal-habeas evidentiary-hearing standard (the Townsend circumstances/deliberate-bypass) was abrogated by Keeney v. Tamayo-Reyes, 504 U.S. 1 (1992), and superseded by AEDPA, 28 U.S.C. \u00a72254(e)(2).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Anthony Juniper v. David Zook",
          "cluster_id": 4443845,
          "cite": [
            "876 F.3d 551"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Halliburton, Inc. v. Administrative Review Board",
          "cluster_id": 2750531,
          "cite": [
            "771 F.3d 254",
            "39 I.E.R. Cas. (BNA) 529",
            "2014 U.S. App. LEXIS 21743",
            "98 Empl. Prac. Dec. (CCH) 45,187",
            "2014 WL 5861790"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brandon Dale Woodruff v. State",
          "cluster_id": 3094579,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Love v. Scribner",
          "cluster_id": 8672855,
          "cite": [
            "278 F. App'x 714"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Sedrice Maurice Simpson v. Larry Norris, Director, Arkansas Department of Correction",
          "cluster_id": 798140,
          "cite": [
            "490 F.3d 1029",
            "2007 U.S. App. LEXIS 15229",
            "2007 WL 1827496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Strickland v. Washington",
          "cluster_id": 111170,
          "cite": [
            "80 L. Ed. 2d 674",
            "104 S. Ct. 2052",
            "466 U.S. 668",
            "1984 U.S. LEXIS 79"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jackson v. Virginia",
          "cluster_id": 110138,
          "cite": [
            "61 L. Ed. 2d 560",
            "99 S. Ct. 2781",
            "443 U.S. 307",
            "1979 U.S. LEXIS 10"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Williams v. Taylor",
          "cluster_id": 145122,
          "cite": [
            "146 L. Ed. 2d 389",
            "120 S. Ct. 1495",
            "529 U.S. 362",
            "2000 U.S. LEXIS 2837"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Preiser v. Rodriguez",
          "cluster_id": 108772,
          "cite": [
            "36 L. Ed. 2d 439",
            "93 S. Ct. 1827",
            "411 U.S. 475",
            "1973 U.S. LEXIS 72"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex Parte Young",
          "cluster_id": 2464872,
          "cite": [
            "418 S.W.2d 824",
            "1967 Tex. Crim. App. LEXIS 1084"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wainwright v. Witt",
          "cluster_id": 111303,
          "cite": [
            "83 L. Ed. 2d 841",
            "105 S. Ct. 844",
            "469 U.S. 412",
            "1985 U.S. LEXIS 43",
            "53 U.S.L.W. 4108"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Browder v. Director, Dept. of Corrections of Ill.",
          "cluster_id": 109761,
          "cite": [
            "54 L. Ed. 2d 521",
            "98 S. Ct. 556",
            "434 U.S. 257",
            "1978 U.S. LEXIS 53"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schriro v. Landrigan",
          "cluster_id": 145734,
          "cite": [
            "167 L. Ed. 2d 836",
            "127 S. Ct. 1933",
            "550 U.S. 465",
            "2007 U.S. LEXIS 5496"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Raddatz",
          "cluster_id": 110315,
          "cite": [
            "65 L. Ed. 2d 424",
            "100 S. Ct. 2406",
            "447 U.S. 667",
            "1980 U.S. LEXIS 49"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sanders v. United States",
          "cluster_id": 106591,
          "cite": [
            "10 L. Ed. 2d 148",
            "83 S. Ct. 1068",
            "373 U.S. 1",
            "1963 U.S. LEXIS 1695"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
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
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Arizona v. Washington",
          "cluster_id": 109773,
          "cite": [
            "54 L. Ed. 2d 717",
            "98 S. Ct. 824",
            "434 U.S. 497",
            "1978 U.S. LEXIS 628"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Townsend v. Sain:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTM4MTQ3MjAwMDAwJnM9ODQ3MDU3NyZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28106544+OR+9422545+OR+9422546+OR+9422547%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 5,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 7,
        "triage_snippet_classified": 193
      },
      "lane2_top_cited": {
        "query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzIxJnM9MTE3ODczJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28106544+OR+9422545+OR+9422546+OR+9422547%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547)",
        "reviewed": 10,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 10,
        "triage_read": 0,
        "triage_snippet_classified": 10
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(106544 OR 9422545 OR 9422546 OR 9422547)",
    "indexed_citing_opinions": 2834,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 106544,
        "count": 2648,
        "count_source": "search"
      },
      {
        "opinion_id": 9422545,
        "count": 270,
        "count_source": "search"
      },
      {
        "opinion_id": 9422546,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9422547,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4499,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/townsend-v-sain.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjY2MjEzOTgmcz00NzEzOTY5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28106544+OR+9422545+OR+9422546+OR+9422547%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 106544,
        "cited_id": 91598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 98441,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 101098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 103458,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 104196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 104557,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 104997,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105074,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105683,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105726,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105813,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 105977,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106031,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106040,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106192,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106218,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 106278,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 235042,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 237553,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 239867,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 242868,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 247792,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 248755,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 250462,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 251564,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 251644,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 252544,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 254906,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 1208179,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 2120258,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 2195532,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 106544,
        "cited_id": 3416896,
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
    "date_created": "2026-07-05T21:52:00Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:52:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:52:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-05T21:56:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:52:12Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Townsend v. Sain

```
<div>
<center><b><span class="citation" data-id="9422545"><a href="/opinion/106544/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">372 U.S. 293</a></span> (1963)</b></center>
<center><h1>TOWNSEND<br>
v.<br>
SAIN, SHERIFF, ET AL.</h1></center>
<center>No. 8.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued February 19, 1962.</center>
<center>Restored to the calendar for reargument April 2, 1962.</center>
<center>Reargued October 8-9, 1962.</center>
<center>Decided March 18, 1963.</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE SEVENTH CIRCUIT.
<p><span class="star-pagination">*295</span> <i>George N. Leighton</i> reargued the cause and filed a brief for petitioner.</p>
<p><i>Edward J. Hladis</i> reargued the cause for respondents. With him on the brief was <i>Daniel P. Ward.</i></p>
<p>MR. CHIEF JUSTICE WARREN delivered the opinion of the Court.</p>
<p>This case, in its present posture raising questions as to the right to a plenary hearing in federal habeas corpus, comes to us once again after a tangle of prior proceedings. In 1955 the petitioner, Charles Townsend, was tried before a jury for murder in the Criminal Court of Cook County, Illinois. At his trial petitioner, through his court-appointed counsel, the public defender, objected to the <span class="star-pagination">*296</span> introduction of his confession on the ground that it was the product of coercion. A hearing was held outside the presence of the jury, and the trial judge denied the motion to suppress. He later admitted the confession into evidence. Further evidence relating to the issue of voluntariness was introduced before the jury. The charge permitted them to disregard the confession if they found that it was involuntary. Under Illinois law the admissibility of the confession is determined solely by the trial judge, but the question of voluntariness, because it bears on the issue of credibility, may also be presented to the jury. See, <i>e. g., </i><i>People</i> v. <i>Schwartz,</i> <span class="citation" data-id="2195532"><a href="/opinion/2195532/people-v-schwartz/#523" aria-description="Citation for case: People v. Schwartz">3 Ill. 2d 520, 523</a></span>, <span class="citation" data-id="2195532"><a href="/opinion/2195532/people-v-schwartz/#760" aria-description="Citation for case: People v. Schwartz">121 N. E. 2d 758, 760</a></span>; <i>People</i> v. <i>Roach,</i> <span class="citation" data-id="3416896"><a href="/opinion/3420387/the-people-v-roach/" aria-description="Citation for case: The People v. Roach">369 Ill. 95</a></span>, <span class="citation" data-id="3416896"><a href="/opinion/3420387/the-people-v-roach/" aria-description="Citation for case: The People v. Roach">15 N. E. 2d 873</a></span>. The jury found petitioner guilty and affixed the death penalty to its verdict. The Supreme Court of Illinois affirmed the conviction, two justices dissenting. <i>People</i> v. <i>Townsend,</i> <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d 30</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d 729</a></span>. This Court denied a writ of certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./355/850/">355 U. S. 850</a></span>.</p>
<p>Petitioner next sought post-conviction collateral relief in the Illinois State courts. The Cook County Criminal Court dismissed his petition without holding an evidentiary hearing. The Supreme Court of Illinois by order affirmed, holding that the issue of coercion was <i>res judicata,</i> and this Court again denied certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./358/887/">358 U. S. 887</a></span>. The issue of coercion was pressed at all stages of these proceedings.</p>
<p>Having thoroughly exhausted his state remedies, Townsend petitioned for habeas corpus in the United States District Court for the Northern District of Illinois. That court, considering only the pleadings filed in the course of that proceeding and the opinion of the Illinois Supreme Court rendered on direct appeal, denied the writ. The Court of Appeals for the Seventh Circuit dismissed an appeal. <span class="citation" data-id="247792"><a href="/opinion/247792/united-states-of-america-ex-rel-charles-townsend-v-frank-g-sain-sheriff/" aria-description="Citation for case: United States of America Ex Rel. Charles Townsend v....">265 F. 2d 660</a></span>. However, this Court granted a petition for certiorari, vacated the judgment and remanded for a decision as to whether, in the light of the <span class="star-pagination">*297</span> state-court record, a plenary hearing was required. <span class="citation multiple-matches"><a href="/c/U.%20S./359/64/">359 U. S. 64</a></span>.</p>
<p>On the remand, the District Court held no hearing and dismissed the petition, finding only that "Justice would not be served by ordering a full hearing or by awarding any or all of [the] relief sought by Petitioner." The judge stated that he was satisfied from the state-court records before him that the decision of the state courts holding the challenged confession to have been freely and voluntarily given by petitioner was correct, and that there had been no denial of federal due process of law. On appeal the Court of Appeals concluded that "[o]n habeas corpus, the district court's inquiry is limited to a study of the <i>undisputed</i> portions of the record" and that the undisputed portions of this record showed no deprivation of constitutional rights. <span class="citation" data-id="250462"><a href="/opinion/250462/united-states-of-america-ex-rel-charles-townsend-v-frank-g-sain-sheriff/#329" aria-description="Citation for case: United States of America Ex Rel. Charles Townsend v....">276 F. 2d 324, 329</a></span>. We granted certiorari to determine whether the courts below had correctly determined and applied the standards governing hearings in federal habeas corpus. <span class="citation multiple-matches"><a href="/c/U.%20S./365/866/">365 U. S. 866</a></span>. The case was first argued during the October Term 1961. Two of the Justices were unable to participate in a decision, and we subsequently ordered it reargued. <span class="citation multiple-matches"><a href="/c/U.%20S./369/834/">369 U. S. 834</a></span>. We now have it before us for decision.</p>
<p>The undisputed evidence adduced at the trial-court hearing on the motion to suppress showed the following. Petitioner was arrested by Chicago police shortly before or after 2 a. m. on New Year's Day 1954. They had received information from one Campbell, then in their custody for robbery, that petitioner was connected with the robbery and murder of Jack Boone, a Chicago steel-worker and the victim in this case. Townsend was 19 years old at the time, a confirmed heroin addict and a user of narcotics since age 15. He was under the influence of a dose of heroin administered approximately one and one-half hours before his arrest. It was his practice to take injections three to five hours apart. At about 2:30 a. m. <span class="star-pagination">*298</span> petitioner was taken to the second district police station and, shortly after his arrival, was questioned for a period variously fixed from one-half to two hours. During this period, he denied committing any crimes. Thereafter at about 5 a. m. he was taken to the 19th district station where he remained, without being questioned, until about 8:15 p. m. that evening. At that time he was returned to the second district station and placed in a line-up with several other men so that he could be viewed by one Anagnost, the victim of another robbery. When Anagnost identified another man, rather than petitioner, as his assailant, a scuffle ensued, the details of which were disputed by petitioner and the police. Following this incident petitioner was again subjected to questioning. He was interrogated more or less regularly from about 8:45 until 9:30 by police officers. At that time an Assistant State's Attorney arrived. Some time shortly before or after nine o'clock, but before the arrival of the State's Attorney, petitioner complained to Officer Cagney that he had pains in his stomach, that he was suffering from other withdrawal symptoms, that he wanted a doctor, and that he was in need of a dose of narcotics. Petitioner clutched convulsively at his stomach a number of times. Cagney, aware that petitioner was a narcotic addict, telephoned for a police physician. There was some dispute between him and the State's Attorney, both prosecution witnesses, as to whether the questioning continued until the doctor arrived. Cagney testified that it did and the State's Attorney to the contrary. In any event, after the withdrawal symptoms commenced it appears that petitioner was unresponsive to questioning. The doctor appeared at 9:45. In the presence of Officer Cagney he gave Townsend a combined dosage by injection of 1/8-grain of phenobarbital and 1/230-grain of hyoscine. Hyoscine is the same as scopolamine and is claimed by petitioner in this proceeding to have the properties of a "truth serum." <span class="star-pagination">*299</span> The doctor also left petitioner four or five 1/4-grain tablets of phenobarbital. Townsend was told to take two of these that evening and the remainder the following day. The doctor testified that these medications were given to petitioner for the purpose of alleviating the withdrawal symptoms; the police officers and the State's Attorney testified that they did not know what the doctor had given petitioner. The doctor departed between 10 and 10:30. The medication alleviated the discomfort of the withdrawal symptoms, and petitioner promptly responded to questioning.</p>
<p>As to events succeeding this point in time on January 1, the testimony of the prosecution witnesses and of the petitioner irreconcilably conflicts. However, for the purposes of this proceeding both sides agree that the following occurred. After the doctor left, Officer Fitzgerald and the Assistant State's Attorney joined Officer Cagney in the room with the petitioner, where he was questioned for about 25 minutes. They all then went to another room; a court reporter there took down petitioner's statements. The State's Attorney turned the questioning to the Boone case about 11:15. In less than nine minutes a full confession was transcribed. At about 11:45 the questioning was terminated, and petitioner was returned to his cell.</p>
<p>The following day, Saturday, January 2, at about 1 p. m. petitioner was taken to the office of the prosecutor where the Assistant State's Attorney read, and petitioner signed, transcriptions of the statements which he had made the night before. When Townsend again experienced discomfort on Sunday evening, the doctor was summoned. He gave petitioner more 1/4-grain tablets of phenobarbital. On Monday, January 4, Townsend was taken to a coroner's inquest where he was called to the witness stand by the State and, after being advised of his right not to testify, again confessed. At the time of the inquest petitioner was without counsel. The public defender was not <span class="star-pagination">*300</span> appointed to represent him until his arraignment on January 12.</p>
<p>Petitioner testified at the motion to suppress to the following version of his detention. He was initially questioned at the second district police station for a period in excess of two hours. Upon his return from the 19th district and after Anagnost, the robbery victim who had viewed the line-up, had identified another person as the assailant, Officer Cagney accompanied Anagnost into the hall and told him that he had identified the wrong person. Another officer then entered the room, hit the petitioner in the stomach and stated that petitioner knew that he had robbed Anagnost. Petitioner fell to the floor and vomited water and a little blood. Officer Cagney spoke to Townsend 5 or 10 minutes later, Townsend told him that he was sick from the use of drugs, and Cagney offered to call a doctor if petitioner would "cooperate" and tell the truth about the Boone murder. Five minutes later the officer had changed his tack; he told petitioner that he thought him innocent and that he would call the doctor, implying that the doctor would give him a narcotic. The doctor gave petitioner an injection in the arm and five pills. Townsend took three of these immediately. Although he felt better, he felt dizzy and sleepy and his distance vision was impaired. Anagnost was then brought into the room, and petitioner was asked by someone to tell Anagnost that he had robbed him. Petitioner then admitted the robbery, and the next thing he knew was that he was sitting at a desk. He fell asleep but was awakened and handed a pen; he signed his name believing that he was going to be released on bond. Townsend was taken to his cell but was later taken back to the room in which he had been before. He could see "a lot of lights flickering," and someone told him to hold his head up. This went on for a minute or so, and petitioner was then again taken back to his cell. The next morning petitioner's <span class="star-pagination">*301</span> head was much clearer, although he could not really remember what had occurred following the injection on the previous evening. An officer then told petitioner that he had confessed. Townsend was taken into a room and asked about a number of robberies and murders. "I believe I said yes to all of them." He could not hear very well and felt sleepy. That afternoon, after he had taken the remainder of the phenobarbital pills, he was taken to the office of the State's Attorney. Half asleep he signed another paper although not aware of its contents. The doctor gave him six or seven pills of a different color on Sunday evening. He took some of these immediately. They kept him awake all night. The following Monday morning he took more of these pills. Later that day he was taken to a coroner's inquest. He testified at the inquest because the officers had told him to do so.</p>
<p>Essentially the prosecution witnesses contradicted all of the above. They testified that petitioner had been questioned initially for only one-half hour, that he had scuffled with the man identified by Anagnost, and not an officer, and that he had not vomited. The officers and the Assistant State's Attorney also testified that petitioner had appeared to be awake and coherent throughout the evening of the 1st of January and at all relevant times thereafter, and that he had not taken the pills given to him by the doctor on the evening of the 1st. They stated that the petitioner had appeared to follow the statement which he signed and which was read to him at the State's Attorney's office. Finally they denied that any threats or promises of any sort had been made or that Townsend had been told to testify at the coroner's inquest. As stated above counsel was not provided for him at this inquest.</p>
<p>There was considerable testimony at the motion to suppress concerning the probable effects of hyoscine and phenobarbital. Dr. Mansfield, who had prescribed for <span class="star-pagination">*302</span> petitioner on the evening when he had first confessed, testified for the prosecution. He stated that a full therapeutic dose of hyoscine was 1/100 of a grain; that he gave Townsend 1/230 of a grain; that "phenobarbital . . . reacts very well combined with [hyoscine when] . . . you want to quiet" a person; that the combination will "pacify" because "it has an effect on the mind"; but that the dosage administered would not put a person to sleep and would not cause amnesia or impairment of eyesight or of mental condition. The doctor denied that he had administered any "truth serum." However, he did not disclose that hyoscine is the same as scopolamine or that the latter is familiarly known as "truth serum." Petitioner's expert was a doctor of physiology, pharmacology and toxicology. He was formerly the senior toxicological chemist of Cook County and at the time of trial was a professor of pharmacology, chemotherapy and toxicology at the Loyola University School of Medicine. He testified to the effect of the injection upon a hypothetical subject, obviously the petitioner. The expert stated that the effect of the prescribed dosage of hyoscine upon the subject, assumed to be a narcotic addict, "would be of such a nature that it could range between absolute sleep . . . and drowsiness, as one extreme, and the other extreme. . . would incorporate complete disorientation and excitation . . . ." And, assuming that the subject took 1/8-grain phenobarbital by injection and 1/2-grain orally at the same time, the expert stated that the depressive effect would be accentuated. The expert testified that the subject would suffer partial or total amnesia for five to eight hours and loss of near vision for four to six hours.</p>
<p>The trial judge summarily denied the motion to suppress and later admitted the court reporter's transcription of the confession into evidence. He made no findings of fact and wrote no opinion stating the grounds of his decision.<sup>[1]</sup><span class="star-pagination">*303</span> Thereafter, for the purpose of testing the credibility of the confession, the evidence relating to coercion was placed before the jury. At that time additional noteworthy testimony was elicited. The identity of hyoscine and scopolamine was established (but no mention of the drug's properties as a "truth serum" was made). An expert witness called by the prosecution testified that Townsend had such a low intelligence that he was a near mental defective and "just a little above moron." Townsend testified that the officers had slapped him on several occasions and had threatened to shoot him. Finally, Officer Corcoran testified that about 9 p. m., Friday evening before the doctor's arrival, Townsend had confessed to the Boone assault and robbery in response to a question propounded by Officer Cagney in the presence of Officers Fitzgerald, Martin and himself. But although Corcoran, Cagney and Martin had testified extensively at the motion to suppress, none had mentioned any such confession. Furthermore, both Townsend and Officer Fitzgerald at the motion to suppress had flatly said that no statement had been made before the doctor arrived. Although the other three officers testified at the trial, not one of them was asked to corroborate this phase of Corcoran's testimony.</p>
<p><span class="star-pagination">*304</span> It was established that the homicide occurred at about 6 p. m. on December 18, 1953. Essentially the only evidence which connected petitioner with the crime, other than his confession, was the testimony of Campbell, then on probation for robbery, and of the pathologist who performed the autopsy on Boone. Campbell testified that about the "middle" of December at about 8:30 p. m. he had seen Townsend walking down a street in the vicinity of the murder with a brick in his hand. He was unable to fix the exact date, did not know of the Boone murder at the time and, so far as his testimony revealed, had no reason to suspect that Townsend had done anything unlawful previous to their meeting.</p>
<p>The pathologist testified that death was caused by a "severe blow to the top of his [Boone's] head . . . ." Contrary to the statement in the opinion of the Illinois Supreme Court on direct appeal there was no testimony that the wounds were "located in such a manner as to have been inflicted by a blow with a house brick . . . ." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#45" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 45</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#737" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 737</a></span>. In any event, that court characterized the evidence as meagre and noted that "it was brought out by cross-examination that Campbell had informed on the defendant to obtain his own release from custody." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#44" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 44, 45</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#737" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 737</a></span>. Prior to petitioner's trial Campbell was placed on probation for robbery. Justice Schaefer, joined by Chief Justice Klingbiel in dissent, found Campbell's testimony "inherently incredible." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#49" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 49</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#739" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 739</a></span>.</p>
<p>The theory of petitioner's application for habeas corpus did not rest upon allegations of physical coercion. Rather, it relied upon the hitherto undisputed testimony and alleged: (1) that petitioner vomited water and blood at the police station when he became ill from the withdrawal of narcotics; (2) that scopolamine is a "truth serum" and that this fact was not brought out at the motion to suppress <span class="star-pagination">*305</span> or at the trial; (3) that scopolamine "either alone or combined with Phenobarbital, is not the proper medication for a narcotic addict [and that] . . . [t]he effect of the intravenous injection of hyoscine and phenobarbital. . . is to produce a physiological and psychological condition adversely affecting the mind and will . . . [and] a psychic effect which removes the subject thus injected from the scope of reality; so that the person so treated is removed from contact with his environment, he is not able to see and feel properly, he loses proper use of his eye-sight, his hearing and his sense of perception and his ability to withstand interrogation"; (4) that the police doctor willfully suppressed this information and information of the identity of hyoscine and scopolamine, of his knowledge of these things, and of his intention to inject the hyoscine for the purpose of producing in Townsend "a physiological and psychological state . . . susceptible to interrogation resulting in . . . confessions . . ."; (5) that the injection caused Townsend to confess; (6) that on the evening of January 1, immediately after the injection of scopolamine, petitioner confessed to three murders and one robbery other than the murder of Boone and the robbery of Anagnost. Although there was some mention of other confessions at the trial, only the confession to the Anagnost robbery was specifically testified to.</p>
<p>Initially, in their answer, respondents stated: "Respondents admit the factual allegations of the petition well pleaded, but deny that Petitioner is held in custody by Respondents in violation of the constitution or laws of the United States . . . ." However, in the course of the first argument before the District Court it appeared that respondents admitted nothing alleged in the petition but merely took the position that the petition, on its face, was insufficient to entitle Townsend either to a hearing or to his release. In the course of the second argument, after the remand by this Court, respondents admitted <span class="star-pagination">*306</span> that "if the allegations of the petition are taken as true, then the petitioner is entitled to the relief he seeks . . . ," and that Townsend had confessed to at least five crimes after the injection of hyoscine. But respondents denied that "petitioner was adversely influenced by its [the hyoscine's] administration to the extent that his confession was obtained involuntarily"; that "Hyoscine is the truth serum"; that "the police surgeon or the prosecution concealed pertinent, material and relevant facts"; or that hyoscine was an improper medication under the circumstances. Despite respondents' concession that a dispute as to these facts existed, the district judge denied Townsend the opportunity to call witnesses or to produce other evidence in support of his allegations and dismissed the petition.</p>
<p>Before we granted the most recent petition for certiorari we requested respondents to submit an additional response directed to certain of the allegations of the petition for habeas corpus. Respondents submitted an "additional answer to petition for habeas corpus" in which they again admitted that Townsend had made confessions immediately after the injection of drugs. Specifically they admitted that petitioner confessed to the robberies of Anagnost and one Joseph Martin and to the murders of Boone, Thomas Johnson, Johnny Stinson, and Willis Thompson. The additional answer revealed the following additional information respecting Townsend's confessions to these crimes. Anagnost had identified another person, rather than petitioner, as his assailant. Thomas Johnson, before his death, had stated that his injury had been an accident. The Assistant State's Attorney did not even bother to transcribe Townsend's statement with respect to Thompson's murder "because the defendant could not recall the details of the assault which led to the death . . . ." At the Thompson coroner's inquest, when <span class="star-pagination">*307</span> the deputy coroner noted that Townsend was then unable to remember even that he had committed the crime, Officer Cagney complained: "Why shouldn't we be given credit for these Clean-ups." Despite these circumstances which made conviction for the Anagnost robbery and the Johnson and Thompson murders, at best, a remote possibility, petitioner was indicted for all of the crimes to which he had confessed. However, after a jury trial, he was acquitted of the murder of Johnny Stinson, and on the very day that he was sentenced to death for the Boone murder, on the motion of the prosecutor, the indictments for the murders of Johnson and Thompson and for the robberies of Anagnost and Martin were dismissed.</p>
<p>Although the petition for habeas corpus contains allegations which would constitute a claim that the police doctor, at the trial, had perjured himself, the heart of Townsend's claim is that his confession was inadmissible simply because it was caused by the injection of hyoscine. We must first determine whether petitioner's allegations, if proved, would establish the right to his release.</p>
<p></p>
<h2>I.</h2>
<p>Numerous decisions of this Court have established the standards governing the admissibility of confessions into evidence. If an individual's "will was overborne"<sup>[2]</sup> or if his confession was not "the product of a rational intellect and a free will,"<sup>[3]</sup> his confession is inadmissible because coerced. These standards are applicable whether a confession is the product of physical intimidation or psychological pressure and, of course, are equally applicable to a drug-induced statement. It is difficult to imagine a situation in which a confession would be less the product of a free intellect, less voluntary, than when brought <span class="star-pagination">*308</span> about by a drug having the effect of a "truth serum."<sup>[4]</sup> It is not significant that the drug may have been administered and the questions asked by persons unfamiliar with hyoscine's properties as a "truth serum," if these properties exist. Any questioning by police officers which <i>in fact</i> produces a confession which is not the product of a free intellect renders that confession inadmissible.<sup>[5]</sup> The <span class="star-pagination">*309</span> Court has usually so stated the test. See, <i>e. g., </i><i>Stroble</i> v. <i>California,</i> <span class="citation" data-id="9420722"><a href="/opinion/104997/stroble-v-california/" aria-description="Citation for case: Stroble v. California">343 U. S. 181</a></span>, 190: "If the confession which petitioner made . . . was in fact involuntary, the conviction cannot stand . . . ." And in <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199</a></span>, we held irrelevant the absence of evidence of improper purpose on the part of the questioning officers. There the evidence indicated that the interrogating officers thought the defendant sane when he confessed, but we judged the confession inadmissible because the probability was that the defendant was in fact insane at the time.</p>
<p>Thus we conclude that the petition for habeas corpus alleged a deprivation of constitutional rights. The remaining question before us then is whether the District Court was required to hold a hearing to ascertain the facts which are a necessary predicate to a decision of the ultimate constitutional question.</p>
<p>The problem of the power and duty of federal judges, on habeas corpus, to hold evidentiary hearingsthat is, to try issues of fact<sup>[6]</sup> anewis a recurring one. The Court last dealt at length with it in <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">344 U. S. 443</a></span>, in opinions by Justices Reed and Frankfurter, both speaking for a majority of the Court. Since then, <span class="star-pagination">*310</span> we have but touched upon it.<sup>[7]</sup> We granted certiorari in the 1959 Term to consider the question, but ultimately disposed of the case on a more immediate ground. <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#540" aria-description="Citation for case: Rogers v. Richmond">365 U. S. 534, 540</a></span>. It has become apparent that the opinions in <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen, supra</a></span></i><i>,</i> do not provide answers for all aspects of the hearing problem for the lower federal courts, which have reached widely divergent, in fact often irreconcilable, results.<sup>[8]</sup> We mean to express no opinion on the correctness of particular decisions. But we think that it is appropriate at this time to elaborate the considerations which ought properly to govern the grant or denial of evidentiary hearings in federal habeas corpus proceedings.</p>
<p></p>
<h2>II.</h2>
<p>The broad considerations bearing upon the proper interpretation of the power of the federal courts on habeas corpus are reviewed at length in the Court's opinion in <i>Fay</i> <span class="star-pagination">*311</span> v. <i>Noia</i><i>, post,</i> p. 391, and need not be repeated here. We pointed out there that the historic conception of the writ, anchored in the ancient common law and in our Constitution as an efficacious and imperative remedy for detentions of fundamental illegality, has remained constant to the present day. We pointed out, too, that the Act of February 5, 1867, c. 28, § 1, <span class="citation no-link">14 Stat. 385</span>-386, which in extending the federal writ to state prisoners described the power of the federal courts to take testimony and determine the facts <i>de novo</i> in the largest terms, restated what apparently was the common-law understanding. <i>Fay</i> v. <i>Noia</i><i>, post,</i> p. 416, n. 27. The hearing provisions of the 1867 Act remain substantially unchanged in the present codification. <span class="citation no-link">28 U. S. C. § 2243</span>. In construing the mandate of Congress, so plainly designed to afford a trial-type proceeding in federal court for state prisoners aggrieved by unconstitutional detentions, this Court has consistently upheld the power of the federal courts on habeas corpus to take evidence relevant to claims of such detention. "Since <i>Frank</i> v. <i>Mangum,</i> <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#331" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309, 331</a></span>, this Court has recognized that habeas corpus in the federal courts by one convicted of a criminal offense is a proper procedure `to safeguard the liberty of all persons within the jurisdiction of the United States against infringement through any violation of the Constitution,' even though the events which were alleged to infringe did not appear upon the face of the record of his conviction." <i>Hawk</i> v. <i>Olson,</i> <span class="citation" data-id="104196"><a href="/opinion/104196/hawk-v-olson/#274" aria-description="Citation for case: Hawk v. Olson">326 U. S. 271, 274</a></span>. <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span></i> and numerous other cases have recognized this.</p>
<p>The rule could not be otherwise. The whole history of the writits unique developmentrefutes a construction of the federal courts' habeas corpus powers that would assimilate their task to that of courts of appellate review. The function on habeas is different. It is to test by way of an original civil proceeding, independent of the normal <span class="star-pagination">*312</span> channels of review of criminal judgments, the very gravest allegations. State prisoners are entitled to relief on federal habeas corpus only upon proving that their detention violates the fundamental liberties of the person, safeguarded against state action by the Federal Constitution. Simply because detention so obtained is intolerable, the opportunity for redress, which presupposes the opportunity to be heard, to argue and present evidence, must never be totally foreclosed. See <i>Frank</i> v. <i>Mangum,</i> <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#345" aria-description="Citation for case: Frank v. Mangum">237 U. S. 309, 345-350</a></span> (dissenting opinion of Mr. Justice Holmes). It is the typical, not the rare, case in which constitutional claims turn upon the resolution of contested factual issues. Thus a narrow view of the hearing power would totally subvert Congress' specific aim in passing the Act of February 5, 1867, of affording state prisoners a forum in the federal trial courts for the determination of claims of detention in violation of the Constitution. The language of Congress, the history of the writ, the decisions of this Court, all make clear that the power of inquiry on federal habeas corpus is plenary. Therefore, where an applicant for a writ of habeas corpus alleges facts which, if proved, would entitled him to relief, the federal court to which the application is made has the power to receive evidence and try the facts anew.</p>
<p></p>
<h2>III.</h2>
<p>We turn now to the considerations which in certain cases may make exercise of that power mandatory. The appropriate standardwhich must be considered to supersede, to the extent of any inconsistencies, the opinions in <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span></i>is this: Where the facts are in dispute, the federal court in habeas corpus must hold an evidentiary hearing if the habeas applicant did not receive a full and fair evidentiary hearing in a state court, either at the time of the trial or in a collateral proceeding. In other words a federal evidentiary hearing is required <span class="star-pagination">*313</span> unless the state-court trier of fact has after a full hearing reliably found the relevant facts.<sup>[9]</sup></p>
<p>It would be unwise to overly particularize this test. The federal district judges are more intimately familiar with state criminal justice, and with the trial of fact, than are we, and to their sound discretion must be left in very large part the administration of federal habeas corpus. But experience proves that a too general standardthe "exceptional circumstances" and "vital flaw" tests of the opinions in <i>Brown</i> v. <i><span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/" aria-description="Citation for case: Brown v. Allen">Allen</a></span></i>does not serve adequately to explain the controlling criteria for the guidance of the federal habeas corpus courts. Some particularization may therefore be useful. We hold that a federal court must grant an evidentiary hearing to a habeas applicant under the following circumstances: If (1) the merits of the factual dispute were not resolved in the state hearing; (2) the state factual determination is not fairly supported by the record as a whole; (3) the fact-finding procedure employed by the state court was not adequate to afford a full and fair hearing; (4) there is a substantial allegation of newly discovered evidence; (5) the material facts were not adequately developed at the state-court hearing; or (6) for any reason it appears that the state trier of fact did not afford the habeas applicant a full and fair fact hearing.</p>
<p>(1) There cannot even be the semblance of a full and fair hearing unless the state court actually reached and <span class="star-pagination">*314</span> decided the issues of fact tendered by the defendant. Thus, if no express findings of fact have been made by the state court, the District Court must initially determine whether the state court has impliedly found material facts. No relevant findings have been made unless the state court decided the constitutional claim tendered by the defendant on the merits. If relief has been denied in prior state collateral proceedings after a hearing but without opinion, it is often likely that the decision is based upon a procedural issuethat the claim is not collaterally cognizableand not on the merits. On the other hand, if the prior state hearing occurred in the course of the original trialfor example, on a motion to suppress allegedly unlawful evidence, as in the instant caseit will usually be proper to assume that the claim was rejected on the merits.</p>
<p>If the state court has decided the merits of the claim but has made no express findings, it may still be possible for the District Court to reconstruct the findings of the state trier of fact, either because his view of the facts is plain from his opinion or because of other indicia. In some cases this will be impossible, and the Federal District Court will be compelled to hold a hearing.</p>
<p>Reconstruction is not possible if it is unclear whether the state finder applied correct constitutional standards in disposing of the claim. Under such circumstances the District Court cannot ascertain whether the state court found the law or the facts adversely to the petitioner's contentions. Since the decision of the state trier of fact may rest upon an error of law rather than an adverse determination of the facts, a hearing is compelled to ascertain the facts. Of course, the possibility of legal error may be eliminated in many situations if the fact finder has articulated the constitutional standards which he has applied. Furthermore, the coequal responsibilities of state and federal judges in the administration of federal <span class="star-pagination">*315</span> constitutional law are such that we think the district judge may, in the ordinary case in which there has been no articulation, properly assume that the state trier of fact applied correct standards of federal law to the facts, in the absence of evidence, such as was present in <i>Rogers</i> v. <i><span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">Richmond</a></span>,</i> that there is reason to suspect that an incorrect standard was in fact applied.<sup>[10]</sup> Thus, if third-degree methods of obtaining a confession are alleged and the state court refused to exclude the confession from evidence, the district judge may assume that the state trier found the facts against the petitioner, the law being, of course, that third-degree methods necessarily produce a coerced confession.</p>
<p>In any event, even if it is clear that the state trier of fact utilized the proper standard, a hearing is sometimes required if his decision presents a situation in which the "so-called facts and their constitutional significance [are] . . . so blended that they cannot be severed in consideration." <i>Rogers</i> v. <span class="citation" data-id="9422147"><a href="/opinion/106192/rogers-v-richmond/#546" aria-description="Citation for case: Rogers v. Richmond"><i>Richmond, supra,</i> at 546</a></span>. See <i>Frank</i> v. <span class="citation" data-id="9418283"><a href="/opinion/98441/frank-v-mangum/#347" aria-description="Citation for case: Frank v. Mangum"><i>Mangum, supra,</i> at 347</a></span> (Holmes, J., dissenting). Unless the district judge can be reasonably certain that the state trier would have granted relief if he had believed petitioner's allegations, he cannot be sure that the state trier in denying relief disbelieved these allegations. If any combination of the facts alleged would prove a violation of constitutional rights and the issue of law on those facts presents a difficult or novel problem for decision, any hypothesis as to the relevant factual determinations of the state trier involves the purest speculation. The federal <span class="star-pagination">*316</span> court cannot exclude the possibility that the trial judge believed facts which showed a deprivation of constitutional rights and yet (erroneously) concluded that relief should be denied. Under these circumstances it is impossible for the federal court to reconstruct the facts, and a hearing must be held.</p>
<p>(2) This Court has consistently held that state factual determinations not fairly supported by the record cannot be conclusive of federal rights. <i>Fiske</i> v. <i>Kansas,</i> <span class="citation" data-id="101098"><a href="/opinion/101098/fiske-v-kansas/#385" aria-description="Citation for case: Fiske v. Kansas">274 U. S. 380, 385</a></span>; <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208-209</a></span>. Where the fundamental liberties of the person are claimed to have been infringed, we carefully scrutinize the state-court record. See, <i>e. g., </i><i>Blackburn</i> v. <i><span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/" aria-description="Citation for case: Blackburn v. Alabama">Alabama, supra</a></span></i><i>; </i><i>Moore</i> v. <i>Michigan,</i> <span class="citation" data-id="9841953"><a href="/opinion/105589/moore-v-michigan/" aria-description="Citation for case: Moore v. Michigan">355 U. S. 155</a></span>. The duty of the Federal District Court on habeas is no less exacting.</p>
<p>(3) However, the obligation of the Federal District Court to scrutinize the state-court findings of fact goes farther than this. Even if all the relevant facts were presented in the state-court hearing, it may be that the fact-finding procedure there employed was not adequate for reaching reasonably correct results. If the state trial judge has made serious procedural errors (respecting the claim pressed in federal habeas) in such things as the burden of proof, a federal hearing is required. Even where the procedure employed does not violate the Constitution, if it appears to be seriously inadequate for the ascertainment of the truth, it is the federal judge's duty to disregard the state findings and take evidence anew. Of course, there are procedural errors so grave as to require an appropriate order directing the habeas applicant's release unless the State grants a new trial forthwith. Our present concern is with errors which, although less serious, are nevertheless grave enough to deprive the state evidentiary hearing of its adequacy as a means of finally determining facts upon which constitutional rights depend.</p>
<p><span class="star-pagination">*317</span> (4) Where newly discovered evidence is alleged in a habeas application, evidence which could not reasonably have been presented to the state trier of facts, the federal court must grant an evidentiary hearing. Of course, such evidence must bear upon the constitutionality of the applicant's detention; the existence merely of newly discovered evidence relevant to the guilt of a state prisoner is not a ground for relief on federal habeas corpus. Also, the district judge is under no obligation to grant a hearing upon a frivolous or incredible allegation of newly discovered evidence.</p>
<p>(5) The conventional notion of the kind of newly discovered evidence which will permit the reopening of a judgment is, however, in some respects too limited to provide complete guidance to the federal district judge on habeas. If, for any reason not attributable to the inexcusable neglect of petitioner, see <i>Fay</i> v. <i>Noia</i><i>, post,</i> p. 438 (Part V), evidence crucial to the adequate consideration of the constitutional claim was not developed at the state hearing, a federal hearing is compelled. The standard of inexcusable default set down in <i>Fay</i> v. <i>Noia</i> adequately protects the legitimate state interest in orderly criminal procedure, for it does not sanction needless piecemeal presentation of constitutional claims in the form of deliberate by-passing of state procedures. Compare <i>Price</i> v. <i>Johnston,</i> <span class="citation" data-id="9420168"><a href="/opinion/104557/price-v-johnston/" aria-description="Citation for case: Price v. Johnston">334 U. S. 266</a></span>, 291: "The primary purpose of a <i>habeas corpus</i> proceeding is to make certain that a man is not unjustly imprisoned. And if for some justifiable reason he was previously unable to assert his rights or was unaware of the significance of relevant facts, it is neither necessary nor reasonable to deny him all opportunity of obtaining judicial relief."</p>
<p>(6) Our final category is intentionally open-ended because we cannot here anticipate all the situations wherein a hearing is demanded. It is the province of the district judges first to determine such necessities in accordance <span class="star-pagination">*318</span> with the general rules. The duty to try the facts anew exists in every case in which the state court has not after a full hearing reliably found the relevant facts.</p>
<p></p>
<h2>IV.</h2>
<p>It is appropriate to add a few observations concerning the proper application of the test we have outlined.</p>
<p><i>First.</i> The purpose of the test is to indicate the situations in which the holding of an evidentiary hearing is mandatory. In all other cases where the material facts are in dispute, the holding of such a hearing is in the discretion of the district judge. If he concludes that the habeas applicant was afforded a full and fair hearing by the state court resulting in reliable findings, he may, and ordinarily should, accept the facts as found in the hearing. But he need not. In every case he has the power, constrained only by his sound discretion, to receive evidence bearing upon the applicant's constitutional claim. There is every reason to be confident that federal district judges, mindful of their delicate role in the maintenance of proper federal-state relations, will not abuse that discretion. We have no fear that the hearing power will be used to subvert the integrity of state criminal justice or to waste the time of the federal courts in the trial of frivolous claims.</p>
<p><i>Second.</i> Although the district judge may, where the state court has reliably found the relevant facts, defer to the state court's findings of fact, he may not defer to its findings of law. It is the district judge's duty to apply the applicable federal law to the state court fact findings independently. The state conclusions of law may not be given binding weight on habeas. That was settled in <i>Brown</i> v. <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#506" aria-description="Citation for case: Brown v. Allen"><i>Allen, supra,</i> at 506</a></span> (opinion of Mr. Justice Frankfurter).</p>
<p><span class="star-pagination">*319</span> <i>Third.</i> A District Court sitting in habeas corpus clearly has the power to compel production of the complete state-court record. Ordinarily such a record including the transcript of testimony (or if unavailable some adequate substitute, such as a narrative record), the pleadings, court opinions, and other pertinent documents is indispensable to determining whether the habeas applicant received a full and fair state-court evidentiary hearing resulting in reliable findings. See <i>United States ex rel. Jennings</i> v. <i>Ragan,</i> <span class="citation" data-id="105813"><a href="/opinion/105813/united-states-ex-rel-jennings-v-ragen/" aria-description="Citation for case: United States Ex Rel. Jennings v. Ragen">358 U. S. 276</a></span>; <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="1208179"><a href="/opinion/1208179/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">359 U. S. 64</a></span>. Of course, if because no record can be obtained the district judge has no way of determining whether a full and fair hearing which resulted in findings of relevant fact was vouchsafed, he must hold one. So also, there may be cases in which it is more convenient for the district judge to hold an evidentiary hearing forthwith rather than compel production of the record. It is clear that he has the power to do so.</p>
<p><i>Fourth.</i> It rests largely with the federal district judges to give practical form to the principles announced today. We are aware that the too promiscuous grant of evidentiary hearings on habeas could both swamp the dockets of the District Courts and cause acute and unnecessary friction with state organs of criminal justice, while the too limited use of such hearings would allow many grave constitutional errors to go forever uncorrected. The accommodation of these competing factors must be made on the front line, by the district judges who are conscious of their paramount responsibility in this area.</p>
<p></p>
<h2>V.</h2>
<p>Application of the foregoing principles to the particular litigation before us is not difficult. Townsend received an evidentiary hearing at his original trial, where his confession was held to be voluntary. Having exhausted his <span class="star-pagination">*320</span> state remedies without receiving any further such hearing, he turned to the Federal District Court. Twice now, habeas corpus relief has been denied without an evidentiary hearing. On appeal from the second denial, the Court of Appeals held that "[o]n habeas corpus, the district court's inquiry is limited to a study of the <i>undisputed</i> portions of the record." That formulation was error. And we believe that on this record it was also error to refuse Townsend an evidentiary hearing in the District Court. The state trial judge rendered neither an opinion, conclusions of law, nor findings of fact. He made no charge to the jury setting forth the constitutional standards governing the admissibility of confessions. In short, there are no indicia which would indicate whether the trial judge applied the proper standard of federal law in ruling upon the admissibility of the confession. The Illinois Supreme Court opinion rendered at the time of direct appeal contains statements which might indicate that the court thought the confession was admissible if it satisfied the "coherency" standard. Under that test the confession would be admissible "[s]o long as the accused [was] . . . capable of making a narrative of past events or of stating his own participation in the crime . . . ." <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#43" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, at 43</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#736" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d, at 736</a></span>. As we have indicated in Part I of this opinion, this test is not the proper one. Possibly the state trial judge believed that the admissibility of allegedly drug-induced confessions was to be judged by the "coherency" standard.<sup>[11]</sup> However, even if this possibility could be eliminated, and it could be ascertained <span class="star-pagination">*321</span> that correct standards of law were applied, it is still unclear whether the state trial judge would have excluded Townsend's confession as involuntary if he had believed the evidence which Townsend presented at the motion to suppress. The problem which the trial judge faced was novel and by no means without difficulty. We believe that the Federal District Court could not conclude that the state trial judge admitted the confession because he disbelieved the evidence which would show that it was involuntary. We believe that the findings of fact of the state trier could not be successfully reconstructed. We hold that, for this reason, an evidentiary hearing was compelled.<sup>[12]</sup></p>
<p>Furthermore, a crucial fact was not disclosed at the state-court hearing: that the substance injected into Townsend before he confessed has properties which may trigger statements in a legal sense involuntary.<sup>[13]</sup> This fact was vital to whether his confession was the product of a free will and therefore admissible. To be sure, there was medical testimony as to the general properties of hyoscine, from which might have been inferred the conclusion <span class="star-pagination">*322</span> that Townsend's power of resistance had been debilitated. But the crucially informative characterization of the drug, the characterization which would have enabled the judge and jury, mere laymen, intelligently to grasp the nature of the substance under inquiry, was inexplicably omitted from the medical experts' testimony. Under the circumstances, disclosure of the identity of hyoscine as a "truth serum" was indispensable to a fair, rounded, development of the material facts. And the medical experts' failure to testify fully cannot realistically be regarded as Townsend's inexcusable default. See <i>Fay</i> v. <i>Noia</i><i>, post,</i> p. 438 (Part V).</p>
<p>On the remand it would not, of course, be sufficient for the District Court merely to hear new evidence and to read the state-court record. Where an unresolved factual dispute exists, demeanor evidence is a significant factor in adjudging credibility. And questions of credibility, of course, are basic to resolution of conflicts in testimony. To be sure, the state-court record is competent evidence,<sup>[14]</sup> and either party may choose to rely solely upon the evidence contained in that record, but the petitioner, and the State, must be given the opportunity to present other testimonial and documentary evidence relevant to the disputed issues. This was not done here.</p>
<p>In deciding this case as we do, we do not mean to prejudge the truth of the allegations of the petition for habeas corpus. We decide only that on this record the federal district judge was obliged to hold a hearing.</p>
<p><i>Reversed and remanded.</i></p>
<p>MR. JUSTICE GOLDBERG, concurring.</p>
<p>I join in the opinion and judgment of the Court and add a few words by way of comment on the dissenting opinion of my Brother STEWART.</p>
<p><span class="star-pagination">*323</span> I cannot agree with MR. JUSTICE STEWART that the instructions given to the jury by the trial judge on the issue of credibility indicate the application of a proper constitutional test to measure the voluntarinessand hence the admissibilityof the petitioner's disputed confession of the Boone murder. In my view, the very portions of the instructions excerpted by my Brother STEWART support, if anything, the contrary conclusion that an improper and constitutionally impermissible standard was utilized by the trial judge himself in the suppression hearing.</p>
<p>If, as suggested by my Brother STEWART, these instructions are taken to evidence the exclusionary standard applied by the trial judge in ruling on the petitioner's motion to suppress, they reflect error of constitutional dimension, as does the standard of admissibility contained in the affirming opinion of the Illinois Supreme Court. While the appellate court, as pointed out in the opinion of THE CHIEF JUSTICE, see <i>ante,</i> pp. 319-321, appears to have adopted a test of "coherency" to measure the admissibility of the confession, the trial court seemingly concluded that inducement of amnesia was a prerequisite to disregard of the confession. Both standards, whether or not intended to incorporate similar elements, fail to conform to the requisite test.</p>
<p>The third paragraph of the instructions quoted by my Brother STEWART in footnote 2, <i>post,</i> p. 330, advises the jury that it might discount the confession if it found that administration of the drug caused the petitioner to "lose his memory," to suffer "a state of amnesia" during the period of questioning, <i>and</i> to be unable "to control his answers or to assert his will by denying the crime charged." By use of the conjunctive to incorporate the requirement of loss of control, this instruction indicates the trial court's apparent view that if the drug had the effect of overbearing the petitioner's will but did not also cause loss of <span class="star-pagination">*324</span> memory, the confession would nonetheless remain acceptable evidence of guilt. This conclusion is buttressed by the instruction quoted in the concluding paragraph of note 2 in my Brother STEWART'S dissenting opinion, in which the trial court indicates that the confession might be disregarded by the jury not simply if the drug had the effect asserted by the petitioner's expert in response to a hypothetical question, but only if, <i>in addition,</i> the drug so affected the petitioner's consciousness that "he did not know what he was doing." The petitioner may have been fully aware of what he was doing in confessing and may have suffered no loss of memory, but that is not the issue. The crucial question, and the measure of evidentiary propriety under the Constitution, is whether the drug whatever label was or was not affixed to itso overbore the petitioner's will that he was unable to resist confessing. Whether or not he was conscious of what he was doing, the petitioner could, because of the drug, have been wholly unable to stop himself from admitting guilt.<sup>[*]</sup></p>
<p>In the absence of contrary indications, I think we must recognize that the misconception of the constitutional standard evidenced by these instructions may well have infected the trial judge's ruling at the suppression hearing. The inference of error is not negatived by the remainder of the instructions, which permit disregard of the confession if induced by force, physical or mental, duress, or promise of reward. In the context of the instructions as a whole, these references to "voluntariness" do not meet the problems raised by the administration of the drug to the petitioner and do not vitiate the crucial inference that <span class="star-pagination">*325</span> the trial judge viewed exclusion as dependent upon the presence of facts in addition to a drug-induced sterilization of the petitioner's will.</p>
<p>For the reasons contained in the opinion of the Court, and on the basis of what I believe to be the wholly fair inference that the trial court misconceived the proper constitutional measure of admissibility of the petitioner's confession, the lack of any indication that the trial court did utilize the correct test, and the state appellate court's apparent application of a similarly erroneous standard, I agree that a hearing must be held below.</p>
<p>Finally, the Court's opinion does not warrant my Brother STEWART'S criticism as to the propriety or wisdom of articulating standards to govern the grant of evidentiary hearings in habeas corpus proceedings. The setting of certain standards is essential to disposition of this case and a definition of their scope and application is an appropriate exercise of this Court's adjudicatory obligations. Particularly when, as here, the Court is directing the federal judiciary as to its role in applying the historic remedy in a difficult and sensitive area involving large issues of federalism, the careful discharge of our function counsels that, "in order to preclude individualized enforcement of the Constitution in different parts of the Nation, [we] . . . lay down as specifically as the nature of the problem permits the standards or directions that should govern the District Judges in the disposition of applications for habeas corpus by prisoners under sentence of State courts." <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#501" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 501-502</a></span> (separate opinion of Mr. Justice Frankfurter).</p>
<p>MR. JUSTICE STEWART, whom MR. JUSTICE CLARK, MR. JUSTICE HARLAN, and MR. JUSTICE WHITE join, dissenting.</p>
<p>The basis for my disagreement with the Court can perhaps best be explained if I define at the outset the several areas in which I am entirely in accord with the Court's <span class="star-pagination">*326</span> opinion. First, as to the underlying issue of constitutional law, I completely agree that a confession induced by the administration of drugs is constitutionally inadmissible in a criminal trial. Secondly, I agree that the Court of Appeals in this case stated an erroneous standard when it said that "[o]n habeas corpus, the district court's inquiry is limited to a study of the <i>undisputed</i> portions of the record. . . ." <span class="citation" data-id="250462"><a href="/opinion/250462/united-states-of-america-ex-rel-charles-townsend-v-frank-g-sain-sheriff/#329" aria-description="Citation for case: United States of America Ex Rel. Charles Townsend v....">276 F. 2d 324, 329</a></span>. Thirdly, I agree that where an applicant for a writ of habeas corpus alleges facts which, if proved, would entitle him to relief, the federal court to which the application is made has the <i>power</i> to receive evidence and try the facts anew.<sup>[1]</sup></p>
<p>I differ with the Court's disposition of this case in two important respects. First, I strongly doubt the wisdom of using this caseor any otheras a vehicle for cataloguing in advance a set of standards which are inflexibly to compel district judges to grant evidentiary hearings in habeas corpus proceedings. Secondly, I think that a <i>de novo</i> evidentiary hearing is not required in the present case, even under the very standards which the Court's opinion elaborates.</p>
<p></p>
<h2>I.</h2>
<p>I have no quarrel with the Court's statement of the basic governing principle which should determine whether a hearing is to be had in a federal habeas corpus <span class="star-pagination">*327</span> proceeding: "Where the facts are in dispute, the federal court in habeas corpus must hold an evidentiary hearing if the habeas applicant did not receive a full and fair evidentiary hearing in a state court, either at the time of the trial or in a collateral proceeding." <i>Ante,</i> p. 312. But the Court rightly says that "[i]t would be unwise to overly particularize this test," and I think that in attempting to erect detailed hearing standards for the myriad situations presented by federal habeas corpus applications, the Court disregards its own wise admonition.</p>
<p>The Court has done little more today than to supply new phrasesimprecise in scope and uncertain in meaning for the habeas corpus vocabulary of District Court judges. And because they purport to establish mandatory requirements rather than guidelines, the tests elaborated in the Court's opinion run the serious risk of becoming talismanic phrases, the mechanistic invocation of which will alone determine whether or not a hearing is to be had.</p>
<p>More fundamentally, the enunciation of an elaborate set of standards governing habeas corpus hearings is in no sense required, or even invited, in order to decide the case before us, and the many pages of the Court's opinion which set these standards forth cannot, therefore, be justified even in terms of the normal function of dictum. The reasons for the rule against advisory opinions which purport to decide questions not actually in issue are too well established to need repeating at this late date. See, <i>e. g., </i><i>Marine Cooks</i> v. <i>Panama S. S. Co.,</i> <span class="citation" data-id="9421959"><a href="/opinion/106031/marine-cooks-stewards-v-panama-steamship-co/#368" aria-description="Citation for case: Marine Cooks &amp; Stewards v. Panama Steamship Co.">362 U. S. 365, 368, n. 5</a></span>; <i>Machinists Local</i> v. <i>Labor Board,</i> <span class="citation" data-id="9421969"><a href="/opinion/106040/local-lodge-no-1424-international-assn-of-machinists-v-national-labor/#415" aria-description="Citation for case: Local Lodge No. 1424, International Ass&#x27;n of MacHinists...">362 U. S. 411, 415, n. 5</a></span>. I regard these reasons as peculiarly persuasive in the present context. We should not try to hedge in with inflexible rules what is essentially an extraordinary writ, designed to do justice in extraordinary and often unpredictable situations.</p>
<p></p>
<h2>
<span class="star-pagination">*328</span> II.</h2>
<p>Even accepting the Court's detailed hearing standards <i>in toto,</i> however, I cannot agree that any one of them requires the District Court to hold a new evidentiary hearing in the present case. And I think, putting these rigid formulations to one side, that accepted principles governing the fair and prompt administration of criminal justice within our federal system affirmatively counsel <i>against</i> a <i>de novo</i> federal court hearing in this case.</p>
<p>The Court refers to two specific defects which it feels compel a hearing in the District Court: the absence of "indicia which would indicate whether the trial judge applied the proper standard of federal law in ruling upon the admissibility of the confession" and the fact that it was not disclosed in the state hearing that "the substance injected into Townsend before he confessed has properties which may trigger statements in a legal sense involuntary." Since the lengthy extracts from the testimony and pleadings in the Court's opinion do not seem to me to bear on these issues, it becomes necessary to sketch the prior proceedings in this case to indicate why I think the Court is mistaken in concluding that a new hearing is required.</p>
<p>During the early morning hours of January 1, 1954, the petitioner was arrested by the Chicago police. He admitted having given himself an injection of heroin 90 minutes before his arrest. Within an hour of his arrest, he was questioned for 30 minutes about various crimes, all of which he denied having committed. He was not questioned again until that evening.</p>
<p>Shortly after the evening questioning began, the petitioner complained of stomach pains and requested a doctor. A police surgeon was summoned, and he administered an injection consisting of 2 cc.'s of a saline solution in which 1/230 grain of hyoscine hydrobromide and 1/8 <span class="star-pagination">*329</span> grain of phenobarbital were dissolved. Slightly more than an hour later, the petitioner confessed to the murder of Boone. The following day, 15 hours after the police surgeon had administered the hyoscine, the petitioner initialed a copy of his previous night's statement in the offices of the State's Attorney General. At the coroner's hearing on January 4, the petitioner again confessed to the Boone killing.</p>
<p></p>
<h2>A. THE STANDARD OF FEDERAL LAW APPLIED BY THE STATE TRIAL COURT IN RULING UPON THE ADMISSIBILITY OF THE CONFESSION.</h2>
<p>At the trial, the petitioner's lawyer objected to introduction of the confession on the ground that it was involuntary. In accordance with Illinois practice, the motion to suppress was argued before the judge in the absence of the jury. During this proceeding, the petitioner testified that the injection had produced a temporary state of amnesia, that he could not remember making any confession, and that various other physical effects were produced. The police officers present at the petitioner's questioning stated that no change in the petitioner's demeanor suggesting any loss of his mental faculties had taken place as a result of the injection. On the question of the possible effects of the injection administered to the petitioner, Dr. Mansfield, the police surgeon and a licensed physician, testified for the State that he had treated thousands of narcotics addicts suffering from withdrawal symptoms, that in about 50% of such cases he had used the same treatment administered to the petitioner, and that he could recall no case in his experience where his use of hyoscine had produced loss of memory. A doctor of pharmacology (who was not a licensed physician) testified on behalf of the petitioner, and in answer to a hypothetical question stated that a person in the petitioner's condition at the time of interrogation could have <span class="star-pagination">*330</span> been suffering amnesia and partial loss of consciousness as the result of the treatment which had been administered to relieve the narcotic withdrawal symptoms. On cross-examination, this witness revealed that he had never actually seen the effects of hyoscine on a human and admitted that he was unfamiliar with its use in treating drug addicts. It is evident that a finder of fact could with reason have accorded more credibility to the evidence offered by the prosecution than to that offered by the defense.</p>
<p>It is true, as the Court today says, that in overruling the motion to suppress the confession, the trial judge did not explicitly spell out the exclusionary standards he was applying. The instructions to the jury at the end of the case, however, although directed to the question of credibility since that was the issue before the jury under Illinois procedurewere couched in terms of voluntariness, and they clearly established that the trial judge was aware of the correct constitutional standards to be applied.<sup>[2]</sup><span class="star-pagination">*331</span> Nothing in the record indicates that an incorrect standard was applied at the suppression hearing. Given these circumstances, I think it completely impermissible for us to assume that the trial judge did not apply "the proper standard of federal law in ruling upon the admissibility of the confession." Where, as here, a record is totally devoid of any indication that a state trial judge employed an erroneous constitutional standard, the presumption should surely be that the judge knew the law and correctly applied it. Certainly it is improper to presume that the trial judge did <i>not</i> know the law which the Constitution commands him to follow. Yet that is precisely the presumption which the Court makes in this case.</p>
<p></p>
<h2>
<span class="star-pagination">*332</span> B. DISCLOSURE OF THE "PROPERTIES" OF THE MEDICINE ADMINISTERED TO THE PETITIONER.</h2>
<p>Much of the evidence which had been presented to the judge alone was subsequently brought before the jury by defense counsel in an attempt to diminish the weight to be given to the confession. Additional evidence was also adduced by the prosecution, including testimony by another licensed physician, who made clear that hyoscine was identical with scopolamine. The case was submitted to the jury under unexceptionable instructions,<sup>[3]</sup> and the petitioner was convicted and sentenced to death. The Illinois Supreme Court, after reviewing in detail the evidence bearing on the voluntariness of the confession, affirmed the conviction. <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d 30</a></span>, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/" aria-description="Citation for case: The People v. Townsend">141 N. E. 2d 729</a></span>. This Court denied certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./355/850/">355 U. S. 850</a></span>; rehearing denied, <span class="citation multiple-matches"><a href="/c/U.%20S./355/886/">355 U. S. 886</a></span>.</p>
<p>The petitioner then instituted post-conviction proceedings in the state trial court. His claim in these proceedings was that the confession had been procured as a result of the administration of scopolamine, that the witnesses for the State were aware of the identity of scopolamine and hyoscine and had deliberately withheld the fact of this identity at trial, and that the petitioner had consequently not been afforded an opportunity to make clear the basis for his claim that his confession had been coerced. The trial court dismissed the petition, and the Supreme Court of Illinois affirmed. In an unpublished opinion, that court concluded as follows:</p>
<blockquote>"A study of our opinion on [the original appeal] discloses that all of the evidence with respect to the injection of hyoscine and phenobarbital was carefully considered by us in resolving the issue of the validity of petitioner's confession. (People vs. <span class="star-pagination">*333</span> Townsend, <span class="citation" data-id="9721211"><a href="/opinion/2120258/the-people-v-townsend/#35" aria-description="Citation for case: The People v. Townsend">11 Ill. 2d, 30, 35, 44</a></span>). Thus, it is clear that the issue of the effect of the drug on the confession was before us . . . . The only matter which was not presented then was the fact that hyoscine and scopolamine are identical. In an attempt to escape from the doctrine of <i>res judicata,</i> the present petition for a writ of error contends that this fact could not have been presented to us because it was unknown to petitioner and his counsel at the time. Assuming for the moment the truth of this statement, we are of the opinion that the mere fact that the drug which was administered to petitioner is known by two different names presents no constitutional issue. At the original trial there was extensive medical testimony as to the properties and effects of hyoscine. If hyoscine and scopolamine are, in fact, identical, the medical testimony as to these properties and effects would be the same, regardless of the name of the drug. In determining the effect of the drug on the validity of petitioner's confession, the vital issue was its nature and its effect, rather than its name. This issue was thoroughly presented, both in the trial court and in this Court. Furthermore, the claim by petitioner now that the State `suppressed' this identity of hyoscine and scopolamine at the trial is destroyed by reference to the bill of exceptions from the original trial. A State medical witness, on cross-examination by petitioner's counsel stated: `Scopolamine or hyoscine are the same.' "</blockquote>
<p>Even under the detailed hearing requirements announced today by the Court, therefore, I think it is clear that the district judge had no choice but to conclude, on the basis of his examination of the full record of the state proceedings, that a new hearing on habeas corpus would <span class="star-pagination">*334</span> not be proper. For the record of the state proceedings clearly shows that the petitioner received a full and fair hearing as to the factual foundation for his constitutional claim<i>i. e.,</i> as to the properties of the drug which had been administered to him and the circumstances surrounding his confession. A total of 3 medical experts and 17 lay witnesses testified. Their testimony was in conflict. The trial court determined upon this conflicting evidence that there was no factual basis for the petitioner's claim that his confession had been involuntary. There is nothing whatever in the record to support an inference that the trial court did not scrupulously apply a completely correct constitutional standard in determining that the confession was admissible.<sup>[4]</sup> The trial court's determination was fully reviewed by the Supreme Court of Illinois on appeal, and reviewed again in state post-conviction proceedings. To be sure, no witness at the trial used the phrase "truth serum"a phrase which has no precise medical or scientific meaning. Yet I cannot but agree with the Supreme Court of Illinois that the mere fact that a drug may be known by more than one name hardly presents a constitutional issue.</p>
<p>Under our Constitution the State of Illinois has the power and duty to administer its own criminal justice. In carrying out that duty, Illinois must, as must each State, conform to the Due Process Clause of the Fourteenth Amendment. I think Illinois has clearly accorded the petitioner due process in this case. To require a federal court now to hold a new trial of factual claims which were long ago fully and fairly determined in the courts of Illinois is, I think, to frustrate the fair and prompt administration of criminal justice, to disrespect the fundamental structure of our federal system, and to debase the Great Writ of Habeas Corpus.</p>
<p>I would affirm.</p>
<h2>NOTES</h2>
<p>[1]  The final defense witness who testified at the motion to suppress was excused. The following then transpired:
</p>
<p>"MR. BRANION [a defense attorney]: That's all we have, if the Court please.</p>
<p>"The COURT: The defense rests on this hearing?</p>
<p>"MR. BRANION: Defense rests.</p>
<p>"The COURT: Anything further from the State?</p>
<p>"MR. McGOVERN: The State rests for the purpose of this hearing, Judge.</p>
<p>"The COURT: Gentlemen, the Court will deny the motion to suppress and admit the statement into evidence and we will proceed with the presentation of the evidence [to the jury]."</p>
<p>[2]  <i>Reck</i> v. <i>Pate,</i> <span class="citation" data-id="9422259"><a href="/opinion/106278/reck-v-pate/#440" aria-description="Citation for case: Reck v. Pate">367 U. S. 433, 440</a></span>.</p>
<p>[3]  <i>Blackburn</i> v. <i>Alabama,</i> <span class="citation" data-id="105977"><a href="/opinion/105977/blackburn-v-alabama/#208" aria-description="Citation for case: Blackburn v. Alabama">361 U. S. 199, 208</a></span>.</p>
<p>[4]  Of course, there are many relevant circumstances in this case which a district judge would be required to consider in determining whether the injection of scopolamine caused Townsend to confess. Among these are his lack of counsel at the time, his drug addiction, the fact that he was a "near mental defective," and his youth and inexperience.</p>
<p>[5]  Respondents do not dispute this. In fact at the time of the second argument before the District Court respondents stated:
</p>
<p>"If it was a factto put it very bluntly as we will very shortly, and elaborate upon itif a truth serum was administered to the petitioner and he was influenced by the truth serum and gave an involuntary confession, upon which his conviction was obtained, then that is it."</p>
<p>It is at least generally recognized that the administration of sufficient doses of scopolamine will break down the will. Thus, it is stated in The Dispensatory of the United States (25th ed. 1955) 1223: "Many persons are excessively susceptible to scopolamine and toxic symptoms may occur; such symptoms are often very alarming. There are marked disturbances of intellection, ranging from complete disorientation to an active delirium . . . ." The early literature on the subject designated scopolamine as a "truth serum." It was thought to produce true confessions by criminal suspects. <i>E. g.,</i> House, Why Truth Serum Should be Made Legal, 42 Medico-Legal Journal 138 (1925). And as recently as 1940 Dean Wigmore suggested that scopolamine might be useful in criminal interrogation. 3 Wigmore on Evidence (3d ed. 1940) § 998, at 642. However, some more recent commentators suggest that scopolamine's use is not likely to produce true confessions. On the contrary it is said:</p>
<p>"Unfortunately, persons under the influence of drugs are very suggestible and may confess to crimes which they have not committed. False or misleading answers may be given, especially when questions are improperly phrased. For example, if the police officer asserted in a confident tone `You did steal the money, didn't you?', a suggestible suspect might easily give a false affirmative answer." MacDonald, Truth Serum, 46 J. Crim. L. 259, 259-260 (1955). We make no findings as to either the medical properties of scopolamine or the likely effect of the dosage administered to Townsend. However, whether scopolamine produces true confessions or false confessions, if it in fact caused Townsend to make statements, those statements were constitutionally inadmissible.</p>
<p>[6]  By "issues of fact" we mean to refer to what are termed basic, primary, or historical facts: facts "in the sense of a recital of external events and the credibility of their narrators . . . ." <i>Brown</i> v. <i>Allen,</i> <span class="citation" data-id="9420862"><a href="/opinion/105074/brown-v-allen/#506" aria-description="Citation for case: Brown v. Allen">344 U. S. 443, 506</a></span> (opinion of Mr. Justice Frankfurter). So-called mixed questions of fact and law, which require the application of a legal standard to the historical-fact determinations, are not facts in this sense.</p>
<p>[7]  See <i>Thomas</i> v. <i>Arizona,</i> <span class="citation" data-id="105683"><a href="/opinion/105683/thomas-v-arizona/" aria-description="Citation for case: Thomas v. Arizona">356 U. S. 390</a></span>; <i>Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="105726"><a href="/opinion/105726/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">357 U. S. 220</a></span> (denial of certiorari with accompanying statement); <i>United States ex rel. Jennings</i> v. <i>Ragen,</i> <span class="citation" data-id="105813"><a href="/opinion/105813/united-states-ex-rel-jennings-v-ragen/" aria-description="Citation for case: United States Ex Rel. Jennings v. Ragen">358 U. S. 276</a></span> (<i>per curiam</i>); <i>Townsend</i> v. <i>Sain,</i> <span class="citation" data-id="1208179"><a href="/opinion/1208179/townsend-v-sain/" aria-description="Citation for case: Townsend v. Sain">359 U. S. 64</a></span> (<i>per curiam</i>) (vacating judgment on authority of <i>Jennings</i> v. <i><span class="citation" data-id="105813"><a href="/opinion/105813/united-states-ex-rel-jennings-v-ragen/" aria-description="Citation for case: United States Ex Rel. Jennings v. Ragen">Ragen, supra</a></span></i>).</p>
<p>[8]  See, <i>e. g., </i><i>United States ex rel. Tillery</i> v. <i>Cavell,</i> <span class="citation" data-id="254906"><a href="/opinion/254906/united-states-of-america-ex-rel-donald-tillery-v-angelo-c-cavell/" aria-description="Citation for case: United States of America Ex Rel. Donald Tillery v. Angelo...">294 F. 2d 12</a></span> (C. A. 3d Cir.); <i>Schlette</i> v. <i>People,</i> <span class="citation" data-id="252544"><a href="/opinion/252544/schlette-v-people-of-state-of-california/" aria-description="Citation for case: Schlette v. People of State of California">284 F. 2d 827</a></span> (C. A. 9th Cir.); <i>Bolling</i> v. <i>Smyth,</i> <span class="citation" data-id="251644"><a href="/opinion/251644/joe-bolling-v-w-frank-smyth-jr-superintendent-of-the-virginia-state/" aria-description="Citation for case: Joe Bolling v. W. Frank Smyth, Jr., Superintendent of the...">281 F. 2d 192</a></span> (C. A. 4th Cir.); <i>Chavez</i> v. <i>Dickson,</i> <span class="citation" data-id="6919807"><a href="/opinion/7018836/chavez-v-dickson/" aria-description="Citation for case: Chavez v. Dickson">280 F. 2d 727</a></span> (C. A. 9th Cir.); <i>Gay</i> v. <i>Graham,</i> <span class="citation" data-id="248755"><a href="/opinion/248755/frank-delano-gay-oliver-townsend-and-willie-olen-scott-v-marcell-graham/" aria-description="Citation for case: Frank Delano Gay, Oliver Townsend and Willie Olen Scott...">269 F. 2d 482</a></span> (C. A. 10th Cir.); <i>United States ex rel. Rogers</i> v. <i>Richmond,</i> <span class="citation" data-id="9446051"><a href="/opinion/244398/united-states-ex-rel-harold-d-rogers-relator-appellee-v-mark-s/" aria-description="Citation for case: United States Ex Rel. Harold D. Rogers, Relator-Appellee...">252 F. 2d 807</a></span> (C. A. 2d Cir.), cert. denied with accompanying statement, <span class="citation" data-id="105726"><a href="/opinion/105726/rogers-v-richmond/" aria-description="Citation for case: Rogers v. Richmond">357 U. S. 220</a></span>; <i>United States ex rel. Alvarez</i> v. <i>Murphy,</i> <span class="citation" data-id="242868"><a href="/opinion/242868/united-states-of-america-ex-rel-george-alvarez-v-robert-murphy-warden-of/" aria-description="Citation for case: United States of America Ex Rel. George Alvarez v. Robert...">246 F. 2d 871</a></span> (C. A. 2d Cir.); <i>Tyler</i> v. <i>Pepersack,</i> <span class="citation" data-id="239867"><a href="/opinion/239867/clarence-e-tyler-v-v-l-pepersack-warden-maryland-penitentiary/" aria-description="Citation for case: Clarence E. Tyler v. V. L. Pepersack, Warden, Maryland...">235 F. 2d 29</a></span> (C. A. 4th Cir.); <i>Cranor</i> v. <i>Gonzales,</i> <span class="citation" data-id="237553"><a href="/opinion/237553/john-r-cranor-superintendent-of-the-washington-state-penitentiary-at/" aria-description="Citation for case: John R. Cranor, Superintendent of the Washington State...">226 F. 2d 83</a></span> (C. A. 9th Cir.); <i>United States ex rel. De Vita</i> v. <i>McCorkle,</i> <span class="citation" data-id="235042"><a href="/opinion/235042/united-states-of-america-ex-rel-silvio-de-vita-v-lloyd-w-mccorkle/" aria-description="Citation for case: United States of America Ex Rel. Silvio De Vita v. Lloyd...">216 F. 2d 743</a></span> (C. A. 3d Cir.). See also Note, Habeas Corpus: Developments Since Brown v. Allen: A Survey and Analysis, <span class="citation no-link">53 Nw. U. L. Rev. 765</span>; Comment, Federal Habeas Corpus Review of State Convictions: An Interplay of Appellate Ambiguity and District Court Discretion, 68 Yale L. J. 98.</p>
<p>[9]  In announcing this test we do not mean to imply that the state courts are required to hold hearings and make findings which satisfy this standard, because such hearings are governed to a large extent by state law.
</p>
<p>The existence of the exhaustion of state remedies requirement (announced in <i>Ex parte Royall,</i> <span class="citation" data-id="91598"><a href="/opinion/91598/ex-parte-royall/" aria-description="Citation for case: Ex Parte Royall">117 U. S. 241</a></span>, and now codified in <span class="citation no-link">28 U. S. C. § 2254</span>) lends support to the view that a federal hearing is not always required. It presupposes that the State's adjudication of the constitutional issue can be of aid to the federal court sitting in habeas corpus.</p>
<p>[10]  Of course, under <i>Rogers</i> v. <i>Richmond,</i> a new trial is required if the trial judge or the jury, in finding the facts, has been guided by an erroneous standard of law. However, there will be situations in which statements of the trier of fact will do no more than create doubt as to whether the correct standard has been applied. In such situations a District Court hearing to determine the constitutional issue will be necessary.</p>
<p>[11]  The charge to the jury dealt only with the issues of credibility so far as the confession was concerned. Even accepting the relevance of the instructions, there is nothing in the charge to the jury to show that the trial judge, like the Supreme Court, did not think that voluntariness was conclusively established by a showing that the defendant was coherent.</p>
<p>[12]  The dissent fails to say why a hearing was not required for this reason. And "accepting the Court's . . . hearing standards" as the dissent does, it cannot seriously be argued that a hearing was not compelled. True the state trial judge instructed the jury that it <i>could</i> disregard the confession on grounds of credibility if it believed the petitioner's expert. But this hardly indicates whether the trial judge, at the motion to suppress, himself disbelieved the expert or whether he thought that, notwithstanding the truth of the expert's testimony, the confession was voluntary.</p>
<p>[13]  It appears that at the suppression hearing it was not disclosed that hyoscine (the substance injected, along with phenobarbital, into Townsend) was identical to scopolamine, and neither was it disclosed that scopolamine is familiarly known as "truth serum." Later on in the trial, there was testimony that hyoscine is identical to scopolamine, but not that scopolamine (or hyoscine) is a "truth serum."</p>
<p>[14]  Cf. <span class="citation no-link">28 U. S. C. §§ 2245</span>, 2247.</p>
<p>[*]  The petitioner's initial resistance to admitting guilt, his sudden change in attitude, and the veritable flood of confessions succeeding immediately upon administration of the drug to him, see <i>ante,</i> pp. 306-307, all indicate the real possibility that his will was so overborne. Moreover, the reliability of a number of these confessions is seriously impaired. See <i><span class="citation no-link">ibid.</span></i></p>
<p>[1]  Indeed, the original version of <span class="citation no-link">28 U. S. C. § 2243</span> directed the court to "proceed in a summary way to <i>determine the facts</i> of the case, <i>by hearing the testimony</i> and arguments, and thereupon to dispose of the party as law and justice require." See <i>Walker</i> v. <i>Johnston,</i> <span class="citation" data-id="103458"><a href="/opinion/103458/walker-v-johnston/#283" aria-description="Citation for case: Walker v. Johnston">312 U. S. 275, 283-284</a></span>. (Emphasis added.) The statute was later revised so that it now provides that "The court shall summarily hear and determine the facts, and dispose of the matter as law and justice require." The Revisers' notes indicate that the change was one of "phraseology" and not substance.
</p>
<p>Where the state court has reliably found facts relevant to any issue, the district judge in such a hearing should, of course, give appropriate deference to such findings. See <i>ante,</i> p. 318.</p>
<p>[2]  Among the instructions given were the following:
</p>
<p>"There has been admitted into evidence a written confession alleged to have been made freely and voluntarily by the defendant.</p>
<p>"You are further instructed that a confession made freely and voluntarily by a person charged with a crime may be considered by you, but if you find from the evidence that any force, physically or mentally, has been exerted upon the defendant by those having the defendant in charge after his arrest in order to obtain a confession, or that those persons made any promises to reward him if he would make such a confession, then you may totally disregard such confession.</p>
<p>"You are further instructed that if you find from the evidence that the defendant was given drugs and that said drugs caused him to lose his memory and create a state of amnesia in the defendant during the questioning of this defendant by the police or State's Attorney and that the defendant was not able to control his answers or to assert his will by denying the crime charged, then you may totally disregard such confession.</p>
<p>"You are instructed that if you find from the evidence that any influence was used on the defendant which amounted to duress upon his mind or body which caused him to make the confession, then you may totally disregard the confession.</p>
<p>.....</p>
<p>"You are further instructed that if you believe from the evidence in this case that duress or influence either physically or mentally, was exerted upon the defendant which caused him to make the written confession which has been introduced into evidence, then you may further consider whether this influence was still in existence at the time the defendant appeared at the coroner's inquest and is alleged to have made a confession there.</p>
<p>"There has been introduced into evidence the testimony of a witness, who is in the category known as an `Expert Witness,' who testified as to what influence or effect certain drugs had upon a hypothetical person.</p>
<p>"You are further instructed that you may take this testimony into consideration in determining whether the drugs alleged to have been administered to the defendant by Dr. Mansfield would have the same effect upon the defendant that the drug in the opinion of the `Expert Witness' had upon the hypothetical person, and if you believe from all the evidence in this case that the drugs had the effect upon the defendant to cause his consciousness to be impaired to the extent that he did not know what he was doing while he was being questioned by police officers or the Assistant State's Attorney, then you may totally disregard any statement or confession that he is alleged to have made during the time such influence, if any, was exerted upon him."</p>
<p>[3]  See footnote <span class="citation" data-id="9421969"><a href="/opinion/106040/local-lodge-no-1424-international-assn-of-machinists-v-national-labor/" aria-description="Citation for case: Local Lodge No. 1424, International Ass&#x27;n of MacHinists...">2, <i>supra.</i></a></span></p>
<p>[4]  See pp. 330-331, <i>supra.</i></p>

</div>
```

---

## GROUP: content/cases/Trupiano v. United States.md  (`case`, 5 assertions)

### content_page

```
---
title: Trupiano v. United States
type: case
citation: "334 U.S. 699 (1948)"
parallel_cite: "68 S. Ct. 1229; 92 L. Ed. 2d 1663; 92 L. Ed. 1663"
neutral_cite: 1948 U.S. LEXIS 1986
court: U.S.
court_level: scotus
circuit: ""
year: 1948
date_decided: 1948-06-14
docket: 427
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
  opinion_url: "https://www.courtlistener.com/opinion/104576/trupiano-v-united-states/"
  cluster_id: 104576
  opinion_id: null
  identity_checked: true
lake:
  record_id: Trupiano v. United States
  status: under_review
  projected_at: 2026-07-07
homes:
  - page: "[[SIA Persons]]"
    role: Historical / origin
related:
  - "[[Chimel v. California]]"
  - "[[SIA Persons]]"
tags:
  - case
  - fourth-amendment
  - search-incident-to-arrest
  - warrant-requirement
  - seizure
  - overruled
  - historical
holding: "Even incident to a lawful arrest, officers who had ample time and opportunity to obtain a search warrant must do so before seizing contraband — the 'whenever reasonably practicable' warrant rule, rejected two years later in United States v. Rabinowitz (1950) and superseded by the modern Chimel framework."
---

# Trupiano v. United States

*334 U.S. 699 (1948)* (No. 427) · Supreme Court of the United States · **Historical** · Treatment: **Overruled — rendered as history (⚪ unverified, pending S9)** — superseded by [[Chimel v. California]] (1969)
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪): the lake stub carries field_i=unverified, so the subsequent-history treatment below is authored orientation, not machine-certified. Identity cluster 104576 → 334 U.S. 699, decided 1948-06-14; Rule quote string-matched to the CL opinion text 2026-07-07. -->

## Background
Federal agents, aided by an informer working inside the operation, surveilled an illegal distillery on a New Jersey farm for weeks. They knew every detail of its construction and operation and had abundant time to obtain warrants. Instead, they entered without a warrant, arrested an operator caught running the still, and seized the distillery equipment and contraband. Trupiano and his codefendants moved to suppress the seized property.

## Issue
Whether contraband and equipment may be seized without a search warrant as incident to a lawful arrest, where the officers had ample opportunity to obtain a warrant beforehand.

## Rule
The Court (Murphy, J.) sustained the warrantless arrest but held the warrantless seizure of the still unlawful. It announced a strong warrant-preference rule for searches and seizures of property: "It is a cardinal rule that, in seizing goods and articles, law enforcement agents must secure and use search warrants wherever reasonably practicable." — 334 U.S. at 705. ^pin-705

A lawful arrest does not, by itself, dispense with that requirement when there is no reason the officers could not have obtained a warrant.

## Application
Because the agents had known the facts for weeks and had every chance to present them to a magistrate, nothing made a warrant impracticable; their failure to get one could not be excused by the fortuity that the seizure coincided with an arrest. The mere presence of a lawful arrest could not, by itself, legalize a warrantless search or seizure, lest the exception swallow the rule.

## Conclusion
The judgment was **reversed** as to the seizure of the contraband; Murphy, J., delivered the opinion of the Court.

## Treatment & subsequent history
**Overruled — the framework has twice been remade.** *Trupiano*'s "whenever reasonably practicable" warrant rule was rejected just two years later in *United States v. Rabinowitz*, 339 U.S. 56 (1950), which held that the test is whether a [[Search Incident to Arrest|search incident to arrest]] is *reasonable*, not whether it was practicable to get a warrant. The Court then reversed course again in *[[Chimel v. California]]* (1969), overruling *Rabinowitz* and confining a [[Search Incident to Arrest|search incident to arrest]] to the arrestee's person and the area within his immediate control — the rule that governs today.

*Status note (⚪):* authored from a CourtListener-verified identity stub; the subsequent-history above is well-settled but has not completed the project's two-key certification, so the page renders under the ⚪ banner until S9 promotion. *United States v. Rabinowitz* is not yet in the corpus and is named in plain text to avoid a dangling link. Preserved as **history**, never as live law.

## Appears on
- [[SIA Persons]] — *Historical / origin*

## Sources
- [*Trupiano v. United States*, 334 U.S. 699 (1948)](https://www.courtlistener.com/opinion/104576/trupiano-v-united-states/) — pinpoint: 705 (Opinion of the Court; Murphy, J.); Rule quote string-matched to the CL opinion text 2026-07-07. Superseded line: *United States v. Rabinowitz*, 339 U.S. 56 (1950); *Chimel v. California*, 395 U.S. 752 (1969) (successor page: [[Chimel v. California]]).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "1bee62b4b57891b6", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "334 U.S. 699 (1948)", "court": "U.S.", "neutral_cite": "1948 U.S. LEXIS 1986", "official_citation_present": true, "parallel_cite": "68 S. Ct. 1229; 92 L. Ed. 2d 1663; 92 L. Ed. 1663", "title": "Trupiano v. United States", "year": "1948"}}
{"assertion_id": "1cad20f45347802e", "dimension": "support", "kind": "home_role", "locator": {"home": "SIA Persons"}, "payload": {"home": "SIA Persons", "role": "Historical / origin", "title": "Trupiano v. United States"}}
{"assertion_id": "9d691c3f59b3d8a7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Even incident to a lawful arrest, officers who had ample time and opportunity to obtain a search warrant must do so before seizing contraband — the 'whenever reasonably practicable' warrant rule, rejected two years later in United States v. Rabinowitz (1950) and superseded by the modern Chimel framework.", "title": "Trupiano v. United States"}}
{"assertion_id": "59d7ca39b4909923", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "null", "as_of_treatment": "null", "composite_basis": "unverified", "composite_basis_ref": "null", "field_i_validity": "unverified", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "title": "Trupiano v. United States", "varies_by_point": "false"}}
{"assertion_id": "ed26ae95417b6ac6", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Trupiano v. United States"}}
```

### lake record — Trupiano v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Trupiano v. United States",
  "status": "under_review",
  "identity": {
    "case_name": "Trupiano v. United States",
    "case_name_short": "Trupiano",
    "case_name_full": "TRUPIANO Et Al. v. UNITED STATES",
    "input_case_name": "Trupiano v. United States",
    "court": "U.S.",
    "court_id": null,
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1948-06-14",
    "year": 1948,
    "docket": "427",
    "cluster_id": 104576,
    "lead_opinion_id": 9420205,
    "sibling_ids": [],
    "absolute_url": "/opinion/104576/trupiano-v-united-states/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "334 U.S. 699",
      "volume": "334",
      "reporter": "U.S.",
      "page": "699",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "68 S. Ct. 1229",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "1229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 1663",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 1663",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1948 U.S. LEXIS 1986",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "1986",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "334 U.S. 699",
        "volume": "334",
        "reporter": "U.S.",
        "page": "699",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "68 S. Ct. 1229",
        "volume": "68",
        "reporter": "S. Ct.",
        "page": "1229",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 2d 1663",
        "volume": "92",
        "reporter": "L. Ed. 2d",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1948 U.S. LEXIS 1986",
        "volume": "1948",
        "reporter": "U.S. LEXIS",
        "page": "1986",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "92 L. Ed. 1663",
        "volume": "92",
        "reporter": "L. Ed.",
        "page": "1663",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "334 U.S. 699",
    "official_selection": {
      "court_class": "scotus",
      "selected": "334 U.S. 699",
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
    "date_created": "2026-07-07T01:38:46Z",
    "date_modified": "2026-07-10T20:54:54Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-07T01:38:55Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "trupiano-v-united-states--104576",
      "to_record_id": "Trupiano v. United States",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Trupiano v. United States

```
<opinion type="majority">
<author id="b772-11">Mr. Justice Murphy</author>
<p id="ASv">delivered the opinion of the Court.</p>
<p id="b772-12">This case adds another chapter to the body of law growing out of the Fourth Amendment to the Constitution of the United States. That Amendment provides: “The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no warrants shall issue, but upon probable cause, supported by oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” In other words, the Fourth Amendment is a recognition of the fact that in this nation individual liberty depends in large part upon freedom from unreasonable intrusion by those in authority. It is the duty of this Court to give effect to that freedom.</p>
<p id="b773-4"><page-number citation-index="1" label="701">*701</page-number>In January, 1946, the petitioners sought to lease part of the Kell farm in Monmouth County, New Jersey, and to erect a building thereon. Kell suspected that they intended to build and operate an illegal still. He accordingly reported the matter to the appropriate federal authority, the Alcohol Tax Unit of the Bureau of Internal Revenue. The federal agents told Kell to accept the proposition, provided he did nothing to entice or encourage the petitioners into going ahead with their plans and provided he kept the agents informed of all developments. Nilsen, one of the agents, was assigned in February to work on the farm in the disguise of a “dumb farm hand” and to accept work at the still if petitioners should offer it.</p>
<p id="b773-5">Toward the end of March, 1946, Kell agreed with petitioners to let them rent part of his farm for $300 a month. Kell and Nilsen assisted petitioners in the erection of the building, a roughly constructed barn about 200 yards from the Kell farmhouse. Nilsen also assisted in the erection of the still and the vats.</p>
<p id="b773-6">Operation of the still began about May 13, 1946. Nil-sen thereafter worked as “mash man” at a salary of $100 a week, which he turned over to the Government. During this period he was in constant communication with his fellow agents. By prearrangement, he would meet one or more of the agents at various places within a few miles of the Kell <em>farm; </em>at these meetings “the conversation would be about the still building I had assisted in erecting or about the illicit distillery that I was working at on the Kell farm.” On May 20 he met with one of his superior officers and gave him samples of alcohol, several sugar bags, a yeast wrapper and an empty five-gallon can which had been taken from the still premises.</p>
<p id="b773-7">On May 26 Nilsen received a two-way portable radio set from his superiors. He used this set to transmit frequent bulletins on the activities of the petitioners. On <page-number citation-index="1" label="702">*702</page-number>the basis of radio intelligence supplied by Nilsen, a truckload of alcohol was seized on May 31 about an hour after it had left the farm.</p>
<p id="b774-6">At about 9 p. m. in the evening of June 3, 1946, Nilsen radioed his superior that the still operators were awaiting the arrival of a load of sugar and that alcohol was to be taken from the farm when the sugar truck arrived. Nil-sen apparently knew then that a raid was scheduled for that night, for he told Kell during the evening that “tonight is the night.” He radioed at 11 p. m. that the truck had been delayed but that petitioners Roett and Antoniole were at the still.</p>
<p id="b774-7">Three federal agents then drove to within three miles of the farm, at which point they were met by Kell. The remainder of the distance was traversed in Kell’s automobile. They arrived at the farm at about 11:45 p. m. The agents stated that the odor of fermenting mash and the sound of a gasoline motor were noticeable as the car was driven onto the farm premises; the odor became stronger and the noise louder as they alighted from the car and approached the building containing the still. Van De Car, one of the agents, went around one end of the building. Looking through an open door into a dimly lighted interior he could see a still column, a boiler and a gasoline pump in operation. He also saw Antoniole bending down near the pump. He entered the building and placed Antoniole under arrest. Thereupon he “seized the illicit distillery.”</p>
<p id="b774-8">After this arrest and seizure, Van De Car looked about further and observed a large number of five-gallon cans which he later found to contain alcohol and some vats which contained fermenting mash. Another agent, Casey, testified that he could see several of these cans through the open door before he entered; he subsequently counted the cans and found that there were 262 of them. After he entered he saw the remainder of the distillery <page-number citation-index="1" label="703">*703</page-number>equipment, including four large mash vats. The third agent, Gettel, proceeded to a small truck standing in the yard and “searched it thoroughly for papers and things of an evidentiary nature.” It does not appear whether he was successful in his search or whether he took anything from the truck.</p>
<p id="b775-5">A few minutes later Roett was arrested outside the building. Petitioners Trupiano and Riccardelli apparently were arrested later that night by other agents, the place and the circumstances not being revealed by the record before us. In addition, three other persons were arrested that night because of their connections with the illegal operations; one of them, who was unknown to Nilsen, was arrested when he arrived at the farm with a truck loaded with coke.</p>
<p id="b775-6">The agents engaged in this raid without securing a search warrant or warrants of arrest. It is undenied that they had more than adequate opportunity to obtain such warrants before the raid occurred, various federal judges and commissioners being readily available.</p>
<p id="b775-7">All of the persons arrested were charged with various violations of the Internal Revenue Code arising out of their ownership and operation of the distillery. Prior to the return of an indictment against them, the four petitioners filed in the District Court for the District of New Jersey a motion alleging that the federal agents had illegally seized “a still, alcohol, mash and other equipment,” and asking that “all such evidence” be excluded and suppressed at any trial and that “all of the aforesaid property” be returned. The District Court denied the motion after a hearing, holding that the seizure was reasonable and hence constitutional. <span class="citation" data-id="8898850"><a href="/opinion/8911109/united-states-v-trupiano/" aria-description="Citation for case: United States v. Trupiano">70 F. Supp. 764</a></span>. The Circuit Court of Appeals for the Third Circuit affirmed <em>per curiam </em>the order of the District Court. <span class="citation multiple-matches"><a href="/c/F.%202d/163/828/">163 F. 2d 828</a></span>.</p>
<p id="b775-8">Thus we have a case where contraband property was seized by federal agents without a search warrant under <page-number citation-index="1" label="704">*704</page-number>circumstances where such a warrant could easily have been obtained. The Government, however, claims that the failure to secure the warrant has no effect upon the validity of the seizure. Reference is made to the well established right of law enforcement officers to arrest without a warrant for a felony committed in their presence, <em>Carroll </em>v. <em>United States, </em><span class="citation" data-id="9418540"><a href="/opinion/100567/carroll-v-united-states/#156" aria-description="Citation for case: Carroll v. United States">267 U. S. 132, 156-167</a></span>, a right said to be unaffected by the fact that there may have been adequate time to procure a warrant of arrest. Since one of the petitioners, Antoniole, was arrested while engaged in operating an illegal still in the presence of agents of the Alcohol Tax Unit, his arrest was valid under this view even though it occurred without the benefit of a warrant. And since this arrest was valid, the argument is made that the seizure of the contraband open to view at the time of the arrest was also lawful. Reliance is here placed on the long line of cases recognizing that an arresting officer may look around at the time of the arrest and seize those fruits and evidences of crime or those contraband articles which are in plain sight and in his immediate and discernible presence. <em>Weeks </em>v. <em>United States, </em><span class="citation" data-id="98094"><a href="/opinion/98094/weeks-v-united-states/#392" aria-description="Citation for case: Weeks v. United States">232 U. S. 383, 392</a></span>; <em>Carroll </em>v. <em>United States, supra, </em>158; <em>Agnello </em>v. <em>United States, </em><span class="citation" data-id="100711"><a href="/opinion/100711/agnello-v-united-states/#30" aria-description="Citation for case: Agnello v. United States">269 U. S. 20, 30</a></span>; <em>United States </em>v. <em>Lee, </em><span class="citation" data-id="101118"><a href="/opinion/101118/united-states-v-lee/#563" aria-description="Citation for case: United States v. Lee">274 U. S. 559, 563</a></span>; <em>Marron </em>v. <em>United States, </em><span class="citation" data-id="101164"><a href="/opinion/101164/marron-v-united-states/#198" aria-description="Citation for case: Marron v. United States">275 U. S. 192, 198-199</a></span>; <em>Go-Bart Co. </em>v. <em>United States, </em><span class="citation" data-id="101643"><a href="/opinion/101643/go-bart-importing-co-v-united-states/#358" aria-description="Citation for case: Go-Bart Importing Co. v. United States">282 U. S. 344, 358</a></span>; <em>United States </em>v. <em>Lefkowits, </em><span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#465" aria-description="Citation for case: United States v. Lefkowitz">285 U. S. 452, 465</a></span>; <em>Harris </em>v. <em>United States, </em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/#150" aria-description="Citation for case: Harris v. United States">331 U. S. 145, 150-151</a></span>.</p>
<p id="b776-5">We sustain the Government’s contention that the arrest of Antoniole was valid. The federal agents had more than adequate cause, based upon the information supplied by Nilsen, to suspect that Antoniole was engaged in felonious activities on the farm premises. Acting on that suspicion, the agents went to the farm and entered onto the premises with the consent of Kell, the owner. There Antoniole was seen through an open doorway by one of the agents to be operating an illegal still, an act <page-number citation-index="1" label="705">*705</page-number>felonious in nature. His arrest was therefore valid on the theory that he was committing a felony in the discernible presence of an agent of the Alcohol Tax Unit, a peace officer of the United States. The absence of a warrant of arrest, even though there was sufficient time to obtain one, does not destroy the validity of an arrest under these circumstances. Warrants of arrest are designed to meet the dangers of unlimited and unreasonable arrests of persons who are not at the moment committing any crime. Those dangers, obviously, are not present where a felony plainly occurs before the eyes of an officer of the law at a place where he is lawfully present. Common sense then dictates that an arrest in that situation is valid despite the failure to obtain a warrant of arrest.</p>
<p id="b777-5">But we cannot agree that the seizure of the contraband property was made in conformity with the requirements of the Fourth Amendment. It is a cardinal rule that, in seizing goods and articles, law enforcement agents must secure and use search warrants wherever reasonably practicable. <em>Carroll </em>v. <em>United States, supra, </em>156; <em>Go-Bart Co. </em>v. <em>United States, supra, </em>358; <em>Taylor </em>v. <em>United States, </em><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/#6" aria-description="Citation for case: Taylor v. United States">286 U. S. 1, 6</a></span>; <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#14" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 14-15</a></span>. This rule rests upon the desirability of having magistrates rather than police officers determine when searches and seizures are permissible and what limitations should be placed upon such activities. <em>United States </em>v. <span class="citation" data-id="101899"><a href="/opinion/101899/united-states-v-lefkowitz/#464" aria-description="Citation for case: United States v. Lefkowitz"><em>Lefkowitz, supra, </em>464</a></span>. In their understandable zeal to ferret out crime and in the excitement of the capture of a suspected person, officers are less likely to possess the detachment and neutrality with which the constitutional rights of the suspect must be viewed. To provide the necessary security against unreasonable intrusions upon the private lives of individuals, the framers of the Fourth Amendment required adherence to judicial processes wherever possible. And subsequent history has confirmed the wisdom of that requirement.</p>
<p id="b778-5"><page-number citation-index="1" label="706">*706</page-number>The facts of this case do not measure up to the foregoing standard. The agents of the Alcohol Tax Unit knew every detail of the construction and operation of the illegal distillery long before the raid was made. One of them was assigned to work on the farm along with the illicit operators, making it possible for him to secure and report the minutest facts. In cooperation with the farm owner, who served as an informer, this agent was in a position to supply information which could easily have formed the basis for a detailed and effective search warrant. Concededly, there was an abundance of time during which such a warrant could have been secured, even on the night of the raid after the odor and noise of the distillery confirmed their expectations. And the property was not of a type that could have been dismantled and removed before the agents had time to secure a warrant; especially is this so since one of them was on hand at all times to report and guard against such a move. See <em>United States </em>v. <em>Kaplan, </em><span class="citation" data-id="1472811"><a href="/opinion/1472811/united-states-v-kaplan/#871" aria-description="Citation for case: United States v. Kaplan">89 F. 2d 869, 871</a></span>.</p>
<p id="b778-6">What was said in <em>Johnson </em>v. <em>United States, supra, </em>15, is equally applicable here: “No reason is offered for not obtaining a search warrant except the inconvenience to the officers and some slight delay necessary to prepare papers and present the evidence to a magistrate. These are never very convincing reasons and, in these circumstances, certainly are not enough to by-pass the consti-tutionál requirement. ... If the officers in this case were excused from the constitutional duty of presenting their evidence to a magistrate, it is difficult to think of a case in which it should be required.”</p>
<p id="b778-7">And so when the agents of the Alcohol Tax Unit decided to dispense with a search warrant <em>and to </em>take matters into their own hands, they did precisely what the Fourth Amendment was designed to outlaw. Uninhibited by any limitations that might have been contained in a warrant, they descended upon the distillery in a mid<page-number citation-index="1" label="707">*707</page-number>night raid. Nothing circumscribed their activities on that raid except their own good senses, which the authors of the Amendment deemed insufficient to justify a search or seizure except in exceptional circumstances not here present. The limitless possibilities afforded by the absence of a warrant were epitomized by the one agent who admitted searching “thoroughly” a small truck parked in the farmyard for items of an evidentiary character. The fact that they actually seized only contraband property, which would doubtless have been described in a warrant had one been issued, does not detract from the illegality of the seizure. See Amos v. <em>United States, </em><span class="citation" data-id="99746"><a href="/opinion/99746/amos-v-united-states/" aria-description="Citation for case: Amos v. United States">255 U. S. 313</a></span>; <em>Byars </em>v. <em>United States, </em><span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/" aria-description="Citation for case: Byars v. United States">273 U. S. 28</a></span>; <em>Taylor </em>v. <em>United States, supra.</em></p>
<p id="b779-5">Moreover, the proximity of the contraband property to the person of Antoniole at the moment of his arrest was a fortuitous circumstance which was inadequate to legalize the seizure. As we have seen, the existence of this property and the desirability of seizing it were known to the agents long before the seizure and formed one of the main purposes of the raid. Likewise, the arrest of An-toniole and the other petitioners in connection with the illicit operations was a foreseeable event motivating the raid. But the precise location of the petitioners at the time of their arrest had no relation to the foreseeability or necessity of the seizure. The practicability of obtaining a search warrant did not turn upon whether Antoniole and the others were within the distillery building when arrested or upon whether they were then engaged in operating the illicit equipment. Antoniole just happened to be working amid the contraband surroundings at 11:45 p. m. on the night in question, while the other three petitioners chanced to be some place else. But Antoniole might well have been outside the building at that particular time. If that had been the case and he had been arrested in the farmyard, the entire argument advanced <page-number citation-index="1" label="708">*708</page-number>by the Government in support of the seizure without warrant would collapse. We do not believe that the applicability of the Fourth Amendment to the facts of this case depends upon such a fortuitous factor as the precise location of Antoniole at the time of the raid.</p>
<p id="b780-5">In other words, the presence or absence of an arrestee at the exact time and place of a foreseeable and anticipated seizure does not determine the validity of that seizure if it occurs without a warrant. Rather the test is the apparent need for summary seizure, a test which clearly is not satisfied by the facts before us.</p>
<p id="b780-6">A search or seizure without a warrant as an incident to a lawful arrest has always been considered to be a strictly limited right. It grows out of the inherent necessities of the situation at the time of the arrest. But there must be something more in the way of necessity than merely a lawful arrest. The mere fact that there is a valid arrest does not <em>ipso facto </em>legalize a search or seizure without a warrant. <em>Carroll </em>v. <em>United States, supra, </em>158. Otherwise the exception swallows the general principle, making a search warrant completely unnecessary wherever there is a lawful arrest. And so there must be some other factor in the situation that would make it unreasonable or impracticable to require the arresting officer to equip himself with a search warrant. In the case before us, however, no reason whatever has been shown why the arresting officers could not have armed themselves during all the weeks of their surveillance of the locus with a duly obtained search warrant — no reason, that is, except indifference to the legal process for search and seizure which the Constitution contemplated.</p>
<p id="b780-7">We do not take occasion here to reexamine the situation involved in <em>Harris </em>v. <em>United States, supra. </em>The instant case relates only to the seizure of contraband the existence and precise nature and location of which the law enforcement officers were aware long before making the lawful arrest. That circumstance was wholly lacking in the <page-number citation-index="1" label="709">*709</page-number><em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>case, which was concerned with the permissible scope of a general search without a warrant as an incident to a lawful arrest. Moreover, the <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>case dealt with the seizure of Government property which could not have been the subject of a prior search warrant, it having been found unexpectedly during the course of a search. In contrast, the contraband seized in this case could easily have been specified in a prior search warrant. These factual differences may or may not be of significance so far as general principles are concerned. But the differences are enough to justify confining ourselves to the precise facts of this case, leaving it to another day to test the <em><span class="citation" data-id="9419996"><a href="/opinion/104422/harris-v-united-states/" aria-description="Citation for case: Harris v. United States">Harris</a></span> </em>situation by the rule that search warrants are to be obtained and used wherever reasonably practicable.</p>
<p id="b781-5">What we have here is a set of facts governed by a principle indistinguishable from that recognized and applied in <em>Taylor </em>v. <em>United States, supra. </em>The Court there held that the seizure of illicit whiskey was unreasonable, however well-grounded the suspicions of the federal agents, where there was an abundant opportunity to obtain a search warrant and to proceed in an orderly, judicial way. True, the <em><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span> </em>case did not involve a seizure in connection with an arrest. And the officers there made an unlawful entry onto the premises. But those factors had no relation to the practicability of obtaining a search warrant before making the seizure. It was the time element and the foreseeability of the need for a search and seizure that made the warrant essential. The <em><span class="citation" data-id="101905"><a href="/opinion/101905/taylor-v-united-states/" aria-description="Citation for case: Taylor v. United States">Taylor</a></span> </em>case accordingly makes plain the illegality of the seizure in the instant proceeding.</p>
<p id="b781-6">The Fourth Amendment was designed to protect both the innocent and the guilty from unreasonable intrusions upon their right of privacy while leaving adequate room for the necessary processes of law enforcement. The people of the United States insisted on writing the Fourth Amendment into the Constitution because sad experience had taught them that the right to search and <page-number citation-index="1" label="710">*710</page-number>seize should not be left to the mere discretion of the police, but should as a matter of principle be subjected to the requirement of previous judicial sanction wherever possible. The effective operation of government, however, could hardly be embarrassed by the requirement that arresting officers who have three weeks or more within which to secure the authorization of judicial authority for making search and seizure should secure such authority and not be left to their own discretion as to what is to be searched and what is to be seized. Such a requirement partakes of the very essence of the orderly and effective administration of the law.</p>
<p id="b782-4">It is a mistake to assume that a search warrant in these circumstances would contribute nothing to the preservation of the rights protected by the Fourth Amendment. A search warrant must describe with particularity the place to be searched and the things to be seized. Without such a warrant, however, officers are free to determine for themselves the extent of their search and the precise objects to be seized. This is no small difference. It is a difference upon which depends much of the potency of the right of privacy. And it is a difference that must be preserved even where contraband articles are seized in connection with a valid arrest.</p>
<p id="b782-5">It follows that it was error to refuse petitioners’ motion to exclude and suppress the property which was improperly seized. But since this property was contraband, they have no right to have it returned to them.</p>
<p id="b782-6">
<em>Reversed.</em>
</p>
</opinion>
```

---
