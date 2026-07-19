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

## GROUP: content/cases/Wearry v. Cain.md  (`case`, 5 assertions)

### content_page

```
---
title: "Wearry v. Cain"
type: case
citation: ""
parallel_cite: "577 U.S. 385; 136 S. Ct. 1002; 194 L. Ed. 2d 78; 84 U.S.L.W. 4125; 26 Fla. L. Weekly Fed. S 17"
neutral_cite: "2016 U.S. LEXIS 1654; 2016 WL 854158"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2016
date_decided: 2016-03-07
docket: ""
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2016-03-07
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wearry v. Cain
  varies_by_point: false
  scope_note: "Per curiam; reaffirms cumulative Brady materiality. Good law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/3183098/wearry-v-cain/"
  cluster_id: 3183098
  opinion_id: 3183080
  identity_checked: true
homes:
  - page: "[[Brady and Giglio]]"
    role: "Key — Progeny / Refinement"
related: ["[[Brady v. Maryland]]", "[[Kyles v. Whitley]]", "[[Smith v. Cain]]", "[[Giglio v. United States]]"]
aliases: ["Wearry"]
tags: ["case", "due-process", "brady", "materiality", "impeachment", "per-curiam"]
holding: "Reaffirms cumulative *Brady* materiality: suppressed evidence assessed collectively undermined confidence in the verdict."
lake:
  record_id: Wearry v. Cain
  status: verified
  projected_at: 2026-07-09
---

# Wearry v. Cain

*577 U.S. 385 (2016)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Michael Wearry was convicted of capital murder and sentenced to death almost entirely on the testimony of two witnesses, Scott (a prison informant) and Brown. On collateral review it emerged that the State had failed to disclose evidence impeaching both: that Scott had coached another inmate to lie about the murder, that a third man (Hutchinson) may have been physically unable to perform the role Scott described, that Scott may have implicated Wearry to settle a personal score, that Brown had twice sought a deal to reduce his own sentence, and medical records casting doubt on a witness's account of Wearry's running. The state postconviction court denied relief, finding no prejudice.

## Issue
Whether the State's suppression of evidence impeaching its key witnesses was material under *[[Brady v. Maryland]]*, requiring a new trial, where the evidence must be assessed cumulatively rather than item by item.

## Rule
Suppressed favorable evidence violates due process when it is material, and materiality is measured generously: "Evidence qualifies as material when there is "'any reasonable likelihood'" it could have "'affected the judgment of the jury.'"" — 136 S. Ct. at 1006. ^pin-1006

The defendant's burden is confidence-based, not preponderance-based: "He must show only that the new evidence is sufficient to 'undermine confidence' in the verdict." — *Id.* ^pin-1006a

And materiality must be assessed collectively — the court must conduct a "cumulative evaluation" of the suppressed evidence rather than gauge each piece "in isolation." — [*Id.* at 1007](https://www.courtlistener.com/opinion/3183098/wearry-v-cain/#:~:text=cumulative%20evaluation). ^pin-1007

## Application
On these facts the prosecution's case "resemble[d] a house of cards, built on the jury crediting Scott's account rather than Wearry's alibi." — 136 S. Ct. at 1006. ^pin-1006b

The withheld evidence went directly to the credibility of the only witnesses tying Wearry to the murder: it would have shown Scott coached a false story and had a motive to lie, that the role he assigned a confederate may have been physically impossible, and that Brown was angling for a sentence reduction. The state court compounded its error by weighing each item separately. Considered cumulatively, that evidence was enough to undermine confidence in the verdict, establishing a *[[Brady v. Maryland|Brady]]* violation.

## Conclusion
The suppressed impeachment evidence was material; its cumulative weight undermined confidence in the verdict. The Court reversed and [[Reading and Citing Cases#on-remand|remanded]] for a new trial without reaching Wearry's ineffective-assistance claim.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** (per curiam).
- No negative treatment. *Wearry* applies the materiality standard of [[Brady v. Maryland]] and [[Giglio v. United States]], reaffirms the "cumulative evaluation" command of [[Kyles v. Whitley]], and tracks the confidence-in-the-verdict analysis of [[Smith v. Cain]].

## Appears on
- [[Brady and Giglio]] — *Key — Progeny / Refinement*

## Sources
- *Wearry v. Cain*, 577 U.S. 385 (2016) — https://www.courtlistener.com/opinion/3183098/wearry-v-cain/ — pinpoints given to the parallel S. Ct. reporter (CourtListener star-paginates *Wearry* by 136 S. Ct.): 1006, 1007. Cluster 3183098 → opinion 3183080.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "30131ff6f6e0fcc3", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2016 U.S. LEXIS 1654; 2016 WL 854158", "official_citation_present": false, "parallel_cite": "577 U.S. 385; 136 S. Ct. 1002; 194 L. Ed. 2d 78; 84 U.S.L.W. 4125; 26 Fla. L. Weekly Fed. S 17", "title": "Wearry v. Cain", "year": "2016"}}
{"assertion_id": "a6a8534f64d8dafd", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Reaffirms cumulative *Brady* materiality: suppressed evidence assessed collectively undermined confidence in the verdict.", "title": "Wearry v. Cain"}}
{"assertion_id": "b5a39f871e82f7e5", "dimension": "support", "kind": "home_role", "locator": {"home": "Brady and Giglio"}, "payload": {"home": "Brady and Giglio", "role": "Key — Progeny / Refinement", "title": "Wearry v. Cain"}}
{"assertion_id": "71d1152803e1d60a", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2016-03-07", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wearry v. Cain", "field_i_validity": "good_law", "scope_note": "Per curiam; reaffirms cumulative Brady materiality. Good law.", "title": "Wearry v. Cain", "varies_by_point": "false"}}
{"assertion_id": "841c3ba552d24783", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Wearry v. Cain"}}
```

### lake record — Wearry v. Cain

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wearry v. Cain",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wearry v. Cain",
    "case_name_short": "Wearry",
    "case_name_full": "Michael WEARRY v. Burl CAIN, Warden.",
    "input_case_name": "Wearry v. Cain",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2016-03-07",
    "year": 2016,
    "docket": null,
    "cluster_id": 3183098,
    "lead_opinion_id": 3183080,
    "sibling_ids": [
      3183080
    ],
    "absolute_url": "/opinion/3183098/wearry-v-cain/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "577 U.S. 385",
        "volume": "577",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 1002",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "1002",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "194 L. Ed. 2d 78",
        "volume": "194",
        "reporter": "L. Ed. 2d",
        "page": "78",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4125",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4125",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 17",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2016 U.S. LEXIS 1654",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "1654",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 854158",
        "volume": "2016",
        "reporter": "WL",
        "page": "854158",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "577 U.S. 385",
        "volume": "577",
        "reporter": "U.S.",
        "page": "385",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "136 S. Ct. 1002",
        "volume": "136",
        "reporter": "S. Ct.",
        "page": "1002",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "194 L. Ed. 2d 78",
        "volume": "194",
        "reporter": "L. Ed. 2d",
        "page": "78",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 U.S. LEXIS 1654",
        "volume": "2016",
        "reporter": "U.S. LEXIS",
        "page": "1654",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "84 U.S.L.W. 4125",
        "volume": "84",
        "reporter": "U.S.L.W.",
        "page": "4125",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 17",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "17",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2016 WL 854158",
        "volume": "2016",
        "reporter": "WL",
        "page": "854158",
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
      "id": "pin-1006",
      "page": null,
      "quote": "--- # Wearry v. Cain *577 U.S. 385 (2016)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background Michael Wearry was convicted of capital murder and sentenced to death almost entirely on the testimony of two witnesses, Scott (a prison informant) and Brown. On collateral review it emerged that the State had failed to disclose evidence impeaching both: that Scott had coached another inmate to lie about the murder, that a third man (Hutchinson) may have been physically unable to perform the role Scott described, that Scott may have implicated Wearry to settle a personal score, that Brown had twice sought a deal to reduce his own sentence, and medical records casting doubt on a witness's account of Wearry's running. The state postconviction court denied relief, finding no prejudice. ## Issue Whether the State's suppression of evidence impeaching its key witnesses was material under *Brady v. Maryland*, requiring a new trial, where the evidence must be assessed cumulatively rather than item by item. ## Rule Suppressed favorable evidence violates due process when it is material, and materiality is measured generously:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1006a",
      "page": null,
      "quote": "He must show only that the new evidence is sufficient to 'undermine confidence' in the verdict.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-1007",
      "page": null,
      "quote": "cumulative evaluation",
      "star_marker": null,
      "quote_fidelity": "matched",
      "pinpoint_status": "slip-only",
      "position": 17776,
      "fragment": "#:~:text=cumulative%20evaluation",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    },
    {
      "id": "pin-1006b",
      "page": null,
      "quote": "resemble[d] a house of cards, built on the jury crediting Scott's account rather than Wearry's alibi.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2016-03-07",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wearry v. Cain",
    "varies_by_point": false,
    "scope_note": "Per curiam; reaffirms cumulative Brady materiality. Good law.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Joseph Prystash v. Lorie Davis, Director",
          "cluster_id": 4386207,
          "cite": [
            "854 F.3d 830",
            "2017 WL 1487229",
            "2017 U.S. App. LEXIS 7365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Dennis v. Secretary, Pennsylvania Department of Corrections",
          "cluster_id": 4250271,
          "cite": [
            "834 F.3d 263",
            "2016 U.S. App. LEXIS 15434",
            "2016 WL 4440925"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Armstrong v. Ashley",
          "cluster_id": 9375737,
          "cite": [
            "60 F.4th 262"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Refugio Ruiz-Cortez v. Glenn Lewellen",
          "cluster_id": 4643210,
          "cite": [
            "931 F.3d 592"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Genesis Hill v. Betty Mitchell",
          "cluster_id": 4326477,
          "cite": [
            "842 F.3d 910",
            "2016 FED App. 0281P",
            "96 Fed. R. Serv. 3d 131",
            "2016 U.S. App. LEXIS 21458"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Commonwealth v. Natividad, R., Aplt.",
          "cluster_id": 4583669,
          "cite": [
            "200 A.3d 11"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Floyd v. Darrel Vannoy, Warden",
          "cluster_id": 4510860,
          "cite": [
            "894 F.3d 143"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Freddie McNeill, Jr. v. Margaret Bagley",
          "cluster_id": 4987267,
          "cite": [
            "10 F.4th 588"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Paul Browning v. Renee Baker",
          "cluster_id": 4427560,
          "cite": [
            "875 F.3d 444"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ex parte Chaney",
          "cluster_id": 6243270,
          "cite": [
            "563 S.W.3d 239"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Walter Liew",
          "cluster_id": 4389310,
          "cite": [
            "856 F.3d 585",
            "2017 WL 1753269"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Glossip v. Oklahoma",
          "cluster_id": 10339023,
          "cite": [
            "604 U.S. 226"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McCray v. Capra",
          "cluster_id": 7857399,
          "cite": [
            "45 F.4th 634"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. John Ausby",
          "cluster_id": 4595449,
          "cite": [
            "916 F.3d 1089"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Wearry v. Foster",
          "cluster_id": 6465433,
          "cite": [
            "33 F.4th 260"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Sepulveda",
          "cluster_id": 9389969,
          "cite": [
            "64 F.4th 700"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Jimenez",
          "cluster_id": 4240628,
          "cite": [
            "142 A.D.3d 149",
            "37 N.Y.S.3d 225"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Davel Chinn v. Warden, Chillicothe Corr. Inst.",
          "cluster_id": 6251617,
          "cite": [
            "24 F.4th 1096"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pennsylvania State Conference of NAACP Branches v. Northampton County Board of Elections",
          "cluster_id": 9488671,
          "cite": [
            "97 F.4th 120"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Solorio v. Muniz",
          "cluster_id": 9022945,
          "cite": [
            "896 F.3d 914"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "State v. Hill",
          "cluster_id": 4587704,
          "cite": [
            "2019 Ohio 365"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Brumfield",
          "cluster_id": 9454987,
          "cite": [
            "89 F.4th 506"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony Juniper v. Melvin Davis",
          "cluster_id": 9414861,
          "cite": [
            "74 F.4th 196"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kuantau Reeder v. Darrel Vannoy, Warden",
          "cluster_id": 4798511,
          "cite": [
            "978 F.3d 272"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "John Floyd v. Darrel Vannoy, Warden",
          "cluster_id": 4484952,
          "cite": [
            "887 F.3d 214"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wearry v. Cain:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(3183080) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 64,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 64,
        "triage_read": 1,
        "triage_snippet_classified": 63
      },
      "lane2_top_cited": {
        "query": "cites:(3183080)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0wJnM9MTA2OTU0MjYmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%283183080%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(3183080)",
        "reviewed": 13,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 13,
        "triage_read": 0,
        "triage_snippet_classified": 13
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(3183080)",
    "indexed_citing_opinions": 78,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 3183080,
        "count": 78,
        "count_source": "search"
      }
    ],
    "citation_count": 202,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wearry-v-cain.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjc4ODIzMjMmcz05NDA0ODc5JnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%283183080%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 3183080,
        "cited_id": 1756,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 105912,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 106598,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 108471,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 109506,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 111514,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 111662,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 117923,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 121158,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 145639,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 145759,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 149653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 620666,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 3183080,
        "cited_id": 1129223,
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
    "date_created": "2026-07-06T04:08:42Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:08:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:08:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:11:06Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:08:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wearry v. Cain

```
                 Cite as: 577 U. S. ____ (2016)            1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
     MICHAEL WEARRY v. BURL CAIN, WARDEN
  ON PETITION FOR WRIT OF CERTIORARI TO THE DISTRICT
        COURT OF LOUISIANA, LIVINGSTON PARISH
             No. 14–10008.   Decided March 7, 2016

  PER CURIAM.
  Michael Wearry is on Louisiana’s death row. Urging
that the prosecution failed to disclose evidence supporting
his innocence and that his counsel provided ineffective
assistance at trial, Wearry unsuccessfully sought postcon-
viction relief in state court. Contrary to the state postcon-
viction court, we conclude that the prosecution’s failure to
disclose material evidence violated Wearry’s due process
rights. We reverse the state postconviction court’s judg-
ment on that account, and therefore do not reach Wearry’s
ineffective-assistance-of-counsel claim.
                              I
                             A
  Sometime between 8:20 and 9:30 on the evening of April
4, 1998, Eric Walber was brutally murdered. Nearly two
years after the murder, Sam Scott, at the time incarcer-
ated, contacted authorities and implicated Michael Wearry.
Scott initially reported that he had been friends with
the victim; that he was at work the night of the murder;
that the victim had come looking for him but had instead
run into Wearry and four others; and that Wearry and the
others had later confessed to shooting and driving over the
victim before leaving his body on Blahut Road. In fact, the
victim had not been shot, and his body had been found on
Crisp Road.
  Scott changed his account of the crime over the course of
four later statements, each of which differed from the
others in material ways. By the time Scott testified as the
2                     WEARRY v. CAIN

                         Per Curiam

State’s star witness at Wearry’s trial, his story bore little
resemblance to his original account. According to the
version Scott told the jury, he had been playing dice with
Wearry and others when the victim drove past. Wearry,
who had been losing, decided to rob the victim. After
Wearry and an acquaintance, Randy Hutchinson, stopped
the victim’s car, Hutchinson shoved the victim into the
cargo area. Five men, including Scott, Hutchinson, and
Wearry, proceeded to drive around, at one point encoun-
tering Eric Brown—the State’s other main witness—and
pausing intermittently to assault the victim. Finally,
Scott related, Wearry and two others killed the victim by
running him over. On cross-examination, Scott admitted
that he had changed his account several times.
   Consistent with Scott’s testimony, Brown testified that
on the night of the murder he had seen Wearry and others
with a man who looked like the victim. Incarcerated on
unrelated charges at the time of Wearry’s trial, Brown
acknowledged that he had made a prior inconsistent
statement to the police, but had recanted and agreed to
testify against Wearry, not for any prosecutorial favor, but
solely because his sister knew the victim’s sister. The
State commented during its opening argument that Brown
“is doing 15 years on a drug charge right now, [but] hasn’t
asked for a thing.” 7 Record 1723 (Tr., Mar. 2, 2002).
During closing argument, the State reiterated that Brown
“has no deal on the table” and was testifying because the
victim’s “family deserves to know.” Pet. for Cert. 19.
   Although the State presented no physical evidence at
trial, it did offer additional circumstantial evidence link-
ing Wearry to the victim. One witness testified that he
saw Wearry in the victim’s car on the night of the murder
and, later, holding the victim’s class ring. Another wit-
ness said he saw Wearry throwing away the victim’s co-
logne. In some respects, however, these witnesses contra-
dicted Scott’s account. For example, the witness who
                     Cite as: 577 U. S. ____ (2016)                    3

                              Per Curiam

reported seeing Wearry in the victim’s car did not place
Scott in the car.
   Wearry’s defense at trial rested on an alibi. He claimed
that, at the time of the murder, he had been at a wedding
reception in Baton Rouge, 40 miles away. Wearry’s girl-
friend, her sister, and her aunt corroborated Wearry’s
account. In closing argument, the State stressed that all
three witnesses had personal relationships with Wearry.
The State also presented two rebuttal witnesses: the bride
at the wedding, who reported that the reception had ended
by 8:30 or 9:00 (potentially leaving sufficient time for
Wearry to have committed the crime); and three jail em-
ployees, who testified that they had overheard Wearry say
that he was a bystander when the crime occurred.
   The jury convicted Wearry of capital murder and sen-
tenced him to death. His conviction and sentence were
affirmed on direct appeal. 1
                              B
   After Wearry’s conviction became final, it emerged that
the prosecution had withheld relevant information that
could have advanced Wearry’s plea. Wearry argued dur-
ing state postconviction proceedings that three categories
of belatedly revealed information would have undermined
the prosecution and materially aided Wearry’s defense at
trial.
   First, previously undisclosed police records showed that
two of Scott’s fellow inmates had made statements that
cast doubt on Scott’s credibility. One inmate had reported
——————
  1 Wearry argued, inter alia, that the trial court improperly denied his

for-cause challenges, and that the prosecution discriminated on the
basis of race in jury selection in violation of Batson v. Kentucky, 476
U. S. 79 (1986). Finding both jury-selection claims credible, then-
Justice Johnson dissented from the affirmance of Wearry’s conviction.
State v. Weary, 2003–3067 (La. 4/2/06), 931 So. 2d 297, 328–337.
(Wearry’s name is misspelled in the direct-appeal case caption.)
4                           WEARRY v. CAIN

                               Per Curiam

hearing Scott say that he wanted to “ ‘make sure [Wearry]
gets the needle cause he jacked over me.’ ” Id., at 22 (quot-
ing inmate affidavit). 2 The other inmate had told investi-
gators—at a meeting Scott orchestrated—that he had
witnessed the murder, but this inmate recanted the next
day. “Scott had told him what to say,” he explained, and
had suggested that lying about having witnessed the
murder “would help him get out of jail.” Pet. Exh. 13 in
No. 01–FELN–015992, pp. 104, 107. See also Pet. for
Cert. 22 (quoting police notes).
  Second, the State had failed to disclose that, contrary to
the prosecution’s assertions at trial, Brown had twice
——————
    2 Illustrative
                 of the liberties the dissent takes with the record is the
assertion that “Scott blamed [Wearry] for putting him in the position of
having to admit his own role in the events surrounding the murder.”
Post, at 2 (opinion of ALITO, J.). Introducing the inmate’s statement,
the dissent therefore suggests, might have “backfired by allowing the
prosecution to return the jury’s focus to a point the State emphasized
often during trial, namely, that Scott’s accusations were credible
precisely because Scott had no motive to tell a story that was contrary
to his own interests.” Id., at 2–3. True, according to the inmate, Scott
had complained that his identification of Wearry had resulted in a
lengthier prison term. The inmate, however, did not suggest that Scott
was angry with Wearry because he had suffered adverse consequences
as a result of Wearry’s crime. Instead, the inmate separately stated
that Scott “wouldn’t tell me who did it”—i.e., who killed Eric Walber—
“but he said I’m gonna make sure Mike gets the needle cause he jacked
over me.” Pet. Exh. 13 in No. 01–FELN–015992, p. 103. See also ibid.
(“If [Scott] would have told me who did this I would tell because I have
a heart and what they did wasn’t right”). Scott’s refusal to identify
Wearry as the culprit—while also endeavoring to “make sure Mike gets
the needle,” ibid.—suggests that Wearry did not commit the crime, but
Scott had decided to bring him down anyway. Nor, contrary to the
dissent, is there any reason to believe that Scott anticipated his partic-
ipation in this case would cost him additional years in prison. Notably,
in the first of his five accounts to police, Scott reported that he had not
been present at the time of the murder and had learned about it only
after the fact. Indeed, it is at least as plausible as the dissent’s hypoth-
esis that Scott believed implicating Wearry might win him early release
on his existing conviction.
                     Cite as: 577 U. S. ____ (2016)                    5

                              Per Curiam

sought a deal to reduce his existing sentence in exchange
for testifying against Wearry. The police had told Brown
that they would “ ‘talk to the D. A. if he told the truth.’ ”
Pet. for Cert. 19 (quoting police notes).
   Third, the prosecution had failed to turn over medical
records on Randy Hutchinson. According to Scott, on the
night of the murder, Hutchinson had run into the street to
flag down the victim, pulled the victim out of his car,
shoved him into the cargo space, and crawled into the
cargo space himself. But Hutchinson’s medical records
revealed that, nine days before the murder, Hutchinson
had undergone knee surgery to repair a ruptured patellar
tendon. Id., at 10–11, 15–16, 32. 3 An expert witness, Dr.
Paul Dworak, testified at the state collateral-review hear-
ing that Hutchinson’s surgically repaired knee could not
have withstood running, bending, or lifting substantial
weight. The State presented an expert witness who disa-
greed with Dr. Dworak’s appraisal of Hutchinson’s physi-
cal fitness.
   During state postconviction proceedings, Wearry also
maintained that his trial attorney had failed to uncover
exonerating evidence. Wearry’s trial attorney admitted at
the state collateral-review hearing that he had conducted
no independent investigation into Wearry’s innocence and
had relied solely on evidence the State and Wearry had
provided. 4 For example, despite Wearry’s alibi, his attor-
——————
  3 The  dissent emphasizes a State’s witness’ testimony that
“Hutchinson had had surgery on his knee ‘about nine days before the
homicide happened.’ ” Post, at 4 (quoting 10 Record 2261 (Tr., Mar. 5,
2002)). But from this witness’ statement, neither Wearry nor the jury
had any way of knowing what the medical records would have revealed:
Hutchinson had undergone a patellar-tendon repair rather than a
routine minor procedure.
  4 Wearry’s trial attorney did ask the public defender’s investigator to

look into the backgrounds of the State’s witnesses and to speak with
Wearry’s family members. But the attorney testified at the collateral-
review hearing that he did not know what persons the investigator
6                          WEARRY v. CAIN

                              Per Curiam

ney undertook no effort to locate independent witnesses
from among the dozens of guests who had attended the
wedding reception.
   Counsel representing Wearry on collateral review con-
ducted an independent investigation. This investigation
revealed many witnesses lacking any personal relation-
ship with Wearry who would have been willing to corrobo-
rate his alibi had they been called at trial. Collateral-
review counsel’s investigation also revealed that Scott’s
brother and sister-in-law would have been willing to tes-
tify at trial, as they did at the collateral-review hearing,
that Scott was with them, mostly at a strawberry festival,
until around 11:00 on the night of the murder.
   Based on this new evidence, Wearry alleged violations of
his due process rights under Brady v. Maryland, 373 U. S.
83 (1963), and of his Sixth Amendment right to effective
assistance of counsel. Acknowledging that the State
“probably ought to have” disclosed the withheld evidence,
App. to Pet. for Cert. B–6, and that Wearry’s counsel
provided “perhaps not the best defense that could have
been rendered,” id., at B–5, the postconviction court de-
nied relief. Even if Wearry’s constitutional rights were
violated, the court concluded, he had not shown prejudice.
Id., at B–5, B–7. In turn, the Louisiana Supreme Court
also denied relief. Id., at A–1. Chief Justice Johnson
would have granted Wearry’s petition on the ground that
he received ineffective assistance of counsel. Id., at A–2. 5

——————
contacted and, in any event, he had serious doubts about the investiga-
tor’s qualifications and competence. Moreover, there is no indication
that the investigator ever engaged in inquiries regarding Scott’s back-
ground or his whereabouts on the night of the murder.
  5 Justice Crichton would have granted Wearry’s petition and remanded

for the trial court to address his claim of intellectual disability under
Atkins v. Virginia, 536 U. S. 304 (2002). App. to Pet. for Cert. A–15.
Wearry does not raise his Atkins claim in his petition for a writ of
certiorari.
                     Cite as: 577 U. S. ____ (2016)                    7

                              Per Curiam

                              II
   Because we conclude that the Louisiana courts’ denial of
Wearry’s Brady claim runs up against settled constitu-
tional principles, and because a new trial is required as a
result, we need not and do not consider the merits of his
ineffective-assistance-of-counsel claim. “[T]he suppression
by the prosecution of evidence favorable to an accused
upon request violates due process where the evidence is
material either to guilt or to punishment, irrespective of
the good faith or bad faith of the prosecution.” Brady,
supra, at 87. See also Giglio v. United States, 405 U. S.
150, 153–154 (1972) (clarifying that the rule stated in
Brady applies to evidence undermining witness credibil-
ity). Evidence qualifies as material when there is “ ‘any
reasonable likelihood’ ” it could have “ ‘affected the judg-
ment of the jury.’ ” Giglio, supra, at 154 (quoting Napue v.
Illinois, 360 U. S. 264, 271 (1959)). To prevail on his
Brady claim, Wearry need not show that he “more likely
than not” would have been acquitted had the new evidence
been admitted. Smith v. Cain, 565 U. S. 73, ___–___
(2012) (slip op., at 2–3) (internal quotation marks and
brackets omitted). He must show only that the new evi-
dence is sufficient to “undermine confidence” in the ver-
dict. Ibid. 6
   Beyond doubt, the newly revealed evidence suffices to
undermine confidence in Wearry’s conviction. The State’s
trial evidence resembles a house of cards, built on the jury
crediting Scott’s account rather than Wearry’s alibi. See
United States v. Agurs, 427 U. S. 97, 113 (1976) (“[I]f the
verdict is already of questionable validity, additional
evidence of relatively minor importance might be suffi-
cient to create a reasonable doubt.”). The dissent asserts
——————
  6 Given this legal standard, Wearry can prevail even if, as the dissent

suggests, the undisclosed information may not have affected the jury’s
verdict.
8                          WEARRY v. CAIN

                               Per Curiam

that, apart from the testimony of Scott and Brown, there
was independent evidence pointing to Wearry as the mur-
derer. See post, at 5 (opinion of ALITO, J.). But all of the
evidence the dissent cites suggests, at most, that someone
in Wearry’s group of friends may have committed the
crime, and that Wearry may have been involved in events
related to the murder after it occurred. Perhaps, on the
basis of this evidence, Louisiana might have charged
Wearry as an accessory after the fact. La. Rev. Stat. Ann.
§14:25 (West 2007) (providing a maximum prison term of
five years for accessories after the fact). But Louisiana
instead charged Wearry with capital murder, and the only
evidence directly tying him to that crime was Scott’s dubi-
ous testimony, corroborated by the similarly suspect tes-
timony of Brown. 7
   As the dissent recognizes, “Scott did not have an exem-
plary record of veracity.” Post, at 3. Scott’s credibility,
already impugned by his many inconsistent stories, would
have been further diminished had the jury learned that
Hutchinson may have been physically incapable of per-
forming the role Scott ascribed to him, that Scott had
coached another inmate to lie about the murder and
thereby enhance his chances to get out of jail, or that Scott
may have implicated Wearry to settle a personal score. 8
——————
  7 As for the three jailers who testified to overhearing Wearry call

himself an “innocent bystander,” post, at 4, so characterizing oneself is
the opposite of an admission of guilt.
  8 Because the inmate who told police that Scott may have wanted to

settle a score did so close to the end of trial, the State argues, the
inmate’s “statement was probably . . . never seen by anyone involved
with the actual trial until . . . it was [all] over, i[f] at all.” Brief in
Opposition 18. But “Brady suppression occurs when the government
fails to turn over even evidence that is known only to police investiga-
tors and not to the prosecutor.” Youngblood v. West Virginia, 547 U. S.
867, 869–870 (2006) (per curiam) (internal quotation marks omitted).
See also Kyles v. Whitley, 514 U. S. 419, 438 (1995) (rejecting Louisi-
ana’s plea for a rule that would not hold the State responsible for
                     Cite as: 577 U. S. ____ (2016)                     9

                              Per Curiam

Moreover, any juror who found Scott more credible in light
of Brown’s testimony might have thought differently had
she learned that Brown may have been motivated to come
forward not by his sister’s relationship with the victim’s
sister—as the prosecution had insisted in its closing ar-
gument—but by the possibility of a reduced sentence on
an existing conviction. See Napue, supra, at 270 (even
though the State had made no binding promises, a wit-
ness’ attempt to obtain a deal before testifying was mate-
rial because the jury “might well have concluded that [the
witness] had fabricated testimony in order to curry the
[prosecution’s] favor”). Even if the jury—armed with all of
this new evidence—could have voted to convict Wearry, we
have “no confidence that it would have done so.” Smith,
supra, at ___ (slip op., at 3).
   Reaching the opposite conclusion, the state postconvic-
tion court improperly evaluated the materiality of each
piece of evidence in isolation rather than cumulatively, see
Kyles v. Whitley, 514 U. S. 419, 441 (1995) (requiring a
“cumulative evaluation” of the materiality of wrongfully
withheld evidence), emphasized reasons a juror might
disregard new evidence while ignoring reasons she might
not, cf. Porter v. McCollum, 558 U. S. 30, 43 (2009) (per
curiam) (“it was not reasonable to discount entirely the
effect that [a defendant’s expert’s] testimony might have
had on the jury” just because the State’s expert provided
contrary testimony), and failed even to mention the state-
ments of the two inmates impeaching Scott.
                             III
  In addition to defending the judgment of the Louisiana
courts, the dissent criticizes the Court for deciding this
“intensely factual question . . . without full briefing and
——————
failing to disclose exculpatory evidence about which prosecutors did not
learn until after trial when that evidence was in the possession of police
investigators at the time of trial).
10                     WEARRY v. CAIN

                          Per Curiam

argument.” Post, at 6. But the Court has not shied away
from summarily deciding fact-intensive cases where, as
here, lower courts have egregiously misapplied settled
law. See, e.g., Mullenix v. Luna, ante, at ___ (per
curiam); Stanton v. Sims, 571 U. S. ___ (2013) (per curiam);
Parker v. Matthews, 567 U. S. ___ (2012) (per curiam);
Coleman v. Johnson, 566 U. S. ___ (2012) (per curiam);
Wetzel v. Lambert, 565 U. S. ___ (2012) (per curiam);
Ryburn v. Huff, 565 U. S. ___ (2012) (per curiam); Sears v.
Upton, 561 U. S. 945 (2010) (per curiam); Porter v.
McCollum, supra.
   Because “[t]he petition does not . . . fall into a category
in which the Court has previously evinced an inclination
to police factbound errors,” the dissent continues, “nothing
warned the State,” when it was drafting its brief in opposi-
tion, that the Court might summarily reverse Wearry’s
conviction. Post, at 5–6. Contrary to the dissent, however,
summarily deciding a capital case, when circumstances so
warrant, is hardly unprecedented. See Sears, supra, at
951–952 (vacating a state postconviction court’s denial of
relief on a penalty-phase ineffective-assistance-of-counsel
claim); Porter, supra, at 38–40 (attorney provided ineffec-
tive assistance of counsel by conducting a constitutionally
inadequate investigation into mitigating evidence). Per-
haps anticipating the possibility of summary reversal, the
State devoted the bulk of its 30-page brief in opposition to
a point-by-point rebuttal of Wearry’s claims. Given this
brief, as well as the State’s lower court filings similarly
concentrating on evidence supporting its position, the
chances that further briefing or argument would change
the outcome are vanishingly slim.
   The dissent also inveighs against the Court’s “de-
part[ure] from our usual procedures . . . [to] decide peti-
tioner’s fact-intensive Brady claim at this stage . . . [rather
than] allow[ing] petitioner to raise that claim in a federal
habeas proceeding.” Post, at 7. This Court, of course, has
                 Cite as: 577 U. S. ____ (2016)                 11

                          Per Curiam

jurisdiction over the final judgments of state postconvic-
tion courts, see 28 U. S. C. §1257(a), and exercises that
jurisdiction in appropriate circumstances. Earlier this
Term, for instance, we heard argument in Foster v. Chat-
man, No. 14–8349, which involves the Georgia courts’
denial of postconviction relief to a capital defendant rais-
ing a claim under Batson v. Kentucky, 476 U. S. 79 (1986).
See also Smith, 565 U. S., at ___ (slip op., at 2) (reversing
a state postconviction court’s denial of relief on a Brady
claim); Sears, supra, at 946. Reviewing the Louisiana
courts’ denial of postconviction relief is thus hardly the
bold departure the dissent paints it to be. The alternative
to granting review, after all, is forcing Wearry to endure
yet more time on Louisiana’s death row in service of a
conviction that is constitutionally flawed.
                       *     *    *
  Because Wearry’s due process rights were violated, we
grant his petition for a writ of certiorari and motion for
leave to proceed in forma pauperis, reverse the judgment
of the Louisiana postconviction court, and remand for
further proceedings not inconsistent with this opinion.

                                                  It is so ordered.
                 Cite as: 577 U. S. ____ (2016)           1

                     ALITO, J., dissenting

SUPREME COURT OF THE UNITED STATES
     MICHAEL WEARRY v. BURL CAIN, WARDEN
  ON PETITION FOR WRIT OF CERTIORARI TO THE DISTRICT
        COURT OF LOUISIANA, LIVINGSTON PARISH
             No. 14–10008.   Decided March 7, 2016

   JUSTICE ALITO, with whom JUSTICE THOMAS joins,
dissenting.
   Without briefing or argument, the Court reverses a 14-
year-old murder conviction on the ground that the prose-
cution violated Brady v. Maryland, 373 U. S. 83 (1963), by
failing to turn over certain information that tended to
exculpate petitioner. There is no question in my mind
that the prosecution should have disclosed this infor-
mation, but whether the information was sufficient to
warrant reversing petitioner’s conviction is another mat-
ter. The failure to turn over exculpatory information
violates due process only “ ‘if there is a reasonable proba-
bility that, had the evidence been disclosed to the defense,
the result of the proceeding would have been different.’ ”
Kyles v. Whitley, 514 U. S. 419, 433–434 (1995) (quoting
United States v. Bagley, 473 U. S. 667, 682 (1985) (opinion
of Blackmun, J.)).
   The Court argues that the information in question here
could have affected the jury’s verdict and that petitioner’s
conviction must therefore be reversed. The Court ably
makes the case for reversal, but there is a reasonable
contrary argument that petitioner’s conviction should
stand because the undisclosed information would not have
affected the jury’s verdict. I will briefly discuss the main
points made in the per curiam, not for the purpose of
showing that they are necessarily wrong, but to show that
the Brady issue is not open and shut. For good reason, we
generally do not decide cases without allowing the parties
to file briefs and present argument. Questions that seem
2                     WEARRY v. CAIN

                     ALITO, J., dissenting

quite simple at first glance sometimes look very different
after both sides are given a chance to make their case. Of
course, this process means extra work for the Court. But
it leads to better results, and it gives the losing side the
satisfaction of knowing that at least its arguments have
been fully heard. There is no justification for departing
from our usual procedures in this case.
                              I
   The first item of information discussed by the Court is a
police report that recounts statements made about Sam
Scott, a key witness for the prosecution, by a fellow in-
mate. According to this report, Scott told the inmate: “I’m
gonna make sure Mike [i.e., petitioner] gets the needle
cause he jacked over me.” Pet. Exh. 13 in No. 01–FELN–
015992, p. 103. Scott, who had been serving a sentence on
unrelated drug charges, reportedly told the inmate that he
had been expecting to be released but that he “still [had
not] gone home because of this,” i.e., petitioner’s prosecu-
tion. Id., at 102. As stated in the report, Scott said that
he was now facing the possibility of a 10-year sentence,
apparently for his admitted role in the events surrounding
the murder. The report did not provide any further expla-
nation for Scott’s alleged statement that petitioner had
“jacked [him] over.”
   The Court reads the report to suggest that Scott impli-
cated petitioner in the murder “to settle a personal score.”
Ante, at 8. But if petitioner’s counsel had actually at-
tempted to use this evidence at trial, the net effect might
well have been harmful, not helpful, to the defense. The
undisclosed police report on which the Court relies may be
read to mean that Scott blamed petitioner for putting him
in the position of having to admit his own role in the
events surrounding the murder and thereby expose him-
self to the 10-year sentence and lose an opportunity to
secure early release from prison on the drug charges. If
                    Cite as: 577 U. S. ____ (2016)                   3

                         ALITO, J., dissenting

defense counsel had attempted to impeach Scott with this
police report, the effort could have backfired by allowing
the prosecution to return the jury’s focus to a point the
State emphasized often during trial, namely, that Scott’s
accusations were credible precisely because Scott had no
motive to tell a story that was contrary to his own inter-
ests. See, e.g., 10 Record 2307 (Tr., Mar. 5, 2002) (“If
[Scott] keeps his mouth shut, he is out in less than five
more months. . . . [But] [i]nstead of getting out in 180
days, he is going to be doing more time”). 1
   The Court next turns to an allegation that Scott had
coached another prisoner to make up lies against peti-
tioner. This prisoner never testified at trial, and there is a
basis for arguing that this information would not have
made a difference to the jury, which was well aware that
Scott did not have an exemplary record of veracity. Scott
himself admitted to fabricating information that he told
the police during their investigations. In addition, a wit-
ness who did testify against petitioner at trial also ac-
cused Scott of asking him to lie, although admittedly this
witness later denied making this accusation. Given that
the jury convicted even with these quite serious strikes
against Scott’s credibility, there is reason to question
whether the jury would have seriously considered a differ-
ent verdict because of an accusation from someone who
never took the stand.
   Third, the Court observes that the prosecution failed to
turn over evidence that another witness, Eric Brown, had
——————
  1 The  majority claims that Scott’s unwillingness to tell this fellow
inmate who killed the victim somehow exculpates petitioner. See ante,
at 4, n. 2. In my view, one cannot reasonably infer from the inmate’s
statement, “[Scott] wouldn’t tell me who did it but he said I’m gonna
make sure Mike gets the needle cause he jacked over me,” that Scott
believed petitioner Michael Wearry to be innocent—especially against
the backdrop of Scott’s complaints about his increased imprisonment.
Pet. Exh. 13 in No. 01–FELN–015992, p. 103.
4                         WEARRY v. CAIN

                         ALITO, J., dissenting

asked for favorable treatment from the district attorney in
exchange for testifying against petitioner. It is true—and
troubling—that the prosecutor claimed in her opening
statement that Brown had not sought favorable treatment.
But even so, it is far from clear that disclosing the contra-
dictory information had real potential to affect the trial’s
outcome. For one thing, there is no evidence that Brown
(unlike Scott) actually received any deal, despite defense
counsel’s efforts in cross-examination to establish that
Brown’s testimony might have earned him leniency from
the State. Moreover, Brown admitted during the ex-
change that he had manipulated his initial story to the
police to avoid implicating himself in criminal activity.
We know, then, that the jury harbored no illusions about
the purity of Brown’s motives, notwithstanding the prose-
cutor’s opening misstatement.
  Finally, the Court says that the medical records of
Randy Hutchinson would have cast doubt on Scott’s trial
testimony that Hutchinson repeatedly dragged the victim
into and out of a car and bludgeoned him with a stick.
The records reveal that Hutchinson had knee surgery to
repair his patellar tendon just nine days before the mur-
der. But one of the State’s witnesses testified at trial that
he had seen records showing that Hutchinson had had
surgery on his knee “about nine days before the homicide
happened.” 10 Record 2261 (Tr., Mar. 5, 2002); see also
id., at 2263. The jury thus knew the most salient fact
revealed by these records—that Scott had attributed
significant strength and mobility to a man nine days
removed from knee surgery. 2 Given that these particular
——————
  2 The per curiam argues that the medical records might have had a

greater effect on the jury because they mentioned the particular type of
knee surgery that petitioner had undergone, and that is certainly
possible. But what is important at this stage is that the basic fact—
that petitioner had recently undergone knee surgery—was known to
the jury, and the incremental impact of the additional details supplied
                    Cite as: 577 U. S. ____ (2016)                  5

                         ALITO, J., dissenting

details about Hutchinson’s actions were a relatively minor
part of Scott’s account of the crime and the State’s case
against petitioner, the significance of the undisclosed
medical records is subject to reasonable dispute.
   While the Court highlights the exculpatory quality of
the withheld information, the Court downplays the con-
siderable evidence of petitioner’s guilt. Aside from Scott’s
and Brown’s testimony, three witnesses told the jury that
they saw petitioner and others driving around shortly
after the murder in the victim’s red car, which according
to one of these witnesses had blood on its exterior. Peti-
tioner offered to sell an Albany High School class ring to
one of these witnesses and a set of new speakers to an-
other. The third witness said he saw petitioner throw away a
bottle of Tommy Hilfiger cologne. Meanwhile, the victim’s
mother testified that her son wore an Albany High class
ring that was not recovered with his body, had received
speakers as a gift shortly before his murder, and had a
bottle of Tommy Hilfiger cologne with him on the night
when he was killed. In addition, three jailers testified
that petitioner called his father after his eventual arrest
and stated that “he didn’t know what he was doing in jail
because he didn’t do anything [and] was just an innocent
bystander.” 9 Record 2120 (Tr., Mar. 4, 2002); see also id.,
at 2124, 2126.
   In short, this is far from a case in which the withheld
information would have allowed the defense to undermine
“the only evidence linking [petitioner] to the crime.”
Smith v. Cain, 565 U. S. 73, ___ (2012) (slip op., at 3).
                            II
  Whether disclosing the information at issue realistically
——————
by the medical records is far from clear. Even at the postconviction
evidentiary hearing, the defense’s and State’s medical experts disa-
greed about whether the particular procedure at issue would have left
the then-20-year-old Hutchinson incapable of the acts Scott described.
6                     WEARRY v. CAIN

                      ALITO, J., dissenting

could have changed the trial’s outcome is indisputably an
intensely factual question. Under Brady, we must evalu-
ate the significance of the withheld information in light of
all the proof at petitioner’s trial. See Kyles, 514 U. S., at
435 (Brady is violated when the withheld “evidence could
reasonably be taken to put the whole case in such a differ-
ent light as to undermine confidence in the verdict” (em-
phasis added)); United States v. Agurs, 427 U. S. 97, 112
(1976) (Brady materiality “must be evaluated in the con-
text of the entire record” (emphasis added)). It is unusual
and, in my judgment, unreasonable for us to decide such a
question without full briefing and argument.
   At this stage, all that we have from the State is its brief
in opposition to the petition for certiorari. And the State
had ample reason to believe when it submitted that brief
that the question on the table was whether the Court
should hear the case, not whether petitioner’s conviction
should be reversed. The State undoubtedly knew that we
generally deny certiorari on factbound questions that do
not implicate any disputed legal issue. See, e.g., this
Court’s Rule 10; S. Shapiro, K. Geller, T. Bishop, E. Hart-
nett, & D. Himmelfarb, Supreme Court Practice
§5.12(c)(3), p. 352 (10th ed. 2013). Nothing warned the
State that this petition was likely to produce an exception
to that general rule. The petition does not, for instance,
fall into a category in which the Court has previously
evinced an inclination to police factbound errors. Cf. Cash
v. Maxwell, 565 U. S. ____, ____ (2012) (Scalia, J., dissent-
ing from denial of certiorari) (slip op., at 8) (listing cases
from one such category).
   To the contrary, we have previously told litigants that
petitions like the one here, challenging a state court’s
denial of postconviction relief, are particularly unlikely to
be granted: We “ ‘rarely gran[t] review at this stage’ ” of
litigation, even when a petition raises “ ‘arguably meritori-
ous federal constitutional claims,’ ” because we prefer that
                     Cite as: 577 U. S. ____ (2016)                     7

                          ALITO, J., dissenting

the claims be reviewed first by a district court and court of
appeals in a federal habeas proceeding. Lawrence v. Flor-
ida, 549 U. S. 327, 335 (2007) (quoting Kyles v. Whitley,
498 U. S. 931, 932 (1990) (Stevens, J., concurring in denial
of stay of execution)). 3
   Why, then, has the Court decided to depart from our
usual procedures and decide petitioner’s fact-intensive
Brady claim at this stage? Why not allow petitioner to
raise that claim in a federal habeas proceeding? If the
case took that course, it would not reach us until a district
court and a court of appeals had studied the record and
evaluated the likely impact of the information in question.
   One consequence of waiting until the claim was raised
in a federal habeas proceeding is that our review would
then be governed by the Antiterrorism and Effective
Death Penalty Act of 1996 (AEDPA). Under AEDPA,
relief could be granted only if it could be said that the
state court’s rejection of the claim represented an “unrea-
sonable application” of Brady. 28 U. S. C. §2254(d)(1). By
intervening now before AEDPA comes into play, the Court
avoids the application of that standard and is able to
exercise plenary review. But if the Brady claim is as open-
and-shut as the Court maintains, AEDPA would not pre-
sent an obstacle to the granting of habeas relief. On the
other hand, if reasonable jurists could disagree about the
application of Brady to the facts of this case, there is no
good reason to dispose of this case summarily. The State
——————
   3 The Court implies that meritorious claims in capital cases do consti-

tute a category of factbound errors that the Court has shown willing-
ness to correct on certiorari papers alone. Ante, at 10. In support, it
cites Sears v. Upton, 561 U. S. 945 (2010) (per curiam), and Porter v.
McCollum, 558 U. S. 30 (2009) (per curiam). Notably, Porter did not
arise directly from state postconviction proceedings, but in federal
habeas. And in neither case did the Court take the dramatic step it
takes here and summarily reverse a long-final state conviction for
capital murder; both cases addressed errors related to the defendants’
sentences.
8                    WEARRY v. CAIN

                     ALITO, J., dissenting

should be given the opportunity to make its full case.
  In my view, therefore, summary reversal is highly inap-
propriate. The Court is anxious to vacate petitioner’s
conviction before the State has the opportunity to make its
case. But if we are going to intervene at this stage, we
should grant the petition and hear the case on the merits.
There is room on our docket to give this case the careful
consideration it deserves.

```

---

## GROUP: content/cases/Welsh v. Wisconsin.md  (`case`, 6 assertions)

### content_page

```
---
title: "Welsh v. Wisconsin"
type: case
citation: "466 U.S. 740 (1984)"
parallel_cite: "104 S. Ct. 2091; 80 L. Ed. 2d 732; 52 U.S.L.W. 4581"
neutral_cite: 1984 U.S. LEXIS 82
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1984
date_decided: 1984-05-15
docket: 82-5466
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1984-05-15
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Welsh v. Wisconsin
  varies_by_point: false
  scope_note: "Gravity-of-offense factor reaffirmed; good law (cf. Lange v. California (2021), misdemeanor hot pursuit is not categorical)."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/111173/welsh-v-wisconsin/"
  cluster_id: 111173
  opinion_id: 9429597
  identity_checked: true
homes:
  - page: "[[Arrest in the Home]]"
    role: "Related (cross-doctrine)"
  - page: "[[Exigent Circumstances and Hot Pursuit]]"
    role: "Key — Progeny / Refinement"
related: ["[[Payton v. New York]]", "[[Lange v. California]]", "[[Kentucky v. King]]"]
aliases: ["Welsh"]
tags: ["case", "fourth-amendment", "exigent-circumstances", "arrest-in-the-home", "minor-offense", "dui"]
holding: "The gravity of the underlying offense is a key factor in the exigency analysis; warrantless home entry for a MINOR offense should rarely…"
lake:
  record_id: Welsh v. Wisconsin
  status: verified
  projected_at: 2026-07-09
---

# Welsh v. Wisconsin

*466 U.S. 740 (1984)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
A witness saw Welsh drive erratically, swerve off the road, and stop in a field; Welsh then abandoned his car and walked home. Acting on the report, police checked the car's registration, went to Welsh's house without a warrant, entered, found him in his upstairs bedroom, and arrested him for driving while intoxicated. Under Wisconsin law, a first DWI offense was a noncriminal civil forfeiture punishable only by a fine, with no possible imprisonment.

## Issue
Whether police may make a warrantless, nighttime entry into a suspect's home to arrest him for a minor, noncriminal traffic offense, on the theory that [[Exigent Circumstances and Hot Pursuit|exigent circumstances]] (preserving blood-alcohol evidence) justified the entry.

## Rule
The seriousness of the crime bears directly on whether an [[Exigent Circumstances and Hot Pursuit|exigency]] justifies a warrantless home entry: the Court "hold[s] that an important factor to be considered when determining whether any exigency exists is the gravity of the underlying offense for which the arrest is being made." — 466 U.S. at 753. ^pin-753

For minor offenses, [[Exigent Circumstances and Hot Pursuit|exigency]] will seldom suffice: "application of the exigent-circumstances exception in the context of a home entry should rarely be sanctioned when there is probable cause to believe that only a minor offense, such as the kind at issue in this case, has been committed." — *Id.* And a warrantless home arrest for such an offense is "clearly prohibited by the special protection afforded the individual in his home by the Fourth Amendment." — [*Id.* at 755](https://www.courtlistener.com/opinion/111173/welsh-v-wisconsin/#:~:text=application%20of%20the%20exigent%2Dcircumstances%20exception%20in). ^pin-755

## Application
On these facts no [[Exigent Circumstances and Hot Pursuit|exigency]] justified the entry. [[Exigent Circumstances and Hot Pursuit|Hot pursuit]] did not apply because there was no immediate or continuous pursuit from the scene. With Welsh already home and his car abandoned at the scene, there was little remaining threat to public safety. The only claimed emergency was the dissipation of his blood-alcohol level — but because Wisconsin had classified a first DWI offense as a noncriminal civil forfeiture with no jail, the State's minimal interest could not justify a warrantless entry into the home. The arrest was therefore unreasonable.

## Conclusion
The warrantless, nighttime home entry to arrest Welsh for a civil traffic offense was invalid; the judgment of the Wisconsin Supreme Court was [[Reading and Citing Cases#vacated|vacated]] and the case [[Reading and Citing Cases#on-remand|remanded]].

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- No negative treatment. *Welsh* applies the home-entry protection of [[Payton v. New York]] and supplies the gravity-of-offense factor for the [[Exigent Circumstances and Hot Pursuit|exigency]] analysis later framed in [[Kentucky v. King]]. [[Lange v. California]] (2021) reinforces *Welsh*'s caution, holding that pursuit of a fleeing misdemeanant does not categorically justify a warrantless home entry — the [[Exigent Circumstances and Hot Pursuit|exigency]] must be assessed case by case.

## Appears on
- [[Arrest in the Home]] — *Related (cross-doctrine)*
- [[Exigent Circumstances and Hot Pursuit]] — *Key — Progeny / Refinement*

## Sources
- *Welsh v. Wisconsin*, 466 U.S. 740 (1984) — https://www.courtlistener.com/opinion/111173/welsh-v-wisconsin/ — pinpoints: 753, 755.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "7b8ed90c13f5ab39", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "466 U.S. 740 (1984)", "court": "U.S. Supreme Court", "neutral_cite": "1984 U.S. LEXIS 82", "official_citation_present": true, "parallel_cite": "104 S. Ct. 2091; 80 L. Ed. 2d 732; 52 U.S.L.W. 4581", "title": "Welsh v. Wisconsin", "year": "1984"}}
{"assertion_id": "42ac192b8dbc1dc6", "dimension": "support", "kind": "home_role", "locator": {"home": "Exigent Circumstances and Hot Pursuit"}, "payload": {"home": "Exigent Circumstances and Hot Pursuit", "role": "Key — Progeny / Refinement", "title": "Welsh v. Wisconsin"}}
{"assertion_id": "5076fea4b47a163a", "dimension": "support", "kind": "home_role", "locator": {"home": "Arrest in the Home"}, "payload": {"home": "Arrest in the Home", "role": "Related (cross-doctrine)", "title": "Welsh v. Wisconsin"}}
{"assertion_id": "c872ce2a3a1c2bd7", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "The gravity of the underlying offense is a key factor in the exigency analysis; warrantless home entry for a MINOR offense should rarely…", "title": "Welsh v. Wisconsin"}}
{"assertion_id": "61a223f3031c008b", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1984-05-15", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Welsh v. Wisconsin", "field_i_validity": "good_law", "scope_note": "Gravity-of-offense factor reaffirmed; good law (cf. Lange v. California (2021), misdemeanor hot pursuit is not categorical).", "title": "Welsh v. Wisconsin", "varies_by_point": "false"}}
{"assertion_id": "cd0a69f0c5b566de", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Welsh v. Wisconsin"}}
```

### lake record — Welsh v. Wisconsin

```json
{
  "schema_version": "s2.v1",
  "record_id": "Welsh v. Wisconsin",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Welsh v. Wisconsin",
    "case_name_short": "Welsh",
    "case_name_full": "Welsh v. Wisconsin",
    "input_case_name": "Welsh v. Wisconsin",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1984-05-15",
    "year": 1984,
    "docket": "82-5466",
    "cluster_id": 111173,
    "lead_opinion_id": 9429597,
    "sibling_ids": [
      111173,
      9429597,
      9429598,
      9429599
    ],
    "absolute_url": "/opinion/111173/welsh-v-wisconsin/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "466 U.S. 740",
      "volume": "466",
      "reporter": "U.S.",
      "page": "740",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "104 S. Ct. 2091",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2091",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 732",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "732",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4581",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4581",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1984 U.S. LEXIS 82",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "466 U.S. 740",
        "volume": "466",
        "reporter": "U.S.",
        "page": "740",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "104 S. Ct. 2091",
        "volume": "104",
        "reporter": "S. Ct.",
        "page": "2091",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "80 L. Ed. 2d 732",
        "volume": "80",
        "reporter": "L. Ed. 2d",
        "page": "732",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1984 U.S. LEXIS 82",
        "volume": "1984",
        "reporter": "U.S. LEXIS",
        "page": "82",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "52 U.S.L.W. 4581",
        "volume": "52",
        "reporter": "U.S.L.W.",
        "page": "4581",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "466 U.S. 740",
    "official_selection": {
      "court_class": "scotus",
      "selected": "466 U.S. 740",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-753",
      "page": null,
      "quote": "--- # Welsh v. Wisconsin *466 U.S. 740 (1984)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background A witness saw Welsh drive erratically, swerve off the road, and stop in a field; Welsh then abandoned his car and walked home. Acting on the report, police checked the car's registration, went to Welsh's house without a warrant, entered, found him in his upstairs bedroom, and arrested him for driving while intoxicated. Under Wisconsin law, a first DWI offense was a noncriminal civil forfeiture punishable only by a fine, with no possible imprisonment. ## Issue Whether police may make a warrantless, nighttime entry into a suspect's home to arrest him for a minor, noncriminal traffic offense, on the theory that exigent circumstances (preserving blood-alcohol evidence) justified the entry. ## Rule The seriousness of the crime bears directly on whether an exigency justifies a warrantless home entry: the Court",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-755",
      "page": null,
      "quote": "application of the exigent-circumstances exception in the context of a home entry should rarely be sanctioned when there is probable cause to believe that only a minor offense, such as the kind at issue in this case, has been committed.",
      "star_marker": "753",
      "quote_fidelity": "matched",
      "pinpoint_status": "star-verified",
      "position": 26435,
      "fragment": "#:~:text=application%20of%20the%20exigent%2Dcircumstances%20exception%20in",
      "fragment_validated_at": "2026-07-09T15:40:45Z"
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1984-05-15",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Welsh v. Wisconsin",
    "varies_by_point": false,
    "scope_note": "Gravity-of-offense factor reaffirmed; good law (cf. Lange v. California (2021), misdemeanor hot pursuit is not categorical).",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "State v. Garrett",
          "cluster_id": 4552162,
          "cite": [
            "2018 Ohio 4530",
            "123 N.E.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
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
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "The People v. Shawn J. Sivertson",
          "cluster_id": 4396228,
          "cite": [
            "29 N.Y.3d 1006",
            "77 N.E.3d 349"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
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
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "State of Minnesota v. Todd Eugene Trahan",
          "cluster_id": 4311782,
          "cite": [
            "886 N.W.2d 216",
            "2016 Minn. LEXIS 660"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Glenda Smith v. City of Wyoming",
          "cluster_id": 3194781,
          "cite": [
            "821 F.3d 697",
            "2016 FED App. 0094P",
            "2016 U.S. App. LEXIS 6833",
            "2016 WL 1533998"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Christopher McCoy v. United States",
          "cluster_id": 3182195,
          "cite": [
            "815 F.3d 292",
            "2016 U.S. App. LEXIS 3947",
            "2016 WL 814644"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
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
        "journal_ref": "Welsh v. Wisconsin:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Anderson v. Creighton",
          "cluster_id": 111953,
          "cite": [
            "97 L. Ed. 2d 523",
            "107 S. Ct. 3034",
            "483 U.S. 635",
            "1987 U.S. LEXIS 2894",
            "55 U.S.L.W. 5092"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Whren v. United States",
          "cluster_id": 118036,
          "cite": [
            "135 L. Ed. 2d 89",
            "116 S. Ct. 1769",
            "517 U.S. 806",
            "1996 U.S. LEXIS 3720"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Tennessee v. Garner",
          "cluster_id": 111397,
          "cite": [
            "85 L. Ed. 2d 1",
            "105 S. Ct. 1694",
            "471 U.S. 1",
            "1985 U.S. LEXIS 195",
            "53 U.S.L.W. 4410"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Lucas v. South Carolina Coastal Council",
          "cluster_id": 112787,
          "cite": [
            "120 L. Ed. 2d 798",
            "112 S. Ct. 2886",
            "505 U.S. 1003",
            "1992 U.S. LEXIS 4537"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Brigham City v. Stuart",
          "cluster_id": 145654,
          "cite": [
            "164 L. Ed. 2d 650",
            "126 S. Ct. 1943",
            "547 U.S. 398",
            "2006 U.S. LEXIS 4155"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Griffin v. Wisconsin",
          "cluster_id": 111959,
          "cite": [
            "97 L. Ed. 2d 709",
            "107 S. Ct. 3164",
            "483 U.S. 868",
            "1987 U.S. LEXIS 2897",
            "55 U.S.L.W. 5156"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Minnesota v. Olson",
          "cluster_id": 112416,
          "cite": [
            "109 L. Ed. 2d 85",
            "110 S. Ct. 1684",
            "495 U.S. 91",
            "1990 U.S. LEXIS 2038",
            "58 U.S.L.W. 4464"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kentucky v. King",
          "cluster_id": 216733,
          "cite": [
            "179 L. Ed. 2d 865",
            "131 S. Ct. 1849",
            "563 U.S. 452",
            "2011 U.S. LEXIS 3541"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Atwater v. City of Lago Vista",
          "cluster_id": 2620702,
          "cite": [
            "149 L. Ed. 2d 549",
            "121 S. Ct. 1536",
            "532 U.S. 318",
            "2001 U.S. LEXIS 3366",
            "2001 Daily Journal DAR 3953",
            "2001 Colo. J. C.A.R. 2069",
            "14 Fla. L. Weekly Fed. S 193",
            "69 U.S.L.W. 4262",
            "2001 Cal. Daily Op. Serv. 3203"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "People v. Ledesma",
          "cluster_id": 1228080,
          "cite": [
            "729 P.2d 839",
            "43 Cal. 3d 171",
            "233 Cal. Rptr. 404",
            "1987 Cal. LEXIS 278"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Karo",
          "cluster_id": 111257,
          "cite": [
            "82 L. Ed. 2d 530",
            "104 S. Ct. 3296",
            "468 U.S. 705",
            "1984 U.S. LEXIS 148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Florence v. Board of Chosen Freeholders of County of Burlington",
          "cluster_id": 626454,
          "cite": [
            "182 L. Ed. 2d 566",
            "132 S. Ct. 1510",
            "566 U.S. 318",
            "2012 U.S. LEXIS 2712"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Stanton v. Sims",
          "cluster_id": 2641101,
          "cite": [
            "187 L. Ed. 2d 341",
            "134 S. Ct. 3",
            "2013 U.S. LEXIS 7773",
            "82 U.S.L.W. 4003",
            "571 U.S. 3",
            "24 Fla. L. Weekly Fed. S 473",
            "2013 WL 5878007"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maxine Veatch v. Bartels Lutheran Home",
          "cluster_id": 181829,
          "cite": [
            "627 F.3d 1254",
            "2010 U.S. App. LEXIS 26270",
            "2010 WL 5293814"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "United States v. Michael Johnson",
          "cluster_id": 773999,
          "cite": [
            "256 F.3d 895",
            "2001 Daily Journal DAR 7479",
            "2001 Cal. Daily Op. Serv. 6099",
            "2001 U.S. App. LEXIS 16092",
            "2001 WL 817633"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
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
        "journal_ref": "Welsh v. Wisconsin:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDE0MDIyNDAwMDAwJnM9Mjc0NTA2NiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28111173+OR+9429597+OR+9429598+OR+9429599%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0yNjAmcz00MzIxMDM0JnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28111173+OR+9429597+OR+9429598+OR+9429599%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599)",
        "reviewed": 23,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 23,
        "triage_read": 0,
        "triage_snippet_classified": 23
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(111173 OR 9429597 OR 9429598 OR 9429599)",
    "indexed_citing_opinions": 1133,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 111173,
        "count": 1004,
        "count_source": "search"
      },
      {
        "opinion_id": 9429597,
        "count": 141,
        "count_source": "search"
      },
      {
        "opinion_id": 9429598,
        "count": 0,
        "count_source": "search"
      },
      {
        "opinion_id": 9429599,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 1875,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/welsh-v-wisconsin.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg2MTI5NTUmcz05NDU4MDQwJnQ9byZkPTIwMjYtMDctMDUmcD0y&order_by=score+desc&page_size=100&q=cites%3A%28111173+OR+9429597+OR+9429598+OR+9429599%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 111173,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 101618,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 102196,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 104504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 104605,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 105404,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 106936,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 107262,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 107465,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 107473,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108185,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108282,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108350,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108377,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 109504,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 109874,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 110464,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 110832,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 111057,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 293653,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 317151,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 358582,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 391450,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1149829,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1223369,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1383130,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1482307,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1585837,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1612671,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1696609,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 1927305,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2064400,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2081551,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2108751,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2178478,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2196053,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2222516,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2295125,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 111173,
        "cited_id": 2404257,
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
    "date_created": "2026-07-06T04:13:32Z",
    "date_modified": "2026-07-09T15:47:29Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:13:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:13:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:16:34Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:13:51Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Welsh v. Wisconsin

```
<opinion type="majority">
<author id="b801-10">Justice Brennan</author>
<p id="Ago">delivered the opinion of the Court.</p>
<p id="AKL"><em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">445 U. S. 573</a></span> (1980), held that, absent probable cause and exigent circumstances, warrantless arrests in the home are prohibited by the Fourth Amend<page-number citation-index="1" label="742">*742</page-number>ment. But the Court in that case explicitly refused “to consider the sort of emergency or dangerous situation, described in our cases as ‘exigent circumstances,’ that would justify a warrantless entry into a home for the purpose of either arrest or search.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 583</a></span>. Certiorari was granted in this case to decide at least one aspect of the unresolved question: whether, and if so under what circumstances, the Fourth Amendment prohibits the police from making a warrantless night entry of a person’s home in order to arrest him for a nonjailable traffic offense.</p>
<p id="b802-8">h — &lt;</p>
<p id="b802-3">A</p>
<p id="b802-4">Shortly before 9 o’clock on the rainy night of April 24,1978, a lone witness, Randy Jablonic, observed a car being driven erratically. After changing speeds and veering from side to side, the car eventually swerved off the road and came to a stop in an open field. No damage to any person or property occurred. Concerned about the driver and fearing that the car would get back on the highway, Jablonic drove his truck up behind the car so as to block it from returning to the road. Another passerby also stopped at the scene, and Jablonic asked her to call the police. Before the police arrived, however, the driver of the car emerged from his vehicle, approached Jablonic’s truck, and asked Jablonic for a ride home. Jablonic instead suggested that they wait for assistance in removing or repairing the car. Ignoring Jablonic’s suggestion, the driver walked away from the scene.</p>
<p id="b802-5">A few minutes later, the police arrived and questioned Jablonic. He told one officer what he had seen, specifically noting that the driver was either very inebriated or very sick. The officer checked the motor vehicle registration of the abandoned car and learned that it was registered to the petitioner, Edward G. Welsh. In addition, the officer noted that the petitioner’s residence was a short distance from the scene, and therefore easily within walking distance.</p>
<p id="b803-4"><page-number citation-index="1" label="743">*743</page-number>Without securing any type of warrant, the police proceeded to the petitioner’s home, arriving about 9 p. m. When the petitioner’s stepdaughter answered the door, the police gained entry into the house.<footnotemark>1</footnotemark> Proceeding upstairs to the petitioner’s bedroom, they found him lying naked in bed. At this point, the petitioner was placed under arrest for driving or operating a motor vehicle while under the influence of an intoxicant, in violation of <span class="citation no-link">Wis. Stat. §346.63</span>(1) (1977).<footnotemark>2</footnotemark> The petitioner was taken to the police station, where he refused to submit to a breath-analysis test.</p>
<p id="b803-5">B</p>
<p id="b803-6">As a result of these events, the petitioner was subjected to two separate but related proceedings: one concerning his refusal to submit to a breath test and the other involving the alleged code violation for driving while intoxicated. Under the Wisconsin Vehicle Code in effect in April 1978, one arrested for driving while intoxicated under §346.63(1) could be requested by a law enforcement officer to provide breath, blood, or urine samples for the purpose of determining the presence or quantity of alcohol. <span class="citation no-link">Wis. Stat. §343.305</span>(1) (1975). If such a request was made, the arrestee was re<page-number citation-index="1" label="744">*744</page-number>quired to submit to the appropriate testing or risk a revocation of operating privileges. Cf. <em>South Dakota </em>v. <em>Neville, </em><span class="citation" data-id="9429007"><a href="/opinion/110832/south-dakota-v-neville/" aria-description="Citation for case: South Dakota v. Neville">459 U. S. 553</a></span> (1983) (admission into evidence of a defendant’s refusal to submit to a blood-alcohol test does not offend constitutional right against self-incrimination). The arrestee could challenge the officer’s request, however, by refusing to undergo testing and then asking for a hearing to determine whether the refusal was justified. If, after the hearing, it was determined that the refusal was not justified, the arrest-ee’s operating privileges would be revoked for 60 days.<footnotemark>3</footnotemark></p>
<p id="b804-5">The statute also set forth specific criteria to be applied by a court when determining whether an arrestee’s refusal to take a breath test was justified. Included among these criteria was a requirement that, before revoking the arrestee’s operating privileges, the court determine that “the refusal. . . to submit to a test was unreasonable.” § 343.305(2)(b)(5) (1975). It is not disputed by the parties that an arrestee’s refusal to take a breath test would be reasonable, and therefore operating privileges could not be revoked, if the underlying arrest was not lawful. Indeed, state law has consistently provided that a valid arrest is a necessary prerequisite to the imposition of a breath test. See <em>Scales </em>v. <em>State, </em><span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#494" aria-description="Citation for case: Scales v. State">64 Wis. 2d 485, 494</a></span>, <span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#292" aria-description="Citation for case: Scales v. State">219 N. W. 2d 286, 292</a></span> (1974).<footnotemark>4</footnotemark> Although the stat<page-number citation-index="1" label="745">*745</page-number>ute in effect in April 1978 referred to reasonableness, the current version of §343.305 explicitly recognizes that one of the issues that an arrestee may raise at a refusal hearing is “whether [he] was lawfully placed under arrest for violation of s.346.63(l).» §§343.306(3)(b)(5)(a), (8)(b) (1981-1982). See also 67 Op. Wis. Atty. Gen. No. 93-78 (1978) (“statutory <page-number citation-index="1" label="746">*746</page-number>scheme . . . contemplates that a lawful arrest be made prior to a request for submission to a test”).<footnotemark>5</footnotemark></p>
<p id="b806-5">Separate statutory provisions control the penalty that might be imposed for the substantive offense of driving while intoxicated. At the time in question, the Vehicle Code provided that a first offense for driving while intoxicated was a noncriminal violation subject to a civil forfeiture proceeding for a maximum fine of $200; a second or subsequent offense in the previous five years was a potential misdemeanor that could be punished by imprisonment for up to one year and a maximum fine of $500. <span class="citation no-link">Wis. Stat. §346.65</span>(2) (1975). Since that time, the State has made only minor amendments to these penalty provisions. Indeed, the statute continues to categorize a first offense as a civil violation that allows for only a monetary forfeiture of no more than $300. §346.65(2)(a) (Supp. 1983-1984). See <em>State </em>v. <em>Albright, </em><span class="citation" data-id="2064400"><a href="/opinion/2064400/state-v-albright/#672" aria-description="Citation for case: State v. Albright">98 Wis. 2d 663, 672-673</a></span>, <span class="citation" data-id="2064400"><a href="/opinion/2064400/state-v-albright/#202" aria-description="Citation for case: State v. Albright">298 N. W. 2d 196, 202</a></span> (App. 1980).</p>
<p id="b806-7">C</p>
<p id="b806-8">As noted, in this case the petitioner refused to submit to a breath test; he subsequently filed a timely request for a refusal hearing. Before that hearing was held, however, the State filed a criminal complaint against the petitioner for driving while intoxicated.<footnotemark>6</footnotemark> The petitioner responded by <page-number citation-index="1" label="747">*747</page-number>filing a motion to dismiss the complaint, relying on his contention that the underlying arrest was invalid. After receiving evidence at a hearing on this motion in July 1980, the trial court concluded that the criminal complaint would not be dismissed because the existence of both probable cause and exigent circumstances justified the warrantless arrest. The decision at the refusal hearing, which was not held until September 1980, was therefore preordained. In fact, the primary issue at the refusal hearing — whether the petitioner acted reasonably in refusing to submit to a breath test because he was unlawfully placed under arrest, see <em>supra, </em>at 744-746 — had already been determined two months earlier by the same trial court.</p>
<p id="b807-5">As expected, after the refusal hearing, the trial court concluded that the arrest of the petitioner was lawful and that the petitioner’s refusal to take the breath test was therefore unreasonable.<footnotemark>7</footnotemark> Accordingly, the court issued an order suspending the petitioner’s operating license for 60 days. On appeal, the suspension order was vacated by the Wisconsin Court of Appeals. See <em>State </em>v. <em>Welsh, </em>No. 80-1686 (May 26, 1981), App. 114-125. Contrary to the trial court, the appellate court concluded that the warrantless arrest of the petitioner in his home violated the Fourth Amendment because the State, although demonstrating probable cause to arrest, had not established the existence of exigent circumstances. The petitioner’s refusal to submit to a breath test was therefore reasonable.<footnotemark>8</footnotemark> The Supreme Court of Wisconsin in turn reversed the Court of Appeals, relying on the existence of <page-number citation-index="1" label="748">*748</page-number>three factors that it believed constituted exigent circumstances: the need for “hot pursuit” of a suspect, the need to prevent physical harm to the offender and the public, and the need to prevent destruction of evidence. See <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#336" aria-description="Citation for case: State v. Welsh">108 Wis. 2d 319, 336-338</a></span>, <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#254" aria-description="Citation for case: State v. Welsh">321 N. W. 2d 245, 254-255</a></span> (1982). Because of the important Fourth Amendment implications of the decision below, we granted certiorari. <span class="citation multiple-matches"><a href="/c/U.%20S./459/1200/">459 U. S. 1200</a></span> (1983).<footnotemark>9</footnotemark></p>
<p id="pAEJ">II</p>
<p id="b808-3">It is axiomatic that the “physical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed.” <em>United States </em>v. <em>United States District Court, </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972). And a principal protection against unnecessary intrusions into private dwellings is the warrant requirement imposed by the Fourth Amendment on agents of the government who seek to enter the home for purposes of search or arrest. See <em>Johnson </em>v. <em>United States, </em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S. 10, 13-14</a></span> (1948).<footnotemark>10</footnotemark> It is not surprising, therefore, <page-number citation-index="1" label="749">*749</page-number>that the Court has recognized, as “a ‘basic principle of Fourth Amendment law[,]’ that searches and seizures inside a home without a warrant are presumptively unreasonable. ” <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York">445 U. S., at 586</a></span>. See <em>Coolidge </em>v. <em>New Hampshire, </em><span class="citation" data-id="9424643"><a href="/opinion/108377/coolidge-v-new-hampshire/#474" aria-description="Citation for case: Coolidge v. New Hampshire">403 U. S. 443, 474-475</a></span> (1971) (“a search or seizure carried out on a suspect’s premises without a warrant is <em>per se </em>unreasonable, unless the police can show. . . the presence of ‘exigent circumstances’ ”). See also <em>Michigan </em>v. <em>Clifford, </em><span class="citation" data-id="9429413"><a href="/opinion/111057/michigan-v-clifford/#296" aria-description="Citation for case: Michigan v. Clifford">464 U. S. 287, 296-297</a></span> (1984) (plurality opinion); <em>Steagald </em>v. <em>United States, </em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/#211" aria-description="Citation for case: Steagald v. United States">451 U. S. 204, 211-212</a></span> (1981); <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#456" aria-description="Citation for case: McDonald v. United States">335 U. S. 451, 456</a></span> (1948); <em>Johnson </em>v. <em>United States, supra, </em>at 13-15; <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#630" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 630</a></span> (1886).</p>
<p id="b809-5">Consistently with these long-recognized principles, the Court decided in <em>Payton </em>v. <em>New <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">York, supra,</a></span> </em>that warrant-less felony arrests in the home are prohibited by the Fourth Amendment, absent probable cause and exigent circumstances. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 583-590</a></span>. At the same time, the Court declined to consider the scope of any exception for exigent circumstances that might justify warrantless home arrests, <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#583" aria-description="Citation for case: Payton v. New York"><em>id., </em>at 583</a></span>, thereby leaving to the lower courts the initial application of the exigent-circumstances exception.<footnotemark>11</footnotemark> Prior decisions of this Court, however, have emphasized that exceptions to the warrant requirement are “few in number and carefully delineated,” <em>United States </em>v. <em>United States District Court, supra, </em>at 318, and that the police bear a heavy burden <page-number citation-index="1" label="750">*750</page-number>when attempting to demonstrate an urgent need that might justify warrantless searches or arrests. Indeed, the Court has recognized only a few such emergency conditions, see, <em>e. g., United States </em>v. <em>Santana, </em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/#42" aria-description="Citation for case: United States v. Santana">427 U. S. 38, 42-43</a></span> (1976) (hot pursuit of a fleeing felon); <em>Warden </em>v. <em>Hayden, </em><span class="citation" data-id="9423434"><a href="/opinion/107465/warden-maryland-penitentiary-v-hayden/#298" aria-description="Citation for case: Warden, Maryland Penitentiary v. Hayden">387 U. S. 294, 298-299</a></span> (1967) (same); <em>Schmerber </em>v. <em>California, </em><span class="citation" data-id="9423255"><a href="/opinion/107262/schmerber-v-california/#770" aria-description="Citation for case: Schmerber v. California">384 U. S. 757, 770-771</a></span> (1966) (destruction of evidence); <em>Michigan </em>v. <em>Tyler, </em><span class="citation" data-id="9427218"><a href="/opinion/109874/michigan-v-tyler/#509" aria-description="Citation for case: Michigan v. Tyler">436 U. S. 499, 509</a></span> (1978) (ongoing fire), and has actually applied only the “hot pursuit” doctrine to arrests in the home, see <em><span class="citation" data-id="9426490"><a href="/opinion/109504/united-states-v-santana/" aria-description="Citation for case: United States v. Santana">Santana, supra.</a></span></em></p>
<p id="b810-5">Our hesitation in finding exigent circumstances, especially when warrantless arrests in the home are at issue, is particularly appropriate when the underlying offense for which there is probable cause to arrest is relatively minor. Before agents of the government may invade the sanctity of the home, the burden is on the government to demonstrate exigent circumstances that overcome the presumption of unreasonableness that attaches to all warrantless home entries. See <em>Payton </em>v. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#586" aria-description="Citation for case: Payton v. New York"><em>New York, supra, </em>at 586</a></span>. When the government’s interest is only to arrest for a minor offense,<footnotemark>12</footnotemark> that presumption of unreasonableness is difficult to rebut, and the government usually should be allowed to make such arrests only with a warrant issued upon probable cause by a neutral and detached magistrate.</p>
<p id="b810-6">This is not a novel idea. Writing in concurrence in <em>McDonald </em>v. <em>United States, </em><span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/" aria-description="Citation for case: McDonald v. United States">335 U. S. 451</a></span> (1948), Justice Jackson explained why a finding of exigent circumstances to justify a warrantless home entry should be severely restricted when only a minor offense has been committed:</p>
<blockquote id="b811-4"><page-number citation-index="1" label="751">*751</page-number>“Even if one were to conclude that urgent circumstances might justify a forced entry without a warrant, no such emergency was present in this case. This method of law enforcement displays a shocking lack of all sense of proportion. Whether there is reasonable necessity for a search without waiting to obtain a warrant certainly depends somewhat upon the gravity of the offense thought to be in progress as well as the hazards of the method of attempting to reach it.. . . It is to me a shocking proposition that private homes, even quarters in a tenement, may be indiscriminately invaded at the discretion of any suspicious police officer engaged in following up offenses that involve no violence or threats of it. While I should be human enough to apply the letter of the law with some indulgence to officers acting to deal with threats or crimes of violence which endanger life or security, it is notable that few of the searches found by this Court to be unlawful dealt with that category of crime. . . . While the enterprise of parting fools from their money by the ‘numbers’ lottery is one that ought to be suppressed, I do not think its suppression is more important to society than the security of the people against unreasonable searches and seizures. When an officer undertakes to act as his own magistrate, he ought to be in a position to justify it by pointing to some real immediate and serious consequences if he postponed action to get a warrant.” <span class="citation" data-id="9420240"><a href="/opinion/104605/mcdonald-v-united-states/#459" aria-description="Citation for case: McDonald v. United States"><em>Id., </em>at 459-460</a></span> (footnote omitted).</blockquote>
<p id="b811-5">Consistently with this approach, the lower courts have looked to the nature of the underlying offense as an important factor to be considered in the exigent-circumstances calculus. In a leading federal case defining exigent circumstances, for example, the en banc United States Court of Appeals for the District of Columbia Circuit recognized that the gravity of the underlying offense was a principal factor <page-number citation-index="1" label="752">*752</page-number>to be weighed. <em>Dorman </em>v. <em>United States, </em>140 U. S. App. D. C. 313, 320, <span class="citation" data-id="9456306"><a href="/opinion/293653/harold-b-dorman-v-united-states/#392" aria-description="Citation for case: Harold B. Dorman v. United States">435 F. 2d 385, 392</a></span> (1970).<footnotemark>13</footnotemark> Without approving all of the factors included in the standard adopted by that court, it is sufficient to note that many other lower courts have also considered the gravity of the offense an important part of their constitutional analysis.</p>
<p id="b812-5">For example, courts have permitted warrantless home arrests for major felonies if identifiable exigencies, independent of the gravity of the offense, existed at the time of the arrest. Compare <em>United States </em>v. <em>Campbell, </em><span class="citation" data-id="358582"><a href="/opinion/358582/united-states-v-david-campbell-and-michael-tartt/" aria-description="Citation for case: United States v. David Campbell and Michael Tartt">581 F. 2d 22</a></span> (CA2 1978) (allowing warrantless home arrest for armed robbery when exigent circumstances existed), with <em>Commonwealth </em>v. <em>Williams, </em><span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">483 Pa. 293</a></span>, <span class="citation" data-id="9750792"><a href="/opinion/2295125/commonwealth-v-williams/" aria-description="Citation for case: Commonwealth v. Williams">396 A. 2d 1177</a></span> (1978) (disallowing war-rantless home arrest for murder due to absence of exigent circumstances). But of those courts addressing the issue, most have refused to permit warrantless home arrests for nonfelonious crimes. See, <em>e. g., State </em>v. <em>Guertin, </em><span class="citation" data-id="2404257"><a href="/opinion/2404257/state-v-guertin/#453" aria-description="Citation for case: State v. Guertin">190 Conn. 440, 453</a></span>, <span class="citation" data-id="2404257"><a href="/opinion/2404257/state-v-guertin/#970" aria-description="Citation for case: State v. Guertin">461 A. 2d 963, 970</a></span> (1983) (“The [exigent-circumstances] exception is narrowly drawn to cover cases of real and not contrived emergencies. The exception is limited to the investigation of serious crimes; misdemeanors are excluded”); <em>People </em>v. <em>Strelow, </em><span class="citation" data-id="2222516"><a href="/opinion/2222516/people-v-strelow/#190" aria-description="Citation for case: People v. Strelow">96 Mich. App. 182, 190-193</a></span>, <span class="citation" data-id="2222516"><a href="/opinion/2222516/people-v-strelow/#521" aria-description="Citation for case: People v. Strelow">292 N. W. 2d 517, 521-522</a></span> (1980). See also <em>People </em>v. <em>Sanders, </em><span class="citation" data-id="2081551"><a href="/opinion/2081551/people-v-sanders/" aria-description="Citation for case: People v. Sanders">59 Ill. App. 3d 6</a></span>, <span class="citation" data-id="2081551"><a href="/opinion/2081551/people-v-sanders/" aria-description="Citation for case: People v. Sanders">374 N. E. 2d 1315</a></span> (1978) (burglary without weapons not grave offense of violence for this purpose); <em>State </em>v. <em>Bennett, </em><span class="citation" data-id="2178478"><a href="/opinion/2178478/state-v-bennett/" aria-description="Citation for case: State v. Bennett">295 N. W. 2d 5</a></span> (S. D. 1980) (distribution of controlled substances not a grave offense for these purposes). But cf. <em>State </em>v. <em>Penas, </em><span class="citation" data-id="9697068"><a href="/opinion/1927305/state-v-penas/" aria-description="Citation for case: State v. Penas">200 Neb. 387</a></span>, <span class="citation" data-id="9697068"><a href="/opinion/1927305/state-v-penas/" aria-description="Citation for case: State v. Penas">263 N. W. 2d 835</a></span> (1978) (allowing warrantless home arrest upon hot pursuit from commission of misdemeanor in the officer’s presence; decided before Payton); <em>State </em>v. <em>Niedermeyer, </em><span class="citation" data-id="1149829"><a href="/opinion/1149829/state-v-niedermeyer/" aria-description="Citation for case: State v. Niedermeyer">48 Ore. App. 665</a></span>, <span class="citation" data-id="1149829"><a href="/opinion/1149829/state-v-niedermeyer/" aria-description="Citation for case: State v. Niedermeyer">617 <page-number citation-index="1" label="753">*753</page-number>P. 2d 911</a></span> (1980) (allowing warrantless home arrest upon hot pursuit from commission of misdemeanor in the officer’s presence). The approach taken in these cases should not be surprising. Indeed, without necessarily approving any of these particular holdings or considering every possible factual situation, we note that it is difficult to conceive of a warrantless home arrest that would not be unreasonable under the Fourth Amendment when the underlying offense is extremely minor.</p>
<p id="b813-5">We therefore conclude that the common-sense approach utilized by most lower courts is required by the Fourth Amendment prohibition on “unreasonable searches and seizures,” and hold that an important factor to be considered when determining whether any exigency exists is the gravity of the underlying offense for which the arrest is being made. Moreover, although no exigency is created simply because there is probable cause to believe that a serious crime has been committed, see <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>application of the exigent-circumstances exception in the context of a home entry should rarely be sanctioned when there is probable cause to believe that only a minor offense, such as the kind at issue in this case, has been committed.</p>
<p id="b813-6">Application of this principle to the facts of the present case is relatively straightforward. The petitioner was arrested in the privacy of his own bedroom for a noncriminal, traffic offense. The State attempts to justify the arrest by relying on the hot-pursuit doctrine, on the threat to public safety, and on the need to preserve evidence of the petitioner’s blood-alcohol level. On the facts of this case, however, the claim of hot pursuit is unconvincing because there was no immediate or continuous pursuit of the petitioner from the scene of a crime. Moreover, because the petitioner had already arrived home, and had abandoned his car at the scene of the accident, there was little remaining threat to the public safety. Hence, the only potential emergency claimed by the State was the need to ascertain the petitioner’s blood-alcohol level.</p>
<p id="b814-6"><page-number citation-index="1" label="754">*754</page-number>Even assuming, however, that the underlying facts would support a finding of this exigent circumstance, mere similarity to other cases involving the imminent destruction of evidence is not sufficient. The State of Wisconsin has chosen to classify the first offense for driving while intoxicated as a noncriminal, civil forfeiture offense for which no imprisonment is possible. See <span class="citation no-link">Wis. Stat. §346.65</span>(2) (1975); §346.65(2)(a) (Supp. 1983-1984); <em>supra, </em>at 746. This is the best indication of the State’s interest in precipitating an arrest, and is one that can be easily identified both by the courts and by officers faced with a decision to arrest. See n. 6, <em>supra. </em>Given this expression of the State’s interest, a warrantless home arrest cannot be upheld simply because evidence of the petitioner’s blood-alcohol level might have dissipated while the police obtained a warrant.<footnotemark>14</footnotemark> To allow a warrantless home entry on these facts would be to approve unreasonable police behavior that the principles of the Fourth Amendment will not sanction.</p>
<p id="pAQW">hH I — I 1 — I</p>
<p id="b814-3">The Supreme Court of Wisconsin let stand a warrant-less, nighttime entry into the petitioner’s home to arrest him for a civil traffic offense. Such an arrest, however, is clearly prohibited by the special protection afforded the individual in his home by the Fourth Amendment. The petitioner’s arrest was therefore invalid, the judgment of the Supreme Court of Wisconsin is vacated, and the case is <page-number citation-index="1" label="755">*755</page-number>remanded for further proceedings not inconsistent with this opinion.<footnotemark>15</footnotemark></p>
<p id="b815-5">
<em>It is so ordered.</em>
</p>
<p id="b815-6">The Chief Justice would dismiss the writ as having been improvidently granted and defer resolution of the question presented to a more appropriate case.</p>
<footnote label="1">
<p id="b803-7"> The state trial court never decided whether there was consent to the entry because it deemed decision of that issue unnecessary in light of its finding that exigent circumstances justified the warrantless arrest. After reversing the lower court’s finding of exigent circumstances, the Wisconsin Court of Appeals remanded for full consideration of the consent issue. See <em>State </em>v. <em>Welsh, </em>No. 80-1686 (May 26, 1981), App. 114-126. That remand never occurred, however, because the Supreme Court of Wisconsin reversed the Court of Appeals and reinstated the trial court’s judgment. See <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/" aria-description="Citation for case: State v. Welsh">108 Wis. 2d 319</a></span>, <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/" aria-description="Citation for case: State v. Welsh">321 N. W. 2d 245</a></span> (1982). For purposes of this decision, therefore, we assume that there was no valid consent to enter the petitioner’s home.</p>
</footnote>
<footnote label="2">
<p id="b803-8"> Since the petitioner’s arrest, §346.63 has been amended to provide that it is a code violation to drive or operate a motor vehicle while under the influence of an intoxicant <em>or </em>while evidencing certain blood- or breath-alcohol levels. See <span class="citation no-link">Wis. Stat. §§346.63</span>(1)(a), (b) (1981-1982). Thisamendment, however, has no bearing on the issues raised by the present case.</p>
</footnote>
<footnote label="3">
<p id="b804-6"> Since the petitioner’s arrest, this statute also has been amended, with the current version found at <span class="citation no-link">Wis. Stat. § 343.305</span> (1981-1982). Although the procedures to be followed by the law enforcement officer and the ar-restee have remained essentially unchanged, §§ 343.305(3), (8), the potential length of any revocation of operating privileges has been increased, depending on the arrestee’s prior driving record, §§ 343.305(9)(a), (b). An arrestee who improperly refuses to submit to a required test may also be required to comply with an assessment order and a driver safety plan, §§343.305(9)(c)-(e). These amendments, however, also have no direct bearing on the issues raised by the present case.</p>
</footnote>
<footnote label="4">
<p id="b804-7"> “The implied consent law does not limit the right to take a blood sample as an incident to a <em>lawful </em>arrest. <em>It should be emphasized, however, that the arrest, and therefore probable cause for making it, must precede the taking of the blood sample. </em>We conclude that the sample was constitu<page-number citation-index="1" label="745">*745</page-number>tionally taken incident to the <em>lawful </em>arrest.” <span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#494" aria-description="Citation for case: Scales v. State">64 Wis. 2d, at 494</a></span>, <span class="citation" data-id="9669978"><a href="/opinion/1696609/scales-v-state/#292" aria-description="Citation for case: Scales v. State">219 N. W. 2d, at 292</a></span> (emphasis added).</p>
<p id="AYY">Nor is there any doubt that the Supreme Court of Wisconsin applies federal constitutional standards when determining whether an arrest, even for a nonjailable traffic offense, is lawful. The court, for example, explained the basis for its holding in this case as follows:</p>
<blockquote id="At7y">“The trial court revoked the defendant’s motor vehicle operator’s license for sixty days pursuant to his unreasonable refusal to submit to a breathalyzer test, as required by [state statute].</blockquote>
<blockquote id="AbD">“The defendant challenges the officer’s warrantless arrest in his residence as violating the Fourth Amendment of the United States Constitution and Article I, section 11 of the Wisconsin Constitution. The [trial court] upheld this warrantless arrest concluding that probable cause to believe that the defendant had been operating a motor vehicle while under the influence of an intoxicant, coupled with the existence of exigent circumstances, justified the officers’ entry into the defendant’s residence. . . . [T]he court of appeals reversed the trial court, holding that, although the officers’ warrantless arrest was unreasonable, thereby violating the Fourth and Fourteenth Amendments, the absence of a finding regarding the consensual entry necessitated remanding the case on that issue. We affirm the findings of the [trial court], holding that the co-existence of probable cause and exigent circumstances in this case justifies the warrantless arrest....</blockquote>
<blockquote id="AyC"><em>“To prevail in this </em>case, <em>the state must prove the co-existence of probable cause and exigent circumstances, justifying the officer’s conduct at the defendant’s residence. We hold that there was ample evidence supporting the trial court’s ruling that the officer’s entry was justified on the basis of both probable cause and exigent circumstances. Entry to effect a war-rantless arrest in a residence is subject to the limitations imposed by both the United States and the Wisconsin Constitutions. U. S. Const. amend. IV; Wis. Const. art. I, sec. 11.” </em><span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#320" aria-description="Citation for case: State v. Welsh">108 Wis. 2d, at 320-321, 326-327</a></span>, <span class="citation" data-id="9656368"><a href="/opinion/1585837/state-v-welsh/#246" aria-description="Citation for case: State v. Welsh">321 N. W. 2d, at 246-247, 249-250</a></span> (emphasis added) (citations and footnotes omitted).</blockquote>
</footnote>
<footnote label="5">
<p id="b806-9"> Because state law provides that evidence of the petitioner’s refusal to submit to a breath test is inadmissible if the underlying arrest was unlawful, this case does not implicate the exclusionary rule under the Federal Constitution.</p>
</footnote>
<footnote label="6">
<p id="b806-13"> The petitioner was charged with a criminal misdemeanor because this was his second such citation in the previous five years. See § 346.65(2) (1975). Although the petitioner was subject to a criminal charge, the police conducting the warrantless entry of his home did not know that the petitioner had ever been charged with, or much less convicted of, a prior violation for driving while intoxicated. It must be assumed, therefore, that at the time of the arrest the police were acting as if they were investigating and eventually arresting for a nonjailable traffic offense that constituted only a civil violation under the applicable state law. See <em>Beck </em>v. <em>Ohio, </em><span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#91" aria-description="Citation for case: Beck v. Ohio">379 U. S. 89, 91, 96</a></span> (1964).</p>
</footnote>
<footnote label="7">
<p id="b807-6"> When ruling from the bench after the refusal hearing, the trial judge specifically indicated:</p>
<blockquote id="b807-7">“[T]he Court is bound by its earlier ruling that that was a valid arrest. And, I think [counsel for the petitioner] certainly will have the right to challenge that on appeal if he appeals this matter, as well as the previous ruling should there be a conviction on the underlying charge.” App. 111. See also <span class="citation" data-id="9422887"><a href="/opinion/106936/beck-v-ohio/#112" aria-description="Citation for case: Beck v. Ohio"><em>id., </em>at 112-113</a></span>.</blockquote>
</footnote>
<footnote label="8">
<p id="b807-8"> The court remanded the case for further findings as to whether the police had entered the petitioner’s home with consent. See n. 1, <em>supra.</em></p>
</footnote>
<footnote label="9">
<p id="b808-4"> Although the state courts differed in their respective conclusions concerning exigent circumstances, they each found that the facts known to the police at the time of the warrantless home entry were sufficient to establish probable cause to arrest. The petitioner has not challenged that finding before this Court.</p>
<p id="b808-5">The parallel criminal proceedings against the petitioner, see <em>supra, </em>at 746-747, and n. 6, resulted in a misdemeanor conviction for driving while intoxicated. During the jury trial, held in early 1982, the State introduced evidence of the petitioner's refusal to submit to a breath test. His appeal from that conviction, now before the Wisconsin Court of Appeals, has been stayed pending our decision in this case. See Brief for Petitioner 17, n. 5.</p>
</footnote>
<footnote label="10">
<p id="b808-6"> In <em><span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/" aria-description="Citation for case: Johnson v. United States">Johnson</a></span>, </em>Justice Jackson eloquently explained the warrant requirement in the context of a home search:</p>
<blockquote id="b808-7">“The point of the Fourth Amendment, which often is not grasped by zealous officers, is not that it denies law enforcement the support of the usual inferences which reasonable men draw from evidence. Its protection consists in requiring that those inferences be drawn by a neutral and detached magistrate instead of being judged by the officer engaged in the often competitive enterprise of ferreting out crime. . . . The right of officers to thrust themselves into a home is ... a grave concern, not only to the individual but to a society which chooses to dwell in reasonable security <page-number citation-index="1" label="749">*749</page-number>and freedom from surveillance. When the right of privacy must reasonably yield to the right of search is, as a rule, to be decided by a judicial officer, not by a policeman or government enforcement agent.” <span class="citation" data-id="104504"><a href="/opinion/104504/johnson-v-united-states/#13" aria-description="Citation for case: Johnson v. United States">333 U. S., at 13-14</a></span> (footnote omitted).</blockquote>
</footnote>
<footnote label="11">
<p id="b809-7"> Our decision in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>allowing warrantless home arrests upon a showing of probable cause and exigent circumstances, was also expressly limited to felony arrests. See, e. <em>g., </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#574" aria-description="Citation for case: Payton v. New York">445 U. S., at 574, 602</a></span>. Because we conclude that, in the circumstances presented by this case, there were no exigent circumstances sufficient to justify a warrantless home entry, we have no occasion to consider whether the Fourth Amendment may impose an absolute ban on warrantless home arrests for certain minor offenses.</p>
</footnote>
<footnote label="12">
<p id="b810-7"> Even the dissenters in <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span>, </em>although believing that warrantless home arrests are not prohibited by the Fourth Amendment, recognized the importance of the felony limitation on such arrests. See <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#616" aria-description="Citation for case: Payton v. New York">id., at 616-617</a></span> (White, J., joined by Burgee, C. J., and Rehnquist, J., dissenting) (“The felony requirement guards against abusive or arbitrary enforcement and ensures that invasions of the home occur only in case of the most serious crimes”).</p>
</footnote>
<footnote label="13">
<p id="b812-6"> See generally Donnino &amp; Girese, Exigent Circumstances for a Warrantless Home Arrest, 45 Albany L. Rev. 90 (1980); Harbaugh &amp; Faust, “Knock on Any Door” — Home Arrests After <em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/" aria-description="Citation for case: Payton v. New York">Payton</a></span> </em>and <em><span class="citation" data-id="9428299"><a href="/opinion/110464/steagald-v-united-states/" aria-description="Citation for case: Steagald v. United States">Steagald</a></span>, </em><span class="citation no-link">86 Dick. L. Rev. 191</span>, 220-233 (1982); Note, Exigent Circumstances for Warrantless Home Arrests, <span class="citation no-link">23 Ariz. L. Rev. 1171</span> (1981).</p>
</footnote>
<footnote label="14">
<p id="b814-4"> Nor do we mean to suggest that the prevention of drunken driving is not properly of maj or concern to the States. The State of Wisconsin, however, along with several other States, see, <em>e. g., </em><span class="citation no-link">Minn. Stat. §169.121</span> subd. 4 (1982); <span class="citation no-link">Neb. Rev. Stat. §39-669.07</span>(1) (Supp. 1983); S. D. Codified Laws § 32-23-2 (Supp. 1983), has chosen to limit severely the penalties that may be imposed after a first conviction for driving while intoxicated. Given that the classification of state crimes differs widely among the States, the penalty that may attach to any particular offense seems to provide the clearest and most consistent indication of the State’s interest in arresting individuals suspected of committing that offense.</p>
</footnote>
<footnote label="15">
<p id="b815-11"> On remand, the state courts may consider whether the petitioner’s arrest was justified because the police had validly obtained consent to enter his home. See n. 1, <em>supra.</em></p>
</footnote>
</opinion>
```

---

## GROUP: content/cases/White v. Pauly.md  (`case`, 6 assertions)

### content_page

```
---
title: "White v. Pauly"
type: case
citation: ""
parallel_cite: "580 U.S. 73; 196 L. Ed. 2d 463; 137 S. Ct. 548; 26 Fla. L. Weekly Fed. S 409; 85 U.S.L.W. 4027"
neutral_cite: "2017 U.S. LEXIS 5; 2017 WL 69170"
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 2017
date_decided: 2017-01-09
docket: 16-67
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 2017-01-09
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: White v. Pauly
  varies_by_point: false
  scope_note: "Per curiam; good law on the specificity ('particularized') requirement for clearly established law in excessive-force cases."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/4374579/white-v-pauly/"
  cluster_id: 4374579
  opinion_id: 4151832
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Use of Force]]"
    role: "Related (cross-doctrine)"
related: ["[[Mullenix v. Luna]]", "[[Ashcroft v. al-Kidd]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "excessive-force", "clearly-established", "per-curiam"]
holding: "Garner and Graham do not by themselves create clearly established law outside an obvious case; an officer who arrives late to an ongoing scene did not violate clearly established law by using deadly force without first shouting a warning."
lake:
  record_id: White v. Pauly
  status: verified
  projected_at: 2026-07-06
---

# White v. Pauly

*580 U.S. 73 (2017)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
Responding to a reckless-driving report, New Mexico State Police officers Truesdale and Mariscal approached the Pauly brothers' rural home and (the brothers say without adequately identifying themselves) shouted "Come out or we're coming in." Believing intruders had arrived, the Paulys armed themselves and yelled "We have guns." Officer White arrived late, took cover behind a stone wall, and — without first shouting a warning — shot and killed Samuel Pauly when Samuel pointed a handgun out a window. Samuel's estate sued under § 1983 for excessive force; the district court and a divided Tenth Circuit denied White [[Qualified Immunity|qualified immunity]].

## Issue
Whether Officer White, who arrived late to an ongoing armed confrontation, violated clearly established law by using deadly force without first giving a warning.

## Rule
"Clearly established law" must be specific to the situation, not abstract. "it is again necessary to reiterate the longstanding principle that 'clearly established law' should not be defined 'at a high level of generality' . . . the clearly established law must be 'particularized' to the facts of the case." — 580 U.S. 73 (slip op., at 6) (quoting [[Ashcroft v. al-Kidd]] and *Anderson v. Creighton*). ^pin-73

The panel's reliance on *[[Tennessee v. Garner|Garner]]* and *[[Graham v. Connor|Graham]]* alone could not supply clearly established law: "we have held that *Garner* and *Graham* do not by themselves create clearly established law outside 'an obvious case.'" — *Id.* (slip op., at 7). ^pin-73b

## Application
The Tenth Circuit "failed to identify a case where an officer acting under similar circumstances as Officer White was held to have violated the Fourth Amendment," relying instead on the general principles of *[[Graham v. Connor|Graham]]* and *[[Tennessee v. Garner|Garner]]*. The panel itself called the facts "a unique set of facts and circumstances" given White's late arrival — which alone should have signaled that any violation was not "clearly established." Clearly established law does not prohibit a reasonable officer who arrives late to an ongoing police action from assuming that proper procedures, such as officer identification, were already followed.

## Conclusion
[[Reading and Citing Cases#certiorari-cert|Certiorari]] granted, judgment [[Reading and Citing Cases#vacated|vacated]], and [[Reading and Citing Cases#on-remand|remanded]] (per curiam). On the record described by the court of appeals, Officer White did not violate clearly established law and was entitled to [[Qualified Immunity|qualified immunity]]; the Court left open a potential alternative ground concerning what White witnessed.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- *White* is part of the run of [[Common Legal Terms#per-curiam|per curiam]] qualified-immunity summary reversals applying the high-specificity requirement of [[Ashcroft v. al-Kidd]] and [[Mullenix v. Luna]] to excessive-force claims, holding that [[Graham v. Connor]] and [[Tennessee v. Garner]] supply only general principles. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Use of Force]] — *Related (cross-doctrine)*

## Sources
- *White v. Pauly*, 580 U.S. 73 (2017) (per curiam) — https://www.courtlistener.com/opinion/4374579/white-v-pauly/ — pinpoints: slip op., at 6–7 (CL stores the slip opinion "580 U. S. ____ (2017)"; pins keyed to the official case-start page 73).

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "6e0635766c334a9e", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "", "court": "U.S. Supreme Court", "neutral_cite": "2017 U.S. LEXIS 5; 2017 WL 69170", "official_citation_present": false, "parallel_cite": "580 U.S. 73; 196 L. Ed. 2d 463; 137 S. Ct. 548; 26 Fla. L. Weekly Fed. S 409; 85 U.S.L.W. 4027", "title": "White v. Pauly", "year": "2017"}}
{"assertion_id": "2221a4ad7f012a0e", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Garner and Graham do not by themselves create clearly established law outside an obvious case; an officer who arrives late to an ongoing scene did not violate clearly established law by using deadly force without first shouting a warning.", "title": "White v. Pauly"}}
{"assertion_id": "26cb88501c46cdf9", "dimension": "support", "kind": "home_role", "locator": {"home": "Use of Force"}, "payload": {"home": "Use of Force", "role": "Related (cross-doctrine)", "title": "White v. Pauly"}}
{"assertion_id": "392db070418f4e03", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "White v. Pauly"}}
{"assertion_id": "21bc7506fc1e5cb9", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "2017-01-09", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "White v. Pauly", "field_i_validity": "good_law", "scope_note": "Per curiam; good law on the specificity ('particularized') requirement for clearly established law in excessive-force cases.", "title": "White v. Pauly", "varies_by_point": "false"}}
{"assertion_id": "552a2360033e4433", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "White v. Pauly"}}
```

### lake record — White v. Pauly

```json
{
  "schema_version": "s2.v1",
  "record_id": "White v. Pauly",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "White v. Pauly",
    "case_name_short": "White",
    "case_name_full": "Ray WHITE, Et Al. v. Daniel T. PAULY, as Personal Representative of the Estate of Samuel Pauly, Deceased Et Al.",
    "input_case_name": "White v. Pauly",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "2017-01-09",
    "year": 2017,
    "docket": "16-67",
    "cluster_id": 4374579,
    "lead_opinion_id": 4151832,
    "sibling_ids": [
      4151832,
      9873109,
      9873111
    ],
    "absolute_url": "/opinion/4374579/white-v-pauly/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": null,
    "parallel": [
      {
        "cite": "580 U.S. 73",
        "volume": "580",
        "reporter": "U.S.",
        "page": "73",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "196 L. Ed. 2d 463",
        "volume": "196",
        "reporter": "L. Ed. 2d",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 548",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "548",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 409",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4027",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4027",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "2017 U.S. LEXIS 5",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 69170",
        "volume": "2017",
        "reporter": "WL",
        "page": "69170",
        "type": 7,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "580 U.S. 73",
        "volume": "580",
        "reporter": "U.S.",
        "page": "73",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "196 L. Ed. 2d 463",
        "volume": "196",
        "reporter": "L. Ed. 2d",
        "page": "463",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 U.S. LEXIS 5",
        "volume": "2017",
        "reporter": "U.S. LEXIS",
        "page": "5",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "137 S. Ct. 548",
        "volume": "137",
        "reporter": "S. Ct.",
        "page": "548",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "26 Fla. L. Weekly Fed. S 409",
        "volume": "26",
        "reporter": "Fla. L. Weekly Fed. S",
        "page": "409",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "85 U.S.L.W. 4027",
        "volume": "85",
        "reporter": "U.S.L.W.",
        "page": "4027",
        "type": 4,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "2017 WL 69170",
        "volume": "2017",
        "reporter": "WL",
        "page": "69170",
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
      "id": "pin-73",
      "page": null,
      "quote": "Officer White arrived late, took cover behind a stone wall, and \u2014 without first shouting a warning \u2014 shot and killed Samuel Pauly when Samuel pointed a handgun out a window. Samuel's estate sued under \u00a7 1983 for excessive force; the district court and a divided Tenth Circuit denied White qualified immunity. ## Issue Whether Officer White, who arrived late to an ongoing armed confrontation, violated clearly established law by using deadly force without first giving a warning. ## Rule",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-73b",
      "page": null,
      "quote": "we have held that *Garner* and *Graham* do not by themselves create clearly established law outside 'an obvious case.'",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "2017-01-09",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "White v. Pauly",
    "varies_by_point": false,
    "scope_note": "Per curiam; good law on the specificity ('particularized') requirement for clearly established law in excessive-force cases.",
    "point_overrides": [],
    "edges": [
      {
        "citing_case": {
          "name": "Nat'l Rifle Ass'n of Am. v. Vullo",
          "cluster_id": 10635063,
          "cite": null,
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Katie Joseph v. John Doe",
          "cluster_id": 4821017,
          "cite": [
            "981 F.3d 319"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Dawn Crawford v. John Tilley",
          "cluster_id": 5288690,
          "cite": [
            "15 F.4th 752"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
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
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Phillip Turner v. Driver",
          "cluster_id": 4349754,
          "cite": [
            "848 F.3d 678",
            "2017 WL 650186",
            "2017 U.S. App. LEXIS 2769"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Merritt Sharp, III v. County of Orange",
          "cluster_id": 4427211,
          "cite": [
            "871 F.3d 901",
            "2017 WL 4126947",
            "2017 U.S. App. LEXIS 18148"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Naumovski v. Norris",
          "cluster_id": 4647449,
          "cite": [
            "934 F.3d 200"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Harmon v. City of Arlington",
          "cluster_id": 5292775,
          "cite": [
            "16 F.4th 1159"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Maria Morales v. Sonya Fry",
          "cluster_id": 4434701,
          "cite": [
            "873 F.3d 817"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Gene Bell, Jr. v. City of Southfield, Mich.",
          "cluster_id": 6477591,
          "cite": [
            "37 F.4th 362"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Percy Taylor v. Joseph Ways",
          "cluster_id": 4888555,
          "cite": [
            "999 F.3d 478"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKinney v. City of Middletown",
          "cluster_id": 8243805,
          "cite": [
            "49 F.4th 730"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Will El v. City of Pittsburgh",
          "cluster_id": 4785653,
          "cite": [
            "975 F.3d 327"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Estate of Lopez Ex Rel. Lopez v. Gelhaus",
          "cluster_id": 4428262,
          "cite": [
            "871 F.3d 998",
            "2017 U.S. App. LEXIS 18439"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Bledsoe v. Board Cty Comm. Jefferson KS",
          "cluster_id": 8511576,
          "cite": [
            "53 F.4th 589"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Natia Sampson v. County of Los Angeles",
          "cluster_id": 4783620,
          "cite": [
            "974 F.3d 1012"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Michael Melton v. Hunt County",
          "cluster_id": 4442642,
          "cite": [
            "875 F.3d 256"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Melissa Knibbs v. Anthony Momphard, Jr.",
          "cluster_id": 6456228,
          "cite": [
            "30 F.4th 200"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Sloley v. VanBramer",
          "cluster_id": 4686314,
          "cite": [
            "945 F.3d 30"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Jerry Lawler v. Hardeman Cnty., Tenn.",
          "cluster_id": 9476181,
          "cite": [
            "93 F.4th 919"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ullery v. Bradley",
          "cluster_id": 4725783,
          "cite": [
            "949 F.3d 1282"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Aguirre v. City of San Antonio",
          "cluster_id": 4876506,
          "cite": [
            "995 F.3d 395"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cope v. Cogdill",
          "cluster_id": 4897232,
          "cite": [
            "3 F.4th 198"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Radwan v. Manuel",
          "cluster_id": 9302274,
          "cite": [
            "55 F.4th 101"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Salvatore Palma, Jr. v. Matthew Johns",
          "cluster_id": 6445970,
          "cite": [
            "27 F.4th 419"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "McKenney v. Mangino",
          "cluster_id": 4432664,
          "cite": [
            "873 F.3d 75",
            "2017 WL 4450989",
            "2017 U.S. App. LEXIS 19548"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "White v. Pauly:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(4151832 OR 9873109 OR 9873111) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNTk1OTgwODAwMDAwJnM9NDc3MTM1NSZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%284151832+OR+9873109+OR+9873111%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(4151832 OR 9873109 OR 9873111)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz03NyZzPTQ3NDA0MzgmdD1vJmQ9MjAyNi0wNy0wNSZwPTM%3D&order_by=citeCount+desc&page_size=25&q=cites%3A%284151832+OR+9873109+OR+9873111%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 25,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(4151832 OR 9873109 OR 9873111)",
        "reviewed": 129,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 1,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 129,
        "triage_read": 1,
        "triage_snippet_classified": 128
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(4151832 OR 9873109 OR 9873111)",
    "indexed_citing_opinions": 330,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 4151832,
        "count": 32,
        "count_source": "search"
      },
      {
        "opinion_id": 9873109,
        "count": 299,
        "count_source": "search"
      },
      {
        "opinion_id": 9873111,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2532,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/white-v-pauly.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjkyNTA0Njcmcz0xMDM1MzA2MSZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%284151832+OR+9873109+OR+9873111%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 4151832,
        "cited_id": 111397,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 137736,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 145918,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 4151832,
        "cited_id": 217703,
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
    "date_created": "2026-07-06T04:16:35Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "official cite selection failed closed: unlisted_reporter:Fla. L. Weekly Fed. S",
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:19:47Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:16:44Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — White v. Pauly

```
                 Cite as: 580 U. S. ____ (2017)           1

                          Per Curiam

SUPREME COURT OF THE UNITED STATES
RAY WHITE, ET AL. v. DANIEL T. PAULY, AS PERSONAL 

   REPRESENTATIVE OF THE ESTATE OF SAMUEL 

           PAULY, DECEASED ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE TENTH CIRCUIT

              No. 16–67. Decided January 9, 2017


   PER CURIAM.
   This case addresses the situation of an officer who—
having arrived late at an ongoing police action and having
witnessed shots being fired by one of several individuals
in a house surrounded by other officers—shoots and kills
an armed occupant of the house without first giving a
warning.
   According to the District Court and the Court of Ap-
peals, the record, when viewed in the light most favorable
to respondents, shows the following. Respondent Daniel
Pauly was involved in a road-rage incident on a highway
near Santa Fe, New Mexico. 814 F. 3d 1060, 1064–1065
(CA10 2016). It was in the evening, and it was raining.
The two women involved called 911 to report Daniel as a
“ ‘drunk driver’ ” who was “ ‘swerving all crazy.’ ” Id., at
1065. The women then followed Daniel down the high-
way, close behind him and with their bright lights on.
Daniel, feeling threatened, pulled his truck over at an off-
ramp to confront them. After a brief, nonviolent encoun-
ter, Daniel drove a short distance to a secluded house
where he lived with his brother, Samuel Pauly.
   Sometime between 9 p.m. and 10 p.m., Officer Kevin
Truesdale was dispatched to respond to the women’s 911
call. Truesdale, arriving after Daniel had already left the
scene, interviewed the two women at the off-ramp. The
women told Truesdale that Daniel had been driving reck-
lessly and gave his license plate number to Truesdale.
2                     WHITE v. PAULY

                         Per Curiam

The state police dispatcher identified the plate as being
registered to the Pauly brothers’ address.
   After the women left, Officer Truesdale was joined at
the off-ramp by Officers Ray White and Michael Mariscal.
The three agreed there was insufficient probable cause to
arrest Daniel. Still, the officers decided to speak with
Daniel to (1) get his side of the story, (2) “ ‘make sure
nothing else happened,’ ” and (3) find out if he was intoxi-
cated. Id., at 1065. The officers split up. White stayed at
the off-ramp in case Daniel returned. Truesdale and
Mariscal drove in separate patrol cars to the Pauly broth-
ers’ address, less than a half mile away. Record 215.
Neither officer turned on his flashing lights.
   When Officers Mariscal and Truesdale arrived at the
address they had received from the dispatcher, they found
two different houses, the first with no lights on inside and
a second one behind it on a hill. Id., at 217, 246. Lights
were on in the second one. The officers parked their cars
near the first house. They examined a vehicle parked near
that house but did not find Daniel’s truck. Id., at 310.
   Officers Mariscal and Truesdale noticed the lights on in
the second house and approached it in a covert manner to
maintain officer safety. Both used their flashlights in an
intermittent manner. Truesdale alone turned on his
flashlight once they got close to the house’s front door.
Upon reaching the house, the officers found Daniel’s
pickup truck and spotted two men moving around inside
the residence. Truesdale and Mariscal radioed White, who
left the off-ramp to join them.
   At approximately 11 p.m., the Pauly brothers became
aware of the officers’ presence and yelled out “ ‘Who are
you?’ ” and “ ‘What do you want?’ ” 814 F. 3d, at 1066. In
response, Officers Mariscal and Truesdale laughed and
responded: “ ‘Hey, (expletive), we got you surrounded.
Come out or we’re coming in.’ ” Ibid. Truesdale shouted
once: “ ‘Open the door, State Police, open the door.’ ” Ibid.
                  Cite as: 580 U. S. ____ (2017)            3

                           Per Curiam

Mariscal also yelled: “ ‘Open the door, open the door.’ ”
Ibid.
   The Pauly brothers heard someone yelling, “ ‘We’re
coming in. We’re coming in.’ ” Ibid. Neither Samuel nor
Daniel heard the officers identify themselves as state
police. Record 81–82. The brothers armed themselves,
Samuel with a handgun and Daniel with a shotgun. One
of the brothers yelled at the police officers that “ ‘We have
guns.’ ” 814 F. 3d, at 1066. The officers saw someone run
to the back of the house, so Officer Truesdale positioned
himself behind the house and shouted “ ‘Open the door,
come outside.’ ” Ibid.
   Officer White had parked at the first house and was
walking up to its front door when he heard shouting from
the second house. He half-jogged, half-walked to the
Paulys’ house, arriving “just as one of the brothers said:
‘We have guns.’ ” Ibid.; see also Civ. No. 12–1311 (D NM,
Feb. 5, 2014), App. to Pet. for Cert. 75–78. When White
heard that statement, he drew his gun and took cover
behind a stone wall 50 feet from the front of the house.
Officer Mariscal took cover behind a pickup truck.
   Just “a few seconds” after the “We have guns” state-
ment, Daniel stepped part way out of the back door and
fired two shotgun blasts while screaming loudly. 814
F. 3d, at 1066–1067. A few seconds after those shots,
Samuel opened the front window and pointed a handgun
in Officer White’s direction. Officer Mariscal fired imme-
diately at Samuel but missed. “ ‘Four to five seconds’ ”
later, White shot and killed Samuel. Id., at 1067.
   The District Court denied the officers’ motions for sum-
mary judgment, and the facts are viewed in the light most
favorable to the Paulys. Mullenix v. Luna, 577 U. S. ___,
___, n. (2015) (per curiam) (slip op., at 2, n.). Because this
case concerns the defense of qualified immunity, however,
the Court considers only the facts that were knowable to
the defendant officers. Kingsley v. Hendrickson, 576 U. S.
4                     WHITE v. PAULY

                         Per Curiam

___, ___ (2015) (slip op., at 9).
   Samuel’s estate and Daniel filed suit against, inter alia,
Officers Mariscal, Truesdale, and White. One of the
claims was that the officers were liable under Rev. Stat.
§1979, 42 U. S. C. §1983, for violating Samuel’s Fourth
Amendment right to be free from excessive force. All three
officers moved for summary judgment on qualified immun-
ity grounds. White in particular argued that the Pauly
brothers could not show that White’s use of force vio-
lated the Fourth Amendment and, regardless, that Sam-
uel’s Fourth Amendment right to be free from deadly
force under the circumstances of this case was not clearly
established.
   The District Court denied qualified immunity. A di-
vided panel of the Court of Appeals for the Tenth Circuit
affirmed. As to Officers Mariscal and Truesdale, the court
held that “[a]ccepting as true plaintiffs’ version of the
facts, a reasonable person in the officers’ position should
have understood their conduct would cause Samuel and
Daniel Pauly to defend their home and could result in the
commission of deadly force against Samuel Pauly by Of-
ficer White.” 814 F. 3d, at 1076. The panel majority
analyzed Officer White’s claim separately from the other
officers because “Officer White did not participate in the
events leading up to the armed confrontation, nor was he
there to hear the other officers ordering the brothers to
‘Come out or we’re coming in.’ ” Ibid. Despite the fact that
“Officer White . . . arrived late on the scene and heard only
‘We have guns’ . . . before taking cover behind a stone
wall,” the majority held that a jury could have concluded
that White’s use of deadly force was not reasonable. Id.,
at 1077, 1082. The majority also decided that this rule—
that a reasonable officer in White’s position would believe
that a warning was required despite the threat of serious
harm—was clearly established at the time of Samuel’s
death. The Court of Appeals’ ruling relied on general
                  Cite as: 580 U. S. ____ (2017)              5

                           Per Curiam

statements from this Court’s case law that (1) “the reason-
ableness of an officer’s use of force depends, in part, on
whether the officer was in danger at the precise moment
that he used force” and (2) “if the suspect threatens the
officer with a weapon[,] deadly force may be used if neces-
sary to prevent escape, and if[,] where feasible, some
warning has been given.” Id., at 1083 (citing, inter alia,
Tennessee v. Garner, 471 U. S. 1 (1985), and Graham v.
Connor, 490 U. S. 386 (1989); emphasis deleted; internal
quotation marks and alterations omitted). The court
concluded that a reasonable officer in White’s position
would have known that, since the Paulys could not have
shot him unless he moved from his position behind a stone
wall, he could not have used deadly force without first
warning Samuel Pauly to drop his weapon.
  Judge Moritz dissented, contending that the “majority
impermissibly second-guesses” Officer White’s quick
choice to use deadly force. 814 F. 3d, at 1084. Judge
Moritz explained that the majority also erred by defining
the clearly established law at too high a level of generality,
in contravention of this Court’s precedent.
   The officers petitioned for rehearing en banc, which 6 of
the 12 judges on the Court of Appeals voted to grant. In a
dissent from denial of rehearing, Judge Hartz noted that
he was “unaware of any clearly established law that sug-
gests . . . that an officer . . . who faces an occupant pointing
a firearm in his direction must refrain from firing his
weapon but, rather, must identify himself and shout a
warning while pinned down, kneeling behind a rock wall.”
817 F. 3d 715, 718 (CA10 2016). Judge Hartz expressed
his hope that “the Supreme Court can clarify the govern-
ing law.” Id., at 719.
  The officers petitioned for certiorari. The petition is now
granted, and the judgment is vacated: Officer White did
not violate clearly established law on the record described
by the Court of Appeals panel.
6                      WHITE v. PAULY

                          Per Curiam

    Qualified immunity attaches when an official’s conduct
“ ‘does not violate clearly established statutory or constitu-
tional rights of which a reasonable person would have
known.’ ” Mullenix v. Luna, 577 U. S., at ___–___ (slip op.,
at 4–5). While this Court’s case law “ ‘do[es] not require a
case directly on point’ ” for a right to be clearly established,
“ ‘existing precedent must have placed the statutory or
constitutional question beyond debate.’ ” Id., at ___ (slip
op., at 5). In other words, immunity protects “ ‘all but the
plainly incompetent or those who knowingly violate the
law.’ ” Ibid.
    In the last five years, this Court has issued a number of
opinions reversing federal courts in qualified immunity
cases. See, e.g., City and County of San Francisco v.
Sheehan, 575 U. S. ___, ___, n. 3 (2015) (slip op., at 10, n.3)
(collecting cases). The Court has found this necessary
both because qualified immunity is important to “ ‘society
as a whole,’ ” ibid., and because as “ ‘an immunity from
suit,’ ” qualified immunity “ ‘is effectively lost if a case is
erroneously permitted to go to trial,’ ” Pearson v. Callahan,
555 U. S. 223, 231 (2009).
    Today, it is again necessary to reiterate the longstand-
ing principle that “clearly established law” should not be
defined “at a high level of generality.” Ashcroft v. al-Kidd,
563 U. S. 731, 742 (2011). As this Court explained dec-
ades ago, the clearly established law must be “particular-
ized” to the facts of the case. Anderson v. Creighton, 483
U. S. 635, 640 (1987). Otherwise, “[p]laintiffs would be
able to convert the rule of qualified immunity . . . into a
rule of virtually unqualified liability simply by alleging
violation of extremely abstract rights.” Id., at 639.
    The panel majority misunderstood the “clearly estab-
lished” analysis: It failed to identify a case where an of-
ficer acting under similar circumstances as Officer White
was held to have violated the Fourth Amendment. In-
stead, the majority relied on Graham, Garner, and their
                 Cite as: 580 U. S. ____ (2017)           7

                          Per Curiam

Court of Appeals progeny, which—as noted above—lay out
excessive-force principles at only a general level. Of
course, “general statements of the law are not inherently
incapable of giving fair and clear warning” to officers,
United States v. Lanier, 520 U. S. 259, 271 (1997), but “in
the light of pre-existing law the unlawfulness must be
apparent,” Anderson v. Creighton, supra, at 640. For that
reason, we have held that Garner and Graham do not
by themselves create clearly established law outside
“an obvious case.” Brosseau v. Haugen, 543 U. S. 194,
199 (2004) (per curiam); see also Plumhoff v. Rickard,
572 U. S. ___, ___ (2014) (slip op., at 13) (emphasiz-
ing that Garner and Graham “are ‘cast at a high level of
generality’ ”).
   This is not a case where it is obvious that there was a
violation of clearly established law under Garner and
Graham. Of note, the majority did not conclude that
White’s conduct—such as his failure to shout a warning—
constituted a run-of-the-mill Fourth Amendment violation.
Indeed, it recognized that “this case presents a unique set
of facts and circumstances” in light of White’s late arrival
on the scene. 814 F. 3d, at 1077. This alone should have
been an important indication to the majority that White’s
conduct did not violate a “clearly established” right.
Clearly established federal law does not prohibit a reason-
able officer who arrives late to an ongoing police action in
circumstances like this from assuming that proper proce-
dures, such as officer identification, have already been
followed. No settled Fourth Amendment principle re-
quires that officer to second-guess the earlier steps al-
ready taken by his or her fellow officers in instances like
the one White confronted here.
   On the record described by the Court of Appeals, Officer
White did not violate clearly established law. The Court
notes, however, that respondents contend Officer White
arrived on the scene only two minutes after Officers
8                     WHITE v. PAULY

                         Per Curiam

Truesdale and Mariscal and more than three minutes
before Daniel’s shots were fired. On the assumption that
the conduct of Officers Truesdale and Mariscal did not
adequately alert the Paulys that they were police officers,
respondents suggest that a reasonable jury could infer
that White witnessed the other officers’ deficient perfor-
mance and should have realized that corrective action was
necessary before using deadly force. Brief in Opposition
11, 22, n. 5. This Court expresses no position on this
potential alternative ground for affirmance, as it appears
that neither the District Court nor the Court of Appeals
panel addressed it. The Court also expresses no opinion
on the question whether this ground was properly pre-
served or whether—in light of this Court’s holding today—
Officers Truesdale and Mariscal are entitled to qualified
immunity.
  For the foregoing reasons, the petition for certiorari is
granted; the judgment of the Court of Appeals is vacated;
and the case is remanded for further proceedings con-
sistent with this opinion.
                                           It is so ordered.
                 Cite as: 580 U. S. ____ (2017)            1

                    GINSBURG, J., concurring

SUPREME COURT OF THE UNITED STATES
RAY WHITE, ET AL. v. DANIEL T. PAULY, AS PERSONAL 

   REPRESENTATIVE OF THE ESTATE OF SAMUEL 

           PAULY, DECEASED ET AL. 

   ON PETITION FOR WRIT OF CERTIORARI TO THE UNITED 

    STATES COURT OF APPEALS FOR THE TENTH CIRCUIT

              No. 16–67. Decided January 9, 2017


   JUSTICE GINSBURG, concurring.
   I join the Court’s opinion on the understanding that it
does not foreclose the denial of summary judgment to
Officers Truesdale and Mariscal. See 814 F. 3d 1060,
1068, 1073, 1074 (CA10 2016) (Court of Appeals empha-
sized, repeatedly, that fact disputes exist on question
whether Truesdale and Mariscal “adequately identified
themselves” as police officers before shouting “Come out or
we’re coming in” (internal quotation marks omitted)).
Further, as to Officer White, the Court, as I comprehend
its opinion, leaves open the propriety of denying summary
judgment based on fact disputes over when Officer White
arrived at the scene, what he may have witnessed, and
whether he had adequate time to identify himself and
order Samuel Pauly to drop his weapon before Officer
White shot Pauly. Compare id., at 1080, with ante, at 8.
See also Civ. No. 12–1311 (D NM, Feb. 5, 2014), pp. 7, and
n. 5, 9, App. to Pet. for Cert. 75–76, and n. 5, 77 (suggest-
ing that Officer White may have been on the scene when
Officers Truesdale and Mariscal threatened to invade the
Pauly home).

```

---

## GROUP: content/cases/Wilson v. Layne.md  (`case`, 6 assertions)

### content_page

```
---
title: "Wilson v. Layne"
type: case
citation: "526 U.S. 603 (1999)"
parallel_cite: "119 S. Ct. 1692; 143 L. Ed. 2d 818"
neutral_cite: 1999 U.S. LEXIS 3633
court: U.S. Supreme Court
court_level: scotus
circuit: ""
year: 1999
date_decided: 1999-05-24
docket: 98-83
authority_weight: "Binding — SCOTUS"
treatment:
  field_i_validity: good_law
  as_of_content: 1999-05-24
  as_of_treatment: 2026-06-30
  composite_basis: migration-seed
  composite_basis_ref: Wilson v. Layne
  varies_by_point: false
  scope_note: "Good law: media ride-along into a home during warrant execution violates the 4A; officers had QI on the then-undeveloped law."
  point_overrides: []
courtlistener:
  opinion_url: "https://www.courtlistener.com/opinion/118289/wilson-v-layne/"
  cluster_id: 118289
  opinion_id: 9433801
  identity_checked: true
homes:
  - page: "[[Qualified Immunity]]"
    role: "Key — Progeny / Refinement"
  - page: "[[Scope Manner and Related Issues]]"
    role: "Related (cross-doctrine)"
related: ["[[Hanlon v. Berger]]", "[[Harlow v. Fitzgerald]]", "[[Graham v. Connor]]"]
aliases: []
tags: ["case", "section-1983", "qualified-immunity", "media-ride-along", "warrant-execution", "clearly-established"]
holding: "Bringing the media or other third parties into a home during the execution of a warrant, when not in aid of the warrant, violates the Fourth Amendment — but the officers had qualified immunity because that right was not clearly established."
lake:
  record_id: Wilson v. Layne
  status: verified
  projected_at: 2026-07-06
---

# Wilson v. Layne

*526 U.S. 603 (1999)* · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above -->

## Background
In April 1992, deputy U.S. Marshals and county deputies executing arrest warrants for Dominic Wilson invited a *Washington Post* reporter and photographer to accompany them into the home of Dominic's parents, Charles and Geraldine Wilson, during the early-morning entry. The parents were roused from bed; Charles Wilson, in his underwear, was subdued on the floor while the journalists observed and photographed (the photos were never published). Dominic was not there. The Wilsons sued the officers under *[[Bivens v. Six Unknown Named Agents|Bivens]]* and § 1983.

## Issue
Whether police violate the Fourth Amendment by bringing media into a home during the execution of a warrant, and if so, whether the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Rule
Such a media intrusion violates the Fourth Amendment: "We hold that it is a violation of the Fourth Amendment for police to bring members of the media or other third parties into a home during the execution of a warrant when the presence of the third parties in the home was not in aid of the execution of the warrant." — 526 U.S. at 614. ^pin-614

But [[Qualified Immunity|qualified immunity]] still protects the officers unless the right was clearly established at the time. "We hold that it was not unreasonable for a police officer in April 1992 to have believed that bringing media observers along during the execution of an arrest warrant (even in a home) was lawful." — *Id.* at 615. ^pin-615

## Application
Inviting the journalists served no purpose in executing the arrest warrant — they did not aid the search for Dominic — so their presence inside the home exceeded what the warrant authorized and violated the Fourth Amendment. On immunity, however, in 1992 the constitutional question was not "open and shut": no judicial decision had held that a media ride-along became unlawful when it entered a home, and the practice was common. Because the contours of the right were not sufficiently clear that a reasonable officer would have understood the entry to be unlawful, the officers were entitled to [[Qualified Immunity|qualified immunity]].

## Conclusion
Affirmed. The media's presence in the home violated the Fourth Amendment, but the officers received [[Qualified Immunity|qualified immunity]] because the right was not clearly established in April 1992.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS**.
- Decided the same day as its [[Common Legal Terms#per-curiam|per curiam]] companion [[Hanlon v. Berger]], which applied the same Fourth Amendment holding and [[Qualified Immunity|qualified immunity]] to a media ride-along onto a ranch. *Wilson* is a leading application of the [[Harlow v. Fitzgerald]] "clearly established" standard. No negative treatment.

## Appears on
- [[Section 1983 Liability and Qualified Immunity]] — *Key — Progeny / Refinement*
- [[Scope Manner and Related Issues]] — *Related (cross-doctrine)*

## Sources
- *Wilson v. Layne*, 526 U.S. 603 (1999) — https://www.courtlistener.com/opinion/118289/wilson-v-layne/ — pinpoints: 614, 615.

```

### group_inventory (assertions under review)

```jsonl
{"assertion_id": "a24303af174605c2", "dimension": "existence", "kind": "case_cite", "locator": {"field": "citation"}, "payload": {"citation": "526 U.S. 603 (1999)", "court": "U.S. Supreme Court", "neutral_cite": "1999 U.S. LEXIS 3633", "official_citation_present": true, "parallel_cite": "119 S. Ct. 1692; 143 L. Ed. 2d 818", "title": "Wilson v. Layne", "year": "1999"}}
{"assertion_id": "aa14de253f8e50d4", "dimension": "support", "kind": "home_role", "locator": {"home": "Scope Manner and Related Issues"}, "payload": {"home": "Scope Manner and Related Issues", "role": "Related (cross-doctrine)", "title": "Wilson v. Layne"}}
{"assertion_id": "cd46c7a31d5ffd2b", "dimension": "support", "kind": "home_role", "locator": {"home": "Qualified Immunity"}, "payload": {"home": "Qualified Immunity", "role": "Key — Progeny / Refinement", "title": "Wilson v. Layne"}}
{"assertion_id": "d581393a88335cf4", "dimension": "support", "kind": "proposition", "locator": {"field": "holding"}, "payload": {"holding": "Bringing the media or other third parties into a home during the execution of a warrant, when not in aid of the warrant, violates the Fourth Amendment — but the officers had qualified immunity because that right was not clearly established.", "title": "Wilson v. Layne"}}
{"assertion_id": "5c10ec367d187294", "dimension": "treatment", "kind": "treatment", "locator": {"field": "treatment"}, "payload": {"as_of_content": "1999-05-24", "as_of_treatment": "2026-06-30", "composite_basis": "migration-seed", "composite_basis_ref": "Wilson v. Layne", "field_i_validity": "good_law", "scope_note": "Good law: media ride-along into a home during warrant execution violates the 4A; officers had QI on the then-undeveloped law.", "title": "Wilson v. Layne", "varies_by_point": "false"}}
{"assertion_id": "7f0bf04f043a17d9", "dimension": "treatment", "kind": "weight_label", "locator": {"field": "authority_weight"}, "payload": {"authority_weight": "Binding — SCOTUS", "title": "Wilson v. Layne"}}
```

### lake record — Wilson v. Layne

```json
{
  "schema_version": "s2.v1",
  "record_id": "Wilson v. Layne",
  "stub": false,
  "status": "verified",
  "identity": {
    "case_name": "Wilson v. Layne",
    "case_name_short": "Wilson",
    "case_name_full": "WILSON Et Al. v. LAYNE, DEPUTY UNITED STATES MARSHAL, Et Al.",
    "input_case_name": "Wilson v. Layne",
    "court": "U.S. Supreme Court",
    "court_id": "scotus",
    "court_level": "scotus",
    "circuit": null,
    "state": null,
    "date_decided": "1999-05-24",
    "year": 1999,
    "docket": "98-83",
    "cluster_id": 118289,
    "lead_opinion_id": 9433801,
    "sibling_ids": [
      118289,
      9433801,
      9433802
    ],
    "absolute_url": "/opinion/118289/wilson-v-layne/",
    "identity_method": "citation+party-text",
    "expected_citation_found": true,
    "party_name_in_text": true,
    "canonical_name_match": true,
    "alternates": [],
    "reason_code": null
  },
  "citations": {
    "official": {
      "cite": "526 U.S. 603",
      "volume": "526",
      "reporter": "U.S.",
      "page": "603",
      "type": 1,
      "selected_official": true,
      "source": "cluster.citations[]"
    },
    "parallel": [
      {
        "cite": "119 S. Ct. 1692",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1692",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 818",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "818",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "vendor_neutral": [
      {
        "cite": "1999 U.S. LEXIS 3633",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3633",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "all": [
      {
        "cite": "526 U.S. 603",
        "volume": "526",
        "reporter": "U.S.",
        "page": "603",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "119 S. Ct. 1692",
        "volume": "119",
        "reporter": "S. Ct.",
        "page": "1692",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "143 L. Ed. 2d 818",
        "volume": "143",
        "reporter": "L. Ed. 2d",
        "page": "818",
        "type": 1,
        "selected_official": false,
        "source": "cluster.citations[]"
      },
      {
        "cite": "1999 U.S. LEXIS 3633",
        "volume": "1999",
        "reporter": "U.S. LEXIS",
        "page": "3633",
        "type": 6,
        "selected_official": false,
        "source": "cluster.citations[]"
      }
    ],
    "display": "526 U.S. 603",
    "official_selection": {
      "court_class": "scotus",
      "selected": "526 U.S. 603",
      "reason": "selected_rank_1"
    }
  },
  "pinpoints": [
    {
      "id": "pin-614",
      "page": null,
      "quote": "--- # Wilson v. Layne *526 U.S. 603 (1999)* \u00b7 U.S. Supreme Court \u00b7 **Binding \u2014 SCOTUS** \u00b7 Treatment: **good** *(as of 2026-06-30)* <!-- header line; TreatmentBadge + weight render here, degrading to the text above --> ## Background In April 1992, deputy U.S. Marshals and county deputies executing arrest warrants for Dominic Wilson invited a *Washington Post* reporter and photographer to accompany them into the home of Dominic's parents, Charles and Geraldine Wilson, during the early-morning entry. The parents were roused from bed; Charles Wilson, in his underwear, was subdued on the floor while the journalists observed and photographed (the photos were never published). Dominic was not there. The Wilsons sued the officers under *Bivens* and \u00a7 1983. ## Issue Whether police violate the Fourth Amendment by bringing media into a home during the execution of a warrant, and if so, whether the officers were entitled to qualified immunity. ## Rule Such a media intrusion violates the Fourth Amendment:",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    },
    {
      "id": "pin-615",
      "page": null,
      "quote": "We hold that it was not unreasonable for a police officer in April 1992 to have believed that bringing media observers along during the execution of an arrest warrant (even in a home) was lawful.",
      "star_marker": null,
      "quote_fidelity": "mismatch",
      "pinpoint_status": "slip-only",
      "position": null
    }
  ],
  "treatment": {
    "field_i_validity": "good_law",
    "as_of_content": "1999-05-24",
    "as_of_treatment": "2026-06-30",
    "composite_basis": "migration-seed",
    "composite_basis_ref": "Wilson v. Layne",
    "varies_by_point": false,
    "scope_note": "Good law: media ride-along into a home during warrant execution violates the 4A; officers had QI on the then-undeveloped law.",
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
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Brown v. City of Hous.",
          "cluster_id": 7329084,
          "cite": [
            "297 F. Supp. 3d 748"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Paul Thompson, Jr. v. Commonwealth of Virginia",
          "cluster_id": 4452532,
          "cite": [
            "878 F.3d 89"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "United States v. Pirk",
          "cluster_id": 7327733,
          "cite": [
            "282 F. Supp. 3d 585"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
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
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Quiroz v. Short",
          "cluster_id": 7311906,
          "cite": [
            "85 F. Supp. 3d 1092",
            "2015 WL 1395786",
            "2015 U.S. Dist. LEXIS 42278"
          ],
          "field_ii": "superseded_by_statute"
        },
        "field_ii": "superseded_by_statute",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane1_negative"
      },
      {
        "citing_case": {
          "name": "Ashcroft v. Iqbal",
          "cluster_id": 145875,
          "cite": [
            "173 L. Ed. 2d 868",
            "129 S. Ct. 1937",
            "556 U.S. 662",
            "2009 U.S. LEXIS 3472"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Pearson v. Callahan",
          "cluster_id": 145918,
          "cite": [
            "172 L. Ed. 2d 565",
            "129 S. Ct. 808",
            "555 U.S. 223",
            "2009 U.S. LEXIS 591"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hope v. Pelzer",
          "cluster_id": 121169,
          "cite": [
            "153 L. Ed. 2d 666",
            "122 S. Ct. 2508",
            "536 U.S. 730",
            "2002 U.S. LEXIS 4884"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Ziglar v. Abbasi",
          "cluster_id": 4403804,
          "cite": [
            "582 U.S. 120",
            "2017 U.S. LEXIS 3874",
            "137 S. Ct. 1843",
            "198 L. Ed. 2d 290",
            "26 Fla. L. Weekly Fed. S 655",
            "85 U.S.L.W. 4360",
            "2017 WL 2621317"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Reichle v. Howards",
          "cluster_id": 801500,
          "cite": [
            "182 L. Ed. 2d 985",
            "132 S. Ct. 2088",
            "566 U.S. 658",
            "2012 U.S. LEXIS 4132"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Kisela v. Hughes",
          "cluster_id": 4482892,
          "cite": [
            "584 U.S. 100",
            "138 S. Ct. 1148",
            "200 L. Ed. 2d 449",
            "2018 U.S. LEXIS 2066"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Plumhoff v. Rickard",
          "cluster_id": 2675750,
          "cite": [
            "188 L. Ed. 2d 1056",
            "134 S. Ct. 2012",
            "2014 U.S. LEXIS 3816",
            "82 U.S.L.W. 4394",
            "572 U.S. 765",
            "24 Fla. L. Weekly Fed. S 790",
            "2014 WL 2178335"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Hartman v. Moore",
          "cluster_id": 145662,
          "cite": [
            "164 L. Ed. 2d 441",
            "126 S. Ct. 1695",
            "547 U.S. 250",
            "2006 U.S. LEXIS 3450"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Johnson v. State",
          "cluster_id": 2336338,
          "cite": [
            "68 S.W.3d 644",
            "2002 Tex. Crim. App. LEXIS 17",
            "2002 WL 122735"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Groh v. Ramirez",
          "cluster_id": 131161,
          "cite": [
            "157 L. Ed. 2d 1068",
            "124 S. Ct. 1284",
            "540 U.S. 551",
            "2004 U.S. LEXIS 1624",
            "2004 WL 330057"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Keith A. Hill v. Borough of Kutztown and Gennaro Marino, Mayor of Kutztown, in His Individual and Official Capacity",
          "cluster_id": 795079,
          "cite": [
            "455 F.3d 225",
            "2006 U.S. App. LEXIS 18708",
            "98 Fair Empl. Prac. Cas. (BNA) 942",
            "2006 WL 2061145"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Terri Vinyard v. Steve Wilson",
          "cluster_id": 76029,
          "cite": [
            "311 F.3d 1340",
            "2002 U.S. App. LEXIS 23576",
            "2002 WL 31521208"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Anthony C. Greene v. Jack Barber, Edward Hillyer, Victor Gillis, William Hegarty, and the City of Grand Rapids, Michigan",
          "cluster_id": 779855,
          "cite": [
            "310 F.3d 889",
            "2002 U.S. App. LEXIS 23228",
            "2002 WL 31487268"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Messerschmidt v. Millender",
          "cluster_id": 623242,
          "cite": [
            "182 L. Ed. 2d 47",
            "132 S. Ct. 1235",
            "565 U.S. 535",
            "2012 U.S. LEXIS 1687"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Owens v. Baltimore City State's Attorneys Office",
          "cluster_id": 2736472,
          "cite": [
            "767 F.3d 379",
            "2014 U.S. App. LEXIS 18294",
            "2014 WL 4723803"
          ],
          "field_ii": "abrogated"
        },
        "field_ii": "abrogated",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "White v. Lee",
          "cluster_id": 7082005,
          "cite": [
            "227 F.3d 1214",
            "2000 Daily Journal DAR 10557",
            "2000 Cal. Daily Op. Serv. 7958",
            "2000 U.S. App. LEXIS 23778",
            "2000 WL 1407125"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Cousins v. Lockyer",
          "cluster_id": 1459853,
          "cite": [
            "568 F.3d 1063",
            "2009 U.S. App. LEXIS 12708",
            "2009 WL 1652208"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Rubin Sira v. R. Morton, C. Artuz, D. Selsky, and G. Goord",
          "cluster_id": 787387,
          "cite": [
            "380 F.3d 57",
            "2004 WL 1837779"
          ],
          "field_ii": "questioned"
        },
        "field_ii": "questioned",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "Holloman Ex Rel. Holloman v. Harland",
          "cluster_id": 76571,
          "cite": [
            "370 F.3d 1252",
            "2004 WL 1178465"
          ],
          "field_ii": "overruled"
        },
        "field_ii": "overruled",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
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
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      },
      {
        "citing_case": {
          "name": "District of Columbia v. Wesby",
          "cluster_id": 4460811,
          "cite": [
            "583 U.S. 48"
          ],
          "field_ii": "criticized"
        },
        "field_ii": "criticized",
        "field_iii": "mentioned",
        "point": null,
        "proposed": true,
        "journal_ref": "Wilson v. Layne:lane2_top_cited"
      }
    ],
    "derivation": {
      "lane1_negative": {
        "query": "cites:(118289 OR 9433801 OR 9433802) AND (overrul* OR abrogat* OR supersed* OR \"recede from\" OR \"no longer good law\" OR vacat* OR reversed) ",
        "reviewed": 200,
        "cap": 200,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xNDI3NzYwMDAwMDAwJnM9NzMxMTkwNiZ0PW8mZD0yMDI2LTA3LTA1JnA9MTE%3D&fields=absolute_url%2CcaseName%2CcaseNameFull%2Ccitation%2CciteCount%2Ccluster_id%2Ccourt%2Ccourt_citation_string%2Ccourt_id%2CdateFiled%2Copinions%2Csibling_ids%2Cstatus%2Csyllabus&order_by=dateFiled+desc&page_size=100&q=cites%3A%28118289+OR+9433801+OR+9433802%29+AND+%28overrul%2A+OR+abrogat%2A+OR+supersed%2A+OR+%22recede+from%22+OR+%22no+longer+good+law%22+OR+vacat%2A+OR+reversed%29+&stat_Published=on&type=o",
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
        "query": "cites:(118289 OR 9433801 OR 9433802)",
        "reviewed": 25,
        "cap": 25,
        "cap_hit": true,
        "final_cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz00ODEmcz0xNDYzMTcyJnQ9byZkPTIwMjYtMDctMDUmcD0z&order_by=citeCount+desc&page_size=25&q=cites%3A%28118289+OR+9433801+OR+9433802%29&type=o",
        "audit_needed": true,
        "proposed_negative_events": 24,
        "audit_marker": "R15 treatment audit required"
      },
      "lane3_recency": {
        "query": "cites:(118289 OR 9433801 OR 9433802)",
        "reviewed": 53,
        "cap": 200,
        "cap_hit": false,
        "final_cursor": null,
        "audit_needed": false,
        "proposed_negative_events": 0,
        "audit_marker": null,
        "triage_mode": "snippet-first",
        "snippet_field": "results[].opinions[].snippet",
        "triage_journaled": 53,
        "triage_read": 0,
        "triage_snippet_classified": 53
      }
    }
  },
  "progeny": {
    "complete_query": "cites:(118289 OR 9433801 OR 9433802)",
    "indexed_citing_opinions": 1451,
    "count_source": "search",
    "per_sibling": [
      {
        "opinion_id": 118289,
        "count": 1241,
        "count_source": "search"
      },
      {
        "opinion_id": 9433801,
        "count": 228,
        "count_source": "search"
      },
      {
        "opinion_id": 9433802,
        "count": 0,
        "count_source": "search"
      }
    ],
    "citation_count": 2687,
    "cache_path": "/Users/johngalt/cssi-lake/cache/progeny/wilson-v-layne.jsonl",
    "enumeration": "bounded",
    "cursor": "https://www.courtlistener.com/api/rest/v4/search/?cursor=cz0xLjg5OTk3NzImcz0xMDEyNTAyMyZ0PW8mZD0yMDI2LTA3LTA1JnA9Mg%3D%3D&order_by=score+desc&page_size=100&q=cites%3A%28118289+OR+9433801+OR+9433802%29&type=o",
    "rows_cached": 20,
    "outbound_opinion_edges": [
      {
        "source_opinion_id": 118289,
        "cited_id": 91573,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 107411,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 108375,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 108581,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 109199,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 109207,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110235,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110339,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110534,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 110763,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111611,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111823,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111834,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 111953,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 112257,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 112448,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 112594,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 118066,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 118098,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 118214,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 579234,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 678500,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 719620,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 724925,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 748210,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 752970,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 1769461,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 2178648,
        "source": "search.opinions[].cites[]"
      },
      {
        "source_opinion_id": 118289,
        "cited_id": 2281316,
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
    "date_created": "2026-07-06T04:29:07Z",
    "date_modified": "2026-07-06T10:25:12Z",
    "warnings": [
      "legacy treatment migrated: good -> good_law"
    ],
    "field_provenance": {
      "identity": {
        "src": "CourtListener search + clusters + lead opinion text",
        "at": "2026-07-06T04:29:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "treatment.field_i_validity": {
        "src": "_treatment-migration.json + page frontmatter",
        "at": "2026-07-06T04:29:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "point_overrides": {
        "src": "S2 treatment derivation proposed only",
        "at": "2026-07-06T04:33:28Z",
        "verifier": "S2-BUILDER-AUTHORING"
      },
      "pinpoints": {
        "src": "content page quote harvest + lead opinion text",
        "at": "2026-07-06T04:29:26Z",
        "verifier": "S2-BUILDER-AUTHORING"
      }
    }
  }
}

```

### cached opinion text — Wilson v. Layne

```
<opinion type="majority">
<author id="b719-9">CHIEF Justice Rehnquist</author>
<p id="AMm8">delivered the opinion of the Court.</p>
<p id="b719-10">While executing an arrest warrant in a private home, police officers invited representatives of the media to accompany them. We hold that such a “media ride-along” does violate the Fourth Amendment, but that because the state <page-number citation-index="1" label="606">*606</page-number>of the law was not clearly established at the time the search in this ease took place, the officers are entitled to the defense of qualified immunity.</p>
<p id="b720-5">I</p>
<p id="b720-6">In early 1992, the Attorney General of the United States approved “Operation Gunsmoke,” a special national fugitive apprehension program in which United States Marshals worked with state and local police to apprehend dangerous criminals. The “Operation Gunsmoke” policy statement explained that the operation was to concentrate on “armed individuals wanted on federal and/or state and local warrants for serious drug and other violent felonies.” App. 15. This effective program ultimately resulted in over 3,000 arrests in 40 metropolitan areas. Brief for Federal Respondents Layne et al. 2.</p>
<p id="b720-7">One of the dangerous as “Operation Gunsmoke” was Dominic Wilson, the son of petitioners Charles and Geraldine Wilson. Dominic Wilson had violated his probation on previous felony charges of robbery, theft, and assault with intent to rob, and the police computer listed “caution indicators” that he was likely to be armed, to resist arrest, and to “assaul[t] police.” App. 40. The computer also listed his address as 909 North StoneStreet Avenue in Rockville, Maryland. Unknown to the police, this was actually the home of petitioners, Dominic Wilson’s parents. Thus, in April 1992, the Circuit Court for Montgomery County issued three arrest warrants for Dominic Wilson, one for each of his probation violations. The warrants were each addressed to “any duly authorized peace officer,” and commanded such officers to arrest him and bring him “immediately” before the Circuit Court to answer an indictment as to his probation violation. The warrants made no mention of media presence or assistance.<footnotemark>1</footnotemark></p>
<p id="b721-4"><page-number citation-index="1" label="607">*607</page-number>In the early morning hours of April 16,1992, a Gunsmoke team of Deputy United States Marshals and Montgomery County Police officers assembled to execute the Dominie Wilson warrants. The team was accompanied by a reporter and a photographer from the Washington Post, who had been invited by the Marshals to accompany them on their mission as part of a Marshals Service ride-along policy.</p>
<p id="b721-5">At around 6:45 a.m., the officers, with media representatives in tow, entered the dwelling at 909 North StoneStreet Avenue in the Lincoln Park neighborhood of Rockville. Petitioners Charles and Geraldine Wilson were still in bed when they heard the officers enter the home. Petitioner Charles Wilson, dressed only in a pair of briefs, ran into the living room to investigate. Discovering at least five men in street clothes with guns in his living room, he angrily demanded that they state their business, and repeatedly cursed the officers. Believing him to be an angry Dominic Wilson, the officers quickly subdued him on the floor. Geraldine Wilson next entered the living room to investigate, wearing only a nightgown. She observed her husband being restrained by the armed officers.</p>
<p id="b721-6">When their protective sweep was completed, the officers learned that Dominic Wilson was not in the house, and they departed. During the time that the officers were in the home, the Washington Post photographer took numerous pictures. The print reporter was also apparently in the living room observing the confrontation between the police and <page-number citation-index="1" label="608">*608</page-number>Charles Wilson. At no time, however, were the reporters involved in the execution of the arrest warrant. Brief for Federal Respondents Layne et al. 4. The Washington Post never published its photographs of the incident.</p>
<p id="b722-5">Petitioners sued the law enforcement personal capacities for money damages under <em>Bivens </em>v. <em>Six Unknown Fed. Narcotics Agents, </em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">403 U. S. 388</a></span> (1971) (the U. S. Marshals Service respondents), and Rev. Stat. §1979, <span class="citation no-link">42 U. S. C. § 1983</span> (the Montgomery County Sheriff’s Department respondents). They contended that the officers’ actions in bringing members of the media to observe and record the attempted execution of the arrest warrant violated their Fourth Amendment rights. The District Court denied respondents’ motion for summary judgment on the basis of qualified immunity.</p>
<p id="b722-6">On interlocutory appeal to the Court of Appeals, a panel reversed and held that respondents were entitled to qualified immunity. The case was twice reheard en banc, where a divided Court of Appeals again upheld the defense of qualified immunity. The Court of Appeals declined to decide whether the actions of the police violated the Fourth Amendment. It concluded instead that because no court had held (at the time of the search) that media presence during a police entry into a residence violated the Fourth Amendment, the right allegedly violated by respondents was not “clearly established” and thus qualified immunity was proper. <span class="citation multiple-matches"><a href="/c/F.%203d/141/111/">141 F. 3d 111</a></span> (CA4 1998). Five judges dissented, arguing that the officers’ actions did violate the Fourth Amendment, and that the clearly established protections of the Fourth Amendment were violated in this case. <em>Id., </em>at 119 (opinion of Murnaghan, J.)</p>
<p id="b722-7">Recognizing a split <em>among </em>the Circuits on we granted certiorari in this case and another raising the same question, <em>Hanlon </em>v. <em>Berger, </em><span class="citation" data-id="9174292"><a href="/opinion/9179569/hanlon-v-berger/" aria-description="Citation for case: Hanlon v. Berger">525 U. S. 981</a></span> (1998), and now affirm the Court of Appeals, although by different reasoning.</p>
<p id="b723-8"><page-number citation-index="1" label="609">*609</page-number>I — H</p>
<p id="b723-3">Petitioners sued the federal officials under <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>and the state officials under §1983. Both <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span> </em>and §1983 allow a plaintiff to seek money damages from government officials who have violated his Fourth Amendment rights. See § 1983; <span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/#397" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of..."><em>Bivens, supra, </em>at 397</a></span>. But government officials performing discretionary functions generally are granted a qualified immunity and are “shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow </em>v. <em>Fitzgerald, </em><span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#818" aria-description="Citation for case: Harlow v. Fitzgerald">457 U. S. 800, 818</a></span> (1982).</p>
<p id="b723-4">Although this case involves suits under both §1983 and <em><span class="citation" data-id="9883113"><a href="/opinion/108375/bivens-v-six-unknown-named-agents-of-federal-bureau-of-narcotics/" aria-description="Citation for case: Bivens v. Six Unknown Named Agents of Federal Bureau of...">Bivens</a></span>, </em>the qualified immunity analysis is identical under either cause of action. See, <em>e.g., Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#394" aria-description="Citation for case: Graham v. Connor">490 U. S. 386, 394, n. 9</a></span> (1989); <em>Malley </em>v. <em>Briggs, </em><span class="citation" data-id="9430379"><a href="/opinion/111611/malley-v-briggs/#340" aria-description="Citation for case: Malley v. Briggs">475 U. S. 335, 340, n. 2</a></span> (1986). A court evaluating a claim of qualified immunity “must first determine whether the plaintiff has alleged the deprivation of an actual constitutional right at all, and if so, proceed to determine whether that right was clearly established at the time of the alleged violation.” <em>Conn </em>v. <em>Gabbert, ante, </em>at 290. This order of procedure is designed to “spare a defendant not only unwarranted liability, but unwarranted demands customarily imposed upon those defending a long drawn out lawsuit.” <em>Siegert </em>v. <em>Gilley, </em><span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/#232" aria-description="Citation for case: Siegert v. Gilley">500 U. S. 226, 232</a></span> (1991). Deciding the constitutional question before addressing the qualified immunity question also promotes clarity in the legal standards for official conduct, to the benefit of both the officers and the general public. See <em>County of Sacramento </em>v. <em>Lewis, </em><span class="citation" data-id="9433650"><a href="/opinion/118214/county-of-sacramento-v-lewis/#840" aria-description="Citation for case: County of Sacramento v. Lewis">523 U. S. 833, 840-842, n. 5</a></span> (1998). We now turn to the Fourth Amendment question.</p>
<p id="b723-5">In 1604, an English court made the now-famous observation that “the house of every one is to him as his castle and fortress, as well for his defence against injury and violence, as for his repose.” <em>Semayne’s Case, </em>5 Co. Rep. 91a, 91b, 77 <page-number citation-index="1" label="610">*610</page-number>Eng. Rep. 194, 195 (K. B.). In his Commentaries on the Laws of England, William Blaekstone noted that</p>
<blockquote id="b724-5">“the law of England has so particular and tender a regal’d to the immunity of a man’s house, that it stiles it his castle, and will never suffer it to be violated with impunity: agreeing herein with the sentiments of antient Rome .... For this reason no doors can in general be broken open to execute any civil process; though, in criminal causes, the public safety supersedes the private.” 4 Commentaries 223 (1765-1769).</blockquote>
<p id="b724-6">The Fourth Amendment embodies this centuries-old principle of respect for the privacy of the home: “The right of the people to be secure in their persons, <em>houses, </em>papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.” U. S. Const., Arndt. 4 (emphasis added). See also <em>United States </em>v. <em>United States Dist. Court for Eastern Dist. of Mich., </em><span class="citation" data-id="9424952"><a href="/opinion/108581/united-states-v-united-states-district-court-for-the-eastern-district-of/#313" aria-description="Citation for case: United States v. United States District Court for the...">407 U. S. 297, 313</a></span> (1972) (“[FJhysical entry of the home is the chief evil against which the wording of the Fourth Amendment is directed”).</p>
<p id="b724-7">Our decisions have applied these basic principles Fourth Amendment to situations, like the one in this case, in which police enter a home under the authority of an arrest warrant in order to take into custody the suspect named in the warrant. In <em>Payton </em>v. <em>New York, </em><span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#602" aria-description="Citation for case: Payton v. New York">445 U. S. 573, 602</a></span> (1980), we noted that although clear in its protection of the home, the common-law tradition at the time of the drafting of the Fourth Amendment was ambivalent on the question whether police could enter a home without a warrant. We were ultimately persuaded that the “overriding respect for the sanctity of the home that has been embedded in our traditions since the origins of the Republic” meant that absent a warrant or exigent circumstances, police could not <page-number citation-index="1" label="611">*611</page-number>enter a home to make an arrest. <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#601" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 601</a></span>, 603-604: We decided that “an arrest warrant founded on probable cause implicitly carries with it the limited authority to enter a dwelling in which the suspect lives when there is reason to believe the suspect is within.” <span class="citation" data-id="9427853"><a href="/opinion/110235/payton-v-new-york/#603" aria-description="Citation for case: Payton v. New York"><em>Id., </em>at 603</a></span>.</p>
<p id="b725-4">Here, of course, the officers had such a warrant, and they were undoubtedly entitled to enter the Wilson home in order to execute the arrest warrant for Dominic Wilson. But it does not necessarily follow that they were entitled to bring a newspaper reporter and a photographer with them. In <em>Horton </em>v. <em>California, </em><span class="citation" data-id="9432041"><a href="/opinion/112448/horton-v-california/#140" aria-description="Citation for case: Horton v. California">496 U. S. 128, 140</a></span> (1990), we held “[i]f the scope of the search exceeds that permitted by the terms of a validly issued warrant or the character of the relevant exception from the warrant requirement, the subsequent seizure is unconstitutional without more.” While this does not mean that every police action while inside a home must be explicitly authorized by the text of the warrant, see <em>Michigan </em>v. <em>Summers, </em><span class="citation" data-id="9428436"><a href="/opinion/110534/michigan-v-summers/#705" aria-description="Citation for case: Michigan v. Summers">452 U. S. 692, 705</a></span> (1981) (Fourth Amendment allows temporary detainer of homeowner while police search the home pursuant to warrant), the Fourth Amendment does require that police actions in execution of a warrant be related to the objectives of the authorized intrusion, see <em>Arizona </em>v. <em>Hicks, </em><span class="citation" data-id="9430865"><a href="/opinion/111834/arizona-v-hicks/#325" aria-description="Citation for case: Arizona v. Hicks">480 U. S. 321, 325</a></span> (1987). See also <em>Maryland </em>v. <em>Garrison, </em><span class="citation" data-id="9430836"><a href="/opinion/111823/maryland-v-garrison/#87" aria-description="Citation for case: Maryland v. Garrison">480 U. S. 79, 87</a></span> (1987) (“[T]he purposes justifying a police search strictly limit the permissible extent of the search”).</p>
<p id="b725-5">Certainly the presence of reporters inside the home was not related to the objectives of the authorized intrusion. Respondents concede that the reporters did not engage in the execution of the warrant, and did not assist the police in their task. The reporters therefore were not present for any reason related to the justification for police entry into the home — the apprehension of Dominic Wilson.</p>
<p id="b725-6">This is not a case in which the presence of the third parties directly aided in the execution of the warrant. Where the police enter a home under the authority of a warrant to <page-number citation-index="1" label="612">*612</page-number>search for stolen property, the presence of third parties for the purpose of identifying the stolen property has long been approved by this Court and our common-law tradition. See, <em>e. g., Entick </em>v. <em>Carrington, </em>19 How. St. Tr. 1029, 1067 (K. B. 1765) (in search for stolen goods ease, “Tt]he owner must swear that the goods are lodged in such a place. He must attend at the execution of the warrant to shew them to the officer, who must see that they answer the description”) (quoted with approval in <em>Boyd </em>v. <em>United States, </em><span class="citation" data-id="9417418"><a href="/opinion/91573/boyd-v-united-states/#628" aria-description="Citation for case: Boyd v. United States">116 U. S. 616, 628</a></span> (1886)).</p>
<p id="b726-5">Respondents argue presence Post reporters in the Wilsons’ home nonetheless served a number of legitimate law enforcement purposes. They first assert that officers should be able to exercise reasonable discretion about when it would “further their law enforcement mission to permit members of the news media to accompany them in executing a warrant.” Brief for Federal Respondents Layne et al. 15. But this claim ignores the importance of the right of residential privacy at the core of the Fourth Amendment. It may well be that media ride-alongs further the law enforcement objectives of the police in a general sense, but that is not the same as furthering the purposes of the search. Were such generalized “law enforcement objectives” themselves sufficient to trump the Fourth Amendment, the protections guaranteed by that Amendment’s text would be significantly watered down.</p>
<p id="b726-6">Respondents next argue presence could serve the law enforcement purpose of publicizing the government’s efforts to combat crime, and facilitate accurate reporting on law enforcement activities. There is certainly language in our opinions interpreting the First Amendment which points to the importance of “the press” in informing the general public about the administration of criminal justice. In <em>Cox Broadcasting Corp. </em>v. <em>Cohn, </em><span class="citation" data-id="9426016"><a href="/opinion/109207/cox-broadcasting-corp-v-cohn/#491" aria-description="Citation for case: Cox Broadcasting Corp. v. Cohn">420 U. S. 469, 491-492</a></span> (1975), for example, we said “in a society in which each individual has but limited time and resources with which to <page-number citation-index="1" label="613">*613</page-number>observe at first hand the operations of his government, he relies necessarily upon the press to bring to him in convenient form the facts of those operations.” See also <em>Richmond Newspapers, Inc. </em>v. <em>Virginia, </em><span class="citation" data-id="9428077"><a href="/opinion/110339/richmond-newspapers-inc-v-virginia/#572" aria-description="Citation for case: Richmond Newspapers, Inc. v. Virginia">448 U. S. 555, 572-573</a></span> (1980). No one could gainsay the truth of these observations, or the importance of the First Amendment in protecting press freedom from abridgment by the government. But the Fourth Amendment also protects a very important right, and in the present case it is in terms of that right that the media ride-alongs must be judged.</p>
<p id="b727-5">Surely the possibility of good public relations for the police is simply not enough, standing alone, to justify the ride-along intrusion into a private home. And even the need for accurate reporting on police issues in general bears no direct relation to the constitutional justification for the police intrusion into a home in order to execute a felony arrest warrant.</p>
<p id="b727-6">Finally, respondents argue that the presence of third parties could serve in some situations to minimize police abuses and protect suspects, and also to protect the safety of the officers. While it might be reasonable for police officers to themselves videotape home entries as part of a “quality control” effort to ensure that the rights of homeowners are being respected, or even to preserve evidence, cf. <em>Ohio </em>v. <em>Robinette, </em><span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#35" aria-description="Citation for case: Ohio v. Robinette">519 U.S. 33, 35</a></span> (1996) (noting the use of a “mounted video camera” to record the details of a routine traffic stop), such a situation is significantly different from the media presence in this case. The Washington Post reporters in the Wilsons’ home were working on a story for their own purposes. They were not present for the purpose of protecting the officers, much less the Wilsons. A private photographer was acting for private purposes, as evidenced in part by the fact that the newspaper and not the police retained the photographs. Thus, although the presence of third parties during the execution of a warrant may in some circumstances be constitutionally permissible, see supra, at 611-612, the presence of these third parties was not.</p>
<p id="b728-6"><page-number citation-index="1" label="614">*614</page-number>The reasons advanced by respondents, taken in their entirety, fall short of justifying the presence of media inside a home. We hold that it is a violation of the Fourth Amendment for police to bring members of the media or other third parties into a home during the execution of a warrant when the presence of the third parties in the home was not in aid of the execution of the warrant.<footnotemark>2</footnotemark></p>
<p id="b728-7">HH</p>
<p id="b728-1">Since the police action in this ease violated petitioners Fourth Amendment right, we now must decide whether this right was clearly established at the time of the search. See <span class="citation" data-id="9432276"><a href="/opinion/112594/siegert-v-gilley/#232" aria-description="Citation for case: Siegert v. Gilley"><em>Siegert, 500 </em>U. S., at 232-233</a></span>. As noted above, Part II, <em>supra, </em>government officials performing discretionary functions generally are granted a qualified immunity and are “shielded from liability for civil damages insofar as their conduct does not violate clearly established statutory or constitutional rights of which a reasonable person would have known.” <em>Harlow </em>v. <em>Fitzgerald, 457 </em>U. S., at 818. What this means in practice is that “whether an official protected by qualified immunity may be held personally liable for an allegedly unlawful official action generally turns on the ‘objective legal reasonableness’ of the action, assessed in light of the legal rules that were ‘clearly established’ at the time it was taken.” <em>Anderson </em>v. <em>Creighton, </em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton">483 U. S. 635, 639</a></span> (1987) (citing <span class="citation" data-id="9428863"><a href="/opinion/110763/harlow-v-fitzgerald/#819" aria-description="Citation for case: Harlow v. Fitzgerald"><em>Harlow, supra, </em>at 819</a></span>); see also <em>Graham </em>v. <em>Connor, </em><span class="citation" data-id="9431666"><a href="/opinion/112257/graham-v-connor/#397" aria-description="Citation for case: Graham v. Connor">490 U. S., at 397</a></span>.</p>
<p id="b728-2">In <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Anderson</a></span>, </em>we explained that what “clearly established” means in this context depends largely “upon the level of generality at which the relevant ‘legal rule’ is to be identified.” <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#639" aria-description="Citation for case: Anderson v. Creighton">483 U. S., at 639</a></span>. “[Cjlearly established” for purposes of <page-number citation-index="1" label="615">*615</page-number>qualified immunity means that “[t]he contours of the right must be sufficiently clear that a reasonable official would understand that what he is doing violates that right. This is not to say that an official action is protected by qualified immunity unless the very action in question has previously been held unlawful, but it is to say that in the light of preexisting law the unlawfulness must be apparent.” <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#640" aria-description="Citation for case: Anderson v. Creighton"><em>Id., </em>at 640</a></span> (citations omitted); see also <em>United States </em>v. <em>Lanier, </em><span class="citation" data-id="118098"><a href="/opinion/118098/united-states-v-lanier/#270" aria-description="Citation for case: United States v. Lanier">520 U. S. 259, 270</a></span> (1997).</p>
<p id="b729-5">It could plausibly be asserted that any violation of the Fourth Amendment is “clearly established,” since it is clearly established that the protections of the Fourth Amendment apply to the actions of police. Some variation of this theory of qualified immunity is urged upon us by petitioners, Brief for Petitioners 37, and seems to have been at the core of the dissenting opinion in the Court of Appeals, see 141 F. 3d, at 123. However, as we explained in <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">Anderson</a></span>, </em>the right allegedly violated must be defined at the appropriate level of specificity before a court can determine if it was clearly established. <span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/#641" aria-description="Citation for case: Anderson v. Creighton">483 U. S., at 641</a></span>. In this case, the appropriate question is the objective inquiry whether a reasonable officer could have believed that bringing members of the media into a home during the execution of an arrest warrant was lawful, in light of clearly established law and the information the officers possessed. Cf. <em><span class="citation" data-id="9431119"><a href="/opinion/111953/anderson-v-creighton/" aria-description="Citation for case: Anderson v. Creighton">ibid.</a></span></em></p>
<p id="b729-6">a police officer in April 1992 to have believed that bringing media observers along during the execution of an arrest warrant (even in a home) was lawful. First, the constitutional question presented by this ease is by no means open and shut. The Fourth Amendment protects the rights of homeowners from entry without a warrant, but there was a warrant here. The question is whether the invitation to the media exceeded the scope of the search authorized by the warrant. Accurate media coverage of police activities serves an important public purpose, and it is not obvious from the general principles <page-number citation-index="1" label="616">*616</page-number>of the Fourth Amendment that the conduct of the officers in this case violated the Amendment.</p>
<p id="b730-5">Second, although media ride-alongs one had apparently become a common police practice,<footnotemark>3</footnotemark> in 1992 there were no judicial opinions holding that this practice became unlawful when it entered a home. The only published decision directly on point was a state intermediate court decision which, though it did not engage in an extensive Fourth Amendment analysis, nonetheless held that such conduct was not unreasonable. <em>Prahl </em>v. <em>Brosamle, </em><span class="citation" data-id="2178204"><a href="/opinion/2178204/bruheim-v-little/" aria-description="Citation for case: Bruheim v. Little">98 Wis. 2d 180</a></span>, 154—155, <span class="citation" data-id="2178648"><a href="/opinion/2178648/prahl-v-brosamle/#782" aria-description="Citation for case: Prahl v. Brosamle">295 N. W. 2d 768, 782</a></span> (App. 1980). From the federal courts, the parties have only identified two unpublished District Court decisions dealing with media entry into homes, each of which upheld the search on unorthodox non-Fourth Amendment right to privacy theories. <em>Moncrief </em>v. <em>Hanton, </em>10 Media L. Rptr. 1620 (ND <span class="citation" data-id="9433390"><a href="/opinion/118066/ohio-v-robinette/#1984" aria-description="Citation for case: Ohio v. Robinette">Ohio 1984</a></span>); <em>Higbee </em>v. <em>Times-Advocate, </em>5 Media L. Rptr. 2372 (SD Cal. 1980). These cases, of course, cannot “clearly establish” that media entry into homes during a police ride-along violates the Fourth Amendment.</p>
<p id="b730-6">At a slightly higher level of <em>Bills </em>v. <em>Aseltine, </em><span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine">958 F. 2d 697</a></span> (CA6 1992), in which the Court of Appeals for the Sixth Circuit held that there were material issues of fact precluding summary judgment on the question whether police exceeded the scope of a search warrant by allowing a private security guard to participate in the search to identify stolen property other than that described in the warrant. <span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/#709" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine"><em>Id., </em>at 709</a></span>. <em><span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine">Bills</a></span>, </em>which was decided a mere five weeks before the events of this case, did anticipate today's holding that police may not bring along third parties during an entry into a private home pursuant <page-number citation-index="1" label="617">*617</page-number>to a warrant for purposes unrelated to those justifying the warrant. <span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/#706" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine"><em>Id., </em>at 706</a></span>. However, we cannot say that even in light of <em><span class="citation" data-id="579234"><a href="/opinion/579234/lorraine-i-bills-v-dennis-w-aseltine/" aria-description="Citation for case: Lorraine I. Bills v. Dennis W. Aseltine">Bills</a></span>, </em>the law on third-party entry into homes was clearly established in April 1992. Petitioners have not brought to our attention any eases of controlling authority in their jurisdiction at the time of the incident that clearly established the rule on which they seek to rely, nor have they identified a consensus of eases of persuasive authority such that a reasonable officer could not have believed that his actions were lawful.</p>
<p id="b731-5">Finally, important to our conclusion was the reliance by the United States marshals in this case on a Marshals Service ride-along policy that explicitly contemplated that media who engaged in ride-alongs might enter private homes with their cameras as part of fugitive apprehension arrests.<footnotemark>4</footnotemark> The Montgomery County Sheriff’s Department also at this time had a ride-along program that did not expressly prohibit media entry into private homes. Deposition of Sheriff Raymond M. Eight, in No. PJM-94-1718, p. 8. Such a policy, of course, could not make reasonable a belief that was contrary to a decided body of case law. But here the state of the law as to third parties accompanying police on home entries was at best undeveloped, and it was not unreasonable for law enforcement officers to look and rely on their formal ride-along policies.</p>
<p id="b731-6">Given such an undeveloped state of the law, the officers in this case cannot have been “expected to predict the future course of constitutional law.” <em>Procunier </em>v. <em>Navarette, </em><span class="citation" data-id="9427054"><a href="/opinion/109776/procunier-v-navarette/#562" aria-description="Citation for case: Procunier v. Navarette">434 <page-number citation-index="1" label="618">*618</page-number>U. S. 555, 562</a></span> (1978). See also <em>Wood </em>v. Strickland, <span class="citation" data-id="9426006"><a href="/opinion/109199/wood-v-strickland/#321" aria-description="Citation for case: Wood v. Strickland">420 U. S. 308, 321</a></span> (1975); <em>Pierson </em>v. <em>Ray, </em><span class="citation" data-id="9423382"><a href="/opinion/107411/pierson-v-ray/#557" aria-description="Citation for case: Pierson v. Ray">386 U. S. 547, 557</a></span> (1967). Between the time of the events of this case and today’s decision, a split among the Federal Circuits in fact developed on the question whether media ride-alongs that enter homes subject the police to <em>money </em>damages. See 141 F. 3d, at 118-119; <em>Ayeni </em>v. <em>Mottola, </em><span class="citation" data-id="678500"><a href="/opinion/678500/tawa-ayeni-v-james-mottola/" aria-description="Citation for case: Tawa Ayeni v. James Mottola">35 F. 3d 680</a></span> (CA2 1994), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./514/1062/">514 U. S. 1062</a></span> (1995); <em>Parker </em>v. <em>Boyer, </em><span class="citation multiple-matches"><a href="/c/F.%203d/93/445/">93 F. 3d 445</a></span> (CA8 1996), cert. denied, <span class="citation multiple-matches"><a href="/c/U.%20S./519/1148/">519 U. S. 1148</a></span> (1997); <em>Berger </em>v. <em>Hanlon, </em><span class="citation" data-id="6959019"><a href="/opinion/7055408/berger-v-hanlon/" aria-description="Citation for case: Berger v. Hanlon">129 F. 3d 505</a></span> (CA9 1997), cert. granted, <span class="citation multiple-matches"><a href="/c/U.%20S./525/981/">525 U. S. 981</a></span> (1998). If judges thus disagree on a constitutional question, it is unfair to subject police to money damages for picking the losing side of the controversy.</p>
<p id="b732-5">For the foregoing reasons,</p>
<p id="AoRV">Appeals is affirmed.</p>
<p id="b732-6">
<em>It is so ordered.</em>
</p>
<footnote label="1">
<p id="b720-8"> The warrants were identical in all relevant respects. By way of example, one of them read as follows:</p>
<p id="b721-7"><page-number citation-index="1" label="607">*607</page-number>“The State of Maryland, to any duly authorized peace officer, greeting: you are hereby commanded to take Dominic Jerome Wilson if he/she shall be found in your bailiwick, and have him immediately before the Circuit Court for Montgomery County, now in session, at the Judicial Center, in Rockville, to answer an indictment, or information, or criminal appeals unto the State of Maryland, of and concerning a certain charge of Robbery [Violation of Probation] by him committed, as hath been presented, and so forth. Hereof fail not at your peril, and have you then and there this writ. Witness.” App. 36-37.</p>
</footnote>
<footnote label="2">
<p id="b728-3"> Even though such actions might violate the Fourth Amendment, if the police are lawfully present, the violation of the Fourth Amendment is the presence of the media and not the presence of the police in the home. We have no occasion here to decide whether the exclusionary rule would apply to any evidence discovered or developed by the media representatives.</p>
</footnote>
<footnote label="3">
<p id="b730-7"> See, <em>e. g., Florida Publishing Co. </em>v. <em>Fletcher, </em><span class="citation" data-id="1769461"><a href="/opinion/1769461/florida-pub-co-v-fletcher/#919" aria-description="Citation for case: Florida Pub. Co. v. Fletcher">340 So. 2d 914, 919</a></span> (1976) (it '“is a widespread practice of long-standing’” for media to accompany officers into homes), cert, denied, <span class="citation multiple-matches"><a href="/c/U.%20S./431/930/">431 U. S. 930</a></span> (1977); Zoglin, Live on the “Vice Beat, Time, Dec. 22, 1986, p. 60 (noting “the increasingly common practice of letting TV crews tag along on drug raids”).</p>
</footnote>
<footnote label="4">
<p id="b731-7"> A booklet distributed to marshals recommended that “fugitive apprehension cases . . . normally offer the best possibilities for ride-alongs.” App. 4-5. In its discussion of the best way to make ride-alongs useful to the media and portray the Marshals Service in a favorable light, the booklet noted that reporters were likely to want to be able to shoot “good action footage, not just a mop-up scene.” It advised agents that “[i]f the arrest is planned to take place inside a house or building, agree ahead of time on when the camera can enter and who will give the signal.” <em>Id., </em>at 7.</p>
</footnote>
</opinion>
```

---
