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

## GROUP: _overhaul2/lake/cases/Brower v. County of Inyo.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Brower v. County of Inyo"
type: case
citation: "489 U.S. 593 (1989)"
parallel_cite: "109 S. Ct. 1378; 103 L. Ed. 2d 628; 57 U.S.L.W. 4321"
neutral_cite: 1989 U.S. LEXIS 1569
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1989
date_decided: 1989-03-21
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1989-03-21
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brower v. County of Inyo
  varies_by_point: false
  scope_note: "Good law. A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; a stop produced by the very instrumentality the police put in place is a seizure. Canonical caption is Brower v. County of Inyo; the ingest queue refers to it as Brower v. Inyo County (aliased)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/"
  cluster_id: 112218
  opinion_id: 112218
  identity_checked: true
homes:
  - page: "[[Seizure of the Person]]"
    role: "Anchor"
  - page: "[[Use of Force]]"
    role: "Related (cross-doctrine)"
related: ["[[California v. Hodari D.]]", "[[Torres v. Madrid]]", "[[Scott v. Harris]]", "[[Tennessee v. Garner]]"]
aliases: ["Brower v. Inyo County"]
tags: ["case", "fourth-amendment", "seizure", "roadblock", "use-of-force", "section-1983"]
holding: "A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; stopping a fleeing driver with a roadblock he crashes into is a seizure because he is stopped by the very instrumentality put in place to stop him."
lake:
  record_id: Brower v. County of Inyo
  status: verified
  projected_at: 2026-07-09
---

# Brower v. County of Inyo

*489 U.S. 593 (1989)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
After Brower stole a car and led police on a roughly 20-mile chase, officers set up a roadblock to stop him: they placed an 18-wheel tractor-trailer across both lanes of the highway, behind a curve, with a police car's headlights aimed to blind Brower as he approached. Brower crashed into the trailer and was killed. His heirs sued under 42 U.S.C. § 1983, alleging an unreasonable Fourth Amendment seizure. The District Court dismissed for failure to state a claim, reasoning no "seizure" had occurred, and the Ninth Circuit affirmed.

## Issue
Whether a Fourth Amendment "seizure" occurs when police stop a fleeing motorist by means of a roadblock into which he crashes — i.e., what governmental conduct counts as a seizure of the person.

## Rule
A seizure requires that the government stop the person by the means it intended. "[A] Fourth Amendment seizure does not occur whenever there is a governmentally caused termination of an individual's freedom of movement (the innocent passerby), nor even whenever there is a governmentally caused and governmentally *desired* termination of an individual's freedom of movement (the fleeing felon), but only when there is a governmental termination of freedom of movement *through means intentionally applied*." — 489 U.S. at 596–597. ^pin-596

The Amendment "addresses 'misuse of power,' . . . not the accidental effects of otherwise lawful government conduct." — *Id.* at 596. ^pin-596b

It is therefore "enough for a seizure that a person be stopped by the very instrumentality set in motion or put in place in order to achieve that result." — [*Id.* at 599](https://www.courtlistener.com/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/#:~:text=enough%20for%20a%20seizure%20that). ^pin-599

## Application
Unlike a pursuing police car with flashing lights — which stops the suspect, if at all, only by his own loss of control — a roadblock "is designed to produce a stop by physical impact if voluntary compliance does not occur." Brower was stopped by the very obstacle the officers erected to stop him: "Brower was meant to be stopped by the physical obstacle of the roadblock — and that he was so stopped." The Court declined to parse the officers' subjective hope that he would halt short of the barrier, or to distinguish a roadblock placed for a voluntary stop from one placed around a bend to force a collision. Because the complaint alleged a stop by the intended means, it stated a Fourth Amendment seizure; the Court reversed the dismissal and [[Reading and Citing Cases#on-remand|remanded]] for the separate question whether that seizure was unreasonable.

## Conclusion
A seizure of the person occurs when the government terminates freedom of movement through means intentionally applied, which the alleged roadblock did; the dismissal was reversed and the case [[Reading and Citing Cases#on-remand|remanded]] to decide reasonableness. *Brower* supplies the controlling definition of when a seizure of the person occurs.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Brower*'s "means intentionally applied" definition governs seizure-of-the-person analysis and is applied in [[California v. Hodari D.]] (show of authority requires submission), [[Scott v. Harris]] (deadly-force pursuit seizure), and [[Torres v. Madrid]] (application of physical force with intent to restrain is a seizure even if the suspect escapes).

## Appears on
- [[Seizure of the Person]] — *Anchor*
- [[Use of Force]] — *Related (cross-doctrine)*

## Sources
- *Brower v. County of Inyo*, 489 U.S. 593 (1989) — https://www.courtlistener.com/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/ — pinpoints: 596–597, 599.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "f80b62f06469f3b0", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brower v. County of Inyo"}, "payload": {"all": [{"cite": "489 U.S. 593", "page": "593", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "489"}, {"cite": "109 S. Ct. 1378", "page": "1378", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "109"}, {"cite": "103 L. Ed. 2d 628", "page": "628", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "103"}, {"cite": "1989 U.S. LEXIS 1569", "page": "1569", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1989"}, {"cite": "57 U.S.L.W. 4321", "page": "4321", "reporter": "U.S.L.W.", "selected_official": false, "source": "cluster.citations[]", "type": 4, "volume": "57"}], "display": "489 U.S. 593", "official": {"cite": "489 U.S. 593", "page": "593", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "489"}, "official_selection_present": true, "record_id": "Brower v. County of Inyo"}}
{"assertion_id": "2a4c5773509fd9e0", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-596b", "record_id": "Brower v. County of Inyo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-596b", "pinpoint_status": "slip-only", "quote": "addresses 'misuse of power,' . . . not the accidental effects of otherwise lawful government conduct.", "quote_fidelity": "mismatch", "record_id": "Brower v. County of Inyo", "star_marker": null}}
{"assertion_id": "a77d22616b1c3136", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-599", "record_id": "Brower v. County of Inyo"}, "payload": {"fragment": "#:~:text=enough%20for%20a%20seizure%20that", "page": null, "pin_id": "pin-599", "pinpoint_status": "star-verified", "quote": "enough for a seizure that a person be stopped by the very instrumentality set in motion or put in place in order to achieve that result.", "quote_fidelity": "matched", "record_id": "Brower v. County of Inyo", "star_marker": "599"}}
{"assertion_id": "d533a3614fab6194", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-596", "record_id": "Brower v. County of Inyo"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-596", "pinpoint_status": "slip-only", "quote": "occurs when police stop a fleeing motorist by means of a roadblock into which he crashes — i.e., what governmental conduct counts as a seizure of the person. ## Rule A seizure requires that the government stop the person by the means it intended.", "quote_fidelity": "mismatch", "record_id": "Brower v. County of Inyo", "star_marker": null}}
{"assertion_id": "acd0e1619f5b3f7a", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brower v. County of Inyo"}, "payload": {"as_of_content": "1989-03-21", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brower v. County of Inyo", "scope_note": "Good law. A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; a stop produced by the very instrumentality the police put in place is a seizure. Canonical caption is Brower v. County of Inyo; the ingest queue refers to it as Brower v. Inyo County (aliased).", "varies_by_point": false}}
```

### lake record — Brower v. County of Inyo

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brower v. County of Inyo",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brower Ex Rel. Estate of Caldwell v. County of Inyo",
    "case_name_short": "Brower",
    "case_name_full": "BROWER, Individually and as Administrator of the ESTATE OF CALDWELL (BROWER), Et Al. v. COUNTY OF INYO Et Al.",
    "input_case_name": "Brower v. County of Inyo",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1989-03-21",
    "year": 1989,
    "docket": null,
    "cluster_id": 112218,
    "lead_opinion_id": 112218,
    "sibling_ids": [
      112218,
      9431604,
      9431605
    ],
    "absolute_url": "/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "489 U.S. 593",
      "volume": "489",
      "reporter": "U.S.",
      "page": "593",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "109 S. Ct. 1378",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 628",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "628",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4321",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4321",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1989 U.S. LEXIS 1569",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1569",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "489 U.S. 593",
        "volume": "489",
        "reporter": "U.S.",
        "page": "593",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "109 S. Ct. 1378",
        "volume": "109",
        "reporter": "S. Ct.",
        "page": "1378",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "103 L. Ed. 2d 628",
        "volume": "103",
        "reporter": "L. Ed. 2d",
        "page": "628",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1989 U.S. LEXIS 1569",
        "volume": "1989",
        "reporter": "U.S. LEXIS",
        "page": "1569",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "57 U.S.L.W. 4321",
        "volume": "57",
        "reporter": "U.S.L.W.",
        "page": "4321",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "489 U.S. 593",
    "official_selection": {
      "court_class": "scotus",
      "selected": "489 U.S. 593",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-596",
      "page": null,
      "quote": "occurs when police stop a fleeing motorist by means of a roadblock into which he crashes \u2014 i.e., what governmental conduct counts as a seizure of the person. ## Rule A seizure requires that the government stop the person by the means it intended.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-596b",
      "page": null,
      "quote": "addresses 'misuse of power,' . . . not the accidental effects of otherwise lawful government conduct.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-599",
      "page": null,
      "quote": "enough for a seizure that a person be stopped by the very instrumentality set in motion or put in place in order to achieve that result.",
      "star_marker": "599",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 15618,
      "fragment": "#:~:text=enough%20for%20a%20seizure%20that",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1989-03-21",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brower v. County of Inyo",
    "varies_by_point": false,
    "scope_note": "Good law. A Fourth Amendment seizure occurs only when the government terminates a person's freedom of movement through means intentionally applied; a stop produced by the very instrumentality the police put in place is a seizure. Canonical caption is Brower v. County of Inyo; the ingest queue refers to it as Brower v. Inyo County (aliased).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Morrow v. Meachum",
          "cluster_id": 8443910,
          "cite": [
            "917 F.3d 870"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Tanguay",
          "cluster_id": 4598184,
          "cite": [
            "918 F.3d 1"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Claudia Harbourt v. PPE Casino Resorts Maryland",
          "cluster_id": 3197571,
          "cite": [
            "820 F.3d 655",
            "26 Wage & Hour Cas.2d (BNA) 625",
            "2016 U.S. App. LEXIS 7415",
            "2016 WL 1621908"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 2546477,
          "cite": [
            "359 S.W.3d 725",
            "2011 WL 6176184"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Hernandez v. City of Pomona",
          "cluster_id": 1801687,
          "cite": [
            "46 Cal. 4th 501",
            "207 P.3d 506",
            "94 Cal. Rptr. 3d 1",
            "2009 Cal. LEXIS 4630"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Bell Atlantic Corp. v. Twombly",
          "cluster_id": 145730,
          "cite": [
            "167 L. Ed. 2d 929",
            "127 S. Ct. 1955",
            "550 U.S. 544",
            "2007 U.S. LEXIS 5901",
            "41 Communications Reg. (P&F) 567",
            "20 Fla. L. Weekly Fed. S 267",
            "68 Fed. R. Serv. 3d 661",
            "75 U.S.L.W. 4337"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Neitzke v. Williams",
          "cluster_id": 112254,
          "cite": [
            "104 L. Ed. 2d 338",
            "109 S. Ct. 1827",
            "490 U.S. 319",
            "1989 U.S. LEXIS 2231",
            "57 U.S.L.W. 4493"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Graham v. Connor",
          "cluster_id": 112257,
          "cite": [
            "104 L. Ed. 2d 443",
            "109 S. Ct. 1865",
            "490 U.S. 386",
            "1989 U.S. LEXIS 2467",
            "57 U.S.L.W. 4513"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Scott v. Harris",
          "cluster_id": 145738,
          "cite": [
            "167 L. Ed. 2d 686",
            "127 S. Ct. 1769",
            "550 U.S. 372",
            "2007 U.S. LEXIS 4748"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "County of Sacramento v. Lewis",
          "cluster_id": 118214,
          "cite": [
            "140 L. Ed. 2d 1043",
            "118 S. Ct. 1708",
            "523 U.S. 833",
            "1998 U.S. LEXIS 3404"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Jones",
          "cluster_id": 622304,
          "cite": [
            "181 L. Ed. 2d 911",
            "132 S. Ct. 945",
            "565 U.S. 400",
            "2012 U.S. LEXIS 1063"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shirley Presley v. City of Charlottesville Rivanna Trails Foundation",
          "cluster_id": 795822,
          "cite": [
            "464 F.3d 480",
            "2006 U.S. App. LEXIS 24048",
            "2006 WL 2709208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Hayes v. Idaho Correctional Center",
          "cluster_id": 4372888,
          "cite": [
            "849 F.3d 1204",
            "2017 WL 836072",
            "2017 U.S. App. LEXIS 3851"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lamont v. New Jersey",
          "cluster_id": 205997,
          "cite": [
            "637 F.3d 177",
            "2011 U.S. App. LEXIS 4104",
            "2011 WL 753856"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Outdoor Media Dimensions Inc. v. State",
          "cluster_id": 836243,
          "cite": [
            "20 P.3d 180",
            "331 Or. 634",
            "2001 Ore. LEXIS 135"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Henry Szabla v. City Of Brooklyn Park",
          "cluster_id": 797743,
          "cite": [
            "486 F.3d 385",
            "2007 U.S. App. LEXIS 11602"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Murphy v. Lynn",
          "cluster_id": 7048090,
          "cite": [
            "118 F.3d 938",
            "1997 WL 371091"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kyle Ciminillo v. Thomas Streicher Daniel Hills Richard Janke, Gerald Knight City of Cincinnati",
          "cluster_id": 792929,
          "cite": [
            "434 F.3d 461",
            "2006 U.S. App. LEXIS 1020",
            "2006 WL 89157"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
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
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Flores v. City of Palacios",
          "cluster_id": 36003,
          "cite": [
            "381 F.3d 391",
            "2004 U.S. App. LEXIS 16477",
            "2004 WL 1775948"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brower v. County of Inyo:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(112218 OR 9431604 OR 9431605) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMTc3ODkxMjAwMDAwJnM9MTQ1NzM4JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28112218+OR+9431604+OR+9431605%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(112218 OR 9431604 OR 9431605)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNTkmcz0xNTI2NTImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28112218+OR+9431604+OR+9431605%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(112218 OR 9431604 OR 9431605)",
        "reviewed": 26,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 26,
        "triage_read": 0,
        "triage_snippet_classified": 26
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(112218 OR 9431604 OR 9431605)",
    "indexed_citing_opinions": 705,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 112218,
        "count": 604,
        "count_source": "search"
      },
      {
        "opinion_id": 9431604,
        "count": 112,
        "count_source": "search"
      },
      {
        "opinion_id": 9431605,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1485,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brower-v-county-of-inyo.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjgxMDUxNzImcz05MzY5NTk3JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28112218+OR+9431604+OR+9431605%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 112218,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 100413,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 100980,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 105573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 108305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 109009,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 110169,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 110264,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111148,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111831,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 458562,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 461210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 476350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 484686,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 112218,
        "cited_id": 487470,
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
    "date_created": "2026-07-04T22:57:48Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T23:16:50Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T23:12:53Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brower v. County of Inyo

```
<div>
<center><b><span class="citation" data-id="9431604"><a href="/opinion/112218/brower-ex-rel-estate-of-caldwell-v-county-of-inyo/" aria-description="Citation for case: Brower Ex Rel. Estate of Caldwell v. County of Inyo">489 U.S. 593</a></span> (1989)</b></center>
<center><h1>BROWER, INDIVIDUALLY AND AS ADMINISTRATOR OF THE ESTATE OF CALDWELL (BROWER), ET AL.<br>
v.<br>
COUNTY OF INYO ET AL.</h1></center>
<center>No. 87-248.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued January 11, 1989</center>
<center>Decided March 21, 1989</center>
CERTIORARI TO THE UNITED STATES COURT OF APPEALS FOR THE NINTH CIRCUIT
<p><span class="star-pagination">*594</span> <i>Robert G. Gilmore</i> argued the cause for petitioners. With him on the briefs was <i>Craig A. Diamond.</i></p>
<p><i>Philip W. McDowell</i> argued the cause for respondents. With him on the brief was <i>Gregory L. James.</i></p>
<p>JUSTICE SCALIA delivered the opinion of the Court.</p>
<p>On the night of October 23, 1984, William James Caldwell (Brower) was killed when the stolen car that he had been driving at high speeds for approximately 20 miles in an effort to elude pursuing police crashed into a police roadblock. His heirs, petitioners here, brought this action in Federal District Court under <span class="citation no-link">42 U. S. C. § 1983</span>, claiming, <i>inter alia,</i> that respondents used "brutal, excessive, unreasonable and unnecessary physical force" in establishing the roadblock, and thus effected an unreasonable seizure of Brower, in violation of the Fourth Amendment. Petitioners alleged that "under color of statutes, regulations, customs and usages," respondents (1) caused an 18-wheel tractor-trailer to be placed across both lanes of a two-lane highway in the path of Brower's flight, (2) "effectively concealed" this roadblock by placing it behind a curve and leaving it unilluminated, and (3) positioned a police car, with its headlights on, between Brower's oncoming vehicle and the truck, so that Brower would be "blinded" on his approach. App. 8-9. Petitioners further alleged that Brower's fatal collision with the truck was "a proximate result" of this official conduct. <span class="citation no-link"><i>Id.,</i> at 9</span>. The District Court granted respondents' motion to dismiss the complaint for failure to state a claim on the ground (insofar as the Fourth Amendment claim was concerned) that "establishing a roadblock [was] not unreasonable under the circumstances." App. to Pet. for Cert. A-21. A divided panel of the Court of Appeals for the Ninth Circuit affirmed the dismissal of the Fourth Amendment claim on the basis that no "seizure" had occurred. <span class="citation multiple-matches"><a href="/c/F.%202d/817/540/">817 F. 2d 540</a></span>, 545-546 (1987). We granted certiorari, <span class="citation multiple-matches"><a href="/c/U.%20S./487/1217/">487 U. S. 1217</a></span> (1988), to resolve a conflict between that decision and the contrary holding <span class="star-pagination">*595</span> of the Court of Appeals for the Fifth Circuit in <i>Jamieson</i> v. <i>Shaw,</i> <span class="citation" data-id="8934389"><a href="/opinion/8943843/jamieson-v-shaw/" aria-description="Citation for case: Jamieson v. Shaw">772 F. 2d 1205</a></span> (1985).</p>
<p>The Fourth Amendment to the Constitution provides:</p>
<blockquote>"The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the person or things to be seized."</blockquote>
<p>In <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985), all Members of the Court agreed that a police officer's fatal shooting of a fleeing suspect constituted a Fourth Amendment "seizure." See <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 7</a></span>; <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#25" aria-description="Citation for case: Tennessee v. Garner"><i>id.,</i> at 25</a></span> (O'CONNOR, J., dissenting). We reasoned that "[w]henever an officer restrains the freedom of a person to walk away, he has seized that person." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner"><i>Id.,</i> at 7</a></span>. While acknowledging <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>,</i> the Court of Appeals here concluded that no "seizure" occurred when Brower collided with the police roadblock because "[p]rior to his failure to stop voluntarily, his freedom of movement was never arrested or restrained" and because "[h]e had a number of opportunities to stop his automobile prior to the impact." 817 F. 2d, at 546. Essentially the same thing, however, could have been said in <i><span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">Garner</a></span>.</i> Brower's independent decision to continue the chase can no more eliminate respondents' responsibility for the termination of his movement effected by the roadblock than Garner's independent decision to flee eliminated the Memphis police officer's responsibility for the termination of his movement effected by the bullet.</p>
<p>The Court of Appeals was impelled to its result by consideration of what it described as the "analogous situation" of a police chase in which the suspect unexpectedly loses control of his car and crashes. See <i>Galas</i> v. <i>McKee,</i> <span class="citation" data-id="476350"><a href="/opinion/476350/galas-v-mckee/#202" aria-description="Citation for case: Galas v. Mckee">801 F. 2d 200, 202-203</a></span> (CA6 1986) (no seizure in such circumstances). We agree that no unconstitutional seizure occurs there, but not for a reason that has any application to the present case. <span class="star-pagination">*596</span> Violation of the Fourth Amendment requires an intentional acquisition of physical control. A seizure occurs even when an unintended person or thing is the object of the detention or taking, see <i>Hill</i> v. <i>California,</i> <span class="citation" data-id="9424518"><a href="/opinion/108305/hill-v-california/#802" aria-description="Citation for case: Hill v. California">401 U. S. 797, 802-805</a></span> (1971); cf. <i>Maryland</i> v. <i>Garrison,</i> <span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#85" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 85-89</a></span> (1987), but the detention or taking itself must be willful. This is implicit in the word "seizure," which can hardly be applied to an unknowing act. The writs of assistance that were the principal grievance against which the Fourth Amendment was directed, see <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#624" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 624-625</a></span> (1886); T. Cooley, Constitutional Limitations *301-*302, did not involve unintended consequences of government action. Nor did the general warrants issued by Lord Halifax in the 1760's, which produced "the first and only major litigation in the English courts in the field of search and seizure," T. Taylor, Two Studies in Constitutional Interpretation 26 (1969), including the case we have described as a "monument of English freedom" "undoubtedly familiar" to "every American statesman" at the time the Constitution was adopted, and considered to be "the true and ultimate expression of constitutional law," <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#626" aria-description="Citation for case: Boyd v. United States"><i>Boyd, supra,</i> at 626</a></span> (discussing <i>Entick</i> v. <i>Carrington,</i> 19 How. St. Tr. 1029, 95 Eng. Rep. 807 (K. B. 1765)). In sum, the Fourth Amendment addresses "misuse of power," <i>Byars</i> v. <i>United States,</i> <span class="citation" data-id="100980"><a href="/opinion/100980/byars-v-united-states/#33" aria-description="Citation for case: Byars v. United States">273 U. S. 28, 33</a></span> (1927), not the accidental effects of otherwise lawful government conduct.</p>
<p>Thus, if a parked and unoccupied police car slips its brake and pins a passerby against a wall, it is likely that a tort has occurred, but not a violation of the Fourth Amendment. And the situation would not change if the passerby happened, by lucky chance, to be a serial murderer for whom there was an outstanding arrest warrant  even if, at the time he was thus pinned, he was in the process of running away from two pursuing constables. It is clear, in other words, that a Fourth Amendment seizure does not occur whenever there is a governmentally caused termination of an <span class="star-pagination">*597</span> individual's freedom of movement (the innocent passerby), nor even whenever there is a governmentally caused and governmentally <i>desired</i> termination of an individual's freedom of movement (the fleeing felon), but only when there is a governmental termination of freedom of movement <i>through means intentionally applied.</i> That is the reason there was no seizure in the hypothetical situation that concerned the Court of Appeals. The pursuing police car sought to stop the suspect only by the show of authority represented by flashing lights and continuing pursuit; and though he was in fact stopped, he was stopped by a different means  his loss of control of his vehicle and the subsequent crash. If, instead of that, the police cruiser had pulled alongside the fleeing car and sideswiped it, producing the crash, then the termination of the suspect's freedom of movement would have been a seizure.</p>
<p>This analysis is reflected by our decision in <i>Hester</i> v. <i>United States,</i> <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/" aria-description="Citation for case: Hester v. United States">265 U. S. 57</a></span> (1924), where an armed revenue agent had pursued the defendant and his accomplice after seeing them obtain containers thought to be filled with "moonshine whisky." During their flight they dropped the containers, which the agent recovered. The defendant sought to suppress testimony concerning the containers' contents as the product of an unlawful seizure. Justice Holmes, speaking for a unanimous Court, concluded: "The defendant's own acts, and those of his associates, disclosed the jug, the jar and the bottle  and there was no seizure in the sense of the law when the officers examined the contents of each after they had been abandoned." <span class="citation" data-id="100413"><a href="/opinion/100413/hester-v-united-states/#58" aria-description="Citation for case: Hester v. United States"><i>Id.,</i> at 58</a></span>. Thus, even though the incriminating containers were unquestionably taken into possession as a result (in the broad sense) of action by the police, the Court held that no seizure had taken place. It would have been quite different, of course, if the revenue agent had shouted, "Stop and give us those bottles, in the name of the law!" and the defendant and his accomplice had complied. Then the taking of possession would have been <span class="star-pagination">*598</span> not merely the result of government action but the result of the very means (the show of authority) that the government selected, and a Fourth Amendment seizure would have occurred.</p>
<p>In applying these principles to the dismissal of petitioners' Fourth Amendment complaint for failure to state a claim, we can sustain the District Court's action only if, taking the allegations of the complaint in the light most favorable to petitioners, see <i>Scheuer</i> v. <i>Rhodes,</i> <span class="citation" data-id="109009"><a href="/opinion/109009/scheuer-v-rhodes/#236" aria-description="Citation for case: Scheuer v. Rhodes">416 U. S. 232, 236</a></span> (1974), we nonetheless conclude that they could prove no set of facts entitling them to relief for a "seizure." See <i>Conley</i> v. <i>Gibson,</i> <span class="citation" data-id="105573"><a href="/opinion/105573/conley-v-gibson/#45" aria-description="Citation for case: Conley v. Gibson">355 U. S. 41, 45-46</a></span> (1957). Petitioners have alleged the establishment of a roadblock crossing both lanes of the highway. In marked contrast to a police car pursuing with flashing lights, or to a policeman in the road signaling an oncoming car to halt, see <i>Kibbe</i> v. <i>Springfield,</i> <span class="citation" data-id="461210"><a href="/opinion/461210/lois-thurston-kibbe-administrator-of-the-estate-of-clinton-thurston-v/#802" aria-description="Citation for case: Lois Thurston Kibbe, Administrator of the Estate of...">777 F. 2d 801, 802-803</a></span> (CA1 1985), cert. dism'd, <span class="citation" data-id="9430858"><a href="/opinion/111831/city-of-springfield-v-kibbe/" aria-description="Citation for case: City of Springfield v. Kibbe">480 U. S. 257</a></span> (1987), a roadblock is not just a significant show of authority to induce a voluntary stop, but is designed to produce a stop by physical impact if voluntary compliance does not occur. It may well be that respondents here preferred, and indeed earnestly hoped, that Brower would stop on his own, without striking the barrier, but we do not think it practicable to conduct such an inquiry into subjective intent. See <i>United States</i> v. <i>Leon,</i> <span class="citation" data-id="9429766"><a href="/opinion/111262/united-states-v-leon/#922" aria-description="Citation for case: United States v. Leon">468 U. S. 897, 922, n. 23</a></span> (1984); see also <i>Anderson</i> v. <i>Creighton,</i> <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 641</a></span> (1987); <i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 815-819</a></span> (1982). Nor do we think it possible, in determining whether there has been a seizure in a case such as this, to distinguish between a roadblock that is designed to give the oncoming driver the option of a voluntary stop (<i>e. g.,</i> one at the end of a long straightaway), and a roadblock that is designed precisely to produce a collision (<i>e. g.,</i> one located just around a bend). In determining whether the means that terminates the freedom of movement is the very means that the government intended we cannot draw too fine a line, or we will be driven to saying that one is not seized who has been <span class="star-pagination">*599</span> stopped by the accidental discharge of a gun with which he was meant only to be bludgeoned, or by a bullet in the heart that was meant only for the leg. We think it enough for a seizure that a person be stopped by the very instrumentality set in motion or put in place in order to achieve that result. It was enough here, therefore, that, according to the allegations of the complaint, Brower was meant to be stopped by the physical obstacle of the roadblock  and that he was so stopped.</p>
<p>This is not to say that the precise character of the roadblock is irrelevant to further issues in this case. "Seizure" alone is not enough for § 1983 liability; the seizure must be "unreasonable." Petitioners can claim the right to recover for Brower's death only because the unreasonableness they allege consists precisely of setting up the roadblock in such manner as to be likely to kill him. This should be contrasted with the situation that would obtain if the sole claim of unreasonableness were that there was no probable cause for the stop. In that case, if Brower had had the opportunity to stop voluntarily at the roadblock, but had negligently or intentionally driven into it, then, because of lack of proximate causality, respondents, though responsible for depriving him of his freedom of movement, would not be liable for his death. See <i>Martinez</i> v. <i>California,</i> <span class="citation" data-id="110169"><a href="/opinion/110169/martinez-v-california/#285" aria-description="Citation for case: Martinez v. California">444 U. S. 277, 285</a></span> (1980); <i>Cameron</i> v. <i>Pontiac,</i> <span class="citation" data-id="484686"><a href="/opinion/484686/betty-cameron-personal-representative-of-the-estate-of-christopher-cameron/#786" aria-description="Citation for case: Betty Cameron, Personal Representative of the Estate of...">813 F. 2d 782, 786</a></span> (CA6 1987). Thus, the circumstances of this roadblock, including the allegation that headlights were used to blind the oncoming driver, may yet determine the outcome of this case.</p>
<p>The complaint here sufficiently alleges that respondents, under color of law, sought to stop Brower by means of a roadblock and succeeded in doing so. That is enough to constitute a "seizure" within the meaning of the Fourth Amendment. Accordingly, we reverse the judgment of the Court of Appeals and remand for consideration of whether the District Court properly dismissed the Fourth Amendment claim <span class="star-pagination">*600</span> on the basis that the alleged roadblock did not effect a seizure that was "unreasonable."</p>
<p><i>It is so ordered.</i></p>
<p>JUSTICE STEVENS, with whom JUSTICE BRENNAN, JUSTICE MARSHALL, and JUSTICE BLACKMUN join, concurring in the judgment.</p>
<p>The Court is unquestionably correct in concluding that respondents' use of a roadblock to stop Brower's car constituted a seizure within the meaning of the Fourth Amendment. I therefore concur in its judgment. I do not, however, join its opinion because its dicta seem designed to decide a number of cases not before the Court and to establish the proposition that "[v]iolation of the Fourth Amendment requires an intentional acquisition of physical control." <i>Ante,</i> at 596.</p>
<p>The intentional acquisition of physical control of something is no doubt a characteristic of the typical seizure, but I am not entirely sure that it is an essential element of every seizure or that this formulation is particularly helpful in deciding close cases. The Court suggests that the test it articulates does not turn on the subjective intent of the officer. <i>Ante,</i> at 598. This, of course, not only comports with the recent trend in our cases, see, <i>e. g., </i><i>Harlow</i> v. <i>Fitzgerald,</i> <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#815" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 815-819</a></span> (1982); <i>United States</i> v. <i>Mendenhall,</i> <span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/#554" aria-description="Citation for case: United States v. Mendenhall">446 U. S. 544, 554, n. 6</a></span> (1980) (opinion of Stewart, J.), but also makes perfect sense. No one would suggest that the Fourth Amendment provides no protection against a police officer who is too drunk to act intentionally, yet who appears in uniform brandishing a weapon in a threatening manner. Alternatively, however, the concept of objective intent, at least in the vast majority of cases, adds little to the well-established rule that "a person has been `seized' within the meaning of the Fourth Amendment only if, in view of all of the circumstances surrounding the incident, a reasonable person would have believed that he was not free to leave." <i><span class="citation" data-id="9427929"><a href="/opinion/110264/united-states-v-mendenhall/" aria-description="Citation for case: United States v. Mendenhall">Id.,</a></span></i> at 554 <span class="star-pagination">*601</span> (opinion of Stewart, J.); see also <i>INS</i> v. <i>Delgado,</i> <span class="citation" data-id="9429566"><a href="/opinion/111148/immigration-naturalization-service-v-delgado/#215" aria-description="Citation for case: Immigration &amp; Naturalization Service v. Delgado">466 U. S. 210, 215</a></span> (1984).</p>
<p>There may be a case that someday comes before this Court in which the concept of intent is useful in applying the Fourth Amendment. What is extraordinary about the Court's discussion of the intent requirement in this case is that there is no dispute that the roadblock was intended to stop the decedent. Decision in the case before us is thus not advanced by pursuing a hypothetical inquiry concerning whether an unintentional act might also violate the Fourth Amendment. Rather, as explained in Judge Pregerson's dissent in the Court of Appeals, this case is plainly controlled by our decision in <i>Tennessee</i> v. <i>Garner,</i> <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/" aria-description="Citation for case: Tennessee v. Garner">471 U. S. 1</a></span> (1985). <span class="citation multiple-matches"><a href="/c/F.%202d/817/540/">817 F. 2d 540</a></span>, 548 (CA9 1987) (opinion concurring in part and dissenting in part). In that case, we held that "there can be no question that apprehension by the use of deadly force is a seizure subject to the reasonableness requirement of the Fourth Amendment." <span class="citation" data-id="9429990"><a href="/opinion/111397/tennessee-v-garner/#7" aria-description="Citation for case: Tennessee v. Garner">471 U. S., at 7</a></span>. Because it was undisputed that the police officer acted intentionally, we did not discuss the hypothetical case of an unintentional seizure. I would exercise the same restraint here.</p>
<p>I am in full accord with Judge Pregerson's dissenting opinion, and, for the reasons stated in his opinion, I join the Court's judgment.</p>
</div>
```

---

## GROUP: _overhaul2/lake/cases/Brown v. Illinois.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Brown v. Illinois"
type: case
citation: "422 U.S. 590 (1975)"
parallel_cite: "95 S. Ct. 2254; 45 L. Ed. 2d 416"
neutral_cite: 1975 U.S. LEXIS 82
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1975
date_decided: 1975-06-26
docket: 73-6650
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1975-06-26
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brown v. Illinois
  varies_by_point: false
  scope_note: "Attenuation factors remain the governing test; applied in Utah v. Strieff."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/109304/brown-v-illinois/"
  cluster_id: 109304
  opinion_id: 109304
  identity_checked: true
homes:
  - page: "[[Fruits & Attenuation]]"
    role: "Key — Progeny / Refinement"
related: ["[[Wong Sun v. United States]]", "[[Utah v. Strieff]]", "[[Dunaway v. New York]]"]
aliases: []
tags: ["case", "fourth-amendment", "exclusionary-rule", "attenuation", "fruit-of-the-poisonous-tree"]
holding: "Sets out the attenuation factors: temporal proximity, intervening circumstances, and the purpose and flagrancy of the official…"
lake:
  record_id: Brown v. Illinois
  status: verified
  projected_at: 2026-07-06
---

# Brown v. Illinois

*422 U.S. 590 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Officers arrested Brown without probable cause or a warrant, broke into and waited in his apartment, then took him to the station, gave [[Miranda and Custodial Interrogation|Miranda warnings]], and obtained two inculpatory statements within about two hours. The Illinois courts treated the [[Miranda and Custodial Interrogation|Miranda warnings]] as automatically dissipating the taint of the unlawful arrest.

## Issue
Whether [[Miranda and Custodial Interrogation|Miranda warnings]], by themselves, break the causal chain between an illegal arrest and a subsequent confession so as to make the confession admissible under the Fourth Amendment.

## Rule
[[Miranda and Custodial Interrogation|Miranda warnings]] do not automatically purge the taint: "The Miranda warnings are an important factor, to be sure, in determining whether the confession is obtained by exploitation of an illegal arrest. But they are not the only factor to be considered." — 422 U.S. at 603. ^pin-603

Voluntariness aside, [[Fruits and Attenuation|attenuation]] turns on a multi-factor inquiry: "The temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct . . . are all relevant." — *Id.* at 603-604. ^pin-604

## Application
Brown's first statement came less than two hours after the illegal arrest, with no significant intervening event, and the arrest had a purposeful, investigatory quality. Weighing those factors, the State failed to show the statements were sufficiently attenuated from the unlawful arrest, so the [[Miranda and Custodial Interrogation|Miranda warnings]] alone did not make them admissible.

## Conclusion
[[Miranda and Custodial Interrogation|Miranda warnings]] do not [[Common Legal Terms#per-se|per se]] purge the taint of an illegal arrest; the statements should have been suppressed, and the judgment was reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The *Brown* [[Fruits and Attenuation|attenuation]] factors remain the governing framework and were applied in [[Utah v. Strieff]].

## Appears on
- [[The Exclusionary Rule]] — *Key — Progeny / Refinement*

## Sources
- *Brown v. Illinois*, 422 U.S. 590 (1975) — https://www.courtlistener.com/opinion/109304/brown-v-illinois/ — pinpoints: 603, 604.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "db944fdab5eb8efd", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brown v. Illinois"}, "payload": {"all": [{"cite": "422 U.S. 590", "page": "590", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "422"}, {"cite": "95 S. Ct. 2254", "page": "2254", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "95"}, {"cite": "45 L. Ed. 2d 416", "page": "416", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "45"}, {"cite": "1975 U.S. LEXIS 82", "page": "82", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1975"}], "display": "422 U.S. 590", "official": {"cite": "422 U.S. 590", "page": "590", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "422"}, "official_selection_present": true, "record_id": "Brown v. Illinois"}}
{"assertion_id": "168045fad14316c5", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-603", "record_id": "Brown v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-603", "pinpoint_status": "slip-only", "quote": "--- # Brown v. Illinois *422 U.S. 590 (1975)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Brown without probable cause or a warrant, broke into and waited in his apartment, then took him to the station, gave Miranda warnings, and obtained two inculpatory statements within about two hours. The Illinois courts treated the Miranda warnings as automatically dissipating the taint of the unlawful arrest. ## Issue Whether Miranda warnings, by themselves, break the causal chain between an illegal arrest and a subsequent confession so as to make the confession admissible under the Fourth Amendment. ## Rule Miranda warnings do not automatically purge the taint:", "quote_fidelity": "mismatch", "record_id": "Brown v. Illinois", "star_marker": null}}
{"assertion_id": "5e06a79f6a6fae29", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-604", "record_id": "Brown v. Illinois"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-604", "pinpoint_status": "slip-only", "quote": "The temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct . . . are all relevant.", "quote_fidelity": "mismatch", "record_id": "Brown v. Illinois", "star_marker": null}}
{"assertion_id": "cefedacfdb71c68f", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brown v. Illinois"}, "payload": {"as_of_content": "1975-06-26", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brown v. Illinois", "scope_note": "Attenuation factors remain the governing test; applied in Utah v. Strieff.", "varies_by_point": false}}
```

### lake record — Brown v. Illinois

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brown v. Illinois",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Brown v. Illinois",
    "case_name_short": "Brown",
    "case_name_full": "Brown v. Illinois",
    "input_case_name": "Brown v. Illinois",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1975-06-26",
    "year": 1975,
    "docket": "73-6650",
    "cluster_id": 109304,
    "lead_opinion_id": 109304,
    "sibling_ids": [
      109304,
      9426178,
      9426179,
      9426180
    ],
    "absolute_url": "/opinion/109304/brown-v-illinois/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "422 U.S. 590",
      "volume": "422",
      "reporter": "U.S.",
      "page": "590",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "95 S. Ct. 2254",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "2254",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 L. Ed. 2d 416",
        "volume": "45",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1975 U.S. LEXIS 82",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "422 U.S. 590",
        "volume": "422",
        "reporter": "U.S.",
        "page": "590",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "95 S. Ct. 2254",
        "volume": "95",
        "reporter": "S. Ct.",
        "page": "2254",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "45 L. Ed. 2d 416",
        "volume": "45",
        "reporter": "L. Ed. 2d",
        "page": "416",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1975 U.S. LEXIS 82",
        "volume": "1975",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "422 U.S. 590",
    "official_selection": {
      "court_class": "scotus",
      "selected": "422 U.S. 590",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-603",
      "page": null,
      "quote": "--- # Brown v. Illinois *422 U.S. 590 (1975)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Officers arrested Brown without probable cause or a warrant, broke into and waited in his apartment, then took him to the station, gave Miranda warnings, and obtained two inculpatory statements within about two hours. The Illinois courts treated the Miranda warnings as automatically dissipating the taint of the unlawful arrest. ## Issue Whether Miranda warnings, by themselves, break the causal chain between an illegal arrest and a subsequent confession so as to make the confession admissible under the Fourth Amendment. ## Rule Miranda warnings do not automatically purge the taint:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-604",
      "page": null,
      "quote": "The temporal proximity of the arrest and the confession, the presence of intervening circumstances, . . . and, particularly, the purpose and flagrancy of the official misconduct . . . are all relevant.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1975-06-26",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brown v. Illinois",
    "varies_by_point": false,
    "scope_note": "Attenuation factors remain the governing test; applied in Utah v. Strieff.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Rogers",
          "cluster_id": 10705828,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Privette",
          "cluster_id": 9387170,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4643309,
          "cite": [
            "445 P.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Fredericq",
          "cluster_id": 4613398,
          "cite": [
            "121 N.E.3d 166",
            "482 Mass. 70"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Serrano-Acevedo",
          "cluster_id": 4506969,
          "cite": [
            "892 F.3d 454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Muldrow",
          "cluster_id": 4448772,
          "cite": [
            "2017 Ohio 8839",
            "100 N.E.3d 1093"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Turpin",
          "cluster_id": 4423584,
          "cite": [
            "2017 Ohio 7435",
            "96 N.E.3d 1171"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Matthew Elliot Cohagan",
          "cluster_id": 4421478,
          "cite": [
            "162 Idaho 717",
            "404 P.3d 659"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane1_negative"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wallace v. Kato",
          "cluster_id": 145756,
          "cite": [
            "127 S. Ct. 1091",
            "549 U.S. 384"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Herring v. United States",
          "cluster_id": 145922,
          "cite": [
            "172 L. Ed. 2d 496",
            "129 S. Ct. 695",
            "555 U.S. 135",
            "2009 U.S. LEXIS 581"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dowthitt v. State",
          "cluster_id": 1777832,
          "cite": [
            "931 S.W.2d 244",
            "1996 Tex. Crim. App. LEXIS 93",
            "1996 WL 347772"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Johnson",
          "cluster_id": 110754,
          "cite": [
            "73 L. Ed. 2d 202",
            "102 S. Ct. 2579",
            "457 U.S. 537",
            "1982 U.S. LEXIS 134",
            "50 U.S.L.W. 4742"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
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
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Edmunds",
          "cluster_id": 2316698,
          "cite": [
            "586 A.2d 887",
            "526 Pa. 374",
            "1991 Pa. LEXIS 28"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Illinois:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDk1NjcwNDAwMDAwJnM9NDM5NTYxMSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28109304+OR+9426178+OR+9426179+OR+9426180%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 8,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 9,
        "triage_snippet_classified": 191
      },
      "lane2_top_cited": {
        "query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODAmcz02MDY2ODkmdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28109304+OR+9426178+OR+9426179+OR+9426180%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180)",
        "reviewed": 52,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 52,
        "triage_read": 1,
        "triage_snippet_classified": 51
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(109304 OR 9426178 OR 9426179 OR 9426180)",
    "indexed_citing_opinions": 3078,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 109304,
        "count": 2757,
        "count_source": "search"
      },
      {
        "opinion_id": 9426178,
        "count": 410,
        "count_source": "search"
      },
      {
        "opinion_id": 9426179,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9426180,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 4589,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brown-v-illinois.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkxMDM1MzImcz0xMDI4NjMwNiZ0PW8mZD0yMDI2LTA3LTA0JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28109304+OR+9426178+OR+9426179+OR+9426180%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 109304,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 103259,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106107,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106285,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106515,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 106699,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 107252,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108139,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108538,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108794,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108800,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108893,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 108898,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 109063,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 109186,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 268537,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 268701,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 292479,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 297732,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 302281,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 313628,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 317292,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 109304,
        "cited_id": 2060189,
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
    "date_created": "2026-07-04T20:42:31Z",
    "date_modified": "2026-07-06T10:25:11Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:42:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:42:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:48:14Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:42:41Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brown v. Illinois

```
<div>
<center><b><span class="citation" data-id="9426178"><a href="/opinion/109304/brown-v-illinois/" aria-description="Citation for case: Brown v. Illinois">422 U.S. 590</a></span> (1975)</b></center>
<center><h1>BROWN<br>
v.<br>
ILLINOIS.</h1></center>
<center>No. 73-6650.</center>
<center><p><b>Supreme Court of United States.</b></p></center>
<center>Argued March 18, 1975.</center>
<center>Decided June 26, 1975.</center>
CERTIORARI TO THE SUPREME COURT OF ILLINOIS.
<p><span class="star-pagination">*591</span> <i>Robert P. Isaacson</i> argued the cause for petitioner <i>pro hac vice.</i> With him on the brief were <i>James J. Doherty</i> and <i>John T. Moran.</i></p>
<p><i>Jayne A. Carr,</i> Assistant Attorney General of Illinois, argued the cause for respondent. With her on the brief were <i>William J. Scott,</i> Attorney General, and <i>James B. Zagel,</i> Assistant Attorney General.<sup>[*]</sup></p>
<p>MR. JUSTICE BLACKMUN delivered the opinion of the Court.</p>
<p>This case lies at the crossroads of the Fourth and the Fifth Amendments. Petitioner was arrested without probable cause and without a warrant. He was given, in full, the warnings prescribed by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966). Thereafter, while in custody, he made two inculpatory statements. The issue is whether evidence of those statements was properly admitted, or should have been excluded, in petitioner's subsequent trial for murder in state court. Expressed another way, the issue is whether the statements were to be excluded <span class="star-pagination">*592</span> as the fruit of the illegal arrest, or were admissible because the giving of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings sufficiently attenuated the taint of the arrest. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963). The Fourth Amendment, of course, has been held to be applicable to the States through the Fourteenth Amendment. <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S. 643</a></span> (1961).</p>
<p></p>
<h2>I</h2>
<p>As petitioner Richard Brown was climbing the last of the stairs leading to the rear entrance of his Chicago apartment in the early evening of May 13, 1968, he happened to glance at the window near the door. He saw, pointed at him through the window, a revolver held by a stranger who was inside the apartment. The man said: "Don't move, you are under arrest." App. 42. Another man, also with a gun, came up behind Brown and repeated the statement that he was under arrest. It was about 7:45 p. m. The two men turned out to be Detectives William Nolan and William Lenz of the Chicago police force. It is not clear from the record exactly when they advised Brown of their identity, but it is not disputed that they broke into his apartment, searched it, and then arrested Brown, all without probable cause and without any warrant, when he arrived. They later testified that they made the arrest for the purpose of questioning Brown as part of their investigation of the murder of a man named Roger Corpus.</p>
<p>Corpus was murdered one week earlier, on May 6, with a .38-caliber revolver in his Chicago West Side second-floor apartment. Shortly thereafter, Detective Lenz obtained petitioner's name, among others, from Corpus' brother. Petitioner and the others were identified as acquaintances of the victim, not as suspects.<sup>[1]</sup></p>
<p><span class="star-pagination">*593</span> On the day of petitioner's arrest. Detectives Lenz and Nolan, armed with a photograph of Brown, and another officer arrived at petitioner's apartment about 5 p. m. App. 77, 78. While the third officer covered the front entrance downstairs, the two detectives broke into Brown's apartment and searched it. <i>Id.,</i> at 86. Lenz then positioned himself near the rear door and watched through the adjacent window which opened onto the back porch. Nolan sat near the front door. He described the situation at the later suppression hearing:</p>
<blockquote>"After we were there for a while, Detective Lenz told me that somebody was coming up the back stairs. I walked out the front door through the hall and around the corner, and I stayed there behind a door leading on to the back porch. At this time I heard Detective Lenz say, `Don't move, you are under arrest.' I looked out. I saw Mr. Brown backing away from the window. I walked up behind him, I told him he is under arrest, come back inside the apartment with us." <i>Id.,</i> at 42.</blockquote>
<p>As both officers held him at gunpoint, the three entered the apartment. Brown was ordered to stand against the wall and was searched. No weapon was found. <i>Id.,</i> at 93. He was asked his name. When he denied being Richard Brown, Detective Lenz showed him the photograph, informed him that he was under arrest for the murder of Roger Corpus, <i>id.,</i> at 16, handcuffed him, <i>id.,</i> at 93, and escorted him to the squad car.</p>
<p>The two detectives took petitioner to the Maxwell Street police station. During the 20-minute drive Nolan again asked Brown, who then was sitting with him in the back seat of the car, whether his name was Richard Brown and whether he owned a 1966 Oldsmobile. Brown <span class="star-pagination">*594</span> alternately evaded these questions or answered them falsely. Tr. 74. Upon arrival at the station house Brown was placed in the second-floor central interrogation room. The room was bare, except for a table and four chairs. He was left alone, apparently without handcuffs, for some minutes while the officers obtained the file on the Corpus homicide. They returned with the file, sat down at the table, one across from Brown and the other to his left, and spread the file on the table in front of him. App. 19.</p>
<p>The officers warned Brown of his rights under <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i><sup>[2]</sup><i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Ibid.</a></span></i> They then informed him that they knew of an incident that had occurred in a poolroom on May 5, when Brown, angry at having been cheated at dice, fired a shot from a revolver into the ceiling. Brown answered: "Oh, you know about that." <i>Id.,</i> at 20. Lenz informed him that a bullet had been obtained from the ceiling of the poolroom and had been taken to the crime laboratory to be compared with bullets taken from Corpus' body.<sup>[3]</sup><i>Ibid.</i> Brown responded: "Oh, you know that, too." <i>Id.,</i> at 20-21. At this pointit was about 8:45 p. m.Lenz asked Brown whether he wanted to talk about the Corpus homicide. Petitioner answered that he did. For the next 20 to 25 minutes Brown answered questions put to him by Nolan, as Lenz typed. <i>Id.,</i> at 21-23.</p>
<p>This questioning produced a two-page statement in which Brown acknowledged that he and a man named <span class="star-pagination">*595</span> Jimmy Claggett visited Corpus on the evening of May 5; that the three for some time sat drinking and smoking marihuana; that Claggett ordered him at gunpoint to bind Corpus' hands and feet with cord from the headphone of a stereo set; and that Claggett, using a .38-caliber revolver sold to him by Brown, shot Corpus three times through a pillow. The statement was signed by Brown. <i>Id.,</i> at 9, 38.</p>
<p>About 9:30 p. m. the two detectives and Brown left the station house to look for Claggett in an area of Chicago Brown knew him to frequent. They made a tour of that area but did not locate their quarry. They then went to police headquarters where they endeavored, without success, to obtain a photograph of Claggett. They resumed their searchit was now about 11 p. m.and they finally observed Claggett crossing at an intersection. Lenz and Nolan arrested him. All four, the two detectives and the two arrested men, returned to the Maxwell Street station about 12:15 a. m. <i>Id.,</i> at 39.</p>
<p>Brown was again placed in the interrogation room. He was given coffee and was left alone, for the most part, until 2 a. m. when Assistant State's Attorney Crilly arrived.</p>
<p>Crilly, too, informed Brown of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. After a half hour's conversation, a court reporter appeared. Once again the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given: "I read him the card." <i>Id.,</i> at 30. Crilly told him that he "was sure he would be charged with murder." <i>Id.,</i> at 32. Brown gave a second statement, providing a factual account of the murder substantially in accord with his first statement, but containing factual inaccuracies with respect to his personal background.<sup>[4]</sup> When the statement <span class="star-pagination">*596</span> was completed, at about 3 a. m., Brown refused to sign it. <i>Id.,</i> at 57. An hour later he made a phone call to his mother. At 9:30 that morning, about 14 hours after his arrest, he was taken before a magistrate.</p>
<p>On June 20 Brown and Claggett were jointly indicted by a Cook County grand jury for Corpus' murder. Prior to trial, petitioner moved to suppress the two statements he had made. He alleged that his arrest and detention had been illegal and that the statements were taken from him in violation of his constitutional rights. After a hearing, the motion was denied. R. 46.</p>
<p>The case proceeded to trial. The State introduced evidence of both statements. Detective Nolan testified as to the contents of the first, App. 89-92, but the writing itself was not placed in evidence. The second statement was introduced and was read to the jury in full. Tr. 509-528. Brown was 23 at the time of the trial. <i>Id.,</i> at 543.</p>
<p>The jury found petitioner guilty of murder. R. 80., He was sentenced to imprisonment for not less than 15 years nor more than 30 years. <i>Id.,</i> at 83.</p>
<p>On appeal, the Supreme Court of Illinois affirmed the judgment of conviction. <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/" aria-description="Citation for case: People v. Brown">56 Ill. 2d 312</a></span>, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/" aria-description="Citation for case: People v. Brown">307 N. E. 2d 356</a></span> (1974). The court refused to accept the State's argument that Brown's arrest was lawful. "Upon review of the record, we conclude that the testimony fails to show that at the time of his apprehension there was probable cause for defendant's arrest, [and] that his arrest was, therefore, unlawful." <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#315" aria-description="Citation for case: People v. Brown"><i>Id.,</i> at 315</a></span>, 307 N. E. <span class="star-pagination">*597</span> 2d, at 357. But it went on to hold in two significant and unembellished sentences:</p>
<blockquote>"[W]e conclude that the giving of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, in the first instance by the police officer and in the second by the assistant State's Attorney, served to break the causal connection between the illegal arrest and the giving of the statements, and that defendant's act in making the statements was `sufficiently an act of free will to purge the primary taint of the unlawful invasion.' (<i>Wong Sun v. United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471, at 486</a></span>.) We hold, therefore, that the circuit court did not err in admitting the statements into evidence." <i>Id.,</i> at 317, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#358" aria-description="Citation for case: People v. Brown">307 N. E. 2d, at 358</a></span>.</blockquote>
<p>Aside from its reliance upon the presence of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, no specific aspect of the record or of the circumstances was cited by the court in support of its conclusion. The court, in other words, appears to have held that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in and of themselves broke the causal chain so that any subsequent statement, even one induced by the continuing effects of unconstitutional custody, was admissible so long as, in the traditional sense, it was voluntary and not coerced in violation of the Fifth and Fourteenth Amendments.</p>
<p>Because of our concern about the implication of our holding in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), to the facts of Brown's case, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./419/894/">419 U. S. 894</a></span> (1974).</p>
<p></p>
<h2>II</h2>
<p>In <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> the Court pronounced the principles to be applied where the issue is whether statements and other evidence obtained after an illegal arrest or search should be excluded. In that case, federal agents elicited an oral statement from defendant Toy after forcing entry <span class="star-pagination">*598</span> at 6 a. m. into his laundry, at the back of which he had his living quarters. The agents had followed Toy down the hall to the bedroom and there had placed him under arrest. The Court of Appeals found that there was no probable cause for the arrest. This Court concluded that finding was "amply justified by the facts clearly shown on this record." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#479" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 479</a></span>. Toy's statement, which bore upon his participation in the sale of narcotics, led the agents to question another person, Johnny Yee, who actually possessed narcotics. Yee stated that heroin had been brought to him earlier by Toy and another Chinese known to him only as "Sea Dog." Under questioning, Toy said that "Sea Dog" was Wong Sun. Toy led agents to a multifamily dwelling where, he said, Wong Sun lived. Gaining admittance to the building through a bell and buzzer, the agents climbed the stairs and entered the apartment. One went into the back room and brought Wong Sun out in hand-cuffs. After arraignment, Wong Sun was released on his own recognizance. Several days later, he returned voluntarily to give an unsigned confession.</p>
<p>This Court ruled that Toy's declarations and the contraband taken from Yee were the fruits of the agents' illegal action and should not have been admitted as evidence against Toy. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#484" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 484-488</a></span>. It held that the statement did not result from " `an intervening independent act of a free will,' " and that it was not "sufficiently an act of free will to purge the primary taint of the unlawful invasion." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 486</a></span>. With respect to Wong Sun's confession, however, the Court held that in the light of his lawful arraignment and release on his own recognizance, and of his return voluntarily several days later to make the statement, the connection between his unlawful arrest and the statement "had `become so attenuated as to dissipate the taint.' <i>Nardone</i> v. <i>United</i> <span class="star-pagination">*599</span> <i>States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#341" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 341</a></span>." <i>Id.,</i> at 491. The Court said:</p>
<blockquote>"We need not hold that all evidence is `fruit of the poisonous tree' simply because it would not have come to light but for the illegal actions of the police. Rather, the more apt question in such a case is `whether, granting establishment of the primary illegality, the evidence to which instant objection is made has been come at by exploitation of that illegality or instead by means sufficiently distinguishable to be purged of the primary taint'. Maguire, Evidence of Guilt, 221 (1959)." <i>Id.,</i> at 487-488.</blockquote>
<p>The exclusionary rule thus was applied in <i>Wong Sun primarily</i> to protect Fourth Amendment rights. Protection of the Fifth Amendment right against self-incrimination was not the Court's paramount concern there. To the extent that the question whether Toy's statement was voluntary was considered, it was only to judge whether it "was <i>sufficiently</i> an act of free will to purge the primary taint of the unlawful invasion." <i>Id.,</i> at 486 (emphasis added).</p>
<p>The Court in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> as is customary, emphasized that application of the exclusionary rule on Toy's behalf protected Fourth Amendment guarantees in two respects: "in terms of deterring lawless conduct by federal officers," and by "closing the doors of the federal courts to any use of evidence unconstitutionally obtained." <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Ibid.</a></span></i> These considerations of deterrence and of judicial integrity, by now, have become rather commonplace in the Court's cases. See <i>e. g., United States</i> v. <i>Peltier, ante,</i> at 535-538; <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347</a></span> (1974); <i>Terry</i> v. <i>Ohio,</i> <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#12" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 12-13, 28-29</a></span> (1968). "The rule is calculated to prevent, not to repair. Its purpose is to deterto compel respect for the <span class="star-pagination">*600</span> constitutional guaranty in the only effectively available wayby removing the incentive to disregard it." <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#217" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 217</a></span> (1960). But "[d]espite its broad deterrent purpose, the exclusionary rule has never been interpreted to proscribe the use of illegally seized evidence in all proceedings or against all persons." <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#348" aria-description="Citation for case: United States v. Calandra">414 U. S., at 348</a></span>. See also <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/#446" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433, 446-447</a></span> (1974).<sup>[5]</sup></p>
<p></p>
<h2>III</h2>
<p>The Illinois courts refrained from resolving the question, as apt here as it was in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> whether Brown's statements were obtained by exploitation of the illegality of his arrest. They assumed that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, by themselves, assured that the statements (verbal acts, as contrasted with physical evidence) were of sufficient free will as to purge the primary taint of the unlawful arrest. <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>,</i> of course, preceded <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span>.</i></p>
<p>This Court has described the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings as a "prophylactic rule", <i>Michigan</i> v. <i>Payne,</i> <span class="citation" data-id="8985601"><a href="/opinion/8993355/michigan-v-payne/#53" aria-description="Citation for case: Michigan v. Payne">412 U. S. 47, 53</a></span> (1973), and as a "procedural safeguard," <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#457" aria-description="Citation for case: Miranda v. Arizona">384 U. S., at 457, 478</a></span>, employed to protect Fifth Amendment rights against "the compulsion inherent in custodial surroundings." <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#458" aria-description="Citation for case: Miranda v. Arizona"><i>Id.,</i> at 458</a></span>. The function of the warnings relates to the Fifth Amendment's guarantee against coerced self-incrimination, and the exclusion <span class="star-pagination">*601</span> of a statement made in the absence of the warnings, it is said, serves to deter the taking of an incriminating statement without first informing the individual of his Fifth Amendment rights.</p>
<p>Although, almost 90 years ago, the Court observed that the Fifth Amendment is in "intimate relation" with the Fourth, <i>Boyd</i> v. <i>United States,</i> <span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#633" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 633</a></span> (1886), the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings thus far have not been regarded as a means either of remedying or deterring violations of Fourth Amendment rights. Frequently, as here, rights under the two Amendments may appear to coalesce since "the `unreasonable searches and seizures' condemned in the Fourth Amendment are almost always made for the purpose of compelling a man to give evidence against himself, which in criminal cases is condemned in the Fifth Amendment." <i>Ibid.;</i> see <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 646</a></span> n. 5. The exclusionary rule, however, when utilized to effectuate the Fourth Amendment, serves interests and policies that are distinct from those it serves under the Fifth. It is directed at all unlawful searches and seizures, and not merely those that happen to produce incriminating material or testimony as fruits. In short, exclusion of a confession made without <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings might be regarded as necessary to effectuate the Fifth Amendment, but it would not be sufficient fully to protect the Fourth. <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, and the exclusion of a confession made without them, do not alone sufficiently deter a Fourth Amendment violation.<sup>[6]</sup></p>
<p>Thus, even if the statements in this case were found to be voluntary under the Fifth Amendment, the Fourth <span class="star-pagination">*602</span> Amendment issue remains. In order for the causal chain, between the illegal arrest and the statements made subsequent thereto, to be broken, <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> requires not merely that the statement meet the Fifth Amendment standard of voluntariness but that it be "sufficiently an act of free will to purge the primary taint." <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#486" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 486</a></span>. <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> thus mandates consideration of a statement's admissibility in light of the distinct policies and interests of the Fourth Amendment.</p>
<p>If <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, by themselves, were held to attenuate the taint of an unconstitutional arrest, regardless of how wanton and purposeful the Fourth Amendment violation, the effect of the exclusionary rule would be substantially diluted. See <i>Davis</i> v. <i>Mississippi,</i> <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/#726" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721, 726-727</a></span> (1969). Arrests made without warrant or without probable cause, for questioning or "investigation," would be encouraged by the knowledge that evidence derived therefrom could well be made admissible at trial by the simple expedient of giving <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings.<sup>[7]</sup> Any incentive to avoid Fourth Amendment violations would be eviscerated by making the warnings, in effect, a "cure-all," and the constitutional guarantee against unlawful searches and seizures could <span class="star-pagination">*603</span> be said to be reduced to "a form of words". See <i>Mapp</i> v. <i>Ohio,</i> <span class="citation" data-id="9422279"><a href="/opinion/106285/mapp-v-ohio/#648" aria-description="Citation for case: Mapp v. Ohio">367 U. S., at 648</a></span>.</p>
<p>It is entirely possible, of course, as the State here argues, that persons arrested illegally frequently may decide to confess as an act of free will unaffected by the initial illegality. But the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, <i>alone</i> and <i>per se,</i> cannot always make the act sufficiently a product of free will to break, for Fourth Amendment purposes, the causal connection between the illegality and the confession. They cannot assure in every case that the Fourth Amendment violation has not been unduly exploited. See <i>Westover</i> v. <i>United States,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/#496" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436, 496-497</a></span> (1966).</p>
<p>While we therefore reject the <i>per se</i> rule which the Illinois courts appear to have accepted, we also decline to adopt any alternative <i>per se</i> or "but for" rule. The petitioner himself professes not to demand so much. Tr. of Oral Arg. 12, 45, 47. The question whether a confession is the product of a free will under <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> must be answered on the facts of each case. No single fact is dispositive. The workings of the human mind are too complex, and the possibilities of misconduct too diverse, to permit protection of the Fourth Amendment to turn on such a talismanic test. The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings are an important factor, to be sure, in determining whether the confession is obtained by exploitation of an illegal arrest. But they are not the only factor to be considered. The temporal proximity of the arrest and the confession,<sup>[8]</sup> the presence of intervening circumstances, <span class="star-pagination">*604</span> see <i>Johnson</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424879"><a href="/opinion/108538/johnson-v-louisiana/#365" aria-description="Citation for case: Johnson v. Louisiana">406 U. S. 356, 365</a></span> (1972), and, particularly, the purpose and flagrancy of the official misconduct<sup>[9]</sup> are all relevant. See <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491</a></span>. The voluntariness of the statement is a threshold requirement. Cf. <span class="citation no-link">18 U. S. C. § 3501</span>. And the burden of showing admissibility rests, of course, on the prosecution.<sup>[10]</sup></p>
<p></p>
<h2>IV</h2>
<p>Although the Illinois courts failed to undertake the inquiry mandated by <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> to evaluate the circumstances of this case in the light of the policy served by the exclusionary rule, the trial resulted in a record of amply sufficient detail and depth from which the determination may be made. We therefore decline the suggestion of the United States, as <i>amicus curiae,</i> see <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/" aria-description="Citation for case: Morales v. New York">396 U. S. 102</a></span> (1969), to remand the case for further factual findings. We conclude that the State failed to sustain the burden of showing that the evidence in question was admissible under <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i></p>
<p>Brown's first statement was separated from his illegal arrest by less than two hours, and there was no intervening event of significance whatsoever. In its essentials, his situation is remarkably like that of James Wah Toy in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i><sup>[11]</sup> We could hold Brown's first statement <span class="star-pagination">*605</span> admissible only if we overrule <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i> We decline to do so. And the second statement was clearly the result and the fruit of the first.<sup>[12]</sup></p>
<p>The illegality here, moreover, had a quality of purposefulness. The impropriety of the arrest was obvious; awareness of that fact was virtually conceded by the two detectives when they repeatedly acknowledged, in their testimony, that the purpose of their action was "for investigation" or for "questioning."<sup>[13]</sup> App. 35, 43, 78, 81, 83, 88, 89, 94. The arrest, both in design and in execution, was investigatory. The detectives embarked upon this expedition for evidence in the hope that something might turn up. The manner in which Brown's arrest was effected gives the appearance of having been calculated to cause surprise, fright, and confusion.</p>
<p>We emphasize that our holding is a limited one. We decide only that the Illinois courts were in error in assuming that the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings, by themselves, under <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> always purge the taint of an illegal arrest.</p>
<p>The judgment of the Supreme Court of Illinois is reversed and the case is remanded for further proceedings not inconsistent with this opinion.</p>
<p><i>It is so ordered.</i></p>
<p><span class="star-pagination">*606</span> MR. JUSTICE WHITE, concurring in the judgment.</p>
<p>Insofar as the Court holds (1) that despite <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings the Fourth and Fourteenth Amendments require the exclusion from evidence of statements obtained as the fruit of an arrest which the arresting officers knew or should have known was without probable cause and unconstitutional, and (2) that the statements obtained in this case were in this category, I am in agreement and therefore concur in the judgment.</p>
<p>MR. JUSTICE POWELL, with whom MR. JUSTICE REHNQUIST joins, concurring in part.</p>
<p>I join the Court insofar as it holds that the <i>per se</i> rule adopted by the Illinois Supreme Court for determining the admissibility of petitioner's two statements inadequately accommodates the diverse interests underlying the Fourth Amendment exclusionary rule. I would, however, remand the case for reconsideration under the general standards articulated in the Court's opinion and elaborated herein.</p>
<p></p>
<h2>A</h2>
<p>The issue presented in this case turns on proper application of the policies underlying the Fourth Amendment exclusionary rule, not on the Fifth Amendment or the prophylaxis added to that guarantee by <i>Miranda</i> v. <i>Arizona,</i> <span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">384 U. S. 436</a></span> (1966).<sup>[1]</sup> The Court recognized in <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963), that the Fourth Amendment exclusionary rule applies to statements obtained following an illegal arrest just as it does to tangible evidence seized in a similar manner <span class="star-pagination">*607</span> or obtained pursuant to an otherwise illegal search and seizure. <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> squarely rejected, however, the suggestion that the admissibility of statements so obtained should be governed by a simple "but for" test that would render inadmissible all statements given subsequent to an illegal arrest. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#487" aria-description="Citation for case: Wong Sun v. United States"><i>Id.,</i> at 487-488</a></span>. In a similar manner, the Court today refrains from according dispositive weight to the single factor of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. I agree with each holding. Neither of the rejected extremes adequately recognizes the competing considerations involved in a determination to exclude evidence after finding that official possession of that evidence was to some degree caused by a violation of the Fourth Amendment.</p>
<p>On this record, I cannot conclude as readily as the Court that admission of the statements here at issue would constitute an effective overruling of <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span>.</i> See <i>ante,</i> at 604-605. Although <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> establishes the boundaries within which this case must be decided, the incompleteness of the record leaves me uncertain that it compels the exclusion of petitioner's statements. The statements at issue in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> were on the temporal extremes in relation to the illegal arrest. Cf. <i>Collins</i> v. <i>Beto,</i> <span class="citation" data-id="9450950"><a href="/opinion/268701/clarence-collins-v-george-j-beto-director-texas-department-of/#832" aria-description="Citation for case: Clarence Collins v. George J. Beto, Director, Texas...">348 F. 2d 823, 832, 834-836</a></span> (CA5 1965) (Friendly, J., concurring). Toy's statement was obtained immediately after his pursuit and arrest by six agents. It appears to have been a spontaneous response to a question put to him in the frenzy of that event, and there is no indication that the agents made any attempt to inform him of his right to remain silent. Wong Sun's statement, by contrast, was not given until after he was arraigned and released on his own recognizance. Wong Sun voluntarily returned to the station a few days after the arrest for questioning. His statement was preceded by an official warning of his right <span class="star-pagination">*608</span> to remain silent and to have counsel if he desired.<sup>[2]</sup> The Court rejected the Government's assertion that Toy's statement resulted from an independent act of free will sufficient to purge the consequences of the illegal arrest. Wong Sun's statement, however, was deemed admissible. Given the circumstances in which Wong Sun's statement was obtained, the Court concluded that "the connection between the arrest and the statement had `become so attenuated as to dissipate the taint.' " <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491</a></span>.</p>
<p>Like most cases in which the admissibility of statements obtained subsequent to an illegal arrest is contested, this case concerns statements more removed than that of Toy from the time and circumstances of the illegal arrest. Petitioner made his first statement some two hours following his arrest, after he had been given <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings. The Court is correct in noting that no other significant intervening event altered the relationship established between petitioner and the officers by the illegal arrest. But the Court's conclusion that admission of this statement could be allowed only by overruling <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> rests either on an overly restrictive interpretation of the attenuation doctrine, to which I cannot subscribe, or on its view that the arrest was made for investigatory purposes, a factual determination that I think more appropriately should have been left for decision in the first instance by the state courts.</p>
<p></p>
<h2>B</h2>
<p>The Court's rejection in <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> of a "but for" test, reaffirmed today, <i>ante,</i> at 603-604, recognizes that in some <span class="star-pagination">*609</span> circumstances strict adherence to the Fourth Amendment exclusionary rule imposes greater cost on the legitimate demands of law enforcement than can be justified by the rule's deterrent purposes. The notion of the "dissipation of the taint" attempts to mark the point at which the detrimental consequences of illegal police action become so attenuated that the deterrent effect of the exclusionary rule no longer justifies its cost. Application of the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> doctrine will generate fact-specific cases bearing distinct differences as well as similarities, and the question of attenuation inevitably is largely a matter of degree. The Court today identifies the general factors that the trial court must consider in making this determination. I think it appropriate, however, to attempt to articulate the possible relationships of those factors in particular, broad categories of cases.</p>
<p>All Fourth Amendment violations are, by constitutional definition, "unreasonable." There are, however, significant practical differences that distinguish among violations, differences that measurably assist in identifying the kinds of cases in which disqualifying the evidence is likely to serve the deterrent purposes of the exclusionary rule. Cf. <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/#347" aria-description="Citation for case: United States v. Calandra">414 U. S. 338, 347-348</a></span> (1974); <i>Schneckloth</i> v. <i>Bustamonte,</i> <span class="citation" data-id="9425314"><a href="/opinion/108800/schneckloth-v-bustamonte/#250" aria-description="Citation for case: Schneckloth v. Bustamonte">412 U. S. 218, 250</a></span> (1973) (POWELL, J., concurring). In my view, the point at which the taint can be said to have dissipated should be related, in the absence of other controlling circumstances, to the nature of that taint.</p>
<p>That police have not succeeded in coercing the accused's confession through willful or negligent misuse of the power of arrest does not remove the fact that they may have tried. The impermissibility of the attempt, and the extent to which such attempts can be deterred by the use of the exclusionary rule, are of primary relevance in determining whether exclusion is an appropriate remedy. <span class="star-pagination">*610</span> The basic purpose of the rule, briefly stated, is to remove possible motivations for illegal arrests. Given this purpose the notion of voluntariness has practical value in deciding whether the rule should apply to statements removed from the immediate circumstances of the illegal arrest. If an illegal arrest merely provides the occasion of initial contact between the police and the accused, and because of time or other intervening factors the accused's eventual statement is the product of his own reflection and free will, application of the exclusionary rule can serve little purpose: the police normally will not make an illegal arrest in the hope of eventually obtaining such a truly volunteered statement. In a similar manner, the role of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> inquiry is indirect. To the extent that they dissipate the psychological pressures of custodial interrogation, <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings serve to assure that the accused's decision to make a statement has been relatively unaffected by the preceding illegal arrest. Correspondingly, to the extent that the police perceive <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings to have this equalizing potential, their motivation to abuse the power of arrest is diminished. Bearing these considerations in mind, and recognizing that the deterrent value of the Fourth Amendment exclusionary rule is limited to certain kinds of police conduct, the following general categories can be identified.</p>
<p>Those most readily identifiable are on the extremes: the flagrantly abusive violation of Fourth Amendment rights, on the one hand, and "technical" Fourth Amendment violations, on the other. In my view, these extremes call for significantly different judicial responses.</p>
<p>I would require the clearest indication of attenuation in cases in which official conduct was flagrantly abusive of Fourth Amendment rights. If, for example, the factors <span class="star-pagination">*611</span> relied on by the police in determining to make the arrest were so lacking in indicia of probable cause as to render official belief in its existence entirely unreasonable, or if the evidence clearly suggested that the arrest was effectuated as a pretext for collateral objectives, cf. <i>United States</i> v. <i>Robinson,</i> <span class="citation" data-id="9425474"><a href="/opinion/108893/united-states-v-robinson/#237" aria-description="Citation for case: United States v. Robinson">414 U. S. 218, 237</a></span>, 238 n. 2 (1973) (POWELL, J., concurring), or the physical circumstances of the arrest unnecessarily intrusive on personal privacy, I would consider the equalizing potential of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings rarely sufficient to dissipate the taint. In such cases the deterrent value of the exclusionary rule is most likely to be effective, and the corresponding mandate to preserve judicial integrity, see <i>United States</i> v. <i>Peltier, ante,</i> p. 531; <i>Michigan</i> v. <i>Tucker,</i> <span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">417 U. S. 433</a></span>, 450 n. 25 (1974), most clearly demands that the fruits of official misconduct be denied. I thus would require some demonstrably effective break in the chain of events leading from the illegal arrest to the statement, such as actual consultation with counsel or the accused's presentation before a magistrate for a determination of probable cause, before the taint can be deemed removed, see <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103</a></span> (1975); cf. <i>Johnson</i> v. <i>Louisiana,</i> <span class="citation" data-id="9424879"><a href="/opinion/108538/johnson-v-louisiana/#365" aria-description="Citation for case: Johnson v. Louisiana">406 U. S. 356, 365</a></span> (1972); <i>Parker</i> v. <i>North Carolina,</i> <span class="citation" data-id="9424258"><a href="/opinion/108139/parker-v-north-carolina/#796" aria-description="Citation for case: Parker v. North Carolina">397 U. S. 790, 796</a></span> (1970).</p>
<p>At the opposite end of the spectrum lie "technical" violations of Fourth Amendment rights where, for example, officers in good faith arrest an individual in reliance on a warrant later invalidated<sup>[3]</sup> or pursuant to a statute that subsequently is declared unconstitutional, see <i>United States</i> v. <i>Kilgen,</i> <span class="citation" data-id="297732"><a href="/opinion/297732/united-states-v-robert-h-kilgen-jr/" aria-description="Citation for case: United States v. Robert H. Kilgen, Jr.">445 F. 2d 287</a></span> (CA5 <span class="star-pagination">*612</span> 1971). As we noted in <i>Michigan</i> v. <i><span class="citation" data-id="9425753"><a href="/opinion/109063/michigan-v-tucker/" aria-description="Citation for case: Michigan v. Tucker">Tucker, supra,</a></span></i> at 447: "The deterrent purpose of the exclusionary rule necessarily assumes that the police have engaged in willful, or at the very least negligent, conduct which has deprived the defendant of some right." In cases in which this underlying premise is lacking, the deterrence rationale of the exclusionary rule does not obtain, and I can see no legitimate justification for depriving the prosecution of reliable and probative evidence. Thus, with the exception of statements given in the immediate circumstances of the illegal arresta constraint I think is imposed by existing exclusionary-rule lawI would not require more than proof that effective <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings were given and that the ensuing statement was voluntary in the Fifth Amendment sense. Absent aggravating circumstances, I would consider a statement given at the station house after one has been advised of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights to be sufficiently removed from the immediate circumstances of the illegal arrest to justify its admission at trial.</p>
<p>Between these extremes lies a wide range of situations that defy ready categorization, and I will not attempt to embellish on the factors set forth in the Court's opinion other than to emphasize that the <i><span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">Wong Sun</a></span></i> inquiry always should be conducted with the deterrent purpose of the Fourth Amendment exclusionary rule sharply in focus. See ALI Model Code of Pre-Arraignment Procedure, Art. 150, p. 54 <i>et seq.</i> and Commentary thereon, p. 375 <i>et seq.</i> (Prop. Off. Draft 1975). And, in view of the inevitably fact-specific nature of the inquiry, we must place primary reliance on the "learning, good sense, fairness and courage" of judges who must make the determination in the first instance. <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#342" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 342</a></span> (1939). See <i>ante,</i> at 604 n. 10.</p>
<p></p>
<h2>
<span class="star-pagination">*613</span> C</h2>
<p>On the facts of record as I view them, it is possible that the police may have believed reasonably that there was probable cause for petitioner's arrest. Although the trial court conducted hearings on petitioner's motion to suppress and received his testimony and that of the arresting officers, its inquiry focused on determining whether petitioner's statements were preceded by adequate <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and were made voluntarily. The court did not inquire into the possible justification, actual or perceived, for the arrest. Indeed, numerous questions addressed to the circumstances of the arrest elicited the State's objection, which was sustained. App. 14-15. The Illinois Supreme Court's consideration of the factual basis for its ruling similarly failed to focus on these relevant issues or to rest in any meaningful sense on the factors set forth in the Court's opinion today. After determining that the officers lacked probable cause for petitioner's arrest, the Illinois court concluded simply that examination of the record persuaded it that "the giving of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings . . . served to break the causal connection between the illegal arrest and the giving of the statements." <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#317" aria-description="Citation for case: People v. Brown">56 Ill. 2d 312, 317</a></span>, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#358" aria-description="Citation for case: People v. Brown">307 N. E. 2d 356, 358</a></span> (1974).</p>
<p>I am not able to conclude on this record that the officers arrested petitioner solely for the purpose of questioning, <i>ante,</i> at 605; see also <i>ante,</i> at 606 (WHITE, J., concurring in judgment). To be sure, there is evidence suggesting, as the Court notes, an investigatory arrest. The strongest evidence on that point is the inconclusive testimony by the arresting officers themselves. But the evidence is conflicting. Responding to questions as to what they told petitioner upon his arrest, the officers testified he was advised that the arrest was for investigation of murder. Responding to more pointed questions, <span class="star-pagination">*614</span> however, one of the arresting officers stated that he informed petitioner that he was being arrested for murder. See App. 16.<sup>[4]</sup></p>
<p>Moreover, other evidence of record indicates that the police may well have believed that probable cause existed to think that petitioner committed the crime of which he ultimately was convicted. As the opinion of the Illinois Supreme Court reveals, petitioner had been identified as an acquaintance of the deceased, and the police had been told that petitioner was seen in the building where the deceased lived on the day of the murder. <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#315" aria-description="Citation for case: People v. Brown">56 Ill. 2d, at 315</a></span>, <span class="citation" data-id="2060189"><a href="/opinion/2060189/people-v-brown/#357" aria-description="Citation for case: People v. Brown">307 N. E. 2d, at 357</a></span>. It is also plain that the investigation had begun to focus on petitioner. For example, the police had gone to the trouble of obtaining a bullet that petitioner had fired in an unrelated incident for the purpose of comparing it with the bullets that killed the victim. App. 20. The officers also obtained petitioner's photograph prior to seeking him out, and the circumstances of petitioner's arrest indicate that their suspicions of him were quite pronounced.</p>
<p>The trial court made no determination as to whether probable cause existed for petitioner's arrest.<sup>[5]</sup> The Illinois <span class="star-pagination">*615</span> Supreme Court resolved that issue, but did not consider whether the officers might reasonably, albeit erroneously, have thought that probable cause existed. Rather than decide those matters for the first time at this level, I think it preferable to allow the state courts to reconsider the case under the general guidelines expressed in today's opinions.<sup>[6]</sup> I therefore would remand for reconsideration<sup>[7]</sup> with directions to conduct such further factual <span class="star-pagination">*616</span> inquiries as may be necessary to resolve the admissibility issue.</p>
<h2>NOTES</h2>
<p>[*]  <i>Solicitor General Bork</i> and <i>Acting Assistant Attorney General Keeney</i> filed a memorandum for the United States as <i>amicus curiae.</i></p>
<p>[1]  The brother, however, when asked at the trial whether any of the victim's family suggested to the police that petitioner was possibly responsible for the victim's death, answered: "Nobody asked." App. 74.</p>
<p>[2]  There is no assertion here that he did not understand those rights.</p>
<p>[3]  It was stipulated at the trial that if expert testimony were taken, it would be to the effect that the bullet eventually was ascertained to be a "wiped bullet," that is, that its sides were "clean and therefore it was not ballistically comparable to any other bullets, specifically the bullets taken from the body of the deceased, Roger Corpus." Tr. 543.</p>
<p>[4]  In response to questions from Mr. Crilly, Brown stated that he was employed at E. I. Guffman Company in Niles, Ill., and that he was a punch press operator, App. 97, whereas he later conceded that he worked at Arnold Schwinn Bicycle Company and had never worked at any other place. <i>Id.,</i> at 63. He also remarked in the Crilly statement that he had completed three years of high school, <i>id.,</i> at 96, whereas later he conceded that he "never went to high school." <i>Id.,</i> at 58.</p>
<p>[5]  Members of the Court on occasion have indicated disenchantment with the rule. See, <i>e. g., </i><i>Coolidge</i> v. <i>New Hampshire,</i> <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#490" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 490</a></span> (1971) (Harlan, J., concurring); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#492" aria-description="Citation for case: Coolidge v. New Hampshire"><i>id.,</i> at 492</a></span> (BURGER, C. J., dissenting in part and concurring in part); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#493" aria-description="Citation for case: Coolidge v. New Hampshire"><i>id.,</i> at 493</a></span> (Black, J., concurring and dissenting); <span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#510" aria-description="Citation for case: Coolidge v. New Hampshire"><i>id.,</i> at 510</a></span> (WHITE, J., concurring and dissenting); <i>Bivens</i> v. <i>Six Unknown Federal Narcotics Agents,</i> <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#411" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388, 411</a></span> (1971) (BURGER, C. J., dissenting). Its efficacy has been subject to some dispute. <i>United States</i> v. <i>Calandra,</i> <span class="citation" data-id="9425486"><a href="/opinion/108898/united-states-v-calandra/" aria-description="Citation for case: United States v. Calandra">414 U. S. 338</a></span>, 348 n. 5 (1974). See <i>Elkins</i> v. <i>United States,</i> <span class="citation" data-id="9422064"><a href="/opinion/106107/elkins-v-united-states/#218" aria-description="Citation for case: Elkins v. United States">364 U. S. 206, 218</a></span> (1960).</p>
<p>[6]  The <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings in no way inform a person of his Fourth Amendment rights, including his right to be released from unlawful custody following an arrest made without a warrant or without probable cause.</p>
<p>[7]  A great majority of the commentators have taken the same position. See, <i>e. g.,</i> Pitler, "The Fruit of the Poisonous Tree" Revisited and Shepardized, <span class="citation no-link">56 Calif. L. Rev. 579</span>, 603-604 (1968); Ruffin, Out on a Limb of the Poisonous Tree: The Tainted Witness, 15 U. C. L. A. L. Rev. 32, 70 (1967); Comment, 1 Fla. St. L. Rev. 533, 539-540 (1973); Note, Admissibility of Confessions Made Subsequent to an Illegal Arrest: Wong Sun v. United States Revisited, 61 J. Crim. L. 207, 212 n. 58 (1970); Comment, Scope of Taint Under the Exclusionary Rule of the Fifth Amendment Privilege Against Self-Incrimination, <span class="citation no-link">114 U. Pa. L. Rev. 570</span>, 574 (1966). But see Comment, Voluntary Incriminating Statements Made Subsequent to an Illegal ArrestA Proposed Modification of the Exclusionary Rule, <span class="citation no-link">71 Dick. L. Rev. 573</span>, 582-583 (1967).</p>
<p>[8]  See <i>United States</i> v. <i>Owen,</i> <span class="citation" data-id="317292"><a href="/opinion/317292/united-states-v-william-e-owen-jr-frederick-morse-allen-joseph-g/#1107" aria-description="Citation for case: United States v. William E. Owen, Jr., Frederick Morse...">492 F. 2d 1100, 1107</a></span> (CA5), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./419/965/">419 U. S. 965</a></span> (1974); <i>Hale</i> v. <i>Henderson,</i> <span class="citation" data-id="9459888"><a href="/opinion/313628/albert-william-hale-v-c-murray-henderson-warden-tennessee-state/#267" aria-description="Citation for case: Albert William Hale v. C. Murray Henderson, Warden...">485 F. 2d 266, 267-269</a></span> (CA6 1973), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./415/930/">415 U. S. 930</a></span> (1974); <i>United States</i> v. <i>Fallon,</i> <span class="citation" data-id="302281"><a href="/opinion/302281/united-states-v-john-kearn-fallon/#19" aria-description="Citation for case: United States v. John Kearn Fallon">457 F. 2d 15, 19-20</a></span> (CA10 1972); <i>Leonard</i> v. <i>United States,</i> <span class="citation" data-id="279328"><a href="/opinion/279328/andrew-j-leonard-v-united-states/#538" aria-description="Citation for case: Andrew J. Leonard v. United States">391 F 2d 537, 538</a></span> (CA9 1968); <i>Pennsylvania ex rel. Craig</i> v. <i>Maroney,</i> <span class="citation" data-id="268537"><a href="/opinion/268537/commonwealth-of-pennsylvania-ex-rel-george-w-craig-v-james-f-maroney/#29" aria-description="Citation for case: Commonwealth of Pennsylvania Ex Rel. George W. Craig v....">348 F. 2d 22, 29</a></span> (CA3 1965).</p>
<p>[9]  See <i>United States</i> v. <i>Edmons,</i> <span class="citation" data-id="8883830"><a href="/opinion/8897209/united-states-v-edmons/" aria-description="Citation for case: United States v. Edmons">432 F. 2d 577</a></span> (CA2 1970). See also <i>United States ex rel. Gockley</i> v. <i>Myers,</i> <span class="citation" data-id="9457491"><a href="/opinion/299686/united-states-of-america-ex-rel-edwin-gockley-v-david-n-myers/#236" aria-description="Citation for case: United States of America Ex Rel. Edwin Gockley v. David...">450 F. 2d 232, 236</a></span> (CA3 1971), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./404/1063/">404 U. S. 1063</a></span> (1972); <i>United States</i> v. <i>Kilgen,</i> <span class="citation" data-id="297732"><a href="/opinion/297732/united-states-v-robert-h-kilgen-jr/#289" aria-description="Citation for case: United States v. Robert H. Kilgen, Jr.">445 F. 2d 287, 289</a></span> (CA5 1971).</p>
<p>[10]  Our approach relies heavily, but not excessively, on the "learning, good sense, fairness and courage of federal trial judges." <i>Nardone</i> v. <i>United States,</i> <span class="citation" data-id="103259"><a href="/opinion/103259/nardone-v-united-states/#342" aria-description="Citation for case: Nardone v. United States">308 U. S. 338, 342</a></span> (1939).</p>
<p>[11]  The situation here is thus in dramatic contrast to that of Wong Sun himself. Wong Sun's confession, which the Court held admissible, came several days after the illegality, and was preceded by a lawful arraignment and a release from custody on his own recognizance. <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#491" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 491</a></span>.</p>
<p>[12]  The fact that Brown had made one statement, believed by him to be admissible, and his cooperation with the arresting and interrogating officers in the search for Claggett, with his anticipation of leniency, bolstered the pressures for him to give the second, or at least vitiated any incentive on his part to avoid self-incrimination. Cf. <i>Fahy</i> v. <i>Connecticut,</i> <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/" aria-description="Citation for case: Fahy v. Connecticut">375 U. S. 85</a></span> (1963).</p>
<p>[13]  Detective Lenz had been a member of the Chicago police force for 14 years and a detective for 12 years. App. 6. Detective Nolan had been a detective on the force for 5 1/2 years. <span class="citation" data-id="9422676"><a href="/opinion/106699/fahy-v-connecticut/#87" aria-description="Citation for case: Fahy v. Connecticut"><i>Id.,</i> at 87</a></span>.</p>
<p>[1]  Each of these guarantees provides an independent ground for suppression of statements and thus may make it unnecessary in many cases to conduct the inquiry mandated by <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/" aria-description="Citation for case: Wong Sun v. United States">371 U. S. 471</a></span> (1963).</p>
<p>[2]  Toy gave a second statement under circumstances similar to those in Wong Sun's case. The Court did not, however, rule as to the admissibility of this statement, finding instead that it lacked corroboration and was therefore insufficient to support Toy's conviction. <i>Wong Sun</i> v. <i>United States,</i> <span class="citation" data-id="9422515"><a href="/opinion/106515/wong-sun-v-united-states/#488" aria-description="Citation for case: Wong Sun v. United States">371 U. S., at 488-491</a></span>.</p>
<p>[3]  I note that this resolution might have the added benefit of encouraging the police to seek a warrant whenever possible. Cf. <i>Gerstein</i> v. <i>Pugh,</i> <span class="citation" data-id="9425988"><a href="/opinion/109186/gerstein-v-pugh/#113" aria-description="Citation for case: Gerstein v. Pugh">420 U. S. 103, 113</a></span> (1975), and sources cited therein.</p>
<p>[4]  The majority of the statements cited by the Court are the officers' responses to questions inquiring as to what the officers <i>told</i> petitioner upon arresting him and thus are only indirectly relevant to the issue whether the officers might reasonably have thought they then had sufficient evidence to support a probable-cause determination. Moreover, as noted above, that evidence is contradictory. In only two instances during the trial did the inquiry relate more directly to whether the officers arrested petitioner for questioning. App. 83, 94. The officers' responses to those questions tend to support the Court's conclusion. In view of the weight of the contrary evidence, however, I think that the matter should be considered in the first instance by the state courts.</p>
<p>[5]  Petitioner's motion to suppress alleged that the police lacked reasonable grounds for believing that he committed a crime. But the testimony at the hearing focused primarily on the issue of the adequacy of the <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> warnings and the voluntariness of petitioner's statements. At the close of the hearing the trial court ruled, without elaboration or findings of fact, that the statements were admissible. <i>Id.,</i> at 65. Conceivably the trial court thought that probable cause existed to support the arrest. The State argued this point unsuccessfully on appeal. Equally possible, the trial court might have determined that the probable-cause issue was a close one and that, viewing the totality of the circumstances with that fact in mind, the statement should be admitted.</p>
<p>[6]  The Solicitor General has filed a memorandum as <i>amicus curiae</i> in which he urges the Court to remand the case for further factual hearings, cf. <i>Morales</i> v. <i>New York,</i> <span class="citation" data-id="108004"><a href="/opinion/108004/morales-v-new-york/" aria-description="Citation for case: Morales v. New York">396 U. S. 102</a></span> (1969). I concur in the Court's rejection of this suggestion, agreeing that the record is adequate to allow us to rule on the major issuewhether advice of <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights constitutes a <i>per se</i> attenuation of the taint of an illegal arrest in all cases. I do not agree, however, that the record is adequate for the Court to rule, in addition, that there was insufficient attenuation of taint in this case.</p>
<p>[7]  Petitioner's second statement, corroborative of the first, was given more than six hours after his arrest and some five hours after the initial statement. During this time petitionercooperating with the policehad made two trips away from the police headquarters in search of Claggett, whom he had identified as his confederate in the murder. This second statement was given to an assistant state's attorney who again had informed petitioner of his <i><span class="citation" data-id="9423233"><a href="/opinion/107252/miranda-v-arizona/" aria-description="Citation for case: Miranda v. Arizona">Miranda</a></span></i> rights. The Court deems this statement to be the fruit of the first one and thus excludable along with it.
</p>
<p>I also would leave the question of admissibility of this statement to the lower Illinois courts. Of course, if the first statement were ruled admissible under the general guidelines articulated in today's opinion, it would follow that the second statement also would be admissible. In any event, the question whether there was sufficient attenuation between the first and second statements to render the second admissible in spite of the inadmissibility of the first presents a factual issue which, like the factual issue underlying the possible admissibility of the first statement, has not been passed on by the state courts.</p>

</div>
```

---

## GROUP: _overhaul2/lake/cases/Brown v. Mississippi.json  (`lake-record`, 4 assertions)

### content_page

```
---
title: "Brown v. Mississippi"
type: case
citation: "297 U.S. 278 (1936)"
parallel_cite: "56 S. Ct. 461; 80 L. Ed. 682"
neutral_cite: 1936 U.S. LEXIS 527
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1936
date_decided: 1936-02-17
docket: 301
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1936-02-17
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brown v. Mississippi
  varies_by_point: false
  scope_note: "Foundational due-process voluntariness case; good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/102604/brown-v-mississippi/"
  cluster_id: 102604
  opinion_id: 102604
  identity_checked: true
homes:
  - page: "[[Due-Process Voluntariness of Confessions]]"
    role: "Key — Anchor"
related: ["[[Chambers v. Florida]]", "[[Ashcraft v. Tennessee]]", "[[Colorado v. Connelly]]"]
aliases: []
tags: ["case", "due-process", "confessions", "voluntariness", "coercion"]
holding: "A confession extracted by physical torture is involuntary and its use to convict violates Fourteenth Amendment due process."
lake:
  record_id: Brown v. Mississippi
  status: under_review
  projected_at: 2026-07-09
---

# Brown v. Mississippi

*297 U.S. 278 (1936)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Three Black tenant farmers were convicted of murder in Mississippi on the strength of confessions extracted by brutal physical torture — repeated whippings and a mock hanging — administered by a deputy and others. The torture was openly described at trial, yet the confessions were admitted and were the only real evidence of guilt.

## Issue
Whether a state criminal conviction resting solely on confessions extracted by physical torture violates the Due Process Clause of the Fourteenth Amendment.

## Rule
"And the trial equally is a mere pretense where the state authorities have contrived a conviction resting solely upon confessions obtained by violence." — 297 U.S. at 286. ^pin-286

"It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process." — [*Id.*](https://www.courtlistener.com/opinion/102604/brown-v-mississippi/#:~:text=It%20would%20be%20difficult%20to) ^pin-286b

## Application
The confessions here were wrung from the defendants by physical brutality, and the convictions rested on nothing else. Using such coerced confessions as the basis for conviction and sentence was a clear denial of due process of law.

## Conclusion
The convictions violated Fourteenth Amendment due process and were reversed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Brown* is the foundational due-process voluntariness case; the doctrine was developed in [[Chambers v. Florida]] and [[Ashcraft v. Tennessee]] and later cabined to coercive *police* conduct in [[Colorado v. Connelly]].

## Appears on
- [[Due-Process Voluntariness of Confessions]] — *Key — Anchor*

## Sources
- *Brown v. Mississippi*, 297 U.S. 278 (1936) — https://www.courtlistener.com/opinion/102604/brown-v-mississippi/ — pinpoint: 286.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a35626a0646ba530", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brown v. Mississippi"}, "payload": {"all": [{"cite": "297 U.S. 278", "page": "278", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "297"}, {"cite": "56 S. Ct. 461", "page": "461", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "56"}, {"cite": "80 L. Ed. 682", "page": "682", "reporter": "L. Ed.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "80"}, {"cite": "1936 U.S. LEXIS 527", "page": "527", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1936"}], "display": "297 U.S. 278", "official": {"cite": "297 U.S. 278", "page": "278", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "297"}, "official_selection_present": true, "record_id": "Brown v. Mississippi"}}
{"assertion_id": "1e7df5ad23edb301", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-286b", "record_id": "Brown v. Mississippi"}, "payload": {"fragment": "#:~:text=It%20would%20be%20difficult%20to", "page": null, "pin_id": "pin-286b", "pinpoint_status": "star-verified", "quote": "It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process.", "quote_fidelity": "matched", "record_id": "Brown v. Mississippi", "star_marker": "286"}}
{"assertion_id": "a05549d3353a8136", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-286", "record_id": "Brown v. Mississippi"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-286", "pinpoint_status": "slip-only", "quote": "--- # Brown v. Mississippi *297 U.S. 278 (1936)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Three Black tenant farmers were convicted of murder in Mississippi on the strength of confessions extracted by brutal physical torture — repeated whippings and a mock hanging — administered by a deputy and others. The torture was openly described at trial, yet the confessions were admitted and were the only real evidence of guilt. ## Issue Whether a state criminal conviction resting solely on confessions extracted by physical torture violates the Due Process Clause of the Fourteenth Amendment. ## Rule", "quote_fidelity": "mismatch", "record_id": "Brown v. Mississippi", "star_marker": null}}
{"assertion_id": "1d820cab93c550ec", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brown v. Mississippi"}, "payload": {"as_of_content": "1936-02-17", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brown v. Mississippi", "scope_note": "Foundational due-process voluntariness case; good law.", "varies_by_point": false}}
```

### lake record — Brown v. Mississippi

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brown v. Mississippi",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Brown v. Mississippi",
    "case_name_short": "Brown",
    "case_name_full": "BROWN Et Al. v. MISSISSIPPI",
    "input_case_name": "Brown v. Mississippi",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1936-02-17",
    "year": 1936,
    "docket": "301",
    "cluster_id": 102604,
    "lead_opinion_id": 102604,
    "sibling_ids": [
      102604
    ],
    "absolute_url": "/opinion/102604/brown-v-mississippi/",
    "identity_method": "name+docket",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": "recent_or_no_official_cite"
  },
  "citations": {
    "official": {
      "cite": "297 U.S. 278",
      "volume": "297",
      "reporter": "U.S.",
      "page": "278",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "56 S. Ct. 461",
        "volume": "56",
        "reporter": "S. Ct.",
        "page": "461",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 682",
        "volume": "80",
        "reporter": "L. Ed.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1936 U.S. LEXIS 527",
        "volume": "1936",
        "reporter": "U.S. LEXIS",
        "page": "527",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "297 U.S. 278",
        "volume": "297",
        "reporter": "U.S.",
        "page": "278",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "56 S. Ct. 461",
        "volume": "56",
        "reporter": "S. Ct.",
        "page": "461",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 682",
        "volume": "80",
        "reporter": "L. Ed.",
        "page": "682",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1936 U.S. LEXIS 527",
        "volume": "1936",
        "reporter": "U.S. LEXIS",
        "page": "527",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "297 U.S. 278",
    "official_selection": {
      "court_class": "scotus",
      "selected": "297 U.S. 278",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-286",
      "page": null,
      "quote": "--- # Brown v. Mississippi *297 U.S. 278 (1936)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Three Black tenant farmers were convicted of murder in Mississippi on the strength of confessions extracted by brutal physical torture \u2014 repeated whippings and a mock hanging \u2014 administered by a deputy and others. The torture was openly described at trial, yet the confessions were admitted and were the only real evidence of guilt. ## Issue Whether a state criminal conviction resting solely on confessions extracted by physical torture violates the Due Process Clause of the Fourteenth Amendment. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-286b",
      "page": null,
      "quote": "It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process.",
      "star_marker": "286",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 17614,
      "fragment": "#:~:text=It%20would%20be%20difficult%20to",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1936-02-17",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brown v. Mississippi",
    "varies_by_point": false,
    "scope_note": "Foundational due-process voluntariness case; good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Long",
          "cluster_id": 4786330,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
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
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Richard Ellis Hill",
          "cluster_id": 3161206,
          "cite": [
            "871 N.W.2d 900",
            "2015 Minn. LEXIS 743",
            "2015 WL 8343418"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
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
        "journal_ref": "Brown v. Mississippi:lane1_negative"
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
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Limone v. Condon",
          "cluster_id": 201063,
          "cite": [
            "372 F.3d 39",
            "2004 WL 1299980"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
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
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Peevy",
          "cluster_id": 1378981,
          "cite": [
            "17 Cal. 4th 1184",
            "953 P.2d 1212",
            "98 Daily Journal DAR 4763",
            "98 Cal. Daily Op. Serv. 3444",
            "73 Cal. Rptr. 2d 865",
            "1998 Cal. LEXIS 2623"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. D.F.",
          "cluster_id": 741773,
          "cite": [
            "115 F.3d 413",
            "1997 U.S. App. LEXIS 11994",
            "1997 WL 254194"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Norman v. Gloria Farms, Inc.",
          "cluster_id": 1703009,
          "cite": [
            "668 So. 2d 1016",
            "1996 WL 46883"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Zuliani v. State",
          "cluster_id": 2372052,
          "cite": [
            "903 S.W.2d 812",
            "1995 WL 410841"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Cathy Burns v. Rick Reed",
          "cluster_id": 686495,
          "cite": [
            "44 F.3d 524"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "People v. Cahill",
          "cluster_id": 1244769,
          "cite": [
            "853 P.2d 1037",
            "5 Cal. 4th 478",
            "20 Cal. Rptr. 2d 582",
            "93 Daily Journal DAR 8304",
            "93 Cal. Daily Op. Serv. 4902",
            "1993 Cal. LEXIS 3087"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Luther Wilkins, Jr. v. James A. May",
          "cluster_id": 521076,
          "cite": [
            "872 F.2d 190"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Griffin v. State",
          "cluster_id": 1779038,
          "cite": [
            "765 S.W.2d 422",
            "1989 Tex. Crim. App. LEXIS 29",
            "1989 WL 8702"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ex Parte McCary",
          "cluster_id": 1793877,
          "cite": [
            "528 So. 2d 1133",
            "1988 WL 10157"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane1_negative"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rose v. Lundy",
          "cluster_id": 110662,
          "cite": [
            "71 L. Ed. 2d 379",
            "102 S. Ct. 1198",
            "455 U.S. 509",
            "1982 U.S. LEXIS 79"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Fay v. Noia",
          "cluster_id": 106548,
          "cite": [
            "9 L. Ed. 2d 837",
            "83 S. Ct. 822",
            "372 U.S. 391",
            "1963 U.S. LEXIS 1945",
            "24 Ohio Op. 2d 12"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rochin v. California",
          "cluster_id": 104943,
          "cite": [
            "96 L. Ed. 2d 183",
            "72 S. Ct. 205",
            "342 U.S. 165",
            "1952 U.S. LEXIS 2576",
            "25 A.L.R. 2d 1396",
            "96 L. Ed. 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Linkletter v. Walker",
          "cluster_id": 107084,
          "cite": [
            "14 L. Ed. 2d 601",
            "85 S. Ct. 1731",
            "381 U.S. 618",
            "1965 U.S. LEXIS 2283",
            "5 Ohio Misc. 49",
            "33 Ohio Op. 2d 118"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brown v. Allen",
          "cluster_id": 105074,
          "cite": [
            "97 L. Ed. 2d 469",
            "73 S. Ct. 397",
            "344 U.S. 443",
            "1953 U.S. LEXIS 2391",
            "97 L. Ed. 469"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Palko v. Connecticut",
          "cluster_id": 102879,
          "cite": [
            "302 U.S. 319",
            "58 S. Ct. 149",
            "82 L. Ed. 288",
            "1937 U.S. LEXIS 549"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McNabb v. United States",
          "cluster_id": 103791,
          "cite": [
            "318 U.S. 332",
            "63 S. Ct. 608",
            "87 L. Ed. 819",
            "1943 U.S. LEXIS 1280"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Screws v. United States",
          "cluster_id": 104135,
          "cite": [
            "325 U.S. 91",
            "65 S. Ct. 1031",
            "89 L. Ed. 1495",
            "1945 U.S. LEXIS 2096",
            "162 A.L.R. 1330"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
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
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lego v. Twomey",
          "cluster_id": 108429,
          "cite": [
            "30 L. Ed. 2d 618",
            "92 S. Ct. 619",
            "404 U.S. 477",
            "1972 U.S. LEXIS 100"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Shelley v. Kraemer",
          "cluster_id": 104545,
          "cite": [
            "92 L. Ed. 2d 1161",
            "68 S. Ct. 836",
            "334 U.S. 1",
            "1948 U.S. LEXIS 2764",
            "3 A.L.R. 2d 441",
            "92 L. Ed. 1161"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Miller v. Fenton",
          "cluster_id": 111542,
          "cite": [
            "88 L. Ed. 2d 405",
            "106 S. Ct. 445",
            "474 U.S. 104",
            "1985 U.S. LEXIS 144",
            "54 U.S.L.W. 4022"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estes v. Texas",
          "cluster_id": 107083,
          "cite": [
            "14 L. Ed. 2d 543",
            "85 S. Ct. 1628",
            "381 U.S. 532",
            "1965 U.S. LEXIS 2339",
            "1 Media L. Rep. (BNA) 1187",
            "6 Rad. Reg. 2d (P & F) 2104"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Culombe v. Connecticut",
          "cluster_id": 106284,
          "cite": [
            "6 L. Ed. 2d 1037",
            "81 S. Ct. 1860",
            "367 U.S. 568",
            "1961 U.S. LEXIS 811"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wolf v. Colorado",
          "cluster_id": 104709,
          "cite": [
            "93 L. Ed. 2d 1782",
            "69 S. Ct. 1359",
            "338 U.S. 25",
            "1949 U.S. LEXIS 2079",
            "93 L. Ed. 1782"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hansberry v. Lee",
          "cluster_id": 103379,
          "cite": [
            "311 U.S. 32",
            "61 S. Ct. 115",
            "85 L. Ed. 22",
            "1940 U.S. LEXIS 108",
            "132 A.L.R. 741"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Mississippi:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(102604) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz01Mzg3OTA0MDAwMDAmcz0xMTQ4MDg1JnQ9byZkPTIwMjYtMDctMDQmcD0xMQ%3D%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28102604%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
        "audit_needed": true,
        "proposed_negative_events": 16,
        "audit_marker": "R15 treatment audit required",
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 200,
        "triage_read": 16,
        "triage_snippet_classified": 184
      },
      "lane2_top_cited": {
        "query": "cites:(102604)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz05MDgmcz0xMTI0NTImdD1vJmQ9MjAyNi0wNy0wNCZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%28102604%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(102604)",
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
    "complete_query": "cites:(102604)",
    "indexed_citing_opinions": 618,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 102604,
        "count": 618,
        "count_source": "search"
      }
    ],
    "citation_count": 961,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brown-v-mississippi.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjU2NTc4Nzcmcz00NDQ5OTI0JnQ9byZkPTIwMjYtMDctMDQmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28102604%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 102604,
        "cited_id": 89245,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 91054,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 96356,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 96885,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 100122,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 100929,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 102189,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 102372,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 1236300,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 3517982,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 102604,
        "cited_id": 3518564,
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
    "date_created": "2026-07-04T20:48:14Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:48:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:48:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:53:09Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:48:37Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brown v. Mississippi

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b325-8">
  Mr. Chief Justice Hughes
 </author>
<p id="AqF">
  delivered the opinion of the Court.
 </p>
<p id="b325-9">
  The question in this case is whether convictions, which rest solely upon confessions shown to have been extorted by officers of the.State by brutality and violence, are consistent with the due process of law required by the Fourteenth Amendment of the Constitution of the United States.
 </p>
<p id="b325-10">
  Petitioners were indicted for the murder of one Raymond Stewart, whose death occurred on March 30, 1934. They, were indicted on April 4, 1934, and were then arraigned and. pleaded not guilty. Counsel were appointed by the court to defend them. Trial was begun the next morning and was concluded on the following day, when they were found guilty and sentenced to death.
 </p>
<p id="b325-11">
  Aside from the confessions, there Was no evidence sufficient, to warrant the submission of the case to the jury. After a preliminary inquiry, testimony as to the confessions was received over the objection of defendants’ counsel. Defendants then testified that the confessions were false and had been procured-by physical torture. The case went to the 'jury with instructions, upon the request of defendants’ counsel, that if the jury had reasonable doubt as to the. confessions having resulted, from coercion, and that they were not true, they were not to be considered as evidence. On their appeal to the Su
  <span citation-index="1" class="star-pagination" label="280"> 
   *280
   </span>
  preme Court of the State, defendants assigned as error the inadmissibility of the confessions. The judgment was affirmed. <span class="citation" data-id="3520101"><a href="/opinion/3547181/brown-v-state/" aria-description="Citation for case: Brown v. State">158 So. 339</a></span>.
 </p>
<p id="b326-6">
  Defendants then moved in the Supreme Court of the State to arrest the judgment and for a new trial' on the ground, that all the evidence against them was obtained by coercion and brutality known to the court and to-the district attorney, and that defendants had been denied the benefit of counsel or opportunity to confer with counsel in, a reasonable manner. The motion was supported by affidavits. At about the same time, defendants filed in the Supreme Court a “suggestion of error” explicitly challenging the proceedings of the trial, in the use of- the confessions and with respect to the alleged denial of representation by counsel, as violating the due process clause of the Fourteenth Amendment of the Constitution of the United States. The state court entertained the suggestion of error, considered the federal question, and decided it against defendants’ contentions. <span class="citation multiple-matches"><a href="/c/So./161/465/">161 So. 465</a></span>. Two judges dissented..
  <em>
   Id.,
  </em>
  p. 470. We granted a writ of certiorari.
 </p>
<p id="b326-7">
  The grounds of the decision were (1) that immunity from self-incrimination is not essential to due process of law, and (2) that the failure of the trial court to exclude the confessions after the introduction of evidence showing their incompetency, in the absence-of a request for such exclusion, did not deprive the defendants of life or liberty without due process of law; and that even if the trial court had erroneously overruled a motion to exclude the confessions^ the ruling would have been, mere error reversible on appeal, but not a violation of constitutional right.
  <em>
   Id.,
  </em>
  p. 468.
 </p>
<p id="b326-8">
  The opinion of the state court did not set forth the evidence as to the circumstances in which the confessions were procured. That the evidence established that they were procured by coercion was not questioned. The state
  <span citation-index="1" class="star-pagination" label="281"> 
   *281
   </span>
  court said: “After the state closed its case on the merits, the appellants, for the first time, introduced evidence from which it appears that the confessions were not madé voluntarily but were coerced.”
  <em>
   Id.,
  </em>
  p. 466. There is no dispute as to the facts upon this point- and as they are clearly and adequately stated in the dissenting opinion of •Judge Griffith (with whom Judge Anderson concurred)-^-1 showing both the extreme brutality of the measures to extort the confessions and the participation of the state auth orities — we quote this part of his opinion in full, as follows
  <em>
   (Id.,
  </em>
  pp. 470, 471):'
 </p>
<blockquote id="b327-6">
  “The crime with which these defendants, all ignorant negroes, are charged, was discovered about one o’clock p. m. on ¡Friday, March 30,1934. On that night one Dial, a deputy sheriff, accompanied by others, came to the home of Ellington,- one of the defendants, and requested him to accompany them to the house of the deceased, and there, a number of white men were gathered, who began to accuse the defendant of the crime. Upon his denial they seized him, and with the participation of the deputy they . hanged him by a rope to the limb of a tree, and having let him down, they hung him again, and when he was.let down the second time, and he still' protested his innocence, he was tied to a tree and whipped, and still declining to accede to the demands that he confess, he was finally released and he returned with some difficulty to his home, suffering intense pain and agony. The record of the' testimony shows that the signs of the rope on his neck were plainly visible during the so-called trial: A da, or two thereafter the said deputy; accompanied by another, returned to the home of the said defendant and arrested him, and departed’with the prisoner towards the jail in an adjoining county, but., went by a route which led into the State of Alabama; and while on the way, in that State, the deputy stopped and again severely whipped the defendant, declaring that he would continue the whipping
  <span citation-index="1" class="star-pagination" label="282"> 
   *282
   </span>
  until he confessed, and the defendant then agreed to confess to such a statement as the deputy would dictate, and he did so, after which he was delivered to jail.
 </blockquote>
<blockquote id="b328-5">
  “The other two defendants, Ed Brown and Henry Shields, were also arrested and taken to the same jail. On Sunday night, April 1, 1934, the same deputy, accompanied by a number of white men, one of whom was also an officer, and by the jailer, came to the jail, and the two last named defendants were made to strip and they were laid over chairs and their backs were cut to pieces with a leather strap with buckles on it, and they were likewise made by the said deputy definitely to understand that the whipping would be continued unless and until they confessed, and not only confessed,' but confessed in every matter of detail as demanded by those present; and in this manner the defendants confessed the crime, and as the whippings progressed and were repeated, they changed or adjusted their confession in all particulars of detail so as to conform to the demands of their torturers. When the confessions had been obtained in the exact form and contents as desired by the mob, they left with the parting admonition and warning that, if the defendants changed their story at any time in any respect from that last statéd, the perpetrators of the outrage would administer the same or equally effective treatment.
 </blockquote>
<blockquote id="b328-6">
  “Further details of the brutal treatment to which these helpless prisoners were subjected need not be pursued. It is sufficient to say that in pertinent respects the transcript reads more like pages tom from some medieval account, than a record made within the confines of a modern civilization which aspires to an enlightened constitutional government.
 </blockquote>
<blockquote id="b328-7">
  “All this having been accomplished, on. the next day, that is, on Monday, April 2, when the defendants had been given time to recuperate somewhat from the tortures to which they had been subjected, the two sheriffs, one
  <span citation-index="1" class="star-pagination" label="283"> 
   *283
   </span>
  of the county where the crime was committed,. and the other of the county of the jail in which the prisoners were confined, came to the jail, accompanied by eight other persons, some of them deputies, there to hear the free and yoluntary confession of these miserable and abject defendants. The sheriff of the county of the crime admitted that he had heard of the whipping, but averred that he had no personal knowledge of it. He admitted that one of the defendants, when brought before him to confess, was limping and did not sit down, and that this particular defendant then and there stated that he had been strapped so severely that he could not sit down, and as already stated, the signs of the rope on the neck of another of the defendants were plainly visible to all. Nevertheless the. solemn farce of hearing the free and voluntary confessions was gone through with, and these two sheriffs and one other person then present were the three witnesses used in court to establish the so-called confessions, which were received by the court and admitted in evidence over the objections of the defendants duly entered of record as each of the said three witnesses delivered their alleged testimony. There was thus enough before the court when these confessions were first offered to make known to the court, that they were not, beyond all reasonable doubt, free and voluntary; and the failure of the court then to exclude the confessions is sufficient to reverse the judgment, under every rule of procedure that has heretofore been prescribed, and hence it was not necessary subsequently to renew the objections by motion or otherwise. *
 </blockquote>
<blockquote id="b329-6">
  “The spurious confessions having been obtained — and the farce last mentioned having been gone through with on Monday, April 2d — the court, thén in session, on the' following day, Tuesday, April 3, 1934, ordered the grand jury to reassemble on the succeeding day, April 4, 1934, at nine o’clock, and on the morning of the day last men
  <span citation-index="1" class="star-pagination" label="284"> 
   *284
   </span>
  tionecl the grand jury returned an indictment against the defendants- for murder. Late that afternoon the defendants were brought from the jail in the adjoining county and arraigned, when one or more of them offered to plead guilty, which the • court declined to accept, and, upon inquiry whether they had or desired counsel, they stated that they had none, and did not suppose that counsel could be of any assistance to them. The court thereupon appointed counsel, and set the case for trial for the following morning at nine o’clock, and the defendants were returned to the jail in the adjoining county about thirty mile's away.
 </blockquote>
<blockquote id="AIdQ">
  “The defendants were brought to the courthouse of the county on the following morning, April 5th, and the so-' called trial was opened, and was concluded on the next day, April 6, 1934, and resulted in a pretended conviction with' death sentences. The evidence upon which the conviction was obtained was the so-called confessions. Without this evidence a peremptory instruction to find for the defendants'would have been inescapable. The defendants were put on the stand, and by their testimony the facts and the details thereof as to the manner by which the confessions were extorted from them were fully developed, and it is. further disclosed by the record that the same deputy, Dial, .under whose guiding hand and active participation the tortures to coerce the confessions were administered, was actively in the performance of the supposed duties of a court deputy in the courthouse and in the presence of the prisoners during what is denominated, in complimentaiy terms, the trial of these defendants. This deputy was put on the stand by the1 state in rebuttal, and admitted the whippings. It is interesting to note that in his testimony with reference to the whipping of the defendant Ellington, and in response to the inquiry as to how severely.he was whipped, the deputy stated, ‘Not, too much for a negro; .not as much as I would have done if it were left to me.’ Two others who had participated
  <span citation-index="1" class="star-pagination" label="285"> 
   *285
   </span>
  in these whippings were introduced and admitted it — not a single witness was introduced who denied it. The facts are not only undisputed, they are admitted, and admitted to have been done by officers of the state, in conjunction with other participants, and all this was definitely well known to everybody connected with the trial, and during the trial, including the state’s prosecuting attorney and the trial judge presiding.”
 </blockquote>
<p id="A4jD">
  1. The State stresses the statement in
  <em>
   Twining
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="9418128"><a href="/opinion/96885/twining-v-new-jersey/#114" aria-description="Citation for case: Twining v. New Jersey">211 U. S. 78, 114</a></span>, that “exemption from compulsory self-incrimination in the courts of the States is not secured by any part of the Federal Constitution,” and the statement in
  <em>
   Snyder
  </em>
  v.
  <em>
   Massachusetts,
  </em>
  <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/#105" aria-description="Citation for case: Snyder v. Massachusetts">291 U. S. 97, 105</a></span>, that “the privilege against self-incrimination may be withdrawn .and the accused put upon the stand as a witness for the State.” But the question of the right of the State to withdraw the privilege against self-incrimination is not here involved. The compulsion to which .the quoted statements refer is that of -the processes' of justice by which the accused may be called as a witness and required to testify. Compulsion by torture to extort a confession is a different matter.
 </p>
<p id="b331-7">
  The State is free to regulate the procedure of its courts in accordance with its own conceptions of policy, unless in so doing it “offends some principle of justice so rooted in the traditions and conscience of our people as to be ranked as fundamental.”
  <em>
   Snyder
  </em>
  v.
  <em>
   <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/" aria-description="Citation for case: Snyder v. Massachusetts">Massachusetts, supra;</a></span> Rogers
  </em>
  v.
  <em>
   Peck,
  </em>
  <span class="citation" data-id="96356"><a href="/opinion/96356/rogers-v-peck/#434" aria-description="Citation for case: Rogers v. Peck">199 U. S. 425, 434</a></span>. The State may abolish trial'by jury. It may dispense with indictment by a grand jury and substitute complaint or information.
  <em>
   Walker
  </em>
  v.
  <em>
   Sauvinet,
  </em>
  <span class="citation" data-id="89245"><a href="/opinion/89245/walker-v-sauvinet/" aria-description="Citation for case: Walker v. Sauvinet">92 U. S. 90</a></span>;
  <em>
   Hurtado
  </em>
  v.
  <em>
   California,
  </em>
  <span class="citation" data-id="9417375"><a href="/opinion/91054/hurtado-v-california/" aria-description="Citation for case: Hurtado v. California">110 U. S. 516</a></span>;
  <em>
   Snyder
  </em>
  v.
  <em>
   <span class="citation" data-id="9418797"><a href="/opinion/102189/snyder-v-massachusetts/" aria-description="Citation for case: Snyder v. Massachusetts">Massachusetts, supra.</a></span>
  </em>
  But the freedom of the State in establishing its policy is the freedom of constitutional government and is limited by the requirement of due process of law. Because a State may dispense with a jury trial, it does not follow that it may substitute trial by ordeal. The rack and tor
  <span citation-index="1" class="star-pagination" label="286"> 
   *286
   </span>
  ture chamber may not be substituted for the witness stand. The ■ State may not permit, an accused to be hurried to conviction under mob domination — where the whole pro- ■ ceeding is but a mask — without supplying corrective process.
  <em>
   Moore
  </em>
  v.
  <em>
   Dempsey,
  </em>
  <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/#91" aria-description="Citation for case: Moore v. Dempsey">261 U. S. 86, 91</a></span>. The State may not deny to the accused the aid of counsel.
  <em>
   Powell
  </em>
  v.
  <em>
   Alabama,
  </em>
  <span class="citation" data-id="9575538"><a href="/opinion/1236300/powell-v-alabama/" aria-description="Citation for case: Powell v. Alabama">287 U. S. 45</a></span>. Nor may a State, through the action of its officers, contrive a conviction through the pretense of a trial which in truth is “but used as a means of depriving a defendant of liberty through a deliberate deception of court and jury, by the presentation of testimony known to be perjured.”
  <em>
   Mooney
  </em>
  v.
  <em>
   Holohan,
  </em>
  <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/#112" aria-description="Citation for case: Mooney v. Holohan">294 U. S. 103, 112</a></span>. And the trial equally is a mere pretense where the state authorities have contrived a conviction resting solely upon confessions obtained by violence. The due process clause requires “that state action, whether through one agency or another, shall be consistent with the fundamental principles of liberty and justice which lie at the base of all oúr civil ,and political institutions.”
  <em>
   Hebert
  </em>
  v.
  <em>
   Louisiana,
  </em>
  <span class="citation" data-id="100929"><a href="/opinion/100929/hebert-v-louisiana/#316" aria-description="Citation for case: Hebert v. Louisiana">272 U. S. 312, 316</a></span>. It would be difficult to conceive of methods more revolting to the sense of justice than those taken to procure the confessions of these petitioners, and the use of the confessions thus obtained as the basis for conviction and sentence was a clear denial of due process.
 </p>
<p id="b332-5">
  2. It is in this view that the further contention of the State must be considered. That contention rests upon the failure of counsel .for the accused, who had objected to the admissibility of the confessions, to move for1 their exclusion after they had been introduced and the fact of coercion had been proved. It is a contention which proceeds upon a misconception of the nature of petitioners’ complaint. That complaint is not of the commission of mere error, but of a wrong so fundamental that it made the whole proceeding a. mere pretense of a trial and rendered-the conviction and sentence wholly void.
  <em>
   Moore
  </em>
  v.
  <em>
   <span class="citation" data-id="9418497"><a href="/opinion/100122/moore-v-dempsey/" aria-description="Citation for case: Moore v. Dempsey">Dempsey, supra.</a></span>
  </em>
  We are not concerned with a mere
  <span citation-index="1" class="star-pagination" label="287"> 
   *287
   </span>
  question of state practice, or whether counsel assigned to petitioners were competent ór mistakenly assumed that their first objections were sufficient. In an earlier case the Supreme Court of the State had recognized the duty of the court to supply corrective process where due process of law had been denied. In
  <em>
   Fisher
  </em>
  v.
  <em>
   State,
  </em>
  <span class="citation" data-id="3518564"><a href="/opinion/3545864/fisher-v-state/#134" aria-description="Citation for case: Fisher v. State">145 Miss. 116, 134</a></span>; <span class="citation" data-id="3518564"><a href="/opinion/3545864/fisher-v-state/#365" aria-description="Citation for case: Fisher v. State">110 So. 361, 365</a></span>, the court said: “Coercing the supposed state’s criminals into confessions and using such confessions so coerced from them against them in trials has been the curse of all countries. It was the chief inequity, the crowning infamy of the Star Chamber, and the Inquisition, and other similar institutions. The constitution recognized the evils that lay behind these practices and prohibited them in this country. . . . The duty of maintaining constitutional rights of a person on trial for his life rises above mere rules of procedure and wherever the court is clearly satisfied that such violations exist, it will refuse to sanction such violations and will apply the corrective.”
 </p>
<p id="b333-6">
  In the instant case, the trial court was fully advised by the undisputed evidence of the way in which the confessions had been procured-. The trial court knew that there was no other evidence upon which conviction and sentence could be based. Yet it proceeded to permit conviction and to pronounce sentence. The conviction and sentence were void for want of the essential elements of due process, and the proceeding thus vitiated could be challenged in any appropriate manner.
  <em>
   Mooney
  </em>
  v.
  <em>
   <span class="citation" data-id="102372"><a href="/opinion/102372/mooney-v-holohan/" aria-description="Citation for case: Mooney v. Holohan">Holohan, supra.</a></span>
  </em>
  It was challenged before the Supreme Court of the State by the express invocation of the Fourteenth Amendment. That court entertained the challenge, considered the federal question thus presented, but declined to enforce petitioners’ constitutional right. The court thus denied a federal right fully established and specially set up and claimed and the jüdgment must be
 </p>
<p id="b333-7">
<em>
   Reversed.
  </em>
</p>
</opinion>
```

---

## GROUP: _overhaul2/lake/cases/Brown v. Texas.json  (`lake-record`, 5 assertions)

### content_page

```
---
title: "Brown v. Texas"
type: case
citation: "443 U.S. 47 (1979)"
parallel_cite: "99 S. Ct. 2637; 61 L. Ed. 2d 357"
neutral_cite: 1979 U.S. LEXIS 136
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1979
date_decided: 1979-06-25
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1979-06-25
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Brown v. Texas
  varies_by_point: false
  scope_note: "Good law. Police may not detain a person and demand identification without reasonable suspicion; the case supplies the three-factor balancing test for suspicionless seizures. Hiibel v. Sixth Judicial Dist. Court (2004) later upheld an identify-yourself demand during a lawful Terry stop — the question Brown expressly reserved — and does not disturb Brown."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/110128/brown-v-texas/"
  cluster_id: 110128
  opinion_id: 110128
  identity_checked: true
homes:
  - page: "[[Terry Stops and Reasonable Suspicion]]"
    role: "Anchor"
  - page: "[[Seizure of the Person]]"
    role: "Related (cross-doctrine)"
related: ["[[Terry v. Ohio]]", "[[Delaware v. Prouse]]", "[[Hiibel v. Sixth Judicial Dist. Court]]", "[[Kolender v. Lawson]]"]
aliases: []
tags: ["case", "fourth-amendment", "terry-stop", "reasonable-suspicion", "stop-and-identify", "seizure"]
holding: "Police may not stop a person and demand identification without reasonable suspicion of criminal activity; the constitutionality of suspicionless seizures is judged by balancing public concern, advancement of the public interest, and the severity of the intrusion on liberty."
lake:
  record_id: Brown v. Texas
  status: under_review
  projected_at: 2026-07-06
---

# Brown v. Texas

*443 U.S. 47 (1979)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Two El Paso officers, patrolling an area with a high incidence of drug traffic, saw Brown and another man walking in opposite directions away from one another in an alley. They stopped Brown and asked him to identify himself and explain what he was doing. One officer testified the situation "looked suspicious" but could point to no specific facts; he acknowledged the only reason for the stop was to ascertain Brown's identity. Brown refused to identify himself and was arrested and convicted under a Texas statute (§ 38.02) making it a crime to refuse to give one's name to an officer who has lawfully stopped him.

## Issue
Whether officers may detain an individual and require him to identify himself, on penalty of criminal punishment for refusing, when they lack reasonable suspicion that he is engaged in criminal activity.

## Rule
No. The constitutionality of a seizure short of arrest is judged by a balancing test: "Consideration of the constitutionality of such seizures involves a weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty." — 443 U.S. at 51. ^pin-51

And the seizure of a particular person requires individualized, objective justification: "the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society's legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers." — *Id.* at 51. ^pin-51b

A brief investigative detention therefore demands "a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity."

## Application
The officers had no such basis. One could say only that the alley "looked suspicious" without identifying any supporting fact; there was no indication it was unusual for people to be there; and "[t]he fact that appellant was in a neighborhood frequented by drug users, standing alone, is not a basis for concluding that appellant himself was engaged in criminal conduct." The only reason for the stop was to learn Brown's identity. Absent reasonable suspicion, the stop tilted the balance toward the individual's liberty, and the Court held: "The application of Tex. Penal Code Ann., Tit. 8, § 38.02 (1974), to detain appellant and require him to identify himself violated the Fourth Amendment because the officers lacked any reasonable suspicion to believe appellant was engaged or had engaged in criminal conduct." — *Id.* at 53. ^pin-53

## Conclusion
Because the stop was not supported by reasonable suspicion, applying the statute to punish Brown for refusing to identify himself violated the Fourth Amendment; the conviction was reversed. An officer may not seize a person to demand identification without reasonable suspicion (or a neutral, plan-based scheme).

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. The *Brown* three-factor balancing test governs suspicionless seizures and is applied in the checkpoint cases ([[Michigan Dept. of State Police v. Sitz]], [[City of Indianapolis v. Edmond]], [[Illinois v. Lidster]]). The Court expressly reserved whether an individual may be required to identify himself during a *lawful* investigatory stop; [[Hiibel v. Sixth Judicial Dist. Court]] (2004) answered yes, upholding a stop-and-identify statute applied during a *[[Terry v. Ohio|Terry]]* stop supported by reasonable suspicion — distinguishing, not overruling, *Brown*.

## Appears on
- [[Terry Stops and Reasonable Suspicion]] — *Anchor*
- [[Seizure of the Person]] — *Related (cross-doctrine)*

## Sources
- *Brown v. Texas*, 443 U.S. 47 (1979) — https://www.courtlistener.com/opinion/110128/brown-v-texas/ — pinpoints: 51, 52, 53.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "97a1cd3fc3bad89e", "dimension": "existence", "kind": "case_cite", "locator": {"record_id": "Brown v. Texas"}, "payload": {"all": [{"cite": "443 U.S. 47", "page": "47", "reporter": "U.S.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "443"}, {"cite": "99 S. Ct. 2637", "page": "2637", "reporter": "S. Ct.", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "99"}, {"cite": "61 L. Ed. 2d 357", "page": "357", "reporter": "L. Ed. 2d", "selected_official": false, "source": "cluster.citations[]", "type": 1, "volume": "61"}, {"cite": "1979 U.S. LEXIS 136", "page": "136", "reporter": "U.S. LEXIS", "selected_official": false, "source": "cluster.citations[]", "type": 6, "volume": "1979"}], "display": "443 U.S. 47", "official": {"cite": "443 U.S. 47", "page": "47", "reporter": "U.S.", "selected_official": true, "source": "cluster.citations[]", "type": 1, "volume": "443"}, "official_selection_present": true, "record_id": "Brown v. Texas"}}
{"assertion_id": "39902fdf9ea56d1b", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-51b", "record_id": "Brown v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-51b", "pinpoint_status": "slip-only", "quote": "the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society's legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers.", "quote_fidelity": "mismatch", "record_id": "Brown v. Texas", "star_marker": null}}
{"assertion_id": "5d71cfe3c27c8812", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-53", "record_id": "Brown v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-53", "pinpoint_status": "slip-only", "quote": "## Application The officers had no such basis. One could say only that the alley", "quote_fidelity": "mismatch", "record_id": "Brown v. Texas", "star_marker": null}}
{"assertion_id": "fbcce3d5aaae9344", "dimension": "quote_fidelity", "kind": "quote_pinpoint", "locator": {"pin_id": "pin-51", "record_id": "Brown v. Texas"}, "payload": {"fragment": null, "page": null, "pin_id": "pin-51", "pinpoint_status": "slip-only", "quote": "but could point to no specific facts; he acknowledged the only reason for the stop was to ascertain Brown's identity. Brown refused to identify himself and was arrested and convicted under a Texas statute (§ 38.02) making it a crime to refuse to give one's name to an officer who has lawfully stopped him. ## Issue Whether officers may detain an individual and require him to identify himself, on penalty of criminal punishment for refusing, when they lack reasonable suspicion that he is engaged in criminal activity. ## Rule No. The constitutionality of a seizure short of arrest is judged by a balancing test:", "quote_fidelity": "mismatch", "record_id": "Brown v. Texas", "star_marker": null}}
{"assertion_id": "f190db6d91c4fb4b", "dimension": "treatment", "kind": "treatment", "locator": {"record_id": "Brown v. Texas"}, "payload": {"as_of_content": "1979-06-25", "as_of_treatment": "2026-06-30", "field_i_validity": "good_law", "record_id": "Brown v. Texas", "scope_note": "Good law. Police may not detain a person and demand identification without reasonable suspicion; the case supplies the three-factor balancing test for suspicionless seizures. Hiibel v. Sixth Judicial Dist. Court (2004) later upheld an identify-yourself demand during a lawful Terry stop — the question Brown expressly reserved — and does not disturb Brown.", "varies_by_point": false}}
```

### lake record — Brown v. Texas

```json
{
  "schema_version": "s2.v1",
  "record_id": "Brown v. Texas",
  "stub": false,
  "status": "under_review",
  "identity": {
    "case_name": "Brown v. Texas",
    "case_name_short": "Brown",
    "case_name_full": "Brown v. Texas",
    "input_case_name": "Brown v. Texas",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1979-06-25",
    "year": 1979,
    "docket": null,
    "cluster_id": 110128,
    "lead_opinion_id": 110128,
    "sibling_ids": [
      110128
    ],
    "absolute_url": "/opinion/110128/brown-v-texas/",
    "identity_method": "pending",
    "expected_citation_found": true,
    "party_name_in_text": false,
    "canonical_name_match": true,
    "alternates": [
      {
        "cluster_id": 9021114,
        "score": 10,
        "case_name": "Brown v. Texas"
      },
      {
        "cluster_id": 9020748,
        "score": 10,
        "case_name": "Brown v. Texas"
      }
    ],
    "reason_code": "two_key_not_satisfied"
  },
  "citations": {
    "official": {
      "cite": "443 U.S. 47",
      "volume": "443",
      "reporter": "U.S.",
      "page": "47",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "99 S. Ct. 2637",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 357",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1979 U.S. LEXIS 136",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "443 U.S. 47",
        "volume": "443",
        "reporter": "U.S.",
        "page": "47",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "99 S. Ct. 2637",
        "volume": "99",
        "reporter": "S. Ct.",
        "page": "2637",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "61 L. Ed. 2d 357",
        "volume": "61",
        "reporter": "L. Ed. 2d",
        "page": "357",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1979 U.S. LEXIS 136",
        "volume": "1979",
        "reporter": "U.S. LEXIS",
        "page": "136",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "443 U.S. 47",
    "official_selection": {
      "court_class": "scotus",
      "selected": "443 U.S. 47",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-51",
      "page": null,
      "quote": "but could point to no specific facts; he acknowledged the only reason for the stop was to ascertain Brown's identity. Brown refused to identify himself and was arrested and convicted under a Texas statute (\u00a7 38.02) making it a crime to refuse to give one's name to an officer who has lawfully stopped him. ## Issue Whether officers may detain an individual and require him to identify himself, on penalty of criminal punishment for refusing, when they lack reasonable suspicion that he is engaged in criminal activity. ## Rule No. The constitutionality of a seizure short of arrest is judged by a balancing test:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-51b",
      "page": null,
      "quote": "the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society's legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-53",
      "page": null,
      "quote": "## Application The officers had no such basis. One could say only that the alley",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1979-06-25",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Brown v. Texas",
    "varies_by_point": false,
    "scope_note": "Good law. Police may not detain a person and demand identification without reasonable suspicion; the case supplies the three-factor balancing test for suspicionless seizures. Hiibel v. Sixth Judicial Dist. Court (2004) later upheld an identify-yourself demand during a lawful Terry stop \u2014 the question Brown expressly reserved \u2014 and does not disturb Brown.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Commonwealth v. Arias",
          "cluster_id": 10843215,
          "cite": null,
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 9352626,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Cobb",
          "cluster_id": 6466320,
          "cite": null,
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Sievers - supplemental opinion",
          "cluster_id": 4571040,
          "cite": [
            "301 Neb. 806",
            "920 N.W.2d 443"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Baskins",
          "cluster_id": 4524209,
          "cite": [
            "818 S.E.2d 381",
            "260 N.C. App. 589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Christian",
          "cluster_id": 4477521,
          "cite": [
            "2018 Ohio 957",
            "109 N.E.3d 183"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Hairston",
          "cluster_id": 4426228,
          "cite": [
            "2017 Ohio 7612",
            "97 N.E.3d 784"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Elvis Elvis Ramirez-Tamayo v. State",
          "cluster_id": 4311099,
          "cite": [
            "501 S.W.3d 788",
            "2016 Tex. App. LEXIS 10905",
            "2016 WL 5874327"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State v. Ashworth",
          "cluster_id": 4243394,
          "cite": [
            "790 S.E.2d 173",
            "248 N.C. App. 649",
            "2016 N.C. App. LEXIS 816"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Carlos Gonzalez v. Able Huerta",
          "cluster_id": 3216824,
          "cite": [
            "826 F.3d 854",
            "2016 U.S. App. LEXIS 11530",
            "2016 WL 3457258"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Leming v. State",
          "cluster_id": 5447022,
          "cite": [
            "493 S.W.3d 552",
            "2016 WL 1458242",
            "2016 Tex. Crim. App. LEXIS 73"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Mocek v. City of Albuquerque",
          "cluster_id": 3164764,
          "cite": [
            "813 F.3d 912",
            "2015 U.S. App. LEXIS 22435",
            "2015 WL 9298662"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Mercedes-De la Cruz",
          "cluster_id": 2803337,
          "cite": [
            "787 F.3d 61",
            "2015 U.S. App. LEXIS 8624",
            "2015 WL 3378255"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane1_negative"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Cortez",
          "cluster_id": 110377,
          "cite": [
            "66 L. Ed. 2d 621",
            "101 S. Ct. 690",
            "449 U.S. 411",
            "1981 U.S. LEXIS 58",
            "49 U.S.L.W. 4099"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sokolow",
          "cluster_id": 112239,
          "cite": [
            "104 L. Ed. 2d 1",
            "109 S. Ct. 1581",
            "490 U.S. 1",
            "1989 U.S. LEXIS 1694",
            "57 U.S.L.W. 4401"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Illinois v. Wardlow",
          "cluster_id": 118326,
          "cite": [
            "145 L. Ed. 2d 570",
            "120 S. Ct. 673",
            "528 U.S. 119",
            "2000 U.S. LEXIS 504"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ford v. State",
          "cluster_id": 1355298,
          "cite": [
            "158 S.W.3d 488",
            "2005 Tex. Crim. App. LEXIS 399",
            "2005 WL 544796"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Smith",
          "cluster_id": 1828048,
          "cite": [
            "433 So. 2d 688"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michigan Department of State Police v. Sitz",
          "cluster_id": 112459,
          "cite": [
            "110 L. Ed. 2d 412",
            "110 S. Ct. 2481",
            "496 U.S. 444",
            "1990 U.S. LEXIS 3144",
            "58 U.S.L.W. 4781"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reid v. Georgia",
          "cluster_id": 110336,
          "cite": [
            "65 L. Ed. 2d 890",
            "100 S. Ct. 2752",
            "448 U.S. 438",
            "1980 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wyoming v. Houghton",
          "cluster_id": 118277,
          "cite": [
            "143 L. Ed. 2d 408",
            "119 S. Ct. 1297",
            "526 U.S. 295",
            "1999 U.S. LEXIS 2347"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
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
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Schall v. Martin",
          "cluster_id": 111198,
          "cite": [
            "81 L. Ed. 2d 207",
            "104 S. Ct. 2403",
            "467 U.S. 253",
            "1984 U.S. LEXIS 96",
            "52 U.S.L.W. 4681"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Yeargan",
          "cluster_id": 1060948,
          "cite": [
            "958 S.W.2d 626",
            "1997 Tenn. LEXIS 574",
            "1997 WL 724993"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Howard",
          "cluster_id": 5684310,
          "cite": [
            "50 N.Y.2d 583",
            "408 N.E.2d 908",
            "430 N.Y.S.2d 578",
            "1980 N.Y. LEXIS 2454"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Brown v. Texas:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(110128) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xMzkyNzY4MDAwMDAwJnM9MjY3OTQ2MSZ0PW8mZD0yMDI2LTA3LTA0JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28110128%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(110128)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNzEmcz0yOTQ3NzE2JnQ9byZkPTIwMjYtMDctMDQmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28110128%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(110128)",
        "reviewed": 32,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 32,
        "triage_read": 1,
        "triage_snippet_classified": 31
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(110128)",
    "indexed_citing_opinions": 1635,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 110128,
        "count": 1635,
        "count_source": "search"
      }
    ],
    "citation_count": 2680,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/brown-v-texas.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg1MjY3NCZzPTk0Mzg0MTMmdD1vJmQ9MjAyNi0wNy0wNCZwPTI%3D&order_by=score+desc&page_size=100&q=cites%3A%28110128%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 110128,
        "cited_id": 103170,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 107729,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 107912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109311,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109541,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 109751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 110045,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 110096,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 110128,
        "cited_id": 246074,
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
    "date_created": "2026-07-04T20:53:09Z",
    "date_modified": "2026-07-06T07:26:24Z",
    "warnings": [
      "two-key identity check did not fully satisfy citation plus party text",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-04T20:56:59Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-04T20:53:33Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Brown v. Texas

```
<?xml version="1.0" encoding="utf-8"?>
<opinion type="majority">
<author id="b72-10">
  Mr. Chief Justice Burger
 </author>
<p id="AWL">
  delivered the opinion of the Court.
 </p>
<p id="b72-11">
  This appeal presents the question whether appellant was validly convicted for refusing to comply with a policeman’s demand that he identify himself pursuant to a provision of the Texas Penal Code which makes it a crime to refuse such identification on request.
 </p>
<p id="b72-12">
  I
 </p>
<p id="b72-13">
  At 12:45 in the afternoon of December 9, 1977, Officers Venegas and Sotelo of the El Paso Police Department were cruising in a patrol car. They observed appellant and another man walking in opposite directions away from one another in an alley. Although the two men were a few feet apart when they first were seen, Officer Venegas later testified that both officers believed the two had been together or were about to meet until the patrol car appeared.
 </p>
<p id="b72-14">
  The car entered the alley, and Officer Venegas got out and asked appellant to identify himself and explain what he was
  <span citation-index="1" class="star-pagination" label="49"> 
   *49
   </span>
  doing there. The other man was not questioned or detained. The officer testified that he stopped appellant because the situation “looked suspicious and we had never seen that subject in that area before.” The area of El Paso where appellant was stopped has a high incidence of drug traffic. However, the officers did not claim to suspect appellant of any specific misconduct, nor did they have any reason to believe that he was armed.
 </p>
<p id="b73-5">
  Appellant refused to identify himself and angrily asserted that the officers had no right to stop him. Officer Venegas replied that he was in a “high drug problem area”; Officer Sotelo then “frisked” appellant, but found nothing.
 </p>
<p id="b73-6">
  When appellant continued to refuse to identify himself, he was arrested for violation of Tex. Penal Code Ann., Tit. 8, § 38.02 (a) (1974), which makes it a criminal act for a person to refuse to give his name and address to an officer “who has lawfully stopped him and requested the information.”
  <a class="footnote" href="#fn1" id="fn1_ref">
   1
  </a>
  Following the arrest the officers searched appellant; nothing untoward was found.
 </p>
<p id="b73-7">
  While being taken to the El Paso County Jail appellant identified himself. Nonetheless, he was held in custody and charged with violating § 38.02 (a). When he was booked he was routinely searched a third time. Appellant was convicted in the El Paso Municipal Court and fined $20 plus court costs for violation of § 38.02. He then exercised his right under Texas law to a trial
  <em>
   de novo
  </em>
  in the El Paso County Court. There, he moved to set aside the information on the ground that § 38.02 (a) of the Texas Penal Code violated the First, Fourth, and Fifth Amendments and was unconstitutionally vague in violation of the Fourteenth Amendment. The
  <span citation-index="1" class="star-pagination" label="50"> 
   *50
   </span>
  motion was denied. Appellant waived a jury, and the court convicted him and imposed a fine of $45 plus court costs.
 </p>
<p id="b74-5">
  Under Texas law an appeal from an inferior court to a county court is subject to further review only if a fine exceeding $100 is imposed. Tex. Code Crim. Proc. Ann., Art. 4.03 (Vernon 1977). Accordingly, the County Courtis rejection of appellant's constitutional claims was a decision “by the highest court of a State in which a decision could be had.” <span class="citation no-link">28 U. S. C. § 1257</span> (2). On appeal here we noted probable jurisdiction. <span class="citation multiple-matches"><a href="/c/U.%20S./439/909/">439 U. S. 909</a></span> (1978). We reverse.
 </p>
<p id="b74-6">
  II
 </p>
<p id="b74-7">
  When the officers detained appellant for the purpose of requiring him to identify himself, they performed a seizure of his person subject to the requirements of the Fourth Amendment. In convicting appellant, the County Court necessarily found as a matter of fact that the officers “lawfully stopped” appellant. See Tex. Penal Code Ann., Tit. 8, § 38.02 (1974). The Fourth Amendment, of course, “applies to all seizures of the person, including seizures that involve only a brief detention short of traditional arrest.
  <em>
   Davis
  </em>
  v.
  <em>
   Mississippi,
  </em>
  <span class="citation" data-id="9424010"><a href="/opinion/107912/davis-v-mississippi/" aria-description="Citation for case: Davis v. Mississippi">394 U. S. 721</a></span> (1969);
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 16-19</a></span> (1968). ‘[W] hen ever a police officer accosts an individual and restrains his freedom to walk away, he has “seized” that person,’
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#16" aria-description="Citation for case: Terry v. Ohio"><em>
   id.,
  </em>
  at 16</a></span>, and the Fourth Amendment requires that the seizure be ‘reasonable.’ ”
  <em>
   United States
  </em>
  v.
  <em>
   Brignoni-Ponce,
  </em>
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 878</a></span> (1975).
 </p>
<p id="b74-8">
  The reasonableness of seizures that are less intrusive than a traditional arrest, see
  <em>
   Dunaway
  </em>
  v.
  <em>
   New York,
  </em>
  <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/#209" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200, 209-210</a></span> (1979);
  <em>
   Terry
  </em>
  v.
  <em>
   Ohio,
  </em>
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#20" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 20</a></span> (1968), depends “on a balance between the public interest and the individual’s right to personal security free from arbitrary interference by law officers.”
  <em>
   Pennsylvania
  </em>
  v.
  <em>
   Mimms,
  </em>
  <span class="citation" data-id="9427002"><a href="/opinion/109751/pennsylvania-v-mimms/#109" aria-description="Citation for case: Pennsylvania v. Mimms">434 U. S. 106, 109</a></span>
  <em>
   (1977); United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 878</a></span>. Consideration of the constitutionality of such seizures involves a
  <span citation-index="1" class="star-pagination" label="51"> 
   *51
   </span>
  weighing of the gravity of the public concerns served by the seizure, the degree to which the seizure advances the public interest, and the severity of the interference with individual liberty. See,
  <em>
   e. g.,
  </em>
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#878" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S., at 878-883</a></span>.
 </p>
<p id="b75-5">
  A central concern in balancing these competing considerations in a variety of settings has been to assure that an individual’s reasonable expectation of privacy is not subject to arbitrary invasions solely at the unfettered discretion of officers in the field. See
  <em>
   Delaware
  </em>
  v.
  <em>
   Prouse,
  </em>
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#654" aria-description="Citation for case: Delaware v. Prouse">440 U. S. 648, 654-655</a></span> (1979);
  <em>
   United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 882</a></span>. To this end, the Fourth Amendment requires that a seizure must be based on specific, objective facts indicating that society’s legitimate interests require the seizure of the particular individual, or that the seizure must be carried out pursuant to a plan embodying explicit, neutral limitations on the conduct of individual officers.
  <em>
   Delaware
  </em>
  v.
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 663</a></span>. See
  <em>
   United States
  </em>
  v.
  <em>
   Martinez-Fuerte,
  </em>
  <span class="citation" data-id="9426591"><a href="/opinion/109541/united-states-v-martinez-fuerte/#558" aria-description="Citation for case: United States v. Martinez-Fuerte">428 U. S. 543, 558-562</a></span> (1976).
 </p>
<p id="b75-6">
  The State does not contend that appellant was stopped pursuant to a practice embodying neutral criteria, but rather maintains that the officers were justified in stopping appellant because they had a “reasonable, articulable suspicion that a crime had just been, was being, or was about to be committed.” We have recognized that in some circumstances an officer may detain a suspect briefly for questioning although he does not have “probable cause” to believe that the suspect is involved in criminal activity, as is required for a traditional arrest.
  <em>
   United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#880" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 880-881</a></span>. See
  <em>
   Terry
  </em>
  v.
  <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#25" aria-description="Citation for case: Terry v. Ohio"><em>
   Ohio, supra,
  </em>
  at 25-26</a></span>. However, we have required the officers to have a reasonable suspicion, based on objective facts, that the individual is involved in criminal activity.
  <em>
   Delaware
  </em>
  v.
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#663" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 663</a></span>;
  <em>
   United States
  </em>
  v.
  <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#882" aria-description="Citation for case: United States v. Brignoni-Ponce"><em>
   Brignoni-Ponce, supra,
  </em>
  at 882-883</a></span>; see also
  <em>
   Lanzetta
  </em>
  v.
  <em>
   New Jersey,
  </em>
  <span class="citation" data-id="103170"><a href="/opinion/103170/lanzetta-v-new-jersey/" aria-description="Citation for case: Lanzetta v. New Jersey">306 U. S. 451</a></span> (1939),
 </p>
<p id="b75-7">
  The flaw in the State’s case is that none of the circum
  <span citation-index="1" class="star-pagination" label="52"> 
   *52
   </span>
  stances preceding the officers’ detention of appellant justified a reasonable suspicion that he was involved in criminal conduct. Officer Yenegas testified at appellant’s trial that the situation in the alley “looked suspicious,” but he was unable to point to any facts supporting that conclusion.
  <a class="footnote" href="#fn2" id="fn2_ref">
   2
  </a>
  There is no indication in the record that it was unusual for people to be in the alley. The fact that appellant was in a neighborhood frequented by drug users, standing alone, is not a basis for concluding that appellant himself was engaged in criminal conduct. In short, the appellant’s activity was no different from the activity of other pedestrians in that neighborhood. When pressed, Officer Venegas acknowledged that the only reason he stopped appellant was to ascertain his identity. The record suggests an understandable desire to assert a police presence; however, that purpose does not negate Fourth Amendment guarantees.
 </p>
<p id="b76-5">
  In the absence of any basis for suspecting appellant of misconduct, the balance between the public interest and appellant’s right to personal security and privacy tilts in favor of freedom from police interference. The Texas statute under which appellant was stopped and required to identify himself is designed to advance a weighty social objective in large metropolitan centers: prevention of crime. But even assuming that purpose is served to some degree by stopping and demanding identification from an individual without any specific basis for believing he is involved in criminal activity, the guarantees of the Fourth Amendment do not allow it. When such a stop is not based on objective criteria, the risk of arbitrary and abusive police practices exceeds tolerable limits. See
  <em>
   Delaware
  </em>
  v.
  <span class="citation" data-id="9427509"><a href="/opinion/110045/delaware-v-prouse/#661" aria-description="Citation for case: Delaware v. Prouse"><em>
   Prouse, supra,
  </em>
  at 661</a></span>.
 </p>
<p id="b77-4">
<span citation-index="1" class="star-pagination" label="53"> 
   *53
   </span>
  The application of Tex. Penal Code Ann., Tit. 8, § 38.02 (1974), to detain appellant and require him to identify himself violated the Fourth Amendment because the officers lacked any reasonable suspicion to believe appellant was engaged or had engaged in criminal conduct.
  <a class="footnote" href="#fn3" id="fn3_ref">
   3
  </a>
  Accordingly, appellant may not be punished for refusing to identify himself, and the conviction is
 </p>
<p id="b77-5">
<em>
   Reversed.
  </em>
</p>
<p id="b77-6">
  APPENDIX TO OPINION OF THE COURT
 </p>
<blockquote id="b77-7">
  “THE COURT: . . . What do you think about if you stop a person lawfully, and then if he doesn’t want to talk to you, you put him in jail for committing a crime.
 </blockquote>
<blockquote id="b77-8">
  “MR. PATTON [Prosecutor]: Well first of all, I would question the Defendant’s statement in his motion that the First Amendment gives an individual the right to silence.
 </blockquote>
<blockquote id="b77-9">
  “THE COURT: . . . I’m asking you why should the State put you in jail because you don’t want to say anything.
 </blockquote>
<blockquote id="b77-10">
  “MR. PATTON: Well, I think there’s certain interests that have to be viewed.
 </blockquote>
<blockquote id="b77-11">
  “THE COURT: Okay, I’d like you to tell me what those are.
 </blockquote>
<blockquote id="b77-12">
  “MR. PATTON: Well, the Governmental interest to maintain the safety and security of the society and the citizens to live in the society, and there are certainly strong Governmental interests in that direction and because of that, these interests outweigh the interests of an individual for a certain amount of intrusion upon his personal liberty. I think these Governmental interests outweigh the individual’s interests in
  <span citation-index="1" class="star-pagination" label="54"> 
   *54
   </span>
  this respect, as far as simply asking an individual for his name and address under the proper circumstances.
 </blockquote>
<blockquote id="b78-5">
  “THE COURT: But why should it be a crime to not answer?
 </blockquote>
<blockquote id="b78-6">
  “MR. PATTON: Again, I can only contend that if an answer is not given, it tends to disrupt.
 </blockquote>
<blockquote id="b78-7">
  “THE COURT: What does it disrupt?
 </blockquote>
<blockquote id="b78-8">
  “MR. PATTON: I think it tends to disrupt the goal of this society to maintain security over its citizens to make sure they are secure in their gains and their homes.
 </blockquote>
<blockquote id="b78-9">
  “THE COURT: How does that secure anybody by forcing them, under penalty of being prosecuted, to giving their name and address, even though they are lawfully stopped?
 </blockquote>
<blockquote id="b78-10">
  “MR. PATTON: Well I, you know, under the circumstances in which some individuals would be lawfully stopped, it’s presumed that perhaps this individual is up to something, and the officer is doing his duty simply to find out the individual’s name and address, and to determine what exactly is going on.
 </blockquote>
<blockquote id="b78-11">
  “THE COURT: I’m not questioning, I’m not asking whether the officer shouldn’t ask questions. I’m sure they should ask everything they possibly could find out.
  <em>
   What I’m asking is what’s the State’s interest in putting a man in jail because he doesn’t want to answer something.
  </em>
  I realize lots of times an officer will give a defendant a Miranda warning which means a defendant doesn’t have to make a statement. Lots of defendants go ahead and confess, which is fine if they want to do that. But if they don’t confess, you can’t put them in jail, can you, for refusing to confess to a crime?” App. 15-17 (emphasis added).
 </blockquote>



<div class="footnotes"><div class="footnote" id="fn1" label="1">
<a class="footnote" href="#fn1_ref">
   1
  </a>
<p id="b73-8">
   The entire section reads as follows:
  </p>
<p id="b73-9">
   “§ 38.02. Failure to Identify as Witness
  </p>
<p id="b73-10">
   “(a) A person commits an offense if he intentionally refuses to report or gives a false report of his name and residence address to a peace officer who has lawfully stopped him and requested the information.”
  </p>
</div><div class="footnote" id="fn2" label="2">
<a class="footnote" href="#fn2_ref">
   2
  </a>
<p id="b76-6">
   This situation is to be distinguished from the observations of a trained, experienced police officer who is able to perceive and articulate meaning in given conduct which would be wholly innocent to the untrained observer. See
   <em>
    United States
   </em>
   v.
   <em>
    Brignoni-Ponce,
   </em>
   <span class="citation" data-id="9426196"><a href="/opinion/109311/united-states-v-brignoni-ponce/#884" aria-description="Citation for case: United States v. Brignoni-Ponce">422 U. S. 873, 884-885</a></span> (1975);
   <em>
    Christensen
   </em>
   v.
   <em>
    United States,
   </em>
   104 U. S. App. D. C. 35, 36, 259 E. 2d 192, 193 (1958).
  </p>
</div><div class="footnote" id="fn3" label="3">
<a class="footnote" href="#fn3_ref">
   3
  </a>
<p id="b77-13">
   We need not decide whether an individual may be punished for refusing to identify himself in the context of a lawful investigatory stop which satisfies Fourth Amendment requirements. See
   <em>
    Dunaway
   </em>
   v.
   <em>
    New York,
   </em>
   <span class="citation" data-id="9427599"><a href="/opinion/110096/dunaway-v-new-york/" aria-description="Citation for case: Dunaway v. New York">442 U. S. 200</a></span>, 210 n. 12 (1979);
   <em>
    Terry
   </em>
   v.
   <em>
    Ohio,
   </em>
   <span class="citation" data-id="9423752"><a href="/opinion/107729/terry-v-ohio/#34" aria-description="Citation for case: Terry v. Ohio">392 U. S. 1, 34</a></span> (1968) (White, J., concurring). The County Court Judge who convicted appellant was troubled by this question, as shown by the colloquy set out in the Appendix to this opinion.
  </p>
</div></div></opinion>
```

---
