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

## GROUP: _overhaul2/lake/cases/Thompson v. Keohane.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "a1d1270eee1f5a37", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Thompson v. Keohane"}, "payload": {"all": [{"cite": "516 U.S. 99", "page": "99", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "516"}, {"cite": "116 S. Ct. 457", "page": "457", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "116"}, {"cite": "133 L. Ed. 2d 383", "page": "383", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "133"}, {"cite": "1995 U.S. LEXIS 8315", "page": "8315", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1995"}, {"cite": "95 Cal. Daily Op. Serv. 8968", "page": "8968", "reporter": "Cal. Daily Op. Serv.", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "95"}], "display": "516 U.S. 99", "official": {"cite": "516 U.S. 99", "page": "99", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "516"}, "official_selection_present": true, "record_id": "Thompson v. Keohane"}}
{"assertion_id": "1a743e99066a6150", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-112", "record_id": "Thompson v. Keohane"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-112", "pinpoint_status": "slip-only", "quote": "determination for Miranda purposes is a factual finding entitled to the §2254(d) presumption of correctness, or a mixed question of law and fact subject to independent federal review — and what the custody inquiry requires. ## Rule The custody inquiry is objective and two-part.", "quote_fidelity": "mismatch", "record_id": "Thompson v. Keohane", "star_marker": null}}
{"assertion_id": "e34e6a05e1b2a564", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-113", "record_id": "Thompson v. Keohane"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-113", "pinpoint_status": "slip-only", "quote": "This ultimate determination, we hold, presents a 'mixed question of law and fact' qualifying for independent review.", "quote_fidelity": "mismatch", "record_id": "Thompson v. Keohane", "star_marker": null}}
{"assertion_id": "b67302ad094a323d", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Thompson v. Keohane"}, "payload": {"as_of_content": "1995-11-29", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Thompson v. Keohane", "scope_note": "Good law; the Miranda custody inquiry is objective (would a reasonable person feel free to terminate the interrogation and leave) and is a mixed question of law and fact. The §2254(d) habeas-review framework was later changed by AEDPA (1996); see Yarborough v. Alvarado for custody under AEDPA deference.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Thompson v. Louisiana.json  (`lake-record`, 4 assertions)

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
{"assertion_id": "01b665dd65190947", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Thompson v. Louisiana"}, "payload": {"all": [{"cite": "469 U.S. 17", "page": "17", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "469"}, {"cite": "105 S. Ct. 409", "page": "409", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "105"}, {"cite": "83 L. Ed. 2d 246", "page": "246", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "83"}, {"cite": "1984 U.S. LEXIS 161", "page": "161", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1984"}], "display": "469 U.S. 17", "official": {"cite": "469 U.S. 17", "page": "17", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "469"}, "official_selection_present": true, "record_id": "Thompson v. Louisiana"}}
{"assertion_id": "00e61c43be6cc9c6", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-21a", "record_id": "Thompson v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-21a", "pinpoint_status": "slip-only", "quote": "A 2-hour general search remains a significant intrusion on petitioner's privacy and therefore may only be conducted subject to the constraints — including the warrant requirement — of the Fourth Amendment.", "quote_fidelity": "mismatch", "record_id": "Thompson v. Louisiana", "star_marker": null}}
{"assertion_id": "46079641799ca423", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-21", "record_id": "Thompson v. Louisiana"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-21", "pinpoint_status": "slip-only", "quote": "search. Homicide investigators then arrived and conducted a two-hour general, warrantless search of the home — the same day as the killing — seizing evidence used against her. The Louisiana courts upheld the search, distinguishing *Mincey* and finding a diminished expectation of privacy. ## Issue Whether a warrantless two-hour general search of a private home that is a recent homicide scene falls within an exception to the warrant requirement. ## Rule No — there is no murder-scene exception: in *Mincey*", "quote_fidelity": "mismatch", "record_id": "Thompson v. Louisiana", "star_marker": null}}
{"assertion_id": "c0bb64aff1c61a31", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Thompson v. Louisiana"}, "payload": {"as_of_content": "1985-01-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Thompson v. Louisiana", "scope_note": "Per curiam (announced January 21, 1985; reported at 469 U.S. 17, O.T. 1984). Reaffirms Mincey v. Arizona; no negative treatment.", "varies_by_point": false}}
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

## GROUP: _overhaul2/lake/cases/Thornton v. United States.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Thornton v. United States"
type: case
citation: "541 U.S. 615 (2004)"
parallel_cite: "124 S. Ct. 2127; 158 L. Ed. 2d 905"
neutral_cite: 2004 U.S. LEXIS 3681
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2004
date_decided: 2004-05-24
docket: 03-5165
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: caution
  as_of_content: 2004-05-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Thornton v. United States
  varies_by_point: true
  scope_note: "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest)."
  point_overrides:
    - point: legacy-limited-thornton-v-united-states
      point_label: Legacy limited treatment point
      field_i_validity: caution
      as_of_treatment: 2026-06-30
      s3_binding_status: provisional
      by:
        - name: Arizona v. Gant
          cluster_id: 145887
          cite: 556 U.S. 332
          field_ii: limited
      scope_note: "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest)."
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/134746/thornton-v-united-states/"
  cluster_id: 134746
  opinion_id: 9434613
  identity_checked: true
homes:
  - page: "[[SIA Vehicles]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Automobile Exception]]"
    role: "Related (cross-doctrine)"
related: ["[[New York v. Belton]]", "[[Arizona v. Gant]]", "[[Chimel v. California]]"]
aliases: []
tags: ["case", "fourth-amendment", "search-incident-to-arrest", "automobile", "vehicle-search", "recent-occupant"]
holding: "New York v. Belton's rule permitting a vehicle search incident to an occupant's arrest applies even when the officer first makes contact after the arrestee has exited the vehicle — i.e., to a 'recent occupant' (later cabined by Arizona v. Gant's two-justification test)."
lake:
  record_id: Thornton v. United States
  status: verified
  projected_at: 2026-07-09
---

# Thornton v. United States

*541 U.S. 615 (2004)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **limited** *(as of 2026-06-30)* — limited by [[Arizona v. Gant]]
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officer Nichols, in an unmarked car, noticed Marcus Thornton slow down to avoid driving next to him, and a license check showed the tags did not match the vehicle. Before Nichols could pull him over, Thornton parked and got out of his car. Nichols stopped him, obtained consent to a patdown, and found drugs in Thornton's pockets. Nichols arrested Thornton, handcuffed him, placed him in the patrol car, and then searched the passenger compartment of Thornton's vehicle, finding a handgun under the driver's seat. Thornton argued [[New York v. Belton]] did not apply because he was already outside the car when the officer first made contact.

## Issue
Whether *[[New York v. Belton|Belton]]*'s rule — allowing a search of a vehicle's passenger compartment incident to the lawful custodial arrest of an occupant — applies when the officer does not initiate contact until after the arrestee has stepped out of the vehicle (a "recent occupant").

## Rule
Yes. "[W]e . . . conclude that *Belton* governs even when an officer does not make contact until the person arrested has left the vehicle." — 541 U.S. at 617. ^pin-617

A "recent occupant" does not lose that status by having exited first: "[W]hile an arrestee's status as a 'recent occupant' may turn on his temporal or spatial relationship to the car at the time of the arrest and search, it certainly does not turn on whether he was inside or outside the car at the moment that the officer first initiated contact with him." — *Id.* at 622. ^pin-622

Thus: "So long as an arrestee is the sort of 'recent occupant' of a vehicle such as petitioner was here, officers may search that vehicle incident to the arrest." — *Id.* at 623–624. ^pin-623

## Application
Thornton had just driven and parked the car, stepping out only moments before Officer Nichols approached him, so he was a "recent occupant." The officer-safety and evidence-preservation concerns underlying *[[New York v. Belton|Belton]]* were no less present because Thornton exited before contact — the situation was equally volatile. A "contact initiation" rule turning on whether the suspect was in or out of the car when the officer first signaled would invite exactly the ad hoc, fact-specific inquiries *[[New York v. Belton|Belton]]* sought to avoid. The warrantless search of the passenger compartment incident to Thornton's arrest was therefore permissible, and the handgun was admissible.

## Conclusion
*[[New York v. Belton|Belton]]* applies to recent occupants; the vehicle search incident to Thornton's arrest was valid, and the judgment was affirmed.

## Treatment & subsequent history
- **Status:** limited *(as of 2026-06-30)* — **Binding — SCOTUS**.
- **Limited by [[Arizona v. Gant]] (2009):** *[[Arizona v. Gant|Gant]]* cabined the broad, automatic vehicle-search rule of *[[New York v. Belton|Belton]]* and *Thornton*. After *[[Arizona v. Gant|Gant]]*, a vehicle search incident to a recent occupant's arrest is permitted only when (1) the arrestee is unsecured and within reaching distance of the passenger compartment at the time of the search, or (2) it is reasonable to believe the vehicle contains evidence of the offense of arrest. On *Thornton*'s own facts the search would fail *[[Arizona v. Gant|Gant]]*'s first prong (Thornton was handcuffed in the patrol car) but could be analyzed under the second.

## Appears on
- [[SIA Vehicles]] — *Key — Progeny / Refinement*
- [[Automobile Exception]] — *Related (cross-doctrine)*

## Sources
- *Thornton v. United States*, 541 U.S. 615 (2004) — https://www.courtlistener.com/opinion/134746/thornton-v-united-states/ — pinpoints: 617, 622, 623–624.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "fb4016cf5296c0a9", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Thornton v. United States"}, "payload": {"all": [{"cite": "541 U.S. 615", "page": "615", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "541"}, {"cite": "124 S. Ct. 2127", "page": "2127", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "124"}, {"cite": "158 L. Ed. 2d 905", "page": "905", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "158"}, {"cite": "2004 U.S. LEXIS 3681", "page": "3681", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2004"}], "display": "541 U.S. 615", "official": {"cite": "541 U.S. 615", "page": "615", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "541"}, "official_selection_present": true, "record_id": "Thornton v. United States"}}
{"assertion_id": "083ba4d930bb82e9", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-622", "record_id": "Thornton v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-622", "pinpoint_status": "star-verified", "quote": "recent occupant", "quote_fidelity": "matched", "record_id": "Thornton v. United States", "star_marker": "620"}}
{"assertion_id": "c61a5c5253e3b215", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-623", "record_id": "Thornton v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-623", "pinpoint_status": "slip-only", "quote": "So long as an arrestee is the sort of 'recent occupant' of a vehicle such as petitioner was here, officers may search that vehicle incident to the arrest.", "quote_fidelity": "mismatch", "record_id": "Thornton v. United States", "star_marker": null}}
{"assertion_id": "d2bba71a82b64004", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-617", "record_id": "Thornton v. United States"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-617", "pinpoint_status": "slip-only", "quote": "). ## Rule Yes.", "quote_fidelity": "mismatch", "record_id": "Thornton v. United States", "star_marker": null}}
{"assertion_id": "d4b09487edf00ce0", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Thornton v. United States"}, "payload": {"as_of_content": "2004-05-24", "as_of_treatment": "2026-06-30", "field_i_validity": "caution", "record_id": "Thornton v. United States", "scope_note": "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest).", "varies_by_point": true}}
```

### lake record — Thornton v. United States

```json
{
  "schema_version": "s2.v1",
  "record_id": "Thornton v. United States",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Thornton v. United States",
    "case_name_short": "Thornton",
    "case_name_full": "Thornton v. United States",
    "input_case_name": "Thornton v. United States",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2004-05-24",
    "year": 2004,
    "docket": "03-5165",
    "cluster_id": 134746,
    "lead_opinion_id": 9434613,
    "sibling_ids": [
      134746,
      9434613,
      9434614,
      9434615,
      9434616
    ],
    "absolute_url": "/opinion/134746/thornton-v-united-states/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "541 U.S. 615",
      "volume": "541",
      "reporter": "U.S.",
      "page": "615",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "124 S. Ct. 2127",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 905",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "905",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2004 U.S. LEXIS 3681",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "3681",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "541 U.S. 615",
        "volume": "541",
        "reporter": "U.S.",
        "page": "615",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "124 S. Ct. 2127",
        "volume": "124",
        "reporter": "S. Ct.",
        "page": "2127",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "158 L. Ed. 2d 905",
        "volume": "158",
        "reporter": "L. Ed. 2d",
        "page": "905",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2004 U.S. LEXIS 3681",
        "volume": "2004",
        "reporter": "U.S. LEXIS",
        "page": "3681",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "541 U.S. 615",
    "official_selection": {
      "court_class": "scotus",
      "selected": "541 U.S. 615",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-617",
      "page": null,
      "quote": "). ## Rule Yes.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-622",
      "page": null,
      "quote": "recent occupant",
      "star_marker": "620",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 12831,
      "fragment": "#:~:text=%5Bwa%5Ds%20its-,recent%20occupant",
      "fragment_validated_at": "2026-07-09T23:46:10Z"
    },
    {
      "id": "pin-623",
      "page": null,
      "quote": "So long as an arrestee is the sort of 'recent occupant' of a vehicle such as petitioner was here, officers may search that vehicle incident to the arrest.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "caution",
    "as_of_content": "2004-05-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Thornton v. United States",
    "varies_by_point": true,
    "scope_note": "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest).",
    "point_overrides": [
      {
        "point": "legacy-limited-thornton-v-united-states",
        "point_label": "Legacy limited treatment point",
        "field_i_validity": "caution",
        "as_of_treatment": "2026-06-30",
        "s3_binding_status": "provisional",
        "by": [
          {
            "name": "Arizona v. Gant",
            "cluster_id": 145887,
            "cite": "556 U.S. 332",
            "field_ii": "limited"
          }
        ],
        "scope_note": "Extended Belton to 'recent occupants'; its automatic-search rule was cabined by Arizona v. Gant (2009), which replaced it with a two-justification test (arrestee unsecured and within reach, or reason to believe the vehicle contains evidence of the offense of arrest)."
      }
    ],
    "edges": [
      {
        "citing_case": {
          "name": "Arizona v. Gant",
          "cluster_id": 145887,
          "cite": "556 U.S. 332",
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
          "name": "State of Indiana v. Justin Crager",
          "cluster_id": 4547157,
          "cite": [
            "113 N.E.3d 657"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Chad Camou",
          "cluster_id": 2759861,
          "cite": [
            "773 F.3d 932",
            "2014 U.S. App. LEXIS 23347",
            "2014 WL 6980135"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Gary Lynn Patton v. State",
          "cluster_id": 3128917,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hill v. State",
          "cluster_id": 1619349,
          "cite": [
            "303 S.W.3d 863",
            "2009 WL 3821453"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Monterio Desha Hill v. State",
          "cluster_id": 2855208,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Grooms v. United States",
          "cluster_id": 2621071,
          "cite": [
            "129 S. Ct. 1981",
            "556 U.S. 1231",
            "77 U.S.L.W. 3632",
            "173 L. Ed. 2d 1288",
            "2009 U.S. LEXIS 3469"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Megginson v. United States",
          "cluster_id": 2621069,
          "cite": [
            "129 S. Ct. 1982",
            "556 U.S. 1230",
            "77 U.S.L.W. 3631",
            "173 L. Ed. 2d 1288",
            "2009 U.S. LEXIS 3471"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Vennus v. State",
          "cluster_id": 1496491,
          "cite": [
            "282 S.W.3d 70",
            "2009 Tex. Crim. App. LEXIS 977",
            "2009 WL 1066947"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Williams, 22924 (4-3-2009)",
          "cluster_id": 3956380,
          "cite": [
            "2009 Ohio 1627"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane1_negative"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davis v. United States",
          "cluster_id": 218926,
          "cite": [
            "180 L. Ed. 2d 285",
            "131 S. Ct. 2419",
            "564 U.S. 229",
            "2011 U.S. LEXIS 4560"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry v. Purnell",
          "cluster_id": 220962,
          "cite": [
            "652 F.3d 524",
            "2011 U.S. App. LEXIS 14391",
            "2011 WL 2725816"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Thomas Cameron Kincade",
          "cluster_id": 787362,
          "cite": [
            "379 F.3d 813",
            "2004 U.S. App. LEXIS 17191",
            "2004 WL 1837840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State Of Iowa Vs. Robert Joseph Vance",
          "cluster_id": 4472492,
          "cite": [
            "790 N.W.2d 775",
            "2010 Iowa Sup. LEXIS 116"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Texas v. Granville, Anthony",
          "cluster_id": 2950015,
          "cite": [
            "423 S.W.3d 399",
            "2014 WL 714730",
            "2014 Tex. Crim. App. LEXIS 237"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Robinson",
          "cluster_id": 2454018,
          "cite": [
            "253 P.3d 84",
            "171 Wash. 2d 292"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael A. Robinson",
          "cluster_id": 788500,
          "cite": [
            "390 F.3d 853",
            "65 Fed. R. Serv. 1188",
            "2004 U.S. App. LEXIS 24893",
            "2004 WL 2735246"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Valdez",
          "cluster_id": 2637812,
          "cite": [
            "224 P.3d 751"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Scottize Danyelle Brown",
          "cluster_id": 4635121,
          "cite": [
            "930 N.W.2d 840"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Kory Ray Smith",
          "cluster_id": 788425,
          "cite": [
            "389 F.3d 944",
            "2004 U.S. App. LEXIS 24343",
            "2004 WL 2660594"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State of Iowa v. Jesse Michael Gaskins",
          "cluster_id": 2812905,
          "cite": [
            "866 N.W.2d 1",
            "2015 Iowa Sup. LEXIS 80"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Peter Evans v. City of Zebulon, Georgia",
          "cluster_id": 76954,
          "cite": [
            "407 F.3d 1272",
            "2005 U.S. App. LEXIS 8071",
            "2005 WL 1076603"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Mora v. City of Gaithersburg, Md.",
          "cluster_id": 1025190,
          "cite": [
            "519 F.3d 216",
            "2008 U.S. App. LEXIS 4561",
            "2008 WL 565711"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Rowell",
          "cluster_id": 2570155,
          "cite": [
            "188 P.3d 95",
            "144 N.M. 371",
            "2008 NMSC 041"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
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
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Evans",
          "cluster_id": 5810664,
          "cite": [
            "200 Cal. App. 4th 735",
            "133 Cal. Rptr. 3d 323",
            "2011 Cal. App. LEXIS 1382"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Baker",
          "cluster_id": 2600016,
          "cite": [
            "2010 UT 18",
            "229 P.3d 650",
            "651 Utah Adv. Rep. 25",
            "2010 Utah LEXIS 17",
            "2010 WL 841271"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Diaz",
          "cluster_id": 2367386,
          "cite": [
            "51 Cal. 4th 84",
            "244 P.3d 501",
            "119 Cal. Rptr. 3d 105",
            "2011 Cal. LEXIS 1"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Thornton v. United States:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMjMwNTk1MjAwMDAwJnM9MjA0NDUxNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28134746+OR+9434613+OR+9434614+OR+9434615+OR+9434616%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz02MCZzPTEwNTc0NTEmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28134746+OR+9434613+OR+9434614+OR+9434615+OR+9434616%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616)",
        "reviewed": 21,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 21,
        "triage_read": 0,
        "triage_snippet_classified": 21
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(134746 OR 9434613 OR 9434614 OR 9434615 OR 9434616)",
    "indexed_citing_opinions": 409,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 134746,
        "count": 365,
        "count_source": "search"
      },
      {
        "opinion_id": 9434613,
        "count": 51,
        "count_source": "search"
      },
      {
        "opinion_id": 9434614,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434615,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9434616,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 660,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/thornton-v-united-states.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgyMzM1MDcmcz0xMDY0MjU2OCZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28134746+OR+9434613+OR+9434614+OR+9434615+OR+9434616%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 134746,
        "cited_id": 98094,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 100711,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 101164,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 104422,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 104769,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 106771,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 107730,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 107979,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 108153,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110168,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110558,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110559,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 110636,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 111020,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 112014,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 112719,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118228,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118250,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 118437,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 133277,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 195782,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 347138,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 360135,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 360237,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 371215,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 382105,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 382713,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 382715,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 509334,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 520415,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 607884,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 666017,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 716780,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 721372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 762479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 768295,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 777993,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 781516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 867520,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1102464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1263396,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1391930,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 1687668,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 134746,
        "cited_id": 2620702,
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
    "date_created": "2026-07-05T21:42:17Z",
    "date_modified": "2026-07-09T23:46:37Z",
    "warnings": [
      "legacy treatment migrated: limited -> caution",
      "F-S2-29 migration reference repair"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-05T21:42:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-05T21:42:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "F-S2-29 migration reference repair",
        "at": "2026-07-06T07:11:32Z",
        "verifier": "orchestrator claude-fable-5"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-05T21:42:27Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Thornton v. United States

```
<opinion type="majority">
<author id="b715-4"><page-number citation-index="1" label="617">*617</page-number>Chief Justice Rehnquist</author>
<p id="ANk">delivered the opinion of the Court except as to footnote 4.</p>
<p id="b715-5">In <em>New York </em>v. <em>Belton, </em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S. 454</a></span> (1981), we held that when a police officer has made a lawful custodial arrest of an occupant of an automobile, the Fourth Amendment allows the officer to search the passenger compartment of that vehicle as a contemporaneous incident of arrest. We have granted certiorari twice before to determine whether <em>Bel-ton’s </em>rule is limited to situations where the officer makes contact with the occupant while the occupant is inside the vehicle, or whether it applies as well when the officer first makes contact with the arrestee after the latter has stepped out of his vehicle. We did not reach the merits in either of those two cases. <em>Arizona </em>v. <em>Gant, </em><span class="citation" data-id="133277"><a href="/opinion/133277/arizona-v-gant/" aria-description="Citation for case: Arizona v. Gant">540 U. S. 963</a></span> (2003) (vacating and remanding for reconsideration in light of <em>State </em>v. <em>Dean, </em><span class="citation" data-id="867520"><a href="/opinion/867520/state-v-dean/" aria-description="Citation for case: State v. Dean">206 Ariz. 158</a></span>, <span class="citation" data-id="867520"><a href="/opinion/867520/state-v-dean/" aria-description="Citation for case: State v. Dean">76 P. 3d 429</a></span> (2003) (en bane)); <em>Florida </em>v. <em>Thomas, </em><span class="citation" data-id="118437"><a href="/opinion/118437/florida-v-thomas/" aria-description="Citation for case: Florida v. Thomas">532 U. S. 774</a></span> (2001) (dismissing for lack of jurisdiction). We now reach that question and conclude that <em>Bel-ton </em>governs even when an officer does not make contact until the person arrested has left the vehicle.</p>
<p id="b715-6">Officer Deion Nichols of the Norfolk, Virginia, Police Department, who was in uniform but driving an unmarked police car, first noticed petitioner Marcus Thornton when petitioner slowed down so as to avoid driving next to him. Nichols suspected that petitioner knew he was a police officer and for some reason did not want to pull next to him. His suspicions aroused, Nichols pulled off onto a side street <page-number citation-index="1" label="618">*618</page-number>and petitioner passed him. After petitioner passed him, Nichols ran a check on petitioner’s license tags, which revealed that the tags had been issued to a 1982 Chevy two-door and not to a Lincoln Town Car, the model of car petitioner was driving. Before Nichols had an opportunity to pull him over, petitioner drove into a parking lot, parked, and got out of the vehicle. Nichols saw petitioner leave his vehicle as he pulled in behind him. He parked the patrol car, accosted petitioner, and asked him for his driver’s license. He also told him that his license tags did not match the vehicle that he was driving.</p>
<p id="b716-4">Petitioner appeared nervous. He began rambling and licking his lips; he was sweating. Concerned for his safety, Nichols asked petitioner if he had any narcotics or weapons on him or in his vehicle. Petitioner said no. Nichols then asked petitioner if he could pat him down, to which petitioner agreed. Nichols felt a bulge in petitioner’s left front pocket and again asked him if he had any illegal narcotics on him. This time petitioner stated that he did, and he reached into his pocket and pulled out two individual bags, one containing three bags of marijuana and the other containing a large amount of crack cocaine. Nichols handcuffed petitioner, informed him that he was under arrest, and placed him in the back seat of the patrol car. He then searched petitioner’s vehicle and found a BryCo 9-millimeter handgun under the driver’s seat.</p>
<p id="b716-5">A grand jury charged petitioner with possession with intent to distribute cocaine base, <span class="citation no-link">84 Stat. 1260</span>, <span class="citation no-link">21 U. S. C. § 841</span>(a)(1), possession of a firearm after having been previously convicted of a crime punishable by a term of imprisonment exceeding one year, <span class="citation no-link">18 U. S. C. § 922</span>(g)(1), and possession of a firearm in furtherance of a drug trafficking crime, § 924(c)(1). Petitioner sought to suppress, <em>inter alia, </em>the firearm as the fruit of an unconstitutional search. After a hearing, the District Court denied petitioner’s motion to suppress, holding that the automobile search was valid under <page-number citation-index="1" label="619">*619</page-number><em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton, supra,</a></span> </em>and alternatively that Nichols could have conducted an inventory search of the automobile. A jury convicted petitioner on all three counts; he was sentenced to 180 months’ imprisonment and 8 years of supervised release.</p>
<p id="b717-4">Petitioner appealed, challenging only the District Court’s denial of the suppression motion. He argued that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was limited to situations where the officer initiated contact with an arrestee while he was still an occupant of the car. The United States Court of Appeals for the Fourth Circuit affirmed. <span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d 189</a></span> (2003). It held that “the historical rationales for the search incident to arrest doctrine — ‘the need to disarm the suspect in order to take him into custody’ and ‘the need to preserve evidence for later use at trial,’ ” <em><span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/" aria-description="Citation for case: United States v. Marcus Thornton">id.,</a></span> </em>at 195 (quoting <em>Knowles </em>v. <em>Iowa, </em><span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#116" aria-description="Citation for case: Knowles v. Iowa">525 U. S. 113, 116</a></span> (1998)), did not require <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to be limited solely to situations in which suspects were still in their vehicles when approached by the police. Noting that petitioner conceded that he was in “close proximity, both temporally and spatially,” to his vehicle, the court concluded that the car was within petitioner’s immediate control, and thus Nichols’ search was reasonable under <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>.</em><footnotemark><em>1</em></footnotemark><em> </em><span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/#196" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d, at 196</a></span>. We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./540/980/">540 U. S. 980</a></span> (2003), and now affirm.</p>
<p id="b717-5">In <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>, </em>an officer overtook a speeding vehicle on the New York Thruway and ordered its driver to pull over. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#455" aria-description="Citation for case: New York v. Belton">453 U. S., at 455</a></span>. Suspecting that the occupants possessed marijuana, the officer directed them to get out of the car and arrested them for unlawful possession. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#454" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 454-455</a></span>. He searched them and then searched the passenger compartment of the car. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#455" aria-description="Citation for case: New York v. Belton"><em>Id., </em>at 455</a></span>. We considered the constitutionally permissible scope of a search in these circumstances- and sought to lay down a workable rule governing that situation.</p>
<p id="b718-4"><page-number citation-index="1" label="620">*620</page-number>We first referred to <em>Chimel </em>v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969), a case where the arrestee was arrested in his home, and we had described the scope of a search incident to a lawful arrest as the person of the arrestee and the area immediately surrounding him. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S., at 457</a></span> (citing <span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/#763" aria-description="Citation for case: Chimel v. California"><em>Chimel, supra, </em>at 763</a></span>). This rule was justified by the need to remove any weapon the arrestee might seek to use to resist arrest or to escape, and the need to prevent the concealment or destruction of evidence. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#457" aria-description="Citation for case: New York v. Belton">453 U. S., at 457</a></span>. Although easily stated, the <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span> </em>principle had proved difficult to apply in specific cases. We pointed out that in <em>United States </em>v. <em>Robinson, </em><span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/" aria-description="Citation for case: United States v. Robinson">414 U. S. 218</a></span> (1973), a case dealing with the scope of the search of the arrestee’s person, we had rejected a suggestion that “ ‘there must be litigated in each case the issue of whether or not there was present one of the reasons supporting the authority’ ” to conduct such a search. <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">453 U. S., at 459</a></span> (quoting <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#235" aria-description="Citation for case: United States v. Robinson"><em>Robinson, supra, </em>at 235</a></span>). Similarly, because “courts ha[d] found no workable definition of ‘the area within the immediate control of the arrestee’ when that area arguably includefd] the interior of an automobile and the arrestee [wa]s its recent occupant,” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>, we sought to set forth a clear rule for police officers and citizens alike. We therefore held that “when a policeman has made a lawful custodial arrest of the occupant of an automobile, he may, as a contemporaneous incident of that arrest, search the passenger compartment of that automobile.” <em>Ibid, </em>(footnote omitted).</p>
<p id="b718-5">In so holding, we placed no reliance on the fact that the officer in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>ordered the occupants out of the vehicle, or initiated contact with them while they remained within it. Nor do we find such a factor persuasive in distinguishing the current situation, as it bears no logical relationship to <em>Bel-toris </em>rationale. There is simply no basis to conclude that the span of the area generally within the arrestee’s immediate control is determined by whether the arrestee exited the <page-number citation-index="1" label="621">*621</page-number>vehicle at the officer’s direction, or whether the officer initiated contact with him while he remained in the car. We recognized as much, albeit in dicta, in <em>Michigan </em>v. <em>Long, </em><span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/" aria-description="Citation for case: Michigan v. Long">463 U. S. 1032</a></span> (1983), where officers observed a speeding car swerve into a ditch. The driver exited and the officers met him at the rear of his car. Although there was no indication that the officers initiated contact with the driver while he was still in the vehicle, we observed that “[i]t is clear . . . that if the officers had arrested [respondent] . . . they could have searched the passenger compartment under <em>New York </em>v. <span class="citation" data-id="9842054"><a href="/opinion/111020/michigan-v-long/#1035" aria-description="Citation for case: Michigan v. Long"><em>Belton.” Id., </em>at 1035-1036</a></span>, and n. 1.</p>
<p id="b719-5">In all relevant aspects, the arrest of a suspect who is next to a vehicle presents identical concerns regarding officer safety and the destruction of evidence as the arrest of one who is inside the vehicle. An officer may search a suspect’s vehicle under <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>only if the suspect is arrested. See <span class="citation" data-id="118250"><a href="/opinion/118250/knowles-v-iowa/#117" aria-description="Citation for case: Knowles v. Iowa"><em>Knowles, supra, </em>at 117-118</a></span>. A custodial arrest is fluid and “[t]he danger to the police officer flows from <em>the fact of the arrest, </em>and its attendant proximity, stress, and uncertainty,” <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#234" aria-description="Citation for case: United States v. Robinson"><em>Robinson, supra, </em>at 234-235</a></span>, and n. 5 (emphasis added). See <em>Washington </em>v. <em>Chrisman, </em><span class="citation" data-id="9428641"><a href="/opinion/110636/washington-v-chrisman/#7" aria-description="Citation for case: Washington v. Chrisman">455 U. S. 1, 7</a></span> (1982) (“Every arrest must be presumed to present a risk of danger to the arresting officer”). The stress is no less merely because the arrestee exited his car before the officer initiated contact, nor is an arrestee less likely to attempt to lunge for a weapon or to destroy evidence if he is outside of, but still in control of, the vehicle. In either case, the officer faces a highly volatile situation. It would make little sense to apply two different rules to what is, at bottom, the same situation.</p>
<p id="b719-6">In some circumstances it may be safer and more effective for officers to conceal their presence from a suspect until he has left his vehicle. Certainly that is a judgment officers should be free to make. But under the strictures of petitioner’s proposed “contact initiation” rule, officers who do so would be unable to search the car’s passenger compartment <page-number citation-index="1" label="622">*622</page-number>in the event of a custodial arrest, potentially compromising their safety and placing incriminating evidence at risk of concealment or destruction. The Fourth Amendment does not require such a gamble.</p>
<p id="b720-5">Petitioner argues, however, that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>will fail to provide a “bright-line” rule if it applies to more than vehicle “occupants.” Brief for Petitioner 29-34. But <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>allows police to search the passenger compartment of a vehicle incident to a lawful custodial arrest of both “occupant[s]” and “recent occupant[s].” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>. Indeed, the respondent in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>was not inside the car at the time of the arrest and search; he was standing on the highway. In any event, while an arrestee’s status as a “recent occupant” may turn on his temporal or spatial relationship to the car at the time of the arrest and search,<footnotemark>2</footnotemark> it certainly does not turn on whether he was inside or outside the car at the moment that the officer first initiated contact with him.</p>
<p id="b720-6">To be sure, not all contraband in the passenger compartment is likely to be readily accessible to a “recent occupant.” It is unlikely in this case that petitioner could have reached under the driver’s seat for his gun once he was outside of his automobile. But the firearm and the passenger compartment in general were no more inaccessible than were the contraband and the passenger compartment in <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span>. </em>The <page-number citation-index="1" label="623">*623</page-number>need for a clear rule, readily understood by police officers and not depending on differing estimates of what items were or were not within reach of an arrestee at any particular moment, justifies the sort of generalization which <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>enunciated.<footnotemark>3</footnotemark> Once an officer determines that there is probable cause to make an arrest, it is reasonable to allow officers to ensure their safety and to preserve evidence by searching the entire passenger compartment.</p>
<p id="b721-5">Rather than clarifying the constitutional limits of a <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>search, petitioner’s “contact initiation” rule would obfuscate them. Under petitioner’s proposed rule, an officer approaching a suspect who has just alighted from his vehicle would have to determine whether he actually confronted or signaled confrontation with the suspect while he remained in the car, or whether the suspect exited his vehicle unaware of, and for reasons unrelated to, the officer’s presence. This determination would be inherently subjective and highly fact specific, and would require precisely the sort of ad hoc determinations on the part of officers in the field and reviewing courts that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>sought to avoid. <em>Id,., </em>at 459-460. Experience has shown that such a rule is impracticable, and we refuse to adopt it. So long as an arrestee is the sort of “re<page-number citation-index="1" label="624">*624</page-number>cent occupant” of a vehicle such as petitioner was here, officers may search that vehicle incident to the arrest.<footnotemark>4</footnotemark></p>
<p id="AUct">The judgment of the Court of Appeals is affirmed.</p>
<p id="b722-5">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b717-6"> The Court of Appeals did not reach the District Court’s alternative holding that Nichols could have conducted a lawful inventory search. <span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/#196" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d, at 196</a></span>.</p>
</footnote>
<footnote label="2">
<p id="b720-7"> Petitioner argues that if we reject his proposed “contact initiation” rule, we should limit the scope of <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>to “recent occupant[s]” who are within “reaching distance” of the car. Brief for Petitioner 35-36. We decline to address petitioner’s argument, however, as it is outside the question on which we granted certiorari, see this Court’s Rule 14.1(a), and was not addressed by the Court of Appeals, see <em>Peralta </em>v. <em>Heights Medical Center, Inc., </em><span class="citation" data-id="112014"><a href="/opinion/112014/peralta-v-heights-medical-center-inc/#86" aria-description="Citation for case: Peralta v. Heights Medical Center, Inc.">485 U. S. 80, 86</a></span> (1988). We note that it is unlikely that petitioner would even meet his own standard as he apparently conceded in the Court of Appeals that he was in “close proximity, both temporally and spatially,” to his vehicle when he was approached by Nichols. <span class="citation" data-id="781516"><a href="/opinion/781516/united-states-v-marcus-thornton/#196" aria-description="Citation for case: United States v. Marcus Thornton">325 F. 3d 189, 196</a></span> (CA4 2003).</p>
</footnote>
<footnote label="3">
<p id="b721-6"> Justice Stevens contends that <em>Belton’s </em>bright-line rule “is not needed for cases in which the arrestee is first accosted when he is a pedestrian, because <em>Chimel </em>[v. <em>California, </em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">395 U. S. 752</a></span> (1969),] itself provides all the guidance that is necessary.” <em>Post, </em>at 636 (dissenting opinion). Under Justice Stevens’ approach, however, even if the car itself was within the arrestee’s reaching distance under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>, </em>police officers and courts would still have to determine whether a particular object within the passenger compartment was also within an arrestee’s reaching distance under <em><span class="citation" data-id="9841975"><a href="/opinion/107979/chimel-v-california/" aria-description="Citation for case: Chimel v. California">Chimel</a></span>. </em>This is exactly the type of unworkable and fact-specific inquiry that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>rejected by holding that the entire passenger compartment may be searched when “ ‘the area within the immediate control of the arrestee’ . . . arguably includes the interior of an automobile and the arrestee is its recent occupant.” <span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/#460" aria-description="Citation for case: New York v. Belton">453 U. S., at 460</a></span>.</p>
</footnote>
<footnote label="4">
<p id="b722-8"> Whatever the merits of Justice Scalia's opinion concurring in the judgment, this is the wrong case in which to address them. Petitioner has never argued that <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>should be limited “to cases where it is reasonable to believe evidence relevant to the crime of arrest might be found in the vehicle,” <em>post, </em>at 632, nor did any court below consider Justice Scalia’s reasoning. See <em>Pennsylvania Dept. of Corrections </em>v. <em>Yeskey, </em><span class="citation" data-id="118228"><a href="/opinion/118228/pennsylvania-department-of-corrections-v-yeskey/#212" aria-description="Citation for case: Pennsylvania Department of Corrections v. Yeskey">524 U. S. 206, 212-213</a></span> (1998) (“ ‘Where issues are neither raised before nor considered by the Court of Appeals, this Court will not ordinarily consider them’ ” (quoting <em>Adickes </em>v. <em>S. H. Kress &amp; Co., </em><span class="citation" data-id="9424277"><a href="/opinion/108153/adickes-v-s-h-kress-co/#147" aria-description="Citation for case: Adickes v. S. H. Kress &amp; Co.">398 U. S. 144, 147, n. 2</a></span> (1970))). The question presented — “[w]hether the bright-line rule announced in <em>New York </em>v. <em><span class="citation" data-id="9428488"><a href="/opinion/110559/new-york-v-belton/" aria-description="Citation for case: New York v. Belton">Belton</a></span> </em>is confined to situations in which the police initiate contact with the occupant of a vehicle while that person is in the vehicle,” Pet. for Cert. — does not fairly encompass Justice Scalia’s analysis. See this Court’s Rule 14.1(a) (“Only the questions set out in the petition, or fairly included therein, will be considered by the Court”). And the United States has never had an opportunity to respond to such an approach. See <em>Yee </em>v. <em>Escondido, </em><span class="citation" data-id="9432511"><a href="/opinion/112719/yee-v-city-of-escondido/#536" aria-description="Citation for case: Yee v. City of Escondido">503 U. S. 519, 536</a></span> (1992). Under these circumstances, it would be imprudent to overrule, for all intents and purposes, our established constitutional precedent, which governs police authority in a common occurrence such as automobile searches pursuant to arrest, and we decline to do so at this time.</p>
</footnote>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Timbs v. Indiana.json  (`lake-record`, 2 assertions)

### content_page

```
---
title: Timbs v. Indiana
type: case
citation: "586 U.S. 146 (2019)"
parallel_cite: "139 S. Ct. 682; 203 L. Ed. 2d 11"
neutral_cite: 2019 U.S. LEXIS 1350
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2019
date_decided: 2019-02-20
docket: No. 17-1091
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
  opinion_url: "https://www.courtlistener.com/opinion/4591916/timbs-v-indiana/"
  cluster_id: 4591916
  opinion_id: 9888039
  identity_checked: true
lake:
  record_id: Timbs v. Indiana
  status: under_review
  projected_at: 2026-07-09
homes:
  - page: "[[Civil Asset Forfeiture]]"
    role: Anchor
related:
  - "[[Civil Asset Forfeiture]]"
  - "[[Austin v. United States]]"
  - "[[United States v. Bajakajian]]"
tags:
  - case
  - eighth-amendment
  - excessive-fines
  - civil-forfeiture
  - incorporation
  - fourteenth-amendment
  - in-rem
holding: "The Eighth Amendment's Excessive Fines Clause is an incorporated protection applicable to the States under the Fourteenth Amendment's Due Process Clause; the safeguard against excessive fines is fundamental to our scheme of ordered liberty and deeply rooted in this Nation's history and tradition, and it reaches civil in rem forfeitures that are at least partly punitive."
aliases:
  - Timbs v. Indiana
  - "Timbs v. Indiana (2019)"
---

# Timbs v. Indiana

*586 U.S. 146 (2019)* (No. 17-1091) · Supreme Court of the United States · **Binding — SCOTUS** · Treatment: **Unverified**
<!-- header line; TreatmentBadge + weight render from frontmatter, degrading to the text above. Born under_review (⚪) — identity cluster 4591916 → majority opinion 9888039 (Ginsburg, J., for a unanimous Court; 586 U.S. 146 / 139 S. Ct. 682, argued Nov. 28, 2018, decided Feb. 20, 2019). Rule quote string-matched to the CL opinion text 2026-07-07; the CL text is paginated to the West S. Ct. reporter (parallel cite), so the pin is `139 S. Ct. at 687` (page-label `*687`) — the official U.S. Reports pagination is not present in the CL text. S9 promotes. -->

## Background
Tyson Timbs pleaded guilty in Indiana state court to dealing in a controlled substance and conspiracy to commit theft. He was sentenced to home detention and probation and ordered to pay roughly $1,203 in fees and costs; the maximum monetary fine for his drug offense was $10,000. When he was arrested, police seized his Land Rover SUV, which he had bought for about $42,000 using money from a life-insurance policy paid on his father's death. The State engaged a private law firm to bring a civil *in rem* forfeiture action against the vehicle. The trial court denied forfeiture as grossly disproportionate to the gravity of the offense — the vehicle was worth more than four times the maximum fine — and the Court of Appeals of Indiana affirmed, but the Indiana Supreme Court reversed, holding that the Excessive Fines Clause constrains only the Federal Government and does not apply to the States.

## Issue
Whether the Eighth Amendment's Excessive Fines Clause is an "incorporated" protection applicable to the States under the Fourteenth Amendment's Due Process Clause.

## Rule
The Court applied its settled incorporation framework: a Bill of Rights guarantee binds the States if it is "fundamental to our scheme of ordered liberty" or "deeply rooted in this Nation's history and tradition." The protection against excessive fines is both — it has a lineage from Magna Carta through the English Bill of Rights to the founding, and it guards against the government's temptation to use fines to raise revenue, chill opponents, and pursue vindictive ends. On that basis the Court held: "The Excessive Fines Clause is therefore incorporated by the Due Process Clause of the Fourteenth Amendment." — 139 S. Ct. at 687. ^pin-687

## Application
Indiana's argument that the Clause does not reach civil *in rem* forfeitures did not change the incorporation analysis. Whether or not the *application* of the Clause to a particular class of forfeitures is itself deeply rooted, the *right* the Clause secures is incorporated; the scope question is distinct from the threshold question of whether the guarantee binds the States at all. Because the Excessive Fines Clause applies to Indiana, the Indiana Supreme Court's contrary premise could not stand, and the excessiveness of this forfeiture remained to be resolved below.

## Conclusion
The judgment of the Indiana Supreme Court was **[[Reading and Citing Cases#vacated|vacated]]** and the case [[Reading and Citing Cases#on-remand|remanded]]. Ginsburg, J., delivered the opinion of a unanimous Court. Gorsuch, J., concurred; Thomas, J., concurred in the judgment (arguing the right is better secured through the Fourteenth Amendment's Privileges or Immunities Clause).

## Treatment & subsequent history
**Status: Unverified — subsequent treatment not yet machine-verified.** This page was authored from a CourtListener-verified identity stub; its citator and progeny history have not completed the project's two-key verification, so it renders under the ⚪ banner until S9 promotion. *Timbs* completes the Excessive Fines line for state and local forfeitures: *[[Austin v. United States]]* (1993) held that punitive civil forfeitures are subject to the Clause, *[[United States v. Bajakajian]]* (1998) supplied the "grossly disproportional" excessiveness standard, and *Timbs* makes the Clause enforceable against the States. Teach it as the doctrine's reach — the guarantee that a state or municipal forfeiture, not just a federal one, can be challenged as an excessive fine.

## Appears on
- [[Civil Asset Forfeiture]] — *Anchor*

## Sources
- [*Timbs v. Indiana*, 586 U.S. 146 (2019)](https://www.courtlistener.com/opinion/4591916/timbs-v-indiana/) — pinpoint: 139 S. Ct. at 687 (Ginsburg, J., for a unanimous Court; the CL opinion text is paginated to the West S. Ct. reporter and carries the page-label `*687` in the paragraph stating the incorporation holding). Rule quote string-matched to the CL opinion text 2026-07-07.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "643c8c2afdb6e69e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Timbs v. Indiana"}, "payload": {"all": [{"cite": "586 U.S. 146", "page": "146", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "586"}, {"cite": "139 S. Ct. 682", "page": "682", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "139"}, {"cite": "2019 U.S. LEXIS 1350", "page": "1350", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "2019"}, {"cite": "203 L. Ed. 2d 11", "page": "11", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "203"}], "display": "586 U.S. 146", "official": {"cite": "586 U.S. 146", "page": "146", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "586"}, "official_selection_present": true, "record_id": "Timbs v. Indiana"}}
{"assertion_id": "e4feb4d9766bc577", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Timbs v. Indiana"}, "payload": {"as_of_content": null, "as_of_treatment": null, "field_i_validity": "unverified", "record_id": "Timbs v. Indiana", "scope_note": "Frontier stub: treatment/progeny intentionally not derived until S6 promotion.", "varies_by_point": false}}
```

### lake record — Timbs v. Indiana

```json
{
  "schema_version": "s2.v1",
  "record_id": "Timbs v. Indiana",
  "status": "under_review",
  "identity": {
    "case_name": "Timbs v. Indiana",
    "case_name_short": "Timbs",
    "case_name_full": "Tyson TIMBS, Petitioner v. INDIANA",
    "input_case_name": "Timbs v. Indiana",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2019-02-20",
    "year": 2019,
    "docket": "No. 17-1091",
    "cluster_id": 4591916,
    "lead_opinion_id": 9888039,
    "sibling_ids": [],
    "absolute_url": "/opinion/4591916/timbs-v-indiana/",
    "identity_method": "frontier-identity",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "586 U.S. 146",
      "volume": "586",
      "reporter": "U.S.",
      "page": "146",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "139 S. Ct. 682",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "203 L. Ed. 2d 11",
        "volume": "203",
        "reporter": "L. Ed. 2d",
        "page": "11",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2019 U.S. LEXIS 1350",
        "volume": "2019",
        "reporter": "U.S. LEXIS",
        "page": "1350",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "586 U.S. 146",
        "volume": "586",
        "reporter": "U.S.",
        "page": "146",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "139 S. Ct. 682",
        "volume": "139",
        "reporter": "S. Ct.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2019 U.S. LEXIS 1350",
        "volume": "2019",
        "reporter": "U.S. LEXIS",
        "page": "1350",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "203 L. Ed. 2d 11",
        "volume": "203",
        "reporter": "L. Ed. 2d",
        "page": "11",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "586 U.S. 146",
    "official_selection": {
      "court_class": "scotus",
      "selected": "586 U.S. 146",
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
    "date_created": "2026-07-06T13:41:50Z",
    "date_modified": "2026-07-09T23:29:56Z",
    "warnings": [],
    "field_provenance": {
      "identity": {
        "src": "CourtListener frontier identity search",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "frontier stub, no treatment",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "frontier stub, no pinpoints",
        "at": "2026-07-06T13:41:52Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    },
    "s6_promotion": {
      "from_record_id": "timbs-v-indiana--4591916",
      "to_record_id": "Timbs v. Indiana",
      "as_of": "2026-07-07",
      "born_status": "under_review"
    }
  }
}

```

### cached opinion text — Timbs v. Indiana

```
<opinion type="majority">
<author id="p-9">Justice GINSBURG delivered the opinion of the Court.</author>
<p id="p-10"><a class="page-label" data-citation-index="1" data-label="686" href="#p686" id="p686">*686</a>Tyson Timbs pleaded guilty in Indiana state court to dealing in a controlled substance and conspiracy to commit theft. The trial court sentenced him to one year of home detention and five years of probation, which included a court-supervised addiction-treatment program. The sentence also required Timbs to pay fees and costs totaling $ 1,203. At the time of Timbs's arrest, the police seized his vehicle, a Land Rover SUV Timbs had purchased for about $ 42,000. Timbs paid for the vehicle with money he received from an insurance policy when his father died.</p>
<p id="p-11">The State engaged a private law firm to bring a civil suit for forfeiture of Timbs's Land Rover, charging that the vehicle had been used to transport heroin. After Timbs's guilty plea in the criminal case, the trial court held a hearing on the forfeiture demand. Although finding that Timbs's vehicle had been used to facilitate violation of a criminal statute, the court denied the requested forfeiture, observing that Timbs had recently purchased the vehicle for $ 42,000, more than four times the maximum $ 10,000 monetary fine assessable against him for his drug conviction. Forfeiture of the Land Rover, the court determined, would be grossly disproportionate to the gravity of Timbs's offense, hence unconstitutional under the Eighth Amendment's Excessive Fines Clause. The Court of Appeals of Indiana affirmed that determination, but the Indiana Supreme Court reversed. <extracted-citation case-ids="12331536" index="0" url="https://cite.case.law/ne3d/84/1179/"><span class="citation" data-id="4217247"><a href="/opinion/4439994/state-of-indiana-v-tyson-timbs/" aria-description="Citation for case: State of Indiana v. Tyson Timbs">84 N.E.3d 1179</a></span></extracted-citation> (2017). The Indiana Supreme Court did not decide whether the forfeiture would be excessive. Instead, it held that the Excessive Fines Clause constrains only federal action and is inapplicable to state impositions. We granted certiorari. 585 U.S. ----, <extracted-citation case-ids="12613687,12613688,12613689,12613690,12613691,12613692" index="1" url="https://cite.case.law/s-ct/138/2650/"><span class="citation multiple-matches"><a href="/c/S.Ct./138/2650/">138 S.Ct. 2650</a></span></extracted-citation>, <extracted-citation index="2" url="https://cite.case.law/citations/?q=201%20L.%20Ed.%202d%201049"><span class="citation no-link">201 L.Ed.2d 1049</span></extracted-citation> (2018).</p>
<p id="p-12">The question presented: Is the Eighth Amendment's Excessive Fines Clause an "incorporated" protection applicable to the States under the Fourteenth Amendment's Due Process Clause? Like the Eighth Amendment's proscriptions of "cruel and unusual punishment" and "[e]xcessive bail," the protection against excessive fines guards against abuses of government's punitive or criminal-law-enforcement authority. This safeguard, we hold, is "fundamental to our scheme of ordered liberty," with "dee[p] root[s] in <a class="page-label" data-citation-index="1" data-label="687" href="#p687" id="p687">*687</a>[our] history and tradition." <em>McDonald</em> v. <em>Chicago</em> , <extracted-citation case-ids="12455289,3644508" index="3" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S. 742</a></span></extracted-citation>, 767, <extracted-citation case-ids="12455289,3644508" index="4" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="5" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">177 L.Ed.2d 894</a></span></extracted-citation> (2010) (internal quotation marks omitted; emphasis deleted). The Excessive Fines Clause is therefore incorporated by the Due Process Clause of the Fourteenth Amendment.</p>
<p id="p-13">I</p>
<p id="p-14">A</p>
<p id="p-15">When ratified in 1791, the Bill of Rights applied only to the Federal Government. <em>Barron ex rel. Tiernan</em> v<em>. Mayor of Baltimore</em> , <extracted-citation case-ids="1436167" index="6" url="https://cite.case.law/us/32/243/"><span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">7 Pet. 243</a></span></extracted-citation>, <extracted-citation case-ids="1436167" index="7" url="https://cite.case.law/us/32/243/"><span class="citation" data-id="85827"><a href="/opinion/85827/barron-ex-rel-tiernan-v-mayor-of-baltimore/" aria-description="Citation for case: Barron Ex Rel. Tiernan v. Mayor of Baltimore">8 L.Ed. 672</a></span></extracted-citation> (1833). "The constitutional Amendments adopted in the aftermath of the Civil War," however, "fundamentally altered our country's federal system." <em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="8" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 754</a></span></extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="9" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>. With only "a handful" of exceptions, this Court has held that the Fourteenth Amendment's Due Process Clause incorporates the protections contained in the Bill of Rights, rendering them applicable to the States. <em><extracted-citation case-ids="12455289,3644508" index="10" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">Id.</a></span></extracted-citation></em> , at 764-765, and nn. 12-13, <extracted-citation case-ids="12455289,3644508" index="11" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>. A Bill of Rights protection is incorporated, we have explained, if it is "fundamental to our scheme of ordered liberty," or "deeply rooted in this Nation's history and tradition." <em><extracted-citation case-ids="12455289,3644508" index="12" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12455289,3644508" index="12" url="https://cite.case.law/us/561/742/"> at 767</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="13" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation> (internal quotation marks omitted; emphasis deleted).</p>
<p id="p-16">Incorporated Bill of Rights guarantees are "enforced against the States under the Fourteenth Amendment according to the same standards that protect those personal rights against federal encroachment." <em><extracted-citation case-ids="12455289,3644508" index="14" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">Id.,</a></span></extracted-citation></em><extracted-citation case-ids="12455289,3644508" index="14" url="https://cite.case.law/us/561/742/"> at 765</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="15" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation> (internal quotation marks omitted). Thus, if a Bill of Rights protection is incorporated, there is no daylight between the federal and state conduct it prohibits or requires.<footnotemark>1</footnotemark></p>
<p id="p-17">B</p>
<p id="p-18">Under the Eighth Amendment, "[e]xcessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted." Taken together, these Clauses place "parallel limitations" on "the power of those entrusted with the criminal-law function of government." <em>Browning-Ferris Industries of Vt., Inc.</em> v. <em>Kelco Disposal, Inc.</em> , <extracted-citation case-ids="6214309" index="16" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S. 257</a></span></extracted-citation>, 263, <extracted-citation case-ids="6214309" index="17" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="18" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">106 L.Ed.2d 219</a></span></extracted-citation> (1989) (quoting <em>Ingraham</em> v. <em>Wright</em> , <extracted-citation case-ids="12126861" index="19" url="https://cite.case.law/us/430/651/#p664"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">430 U.S. 651</a></span></extracted-citation>, 664, <extracted-citation case-ids="12126861" index="20" url="https://cite.case.law/us/430/651/#p664"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">97 S.Ct. 1401</a></span></extracted-citation>, <extracted-citation case-ids="12126861" index="21" url="https://cite.case.law/us/430/651/#p664"><span class="citation" data-id="9426747"><a href="/opinion/109635/ingraham-v-wright/" aria-description="Citation for case: Ingraham v. Wright">51 L.Ed.2d 711</a></span></extracted-citation> (1977) ). Directly at issue here is the phrase "nor excessive fines imposed," which "limits the government's power to extract payments, whether in cash or in kind, 'as punishment for some offense.' " <em>United States</em> v<em>. Bajakajian</em> , <extracted-citation case-ids="11182447" index="22" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">524 U.S. 321</a></span></extracted-citation>, 327-328, <extracted-citation case-ids="11182447" index="23" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">118 S.Ct. 2028</a></span></extracted-citation>, <extracted-citation case-ids="11182447" index="24" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">141 L.Ed.2d 314</a></span></extracted-citation> (1998) (quoting <em>Austin</em> v. <em>United States</em> , <extracted-citation case-ids="355668" index="25" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">509 U.S. 602</a></span></extracted-citation>, 609-610, <extracted-citation case-ids="355668" index="26" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">113 S.Ct. 2801</a></span></extracted-citation>, <extracted-citation case-ids="355668" index="27" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">125 L.Ed.2d 488</a></span></extracted-citation> (1993) ). The Fourteenth Amendment, we hold, incorporates this protection.</p>
<p id="p-19">The Excessive Fines Clause traces its venerable lineage back to at least 1215, when Magna Carta guaranteed that "[a] Free-man shall not be amerced for a small fault, but after the manner of the fault; and for a great fault after the greatness thereof, saving to him his contenement ...." § 20, 9 Hen. III, ch. 14, in 1 Eng.</p>
<p id="p-20"><a class="page-label" data-citation-index="1" data-label="688" href="#p688" id="p688">*688</a>Stat. at Large 5 (1225).<footnotemark>2</footnotemark> As relevant here, Magna Carta required that economic sanctions "be proportioned to the wrong" and "not be so large as to deprive [an offender] of his livelihood." <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="28" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 271</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="29" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. See also 4 W. Blackstone, Commentaries on the Laws of England 372 (1769) ("[N]o man shall have a larger amercement imposed upon him, than his circumstances or personal estate will bear ...."). But cf. <em>Bajakajian</em> , <extracted-citation case-ids="11182447" index="30" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/#340" aria-description="Citation for case: United States v. Bajakajian">524 U.S., at 340</a></span>, n. 15</extracted-citation>, <extracted-citation case-ids="11182447" index="31" url="https://cite.case.law/us/524/321/#p327"><span class="citation" data-id="9433683"><a href="/opinion/118234/united-states-v-bajakajian/" aria-description="Citation for case: United States v. Bajakajian">118 S.Ct. 2028</a></span></extracted-citation> (taking no position on the question whether a person's income and wealth are relevant considerations in judging the excessiveness of a fine).</p>
<p id="p-21">Despite Magna Carta, imposition of excessive fines persisted. The 17th century Stuart kings, in particular, were criticized for using large fines to raise revenue, harass their political foes, and indefinitely detain those unable to pay. <em>E.g.</em> , The Grand Remonstrance ¶¶17, 34 (1641), in The Constitutional Documents of the Puritan Revolution 1625-1660, pp. 210, 212 (S. Gardiner ed., 3d ed. rev. 1906); <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="32" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 267</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="33" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. When James II was overthrown in the Glorious Revolution, the attendant English Bill of Rights reaffirmed Magna Carta's guarantee by providing that "excessive Bail ought not to be required, nor excessive Fines imposed; nor cruel and unusual Punishments inflicted." 1 Wm. &amp; Mary, ch. 2, § 10, in 3 Eng. Stat. at Large 441 (1689).</p>
<p id="p-22">Across the Atlantic, this familiar language was adopted almost verbatim, first in the Virginia Declaration of Rights, then in the Eighth Amendment, which states: "Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted."</p>
<p id="p-23">Adoption of the Excessive Fines Clause was in tune not only with English law; the Clause resonated as well with similar colonial-era provisions. See, <em>e.g.</em> , Pa. Frame of Govt., Laws Agreed Upon in England, Art. XVIII (1682), in 5 Federal and State Constitutions 3061 (F. Thorpe ed. 1909) ("[A]ll fines shall be moderate, and saving men's contenements, merchandize, or wainage."). In 1787, the constitutions of eight States-accounting for 70% of the U.S. population-forbade excessive fines. Calabresi, Agudo, &amp; Dore, State Bills of Rights in 1787 and 1791, <extracted-citation index="34" url="https://cite.case.law/citations/?q=85%20S.%20Cal.%20L.%20Rev.%201451"><span class="citation no-link">85 S. Cal. L. Rev. 1451</span></extracted-citation>, 1517 (2012).</p>
<p id="p-24">An even broader consensus obtained in 1868 upon ratification of the Fourteenth Amendment. By then, the constitutions of 35 of the 37 States-accounting for over 90% of the U.S. population-expressly prohibited excessive fines. Calabresi &amp; Agudo, Individual Rights Under State Constitutions When the Fourteenth Amendment Was Ratified in 1868, <extracted-citation index="35" url="https://cite.case.law/citations/?q=87%20Tex.%20L.%20Rev.%207">87 Texas L. Rev. 7</extracted-citation>, 82 (2008).</p>
<p id="p-25">Notwithstanding the States' apparent agreement that the right guaranteed by the Excessive Fines Clause was fundamental, abuses continued. Following the Civil War, Southern States enacted Black Codes to subjugate newly freed slaves and maintain the prewar racial hierarchy. Among these laws' provisions were draconian fines for violating broad proscriptions on "vagrancy" and other dubious offenses. See, <em>e.g.</em> , Mississippi Vagrant Law, Laws of Miss. § 2 (1865), in 1 W. Fleming, Documentary <a class="page-label" data-citation-index="1" data-label="689" href="#p689" id="p689">*689</a>History of Reconstruction 283-285 (1950). When newly freed slaves were unable to pay imposed fines, States often demanded involuntary labor instead. <em>E.g.</em> , <em><extracted-citation index="36" url="https://cite.case.law/citations/?q=87%20Tex.%20L.%20Rev.%207">id.</extracted-citation></em> § 5; see Finkelman, John Bingham and the Background to the Fourteenth Amendment, <extracted-citation index="37" url="https://cite.case.law/citations/?q=36%20Akron%20L.%20Rev.%20671">36 Akron L. Rev 671</extracted-citation>, 681-685 (2003) (describing Black Codes' use of fines and other methods to "replicate, as much as possible, a system of involuntary servitude"). Congressional debates over the Civil Rights Act of 1866, the joint resolution that became the Fourteenth Amendment, and similar measures repeatedly mentioned the use of fines to coerce involuntary labor. See, <em>e.g.</em> , Cong. Globe, 39th Cong., 1st Sess., 443 (1866); <em>id.,</em> at 1123-1124.</p>
<p id="p-26">Today, acknowledgment of the right's fundamental nature remains widespread. As Indiana itself reports, all 50 States have a constitutional provision prohibiting the imposition of excessive fines either directly or by requiring proportionality. Brief in Opposition 8-9. Indeed, Indiana explains that its own Supreme Court has held that the Indiana Constitution should be interpreted to impose the same restrictions as the Eighth Amendment. <em>Id.</em> , at 9 (citing <em>Norris</em> v. <em>State</em> , <extracted-citation case-ids="1823589" index="38" url="https://cite.case.law/ind/271/568/#p576"><span class="citation" data-id="2045779"><a href="/opinion/2045779/norris-v-state/" aria-description="Citation for case: Norris v. State">271 Ind. 568</a></span></extracted-citation>, 576, <extracted-citation case-ids="11067811" index="39" url="https://cite.case.law/ne2d/394/144/#p150"><span class="citation" data-id="2045779"><a href="/opinion/2045779/norris-v-state/" aria-description="Citation for case: Norris v. State">394 N.E.2d 144</a></span></extracted-citation>, 150 (1979) ).</p>
<p id="p-27">For good reason, the protection against excessive fines has been a constant shield throughout Anglo-American history: Exorbitant tolls undermine other constitutional liberties. Excessive fines can be used, for example, to retaliate against or chill the speech of political enemies, as the Stuarts' critics learned several centuries ago. See <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="40" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 267</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="41" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. Even absent a political motive, fines may be employed "in a measure out of accord with the penal goals of retribution and deterrence," for "fines are a source of revenue," while other forms of punishment "cost a State money." <em>Harmelin</em> v. <em>Michigan</em> , <extracted-citation case-ids="1107767" index="42" url="https://cite.case.law/us/501/957/#p979"><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/" aria-description="Citation for case: Harmelin v. Michigan">501 U.S. 957</a></span></extracted-citation>, 979, n. 9, <extracted-citation case-ids="1107767" index="43" url="https://cite.case.law/us/501/957/#p979"><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/" aria-description="Citation for case: Harmelin v. Michigan">111 S.Ct. 2680</a></span></extracted-citation>, <extracted-citation case-ids="1107767" index="44" url="https://cite.case.law/us/501/957/#p979"><span class="citation" data-id="9432400"><a href="/opinion/112646/harmelin-v-michigan/" aria-description="Citation for case: Harmelin v. Michigan">115 L.Ed.2d 836</a></span></extracted-citation> (1991) (opinion of Scalia, J.) ("it makes sense to scrutinize governmental action more closely when the State stands to benefit"). This concern is scarcely hypothetical. See Brief for American Civil Liberties Union et al. as <em>Amici Curiae</em> 7 ("Perhaps because they are politically easier to impose than generally applicable taxes, state and local governments nationwide increasingly depend heavily on fines and fees as a source of general revenue.").</p>
<p id="p-28">In short, the historical and logical case for concluding that the Fourteenth Amendment incorporates the Excessive Fines Clause is overwhelming. Protection against excessive punitive economic sanctions secured by the Clause is, to repeat, both "fundamental to our scheme of ordered liberty" and "deeply rooted in this Nation's history and tradition." <em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="45" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 767</a></span></extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="46" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation> (internal quotation marks omitted; emphasis deleted).</p>
<p id="p-29">II</p>
<p id="p-30">The State of Indiana does not meaningfully challenge the case for incorporating the Excessive Fines Clause as a general matter. Instead, the State argues that the Clause does not apply to its use of civil <em>in rem</em> forfeitures because, the State says, the Clause's specific application to such forfeitures is neither fundamental nor deeply rooted.</p>
<p id="p-31">In <em>Austin</em> v<em>. United States</em> , <extracted-citation case-ids="355668" index="47" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">509 U.S. 602</a></span></extracted-citation>, <extracted-citation case-ids="355668" index="48" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">113 S.Ct. 2801</a></span></extracted-citation>, <extracted-citation case-ids="355668" index="49" url="https://cite.case.law/us/509/602/#p609"><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">125 L.Ed.2d 488</a></span></extracted-citation> (1993), however, this Court held that civil <em>in rem</em> forfeitures fall within the Clause's protection when they are at least partially punitive. <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> arose in the federal context. But when a Bill of Rights protection is incorporated, the protection applies "identically to both the Federal Government and the States."</p>
<p id="p-32"><a class="page-label" data-citation-index="1" data-label="690" href="#p690" id="p690">*690</a><em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="50" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/#766" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 766</a></span>, n. 14</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="51" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>. Accordingly, to prevail, Indiana must persuade us either to overrule our decision in <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> or to hold that, in light of <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> , the Excessive Fines Clause is not incorporated because the Clause's application to civil <em>in rem</em> forfeitures is neither fundamental nor deeply rooted. The first argument is not properly before us, and the second misapprehends the nature of our incorporation inquiry.</p>
<p id="p-33">A</p>
<p id="p-34">In the Indiana Supreme Court, the State argued that forfeiture of Timbs's SUV would not be excessive. See Brief in Opposition 5. It never argued, however, that civil <em>in rem</em> forfeitures were categorically beyond the reach of the Excessive Fines Clause. The Indiana Supreme Court, for its part, held that the Clause did not apply to the States at all, and it nowhere addressed the Clause's application to civil <em>in rem</em> forfeitures. See <extracted-citation case-ids="12331536" index="52" url="https://cite.case.law/ne3d/84/1179/"><span class="citation" data-id="4217247"><a href="/opinion/4439994/state-of-indiana-v-tyson-timbs/" aria-description="Citation for case: State of Indiana v. Tyson Timbs">84 N.E.3d 1179</a></span></extracted-citation>. Accordingly, Timbs sought our review of the question "[w]hether the Eighth Amendment's Excessive Fines Clause is incorporated against the States under the Fourteenth Amendment." Pet. for Cert. i. In opposing review, Indiana attempted to reformulate the question to ask "[w]hether the Eighth Amendment's Excessive Fines Clause restricts States' use of civil asset forfeitures." Brief in Opposition i. And on the merits, Indiana has argued not only that the Clause is not incorporated, but also that <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> was wrongly decided. Respondents' "right, in their brief in opposition, to restate the questions presented," however, "does not give them the power to expand [those] questions." <em>Bray</em> v. <em>Alexandria Women's Health Clinic</em> , <extracted-citation case-ids="11925246" index="53" url="https://cite.case.law/us/506/263/#p279"><span class="citation" data-id="9432717"><a href="/opinion/112805/bray-v-alexandria-womens-health-clinic/" aria-description="Citation for case: Bray v. Alexandria Women&#x27;s Health Clinic">506 U.S. 263</a></span></extracted-citation>, 279, n. 10, <extracted-citation case-ids="11925246" index="54" url="https://cite.case.law/us/506/263/#p279"><span class="citation" data-id="9432717"><a href="/opinion/112805/bray-v-alexandria-womens-health-clinic/" aria-description="Citation for case: Bray v. Alexandria Women&#x27;s Health Clinic">113 S.Ct. 753</a></span></extracted-citation>, <extracted-citation case-ids="11925246" index="55" url="https://cite.case.law/us/506/263/#p279"><span class="citation" data-id="9432717"><a href="/opinion/112805/bray-v-alexandria-womens-health-clinic/" aria-description="Citation for case: Bray v. Alexandria Women&#x27;s Health Clinic">122 L.Ed.2d 34</a></span></extracted-citation> (1993) (emphasis deleted). That is particularly the case where, as here, a respondent's reformulation would lead us to address a question neither pressed nor passed upon below. Cf. <em>Cutter</em> v<em>. Wilkinson</em> , <extracted-citation case-ids="5868782" index="56" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">544 U.S. 709</a></span></extracted-citation>, 718, n. 7, <extracted-citation case-ids="5868782" index="57" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">125 S.Ct. 2113</a></span></extracted-citation>, <extracted-citation case-ids="5868782" index="58" url="https://cite.case.law/us/544/709/#p718"><span class="citation" data-id="9434809"><a href="/opinion/142900/cutter-v-wilkinson/" aria-description="Citation for case: Cutter v. Wilkinson">161 L.Ed.2d 1020</a></span></extracted-citation> (2005) ("[W]e are a court of review, not of first view ...."). We thus decline the State's invitation to reconsider our unanimous judgment in <em><span class="citation" data-id="9432892"><a href="/opinion/112904/austin-v-united-states/" aria-description="Citation for case: Austin v. United States">Austin</a></span></em> that civil <em>in rem</em> forfeitures are fines for purposes of the Eighth Amendment when they are at least partially punitive.</p>
<p id="p-35">B</p>
<p id="p-36">As a fallback, Indiana argues that the Excessive Fines Clause cannot be incorporated if it applies to civil <em>in rem</em> forfeitures. We disagree. In considering whether the Fourteenth Amendment incorporates a protection contained in the Bill of Rights, we ask whether the right guaranteed-not each and every particular application of that right-is fundamental or deeply rooted.</p>
<p id="p-37">Indiana's suggestion to the contrary is inconsistent with the approach we have taken in cases concerning novel applications of rights already deemed incorporated. For example, in <em>Packingham</em> v. <em>North Carolina</em> , 582 U.S. ----, <extracted-citation case-ids="12604756" index="59" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">137 S.Ct. 1730</a></span></extracted-citation>, <extracted-citation case-ids="12604756" index="60" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">198 L.Ed.2d 273</a></span></extracted-citation> (2017), we held that a North Carolina statute prohibiting registered sex offenders from accessing certain commonplace social media websites violated the First Amendment right to freedom of speech. In reaching this conclusion, we noted that the First Amendment's Free Speech Clause was "applicable to the States under the Due Process Clause of the Fourteenth Amendment." <em><extracted-citation case-ids="12604756" index="61" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">Id.,</a></span></extracted-citation></em> at ----, <extracted-citation case-ids="12604756" index="62" url="https://cite.case.law/s-ct/137/1730/"><span class="citation" data-id="4181058"><a href="/opinion/4403805/packingham-v-north-carolina/" aria-description="Citation for case: Packingham v. North Carolina">137 S.Ct., at 1733</a></span></extracted-citation>. We did not, however, inquire whether the Free Speech Clause's application specifically to social media websites was fundamental or deeply rooted. See also, <em>e.g.</em> , <em>Riley</em> v<em>. California</em> , <extracted-citation index="63" url="https://cite.case.law/citations/?q=573%20U.S.%20373"><span class="citation no-link">573 U.S. 373</span></extracted-citation>, <extracted-citation case-ids="12581677" index="64" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">134 S.Ct. 2473</a></span></extracted-citation>, <extracted-citation case-ids="12581677" index="65" url="https://cite.case.law/s-ct/134/2473/"><span class="citation" data-id="2680439"><a href="/opinion/2680439/riley-v-cal-united-states/" aria-description="Citation for case: Riley v. Cal. United States">189 L.Ed.2d 430</a></span></extracted-citation> (2014) (holding, without separately considering incorporation, that States' warrantless <a class="page-label" data-citation-index="1" data-label="691" href="#p691" id="p691">*691</a>search of digital information stored on cell phones ordinarily violates the Fourth Amendment). Similarly here, regardless of whether application of the Excessive Fines Clause to civil <em>in rem</em> forfeitures is itself fundamental or deeply rooted, our conclusion that the Clause is incorporated remains unchanged.</p>
<p id="p-38">* * *</p>
<p id="p-39">For the reasons stated, the judgment of the Indiana Supreme Court is vacated, and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p id="p-40">It is so ordered.</p>
<footnote label="1">
<p id="p-81">The sole exception is our holding that the Sixth Amendment requires jury unanimity in federal, but not state, criminal proceedings. <em>Apodaca</em> v. <em>Oregon</em> , <extracted-citation case-ids="6171091" index="66" url="https://cite.case.law/us/406/404/"><span class="citation" data-id="9424885"><a href="/opinion/108539/apodaca-v-oregon/" aria-description="Citation for case: Apodaca v. Oregon">406 U.S. 404</a></span></extracted-citation>, <extracted-citation case-ids="6171091" index="67" url="https://cite.case.law/us/406/404/"><span class="citation" data-id="9424885"><a href="/opinion/108539/apodaca-v-oregon/" aria-description="Citation for case: Apodaca v. Oregon">92 S.Ct. 1628</a></span></extracted-citation>, <extracted-citation case-ids="6171091" index="68" url="https://cite.case.law/us/406/404/"><span class="citation" data-id="9424885"><a href="/opinion/108539/apodaca-v-oregon/" aria-description="Citation for case: Apodaca v. Oregon">32 L.Ed.2d 184</a></span></extracted-citation> (1972). As we have explained, that "exception to th[e] general rule ... was the result of an unusual division among the Justices," and it "does not undermine the well-established rule that incorporated Bill of Rights protections apply identically to the States and the Federal Government." <em>McDonald</em> , <extracted-citation case-ids="12455289,3644508" index="69" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/#766" aria-description="Citation for case: McDonald v. City of Chicago">561 U.S., at 766</a></span>, n. 14</extracted-citation>, <extracted-citation case-ids="12455289,3644508" index="70" url="https://cite.case.law/us/561/742/"><span class="citation" data-id="9435860"><a href="/opinion/149702/mcdonald-v-city-of-chicago/" aria-description="Citation for case: McDonald v. City of Chicago">130 S.Ct. 3020</a></span></extracted-citation>.</p>
</footnote>
<footnote label="2">
<p id="p-82">"Amercements were payments to the Crown, and were required of individuals who were 'in the King's mercy,' because of some act offensive to the Crown." <em>Browning-Ferris</em> , <extracted-citation case-ids="6214309" index="71" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">492 U.S., at 269</a></span></extracted-citation>, <extracted-citation case-ids="6214309" index="72" url="https://cite.case.law/us/492/257/#p263"><span class="citation" data-id="9431824"><a href="/opinion/112324/browning-ferris-industries-of-vermont-inc-v-kelco-disposal-inc/" aria-description="Citation for case: Browning-Ferris Industries of Vermont, Inc. v. Kelco...">109 S.Ct. 2909</a></span></extracted-citation>. "[T]hough fines and amercements had distinct historical antecedents, they served fundamentally similar purposes-and, by the seventeenth and eighteenth centuries, the terms were often used interchangeably." Brief for Eighth Amendment Scholars as <em>Amici Curiae</em> 12.</p>
</footnote>
</opinion>
```

---
